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

## GROUP: content/cases/Illinois v. Caballes.md  (`case`, 6 assertions)

### content_page

```
---
title: "Illinois v. Caballes"
type: case
citation: "543 U.S. 405 (2005)"
parallel_cite: "125 S. Ct. 834; 160 L. Ed. 2d 842"
neutral_cite: 2005 U.S. LEXIS 769
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2005
date_decided: 2005-01-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2005-01-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Illinois v. Caballes
  varies_by_point: false
  scope_note: "Good law. Rodriguez v. United States (2015) applied the no-prolongation principle (a stop may not be extended even briefly for a dog sniff absent reasonable suspicion). Florida v. Jardines (2013) held a dog sniff at a home's curtilage is a search — a context boundary, not an overruling of the vehicle holding."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/137742/illinois-v-caballes/"
  cluster_id: 137742
  opinion_id: 137742
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Key — Anchor"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Place]]", "[[Rodriguez v. United States]]", "[[Florida v. Jardines]]", "[[Kyllo v. United States]]", "[[Florida v. Harris]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "dog-sniff", "traffic-stop", "contraband"]
holding: "A dog sniff during a lawful traffic stop that does not prolong the stop needs no independent suspicion, because it reveals only contraband and does not implicate legitimate privacy interests."
lake:
  record_id: Illinois v. Caballes
  status: verified
  projected_at: 2026-07-09
---

# Illinois v. Caballes

*543 U.S. 405 (2005)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An Illinois trooper stopped Caballes for speeding. While the trooper wrote a warning ticket, a second trooper arrived and walked a drug-detection dog around the car. The dog alerted at the trunk; a search revealed marijuana. The entire stop lasted under ten minutes and was not prolonged by the sniff. Caballes argued the dog sniff converted a routine traffic stop into an unjustified drug investigation.

## Issue
Whether the Fourth Amendment requires reasonable, articulable suspicion to justify a dog sniff of a vehicle's exterior conducted during an otherwise lawful traffic stop.

## Rule
A lawful stop must not be prolonged for the sniff: "A seizure that is justified solely by the interest in issuing a warning ticket to the driver can become unlawful if it is prolonged beyond the time reasonably required to complete that mission." — 543 U.S. at 407. ^pin-407

But a non-prolonging sniff invades no protected interest: "the use of a well-trained narcotics-detection dog — one that 'does not expose noncontraband items that otherwise would remain hidden from public view,' *Place*, 462 U.S., at 707 — during a lawful traffic stop, generally does not implicate legitimate privacy interests." — *Id.* at 409. ^pin-409

The holding: "A dog sniff conducted during a concededly lawful traffic stop that reveals no information other than the location of a substance that no individual has any right to possess does not violate the Fourth Amendment." — [*Id.* at 410](https://www.courtlistener.com/opinion/137742/illinois-v-caballes/#:~:text=A%20dog%20sniff%20conducted%20during). ^pin-410

## Application
The traffic stop was lawful at its inception and was not extended by the dog sniff, which occurred while the warning ticket was being written. Because a reliable narcotics dog discloses only the presence or absence of contraband — in which no person has a legitimate privacy interest — the sniff of the car's exterior implicated no constitutionally cognizable privacy interest and required no independent reasonable suspicion. The alert then supplied probable cause for the trunk search.

## Conclusion
A dog sniff during an unprolonged, lawful traffic stop is not a Fourth Amendment search and needs no separate suspicion; the marijuana was admissible. *Caballes* anchors the vehicle dog-sniff rule while preserving the limit that the stop may not be extended to conduct it.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Applies the dog-sniff reasoning of [[United States v. Place]] and contrasts the home-interior technology case [[Kyllo v. United States]]. The no-prolongation limit is enforced by [[Rodriguez v. United States]]; the home-[[Curtilage|curtilage]] boundary is set by [[Florida v. Jardines]]; dog-reliability/probable-cause questions are addressed in [[Florida v. Harris]].

## Appears on
- [[Traffic Stops]] — *Key — Anchor*
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*

## Sources
- *Illinois v. Caballes*, 543 U.S. 405 (2005) — https://www.courtlistener.com/opinion/137742/illinois-v-caballes/ — pinpoints: 407, 409, 410.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8ba4c6a58d04135f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "543 U.S. 405 (2005)", "court": "U.S. Supreme Court", "neutral_cite": "2005 U.S. LEXIS 769", "official_citation_present": true, "parallel_cite": "125 S. Ct. 834; 160 L. Ed. 2d 842", "title": "Illinois v. Caballes", "year": "2005"}}
{"assertion_id": "42a7cc181f28130f", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Related (cross-doctrine)", "title": "Illinois v. Caballes"}}
{"assertion_id": "5173e6e42fcc34c4", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Key — Anchor", "title": "Illinois v. Caballes"}}
{"assertion_id": "760e1fc068669c98", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A dog sniff during a lawful traffic stop that does not prolong the stop needs no independent suspicion, because it reveals only contraband and does not implicate legitimate privacy interests.", "title": "Illinois v. Caballes"}}
{"assertion_id": "ae5f68644005b14d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2005-01-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Illinois v. Caballes", "field_i_validity": "good_law", "scope_note": "Good law. Rodriguez v. United States (2015) applied the no-prolongation principle (a stop may not be extended even briefly for a dog sniff absent reasonable suspicion). Florida v. Jardines (2013) held a dog sniff at a home's curtilage is a search — a context boundary, not an overruling of the vehicle holding.", "title": "Illinois v. Caballes", "varies_by_point": "false"}}
{"assertion_id": "ec750f0421457723", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Illinois v. Caballes"}}
```

### lake record — Illinois v. Caballes

