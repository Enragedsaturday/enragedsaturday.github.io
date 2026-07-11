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

## GROUP: _overhaul2/lake/cases/reid-v-georgia--110336.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "928e4c56e39660ed", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "reid-v-georgia--110336"}, "payload": {"all": [{"cite": "448 U.S. 438", "page": "438", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "448"}, {"cite": "100 S. Ct. 2752", "page": "2752", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "100"}, {"cite": "65 L. Ed. 2d 890", "page": "890", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "65"}, {"cite": "1980 U.S. LEXIS 148", "page": "148", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1980"}], "display": null, "official": null, "official_selection_present": false, "record_id": "reid-v-georgia--110336"}}
{"assertion_id": "6f416f7420f9d7cd", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "reid-v-georgia--110336"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "reid-v-georgia--110336", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — reid-v-georgia--110336

```json
{
  "schema_version": "s2.v1",
  "record_id": "reid-v-georgia--110336",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Reid v. Georgia",
    "case_name_short": "Reid",
    "case_name_full": "Reid v. Georgia",
    "input_case_name": "Reid v. Georgia",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-06-30",
    "year": 1980,
    "docket": null,
    "cluster_id": 110336,
    "lead_opinion_id": 9428067,
    "sibling_ids": [],
    "absolute_url": "/opinion/110336/reid-v-georgia/",
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
        "cite": "448 U.S. 438",
        "volume": "448",
        "reporter": "U.S.",
        "page": "438",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 2752",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2752",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 890",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "890",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 148",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "148",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "448 U.S. 438",
        "volume": "448",
        "reporter": "U.S.",
        "page": "438",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 2752",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2752",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 890",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "890",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 148",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "148",
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
    "date_created": "2026-07-06T13:51:13Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:51:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:51:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:51:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:51:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — reid-v-georgia--110336

```
<opinion type="majority">
<author id="b470-12">Per Curiam.</author>
<p id="b470-13">The petitioner was indicted in the Superior Court of Fulton County, Ga., for possessing cocaine. At a hearing before trial, he moved to suppress the introduction of the cocaine as evidence against him on the ground that it had been seized from him by an agent of the federal Drug Enforcement Administration (DEA) in violation of his rights under the Fourth and Fourteenth Amendments.</p>
<p id="b471-3"><page-number citation-index="1" label="439">*439</page-number>The relevant facts were determined at the pretrial hearing and may be recounted briefly. The petitioner arrived at the Atlanta Airport on a commercial airline flight from Fort Lau-derdale, Fla., in the early morning hours of August 14, 1978. The passengers left the plane in a single file and proceeded through the concourse. The petitioner was observed by an agent of the DEA, who was in the airport for the purpose of uncovering illicit commerce in narcotics. Separated from the petitioner by several persons was another man, who carried a shoulder bag like the one the petitioner carried. As they proceeded through the concourse past the baggage claim area, the petitioner occasionally looked backward in the direction of the second man. When they reached the main lobby of the terminal, the second man caught up with the petitioner and spoke briefly with him. They then left the terminal building together.</p>
<p id="b471-4">The DEA agent approached them outside of the building, identified himself as a federal narcotics agent, and asked them to show him their airline ticket stubs and identification, which they did. The airline tickets had been purchased with the petitioner’s credit card and indicated that the men had stayed in Fort Lauderdale only one day. According to the agent’s testimony, the men appeared nervous during the encounter. The agent then asked them if they would agree to return to the terminal and to consent to a search of their persons and their shoulder bags. The agent testified that the petitioner nodded his head affirmatively, and that the other responded, “Yeah, okay.” As the three of them entered the terminal, however, the petitioner began to run and before he was apprehended, abandoned his shoulder bag. The bag, when recovered, was found to contain cocaine.</p>
<p id="b471-5">The Superior Court granted the petitioner’s motion to suppress the cocaine, concluding that it had been obtained as a result of a seizure of him by the DEA agent without an articu-lable suspicion that he was unlawfully carrying narcotics. The Georgia Court of Appeals reversed. <span class="citation" data-id="1304557"><a href="/opinion/1304557/state-v-reid/" aria-description="Citation for case: State v. Reid">149 Ga. App. 685</a></span>, <page-number citation-index="1" label="440">*440</page-number><span class="citation" data-id="1304557"><a href="/opinion/1304557/state-v-reid/" aria-description="Citation for case: State v. Reid">255 S. E. 2d 71</a></span>. It held that the stop of the petitioner was permissible, citing <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), since the petitioner, “in a number df respects, fit a 'profile’ of drug couriers compiled by the [DEA].” <span class="citation" data-id="1304557"><a href="/opinion/1304557/state-v-reid/#686" aria-description="Citation for case: State v. Reid">149 Ga. App., at 686</a></span>, <span class="citation" data-id="1304557"><a href="/opinion/1304557/state-v-reid/#72" aria-description="Citation for case: State v. Reid">255 S. E. 2d, at 72</a></span>. The appellate court also concluded that the petitioner had consented to return to the terminal for a search of his person, and that after he had attempted to flee and had discarded his shoulder bag, there existed probable cause for the search of the bag.</p>
<p id="b472-4">The Fourth and Fourteenth Amendments’ prohibition of searches and seizures that are not supported by some objective justification governs all seizures of the person, “including seizures that involve only a brief detention short of traditional arrest. <em>Davis </em>v. <em>Mississippi, </em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969); <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 16-19</a></span> (1968) <em>” United States </em>v. <em>Brignoni</em>-<em>Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975)1.<footnotemark>*</footnotemark> While the Court has recognized that in some circumstances a person may be detained briefly, without probable cause to arrest him, any curtailment of a person’s liberty by the police must be' supported at least by a reasonable and articulable suspicion that, the person seized is engaged in criminal activity. See <em>Brown </em>v. <em>Texas, </em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 51</a></span> (1979); <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#661" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 661</a></span> (1979); <em>United States </em>v. <em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce, supra;</a></span> Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 146-149</a></span> (1972); <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra.</a></span></em></p>
<p id="b472-5">The appellate court’s, conclusion in this case that the DEA agent reasonably suspected the petitioner of wrongdoing rested on the fact that the petitioner appeared to the agent to - fit the so-called “drug courier profile,” a somewhat informál compilation of characteristics believed tó be typical of persons unlawfully carrying narcotics. Specifically, the court thought <page-number citation-index="1" label="441">*441</page-number>it relevant that (1) the petitioner had arrived from Fort Lauderdale, which the agent testified is a principal place of origin of cocaine sold elsewhere in the country, (2) the petitioner arrived in the early morning, when law enforcement activity is diminished, (3) he and his companion appeared to the agent to be trying to conceal the fact that they were traveling together, and (4) they apparently had no luggage other than their shoulder bags.</p>
<p id="b473-5">We conclude that the agent could not, as a matter of law, have reasonably suspected the petitioner of criminal activity on the basis of these observed circumstances. Of the evidence relied on, only the fact that the petitioner preceded another person and occasionally looked backward at him as they proceeded through the concourse relates to their particular conduct. The other circumstances describe a very large category of presumably innocent travelers, who would be subject to virtually random seizures were the Court to conclude that as little foundation as there was in this case could justify a seizure. Nor can we agree, on this record, that the manner in which the petitioner and his companion walked through the airport reasonably could have led the agent to suspect them of wrongdoing. Although there could, of course, be circumstances in which wholly lawful conduct might justify the suspicion that criminal activity was afoot, see <em>Terry </em>v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><em>Ohio, supra, </em>at 27-28</a></span>, this is not such a case. The agent’s belief that the petitioner and his companion were attempting to conceal the fact that they were traveling together, a belief that was more an “inchoate and unparticularized suspicion or ‘hunch/ <em>” </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 27</a></span>, than a fair inference in the light of his experience, is simply too slender a reed to support the seizure in this case.</p>
<p id="b473-6">For these reasons, the judgment of the appellate court cannot be sustained insofar as it rests on the determination that the DEA agent lawfully seized the petitioner when he approached him outside the airline terminal. Accordingly, the petition for certiorari is granted, the judgment of the Georgia <page-number citation-index="1" label="442">*442</page-number>Court of Appeals is vacated, and the case is remanded to that court for further proceedings not inconsistent with this opinion.</p>
<p id="b474-4">
<em>It is so ordered.</em>
</p>
<footnote label="*">
<p id="b472-6">“Obviously, not all personal intercourse between policemen and citi- • zens involves ‘seizures’ of persons. Only when the officer, by means of physical force or show of authority, has in some way restrained the liberty of a citizen may we conclude that a seizure has occurred.” <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1,19, n. 16</a></span> (1968). See also <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio"><em>id., </em>at 34</a></span> (White, J., concurring) ; <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#31" aria-description="Citation for case: Terry v. Ohio"><em>id., </em>at 31, 32-33</a></span> (Harlan, J.,-concurring).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/state-v-andrews--4335207.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bf38bfbe2235d92d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "state-v-andrews--4335207"}, "payload": {"all": [{"cite": "2016 Ohio 8517", "page": "8517", "reporter": "Ohio", "selected_official": false, "source": "cluster.citations[]", "type": 8, "volume": "2016"}], "display": null, "official": null, "official_selection_present": false, "record_id": "state-v-andrews--4335207"}}
{"assertion_id": "418d9f862c6e3eaa", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "state-v-andrews--4335207"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "state-v-andrews--4335207", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — state-v-andrews--4335207

```json
{
  "schema_version": "s2.v1",
  "record_id": "state-v-andrews--4335207",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "State v. Andrews",
    "case_name_short": "Andrews",
    "case_name_full": "",
    "input_case_name": "State v. Andrews",
    "court": "Maryland Ct. of Special Appeals",
    "court_id": null,
    "court_level": "other",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2016,
    "docket": null,
    "cluster_id": 4335207,
    "lead_opinion_id": 4112468,
    "sibling_ids": [],
    "absolute_url": "/opinion/4335207/state-v-andrews/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2016 Ohio 8517",
        "volume": "2016",
        "reporter": "Ohio",
        "page": "8517",
        "type": 8,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "2016 Ohio 8517",
        "volume": "2016",
        "reporter": "Ohio",
        "page": "8517",
        "type": 8,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "other",
      "selected": null,
      "reason": "unlisted_reporter:Ohio"
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
    "date_created": "2026-07-06T13:12:19Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:12:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:12:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:12:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:12:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — state-v-andrews--4335207

```
[Cite as State v. Andrews, 2016-Ohio-8517.]


                                   IN THE COURT OF APPEALS

                               ELEVENTH APPELLATE DISTRICT

                                        LAKE COUNTY, OHIO


STATE OF OHIO,                                   :       OPINION

                 Plaintiff-Appellee,             :
                                                         CASE NO. 2016-L-048
        - vs -                                   :

ANTHONY R. ANDREWS, JR.,                         :

                 Defendant-Appellant.            :


Criminal Appeal from the Lake County Court of Common Pleas, Case No. 2016 CR
000021.

Judgment: Affirmed.


Charles E. Coulson, Lake County Prosecutor, and Teri R. Daniel, Assistant Prosecutor,
Lake County Administration Building, 105 Main Street, P.O. Box 490, Painesville, OH
44077 (For Plaintiff-Appellee).

Charles R. Grieshammer, Lake County Public Defender, and Vanessa R. Clapp,
Assistant Public Defender, 125 East Erie Street, Painesville, OH 44077 (For
Defendant-Appellant).



THOMAS R. WRIGHT, J.


        {¶1}     Appellant, Anthony J. Andrews, Jr., appeals the length of the prison terms

imposed by the trial court following his conviction on two felony offenses. He contends

that his sentence is contrary to law because the trial court did not accord proper weight

to various factors that supported shorter terms. For the following reasons, the imposed

sentence is upheld.
         {¶2}   In February 2016, appellant was indicted on two counts of theft, one count

of illegal conveyance of drugs of abuse onto the grounds of a governmental facility, one

count of aggravated possession of drugs, and one count of possession of heroin. The

theft counts were based upon an incident in which appellant entered a hardware store

with two other men, placed two sinks and two faucets on a shopping cart, took the items

to the front of the store and told a clerk that he was returning the items, and was given a

gift card for the value of the items. The three drug counts were predicated upon the fact

that, after appellant was arrested for the theft and searched at a local city jail, an officer

found two pieces of paper on his person that contained heroin and fentanyl.

         {¶3}   On the date he committed the theft offense, appellant was on post-release

control, having served a nine-month sentence on a prior theft and forgery conviction in

the same trial court. That sentence constituted the fifth prison term he had served as an

adult.

         {¶4}   After receiving discovery from the state, appellant agreed to plead guilty to

one count of theft, a fifth-degree felony under R.C. 2913.02(A), and an amended count

of attempted illegal conveyance of drugs of abuse onto the grounds of a governmental

facility, a fourth-degree felony under R.C. 2921.36(A) and 2923.02(A). The latter count

also had a forfeiture specification regarding the contraband found on appellant’s person.

Upon accepting the plea, the trial court found him guilty of the two offenses and referred

the case to the county adult probation department for the preparation of a presentencing

investigation report and a drug and alcohol evaluation.

         {¶5}   At sentencing, appellant asserted that the imposition of short prison terms

for the two offenses was justified because his theft of the funds from the hardware store




                                              2
was directly attributable to his addiction to illegal drugs; i.e., he needed the funds to buy

more drugs and provide for his children. As to this point, he claimed that he had been

able to stay “clean” following his most recent prison term until he injured himself at work,

and that his reliance upon pain pills had led him to begin using heroin. Appellant also

noted that the short terms were warranted because he had become more involved in his

children’s lives since being released from prison. In rejecting these arguments, the trial

court cited: (1) appellant’s extensive criminal record, both as an adult and a juvenile; (2)

his multiple probation violations; and (3) the fact that he quit attending a drug treatment

program immediately prior to his commission of the theft offense.

       {¶6}   In light of the foregoing factors, the trial court sentenced appellant to two

consecutive terms of eleven months on the theft offense and seventeen months on the

“illegal conveyance” offense. In addition, the trial court imposed a separate consecutive

term of eight months on the post-release control violation stemming from his 2012 theft

and forgery convictions. Thus, appellant was ordered to serve an aggregate sentence

of thirty-six months.

       {¶7}   After the trial court restated the sentence in its final judgment, appellant

timely appealed, raising one assignment of error:

       {¶8}   “The trial court erred by sentencing the defendant-appellant to a

consecutive, thirty-six month prison term.”

       {¶9}   In maintaining that the length of the each imposed prison term is too long

under the facts of this case, appellant asserts that the trial court did not give adequate

weight to sentencing factors under R.C. 2929.12 which tended to show the offenses he

committed were not overly serious. He argues that the trial court failed to consider the




                                              3
undisputed facts that he had a serious addiction problem, he had previously shown that

he could be successful when his addiction was under control, he needed more money

to properly provide for his children, and he was remorseful for his actions.

       {¶10} Appellate review of a felony sentence is governed by R.C. 2953.08(G)(2),

which provides:

       {¶11} “The court hearing an appeal under division (A), (B), or (C) of this section

shall review the record, including the findings underlying the sentence or modification

given by the sentencing court.

       {¶12} “The appellate court may increase, reduce, or otherwise modify a

sentence that is appealed under this section or may vacate the sentence and remand

the matter to the sentencing court for resentencing. The appellate court’s standard for

review is not whether the sentencing court abused its discretion. The appellate court

may take any action authorized by this division if it clearly and convincingly finds either

of the following:

       {¶13} “(a) That the record does not support the sentencing court’s findings under

division (B) or (D) of section 2929.13, division (B)(2)(e) or (C)(4) of section 2929.14, or

division (I) of section 2929.20 of the Revised Code, whichever, if any, is relevant;

       {¶14} “(b) That the sentence is otherwise contrary to law.”

       {¶15} In analyzing the statutory standard, this court has stated:

       {¶16} “R.C. 2953.08(G)(2) provides a two-step analysis for reviewing the

imposition of a felony sentence. Specifically, an appellate court must affirm the felony

sentence unless: (1) the trial court’s findings on applicable mandatory requirements are

not supported by the record; or (2) the sentence is not consistent with other relevant




                                             4
aspects of the law. State v. Robinson, 1st Dist. Hamilton No. C-140043, 2015-Ohio-

773, ¶38.” State v. Talley, 11th Dist. Trumbull No. 2014-T-0098, 2015-Ohio-2816, ¶15.

       {¶17} In this case, appellant essentially claims that the materials before the trial

court did not support its findings under R.C. 2929.12 as to the seriousness of the crimes

and the likelihood of future criminal behavior. However, R.C. 2929.12 is not one of the

statutory provisions listed in R.C. 2953.08(G)(2)(a). As a result, the scope of our review

is limited to the second step of the R.C. 2953.08(G)(2) standard: i.e., is the imposition of

the eleven and seventeen month terms contrary to law? As a general proposition, “the

imposition of any sentence for an individual offense is not contrary to law if the term falls

within the statutory range for that particular offense and the record demonstrates that

the trial court considered the purposes and principles of felony sentencing, as stated in

R.C. 2929.11, and the sentencing factors of seriousness and recidivism, as delineated

in R.C. 2929.12. State v. Marcum, 146 Ohio St.3d 516, 2016-Ohio-1002, ¶23; State v.

Hayes, 2nd Dist. Clark No. 2014-CA-27, 2014-Ohio-5362, ¶15-16.” State v. Lough,

11th Dist. Trumbull No. 2015-T-0093, 2015-Ohio-3513, ¶18.

       {¶18} Since the value of the property appellant stole was between $1,000 and

$7,500, the offense of theft is a fifth-degree felony. R.C. 2913.02(B)(2). For this degree

of felony, a trial court can only impose a term of six, seven, nine, ten, eleven, or twelve

months. R.C. 2929.14(A)(5). Thus, the imposed term of eleven months fell within the

statutory range.

       {¶19} When the crime of illegal conveyance upon the grounds of a governmental

facility involves a drug of abuse, it is deemed a third-degree felony. R.C. 2921.36(G)(2).

In turn, since appellant’s conviction was for attempted illegal conveyance, the degree of




                                             5
his offense would be one degree less: i.e., a fourth-degree felony. R.C. 2923.02(E)(1).

For this degree of felony, the permissible range of jail terms is between six and eighteen

months. R.C. 2929.14(A)(4). Accordingly, the imposed term of seventeen months was

in compliance with the governing law.

       {¶20} Furthermore, the trial court expressly stated during the sentencing hearing

and in its final sentencing judgment that, prior to imposing the sentence, it considered

the statutory guidelines set forth in R.C. 2929.11 and 2929.12. The court also provided

a lengthy discussion of the R.C. 2929.12 sentencing factors during the hearing. To this

extent, the record shows that the trial court employed the correct procedure in deciding

the length of the respective prison terms.

       {¶21} As to the merits of the trial court’s R.C. 2929.12 analysis, appellant argues

that the court failed to acknowledge those factors that tended to show his crimes were

not as serious as the usual forms of those offenses. Yet, the record establishes that the

trial court cited many of the factors favorable to appellant during its oral discussion. For

example, the court recognized he had a serious drug problem. Nevertheless, the trial

court concluded that the factors cited by appellant as to the “seriousness” issue were

readily outweighed by other factors supporting the finding that he was likely to commit

new crimes in the future.

       {¶22} This conclusion was based upon appellant’s substantial criminal record as

a juvenile and an adult. Prior to becoming an adult, he was convicted of nine separate

crimes, including five theft offenses. After turning eighteen, he was convicted of twenty-

five additional crimes, including the two in this case. Of those twenty-five convictions,

twenty-one were for felony offenses. Furthermore, as a result of those convictions, he




                                             6
had served five separate prison terms as an adult.

         {¶23} The record before the trial court also established that appellant could not

be trusted to abide by any restrictions upon his behaviors. Specifically, he was found

guilty of two probation violations as a juvenile and three as an adult. The last of the five

violations occurred in a 2012 case before the same trial court, in which appellant was

convicted of one count of theft and three counts of forgery. Only one day after being

granted probation for four years, he was cited for submitting a fictitious letter regarding

his alleged employment.

         {¶24} Appellant argued at the trial level that, despite his many prior convictions,

he was never afforded treatment for his drug addiction. However, he did not dispute the

fact that, immediately prior to his commission of the two offenses underlying this case,

he had stopped attending a local drug treatment program after only three visits. In light

of this, the materials before the trial court justified the conclusion that appellant was not

serious about dealing with his drug addiction.

         {¶25} Taken as a whole, the record contains considerable evidence supporting

the trial court’s analysis of the R.C. 2929.12 sentencing factors governing seriousness

of the offenses and recidivism. Accordingly, appellant has failed to demonstrate that the

trial court’s decision to impose prison terms of eleven and seventeen months is clearly

and convincingly contrary to law. The imposition of longer terms is warranted in light of

appellant’s clear inability to control his own behavior. Appellant’s sole assignment lacks

merit.

         {¶26} The judgment of the Lake County Court of Common Pleas is affirmed.




                                              7

```

---

## GROUP: _overhaul2/lake/cases/uniformed-sanitation-men-assn-inc-v-commissioner-of-sanitation--107739.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bdb331e47af6ce66", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "uniformed-sanitation-men-assn-inc-v-commissioner-of-sanitation--107739"}, "payload": {"all": [{"cite": "392 U.S. 280", "page": "280", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "392"}, {"cite": "88 S. Ct. 1917", "page": "1917", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "88"}, {"cite": "20 L. Ed. 2d 1089", "page": "1089", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "20"}, {"cite": "1968 U.S. LEXIS 1352", "page": "1352", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1968"}], "display": null, "official": null, "official_selection_present": false, "record_id": "uniformed-sanitation-men-assn-inc-v-commissioner-of-sanitation--107739"}}
{"assertion_id": "b55c503f5ab65200", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "uniformed-sanitation-men-assn-inc-v-commissioner-of-sanitation--107739"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "uniformed-sanitation-men-assn-inc-v-commissioner-of-sanitation--107739", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — uniformed-sanitation-men-assn-inc-v-commissioner-of-sanitation--107739

```json
{
  "schema_version": "s2.v1",
  "record_id": "uniformed-sanitation-men-assn-inc-v-commissioner-of-sanitation--107739",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Uniformed Sanitation Men Ass'n v. Commissioner of Sanitation of New York",
    "case_name_short": "",
    "case_name_full": "UNIFORMED SANITATION MEN ASSN., INC., Et Al. v. COMMISSIONER OF SANITATION OF THE CITY OF NEW YORK Et Al.",
    "input_case_name": "Uniformed Sanitation Men Assn., Inc. v. Commissioner of Sanitation",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-06-10",
    "year": 1968,
    "docket": null,
    "cluster_id": 107739,
    "lead_opinion_id": 9423788,
    "sibling_ids": [],
    "absolute_url": "/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/",
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
        "cite": "392 U.S. 280",
        "volume": "392",
        "reporter": "U.S.",
        "page": "280",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 1917",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1917",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 1089",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "1089",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 1352",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1352",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "392 U.S. 280",
        "volume": "392",
        "reporter": "U.S.",
        "page": "280",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 1917",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1917",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 1089",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "1089",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 1352",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1352",
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
    "date_created": "2026-07-06T13:48:22Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:48:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:48:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:48:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:48:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — uniformed-sanitation-men-assn-inc-v-commissioner-of-sanitation--107739

```
<opinion type="majority">
<author id="b323-4">Mr. Justice Fortas</author>
<p id="AR">delivered the opinion of the Court.</p>
<p id="b323-5">The individual petitioners are 15 employees of the Department of Sanitation of New York City. Claiming they were wrongfully dismissed from employment in violation of their rights under the United States Constitution, they commenced this action for declaratory judgment and injunctive relief in the United States District Court for the Southern District of New York. That court dismissed the action and the Court of Appeals for the Second Circuit affirmed. <span class="citation multiple-matches"><a href="/c/F.%202d/383/364/">383 F. 2d 364</a></span> (1967). We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./390/919/">390 U. S. 919</a></span> (1968).</p>
<p id="b323-6">Sometime in 1966, the Commissioner of Investigation of New York City<footnotemark>1</footnotemark> began an investigation of charges that employees of the Department of Sanitation were not charging private cartmen proper fees for use of certain city facilities and were diverting to themselves the proceeds of fees that they did charge. The Commissioner obtained an order from the Supreme Court in New York County authorizing him to tap a telephone leased by the Department of Sanitation for the transaction of official business at the city facilities in question.<footnotemark>2</footnotemark></p>
<p id="b323-7">In November 1966 each of the petitioners was summoned before the Commissioner. Each was advised that, in accordance with § 1123 of the New York City Charter, <page-number citation-index="1" label="282">*282</page-number>if he refused to testify with respect to his official conduct or that of any other city employee on the grounds of self-incrimination, his employment and eligibility for other city employment would terminate.<footnotemark>3</footnotemark></p>
<p id="b324-4">Twelve of the petitioners, asserting the constitutional privilege against self-incrimination, refused to testify. After a disciplinary hearing held pursuant to § 75 of the New York Civil Service Law, they were dismissed by the Commissioner of Sanitation on the explicit ground provided by § 1123 of the City Charter that they had refused to testify.</p>
<p id="b324-5">Three of the petitioners answered the questions put to them, denying the charges made. They were thereafter suspended by the Commissioner of Sanitation on the basis of “information received from the Commissioner of Investigation concerning irregularities arising out of [their] employment in the Department of Sanitation.” Subsequently, they were summoned before a grand jury and asked to sign waivers of immunity. They refused. Administrative hearings were held pursuant to § 75 of the Civil Service Law, and they were dismissed from employment on the sole ground that they had <page-number citation-index="1" label="283">*283</page-number>violated § 1123 of the City Charter by refusing to sign waivers of immunity. We consider only the dismissal, rather than the suspension, of these petitioners.</p>
<p id="b325-4">Relying upon the decision of the New York Court of Appeals in <em>Gardner </em>v. <em>Broderick, </em>20 N. Y. 2d 227, <span class="citation" data-id="5523781"><a href="/opinion/5676083/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">229 N. E. 2d 184</a></span> (1967) (reversed this day, <em>ante, </em>p. 273), the Court of Appeals for the Second Circuit held that the dismissal of petitioners did not offend the Federal Constitution. For the reasons which we elaborate in our opinion reversing the New York court’s decision in <em>Gardner </em>v. <em><span class="citation" data-id="5523781"><a href="/opinion/5676083/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">Broderick, supra,</a></span> </em>we hold that the Court of Appeals erred.</p>
<p id="b325-5">Petitioners were not discharged merely for refusal to account for their conduct as employees of the city. They were dismissed for invoking and refusing to waive their constitutional right against self-incrimination. They were discharged for refusal to expose themselves to criminal prosecution based on testimony which they would give under compulsion, despite their constitutional privilege. Three were asked to sign waivers of immunity before the grand jury. Twelve were told that their answers to questions put to them by the Commissioner of Investigation could be used against them in subsequent proceedings,<footnotemark>4</footnotemark> and were discharged for refusal to <page-number citation-index="1" label="284">*284</page-number>answer the questions on this basis. <em>Garrity </em>v. <em>New Jersey, </em><span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">385 U. S. 493</a></span> (1967), in which we held that testimony compelled by threat of dismissal from employment could not be used in a criminal prosecution of the witness, had not been decided when these 12 petitioners were put to their hazardous choice. In any event, we need not decide whether these petitioners would have effectively waived this constitutional protection if they had testified following the warning that their testimony could be used against them. They were entitled to remain silent because it was clear that New York was seeking, not merely an accounting of their use or abuse of their public trust, but testimony from their own lips which, despite the constitutional prohibition, could be used to prosecute them criminally.<footnotemark>5</footnotemark></p>
<p id="b326-6">As we stated in <em>Gardner </em>v. <em><span class="citation" data-id="5523781"><a href="/opinion/5676083/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">Broderick, supra,</a></span> </em>if New York had demanded that petitioners answer questions specifically, directly, and narrowly relating to the performance of their official duties on pain of dismissal from public employment without requiring relinquishment of the benefits of the constitutional privilege, and if they had refused to do so, this case would be entirely different. In such a case, the employee’s right to immunity as a result of his compelled testimony would not be at stake. But here the precise and plain impact of the proceedings against petitioners as well as of § 1123 of the New York Charter was to present them with a choice between surrendering their constitutional rights or their jobs. Petitioners as public employees are entitled, like all other persons, to the benefit of the Con<page-number citation-index="1" label="285">*285</page-number>stitution, including the privilege against self-incrimination. <em>Gardner </em>v. <em><span class="citation" data-id="5523781"><a href="/opinion/5676083/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">Broderick, supra;</a></span> Garrity </em>v. <em>New <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Jersey, supra.</a></span> </em>Cf. <em>Murphy </em>v. <em>Waterfront Commission, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#79" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, at 79</a></span> (1964). At the same time, petitioners, being public employees, subject themselves to dismissal if they refuse to account for their performance of their public trust, after proper proceedings, which do not involve an attempt to coerce them to relinquish their constitutional rights.</p>
<p id="b327-4">Accordingly, the judgment is reversed.<footnotemark>6</footnotemark></p>
<p id="b327-5">
<em>Reversed.</em>
</p>
<judges id="b327-6">Mr. Justice Black concurs in the result.</judges>
<footnote label="1">
<p id="b323-8"> Section 803, subd. 2, of the New York City Charter provides that the Commissioner “[i]s authorized and empowered to make any study or investigation which in his opinion may be in the best interests of the city, including but not limited to investigations of the affairs, functions, accounts, methods, personnel or efficiency of any agency.”</p>
</footnote>
<footnote label="2">
<p id="b323-9"> This order was pursuant to § 813-a of the Code of Criminal Procedure of New York. See <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967).</p>
</footnote>
<footnote label="3">
<p id="b324-6"> Section 1123 of the New York City Charter provides:</p>
<blockquote id="b324-7">“If any councilman or other officer or employee of the city shall, after lawful notice or process, wilfully refuse or fail to appear before any court or judge, any legislative committee, or any officer, board or body authorized to conduct any hearing or inquiry, or having appeared shall refuse to testify or to answer any question regarding the property, government or affairs of the city or of any county included within its territorial limits, or regarding the nomination, election, appointment or official conduct of any officer or employee of the city or of any such county, on the ground that his answer would tend to incriminate him, or shall refuse to waive immunity from prosecution on account of any such matter in relation to which he may be asked to testify upon any such hearing or inquiry, his term or tenure of office or employment shall terminate and such office or employment shall be vacant, and he shall not be eligible to election or appointment to any office or employment under the city or any agency.”</blockquote>
</footnote>
<footnote label="4">
<p id="b325-6"> The Commissioner said:</p>
<blockquote id="b325-7">“Mr. [name of witness], this is a private hearing being conducted by the Department of Investigation of the City of New York, pursuant to Chapter 34, of the New York City Charter. The investigation in which you are about to testify relates particularly to the affairs, functions, accounts, methods, personnel and efficiency of the Department of Sanitation of the City of New York. I wish to advise you that you have all the rights and privileges guaranteed by the laws of the State of New York and the Constitutions of this State and of the United States, including the right to remain silent and the right not to be compelled to be a witness against yourself. <em>I wish further to advise you that anything you say can be used against you in a court of law. </em>You have the right to have an attorney present <page-number citation-index="1" label="284">*284</page-number>at this hearing, if you wish, and I understand that you are represented by counsel in the person of [name of attorney], is that correct?” (Emphasis added.)</blockquote>
</footnote>
<footnote label="5">
<p id="b326-10"> As we noted in <em>Gardner </em>v. <span class="citation" data-id="5523781"><a href="/opinion/5676083/gardner-v-broderick/#278" aria-description="Citation for case: Gardner v. Broderick"><em>Broderick, supra, </em>at 278-279</a></span>, the possible ineffectiveness of this waiver does not change the fact that the State attempted to force petitioners, upon penalty of loss of employment, to relinquish a right guaranteed them by the Constitution.</p>
</footnote>
<footnote label="6">
<p id="b327-9"><em> </em>In view of our disposition of the ease, we do not reach the issues raised by petitioners with respect to the wiretap.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/united-states-v-ackerman--4245010.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ebc35e4a5729753e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "united-states-v-ackerman--4245010"}, "payload": {"all": [{"cite": "831 F.3d 1292", "page": "1292", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "831"}, {"cite": "2016 U.S. App. LEXIS 14411", "page": "14411", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2016"}, {"cite": "2016 WL 4158217", "page": "4158217", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2016"}], "display": null, "official": null, "official_selection_present": false, "record_id": "united-states-v-ackerman--4245010"}}
{"assertion_id": "2d86b93990717bf4", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-ackerman--4245010"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-ackerman--4245010", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-ackerman--4245010

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-ackerman--4245010",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "United States v. Ackerman",
    "case_name_short": "Ackerman",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Walter E. ACKERMAN, Defendant-Appellant. National Center for Missing and Exploited Children; Dropbox, Inc.; Facebook, Inc.; Google, Inc.; Microsoft Corporation; Pinterest, Inc.; Snapchat, Inc.; Twitter, Inc., Amici Curiae",
    "input_case_name": "United States v. Ackerman",
    "court": "10th Cir. 2016",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": "2016-08-05",
    "year": 2016,
    "docket": "14-3265",
    "cluster_id": 4245010,
    "lead_opinion_id": 4022271,
    "sibling_ids": [],
    "absolute_url": "/opinion/4245010/united-states-v-ackerman/",
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
        "cite": "831 F.3d 1292",
        "volume": "831",
        "reporter": "F.3d",
        "page": "1292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2016 U.S. App. LEXIS 14411",
        "volume": "2016",
        "reporter": "U.S. App. LEXIS",
        "page": "14411",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 4158217",
        "volume": "2016",
        "reporter": "WL",
        "page": "4158217",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "831 F.3d 1292",
        "volume": "831",
        "reporter": "F.3d",
        "page": "1292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 U.S. App. LEXIS 14411",
        "volume": "2016",
        "reporter": "U.S. App. LEXIS",
        "page": "14411",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 4158217",
        "volume": "2016",
        "reporter": "WL",
        "page": "4158217",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "other",
      "selected": null,
      "reason": "unlisted_reporter:F.3d"
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
    "date_created": "2026-07-06T13:51:03Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:51:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:51:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:51:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:51:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — united-states-v-ackerman--4245010

```
                                                                     FILED
                                                         United States Court of Appeals
                                                                 Tenth Circuit

                                                               August 5, 2016
                                          PUBLISH           Elisabeth A. Shumaker
                                                                Clerk of Court
                      UNITED STATES COURT OF APPEALS

                                    TENTH CIRCUIT


 UNITED STATES OF AMERICA,

        Plaintiff-Appellee,
 v.

 WALTER E. ACKERMAN,

        Defendant-Appellant.

 --------------------------------------------
                                                       No. 14-3265
 NATIONAL CENTER FOR MISSING
 AND EXPLOITED CHILDREN;
 DROPBOX, INC.; FACEBOOK, INC.;
 GOOGLE, INC.; MICROSOFT
 CORPORATION; PINTEREST, INC.;
 SNAPCHAT, INC.; TWITTER, INC.,

        Amici Curiae.


                    Appeal from the United States District Court
                             for the District of Kansas
                        (D.C. No. 6:13-CR-10176-EFM-1)


Daniel T. Hansmeier, Appellate Chief (Melody Brannon, Federal Public Defender,
with him on the briefs), Office of the Kansas Federal Public Defender, Kansas
City, Kansas, for Defendant-Appellant.

Jason W. Hart, Assistant United States Attorney (Barry R. Grissom, United States
Attorney, with him on the brief), Office of the United States Attorney, Wichita,
Kansas, for Plaintiff-Appellee.
Christopher J. Schmidt, Bryan Cave LLP, St. Louis, Missouri (Lee Marshall,
Bryan Cave LLP, San Francisco, California, and Logan Rutherford, Bryan Cave
LLP, Kansas City, Missouri, with him on the brief), for amicus curiae National
Center for Missing and Exploited Children, in support of Plaintiff-Appellee.

Eric D. Miller, Ryan T. Mrazik, Nicola Menaldo, Erin K. Earl, Perkins Coie LLP,
Seattle, Washington, for amici curiae Dropbox, Inc., Facebook, Inc., Google, Inc.,
Microsoft Corporation, Pinterest, Inc., Snapchat, Inc., and Twitter, Inc., in
support of Plaintiff-Appellee.


Before HARTZ, GORSUCH, and PHILLIPS, Circuit Judges.


GORSUCH, Circuit Judge, delivered the opinion of the Court, in which
PHILLIPS, J., joined. HARTZ, J., joined Parts I, II, III(A), and IV.


      Walter Ackerman’s email never made it to its intended recipient. It didn’t

because AOL, Mr. Ackerman’s internet service provider (ISP), has an automated

filter designed to thwart the transmission of child pornography. After that filter

identified one of four images attached to Mr. Ackerman’s email as child

pornography, AOL instantly stopped delivery and the company soon shuttered Mr.

Ackerman’s account.

      How does AOL’s screening system work? It relies on hash value matching.

A hash value is (usually) a short string of characters generated from a much larger

string of data (say, an electronic image) using an algorithm — and calculated in a

way that makes it highly unlikely another set of data will produce the same value.

Some consider a hash value as a sort of digital fingerprint. See Richard P.

Salgado, Fourth Amendment Search and the Power of the Hash, 119 Harv. L.

                                        -2-
Rev. F. 38, 38-40 (2005). AOL’s automated filter works by identifying the hash

values of images attached to emails sent through its mail servers. Those values

are then compared to the hash values of images that AOL employees have viewed

previously and deemed child pornography. Any email containing an image with a

matching hash value is automatically weeded out.

      As soon as AOL identified a hash value match in this case, the company

did just what federal law requires: it forwarded a report to the National Center

for Missing and Exploited Children (NCMEC) through an online tool called the

CyberTipline. AOL’s report included Mr. Ackerman’s email along with all four

attached images. A NCMEC analyst opened the email, viewed each of the

attached images, and confirmed that all four (not just the one AOL’s automated

filter identified) appeared to be child pornography. After the analyst determined

as well that Mr. Ackerman was the likely owner of the account, NCMEC alerted

law enforcement agents in the area where he lived. And not long after that, a

federal grand jury indicted Mr. Ackerman on charges of possession and

distribution of child pornography. At the end of it all, Mr. Ackerman entered a

conditional guilty plea but reserved his right to appeal the denial of his motion to

suppress the fruits of NCMEC’s investigation.

      We can appreciate why, for his motion raises (at least) two difficult

constitutional questions. Mr. Ackerman alleges that NCMEC’s actions amounted

to an unreasonable search of his email and its attachments because no one sought

                                        -3-
a warrant and no one invoked any recognized lawful basis for failing to seek one.

But the Fourth Amendment only protects against unreasonable searches

undertaken by the government or its agents — not private parties. So Mr.

Ackerman’s motion raises the question: does NCMEC qualify as a governmental

entity or agent? Even if it does, a second hard question remains. The Supreme

Court’s “private search” doctrine suggests the government doesn’t conduct a

Fourth Amendment “search” when it merely repeats an investigation already

conducted by a private party like AOL. Which raises this question: did NCMEC

simply repeat or did it exceed the scope of AOL’s investigation? For its part, the

district court denied Mr. Ackerman’s motion to suppress both because NCMEC is

not a governmental actor and, alternatively and in any event, because NCMEC’s

search didn’t exceed the scope of AOL’s private search.

      We find we must disagree.

                                         I

      Start with the question whether NCMEC qualifies as a governmental entity.

The problem of drawing a line between public and private entities is an old and

difficult one. Perhaps the Supreme Court’s first great tangle with the task came

in Trustees of Dartmouth College v. Woodward, 17 U.S. (4 Wheat.) 518, 668-69

(1819). There the Court suggested that the calling card of a governmental entity

is whether it is “invested with any portion of political power, partaking in any

degree in the administration of civil government, and performing duties which

                                        -4-
flow from the sovereign authority.” Id. at 634 (opinion of Marshall, C.J.). That

an entity might be incorporated, as NCMEC is, doesn’t prevent it from also

qualifying as a governmental entity: the dispositive question isn’t one of form

but function, turning on what the entity does, not how it is organized. So, for

example, a municipality may undoubtedly qualify both as a corporation and as a

governmental entity. See Philips v. Bury (1694) 90 Eng. Rep. 1294, 1299 (“There

are in law two sorts of corporations aggregate of many; such as are for publick

government, and such as are for private charity.”); 1 Joseph Stancliffe Davis,

Essays in the Earlier History of American Corporations 72-74 (1917).

      When it comes to what qualifies as a public, political, or sovereign

function, we know too that the “police function” is among the paradigmatic

examples. See Foley v. Connelie, 435 U.S. 291, 297 (1978) (describing the

“police function” as “one of the basic functions of government”); Flagg Bros.,

Inc. v. Brooks, 436 U.S. 149, 163 (1978) (noting that policing is among the “state

and municipal functions” that “have been administered with a greater degree of

exclusivity by States and municipalities”). Even before the rise of professional

police departments, a private person dragooned into a “posse comitatus” bore “the

same authority as the sheriff” and “was protected [by law] to the same extent.”

Filarsky v. Delia, 132 S. Ct. 1657, 1664 (2012); see also 1 William Blackstone,

Commentaries *332. To be sure, some cases have suggested that the mere

investigation of crime or temporary detention of suspected criminals by private

                                        -5-
security guards is not a uniquely public function. See, e.g., Gallagher v. “Neil

Young Freedom Concert,” 49 F.3d 1442, 1457 (10th Cir. 1995); Wade v. Byles,

83 F.3d 902, 905-06 (7th Cir. 1996); United States v. Garlock, 19 F.3d 441, 443-

44 (8th Cir. 1994). But that’s because the guards’ lawful authority to act in those

cases was no broader than that enjoyed by any private citizen — including the

right to carry a weapon, to use deadly force in self-defense, and to conduct a

citizen’s arrest. See Romanski v. Detroit Entm’t, L.L.C., 428 F.3d 629, 637-38

(6th Cir. 2005). Meanwhile, when an actor is endowed with law enforcement

powers beyond those enjoyed by private citizens, courts have traditionally found

the exercise of the public police power engaged. Id. at 637. 1

      NCMEC’s law enforcement powers extend well beyond those enjoyed by

private citizens — and in this way it seems to mark it as a fair candidate for a

governmental entity. NCMEC’s two primary authorizing statutes — 18 U.S.C.

§ 2258A and 42 U.S.C. § 5773(b) — mandate its collaboration with federal (as

well as state and local) law enforcement in over a dozen different ways, many of

which involve duties and powers conferred on and enjoyed by NCMEC but no

other private person. For example, NCMEC is statutorily obliged to operate the

      1
          Richardson v. McKnight, 521 U.S. 399 (1997), might appear an exception
to this rule, for there the Supreme Court held that certain private prison guards
weren’t state actors for purposes of qualified immunity. Id. at 412. But
Richardson was criticized at the time for elevating form over function, see id. at
414-18 (Scalia, J., dissenting), and since then the Court has both returned to
Dartmouth College’s tried and true approach and expressly limited Richardson to
its facts, see Filarsky, 132 S. Ct. at 1662-65, 1667.

                                        -6-
official national clearinghouse for information about missing and exploited

children, to help law enforcement locate and recover missing and exploited

children, to “provide forensic technical assistance . . . to law enforcement” to help

identify victims of child exploitation, to track and identify patterns of attempted

child abductions for law enforcement purposes, to “provide training . . . to law

enforcement agencies in identifying and locating non-compliant sex offenders,”

and of course to operate the CyberTipline as a means of combating Internet child

sexual exploitation. 42 U.S.C. § 5773(b). Responsibilities and rights Congress

has extended to NCMEC alone “under Federal law” and done so specifically “to

assist or support law enforcement agencies in administration of criminal justice

functions.” Id. § 16961(a)(1). This special relationship runs both ways, too, for

NCMEC is also empowered to call on various federal agencies for unique forms

of assistance in aid of its statutory functions. See 18 U.S.C. § 3056(f)

(authorizing the U.S. Secret Service to provide, “at the request of” NCMEC,

“forensic and investigative assistance in support of any investigation involving

missing or exploited children”).

      Focusing in particular on NCMEC’s CyberTipline functions, the functions

at issue in this case, illustrates and confirms the special law enforcement duties

and powers it enjoys. First, NCMEC and NCMEC alone is statutorily obliged to

maintain an electronic tipline for ISPs to use to report possible Internet child

sexual exploitation violations to the government. Under the statutory scheme,

                                         -7-
NCMEC is obliged to forward every single report it receives to federal law

enforcement agencies and it may make its reports available to state and local law

enforcement as well. See id. § 2258A(c).

      Second, ISPs must report any known child pornography violations to

NCMEC. Not to any other governmental agency, but again to NCMEC and

NCMEC alone. ISPs who fail to comply with this obligation face substantial (and

apparently criminal) penalties payable to the federal government. Id.

§ 2258A(a)(1), (e); see also Child Exploitation & Obscenity Section, Frequently

Asked Questions (FAQs), U.S. Dep’t Just., https://www.justice.gov/criminal-ceos/

frequently-asked-questions-faqs (last visited July 7, 2016) (“If the ISP knowingly

and willfully fails to report the apparent violation, it is subject to criminal

penalties.”).

      Third, when NCMEC confirms it has received a report the ISP must treat

that confirmation as a request to preserve evidence issued by the government

itself. Compare 18 U.S.C. § 2258A(h)(1) (“[T]he notification to an [ISP] . . . by

the CyberTipline of receipt of a report . . . shall be treated as a request to

preserve, as if such request was made pursuant to section 2703(f).”), with id.

§ 2703(f)(1) (“A[n ISP] . . . , upon the request of a governmental entity, shall take

all necessary steps to preserve records and other evidence in its possession

. . . .”). Failure to comply again opens an ISP to potential civil or criminal

sanctions. See id. § 2258B.

                                         -8-
      Fourth, in aid of its tipline functions NCMEC is statutorily authorized to

receive contraband (child pornography) knowingly and to review its contents

intentionally. Id. § 2258A(a), (b)(4); NCMEC Amicus Br. at 20-21. Actions that

would normally subject private persons to criminal prosecution. See 18 U.S.C.

§ 2252A(a)(2) (knowing receipt or distribution); id. § 2252A(a)(5)(B) (knowing

possession or access with intent to view). But actions that Congress allows

NCMEC to take precisely because of the unique value it provides in the

prosecution of child exploitation crimes. See R. vol. 3 at 198-99. Of course,

Congress also provides that ISPs who forward and preserve images of child

pornography in accord with the law may not be prosecuted. See 18 U.S.C.

§ 2258B(a). But this insulates ISPs only when they do what any private citizen

who discovers apparent child pornography might without inviting a real risk of

criminal prosecution: pass evidence along to law enforcement and comply with

its preservation instructions. All quite unlike NCMEC, which (again alone)

enjoys the right to receive child pornography knowingly and review it

intentionally.

      Recent Supreme Court decisions fortify our conviction that NCMEC

qualifies as a governmental entity. In a pair of cases the Court held that Amtrak

— a publicly owned corporation — is a governmental entity. Lebron v. Nat’l R.R.

Passenger Corp., 513 U.S. 374, 399 (1995); Dep’t of Transp. v. Ass’n of Am.

R.Rs. (DOT), 135 S. Ct. 1225, 1233 (2015). The Court began by recalling that the

                                       -9-
government cannot “evade the most solemn obligations imposed in the

Constitution by simply resorting to the corporate form.” Lebron, 513 U.S. at 397.

Then the Court proceeded to examine the level of governmental control over

Amtrak, the broad statutory mandates to which it was subject, its dependence on

federal funding, the purpose behind its creation, and the benefits it conferred on

the government. See id. at 397-400; see also DOT, 135 S. Ct. at 1231-33. In the

end, the Court held that the “combination” of these considerations conspired to

suggest that Amtrak was indeed a governmental entity. Id. at 1232-33.

      Looking to similar considerations here leads us to a similar conclusion.

Much as Amtrak was created by statute to assume functions previously carried out

by private railroads, Congress passed statutes to fund and mandate various of

NCMEC’s functions soon after private parties incorporated it. 2 Today, NCMEC

is statutorily required to perform over a dozen separate functions, a fact that

evinces the sort of “day-to-day” statutory control over its operations that the

Court found tellingly present in the Amtrak cases. 3 Law enforcement agents

      2
        See, e.g., Missing Children’s Assistance Act, Pub. L. No. 98-473, 98 Stat.
1837, 2125-27 (1984) (codified as amended at 42 U.S.C. § 5771); Pub. L. No.
106-113 app. A, 113 Stat. 1501, 1501A-23 (1999); PROTECT Act, Pub. L. No.
108-21, 117 Stat. 650, 665 (2003) (codified as amended at 42 U.S.C. § 5773);
PROTECT Our Children Act of 2008, Pub. L. No. 110-401, 122 Stat. 4229, 4243-
48 (codified as amended at 18 U.S.C. § 2258A). See generally Our History,
NCMEC, http://www.missingkids.com/history (last visited July 7, 2016).
      3
         Compare 42 U.S.C. § 5773(b) (requiring NCMEC to, among other things,
operate a “national 24-hour toll-free telephone line,” “cyber tipline,” and “child
victim identification program,” provide “training” and “technical assistance” to

                                        - 10 -
participate at varying levels in its daily operations, 4 and government officials

enjoy a sizeable presence on its board. 5 As much as 75 percent of its budget

(excluding in-kind donations) comes from the federal government. NCMEC


law enforcement agencies, and develop and disseminate “information” to a variety
of governmental and non-governmental entities), with DOT, 135 S. Ct. at 1232
(observing that “Congress has mandated certain aspects of Amtrak’s day-to-day
operations,” including “maintain[ing] a route between Louisiana and Florida,”
applying certain considerations when “making improvements to the Northeast
corridor,” and abiding by certain raw material source requirements when making
purchases of “more than $1 million”).
      4
          Representatives of multiple law enforcement agencies have offices in the
NCMEC building, including the FBI, Department of Homeland Security, U.S.
Marshals, U.S. Postal Inspection Service, and Department of Defense. R. vol. 3
at 246-47; United States v. Keith, 980 F. Supp. 2d 33, 41 (D. Mass. 2013) (“[The]
U.S. Marshals and other law enforcement personnel provide on-site support and
referral assistance for NCMEC’s Exploited Child Division.”). The FBI’s on-site
presence includes both a “supervisory special agent” assigned “full-time” to
NCMEC to “coordinate the use of both FBI and NCMEC resources and facilitate
the most effective response to . . . child pornography, and other cases” and an
“embedded intelligence analyst” who “addresses cyber tips” and “supports” the
Child Victim Identification Program. U.S. Dep’t of Justice, Office of Juvenile
Justice & Delinquency Prevention, Federal Resources on Missing and Exploited
Children 21-24 (6th ed. 2011). The Secret Service, too, provides forensic
services to NCMEC in the form of “polygraph examinations, handwriting and
fingerprint analysis, voiceprint comparisons, audio and video enhancements,
computer and other electronic media examinations, forensic photography, graphic
arts, research and identification, and the Operation Safe Kid Program.” Id. at 17;
see also 18 U.S.C. § 3056(f).
      5
        Almost a quarter of NCMEC’s board members represent government
agencies or law enforcement, including the FBI, U.S. Secret Service, U.S.
Marshals, Bureau of Alcohol, Tobacco, Firearms and Explosives, Immigration and
Customs Enforcement, Naval Criminal Investigative Service, U.S. Postal
Inspection Service, U.S. Nuclear Regulatory Commission, National Sheriffs’
Association, Fraternal Order of Police, and National Association of Attorneys
General. See Board of Directors, NCMEC,
http://www.missingkids.com/boardofdirectors (last visited July 7, 2016).

                                        - 11 -
Amicus Br. at 9. Neither is there any question about the public benefit NCMEC

confers, for by all accounts its important work is essential to the identification

and prevention of child sexual exploitation crimes. Congress and NCMEC alike

have expressly said as much. See, e.g., 42 U.S.C. § 5771; National Center for

Missing & Exploited Children: Our Work, NCMEC, http://www.missingkids.

com/NCMEC (last visited July 7, 2016). Given all this and as a matter of

analogistic reasoning, it’s difficult to see how a quasi-public corporation like

Amtrak (a mere utility, really) might qualify as a governmental entity while

NCMEC, an entity afforded so many unique law enforcement powers, might not.

      In the face of so much law and evidence suggesting NCMEC qualifies as a

governmental entity, the government offers almost no reply. In fact, its only

response is to question whether the question is properly before us. According to

the government, when Mr. Ackerman was before the district court he argued

merely that NCMEC is a governmental agent and failed to argue that NCMEC is

also a governmental entity. As a result, the government suggests, any “entity

argument” is waived. Of course, Mr. Ackerman avidly disputes the government’s

assessment and submits that he pursued both an agent and an entity theory before

the district court. But who is right about this much doesn’t much matter. It

doesn’t because the Supreme Court has specifically held that a defendant who

asserts an agency theory before the district court preserves an entity theory on

appeal. See Lebron, 513 U.S. at 378-79. And to this controlling direction the


                                         - 12 -
government provides no answer. So it is that the government’s only response

turns out to be no real response at all.

      Seeing the void left by the government, NCMEC offers a number of

substantive responses to Mr. Ackerman’s entity theory in its own amicus brief.

But ours is a party-directed adversarial system and we normally limit ourselves to

the arguments the parties before us choose to present. Amici briefs often serve

valuable functions, but those functions don’t include presenting arguments

forgone by the parties themselves or effectively and unilaterally expanding the

word limits established by rule for a favored party. Indeed, for just these reasons

(and more) this court has routinely declined to consider arguments presented only

in an amicus brief — and no one even attempts to offer us a reason to depart from

that practice here. See, e.g., Fed. R. App. P. 28; In re McGough, 737 F.3d 1268,

1277 n.8 (10th Cir. 2013); Tyler v. City of Manhattan, 118 F.3d 1400, 1403-04

(10th Cir. 1997).

      Alternatively and anyway, the various arguments NCMEC offers do not

change the equation materially. In an effort to distinguish Lebron from its own

case, NCMEC argues that, unlike Amtrak, it and its CyberTipline existed for a

(brief) period of time before Congress passed statutes funding and mandating its

functions. But factually the distinction seems pretty unpersuasive, for many of

the assets of what later became Amtrak existed in private hands long before

Amtrak’s statutory authorization. And analytically we are uncertain why it


                                           - 13 -
matters whether NCMEC was once private. For no one, NCMEC included, gives

us reason to doubt that even an admittedly private entity can be made into a

public one later by sufficient statutory action (consider the Tennessee Valley

Authority).

      In an effort to establish that even today it is not a public entity, NCMEC

stresses that it receives some (unspecified amount of) in-kind donations from

private parties every year and engages in partnerships with private firms

interested in reducing child exploitation. But it remains undisputed that NCMEC

receives the bulk of its funding from the federal government and we are aware of

no authority suggesting that the existence of some (unspecified) amount of in-

kind private donations converts a public entity into a private one. Surely the local

public library would disagree — and so might Amtrak for it, too, receives plenty

of private funding (not merely in-kind donations) from paying customers. See 49

U.S.C. § 24301(a)(2) (“Amtrak . . . shall be operated and managed as a for-profit

corporation . . . .”). Neither is it unknown for public entities to partner with

private ones. See Partnerships and Outreach, FBI, https://www.fbi.gov/about-

us/partnerships_and_outreach (last visited July 7, 2016) (“To do its job, the FBI

works with both government and private sector partners every day . . . .”).

      Next, NCMEC suggests it isn’t required to spend its federal funding in any

particular way. It may pursue the various law enforcement functions Congress

has identified, but it doesn’t have to do so. Here again we cannot agree. The law


                                        - 14 -
expressly states that NCMEC’s federal funding “shall be used” for over a dozen

specifically enumerated functions. 42 U.S.C. § 5773(b). And while “shall” can

sometimes mean “may,” that’s the exception and not the rule, for the word is

generally considered “imperative or mandatory” in character. Black’s Law

Dictionary 1375 (6th ed. 1990). Neither do we see the case for an exception here.

Congress itself has described NCMEC’s functions as “duties and responsibilities

under Federal law.” 42 U.S.C. § 16961(a)(1). Neither does anyone dispute that

the use of “shall” in the first clause of § 5773(b) — providing that “[t]he

Administrator shall annually make a grant” to NCMEC — is mandatory in

character, and it seems most unlikely that the same word might bear a different

meaning in the second clause where NCMEC’s duties are described. After all, we

usually presume Congress means the same thing when it uses the same word more

than once in the same sentence. See Brown v. Gardner, 513 U.S. 115, 118 (1994).

Congress, too, appears to be well aware of the difference between “may” and

“shall” in the funding context, for in other similar grant-making statutes it has

indeed adopted the more permissive “may.” See, e.g., 42 U.S.C. § 16985(b)(2)

(“The Administrator shall annually make a grant to RAINN, which shall be used

for the performance of the organization’s national programs, which may include

. . . .” (emphasis added)). And in other contexts, too, even NCMEC itself has

seemed to characterize its work as mandatory. See, e.g., Michelle K. Collins,

Child Pornography: A Closer Look, The Police Chief, Mar. 2007, available at


                                        - 15 -
http://goo.gl/LohIYz (the director of NCMEC’s Exploited Child Division

discussing “NCMEC’s congressionally mandated CyberTipline”).

      Finally, NCMEC suggests that the statutes governing its operations are

“like” routine federal grant-making or state licensing statutes. But we just don’t

see how. Federal grantees and state licensees don’t typically enjoy (for example)

the statutory authority to receive contraband knowingly, backed by statutes

compelling private and public entities to cooperate with them. Neither do they

typically enjoy such powers in aid of traditionally public law enforcement

functions. Certainly at no point in these proceedings has NCMEC or the

government sought to identify a single federal grantee or state licensee with

anything fairly analogous to the sorts of statutory law enforcement powers and

duties NCMEC possesses.

                                         II

      Even if we are wrong and NCMEC isn’t a governmental entity, that doesn’t

necessarily mean its searches escape the Fourth Amendment’s ambit. After all,

since time out of mind the law has prevented agents from exercising powers their

principals do not possess and so cannot delegate. 1 William Blackstone,

Commentaries *417-20; Restatement (Second) of Agency § 17 (1958). That is a

rule of law the founders knew, understood, and undoubtedly relied upon when

they drafted the Fourth Amendment — for what would have been the point of the

Amendment if the government could have instantly rendered it a dead letter by


                                       - 16 -
the simple expedient of delegating to agents investigative work it was forbidden

from undertaking itself? Indeed, it’s long since accepted that the Amendment’s

proscriptions apply not just to governmental entities but also to those who serve

as the government’s agents in particular cases. See Skinner v. Ry. Labor Execs.’

Ass’n, 489 U.S. 602, 614 (1989) (“Although the Fourth Amendment does not

apply to a search or seizure, even an arbitrary one, effected by a private party on

his own initiative, the Amendment protects against such intrusions if the private

party acted as an instrument or agent of the Government.”).

      How can we tell if NCMEC acted as the government’s agent in this case?

An agency relationship is usually said to “result[] from the manifestation of

consent by one person to another that the other shall act on his behalf and subject

to his control, and consent by the other so to act.” Restatement (Second) of

Agency § 1. This manifestation and consent doesn’t have to be formalized in any

particular way. See id. §§ 15-16. Instead, the “authority to do an act can be

created by written or spoken words or other conduct of the principal which,

reasonably interpreted, causes the agent to believe that the principal desires him

so to act on the principal’s account.” Id. § 26. As well, a principal may delegate

general authority to his or her agent to act in the ordinary course, without

constant supervision or awareness of every discrete act. See id. § 7 cmt. c.

Neither has the common law traditionally required that the agent be an altruist,

acting without any intent of advancing some personal interest along the way (like


                                       - 17 -
monetary gain). As clients know well, lawyers can serve as their agents all while

zealously charging by the hour. Instead, the question is usually simply whether

the agent acts with the principal’s consent and (in some way) to further the

principal’s purpose. See generally id. §§ 387-93. All these traditional agency

principles were reasonably well ensconced in the law at the time of the founding

and would seem the natural place to start in understanding the Amendment’s

original meaning and application to governmental agents. See generally Joseph

Story, Commentaries on the Law of Agency (6th ed., Little, Brown & Co. 1863)

(1839); United States v. Ellyson, 326 F.3d 522, 527 (4th Cir. 2003) (noting that

the governmental agent inquiry should be “guided by common law agency

principles”).

      Admittedly, in recent years some courts have offered more stylized agency

tests for Fourth Amendment cases, which at first glance may appear to depart

from and demand more than the common law did to establish an agency

relationship. So, for example, some treat the Fourth Amendment agency inquiry

as a three-factor test. See, e.g., United States v. Silva, 554 F.3d 13, 18 (1st Cir.

2009) (analyzing “[1] the extent of the government’s role in instigating or

participating in the search, [2] its intent and the degree of control it exercises over

the search and the private party, and [3] the extent to which the private party aims

primarily to help the government or to serve its own interests”). Our court seems

to have adopted a two-part variation in United States v. Souza, 223 F.3d 1197


                                         - 18 -
(10th Cir. 2000). Id. at 1201 (asking “1) whether the government knew of and

acquiesced in the intrusive conduct, and 2) whether the party performing the

