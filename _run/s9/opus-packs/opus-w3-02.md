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

## GROUP: _overhaul2/lake/cases/City of Los Angeles v. Patel.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "City of Los Angeles v. Patel"
type: case
citation: ""
parallel_cite: "576 U.S. 409; 135 S. Ct. 2443; 192 L. Ed. 2d 435; 83 U.S.L.W. 4520; 25 Fla. L. Weekly Fed. S 412"
neutral_cite: 2015 U.S. LEXIS 4065
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2015
date_decided: 2015-06-22
docket: 13-1175
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2015-06-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: City of Los Angeles v. Patel
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2811846/city-of-l-a-v-patel/"
  cluster_id: 2811846
  opinion_id: 2811846
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Camara v. Municipal Court]]", "[[City of Indianapolis v. Edmond]]"]
aliases: ["Los Angeles v. Patel"]
tags: ["case", "fourth-amendment", "administrative-search", "special-needs", "precompliance-review", "facial-challenge"]
holding: "A hotel guest-registry inspection ordinance is facially unconstitutional because it gives operators no opportunity for pre-compliance…"
lake:
  record_id: City of Los Angeles v. Patel
  status: verified
  projected_at: 2026-07-06
---

# City of Los Angeles v. Patel

*576 U.S. 409 (2015)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Los Angeles ordinance required hotel operators to keep specified guest-registry information and to make it available to police on demand, making refusal a misdemeanor punishable by arrest. A group of motel operators brought a facial Fourth Amendment challenge to the on-demand inspection provision.

## Issue
Whether an ordinance compelling hotel operators to turn over their guest registries to police on demand, with no opportunity for pre-compliance review and arrest for refusal, is facially unconstitutional.

## Rule
Yes. An administrative search regime must afford the subject a chance to contest the demand before a neutral official: "absent consent, exigent circumstances, or the like, in order for an administrative search to be constitutional, the subject of the search must be afforded an opportunity to obtain precompliance review before a neutral decisionmaker." — *Los Angeles v. Patel*, 576 U.S. 409 (2015) (slip op., at 10). ^pin-op10

"[W]e hold only that a hotel owner must be afforded an opportunity to have a neutral decisionmaker review an officer's demand to search the registry before he or she faces penalties for failing to comply." — *Id.* (slip op., at 11). ^pin-op11

## Application
The ordinance let an officer demand a hotel's registry on the spot and arrest the operator for any refusal, with no mechanism — administrative subpoena or otherwise — to obtain review before penalties attached. Because it provided no opportunity whatsoever for pre-compliance review, the inspection provision was facially invalid on these terms.

