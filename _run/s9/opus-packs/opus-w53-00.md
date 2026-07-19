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

## GROUP: content/cases/United States v. Gastiaburo.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Gastiaburo"
type: case
citation: "16 F.3d 582 (1994)"
parallel_cite: ""
neutral_cite: 1994 WL 32623
court: "U.S. Court of Appeals, Fourth Circuit"
court_level: coa
circuit: 4th
year: 1994
date_decided: 1994-02-08
docket: ""
authority_weight: "Binding in-circuit — 4th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 1994-02-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Gastiaburo
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/7027957/united-states-v-gastiaburo/"
  cluster_id: 7027957
  opinion_id: 6929715
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[California v. Acevedo]]", "[[Carroll v. United States]]", "[[United States v. Johns]]", "[[Chambers v. Maroney]]"]
aliases: ["United States v. Gastiaburo (4th Cir. 1994)"]
tags: ["case", "fourth-amendment", "automobile-exception", "impoundment", "delayed-search", "fourth-circuit"]
holding: "The automobile exception is not subject to a temporal limit; a 38-day gap between the car's seizure and the warrantless search did not…"
lake:
  record_id: United States v. Gastiaburo
  status: verified
  projected_at: 2026-07-09
---

# United States v. Gastiaburo

*16 F.3d 582 (4th Cir. 1994)* · U.S. Court of Appeals, Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gastiaburo's car was seized on October 8, 1991. Thirty-eight days later, on November 15, 1991, after his passenger Dina Viola told the police there was a hidden compartment behind the radio containing drugs, money, and a handgun, officer Cosslett went to the impound lot and searched that compartment without a warrant, recovering a gun and a 24-gram rock of crack cocaine. Gastiaburo moved to suppress, arguing the impoundment and the 38-day delay defeated the automobile exception.

## Issue
Whether the automobile exception justifies a warrantless search of a car that has already been seized and impounded, where 38 days elapsed between the seizure and the search.

## Rule
Yes. Probable cause supporting an automobile-exception search is not dissolved by impoundment or by the passage of time. The Fourth Circuit held the government's automobile-exception argument "is clearly correct." — 16 F.3d at 585. ^pin-585