search intended to assist law enforcement efforts or to further his own ends”).

Still others appear to collapse these same factors into “[o]ne highly pertinent

consideration.” Ellyson, 326 F.3d at 527.

      But in this particular case it doesn’t much matter which agency test you

might wish to employ. Even under this court’s decision in Souza or similar

decisions adopted in other circuits it’s hard to see how we could avoid deeming

NCMEC the government’s agent in this case. Souza suggests that we should first

ask whether the government “knew of and acquiesced in” NCMEC’s putative

search. Here we know Congress statutorily required AOL to forward Mr.

Ackerman’s email to NCMEC; Congress statutorily required NCMEC to maintain

the CyberTipline to receive emails like Mr. Ackerman’s; Congress statutorily

permitted NCMEC to review Mr. Ackerman’s email and attachments; and

Congress statutorily required NCMEC to pass along a report about Mr.

Ackerman’s activities to law enforcement authorities. All at the government’s

expense and backed by threat of sanction should AOL have failed to cooperate.

All with special dispensation, too, to NCMEC to possess and review contraband

knowingly and intentionally. This comprehensive statutory structure seems more

than enough to suggest both congressional knowledge of and acquiescence in the

possibility that NCMEC would do exactly as it did here.


                                        - 19 -
      Of course and as the government notes, Congress’s statutes don’t require

