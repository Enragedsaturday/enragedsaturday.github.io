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

## GROUP: _overhaul2/lake/cases/united-states-v-vergara--4477911.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6bfa9411672c0c85", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "united-states-v-vergara--4477911"}, "payload": {"all": [{"cite": "884 F.3d 1309", "page": "1309", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "884"}], "display": "884 F.3d 1309", "official": {"cite": "884 F.3d 1309", "page": "1309", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "884"}, "official_selection_present": true, "record_id": "united-states-v-vergara--4477911"}}
{"assertion_id": "11eaf70b901530e3", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-vergara--4477911"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-vergara--4477911", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-vergara--4477911

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-vergara--4477911",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "United States v. Hernando Javier Vergara",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Hernando Javier VERGARA, Defendant-Appellant.",
    "input_case_name": "United States v. Vergara",
    "court": "U.S. Court of Appeals, 11th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca11",
    "state": null,
    "date_decided": null,
    "year": 2018,
    "docket": null,
    "cluster_id": 4477911,
    "lead_opinion_id": 9880576,
    "sibling_ids": [],
    "absolute_url": "/opinion/4477911/united-states-v-hernando-javier-vergara/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "884 F.3d 1309",
      "volume": "884",
      "reporter": "F.3d",
      "page": "1309",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "884 F.3d 1309",
        "volume": "884",
        "reporter": "F.3d",
        "page": "1309",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "884 F.3d 1309",
    "official_selection": {
      "court_class": "coa",
      "selected": "884 F.3d 1309",
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
    "date_created": "2026-07-06T13:14:27Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:14:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:14:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:14:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:14:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — united-states-v-vergara--4477911

```
<opinion type="majority">
<author id="p-8">WILLIAM PRYOR, Circuit Judge:</author>
<p id="p-9">This appeal presents the issue whether warrantless forensic searches of two cell phones at the border violated the Fourth Amendment. U.S. Const. amend IV. Hernando Javier Vergara appeals the denial of his motion to suppress evidence found on two cell phones that he carried on a cruise from Cozumel, Mexico to Tampa, Florida. He argues that the recent decision of the Supreme Court in <a class="page-label" data-citation-index="1" data-label="1311" href="#p1311" id="p1311">*1311</a><em>Riley v. California</em> , --- U.S. ----, <extracted-citation case-ids="12581677" index="0" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. 2473</a></span></extracted-citation>, <extracted-citation case-ids="12581677" index="1" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">189 L.Ed.2d 430</a></span></extracted-citation> (2014) -that the search-incident-to-arrest exception to the warrant requirement does not apply to searches of cell phones-should govern this appeal. But we disagree. The forensic searches of Vergara's cell phones occurred at the border, not as searches incident to arrest, and border searches never require a warrant or probable cause. At most, border searches require reasonable suspicion, but Vergara has not argued that the agents lacked reasonable suspicion to conduct a forensic search of his phones. We affirm.</p>
<p id="p-10"><strong>I. BACKGROUND</strong></p>
<p id="p-11">Vergara returned to Tampa, Florida, on a cruise ship from Cozumel, Mexico, with three phones: a Samsung phone inside a bag in his luggage, an LG phone, and an iPhone. Christopher Ragan, an officer with Customs and Border Protection, identified Vergara and searched his luggage. When Ragan found the Samsung phone in Vergara's luggage, he asked Vergara to turn the phone on and then looked through the phone for about five minutes. During this search, Ragan found a video of two topless female minors. After watching a few seconds of that video, Ragan called investigators for the Department of Homeland Security.</p>
<p id="p-12">After viewing the video and interviewing Vergara, Terri Botterbusch, a special agent with the Department of Homeland Security, decided to have all three phones forensically examined. Agents later returned the iPhone to Vergara's niece after a forensic examination revealed that it did not contain any child pornography.</p>
<p id="p-13">A forensic examination of the Samsung and LG phones conducted that day revealed more than 100 images and videos, "the production of which involved the use of a minor engaging in sexually explicit conduct and the visual depictions were of such conduct." Neither the earlier manual search nor the forensic examinations damaged the phones. A grand jury later indicted Vergara on two counts: (1) that he "did knowingly transport in and affecting interstate and foreign commerce one or more visual depictions, the production of which involved the use of a minor engaging in sexually explicit conduct and such visual depictions were of such conduct"; and (2) that he "did knowingly possess numerous matters that had been shipped and transported using any means and facility of interstate and foreign commerce, including by computer, which matters contained visual depictions of minors engaging in sexually explicit conduct and the production of which involved the use of minors engaging in sexually explicit conduct." <em>See</em> <extracted-citation index="2" url="https://cite.case.law/citations/?q=18%20U.S.C.%20%C2%A7%202252"><span class="citation no-link">18 U.S.C. § 2252</span></extracted-citation>(a)(1), (b)(1) ; <extracted-citation index="3" url="https://cite.case.law/citations/?q=18%20U.S.C.%20%C2%A7%202252"><span class="citation no-link">18 U.S.C. § 2252</span></extracted-citation>(a)(4)(B), (b)(2).</p>
<p id="p-14">Vergara filed a motion to suppress the evidence obtained from his cell phones. The court held a suppression hearing, at which Ragan and Botterbusch testified, and later denied Vergara's motion. The district court ruled that the initial manual search did not require reasonable suspicion and found that "in any event, ... Agent Ragan had reasonable suspicion to search the applications and settings of the phone for evidence of child pornography." The district court also rejected Vergara's argument that <em>Riley v. California</em> , --- U.S. ----, <extracted-citation case-ids="12581677" index="4" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. 2473</a></span></extracted-citation>, <extracted-citation case-ids="12581677" index="5" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">189 L.Ed.2d 430</a></span></extracted-citation> (2014), required the agents to obtain a warrant before conducting the forensic search. It reasoned that <em><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Riley</a></span></em> did not apply to border searches. It agreed with the government that "if [Vergara] had entered the country with child pornography images in a notebook, the notebook would have been subject to inspection, and he cannot be allowed to insulate himself from inspection by storing child pornography electronically on his cell phone." And it concluded that, in any event, the search was supported by reasonable suspicion.</p>
<p id="p-15"><a class="page-label" data-citation-index="1" data-label="1312" href="#p1312" id="p1312">*1312</a>At a later bench trial, the district court found Vergara guilty of both counts and later sentenced him to ninety-six months of imprisonment on each count concurrently followed by supervision for life.</p>
<p id="p-16"><strong>II. STANDARD OF REVIEW</strong></p>
<p id="p-17">"With regard to [a] motion to suppress, we review the district court's factual findings for clear error and its legal conclusions <em>de novo</em> ." <em>United States v. Newsome</em> , <extracted-citation case-ids="3752686" index="6" url="https://cite.case.law/f3d/475/1221/#p1223"><span class="citation" data-id="77569"><a href="/opinion/77569/united-states-v-kenneth-newsome/" aria-description="Citation for case: United States v. Kenneth Newsome">475 F.3d 1221</a></span></extracted-citation>, 1223 (11th Cir. 2007). We construe all facts "in the light most favorable to the prevailing party below." <em><extracted-citation case-ids="3752686" index="7" url="https://cite.case.law/f3d/475/1221/#p1223">Id.</extracted-citation></em><extracted-citation case-ids="3752686" index="7" url="https://cite.case.law/f3d/475/1221/#p1223"> at 1224</extracted-citation> (internal quotation marks omitted). And "[t]he individual challenging the search bears the burdens of proof and persuasion." <em><extracted-citation case-ids="3752686" index="8" url="https://cite.case.law/f3d/475/1221/#p1223"><span class="citation" data-id="77569"><a href="/opinion/77569/united-states-v-kenneth-newsome/" aria-description="Citation for case: United States v. Kenneth Newsome">Id.</a></span></extracted-citation></em> (internal quotation marks omitted).</p>
<p id="p-18"><strong>III. DISCUSSION</strong></p>
<p id="p-19">The Fourth Amendment to the U.S. Constitution provides, "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause ...." U.S. Const. amend. IV. Ordinarily, "where a search is undertaken by law enforcement officials to discover evidence of criminal wrongdoing, reasonableness ... requires the obtaining of a judicial warrant." <em>Riley</em> , <extracted-citation case-ids="12581677" index="9" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/#2482" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. at 2482</a></span></extracted-citation> (alterations adopted) (internal quotation marks omitted). But searches at the border, "from before the adoption of the Fourth Amendment, have been considered to be 'reasonable' by the single fact that the person or item in question had entered into our country from outside." <em>United States v. Ramsey</em> , <extracted-citation case-ids="1727" index="10" url="https://cite.case.law/us/431/606/#p619"><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">431 U.S. 606</a></span></extracted-citation>, 619, <extracted-citation case-ids="1727" index="11" url="https://cite.case.law/us/431/606/#p619"><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">97 S.Ct. 1972</a></span></extracted-citation>, <extracted-citation case-ids="1727" index="12" url="https://cite.case.law/us/431/606/#p619"><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">52 L.Ed.2d 617</a></span></extracted-citation> (1977). Border searches "never" require probable cause or a warrant. <em><extracted-citation case-ids="1727" index="13" url="https://cite.case.law/us/431/606/#p619"><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">Id.</a></span></extracted-citation></em> And we require reasonable suspicion at the border only "for highly intrusive searches of a person's body such as a strip search or an x-ray examination." <em>United States v. Alfaro-Moncada</em> , <extracted-citation case-ids="3683143" index="14" url="https://cite.case.law/f3d/607/720/#p729"><span class="citation" data-id="147332"><a href="/opinion/147332/united-states-v-alfaro-moncada/" aria-description="Citation for case: United States v. Alfaro-Moncada">607 F.3d 720</a></span></extracted-citation>, 729 (11th Cir. 2010).</p>
<p id="p-20">The forensic searches of Vergara's phones required neither a warrant nor probable cause. "The Supreme Court has consistently held that border searches are not subject to the probable cause and warrant requirements of the Fourth Amendment." <em>United States v. Vega-Barvo</em> , <extracted-citation case-ids="1938913" index="15" url="https://cite.case.law/f2d/729/1341/#p1344"><span class="citation" data-id="9471930"><a href="/opinion/432317/united-states-v-maria-vega-barvo/" aria-description="Citation for case: United States v. Maria Vega-Barvo">729 F.2d 1341</a></span></extracted-citation>, 1344 (11th Cir. 1984) (citing <em>Ramsey</em> , <extracted-citation case-ids="1727" index="16" url="https://cite.case.law/us/431/606/#p619"><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">431 U.S. at 619</a></span></extracted-citation>, <extracted-citation case-ids="1727" index="17" url="https://cite.case.law/us/431/606/#p619"><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">97 S.Ct. 1972</a></span></extracted-citation> ). Instead, "they are simply subject to that amendment's more amorphous reasonableness standard." <em>United States v. Villabona-Garnica</em> , <extracted-citation case-ids="7416112" index="18" url="https://cite.case.law/f3d/63/1051/#p1057"><span class="citation" data-id="702402"><a href="/opinion/702402/united-states-v-german-villabona-garnica-jorge-enrique-munoz/" aria-description="Citation for case: United States v. German Villabona-Garnica, Jorge Enrique...">63 F.3d 1051</a></span></extracted-citation>, 1057 (11th Cir. 1995). The "longstanding recognition that searches at our borders without probable cause and without a warrant are nonetheless 'reasonable' has a history as old as the Fourth Amendment itself." <em>Ramsey</em> , <extracted-citation case-ids="1727" index="19" url="https://cite.case.law/us/431/606/#p619"><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">431 U.S. at 619</a></span></extracted-citation>, <extracted-citation case-ids="1727" index="20" url="https://cite.case.law/us/431/606/#p619"><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">97 S.Ct. 1972</a></span></extracted-citation>. And "[t]here has never been any additional requirement that the reasonableness of a border search depended on the existence of probable cause." <em><extracted-citation case-ids="1727" index="21" url="https://cite.case.law/us/431/606/#p619"><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">Id.</a></span></extracted-citation></em> ; <em>see also</em> <em>United States v. Montoya de Hernandez</em> , <extracted-citation case-ids="6203102" index="22" url="https://cite.case.law/us/473/531/#p537"><span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U.S. 531</a></span></extracted-citation>, 537-38, <extracted-citation case-ids="6203102" index="23" url="https://cite.case.law/us/473/531/#p537"><span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/" aria-description="Citation for case: United States v. Montoya De Hernandez">105 S.Ct. 3304</a></span></extracted-citation>, <extracted-citation case-ids="6203102" index="24" url="https://cite.case.law/us/473/531/#p537"><span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/" aria-description="Citation for case: United States v. Montoya De Hernandez">87 L.Ed.2d 381</a></span></extracted-citation> (1985).</p>
<p id="p-21">Vergara argues that <em><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Riley</a></span></em> required a warrant for both the manual and the forensic searches of his phones, but he challenges only the forensic searches because no evidence from the manual search was admitted as evidence against him. In <em><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Riley</a></span></em> , the Supreme Court addressed the constitutionality of warrantless manual searches of cell phones following the arrest of two defendants in the United States. <extracted-citation case-ids="12581677" index="25" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. at 2480</a></span>-82</extracted-citation>. And the Supreme Court expressly limited its holding to the search-incident-to-arrest exception. It explained that "even though [that] exception does not apply to cell phones, other case-specific exceptions may still justify a warrantless search of a particular phone." <em><extracted-citation case-ids="12581677" index="26" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12581677" index="26" url="https://cite.case.law/s-ct/134/2473/"> at 2494</extracted-citation>.</p>
<p id="p-22">Border searches have long been excepted from warrant and probable cause requirements, <a class="page-label" data-citation-index="1" data-label="1313" href="#p1313" id="p1313">*1313</a>and the holding of <em><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Riley</a></span></em> does not change this rule. Vergara points to language from <em><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Riley</a></span></em> about the "consequences for privacy" involved in a search of a cell phone. <em><extracted-citation case-ids="12581677" index="27" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12581677" index="27" url="https://cite.case.law/s-ct/134/2473/"> at 2489</extracted-citation>. But this language does not help him. At the border, the highest standard for a search is reasonable suspicion, <em>see</em> <em>Vega-Barvo</em> , <extracted-citation case-ids="1938913" index="28" url="https://cite.case.law/f2d/729/1341/#p1344"><span class="citation" data-id="9471930"><a href="/opinion/432317/united-states-v-maria-vega-barvo/" aria-description="Citation for case: United States v. Maria Vega-Barvo">729 F.2d at 1344</a></span>-45</extracted-citation>, and Vergara has not challenged the finding of the district court that reasonable suspicion existed for the searches of his phones. So we need not-and do not-address the questions whether reasonable suspicion was required for the searches or whether reasonable suspicion existed.</p>
<p id="p-23"><strong>IV. CONCLUSION</strong></p>
<p id="p-24">We <strong>AFFIRM</strong> Vergara's judgment of conviction and sentence.</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/united-states-v-west--10653830.json  (`lake-record`, 1 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9f3989b430011349", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-west--10653830"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-west--10653830", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-west--10653830

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-west--10653830",
  "stub": true,
  "status": "fabrication_suspected",
  "identity": {
    "case_name": "Sauer West LLC v. United States",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. West",
    "court": "unknown",
    "court_id": null,
    "court_level": null,
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": null,
    "docket": null,
    "cluster_id": 10653830,
    "lead_opinion_id": null,
    "sibling_ids": [],
    "absolute_url": "/opinion/10653830/sauer-west-llc-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": false,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": "state",
      "selected": null,
      "reason": "no_official_class_citation"
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
    "date_created": "2026-07-06T05:59:55Z",
    "date_modified": "2026-07-06T06:00:08Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T06:00:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T06:00:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T06:00:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T06:00:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

---

## GROUP: _overhaul2/lake/cases/united-states-v-white--10349533.json  (`lake-record`, 1 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d73ff2dab846fcb7", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-white--10349533"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-white--10349533", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-white--10349533

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-white--10349533",
  "stub": true,
  "status": "fabrication_suspected",
  "identity": {
    "case_name": "White v. United States",
    "case_name_short": "White",
    "case_name_full": "",
    "input_case_name": "United States v. White",
    "court": "unknown",
    "court_id": null,
    "court_level": null,
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": null,
    "docket": null,
    "cluster_id": 10349533,
    "lead_opinion_id": null,
    "sibling_ids": [],
    "absolute_url": "/opinion/10349533/white-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": false,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": "state",
      "selected": null,
      "reason": "no_official_class_citation"
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
    "date_created": "2026-07-06T06:00:09Z",
    "date_modified": "2026-07-06T06:00:32Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T06:00:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T06:00:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T06:00:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T06:00:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

---

## GROUP: _overhaul2/lake/cases/wallace-v-kato--145756.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "72cbcaba7bbdc6c9", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "wallace-v-kato--145756"}, "payload": {"all": [{"cite": "127 S. Ct. 1091", "page": "1091", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "127"}, {"cite": "549 U.S. 384", "page": "384", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "549"}], "display": null, "official": null, "official_selection_present": false, "record_id": "wallace-v-kato--145756"}}
{"assertion_id": "57b093235fa09021", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "wallace-v-kato--145756"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "wallace-v-kato--145756", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — wallace-v-kato--145756

```json
{
  "schema_version": "s2.v1",
  "record_id": "wallace-v-kato--145756",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Wallace v. Kato",
    "case_name_short": "Wallace",
    "case_name_full": "WALLACE v. KATO Et Al.",
    "input_case_name": "Wallace v. Kato",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2007-02-21",
    "year": 2007,
    "docket": "No. 05-1240",
    "cluster_id": 145756,
    "lead_opinion_id": 9435115,
    "sibling_ids": [],
    "absolute_url": "/opinion/145756/wallace-v-kato/",
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
        "cite": "127 S. Ct. 1091",
        "volume": "127",
        "reporter": "S. Ct.",
        "page": "1091",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "549 U.S. 384",
        "volume": "549",
        "reporter": "U.S.",
        "page": "384",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "127 S. Ct. 1091",
        "volume": "127",
        "reporter": "S. Ct.",
        "page": "1091",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "549 U.S. 384",
        "volume": "549",
        "reporter": "U.S.",
        "page": "384",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "other",
      "selected": null,
      "reason": "unlisted_reporter:S. Ct."
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
    "date_created": "2026-07-06T13:42:15Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:42:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:42:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:42:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:42:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — wallace-v-kato--145756

```
<opinion type="majority">
<author id="b660-4"><page-number citation-index="1" label="386">*386</page-number>Justice Scalia</author>
<p id="AoY">delivered the opinion of the Court.</p>
<p id="b660-5">Petitioner filed suit under Rev. Stat. § 1979, <span class="citation no-link">42 U. S. C. §1983</span>, seeking damages for an arrest that violated the Fourth Amendment. We decide whether his suit is timely.</p>
<p id="b660-6">I</p>
<p id="b660-7">On January 17,1994, John Handy was shot to death in the city of Chicago. Sometime around 8 p.m. two days later, Chicago police officers located petitioner, then 15 years of age, and transported him to a police station for questioning. After interrogations that lasted into the early morning hours the next day, petitioner agreed to confess to Handy’s murder. An assistant state’s attorney prepared a statement to this effect, and petitioner signed it, at the same time waiving his <em>Miranda </em>rights.</p>
<p id="b660-8">Prior to trial in the Circuit Court of Cook County, petitioner unsuccessfully attempted to suppress his station house statements as the product of an unlawful arrest. He was convicted of first-degree murder and sentenced to 26 years in prison. On direct appeal, the Appellate Court of Illinois held that officers had arrested petitioner without probable cause, in violation of the Fourth Amendment. <em>People </em>v. <em>Wallace, </em>299 111. App. 3d 9, 17-18, <span class="citation" data-id="9720206"><a href="/opinion/2115873/people-v-wallace/#94" aria-description="Citation for case: People v. Wallace">701 N. E. 2d 87, 94</a></span> (1998). According to that court (whose determination we are not reviewing here), even assuming petitioner willingly accompanied police to the station, his presence there “esca<page-number citation-index="1" label="387">*387</page-number>lated to an involuntary seizure prior to his formal arrest.” <em>Id., </em>at 18, <span class="citation" data-id="9720206"><a href="/opinion/2115873/people-v-wallace/#94" aria-description="Citation for case: People v. Wallace">701 N. E. 2d, at 94</a></span>. After another round of appeals, the Appellate Court concluded on August 31, 2001, that the effect of petitioner’s illegal arrest had not been sufficiently attenuated to render his statements admissible, see <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975), and remanded for a new trial. Judgt. order reported <em>sub nom. People </em>v. <em>Wallace, </em>324 111. App. 3d 1139, <span class="citation no-link">805 N. E. 2d 756</span> (2001). On April 10, 2002, prosecutors dropped the charges against petitioner.</p>
<p id="b661-4">On April 2,2003, petitioner filed this § 1983 suit against the city of Chicago and several Chicago police officers, seeking damages arising from, <em>inter alia, </em>his unlawful arrest.<footnotemark>1</footnotemark> The District Court granted summary judgment to respondents and the Court of Appeals affirmed. According to the Seventh Circuit, petitioner’s § 1983 suit was time barred because his cause of action accrued at the time of his arrest, and not when his conviction was later set aside. <em>Wallace </em>v. <em>Chicago, </em><span class="citation" data-id="9498735"><a href="/opinion/793583/andre-wallace-v-city-of-chicago-kristen-kato-and-eugene-roy/#427" aria-description="Citation for case: Andre Wallace v. City of Chicago, Kristen Kato and Eugene...">440 F. 3d 421, 427</a></span> (2006). We granted certiorari, <span class="citation no-link">547 U. S. 1205</span> (2006).</p>
<p id="b661-5">II</p>
<p id="b661-6">Section 1983 provides a federal cause of action, but in several respects relevant here federal law looks to the law of the State in which the cause of action arose. This is so for the length of the statute of limitations: It is that which the State provides for personal-injury torts. <em>Owens </em>v. <em>Okure, </em><span class="citation" data-id="112166"><a href="/opinion/112166/owens-v-okure/#249" aria-description="Citation for case: Owens v. Okure">488 U. S. 235,249-250</a></span> (1989); <em>Wilson </em>v. <em>Garcia, </em><span class="citation" data-id="9430006"><a href="/opinion/111415/wilson-v-garcia/#279" aria-description="Citation for case: Wilson v. Garcia">471 U. S. 261, 279-280</a></span> (1985). The parties agree that under Illinois law, this period is two years. 111. Comp. Stat., ch. 735, § 5/13-202 (West 2003). Thus, if the statute on petitioner’s cause of action began to run at the time of his unlawful arrest, or even at the time he was ordered held by a magistrate, his <page-number citation-index="1" label="388">*388</page-number>§ 1983 suit was plainly dilatory, even according him tolling for the two-plus years of his minority, see §5/13-211. But if, as the dissenting judge argued below, the commencement date for running of the statute is governed by this Court’s decision in <em>Heck </em>v. <em>Humphrey, </em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U. S. 477</a></span> (1994), that date <em>may </em>be the date on which petitioner’s conviction was vacated, in which case the § 1983 suit would have been timely filed.</p>
<p id="b662-5">While we have never stated so expressly, the accrual date of a § 1983 cause of action is a question of federal law that is <em>not </em>resolved by reference to state law. The parties agree, the Seventh Circuit in this case so held, see <span class="citation" data-id="9498735"><a href="/opinion/793583/andre-wallace-v-city-of-chicago-kristen-kato-and-eugene-roy/#424" aria-description="Citation for case: Andre Wallace v. City of Chicago, Kristen Kato and Eugene...">440 F. 3d, at 424</a></span>, and we are aware of no federal court of appeals holding to the contrary. Aspects of § 1983 which are not governed by reference to state law are governed by federal rules conforming in general to common-law tort principles. See <span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/#483" aria-description="Citation for case: Heck v. Humphrey"><em>Heck, supra, </em>at 483</a></span>; <em>Carey </em>v. <em>Piphus, </em><span class="citation" data-id="109815"><a href="/opinion/109815/carey-v-piphus/#257" aria-description="Citation for case: Carey v. Piphus">435 U. S. 247, 257-258</a></span> (1978). Under those principles, it is “the standard rule that [accrual occurs] when the plaintiff has <em>‘a </em>complete and present cause of action,’ ” <em>Bay Area Laundry and Dry Cleaning Pension Trust Fund </em>v. <em>Ferbar Corp. of Cal., </em><span class="citation" data-id="118159"><a href="/opinion/118159/bay-area-laundry-dry-cleaning-pension-trust-fund-v-ferbar-corp-of/#201" aria-description="Citation for case: Bay Area Laundry &amp; Dry Cleaning Pension Trust Fund v....">522 U. S. 192, 201</a></span> (1997) (quoting <em>Rawlings </em>v. <em>Ray, </em><span class="citation" data-id="103441"><a href="/opinion/103441/rawlings-v-ray/#98" aria-description="Citation for case: Rawlings v. Ray">312 U. S. 96, 98</a></span> (1941)), that is, when “the plaintiff can file suit and obtain relief,” <span class="citation" data-id="118159"><a href="/opinion/118159/bay-area-laundry-dry-cleaning-pension-trust-fund-v-ferbar-corp-of/#201" aria-description="Citation for case: Bay Area Laundry &amp; Dry Cleaning Pension Trust Fund v...."><em>Bay Area Laundry, supra, </em>at 201</a></span>. There can be no dispute that petitioner could have filed suit as soon as the allegedly wrongful arrest occurred, subjecting him to the harm of involuntary detention, so the statute of limitations would normally commence to run from that date.</p>
<p id="b662-6">There is, however, a refinement to be considered, arising from the common law’s distinctive treatment of the torts of false arrest and false imprisonment, “[t]he . . . causefs] of action [that] provid[e] the closest analogy to claims of the type considered here,” <span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/#484" aria-description="Citation for case: Heck v. Humphrey"><em>Heck, supra, </em>at 484</a></span>. See 1 D. Dobbs, Law of Torts §47, p. 88 (2001). False arrest and false imprisonment overlap; the former is a species of the latter. “Every confinement of the person is an imprison<page-number citation-index="1" label="389">*389</page-number>ment, whether it be in a common prison or in a private house, or in the stocks, or even by forcibly detaining one in the public streets; and when a man is lawfully in a house, it is imprisonment to prevent him from leaving the room in which he is.” M. Newell, Law of Malicious Prosecution, False Imprisonment, and Abuse of Legal Process §2, p. 57 (1892) (footnote omitted). See also 7 S. Speiser, C. Krause, &amp; A. Gans, American Law of Torts § 27:2, pp. 940-942 (1990). We shall thus refer to the two torts together as false imprisonment. That tort provides the proper analogy to the cause of action asserted against the present respondents for the following reason: The sort of unlawful detention remediable by the tort of false imprisonment is detention <em>without legal process, </em>see, <em>e. g., </em>W. Keeton, D. Dobbs, R. Keeton, &amp; D. Owen, Prosser and Keeton on Law of Torts § 11, p. 54, §119, pp. 885-886 (5th ed. 1984); 7 Speiser, <em>supra, </em>§27:2, at 943-944, and the allegations before us arise from respondents’ detention of petitioner <em>without legal process </em>in January 1994. They did not have a warrant for his arrest.</p>
<p id="b663-5">The running of the statute of limitations on false imprisonment is subject to a distinctive rule — dictated, perhaps, by the reality that the victim may not be able to sue while he is still imprisoned: “Limitations begin to run against an action for false imprisonment when the alleged false imprisonment ends.” 2 H. Wood, Limitation of Actions §187d(4), p. 878 (rev. 4th ed. 1916); see also 4 Restatement (Second) of Torts §899, Comment c (1977); A. Underhill, Principles of Law of Torts 202 (1881). Thus, to determine the beginning of the limitations period in this case, we must determine when petitioner’s false imprisonment came to an end.</p>
<p id="b663-6">Reflective of the fact that false imprisonment consists of detention without legal process, a false imprisonment ends once the victim becomes held <em>pursuant to such </em>process— when, for example, he is bound over by a magistrate or arraigned on charges. 1 Dobbs, <em>supra, </em>§ 39, at 74, n. 2; Keeton, <em>supra, </em>§ 119, at 888; H. Stephen, Actions for Malicious Prose<page-number citation-index="1" label="390">*390</page-number>cution 120-123 (1888). Thereafter, unlawful detention forms part of the damages for the “entirely distinct” tort of malicious prosecution, which remedies detention accompanied, not by absence of legal process, but by <em>wrongful institution </em>of legal process.<footnotemark>2</footnotemark> Keeton, <em>supra, </em>§ 119, at 885-886; see 1 F. Harper, F. James, &amp; O. Gray, Law of Torts § 3.9, p. 3:36 (3d ed. 1996); 7 Speiser, <em>supra, </em>§ 27:2, at 943-945. “If there is a false arrest claim, damages for that claim cover the time of detention up until issuance of process or arraignment, but not more. From that point on, any damages recoverable must be based on a malicious prosecution claim and on the wrongful use of judicial process rather than detention itself.” Keeton, <em>supra, </em>§ 119, at 888; see also <span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/#484" aria-description="Citation for case: Heck v. Humphrey"><em>Heck, supra, </em>at 484</a></span>; 8 Speiser, <em>supra, </em>§28:15, at 80. Thus, petitioner’s contention that his false imprisonment ended upon his release from custody, after the State dropped the charges against him, must be rejected. It ended much earlier, when legal process was initiated against him, and the statute would have begun to run from that date, but for its tolling by reason of petitioner’s minority.<footnotemark>3</footnotemark></p>
<p id="b665-4"><page-number citation-index="1" label="391">*391</page-number>Petitioner asserts that the date of his release from custody must be the relevant date in the circumstances of the present suit, since he is seeking damages up to that time. The theory of his complaint is that the initial Fourth Amendment violation set the wheels in motion for his subsequent conviction and detention: The unlawful arrest led to the coerced confession, which was introduced at his trial, producing his conviction and incarceration. As we have just explained, at common law damages for detention after issuance of process or arraignment would be attributable to a tort other than the unlawful arrest alleged in petitioner’s complaint — and probably a tort chargeable to defendants other than the respondents here. Even assuming, however, that all damages for detention pursuant to legal process could be regarded as consequential damages attributable to the unlawful arrest, that would not alter the commencement date for the statute of limitations. “Under the traditional rule of accrual... the tort cause of action accrues, and the statute of limitations commences to run, when the wrongful act or omission results in damages. The cause of action accrues even though the full extent of the injury is not then known or predictable.” 1 C. Corman, Limitation of Actions § 7.4.1, pp. 526-527 (1991) (footnote omitted); see also 54 C. J. S., Limitations of Actions §112, p. 150 (2005). Were it otherwise, the statute would begin to run only after a plaintiff became satisfied that he had been harmed enough, placing the supposed statute of repose in the sole hands of the party seeking relief.</p>
<p id="b665-5">We conclude that the statute of limitations on petitioner’s § 1988 claim commenced to run when he appeared before the examining magistrate and was bound over for trial. Since more than two years elapsed between that date and the filing <page-number citation-index="1" label="392">*392</page-number>of this suit — even leaving out of the count the period before he reached his majority — the action was time barred.</p>
<p id="b666-5">Ill</p>
<p id="b666-6">This would end the matter, were it not for petitioner’s contention that <em>Heck </em>v. <em>Humphrey, </em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/#477" aria-description="Citation for case: Heck v. Humphrey">512 U. S., at 477</a></span>, compels the conclusion that his suit could not accrue until the State dropped its charges against him. In <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span>, </em>a state prisoner filed suit under §1983 raising claims which, if true, would have established the invalidity of his outstanding conviction. We analogized his suit to one for malicious prosecution, an element of which is the favorable termination of criminal proceedings. <em>Id., </em>at 484. We said:</p>
<blockquote id="b666-7">“[I]n order to recover damages for allegedly unconstitutional conviction or imprisonment, or for other harm caused by actions whose unlawfulness would render a conviction or sentence invalid, a §1983 plaintiff must prove that the conviction or sentence has been reversed on direct appeal, expunged by executive order, declared invalid by a state tribunal authorized to make such determination, or called into question by a federal court’s issuance of a writ of habeas corpus, <span class="citation no-link">28 U. S. C. § 2254</span>. A claim for damages bearing that relationship to a conviction or sentence that has <em>not </em>been so invalidated is not cognizable under §1983.” <em>Id., </em>at 486-487 (footnote omitted).</blockquote>
<p id="b666-8">We rested this conclusion upon “the hoary principle that civil tort actions are not appropriate vehicles for challenging the validity of outstanding criminal judgments.” <em>Id., </em>at 486. “ ‘Congress,’ ” we said, “ ‘has determined that habeas corpus is the appropriate remedy for state prisoners attacking the validity of the fact or length of their confinement, and that specific determination must override the general terms of § 1983.’ ” <em>Id., </em>at 482 (quoting <em>Preiser </em>v. <em>Rodriguez, </em><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/#490" aria-description="Citation for case: Preiser v. Rodriguez">411 U. S. 475, 490</a></span> (1973)).</p>
<p id="b667-4"><page-number citation-index="1" label="393">*393</page-number>As the above excerpts show, the <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span> </em>rule for deferred accrual is called into play only when there exists “a conviction or sentence that has <em>not </em>been . . . invalidated,” that is to say, an “outstanding criminal judgment.” It delays what would otherwise be the accrual date of a tort action until the setting aside <em>of an extant conviction </em>which success in that tort action would impugn. We assume that, for purposes of the present tort action, the <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span> </em>principle would be applied not to the date of accrual but to the date on which the statute of limitations began to run, that is, the date petitioner became held pursuant to legal process. See <em>supra, </em>at 389-390. Even at that later time, there was in existence no criminal conviction that the cause of action would impugn; indeed, there may not even have been an indictment.</p>
<p id="b667-5">What petitioner seeks, in other words, is the adoption of a principle that goes well beyond <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span>: </em>that an action which would impugn <em>an anticipated future conviction </em>cannot be brought until that conviction occurs and is set aside. The impractieality of such a rule should be obvious. In an action for false arrest it would require the plaintiff (and if he brings suit promptly, the court) to speculate about whether a prosecution will be brought, whether it will result in conviction, and whether the pending civil action will impugn that verdict, see <em>Heck, </em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/#487" aria-description="Citation for case: Heck v. Humphrey">512 U. S., at 487</a></span>, n. 7 — all this at a time when it can hardly be known what evidence the prosecution has in its possession. And what if the plaintiff (or the court) guesses wrong, and the anticipated future conviction never occurs, because of acquittal or dismissal? Does that event (instead of the <em>Heck-required </em>setting aside of the extant conviction) trigger accrual of the cause of action? Or what if prosecution never occurs — what will the trigger be then?</p>
<p id="b667-6">We are not disposed to embrace this bizarre extension of <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span>. </em>If a plaintiff files a false-arrest claim before he has been convicted (or files any other claim related to rulings that will likely be made in a pending or anticipated criminal trial), it is within the power of the district court, and in ac<page-number citation-index="1" label="394">*394</page-number>cord with common practice, to stay the civil action until the criminal case or the likelihood of a criminal case is ended. See <span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/#487" aria-description="Citation for case: Heck v. Humphrey"><em>id., </em>at 487-488, n. 8</a></span> (noting that “abstention may be an appropriate response to the parallel state-court proceedings”); <em>Quackenbush </em>v. <em>Allstate Ins. Co., </em><span class="citation" data-id="9433307"><a href="/opinion/118031/quackenbush-v-allstate-insurance/#730" aria-description="Citation for case: Quackenbush v. Allstate Insurance">517 U. S. 706, 730</a></span> (1996). If the plaintiff is ultimately convicted, and if the stayed civil suit would impugn that conviction, <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span> </em>will require dismissal; otherwise, the civil action will proceed, absent some other bar to suit. <em>Edwards </em>v. <em>Balisok, </em><span class="citation" data-id="9433460"><a href="/opinion/118112/edwards-v-balisok/#649" aria-description="Citation for case: Edwards v. Balisok">520 U. S. 641, 649</a></span> (1997); <em>Heck, </em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/#487" aria-description="Citation for case: Heck v. Humphrey">512 U. S., at 487</a></span>.</p>
<p id="b668-5">There is, however, one complication that we must address here. It arises from the fact that § 1983 actions, unlike the tort of malicious prosecution which <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span> </em>took as its model, see <span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/#484" aria-description="Citation for case: Heck v. Humphrey"><em>id., </em>at 484</a></span>, sometimes accrue before the setting aside of— indeed, even before the existence of — the related criminal conviction. That of course is the case here, and it raises the question whether, assuming that the <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span> </em>bar takes effect when the later conviction is obtained, the statute of limitations on the once valid cause of action is tolled as long as the <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span> </em>bar subsists. In the context of the present case: If petitioner’s conviction on April 19, 1996, caused the statute of limitations on his (possibly) impugning but yet-to-be-filed cause of action to be tolled until that conviction was set aside, his filing here would have been timely.</p>
<p id="b668-6">We have generally referred to state law for tolling rules, just as we have for the length of statutes of limitations. <em>Hardin </em>v. <em>Straub, </em><span class="citation" data-id="112265"><a href="/opinion/112265/hardin-v-straub/#538" aria-description="Citation for case: Hardin v. Straub">490 U. S. 536, 538-539</a></span> (1989); <em>Board of Regents of Univ. of State of N. Y. </em>v. <em>Tomanio, </em><span class="citation" data-id="9427922"><a href="/opinion/110261/board-of-regents-of-univ-of-state-of-ny-v-tomanio/#484" aria-description="Citation for case: Board of Regents of Univ. of State of NY v. Tomanio">446 U. S. 478, 484-486</a></span> (1980). Petitioner has not brought to our attention, nor are we aware of, Illinois cases providing tolling in even remotely comparable circumstances. (Indeed, petitioner did not even argue for such tolling below, though he supported its suggestion at oral argument.) Nor would we be inclined to adopt a federal tolling rule to this effect. Under such a regime, it would not be known whether tolling is appropriate by reason of the <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span> </em>bar until it is established that the <page-number citation-index="1" label="395">*395</page-number>newly entered conviction would be impugned by the not-yet-filed, and thus utterly indeterminate, § 1983 claim.<footnotemark>4</footnotemark> It would hardly be desirable to place the question of tolling <em>vel non </em>in this jurisprudential limbo, leaving it to be determined by those later events, and then pronouncing it retroactively. Defendants need to be on notice to preserve beyond the normal limitations period evidence that will be needed for their defense; and a statute that becomes retroactively extended, by the action of the plaintiff in crafting a conviction-impugning cause of action, is hardly a statute of repose.<footnotemark>5</footnotemark></p>
<p id="b670-4"><page-number citation-index="1" label="396">*396</page-number>Justice Breyer argues in dissent that equitable tolling should apply “so long as the issues that [a § 1983] claim would raise are being pursued in state court.” <em>Post, </em>at 403. We know of no support (nor does the dissent suggest any) for the far-reaching proposition that equitable tolling is appropriate to avoid the risk of concurrent litigation. As best we can tell, the only rationale for such a rule is the concern that “petitioner would have had to divide his attention between criminal and civil cases.” <em>Post, </em>at 400. But when has it been the law that a criminal defendant, or a potential criminal defendant, is absolved from all other responsibilities that the law would otherwise place upon him? If a defendant has a breach-of-contract claim against the prime contractor for his new home, is he entitled to tolling for that as well while his criminal case is pending? Equitable tolling is a rare remedy to be applied in unusual circumstances, not a cure-all for an entirely common state of affairs. Besides its never-heard-of-before quality, the dissent’s proposal suffers from a more ironic flaw. Although the dissent criticizes us for having to develop a system of stays and dismissals, it should be obvious that the omnibus tolling solution will require the same. Despite the existence of the new tolling rule, some (if not most) plaintiffs will nevertheless file suit before or during state criminal proceedings. How does the dissent propose to handle such suits? Finally, the dissent’s <page-number citation-index="1" label="397">*397</page-number>contention that law enforcement officers would prefer the possibility of a later § 1983 suit to the more likely reality of an immediate filing, <em>post, </em>at 403-404, is both implausible and contradicted by those who know best. As no fewer than 11 States have informed us in this litigation, “States and municipalities have a strong interest in timely notice of alleged misconduct by their agents. ” Brief for State of Illinois et al. as <em>Amici Curiae </em>18.</p>
<p id="b671-5">* * *</p>
<p id="b671-6">We hold that the statute of limitations upon a § 1983 claim seeking damages for a false arrest in violation of the Fourth Amendment, where the arrest is followed by criminal proceedings, begins to run at the time the claimant becomes detained pursuant to legal process. Since in the present case this occurred (with appropriate tolling for the plaintiff’s minority) more than two years before the complaint was filed, the suit was out of time. The judgment of the Court of Appeals is affirmed.</p>
<p id="b671-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b661-7"> All of petitioner’s other state and federal claims were resolved adversely to him and are not before us. We expressly limited our grant of certiorari to the Fourth Amendment false-arrest claim. See <span class="citation no-link">547 U. S. 1205</span> (2006). The city of Chicago is no longer a party to this suit.</p>
</footnote>
<footnote label="2">
<p id="b664-5"> We have never explored the contours of a Fourth Amendment malicious-prosecution suit under § 1983, see <em>Albright </em>v. <em>Oliver, </em><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/#270" aria-description="Citation for case: Albright v. Oliver">510 U. S. 266,270-271,275</a></span> (1994) (plurality opinion), and we do not do so here. See generally 1 M. Schwartz, Section 1983 Litigation §3.18[C], pp. 3-605 to 3-629 (4th ed. 2004) (noting a range of approaches in the lower courts). Assuming without deciding that such a claim is cognizable under § 1983, petitioner has not made one. Petitioner did not include such a claim in his complaint. He in fact abandoned a state-law malicious-prosecution claim in the District Court, and stated, in his opposition to respondents’ first motion for summary judgment, that “Plaintiff does not seek to raise ... a malicious prosecution claim under § 1983,” Record, Doc. 17, p. 3, n. 5. In this Court, he has told us that respondents are “mistaken in characterizing petitioner’s cause of action as involving “unwarranted prosecution.’ ” Reply Brief 12.</p>
</footnote>
<footnote label="3">
<p id="b664-6"> This is not to say, of course, that petitioner could not have filed suit immediately upon his false arrest. While the statute of limitations did not begin to run until petitioner became detained pursuant to legal process, he was injured and suffered damages at the moment of his arrest, <page-number citation-index="1" label="391">*391</page-number>and was entitled to bring suit at that time. See <em>Adler </em>v. <em>Beverly Hills Hospital, </em><span class="citation" data-id="1632275"><a href="/opinion/1632275/adler-v-beverly-hills-hospital/#156" aria-description="Citation for case: Adler v. Beverly Hills Hospital">594 S. W. 2d 153, 156</a></span> (Tex. Civ. App. 1980) (“We may concede that a person falsely imprisoned has the right to sue on the first day for his detention”).</p>
</footnote>
<footnote label="4">
<p id="b669-5"> Had petitioner filed suit upon his arrest and had his suit then been dismissed under <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span>, </em>the statute of limitations, absent tolling, would have run by the time he obtained reversal of his conviction. If under those circumstances he were not allowed to refile his suit, <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span> </em>would produce immunity from § 1983 liability, a result surely not intended. Because in the present case petitioner did not file his suit within the limitations period, we need not decide, had he done so, how much time he would have had to refile the suit once the <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span> </em>bar was removed.</p>
</footnote>
<footnote label="5">
<p id="b669-6"> Justice Stevens reaches the same result by arguing that, under <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U. S. 465</a></span> (1976), the <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span> </em>bar can never come into play in a § 1983 suit seeking damages for a Fourth Amendment violation, so that “a habeas remedy was never available to [petitioner] in the first place.” <em>Post, </em>at 399 (opinion concurring in judgment). This reads <em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span> </em>to say more than it does. Under <em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span>, </em>Fourth Amendment violations are <em>generally </em>not cognizable on federal habeas, but they <em>are </em>cognizable when the State has failed to provide the habeas petitioner “an opportunity for full and fair litigation of a Fourth Amendment claim.” <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#482" aria-description="Citation for case: Stone v. Powell">428 U. S., at 482</a></span>. Federal habeas petitioners have sometimes succeeded in arguing that <em>Stone’s </em>general prohibition does not apply. See, <em>e.g., Herrera </em>v. <em>LeMaster, </em><span class="citation" data-id="160180"><a href="/opinion/160180/herrera-v-lemaster/#1178" aria-description="Citation for case: Herrera v. Lemaster">225 F. 3d 1176, 1178</a></span> (2000), aff’d on this point, <span class="citation" data-id="778969"><a href="/opinion/778969/ruben-r-herrera-v-tim-lemaster-warden-new-mexico-state-penitentiary/#1195" aria-description="Citation for case: Ruben R. Herrera v. Tim Lemaster, Warden, New Mexico...">301 F. 3d 1192, 1195, n. 4</a></span> (CA10 2002) (en banc); <em>United States ex rel. Bostick </em>v. <em>Peters, </em><span class="citation" data-id="6927870"><a href="/opinion/7026298/united-states-ex-rel-bostick-v-peters/#1029" aria-description="Citation for case: United States ex rel. Bostick v. Peters">3 F. 3d 1023, 1029</a></span> (CA7 1993); <em>Agee </em>v. <em>White, </em><span class="citation" data-id="482073"><a href="/opinion/482073/wayne-anthony-agee-v-jd-white-warden-and-attorney-general-of-the-state/#1490" aria-description="Citation for case: Wayne Anthony Agee v. J.D. White, Warden and Attorney...">809 F. 2d 1487, 1490</a></span> (CA11 1987); <em>Doescher </em>v. <em>Estelle, </em><span class="citation" data-id="397907"><a href="/opinion/397907/john-d-doescher-v-w-j-estelle-director-texas-department-of/#287" aria-description="Citation for case: John D. Doescher v. W. J. Estelle, Director, Texas...">666 F. 2d 285, 287</a></span> (CA5 1982); <em>Boyd </em>v. <em>Mintz, </em><span class="citation" data-id="382311"><a href="/opinion/382311/rodney-t-boyd-v-ira-mintz-superintendent-of-the-new-jersey-adult/#250" aria-description="Citation for case: Rodney T. Boyd v. Ira Mintz, Superintendent of the New...">631 F. 2d 247, 250-251</a></span> (CA3 1980); see also 2 R. Hertz &amp; J. Liebman, Federal Habeas Corpus Practice and Procedure §§27.1-27.3, pp. 1373-1389 (5th ed. 2005). At the time of a Fourth Amendment wrong, and at the time of conviction, it cannot be known whether a prospective § 1983 plaintiff will receive a full and fair opportunity to litigate his Fourth Amendment claim. It thus remains the case that a conflict with the federal ha<page-number citation-index="1" label="396">*396</page-number>beas statute is possible, that a Fourth Amendment claim can necessarily imply the invalidity of a conviction, and that if it does it must, under <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span>, </em>be dismissed.</p>
<p id="b670-6">Insofar as Justice Stevens simply suggests that <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span> </em>has no bearing here because <em>petitioner </em>received a full and fair opportunity to litigate his Fourth Amendment claim in state court, the argument is equally untenable. At the time that petitioner became detained pursuant to legal process, it was impossible to predict whether this would be true. And even at the point when his limitations period ended, state proceedings on his conviction were ongoing; full and fair opportunity up to that point was not enough. <em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span> </em>requires full and fair opportunity to litigate a Fourth Amendment claim “at trial <em>and on direct review.” </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#494" aria-description="Citation for case: Stone v. Powell">428 U. S., at 494-495, n. 37</a></span> (emphasis added).</p>
</footnote>
</opinion>
```

---