Immobilization does not matter: "the justification to conduct a warrantless search under the automobile exception does not disappear merely because the car has been immobilized and impounded." — [*Id.* at 586](https://www.courtlistener.com/opinion/7027957/united-states-v-gastiaburo/#:~:text=the%20justification%20to%20conduct%20a). ^pin-586

Nor is there any temporal limit: "Not a single published federal case speaks of a 'temporal limit' to the automobile exception. The Supreme Court has repeatedly stated that a warrantless search of a car (1) need not occur contemporaneously with the car's lawful seizure and (2) need not be justified by the existence of exigent circumstances that might have made it impractical to secure a warrant prior to the search." — *Id.* at 587. ^pin-587

## Application
On these facts the November 15 search was valid. Viola's uncontroverted tip about the hidden compartment "would have more than sufficed to justify the issuance of a warrant," so it sufficed to justify a warrantless search of that same area, and the officer confined his search to it. Neither of Gastiaburo's objections defeated the exception: the car's impoundment did not convert it into a "fixed piece of property" (citing [[United States v. Johns]]), and the 38-day gap was not a *[[Common Legal Terms#per-se|per se]]* unreasonable delay — indeed the officer "conducted his search on the very same day that he first had probable cause to believe contraband could be found behind the dashboard," so the search "falls squarely within the specifically established and well-delineated 'automobile exception.'" — *Id.* at 587.

## Conclusion
The warrantless search of the impounded car was reasonable under the automobile exception; the denial of suppression was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 4th Cir.**
- No negative subsequent treatment identified. The decision applies [[California v. Acevedo]], [[Carroll v. United States]], [[Chambers v. Maroney]], and [[United States v. Johns]] to reject any "temporal limit" on a probable-cause vehicle search.

## Appears on
- [[Automobile Exception]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Gastiaburo*, 16 F.3d 582 (4th Cir. 1994) — https://www.courtlistener.com/opinion/7027957/united-states-v-gastiaburo/ — pinpoints: 585, 586, 587. (Lead opinion id 6929715; the cluster-URL integer 7027957 is, separately, an unrelated opinion id — see SR-5 note.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ec2f86eccb27c689", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "16 F.3d 582 (1994)", "court": "U.S. Court of Appeals, Fourth Circuit", "neutral_cite": "1994 WL 32623", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Gastiaburo", "year": "1994"}}
{"assertion_id": "630396bb8049d7fc", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Key — Progeny / Refinement", "title": "United States v. Gastiaburo"}}
{"assertion_id": "82f6cf94261084a5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The automobile exception is not subject to a temporal limit; a 38-day gap between the car's seizure and the warrantless search did not…", "title": "United States v. Gastiaburo"}}
{"assertion_id": "8f1ed10bdce5dba9", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 4th Cir.", "title": "United States v. Gastiaburo"}}
{"assertion_id": "da705204467e601a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1994-02-08", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Gastiaburo", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Gastiaburo", "varies_by_point": "false"}}
```

### lake record — United States v. Gastiaburo

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Gastiaburo",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Gastiaburo",
    "case_name_short": "Gastiaburo",
    "case_name_full": "United States v. Joseph GASTIABURO, a/k/a Joe Gastiaburo, a/k/a Joseph Gastiburo, a/k/a Joseph Menendez, a/k/a Joseph Gastibury, a/k/a Robert Julio Gastiaburo, a/k/a Joseph Mendez, a/k/a Joseph Rodriguez",
    "input_case_name": "United States v. Gastiaburo",
    "court": "U.S. Court of Appeals, Fourth Circuit",
    "court_id": "ca4",
    "court_level": "coa",
    "circuit": "4th",
    "state": null,
    "date_decided": "1994-02-08",
    "year": 1994,
    "docket": null,
    "cluster_id": 7027957,
    "lead_opinion_id": 6929715,
    "sibling_ids": [
      6929715
    ],
    "absolute_url": "/opinion/7027957/united-states-v-gastiaburo/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 663093,
        "score": 120,
        "case_name": "United States v. Gastiaburo"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "16 F.3d 582",
      "volume": "16",
      "reporter": "F.3d",
      "page": "582",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1994 WL 32623",
        "volume": "1994",
        "reporter": "WL",
        "page": "32623",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "16 F.3d 582",
        "volume": "16",
        "reporter": "F.3d",
        "page": "582",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1994 WL 32623",
        "volume": "1994",
        "reporter": "WL",
        "page": "32623",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "16 F.3d 582",
    "official_selection": {
      "court_class": "coa",
      "selected": "16 F.3d 582",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-585",
      "page": null,
      "quote": "--- # United States v. Gastiaburo *16 F.3d 582 (4th Cir. 1994)* \u00b7 U.S. Court of Appeals, Fourth Circuit \u00b7 **Binding in-circuit \u2014 4th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gastiaburo's car was seized on October 8, 1991. Thirty-eight days later, on November 15, 1991, after his passenger Dina Viola told the police there was a hidden compartment behind the radio containing drugs, money, and a handgun, officer Cosslett went to the impound lot and searched that compartment without a warrant, recovering a gun and a 24-gram rock of crack cocaine. Gastiaburo moved to suppress, arguing the impoundment and the 38-day delay defeated the automobile exception. ## Issue Whether the automobile exception justifies a warrantless search of a car that has already been seized and impounded, where 38 days elapsed between the seizure and the search. ## Rule Yes. Probable cause supporting an automobile-exception search is not dissolved by impoundment or by the passage of time. The Fourth Circuit held the government's automobile-exception argument",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-586",
      "page": null,
      "quote": "the justification to conduct a warrantless search under the automobile exception does not disappear merely because the car has been immobilized and impounded.",
      "star_marker": "586",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15463,
      "fragment": "#:~:text=the%20justification%20to%20conduct%20a",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-587",
      "page": null,
      "quote": "Not a single published federal case speaks of a 'temporal limit' to the automobile exception. The Supreme Court has repeatedly stated that a warrantless search of a car (1) need not occur contemporaneously with the car's lawful seizure and (2) need not be justified by the existence of exigent circumstances that might have made it impractical to secure a warrant prior to the search.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1994-02-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Gastiaburo",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Lenzi v. Systemax, Inc.",
          "cluster_id": 4684832,
          "cite": [
            "944 F.3d 97"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gastiaburo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morris v. State",
          "cluster_id": 5281599,
          "cite": [
            "361 S.W.3d 649",
            "2011 Tex. Crim. App. LEXIS 1664",
            "2011 WL 6057840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gastiaburo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Nicholson",
          "cluster_id": 6587522,
          "cite": [
            "58 Mass. App. Ct. 601",
            "792 N.E.2d 124",
            "2003 Mass. App. LEXIS 765"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gastiaburo:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(6929715) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca4)",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 0,
        "triage_read": 0,
        "triage_snippet_classified": 0
      },
      "lane2_top_cited": {
        "query": "cites:(6929715)",
        "reviewed": 3,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(6929715)",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 0,
        "triage_read": 0,
        "triage_snippet_classified": 0
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(6929715)",
    "indexed_citing_opinions": 3,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 6929715,
        "count": 3,
        "count_source": "search"
      }
    ],
    "citation_count": 159,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-gastiaburo.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 3,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T00:05:59Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:06:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:06:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:07:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:06:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Gastiaburo

```
<opinion type="majority">
<p id="b684-6">OPINION</p>
<author id="b684-7">MURNAGHAN, Circuit Judge:</author>
<p id="b684-8">After pulling over defendant-appellant, Joseph Gastiaburo, for a routine traffic stop, a Virginia State Trooper conducted a warrant-less consent search of Gastiaburo’s car. The search produced $10,000 cash, drug paraphernalia, and several grams of cocaine base (“crack cocaine”). The state police arrested Gastiaburo and impounded his car.</p>
<p id="b684-9">Five weeks later, after receiving a tip from an acquaintance of Gastiaburo, the police conducted a warrantless search of a hidden compartment in the car’s dashboard and seized a loaded semiautomatic pistol and a much larger quantity of crack cocaine. The district court denied Gastiaburo’s motion to suppress the evidence seized during the latter search.</p>
<p id="b684-10">At trial under an indictment charging (a) possession of drugs with intent to distribute, (b) carrying a firearm during and in relation to a drug trafficking crime, and (c) possession of a firearm by a convicted felon, the government put a law enforcement officer on the stand as an expert on drug trafficking practices and techniques. Over and beyond direct and cross-examination, the district judge asked the government’s expert several questions; later, he asked the defense’s sole witness several questions, as well. The jury convicted Gastiaburo on all counts, and the district judge sentenced him to 322 months imprisonment. He has appealed.</p>
<p id="b684-11">
<em>I. The Facts</em>
</p>
<p id="b684-12">At midday on October 8,1991, Joseph Gas-tiaburo and a passenger, Dina Viola, were heading southbound on Interstate 95. Virginia State Police Trooper Mark Cosslett pulled Gastiaburo over for reckless driving. Adhering to state police procedures for a routine traffic stop, Cosslett asked Gastiabu-ro for his license and registration and also asked if he was transporting any drugs or weapons. Gastiaburo replied that he was not, and asked Cosslett whether he would like to take a look in the vehicle. Cosslett replied, “You don’t mind if I take a look through your vehicle?” Gastiaburo answered, “No, go ahead.” Cosslett reiterated his request and explicitly confirmed that Gas-tiaburo had no objections to a search of both the vehicle and any containers therein.</p>
<p id="b684-13">Following those repeated consents to a search, Cosslett placed Gastiaburo in the police cruiser, wrote out a traffic citation, and waited for a backup officer. After the backup arrived, Gastiaburo was again asked for permission to search the vehicle, including any containers, and he again consented. With Gastiaburo sitting on the interstate guardrail adjacent to the car, Cosslett commenced his search. The search produced, among other things, a set of hand scales, rolling papers, razor blades, a knife with a retractable blade, a large number of small plastic baggies, an address book with various names and financial notations, a paging device or “beeper,” $10,000 in cash (folded into $100 increments), a box of .25 caliber ammunition, and a black leather zippered pouch containing twenty-one small zip-locked plastic baggies, each containing about one-fifth of a gram of a rock-like substance that was subsequently determined to be crack cocaine.</p>
<p id="b684-14">The backup officer arrested Gastiaburo and drove him to a nearby detention center. His car was seized for forfeiture by the Commonwealth of Virginia and removed to an impoundment lot at the regional State Police headquarters, where it was secured by parking state vehicles around it. The next morning an inventory search of the impounded car produced no additional contraband.</p>
<p id="b684-15">On November 15, 1991, Cosslett and Viola, Gastiaburo’s passenger at the time of arrest, <page-number citation-index="1" label="585">*585</page-number>met at the Prince William County Courthouse. Viola inquired whether he had found the gun. When Cosslett said that he had not, Viola told him that there was a hidden compartment located behind the radio in the console of Gastiaburo’s car, and that the compartment contained drugs, money, and a handgun.</p>
<p id="b685-4">Cosslett promptly went to the impound lot and, without obtaining a warrant, searched for and located the hidden compartment. He found and seized a loaded, .25 caliber semiautomatic pistol and, wrapped in aluminum foil and then in brown paper lunch bags, a lump of rock-like substance that was subsequently determined to be a 24-gram “rock” of crack cocaine.</p>
<p id="b685-5">A grand jury of the United States District Court for the Eastern District of Virginia returned the above-mentioned three-count indictment against Gastiaburo. On April 3, 1992, a suppression hearing took place. After listening to conflicting testimony from Gastiaburo and Cosslett, the district judge resolved the credibility conflicts in Cosslett’s favor and denied all of Gastiaburo’s motions, including a motion to suppress the gun and the crack cocaine that Cosslett had seized during his warrantless search of the impounded car on November 15, 1991.</p>
<p id="b685-6">On April 22, 1992, Gastiaburo was tried before a jury in Judge Ellis’s courtroom. The government called Cosslett, who gave testimony substantially similar to his earlier testimony at the suppression hearing. The government also called Sergeant Floyd Johnston of the U.S. Park Police as an expert in the field of drug trafficking practices and techniques. Among other things, Johnston examined the various government exhibits that had been seized from Gastiaburo’s car and testified that they were generally consistent with crack cocaine distribution, rather than with mere personal use of the drug. In response to questions from the bench, Johnston also testified about the quantities of crack cocaine consumed by typical addicts.</p>
<p id="b685-7">Gastiaburo called only one witness, Charles J. Pucci, his brother-in-law. Pucci testified that Gastiaburo had visited him in New York City shortly before the arrest, and that he had given Gastiaburo $10,000 in loose cash to pay a debt to a family member in Florida. The court asked Pucci several questions about the cash, and also inquired about Pucci’s occupation. Judge Ellis then asked whether Pucci had ever been convicted of a felony. Pucci responded, “I have not.”</p>
<p id="b685-9">The jury returned guilty verdicts on all three counts. The district court imposed a sentence of 322 months imprisonment plus five years of supervised release, $10,000 forfeiture, and $150 in special assessments. Gastiaburo’s appeal followed.</p>
<p id="b685-10">
<em>II. The Gun and Cocaine Seized on November 15, 1991</em>
</p>
<p id="b685-11">Gastiaburo has contended that the gun and the 24-gram rock of crack cocaine that the police seized from his car on November 15, 1991 should have been suppressed because they were obtained without a warrant, in violation of his Fourth Amendment rights. In response the government has argued that the district court’s denial of Gastiaburo’s motion to suppress should be affirmed on- any of four grounds: (1) the evidence was seized during a valid consent search; (2) the evidence was seized during a valid inventory search; (3) the police had probable cause to believe the search would uncover contraband (i.e., the so-called “automobile exception” to the warrant requirement); or (4) the evidence was seized during a valid search of a vehicle subject to forfeiture. The third argument, based on the “automobile exception” to the warrant requirement, is clearly correct. Because we review such a mixed question of law and fact <em>de novo, see, e.g., United States v. Moore, </em><span class="citation" data-id="487763"><a href="/opinion/487763/united-states-v-norman-delano-moore/#1106" aria-description="Citation for case: United States v. Norman Delano Moore">817 F.2d 1105, 1106-08</a></span> (4th Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./484/965/">484 U.S. 965</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./108/456/">108 S.Ct. 456</a></span>, <span class="citation" data-id="9067158"><a href="/opinion/9073337/smith-v-united-states-merit-systems-protection-board/" aria-description="Citation for case: Smith v. United States Merit Systems Protection Board">98 L.Ed.2d 396</a></span> (1987), the district court’s decision not to suppress the evidence seized on November 15, 1991 should be affirmed.</p>
<p id="b685-12">The Fourth Amendment protects the “right of the people to be secure in their persons, houses, papers, and effects against unreasonable searches and seizures.” U.S. Const. amend. IV. Searches conducted without a warrant issued by a judge or magistrate upon probable cause “are <em>per se </em>unreasonable under the Fourth Amendment — subject only to a few specifically established and <page-number citation-index="1" label="586">*586</page-number>well-delineated exceptions.” <em>California v. Acevedo, </em><span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">500 U.S. 565</a></span>, -, -, <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/#1991" aria-description="Citation for case: California v. Acevedo">111 S.Ct. 1982, 1991</a></span>, <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">114 L.Ed.2d 619</a></span> (1991) (citations and internal quotation marks omitted); <em>see also United States v. Turner, </em><span class="citation no-link">9383 F.2d 240</span>, 244 (4th Cir.1991). At least since 1925, when the Supreme Court handed down its decision in <em>Carroll v. United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U.S. 132</a></span>, <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">45 S.Ct. 280</a></span>, <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">69 L.Ed. 543</a></span> (1925), the federal judiciary has recognized an “automobile exception” to the warrant requirement: it may be reasonable and therefore constitutional to search a movable vehicle without a warrant, even though it would be unreasonable and unconstitutional to conduct a similar search of a home, store, or other fixed piece of property. <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States"><em>See id. </em>at 153, 158-59</a></span>, <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#285" aria-description="Citation for case: Carroll v. United States">45 S.Ct. at 285, 287</a></span>.</p>
<p id="b686-6">The Supreme Court delivered its most recent exposition on the “automobile exception” in <em>California v. <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">Acevedo, supra.</a></span> </em>The <em><span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">Acevedo</a></span> </em>Court held that “[t]he police may search an automobile and the containers within it where they have probable cause to believe contraband or evidence is contained.” Ill S.Ct. at 1991. “[T]he scope of a warrant-less search of an automobile is ‘no narrower — and no broader — than the scope of a search authorized by a warrant supported by probable cause.’” <em>United States v. $29,000</em>—U.S. <em>Currency, </em><span class="citation" data-id="442875"><a href="/opinion/442875/united-states-v-29000-us-currency-in-re-2900000-us-currency/#855" aria-description="Citation for case: United States v. $29,000--u.s. Currency, in Re 29,000.00...">745 F.2d 853, 855</a></span> (4th Cir.1984) (quoting <em>United States v. Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#823" aria-description="Citation for case: United States v. Ross">456 U.S. 798, 823</a></span>, <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#2172" aria-description="Citation for case: United States v. Ross">102 S.Ct. 2157, 2172</a></span>, <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">72 L.Ed.2d 572</a></span> (1982)). With or without warrant, the scope of the search of an automobile is defined by the object of the search and the places in which there is probable cause to believe that it may be found. For example, probable cause to believe that a container placed in the trunk of an automobile contains contraband does not justify a search of the entire car. <em>See Acevedo, </em>500 U.S. at -, <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">111 S.Ct. at 1991</a></span> (citing <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross">456 U.S. at 824</a></span>, <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#2172" aria-description="Citation for case: United States v. Ross">102 S.Ct. at 2172</a></span>).</p>
<p id="b686-9">In the present case, as of November 15, 1991, the police had probable cause to believe that one particular area within Gastiaburo’s car contained as-yet undiscovered contraband. On that date, Dina Viola, Gastiaburo’s passenger at the time <em>of - </em>his arrest, met Cosslett at the Prince William County Courthouse and told him that there was a hidden compartment behind the radio in the console of Gastiaburo’s car and that the compartment contained additional drugs and money, as well as a handgun. Those facts are uneon-troverted, and they would have more than sufficed to justify the issuance of a warrant by a magistrate. Therefore, they also sufficed to justify a warrantless search of the area behind the radio.</p>
<p id="b686-11">Furthermore, the facts in the record indicate no overreaching by the police. As of November 15, 1991, the police apparently had probable cause to believe that contraband remained hidden only where Viola had told Cosslett to look. Appropriately, Cos-slett confined his search to that area. And Gastiaburo does not claim that the search of November 15, 1991 covered a broader scope than that contained in the tip that gave Cos-slett probable cause. Therefore, the November 15, 1991 search complied with the requirements of the Fourth Amendment.</p>
<p id="b686-12">Gastiaburo has made two responses to the government’s “automobile exception” argument. First, he has contended that im-poundment effectively transformed his car from a movable vehicle into a “fixed piece of property,” thus making the automobile exception to the warrant requirement inapplicable. However, the justification to conduct a warrantless search under the automobile exception does not disappear merely because the car has been immobilized and impounded. See <em>United States v. Johns, </em><span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/#484" aria-description="Citation for case: United States v. Johns">469 U.S. 478, 484</a></span>, <span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/#885" aria-description="Citation for case: United States v. Johns">105 S.Ct. 881, 885</a></span>, <span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/" aria-description="Citation for case: United States v. Johns">83 L.Ed.2d 890</a></span> (1985); <em>Florida v. Meyers, </em><span class="citation" data-id="9429577"><a href="/opinion/111157/florida-v-meyers/#382" aria-description="Citation for case: Florida v. Meyers">466 U.S. 380, 382</a></span>, <span class="citation" data-id="9429577"><a href="/opinion/111157/florida-v-meyers/#1853" aria-description="Citation for case: Florida v. Meyers">104 S.Ct. 1852, 1853</a></span>, <span class="citation" data-id="9429577"><a href="/opinion/111157/florida-v-meyers/" aria-description="Citation for case: Florida v. Meyers">80 L.Ed.2d 381</a></span> (1984) (per curiam); <em>Michigan v. Thomas, </em><span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#261" aria-description="Citation for case: Michigan v. Thomas">458 U.S. 259, 261</a></span>, <span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/" aria-description="Citation for case: Michigan v. Thomas">102 S.Ct. 3079</a></span>-3080-81, <span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/" aria-description="Citation for case: Michigan v. Thomas">73 L.Ed.2d 750</a></span> (1982) (per curiam); <em>see also Turner, </em>933 F.2d at 244; <em>$29,000</em>—U.S. <em>Currency, </em><span class="citation" data-id="442875"><a href="/opinion/442875/united-states-v-29000-us-currency-in-re-2900000-us-currency/#855" aria-description="Citation for case: United States v. $29,000--u.s. Currency, in Re 29,000.00...">745 F.2d at 855</a></span>. Under the Supreme Court’s precedents, the fact that impoundment may have made it virtually impossible for anyone to drive the car away or to tamper with its contents is irrelevant to the constitutionality of a warrantless search under the circumstances of the present case. <em>See, e.g., Thomas, </em><span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#261" aria-description="Citation for case: Michigan v. Thomas">458 U.S. at 261</a></span>, <span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#3081" aria-description="Citation for case: Michigan v. Thomas">102 S.Ct. at 3081</a></span>.</p>
<p id="b686-13">Second, Gastiaburo has noted that thirty-eight days transpired between the sei<page-number citation-index="1" label="587">*587</page-number>zure of his car on October 8, 1991 and the warrantless search in question, and has argued that the delay violated the “temporal limit on the automobile exception” and that “it was a <em>per se </em>unreasonable delay.” Gastia-buro’s “delay” argument also lacks merit. Not a single published federal case speaks of a “temporal limit” to the automobile exception. The Supreme Court has repeatedly stated that a warrantless search of a car (1) need not occur contemporaneously with the car’s lawful seizure and (2) need not be justified by the existence of exigent circumstances that might have made it impractical to secure a warrant prior to the search. <em>See Acevedo, </em>500 U.S. at -, <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/#1986" aria-description="Citation for case: California v. Acevedo">111 S.Ct. at 1986</a></span> (explaining that the police can search later whenever they could have searched earlier, had they so chosen) (describing the Court’s reasoning in <em>Chambers v. Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney">399 U.S. 42, 51-52</a></span>, <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#1981" aria-description="Citation for case: Chambers v. Maroney">90 S.Ct. 1975, 1981-82</a></span>, <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">26 L.Ed.2d 419</a></span> (1970)); <em>Johns, </em><span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/#484" aria-description="Citation for case: United States v. Johns">469 U.S. at 484-85</a></span>, <span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/#885" aria-description="Citation for case: United States v. Johns">105 S.Ct. at 885-86</a></span>; <em>Thomas, </em><span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#261" aria-description="Citation for case: Michigan v. Thomas">458 U.S. at 261-62</a></span>, <span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#3080" aria-description="Citation for case: Michigan v. Thomas">102 S.Ct. at 3080-81</a></span>. Therefore, the passage of time between the seizure and the search of Gastiaburo’s car is legally irrelevant.</p>
<p id="b687-6">Moreover, Cosslett’s actual “delay” here was minimal: he conducted the search on the very same day that he first had probable cause to believe contraband could be found behind the dashboard of Gastiaburo’s car. Cosslett testified at the suppression hearing that, upon learning of the hidden compartment in Gastiaburo’s dashboard, he proceeded “to the headquarters, obtained the keys from the evidence custodian, removed the vehicles [that were blocking in Gastiaburo’s ear], and checked the hidden compartment.” Such an expeditious search cannot be deemed <em>“per se </em>unreasonable.” Rather, it falls squarely within the specifically established and well-delineated “automobile exception” to the Fourth Amendment’s warrant requirement.</p>
<p id="b687-7">
<em>III. Expert Testimony</em>
</p>
<p id="b687-8">Gastiaburo next has contended that the district court erred in admitting expert testimony from Sergeant Johnston that included (1) an opinion as to Gastiaburo’s intent, allegedly in violation of Rule 704(b) of the Federal Rules of Evidence; and (2) matters within the common understanding of the jurors, allegedly in violation of Rule 702.</p>
<p id="b687-11"><em>A Johnston’s testimony on “intent to distribute.” </em>The prosecutor had asked Johnston: “Would you have an opinion based on your training and experience what that crack cocaine [that the police had seized from the hidden compartment in Gastiaburo’s car and the twenty-one zip-locked plastic baggies, each containing a “hit” of crack cocaine], ... were possessed for, taking all the elements into consideration?” Johnston replied: “Clearly, based on my opinion, my training and experience, it was certainly possessed with the intent to distribute.” Gastiaburo’s trial attorney did not object. On appeal, Gastiaburo has claimed that Johnston’s answer provided expert opinion testimony on Gastiaburo’s intent in a specific-intent crime, a violation of Federal Rule of Evidence 704(b).</p>
<p id="b687-12">Because Gastiaburo did not object at trial, we review the admission of Johnston’s expert testimony for plain error. Rule 52(b) of the Federal Rules of Criminal Procedure provides that “[p]lain errors or defects affecting substantial rights may be noticed although they were not brought to the attention of the court.” Fed.R.Crim.P. 52(b). The Supreme Court recently interpreted Rule 52(b) to require not only the existence of an “error” <em>(i.e., </em>a “[deviation from a legal rule” that the defendant has not waived), but also that the error be “plain” <em>(i.e., </em>“clear” or, equivalently, “obvious” under the current applicable law). <em>United States v. Olano, </em>— U.S. -, -, <span class="citation" data-id="9432789"><a href="/opinion/112848/united-states-v-olano/#1777" aria-description="Citation for case: United States v. Olano">113 S.Ct. 1770, 1777</a></span>, <span class="citation" data-id="9432789"><a href="/opinion/112848/united-states-v-olano/" aria-description="Citation for case: United States v. Olano">123 L.Ed.2d 508</a></span> (1993) (citations and internal quotation marks omitted).</p>
<p id="b687-15">Rule 704(b) of the Federal Rules of Evidence provides:</p>
<blockquote id="b687-16">No expert witness testifying with respect to the mental state or condition of a defendant in a criminal case may state an opinion or inference as to whether the defendant did or did not have the mental state or condition constituting an element of the crime charged or of a defense thereto. Such ultimate issues are matters for the trier of fact alone.</blockquote>
<p id="b688-3"><page-number citation-index="1" label="588">*588</page-number>Fed.R.Evid. 704(b). Rule 704(b) was enacted in the wake of the attempted assassination of President Reagan and the murder of John Lennon, and was an attempt to constrain psychiatric testimony on behalf of defendants asserting the insanity defense. <em>See generally </em>Anne Lawson Braswell, Note, <em>Resurrection of the Ultimate Issue Rule: Federal Rule of Evidence 701(b) and the Insanity Defense, </em>72 Cornell L.Rev. 620 (1987). The application of the same rule in an entirely different context — a law enforcement officer’s expert opinion testimony on behalf of the government at the trial of an alleged drug dealer — is murky at best.</p>
<p id="b688-4">Was Johnston in fact “testifying with respect to the mental state or condition of a defendant in a criminal case”? Did he actually “state an opinion or inference as to whether the defendant did or did not have the mental state or condition constituting an element” of the crime of possession of cocaine with intent to distribute? The testimony lends itself to the interpretation that possession of the quantity of crack cocaine seized from Gastiaburo’s car — with the individual “hits” packaged in twenty-one small zip-locked baggies, and the larger “rock” in foil and paper bags — was consistent with the distribution of cocaine, rather than with mere personal use of the drug.</p>
<p id="b688-5">In any event, Gastiaburo’s failure to object at the trial made the relevant inquiry for us whether Judge Ellis committed a “plain error” under Rule 52(b). The error, if any, was not “plain” (or “clear” or “obvious”). <em>Cf. Olano, </em>— U.S. at -, <span class="citation" data-id="9432789"><a href="/opinion/112848/united-states-v-olano/#1777" aria-description="Citation for case: United States v. Olano">113 S.Ct. at 1777</a></span>. Most appellate panels have refused to find error in the admission of expert testimony on intent to distribute controlled substances. <em>See, e.g., United States v. Valentine, </em><span class="citation" data-id="599184"><a href="/opinion/599184/united-states-v-glenn-valentine/#910" aria-description="Citation for case: United States v. Glenn Valentine">984 F.2d 906, 910</a></span> (8th Cir.), <em>cert. denied, </em>— U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./114/93/">114 S.Ct. 93</a></span>, <span class="citation" data-id="113210"><a href="/opinion/113210/robinson-v-central-brass-manufacturing-co/" aria-description="Citation for case: Robinson v. Central Brass Manufacturing Co.">126 L.Ed.2d 60</a></span> (1993); <em>United States v. Chin, </em><span class="citation" data-id="597101"><a href="/opinion/597101/united-states-v-andrew-p-chin/#1279" aria-description="Citation for case: United States v. Andrew P. Chin">981 F.2d 1275, 1279</a></span> (D.C.Cir.1992), <em>cert. denied, </em>—— U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./113/2377/">113 S.Ct. 2377</a></span>, <span class="citation no-link">124 L.Ed.2d 281</span> (1993); <em>United States v. Williams, </em><span class="citation" data-id="596385"><a href="/opinion/596385/united-states-v-patrick-a-williams/#1465" aria-description="Citation for case: United States v. Patrick A. Williams">980 F.2d 1463, 1465-66</a></span> (D.C.Cir.1992); <em>United States v. Wilson, </em><span class="citation" data-id="583690"><a href="/opinion/583690/united-states-v-terry-wilson/#810" aria-description="Citation for case: United States v. Terry Wilson">964 F.2d 807, 810</a></span> (8th Cir.1992); <em>United States v. Gomez-Norena, </em><span class="citation" data-id="544744"><a href="/opinion/544744/united-states-v-jaime-leon-gomez-norena/#502" aria-description="Citation for case: United States v. Jaime Leon Gomez-Norena">908 F.2d 497, 502</a></span> (9th Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./498/947/">498 U.S. 947</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./111/363/">111 S.Ct. 363</a></span>, <span class="citation" data-id="9097104"><a href="/opinion/9102741/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">112 L.Ed.2d 326</a></span> (1990); <em>United States v. Alvarez, </em><span class="citation" data-id="500424"><a href="/opinion/500424/united-states-v-marcelino-efrain-alvarez-jose-delgado-ramirez-juan-ramon/#1030" aria-description="Citation for case: United States v. Marcelino Efrain Alvarez, Jose Delgado...">837 F.2d 1024, 1030-31</a></span> (11th Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./486/1026/">486 U.S. 1026</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./108/2003/">108 S.Ct. 2003</a></span>, 2004, <span class="citation no-link">100 L.Ed.2d 234</span>, 235 (1988).<footnotemark>*</footnotemark> One recent D.C. Circuit decision did find that the admission of expert testimony on the defendant’s intent to distribute violated Rule 704(b), but went on to hold that the error was not “plain” under the settled law of the Supreme Court or the D.C. Circuit, as it stood at the time of the trial. <em>See United States v. Mitchell, </em><span class="citation" data-id="609728"><a href="/opinion/609728/united-states-v-keith-len-mitchell-united-states-of-america-v-richard/#421" aria-description="Citation for case: United States v. Keith Len Mitchell, United States of...">996 F.2d 419, 421-23</a></span> (D.C.Cir.1993).</p>
<p id="b688-16"><em>B. Johnston’s other testimony. </em>Gastiaburo also has contended that the district court should have rejected various parts of Johnston’s testimony as insufficiently helpful for the trier of fact under Federal Rule of Evidence 702. On direct examination, Johnston testified, over defense counsel’s objection, that it is not uncommon for people transporting controlled substances to grant consent to law enforcement officers to search their possessions or their persons. He also testified about the attributes of persons involved in the distribution of drugs and the “tools of the <em>trade” </em>— e.g., beepers, address books, the quantities of drugs possessed by dealers, and so on. During defense counsel’s cross-examination, Judge Ellis interjected, asking Johnston about half-a-dozen questions. In response, Johnston testified about addicts’ typical levels of crack consumption, typical patterns of addiction, and typical quantities of crack that a user will purchase and hold at any given moment. Although Gastiaburo did not object at trial to the colloquy between Judge Ellis and Johnston, he has complained on appeal that the judge’s questions violated Rule 614 of the Federal Rules of Evidence, <em>see infra </em>Part IV, and that the Johnston’s answers violated Rule 702.</p>
<p id="b688-17">Federal Rule of Evidence 702 provides:</p>
<blockquote id="AMb-">If scientific, technical, or other specialized knowledge-will assist the trier of fact to understand the evidence or to determine a <page-number citation-index="1" label="589">*589</page-number>fact in issue, a witness qualified as an expert by knowledge, skill, experience, training, or education, may testify thereto in the form of an opinion or otherwise.</blockquote>
<p id="Agk">The trial judge has broad discretion under Rule 702. <em>See Hamling v. United States, </em><span class="citation" data-id="9842003"><a href="/opinion/109084/hamling-v-united-states/#108" aria-description="Citation for case: Hamling v. United States">418 U.S. 87, 108</a></span>, <span class="citation" data-id="9842003"><a href="/opinion/109084/hamling-v-united-states/#2903" aria-description="Citation for case: Hamling v. United States">94 S.Ct. 2887, 2903</a></span>, <span class="citation" data-id="9842003"><a href="/opinion/109084/hamling-v-united-states/" aria-description="Citation for case: Hamling v. United States">41 L.Ed.2d 590</a></span> (1974) (“[T]he District Court has wide discretion in its determination to admit and exclude evidence, and this is particularly true in the case of expert testimony.”) (citations omitted); <em>cf. United States v. Ham, </em><span class="citation" data-id="9011910"><a href="/opinion/9018724/united-states-v-ham/#1252" aria-description="Citation for case: United States v. Ham">998 F.2d 1247, 1252</a></span> (4th Cir.1993).</p>
<p id="b689-4">As then-Judge Ruth Bader Ginsburg has explained: “In accord with the commodious standard of Federal Rule of Evidence 702, expert testimony on the <em>modus operandi </em>of criminals ‘is commonly admitted,’ particularly regarding the methods of drug dealers.” <em>Chin, </em><span class="citation" data-id="597101"><a href="/opinion/597101/united-states-v-andrew-p-chin/" aria-description="Citation for case: United States v. Andrew P. Chin">981 F.2d at 1279</a></span> (quoting <em>United States v. Dunn, </em><span class="citation" data-id="506047"><a href="/opinion/506047/united-states-v-richard-earl-dunn-united-states-of-america-v-angelo/#763" aria-description="Citation for case: United States v. Richard Earl Dunn, United States of...">846 F.2d 761, 763</a></span> (D.C.Cir.1988)); <em>see also Mitchell, </em><span class="citation" data-id="609728"><a href="/opinion/609728/united-states-v-keith-len-mitchell-united-states-of-america-v-richard/#423" aria-description="Citation for case: United States v. Keith Len Mitchell, United States of...">996 F.2d at 423</a></span> (“Federal courts often allow expert testimony on narcotics operations to familiarize jurors with the variety of methods by which drug dealers attempt to pursue and conceal their activities_”) (citing <em>Dunn, </em><span class="citation" data-id="506047"><a href="/opinion/506047/united-states-v-richard-earl-dunn-united-states-of-america-v-angelo/#763" aria-description="Citation for case: United States v. Richard Earl Dunn, United States of...">846 F.2d at 763</a></span>).</p>
<p id="b689-7">We have repeatedly upheld the admission of law enforcement officers’ expert opinion testimony in drug trafficking eases. <em>See, e.g., United States v. Safari, </em><span class="citation" data-id="507790"><a href="/opinion/507790/united-states-v-mahmoud-safari/#895" aria-description="Citation for case: United States v. Mahmoud Safari">849 F.2d 891, 895</a></span> (4th Cir.) (upholding the admission of expert testimony on the size of an average dose of heroin, because, “[w]hile not usurping the function of the jury, this testimony aided the jury dining its deliberations, for most laymen are not familiar with the quantity, purity, and dosage units of heroin”), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./488/945/">488 U.S. 945</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./109/374/">109 S.Ct. 374</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/102/363/">102 L.Ed.2d 363</a></span> (1988); <em>United States v. Monu, </em><span class="citation" data-id="464629"><a href="/opinion/464629/united-states-v-ifeanyi-monu/#1210" aria-description="Citation for case: United States v. Ifeanyi Monu">782 F.2d 1209, 1210-11</a></span> (4th Cir.1986) (upholding the admission of two investigative agents’ expert opinion testimony regarding the purity of heroin and heroin distributors’ use of triple-beam balance scales). Similarly, in <em>United States v. Wilson, </em><span class="citation" data-id="583690"><a href="/opinion/583690/united-states-v-terry-wilson/#809" aria-description="Citation for case: United States v. Terry Wilson">964 F.2d at 809-10</a></span>, the Eighth Circuit upheld a conviction for possession with intent to distribute and affirmed the admission of a drug enforcement agent’s testimony that, based upon his experience and training, 130 grams of methamphetamine (the amount seized from the defendant) was more than generally possessed by mere users of the drug. The Eighth Circuit found no abuse of discretion in admitting the agent’s testimony: “Such testimony aids the jury by putting the drug dealer in context with the drug world. It is a reasonable assumption that a jury is not well versed in the behavior and average consumption of drug users.” <span class="citation" data-id="583690"><a href="/opinion/583690/united-states-v-terry-wilson/#810" aria-description="Citation for case: United States v. Terry Wilson"><em>Id. </em>at 810</a></span> (citation omitted); <em>see also United States v. Foster, </em><span class="citation" data-id="565036"><a href="/opinion/565036/united-states-v-derek-foster/#452" aria-description="Citation for case: United States v. Derek Foster">939 F.2d 445, 452</a></span> (7th Cir.1991) (noting that “jurors are not well versed in the behavior of drug dealers”). Here, too, the. district court properly admitted Johnston’s expert testimony.</p>
<p id="b689-10">
<em>IV. The District Judge’s Questioning of Witnesses</em>
</p>
<p id="b689-11">Gastiaburo has further contended that he was denied a fair trial because the district judge violated Rule 614 of the Federal Rules of Evidence by improperly questioning witnesses at trial. Gastiaburo has claimed that there was error in the judge’s questioning of Charles Pucci, Gastiaburo’s brother-in-law and the only witness whom Gastiaburo called at trial. At the end of the government’s cross-examination of Pucci, the judge asked him whether he typically sent $10,000 payments in cash via his brother-in-law (Gastiaburo), where he got the cash, what his occupation was, and whether he had ever been convicted of a felony. Gastiaburo did not object to those questions at trial.</p>
<p id="b689-12">Gastiaburo’s argument appears to come too late. The plain language of Rule 614(c) of the Federal Rules of Evidence requires objections to the trial judge’s interrogation of witnesses “[to] be made at the time or at the next available opportunity when the jury is not present.” Fed.R.Evid. 614(c). We, interpreting that rule, have held that “the failure of ... counsel to object to any of [the district judge’s] questioning at trial precludes our review of this issue on appeal.” <em>Stillman v. Norfolk &amp; W. Ry. Co., </em><span class="citation" data-id="483263"><a href="/opinion/483263/carl-r-stillman-v-norfolk-western-railway-company-a-corporation/#839" aria-description="Citation for case: Carl R. Stillman v. Norfolk &amp; Western Railway Company, a...">811 F.2d 834, 839</a></span> (4th Cir.1987).</p>
<p id="b689-13"><em><span class="citation" data-id="483263"><a href="/opinion/483263/carl-r-stillman-v-norfolk-western-railway-company-a-corporation/" aria-description="Citation for case: Carl R. Stillman v. Norfolk &amp; Western Railway Company, a...">Stillman</a></span> </em>recognized a “limited exception” to the general rule against appellate review “‘[w]here a trial judge’s comments were so prejudicial as to deny a party an opportunity for a fair and impartial trial.’” <page-number citation-index="1" label="590">*590</page-number><em><span class="citation" data-id="483263"><a href="/opinion/483263/carl-r-stillman-v-norfolk-western-railway-company-a-corporation/" aria-description="Citation for case: Carl R. Stillman v. Norfolk &amp; Western Railway Company, a...">Id.</a></span> </em>(quoting <em>Miley v. Delta Marine Drilling Co., </em><span class="citation" data-id="308314"><a href="/opinion/308314/burns-miley-jr-v-delta-marine-drilling-company/#857" aria-description="Citation for case: Burns Miley, Jr. v. Delta Marine Drilling Company">473 F.2d 856, 857-58</a></span> (5th Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./414/871/">414 U.S. 871</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./94/93/">94 S.Ct. 93</a></span>, <span class="citation" data-id="8987391"><a href="/opinion/8995064/thomas-v-estelle/" aria-description="Citation for case: Thomas v. Estelle">38 L.Ed.2d 89</a></span> (1973)). In sketching the contours of that “limited exception,” we cited a case in which the judge interrupted the witness to answer the counsel’s question himself, referred to the question as one that “any five-year-old idiot” could answer, and then instructed counsel, “Don’t waste my time and the jury’s on that.” <em><span class="citation" data-id="8987391"><a href="/opinion/8995064/thomas-v-estelle/" aria-description="Citation for case: Thomas v. Estelle">Id.</a></span> </em>(internal quotation marks omitted). Even those inflammatory and insulting comments were deemed <em>not </em>“sufficiently biased or notorious” to permit appellate review absent any objection at trial. <em><span class="citation" data-id="8987391"><a href="/opinion/8995064/thomas-v-estelle/" aria-description="Citation for case: Thomas v. Estelle">Id.</a></span></em></p>
<p id="b690-4">Clearly, none of the questions that Judge Ellis asked of Johnston (a topic dealt with above) even began to approach the level of “bias” or “notoriety” found in the above-cited example. The same can be said of Judge Ellis’s questioning of Pucci, with one qualification. Judge Ellis may appear to have overstepped the bounds of proper judicial interrogation when he asked the criminal defendant’s sole witness whether he had ever been convicted of a felony. Seen in the printed record, the absence of any particularized, good-faith basis made the question inappropriate.</p>
<p id="b690-5">However, while Judge Ellis’s final question of Pucci may have been improvident, it was not so prejudicial as to deny Gastiaburo the opportunity for a fair and impartial trial. Judge Ellis was not requested to retract the question. The answer to it, promptly given, was in the negative. Thus, Gastiaburo’s failure to object to Judge Ellis’s interrogation during the trial is fatal to his argument on appeal.</p>
<p id="b690-6">
<em>V. Ineffective Assistance of Counsel at Sentencing</em>
</p>
<p id="b690-7">Finally, Gastiaburo has contended that he was denied the effective assistance of counsel at sentencing when, after he claimed on the record that his trial counsel had been ineffective, his counsel failed to alloeute on his behalf.</p>
<p id="b690-8">A claim of ineffective assistance of counsel should be raised by motion under <span class="citation no-link">28 U.S.C. § 2255</span> in the district court and not on direct appeal, unless it “conclusively appears” from the record that defense counsel did not provide effective representation. <em>United States v. Fisher, </em><span class="citation" data-id="310396"><a href="/opinion/310396/united-states-v-ronald-richard-fisher/#302" aria-description="Citation for case: United States v. Ronald Richard Fisher">477 F.2d 300, 302</a></span> (4th Cir.1973) (citing <em>United States v. Mandello, </em><span class="citation" data-id="290322"><a href="/opinion/290322/united-states-v-mauro-m-mandello/#1023" aria-description="Citation for case: United States v. Mauro M. Mandello">426 F.2d 1021, 1023</a></span> (4th Cir.1970)); <em>see also United States v. DeFusco, </em><span class="citation" data-id="572183"><a href="/opinion/572183/united-states-v-david-allen-hagen-defusco-two-cases/#120" aria-description="Citation for case: United States v. David Allen Hagen Defusco, (Two Cases)">949 F.2d 114, 120-21</a></span> (4th Cir.1991), <em>cert. denied, </em>— U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./112/1703/">112 S.Ct. 1703</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/118/412/">118 L.Ed.2d 412</a></span> (1992); <em>United States v. Percy, </em><span class="citation" data-id="454500"><a href="/opinion/454500/united-states-v-james-percy/#1205" aria-description="Citation for case: United States v. James Percy">765 F.2d 1199, 1205</a></span> (4th Cir.1985).</p>
<p id="b690-12">In the present case, the record on appeal does not conclusively demonstrate ineffective assistance of counsel. Therefore, we do not now address the issue on direct appeal. Gas-tiaburo may assert the claim in a § 2255 <em>habeas </em>motion, if he so chooses.</p>
<p id="b690-13">
<em>VI. Conclusion</em>
</p>
<p id="A-y">Accordingly, the judgment is</p>
<p id="Am_">
<em>AFFIRMED.</em>
</p>
<footnote label="*">
<p id="b688-12">The question presented here has only recently been discussed. At the time of Gastiaburo’s trial, the cases cited here had not yet been decided and published, with the exceptions of <em><span class="citation" data-id="544744"><a href="/opinion/544744/united-states-v-jaime-leon-gomez-norena/" aria-description="Citation for case: United States v. Jaime Leon Gomez-Norena">Gomez-Norena</a></span> </em>and <em><span class="citation" data-id="500424"><a href="/opinion/500424/united-states-v-marcelino-efrain-alvarez-jose-delgado-ramirez-juan-ramon/" aria-description="Citation for case: United States v. Marcelino Efrain Alvarez, Jose Delgado...">Alvarez</a></span>.</em></p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Gouveia.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Gouveia"
type: case
citation: "467 U.S. 180 (1984)"
parallel_cite: "104 S. Ct. 2292; 81 L. Ed. 2d 146; 52 U.S.L.W. 4659"
neutral_cite: 1984 U.S. LEXIS 91
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-05-29
docket: 83-128
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-05-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Gouveia
  varies_by_point: false
  scope_note: "Good law; the attachment rule was reaffirmed in Rothgery v. Gillespie County (2008)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111193/united-states-v-gouveia/"
  cluster_id: 111193
  opinion_id: 9429629
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny"
related: ["[[Kirby v. Illinois]]", "[[Massiah v. United States]]", "[[Brewer v. Williams]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "attachment"]
holding: "The Sixth Amendment right to counsel attaches only at or after the initiation of adversary judicial proceedings (formal charge, preliminary hearing, indictment, information, or arraignment); inmates held in administrative segregation during a preindictment investigation have no Sixth Amendment right to counsel."
lake:
  record_id: United States v. Gouveia
  status: verified
  projected_at: 2026-07-09
---

# United States v. Gouveia

*467 U.S. 180 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gouveia and other federal prison inmates were suspected of a murder committed inside the prison and were placed in administrative detention (segregation) for months while the crime was investigated, before any indictment. They received no appointed counsel during that segregation. After indictment they were appointed counsel, tried, and convicted; the Ninth Circuit [[Reading and Citing Cases#en-banc|en banc]] held they had been entitled to counsel during the preindictment segregation.

## Issue
Whether prison inmates have a Sixth Amendment right to appointed counsel while held in administrative segregation during the investigation of a crime, before adversary judicial proceedings have begun.

## Rule
No. "[O]ur cases have long recognized that the right to counsel attaches only at or after the initiation of adversary judicial proceedings against the defendant." — 467 U.S. at 187. ^pin-187

Adopting the *[[Kirby v. Illinois|Kirby]]* formulation, the Court explained that the recognized points of attachment "have involved points of time at or after the initiation of adversary judicial criminal proceedings — whether by way of formal charge, preliminary hearing, indictment, information, or arraignment." — [467 U.S. at 188](https://www.courtlistener.com/opinion/111193/united-states-v-gouveia/#:~:text=have%20involved%20points%20of%20time) (quoting *Kirby v. Illinois*, 406 U.S. at 689). ^pin-188

The right is tied to the defendant's status as an "accused" facing the prosecutorial forces of the State, which arises only when the government has committed itself to prosecute.

## Application
During their preindictment administrative segregation the inmates were not yet "accused" within the meaning of the Sixth Amendment — no formal charge, indictment, or other adversary judicial proceeding had been initiated. The segregation served institutional security and investigative purposes, not the commencement of prosecution. They therefore had no Sixth Amendment right to counsel for that period, and the loss of any investigative advantage was not a Sixth Amendment injury.

## Conclusion
The Sixth Amendment right to counsel had not attached during preindictment segregation; the Ninth Circuit was reversed. Attachment requires the initiation of adversary judicial proceedings.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The attachment rule stated here is settled and was reaffirmed in *[[Rothgery v. Gillespie County]]* (2008). It marks the dividing line between the Fifth Amendment *[[Miranda v. Arizona|Miranda]]* world (custody) and the Sixth Amendment world (post-charge), and confines the pre-charge attachment suggested by [[Escobedo v. Illinois]].

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny*

## Sources
- *United States v. Gouveia*, 467 U.S. 180 (1984) — https://www.courtlistener.com/opinion/111193/united-states-v-gouveia/ — pinpoints: 187, 188.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "663de7828642b52e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "467 U.S. 180 (1984)", "court": "U.S. Supreme Court", "neutral_cite": "1984 U.S. LEXIS 91", "official_citation_present": true, "parallel_cite": "104 S. Ct. 2292; 81 L. Ed. 2d 146; 52 U.S.L.W. 4659", "title": "United States v. Gouveia", "year": "1984"}}
{"assertion_id": "bd2c4315c6cfb17d", "dimension": "support", "kind": "home_role", "locator": {"home": "Sixth Amendment Right to Counsel"}, "payload": {"home": "Sixth Amendment Right to Counsel", "role": "Key — Progeny", "title": "United States v. Gouveia"}}
{"assertion_id": "e40ce86a2c30ab7b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Sixth Amendment right to counsel attaches only at or after the initiation of adversary judicial proceedings (formal charge, preliminary hearing, indictment, information, or arraignment); inmates held in administrative segregation during a preindictment investigation have no Sixth Amendment right to counsel.", "title": "United States v. Gouveia"}}
{"assertion_id": "3a298f1184004efd", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Gouveia"}}
{"assertion_id": "fbc80c37735b7872", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1984-05-29", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Gouveia", "field_i_validity": "good_law", "scope_note": "Good law; the attachment rule was reaffirmed in Rothgery v. Gillespie County (2008).", "title": "United States v. Gouveia", "varies_by_point": "false"}}
```

### lake record — United States v. Gouveia

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Gouveia",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Gouveia",
    "case_name_short": "Gouveia",
    "case_name_full": "UNITED STATES v. GOUVEIA Et Al.",
    "input_case_name": "United States v. Gouveia",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-05-29",
    "year": 1984,
    "docket": "83-128",
    "cluster_id": 111193,
    "lead_opinion_id": 9429629,
    "sibling_ids": [
      111193,
      9429629,
      9429630,
      9429631
    ],
    "absolute_url": "/opinion/111193/united-states-v-gouveia/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "467 U.S. 180",
      "volume": "467",
      "reporter": "U.S.",
      "page": "180",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 2292",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 L. Ed. 2d 146",
        "volume": "81",
        "reporter": "L. Ed. 2d",
        "page": "146",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4659",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4659",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 91",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "91",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "467 U.S. 180",
        "volume": "467",
        "reporter": "U.S.",
        "page": "180",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 2292",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 L. Ed. 2d 146",
        "volume": "81",
        "reporter": "L. Ed. 2d",
        "page": "146",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 91",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "91",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4659",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4659",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "467 U.S. 180",
    "official_selection": {
      "court_class": "scotus",
      "selected": "467 U.S. 180",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-187",
      "page": null,
      "quote": "--- # United States v. Gouveia *467 U.S. 180 (1984)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gouveia and other federal prison inmates were suspected of a murder committed inside the prison and were placed in administrative detention (segregation) for months while the crime was investigated, before any indictment. They received no appointed counsel during that segregation. After indictment they were appointed counsel, tried, and convicted; the Ninth Circuit en banc held they had been entitled to counsel during the preindictment segregation. ## Issue Whether prison inmates have a Sixth Amendment right to appointed counsel while held in administrative segregation during the investigation of a crime, before adversary judicial proceedings have begun. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-188",
      "page": null,
      "quote": "have involved points of time at or after the initiation of adversary judicial criminal proceedings \u2014 whether by way of formal charge, preliminary hearing, indictment, information, or arraignment.",
      "star_marker": "188",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15774,
      "fragment": "#:~:text=have%20involved%20points%20of%20time",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-05-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Gouveia",
    "varies_by_point": false,
    "scope_note": "Good law; the attachment rule was reaffirmed in Rothgery v. Gillespie County (2008).",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Gouveia:lane1_negative"
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
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Turner v. United States",
          "cluster_id": 4348984,
          "cite": [
            "848 F.3d 767",
            "2017 FED App. 0034P",
            "2017 WL 603848",
            "2017 U.S. App. LEXIS 2629"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Zackary Stewart v. Karl Wagner",
          "cluster_id": 4255669,
          "cite": [
            "836 F.3d 978",
            "2016 U.S. App. LEXIS 16642",
            "2016 WL 4728039"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
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
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Medunjanin",
          "cluster_id": 2675041,
          "cite": [
            "752 F.3d 576",
            "2014 U.S. App. LEXIS 9306",
            "2014 WL 2054016"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Patrick Henry Murphy v. State",
          "cluster_id": 3127894,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Earl Dangerfield v. State",
          "cluster_id": 3096392,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Flores v. State",
          "cluster_id": 1871985,
          "cite": [
            "299 S.W.3d 843",
            "2009 WL 3466009"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
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
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Samuel Constanza Alvarado",
          "cluster_id": 793566,
          "cite": [
            "440 F.3d 191",
            "2006 U.S. App. LEXIS 6055",
            "2006 WL 598152"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
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
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
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
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doggett v. United States",
          "cluster_id": 112780,
          "cite": [
            "120 L. Ed. 2d 520",
            "112 S. Ct. 2686",
            "505 U.S. 647",
            "1992 U.S. LEXIS 4362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 117863,
          "cite": [
            "129 L. Ed. 2d 362",
            "114 S. Ct. 2350",
            "512 U.S. 452",
            "1994 U.S. LEXIS 4827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNeil v. Wisconsin",
          "cluster_id": 112622,
          "cite": [
            "115 L. Ed. 2d 158",
            "111 S. Ct. 2204",
            "501 U.S. 171",
            "1991 U.S. LEXIS 3483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Jackson",
          "cluster_id": 111622,
          "cite": [
            "89 L. Ed. 2d 631",
            "106 S. Ct. 1404",
            "475 U.S. 625",
            "1986 U.S. LEXIS 91",
            "54 U.S.L.W. 4334"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Green v. State",
          "cluster_id": 1657475,
          "cite": [
            "934 S.W.2d 92",
            "1996 Tex. Crim. App. LEXIS 185",
            "1996 WL 512395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maine v. Moulton",
          "cluster_id": 111546,
          "cite": [
            "88 L. Ed. 2d 481",
            "106 S. Ct. 477",
            "474 U.S. 159",
            "1985 U.S. LEXIS 147",
            "54 U.S.L.W. 4039"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patterson v. Illinois",
          "cluster_id": 112127,
          "cite": [
            "101 L. Ed. 2d 261",
            "108 S. Ct. 2389",
            "487 U.S. 285",
            "1988 U.S. LEXIS 2876",
            "56 U.S.L.W. 4733"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Frye",
          "cluster_id": 5607916,
          "cite": [
            "18 Cal. 4th 894",
            "98 Cal. Daily Op. Serv. 5949",
            "959 P.2d 183",
            "98 Daily Journal DAR 8259",
            "77 Cal. Rptr. 2d 25",
            "1998 Cal. LEXIS 4688"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albert L. Wilson v. Edward Murray, Director of the Virginia Department of Corrections",
          "cluster_id": 480360,
          "cite": [
            "806 F.2d 1232",
            "1986 U.S. App. LEXIS 34712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Loud Hawk",
          "cluster_id": 111554,
          "cite": [
            "88 L. Ed. 2d 640",
            "106 S. Ct. 648",
            "474 U.S. 302",
            "1986 U.S. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Montejo v. Louisiana",
          "cluster_id": 145873,
          "cite": [
            "173 L. Ed. 2d 955",
            "129 S. Ct. 2079",
            "556 U.S. 778",
            "2009 U.S. LEXIS 3973"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Guidry v. State",
          "cluster_id": 2342370,
          "cite": [
            "9 S.W.3d 133",
            "1999 Tex. Crim. App. LEXIS 145",
            "1999 WL 1144826"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ibarra v. State",
          "cluster_id": 1960811,
          "cite": [
            "11 S.W.3d 189",
            "1999 Tex. Crim. App. LEXIS 117",
            "1999 WL 956173"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Cobb",
          "cluster_id": 118417,
          "cite": [
            "149 L. Ed. 2d 321",
            "121 S. Ct. 1335",
            "532 U.S. 162",
            "2001 U.S. LEXIS 2696"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Bomar",
          "cluster_id": 1989353,
          "cite": [
            "826 A.2d 831",
            "573 Pa. 426",
            "2003 Pa. LEXIS 920"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mickey",
          "cluster_id": 1226896,
          "cite": [
            "818 P.2d 84",
            "54 Cal. 3d 612",
            "286 Cal. Rptr. 801",
            "91 Daily Journal DAR 13544",
            "91 Cal. Daily Op. Serv. 8732",
            "1991 Cal. LEXIS 4664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Voigt",
          "cluster_id": 722380,
          "cite": [
            "89 F.3d 1050",
            "78 A.F.T.R.2d (RIA) 5577",
            "1996 U.S. App. LEXIS 16287",
            "1996 WL 380609"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rothgery v. Gillespie County",
          "cluster_id": 145785,
          "cite": [
            "171 L. Ed. 2d 366",
            "128 S. Ct. 2578",
            "554 U.S. 191",
            "2008 U.S. LEXIS 5057",
            "21 Fla. L. Weekly Fed. S 429",
            "76 U.S.L.W. 4520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yousef",
          "cluster_id": 781722,
          "cite": [
            "327 F.3d 56",
            "61 Fed. R. Serv. 251",
            "2003 U.S. App. LEXIS 6437"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Johnson",
          "cluster_id": 1205096,
          "cite": [
            "842 P.2d 1",
            "3 Cal. 4th 1183",
            "14 Cal. Rptr. 2d 702",
            "92 Cal. Daily Op. Serv. 9582",
            "92 Daily Journal DAR 15971",
            "1992 Cal. LEXIS 5693"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Willie v. State",
          "cluster_id": 1706565,
          "cite": [
            "585 So. 2d 660",
            "1991 WL 142136"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Conway",
          "cluster_id": 6894227,
          "cite": [
            "108 Ohio St. 3d 214"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Atwood",
          "cluster_id": 1182224,
          "cite": [
            "832 P.2d 593",
            "171 Ariz. 576"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111193 OR 9429629 OR 9429630 OR 9429631) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTQxNzc2MDAwMDAwJnM9Njg5NDIyNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111193+OR+9429629+OR+9429630+OR+9429631%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 11,
        "triage_snippet_classified": 189
      },
      "lane2_top_cited": {
        "query": "cites:(111193 OR 9429629 OR 9429630 OR 9429631)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDAmcz0yMDQwMjgwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111193+OR+9429629+OR+9429630+OR+9429631%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111193 OR 9429629 OR 9429630 OR 9429631)",
        "reviewed": 15,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 15,
        "triage_read": 0,
        "triage_snippet_classified": 15
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111193 OR 9429629 OR 9429630 OR 9429631)",
    "indexed_citing_opinions": 721,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111193,
        "count": 650,
        "count_source": "search"
      },
      {
        "opinion_id": 9429629,
        "count": 93,
        "count_source": "search"
      },
      {
        "opinion_id": 9429630,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429631,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1099,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-gouveia.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc4MTY2MyZzPTgyNDg5NzAmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28111193+OR+9429629+OR+9429630+OR+9429631%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111193,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 104637,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 108148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 108420,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 108590,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 108846,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 109097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 109331,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 109429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 109442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 109682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 109757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 110300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 110372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 110474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 110686,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 110829,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 322550,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 338481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 363882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 387309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 413324,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 416732,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 1236300,
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
    "date_created": "2026-07-06T00:11:44Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:11:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:11:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:15:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:11:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Gouveia

```
<opinion type="majority">
<author id="b240-5">Justice Rehnquist</author>
<p id="A7g">delivered the opinion of the Court.</p>
<p id="b240-6">Respondents William Gouveia, Robert Ramirez, Adolpho Reynoso, and Philip Segura were convicted of murdering a fellow inmate at a federal prison in Lompoc, Cal. Respondents Robert Mills and Richard Pierce were convicted of a later murder of another inmate at the same institution. Prison officials placed each respondent in administrative detention shortly after the murders, and they remained there for an extended period of time before they were eventually indicted on criminal charges. On appeal of respondents’ convictions, the en banc Court of Appeals for the Ninth Circuit held by divided vote that they had a Sixth Amendment right to an attorney during the period in which they were held in administrative detention before the return of indictments against them, and that because they had been denied that right, their convictions had to be overturned and their indictments dismissed. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d 1116</a></span> (1983). We granted cer-tiorari to review the Court of Appeals’ novel application of our Sixth Amendment precedents, <span class="citation multiple-matches"><a href="/c/U.%20S./464/913/">464 U. S. 913</a></span> (1983), and we now reverse.</p>
<p id="b240-7">On November 11, 1978, Thomas Trejo, an inmate at the Federal Correctional Institution in Lompoc, Cal., was found dead from 45 stab wounds in the chest. Prison officials and agents from the Federal Bureau of Investigation began inde<page-number citation-index="1" label="183">*183</page-number>pendent investigations of the murder. Prison officials immediately suspected respondents Reynoso and Gouveia and placed them in the Administrative Detention Unit (ADU) at Lompoc. They were released back into the general prison population on November 22, 1978, but after officials obtained further information about the murder, on December 4, 1978, they returned Reynoso and Gouveia to the ADU, and placed respondents Segura and Ramirez in the ADU as well. Later in December, prison officials held disciplinary hearings, determined that all four respondents had participated in the murder of inmate Trejo, and ordered their continued confinement in the ADU. While in the ADU, respondents were separated from the general prison population and confined to individual cells. Although their participation in various prison programs was curtailed, they were still allowed regular visitation rights, exercise periods, access to legal materials, and unmonitored phone calls. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1118" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d, at 1118</a></span>; see generally <span class="citation no-link">28 CFR §§541.19</span>, 541.20(d) (1983). Respondents remained in the ADU without appointed counsel for approximately 19 months. On June 17, 1980, a federal grand jury returned an indictment against respondents on charges of first-degree murder and conspiracy to commit murder in violation of <span class="citation no-link">18 U. S. C. §§1111</span> and 1117 respectively. On July 14, 1980, respondents were arraigned in federal court, at which time a Federal Magistrate appointed counsel for them.</p>
<p id="b241-5">Before trial respondents filed a motion to dismiss their indictments, arguing that the delay of approximately 19 months between the commission of the crime and the return of the indictments violated their due process rights under the Fifth Amendment or, alternatively, their Sixth Amendment right to a speedy trial, and that their confinement in the ADU without appointment of counsel during that period violated their Sixth Amendment right to counsel. The District Court for the Central District of California denied their motion, and respondents proceeded to trial. Their first trial, which lasted approximately four weeks, ended in a mistrial. On retrial, respondents were convicted on both counts and <page-number citation-index="1" label="184">*184</page-number>were sentenced to consecutive life and 99-year terms of imprisonment.</p>
<p id="b242-5">The scenario is much the same in the case of Mills and Pierce. Inmate Thomas Hall was stabbed to death at Lom-poc on August 22, 1979. Immediately afterwards Mills and Pierce were examined by a prison doctor and questioned by FBI agents regarding the murder. Prison officials suspected them of involvement in the murder and placed them in the ADU pending further investigation. On September 13, 1979, prison officials conducted a disciplinary hearing, concluded that respondents had murdered inmate Hall, and ordered their continued confinement in the ADU where they remained for the next eight months. On March 27, 1980, a federal grand jury returned an indictment against Mills and Pierce on charges of first-degree murder in violation of <span class="citation no-link">18 U. S. C. §1111</span> and of conveyance of a weapon in prison in violation of <span class="citation no-link">18 U. S. C. § 1792</span>, and against Pierce on a charge of assault in violation of <span class="citation no-link">18 U. S. C. § 113</span>(c). At the time of their arraignment on April 21, 1980, Mills and Pierce were appointed counsel and were released from the ADU.</p>
<p id="b242-6">Before trial Mills and Pierce also filed a motion to dismiss their indictments, alleging that the 8-month preindictment delay violated their Fifth Amendment due process rights and their Sixth Amendment speedy trial right, and that their confinement without counsel for that period violated their Sixth Amendment right to counsel. The District Court for the Central District of California granted the motion to dismiss. A panel of the Court of Appeals for the Ninth Circuit reversed and remanded for trial, holding that respondents’ Sixth Amendment rights were not triggered during their administrative segregation because they had not yet been arrested and accused, and that respondents had made an insufficient showing of actual prejudice from the preindictment delay so as to justify dismissal of the indictments on due process grounds. <em>United States </em>v. <em>Mills, </em><span class="citation" data-id="9467607"><a href="/opinion/387309/united-states-v-robert-eugene-mills-and-richard-raymond-pierce/" aria-description="Citation for case: United States v. Robert Eugene Mills and Richard Raymond...">641 F. 2d 785</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./454/902/">454 U. S. 902</a></span> (1981). Respondents Mills and <page-number citation-index="1" label="185">*185</page-number>Pierce were then convicted on all counts and sentenced to life imprisonment.</p>
<p id="b243-5">The Court of Appeals, proceeding en banc, consolidated the appeals of all six respondents and addressed only the issue of whether the Sixth Amendment requires the appointment of counsel before indictment for indigent inmates confined in administrative detention while being investigated for criminal activities. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1119" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d, at 1119</a></span>.<footnotemark>1</footnotemark> The Court of Appeals majority recognized that a plurality of this Court had concluded in <em>Kirby </em>v. <em>Illinois, </em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682</a></span> (1972), that the Sixth Amendment right to counsel attaches only when formal judicial proceedings are initiated against an individual by way of indictment, information, arraignment, or preliminary hearing. The majority recognized that no such proceedings had been initiated against respondents during the period of time for which they asserted a right to appointed counsel in this case.</p>
<p id="b243-6">The majority went on to note, however, that <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span> </em>is not a prison case and that the point at which the Sixth Amendment right to counsel is triggered is different in the prosecution of prison crimes. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1120" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d, at 1120</a></span>. In so holding the majority analogized to Sixth Amendment speedy trial cases, where this Court has held that the Sixth Amendment speedy trial right is triggered when an individual is arrested and held to <page-number citation-index="1" label="186">*186</page-number>answer criminal charges. See <em>United States </em>v. <em>Marion, </em><span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#320" aria-description="Citation for case: United States v. Marion">404 U. S. 307, 320</a></span> (1971). The en banc majority reasoned that just as such an arrest constitutes an “accusation” for Sixth Amendment speedy trial purposes, the administrative detention of an inmate for more than 90 days because of a pending felony investigation constitutes an “accusation” for Sixth Amendment right to counsel purposes.<footnotemark>2</footnotemark> Thus, according to the Court of Appeals’ holding, an indigent inmate isolated in administrative detention while the subject of a felony investigation must be afforded counsel after 90 days, or else be released back into the prison population, in order to ensure that he or his lawyer will be able to take preindictment investigatory steps to preserve his defense at trial. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1124" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d, at 1124</a></span>.</p>
<p id="b244-5">Applying its test to the facts of this case, the Court of Appeals majority held that each respondent had been denied his Sixth Amendment right to counsel. It concluded that the record showed that each respondent had been held in administrative detention longer than 90 days, that each had been held at least in part because of a pending felony investigation,<footnotemark>3</footnotemark> and that each had requested and had been denied counsel during his confinement in the ADU. The majority went on to conclude that the appropriate remedy for redressing <page-number citation-index="1" label="187">*187</page-number>the Sixth Amendment violations in this case was reversal of respondents’ convictions and dismissal of the indictments against them.<footnotemark>4</footnotemark></p>
<p id="b245-5">Five judges dissented from the en banc majority’s Sixth Amendment holding. Relying on <em>Kirby </em>v. <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Illinois, supra,</a></span> </em>the dissent concluded that the Sixth Amendment right to counsel is triggered by the initiation of formal criminal proceedings even in the prison context, and that the majority’s conclusion to the contrary shows a misunderstanding of the purpose of the counsel guarantee. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1127" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d, at 1127-1129</a></span>. We agree with the dissenting judges’ application of our precedents to this situation, and, accordingly, we reverse the en banc majority’s holding that respondents had a Sixth Amendment right to the appointment of counsel during their preindictment segregation.</p>
<p id="b245-6">The Sixth Amendment guarantees that “[i]n all criminal prosecutions, the accused shall enjoy the right ... to have the Assistance of Counsel for his defence.” As the Court of Appeals majority noted, our cases have long recognized that the right to counsel attaches only at or after the initiation of adversary judicial proceedings against the defendant. In <em>Kirby </em>v. <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Illinois, supra,</a></span> </em>a plurality of the Court summarized our prior cases as follows:</p>
<blockquote id="b245-7">“In a line of constitutional cases in this Court stemming back to the Court’s landmark opinion in <em>Powell </em>v. <em>Alabama, </em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>, it has been firmly established that a person’s Sixth and Fourteenth Amendment right to counsel attaches only at or after the time that adversary judicial proceedings have been initiated against him. See <em>Powell </em>v. <em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">Alabama, supra;</a></span> Johnson </em>v. <em>Zerbst, </em><page-number citation-index="1" label="188">*188</page-number><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span>; <em>Hamilton </em>v. <em>Alabama, </em><span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span>; <em>Gideon </em>v. <em>Wainwright, </em><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>; <em>White </em>v. <em>Maryland, </em><span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span>; <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span>; <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span>; <em>Gilbert </em>v. <em>California, </em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span>; <em>Coleman </em>v. <em>Alabama, </em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span>.</blockquote>
<blockquote id="ApI">. . [Wjhile members of the Court have differed as to the existence of the right to counsel in the contexts of some of the above cases, <em>all </em>of those cases have involved points of time at or after the initiation of adversary judicial criminal proceedings — whether by way of formal charge, preliminary hearing, indictment, information, or arraignment.” <em>Id., </em>at 688-689 (emphasis in original).</blockquote>
<p id="b246-5">The view that the right to counsel does not attach until the initiation of adversary judicial proceedings has been confirmed by this Court in cases subsequent to <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span>. </em>See <em>Estelle </em>v. <em>Smith, </em><span class="citation" data-id="9428322"><a href="/opinion/110474/estelle-v-smith/#469" aria-description="Citation for case: Estelle v. Smith">451 U. S. 454, 469-470</a></span> (1981); <em>Moore </em>v. <em>Illinois, </em><span class="citation" data-id="9427017"><a href="/opinion/109757/moore-v-illinois/#226" aria-description="Citation for case: Moore v. Illinois">434 U. S. 220, 226-227</a></span> (1977); <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#398" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387, 398-399</a></span> (1977); <em>United States </em>v. <em>Mandujano, </em><span class="citation" data-id="9426389"><a href="/opinion/109442/united-states-v-mandujano/#581" aria-description="Citation for case: United States v. Mandujano">425 U. S. 564, 581</a></span> (1976) (opinion of Burger, C. J.).<footnotemark>5</footnotemark></p>
<p id="b246-6">That interpretation of the Sixth Amendment right to counsel is consistent not only with the literal language of the Amendment, which requires the existence of both a “criminal prosecutio[n]” and an “accused,” but also with the purposes which we have recognized that the right to counsel serves. We have recognized that the “core purpose” of the counsel guarantee is to assure aid at trial, “when the accused [is] con<page-number citation-index="1" label="189">*189</page-number>fronted with both the intricacies of the law and the advocacy of the public prosecutor.” <em>United States </em>v. <em>Ash, </em><span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/#309" aria-description="Citation for case: United States v. Ash">413 U. S. 300, 309</a></span> (1973). Indeed the right to counsel</p>
<blockquote id="b247-4">“embodies a realistic recognition of the obvious truth that the average defendant does not have the professional legal skill to protect himself when brought before a tribunal with power to take his life or liberty, wherein the prosecution is presented by experienced and learned counsel.” <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#462" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 462-463</a></span> (1938).</blockquote>
<p id="b247-5">Although we have extended an accused’s right to counsel to certain “critical” pretrial proceedings, <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), we have done so recognizing that at those proceedings, “the accused [is] confronted, just as at trial, by the procedural system, or by his expert adversary, or by both,” <em>United States </em>v. <span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/#310" aria-description="Citation for case: United States v. Ash"><em>Ash, supra, </em>at 310</a></span>, in a situation where the results of the confrontation “might well settle the accused’s fate and reduce the trial itself to a mere formality.” <em>United States </em>v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#224" aria-description="Citation for case: United States v. Wade"><em>Wade, supra, </em>at 224</a></span>.</p>
<p id="b247-6">Thus, given the plain language of the Amendment and its purpose of protecting the unaided layman at critical confrontations with his adversary, our conclusion that the right to counsel attaches at the initiation of adversary judicial criminal proceedings “is far from a mere formalism.” <em>Kirby </em>v. <em>Illinois, </em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S., at 689</a></span>. It is only at that time “that the government has committed itself to prosecute, and only then that the adverse positions of government and defendant have solidified. It is then that a defendant finds himself faced with the prosecutorial forces of organized society, and immersed in the intricacies of substantive and procedural criminal law.” <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Ibid.</a></span></em></p>
<p id="b247-7">The Court of Appeals departed from our consistent interpretation of the Sixth Amendment in these cases, and in so doing, fundamentally misconceived the nature of the right to counsel guarantee. We agree with the dissent that the ma<page-number citation-index="1" label="190">*190</page-number>jority’s analogy to Sixth Amendment speedy trial cases is inapt. Our speedy trial cases hold that that Sixth Amendment right may attach before an indictment and as early as the time of “arrest and holding to answer a criminal charge,” <em>United States </em>v. <em>MacDonald, </em><span class="citation" data-id="9428723"><a href="/opinion/110686/united-states-v-macdonald/#6" aria-description="Citation for case: United States v. MacDonald">456 U. S. 1, 6-7</a></span> (1982); <em>United States </em>v. <em>Lovasco, </em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#788" aria-description="Citation for case: United States v. Lovasco">431 U. S. 783, 788-789</a></span> (1977); <em>Dillingham </em>v. <em>United States, </em><span class="citation" data-id="109331"><a href="/opinion/109331/dillingham-v-united-states/" aria-description="Citation for case: Dillingham v. United States">423 U. S. 64</a></span> (1975) <em>(per curiam); United States </em>v. <em>Marion, </em><span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#320" aria-description="Citation for case: United States v. Marion">404 U. S., at 320</a></span>, but we have never held that the right to counsel attaches at the time of arrest. This difference is readily explainable, given the fact that the speedy trial right and the right to counsel protect different interests. While the right to counsel exists to protect the accused during trial-type confrontations with the prosecutor, the speedy trial right exists primarily to protect an individual’s liberty interest, “to minimize the possibility of lengthy incarceration prior to trial, to reduce the lesser, but nevertheless substantial, impairment of liberty imposed on an accused while released on bail, and to shorten the disruption of life caused by arrest and the presence of unresolved criminal charges.” <em>United States </em>v. <span class="citation" data-id="9428723"><a href="/opinion/110686/united-states-v-macdonald/#8" aria-description="Citation for case: United States v. MacDonald"><em>MacDonald, supra, </em>at 8</a></span>. See <em>Barker </em>v. <em>Wingo, </em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/#532" aria-description="Citation for case: Barker v. Wingo">407 U. S. 514, 532-533</a></span> (1972); <em>United States </em>v. <span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#320" aria-description="Citation for case: United States v. Marion"><em>Marion, supra, </em>at 320</a></span>. Thus, the majority’s attempt to draw an analogy between an arrest and an inmate’s administrative detention pending investigation may have some relevance in analyzing when the speedy trial right attaches in this context, but it is not relevant to a proper determination of when the right to counsel attaches.<footnotemark>6</footnotemark></p>
<p id="b249-4"><page-number citation-index="1" label="191">*191</page-number>The Court of Appeals’ holding also confuses the purpose of the right to counsel with purposes that are served by the Fifth Amendment due process guarantee and the statutes of limitations applicable to the particular crime being investigated. The majority concludes that the extension of the right to counsel to this prison context is necessary to protect against the possibility that the Government may delay the initiation of formal charges, thus delaying the appointment of counsel, while it develops its case against the isolated and unaided inmate. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1122" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d, at 1122</a></span>. By the time the Government decides to bring charges, the majority felt, witnesses’ memories could have dimmed, alibi witnesses could have been transferred to other facilities, and physical evidence could have deteriorated. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1126" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip..."><em>Id., </em>at 1126</a></span>.</p>
<p id="b249-5">Those concerns, while certainly legitimate ones, are simply not concerns implicating the right to counsel, and we reaffirm that the mere “possibility of prejudice [to a defendant resulting from the passage of time] ... is not itself sufficient reason to wrench the Sixth Amendment from its proper context.” <em>United States </em>v. <span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#321" aria-description="Citation for case: United States v. Marion"><em>Marion, supra, </em>at 321-322</a></span>. In holding that the appointment of counsel or the release of the inmate from segregation could remedy its concerns, the Court of Appeals must have concluded, quite illogically we believe, that the presence of the inmate in the general prison population or the appointment of a lawyer could somehow prevent the deterioration of physical evidence, or that the inmate or his counsel could begin an effective investigation of the crime within the restricted prison walls before even being able to discover the nature of the Government’s case. Of course, both inside and outside the prison, it may well be true that in some cases preindictment investigation could help a defendant prepare a better defense. But, as we have noted, our cases have never suggested that the purpose of the right to counsel is to provide a defendant with a preindictment private investigator, and we see no reason to adopt that novel interpretation of the right to counsel in this case.</p>
<p id="b250-4"><page-number citation-index="1" label="192">*192</page-number>Thus, at bottom, the majority’s concern is that because an inmáte suspected of a crime is already in prison, the prosecution may have little incentive promptly to bring formal charges against him, and that the resulting preindictment delay may be particularly prejudicial to the inmate, given the problems inherent in investigating prison crimes, such as the transient nature of the prison population and the general reluctance of inmates to cooperate. But applicable statutes of limitations protect against the prosecution’s bringing stale criminal charges against any defendant, <em>United States </em>v. <span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#788" aria-description="Citation for case: United States v. Lovasco"><em>Lovasco, supra, </em>at 788-789</a></span>; <em>United States </em>v. <span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#322" aria-description="Citation for case: United States v. Marion"><em>Marion, supra, </em>at 322</a></span>, and, beyond that protection, the Fifth Amendment requires the dismissal of an indictment, even if it is brought within the statute of limitations, if the defendant can prove that the Government’s delay in bringing the indictment was a deliberate device to gain an advantage over him and that it caused him actual prejudice in presenting his defense. <em>United States </em>v. <span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#789" aria-description="Citation for case: United States v. Lovasco"><em>Lovasco, supra, </em>at 789-790</a></span>; <em>United States </em>v. <span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#324" aria-description="Citation for case: United States v. Marion"><em>Marion, supra, </em>at 324</a></span>.<footnotemark>7</footnotemark> Those protections apply to criminal defendants within and without the prison walls, and we decline to depart from our traditional interpretation of the Sixth Amendment right to counsel in order to provide additional protections for respondents here.</p>
<p id="b250-5">We conclude that the Court of Appeals was wrong in holding that respondents were constitutionally entitled to the appointment of counsel while they were in administrative segregation and before any adversary judicial proceedings had been initiated against them. Accordingly, we reverse <page-number citation-index="1" label="193">*193</page-number>the judgment of the Court of Appeals and remand for further proceedings consistent with this opinion.</p>
<p id="b251-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b243-7"> The narrow issue before the Court of Appeals and before us today is whether the Sixth Amendment requires the appointment of counsel for indigent inmates in respondents’ situation. Respondents have not contended that they were denied the opportunity to retain their own private counsel while they were in administrative segregation. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1119" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d, at 1119</a></span>. As the Court of Appeals noted, respondents had visitation privileges and the opportunity to make unmonitored phone calls to attorneys while in the ADU. <em><span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">Ibid.</a></span> </em>See <span class="citation no-link">28 CFR §§ 541.19</span>(c)(10), 541.20(d) (1983). Respondents also have not asserted a Sixth Amendment ineffective-assistance-of-counsel claim nor have they questioned our holding in <em>Wolff </em>v. <em>McDonnell, </em><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#570" aria-description="Citation for case: Wolff v. McDonnell">418 U. S. 539, 570</a></span> (1974), that inmates have no right to retained or appointed counsel at prison disciplinary proceedings. See <em>Baxter </em>v. <em>Palmigiano, </em><span class="citation" data-id="9426363"><a href="/opinion/109429/baxter-v-palmigiano/#315" aria-description="Citation for case: Baxter v. Palmigiano">425 U. S. 308, 315</a></span> (1976).</p>
</footnote>
<footnote label="2">
<p id="b244-6"> The majority arrived at the 90-day figure based on its own interpretation of the current federal prison regulations as allowing detention for up to 90 days for disciplinary reasons. See <span class="citation no-link">28 CFR § 641.20</span>(c) (1983).</p>
</footnote>
<footnote label="3">
<p id="b244-7"> Relying on his interpretation of current prison regulations, the Solicitor General vehemently argues that, whatever additional reasons legitimately may have contributed to the decision to confine respondents in the ADU, the primary reason for their confinement was to ensure the security of the institution. Thus he argues that that security-related detention cannot be equated with an arrest or accusation for Sixth Amendment purposes. Brief for United States 23-27; Tr. of Oral Arg. 9-12. But our holding today makes the reason for the detention irrelevant for purposes of the only issue before us, the point at which the Sixth Amendment right to counsel is triggered. Respondents have not challenged “the legitimacy of administrative detention in general or its appropriateness” in their particular cases. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1121" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d, at 1121</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b245-8"> The Solicitor General argues here that dismissal of the indictments is an inappropriate remedy absent a showing of actual and specific prejudice to respondents and that they have not made that showing in this case. Brief for United States 44-60. Given our holding on the substantive Sixth Amendment issue, however, we have no occasion to address the remedy question.</p>
</footnote>
<footnote label="5">
<p id="b246-7"> The only arguable deviations from that consistent line of cases are <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964). Although there may be some language to the contrary in <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), we have made clear that we required counsel in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>in order to protect the Fifth Amendment privilege against self-incrimination rather than to vindicate the Sixth Amendment right to counsel. See <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#300" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 300, n. 4</a></span> (1980); <em>Kirby </em>v. <em>Illinois, </em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S., at 689</a></span>; <em>Johnson </em>v. <em>New Jersey, </em><span class="citation multiple-matches"><a href="/c/U.%20S./384/719/">384 U. S. 719</a></span>, 729-730 (1966).</p>
</footnote>
<footnote label="6">
<p id="b248-5"> Of course we express no view as to when the Sixth Amendment speedy-trial right attaches in this context because that issue is not before us. The Court of Appeals for the Ninth Circuit, like several other Circuits, see, <em>e. g., United States </em>v. <em>Daniels, </em><span class="citation no-link">698 P. 2d 221</span>, 223 (CA4 1983); <em>United States </em>v. <em>Blevins, </em><span class="citation" data-id="363882"><a href="/opinion/363882/united-states-v-ralph-blevins/#647" aria-description="Citation for case: United States v. Ralph Blevins">593 F. 2d 646, 647</a></span> (CA5 1979) <em>(per curiam), </em>however, has held that the segregation of an inmate from the general population pending criminal charges does not constitute an “arrest” for purposes of the speedy trial right. <em>United States </em>v. <em>Clardy, </em><span class="citation" data-id="338481"><a href="/opinion/338481/united-states-v-harry-clardy-united-states-of-america-v-phillip-alfonso/#441" aria-description="Citation for case: United States v. Harry Clardy, United States of America...">540 F. 2d 439, 441</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/963/">429 U. S. 963</a></span> (1976). Given its own <em><span class="citation" data-id="338481"><a href="/opinion/338481/united-states-v-harry-clardy-united-states-of-america-v-phillip-alfonso/" aria-description="Citation for case: United States v. Harry Clardy, United States of America...">Clardy</a></span> </em>holding, the Court of Appeals’ analogy here seems somewhat strained.</p>
</footnote>
<footnote label="7">
<p id="b250-6"> We have of course rejected the arguments that prosecutors are constitutionally obligated to file charges against a suspect as soon as they have probable cause but before they believe that they can establish guilt beyond a reasonable doubt, <em>United States </em>v. <em>Lovasco, </em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#791" aria-description="Citation for case: United States v. Lovasco">431 U. S., at 791</a></span>, and that prosecutors must file charges as soon as they marshal enough evidence to prove guilt beyond a reasonable doubt but before their investigations are complete. <span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#792" aria-description="Citation for case: United States v. Lovasco"><em>Id., </em>at 792-795</a></span>.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Grubbs.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Grubbs"
type: case
citation: "547 U.S. 90 (2006)"
parallel_cite: "126 S. Ct. 1494; 164 L. Ed. 2d 195"
neutral_cite: 2006 U.S. LEXIS 2496
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2006
date_decided: 2006-03-21
docket: 04-1414
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2006-03-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Grubbs
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145670/united-states-v-grubbs/"
  cluster_id: 145670
  opinion_id: 145670
  identity_checked: true
homes:
  - page: "[[Probable Cause in the Affidavit]]"
    role: "Key — Progeny / Refinement"
related: ["[[Illinois v. Gates]]", "[[Groh v. Ramirez]]", "[[Massachusetts v. Sheppard]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant-requirement", "anticipatory-warrant", "triggering-condition", "particularity"]
holding: "**Anticipatory warrants** — warrants that take effect only upon a future 'triggering condition' — are not categorically…"
lake:
  record_id: United States v. Grubbs
  status: verified
  projected_at: 2026-07-09
---

# United States v. Grubbs

*547 U.S. 90 (2006)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Jeffrey Grubbs bought a child-pornography videotape from a website run by an undercover postal inspector. Officers arranged a controlled delivery to his home and obtained a search warrant supported by an affidavit stating the warrant would be executed only after the package was "received by a person(s) and has been physically taken into the residence." The package was delivered, Grubbs' wife took it inside, and officers executed the warrant. The Ninth Circuit invalidated the warrant because the triggering condition appeared only in the affidavit, not on the face of the warrant.

## Issue
(1) Whether anticipatory search warrants are categorically unconstitutional under the Fourth Amendment's probable-cause requirement; and (2) whether the Fourth Amendment requires the triggering condition to be set forth in the warrant itself.

## Rule
No to both. An anticipatory warrant — one "based upon an affidavit showing probable cause that at some future time (but not presently) certain evidence of crime will be located at a specified place" — is constitutional. "Anticipatory warrants are, therefore, no different in principle from ordinary warrants. They require the magistrate to determine (1) that it is *now probable* that (2) contraband, evidence of a crime, or a fugitive *will be* on the described premises (3) when the warrant is executed." — 547 U.S. at 96. ^pin-96

For a conditioned anticipatory warrant, "two prerequisites of probability must be satisfied": it must be probable both that the triggering condition will occur and that, if it does, the object of the search will be found at the place. — [*Id.* at 96–97](https://www.courtlistener.com/opinion/145670/united-states-v-grubbs/#:~:text=two%20prerequisites%20of%20probability%20must). ^pin-96a

The triggering condition need not appear on the warrant: "Because the Fourth Amendment does not require that the triggering condition for an anticipatory search warrant be set forth in the warrant itself, the Court of Appeals erred in invalidating the warrant at issue here." — [*Id.* at 99](https://www.courtlistener.com/opinion/145670/united-states-v-grubbs/#:~:text=Because%20the%20Fourth%20Amendment%20does). ^pin-99

## Application
On these facts the warrant was valid. The affidavit's triggering condition — controlled delivery and movement of the package into the residence — established that it was then probable both that the delivery would occur and that, once it did, the contraband would be in the home; the supporting probable cause therefore existed when the warrant issued. The Court rejected Grubbs' [[Particularity|particularity]] argument: the Fourth Amendment's [[Particularity|particularity]] requirement reaches only the place to be searched and the persons or things to be seized, and "does not include the conditions precedent to execution of the warrant." Because probable cause itself — "the quintessential 'precondition to the valid exercise of executive power'" — need not be recited on the warrant, neither must the triggering condition. The controlled delivery satisfied the condition, and the search was lawful.

## Conclusion
Anticipatory warrants are constitutional, and the triggering condition need not be stated on the warrant's face; the Ninth Circuit's judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Grubbs* applies the totality probable-cause standard of [[Illinois v. Gates]] to anticipatory warrants and distinguishes the [[Particularity|particularity]] defect of [[Groh v. Ramirez]] (which concerned the place/things-to-be-seized [[Particularity|particularity]] that the Fourth Amendment's text *does* require).

## Appears on
- [[Probable Cause in the Affidavit]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Grubbs*, 547 U.S. 90 (2006) — https://www.courtlistener.com/opinion/145670/united-states-v-grubbs/ — pinpoints: 96, 99.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "db6cdbc962718b7b", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "547 U.S. 90 (2006)", "court": "U.S. Supreme Court", "neutral_cite": "2006 U.S. LEXIS 2496", "official_citation_present": true, "parallel_cite": "126 S. Ct. 1494; 164 L. Ed. 2d 195", "title": "United States v. Grubbs", "year": "2006"}}
{"assertion_id": "0d7182757de5d7d9", "dimension": "support", "kind": "home_role", "locator": {"home": "Probable Cause in the Affidavit"}, "payload": {"home": "Probable Cause in the Affidavit", "role": "Key — Progeny / Refinement", "title": "United States v. Grubbs"}}
{"assertion_id": "6adde3f70a3f0855", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "**Anticipatory warrants** — warrants that take effect only upon a future 'triggering condition' — are not categorically…", "title": "United States v. Grubbs"}}
{"assertion_id": "495eebdc5752da00", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2006-03-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Grubbs", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Grubbs", "varies_by_point": "false"}}
{"assertion_id": "9e1fa5c37b46bc54", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Grubbs"}}
```

### lake record — United States v. Grubbs

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Grubbs",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Grubbs",
    "case_name_short": "Grubbs",
    "case_name_full": "United States v. Grubbs",
    "input_case_name": "United States v. Grubbs",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2006-03-21",
    "year": 2006,
    "docket": "04-1414",
    "cluster_id": 145670,
    "lead_opinion_id": 145670,
    "sibling_ids": [
      145670,
      9434968,
      9434969
    ],
    "absolute_url": "/opinion/145670/united-states-v-grubbs/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "547 U.S. 90",
      "volume": "547",
      "reporter": "U.S.",
      "page": "90",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "126 S. Ct. 1494",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "1494",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "164 L. Ed. 2d 195",
        "volume": "164",
        "reporter": "L. Ed. 2d",
        "page": "195",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2006 U.S. LEXIS 2496",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "2496",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "547 U.S. 90",
        "volume": "547",
        "reporter": "U.S.",
        "page": "90",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "126 S. Ct. 1494",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "1494",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "164 L. Ed. 2d 195",
        "volume": "164",
        "reporter": "L. Ed. 2d",
        "page": "195",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2006 U.S. LEXIS 2496",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "2496",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "547 U.S. 90",
    "official_selection": {
      "court_class": "scotus",
      "selected": "547 U.S. 90",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-96",
      "page": null,
      "quote": "The package was delivered, Grubbs' wife took it inside, and officers executed the warrant. The Ninth Circuit invalidated the warrant because the triggering condition appeared only in the affidavit, not on the face of the warrant. ## Issue (1) Whether anticipatory search warrants are categorically unconstitutional under the Fourth Amendment's probable-cause requirement; and (2) whether the Fourth Amendment requires the triggering condition to be set forth in the warrant itself. ## Rule No to both. An anticipatory warrant \u2014 one",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-96a",
      "page": null,
      "quote": "two prerequisites of probability must be satisfied",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 15892,
      "fragment": "#:~:text=two%20prerequisites%20of%20probability%20must",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-99",
      "page": null,
      "quote": "Because the Fourth Amendment does not require that the triggering condition for an anticipatory search warrant be set forth in the warrant itself, the Court of Appeals erred in invalidating the warrant at issue here.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 21470,
      "fragment": "#:~:text=Because%20the%20Fourth%20Amendment%20does",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2006-03-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Grubbs",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Harte v. Board Comm'rs Cnty of Johnson",
          "cluster_id": 4411980,
          "cite": [
            "864 F.3d 1154",
            "2017 WL 3138494"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wheeler v. State",
          "cluster_id": 3182294,
          "cite": [
            "135 A.3d 282",
            "2016 Del. LEXIS 121",
            "2016 WL 825395"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane1_negative"
      },
      {
        "citing_case": {
          "name": "381 Search Warrants Directed to Facebook, Inc. v. New York County Dist. Attorney's Off.",
          "cluster_id": 2818762,
          "cite": [
            "132 A.D.3d 11",
            "14 N.Y.S.3d 23"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Wright",
          "cluster_id": 2777610,
          "cite": [
            "777 F.3d 635",
            "2015 WL 507169",
            "2015 U.S. App. LEXIS 1939"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane1_negative"
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
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mink v. Knox",
          "cluster_id": 158328,
          "cite": [
            "613 F.3d 995",
            "38 Media L. Rep. (BNA) 1961",
            "2010 U.S. App. LEXIS 14684",
            "2010 WL 2802729"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kasten v. Saint-Gobain Performance Plastics Corp.",
          "cluster_id": 212970,
          "cite": [
            "179 L. Ed. 2d 379",
            "131 S. Ct. 1325",
            "563 U.S. 1",
            "2011 U.S. LEXIS 2417"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Wallace",
          "cluster_id": 2303175,
          "cite": [
            "42 A.3d 1040",
            "615 Pa. 395",
            "2012 WL 1434885",
            "2012 Pa. LEXIS 981"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. Com.",
          "cluster_id": 1058401,
          "cite": [
            "670 S.E.2d 727",
            "277 Va. 171",
            "2009 Va. LEXIS 10"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillip C. BAY, S/K/A Philip C. Bay v. COMMONWEALTH of Virginia",
          "cluster_id": 1061627,
          "cite": [
            "60 Va. App. 520",
            "729 S.E.2d 768",
            "2012 WL 3165070",
            "2012 Va. App. LEXIS 254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin McClain George Brandt, III Jason Davis",
          "cluster_id": 793976,
          "cite": [
            "444 F.3d 556",
            "2006 U.S. App. LEXIS 32292"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hurwitz",
          "cluster_id": 2968341,
          "cite": [
            "459 F.3d 463",
            "2006 WL 2414056"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Unus v. Kane",
          "cluster_id": 1028751,
          "cite": [
            "565 F.3d 103",
            "2009 U.S. App. LEXIS 9955",
            "2009 WL 1219679"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sisson v. State",
          "cluster_id": 1443990,
          "cite": [
            "903 A.2d 288",
            "2006 Del. LEXIS 326",
            "2006 WL 1699480"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tracey",
          "cluster_id": 62,
          "cite": [
            "597 F.3d 140",
            "2010 U.S. App. LEXIS 4204",
            "2010 WL 681364"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Jesus Angel Ramirez",
          "cluster_id": 4394389,
          "cite": [
            "895 N.W.2d 884",
            "2017 WL 2291388",
            "2017 Iowa Sup. LEXIS 57"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Christopher George Storm",
          "cluster_id": 4405282,
          "cite": [
            "898 N.W.2d 140",
            "2017 WL 2822483",
            "2017 Iowa Sup. LEXIS 81"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Clark",
          "cluster_id": 206195,
          "cite": [
            "638 F.3d 89",
            "2011 U.S. App. LEXIS 4506",
            "2011 WL 781597"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. SDI Future Health, Inc.",
          "cluster_id": 1459636,
          "cite": [
            "568 F.3d 684",
            "103 A.F.T.R.2d (RIA) 2436",
            "2009 U.S. App. LEXIS 13003",
            "2009 WL 1508763"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hurwitz",
          "cluster_id": 795366,
          "cite": [
            "459 F.3d 463",
            "2006 U.S. App. LEXIS 21425"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Keller",
          "cluster_id": 842342,
          "cite": [
            "739 N.W.2d 505",
            "479 Mich. 467"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scott",
          "cluster_id": 150069,
          "cite": [
            "610 F.3d 1009",
            "2010 U.S. App. LEXIS 13683",
            "2010 WL 2650709"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lyman Wagers",
          "cluster_id": 794753,
          "cite": [
            "452 F.3d 534",
            "2006 U.S. App. LEXIS 16070",
            "2006 WL 1735574"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rosa",
          "cluster_id": 178085,
          "cite": [
            "626 F.3d 56",
            "2010 U.S. App. LEXIS 22099",
            "2010 WL 4227428"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bowling v. Rector",
          "cluster_id": 172792,
          "cite": [
            "584 F.3d 956",
            "2009 U.S. App. LEXIS 23542",
            "2009 WL 3416342"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Penney",
          "cluster_id": 1188924,
          "cite": [
            "576 F.3d 297",
            "80 Fed. R. Serv. 590",
            "2009 U.S. App. LEXIS 17595",
            "2009 WL 2408721"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Spencer",
          "cluster_id": 187217,
          "cite": [
            "530 F.3d 1003",
            "382 U.S. App. D.C. 90",
            "2008 U.S. App. LEXIS 14713",
            "2008 WL 2697191"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 2281341,
          "cite": [
            "338 S.W.3d 725",
            "2011 Tex. App. LEXIS 4300",
            "2011 WL 1448147"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145670 OR 9434968 OR 9434969) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 178,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 178,
        "triage_read": 4,
        "triage_snippet_classified": 174
      },
      "lane2_top_cited": {
        "query": "cites:(145670 OR 9434968 OR 9434969)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MCZzPTI2NjkxNTImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145670+OR+9434968+OR+9434969%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145670 OR 9434968 OR 9434969)",
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
    "complete_query": "cites:(145670 OR 9434968 OR 9434969)",
    "indexed_citing_opinions": 245,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145670,
        "count": 199,
        "count_source": "search"
      },
      {
        "opinion_id": 9434968,
        "count": 55,
        "count_source": "search"
      },
      {
        "opinion_id": 9434969,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 430,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-grubbs.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0MDkxMDYmcz05NDIxNDM5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28145670+OR+9434968+OR+9434969%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145670,
        "cited_id": 101970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 110061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 111263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 131161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 355709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 527795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 539861,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 602842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 610895,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 754298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 764737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 766120,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 778595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 787181,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 788436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 799975,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LCU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T00:15:29Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:15:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:15:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:22:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:15:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Grubbs

```
(Slip Opinion)              OCTOBER TERM, 2005                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                    UNITED STATES v. GRUBBS

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE NINTH CIRCUIT

   No. 04–1414. Argued January 18, 2006—Decided March 21, 2006
A Magistrate Judge issued an “anticipatory” search warrant for re-
  spondent Grubbs’ house based on a federal officer’s affidavit. The af-
  fidavit explained that the warrant would not be executed until a par-
  cel containing a videotape of child pornography—which Grubbs had
  ordered from an undercover postal inspector—was received at, and
  physically taken into, the residence. The affidavit also referred to
  two attachments describing the residence and the items to be seized.
  After the package was delivered and the search commenced, Grubbs
  was given a copy of the warrant, which included the attachments but
  not the supporting affidavit. When he admitted ordering the video-
  tape, he was arrested, and the videotape and other items were seized.
  Following his indictment for receiving child pornography, see 18
  U. S. C. §2252(a)(2), Grubbs moved to suppress the seized evidence,
  arguing, inter alia, that the warrant was invalid because it failed to
  list the triggering condition. The District Court denied the motion,
  and Grubbs pleaded guilty. The Ninth Circuit reversed, concluding
  that the warrant ran afoul of the Fourth Amendment’s particularity
  requirement, which, under Circuit precedent, applied to the condi-
  tions precedent to an anticipatory warrant.
Held:
    1. Anticipatory warrants are not categorically unconstitutional un-
 der the Fourth Amendment’s provision that “no Warrants shall issue,
 but upon probable cause.” Probable cause exists when “there is a fair
 probability that contraband or evidence of a crime will be found in a
 particular place.” Illinois v. Gates, 462 U. S. 213, 238. When an an-
 ticipatory warrant is issued, the fact that the contraband is not pres-
 ently at the place described is immaterial, so long as there is prob-
 able cause to believe it will be there when the warrant is executed.
2                      UNITED STATES v. GRUBBS

                                  Syllabus

    Anticipatory warrants are, therefore, no different in principle from
    ordinary warrants: They require the magistrate to determine (1) that
    it is now probable that (2) contraband, evidence of a crime, or a fugi-
    tive will be on the described premises (3) when the warrant is exe-
    cuted. Where the anticipatory warrant places a condition (other than
    the mere passage of time) upon its execution, the first of these deter-
    minations goes not merely to what will probably be found if the con-
    dition is met, but also to the likelihood that the condition will be met,
    and thus that a proper object of seizure will be on the described
    premises.      Here, the occurrence of the triggering condition—
    successful delivery of the videotape—would plainly establish probable
    cause for the search, and the affidavit established probable cause to
    believe the triggering condition would be satisfied. Pp. 3–7.
       2. The warrant at issue did not violate the Fourth Amendment’s
    particularity requirement. The Amendment specifies only two mat-
    ters that the warrant must “particularly describ[e]”: “the place to be
    searched” and “the persons or things to be seized.” That language is
    decisive here; the particularity requirement does not include the con-
    ditions precedent to execution of the warrant. Cf. Dalia v. United
    States, 441 U. S. 238, 255, 257. Respondent’s two policy rationales—
    that setting forth the triggering condition in the warrant itself is nec-
    essary (1) to delineate the limits of the executing officer’s power and
    (2) to allow the individual whose property is searched or seized to po-
    lice the officer’s conduct—find no basis in either the Fourth Amend-
    ment or Federal Rule of Criminal Procedure 41. Pp. 7–9.
377 F. 3d 1072 and 389 F. 3d 1306, reversed and remanded.

  SCALIA, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and KENNEDY, THOMAS, and BREYER, JJ., joined, and in which
STEVENS, SOUTER, and GINSBURG, J., joined as to Parts I and II.
SOUTER, J., filed an opinion concurring in part and concurring in the
judgment, in which STEVENS and GINSBURG, JJ., joined. ALITO, J., took
no part in the consideration or decision of the case.
                       Cite as: 547 U. S. ____ (2006)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of thfe United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash-
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 04–1414
                                  _________________


UNITED STATES, PETITIONER v. JEFFREY GRUBBS
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE NINTH CIRCUIT
                               [March 21, 2006]

  JUSTICE SCALIA delivered the opinion of the Court.
  Federal law enforcement officers obtained a search
warrant for respondent’s house on the basis of an affidavit
explaining that the warrant would be executed only after a
controlled delivery of contraband to that location. We
address two challenges to the constitutionality of this
anticipatory warrant.
                              I
  Respondent Jeffrey Grubbs purchased a videotape
containing child pornography from a Web site operated by
an undercover postal inspector. Officers from the Postal
Inspection Service arranged a controlled delivery of a
package containing the videotape to Grubbs’ residence. A
postal inspector submitted a search warrant application to
a Magistrate Judge for the Eastern District of California,
accompanied by an affidavit describing the proposed op-
eration in detail. The affidavit stated:
    “Execution of this search warrant will not occur
    unless and until the parcel has been received by a
    person(s) and has been physically taken into the resi-
    dence . . . . At that time, and not before, this search
    warrant will be executed by me and other United
2               UNITED STATES v. GRUBBS

                     Opinion of the Court

    States Postal inspectors, with appropriate assistance
    from other law enforcement officers in accordance
    with this warrant’s command.” App. to Pet. for Cert.
    72a.
In addition to describing this triggering condition, the
affidavit referred to two attachments, which described
Grubbs’ residence and the items officers would seize.
These attachments, but not the body of the affidavit, were
incorporated into the requested warrant. The affidavit
concluded:
    “Based upon the foregoing facts, I respectfully submit
    there exists probable cause to believe that the items
    set forth in Attachment B to this affidavit and the
    search warrant, will be found [at Grubbs’ residence],
    which residence is further described at Attachment
    A.” Ibid.
  The Magistrate Judge issued the warrant as requested.
Two days later, an undercover postal inspector delivered
the package. Grubbs’ wife signed for it and took the un-
opened package inside. The inspectors detained Grubbs as
he left his home a few minutes later, then entered the
house and commenced the search. Roughly 30 minutes
into the search, Grubbs was provided with a copy of the
warrant, which included both attachments but not the
supporting affidavit that explained when the warrant
would be executed. Grubbs consented to interrogation by
the postal inspectors and admitted ordering the videotape.
He was placed under arrest, and various items were
seized, including the videotape.
  A grand jury for the Eastern District of California in-
dicted Grubbs on one count of receiving a visual depiction
of a minor engaged in sexually explicit conduct. See 18
U. S. C. §2252(a)(2). He moved to suppress the evidence
seized during the search of his residence, arguing as rele-
vant here that the warrant was invalid because it failed to
                      Cite as: 547 U. S. ____ (2006)                     3

                          Opinion of the Court

list the triggering condition. After an evidentiary hearing,
the District Court denied the motion. Grubbs pleaded
guilty, but reserved his right to appeal the denial of his
motion to suppress.
   The Court of Appeals for the Ninth Circuit reversed.
377 F. 3d 1072, amended, 389 F. 3d 1306 (2004). Relying
on Circuit precedent, it held that “the particularity re-
quirement of the Fourth Amendment applies with full
force to the conditions precedent to an anticipatory search
warrant.” 377 F. 3d, at 1077–1078 (citing United States v.
Hotal, 143 F. 3d 1223, 1226 (CA9 1998)). An anticipatory
warrant defective for that reason may be “cur[ed]” if the
conditions precedent are set forth in an affidavit that is
incorporated in the warrant and “presented to the person
whose property is being searched.” 377 F. 3d, at 1079.
Because the postal inspectors “failed to present the affida-
vit—the only document in which the triggering conditions
were listed”—to Grubbs or his wife, the “warrant was . . .
inoperative, and the search was illegal.” Ibid. We granted
certiorari. 545 U. S. ___ (2005).
                            II
  Before turning to the Ninth Circuit’s conclusion that the
warrant at issue here ran afoul of the Fourth Amend-
ment’s particularity requirement, we address the antece-
dent question whether anticipatory search warrants are
categorically unconstitutional.1 An anticipatory warrant
is “a warrant based upon an affidavit showing probable
——————
   1 This issue is “predicate to an intelligent resolution of the question

presented.” Ohio v. Robinette, 519 U. S. 33, 38 (1996) (internal quotation
marks omitted). It makes little sense to address what the Fourth
Amendment requires of anticipatory search warrants if it does not
allow them at all. Cf. Wilkinson v. Austin, 545 U. S. ___, ___ (2005) (slip
op., at 9) (addressing whether inmates had a liberty interest in avoiding
assignment to a “Supermax” prison, despite the State’s concession that
they did, because “[w]e need reach the question of what process is due only
if the inmates establish a constitutionally protected liberty interest”).
4                UNITED STATES v. GRUBBS

                      Opinion of the Court

cause that at some future time (but not presently) certain
evidence of crime will be located at a specified place.” 2 W.
LaFave, Search and Seizure §3.7(c), p. 398 (4th ed. 2004).
Most anticipatory warrants subject their execution to
some condition precedent other than the mere passage of
time—a so-called “triggering condition.” The affidavit at
issue here, for instance, explained that “[e]xecution of
th[e] search warrant will not occur unless and until the
parcel [containing child pornography] has been received by
a person(s) and has been physically taken into the resi-
dence.” App. to Pet. for Cert. 72a. If the government were
to execute an anticipatory warrant before the triggering
condition occurred, there would be no reason to believe the
item described in the warrant could be found at the
searched location; by definition, the triggering condition
which establishes probable cause has not yet been satis-
fied when the warrant is issued. Grubbs argues that for
this reason anticipatory warrants contravene the Fourth
Amendment’s provision that “no Warrants shall issue, but
upon probable cause.”
   We reject this view, as has every Court of Appeals to
confront the issue, see, e.g., United States v. Loy, 191 F. 3d
360, 364 (CA3 1999) (collecting cases). Probable cause
exists when “there is a fair probability that contraband or
evidence of a crime will be found in a particular place.”
Illinois v. Gates, 462 U. S. 213, 238 (1983). Because the
probable-cause requirement looks to whether evidence will
be found when the search is conducted, all warrants are, in
a sense, “anticipatory.” In the typical case where the
police seek permission to search a house for an item they
believe is already located there, the magistrate’s determi-
nation that there is probable cause for the search amounts
to a prediction that the item will still be there when the
warrant is executed. See People v. Glen, 30 N. Y. 2d 252,
258, 282 N. E. 2d 614, 617 (1972) (“[P]resent possession is
                     Cite as: 547 U. S. ____ (2006)                     5

                          Opinion of the Court

only probative of the likelihood of future possession.”).2
The anticipatory nature of warrants is even clearer in the
context of electronic surveillance. See, e.g., Katz v. United
States, 389 U. S. 347 (1967). When police request approval
to tap a telephone line, they do so based on the probability
that, during the course of the surveillance, the subject will
use the phone to engage in crime-related conversations.
The relevant federal provision requires a judge authoriz-
ing “interception of wire, oral, or electronic communica-
tions” to determine that “there is probable cause for belief
that particular communications concerning [one of various
listed offenses] will be obtained through such intercep-
tion.” 18 U. S. C. §2518(3)(b) (emphasis added); see also
United States v. Ricciardelli, 998 F. 2d 8, 11, n. 3 (CA1
1993) (“[T]he magistrate issues the warrant on the basis of
a substantial probability that crime-related conversations
will ensue.”). Thus, when an anticipatory warrant is
issued, “the fact that the contraband is not presently
located at the place described in the warrant is immate-
rial, so long as there is probable cause to believe that it
will be there when the search warrant is executed.”
United States v. Garcia, 882 F. 2d 699, 702 (CA2 1989)
(quoting United States v. Lowe, 575 F. 2d 1193, 1194 (CA6
1978); internal quotation marks omitted).
——————
  2 For this reason, probable cause may cease to exist after a warrant is

issued. The police may learn, for instance, that contraband is no longer
located at the place to be searched. See, e.g., United States v. Bowling,
900 F. 2d 926, 932 (CA6 1990) (recognizing that a fruitless consent
search could “dissipat[e] the probable cause that justified a warrant”).
Or the probable-cause showing may have grown “stale” in view of the
time that has passed since the warrant was issued. See United States
v. Wagner, 989 F. 2d 69, 75 (CA2 1993) (“[T]he facts in an affidavit
supporting a search warrant must be sufficiently close in time to the
issuance of the warrant and the subsequent search conducted so that
probable cause can be said to exist as of the time of the search and not
simply as of some time in the past.”); see also Sgro v. United States, 287
U. S. 206, 210–211 (1932).
6                UNITED STATES v. GRUBBS

                     Opinion of the Court

   Anticipatory warrants are, therefore, no different in
principle from ordinary warrants. They require the mag-
istrate to determine (1) that it is now probable that (2)
contraband, evidence of a crime, or a fugitive will be on
the described premises (3) when the warrant is executed.
It should be noted, however, that where the anticipatory
warrant places a condition (other than the mere passage of
time) upon its execution, the first of these determinations
goes not merely to what will probably be found if the
condition is met. (If that were the extent of the probability
determination, an anticipatory warrant could be issued for
every house in the country, authorizing search and seizure
if contraband should be delivered—though for any single
location there is no likelihood that contraband will be
delivered.) Rather, the probability determination for a
conditioned anticipatory warrant looks also to the likeli-
hood that the condition will occur, and thus that a proper
object of seizure will be on the described premises. In
other words, for a conditioned anticipatory warrant to
comply with the Fourth Amendment’s requirement of
probable cause, two prerequisites of probability must be
satisfied. It must be true not only that if the triggering
condition occurs “there is a fair probability that contra-
band or evidence of a crime will be found in a particular
place,” Gates, supra, at 238, but also that there is probable
cause to believe the triggering condition will occur. The
supporting affidavit must provide the magistrate with
sufficient information to evaluate both aspects of the
probable-cause determination. See Garcia, supra, at 703.
   In this case, the occurrence of the triggering condition—
successful delivery of the videotape to Grubbs’ residence—
would plainly establish probable cause for the search. In
addition, the affidavit established probable cause to be-
lieve the triggering condition would be satisfied. Although
it is possible that Grubbs could have refused delivery of
the videotape he had ordered, that was unlikely. The
                 Cite as: 547 U. S. ____ (2006)            7

                     Opinion of the Court

Magistrate therefore “had a ‘substantial basis for . . .
conclud[ing]’ that probable cause existed.” Gates, 462
U. S., at 238–239 (quoting Jones v. United States, 362 U. S.
257, 271 (1960)).
                              III
   The Ninth Circuit invalidated the anticipatory search
warrant at issue here because the warrant failed to specify
the triggering condition. The Fourth Amendment’s par-
ticularity requirement, it held, “applies with full force to
the conditions precedent to an anticipatory search war-
rant.” 377 F. 3d, at 1077–1078.
   The Fourth Amendment, however, does not set forth
some general “particularity requirement.” It specifies only
two matters that must be “particularly describ[ed]” in the
warrant: “the place to be searched” and “the persons or
things to be seized.” We have previously rejected efforts to
expand the scope of this provision to embrace unenumer-
ated matters. In Dalia v. United States, 441 U. S. 238
(1979), we considered an order authorizing the intercep-
tion of oral communications by means of a “bug” installed
by the police in the petitioner’s office. The petitioner
argued that, if a covert entry is necessary to install such a
listening device, the authorizing order must “explicitly set
forth its approval of such entries before the fact.” Id., at
255. This argument fell before the “ ‘precise and clear’ ”
words of the Fourth Amendment: “Nothing in the lan-
guage of the Constitution or in this Court’s decisions
interpreting that language suggests that, in addition to
the [requirements set forth in the text], search warrants
also must include a specification of the precise manner in
which they are to be executed.” Id., at 255 (quoting Stan-
ford v. Texas, 379 U. S. 476, 481 (1965)), 257. The language
of the Fourth Amendment is likewise decisive here; its
particularity requirement does not include the conditions
precedent to execution of the warrant.
8                UNITED STATES v. GRUBBS

                      Opinion of the Court

   Respondent, drawing upon the Ninth Circuit’s analysis
below, relies primarily on two related policy rationales.
First, he argues, setting forth the triggering condition in
the warrant itself is necessary “to delineate the limits of
the executing officer’s power.” Brief for Respondent 20.
This is an application, respondent asserts, of the following
principle: “[I]f there is a precondition to the valid exercise
of executive power, that precondition must be particularly
identified on the face of the warrant.” Id., at 23. That
principle is not to be found in the Constitution. The
Fourth Amendment does not require that the warrant set
forth the magistrate’s basis for finding probable cause,
even though probable cause is the quintessential “precon-
dition to the valid exercise of executive power.” Much less
does it require description of a triggering condition.
   Second, respondent argues that listing the triggering
condition in the warrant is necessary to “ ‘assur[e] the
individual whose property is searched or seized of the
lawful authority of the executing officer, his need to
search, and the limits of his power to search.’ ” Id., at 19
(quoting United States v. Chadwick, 433 U. S. 1, 9 (1977)).
The Ninth Circuit went even further, asserting that if the
property owner were not informed of the triggering condi-
tion, he “would ‘stand [no] real chance of policing the
officers’ conduct.’ ” 377 F. 3d, at 1079 (quoting Ramirez v.
Butte-Silver Bow County, 298 F. 3d 1022, 1027 (CA9
2002)). This argument assumes that the executing officer
must present the property owner with a copy of the war-
rant before conducting his search. See 377 F. 3d, at 1079,
n. 9. In fact, however, neither the Fourth Amendment nor
Rule 41 of the Federal Rules of Criminal Procedure im-
poses such a requirement. See Groh v. Ramirez, 540 U. S.
551, 562, n. 5 (2004). “The absence of a constitutional
requirement that the warrant be exhibited at the outset of
the search, or indeed until the search has ended, is . . .
evidence that the requirement of particular description
                  Cite as: 547 U. S. ____ (2006)            9

                      Opinion of the Court

does not protect an interest in monitoring searches.”
United States v. Stefonek, 179 F. 3d 1030, 1034 (CA7 1999)
(citations omitted). The Constitution protects property
owners not by giving them license to engage the police in a
debate over the basis for the warrant, but by interposing,
ex ante, the “deliberate, impartial judgment of a judicial
officer . . . between the citizen and the police.” Wong Sun
v. United States, 371 U. S. 471, 481–482 (1963), and by
providing, ex post, a right to suppress evidence improperly
obtained and a cause of action for damages.
                        *     *    *
  Because the Fourth Amendment does not require that
the triggering condition for an anticipatory search warrant
be set forth in the warrant itself, the Court of Appeals
erred in invalidating the warrant at issue here. The
judgment of the Court of Appeals is reversed, and the case
is remanded for further proceedings consistent with this
opinion.
                                             It is so ordered.

  JUSTICE ALITO took no part in the consideration or
decision of this case.
                 Cite as: 547 U. S. ____ (2006)           1

                     Opinion of SOUTER, J.

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 04–1414
                         _________________


UNITED STATES, PETITIONER v. JEFFREY GRUBBS
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE NINTH CIRCUIT
                       [March 21, 2006]

   JUSTICE SOUTER, with whom JUSTICE STEVENS and
JUSTICE GINSBURG join, concurring in part and concurring
in the judgment.
   I agree with the Court that anticipatory warrants are
constitutional for the reasons stated in Part II of the
Court’s opinion, and I join in the disposition of this case.
But I would qualify some points made in Part III.
   The Court notes that a warrant’s failure to specify the
place to be searched and the objects sought violates an
express textual requirement of the Fourth Amendment,
whereas the text says nothing about a condition placed by
the issuing magistrate on the authorization to search
(here, delivery of the package of contraband). That textual
difference is, however, no authority for neglecting to spec-
ify the point or contingency intended by the magistrate to
trigger authorization, and the government should beware
of banking on the terms of a warrant without such specifi-
cation. The notation of a starting date was an established
feature even of the objectionable 18th-century writs of
assistance, see, e.g., Massachusetts Writs of Assistance
Bill, 1762, reprinted in M. Smith, The Writs of Assistance
Case 567–568 (1978); Writ of Assistance (English) of
George III, 1761, reprinted in id., at 524–527. And it is
fair to say that the very word “warrant” in the Fourth
Amendment means a statement of authority that sets out
the time at which (or, in the case of anticipatory warrants,
2                   UNITED STATES v. GRUBBS

                         Opinion of SOUTER, J.

the condition on which) the authorization begins.*
   An issuing magistrate’s failure to mention that condi-
tion can lead to several untoward consequences with
constitutional significance. To begin with, a warrant that
fails to tell the truth about what a magistrate authorized
cannot inform the police officer’s responsibility to respect
the limits of authorization, see Groh v. Ramirez, 540 U. S.
551, 560–563, 561, and n. 4 (2004), a failing assuming real
significance when the warrant is not executed by the
official who applied for it and happens to know the un-
stated condition. The peril is that if an officer simply
takes such a warrant on its face and makes the ostensibly
authorized search before the unstated condition has been
met, the search will be held unreasonable. It is true that
we have declined to apply the exclusionary rule when a
police officer reasonably relies on the product of a magis-
trate’s faulty judgment or sloppy practice, see Massachu-
setts v. Sheppard, 468 U. S. 981, 987–991 (1984). But when
a government officer obtains what the magistrate says is
an anticipatory warrant, he must know or should realize
when it omits the condition on which authorization de-
pends, and it is hard to see why the government should
not be held to the condition despite the unconditional face
of the warrant. Cf. Groh v. Ramirez, supra, at 554–555,
563, and n. 6 (declaring unconstitutional a search con-
ducted pursuant to a warrant failing to specify the items
the government asked the magistrate permission to seize
in part because “officers leading a search team must ‘make
sure that they have a proper warrant that in fact author-
izes the search and seizure they are about to conduct’ ”
(brackets omitted)).
   Nor does an incomplete anticipatory warrant address an
——————
  * Federal Rule of Criminal Procedure 41(e)(2)(A) in fact requires that
an issued warrant command the executing officer to “execute the
warrant within a specified time no longer than 10 days.”
                  Cite as: 547 U. S. ____ (2006)             3

                      Opinion of SOUTER, J.

owner’s interest in an accurate statement of the govern-
ment’s authority to search property. To be sure, the ex-
tent of that interest is yet to be settled; in Groh v. Ramirez,
supra, the Court was careful to note that the right of an
owner to demand to see a copy of the warrant before mak-
ing way for the police had not been determined, id., at 562,
n. 5, and it remains undetermined today. But regardless
of any right on the owner’s part, showing an accurate
warrant reliably “assures the individual whose property is
searched or seized of the lawful authority of the executing
officer, his need to search, and the limits of his power to
search.” United States v. Chadwick, 433 U. S. 1, 9 (1977),
quoted in Groh v. Ramirez, supra, at 561. And if a later
case holds that the homeowner has a right to inspect the
warrant on request, a statement of the condition of au-
thorization would give the owner a right to correct any
misapprehension on the police’s part that the condition
had been met when in fact it had not been. If the police
were then to enter anyway without a reasonable (albeit
incorrect) justification, the search would certainly be open
to serious challenge as unreasonable within the meaning
of the Fourth Amendment.

```

---

## GROUP: content/cases/United States v. Harris (1971).md  (`case`, 6 assertions)

### content_page

```
---
title: "United States v. Harris (1971)"
type: case
citation: "403 U.S. 573 (1971)"
parallel_cite: "91 S. Ct. 2075; 29 L. Ed. 2d 723"
neutral_cite: 1971 U.S. LEXIS 18
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1971
date_decided: 1971-06-28
docket: 30
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1971-06-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "United States v. Harris (1971)"
  varies_by_point: false
  scope_note: "The penal-interest reliability principle survives — a declaration against penal interest remains a recognized indicium of an informant's reliability, carried forward into the totality-of-the-circumstances test. The Aguilar-Spinelli two-pronged framework this plurality was eroding was later replaced by Illinois v. Gates (1983)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108379/united-states-v-harris/"
  cluster_id: 108379
  opinion_id: 108379
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Progeny"
  - page: "[[Probable Cause in the Affidavit]]"
    role: "Related (cross-doctrine)"
related: ["[[Aguilar v. Texas]]", "[[Spinelli v. United States]]", "[[Illinois v. Gates]]"]
aliases: ["United States v. Harris"]
tags: ["case", "fourth-amendment", "probable-cause", "informant", "warrant-requirement"]
holding: "An informant's statement against his penal interest is itself an indicium of reliability that can support probable cause for a warrant; admissions of crime 'carry their own indicia of credibility,' and a magistrate may also rely on an officer's knowledge of the suspect's reputation."
lake:
  record_id: "United States v. Harris (1971)"
  status: verified
  projected_at: 2026-07-09
---

# United States v. Harris (1971)

*403 U.S. 573 (1971)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A federal tax investigator obtained a warrant to search Harris's premises for nontaxpaid liquor. The affidavit recited the affiant's knowledge of Harris's longstanding reputation as a trafficker in illicit whiskey and a tip from a confidential informant — who feared for his safety — stating that he had repeatedly, and recently, purchased illicit whiskey at the premises over the past two years. The Court of Appeals held the affidavit insufficient under *[[Aguilar v. Texas]]* and *[[Spinelli v. United States]]*.

## Issue
May an informant's tip support probable cause for a warrant where it is corroborated by the affiant's knowledge of the suspect's reputation and by the informant's own admission — against his penal interest — of buying illicit whiskey at the premises?

## Rule
Yes. The informant's statements "were against the informant's penal interest, for he thereby admitted major elements of an offense." Because "[p]eople do not lightly admit a crime and place critical evidence in the hands of the police in the form of their own admissions," such "[a]dmissions of crime, like admissions against proprietary interests, carry their own indicia of credibility — sufficient at least to support a finding of probable cause to search." — 403 U.S. at 583. ^pin-583

"That the informant may be paid or promised a 'break' does not eliminate the residual risk and opprobrium of having admitted criminal conduct." — *Id.* at 584. ^pin-584

The admission of long-running illicit purchases "itself and without more, implicated that property and furnished probable cause to search." — [*Id.*](https://www.courtlistener.com/opinion/108379/united-states-v-harris/#:~:text=itself%20and%20without%20more%2C%20implicated) ^pin-584b

A magistrate may likewise rely on an officer's knowledge of a suspect's reputation as a "practical consideration of everyday life." — *Id.* at 583. ^pin-583b

## Application
The informant admitted repeatedly buying unstamped whiskey from Harris — major elements of a federal offense — so his tip carried its own credibility, undiminished by any payment or promised leniency, and standing alone furnished probable cause to search the premises. The affiant's knowledge of Harris's reputation as a bootlegger added further support. Read commonsensically rather than under a rigid two-pronged formula, the affidavit established probable cause.

## Conclusion
The affidavit established probable cause and the warrant was valid; the judgment below was reversed. (The Chief Justice's opinion was fractured, but a majority agreed with Part III's penal-interest rationale.)

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The penal-interest reliability principle remains valid and is a recognized factor in assessing an informant's credibility. The *[[Aguilar v. Texas|Aguilar]]*–*[[Spinelli v. United States|Spinelli]]* two-pronged test that this plurality was already eroding was later abandoned for a totality-of-the-circumstances inquiry in [[Illinois v. Gates]] (1983), within which *Harris*'s penal-interest insight survives. No negative treatment of *Harris* itself.

## Appears on
- [[Probable Cause]] — *Progeny*
- [[Probable Cause in the Affidavit]] — *Related (cross-doctrine)*

## Sources
- *United States v. Harris*, 403 U.S. 573 (1971) — https://www.courtlistener.com/opinion/108379/united-states-v-harris/ — pinpoints: 583, 584.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3493ed0e19fedf61", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "403 U.S. 573 (1971)", "court": "U.S. Supreme Court", "neutral_cite": "1971 U.S. LEXIS 18", "official_citation_present": true, "parallel_cite": "91 S. Ct. 2075; 29 L. Ed. 2d 723", "title": "United States v. Harris (1971)", "year": "1971"}}
{"assertion_id": "6639ccc2ce2449c3", "dimension": "support", "kind": "home_role", "locator": {"home": "Probable Cause"}, "payload": {"home": "Probable Cause", "role": "Progeny", "title": "United States v. Harris (1971)"}}
{"assertion_id": "715856d0545c719b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An informant's statement against his penal interest is itself an indicium of reliability that can support probable cause for a warrant; admissions of crime 'carry their own indicia of credibility,' and a magistrate may also rely on an officer's knowledge of the suspect's reputation.", "title": "United States v. Harris (1971)"}}
{"assertion_id": "aa96eff877a937f8", "dimension": "support", "kind": "home_role", "locator": {"home": "Probable Cause in the Affidavit"}, "payload": {"home": "Probable Cause in the Affidavit", "role": "Related (cross-doctrine)", "title": "United States v. Harris (1971)"}}
{"assertion_id": "569fc45b70c3e119", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Harris (1971)"}}
{"assertion_id": "ae24a5becded46d1", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1971-06-28", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Harris (1971)", "field_i_validity": "good_law", "scope_note": "The penal-interest reliability principle survives — a declaration against penal interest remains a recognized indicium of an informant's reliability, carried forward into the totality-of-the-circumstances test. The Aguilar-Spinelli two-pronged framework this plurality was eroding was later replaced by Illinois v. Gates (1983).", "title": "United States v. Harris (1971)", "varies_by_point": "false"}}
```

### lake record — United States v. Harris (1971)

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Harris (1971)",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Harris",
    "case_name_short": "Harris",
    "case_name_full": "United States v. Harris",
    "input_case_name": "United States v. Harris (1971)",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1971-06-28",
    "year": 1971,
    "docket": "30",
    "cluster_id": 108379,
    "lead_opinion_id": 108379,
    "sibling_ids": [
      108379,
      9883118,
      9883119,
      9883120,
      9883121
    ],
    "absolute_url": "/opinion/108379/united-states-v-harris/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "403 U.S. 573",
      "volume": "403",
      "reporter": "U.S.",
      "page": "573",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "91 S. Ct. 2075",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "2075",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "29 L. Ed. 2d 723",
        "volume": "29",
        "reporter": "L. Ed. 2d",
        "page": "723",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1971 U.S. LEXIS 18",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "18",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "403 U.S. 573",
        "volume": "403",
        "reporter": "U.S.",
        "page": "573",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 S. Ct. 2075",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "2075",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "29 L. Ed. 2d 723",
        "volume": "29",
        "reporter": "L. Ed. 2d",
        "page": "723",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1971 U.S. LEXIS 18",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "18",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "403 U.S. 573",
    "official_selection": {
      "court_class": "scotus",
      "selected": "403 U.S. 573",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-583",
      "page": null,
      "quote": "--- # United States v. Harris (1971) *403 U.S. 573 (1971)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A federal tax investigator obtained a warrant to search Harris's premises for nontaxpaid liquor. The affidavit recited the affiant's knowledge of Harris's longstanding reputation as a trafficker in illicit whiskey and a tip from a confidential informant \u2014 who feared for his safety \u2014 stating that he had repeatedly, and recently, purchased illicit whiskey at the premises over the past two years. The Court of Appeals held the affidavit insufficient under *Aguilar v. Texas* and *Spinelli v. United States*. ## Issue May an informant's tip support probable cause for a warrant where it is corroborated by the affiant's knowledge of the suspect's reputation and by the informant's own admission \u2014 against his penal interest \u2014 of buying illicit whiskey at the premises? ## Rule Yes. The informant's statements",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-584",
      "page": null,
      "quote": "That the informant may be paid or promised a 'break' does not eliminate the residual risk and opprobrium of having admitted criminal conduct.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-584b",
      "page": null,
      "quote": "itself and without more, implicated that property and furnished probable cause to search.",
      "star_marker": "584",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 26583,
      "fragment": "#:~:text=itself%20and%20without%20more%2C%20implicated",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-583b",
      "page": null,
      "quote": "practical consideration of everyday life.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1971-06-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Harris (1971)",
    "varies_by_point": false,
    "scope_note": "The penal-interest reliability principle survives \u2014 a declaration against penal interest remains a recognized indicium of an informant's reliability, carried forward into the totality-of-the-circumstances test. The Aguilar-Spinelli two-pronged framework this plurality was eroding was later replaced by Illinois v. Gates (1983).",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Harris (1971):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Brundidge",
          "cluster_id": 73678,
          "cite": [
            "170 F.3d 1350",
            "1999 U.S. App. LEXIS 5958",
            "1999 WL 181850"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lawrence D. Lamorie Patricia L. Lamorie",
          "cluster_id": 729724,
          "cite": [
            "100 F.3d 547",
            "1996 U.S. App. LEXIS 28984",
            "1996 WL 637645"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hackleman v. State",
          "cluster_id": 2459738,
          "cite": [
            "919 S.W.2d 440",
            "1996 WL 60451"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lauren Eric Wilhelm",
          "cluster_id": 715677,
          "cite": [
            "80 F.3d 116",
            "1996 U.S. App. LEXIS 6245",
            "1996 WL 149356"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Edward Czuprynski",
          "cluster_id": 656589,
          "cite": [
            "8 F.3d 1113",
            "1993 WL 454161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Mellan",
          "cluster_id": 8717546,
          "cite": [
            "817 F. Supp. 1072"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane1_negative"
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
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
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
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chambers v. Mississippi",
          "cluster_id": 108718,
          "cite": [
            "35 L. Ed. 2d 297",
            "93 S. Ct. 1038",
            "410 U.S. 284",
            "1973 U.S. LEXIS 107"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Melson",
          "cluster_id": 2442934,
          "cite": [
            "638 S.W.2d 342",
            "1982 Tenn. LEXIS 431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Novembrino",
          "cluster_id": 1516571,
          "cite": [
            "519 A.2d 820",
            "105 N.J. 95",
            "1987 N.J. LEXIS 265"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carmine Tramunti",
          "cluster_id": 326798,
          "cite": [
            "513 F.2d 1087"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Johnson",
          "cluster_id": 5687957,
          "cite": [
            "66 N.Y.2d 398",
            "488 N.E.2d 439",
            "497 N.Y.S.2d 618",
            "1985 N.Y. LEXIS 17918"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bower v. State",
          "cluster_id": 1625069,
          "cite": [
            "769 S.W.2d 887",
            "1989 Tex. Crim. App. LEXIS 6",
            "1989 WL 4325"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 1690639,
          "cite": [
            "709 So. 2d 512",
            "1998 WL 114500"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Abram v. State",
          "cluster_id": 1096122,
          "cite": [
            "606 So. 2d 1015",
            "1992 WL 223914"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Randolph Jakobetz",
          "cluster_id": 577111,
          "cite": [
            "955 F.2d 786",
            "34 Fed. R. Serv. 876",
            "1992 U.S. App. LEXIS 322",
            "1992 WL 2126"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bartolomeo",
          "cluster_id": 5684916,
          "cite": [
            "53 N.Y.2d 225",
            "423 N.E.2d 371",
            "440 N.Y.S.2d 894",
            "1981 N.Y. LEXIS 2477"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martin F. Burke",
          "cluster_id": 328036,
          "cite": [
            "517 F.2d 377",
            "1975 U.S. App. LEXIS 14661"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stanley Mills Stanert",
          "cluster_id": 452155,
          "cite": [
            "762 F.2d 775"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Frank Diecidue, Larry Neil Miller, Frank Boni, Jr., A/K/A \"Mustache Frankie,\" Manuel Gispert, Anthony Antone, and Homer Rex Davis",
          "cluster_id": 368882,
          "cite": [
            "603 F.2d 535",
            "4 Fed. R. Serv. 1294",
            "1979 U.S. App. LEXIS 11494"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Martin",
          "cluster_id": 374716,
          "cite": [
            "615 F.2d 318",
            "1980 U.S. App. LEXIS 18767"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lilly",
          "cluster_id": 1375322,
          "cite": [
            "461 S.E.2d 101",
            "194 W. Va. 595"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Woodward v. State",
          "cluster_id": 2388927,
          "cite": [
            "668 S.W.2d 337",
            "1984 Tex. Crim. App. LEXIS 616"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin Davis (03-1451) and Keith Presley (03-1621)",
          "cluster_id": 792556,
          "cite": [
            "430 F.3d 345",
            "2005 U.S. App. LEXIS 25124",
            "2005 WL 3108503"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Warren G. Johnson",
          "cluster_id": 303789,
          "cite": [
            "461 F.2d 285",
            "1972 U.S. App. LEXIS 9023"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hanlon",
          "cluster_id": 5681186,
          "cite": [
            "36 N.Y.2d 549",
            "330 N.E.2d 631",
            "369 N.Y.S.2d 677",
            "1975 N.Y. LEXIS 1854"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Janecka v. State",
          "cluster_id": 2467162,
          "cite": [
            "739 S.W.2d 813",
            "1987 Tex. Crim. App. LEXIS 739"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kirk C. Reivich",
          "cluster_id": 471842,
          "cite": [
            "793 F.2d 957",
            "1986 U.S. App. LEXIS 26468"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Arrington",
          "cluster_id": 1350177,
          "cite": [
            "319 S.E.2d 254",
            "311 N.C. 633",
            "1984 N.C. LEXIS 1750"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Couture",
          "cluster_id": 7891945,
          "cite": [
            "194 Conn. 530",
            "482 A.2d 300",
            "1984 Conn. LEXIS 695"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108379 OR 9883118 OR 9883119 OR 9883120 OR 9883121) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NzQ0Mzg0MDAwMDAmcz0yMDY2NDIxJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108379+OR+9883118+OR+9883119+OR+9883120+OR+9883121%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(108379 OR 9883118 OR 9883119 OR 9883120 OR 9883121)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDUmcz0yMTQxMDQzJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108379+OR+9883118+OR+9883119+OR+9883120+OR+9883121%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108379 OR 9883118 OR 9883119 OR 9883120 OR 9883121)",
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
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108379 OR 9883118 OR 9883119 OR 9883120 OR 9883121)",
    "indexed_citing_opinions": 1258,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108379,
        "count": 1178,
        "count_source": "search"
      },
      {
        "opinion_id": 9883118,
        "count": 115,
        "count_source": "search"
      },
      {
        "opinion_id": 9883119,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9883120,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9883121,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1806,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-harris-1971.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjYzMTc3MSZzPTQ2MjM2NjAmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28108379+OR+9883118+OR+9883119+OR+9883120+OR+9883121%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108379,
        "cited_id": 97847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 107684,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 277169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 285442,
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
    "date_created": "2026-07-06T00:22:38Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:22:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:22:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:27:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:22:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Harris (1971)

```
<div>
<center><b><span class="citation" data-id="9883118"><a href="/opinion/108379/united-states-v-harris/" aria-description="Citation for case: United States v. Harris">403 U.S. 573</a></span> (1971)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
HARRIS.</h1></center>
<center>No. 30.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 23, 1971</center>
<center>Decided June 28, 1971</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SIXTH CIRCUIT.
<p><span class="star-pagination">*574</span> <i>Beatrice Rosenberg</i> argued the cause for the United States. With her on the brief were <i>Solicitor General Griswold, Assistant Attorney General Wilson, Richard B. Stone,</i> and <i>Mervyn Hamburg.</i></p>
<p><i>Steven M. Umin,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./400/955/">400 U. S. 955</a></span>, argued the cause and filed a brief for respondent.</p>
<p><i>Frank G. Carrington, Jr.,</i> and <i>Alan S. Ganz</i> filed a brief for Americans for Effective Law Enforcement, Inc., as <i>amicus curiae</i> urging reversal.</p>
<p>MR. CHIEF JUSTICE BURGER announced the judgment of the Court and an opinion in which MR. JUSTICE BLACK and MR. JUSTICE BLACKMUN join, and in Part I of which <span class="star-pagination">*575</span> MR. JUSTICE STEWART joins, and in Part III of which MR. JUSTICE WHITE joins.</p>
<p>We granted certiorari in this case to consider the recurring question of what showing is constitutionally necessary to satisfy a magistrate that there is a substantial basis for crediting the report of an informant known to the police, but not identified to the magistrate, who purports to relate his personal knowledge of criminal activity.</p>
<p>In 1967 a federal tax investigator and a local constable entered the premises of respondent Harris, pursuant to a search warrant issued by a federal magistrate, and seized jugs of whiskey upon which the federal tax had not been paid. The warrant had been issued solely on the basis of the investigator's affidavit, which recited the following:</p>
<blockquote>"Roosevelt Harris has had a reputation with me for over 4 years as being a trafficker of nontaxpaid distilled spirits, and over this period I have received numerous information [<i>sic</i>] from all types of persons as to his activities. Constable Howard Johnson located a sizeable stash of illicit whiskey in an abandoned house under Harris' control during this period of time. This date, I have received information from a person who fears for their [<i>sic</i>] life and property should their name be revealed. I have interviewed this person, found this person to be a prudent person, and have, under a sworn verbal statement, gained the following information: This person has personal knowledge of and has purchased illicit whiskey from within the residence described, for a period of more than 2 years, and most recently within the past 2 weeks, has knowledge of a person who purchased illicit whiskey within the past two days from the house, has personal knowledge that the illicit whiskey is consumed by purchasers in the outbuilding known as and utilized as <span class="star-pagination">*576</span> the `dance hall,' and has seen Roosevelt Harris go to the other outbuilding, located about 50 yards from the residence, on numerous occasions, to obtain the whiskey for this person and other persons."</blockquote>
<p>Respondent was subsequently charged with possession of nontaxpaid liquor, in violation of <span class="citation no-link">26 U. S. C. § 5205</span> (a) (2). His pretrial motion to suppress the seized evidence on the ground that the affidavit was insufficient to establish probable cause was overruled, and he was convicted after a jury trial and sentenced to two years' imprisonment. The Court of Appeals for the Sixth Circuit reversed the conviction, holding that the information in the affidavit was insufficient to enable the magistrate to assess the informant's reliability and trustworthiness. <span class="citation" data-id="285442"><a href="/opinion/285442/united-states-v-roosevelt-hudson-harris/#797" aria-description="Citation for case: United States v. Roosevelt Hudson Harris">412 F. 2d 796, 797</a></span> (1969).</p>
<p>The Court of Appeals relied on <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), in which we held that an affidavit based solely on the hearsay report of an unidentified informant must set forth "some of the underlying circumstances from which the officer concluded that the informant . . . was `credible' or his information `reliable.' " <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#114" aria-description="Citation for case: Aguilar v. Texas"><i>Id.,</i> at 114</a></span>. It concluded that the affidavit was insufficient because no information was presented to enable the magistrate to evaluate the informant's reliability or trustworthiness. The court noted the absence of any allegation that the informant was a "truthful" person, but only an allegation that the informant was "prudent." Having found the informant's tip inadequate under <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i> the court of Appeals, relying on <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969), looked to the remaining allegations of the affidavit to determine whether they provided independent corroboration of the informant. The Court of Appeals held that the constable's prior discovery of a cache on respondent's property within the previous four years was too remote, and, <span class="star-pagination">*577</span> citing certain language from <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>,</i> it gave no weight whatever to the assertion that respondent had a general reputation known to the officer as a trafficker in illegal whiskey.</p>
<p>For the reasons stated below, we reverse the judgment of the Court of Appeals and reinstate the judgment of conviction.</p>
<p></p>
<h2>I</h2>
<p>In evaluating the showing of probable cause necessary to support a search warrant, against the Fourth Amendment's prohibition of unreasonable searches and seizures, we would do well to heed the sound admonition of <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102</a></span> (1965):</p>
<blockquote>"[T]he Fourth Amendment's commands, like all constitutional requirements, are practical and not abstract. If the teachings of the Court's cases are to be followed and the constitutional policy served, affidavits for search warrants, such as the one involved here, must be tested and interpreted by magistrates and courts in a commonsense and realistic fashion. They are normally drafted by nonlawyers in the midst and haste of a criminal investigation. Technical requirements of elaborate specificity once exacted under common law pleadings have no proper place in this area. A grudging or negative attitude by reviewing courts toward warrants will tend to discourage police officers from submitting their evidence to a judicial officer before acting." <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S., at 108</a></span>.</blockquote>
<p><i>Aguilar</i> in no way departed from these sound principles. There a warrant was issued on nothing more than an affidavit reciting:</p>
<blockquote>"Affiants have received reliable information from a credible person and do believe that heroin, marijuana, <span class="star-pagination">*578</span> barbiturates and other narcotics and narcotic paraphernalia are being kept at the above described premises for the purpose of sale and use contrary to the provisions of the law." <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#109" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 109</a></span>.</blockquote>
<p>The affidavit, therefore, contained none of the underlying "facts or circumstances" from which the magistrate could find probable cause. <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#47" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41, 47</a></span> (1933). On the contrary, the affidavit was a "mere affirmation of suspicion and belief" (<span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#46" aria-description="Citation for case: Nathanson v. United States"><i>Nathanson, supra,</i> at 46</a></span>) and gained nothing by the incorporation by reference of the informant's unsupported belief. See <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar, supra,</a></span></i> at 114 n. 4.</p>
<p>Significantly, the Court in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> cited with approval the affidavit upheld in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960). That affidavit read in pertinent part as follows:</p>
<blockquote>"In the late afternoon of Tuesday, August 20, 1957, I, Detective Thomas Didone, Jr. received information that Cecil Jones and Earline Richardson were involved in the illicit narcotic traffic and that they kept a ready supply of heroin on hand in the above mentioned apartment. The source of information also relates that the two aforementioned persons kept these same narcotics either on their person, under a pillow, on a dresser or on a window ledge in said apartment. The source of information goes on to relate that on many occasions the source of information has gone to said apartment and purchased narcotic drugs from the above mentioned persons and that the narcotics were secreated [<i>sic</i>] in the above mentioned places. The last time being August 20, 1957." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States"><i>Id.,</i> at 267-268, n. 2</a></span>.</blockquote>
<p>The substance of the tip, held sufficient in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> closely parallels that here held insufficient by the Court <span class="star-pagination">*579</span> of Appeals. Both recount personal and recent<sup>[*]</sup> observations by an unidentified informant of criminal activity, factors showing that the information had been gained in a reliable manner, and serving to distinguish both tips from that held insufficient in <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli, supra,</a></span></i> in which the affidavit failed to explain how the informant came by his information. <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#416" aria-description="Citation for case: Spinelli v. United States"><i>Spinelli, supra,</i> at 416</a></span>.</p>
<p>The Court of Appeals seems to have believed, however, that there was no substantial basis for believing that the tip was truthful. Indeed, it emphasized that the affiant had never alleged that the informant was truthful, but only "prudent," a word that "signifies that he is circumspect in the conduct of his affairs, but reveals nothing about his credibility." <span class="citation" data-id="285442"><a href="/opinion/285442/united-states-v-roosevelt-hudson-harris/#797" aria-description="Citation for case: United States v. Roosevelt Hudson Harris">412 F. 2d, at 797-798</a></span>. Such a construction of the affidavit is the very sort of hypertechnicalitythe "elaborate specificity once exacted under common law"condemned by this Court in <i><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/" aria-description="Citation for case: United States v. Ventresca">Ventresca</a></span>.</i> A policeman's affidavit "should not be judged as an entry in an essay contest," <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#438" aria-description="Citation for case: Spinelli v. United States"><i>Spinelli, supra,</i> at 438</a></span> (Fortas, J., dissenting), but, rather, must be judged by the facts it contains. While a bare statement by an affiant that he believed the informant to be truthful would not, in itself, provide a <i>factual</i> basis for crediting the report of an unnamed informant, we conclude that the affidavit in the present case contains an ample factual basis for believing the informant which, when coupled <span class="star-pagination">*580</span> with affiant's own knowledge of the respondent's background, afforded a basis upon which a magistrate could reasonably issue a warrant. The accusation by the informant was plainly a declaration against interest since it could readily warrant a prosecution and could sustain a conviction against the informant himself. This will be developed in Part III.</p>
<p></p>
<h2>II</h2>
<p>In determining what quantum of information is necessary to support a belief that an unidentified informant's information is truthful, <i>Jones</i> v. <i>United States, supra</i><i>,</i> is a suitable benchmark. The affidavit in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> recounted the tip of an anonymous informant, who claimed to have recently purchased narcotics from the defendant at his apartment, and described the apartment in some detail. After reciting the substance of the tip the affiant swore as follows:</p>
<blockquote>"Both the aforementioned persons are familiar to the undersigned and other members of the Narcotic Squad. Both have admitted to the use of narcotic drugs and display needle marks as evidence of same.</blockquote>
<blockquote>"This same information, regarding the illicit narcotic traffic, conducted by [the defendant] has been given to the undersigned and to other officers of the narcotic squad by other sources of information.</blockquote>
<blockquote>"Because the source of information mentioned in the opening paragraph has given information to the undersigned on previous occasion and which was correct, and because this same information is given by other sources does believe that there is now illicit narcotic drugs being secreated [<i>sic</i>] in the above apartment . . . ." <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Id.,</a></span></i> at 268 n. 2.</blockquote>
<p>Mr. Justice Frankfurter, writing for the Court in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> upheld the warrant. Although the information in the affidavit was almost entirely hearsay, he concluded that <span class="star-pagination">*581</span> there was "substantial basis" for crediting the hearsay. The informant had previously given accurate information; his story was corroborated by "other sources" (albeit unnamed); additionally the defendant was known to the police as a user of narcotics. Justice Frankfurter emphasized the last two of these factors:</p>
<blockquote>"Corroboration through other sources of information reduced the chances of a reckless or prevaricating tale; that petitioner was a known user of narcotics made the charge against him much less subject to scepticism than would be such a charge against one without such a history." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States"><i>Id.,</i> at 271</a></span>.</blockquote>
<p><i>Aguilar</i> cannot be read as questioning the "substantial basis" approach of <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>.</i> And unless <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> has somehow, without acknowledgment, been overruled by <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>,</i> there would be no basis whatever for a holding that the affidavit in the present case is wanting. The affidavit in the present case, like that in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> contained a substantial basis for crediting the hearsay. Both affidavits purport to relate the personal observations of the informanta factor that clearly distinguishes <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>,</i> in which the affidavit failed to explain how the informant came by his information. Both recite prior events within the affiant's own knowledgethe needle marks in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> and Constable Johnson's prior seizure in the present caseindicating that the defendant had previously trafficked in contraband. These prior events again distinguish <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>,</i> in which no facts were supplied to support the assertion that Spinelli was "known . . . as a bookmaker, an associate of bookmakers, a gambler, and an associate of gamblers." <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#422" aria-description="Citation for case: Spinelli v. United States"><i>Spinelli, supra,</i> at 422</a></span>.</p>
<p>To be sure there is no averment in the present affidavit, as there was in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> that the informant had previously given "correct information," but this Court in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> never suggested that an averment of previous reliability was <span class="star-pagination">*582</span> necessary. Indeed, when the inquiry is, as it always must be in determining probable cause, whether the informant's <i>present</i> information is truthful or reliable, it is curious, at the very least, that MR. JUSTICE HARLAN would place such stress on vague attributes of "general background, employment . . . position in the community. . . ." (<i>Post,</i> at 600.) Were it not for some language in <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>,</i> it is doubtful that any of these reputation attributes of the informant could be said to reveal any more about his present reliability than is afforded by the support of the officer's personal knowledge of the suspect. In <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>,</i> however, the Court rejected as entitled to no weight the "bald and unilluminating" assertion that the suspect was known to the affiant as a gambler. <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#414" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 414</a></span>. For this proposition the Court relied on <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span> (1933). But a careful examination of <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> shows that the <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span></i> opinion did not fully reflect the critical points of what <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> held since it was limited to holding that reputation, <i>standing alone,</i> was insufficient; it surely did not hold it irrelevant when supported by other information. This reading of <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> is confirmed by <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949), in which the Court, in sustaining a finding of probable cause for a warrantless arrest, held proper the assertion of the searching officer that he had previously arrested the defendant for a similar offense and that the defendant had a reputation for hauling liquor. Such evidence would rarely be admissible at trial, but the Court took pains to emphasize the very different functions of criminal trials and preliminary determinations of probable cause. Trials are necessarily surrounded with evidentiary rules "developed to safeguard men from dubious and unjust convictions." <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States"><i>Id.,</i> at 174</a></span>. But before the trial we deal only with probabilities that "are not technical, they are the factual and practical considerations of <span class="star-pagination">*583</span> everyday life on which reasonable and prudent men, not legal technicians, act." <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States"><i>Brinegar, supra,</i> at 175</a></span>.</p>
<p>We cannot conclude that a policeman's knowledge of a suspect's reputationsomething that policemen frequently know and a factor that impressed such a "legal technician" as Mr. Justice Frankfurteris not a "practical consideration of everyday life" upon which an officer (or a magistrate) may properly rely in assessing the reliability of an informant's tip. To the extent that <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span></i> prohibits the use of such probative information, it has no support in our prior cases, logic, or experience and we decline to apply it to preclude a magistrate from relying on a law enforcement officer's knowledge of a suspect's reputation.</p>
<p></p>
<h2>III</h2>
<p>Quite apart from the affiant's own knowledge of respondent's activities, there was an additional reason for crediting the informant's tip. Here the warrant's affidavit recited extrajudicial statements of a declarant, who feared for his life and safety if his identity was revealed, that over the past two years he had many times and recently purchased "illicit whiskey." These statements were against the informant's penal interest, for he thereby admitted major elements of an offense under the Internal Revenue Code. Section 5205 (a) (2), Title 26, United States Code, proscribes the sale, purchase, or possession of unstamped liquor.</p>
<p>Common sense in the important daily affairs of life would induce a prudent and disinterested observer to credit these statements. People do not lightly admit a crime and place critical evidence in the hands of the police in the form of their own admissions. Admissions of crime, like admissions against proprietary interests, carry their own indicia of credibilitysufficient at least to support a finding of probable cause to search. That the informant may be paid or promised a "break" does <span class="star-pagination">*584</span> not eliminate the residual risk and opprobrium of having admitted criminal conduct. Concededly admissions of crime do not always lend credibility to contemporaneous or later accusations of another. But here the informant's admission that over a long period and currently he had been buying illicit liquor on certain premises, itself and without more, implicated that property and furnished probable cause to search.</p>
<p>It may be that this informant's out-of-court declarations would not be admissible at respondent's trial under <i>Donnelly</i> v. <i>United States,</i> <span class="citation" data-id="97847"><a href="/opinion/97847/donnelly-v-united-states/" aria-description="Citation for case: Donnelly v. United States">228 U. S. 243</a></span> (1913), or under <i>Bruton</i> v. <i>United States,</i> <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">391 U. S. 123</a></span> (1968). But <i>Donnelly's</i> implication that statements against penal interest are without value and <i>per se</i> inadmissible has been widely criticized; see the dissenting opinion of Mr. Justice Holmes in <span class="citation" data-id="97847"><a href="/opinion/97847/donnelly-v-united-states/#277" aria-description="Citation for case: Donnelly v. United States"><i>Donnelly, supra,</i> at 277</a></span>; 5 J. Wigmore, Evidence § 1477 (3d ed. 1940), and has been partially rejected in Rule 804 of the Proposed Rules of Evidence for the District Courts and Magistrates. More important, the issue in warrant proceedings is not guilt beyond reasonable doubt but probable cause for believing the occurrence of a crime and the secreting of evidence in specific premises. See <i>Brinegar</i> v. <i>United States, supra,</i> at 173. Whether or not <i><span class="citation" data-id="97847"><a href="/opinion/97847/donnelly-v-united-states/" aria-description="Citation for case: Donnelly v. United States">Donnelly</a></span></i> is to survive as a rule of evidence in federal trials, it should not be extended to warrant proceedings to prevent magistrates from crediting, in all circumstances, statements of a declarant containing admissions of criminal conduct. As for <i><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span>,</i> that case rested on the Confrontation Clause of the Sixth Amendment which seems inapposite to <i>ex parte</i> search warrant proceedings under the Fourth Amendment.</p>
<p>It will not do to say that warrants may not issue on uncorroborated hearsay. This only avoids the issue of whether there is reason for crediting the out-of-court statement. Nor is it especially significant that neither <span class="star-pagination">*585</span> the name nor the person of the informant was produced before the magistrate. The police themselves almost certainly knew his name, the truth of the affidavit is not in issue, and <i>McCray</i> v. <i>Illinois,</i> <span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300</a></span> (1967), disposed of the claim that the informant must be produced whenever the defendant so demands.</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE STEWART joins in Part I of THE CHIEF JUSTICE'S opinion and in the judgment of the Court.</p>
<p>MR. JUSTICE WHITE agrees with Part III of THE CHIEF JUSTICE'S opinion and has concluded that the affidavit, considered as a whole, was sufficient to support issuance of the warrant. He therefore concurs in the judgment of reversal.</p>
<p>MR. JUSTICE BLACK, concurring.</p>
<p>While I join the opinion of THE CHIEF JUSTICE which distinguishes this case from <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), and <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969), I would go further and overrule those two cases and wipe their holdings from the books for the reasons, among others, set forth in the dissent of Mr. Justice Clark in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i> which I joined, and my dissent in <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>.</i></p>
<p>MR. JUSTICE BLACKMUN, concurring.</p>
<p>I join the opinion of THE CHIEF JUSTICE and the judgment of the Court, but I add a personal comment in order to make very clear my posture as to <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969), cited in several places in that opinion. I was a member of the 6-2 majority of the United States Court of Appeals for the Eighth Circuit in <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9452981"><a href="/opinion/277169/william-spinelli-v-united-states/" aria-description="Citation for case: William Spinelli v. United States">382 F. 2d 871</a></span> (1967), which this Court by a 5-3 vote reversed, with the pivotal Justice concluding his concurring <span class="star-pagination">*586</span> opinion, <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#429" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 429</a></span>, by the observation that, "Pending full-scale reconsideration of that case [<i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959)], on the one hand, or of the <i>Nathanson-Aguilar</i> cases on the other, I join the opinion of the Court and the judgment of reversal, especially since a vote to affirm would produce an evenly divided Court." Obviously, I then felt that the Court of Appeals had correctly decided the case. Nothing this Court said in <i>Spinelli</i> convinced me to the contrary. I continue to feel today that <i>Spinelli</i> at this level was wrongly decided and, like MR. JUSTICE BLACK, I would overrule it.</p>
<p>MR. JUSTICE HARLAN, with whom MR. JUSTICE DOUGLAS, MR. JUSTICE BRENNAN, and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>This case presents the question of how our decisions in <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), and <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969), apply where magistrates in issuing search warrants are faced with the task of assessing the probable credibility of unidentified informants who purport to describe criminal activity of which they have personal knowledge, and where it does not appear that such informants have previously supplied accurate information to law enforcement officers.</p>
<p>I cannot agree that the affidavit here at issue provided a sufficient basis for an independent determination, by a neutral judicial officer, that probable cause existed. Accordingly, I would affirm the judgment of the Court of Appeals. Five members of this Court, however, for four separately expressed reasons, have concluded that the judgment below must be reversed. Some of the theories employed by those voting to reverse are wholly unlike any of the grounds urged by the Government.</p>
<p></p>
<h2>
<span class="star-pagination">*587</span> I</h2>
<p>Where, as in this case, the affiant states under oath that he has been informed of the existence of certain criminal activity, but has not observed that activity himself, a magistrate in discharging his duty to make an independent assessment of probable cause can properly issue a search warrant only if he concludes that; (a) the knowledge attributed to the informant, if true, would be sufficient to establish probable cause; (b) the affiant is likely relating truthfully what the informer said; and (c) it is reasonably likely that the informer's description of criminal behavior accurately reflects reality.<sup>[1]</sup></p>
<p>In the case before us, no one maintains that the magistrate's judgment as to elements (a) and (b) was not properly supported. Plainly the information set forth in the affidavit, if entitled to credit, establishes probable cause. And the magistrate was certainly entitled to rely on the agent's official status, his personal observation of the agent, and the oath administered to him by the magistrate in concluding that the affiant's assertions as to what he had been told by the informer were credible.</p>
<p>The final component of the probable cause equation, here involved, is that it must appear reasonably likely that the informer's claim that criminal conduct has occurred or is occurring is probably accurate. Our <span class="star-pagination">*588</span> cases establish that this element is satisfied only if there is reason to believe both that the informer is a truthful person generally and that he has based his particular conclusions in the matter at hand on reliable data, <i>Aguilar</i> v. <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Texas, supra</a></span></i><i>; </i><i>Spinelli</i> v. <i>United States, supra</i><i>,</i> for it is not reasonable to invade another's premises on the basis of information, even if it appears quite damning when simply taken at face value, unless there is corroboration of its trustworthiness. The fact that the magistrate has determined that the agent probably truthfully reported what the informant conveyed cannot, of course, establish the credibility or reliability of the information itself. More immediately relevant here, our cases have established that where the affiant relies upon the assertions of confidants to establish probable cause, the affidavit must set forth facts which enable the magistrate to judge for himself both the probable credibility of the informant and the reliability of his information, for only if this condition is met can a reviewing court be satisfied that the magistrate has fulfilled his constitutional duty to render an independent determination that probable cause exists. <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964); <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969). Cf. <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span> (1958); <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span> (1933); <i>Whiteley</i> v. <i>Warden,</i> <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560</a></span> (1971).<sup>[2]</sup></p>
<p>The parties are in agreement with these principles and have not urged that they be re-examined. Indeed, I think these precepts follow ineluctably from the constitutional command that "no Warrants shall issue, but upon probable cause." Whether, in this case, either of <span class="star-pagination">*589</span> these tests of the trustworthiness of the informer's tip has been met is, however, vigorously disputed.</p>
<p></p>
<h2>II</h2>
<p>Although the Court of Appeals did not address itself to this contention, respondent claims that the affidavit is insufficient to establish the reliability of the evidence upon which the informant based his conclusions. Of course, most of these data come from alleged direct personal observation of the informant, surely a sufficient basis upon which to predicate a finding of reliability under any test. However, respondent stresses that the allegation of direct observation of the criminal activity does not necessarily purport to embrace a period less than two weeks prior to the issuance of the search warrant. Moreover, the reliability of the source of the information that a purchase was made "within the past two days" is not established and, it is argued, the other information was too stale to support the issuance of a warrant.</p>
<p>This argument is premised upon an overly technical view of the affidavit. The informant is said to have personally bought illegal whiskey from respondent "within the past 2 weeks," which could well include a point in time quite close to the issuance of the warrant. More importantly, the totality of the tip evidently reveals that the informer purported to describe an ongoing operation which he claimed he had personally observed over the course of two years. Giving due deference to the magistrate's determination of probable cause and reading the affidavit "in a commonsense and realistic fashion," <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 108</a></span> (1965), I must conclude that the affidavit sets forth sufficient data to permit a magistrate to determine that, if the informer was likely telling the truth, information adequate to support a finding of probable cause was likely obtained in a reliable fashion.</p>
<p></p>
<h2>
<span class="star-pagination">*590</span> III</h2>
<p>I turn, then, to what the parties have treated as the crux of the controversy before us. Respondent contends, and the Court of Appeals so held, that the affidavit does not sufficiently set forth facts and circumstances from which the magistrate might properly have concluded that the informant, in purporting to detail his personal observation, was probably telling the truth. Conversely, the Government principally argues that two factors, singly or in combination, provided a factual basis for the magistrate's judgment that the tip was credible. First, the agent stated that he had "interviewed this person [and] found this person to be a prudent person." Second, the informant described the criminal activity in some detail and from his own personal knowledge.<sup>[3]</sup></p>
<p></p>
<h2>A</h2>
<p>The Government's first contention misconceives the basic thrust of this Court's decisions in the <i>Nathanson, Giordenello, Aguilar, Spinelli,</i> and <i><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span></i> cases, <i>supra.</i> The central proposition common to each of these decisions is that the determination of probable cause is to be made by the magistrate, not the affiant. That the agent-affiant determined the informer to be prudent cannot be a basis for sustaining this warrant unless magistrates are entitled to delegate their responsibilities to law enforcement officials. <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> held that an affidavit <span class="star-pagination">*591</span> to the effect that the affiant "has cause to suspect and does believe" that illicit liquor was located on certain premises did not sufficiently apprise the issuing magistrate of the underlying "facts or circumstances" from which "<i>he</i> can find probable cause." <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#47" aria-description="Citation for case: Nathanson v. United States">290 U. S., at 47</a></span> (emphasis added). In <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i> a sworn assertion that the informant was "a credible person" was held insufficient to enable the magistrate to assess that conclusion for himself. Only two Terms ago, we held a warrant constitutionally defective because "[t]hough the affiant swore that his confidant was `reliable,' he offered the magistrate no reason in support of this conclusion." <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#416" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 416</a></span>. Reading the assertion that the informer in this case was "prudent" in the broadest conceivable commonsense fashion, it does no more than claim he was "credible" or "reliable," <i>i. e.,</i> that he was likely telling the truth.<sup>[4]</sup> Such an assertion, however, is no more than a conclusion which the Constitution requires must be drawn independently by the magistrate. What this portion of the affidavit lacks are any of the underlying "facts or circumstances" that informed the agent's conclusion and whose presentation to the magistrate would enable him to assess the probability that this determination was sufficiently plausible to justify authorizing a search of respondent's premises.</p>
<p></p>
<h2>B</h2>
<p>Nor do I think this void is filled by the fact that the informant claimed to speak from his personal knowledge. <span class="star-pagination">*592</span> It is true that in <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> the Court was not dealing with the sufficiency of the allegations respecting one or more of the above-described components of probable cause, but merely with a bare overall statement of the affiant that probable cause existed. Further, as the Government notes, our chief, but not sole, emphasis in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> was upon the absence of any evidence communicated by the affiant from which a magistrate could infer that the confidant gathered his evidence from a reliable source. From this, the Government contends that <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i>'s reliability-of-the-informer test is not applicable in full force where, as here, it does seem clear that the sources of the informer's belief, if truthfully reported, were reliable. I think this argument makes too much of the circumstances of our previous cases. The central point of the discussion of probable cause in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> is, as perhaps more precisely emphasized by our explicit twin holdings in <i>Spinelli,</i> see <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#416" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 416</a></span>, that the two elements necessary to establish the informer's trustworthinessnamely, that the tip relayed to the magistrate be both truthful and reliableare analytically severable. It is not possible to argue that since certain information, if true, would be trustworthy, therefore, it must be true. The possibility remains that the information might have been fabricated. This is why our cases require that there be a reasonable basis for crediting the accuracy of the observation related in the tip. In short, the requirement that the magistrate independently assess the probable credibility of the informant does not vanish where the source of the tip indicates that, if true, it is trustworthy.</p>
<p>This is not to say, however, that I think the fact of asserted personal observation can never play a role in determining whether that observation actually took place. I can perceive at least two ways in which, in circumstances <span class="star-pagination">*593</span> similar to those of this case, that information might be taken to bear upon the informer's credibility, as well as upon the reliability of his sources of information. For example, to the extent that the informant is somehow responsible to the affiant, the fact of asserted personal observation might be of some value to a magistrate in assessing the informer's credibility. In such circumstances, perhaps a magistrate could conclude that where the confidant claimed to speak from personal knowledge it is somewhat less likely that the informant was falsifying his report because, if the search yields no fruit, when called to account he would be unable to explain this away by impugning the veracity or reliability of his sources. However, no such relationship is revealed in this case.</p>
<p>Additionally, it might be of significance that the informant had given a more than ordinarily detailed description of the suspect's criminal activities. Although this would be more probative of the reliability of the information, it might also permissibly lead a magistrate, in an otherwise close case, to credit the accuracy of the account as well. I do not believe, however, that in this instance the relatively meager allegations of this character are, standing alone, enough to satisfy the credibility requirement essential to the sufficiency of this probable-cause affidavit. Reading this aspect of the affidavit in a not unduly circumspect manner, the allegations are of a character that would readily occur to a person prone to fabricate. To hold that this aspect of the affidavit, without more, would enable "a man of reasonable caution," <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#55" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 55</a></span> (1967), to conclude that there was adequate reason to believe the informant credible would open the door to the acceptance of little more than florid affidavits as justifying the issuance of search warrants.</p>
<p></p>
<h2>
<span class="star-pagination">*594</span> C</h2>
<p>Some members of the Court would reverse the judgment below on the grounds that the magistrate might properly have credited the informant's assertions because they confessed to the commission of a crime. This rationale is advanced notwithstanding the Government's failure even to suggest it.</p>
<p>Had this argument been pressed upon us, I would find it difficult to accept. First, the analogy to the hearsay exception is quite tenuous. The federal rule, although it is often criticized, is that declarations against penal interest do not fall within this exception. <i>Donnelly</i> v. <i>United States,</i> <span class="citation" data-id="97847"><a href="/opinion/97847/donnelly-v-united-states/" aria-description="Citation for case: Donnelly v. United States">228 U. S. 243</a></span> (1913). Moreover, because it has been thought that such statements should be relied upon by factfinders only when necessity justifies it, the rule universally requires a showing that the declarant cannot be produced personally before the trier of fact, C. McCormick, Evidence §§ 253, 257 (1954), an element not shown to be present here. See Part V, <i>infra.</i> Finally, we have not found any instance of the application of this rule where the witness declined to reveal to the trier of fact the identity of the declarant, presumably because without this knowledge it cannot be readily assumed that the declarant might have had reason to suspect the use of the statement would do him harm. Thus, while strict rules of evidence certainly do not govern magistrates' assessments of probable cause, it would require a rather extensive relaxation of them to permit reliance on this factor. And these rules cannot be completely relaxed, of course, since the basic thrust of <i>Spinelli, Aguilar, Nathanson, Whiteley,</i> and <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello, supra,</a></span></i> is to prohibit the issuance of warrants upon mere uncorroborated hearsay. The simple statement by an affiant that an unspecified individual told the affiant that he and another had committed a <span class="star-pagination">*595</span> crime, where offered to prove the complicity of the third party, is little, if any, more than that.</p>
<p>Secondly, the rationale for this exception to the hearsay rule is that the fact that the declaration was against the speaker's self-interest tends to indicate that its substance is accurate. 5 J. Wigmore, Evidence § 1457 (3d ed. 1940). But where the declarant is also a police informant it seems at least as plausible to assume, without further enlightenment either as to the Government's general practice or as to the particular facts of this case, that the declarant-confidant at least believed he would receive absolution from prosecution for his confessed crime in return for his statement. (This, of course, would not be an objection where the declarant is not also the informant. See <i>Spinelli, supra,</i> at 425 (WHITE, J., concurring).) Thus, some showing that the informant did not possess illusions of immunity might well be essential.</p>
<p>Thirdly, the effect of adopting such a rule would be to encourage the Government to prefer as informants participants in criminal enterprises rather than ordinary citizens, a goal the Government specifically eschews in its brief in this case upon the explicit premise that such persons are often less reliable than those who obey the law. Brief for the United States 14.</p>
<p>In short, I am inclined to the view, although I would not decide the question here, that magistrates may not properly predicate a determination that an unnamed confidant is credible upon the bare fact that by giving information he also confessed to having committed a crime. More importantly at this juncture, it seems to me quite clear that no such rule should be injected into our federal jurisprudence in the absence of any representation by the Government that the factual assumptions underlying it do, indeed, comport with reality, and in the face of the Government's apparent explicit assertion, in this very <span class="star-pagination">*596</span> case, that those able to supply information sufficient to establish probable cause under such a new rule would tend to be less reliable than those who cannot. The necessity for this haste to embrace such a speculative theory, without any argument from those who will be affected by it, wholly escapes me.</p>
<p></p>
<h2>IV</h2>
<p>Finally, it is argued that even if the tip plus the affiant's assertion that the informant was "prudent" did not provide a reasonable basis for the magistrate's conclusion that the confidant was credible, two other factors would have sufficed. First, at some time in the past four or more years, in an abandoned house "under Harris' control," the local constable had located "a sizeable stash of illicit whiskey." While an assertion of "prior events within the affiant's own knowledge . . . indicating that the defendant had previously trafficked in contraband," <i>ante,</i> at 581, admittedly did not appear in the affidavit held insufficient in <i>Spinelli,</i> this hardly distinguishes that case in any purposeful manner. Surely, it cannot seriously be suggested that, once an individual has been convicted of bootlegging, any anonymous phone caller who states he has just personally witnessed another illicit sale (up to four years later) by that individual provides federal agents with probable cause to search the suspect's home. I can only conclude that this argument is a make-weight, intended to avoid the necessity of calling for an outright overruling of <i>Spinelli.</i></p>
<p>Secondly, the claim is made that a magistrate could conclude the confidant here was credible because the agent had "received numerous information from all types of persons as to [respondent's] activities." To rely on this factor alone, of course, is flatly inconsistent with <i>Spinelli,</i> where we held that "the allegation that Spinelli was `known' to the affiant and to other federal and local <span class="star-pagination">*597</span> law enforcement officers as a gambler and an associate of gamblers is but a bald and unilluminating assertion of suspicion that is entitled to no weight in appraising the magistrate's decision." <i>Spinelli, supra,</i> at 414. In the instant case, the affiant did not purport to "know" respondent was a dealer in illicit whiskey, nor did he identify the source of his information to that effect.</p>
<p>Nevertheless, the contention is advanced that this aspect of <i>Spinelli</i> had "no support in our prior cases, logic, or experience," <i>ante,</i> at 583, and thus should be discarded. However, <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> held that "[m]ere affirmance of belief or suspicion is not enough" to establish probable cause for issuance of a warrant to search a private dwelling. <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#47" aria-description="Citation for case: Nathanson v. United States">290 U. S., at 47</a></span>. It is argued that <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> "was limited to holding that reputation, <i>standing alone,</i> was insufficient." <i>Ante,</i> at 582. But this is the precise problem hereonly the respondent's reputation has been seriously invoked to establish the credibility of the informant, an element of probable cause entirely severable from the requirement that the confidant's source be reliable. See Parts I and III of this opinion.</p>
<p>A narrower view of <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> is said to be confirmed by reading <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949), to have "held proper the assertion of the searching officer that he had previously arrested the defendant for a similar offense and that the defendant had a reputation for hauling liquor." <i>Ante,</i> at 582. But <i><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span></i> itself was very carefully limited to situations involving the arrest of those driving moving vehicles, <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States">338 U. S., at 174, 176-177</a></span>, a problem that has typically been treated as <i>sui generis</i> by this Court. Further, the Court in <i><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span></i> specifically held the arrest valid "[w]holly apart from [the agent's] knowledge that [the suspect] bore the general reputation of being engaged in liquor running." <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#170" aria-description="Citation for case: Brinegar v. United States"><i>Id.,</i> at 170</a></span>. While it is true that <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 271</a></span> (1960), cites the fact that the informant's <span class="star-pagination">*598</span> "story was corroborated by other sources of information," the opinion nowhere suggests that this factor, standing alone, would have been sufficient to enable a magistrate to assess the confidant's reliability. At least equal emphasis was placed upon the informant's previously proved veracity and his tangible proof of actual observation of the illegal activity.</p>
<p>Thus, I conclude that <i>Spinelli</i> and <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span>,</i> without contradiction, stand for the proposition that the magistrate could not establish the likely veracity of the unidentified informant on the grounds that his story coincided, in unspecified particulars, with rumors circulated by unknown third parties. I am not certain what is meant by the claim that such a rule of law is illogical. It would, indeed, be illogical to argue that the agent could not have relied upon information as to respondent's reputation that he deemed credible and reliable in concluding that the informant had likely told the truth. But it was not the agent's task to determine whether a search warrant should issue. This was the magistrate's responsibility. As to the magistrate, I confess that I do not comprehend, where the issue is whether the confidant is to be believed, how the agent's assertion that he had "received numerous information from all types of persons as to [respondent's] activities," can, as a matter of logic or experience, be accurately described as other than "a bald and unilluminating assertion of suspicion." It is, at best, a conclusory statement that respondent had a deserved reputation as a dealer in illicit whiskey. The Fourth Amendment, I repeat, requires that such conclusions be drawn, from the underlying facts and circumstances, by the magistrate, not the agent.</p>
<p></p>
<h2>V</h2>
<p>The Government has earnestly protested that the result below, if permitted to stand, will seriously hamper the <span class="star-pagination">*599</span> enforcement of the federal criminal law. It is said that if this affidavit is insufficient to support the issuance of a search warrant, it will be extremely difficult to meet the Fourth Amendment's standards where the informer, although apparently quite credible, has never before given accurate information to law enforcement officers, especially where he, or the agent, is unwilling to have the informant's identity disclosed. It would, indeed, be anomalous if the Fourth Amendment dictated such results, for it surely was never intended as a hindrance to fair, vigorous law enforcement. Further, I think there is much truth in the Government's supporting assertion that the ordinary citizen who has never before reported a crime to the police may, in fact, be more reliable than one who supplies information on a regular basis. "The latter is likely to be someone who is himself involved in criminal activity or is, at least, someone who enjoys the confidence of criminals." Government's Brief 14.<sup>[5]</sup></p>
<p>I do not, however, share the Government's concern that a judgment of affirmance would have such a constricting effect on legitimate federal law enforcement. For example, it would seem that such informers could often be brought before the magistrate where he could assess their credibility for himself. We cannot assume that the ordinary law-abiding citizen has qualms about this sort of cooperation with law enforcement officers. And I do not understand the Government to be asserting <span class="star-pagination">*600</span> that effective law enforcement will often dictate that the identity of informants be kept secret from federal magistrates themselves. Moreover, it will always be open to the officer to seek corroboration of the tip.</p>
<p>Beyond these considerations, I do not understand why a federal agent, who has determined a confidant to be "reliable," "credible," or "prudent" cannot lay before the magistrate the grounds upon which he based that judgment. I would not hold that a magistrate's determination that an informer is "prudent" is insufficient to support the issuance of a warrant. To the contrary, I would only insist that this judgment be that of the magistrate, not the law enforcement officer who seeks the warrant. Without violating the confidences of his source, the agent surely could describe for the magistrate such things as the informer's general background, employment, personal attributes that enable him to observe and relate accurately, position in the community, reputation with others, personal connection with the suspect, any circumstances which suggest the probable absence of any motivation to falsify, the apparent motivation for supplying the information, the presence or absence of a criminal record or association with known criminals, and the like.</p>
<p></p>
<h2>VI</h2>
<p>This affidavit is barren of anything that enabled the magistrate to judge for himself of the credibility of the informant. We should not countenance the issuance of a search warrant by a federal magistrate upon no more evidence than that presented here. A person who has not been shown to possess any of the common attributes of credibility, whose name cannot be disclosed to a magistrate, and whose information has not been corroborated is precisely the sort of informant whose tip should not be the sole basis for the issuance of a warrant, if the constitutional command that "no Warrants shall issue, but <span class="star-pagination">*601</span> upon probable cause" is to be respected. And the assertion that such a person may be believed where he confesses that he is a criminal or where his statements dovetail with other, unspecified rumors carries its own refutation. With all respect, such an analysis bespeaks more a firm hostility to <i>Aguilar, Nathanson,</i> and <i>Spinelli</i> than a careful judgment as to the principles those cases reflect. Despite all its surface detail, this affidavit cannot be sustained without cutting deeply into the core requirement of the Fourth Amendment that search warrants cannot issue except upon the independent finding of a neutral magistrate that probable cause exists.</p>
<p>For these reasons, I dissent.</p>
<h2>NOTES</h2>
<p>[*]  We reject the contention of respondent that the informant's observations were too stale to establish probable cause at the time the warrant was issued. The informant reported having purchased whiskey from respondent "within the past 2 weeks," which could well include purchases up to the date of the affidavit. Moreover, these recent purchases were part of a history of purchases over a two-year period. It was certainly reasonable for a magistrate, concerned only with a balancing of probabilities, to conclude that there was a reasonable basis for a search.</p>
<p>[1]  Of course where, as here, the affiant provides information in addition to the informant's tip, the magistrate could alternatively find probable cause, without examining the tip, if he can conclude that (a) the affiant is probably telling the truth and (b) the affidavit apart from the tip is sufficiently informative to establish probable cause. See <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#414" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410, 414</a></span> (1969). Concededly, this latter element is not present here. Government's Brief 16. Without crediting the tip, the affidavit is insufficient.</p>
<p>[2]  <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> and <i><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span></i> each involved an arrest warrant rather than a search warrant, but the analysis required to determine the validity of either is basically the same.</p>
<p>[3]  The Government makes brief reference to the assertion that the informant's verbal statement to the affiant was "sworn." Government's Brief 13 n. 2. I do not see how this affects the case. Surely there is no reason to suspect that this indicates the confidant anticipated potential perjury proceedings if he were subsequently proved a liar. Nor does that assertion reveal, in any meaningful sense, what sort of relationship this might have reflected or created between the agent and his informer.</p>
<p>[4]  The Court of Appeals in reversing respondent's conviction stated that "[t]he allegation that [the informant] is a `prudent person' signifies that he is circumspect in the conduct of his affairs, but reveals nothing about his credibility." <span class="citation" data-id="285442"><a href="/opinion/285442/united-states-v-roosevelt-hudson-harris/#797" aria-description="Citation for case: United States v. Roosevelt Hudson Harris">412 F. 2d 796, 797-798</a></span>. I consider this a too restrictive construction of the affidavit and cannot accept that aspect of the reasoning of the Court of Appeals.</p>
<p>[5]  Of course, the magistrate was presented no evidence that this is, in fact, such a case. Indeed, the very allegations in the affidavit to the effect that the informant here had been a frequent purchaser from respondent would suggest that he "is, at least, someone who enjoys the confidence of criminals." The Government's argument, as I understand it, is that the affidavit in this case is typical of those that can be produced by agents who rely on first-time informers not bound up themselves in criminal activity. As I point out below, if this had been the situation here, and that fact had been communicated to the magistrate, this would be a very different case.</p>

</div>
```

---
