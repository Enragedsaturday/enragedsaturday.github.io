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

## GROUP: content/cases/United States v. Chadwick.md  (`case`, 8 assertions)

### content_page

```
---
title: "United States v. Chadwick"
type: case
citation: "433 U.S. 1 (1977)"
parallel_cite: "97 S. Ct. 2476; 53 L. Ed. 2d 538"
neutral_cite: 1977 U.S. LEXIS 133
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-06-21
docket: 75-1721
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 1977-06-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Chadwick
  varies_by_point: true
  scope_note: "The Chadwick-Sanders distinction — that luggage/containers carry a high REP demanding a warrant even when connected to a car — was collapsed in the automobile context by California v. Acevedo, which lets police search a container in a vehicle on PC alone. Chadwick's core (property reduced to exclusive police control, no exigency, needs a warrant) survives outside the auto-container setting."
  point_overrides:
    - point: legacy-limited-united-states-v-chadwick
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: California v. Acevedo
          cluster_id: 112608
          cite: 500 U.S. 565
          field_ii: limited
      scope_note: "The Chadwick-Sanders distinction — that luggage/containers carry a high REP demanding a warrant even when connected to a car — was collapsed in the automobile context by California v. Acevedo, which lets police search a container in a vehicle on PC alone. Chadwick's core (property reduced to exclusive police control, no exigency, needs a warrant) survives outside the auto-container setting."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109714/united-states-v-chadwick/"
  cluster_id: 109714
  opinion_id: 9426913
  identity_checked: true
homes:
  - page: "[[Searching Effects and Containers]]"
    role: "Key — Anchor"
  - page: "[[SIA Persons]]"
    role: "Related (cross-doctrine)"
  - page: "[[Automobile Exception]]"
    role: "Related (limited by Acevedo for a container in a car)"
related: ["[[California v. Acevedo]]", "[[United States v. Ross]]", "[[Chambers v. Maroney]]", "[[Chimel v. California]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "containers", "luggage", "search-incident-to-arrest", "warrant-requirement"]
holding: "Luggage/containers carry a high expectation of privacy; once seized and reduced to exclusive police control with no exigency, a footlocker may not be searched without a warrant, and the search is not incident to arrest."
lake:
  record_id: United States v. Chadwick
  status: verified
  projected_at: 2026-07-09
---

# United States v. Chadwick

*433 U.S. 1 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal agents had probable cause to believe a 200-pound double-locked footlocker shipped by train contained marijuana. After Chadwick and his confederates picked it up and loaded it into the trunk of a waiting car, agents arrested them and seized the footlocker. More than an hour later, at the federal building and with the footlocker under the agents' exclusive control, they opened and searched it without a warrant and found the marijuana.

## Issue
Whether federal agents who have lawfully seized a footlocker incident to arrest, and reduced it to their exclusive control, may search it without a warrant when no [[Exigent Circumstances and Hot Pursuit|exigency]] exists.

## Rule
No. Personal luggage carries a high expectation of privacy that the warrant requirement protects: "By placing personal effects inside a double-locked footlocker, respondents manifested an expectation that the contents would remain free from public examination. . . . There being no exigency, it was unreasonable for the Government to conduct this search without the safeguards a judicial warrant provides." — 433 U.S. at 11. ^pin-11

The vehicle's diminished privacy does not extend to luggage: "a person's expectations of privacy in personal luggage are substantially greater than in an automobile." — *Id.* at 13. ^pin-13

Nor is the [[Search Incident to Arrest|search incident to arrest]] once the property is secured: "Once law enforcement officers have reduced luggage or other personal property not immediately associated with the person of the arrestee to their exclusive control, and there is no longer any danger that the arrestee might gain access to the property to seize a weapon or destroy evidence, a search of that property is no longer an incident of the arrest." — [*Id.* at 15](https://www.courtlistener.com/opinion/109714/united-states-v-chadwick/#:~:text=Once%20law%20enforcement%20officers%20have). ^pin-15

## Application
The footlocker's brief contact with Chadwick's car did not make this an automobile search, and its diminished-privacy rationale did not apply to luggage. Once agents seized the footlocker and moved it to the federal building under their exclusive control, there was no danger of removal or destruction of evidence, so no [[Exigent Circumstances and Hot Pursuit|exigency]] justified bypassing a magistrate; and because the search came more than an hour after the agents gained exclusive control and the arrestees were securely in custody, it could not be justified as incident to the arrest.

## Conclusion
The warrantless search was unreasonable; suppression was affirmed. The Warrant Clause draws the line at the point where seized property comes under the exclusive dominion of police authority and no [[Exigent Circumstances and Hot Pursuit|exigency]] is shown.

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Limited by** [[California v. Acevedo]] — Acevedo collapsed the *Chadwick*/*[[Arkansas v. Sanders]]* container distinction **in the automobile context**, holding that police with probable cause may search a container located in a vehicle without a warrant. *Chadwick*'s core teaching — that luggage and other personal effects reduced to exclusive police control with no [[Exigent Circumstances and Hot Pursuit|exigency]] require a warrant — remains the rule outside that auto-container setting.

## Appears on
- [[Automobile Exception]] — *Key — Limiting / Historical*
- [[SIA Persons]] — *Related (cross-doctrine)*

## Sources
- *United States v. Chadwick*, 433 U.S. 1 (1977) — https://www.courtlistener.com/opinion/109714/united-states-v-chadwick/ — pinpoints: 11, 13, 15.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6edf985357e7ff5b", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "433 U.S. 1 (1977)", "court": "U.S. Supreme Court", "neutral_cite": "1977 U.S. LEXIS 133", "official_citation_present": true, "parallel_cite": "97 S. Ct. 2476; 53 L. Ed. 2d 538", "title": "United States v. Chadwick", "year": "1977"}}
{"assertion_id": "3f8e84be32cc7b02", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Luggage/containers carry a high expectation of privacy; once seized and reduced to exclusive police control with no exigency, a footlocker may not be searched without a warrant, and the search is not incident to arrest.", "title": "United States v. Chadwick"}}
{"assertion_id": "cba4f4d7c8363e31", "dimension": "support", "kind": "home_role", "locator": {"home": "Searching Effects and Containers"}, "payload": {"home": "Searching Effects and Containers", "role": "Key — Anchor", "title": "United States v. Chadwick"}}
{"assertion_id": "f14a0a79a7b1d597", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Persons"}, "payload": {"home": "SIA Persons", "role": "Related (cross-doctrine)", "title": "United States v. Chadwick"}}
{"assertion_id": "f747e881df323a44", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Related (limited by Acevedo for a container in a car)", "title": "United States v. Chadwick"}}
{"assertion_id": "3ab0f9c3ebdb2ef9", "dimension": "treatment", "kind": "treatment_override", "locator": {"point": "legacy-limited-united-states-v-chadwick"}, "payload": {"by": [{"cite": "500 U.S. 565", "cluster_id": "112608", "field_ii": "limited", "name": "California v. Acevedo"}], "field_i_validity": "caution", "point": "legacy-limited-united-states-v-chadwick", "point_label": "Legacy limited treatment point", "s3_binding_status": "provisional", "title": "United States v. Chadwick"}}
{"assertion_id": "47581e4d15ab864a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1977-06-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Chadwick", "field_i_validity": "caution", "scope_note": "The Chadwick-Sanders distinction — that luggage/containers carry a high REP demanding a warrant even when connected to a car — was collapsed in the automobile context by California v. Acevedo, which lets police search a container in a vehicle on PC alone. Chadwick's core (property reduced to exclusive police control, no exigency, needs a warrant) survives outside the auto-container setting.", "title": "United States v. Chadwick", "varies_by_point": "true"}}
{"assertion_id": "890afc06d667c86e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Chadwick"}}
```