NCMEC to open and view email and attachments like Mr. Ackerman’s. But

everyone accepts that Congress has authorized and funded NCMEC to do just

that. And everyone accepts that Congress enabled NCMEC to review Mr.

Ackerman’s email by excepting the Center from the myriad laws banning the

knowing receipt, possession, and viewing of child pornography. Nothing about

NCMEC’s actions could possibly have come as a surprise. Neither does anything

in Souza (or any other authority cited to us) suggest that the principal must

mandate rather than merely consent to the agent’s challenged conduct.

      When it comes to Souza’s second factor, too, we harbor no doubt. Surely,

after all, NCMEC did as it did in this case with some “inten[tion] to assist” law

enforcement. As we’ve seen, Congress authorizes and funds NCMEC to perform

the functions it performed here because (and expressly premised on the finding

that) they are designed (intended) to help law enforcement. See, e.g., 42 U.S.C.

§ 5771. And of course NCMEC itself has acknowledged that it undertakes the

sort of conduct challenged here precisely because (at least in part) it intends to

aid law enforcement. About Us, NCMEC, http://www.missingkids.com/About

(last visited July 7, 2016) (explaining that NCMEC “provid[es] assistance to law

enforcement and families to find missing children, reduce child sexual

exploitation and prevent child victimization”).




                                        - 20 -
      Bolstering our confidence about all this is the Supreme Court’s leading