```json
{
  "schema_version": "s2.v1",
  "record_id": "Illinois v. Caballes",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Illinois v. Caballes",
    "case_name_short": "Caballes",
    "case_name_full": "Illinois v. Caballes",
    "input_case_name": "Illinois v. Caballes",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2005-01-24",
    "year": 2005,
    "docket": null,
    "cluster_id": 137742,
    "lead_opinion_id": 137742,
    "sibling_ids": [
      137742,
      9434728,
      9434729,
      9434730
    ],
    "absolute_url": "/opinion/137742/illinois-v-caballes/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "543 U.S. 405",
      "volume": "543",
      "reporter": "U.S.",
      "page": "405",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "125 S. Ct. 834",
        "volume": "125",
        "reporter": "S. Ct.",
        "page": "834",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "160 L. Ed. 2d 842",
        "volume": "160",
        "reporter": "L. Ed. 2d",
        "page": "842",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2005 U.S. LEXIS 769",
        "volume": "2005",
        "reporter": "U.S. LEXIS",
        "page": "769",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "543 U.S. 405",
        "volume": "543",
        "reporter": "U.S.",
        "page": "405",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "125 S. Ct. 834",
        "volume": "125",
        "reporter": "S. Ct.",
        "page": "834",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "160 L. Ed. 2d 842",
        "volume": "160",
        "reporter": "L. Ed. 2d",
        "page": "842",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2005 U.S. LEXIS 769",
        "volume": "2005",
        "reporter": "U.S. LEXIS",
        "page": "769",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "543 U.S. 405",
    "official_selection": {
      "court_class": "scotus",
      "selected": "543 U.S. 405",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-407",
      "page": null,
      "quote": "--- # Illinois v. Caballes *543 U.S. 405 (2005)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An Illinois trooper stopped Caballes for speeding. While the trooper wrote a warning ticket, a second trooper arrived and walked a drug-detection dog around the car. The dog alerted at the trunk; a search revealed marijuana. The entire stop lasted under ten minutes and was not prolonged by the sniff. Caballes argued the dog sniff converted a routine traffic stop into an unjustified drug investigation. ## Issue Whether the Fourth Amendment requires reasonable, articulable suspicion to justify a dog sniff of a vehicle's exterior conducted during an otherwise lawful traffic stop. ## Rule A lawful stop must not be prolonged for the sniff:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-409",
      "page": null,
      "quote": "the use of a well-trained narcotics-detection dog \u2014 one that 'does not expose noncontraband items that otherwise would remain hidden from public view,' *Place*, 462 U.S., at 707 \u2014 during a lawful traffic stop, generally does not implicate legitimate privacy interests.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-410",
      "page": null,
      "quote": "A dog sniff conducted during a concededly lawful traffic stop that reveals no information other than the location of a substance that no individual has any right to possess does not violate the Fourth Amendment.",
      "star_marker": "410",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 11448,
      "fragment": "#:~:text=A%20dog%20sniff%20conducted%20during",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2005-01-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Illinois v. Caballes",
    "varies_by_point": false,
    "scope_note": "Good law. Rodriguez v. United States (2015) applied the no-prolongation principle (a stop may not be extended even briefly for a dog sniff absent reasonable suspicion). Florida v. Jardines (2013) held a dog sniff at a home's curtilage is a search \u2014 a context boundary, not an overruling of the vehicle holding.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Marlon Juan Lall v. the State of Texas",
          "cluster_id": 10046849,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rodriguez v. United States",
          "cluster_id": 2795278,
          "cite": [
            "575 U.S. 348",
            "135 S. Ct. 1609",
            "191 L. Ed. 2d 492",
            "2015 U.S. LEXIS 2807",
            "83 U.S.L.W. 4241",
            "25 Fla. L. Weekly Fed. S 191"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jardines",
          "cluster_id": 856347,
          "cite": [
            "185 L. Ed. 2d 495",
            "133 S. Ct. 1409",
            "569 U.S. 1",
            "2013 U.S. LEXIS 2542",
            "24 Fla. L. Weekly Fed. S 117",
            "81 U.S.L.W. 4209",
            "2013 WL 1196577"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. United States",
          "cluster_id": 803270,
          "cite": [
            "183 L. Ed. 2d 351",
            "132 S. Ct. 2492",
            "567 U.S. 387",
            "2012 U.S. LEXIS 4872",
            "80 U.S.L.W. 4539",
            "23 Fla. L. Weekly Fed. S 437",
            "2012 WL 2368661",
            "95 Empl. Prac. Dec. (CCH) 44,539",
            "115 Fair Empl. Prac. Cas. (BNA) 353"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Muehler v. Mena",
          "cluster_id": 142878,
          "cite": [
            "161 L. Ed. 2d 299",
            "125 S. Ct. 1465",
            "544 U.S. 93",
            "2005 U.S. LEXIS 2755"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Chavez-Barragan",
          "cluster_id": 4260741,
          "cite": [
            "2016 CO 66",
            "379 P.3d 330",
            "2016 WL 5375502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Erickson Meko Campbell",
          "cluster_id": 6357475,
          "cite": [
            "26 F.4th 860"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Henderson",
          "cluster_id": 1057155,
          "cite": [
            "2013 IL 114040"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Branch",
          "cluster_id": 1026476,
          "cite": [
            "537 F.3d 328",
            "2008 U.S. App. LEXIS 17710",
            "2008 WL 3854500"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Felders v. Malcom",
          "cluster_id": 2679716,
          "cite": [
            "755 F.3d 870",
            "2014 WL 2782368",
            "2014 U.S. App. LEXIS 11627"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kevin M. Clark v. State of Indiana",
          "cluster_id": 1041668,
          "cite": [
            "994 N.E.2d 252",
            "2013 WL 5228498",
            "2013 Ind. LEXIS 700"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Caballes",
          "cluster_id": 2192166,
          "cite": [
            "851 N.E.2d 26",
            "221 Ill. 2d 282",
            "303 Ill. Dec. 128",
            "2006 Ill. LEXIS 625"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Elias",
          "cluster_id": 2539936,
          "cite": [
            "339 S.W.3d 667",
            "2011 Tex. Crim. App. LEXIS 448",
            "2011 WL 1267248"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Randall Lee Pals",
          "cluster_id": 4472392,
          "cite": [
            "805 N.W.2d 767",
            "2011 Iowa Sup. LEXIS 87"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
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
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bew",
          "cluster_id": 2231907,
          "cite": [
            "886 N.E.2d 1002",
            "228 Ill. 2d 122",
            "319 Ill. Dec. 878",
            "2008 Ill. LEXIS 291"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Maynard",
          "cluster_id": 152441,
          "cite": [
            "615 F.3d 544",
            "392 U.S. App. D.C. 291",
            "2010 U.S. App. LEXIS 16417",
            "2010 WL 3063788"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lerma v. State",
          "cluster_id": 6241263,
          "cite": [
            "543 S.W.3d 184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hernandez v. United States",
          "cluster_id": 4661436,
          "cite": [
            "939 F.3d 191"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cosby",
          "cluster_id": 2105166,
          "cite": [
            "898 N.E.2d 603",
            "231 Ill. 2d 262",
            "325 Ill. Dec. 556",
            "2008 Ill. LEXIS 890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thompson",
          "cluster_id": 2623710,
          "cite": [
            "166 P.3d 1015",
            "284 Kan. 763",
            "2007 Kan. LEXIS 487"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Leyva",
          "cluster_id": 891705,
          "cite": [
            "2011 NMSC 9",
            "250 P.3d 861",
            "149 N.M. 435",
            "2011 NMSC 009"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Farrior",
          "cluster_id": 1026364,
          "cite": [
            "535 F.3d 210",
            "2008 U.S. App. LEXIS 16575",
            "2008 WL 2971779"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William Windham v. Harris County, Texas",
          "cluster_id": 4442638,
          "cite": [
            "875 F.3d 229"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Weaver",
          "cluster_id": 2546485,
          "cite": [
            "349 S.W.3d 521",
            "2011 Tex. Crim. App. LEXIS 1320",
            "2011 WL 4715178"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(137742 OR 9434728 OR 9434729 OR 9434730) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTkzOTkzNjAwMDAwJnM9NDgzMjU4NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28137742+OR+9434728+OR+9434729+OR+9434730%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      },
      "lane2_top_cited": {
        "query": "cites:(137742 OR 9434728 OR 9434729 OR 9434730)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjImcz0yNjMxMTA5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28137742+OR+9434728+OR+9434729+OR+9434730%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(137742 OR 9434728 OR 9434729 OR 9434730)",
        "reviewed": 121,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 121,
        "triage_read": 1,
        "triage_snippet_classified": 120
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(137742 OR 9434728 OR 9434729 OR 9434730)",
    "indexed_citing_opinions": 1117,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 137742,
        "count": 818,
        "count_source": "search"
      },
      {
        "opinion_id": 9434728,
        "count": 312,
        "count_source": "search"
      },
      {
        "opinion_id": 9434729,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434730,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2012,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/illinois-v-caballes.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyOTYxNjcmcz0xMDM3NTI0OSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28137742+OR+9434728+OR+9434729+OR+9434730%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 137742,
        "cited_id": 76430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 111667,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 118250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 118354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 136990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 155490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 164282,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 485654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 671474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 749428,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 775355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 1882050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 2038990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 2106553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 2207633,
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
    "date_created": "2026-07-05T07:51:31Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:51:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:51:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:54:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:51:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Illinois v. Caballes

```
<div>
<center><b><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">543 U.S. 405</a></span> (2005)</b></center>
<center><h1>ILLINOIS<br>
v.<br>
CABALLES.</h1></center>
<center>No. 03-923.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 10, 2004.</center>
<center>Decided January 24, 2005.</center>
CERTIORARI TO THE SUPREME COURT OF ILLINOIS.
<p>STEVENS, J., delivered the opinion of the Court, in which O'CONNOR, SCALIA, KENNEDY, THOMAS, and BREYER, JJ., joined. SOUTER, J., filed a dissenting opinion, <i>post,</i> p. 410. GINSBURG, J., filed a dissenting opinion, in which SOUTER, J., joined, <i>post,</i> p. 417. REHNQUIST, C. J., took no part in the decision of the case.</p>
<p><i>Lisa Madigan,</i> Attorney General of Illinois, argued the cause for petitioner. With her on the briefs were <i>Gary Feinerman,</i> Solicitor General, and <i>Linda D. Woloshin</i> and <i>Mary Fleming,</i> Assistant Attorneys General.</p>
<p><i>Assistant Attorney General Wray</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were former <i>Solicitor General Olson, Deputy Solicitor General Dreeben, James A. Feldman,</i> and <i>John A. Drennan.</i></p>
<p><span class="star-pagination">*406</span> <i>Ralph E. Meczyk</i> argued the cause for respondent. With him on the brief was <i>Lawrence H. Hyman.</i><sup>[*]</sup></p>
<p>JUSTICE STEVENS delivered the opinion of the Court.</p>
<p>Illinois State Trooper Daniel Gillette stopped respondent for speeding on an interstate highway. When Gillette radioed the police dispatcher to report the stop, a second trooper, Craig Graham, a member of the Illinois State Police Drug Interdiction Team, overheard the transmission and immediately headed for the scene with his narcotics-detection dog. When they arrived, respondent's car was on the shoulder of the road and respondent was in Gillette's vehicle. While Gillette was in the process of writing a warning ticket, Graham walked his dog around respondent's car. The dog alerted at the trunk. Based on that alert, the officers searched the trunk, found marijuana, and arrested respondent. The entire incident lasted less than 10 minutes.</p>
<p><span class="star-pagination">*407</span> Respondent was convicted of a narcotics offense and sentenced to 12 years' imprisonment and a $256,136 fine. The trial judge denied his motion to suppress the seized evidence and to quash his arrest. He held that the officers had not unnecessarily prolonged the stop and that the dog alert was sufficiently reliable to provide probable cause to conduct the search. Although the Appellate Court affirmed, the Illinois Supreme Court reversed, concluding that because the canine sniff was performed without any "`specific and articulable facts'" to suggest drug activity, the use of the dog "unjustifiably enlarg[ed] the scope of a routine traffic stop into a drug investigation." <span class="citation multiple-matches"><a href="/c/Ill.%202d/207/504/">207 Ill. 2d 504</a></span>, 510, <span class="citation multiple-matches"><a href="/c/N.%20E.%202d/802/202/">802 N. E. 2d 202</a></span>, 205 (2003).</p>
<p>The question on which we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./541/972/">541 U. S. 972</a></span> (2004), is narrow: "Whether the Fourth Amendment requires reasonable, articulable suspicion to justify using a drug-detection dog to sniff a vehicle during a legitimate traffic stop." Pet. for Cert. i. Thus, we proceed on the assumption that the officer conducting the dog sniff had no information about respondent except that he had been stopped for speeding; accordingly, we have omitted any reference to facts about respondent that might have triggered a modicum of suspicion.</p>
<p>Here, the initial seizure of respondent when he was stopped on the highway was based on probable cause and was concededly lawful. It is nevertheless clear that a seizure that is lawful at its inception can violate the Fourth Amendment if its manner of execution unreasonably infringes interests protected by the Constitution. <i>United States</i> v. <i>Jacobsen,</i> <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#124" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 124</a></span> (1984). A seizure that is justified solely by the interest in issuing a warning ticket to the driver can become unlawful if it is prolonged beyond the time reasonably required to complete that mission. In an earlier case involving a dog sniff that occurred during an unreasonably prolonged traffic stop, the Illinois Supreme Court held that use of the dog and the subsequent discovery <span class="star-pagination">*408</span> of contraband were the product of an unconstitutional seizure. <i>People</i> v. <i>Cox,</i> <span class="citation" data-id="9526758"><a href="/opinion/2038990/people-v-cox/" aria-description="Citation for case: People v. Cox">202 Ill. 2d 462</a></span>, <span class="citation" data-id="9526758"><a href="/opinion/2038990/people-v-cox/" aria-description="Citation for case: People v. Cox">782 N. E. 2d 275</a></span> (2002). We may assume that a similar result would be warranted in this case if the dog sniff had been conducted while respondent was being unlawfully detained.</p>
<p>In the state-court proceedings, however, the judges carefully reviewed the details of Officer Gillette's conversations with respondent and the precise timing of his radio transmissions to the dispatcher to determine whether he had improperly extended the duration of the stop to enable the dog sniff to occur. We have not recounted those details because we accept the state court's conclusion that the duration of the stop in this case was entirely justified by the traffic offense and the ordinary inquiries incident to such a stop.</p>
<p>Despite this conclusion, the Illinois Supreme Court held that the initially lawful traffic stop became an unlawful seizure solely as a result of the canine sniff that occurred outside respondent's stopped car. That is, the court characterized the dog sniff as the cause rather than the consequence of a constitutional violation. In its view, the use of the dog converted the citizen-police encounter from a lawful traffic stop into a drug investigation, and because the shift in purpose was not supported by any reasonable suspicion that respondent possessed narcotics, it was unlawful. In our view, conducting a dog sniff would not change the character of a traffic stop that is lawful at its inception and otherwise executed in a reasonable manner, unless the dog sniff itself infringed respondent's constitutionally protected interest in privacy. Our cases hold that it did not.</p>
<p>Official conduct that does not "compromise any legitimate interest in privacy" is not a search subject to the Fourth Amendment. <i>Jacobsen,</i> <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#123" aria-description="Citation for case: United States v. Jacobsen">466 U. S., at 123</a></span>. We have held that any interest in possessing contraband cannot be deemed "legitimate," and thus, governmental conduct that <i>only</i> reveals the possession of contraband "compromises no legitimate privacy interest." <i><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Ibid.</a></span></i> This is because the expectation <span class="star-pagination">*409</span> "that certain facts will not come to the attention of the authorities" is not the same as an interest in "privacy that society is prepared to consider reasonable." <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#122" aria-description="Citation for case: United States v. Jacobsen"><i>Id.,</i> at 122</a></span> (punctuation omitted). In <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983), we treated a canine sniff by a well-trained narcotics-detection dog as <i>"sui generis"</i> because it "discloses only the presence or absence of narcotics, a contraband item." <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place"><i>Id.,</i> at 707</a></span>; see also <i>Indianapolis</i> v. <i>Edmond,</i> <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#40" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S. 32, 40</a></span> (2000). Respondent likewise concedes that "drug sniffs are designed, and if properly conducted are generally likely, to reveal only the presence of contraband." Brief for Respondent 17. Although respondent argues that the error rates, particularly the existence of false positives, call into question the premise that drug-detection dogs alert only to contraband, the record contains no evidence or findings that support his argument. Moreover, respondent does not suggest that an erroneous alert, in and of itself, reveals any legitimate private information, and, in this case, the trial judge found that the dog sniff was sufficiently reliable to establish probable cause to conduct a full-blown search of the trunk.</p>
<p>Accordingly, the use of a well-trained narcotics-detection dogone that "does not expose noncontraband items that otherwise would remain hidden from public view," <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> 462 U. S., at 707during a lawful traffic stop, generally does not implicate legitimate privacy interests. In this case, the dog sniff was performed on the exterior of respondent's car while he was lawfully seized for a traffic violation. Any intrusion on respondent's privacy expectations does not rise to the level of a constitutionally cognizable infringement.</p>
<p>This conclusion is entirely consistent with our recent decision that the use of a thermal-imaging device to detect the growth of marijuana in a home constituted an unlawful search. <i>Kyllo</i> v. <i>United States,</i> <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">533 U. S. 27</a></span> (2001). Critical to that decision was the fact that the device was capable of detecting lawful activityin that case, intimate details in a <span class="star-pagination">*410</span> home, such as "at what hour each night the lady of the house takes her daily sauna and bath." <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#38" aria-description="Citation for case: Kyllo v. United States"><i>Id.,</i> at 38</a></span>. The legitimate expectation that information about perfectly lawful activity will remain private is categorically distinguishable from respondent's hopes or expectations concerning the nondetection of contraband in the trunk of his car. A dog sniff conducted during a concededly lawful traffic stop that reveals no information other than the location of a substance that no individual has any right to possess does not violate the Fourth Amendment.</p>
<p>The judgment of the Illinois Supreme Court is vacated, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>THE CHIEF JUSTICE took no part in the decision of this case.</p>
<p>JUSTICE SOUTER, dissenting.</p>
<p>I would hold that using the dog for the purposes of determining the presence of marijuana in the car's trunk was a search unauthorized as an incident of the speeding stop and unjustified on any other ground. I would accordingly affirm the judgment of the Supreme Court of Illinois, and I respectfully dissent.</p>
<p>In <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983), we categorized the sniff of the narcotics-seeking dog as <i>"sui generis"</i> under the Fourth Amendment and held it was not a search. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place"><i>Id.,</i> at 707</a></span>. The classification rests not only upon the limited nature of the intrusion, but on a further premise that experience has shown to be untenable, the assumption that trained sniffing dogs do not err. What we have learned about the fallibility of dogs in the years since <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> was decided would itself be reason to call for reconsidering <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i>'s decision against treating the intentional use of a trained dog as a search. The portent of this very case, however, adds insistence <span class="star-pagination">*411</span> to the call, for an uncritical adherence to <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> would render the Fourth Amendment indifferent to suspicionless and indiscriminate sweeps of cars in parking garages and pedestrians on sidewalks; if a sniff is not preceded by a seizure subject to Fourth Amendment notice, it escapes Fourth Amendment review entirely unless it is treated as a search. We should not wait for these developments to occur before rethinking <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i>'s analysis, which invites such untoward consequences.<sup>[1]</sup></p>
<p>At the heart both of <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> and the Court's opinion today is the proposition that sniffs by a trained dog are <i>sui generis</i> because a reaction by the dog in going alert is a response to nothing but the presence of contraband.<sup>[2]</sup> See <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">ibid.</a></span></i> ("[T]he sniff discloses only the presence or absence of narcotics, a contraband item"); <i>ante,</i> at 409 (assuming that "a canine sniff by a well-trained narcotics-detection dog" will only reveal "`the presence or absence of narcotics, a contraband item'" (quoting <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place"><i>Place, supra,</i> at 707</a></span>)). Hence, the argument goes, because the sniff can only reveal the presence of items devoid of any legal use, the sniff "does not implicate legitimate privacy interests" and is not to be treated as a search. <i>Ante,</i> at 409.</p>
<p>The infallible dog, however, is a creature of legal fiction. Although the Supreme Court of Illinois did not get into the sniffing averages of drug dogs, their supposed infallibility is belied by judicial opinions describing well-trained animals sniffing and alerting with less than perfect accuracy, whether <span class="star-pagination">*412</span> owing to errors by their handlers, the limitations of the dogs themselves, or even the pervasive contamination of currency by cocaine. See, <i>e. g., </i><i>United States</i> v. <i>Kennedy,</i> <span class="citation" data-id="749428"><a href="/opinion/749428/united-states-v-keiran-george-kennedy/#1378" aria-description="Citation for case: United States v. Keiran George Kennedy">131 F. 3d 1371, 1378</a></span> (CA10 1997) (describing a dog that had a 71% accuracy rate); <i>United States</i> v. <i>Scarborough,</i> <span class="citation" data-id="155490"><a href="/opinion/155490/united-states-v-scarborough/#1378" aria-description="Citation for case: United States v. Scarborough">128 F. 3d 1373, 1378, n. 3</a></span> (CA10 1997) (describing a dog that erroneously alerted 4 times out of 19 while working for the postal service and 8% of the time over its entire career); <i>United States</i> v. <i>Limares,</i> <span class="citation" data-id="775355"><a href="/opinion/775355/united-states-v-luis-c-limares/#797" aria-description="Citation for case: United States v. Luis C. Limares">269 F. 3d 794, 797</a></span> (CA7 2001) (accepting as reliable a dog that gave false positives between 7% and 38% of the time); <i>Laime</i> v. <i>State,</i> <span class="citation" data-id="9691597"><a href="/opinion/1882050/laime-v-state/#159" aria-description="Citation for case: Laime v. State">347 Ark. 142, 159</a></span>, <span class="citation" data-id="9691597"><a href="/opinion/1882050/laime-v-state/#476" aria-description="Citation for case: Laime v. State">60 S. W. 3d 464, 476</a></span> (2001) (speaking of a dog that made between 10 and 50 errors); <i>United States</i> v. <i>$242,484.00,</i> <span class="citation" data-id="8408430"><a href="/opinion/8437934/united-states-v-24248400/#511" aria-description="Citation for case: United States v. $242,484.00">351 F. 3d 499, 511</a></span> (CA11 2003) (noting that because as much as 80% of all currency in circulation contains drug residue, a dog alert "is of little value"), vacated on other grounds by rehearing en banc, <span class="citation" data-id="76430"><a href="/opinion/76430/united-states-v-24240400/" aria-description="Citation for case: United States v. $242,404.00">357 F. 3d 1225</a></span> (CA11 2004); <i>United States</i> v. <i>Carr,</i> <span class="citation" data-id="9486834"><a href="/opinion/671474/united-states-v-robert-joseph-carr-jr-in-no-93-1376-united-states-of/#1214" aria-description="Citation for case: United States v. Robert Joseph Carr, Jr., in No. 93-1376....">25 F. 3d 1194, 1214-1217</a></span> (CA3 1994) (Becker, J., concurring in part and dissenting in part) ("[A] substantial portion of United States currency ... is tainted with sufficient traces of controlled substances to cause a trained canine to alert to their presence"). Indeed, a study cited by Illinois in this case for the proposition that dog sniffs are "generally reliable" shows that dogs in artificial testing situations return false positives anywhere from 12.5% to 60% of the time, depending on the length of the search. See Reply Brief for Petitioner 13; Federal Aviation Admin., K. Garner et al., Duty Cycle of the Detector Dog: A Baseline Study 12 (Apr. 2001) (prepared by the Auburn U. Inst. for Biological Detection Systems). In practical terms, the evidence is clear that the dog that alerts hundreds of times will be wrong dozens of times.</p>
<p>Once the dog's fallibility is recognized, however, that ends the justification claimed in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> for treating the sniff as <i>sui generis</i> under the Fourth Amendment: the sniff alert does not necessarily signal hidden contraband, and opening the container or enclosed space whose emanations the dog has <span class="star-pagination">*413</span> sensed will not necessarily reveal contraband or any other evidence of crime. This is not, of course, to deny that a dog's reaction may provide reasonable suspicion, or probable cause, to search the container or enclosure; the Fourth Amendment does not demand certainty of success to justify a search for evidence or contraband. The point is simply that the sniff and alert cannot claim the certainty that <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> assumed, both in treating the deliberate use of sniffing dogs as <i>sui generis</i> and then taking that characterization as a reason to say they are not searches subject to Fourth Amendment scrutiny. And when that aura of uniqueness disappears, there is no basis in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i>'s reasoning, and no good reason otherwise, to ignore the actual function that dog sniffs perform. They are conducted to obtain information about the contents of private spaces beyond anything that human senses could perceive, even when conventionally enhanced. The information is not provided by independent third parties beyond the reach of constitutional limitations, but gathered by the government's own officers in order to justify searches of the traditional sort, which may or may not reveal evidence of crime but will disclose anything meant to be kept private in the area searched. Thus in practice the government's use of a trained narcotics dog functions as a limited search to reveal undisclosed facts about private enclosures, to be used to justify a further and complete search of the enclosed area. And given the fallibility of the dog, the sniff is the first step in a process that may disclose "intimate details" without revealing contraband, just as a thermal-imaging device might do, as described in <i>Kyllo</i> v. <i>United States,</i> <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">533 U. S. 27</a></span> (2001).<sup>[3]</sup></p>
<p><span class="star-pagination">*414</span> It makes sense, then, to treat a sniff as the search that it amounts to in practice, and to rely on the body of our Fourth Amendment cases, including <i><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">Kyllo</a></span>,</i> in deciding whether such a search is reasonable. As a general proposition, using a dog to sniff for drugs is subject to the rule that the object of enforcing criminal laws does not, without more, justify suspicionless Fourth Amendment intrusions. See <i>Indianapolis</i> v. <i>Edmond,</i> <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#41" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S. 32, 41-42</a></span> (2000). Since the police claim to have had no particular suspicion that Caballes was violating any drug law,<sup>[4]</sup> this sniff search must stand or fall on its being ancillary to the traffic stop that led up to it. It is true that the police had probable cause to stop the car for an offense committed in the officer's presence, which Caballes concedes could have justified his arrest. See Brief for Respondent 31. There is no occasion to consider authority incident to arrest, however, see <i>Knowles</i> v. <i>Iowa,</i> <span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/" aria-description="Citation for case: Knowles v. Iowa">525 U. S. 113</a></span> (1998), for the police did nothing more than detain Caballes long enough to check his record and write a ticket. As a consequence, the reasonableness of the search must be assessed in relation to the actual delay the police chose to impose, and as JUSTICE GINSBURG points out in her opinion, <i>post,</i> at 419-420, the Fourth Amendment consequences of stopping for a traffic citation are settled law.</p>
<p><span class="star-pagination">*415</span> In <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#439" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 439-440</a></span> (1984), followed in <span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/#117" aria-description="Citation for case: Knowles v. Iowa"><i>Knowles, supra,</i> at 117</a></span>, we held that the analogue of the common traffic stop was the limited detention for investigation authorized by <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). While <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> authorized a restricted incidental search for weapons when reasonable suspicion warrants such a safety measure, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#25" aria-description="Citation for case: Terry v. Ohio"><i>id.,</i> at 25-26</a></span>, the Court took care to keep a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop from automatically becoming a foot in the door for all investigatory purposes; the permissible intrusion was bounded by the justification for the detention, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio"><i>id.,</i> at 29-30</a></span>.<sup>[5]</sup> Although facts disclosed by enquiry within this limit might give grounds to go further, the government could not otherwise take advantage of a suspect's immobility to search for evidence unrelated to the reason for the detention. That has to be the rule unless <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> is going to become an open sesame for general searches, and that rule requires holding that the police do not have reasonable grounds to conduct sniff searches for drugs simply because they have stopped someone to receive a ticket for a highway offense. Since the police had no indication of illegal activity beyond the speed of the car in this case, the sniff search should be held unreasonable under the Fourth Amendment and its fruits should be suppressed.</p>
<p>Nothing in the case relied upon by the Court, <i>United States</i> v. <i>Jacobsen,</i> <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109</a></span> (1984), unsettled the limit of reasonable enquiry adopted in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</i> In <i><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Jacobsen</a></span>,</i> the Court found that no Fourth Amendment search occurred when federal agents analyzed powder they had already lawfully obtained. The Court noted that because the test could only reveal whether the powder was cocaine, the owner had no legitimate privacy interest at stake. <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#123" aria-description="Citation for case: United States v. Jacobsen">466 U. S., at 123</a></span>. <span class="star-pagination">*416</span> As already explained, however, the use of a sniffing dog in cases like this is significantly different and properly treated as a search that does indeed implicate Fourth Amendment protection.</p>
<p>In <i><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Jacobsen</a></span>,</i> once the powder was analyzed, that was effectively the end of the matter: either the powder was cocaine, a fact the owner had no legitimate interest in concealing, or it was not cocaine, in which case the test revealed nothing about the powder or anything else that was not already legitimately obvious to the police. But in the case of the dog sniff, the dog does not smell the disclosed contraband; it smells a closed container. An affirmative reaction therefore does not identify a substance the police already legitimately possess, but informs the police instead merely of a reasonable chance of finding contraband they have yet to put their hands on. The police will then open the container and discover whatever lies within, be it marijuana or the owner's private papers. Thus, while <i><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Jacobsen</a></span></i> could rely on the assumption that the enquiry in question would either show with certainty that a known substance was contraband or would reveal nothing more, both the certainty and the limit on disclosure that may follow are missing when the dog sniffs the car.<sup>[6]</sup></p>
<p><span class="star-pagination">*417</span> The Court today does not go so far as to say explicitly that sniff searches by dogs trained to sense contraband always get a free pass under the Fourth Amendment, since it reserves judgment on the constitutional significance of sniffs assumed to be more intrusive than a dog's walk around a stopped car, <i>ante,</i> at 409. For this reason, I do not take the Court's reliance on <i><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Jacobsen</a></span></i> as actually signaling recognition of a broad authority to conduct suspicionless sniffs for drugs in any parked car, about which JUSTICE GINSBURG is rightly concerned, <i>post,</i> at 422, or on the person of any pedestrian minding his own business on a sidewalk. But the Court's stated reasoning provides no apparent stopping point short of such excesses. For the sake of providing a workable framework to analyze cases on facts like these, which are certain to come along, I would treat the dog sniff as the familiar search it is in fact, subject to scrutiny under the Fourth Amendment.<sup>[7]</sup></p>
<p>JUSTICE GINSBURG, with whom JUSTICE SOUTER joins, dissenting.</p>
<p>Illinois State Police Trooper Daniel Gillette stopped Roy Caballes for driving 71 miles per hour in a zone with a posted <span class="star-pagination">*418</span> speed limit of 65 miles per hour. Trooper Craig Graham of the Drug Interdiction Team heard on the radio that Trooper Gillette was making a traffic stop. Although Gillette requested no aid, Graham decided to come to the scene to conduct a dog sniff. Gillette informed Caballes that he was speeding and asked for the usual documents  driver's license, car registration, and proof of insurance. Caballes promptly provided the requested documents but refused to consent to a search of his vehicle. After calling his dispatcher to check on the validity of Caballes' license and for outstanding warrants, Gillette returned to his vehicle to write Caballes a warning ticket. Interrupted by a radio call on an unrelated matter, Gillette was still writing the ticket when Trooper Graham arrived with his drug-detection dog. Graham walked the dog around the car, the dog alerted at Caballes' trunk, and, after opening the trunk, the troopers found marijuana. <span class="citation multiple-matches"><a href="/c/Ill.%202d/207/504/">207 Ill. 2d 504</a></span>, 506-507, <span class="citation multiple-matches"><a href="/c/N.%20E.%202d/802/202/">802 N. E. 2d 202</a></span>, 203 (2003).</p>
<p>The Supreme Court of Illinois held that the drug evidence should have been suppressed. <i>Id.,</i> at 506, 802 N. E. 2d, at 202. Adhering to its decision in <i>People</i> v. <i>Cox,</i> <span class="citation" data-id="9526758"><a href="/opinion/2038990/people-v-cox/" aria-description="Citation for case: People v. Cox">202 Ill. 2d 462</a></span>, <span class="citation" data-id="9526758"><a href="/opinion/2038990/people-v-cox/" aria-description="Citation for case: People v. Cox">782 N. E. 2d 275</a></span> (2002), the court employed a two-part test taken from <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), to determine the overall reasonableness of the stop. 207 Ill. 2d, at 508, 802 N. E. 2d, at 204. The court asked first "whether the officer's action was justified at its inception," and second "whether it was reasonably related in scope to the circumstances which justified the interference in the first place." <i>Ibid.</i> (quoting <i>People</i> v. <i>Brownlee,</i> <span class="citation" data-id="9718595"><a href="/opinion/2106553/people-v-brownlee/#518" aria-description="Citation for case: People v. Brownlee">186 Ill. 2d 501, 518-519</a></span>, <span class="citation" data-id="9718595"><a href="/opinion/2106553/people-v-brownlee/#565" aria-description="Citation for case: People v. Brownlee">713 N. E. 2d 556, 565</a></span> (1999) (in turn quoting <i>Terry,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 19-20</a></span>)). "[I]t is undisputed," the court observed, "that the traffic stop was properly initiated"; thus, the dispositive inquiry trained on the "second part of the <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> test," in which "[t]he State bears the burden of establishing that the conduct remained within the scope of the stop." 207 Ill. 2d, at 509, 802 N. E. 2d, at 204.</p>
<p><span class="star-pagination">*419</span> The court concluded that the State failed to offer sufficient justification for the canine sniff: "The police did not detect the odor of marijuana in the car or note any other evidence suggesting the presence of illegal drugs." <i>Ibid.</i> Lacking "specific and articulable facts" supporting the canine sniff, <i>ibid.</i> (quoting <i>Cox,</i> <span class="citation" data-id="9526758"><a href="/opinion/2038990/people-v-cox/#470" aria-description="Citation for case: People v. Cox">202 Ill. 2d, at 470-471</a></span>, <span class="citation" data-id="9526758"><a href="/opinion/2038990/people-v-cox/#281" aria-description="Citation for case: People v. Cox">782 N. E. 2d, at 281</a></span>), the court ruled, "the police impermissibly broadened the scope of the traffic stop in this case into a drug investigation." 207 Ill. 2d, at 509, 802 N. E. 2d, at 204.<sup>[1]</sup> I would affirm the Illinois Supreme Court's judgment and hold that the drug sniff violated the Fourth Amendment.</p>
<p>In <i>Terry</i> v. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio</a></span></i><i>,</i> the Court upheld the stop and subsequent frisk of an individual based on an officer's observation of suspicious behavior and his reasonable belief that the suspect was armed. See <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 27-28</a></span>. In a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i>-type investigatory stop, "the officer's action [must be] justified at its inception, and ... reasonably related in scope to the circumstances which justified the interference in the first place." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 20</a></span>. In applying <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> the Court has several times indicated that the limitation on "scope" is not confined to the duration of the seizure; it also encompasses the manner in which the seizure is conducted. See, <i>e. g., </i><i>Hiibel</i> v. <i>Sixth Judicial Dist. Court of Nev., Humboldt Cty.,</i> <span class="citation" data-id="9434645"><a href="/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/#188" aria-description="Citation for case: Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.">542 U. S. 177, 188</a></span> (2004) (an officer's request that an individual identify himself "has an immediate relation to the purpose, rationale, and practical demands of a <i>Terry</i> stop"); <i>United States</i> v. <i>Hensley,</i> <span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#235" aria-description="Citation for case: United States v. Hensley">469 U. S. 221, 235</a></span> (1985) (examining, under <i>Terry,</i> <span class="star-pagination">*420</span> both "the length and intrusiveness of the stop and detention"); <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 500</a></span> (1983) (plurality opinion) ("[A]n investigative detention must be temporary and last no longer than is necessary to effectuate the purpose of the stop [and] the investigative methods employed should be the least intrusive means reasonably available to verify or dispel the officer's suspicion. . . .").</p>
<p>"A routine traffic stop," the Court has observed, "is a relatively brief encounter and `is more analogous to a so-called <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop . . . than to a formal arrest.'" <i>Knowles</i> v. <i>Iowa,</i> <span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/#117" aria-description="Citation for case: Knowles v. Iowa">525 U. S. 113, 117</a></span> (1998) (quoting <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#439" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 439</a></span> (1984)); see also <i>ante,</i> at 415 (SOUTER, J., dissenting) (The government may not "take advantage of a suspect's immobility to search for evidence unrelated to the reason for the detention.").<sup>[2]</sup> I would apply <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i>'s reasonable-relation test, as the Illinois Supreme Court did, to determine whether the canine sniff impermissibly expanded the scope of the initially valid seizure of Caballes.</p>
<p>It is hardly dispositive that the dog sniff in this case may not have lengthened the duration of the stop. Cf. <i>ante,</i> at 407 ("A seizure ... can become unlawful if it is prolonged beyond the time reasonably required to complete [the initial] mission."). <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> it merits repetition, instructs that any investigation must be "reasonably related in <i>scope</i> to the circumstances which justified the interference in the first place." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20</a></span> (emphasis added). The unwarranted <span class="star-pagination">*421</span> and nonconsensual expansion of the seizure here from a routine traffic stop to a drug investigation broadened the scope of the investigation in a manner that, in my judgment, runs afoul of the Fourth Amendment.<sup>[3]</sup></p>
<p>The Court rejects the Illinois Supreme Court's judgment and, implicitly, the application of <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> to a traffic stop converted, by calling in a dog, to a drug search. The Court so rules, holding that a dog sniff does not render a seizure that is reasonable in time unreasonable in scope. <i>Ante,</i> at 408. Dog sniffs that detect only the possession of contraband may be employed without offense to the Fourth Amendment, the Court reasons, because they reveal no lawful activity and hence disturb no legitimate expectation of privacy. <i>Ante,</i> at 408-409.</p>
<p>In my view, the Court diminishes the Fourth Amendment's force by abandoning the second <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> inquiry (was the police action "reasonably related in scope to the circumstances [justifiying] the [initial] interference"). <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20</a></span>. A drug-detection dog is an intimidating animal. Cf. <i>United States</i> v. <i>Williams,</i> <span class="citation" data-id="9437405"><a href="/opinion/164282/united-states-v-williams/#1276" aria-description="Citation for case: United States v. Williams">356 F. 3d 1268, 1276</a></span> (CA10 2004) (McKay, J., dissenting) ("drug dogs are not lap dogs"). Injecting such an animal into a routine traffic stop changes the character of the encounter between the police and the motorist. The stop becomes broader, more adversarial, and (in at least some cases) longer. Caballes  who, as far as Troopers Gillette and Graham knew, was guilty solely of driving six miles per hour over the speed limit  was exposed to the embarrassment and intimidation of being investigated, on a public thoroughfare, for drugs. Even if the drug sniff is not characterized as a Fourth Amendment "search," cf. <i><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Indianapolis</a></span></i> <span class="star-pagination">*422</span> v. <i>Edmond,</i> <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#40" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S. 32, 40</a></span> (2000); <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U. S. 696, 707</a></span> (1983), the sniff surely broadened the scope of the traffic-violation-related seizure.</p>
<p>The Court has never removed police action from Fourth Amendment control on the ground that the action is well calculated to apprehend the guilty. See, <i>e. g., </i><i>United States</i> v. <i>Karo,</i> <span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/#717" aria-description="Citation for case: United States v. Karo">468 U. S. 705, 717</a></span> (1984) (Fourth Amendment warrant requirement applies to police monitoring of a beeper in a house even if "the facts [justify] believing that a crime is being or will be committed and that monitoring the beeper wherever it goes is likely to produce evidence of criminal activity."); see also <i>Minnesota</i> v. <i>Carter,</i> <span class="citation" data-id="9433723"><a href="/opinion/118249/minnesota-v-carter/#110" aria-description="Citation for case: Minnesota v. Carter">525 U. S. 83, 110</a></span> (1998) (GINSBURG, J., dissenting) ("Fourth Amendment protection, reserved for the innocent only, would have little force in regulating police behavior toward either the innocent or the guilty."). Under today's decision, every traffic stop could become an occasion to call in the dogs, to the distress and embarrassment of the law-abiding population.</p>
<p>The Illinois Supreme Court, it seems to me, correctly apprehended the danger in allowing the police to search for contraband despite the absence of cause to suspect its presence. Today's decision, in contrast, clears the way for suspicionless, dog-accompanied drug sweeps of parked cars along sidewalks and in parking lots. Compare, <i>e. g., </i><i>United States</i> v. <i>Ludwig,</i> <span class="citation" data-id="658364"><a href="/opinion/658364/united-states-v-keith-rudolph-ludwig-national-association-of-criminal/#1526" aria-description="Citation for case: United States v. Keith Rudolph Ludwig, National...">10 F. 3d 1523, 1526-1527</a></span> (CA10 1993) (upholding a search based on a canine drug sniff of a parked car in a motel parking lot conducted without particular suspicion), with <i>United States</i> v. <i>Quinn,</i> <span class="citation" data-id="9475983"><a href="/opinion/485654/united-states-v-daniel-j-quinn/#159" aria-description="Citation for case: United States v. Daniel J. Quinn">815 F. 2d 153, 159</a></span> (CA1 1987) (officers must have reasonable suspicion that a car contains narcotics at the moment a dog sniff is performed), and <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#706" aria-description="Citation for case: United States v. Place">462 U. S., at 706-707</a></span> (Fourth Amendment not violated by a dog sniff of a piece of luggage that was seized, pre-sniff, based on suspicion of drugs). Nor would motorists have constitutional grounds for complaint should police with dogs, stationed at long traffic lights, circle cars waiting for the red signal to turn green.</p>
<p><span class="star-pagination">*423</span> Today's decision also undermines this Court's situation-sensitive balancing of Fourth Amendment interests in other contexts. For example, in <i>Bond</i> v. <i>United States,</i> <span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/#338" aria-description="Citation for case: Bond v. United States">529 U. S. 334, 338-339</a></span> (2000), the Court held that a bus passenger had an expectation of privacy in a bag placed in an overhead bin and that a police officer's physical manipulation of the bag constituted an illegal search. If canine drug sniffs are entirely exempt from Fourth Amendment inspection, a sniff could substitute for an officer's request to a bus passenger for permission to search his bag, with this significant difference: The passenger would not have the option to say "No."</p>
<p>The dog sniff in this case, it bears emphasis, was for drug detection only. A dog sniff for explosives, involving security interests not presented here, would be an entirely different matter. Detector dogs are ordinarily trained not as all-purpose sniffers, but for discrete purposes. For example, they may be trained for narcotics detection or for explosives detection or for agricultural products detection. See, <i>e. g.,</i> U. S. Customs &amp; Border Protection, Canine Enforcement Training Center Training Program Course Descriptions, http://www.cbp.gov/xp/cgov/border_security/canines/training_program.xml (all Internet materials as visited Dec. 16, 2004, and available in Clerk of Court's case file) (describing Customs training courses in narcotics detection); Transportation Security Administration, Canine and Explosives Program, http://www.tsa.gov/public/display?theme=32 (describing Transportation Security Administration's explosives detection canine program); U. S. Dept. of Agriculture, Animal and Plant Health Inspection Service, USDA's Detector Dogs: Protecting American Agriculture (Oct. 2001), available at http://www.aphis.usda.gov/oa/pubs/detdogs.pdf (describing USDA Beagle Brigade detector dogs trained to detect prohibited fruits, plants, and meat); see also Jennings, Origins and History of Security and Detector Dogs, in Canine Sports Medicine and Surgery 16, 18-19 (M. Bloomberg, J. Dee, &amp; R. Taylor eds. 1998) (describing narcotics-detector <span class="star-pagination">*424</span> dogs used by Border Patrol and Customs, and bomb detector dogs used by the Federal Aviation Administration and the Secret Service, but noting the possibility in some circumstances of cross training dogs for multiple tasks); S. Chapman, Police Dogs in North America 64, 70-79 (1990) (describing narcotics- and explosives-detection dogs and noting the possibility of cross training). There is no indication in this case that the dog accompanying Trooper Graham was trained for anything other than drug detection. See 207 Ill. 2d, at 507, 802 N. E. 2d, at 203 ("Trooper Graham arrived with his drug-detection dog. . . ."); Brief for Petitioner 3 ("Trooper Graham arrived with a drug-detection dog. . . .").</p>
<p>This Court has distinguished between the general interest in crime control and more immediate threats to public safety. In <i>Michigan Dept. of State Police</i> v. <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U.S. 444</a></span> (1990), this Court upheld the use of a sobriety traffic checkpoint. Balancing the State's interest in preventing drunk driving, the extent to which that could be accomplished through the checkpoint program, and the degree of intrusion the stops involved, the Court determined that the State's checkpoint program was consistent with the Fourth Amendment. <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#455" aria-description="Citation for case: Michigan Department of State Police v. Sitz"><i>Id.,</i> at 455</a></span>. Ten years after <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span>,</i> in <i>Indianapolis</i> v. <i>Edmond,</i> <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S. 32</a></span>, this Court held that a drug interdiction checkpoint violated the Fourth Amendment. Despite the illegal narcotics traffic that the Nation is struggling to stem, the Court explained, a "general interest in crime control" did not justify the stops. <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#43" aria-description="Citation for case: City of Indianapolis v. Edmond"><i>Id.,</i> at 43-44</a></span> (internal quotation marks omitted). The Court distinguished the sobriety checkpoints in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> on the ground that those checkpoints were designed to eliminate an "immediate, vehicle-bound threat to life and limb." <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#43" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S., at 43</a></span>.</p>
<p>The use of bomb-detection dogs to check vehicles for explosives without doubt has a closer kinship to the sobriety checkpoints in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> than to the drug checkpoints in <i><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span>.</i> As the Court observed in <i><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span>:</i> "[T]he Fourth Amendment would almost certainly permit an appropriately tailored <span class="star-pagination">*425</span> roadblock set up to thwart an imminent terrorist attack. . . ." <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#44" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S., at 44</a></span>. Even if the Court were to change course and characterize a dog sniff as an independent Fourth Amendment search, see <i>ante,</i> p. 410 (SOUTER, J., dissenting), the immediate, present danger of explosives would likely justify a bomb sniff under the special needs doctrine. See, <i>e. g., ante,</i> at 417, n. 7 (SOUTER, J., dissenting); <i>Griffin</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868, 873</a></span> (1987) (permitting exceptions to the warrant and probable-cause requirements for a search when "special needs, beyond the normal need for law enforcement," make those requirements impracticable (quoting <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#351" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 351</a></span> (1985) (Blackmun, J., concurring in judgment))).</p>
<p></p>
<h2>* * *</h2>
<p>For the reasons stated, I would hold that the police violated Caballes' Fourth Amendment rights when, without cause to suspect wrongdoing, they conducted a dog sniff of his vehicle. I would therefore affirm the judgment of the Illinois Supreme Court.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the State of Arkansas et al. by <i>Mike Beebe,</i> Attorney General of Arkansas, <i>Lauren Elizabeth Heil,</i> Assistant Attorney General, and <i>Dan Schweitzer,</i> and by the Attorneys General for their respective States as follows: <i>Troy King</i> of Alabama, <i>Terry Goddard</i> of Arizona, <i>Christopher L. Morano</i> of Connecticut, <i>M. Jane Brady</i> of Delaware, <i>Thurbert E. Baker</i> of Georgia, <i>Mark J. Bennett</i> of Hawaii, <i>Lawrence G. Wasden</i> of Idaho, <i>Steve Carter</i> of Indiana, <i>Phill Kline</i> of Kansas, <i>Charles C. Foti</i> of Louisiana, <i>G. Steven Rowe</i> of Maine, <i>J. Joseph Curran, Jr.,</i> of Maryland, <i>Michael A. Cox</i> of Michigan, <i>Jon Bruning</i> of Nebraska, <i>Peter C. Harvey</i> of New Jersey, <i>Patricia A. Madrid</i> of New Mexico, <i>Roy Cooper</i> of North Carolina, <i>Wayne Stenehjem</i> of North Dakota, <i>Jim Petro</i> of Ohio, <i>Hardy Myers</i> of Oregon, <i>Henry D. McMaster</i> of South Carolina, <i>Lawrence E. Long</i> of South Dakota, <i>Greg Abbott</i> of Texas, <i>Mark L. Shurtleff</i> of Utah, <i>William H. Sorrell</i> of Vermont, <i>Jerry Kilgore</i> of Virginia, and <i>Patrick J. Crank</i> of Wyoming; and for the Illinois Association of Chiefs of Police et al. by <i>James G. Sotos.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the American Civil Liberties Union et al. by <i>Barry Sullivan, Jacob I. Corré, Steven R. Shapiro,</i> and <i>Harvey Grossman;</i> and for the National Association of Criminal Defense Lawyers by <i>Jeffrey T. Green, John Wesley Hall, Jr.,</i> and <i>David M. Siegel.</i></p>
<p>[1]  I also join JUSTICE GINSBURG's dissent, <i>post,</i> p. 417. Without directly reexamining the soundness of the Court's analysis of government dog sniffs in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> she demonstrates that investigation into a matter beyond the subject of the traffic stop here offends the rule in <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), the analysis I, too, adopt.</p>
<p>[2]  Another proffered justification for <i>sui generis</i> status is that a dog sniff is a particularly nonintrusive procedure. <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U. S. 696, 707</a></span> (1983). I agree with JUSTICE GINSBURG that the introduction of a dog to a traffic stop (let alone an encounter with someone walking down the street) can in fact be quite intrusive. <i>Post,</i> at 421-422.</p>
<p>[3]  <i><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">Kyllo</a></span></i> was concerned with whether a search occurred when the police used a thermal-imaging device on a house to detect heat emanations associated with high-powered marijuana-growing lamps. In concluding that using the device was a search, the Court stressed that the "Government [may not] us[e] a device ... to explore details of the home that would previously have been unknowable without physical intrusion." <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#40" aria-description="Citation for case: Kyllo v. United States">533 U.S., at 40</a></span>. Any difference between the dwelling in <i><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">Kyllo</a></span></i> and the trunk of the car here may go to the issue of the reasonableness of the respective searches, but it has no bearing on the question of search or no search. Nor is it significant that <i><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">Kyllo</a></span></i>'s imaging device would disclose personal details immediately, whereas they would be revealed only in the further step of opening the enclosed space following the dog's alert reaction; in practical terms the same values protected by the Fourth Amendment are at stake in each case. The justifications required by the Fourth Amendment may or may not differ as between the two practices, but if constitutional scrutiny is in order for the imager, it is in order for the dog.</p>
<p>[4]  Despite the remarkable fact that the police pulled over a car for going 71 miles an hour on I-80, the State maintains that excessive speed was the only reason for the stop, and the case comes to us on that assumption.</p>
<p>[5]  Thus, in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> itself, the Government officials had independent grounds to suspect that the luggage in question contained contraband before they employed the dog sniff. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#698" aria-description="Citation for case: United States v. Place">462 U. S., at 698</a></span> (describing how Place had acted suspiciously in line at the airport and had labeled his luggage with inconsistent and fictional addresses).</p>
<p>[6]  It would also be error to claim that some variant of the plain-view doctrine excuses the lack of justification for the dog sniff in this case. When an officer observes an object left by its owner in plain view, no search occurs because the owner has exhibited "no intention to keep [the object] to himself." <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 361</a></span> (1967) (Harlan, J., concurring). In contrast, when an individual conceals his possessions from the world, he has grounds to expect some degree of privacy. While plain view may be enhanced somewhat by technology, see, <i>e.g., </i><i>Dow Chemical Co.</i> v. <i>United States,</i> <span class="citation" data-id="9430504"><a href="/opinion/111667/dow-chemical-co-v-united-states-ex-rel-administrator/" aria-description="Citation for case: Dow Chemical Co. v. United States Ex Rel. Administrator">476 U. S. 227</a></span> (1986) (allowing for aerial surveillance of an industrial complex), there are limits. As <i>Kyllo</i> v. <i>United States,</i> <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#33" aria-description="Citation for case: Kyllo v. United States">533 U. S. 27, 33</a></span> (2001), explained in treating the thermal-imaging device as outside the plain-view doctrine, "[w]e have previously reserved judgment as to how much technological enhancement of ordinary perception" turns mere observation into a Fourth Amendment search. While <i><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">Kyllo</a></span></i> laid special emphasis on the heightened privacy expectations that surround the home, closed car trunks are accorded some level of privacy protection. See, <i>e. g., </i><i>New York</i> v. <i>Belton,</i> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S. 454, 460, n. 4</a></span> (1981) (holding that even a search incident to arrest in a vehicle does not itself permit a search of the trunk). As a result, if Fourth Amendment protections are to have meaning in the face of superhuman, yet fallible, techniques like the use of trained dogs, those techniques must be justified on the basis of their reasonableness, lest everything be deemed in plain view.</p>
<p>[7]  I should take care myself to reserve judgment about a possible case significantly unlike this one. All of us are concerned not to prejudge a claim of authority to detect explosives and dangerous chemical or biological weapons that might be carried by a terrorist who prompts no individualized suspicion. Suffice it to say here that what is a reasonable search depends in part on demonstrated risk. Unreasonable sniff searches for marijuana are not necessarily unreasonable sniff searches for destructive or deadly material if suicide bombs are a societal risk.</p>
<p>[1]  The Illinois Supreme Court held insufficient to support a canine sniff Gillette's observations that (1) Caballes said he was moving to Chicago, but his only visible belongings were two sport coats in the backseat; (2) the car smelled of air freshener; (3) Caballes was dressed for business, but was unemployed; and (4) Caballes seemed nervous. Even viewed together, the court said, these observations gave rise to "nothing more than a vague hunch" of "possible wrongdoing." <span class="citation multiple-matches"><a href="/c/Ill.%202d/207/504/">207 Ill. 2d 504</a></span>, 509-510, <span class="citation multiple-matches"><a href="/c/N.%20E.%202d/802/202/">802 N. E. 2d 202</a></span>, 204-205 (2003). This Court proceeds on "the assumption that the officer conducting the dog sniff had no information about [Caballes]." <i>Ante,</i> at 407.</p>
<p>[2]  The <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i> Court cautioned that by analogizing a traffic stop to a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop, it did "not suggest that a traffic stop supported by probable cause may not exceed the bounds set by the Fourth Amendment on the scope of a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop." 468 U. S., at 439, n. 29. This Court, however, looked to <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> earlier in deciding that an officer acted reasonably when he ordered a motorist stopped for driving with expired license tags to exit his car, <i>Pennsylvania</i> v. <i>Mimms,</i> <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#109" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 109-110</a></span> (1977) <i>(per curiam)</i><i>,</i> and later reaffirmed the <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> analogy when evaluating a police officer's authority to search a vehicle during a routine traffic stop, <i>Knowles,</i> <span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/#117" aria-description="Citation for case: Knowles v. Iowa">525 U. S., at 117</a></span>.</p>
<p>[3]  The question whether a police officer inquiring about drugs without reasonable suspicion unconstitutionally broadens a traffic investigation is not before the Court. Cf. <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#434" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429, 434</a></span> (1991) (police questioning of a bus passenger, who might have just said "No," did not constitute a seizure).</p>

</div>
```

---

## GROUP: content/cases/Illinois v. Gates.md  (`case`, 7 assertions)

### content_page

```
---
title: "Illinois v. Gates"
type: case
citation: "462 U.S. 213 (1983)"
parallel_cite: "103 S. Ct. 2317; 76 L. Ed. 2d 527; 51 U.S.L.W. 4709"
neutral_cite: 1983 U.S. LEXIS 54
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-06-08
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1983-06-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Illinois v. Gates
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110959/illinois-v-gates/"
  cluster_id: 110959
  opinion_id: 9429232
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Key — Anchor"
  - page: "[[Probable Cause in the Affidavit]]"
    role: "Related (cross-doctrine)"
  - page: "[[The Proof Ladder]]"
    role: "Key — rung anchor"
related: ["[[Aguilar v. Texas]]", "[[Spinelli v. United States]]", "[[Brinegar v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "probable-cause", "informants", "totality-of-the-circumstances", "warrant"]
holding: "Probable cause from an informant's tip is judged by the **totality of the circumstances** — the issuing magistrate makes a practical,…"
lake:
  record_id: Illinois v. Gates
  status: verified
  projected_at: 2026-07-06
---

# Illinois v. Gates

*462 U.S. 213 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police received an anonymous letter stating that Lance and Susan Gates were drug dealers, detailing a method by which one would fly to Florida, load a car with drugs, and drive it back while the other flew home. Officers corroborated the largely innocent travel details and obtained a warrant; a search of the Gateses' car and home turned up marijuana and other contraband. The Illinois courts, applying the rigid two-pronged informant test, suppressed the evidence.

## Issue
Whether probable cause based on an informant's tip must satisfy the two independent prongs of the *[[Aguilar v. Texas|Aguilar]]*–*[[Spinelli v. United States|Spinelli]]* test, or is instead judged by the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]].

## Rule
Probable cause from a tip is judged by the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]. "For all these reasons, we conclude that it is wiser to abandon the 'two-pronged test' established by our decisions in Aguilar and Spinelli. In its place we reaffirm the totality-of-the-circumstances analysis that traditionally has informed probable-cause determinations." — 462 U.S. at 238. ^pin-238

"The task of the issuing magistrate is simply to make a practical, common-sense decision whether, given all the circumstances set forth in the affidavit before him, including the 'veracity' and 'basis of knowledge' of persons supplying hearsay information, there is a fair probability that contraband or evidence of a crime will be found in a particular place." — *Id.* ^pin-238a

## Application
Treating the informant's veracity and basis of knowledge as relevant but no longer independent, dispositive requirements, the Court found the anonymous letter, corroborated by the police investigation of the Gateses' predicted Florida travel, gave the magistrate a substantial basis to conclude there was a fair probability that contraband would be found in the car and home. The warrant was therefore supported by probable cause.