## Conclusion
The registry-inspection provision was facially unconstitutional; the judgment striking it down was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Patel* applies the administrative-search precompliance-review principle of [[Camara v. Municipal Court]] and complements the special-needs purpose analysis of [[City of Indianapolis v. Edmond]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *City of Los Angeles v. Patel*, 576 U.S. 409 (2015) — https://www.courtlistener.com/opinion/2810524/los-angeles-v-patel/ — pinpoints: slip op., at 10, 11 (CL carries the slip opinion under the cluster name "Los Angeles v. Patel").

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5cfb803d18351bb0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "City of Los Angeles v. Patel"}, "payload": {"all": [{"cite": "576 U.S. 409", "page": "409", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "576"}, {"cite": "135 S. Ct. 2443", "page": "2443", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "135"}, {"cite": "192 L. Ed. 2d 435", "page": "435", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "192"}, {"cite": "2015 U.S. LEXIS 4065", "page": "4065", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2015"}, {"cite": "83 U.S.L.W. 4520", "page": "4520", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "83"}, {"cite": "25 Fla. L. Weekly Fed. S 412", "page": "412", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "25"}], "display": null, "official": null, "official_selection_present": false, "record_id": "City of Los Angeles v. Patel"}}
{"assertion_id": "370cd1bdd1669479", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op11", "record_id": "City of Los Angeles v. Patel"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op11", "pinpoint_status": "slip-only", "quote": "[W]e hold only that a hotel owner must be afforded an opportunity to have a neutral decisionmaker review an officer's demand to search the registry before he or she faces penalties for failing to comply.", "quote_fidelity": "mismatch", "record_id": "City of Los Angeles v. Patel", "star_marker": null}}
{"assertion_id": "d08149d570b741fc", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op10", "record_id": "City of Los Angeles v. Patel"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op10", "pinpoint_status": "slip-only", "quote": "--- # City of Los Angeles v. Patel *576 U.S. 409 (2015)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Los Angeles ordinance required hotel operators to keep specified guest-registry information and to make it available to police on demand, making refusal a misdemeanor punishable by arrest. A group of motel operators brought a facial Fourth Amendment challenge to the on-demand inspection provision. ## Issue Whether an ordinance compelling hotel operators to turn over their guest registries to police on demand, with no opportunity for pre-compliance review and arrest for refusal, is facially unconstitutional. ## Rule Yes. An administrative search regime must afford the subject a chance to contest the demand before a neutral official:", "quote_fidelity": "mismatch", "record_id": "City of Los Angeles v. Patel", "star_marker": null}}
{"assertion_id": "5ec3c8ec8107144d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "City of Los Angeles v. Patel"}, "payload": {"as_of_content": "2015-06-22", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "City of Los Angeles v. Patel", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — City of Los Angeles v. Patel

```json
{
  "schema_version": "s2.v1",
  "record_id": "City of Los Angeles v. Patel",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "City of L. A. v. Patel",
    "case_name_short": "Patel",
    "case_name_full": "CITY OF LOS ANGELES, CALIFORNIA, for Petitioner v. Naranjibhai PATEL, Et Al.",
    "input_case_name": "City of Los Angeles v. Patel",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2015-06-22",
    "year": 2015,
    "docket": "13-1175",
    "cluster_id": 2811846,
    "lead_opinion_id": 2811846,
    "sibling_ids": [
      2811846
    ],
    "absolute_url": "/opinion/2811846/city-of-l-a-v-patel/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 2810524,
        "score": 120,
        "case_name": "Los Angeles v. Patel"
      },
      {
        "cluster_id": 8172542,
        "score": 20,
        "case_name": "City of L. A. v. Patel"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "576 U.S. 409",
        "volume": "576",
        "reporter": "U.S.",
        "page": "409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 S. Ct. 2443",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "2443",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "192 L. Ed. 2d 435",
        "volume": "192",
        "reporter": "L. Ed. 2d",
        "page": "435",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4520",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4520",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 412",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "412",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2015 U.S. LEXIS 4065",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "4065",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "576 U.S. 409",
        "volume": "576",
        "reporter": "U.S.",
        "page": "409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 S. Ct. 2443",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "2443",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "192 L. Ed. 2d 435",
        "volume": "192",
        "reporter": "L. Ed. 2d",
        "page": "435",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 U.S. LEXIS 4065",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "4065",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4520",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4520",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 412",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "412",
        "type": 1,
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
      "id": "pin-op10",
      "page": null,
      "quote": "--- # City of Los Angeles v. Patel *576 U.S. 409 (2015)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Los Angeles ordinance required hotel operators to keep specified guest-registry information and to make it available to police on demand, making refusal a misdemeanor punishable by arrest. A group of motel operators brought a facial Fourth Amendment challenge to the on-demand inspection provision. ## Issue Whether an ordinance compelling hotel operators to turn over their guest registries to police on demand, with no opportunity for pre-compliance review and arrest for refusal, is facially unconstitutional. ## Rule Yes. An administrative search regime must afford the subject a chance to contest the demand before a neutral official:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op11",
      "page": null,
      "quote": "[W]e hold only that a hotel owner must be afforded an opportunity to have a neutral decisionmaker review an officer's demand to search the registry before he or she faces penalties for failing to comply.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2015-06-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "City of Los Angeles v. Patel",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "City of Los Angeles v. Patel:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cosino v. State",
          "cluster_id": 5447462,
          "cite": [
            "503 S.W.3d 592",
            "2016 Tex. App. LEXIS 11431",
            "2016 WL 6134461"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane1_negative"
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
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Perry, Ex Parte James Richard \"Rick\"",
          "cluster_id": 3180638,
          "cite": [
            "483 S.W.3d 884",
            "2016 Tex. Crim. App. LEXIS 43",
            "2016 WL 738237"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salinas, Orlando",
          "cluster_id": 4374733,
          "cite": [
            "523 S.W.3d 103",
            "2017 WL 915525",
            "2017 Tex. Crim. App. LEXIS 284"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Eubanks",
          "cluster_id": 4684248,
          "cite": [
            "2019 IL 123525"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Burns",
          "cluster_id": 3171866,
          "cite": [
            "2015 IL 117387"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of El Cenizo, Texas v. State of Texas",
          "cluster_id": 4496244,
          "cite": [
            "890 F.3d 164"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Plains All American Pipeline L v. Thomas Cook",
          "cluster_id": 4417283,
          "cite": [
            "866 F.3d 534",
            "2017 WL 3403129",
            "2017 U.S. App. LEXIS 14661"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joseph Zadeh v. Mari Robinson",
          "cluster_id": 4636058,
          "cite": [
            "928 F.3d 457"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Free Speech Coalition, Inc. v. Attorney General United States",
          "cluster_id": 3210858,
          "cite": [
            "825 F.3d 149",
            "44 Media L. Rep. (BNA) 2157",
            "2016 U.S. App. LEXIS 10356",
            "2016 WL 3191474"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Porter v. City of Philadelphia",
          "cluster_id": 4786569,
          "cite": [
            "975 F.3d 374"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Toledo v. State",
          "cluster_id": 5448352,
          "cite": [
            "519 S.W.3d 273",
            "2017 WL 1281437",
            "2017 Tex. App. LEXIS 3023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Durham",
          "cluster_id": 4531050,
          "cite": [
            "902 F.3d 1180"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Shaquille Robinson",
          "cluster_id": 4340460,
          "cite": [
            "846 F.3d 694",
            "2017 WL 280727",
            "2017 U.S. App. LEXIS 1134"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William Gardner v. Jason Evans",
          "cluster_id": 4607076,
          "cite": [
            "920 F.3d 1038"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Winston v. City of Syracuse",
          "cluster_id": 8439878,
          "cite": [
            "887 F.3d 553"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Liberty Coins v. David Goodman",
          "cluster_id": 4460823,
          "cite": [
            "880 F.3d 274"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Curtis Morrison v. Mark Peterson",
          "cluster_id": 3162649,
          "cite": [
            "809 F.3d 1059",
            "2015 U.S. App. LEXIS 21669",
            "2015 WL 8756229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nadine Pellegrino v. TSA",
          "cluster_id": 4657793,
          "cite": [
            "937 F.3d 164"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas Association of Business National Federation of Independent Business, American Staffing Association LeadingEdge Personnel, Ltd. Staff Force, Inc. HT Staffing Ltd. D/B/A the HT Group The Burnett Companies Consolidated, Inc., D/B/A Burnett Specialists Society for Human Resource Management Texas State Council of the Society for Human Resource Management Austin Human Resource Management Association Strickland School, LLC And the State of Texas v. City of Austin, Texas, and Spencer Cronk, City Manager of the City of Austin",
          "cluster_id": 4565114,
          "cite": [
            "565 S.W.3d 425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Allmond v. Department of Health & Mental Hygiene",
          "cluster_id": 4237242,
          "cite": [
            "141 A.3d 57",
            "448 Md. 592",
            "2016 Md. LEXIS 436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mohamed Mohamud",
          "cluster_id": 4327222,
          "cite": [
            "843 F.3d 420",
            "2016 U.S. App. LEXIS 21622",
            "2016 WL 7046751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Expressions Hair Design v. Schneiderman",
          "cluster_id": 8442471,
          "cite": [
            "808 F.3d 118",
            "2015 U.S. App. LEXIS 21521",
            "2015 WL 8537667"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2811846) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 127,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 127,
        "triage_read": 2,
        "triage_snippet_classified": 125
      },
      "lane2_top_cited": {
        "query": "cites:(2811846)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05JnM9NDU0MjIyMSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%282811846%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2811846)",
        "reviewed": 8,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 8,
        "triage_read": 0,
        "triage_snippet_classified": 8
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2811846)",
    "indexed_citing_opinions": 140,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2811846,
        "count": 140,
        "count_source": "search"
      }
    ],
    "citation_count": 241,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/city-of-los-angeles-v-patel.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc3NDAwOTgmcz02NDY3MDQ5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%282811846%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2811846,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 109005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 111061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 111835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 111891,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 112765,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 112786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 118100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 118299,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 118405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 118414,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 145777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 145824,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 145887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 202028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 357364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 385866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 449079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 677802,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 1254195,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 1489882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 2142195,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 2620876,
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
    "date_created": "2026-07-05T00:21:22Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:22:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:22:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:26:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:22:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — City of Los Angeles v. Patel

```
(Slip Opinion)              OCTOBER TERM, 2014                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

CITY OF LOS ANGELES, CALIFORNIA v. PATEL ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE NINTH CIRCUIT

      No. 13–1175. Argued March 3, 2015—Decided June 22, 2015
Petitioner, the city of Los Angeles (City), requires hotel operators to
  record and keep specific information about their guests on the prem-
  ises for a 90-day period. Los Angeles Municipal Code §41.49. These
  records “shall be made available to any officer of the Los Angeles Po-
  lice Department for inspection . . . at a time and in a manner that
  minimizes any interference with the operation of the business,”
  §41.49(3)(a), and a hotel operator’s failure to make the records avail-
  able is a criminal misdemeanor, §11.00(m). Respondents, a group of
  motel operators and a lodging association, brought a facial challenge
  to §41.49(3)(a) on Fourth Amendment grounds. The District Court
  entered judgment for the City, finding that respondents lacked a rea-
  sonable expectation of privacy in their records. The Ninth Circuit
  subsequently reversed, determining that inspections under
  §41.49(3)(a) are Fourth Amendment searches and that such searches
  are unreasonable under the Fourth Amendment because hotel own-
  ers are subjected to punishment for failure to turn over their records
  without first being afforded the opportunity for precompliance re-
  view.
Held:
    1. Facial challenges under the Fourth Amendment are not categor-
 ically barred or especially disfavored. Pp. 4–8.
       (a) Facial challenges to statutes—as opposed to challenges to
 particular applications of statutes—have been permitted to proceed
 under a diverse array of constitutional provisions. See, e.g., Sorrell v.
 IMS Health Inc., 564 U. S. ___ (First Amendment); District of Colum-
 bia v. Heller, 554 U. S. 570 (Second Amendment). The Fourth
 Amendment is no exception. Sibron v. New York, 392 U. S. 40, dis-
 tinguished. This Court has entertained facial challenges to statutes
2                        LOS ANGELES v. PATEL

                                   Syllabus

    authorizing warrantless searches, declaring them, on several occa-
    sions, facially invalid, see, e.g., Chandler v. Miller, 520 U. S. 305,
    308–309. Pp. 4–7.
          (b) Petitioner contends that facial challenges to statutes author-
    izing warrantless searches must fail because they will never be un-
    constitutional in all applications, but this Court’s precedents demon-
    strate that such challenges can be brought, and can succeed. Under
    the proper facial-challenge analysis, only applications of a statute in
    which the statute actually authorizes or prohibits conduct are consid-
    ered. See, e.g., Planned Parenthood of Southeastern Pa. v. Casey, 505
    U. S. 833. When addressing a facial challenge to a statute authoriz-
    ing warrantless searches, the proper focus is on searches that the law
    actually authorizes and not those that could proceed irrespective of
    whether they are authorized by the statute, e.g., where exigent cir-
    cumstances, a warrant, or consent to search exists. Pp. 7–8.
       2. Section 41.49(3)(a) is facially unconstitutional because it fails to
    provide hotel operators with an opportunity for precompliance re-
    view. Pp. 9–17.
          (a) “ ‘[S]earches conducted outside the judicial process . . . are
    per se unreasonable under the Fourth Amendment—subject only to a
    few . . . exceptions.’ ” Arizona v. Gant, 556 U. S. 332, 338. One ex-
    ception is for administrative searches. See Camara v. Municipal
    Court of City and County of San Francisco, 387 U. S. 523, 534. To be
    constitutional, the subject of an administrative search must, among
    other things, be afforded an opportunity to obtain precompliance re-
    view before a neutral decisionmaker. See See v. Seattle, 387 U. S.
    541, 545. Assuming the administrative search exception otherwise
    applies here, §41.49 is facially invalid because it fails to afford hotel
    operators any opportunity for precompliance review. To be clear, a
    hotel owner must only be afforded an opportunity for precompliance
    review; actual review need occur only when a hotel operator objects to
    turning over the records. This opportunity can be provided without
    imposing onerous burdens on law enforcement. For instance, officers
    in the field can issue administrative subpoenas without probable
    cause that a regulation is being infringed. This narrow holding does
    not call into question those parts of §41.49 requiring hotel operators
    to keep records nor does it prevent police from obtaining access to
    those records where a hotel operator consents to the search, where
    the officer has a proper administrative warrant, or where some other
    exception to the warrant requirement applies. Pp. 9–13.
          (b) Petitioner’s argument that the ordinance is facially valid un-
    der the more relaxed standard for closely regulated industries is re-
    jected. See Marshall v. Barlow’s, Inc., 436 U. S. 307, 313. This Court
    has only recognized four such industries, and nothing inherent in the
                     Cite as: 576 U. S. ____ (2015)                     3

                                Syllabus

  operation of hotels poses a comparable clear and significant risk to
  the public welfare. Additionally, because the majority of regulations
  applicable to hotels apply to many businesses, to classify hotels as
  closely regulated would permit what has always been a narrow ex-
  ception to swallow the rule. But even if hotels were closely regulated,
  §41.49 would still contravene the Fourth Amendment as it fails to
  satisfy the additional criteria that must be met for searches of closely
  regulated industries to be reasonable. See New York v. Burger, 482
  U. S. 691, 702–703. Pp. 13–17.
738 F. 3d 1058, affirmed.

  SOTOMAYOR, J., delivered the opinion of the Court, in which KENNE-
DY, GINSBURG, BREYER, and KAGAN, JJ., joined. SCALIA, J., filed a dis-
senting opinion, in which ROBERTS, C. J., and THOMAS, J., joined.
ALITO, J., filed a dissenting opinion, in which THOMAS, J., joined.
                        Cite as: 576 U. S. ____ (2015)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 13–1175
                                   _________________


 CITY OF LOS ANGELES, CALIFORNIA, PETITIONER
          v. NARANJIBHAI PATEL, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE NINTH CIRCUIT

                                 [June 22, 2015] 


  JUSTICE SOTOMAYOR delivered the opinion of the Court.
  Respondents brought a Fourth Amendment challenge to
a provision of the Los Angeles Municipal Code that com-
pels “[e]very operator of a hotel to keep a record” contain-
ing specified information concerning guests and to make
this record “available to any officer of the Los Angeles
Police Department for inspection” on demand. Los Ange-
les Municipal Code §§41.49(2), (3)(a), (4) (2015). The
questions presented are whether facial challenges to stat-
utes can be brought under the Fourth Amendment and, if
so, whether this provision of the Los Angeles Municipal
Code is facially invalid. We hold facial challenges can be
brought under the Fourth Amendment. We further hold
that the provision of the Los Angeles Municipal Code that
requires hotel operators to make their registries available
to the police on demand is facially unconstitutional be-
cause it penalizes them for declining to turn over their
records without affording them any opportunity for pre-
compliance review.
2                  LOS ANGELES v. PATEL

                     Opinion of the Court

                              I

                              A

   Los Angeles Municipal Code (LAMC) §41.49 requires
hotel operators to record information about their guests,
including: the guest’s name and address; the number of
people in each guest’s party; the make, model, and license
plate number of any guest’s vehicle parked on hotel prop-
erty; the guest’s date and time of arrival and scheduled
departure date; the room number assigned to the guest;
the rate charged and amount collected for the room; and
the method of payment. §41.49(2). Guests without reser-
vations, those who pay for their rooms with cash, and any
guests who rent a room for less than 12 hours must pre-
sent photographic identification at the time of check-in,
and hotel operators are required to record the number and
expiration date of that document. §41.49(4). For those
guests who check in using an electronic kiosk, the hotel’s
records must also contain the guest’s credit card infor-
mation. §41.49(2)(b). This information can be maintained
in either electronic or paper form, but it must be “kept on
the hotel premises in the guest reception or guest check-in
area or in an office adjacent” thereto for a period of 90
days. §41.49(3)(a).
   Section 41.49(3)(a)—the only provision at issue here—
states, in pertinent part, that hotel guest records “shall be
made available to any officer of the Los Angeles Police
Department for inspection,” provided that “[w]henever
possible, the inspection shall be conducted at a time and in
a manner that minimizes any interference with the opera-
tion of the business.” A hotel operator’s failure to make
his or her guest records available for police inspection is a
misdemeanor punishable by up to six months in jail and a
$1,000 fine. §11.00(m) (general provision applicable to
entire LAMC).
                 Cite as: 576 U. S. ____ (2015)            3

                     Opinion of the Court 


                              B

   In 2003, respondents, a group of motel operators along
with a lodging association, sued the city of Los Angeles
(City or petitioner) in three consolidated cases challenging
the constitutionality of §41.49(3)(a). They sought declara-
tory and injunctive relief. The parties “agree[d] that the
sole issue in the . . . action [would be] a facial constitu-
tional challenge” to §41.49(3)(a) under the Fourth Amend-
ment. App. 195. They further stipulated that respondents
have been subjected to mandatory record inspections
under the ordinance without consent or a warrant. Id., at
194–195.
   Following a bench trial, the District Court entered
judgment in favor of the City, holding that respondents’
facial challenge failed because they lacked a reasonable
expectation of privacy in the records subject to inspection.
A divided panel of the Ninth Circuit affirmed on the same
grounds. 686 F. 3d 1085 (2012). On rehearing en banc,
however, the Court of Appeals reversed. 738 F. 3d 1058,
1065 (2013).
   The en banc court first determined that a police officer’s
nonconsensual inspection of hotel records under §41.49 is
a Fourth Amendment “search” because “[t]he business
records covered by §41.49 are the hotel’s private property”
and the hotel therefore “has the right to exclude others
from prying into the[ir] contents.” Id., at 1061. Next, the
court assessed “whether the searches authorized by §41.49
are reasonable.” Id., at 1063. Relying on Donovan v. Lone
Steer, Inc., 464 U. S. 408 (1984), and See v. Seattle, 387
U. S. 541 (1967), the court held that §41.49 is facially
unconstitutional “as it authorizes inspections” of hotel
records “without affording an opportunity to ‘obtain judi-
cial review of the reasonableness of the demand prior to
suffering penalties for refusing to comply.’ ” 738 F. 3d, at
1065 (quoting See, 387 U. S., at 545).
   Two dissenting opinions were filed. The first dissent
4                  LOS ANGELES v. PATEL

                     Opinion of the Court

argued that facial relief should rarely be available for
Fourth Amendment challenges, and was inappropriate
here because the ordinance would be constitutional in
those circumstances where police officers demand access
to hotel records with a warrant in hand or exigent circum-
stances justify the search. 738 F. 3d, at 1065–1070 (opin-
ion of Tallman, J.). The second dissent conceded that
inspections under §41.49 constitute Fourth Amendment
searches, but faulted the majority for assessing the rea-
sonableness of these searches without accounting for the
weakness of the hotel operators’ privacy interest in the
content of their guest registries. Id., at 1070–1074 (opin-
ion of Clifton, J.).
  We granted certiorari, 574 U. S. ___ (2014), and now
affirm.
                             II
  We first clarify that facial challenges under the Fourth
Amendment are not categorically barred or especially
disfavored.
                               A
   A facial challenge is an attack on a statute itself as
opposed to a particular application. While such challenges
are “the most difficult . . . to mount successfully,” United
States v. Salerno, 481 U. S. 739, 745 (1987), the Court
has never held that these claims cannot be brought
under any otherwise enforceable provision of the Constitu-
tion. Cf. Fallon, Fact and Fiction About Facial Chal-
lenges, 99 Cal. L. Rev. 915, 918 (2011) (pointing to several
Terms in which “the Court adjudicated more facial chal-
lenges on the merits than it did as-applied challenges”).
Instead, the Court has allowed such challenges to proceed
under a diverse array of constitutional provisions. See,
e.g., Sorrell v. IMS Health Inc., 564 U. S. ___ (2011) (First
Amendment); District of Columbia v. Heller, 554 U. S. 570
                  Cite as: 576 U. S. ____ (2015)             5

                      Opinion of the Court

(2008) (Second Amendment); Chicago v. Morales, 527 U. S.
41 (1999) (Due Process Clause of the Fourteenth Amend-
ment); Kraft Gen. Foods, Inc. v. Iowa Dept. of Revenue and
Finance, 505 U. S. 71 (1992) (Foreign Commerce Clause).
   Fourth Amendment challenges to statutes authorizing
warrantless searches are no exception. Any claim to the
contrary reflects a misunderstanding of our decision in
Sibron v. New York, 392 U. S. 40 (1968). In Sibron, two
criminal defendants challenged the constitutionality of a
statute authorizing police to, among other things, “ ‘stop
any person abroad in a public place whom [they] reason-
ably suspec[t] is committing, has committed or is about to
commit a felony.” Id., at 43 (quoting then N. Y. Code
Crim. Proc. §180–a). The Court held that the search of
one of the defendants under the statute violated the
Fourth Amendment, 392 U. S., at 59, 62, but refused to
opine more broadly on the statute’s validity, stating that
“[t]he constitutional validity of a warrantless search is
pre-eminently the sort of question which can only be de-
cided in the concrete factual context of the individual
case.” Id., at 59.
   This statement from Sibron—which on its face might
suggest an intent to foreclose all facial challenges to stat-
utes authorizing warrantless searches—must be under-
stood in the broader context of that case. In the same
section of the opinion, the Court emphasized that the
“operative categories” of the New York law at issue were
“susceptible of a wide variety of interpretations,” id., at 60,
and that “[the law] was passed too recently for the State’s
highest court to have ruled upon many of the questions
involving potential intersections with federal constitutional
guarantees,” id., at 60, n. 20. Sibron thus stands for the
simple proposition that claims for facial relief under the
Fourth Amendment are unlikely to succeed when there is
substantial ambiguity as to what conduct a statute au-
thorizes: Where a statute consists of “extraordinarily
6                  LOS ANGELES v. PATEL

                      Opinion of the Court

elastic categories,” it may be “impossible to tell” whether
and to what extent it deviates from the requirements of
the Fourth Amendment. Id., at 59, 61, n. 20.
   This reading of Sibron is confirmed by subsequent prec-
edents. Since Sibron, the Court has entertained facial
challenges under the Fourth Amendment to statutes
authorizing warrantless searches. See, e.g., Vernonia
School District 47J v. Acton, 515 U. S. 646, 648 (1995)
(“We granted certiorari to decide whether” petitioner’s
student athlete drug testing policy “violates the Fourth
and Fourteenth Amendments to the United States Consti-
tution”); Skinner v. Railway Labor Executives’ Assn., 489
U. S. 602, 633, n. 10 (1989) (“[R]espondents have chal-
lenged the administrative scheme on its face. We deal
therefore with whether the [drug] tests contemplated by
the regulation can ever be conducted”); cf. Illinois v. Krull,
480 U. S. 340, 354 (1987) (“[A] person subject to a statute
authorizing searches without a warrant or probable cause
may bring an action seeking a declaration that the statute
is unconstitutional and an injunction barring its imple-
mentation”). Perhaps more importantly, the Court has on
numerous occasions declared statutes facially invalid
under the Fourth Amendment. For instance, in Chandler
v. Miller, 520 U. S. 305, 308–309 (1997), the Court struck
down a Georgia statute requiring candidates for certain
state offices to take and pass a drug test, concluding that
this “requirement . . . [did] not fit within the closely
guarded category of constitutionally permissible suspicion-
less searches.” Similar examples abound. See, e.g., Fer-
guson v. Charleston, 532 U. S. 67, 86 (2001) (holding that
a hospital policy authorizing “nonconsensual, warrantless,
and suspicionless searches” contravened the Fourth
Amendment); Payton v. New York, 445 U. S. 573, 574, 576
(1980) (holding that a New York statute “authoriz[ing]
police officers to enter a private residence without a war-
rant and with force, if necessary, to make a routine felony
                 Cite as: 576 U. S. ____ (2015)           7

                     Opinion of the Court

arrest” was “not consistent with the Fourth Amendment”);
Torres v. Puerto Rico, 442 U. S. 465, 466, 471 (1979) (hold-
ing that a Puerto Rico statute authorizing “police to search
the luggage of any person arriving in Puerto Rico from the
United States” was unconstitutional because it failed to
require either probable cause or a warrant).

                              B
   Petitioner principally contends that facial challenges to
statutes authorizing warrantless searches must fail be-
cause such searches will never be unconstitutional in all
applications. Cf. Salerno, 481 U. S., at 745 (to obtain
facial relief the party seeking it “must establish that no
set of circumstances exists under which the [statute]
would be valid”). In particular, the City points to situa-
tions where police are responding to an emergency, where
the subject of the search consents to the intrusion, and
where police are acting under a court-ordered warrant.
See Brief for Petitioner 19–20. While petitioner frames
this argument as an objection to respondents’ challenge in
this case, its logic would preclude facial relief in every
Fourth Amendment challenge to a statute authorizing
warrantless searches. For this reason alone, the City’s
argument must fail: The Court’s precedents demonstrate
not only that facial challenges to statutes authorizing
warrantless searches can be brought, but also that they
can succeed. See Part II–A, supra.
   Moreover, the City’s argument misunderstands how
courts analyze facial challenges. Under the most exacting
standard the Court has prescribed for facial challenges, a
plaintiff must establish that a “law is unconstitutional in
all of its applications.” Washington State Grange v. Wash-
ington State Republican Party, 552 U. S. 442, 449 (2008).
But when assessing whether a statute meets this stand-
ard, the Court has considered only applications of the
8                      LOS ANGELES v. PATEL

                          Opinion of the Court

statute in which it actually authorizes or prohibits con-
duct. For instance, in Planned Parenthood of Southeast-
ern Pa. v. Casey, 505 U. S. 833 (1992), the Court struck
down a provision of Pennsylvania’s abortion law that
required a woman to notify her husband before obtaining
an abortion. Those defending the statute argued that
facial relief was inappropriate because most women volun-
tarily notify their husbands about a planned abortion and
for them the law would not impose an undue burden. The
Court rejected this argument, explaining: The
“[l]egislation is measured for consistency with the Consti-
tution by its impact on those whose conduct it affects. . . .
The proper focus of the constitutional inquiry is the group
for whom the law is a restriction, not the group for whom
the law is irrelevant.” Id., at 894.
   Similarly, when addressing a facial challenge to a stat-
ute authorizing warrantless searches, the proper focus of
the constitutional inquiry is searches that the law actually
authorizes, not those for which it is irrelevant. If exigency
or a warrant justifies an officer’s search, the subject of the
search must permit it to proceed irrespective of whether it
is authorized by statute. Statutes authorizing warrantless
searches also do no work where the subject of a search has
consented. Accordingly, the constitutional “applications”
that petitioner claims prevent facial relief here are irrele-
vant to our analysis because they do not involve actual
applications of the statute.1
——————
  1 Relatedly, the United States claims that a statute authorizing war-

rantless searches may still have independent force if it imposes a
penalty for failing to cooperate in a search conducted under a warrant
or in an exigency. See Brief for United States as Amicus Curiae 19.
This argument gets things backwards. An otherwise facially unconsti-
tutional statute cannot be saved from invalidation based solely on the
existence of a penalty provision that applies when searches are not
actually authorized by the statute. This argument is especially uncon-
vincing where, as here, an independent obstruction of justice statute
imposes a penalty for “willfully, resist[ing], delay[ing], or obstruct[ing]
                     Cite as: 576 U. S. ____ (2015)                      9

                          Opinion of the Court

                             III
  Turning to the merits of the particular claim before us,
we hold that §41.49(3)(a) is facially unconstitutional be-
cause it fails to provide hotel operators with an opportu-
nity for precompliance review.
                             A
  The Fourth Amendment protects “[t]he right of the
people to be secure in their persons, houses, papers, and
effects, against unreasonable searches and seizures.” It
further provides that “no Warrants shall issue, but upon
probable cause.” Based on this constitutional text, the
Court has repeatedly held that “ ‘searches conducted out-
side the judicial process, without prior approval by [a]
judge or [a] magistrate [judge], are per se unreasonable . . .
subject only to a few specifically established and well-
delineated exceptions.’ ” Arizona v. Gant, 556 U. S. 332,
338 (2009) (quoting Katz v. United States, 389 U. S. 347,
357 (1967)). This rule “applies to commercial premises as
well as to homes.” Marshall v. Barlow’s, Inc., 436 U. S.
307, 312 (1978).
  Search regimes where no warrant is ever required may
be reasonable where “ ‘special needs . . . make the warrant
and probable-cause requirement impracticable,’ ” Skinner,
489 U. S., at 619 (quoting Griffin v. Wisconsin, 483 U. S.
868, 873 (1987) (some internal quotation marks omitted)),
and where the “primary purpose” of the searches is
“[d]istinguishable from the general interest in crime con-
trol,” Indianapolis v. Edmond, 531 U. S. 32, 44 (2000).
Here, we assume that the searches authorized by §41.49
serve a “special need” other than conducting criminal
investigations: They ensure compliance with the record-

—————— 

any public officer . . . in the discharge or attempt to discharge any duty

of his or her office of employment.” Cal. Penal Code Ann. §148(a)(1)

(West 2014).

10                    LOS ANGELES v. PATEL

                         Opinion of the Court

keeping requirement, which in turn deters criminals from
operating on the hotels’ premises.2 The Court has referred
to this kind of search as an “administrative searc[h].”
Camara v. Municipal Court of City and County of San
Francisco, 387 U. S. 523, 534 (1967). Thus, we consider
whether §41.49 falls within the administrative search
exception to the warrant requirement.
   The Court has held that absent consent, exigent circum-
stances, or the like, in order for an administrative search
to be constitutional, the subject of the search must be
afforded an opportunity to obtain precompliance review
before a neutral decisionmaker. See See, 387 U. S., at 545;
Lone Steer, 464 U. S., at 415 (noting that an administra-
tive search may proceed with only a subpoena where the
subpoenaed party is sufficiently protected by the oppor-
tunity to “question the reasonableness of the subpoena,
before suffering any penalties for refusing to comply with
it, by raising objections in an action in district court”).
And, we see no reason why this minimal requirement is
inapplicable here. While the Court has never attempted to
prescribe the exact form an opportunity for precompliance
review must take, the City does not even attempt to argue
that §41.49(3)(a) affords hotel operators any opportunity
whatsoever. Section 41.49(3)(a) is, therefore, facially
invalid.
   A hotel owner who refuses to give an officer access to his
or her registry can be arrested on the spot. The Court has
held that business owners cannot reasonably be put to this
kind of choice. Camara, 387 U. S., at 533 (holding that
“broad statutory safeguards are no substitute for individ-
ualized review, particularly when those safeguards may
——————
  2 Respondents contend that §41.49’s principal purpose instead is to

facilitate criminal investigation. Brief for Respondents 44–47. Because
we find that the searches authorized by §41.49 are unconstitutional
even if they serve the City’s asserted purpose, we decline to address
this argument.
                 Cite as: 576 U. S. ____ (2015)          11

                     Opinion of the Court

only be invoked at the risk of a criminal penalty”). Absent
an opportunity for precompliance review, the ordinance
creates an intolerable risk that searches authorized by it
will exceed statutory limits, or be used as a pretext to
harass hotel operators and their guests. Even if a hotel
has been searched 10 times a day, every day, for three
months, without any violation being found, the operator
can only refuse to comply with an officer’s demand to turn
over the registry at his or her own peril.
  To be clear, we hold only that a hotel owner must be
afforded an opportunity to have a neutral decisionmaker
review an officer’s demand to search the registry before he
or she faces penalties for failing to comply. Actual review
need only occur in those rare instances where a hotel
operator objects to turning over the registry. Moreover,
this opportunity can be provided without imposing oner-
ous burdens on those charged with an administrative
scheme’s enforcement. For instance, respondents accept
that the searches authorized by §41.49(3)(a) would be
constitutional if they were performed pursuant to an
administrative subpoena. Tr. of Oral Arg. 36–37. These
subpoenas, which are typically a simple form, can be
issued by the individual seeking the record—here, officers
in the field—without probable cause that a regulation is
being infringed. See See, 387 U. S., at 544 (“[T]he demand
to inspect may be issued by the agency”). Issuing a sub-
poena will usually be the full extent of an officer’s burden
because “the great majority of businessmen can be ex-
pected in normal course to consent to inspection without
warrant.” Barlow’s, Inc., 436 U. S., at 316. Indeed, the
City has cited no evidence suggesting that without an
ordinance authorizing on-demand searches, hotel opera-
tors would regularly refuse to cooperate with the police.
  In those instances, however, where a subpoenaed hotel
operator believes that an attempted search is motivated
by illicit purposes, respondents suggest it would be suffi-
12                    LOS ANGELES v. PATEL

                         Opinion of the Court

cient if he or she could move to quash the subpoena before
any search takes place. Tr. of Oral Arg. 38–39. A neutral
decisionmaker, including an administrative law judge,
would then review the subpoenaed party’s objections
before deciding whether the subpoena is enforceable.
Given the limited grounds on which a motion to quash can
be granted, such challenges will likely be rare. And, in the
even rarer event that an officer reasonably suspects that a
hotel operator may tamper with the registry while the
motion to quash is pending, he or she can guard the regis-
try until the required hearing can occur, which ought not
take long. Riley v. California, 573 U. S. ___ (2014) (slip
op., at 12) (police may seize and hold a cell phone “to
prevent destruction of evidence while seeking a warrant”);
Illinois v. McArthur, 531 U. S. 326, 334 (2001) (citing
cases upholding the constitutionality of “temporary re-
straints where [they are] needed to preserve evidence until
police could obtain a warrant”). Cf. Missouri v. McNeely,
569 U. S. ___ (2013) (slip op., at 12) (noting that many
States have procedures in place for considering warrant
applications telephonically).3
   Procedures along these lines are ubiquitous. A 2002
report by the Department of Justice “identified
approximately 335 existing administrative subpoena
authorities held by various [federal] executive branch
entities.” Office of Legal Policy, Report to Congress
on the Use of Administrative Subpoena Authorities by
Executive Branch Agencies and Entities 3, online
at http://www.justice.gov/archive/olp/rpt_to_congress.htm
(All Internet materials as visited June 19, 2015, and
available in Clerk of Court’s case file). Their prevalence
——————
  3 JUSTICE SCALIA professes to be baffled at the idea that we could

suggest that in certain circumstances, police officers may seize some-
thing that they cannot immediately search. Post, at 10–11 (dissenting
opinion). But that is what this Court’s cases have explicitly endorsed,
including Riley just last Term.
                    Cite as: 576 U. S. ____ (2015)                13

                        Opinion of the Court

confirms what common sense alone would otherwise lead
us to conclude: In most contexts, business owners can be
afforded at least an opportunity to contest an administra-
tive search’s propriety without unduly compromising the
government’s ability to achieve its regulatory aims.
   Of course administrative subpoenas are only one way in
which an opportunity for precompliance review can be
made available. But whatever the precise form, the avail-
ability of precompliance review alters the dynamic be-
tween the officer and the hotel to be searched, and reduces
the risk that officers will use these administrative searches
as a pretext to harass business owners.
   Finally, we underscore the narrow nature of our hold-
ing. Respondents have not challenged and nothing in our
opinion calls into question those parts of §41.49 that re-
quire hotel operators to maintain guest registries contain-
ing certain information. And, even absent legislative
action to create a procedure along the lines discussed
above, see supra, at 11, police will not be prevented from
obtaining access to these documents. As they often do,
hotel operators remain free to consent to searches of their
registries and police can compel them to turn them over
if they have a proper administrative warrant—including
one that was issued ex parte—or if some other exception
to the warrant requirement applies, including exigent
circumstances.4
                          B
  Rather than arguing that §41.49(3)(a) is constitutional

——————
  4 In suggesting that our holding today will somehow impede law en-

forcement from achieving its important aims, JUSTICE SCALIA relies on
instances where hotels were used as “prisons for migrants smuggled
across the border and held for ransom” or as “rendezvous sites where
child sex workers meet their clients on threat of violence from their
procurers.” See post, at 2. It is hard to imagine circumstances more
exigent than these.
14                     LOS ANGELES v. PATEL

                          Opinion of the Court

under the general administrative search doctrine, the City
and JUSTICE SCALIA contend that hotels are “closely regu-
lated,” and that the ordinance is facially valid under the
more relaxed standard that applies to searches of this
category of businesses. Brief for Petitioner 28–47; post, at
5. They are wrong on both counts.
  Over the past 45 years, the Court has identified only
four industries that “have such a history of government
oversight that no reasonable expectation of privacy . . .
could exist for a proprietor over the stock of such an en-
terprise,” Barlow’s, Inc., 436 U. S., 313. Simply listing
these industries refutes petitioner’s argument that hotels
should be counted among them. Unlike liquor sales, Col-
onnade Catering Corp. v. United States, 397 U. S. 72
(1970), firearms dealing, United States v. Biswell, 406
U. S. 311, 311–312 (1972), mining, Donovan v. Dewey, 452
U. S. 594 (1981), or running an automobile junkyard, New
York v. Burger, 482 U. S. 691 (1987), nothing inherent in
the operation of hotels poses a clear and significant risk to
the public welfare. See, e.g., id., at 709 (“Automobile
junkyards and vehicle dismantlers provide the major
market for stolen vehicles and vehicle parts”); Dewey, 452
U. S., at 602 (describing the mining industry as “among
the most hazardous in the country”).5
  Moreover, “[t]he clear import of our cases is that the
closely regulated industry . . . is the exception.” Barlow’s,
Inc., 436 U. S., at 313. To classify hotels as pervasively
regulated would permit what has always been a narrow
exception to swallow the rule. The City wisely refrains
from arguing that §41.49 itself renders hotels closely
regulated. Nor do any of the other regulations on which
——————
  5 JUSTICE SCALIA’s effort to depict hotels as raising a comparable de-

gree of risk rings hollow. See post, at 1, 14. Hotels—like practically all
commercial premises or services—can be put to use for nefarious ends.
But unlike the industries that the Court has found to be closely regu-
lated, hotels are not intrinsically dangerous.
                 Cite as: 576 U. S. ____ (2015)          15

                     Opinion of the Court

petitioner and JUSTICE SCALIA rely—regulations requiring
hotels to, inter alia, maintain a license, collect taxes,
conspicuously post their rates, and meet certain sanitary
standards—establish a comprehensive scheme of regula-
tion that distinguishes hotels from numerous other busi-
nesses. See Brief for Petitioner 33–34 (citing regulations);
post, at 7 (same). All businesses in Los Angeles need a
license to operate. LAMC §§21.03(a), 21.09(a). While
some regulations apply to a smaller set of businesses, see
e.g. Cal. Code Regs., tit. 25, §40 (2015) (requiring linens
to be changed between rental guests), online at
http://www.oal.ca.gov/ccr.htm, these can hardly be said to
have created a “ ‘comprehensive’ ” scheme that puts hotel
owners on notice that their “ ‘property will be subject to
periodic inspections undertaken for specific purposes,’ ”
Burger, 482 U. S., at 705, n. 16 (quoting Dewey, 452 U. S.,
at 600). Instead, they are more akin to the widely appli-
cable minimum wage and maximum hour rules that the
Court rejected as a basis for deeming “the entirety of
American interstate commerce” to be closely regulated in
Barlow’s, Inc. 436 U. S., at 314. If such general regula-
tions were sufficient to invoke the closely regulated indus-
try exception, it would be hard to imagine a type of busi-
ness that would not qualify. See Brief for Google Inc. as
Amicus Curiae 16–17; Brief for the Chamber of Commerce
of United States of America as Amicus Curiae 12–13.
   Petitioner attempts to recast this hodgepodge of reg-
ulations as a comprehensive scheme by referring to a
“centuries-old tradition” of warrantless searches of hotels.
Brief for Petitioner 34–36. History is relevant when deter-
mining whether an industry is closely regulated. See,
e.g., Burger, 482 U. S., at 707. The historical record here,
however, is not as clear as petitioner suggests. The City
and JUSTICE SCALIA principally point to evidence that
hotels were treated as public accommodations. Brief for
Petitioner 34–36; post, at 5–6, and n. 1. For instance, the
16                 LOS ANGELES v. PATEL

                     Opinion of the Court

Commonwealth of Massachusetts required innkeepers to
“ ‘furnish[ ] . . . suitable provisions and lodging, for the
refreshment and entertainment of strangers and travel-
lers, pasturing and stable room, hay and provender . . . for
their horses and cattle.’ ” Brief for Petitioner 35 (quoting
An Act For The Due Regulation Of Licensed Houses
(1786), reprinted in Acts and Laws of the Commonwealth
of Massachusetts 209 (1893)). But laws obligating inns to
provide suitable lodging to all paying guests are not the
same as laws subjecting inns to warrantless searches.
Petitioner also asserts that “[f]or a long time, [hotel] own-
ers left their registers open to widespread inspection.”
Brief for Petitioner 51. Setting aside that modern hotel
registries contain sensitive information, such as driver’s
licenses and credit card numbers for which there is no
historic analog, the fact that some hotels chose to make
registries accessible to the public has little bearing on
whether government authorities could have viewed these
documents on demand without a hotel’s consent.
    Even if we were to find that hotels are pervasively
regulated, §41.49 would need to satisfy three additional
criteria to be reasonable under the Fourth Amendment:
(1) “[T]here must be a ‘substantial’ government interest
that informs the regulatory scheme pursuant to which the
inspection is made”; (2) “the warrantless inspections must
be ‘necessary’ to further [the] regulatory scheme”; and (3)
“the statute’s inspection program, in terms of the certainty
and regularity of its application, [must] provid[e] a consti-
tutionally adequate substitute for a warrant.” Burger, 482
U. S., at 702–703 (internal quotation marks omitted). We
assume petitioner’s interest in ensuring that hotels main-
tain accurate and complete registries might fulfill the first
of these requirements, but conclude that §41.49 fails the
second and third prongs of this test.
    The City claims that affording hotel operators any op-
portunity for precompliance review would fatally under-
                 Cite as: 576 U. S. ____ (2015)           17

                     Opinion of the Court

mine the scheme’s efficacy by giving operators a chance to
falsify their records. Brief for Petitioner 41–42. The
Court has previously rejected this exact argument, which
could be made regarding any recordkeeping requirement.
See Barlow’s, Inc., 436 U. S., at 320 (“[It is not] apparent
why the advantages of surprise would be lost if, after
being refused entry, procedures were available for the
[Labor] Secretary to seek an ex parte warrant to reappear
at the premises without further notice to the establish-
ment being inspected”); cf. Lone Steer, 464 U. S., at 411,
415 (affirming use of administrative subpoena which
provided an opportunity for precompliance review as a
means for obtaining “payroll and sales records”). We see
no reason to accept it here.
  As explained above, nothing in our decision today pre-
cludes an officer from conducting a surprise inspection by
obtaining an ex parte warrant or, where an officer reason-
ably suspects the registry would be altered, from guarding
the registry pending a hearing on a motion to quash. See
Barlow’s, Inc., 436 U. S., at 319–321; Riley, 573 U. S., at
___ (slip op., at 12). JUSTICE SCALIA’s claim that these
procedures will prove unworkable given the large number
of hotels in Los Angeles is a red herring. See post, at 11.
While there are approximately 2,000 hotels in Los Ange-
les, ibid., there is no basis to believe that resort to such
measures will be needed to conduct spot checks in the vast
majority of them. See supra, at 11.
  Section 41.49 is also constitutionally deficient under the
“certainty and regularity” prong of the closely regulated
industries test because it fails sufficiently to constrain
police officers’ discretion as to which hotels to search and
under what circumstances. While the Court has upheld
inspection schemes of closely regulated industries that
called for searches at least four times a year, Dewey, 452
U. S., at 604, or on a “regular basis,” Burger, 482 U. S., at
711, §41.49 imposes no comparable standard.
18                 LOS ANGELES v. PATEL

                      Opinion of the Court

                       *     *     *
   For the foregoing reasons, we agree with the Ninth
Circuit that §41.49(3)(a) is facially invalid insofar as it
fails to provide any opportunity for precompliance review
before a hotel must give its guest registry to the police for
inspection. Accordingly, the judgment of the Ninth Circuit
is affirmed.
                                             It is so ordered.
                 Cite as: 576 U. S. ____ (2015)            1

                     SCALIA, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 13–1175
                         _________________


 CITY OF LOS ANGELES, CALIFORNIA, PETITIONER
          v. NARANJIBHAI PATEL, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE NINTH CIRCUIT

                        [June 22, 2015] 


   JUSTICE SCALIA, with whom THE CHIEF JUSTICE and
JUSTICE THOMAS join, dissenting.
   The city of Los Angeles, like many jurisdictions across
the country, has a law that requires motels, hotels, and
other places of overnight accommodation (hereinafter
motels) to keep a register containing specified information
about their guests. Los Angeles Municipal Code (LAMC)
§41.49(2) (2015). The purpose of this recordkeeping re-
quirement is to deter criminal conduct, on the theory that
criminals will be unwilling to carry on illicit activities in
motel rooms if they must provide identifying information
at check-in. Because this deterrent effect will only be
accomplished if motels actually do require guests to pro-
vide the required information, the ordinance also author-
izes police to conduct random spot checks of motels’ guest
registers to ensure that they are properly maintained.
§41.49(3). The ordinance limits these spot checks to the
four corners of the register, and does not authorize police
to enter any nonpublic area of the motel. To the extent
possible, police must conduct these spot checks at times
that will minimize any disruption to a motel’s business.
   The parties do not dispute the governmental interests at
stake. Motels not only provide housing to vulnerable
transient populations, they are also a particularly attrac-
tive site for criminal activity ranging from drug dealing
2                  LOS ANGELES v. PATEL

                     SCALIA, J., dissenting

and prostitution to human trafficking. Offering privacy
and anonymity on the cheap, they have been employed
as prisons for migrants smuggled across the border and
held for ransom, see Sanchez, Immigrant Smugglers Be-
come More Ruthless, Washington Post, June 28, 2004,
p. A3; Wagner, Human Smuggling, Arizona Republic,
July 23, 2006, p. A1, and rendezvous sites where child sex
workers meet their clients on threat of violence from their
procurers.
   Nevertheless, the Court today concludes that Los Ange-
les’s ordinance is “unreasonable” inasmuch as it permits
police to flip through a guest register to ensure it is being
filled out without first providing an opportunity for the
motel operator to seek judicial review. Because I believe
that such a limited inspection of a guest register is emi-
nently reasonable under the circumstances presented, I
dissent.
                               I
   I assume that respondents may bring a facial challenge
to the City’s ordinance under the Fourth Amendment.
Even so, their claim must fail because, as discussed infra,
the law is constitutional in most, if not all, of its applica-
tions. See United States v. Salerno, 481 U. S. 739, 751
(1987). But because the Court discusses the propriety of a
facial challenge at some length, I offer a few thoughts.
   Article III limits our jurisdiction to “Cases” and “Con-
troversies.” Accordingly, “[f]ederal courts may not ‘decide
questions that cannot affect the rights of litigants in the
case before them’ or give ‘opinion[s] advising what the law
would be upon a hypothetical state of facts.’ ” Chafin v.
Chafin, 568 U. S. ___, ___ (2013) (slip op., at 5). To be
sure, the reasoning of a decision may suggest that there is
no permissible application of a particular statute, Chicago
v. Morales, 527 U. S. 41, 77 (1999) (SCALIA, J., dissenting),
and under the doctrine of stare decisis, this reasoning—to
                  Cite as: 576 U. S. ____ (2015)            3

                      SCALIA, J., dissenting

the extent that it is necessary to the holding—will be
binding in all future cases. But in this sense, the facial
invalidation of a statute is a logical consequence of the
Court’s opinion, not the immediate effect of its judgment.
Although we have at times described our holdings as
invalidating a law, it is always the application of a law,
rather than the law itself, that is before us.
  The upshot is that the effect of a given case is a function
not of the plaintiff ’s characterization of his challenge, but
the narrowness or breadth of the ground that the Court
relies upon in disposing of it. If a plaintiff elects not to
present any case-specific facts in support of a claim that a
law is unconstitutional—as is the case here—he will limit
the grounds on which a Court may find for him to highly
abstract rules that would have broad application in future
cases. The decision to do this might be a poor strategic
move, especially in a Fourth Amendment case, where the
reasonableness of a search is a highly factbound question
and general, abstract rules are hard to come by. Cf.
Sibron v. New York, 392 U. S. 40, 59 (1968). But even had
the plaintiffs in this case presented voluminous facts in a
self-styled as-applied challenge, nothing would force this
Court to rely upon those facts rather than the broader
principle that the Court has chosen to rely upon. I see no
reason why a plaintiff ’s self-description of his challenge as
facial would provide an independent reason to reject it
unless we were to delegate to litigants our duty to say
what the law is.
                             II
   The Fourth Amendment provides, in relevant part, that
“[t]he right of the people to be secure in their persons,
houses, papers, and effects, against unreasonable searches
and seizures, shall not be violated, and no Warrants shall
issue, but upon probable cause.” Grammatically, the two
clauses of the Amendment seem to be independent—and
4                  LOS ANGELES v. PATEL

                     SCALIA, J., dissenting

directed at entirely different actors. The former tells the
executive what it must do when it conducts a search, and
the latter tells the judiciary what it must do when it issues
a search warrant. But in an effort to guide courts in ap-
plying the Search-and-Seizure Clause’s indeterminate
reasonableness standard, and to maintain coherence in
our case law, we have used the Warrant Clause as a
guidepost for assessing the reasonableness of a search,
and have erected a framework of presumptions applicable
to broad categories of searches conducted by executive
officials. Our case law has repeatedly recognized, how-
ever, that these are mere presumptions, and the only consti-
tutional requirement is that a search be reasonable.
  When, for example, a search is conducted to enforce an
administrative regime rather than to investigate criminal
wrongdoing, we have been willing to modify the probable-
cause standard so that a warrant may issue absent indi-
vidualized suspicion of wrongdoing. Thus, our cases say a
warrant may issue to inspect a structure for fire-code
violations on the basis of such factors as the passage of
time, the nature of the building, and the condition of the
neighborhood. Camara v. Municipal Court of City and
County of San Francisco, 387 U. S. 523, 538–539 (1967).
As we recognized in that case, “reasonableness is still the
ultimate standard. If a valid public interest justifies the
intrusion contemplated, then there is probable cause to
issue a suitably restricted search warrant.” Id., at 539.
And precisely “because the ultimate touchstone of the
Fourth Amendment is ‘reasonableness,’ ” even the pre-
sumption that the search of a home without a warrant is
unreasonable “is subject to certain exceptions.” Brigham
City v. Stuart, 547 U. S. 398, 403 (2006).
  One exception to normal warrant requirements applies
to searches of closely regulated businesses. “[W]hen an
entrepreneur embarks upon such a business, he has vol-
untarily chosen to subject himself to a full arsenal of
                 Cite as: 576 U. S. ____ (2015)           5

                     SCALIA, J., dissenting

governmental regulation,” and so a warrantless search to
enforce those regulations is not unreasonable. Marshall v.
Barlow’s, Inc., 436 U. S. 307, 313 (1978). Recognizing that
warrantless searches of closely regulated businesses may
nevertheless become unreasonable if arbitrarily conducted,
we have required laws authorizing such searches to satisfy
three criteria: (1) There must be a “ ‘substantial’ govern-
ment interest that informs the regulatory scheme pursu-
ant to which the inspection is made”; (2) “the warrantless
inspections must be ‘necessary to further [the] regulatory
scheme’ ”; and (3) “ ‘the statute’s inspection program, in
terms of the certainty and regularity of its application,
[must] provid[e] a constitutionally adequate substitute for
a warrant.’ ” New York v. Burger, 482 U. S. 691, 702–703
(1987).
  Los Angeles’s ordinance easily meets these standards.
                              A
   In determining whether a business is closely regulated,
this Court has looked to factors including the duration of
the regulatory tradition, id., at 705–707, Colonnade Cater-
ing Corp. v. United States, 397 U. S. 72, 75–77 (1970),
Donovan v. Dewey, 452 U. S. 594, 606 (1981); the compre-
hensiveness of the regulatory regime, Burger, supra, at
704–705, Dewey, supra, at 606; and the imposition of
similar regulations by other jurisdictions, Burger, supra,
at 705. These factors are not talismans, but shed light on
the expectation of privacy the owner of a business may
reasonably have, which in turn affects the reasonableness
of a warrantless search. See Barlow’s, supra, at 313.
   Reflecting the unique public role of motels and their
commercial forebears, governments have long subjected
these businesses to unique public duties, and have estab-
lished inspection regimes to ensure compliance. As Black-
stone observed, “Inns, in particular, being intended for the
lodging and receipt of travellers, may be indicted, sup-
6                      LOS ANGELES v. PATEL

                          SCALIA, J., dissenting

pressed, and the inn-keepers fined, if they refuse to enter-
tain a traveller without a very sufficient cause: for thus to
frustrate the end of their institution is held to be disorderly
behavior.” 4 W. Blackstone, Commentaries on the Laws
of England 168 (1765). Justice Story similarly recognized
“[t]he soundness of the public policy of subjecting particu-
lar classes of persons to extraordinary responsibility, in
cases where an extraordinary confidence is necessarily
reposed in them, and there is an extraordinary temptation
to fraud, or danger of plunder.” J. Story, Commentaries
on the Law of Bailments §464, pp. 487–488 (5th ed. 1851).
Accordingly, in addition to the obligation to receive any
paying guest, “innkeepers are bound to take, not merely
ordinary care, but uncommon care, of the goods, money,
and baggage of their guests,” id., §470, at 495, as travel-
lers “are obliged to rely almost implicitly on the good faith
of innholders, whose education and morals are none of the
best, and who might have frequent opportunities of asso-
ciating with ruffians and pilferers,” id., §471, at 498.
   These obligations were not merely aspirational. At the
time of the founding, searches—indeed, warrantless
searches—of inns and similar places of public accommoda-
tion were commonplace. For example, although Massa-
chusetts was perhaps the State most protective against
government searches, “the state code of 1788 still allowed
tithingmen to search public houses of entertainment on
every Sabbath without any sort of warrant.” W. Cuddihy,
Fourth Amendment: Origins and Original Meaning 602–
1791, 743 (2009).1
   As this evidence demonstrates, the regulatory tradition
governing motels is not only longstanding, but comprehen-
——————
  1 As Beale helpfully confirms, “[f ]rom the earliest times the funda-

mental characteristic of an inn has been its public nature. It is a public
house, a house of public entertainment, or, as it is legally phrased, a
common inn.” J. Beale, The Law of Innkeepers and Hotels §11, p. 10
(1906).
                  Cite as: 576 U. S. ____ (2015)             7

                      SCALIA, J., dissenting

sive. And the tradition continues in Los Angeles. The
City imposes an occupancy tax upon transients who stay
in motels, LAMC §21.7.3, and makes the motel owner
responsible for collecting it, §21.7.5. It authorizes city
officials “to enter [a motel], free of charge, during business
hours” in order to “inspect and examine” them to deter-
mine whether these tax provisions have been complied
with. §§21.7.9, 21.15. It requires all motels to obtain a
“Transient Occupancy Registration Certificate,” which
must be displayed on the premises. §21.7.6. State law
requires motels to “post in a conspicuous place . . . a
statement of rate or range of rates by the day for lodging,”
and forbids any charges in excess of those posted rates.
Cal. Civ. Code Ann. §1863 (West 2010). Hotels must
change bed linens between guests, Cal. Code Regs., tit. 25,
§40 (2015), and they must offer guests the option not to
have towels and linens laundered daily, LAMC §121.08.
“Multiuse drinking utensils” may be placed in guest rooms
only if they are “thoroughly washed and sanitized after
each use” and “placed in protective bags.” Cal. Code Regs.,
tit. 17, §30852. And state authorities, like their municipal
counterparts, “may at reasonable times enter and inspect
any hotels, motels, or other public places” to ensure com-
pliance. §30858.
   The regulatory regime at issue here is thus substan-
tially more comprehensive than the regulations governing
junkyards in Burger, where licensing, inventory-recording,
and permit-posting requirements were found sufficient to
qualify the industry as closely regulated. 482 U. S., at
704–705. The Court’s suggestion that these regulations
are not sufficiently targeted to motels, and are “akin to . . .
minimum wage and maximum hour rules,” ante, at 15, is
simply false. The regulations we have described above
reach into the “minutest detail[s]” of motel operations,
Barlow’s, supra, at 314, and those who enter that business
today (like those who have entered it over the centuries)
8                 LOS ANGELES v. PATEL

                     SCALIA, J., dissenting

do so with an expectation that they will be subjected to
especially vigilant governmental oversight.
   Finally, this ordinance is not an outlier. The City has
pointed us to more than 100 similar register-inspection
laws in cities and counties across the country, Brief for
Petitioner 36, and n. 3, and that is far from exhaustive. In
all, municipalities in at least 41 States have laws similar
to Los Angeles’s, Brief for National League of Cities et al.
as Amici Curiae 16–17, and at least 8 States have their
own laws authorizing register inspections, Brief for Cali-
fornia et al. as Amici Curiae 12–13.
   This copious evidence is surely enough to establish that
“[w]hen a [motel operator] chooses to engage in this perva-
sively regulated business . . . he does so with the
knowledge that his business records . . . will be subject to
effective inspection.” United States v. Biswell, 406 U. S.
311, 316 (1972). And that is the relevant constitutional
test—not whether this regulatory superstructure is “the
same as laws subjecting inns to warrantless searches,” or
whether, as an historical matter, government authorities
not only required these documents to be kept but permit-
ted them to be viewed on demand without a motel’s con-
sent. Ante, at 16.
   The Court’s observation that “[o]ver the past 45 years,
the Court has identified only four industries” as closely
regulated, ante, at 14, is neither here nor there. Since we
first concluded in Colonnade Catering that warrantless
searches of closely regulated businesses are reasonable,
we have only identified one industry as not closely regu-
lated, see Barlow’s, 436 U. S., at 313–314. The Court’s
statistic thus tells us more about how this Court exercises
its discretionary review than it does about the number of
industries that qualify as closely regulated. At the same
time, lower courts, which do not have the luxury of picking
the cases they hear, have identified many more businesses
as closely regulated under the test we have announced:
                 Cite as: 576 U. S. ____ (2015)            9

                     SCALIA, J., dissenting

pharmacies, United States v. Gonsalves, 435 F. 3d 64, 67
(CA1 2006); massage parlors, Pollard v. Cockrell, 578
F. 2d 1002, 1014 (CA5 1978); commercial-fishing opera-
tions, United States v. Raub, 637 F. 2d 1205, 1208–1209
(CA9 1980); day-care facilities, Rush v. Obledo, 756 F. 2d
713, 720–721 (CA9 1985); nursing homes, People v. First-
enberg, 92 Cal. App. 3d 570, 578–580, 155 Cal. Rptr. 80,
84–86 (1979); jewelers, People v. Pashigian, 150 Mich.
App. 97, 100–101, 388 N. W. 2d 259, 261–262 (1986) (per
curiam); barbershops, Stogner v. Kentucky, 638 F. Supp. 1,
3 (WD Ky. 1985); and yes, even rabbit dealers, Lesser v.
Espy, 34 F. 3d 1301, 1306–1307 (CA7 1994). Like auto-
mobile junkyards and catering companies that serve alco-
hol, many of these businesses are far from “intrinsically
dangerous,” cf. ante, at 14, n. 5. This should come as no
surprise. The reason closely regulated industries may be
searched without a warrant has nothing to do with the
risk of harm they pose; rather, it has to do with the expec-
tations of those who enter such a line of work. See Bar-
low’s, supra, at 313.
                              B
   The City’s ordinance easily satisfies the remaining
Burger requirements: It furthers a substantial govern-
mental interest, it is necessary to achieving that interest,
and it provides an adequate substitute for a search
warrant.
   Neither respondents nor the Court question the sub-
stantial interest of the City in deterring criminal activity.
See Brief for Respondents 34–41; ante, at 15. The private
pain and public costs imposed by drug dealing, prostitu-
tion, and human trafficking are beyond contention, and
motels provide an obvious haven for those who trade in
human misery.
   Warrantless inspections are also necessary to advance
this interest. Although the Court acknowledges that law
10                LOS ANGELES v. PATEL

                     SCALIA, J., dissenting

enforcement can enter a motel room without a warrant
when exigent circumstances exist, see ante, at 13, n. 4, the
whole reason criminals use motel rooms in the first place
is that they offer privacy and secrecy, so that police will
never come to discover these exigencies. The recordkeep-
ing requirement, which all parties admit is permissible,
therefore operates by deterring crime. Criminals, who
depend on the anonymity that motels offer, will balk when
confronted with a motel’s demand that they produce iden-
tification. And a motel’s evasion of the recordkeeping
requirement fosters crime. In San Diego, for example,
motel owners were indicted for collaborating with mem-
bers of the Crips street gang in the prostitution of under-
age girls; the motel owners “set aside rooms apart from
the rest of their legitimate customers where girls and
women were housed, charged the gang members/pimps a
higher rate for the rooms where ‘dates’ or ‘tricks’ took
place, and warned the gang members of inquiries by law
enforcement.” Office of the Attorney General, Cal. Dept. of
Justice, The State of Human Trafficking in California 25
(2012). The warrantless inspection requirement provides
a necessary incentive for motels to maintain their regis-
ters thoroughly and accurately: They never know when
law enforcement might drop by to inspect.
   Respondents and the Court acknowledge that inspec-
tions are necessary to achieve the purposes of the record-
keeping regime, but insist that warrantless inspections are
not. They have to acknowledge, however, that the motel
operators who conspire with drug dealers and procurers
may demand precompliance judicial review simply as a
pretext to buy time for making fraudulent entries in their
guest registers. The Court therefore must resort to argu-
ing that warrantless inspections are not “necessary” be-
cause other alternatives exist.
   The Court suggests that police could obtain an adminis-
trative subpoena to search a guest register and, if a motel
                     Cite as: 576 U. S. ____ (2015)                   11

                         SCALIA, J., dissenting

moves to quash, the police could “guar[d] the registry
pending a hearing” on the motion. Ante, at 17. This pro-
posal is equal parts 1984 and Alice in Wonderland. It
protects motels from government inspection of their regis-
ters by authorizing government agents to seize the regis-
ters2 (if “guarding” entails forbidding the register to be
moved) or to upset guests by a prolonged police presence
at the motel. The Court also notes that police can obtain
an ex parte warrant before conducting a register inspec-
tion. Ante, at 17. Presumably such warrants could issue
without probable cause of wrongdoing by a particular
motel, see Camara, 387 U. S., at 535–536; otherwise, this
would be no alternative at all. Even so, under this regime
police would have to obtain an ex parte warrant before
every inspection. That is because law enforcement would
have no way of knowing ahead of time which motels would
refuse consent to a search upon request; and if they wait
to obtain a warrant until consent is refused, motels will
have the opportunity to falsify their guest registers while
the police jump through the procedural hoops required to
obtain a warrant. It is quite plausible that the costs of
this always-get-a-warrant “alternative” would be prohibi-
tive for a police force in one of America’s largest cities,
juggling numerous law-enforcement priorities, and con-
fronting more than 2,000 motels within its jurisdiction.
E. Wallace, K. Pollock, B. Horth, S. Carty, & N. El-
yas, Los Angeles Tourism: A Domestic and Interna-
tional Analysis 7 (May 2014 online at http:
//www.lachamber.com/clientuploads/Global_Programs/
WTW/2014/LATourism_LMU_May2014.pdf            (as    visited
June 19, 2015, and available in Clerk of Court’s

——————
  2 We are not at all “baffled at the idea that . . . police officers may
seize something that they cannot immediately search.” Ante, at 12,
n. 3. We are baffled at the idea that anyone would think a seizure of
required records less intrusive than a visual inspection.
12                 LOS ANGELES v. PATEL

                     SCALIA, J., dissenting

 case file). To be sure, the fact that obtaining a warrant
might be costly will not by itself render a warrantless
search reasonable under the Fourth Amendment; but it
can render a warrantless search necessary in the context
of an administrative-search regime governing closely
regulated businesses.
  But all that discussion is in any case irrelevant. The
administrative search need only be reasonable. It is not
the burden of Los Angeles to show that there are no less
restrictive means of achieving the City’s purposes. Se-
questration or ex parte warrants were possible alternatives
to the warrantless search regimes approved by this Court
in Colonnade Catering, Biswell, Dewey, and Burger. By
importing a least-restrictive-means test into Burger’s
Fourth Amendment framework, today’s opinion implicitly
overrules that entire line of cases.
  Finally, the City’s ordinance provides an adequate
substitute for a warrant. Warrants “advise the owner of
the scope and objects of the search, beyond which limits
the inspector is not expected to proceed.” Barlow’s, 436
U. S., at 323. Ultimately, they aim to protect against
“devolv[ing] almost unbridled discretion upon executive
and administrative officers, particularly those in the field,
as to when to search and whom to search.” Ibid.
  Los Angeles’s ordinance provides that the guest register
must be kept in the guest reception or guest check-in area,
or in an adjacent office, and that it “be made available to
any officer of the Los Angeles Police Department for in-
spection. Whenever possible, the inspection shall be con-
ducted at a time and in a manner that minimizes any
interference with the operation of the business.” LAMC
§41.49(3). Nothing in the ordinance authorizes law en-
forcement to enter a nonpublic part of the motel. Compare
this to the statute upheld in Colonnade Catering, which
provided that “ ‘[t]he Secretary or his delegate may enter,
in the daytime, any building or place where any articles or
                 Cite as: 576 U. S. ____ (2015)           13

                     SCALIA, J., dissenting

objects subject to tax are made, produced, or kept, so far as
it may be necessary for the purpose of examining said
articles or objects,’ ” 397 U. S., at 73, n. 2 (quoting 26
U. S. C. §7606(a) (1964 ed.)); or the one in Biswell, which
stated that “ ‘[t]he Secretary may enter during business
hours the premises (including places of storage) of any
firearms or ammunition importer . . . for the purpose of
inspecting or examining (1) any records or documents
required to be kept . . . , and (2) any firearms or ammuni-
tion kept or stored,’ ” 406 U. S., at 312, n. 1 (quoting 18
U. S. C. §923(g) (1970 ed.)); or the one in Dewey, which
granted federal mine inspectors “ ‘a right of entry to, upon,
or through any coal or other mine,’ ” 452 U. S., at 596
(quoting 30 U. S. C. §813(a) (1976 ed., Supp. III)); or the
one in Burger, which compelled junkyard operators to
“ ‘produce such records and permit said agent or police
officer to examine them and any vehicles or parts of vehi-
cles which are subject to the record keeping requirements
of this section and which are on the premises,’ ” 482 U. S.,
at 694, n. 1 (quoting N. Y. Veh. & Traf. Law §415–a5
(McKinney 1986)). The Los Angeles ordinance—which
limits warrantless police searches to the pages of a guest
register in a public part of a motel—circumscribes police
discretion in much more exacting terms than the laws we
have approved in our earlier cases.
   The Court claims that Los Angeles’s ordinance confers
too much discretion because it does not adequately limit
the frequency of searches. Without a trace of irony, the
Court tries to distinguish Los Angeles’s law from the laws
upheld in Dewey and Burger by pointing out that the
latter regimes required inspections at least four times a
year and on a “ ‘regular basis,’ ” respectively. Ante, at 17.
But the warrantless police searches of a business “10
times a day, every day, for three months” that the Court
envisions under Los Angeles’s regime, ante, at 11, are
entirely consistent with the regimes in Dewey and Burger;
14                 LOS ANGELES v. PATEL

                     SCALIA, J., dissenting

10 times a day, every day, is “at least four times a year,”
and on a (much too) “ ‘regular basis.’ ” Ante, at 17.
  That is not to say that the Court’s hypothetical searches
are necessarily constitutional. It is only to say that Los
Angeles’s ordinance presents no greater risk that such a
hypothetical will materialize than the laws we have al-
ready upheld. As in our earlier cases, we should leave it to
lower courts to consider on a case-by-case basis whether
warrantless searches have been conducted in an unrea-
sonably intrusive or harassing manner.
                             III
   The Court reaches its wrongheaded conclusion not
simply by misapplying our precedent, but by mistaking
our precedent for the Fourth Amendment itself. Rather
than bother with the text of that Amendment, the Court
relies exclusively on our administrative-search cases,
Camara, See v. Seattle, 387 U. S. 541 (1967), and Barlow’s.
But the Constitution predates 1967, and it remains the
supreme law of the land today. Although the categorical
framework our jurisprudence has erected in this area may
provide us guidance, it is guidance to answer the constitu-
tional question at issue: whether the challenged search is
reasonable.
   An administrative, warrantless-search ordinance that
narrowly limits the scope of searches to a single business
record, that does not authorize entry upon premises not
open to the public, and that is supported by the need to
prevent fabrication of guest registers, is, to say the least,
far afield from the laws at issue in the cases the Court
relies upon. The Court concludes that such minor intru-
sions, permissible when the police are trying to tamp down
the market in stolen auto parts, are “unreasonable” when
police are instead attempting to stamp out the market in
child sex slaves.
   Because I believe that the limited warrantless searches
               Cite as: 576 U. S. ____ (2015)     15

                   SCALIA, J., dissenting

authorized by Los Angeles’s ordinance are reasonable
under the circumstances, I respectfully dissent.
                 Cite as: 576 U. S. ____ (2015)            1

                     ALITO, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 13–1175
                         _________________


 CITY OF LOS ANGELES, CALIFORNIA, PETITIONER
          v. NARANJIBHAI PATEL, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE NINTH CIRCUIT

                        [June 22, 2015] 


   JUSTICE ALITO, with whom JUSTICE THOMAS joins,
dissenting.
   After today, the city of Los Angeles can never, under any
circumstances, enforce its 116-year-old requirement that
hotels make their registers available to police officers.
That is because the Court holds that §41.49(3)(a) of the
Los Angeles Municipal Code (2015) is facially unconstitu-
tional. Before entering a judgment with such serious
safety and federalism implications, the Court must con-
clude that every application of this law is unconstitu-
tional—i.e., that “ ‘no set of circumstances exists under
which the [law] would be valid.’ ” Ante, at 7 (quoting United
States v. Salerno, 481 U. S. 739, 745 (1987)). I have
doubts about the Court’s approach to administrative
searches and closely regulated industries. Ante, at 9–17.
But even if the Court were 100% correct, it still should
uphold §41.49(3)(a) because many other applications of
this law are constitutional. Here are five examples.
   Example One. The police have probable cause to believe
that a register contains evidence of a crime. They go to a
judge and get a search warrant. The hotel operator, how-
ever, refuses to surrender the register, but instead stashes
it away. Officers could tear the hotel apart looking for it.
Or they could simply order the operator to produce it. The
Fourth Amendment does not create a right to defy a war-
2                   LOS ANGELES v. PATEL

                       ALITO, J., dissenting

rant. Hence §41.49(3)(a) could be constitutionally applied
in this scenario. Indeed, the Court concedes that it is
proper to apply a California obstruction of justice law in
such a case. See ante, at 8–9, n. 1; Brief for Respondents
49. How could applying a city law with a similar effect be
different? No one thinks that overlapping laws are uncon-
stitutional. See, e.g., Yates v. United States, 574 U. S. ___,
___ (2015) (KAGAN, J. dissenting) (slip op., at 10–11)
(“Overlap—even significant overlap—abounds in criminal
law”) (collecting citations). And a specific law gives more
notice than a general law.
  In any event, the Los Angeles ordinance is arguably
broader in at least one important respect than the Califor-
nia obstruction of justice statute on which the Court relies.
Ante, at 8–9, n. 1. The state law applies when a person
“willfully resists, delays, or obstructs any public officer . . .
in the discharge or attempt to discharge any duty of his or
her office.” Cal. Penal Code Ann. §148(a)(1) (West 2014).
In the example set out above, suppose that the hotel oper-
ator, instead of hiding the register, simply refused to tell
the police where it is located. The Court cites no Califor-
nia case holding that such a refusal would be unlawful,
and the city of Los Angeles submits that under California
law, “[o]bstruction statutes prohibit a hotel owner from
obstructing a search, but they do not require affirmative
assistance.” Reply Brief 5. The Los Angeles ordinance, by
contrast, unequivocally requires a hotel operator to make
the register available on request.
  Example Two. A murderer has kidnapped a woman
with the intent to rape and kill her and there is reason to
believe he is holed up in a certain motel. The Fourth
Amendment’s reasonableness standard accounts for exi-
gent circumstances. See, e.g., Brigham City v. Stuart, 547
U. S. 398, 403 (2006). When the police arrive, the motel
operator folds her arms and says the register is locked in a
safe. Invoking §41.49(3)(a), the police order the operator
                 Cite as: 576 U. S. ____ (2015)            3

                     ALITO, J., dissenting

to turn over the register. She refuses. The Fourth
Amendment does not protect her from arrest.
   Example Three. A neighborhood of “pay by the hour”
motels is a notorious gathering spot for child-sex traffick-
ers. Police officers drive through the neighborhood late
one night and see unusual amounts of activity at a partic-
ular motel. The officers stop and ask the motel operator
for the names of those who paid with cash to rent rooms
for less than three hours. The operator refuses to provide
the information. Requesting to see the register—and
arresting the operator for failing to provide it—would be
reasonable under the “totality of the circumstances.” Ohio
v. Robinette, 519 U. S. 33, 39 (1996). In fact, the Court has
upheld a similar reporting duty against a Fourth Amend-
ment challenge where the scope of information required
was also targeted and the public’s interest in crime pre-
vention was no less serious. See California Bankers Assn.
v. Shultz, 416 U. S. 21, 39, n. 15, 66–67 (1974) (having “no
difficulty” upholding a requirement that banks must
provide reports about transactions involving more than
$10,000, including the name, address, occupation, and
social security number of the customer involved, along
with a summary of the transaction, the amount of money
at issue, and the type of identification presented).
   Example Four. A motel is operated by a dishonest
employee. He has been charging more for rooms than he
records, all the while pocketing the difference. The owner
finds out and eagerly consents to a police inspection of the
register. But when officers arrive and ask to see the regis-
ter, the operator hides it. The Fourth Amendment does
not allow the operator’s refusal to defeat the owner’s
consent. See, e.g., Mancusi v. DeForte, 392 U. S. 364, 369–
370 (1968). Accordingly, it would not violate the Fourth
Amendment to arrest the operator for failing to make the
register “available to any officer of the Los Angeles Police
Department for inspection.” §41.49(3)(a).
4                  LOS ANGELES v. PATEL

                     ALITO, J., dissenting

   Example Five. A “mom and pop” motel always keeps its
old-fashioned guest register open on the front desk. Any-
one who wants to can walk up and leaf through it. (Such
motels are not as common as they used to be, but Los
Angeles is a big place.) The motel has no reasonable
expectation of privacy in the register, and no one doubts
that police officers—like anyone else—can enter into the
lobby. See, e.g., Florida v. Jardines, 569 U. S. 1, ___
(2013) (slip op., at 6); Donovan v. Lone Steer, Inc., 464
U. S. 408, 413 (1984). But when an officer starts looking
at the register, as others do, the motel operator at the desk
snatches it away and will not give it back. Arresting that
person would not violate the Fourth Amendment.
   These are just five examples. There are many more.
The Court rushes past examples like these by suggesting
that §41.49(3)(a) does no “work” in such scenarios. Ante,
at 8. That is not true. Under threat of legal sanction, this
law orders hotel operators to do things they do not want to
do. To be sure, there may be circumstances in which
§41.49(3)(a)’s command conflicts with the Fourth Amend-
ment, and in those circumstances the Fourth Amendment
is supreme. See U. S. Const., Art VI, cl. 2. But no differ-
ent from any other local law, the remedy for such circum-
stances should be an as-applied injunction limited to the
conflict with the Fourth Amendment. Such an injunction
would protect a hotel from being “searched 10 times a day,
every day, for three months, without any violation being
found.” Ante, at 11. But unlike facial invalidation, an as-
applied injunction does not produce collateral damage.
Section 41.49(3)(a) should be enforceable in those many
cases in which the Fourth Amendment is not violated.
   There are serious arguments that the Fourth Amend-
ment’s application to warrantless searches and seizures is
inherently inconsistent with facial challenges. See Sibron
v. New York, 392 U. S. 40, 59, 62 (1968) (explaining that
because of the Fourth Amendment’s reasonableness re-
                 Cite as: 576 U. S. ____ (2015)           5

                     ALITO, J., dissenting

quirement, “[t]he constitutional validity of a warrantless
search is pre-eminently the sort of question which can only
be decided in the concrete factual context of the individual
case”); Brief for Manhattan Institute for Policy Research
as Amicus Curiae 33 (“A constitutional claim under the
first clause of the Fourth Amendment is never a ‘facial’
challenge, because it is always and inherently a challenge
to executive action”). But assuming such facial challenges
ever make sense conceptually, this particular one fails
under basic principles of facial invalidation. The Court’s
contrary holding is befuddling. I respectfully dissent.

```

---

## GROUP: _overhaul2/lake/cases/City of Ontario v. Quon.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "City of Ontario v. Quon"
type: case
citation: ""
parallel_cite: "177 L. Ed. 2d 216; 130 S. Ct. 2619; 560 U.S. 746; 30 I.E.R. Cas. (BNA) 1345; 78 U.S.L.W. 4591; 22 Fla. L. Weekly Fed. S 470; 93 Empl. Prac. Dec. (CCH) 43,907"
neutral_cite: 2010 U.S. LEXIS 4972
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2010
date_decided: 2010-06-17
docket: 08-1332
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2010-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: City of Ontario v. Quon
  varies_by_point: false
  scope_note: "Good law; applies O'Connor v. Ortega to electronic communications. The Court deliberately declined to set broad rules about digital privacy expectations — a caution later echoed in Riley v. California and Carpenter."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/6796843/city-of-ontario-v-quon/"
  cluster_id: 6796843
  opinion_id: 6681698
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Progeny (digital workplace REP)"
related: ["[[O'Connor v. Ortega]]"]
aliases: ["Ontario v. Quon", "City of Ontario, California v. Quon"]
tags: ["case", "fourth-amendment", "special-needs", "workplace", "public-employee", "electronic-communications", "text-messages"]
holding: "A government employer's review of an employee's text messages on an employer-issued pager is a reasonable search where it is motivated by a legitimate work-related purpose and not excessive in scope; the Court assumed a privacy expectation without deciding it, declining to set broad rules for emerging communications technology."
lake:
  record_id: City of Ontario v. Quon
  status: verified
  projected_at: 2026-07-06
---

# City of Ontario v. Quon

*560 U.S. 746 (2010)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Jeff Quon, a police sergeant on the Ontario, California, SWAT team, was issued a city pager with a monthly character allotment. After he repeatedly exceeded the limit and reimbursed the overage fees, the police chief ordered an audit of the message transcripts (obtained from the wireless carrier) to decide whether the character limit was too low for legitimate work use or whether officers were effectively subsidizing personal texting. The audit revealed many personal and sexually explicit messages. Quon sued, claiming the review of his texts violated the Fourth Amendment.

## Issue
Whether a public employer's warrantless review of the contents of an employee's text messages sent on an employer-provided pager was an unreasonable search under the Fourth Amendment.

## Rule
The search is judged by reasonableness under *[[O'Connor v. Ortega]]*. Assuming arguendo that Quon had a privacy expectation and that the review was a search, the audit was reasonable: "Because the search was motivated by a legitimate work-related purpose, and because it was not excessive in scope, the search was reasonable under the approach of the *O'Connor* plurality." — 560 U.S. at 761. ^pin-761

The Court declined to announce broad rules about digital privacy: "The Court must proceed with care when considering the whole concept of privacy expectations in communications made on electronic equipment owned by a government employer. The judiciary risks error by elaborating too fully on the Fourth Amendment implications of emerging technology before its role in society has become clear." — *Id.* at 759. ^pin-759

## Application
The chief ordered the audit for a legitimate, noninvestigatory purpose — to assess whether the City's wireless plan met the SWAT team's work needs — not to expose Quon's private life, so it was justified at its inception. In scope, the review was limited to transcripts of on-duty months and redacted off-duty messages, so it was not excessively intrusive given its purpose. Whether or not Quon had a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the texts (a question the Court left open in light of fast-changing technology), the search was reasonable.

## Conclusion
The review of Quon's pager messages was a reasonable, constitutional search; the Ninth Circuit's contrary judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Quon* extends the [[O'Connor v. Ortega]] reasonableness framework to electronic workplace communications while expressly declining to fix broad digital-privacy rules — the same caution about emerging technology the Court later voiced in *[[Riley v. California]]* and *[[Carpenter v. United States]]*.

## Appears on
- [[Special Needs and Administrative Searches]] — *Progeny (digital workplace REP)*

## Sources
- *City of Ontario v. Quon*, 560 U.S. 746 (2010) — https://www.courtlistener.com/opinion/148797/city-of-ontario-v-quon/ — pinpoints: 759, 761.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5759fc97f62a974c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "City of Ontario v. Quon"}, "payload": {"all": [{"cite": "177 L. Ed. 2d 216", "page": "216", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "177"}, {"cite": "2010 U.S. LEXIS 4972", "page": "4972", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2010"}, {"cite": "130 S. Ct. 2619", "page": "2619", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "130"}, {"cite": "560 U.S. 746", "page": "746", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "560"}, {"cite": "30 I.E.R. Cas. (BNA) 1345", "page": "1345", "reporter": "I.E.R. Cas. (BNA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "30"}, {"cite": "78 U.S.L.W. 4591", "page": "4591", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "78"}, {"cite": "22 Fla. L. Weekly Fed. S 470", "page": "470", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "22"}, {"cite": "93 Empl. Prac. Dec. (CCH) 43,907", "page": "43,907", "reporter": "Empl. Prac. Dec. (CCH)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "93"}], "display": null, "official": null, "official_selection_present": false, "record_id": "City of Ontario v. Quon"}}
{"assertion_id": "b74e8c886d67b906", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-759", "record_id": "City of Ontario v. Quon"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-759", "pinpoint_status": "slip-only", "quote": "The Court must proceed with care when considering the whole concept of privacy expectations in communications made on electronic equipment owned by a government employer. The judiciary risks error by elaborating too fully on the Fourth Amendment implications of emerging technology before its role in society has become clear.", "quote_fidelity": "mismatch", "record_id": "City of Ontario v. Quon", "star_marker": null}}
{"assertion_id": "d7acd4198ca71df5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-761", "record_id": "City of Ontario v. Quon"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-761", "pinpoint_status": "slip-only", "quote": "--- # City of Ontario v. Quon *560 U.S. 746 (2010)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Jeff Quon, a police sergeant on the Ontario, California, SWAT team, was issued a city pager with a monthly character allotment. After he repeatedly exceeded the limit and reimbursed the overage fees, the police chief ordered an audit of the message transcripts (obtained from the wireless carrier) to decide whether the character limit was too low for legitimate work use or whether officers were effectively subsidizing personal texting. The audit revealed many personal and sexually explicit messages. Quon sued, claiming the review of his texts violated the Fourth Amendment. ## Issue Whether a public employer's warrantless review of the contents of an employee's text messages sent on an employer-provided pager was an unreasonable search under the Fourth Amendment. ## Rule The search is judged by reasonableness under *O'Connor v. Ortega*. Assuming arguendo that Quon had a privacy expectation and that the review was a search, the audit was reasonable:", "quote_fidelity": "mismatch", "record_id": "City of Ontario v. Quon", "star_marker": null}}
{"assertion_id": "8c767db79fb25690", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "City of Ontario v. Quon"}, "payload": {"as_of_content": "2010-06-17", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "City of Ontario v. Quon", "scope_note": "Good law; applies O'Connor v. Ortega to electronic communications. The Court deliberately declined to set broad rules about digital privacy expectations — a caution later echoed in Riley v. California and Carpenter.", "varies_by_point": false}}
```

### lake record — City of Ontario v. Quon

```json
{
  "schema_version": "s2.v1",
  "record_id": "City of Ontario v. Quon",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "City of Ontario v. Quon",
    "case_name_short": "Quon",
    "case_name_full": "CITY OF ONTARIO, CALIFORNIA v. JEFF QUON",
    "input_case_name": "City of Ontario v. Quon",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2010-06-17",
    "year": 2010,
    "docket": "08-1332",
    "cluster_id": 6796843,
    "lead_opinion_id": 6681698,
    "sibling_ids": [
      6681698,
      6681699,
      6681700
    ],
    "absolute_url": "/opinion/6796843/city-of-ontario-v-quon/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 148797,
        "score": 120,
        "case_name": "City of Ontario v. Quon"
      },
      {
        "cluster_id": 6794962,
        "score": 20,
        "case_name": "City of Ontario v. Quon"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "177 L. Ed. 2d 216",
        "volume": "177",
        "reporter": "L. Ed. 2d",
        "page": "216",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "130 S. Ct. 2619",
        "volume": "130",
        "reporter": "S. Ct.",
        "page": "2619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "560 U.S. 746",
        "volume": "560",
        "reporter": "U.S.",
        "page": "746",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "30 I.E.R. Cas. (BNA) 1345",
        "volume": "30",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "1345",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "78 U.S.L.W. 4591",
        "volume": "78",
        "reporter": "U.S.L.W.",
        "page": "4591",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 Fla. L. Weekly Fed. S 470",
        "volume": "22",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "470",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Empl. Prac. Dec. (CCH) 43,907",
        "volume": "93",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "43,907",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2010 U.S. LEXIS 4972",
        "volume": "2010",
        "reporter": "U.S. LEXIS",
        "page": "4972",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "177 L. Ed. 2d 216",
        "volume": "177",
        "reporter": "L. Ed. 2d",
        "page": "216",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 U.S. LEXIS 4972",
        "volume": "2010",
        "reporter": "U.S. LEXIS",
        "page": "4972",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "130 S. Ct. 2619",
        "volume": "130",
        "reporter": "S. Ct.",
        "page": "2619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "560 U.S. 746",
        "volume": "560",
        "reporter": "U.S.",
        "page": "746",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "30 I.E.R. Cas. (BNA) 1345",
        "volume": "30",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "1345",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "78 U.S.L.W. 4591",
        "volume": "78",
        "reporter": "U.S.L.W.",
        "page": "4591",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 Fla. L. Weekly Fed. S 470",
        "volume": "22",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "470",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Empl. Prac. Dec. (CCH) 43,907",
        "volume": "93",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "43,907",
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
      "id": "pin-761",
      "page": null,
      "quote": "--- # City of Ontario v. Quon *560 U.S. 746 (2010)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Jeff Quon, a police sergeant on the Ontario, California, SWAT team, was issued a city pager with a monthly character allotment. After he repeatedly exceeded the limit and reimbursed the overage fees, the police chief ordered an audit of the message transcripts (obtained from the wireless carrier) to decide whether the character limit was too low for legitimate work use or whether officers were effectively subsidizing personal texting. The audit revealed many personal and sexually explicit messages. Quon sued, claiming the review of his texts violated the Fourth Amendment. ## Issue Whether a public employer's warrantless review of the contents of an employee's text messages sent on an employer-provided pager was an unreasonable search under the Fourth Amendment. ## Rule The search is judged by reasonableness under *O'Connor v. Ortega*. Assuming arguendo that Quon had a privacy expectation and that the review was a search, the audit was reasonable:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-759",
      "page": null,
      "quote": "The Court must proceed with care when considering the whole concept of privacy expectations in communications made on electronic equipment owned by a government employer. The judiciary risks error by elaborating too fully on the Fourth Amendment implications of emerging technology before its role in society has become clear.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2010-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "City of Ontario v. Quon",
    "varies_by_point": false,
    "scope_note": "Good law; applies O'Connor v. Ortega to electronic communications. The Court deliberately declined to set broad rules about digital privacy expectations \u2014 a caution later echoed in Riley v. California and Carpenter.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "In re the United States",
          "cluster_id": 8441402,
          "cite": [
            "724 F.3d 600",
            "58 Communications Reg. (P&F) 1292",
            "2013 WL 3914484",
            "2013 U.S. App. LEXIS 15510"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Zailey Hess v. Jamie Garcia",
          "cluster_id": 9415232,
          "cite": [
            "72 F.4th 753"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Love v. State",
          "cluster_id": 6241312,
          "cite": [
            "543 S.W.3d 835"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Simon v. City and County of San Francisco",
          "cluster_id": 10382775,
          "cite": [
            "135 F.4th 784"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ruskai v. Pistole",
          "cluster_id": 2764193,
          "cite": [
            "775 F.3d 61",
            "2014 U.S. App. LEXIS 24350",
            "2014 WL 7272770"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crenshaw-Logal v. City of Abilene",
          "cluster_id": 8468431,
          "cite": [
            "436 F. App'x 306"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
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
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Caraballo",
          "cluster_id": 8727352,
          "cite": [
            "963 F. Supp. 2d 341",
            "2013 WL 4039028",
            "2013 U.S. Dist. LEXIS 112739"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. Town of Duxbury",
          "cluster_id": 4643762,
          "cite": [
            "931 F.3d 102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adkisson v. Paxton",
          "cluster_id": 5445438,
          "cite": [
            "459 S.W.3d 761",
            "43 Media L. Rep. (BNA) 1560",
            "2015 Tex. App. LEXIS 2167",
            "2015 WL 1030295"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Moises Zelaya-Veliz",
          "cluster_id": 9476330,
          "cite": [
            "94 F.4th 321"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Osborne v. Harris County",
          "cluster_id": 7312912,
          "cite": [
            "97 F. Supp. 3d 911",
            "2015 U.S. Dist. LEXIS 42534"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rickey Beene",
          "cluster_id": 3183556,
          "cite": [
            "818 F.3d 157",
            "2016 U.S. App. LEXIS 4331",
            "2016 WL 890127"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In re the United States for an Order Pursuant to Title 18",
          "cluster_id": 8713843,
          "cite": [
            "849 F. Supp. 2d 177",
            "2012 WL 989638",
            "2012 U.S. Dist. LEXIS 42779"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barrett v. Town of Plainville",
          "cluster_id": 7327099,
          "cite": [
            "272 F. Supp. 3d 235"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clarissa Gilmore v. Georgia Department of Corrections",
          "cluster_id": 10631717,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Apache Stronghold v. USA",
          "cluster_id": 9501928,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gilberto Morales",
          "cluster_id": 9476335,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jonathan Zelaya-Veliz",
          "cluster_id": 9476334,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Molina-Veliz",
          "cluster_id": 9476333,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Luis Gonzales",
          "cluster_id": 9476332,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Santos Castro",
          "cluster_id": 9476324,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zailey Hess v. Jamie Garcia",
          "cluster_id": 9415233,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "ANDRE VERDUN V. CITY OF SAN DIEGO",
          "cluster_id": 9367683,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jordan",
          "cluster_id": 8358611,
          "cite": [
            "33 Mass. L. Rptr. 180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(6681698 OR 6681699 OR 6681700) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 21,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 21,
        "triage_read": 1,
        "triage_snippet_classified": 20
      },
      "lane2_top_cited": {
        "query": "cites:(6681698 OR 6681699 OR 6681700)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0wJnM9OTQ3NjMzMyZ0PW8mZD0yMDI2LTA3LTA2JnA9Mg%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%286681698+OR+6681699+OR+6681700%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(6681698 OR 6681699 OR 6681700)",
        "reviewed": 9,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 9,
        "triage_read": 0,
        "triage_snippet_classified": 9
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(6681698 OR 6681699 OR 6681700)",
    "indexed_citing_opinions": 29,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 6681698,
        "count": 29,
        "count_source": "search"
      },
      {
        "opinion_id": 6681699,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 6681700,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 234,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/city-of-ontario-v-quon.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQ5MDgzNjkmcz0zMTgzNTU2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%286681698+OR+6681699+OR+6681700%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T00:26:01Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:26:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:26:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:29:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:26:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — City of Ontario v. Quon

```
<opinion type="majority">
<p id="b267-8">OPINION OF THE COURT</p>
<p id="b267-9">[<span class="citation no-link">560 U.S. 750</span>]</p>
<author id="b267-10">Justice Kennedy</author>
<p id="AMr">delivered the opinion of the Court.</p>
<p id="b267-11">This case involves the assertion by a government employer of the right, in circumstances to be described, to read text messages sent and received on a pager the employer owned and issued to an employee. The employee contends that the privacy of the messages is protected by the ban on “unreasonable searches and seizures” found in the Fourth Amendment to the United States Constitution, made applicable to the States by the Due Process Clause of the Fourteenth Amendment. <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U.S. 643</a></span>, <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">81 S. Ct. 1684</a></span>, <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">6 L. Ed. 2d 1081</a></span> (1961). Though the case touches issues of far-reaching significance, the Court concludes it can be resolved by settled principles determining when a search is reasonable.</p>
<p id="b267-12">I</p>
<p id="b267-13">A</p>
<p id="b267-14">The city of Ontario (City) is a political subdivision of the State of California. The case arose out of incidents in 2001 and 2002 when respondent Jeff Quon was employed by the Ontario Police Department (OPD). He was a police sergeant and member of OPD’s Special Weapons and Tactics (SWAT) Team. The City, OPD, and OPD’s Chief, Lloyd Scharf, are petitioners here. As will be discussed, two respondents share the last name Quon. In this opinion “Quon” refers to Jeff Quon, for the relevant events mostly revolve around him.</p>
<p id="b267-15">In October 2001, the City acquired 20 alphanumeric pagers capable of sending and receiving text messages. Arch Wireless Operating Company <page-number citation-index="1" label="222">*222</page-number>provided wireless service for the pagers. Under the City’s service contract with Arch Wireless, each pager was allotted a limited number of characters</p>
<p id="b268-4">[<span class="citation no-link">560 U.S. 751</span>]</p>
<p id="b268-5">sent or received each month. Usage in excess of that amount would result in an additional fee. The City issued pagers to Quon and other SWAT Team members in order to help the SWAT Team mobilize and respond to emergency situations.</p>
<p id="b268-6">Before acquiring the pagers, the City announced a “Computer Usage, Internet and E-Mail Policy” (Computer Policy) that applied to all employees. Among other provisions, it specified that the City “reserves the right to monitor and log all network activity including e-mail and Internet use, with or without notice. Users should have no expectation of privacy or confidentiality when using these resources.” App. to Pet. for Cert. 151, 152. In March 2000, Quon signed a statement acknowledging that he had read and understood the Computer Policy.</p>
<p id="b268-7">The Computer Policy did not apply, on its face, to text messaging. Text messages share similarities with e-mails, but the two differ in an important way. In this case, for instance, an e-mail sent on a City computer was transmitted through the City’s own data servers, but a text message sent on one of the City’s pagers was transmitted using wireless radio frequencies from an individual pager to a receiving station owned by Arch Wireless. It was routed through Arch Wireless’ computer network, where it remained until the recipient’s pager or cellular telephone was ready to receive the message, at which point Arch Wireless transmitted the message from the transmitting station nearest to the recipient. After delivery, Arch Wireless retained a copy on its computer servers. The message did not pass through computers owned by the City.</p>
<p id="b268-9">Although the Computer Policy did not cover text messages by its explicit terms, the City made clear to employees, including Quon, that the City would treat text messages the same way as it treated e-mails. At an April 18, 2002, staff meeting at which Quon was present, Lieutenant Steven Duke, the OPD officer responsible for the City’s contract</p>
<p id="b268-10">[<span class="citation no-link">560 U.S. 752</span>]</p>
<p id="b268-11">with Arch Wireless, told officers that messages sent on the pagers “are considered e-mail messages. This means that [text] messages would fall under the City’s policy as public information and [would be] eligible for auditing.” App. 30. Duke’s comments were put in writing in a memorandum sent on April 29, 2002, by Chief Scharf to Quon and other City personnel.</p>
<p id="b268-12">Within the first or second billing cycle after the pagers were distributed, Quon exceeded his monthly text message character allotment. Duke told Quon about the overage, and reminded him that messages sent on the pagers were “considered e-mail and could be audited.” <em>Id., </em>at 40. Duke said, however, that “it was not his intent to audit [an] employee’s text messages to see if the overage [was] due to work related transmissions.” <em>Ibid. </em>Duke suggested that Quon could reimburse the City for the overage fee rather than have Duke audit the messages. Quon wrote a check to the City for the overage. Duke offered the same arrangement to other employees who incurred overage fees.</p>
<p id="b268-13">Over the next few months, Quon exceeded his character limit three or four times. Each time he reimbursed the City. Quon and another officer again incurred overage fees for their <page-number citation-index="1" label="223">*223</page-number>pager usage in August 2002. At a meeting in October, Duke told Scharf that he had become “ ‘tired of being a bill collector.’ ” <em>Id., </em>at 91. Scharf decided to determine whether the existing character limit was too low—that is, whether officers such as Quon were having to pay fees for sending work-related messages—or if the overages were for personal messages. Scharf told Duke to request transcripts of text messages sent in August and September by Quon and the other employee who had exceeded the character allowance.</p>
<p id="b269-4">At Duke’s request, an administrative assistant employed by OPD contacted Arch Wireless. After verifying that the City was the subscriber on the accounts, Arch Wireless provided the desired transcripts. Duke reviewed the transcripts</p>
<p id="b269-5">[<span class="citation no-link">560 U.S. 753</span>]</p>
<p id="b269-6">and discovered that many of the messages sent and received on Quon’s pager were not work related, and some were sexually explicit. Duke reported his findings to Scharf, who, along with Quon’s immediate supervisor, reviewed the transcripts himself. After his review, Scharf referred the matter to OPD’s internal affairs division for an investigation into whether Quon was violating OPD rules by pursuing personal matters while on duty.</p>
<p id="b269-7">The officer in charge of the internal affairs review was Sergeant Patrick McMahon. Before conducting a review, McMahon used Quon’s work schedule to redact the transcripts in order to eliminate any messages Quon sent while off duty. He then reviewed the content of the messages Quon sent during work hours. McMahon’s report noted that Quon sent or received 456 messages during work hours in the month of August 2002, of which no more than 57 were work related; he sent as many as 80 messages during a single day at work; and on an average workday, Quon sent or received 28 messages, of which only 3 were related to police business. The report concluded that Quon had violated OPD rules. Quon was allegedly disciplined.</p>
<p id="b269-9">B</p>
<p id="b269-10">Raising claims under Rev. Stat. § 1979, <span class="citation no-link">42 U.S.C. § 1983</span>; <span class="citation no-link">18 U.S.C. § 2701</span> <em>et seq., </em>popularly known as the Stored Communications Act (SCA); and California law, Quon filed suit against petitioners in the United States District Court for the Central District of California. Arch Wireless and an individual not relevant here were also named as defendants. Quon was joined in his suit by another plaintiff who is not a party before this Court and by the other respondents, each of whom exchanged text messages with Quon during August and September 2002: Jerilyn Quon, Jeff Quon’s then-wife, from whom he was separated; April Florio, an OPD employee with whom Jeff Quon was romantically involved; and Steve Trujillo, another member of the OPD SWAT Team.</p>
<p id="b269-11">[<span class="citation no-link">560 U.S. 754</span>]</p>
<p id="b269-12">Among the allegations in the complaint was that petitioners violated respondents’ Fourth Amendment rights and the SCA by obtaining and reviewing the transcript of Jeff Quon’s pager messages and that Arch Wireless had violated the SCA by turning over the transcript to the City.</p>
<p id="b269-13">The parties filed cross-motions for summary judgment. The District Court granted Arch Wireless’ motion for summary judgment on the SCA claim but denied petitioners’ motion for summary judgment on the Fourth Amendment claims. <em>Quon </em>v. <em>Arch Wireless Operating Co., </em><span class="citation" data-id="2499887"><a href="/opinion/2499887/quon-v-arch-wireless-operating-co-inc/" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc.">445 F. Supp. 2d 1116</a></span> (CD Cal. 2006). Relying on <page-number citation-index="1" label="224">*224</page-number>the plurality opinion in <em>O’Connor </em>v. <em>Ortega, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#711" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U.S. 709, 711</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (1987), the District Court determined that Quon had a reasonable expectation of privacy in the content of his text messages. Whether the audit of the text messages was nonetheless reasonable, the District Court concluded, turned on Chief Scharf's intent: “[I]f the purpose for the audit was to determine if Quon was using his pager to ‘play games’ and ‘waste time,’ then the audit was not constitutionally reasonable”; but if the audit’s purpose “was to determine the efficacy of the existing character limits to ensure that officers were not paying hidden work-related costs, ... no constitutional violation occurred.” <span class="citation" data-id="2499887"><a href="/opinion/2499887/quon-v-arch-wireless-operating-co-inc/#1146" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc.">445 F. Supp. 2d, at 1146</a></span>.</p>
<p id="b270-4">The District Court held a jury trial to determine the purpose of the audit. The jury concluded that Scharf ordered the audit to determine the efficacy of the character limits. The District Court accordingly held that petitioners did not violate the Fourth Amendment. It entered judgment in their favor.</p>
<p id="b270-5">The United States Court of Appeals for the Ninth Circuit reversed in part. <em>Quon </em>v. <em>Arch Wireless Operating Co., </em><span class="citation" data-id="1455295"><a href="/opinion/1455295/quon-v-arch-wireless-operating-co-inc/" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc.">529 F.3d 892</a></span> (2008). The panel agreed with the District Court that Jeff Quon had a reasonable expectation of privacy in his text messages but disagreed with the District Court about whether the search was reasonable. Even though the search was conducted for “a legitimate work-related rationale,”</p>
<p id="b270-6">[<span class="citation no-link">560 U.S. 755</span>]</p>
<p id="b270-7">the Court of Appeals concluded, it “was not reasonable in scope.” <em>Id., </em>at 908. The panel disagreed with the District Court’s observation that “there were no less-intrusive means” that Chief Scharf could have used “to verify the efficacy of the 25,000 character limit . . . without intruding on [respondents’] Fourth Amendment rights.” <em>Id., </em>at 908-909. The opinion pointed to a “host of simple ways” that the chief could have used instead of the audit, such as warning Quon at the beginning of the month that his future messages would be audited, or asking Quon himself to redact the transcript of his messages. <em>Id., </em>at 909. The Court of Appeals further concluded that Arch Wireless had violated the SCA by turning over the transcript to the City.</p>
<p id="b270-9">The Ninth Circuit denied a petition for rehearing en banc. <em>Quon </em>v. <em>Arch Wireless Operating Co., </em><span class="citation" data-id="9849623"><a href="/opinion/1276870/quon-v-arch-wireless-operating-co-inc/" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc.">554 F.3d 769</a></span> (2009). Judge Ikuta, joined by six other Circuit Judges, dissented. <span class="citation" data-id="9849623"><a href="/opinion/1276870/quon-v-arch-wireless-operating-co-inc/#774" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc."><em>Id., </em>at 774-779</a></span>. Judge Wardlaw concurred in the denial of rehearing, defending the panel’s opinion against the dissent. <span class="citation" data-id="9849623"><a href="/opinion/1276870/quon-v-arch-wireless-operating-co-inc/#769" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc."><em>Id., </em>at 769-774</a></span>.</p>
<p id="b270-10">This Court granted the petition for certiorari filed by the City, OPD, and Chief Scharf challenging the Court of Appeals’ holding that they violated the Fourth Amendment. <span class="citation no-link">558 U.S. 1090</span>, <span class="citation no-link">130 S. Ct. 1011</span>, <span class="citation no-link">175 L. Ed. 2d 617</span> (2009). The petition for certiorari filed by Arch Wireless challenging the Ninth Circuit’s ruling that Arch Wireless violated the SCA was denied. <em>USA Mobility Wireless, Inc. </em>v. <em>Quon, </em><span class="citation no-link">558 U.S. 1091</span>, <span class="citation no-link">130 S. Ct. 1011</span>, <span class="citation no-link">175 L. Ed. 2d 618</span> (2009).</p>
<p id="b270-11">II</p>
<p id="b270-12">The Fourth Amendment states: “The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated . . . .” It is well settled that the Fourth Amendment’s protection extends beyond the sphere of criminal investigations. <em>Camara </em>v. <em>Municipal Court of City and County of San Francisco, </em><page-number citation-index="1" label="225">*225</page-number><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#530" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U.S. 523, 530</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">87 S. Ct. 1727</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">18 L. Ed. 2d 930</a></span> (1967). “The Amendment guarantees the privacy, dignity, and security of</p>
<p id="b271-4">[<span class="citation no-link">560 U.S. 756</span>]</p>
<p id="b271-5">persons against certain arbitrary and invasive acts by officers of the Government,” without regard to whether the government actor is investigating crime or performing another function. <em>Skinner </em>v. <em>Railway Labor Executives’ Assn., </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#613" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U.S. 602, 613-614</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">109 S. Ct. 1402</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">103 L. Ed. 2d 639</a></span> (1989). The Fourth Amendment applies as well when the Government acts in its capacity as an employer. <em>Treasury Employees </em>v. <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#665" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U.S. 656, 665</a></span>, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">109 S. Ct. 1384</a></span>, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">103 L. Ed. 2d 685</a></span> (1989).</p>
<p id="b271-6">The Court discussed this principle in <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span>. </em>There a physician employed by a state hospital alleged that hospital officials investigating workplace misconduct had violated his Fourth Amendment rights by searching his office and seizing personal items from his desk and filing cabinet. All Members of the Court agreed with the general principle that  “[individuals do not lose Fourth Amendment rights merely because they work for the government instead of a private employer.” <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#717" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U.S., at 717</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (plurality opinion); see also <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#731" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 731</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (Scalia, J., concurring in judgment); <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#737" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 737</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (Blackmun, J., dissenting). A majority of the Court further agreed that “ ‘special needs, beyond the normal need for law enforcement,’ ” make the warrant and probable-cause requirement impracticable for government employers. <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#725" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>Id., </em>at 725</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (plurality opinion) (quoting <em>New Jersey </em>v. <em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#351" aria-description="Citation for case: New Jersey v. T. L. O.">469 U.S. 325, 351</a></span>, <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">105 S. Ct. 733</a></span>, <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">83 L. Ed. 2d 720</a></span> (1985) (Blackmun, J., concurring in judgment)); <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#732" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U.S., at 732</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (opinion of Scalia, J.) (quoting same).</p>
<p id="b271-8">The <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span> </em>Court did disagree on the proper analytical framework for Fourth Amendment claims against government employers. A four-Justice plurality concluded that the correct analysis has two steps. First, because “some government offices may be so open to fellow employees or the public that no expectation of privacy is reasonable,” id<em>., </em>at 718, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>, a court must consider “ [t]he operational realities of the workplace” in order to determine whether an employee’s Fourth Amendment rights are implicated, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#717" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 717</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>. On this view, “the question whether an employee has a reasonable</p>
<p id="b271-9">[<span class="citation no-link">560 U.S. 757</span>]</p>
<p id="b271-10">expectation of privacy must be addressed on a case-by-case basis.” <em>Id., </em>at 718, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>. Next, where an employee has a legitimate privacy expectation, an employer’s intrusion on that expectation “for noninvestiga-tory, work-related purposes, as well as for investigations of work-related misconduct, should be judged by the standard of reasonableness under all the circumstances.” <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#725" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>Id., </em>at 725-726</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>.</p>
<p id="b271-11">Justice Scalia, concurring in the judgment, outlined a different approach. His opinion would have dispensed with an inquiry into “operational realities” and would conclude “that the offices of government employees . . . are covered by Fourth Amendment protections as a general matter.” <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#731" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>Id., </em>at 731</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>. But he would also have held “that government searches to retrieve work-related materials or to investigate violations of workplace rules—searches of the sort that are regarded as reasonable and normal in <page-number citation-index="1" label="226">*226</page-number>the private-employer context—do not violate the Fourth Amendment.” <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#732" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>Id., </em>at 732</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>.</p>
<p id="b272-4">Later, in the <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span> </em>decision, the Court explained that “operational realities” could diminish an employee’s privacy expectations, and that this diminution could be taken into consideration when assessing the reasonableness of a workplace search. 489 U.S., at 671, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">109 S. Ct. 1402</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">103 L. Ed. 2d 639</a></span>. In the two decades since <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span>, </em>however, the threshold test for determining the scope of an employee’s Fourth Amendment rights has not been clarified further. Here, though they disagree on whether Quon had a reasonable expectation of privacy, both petitioners and respondents start from the premise that the <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span> </em>plurality controls. See Brief for Petitioners 22-28; Brief for Respondents 25-32. It is not necessary to resolve whether that premise is correct. The case can be decided by determining that the search was reasonable even assuming Quon had a reasonable expectation of privacy. The two <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span> </em>approaches—the plurality’s and Justice Scalia’s—there-fore lead to the same result here.</p>
<p id="b272-5">[<span class="citation no-link">560 U.S. 758</span>]</p>
<p id="b272-6">III</p>
<p id="b272-7">A</p>
<p id="b272-8">Before turning to the reasonableness of the search, it is instructive to note the parties’ disagreement over whether Quon had a reasonable expectation of privacy. The record does establish that OPD, at the outset, made it clear that pager messages were not considered private. The City’s Computer Policy stated that “[u]sers should have no expectation of privacy or confidentiality when using” City computers. App. to Pet. for Cert. 152. Chief Scharf’s memo and Duke’s statements made clear that this official policy extended to text messaging. The disagreement, at least as respondents see the case, is over whether Duke’s later statements overrode the official policy. Respondents contend that because Duke told Quon that an audit would be unnecessary if Quon paid for the overage, Quon reasonably could expect that the contents of his messages would remain private.</p>
<p id="b272-10">At this point, were we to assume that inquiry into “operational realities” were called for, compare <em>O’Connor, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#717" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U.S., at 717</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (plurality opinion), with <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#730" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 730-731</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (opinion of Scalia, J.); see also <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#737" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 737-738</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (Blackmun, J., dissenting), it would be necessary to ask whether Duke’s statements could be taken as announcing a change in OPD policy, and if so, whether he had, in fact or appearance, the authority to make such a change and to guarantee the privacy of text messaging. It would also be necessary to consider whether a review of messages sent on police pagers, particularly those sent while officers are on duty, might be justified for other reasons, including performance evaluations, litigation concerning the lawfulness of police actions, and perhaps compliance with state open records laws. See Brief for Petitioners 35-40 (citing Cal. Public Records Act, Cal. Govt. Code Ann. § 6250 <em>et seq. </em>(West 2008)). These matters would all bear on the legitimacy of an employee’s privacy expectation.</p>
<p id="b272-11">[<span class="citation no-link">560 U.S. 759</span>]</p>
<p id="b272-12">The Court must proceed with care when considering the whole concept of privacy expectations in communi<page-number citation-index="1" label="227">*227</page-number>cations made on electronic equipment owned by a government employer. The judiciary risks error by elaborating too fully on the Fourth Amendment implications of emerging technology before its role in society has become clear. See, <em>e.g., Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U.S. 438</a></span>, <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">48 S. Ct. 564</a></span>, <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">72 L. Ed. 944</a></span> (1928), overruled by <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U.S. 347, 353</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S. Ct. 507</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L. Ed. 2d 576</a></span> (1967). In <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>the Court relied on its own knowledge and experience to conclude that there is a reasonable expectation of privacy in a telephone booth. See <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States"><em>id., </em>at 360-361</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S. Ct. 507</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L. Ed. 2d 576</a></span> (Harlan, J., concurring). It is not so clear that courts at present are on so sure a ground. Prudence counsels caution before the facts in the instant case are used to establish far-reaching premises that define the existence, and extent, of privacy expectations enjoyed by employees when using employer-provided communication devices.</p>
<p id="b273-4">Rapid changes in the dynamics of communication and information transmission are evident not just in the technology itself but in what society accepts as proper behavior. As one <em>amici </em>brief notes, many employers expect or at least tolerate personal use of such equipment by employees because it often increases worker efficiency. See Brief for Electronic Frontier Foundation et al. 16-20. Another <em>amicus </em>points out that the law is beginning to respond to these developments, as some States have recently passed statutes requiring employers to notify employees when monitoring their electronic communications. See Brief for New York Intellectual Property Law Association 22 (citing Del. Code Ann., Tit. 19, § 705 (2005); <span class="citation no-link">Conn. Gen. Stat. Ann. § 31</span>-48d (West 2003)). At present, it is uncertain how workplace norms, and the law’s treatment of them, will evolve.</p>
<p id="b273-6">Even if the Court were certain that the <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span> </em>plurality’s approach were the right one, the Court would have difficulty predicting how employees’ privacy expectations will be shaped by those changes or the degree to which society</p>
<p id="b273-7">[<span class="citation no-link">560 U.S. 760</span>]</p>
<p id="b273-8">will be prepared to recognize those expectations as reasonable. See <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#715" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U.S., at 715</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>. Cell phone and text message communications are so pervasive that some persons may consider them to be essential means or necessary instruments for self-expression, even self-identification. That might strengthen the case for an expectation of privacy. On the other hand, the ubiquity of those devices has made them generally affordable, so one could counter that employees who need cell phones or similar devices for personal matters can purchase and pay for their own. And employer policies concerning communications will of course shape the reasonable expectations of their employees, especially to the extent that such policies are clearly communicated.</p>
<p id="b273-9">Abroad holding concerning employees’ privacy expectations vis-a-vis employer-provided technological equipment might have implications for future cases that cannot be predicted. It is preferable to dispose of this case on narrower grounds. For present purposes we assume several propositions, <em>arguendo: </em>First, Quon had a reasonable expectation of privacy in the text messages sent on the pager provided to him by the City; second, petitioners’ review of the transcript constituted a search within the meaning of the Fourth Amendment; and third, the principles applicable to a government employer’s search of an employ<page-number citation-index="1" label="228">*228</page-number>ee’s physical office apply with at least the same force when the employer intrudes on the employee’s privacy in the electronic sphere.</p>
<p id="b274-4">B</p>
<p id="b274-5">Even if Quon had a reasonable expectation of privacy in his text messages, petitioners did not necessarily violate the Fourth Amendment by obtaining and reviewing the transcripts.  Although as a general matter, warrantless searches “are <em>per se </em>unreasonable under the Fourth Amendment,” there are “a few specifically established and well-delineated exceptions” to that general rule. <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States"><em>Katz, supra, </em>at 357</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S. Ct. 507</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L. Ed. 2d 576</a></span>. The Court has held that the “ ‘special needs’ ” of the workplace</p>
<p id="AMa">[<span class="citation no-link">560 U.S. 761</span>]</p>
<p id="b274-6">justify one such exception. <em>O’Connor, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#725" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U.S., at 725</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (plurality opinion); <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#732" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 732</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (Scalia, J., concurring in judgment); <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#666" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U.S., at 666-667</a></span>, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">109 S. Ct. 1384</a></span>, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">103 L. Ed. 2d 685</a></span>.</p>
<p id="b274-7">Under the approach of the <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span> </em>plurality,  when conducted for a “noninvestigatory, work-related purpos[e]” or for the “investi-gatio[n] of work-related misconduct,” a government employer’s warrantless search is reasonable if it is “ ‘justified at its inception’ ” and if “ ‘the measures adopted are reasonably related to the objectives of the search and not excessively intrusive in light of’ ” the circumstances giving rise to the search. <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#725" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U.S., at 725-726</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>. The search here satisfied the standard of the <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span> </em>plurality and was reasonable under that approach.</p>
<p id="b274-8">The search was justified at its inception because there were “reasonable grounds for suspecting that the search [was] necessary for a noninvestigatory work-related purpose.” <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#726" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>Id., </em>at 726</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>. As a jury found, Chief Scharf ordered the search in order to determine whether the character limit on the City’s contract with Arch Wireless was sufficient to meet the City’s needs. This was, as the Ninth Circuit noted, a “legitimate work-related rationale.” <span class="citation" data-id="1455295"><a href="/opinion/1455295/quon-v-arch-wireless-operating-co-inc/#908" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc.">529 F.3d, at 908</a></span>. The City and OPD had a legitimate interest in ensuring that employees were not being forced to pay out of their own pockets for work-related expenses, or on the other hand that the City was not paying for extensive personal communications.</p>
<p id="b274-10">As for the scope of the search, reviewing the transcripts was reasonable because it was an efficient and expedient way to determine whether Quon’s overages were the result of work-related messaging or personal use. The review was also not “ ‘excessively intrusive.’ ” <em>O’Connor, supra, </em>at 726, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (plurality opinion). Although Quon had gone over his monthly allotment a number of times, OPD requested transcripts for only the months of August and September 2002. While it may have been reasonable as well for OPD to review transcripts of all the months in which Quon exceeded his</p>
<p id="Amep">[<span class="citation no-link">560 U.S. 762</span>]</p>
<p id="b274-11">allowance, it was certainly reasonable for OPD to review messages for just two months in order to obtain a large enough sample to decide whether the character limits were efficacious. And it is worth noting that during his internal affairs investigation, McMahon redacted all messages Quon sent while off duty, a measure which reduced the intrusiveness of any further review of the transcripts.</p>
<p id="b275-3"><page-number citation-index="1" label="229">*229</page-number>Furthermore, and again on the assumption that Quon had a reasonable expectation of privacy in the contents of his messages,  the extent of an expectation is relevant to assessing whether the search was too intrusive. See <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#671" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>Von Raab, supra, </em>at 671</a></span>, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">109 S. Ct. 1384</a></span>, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">103 L. Ed. 2d 685</a></span>; cf. <em>Vernonia School Dist. 47J </em>v. <em>Acton, </em><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#654" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U.S. 646, 654-657</a></span>, <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">115 S. Ct. 2386</a></span>, <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">132 L. Ed. 2d 564</a></span> (1995). Even if he could assume some level of privacy would inhere in his messages, it would not have been reasonable for Quon to conclude that his messages were in all circumstances immune from scrutiny. Quon was told that his messages were subject to auditing. As a law enforcement officer, he would or should have known that his actions were likely to come under legal scrutiny, and that this might entail an analysis of his on-the-job communications. Under the circumstances, a reasonable employee would be aware that sound management principles might require the audit of messages to determine whether the pager was being appropriately used. Given that the City issued the pagers to Quon and other SWAT Team members in order to help them more quickly respond to crises— and given that Quon had received no assurances of privacy—Quon could have anticipated that it might be necessary for the City to audit pager messages to assess the SWAT Team’s performance in particular emergency situations.</p>
<p id="b275-4">From OPD’s perspective, the fact that Quon likely had only a limited privacy expectation, with boundaries that we need not here explore, lessened the risk that the review would intrude on highly private details of Quon’s life. OPD’s audit of messages on Quon’s employer-provided pager was not nearly as intrusive as a search of his personal e-mail account</p>
<p id="b275-5">[<span class="citation no-link">560 U.S. 763</span>]</p>
<p id="b275-6">or pager, or a wiretap on his home phone line, would have been. That the search did reveal intimate details of Quon’s life does not make it unreasonable, for under the circumstances a reasonable employer would not expect that such a review would intrude on such matters. The search was permissible in its scope.</p>
<p id="b275-7">The Court of Appeals erred in finding the search unreasonable. It pointed to a “host of simple ways to verify the efficacy of the 25,000 character limit . . . without intruding on [respondents’] Fourth Amendment rights.” <span class="citation" data-id="1455295"><a href="/opinion/1455295/quon-v-arch-wireless-operating-co-inc/#909" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc.">529 F.3d, at 909</a></span>. The panel suggested that Scharf “could have warned Quon that for the month of September he was forbidden from using his pager for personal communications, and that the contents of all of his messages would be reviewed to ensure the pager was used only for work-related purposes during that timeframe. Alternatively, if [OPD] wanted to review past usage, it could have asked Quon to count the characters himself, or asked him to redact personal messages and grant permission to [OPD] to review the redacted transcript.” <em><span class="citation" data-id="1455295"><a href="/opinion/1455295/quon-v-arch-wireless-operating-co-inc/" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc.">Ibid.</a></span></em></p>
<p id="b275-8">This approach was inconsistent with controlling precedents.  This Court has “repeatedly refused to declare that only the ‘least intrusive’ search practicable can be reasonable under the Fourth Amendment.” <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#663" aria-description="Citation for case: Vernonia School District 47J v. Acton"><em>Vernonia, supra, </em>at 663</a></span>, <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">115 S. Ct. 2386</a></span>, <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">132 L. Ed. 2d 564</a></span>; see also, <em>e.g., Board of Ed. of Independent School Dist. No. 92 of Pottawatomie Cty. </em>v. <em>Earls, </em><span class="citation" data-id="9434325"><a href="/opinion/121171/board-of-education-of-independent-school-district-no-92-of-pottawatomie/#837" aria-description="Citation for case: Board of Education of Independent School District No. 92...">536 U.S. 822, 837</a></span>, <span class="citation" data-id="9434325"><a href="/opinion/121171/board-of-education-of-independent-school-district-no-92-of-pottawatomie/" aria-description="Citation for case: Board of Education of Independent School District No. 92...">122 S. Ct. 2559</a></span>, <span class="citation" data-id="9434325"><a href="/opinion/121171/board-of-education-of-independent-school-district-no-92-of-pottawatomie/" aria-description="Citation for case: Board of Education of Independent School District No. 92...">153 L. Ed. 2d 735</a></span> (2002); <em>Illinois </em>v. <em>Lafayette, </em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/#647" aria-description="Citation for case: Illinois v. Lafayette">462 U.S. 640, 647</a></span>, <span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">103 S. Ct. 2605</a></span>, <span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">77 L. Ed. 2d 65</a></span> (1983). That rationale “could raise insuperable barriers to the exercise of virtually all search- <page-number citation-index="1" label="230">*230</page-number>and-seizure powers,” <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#557" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U.S. 543, 557, n. 12</a></span>, <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">96 S. Ct. 3074</a></span>, <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">49 L. Ed. 2d 1116</a></span> (1976), because “judges engaged in <em>post hoc </em>evaluations of government conduct can almost always imagine some alternative means by which the objectives of the government might have been accomplished,” <em>Skinner, </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#629" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U.S., at 629, n. 9</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">109 S. Ct. 1402</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">103 L. Ed. 2d 639</a></span> (internal quotation marks and brackets omitted). The analytic errors of the Court of Appeals in this case illustrate the necessity of</p>
<p id="ACI">[<span class="citation no-link">560 U.S. 764</span>]</p>
<p id="b276-4">this principle. Even assuming there were ways that OPD could have performed the search that would have been less intrusive, it does not follow that the search as conducted was unreasonable.</p>
<p id="b276-5">Respondents argue that the search was <em>per se </em>unreasonable in light of the Court of Appeals’ conclusion that Arch Wireless violated the SCA by giving the City the transcripts of Quon’s text messages. The merits of the SCA claim are not before us. But even if the Court of Appeals was correct to conclude that the SCA forbade Arch Wireless from turning over the transcripts, it does not follow that petitioners’ actions were unreasonable. Respondents point to no authority for the proposition that the existence of statutory protection renders a search <em>per se </em>unreasonable under the Fourth Amendment. And the precedents counsel otherwise. See <em>Virginia </em>v. <em>Moore, </em><span class="citation" data-id="9435233"><a href="/opinion/145814/virginia-v-moore/#168" aria-description="Citation for case: Virginia v. Moore">553 U.S. 164, 168</a></span>, <span class="citation" data-id="9435233"><a href="/opinion/145814/virginia-v-moore/" aria-description="Citation for case: Virginia v. Moore">128 S. Ct. 1598</a></span>, <span class="citation" data-id="9435233"><a href="/opinion/145814/virginia-v-moore/" aria-description="Citation for case: Virginia v. Moore">170 L. Ed. 2d 559</a></span> (2008) (search incident to an arrest that was illegal under state law was reasonable); <em>California </em>v. <em>Greenwood, </em><span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/#43" aria-description="Citation for case: California v. Greenwood">486 U.S. 35, 43</a></span>, <span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/" aria-description="Citation for case: California v. Greenwood">108 S. Ct. 1625</a></span>, <span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/" aria-description="Citation for case: California v. Greenwood">100 L. Ed. 2d 30</a></span> (1988) (rejecting argument that if state law forbade police search of individual’s garbage the search would violate the Fourth Amendment). Furthermore, respondents do not maintain that any OPD employee either violated the law him-self or herself or knew or should have known that Arch Wireless, by turning over the transcript, would have violated the law. The otherwise reasonable search by OPD is not rendered unreasonable by the assumption that Arch Wireless violated the SCA by turning over the transcripts.</p>
<p id="b276-7">Because the search was motivated by a legitimate work-related purpose, and because it was not excessive in scope, the search was reasonable under the approach of the <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span> </em>plurality. <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#726" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U.S., at 726</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>. For these same reasons—that the employer had a legitimate reason for the search, and that the search was not excessively intrusive in light of that justification—the Court also concludes that the search would be “regarded as reasonable and normal in the private-employer context” and would satisfy the approach of Justice</p>
<p id="A_p">[<span class="citation no-link">560 U.S. 765</span>]</p>
<p id="b276-8">Scalia’s concurrence. <em>Id., </em>at 732, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>. The search was reasonable, and the Court of Appeals erred by holding to the contrary. Petitioners did not violate Quon’s Fourth Amendment rights.</p>
<p id="b276-9">C</p>
<p id="b276-10">Finally, the Court must consider whether the search violated the Fourth Amendment rights of Jerilyn Quon, Florio, and Trujillo, the respondents who sent text messages to Jeff Quon. Petitioners and respondents disagree whether a sender of a text message can have a reasonable expectation of privacy in a message he knowingly sends to someone’s employer-provided pager. It is not necessary to resolve this question in order to dispose of the case, however. <page-number citation-index="1" label="231">*231</page-number>Respondents argue that because “the search was unreasonable as to Sergeant Quon, it was also unreasonable as to his correspondents.” Brief for Respondents 60 (some capitalization omitted; boldface deleted). They make no corollary argument that the search, if reasonable as to Quon, could nonetheless be unreasonable as to Quon’s correspondents. See <em>id., </em>at 65-66. In light of this litigating position and the Court’s conclusion that the search was reasonable as to Jeff Quon, it necessarily follows that these other respondents cannot prevail.</p>
<p id="pAiz">
<img class="p" height="29" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPgAAAAdAQAAAACvI5yXAAAAiUlEQVR4nM3SsQ0CMQwF0J8vRAsNPTABKzAVY8BGiHUQxXUXoYNPh618Kc1JCHfPju1ISRG6wX75F/Wa3YLAI6dazN//XFyCBmJcp+MO1dNK3zAQy+shWhzSTSlaENjn+xqkTW5pQbx22+gwENNxiJRDw3iOiYai973GTAPBKa00zH2/8v//uxsfCuKccmBnLFwAAAAASUVORK5CYII=" width="247"/>
</p>
<p id="b277-5">Because the search was reasonable, petitioners did not violate respondents’ Fourth Amendment rights, and the court below erred by concluding otherwise. The judgment of the Court of Appeals for the Ninth Circuit is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b277-6">It is so ordered.</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/City of Tahlequah v. Bond.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "City of Tahlequah v. Bond"
type: case
citation: "595 U.S. 9 (2021)"
parallel_cite: ""
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2021
date_decided: 2021-10-18
docket: 20-1668
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2021-10-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: City of Tahlequah v. Bond
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/5292018/city-of-tahlequah-v-bond/"
  cluster_id: 5292018
  opinion_id: 5120580
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[District of Columbia v. Wesby]]", "[[Graham v. Connor]]", "[[Harlow v. Fitzgerald]]", "[[Hope v. Pelzer]]"]
aliases: ["Tahlequah v. Bond"]
tags: ["case", "qualified-immunity", "section-1983", "excessive-force", "clearly-established-law", "per-curiam"]
holding: "Courts must not define clearly established law at too high a level of generality; QI protects 'all but the plainly incompetent or those who knowingly violate the law.'"
lake:
  record_id: City of Tahlequah v. Bond
  status: verified
  projected_at: 2026-07-06
---

# City of Tahlequah v. Bond

*595 U.S. 9 (2021)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers responded to a call that Dominic Rollice, intoxicated, would not leave his ex-wife's garage. As they spoke with him, Rollice grabbed a hammer and raised it as if to strike or throw it; two officers shot and killed him. His estate sued under § 1983 for excessive force. The Tenth Circuit denied [[Qualified Immunity|qualified immunity]], holding the officers' earlier "cornering" of Rollice was reckless and that circuit precedent clearly established the violation.

## Issue
Whether the officers were entitled to [[Qualified Immunity|qualified immunity]] because no precedent clearly established that their conduct violated the Fourth Amendment.

## Rule
Yes. Clearly established law must be defined with specificity: "We have repeatedly told courts not to define clearly established law at too high a level of generality." — *City of Tahlequah v. Bond*, 595 U.S. 9 (2021) (slip op., at 3). ^pin-op3

[[Qualified Immunity|Qualified immunity]] "protects '"all but the plainly incompetent or those who knowingly violate the law."'" — *Id.* (slip op., at 3) (quoting *District of Columbia v. Wesby*). ^pin-op3a

## Application
None of the decisions the Tenth Circuit invoked involved facts close enough to give these officers fair notice that confronting an armed, intoxicated man who raised a hammer would violate the Fourth Amendment. Because no precedent squarely governed the situation the officers faced, they did not violate clearly established law and were entitled to [[Qualified Immunity|qualified immunity]] on this record.

## Conclusion
The officers were entitled to [[Qualified Immunity|qualified immunity]]; the Tenth Circuit's contrary judgment was reversed. The Court did not decide whether a constitutional violation occurred.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Tahlequah* reaffirms the particularized "clearly established law" standard of [[District of Columbia v. Wesby]] and the objective qualified-immunity framework of [[Harlow v. Fitzgerald]], cautioning against the high-generality approach the "obvious case" exception of [[Hope v. Pelzer]] permits only rarely.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *City of Tahlequah v. Bond*, 595 U.S. 9 (2021) (per curiam) — https://www.courtlistener.com/opinion/5290448/city-of-tahlequah-v-bond/ — pinpoint: slip op., at 3 (CL carries the slip opinion; cluster 5290448 → opinion 5118994).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "995a3707d2c53783", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "City of Tahlequah v. Bond"}, "payload": {"all": [{"cite": "595 U.S. 9", "page": "9", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "595"}], "display": "595 U.S. 9", "official": {"cite": "595 U.S. 9", "page": "9", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "595"}, "official_selection_present": true, "record_id": "City of Tahlequah v. Bond"}}
{"assertion_id": "1884711c7ad5cae9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op3", "record_id": "City of Tahlequah v. Bond"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op3", "pinpoint_status": "slip-only", "quote": "of Rollice was reckless and that circuit precedent clearly established the violation. ## Issue Whether the officers were entitled to qualified immunity because no precedent clearly established that their conduct violated the Fourth Amendment. ## Rule Yes. Clearly established law must be defined with specificity:", "quote_fidelity": "mismatch", "record_id": "City of Tahlequah v. Bond", "star_marker": null}}
{"assertion_id": "529cf268b39f5c0d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op3a", "record_id": "City of Tahlequah v. Bond"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op3a", "pinpoint_status": "slip-only", "quote": "all but the plainly incompetent or those who knowingly violate the law.", "quote_fidelity": "mismatch", "record_id": "City of Tahlequah v. Bond", "star_marker": null}}
{"assertion_id": "81de6225172ff474", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "City of Tahlequah v. Bond"}, "payload": {"as_of_content": "2021-10-18", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "City of Tahlequah v. Bond", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — City of Tahlequah v. Bond

```json
{
  "schema_version": "s2.v1",
  "record_id": "City of Tahlequah v. Bond",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "City of Tahlequah v. Bond",
    "case_name_short": "Bond",
    "case_name_full": "",
    "input_case_name": "City of Tahlequah v. Bond",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2021-10-18",
    "year": 2021,
    "docket": "20-1668",
    "cluster_id": 5292018,
    "lead_opinion_id": 5120580,
    "sibling_ids": [
      5120580
    ],
    "absolute_url": "/opinion/5292018/city-of-tahlequah-v-bond/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 5290448,
        "score": 120,
        "case_name": "City of Tahlequah v. Bond"
      },
      {
        "cluster_id": 5292017,
        "score": 20,
        "case_name": "City of Tahlequah v. Bond"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "595 U.S. 9",
      "volume": "595",
      "reporter": "U.S.",
      "page": "9",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "595 U.S. 9",
        "volume": "595",
        "reporter": "U.S.",
        "page": "9",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "595 U.S. 9",
    "official_selection": {
      "court_class": "scotus",
      "selected": "595 U.S. 9",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op3",
      "page": null,
      "quote": "of Rollice was reckless and that circuit precedent clearly established the violation. ## Issue Whether the officers were entitled to qualified immunity because no precedent clearly established that their conduct violated the Fourth Amendment. ## Rule Yes. Clearly established law must be defined with specificity:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op3a",
      "page": null,
      "quote": "all but the plainly incompetent or those who knowingly violate the law.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2021-10-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "City of Tahlequah v. Bond",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(5120580) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
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
        "query": "cites:(5120580)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(5120580)",
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
    "complete_query": "cites:(5120580)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 5120580,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/city-of-tahlequah-v-bond.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 5120580,
        "cited_id": 145918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5120580,
        "cited_id": 169897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5120580,
        "cited_id": 744141,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5120580,
        "cited_id": 4638478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5120580,
        "cited_id": 9430379,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5120580,
        "cited_id": 9434715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5120580,
        "cited_id": 9820073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5120580,
        "cited_id": 9888205,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "C",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T00:29:11Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:29:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:29:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:30:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:29:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — City of Tahlequah v. Bond

```
                 Cite as: 595 U. S. ____ (2021)            1

                          Per Curiam

SUPREME COURT OF THE UNITED STATES
CITY OF TAHLEQUAH, OKLAHOMA, ET AL. v. AUSTIN
 P. BOND, AS SPECIAL ADMINISTRATOR OF THE ESTATE OF
          DOMINIC F. ROLLICE, DECEASED
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED
    STATES COURT OF APPEALS FOR THE TENTH CIRCUIT
             No. 20–1668. Decided October 18, 2021

   PER CURIAM.
   On August 12, 2016, Dominic Rollice’s ex-wife, Joy, called
911. Rollice was in her garage, she explained, and he was
intoxicated and would not leave. Joy requested police as-
sistance; otherwise, “it’s going to get ugly real quick.” 981
F. 3d 808, 812 (CA10 2020). The dispatcher asked whether
Rollice lived at the residence. Joy said he did not but ex-
plained that he kept tools in her garage.
   Officers Josh Girdner, Chase Reed, and Brandon Vick re-
sponded to the call. All three knew that Rollice was Joy’s
ex-husband, was intoxicated, and would not leave her
home.
   Joy met the officers out front and led them to the side
entrance of the garage. There the officers encountered Rol-
lice and began speaking with him in the doorway. Rollice
expressed concern that the officers intended to take him to
jail; Officer Girdner told him that they were simply trying
to get him a ride. Rollice began fidgeting with something
in his hands and the officers noticed that he appeared nerv-
ous. Officer Girdner asked if he could pat Rollice down for
weapons. Rollice refused.
   Police body-camera video captured what happened next.
As the conversation continued, Officer Girdner gestured
with his hands and took one step toward the doorway, caus-
ing Rollice to take one step back. Rollice, still conversing
with the officers, turned around and walked toward the
back of the garage where his tools were hanging over a
2               CITY OF TAHLEQUAH v. BOND

                          Per Curiam

workbench. Officer Girdner followed, the others close be-
hind. No officer was within six feet of Rollice. The video is
silent, but the officers stated that they ordered Rollice to
stop. Rollice kept walking. He then grabbed a hammer
from the back wall over the workbench and turned around
to face the officers. Rollice grasped the handle of the ham-
mer with both hands, as if preparing to swing a baseball
bat, and pulled it up to shoulder level. The officers backed
up, drawing their guns. At this point the video is no longer
silent, and the officers can be heard yelling at Rollice to
drop the hammer.
   He did not. Instead, Rollice took a few steps to his right,
coming out from behind a piece of furniture so that he had
an unobstructed path to Officer Girdner. He then raised
the hammer higher back behind his head and took a stance
as if he was about to throw the hammer or charge at the
officers. In response, Officers Girdner and Vick fired their
weapons, killing Rollice.
   Rollice’s estate filed suit against, among others, Officers
Girdner and Vick, alleging that the officers were liable un-
der 42 U. S. C. §1983, for violating Rollice’s Fourth Amend-
ment right to be free from excessive force. The officers
moved for summary judgment, both on the merits and on
qualified immunity grounds. The District Court granted
their motion. Burke v. Tahlequah, 2019 WL 4674316, *6
(ED Okla., Sept. 25, 2019). The officers’ use of force was
reasonable, it concluded, and even if not, qualified immun-
ity prevented the case from going further. Ibid.
   A panel of the Court of Appeals for the Tenth Circuit re-
versed. 981 F. 3d, at 826. The Court began by explaining
that Tenth Circuit precedent allows an officer to be held li-
able for a shooting that is itself objectively reasonable if the
officer’s reckless or deliberate conduct created a situation
requiring deadly force. Id., at 816. Applying that rule, the
Court concluded that a jury could find that Officer Girdner’s
                  Cite as: 595 U. S. ____ (2021)              3

                           Per Curiam

initial step toward Rollice and the officers’ subsequent “cor-
nering” of him in the back of the garage recklessly created
the situation that led to the fatal shooting, such that their
ultimate use of deadly force was unconstitutional. Id., at
823. As to qualified immunity, the Court concluded that
several cases, most notably Allen v. Muskogee, 119 F. 3d 837
(CA10 1997), clearly established that the officers’ conduct
was unlawful. 981 F. 3d, at 826. This petition followed.
   We need not, and do not, decide whether the officers vio-
lated the Fourth Amendment in the first place, or whether
recklessly creating a situation that requires deadly force
can itself violate the Fourth Amendment. On this record,
the officers plainly did not violate any clearly established
law.
   The doctrine of qualified immunity shields officers from
civil liability so long as their conduct “does not violate
clearly established statutory or constitutional rights of
which a reasonable person would have known.” Pearson v.
Callahan, 555 U. S. 223, 231 (2009). As we have explained,
qualified immunity protects “ ‘all but the plainly incompe-
tent or those who knowingly violate the law.’ ” District of
Columbia v. Wesby, 583 U. S. ___, ___ –___ (2018) (slip op.,
at 13–14) (quoting Malley v. Briggs, 475 U. S. 335, 341
(1986)).
   We have repeatedly told courts not to define clearly es-
tablished law at too high a level of generality. See, e.g.,
Ashcroft v. al-Kidd, 563 U. S. 731, 742 (2011). It is not
enough that a rule be suggested by then-existing precedent;
the “rule’s contours must be so well defined that it is ‘clear
to a reasonable officer that his conduct was unlawful in the
situation he confronted.’ ” Wesby, 583 U. S., at ___ (slip op.,
at 14) (quoting Saucier v. Katz, 533 U. S. 194, 202 (2001)).
Such specificity is “especially important in the Fourth
Amendment context,” where it is “sometimes difficult for an
officer to determine how the relevant legal doctrine, here
excessive force, will apply to the factual situation the officer
4               CITY OF TAHLEQUAH v. BOND

                         Per Curiam

confronts.” Mullenix v. Luna, 577 U. S. 7, 12 (2015) (per
curiam) (internal quotation marks omitted).
   The Tenth Circuit contravened those settled principles
here. Not one of the decisions relied upon by the Court of
Appeals—Estate of Ceballos v. Husk, 919 F. 3d 1204 (CA10
2019), Hastings v. Barnes, 252 Fed. Appx. 197 (CA10 2007),
Allen, 119 F. 3d 837, and Sevier v. Lawrence, 60 F. 3d 695
(CA10 1995)—comes close to establishing that the officers’
conduct was unlawful. The Court relied most heavily on
Allen. But the facts of Allen are dramatically different from
the facts here. The officers in Allen responded to a potential
suicide call by sprinting toward a parked car, screaming at
the suspect, and attempting to physically wrest a gun from
his hands. 119 F. 3d, at 841. Officers Girdner and Vick, by
contrast, engaged in a conversation with Rollice, followed
him into a garage at a distance of 6 to 10 feet, and did not
yell until after he picked up a hammer. We cannot conclude
that Allen “clearly established” that their conduct was reck-
less or that their ultimate use of force was unlawful.
   The other decisions relied upon by the Court of Appeals
are even less relevant. As for Sevier, that decision merely
noted in dicta that deliberate or reckless preseizure conduct
can render a later use of force excessive before dismissing
the appeal for lack of jurisdiction. See 60 F. 3d, at 700–701.
To state the obvious, a decision where the court did not even
have jurisdiction cannot clearly establish substantive con-
stitutional law. Regardless, that formulation of the rule is
much too general to bear on whether the officers’ particular
conduct here violated the Fourth Amendment. See al-Kidd,
563 U. S., at 742. Estate of Ceballos, decided after the
shooting at issue, is of no use in the clearly established in-
quiry. See Brosseau v. Haugen, 543 U. S. 194, 200, n. 4
(2004) (per curiam). And Hastings, an unpublished deci-
sion, involved officers initiating an encounter with a poten-
tially suicidal individual by chasing him into his bedroom,
screaming at him, and pepper-spraying him. 252 Fed.
                  Cite as: 595 U. S. ____ (2021)              5

                           Per Curiam

Appx., at 206. Suffice it to say, a reasonable officer could
miss the connection between that case and this one.
   Neither the panel majority nor the respondent has iden-
tified a single precedent finding a Fourth Amendment vio-
lation under similar circumstances. The officers were thus
entitled to qualified immunity.
   The petition for certiorari and the motions for leave to file
briefs amici curiae are granted, and the judgment of the
Court of Appeals is reversed.
                                              It is so ordered.

```

---

## GROUP: _overhaul2/lake/cases/Collins v. Virginia.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Collins v. Virginia"
type: case
citation: "584 U.S. 586 (2018)"
parallel_cite: "138 S. Ct. 1663; 201 L. Ed. 2d 9"
neutral_cite: 2018 U.S. LEXIS 3210
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2018
date_decided: 2018-05-29
docket: 16-1027
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2018-05-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Collins v. Virginia
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4501697/collins-v-virginia/"
  cluster_id: 4501697
  opinion_id: 4278950
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[Carroll v. United States]]", "[[California v. Carney]]", "[[Florida v. Jardines]]", "[[Coolidge v. New Hampshire]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "curtilage", "home", "warrantless-search"]
holding: "The automobile exception does NOT authorize a warrantless entry of a home or its curtilage to search a vehicle parked there. The…"
lake:
  record_id: Collins v. Virginia
  status: verified
  projected_at: 2026-07-06
---

# Collins v. Virginia

*584 U.S. 586 (2018)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An officer investigating a distinctive orange-and-black motorcycle suspected of eluding police walked up the driveway of Collins's house to a parking patio partly enclosed by the home, pulled back a tarp covering the motorcycle, ran the plates, and confirmed it was stolen — all without a warrant. Collins moved to suppress, and the Virginia Supreme Court upheld the search under the automobile exception.

## Issue
Whether the automobile exception permits an officer, without a warrant, to enter the [[Curtilage|curtilage]] of a home to search a vehicle parked there.

## Rule
No. "For the foregoing reasons, we conclude that the automobile exception does not permit an officer without a warrant to enter a home or its curtilage in order to search a vehicle therein." — *Collins v. Virginia*, 584 U.S. 586 (2018) (slip op., at 14). ^pin-op14

The automobile exception is a warrant exception for the vehicle; it does not independently justify the separate trespass of entering constitutionally protected [[Curtilage|curtilage]] to reach the vehicle.

## Application
The motorcycle was parked on the [[Curtilage|curtilage]] — a partly enclosed section of the driveway adjacent to and intimately tied to the home. The officer physically entered that [[Curtilage|curtilage]] and pulled off the tarp to search the motorcycle without a warrant. Because the automobile exception did not authorize entering the [[Curtilage|curtilage]], the warrantless intrusion was unlawful on these facts; whether it might be justified on another ground, such as [[Exigent Circumstances and Hot Pursuit|exigency]], was left for remand.

## Conclusion
The automobile exception did not authorize the warrantless [[Curtilage|curtilage]] entry; the judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Collins* bounds the [[Carroll v. United States]] / [[California v. Carney]] automobile exception at the home's [[Curtilage|curtilage]], applying the [[Curtilage|curtilage]] protection recognized in [[Florida v. Jardines]].

## Appears on
- [[Automobile Exception]] — *Key — Progeny / Refinement*

## Sources
- *Collins v. Virginia*, 584 U.S. 586 (2018) — https://www.courtlistener.com/opinion/4501697/collins-v-virginia/ — pinpoint: slip op., at 14 (CL carries the slip opinion; cluster 4501697 → opinion 4278950).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fb612d0b4dfc9c02", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Collins v. Virginia"}, "payload": {"all": [{"cite": "584 U.S. 586", "page": "586", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "584"}, {"cite": "138 S. Ct. 1663", "page": "1663", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "138"}, {"cite": "201 L. Ed. 2d 9", "page": "9", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "201"}, {"cite": "2018 U.S. LEXIS 3210", "page": "3210", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2018"}], "display": "584 U.S. 586", "official": {"cite": "584 U.S. 586", "page": "586", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "584"}, "official_selection_present": true, "record_id": "Collins v. Virginia"}}
{"assertion_id": "72aa445bd21761b7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op14", "record_id": "Collins v. Virginia"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op14", "pinpoint_status": "slip-only", "quote": "--- # Collins v. Virginia *584 U.S. 586 (2018)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An officer investigating a distinctive orange-and-black motorcycle suspected of eluding police walked up the driveway of Collins's house to a parking patio partly enclosed by the home, pulled back a tarp covering the motorcycle, ran the plates, and confirmed it was stolen — all without a warrant. Collins moved to suppress, and the Virginia Supreme Court upheld the search under the automobile exception. ## Issue Whether the automobile exception permits an officer, without a warrant, to enter the curtilage of a home to search a vehicle parked there. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Collins v. Virginia", "star_marker": null}}
{"assertion_id": "c353f017a0026bd3", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Collins v. Virginia"}, "payload": {"as_of_content": "2018-05-29", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Collins v. Virginia", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Collins v. Virginia

```json
{
  "schema_version": "s2.v1",
  "record_id": "Collins v. Virginia",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Collins v. Virginia",
    "case_name_short": "Collins",
    "case_name_full": "",
    "input_case_name": "Collins v. Virginia",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2018-05-29",
    "year": 2018,
    "docket": "16-1027",
    "cluster_id": 4501697,
    "lead_opinion_id": 4278950,
    "sibling_ids": [
      4278950
    ],
    "absolute_url": "/opinion/4501697/collins-v-virginia/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "584 U.S. 586",
      "volume": "584",
      "reporter": "U.S.",
      "page": "586",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "138 S. Ct. 1663",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "1663",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "201 L. Ed. 2d 9",
        "volume": "201",
        "reporter": "L. Ed. 2d",
        "page": "9",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2018 U.S. LEXIS 3210",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "3210",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "584 U.S. 586",
        "volume": "584",
        "reporter": "U.S.",
        "page": "586",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "138 S. Ct. 1663",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "1663",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "201 L. Ed. 2d 9",
        "volume": "201",
        "reporter": "L. Ed. 2d",
        "page": "9",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2018 U.S. LEXIS 3210",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "3210",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "584 U.S. 586",
    "official_selection": {
      "court_class": "scotus",
      "selected": "584 U.S. 586",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op14",
      "page": null,
      "quote": "--- # Collins v. Virginia *584 U.S. 586 (2018)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An officer investigating a distinctive orange-and-black motorcycle suspected of eluding police walked up the driveway of Collins's house to a parking patio partly enclosed by the home, pulled back a tarp covering the motorcycle, ran the plates, and confirmed it was stolen \u2014 all without a warrant. Collins moved to suppress, and the Virginia Supreme Court upheld the search under the automobile exception. ## Issue Whether the automobile exception permits an officer, without a warrant, to enter the curtilage of a home to search a vehicle parked there. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2018-05-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Collins v. Virginia",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "LaCour v. Marshalls of California",
          "cluster_id": 10765564,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Wittey",
          "cluster_id": 9404034,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Chesney",
          "cluster_id": 4536724,
          "cite": [
            "196 A.3d 253"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Garza v. Idaho",
          "cluster_id": 4594419,
          "cite": [
            "586 U.S. 232",
            "139 S. Ct. 738",
            "203 L. Ed. 2d 77",
            "2019 U.S. LEXIS 1596"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Caldwell",
          "cluster_id": 4904976,
          "cite": [
            "7 F.4th 191"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
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
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Alexis",
          "cluster_id": 4573870,
          "cite": [
            "112 N.E.3d 796",
            "481 Mass. 91"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Soukaneh v. Andrzejewski",
          "cluster_id": 10038252,
          "cite": [
            "112 F.4th 107"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lewis",
          "cluster_id": 9385343,
          "cite": [
            "62 F.4th 733"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raheim Trice",
          "cluster_id": 4769607,
          "cite": [
            "966 F.3d 506"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alexander v. City of Syracuse",
          "cluster_id": 10356512,
          "cite": [
            "132 F.4th 129"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Suggs",
          "cluster_id": 4888422,
          "cite": [
            "998 F.3d 1125"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lewis v. State",
          "cluster_id": 10020965,
          "cite": [
            "233 A.3d 86",
            "470 Md. 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Long",
          "cluster_id": 4775413,
          "cite": [
            "157 N.E.3d 362",
            "2020 Ohio 4090"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Maxim",
          "cluster_id": 4683972,
          "cite": [
            "454 P.3d 543",
            "165 Idaho 901"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Noli",
          "cluster_id": 9399584,
          "cite": [
            "412 Mont. 170",
            "529 P.3d 813",
            "2023 MT 84"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 7852694,
          "cite": [
            "43 F.4th 94"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. James",
          "cluster_id": 4869243,
          "cite": [
            "2021 IL App (1st) 180509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lamar Clancy",
          "cluster_id": 4805551,
          "cite": [
            "979 F.3d 1135"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Bruce Akers",
          "cluster_id": 5093384,
          "cite": [
            "259 A.3d 127",
            "2021 ME 43"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
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
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hernandez-Mieses",
          "cluster_id": 4644586,
          "cite": [
            "931 F.3d 134"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dylan Ostrum",
          "cluster_id": 9496998,
          "cite": [
            "99 F.4th 999"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 8439952,
          "cite": [
            "893 F.3d 66"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Prentiss Jackson",
          "cluster_id": 9510705,
          "cite": [
            "103 F.4th 483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Wright",
          "cluster_id": 9500300,
          "cite": [
            "243 N.E.3d 782",
            "2024 Ohio 1763"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Simpkins",
          "cluster_id": 4796830,
          "cite": [
            "978 F.3d 1"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4278950) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 111,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 111,
        "triage_read": 3,
        "triage_snippet_classified": 108
      },
      "lane2_top_cited": {
        "query": "cites:(4278950)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00JnM9Nzg2MjEzMiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%284278950%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4278950)",
        "reviewed": 48,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 48,
        "triage_read": 1,
        "triage_snippet_classified": 47
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4278950)",
    "indexed_citing_opinions": 142,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4278950,
        "count": 142,
        "count_source": "search"
      }
    ],
    "citation_count": 349,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/collins-v-virginia.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MzU0MyZzPTEwMDM4MjUyJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%284278950%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4278950,
        "cited_id": 85412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 87010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 103012,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 103013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 103100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 103794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 105511,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 106628,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 106775,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 107875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 110484,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 110645,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 111263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 111833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 112416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 112448,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 112795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 117905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 118063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 118235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 118277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 118363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 145646,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 145887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 145902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 145922,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 216733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 218926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 354014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 622304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 1501475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 2089408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 2621047,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 3580565,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "C",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T00:30:26Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:30:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:30:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:34:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:30:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Collins v. Virginia

```
(Slip Opinion)              OCTOBER TERM, 2017                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                          COLLINS v. VIRGINIA

        CERTIORARI TO THE SUPREME COURT OF VIRGINIA

     No. 16–1027. Argued January 9, 2018—Decided May 29, 2018
During the investigation of two traffic incidents involving an orange
 and black motorcycle with an extended frame, Officer David Rhodes
 learned that the motorcycle likely was stolen and in the possession of
 petitioner Ryan Collins. Officer Rhodes discovered photographs on
 Collins’ Facebook profile of an orange and black motorcycle parked in
 the driveway of a house, drove to the house, and parked on the street.
 From there, he could see what appeared to be the motorcycle under a
 white tarp parked in the same location as the motorcycle in the pho-
 tograph. Without a search warrant, Office Rhodes walked to the top
 of the driveway, removed the tarp, confirmed that the motorcycle was
 stolen by running the license plate and vehicle identification num-
 bers, took a photograph of the uncovered motorcycle, replaced the
 tarp, and returned to his car to wait for Collins. When Collins re-
 turned, Officer Rhodes arrested him. The trial court denied Collins’
 motion to suppress the evidence on the ground that Officer Rhodes
 violated the Fourth Amendment when he trespassed on the house’s
 curtilage to conduct a search, and Collins was convicted of receiving
 stolen property. The Virginia Court of Appeals affirmed. The State
 Supreme Court also affirmed, holding that the warrantless search
 was justified under the Fourth Amendment’s automobile exception.
Held: The automobile exception does not permit the warrantless entry
 of a home or its curtilage in order to search a vehicle therein. Pp. 3–
 14.
    (a) This case arises at the intersection of two components of the
 Court’s Fourth Amendment jurisprudence: the automobile exception
 to the warrant requirement and the protection extended to the curti-
 lage of a home. In announcing each of the automobile exception’s jus-
 tifications—i.e., the “ready mobility of the automobile” and “the per-
 vasive regulation of vehicles capable of traveling on the public
2                          COLLINS v. VIRGINIA

                                   Syllabus

    highways,” California v. Carney, 471 U. S. 386, 390, 392—the Court
    emphasized that the rationales applied only to automobiles and not
    to houses, and therefore supported their different treatment as a con-
    stitutional matter. When these justifications are present, officers
    may search an automobile without a warrant so long as they have
    probable cause. Curtilage—“the area ‘immediately surrounding and
    associated with the home’ ”—is considered “ ‘part of the home itself for
    Fourth Amendment purposes.’ ” Florida v. Jardines, 569 U. S. 1, 6.
    Thus, when an officer physically intrudes on the curtilage to gather
    evidence, a Fourth Amendment search has occurred and is presump-
    tively unreasonable absent a warrant. Pp. 3–6.
        (b) As an initial matter, the part of the driveway where Collins’ mo-
    torcycle was parked and subsequently searched is curtilage. When
    Officer Rhodes searched the motorcycle, it was parked inside a par-
    tially enclosed top portion of the driveway that abuts the house. Just
    like the front porch, side garden, or area “outside the front window,”
    that enclosure constitutes “an area adjacent to the home and ‘to
    which the activity of home life extends.’ ” Jardines, 569 U. S., at 6, 7.
        Because the scope of the automobile exception extends no further
    than the automobile itself, it did not justify Officer Rhodes’ invasion
    of the curtilage. Nothing in this Court’s case law suggests that the
    automobile exception gives an officer the right to enter a home or its
    curtilage to access a vehicle without a warrant. Such an expansion
    would both undervalue the core Fourth Amendment protection af-
    forded to the home and its curtilage and “ ‘untether’ ” the exception
    “ ‘from the justifications underlying’ ” it. Riley v. California, 573 U. S.
    ___, ___. This Court has similarly declined to expand the scope of
    other exceptions to the warrant requirement. Thus, just as an officer
    must have a lawful right of access to any contraband he discovers in
    plain view in order to seize it without a warrant—see Horton v. Cali-
    fornia, 496 U. S. 128, 136–137—and just as an officer must have a
    lawful right of access in order to arrest a person in his home—see
    Payton v. New York, 445 U. S. 573, 587–590—so, too, an officer must
    have a lawful right of access to a vehicle in order to search it pursu-
    ant to the automobile exception. To allow otherwise would unmoor
    the exception from its justifications, render hollow the core Fourth
    Amendment protection the Constitution extends to the house and its
    curtilage, and transform what was meant to be an exception into a
    tool with far broader application. Pp. 6–11.
        (c) Contrary to Virginia’s claim, the automobile exception is not a
    categorical one that permits the warrantless search of a vehicle any-
    time, anywhere, including in a home or curtilage. Scher v. United
    States, 305 U. S. 251; Pennsylvania v. Labron, 518 U. S. 938, distin-
    guished. Also unpersuasive is Virginia’s proposed bright line rule for
                      Cite as: 584 U. S. ____ (2018)                       3

                                 Syllabus

  an automobile exception that would not permit warrantless entry
  only of the house itself or another fixed structure, e.g., a garage, inside
  the curtilage. This Court has long been clear that curtilage is afford-
  ed constitutional protection, and creating a carveout for certain types
  of curtilage seems more likely to create confusion than does uniform
  application of the Court’s doctrine. Virginia’s rule also rests on a
  mistaken premise, for the ability to observe inside curtilage from a
  lawful vantage point is not the same as the right to enter curtilage
  without a warrant to search for information not otherwise accessible.
  Finally, Virginia’s rule automatically would grant constitutional
  rights to those persons with the financial means to afford residences
  with garages but deprive those persons without such resources of any
  individualized consideration as to whether the areas in which they
  store their vehicles qualify as curtilage. Pp. 11–14.
292 Va. 486, 790 S. E. 2d 611, reversed and remanded.

  SOTOMAYOR, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and KENNEDY, THOMAS, GINSBURG, BREYER, KAGAN, and GORSUCH,
JJ., joined. THOMAS, J., filed a concurring opinion. ALITO, J., filed a
dissenting opinion.
                        Cite as: 584 U. S. ____ (2018)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 16–1027
                                   _________________


 RYAN AUSTIN COLLINS, PETITIONER v. VIRGINIA
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF 

                       VIRGINIA

                                 [May 29, 2018] 


  JUSTICE SOTOMAYOR delivered the opinion of the Court.
  This case presents the question whether the automobile
exception to the Fourth Amendment permits a police
officer, uninvited and without a warrant, to enter the
curtilage of a home in order to search a vehicle parked
therein. It does not.
                             I
   Officer Matthew McCall of the Albemarle County Police
Department in Virginia saw the driver of an orange and
black motorcycle with an extended frame commit a traffic
infraction. The driver eluded Officer McCall’s attempt to
stop the motorcycle. A few weeks later, Officer David
Rhodes of the same department saw an orange and black
motorcycle traveling well over the speed limit, but the
driver got away from him, too. The officers compared
notes and concluded that the two incidents involved the
same motorcyclist.
   Upon further investigation, the officers learned that the
motorcycle likely was stolen and in the possession of peti-
tioner Ryan Collins. After discovering photographs on
Collins’ Facebook profile that featured an orange and
black motorcycle parked at the top of the driveway of a
2                    COLLINS v. VIRGINIA

                      Opinion of the Court

house, Officer Rhodes tracked down the address of the
house, drove there, and parked on the street. It was later
established that Collins’ girlfriend lived in the house and
that Collins stayed there a few nights per week.1
  From his parked position on the street, Officer Rhodes
saw what appeared to be a motorcycle with an extended
frame covered with a white tarp, parked at the same angle
and in the same location on the driveway as in the Face-
book photograph. Officer Rhodes, who did not have a
warrant, exited his car and walked toward the house. He
stopped to take a photograph of the covered motorcycle
from the sidewalk, and then walked onto the residential
property and up to the top of the driveway to where the
motorcycle was parked. In order “to investigate further,”
App. 80, Officer Rhodes pulled off the tarp, revealing a
motorcycle that looked like the one from the speeding
incident. He then ran a search of the license plate and
vehicle identification numbers, which confirmed that the
motorcycle was stolen. After gathering this information,
Officer Rhodes took a photograph of the uncovered motor-
cycle, put the tarp back on, left the property, and returned
to his car to wait for Collins.
  Shortly thereafter, Collins returned home.          Officer
Rhodes walked up to the front door of the house and
knocked. Collins answered, agreed to speak with Officer
Rhodes, and admitted that the motorcycle was his and
that he had bought it without title. Officer Rhodes then
arrested Collins.
  Collins was indicted by a Virginia grand jury for receiv-
ing stolen property. He filed a pretrial motion to suppress
the evidence that Officer Rhodes had obtained as a result
of the warrantless search of the motorcycle. Collins ar-
gued that Officer Rhodes had trespassed on the curtilage
——————
  1 Virginia does not dispute that Collins has Fourth Amendment

standing. See Minnesota v. Olson, 495 U. S. 91, 96–100 (1990).
                  Cite as: 584 U. S. ____ (2018)             3

                      Opinion of the Court

of the house to conduct an investigation in violation of the
Fourth Amendment. The trial court denied the motion
and Collins was convicted.
   The Court of Appeals of Virginia affirmed. It assumed
that the motorcycle was parked in the curtilage of the
home and held that Officer Rhodes had probable cause to
believe that the motorcycle under the tarp was the same
motorcycle that had evaded him in the past. It further
concluded that Officer Rhodes’ actions were lawful under
the Fourth Amendment even absent a warrant because
“numerous exigencies justified both his entry onto the
property and his moving the tarp to view the motorcycle
and record its identification number.” 65 Va. App. 37, 46,
773 S. E. 2d 618, 623 (2015).
   The Supreme Court of Virginia affirmed on different
reasoning. It explained that the case was most properly
resolved with reference to the Fourth Amendment’s auto-
mobile exception. 292 Va. 486, 496–501, 790 S. E. 2d 611,
616–618 (2016). Under that framework, it held that
Officer Rhodes had probable cause to believe that the
motorcycle was contraband, and that the warrantless
search therefore was justified. Id., at 498–499, 790 S. E. 2d,
at 617.
   We granted certiorari, 582 U. S. ___ (2017), and now
reverse.
                               II
  The Fourth Amendment provides in relevant part that
the “right of the people to be secure in their persons, houses,
papers, and effects, against unreasonable searches and
seizures, shall not be violated.” This case arises at the
intersection of two components of the Court’s Fourth
Amendment jurisprudence: the automobile exception to
the warrant requirement and the protection extended to
the curtilage of a home.
4                   COLLINS v. VIRGINIA

                      Opinion of the Court

                              A
                              1
   The Court has held that the search of an automobile can
be reasonable without a warrant. The Court first articu-
lated the so-called automobile exception in Carroll v.
United States, 267 U. S. 132 (1925). In that case, law
enforcement officers had probable cause to believe that a
car they observed traveling on the road contained illegal
liquor. They stopped and searched the car, discovered and
seized the illegal liquor, and arrested the occupants. Id.,
at 134–136. The Court upheld the warrantless search and
seizure, explaining that a “necessary difference” exists
between searching “a store, dwelling house or other struc-
ture” and searching “a ship, motor boat, wagon or automo-
bile” because a “vehicle can be quickly moved out of the
locality or jurisdiction in which the warrant must be
sought.” Id., at 153.
   The “ready mobility” of vehicles served as the core justi-
fication for the automobile exception for many years.
California v. Carney, 471 U. S. 386, 390 (1985) (citing, e.g.,
Cooper v. California, 386 U. S. 58, 59 (1967); Chambers v.
Maroney, 399 U. S. 42, 51–52 (1970)). Later cases then
introduced an additional rationale based on “the pervasive
regulation of vehicles capable of traveling on the public
highways.” Carney, 471 U. S., at 392. As the Court ex-
plained in South Dakota v. Opperman, 428 U. S. 364
(1976):
    “Automobiles, unlike homes, are subjected to perva-
    sive and continuing governmental regulation and con-
    trols, including periodic inspection and licensing re-
    quirements. As an everyday occurrence, police stop
    and examine vehicles when license plates or inspec-
    tion stickers have expired, or if other violations, such
    as exhaust fumes or excessive noise, are noted, or if
    headlights or other safety equipment are not in proper
                  Cite as: 584 U. S. ____ (2018)            5

                      Opinion of the Court

    working order.” Id., at 368.
  In announcing each of these two justifications, the Court
took care to emphasize that the rationales applied only to
automobiles and not to houses, and therefore supported
“treating automobiles differently from houses” as a consti-
tutional matter. Cady v. Dombrowski, 413 U. S. 433, 441
(1973).
  When these justifications for the automobile exception
“come into play,” officers may search an automobile with-
out having obtained a warrant so long as they have proba-
ble cause to do so. Carney, 471 U. S., at 392–393.
                               2
   Like the automobile exception, the Fourth Amendment’s
protection of curtilage has long been black letter law.
“[W]hen it comes to the Fourth Amendment, the home is
first among equals.” Florida v. Jardines, 569 U. S. 1, 6
(2013). “At the Amendment’s ‘very core’ stands ‘the right
of a man to retreat into his own home and there be free
from unreasonable governmental intrusion.’ ” Ibid. (quot-
ing Silverman v. United States, 365 U. S. 505, 511 (1961)).
To give full practical effect to that right, the Court consid-
ers curtilage—“the area ‘immediately surrounding and
associated with the home’ ”—to be “ ‘part of the home itself
for Fourth Amendment purposes.’ ” Jardines, 569 U. S., at
6 (quoting Oliver v. United States, 466 U. S. 170, 180
(1984)). “The protection afforded the curtilage is essentially
a protection of families and personal privacy in an area
intimately linked to the home, both physically and psycho-
logically, where privacy expectations are most height-
ened.” California v. Ciraolo, 476 U. S. 207, 212–213
(1986).
   When a law enforcement officer physically intrudes on
the curtilage to gather evidence, a search within the mean-
ing of the Fourth Amendment has occurred. Jardines, 569
U. S., at 11. Such conduct thus is presumptively unrea-
6                    COLLINS v. VIRGINIA

                      Opinion of the Court

sonable absent a warrant.
                              B
                              1
   With this background in mind, we turn to the applica-
tion of these doctrines in the instant case. As an initial
matter, we decide whether the part of the driveway where
Collins’ motorcycle was parked and subsequently searched
is curtilage.
   According to photographs in the record, the driveway
runs alongside the front lawn and up a few yards past the
front perimeter of the house. The top portion of the
driveway that sits behind the front perimeter of the house
is enclosed on two sides by a brick wall about the height of
a car and on a third side by the house. A side door pro-
vides direct access between this partially enclosed section
of the driveway and the house. A visitor endeavoring to
reach the front door of the house would have to walk
partway up the driveway, but would turn off before enter-
ing the enclosure and instead proceed up a set of steps
leading to the front porch. When Officer Rhodes searched
the motorcycle, it was parked inside this partially enclosed
top portion of the driveway that abuts the house.
   The “ ‘conception defining the curtilage’ is . . . familiar
enough that it is ‘easily understood from our daily experi-
ence.’ ” Jardines, 569 U. S., at 7 (quoting Oliver, 466 U. S.,
at 182, n. 12). Just like the front porch, side garden, or
area “outside the front window,” Jardines, 569 U. S., at 6,
the driveway enclosure where Officer Rhodes searched the
motorcycle constitutes “an area adjacent to the home and
‘to which the activity of home life extends,’ ” and so is
properly considered curtilage, id., at 7 (quoting Oliver, 466
U. S., at 182, n. 12).
                              2
    In physically intruding on the curtilage of Collins’ home
                    Cite as: 584 U. S. ____ (2018)                  7

                        Opinion of the Court

to search the motorcycle, Officer Rhodes not only invaded
Collins’ Fourth Amendment interest in the item searched,
i.e., the motorcycle, but also invaded Collins’ Fourth
Amendment interest in the curtilage of his home. The
question before the Court is whether the automobile ex-
ception justifies the invasion of the curtilage.2 The answer
is no.
   Applying the relevant legal principles to a slightly dif-
ferent factual scenario confirms that this is an easy case.
Imagine a motorcycle parked inside the living room of a
house, visible through a window to a passerby on the
street. Imagine further that an officer has probable cause
to believe that the motorcycle was involved in a traffic
infraction. Can the officer, acting without a warrant,
enter the house to search the motorcycle and confirm
whether it is the right one? Surely not.
   The reason is that the scope of the automobile exception
extends no further than the automobile itself. See, e.g.,
Pennsylvania v. Labron, 518 U. S. 938, 940 (1996) (per
curiam) (explaining that the automobile exception “per-
mits police to search the vehicle”); Wyoming v. Houghton,
526 U. S. 295, 300 (1999) (“[T]he Framers would have
regarded as reasonable (if there was probable cause) the
warrantless search of containers within an automobile”).
Virginia asks the Court to expand the scope of the auto-
mobile exception to permit police to invade any space
outside an automobile even if the Fourth Amendment
protects that space. Nothing in our case law, however,
suggests that the automobile exception gives an officer the
right to enter a home or its curtilage to access a vehicle
——————
  2 Helpfully, the parties have simplified matters somewhat by each

making a concession. Petitioner concedes “for purposes of this appeal”
that Officer Rhodes had probable cause to believe that the motorcycle
was the one that had eluded him, Brief for Petitioner 5, n. 3, and
Virginia concedes that “Officer Rhodes searched the motorcycle,” Brief
for Respondent 12.
8                    COLLINS v. VIRGINIA

                      Opinion of the Court

without a warrant. Expanding the scope of the automobile
exception in this way would both undervalue the core
Fourth Amendment protection afforded to the home and
its curtilage and “ ‘untether’ ” the automobile exception
“ ‘from the justifications underlying’ ” it. Riley v. Califor-
nia, 573 U. S. ___, ___ (2014) (slip op., at 10) (quoting
Arizona v. Gant, 556 U. S. 332, 343 (2009)).
    The Court already has declined to expand the scope of
other exceptions to the warrant requirement to permit
warrantless entry into the home. The reasoning behind
those decisions applies equally well in this context. For
instance, under the plain-view doctrine, “any valid war-
rantless seizure of incriminating evidence” requires that
the officer “have a lawful right of access to the object
itself.” Horton v. California, 496 U. S. 128, 136–137
(1990); see also id., at 137, n. 7 (“ ‘[E]ven where the object
is contraband, this Court has repeatedly stated and en-
forced the basic rule that the police may not enter and
make a warrantless seizure’ ”); G. M. Leasing Corp. v.
United States, 429 U. S. 338, 354 (1977) (“It is one thing to
seize without a warrant property resting in an open area
. . . , and it is quite another thing to effect a warrantless
seizure of property . . . situated on private premises to
which access is not otherwise available for the seizing
officer”). A plain-view seizure thus cannot be justified if it
is effectuated “by unlawful trespass.” Soldal v. Cook
County, 506 U. S. 56, 66 (1992). Had Officer Rhodes seen
illegal drugs through the window of Collins’ house, for
example, assuming no other warrant exception applied, he
could not have entered the house to seize them without
first obtaining a warrant.
    Similarly, it is a “settled rule that warrantless arrests in
public places are valid,” but, absent another exception
such as exigent circumstances, officers may not enter a
home to make an arrest without a warrant, even when
they have probable cause. Payton v. New York, 445 U. S.
                 Cite as: 584 U. S. ____ (2018)            9

                     Opinion of the Court

573, 587–590 (1980). That is because being “ ‘arrested in
the home involves not only the invasion attendant to all
arrests but also an invasion of the sanctity of the home.’ ”
Id., at 588–589 (quoting United States v. Reed, 572 F. 2d
412, 423 (CA2 1978)). Likewise, searching a vehicle
parked in the curtilage involves not only the invasion of
the Fourth Amendment interest in the vehicle but also an
invasion of the sanctity of the curtilage.
   Just as an officer must have a lawful right of access to
any contraband he discovers in plain view in order to seize
it without a warrant, and just as an officer must have a
lawful right of access in order to arrest a person in his
home, so, too, an officer must have a lawful right of access
to a vehicle in order to search it pursuant to the automo-
bile exception. The automobile exception does not afford
the necessary lawful right of access to search a vehicle
parked within a home or its curtilage because it does not
justify an intrusion on a person’s separate and substantial
Fourth Amendment interest in his home and curtilage.
   As noted, the rationales underlying the automobile
exception are specific to the nature of a vehicle and the
ways in which it is distinct from a house. See Part II–A–1,
supra. The rationales thus take account only of the bal-
ance between the intrusion on an individual’s Fourth
Amendment interest in his vehicle and the governmental
interests in an expedient search of that vehicle; they do
not account for the distinct privacy interest in one’s home
or curtilage. To allow an officer to rely on the automobile
exception to gain entry into a house or its curtilage for the
purpose of conducting a vehicle search would unmoor the
exception from its justifications, render hollow the core
Fourth Amendment protection the Constitution extends to
the house and its curtilage, and transform what was
meant to be an exception into a tool with far broader
application. Indeed, its name alone should make all this
10                       COLLINS v. VIRGINIA

                          Opinion of the Court

clear enough: It is, after all, an exception for automobiles.3
——————
  3 The dissent concedes that “the degree of the intrusion on privacy” is

relevant in determining whether a warrant is required to search a
motor vehicle “located on private property.” Post, at 5–6 (opinion of
ALITO, J.). Yet it puzzlingly asserts that the “privacy interests at stake”
here are no greater than when a motor vehicle is searched “on public
streets.” Post, at 3–4. “An ordinary person of common sense,” post,
at 2, however, clearly would understand that the privacy interests at
stake in one’s private residential property are far greater than on a
public street. Contrary to the dissent’s suggestion, it is of no signifi-
cance that the motorcycle was parked just a “short walk up the drive-
way.” Ibid. The driveway was private, not public, property, and the
motorcycle was parked in the portion of the driveway beyond where a
neighbor would venture, in an area “intimately linked to the home, . . .
where privacy expectations are most heightened.” California v. Ciraolo,
476 U. S. 207, 213 (1986). Nor does it matter that Officer Rhodes
“did not damage any property,” post, at 2, for an officer’s care in con-
ducting a search does not change the character of the place being
searched. And, as we explain, see infra, at 13–14, it is not dispositive
that Officer Rhodes did not “observe anything along the way” to the
motorcycle “that he could not have seen from the street,” post, at 2.
Law enforcement officers need not “shield their eyes when passing by a
home on public thoroughfares,” Ciraolo, 476 U. S., at 213, but the
ability visually to observe an area protected by the Fourth Amendment
does not give officers the green light physically to intrude on it. See
Florida v. Jardines, 569 U. S. 1, 7–8 (2013). It certainly does not
permit an officer physically to intrude on curtilage, remove a tarp to
reveal license plate and vehicle identification numbers, and use those
numbers to confirm that the defendant committed a crime.
  The dissent also mistakenly relies on a law enacted by the First
Congress and mentioned in Carroll v. United States, 267 U. S. 132,
150–151 (1925), that authorized the warrantless search of vessels.
Post, at 4–5, n. 3. The dissent thinks it implicit in that statute that
“officers could cross private property such as wharves in order to reach
and board those vessels.” Ibid. Even if it were so that a police officer
could have entered a private wharf to search a vessel, that would not
prove he could enter the curtilage of a home to do so. To the contrary,
whereas the statute relied upon in Carroll authorized warrantless
searches of vessels, it expressly required warrants to search houses.
See 267 U. S., at 150–157; Act of July 31, 1789, §24, 1 Stat. 43. Here,
Officer Rhodes did not invade a private wharf to undertake a search; he
invaded the curtilage of a home.
                 Cite as: 584 U. S. ____ (2018)           11

                     Opinion of the Court

  Given the centrality of the Fourth Amendment interest
in the home and its curtilage and the disconnect between
that interest and the justifications behind the automobile
exception, we decline Virginia’s invitation to extend the
automobile exception to permit a warrantless intrusion on
a home or its curtilage.
                             III

                              A

  Virginia argues that this Court’s precedent indicates
that the automobile exception is a categorical one that
permits the warrantless search of a vehicle anytime,
anywhere, including in a home or curtilage. Specifically,
Virginia points to two decisions that it contends resolve
this case in its favor. Neither is dispositive or persuasive.
  First, Virginia invokes Scher v. United States, 305 U. S.
251 (1938). In that case, federal officers received a confi-
dential tip that a particular car would be transporting
bootleg liquor at a specified time and place. The officers
identified and followed the car until the driver “turned
into a garage a few feet back of his residence and within
the curtilage.” Id., at 253. As the driver exited his car, an
officer approached and stated that he had been informed
that the car was carrying contraband.              The driver
acknowledged that there was liquor in the trunk, and the
officer proceeded to open the trunk, find the liquor, arrest
the driver, and seize both the car and the liquor. Id., at
253–254. Although the officer did not have a search war-
rant, the Court upheld the officer’s actions as reasonable.
Id., at 255.
  Scher is inapposite. Whereas Collins’ motorcycle was
parked and unattended when Officer Rhodes intruded on
the curtilage to search it, the officers in Scher first en-
countered the vehicle when it was being driven on public
streets, approached the curtilage of the home only when
the driver turned into the garage, and searched the vehicle
12                  COLLINS v. VIRGINIA

                     Opinion of the Court

only after the driver admitted that it contained contra-
band. Scher by no means established a general rule that
the automobile exception permits officers to enter a home
or its curtilage absent a warrant. The Court’s brief analy-
sis referenced Carroll, but only in the context of observing
that, consistent with that case, the “officers properly could
have stopped” and searched the car “just before [petitioner]
entered the garage,” a proposition the petitioner did
“not seriously controvert.” Scher, 305 U. S., at 254–255.
The Court then explained that the officers did not lose
their ability to stop and search the car when it entered
“the open garage closely followed by the observing officer”
because “[n]o search was made of the garage.” Id., at 255.
It emphasized that “[e]xamination of the automobile ac-
companied an arrest, without objection and upon admis-
sion of probable guilt,” and cited two search-incident-to-
arrest cases. Ibid. (citing Agnello v. United States, 269
U. S. 20, 30 (1925); Wisniewski v. United States, 47 F. 2d
825, 826 (CA6 1931)). Scher’s reasoning thus was both
case specific and imprecise, sounding in multiple doc-
trines, particularly, and perhaps most appropriately, hot
pursuit. The decision is best regarded as a factbound one,
and it certainly does not control this case.
   Second, Virginia points to Labron, 518 U. S. 938, where
the Court upheld under the automobile exception the
warrantless search of an individual’s pickup truck that
was parked in the driveway of his father-in-law’s farm-
house. Id., at 939–940; Commonwealth v. Kilgore, 544 Pa.
439, 444, 677 A. 2d 311, 313 (1995). But Labron provides
scant support for Virginia’s position. Unlike in this case,
there was no indication that the individual who owned the
truck in Labron had any Fourth Amendment interest in
the farmhouse or its driveway, nor was there a determina-
tion that the driveway was curtilage.
                 Cite as: 584 U. S. ____ (2018)          13

                     Opinion of the Court

                              B
   Alternatively, Virginia urges the Court to adopt a more
limited rule regarding the intersection of the automobile
exception and the protection afforded to curtilage. Virginia
would prefer that the Court draw a bright line and hold
that the automobile exception does not permit warrantless
entry into “the physical threshold of a house or a similar
fixed, enclosed structure inside the curtilage like a gar-
age.” Brief for Respondent 46. Requiring officers to make
“case-by-case curtilage determinations,” Virginia reasons,
unnecessarily complicates matters and “raises the poten-
tial for confusion and . . . error.” Id., at 46–47 (internal
quotation marks omitted).
   The Court, though, has long been clear that curtilage is
afforded constitutional protection. See Oliver, 466 U. S.,
at 180. As a result, officers regularly assess whether an
area is curtilage before executing a search. Virginia pro-
vides no reason to conclude that this practice has proved
to be unadministrable, either generally or in this context.
Moreover, creating a carveout to the general rule that
curtilage receives Fourth Amendment protection, such
that certain types of curtilage would receive Fourth
Amendment protection only for some purposes but not for
others, seems far more likely to create confusion than does
uniform application of the Court’s doctrine.
   In addition, Virginia’s proposed rule rests on a mistaken
premise about the constitutional significance of visibility.
The ability to observe inside curtilage from a lawful van-
tage point is not the same as the right to enter curtilage
without a warrant for the purpose of conducting a search
to obtain information not otherwise accessible. Cf. Cir-
aolo, 476 U. S., at 213–214 (holding that “physically non-
intrusive” warrantless aerial observation of the curtilage
of a home did not violate the Fourth Amendment, and
could form the basis for probable cause to support a war-
rant to search the curtilage). So long as it is curtilage, a
14                   COLLINS v. VIRGINIA

                      Opinion of the Court

parking patio or carport into which an officer can see from
the street is no less entitled to protection from trespass
and a warrantless search than a fully enclosed garage.
  Finally, Virginia’s proposed bright-line rule automati-
cally would grant constitutional rights to those persons
with the financial means to afford residences with garages
in which to store their vehicles but deprive those persons
without such resources of any individualized consideration
as to whether the areas in which they store their vehicles
qualify as curtilage. See United States v. Ross, 456 U. S.
798, 822 (1982) (“[T]he most frail cottage in the kingdom is
absolutely entitled to the same guarantees of privacy as
the most majestic mansion”).
                             IV
   For the foregoing reasons, we conclude that the automo-
bile exception does not permit an officer without a warrant
to enter a home or its curtilage in order to search a vehicle
therein. We leave for resolution on remand whether Of-
ficer Rhodes’ warrantless intrusion on the curtilage of
Collins’ house may have been reasonable on a different
basis, such as the exigent circumstances exception to the
warrant requirement. The judgment of the Supreme
Court of Virginia is therefore reversed, and the case is
remanded for further proceedings not inconsistent with
this opinion.
                                              It is so ordered.
                 Cite as: 584 U. S. ____ (2018)           1

                    THOMAS, J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 16–1027
                         _________________


 RYAN AUSTIN COLLINS, PETITIONER v. VIRGINIA
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF 

                       VIRGINIA

                        [May 29, 2018] 


   JUSTICE THOMAS, concurring.
   I join the Court’s opinion because it correctly resolves
the Fourth Amendment question in this case. Notably,
the only reason that Collins asked us to review this ques-
tion is because, if he can prove a violation of the Fourth
Amendment, our precedents require the Virginia courts to
apply the exclusionary rule and potentially suppress the
incriminating evidence against him. I write separately
because I have serious doubts about this Court’s authority
to impose that rule on the States. The assumption that
state courts must apply the federal exclusionary rule is
legally dubious, and many jurists have complained that it
encourages “distort[ions]” in substantive Fourth Amend-
ment law, Rakas v. Illinois, 439 U. S. 128, 157 (1978)
(White, J., dissenting); see also Coolidge v. New Hamp-
shire, 403 U. S. 443, 490 (1971) (Harlan, J., concurring);
Calabresi, The Exclusionary Rule, 26 Harv. J. L. & Pub.
Pol’y 111, 112 (2003).
   The Fourth Amendment, as relevant here, protects the
people from “unreasonable searches” of “their . . . houses.”
As a general rule, warrantless searches of the curtilage
violate this command. At the founding, curtilage was
considered part of the “hous[e]” itself. See 4 W. Black-
stone, Commentaries on the Laws of England 225
(1769) (“[T]he capital house protects and privileges all its
branches and appurtenants, if within the curtilage”). And
2                       COLLINS v. VIRGINIA

                        THOMAS, J., concurring

except in circumstances not present here, house searches
required a specific warrant. See W. Cuddihy, The Fourth
Amendment: Origins and Original Meaning 602–1791,
p. 743 (2009) (Cuddihy); Donahue, The Original Fourth
Amendment, 83 U. Chi. L. Rev. 1181, 1237–1240 (2016);
Davies, Recovering the Original Fourth Amendment, 98
Mich. L. Rev. 547, 643–646 (1999). A warrant was re-
quired even if the house was being searched for stolen
goods or contraband—objects that, unlike cars, are not
protected by the Fourth Amendment at all. Id., at 647–
650; see also Carroll v. United States, 267 U. S. 132, 150–
152 (1925) (Taft, C. J.) (discussing founding-era evidence
that a search warrant was required when stolen goods and
contraband were “concealed in a dwelling house” but not
when they were “in course of transportation and concealed
in a movable vessel”). Accordingly, the police acted “un-
reasonabl[y]” when they searched the curtilage of Collins’
house without a warrant.1
   While those who ratified the Fourth and Fourteenth
Amendments would agree that a constitutional violation
occurred here, they would be deeply confused about the
posture of this case and the remedy that Collins is seek-
ing. Historically, the only remedies for unconstitutional
searches and seizures were “tort suits” and “self-help.”
Utah v. Strieff, 579 U. S. ___, ___ (2016) (slip op., at 4).
The exclusionary rule—the practice of deterring illegal
searches and seizures by suppressing evidence at criminal
trials—did not exist. No such rule existed in “Roman Law,
Napoleonic Law or even the Common Law of England.”
Burger, Who Will Watch the Watchman? 14 Am. U.
L. Rev. 1 (1964). And this Court did not adopt the federal
——————
  1 Collins did not live at the house; he merely stayed there with his

girlfriend several times a week. But Virginia does not contest Collins’
assertion that the house is his, so I agree with the Court that Virginia
has forfeited any argument to the contrary. See ante, at 2, n. 1; United
States v. Jones, 565 U. S. 400, 404, n. 2 (2012).
                  Cite as: 584 U. S. ____ (2018)            3

                     THOMAS, J., concurring

exclusionary rule until the 20th century. See Weeks v.
United States, 232 U. S. 383 (1914). As late as 1949,
nearly two-thirds of the States did not have an exclusion-
ary rule. See Wolf v. Colorado, 338 U. S. 25, 29 (1949).
Those States, as then-Judge Cardozo famously explained,
did not understand the logic of a rule that allowed “[t]he
criminal . . . to go free because the constable has blun-
dered.” People v. Defore, 242 N. Y. 13, 21, 150 N. E. 585,
587 (1926).
   The Founders would not have understood the logic of
the exclusionary rule either. Historically, if evidence was
relevant and reliable, its admissibility did not “depend
upon the lawfulness or unlawfulness of the mode, by
which it [was] obtained.” United States v. The La Jeune
Eugenie, 26 F. Cas. 832, 843 (No. 15, 551) (CC Mass. 1822)
(Story, J.); accord, 1 S. Greenleaf, Evidence §254a,
pp. 825–826 (14th ed. 1883) (“[T]hat . . . subjects of evi-
dence may have been . . . unlawfully obtained . . . is no
valid objection to their admissibility if they are pertinent
to the issue”); 4 J. Wigmore, Evidence §2183, p. 626 (2d ed.
1923) (“[I]t has long been established that the admissibil-
ity of evidence is not affected by the illegality of the means
through which the party has been enabled to obtain the
evidence” (emphasis deleted)). And the common law some-
times reflected the inverse of the exclusionary rule: The
fact that someone turned out to be guilty could justify an
illegal seizure. See Gelston v. Hoyt, 3 Wheat. 246, 310
(1818) (Story, J.) (“At common law, any person may at his
peril, seize for a forfeiture to the government; and if the
government adopt his seizure, and the property is con-
demned, he will be completely justified”); 2 W. Hawkins,
Pleas of the Crown 77 (1721) (“And where a Man arrests
another, who is actually guilty of the Crime for which he is
arrested, . . . he needs not in justifying it, set forth any
special Cause of his Suspicion”).
   Despite this history, the Court concluded in Mapp v.
4                        COLLINS v. VIRGINIA

                         THOMAS, J., concurring

Ohio, 367 U. S. 643 (1961), that the States must apply the
federal exclusionary rule in their own courts. Id., at 655.2
Mapp suggested that the exclusionary rule was required
by the Constitution itself. See, e.g., id., at 657 (“[T]he
exclusionary rule is an essential part of both the Fourth
and Fourteenth Amendments”); id., at 655 (“[E]vidence
obtained by searches and seizures in violation of the Con-
stitution is, by that same authority, inadmissible in a
state court”); id., at 655–656 (“[I]t was . . . constitutionally
necessary that the exclusion doctrine—an essential part of
the right to privacy—be also insisted upon”).3 But that
suggestion could not withstand even the slightest scrutiny.
The exclusionary rule appears nowhere in the Constitu-
tion, postdates the founding by more than a century, and
contradicts several longstanding principles of the common
law. See supra, at 2–3; Cuddihy 759–760; Amar, Fourth
Amendment First Principles, 107 Harv. L. Rev. 757, 786
(1994); Kaplan, The Limits of the Exclusionary Rule, 26

——————
   2 Twelve years before Mapp, the Court declined to apply the federal

exclusionary rule to the States. See Wolf v. Colorado, 338 U. S. 25
(1949). Wolf denied that the Constitution requires the exclusionary
rule, since “most of the English-speaking world” does not apply that
rule and alternatives such as civil suits and internal police discipline do
not “fal[l] below the minimal standards assured by the Due Process
Clause.” Id., at 29, 31. In Mapp, the Court overruled Wolf and applied
the exclusionary rule to the States, even though no party had briefed or
argued that question. See 367 U. S., at 672–674, and nn. 4–6 (Harlan,
J., dissenting); Stewart, The Road to Mapp v. Ohio and Beyond: The
Origins, Development and Future of the Exclusionary Rule, 83 Colum.
L. Rev. 1365, 1368 (1983).
   3 Justice Black, the essential fifth vote in Mapp, did not agree that

the Fourth Amendment contains an exclusionary rule. See 367 U. S.,
at 661–662 (concurring opinion) (“[T]he Fourth Amendment does not
itself contain any provision expressly precluding the use of such evi-
dence, and I am extremely doubtful that such a provision could prop-
erly be inferred”). But he concluded that, when the police seize private
papers, suppression is required by a combination of the Fourth and
Fifth Amendments. See id., at 662–666.
                      Cite as: 584 U. S. ____ (2018)                       5

                          THOMAS, J., concurring

Stan. L. Rev. 1027, 1030–1031 (1974).
    Recognizing this, the Court has since rejected Mapp’s
“ ‘[e]xpansive dicta’ ” and clarified that the exclusionary
rule is not required by the Constitution. Davis v. United
States, 564 U. S. 229, 237 (2011) (quoting Hudson v. Mich-
igan, 547 U. S. 586, 591 (2006)). Suppression, this Court
has explained, is not “a personal constitutional right.”
United States v. Calandra, 414 U. S. 338, 348 (1974);
accord, Stone v. Powell, 428 U. S. 465, 486 (1976). The
Fourth Amendment “says nothing about suppressing
evidence,” Davis, supra, at 236, and a prosecutor’s “use of
fruits of a past unlawful search or seizure ‘work[s] no new
Fourth Amendment wrong,’ ” United States v. Leon, 468
U. S. 897, 906 (1984) (quoting Calandra, supra, at 354).4
Instead, the exclusionary rule is a “judicially created”
doctrine that is “prudential rather than constitutionally
mandated.” Pennsylvania Bd. of Probation and Parole v.
Scott, 524 U. S. 357, 363 (1998); accord, Herring v. United
States, 555 U. S. 135, 139 (2009); Arizona v. Evans, 514
U. S. 1, 10 (1995); United States v. Janis, 428 U. S. 433,
459–460 (1976).5
——————
   4 The exclusionary rule is not required by the Due Process Clause

either. Given its nonexistent historical foundation, the exclusionary
rule cannot be a “settled usag[e] and mod[e] of proceeding existing in
the common and statute law of England, before the emigration of our
ancestors.” Murray’s Lessee v. Hoboken Land & Improvement Co., 18
How. 272, 277 (1856). And the rule “has ‘no bearing on . . . the fairness
of the trial.’ ” Desist v. United States, 394 U. S. 244, 254, n. 24 (1969).
If anything, the exclusionary rule itself “ ‘offends basic concepts of the
criminal justice system’ ” and exacts a “ ‘costly toll upon truth-seeking.’ ”
Herring v. United States, 555 U. S. 135, 141 (2009). “The [excluded]
evidence is likely to be the most reliable that could possibly be obtained
[and thus] exclusion rather than admission creates the danger of a
verdict erroneous on the true facts.” H. Friendly, Benchmarks 260
(1967).
   5 These statements cannot be dismissed as mere dicta. Cf. Dickerson

v. United States, 530 U. S. 428, 438–441, and n. 2 (2000) (constitution-
alizing the rule announced in Miranda v. Arizona, 384 U. S. 436 (1966),
6                       COLLINS v. VIRGINIA

                        THOMAS, J., concurring

   Although the exclusionary rule is not part of the Consti-
tution, this Court has continued to describe it as “federal
law” and assume that it applies to the States. Evans,
supra; Massachusetts v. Sheppard, 468 U. S. 981, 991
(1984). Yet the Court has never attempted to justify this
assumption. If the exclusionary rule is federal law, but is
not grounded in the Constitution or a federal statute, then
it must be federal common law. See Monaghan, Foreword:
Constitutional Common Law, 89 Harv. L. Rev. 1, 10
(1975). As federal common law, however, the exclusionary
rule cannot bind the States.
   Federal law trumps state law only by virtue of the Su-
premacy Clause, which makes the “Constitution, and the
Laws of the United States which shall be made in Pursu-
ance thereof; and all Treaties . . . the supreme Law of the
Land,” Art. VI, cl. 2. When the Supremacy Clause refers
to “[t]he Laws of the United States made in Pursuance [of
the Constitution],” it means federal statutes, not federal
common law. Ramsey, The Supremacy Clause, Original
Meaning, and Modern Law, 74 Ohio St. L. J. 559, 572–599
(2013) (Ramsey); Clark, Separation of Powers as a Safe-
guard of Federalism, 79 Texas L. Rev. 1321, 1334–1336,
1338–1367 (2001) (Clark); see also Gibbons v. Ogden, 9
Wheat. 1, 211 (1824) (Marshall, C. J.) (“The appropriate
application of that part of the clause which confers . . .
supremacy on laws . . . is to . . . the laws of Congress, made
in pursuance of the constitution”); Hart, The Relations

——————
despite earlier precedents to the contrary). The nonconstitutional
status of the exclusionary rule is why this Court held in Stone v.
Powell, 428 U. S. 465, 482–495 (1976), that violations are not cogniza-
ble on federal habeas review. Cf. Dickerson, supra, at 439 n. 3. And
the nonconstitutional status of the rule is why this Court has created
more than a dozen exceptions to it, which apply even when the Fourth
Amendment is concededly violated. See United States v. Weaver, 808
F. 3d 26, 49 (CADC 2015) (Henderson, J., dissenting) (collecting cases);
cf. Dickerson, supra, at 441.
                 Cite as: 584 U. S. ____ (2018)            7

                    THOMAS, J., concurring

Between State and Federal Law, 54 Colum. L. Rev. 489,
500 (1954) (“[T]he supremacy clause is limited to those
‘Laws’ of the United States which are passed by Congress
pursuant to the Constitution”). By referencing laws “made
in Pursuance” of the Constitution, the Supremacy Clause
incorporates the requirements of Article I, which force
Congress to stay within its enumerated powers, §8, and
follow the cumbersome procedures for enacting federal
legislation, §7. See Wyeth v. Levine, 555 U. S. 555, 585–
587 (2009) (THOMAS, J., concurring in judgment); 3 J.
Story, Commentaries on the Constitution of the United
States §1831, pp. 693–694 (1833); Clark 1334. Those
procedures—especially the requirement that bills pass the
Senate, where the States are represented equally and
Senators were originally elected by state legislatures—
safeguard federalism by making federal legislation more
difficult to pass and more responsive to state interests.
See Ramsey 565; Clark 1342–1343. Federal common law
bypasses these procedures and would not have been con-
sidered the kind of “la[w]” that can bind the States under
the Supremacy Clause. See Ramsey 564–565, 568, 574,
581; Jay, Origins of Federal Common Law: Part Two, 133
U. Pa. L. Rev. 1231, 1275 (1985).
   True, this Court, without citing the Supremacy Clause,
has recognized several “enclaves of federal judge-made law
which bind the States.” Banco Nacional de Cuba v. Sab-
batino, 376 U. S. 398, 426 (1964); see, e.g., id., at 427–428
(foreign affairs); Hinderlider v. La Plata River & Cherry
Creek Ditch Co., 304 U. S. 92, 110 (1938) (disputes be-
tween States); Garrett v. Moore-McCormack Co., 317 U. S.
239, 245 (1942) (admiralty); Clearfield Trust Co. v. United
States, 318 U. S. 363, 366 (1943) (certain rights and obli-
gations of the United States); Textile Workers v. Lincoln
Mills of Ala., 353 U. S. 448, 456–457 (1957) (aspects of
federal labor law). To the extent these enclaves are dele-
gations of lawmaking authority from the Constitution or a
8                   COLLINS v. VIRGINIA

                    THOMAS, J., concurring

federal statute, they do not conflict with the original
meaning of the Supremacy Clause (though they might be
illegitimate for other reasons). See Ramsey 568–569;
Grano, Prophylactic Rules in Criminal Procedure: A Ques-
tion of Article III Legitimacy, 80 Nw. U. L. Rev. 100, 131–
132 (1985). To the extent these enclaves are not rooted in
the Constitution or a statute, their pre-emptive force is
questionable. But that is why this Court has “limited”
them to a “ ‘few’ ” “narrow areas” where “the authority and
duties of the United States as sovereign are intimately
involved” or where “the interstate or international nature
of the controversy makes it inappropriate for state law to
control.” Texas Industries, Inc. v. Radcliff Materials, Inc.,
451 U. S. 630, 640–641 (1981) (quoting Wheeldin v.
Wheeler, 373 U. S. 647, 651 (1963)). Outside these narrow
enclaves, the general rule is that “[t]here is no federal
general common law” and “[e]xcept in matters governed by
the Federal Constitution or by Acts of Congress, the law to
be applied in any case is the law of the State.” Erie R. Co.
v. Tompkins, 304 U. S. 64, 78 (1938).
   These precedents do not support requiring the States to
apply the exclusionary rule. As explained, the exclusion-
ary rule is not rooted in the Constitution or a federal
statute. This Court has repeatedly rejected the idea that
the rule is in the Fourth and Fourteenth Amendments,
expressly or implicitly. See Davis, 564 U. S., at 236; Leon,
468 U. S., at 905–906; cf. Ziglar v. Abbasi, 582 U. S. ___,
___ (2017) (slip op., at 11) (explaining that reading implied
remedies into the Constitution is “a ‘disfavored’ judicial
activity”). And the exclusionary rule does not implicate
any of the special enclaves of federal common law. It does
not govern the sovereign duties of the United States or
disputes of an interstate or international character. In-
stead, the rule governs the methods that state police
officers use to solve crime and the procedures that state
courts use at criminal trials—subjects that the Federal
                      Cite as: 584 U. S. ____ (2018)                       9

                          THOMAS, J., concurring

Government generally has no power to regulate. See
United States v. Morrison, 529 U. S. 598, 618 (2000) (ex-
plaining that “[t]he regulation” and “vindication” of intra-
state crime “has always been the province of the States”);
Smith v. Phillips, 455 U. S. 209, 221 (1982) (“Federal
courts hold no supervisory authority over state judicial
proceedings”). These are not areas where federal common
law can bind the States.6
                         *    *    *
  In sum, I am skeptical of this Court’s authority to im-
pose the exclusionary rule on the States. We have not yet
revisited that question in light of our modern precedents,
which reject Mapp’s essential premise that the exclusion-
ary rule is required by the Constitution. We should do so.




——————
  6 Of course, the States are free to adopt their own exclusionary rules

as a matter of state law. But nothing in the Federal Constitution
requires them to do so. Even assuming the Constitution requires
particular state-law remedies for federal constitutional violations, it
does not require the exclusionary rule. The “sole purpose” of the
exclusionary rule is “to deter future Fourth Amendment violations”; it
does not “ ‘redress’ ” or “ ‘repair’ ” past ones. Davis v. United States, 564
U. S. 229, 236–237 (2011). This Court has noted the lack of evidence
supporting its deterrent effect, see United States v. Janis, 428 U. S.
433, 450, n. 22 (1976), and this Court has recognized the effectiveness
of alternative deterrents such as state tort law, state criminal law,
internal police discipline, and suits under 42 U. S. C. §1983, see Hud-
son v. Michigan, 547 U. S. 586, 597–599 (2006).
                    Cite as: 584 U. S. ____ (2018)                   1

                         ALITO, J., dissenting

SUPREME COURT OF THE UNITED STATES
                             _________________

                             No. 16–1027
                             _________________


 RYAN AUSTIN COLLINS, PETITIONER v. VIRGINIA
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF 

                       VIRGINIA

                            [May 29, 2018] 


   JUSTICE ALITO, dissenting.
   The Fourth Amendment prohibits “unreasonable”
searches. What the police did in this case was entirely
reasonable. The Court’s decision is not.
   On the day in question, Officer David Rhodes was stand-
ing at the curb of a house where petitioner, Ryan Austin
Collins, stayed a couple of nights a week with his girl-
friend. From his vantage point on the street, Rhodes saw
an object covered with a tarp in the driveway, just a car’s
length or two from the curb. It is undisputed that Rhodes
had probable cause to believe that the object under the
tarp was a motorcycle that had been involved a few
months earlier in a dangerous highway chase, eluding the
police at speeds in excess of 140 mph. See Tr. of Oral Arg.
22; App. to Pet. for Cert. 67. Rhodes also had probable
cause to believe that petitioner had been operating the
motorcycle1 and that a search of the motorcycle would
provide evidence that the motorcycle had been stolen.2
   If the motorcycle had been parked at the curb, instead of
in the driveway, it is undisputed that Rhodes could have
——————
  1 Petitioner had a photo on his Facebook profile of a motorcycle that

resembled the unusual motorcycle involved in the prior highway chase.
See ante, at 1–2 (majority opinion).
  2 Rhodes suspected the motorcycle was stolen based on a conversation

he had with the man who had sold the motorcycle to petitioner. See
App. 57–58.
2                  COLLINS v. VIRGINIA

                     ALITO, J., dissenting

searched it without obtaining a warrant. See Tr. of Oral
Arg. 9; Reply Brief 1. Nearly a century ago, this Court
held that officers with probable cause may search a motor
vehicle without obtaining a warrant. Carroll v. United
States, 267 U. S. 132, 153, 155–156 (1925). The principal
rationale for this so-called automobile or motor-vehicle
exception to the warrant requirement is the risk that the
vehicle will be moved during the time it takes to obtain a
warrant. Id., at 153; California v. Carney, 471 U. S. 386,
390–391 (1985). We have also observed that the owner of
an automobile has a diminished expectation of privacy in
its contents. Id., at 391–393.
   So why does the Court come to the conclusion that
Officer Rhodes needed a warrant in this case? Because, in
order to reach the motorcycle, he had to walk 30 feet or so
up the driveway of the house rented by petitioner’s girl-
friend, and by doing that, Rhodes invaded the home’s
“curtilage.” Ante, at 6–7. The Court does not dispute that
the motorcycle, when parked in the driveway, was just as
mobile as it would have been had it been parked at the
curb. Nor does the Court claim that Officer Rhodes’s short
walk up the driveway did petitioner or his girlfriend any
harm. Rhodes did not damage any property or observe
anything along the way that he could not have seen from
the street. But, the Court insists, Rhodes could not enter
the driveway without a warrant, and therefore his search
of the motorcycle was unreasonable and the evidence
obtained in that search must be suppressed.
   An ordinary person of common sense would react to the
Court’s decision the way Mr. Bumble famously responded
when told about a legal rule that did not comport with the
reality of everyday life. If that is the law, he exclaimed,
“the law is a ass—a idiot.” C. Dickens, Oliver Twist 277
(1867).
   The Fourth Amendment is neither an “ass” nor an “idiot.”
Its hallmark is reasonableness, and the Court’s strikingly
                  Cite as: 584 U. S. ____ (2018)            3

                      ALITO, J., dissenting

unreasonable decision is based on a misunderstanding of
Fourth Amendment basics.
   The Fourth Amendment protects “[t]he right of the
people to be secure in their persons, houses, papers, and
effects.” A “house,” for Fourth Amendment purposes, is
not limited to the structure in which a person lives, but by
the same token, it also does not include all the real property
surrounding a dwelling. See, e.g., Florida v. Jardines, 569
U. S. 1, 6 (2013); United States v. Dunn, 480 U. S. 294,
300–301 (1987). Instead, a person’s “house” encompasses
the dwelling and a circumscribed area of surrounding land
that is given the name “curtilage.” Oliver v. United States,
466 U. S. 170, 180 (1984). Land outside the curtilage is
called an “open field,” and a search conducted in that area
is not considered a search of a “house” and is therefore not
governed by the Fourth Amendment. Ibid. Ascertaining
the boundaries of the curtilage thus determines only
whether a search is governed by the Fourth Amendment.
The concept plays no other role in Fourth Amendment
analysis.
   In this case, there is no dispute that the search of the
motorcycle was governed by the Fourth Amendment, and
therefore whether or not it occurred within the curtilage is
not of any direct importance. The question before us is not
whether there was a Fourth Amendment search but
whether the search was reasonable. And the only possible
argument as to why it might not be reasonable concerns
the need for a warrant. For nearly a century, however, it
has been well established that officers do not need a war-
rant to search a motor vehicle on public streets so long as
they have probable cause. Carroll, supra, at 153, 156; see
also, e.g., Pennsylvania v. Labron, 518 U. S. 938, 940
(1996) (per curiam); Carney, supra, at 394; South Dakota
v. Opperman, 428 U. S. 364, 367–368 (1976); Chambers v.
Maroney, 399 U. S. 42, 50–51 (1970). Thus, the issue here
is whether there is any good reason why this same rule
4                      COLLINS v. VIRGINIA

                         ALITO, J., dissenting

should not apply when the vehicle is parked in plain view
in a driveway just a few feet from the street.
   In considering that question, we should ask whether the
reasons for the “automobile exception” are any less valid
in this new situation. Is the vehicle parked in the drive-
way any less mobile? Are any greater privacy interests at
stake? If the answer to those questions is “no,” then the
automobile exception should apply. And here, the answer
to each question is emphatically “no.” The tarp-covered
motorcycle parked in the driveway could have been uncov-
ered and ridden away in a matter of seconds. And Officer
Rhodes’s brief walk up the driveway impaired no real
privacy interests.
   In this case, the Court uses the curtilage concept in a way
that is contrary to our decisions regarding other, exigency-
based exceptions to the warrant requirement. Take, for
example, the “emergency aid” exception. See Brigham
City v. Stuart, 547 U. S. 398 (2006). When officers reason-
ably believe that a person inside a dwelling has urgent
need of assistance, they may cross the curtilage and enter
the building without first obtaining a warrant. Id., at
403–404. The same is true when officers reasonably be-
lieve that a person in a dwelling is destroying evidence.
See Kentucky v. King, 563 U. S. 452, 460 (2011). In both of
those situations, we ask whether “ ‘the exigencies of the
situation’ make the needs of law enforcement so compel-
ling that the warrantless search is objectively reasonable.”
Brigham City, supra, at 403 (quoting Mincey v. Arizona,
437 U. S. 385, 394 (1978)). We have not held that the need
to cross the curtilage independently necessitates a war-
rant, and there is no good reason to apply a different rule
here.3
——————
  3 Indeed, I believe that the First Congress implicitly made the same

judgment in enacting the statute on which Carroll v. United States, 267
U. S. 132 (1925), relied when the motor-vehicle exception was first
                     Cite as: 584 U. S. ____ (2018)                    5

                          ALITO, J., dissenting

   It is no answer to this argument that the emergency-aid
and destruction-of-evidence exceptions require an inquiry
into the practicality of obtaining a warrant in the particu-
lar circumstances of the case. Our precedents firmly
establish that the motor-vehicle exception, unlike these
other exceptions, “has no separate exigency requirement.”
Maryland v. Dyson, 527 U. S. 465, 466–467 (1999) (per
curiam). It is settled that the mobility of a motor vehicle
categorically obviates any need to engage in such a case-
specific inquiry. Requiring such an inquiry here would
mark a substantial alteration of settled Fourth Amend-
ment law.
   This does not mean, however, that a warrant is never
needed when officers have probable cause to search a
motor vehicle, no matter where the vehicle is located.
While a case-specific inquiry regarding exigency would be
inconsistent with the rationale of the motor-vehicle excep-
tion, a case-specific inquiry regarding the degree of intru-
sion on privacy is entirely appropriate when the motor
vehicle to be searched is located on private property. After
all, the ultimate inquiry under the Fourth Amendment is
——————
recognized. Since the First Congress sent the Bill of Rights to the
States for ratification, we have often looked to laws enacted by that
Congress as evidence of the original understanding of the meaning of
those Amendments. See, e.g., id., at 150–151; Town of Greece v. Gallo-
way, 572 U. S. ___, ___–___ (2014) (slip op., at 7–8); United States v.
Villamonte-Marquez, 462 U. S. 579, 585–586 (1983); United States v.
Ramsey, 431 U. S. 606, 616–617 (1977). Carroll itself noted that the
First Congress enacted a law authorizing officers to search vessels
without a warrant. 267 U. S., at 150–151. Although this statute did
not expressly state that these officers could cross private property such
as wharves in order to reach and board those vessels, I think that was
implicit. Otherwise, the statute would very often have been ineffective.
And when Congress later enacted similar laws, it made this authoriza-
tion express. See, e.g., An Act Further to Prevent Smuggling and for
Other Purposes, §5, 14 Stat. 179. For this reason, Officer Rhodes’s
conduct in this case is consistent with the original understanding of the
Fourth Amendment, as explicated in Carroll.
6                   COLLINS v. VIRGINIA

                     ALITO, J., dissenting

whether a search is reasonable, and that inquiry often
turns on the degree of the intrusion on privacy. Thus,
contrary to the opinion of the Court, an affirmance in this
case would not mean that officers could perform a war-
rantless search if a motorcycle were located inside a house.
See ante, at 7. In that situation, the intrusion on privacy
would be far greater than in the present case, where the
real effect, if any, is negligible.
  I would affirm the decision below and therefore respect-
fully dissent.

```

---