Fourth Amendment agency case, Skinner v. Railway Labor Executives’ Ass’n, 489

U.S. 602 (1989). There the Federal Railroad Administration promulgated

regulations requiring private railroads to test certain of their employees for illicit

drugs and authorizing (but not requiring) railroads to test certain other of their

employees. Id. at 609-12. The government acknowledged that the mandatory

testing requirements converted otherwise private railroads into governmental

agents for purposes of the Fourth Amendment, but it suggested that the

permissive testing requirements did not. The Supreme Court disagreed. Rather

than endorsing a rigid multi-part agency test of the sort some lower courts had by

that time devised, the Court seemed to follow the common law by asking simply

whether “the Government’s encouragement, endorsement, and participation” in

the permissive testing was enough to render otherwise private railroads agents of

the government for Fourth Amendment purposes. Id. at 615-16. And applying

that test here there can be little doubt of the result it yields. For the government

surely “encouraged and endorsed and participated” in NCMEC’s putative search

for the same reasons it “knew of and acquiesced in” that activity: Congress

funded the Center, required AOL to cooperate with it, allowed it to review Mr.

Ackerman’s email by excepting it from various federal criminal laws, and

statutorily mandated or authorized every bit of its challenged conduct.




                                         - 21 -
      Even if all that is true, and a finding of agency would be consistent with the