## Conclusion
The warrant was valid under the totality-of-the-circumstances test; the suppression was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of *Gates*. *Gates* itself **abandoned** the rigid two-pronged framework of [[Aguilar v. Texas]] and [[Spinelli v. United States]], replacing it with the flexible totality-of-the-circumstances standard.

## Appears on
- [[Probable Cause]] — *Key — Anchor*
- [[Probable Cause in the Affidavit]] — *Related (cross-doctrine)*
- [[The Proof Ladder]] — *Key — rung anchor*

## Sources
- *Illinois v. Gates*, 462 U.S. 213 (1983) — https://www.courtlistener.com/opinion/110959/illinois-v-gates/ — pinpoint: 238.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "17a2275ae2efef21", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "462 U.S. 213 (1983)", "court": "U.S. Supreme Court", "neutral_cite": "1983 U.S. LEXIS 54", "official_citation_present": true, "parallel_cite": "103 S. Ct. 2317; 76 L. Ed. 2d 527; 51 U.S.L.W. 4709", "title": "Illinois v. Gates", "year": "1983"}}
{"assertion_id": "3027cf48c8f13435", "dimension": "support", "kind": "home_role", "locator": {"home": "The Proof Ladder"}, "payload": {"home": "The Proof Ladder", "role": "Key — rung anchor", "title": "Illinois v. Gates"}}
{"assertion_id": "50808f56a788eab9", "dimension": "support", "kind": "home_role", "locator": {"home": "Probable Cause in the Affidavit"}, "payload": {"home": "Probable Cause in the Affidavit", "role": "Related (cross-doctrine)", "title": "Illinois v. Gates"}}
{"assertion_id": "e5ade4ca3bd50c16", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Probable cause from an informant's tip is judged by the **totality of the circumstances** — the issuing magistrate makes a practical,…", "title": "Illinois v. Gates"}}
{"assertion_id": "e622ce9d8c62dee9", "dimension": "support", "kind": "home_role", "locator": {"home": "Probable Cause"}, "payload": {"home": "Probable Cause", "role": "Key — Anchor", "title": "Illinois v. Gates"}}
{"assertion_id": "3f023f35e5f695b5", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Illinois v. Gates"}}
{"assertion_id": "bc0d73c285baf19e", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1983-06-08", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Illinois v. Gates", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Illinois v. Gates", "varies_by_point": "false"}}
```

### lake record — Illinois v. Gates

```json
{
  "schema_version": "s2.v1",
  "record_id": "Illinois v. Gates",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Illinois v. Gates",
    "case_name_short": "Gates",
    "case_name_full": "ILLINOIS v. GATES Et Ux.",
    "input_case_name": "Illinois v. Gates",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-06-08",
    "year": 1983,
    "docket": null,
    "cluster_id": 110959,
    "lead_opinion_id": 9429232,
    "sibling_ids": [
      110959,
      9429232,
      9429233,
      9429234,
      9429235
    ],
    "absolute_url": "/opinion/110959/illinois-v-gates/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9046341,
        "score": 20,
        "case_name": "Illinois v. Gates"
      },
      {
        "cluster_id": 9044083,
        "score": 20,
        "case_name": "Illinois v. Gates"
      },
      {
        "cluster_id": 9043404,
        "score": 20,
        "case_name": "Illinois v. Gates"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "462 U.S. 213",
      "volume": "462",
      "reporter": "U.S.",
      "page": "213",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 2317",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2317",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "76 L. Ed. 2d 527",
        "volume": "76",
        "reporter": "L. Ed. 2d",
        "page": "527",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4709",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4709",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 54",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "54",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "462 U.S. 213",
        "volume": "462",
        "reporter": "U.S.",
        "page": "213",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 2317",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2317",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "76 L. Ed. 2d 527",
        "volume": "76",
        "reporter": "L. Ed. 2d",
        "page": "527",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 54",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "54",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4709",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4709",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "462 U.S. 213",
    "official_selection": {
      "court_class": "scotus",
      "selected": "462 U.S. 213",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-238",
      "page": null,
      "quote": "--- # Illinois v. Gates *462 U.S. 213 (1983)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police received an anonymous letter stating that Lance and Susan Gates were drug dealers, detailing a method by which one would fly to Florida, load a car with drugs, and drive it back while the other flew home. Officers corroborated the largely innocent travel details and obtained a warrant; a search of the Gateses' car and home turned up marijuana and other contraband. The Illinois courts, applying the rigid two-pronged informant test, suppressed the evidence. ## Issue Whether probable cause based on an informant's tip must satisfy the two independent prongs of the *Aguilar*\u2013*Spinelli* test, or is instead judged by the totality of the circumstances. ## Rule Probable cause from a tip is judged by the totality of the circumstances.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-238a",
      "page": null,
      "quote": "The task of the issuing magistrate is simply to make a practical, common-sense decision whether, given all the circumstances set forth in the affidavit before him, including the 'veracity' and 'basis of knowledge' of persons supplying hearsay information, there is a fair probability that contraband or evidence of a crime will be found in a particular place.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-06-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Illinois v. Gates",
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
        "journal_ref": "Illinois v. Gates:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wright",
          "cluster_id": 10658752,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane1_negative"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ornelas v. United States",
          "cluster_id": 118030,
          "cite": [
            "134 L. Ed. 2d 911",
            "116 S. Ct. 1657",
            "517 U.S. 690",
            "1996 U.S. LEXIS 3391"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malley v. Briggs",
          "cluster_id": 111611,
          "cite": [
            "89 L. Ed. 2d 271",
            "106 S. Ct. 1092",
            "475 U.S. 335",
            "1986 U.S. LEXIS 29",
            "54 U.S.L.W. 4243"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sokolow",
          "cluster_id": 112239,
          "cite": [
            "104 L. Ed. 2d 1",
            "109 S. Ct. 1581",
            "490 U.S. 1",
            "1989 U.S. LEXIS 1694",
            "57 U.S.L.W. 4401"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edward H. Phillips v. Awh Corporation, Hopeman Brothers, Inc., and Lofton Corporation, Defendants-Cross",
          "cluster_id": 791122,
          "cite": [
            "415 F.3d 1303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Siegert v. Gilley",
          "cluster_id": 112594,
          "cite": [
            "114 L. Ed. 2d 277",
            "111 S. Ct. 1789",
            "500 U.S. 226",
            "1991 U.S. LEXIS 2909",
            "59 U.S.L.W. 4465"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460854,
          "cite": [
            "583 U.S. 48",
            "138 S. Ct. 577",
            "199 L. Ed. 2d 453",
            "2018 U.S. LEXIS 760"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Unger",
          "cluster_id": 1916834,
          "cite": [
            "749 N.W.2d 272",
            "278 Mich. App. 210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Idaho v. Wright",
          "cluster_id": 112488,
          "cite": [
            "111 L. Ed. 2d 638",
            "110 S. Ct. 3139",
            "497 U.S. 805",
            "1990 U.S. LEXIS 3461",
            "30 Fed. R. Serv. 24",
            "58 U.S.L.W. 5036"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "R. A. v. v. City of St. Paul",
          "cluster_id": 112774,
          "cite": [
            "120 L. Ed. 2d 305",
            "112 S. Ct. 2538",
            "505 U.S. 377",
            "1992 U.S. LEXIS 3863"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Pringle",
          "cluster_id": 131150,
          "cite": [
            "157 L. Ed. 2d 769",
            "124 S. Ct. 795",
            "540 U.S. 366",
            "2003 U.S. LEXIS 9198"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Quarles",
          "cluster_id": 111214,
          "cite": [
            "81 L. Ed. 2d 550",
            "104 S. Ct. 2626",
            "467 U.S. 649",
            "1984 U.S. LEXIS 111",
            "52 U.S.L.W. 4790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Acevedo",
          "cluster_id": 112608,
          "cite": [
            "114 L. Ed. 2d 619",
            "111 S. Ct. 1982",
            "500 U.S. 565",
            "1991 U.S. LEXIS 3016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wiede v. State",
          "cluster_id": 1404049,
          "cite": [
            "214 S.W.3d 17",
            "2007 Tex. Crim. App. LEXIS 100",
            "2007 WL 257624"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramos v. Louisiana",
          "cluster_id": 9231323,
          "cite": [
            "140 S. Ct. 1390",
            "206 L. Ed. 2d 583"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110959 OR 9429232 OR 9429233 OR 9429234 OR 9429235) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzI5MTIzMjAwMDAwJnM9MTAxNDUzMzkmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110959+OR+9429232+OR+9429233+OR+9429234+OR+9429235%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 2,
        "triage_snippet_classified": 198
      },
      "lane2_top_cited": {
        "query": "cites:(110959 OR 9429232 OR 9429233 OR 9429234 OR 9429235)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04MjImcz0xMTExNzImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110959+OR+9429232+OR+9429233+OR+9429234+OR+9429235%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110959 OR 9429232 OR 9429233 OR 9429234 OR 9429235)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzQ0ODQ4MDAwMDAwJnM9MTAzODA1NDImdD1vJmQ9MjAyNi0wNy0wNiZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110959+OR+9429232+OR+9429233+OR+9429234+OR+9429235%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 2,
        "triage_snippet_classified": 198
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110959 OR 9429232 OR 9429233 OR 9429234 OR 9429235)",
    "indexed_citing_opinions": 10044,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110959,
        "count": 8815,
        "count_source": "search"
      },
      {
        "opinion_id": 9429232,
        "count": 1423,
        "count_source": "search"
      },
      {
        "opinion_id": 9429233,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429234,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429235,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 16734,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/illinois-v-gates.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk4MDM4Njcmcz0yMjk4NDE2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110959+OR+9429232+OR+9429233+OR+9429234+OR+9429235%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110959,
        "cited_id": 93933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 95004,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 101335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 103320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 103597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 104087,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 104668,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107526,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107577,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108379,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108497,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109303,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109349,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110236,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110425,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110916,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 312873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 326825,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 378896,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 1123854,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 2023247,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 2100482,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 2151397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 2333704,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 2433225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 2620876,
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
    "date_created": "2026-07-05T07:54:35Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:55:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:55:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:59:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:55:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Illinois v. Gates

```
<opinion type="majority">
<author id="b260-4"><page-number citation-index="1" label="216">*216</page-number>Justice Rehnquist</author>
<p id="AKb">delivered the opinion of the Court.</p>
<p id="A6a">Respondents Lance and Susan Gates were indicted for violation of state drug laws after police officers, executing a search warrant, discovered marihuana and other contraband in their automobile and home. Prior to trial the Gateses moved to suppress evidence seized during this search. The Illinois Supreme Court affirmed the decisions of lower state courts granting the motion. <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/" aria-description="Citation for case: People of Illinois v. Gates">85 Ill. 2d 376</a></span>, <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d 887</a></span> (1981). ■ It held that the affidavit submitted in support of the State’s application for a warrant to search the Gateses’ prop<page-number citation-index="1" label="217">*217</page-number>erty was inadequate under this Court’s decisions in <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), and <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969).</p>
<p id="Alt">We granted certiorari to consider the application of the Fourth Amendment to a magistrate’s issuance of a search warrant on the basis of a partially corroborated anonymous informant’s tip. <span class="citation multiple-matches"><a href="/c/U.%20S./454/1140/">454 U. S. 1140</a></span> (1982). After receiving briefs and hearing oral argument on this question, however, we requested the parties to address an additional question:</p>
<blockquote id="A63">“[Wjhether the rule requiring the exclusion at a criminal trial of evidence obtained in violation of the Fourth Amendment, <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961); <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), should to any extent be modified, so as, for example, not to require the exclusion of evidence obtained in the reasonable belief that the search and seizure at issue was consistent with the Fourth Amendment.” <span class="citation" data-id="9429042"><a href="/opinion/110850/illinois-v-gates-et-ux/" aria-description="Citation for case: Illinois v. Gates Et Ux.">459 U. S. 1028</a></span> (1982).</blockquote>
<p id="Aelb">We decide today, with apologies to all, that the issue we framed for the parties was not presented to the Illinois courts and, accordingly, do not address it. Rather, we consider the question originally presented in the petition for certiorari, and conclude that the Illinois Supreme Court read the requirements of our Fourth Amendment decisions too restrictively. Initially, however, we set forth our reasons for not addressing the question regarding modification of the exclusionary rule framed in our order of November 29,1982. <em><span class="citation" data-id="9429042"><a href="/opinion/110850/illinois-v-gates-et-ux/" aria-description="Citation for case: Illinois v. Gates Et Ux.">Ibid.</a></span></em></p>
<p id="AqtE">HH</p>
<p id="A9_">Our certiorari jurisdiction over decisions from state courts derives from <span class="citation no-link">28 U. S. C. § 1257</span>, which provides that “[f]inal judgments or decrees rendered by the highest court of a State in which a decision could be had, may be reviewed by the Supreme Court as follows: ... (3) By writ of certiorari, . . . where any title, right, privilege or immunity is specially set up or claimed under the Constitution, treaties or statutes <page-number citation-index="1" label="218">*218</page-number>of... the United States.” The provision derives, albeit with important alterations, see, <em>e. g., </em>Act of Dec. 23, 1914, ch. 2, <span class="citation no-link">38 Stat. 790</span>; Act of June 25, 1948, § 1257, <span class="citation no-link">62 Stat. 929</span>, from the Judiciary Act of 1789, § 25, <span class="citation no-link">1 Stat. 85</span>.</p>
<p id="b262-5">Although we have spoken frequently on the meaning of §1257 and its predecessors, our decisions are in some respects not entirely clear. We held early on that § 25 of the Judiciary Act of 1789 furnished us with no jurisdiction unless a federal question had been both raised and decided in the state court below. As Justice Story wrote in <em>Crowell </em>v. <em>Randell, </em><span class="citation no-link">10 Pet. 368</span>, 392 (1836): “If both of these requirements do not appear on the record, the appellate jurisdiction fails.” See also <em>Owings </em>v. <em>Norwood’s Lessee, </em><span class="citation" data-id="84919"><a href="/opinion/84919/owings-v-norwoods-lessee/" aria-description="Citation for case: Owings v. Norwood&#x27;s Lessee">5 Cranch 344</a></span> (1809).<footnotemark>1</footnotemark></p>
<p id="b262-6">More recently, in <em>McGoldrick </em>v. <em>Compagnie Generale Transatlantique, </em><span class="citation" data-id="9419089"><a href="/opinion/103320/mcgoldrick-v-compagnie-generale-transatlantique/#434" aria-description="Citation for case: McGoldrick v. Compagnie Generale Transatlantique">309 U. S. 430, 434-435</a></span> (1940), the Court observed:</p>
<blockquote id="b262-7">“But it is also the settled practice of this Court, in the exercise of its appellate jurisdiction, that it is only in exceptional cases, and then only in cases coming from the federal courts, that it considers questions urged by a petitioner or appellant not pressed or passed upon in the courts below.... In cases coming here from state courts in which a state statute is assailed as unconstitutional, there are reasons of peculiar force which should lead us to refrain from deciding questions not presented or decided in the highest court of the state whose judicial action we are called upon to review. Apart from the <page-number citation-index="1" label="219">*219</page-number>reluctance with which every court should proceed to set aside legislation as unconstitutional on grounds not properly presented, due regard for the appropriate relationship of this Court to state courts requires us to decline to consider and decide questions affecting the validity of state statutes not urged or considered there. It is for these reasons that this Court, where the constitutionality of a statute has been upheld in the state court, consistently refuses to consider any grounds of attack not raised or decided in that court.”</blockquote>
<p id="b263-5">Finally, the Court seemed to reaffirm the jurisdictional character of the rule against our deciding claims “not pressed nor passed upon” in state court in <em>State Farm Mutual Automobile Ins. Co. </em>v. <em>Duel, </em><span class="citation" data-id="104087"><a href="/opinion/104087/state-farm-mutual-automobile-insurance-v-duel/#160" aria-description="Citation for case: State Farm Mutual Automobile Insurance v. Duel">324 U. S. 154, 160</a></span> (1945), where we explained that “[sjince the [State] Supreme Court did not pass on the question, we may not do so.” See also <em>Hill </em>v. <em>California, </em><span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/#805" aria-description="Citation for case: Hill v. California">401 U. S. 797, 805-806</a></span> (1971).</p>
<p id="b263-6">Notwithstanding these decisions, however, several of our more recent cases have treated the so-called “not pressed or passed upon below” rule as merely a prudential restriction. In <em>Terminiello </em>v. <em>Chicago, </em><span class="citation" data-id="9420312"><a href="/opinion/104668/terminiello-v-chicago/" aria-description="Citation for case: Terminiello v. Chicago">337 U. S. 1</a></span> (1949), the Court reversed a state criminal conviction on a ground not urged in state court, nor even in this Court. Likewise, in <em>Vachon </em>v. <em>New Hampshire, </em><span class="citation" data-id="9425500"><a href="/opinion/108905/vachon-v-new-hampshire/" aria-description="Citation for case: Vachon v. New Hampshire">414 U. S. 478</a></span> (1974), the Court summarily reversed a state criminal conviction on the ground, not raised in state court, or here, that it had been obtained in violation of the Due Process Clause of the Fourteenth Amendment. The Court indicated in a footnote, <span class="citation" data-id="9425500"><a href="/opinion/108905/vachon-v-new-hampshire/#479" aria-description="Citation for case: Vachon v. New Hampshire"><em>id., </em>at 479, n. 3</a></span>, that it possessed discretion to ignore the failure to raise in state court the question on which it decided the case.</p>
<p id="b263-7">In addition to this lack of clarity as to the character of the “not pressed or passed upon below” rule, we have recognized that it often may be unclear whether the particular federal question presented in this Court was raised or passed upon below. In <em>Dewey </em>v. <em>Des Moines, </em><span class="citation" data-id="95004"><a href="/opinion/95004/dewey-v-des-moines/#197" aria-description="Citation for case: Dewey v. Des Moines">173 U. S. 193, 197-198</a></span> (1899), the fullest treatment of the subject, the Court said <page-number citation-index="1" label="220">*220</page-number>that “[i]f the question were only an enlargement of the one mentioned in the assignment of errors, or if it were so connected with it in substance as to form but another ground or reason for alleging the invalidity of the [lower court’s] judgment, we should have no hesitation in holding the assignment sufficient to permit the question to be now raised and argued. Parties are not confined here to the same arguments which were advanced in the courts below upon a Federal question there discussed.”<footnotemark>2</footnotemark> We have not attempted, and likely would not have been able, to draw a clear-cut line between cases involving only an “enlargement” of questions presented below and those involving entirely new questions.</p>
<p id="b264-5">The application of these principles in the instant case is not entirely straightforward. It is clear in this case that respondents expressly raised, at every level of the Illinois judicial system, the claim that the Fourth Amendment had been violated by the actions of the Illinois police and that the evidence seized by the officers should be excluded from their trial. It also is clear that the State challenged, at every level of the Illinois court system, respondents’ claim that the substantive requirements of the Fourth Amendment had been violated. The State never, however, raised or addressed the question whether the federal exclusionary rule should be modified in any respect, and none of the opinions of the <page-number citation-index="1" label="221">*221</page-number>Illinois courts give any indication that the question was considered.</p>
<p id="b265-5">The case, of course, is before us on the State’s petition for a writ of certiorari. Since the Act of Dec. 23, 1914, ch. 2, <span class="citation no-link">38 Stat. 790</span>, jurisdiction has been vested in this Court to review state-court decisions even when a claimed federal right has been upheld. Our prior decisions interpreting the “not pressed or passed on below” rule have not, however, involved a State’s failure to raise a defense to a federal right or remedy asserted below. As explained below, however, we can see no reason to treat the State’s failure to have challenged an asserted federal claim differently from the failure of the proponent of a federal claim to have raised that claim.</p>
<p id="b265-6">We have identified several purposes underlying the “not pressed or passed upon” rule: for the most part, these are as applicable to the State’s failure to have opposed the assertion of a particular federal right, as to a party’s failure to have asserted the claim. First, “[questions not raised below are those on which the record is very likely to be inadequate since it certainly was not compiled with those questions in mind.” <em>Cardinale </em>v. <em>Louisiana, </em><span class="citation" data-id="107889"><a href="/opinion/107889/cardinale-v-louisiana/#439" aria-description="Citation for case: Cardinale v. Louisiana">394 U. S. 437, 439</a></span> (1969). Exactly the same difficulty exists when the State urges modification of an existing constitutional right or accompanying remedy. Here, for example, the record contains little, if anything, regarding the subjective good faith of the police officers that searched the Gateses’ property — which might well be an important consideration in determining whether to fashion a good-faith exception to the exclusionary rule. Our consideration of whether to modify the exclusionary rule plainly would benefit from a record containing such facts.</p>
<p id="b265-7">Likewise, “due regard for the appropriate relationship of this Court to state courts,” <em>McGoldrick </em>v. <em>Compagnie Generale Transatlantique, </em><span class="citation" data-id="9419089"><a href="/opinion/103320/mcgoldrick-v-compagnie-generale-transatlantique/#434" aria-description="Citation for case: McGoldrick v. Compagnie Generale Transatlantique">309 U. S., at 434-435</a></span>, demands that those courts be given an opportunity to consider the constitutionality of the actions of state officials, and, equally important, proposed changes in existing remedies for uncon<page-number citation-index="1" label="222">*222</page-number>stitutional actions. Finally, by requiring that the State first argue to the state courts that the federal exclusionary rule should be modified, we permit a state court, even if it agrees with the State as a matter of federal law, to rest its decision on an adequate and independent state ground. See <span class="citation" data-id="107889"><a href="/opinion/107889/cardinale-v-louisiana/#439" aria-description="Citation for case: Cardinale v. Louisiana"><em>Cardinale, supra, </em>at 439</a></span>. Illinois, for example, adopted an exclusionary rule as early as 1923, see <em>People </em>v. <em>Brocamp, </em><span class="citation" data-id="6980967"><a href="/opinion/7076213/people-v-brocamp/" aria-description="Citation for case: People v. Brocamp">307 Ill. 448</a></span>, <span class="citation" data-id="6980967"><a href="/opinion/7076213/people-v-brocamp/" aria-description="Citation for case: People v. Brocamp">138 N. E. 728</a></span> (1923), and might adhere to its view even if it thought we would conclude that the federal rule should be modified. In short, the reasons supporting our refusal to hear federal claims not raised in state court apply with equal force to the State’s failure to challenge the availability of a well-settled federal remedy. Whether the “not pressed or passed upon below” rule is jurisdictional, as our earlier decisions indicate, see <em>supra, </em>at 217-219, or prudential, as several of our later decisions assume, or whether its character might be different in cases like this from its character elsewhere, we need not decide. Whatever the character of the rule may be, consideration of the question presented in our order of November 29, 1982, would be contrary to the sound justifications for the “not pressed or passed upon below” rule, and we thus decide not to pass on the issue.</p>
<p id="b266-5">The fact that the Illinois courts affirmatively applied the federal exclusionary rule — suppressing evidence against respondents — does not affect our conclusion. In <em>Morrison </em>v. <em>Watson, </em><span class="citation" data-id="93933"><a href="/opinion/93933/morrison-v-watson/" aria-description="Citation for case: Morrison v. Watson">154 U. S. 111</a></span> (1894), the Court was asked to consider whether a state statute impaired the plaintiff in error’s contract with the defendant in error. It declined to hear the case because the question presented here had not been pressed or passed on below. The Court acknowledged that the lower court’s opinion had restated the conclusion, set forth in an earlier decision of that court, that the state statute did not impermissibly impair contractual obligations. Nonetheless, it held that there was no showing that “there was any real contest at any stage of this case upon the point,” <span class="citation" data-id="93933"><a href="/opinion/93933/morrison-v-watson/#115" aria-description="Citation for case: Morrison v. Watson"><em>id., </em>at 115</a></span>, and that without such a contest, the routine restate<page-number citation-index="1" label="223">*223</page-number>ment and application of settled law by an appellate court did not satisfy the “not pressed or passed upon below” rule. Similarly, in the present case, although the Illinois courts applied the federal exclusionary rule, there was never “any real contest” upon the point. The application of the exclusionary rule was merely a routine act, once a violation of the Fourth Amendment had been found, and not the considered judgment of the Illinois courts on the question whether application of a modified rule would be warranted on the facts of this case. In such circumstances, absent the adversarial dispute necessary to apprise the state court of the arguments for not applying the exclusionary rule, we will not consider the question whether the exclusionary rule should be modified.</p>
<p id="b267-5">Likewise, we do not believe that the State’s repeated opposition to respondents’ substantive Fourth Amendment claims suffices to have raised the question whether the exclusionary rule should be modified. The exclusionary rule is “a judicially created remedy designed to safeguard Fourth Amendment rights generally” and not “a personal constitutional right of the party aggrieved.” <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 348</a></span> (1974). The question whether the exclusionary rule’s remedy is appropriate in a particular context has long been regardéd as an issue separate from the question whether the Fourth Amendment rights of the party seeking to invoke the rule were violated by police conduct. See, <em>e. g., United States </em>v. <em>Havens, </em><span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/" aria-description="Citation for case: United States v. Havens">446 U. S. 620</a></span> (1980); <em>United States </em>v. <em>Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">435 U. S. 268</a></span> (1978); <em>United States </em>v. <em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">Calandra, supra;</a></span> Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U. S. 465</a></span> (1976). Because of this distinction, we cannot say that modification or abolition of the exclusionary rule is “so connected with [the substantive Fourth Amendment right at issue] as to form but another ground or reason for alleging the invalidity” of the judgment. <em>Dewey </em>v. <em>Des Moines, </em><span class="citation" data-id="95004"><a href="/opinion/95004/dewey-v-des-moines/#197" aria-description="Citation for case: Dewey v. Des Moines">173 U. S., at 197-198</a></span>. Rather, the rule’s modification was, for purposes of the “not pressed or passed upon below” rule, a separate claim that had to be specifically presented to the state courts.</p>
<p id="b268-4"><page-number citation-index="1" label="224">*224</page-number>Finally, weighty prudential considerations militate against our considering the question presented in our order of November 29, 1982. The extent of the continued vitality of the rules that have developed from our decisions in <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), and <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), is an issue of unusual significance. Sufficient evidence of this lies just in the comments on the issue that Members of this Court recently have made, <em>e. g., Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#415" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388, 415</a></span> (1971) (Burger, C. J., dissenting); <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#490" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 490</a></span> (1971) (Harlan, J., concurring); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#502" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 502</a></span> (Black, J., dissenting); <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#537" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 537-539</a></span> (White, J., dissenting); <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#413" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387, 413-414</a></span> (1977) (Powell, J., concurring); <em>Robbins </em>v. <em>California, </em><span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#437" aria-description="Citation for case: Robbins v. California">453 U. S. 420, 437, 443-444</a></span> (1981) (Rehnquist, J., dissenting). Where difficult issues of great public importance are involved, there are strong reasons to adhere scrupulously to the customary limitations on our discretion. By doing so we “promote respect... for the Court’s adjudicatory process [and] the stability of [our] decisions.” <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#677" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 677</a></span> (Harlan, J., dissenting). Moreover, fidelity to the rule guarantees that a factual record will be available to us, thereby discouraging the framing of broad rules, seemingly sensible on one set of facts, which may prove ill-considered in other circumstances. In Justice Harlan’s words, adherence to the rule lessens the threat of “untoward practical ramifications,” <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#676" aria-description="Citation for case: Mapp v. Ohio"><em>id., </em>at 676</a></span> (dissenting opinion), not foreseen at the time of decision. The public importance of our decisions in <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>and <em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span> </em>and the emotions engendered by the debate surrounding these decisions counsel that we meticulously observe our customary procedural rules. By following this course, we promote respect for the procedures by which our decisions are rendered, as well as confidence in the stability of prior decisions. A wise exercise of the powers confided in this Court dictates that we reserve for another day the question whether the exclusionary rule should be modified.</p>
<p id="AcZz"><page-number citation-index="1" label="225">*225</page-number>l-H H — (</p>
<p id="Aao">We now turn to the question presented in the State’s original petition for certiorari, which requires us to decide whether respondents’ rights under the Fourth and Fourteenth Amendments were violated by the search of their car and house. A chronological statement of events usefully introduces the issues at stake. Bloomingdale, Ill., is a suburb of Chicago located in Du Page County. On May 3, 1978, the Bloomingdale Police Department received by mail an anonymous handwritten letter which read as follows:</p>
<blockquote id="AAU">“This letter is to inform you that you have a couple in your town who strictly make their living on selling drugs. They are Sue and Lance Gates, they live on Greenway, off Bloomingdale Rd. in the condominiums. Most of their buys are done in Florida. Sue his wife drives their car to Florida, where she leaves it to be loaded up with drugs, then Lance flys down and drives it back. Sue flys back after she drops the car off in Florida. May 3 she is driving down there again and Lance will be flying down in a few days to drive it back. At the time Lance drives the car back he has the trunk loaded with over $100,000.00 in drugs. Presently they have over $100,000.00 worth of drugs in their basement.</blockquote>
<blockquote id="A-m">“They brag about the fact they never have to work, and make their entire living on pushers.</blockquote>
<blockquote id="AJ_">“I guarantee if you watch them carefully you will make a big catch. They are friends with some big drugs dealers, who visit their house often.</blockquote>
<blockquote id="AHsi">“Lance &amp; Susan Gates</blockquote>
<blockquote id="AIH">“Greenway</blockquote>
<blockquote id="AygP">“in Condominiums”</blockquote>
<p id="Aml">The letter was referred by the Chief of Police of the Bloomingdale Police Department to Detective Mader, who decided to pursue the tip. Mader learned, from the office of the Illinois Secretary of State, that an Illinois driver’s license had <page-number citation-index="1" label="226">*226</page-number>been issued to one Lance Gates, residing at a stated address in Bloomingdale. He contacted a confidential informant, whose examination of certain financial records revealed a more recent address for the Gateses, and he also learned from a police officer assigned to O'Hare Airport that “L. Gates” had made a reservation on Eastern Airlines Flight 245 to West Palm Beach, Fla., scheduled to depart from Chicago on May 5 at 4:15 p. m.</p>
<p id="b270-5">Mader then made arrangements with an agent of the Drug Enforcement Administration for surveillance of the May 5 Eastern Airlines flight. The agent later reported to Mader that Gates had boarded the flight, and that federal agents in Florida had observed him arrive in West Palm Beach and take a taxi to the nearby Holiday Inn. They also reported that Gates went to a room registered to one Susan Gates and that, at 7 o’clock the next morning, Gates and an unidentified woman left the motel in a Mercury bearing Illinois license plates and drove northbound on an interstate highway frequently used by travelers to the Chicago area. In addition, the DEA agent informed Mader that the license plate number on the Mercury was registered to a Hornet station wagon owned by Gates. The agent also advised Mader that the driving time between West Palm Beach and Bloomingdale was approximately 22 to 24 hours.</p>
<p id="b270-6">Mader signed an affidavit setting forth the foregoing facts, and submitted it to a judge of the Circuit Court of Du Page County, together with a copy of the anonymous letter. The judge of that court thereupon issued a search warrant for the Gateses' residence and for their automobile. The judge, in deciding to issue the warrant, could have determined that the <em>modus operandi of </em>the Gateses had been substantially corroborated. As the anonymous letter predicted, Lance Gates had flown from Chicago to West Palm Beach late in the afternoon of May 5th, had checked into a hotel room registered in the name of his wife, and, at 7 o’clock the following morning, had headed north, accompanied by an unidentified woman, <page-number citation-index="1" label="227">*227</page-number>out of West Palm Beach on an interstate highway used by travelers from South Florida to Chicago in an automobile bearing a license plate issued to him.</p>
<p id="b271-5">At 5:15 a. m. on March 7, only 36 hours after he had flown out of Chicago, Lance Gates, and his wife, returned to their home in Bloomingdale, driving the car in which they had left West Palm Beach some 22 hours earlier. The Bloomingdale police were awaiting them, searched the trunk of the Mercury, and uncovered approximately 350 pounds of marihuana. A search of the Gateses’ home revealed marihuana, weapons, and other contraband. The Illinois Circuit Court ordered suppression of all these items, on the ground that the affidavit submitted to the Circuit Judge failed to support the necessary determination of probable cause to believe that the Gateses’ automobile and home contained the contraband in question. This decision was affirmed in turn by the Illinois Appellate Court, <span class="citation" data-id="2151397"><a href="/opinion/2151397/people-v-gates/" aria-description="Citation for case: People v. Gates">82 Ill. App. 3d 749</a></span>, <span class="citation" data-id="2151397"><a href="/opinion/2151397/people-v-gates/" aria-description="Citation for case: People v. Gates">403 N. E. 2d 77</a></span> (1980), and by a divided vote of the Supreme Court of Illinois. <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/" aria-description="Citation for case: People of Illinois v. Gates">85 Ill. 2d 376</a></span>, <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d 887</a></span> (1981).</p>
<p id="b271-6">The Illinois Supreme Court concluded — and we are inclined to agree — that, standing alone, the anonymous letter sent to the Bloomingdale Police Department would not provide the basis for a magistrate’s determination that there was probable cause to believe contraband would be found in the Gateses’ car and home. The letter provides virtually nothing from which one might conclude that its author is either honest or his information reliable; likewise, the letter gives absolutely no indication of the basis for the writer’s predictions regarding the Gateses’ criminal activities. Something more was required, then, before a magistrate could conclude that there was probable cause to believe that contraband would be found in the Gateses’ home and car. See <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#109" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 109, n. 1</a></span>; <em>Nathanson </em>v. <em>United States, </em><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span> (1933).</p>
<p id="b271-7">The Illinois Supreme Court also properly recognized that Detective Mader’s affidavit might be capable of supplement<page-number citation-index="1" label="228">*228</page-number>ing the anonymous letter with information sufficient to permit a determination of probable cause. See <em>Whiteley </em>v. <em>Warden, </em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#567" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560, 567</a></span> (1971). In holding that the affidavit in fact did not contain sufficient additional information to sustain a determination of probable cause, the Illinois court applied a “two-pronged test,” derived from our decision in <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969).<footnotemark>3</footnotemark> The Illinois Supreme Court, like some others, apparently understood <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>as requiring that the anonymous letter satisfy each of two independent requirements before it could be relied on. <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#383" aria-description="Citation for case: People of Illinois v. Gates">85 Ill. 2d, at 383</a></span>, <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#890" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d, at 890</a></span>. According to this view, the letter, as supplemented by Mader’s affidavit, first had to adequately reveal the “basis of knowledge” of the letterwriter — the particular means by which he came by the information given in his report. Second, it had to pro<page-number citation-index="1" label="229">*229</page-number>vide facts sufficiently establishing either the “veracity” of the affiant’s informant, or, alternatively, the “reliability” of the informant’s report in this particular case.</p>
<p id="b273-5">The Illinois court, alluding to an elaborate set of legal rules that have developed among various lower courts to enforce the “two-pronged test,”<footnotemark>4</footnotemark> found that the test had not been satisfied. First, the “veracity” prong was not satisfied because, “[t]here was simply no basis [for] concluding] that the anonymous person [who wrote the letter to the Bloomingdale Police Department] was credible.” <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#385" aria-description="Citation for case: People of Illinois v. Gates"><em>Id., </em>at 385</a></span>, <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#891" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d, at 891</a></span>. The court indicated that corroboration by police of details contained in the letter might never satisfy the “veracity” prong, and in any event, could not do so if, as in the present case, only “innocent” details are corroborated. <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#390" aria-description="Citation for case: People of Illinois v. Gates"><em>Id., </em>at 390</a></span>, <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#893" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d, at 893</a></span>. In addition, the letter gave no indication of the basis of its writer’s knowledge of the <page-number citation-index="1" label="230">*230</page-number>Gateses’ activities. The Illinois court understood <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>as permitting the detail contained in a tip to be used to infer that the informant had a reliable basis for his statements, but it thought that the anonymous letter failed to provide sufficient detail to permit such an inference. Thus, it concluded that no showing of probable cause had been made.</p>
<p id="b274-5">We agree with the Illinois Supreme Court that an informant’s “veracity,” “reliability,” and “basis of knowledge” are all highly relevant in determining the value of his report. We do not agree, however, that these elements should be understood as entirely separate and independent requirements to be rigidly exacted in every case,<footnotemark>5</footnotemark> which the opinion of the Supreme Court of Illinois would imply. Rather, as detailed below, they should be understood simply as closely intertwined issues that may usefully illuminate the commonsense, practical question whether there is “probable cause” to believe that contraband or evidence is located in a particular place.</p>
<p id="b274-6">Ill</p>
<p id="b274-7">This totality-of-the-circumstances approach is far more consistent with our prior treatment of probable cause<footnotemark>6</footnotemark> than <page-number citation-index="1" label="231">*231</page-number>is any rigid demand that specific “tests” be satisfied by every informant’s tip. Perhaps the central teaching of our decisions bearing on the probable-cause standard is that it is a “practical, nontechnical conception.” <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949). “In dealing with probable cause, ... as the very name implies, we deal with probabilities. These are not technical; they are the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act.” <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States"><em>Id., </em>at 175</a></span>. Our observation in <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#418" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 418</a></span> (1981), regarding “particularized suspicion,” is also applicable to the probable-cause standard:</p>
<blockquote id="b275-5">“The process does not deal with hard certainties, but with probabilities. Long before the law of probabilities was articulated as such, practical people formulated certain common-sense conclusions about human behavior; jurors as factfinders are permitted to do the same — and <page-number citation-index="1" label="232">*232</page-number>so are law enforcement officers. Finally, the evidence thus collected must be seen and weighed not in terms of library analysis by scholars, but as understood by those versed in the field of law enforcement.”</blockquote>
<p id="b276-5">As these comments illustrate, probable cause is a fluid concept — turning on the assessment of probabilities in particular factual contexts — not readily, or even usefully, reduced to a neat set of legal rules. Informants’ tips doubtless come in many shapes and sizes from many different types of persons. As we said in <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#147" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 147</a></span> (1972): “Informants’ tips, like all other clues and evidence coming to a policeman on the scene, may vary greatly in their value and reliability.” Rigid legal rules are ill-suited to an area of such diversity. “One simple rule will not cover every situation.” <em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Ibid.</a></span></em><footnotemark><em>7</em></footnotemark></p>
<p id="b277-4"><page-number citation-index="1" label="233">*233</page-number>Moreover, the “two-pronged test” directs analysis into two largely independent channels — the informant’s “veracity” or “reliability” and his “basis of knowledge.” See nn. 4 and 5, <em>supra. </em>There are persuasive arguments against according these two elements such independent status. Instead, they are better understood as relevant considerations in the totality-of-the-circumstances analysis that traditionally has guided probable-cause determinations: a deficiency in one may be compensated for, in determining the overall reliability of a tip, by a strong showing as to the other, or by some other indicia of reliability. See, <em>e. g., Adams </em>v. <em>Williams, supra, </em>at 146-147; <em>United States </em>v. <em>Harris, </em><span class="citation" data-id="9883118"><a href="/opinion/108379/united-states-v-harris/" aria-description="Citation for case: United States v. Harris">403 U. S. 573</a></span> (1971).</p>
<p id="b277-5">If, for example, a particular informant is known for the unusual reliability of his predictions of certain types of criminal activities in a locality, his failure, in a particular case, to thoroughly set forth the basis of his knowledge surely should not serve as an absolute bar to a finding of probable cause based on his tip. See <em>United States </em>v. <em>Sellers, </em><span class="citation" data-id="312873"><a href="/opinion/312873/united-states-v-charles-e-sellers-jr/" aria-description="Citation for case: United States v. Charles E. Sellers, Jr.">483 F. 2d 37</a></span> (CA5 1973).<footnotemark>8</footnotemark> Likewise, if an unquestionably honest citizen comes forward with a report of criminal activity — which if fabricated would subject him to criminal liability — we have found <page-number citation-index="1" label="234">*234</page-number>rigorous scrutiny of the basis of his knowledge unnecessary. <em>Adams </em>v. <em>Williams, supra. </em>Conversely, even if we entertain some doubt as to an informant’s motives, his explicit and detailed description of alleged wrongdoing, along with a statement that the event was observed firsthand, entitles his tip to greater weight than might otherwise be the case. Unlike a totality-of-the-circumstances analysis, which permits a balanced assessment of the relative weights of all the various indicia of reliability (and unreliability) attending an informant’s tip, the “two-pronged test” has encouraged an excessively technical dissection of informants’ tips,<footnotemark>9</footnotemark> with undue at<page-number citation-index="1" label="235">*235</page-number>tention being focused on isolated issues that cannot sensibly be divorced from the other facts presented to the magistrate.</p>
<p id="b279-4">As early as <em>Locke </em>v. <em>United States, </em><span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/#348" aria-description="Citation for case: Locke v. United States">7 Cranch 339, 348</a></span> (1813), Chief Justice Marshall observed, in a closely related context: “[T]he term ‘probable cause,’ according to its usual acceptation, means less than evidence which would justify condemnation .... It imports a seizure made under circumstances which warrant suspicion.” More recently, we said that “the <em>quanta </em>... of proof” appropriate in ordinary judicial proceedings are inapplicable to the decision to issue a warrant. <em>Brinegar, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#173" aria-description="Citation for case: Brinegar v. United States">338 U. S., at 173</a></span>. Finely tuned standards such as proof beyond a reasonable doubt or by a preponderance of the evidence, useful in formal trials, have no place in the magistrate’s decision. While an effort to fix some general, numerically precise degree of certainty corresponding to “probable cause” may not be helpful, it is clear that “only the probability, and not a prima facie showing, of criminal activity is the standard of probable cause.” <em>Spinelli, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#419" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 419</a></span>. See Model Code of Pre-Arraignment Procedure §210.1(7) (Prop. Off. Draft 1972); 1 W. LaFave, Search and Seizure § 3.2(e) (1978).</p>
<p id="b279-5">We also have recognized that affidavits “are normally drafted by nonlawyers in the midst and haste of a criminal investigation. Technical requirements of elaborate specificity once exacted under common law pleadings have no proper place in this area.” <em>United States </em>v. <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 108</a></span> (1965). Likewise, search and arrest warrants long have been issued by persons who are neither lawyers nor judges, and who certainly do not remain abreast of each judicial refinement of the nature of “probable cause.” See <em>Shadwick </em>v. <em>City of Tampa, </em><span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/#348" aria-description="Citation for case: Shadwick v. City of Tampa">407 U. S. 345, 348-350</a></span> (1972). The rigorous inquiry into the <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>prongs and the complex superstructure of evidentiary and analytical rules that some have seen implicit in our <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>decision, cannot be reconciled with the fact that many warrants are — quite properly, 407 U. S., at 348-350 — issued on the basis of nontechnical, <page-number citation-index="1" label="236">*236</page-number>common-sense judgments of laymen applying a standard less demanding than those used in more formal legal proceedings. Likewise, given the informal, often hurried context in which it must be applied, the “built-in subtleties,” <em>Stanley </em>v. <em>State, </em><span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#528" aria-description="Citation for case: Stanley v. State">19 Md. App. 507, 528</a></span>, <span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#860" aria-description="Citation for case: Stanley v. State">313 A. 2d 847, 860</a></span> (1974), of the “two-pronged test” are particularly unlikely to assist magistrates in determining probable cause.</p>
<p id="b280-5">Similarly, we have repeatedly said that after-the-fact scrutiny by courts of the sufficiency of an affidavit should not take the form of <em>de novo </em>review. A magistrate's “determination of probable cause should be paid great deference by reviewing courts.” <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#419" aria-description="Citation for case: Spinelli v. United States"><em>Spinelli, supra, </em>at 419</a></span>. “A grudging or negative attitude by reviewing courts toward warrants,” <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S., at 108</a></span>, is inconsistent with the Fourth Amendment’s strong preference for searches conducted pursuant to a warrant; “courts should not invalidate warrants] by interpreting affidavits] in a hypertechnical, rather than a commonsense, manner.” <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#109" aria-description="Citation for case: United States v. Ventresca"><em>Id., </em>at 109</a></span>.</p>
<p id="b280-6">If the affidavits submitted by police officers are subjected to the type of scrutiny some courts have deemed appropriate, police might well resort to warrantless searches, with the hope of relying on consent or some other exception to the Warrant Clause that might develop at the time of the search. In addition, the possession of a warrant by officers conducting an arrest or search greatly reduces the perception of unlawful or intrusive police conduct, by assuring “the individual whose property is searched or seized of the lawful authority of the executing officer, his need to search, and the limits of his power to search.” <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 9</a></span> (1977). Reflecting this preference for the warrant process, the traditional standard for review of an issuing magistrate’s probable-cause determination has been that so long as the magistrate had a “substantial basis for . . . concluding]” that a search would uncover evidence of wrongdoing, the Fourth Amendment requires no more. <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 271</a></span> (1960). See <em>United States </em>v. <page-number citation-index="1" label="237">*237</page-number><em>Harris, </em><span class="citation" data-id="9883118"><a href="/opinion/108379/united-states-v-harris/#577" aria-description="Citation for case: United States v. Harris">403 U. S., at 577-583</a></span>.<footnotemark>10</footnotemark> We think reaffirmation of this standard better serves the purpose of encouraging recourse to the warrant procedure and is more consistent with our traditional deference to the probable-cause determinations of magistrates than is the “two-pronged test.”</p>
<p id="b281-5">Finally, the direction taken by decisions following <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>poorly serves “[t]he most basic function of any government”: “to provide for the security of the individual and of his property.” <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#539" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 539</a></span> (1966) (White, J., dissenting). The strictures that inevitably accompany the “two-pronged test” cannot avoid seriously impeding the task of law enforcement, see, <em>e. g., </em>n. 9, <em>supra. </em>If, as the Illinois Supreme Court apparently thought, that test must be rigorously applied in every case, anonymous tips would be of greatly diminished value in police work. Ordinary citizens, like ordinary witnesses, see Advisory Committee’s Notes on Fed. Rule Evid. 701, 28 U. S. C. App., p. 570, generally do not provide extensive recitations of the basis of their everyday observations. Likewise, as the Illinois Supreme Court observed in this case, the veracity of persons supplying anonymous tips is by hypothesis largely unknown, and unknowable. As a result, anonymous tips seldom could survive a rigorous application of either of the <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>prongs. Yet, such tips, particularly when supplemented by <page-number citation-index="1" label="238">*238</page-number>independent police investigation, frequently contribute to the solution of otherwise “perfect crimes.” While a conscientious assessment of the basis for crediting such tips is required by the Fourth Amendment, a standard that leaves virtually no place for anonymous citizen informants is not.</p>
<p id="b282-5">For all these reasons, we conclude that it is wiser to abandon the “two-pronged test” established by our decisions in <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span> </em>and Spinelli.<footnotemark>11</footnotemark> In its place we reaffirm the totality-of-the-circumstances analysis that traditionally has informed probable-cause determinations. See <em>Jones </em>v. <em>United States, supra; United States </em>v. <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102</a></span> (1965); <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949). The task of the issuing magistrate is simply to make a practical, commonsense decision whether, given all the circumstances set forth in the affidavit before him, including the “veracity” and “basis of knowledge” of persons supplying hearsay information, there is a fair probability that contraband or evidence of a crime will be found in a particular place. And the duty of a reviewing court is simply to ensure that the magistrate had a “substantial basis for . . . concluding]” that probable cause <page-number citation-index="1" label="239">*239</page-number>existed. <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States">362 U. S., at 271</a></span>. We are convinced that this flexible, easily applied standard will better achieve the accommodation of public and private interests that the Fourth Amendment requires than does the approach that has developed from <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span> </em>and <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>.</em></p>
<p id="b283-5">Our earlier cases illustrate the limits beyond which a magistrate may not venture in issuing a warrant. A sworn statement of an affiant that “he has cause to suspect and does believe” that liquor illegally brought into the United States is located on certain premises will not do. <em>Nathanson </em>v. <em>United States, </em><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span> (1933). An affidavit must provide the magistrate with a substantial basis for determining the existence of probable cause, and the wholly conclusory statement at issue in <em><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span> </em>failed to meet this requirement. An officer’s statement that “[a]ffiants have received reliable information from a credible person and do believe” that heroin is stored in a home, is likewise inadequate. <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964). As in <em><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span>, </em>this is a mere conclusory statement that gives the magistrate virtually no basis at all for making a judgment regarding probable cause. Sufficient information must be presented to the magistrate to allow that official to determine probable cause; his action cannot be a mere ratification of the bare conclusions of others. In order to ensure that such an abdication of the magistrate’s duty does not occur, courts must continue to conscientiously review the sufficiency of affidavits on which warrants are issued. But when we move beyond the “bare bones” affidavits present in cases such as <em><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span> </em>and <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>, </em>this area simply does not lend itself to a prescribed set of rules, like that which had developed from <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>. </em>Instead, the flexible, common-sense standard articulated in <em>Jones, Ventresca, </em>and <em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span> </em>better serves the purposes of the Fourth Amendment’s probable-cause requirement.</p>
<p id="b283-6">Justice Brennan’s dissent suggests in several places that the approach we take today somehow downgrades the <page-number citation-index="1" label="240">*240</page-number>role of the neutral magistrate, because <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span> </em>and <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>“preserve the role of magistrates as independent arbiters of probable cause . . . <em>Post, </em>at 287. Quite the contrary, we believe, is the case. The essential protection of the warrant requirement of the Fourth Amendment, as stated in <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948), is in “requiring that [the usual inferences which reasonable men draw from evidence] be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime.” <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States"><em>Id., </em>at 13-14</a></span>. Nothing in our opinion in any way lessens the authority of the magistrate to draw such reasonable inferences as he will from the material supplied to him by applicants for a warrant; indeed, he is freer than under the regime of <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span> </em>and <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>to draw such inferences, or to refuse to draw them if he is so minded.</p>
<p id="b284-6">The real gist of Justice Brennan’s criticism seems to be a second argument, somewhat at odds with the first, that magistrates should be restricted in their authority to make probable-cause determinations by the standards laid down in Aguilar and <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>, </em>and that such findings “should not be authorized unless there is some assurance that the information on which they are based has been obtained in a reliable way by an honest or credible person.” <em>Post, </em>at 283. However, under our opinion magistrates remain perfectly free to exact such assurances as they deem necessary, as well as those required by this opinion, in making probable-cause determinations. Justice Brennan would apparently prefer that magistrates be restricted in their findings of probable cause by the development of an elaborate body of case law dealing with the “veracity” prong of the <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>test, which in turn is broken down into two “spurs” — the informant’s “credibility” and the “reliability” of his information, together with the “basis of knowledge” prong of the <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>test. See n. 4, <em>supra. </em>That such a labyrinthine body of judicial refinement bears any relationship to familiar definitions of <page-number citation-index="1" label="241">*241</page-number>probable cause is hard to imagine. As previously noted, probable cause deals “with probabilities. These are not technical; they are the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act <em>"Brinegar v. United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S., at 175</a></span>.</p>
<p id="b285-5">Justice Brennan’s dissent also suggests that “[w]ords such as ‘practical,’ ‘nontechnical,’ and ‘common sense,’ as used in the Court’s opinion, are but code words for an overly permissive attitude towards police practices in derogation of the rights secured by the Fourth Amendment.” <em>Post, </em>at 290. An easy, but not a complete, answer to this rather florid statement would be that nothing we know about Justice Rutledge suggests that he would have used the words he chose in <em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span> </em>in such a manner. More fundamentally, no one doubts that “under our Constitution only measures consistent with the Fourth Amendment may be employed by government to cure [the horrors of drug trafficking],” <em>post, </em>at 290; but this agreement does not advance the inquiry as to which measures are, and which measures are not, consistent with the Fourth Amendment. “Fidelity” to the commands of the Constitution suggests balanced judgment rather than exhortation. The highest “fidelity” is not achieved by the judge who instinctively goes furthest in upholding even the most bizarre claim of individual constitutional rights, any more than it is achieved by a judge who instinctively goes furthest in accepting the most restrictive claims of governmental authorities. The task of this Court, as of other courts, is to “hold the balance true,” and we think we have done that in this case.</p>
<p id="b285-6">IV</p>
<p id="b285-7">Our decisions applying the totality-of-the-circumstances analysis outlined above have consistently recognized the value of corroboration of details of an informant’s tip by independent police work. In <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#269" aria-description="Citation for case: Jones v. United States">362 U. S., at 269</a></span>, we held that an affidavit relying on hearsay “is not to <page-number citation-index="1" label="242">*242</page-number>be deemed insufficient on that score, so long as a substantial basis for crediting the hearsay is presented.” We went on to say that even in making a warrantless arrest an officer “may rely upon information received through an informant, rather than upon his direct observations, so long as the informant’s statement is reasonably corroborated by other matters within the officer’s knowledge.” <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Ibid.</a></span> </em>Likewise, we recognized the probative value of corroborative efforts of police officials in <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span> </em>— the source of the “two-pronged test” — by observing that if the police had made some effort to corroborate the informant’s report at issue, “an entirely different case” would have been presented. <em>Aguilar, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#109" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 109, n. 1</a></span>.</p>
<p id="b286-5">Our decision in <em>Draper </em>v. <em>United States, </em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959), however, is the classic case on the value of corroborative efforts of police officials. There, an informant named Hereford reported that Draper would arrive in Denver on a train from Chicago on one of two days, and that he would be carrying a quantity of heroin. The informant also supplied a fairly detailed physical description of Draper, and predicted that he would be wearing a light colored raincoat, brown slacks, and black shoes, and would be walking “real fast.” <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#309" aria-description="Citation for case: Draper v. United States"><em>Id., </em>at 309</a></span>. Hereford gave no indication of the basis for his information.<footnotemark>12</footnotemark></p>
<p id="b286-6">On one of the stated dates police officers observed a man matching this description exit a train arriving from Chicago; his attire and luggage matched Hereford’s report and he was <page-number citation-index="1" label="243">*243</page-number>walking rapidly. We explained in <em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span> </em>that, by this point in his investigation, the arresting officer “had personally verified every facet of the information given him by Hereford except whether petitioner had accomplished his mission and had the three ounces of heroin on his person or in his bag. And surely, with every other bit of Hereford’s information being thus personally verified, [the officer] had ‘reasonable grounds’ to believe that the remaining unverified bit of Hereford’s information — that Draper would have the heroin with him — was likewise true,” <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#313" aria-description="Citation for case: Draper v. United States"><em>id., </em>at 313</a></span>.</p>
<p id="b287-5">The showing of probable cause in the present case was fully as compelling as that in <em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span>. </em>Even standing alone, the facts obtained through the independent investigation of Mader and the DEA at least suggested that the Gateses were involved in drug trafficking. In addition to being a popular vacation site, Florida is well known as a source of narcotics and other illegal drugs. See <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#562" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 562</a></span> (1980) (Powell, J., concurring in part and concurring in judgment); DEA, Narcotics Intelligence Estimate, The Supply of Drugs to the U. S. Illicit Market From Foreign and Domestic Sources in 1980, pp. 8-9. Lance Gates’ flight to West Palm Beach, his brief, overnight stay in a motel, and apparent immediate return north to Chicago in the family car, conveniently awaiting him in West Palm Beach, is as suggestive of a prearranged drug run, as it is of an ordinary vacation trip.</p>
<p id="b287-6">In addition, the judge could rely on the anonymous letter, which had been corroborated in major part by Mader's efforts — just as had occurred in <em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span>.</em><footnotemark><em>13</em></footnotemark><em> </em>The Supreme Court <page-number citation-index="1" label="244">*244</page-number>of Illinois reasoned that <em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span> </em>involved an informant who had given reliable information on previous occasions, while the honesty and reliability of the anonymous informant in this case were unknown to the Bloomingdale police. While this distinction might be an apt one at the time the Police Department received the anonymous letter, it became far less significant after Mader’s independent investigative work occurred. The corroboration of the letter’s predictions that the Gateses’ car would be in Florida, that Lance Gates would fly to Florida in the next day or so, and that he would drive the car north toward Bloomingdale all indicated, albeit not with certainty, that the informant’s other assertions also were true. “[Bjecause an informant is right about some things, he is more probably right about other facts,” <em>Spinelli, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#427" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 427</a></span> (White, J., concurring) — including the claim regarding the Gateses’ illegal activity. This may well not be the type of “reliability” or “veracity” necessary to satisfy some views of the “veracity prong” of <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>, </em>but we think it suffices for the practical, common-sense judgment called for in making a probable-cause determination. It is enough, for purposes of assessing probable cause, that “[corroboration through other sources of information reduced the <page-number citation-index="1" label="245">*245</page-number>chances of a reckless or prevaricating tale,” thus providing “a substantial basis for crediting the hearsay.” <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#269" aria-description="Citation for case: Jones v. United States">362 U. S., at 269, 271</a></span>.</p>
<p id="b289-5">Finally, the anonymous letter contained a range of details relating not just to easily obtained facts and conditions existing at the time of the tip, but to future actions of third parties ordinarily not easily predicted. The letterwriter’s accurate information as to the travel plans of each of the Gateses was of a character likely obtained only from the Gateses themselves, or from someone familiar with their not entirely ordinary travel plans. If the informant had access to accurate information of this type a magistrate could properly conclude that it was not unlikely that he also had access to reliable information of the Gateses’ alleged illegal activities.<footnotemark>14</footnotemark> Of <page-number citation-index="1" label="246">*246</page-number>course, the Gateses’ travel plans might have been learned from a talkative neighbor or travel agent; under the “two-pronged test” developed from <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>, </em>the character of the details in the anonymous letter might well not permit a sufficiently clear inference regarding the letterwriter’s “basis of knowledge.” But, as discussed previously, <em>supra, </em>at 235, probable cause does not demand the certainty we associate with formal trials. It is enough that there was a fair probability that the writer of the anonymous letter had obtained his entire story either from the Gateses or someone they trusted. And corroboration of major portions of the letter’s predictions provides just this probability. It is apparent, therefore, that the judge issuing the warrant had a “substantial basis for . . . conclud[ing]” that probable cause to search the Gateses’ home and car existed. The judgment of the Supreme Court of Illinois therefore must be</p>
<p id="b290-4">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b262-8"> The apparent rule of <em>Crowell </em>v. <em><span class="citation no-link">Randell</span> </em>that a federal claim have been <em>both </em>raised and addressed in state court was generally not understood in the literal fashion in which it was phrased. See R. Robertson &amp; F. Kirkham, Jurisdiction of the Supreme Court of the United States § 60 (1951). Instead, the Court developed the rule that a claim would not be considered here unless it had been <em>either </em>raised or squarely considered and resolved in state court. See, <em>e. g., McGoldrick </em>v. <em>Compagnie Generale Transatlantique, </em><span class="citation" data-id="9419089"><a href="/opinion/103320/mcgoldrick-v-compagnie-generale-transatlantique/#434" aria-description="Citation for case: McGoldrick v. Compagnie Generale Transatlantique">309 U. S. 430, 434-435</a></span> (1940); <em>State Farm Mutual Ins. Co. </em>v. <em>Duel, </em><span class="citation" data-id="104087"><a href="/opinion/104087/state-farm-mutual-automobile-insurance-v-duel/#160" aria-description="Citation for case: State Farm Mutual Automobile Insurance v. Duel">324 U. S. 154, 160</a></span> (1945).</p>
</footnote>
<footnote label="2">
<p id="b264-6"> In <em><span class="citation" data-id="95004"><a href="/opinion/95004/dewey-v-des-moines/" aria-description="Citation for case: Dewey v. Des Moines">Dewey</a></span>, </em>certain assessments had been levied against the owner of property abutting a street paved by the city; a state trial court ordered that the property be forfeited when the assessments were not paid, and in addition, held the plaintiff in error personally liable for the amount by which the assessments exceeded the value of the lots. In state court the plaintiff in error argued that the imposition of personal liability against him violated the Due Process Clause of the Fourteenth Amendment, because he had not received personal notice of the assessment proceedings. In this Court, he also attempted to argue that the assessment itself constituted a taking under the Fourteenth Amendment. The Court held that, beyond arising from a single factual occurrence, the two claims “are not in anywise necessarily connected,” <span class="citation" data-id="95004"><a href="/opinion/95004/dewey-v-des-moines/#198" aria-description="Citation for case: Dewey v. Des Moines">173 U. S., at 198</a></span>. Because of this, we concluded that the plaintiff in error’s taking claim could not be considered.</p>
</footnote>
<footnote label="3">
<p id="b272-5"> In <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>, </em>police officers observed Mr. Spinelli going to and from a particular apartment, which the telephone company said contained two telephones with stated numbers. The officers also were “informed by a confidential reliable informant that William Spinelli [was engaging in illegal gambling activities]” at the apartment, and that he used two phones, with numbers corresponding to those possessed by the police. <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#414" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 414</a></span>. The officers submitted an affidavit with this information to a magistrate and obtained a warrant to search Spinelli’s apartment. We held that the magistrate could have made his determination of probable cause only by “abdicating his constitutional function,” <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#416" aria-description="Citation for case: Spinelli v. United States"><em>id., </em>at 416</a></span>. The Government’s affidavit contained absolutely no information regarding the informant’s reliability. Thus, it did not satisfy Aguilar*s requirement that such affidavits contain “some of the underlying circumstances” indicating that “the informant . . . was ‘credible’” or that “his information [was] ‘reliable.’” <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#114" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 114</a></span> (1964). In addition, the tip failed to satisfy <em>Aguilar’s </em>requirement that it detail “some of the underlying circumstances from which the informant concluded that. . . narcotics were where he claimed they were.” <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Ibid.</a></span> </em>We also held that if the tip concerning Spinelli had contained “sufficient detail” to permit the magistrate to conclude “that he [was] relying on something more substantial than a casual rumor circulating in the underworld or an accusation based merely on an individual’s general reputation,” <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#416" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 416</a></span>, then he properly could have relied on it; we thought, however, that the tip lacked the requisite detail to permit this “self-verifying detail” analysis.</p>
</footnote>
<footnote label="4">
<p id="b273-6"> See, <em>e. g., Stanley </em>v. <em>State, </em><span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/" aria-description="Citation for case: Stanley v. State">19 Md. App. 507</a></span>, <span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/" aria-description="Citation for case: Stanley v. State">313 A. 2d 847</a></span> (1974). In summary, these rules posit that the “veracity” prong of the <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>test has two “spurs” — the informant’s “credibility” and the “reliability” of his information. Various interpretations are advanced for the meaning of the “reliability” spur of the “veracity” prong. Both the “basis of knowledge” prong and the “veracity” prong are treated as entirely separate requirements, which must be independently satisfied in every case in order to sustain a determination of probable cause. See n. 5, <em>infra. </em>Some ancillary doctrines are relied on to satisfy certain of the foregoing requirements. For example, the “self-verifying detail” of a tip may satisfy the “basis of knowledge” requirement, although not the “credibility” spur of the “veracity” prong. See <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#388" aria-description="Citation for case: People of Illinois v. Gates">85 Ill. 2d, at 388</a></span>, <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#892" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d, at 892</a></span>. Conversely, corroboration would seem not capable of supporting the “basis of knowledge” prong, but only the “veracity” prong. <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#390" aria-description="Citation for case: People of Illinois v. Gates"><em>Id., </em>at 390</a></span>, <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#893" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d, at 893</a></span>.</p>
<p id="b273-7">The decision in <em><span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/" aria-description="Citation for case: Stanley v. State">Stanley</a></span>, </em>while expressly approving and conscientiously attempting to apply the “two-pronged test” observes that “[t]he built-in subtleties [of the test] are such, however, that a slipshod application calls down upon us the fury of Murphy’s Law.” <span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#528" aria-description="Citation for case: Stanley v. State">19 Md. App., at 528</a></span>, <span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#860" aria-description="Citation for case: Stanley v. State">313 A. 2d, at 860</a></span> (footnote omitted). The decision also suggested that it is necessary to “evolve analogous guidelines [to hearsay rules employed in trial settings] for the reception of hearsay in a probable cause setting.” <span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#522" aria-description="Citation for case: Stanley v. State"><em>Id., </em>at 522, n. 12</a></span>, <span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#857" aria-description="Citation for case: Stanley v. State">313 A. 2d, at 857, n. 12</a></span>.</p>
</footnote>
<footnote label="5">
<p id="b274-8"> The entirely independent character that the <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>prongs have assumed is indicated both by the opinion of the Illinois Supreme Court in this case, and by decisions of other courts. One frequently cited decision, <em>Stanley </em>v. <em>State, supra, </em>at 530, <span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#861" aria-description="Citation for case: Stanley v. State">313 A. 2d, at 861</a></span> (footnote omitted), remarks that “the dual requirements represented by the ‘two-pronged test’ are ‘analytically severable’ and an ‘overkill’ on one prong will not carry over to make up for a deficit on the other prong.” See also n. 9, <em>infra.</em></p>
</footnote>
<footnote label="6">
<p id="b274-9"> Our original phrasing of the so-called “two-pronged test” in <em>Aguilar </em>v. <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Texas, supra,</a></span> </em>suggests that the two prongs were intended simply as guides to a magistrate’s determination of probable cause, not as inflexible, independent requirements applicable in every case. In <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>, </em>we required only that</p>
<blockquote id="b274-10">“the magistrate must be informed of <em>some of the underlying circumstances </em>from which the informant concluded that . . . narcotics were where he claimed they were, and <em>some of the underlying circumstances </em>from which <page-number citation-index="1" label="231">*231</page-number>the officer concluded that the informant. . . was ‘credible’ or his information ‘reliable.’” <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#114" aria-description="Citation for case: Aguilar v. Texas"><em>Id., </em>at 114</a></span> (emphasis added).</blockquote>
<p id="b275-7">As our language indicates, we intended neither a rigid compartmentalization of the inquiries into an informant’s “veracity,” “reliability,” and “basis of knowledge,” nor that these inquiries be elaborate exegeses of an informant’s tip. Rather, we required only that some facts bearing on two particular issues be provided to the magistrate. Our decision in <em>Jaben </em>v. <em>United States, </em><span class="citation" data-id="9423037"><a href="/opinion/107058/jaben-v-united-states/" aria-description="Citation for case: Jaben v. United States">381 U. S. 214</a></span> (1965), demonstrated this latter point. We held there that a criminal complaint showed probable cause to believe the defendant had attempted to evade the payment of income taxes. We commented:</p>
<blockquote id="b275-8">“Obviously any reliance upon factual allegations necessarily entails some degree of reliability upon the credibility of the source.... Nor does it indicate that each factual allegation which the affiant puts forth must be independently documented, or that each and every fact which contributed to his conclusions be spelled out in the complaint. <em>. . . It simply requires that enough information be presented to the Commissioner to enable him to make the judgment that the charges are not capricious and are sufficiently supported to justify bringing into play the further steps of the criminal process.” Id., </em>at 224-225 (emphasis added).</blockquote>
</footnote>
<footnote label="7">
<p id="b276-6"> The diversity of informants’ tips, as well as the usefulness of the totality-of-the-circumstances approach to probable cause, is reflected in our prior decisions on the subject. In <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 271</a></span> (1960), we held that probable cause to search petitioners’ apartment was established by an affidavit based principally on an informant’s tip. The unnamed informant claimed to have purchased narcotics from petitioners at their apartment; the affiant stated that he had been given correct information from the informant on a prior occasion. This, and the fact that petitioners had admitted to police officers on another occasion that they were narcotics users, sufficed to support the magistrate’s determination of probable cause.</p>
<p id="b276-7">Likewise, in <em>Rugendorf v. United States, </em><span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">376 U. S. 528</a></span> (1964), the Court upheld a magistrate’s determination that there was probable cause to believe that certain stolen property would be found in petitioner’s apartment. The affidavit submitted to the magistrate stated that certain furs had been stolen, and that a confidential informant, who previously had furnished confidential information, said that he saw the furs in petitioner’s home. Moreover, another confidential informant, also claimed to be reliable, stated that one Schweihs had stolen the furs. Police reports indicated that petitioner had been seen in Schweihs’ company, and a third informant stated that petitioner was a fence for Schweihs.</p>
<p id="b276-8">Finally, in <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963), we held that information within the knowledge of officers who searched the Kers’ apartment provided them with probable cause to believe drugs would be found there. The officers were aware that one Murphy had previously sold marihuana <page-number citation-index="1" label="233">*233</page-number>to a police officer; the transaction had occurred in an isolated area, to which Murphy had led the police. The night after this transaction, police observed Mr. Ker and Murphy meet in the same location. Murphy approached Ker’s car, and, although police could see nothing change hands, Murphy’s <em>modus operandi </em>was identical to what it had been the night before. Moreover, when police followed Ker from the scene of the meeting with Murphy he managed to lose them after performing an abrupt U-turn. Finally, the police had a statement from an informant who had provided reliable information previously, that Ker was engaged in selling marihuana, and that his source was Murphy. We concluded that “[t]o say that this coincidence of information was sufficient to support a reasonable belief of the officers that Ker was illegally in possession of marijuana is to indulge in understatement.” <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#36" aria-description="Citation for case: Ker v. California"><em>Id., </em>at 36</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b277-7"> Compare <em>Stanley </em>v. <em>State, </em><span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#530" aria-description="Citation for case: Stanley v. State">19 Md. App., at 530</a></span>, <span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#861" aria-description="Citation for case: Stanley v. State">313 A. 2d, at 861</a></span>, reasoning that “[e]ven assuming ‘credibility’ amounting to sainthood, the judge still may not accept the bare conclusion ... of a sworn and known and trusted police-affiant.”</p>
</footnote>
<footnote label="9">
<p id="b278-5"> Some lower court decisions, brought to our attention by the State, reflect a rigid application of such rules. In <em>Bridger </em>v. <em>State, </em><span class="citation" data-id="2433225"><a href="/opinion/2433225/bridger-v-state/" aria-description="Citation for case: Bridger v. State">503 S. W. 2d 801</a></span> (Tex. Crim. App. 1974), .the affiant had received a confession of armed robbery from one of two suspects in the robbery; in addition, the suspect had given the officer $800 in cash stolen during the robbery. The suspect also told the officer that the gun used in the robbery was hidden in the other suspect’s apartment. A warrant issued on the basis of this was invalidated on the ground that the affidavit did not satisfactorily describe how the accomplice had obtained his information regarding the gun.</p>
<p id="b278-6">Likewise, in <em>People </em>v. <em>Palanza, </em><span class="citation" data-id="2023247"><a href="/opinion/2023247/people-v-palanza/" aria-description="Citation for case: People v. Palanza">55 Ill. App. 3d 1028</a></span>, <span class="citation" data-id="2023247"><a href="/opinion/2023247/people-v-palanza/" aria-description="Citation for case: People v. Palanza">371 N. E. 2d 687</a></span> (1978), the affidavit submitted in support of an application for a search warrant stated that an informant of proven and uncontested reliability had seen, in specifically described premises, “a quantity of a white crystalline substance which was represented to the informant by a white male occupant of the premises to be cocaine. Informant has observed cocaine on numerous occasions in the past and is thoroughly familiar with its appearance. The informant states that the white crystalline powder he observed in the above described premises appeared to him to be cocaine.” <span class="citation" data-id="2023247"><a href="/opinion/2023247/people-v-palanza/#1029" aria-description="Citation for case: People v. Palanza"><em>Id., </em>at 1029</a></span>, 371N. E. 2d, at 688. The warrant issued on the basis of the affidavit was invalidated because “[t]here is no indication as to how the informant or for that matter any other person could tell whether a white substance was cocaine and not some other substance such as sugar or salt.” <span class="citation" data-id="2023247"><a href="/opinion/2023247/people-v-palanza/#1030" aria-description="Citation for case: People v. Palanza"><em>Id., </em>at 1030</a></span>, <span class="citation" data-id="2023247"><a href="/opinion/2023247/people-v-palanza/#689" aria-description="Citation for case: People v. Palanza">371 N. E. 2d, at 689</a></span>.</p>
<p id="b278-7">Finally, in <em>People </em>v. <em>Brethauer, </em><span class="citation" data-id="9532437"><a href="/opinion/1123854/people-v-brethauer/" aria-description="Citation for case: People v. Brethauer">174 Colo. 29</a></span>, <span class="citation" data-id="9532437"><a href="/opinion/1123854/people-v-brethauer/" aria-description="Citation for case: People v. Brethauer">482 P. 2d 369</a></span> (1971), an informant, stated to have supplied reliable information in the past, claimed that L. S. D. and marihuana were located on certain premises. The informant supplied police with drugs, which were tested by police and confirmed to be illegal substances. The affidavit setting forth these, and other, facts was found defective under both prongs of <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>.</em></p>
</footnote>
<footnote label="10">
<p id="b281-6"> We also have said that “[a]lthough in a particular case it may not be easy to determine when an affidavit demonstrates the existence of probable cause, the resolution of doubtful or marginal cases in this area should be largely determined by the preference to be accorded to warrants,” <em>United States </em>v. <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#109" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 109</a></span> (1965). This reflects both a desire to encourage use of the warrant process by police officers and a recognition that once a warrant has been obtained, intrusion upon interests protected by the Fourth Amendment is less severe than otherwise may be the case. Even if we were to accept the premise that the accurate assessment of probable cause would be furthered by the “two-pronged test,” which we do not, these Fourth Amendment policies would require a less rigorous standard than that which appears to have been read into <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span> </em>and <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>.</em></p>
</footnote>
<footnote label="11">
<p id="b282-6"> The Court’s decision in <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>has been the subject of considerable criticism, both by Members of this Court and others. Justice Blackmun, concurring in <em>United States </em>v. <em>Harris, </em><span class="citation" data-id="9883118"><a href="/opinion/108379/united-states-v-harris/#585" aria-description="Citation for case: United States v. Harris">403 U. S. 573, 585-586</a></span> (1971), noted his long-held view “that <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> . . </em>. was wrongly decided” by this Court. Justice Black similarly would have overruled that decision. <em>Id., </em>at 585. Likewise, a noted commentator has observed that “[t]he <em>Aguilar-Spinelli </em>formulation has provoked apparently ceaseless litigation.” 8A J. Moore, Moore’s Federal Practice ¶ 41.04, p. 41-43 (1982).</p>
<p id="b282-7">Whether the allegations submitted to the magistrate in <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>would, under the view we now take, have supported a finding of probable cause, we think it would not be profitable to decide. There are so many variables in the probable-cause equation that one determination will seldom be a useful “precedent” for another. Suffice it to say that while we in no way abandon Spinelli’s concern for the trustworthiness of informers and for the principle that it is the magistrate who must ultimately make a finding of probable cause, we reject the rigid categorization suggested by some of its language.</p>
</footnote>
<footnote label="12">
<p id="b286-7"> The tip in <em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span> </em>might well not have survived the rigid application of the “two-pronged test” that developed following <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>. </em>The only reference to Hereford’s reliability was that he had “been engaged as a ‘special employee’ of the Bureau of Narcotics at Denver for about six months, and from time to time gave information to [the police for] small sums of money, and that [the officer] had always found the information given by Hereford to be accurate and reliable.” <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#309" aria-description="Citation for case: Draper v. United States">358 U. S., at 309</a></span>. Likewise, the tip gave no indication of how Hereford came by his information. At most, the detailed and accurate predictions in the tip indicated that, however Hereford obtained his information, it was reliable.</p>
</footnote>
<footnote label="13">
<p id="b287-7"> The Illinois Supreme Court thought that the verification of details contained in the anonymous letter in this case amounted only to “[t]he corroboration of innocent activity,” <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#390" aria-description="Citation for case: People of Illinois v. Gates">85 Ill. 2d 376, 390</a></span>, <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#893" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d 887, 893</a></span> (1981), and that this was insufficient to support a finding of probable cause. We are inclined to agree, however, with the observation of Justice Moran in his dissenting opinion that “[i]n this case, just as in <em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span>, </em>seemingly innocent activity became suspicious in light of the initial tip.” <em>Id.., </em>at 396, <page-number citation-index="1" label="244">*244</page-number><span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#896" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d, at 896</a></span>. And it bears noting that <em>all </em>of the corroborating detail established in <em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span> </em>was of entirely innocent activity — a fact later pointed out by the Court in both <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#269" aria-description="Citation for case: Jones v. United States">362 U. S., at 269-270</a></span>, and <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#36" aria-description="Citation for case: Ker v. California">374 U. S., at 36</a></span>.</p>
<p id="b288-6">This is perfectly reasonable. As discussed previously, probable cause requires only a probability or substantial chance of criminal activity, not an actual showing of such activity. By hypothesis, therefore, innocent behavior frequently will provide the basis for a showing of probable cause; to require otherwise would be to <em>sub silentio </em>impose a drastically more rigorous definition of probable cause than the security of our citizens’ demands. We think the Illinois court attempted a too rigid classification of the types of conduct that may be relied upon in seeking to demonstrate probable cause. See <em>Brown </em>v. <em>Texas, </em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#52" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 52, n. 2</a></span> (1979). In making a determination of probable cause the relevant inquiry is not whether particular conduct is “innocent” or “guilty,” but the degree of suspicion that attaches to particular types of noncriminal acts.</p>
</footnote>
<footnote label="14">
<p id="b289-6"> Justice Stevens’ dissent seizes on one inaccuracy in the anonymous informant’s letter — its statement that Sue Gates would fly from Florida to Illinois, when in fact she drove — and argues that the probative value of the entire tip was undermined by this allegedly “material mistake.” We have never required that informants used by the police be infallible, and can see no reason to impose such a requirement in this case. Probable cause, particularly when police have obtained a warrant, simply does not require the perfection the dissent finds necessary.</p>
<p id="b289-7">Likewise, there is no force to the dissent’s argument that the Gateses’ action in leaving their home unguarded undercut the informant’s claim that drugs were hidden there. Indeed, the line-by-line scrutiny that the dissent applies to the anonymous letter is akin to that which we find inappropriate in reviewing magistrates’ decisions. The dissent apparently attributes to the judge who issued the warrant in this case the rather implausible notion that persons dealing in drugs always stay at home, apparently out of fear that to leave might risk intrusion by criminals. If accurate, one could not help sympathizing with the self-imposed isolation of people so situated. In reality, however, it is scarcely likely that the judge ever thought that the anonymous tip “kept one spouse” at home, much less that he relied on the theory advanced by the dissent. The letter simply says that Sue would fly from Florida to Illinois, without indicating whether the Gateses made the bitter choice of leaving the drugs in their house, or those in their car, unguarded. The judge’s determination that there might be drugs or evidence of criminal activity in the Gateses’ home was well supported by the less speculative theory, noted in text, that if the informant <page-number citation-index="1" label="246">*246</page-number>could predict with considerable accuracy the somewhat unusual travel plans of the Gateses, he probably also had a reliable basis for his statements that the Gateses kept a large quantity of drugs in their home and frequently were visited by other drug traffickers there.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Illinois v. McArthur.md  (`case`, 5 assertions)

### content_page

```
---
title: "Illinois v. McArthur"
type: case
citation: "531 U.S. 326 (2001)"
parallel_cite: "121 S. Ct. 946; 148 L. Ed. 2d 838"
neutral_cite: "2001 U.S. LEXIS 962; 1 Cal. Daily Op. Serv. 1442"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2001
date_decided: 2001-02-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2001-02-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Illinois v. McArthur
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118405/illinois-v-mcarthur/"
  cluster_id: 118405
  opinion_id: 118405
  identity_checked: true
homes:
  - page: "[[Securing the Scene]]"
    role: "Key — Anchor"
related: ["[[Michigan v. Summers]]", "[[Segura v. United States]]", "[[Bailey v. United States]]", "[[Welsh v. Wisconsin]]"]
aliases: []
tags: ["case", "fourth-amendment", "securing-the-scene", "temporary-seizure", "exigent-circumstances", "warrant"]
holding: "Where police have probable cause to believe a home contains contraband, they may reasonably impose a temporary restraint on a resident —…"
lake:
  record_id: Illinois v. McArthur
  status: verified
  projected_at: 2026-07-09
---

# Illinois v. McArthur

*531 U.S. 326 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
While police helped Tera McArthur remove her belongings from the trailer she shared with her husband, she told officers he had marijuana inside. When Charles McArthur refused consent to a search, an officer prevented him from re-entering the trailer unaccompanied while another officer left to obtain a warrant; for about two hours McArthur was allowed inside only with an officer observing. A warrant issued, the search found marijuana and a pipe, and McArthur moved to suppress the temporary restraint as unreasonable.

## Issue
Whether police with probable cause may temporarily prevent a resident from entering his home unaccompanied, to avoid the destruction of evidence, while they diligently obtain a search warrant.

## Rule
Yes, on these combined circumstances. "We conclude that the restriction at issue was reasonable, and hence lawful, in light of the following circumstances, which we consider in combination." — 531 U.S. at 331. ^pin-331

The Court considered: probable cause to believe the home held contraband; good reason to fear the evidence would be destroyed; police efforts to reconcile law-enforcement needs with privacy by imposing only a restraint rather than searching; and a limited duration.

"We have found no case in which this Court has held unlawful a temporary seizure that was supported by probable cause and was designed to prevent the loss of evidence while the police diligently obtained a warrant in a reasonable period of time." — [*Id.* at 334](https://www.courtlistener.com/opinion/118405/illinois-v-mcarthur/#:~:text=We%20have%20found%20no%20case). ^pin-334

## Application
The officers had probable cause from Tera McArthur's reliable, firsthand report; good reason to fear McArthur would destroy the marijuana if left alone inside; and they imposed only a limited restraint — keeping him from entering unaccompanied — rather than searching without a warrant. The restraint lasted only about two hours while an officer diligently obtained the warrant. Considered together, these circumstances made the temporary restriction reasonable.

## Conclusion
The temporary restraint pending the warrant was reasonable; the evidence was admissible and the suppression reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *McArthur* extends the scene-securing logic of [[Michigan v. Summers]] and [[Segura v. United States]] to a brief, probable-cause-based restraint on a resident pending a warrant; it is distinguished from [[Welsh v. Wisconsin]] (warrantless home entry for a nonjailable offense).

## Appears on
- [[Securing the Scene]] — *Key — Anchor*

## Sources
- *Illinois v. McArthur*, 531 U.S. 326 (2001) — https://www.courtlistener.com/opinion/118405/illinois-v-mcarthur/ — pinpoints: 331, 334.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8e02e456008654fe", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "531 U.S. 326 (2001)", "court": "U.S. Supreme Court", "neutral_cite": "2001 U.S. LEXIS 962; 1 Cal. Daily Op. Serv. 1442", "official_citation_present": true, "parallel_cite": "121 S. Ct. 946; 148 L. Ed. 2d 838", "title": "Illinois v. McArthur", "year": "2001"}}
{"assertion_id": "44f53640a437c918", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Where police have probable cause to believe a home contains contraband, they may reasonably impose a temporary restraint on a resident —…", "title": "Illinois v. McArthur"}}
{"assertion_id": "fa2d041aefcbcebc", "dimension": "support", "kind": "home_role", "locator": {"home": "Securing the Scene"}, "payload": {"home": "Securing the Scene", "role": "Key — Anchor", "title": "Illinois v. McArthur"}}
{"assertion_id": "3c884ee8ad79f69d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2001-02-20", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Illinois v. McArthur", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Illinois v. McArthur", "varies_by_point": "false"}}
{"assertion_id": "f0ee7dd7e6269fb9", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Illinois v. McArthur"}}
```

### lake record — Illinois v. McArthur

```json
{
  "schema_version": "s2.v1",
  "record_id": "Illinois v. McArthur",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Illinois v. McArthur",
    "case_name_short": "McArthur",
    "case_name_full": "ILLINOIS v. McARTHUR",
    "input_case_name": "Illinois v. McArthur",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2001-02-20",
    "year": 2001,
    "docket": null,
    "cluster_id": 118405,
    "lead_opinion_id": 118405,
    "sibling_ids": [
      118405,
      9434039,
      9434040,
      9434041
    ],
    "absolute_url": "/opinion/118405/illinois-v-mcarthur/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "531 U.S. 326",
      "volume": "531",
      "reporter": "U.S.",
      "page": "326",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "121 S. Ct. 946",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "946",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "148 L. Ed. 2d 838",
        "volume": "148",
        "reporter": "L. Ed. 2d",
        "page": "838",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2001 U.S. LEXIS 962",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "962",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1 Cal. Daily Op. Serv. 1442",
        "volume": "1",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "1442",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "531 U.S. 326",
        "volume": "531",
        "reporter": "U.S.",
        "page": "326",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 946",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "946",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "148 L. Ed. 2d 838",
        "volume": "148",
        "reporter": "L. Ed. 2d",
        "page": "838",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 U.S. LEXIS 962",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "962",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1 Cal. Daily Op. Serv. 1442",
        "volume": "1",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "1442",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "531 U.S. 326",
    "official_selection": {
      "court_class": "scotus",
      "selected": "531 U.S. 326",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-331",
      "page": null,
      "quote": "--- # Illinois v. McArthur *531 U.S. 326 (2001)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background While police helped Tera McArthur remove her belongings from the trailer she shared with her husband, she told officers he had marijuana inside. When Charles McArthur refused consent to a search, an officer prevented him from re-entering the trailer unaccompanied while another officer left to obtain a warrant; for about two hours McArthur was allowed inside only with an officer observing. A warrant issued, the search found marijuana and a pipe, and McArthur moved to suppress the temporary restraint as unreasonable. ## Issue Whether police with probable cause may temporarily prevent a resident from entering his home unaccompanied, to avoid the destruction of evidence, while they diligently obtain a search warrant. ## Rule Yes, on these combined circumstances.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-334",
      "page": null,
      "quote": "We have found no case in which this Court has held unlawful a temporary seizure that was supported by probable cause and was designed to prevent the loss of evidence while the police diligently obtained a warrant in a reasonable period of time.",
      "star_marker": "334",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 19295,
      "fragment": "#:~:text=We%20have%20found%20no%20case",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2001-02-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Illinois v. McArthur",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Jerel Chinedu Igboji v. State",
          "cluster_id": 4789821,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grady",
          "cluster_id": 4649078,
          "cite": [
            "831 S.E.2d 542",
            "372 N.C. 509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Tremblay",
          "cluster_id": 4428704,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Matthew Vaughn Diamond",
          "cluster_id": 4338873,
          "cite": [
            "890 N.W.2d 143",
            "2017 Minn. App. LEXIS 9",
            "2017 WL 163710"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Florida v. Stacey Renee McRae",
          "cluster_id": 3218840,
          "cite": [
            "194 So. 3d 524",
            "2016 Fla. App. LEXIS 9500",
            "2016 WL 3402450"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Olushola Akinmboni v. United States",
          "cluster_id": 3155941,
          "cite": [
            "126 A.3d 694",
            "2015 D.C. App. LEXIS 530",
            "2015 WL 7289524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Yee",
          "cluster_id": 3062319,
          "cite": [
            "177 So. 3d 72",
            "2015 Fla. App. LEXIS 15198",
            "2015 WL 5965213"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grice",
          "cluster_id": 2792904,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grice",
          "cluster_id": 2772730,
          "cite": [
            "367 N.C. 753",
            "767 S.E.2d 312",
            "2015 N.C. LEXIS 69"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dave McNeil v. State",
          "cluster_id": 3094175,
          "cite": [
            "443 S.W.3d 295",
            "2014 WL 3843757",
            "2014 Tex. App. LEXIS 8519"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
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
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Christine Ann Kern",
          "cluster_id": 4472227,
          "cite": [
            "831 N.W.2d 149",
            "2013 WL 2278018",
            "2013 Iowa Sup. LEXIS 61"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Missouri v. McNeely",
          "cluster_id": 858288,
          "cite": [
            "185 L. Ed. 2d 696",
            "133 S. Ct. 1552",
            "569 U.S. 141",
            "2013 U.S. LEXIS 3160",
            "81 U.S.L.W. 4250",
            "24 Fla. L. Weekly Fed. S 150",
            "2013 WL 1628934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knights",
          "cluster_id": 118468,
          "cite": [
            "151 L. Ed. 2d 497",
            "122 S. Ct. 587",
            "534 U.S. 112",
            "2001 U.S. LEXIS 10950"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Georgia v. Randolph",
          "cluster_id": 145669,
          "cite": [
            "164 L. Ed. 2d 208",
            "126 S. Ct. 1515",
            "547 U.S. 103",
            "2006 U.S. LEXIS 2498"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. King",
          "cluster_id": 873669,
          "cite": [
            "186 L. Ed. 2d 1",
            "133 S. Ct. 1958",
            "2013 U.S. LEXIS 4165",
            "569 U.S. 435",
            "24 Fla. L. Weekly Fed. S 234",
            "81 U.S.L.W. 4343",
            "2013 WL 2371466"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cortez v. McCauley",
          "cluster_id": 167088,
          "cite": [
            "478 F.3d 1108",
            "2007 WL 503819"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gutierrez v. State",
          "cluster_id": 1508583,
          "cite": [
            "221 S.W.3d 680",
            "2007 Tex. Crim. App. LEXIS 500",
            "2007 WL 1217343"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Menotti v. City of Seattle",
          "cluster_id": 3032002,
          "cite": [
            "409 F.3d 1113",
            "2005 WL 1300994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dennis Dayton Holt",
          "cluster_id": 774866,
          "cite": [
            "264 F.3d 1215",
            "2001 Colo. J. C.A.R. 4452",
            "2001 U.S. App. LEXIS 19759",
            "2001 WL 1013251"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jones",
          "cluster_id": 2058953,
          "cite": [
            "830 N.E.2d 541",
            "215 Ill. 2d 261",
            "294 Ill. Dec. 129",
            "2005 Ill. LEXIS 632"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Villarreal, David",
          "cluster_id": 2948963,
          "cite": [
            "475 S.W.3d 784",
            "2014 Tex. Crim. App. LEXIS 1898",
            "2014 WL 6734178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of L. A. v. Patel",
          "cluster_id": 2811846,
          "cite": [
            "576 U.S. 409",
            "135 S. Ct. 2443",
            "192 L. Ed. 2d 435",
            "2015 U.S. LEXIS 4065",
            "83 U.S.L.W. 4520",
            "25 Fla. L. Weekly Fed. S 412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Schriner",
          "cluster_id": 4635000,
          "cite": [
            "303 Neb. 476",
            "929 N.W.2d 514"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Douglas McClish v. Richard B. Nugent",
          "cluster_id": 77659,
          "cite": [
            "483 F.3d 1231",
            "2007 U.S. App. LEXIS 8294",
            "2007 WL 1063337"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Swietlicki",
          "cluster_id": 3157591,
          "cite": [
            "2015 CO 67",
            "361 P.3d 411",
            "2015 WL 7423463"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Loria v. Gorman",
          "cluster_id": 7108550,
          "cite": [
            "306 F.3d 1271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marco Burton",
          "cluster_id": 777431,
          "cite": [
            "288 F.3d 91",
            "2002 U.S. App. LEXIS 7851",
            "2002 WL 753492"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Tierney",
          "cluster_id": 1972558,
          "cite": [
            "703 N.W.2d 204",
            "266 Mich. App. 687"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gonzalez",
          "cluster_id": 2200827,
          "cite": [
            "789 N.E.2d 260",
            "204 Ill. 2d 220",
            "273 Ill. Dec. 360",
            "2003 Ill. LEXIS 765"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fredrick K. Koch v. Town of Brattleboro, Vermont, Sherwood D. Lake, Jr., and John Doe, Unidentified Brattleboro Police Officer",
          "cluster_id": 777318,
          "cite": [
            "287 F.3d 162",
            "2002 U.S. App. LEXIS 5301"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estate of Bennett v. Wainwright",
          "cluster_id": 203573,
          "cite": [
            "548 F.3d 155",
            "2008 U.S. App. LEXIS 24217",
            "2008 WL 5005534"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McDonough",
          "cluster_id": 2483242,
          "cite": [
            "940 N.E.2d 1100",
            "239 Ill. 2d 260",
            "346 Ill. Dec. 496",
            "2010 Ill. LEXIS 1557"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Colon",
          "cluster_id": 773257,
          "cite": [
            "250 F.3d 130",
            "2001 U.S. App. LEXIS 9205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. Commonwealth",
          "cluster_id": 1063086,
          "cite": [
            "642 S.E.2d 295",
            "49 Va. App. 439",
            "2007 Va. App. LEXIS 113"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lampitok",
          "cluster_id": 2148470,
          "cite": [
            "798 N.E.2d 91",
            "207 Ill. 2d 231",
            "278 Ill. Dec. 244"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. McArthur:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118405 OR 9434039 OR 9434040 OR 9434041) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjI3NjU3NjAwMDAwJnM9MjAzNTczJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118405+OR+9434039+OR+9434040+OR+9434041%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118405 OR 9434039 OR 9434040 OR 9434041)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05OSZzPTgxMjk1MCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118405+OR+9434039+OR+9434040+OR+9434041%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118405 OR 9434039 OR 9434040 OR 9434041)",
        "reviewed": 25,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 25,
        "triage_read": 0,
        "triage_snippet_classified": 25
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118405 OR 9434039 OR 9434040 OR 9434041)",
    "indexed_citing_opinions": 421,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118405,
        "count": 350,
        "count_source": "search"
      },
      {
        "opinion_id": 9434039,
        "count": 73,
        "count_source": "search"
      },
      {
        "opinion_id": 9434040,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434041,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 737,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/illinois-v-mcarthur.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgzNDQxMTYmcz05NDEyMTYxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118405+OR+9434039+OR+9434040+OR+9434041%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118405,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 108099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 111172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 111259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 118063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 118103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118405,
        "cited_id": 2106379,
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
    "date_created": "2026-07-05T08:14:17Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:14:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:14:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:20:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:14:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Illinois v. McArthur

```
<div>
<center><b><span class="citation" data-id="9434039"><a href="/opinion/118405/illinois-v-mcarthur/" aria-description="Citation for case: Illinois v. McArthur">531 U.S. 326</a></span> (2001)</b></center>
<center><h1>ILLINOIS<br>
v.<br>
McARTHUR</h1></center>
<center>No. 99-1132.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued November 1, 2000.</center>
<center>Decided February 20, 2001.</center>
CERTIORARI TO THE APPELLATE COURT OF ILLINOIS, FOURTH DISTRICT
<p><span class="star-pagination">*328</span> Breyer, J., delivered the opinion of the Court, in which Rehnquist, C. J., and O'Connor, Scalia, Kennedy, Souter, Thomas, and Ginsburg, JJ., joined. Souter, J., filed a concurring opinion, <i>post,</i> p. 337. Stevens, J., filed a dissenting opinion, <i>post,</i> p. 338.</p>
<p><i>Joel D. Bertocchi,</i> Solicitor General of Illinois, argued the cause for petitioner. With him on the briefs were <i>James E. Ryan,</i> Attorney General, and <i>William L. Browers</i> and <i>Colleen M. Griffin,</i> Assistant Attorneys General.</p>
<p><i>Matthew D. Roberts</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Waxman, Assistant Attorney General Robinson, Deputy Solicitor General Dreeben,</i> and <i>Deborah Watson.</i> </p>
<p><span class="star-pagination">*328</span> <i>Deanne Fortna Jones</i> argued the cause for respondent. With her on the brief was <i>Jeff Justice.</i><sup>[*]</sup></p>
<p>Justice Breyer, delivered the opinion of the Court.</p>
<p>Police officers, with probable cause to believe that a man had hidden marijuana in his home, prevented that man from entering the home for about two hours while they obtained a search warrant. We must decide whether those officers violated the Fourth Amendment. We conclude that the officers acted reasonably. They did not violate the Amendment's requirements. And we reverse an Illinois court's holding to the contrary.</p>
<p></p>
<h2>I</h2>
<p></p>
<h2>A</h2>
<p>On April 2, 1997, Tera McArthur asked two police officers to accompany her to the trailer where she lived with her husband, Charles, so that they could keep the peace while she removed her belongings. The two officers, Assistant Chief John Love and Officer Richard Skidis, arrived with <span class="star-pagination">*329</span> Tera at the trailer at about 3:15 p.m. Tera went inside, where Charles was present. The officers remained outside.</p>
<p>When Tera emerged after collecting her possessions, she spoke to Chief Love, who was then on the porch. She suggested he check the trailer because "Chuck had dope in there." App. 15. She added (in Love's words) that she had seen Chuck "slid[e] some dope underneath the couch." <i>Id.,</i>  at 19.</p>
<p>Love knocked on the trailer door, told Charles what Tera had said, and asked for permission to search the trailer, which Charles denied. Love then sent Officer Skidis with Tera to get a search warrant.</p>
<p>Love told Charles, who by this time was also on the porch, that he could not reenter the trailer unless a police officer accompanied him. Charles subsequently reentered the trailer two or three times (to get cigarettes and to make phone calls), and each time Love stood just inside the door to observe what Charles did.</p>
<p>Officer Skidis obtained the warrant by about 5 p.m. He returned to the trailer and, along with other officers, searched it. The officers found under the sofa a marijuana pipe, a box for marijuana (called a "one-hitter" box), and a small amount of marijuana. They then arrested Charles.</p>
<p></p>
<h2>B</h2>
<p>Illinois subsequently charged Charles McArthur with unlawfully possessing drug paraphernalia and marijuana (less than 2.5 grams), both misdemeanors. See Ill. Comp. Stat., ch. 720, §§ 550/4(a), 600/3.5(a) (1998). McArthur moved to suppress the pipe, box, and marijuana on the ground that they were the "fruit" of an unlawful police seizure, namely, the refusal to let him reenter the trailer unaccompanied, which would have permitted him, he said, to "have destroyed the marijuana." App. 27.</p>
<p>The trial court granted McArthur's suppression motion. The Appellate Court of Illinois affirmed, 304 Ill. App. 3d <span class="star-pagination">*330</span> 395, <span class="citation" data-id="2106379"><a href="/opinion/2106379/people-v-mcarthur/" aria-description="Citation for case: People v. McArthur">713 N. E. 2d 93</a></span> (1999), and the Illinois Supreme Court denied the State's petition for leave to appeal, <span class="citation no-link">185 Ill. 2d 651</span>, <span class="citation no-link">720 N. E. 2d 1101</span> (1999). We granted certiorari to determine whether the Fourth Amendment prohibits the kind of temporary seizure at issue here.</p>
<p></p>
<h2>II</h2>
<p></p>
<h2>A</h2>
<p>The Fourth Amendment says that the "right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated." U. S. Const., Amdt. 4. Its "central requirement" is one of reasonableness. See <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#739" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 739</a></span> (1983). In order to enforce that requirement, this Court has interpreted the Amendment as establishing rules and presumptions designed to control conduct of law enforcement officers that may significantly intrude upon privacy interests. Sometimes those rules require warrants. We have said, for example, that in "the ordinary case," seizures of personal property are "unreasonable within the meaning of the Fourth Amendment," without more, "unless . . . accomplished pursuant to a judicial warrant," issued by a neutral magistrate after finding probable cause. <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#701" aria-description="Citation for case: United States v. Place">462 U. S. 696, 701</a></span> (1983).</p>
<p>We nonetheless have made it clear that there are exceptions to the warrant requirement. When faced with special law enforcement needs, diminished expectations of privacy, minimal intrusions, or the like, the Court has found that certain general, or individual, circumstances may render a warrantless search or seizure reasonable. See, <i>e. g., </i><i>Pennsylvania</i> v. <i>Labron,</i> <span class="citation" data-id="9433386"><a href="/opinion/118063/pennsylvania-v-labron/#940" aria-description="Citation for case: Pennsylvania v. Labron">518 U. S. 938, 940-941</a></span> (1996) <i>(per curiam)</i> (search of automobile supported by probable cause); <i>Michigan Dept. of State Police</i> v. <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#455" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S. 444, 455</a></span> (1990) (suspicionless stops at drunk driver checkpoint); <i>United States</i> v. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#706" aria-description="Citation for case: United States v. Place"><i>Place, supra,</i> at 706</a></span> (temporary seizure of luggage based on reasonable suspicion); <i>Michigan</i> v. <span class="star-pagination">*331</span> <i>Summers,</i> <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 702-705</a></span> (1981) (temporary detention of suspect without arrest warrant to prevent flight and protect officers while executing search warrant); <i>Terry</i> v. <i>Ohio,</i>  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 27</a></span> (1968) (temporary stop and limited search for weapons based on reasonable suspicion).</p>
<p>In the circumstances of the case before us, we cannot say that the warrantless seizure was <i>per se</i> unreasonable. It involves a plausible claim of specially pressing or urgent law enforcement need, <i>i. e.,</i> "exigent circumstances." Cf., <i>e. g., </i><i>United States</i> v. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#701" aria-description="Citation for case: United States v. Place"><i>Place, supra,</i> at 701</a></span> ("[T]he exigencies of the circumstances" may permit temporary seizure without warrant); <i>Warden, Md. Penitentiary</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298-299</a></span> (1967) (warrantless search for suspect and weapons reasonable where delay posed grave danger); <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 770-771</a></span> (1966) (warrantless blood test for alcohol reasonable where delay would have led to loss of evidence). Moreover, the restraint at issue was tailored to that need, being limited in time and scope, cf. <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i> at 29-30</a></span>, and avoiding significant intrusion into the home itself, cf. <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#585" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 585</a></span> (1980) ("`[T]he chief evil against which the . . . Fourth Amendment is directed' " is warrantless entry and search of home) (quoting <i>United States</i> v. <i>United States Dist. Court for Eastern Dist. of Mich.,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span> (1972)). Consequently, rather than employing a <i>per se</i>  rule of unreasonableness, we balance the privacy-related and law enforcement-related concerns to determine if the intrusion was reasonable. Cf. <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979) (determining lawfulness by balancing privacy and law enforcement interests); <i>United States</i> v. <i>BrignoniPonce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975) (same).</p>
<p>We conclude that the restriction at issue was reasonable, and hence lawful, in light of the following circumstances, which we consider in combination. First, the police had probable cause to believe that McArthur's trailer home contained evidence of a crime and contraband, namely, unlawful <span class="star-pagination">*332</span> drugs. The police had had an opportunity to speak with Tera McArthur and make at least a very rough assessment of her reliability. They knew she had had a firsthand opportunity to observe her husband's behavior, in particular with respect to the drugs at issue. And they thought, with good reason, that her report to them reflected that opportunity. Cf. <i>Massachusetts</i> v. <i>Upton,</i> <span class="citation" data-id="9429595"><a href="/opinion/111172/massachusetts-v-upton/#732" aria-description="Citation for case: Massachusetts v. Upton">466 U. S. 727, 732-734</a></span> (1984) <i>(per curiam)</i> (upholding search warrant issued in similar circumstances).</p>
<p>Second, the police had good reason to fear that, unless restrained, McArthur would destroy the drugs before they could return with a warrant. They reasonably might have thought that McArthur realized that his wife knew about his marijuana stash; observed that she was angry or frightened enough to ask the police to accompany her; saw that after leaving the trailer she had spoken with the police; and noticed that she had walked off with one policeman while leaving the other outside to observe the trailer. They reasonably could have concluded that McArthur, consequently suspecting an imminent search, would, if given the chance, get rid of the drugs fast.</p>
<p>Third, the police made reasonable efforts to reconcile their law enforcement needs with the demands of personal privacy. They neither searched the trailer nor arrested McArthur before obtaining a warrant. Rather, they imposed a significantly less restrictive restraint, preventing McArthur only from entering the trailer unaccompanied. They left his home and his belongings intactuntil a neutral Magistrate, finding probable cause, issued a warrant.</p>
<p>Fourth, the police imposed the restraint for a limited period of time, namely, two hours. Cf. <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#28" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i>  at 28</a></span> (manner in which police act is "vital . .. part of . . . inquiry"). As far as the record reveals, this time period was no longer than reasonably necessary for the police, acting with diligence, to obtain the warrant. Compare <i>United</i>  <span class="star-pagination">*333</span> <i>States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place">462 U. S., at 709-710</a></span> (holding 90-minute detention of luggage unreasonable based on nature of interference with person's travels and lack of diligence of police), with <i>United States</i> v. <i>Van Leeuwen,</i> <span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/#253" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S. 249, 253</a></span> (1970) (holding 29-hour detention of mailed package reasonable given unavoidable delay in obtaining warrant and minimal nature of intrusion). Given the nature of the intrusion and the law enforcement interest at stake, this brief seizure of the premises was permissible.</p>
<p></p>
<h2>B</h2>
<p>Our conclusion that the restriction was lawful finds significant support in this Court's case law. In <i>Segura</i> v. <i>United States,</i> <span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">468 U. S. 796</a></span> (1984), the Court considered the admissibility of drugs which the police had found in a lawful, warrant-based search of an apartment, but only after unlawfully entering the apartment and occupying it for 19 hours. The majority held that the drugs were admissible because, had the police acted lawfully throughout, they could have discovered and seized the drugs pursuant to the validly issued warrant. See <span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/#799" aria-description="Citation for case: Segura v. United States"><i>id.,</i> at 799</a></span>, 814-815 (citing <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920)). The minority disagreed. However, when describing alternative lawful search and seizure methods, both majority and minority assumed, at least for argument's sake, that the police, armed with reliable information that the apartment contained drugs, might lawfully have sealed the apartment from the outside, restricting entry into the apartment while waiting for the warrant. Compare <i>Segura</i>  v. <i>United States,</i> <span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/#814" aria-description="Citation for case: Segura v. United States">468 U. S., at 814</a></span> ("Had police never entered the apartment, but instead conducted a perimeter stake out to prevent anyone from entering . . . and destroying evidence, the contraband . . .would have been . . .seized precisely as it was here"), with <span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/#824" aria-description="Citation for case: Segura v. United States"><i>id.,</i> at 824, n. 15</a></span> (Stevens, J., dissenting) ("I assume impoundment would be permissible <span class="star-pagination">*334</span> even absent exigent circumstances when it occurs `from the outside'when the authorities merely seal off premises pending the issuance of a warrant but do not enter"); see also <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#394" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 394</a></span> (1978) (exigent circumstances do not justify search where police guard at door could prevent loss of evidence); <i>United States</i> v. <i>Jeffers,</i>  <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#52" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 52</a></span> (1951) (same).</p>
<p>In various other circumstances, this Court has upheld temporary restraints where needed to preserve evidence until police could obtain a warrant. See, <i>e. g., </i><i>United States</i>  v. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#706" aria-description="Citation for case: United States v. Place"><i>Place, supra,</i> at 706</a></span> (reasonable suspicion justifies brief detention of luggage pending further investigation); <i>United States</i> v. <span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/#253" aria-description="Citation for case: United States v. Van Leeuwen"><i>Van Leeuwen, supra,</i> at 253</a></span> (reasonable suspicion justifies detaining package delivered for mailing). Cf. <i>Richards</i> v. <i>Wisconsin,</i> <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/#395" aria-description="Citation for case: Richards v. Wisconsin">520 U. S. 385, 395</a></span> (1997) (no need to "knock and announce" when executing a search warrant where officers reasonably suspect that evidence might be destroyed); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153</a></span> (1925) (warrantless search of automobile constitutionally permissible).</p>
<p>We have found no case in which this Court has held unlawful a temporary seizure that was supported by probable cause and was designed to prevent the loss of evidence while the police diligently obtained a warrant in a reasonable period of time. But cf. <i>Welsh</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#754" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740, 754</a></span> (1984) (holding warrantless entry into and arrest in home unreasonable despite possibility that evidence of noncriminal offense would be lost while warrant was being obtained).</p>
<p></p>
<h2>C</h2>
<p>Nor are we persuaded by the countervailing considerations that the parties or lower courts have raised. McArthur argues that the police proceeded without probable cause. But McArthur has waived this argument. See <span class="citation" data-id="2106379"><a href="/opinion/2106379/people-v-mcarthur/#397" aria-description="Citation for case: People v. McArthur">304 Ill. App. 3d, at 397</a></span>, <span class="citation" data-id="2106379"><a href="/opinion/2106379/people-v-mcarthur/#95" aria-description="Citation for case: People v. McArthur">713 N. E. 2d, at 95</a></span> (stating that McArthur <span class="star-pagination">*335</span> does not contest existence of probable cause); Brief in Opposition 7 (acknowledging probable cause). And, in any event, it is without merit. See <i>supra,</i> at 331-332.</p>
<p>The Appellate Court of Illinois concluded that the police could not order McArthur to stay outside his home because McArthur's porch, where he stood at the time, was part of his home; hence the order "amounted to a constructive eviction" of McArthur from his residence. <span class="citation" data-id="2106379"><a href="/opinion/2106379/people-v-mcarthur/#402" aria-description="Citation for case: People v. McArthur">304 Ill. App. 3d, at 402</a></span>, <span class="citation" data-id="2106379"><a href="/opinion/2106379/people-v-mcarthur/#98" aria-description="Citation for case: People v. McArthur">713 N. E. 2d, at 98</a></span>. This Court has held, however, that a person standing in the doorway of a house is "in a `public' place," and hence subject to arrest without a warrant permitting entry of the home. <i>United States</i> v. <i>Santana,</i>  <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#42" aria-description="Citation for case: United States v. Santana">427 U. S. 38, 42</a></span> (1976). Regardless, we do not believe the difference to which the Appellate Court pointsporch versus, <i>e. g.,</i> front walkcould make a significant difference here as to the reasonableness of the police restraint; and that, from the Fourth Amendment's perspective, is what matters.</p>
<p>The Appellate Court also found negatively significant the fact that Chief Love, with McArthur's consent, stepped inside the trailer's doorway to observe McArthur when McArthur reentered the trailer on two or three occasions. <span class="citation" data-id="2106379"><a href="/opinion/2106379/people-v-mcarthur/#402" aria-description="Citation for case: People v. McArthur">304 Ill. App. 3d, at 402-403</a></span>, <span class="citation" data-id="2106379"><a href="/opinion/2106379/people-v-mcarthur/#98" aria-description="Citation for case: People v. McArthur">713 N. E. 2d, at 98</a></span>. McArthur, however, reentered simply for his own convenience, to make phone calls and to obtain cigarettes. Under these circumstances, the reasonableness of the greater restriction (preventing reentry) implies the reasonableness of the lesser (permitting reentry conditioned on observation).</p>
<p>Finally, McArthur points to a case (and we believe it is the only case) that he believes offers direct support, namely, <i>Welsh</i> v. <i>Wisconsin, supra</i><i>.</i> In <i><span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">Welsh</a></span>,</i> this Court held that police could not enter a home without a warrant in order to prevent the loss of evidence (namely, the defendant's blood alcohol level) of the "nonjailable traffic offense" of driving while intoxicated. 466 U. S., at 742, 754. McArthur notes <span class="star-pagination">*336</span> that his two convictions are for misdemeanors, which, he says, are as minor, and he adds that the restraint, keeping him out of his home, was nearly as serious.</p>
<p>We nonetheless find significant distinctions. The evidence at issue here was of crimes that were "jailable," not "nonjailable." See Ill. Comp. Stat., ch. 720, § 550/4(a) (1998); ch. 730, § 5/5-83(3) (possession of less than 2.5 grams of marijuana punishable by up to 30 days in jail); ch. 720, § 600/ 3.5; ch. 730, § 5/5-83(1) (possession of drug paraphernalia punishable by up to one year in jail). In <i><span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">Welsh</a></span>,</i> we noted that, "[g]iven that the classification of state crimes differs widely among the States, the penalty that may attach to any particular offense seems to provide the clearest and most consistent indication of the State's interest in arresting individuals suspected of committing that offense." 466 U. S., at 754, n. 14. The same reasoning applies here, where class C misdemeanors include such widely diverse offenses as drag racing, drinking alcohol in a railroad car or on a railroad platform, bribery by a candidate for public office, and assault. See, <i>e. g.,</i> Ill. Comp. Stat., ch. 65, § 5/4-82 (1998); ch. 610, § 90/1; ch. 625, § 5/11-504; ch. 720, § 5/12-1.</p>
<p>And the restriction at issue here is less serious. Temporarily keeping a person from entering his home, a consequence whenever police stop a person on the street, is considerably less intrusive than police entry into the home itself in order to make a warrantless arrest or conduct a search. Cf. <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#585" aria-description="Citation for case: Payton v. New York">445 U. S., at 585</a></span> (the Fourth Amendment's central concern is the warrantless entry and search of the home).</p>
<p>We have explained above why we believe that the need to preserve evidence of a "jailable" offense was sufficiently urgent or pressing to justify the restriction upon entry that the police imposed. We need not decide whether the circumstances before us would have justified a greater restriction for this type of offense or the same restriction were only a "nonjailable" offense at issue.</p>
<p></p>
<h2>
<span class="star-pagination">*337</span> III</h2>
<p>In sum, the police officers in this case had probable cause to believe that a home contained contraband, which was evidence of a crime. They reasonably believed that the home's resident, if left free of any restraint, would destroy that evidence. And they imposed a restraint that was both limited and tailored reasonably to secure law enforcement needs while protecting privacy interests. In our view, the restraint met the Fourth Amendment's demands.</p>
<p>The judgment of the Illinois Appellate Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i> </p>
<p>Justice Souter, concurring.</p>
<p>I join the Court's opinion subject to this afterword on two points: the constitutionality of a greater intrusion than the one here and the permissibility of choosing impoundment over immediate search. Respondent McArthur's location made the difference between the exigency that justified temporarily barring him from his own dwelling and circumstances that would have supported a greater interference with his privacy and property. As long as he was inside his trailer, the police had probable cause to believe that he had illegal drugs stashed as his wife had reported and that with any sense he would flush them down the drain before the police could get a warrant to enter and search. This probability of destruction in anticipation of a warrant exemplifies the kind of present risk that undergirds the accepted exigent circumstances exception to the general warrant requirement. <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 770-771</a></span> (1966). That risk would have justified the police in entering McArthur's trailer promptly to make a lawful, warrantless search. <i>United States</i> v. <i>Santana,</i> <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#42" aria-description="Citation for case: United States v. Santana">427 U. S. 38, 42-43</a></span> (1976); <i>Warden, Md. Penitentiary</i> v. <i>Hayden,</i>  <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298-299</a></span> (1967). When McArthur stepped <span class="star-pagination">*338</span> outside and left the trailer uninhabited, the risk abated and so did the reasonableness of entry by the police for as long as he was outside. This is so because the only justification claimed for warrantless action here is the immediate risk, and the limit of reasonable response by the police is set by the scope of the risk. See <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#25" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 25-26</a></span> (1968).</p>
<p>Since, however, McArthur wished to go back in, why was it reasonable to keep him out when the police could perfectly well have let him do as he chose, and then enjoyed the ensuing opportunity to follow him and make a warrantless search justified by the renewed danger of destruction? The answer is not that the law officiously insists on safeguarding a suspect's privacy from search, in preference to respecting the suspect's liberty to enter his own dwelling. Instead, the legitimacy of the decision to impound the dwelling follows from the law's strong preference for warrants, which underlies the rule that a search with a warrant has a stronger claim to justification on later, judicial review than a search without one. See <i>United States</i> v<i>. Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#106" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 106</a></span> (1965); see also 5 W. LaFave, Search and Seizure § 11.2(b), p. 38 (3d ed. 1996) ("[M]ost states follow the rule which is utilized in the federal courts: if the search or seizure was pursuant to a warrant, the defendant has the burden of proof; but if the police acted without a warrant the burden of proof is on the prosecution"). The law can hardly raise incentives to obtain a warrant without giving the police a fair chance to take their probable cause to a magistrate and get one.</p>
<p>Justice Stevens, dissenting.</p>
<p>The Illinois General Assembly has decided that the possession of less than 2.5 grams of marijuana is a class C misdemeanor. See Ill. Comp. Stat., ch. 720, § 550/4(a) (1998). In so classifying the offense, the legislature made a concerted policy judgment that the possession of small amounts of <span class="star-pagination">*339</span> marijuana for personal use does not constitute a particularly significant public policy concern. While it is true that this offenselike feeding livestock on a public highway or offering a movie for rent without clearly displaying its rating<sup>[1]</sup> may warrant a jail sentence of up to 30 days, the detection and prosecution of possessors of small quantities of this substance is by no means a law enforcement priority in the State of Illinois.<sup>[2]</sup></p>
<p>Because the governmental interest implicated by the particular criminal prohibition at issue in this case is so slight, this is a poor vehicle for probing the boundaries of the government's power to limit an individual's possessory interest in his or her home pending the arrival of a search warrant. Cf. <i>Segura</i> v. <i>United States,</i> <span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">468 U. S. 796</a></span> (1984) (seven Justices decline to address this issue because case does not require its resolution). Given my preference, I would, therefore, dismiss the writ of certiorari as improvidently granted.</p>
<p>Compelled by the vote of my colleagues to reach the merits, I would affirm. As the majority explains, the essential inquiry in this case involves a balancing of the "privacyrelated <span class="star-pagination">*340</span> and law enforcement-related concerns to determine if the intrusion was reasonable." <i>Ante,</i> at 331. Under the specific facts of this case, I believe the majority gets the balance wrong. Each of the Illinois jurists who participated in the decision of this case placed a higher value on the sanctity of the ordinary citizen's home than on the prosecution of this petty offense. They correctly viewed that interestwhether the home be a humble cottage, a secondhand trailer, or a stately mansionas one meriting the most serious constitutional protection.<sup>[3]</sup> Following their analysis and the reasoning in our decision in <i>Welsh</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740</a></span> (1984) (holding that some offenses may be so minor as to make it unreasonable for police to undertake searches that would be constitutionally permissible if graver offenses were suspected), I would affirm.</p>
<h2>NOTES</h2>
<p>[*]   A brief of <i>amici curiae</i> urging reversal was filed for the State of Ohio et al. by <i>Betty D. Montgomery,</i> Attorney General of Ohio, <i>Edward B. Foley,</i> State Solicitor, and <i>Robert C. Maier</i> and <i>Matthew D. Miko,</i> Assistant Solicitors, and by the Attorneys General for their respective States as follows: <i>Bruce M. Botelho</i> of Alaska, <i>Janet Napolitano</i> of Arizona, <i>M. Jane Brady</i> of Delaware, <i>Alan G. Lance</i> of Idaho, <i>Thomas J. Miller</i> of Iowa, <i>Andrew Ketterer</i> of Maine, <i>J. Joseph Curran, Jr.,</i> of Maryland, <i>Mike Hatch</i> of Minnesota, <i>Joseph P. Mazurek</i> of Montana, <i>Philip McLaughlin</i>  of New Hampshire, <i>John J. Farmer, Jr.,</i> of New Jersey, <i>Don Stenberg</i> of Nebraska, <i>Frankie Sue Del Papa</i> of Nevada, <i>W. A. Drew Edmondson</i> of Oklahoma, <i>Charles M. Condon</i> of South Carolina, <i>Mark Barnett</i> of South Dakota, <i>Jan Graham</i> of Utah, <i>William H. Sorrell</i> of Vermont, <i>Christine O. Gregoire</i> of Washington, <i>Thomas F. Reilly</i> of Massachusetts, <i>D. Michael Fisher</i> of Pennsylvania, and <i>Mark L. Earley</i> of Virginia.
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the National Association of Criminal Defense Lawyers by <i>Lisa B. Kemler;</i> and for the Rutherford Institute by <i>John W. Whitehead</i> and <i>Steven H. Aden.</i> </p>
<p>[1]  See Ill. Comp. Stat., ch. 605, § 5/9-124.1 (1998) (making feeding livestock on a public highway a class C misdemeanor); ch. 720, §§ 395/3-395/4 (making it a class C misdemeanor to sell or rent a video that does not display the official rating of the motion picture from which it is copied). Other examples of offenses classified as class C misdemeanors in Illinois include camping on the side of a public highway, ch. 605, § 5/9-124, interfering with the "lawful taking of wild animals," ch. 720, § 125/2, and tattooing the body of a person under 21 years of age, ch. 720, § 5/12-10.</p>
<p>[2]  Nor in many other States. Under the laws of many other States, the maximum penalty McArthur would have faced for possession of 2.3 grams of marijuana would have been less than what he faced in Illinois. See, <i>e. g.,</i> Cal. Health &amp; Safety Code Ann. § 11357(b) (West 1991) ($100 fine); <span class="citation no-link">Colo. Rev. Stat. § 18-18-406</span>(1) (1999) ($100 fine); <span class="citation no-link">Minn. Stat. § 152.027</span>(4) (2000) ($200 fine and drug education); <span class="citation no-link">Miss. Code Ann. § 41-29-139</span>(c)(2)(A) (Supp. 1999) ($100$250 fine); <span class="citation no-link">Neb. Rev. Stat. § 28-416</span>(13) (1995) ($100 fine and drug education); N. M. Stat. Ann. § 30-31-23(B) (1997) ($50$100 fine and 15 days in jail); N. Y. Penal Law § 221.05 (McKinney 2000) ($100 fine); Ore. Rev. Stat. § 475.992(4)(f) (Supp. 1998) ($100 fine).</p>
<p>[3]  Principled respect for the sanctity of the home has long animated this Court's Fourth Amendment jurisprudence. See, <i>e. g., </i><i>Wilson</i> v. <i>Layne,</i> <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#610" aria-description="Citation for case: Wilson v. Layne">526 U. S. 603, 610</a></span> (1999) ("The Fourth Amendment embodies this centuries-old principle of respect for the privacy of the home"); <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#601" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 601</a></span> (1980) (emphasizing "the overriding respect for the sanctity of the home that has been embedded in our traditions since the origins of the Republic"); <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 393</a></span> (1978) ("[T]he Fourth Amendment reflects the view of those who wrote the Bill of Rights that the privacy of a person's home and property may not be totally sacrificed in the name of maximum simplicity in enforcement of the criminal law").</p>

</div>
```

---

## GROUP: content/cases/Imbler v. Pachtman.md  (`case`, 5 assertions)

### content_page

```
---
title: Imbler v. Pachtman
type: case
citation: "424 U.S. 409 (1976)"
parallel_cite: "96 S. Ct. 984; 47 L. Ed. 2d 128"
neutral_cite: 1976 U.S. LEXIS 25
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-03-02
docket: No. 74-5435
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
  opinion_url: "https://www.courtlistener.com/opinion/109387/imbler-v-pachtman/"
  cluster_id: 109387
  opinion_id: null
  identity_checked: true
lake:
  record_id: Imbler v. Pachtman
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Absolute Immunity]]"
    role: Anchor
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Buckley v. Fitzsimmons]]"
  - "[[Briscoe v. LaHue]]"
tags:
  - case
  - section-1983
  - prosecutorial-immunity
  - absolute-immunity
  - judicial-phase
holding: "A state prosecutor is absolutely immune from a § 1983 damages suit for conduct intimately associated with the judicial phase of the criminal process — that is, in initiating a prosecution and in presenting the State's case — even where the claim is that the prosecutor knowingly used false testimony and suppressed exculpatory evidence."
aliases:
  - Imbler v. Pachtman
  - "Imbler v. Pachtman (1976)"
---

# Imbler v. Pachtman

*424 U.S. 409 (1976)* (No. 74-5435) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 109387 → combined opinion 109387 (Powell, J.; 424 U.S. 409, decided Mar. 2, 1976). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*431`). S9 promotes. -->

## Background
Paul Imbler was convicted of murder in a prosecution handled by deputy district attorney Richard Pachtman. Imbler was later released on federal [[Common Legal Terms#habeas-corpus|habeas]] after evidence emerged that the State's case had rested in part on testimony the prosecutor allegedly knew to be false and on the suppression of [[Brady and Giglio|exculpatory]] material. Imbler then sued Pachtman under § 1983 for damages. The lower courts held the prosecutor absolutely immune from such a suit, and the Supreme Court granted [[Reading and Citing Cases#certiorari-cert|certiorari]].

## Issue
Whether a state prosecutor may be held liable in damages under § 1983 for allegedly knowingly using false testimony and suppressing [[Brady and Giglio|exculpatory]] evidence in securing a conviction.

## Rule
Drawing on the common-law immunity of prosecutors and the policy reasons behind it, the Court confined its holding to the prosecutor's advocacy role but held that role absolutely immune: "We hold only that in initiating a prosecution and in presenting the State's case, the prosecutor is immune from a civil suit for damages under § 1983." — 424 U.S. at 431. ^pin-431

## Application
Deciding to prosecute and presenting the State's case are functions intimately associated with the judicial phase of the criminal process, and the reasons for absolute immunity — shared with judges and grand jurors — apply with full force: exposing prosecutors to damages suits by every convicted defendant would deflect their energies and distort the independent judgment the office requires. The Court pointedly reserved whether the same immunity covers a prosecutor's administrative or investigative acts, leaving that question for another day.

## Conclusion
The judgment was **affirmed**. Powell, J., delivered the opinion of the Court; White, J. (joined by Brennan and Marshall, JJ.), concurred in the judgment; Stevens, J., took no part in the consideration or decision of the case.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Imbler* is the foundational grant of **absolute prosecutorial immunity** for advocacy. The question it expressly reserved — whether investigative or administrative acts are also absolutely immune — was answered in *[[Buckley v. Fitzsimmons]]* (1993): only **qualified** immunity attaches to a prosecutor's investigative fabrication of evidence and press statements. Teach *Imbler* with *[[Buckley v. Fitzsimmons|Buckley]]* (the advocacy/investigation line) and *[[Briscoe v. LaHue]]* (witness immunity).

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Anchor*

## Sources
- [*Imbler v. Pachtman*, 424 U.S. 409 (1976)](https://www.courtlistener.com/opinion/109387/imbler-v-pachtman/) — pinpoint: 431 (Powell, J., for the Court; the CL opinion text carries the reporter star `*431` immediately before the holding, which sits between `*431` and `*432`). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5375eb91c2b46859", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "424 U.S. 409 (1976)", "court": "U.S. Supreme Court", "neutral_cite": "1976 U.S. LEXIS 25", "official_citation_present": true, "parallel_cite": "96 S. Ct. 984; 47 L. Ed. 2d 128", "title": "Imbler v. Pachtman", "year": "1976"}}
{"assertion_id": "37703dd1471d4515", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A state prosecutor is absolutely immune from a § 1983 damages suit for conduct intimately associated with the judicial phase of the criminal process — that is, in initiating a prosecution and in presenting the State's case — even where the claim is that the prosecutor knowingly used false testimony and suppressed exculpatory evidence.", "title": "Imbler v. Pachtman"}}
{"assertion_id": "3dfffba21d8fbe93", "dimension": "support", "kind": "home_role", "locator": {"home": "Absolute Immunity"}, "payload": {"home": "Absolute Immunity", "role": "Anchor", "title": "Imbler v. Pachtman"}}
{"assertion_id": "2629fc2f0b07c87c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Imbler v. Pachtman"}}
{"assertion_id": "385f9f374bb4a8fb", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Imbler v. Pachtman", "varies_by_point": "false"}}
```

### lake record — Imbler v. Pachtman

```json
{
  "schema_version": "s2.v1",
  "record_id": "Imbler v. Pachtman",
  "status": "under_review",
  "identity": {
    "case_name": "Imbler v. Pachtman",
    "case_name_short": "Imbler",
    "case_name_full": "Imbler v. Pachtman, District Attorney",
    "input_case_name": "Imbler v. Pachtman",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-03-02",
    "year": 1976,
    "docket": "No. 74-5435",
    "cluster_id": 109387,
    "lead_opinion_id": 9426281,
    "sibling_ids": [],
    "absolute_url": "/opinion/109387/imbler-v-pachtman/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "424 U.S. 409",
      "volume": "424",
      "reporter": "U.S.",
      "page": "409",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 984",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "984",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "47 L. Ed. 2d 128",
        "volume": "47",
        "reporter": "L. Ed. 2d",
        "page": "128",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 25",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "25",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "424 U.S. 409",
        "volume": "424",
        "reporter": "U.S.",
        "page": "409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 984",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "984",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "47 L. Ed. 2d 128",
        "volume": "47",
        "reporter": "L. Ed. 2d",
        "page": "128",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 25",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "25",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "424 U.S. 409",
    "official_selection": {
      "court_class": "scotus",
      "selected": "424 U.S. 409",
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
    "date_created": "2026-07-06T13:53:37Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:53:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:53:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:53:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:53:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "imbler-v-pachtman--109387",
      "to_record_id": "Imbler v. Pachtman",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Imbler v. Pachtman

```
<opinion type="majority">
<author id="b464-8">Me. Justice Powell</author>
<p id="Av">delivered the opinion of the Court.</p>
<p id="b464-9">The question presented in this case is whether a state prosecuting attorney who acted within the scope of his duties in initiating and pursuing a criminal prosecution is amenable to suit under <span class="citation no-link">42 U. S. C. § 1983</span> for alleged deprivations of the defendant's constitutional rights. The Court of Appeals for the Ninth Circuit held that he is not. <span class="citation" data-id="9460865"><a href="/opinion/320782/paul-kern-imbler-v-richard-pachtman/" aria-description="Citation for case: Paul Kern Imbler v. Richard Pachtman">500 F. 2d 1301</a></span>. We affirm.</p>
<p id="b464-10">I</p>
<p id="b464-11">The events which culminated in this suit span many years and several judicial proceedings. They began in <page-number citation-index="1" label="411">*411</page-number>January 1961, when two men attempted to rob a Los Angeles market run by Morris Hasson. One shot and fatally wounded Hasson, and the two fled in different directions. Ten days later Leonard Lingo was killed while attempting a robbery in Pomona, Cal., but his two accomplices escaped. Paul Imbler, petitioner in this case, turned himself in the next day as one of those accomplices. Subsequent investigation led the Los Angeles District Attorney to believe that Imbler and Lingo had perpetrated the first crime as well, and that Imbler had killed Hasson. Imbler was charged with first-degree felony murder for Hasson’s death.</p>
<p id="b465-5">The State’s case consisted of eyewitness testimony from Hasson’s wife and identification testimony from three men who had seen Hasson’s assailants fleeing after the shooting. Mrs. Hasson was unable to identify the gunman because a hat had obscured his face, but from police photographs she identified the killer’s companion as Leonard Lingo. The primary identification witness was Alfred Costello, a passerby on the night of the crime, who testified that he had a clear view both as the gunman emerged from the market and again a few moments later when the fleeing gunman — after losing his hat — r turned to fire a shot at Costello<footnotemark>1</footnotemark> and to shed his coat<footnotemark>2</footnotemark> before continuing on. . Costello positively identified Imbler as the gunman. The second identification witness, an attendant at a parking lot through which the gunman ultimately escaped, testified that he had a side and front view as the man passed. Finally, a customer who was leaving Hasson’s market as the robbers entered <page-number citation-index="1" label="412">*412</page-number>testified that he had a good look then and as they exited moments later. All of these witnesses identified Imbler as the gunman, and the customer also identified the second man as Leonard Lingo. Rigorous cross-examination failed to shake any of these witnesses.<footnotemark>3</footnotemark></p>
<p id="b466-5">Imbler’s defense was an alibi. He claimed to have spent the night of the Hasson killing bar-hopping with several persons, and to have met Lingo for the first time the morning before the attempted robbery in Pomona. This testimony was corroborated by Mayes, the other accomplice in the Pomona robbery, who also claimed to have accompanied Imbler on the earlier rounds of the bars. The jury found Imbler guilty and fixed punishment at death.<footnotemark>4</footnotemark> On appeal the Supreme Court of California affirmed unanimously over numerous contentions of error. <em>People </em>v. <em>Imbler, </em><span class="citation" data-id="1131905"><a href="/opinion/1131905/people-v-imbler/" aria-description="Citation for case: People v. Imbler">57 Cal. 2d 711</a></span>, <span class="citation" data-id="1131905"><a href="/opinion/1131905/people-v-imbler/" aria-description="Citation for case: People v. Imbler">371 P. 2d 304</a></span> (1962).</p>
<p id="b466-6">Shortly thereafter Deputy District Attorney Richard Pachtman, who had been the prosecutor at Imbler’s trial and who is the respondent before this Court, wrote to the Governor of California describing evidence turned up after trial by himself and an investigator for the state correctional authority. In substance, the evidence consisted of newly discovered corroborating witnesses for Imbler’s alibi, as well as new revelations about prime witness Costello’s background which indicated that he was less trustworthy than he had represented originally to Pachtman and in his testimony. Pachtman noted that leads to some of this information had been available to Imbler’s counsel prior to trial but apparently <page-number citation-index="1" label="413">*413</page-number>had not been developed, that Costello had testified convincingly and withstood intense cross-examination, and that none of the new evidence was conclusive of Imbler’s innocence. He explained that he wrote from a belief that “a prosecuting attorney has a duty to be fair and see that all true facts, whether helpful to the case or not, should be presented.” <footnotemark>5</footnotemark></p>
<p id="b467-5">Imbler filed a state habeas corpus petition shortly after Pachtman’s letter. The Supreme Court of California appointed one of its retired justices as referee to hold a hearing, at which Costello was the main attraction. He recanted his trial identification of Imbler, and it also was established that on cross-examination and redirect he had painted a picture of his own background that was more flattering than trüe. Imbler’s corroborating witnesses, uncovered by prosecutor Pachtman’s investigations, also testified.</p>
<p id="b467-6">In his brief to the Supreme Court of California on this habeas petition, Imbler’s counsel described Pacht-man’s post-trial detective work as “[i]n the highest tradition of law enforcement and justice,” and as a premier example of “devotion to duty.” <footnotemark>6</footnotemark> But he also charged that the prosecution had knowingly used false testimony and suppressed material evidence at Imbler’s trial.<footnotemark>7</footnotemark> In a thorough opinion by then Justice Traynor, the Supreme Court of California unanimously rejected these contentions and denied the writ. <em>In re Imbler, </em><page-number citation-index="1" label="414">*414</page-number><span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/" aria-description="Citation for case: In Re Imbler">60 Cal. 2d 554</a></span>, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/" aria-description="Citation for case: In Re Imbler">387 P. 2d 6</a></span> (1963). The California court noted that the hearing record fully supported the referee’s finding that Costello’s recantation of his identification lacked credibility compared to the original identification itself, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#562" aria-description="Citation for case: In Re Imbler"><em>id., </em>at 562</a></span>, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#10" aria-description="Citation for case: In Re Imbler">387 P. 2d, at 10-11</a></span>, and that the new corroborating witnesses who appeared on Imbler’s behalf were unsure of their stories or were otherwise impeached, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#569" aria-description="Citation for case: In Re Imbler"><em>id., </em>at 569-570</a></span>, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#14" aria-description="Citation for case: In Re Imbler">387 P. 2d, at 14</a></span>.</p>
<p id="b468-5">In 1964, the year after denial of his state habeas petition, Imbler succeeded in having his death sentence overturned on grounds unrelated to this case. <em>In re Imbler, </em><span class="citation" data-id="9558198"><a href="/opinion/1194513/in-re-imbler/" aria-description="Citation for case: In Re Imbler">61 Cal. 2d 556</a></span>, <span class="citation" data-id="9558198"><a href="/opinion/1194513/in-re-imbler/" aria-description="Citation for case: In Re Imbler">393 P. 2d 687</a></span> (1964). Rather than resentence him, the State stipulated to life imprisonment. There the matter lay for several years, until in late 1967 or early 1968 Imbler filed a habeas corpus petition in Federal District Court based on the same contentions previously urged upon and rejected by the Supreme Court of California.</p>
<p id="b468-6">The District Court held no hearing. Instead, it decided the petition upon the record, including Pacht-man’s letter to the Governor and the transcript of the referee’s hearing ordered by the Supreme Court of California. Reading that record quite differently than had the seven justices of the State Supreme Court, the District Court found eight instances of state misconduct at Imbler’s trial, the cumulative effect of which required issuance of the writ. <em>Imbler </em>v. <em>Craven, </em><span class="citation" data-id="1868466"><a href="/opinion/1868466/imbler-v-craven/#812" aria-description="Citation for case: Imbler v. Craven">298 F. Supp. 795, 812</a></span> (CD Cal. 1969). Six occurred during Costello’s testimony and amounted in the court’s view to the culpable use by the prosecution of misleading or false testimony.<footnotemark>8</footnotemark> The other two instances were suppressions of <page-number citation-index="1" label="415">*415</page-number>evidence favorable to Imbler by a police fingerprint expert who testified at trial and by the police who investigated Hasson’s murder.<footnotemark>9</footnotemark> The District Court ordered that the writ of habeas corpus issue unless California retried Imbler within 60 days, and denied a petition for rehearing.</p>
<p id="b469-5">The State appealed to the Court of Appeals for the Ninth Circuit, claiming that the District Court had failed to give appropriate deference to the factual determinations of the Supreme Court of California as required by <span class="citation no-link">28 U. S. C. § 2254</span> (d). The Court of Appeals affirmed, finding that the District Court had merely “reached different conclusions than the state court in applying federal constitutional standards to [the] facts,” <em>Imbler </em>v. <em>California, </em><span class="citation" data-id="289539"><a href="/opinion/289539/paul-k-imbler-v-state-of-california/#632" aria-description="Citation for case: Paul K. Imbler v. State of California">424 F. 2d 631, 632</a></span>, and certiorari was denied, <span class="citation multiple-matches"><a href="/c/U.%20S./400/865/">400 U. S. 865</a></span> (1970). California chose not to retry Imbler, and he was released.</p>
<p id="b469-6">At this point, after a decade of litigation and with Imbler now free, the stage was set for the present suit. In April 1972, Imbler filed a civil rights action, under <span class="citation no-link">42 U. S. C. § 1983</span> and related statutes, against respondent Pachtman, the police fingerprint expert, and various other officers of the Los Angeles police force. He alleged <page-number citation-index="1" label="416">*416</page-number>that a conspiracy among them unlawfully to charge and convict him had caused him loss of liberty and other grievous injury. He demanded $2.7 million in actual and exemplary damages from each defendant, plus $15,-000 attorney’s fees.</p>
<p id="b470-5">Imbler attempted to incorporate into his complaint the District Court’s decision granting the writ of habeas corpus, and for the most part tracked that court’s opinion in setting out the overt acts in furtherance of the alleged conspiracy. The gravamen of his complaint against Pachtman was that he had “with intent, and on other occasions with negligence” allowed Costello to give false testimony as found by the District Court, and that the fingerprint expert’s suppression of evidence was “chargeable under federal law” to Pachtman. In addition Imbler claimed that Pachtman had prosecuted him with knowledge of a lie detector test that had “cleared” Imbler, and that Pachtman had used at trial a police artist’s sketch of Hasson’s killer made shortly after the crime and allegedly altered to resemble Imbler more closely after the investigation had focused upon him.</p>
<p id="b470-6">Pachtman moved under Fed. Rule Civ. Proc. 12 (b)(6) to have the complaint dismissed as to him. The District Court, noting that public prosecutors repeatedly had been held immune from civil liability for “acts done as part of their traditional official functions,” found that Pacht-man’s alleged acts fell into that category and granted his motion. Following the entry of final judgment as to Pachtman under Fed. Rule Civ. Proc. 54 (b), Imbler appealed to the Court of Appeals for the Ninth Circuit. That court, one judge dissenting, affirmed the District Court in an opinion finding Pachtman’s alleged acts to have been committed “during prosecutorial activities which can only be characterized as an ‘integral part of the judicial process,’ ” <span class="citation" data-id="9460865"><a href="/opinion/320782/paul-kern-imbler-v-richard-pachtman/#1302" aria-description="Citation for case: Paul Kern Imbler v. Richard Pachtman">500 F. 2d, at 1302</a></span>, quoting <page-number citation-index="1" label="417">*417</page-number><em>Marlowe </em>v. <em>Coakley, </em><span class="citation" data-id="282495"><a href="/opinion/282495/benjamin-f-marlowe-v-j-frank-coakley/" aria-description="Citation for case: Benjamin F. Marlowe v. J. Frank Coakley">404 F. 2d 70</a></span> (CA9 1968). We granted certiorari to consider the important and recurring issue of prosecutorial liability under the Civil Rights Act of 1871. <span class="citation multiple-matches"><a href="/c/U.%20S./420/945/">420 U. S. 945</a></span> (1975).</p>
<p id="b471-5">II</p>
<p id="b471-6">Title <span class="citation no-link">42 U. S. C. § 1983</span> provides that “[e]very person” who acts under color of state law to deprive another of a constitutional right shall be answerable to that person in a suit for damages.<footnotemark>10</footnotemark> The statute thus creates a species of tort liability that on its face admits of no immunities, and some have argued that it should be applied as stringently as it reads.<footnotemark>11</footnotemark> But that view has not prevailed.</p>
<p id="b471-7">This Court first considered the implications of the statute’s literal sweep in <em>Tenney </em>v. <em>Brandhove, </em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">341 U. S. 367</a></span> (1951). There it was claimed that members of a state legislative committee had called the plaintiff to appear before them, not for a proper legislative purpose, but to intimidate him into silence on certain matters of public concern, and thereby had deprived him of his constitutional rights. Because legislators in both England and this country had enjoyed absolute immunity for their official actions, <em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">Tenney</a></span> </em>squarely presented the issue of whether the Reconstruction Congress had intended to <page-number citation-index="1" label="418">*418</page-number>restrict the availability in § 1983 suits of those immunities which historically, and for reasons of public policy, had been accorded to various categories of officials. The Court concluded that immunities “well grounded in history and reason” had not been abrogated “by covert inclusion in the general language” of § 1983. <span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#376" aria-description="Citation for case: Tenney v. Brandhove">341 U. S., at 376</a></span>. Regardless of any unworthy purpose animating their actions, legislators were held to enjoy under this statute their usual immunity when acting “in a field where legislators traditionally have power to act.” <em>Id., </em>at 379.</p>
<p id="b472-5">The decision in <em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">Tenney</a></span> </em>established that § 1983 is to be read in harmony with general principles of tort immunities and defenses rather than in derogation of them. Before today the Court has had occasion to consider the liability of several types of government officials in addition to legislators. The common-law absolute immunity of judges for “acts committed within their judicial jurisdiction,” see <em>Bradley </em>v. <em>Fisher, </em><span class="citation" data-id="9416839"><a href="/opinion/88468/bradley-v-fisher/" aria-description="Citation for case: Bradley v. Fisher">13 Wall. 335</a></span> (1872), was found to be preserved under § 1983 in <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#554" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547, 554-555</a></span> (1967).<footnotemark>12</footnotemark> In the same case, local police officers sued for a deprivation of liberty resulting from unlawful arrest were held to enjoy under § 1983 a “good faith and probable cause” defense coextensive with their defense to false arrest actions at <page-number citation-index="1" label="419">*419</page-number>common law. <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#555" aria-description="Citation for case: Pierson v. Ray">386 U. S., at <em>555-557. </em></a></span>We found qualified immunities appropriate in two recent cases.<footnotemark>13</footnotemark> In <em>Scheuer </em>v. <em>Rhodes, </em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232</a></span> (1974), we concluded that the Governor and other executive officials of a State had a qualified immunity that varied with “the scope of discretion and responsibilities of the office and all the circumstances as they reasonably appeared at the time of the action. . . .” <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#247" aria-description="Citation for case: Scheuer v. Rhodes"><em>Id., </em>at 247</a></span>.<footnotemark>14</footnotemark> Last Term in <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308</a></span> (1975), we held that school officials, in the context of imposing disciplinary penalties, were not liable so long as they could not reasonably have known that their action violated students’ clearly established constitutional rights, and provided they did not act with malicious intention to cause constitutional or other injury. <span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#322" aria-description="Citation for case: Wood v. Strickland"><em>Id., </em>at 322</a></span>; cf. <em>O'Connor </em>v. <em>Donaldson, </em><span class="citation" data-id="9842006"><a href="/opinion/109303/oconnor-v-donaldson/#577" aria-description="Citation for case: O&#x27;Connor v. Donaldson">422 U. S. 563, 577</a></span> (1975). In <em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">Scheuer</a></span> </em>and in <em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">Wood</a></span>, </em>as in the two earlier cases, the considerations underlying the nature of the immunity of the respective officials in suits at common law led to essentially the same immunity under § 1983.<footnotemark>15</footnotemark> See <span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#318" aria-description="Citation for case: Wood v. Strickland">420 U. S., at 318-321</a></span>; <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#239" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S., at 239-247</a></span>, and n. 4.</p>
<p id="b474-7"><page-number citation-index="1" label="420">*420</page-number>III</p>
<p id="b474-1">This case marks our first opportunity to address the § 1983 liability of a state prosecuting officer. The Courts of Appeals, however, have confronted the issue many times and under varying circumstances. Although the precise contours of their holdings have been unclear at times, at bottom they are virtually unanimous that a prosecutor enjoys absolute immunity from § 1983 suits for damages when he acts within the scope of his prosecutorial duties.<footnotemark>16</footnotemark> These courts sometimes have described the prosecutor’s immunity as a form of “quasi-judicial” immunity and referred to it as derivative of the immunity of judges recognized in <em>Pierson </em>v. <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Ray, supra.</a></span></em><footnotemark><em>17</em></footnotemark><em> </em>Petitioner focuses upon the “quasi-judicial” characterization, and contends that it illustrates a fundamental illogic in according absolute immunity to a prosecutor. He argues that the prosecutor, ás a member of the executive branch, cannot claim the immunity reserved for the judiciary, but only a qualified immunity <page-number citation-index="1" label="421">*421</page-number>akin to that accorded other executive officials in this Court’s previous cases.</p>
<p id="b475-5">Petitioner takes an overly simplistic approach to the issue of prosecutorial liability. As noted above, our earlier decisions on § 1983 immunities were not products of judicial fiat that officials in different branches of government are differently amenable to suit under § 1983. Rather, each was predicated upon a considered inquiry into the immunity historically accorded the relevant official at common law and the interests behind it. The liability of a state prosecutor under § 1983 must be determined in the same manner.</p>
<p id="b475-6">A</p>
<p id="b475-7">The function of a prosecutor that most often invites a common-law tort action is his decision to initiate a prosecution, as this may lead to a suit for malicious prosecution if the State’s case misfires. The first American case to address the question of a prosecutor’s amenability to such an action was <em>Griffith </em>v. <em>Slinkard, </em><span class="citation" data-id="7052941"><a href="/opinion/7144738/griffith-v-slinkard/" aria-description="Citation for case: Griffith v. Slinkard">146 Ind. 117</a></span>, <span class="citation" data-id="7052941"><a href="/opinion/7144738/griffith-v-slinkard/" aria-description="Citation for case: Griffith v. Slinkard">44 N. E. 1001</a></span> (1896).<footnotemark>18</footnotemark> The complaint charged that a local prosecutor without probable cause added the plaintiff’s name to a grand jury true bill after the grand jurors had refused to indict him, with the result that the plaintiff was arrested and forced to appear in court repeatedly before the charge finally was <em>nolle prossed. </em>Despite allegations of malice, the Supreme Court of Indiana dismissed the action on the ground that the prosecutor was absolutely immune. <span class="citation" data-id="7052941"><a href="/opinion/7144738/griffith-v-slinkard/#122" aria-description="Citation for case: Griffith v. Slinkard"><em>Id., </em>at 122</a></span>, <span class="citation" data-id="7052941"><a href="/opinion/7144738/griffith-v-slinkard/#1002" aria-description="Citation for case: Griffith v. Slinkard">44 N. E., at 1002</a></span>.</p>
<p id="b476-4"><page-number citation-index="1" label="422">*422</page-number>The <em><span class="citation" data-id="7052941"><a href="/opinion/7144738/griffith-v-slinkard/" aria-description="Citation for case: Griffith v. Slinkard">Griffith</a></span> </em>view on prosecutorial immunity became the clear majority rule on the issue.<footnotemark>19</footnotemark> The question eventually came to this Court on writ of certiorari to the Court of Appeals for the Second Circuit. In <em>Yaselli </em>v. <em>Goff, </em><span class="citation" data-id="1490367"><a href="/opinion/1490367/yaselli-v-goff/" aria-description="Citation for case: Yaselli v. Goff">12 F. 2d 396</a></span> (1926), the claim was that the defendant, a Special Assistant to the Attorney General of the United States, maliciously and without probable cause procured plaintiff’s grand jury indictment by the willful introduction of false and misleading evidence. Plaintiff sought some $300,000 in damages for having been subjected to the rigors of a trial, in which the court ultimately directed a verdict against the Government. The District Court dismissed the complaint, and the Court of Appeals affirmed. After reviewing the development of the doctrine of prosecutorial immunity, <span class="citation" data-id="1490367"><a href="/opinion/1490367/yaselli-v-goff/#399" aria-description="Citation for case: Yaselli v. Goff"><em>id., </em>at 399-404</a></span>, that court stated:</p>
<blockquote id="b476-5">“In our opinion the law requires us to hold that a special assistant to the Attorney General of the United States, in the performance of the duties imposed upon him by law, is immune from a civil action for malicious prosecution based on an indictment and prosecution, although it results in a verdict of not guilty rendered by a jury. The immunity is absolute, and is grounded on principles of public policy.” <span class="citation" data-id="1490367"><a href="/opinion/1490367/yaselli-v-goff/#406" aria-description="Citation for case: Yaselli v. Goff"><em>Id., </em>at 406</a></span>.</blockquote>
<p id="b476-6">After briefing and oral argument, this Court affirmed the Court of Appeals in a <em>per curiam </em>opinion. <em>Yaselli </em>v. <em>Goff, </em><span class="citation" data-id="8146727"><a href="/opinion/8184801/yaselli-v-goff/" aria-description="Citation for case: Yaselli v. Goff">275 U. S. 503</a></span> (1927).</p>
<p id="b476-7">The common-law immunity of a prosecutor is based upon the same considerations that underlie the common-<page-number citation-index="1" label="423">*423</page-number>law immunities of judges and grand jurors acting within the scope of their duties.<footnotemark>20</footnotemark> These include concern that harassment by unfounded litigation would cause a deflection of the prosecutor’s energies from his public duties, and the possibility that he would shade his decisions instead of exercising the independence of judgment required by his public trust. One court expressed both considerations as follows:</p>
<blockquote id="b477-5">“The office of public prosecutor is one which must be administered with courage and independence. Yet how can this be if the prosecutor is made subject to suit by those whom he accuses and fails to convict? To allow this would open the way for unlimited harassment and embarrassment of the most conscientious officials by those who would profit thereby. There would be involved in every case the possible consequences of a failure to obtain a con<page-number citation-index="1" label="424">*424</page-number>viction. There would always be a question of possible civil action in case the prosecutor saw fit to move dismissal of the case. . . . The apprehension of such consequences would tend toward great uneasiness and toward weakening the fearless and impartial policy which should characterize the administration of this office. The work of the prosecutor would thus be impeded and we would have moved away from the desired objective of stricter and fairer law enforcement.” <em>Pearson </em>v. <em>Reed, </em><span class="citation" data-id="1422703"><a href="/opinion/1422703/pearson-v-reed/#287" aria-description="Citation for case: Pearson v. Reed">6 Cal. App. 2d 277, 287</a></span>, <span class="citation" data-id="1422703"><a href="/opinion/1422703/pearson-v-reed/#597" aria-description="Citation for case: Pearson v. Reed">44 P. 2d 592, 597</a></span> (1935).</blockquote>
<p id="b478-5">See also <em>Yaselli </em>v. <em>Goff, </em><span class="citation" data-id="1490367"><a href="/opinion/1490367/yaselli-v-goff/#404" aria-description="Citation for case: Yaselli v. Goff">12 F. 2d, at 404-406</a></span>.</p>
<p id="b478-6">B</p>
<p id="b478-7">The common-law rule of immunity is thus well settled.<footnotemark>21</footnotemark> We now must determine whether the same considerations of public policy that underlie the common-law rule likewise countenance absolute immunity under § 1983. We think they do.</p>
<p id="b478-8">If a prosecutor had only a qualified immunity, the threat of § 1983 suits would undermine performance of his duties no less than would the threat of common-law suits for malicious prosecution. A prosecutor is duty bound to exercise his best judgment both in deciding which suits to bring and in conducting them in court. The public trust of the prosecutor’s office would suffer if he were constrained in making every decision by the consequences in terms of his own potential liability in a <page-number citation-index="1" label="425">*425</page-number>suit for damages. Such suits could be expected with some frequency, for a defendant often will transform his resentment at being prosecuted into the ascription of improper and malicious actions to the State’s advocate. Cf. <em>Bradley </em>v. <em>Fisher, </em><span class="citation" data-id="9416839"><a href="/opinion/88468/bradley-v-fisher/#348" aria-description="Citation for case: Bradley v. Fisher">13 Wall., at 348</a></span>; <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#554" aria-description="Citation for case: Pierson v. Ray">386 U. S., at 554</a></span>. Further, if the prosecutor could be made to answer in court each time such a person charged him with wrongdoing, his energy and attention would be diverted from the pressing duty of enforcing the criminal law.</p>
<p id="b479-5">Moreover, suits that survived the pleadings would pose substantial danger of liability even to the honest prosecutor. The prosecutor’s possible knowledge of a witness’ falsehoods, the materiality of evidence not revealed to the defense, the propriety of a closing argument, and— ultimately in every case — the likelihood that prosecu-torial misconduct so infected a trial as to deny due process, are typical of issues with which judges struggle in actions for post-trial relief, sometimes to differing conclusions.<footnotemark>22</footnotemark> The presentation of such issues in a § 1983 action often would require a virtual retrial of the criminal offense in a new forum, and the resolution of some technical issues by the lay jury. It is fair to say, we think, that the honest prosecutor would face greater difficulty in meeting the standards of qualified immunity than other executive or administrative officials. Frequently acting under serious constraints of time and even information, a prosecutor inevitably makes many decisions that could engender colorable claims of constitutional deprivation. Defending these decisions, often years after they were made, could impose unique <page-number citation-index="1" label="426">*426</page-number>and intolerable burdens upon a prosecutor responsible annually for hundreds of indictments and trials. Cf. <em>Bradley </em>v. <span class="citation" data-id="9416839"><a href="/opinion/88468/bradley-v-fisher/#349" aria-description="Citation for case: Bradley v. Fisher"><em>Fisher, supra, </em>at 349</a></span>.</p>
<p id="b480-5">The affording of only a qualified immunity to the prosecutor also could have an adverse effect upon the functioning of the criminal justice system. Attaining the system’s goal of accurately determining guilt or innocence requires that both the prosecution and the defense have wide discretion in the conduct of the trial and the presentation of evidence.<footnotemark>23</footnotemark> The veracity of witnesses in criminal cases frequently is subject to doubt before and after they testify, as is illustrated by the history of this case. If prosecutors were hampered in exercising their judgment as to the use of such witnesses by concern about resulting personal liability, the triers of fact in criminal cases often would be denied relevant evidence.<footnotemark>24</footnotemark></p>
<p id="b481-4"><page-number citation-index="1" label="427">*427</page-number>The ultimate fairness of the operation of the system itself could be weakened by subjecting prosecutors to § 1983 liability. Various post-trial procedures are available to determine whether an accused has received a fair trial. These procedures include the remedial powers of the trial judge, appellate review, and state and federal post-conviction collateral remedies. In all of these the attention of the reviewing judge or tribunal is focused primarily on whether there was a fair trial under law. This focus should not be blurred by even the subconscious knowledge that a post-trial decision in favor of the accused might result in the prosecutor’s being called upon to respond in damages for his error or mistaken judgment.<footnotemark>25</footnotemark></p>
<p id="b481-5">We conclude that the considerations outlined above dictate the same absolute immunity under § 1983 that the prosecutor enjoys at common law. To be sure, this immunity does leave the genuinely wronged defendant without civil redress against a prosecutor whose malicious or dishonest action deprives him of liberty. But the alternative of qualifying a prosecutor’s immunity would disserve the broader public interest. It would prevent the vigorous and fearless performance of the prosecutor’s duty that is essential to the proper function<page-number citation-index="1" label="428">*428</page-number>ing of the criminal justice system.<footnotemark>26</footnotemark> Moreover, it often would prejudice defendants in criminal cases by skewing post-conviction judicial decisions that should be made with the sole purpose of insuring justice. With the issue thus framed, we find ourselves in agreement with Judge Learned Hand, who wrote of the prosecutor’s immunity from actions for malicious prosecution:</p>
<blockquote id="b482-5">“As is so often the case, the answer must be found in a balance between the evils inevitable in either alternative. In this instance it has been thought in the end better to leave unredressed the wrongs done by dishonest officers than to subject those who try to do their duty to the constant dread of retaliation.” <em>Gregoire </em>v. <em>Biddle, </em><span class="citation" data-id="1507366"><a href="/opinion/1507366/gregoire-v-biddle/#581" aria-description="Citation for case: Gregoire v. Biddle">177 F. 2d 579, 581</a></span> (CA2 1949), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./339/949/">339 U. S. 949</a></span> (1950).</blockquote>
<p id="b482-6">See <em>Yaselli </em>v. <em>Goff, </em><span class="citation" data-id="1490367"><a href="/opinion/1490367/yaselli-v-goff/#404" aria-description="Citation for case: Yaselli v. Goff">12 F. 2d, at 404</a></span>; cf. <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#320" aria-description="Citation for case: Wood v. Strickland">420 U. S., at 320</a></span>.<footnotemark>27</footnotemark></p>
<p id="b482-7">We emphasize that the immunity of prosecutors from <page-number citation-index="1" label="429">*429</page-number>liability in suits under § 1983 does not leave the public powerless to deter misconduct or to punish that which occurs. This Court has never suggested that the policy considerations which compel civil immunity for certain governmental officials also place them beyond the reach of the criminal law. Even judges, cloaked with absolute civil immunity for centuries, could be punished criminally for willful deprivations of constitutional rights on the strength of <span class="citation no-link">18 U. S. C. § 242</span>,<footnotemark>28</footnotemark> the criminal analog of § 1983. <em>O’Shea </em>v. <em>Littleton, </em><span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/#503" aria-description="Citation for case: O&#x27;Shea v. Littleton">414 U. S. 488, 503</a></span> (1974); cf. <em>Gravel </em>v. <em>United States, </em><span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/#627" aria-description="Citation for case: Gravel v. United States">408 U. S. 606, 627</a></span> (1972). The prosecutor would fare no better for his willful acts.<footnotemark>29</footnotemark> Moreover, a prosecutor stands perhaps unique, among officials whose acts could deprive persons of constitutional rights, in his amenability to professional discipline by an association of his peers.<footnotemark>30</footnotemark> These checks undermine the argument that the imposition of civil liability is the only way to insure that prosecutors are mindful of the constitutional rights of persons accused of crime.</p>
<p id="b484-4"><page-number citation-index="1" label="430">*430</page-number>IV</p>
<p id="b484-5">It remains to delineate the boundaries of our holding. As noted, <em>supra, </em>at 416, the Court of Appeals emphasized that each of respondent’s challenged activities was an “integral part of the judicial process.” 600 F. 2d, at 1302. The purpose of the Court of Appeals’ focus upon the functional nature of the activities rather than respondent’s status was to distinguish and leave standing those cases, in its Circuit and in some others, which hold that a prosecutor engaged in certain investigative activities enjoys, not the absolute immunity associated with the judicial process, but only a good-faith defense comparable to the policeman’s.<footnotemark>31</footnotemark> See <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#557" aria-description="Citation for case: Pierson v. Ray">386 U. S., at 557</a></span>. We agree with the Court of Appeals that respondent’s activities were intimately associated with the judicial phase of the criminal process, and thus were functions to which the reasons for absolute immunity apply with full force.<footnotemark>32</footnotemark> We have no occasion to consider whether like or similar reasons require immunity for those aspects of the prosecutor’s responsibility that cast him in the role of an administrator or investigative <page-number citation-index="1" label="431">*431</page-number>officer rather than that of advocate.<footnotemark>33</footnotemark> We hold only that in initiating a prosecution and in presenting the State’s case, the prosecutor is immune from a civil suit for damages under § 1983.<footnotemark>34</footnotemark> The judgment of the Court of Appeals for the Ninth Circuit accordingly is</p>
<p id="b485-5">
<em>Affirmed.</em>
</p>
<p id="b486-4"><page-number citation-index="1" label="432">*432</page-number>Mr. Justice Stevens took no part in the consideration or decision of this case.</p>
<footnote label="1">
<p id="b465-6"> This shot formed the basis of a second count against Imbler for assault, which was tried with the murder count.</p>
</footnote>
<footnote label="2">
<p id="b465-7"> This coat, identified by Mrs. Hasson as that worn by her husband’s assailant, yielded a gun determined by ballistics evidence to be the murder weapon.</p>
</footnote>
<footnote label="3">
<p id="b466-7"> A fourth man who saw Hasson’s killer leaving the scene identified Imbler in a pretrial lineup, but police were unable to find him at the time of trial.</p>
</footnote>
<footnote label="4">
<p id="b466-8"> Imbler also received a 10-year prison term on the assault charge. See n. 1, <em>supra.</em></p>
</footnote>
<footnote label="5">
<p id="b467-7"> Brief for Respondent, App. A, p. 6. The record does not indicate what specific action was taken in response to Pachtman’s letter. We do note that the letter was dated August 17, 1962, and that Imbler’s execution, scheduled for September 12, 1962, subsequently was stayed. The letter became a part of the permanent record in the case available to the courts in all subsequent litigation.</p>
</footnote>
<footnote label="6">
<p id="b467-8"> Brief for Respondent 5.</p>
</footnote>
<footnote label="7">
<p id="b467-9"> See generally <em>Napue </em>v. <em>Illinois, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264</a></span> (1959); <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963).</p>
</footnote>
<footnote label="8">
<p id="b468-7"> The District Court found that Costello had given certain ambiguous or misleading testimony, and had lied flatly about his criminal record, his education, and his current income. As to the misleading testimony, the court found that either Pachtman or a <page-number citation-index="1" label="415">*415</page-number>police officer present in the courtroom knew it was misleading. As to the false testimony, the District Court concluded that Pachtman had “cause to suspect” its falsity although, apparently, no actual knowledge thereof. See <span class="citation" data-id="1868466"><a href="/opinion/1868466/imbler-v-craven/#799" aria-description="Citation for case: Imbler v. Craven">298 F. Supp., at 799-807</a></span>. The Supreme Court of California earlier had addressed and rejected allegations based on many of the same parts of Costello's testimony. It found either an absence of falsehood or an absence of prosecutorial knowledge in each instance. See <em>In re Imbler, </em><span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#562" aria-description="Citation for case: In Re Imbler">60 Cal. 2d 554, 562-565</a></span>, and n. 3, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#10" aria-description="Citation for case: In Re Imbler">387 P. 2d 6, 10-12</a></span>, and n. 3 (1963).</p>
</footnote>
<footnote label="9">
<p id="b469-8"> See <span class="citation" data-id="1868466"><a href="/opinion/1868466/imbler-v-craven/#809" aria-description="Citation for case: Imbler v. Craven">298 F. Supp., at 809-811</a></span>. The Supreme Court of California earlier had rejected similar allegations. See <em>In re Imbler, supra, </em>at 566-568, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#12" aria-description="Citation for case: In Re Imbler">387 P. 2d, at 12-13</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b471-8"> Title <span class="citation no-link">42 U. S. C. § 1983</span>, originally passed as § 1 of the Civil Rights Act of 1871, <span class="citation no-link">17 Stat. 13</span>, reads in full:</p>
<blockquote id="b471-9">“Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory, subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress.”</blockquote>
</footnote>
<footnote label="11">
<p id="b471-10"> See, e. <em>g., Pierson </em>v. <em>Ray, </em><span class="citation multiple-matches"><a href="/c/U.%20S./386/647/">386 U. S. 647</a></span>, 559 (1967) (Douglas, J., dissenting); <em>Tenney </em>v. <em>Brandhove, </em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#382" aria-description="Citation for case: Tenney v. Brandhove">341 U. S. 367, 382-383</a></span> (1951) (Douglas, J., dissenting).</p>
</footnote>
<footnote label="12">
<p id="b472-6"> The Court described the immunity of judges as follows:</p>
<blockquote id="b472-7">“Few doctrines were more solidly established at common law than the immunity of judges from liability for damages for acts committed within their judicial jurisdiction, as this Court recognized when it adopted the doctrine, in <em>Bradley </em>v. <em>Fisher, </em><span class="citation" data-id="9416839"><a href="/opinion/88468/bradley-v-fisher/" aria-description="Citation for case: Bradley v. Fisher">13 Wall. 335</a></span> (1872). This immunity applies even when the judge is accused of acting maliciously and corruptly, and it ‘is not for the protection or benefit of a malicious or corrupt judge, but for the benefit of the public, whose interest it is that the judges should be at liberty to exercise their functions with independence and without fear of consequences.’ ” <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#553" aria-description="Citation for case: Pierson v. Ray">386 U. S., at 553-554</a></span> (citation omitted).</blockquote>
</footnote>
<footnote label="13">
<p id="b473-5"> The procedural difference between the absolute and the qualified immunities is important. An absolute immunity defeats a suit at the outset, so long as the official’s actions were within the scope of the immunity. The fate of an official with qualified immunity depends upon the circumstances and motivations of his actions, as established by the evidence at trial. See <em>Scheuer </em>v. <em>Rhodes, </em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#238" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232, 238-239</a></span> (1974); <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#320" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308, 320-322</a></span> (1975).</p>
</footnote>
<footnote label="14">
<p id="b473-6"> The elements of this immunity were described in <em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">Scheuer</a></span> </em>as follows:</p>
<blockquote id="b473-7">“It is the existence of reasonable grounds for the belief formed at the time and in light of all the circumstances, coupled with good faith belief, that affords a basis for qualified immunity of executive officers for acts performed in the course of official conduct.” <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#247" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S., at 247-248</a></span>.</blockquote>
</footnote>
<footnote label="15">
<p id="b473-8"> In <em>Tenney </em>v. <em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">Brandhove</a></span>, </em>of course, the Court looked to the <page-number citation-index="1" label="420">*420</page-number>immunity accorded legislators by the Federal and State Constitutions, as well as that developed by the common law. <span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#372" aria-description="Citation for case: Tenney v. Brandhove">341 U. S., at 372-375</a></span>. See generally <em>Doe </em>v. <em>McMillan, </em><span class="citation" data-id="9425326"><a href="/opinion/108802/doe-v-mcmillan/" aria-description="Citation for case: Doe v. McMillan">412 U. S. 306</a></span> (1973).</p>
</footnote>
<footnote label="16">
<p id="b474-3"> <em>Fanale </em>v. <em>Sheeky, </em><span class="citation multiple-matches"><a href="/c/F.%202d/385/866/">385 F. 2d 866</a></span>, 868 (CA2 1967); <em>Bauers </em>v. <em>Heisel, </em><span class="citation" data-id="9451819"><a href="/opinion/272024/william-j-bauers-jr-v-herbert-t-heisel-jr/" aria-description="Citation for case: William J. Bauers, Jr. v. Herbert T. Heisel, Jr">361 F. 2d 581</a></span> (CA3 1966), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./386/1021/">386 U. S. 1021</a></span> (1967); <em>Carmack </em>v. <em>Gibson, </em><span class="citation" data-id="272579"><a href="/opinion/272579/herbert-b-carmack-v-wallace-gibson-judge-circuit-court-of-jefferson/#864" aria-description="Citation for case: Herbert B. Carmack v. Wallace Gibson, Judge, Circuit...">363 F. 2d 862, 864</a></span> (CA5 1966); <em>Tyler </em>v. <em>Witkowski, </em><span class="citation" data-id="325501"><a href="/opinion/325501/maurice-tyler-v-joseph-witkowski/#450" aria-description="Citation for case: Maurice Tyler v. Joseph Witkowski">511 F. 2d 449, 450-451</a></span> (CA7 1975); <em>Barnes </em>v. <em>Dorsey, </em><span class="citation" data-id="312106"><a href="/opinion/312106/eugene-barnes-v-sam-elmer-dorsey/#1060" aria-description="Citation for case: Eugene Barnes v. Sam Elmer Dorsey">480 F. 2d 1057, 1060</a></span> (CA8 1973); <em>Kostal </em>v. <em>Stoner, </em><span class="citation" data-id="6921515"><a href="/opinion/7020406/kostal-v-stoner/#493" aria-description="Citation for case: Kostal v. Stoner">292 F. 2d 492, 493</a></span> (CA10 1961), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./369/868/">369 U. S. 868</a></span> (1962); cf. <em>Guerro </em>v. <em>Mulhearn, </em><span class="citation" data-id="320118"><a href="/opinion/320118/thomas-a-guerro-v-roger-f-mulhearn-ralph-f-andrews-v-kathy-decote/#1255" aria-description="Citation for case: Thomas A. Guerro v. Roger F. Mulhearn, Ralph F. Andrews...">498 F. 2d 1249, 1255-1256</a></span> (CA1 1974); <em>Weathers </em>v. <em>Ebert, </em><span class="citation" data-id="322638"><a href="/opinion/322638/roy-w-weathers-v-paul-ebert/#515" aria-description="Citation for case: Roy W. Weathers v. Paul Ebert">505 F. 2d 514, 515-516</a></span> (CA4 1974). But compare <em>Hurlburt </em>v. <em>Graham, </em><span class="citation" data-id="262073"><a href="/opinion/262073/edward-joseph-hurlburt-an-infant-over-the-age-of-14-years-by-dorothy-e/" aria-description="Citation for case: Edward Joseph Hurlburt, an Infant Over the Age of 14...">323 F. 2d 723</a></span> (CA6 1963), with <em>Hilliard </em>v. <em>Williams, </em><span class="citation" data-id="305314"><a href="/opinion/305314/lilly-mae-onie-lee-whitelaw-hilliard-v-john-l-williams/" aria-description="Citation for case: Lilly Mae Onie Lee Whitelaw Hilliard v. John L. Williams">465 F. 2d 1212</a></span> (CA6), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./409/1029/">409 U. S. 1029</a></span> (1972). See Part IV, <em>infra.</em></p>
</footnote>
<footnote label="17">
<p id="AqS"> <em>E. g., Tyler </em>v. <span class="citation" data-id="325501"><a href="/opinion/325501/maurice-tyler-v-joseph-witkowski/#450" aria-description="Citation for case: Maurice Tyler v. Joseph Witkowski"><em>Witkowski, supra, </em>at 450</a></span>; <em>Kostal </em>v. <span class="citation" data-id="6921515"><a href="/opinion/7020406/kostal-v-stoner/#493" aria-description="Citation for case: Kostal v. Stoner"><em>Stoner, supra, </em>at 493</a></span>; <em>Hampton </em>v. <em>City of Chicago, </em><span class="citation" data-id="8890918"><a href="/opinion/8903845/hampton-v-city-of-chicago/#608" aria-description="Citation for case: Hampton v. City of Chicago">484 F. 2d 602, 608</a></span> (CA7 1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./415/917/">415 U. S. 917</a></span> (1974). See n. <em>20, infra.</em></p>
</footnote>
<footnote label="18">
<p id="b475-8"> The Supreme Court of Indiana in <em><span class="citation" data-id="7052941"><a href="/opinion/7144738/griffith-v-slinkard/" aria-description="Citation for case: Griffith v. Slinkard">Griffith</a></span> </em>cited an earlier Massachusetts decision, apparently as authority for its own holding. But that case, <em>Parker </em>v. <em>Huntington, </em><span class="citation" data-id="6410355"><a href="/opinion/6536635/parker-v-huntington/" aria-description="Citation for case: Parker v. Huntington">68 Mass. 124</a></span> (1854), involved the elements of a malicious prosecution cause of action rather than the immunity of a prosecutor. See also Note, <span class="citation no-link">73 U. Pa. L. Rev. 300</span>, 304 (1925).</p>
</footnote>
<footnote label="19">
<p id="b476-8"> <em>Smith </em>v. <em>Parman, </em><span class="citation" data-id="7903738"><a href="/opinion/7952516/smith-v-parman/" aria-description="Citation for case: Smith v. Parman">101 Kan. 115</a></span>, <span class="citation" data-id="7903738"><a href="/opinion/7952516/smith-v-parman/" aria-description="Citation for case: Smith v. Parman">165 P. 663</a></span> (1917); <em>Semmes </em>v. <em>Collins, </em><span class="citation" data-id="7993445"><a href="/opinion/8037139/semmes-v-collins/" aria-description="Citation for case: Semmes v. Collins">120 Miss. 265</a></span>, <span class="citation" data-id="7993445"><a href="/opinion/8037139/semmes-v-collins/" aria-description="Citation for case: Semmes v. Collins">82 So. 145</a></span> (1919); <em>Kittler </em>v. <em>Kelsch, </em><span class="citation" data-id="3679965"><a href="/opinion/3933190/kittler-v-kelsch/" aria-description="Citation for case: Kittler v. Kelsch">56 N. D. 227</a></span>, <span class="citation" data-id="3679965"><a href="/opinion/3933190/kittler-v-kelsch/" aria-description="Citation for case: Kittler v. Kelsch">216 N. W. 898</a></span> (1927); <em>Watts </em>v. <em>Gerking, </em><span class="citation" data-id="6908241"><a href="/opinion/7008041/watts-v-gerking/" aria-description="Citation for case: Watts v. Gerking">111 Ore. 654</a></span>, <span class="citation no-link">228 P. 135</span> (1924) (on rehearing). Contra, <em>Leong Yau </em>v. <em>Carden, </em><span class="citation" data-id="6485314"><a href="/opinion/6609156/leong-yau-v-carden/" aria-description="Citation for case: Leong Yau v. Carden">23 Haw. 362</a></span> (1916).</p>
</footnote>
<footnote label="20">
<p id="b477-6"> The immunity of a judge for acts within his jurisdiction has roots extending to the earliest days of the common law. See <em>Floyd </em>v. <em>Barker, </em>12 Coke 23, 77 Eng. Rep. 1305 (1608). Chancellor Kent traced some of its history in <em>Yates </em>v. <em>Lansing, </em><span class="citation" data-id="5472513"><a href="/opinion/5627426/yates-v-lansing/" aria-description="Citation for case: Yates v. Lansing">5 Johns. 282</a></span> (N. Y. 1810), and this Court accepted the rule of judicial immunity in <em>Bradley </em>v. <em>Fisher, </em><span class="citation" data-id="9416839"><a href="/opinion/88468/bradley-v-fisher/" aria-description="Citation for case: Bradley v. Fisher">13 Wall. 335</a></span> (1872). See n. 12, <em>supra. </em>The immunity of grand jurors, an almost equally venerable common-law tenet, see <em>Floyd </em>v. <em>Barker, supra, </em>also has been adopted in this country. See, <em>e. g., Turpen </em>v. <em>Booth, </em><span class="citation" data-id="5439895"><a href="/opinion/5597013/turpen-v-booth/" aria-description="Citation for case: Turpen v. Booth">56 Cal. 65</a></span> (1880); <em>Hunter </em>v. <em>Mathis, </em><span class="citation" data-id="7039285"><a href="/opinion/7131846/hunter-v-mathis/" aria-description="Citation for case: Hunter v. Mathis">40 Ind. 356</a></span> (1872). Courts that have extended the same immunity to the prosecutor have sometimes remarked on the fact that all three officials — judge, grand juror, and prosecutor — exercise a discretionary judgment on the basis of evidence presented to them. <em>Smith </em>v. <em><span class="citation" data-id="7903738"><a href="/opinion/7952516/smith-v-parman/" aria-description="Citation for case: Smith v. Parman">Parman, supra;</a></span> Watts </em>v. <em><span class="citation" data-id="6908241"><a href="/opinion/7008041/watts-v-gerking/" aria-description="Citation for case: Watts v. Gerking">Gerking, supra.</a></span> </em>It is the functional comparability of their judgments to those of the judge that has resulted in both grand jurors and prosecutors being referred to as “quasi-judicial” officers, and their immunities being termed “quasi-judicial” as well. See, <em>e. g., Turpen </em>v. <span class="citation" data-id="5439895"><a href="/opinion/5597013/turpen-v-booth/#69" aria-description="Citation for case: Turpen v. Booth"><em>Booth, supra, </em>at 69</a></span>; <em>Watts </em>v. <span class="citation" data-id="6908241"><a href="/opinion/7008041/watts-v-gerking/#661" aria-description="Citation for case: Watts v. Gerking"><em>Gerking, supra, </em>at 661</a></span>, 228 P., at 138.</p>
</footnote>
<footnote label="21">
<p id="b478-9"> See, <em>e. g., Gregoire </em>v. <em>Biddle, </em><span class="citation" data-id="1507366"><a href="/opinion/1507366/gregoire-v-biddle/" aria-description="Citation for case: Gregoire v. Biddle">177 F. 2d 579</a></span> (CA2 1949), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./339/949/">339 U. S. 949</a></span> (1950); <em>Cooper </em>v. <em>O’Connor, </em>69 App. D. C. 100, <span class="citation" data-id="1544268"><a href="/opinion/1544268/cooper-v-oconnor/#140" aria-description="Citation for case: Cooper v. O&#x27;CONNOR">99 F. 2d 135, 140-141</a></span> (1938); <em>Anderson </em>v. <em>Rohrer, </em><span class="citation" data-id="1876540"><a href="/opinion/1876540/anderson-v-rohrer/" aria-description="Citation for case: Anderson v. Rohrer">3 F. Supp. 367</a></span> (SD Fla. 1933); <em>Pearson </em>v. <em>Reed, </em><span class="citation" data-id="1422703"><a href="/opinion/1422703/pearson-v-reed/" aria-description="Citation for case: Pearson v. Reed">6 Cal. App. 2d 277</a></span>, <span class="citation" data-id="1422703"><a href="/opinion/1422703/pearson-v-reed/" aria-description="Citation for case: Pearson v. Reed">44 P. 2d 592</a></span> (1935); <em>Anderson </em>v. <em>Manley, </em><span class="citation" data-id="4001444"><a href="/opinion/4225250/anderson-v-manley/" aria-description="Citation for case: Anderson v. Manley">181 Wash. 327</a></span>, <span class="citation" data-id="4001444"><a href="/opinion/4225250/anderson-v-manley/" aria-description="Citation for case: Anderson v. Manley">43 P. 2d 39</a></span> (1935). See generally Restatement of Torts § 656 and comment, b (1938); 1 F. Harper &amp; F. James, The Law of Torts § 4.3, pp. 305-306 (1956).</p>
</footnote>
<footnote label="22">
<p id="b479-6"> This is illustrated by the history of the disagreement as to the culpability of the prosecutor’s conduct in this case. We express no opinion as to which of the courts was correct. See nn. 8 and 9, <em>supra.</em></p>
</footnote>
<footnote label="23">
<p id="b480-6"> In the law of defamation, a concern for the airing of all evidence has resulted in an absolute privilege for any courtroom statement relevant to the subject matter of the proceeding. In the case of lawyers the privilege extends to their briefs and pleadings as well. See generally 1 T. Cooley, Law of Torts § 153 (4th ed. 1932); 1 F. Harper &amp; F. James, <em>supra, </em>§ 5.22. In the leading case of <em>Hoar </em>v. <em>Wood, </em><span class="citation" data-id="6407880"><a href="/opinion/6534162/hoar-v-wood/" aria-description="Citation for case: Hoar v. Wood">44 Mass. 193</a></span> (1841), Chief Justice Shaw expressed the policy decision as follows:</p>
<blockquote id="b480-7">“Subject to this restriction [of relevancy], it is, on the whole, for the public interest, and best calculated to subserve the purposes of justice, to allow counsel full freedom of speech, in conducting the causes and advocating and sustaining the rights, of their constituents; and this freedom of discussion ought not to be impaired by numerous and refined distinctions.” <span class="citation" data-id="6407880"><a href="/opinion/6534162/hoar-v-wood/#197" aria-description="Citation for case: Hoar v. Wood"><em>Id., </em>at 197-198</a></span>.</blockquote>
</footnote>
<footnote label="24">
<p id="b480-8"> A prosecutor often must decide, especially in cases of wide public interest, whether to proceed to trial where there is a sharp conflict in the evidence. The appropriate course of action in such a case may well be to permit a jury to resolve the conflict. Yet, a prosecutor understandably would be reluctant to go forward with a close case where an acquittal likely would trigger a suit against him for damages. Cf. American Bar Association Project on Stand<page-number citation-index="1" label="427">*427</page-number>ards for Criminal Justice, Prosecution and Defense Function §3.9 (c) (Approved Draft 1971).</p>
</footnote>
<footnote label="25">
<p id="b481-7"> The possibility of personal liability also could dampen the prosecutor’s exercise of his duty to bring to the attention of the court or of proper officials all significant evidence suggestive of innocence or mitigation. At trial this duty is enforced by the requirements of due process, but after a conviction the prosecutor also is bound by the ethics of his office to inform the appropriate authority of after-acquired or other information that casts doubt upon the correctness of the conviction. Cf. ABA Code of Professional Responsibility §EC 7-13 (1969); ABA, Standards, <em>supra, </em>§3.11. Indeed, the record in this case suggests that respondent’s recognition of this duty led to the post-conviction hearing which in turn resulted ultimately in the District Court’s granting of the writ of habeas corpus.</p>
</footnote>
<footnote label="26">
<p id="b482-8"> In addressing the consequences of subjecting judges to suits for damages under § 1983, the Court has commented:</p>
<blockquote id="b482-9">“Imposing such a burden on judges would contribute not to principled and fearless decision-making but to intimidation.” <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#554" aria-description="Citation for case: Pierson v. Ray">386 U. S., at 554</a></span>.</blockquote>
</footnote>
<footnote label="27">
<p id="b482-10"> Petitioner contends that his suit should be allowed, even if others would not be, because the District Court’s issuance of the writ of habeas corpus shows that his suit has substance. We decline to carve out such an exception to prosecutorial immunity. Petitioner’s success on habeas, where the question was the alleged misconduct by several state agents, does not necessarily establish the merit of his civil rights action where only the respondent’s alleged wrongdoing is at issue. Certainly nothing determined on habeas would bind respondent, who was not a • party. Moreover, using the habeas proceeding as a “door-opener” for a subsequent civil rights action would create the risk of injecting extraneous concerns into that proceeding. As we noted in the text, consideration of the habeas petition could well be colored by an awareness of potential prosecutorial liability.</p>
</footnote>
<footnote label="28">
<p id="b483-5"> “Whoever, under color of any law, statute, ordinance, regulation, or custom, willfully subjects any inhabitant of any State, Territory, or District to the deprivation of any rights, privileges, or immunities secured or protected by the Constitution or laws of the United States, or to different punishments, pains, or penalties, on account of such inhabitant being an alien, or by reason of his color, or race, than are prescribed for the punishment of citizens, shall be fined not more than $1,000 or imprisoned not more than one year, or both; and if death results shall be subject to imprisonment for any term of years or for life.”</p>
</footnote>
<footnote label="29">
<p id="b483-6"> California also appears to provide for criminal punishment of a prosecutor who commits some of the acts ascribed to respondent by petitioner. <span class="citation no-link">Cal. Penal Code § 127</span> (1970); cf. <em>In re Branch, </em><span class="citation" data-id="1345315"><a href="/opinion/1345315/in-re-branch/#210" aria-description="Citation for case: In Re Branch">70 Cal. 2d 200, 210-211</a></span>, <span class="citation" data-id="1345315"><a href="/opinion/1345315/in-re-branch/#181" aria-description="Citation for case: In Re Branch">449 P. 2d 174, 181</a></span> (1969).</p>
</footnote>
<footnote label="30">
<p id="b483-7"> See ABA Code of Professional Responsibility § EC 7-13. See generally ABA, Standards, <em>supra, </em>n. 24, §§ 1.1 (c), (e), and Commentary, pp. 44-45.</p>
</footnote>
<footnote label="31">
<p id="b484-6"> <em>Guerro </em>v. <em>Mulhearn, </em><span class="citation" data-id="320118"><a href="/opinion/320118/thomas-a-guerro-v-roger-f-mulhearn-ralph-f-andrews-v-kathy-decote/#1256" aria-description="Citation for case: Thomas A. Guerro v. Roger F. Mulhearn, Ralph F. Andrews...">498 F. 2d, at 1256</a></span>; <em>Hampton </em>v. <em>City of Chicago, </em><span class="citation" data-id="8890918"><a href="/opinion/8903845/hampton-v-city-of-chicago/#608" aria-description="Citation for case: Hampton v. City of Chicago">484 F. 2d, at 608-609</a></span>; <em>Robichaud </em>v. <em>Ronan, </em><span class="citation" data-id="8873827"><a href="/opinion/8887719/robichaud-v-ronan/#537" aria-description="Citation for case: Robichaud v. Ronan">351 F. 2d 533, 537</a></span> (CA9 1965); cf. <em>Madison </em>v. <em>Purdy, </em><span class="citation" data-id="284582"><a href="/opinion/284582/john-madison-and-kim-madison-v-e-wilson-purdy-and-richard-e-gerstein/" aria-description="Citation for case: John Madison and Kim Madison v. E. Wilson Purdy and...">410 F. 2d 99</a></span> (CA5 1969); <em>Lewis </em>v. <em>Brautigam, </em><span class="citation" data-id="237817"><a href="/opinion/237817/james-n-lewis-v-george-brautigam-i-ray-mills-dayton-blackford-and/" aria-description="Citation for case: James N. Lewis v. George Brautigam, I. Ray Mills, Dayton...">227 F. 2d 124</a></span> (CA5 1955). But cf. <em>Cambist Films, Inc. </em>v. <em>Duggan, </em><span class="citation" data-id="9459299"><a href="/opinion/309629/cambist-films-inc-a-corporation-v-robert-w-duggan/#889" aria-description="Citation for case: Cambist Films, Inc., a Corporation v. Robert W. Duggan">475 F. 2d 887, 889</a></span> (CA3 1973).</p>
</footnote>
<footnote label="32">
<p id="Akd"> Both in his complaint in District Court and in his argument to us, petitioner characterizes some of respondent’s actions as “police-related” or investigative. Specifically, he points to a request by respondent of the police during a courtroom recess that they hold off questioning Costello about a pending bad-check charge until after Costello had completed his testimony. Petitioner asserts that this request was an investigative activity because it was a direction to police officers engaged in the investigation of crime. Seen in its proper light, however, respondent’s request of the officers was an effort to control the presentation of his witness’ testimony, a task fairly within his function as an advocate.</p>
</footnote>
<footnote label="33">
<p id="b485-6"> We recognize that the duties of the prosecutor in his role as advocate for the State involve actions preliminary to the initiation of a prosecution and actions apart from the courtroom. A prosecuting attorney is required constantly, in the course of his duty as such, to make decisions on a wide variety of sensitive issues. These include questions of whether to present a ease to a grand jury, whether to file an information, whether and when to prosecute, whether to dismiss an indictment against particular defendants, which witnesses to call, and what other evidence to present. Preparation, both for the initiation of the criminal process and for a trial, may require the obtaining, reviewing, and evaluating of evidence. At some point, and with respect to some decisions, the prosecutor no doubt functions as an administrator rather than as an officer of the court. Drawing a proper line between these functions may present difficult questions, but this case does not require us to anticipate them.</p>
</footnote>
<footnote label="34">
<p id="b485-7"> Mr. Justice White, concurring in the judgment, would distinguish between willful use by a prosecutor of perjured testimony and willful suppression by a prosecutor of exculpatory information. In the former case, Mr. Justice White agrees that absolute immunity is appropriate. He thinks, however, that only a qualified immunity is appropriate where information relevant to the defense is “unconstitutionally <em>withheld </em>. . . from the court.” <em>Post, </em>at 443.</p>
<p id="b485-8">We do not accept the distinction urged by Mr. Justice White {or several reasons. As a matter of principle, we perceive no less ,n infringement of a defendant’s rights by the knowing use of per-ured testimony than by the deliberate withholding of exculpatory [information. The conduct in either case is reprehensible, warranting criminal prosecution as well as disbarment. See <em>supra, </em>at 429 nn. 29 and 30. Moreover, the distinction is not susceptible of practical application. A claim of using perjured-testimony simply may be re-framed and asserted as a claim of suppression of the evidence upon which the knowledge of perjury rested. That the two types of claims can thus be viewed is clear from our cases discussing the constitutional prohibitions against both practices. <em>Mooney </em>v. <em>Holohan, </em><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#110" aria-description="Citation for case: Mooney v. Holohan">294 <page-number citation-index="1" label="432">*432</page-number>U. S. 103, 110</a></span> (1935); <em>Alcorta </em>v. <em>Texas, </em><span class="citation" data-id="105566"><a href="/opinion/105566/alcorta-v-texas/#31" aria-description="Citation for case: Alcorta v. Texas">355 U. S. 28, 31-32</a></span> (1957); <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#86" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83, 86</a></span> (1963); <em>Miller </em>v. <em>Pate, </em><span class="citation" data-id="107354"><a href="/opinion/107354/miller-v-pate/" aria-description="Citation for case: Miller v. Pate">386 U. S. 1</a></span>, 4—6 (1967); <em>Giglio </em>v. <em>United States, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#151" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 151-155</a></span> (1972). It is also illustrated by the history of this case: at least one of the charges of prosecutorial • misconduct discussed by the Federal District Court in terms of suppression of evidence had been discussed by the Supreme Court of California in terms of use of perjured testimony. Compare <em>Imbler </em>v. <em>Craven, </em><span class="citation" data-id="1868466"><a href="/opinion/1868466/imbler-v-craven/#809" aria-description="Citation for case: Imbler v. Craven">298 F. Supp., at 809-811</a></span>, with <em>In re Imbler, </em><span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#566" aria-description="Citation for case: In Re Imbler">60 Cal. 2d, at 566-567</a></span>, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#12" aria-description="Citation for case: In Re Imbler">387 P. 2d, at 12-13</a></span>. Denying absolute immunity from suppression claims could thus eviscerate, in many situations, the absolute immunity from claims of using perjured testimony.</p>
<p id="b486-8">We further think Mr. Justice White’s suggestion, post, at 440 n. 5, that absolute immunity should be accorded only when the prosecutor makes a “full disclosure” of all facts casting doubt upon the State’s testimony, would place upon the prosecutor a duty exceeding the disclosure requirements of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>and its progeny, see <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>; <em>Moore </em>v. <em>Illinois, </em><span class="citation" data-id="9425027"><a href="/opinion/108613/moore-v-illinois/#795" aria-description="Citation for case: Moore v. Illinois">408 U. S. 786, 795</a></span> (1972); cf. <em>Donnelly </em>v. <em>DeChristoforo, </em><span class="citation" data-id="9425708"><a href="/opinion/109024/donnelly-v-dechristoforo/#647" aria-description="Citation for case: Donnelly v. DeChristoforo">416 U. S. 637, 647-648</a></span> (1974). It also would weaken the adversary system at the same time it interfered seriously with the legitimate exercise of prosecutorial discretion.</p>
</footnote>
</opinion>
```

---