### lake record — United States v. Chadwick

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Chadwick",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Chadwick",
    "case_name_short": "Chadwick",
    "case_name_full": "UNITED STATES v. CHADWICK Et Al.",
    "input_case_name": "United States v. Chadwick",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-06-21",
    "year": 1977,
    "docket": "75-1721",
    "cluster_id": 109714,
    "lead_opinion_id": 9426913,
    "sibling_ids": [
      109714,
      9426913,
      9426914,
      9426915
    ],
    "absolute_url": "/opinion/109714/united-states-v-chadwick/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "433 U.S. 1",
      "volume": "433",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 2476",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "2476",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 L. Ed. 2d 538",
        "volume": "53",
        "reporter": "L. Ed. 2d",
        "page": "538",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 133",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "133",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "433 U.S. 1",
        "volume": "433",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 2476",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "2476",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 L. Ed. 2d 538",
        "volume": "53",
        "reporter": "L. Ed. 2d",
        "page": "538",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 133",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "133",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "433 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "433 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-11",
      "page": null,
      "quote": "--- # United States v. Chadwick *433 U.S. 1 (1977)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **limited** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal agents had probable cause to believe a 200-pound double-locked footlocker shipped by train contained marijuana. After Chadwick and his confederates picked it up and loaded it into the trunk of a waiting car, agents arrested them and seized the footlocker. More than an hour later, at the federal building and with the footlocker under the agents' exclusive control, they opened and searched it without a warrant and found the marijuana. ## Issue Whether federal agents who have lawfully seized a footlocker incident to arrest, and reduced it to their exclusive control, may search it without a warrant when no exigency exists. ## Rule No. Personal luggage carries a high expectation of privacy that the warrant requirement protects:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-13",
      "page": null,
      "quote": "a person's expectations of privacy in personal luggage are substantially greater than in an automobile.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-15",
      "page": null,
      "quote": "Once law enforcement officers have reduced luggage or other personal property not immediately associated with the person of the arrestee to their exclusive control, and there is no longer any danger that the arrestee might gain access to the property to seize a weapon or destroy evidence, a search of that property is no longer an incident of the arrest.",
      "star_marker": "15",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 28915,
      "fragment": "#:~:text=Once%20law%20enforcement%20officers%20have",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "1977-06-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Chadwick",
    "varies_by_point": true,
    "scope_note": "The Chadwick-Sanders distinction \u2014 that luggage/containers carry a high REP demanding a warrant even when connected to a car \u2014 was collapsed in the automobile context by California v. Acevedo, which lets police search a container in a vehicle on PC alone. Chadwick's core (property reduced to exclusive police control, no exigency, needs a warrant) survives outside the auto-container setting.",
    "point_overrides": [
      {
        "point": "legacy-limited-united-states-v-chadwick",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "California v. Acevedo",
            "cluster_id": 112608,
            "cite": "500 U.S. 565",
            "field_ii": "limited"
          }
        ],
        "scope_note": "The Chadwick-Sanders distinction \u2014 that luggage/containers carry a high REP demanding a warrant even when connected to a car \u2014 was collapsed in the automobile context by California v. Acevedo, which lets police search a container in a vehicle on PC alone. Chadwick's core (property reduced to exclusive police control, no exigency, needs a warrant) survives outside the auto-container setting."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "California v. Acevedo",
          "cluster_id": 112608,
          "cite": "500 U.S. 565",
          "field_ii": "limited"
        },
        "field_ii": "limited",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:limited"
      },
      {
        "citing_case": {
          "name": "State of Indiana v. Justin Crager",
          "cluster_id": 4547157,
          "cite": [
            "113 N.E.3d 657"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chad Camou",
          "cluster_id": 2759861,
          "cite": [
            "773 F.3d 932",
            "2014 U.S. App. LEXIS 23347",
            "2014 WL 6980135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Riley v. Cal. United States",
          "cluster_id": 2680439,
          "cite": [
            "189 L. Ed. 2d 430",
            "134 S. Ct. 2473",
            "2014 U.S. LEXIS 4497",
            "82 U.S.L.W. 4558"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jonathan Thomas",
          "cluster_id": 1036878,
          "cite": [
            "726 F.3d 1086",
            "2013 U.S. App. LEXIS 16413",
            "2013 WL 4017239"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane1_negative"
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
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
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
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
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
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rakas v. Illinois",
          "cluster_id": 109953,
          "cite": [
            "58 L. Ed. 2d 387",
            "99 S. Ct. 421",
            "439 U.S. 128",
            "1978 U.S. LEXIS 2452"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ross",
          "cluster_id": 110719,
          "cite": [
            "72 L. Ed. 2d 572",
            "102 S. Ct. 2157",
            "456 U.S. 798",
            "1982 U.S. LEXIS 18",
            "50 U.S.L.W. 4580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mincey v. Arizona",
          "cluster_id": 109905,
          "cite": [
            "57 L. Ed. 2d 290",
            "98 S. Ct. 2408",
            "437 U.S. 385",
            "1978 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Hodari D.",
          "cluster_id": 112579,
          "cite": [
            "113 L. Ed. 2d 690",
            "111 S. Ct. 1547",
            "499 U.S. 621",
            "1991 U.S. LEXIS 2397",
            "91 Cal. Daily Op. Serv. 2893",
            "59 U.S.L.W. 4335",
            "91 Daily Journal DAR 4665"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Belton",
          "cluster_id": 110559,
          "cite": [
            "69 L. Ed. 2d 768",
            "101 S. Ct. 2860",
            "453 U.S. 454",
            "1981 U.S. LEXIS 13"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
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
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
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
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Brown",
          "cluster_id": 110901,
          "cite": [
            "75 L. Ed. 2d 502",
            "103 S. Ct. 1535",
            "460 U.S. 730",
            "1983 U.S. LEXIS 143",
            "51 U.S.L.W. 4361"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Horton v. California",
          "cluster_id": 112448,
          "cite": [
            "110 L. Ed. 2d 112",
            "110 S. Ct. 2301",
            "496 U.S. 128",
            "1990 U.S. LEXIS 2937"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Rodriguez",
          "cluster_id": 112475,
          "cite": [
            "111 L. Ed. 2d 148",
            "110 S. Ct. 2793",
            "497 U.S. 177",
            "1990 U.S. LEXIS 3295",
            "58 U.S.L.W. 4892"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
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
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rawlings v. Kentucky",
          "cluster_id": 110326,
          "cite": [
            "65 L. Ed. 2d 633",
            "100 S. Ct. 2556",
            "448 U.S. 98",
            "1980 U.S. LEXIS 142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
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
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Maryland",
          "cluster_id": 110118,
          "cite": [
            "61 L. Ed. 2d 220",
            "99 S. Ct. 2577",
            "442 U.S. 735",
            "1979 U.S. LEXIS 134"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jimeno",
          "cluster_id": 112595,
          "cite": [
            "114 L. Ed. 2d 297",
            "111 S. Ct. 1801",
            "500 U.S. 248",
            "1991 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
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
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oliver v. United States",
          "cluster_id": 111146,
          "cite": [
            "80 L. Ed. 2d 214",
            "104 S. Ct. 1735",
            "466 U.S. 170",
            "1984 U.S. LEXIS 55",
            "52 U.S.L.W. 4425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Bertine",
          "cluster_id": 111788,
          "cite": [
            "93 L. Ed. 2d 739",
            "107 S. Ct. 738",
            "479 U.S. 367",
            "1987 U.S. LEXIS 286",
            "55 U.S.L.W. 4105"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
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
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
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
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Birchfield v. N. Dakota. William Robert Bernard",
          "cluster_id": 3216497,
          "cite": [
            "579 U.S. 438",
            "195 L. Ed. 2d 560",
            "2016 U.S. LEXIS 4058",
            "136 S. Ct. 2160"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marshall v. Barlow's, Inc.",
          "cluster_id": 109866,
          "cite": [
            "56 L. Ed. 2d 305",
            "98 S. Ct. 1816",
            "436 U.S. 307",
            "1978 U.S. LEXIS 26",
            "8 Envtl. L. Rep. (Envtl. Law Inst.) 20434",
            "6 OSHC (BNA) 1571"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109714 OR 9426913 OR 9426914 OR 9426915) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTk5ODM2ODAwMDAwJnM9MTM4NTc2NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109714+OR+9426913+OR+9426914+OR+9426915%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      },
      "lane2_top_cited": {
        "query": "cites:(109714 OR 9426913 OR 9426914 OR 9426915)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NDImcz0xMTAxMDAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109714+OR+9426913+OR+9426914+OR+9426915%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109714 OR 9426913 OR 9426914 OR 9426915)",
        "reviewed": 19,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 19,
        "triage_read": 0,
        "triage_snippet_classified": 19
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109714 OR 9426913 OR 9426914 OR 9426915)",
    "indexed_citing_opinions": 1642,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109714,
        "count": 1488,
        "count_source": "search"
      },
      {
        "opinion_id": 9426913,
        "count": 202,
        "count_source": "search"
      },
      {
        "opinion_id": 9426914,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426915,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2561,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-chadwick.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyNTc4NjImcz05Mzk3NDYwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109714+OR+9426913+OR+9426914+OR+9426915%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109714,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 106287,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 108099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 108894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 108995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 109332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 292608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 294420,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 305845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 312363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 317229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 319326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 325005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 326798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 328838,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 334451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 335388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 339773,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 340781,
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
    "date_created": "2026-07-05T23:06:52Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:07:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:07:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:07:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Chadwick

```
<opinion type="majority">
<author id="b31-5">MR. Chief Justice Burger</author>
<p id="Azh">delivered the opinion of the Court.</p>
<p id="b31-6">We granted certiorari in this case to decide whether a search warrant is required before federal agents may open a locked footlocker which they have lawfully seized at the time of the arrest of its owners, when there is probable cause to believe the footlocker contains contraband.</p>
<p id="b31-7">(1)</p>
<p id="b31-8">On May 8, 1973, Amtrak railroad officials in San Diego observed respondents Gregory Machado and Bridget Leary load a brown footlocker onto a train bound for Boston. Their suspicions were aroused when they noticed that the trunk was unusually heavy for its size, and that it was leaking talcum powder, a substance often used to mask the odor of marihuana or hashish. Because Machado matched a profile used to spot drug traffickers, the railroad officials reported these circumstances to federal agents in San Diego, who in turn relayed the information, together with detailed descriptions of Machado and the footlocker, to their counterparts in Boston.</p>
<p id="b31-9">When the train arrived in Boston two days later, federal narcotics agents were on hand. Though the officers had not obtained an arrest or search warrant, they had with them a police dog trained to detect marihuana. The agents identified Machado and Leary and kept them under surveillance as they claimed their suitcases and the footlocker, which had been <page-number citation-index="1" label="4">*4</page-number>transported by baggage cart from the train to the departure area. Machado and Leary lifted the footlocker from the baggage cart, placed it on the floor and sat down on it.</p>
<p id="b32-5">The agents then released the dog near the footlocker. Without alerting respondents, the dog signaled the presence of a controlled substance inside. Respondent Chadwick then joined Machado and Leary, and they engaged an attendant to move the footlocker outside to Chadwick’s waiting automobile. Machado, Chadwick, and the attendant together lifted the 200-pound footlocker into the trunk of the car, while Leary waited in'the front seat. At that point, while the trunk of the car was still open and before the car engine had been started, the officers arrested all three. A search disclosed no weapons, but the keys to the footlocker were apparently taken from Machado.</p>
<p id="b32-6">Respondents were taken to the Federal Building in Boston; the agents followed with Chadwick’s car and the footlocker. As the Government concedes, from the moment of respondents’ arrests at about 9 p. m., the footlocker remained under the exclusive control of law enforcement officers at all times. The footlocker and luggage were placed in the Federal Building, where, as one of the agents later testified, “there was no risk that whatever was contained in the footlocker trunk would be removed by the defendants or their associates.” App. 44. The agents had no reason to believe that the footlocker contained explosives or other inherently dangerous items, or that it contained evidence which would lose its value unless the footlocker were opened at once. Facilities were readily available in which the footlocker could have been stored securely; it is not contended that there was any exigency calling for an immediate search.</p>
<p id="b32-7">At the Federal Building an hour and a half after the arrests, the agents opened the footlocker and luggage. They did not obtain respondents’ consent; they did not secure a search warrant. The footlocker was locked with a padlock and a <page-number citation-index="1" label="5">*5</page-number>regular trunk lock. It is unclear whether it was opened with the keys taken from respondent Machado, or by other means. Large amounts of marihuana were found in the footlocker.<footnotemark>1</footnotemark></p>
<p id="b33-5">Respondents were indicted for possession of marihuana with intent to distribute it, in violation of <span class="citation no-link">21 U. S. C. § 841</span> (a) (1), and for conspiracy, in violation of <span class="citation no-link">21 U. S. C. § 846</span>. Before trial, they moved to suppress the marihuana obtained from the footlocker. In the District Court, the Government sought to justify its failure to secure a search warrant under the “automobile exception” of <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970), and as a search incident to the arrests. Holding that “ [warrantless searches are <em>per se </em>unreasonable, subject to a few carefully delineated and limited exceptions,” the District Court rejected both justifications. <span class="citation" data-id="1452588"><a href="/opinion/1452588/united-states-v-chadwick/#771" aria-description="Citation for case: United States v. Chadwick">393 F. Supp. 763, 771</a></span> (Mass. 1975). The court saw the relationship between the footlocker and Chadwick’s automobile as merely coincidental, and held that the double-locked, 200-pound footlocker was not part of “the area from within which [respondents] might gain possession of a weapon or destructible evidence.” <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 763</a></span> (1969).</p>
<p id="b33-6">A divided Court of Appeals for the First Circuit affirmed the suppression of the seized marihuana. The court held that the footlocker had been properly taken into federal custody after respondents’ lawful arrest; it also agreed that the agents had probable cause to believe that the footlocker contained a controlled substance when they opened it. But probable cause alone was held not enough to sustain the warrantless search. <page-number citation-index="1" label="6">*6</page-number>On the premise that warrantless searches are <em>per se </em>unreasonable unless they fall within some established exception to the warrant requirement, the Court of Appeals agreed with the District Court that the footlocker search was not justified either under the “automobile exception” or as a search incident to a lawful arrest.</p>
<p id="b34-5">The Court of Appeals then responded to an argument, suggested by the Government for the first time on appeal, that movable personalty lawfully seized in a public place should be subject to search without a warrant if there exists probable cause to believe it contains evidence of a crime. Conceding that such personalty shares some characteristics of mobility which support warrantless automobile searches, the court nevertheless concluded that a rule permitting a search of personalty on probable cause alone had not yet “received sufficient recognition by the Supreme Court outside the automobile area, or generally, for us to recognize it as a valid exception to the fourth amendment warrant requirement.” <span class="citation" data-id="9462594"><a href="/opinion/334451/united-states-v-joseph-a-chadwick/#781" aria-description="Citation for case: United States v. Joseph A. Chadwick">532 F. 2d 773, 781</a></span> (1976). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./429/814/">429 U. S. 814</a></span> (1976). We affirm.</p>
<p id="b34-6">(2)</p>
<p id="b34-7">In this Court the Government again contends that the Fourth Amendment Warrant Clause protects only interests traditionally identified with the home.<footnotemark>2</footnotemark> Recalling the colonial writs of assistance, which were often executed in searches of private dwellings, the Government claims that the Warrant Clause was adopted primarily, if not exclusively, in response to unjustified intrusions into private homes on the authority of general warrants. The Government argues there is no evidence that the Framers of the Fourth Amendment intended <page-number citation-index="1" label="7">*7</page-number>to disturb the established practice of permitting warrantless searches outside the home, or to modify the initial clause of the Fourth Amendment by making warrantless searches supported by probable cause <em>per se </em>unreasonable.</p>
<p id="b35-5">Drawing on its reading of history, the Government argues that only homes, offices, and private communications implicate interests which lie at the core of the Fourth Amendment. Accordingly, it is only in these contexts that the determination whether a search or seizure is reasonable should turn on whether a warrant has been obtained. In all other situations, the Government contends, less significant privacy values are at stake, and the reasonableness of a government intrusion should depend solely on whether there is probable cause to believe evidence of criminal conduct is present. Where personal effects are lawfully seized outside the home on probable cause, the Government would thus regard searches without a warranty not “unreasonable.”</p>
<p id="b35-6">We do not agree that the Warrant Clause protects only dwellings and other specifically designated locales. As we have noted before, the Fourth Amendment “protects people, not places,” <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967); more particularly, it protects people from unreasonable government intrusions into their legitimate expectations of privacy. In this case, the Warrant Clause makes a significant contribution to that protection. The question, then, is whether a warrantless search in these circumstances was unreasonable.<footnotemark>3</footnotemark></p>
<p id="b35-7">(3)</p>
<p id="b35-8">It cannot be doubted that the Fourth Amendment’s commands grew in large measure out of the colonists’ experience <page-number citation-index="1" label="8">*8</page-number>with the writs of assistance and their memories of the general warrants formerly in use in England. These writs, which were issued on executive rather than judicial authority, granted sweeping power to customs officials and other agents of the King to search at large for smuggled goods. Though the authority to search granted by the writs was not limited to the home, searches conducted pursuant to them often were carried out in private residences. See generally <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481-485</a></span> (1965); <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#724" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, 724-729</a></span> (1961); <em>Frank </em>v. <em>Maryland, </em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360</a></span> (1959).</p>
<p id="b36-5">Although the searches and seizures which deeply concerned the colonists, and which were foremost in the minds of the Framers, were those involving invasions of the home, it would be a mistake to conclude, as the Government contends, that the Warrant Clause was therefore intended to guard only against intrusions into the home. First, the Warrant Clause does not in terms distinguish between searches conducted in private homes and other searches. There is also a strong historical connection between the Warrant Clause and the initial clause of the Fourth Amendment, which draws no distinctions among “persons, houses, papers, and effects” in safeguarding against unreasonable searches and seizures. See <em>United States </em>v. <em>Rabinowits, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#68" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 68</a></span> (1950) (Frankfurter, J., dissenting).</p>
<p id="b36-6">Moreover, if there is little evidence that the Framers intended the Warrant Clause to operate outside the home, there is no evidence at all that they intended to exclude from protection of the Clause all searches occurring outside the home. The absence of a contemporary outcry against war-rantless searches in public places was because, aside from searches incident to arrest, such warrantless searches were not a large issue in colonial America. Thus, silence in the historical record tells us little about the Framers' attitude toward application of the Warrant Clause to the search of respond<page-number citation-index="1" label="9">*9</page-number>ents’ footlocker.<footnotemark>4</footnotemark> What we do know is that the Framers were men who focused on the wrongs of that day but who intended the Fourth Amendment to safeguard fundamental values which would far outlast the specific abuses which gave it birth.</p>
<p id="b37-5">Moreover, in this area we do not write on a clean slate. Our fundamental inquiry in considering Fourth Amendment issues is whether or not a search or seizure is reasonable under all the circumstances. <em>Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967). The judicial warrant has a significant role to play in that it provides the detached scrutiny of a neutral magistrate, which is a more reliable safeguard against improper searches than the hurried judgment of a law enforcement officer “engaged in the often competitive enterprise of ferreting out crime.” <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). Once a lawful search has begun, it is also far more likely that it will not exceed proper bounds when it is done pursuant to a judicial authorization “particularly describing the place to be searched and the persons or things to be seized.” Further, a warrant assures the individual whose property is searched or seized of the lawful authority of the executing officer, his need to search, and the limits of his power to search. <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 532</a></span> (1967).</p>
<p id="b37-6">Just as the Fourth Amendment “protects people, not places,” the protections a judicial warrant offers against erro<page-number citation-index="1" label="10">*10</page-number>neous governmental intrusions are effective whether applied in or out of the home. Accordingly, we have held warrantless searches unreasonable, and therefore unconstitutional, in a variety of settings.<footnotemark>5</footnotemark> A century ago, Mr. Justice Field, speaking for the Court, included within the reach of the Warrant Clause printed matter traveling through the mails within the United States:</p>
<blockquote id="b38-5">“Letters and sealed packages of this kind in the mail are as fully guarded from examination and inspection, except as to their outward form and weight, as if they were retained by the parties forwarding them in their own domiciles. The constitutional guaranty of the right of the people to be secure in their papers against unreasonable searches and seizures extends to their papers, thus closed against inspection, wherever they may be. Whilst in the mail, they can only be opened and examined under like warrant, issued upon similar oath or affirmation, particularly describing the thing to be seized, as is required when papers are subjected to search in one’s own household.” <em>Ex parte Jackson, </em><span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727, 733</a></span> (1878).</blockquote>
<p id="b38-6">We reaffirmed <em>Jackson </em>in <em>United States </em>v. <em>Van Leeuwen, </em><span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S. 249</a></span> (1970), where a search warrant was obtained to open two packages which, on mailing, the sender had declared contained only coins. Judicial warrants have been required for other searches conducted outside the home. <em>E. g., Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967) (electronic interception of conversation in public telephone booth); <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971) (automobile on private <page-number citation-index="1" label="11">*11</page-number>premises); <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span> (1964) (automobile in custody); <em>United States </em>v. <em>Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span> (1961) (hotel room); <em>G. M. Leasing Corp, </em>v. <em>United States, </em><span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338</a></span> (1977) (office); <em>Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364</a></span> (1968) (office). These cases illustrate the applicability of the Warrant Clause beyond the narrow limits suggested by the Government. They also reflect the settled constitutional principle, discussed earlier, that a fundamental purpose of the Fourth Amendment is to safeguard individuals from unreasonable government invasions of legitimate privacy interests,<footnotemark>6</footnotemark> and not simply those interests found inside the four walls of the home. <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span> (1949).</p>
<p id="b39-5">In this case, important Fourth Amendment privacy interests were at stake. By placing personal effects inside a double-locked footlocker, respondents manifested an expectation that the contents would remain free from public examination. No less than one who locks the doors of his home against intruders, one who safeguards his personal possessions in this manner is due the protection of the Fourth Amendment Warrant Clause. There being no exigency, it was unreasonable for the Government to conduct this search without the safeguards a judicial warrant provides.</p>
<p id="b39-6">(4)</p>
<p id="b39-7">The Government does not contend that the footlocker’s brief contact with Chadwick’s car makes this an automobile search, but it is argued that the rationale of our automobile <page-number citation-index="1" label="12">*12</page-number>search cases demonstrates the reasonableness of permitting warrantless searches of luggage; the Government views such luggage as analogous to motor vehicles for Fourth Amendment purposes. It is true that, like the footlocker in issue here, automobiles are “effects” under the Fourth Amendment, and searches and seizures of automobiles are therefore subject to the constitutional standard of reasonableness. But this Court has recognized significant differences between motor vehicles and other property which permit warrantless searches of automobiles in circumstances in which warrantless searches would not be reasonable in other contexts. <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925); <em>Preston </em>v. <em>United States, supra, </em>at 366-367; <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970). See also <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#367" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 367</a></span> (1976).</p>
<p id="b40-5">Our treatment of automobiles has been based in part on their inherent mobility, which often makes obtaining a judicial warrant impracticable. Nevertheless, we have also sustained “warrantless searches of vehicles ... in cases in which the possibilities of the vehicle’s being removed or evidence in it destroyed were remote, if not nonexistent.” . <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 441-442</a></span> (1973); accord, <em>South Dakota </em>v. <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#367" aria-description="Citation for case: South Dakota v. Opperman"><em>Opperman, supra, </em>at 367</a></span>; see <em>Texas </em>v. <em>White, </em><span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/" aria-description="Citation for case: Texas v. White">423 U. S. 67</a></span> (1975); <em>Chambers </em>v. <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney, supra;</a></span> Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967).</p>
<p id="b40-6">The answer lies in the diminished expectation of privacy which surrounds the automobile:</p>
<blockquote id="b40-7">“One has a lesser expectation of privacy in a motor vehicle because its function is transportation and it seldom serves as one’s residence or as the repository of personal effects. ... It travels public thoroughfares where both its occupants and its contents are in plain view.” <em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590</a></span> (1974) (plurality opinion).</blockquote>
<p id="b40-8">Other factors reduce automobile privacy. “All States require <page-number citation-index="1" label="13">*13</page-number>vehicles to be registered and operators to be licensed. States and localities have enacted extensive and detailed codes regulating the condition and manner in which motor vehicles may be operated on public streets and highways.” <em>Cady </em>v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski"><em>Dombrowski, supra, </em>at 441</a></span>. Automobiles periodically undergo official inspection, and they are often taken into police custody in the interests of public safety. <em>South Dakota </em>v. <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#368" aria-description="Citation for case: South Dakota v. Opperman"><em>Opperman, supra, </em>at 368</a></span>.</p>
<p id="b41-5">The factors which diminish the privacy aspects of an automobile do not apply to respondents’ footlocker. Luggage contents are not open to public view, except as a condition to a border entry or common carrier travel; nor is luggage subject to regular inspections and official • scrutiny on a continuing basis. Unlike an automobile, whose primary function is transportation, luggage is intended as a repository of personal effects. In sum, a person’s expectations of privacy in personal luggage are substantially greater than in an automobile.</p>
<p id="b41-6">Nor does the footlocker’s mobility justify dispensing with the added protections of the Warrant Clause. Once the federal agents had seized it at the railroad station and had safely transferred it to the Boston Federal Building under their exclusive control, there was not the slightest danger that the footlocker or its contents could have been removed before a valid search warrant could be obtained.<footnotemark>7</footnotemark> The initial seizure and detention of the footlocker, the validity of which respondents do not contest, were sufficient to guard against any risk that evidence might be lost. With the footlocker safely immobilized, it was unreasonable to undertake the additional and greater intrusion of a search without a warrant.<footnotemark>8</footnotemark></p>
<p id="b42-4"><page-number citation-index="1" label="14">*14</page-number>Finally, the Government urges that the Constitution permits the warrantless search- of any property in the possession of a person arrested in public, so long as there is probable cause to believe that the property contains contraband or evidence of crime. Although recognizing that the footlocker was not within respondents’ immediate control, the Government insists that the search was reasonable because the footlocker was seized contemporaneously with respondents' arrests and was searched as soon thereafter as was practicable. The reasons justifying search in a custodial arrest are quite different. When a custodial arrest is made, there is always some danger that the person arrested may seek to use a weapon, or that evidence may be concealed or destroyed. To safeguard himself and others, and to prevent the loss of evidence, it has been held reasonable for the arresting officer to conduct a prompt, warrantless “search of the arrestee’s person and the area ‘within his immediate control’ — construing that phrase to mean the area from within which he might gain possession of a weapon or destructible evidence.” <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span>. See also <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968).</p>
<p id="b42-5">Such searches may be conducted without a warrant, and they may also be made whether or not there is probable cause to believe that the person arrested may have a weapon or is about to destroy evidence. The potential dangers lurking in <page-number citation-index="1" label="15">*15</page-number>all custodial arrests make warrantless searches of items within the “immediate control” area reasonable without requiring the arresting officer to calculate the probability that weapons or destructible evidence may be involved. <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973); <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra.</a></span> </em>However, warrantless searches of luggage or other property seized at the time of an arrest cannot be justified as incident to that arrest either if the “search is remote in time or place from the arrest,” <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S., at 367</a></span>, or no exigency exists. Once law enforcement officers have reduced luggage or other personal property not immediately associated with the person of the arrestee to their exclusive control, and there is no longer any danger that the arrestee might gain access to the property to seize a weapon or destroy evidence, a search of that property is no longer an incident of the arrest.<footnotemark>9</footnotemark></p>
<p id="b43-5">Here the search was conducted more than an hour after federal agents had gained exclusive control of the footlocker and long after respondents were securely in custody; the search therefore cannot be viewed as incidental to the arrest or as justified by any other exigency. Even though on this record the issuance of a warrant by a judicial officer was reasonably predictable, a line must be drawn. In our view, when no exigency is shown to support the need for an immediate search, the Warrant Clause places the line at the point where the property to be searched comes under the exclusive dominion of police authority. Respondents were therefore entitled to the protection of the Warrant Clause with the <page-number citation-index="1" label="16">*16</page-number>evaluation of a neutral magistrate, before their privacy-interests in the contents of the footlocker were invaded.<footnotemark>10</footnotemark></p>
<p id="AzR">Accordingly, the judgment is</p>
<p id="b44-5">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b33-7"> Marihuana was also found in the suitcases. The Court of Appeals found no adequate justification for the warrantless suitcase search, and suppressed this evidence. Incriminating statements made by respondent Chadwick during the arrest procedure were also suppressed, on the theory that there had not been probable cause to arrest him and that his statements were therefore tainted as the product of an illegal arrest. However, the petition for certiorari draws into question only the footlocker search; consequently, we need not pass on the legality of Chadwick’s arrest or the search of the suitcases.</p>
</footnote>
<footnote label="2">
<p id="b34-8"> The Fourth Amendment provides:</p>
<blockquote id="b34-9">“The right of the people to be secure in their persons, houses, papersj and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”</blockquote>
</footnote>
<footnote label="3">
<p id="b35-9"> In this Court the Government has limited the question presented to “[w]hether a search warrant is required before federal agents may open a locked footlocker that is properly in their possession and that they have probable cause to believe contains contraband.” Accordingly, this case presents no issue of the application of the exclusionary rule.</p>
</footnote>
<footnote label="4">
<p id="b37-7"> The Government’s historical analysis is further undercut by its own arguments. The Government acknowledges that the core values the Fourth Amendment protects are privacy interests. In its view, those privacy interests which should receive the “maximum protection from governmental search or seizure” provided by the Warrant Clause include private oral and electronic communication, “[i]n addition to the home and other structures such as an office or hotel room . . . .” Brief for United States 30. It is not readily apparent how the Government’s contention that the Warrant Clause applies to high privacy areas, both within and without the home, can be reconciled with its earlier contention that judicial warrants are appropriate only for searches conducted within private dwellings.</p>
</footnote>
<footnote label="5">
<p id="b38-7"><em> </em>In circumstances involving noncriminal inventory searches, where probable cause to search is irrelevant, we have recognized "that search warrants are not required, linked as the warrant requirement textually is to the probable-cause concept.” <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span>, 370 n. 5 (1976). This is so because the salutary functions of a warrant simply have no application in that context; the constitutional reasonableness of inventory searches must be determined on other bases.</p>
</footnote>
<footnote label="6">
<p id="b39-8"> This has been settled law in this Court for over 90 years. At least since <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886), we have known that “[i]t is not the breaking of his doors, and the rummaging of his drawers, that constitutes the essence of the offence; but it is the invasion of his indefeasible right of personal security, personal liberty and private property . . . .” <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States"><em>Id., </em>at 630</a></span>.</p>
<p id="b39-9">This is not to say that the Fourth Amendment translates precisely into a constitutional privacy right. See <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#350" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 350-351</a></span> (1967).</p>
</footnote>
<footnote label="7">
<p id="b41-7"> This may often not be the case when automobiles are seized, Absolutely secure storage facilities may not be available, see <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span> (1976); <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973), and the size and inherent mobility of a vehicle malee it susceptible to theft or intrusion by vandals.</p>
</footnote>
<footnote label="8">
<p id="b41-8"> Respondents’ principal privacy interest in the footlocker was, of <page-number citation-index="1" label="14">*14</page-number>course, not in the container itself, which was exposed to public view, but in its contents. A search of the interior was therefore a far greater intrusion into Fourth Amendment values than the impoundment of the footlocker. Though surely a substantial infringement of’respondents’ use and possession, the seizure did not diminish respondents’ legitimate expectation that the footlocker’s contents would remain private.</p>
<p id="b42-7">It was the greatly reduced expectation of privacy in the automobile, coupled with the transportation function of the vehicle, which made the Court in <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span> </em>unwilling to decide whether an immediate search of an automobile, or its seizure and indefinite immobilization, constituted a greater interference with the rights of the owner. This is clearly not the case with locked luggage.</p>
</footnote>
<footnote label="9">
<p id="b43-6"> Of course, there may be other justifications for a warrantless search of luggage taken from a suspect at the time of his arrest; for example, if officers have reason to believe that luggage contains some immediately dangerous instrumentality, such as explosives, it would be foolhardy to transport it to the station house without opening the luggage and dis&gt;arming the weapon. See, <em>e. g., United States </em>v. <em>Johnson, </em><span class="citation" data-id="9458727"><a href="/opinion/305845/united-states-v-alphonse-johnson/#639" aria-description="Citation for case: United States v. Alphonse Johnson">467 F. 2d 630, 639</a></span> (CA2 1972).</p>
</footnote>
<footnote label="10">
<p id="b44-10"> TMike searches of the person, <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973); <em>United States </em>v. <em>Edwards, <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/" aria-description="Citation for case: United States v. Edwards">415 U. S. 800</a></span> </em>(1974), searches of possessions within an arrestee’s immediate control cannot be justified by any reduced expectations of privacy caused by the arrest. Respondents’ privacy interest in the contents of the footlocker was not eliminated simply because they were under arrest.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Wolf v. Colorado.md  (`case`, 5 assertions)

### content_page

```
---
title: "Wolf v. Colorado"
type: case
citation: "338 U.S. 25 (1949)"
parallel_cite: "69 S. Ct. 1359; 93 L. Ed. 2d 1782; 93 L. Ed. 1782"
neutral_cite: 1949 U.S. LEXIS 2079
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1949
date_decided: 1949-06-27
docket: "17, 18"
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: superseded
  as_of_content: 1949-06-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Wolf v. Colorado
  varies_by_point: false
  scope_note: "Wolf's holding that the Fourteenth Amendment does not require the exclusionary rule of the States was overruled on that remedy point by Mapp v. Ohio (1961). Wolf's separate holding incorporating the Fourth Amendment's core against the States survived and was reaffirmed in Mapp."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/104709/wolf-v-colorado/"
  cluster_id: 104709
  opinion_id: 104709
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Historical (overruled by Mapp on remedy)"
related: ["[[Mapp v. Ohio]]", "[[Weeks v. United States]]", "[[Elkins v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "incorporation", "fourteenth-amendment", "overruled", "historical"]
holding: "The Fourth Amendment's core security against arbitrary police intrusion is enforceable against the States through the Fourteenth Amendment's Due Process Clause, but the Weeks exclusionary rule is not itself commanded of the States — a remedy holding later overruled by Mapp v. Ohio."
lake:
  record_id: Wolf v. Colorado
  status: verified
  projected_at: 2026-07-09
---

# Wolf v. Colorado

*338 U.S. 25 (1949)* · U.S. Supreme Court · **Historical** · Treatment: **overruled** *(as of 2026-06-30)* — overruled on remedy by [[Mapp v. Ohio]]
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Wolf was convicted in a Colorado court of conspiracy to commit abortion on evidence (including an appointment book) obtained by a sheriff without a warrant. He argued that the Fourteenth Amendment required a state court to exclude evidence obtained by an unreasonable search and seizure, just as *[[Weeks v. United States]]* required exclusion in federal prosecutions.

## Issue
Whether the Due Process Clause of the Fourteenth Amendment requires a state court to exclude evidence obtained by an unreasonable search and seizure, as the *[[Weeks v. United States|Weeks]]* rule requires in federal court.

## Rule
The Fourth Amendment's core is binding on the States, but its federal exclusionary remedy is not. "The security of one's privacy against arbitrary intrusion by the police—which is at the core of the Fourth Amendment—is basic to a free society. It is therefore implicit in 'the concept of ordered liberty' and as such enforceable against the States through the Due Process Clause." — 338 U.S. at 27–28. ^pin-27

But the *[[Weeks v. United States|Weeks]]* exclusionary rule was a judicially implied remedy, not a constitutional command on the States: "in a prosecution in a State court for a State crime the Fourteenth Amendment does not forbid the admission of evidence obtained by an unreasonable search and seizure." — [*Id.* at 33](https://www.courtlistener.com/opinion/104709/wolf-v-colorado/#:~:text=in%20a%20prosecution%20in%20a). ^pin-33

**This remedy holding was overruled by [[Mapp v. Ohio]] (1961).**

## Application
Because exclusion was an implied federal remedy rather than an essential ingredient of the right enforceable against the States, the Court left the States free to choose other means of enforcing the constitutional guarantee. Colorado's admission of the unlawfully obtained evidence therefore did not deny Wolf due process of law.

## Conclusion
The conviction was affirmed: the Fourteenth Amendment incorporated the substance of the Fourth Amendment against the States but did not, in 1949, compel them to apply the exclusionary rule. **The Court reversed course twelve years later in [[Mapp v. Ohio]], which extended the exclusionary rule to the States and overruled this part of *Wolf*.**

## Treatment & subsequent history
- **Status:** overruled *(as of 2026-06-30)* — **Historical** (tier 6). **Overruled on the remedy holding by [[Mapp v. Ohio]], 367 U.S. 643 (1961)**, which held the exclusionary rule applicable to the States.
- *Wolf*'s incorporation holding — that the Fourth Amendment's core binds the States through the Fourteenth — **survived** and was reaffirmed in *[[Mapp v. Ohio|Mapp]]*. *Wolf* is taught as the foil for the modern rule: it is the case instructors name to explain how *[[Mapp v. Ohio|Mapp]]* came to require state exclusion. Compare [[Elkins v. United States]] (abolishing the silver-platter doctrine the year before *[[Mapp v. Ohio|Mapp]]*).

## Appears on
- [[The Exclusionary Rule]] — *Key — Historical (overruled by Mapp on remedy)*

## Sources
- *Wolf v. Colorado*, 338 U.S. 25 (1949) — https://www.courtlistener.com/opinion/104709/wolf-v-colorado/ — pinpoints: 27–28, 33.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d26d6adc9e81c67a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "338 U.S. 25 (1949)", "court": "U.S. Supreme Court", "neutral_cite": "1949 U.S. LEXIS 2079", "official_citation_present": true, "parallel_cite": "69 S. Ct. 1359; 93 L. Ed. 2d 1782; 93 L. Ed. 1782", "title": "Wolf v. Colorado", "year": "1949"}}
{"assertion_id": "0645b50885266746", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Key — Historical (overruled by Mapp on remedy)", "title": "Wolf v. Colorado"}}
{"assertion_id": "ec7609e28ec74cdd", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Fourth Amendment's core security against arbitrary police intrusion is enforceable against the States through the Fourteenth Amendment's Due Process Clause, but the Weeks exclusionary rule is not itself commanded of the States — a remedy holding later overruled by Mapp v. Ohio.", "title": "Wolf v. Colorado"}}
{"assertion_id": "8628b4591158c951", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1949-06-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Wolf v. Colorado", "field_i_validity": "superseded", "scope_note": "Wolf's holding that the Fourteenth Amendment does not require the exclusionary rule of the States was overruled on that remedy point by Mapp v. Ohio (1961). Wolf's separate holding incorporating the Fourth Amendment's core against the States survived and was reaffirmed in Mapp.", "title": "Wolf v. Colorado", "varies_by_point": "false"}}
{"assertion_id": "ee6d891113d62f65", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Wolf v. Colorado"}}
```

### lake record — Wolf v. Colorado

```json
{
  "schema_version": "s2.v1",
  "record_id": "Wolf v. Colorado",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Wolf v. Colorado",
    "case_name_short": "Wolf",
    "case_name_full": "Wolf v. Colorado",
    "input_case_name": "Wolf v. Colorado",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1949-06-27",
    "year": 1949,
    "docket": "17, 18",
    "cluster_id": 104709,
    "lead_opinion_id": 104709,
    "sibling_ids": [
      104709,
      9420374,
      9420375,
      9420376,
      9420377,
      9420378
    ],
    "absolute_url": "/opinion/104709/wolf-v-colorado/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "338 U.S. 25",
      "volume": "338",
      "reporter": "U.S.",
      "page": "25",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "69 S. Ct. 1359",
        "volume": "69",
        "reporter": "S. Ct.",
        "page": "1359",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 1782",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "1782",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 1782",
        "volume": "93",
        "reporter": "L. Ed.",
        "page": "1782",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1949 U.S. LEXIS 2079",
        "volume": "1949",
        "reporter": "U.S. LEXIS",
        "page": "2079",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "338 U.S. 25",
        "volume": "338",
        "reporter": "U.S.",
        "page": "25",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 S. Ct. 1359",
        "volume": "69",
        "reporter": "S. Ct.",
        "page": "1359",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 1782",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "1782",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1949 U.S. LEXIS 2079",
        "volume": "1949",
        "reporter": "U.S. LEXIS",
        "page": "2079",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 1782",
        "volume": "93",
        "reporter": "L. Ed.",
        "page": "1782",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "338 U.S. 25",
    "official_selection": {
      "court_class": "scotus",
      "selected": "338 U.S. 25",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-27",
      "page": null,
      "quote": "--- # Wolf v. Colorado *338 U.S. 25 (1949)* \u00b7 U.S. Supreme Court \u00b7 **Historical** \u00b7 Treatment: **overruled** *(as of 2026-06-30)* \u2014 overruled on remedy by [[Mapp v. Ohio]] <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Wolf was convicted in a Colorado court of conspiracy to commit abortion on evidence (including an appointment book) obtained by a sheriff without a warrant. He argued that the Fourteenth Amendment required a state court to exclude evidence obtained by an unreasonable search and seizure, just as *Weeks v. United States* required exclusion in federal prosecutions. ## Issue Whether the Due Process Clause of the Fourteenth Amendment requires a state court to exclude evidence obtained by an unreasonable search and seizure, as the *Weeks* rule requires in federal court. ## Rule The Fourth Amendment's core is binding on the States, but its federal exclusionary remedy is not.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-33",
      "page": null,
      "quote": "in a prosecution in a State court for a State crime the Fourteenth Amendment does not forbid the admission of evidence obtained by an unreasonable search and seizure.",
      "star_marker": "33",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 16043,
      "fragment": "#:~:text=in%20a%20prosecution%20in%20a",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "superseded",
    "as_of_content": "1949-06-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Wolf v. Colorado",
    "varies_by_point": false,
    "scope_note": "Wolf's holding that the Fourteenth Amendment does not require the exclusionary rule of the States was overruled on that remedy point by Mapp v. Ohio (1961). Wolf's separate holding incorporating the Fourth Amendment's core against the States survived and was reaffirmed in Mapp.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Mapp v. Ohio",
          "cluster_id": 106285,
          "cite": "367 U.S. 643",
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:overruled"
      },
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 10705828,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane1_negative"
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
        "journal_ref": "Wolf v. Colorado:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Isaac Andrew Baldon III",
          "cluster_id": 4472245,
          "cite": [
            "829 N.W.2d 785",
            "2013 WL 1694553",
            "2013 Iowa Sup. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Armendariz v. State",
          "cluster_id": 1495683,
          "cite": [
            "123 S.W.3d 401",
            "2003 Tex. Crim. App. LEXIS 924",
            "2003 WL 22902856"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Munroe v. Zoning Board of Appeals",
          "cluster_id": 7899534,
          "cite": [
            "261 Conn. 263",
            "802 A.2d 55",
            "2002 Conn. LEXIS 298"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gary Lynn Weaver",
          "cluster_id": 729642,
          "cite": [
            "99 F.3d 1372",
            "1996 WL 648108"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hatcher v. State",
          "cluster_id": 2449969,
          "cite": [
            "916 S.W.2d 643",
            "1996 WL 46937"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 1676406,
          "cite": [
            "912 S.W.2d 227",
            "1995 Tex. Crim. App. LEXIS 115",
            "1995 WL 675559"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane1_negative"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schneckloth v. Bustamonte",
          "cluster_id": 108800,
          "cite": [
            "36 L. Ed. 2d 854",
            "93 S. Ct. 2041",
            "412 U.S. 218",
            "1973 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gideon v. Wainwright",
          "cluster_id": 106545,
          "cite": [
            "9 L. Ed. 2d 799",
            "83 S. Ct. 792",
            "372 U.S. 335",
            "1963 U.S. LEXIS 1942",
            "93 A.L.R. 2d 733",
            "23 Ohio Op. 2d 258"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albright v. Oliver",
          "cluster_id": 112924,
          "cite": [
            "127 L. Ed. 2d 114",
            "114 S. Ct. 807",
            "510 U.S. 266",
            "1994 U.S. LEXIS 1319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clewis v. State",
          "cluster_id": 2462780,
          "cite": [
            "922 S.W.2d 126",
            "1996 Tex. Crim. App. LEXIS 11",
            "1996 WL 37908"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pointer v. Texas",
          "cluster_id": 107014,
          "cite": [
            "13 L. Ed. 2d 923",
            "85 S. Ct. 1065",
            "380 U.S. 400",
            "1965 U.S. LEXIS 1481"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griswold v. Connecticut",
          "cluster_id": 107082,
          "cite": [
            "14 L. Ed. 2d 510",
            "85 S. Ct. 1678",
            "381 U.S. 479",
            "1965 U.S. LEXIS 2282"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duncan v. Louisiana",
          "cluster_id": 107685,
          "cite": [
            "20 L. Ed. 2d 491",
            "88 S. Ct. 1444",
            "391 U.S. 145",
            "1968 U.S. LEXIS 1631",
            "45 Ohio Op. 2d 198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. O'Brien",
          "cluster_id": 107701,
          "cite": [
            "20 L. Ed. 2d 672",
            "88 S. Ct. 1673",
            "391 U.S. 367",
            "1968 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(104709 OR 9420374 OR 9420375 OR 9420376 OR 9420377 OR 9420378) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NDM3MzEyMDAwMDAmcz0zOTU5MTYzJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28104709+OR+9420374+OR+9420375+OR+9420376+OR+9420377+OR+9420378%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      },
      "lane2_top_cited": {
        "query": "cites:(104709 OR 9420374 OR 9420375 OR 9420376 OR 9420377 OR 9420378)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDM1JnM9MTQ5NzAyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28104709+OR+9420374+OR+9420375+OR+9420376+OR+9420377+OR+9420378%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(104709 OR 9420374 OR 9420375 OR 9420376 OR 9420377 OR 9420378)",
        "reviewed": 8,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 8,
        "triage_read": 1,
        "triage_snippet_classified": 7
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(104709 OR 9420374 OR 9420375 OR 9420376 OR 9420377 OR 9420378)",
    "indexed_citing_opinions": 960,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 104709,
        "count": 890,
        "count_source": "search"
      },
      {
        "opinion_id": 9420374,
        "count": 103,
        "count_source": "search"
      },
      {
        "opinion_id": 9420375,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9420376,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9420377,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9420378,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1555,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/wolf-v-colorado.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjYzNTY5MDYmcz00NjU4OTgyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28104709+OR+9420374+OR+9420375+OR+9420376+OR+9420377+OR+9420378%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 104709,
        "cited_id": 89675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 91054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 96885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 104455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3233534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3246119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3307559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3311672,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3312462,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3314804,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3321660,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3412636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3471999,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3484807,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3487094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3529427,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3536208,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3553875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3571966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3580565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3588018,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3594947,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3646527,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3672959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3682031,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3780866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3812264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3827556,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3839135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3842073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3848320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3870663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3907069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3932614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3977442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3980535,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3990360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 4012941,
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
    "date_created": "2026-07-06T04:41:07Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: overruled -> superseded",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:41:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:41:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:41:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Wolf v. Colorado

```
<div>
<center><b><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U.S. 25</a></span> (1949)</b></center>
<center><h1>WOLF<br>
v.<br>
COLORADO.</h1></center>
<center>Nos. 17 and 18.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 19, 1948.</center>
<center>Decided June 27, 1949.</center>
CERTIORARI TO THE SUPREME COURT OF COLORADO.
<p><i>Philip Hornbein,</i> argued the cause for petitioner. With him on the brief were <i>Philip Hornbein, Jr.</i> and <i>Donald M. Shere.</i></p>
<p><i>James S. Henderson,</i> Assistant Attorney General of Colorado, argued the cause for respondent. With him on the brief was <i>H. Lawrence Hinkley,</i> Attorney General.</p>
<p>MR. JUSTICE FRANKFURTER delivered the opinion of the Court.</p>
<p>The precise question for consideration is this: Does a conviction by a State court for a State offense deny the "due process of law" required by the Fourteenth Amendment, solely because evidence that was admitted <span class="star-pagination">*26</span> at the trial was obtained under circumstances which would have rendered it inadmissible in a prosecution for violation of a federal law in a court of the United States because there deemed to be an infraction of the Fourth Amendment as applied in <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>? The Supreme Court of Colorado has sustained convictions in which such evidence was admitted, <span class="citation no-link">117 Col. 279</span>, <span class="citation" data-id="3312462"><a href="/opinion/3317383/wolf-v-people/" aria-description="Citation for case: Wolf v. People">187 P. 2d 926</a></span>; <span class="citation no-link">117 Col. 321</span>, <span class="citation" data-id="3314804"><a href="/opinion/3319666/wolf-v-people/" aria-description="Citation for case: Wolf v. People">187 P. 2d 928</a></span>, and we brought the cases here. <span class="citation multiple-matches"><a href="/c/U.%20S./333/879/">333 U. S. 879</a></span>.</p>
<p>Unlike the specific requirements and restrictions placed by the Bill of Rights (Amendments I to VIII) upon the administration of criminal justice by federal authority, the Fourteenth Amendment did not subject criminal justice in the States to specific limitations. The notion that the "due process of law" guaranteed by the Fourteenth Amendment is shorthand for the first eight amendments of the Constitution and thereby incorporates them has been rejected by this Court again and again, after impressive consideration. See, e. g., <i>Hurtado</i> v. <i>California,</i> <span class="citation" data-id="9417375"><a href="/opinion/91054/hurtado-v-california/" aria-description="Citation for case: Hurtado v. California">110 U. S. 516</a></span>; <i>Twining</i> v. <i>New Jersey,</i> <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78</a></span>; <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span>; <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319</a></span>. Only the other day the Court reaffirmed this rejection after thorough reexamination of the scope and function of the Due Process Clause of the Fourteenth Amendment. <i>Adamson</i> v. <i>California,</i> <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/" aria-description="Citation for case: Adamson v. California">332 U. S. 46</a></span>. The issue is closed.</p>
<p>For purposes of ascertaining the restrictions which the Due Process Clause imposed upon the States in the enforcement of their criminal law, we adhere to the views expressed in <i>Palko</i> v. <i><span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">Connecticut, supra,</a></span></i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319</a></span>. That decision speaks to us with the great weight of the authority, particularly in matters of civil liberty, of a court that included Mr. Chief Justice Hughes, Mr. Justice Brandeis, Mr. Justice Stone and Mr. Justice Cardozo, to name only the dead. In rejecting the suggestion that the Due Process Clause incorporated the original Bill of Rights, Mr. Justice Cardozo reaffirmed on behalf of that <span class="star-pagination">*27</span> Court a different but deeper and more pervasive conception of the Due Process Clause. This Clause exacts from the States for the lowliest and the most outcast all that is "implicit in the concept of ordered liberty." <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U. S. at 325</a></span>.</p>
<p>Due process of law thus conveys neither formal nor fixed nor narrow requirements. It is the compendious expression for all those rights which the courts must enforce because they are basic to our free society. But basic rights do not become petrified as of any one time, even though, as a matter of human experience, some may not too rhetorically be called eternal verities. It is of the very nature of a free society to advance in its standards of what is deemed reasonable and right. Representing as it does a living principle, due process is not confined within a permanent catalogue of what may at a given time be deemed the limits or the essentials of fundamental rights.</p>
<p>To rely on a tidy formula for the easy determination of what is a fundamental right for purposes of legal enforcement may satisfy a longing for certainty but ignores the movements of a free society. It belittles the scale of the conception of due process. The real clue to the problem confronting the judiciary in the application of the Due Process Clause is not to ask where the line is once and for all to be drawn but to recognize that it is for the Court to draw it by the gradual and empiric process of "inclusion and exclusion." <i>Davidson</i> v. <i>New Orleans,</i> <span class="citation" data-id="9841711"><a href="/opinion/89675/davidson-v-new-orleans/#104" aria-description="Citation for case: Davidson v. New Orleans">96 U. S. 97, 104</a></span>. This was the Court's insight when first called upon to consider the problem; to this insight the Court has on the whole been faithful as case after case has come before it since <i>Davidson</i> v. <i><span class="citation" data-id="9841711"><a href="/opinion/89675/davidson-v-new-orleans/" aria-description="Citation for case: Davidson v. New Orleans">New Orleans</a></span></i> was decided.</p>
<p>The security of one's privacy against arbitrary intrusion by the policewhich is at the core of the Fourth Amendmentis basic to a free society. It is therefore implicit in "the concept of ordered liberty" and as such enforceable against the States through the Due Process <span class="star-pagination">*28</span> Clause. The knock at the door, whether by day or by night, as a prelude to a search, without authority of law but solely on the authority of the police, did not need the commentary of recent history to be condemned as inconsistent with the conception of human rights enshrined in the history and the basic constitutional documents of English-speaking peoples.</p>
<p>Accordingly, we have no hesitation in saying that were a State affirmatively to sanction such police incursion into privacy it would run counter to the guaranty of the Fourteenth Amendment. But the ways of enforcing such a basic right raise questions of a different order. How such arbitrary conduct should be checked, what remedies against it should be afforded, the means by which the right should be made effective, are all questions that are not to be so dogmatically answered as to preclude the varying solutions which spring from an allowable range of judgment on issues not susceptible of quantitative solution.</p>
<p>In <i>Weeks</i> v. <i>United <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">States, supra</a></span></i><i>,</i> this Court held that in a federal prosecution the Fourth Amendment barred the use of evidence secured through an illegal search and seizure. This ruling was made for the first time in 1914. It was not derived from the explicit requirements of the Fourth Amendment; it was not based on legislation expressing Congressional policy in the enforcement of the Constitution. The decision was a matter of judicial implication. Since then it has been frequently applied and we stoutly adhere to it. But the immediate question is whether the basic right to protection against arbitrary intrusion by the police demands the exclusion of logically relevant evidence obtained by an unreasonable search and seizure because, in a federal prosecution for a federal crime, it would be excluded. As a matter of inherent reason, one would suppose this to be an issue as to which men with complete devotion to the protection of the right <span class="star-pagination">*29</span> of privacy might give different answers. When we find that in fact most of the English-speaking world does not regard as vital to such protection the exclusion of evidence thus obtained, we must hesitate to treat this remedy as an essential ingredient of the right. The contrariety of views of the States is particularly impressive in view of the careful reconsideration which they have given the problem in the light of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> decision.</p>
   I. Before the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> decision 27 States had passed on
       the admissibility of evidence obtained by unlawful
       search and seizure.
         (a) Of these, 26 States opposed the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine.
               (See Appendix, Table A.)
         (b) Of these, 1 State anticipated the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine.
               (Table B.)
   II. Since the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> decision 47 States all told have
         passed on the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine. (Table C.)
           (a) Of these, 20 passed on it for the first time.
                   (1) Of the foregoing States, 6 followed
                         the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine. (Table D.)
                   (2) Of the foregoing States, 14 rejected
                         the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine. (Table E.)
           (b) Of these, 26 States reviewed prior decisions
                 contrary to the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine.
                   (1) Of these, 10 States have followed
                         <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>,</i> overruling or distinguishing
                         their prior decisions. (Table
                         F.)
                   (2) Of these, 16 States adhered to their
                         prior decisions against <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>.</i>
                         (Table G.)
            (c) Of these, 1 State repudiated its prior formulation
                 of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine. (Table H.)
   III. As of today 31 States reject the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine, 16
         States are in agreement with it. (Table I.)
<span class="star-pagination">*30</span>
   IV. Of 10 jurisdictions within the United Kingdom and
        the British Commonwealth of Nations which have
        passed on the question, none has held evidence
        obtained by illegal search and seizure inadmissible.
        (Table J.)
<p>The jurisdictions which have rejected the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine have not left the right to privacy without other means of protection.<sup>[1]</sup> Indeed, the exclusion of evidence <span class="star-pagination">*31</span> is a remedy which directly serves only to protect those upon whose person or premises something incriminating has been found. We cannot, therefore, regard it as a departure from basic standards to remand such persons, together with those who emerge scatheless from a search, to the remedies of private action and such protection as the internal discipline of the police, under the eyes of an alert public opinion, may afford. Granting that in practice the exclusion of evidence may be an effective way of deterring unreasonable searches, it is not for this Court to condemn as falling below the minimal standards assured by the Due Process Clause a State's reliance upon other methods which, if consistently enforced, would be equally effective. Weighty testimony against such an insistence on our own view is furnished by the opinion of Mr. Justice (then Judge) Cardozo in <i>People</i> v. <i>Defore,</i> <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">242 N. Y. 13</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">150 N. E. 585</a></span>.<sup>[2]</sup> We cannot brush aside the experience of States which deem the incidence of such <span class="star-pagination">*32</span> conduct by the police too slight to call for a deterrent remedy not by way of disciplinary measures but by overriding the relevant rules of evidence. There are, moreover, reasons for excluding evidence unreasonably obtained by the federal police which are less compelling in the case of police under State or local authority. The public opinion of a community can far more effectively be exerted against oppressive conduct on the part of police directly responsible to the community itself than can local opinion, sporadically aroused, be brought to bear upon <span class="star-pagination">*33</span> remote authority pervasively exerted throughout the country.</p>
<p>We hold, therefore, that in a prosecution in a State court for a State crime the Fourteenth Amendment does not forbid the admission of evidence obtained by an unreasonable search and seizure. And though we have interpreted the Fourth Amendment to forbid the admission of such evidence, a different question would be presented if Congress under its legislative powers were to pass a statute purporting to negate the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine. We would then be faced with the problem of the respect to be accorded the legislative judgment on an issue as to which, in default of that judgment, we have been forced to depend upon our own. Problems of a converse character, also not before us, would be presented should Congress under § 5 of the Fourteenth Amendment undertake to enforce the rights there guaranteed by attempting to make the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine binding upon the States.</p>
<p><i>Affirmed.</i></p>
                        APPENDIX.<sup>[*]</sup>
                           TABLE A.
    STATES WHICH OPPOSED THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE BEFORE
           THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> CASE HAD BEEN DECIDED.
ALA.    <i>Shields</i> v. <i>State,</i> <span class="citation" data-id="6515773"><a href="/opinion/6639159/shields-v-state/" aria-description="Citation for case: Shields v. State">104 Ala. 35</a></span>, <span class="citation no-link">16 So. 85</span>.
ARK.    <i>Starchman</i> v. <i>State,</i> <span class="citation" data-id="6543624"><a href="/opinion/6665982/starchman-v-state/" aria-description="Citation for case: Starchman v. State">62 Ark. 538</a></span>, <span class="citation" data-id="6543624"><a href="/opinion/6665982/starchman-v-state/" aria-description="Citation for case: Starchman v. State">36 S. W. 940</a></span>.
CONN.   <i>State</i> v. <i>Griswold,</i> <span class="citation" data-id="6583651"><a href="/opinion/6703553/state-v-griswold/" aria-description="Citation for case: State v. Griswold">67 Conn. 290</a></span>, <span class="citation" data-id="6583651"><a href="/opinion/6703553/state-v-griswold/" aria-description="Citation for case: State v. Griswold">34 A. 1046</a></span>.
GA.     <i>Williams</i> v. <i>State,</i> <span class="citation" data-id="5567449"><a href="/opinion/5717379/williams-v-state/" aria-description="Citation for case: Williams v. State">100 Ga. 511</a></span>, <span class="citation" data-id="5567449"><a href="/opinion/5717379/williams-v-state/" aria-description="Citation for case: Williams v. State">28 S. E. 624</a></span>.
IDAHO   <i>State</i> v. <i>Bond,</i> <span class="citation" data-id="5169254"><a href="/opinion/5337571/state-v-bond/#439" aria-description="Citation for case: State v. Bond">12 Idaho 424, 439</a></span>, <span class="citation" data-id="5169254"><a href="/opinion/5337571/state-v-bond/#47" aria-description="Citation for case: State v. Bond">86 P. 43, 47</a></span>.
ILL.    <i>Siebert</i> v. <i>People,</i> <span class="citation" data-id="6965240"><a href="/opinion/7061242/siebert-v-people/#583" aria-description="Citation for case: Siebert v. People">143 Ill. 571, 583</a></span>, <span class="citation" data-id="6965240"><a href="/opinion/7061242/siebert-v-people/#434" aria-description="Citation for case: Siebert v. People">32 N. E. 431, 434</a></span>.
KAN.    <i>State</i> v. <i>Miller,</i> <span class="citation" data-id="7891978"><a href="/opinion/7941374/state-v-miller/" aria-description="Citation for case: State v. Miller">63 Kan. 62</a></span>, <span class="citation" data-id="7891978"><a href="/opinion/7941374/state-v-miller/" aria-description="Citation for case: State v. Miller">64 P. 1033</a></span>.
ME.     See <i>State</i> v. <i>Gorham,</i> <span class="citation" data-id="4932917"><a href="/opinion/5114261/state-v-gorham/#272" aria-description="Citation for case: State v. Gorham">65 Me. 270, 272</a></span>.
MD.     <i>Lawrence</i> v. <i>State,</i> <span class="citation" data-id="3487094"><a href="/opinion/3489145/lawrence-v-state/#35" aria-description="Citation for case: Lawrence v. State">103 Md. 17, 35</a></span>, <span class="citation" data-id="3487094"><a href="/opinion/3489145/lawrence-v-state/#103" aria-description="Citation for case: Lawrence v. State">63 A. 96, 103</a></span>.
<span class="star-pagination">*34</span>
    STATES WHICH OPPOSED THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE BEFORE
           THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> CASE HAD BEEN DECIDED.
MASS.   <i>Commonwealth</i> v. <i>Dana,</i> <span class="citation no-link">2 Metc. 329</span>.
MICH.   <i>People</i> v. <i>Aldorfer,</i> <span class="citation" data-id="7946344"><a href="/opinion/7992842/people-v-aldorfer/" aria-description="Citation for case: People v. Aldorfer">164 Mich. 676</a></span>, <span class="citation" data-id="7946344"><a href="/opinion/7992842/people-v-aldorfer/" aria-description="Citation for case: People v. Aldorfer">130 N. W. 351</a></span>.
MINN.   <i>State</i> v. <i>Strait,</i> <span class="citation" data-id="7973247"><a href="/opinion/8017916/state-v-strait/" aria-description="Citation for case: State v. Strait">94 Minn. 384</a></span>, <span class="citation" data-id="7973247"><a href="/opinion/8017916/state-v-strait/" aria-description="Citation for case: State v. Strait">102 N. W. 913</a></span>.
MO.     <i>State</i> v. <i>Pomeroy,</i> <span class="citation" data-id="8011909"><a href="/opinion/8054876/state-v-pomeroy/" aria-description="Citation for case: State v. Pomeroy">130 Mo. 489</a></span>, <span class="citation" data-id="8011909"><a href="/opinion/8054876/state-v-pomeroy/" aria-description="Citation for case: State v. Pomeroy">32 S. W. 1002</a></span>.
MONT.   See <i>State</i> v. <i>Fuller,</i> <span class="citation" data-id="8020864"><a href="/opinion/8063090/state-v-fuller/#19" aria-description="Citation for case: State v. Fuller">34 Mont. 12, 19</a></span>, <span class="citation" data-id="8020864"><a href="/opinion/8063090/state-v-fuller/#373" aria-description="Citation for case: State v. Fuller">85 P. 369, 373</a></span>.
NEB.    <i>Geiger</i> v. <i>State,</i> <span class="citation" data-id="6642402"><a href="/opinion/6759719/geiger-v-state/" aria-description="Citation for case: Geiger v. State">6 Neb. 545</a></span>.
N. H.   <i>State</i> v. <i>Flynn,</i> 36 N. H. 64.
N. Y.   <i>People</i> v. <i>Adams,</i> <span class="citation" data-id="5650086"><a href="/opinion/5795142/people-v-adams/" aria-description="Citation for case: People v. Adams">176 N. Y. 351</a></span>, <span class="citation" data-id="3588018"><a href="/opinion/3606309/people-v-adams/" aria-description="Citation for case: People v. . Adams">68 N. E. 636</a></span>.
N. C.   <i>State</i> v. <i>Wallace,</i> <span class="citation" data-id="6695783"><a href="/opinion/6809677/state-v-wallace/" aria-description="Citation for case: State v. Wallace">162 N. C. 622</a></span>, <span class="citation" data-id="3672959"><a href="/opinion/3926369/s-v-wallace/" aria-description="Citation for case: S. v. . Wallace">78 S. E. 1</a></span>.
OKLA.   <i>Silva</i> v. <i>State,</i> <span class="citation" data-id="3827556"><a href="/opinion/4069690/silva-v-state/" aria-description="Citation for case: Silva v. State">6 Okla. Cr. 97</a></span>, <span class="citation" data-id="3827556"><a href="/opinion/4069690/silva-v-state/" aria-description="Citation for case: Silva v. State">116 P. 199</a></span>.
ORE.    <i>State</i> v. <i>McDaniel,</i> <span class="citation" data-id="6898602"><a href="/opinion/6999518/state-v-mcdaniel/#169" aria-description="Citation for case: State v. McDaniel">39 Ore. 161, 169-70</a></span>, <span class="citation" data-id="6898602"><a href="/opinion/6999518/state-v-mcdaniel/#523" aria-description="Citation for case: State v. McDaniel">65 P. 520, 523</a></span>.
S. C.   <i>State</i> v. <i>Atkinson,</i> 40 S. C. 363, 371, <span class="citation" data-id="6678093"><a href="/opinion/6793472/state-v-atkinson/#1024" aria-description="Citation for case: State v. Atkinson">18 S. E. 1021, 1024</a></span>.
S. D.   <i>State</i> v. <i>Madison,</i> 23 S. D. 584, 591, <span class="citation" data-id="6687221"><a href="/opinion/6802175/state-v-madison/#650" aria-description="Citation for case: State v. Madison">122 N. W. 647, 650</a></span>.
TENN.   <i>Cohn</i> v. <i>State,</i> <span class="citation" data-id="8300564"><a href="/opinion/8332572/cohn-v-state/" aria-description="Citation for case: Cohn v. State">120 Tenn. 61</a></span>, <span class="citation" data-id="3980535"><a href="/opinion/4208407/parriss-v-hughes/" aria-description="Citation for case: Parriss v. Hughes">109 S. W. 1149</a></span>.
VT.     <i>State</i> v. <i>Mathers,</i> <span class="citation" data-id="6583727"><a href="/opinion/6703627/state-v-mathers/" aria-description="Citation for case: State v. Mathers">64 Vt. 101</a></span>, <span class="citation no-link">23 A. 590</span>.
WASH.   <i>State</i> v. <i>Royce,</i> <span class="citation" data-id="4726508"><a href="/opinion/4919818/state-v-royce/" aria-description="Citation for case: State v. Royce">38 Wash. 111</a></span>, <span class="citation" data-id="4726508"><a href="/opinion/4919818/state-v-royce/" aria-description="Citation for case: State v. Royce">80 P. 268</a></span>.
W. VA.  See <i>State</i> v. <i>Edwards,</i> <span class="citation" data-id="8175125"><a href="/opinion/8212628/state-v-edwards/#229" aria-description="Citation for case: State v. Edwards">51 W. Va. 220, 229</a></span>, <span class="citation" data-id="8175125"><a href="/opinion/8212628/state-v-edwards/#432" aria-description="Citation for case: State v. Edwards">41 S. E. 429,
          432-33</a></span>.
                           TABLE B.
    STATE WHICH HAD FORMULATED THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE
              BEFORE THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DECISION.
IOWA    <i>State</i> v. <i>Sheridan,</i> <span class="citation" data-id="7110547"><a href="/opinion/7199309/state-v-sheridan/" aria-description="Citation for case: State v. Sheridan">121 Iowa 164</a></span>, <span class="citation" data-id="7110547"><a href="/opinion/7199309/state-v-sheridan/" aria-description="Citation for case: State v. Sheridan">96 N. W. 730</a></span>.
                           TABLE C.
    STATES WHICH HAVE PASSED ON THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE
          SINCE THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> CASE WAS DECIDED.
   Every State except Rhode Island. But see <i>State</i> v. <i>Lorenzo,</i> 72
R. I. 175, <span class="citation" data-id="3870663"><a href="/opinion/4110701/state-v-lorenzo/" aria-description="Citation for case: State v. Lorenzo">48 A. 2d 407</a></span> (holding that defendant had consented to
the search, but that, even if he had not and even if the federal rule
applied, the evidence was admissible because no timely motion to
suppress had been made).
<span class="star-pagination">*35</span>
                           TABLE D.
STATES WHICH PASSED ON THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE FOR THE FIRST TIME
AFTER THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DECISION AND IN SO DOING FOLLOWED IT.
FLA.    <i>Atz</i> v. <i>Andrews,</i> <span class="citation" data-id="4921024"><a href="/opinion/5103176/atz-v-andrews/" aria-description="Citation for case: Atz v. Andrews">84 Fla. 43</a></span>, <span class="citation" data-id="4921024"><a href="/opinion/5103176/atz-v-andrews/" aria-description="Citation for case: Atz v. Andrews">94 So. 329</a></span>.
IND.    <i>Flum</i> v. <i>State,</i> <span class="citation" data-id="7057995"><a href="/opinion/7149435/flum-v-state/" aria-description="Citation for case: Flum v. State">193 Ind. 585</a></span>, <span class="citation" data-id="7057995"><a href="/opinion/7149435/flum-v-state/" aria-description="Citation for case: Flum v. State">141 N. E. 353</a></span>.
KY.     <i>Youman</i> v. <i>Commonwealth,</i> <span class="citation" data-id="7146240"><a href="/opinion/7233831/youman-v-commonwealth/" aria-description="Citation for case: Youman v. Commonwealth">189 Ky. 152</a></span>, <span class="citation" data-id="7146240"><a href="/opinion/7233831/youman-v-commonwealth/" aria-description="Citation for case: Youman v. Commonwealth">224 S. W. 860</a></span>.
MISS.   <i>Tucker</i> v. <i>State,</i> <span class="citation" data-id="7994199"><a href="/opinion/8037845/tucker-v-state/" aria-description="Citation for case: Tucker v. State">128 Miss. 211</a></span>, <span class="citation" data-id="7994199"><a href="/opinion/8037845/tucker-v-state/" aria-description="Citation for case: Tucker v. State">90 So. 845</a></span>.
WIS.    <i>Hoyer</i> v. <i>State,</i> <span class="citation" data-id="8194030"><a href="/opinion/8229755/hoyer-v-state/" aria-description="Citation for case: Hoyer v. State">180 Wis. 407</a></span>, <span class="citation" data-id="8194030"><a href="/opinion/8229755/hoyer-v-state/" aria-description="Citation for case: Hoyer v. State">193 N. W. 89</a></span>.
WYO.    <i>State</i> v. <i>George,</i> <span class="citation" data-id="4012941"><a href="/opinion/4235695/state-v-george/" aria-description="Citation for case: State v. George">32 Wyo. 223</a></span>, <span class="citation" data-id="4012941"><a href="/opinion/4235695/state-v-george/" aria-description="Citation for case: State v. George">231 P. 683</a></span>.
                           TABLE E.
STATES WHICH PASSED ON THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE FOR THE FIRST TIME
AFTER THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DECISION AND IN SO DOING REJECTED IT.
ARIZ.   <i>Argetakis</i> v. <i>State,</i> <span class="citation" data-id="6474949"><a href="/opinion/6599573/argetakis-v-state/" aria-description="Citation for case: Argetakis v. State">24 Ariz. 599</a></span>, <span class="citation" data-id="6474949"><a href="/opinion/6599573/argetakis-v-state/" aria-description="Citation for case: Argetakis v. State">212 P. 372</a></span>.
CALIF.  <i>People</i> v. <i>Mayen,</i> 188 Calif. 237, <span class="citation" data-id="3307559"><a href="/opinion/3307673/people-v-mayen/" aria-description="Citation for case: People v. Mayen">205 P. 435</a></span> (adopting the
          general rule but distinguishing the cases then decided by
          this Court on the ground that they apply only when a
          timely motion for return of the property seized has been
          made).
COLO.   <i>Massantonio</i> v. <i>People,</i> <span class="citation" data-id="3311672"><a href="/opinion/3316610/massantonio-v-people/" aria-description="Citation for case: Massantonio v. People">77 Colo. 392</a></span>, <span class="citation" data-id="3311672"><a href="/opinion/3316610/massantonio-v-people/" aria-description="Citation for case: Massantonio v. People">236 P. 1019</a></span>.
DEL.    <i>State</i> v. <i>Chuchola,</i> <span class="citation" data-id="6556679"><a href="/opinion/6677615/state-v-chuchola/" aria-description="Citation for case: State v. Chuchola">32 Del. 133</a></span>, <span class="citation" data-id="6556679"><a href="/opinion/6677615/state-v-chuchola/" aria-description="Citation for case: State v. Chuchola">120 A. 212</a></span> (distinguishing
          this Court's decisions).
LA.     <i>State</i> v. <i>Fleckinger,</i> <span class="citation" data-id="7172743"><a href="/opinion/7258568/nolan-v-brown/" aria-description="Citation for case: Nolan v. Brown">152 La. 337</a></span>, <span class="citation" data-id="7172750"><a href="/opinion/7258573/state-v-fleckinger/" aria-description="Citation for case: State v. Fleckinger">93 So. 115</a></span>. The constitutional
          convention of 1921 refused to adopt an amendment
          incorporating the federal rule. See <i>State</i> v. <i>Eddins,</i>
          <span class="citation" data-id="3471999"><a href="/opinion/3472961/state-v-eddins/" aria-description="Citation for case: State v. Eddins">161 La. 240</a></span>, <span class="citation" data-id="3471999"><a href="/opinion/3472961/state-v-eddins/" aria-description="Citation for case: State v. Eddins">108 So. 468</a></span>.
NEV.    <i>State</i> v. <i>Chin Gim,</i> <span class="citation" data-id="8042834"><a href="/opinion/8083180/state-v-chin-gim/" aria-description="Citation for case: State v. Chin Gim">47 Nev. 431</a></span>, <span class="citation" data-id="8042834"><a href="/opinion/8083180/state-v-chin-gim/" aria-description="Citation for case: State v. Chin Gim">224 P. 798</a></span>.
N. J.   <i>State</i> v. <i>Black,</i> 5 N. J. Misc. 48, <span class="citation" data-id="8506298"><a href="/opinion/8533787/state-v-black/" aria-description="Citation for case: State v. Black">135 A. 685</a></span>.
N. M.   <i>State</i> v. <i>Dillon,</i> 34 N. M. 366, <span class="citation" data-id="3571966"><a href="/opinion/3591159/state-v-dillon/" aria-description="Citation for case: State v. Dillon">281 P. 474</a></span>.
N. D.   <i>State</i> v. <i>Fahn,</i> <span class="citation" data-id="3682031"><a href="/opinion/3934924/state-v-fahn/" aria-description="Citation for case: State v. Fahn">53 N. D. 203</a></span>, <span class="citation" data-id="3682031"><a href="/opinion/3934924/state-v-fahn/" aria-description="Citation for case: State v. Fahn">205 N. W. 67</a></span>.
OHIO    <i>State</i> v. <i>Lindway,</i> <span class="citation" data-id="3780866"><a href="/opinion/4024496/state-v-lindway/" aria-description="Citation for case: State v. Lindway">131 Ohio St. 166</a></span>, <span class="citation" data-id="3780866"><a href="/opinion/4024496/state-v-lindway/" aria-description="Citation for case: State v. Lindway">2 N. E. 2d 490</a></span>.
PA.     <i>Commonwealth</i> v. <i>Dabbierio,</i> <span class="citation" data-id="3848320"><a href="/opinion/4089084/commonwealth-v-dabbierio/" aria-description="Citation for case: Commonwealth v. Dabbierio">290 Pa. 174</a></span>, <span class="citation" data-id="3848320"><a href="/opinion/4089084/commonwealth-v-dabbierio/" aria-description="Citation for case: Commonwealth v. Dabbierio">138 A. 679</a></span>.
TEX.    <i>Welchek</i> v. <i>State,</i> 93 Tex. Cr. Rep. 271, <span class="citation" data-id="3977441"><a href="/opinion/4205697/welchek-v-state/" aria-description="Citation for case: Welchek v. State">247 S. W. 524</a></span>. In
          1925 a statute changed the rule by providing that "No
          evidence obtained by an officer or other person in violation
          of any provisions of the Constitution or laws of the State
<span class="star-pagination">*36</span>
STATES WHICH PASSED ON THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE FOR THE FIRST TIME
AFTER THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DECISION AND IN SO DOING REJECTED IT.
          of Texas, or of the Constitution of the United States of
          America, shall be admitted in evidence against the accused
          on the trial of any criminal case." Texas Laws 1925,
          c. 49, as amended, 2 Vernon's Tex. Stat., 1948 (Code
          of Crim. Proc.), Art. 727a.
UTAH    <i>State</i> v. <i>Aime,</i> <span class="citation" data-id="8657438"><a href="/opinion/8674530/state-v-aime/" aria-description="Citation for case: State v. Aime">62 Utah 476</a></span>, <span class="citation" data-id="8657438"><a href="/opinion/8674530/state-v-aime/" aria-description="Citation for case: State v. Aime">220 P. 704</a></span>.
VA.     <i>Hall</i> v. <i>Commonwealth,</i> <span class="citation" data-id="6815460"><a href="/opinion/6919821/hall-v-commonwealth/" aria-description="Citation for case: Hall v. Commonwealth">138 Va. 727</a></span>, <span class="citation" data-id="6815460"><a href="/opinion/6919821/hall-v-commonwealth/" aria-description="Citation for case: Hall v. Commonwealth">121 S. E. 154</a></span>.
                           TABLE F.
 STATES WHICH, AFTER THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DECISION, OVERRULED OR
            DISTINGUISHED PRIOR CONTRARY DECISIONS.
IDAHO   Idaho expressly refused to follow the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> decision in <i>State</i>
          v. <i>Myers,</i> <span class="citation" data-id="5171906"><a href="/opinion/5339733/state-v-myers/" aria-description="Citation for case: State v. Myers">36 Idaho 396</a></span>, <span class="citation" data-id="5171906"><a href="/opinion/5339733/state-v-myers/" aria-description="Citation for case: State v. Myers">211 P. 440</a></span>, but repudiated the
          <i><span class="citation" data-id="5171906"><a href="/opinion/5339733/state-v-myers/" aria-description="Citation for case: State v. Myers">Myers</a></span></i> case and adopted the federal rule in <i>State</i> v.
          <i>Arregui,</i> <span class="citation" data-id="3412636"><a href="/opinion/3416496/state-v-arregui/" aria-description="Citation for case: State v. Arregui">44 Idaho 43</a></span>, <span class="citation" data-id="3412636"><a href="/opinion/3416496/state-v-arregui/" aria-description="Citation for case: State v. Arregui">254 P. 788</a></span>.
ILL.    After two cases following the former state rule, Illinois
          adopted the federal rule in <i>People</i> v. <i>Castree,</i> <span class="citation" data-id="6981353"><a href="/opinion/7076578/people-v-castree/" aria-description="Citation for case: People v. Castree">311 Ill. 392</a></span>,
          <span class="citation" data-id="6981353"><a href="/opinion/7076578/people-v-castree/" aria-description="Citation for case: People v. Castree">143 N. E. 112</a></span>.
MICH.   <i>People</i> v. <i>Marxhausen,</i> <span class="citation" data-id="7950359"><a href="/opinion/7996598/people-v-marxhausen/" aria-description="Citation for case: People v. Marxhausen">204 Mich. 559</a></span>, <span class="citation" data-id="7950359"><a href="/opinion/7996598/people-v-marxhausen/" aria-description="Citation for case: People v. Marxhausen">171 N. W. 557</a></span> (distinguishing
          earlier cases on the ground that in them no
          preliminary motion to suppress had been made).
MO.     <i>State</i> v. <i>Graham,</i> <span class="citation" data-id="3536208"><a href="/opinion/3558301/state-v-graham/" aria-description="Citation for case: State v. Graham">295 Mo. 695</a></span>, <span class="citation" data-id="3536208"><a href="/opinion/3558301/state-v-graham/" aria-description="Citation for case: State v. Graham">247 S. W. 194</a></span>, supported
          the old rule in a dictum, but the federal rule was adopted
          in <i>State</i> v. <i>Owens,</i> <span class="citation" data-id="3529427"><a href="/opinion/3553710/state-v-owens/" aria-description="Citation for case: State v. Owens">302 Mo. 348</a></span>, <span class="citation" data-id="3529427"><a href="/opinion/3553710/state-v-owens/" aria-description="Citation for case: State v. Owens">259 S. W. 100</a></span> (distinguishing
          earlier cases on the ground that in them no
          preliminary motion to dismiss had been made).
MONT.   <i>State ex rel. King</i> v. <i>District Court,</i> <span class="citation" data-id="8024014"><a href="/opinion/8066072/state-ex-rel-king-v-district-court/" aria-description="Citation for case: State ex rel. King v. District Court">70 Mont. 191</a></span>, <span class="citation" data-id="8024014"><a href="/opinion/8066072/state-ex-rel-king-v-district-court/" aria-description="Citation for case: State ex rel. King v. District Court">224 P.
          862</a></span>.
OKLA.   <i>Gore</i> v. <i>State,</i> <span class="citation" data-id="3812264"><a href="/opinion/4054922/gore-v-state/" aria-description="Citation for case: Gore v. State">24 Okla. Cr. 394</a></span>, <span class="citation" data-id="3812264"><a href="/opinion/4054922/gore-v-state/" aria-description="Citation for case: Gore v. State">218 P. 545</a></span>.
S. D.   <i>State</i> v. <i>Gooder,</i> 57 S. D. 619, <span class="citation" data-id="6692555"><a href="/opinion/6806990/state-v-gooder/" aria-description="Citation for case: State v. Gooder">234 N. W. 610</a></span>. But cf.
          S. D. Laws 1935, c. 96, now S. D. Code § 34.1102 (1939),
          amending Rev. Code 1919, § 4606 (all evidence admissible
<span class="star-pagination">*37</span>
 STATES WHICH, AFTER THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DECISION, OVERRULED OR
            DISTINGUISHED PRIOR CONTRARY DECISIONS.
            under a valid search warrant is admissible notwithstanding
            defects in the issuance of the warrant).
TENN.   <i>Hughes</i> v. <i>State,</i> <span class="citation" data-id="8302107"><a href="/opinion/8334068/hughes-v-state/" aria-description="Citation for case: Hughes v. State">145 Tenn. 544</a></span>, <span class="citation no-link">238 S. W. 588</span> (distinguishing
          <i>Cohn</i> v. <i>State, supra,</i> Table A).
WASH.   <i>State</i> v. <i>Gibbons,</i> <span class="citation" data-id="4720844"><a href="/opinion/4914645/state-v-gibbons/" aria-description="Citation for case: State v. Gibbons">118 Wash. 171</a></span>, <span class="citation" data-id="4720844"><a href="/opinion/4914645/state-v-gibbons/" aria-description="Citation for case: State v. Gibbons">203 P. 390</a></span>.
W. VA.  <i>State</i> v. <i>Andrews,</i> <span class="citation" data-id="8179544"><a href="/opinion/8216695/state-v-andrews/" aria-description="Citation for case: State v. Andrews">91 W. Va. 720</a></span>, <span class="citation" data-id="8179544"><a href="/opinion/8216695/state-v-andrews/" aria-description="Citation for case: State v. Andrews">114 S. E. 257</a></span> (distinguishing
          earlier cases).
                           TABLE G.
STATES WHICH, AFTER THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DECISION, REVIEWED PRIOR CONTRARY
     DECISIONS AND IN SO DOING ADHERED TO THOSE DECISIONS.
ALA.    <i>Banks</i> v. <i>State,</i> <span class="citation" data-id="3233534"><a href="/opinion/3232762/banks-v-state/" aria-description="Citation for case: Banks v. State">207 Ala. 179</a></span>, <span class="citation" data-id="3233534"><a href="/opinion/3232762/banks-v-state/" aria-description="Citation for case: Banks v. State">93 So. 293</a></span>.
ARK.    <i>Benson</i> v. <i>State,</i> <span class="citation" data-id="7811152"><a href="/opinion/7866973/benson-v-state/" aria-description="Citation for case: Benson v. State">149 Ark. 633</a></span>, <span class="citation" data-id="7811152"><a href="/opinion/7866973/benson-v-state/" aria-description="Citation for case: Benson v. State">233 S. W. 758</a></span>.
CONN.   <i>State</i> v. <i>Reynolds,</i> <span class="citation" data-id="3321660"><a href="/opinion/3326264/state-v-reynolds/" aria-description="Citation for case: State v. Reynolds">101 Conn. 224</a></span>, <span class="citation" data-id="3321660"><a href="/opinion/3326264/state-v-reynolds/" aria-description="Citation for case: State v. Reynolds">125 A. 636</a></span>.
GA.     <i>Jackson</i> v. <i>State,</i> <span class="citation" data-id="5584660"><a href="/opinion/5734032/jackson-v-state/" aria-description="Citation for case: Jackson v. State">156 Ga. 647</a></span>, <span class="citation" data-id="5584660"><a href="/opinion/5734032/jackson-v-state/" aria-description="Citation for case: Jackson v. State">119 S. E. 525</a></span>.
KAN.    <i>State</i> v. <i>Johnson,</i> <span class="citation" data-id="7907024"><a href="/opinion/7955587/state-v-johnson/" aria-description="Citation for case: State v. Johnson">116 Kan. 58</a></span>, <span class="citation" data-id="7907024"><a href="/opinion/7955587/state-v-johnson/" aria-description="Citation for case: State v. Johnson">226 P. 245</a></span>.
ME.     <i>State</i> v. <i>Schoppe,</i> <span class="citation" data-id="4938095"><a href="/opinion/5119383/state-v-schoppe/#16" aria-description="Citation for case: State v. Schoppe">113 Me. 10, 16</a></span>, <span class="citation" data-id="4938095"><a href="/opinion/5119383/state-v-schoppe/#869" aria-description="Citation for case: State v. Schoppe">92 A. 867, 869</a></span> (alternative
          holding, not noticing <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i>).
MD.     <i>Meisinger</i> v. <i>State,</i> <span class="citation" data-id="3484807"><a href="/opinion/3486914/meisinger-v-state/" aria-description="Citation for case: Meisinger v. State">155 Md. 195</a></span>, <span class="citation" data-id="3484807"><a href="/opinion/3486914/meisinger-v-state/" aria-description="Citation for case: Meisinger v. State">141 A. 536</a></span>, <span class="citation no-link">142 A. 190</span>.
          But cf. Md. Laws 1929, c. 194, as amended, Md. Code
          Ann., Art. 35, § 5 (1947 Supp.) (in trial of misdemeanors,
          evidence obtained by illegal search and seizure is inadmissible).
MASS.   <i>Commonwealth</i> v. <i>Wilkins,</i> <span class="citation" data-id="6436025"><a href="/opinion/6562275/commonwealth-v-wilkins/" aria-description="Citation for case: Commonwealth v. Wilkins">243 Mass. 356</a></span>, <span class="citation no-link">138 N. E. 11</span>.
MINN.   <i>State</i> v. <i>Pluth,</i> <span class="citation" data-id="7981382"><a href="/opinion/8025591/state-v-pluth/" aria-description="Citation for case: State v. Pluth">157 Minn. 145</a></span>, <span class="citation" data-id="7981382"><a href="/opinion/8025591/state-v-pluth/" aria-description="Citation for case: State v. Pluth">195 N. W. 789</a></span>.
NEB.    <i>Billings</i> v. <i>State,</i> <span class="citation" data-id="8032854"><a href="/opinion/8074092/billings-v-state/" aria-description="Citation for case: Billings v. State">109 Neb. 596</a></span>, <span class="citation" data-id="8032854"><a href="/opinion/8074092/billings-v-state/" aria-description="Citation for case: Billings v. State">191 N. W. 721</a></span>.
N. H.   <i>State</i> v. <i>Agalos,</i> 79 N. H. 241, 242, <span class="citation" data-id="3553875"><a href="/opinion/3573624/state-v-agalos/#315" aria-description="Citation for case: State v. Agalos">107 A. 314, 315</a></span> (not
          noticing <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i>).
N. Y.   <i>People</i> v. <i>Defore,</i> <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">242 N. Y. 13</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">150 N. E. 585</a></span>; <i>People</i> v.
          <i>Richter's Jewelers,</i> <span class="citation" data-id="3594947"><a href="/opinion/3612831/people-v-richters-jewelers-inc/#169" aria-description="Citation for case: People v. Richter&#x27;s Jewelers, Inc.">291 N. Y. 161, 169</a></span>, <span class="citation" data-id="3594947"><a href="/opinion/3612831/people-v-richters-jewelers-inc/#693" aria-description="Citation for case: People v. Richter&#x27;s Jewelers, Inc.">51 N. E. 2d 690,
          693</a></span> (holding that adoption of Amendment to State Constitution
<span class="star-pagination">*38</span>
STATES WHICH, AFTER THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DECISION, REVIEWED PRIOR CONTRARY
     DECISIONS AND IN SO DOING ADHERED TO THOSE DECISIONS.
         in same language as Civil Rights Law construed
         in the <i><span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">Defore</a></span></i> case is not occasion for changing interpretation,
         especially since proceedings of the convention
         which framed the amendment show that no change was
         intended).
N. C.   <i>State</i> v. <i>Simmons,</i> <span class="citation" data-id="3646527"><a href="/opinion/3900534/state-v-simmons/" aria-description="Citation for case: State v. . Simmons">183 N. C. 684</a></span>, <span class="citation" data-id="3646527"><a href="/opinion/3900534/state-v-simmons/" aria-description="Citation for case: State v. . Simmons">110 S. E. 591</a></span> (distinguishing
          between evidentiary articles and corpus delicti).
ORE.    See <i>State</i> v. <i>Folkes,</i> <span class="citation" data-id="3842073"><a href="/opinion/4083033/state-v-folkes/#588" aria-description="Citation for case: State v. Folkes">174 Ore. 568, 588-89</a></span>, <span class="citation" data-id="3842073"><a href="/opinion/4083033/state-v-folkes/#25" aria-description="Citation for case: State v. Folkes">150 P. 2d 17, 25</a></span>.
          But see <i>State</i> v. <i>Laundy,</i> <span class="citation" data-id="6907613"><a href="/opinion/7007488/state-v-laundy/#493" aria-description="Citation for case: State v. Laundy">103 Ore. 443, 493-95</a></span>, <span class="citation" data-id="6907613"><a href="/opinion/7007488/state-v-laundy/#974" aria-description="Citation for case: State v. Laundy">204 P.
          958, 974-75</a></span>.
S. C.   After granting a motion to return illegally seized property
         in <i>Blacksburg</i> v. <i>Beam,</i> 104 S. C. 146, <span class="citation" data-id="3880639"><a href="/opinion/4119711/town-of-blacksburg-v-beam/" aria-description="Citation for case: Town of Blacksburg v. Beam">88 S. E. 441</a></span>, South
         Carolina reaffirmed its agreement with the general rule in
         <i>State</i> v. <i>Green,</i> 121 S. C. 230, <span class="citation no-link">114 S. E. 317</span>.
VT.     <i>State</i> v. <i>Stacy,</i> <span class="citation" data-id="3990360"><a href="/opinion/4216163/state-v-stacy/#401" aria-description="Citation for case: State v. Stacy">104 Vt. 379, 401</a></span>, <span class="citation no-link">160 A. 257</span>, 266.
                           TABLE H.
       STATE WHICH HAS REPUDIATED ITS PRIOR FORMULATION
                OF THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE.
IOWA    <i>State</i> v. <i>Rowley,</i> <span class="citation" data-id="7120701"><a href="/opinion/7208995/state-v-rowley/" aria-description="Citation for case: State v. Rowley">197 Iowa 977</a></span>, <span class="citation no-link">195 N. W. 881</span> (withdrawing
          earlier opinion in <span class="citation no-link">187 N. W. 7</span>).
                           TABLE I.
       SUMMARY OF PRESENT POSITION OF STATES WHICH HAVE
            PASSED ON THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE.
   (a) States that reject <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>:</i>
   Ala., Ariz., Ark., Calif., Colo., Conn., Del., Ga., Iowa, Kan., La.,
Me., Md., Mass., Minn., Neb., Nev., N. H., N. J., N. M., N. Y.,
N. C., N. D., Ohio, Ore., Pa., S. C., Texas, Utah, Vt., Va.
   (b) States that are in agreement with <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>:</i>
   Fla., Idaho, Ill., Ind., Ky., Mich., Miss., Mo., Mont., Okla., S. D.,
Tenn., Wash., W. Va., Wis., Wyo.
<span class="star-pagination">*39</span>
                           TABLE J.
JURISDICTIONS OF THE UNITED KINGDOM AND THE BRITISH COMMONWEALTH
             OF NATIONS WHICH HAVE HELD ADMISSIBLE
       EVIDENCE OBTAINED BY ILLEGAL SEARCH AND SEIZURE.
AUSTRALIA  <i>Miller</i> v. <i>Noblet,</i> [1927] S. A. S. R. 385.
CANADA
  ALTA.   <i>Rex</i> v. <i>Nelson,</i> [1922] 2 W. W. R. 381, 69 D. L. R. 180.
   MAN.   <i>Rex</i> v. <i>Duroussel,</i> 41 Man. 15, [1933] 2 D. L. R. 446.
   ONT.   <i>Regina</i> v. <i>Doyle,</i> 12 Ont. 347.
  SASK.   <i>Rex</i> v. <i>Kostachuk,</i> 24 Sask. 485, 54 Can. C. C. 189.
ENGLAND   See <i>Elias</i> v. <i>Pasmore,</i> [1934] 2 K. B. 164.
INDIA
  ALL.    <i>Ali Ahmad Khan</i> v. <i>Emperor,</i> 81 I. C. 615 (1).
  CAL.    <i>Baldeo Bin</i> v. <i>Emperor,</i> 142 I. C. 639.
  RANG.   <i>Chwa Hum Htive</i> v. <i>Emperor,</i> 143 I. C. 824.
SCOTLAND  See <i>Hodgson</i> v. <i>Macpherson,</i> [1913] S. C. (J.) 68, 73.
<p>MR. JUSTICE BLACK, concurring.</p>
<p>In this case petitioner was convicted of a crime in a state court on evidence obtained by a search and seizure conducted in a manner that this Court has held "unreasonable" and therefore in violation of the Fourth Amendment. And under a rule of evidence adopted by this Court evidence so obtained by federal officers cannot be used against defendants in federal courts. For reasons stated in my dissenting opinion in <i>Adamson</i> v. <i>California,</i> <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/#68" aria-description="Citation for case: Adamson v. California">332 U. S. 46, 68</a></span>, I agree with the conclusion of the Court that the Fourth Amendment's prohibition of "unreasonable searches and seizures" is enforceable against the states. Consequently, I should be for reversal of this case if I thought the Fourth Amendment not only prohibited "unreasonable searches and seizures," but also, of itself, barred the use of evidence so unlawfully obtained. But I agree with what appears to be a plain implication of the Court's opinion that the federal exclusionary rule is <span class="star-pagination">*40</span> not a command of the Fourth Amendment but is a judicially created rule of evidence which Congress might negate. See <i>McNabb</i> v. <i>United States,</i> <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U. S. 332</a></span>. This leads me to concur in the Court's judgment of affirmance.</p>
<p>It is not amiss to repeat my belief that the Fourteenth Amendment was intended to make the Fourth Amendment in its entirety applicable to the states. The Fourth Amendment was designed to protect people against unrestrained searches and seizures by sheriffs, policemen and other law enforcement officers. Such protection is an essential in a free society. And I am unable to agree that the protection of people from over-zealous or ruthless state officers is any less essential in a country of "ordered liberty" than is the protection of people from over-zealous or ruthless federal officers. Certainly there are far more state than federal enforcement officers and their activities, up to now, have more frequently and closely touched the intimate daily lives of people than have the activities of federal officers. A state officer's "knock at the door . . . as a prelude to a search, without authority of law," may be, as our experience shows, just as ominous to "ordered liberty" as though the knock were made by a federal officer.</p>
<p>MR. JUSTICE DOUGLAS, dissenting.</p>
<p>I believe for the reasons stated by MR. JUSTICE BLACK in his dissent in <i>Adamson</i> v. <i>California,</i> <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/#68" aria-description="Citation for case: Adamson v. California">332 U. S. 46, 68</a></span>, that the Fourth Amendment is applicable to the States. I agree with MR. JUSTICE MURPHY that the evidence obtained in violation of it <i>must</i> be excluded in state prosecutions as well as in federal prosecutions, since in absence of that rule of evidence the Amendment would have no effective sanction. I also agree with him that under that <span class="star-pagination">*41</span> test this evidence was improperly admitted and that the judgments of conviction must be reversed.</p>
<p>MR. JUSTICE MURPHY, with whom MR. JUSTICE RUTLEDGE joins, dissenting.</p>
<p>It is disheartening to find so much that is right in an opinion which seems to me so fundamentally wrong. Of course I agree with the Court that the Fourteenth Amendment prohibits activities which are proscribed by the search and seizure clause of the Fourth Amendment. See my dissenting views, and those of MR. JUSTICE BLACK, in <i>Adamson</i> v. <i>California,</i> <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/#68" aria-description="Citation for case: Adamson v. California">332 U. S. 46, 68, 123</a></span>. Quite apart from the blanket application of the Bill of Rights to the States, a devotee of democracy would ill suit his name were he to suggest that his home's protection against unlicensed governmental invasion was not "of the very essence of a scheme of ordered liberty." <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319, 325</a></span>. It is difficult for me to understand how the Court can go this far and yet be unwilling to make the step which can give some meaning to the pronouncements it utters.</p>
<p>Imagination and zeal may invent a dozen methods to give content to the commands of the Fourth Amendment. But this Court is limited to the remedies currently available. It cannot legislate the ideal system. If we would attempt the enforcement of the search and seizure clause in the ordinary case today, we are limited to three devices: judicial exclusion of the illegally obtained evidence; criminal prosecution of violators; and civil action against violators in the action of trespass.</p>
<p>Alternatives are deceptive. Their very statement conveys the impression that one possibility is as effective as the next. In this case their statement is blinding. For there is but one alternative to the rule of exclusion. That is no sanction at all.</p>
<p><span class="star-pagination">*42</span> This has been perfectly clear since 1914, when a unanimous Court decided <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#393" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 393</a></span>. "If letters and private documents can thus be seized and held and used in evidence against a citizen accused of an offense," we said, "the protection of the Fourth Amendment declaring his right to be secure against such searches and seizures is of no value, and, so far as those thus placed are concerned, might as well be stricken from the Constitution." "It reduces the Fourth Amendment to a form of words." Holmes, J., for the Court, in <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span>.</p>
<p>Today the Court wipes those statements from the books with its bland citation of "other remedies." Little need be said concerning the possibilities of criminal prosecution. Self-scrutiny is a lofty ideal, but its exaltation reaches new heights if we expect a District Attorney to prosecute himself or his associates for well-meaning violations of the search and seizure clause during a raid the District Attorney or his associates have ordered.<sup>[1]</sup> But there is an appealing ring in another alternative. A trespass action for damages is a venerable means of securing reparation for unauthorized invasion of the home. Why not put the old writ to a new use? When the Court cites cases permitting the action, the remedy seems complete.</p>
<p>But what an illusory remedy this is, if by "remedy" we mean a positive deterrent to police and prosecutors <span class="star-pagination">*43</span> tempted to violate the Fourth Amendment. The appealing ring softens when we recall that in a trespass action the measure of damages is simply the extent of the injury to physical property. If the officer searches with care, he can avoid all but nominal damagesa penny, or a dollar. Are punitive damages possible? Perhaps. But a few states permit none, whatever the circumstances.<sup>[2]</sup> In those that do, the plaintiff must show the real ill will or malice of the defendant,<sup>[3]</sup> and surely it is not unreasonable to assume that one in honest pursuit of crime bears no malice toward the search victim. If that burden is carried, recovery may yet be defeated by the rule that there must be physical damages before punitive damages may be awarded.<sup>[4]</sup> In addition, some states limit punitive damages to the actual expenses of litigation. See <span class="citation no-link">61 Harv. L. Rev. 113</span>, 119-120. Others demand some arbitrary ratio between actual and punitive damages before a verdict may stand. See Morris, <i>Punitive Damages in Tort Cases,</i> <span class="citation no-link">44 Harv. L. Rev. 1173</span>, 1180-1181. Even assuming the ill will of the officer, his reasonable grounds for belief that the home he searched harbored evidence of crime is admissible in mitigation of punitive damages. <i>Gamble</i> v. <i>Keyes,</i> 35 S. D. 644, <span class="citation" data-id="6688877"><a href="/opinion/6803692/gamble-v-keyes/" aria-description="Citation for case: Gamble v. Keyes">153 N. W. 888</a></span>; <i>Simpson</i> v. <i>McCaffrey,</i> <span class="citation no-link">13 Ohio 508</span>. The bad reputation of the plaintiff is likewise admissible. <i>Banfill</i> v. <i>Byrd,</i> <span class="citation" data-id="7993628"><a href="/opinion/8037305/banfill-v-byrd/" aria-description="Citation for case: Banfill v. Byrd">122 Miss. 288</a></span>, <span class="citation" data-id="7993628"><a href="/opinion/8037305/banfill-v-byrd/" aria-description="Citation for case: Banfill v. Byrd">84 So. 227</a></span>. If the evidence seized was actually used at a trial, that fact has been <span class="star-pagination">*44</span> held a complete justification of the search, and a defense against the trespass action. <i>Elias</i> v. <i>Pasmore</i> [1934] 2 K. B. 164. And even if the plaintiff hurdles all these obstacles, and gains a substantial verdict, the individual officer's finances may well make the judgment useless for the municipality, of course, is not liable without its consent. Is it surprising that there is so little in the books concerning trespass actions for violation of the search and seizure clause?</p>
<p>The conclusion is inescapable that but one remedy exists to deter violations of the search and seizure clause. That is the rule which excludes illegally obtained evidence. Only by exclusion can we impress upon the zealous prosecutor that violation of the Constitution will do him no good. And only when that point is driven home can the prosecutor be expected to emphasize the importance of observing constitutional demands in his instructions to the police.</p>
<p>If proof of the efficacy of the federal rule were needed, there is testimony in abundance in the recruit training programs and in-service courses provided the police in states which follow the federal rule.<sup>[5]</sup> St. Louis, for example, demands extensive training in the rules of search and seizure, with emphasis upon the ease with which a case may collapse if it depends upon evidence obtained <span class="star-pagination">*45</span> unlawfully. Current court decisions are digested and read at roll calls. The same general pattern prevails in Washington, D. C.<sup>[6]</sup> In Dallas, officers are thoroughly briefed and instructed that "the courts will follow the rules very closely and will detect any frauds."<sup>[7]</sup> In Milwaukee, a stout volume on the law of arrest and search and seizure is made the basis of extended instruction.<sup>[8]</sup> Officer preparation in the applicable rules in Jackson, Mississippi, has included the lectures of an Associate Justice of the Mississippi Supreme Court. The instructions on evidence and search and seizure given to trainees in San Antonio carefully note the rule of exclusion in Texas, and close with this statement: "Every police officer should know the laws and the rules of evidence. Upon knowledge of these facts determines whether the . . . defendant will be convicted or acquitted. . . . When you investigate a case . . . remember throughout your investigation that only admissible evidence can be used."</p>
<p>But in New York City, we are informed simply that "copies of the State Penal Law and Code of Criminal Procedure" are given to officers, and that they are "kept advised" that illegally obtained evidence may be admitted in New York courts. In Baltimore, a "Digest of Laws" is distributed, and it is made clear that the <span class="star-pagination">*46</span> statutory section excluding evidence "is limited in its application to the trial of misdemeanors. . . . It would appear . . . that . . . evidence illegally obtained may still be admissible in the trial of felonies." In Cleveland, recruits and other officers are told of the rules of search and seizure, but "instructed that it is admissible in the courts of Ohio. The Ohio Supreme Court has indicated very definitely and clearly that Ohio belongs to the `admissionist' group of states when evidence obtained by an illegal search is presented to the court." A similar pattern emerges in Birmingham, Alabama.</p>
<p>The contrast between states with the federal rule and those without it is thus a positive demonstration of its efficacy. There are apparent exceptions to the contrast Denver, for example, appears to provide as comprehensive a series of instructions as that in Chicago, although Colorado permits introduction of the evidence and Illinois does not. And, so far as we can determine from letters, a fairly uniform standard of officer instruction appears in other cities, irrespective of the local rule of evidence. But the examples cited above serve to ground an assumption that has motivated this Court since the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case: that this is an area in which judicial action has positive effect upon the breach of law; and that, without judicial action, there are simply no effective sanctions presently available.</p>
<p>I cannot believe that we should decide due process questions by simply taking a poll of the rules in various jurisdictions, even if we follow the <i><span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">Palko</a></span></i> "test." Today's decision will do inestimable harm to the cause of fair police methods in our cities and states. Even more important, perhaps, it must have tragic effect upon public respect for our judiciary. For the Court now allows what is indeed shabby business: lawlessness by officers of the law.</p>
<p><span class="star-pagination">*47</span> Since the evidence admitted was secured in violation of the Fourth Amendment, the judgment should be reversed.</p>
<p>MR. JUSTICE RUTLEDGE, dissenting.</p>
<p>"Wisdom too often never comes, and so one ought not to reject it merely because it comes late." Similarly, one should not reject a piecemeal wisdom, merely because it hobbles toward the truth with backward glances. Accordingly, although I think that all "the specific guarantees of the Bill of Rights should be carried over intact into the first section of the Fourteenth Amendment," <i>Adamson</i> v. <i>California,</i> <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/" aria-description="Citation for case: Adamson v. California">332 U. S. 46</a></span>, dissenting opinion at 124, I welcome the fact that the Court, in its slower progress toward this goal, today finds the substance of the Fourth Amendment "to be implicit in the concept of ordered liberty, and thus, through the Fourteenth Amendment,. . . valid as against the states." <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319, 325</a></span>.</p>
<p>But I reject the Court's simultaneous conclusion that the mandate embodied in the Fourth Amendment, although binding on the states, does not carry with it the one sanctionexclusion of evidence taken in violation of the Amendment's termsfailure to observe which means that "the protection of the Fourth Amendment . . . might as well be stricken from the Constitution." <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#393" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 393</a></span>. For I agree with my brother MURPHY'S demonstration that the Amendment without the sanction is a dead letter. Twenty-nine years ago this Court, speaking through Justice Holmes, refused to permit the Government to subpoena documentary evidence which it had stolen, copied and then returned, for the reason that such a procedure "reduces the Fourth Amendment to a form of words." <i>Silverthrone Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span>. But the version of the Fourth Amendment today held <span class="star-pagination">*48</span> applicable to the states hardly rises to the dignity of a form of words; at best it is a pale and frayed carbon copy of the original, bearing little resemblance to the Amendment the fulfillment of whose command I had heretofore thought to be "an indispensable need for a democratic society." <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span>, dissenting opinion at 161.</p>
<p>I also reject any intimation that Congress could validly enact legislation permitting the introduction in federal courts of evidence seized in violation of the Fourth Amendment. I had thought that issue settled by this Court's invalidation on dual grounds, in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, of a federal statute which in effect required the production of evidence thought probative by Government counselthe Court there holding the statute to be "obnoxious to the prohibition of the Fourth Amendment of the Constitution, as well as of the Fifth." <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#632" aria-description="Citation for case: Boyd v. United States"><i>Id.</i> at 632</a></span>. See <i>Adams</i> v. <i>New York,</i> <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/#597" aria-description="Citation for case: Adams v. New York">192 U. S. 585, 597, 598</a></span>. The view that the Fourth Amendment itself forbids the introduction of evidence illegally obtained in federal prosecutions is one of long standing and firmly established. See <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#462" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 462</a></span>. It is too late in my judgment to question it now. We apply it today in <i>Lustig</i> v. <i>United States, post,</i> p. 74.</p>
<p>As Congress and this Court are, in my judgment, powerless to permit the admission in federal courts of evidence seized in defiance of the Fourth Amendment, so I think state legislators and judgesif subject to the Amendment, as I believe them to bemay not lend their offices to the admission in state courts of evidence thus seized. Compliance with the Bill of Rights betokens more than lip service.</p>
<p>The Court makes the illegality of this search and seizure its inarticulate premise of decision. I acquiesce in that premise and think the convictions should be reversed.</p>
<p>MR. JUSTICE MURPHY joins in this opinion.</p>
<h2>NOTES</h2>
<p>[1]  The common law provides actions for damages against the searching officer, e. g., <i>Entick</i> v. <i>Carrington,</i> 2 Wils. 275, 19 How. St. Tr. 1029; <i>Grumon</i> v. <i>Raymond,</i> <span class="citation" data-id="6572959"><a href="/opinion/6693083/grumon-v-raymond/" aria-description="Citation for case: Grumon v. Raymond">1 Conn. 40</a></span>; <i>Sandford</i> v. <i>Nichols,</i> <span class="citation" data-id="6404479"><a href="/opinion/6530776/sandford-v-nichols/" aria-description="Citation for case: Sandford v. Nichols">13 Mass. 286</a></span>; <i>Halsted</i> v. <i>Brice,</i> <span class="citation" data-id="6613020"><a href="/opinion/6731385/halsted-v-brice/" aria-description="Citation for case: Halsted v. Brice">13 Mo. 171</a></span>; <i>Hussey</i> v. <i>Davis,</i> 58 N. H. 317; <i>Reed</i> v. <i>Lucas,</i> <span class="citation" data-id="4892398"><a href="/opinion/5076811/reed-v-lucas/" aria-description="Citation for case: Reed v. Lucas">42 Texas 529</a></span>; against one who procures the issuance of a warrant maliciously and without probable cause, e. g., <i>Gulsby</i> v. <i>Louisville &amp; N. R. Co.,</i> <span class="citation" data-id="7365014"><a href="/opinion/7444823/gulsby-v-louisville-nashville-r-r/" aria-description="Citation for case: Gulsby v. Louisville &amp; Nashville R. R.">167 Ala. 122</a></span>, <span class="citation" data-id="7365014"><a href="/opinion/7444823/gulsby-v-louisville-nashville-r-r/" aria-description="Citation for case: Gulsby v. Louisville &amp; Nashville R. R.">52 So. 392</a></span>; <i>Whitson</i> v. <i>May,</i> <span class="citation" data-id="7043683"><a href="/opinion/7136045/whitson-v-may/" aria-description="Citation for case: Whitson v. May">71 Ind. 269</a></span>; <i>Krehbiel</i> v. <i>Henkle,</i> <span class="citation" data-id="7114657"><a href="/opinion/7203240/krehbiel-v-henkle/" aria-description="Citation for case: Krehbiel v. Henkle">152 Iowa 604</a></span>, <span class="citation" data-id="7114378"><a href="/opinion/7202985/roberts-v-playle/" aria-description="Citation for case: Roberts v. Playle">129 N. W. 945</a></span>; <i>Olson</i> v. <i>Tvete,</i> <span class="citation" data-id="7966966"><a href="/opinion/8012053/olson-v-tvete/" aria-description="Citation for case: Olson v. Tvete">46 Minn. 225</a></span>, <span class="citation" data-id="7966966"><a href="/opinion/8012053/olson-v-tvete/" aria-description="Citation for case: Olson v. Tvete">48 N. W. 914</a></span>; <i>Boeger</i> v. <i>Langenberg,</i> <span class="citation" data-id="8009494"><a href="/opinion/8052623/boeger-v-langenberg/" aria-description="Citation for case: Boeger v. Langenberg">97 Mo. 390</a></span>, <span class="citation no-link">11 S. W. 223</span>; <i>Doane</i> v. <i>Anderson,</i> <span class="citation" data-id="5501189"><a href="/opinion/5654770/doane-v-anderson/" aria-description="Citation for case: Doane v. Anderson">60 Hun 586</a></span>, 15 N. Y. S. 459; <i>Shall</i> v. <i>Minneapolis, St. P. &amp; S. S. M. R. Co.,</i> <span class="citation" data-id="8191222"><a href="/opinion/8227270/shall-v-minneapolis-st-paul-sault-ste-marie-railway-co/" aria-description="Citation for case: Shall v. Minneapolis, St. Paul &amp; Sault Ste. Marie Railway...">156 Wis. 195</a></span>, <span class="citation" data-id="8191222"><a href="/opinion/8227270/shall-v-minneapolis-st-paul-sault-ste-marie-railway-co/" aria-description="Citation for case: Shall v. Minneapolis, St. Paul &amp; Sault Ste. Marie Railway...">145 N. W. 649</a></span>; against a magistrate who has acted without jurisdiction in issuing a warrant, e. g., <i>Williams</i> v. <i>Kozak,</i> <span class="citation" data-id="8825314"><a href="/opinion/8840170/williams-v-kozak/" aria-description="Citation for case: Williams v. Kozak">280 F. 373</a></span> (C. A. 4th Cir.); <i>Grumon</i> v. <i>Raymond,</i> <span class="citation" data-id="6572959"><a href="/opinion/6693083/grumon-v-raymond/" aria-description="Citation for case: Grumon v. Raymond">1 Conn. 40</a></span>; <i>Kennedy</i> v. <i>Terrill,</i> Hardin (Ky.) 490; <i>Shaw</i> v. <i>Moon,</i> <span class="citation" data-id="3839135"><a href="/opinion/4080582/shaw-v-moon/" aria-description="Citation for case: Shaw v. Moon">117 Ore. 558</a></span>, <span class="citation" data-id="3839135"><a href="/opinion/4080582/shaw-v-moon/" aria-description="Citation for case: Shaw v. Moon">245 P. 318</a></span>; and against persons assisting in the execution of an illegal search, e. g., <i>Hebrew</i> v. <i>Pulis,</i> 73 N. J. L. 621, 625, <span class="citation" data-id="8271776"><a href="/opinion/8304929/hebrew-v-pulis/#122" aria-description="Citation for case: Hebrew v. Pulis">64 A. 121, 122</a></span>; <i>Cartwright</i> v. <i>Canode,</i> <span class="citation" data-id="3932614"><a href="/opinion/4166002/cartwright-v-canode/" aria-description="Citation for case: Cartwright v. Canode">138 S. W. 792</a></span> (Tex. Civ. App.), aff'd, <span class="citation" data-id="3907069"><a href="/opinion/4143577/cartwright-v-canode/" aria-description="Citation for case: Cartwright v. Canode">106 Texas 502</a></span>, <span class="citation" data-id="3907069"><a href="/opinion/4143577/cartwright-v-canode/" aria-description="Citation for case: Cartwright v. Canode">171 S. W. 696</a></span>. One may also without liability use force to resist an unlawful search. E. g., <i>Commonwealth</i> v. <i>Martin,</i> <span class="citation" data-id="6416154"><a href="/opinion/6542429/commonwealth-v-certain-intoxicating-liquors/" aria-description="Citation for case: Commonwealth v. Certain Intoxicating Liquors">105 Mass. 178</a></span>; <i>State</i> v. <i>Mann,</i> <span class="citation" data-id="3659541"><a href="/opinion/3913233/state-v-mann/" aria-description="Citation for case: State v. Mann">27 N. C. 45</a></span>.
</p>
<p>Statutory sanctions in the main provide for the punishment of one maliciously procuring a search warrant or willfully exceeding his authority in exercising it. <i>E. g.,</i> 18 U. S. C. (1946 ed.) §§ 630, 631; Ala. Code, Tit. 15, § 99 (1940); Ariz. Code Ann. § 44-3513 (1939); <span class="citation no-link">Fla. Stat. Ann. §§ 933.16</span>, 933.17 (1944); <span class="citation no-link">Iowa Code §§ 751.38</span>, 751.39 (1946); Mont. Rev. Code Ann. §§ 10948, 10952 (1935); Nev. Comp. Laws §§ 10425, 10426 (1929); N. Y. Crim. Code §§ 811, 812, N. Y. Penal Law §§ 1786, 1847; N. D. Rev. Code §§ 12-1707, 12-1708 (1943); Okla. Stat. Ann., Tit. 21, §§ 536, 585, Tit. 22, §§ 1239, 1240 (1937); Ore. Comp. Laws Ann. § 26-1717 (1940); S. D. Code §§ 13.1213, 13.1234, 34.9904, 34.9905 (1939); <span class="citation no-link">Tenn. Code Ann. § 11905</span> (1934). Some statutes more broadly penalize unlawful searches. <i>E. g.,</i> 18 U. S. C. (1946 ed.) § 53a; <span class="citation no-link">Idaho Code Ann. §§ 17-1004</span>, 17-1024 (1932); <span class="citation no-link">Minn. Stat. §§ 613.54</span>, 621.17 (1945); Va. Code Ann. § 4822d (Michie, 1942); Wash. Rev. Stat. Ann. §§ 2240-1, 2240-2. Virginia also makes punishable one who issues a general search warrant or a warrant unsupported by affidavit. Va. Code Ann. § 4822e (Michie, 1942). A few States have provided statutory civil remedies. See, <i>e. g.,</i> <span class="citation no-link">Ga. Code Ann. § 27-301</span> (1935); Ill. Rev. Stat., c. 38, § 698 (Smith-Hurd, 1935); <span class="citation no-link">Miss. Code Ann. § 1592</span> (1942). And in one State, misuse of a search warrant may be an abuse of process punishable as contempt of court. See Mich. Stat. Ann. § 27.511 (1938).</p>
<p>[2]  "We hold, then, with the defendant that the evidence against him was the outcome of a trespass. The officer might have been resisted, or sued for damages, or even prosecuted for oppression (Penal Law, §§ 1846, 1847). He was subject to removal or other discipline at the hands of his superiors. These consequences are undisputed. The defendant would add another. We must determine whether evidence of criminality, procured by an act of trespass, is to be rejected as incompetent for the misconduct of the trespasser. . . .
</p>
<p>"Those judgments [<i>Weeks</i> v. <i>United States</i> and cases which followed it] do not bind us, for they construe provisions of the Federal Constitution, the Fourth and Fifth Amendments, not applicable to the States. Even though not binding, they merit our attentive scrutiny. . . .</p>
<p>"In so holding [<i>i. e.,</i> that evidence procured by unlawful search is not incompetent], we are not unmindful of the argument that unless the evidence is excluded, the statute becomes a form and its protection an illusion. This has a strange sound when the immunity is viewed in the light of its origin and history. The rule now embodied in the statute was received into English law as the outcome of the prosecution of Wilkes and Entick . . . . Wilkes sued the messengers who had ransacked his papers, and recovered a verdict of £4,000 against one and £1,000 against the other. Entick, too, had a substantial verdict . . . . We do not know whether the public, represented by its juries, is to-day more indifferent to its liberties than it was when the immunity was born. If so, the change of sentiment without more does not work a change of remedy. Other sanctions, penal and disciplinary, supplementing the right to damages, have already been enumerated. No doubt the protection of the statute would be greater from the point of view of the individual whose privacy had been invaded if the government were required to ignore what it had learned through the invasion. The question is whether protection for the individual would not be gained at a disproportionate loss of protection for society. On the one side is the social need that crime shall be repressed. On the other, the social need that law shall not be flouted by the insolence of office. There are dangers in any choice. The rule of the <i>Adams</i> case [<span class="citation multiple-matches"><a href="/c/N.%20Y./176/351/">176 N. Y. 351</a></span>, <span class="citation" data-id="3588018"><a href="/opinion/3606309/people-v-adams/" aria-description="Citation for case: People v. . Adams">68 N. E. 636</a></span>] strikes a balance between opposing interests." <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#19" aria-description="Citation for case: People v. Defore">242 N. Y. at 19, 20, 24-25</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#586" aria-description="Citation for case: People v. Defore">150 N. E. at 586-87, 587, 588-89</a></span>.</p>
<p>[*]  In the case of jurisdictions which have decided more than one case in point, the following Tables cite only the leading case.</p>
<p>[1]  See Pound, Criminal Justice in America (New York, 1930): "Under our legal system the way of the prosecutor is hard, and the need of `getting results' puts pressure upon prosecutors to . . . indulge in that lawless enforcement of law which produces a vicious circle of disrespect for law." P. 186.
</p>
<p>And note the statement of the Wickersham Commission, with reference to arrests: ". . . in case of persons of no influence or little or no means the legal restrictions are not likely to give an officer serious trouble." II National Commission on Law Observance and Enforcement, Report on Criminal Procedure (1931), p. 19.</p>
<p>[2]  See McCormick, Damages, § 78. See Willis, <i>Measure of Damages When Property is Wrongfully Taken by a Private Individual,</i> <span class="citation no-link">22 Harv. L. Rev. 419</span>.</p>
<p>[3]  <i><span class="citation no-link">Id.,</span></i> § 79. See <i>Fennemore</i> v. <i>Armstrong,</i> <span class="citation" data-id="6556335"><a href="/opinion/6677276/fennemore-v-armstrong/" aria-description="Citation for case: Fennemore v. Armstrong">29 Del. 35</a></span>, <span class="citation" data-id="6556335"><a href="/opinion/6677276/fennemore-v-armstrong/" aria-description="Citation for case: Fennemore v. Armstrong">96 A. 204</a></span>.</p>
<p>[4]  "It is a well settled and almost universally accepted rule in the law of damages that a finding of exemplary damages must be predicated upon a finding of actual damages." <span class="citation no-link">17 Iowa L. Rev. 413</span>, 414. This appears to be an overstatement. See McCormick, <i>supra,</i> § 83; Restatement IV, Torts, § 908, comment <i>c.</i></p>
<p>[5]  The material which follows is gleaned from letters and other material from Commissioners of Police and Chiefs of Police in twenty-six cities. Thirty-eight large cities in the United States were selected at random, and inquiries directed concerning the instructions provided police on the rules of search and seizure. Twenty-six replies have been received to date. Those of any significance are mentioned in the text of this opinion. The sample is believed to be representative, but it cannot, of course, substitute for a thoroughgoing comparison of present-day police procedures by a completely objective observer. A study of this kind would be of inestimable value.</p>
<p>[6]  <i>E. g.,</i> Assistant Superintendent Truscott's letter to the Washington Police Force of January 3, 1949, concerning <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>.</p>
<p>[7]  Recently lectures have included two pages of discussion of the opinions in <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span>.</p>
<p>[8]  Chief of Police John W. Polcyn notes, in a Foreword to the book, that officers were often not properly informed with respect to searches and seizures before thoroughgoing instruction was undertaken. One of their fears was that of "losing their cases in court, only because they neglected to do what they might have done with full legal sanction at the time of the arrest, or did what they had no legal right to do at such time."</p>

</div>
```

---

## GROUP: content/cases/Franks v. Delaware.md  (`case`, 6 assertions)

### content_page

```
---
title: "Franks v. Delaware"
type: case
citation: "438 U.S. 154 (1978)"
parallel_cite: "98 S. Ct. 2674; 57 L. Ed. 2d 667"
neutral_cite: 1978 U.S. LEXIS 127
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1978
date_decided: 1978-06-26
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1978-06-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Franks v. Delaware
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109925/franks-v-delaware/"
  cluster_id: 109925
  opinion_id: 109925
  identity_checked: true
homes:
  - page: "[[Franks Challenges]]"
    role: "Key — Anchor"
  - page: "[[The Good-Faith Exception]]"
    role: "Related (cross-doctrine)"
related: ["[[Illinois v. Gates]]", "[[United States v. Leon]]", "[[Groh v. Ramirez]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant", "affidavit", "franks-hearing", "veracity"]
holding: "A warrant affidavit containing a knowing/intentional or reckless material falsehood may be challenged at a hearing on a substantial…"
lake:
  record_id: Franks v. Delaware
  status: verified
  projected_at: 2026-07-06
---

# Franks v. Delaware

*438 U.S. 154 (1978)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police obtained a warrant to search Jerome Franks's home in a rape investigation, relying in part on an affidavit reciting statements two officers attributed to named acquaintances about Franks's clothing. Franks contended the officers had not actually interviewed those people as the affidavit claimed and sought to prove the affidavit contained deliberate falsehoods. The Delaware Supreme Court held that a defendant may never go behind a facially sufficient warrant affidavit to attack its truthfulness.

## Issue
Whether a defendant ever has the right, after a warrant issues, to challenge the truthfulness of factual statements in the supporting affidavit — and to suppress the evidence if a deliberate or reckless falsehood necessary to probable cause is shown.

## Rule
Yes — on a substantial preliminary showing, the defendant is entitled to a veracity hearing, and a proven falsehood essential to probable cause voids the warrant. "[W]here the defendant makes a substantial preliminary showing that a false statement knowingly and intentionally, or with reckless disregard for the truth, was included by the affiant in the warrant affidavit, and if the allegedly false statement is necessary to the finding of probable cause, the Fourth Amendment requires that a hearing be held at the defendant's request." — 438 U.S. at 155–156. ^pin-155

"In the event that at that hearing the allegation of perjury or reckless disregard is established by the defendant by a preponderance of the evidence, and, with the affidavit's false material set to one side, the affidavit's remaining content is insufficient to establish probable cause, the search warrant must be voided and the fruits of the search excluded." — *Id.* at 156. ^pin-156

## Application
Franks made specific allegations — backed by an offer of proof — that the affiants had fabricated the statements they attributed to his acquaintances, and those statements bore on probable cause. Because that was the kind of substantial preliminary showing of deliberate or reckless falsehood that entitles a defendant to go behind the affidavit, the Delaware courts erred in treating such a challenge as categorically barred.

## Conclusion
A defendant may challenge a warrant affidavit's veracity on a substantial preliminary showing; the Delaware Supreme Court's categorical bar was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The "Franks hearing" remains the standard mechanism for attacking deliberate or reckless falsehoods in a warrant affidavit.

## Appears on
- [[Franks Challenges]] — *Key — Anchor*
- [[The Exclusionary Rule]] — *Related (cross-doctrine)*

## Sources
- *Franks v. Delaware*, 438 U.S. 154 (1978) — https://www.courtlistener.com/opinion/109925/franks-v-delaware/ — pinpoints: 155, 156.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ecd7c009969ede8c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "438 U.S. 154 (1978)", "court": "U.S. Supreme Court", "neutral_cite": "1978 U.S. LEXIS 127", "official_citation_present": true, "parallel_cite": "98 S. Ct. 2674; 57 L. Ed. 2d 667", "title": "Franks v. Delaware", "year": "1978"}}
{"assertion_id": "742b1d3d7727803e", "dimension": "support", "kind": "home_role", "locator": {"home": "The Good-Faith Exception"}, "payload": {"home": "The Good-Faith Exception", "role": "Related (cross-doctrine)", "title": "Franks v. Delaware"}}
{"assertion_id": "83496f6d3855c7f5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrant affidavit containing a knowing/intentional or reckless material falsehood may be challenged at a hearing on a substantial…", "title": "Franks v. Delaware"}}
{"assertion_id": "f8dd52573b5212e9", "dimension": "support", "kind": "home_role", "locator": {"home": "Franks Challenges"}, "payload": {"home": "Franks Challenges", "role": "Key — Anchor", "title": "Franks v. Delaware"}}
{"assertion_id": "b05b8452b70a4093", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1978-06-26", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Franks v. Delaware", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Franks v. Delaware", "varies_by_point": "false"}}
{"assertion_id": "e1701cdd5b97c06c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Franks v. Delaware"}}
```

### lake record — Franks v. Delaware

```json
{
  "schema_version": "s2.v1",
  "record_id": "Franks v. Delaware",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Franks v. Delaware",
    "case_name_short": "Franks",
    "case_name_full": "Franks v. Delaware",
    "input_case_name": "Franks v. Delaware",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1978-06-26",
    "year": 1978,
    "docket": null,
    "cluster_id": 109925,
    "lead_opinion_id": 109925,
    "sibling_ids": [
      109925,
      9427321,
      9427322
    ],
    "absolute_url": "/opinion/109925/franks-v-delaware/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9016328,
        "score": 20,
        "case_name": "Franks v. Delaware"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "438 U.S. 154",
      "volume": "438",
      "reporter": "U.S.",
      "page": "154",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "98 S. Ct. 2674",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "2674",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 L. Ed. 2d 667",
        "volume": "57",
        "reporter": "L. Ed. 2d",
        "page": "667",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1978 U.S. LEXIS 127",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "127",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "438 U.S. 154",
        "volume": "438",
        "reporter": "U.S.",
        "page": "154",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 S. Ct. 2674",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "2674",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 L. Ed. 2d 667",
        "volume": "57",
        "reporter": "L. Ed. 2d",
        "page": "667",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1978 U.S. LEXIS 127",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "127",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "438 U.S. 154",
    "official_selection": {
      "court_class": "scotus",
      "selected": "438 U.S. 154",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-155",
      "page": null,
      "quote": "--- # Franks v. Delaware *438 U.S. 154 (1978)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police obtained a warrant to search Jerome Franks's home in a rape investigation, relying in part on an affidavit reciting statements two officers attributed to named acquaintances about Franks's clothing. Franks contended the officers had not actually interviewed those people as the affidavit claimed and sought to prove the affidavit contained deliberate falsehoods. The Delaware Supreme Court held that a defendant may never go behind a facially sufficient warrant affidavit to attack its truthfulness. ## Issue Whether a defendant ever has the right, after a warrant issues, to challenge the truthfulness of factual statements in the supporting affidavit \u2014 and to suppress the evidence if a deliberate or reckless falsehood necessary to probable cause is shown. ## Rule Yes \u2014 on a substantial preliminary showing, the defendant is entitled to a veracity hearing, and a proven falsehood essential to probable cause voids the warrant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-156",
      "page": null,
      "quote": "In the event that at that hearing the allegation of perjury or reckless disregard is established by the defendant by a preponderance of the evidence, and, with the affidavit's false material set to one side, the affidavit's remaining content is insufficient to establish probable cause, the search warrant must be voided and the fruits of the search excluded.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1978-06-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Franks v. Delaware",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 10705828,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fields",
          "cluster_id": 10309030,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Seneca Warrior Steeprock",
          "cluster_id": 10102625,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Dunn",
          "cluster_id": 9500669,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Jesse Jon Harbach",
          "cluster_id": 9493041,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Whitfield",
          "cluster_id": 9400623,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane1_negative"
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
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
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
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ashcroft v. al-Kidd",
          "cluster_id": 217703,
          "cite": [
            "179 L. Ed. 2d 1149",
            "131 S. Ct. 2074",
            "563 U.S. 731",
            "2011 U.S. LEXIS 4021"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County Court of Ulster Cty. v. Allen",
          "cluster_id": 110093,
          "cite": [
            "60 L. Ed. 2d 777",
            "99 S. Ct. 2213",
            "442 U.S. 140",
            "1979 U.S. LEXIS 124"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herring v. United States",
          "cluster_id": 145922,
          "cite": [
            "172 L. Ed. 2d 496",
            "129 S. Ct. 695",
            "555 U.S. 135",
            "2009 U.S. LEXIS 581"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Dominguez-Castor",
          "cluster_id": 4691722,
          "cite": [
            "2020 COA 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mills v. Maryland",
          "cluster_id": 112085,
          "cite": [
            "100 L. Ed. 2d 384",
            "108 S. Ct. 1860",
            "486 U.S. 367",
            "1988 U.S. LEXIS 2488",
            "56 U.S.L.W. 4503"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
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
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jerry L. Branch, Valenna Branch, Colby Branch v. Dale L. Tunnell, Individually and as Special Agent of Bureau of Land Management, State of Montana",
          "cluster_id": 660713,
          "cite": [
            "14 F.3d 449",
            "94 Cal. Daily Op. Serv. 253",
            "28 Fed. R. Serv. 3d 1211",
            "94 Daily Journal DAR 442",
            "1994 U.S. App. LEXIS 409",
            "1994 WL 5496"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karo",
          "cluster_id": 111257,
          "cite": [
            "82 L. Ed. 2d 530",
            "104 S. Ct. 3296",
            "468 U.S. 705",
            "1984 U.S. LEXIS 148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Marshall",
          "cluster_id": 1969802,
          "cite": [
            "690 A.2d 1",
            "148 N.J. 89",
            "1997 N.J. LEXIS 70"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1239150,
          "cite": [
            "15 Cal. 4th 1229",
            "939 P.2d 259",
            "97 Daily Journal DAR 9003",
            "97 Cal. Daily Op. Serv. 5537",
            "65 Cal. Rptr. 2d 145",
            "1997 Cal. LEXIS 3699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. Greenfield",
          "cluster_id": 111553,
          "cite": [
            "88 L. Ed. 2d 623",
            "106 S. Ct. 634",
            "474 U.S. 284",
            "1986 U.S. LEXIS 41",
            "54 U.S.L.W. 4077"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Williams",
          "cluster_id": 112730,
          "cite": [
            "118 L. Ed. 2d 352",
            "112 S. Ct. 1735",
            "504 U.S. 36",
            "1992 U.S. LEXIS 2688"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Martinez v. State",
          "cluster_id": 1561283,
          "cite": [
            "17 S.W.3d 677",
            "2000 Tex. Crim. App. LEXIS 53",
            "2000 WL 628325"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sykes v. Anderson",
          "cluster_id": 178987,
          "cite": [
            "625 F.3d 294",
            "2010 U.S. App. LEXIS 23204",
            "2010 WL 4453313"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gregory v. City of Louisville",
          "cluster_id": 2973641,
          "cite": [
            "444 F.3d 725",
            "2006 WL 909935"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Robinson",
          "cluster_id": 1539942,
          "cite": [
            "974 A.2d 1057",
            "200 N.J. 1",
            "2009 N.J. LEXIS 804"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Panah",
          "cluster_id": 2509294,
          "cite": [
            "107 P.3d 790",
            "25 Cal. Rptr. 3d 672",
            "35 Cal. 4th 395",
            "2005 Cal. Daily Op. Serv. 2194",
            "2005 Daily Journal DAR 3023",
            "2005 Cal. LEXIS 2712"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pagan v. State",
          "cluster_id": 1110208,
          "cite": [
            "830 So. 2d 792",
            "2002 WL 500315"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Janecka v. State",
          "cluster_id": 1743739,
          "cite": [
            "937 S.W.2d 456",
            "1996 Tex. Crim. App. LEXIS 240",
            "1996 WL 682137"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tyron Brown v. Lee Lucas",
          "cluster_id": 2675935,
          "cite": [
            "753 F.3d 606",
            "2014 WL 2198419",
            "2014 U.S. App. LEXIS 9771"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Letner and Tobin",
          "cluster_id": 2630926,
          "cite": [
            "235 P.3d 62",
            "50 Cal. 4th 99",
            "112 Cal. Rptr. 3d 746",
            "2010 Cal. LEXIS 7290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Waclawski",
          "cluster_id": 1703326,
          "cite": [
            "780 N.W.2d 321",
            "286 Mich. App. 634"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Greg Myers, Etc. v. R. Kathleen Morris, Scott County Attorney, Etc.",
          "cluster_id": 482831,
          "cite": [
            "810 F.2d 1437"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109925 OR 9427321 OR 9427322) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjcxNTgwODAwMDAwJnM9OTM2NzYxNiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109925+OR+9427321+OR+9427322%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109925 OR 9427321 OR 9427322)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00Mjkmcz0yNzA0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109925+OR+9427321+OR+9427322%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109925 OR 9427321 OR 9427322)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzAzNzIxNjAwMDAwJnM9OTQ1NTgxNiZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109925+OR+9427321+OR+9427322%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109925 OR 9427321 OR 9427322)",
    "indexed_citing_opinions": 5121,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109925,
        "count": 4294,
        "count_source": "search"
      },
      {
        "opinion_id": 9427321,
        "count": 880,
        "count_source": "search"
      },
      {
        "opinion_id": 9427322,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 8699,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/franks-v-delaware.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk1MDQ4NiZzPTEwNjU4ODk4JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109925+OR+9427321+OR+9427322%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109925,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 98212,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 104373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 105925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 106783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 107951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 108302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 108582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 109302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 299224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 307033,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 316109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 317254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 318456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 324012,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 327139,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 331000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 338659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 338672,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 340645,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1130838,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1148533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1163909,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1176912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1180163,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1183476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1190217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1198737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1285341,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1306980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1311035,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1312713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1353828,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1363434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1367322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1367376,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1391098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1415130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1424506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1437089,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1445282,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1451648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1452068,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1498442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1530851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1600679,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1631048,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1760963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1768917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1769197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1828817,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1850125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1851918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1886978,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1895767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1973195,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1987009,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2053522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2060217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2120568,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2133918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2184913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2215694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2221046,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2233092,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2341043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2349003,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2356548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2379504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2386408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2398659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2442476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2467369,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2609109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 3423317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 3486405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 3493017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 3535850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 3744266,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 3865272,
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
    "date_created": "2026-07-05T04:50:20Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T04:50:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T04:50:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T04:55:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T04:50:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Franks v. Delaware

```
<div>
<center><b><span class="citation" data-id="9427321"><a href="/opinion/109925/franks-v-delaware/" aria-description="Citation for case: Franks v. Delaware">438 U.S. 154</a></span> (1978)</b></center>
<center><h1>FRANKS<br>
v.<br>
DELAWARE.</h1></center>
<center>No. 77-5176.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 27, 1978.</center>
<center>Decided June 26, 1978.</center>
CERTIORARI TO THE SUPREME COURT OF DELAWARE.
<p><span class="star-pagination">*155</span> <i>Donald W. Huntley</i> argued the cause and filed briefs for petitioner.</p>
<p><i>Harrison F. Turner,</i> Deputy Attorney General of Delaware, argued the cause for respondent. With him on the brief was <i>Richard R. Wier, Jr.,</i> Attorney General.<sup>[*]</sup></p>
<p>MR. JUSTICE BLACKMUN delivered the opinion of the Court.</p>
<p>This case presents an important and longstanding issue of Fourth Amendment law. Does a defendant in a criminal proceeding ever have the right, under the Fourth and Fourteenth Amendments, subsequent to the <i>ex parte</i> issuance of a search warrant, to challenge the truthfulness of factual statements made in an affidavit supporting the warrant?</p>
<p>In the present case the Supreme Court of Delaware held, as a matter of first impression for it, that a defendant under <i>no</i> circumstances may so challenge the veracity of a sworn statement used by police to procure a search warrant. We reverse, and we hold that, where the defendant makes a substantial preliminary showing that a false statement knowingly and intentionally, or with reckless disregard for the truth, was <span class="star-pagination">*156</span> included by the affiant in the warrant affidavit, and if the allegedly false statement is necessary to the finding of probable cause, the Fourth Amendment requires that a hearing be held at the defendant's request. In the event that at that hearing the allegation of perjury or reckless disregard is established by the defendant by a preponderance of the evidence, and, with the affidavit's false material set to one side, the affidavit's remaining content is insufficient to establish probable cause, the search warrant must be voided and the fruits of the search excluded to the same extent as if probable cause was lacking on the face of the affidavit.</p>
<p></p>
<h2>I</h2>
<p>The controversy over the veracity of the search warrant affidavit in this case arose in connection with petitioner Jerome Franks' state conviction for rape, kidnaping, and burglary. On Friday, March 5, 1976, Mrs. Cynthia Bailey told police in Dover, Del., that she had been confronted in her home earlier that morning by a man with a knife, and that he had sexually assaulted her. She described her assailant's age, race, height, build, and facial hair, and gave a detailed description of his clothing as consisting of a white thermal undershirt, black pants with a silver or gold buckle, a brown leather three-quarter-length coat, and a dark knit cap that he wore pulled down around his eyes.</p>
<p>That same day, petitioner Franks coincidentally was taken into custody for an assault involving a 15-year-old girl, Brenda B. ______, six days earlier. After his formal arrest, and while awaiting a bail hearing in Family Court, petitioner allegedly stated to Robert McClements, the youth officer accompanying him, that he was surprised the bail hearing was "about Brenda B. ______. I know her. I thought you said Bailey. I don't know her." Tr. 175, 186. At the time of this statement, the police allegedly had not yet recited to petitioner his rights under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966).</p>
<p><span class="star-pagination">*157</span> On the following Monday, March 8, Officer McClements happened to mention the courthouse incident to a detective, Ronald R. Brooks, who was working on the Bailey case. Tr. 186, 190-191. On March 9, Detective Brooks and Detective Larry D. Gray submitted a sworn affidavit to a Justice of the Peace in Dover, in support of a warrant to search petitioner's apartment.<sup>[1]</sup> In paragraph 8 of the affidavit's "probable cause page" mention was made of petitioner's statement to McClements. In paragraph 10, it was noted that the description of the assailant given to the police by Mrs. Bailey included the above-mentioned clothing. Finally, the affidavit also described the attempt made by police to confirm that petitioner's typical outfit matched that of the assailant. Paragraph 15 recited: "On Tuesday, 3/9/76, your affiant contacted Mr. James Williams and Mr. Wesley Lucas of the Delaware Youth Center where Jerome Franks is employed and did have personal conversation with both these people." Paragraphs 16 and 17 respectively stated: "Mr. James Williams revealed to your affiant that the normal dress of Jerome Franks does consist of a white knit thermal undershirt and a brown leather jacket," and "Mr. Wesley Lucas revealed to your affiant that in addition to the thermal undershirt and jacket, Jerome Franks often wears a dark green knit hat."</p>
<p>The warrant was issued on the basis of this affidavit. App. 9. Pursuant to the warrant, police searched petitioner's apartment and found a white thermal undershirt, a knit hat, dark pants, and a leather jacket, and, on petitioner's kitchen table, a single-blade knife. All these ultimately were introduced in evidence at trial.</p>
<p>Prior to the trial, however, petitioner's counsel filed a written motion to suppress the clothing and the knife found in the search; this motion alleged that the warrant on its face did not show probable cause and that the search and seizure were <span class="star-pagination">*158</span> in violation of the Fourth and Fourteenth Amendments. <i>Id.,</i> at 11-12. At the hearing on the motion to suppress, defense counsel orally amended the challenge to include an attack on the veracity of the warrant affidavit; he also specifically requested the right to call as witnesses Detective Brooks, Wesley Lucas of the Youth Center, and James D. Morrison, formerly of the Youth Center.<sup>[2]</sup><i>Id.,</i> at 14-17. Counsel asserted that Lucas and Morrison would testify that neither had been personally interviewed by the warrant affiants, and that, although they might have talked to another police officer, any information given by them to that officer was "somewhat different" from what was recited in the affidavit. <i>Id.,</i> at 16. Defense counsel charged that the misstatements were included in the affidavit not inadvertently, but in "bad faith." <i>Id.,</i> at 25. Counsel also sought permission to call Officer McClements and petitioner as witnesses, to seek to establish that petitioner's courthouse statement to police had been obtained in violation of petitioner's <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, and that the search warrant was thereby tainted as the fruit of an illegally obtained confession. <i>Id.,</i> at 17, 27.</p>
<p>In rebuttal, the State's attorney argued in detail, App. 15-24, (a) that Del. Code Ann., Tit. 11, §§ 2306, 2307 (1974), contemplated that any challenge to a search warrant was to be limited to questions of sufficiency based on the face of the affidavit; (b) that, purportedly, a majority of the States whose <span class="star-pagination">*159</span> practice was not dictated by statute observed such a rule;<sup>[3]</sup> and (c) that federal cases on the issue were to be distinguished because of Fed. Rule Crim. Proc. 41 (e).<sup>[4]</sup> He also noted that <span class="star-pagination">*160</span> this Court had reserved the general issue of subfacial challenge to veracity in <i>Rugendorf</i> v. <i>United States,</i> <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/#531" aria-description="Citation for case: Rugendorf v. United States">376 U. S. 528, 531-532</a></span> (1964). when it disposed of that case on the ground that, even if a veracity challenge were permitted, the alleged factual inaccuracies in that case's affidavit "were of only peripheral relevancy to the showing of probable cause, and, not being within the personal knowledge of the affiant, did not go to the integrity of the affidavit." <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/#532" aria-description="Citation for case: Rugendorf v. United States"><i>Id.,</i> at 532</a></span>. The State objected to petitioner's "going behind [the warrant affidavit] in any way," and argued that the court must decide petitioner's motion "on the four corners" of the affidavit. App. 21.</p>
<p>The trial court sustained the State's objection to petitioner's proposed evidence. <i>Id.,</i> at 25, 27. The motion to suppress was denied, and the clothing and knife were admitted as evidence at the ensuing trial. Tr. 192-196. Petitioner was convicted. In a written motion for judgment of acquittal and/or new trial, Record Doc. No. 23, petitioner repeated his objection to the admission of the evidence, stating that he "should have been allowed to impeach the Affidavit used in the Search Warrant to show purposeful misrepresentation of information contained therein." <i>Id.,</i> at 2. The motion was denied, and petitioner was sentenced to two consecutive terms of 25 years each and an additional consecutive life sentence.</p>
<p>On appeal, the Supreme Court of Delaware affirmed. <span class="citation" data-id="2356548"><a href="/opinion/2356548/franks-v-state/" aria-description="Citation for case: Franks v. State">373 A. 2d 578</a></span> (1977). It agreed with what it deemed to be the "majority rule" that no attack upon the veracity of a warrant affidavit could be made:</p>
<blockquote>"We agree with the majority rule for two reasons. First, it is the function of the issuing magistrate to determine the reliability of information and credibility of affiants in deciding whether the requirement of probable cause has been met. There has been no need demonstrated for interfering with this function. Second, neither the probable cause nor suppression hearings are adjudications of guilt or innocence; the matters asserted by defendant are <span class="star-pagination">*161</span> more properly considered in a trial on the merits." <span class="citation" data-id="2356548"><a href="/opinion/2356548/franks-v-state/#580" aria-description="Citation for case: Franks v. State"><i>Id.,</i> at 580</a></span>.</blockquote>
<p>Because of this resolution, the Delaware Supreme Court noted that there was no need to consider petitioner's "other contentions, relating to the evidence that would have been introduced for impeachment purposes." <i><span class="citation" data-id="2356548"><a href="/opinion/2356548/franks-v-state/" aria-description="Citation for case: Franks v. State">Ibid.</a></span></i></p>
<p>Franks' petition for certiorari presented only the issue whether the trial court had erred in refusing to consider his allegation of misrepresentation in the warrant affidavit.<sup>[5]</sup> Because of the importance of the question, and because of the conflict among both state and federal courts, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./434/889/">434 U. S. 889</a></span> (1977).</p>
<p></p>
<h2>II</h2>
<p>It may be well first to note how we are compelled to reach the Fourth Amendment issue proffered in this case. In particular, the State's proposals of an independent and adequate state ground and of harmless error do not dispose of the controversy.</p>
<p>Respondent argues that petitioner's trial counsel, who is not the attorney representing him in this Court, failed to include the challenge to the veracity of the warrant affidavit in the written motion to suppress filed before trial, contrary to the requirement of Del. Super. Ct. Rule Crim. Proc. 41 (e) that a motion to suppress "shall state the grounds upon which it is made." The Supreme Court of Delaware, however, disposed of petitioner's Fourth Amendment claim on the merits. A ruling on the merits of a federal question by the highest state court leaves the federal question open to review <span class="star-pagination">*162</span> in this Court. <i>Manhattan Life Ins. Co.</i> v. <i>Cohen,</i> <span class="citation" data-id="98212"><a href="/opinion/98212/manhattan-life-ins-co-of-ny-v-cohen/#134" aria-description="Citation for case: Manhattan Life Ins. Co. of NY v. Cohen">234 U. S. 123, 134</a></span> (1914); <i>Raley</i> v. <i>Ohio,</i> <span class="citation" data-id="105925"><a href="/opinion/105925/raley-v-ohio/#436" aria-description="Citation for case: Raley v. Ohio">360 U. S. 423, 436-437</a></span> (1959); <i>Boykin</i> v. <i>Alabama,</i> <span class="citation" data-id="9424054"><a href="/opinion/107951/boykin-v-alabama/#241" aria-description="Citation for case: Boykin v. Alabama">395 U. S. 238, 241-242</a></span> (1969).</p>
<p>Respondent next suggests that any error here was harmless. Assuming, <i>arguendo,</i> respondent says, that petitioner's Fourth Amendment claim was valid, and that the warrant should have been tested for veracity and the evidence excluded, it is still clear beyond a reasonable doubt that the evidence complained of did not contribute to petitioner's conviction. <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 52-53</a></span> (1970). This contention falls of its own weight. The sole issue at trial was that of consent. Petitioner admitted, App. 37, that he had engaged in sexual relations with Mrs. Bailey on the day in question. She testified, Tr. 50-51, 69-70, that she had not consented to this, and that petitioner, upon first encountering her in the house, had threatened her with a knife to force her to submit. Petitioner claimed that she had given full consent and that no knife had been present. <i>Id.,</i> at 254, 271. To corroborate its contention that consent was lacking, the State introduced in evidence a stainless steel, wooden-handled kitchen knife found by the detectives on the kitchen table in petitioner's apartment four days after the alleged rape. <i>Id.,</i> at 195-196; Magistrate's Return on the Search Warrant March 9, 1976, Record Doc. No. 23. Defense counsel objected to its admission, arguing that Mrs. Bailey had not given any detailed description of the knife alleged to be involved in the incident and had claimed to have seen the knife only in "pitch blackness." Tr. 195. The State obtained its admission, however, as a knife that matched the description contained in the search warrant, and Mrs. Bailey testified that the knife allegedly used was, like the knife in evidence, single-edged and not a pocket knife, and that the knife in evidence was the same length and thickness as the knife used in the crime. <i>Id.,</i> at 69, 114-115. The State carefully elicited from Detective Brooks the fact that this was the only knife found in petitioner's <span class="star-pagination">*163</span> apartment. <i>Id.,</i> at 196. Although respondent argues that the knife was presented to the jury as "merely exemplary of the generic class of weapon testimonially described by the victim," Brief for Respondent 15-16, the State at trial clearly meant to suggest that this was the knife that had been used against Mrs. Bailey. Had the warrant been quashed, and the knife excluded from the trial as evidence, we cannot say with any assurance that the jury would have reached the same decision on the issue of consent, particularly since there was countervailing evidence on that issue.</p>
<p>We should note, in addition, why this case cannot be treated as was the situation in <i>Rugendorf</i> v. <i>United States</i><i>.</i> There the Court held that no Fourth Amendment question was presented when the claimed misstatements in the search warrant affidavit "were of only peripheral relevancy to the showing of probable cause, <i>and,</i> not being within the personal knowledge of the affiant, did not go to the integrity of the affidavit." <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/#532" aria-description="Citation for case: Rugendorf v. United States">376 U. S., at 532</a></span> (emphasis added). <i><span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">Rugendorf</a></span></i> emphasized that the "erroneous statements . . . were not those of the affiant" and thus "fail[ed] to show that the affiant was in bad faith or that he made any misrepresentations to the Commissioner in securing the warrant." <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/#533" aria-description="Citation for case: Rugendorf v. United States"><i>Id.,</i> at 533</a></span>.<sup>[6]</sup> Here, <span class="star-pagination">*164</span> whatever the judgment may be as to the relevancy of the alleged misstatements, the integrity of the affidavit was directly placed in issue by petitioner in his allegation that the affiants did not, as claimed, speak directly to Lucas and Morrison. Whether such conversations took place is surely a matter "within the personal knowledge of the affiant[s]." We also might note that although respondent's brief puts forth that the alleged misrepresentations in the affidavit were of little importance in establishing probable cause, Brief for Respondent 16, respondent at oral argument appeared to disclaim any reliance on <i><span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">Rugendorf</a></span>.</i> Tr. of Oral Arg. 30.</p>
<p></p>
<h2>III</h2>
<p>Whether the Fourth and Fourteenth Amendments, and the derivative exclusionary rule made applicable to the States under <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), ever mandate that a defendant be permitted to attack the veracity of a warrant affidavit after the warrant has been issued and executed, is a question that encounters conflicting values. The bulwark of Fourth Amendment protection, of course, is the Warrant Clause, requiring that, absent certain exceptions, police obtain a warrant from a neutral and disinterested magistrate before embarking upon a search. In deciding today that, in certain circumstances, a challenge to a warrant's veracity must be permitted, we derive our ground from language of the Warrant Clause itself, which surely takes the affiant's good faith as its premise: "[N]o Warrants shall issue, but upon probable cause, supported by Oath or affirmation . . . ." Judge Frankel, in <i>United States</i> v. <i>Halsey,</i> <span class="citation" data-id="1600679"><a href="/opinion/1600679/united-states-v-halsey/#1005" aria-description="Citation for case: United States v. Halsey">257 F. Supp. 1002, 1005</a></span> (SDNY 1966), aff'd, Docket No. 31369 (CA2, June 12, 1967) (unreported), put the matter simply: "[W]hen the Fourth Amendment demands a factual showing sufficient to comprise `probable cause,' the obvious assumption is that there will be a <span class="star-pagination">*165</span> <i>truthful</i> showing" (emphasis in original). This does not mean "truthful" in the sense that every fact recited in the warrant affidavit is necessarily correct, for probable cause may be founded upon hearsay and upon information received from informants, as well as upon information within the affiant's own knowledge that sometimes must be garnered hastily. But surely it is to be "truthful" in the sense that the information put forth is believed or appropriately accepted by the affiant as true. It is established law, see <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#47" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41, 47</a></span> (1933); <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#485" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 485-486</a></span> (1958); <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#114" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 114-115</a></span> (1964), that a warrant affidavit must set forth particular facts and circumstances underlying the existence of probable cause, so as to allow the magistrate to make an independent evaluation of the matter. If an informant's tip is the source of information, the affidavit must recite "some of the underlying circumstances from which the informant concluded" that relevant evidence might be discovered, and "some of the underlying circumstances from which the officer concluded that the informant, whose identity need not be disclosed,. . . was `credible' or his information `reliable.'" <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#114" aria-description="Citation for case: Aguilar v. Texas"><i>Id.,</i> at 114</a></span>. Because it is the magistrate who must determine independently whether there is probable cause, <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-14</a></span> (1948); <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#270" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 270-271</a></span> (1960), it would be an unthinkable imposition upon his authority if a warrant affidavit, revealed after the fact to contain a deliberately or recklessly false statement, were to stand beyond impeachment.</p>
<p>In saying this, however, one must give cognizance to competing values that lead us to impose limitations. They perhaps can best be addressed by noting the arguments of respondent and others against allowing veracity challenges. The arguments are several:</p>
<p>First, respondent argues that the exclusionary rule, created in <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), is not a <span class="star-pagination">*166</span> personal constitutional right, but only a judicially created remedy extended where its benefit as a deterrent promises to outweigh the societal cost of its use; that the Court has declined to apply the exclusionary rule when illegally seized evidence is used to impeach the credibility of a defendant's testimony, <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954), is used in a grand jury proceeding, <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U. S. 338</a></span> (1974), or is used in a civil trial, <i>United States</i> v. <i>Janis,</i> <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">428 U. S. 433</a></span> (1976); and that the Court similarly has restricted application of the Fourth Amendment exclusionary rule in federal habeas corpus review of a state conviction. See <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U. S. 465</a></span> (1976). Respondent argues that applying the exclusionary rule to another situationthe deterrence of deliberate or reckless untruthfulness in a warrant affidavitis not justified for many of the same reasons that led to the above restrictions; interfering with a criminal conviction in order to deter official misconduct is a burden too great to impose on society.</p>
<p>Second, respondent argues that a citizen's privacy interests are adequately protected by a requirement that applicants for a warrant submit a sworn affidavit and by the magistrate's independent determination of sufficiency based on the face of the affidavit. Applying the exclusionary rule to attacks upon veracity would weed out a minimal number of perjuries government statements, says respondent, but would overlap unnecessarily with existing penalties against perjury, including criminal prosecutions, departmental discipline for misconduct, contempt of court, and civil actions.</p>
<p>Third, it is argued that the magistrate already is equipped to conduct a fairly vigorous inquiry into the accuracy of the factual affidavit supporting a warrant application. He may question the affiant, or summon other persons to give testimony at the warrant proceeding. The incremental gain from a post-search adversary proceeding, it is said, would not be great.</p>
<p><span class="star-pagination">*167</span> Fourth, it is argued that it would unwisely diminish the solemnity and moment of the magistrate's proceeding to make his inquiry into probable cause reviewable in regard to veracity. The less final, and less deference paid to, the magistrate's determination of veracity, the less initiative will he use in that task. Denigration of the magistrate's function would be imprudent insofar as his scrutiny is the last bulwark preventing any particular invasion of privacy before it happens.</p>
<p>Fifth, it is argued that permitting a post-search evidentiary hearing on issues of veracity would confuse the pressing issue of guilt or innocence with the collateral question as to whether there had been official misconduct in the drafting of the affidavit. The weight of criminal dockets, and the need to prevent diversion of attention from the main issue of guilt or innocence, militate against such an added burden on the trial courts. And if such hearings were conducted routinely, it is said, they would be misused by defendants as a convenient source of discovery. Defendants might even use the hearings in an attempt to force revelation of the identity of informants.</p>
<p>Sixth and finally, it is argued that a post-search veracity challenge is inappropriate because the accuracy of an affidavit in large part is beyond the control of the affiant. An affidavit may properly be based on hearsay, on fleeting observations, and on tips received from unnamed informants whose identity often will be properly protected from revelation under <i>McCray</i> v. <i>Illinois,</i> <span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300</a></span> (1967).</p>
<p>None of these considerations is trivial. Indeed, because of them, the rule announced today has a limited scope, both in regard to when exclusion of the seized evidence is mandated, and when a hearing on allegations of misstatements must be accorded. But neither do the considerations cited by respondent and others have a fully controlling weight; we conclude that they are insufficient to justify an <i>absolute</i> ban on post-search impeachment of veracity. On this side of the balance, also, there are pressing considerations:</p>
<p><span class="star-pagination">*168</span> First, a flat ban on impeachment of veracity could denude the probable-cause requirement of all real meaning. The requirement that a warrant not issue "but upon probable cause, supported by Oath or affirmation," would be reduced to a nullity if a police officer was able to use deliberately falsified allegations to demonstrate probable cause, and, having misled the magistrate, then was able to remain confident that the ploy was worthwhile. It is this specter of intentional falsification that, we think, has evoked such widespread opposition to the flat nonimpeachment rule from the commentators,<sup>[7]</sup> from the American Law Institute in its Model Code of Pre-Arraignment Procedure, § SS290.3 (1) (Prop. Off. Draft 1975), from the federal courts of appeals, and from state courts. On occasion, of course, an instance of deliberate falsity will be exposed and confirmed without a special inquiry either at trial, see <i>United States ex rel. Petillo</i> v. <i>New Jersey,</i> <span class="citation" data-id="1367376"><a href="/opinion/1367376/united-states-ex-rel-petillo-v-state-of-nj/#1171" aria-description="Citation for case: United States Ex Rel. Petillo v. State of NJ">400 F. Supp. 1152, 1171-1172</a></span> (NJ 1975), vacated and remanded by order <i>sub nom. </i><i>Albanese</i> v. <i>Yeager,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/541/275/">541 F. 2d 275</a></span> (CA3 1976), or at a hearing on the sufficiency of the affidavit, cf. <i>United States</i> v. <i>Upshaw,</i> <span class="citation" data-id="9457392"><a href="/opinion/299224/united-states-v-eddie-upshaw/" aria-description="Citation for case: United States v. Eddie Upshaw">448 F. 2d 1218</a></span>, 1221-1222 <span class="star-pagination">*169</span> (CA5 1971), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./405/934/">405 U. S. 934</a></span> (1972). A flat nonimpeachment rule would bar re-examination of the warrant even in these cases.</p>
<p>Second, the hearing before the magistrate not always will suffice to discourage lawless or reckless misconduct. The pre-search proceeding is necessarily <i>ex parte,</i> since the subject of the search cannot be tipped off to the application for a warrant lest he destroy or remove evidence. The usual reliance of our legal system on adversary proceedings itself should be an indication that an <i>ex parte</i> inquiry is likely to be less vigorous. The magistrate has no acquaintance with the information that may contradict the good faith and reasonable basis of the affiant's allegations. The pre-search proceeding will frequently be marked by haste, because of the understandable desire to act before the evidence disappears; this urgency will not always permit the magistrate to make an extended independent examination of the affiant or other witnesses.</p>
<p>Third, the alternative sanctions of a perjury prosecution, administrative discipline, contempt, or a civil suit are not likely to fill the gap. <i>Mapp</i> v. <i>Ohio</i> implicitly rejected the adequacy of these alternatives. Mr. Justice Douglas noted this in his concurrence in <i>Mapp,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#670" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 670</a></span>, where he quoted from <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#42" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 42</a></span> (1949): " `Self-scrutiny is a lofty ideal, but its exaltation reaches new heights if we expect a District Attorney to prosecute himself or his associates for well-meaning violations of the search and seizure clause during a raid the District Attorney or his associates have ordered.'"</p>
<p>Fourth, allowing an evidentiary hearing, after a suitable preliminary proffer of material falsity, would not diminish the importance and solemnity of the warrant-issuing process. It is the <i>ex parte</i> nature of the initial hearing, rather than the magistrate's capacity, that is the reason for the review. A magistrate's determination is presently subject to review before trial as to <i>sufficiency</i> without any undue interference <span class="star-pagination">*170</span> with the dignity of the magistrate's function. Our reluctance today to extend the rule of exclusion beyond instances of deliberate misstatements, and those of reckless disregard, leaves a broad field where the magistrate is the sole protection of a citizen's Fourth Amendment rights, namely, in instances where police have been merely negligent in checking or recording the facts relevant to a probable-cause determination.</p>
<p>Fifth, the claim that a post-search hearing will confuse the issue of the defendant's guilt with the issue of the State's possible misbehavior is footless. The hearing will not be in the presence of the jury. An issue extraneous to guilt already is examined in any probable-cause determination or review of probable cause. Nor, if a sensible threshold showing is required and sensible substantive requirements for suppression are maintained, need there be any new large-scale commitment of judicial resources; many claims will wash out at an early stage, and the more substantial ones in any event would require judicial resources for vindication if the suggested alternative sanctions were truly to be effective. The requirement of a substantial preliminary showing should suffice to prevent the misuse of a veracity hearing for purposes of discovery or obstruction. And because we are faced today with only the question of the integrity of the affiant's representations as to his own activities, we need not decide, and we in no way predetermine, the difficult question whether a reviewing court must ever require the revelation of the identity of an informant once a substantial preliminary showing of falsity has been made. <i>McCray</i> v. <i>Illinois,</i> <span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300</a></span> (1967), the Court's earlier disquisition in this area, concluded only that the Due Process Clause of the Fourteenth Amendment did not require the State to expose an informant's identity routinely, upon a defendant's mere demand, when there was ample evidence in the probable-cause hearing to show that the informant was reliable and his information credible.</p>
<p>Sixth and finally, as to the argument that the exclusionary <span class="star-pagination">*171</span> rule should not be extended to a "new" area, we cannot regard any such extension really to be at issue here. Despite the deep skepticism of Members of this Court as to the wisdom of extending the exclusionary rule to collateral areas, such as civil or grand jury proceedings, the Court has not questioned, in the absence of a more efficacious sanction, the continued application of the rule to suppress evidence from the State's case where a Fourth Amendment violation has been substantial and deliberate. See <i>Brewer</i> v. <i>Williams,</i> <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#422" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387, 422</a></span> (1977) (BURGER, C. J., dissenting); <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#538" aria-description="Citation for case: Stone v. Powell">428 U. S., at 538</a></span> (WHITE, J., dissenting). We see no principled basis for distinguishing between the question of the sufficiency of an affidavit, which also is subject to a post-search re-examination, and the question of its integrity.</p>
<p></p>
<h2>IV</h2>
<p>In sum, and to repeat with some embellishment what we stated at the beginning of this opinion: There is, of course, a presumption of validity with respect to the affidavit supporting the search warrant. To mandate an evidentiary hearing, the challenger's attack must be more than conclusory and must be supported by more than a mere desire to cross-examine. There must be allegations of deliberate falsehood or of reckless disregard for the truth, and those allegations must be accompanied by an offer of proof. They should point out specifically the portion of the warrant affidavit that is claimed to be false; and they should be accompanied by a statement of supporting reasons. Affidavits or sworn or otherwise reliable statements of witnesses should be furnished, or their absence satisfactorily explained. Allegations of negligence or innocent mistake are insufficient. The deliberate falsity or reckless disregard whose impeachment is permitted today is only that of the affiant, not of any nongovernmental informant. Finally, if these requirements are met, and if, when material that is the subject of the alleged falsity or reckless <span class="star-pagination">*172</span> disregard is set to one side, there remains sufficient content in the warrant affidavit to support a finding of probable cause, no hearing is required.<sup>[8]</sup> On the other hand, if the remaining content is insufficient, the defendant is entitled, under the Fourth and Fourteenth Amendments, to his hearing. Whether he will prevail at that hearing is, of course, another issue.</p>
<p>Because of Delaware's absolute rule, its courts did not have occasion to consider the proffer put forward by petitioner Franks. Since the framing of suitable rules to govern proffers is a matter properly left to the States, we decline ourselves to pass on petitioner's proffer. The judgment of the Supreme Court of Delaware is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p></p>
<h2>APPENDIX A TO OPINION OF THE COURT</h2>
                                      J. P. COURT #7
<p>IN THE MATTER OF: Jerome Franks, B/M, DOB: 10/9/54 and 222 S. Governors Ave., Apt. #3, Dover, Delaware. A two room apartment located on the South side, second floor, of a white block building on the west side of S. Governors Avenue, Between Loockerman Street and North Street, in the City of Dover. The ground floor of this building houses Wayman's Barber Shop.</p>
STATE OF DELAWARE
                     ss:
COUNTY OF KENT
<p>Be it remembered that on this 9th day of March A. D. <span class="star-pagination">*173</span> 1976 before me John Green, personally appeared Det. Ronald R. Brooks and Det. Larry Gray of the Dover Police Department who being by me duly sworn depose and say:</p>
<p>That they have reason to believe and do believe that in the 222 S. Governors Avenue, Apartment #3, Dover, Delaware. A two room apartment located on the south side second floor of a white block building on the west side of S. Governors Avenue between Loockerman Street and North Street in the City of Dover. The ground floor of this building houses Wayman's Barber Shop the occupant of which is Jerome Franks there has been and/or there is now located and/or concealed certain property in said house, place, conveyance and/or on the person or persons of the occupants thereof, consisting of property, papers, articles, or things which are the instruments of criminal offense, and/or obtained in the commission of a crime, and/or designated to be used in the commission of a crime, and not reasonably calculated to be used for any other purpose and/or the possession of which is unlawful, papers, articles, or things which are of an evidentiary nature pertaining to the commission of a crime or crimes specified therein and in particular, a white knit thermal undershirt; a brown 3/4 length leather jacket with a tie-belt; a pair of black mens pants; a dark colored knit hat; a long thin bladed knife or other instruments or items relating to the crime.</p>
<p>Articles, or things were, are, or will be possessed and/or used in violation of Title 11, Sub-Chapter D, Section 763, Delaware Code in that [see attached probable-cause page].</p>
<p>Wherefore, affiants pray that a search warrant may be issued authorizing a search of the aforesaid 222 S. Governors Avenue, Apartment #3, Dover, Delaware. A two room apartment located on the south side second floor of a white block building on the west side of S. Governors Avenue <span class="star-pagination">*174</span> between Loockerman St. and North Street, in the City of Dover in the manner provided by law.</p>
      /s/ Det. Ronald R. Brooks
          Affiant
      /s/ Det. Larry D. Gray
          Affiant
<p>SWORN to (or affirmed) and subscribed before me this 9th day of March A. D. 1976.</p>
      /s/ John [illegible] Green
          Judge Ct 7
<p>The facts tending to establish probable cause for the issuance of this search warrant are:</p>
<blockquote>1. On Saturday, 2/28/76, Brenda L. B. ______, W/F/15, reported to the Dover Police Department that she had been kidnapped and raped.</blockquote>
<blockquote>2. An investigation of this complaint was conducted by Det. Boyce Failing of the Dover Police Department.</blockquote>
<blockquote>3. Investigation of the aforementioned complaint revealed that Brenda B. ______, while under the influence of drugs, was taken to 222 S. Governors Avenue, Apartment 3, Dover, Delaware.</blockquote>
<blockquote>4. Investigation of the aforementioned complaint revealed that 222 S. Governors Avenue, Apartment #3, Dover, Delaware, is the residence of Jerome Franks, B/M DOB: 10/9/54.</blockquote>
<blockquote>5. Investigation of the aforementioned complaint revealed that on Saturday, 2/2[8]/76, Jerome Franks did have sexual contact with Brenda B. ______ without her consent.</blockquote>
<blockquote>6. On Thursday, 3/4/76 at the Dover Police Department, Brenda B. ______ revealed to Det. Boyce Failing that Jerome Franks was the person who committed the Sexual Assault against her.</blockquote>
<blockquote>7. On Friday, 3/5/76, Jerome Franks was placed under <span class="star-pagination">*175</span> arrest by Cpl. Robert McClements of the Dover Police Department, and charged with Sexual Misconduct.</blockquote>
<blockquote>8. On 3/5/76 at Family Court in Dover, Delaware, Jerome Franks did, after being arrested on the charge of Sexual Misconduct, ma[k]e a statement to Cpl. Robert McClements, that he thought the charge was concerning Cynthia Bailey not Brenda B. ______.</blockquote>
<blockquote>9. On Friday, 3/5/76, Cynthia C. Bailey, W/F/21 of 132 North Street, Dover, Delaware, did report to Dover Police Department that she had been raped at her residence during the night.</blockquote>
<blockquote>10. Investigation conducted by your affiant on Friday, 3/5/76, revealed the perpetrator of the crime to be an unknown black male, approximately 5′7″, 150 lbs., dark complexion, wearing white thermal undershirt, black pants with a belt having a silver or gold buckle, a brown leather 3/4 length coat with a tie belt in the front, and a dark knit cap pulled around the eyes.</blockquote>
<blockquote>11. Your affiant can state, that during the commission of this crime, Cynthia Bailey was forced at knife point and with the threat of death to engage in sexual intercourse with the perpetrator of the crime.</blockquote>
<blockquote>12. Your affiant can state that entry was gained to the residence of Cynthia Bailey through a window located on the east side of the residence.</blockquote>
<blockquote>13. Your affiant can state that the residence of Jerome Franks is within a very short distance and direct sight of the residence of Cynthia Bailey.</blockquote>
<blockquote>14. Your affiant can state that the description given by Cynthia Bailey of the unknown black male does coincide with the description of Jerome Franks.</blockquote>
<blockquote>15. On Tuesday, 3/9/76, your affiant contacted Mr. James Williams and Mr. Wesley Lucas of the Delaware Youth Center where Jerome Franks is employed and did have personal conversation with both these people.</blockquote>
<blockquote>
<span class="star-pagination">*176</span> 16. On Tuesday, 3/9/76, Mr. James Williams revealed to your affiant that the normal dress of Jerome Franks does consist of a white knit thermal undershirt and a brown leather jacket.</blockquote>
<blockquote>17. On Tuesday, 3/9/76, Mr. Wesley Lucas revealed to your affiant that in addition to the thermal undershirt and jacket, Jerome Franks often wears a dark green knit hat.</blockquote>
<blockquote>18. Your affiant can state that a check of official records reveals that in 1971 Jerome Franks was arrested for the crime of rape and subsequently convicted with Assault with intent to Rape.</blockquote>
<p></p>
<h2>APPENDIX B TO OPINION OF THE COURT</h2>
<p>States permitting veracity challenges include:</p>
Alabama:           <i>McConnell</i> v. <i>State,</i> <span class="citation" data-id="1769197"><a href="/opinion/1769197/mcconnell-v-state/#526" aria-description="Citation for case: McConnell v. State">48 Ala. App. 523, 526-528</a></span>,
                   <span class="citation" data-id="1769197"><a href="/opinion/1769197/mcconnell-v-state/#330" aria-description="Citation for case: McConnell v. State">266 So. 2d 328, 330-333</a></span> (Crim. App.),
                   cert. denied, <span class="citation multiple-matches"><a href="/c/Ala./289/746/">289 Ala. 746</a></span>, <span class="citation" data-id="1768917"><a href="/opinion/1768917/mcconnell-v-state/" aria-description="Citation for case: McConnell v. State">266 So. 2d 334</a></span>
                   (1972).
Alaska:            <i>Davenport</i> v. <i>State,</i> <span class="citation" data-id="1452068"><a href="/opinion/1452068/davenport-v-state/#380" aria-description="Citation for case: Davenport v. State">515 P. 2d 377, 380</a></span>
                   (1973).
Arizona:           <i>State</i> v. <i>Payne,</i> <span class="citation" data-id="1367322"><a href="/opinion/1367322/state-v-payne/#456" aria-description="Citation for case: State v. Payne">25 Ariz. App. 454, 456</a></span>, <span class="citation" data-id="1367322"><a href="/opinion/1367322/state-v-payne/#673" aria-description="Citation for case: State v. Payne">544
                   P. 2d 671, 673</a></span> (1976); cf. <i>State</i> v. <i>Pike,</i> <span class="citation" data-id="1148533"><a href="/opinion/1148533/state-v-pike/#513" aria-description="Citation for case: State v. Pike">113
                   Ariz. 511, 513-514</a></span>, <span class="citation" data-id="1148533"><a href="/opinion/1148533/state-v-pike/#1070" aria-description="Citation for case: State v. Pike">557 P. 2d 1068, 1070-1071</a></span>
                   (1976) (en banc).
Colorado:          <i>People</i> v. <i>Arnold,</i> <span class="citation" data-id="9548905"><a href="/opinion/1176912/people-v-arnold/#377" aria-description="Citation for case: People v. Arnold">186 Colo. 372, 377-378</a></span>,
                   <span class="citation" data-id="9548905"><a href="/opinion/1176912/people-v-arnold/#809" aria-description="Citation for case: People v. Arnold">527 P. 2d 806, 809</a></span> (1974) (en banc).
Iowa:              <i>State</i> v. <i>Boyd,</i> <span class="citation" data-id="1851918"><a href="/opinion/1851918/state-v-boyd/#616" aria-description="Citation for case: State v. Boyd">224 N. W. 2d 609, 616</a></span>
                   (1974) (en banc).
Louisiana:         <i>State</i> v. <i>Melson,</i> <span class="citation" data-id="1828817"><a href="/opinion/1828817/state-v-melson/#874" aria-description="Citation for case: State v. Melson">284 So. 2d 873, 874-875</a></span>
                   (1973), limiting <i>State</i> v. <i>Anselmo,</i> <span class="citation" data-id="9534579"><a href="/opinion/1130838/state-v-anselmo/#313" aria-description="Citation for case: State v. Anselmo">260
                   La. 306, 313-322</a></span>, <span class="citation" data-id="9534579"><a href="/opinion/1130838/state-v-anselmo/#101" aria-description="Citation for case: State v. Anselmo">256 So. 2d 98, 101-104</a></span>
                   (1971), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./407/911/">407 U. S. 911</a></span> (1972).
Massachusetts:     <i>Commonwealth</i> v. <i>Reynolds,</i> <span class="citation" data-id="2233092"><a href="/opinion/2233092/commonwealth-v-reynolds/#149" aria-description="Citation for case: Commonwealth v. Reynolds">374 Mass. 142,
                   149-151</a></span>, <span class="citation" data-id="2233092"><a href="/opinion/2233092/commonwealth-v-reynolds/#1379" aria-description="Citation for case: Commonwealth v. Reynolds">370 N. E. 2d 1375, 1379-1380</a></span>
                   (1977).
<span class="star-pagination">*177</span>
Minnesota:         <i>State</i> v. <i>Luciow,</i> <span class="citation" data-id="2215694"><a href="/opinion/2215694/state-v-luciow/#10" aria-description="Citation for case: State v. Luciow">308 Minn. 6, 10-13</a></span>, <span class="citation" data-id="2215694"><a href="/opinion/2215694/state-v-luciow/#837" aria-description="Citation for case: State v. Luciow">240
                   N. W. 2d 833, 837-838</a></span> (1976) (en banc).
Montana:           <i>State</i> v. <i>Nanoff,</i> <span class="citation" data-id="8026226"><a href="/opinion/8068009/state-v-nanoff/#348" aria-description="Citation for case: State v. Nanoff">160 Mont. 344, 348</a></span>, <span class="citation" data-id="8026226"><a href="/opinion/8068009/state-v-nanoff/#1140" aria-description="Citation for case: State v. Nanoff">502
                   P. 2d 1138, 1140</a></span> (1972), <i>sub silentio</i> overruling
                   <i>State</i> v. <i>English,</i> <span class="citation" data-id="8024116"><a href="/opinion/8066168/state-v-english/#350" aria-description="Citation for case: State v. English">71 Mont. 343, 350</a></span>,
                   <span class="citation" data-id="8024116"><a href="/opinion/8066168/state-v-english/#729" aria-description="Citation for case: State v. English">229 P. 727, 729</a></span> (1924).
New Hampshire:     <i>State</i> v. <i>Spero,</i> 177 N. H. 199, 204-205, <span class="citation" data-id="2365893"><a href="/opinion/2365893/state-v-spero/#1158" aria-description="Citation for case: State v. Spero">371
                   A. 2d 1155, 1158</a></span> (1977) (based on State
                   Constitution).
Pennsylvania:      <i>Commonwealth</i> v. <i>Hall,</i> <span class="citation" data-id="9757210"><a href="/opinion/2349003/commonwealth-v-hall/#204" aria-description="Citation for case: Commonwealth v. Hall">451 Pa. 201, 204</a></span>,
                   <span class="citation" data-id="9757210"><a href="/opinion/2349003/commonwealth-v-hall/#344" aria-description="Citation for case: Commonwealth v. Hall">302 A. 2d 342, 344</a></span> (1973).
South Carolina:    <i>State</i> v. <i>Sachs,</i> 264 S. C. 541, 556, <span class="citation" data-id="9616512"><a href="/opinion/1391098/state-v-sachs/#509" aria-description="Citation for case: State v. Sachs">216 S. E.
                   2d 501, 509</a></span> (1975).
Vermont:           <i>State</i> v. <i>Dupaw,</i> <span class="citation" data-id="1498442"><a href="/opinion/1498442/state-v-dupaw/#452" aria-description="Citation for case: State v. Dupaw">134 Vt. 451, 452-453</a></span>, <span class="citation" data-id="1498442"><a href="/opinion/1498442/state-v-dupaw/#968" aria-description="Citation for case: State v. Dupaw">365
                   A. 2d 967, 968</a></span> (1976).
Washington:        <i>State</i> v. <i>Lehman,</i> <span class="citation" data-id="1353828"><a href="/opinion/1353828/state-v-lehman/#414" aria-description="Citation for case: State v. Lehman">8 Wash. App. 408, 414</a></span>,
                   <span class="citation" data-id="1353828"><a href="/opinion/1353828/state-v-lehman/#1321" aria-description="Citation for case: State v. Lehman">506 P. 2d 1316, 1321</a></span> (1973) (Div. 3); <i>State</i>
                   v. <i>Goodlow,</i> <span class="citation" data-id="1163909"><a href="/opinion/1163909/state-v-goodlow/#535" aria-description="Citation for case: State v. Goodlow">11 Wash. App. 533, 535</a></span>, <span class="citation" data-id="1163909"><a href="/opinion/1163909/state-v-goodlow/#1206" aria-description="Citation for case: State v. Goodlow">523 P.
                   2d 1204, 1206</a></span> (1974) (Div. 1); cf. <i>State</i> v.
                   <i>Manly,</i> <span class="citation" data-id="9791370"><a href="/opinion/2609109/state-v-manly/#125" aria-description="Citation for case: State v. Manly">85 Wash. 2d 120, 125</a></span>, <span class="citation" data-id="9791370"><a href="/opinion/2609109/state-v-manly/#309" aria-description="Citation for case: State v. Manly">530 P. 2d
                   306, 309</a></span> (en banc), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./423/855/">423 U. S.
                   855</a></span> (1975).
<p>Five States, whose practice is dictated or may be dictated by statute, also permit veracity challenges:</p>
California:        <i>Theodor</i> v. <i>Superior Court,</i> <span class="citation" data-id="1180163"><a href="/opinion/1180163/theodor-v-superior-court/#90" aria-description="Citation for case: Theodor v. Superior Court">8 Cal. 3d 77, 90,
                   100-101</a></span>, <span class="citation" data-id="1180163"><a href="/opinion/1180163/theodor-v-superior-court/#243" aria-description="Citation for case: Theodor v. Superior Court">501 P. 2d 234, 243, 251</a></span> (1972)
                   (en banc); see Cal. Penal Code Ann.
                   §§ 1538.5, 1539, 1540 (West 1970 and Supp.
                   1978).
New York:          <i>People</i> v. <i>Alfinito,</i> 16 N. Y. 2d 181, 185-186,
                   <span class="citation" data-id="5522037"><a href="/opinion/5674467/people-v-alfinito/#646" aria-description="Citation for case: People v. Alfinito">211 N. E. 2d 644, 646</a></span> (1965); <i>People</i> v.
                   <i>Slaughter,</i> 37 N. Y. 2d 596, 600, <span class="citation" data-id="5529933"><a href="/opinion/5681518/people-v-slaughter/#624" aria-description="Citation for case: People v. Slaughter">338 N. E.
                   2d 622, 624</a></span> (1975); see N. Y. Code Crim.
                   Proc. §§ 813-c, 813-d, 813-e (McKinney
<span class="star-pagination">*178</span>
                   Supp. 1970-1971), superseded by N. Y.
                   Crim. Proc. Law, Art. 710 (McKinney
                   Supp. 1977-1978).
North Carolina:    See N. C. Gen. Stat. § 15A-978 (1978).
Oregon:            <i>State</i> v. <i>Wright,</i> <span class="citation" data-id="1183476"><a href="/opinion/1183476/state-v-wright/#168" aria-description="Citation for case: State v. Wright">266 Ore. 163, 168-169, n. 3</a></span>,
                   <span class="citation" data-id="1183476"><a href="/opinion/1183476/state-v-wright/#1225" aria-description="Citation for case: State v. Wright">511 P. 2d 1223, 1225-1226, n. 3</a></span> (1973) (en
                   banc); see Ore. Rev. Stat. § 133.693 (1977).
Utah:              <i>State</i> v. <i>Bankhead,</i> <span class="citation" data-id="1451648"><a href="/opinion/1451648/state-v-bankhead/#138" aria-description="Citation for case: State v. Bankhead">30 Utah 2d 135, 138</a></span>, <span class="citation" data-id="1451648"><a href="/opinion/1451648/state-v-bankhead/#802" aria-description="Citation for case: State v. Bankhead">514
                   P. 2d 800, 802</a></span> (1973); see <span class="citation no-link">Utah Code Ann.
                   §§ 77-54-17</span>, 77-54-18 (1953).
<p>Two other States are more doubtful, but seem to allow veracity challenges:</p>
Michigan:          <i>People</i> v. <i>Burt,</i> <span class="citation" data-id="3493017"><a href="/opinion/3523662/people-v-burt/#74" aria-description="Citation for case: People v. Burt">236 Mich. 62, 74</a></span>, <span class="citation" data-id="3493017"><a href="/opinion/3523662/people-v-burt/#101" aria-description="Citation for case: People v. Burt">210 N. W.
                   97, 101</a></span> (1926).
New Mexico:        <i>State</i> v. <i>Baca,</i> 84 N. M. 513, 515, <span class="citation" data-id="1445282"><a href="/opinion/1445282/state-v-baca/#858" aria-description="Citation for case: State v. Baca">505 P.
                   2d 856, 858</a></span> (1973) (dictum).
<p>The following States have disposed of particular veracity challenges on the ground the affidavits were in fact not false, or that any misstatements were immaterial or unintentional or were not by the affiant himself:</p>
Florida:           <i>McDougall</i> v. <i>State,</i> <span class="citation" data-id="1886978"><a href="/opinion/1886978/mcdougall-v-state/#625" aria-description="Citation for case: McDougall v. State">316 So. 2d 624, 625</a></span>
                   (Dist. Ct. App. 1975).
Georgia:           <i>Williams</i> v. <i>State,</i> <span class="citation" data-id="1363434"><a href="/opinion/1363434/williams-v-state/#213" aria-description="Citation for case: Williams v. State">232 Ga. 213, 213-214</a></span>,
                   <span class="citation" data-id="1363434"><a href="/opinion/1363434/williams-v-state/#860" aria-description="Citation for case: Williams v. State">205 S. E. 2d 859, 860</a></span> (1974); <i>Lee</i> v. <i>State,</i>
                   <span class="citation" data-id="1424506"><a href="/opinion/1424506/lee-v-state/#773" aria-description="Citation for case: Lee v. State">239 Ga. 769, 773-774</a></span>, <span class="citation" data-id="1424506"><a href="/opinion/1424506/lee-v-state/#856" aria-description="Citation for case: Lee v. State">238 S. E. 2d 852, 856</a></span>
                   (1977); <i>Birge</i> v. <i>State,</i> <span class="citation" data-id="1415130"><a href="/opinion/1415130/birge-v-state/#633" aria-description="Citation for case: Birge v. State">143 Ga. App. 632,
                   633</a></span>, <span class="citation" data-id="1415130"><a href="/opinion/1415130/birge-v-state/#397" aria-description="Citation for case: Birge v. State">239 S. E. 2d 395, 397</a></span> (1977).
Indiana:           <i>Moore</i> v. <i>State,</i> <span class="citation" data-id="2060217"><a href="/opinion/2060217/moore-v-state/#385" aria-description="Citation for case: Moore v. State">159 Ind. App. 381, 385-386</a></span>,
                   <span class="citation" data-id="2060217"><a href="/opinion/2060217/moore-v-state/#94" aria-description="Citation for case: Moore v. State">307 N. E. 2d 92, 94-95</a></span> (1974); <i>Grzesiowski</i>
                   v. <i>State,</i> <span class="citation" data-id="2221046"><a href="/opinion/2221046/grzesiowski-v-state/#328" aria-description="Citation for case: Grzesiowski v. State">168 Ind. App. 318, 328</a></span>, <span class="citation" data-id="2221046"><a href="/opinion/2221046/grzesiowski-v-state/#312" aria-description="Citation for case: Grzesiowski v. State">343
                   N. E. 2d 305, 312</a></span> (1976); but see <i>Seager</i> v.
                   <i>State,</i> <span class="citation" data-id="3423317"><a href="/opinion/3426273/seager-v-state/#582" aria-description="Citation for case: Seager v. State">200 Ind. 579, 582</a></span>, <span class="citation" data-id="3423317"><a href="/opinion/3426273/seager-v-state/#275" aria-description="Citation for case: Seager v. State">164 N. E. 274, 275</a></span>
                   (1928).
<span class="star-pagination">*179</span>
Ohio:              <i>State</i> v. <i>Dodson,</i> <span class="citation" data-id="3744266"><a href="/opinion/3991275/state-v-dodson/#35" aria-description="Citation for case: State v. Dodson">43 Ohio App. 2d 31, 35-36</a></span>,
                   <span class="citation" data-id="3744266"><a href="/opinion/3991275/state-v-dodson/#374" aria-description="Citation for case: State v. Dodson">332 N. E. 2d 371, 374-375</a></span> (1974).
Wisconsin:         <i>Scott</i> v. <i>State,</i> <span class="citation" data-id="1311035"><a href="/opinion/1311035/scott-v-state/#511" aria-description="Citation for case: Scott v. State">73 Wis. 2d 504, 511-512</a></span>, <span class="citation" data-id="1311035"><a href="/opinion/1311035/scott-v-state/#219" aria-description="Citation for case: Scott v. State">243
                   N. W. 2d 215, 219</a></span> (1976).
Cf. Maine:         <i>State</i> v. <i>Koucoules,</i> <span class="citation" data-id="2184913"><a href="/opinion/2184913/state-v-koucoules/" aria-description="Citation for case: State v. Koucoules">343 A. 2d 860</a></span>, 865 n. 3
                   (1974).
<p>Eleven States flatly prohibit veracity challenges:</p>
Arkansas:          <i>Liberto</i> v. <i>State,</i> <span class="citation" data-id="1631048"><a href="/opinion/1631048/liberto-v-state/#356" aria-description="Citation for case: Liberto v. State">248 Ark. 350, 356-357</a></span>, <span class="citation" data-id="1631048"><a href="/opinion/1631048/liberto-v-state/#468" aria-description="Citation for case: Liberto v. State">451
                   S. W. 2d 464, 468</a></span> (1970) (alternative holding);
                   cf. <i>Powell</i> v. <i>State,</i> <span class="citation" data-id="2467369"><a href="/opinion/2467369/powell-v-state/#383" aria-description="Citation for case: Powell v. State">260 Ark. 381, 383</a></span>,
                   <span class="citation" data-id="2467369"><a href="/opinion/2467369/powell-v-state/#2" aria-description="Citation for case: Powell v. State">540 S. W. 2d 1, 2</a></span> (1976).
Connecticut:       <i>State</i> v. <i>Williams,</i> <span class="citation" data-id="2398659"><a href="/opinion/2398659/state-v-williams/#327" aria-description="Citation for case: State v. Williams">169 Conn. 322, 327-329</a></span>,
                   <span class="citation" data-id="2398659"><a href="/opinion/2398659/state-v-williams/#76" aria-description="Citation for case: State v. Williams">363 A. 2d 72, 76-77</a></span> (1975).
Illinois:          <i>People</i> v. <i>Bak,</i> <span class="citation" data-id="9884743"><a href="/opinion/2133918/the-people-v-bak/#144" aria-description="Citation for case: The People v. Bak">45 Ill. 2d 140, 144-146</a></span>, <span class="citation" data-id="9884743"><a href="/opinion/2133918/the-people-v-bak/#343" aria-description="Citation for case: The People v. Bak">258
                   N. E. 2d 341, 343-344</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./400/882/">400
                   U. S. 882</a></span> (1970); <i>People</i> v. <i>Stansberry,</i> <span class="citation" data-id="9884688"><a href="/opinion/2120568/the-people-v-stansberry/#544" aria-description="Citation for case: The PEOPLE v. Stansberry">47
                   Ill. 2d 541, 544</a></span>, <span class="citation" data-id="9884688"><a href="/opinion/2120568/the-people-v-stansberry/#433" aria-description="Citation for case: The PEOPLE v. Stansberry">268 N. E. 2d 431, 433</a></span>, cert.
                   denied, <span class="citation multiple-matches"><a href="/c/U.%20S./404/873/">404 U. S. 873</a></span> (1971).
Kansas:            <i>State</i> v. <i>Lamb,</i> <span class="citation" data-id="1306980"><a href="/opinion/1306980/state-v-lamb/#467" aria-description="Citation for case: State v. Lamb">209 Kan. 453, 467-468</a></span>, <span class="citation" data-id="1306980"><a href="/opinion/1306980/state-v-lamb/#287" aria-description="Citation for case: State v. Lamb">497
                   P. 2d 275, 287</a></span> (1972); <i>State</i> v. <i>Sanders,</i> <span class="citation" data-id="1285341"><a href="/opinion/1285341/state-v-sanders/#194" aria-description="Citation for case: State v. Sanders">222
                   Kan. 189, 194-196</a></span>, <span class="citation" data-id="1285341"><a href="/opinion/1285341/state-v-sanders/#466" aria-description="Citation for case: State v. Sanders">563 P. 2d 461, 466-467</a></span>
                   (alternative holding), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./434/833/">434
                   U. S. 833</a></span> (1977).
Kentucky:          <i>Caslin</i> v. <i>Commonwealth,</i> <span class="citation" data-id="1530851"><a href="/opinion/1530851/caslin-v-commonwealth/#834" aria-description="Citation for case: Caslin v. Commonwealth">491 S. W. 2d 832,
                   834</a></span> (1973).
Maryland:          <i>Smith</i> v. <i>State,</i> <span class="citation" data-id="3486405"><a href="/opinion/3488471/smith-v-state/#334" aria-description="Citation for case: Smith v. State">191 Md. 329, 334-336</a></span>, <span class="citation" data-id="3486405"><a href="/opinion/3488471/smith-v-state/#289" aria-description="Citation for case: Smith v. State">62 A.
                   2d 287, 289-290</a></span> (1948), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./336/925/">336
                   U. S. 925</a></span> (1949); <i>Tucker</i> v. <i>State,</i> <span class="citation" data-id="2053522"><a href="/opinion/2053522/tucker-v-state/#499" aria-description="Citation for case: Tucker v. State">244 Md.
                   488, 499-500</a></span>, <span class="citation" data-id="2053522"><a href="/opinion/2053522/tucker-v-state/#117" aria-description="Citation for case: Tucker v. State">224 A. 2d 111, 117-118</a></span>
                   (1966), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./386/1024/">386 U. S. 1024</a></span> (1967);
                   <i>Dawson</i> v. <i>State,</i> <span class="citation" data-id="1895767"><a href="/opinion/1895767/dawson-v-state/#713" aria-description="Citation for case: Dawson v. State">11 Md. App. 694, 713-715</a></span>,
                   <span class="citation" data-id="1895767"><a href="/opinion/1895767/dawson-v-state/#690" aria-description="Citation for case: Dawson v. State">276 A. 2d 680, 690-691</a></span> (1971).
Mississippi:       <i>Wood</i> v. <i>State,</i> <span class="citation" data-id="1850125"><a href="/opinion/1850125/wood-v-state/#465" aria-description="Citation for case: Wood v. State">322 So. 2d 462, 465</a></span> (1975).
<span class="star-pagination">*180</span>
New Jersey:        <i>State</i> v. <i>Petillo,</i> 61 N. J. 165, 173-179, <span class="citation" data-id="2341043"><a href="/opinion/2341043/state-v-petillo/#653" aria-description="Citation for case: State v. Petillo">293
                   A. 2d 649, 653-656</a></span> (1972), cert. denied,
                   <span class="citation multiple-matches"><a href="/c/U.%20S./410/945/">410 U. S. 945</a></span> (1973); but see 61 N. J., at
                   178 n. 1, <span class="citation" data-id="2341043"><a href="/opinion/2341043/state-v-petillo/" aria-description="Citation for case: State v. Petillo">293 A. 2d, at 656</a></span> n. 1.
Oklahoma:          <i>Brown</i> v. <i>State,</i> <span class="citation" data-id="9559541"><a href="/opinion/1198737/brown-v-state/" aria-description="Citation for case: Brown v. State">565 P. 2d 697</a></span> (Crim. App.
                   1977), overruling <i>McCaskey</i> v. <i>State,</i> <span class="citation" data-id="1190217"><a href="/opinion/1190217/mccaskey-v-state/#1311" aria-description="Citation for case: McCaskey v. State">534
                   P. 2d 1309, 1311-1312</a></span> (Crim. App. 1975),
                   and <i>Henderson</i> v. <i>State,</i> <span class="citation" data-id="1437089"><a href="/opinion/1437089/henderson-v-state/#789" aria-description="Citation for case: Henderson v. State">490 P. 2d 786, 789</a></span>
                   (Crim. App. 1971), and reaffirming <i>Gaddis</i>
                   v. <i>State,</i> <span class="citation" data-id="9574534"><a href="/opinion/1312713/gaddis-v-state/" aria-description="Citation for case: Gaddis v. State">447 P. 2d 42</a></span> (Crim. App. 1968).
Tennessee:         <i>Owens</i> v. <i>State,</i> <span class="citation" data-id="2442476"><a href="/opinion/2442476/owens-v-state/#553" aria-description="Citation for case: Owens v. State">217 Tenn. 544, 553</a></span>, <span class="citation" data-id="2442476"><a href="/opinion/2442476/owens-v-state/#511" aria-description="Citation for case: Owens v. State">399
                   S. W. 2d 507, 511</a></span> (1965); <i>Poole</i> v. <i>State,</i> 4
                   Tenn. Crim. 41, 53-54, <span class="citation" data-id="2379504"><a href="/opinion/2379504/poole-v-state/#832" aria-description="Citation for case: Poole v. State">467 S. W. 2d 826,
                   832</a></span>, cert. denied, <i><span class="citation" data-id="2379504"><a href="/opinion/2379504/poole-v-state/" aria-description="Citation for case: Poole v. State">ibid.</a></span></i> (1971).
Texas:             <i>Phenix</i> v. <i>State,</i> <span class="citation" data-id="2386408"><a href="/opinion/2386408/phenix-v-state/#765" aria-description="Citation for case: Phenix v. State">488 S. W. 2d 759, 765</a></span>
                   (Crim. App. 1972); <i>Oubre</i> v. <i>State,</i> <span class="citation" data-id="1760963"><a href="/opinion/1760963/oubre-v-state/#877" aria-description="Citation for case: Oubre v. State">542
                   S. W. 2d 875, 877</a></span> (Crim. App. 1976).
<p>Two States have prohibited challenges that were directed seemingly against the conclusory nature of the affidavits, rather than their veracity.</p>
Missouri:          <i>State</i> v. <i>Brugioni,</i> <span class="citation" data-id="3535850"><a href="/opinion/3558063/state-v-brugioni/#206" aria-description="Citation for case: State v. Brugioni">320 Mo. 202, 206</a></span>, <span class="citation" data-id="3535850"><a href="/opinion/3558063/state-v-brugioni/#263" aria-description="Citation for case: State v. Brugioni">7 S. W.
                   2d 262, 263</a></span> (1928).
Rhode Island:      <i>State</i> v. <i>Seymour,</i> 46 R. I. 257, 260, <span class="citation" data-id="3865272"><a href="/opinion/4105545/state-v-seymour/#756" aria-description="Citation for case: State v. Seymour">126 A.
                   755, 756</a></span> (1924), partially overruled, <i>State</i>
                   v. <i>LeBlanc,</i> 100 R. I. 523, 528-529, <span class="citation" data-id="1987009"><a href="/opinion/1987009/state-v-leblanc/#474" aria-description="Citation for case: State v. LeBlanc">217 A.
                   2d 471, 474</a></span> (1966); but see <i>State</i> v. <i>Cofone,</i>
                   112 R. I. 760, 766-767, <span class="citation" data-id="1973195"><a href="/opinion/1973195/state-v-cofone/#755" aria-description="Citation for case: State v. Cofone">315 A. 2d 752, 755-756</a></span>
                   (1974).
<p>MR. JUSTICE REHNQUIST, with whom THE CHIEF JUSTICE joins, dissenting.</p>
<p>The Court's opinion in this case carefully identifies the factors which militate against the result which it reaches, and emphasizes their weight in attempting to limit the circumstances <span class="star-pagination">*181</span> under which an affidavit supporting a search warrant may be impeached. I am not ultimately persuaded, however, that the Court is correct as a matter of constitutional law that the impeachment of such an affidavit must be permitted under the circumstances described by the Court, and I am thoroughly persuaded that the barriers which the Court believes that it is erecting against misuse of the impeachment process are frail indeed.</p>
<p></p>
<h2>I</h2>
<p>The Court's reliance on <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948), for the proposition that a determination by a neutral magistrate is a prerequisite to the sufficiency of an application for a warrant is obviously correct. In that case the Court said:</p>
<blockquote>"The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime." <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States"><i>Id.,</i> at 13-14</a></span>.</blockquote>
<p>The notion that there may be incorrect or even deliberately falsified information presented to a magistrate in the course of an effort to obtain a search warrant does not render the proceeding before a magistrate any different from any other factfinding procedure known to the law. The Court here says that "it would be an unthinkable imposition upon [the magistrate's] authority if a warrant affidavit, revealed after the fact to contain a deliberately or recklessly false statement, were to stand beyond impeachment." <i>Ante,</i> at 165. I do not believe that this flat statement survives careful analysis.</p>
<p>If the function of the warrant requirement is to obtain the determination of a neutral magistrate as to whether sufficient <span class="star-pagination">*182</span> grounds have been urged to support the issuance of a warrant, that function is fulfilled at the time the magistrate concludes that the requirement has been met. Like any other determination of a magistrate, of a court, or of countless other factfinding tribunals, the decision may be incorrect as a matter of law. Even if correct, some inaccurate or falsified information may have gone into the making of the determination. But unless we are to exalt as the <i>ne plus ultra</i> of our system of criminal justice the absolute correctness of every factual determination made along the tortuous route from the filing of the complaint or the issuance of an indictment to the final determination that a judgment of conviction was properly obtained, we shall lose perspective as to the purposes of the system as well as of the warrant requirement of the Fourth and Fourteenth Amendments. Much of what Mr. Justice Harlan said in his separate opinion in <i>Mackey</i> v. <i>United States,</i> <span class="citation" data-id="9424506"><a href="/opinion/108302/mackey-v-united-states/" aria-description="Citation for case: MacKey v. United States">401 U. S. 667</a></span> (1971), with respect to collateral relief from a criminal conviction is likewise applicable to collateral impeachment of a search warrant:</p>
<blockquote>"At some point, the criminal process, if it is to function at all, must turn its attention from whether a man ought properly to be incarcerated to how he is to be treated once convicted. If law, criminal or otherwise, is worth having and enforcing, it must at some time provide a definitive answer to the questions litigants present or else it never provides an answer at all. Surely it is an unpleasant task to strip a man of his freedom and subject him to institutional restraints. But this does not mean that in so doing, we should always be halting or tentative. No one, not criminal defendants, not the judicial system, not society as a whole is benefited by a judgment providing a man shall tentatively go to jail today, but tomorrow and every day thereafter his continued incarceration shall be subject to fresh litigation on issues already resolved.</blockquote>
<blockquote>
<span class="star-pagination">*183</span> "A rule of law that fails to take account of these finality interests would do more than subvert the criminal process itself. It would also seriously distort the very limited resources society has allocated to the criminal process. While men languish in jail, not uncommonly for over a year, awaiting a first trial on their guilt or innocence, it is not easy to justify expending substantial quantities of the time and energies of judges, prosecutors, and defense lawyers litigating the validity under present law of criminal convictions that were perfectly free from error when made final. [Citation omitted.] This drain on society's resources is compounded by the fact that issuance of the habeas writ compels a State that wishes to continue enforcing its laws against the successful petitioner to relitigate facts buried in the remote past through presentation of witnesses whose memories of the relevant events often have dimmed. This very act of trying stale facts may well, ironically, produce a second trial no more reliable as a matter of getting at the truth than the first." <span class="citation" data-id="9424506"><a href="/opinion/108302/mackey-v-united-states/#690" aria-description="Citation for case: MacKey v. United States"><i>Id.,</i> at 690-691</a></span>.</blockquote>
<p>I am quite confident that if our system of justice were not administered by judges who were once lawyers, it might well be less satisfactory than it now is. But I am equally confident that one improvement which would manifest itself as a result of such a change would be a willingness, reflected in almost all callings in our society except lawyers, to refrain from constant relitigation, whether in the form of collateral attack, appeal, retrial, or whatever, of issues that have originally been decided by a competent authority.</p>
<p>It would be extraordinarily troubling in any system of criminal justice if a verdict or finding of guilt, later conclusively shown to be based on false testimony, were to result in the incarceration of the accused notwithstanding this fact. But the Court's reference to the "unthinkable imposition" of not allowing the impeachment of an affiant's testimony in support <span class="star-pagination">*184</span> of a search warrant is a horse of quite another color. Particularly in view of the many hurdles which the prosecution must surmount to ultimately obtain and retain a finding of guilt in the light of the many constitutional safeguards which surround a criminal accused, it is essential to understand the role of a search warrant in the process which may lead to the conviction of such an accused. The warrant issued on impeachable testimony has, by hypothesis, turned up incriminating and admissible evidence to be considered by the jury at the trial. The fact that it was obtained by reason of an impeachable warrant bears not at all on the innocence or guilt of the accused. The only conceivable harm done by such evidence is to the accused's rights under the Fourth and Fourteenth Amendments, which have nothing to do with his guilt or innocence of the crime with which he is charged.</p>
<p>Given the definitive exposition of the warrant requirement quoted above from <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S., at 13-14</a></span>, it seems to me it would be quite reasonable for this Court, consistently with the Fourth and Fourteenth Amendments, to adopt any one of three positions with respect to the impeachability of a search warrant which had been in fact issued by a neutral magistrate who satisfied the requirements of <i>Shadwick</i> v. <i>Tampa,</i> <span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/" aria-description="Citation for case: Shadwick v. City of Tampa">407 U. S. 345</a></span> (1972).</p>
<p>First, it could decide that the warrant requirement was satisfied when such a magistrate had been persuaded, and allow no further collateral attack on the warrant. In <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), the Court in reliance on <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span> (1958), a case concededly decided pursuant to Fed. Rule Crim. Proc. 4, nonetheless held that the determination by a magistrate that the affidavit submitted to him made out "probable cause" for purposes of the Fourth and Fourteenth Amendments was subject to later judicial review as to the sufficiency of the affidavit. This rule was later reaffirmed in <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969). The Court has thus for more than a decade <span class="star-pagination">*185</span> rejected the first possible stopping place in judicial re-examination of affidavits in support of warrants, and held that the legal determination as to probable cause was subject to collateral attack. While this conclusion does not seem to me to flow inexorably from the Fourth Amendment, I think that it makes a good deal of sense in light of the fact that a magistrate need not be a trained lawyer, see <i><span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/" aria-description="Citation for case: Shadwick v. City of Tampa">Shadwick, supra,</a></span></i> and therefore may not be versed in the latest nuances of what is or what is not "probable cause" for purposes of the Fourth Amendment.</p>
<p>But to allow collateral examination of an affidavit in support of a warrant on a legal ground such as that is quite different from the rejection of the second possible stopping place as the Court does today. Magistrates need not be lawyers, but lawyers have no monopoly on determining whether or not an affiant who appears before them is or is not telling the truth. Indeed, a magistrate whose time may be principally spent in conducting preliminary hearings and trying petty offenses may have every bit as good a feel for the veracity of a particular witness as a judge of a court of general jurisdiction.</p>
<p>True, a warrant is issued <i>ex parte,</i> without an opportunity for the person whose effects are to be seized to impeach the testimony of the affiant. The proceeding leading to the issuance of a warrant is, therefore, obviously less reliable and less likely to be a searching inquiry into the truth of the affiant's statements than is a full-dress adversary proceeding. But it is at this point that I part company with the Court in its underlying assumption that somehow a full-dress adversary proceeding will virtually guarantee a truthful answer to the question of whether or not the affiant seeking the warrant falsified his testimony. A full-dress adversary proceeding is undoubtedly a better vehicle than an <i>ex parte</i> proceeding for arriving at the truth of any particular inquiry, but it is scarcely a guarantee of truth. Mr. Justice Jackson in his <span class="star-pagination">*186</span> opinion concurring in the result in <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">344 U. S. 443</a></span> (1953), observed with respect to purely legal issues decided by this Court:</p>
<blockquote>"However, reversal by a higher court is not proof that justice is thereby better done. There is no doubt that if there were a super-Supreme Court, a substantial proportion of our reversals of state courts would also be reversed. We are not final because we are infallible, but we are infallible only because we are final." <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#540" aria-description="Citation for case: Brown v. Allen"><i>Id.,</i> at 540</a></span>.</blockquote>
<p>The same is surely true of a judge's review of the factual determinations of a magistrate; a larger percentage of the judge's findings as to the truth of an affiant's statement may be objectively correct than the percentage of the magistrate's determinations which are, but neither one is going to be 100 percent. Since once the warrant is issued and the search is made, the privacy interest protected by the Fourth and Fourteenth Amendments is breached, a subsequent determination that it was wrongfully breached cannot possibly restore the privacy interest. See <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U. S. 338</a></span> (1974). Since the evidence obtained pursuant to the warrant is by hypothesis relevant and admissible on the issue of guilt, the only purpose served by suppression of such evidence is deterrence of falsified testimony on the part of affiant in the future. Without attempting to summarize the many cases in which this Court has discussed the balance to be struck in such situations, see <i>United States</i> v. <i>Peltier,</i> <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">422 U. S. 531</a></span> (1975), I simply do not think the game is worth the candle in this situation.</p>
<p>As the Court's opinion points out, the other jurisdictions which have considered this question are divided, although a majority of them favor the result reached by the Court today. The signed articles and student law review notes which the Court refers to in its opinion are not there, I trust, to be considered <i>en bloc</i> or by some process of counting without weighing. Presumably, to the extent that their reasoning <span class="star-pagination">*187</span> commends itself to the courts which are committed to decide these questions, that reasoning will find its way into the opinions of those courts; to the extent that the reasoning does not so commend itself, the piece containing the reasoning does not weigh in the scales of decision simply because it appeared in a periodical devoted to the discussion of legal questions.</p>
<p></p>
<h2>II</h2>
<p>The Court has commendably, in my opinion, surrounded the right to impeach the affidavit relied upon to support the issuance of a warrant with numerous limitations. My fear, and I do not think it an unjustified one, is that these limitations will quickly be subverted in actual practice. The Court states:</p>
<blockquote>"Nor, if a sensible threshold showing is required and sensible substantive requirements for suppression are maintained, need there be any new large-scale commitment of judicial resources; many claims will wash out at an early stage, and the more substantial ones in any event would require judicial resources for vindication if the suggested alternative sanctions were truly to be effective. The requirement of a substantial preliminary showing should suffice to prevent the misuse of a veracity hearing for purposes of discovery or obstruction." <i>Ante,</i> at 170.</blockquote>
<p>I greatly fear that this generalized language will afford insufficient protection against the natural tendency of ingenious lawyers charged with representing their client's cause to ceaselessly undermine the limitations which the Court has placed on impeachment of the affidavit offered in support of a search warrant. I am sure that the Court is sincere in its expressed hope that the doctrine which it adopts will not lead to "any new large-scale commitment of judicial resources," but in the end I am led once more to echo the <span class="star-pagination">*188</span> observation contained in another opinion of Mr. Justice Jackson:</p>
<blockquote>"The case which irresistibly comes to mind as the most fitting precedent is that of Julia who, according to Byron's reports, `whispering "I will ne'er consent,"consented.'" <i>Everson</i> v. <i>Board of Education,</i> <span class="citation" data-id="9419925"><a href="/opinion/104373/everson-v-board-of-ed-of-ewing/#19" aria-description="Citation for case: Everson v. Board of Ed. of Ewing">330 U. S. 1, 19</a></span> (1947) (dissenting opinion).</blockquote>
<p>Since I would not "consent" even to the extent that the Court does in its opinion, I dissent from that opinion and would affirm the judgment of the Supreme Court of Delaware.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> were filed by <i>Solicitor General McCree, Assistant Attorney General Civiletti, Kenneth S. Geller, Jerome M. Feit,</i> and <i>Paul J. Brysh</i> for the United States, and by <i>Bruce J. Ennis</i> for the American Civil Liberties Union.</p>
<p>[1]  The affidavit is reproduced as Appendix A to this opinion. <i>Post,</i> at 172.</p>
<p>[2]  The references in paragraphs 15 and 16 of the warrant affidavit's probable-cause page to "James Williams" appear to have been intended as references to James D. Morrison, who was petitioner's supervisor at the Youth Center. Tr. 269. This misapprehension on the part of the State continued until shortly before trial. Eleven days prior to trial, the prosecution requested the Clerk of the Kent Country Superior Court to summon "James Williams, Delaware Youth Center," for petitioner's trial. In his return on the summons, Record Doc. No. 16, the Kent County Sheriff stated that he "[s]erved the within summons upon . . . James Williams (Morrison)." The summons actually delivered was made out in the name of James Morrison.</p>
<p>[3]  It appears this is no longer the majority rule among the States. Compare Comment, <span class="citation no-link">7 Seton Hall L. Rev. 827</span>, 844 (1976) (about half of the States have addressed the issue, and the weight of authority is "slightly in favor" of permitting veracity challenges), with <i>North Carolina</i> v. <i>Wrenn,</i> <span class="citation" data-id="8991165"><a href="/opinion/8998746/north-carolina-v-wrenn/" aria-description="Citation for case: North Carolina v. Wrenn">417 U. S. 973</a></span> (1974) (WHITE, J., dissenting from denial of certiorari) (majority of state decisions prohibit subsequent impeachment of an affidavit).
</p>
<p>By our count, 19 States, and perhaps as many as 21, permit veracity challenges; 5 of these apparently rely on statutory provisions in so holding. Five States have disposed of particular veracity challenges on the ground there was no misstatement, or that any misstatement was immaterial or unintentional, without opining what would be done when there is a deliberate and material misrepresentation. There are now only 11 States that prohibit veracity challenges outright. Another two have barred impeachment challenges that seemed directed at the conclusory nature of affidavit allegations rather than at their veracity.</p>
<p>The case law is detailed in Appendix B. <i>Post,</i> at 176.</p>
<p>[4]  This reasoning is misplaced. The Federal Courts of Appeals decisions allowing a defendant to challenge the veracity of a warrant affidavit rest on a constitutional footing. See <i>United States</i> v. <i>Belculfine,</i> <span class="citation" data-id="324012"><a href="/opinion/324012/united-states-v-joseph-l-belculfine/#61" aria-description="Citation for case: United States v. Joseph L. Belculfine">508 F. 2d 58, 61, 63</a></span> (CA1 1974); <i>United States</i> v. <i>Dunnings,</i> <span class="citation" data-id="9455592"><a href="/opinion/289921/united-states-v-edward-dunnings/#839" aria-description="Citation for case: United States v. Edward Dunnings">425 F. 2d 836, 839-840</a></span> (CA2 1969), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./397/1002/">397 U. S. 1002</a></span> (1970); <i>United States</i> v. <i>Armocida,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/515/29/">515 F. 2d 29</a></span>, 41 (CA3), cert. denied <i>sub nom. </i><i>Gazal</i> v. <i>United States,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./423/858/">423 U. S. 858</a></span> (1975); <i>United States</i> v. <i>Lee,</i> <span class="citation" data-id="9463031"><a href="/opinion/338672/united-states-v-bernard-jerome-lee-aka-james-wesley-carter/#1208" aria-description="Citation for case: United States v. Bernard Jerome Lee, A/K/A James Wesley...">540 F. 2d 1205, 1208-1209</a></span> (CA4), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/894/">429 U. S. 894</a></span> (1976); <i>United States</i> v. <i>Thomas,</i> <span class="citation" data-id="315831"><a href="/opinion/315831/united-states-v-titus-thomas-aka-tee/#668" aria-description="Citation for case: United States v. Titus Thomas, AKA Tee">489 F. 2d 664, 668, 671</a></span> (CA5 1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./423/844/">423 U. S. 844</a></span> (1975); <i>United States</i> v. <i>Luna,</i> <span class="citation" data-id="331000"><a href="/opinion/331000/united-states-v-gilbert-luna/#8" aria-description="Citation for case: United States v. Gilbert Luna">525 F. 2d 4, 8</a></span> (CA6 1975), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./424/965/">424 U. S. 965</a></span> (1976); <i>United States</i> v. <i>Carmichael,</i> <span class="citation" data-id="316109"><a href="/opinion/316109/united-states-v-robert-e-carmichael/#988" aria-description="Citation for case: United States v. Robert E. Carmichael">489 F. 2d 983, 988-989</a></span> (CA7 1973) (en banc); <i>United States</i> v. <i>Marihart,</i> <span class="citation" data-id="9460368"><a href="/opinion/317254/united-states-v-james-marihart/#898" aria-description="Citation for case: United States v. James Marihart">492 F. 2d 897, 898</a></span> (CA8), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/827/">419 U. S. 827</a></span> (1974); <i>United States</i> v. <i>Damitz,</i> <span class="citation" data-id="318456"><a href="/opinion/318456/united-states-v-dwight-edward-damitz-united-states-of-america-v-harry/#54" aria-description="Citation for case: United States v. Dwight Edward Damitz, United States of...">495 F. 2d 50, 54-56</a></span> (CA9 1974); <i>United States</i> v. <i>Harwood,</i> <span class="citation" data-id="307033"><a href="/opinion/307033/united-states-v-gerald-paul-harwood/#324" aria-description="Citation for case: United States v. Gerald Paul Harwood">470 F. 2d 322, 324-325</a></span> (CA10 1972).
</p>
<p>Of all the Federal Courts of Appeals, only one now apparently refrains from permitting challenges to affidavit veracity. See <i>United States</i> v. <i>Watts,</i> 176 U. S. App. D. C. 314, 317-318 n. 5, <span class="citation" data-id="338659"><a href="/opinion/338659/united-states-v-schuessler-watts-jr/" aria-description="Citation for case: United States v. Schuessler Watts, Jr.">540 F. 2d 1093</a></span>, 1096-1097 n. 5 (1976); <i>United States</i> v. <i>Branch,</i> 178 U. S. App. D. C. 99, 102 n. 2, <span class="citation" data-id="340645"><a href="/opinion/340645/united-states-v-joseph-p-branch-united-states-of-america-v-eric-b/" aria-description="Citation for case: United States v. Joseph P. Branch, United States of...">545 F. 2d 177</a></span>, 180 n. 2 (1976).</p>
<p>[5]  Franks did not raise in his petition the issue of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> challenge to the courthouse statement given to police and the use of that statement in the warrant affidavit. The propriety of the trial court's refusal to hear testimony on that subject is therefore not before us. It also appears that Franks did not take that issue to the Supreme Court of Delaware. See Opening Brief for Appellant, No. 259, 1976 (Del. Sup. Ct.).</p>
<p>[6]  The <i><span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">Rugendorf</a></span></i> affidavit, sworn to by FBI Special Agent Moore, contained two alleged inaccuracies; a double hearsay statement that petitioner Samuel Rugendorf was the manager of Rugendorf Brothers Meat Market, and a double hearsay statement that he was associated with his brother, Leo, in the meat business. As to the second, the affidavit stated that a confidential informant told FBI Special Agent McCormick about the Rugendorf brothers' association, and McCormick told affiant Moore. As to the first, the affidavit stated that the information was given by Chicago Police Officer Kelleher to Special Agent McCormick, who in turn relayed it to affiant Moore. Kelleher testified that he did not so inform McCormick, but the petitioner in <i><span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">Rugendorf</a></span></i> had failed to pursue the discrepancy: He did not seek a deposition from McCormick, who was in the hospital at the time of trial, and did not seek a postponement to enable McCormick to be present. <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">376 U. S., at 533</a></span> n. 4. In characterizing the affidavit in <i><span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">Rugendorf</a></span></i> as raising no question of integrity, the Court took as its premise that police could not insulate one officer's deliberate misstatement merely by relaying it through an officer-affiant personally ignorant of its falsity.</p>
<p>[7]  Mascolo, Impeaching the Credibility of Affidavits for Search Warrants: Piercing the Presumption of Validity, 44 Conn. Bar J. 9, 19, 25-28 (1970); Kipperman, Inaccurate Search Warrant Affidavits as a Ground for Suppressing Evidence, <span class="citation no-link">84 Harv. L. Rev. 825</span>, 830-832 (1971); Grano, A Dilemma for Defense Counsel; Spinelli-Harris Search Warrants and the Possibility of Police Perjury, 1971 U. Ill. Law Forum 405, 456; Forkosh, The Constitutional Right to Challenge the Content of Affidavits in Warrants Issued Under the Fourth Amendment, 34 Ohio St. L. J. 297, 306, 308, 340 (1973); Sevilla, The Exclusionary Rule and Police Perjury, <span class="citation no-link">11 San Diego L. Rev. 839</span>, 869 (1974); Herman, Warrants for Arrest or Search: Impeaching the Allegations of a Facially Sufficient Affidavit, 36 Ohio St. L. J. 721, 738-739, 750 (1975); Note, 15 Buffalo L. Rev. 712, 716-717 (1966); Note, 51 Cornell L. Q. 822, 825-826 (1966); Note, 34 Ford. L. Rev. 740, 745 (1966); Note, <span class="citation no-link">67 Colum. L. Rev. 1529</span>, 1530-1531 (1967); Comment, <span class="citation no-link">19 UCLA L. Rev. 96</span>, 108, 146 (1971); Comment, 63 J. Crim. L., C. &amp; P. S. 41, 48, 50 (1972); Note, <span class="citation no-link">23 Drake L. Rev. 623</span>, 638-639 (1974); Comment, <span class="citation no-link">7 Seton Hall L. Rev. 827</span>, 859-860 (1976).</p>
<p>[8]  Petitioner conceded that if what is left is sufficient to sustain probable cause, the inaccuracies are irrelevant. Tr. of Oral Arg. 3, 13. Petitioner also conceded that if the warrant affiant had no reason to believe the information was false, there was no violation of the Fourth Amendment. <span class="citation no-link"><i>Id.,</i> at 16-17</span>.</p>

</div>
```

---

## GROUP: content/cases/Garrity v. New Jersey.md  (`case`, 5 assertions)

### content_page

```
---
title: "Garrity v. New Jersey"
type: case
citation: "385 U.S. 493 (1967)"
parallel_cite: "87 S. Ct. 616; 17 L. Ed. 2d 562"
neutral_cite: 1967 U.S. LEXIS 2882
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-01-23
docket: 13
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-01-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Garrity v. New Jersey
  varies_by_point: false
  scope_note: "Good law; foundation of the 'Garrity rule' / Garrity warnings for compelled public-employee statements."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107336/garrity-v-new-jersey/"
  cluster_id: 107336
  opinion_id: 107336
  identity_checked: true
homes:
  - page: "[[Public-Employee Compelled Statements (Garrity)]]"
    role: "Key — Anchor"
related: ["[[Gardner v. Broderick]]", "[[Lefkowitz v. Turley]]", "[[Kalkines v. United States]]"]
aliases: []
tags: ["case", "fifth-amendment", "self-incrimination", "public-employee", "garrity", "compelled-statements"]
holding: "Statements compelled from a public employee under threat of removal from office are involuntary, and the Fourteenth Amendment bars their use against the employee in a subsequent criminal prosecution (the Garrity rule)."
lake:
  record_id: Garrity v. New Jersey
  status: verified
  projected_at: 2026-07-09
---

# Garrity v. New Jersey

*385 U.S. 493 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
New Jersey police officers were investigated for fixing traffic tickets. Before questioning, each officer was warned that anything he said could be used against him in a criminal proceeding, that he could refuse to answer to avoid self-incrimination, but that under a state forfeiture-of-office statute a refusal to answer would cost him his job. The officers answered, and their statements were used to convict them of conspiracy to obstruct the administration of the traffic laws. They challenged the convictions as resting on coerced statements.

## Issue
Whether statements obtained from public employees under threat of removal from office are made voluntarily, such that they may be used against the employees in a subsequent criminal prosecution consistent with the Fourteenth Amendment.

## Rule
No. The threat of discharge renders such statements involuntary. "The choice given petitioners was either to forfeit their jobs or to incriminate themselves. The option to lose their means of livelihood or to pay the penalty of self-incrimination is the antithesis of free choice to speak out or to remain silent." — 385 U.S. at 497. ^pin-497

The Court therefore held: "We now hold the protection of the individual under the Fourteenth Amendment against coerced statements prohibits use in subsequent criminal proceedings of statements obtained under threat of removal from office, and that it extends to all, whether they are policemen or other members of our body politic." — [*Id.* at 500](https://www.courtlistener.com/opinion/107336/garrity-v-new-jersey/#:~:text=We%20now%20hold%20the%20protection). ^pin-500

## Application
Each officer was confronted with the choice to answer the investigators' questions or lose his job under the forfeiture statute. Faced with self-incrimination on one side and loss of livelihood on the other, the officers' answers were the product of coercion rather than free will, much like the pressures condemned in *[[Miranda v. Arizona|Miranda]]*. Because the convictions rested on these compelled statements, they could not stand.

## Conclusion
The statements were coerced and inadmissible in the criminal prosecutions; the convictions were reversed. *Garrity* establishes that a public employer may not compel an employee, on pain of job loss, to make statements that are then used against him in a criminal case — the foundation of the "Garrity rule" and [[Public-Employee Compelled Statements (Garrity)|Garrity warnings]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Garrity* is good law and anchors the public-employee compelled-statement line, refined by [[Gardner v. Broderick]] and [[Lefkowitz v. Turley]] (a public employee may be compelled to answer narrowly job-related questions only under a grant of use immunity, and may not be fired merely for asserting the privilege) and the federal [[Kalkines v. United States]] warning.

## Appears on
- [[Public-Employee Compelled Statements (Garrity)]] — *Key — Anchor*

## Sources
- *Garrity v. New Jersey*, 385 U.S. 493 (1967) — https://www.courtlistener.com/opinion/107336/garrity-v-new-jersey/ — pinpoints: 497, 500.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b8426cb210a601b7", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "385 U.S. 493 (1967)", "court": "U.S. Supreme Court", "neutral_cite": "1967 U.S. LEXIS 2882", "official_citation_present": true, "parallel_cite": "87 S. Ct. 616; 17 L. Ed. 2d 562", "title": "Garrity v. New Jersey", "year": "1967"}}
{"assertion_id": "65af23ddeb4ee0ec", "dimension": "support", "kind": "home_role", "locator": {"home": "Public-Employee Compelled Statements (Garrity)"}, "payload": {"home": "Public-Employee Compelled Statements (Garrity)", "role": "Key — Anchor", "title": "Garrity v. New Jersey"}}
{"assertion_id": "9d51828449f681d6", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Statements compelled from a public employee under threat of removal from office are involuntary, and the Fourteenth Amendment bars their use against the employee in a subsequent criminal prosecution (the Garrity rule).", "title": "Garrity v. New Jersey"}}
{"assertion_id": "d68d47b846a7aa2b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1967-01-16", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Garrity v. New Jersey", "field_i_validity": "good_law", "scope_note": "Good law; foundation of the 'Garrity rule' / Garrity warnings for compelled public-employee statements.", "title": "Garrity v. New Jersey", "varies_by_point": "false"}}
{"assertion_id": "f8af268c6324e59a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Garrity v. New Jersey"}}
```

### lake record — Garrity v. New Jersey

```json
{
  "schema_version": "s2.v1",
  "record_id": "Garrity v. New Jersey",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Garrity v. New Jersey",
    "case_name_short": "Garrity",
    "case_name_full": "GARRITY Et Al. v. NEW JERSEY",
    "input_case_name": "Garrity v. New Jersey",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-01-23",
    "year": 1967,
    "docket": "13",
    "cluster_id": 107336,
    "lead_opinion_id": 107336,
    "sibling_ids": [
      107336,
      9423318,
      9423319
    ],
    "absolute_url": "/opinion/107336/garrity-v-new-jersey/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "385 U.S. 493",
      "volume": "385",
      "reporter": "U.S.",
      "page": "493",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 616",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "616",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 562",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "562",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 2882",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2882",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "385 U.S. 493",
        "volume": "385",
        "reporter": "U.S.",
        "page": "493",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 616",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "616",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 562",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "562",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 2882",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2882",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "385 U.S. 493",
    "official_selection": {
      "court_class": "scotus",
      "selected": "385 U.S. 493",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-497",
      "page": null,
      "quote": "--- # Garrity v. New Jersey *385 U.S. 493 (1967)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background New Jersey police officers were investigated for fixing traffic tickets. Before questioning, each officer was warned that anything he said could be used against him in a criminal proceeding, that he could refuse to answer to avoid self-incrimination, but that under a state forfeiture-of-office statute a refusal to answer would cost him his job. The officers answered, and their statements were used to convict them of conspiracy to obstruct the administration of the traffic laws. They challenged the convictions as resting on coerced statements. ## Issue Whether statements obtained from public employees under threat of removal from office are made voluntarily, such that they may be used against the employees in a subsequent criminal prosecution consistent with the Fourteenth Amendment. ## Rule No. The threat of discharge renders such statements involuntary.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-500",
      "page": null,
      "quote": "We now hold the protection of the individual under the Fourteenth Amendment against coerced statements prohibits use in subsequent criminal proceedings of statements obtained under threat of removal from office, and that it extends to all, whether they are policemen or other members of our body politic.",
      "star_marker": "500",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15381,
      "fragment": "#:~:text=We%20now%20hold%20the%20protection",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-01-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Garrity v. New Jersey",
    "varies_by_point": false,
    "scope_note": "Good law; foundation of the 'Garrity rule' / Garrity warnings for compelled public-employee statements.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Gideon",
          "cluster_id": 4632199,
          "cite": [
            "2019 Ohio 2482",
            "130 N.E.3d 357"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Allen",
          "cluster_id": 4409967,
          "cite": [
            "864 F.3d 63",
            "2017 U.S. App. LEXIS 12942",
            "2017 WL 3040201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gregory Wayne Powell",
          "cluster_id": 4348676,
          "cite": [
            "161 Idaho 774",
            "391 P.3d 659",
            "2017 WL 587254",
            "2017 Ida. App. LEXIS 17"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Von Behren",
          "cluster_id": 3202148,
          "cite": [
            "822 F.3d 1139",
            "2016 U.S. App. LEXIS 8567",
            "2016 WL 2641270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "National Railroad Passenger Corporation v. Fraternal Order of Police, Lodge 189",
          "cluster_id": 3151447,
          "cite": [
            "142 F. Supp. 3d 82",
            "204 L.R.R.M. (BNA) 3525",
            "2015 U.S. Dist. LEXIS 148320",
            "2015 WL 6692104"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "James Patrick Smith v. State",
          "cluster_id": 2854959,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Korey Demaine Walker v. State",
          "cluster_id": 2855445,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Spielbauer v. County of Santa Clara",
          "cluster_id": 5608087,
          "cite": [
            "45 Cal. 4th 704",
            "199 P.3d 1125",
            "88 Cal. Rptr. 3d 590",
            "28 I.E.R. Cas. (BNA) 1254",
            "2009 Cal. LEXIS 1010"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Aguilera v. Baca",
          "cluster_id": 1390016,
          "cite": [
            "510 F.3d 1161",
            "27 I.E.R. Cas. (BNA) 31",
            "2007 U.S. App. LEXIS 29804",
            "2007 WL 4531990"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Sher v. U.S. Department of Veterans Affairs",
          "cluster_id": 202763,
          "cite": [
            "488 F.3d 489",
            "26 I.E.R. Cas. (BNA) 243",
            "2007 U.S. App. LEXIS 12365",
            "90 Empl. Prac. Dec. (CCH) 43,067",
            "100 Fair Empl. Prac. Cas. (BNA) 1495",
            "2007 WL 1532655"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
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
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baxter v. Palmigiano",
          "cluster_id": 109429,
          "cite": [
            "47 L. Ed. 2d 810",
            "96 S. Ct. 1551",
            "425 U.S. 308",
            "1976 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dunn v. Blumstein",
          "cluster_id": 108485,
          "cite": [
            "31 L. Ed. 2d 274",
            "92 S. Ct. 995",
            "405 U.S. 330",
            "1972 U.S. LEXIS 75"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
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
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cox Broadcasting Corp. v. Cohn",
          "cluster_id": 109207,
          "cite": [
            "43 L. Ed. 2d 328",
            "95 S. Ct. 1029",
            "420 U.S. 469",
            "1975 U.S. LEXIS 139",
            "32 Rad. Reg. 2d (P & F) 1511",
            "1 Media L. Rep. (BNA) 1819"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lefkowitz v. Turley",
          "cluster_id": 108882,
          "cite": [
            "38 L. Ed. 2d 274",
            "94 S. Ct. 316",
            "414 U.S. 70",
            "1973 U.S. LEXIS 132"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McGautha v. California",
          "cluster_id": 108329,
          "cite": [
            "28 L. Ed. 2d 711",
            "91 S. Ct. 1454",
            "402 U.S. 183",
            "1971 U.S. LEXIS 107"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
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
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maness v. Meyers",
          "cluster_id": 109130,
          "cite": [
            "42 L. Ed. 2d 574",
            "95 S. Ct. 584",
            "419 U.S. 449",
            "1975 U.S. LEXIS 20"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parker v. North Carolina",
          "cluster_id": 108139,
          "cite": [
            "25 L. Ed. 2d 785",
            "90 S. Ct. 1458",
            "397 U.S. 790",
            "1970 U.S. LEXIS 47"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lefkowitz v. Cunningham",
          "cluster_id": 109683,
          "cite": [
            "53 L. Ed. 2d 1",
            "97 S. Ct. 2132",
            "431 U.S. 801",
            "1977 U.S. LEXIS 19"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gardner v. Broderick",
          "cluster_id": 107738,
          "cite": [
            "20 L. Ed. 2d 1082",
            "88 S. Ct. 1913",
            "392 U.S. 273",
            "1968 U.S. LEXIS 1351"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garner v. United States",
          "cluster_id": 109400,
          "cite": [
            "47 L. Ed. 2d 370",
            "96 S. Ct. 1178",
            "424 U.S. 648",
            "1976 U.S. LEXIS 138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mandujano",
          "cluster_id": 109442,
          "cite": [
            "48 L. Ed. 2d 212",
            "96 S. Ct. 1768",
            "425 U.S. 564",
            "1976 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kelley v. Johnson",
          "cluster_id": 109423,
          "cite": [
            "47 L. Ed. 2d 708",
            "96 S. Ct. 1440",
            "425 U.S. 238",
            "1976 U.S. LEXIS 35",
            "11 Empl. Prac. Dec. (CCH) 10,788"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dennis v. Higgins",
          "cluster_id": 112534,
          "cite": [
            "112 L. Ed. 2d 969",
            "111 S. Ct. 865",
            "498 U.S. 439",
            "1991 U.S. LEXIS 1142"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Uniformed Sanitation Men Ass'n v. Commissioner of Sanitation of New York",
          "cluster_id": 107739,
          "cite": [
            "20 L. Ed. 2d 1089",
            "88 S. Ct. 1917",
            "392 U.S. 280",
            "1968 U.S. LEXIS 1352"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kenneth Wynder v. James W. McMahon David Spahl, Robert Jones, Louis B. Barbaria, Craig Masterson, Individually, John Keats, Marine Midland Bank",
          "cluster_id": 785304,
          "cite": [
            "360 F.3d 73",
            "2004 U.S. App. LEXIS 3906",
            "93 Fair Empl. Prac. Cas. (BNA) 596",
            "2004 WL 370665"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Byers",
          "cluster_id": 108335,
          "cite": [
            "29 L. Ed. 2d 9",
            "91 S. Ct. 1535",
            "402 U.S. 424",
            "1971 U.S. LEXIS 128"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 1670023,
          "cite": [
            "755 N.W.2d 664",
            "279 Mich. App. 116"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles E. Egger v. Harlan C. Phillips",
          "cluster_id": 420747,
          "cite": [
            "710 F.2d 292"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Selective Service System v. Minnesota Public Interest Research Group",
          "cluster_id": 111260,
          "cite": [
            "82 L. Ed. 2d 632",
            "104 S. Ct. 3348",
            "468 U.S. 841",
            "1984 U.S. LEXIS 151",
            "52 U.S.L.W. 5140"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salinas v. Texas",
          "cluster_id": 903977,
          "cite": [
            "186 L. Ed. 2d 376",
            "133 S. Ct. 2174",
            "2013 U.S. LEXIS 4697",
            "570 U.S. 178",
            "81 U.S.L.W. 4467",
            "24 Fla. L. Weekly Fed. S 294",
            "2013 WL 2922119"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Avant v. Clifford",
          "cluster_id": 1549504,
          "cite": [
            "341 A.2d 629",
            "67 N.J. 496",
            "1975 N.J. LEXIS 205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sheldon L. Wulf v. The City of Wichita, Gene Denton, and Richard Lamunyon",
          "cluster_id": 528293,
          "cite": [
            "883 F.2d 842"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107336 OR 9423318 OR 9423319) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTQ2MDk2MDAwMDAwJnM9NDExMzg5MCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107336+OR+9423318+OR+9423319%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107336 OR 9423318 OR 9423319)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTQmcz0xMTIzNjAmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107336+OR+9423318+OR+9423319%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107336 OR 9423318 OR 9423319)",
        "reviewed": 22,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 22,
        "triage_read": 0,
        "triage_snippet_classified": 22
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107336 OR 9423318 OR 9423319)",
    "indexed_citing_opinions": 1024,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107336,
        "count": 906,
        "count_source": "search"
      },
      {
        "opinion_id": 9423318,
        "count": 134,
        "count_source": "search"
      },
      {
        "opinion_id": 9423319,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1543,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/garrity-v-new-jersey.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc5NzUwMzUmcz04NDA0NDA5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107336+OR+9423318+OR+9423319%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107336,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 97150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 99227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 99901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 101688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 102991,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 103831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 104061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 105377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 105743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 106007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 107033,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 107064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 107173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 228335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 2286396,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 2402426,
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
    "date_created": "2026-07-05T05:12:44Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:12:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:12:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:18:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:12:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Garrity v. New Jersey

```
<div>
<center><b><span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">385 U.S. 493</a></span> (1967)</b></center>
<center><h1>GARRITY ET AL.<br>
v.<br>
NEW JERSEY.</h1></center>
<center>No. 13.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 10, 1966.</center>
<center>Decided January 16, 1967.</center>
APPEAL FROM THE SUPREME COURT OF NEW JERSEY.
<p><span class="star-pagination">*494</span> <i>Daniel L. O'Connor</i> argued the cause for appellants. With him on the brief was <i>Eugene Gressman.</i></p>
<p><i>Alan B. Handler,</i> First Assistant Attorney General of New Jersey, argued the cause for appellee. With him on the brief were <i>Arthur J. Sills,</i> Attorney General, and <i>Norman Heine.</i></p>
<p>MR. JUSTICE DOUGLAS delivered the opinion of the Court.</p>
<p>Appellants were police officers in certain New Jersey boroughs. The Supreme Court of New Jersey ordered that alleged irregularities in handling cases in the municipal courts of those boroughs be investigated by the Attorney General, invested him with broad powers of inquiry and investigation, and directed him to make a report to the court. The matters investigated concerned alleged fixing of traffic tickets.</p>
<p>Before being questioned, each appellant was warned (1) that anything he said might be used against him in any state criminal proceeding; (2) that he had the privilege to refuse to answer if the disclosure would tend to incriminate him; but (3) that if he refused to answer he would be subject to removal from office.<sup>[1]</sup></p>
<p><span class="star-pagination">*495</span> Appellants answered the questions. No immunity was granted, as there is no immunity statute applicable in these circumstances. Over their objections, some of the answers given were used in subsequent prosecutions for conspiracy to obstruct the administration of the traffic laws. Appellants were convicted and their convictions were sustained over their protests that their statements were coerced,<sup>[2]</sup> by reason of the fact that, if they refused to answer, they could lose their positions with the police department. See 44 N. J. 209, <span class="citation" data-id="2402426"><a href="/opinion/2402426/state-v-naglee/" aria-description="Citation for case: State v. Naglee">207 A. 2d 689</a></span>, 44 N. J. 259, <span class="citation" data-id="2286396"><a href="/opinion/2286396/state-v-holroyd/" aria-description="Citation for case: State v. Holroyd">208 A. 2d 146</a></span>.</p>
<p>We postponed the question of jurisdiction to a hearing on the merits. <span class="citation multiple-matches"><a href="/c/U.%20S./383/941/">383 U. S. 941</a></span>. The statute whose validity was sought to be "drawn in question," <span class="citation no-link">28 U. S. C. § 1257</span> (2), was the forfeiture statute.<sup>[3]</sup> But the New <span class="star-pagination">*496</span> Jersey Supreme Court refused to reach that question (44 N. J., at 223, <span class="citation" data-id="2402426"><a href="/opinion/2402426/state-v-naglee/#697" aria-description="Citation for case: State v. Naglee">207 A. 2d, at 697</a></span>), deeming the voluntariness of the statements as the only issue presented. <i>Id.,</i> at 220-222, <span class="citation" data-id="2402426"><a href="/opinion/2402426/state-v-naglee/#695" aria-description="Citation for case: State v. Naglee">207 A. 2d, at 695-696</a></span>. The statute is therefore too tangentially involved to satisfy <span class="citation no-link">28 U. S. C. § 1257</span> (2), for the only bearing it had was whether, valid or not, the fear of being discharged under it for refusal to answer on the one hand and the fear of self-incrimination on the other was "a choice between the rock and the whirlpool"<sup>[4]</sup> which made the statements products of coercion in violation of the Fourteenth Amendment. We therefore dismiss the appeal, treat the papers as a petition for certiorari (<span class="citation no-link">28 U. S. C. § 2103</span>), grant the petition and proceed to the merits.</p>
<p>We agree with the New Jersey Supreme Court that the forfeiture-of-office statute is relevant here only for the bearing it has on the voluntary character of the statements used to convict petitioners in their criminal prosecutions.</p>
<p>The choice imposed on petitioners was one between self-incrimination or job forfeiture. Coercion that vitiates a confession under <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span>, and related cases can be "mental as well as physical"; "the blood of the accused is not the only hallmark of an unconstitutional inquisition." <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 206</a></span>. Subtle pressures (<i>Leyra</i> v. <i>Denno,</i> <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556</a></span>; <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span>) may be as telling as coarse and vulgar ones. The question is whether the accused was deprived of his "free choice to admit, to deny, or to refuse to answer." <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#241" aria-description="Citation for case: Lisenba v. California">314 U. S. 219, 241</a></span>.</p>
<p>We adhere to <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, a civil forfeiture action against property. A statute offered <span class="star-pagination">*497</span> the owner an election between producing a document or forfeiture of the goods at issue in the proceeding. This was held to be a form of compulsion in violation of both the Fifth Amendment and the Fourth Amendment. <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#634" aria-description="Citation for case: Boyd v. United States"><i>Id.,</i> at 634-635</a></span>. It is that principle that we adhere to and apply in <i>Spevack</i> v. <i>Klein</i><i>, post,</i> p. 511.</p>
<p>The choice given petitioners was either to forfeit their jobs or to incriminate themselves. The option to lose their means of livelihood or to pay the penalty of self-incrimination is the antithesis of free choice to speak out or to remain silent. That practice, like interrogation practices we reviewed in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#464" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 464-465</a></span>, is "likely to exert such pressure upon an individual as to disable him from making a free and rational choice." We think the statements were infected by the coercion<sup>[5]</sup> inherent in this scheme of questioning <span class="star-pagination">*498</span> and cannot be sustained as voluntary under our prior decisions.</p>
<p>It is said that there was a "waiver." That, however, is a federal question for us to decide. <i>Union Pac. R. R. Co.</i> v. <i>Pub. Service Comm.,</i> <span class="citation" data-id="99227"><a href="/opinion/99227/union-pacific-railroad-v-public-service-commission/#69" aria-description="Citation for case: Union Pacific Railroad v. Public Service Commission">248 U. S. 67, 69-70</a></span>; <i>Stevens</i> v. <i>Marks,</i> <span class="citation" data-id="9423156"><a href="/opinion/107173/stevens-v-marks/#243" aria-description="Citation for case: Stevens v. Marks">383 U. S. 234, 243-244</a></span>. The Court in <i>Union Pac. R. R. Co.</i> v. <i>Pub. Service <span class="citation" data-id="99227"><a href="/opinion/99227/union-pacific-railroad-v-public-service-commission/" aria-description="Citation for case: Union Pacific Railroad v. Public Service Commission">Comm., supra</a></span></i><i>,</i> in speaking of a certificate exacted under protest and in violation of the Commerce Clause, said:</p>
<blockquote>"Were it otherwise, as conduct under duress involves a choice, it always would be possible for a State to impose an unconstitutional burden by the threat of penalties worse than it in case of a failure to accept it, and then to declare the acceptance voluntary . . . ." <span class="citation" data-id="99227"><a href="/opinion/99227/union-pacific-railroad-v-public-service-commission/#70" aria-description="Citation for case: Union Pacific Railroad v. Public Service Commission"><i>Id.,</i> at 70</a></span>.</blockquote>
<p>Where the choice is "between the rock and the whirlpool," duress is inherent in deciding to "waive" one or the other.</p>
<blockquote>"It always is for the interest of a party under duress to choose the lesser of two evils. But the fact that a choice was made according to interest does not exclude duress. It is the characteristic of duress properly so called." <i><span class="citation" data-id="99227"><a href="/opinion/99227/union-pacific-railroad-v-public-service-commission/" aria-description="Citation for case: Union Pacific Railroad v. Public Service Commission">Ibid.</a></span></i>
</blockquote>
<p><span class="star-pagination">*499</span> In that case appellant paid under protest. In these cases also, though petitioners succumbed to compulsion, they preserved their objections, raising them at the earliest possible point. Cf. <i>Abie State Bank</i> v. <i>Bryan,</i> <span class="citation" data-id="101688"><a href="/opinion/101688/abie-state-bank-v-bryan/#776" aria-description="Citation for case: Abie State Bank v. Bryan">282 U. S. 765, 776</a></span>. The cases are therefore quite different from the situation where one who is anxious to make a clean breast of the whole affair volunteers the information.</p>
<p>Mr. Justice Holmes in <i>McAuliffe</i> v. <i>New Bedford,</i> <span class="citation" data-id="6424016"><a href="/opinion/6550282/mcauliffe-v-mayor-and-board-of-aldermen/" aria-description="Citation for case: McAuliffe v. Mayor and Board of Aldermen">155 Mass. 216</a></span>, <span class="citation" data-id="6424016"><a href="/opinion/6550282/mcauliffe-v-mayor-and-board-of-aldermen/" aria-description="Citation for case: McAuliffe v. Mayor and Board of Aldermen">29 N. E. 517</a></span>, stated a dictum on which New Jersey heavily relies:</p>
<blockquote>"The petitioner may have a constitutional right to talk politics, but he has no constitutional right to be a policeman. There are few employments for hire in which the servant does not agree to suspend his constitutional right of free speech, as well as of idleness, by the implied terms of his contract. The servant cannot complain, as he takes the employment on the terms which are offered him. On the same principle, the city may impose any reasonable condition upon holding offices within its control." <span class="citation" data-id="6424016"><a href="/opinion/6550282/mcauliffe-v-mayor-and-board-of-aldermen/#220" aria-description="Citation for case: McAuliffe v. Mayor and Board of Aldermen"><i>Id.,</i> at 220</a></span>, <span class="citation" data-id="6424016"><a href="/opinion/6550282/mcauliffe-v-mayor-and-board-of-aldermen/#517" aria-description="Citation for case: McAuliffe v. Mayor and Board of Aldermen">29 N. E., at 517-518</a></span>.</blockquote>
<p>The question in this case, however, is not cognizable in those terms. Our question is whether a State, contrary to the requirement of the Fourteenth Amendment, can use the threat of discharge to secure incriminatory evidence against an employee.</p>
<p>We held in <i>Slochower</i> v. <i>Board of Education,</i> <span class="citation" data-id="9421254"><a href="/opinion/105377/slochower-v-board-of-higher-ed-of-new-york-city/" aria-description="Citation for case: Slochower v. Board of Higher Ed. of New York City">350 U. S. 551</a></span>, that a public school teacher could not be discharged merely because he had invoked the Fifth Amendment privilege against self-incrimination when questioned by a congressional committee:</p>
<blockquote>"The privilege against self-incrimination would be reduced to a hollow mockery if its exercise could be taken as equivalent either to a confession of <span class="star-pagination">*500</span> guilt or a conclusive presumption of perjury. . . . The privilege serves to protect the innocent who otherwise might be ensnared by ambiguous circumstances." <span class="citation" data-id="9421254"><a href="/opinion/105377/slochower-v-board-of-higher-ed-of-new-york-city/#557" aria-description="Citation for case: Slochower v. Board of Higher Ed. of New York City"><i>Id.,</i> at 557-558</a></span>.</blockquote>
<p>We conclude that policemen, like teachers and lawyers, are not relegated to a watered-down version of constitutional rights.</p>
<p>There are rights of constitutional stature whose exercise a State may not condition by the exaction of a price. Engaging in interstate commerce is one. <i>Western Union Tel. Co.</i> v. <i>Kansas,</i> <span class="citation" data-id="9418165"><a href="/opinion/97150/western-union-telegraph-co-v-kansas-ex-rel-coleman/" aria-description="Citation for case: Western Union Telegraph Co. v. Kansas Ex Rel. Coleman">216 U. S. 1</a></span>. Resort to the federal courts in diversity of citizenship cases is another. <i>Terral</i> v. <i>Burke Constr. Co.,</i> <span class="citation" data-id="99901"><a href="/opinion/99901/terral-v-burke-construction-co/" aria-description="Citation for case: Terral v. Burke Construction Co.">257 U. S. 529</a></span>. Assertion of a First Amendment right is still another. <i>Lovell</i> v. <i>City of Griffin,</i> <span class="citation" data-id="102991"><a href="/opinion/102991/lovell-v-city-of-griffin/" aria-description="Citation for case: Lovell v. City of Griffin">303 U. S. 444</a></span>; <i>Murdock</i> v. <i>Pennsylvania,</i> <span class="citation" data-id="9419338"><a href="/opinion/103831/murdock-v-pennsylvania/" aria-description="Citation for case: Murdock v. Pennsylvania">319 U. S. 105</a></span>; <i>Thomas</i> v. <i>Collins,</i> <span class="citation" data-id="9419572"><a href="/opinion/104061/thomas-v-collins/" aria-description="Citation for case: Thomas v. Collins">323 U. S. 516</a></span>; <i>Lamont</i> v. <i>Postmaster General,</i> <span class="citation" data-id="9423040"><a href="/opinion/107064/lamont-v-postmaster-general/#305" aria-description="Citation for case: Lamont v. Postmaster General">381 U. S. 301, 305-306</a></span>. The imposition of a burden on the exercise of a Twenty-fourth Amendment right is also banned. <i>Harman</i> v. <i>Forssenius,</i> <span class="citation" data-id="107033"><a href="/opinion/107033/harman-v-forssenius/" aria-description="Citation for case: Harman v. Forssenius">380 U. S. 528</a></span>. We now hold the protection of the individual under the Fourteenth Amendment against coerced statements prohibits use in subsequent criminal proceedings of statements obtained under threat of removal from office, and that it extends to all, whether they are policemen or other members of our body politic.</p>
<p><i>Reversed.</i></p>
<p>[For dissenting opinion of MR. JUSTICE WHITE, see <i>post,</i> p. 530.]</p>
<p>MR. JUSTICE HARLAN, whom MR. JUSTICE CLARK and MR. JUSTICE STEWART join, dissenting.</p>
<p>The majority opinion here and the plurality opinion in <i>Spevack</i> v. <i>Klein</i><i>, post,</i> p. 511, stem from fundamental misconceptions about the logic and necessities of the <span class="star-pagination">*501</span> constitutional privilege against self-incrimination. I fear that these opinions will seriously and quite needlessly hinder the protection of other important public values. I must dissent here, as I do in <i>Spevack.</i></p>
<p>The majority employs a curious mixture of doctrines to invalidate these convictions, and I confess to difficulty in perceiving the intended relationships among the various segments of its opinion. I gather that the majority believes that the possibility that these policemen might have been discharged had they refused to provide information pertinent to their public responsibilities is an impermissible "condition" imposed by New Jersey upon petitioners' privilege against self-incrimination. From this premise the majority draws the conclusion that the statements obtained from petitioners after a warning that discharge was possible were inadmissible. Evidently recognizing the weakness of its conclusion, the majority attempts to bring to its support illustrations from the lengthy series of cases in which this Court, in light of all the relevant circumstances, has adjudged the voluntariness <i>in fact</i> of statements obtained from accused persons.</p>
<p>The majority is apparently engaged in the delicate task of riding two unruly horses at once: it is presumably arguing simultaneously that the statements were involuntary as a matter of fact, in the same fashion that the statements in <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span>, and <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span>, were thought to be involuntary, and that the statements were inadmissible as a matter of law, on the premise that they were products of an impermissible condition imposed on the constitutional privilege. These are very different contentions and require separate replies, but in my opinion both contentions are plainly mistaken, for reasons that follow.</p>
<p></p>
<h2>
<span class="star-pagination">*502</span> I.</h2>
<p>I turn first to the suggestion that these statements were involuntary in fact. An assessment of the voluntariness of the various statements in issue here requires a more comprehensive examination of the pertinent circumstances than the majority has undertaken.</p>
<p>The petitioners were at all material times policemen in the boroughs of Bellmawr and Barrington, New Jersey. Garrity was Bellmawr's chief of police and Virtue one of its police officers; Holroyd, Elwell, and Murray were police officers in Barrington. Another defendant below, Mrs. Naglee, the clerk of Bellmawr's municipal court, has since died. In June 1961 the New Jersey Supreme Court <i>sua sponte</i> directed the State's Attorney General to investigate reports of traffic ticket fixing in Bellmawr and Barrington. Subsequent investigations produced evidence that the petitioners, in separate conspiracies, had falsified municipal court records, altered traffic tickets, and diverted moneys produced from bail and fines to unauthorized purposes. In the course of these investigations the State obtained two sworn statements from each of the petitioners; portions of those statements were admitted at trial. The petitioners were convicted in two separate trials of conspiracy to obstruct the proper administration of the state motor traffic laws, the cases being now consolidated for purposes of our review. The Supreme Court of New Jersey affirmed all the convictions.</p>
<p>The first statements were taken from the petitioners by the State's Deputy Attorney General in August and November 1961. All of the usual indicia of duress are wholly absent. As the state court noted, there was "no physical coercion, no overbearing tactics of psychological persuasion, no lengthy incommunicado detention, or efforts to humiliate or ridicule the defendants." 44 N. J. <span class="star-pagination">*503</span> 209, 220, <span class="citation" data-id="2402426"><a href="/opinion/2402426/state-v-naglee/#695" aria-description="Citation for case: State v. Naglee">207 A. 2d 689, 695</a></span>. The state court found no evidence that any of the petitioners were reluctant to offer statements, and concluded that the interrogations were conducted with a "high degree of civility and restraint." <i><span class="citation" data-id="2402426"><a href="/opinion/2402426/state-v-naglee/" aria-description="Citation for case: State v. Naglee">Ibid.</a></span></i></p>
<p>These conclusions are fully substantiated by the record. The statements of the Bellmawr petitioners were taken in a room in the local firehouse, for which Chief Garrity himself had made arrangements. None of the petitioners were in custody before or after the depositions were taken; each apparently continued to pursue his ordinary duties as a public official of the community. The statements were recorded by a court stenographer, who testified that he witnessed no indications of unwillingness or even significant hesitation on the part of any of the petitioners. The Bellmawr petitioners did not have counsel present, but the Deputy Attorney General testified without contradiction that Garrity had informed him as they strolled between Garrity's office and the firehouse that he had arranged for counsel, but thought that none would be required at that stage. The interrogations were not excessively lengthy, and reasonable efforts were made to assure the physical comfort of the witnesses. Mrs. Naglee, the clerk of the Bellmawr municipal court, who was known to suffer from a heart ailment, was assured that questioning would cease if she felt any discomfort.</p>
<p>The circumstances in which the depositions of the Barrington petitioners were taken are less certain, for the New Jersey Supreme Court found that there was an informal agreement at the Barrington trial that the defendants would argue simply that the possibility of dismissal made the statements "involuntary as a matter of law." The defense did not contend that the statements were the result of physical or mental coercion, or that the wills of the Barrington petitioners were overborne. Accordingly, the State was never obliged to offer evidence <span class="star-pagination">*504</span> of the voluntariness in fact of the statements. We are, however, informed that the three Barrington petitioners had counsel present as their depositions were taken. Insofar as the majority suggests that the Barrington statements are involuntary in fact, in the fashion of <i><span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">Chambers</a></span></i> or <i><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">Haynes</a></span>,</i> it has introduced a factual contention never urged by the Barrington petitioners and never considered by the courts of New Jersey.</p>
<p>As interrogation commenced, each of the petitioners was sworn, carefully informed that he need not give any information, reminded that any information given might be used in a subsequent criminal prosecution, and warned that as a police officer he was subject to a proceeding to discharge him if he failed to provide information relevant to his public responsibilities. The cautionary statements varied slightly, but all, except that given to Mrs. Naglee, included each of the three warnings.<sup>[1]</sup> Mrs. Naglee was <span class="star-pagination">*505</span> not told that she could be removed from her position at the court if she failed to give information pertinent to the discharge of her duties. All of the petitioners consented to give statements, none displayed any significant hesitation, and none suggested that the decision to offer information was motivated by the possibility of discharge.</p>
<p>A second statement was obtained from each of the petitioners in September and December 1962. These statements were not materially different in content or circumstances from the first. The only significant distinction was that the interrogator did not advert even obliquely to any possibility of dismissal. All the petitioners were cautioned that they were entitled to remain silent, and there was no evidence whatever of physical or mental coercion.</p>
<p>All of the petitioners testified at trial, and gave evidence essentially consistent with the statements taken from them. At a preliminary hearing conducted at the Bellmawr trial to determine the voluntariness of the statements, the Bellmawr petitioners offered no evidence beyond proof of the warning given them.</p>
<p>The standards employed by the Court to assess the voluntariness of an accused's statements have reflected a number of values, and thus have emphasized a variety of factual criteria. The criteria employed have included threats of imminent danger, <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span>, physical deprivations, <i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/" aria-description="Citation for case: Reck v. Pate">367 U. S. 433</a></span>, repeated or extended interrogation, <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span>, limits on access to counsel or friends, <i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span>, length and illegality of detention under state law, <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span>, individual weakness or incapacity, <i>Lynumn</i> v. <i>Illinois,</i> <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528</a></span>, and the adequacy of warnings of constitutional rights, <i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737</a></span>. Whatever the criteria employed, the duty of the Court has been "to examine the entire <span class="star-pagination">*506</span> record," and thereby to determine whether the accused's will "was overborne by the sustained pressures upon him." <i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#741" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737, 741, 739</a></span>.</p>
<p>It would be difficult to imagine interrogations to which these criteria of duress were more completely inapplicable, or in which the requirements which have subsequently been imposed by this Court on police questioning were more thoroughly satisfied. Each of the petitioners received a complete and explicit reminder of his constitutional privilege. Three of the petitioners had counsel present; at least a fourth had consulted counsel but freely determined that his presence was unnecessary. These petitioners were not in any fashion "swept from familiar surroundings into police custody, surrounded by antagonistic forces, and subjected to the techniques of persuasion . . . ." <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#461" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 461</a></span>. I think it manifest that, under the standards developed by this Court to assess voluntariness, there is no basis for saying that any of these statements were made involuntarily.</p>
<p></p>
<h2>II.</h2>
<p>The issue remaining is whether the statements were inadmissible because they were "involuntary as a matter of law," in that they were given after a warning that New Jersey policemen may be discharged for failure to provide information pertinent to their public responsibilities. What is really involved on this score, however, is not in truth a question of "voluntariness" at all, but rather whether the condition imposed by the State on the exercise of the privilege against self-incrimination, namely dismissal from office, in this instance serves in itself to render the statements inadmissible. Absent evidence of involuntariness in fact, the admissibility of these statements thus hinges on the validity of the consequence which the State acknowledged might have resulted if the statements had not been given. If the consequence is <span class="star-pagination">*507</span> constitutionally permissible, there can surely be no objection if the State cautions the witness that it may follow if he remains silent. If both the consequence and the warning are constitutionally permissible, a witness is obliged, in order to prevent the use of his statements against him in a criminal prosecution, to prove under the standards established since <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span>, that as a matter of fact the statements were involuntarily made. The central issues here are therefore identical to those presented in <i>Spevack</i> v. <i>Klein, supra</i><i>:</i> whether consequences may properly be permitted to result to a claimant after his invocation of the constitutional privilege, and if so, whether the consequence in question is permissible. For reasons which I have stated in <i>Spevack</i> v. <i>Klein</i><i>,</i> in my view nothing in the logic or purposes of the privilege demands that all consequences which may result from a witness' silence be forbidden merely because that silence is privileged. The validity of a consequence depends both upon the hazards, if any, it presents to the integrity of the privilege and upon the urgency of the public interests it is designed to protect.</p>
<p>It can hardly be denied that New Jersey is permitted by the Constitution to establish reasonable qualifications and standards of conduct for its public employees. Nor can it be said that it is arbitrary or unreasonable for New Jersey to insist that its employees furnish the appropriate authorities with information pertinent to their employment. Cf. <i>Beilan</i> v. <i>Board of Education,</i> <span class="citation" data-id="9421681"><a href="/opinion/105743/beilan-v-board-of-public-ed-school-dist-of-philadelphia/" aria-description="Citation for case: Beilan v. Board of Public Ed., School Dist. of Philadelphia">357 U. S. 399</a></span>; <i>Slochower</i> v. <i>Board of Education,</i> <span class="citation" data-id="9421254"><a href="/opinion/105377/slochower-v-board-of-higher-ed-of-new-york-city/" aria-description="Citation for case: Slochower v. Board of Higher Ed. of New York City">350 U. S. 551</a></span>. Finally, it is surely plain that New Jersey may in particular require its employees to assist in the prevention and detection of unlawful activities by officers of the state government. The urgency of these requirements is the more obvious here, where the conduct in question is that of officials directly entrusted with the administration of justice. The importance for our systems of justice <span class="star-pagination">*508</span> of the integrity of local police forces can scarcely be exaggerated. Thus, it need only be recalled that this Court itself has often intervened in state criminal prosecutions precisely on the ground that this might encourage high standards of police behavior. See, <i>e. g., </i><i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span>; <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona, supra</a></span></i><i>.</i> It must be concluded, therefore, that the sanction at issue here is reasonably calculated to serve the most basic interests of the citizens of New Jersey.</p>
<p>The final question is the hazard, if any, which this sanction presents to the constitutional privilege. The purposes for which, and the circumstances in which, an officer's discharge might be ordered under New Jersey law plainly may vary. It is of course possible that discharge might in a given case be predicated on an imputation of guilt drawn from the use of the privilege, as was thought by this Court to have occurred in <i>Slochower</i> v. <i>Board of Education, supra</i><i>.</i> But from our vantage point, it would be quite improper to assume that New Jersey will employ these procedures for purposes other than to assess in good faith an employee's continued fitness for public employment. This Court, when a state procedure for investigating the loyalty and fitness of public employees might result either in the <i><span class="citation" data-id="9421254"><a href="/opinion/105377/slochower-v-board-of-higher-ed-of-new-york-city/" aria-description="Citation for case: Slochower v. Board of Higher Ed. of New York City">Slochower</a></span></i> situation or in an assessment in good faith of an employee, has until today consistently paused to examine the actual circumstances of each case. <i>Beilan</i> v. <i>Board of Education, supra</i><i>; </i><i>Nelson</i> v. <i>Los Angeles County,</i> <span class="citation" data-id="9421934"><a href="/opinion/106007/nelson-v-county-of-los-angeles/" aria-description="Citation for case: Nelson v. County of Los Angeles">362 U. S. 1</a></span>. I am unable to see any justification for the majority's abandonment of that process; it is well calculated both to protect the essential purposes of the privilege and to guarantee the most generous opportunities for the pursuit of other public values. The majority's broad prohibition, on the other hand, extends the scope of the privilege beyond its essential purposes, and seriously hampers the protection of other important values. Despite the majority's <span class="star-pagination">*509</span> disclaimer, it is quite plain that the logic of its prohibitory rule would in this situation prevent the discharge of these policemen. It would therefore entirely forbid a sanction which presents, at least on its face, no hazard to the purposes of the constitutional privilege, and which may reasonably be expected to serve important public interests. We are not entitled to assume that discharges will be used either to vindicate impermissible inferences of guilt or to penalize privileged silence, but must instead presume that this procedure is only intended and will only be used to establish and enforce standards of conduct for public employees.<sup>[2]</sup> As such, it does not minimize or endanger the petitioners' constitutional privilege against self-incrimination.<sup>[3]</sup></p>
<p><span class="star-pagination">*510</span> I would therefore conclude that the sanction provided by the State is constitutionally permissible. From this, it surely follows that the warning given of the possibility of discharge is constitutionally unobjectionable. Given the constitutionality both of the sanction and of the warning of its application, the petitioners would be constitutionally entitled to exclude the use of their statements as evidence in a criminal prosecution against them only if it is found that the statements were, when given, involuntary in fact. For the reasons stated above, I cannot agree that these statements were involuntary in fact.</p>
<p>I would affirm the judgments of the Supreme Court of New Jersey.</p>
<h2>NOTES</h2>
<p>[1]  "Any person holding or who has held any elective or appointive public office, position or employment (whether state, county or municipal), who refuses to testify upon matters relating to the office, position or employment in any criminal proceeding wherein he is a defendant or is called as a witness on behalf of the prosecution, upon the ground that his answer may tend to incriminate him or compel him to be a witness against himself or refuses to waive immunity when called by a grand jury to testify thereon or who willfully refuses or fails to appear before any court, commission or body of this state which has the right to inquire under oath upon matters relating to the office, position or employment of such person or who, having been sworn, refuses to testify or to answer any material question upon the ground that his answer may tend to incriminate him or compel him to be a witness against himself, shall, if holding elective or public office, position or employment, be removed therefrom or shall thereby forfeit his office, position or employment and any vested or future right of tenure or pension granted to him by any law of this state provided the inquiry relates to a matter which occurred or arose within the preceding five years. Any person so forfeiting his office, position or employment shall not thereafter be eligible for election or appointment to any public office, position or employment in this state." N. J. Rev. Stat. § 2A:81-17.1 (Supp. 1965).</p>
<p>[2]  At the trial the court excused the jury and conducted a hearing to determine whether, <i>inter alia,</i> the statements were voluntary. The State offered witnesses who testified as to the manner in which the statements were taken; the appellants did not testify at that hearing. The court held the statements to be voluntary.</p>
<p>[3]  N. 1, <i>supra.</i></p>
<p>[4]  <i>Stevens</i> v. <i>Marks,</i> <span class="citation" data-id="9423156"><a href="/opinion/107173/stevens-v-marks/#243" aria-description="Citation for case: Stevens v. Marks">383 U. S. 234, 243</a></span>, quoting from <i>Frost Trucking Co.</i> v. <i>Railroad Comm'n,</i> <span class="citation" data-id="9418562"><a href="/opinion/100914/frost-frost-trucking-co-v-railroad-commn-of-cal/#593" aria-description="Citation for case: Frost &amp; Frost Trucking Co. v. Railroad Comm&#x27;n of Cal.">271 U. S. 583, 593</a></span>.</p>
<p>[5]  Cf. Lamm, The 5th Amendment and Its Equivalent in Jewish Law, 17 Decalogue Jour. 1 (Jan.-Feb. 1967):
</p>
<p>"It should be pointed out, at the very outset, that the Halakhah does not distinguish between voluntary and forced confessions, for reasons which will be discussed later. And it is here that one of the basic differences between Constitutional and Talmudic Law arises. According to the Constitution, a man cannot be compelled to testify against himself. The provision against self-incrimination is a privilege of which a citizen may or may not avail himself, as he wishes. The Halakhah, however, does not permit self-incriminating testimony. It is inadmissible, even if voluntarily offered. Confession, in other than a religious context, or financial cases completely free from any traces of criminality, is simply not an instrument of the Law. The issue, then, is not compulsion, but the whole idea of legal confession.</p>
<p>.....</p>
<p>"The Halakhah, then, is obviously concerned with protecting the confessant from his own aberrations which manifest themselves, either as completely fabricated confessions, or as exaggerations of the real facts. . . . While certainly not all, or even most criminal confessions are directly attributable, in whole or part, to the Death Instinct, the Halakhah is sufficiently concerned with the minority of instances, where such is the case, to disqualify all criminal confessions and to discard confession as a legal instrument. Its function is to ensure the total victory of the Life Instinct over its omnipresent antagonist. Such are the conclusions to be drawn from Maimonides' interpretation of the Halakhah's equivalent of the Fifth Amendment.</p>
<p>"In summary, therefore, the Constitutional ruling on self-incrimination concerns only forced confessions, and its restricted character is a result of its historical evolution as a civilized protest against the use of torture in extorting confessions. The Halakhie ruling, however, is much broader and discards confessions in toto, and this because of its psychological insight and its concern for saving man from his own destructive inclinations." <i>Id.,</i> at 10, 12.</p>
<p>[1]  The warning given to Chief Garrity is typical. "I want to advise you that anything you say must be said of your own free will and accord without any threats or promises or coercion, and anything you say may be, of course, used against you or any other person in any subsequent criminal proceedings in the courts of our state.
</p>
<p>"You do have, under our law, as you probably know, a privilege to refuse to make any disclosure which may tend to incriminate you. If you make a disclosure with knowledge of this right or privilege, voluntarily, you thereby waive that right or privilege in relation to any other questions which I might put to you relevant to such disclosure in this investigation.</p>
<p>"This right or privilege which you have is somewhat limited to the extent that you as a police officer under the laws of our state, may be subjected to a proceeding to have you removed from office if you refuse to answer a question put to you under oath pertaining to your office or your function within that office. It doesn't mean, however, you can't exercise the right. You do have the right."</p>
<p>A. "No, I will cooperate."</p>
<p>Q. "Understanding this, are you willing to proceed at this time and answer any questions?"</p>
<p>A. "Yes."</p>
<p>[2]  The legislative history of N. J. Rev. Stat. 2A:81-17.1 provides nothing which clearly indicates the purposes of the statute, beyond what is to be inferred from its face. In any event, the New Jersey Supreme Court noted below that the State would be entitled, even without the statutory authorization, to discharge state employees who declined to provide information relevant to their official responsibilities. There is therefore nothing to which this Court could properly now look to forecast the purposes for which or circumstances in which New Jersey might discharge those who have invoked the constitutional privilege.</p>
<p>[3]  The late Judge Jerome Frank thus once noted, in the course of a spirited defense of the privilege, that it would be entirely permissible to discharge police officers who decline, on grounds of the privilege, to disclose information pertinent to their public responsibilities. Judge Frank quoted the following with approval:
</p>
<p>" `<i>Duty required them to answer. Privilege permitted them to refuse to answer. They chose to exercise the privilege, but the exercise of such privilege was wholly inconsistent with their duty as police officers.</i> They claim that they had a constitutional right to refuse to answer under the circumstances, but . . . <i>they had no constitutional right to remain police officers</i> in the face of their clear violation of the duty imposed upon them.' Christal v. Police Commission of San Francisco." Citing <span class="citation" data-id="1400422"><a href="/opinion/1400422/christal-v-police-commission/" aria-description="Citation for case: Christal v. Police Commission">33 Cal. App. 2d 564</a></span>, <span class="citation" data-id="1400422"><a href="/opinion/1400422/christal-v-police-commission/" aria-description="Citation for case: Christal v. Police Commission">92 P. 2d 416</a></span>. (Emphasis added by Judge Frank.) <i>United States</i> v. <i>Field,</i> <span class="citation" data-id="9443042"><a href="/opinion/228335/united-states-v-field/#106" aria-description="Citation for case: United States v. Field">193 F. 2d 92, 106</a></span> (separate opinion).</p>

</div>
```

---