common law at the time of the founding, the test this court articulated in Souza,

and the test the Supreme Court applied in Skinner, the government suggests that

our prior decision in United States v. Poe, 556 F.3d 1113 (10th Cir. 2009), still

precludes us from holding that NCMEC acted as its agent in this case. In Poe,

this court faced the question whether bounty hunters who searched a home

qualified as governmental agents by virtue of the fact that the state of Oklahoma

regulated the bail bonds industry. Poe held not. Both because the mere licensing

and regulation of an industry wasn’t enough to suggest that the government knew

of or acquiesced in the particular search in question. And because the bounty

hunters’ purpose or intention in searching the house was to find a bail-jumping

suspect and so receive a reward from the bail bondsman that employed them.

Given that, Poe thought it fair to conclude that the bounty hunters intended to

help themselves or their employer (their true principal) but “did not intend to

assist law enforcement” at all. Id. at 1124.

      Neither of the grounds on which Poe rested are present here. As we’ve

already acknowledged, a governmental licensing and regulation regime does not

always suffice to render the licensed or regulated party a governmental entity or

agent. After all private lawyers, doctors, and accountants are all licensed and

regulated by the state, yet they don’t (usually) qualify as governmental entities or

agents. But as we’ve already observed, too, in this case we don’t face a general


                                        - 22 -
