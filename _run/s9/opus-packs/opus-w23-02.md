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

## GROUP: _overhaul2/lake/cases/hunter-v-bryant--112671.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "660de908f943db08", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "hunter-v-bryant--112671"}, "payload": {"all": [{"cite": "502 U.S. 224", "page": "224", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "502"}, {"cite": "112 S. Ct. 534", "page": "534", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "112"}, {"cite": "116 L. Ed. 2d 589", "page": "589", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "116"}, {"cite": "1991 U.S. LEXIS 7262", "page": "7262", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1991"}], "display": null, "official": null, "official_selection_present": false, "record_id": "hunter-v-bryant--112671"}}
{"assertion_id": "ea9c3dc19cc4bebf", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "hunter-v-bryant--112671"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "hunter-v-bryant--112671", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — hunter-v-bryant--112671

```json
{
  "schema_version": "s2.v1",
  "record_id": "hunter-v-bryant--112671",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Hunter v. Bryant",
    "case_name_short": "Hunter",
    "case_name_full": "HUNTER Et Al. v. BRYANT",
    "input_case_name": "Hunter v. Bryant",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1991-12-16",
    "year": 1991,
    "docket": null,
    "cluster_id": 112671,
    "lead_opinion_id": 9432435,
    "sibling_ids": [],
    "absolute_url": "/opinion/112671/hunter-v-bryant/",
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
        "cite": "502 U.S. 224",
        "volume": "502",
        "reporter": "U.S.",
        "page": "224",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "112 S. Ct. 534",
        "volume": "112",
        "reporter": "S. Ct.",
        "page": "534",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "116 L. Ed. 2d 589",
        "volume": "116",
        "reporter": "L. Ed. 2d",
        "page": "589",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1991 U.S. LEXIS 7262",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "7262",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "502 U.S. 224",
        "volume": "502",
        "reporter": "U.S.",
        "page": "224",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "112 S. Ct. 534",
        "volume": "112",
        "reporter": "S. Ct.",
        "page": "534",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "116 L. Ed. 2d 589",
        "volume": "116",
        "reporter": "L. Ed. 2d",
        "page": "589",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 U.S. LEXIS 7262",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "7262",
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
    "date_created": "2026-07-06T13:51:33Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:51:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:51:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:51:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:51:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — hunter-v-bryant--112671

```
<opinion type="majority">
<author id="b384-10">Per Curiam.</author>
<p id="b384-11">On May 3,1985, respondent James V. Bryant delivered two photocopies of a handwritten letter to two administrative <page-number citation-index="1" label="225">*225</page-number>offices at the University of Southern California. The rambling letter referred to a plot to assassinate President Ronald Reagan by “Mr Image,” who was described as “Communist white men within the 'National Council of Churches.’” The letter stated that “Mr Image wants to murder President Reagan on his up and coming trip to Germany,” that “Mr Image had conspired with a large number of U. S. officials in the plot to murder President Reagan” and others, and that “Mr Image (NCC) still plans on murdering the President on his trip to Germany in May, 1985.” See <em>Bryant </em>v. <em>United States Treasury Department, Secret Service, </em><span class="citation" data-id="9480344"><a href="/opinion/541812/james-v-bryant-jr-v-united-states-treasury-department-secret-service/#724" aria-description="Citation for case: James v. Bryant, Jr. v. United States Treasury...">903 F. 2d 717, 724-727</a></span> (CA9 1990) (Bryant’s letter). President Reagan was traveling in Germany at the time.</p>
<p id="b385-5">A campus police sergeant telephoned the Secret Service, and agent Brian Hunter responded to the call. After reading the letter, agent Hunter interviewed university employees. One identified James Bryant as the man who had delivered the letter and reported that Bryant had “told her ‘[h]e should have been assassinated in Bonn.’” Another employee said that the man who delivered the letter made statements about “'bloody coups’” and “‘assassination,’” and said something about “ ‘across the throat’ ” while moving his hand horizontally across his throat to simulate a cutting action. <span class="citation" data-id="9480344"><a href="/opinion/541812/james-v-bryant-jr-v-united-states-treasury-department-secret-service/#718" aria-description="Citation for case: James v. Bryant, Jr. v. United States Treasury..."><em>Id., </em>at 718-719</a></span>.</p>
<p id="b385-6">Hunter and another Secret Service agent, Jeffrey Jordan, then visited a local address that appeared on the letter. Bryant came to the door and gave the agents permission to enter. He admitted writing and delivering the letter, but refused to identify “Mr. Image” and answered questions about “Mr. Image” in a rambling fashion. Bryant gave Hunter permission to search the apartment, and the agent found the original of the letter. While the search was underway, Jordan continued questioning Bryant, who refused to answer questions about his feelings toward the President or to state whether he intended to harm the President. <span class="citation" data-id="9480344"><a href="/opinion/541812/james-v-bryant-jr-v-united-states-treasury-department-secret-service/#719" aria-description="Citation for case: James v. Bryant, Jr. v. United States Treasury..."><em>Id., </em>at 719</a></span>.</p>
<p id="b386-4"><page-number citation-index="1" label="226">*226</page-number>Hunter and Jordan arrested Bryant for making threats against the President, in violation of <span class="citation no-link">18 U. S. C. § 871</span>(a).<footnotemark>*</footnotemark> Bryant was arraigned and held without bond until May 17, 1985, when the criminal complaint was dismissed on the Government’s motion.</p>
<p id="b386-5">Bryant subsequently sued agents Hunter and Jordan, the United States Department of the Treasury, and the Director of the Secret Service, seeking recovery under the Federal Tort Claims Act and alleging that the agents had violated his rights under the Fourth, Fifth, Sixth, and Fourteenth Amendments. See <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971). The District Court dismissed all defendants other than agents Hunter and Jordan and all causes of action other than Bryant’s Fourth Amendment claims for arrest without probable cause and without a warrant. The court denied the agents’ motion for summary judgment on qualified immunity grounds.</p>
<p id="b386-6">On appeal, a Ninth Circuit panel held that the agents were entitled to qualified immunity for arresting Bryant without a warrant because, at that time, the warrant requirement was not clearly established for situations in which the ar-restee had consented to the agents’ entry into a residence. <span class="citation" data-id="9480344"><a href="/opinion/541812/james-v-bryant-jr-v-united-states-treasury-department-secret-service/#723" aria-description="Citation for case: James v. Bryant, Jr. v. United States Treasury...">903 F. 2d, at 723-724</a></span>.</p>
<p id="b386-7">However, the panel divided on the question whether the agents were entitled to immunity on the claim that they had <page-number citation-index="1" label="227">*227</page-number>arrested Bryant without probable cause. The majority concluded that the agents had failed to sustain the burden of establishing qualified immunity because their reason for arresting Bryant — their belief that the “Mr. Image” plotting to kill the President in Bryant’s letter could be a pseudonym for Bryant — was not the most reasonable reading of Bryant’s letter:</p>
<blockquote id="b387-5">“Even accepting the ‘alter ego’ theory that by warning what Mr. Image was going to do, Mr. Bryant was in fact communicating what he himself planned to do, the letter read in its entirety does not appear to make a threat against the president. Most of the letter does not even talk about President Reagan. <em>A more reasonable interpretation of the letter might be that Bryant was trying to convince people of the danger Mr. Image and the conspiracy posed rather than that Bryant was speaking through Mr. Image.” Id., </em>at 722 (emphasis added).</blockquote>
<p id="b387-6">Our cases establish that qualified immunity shields agents Hunter and Jordan from suit for damages if “a reasonable officer could have believed [Bryant’s arrest] to be lawful, in light of clearly established law and the information the [arresting] officers possessed.” <em>Anderson </em>v. <em>Creighton, </em><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#641" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635, 641</a></span> (1987). Even law enforcement officials who “reasonably but mistakenly conclude that probable cause is present” are entitled to immunity. <em><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">Ibid.</a></span> </em>Moreover, because “[t]he entitlement is an <em>immunity from suit </em>rather than a mere defense to liability,” <em>Mitchell </em>v. <em>Forsyth, </em><span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/#526" aria-description="Citation for case: Mitchell v. Forsyth">472 U. S. 511, 526</a></span> (1985), we repeatedly have stressed the importance of resolving immunity questions at the earliest possible stage in litigation. See <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 818</a></span> (1982); <em>Davis </em>v. <em>Scherer, </em><span class="citation" data-id="9429708"><a href="/opinion/111241/davis-v-scherer/#195" aria-description="Citation for case: Davis v. Scherer">468 U. S. 183, 195</a></span> (1984); <span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/#526" aria-description="Citation for case: Mitchell v. Forsyth"><em>Mitchell, supra, </em>at 526</a></span>; <em>Malley </em>v. <em>Briggs, </em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#341" aria-description="Citation for case: Malley v. Briggs">475 U. S. 335, 341</a></span> (1986); <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#646" aria-description="Citation for case: Anderson v. Creighton"><em>Anderson, supra, </em>at 646, n. 6</a></span>.</p>
<p id="b387-7">The decision of the Ninth Circuit ignores the import of these decisions. The Court of Appeals’ confusion is evident <page-number citation-index="1" label="228">*228</page-number>from its statement that “[wjhether a reasonable officer could have believed he had probable cause is a question for the trier of fact, and summary judgment' . . . based on lack of probable cause is proper only if there is only one reasonable conclusion a jury could reach.” <span class="citation" data-id="9480344"><a href="/opinion/541812/james-v-bryant-jr-v-united-states-treasury-department-secret-service/#721" aria-description="Citation for case: James v. Bryant, Jr. v. United States Treasury...">903 F. 2d, at 721</a></span>. This statement of law is wrong for two reasons. First, it routinely places the question of immunity in the hands of the jury. Immunity ordinarily should be decided by the court long before trial. See <span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/#527" aria-description="Citation for case: Mitchell v. Forsyth"><em>Mitchell, supra, </em>at 527-529</a></span>. Second, the court should ask whether the agents acted reasonably under settled law in the circumstances, not whether another reasonable, or more reasonable, interpretation of the events can be constructed five years after the fact.</p>
<p id="b388-5">Under settled law, Secret Service Agents Hunter and Jordan are entitled to immunity if a reasonable officer could have believed that probable cause existed to arrest Bryant. Probable cause existed if “at the moment the arrest was made ... the facts and circumstances within their knowledge and of which they had reasonably trustworthy information were sufficient to warrant a prudent man in believing” that Bryant had violated <span class="citation no-link">18 U. S. C. § 871</span>. <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#91" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 91</a></span> (1964).</p>
<p id="b388-6">When Agents Hunter and Jordan arrested Bryant, they possessed trustworthy information that Bryant had written a letter containing references to an assassination scheme directed against the President, that Bryant was cognizant of the President’s whereabouts, that Bryant had made an oral statement that “‘[h]e should have been assassinated in Bonn,’ ” <span class="citation" data-id="9480344"><a href="/opinion/541812/james-v-bryant-jr-v-united-states-treasury-department-secret-service/#719" aria-description="Citation for case: James v. Bryant, Jr. v. United States Treasury...">903 F. 2d, at 719</a></span>, and that Bryant refused to answer questions about whether he intended to harm the President. On the basis of this information, a Magistrate ordered Bryant to be held without bond.</p>
<p id="b388-7">These undisputed facts establish that the Secret Service agents are entitled to qualified immunity. Even if we assumed, <em>arguendo, </em>that they <em>(and </em>the magistrate) erred in concluding that probable cause existed to arrest Bryant, the <page-number citation-index="1" label="229">*229</page-number>agents nevertheless would be entitled to qualified immunity because their decision was reasonable, even if mistaken. <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#641" aria-description="Citation for case: Anderson v. Creighton"><em>Anderson, supra, </em>at 641</a></span>.</p>
<p id="b389-5">The qualified immunity standard “gives ample room for mistaken judgments” by protecting “all but the plainly incompetent or those who knowingly violate the law.” <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#343" aria-description="Citation for case: Malley v. Briggs"><em>Malley, supra, </em>at 343, 341</a></span>. This accommodation for reasonable error exists because “officials should not err always on the side of caution” because they fear being sued. <span class="citation" data-id="9429708"><a href="/opinion/111241/davis-v-scherer/#196" aria-description="Citation for case: Davis v. Scherer"><em>Davis, supra, </em>at 196</a></span>. Our national experience has taught that this principle is nowhere more important than when the specter of Presidential assassination is raised.</p>
<p id="b389-6">The petition for a writ of certiorari is granted, the judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b389-7">
<em>It is so ordered.</em>
</p>
<p id="b389-8">Justice Thomas took no part in the consideration or decision of this case.</p>
<footnote label="*">
<p id="b386-8"> Title <span class="citation no-link">18 U. S. C. § 871</span>(a) provides:</p>
<blockquote id="b386-9">“Whoever knowingly and willfully deposits for conveyance in the mail or for a delivery from any post office or by any letter carrier any letter, paper, writing, print, missive, or document containing any threat to take the life of, to kidnap, or to inflict bodily harm upon the President of the United States, the President-elect, the Vice President or other officer next in the order of succession to the office of President of the United States, or the Vice President-elect, or knowingly and willfully otherwise makes any such threat against the President, President-elect, Vice President or other officer next in the order of succession to the office of President, or Vice President-elect, shall be fined not more than $1,000 or imprisoned not more than five years, or both.”</blockquote>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/illinois-v-fisher--5141053.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "47002802696d3238", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "illinois-v-fisher--5141053"}, "payload": {"all": [{"cite": "860 A.2d 363", "page": "363", "reporter": "A.2d", "selected_official": false, "source": "cluster.citations[]", "type": 3, "volume": "860"}, {"cite": "2004 WL 2445390", "page": "2445390", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2004"}], "display": null, "official": null, "official_selection_present": false, "record_id": "illinois-v-fisher--5141053"}}
{"assertion_id": "56eacd28d974f9ba", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "illinois-v-fisher--5141053"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "illinois-v-fisher--5141053", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — illinois-v-fisher--5141053

```json
{
  "schema_version": "s2.v1",
  "record_id": "illinois-v-fisher--5141053",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Illinois v. Fisher",
    "case_name_short": "Fisher",
    "case_name_full": "Illinois v. Fisher",
    "input_case_name": "Illinois v. Fisher",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-02-23",
    "year": 2004,
    "docket": "No. 03-374",
    "cluster_id": 131160,
    "lead_opinion_id": 9434538,
    "sibling_ids": [
      131160,
      9434538,
      9434539
    ],
    "absolute_url": "/opinion/131160/illinois-v-fisher/",
    "identity_method": "panel-cluster-rekey",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": false,
    "alternates": [
      {
        "cluster_id": 5277866,
        "score": 100,
        "case_name": "In re J.D.P."
      },
      {
        "cluster_id": 2425051,
        "score": 90,
        "case_name": "Kentucky Restaurant Concepts, Inc. v. City of Louisville"
      }
    ],
    "reason_code": "caption_mismatch_accepted_by_docket_number"
  },
  "citations": {
    "official": {
      "cite": "540 U.S. 544",
      "volume": "540",
      "reporter": "U.S.",
      "page": "544",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "124 S. Ct. 1200",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "1200",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 1060",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "1060",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 1412",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "1412",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "540 U.S. 544",
        "volume": "540",
        "reporter": "U.S.",
        "page": "544",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 1200",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "1200",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 1060",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "1060",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 1412",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "1412",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "540 U.S. 544",
    "official_selection": {
      "court_class": "scotus",
      "selected": "540 U.S. 544",
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
    "date_created": "2026-07-06T13:46:26Z",
    "date_modified": "2026-07-09T23:42:50Z",
    "warnings": [
      "input caption does not match CL canonical caption",
      "frontier identity accepted by docket_number rung despite caption mismatch",
      "panel cluster re-key -> cluster 131160 (evidence: S9 F-S9-IDS-001; _run/s9/rekey-targets.jsonl 2026-07-09; In re Mirsky mis-key cluster 5141053 -> Illinois v. Fisher 131160 (540 U.S. 544, per curiam, docket 03-374))"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:47:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:47:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:47:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:47:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — illinois-v-fisher--5141053

```
<opinion type="majority">
<author id="b757-4"><page-number citation-index="1" label="545">*545</page-number>Per Curiam.</author>
<p id="b757-5">The Appellate Court of Illinois held here that the Fourteenth Amendment’s Due Process Clause required the dismissal of criminal charges because the police, acting in good faith and according to normal police procedures, destroyed evidence that respondent had requested more than 10 years earlier in a discovery motion. Petitioner, the State of Illinois, contends that such a result is foreclosed by our decision in <em>Arizona </em>v. <em>Youngblood, </em><span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/" aria-description="Citation for case: Arizona v. Youngblood">488 U. S. 51</a></span> (1988). There we held that “unless a criminal defendant can show bad faith on the part of the police, failure to preserve potentially useful evidence does not constitute a denial of due process of law.” <span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/#58" aria-description="Citation for case: Arizona v. Youngblood"><em>Id., </em>at 58</a></span>. We agree with petitioner, grant the petition for certiorari and respondent’s motion for leave to proceed <em>in forma pauperis, </em>and reverse the judgment of the Appellate Court.</p>
<p id="b757-6">In September 1988, Chicago police arrested respondent in the course of a traffic stop during which police observed him furtively attempting to conceal a plastic bag containing a white powdery substance. Four tests conducted by the Chicago Police Crime Lab and the Illinois State Police Crime Lab confirmed that the bag seized from respondent contained cocaine.</p>
<p id="b757-7">Respondent was charged with possession of cocaine in the Circuit Court of Cook County in October 1988. He filed a motion for discovery eight days later requesting all physical evidence the State intended to use at trial. The State responded that all evidence would be made available at a reasonable time and date upon request. Respondent was released on bond pending trial. In July 1989, however, he failed to appear in court, and the court issued an arrest warrant to secure his presence. Respondent remained a fugitive for over 10 years, apparently settling in Tennessee. The outstanding arrest warrant was finally executed in November 1999, after respondent was detained on an unrelated matter. The State then reinstated the 1988 cocaine-possession charge.</p>
<p id="b758-4"><page-number citation-index="1" label="546">*546</page-number>Before trial, the State informed respondent that in September 1999, the police, acting in accord with established procedures, had destroyed the substance seized from him during his arrest. Respondent thereupon formally requested production of the substance and filed a motion to dismiss the cocaine-possession charge based on the State’s destruction of evidence. The trial court denied the motion, and the ease proceeded to a jury trial. The State introduced evidence tending to prove the facts recounted above. Respondent’s case in chief consisted solely of his own testimony, in which he denied that he ever possessed cocaine and insinuated that the police had “framed” him for the crime. The jury returned a verdict of guilty, and respondent was sentenced to one year of imprisonment.</p>
<p id="b758-5">The Appellate Court reversed the conviction, holding that the Due Process Clause required dismissal of the charge. Relying on the Illinois Supreme Court’s decision in <em>Illinois </em>v. <em>Newberry, </em><span class="citation" data-id="9709314"><a href="/opinion/2065766/people-v-newberry/" aria-description="Citation for case: People v. Newberry">166 Ill. 2d 310</a></span>, <span class="citation" data-id="9709314"><a href="/opinion/2065766/people-v-newberry/" aria-description="Citation for case: People v. Newberry">652 N. E. 2d 288</a></span> (1995), the Appellate Court reasoned:</p>
<blockquote id="b758-6">“ ‘Where evidence is requested by the defense in a discovery motion, the State is on notice that the evidence must be preserved, and the defense is not required to make an independent showing that the evidence has exculpatory value in order to establish a due process violation. If the State proceeds to destroy the evidence, appropriate sanctions may be imposed even if the destruction is inadvertent. No showing of bad faith is necessary.’” App. to Pet. for Cert. 12 (quoting <span class="citation" data-id="9709314"><a href="/opinion/2065766/people-v-newberry/#317" aria-description="Citation for case: People v. Newberry"><em>Newberry, supra, </em>at 317</a></span>, <span class="citation" data-id="9709314"><a href="/opinion/2065766/people-v-newberry/#292" aria-description="Citation for case: People v. Newberry">652 N. E. 2d, at 292</a></span>) (citation omitted in original).</blockquote>
<p id="b758-7">The Appellate Court observed that <em><span class="citation" data-id="9709314"><a href="/opinion/2065766/people-v-newberry/" aria-description="Citation for case: People v. Newberry">Newberry</a></span> </em>distinguished our decision in <em><span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/" aria-description="Citation for case: Arizona v. Youngblood">Youngblood</a></span> </em>on the ground that the police in <em><span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/" aria-description="Citation for case: Arizona v. Youngblood">Youngblood</a></span> </em>did not destroy evidence subsequent to a discovery motion by the defendant. App. to Pet. for Cert. 13. While acknowledging that “there is nothing in the record to <page-number citation-index="1" label="547">*547</page-number>indicate that the alleged cocaine was destroyed in bad faith,” <em>id., </em>at 15, the court further determined that <em><span class="citation" data-id="9709314"><a href="/opinion/2065766/people-v-newberry/" aria-description="Citation for case: People v. Newberry">Newberry</a></span> </em>dictated dismissal because, unlike in <em><span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/" aria-description="Citation for case: Arizona v. Youngblood">Youngblood</a></span>, </em>the destroyed evidence provided respondent’s “only hope for exoneration,” App. to Pet. for Cert. 15, and was “ ‘essential to and determinative of the outcome of the case,”’ App. to Pet. for Cert. 16 (quoting <span class="citation" data-id="9709314"><a href="/opinion/2065766/people-v-newberry/#315" aria-description="Citation for case: People v. Newberry"><em>Newberry, supra, </em>at 315</a></span>, <span class="citation" data-id="9709314"><a href="/opinion/2065766/people-v-newberry/#291" aria-description="Citation for case: People v. Newberry">652 N. E. 2d, at 291</a></span>). Consequently, the court concluded that respondent “was denied due process when he was tried subsequent to the destruction of the alleged cocaine.” App. to Pet. for Cert. 16. The Illinois Supreme Court denied leave to appeal.<footnotemark>*</footnotemark></p>
<p id="b759-5">We have held that when the State suppresses or fails to disclose material exculpatory evidence, the good or bad faith of the prosecution is irrelevant: a due process violation occurs whenever such evidence is withheld. See <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963); <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">427 U. S. 97</a></span> (1976). In <em><span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/" aria-description="Citation for case: Arizona v. Youngblood">Youngblood</a></span>, </em>by contrast, we recognized that the Due Process Clause “requires a different result when we deal with the failure of the State to preserve evidentiary material of which no more can be said than that it could have been subjected to tests, the results of which might have exonerated the defendant.” <span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/#57" aria-description="Citation for case: Arizona v. Youngblood">488 U. S., at 57</a></span>. We concluded that the failure to preserve this “potentially <page-number citation-index="1" label="548">*548</page-number>useful evidence" does not violate due process <em>“unless a criminal defendant can show bad faith on the part of the police.” Id., </em>at 58 (emphasis added).</p>
<p id="b760-5">The substance of “potentially useful evidence” referred to in <em><span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/" aria-description="Citation for case: Arizona v. Youngblood">Youngblood</a></span>, </em>not the material exculpatory evidence addressed in <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>and <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span>. </em>At most, respondent could hope that, had the evidence been preserved, a <em>fifth </em>test conducted on the substance would have exonerated him. See <em>Youngblood, </em><span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/#57" aria-description="Citation for case: Arizona v. Youngblood">488 U. S., at 57</a></span>. But respondent did not allege, nor did the Appellate Court find, that the Chicago police acted in bad faith when they destroyed the substance. Quite the contrary, police testing indicated that the chemical makeup of the substance inculpated, not exculpated, respondent, see <span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/#57" aria-description="Citation for case: Arizona v. Youngblood"><em>id., </em>at 57</a></span>, n., and it is undisputed that police acted in “good faith and in accord with their normal practice,” <span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/#56" aria-description="Citation for case: Arizona v. Youngblood"><em>id., </em>at 56</a></span> (internal quotation marks omitted) (quoting <em>California </em>v. <em>Trombetta, </em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/#488" aria-description="Citation for case: California v. Trombetta">467 U. S. 479, 488</a></span> (1984), in turn quoting <em>Killian </em>v. <em>United States, </em><span class="citation" data-id="9422314"><a href="/opinion/106310/killian-v-united-states/#242" aria-description="Citation for case: Killian v. United States">368 U. S. 231, 242</a></span> (1961)). Under <em><span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/" aria-description="Citation for case: Arizona v. Youngblood">Youngblood</a></span>, </em>then, respondent has failed to establish a due process violation.</p>
<p id="b760-6">We have never held or suggested a pending discovery request eliminates the necessity of showing bad faith on the part of police. Indeed, the result reached in this case demonstrates why such a <em>per se </em>rule would negate the very reason we adopted the bad-faith requirement in the first place: to “limi[t] the extent of the police’s obligation to preserve evidence to reasonable grounds and confin[e] it to that class of cases where the interests of justice most clearly require it.” <span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/#58" aria-description="Citation for case: Arizona v. Youngblood">488 U. S., at 58</a></span>.</p>
<p id="b760-7">We also disagree that <em><span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/" aria-description="Citation for case: Arizona v. Youngblood">Youngblood</a></span> </em>ever the contested evidence provides a defendant’s “only hope for exoneration” and is “ ‘essential to and determinative of the outcome of the case.’” App. to Pet. for Cert. 15-16 (citing <span class="citation" data-id="9709314"><a href="/opinion/2065766/people-v-newberry/#315" aria-description="Citation for case: People v. Newberry"><em>Newberry, supra, </em>at 315</a></span>, <span class="citation" data-id="9709314"><a href="/opinion/2065766/people-v-newberry/#291" aria-description="Citation for case: People v. Newberry">652 N. E. 2d, at 291</a></span>). In <em><span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/" aria-description="Citation for case: Arizona v. Youngblood">Youngblood</a></span>, </em>the Arizona Court of Appeals said that the destroyed evidence “could [have] eliminate^] the defendant <page-number citation-index="1" label="549">*549</page-number>as the perpetrator.” <span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/#54" aria-description="Citation for case: Arizona v. Youngblood">488 U. S., at 54</a></span> (quotation marks and citations omitted). Similarly here, an additional test might have provided the defendant with an opportunity to show that the police tests were mistaken. It is thus difficult to distinguish the two cases on this basis. But in any event, the applicability of the bad-faith' requirement in <em><span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/" aria-description="Citation for case: Arizona v. Youngblood">Youngblood</a></span> </em>depended not on the centrality of the contested evidence to the prosecution’s case or the defendant’s defense, but on the distinction between “material exculpatory” evidence and “potentially useful” evidence. <span class="citation" data-id="9431483"><a href="/opinion/112156/arizona-v-youngblood/#57" aria-description="Citation for case: Arizona v. Youngblood">488 U. S., at 57-58</a></span>. As we have held, <em>supra, </em>at 548, the substance destroyed here was, at best, “potentially useful” evidence, and therefore <em>Young-blood's </em>bad-faith requirement applies.</p>
<p id="b761-5">The judgment of the Appellate Court of Illinois is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b761-6">
<em>It is so ordered.</em>
</p>
<footnote label="*">
<p id="b759-6"> Respondent suggests that we lack jurisdiction because the Appellate Court relied on <em><span class="citation" data-id="9709314"><a href="/opinion/2065766/people-v-newberry/" aria-description="Citation for case: People v. Newberry">Newberry</a></span>, </em>which in turn relied on an adequate and independent state ground. See, <em>e. g., Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1040-1042</a></span> (1983). Respondent is correct that <em><span class="citation" data-id="9709314"><a href="/opinion/2065766/people-v-newberry/" aria-description="Citation for case: People v. Newberry">Newberry</a></span> </em>relied on both the Due Process Clause, and in the alternative, Illinois Supreme Court Rule 415(g)(i) (1990). <span class="citation" data-id="9709314"><a href="/opinion/2065766/people-v-newberry/#314" aria-description="Citation for case: People v. Newberry">166 Ill. 2d, at 314-317</a></span>, <span class="citation" data-id="9709314"><a href="/opinion/2065766/people-v-newberry/#290" aria-description="Citation for case: People v. Newberry">652 N. E. 2d, at 290-292</a></span>. The Appellate Court, however, relied only on the portion of <em><span class="citation" data-id="9709314"><a href="/opinion/2065766/people-v-newberry/" aria-description="Citation for case: People v. Newberry">Newberry</a></span> </em>that addressed due process, and the Appellate Court based its decision solely on the Due Process Clause. Accordingly, we have jurisdiction to review that decision. See, <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1038" aria-description="Citation for case: Michigan v. Long"><em>e. g., Long, supra, </em>at 1038, n. 4</a></span> (“We may review a state case decided on a federal ground even if it is clear that there was an available state ground for decision on which the state court could properly have relied” (citing <em>Beecher </em>v. <em>Alabama, </em><span class="citation" data-id="9423505"><a href="/opinion/107526/beecher-v-alabama/#37" aria-description="Citation for case: Beecher v. Alabama">389 U. S. 35, 37, n. 3</a></span> (1967) <em>(per curiam))).</em></p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/in-re-winship--108111.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1c58617e7be2a530", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "in-re-winship--108111"}, "payload": {"all": [{"cite": "397 U.S. 358", "page": "358", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "397"}, {"cite": "90 S. Ct. 1068", "page": "1068", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "90"}, {"cite": "25 L. Ed. 2d 368", "page": "368", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "25"}, {"cite": "1970 U.S. LEXIS 56", "page": "56", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1970"}], "display": null, "official": null, "official_selection_present": false, "record_id": "in-re-winship--108111"}}
{"assertion_id": "361615e87ebc2fc5", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "in-re-winship--108111"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "in-re-winship--108111", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — in-re-winship--108111

```json
{
  "schema_version": "s2.v1",
  "record_id": "in-re-winship--108111",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "In Re WINSHIP",
    "case_name_short": "In Re Winship",
    "case_name_full": "In Re Winship",
    "input_case_name": "In re Winship",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1970-05-18",
    "year": 1970,
    "docket": null,
    "cluster_id": 108111,
    "lead_opinion_id": 9424220,
    "sibling_ids": [],
    "absolute_url": "/opinion/108111/in-re-winship/",
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
        "cite": "397 U.S. 358",
        "volume": "397",
        "reporter": "U.S.",
        "page": "358",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 S. Ct. 1068",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "1068",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 L. Ed. 2d 368",
        "volume": "25",
        "reporter": "L. Ed. 2d",
        "page": "368",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1970 U.S. LEXIS 56",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "56",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "397 U.S. 358",
        "volume": "397",
        "reporter": "U.S.",
        "page": "358",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 S. Ct. 1068",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "1068",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 L. Ed. 2d 368",
        "volume": "25",
        "reporter": "L. Ed. 2d",
        "page": "368",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1970 U.S. LEXIS 56",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "56",
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
    "date_created": "2026-07-06T13:52:46Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:52:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:52:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:52:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:52:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — in-re-winship--108111

```
<opinion type="majority">
<author id="b460-12">Mr. Justice Brennan</author>
<p id="AzE">delivered the opinion of the Court.</p>
<p id="b460-13">Constitutional questions decided by this Court concerning the juvenile process have centered on the adjudicatory stage at “which a determination is made as to <page-number citation-index="1" label="359">*359</page-number>whether a juvenile is a ‘delinquent’ as a result of alleged misconduct on his part, with the consequence that he may be committed to a state institution.” <em>In re Gault, </em><span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/#13" aria-description="Citation for case: In Re GAULT">387 U. S. 1, 13</a></span> (1967). <em><span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/" aria-description="Citation for case: In Re GAULT">Gault</a></span> </em>decided that, although the Fourteenth Amendment does not require that the hearing at this stage conform with all the requirements of a criminal trial or even of the usual administrative proceeding, the Due Process Clause does require application during the adjudicatory hearing of “ ‘the essentials of due process and fair treatment.’ ” <span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/#30" aria-description="Citation for case: In Re GAULT"><em>Id., </em>at 30</a></span>. This case presents the single, narrow question whether proof beyond a reasonable doubt is among the “essentials of due process and fair treatment” required during the adjudicatory stage when a juvenile is charged with an act which would constitute a crime if committed by an adult.<footnotemark>1</footnotemark></p>
<p id="b461-5">Section 712 of the New York Family Court Act defines a juvenile delinquent as “a person over seven and less than sixteen years of age who does any act which, if done by an adult, would constitute a crime.” During a 1967 adjudicatory hearing, conducted pursuant to § 742 of the Act, a judge in New York Family Court <page-number citation-index="1" label="360">*360</page-number>found that appellant, then a 12-year-old boy, had entered a locker and stolen $112 from a woman’s pocketbook. The petition which charged appellant with delinquency alleged that his act, “if done by an adult, would constitute the crime or crimes of Larceny.” The judge acknowledged that the proof might not establish guilt beyond a reasonable doubt, but rejected appellant’s contention that such proof was required by the Fourteenth Amendment. The judge relied instead on § 744 (b) of the New York Family Court Act which provides that “[a]ny determination at the conclusion of [an adjudicatory] hearing that a [juvenile] did an act or acts must be based on a preponderance of the evidence.”<footnotemark>2</footnotemark> During a subsequent dispositional hearing, appellant was ordered placed in a training school for an initial period of 18 months, subject to annual extensions of his commitment until his 18th birthday — six years in appellant’s case. The Appellate Division of the New York Supreme Court, First Judicial Department, affirmed without opinion, 30 App. Div. 2d 781, 291 N. Y. S. 2d 1005 (1968). The New York Court of Appeals then affirmed by a four-to-three vote, expressly sustaining the constitutionality of § 744 (b), 24 N. Y. 2d 196, <span class="citation" data-id="5524841"><a href="/opinion/5677035/in-re-samuel-w/" aria-description="Citation for case: In re Samuel W.">247 N. E. 2d 253</a></span> (1969).<footnotemark>3</footnotemark> <page-number citation-index="1" label="361">*361</page-number>We noted probable jurisdiction, <span class="citation multiple-matches"><a href="/c/U.%20S./396/885/">396 U. S. 885</a></span> (1969). We reverse.</p>
<p id="b463-5">I</p>
<p id="b463-6">The requirement that guilt of a criminal charge be established by proof beyond a reasonable doubt dates at least from our early years as a Nation. The “demand for a higher degree of persuasion in criminal cases was recurrently expressed from ancient times, [though] its crystallization into the formula ‘beyond a reasonable doubt’ seems to have occurred as late as 1798. It is now accepted in common law jurisdictions as the measure of persuasion by which the prosecution must convince the trier of all the essential elements of guilt.” C. McCormick, Evidence § 321, pp. 681-682 (1954); see also 9 J. Wigmore, Evidence § 2497 (3d ed. 1940). Although virtually unanimous adherence to the reasonable-doubt standard in common-law jurisdictions may not conclusively establish it as a requirement of due process, such adherence does “reflect a profound judgment about the <page-number citation-index="1" label="362">*362</page-number>way in which law should be enforced and justice administered.” <em>Duncan </em>v. <em>Louisiana, </em><span class="citation" data-id="9423691"><a href="/opinion/107685/duncan-v-louisiana/#155" aria-description="Citation for case: Duncan v. Louisiana">391 U. S. 145, 155</a></span> (1968).</p>
<p id="b464-5">Expressions in many opinions of this Court indicate that it has long been assumed that proof of a criminal charge beyond a reasonable doubt is constitutionally required. See, for example, <em>Miles </em>v. <em>United States, </em>103 E. S. 304, 312 (1881); <em>Davis </em>v. <em>United States, </em><span class="citation" data-id="94338"><a href="/opinion/94338/davis-v-united-states/#488" aria-description="Citation for case: Davis v. United States">160 U. S. 469, 488</a></span> (1895); <em>Holt </em>v. <em>United States, </em><span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/#253" aria-description="Citation for case: Holt v. United States">218 U. S. 245, 253</a></span> (1910); <em>Wilson </em>v. <em>United States, </em><span class="citation" data-id="98112"><a href="/opinion/98112/wilson-v-united-states/#569" aria-description="Citation for case: Wilson v. United States">232 U. S. 563, 569-570</a></span> (1914); <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 174</a></span> (1949); <em>Leland </em>v. <em>Oregon, </em><span class="citation" data-id="9420774"><a href="/opinion/105024/leland-v-oregon/#795" aria-description="Citation for case: Leland v. Oregon">343 U. S. 790, 795</a></span> (1952); <em>Holland </em>v. <em>United States, </em><span class="citation" data-id="105254"><a href="/opinion/105254/holland-v-united-states/#138" aria-description="Citation for case: Holland v. United States">348 U. S. 121, 138</a></span> (1954); <em>Speiser </em>v. <em>Randall, </em><span class="citation" data-id="9421696"><a href="/opinion/105751/speiser-v-randall/#525" aria-description="Citation for case: Speiser v. Randall">357 U. S. 513, 525-526</a></span> (1958). Cf. <em>Coffin </em>v. <em>United States, </em><span class="citation" data-id="94110"><a href="/opinion/94110/coffin-v-united-states/" aria-description="Citation for case: Coffin v. United States">156 U. S. 432</a></span> (1895). Mr. Justice Frankfurter stated that “[i]t is the duty of the Government to establish . . . guilt beyond a reasonable doubt. This notion — basic in our law and rightly one of the boasts of a free society — is a requirement and a safeguard of due process of law in the historic, procedural content of ‘due process.' ” <em>Leland </em>v. <span class="citation" data-id="9420774"><a href="/opinion/105024/leland-v-oregon/#802" aria-description="Citation for case: Leland v. Oregon"><em>Oregon, supra, </em>at 802-803</a></span> (dissenting opinion). In a similar vein, the Court said in <em>Brinegar </em>v. <em>United States, supra, </em>at 174, that “[g]uilt in a criminal case must be proved beyond a reasonable doubt and by evidence confined to that which long experience in the common-law tradition, to some extent embodied in the Constitution, has crystallized into rules of evidence consistent with that standard. These rules are historically grounded rights of our system, developed to safeguard men from dubious and unjust convictions, with resulting forfeitures of life, liberty and property.” <em>Davis </em>v. <em>United States, supra, </em>at 488, stated that the requirement is implicit in “constitutions . . . [which] recognize the fundamental principles that are deemed essential for the protection of life and liberty.” In <em><span class="citation" data-id="94338"><a href="/opinion/94338/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">Davis</a></span> </em>a murder conviction was <page-number citation-index="1" label="363">*363</page-number>reversed because the trial judge instructed the jury that it was their duty to convict when the evidence was equally balanced regarding the sanity of the accused. This Court said: “On the contrary, he is entitled to an acquittal of the specific crime charged if upon all the evidence there is reasonable doubt whether he was capable in law of committing crime. ... No man should be deprived of his life under the forms of law unless the jurors who try him are able, upon their consciences, to say that the evidence before them ... is sufficient to show beyond a reasonable doubt the existence of every fact necessary to constitute the crime charged.” <span class="citation" data-id="94338"><a href="/opinion/94338/davis-v-united-states/#484" aria-description="Citation for case: Davis v. United States"><em>Id., </em>at 484, 493</a></span>.</p>
<p id="b465-5">The reasonable-doubt standard plays a vital role in the American scheme of criminal procedure. It is a prime instrument for reducing the risk of convictions resting on factual error. The standard provides concrete substance for the presumption of innocence — that bedrock “axiomatic and elementary” principle whose “enforcement lies at the foundation of the administration of our criminal law.” <em>Coffin </em>v. <em>United States, supra, </em>at 453. As the dissenters in the New York Court of Appeals observed, and we agree, “a person accused of a crime . . . would be at a severe disadvantage, a disadvantage amounting to a lack of fundamental fairness, if he could be adjudged guilty and imprisoned for years on the strength of the same evidence as would suffice in a civil case.” 24 N. Y. 2d, at 205, <span class="citation" data-id="5524841"><a href="/opinion/5677035/in-re-samuel-w/#259" aria-description="Citation for case: In re Samuel W.">247 N. E. 2d, at 259</a></span>.</p>
<p id="b465-6">The requirement of proof beyond a reasonable doubt has this vital role in our criminal procedure for cogent reasons. The accused during a criminal prosecution has at stake interests of immense importance, both because of the possibility that he may lose his liberty upon conviction and because of the certainty that he would be stigmatized by the conviction. Accordingly, a society <page-number citation-index="1" label="364">*364</page-number>that values the good name and freedom of every individual should not condemn a man for commission of a crime when there is reasonable doubt about his guilt. As we said in <em>Speiser </em>v. <em><span class="citation" data-id="9421696"><a href="/opinion/105751/speiser-v-randall/" aria-description="Citation for case: Speiser v. Randall">Randall, supra,</a></span> </em>at 525-526: “There is always in litigation a margin of error, representing error in factfinding, which both parties must take into account. Where one party has at stake an interest of transcending value — as a criminal defendant his liberty — this margin of error is reduced as to him by the process of placing on the other party the burden of . . . persuading the factfinder at the conclusion of the trial of his guilt beyond a reasonable doubt. Due process commands that no man shall lose his liberty unless the Government has borne the burden of . . . convincing the factfinder of his guilt.” To this end, the reasonable-doubt standard is indispensable, for it “impresses on the trier of fact the necessity of reaching a subjective state of certitude of the facts in issue.” Dorsen &amp; Rezneck, In Re Gault and the Future of Juvenile Law, 1 Family Law Quarterly, No. 4, pp. 1, 26 (1967).</p>
<p id="b466-5">Moreover, use of the reasonable-doubt standard is indispensable to command the respect and confidence of the community in applications of the criminal law. It is critical that the moral force of the criminal law not be diluted by a standard of proof that leaves people in doubt whether innocent men are being condemned. It is also important in our free society that every individual going about his ordinary affairs have confidence that his government cannot adjudge him guilty of a criminal offense without convincing a proper factfinder of his guilt with utmost certainty.</p>
<p id="b466-6">Lest there remain any doubt about the constitutional stature of the reasonable-doubt standard, we explicitly hold that the Due Process Clause protects the accused against conviction except upon proof beyond a reasonable doubt of every fact necessary to constitute the crime with which he is charged.</p>
<p id="b467-4"><page-number citation-index="1" label="365">*365</page-number>II</p>
<p id="b467-5">We turn to the question whether juveniles, like adults, are constitutionally entitled to proof beyond a reasonable doubt when they are charged with violation of a criminal law. The same considerations that demand y, extreme caution in factfinding to protect the innocent adult apply as well to the innocent child. We do not find convincing the contrary arguments of thé New York Court of Appeals. <em><span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/" aria-description="Citation for case: In Re GAULT">Gault</a></span> </em>rendered untenable much of the reasoning relied upon by that court to sustain the constitutionality of § 744(b). The Court of Appeals indicated that a delinquency adjudication “is not a ‘conviction’ (§781); that it affects no right or privilege, including the right to hold public office or to obtain a license (§ 782); and a cloak of protective confidentiality is thrown around all the proceedings (§§ 783-784).” 24 N. Y. 2d, at 200, <span class="citation" data-id="5524841"><a href="/opinion/5677035/in-re-samuel-w/#255" aria-description="Citation for case: In re Samuel W.">247 N. E. 2d, at 255-256</a></span>. The court said further: “The delinquency status is not made a crime; and the proceedings are not criminal. There is, hence, no deprivation of due process in the statutory provision [challenged by appellant] . . . .” 24 N. Y. 2d, at 203, <span class="citation" data-id="5524841"><a href="/opinion/5677035/in-re-samuel-w/#257" aria-description="Citation for case: In re Samuel W.">247 N. E. 2d, at 257</a></span>. In effect the Court of Appeals distinguished the proceedings in question here from a criminal prosecution by use of what <em><span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/" aria-description="Citation for case: In Re GAULT">Gault</a></span> </em>called the “ ‘civil’ label-of-convenience which has been attached to juvenile proceedings.” <span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/#50" aria-description="Citation for case: In Re GAULT">387 U. S., at 50</a></span>. But <em><span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/" aria-description="Citation for case: In Re GAULT">Gault</a></span> </em>expressly rejected that distinction as a reason for holding the Due Process Clause inapplicable to a juvenile proceeding. <span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/#50" aria-description="Citation for case: In Re GAULT">387 U. S., at 50-51</a></span>. The Court of Appeals also attempted to justify the preponderance standard on the related ground that juvenile proceedings are designed “not to punish, but to save the child.” 24 N. Y. 2d, at 197, <span class="citation" data-id="5524841"><a href="/opinion/5677035/in-re-samuel-w/#254" aria-description="Citation for case: In re Samuel W.">247 N. E. 2d, at 254</a></span>. Again, however, <em><span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/" aria-description="Citation for case: In Re GAULT">Gault</a></span> </em>expressly rejected this justification. <span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/#27" aria-description="Citation for case: In Re GAULT">387 U. S., at 27</a></span>. We made clear in that decision that civil labels and good <page-number citation-index="1" label="366">*366</page-number>intentions do not themselves obviate the need for criminal due process safeguards in juvenile courts, for "[a] proceeding where the issue is whether the child will be found to be 'delinquent’ and subjected to the loss of his liberty for years is comparable in seriousness to a felony prosecution.” <span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/#36" aria-description="Citation for case: In Re GAULT"><em>Id., </em>at 36</a></span>.</p>
<p id="b468-6">Nor do we perceive any merit in the argument that to afford juveniles the protection of proof beyond a reasonable doubt would risk destruction of beneficial aspects of the juvenile process.<footnotemark>4</footnotemark> Use of the reasonable-doubt standard during the adjudicatory hearing will not disturb New York’s policies that a finding that a child has violated a criminal law does not constitute a criminal conviction, that such a finding does not deprive the child of his civil rights, and that juvenile proceedings are confidential. Nor will there be any effect on the informality, flexibility, or speed of the hearing at which the factfinding takes place. And the opportunity during the post-adjudicatory or dispositional hearing for a wide-ranging review of the child’s social history and for his individualized treatment will remain unimpaired. Similarly, there will be no effect on the pro<page-number citation-index="1" label="367">*367</page-number>cedures distinctive to juvenile proceedings that are employed prior to the adjudicatory hearing.</p>
<p id="b469-5">The Court of Appeals observed that “a child’s best interest is not necessarily, or even probably, promoted if he wins in the particular inquiry which may bring him to the juvenile court.” 24 N. Y. 2d, at 199, <span class="citation" data-id="5524841"><a href="/opinion/5677035/in-re-samuel-w/#255" aria-description="Citation for case: In re Samuel W.">247 N. E. 2d, at 255</a></span>. It is true, of course, that the juvenile may be engaging in a general course of conduct inimical to his welfare that calls for judicial intervention. But that intervention cannot take the form of subjecting the child to the stigma of a finding that he violated a criminal law<footnotemark>5</footnotemark> and to the possibility of institutional confinement on proof insufficient to convict him were he an adult.</p>
<p id="b469-6">We conclude, as we concluded regarding the essential due process safeguards applied in <em><span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/" aria-description="Citation for case: In Re GAULT">Gault</a></span>, </em>that the observance of the standard of proof beyond a reasonable doubt “will not compel the States to abandon or displace any of the substantive benefits of the juvenile process.” <em>Gault, supra, </em>at 21.</p>
<p id="b469-7">Finally, we reject the Court of Appeals’ suggestion that there is, in any event, only a “tenuous difference” between the reasonable-doubt and preponderance standards. The suggestion is singularly unpersuasive. In this very case, the trial judge’s ability to distinguish between the two standards enabled him to make a finding of guilt that he conceded he might not have made under the standard of proof beyond a reasonable doubt. Indeed, the trial judge’s action evidences the accuracy of the observation of commentators that “the preponderance test is susceptible to the misinter<page-number citation-index="1" label="368">*368</page-number>pretation that it calls on the trier of fact merely to perform an abstract weighing of the evidence in order to determine which side has produced the greater quantum, without regard to its effect in convincing his mind of the truth of the proposition asserted.” Dorsen &amp; Rezneck, <em>supra, </em>at 26-27.<footnotemark>6</footnotemark></p>
<p id="b470-6">Ill</p>
<p id="b470-7">In sum, the constitutional safeguard of proof beyond a reasonable doubt is as much required during the adjudicatory stage of a delinquency proceeding as are those constitutional safeguards applied in <em><span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/" aria-description="Citation for case: In Re GAULT">Gault</a></span> </em>— notice of charges, right to counsel, the rights of confrontation and examination, and the privilege against self-incrimination. We therefore hold, in agreement with Chief Judge Fuld in dissent in the Court of Appeals, “that, where a 12-year-old child is charged with an act of stealing which renders him liable to confinement for as long as six years, then, as a matter of due process . . . the case against him must be proved beyond a reasonable doubt.” 24 N. Y. 2d, at 207, <span class="citation" data-id="5524841"><a href="/opinion/5677035/in-re-samuel-w/#260" aria-description="Citation for case: In re Samuel W.">247 N. E. 2d, at 260</a></span>.</p>
<p id="b470-8">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b461-6">Thus, we do not see how it can be said in dissent that this opinion “rests entirely on the assumption that all juvenile proceedings are 'criminal prosecutions/ hence subject to constitutional limitations.” As in <em><span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/" aria-description="Citation for case: In Re GAULT">Gault</a></span>, </em>“we are not here concerned with . . . the pre-judicial stages of the juvenile process, nor do we direct our attention to the post-adjudicative or dispositional process.” 387 IT. S., at 13. In New York, the adjudicatory stage of a delinquency proceeding is clearly distinct from both the preliminary phase of the juvenile process and from its dispositional stage. See N. Y. Family Court Act §§ 731-749. Similarly, we intimate no view concerning the constitutionality of the New York procedures governing children “in need of supervision.” See <em>id,., </em>at §§ 711-712, 742-745. Nor do we consider whether there are other “essentials of due process and fair treatment” required during the adjudicatory hearing of a delinquency proceeding. Finally, we have no occasion to consider appellant’s argument that § 744 (b) is a violation of the Equal Protection Clause, as well as a denial of due process.</p>
</footnote>
<footnote label="2">
<p id="b462-5"> The ruling appears in the following portion of the hearing transcript:</p>
<p id="b462-6">Counsel: “Your Honor is making a finding by the preponderance of the evidence.”</p>
<p id="b462-7">Court: “Well, it convinces me.”</p>
<p id="b462-8">Counsel: “It’s not beyond a reasonable doubt, Your Honor.” Court: “That is true .... Our statute says a preponderance and a preponderance it is.”</p>
</footnote>
<footnote label="3">
<p id="b462-9"> Accord, <em>e. g., In re Dennis M., </em><span class="citation" data-id="9624619"><a href="/opinion/1413298/thornton-v-dennis-m/" aria-description="Citation for case: Thornton v. Dennis M.">70 Cal. 2d 444</a></span>, <span class="citation" data-id="9624619"><a href="/opinion/1413298/thornton-v-dennis-m/" aria-description="Citation for case: Thornton v. Dennis M.">450 P. 2d 296</a></span> (1969); <em>In re Ellis, </em><span class="citation" data-id="2297131"><a href="/opinion/2297131/in-re-ellis/" aria-description="Citation for case: In Re Ellis">253 A. 2d 789</a></span> (D. C. Ct. App. 1969); <em>State </em>v. <em>Arenas, </em><span class="citation" data-id="9568839"><a href="/opinion/1225259/state-v-arenas/" aria-description="Citation for case: State v. Arenas">253 Ore. 215</a></span>, <span class="citation" data-id="9568839"><a href="/opinion/1225259/state-v-arenas/" aria-description="Citation for case: State v. Arenas">453 P. 2d 915</a></span> (1969); <em>State </em>v. <em>Santana, </em><span class="citation" data-id="9674285"><a href="/opinion/1728982/state-v-santana/" aria-description="Citation for case: State v. Santana">444 S. W. 2d 614</a></span> (Texas 1969). Contra, <em>United States </em>v. <em>Costanzo, </em><span class="citation" data-id="280322"><a href="/opinion/280322/united-states-v-august-costanzo/" aria-description="Citation for case: United States v. August Costanzo">395 F. 2d 441</a></span> (C. A. 4th Cir. 1968); <em>In re Urbaseh, </em>38 111. 2d 535, <span class="citation" data-id="2225213"><a href="/opinion/2225213/people-v-urbasek/" aria-description="Citation for case: People v. Urbasek">232 N. E. 2d 716</a></span> (1967); <em>Jones </em>v. <em>Commonwealth, </em><page-number citation-index="1" label="361">*361</page-number><span class="citation" data-id="6821552"><a href="/opinion/6925461/jones-v-commonwealth/" aria-description="Citation for case: Jones v. Commonwealth">185 Va. 335</a></span>, <span class="citation" data-id="6821552"><a href="/opinion/6925461/jones-v-commonwealth/" aria-description="Citation for case: Jones v. Commonwealth">38 S. E. 2d 444</a></span> (1946); N. D. Cent. Code § 27-20-29 (2) (Supp. 1969); <span class="citation no-link">Colo. Rev. Stat. Ann. § 22-3-6</span> (1) (1967); Md. Ann. Code, Art. 26, § 70-18 (a) (Supp. 1969); N. J. Ct. Rule 6:9 (1)(f) (1967); Wash. Sup. Ct., Juv. Ct. Rule § 4.4 (b) (1969); cf. <em>In re Agler, </em><span class="citation" data-id="6754234"><a href="/opinion/6864455/in-re-agler/" aria-description="Citation for case: In re Agler">19 Ohio St. 2d 70</a></span>, <span class="citation" data-id="6754234"><a href="/opinion/6864455/in-re-agler/" aria-description="Citation for case: In re Agler">249 N. E. 2d 808</a></span> (1969).</p>
<p id="b463-8">Legislative adoption of the reasonable-doubt standard has been urged by the National Conference of Commissioners on Uniform State Laws and by the Children’s Bureau of the Department of Health, Education, and Welfare’s Social and Rehabilitation Service. See Uniform Juvenile Court Act § 29 (b) (1968); Children’s Bureau, Social and Rehabilitation Service, U. S. Department of Health, Education, and Welfare, Legislative Guide for Drafting Family and Juvenile Court Acts § 32 (c) (1969). Cf. the proposal of the National Council on Crime and Delinquency that a “clear and convincing” standard be adopted. Model Rules for Juvenile Courts, Rule 26, p. 57 (1969). See generally Cohen,. The Standard of Proof in Juvenile Proceedings: <em><span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/" aria-description="Citation for case: In Re GAULT">Gault</a></span> </em>Beyond a Reasonable Doubt, <span class="citation no-link">68 Mich. L. Rev. 567</span> (1970).</p>
</footnote>
<footnote label="4">
<p id="b468-7"> Appellee, New York City, apparently concedes as much in its Brief, page 8, where it <em>states:</em></p>
<blockquote id="b468-8">“A determination that the New York law unconstitutionally denies due process because it does not provide for use of the reasonable doubt standard probably would not have a serious impact if all that resulted would be a change in the quantum of proof.”</blockquote>
<p id="b468-9">And Doreen &amp; Rezneck, <em>supra, </em>at 27, have observed:</p>
<blockquote id="b468-10">“[TJhe reasonable doubt test is superior to all others in protecting against an unjust adjudication of guilt, and that is as much a concern of the juvenile court as of the criminal court. It is difficult to see how the distinctive objectives of the juvenile court give rise to a legitimate institutional interest in finding a juvenile to have committed a violation of the criminal law on less evidence than if he were an adult.”</blockquote>
</footnote>
<footnote label="5">
<p id="b469-8"> The more comprehensive and effective the procedures used to prevent public disclosure of the finding, the less the danger of stigma. As we indicated in <em><span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/" aria-description="Citation for case: In Re GAULT">Gault</a></span>, </em>however, often the “claim of secrecy ... is more rhetoric than reality.” <span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/#24" aria-description="Citation for case: In Re GAULT">387 U. S., at 24</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b470-11"> Compare this Court’s rejection of the preponderance standard in deportation proceedings, where we ruled that the Government must support its allegations with “clear, unequivocal, and convincing evidence.” <em>Woodby </em>v. <em>Immigration and Naturalization Service, </em><span class="citation" data-id="9423303"><a href="/opinion/107317/woodby-v-immigration-naturalization-service/#285" aria-description="Citation for case: Woodby v. Immigration &amp; Naturalization Service">385 U. S. 276, 285</a></span> (1966). Although we ruled in <em><span class="citation" data-id="9423303"><a href="/opinion/107317/woodby-v-immigration-naturalization-service/" aria-description="Citation for case: Woodby v. Immigration &amp; Naturalization Service">Woodby</a></span> </em>that deportation is not tantamount to a criminal conviction, we found that since it could lead to “drastic deprivations,” it is impermissible for a person to be “banished from this country upon no higher degree of proof than applies in a negligence case.” <em><span class="citation" data-id="9423303"><a href="/opinion/107317/woodby-v-immigration-naturalization-service/" aria-description="Citation for case: Woodby v. Immigration &amp; Naturalization Service">Ibid.</a></span></em></p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/kalina-v-fletcher--118156.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6c7771f3c7a01519", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "kalina-v-fletcher--118156"}, "payload": {"all": [{"cite": "522 U.S. 118", "page": "118", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "522"}, {"cite": "118 S. Ct. 502", "page": "502", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "118"}, {"cite": "139 L. Ed. 2d 471", "page": "471", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "139"}, {"cite": "1997 U.S. LEXIS 7498", "page": "7498", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1997"}], "display": null, "official": null, "official_selection_present": false, "record_id": "kalina-v-fletcher--118156"}}
{"assertion_id": "fd5309152110cabb", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "kalina-v-fletcher--118156"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "kalina-v-fletcher--118156", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — kalina-v-fletcher--118156

```json
{
  "schema_version": "s2.v1",
  "record_id": "kalina-v-fletcher--118156",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Kalina v. Fletcher",
    "case_name_short": "Kalina",
    "case_name_full": "Kalina v. Fletcher",
    "input_case_name": "Kalina v. Fletcher",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1997-12-10",
    "year": 1997,
    "docket": null,
    "cluster_id": 118156,
    "lead_opinion_id": 9433547,
    "sibling_ids": [],
    "absolute_url": "/opinion/118156/kalina-v-fletcher/",
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
        "cite": "522 U.S. 118",
        "volume": "522",
        "reporter": "U.S.",
        "page": "118",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "118 S. Ct. 502",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "502",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "139 L. Ed. 2d 471",
        "volume": "139",
        "reporter": "L. Ed. 2d",
        "page": "471",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1997 U.S. LEXIS 7498",
        "volume": "1997",
        "reporter": "U.S. LEXIS",
        "page": "7498",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "522 U.S. 118",
        "volume": "522",
        "reporter": "U.S.",
        "page": "118",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "118 S. Ct. 502",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "502",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "139 L. Ed. 2d 471",
        "volume": "139",
        "reporter": "L. Ed. 2d",
        "page": "471",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1997 U.S. LEXIS 7498",
        "volume": "1997",
        "reporter": "U.S. LEXIS",
        "page": "7498",
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
    "date_created": "2026-07-06T13:54:18Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:54:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:54:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:54:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:54:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — kalina-v-fletcher--118156

```
<opinion type="majority">
<author id="b296-5">Justice Stevens</author>
<p id="AI1">delivered the opinion of the Court.</p>
<p id="b296-6">The question presented is whether <span class="citation no-link">42 U. S. C. § 1988</span> creates a damages remedy against a prosecutor for making false statements of faet in an affidavit supporting an application for an arrest warrant, or whether, as she contends, such conduct is protected by “the doctrine of absolute prosecutorial immunity.”</p>
<p id="b296-7">I</p>
<p id="b296-8">Petitioner is a deputy prosecuting attorney for King County, Washington. Following customary practice, on December 14, 1992, she commenced a criminal proceeding <page-number citation-index="1" label="121">*121</page-number>against respondent by filing three documents in the King County Superior Court. Two of those documents — an information charging respondent with burglary and a motion for an arrest warrant — were unsworn pleadings. The burglary charge was based on an alleged theft of computer equipment from a school.</p>
<p id="b297-5">Washington Criminal Rules require that an arrest warrant be supported by an affidavit or “sworn testimony establishing the grounds for issuing the warrant.”<footnotemark>1</footnotemark> To satisfy that requirement, petitioner supported her motion with a third document — a “Certification for Determination of Probable Cause” — that summarized the evidence supporting the charge. She personally vouched for the truth of the facts set forth in the certification under penalty of perjury.<footnotemark>2</footnotemark> Based on petitioner’s certification, the trial court found probable cause and ordered that an arrest warrant be issued.</p>
<p id="b297-6">Petitioner’s certification contained two inaccurate factual statements. After noting that respondent’s fingerprints had been found on a glass partition in the school, petitioner stated that respondent had “never been associated with the school in any manner and did not have permission to enter the school or to take any property.”<footnotemark>3</footnotemark> In fact, he had installed partitions on the premises and was authorized to enter the school. She also stated that an employee of an electronics store had identified respondent “from a photo montage” as the person who had asked for an appraisal of a computer stolen from the school.<footnotemark>4</footnotemark> In fact, the employee did not identify respondent.<footnotemark>5</footnotemark></p>
<p id="b298-4"><page-number citation-index="1" label="122">*122</page-number>Respondent was arrested and spent a day in jail. About a month later, the charges against him were dismissed on the prosecutor’s motion.</p>
<p id="b298-5">II</p>
<p id="b298-6">Respondent brought this action under Rev. Stat. § 1979, as amended, <span class="citation no-link">42 U. S. C. § 1988</span>, seeking damages from petitioner based on her alleged violation of his constitutional right to be free from unreasonable seizures. In determining immunity, we accept the allegations of respondent’s complaint as true. See <em>Buckley </em>v. <em>Fitzsimmons, </em><span class="citation" data-id="9432862"><a href="/opinion/112894/buckley-v-fitzsimmons/#261" aria-description="Citation for case: Buckley v. Fitzsimmons">509 U. S. 259, 261</a></span> (1993). Respondent’s complaint focuses on the false statements made by petitioner in the certification.<footnotemark>6</footnotemark> Petitioner moved for summary judgment on the ground that the. three documents that she filed to commence the criminal proceedings- and to procure the arrest warrant were protected by “the doctrine of absolute prosecutorial immunity.”<footnotemark>7</footnotemark> The District Court denied the motion, holding that she was not entitled to absolute immunity and that whether qualified immunity would apply was a question of fact.<footnotemark>8</footnotemark> The Court of Appeals for the Ninth Circuit affirmed.</p>
<p id="b298-7">The Ninth Circuit first noted that under our decision in <em>Malley </em>v. <em>Briggs, </em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">475 U. S. 335</a></span> (1986), “a <em>police officer </em>who secures an arrest warrant without probable cause cannot assert an absolute immunity defense,” and then observed that petitioner’s “actions in writing, signing and filing the declaration for an arrest warrant” were “virtually identical to the police officer’s actions in <em>Malley.” </em><span class="citation" data-id="724957"><a href="/opinion/724957/rodney-fletcher-plaintiff-appellee-v-lynne-kalina-defendant-appellant/#655" aria-description="Citation for case: Rodney FLETCHER, Plaintiff-Appellee, v. Lynne KALINA,...">93 F. 3d 653, 655-656</a></span> (1996). Relying on the functional approach endorsed in <em>Buckley </em>v. <em><span class="citation" data-id="9432862"><a href="/opinion/112894/buckley-v-fitzsimmons/" aria-description="Citation for case: Buckley v. Fitzsimmons">Fitzsimmons</a></span>, </em>the Court of Appeals concluded that “it would be ‘incongruous’ to expose police to potential liability while protecting prosecutors for the same act.” <span class="citation" data-id="724957"><a href="/opinion/724957/rodney-fletcher-plaintiff-appellee-v-lynne-kalina-defendant-appellant/#656" aria-description="Citation for case: Rodney FLETCHER, Plaintiff-Appellee, v. Lynne KALINA,...">93 F. 3d, at 656</a></span>.</p>
<p id="b299-9"><page-number citation-index="1" label="123">*123</page-number>The Court of Appeals acknowledged that the Sixth Circuit had reached a different result in <em>Joseph </em>v. <em>Patterson, </em><span class="citation" data-id="8942852"><a href="/opinion/8952029/joseph-v-patterson/#555" aria-description="Citation for case: Joseph v. Patterson">795 F. 2d 549, 555</a></span> (1986), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./481/1023/">481 U. S. 1023</a></span> (1987), a case that predated our decision in <em><span class="citation" data-id="9432862"><a href="/opinion/112894/buckley-v-fitzsimmons/" aria-description="Citation for case: Buckley v. Fitzsimmons">Buckley</a></span>. </em>Because we have never squarely addressed the question whether a prosecutor may be held liable for conduct in obtaining an arrest warrant, we granted certiorari to resolve the conflict. <span class="citation multiple-matches"><a href="/c/U.%20S./519/1148/">519 U. S. 1148</a></span> (1997). We now affirm.</p>
<p id="b299-10">J-H HH hH</p>
<p id="b299-3">Section 1983 is a codification of §1 of the Civil Rights Act of 1871.<footnotemark>9</footnotemark> The text of the statute purports to create a damages remedy against every state official for the violation of any person’s federal constitutional or statutory rights.<footnotemark>10</footnotemark> The coverage of the statute is thus broader than the preexisting common law of torts. Wé have nevertheless recognized that Congress intended the statute to be construed in the light of common-law principles that were well settled at the time of its enactment. See <em>Tenney </em>v. <em>Brandhove, </em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">341 U. S. 367</a></span> (1951); <em>Briscoe </em>v. <em>LaHue, </em><span class="citation" data-id="9429107"><a href="/opinion/110885/briscoe-v-lahue/#330" aria-description="Citation for case: Briscoe v. LaHue">460 U. S. 325, 330</a></span> (1983). Thus, we have examined common-law doctrine when identifying both the elements of the cause of action and the defenses available to state actors.</p>
<p id="b299-4">In <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409</a></span> (1976), we held that a former prisoner whose conviction had been set aside in collateral proceedings could not maintain a § 1983 action against the prosecutor who had litigated the charges against him. Relying in part on common-law precedent, and per<page-number citation-index="1" label="124">*124</page-number>haps even more importantly on the policy considerations underlying that precedent, we concluded that “a state prosecuting attorney who acted within the scope of his duties in initiating and pursuing a criminal prosecution” was not amenable to suit under § 1983. <em>Id., </em>at 410.</p>
<p id="b300-5">Liberally construed, Imbler’s complaint included not only a charge that the prosecution had been wrongfully commenced, but also a charge that false testimony had been offered as well as a charge that exculpatory evidence had been suppressed. His constitutional claims were thus broader than any specific common-law antecedent. Nevertheless, relying on common-law decisions providing prosecutors with absolute immunity from tort actions based on claims that the decision to prosecute was malicious and unsupported by probable cause,<footnotemark>11</footnotemark> as well as from actions for defamation based on statements made during trial,<footnotemark>12</footnotemark> we concluded that <page-number citation-index="1" label="125">*125</page-number>the statute should be construed to provide an analogous defense against the claims asserted by Imbler, The policy considerations that justified the common-law decisions affording absolute immunity to prosecutors when performing traditional functions applied equally to statutory claims based on the conduct of the same functions.</p>
<p id="b301-5">Those considerations included both the interest in protecting the prosecutor from harassing litigation that would divert his time and attention from his official duties and the interest in enabling him to exercise independent judgment when “deciding which suits to bring and in conducting them in court.” <em>Id., </em>at 424. The former interest would lend support to an immunity from all litigation against the occupant of the office whereas the'latter is applicable only when the official is performing functions that require the exercise of prosecutorial discretion. Our later eases have made it clear that it is the interest in protecting the proper functioning of the office, rather than the interest in protecting its occupant, that is of primary importance.</p>
<p id="b301-6">In <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Imbler</a></span>, </em>we did not attempt to define the outer limits of the prosecutor’s absolute immunity, but we did recognize that our rationale would not encompass some of his official activities. Thus, while we concluded that Pachtman’s “activities were intimately associated with the judicial phase of the criminal process, and thus were functions to which the reasons for absolute immunity apply with full force,” <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#430" aria-description="Citation for case: Imbler v. Pachtman"><em>id., </em>at 430</a></span>, we put to one side “those aspects of the prosecutor’s responsibility that cast him in the role of an administrator or investigative officer rather than that of advocate,” <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#430" aria-description="Citation for case: Imbler v. Pachtman"><em>id., </em>at 430-431</a></span>.</p>
<p id="b301-7">Subsequent cases have confirmed the importance to the judicial process of protecting the prosecutor when serving as an advocate in judicial proceedings. Thus, in <em>Burns </em>v. <em>Reed, </em><span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/" aria-description="Citation for case: Burns v. Reed">500 U. S. 478</a></span> (1991), after noting the consensus among the Courts of Appeals concerning prosecutorial conduct before grand juries, <span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/#490" aria-description="Citation for case: Burns v. Reed"><em>id., </em>at 490, n. 6</a></span>, we held that the prosecutor’s <page-number citation-index="1" label="126">*126</page-number>appearance in court in support of an application for a search warrant and the presentation of evidence at that hearing were protected by absolute immunity, <span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/#492" aria-description="Citation for case: Burns v. Reed"><em>id., </em>at 492</a></span>. And in <em><span class="citation" data-id="9432862"><a href="/opinion/112894/buckley-v-fitzsimmons/" aria-description="Citation for case: Buckley v. Fitzsimmons">Buckley</a></span>, </em>we categorically stated that “acts undertaken by a prosecutor in preparing for the initiation of judicial proceedings or for trial, and which occur in the course of his role as an advocate for the State, are entitled to the protections of absolute immunity.” <span class="citation" data-id="9432862"><a href="/opinion/112894/buckley-v-fitzsimmons/#278" aria-description="Citation for case: Buckley v. Fitzsimmons">509 U. S., at 278</a></span>.</p>
<p id="b302-5">In both of those cases, we available when the prosecutor was performing a different function. In <em><span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/" aria-description="Citation for case: Burns v. Reed">Burns</a></span>, </em>the provision of legal advice to the police during their pretrial investigation of the facts was protected only by qualified, rather than absolute, immunity. <span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/#492" aria-description="Citation for case: Burns v. Reed">500 U. S., at 492-496</a></span>. Similarly, in <em><span class="citation" data-id="9432862"><a href="/opinion/112894/buckley-v-fitzsimmons/" aria-description="Citation for case: Buckley v. Fitzsimmons">Buckley</a></span>, </em>the prosecutor was not acting as an advocate either when he held a press conference, <span class="citation" data-id="9432862"><a href="/opinion/112894/buckley-v-fitzsimmons/#276" aria-description="Citation for case: Buckley v. Fitzsimmons">509 U. S., at 276-278</a></span>, or when he allegedly fabricated evidence concerning an unsolved crime. With reference to the latter holding, we explained:</p>
<blockquote id="b302-6">“There is a difference between the advocate’s role in evaluating evidence and interviewing witnesses as he prepares for trial, on the one hand, and the detective’s role in searching for the clues and corroboration that might give him probable cause to recommend that a suspect be arrested, on the other hand. When a prosecutor performs the investigative functions normally performed by a detective or police officer, it is ‘neither appropriate nor justifiable that, for the same act, immunity should protect the one and not the other.’ <em>Hampton </em>v. <em>Chicago, </em><span class="citation multiple-matches"><a href="/c/F.%202d/484/602/">484 F. 2d 602</a></span>, 608 (CA7 1973) (internal quotation marks omitted), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./415/917/">415 U. S. 917</a></span> (1974). Thus, if a prosecutor plans and executes a raid on a suspected weapons cache, he ‘has no greater claim to complete immunity than activities of police officers allegedly acting under his direction.’ 484 F. 2d, at 608-609.” <em>Id., at </em>273-274.</blockquote>
<p id="b303-4"><page-number citation-index="1" label="127">*127</page-number>These eases make it clear that the absolute immunity that protects the prosecutor’s role as an advocate is not grounded in any special “esteem for those who perform these functions, and certainly not from a desire to shield abuses of office, but because any lesser degree of immunity could impair the judicial process itself.” <em>Malley, </em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#342" aria-description="Citation for case: Malley v. Briggs">475 U. S., at 342</a></span>. Thus, in determining immunity, we examine “the nature of the function performed, not the identity of the actor who performed it.” <em>Forrester </em>v. <em>White, </em><span class="citation" data-id="111977"><a href="/opinion/111977/forrester-v-white/#229" aria-description="Citation for case: Forrester v. White">484 U. S. 219, 229</a></span> (1988).<footnotemark>13</footnotemark> This point is perhaps best illustrated by the determination that the senior law enforcement official in the Nation — the Attorney General of the United States — is protected only by qualified, rather than absolute, immunity when engaged in the performance of national defense functions rather than prosecutorial functions. <em>Mitchell </em>v. <em>Forsyth, </em><span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/" aria-description="Citation for case: Mitchell v. Forsyth">472 U. S. 511</a></span> (1985).</p>
<p id="b303-5">In <em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">Malley</a></span> </em>we considered, and rejected, two theories on which immunity might have been accorded to a police officer who had caused an unconstitutional arrest by presenting a judge with a complaint and supporting affidavit that failed to establish probable cause. His first argument, that his function was comparable to that of a complaining witness, actually militated against his claim because such witnesses were subject to suit at common law.<footnotemark>14</footnotemark></p>
<p id="b304-4"><page-number citation-index="1" label="128">*128</page-number>His second argument rested on the similarity between his conduct and the functions often performed by prosecutors. As we explained:</p>
<blockquote id="b304-5">“As an alternative ground for claiming absolute immunity, petitioner draws an analogy between an officer requesting a warrant and a prosecutor who asks a grand jury to indict a suspect. Like the prosecutor, petitioner argues, the officer must exercise a discretionary judgment based on the evidence before him, and like the prosecutor, the officer may not exercise his best judgment if the threat of retaliatory lawsuits hangs over him. Thus, petitioner urges us to read § 1983 as giving the officer the same absolute immunity enjoyed by the prosecutor. Cf. <em>Imbler v. Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409</a></span> (1976).</blockquote>
<blockquote id="b304-6">“. . . We intend no disrespect to the officer applying for a warrant by observing that his action, while a vital part of the administration of criminal justice, is further removed from the judicial phase of criminal proceedings than the act of a prosecutor in seeking an indictment. Furthermore, petitioner’s analogy, while it has some force, does not take account of the fact that the prosecutor’s act in seeking an indictment is but the first step in the process of seeking a conviction. Exposing the prosecutor to liability for the initial phase of his prosecu-torial work could interfere with his exercise of independent judgment at every phase of his work, since the prosecutor might come to see later decisions in terms of their effect on his potential liability. Thus, we shield the prosecutor seeking an indictment because any lesser immunity could impair the performance of a central actor in the judicial process.” <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#341" aria-description="Citation for case: Malley v. Briggs">475 U. S., at 341-343</a></span>.</blockquote>
<p id="b305-4"><page-number citation-index="1" label="129">*129</page-number>These eases make it quite clear that petitioner’s activities in connection with the preparation and filing of two of the three charging documents — the information and the motion for an arrest warrant — are protected by absolute immunity. Indeed, except for her act in personally attesting to the truth of the averments in the certification, it seems equally clear that the preparation and filing of the third document in the package was part of the advocate’s function as well. The critical question, however, is whether she was acting as a complaining witness rather than a lawyer when she executed the certification “[ujnder penalty of perjury.” We now turn to that question.</p>
<p id="b305-5">IV</p>
<p id="b305-6">The Fourth Amendment requires that arrest warrants be based “upon probable cause, supported by Oath or affirmation” — a requirement that may be satisfied by an indictment returned by a grand jury, but not by the mere filing of criminal charges in an unsworn information signed by the prosecutor. <em>Gerstein </em>v. Pugh, <span class="citation multiple-matches"><a href="/c/U.%20S./420/108/">420 U. S. 108</a></span>, 117 (1975); see also <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971). Accordingly, since most prosecutions in Washington are commenced by information, Washington law requires, in compliance with the constitutional command, that an arrest warrant be supported by either an affidavit “or sworn testimony establishing the grounds for issuing the warrant.”<footnotemark>15</footnotemark> The “Certification for Determination of Probable Cause” executed by petitioner was designed to satisfy those requirements.</p>
<p id="b305-7">Although the law required that document to be sworn or certified under penalty of perjury, neither federal nor state law made it necessary for the prosecutor to make that certification. In doing so, petitioner performed an act that any <page-number citation-index="1" label="130">*130</page-number>competent witness might have performed. . Even if she may have1 been following a practice that was routinely employed by her colleagues and predecessors in King County, Washington, that practice is surely not prevalent in other parts of the country and is not even mandated by law in King County. Neither petitioner nor <em>amici </em>argue that prosecutors routinely follow the King County practice.<footnotemark>16</footnotemark> Indeed, tradition, as well as the ethics of our profession, generally instruct counsel to avoid the risks associated with participating as both advocate and witness in the same proceeding.<footnotemark>17</footnotemark></p>
<p id="b306-5">Nevertheless, petitioner argues that the execution of the certificate was just one incident in a presentation that, viewed as a whole, was the work of an advocate and was integral to the initiation of the prosecution. That characterization is appropriate for her drafting of the certification, her determination that the evidence was sufficiently strong to justify a probable-cause finding, her decision to file charges, and her presentation of the information and the motion to the court. Each of those matters involved the exercise of professional judgment; indeed, even the selection of the particular facts to include in the certification to provide the evidentiary support for the finding of probable cause required the exercise of the judgment of the advocate. But that judgment could not affect the truth or falsity of the factual statements themselves. Testifying about facts is the function of the witness, not of the lawyer. No matter how <page-number citation-index="1" label="131">*131</page-number>brief or succinct it may be, the evidentiary component of an application for an arrest warrant is a distinct and essential predicate for a finding of probable cause. Even when the person who makes the constitutionally required “Oath or affirmation” is a lawyer, the only function that she performs in giving sworn testimony is that of a witness.</p>
<p id="b307-4">Finally, petitioner argues that denying her absolute immunity will have a “chilling effect” on prosecutors in the administration of justice.<footnotemark>18</footnotemark> We are not persuaded.</p>
<p id="b307-5">It may well be true that prosecutors in King County may abandon the practice of routinely attesting to the facts recited in a “Certification for Determination of Probable Cause” and pattern their procedures after those employed in other parts of the Nation. Petitioner presents no evidence that the administration of justice is harmed where the King County practice is not followed. In other respects, however, her argument addresses concerns that are not affected by our decision because we merely hold that § 1983 may provide a remedy for respondent insofar as petitioner performed the function of a complaining witness. We do not depart from our prior cases that have recognized that the prosecutor is fully protected by absolute immunity when performing the traditional functions of an advocate. See <em>Imbler, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#431" aria-description="Citation for case: Imbler v. Pachtman">424 U. S., at 431</a></span>; <em>Buckley, </em><span class="citation" data-id="9432862"><a href="/opinion/112894/buckley-v-fitzsimmons/#273" aria-description="Citation for case: Buckley v. Fitzsimmons">509 U. S., at 273</a></span>.</p>
<p id="b307-6">Accordingly, the judgment of the Court of Appeals for the Ninth Circuit is</p>
<p id="b307-7">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b297-7"> Washington Criminal Rule 2.2(a); see Wash. Rev. Code § 9A.72.085 (1994) (providing, <em>inter alia, </em>that a certification made under penalty of perjury is the equivalent of an affidavit). Accord, King County Local Criminal Rule 2.2.</p>
</footnote>
<footnote label="2">
<p id="b297-8"> App. 20.</p>
</footnote>
<footnote label="3">
<p id="b297-9"> Id, at 19-20.</p>
</footnote>
<footnote label="4">
<p id="b297-10"> Id, at 20.</p>
</footnote>
<footnote label="5">
<p id="b297-11"> Id, at 5.</p>
</footnote>
<footnote label="6">
<p id="b298-8"><em> Id., </em>at 5-6.</p>
</footnote>
<footnote label="7">
<p id="b298-9"> <em>Id., </em>at 10.</p>
</footnote>
<footnote label="8">
<p id="b298-10"><em> Id., </em>at 21.</p>
</footnote>
<footnote label="9">
<p id="b299-5"> See <em>Briscoe </em>v. <em>LaHue, </em><span class="citation" data-id="9429107"><a href="/opinion/110885/briscoe-v-lahue/#337" aria-description="Citation for case: Briscoe v. LaHue">460 U. S. 325, 337</a></span> (1983).</p>
</footnote>
<footnote label="10">
<p id="b299-6"> Title <span class="citation no-link">42 U. S. C. § 1983</span> provides:</p>
<p id="b299-7">“Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory or the District of Columbia, subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress ....”</p>
</footnote>
<footnote label="11">
<p id="b300-6"> See <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#421" aria-description="Citation for case: Imbler v. Pachtman">424 U. S., at 421-422</a></span>. The eases that the Court cited were decided after 1871 and granted a broader immunity to public prosecutors than had been available in malicious prosecution actions against private persons who brought prosecutions at early common law. See <em>Savile </em>v. <em>Roberts, </em>1 Ld. Raym. 374, 91 Eng. Rep. 1147 (K. B. 1699); <em>Hill </em>v. <em>Miles, </em>9 N. H. 9 (1837); M. Bigelow, Leading Cases on the Law of Torts 193-204 (1875). However, these early cases were decided before the office of public prosecutor in its modern form was common. See Langbein, The Origins of Public Prosecution at Common Law, <span class="citation no-link">17 Am. J. Legal Hist. 313</span>, 316 (1973); Kress, Progress and Prosecution, <span class="citation no-link">423 Annals Am. Acad. Pol. &amp; Soc. Sci. 99</span>, 100-102 (1976); <em>White </em>v. <em>Frank, </em><span class="citation" data-id="510966"><a href="/opinion/510966/willie-d-white-v-richard-frank-freeman-marshall-city-of-poughkeepsie/#962" aria-description="Citation for case: Willie D. White v. Richard Frank, Freeman Marshall, City...">855 F. 2d 956, 962</a></span> (CA2 1988) (noting that “the availability of the malidous prosecution aetion has been curtailed with the growth of the office of the public prosecutor”). Thus, the Court in <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Imbler</a></span> </em>drew guidance both from the. first American cases addressing the availability of malidous prosecution actions against public prosecutors, and perhaps more importantly, from the policy considerations underlying the firmly established common-law rules providing absolute immunity for judges and jurors. See <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#423" aria-description="Citation for case: Imbler v. Pachtman">424 U. S., at 423, n. 20</a></span> (discussing similarity in some functions performed by judges, jurors, and prosecutors); <em>Bradley </em>v. <em>Fisher, </em><span class="citation" data-id="9416839"><a href="/opinion/88468/bradley-v-fisher/#347" aria-description="Citation for case: Bradley v. Fisher">13 Wall. 335, 347</a></span> (1872); <em>Yates </em>v. <span class="citation" data-id="5472513"><a href="/opinion/5627426/yates-v-lansing/" aria-description="Citation for case: Yates v. Lansing"><em>Lansing, 5 </em>Johns. 282</a></span> (N. Y. 1810) (Kent, C. J.); Note, Civil Liability of a District Attorney for Quasi-Judicial Acts, <span class="citation no-link">73 U. Pa. L. Rev. 300</span>, 303, n. 13 (1925).</p>
</footnote>
<footnote label="12">
<p id="b300-7"> See <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">424 U. S., at 439</a></span>-440</p>
</footnote>
<footnote label="13">
<p id="b303-6"> Examining the nature of the function performed is-not a recent innovation. In <em>Ex parte Virginia, </em><span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/#348" aria-description="Citation for case: Ex Parte Virginia">100 U. S. 339, 348</a></span> (1880), we stated “[w]hether the act done by [a judge] was judicial or not is to be determined by its character, and not by the character of the agent.” See also <em>Bradley </em>v. <em>Fisher, </em><span class="citation" data-id="9416839"><a href="/opinion/88468/bradley-v-fisher/#347" aria-description="Citation for case: Bradley v. Fisher">13 Wall., at 347</a></span> (examining “the character of the act” performed by a judge).</p>
</footnote>
<footnote label="14">
<p id="b303-7"> We noted that:</p>
<p id="b303-8">“[C]omplaining witnesses were not absolutely immune at common law. In 1871, the generally accepted rule was that one who procured the issuance of an arrest warrant by submitting a complaint could be held liable if the complaint was made maliciously and without probable cause. Given malice and the lack of probable cause, the complainant enjoyed no immu<page-number citation-index="1" label="128">*128</page-number>nity. The common law thus affords no support for petitioner.” <em>Malley </em>v. <em>Briggs, </em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#340" aria-description="Citation for case: Malley v. Briggs">475 U. S. 335, 340-341</a></span> (1986) (footnote omitted).</p>
</footnote>
<footnote label="15">
<p id="b305-8"> Washington Criminal Rule 2.2(a) (1995) provides:</p>
<p id="b305-9">“A warrant of arrest must be supported by an affidavit, ... or sworn testimony establishing the grounds for issuing the warrant.... The court must determine there is probable cause ... before issuing the warrant. ”</p>
</footnote>
<footnote label="16">
<p id="b306-6"> <em>Amicus Curiae </em>United States points out that federal prosecutors typically do not personally attest to the facts in an affidavit filed in support of an application for an arrest warrant, but “[finstead a law enforcement agent ordinarily attests to those facts.” Brief 7. <em>Amici Curiae </em>Thirty-Nine Counties of the State of Washington state that local court rules in only two 'counties in Washington require the prosecutor to file an additional document beyond an information. Brief 2.</p>
</footnote>
<footnote label="17">
<p id="b306-7"> See, <em>e. g., </em>Washington Rule of Professional Conduct 3.7 (1995) (“A lawyer shall not act as advocate at a trial in which the lawyer... is likely to be a necessary witness,” unless four narrow exceptions apply); ABA Model Rules of Professional Conduct 3.7 (1992).</p>
</footnote>
<footnote label="18">
<p id="b307-10"> Brief for Petitioner 25.</p>
</footnote>
</opinion>
```

---