licensing or regulatory regime open to all qualified applicants but a statutory

grant of special law enforcement authority to a single entity and no other,

authorizing and encouraging it to perform functions no other private person or

entity may lawfully undertake. And as we’ve seen, helping law enforcement is at

least part of NCMEC’s intentions when it reviews emails pursuant to its statutory

tipline authority.

      Admittedly, the government reads Poe differently than we do. It reads the

decision as suggesting that a private party who bears any private purpose cannot

serve as a governmental agent. But this reading is a misreading. After all, and as

we’ve seen, the common law recognized that agents routinely intend to serve their

principals with the further intention to make money for themselves. In Skinner,

too, the fact that the private railroads had private (economic) reasons for seeking

to curb drug abuse by railroad employees — and had sought to do so before the

government promulgated its regulations, 489 U.S. at 606-07 — was no barrier to

the Court’s determination that the statutory scheme converted the railroads into

governmental agents. And in United States v. Leffall, 82 F.3d 343 (10th Cir.

1996), this court likewise expressly explained that the agency question cannot be

resolved “simply” by “evaluat[ing] the private person’s state of mind — whether

his motive to aid law enforcement preponderates.” Id. at 347. Neither do we read

Poe as disagreeing with any of this standard stuff but as suggesting instead and

much more modestly that a question about a claim of agency may arise when a


                                        - 23 -
private party bears no intention to assist the government. Or put another way,

when the agent serves a different principal and not the government. Nothing like

that complication is present here.

      One final wrinkle remains to unfold on the agency question. The

government insists that whether NCMEC is a governmental agent is a question of

fact, permitting this court to reverse the district court’s determination only if it

clearly erred. For our part, we readily agree that this court is obligated to give

great deference to the district court’s findings of historic fact — something we

have done in our analysis above and find little difficulty doing, for the historic

facts are (materially) undisputed in this case. But having said that much, we

cannot agree with the government if it means to suggest that the deference we

owe to the district court’s factual findings extends to its definition of the “legal

concept” of agency, Restatement (Second) of Agency § 1 cmt. b, or to the

question whether the facts the district court found are sufficient to satisfy it. It is

for this court to decide (de novo) what the law is and whether the facts (as found

by the district court and so long as they are not clearly erroneous) satisfy its

demands. See Ornelas v. United States, 517 U.S. 690, 694-99 (1996) (holding

that appellate courts must review a district court’s determination of reasonable

suspicion and probable cause de novo, with deference to its findings of historic

fact); United States v. Ginglen, 467 F.3d 1071, 1074 (7th Cir. 2006)

(acknowledging Ornelas’s relevance to review of a governmental agency


                                         - 24 -
determination). Nothing in the case the government purports to rely upon

abandons these stolid principles of appellate review found most everywhere in the

law. To the contrary, it explains quite rightly that “[w]e review the district

court’s findings of fact” relevant to an agency determination “under a clearly

erroneous standard,” but “review de novo the ultimate question of constitutional

law,” Leffall, 82 F.3d at 347 — and the Fourth Amendment agency question is

unquestionably one of constitutional law.

                                          III

      Assuming NCMEC is a governmental entity or agent, its actions still

implicate the Fourth Amendment only if a “search” took place here. On first

blush, the answer to that question might seem obvious. No one in this appeal

disputes that an email is a “paper” or “effect” for Fourth Amendment purposes, a

form of communication capable of storing all sorts of private and personal details,

from correspondence to images, video or audio files, and so much more. See

United States v. Cotterman, 709 F.3d 952, 964 (9th Cir. 2013) (en banc); cf.

United States v. Lichtenberger, 786 F.3d 478, 489 (6th Cir. 2015). The

undisputed facts show, too, that NCMEC opened Mr. Ackerman’s email, found

four attachments, and proceeded to view each of them. 6 And that sort of

      6
        The record shows that what NCMEC received from AOL was an email —
technically, a .eml file — which contained the four attachments. See R. vol. 3 at
15-16 (law enforcement describing the “.eml file” as the “actual file that AOL
sends through [NCMEC’s] Tipline,” which, when opened, “show[s] . . . the e-
mail” with “four attachments” inside); id. at 221-22 (NCMEC’s Executive

                                        - 25 -
rummaging through private papers or effects would seem pretty obviously a

“search.” After all, if opening and reviewing “physical” mail is generally a

“search” — and it is, Ex Parte Jackson, 96 U.S. 727, 733 (1877); United States v.

Van Leeuwen, 397 U.S. 249, 251 (1970) — why not “virtual” mail too?

      Admittedly, it’s an open question whether the Supreme Court’s so-called

“third-party doctrine” might undermine any claim to Fourth Amendment

protections when someone (like Mr. Ackerman) engages a private agent (like

AOL) to deliver his correspondence. The Court has, after all, suggested that

individuals lack any reasonable expectation of privacy and so forfeit any Fourth

Amendment protections in materials they choose to share with third parties like

banks or telephone companies. See, e.g., United States v. Miller, 425 U.S. 435,

440-43 (1976); Smith v. Maryland, 442 U.S. 735, 742-46 (1979). And lower

courts have only begun to consider whether (and to what extent) the doctrine

should be extended to email where (as here) a subscriber relies on a commercial

ISP to store and deliver it. Compare United States v. Forrester, 512 F.3d 500,

510-11 (9th Cir. 2007) (finding no Fourth Amendment protection for the “to/from

addresses of e-mail messages”), with United States v. Warshak, 631 F.3d 266,

283-88 (6th Cir. 2010) (finding Fourth Amendment protection for email contents).

But the district court didn’t rely upon third-party doctrine in ruling against Mr.


Director of the Exploited Child Division explaining that “[i]n this case there is
one uploaded file,” a “.eml file,” which NCMEC did not “alter, manipulate, [or]
change,” with “four images located within [the] uploaded file”).

                                        - 26 -
Ackerman. Exactly to the contrary, throughout its decision the court assumed that

Mr. Ackerman had a reasonable expectation of privacy in his email. And though

we may of course affirm the district court’s judgment on any basis the record

supports, we think making the attempt here imprudent given that the district court

has yet to make any factual findings relevant to Mr. Ackerman’s subjective

expectations of privacy or the objective reasonableness of those expectations in

light of the parties’ dealings (e.g., the extent to which AOL regularly accessed

emails and the extent to which users were aware of or acquiesced in such access).

Facts that could well impact the legal analysis. See, e.g., Harper v. P. Urbana,

P.A., 342 F. App’x 380, 382 (10th Cir. 2009).

                                          A

      Even so, the government says there’s another Fourth Amendment doctrine

that compels a ruling in its favor, one the district court did cite and rely upon, this

one called the “private search” doctrine and often associated with United States v.

Jacobsen, 466 U.S. 109 (1984). In that case, FedEx employees opened a damaged

package, found suspicious plastic bags of white powder inside, and passed the

parcel to the government, along with a description of what they’d found. Id. at

111. A DEA agent then repeated the same investigation, opening the package and

examining its contents. Id. Finally, he subjected the white powder to a chemical

drug test to confirm it was cocaine. Id. at 111-12. Considering all this, the

Supreme Court held that no “search” implicating the Fourth Amendment had


                                        - 27 -
taken place because there was a “virtual certainty” that (but for one thing) the

government could have discovered “nothing else of significance” in the package

nor learned anything beyond what it had “already . . . been told” by a private

party. Id. at 119.

      The one thing, of course, was the drug test. FedEx didn’t test the chemical

composition of the white powder and the government did. And so you might well

ask, why isn’t at least that a search implicating the Fourth Amendment? The

Court acknowledged that the drug test promised to (and surely did) reveal

information previously unknown to FedEx. Yet the Court proceeded to hold that

the drug test still didn’t qualify as a Fourth Amendment search because it “merely

disclose[d]” whether the powder was contraband “and no other arguably ‘private’

fact.” Id. at 123. In these circumstances, the Court announced, the government’s

apparent search was no search at all because it compromised no “legitimate

privacy interest” within the meaning of Katz v. United States, 389 U.S. 347

(1967). Jacobsen, 466 U.S. at 123.

      Accepting our obligation as a lower court to apply both aspects of

Jacobsen’s private search doctrine faithfully, we fail all the same to see how they

might help the government in this case. Yes, AOL ran a search that suggested a

hash value match between one attachment to Mr. Ackerman’s email and an image

AOL employees had previously identified as child pornography. But AOL never

opened the email itself. Only NCMEC did that, and in at least this way exceeded


                                        - 28 -
rather than repeated AOL’s private search. Neither is there any doubt NCMEC’s

search of the email itself quite easily “could [have] disclose[d]” information

previously unknown to the government besides whether the one attachment

contained contraband. Id. at 122. Indeed, when NCMEC opened Mr. Ackerman’s

email it could have learned any number of private and protected facts, for (again)

no one before us disputes that an email is a virtual container, capable of storing

all sorts of private and personal details, from correspondence to other private (and

perfectly legal) images, video or audio files, and beyond. See, e.g., Warshak, 631

F.3d at 284. And we know, too, that this particular container did contain three

additional attachments, the content of which AOL and NCMEC knew nothing

about before NCMEC opened them too. As far as anyone knew at the time, they

could have revealed virtually any kind of noncontraband information to the prying

eye.

       Our view about the inapplicability of Jacobsen’s private search doctrine

finds support in at least two related cases. In United States v. Place, 462 U.S.

696 (1983), the Court held that a dog sniff of luggage by a “well-trained narcotics

detection dog” didn’t offend the Fourth Amendment because it didn’t “require

opening the luggage” and could have suggested only the presence or absence of

“contraband items.” Id. at 707 (quoted in Jacobsen, 466 U.S. at 124).

Meanwhile, in Walter v. United States, 447 U.S. 649 (1980), the Court held law

enforcement’s projection and viewing of films did implicate the Constitution


                                        - 29 -
because the prior private search was much narrower, involving only the visual

inspection of the labels on the outside of the film boxes. See id. at 656-60

(opinion of Stevens, J.). As interpreted by the Court in Jacobsen, the analytical

thread stitching together these results and its own is the question whether “the

governmental conduct could [have] reveal[ed] nothing about noncontraband

items.” 466 U.S. at 124 n.24. In Place and Jacobsen, the government’s conduct

could have revealed nothing about noncontraband items, so no “search” took

place within the meaning of the Fourth Amendment. In Walter, by contrast, the

government’s conduct could have revealed something previously unknown about

noncontraband items, so a constitutionally triggering “search” did take place.

And by the same reasoning the same result should follow here.

      At this point you might wonder about a similar but different scenario than

the one we confront today. What if NCMEC hadn’t opened Mr. Ackerman’s

email but had somehow directly accessed (only) the (one) attached image with the

matching hash value? Could the government have argued that, in that case,

NCMEC’s actions didn’t risk exposing any private information beyond what AOL

had already reported to it? Or might even that have risked exposing new and

protected information, maybe because the hash value match could have proven

mistaken (unlikely if not impossible) or because the AOL employee who

identified the original image as child pornography was mistaken in his assessment

(unlikely if maybe more possible)? See Salgado, supra, at 45-46. Interesting


                                        - 30 -
questions, to be sure, but ones we don’t have to resolve in this case. We don’t

because the undisputed facts before us indicate that NCMEC opened Mr.

Ackerman’s email first and did so before and in order to view not just the

attachment that was the target of AOL’s private search but three others as well.

And as we’ve seen, each of these steps — opening the email and viewing the

three other attachments — was enough to risk exposing private, noncontraband

information that AOL had not previously examined.

                                         B

      Our conclusion about this is confirmed by yet another and distinct line of

authority. Jacobsen said no “search” implicating the Fourth Amendment took

place even when officers exceeded the scope of the search previously performed

by the private party and removed and destroyed a small amount of powder to

conduct a drug test. In doing so, Jacobsen invoked Katz and held there was no

“reasonable expectation of privacy” in concealing whether something is or isn’t

contraband. See 466 U.S. at 122-23. But after United States v. Jones, 132 S. Ct.

945 (2012), there’s reason to wonder about that conclusion. After all, Jones held

that the Katz formula is but one way to determine if a constitutionally qualifying

“search” has taken place. Id. at 949-51. In light of the Fourth Amendment’s

original meaning, Jones explained that government conduct can constitute a

Fourth Amendment search either when it infringes on a reasonable expectation of

privacy or when it involves a physical intrusion (a trespass) on a constitutionally


                                       - 31 -
protected space or thing (“persons, houses, papers, and effects”) for the purpose

of obtaining information. So the fact the government’s conduct doesn’t trigger

Katz doesn’t mean it doesn’t trigger the Fourth Amendment. Id. at 950 (“Fourth

Amendment rights do not rise or fall with the Katz formulation. . . . [F]or most of

our history the Fourth Amendment was understood to embody a particular

concern for government trespass upon the areas . . . it enumerates. Katz did not

repudiate that understanding.”).

      Reexamining the facts of Jacobsen in light of Jones, it seems at least

possible the Court today would find that a “search” did take place there. After

all, the DEA agent who performed the drug test in Jacobsen took and destroyed a

“trace amount” of private property, 466 U.S. at 125, a seeming trespass to

chattels. Neither is there any question that the purpose and effect of the agent’s

action was to obtain information. See id. at 122-23. And while the destruction of

only a “trace amount” of private property might not amount to a trespass under

modern tort law, even less was required to establish a claim of trespass to chattels

at the time of the founding — and we know the Fourth Amendment is no less

protective of persons and property against governmental invasions than the

common law was at the time of the founding. Jones, 132 S. Ct. at 950, 953; id. at

957 n.2 (Alito, J., concurring in the judgment) (“At common law, a suit for

trespass to chattels could be maintained if there was a violation of ‘the dignitary

interest in the inviolability of chattels,’ but today there must be ‘some actual


                                        - 32 -
damage to the chattel before the action can be maintained.’” (quoting W. Keeton

et al., Prosser & Keeton on Law of Torts § 14, at 87 (5th ed. 1984))).

      Given the uncertain status of Jacobsen after Jones, we cannot see how we

might ignore Jones’s potential impact on our case. And its impact here seems

even clearer than in Jacobsen. After all, we are not dealing with a governmental

drug test that destroyed but a trace amount of potential contraband. We are

dealing instead with the warrantless opening and examination of (presumptively)

private correspondence that could have contained much besides potential

contraband for all anyone knew. And that seems pretty clearly to qualify as

exactly the type of trespass to chattels that the framers sought to prevent when

they adopted the Fourth Amendment. See, e.g., 1 Thomas M. Cooley, The

General Principles of Constitutional Law in the United States of America 212 &

n.2 (1880); Thomas M. Cooley, A Treatise on the Constitutional Limitations

Which Rest upon the Legislative Power of the States of the American Union 306

n.2 (1868); Ex parte Jackson, 96 U.S. at 733. Of course, the framers were

concerned with the protection of physical rather than virtual correspondence. But

a more obvious analogy from principle to new technology is hard to imagine and,

indeed, many courts have already applied the common law’s ancient trespass to

chattels doctrine to electronic, not just written, communications. See, e.g., eBay,

Inc. v. Bidder’s Edge, Inc., 100 F. Supp. 2d 1058, 1063, 1069-70 (N.D. Cal.

2000); CompuServe Inc. v. Cyber Promotions, Inc., 962 F. Supp. 1015, 1019,


                                        - 33 -
1027 (S.D. Ohio 1997); Thrifty-Tel, Inc. v. Bezenek, 46 Cal. App. 4th 1559, 1565-

67 (1996). So it seems that, whether we analyze the “search” question through

the lens of the government’s preferred authority — Jacobsen and Katz — or

through the lens of the traditional trespass test suggested by Jones, they yield the

same (and pretty intuitive) result: NCMEC conducted a “search” when it opened

and examined Mr. Ackerman’s email.

                                         IV

      Having determined that NCMEC is a governmental entity or agent and that

it searched Mr. Ackerman’s email without a warrant, at this point you might

wonder whether the government could argue that NCMEC’s search still qualifies

as a “reasonable” one because of, say, exigent circumstances or the “special

needs” doctrine. Or whether any Fourth Amendment violation in opening the

email or the three other attachments was too attenuated from the discovery of

incriminating evidence in the matching hash value attachment to justify exclusion

as the appropriate remedy. Or whether suppression might also be an

inappropriate remedy because NCMEC acted in “good faith.” But the government

argues none of these points in this appeal, seeming instead to accept that if

NCMEC was a governmental entity or agent and if its opening of the email was

an unwarranted search, then its subsequent discovery of four attached images of

child pornography was “fruit of a poisonous tree” and should be suppressed.

Indeed, the closest the government comes to briefing any of these questions is to


                                        - 34 -
tell us it incorporates by reference the good faith arguments it presented to the

district court. Even though this court has repeatedly instructed (both in rule and

case law) that this sort of mechanical “[i]ncorporating by reference portions of

lower court or agency briefs or pleadings” is insufficient to preserve a point for

appellate review. 10th Cir. R. 28.4; see also Gaines-Tabb v. ICI Explosives, USA,

Inc., 160 F.3d 613, 623-24 (10th Cir. 1998).

      So with that, our encounter with this case comes to an end — at least for

now. Surely hard questions remain to be resolved on remand, not least the

question whether the third-party doctrine might preclude Mr. Ackerman’s claim to

the Fourth Amendment’s application, a question the government has preserved

and the district court and we have reserved. But about one thing we can be very

certain. There can be no doubt that NCMEC does important work and that its

work can continue without interruption. After all, it could be that the third-party

doctrine will preclude motions to suppress like Mr. Ackerman’s. Or that changes

in how reports are submitted or reviewed might allow NCMEC to access

attachments with matching hash values directly, without reviewing email

correspondence or other attachments with possibly private, noncontraband content

— and in this way perhaps bring the government closer to a successful invocation

of the private search doctrine. Or it may be possible that the government could

cite exigent circumstances or attenuation doctrine or special needs doctrine or the

good faith exception to excuse warrantless searches or avoid suppression in at


                                        - 35 -
least some cases. But even if not a single one of these potential scenarios plays

out — and we do not mean to prejudge any of them — we are confident that

NCMEC’s law enforcement partners will struggle not at all to obtain warrants to

open emails when the facts in hand suggest, as they surely did here, that a crime

against a child has taken place.

      The district court’s denial of the motion to suppress is reversed. The case

is remanded for further proceedings consistent with this opinion.




                                       - 36 -

```

---
