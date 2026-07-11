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

## GROUP: _overhaul2/lake/cases/Arizona v. Gant.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Arizona v. Gant"
type: case
citation: "556 U.S. 332 (2009)"
parallel_cite: "129 S. Ct. 1710; 173 L. Ed. 2d 485"
neutral_cite: 2009 U.S. LEXIS 3120
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-04-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2009-04-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Arizona v. Gant
  varies_by_point: false
  scope_note: "Gant itself cabins the broad reading of New York v. Belton; Gant is good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145887/arizona-v-gant/"
  cluster_id: 145887
  opinion_id: 9435359
  identity_checked: true
homes:
  - page: "[[SIA Vehicles]]"
    role: "Key — Anchor"
  - page: "[[Traffic Stops]]"
    role: "Related (cross-doctrine)"
related: ["[[New York v. Belton]]", "[[Chimel v. California]]", "[[Thornton v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "automobile", "vehicle-search"]
holding: "Cabins Belton. A vehicle search incident to a recent occupant's arrest is permitted only when (1) the arrestee is unsecured and within…"
lake:
  record_id: Arizona v. Gant
  status: verified
  projected_at: 2026-07-06
---

# Arizona v. Gant

*556 U.S. 332 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gant was arrested for driving on a suspended license. After he was handcuffed and locked in the back of a patrol car, officers searched his car and found cocaine in a jacket on the back seat. He moved to suppress the cocaine as the product of an unlawful [[Search Incident to Arrest|search incident to arrest]].

## Issue
Whether police may search the passenger compartment of a vehicle incident to a recent occupant's arrest when the arrestee has been secured and cannot reach the vehicle, and there is no reason to believe the vehicle contains evidence of the offense of arrest.

## Rule
A vehicle search incident to a recent occupant's arrest is allowed only on one of two independent justifications: "Police may search a vehicle incident to a recent occupant's arrest only if the arrestee is within reaching distance of the passenger compartment at the time of the search or it is reasonable to believe the vehicle contains evidence of the offense of arrest." — 556 U.S. at 351 (129 S. Ct. at 1723). ^pin-351

Absent those justifications, "a search of an arrestee's vehicle will be unreasonable unless police obtain a warrant or show that another exception to the warrant requirement applies." — *Id.* This reading cabins the broad understanding of [[New York v. Belton]] that had been taken to authorize a vehicle search whenever an occupant was arrested.

## Application
On these facts both justifications were absent. Gant had been handcuffed and locked in a patrol car before the search, so he was not within reaching distance of the passenger compartment; and he was arrested for driving on a suspended license — an offense for which the car would hold no evidence. Because neither the officer-safety/evidence-preservation rationale of *[[Chimel v. California|Chimel]]* nor the evidence-of-the-offense rationale applied, the [[Search Incident to Arrest|search incident to arrest]] was unreasonable.

## Conclusion
The vehicle search was unconstitutional; the judgment of the Arizona Supreme Court suppressing the evidence was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of *Gant*. *Gant* itself **narrowed** the expansive reading of [[New York v. Belton]] (and [[Thornton v. United States]]) for vehicle [[Search Incident to Arrest|searches incident to arrest]], replacing automatic passenger-compartment searches with its two-justification test.

## Appears on
- [[SIA Vehicles]] — *Key — Anchor*
- [[Traffic Stops]] — *Related (cross-doctrine)*

## Sources
- *Arizona v. Gant*, 556 U.S. 332 (2009) — https://www.courtlistener.com/opinion/145887/arizona-v-gant/ — pinpoint: 351 (parallel 129 S. Ct. 1723).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "868055f5797209ae", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Arizona v. Gant"}, "payload": {"all": [{"cite": "556 U.S. 332", "page": "332", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "556"}, {"cite": "129 S. Ct. 1710", "page": "1710", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "129"}, {"cite": "173 L. Ed. 2d 485", "page": "485", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "173"}, {"cite": "2009 U.S. LEXIS 3120", "page": "3120", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2009"}], "display": "556 U.S. 332", "official": {"cite": "556 U.S. 332", "page": "332", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "556"}, "official_selection_present": true, "record_id": "Arizona v. Gant"}}
{"assertion_id": "77f0c665970ef8f1", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-351", "record_id": "Arizona v. Gant"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-351", "pinpoint_status": "slip-only", "quote": "--- # Arizona v. Gant *556 U.S. 332 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gant was arrested for driving on a suspended license. After he was handcuffed and locked in the back of a patrol car, officers searched his car and found cocaine in a jacket on the back seat. He moved to suppress the cocaine as the product of an unlawful search incident to arrest. ## Issue Whether police may search the passenger compartment of a vehicle incident to a recent occupant's arrest when the arrestee has been secured and cannot reach the vehicle, and there is no reason to believe the vehicle contains evidence of the offense of arrest. ## Rule A vehicle search incident to a recent occupant's arrest is allowed only on one of two independent justifications:", "quote_fidelity": "mismatch", "record_id": "Arizona v. Gant", "star_marker": null}}
{"assertion_id": "330abd3fbfa388ad", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Arizona v. Gant"}, "payload": {"as_of_content": "2009-04-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Arizona v. Gant", "scope_note": "Gant itself cabins the broad reading of New York v. Belton; Gant is good law.", "varies_by_point": false}}
```

### lake record — Arizona v. Gant

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arizona v. Gant",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Arizona v. Gant",
    "case_name_short": "Gant",
    "case_name_full": "Arizona v. Gant",
    "input_case_name": "Arizona v. Gant",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-04-21",
    "year": 2009,
    "docket": null,
    "cluster_id": 145887,
    "lead_opinion_id": 9435359,
    "sibling_ids": [
      145887,
      9435359,
      9435360,
      9435361
    ],
    "absolute_url": "/opinion/145887/arizona-v-gant/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "556 U.S. 332",
      "volume": "556",
      "reporter": "U.S.",
      "page": "332",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "129 S. Ct. 1710",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "1710",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 485",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "485",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 3120",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "3120",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "556 U.S. 332",
        "volume": "556",
        "reporter": "U.S.",
        "page": "332",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 1710",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "1710",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 485",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "485",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 3120",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "3120",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "556 U.S. 332",
    "official_selection": {
      "court_class": "scotus",
      "selected": "556 U.S. 332",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-351",
      "page": null,
      "quote": "--- # Arizona v. Gant *556 U.S. 332 (2009)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gant was arrested for driving on a suspended license. After he was handcuffed and locked in the back of a patrol car, officers searched his car and found cocaine in a jacket on the back seat. He moved to suppress the cocaine as the product of an unlawful search incident to arrest. ## Issue Whether police may search the passenger compartment of a vehicle incident to a recent occupant's arrest when the arrestee has been secured and cannot reach the vehicle, and there is no reason to believe the vehicle contains evidence of the offense of arrest. ## Rule A vehicle search incident to a recent occupant's arrest is allowed only on one of two independent justifications:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2009-04-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Arizona v. Gant",
    "varies_by_point": false,
    "scope_note": "Gant itself cabins the broad reading of New York v. Belton; Gant is good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Minnesota v. Raenard Romalle Douglas",
          "cluster_id": 10129058,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Williams",
          "cluster_id": 10027459,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Silvelo",
          "cluster_id": 4796646,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane1_negative"
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
        "journal_ref": "Arizona v. Gant:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Alleyne v. United States",
          "cluster_id": 903985,
          "cite": [
            "186 L. Ed. 2d 314",
            "133 S. Ct. 2151",
            "2013 U.S. LEXIS 4543",
            "570 U.S. 99",
            "81 U.S.L.W. 4444",
            "24 Fla. L. Weekly Fed. S 310",
            "2013 WL 2922116"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
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
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
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
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
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
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
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
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kisor v. Wilkie",
          "cluster_id": 4632953,
          "cite": [
            "588 U.S. 558",
            "139 S. Ct. 2400",
            "204 L. Ed. 2d 841",
            "2019 U.S. LEXIS 4397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
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
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Janus v. State, County, and Municipal Employees",
          "cluster_id": 4511640,
          "cite": [
            "585 U.S. 878",
            "138 S. Ct. 2448",
            "201 L. Ed. 2d 924",
            "2018 U.S. LEXIS 4028"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Manigan",
          "cluster_id": 1031401,
          "cite": [
            "592 F.3d 621",
            "2010 U.S. App. LEXIS 1713",
            "2010 WL 298031"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rocha",
          "cluster_id": 4345763,
          "cite": [
            "295 Neb. 716",
            "890 N.W.2d 178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Allen",
          "cluster_id": 4673511,
          "cite": [
            "2019 CO 88"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bailey v. United States",
          "cluster_id": 820749,
          "cite": [
            "185 L. Ed. 2d 19",
            "133 S. Ct. 1031",
            "568 U.S. 186",
            "2013 U.S. LEXIS 1075"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Utah v. Strieff",
          "cluster_id": 3214882,
          "cite": [
            "579 U.S. 232",
            "195 L. Ed. 2d 400",
            "2016 U.S. LEXIS 3926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. Virginia",
          "cluster_id": 4501697,
          "cite": [
            "584 U.S. 586",
            "138 S. Ct. 1663",
            "201 L. Ed. 2d 9",
            "2018 U.S. LEXIS 3210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heller v. District of Columbia",
          "cluster_id": 614652,
          "cite": [
            "670 F.3d 1244",
            "399 U.S. App. D.C. 314",
            "2011 U.S. App. LEXIS 20130",
            "2011 WL 4551558"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Byrd v. United States",
          "cluster_id": 4497658,
          "cite": [
            "584 U.S. 395",
            "138 S. Ct. 1518",
            "200 L. Ed. 2d 805",
            "2018 U.S. LEXIS 2803"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. William L. Witt(074468)",
          "cluster_id": 2993869,
          "cite": [
            "223 N.J. 409",
            "126 A.3d 850",
            "2015 N.J. LEXIS 890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
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
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Swick",
          "cluster_id": 891802,
          "cite": [
            "2012 NMSC 18",
            "2 N.M. 30",
            "2012 NMSC 018"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
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
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
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
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramos v. Louisiana",
          "cluster_id": 4746633,
          "cite": [
            "590 U.S. 83"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145887 OR 9435359 OR 9435360 OR 9435361) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTg1ODcyMDAwMDAwJnM9MTAwMjEwMTAmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145887+OR+9435359+OR+9435360+OR+9435361%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(145887 OR 9435359 OR 9435360 OR 9435361)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTQmcz0yNjgxODE4JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28145887+OR+9435359+OR+9435360+OR+9435361%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145887 OR 9435359 OR 9435360 OR 9435361)",
        "reviewed": 117,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 117,
        "triage_read": 2,
        "triage_snippet_classified": 115
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145887 OR 9435359 OR 9435360 OR 9435361)",
    "indexed_citing_opinions": 1426,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145887,
        "count": 1166,
        "count_source": "search"
      },
      {
        "opinion_id": 9435359,
        "count": 280,
        "count_source": "search"
      },
      {
        "opinion_id": 9435360,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9435361,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2728,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/arizona-v-gant.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNDc0MjUmcz0xMDM1MjEwNCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145887+OR+9435359+OR+9435360+OR+9435361%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145887,
        "cited_id": 30547,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 101894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 106447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 111600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 112296,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 112384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 112643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 118250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 130160,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 134735,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 134746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 145630,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 145701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 145814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 195782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 498214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 520415,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 593396,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 719587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 721372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 762479,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 789343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 791442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 792893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 794927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 867371,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 1057451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 1195099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 1223809,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 1234081,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 1399986,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 1401546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 1427013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 1983319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 2009627,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 2080120,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 2112994,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 2221553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 2598312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 2620702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 5538778,
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
    "date_created": "2026-07-04T18:20:38Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:20:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:20:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:25:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:20:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Arizona v. Gant

```
<opinion type="majority">
<author id="b435-4"><page-number citation-index="1" label="335">*335</page-number>Justice Stevens</author>
<p id="AEK">delivered the opinion of the Court.</p>
<p id="b435-5">After Rodney Gant was arrested for driving with a suspended license, handcuffed, and locked in the back of a patrol car, police officers searched his car and discovered cocaine in the pocket of a jacket on the backseat. Because Gant could not have accessed his ear to retrieve weapons or evidence at the time of the search, the Arizona Supreme Court held that the search-incident-to-arrest exception to the Fourth Amendment’s warrant requirement, as defined in <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), and applied to vehicle searches in <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981), did not justify the search in this case. We agree with that conclusion.</p>
<p id="b435-6">Under <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>, </em>police may search incident to arrest only the space within an arrestee’s “ ‘immediate control,’ ” meaning “the area from within which he might gain possession of a weapon or destructible evidence.” <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span>. The safety and evidentiary justifications underlying Chimel's reaching-distance rule determine <em>Belton's </em>scope. Accordingly, we hold that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>does not authorize a vehicle search incident to a recent occupant’s arrest after the arrestee has been secured and cannot access the interior of the vehicle. Consistent with the holding in <em>Thornton </em>v. <em>United States, </em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">541 U. S. 615</a></span> (2004), and following the suggestion in Justice Scalia’s opinion concurring in the judgment in that case, <span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/#632" aria-description="Citation for case: Thornton v. United States"><em>id., </em>at 632</a></span>, we also conclude that circumstances unique to the automobile context justify a search incident to arrest when it is reasonable to believe that evidence of the offense of arrest might be found in the vehicle.</p>
<p id="b435-7">I</p>
<p id="b435-8">On August 25, 1999, acting on an anonymous tip that the residence at 2524 North Walnut Avenue was being used to sell drugs, Tucson police officers Griffith and Reed knocked on the front door and asked to speak to the owner. Gant answered the door and, after identifying himself, stated that <page-number citation-index="1" label="336">*336</page-number>he expected the owner to return later. The officers left the residence and conducted a records check, which revealed that Gant’s driver’s license had been suspended and there was an outstanding warrant for his arrest for driving with a suspended license.</p>
<p id="b436-5">When the officers returned to the house that evening, they found a man near the back of the house and a woman in a car parked in front of it. After a third officer arrived, they arrested the man for providing a false name and the woman for possessing drug paraphernalia. Both arrestees were handcuffed and secured in separate patrol cars when Gant arrived. The officers recognized his car as it entered the driveway, and Officer Griffith confirmed that Gant was the driver by shining a flashlight into the car as it drove by him. Gant parked at the end of the driveway, got out of his car, and shut the door. Griffith, who was about 30 feet away, called to Gant, and they approached each other, meeting 10-to-12 feet from Gant’s car. Griffith immediately arrested Gant and handcuffed him.</p>
<p id="b436-6">Because the other arrestees were secured in the only patrol cars at the scene, Griffith called for backup. When two more officers arrived, they locked Gant in the backseat of their vehicle. After Gant had been handcuffed and placed in the back of a patrol car, two officers searched his car: One of them found a gun, and the other discovered a bag of cocaine in the pocket of a jacket on the backseat.</p>
<p id="b436-7">Gant was charged with two offenses — possession of a narcotic drug for sale and possession of drug paraphernalia (1 <em>e., </em>the plastic bag in which the cocaine was found). He moved to suppress the evidence seized from his car on the ground that the warrantless search violated the Fourth Amendment. Among other things, Gant argued that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>did not authorize the search of his vehicle because he posed no threat to the officers after he was handcuffed in the patrol car and because he was arrested for a traffic offense for which no evidence could be found in his vehicle. When asked at the <page-number citation-index="1" label="337">*337</page-number>suppression hearing why the search was conducted, Officer Griffith responded: “Because the law says we can do it.” App. 75.</p>
<p id="b437-5">The trial court rejected the State’s contention that the officers had probable cause to search Gant’s car for contraband when the search began, <em>id., </em>at 18, 30, but it denied the motion to suppress. Relying on the fact that the police saw Gant commit the crime of driving without a license and apprehended him only shortly after he exited his ear, the court held that the search was permissible as a search incident to arrest. <em>Id., </em>at 37. A jury found Gant guilty on both drug counts, and he was sentenced to a 3-year term of imprisonment.</p>
<p id="b437-6">After protracted state-court proceedings, the Arizona Supreme Court concluded that the search of Gant’s car was unreasonable within the meaning of the Fourth Amendment. The court’s opinion discussed at length our decision in <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>, </em>which held that police may search the passenger compartment of a vehicle and any containers therein as a contemporaneous incident of an arrest of the vehicle’s recent occupant. <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#3" aria-description="Citation for case: State v. Gant">216 Ariz. 1, 3-4</a></span>, 162 R 3d 640, 642-643 (2007) (citing <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460</a></span>). The court distinguished <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>as a case concerning the permissible scope of a vehicle search incident to arrest and concluded that it did not answer “the threshold question whether the police may conduct a search incident to arrest at all once the scene is secure.” <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#4" aria-description="Citation for case: State v. Gant">216 Ariz., at 4</a></span>, 162 R 3d, at 643. Relying on our earlier decision in <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>, </em>the court observed that the search-ineident-toarrest exception to the warrant requirement is justified by interests in officer safety and evidence preservation. <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#4" aria-description="Citation for case: State v. Gant">216 Ariz., at 4</a></span>,<span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#643" aria-description="Citation for case: State v. Gant">162 P. 3d, at 643</a></span>. When “the justifications underlying <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>no longer exist because the scene is secure and the arrestee is handcuffed, secured in the back of a patrol ear, and under the supervision of an officer,” the court concluded, a “warrantless search of the arrestee’s car cannot be justified as necessary to protect the officers at the scene or <page-number citation-index="1" label="338">*338</page-number>prevent the destruction of evidence.” <em>Id., </em>at 5,<span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#644" aria-description="Citation for case: State v. Gant">162 P. 3d, at 644</a></span>. Accordingly, the court held that the search of Gant’s ear was unreasonable.</p>
<p id="b438-5">The dissenting justices would have upheld the search of Gant's car based on their view that “the validity of a <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>search . . . clearly does not depend on the presence of the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>rationales in a particular case.” <em>Id., </em>at 8, <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#647" aria-description="Citation for case: State v. Gant">162 P. 3d, at 647</a></span>. Although they disagreed with the majority’s view of <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>, </em>the dissenting justices acknowledged that “[t]he bright-line rule embraced in <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>has long been criticized and probably merits reconsideration.” <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#10" aria-description="Citation for case: State v. Gant">216 Ariz., at 10</a></span>, <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#649" aria-description="Citation for case: State v. Gant">162 P. 3d, at 649</a></span>. They thus “add[ed their] voice[s] to the others that have urged the Supreme Court to revisit Belton.” <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#11" aria-description="Citation for case: State v. Gant"><em>Id., </em>at 11</a></span>, <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#650" aria-description="Citation for case: State v. Gant">162 P. 3d, at 650</a></span>.</p>
<p id="b438-6">The chorus that has called for us to revisit <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>includes courts, scholars, and Members of this Court who have questioned that decision’s clarity and its fidelity to Fourth Amendment principles. We therefore granted the State’s petition for certiorari. <span class="citation no-link">552 U. S. 1230</span> (2008).</p>
<p id="b438-7">II</p>
<p id="b438-8">Consistent with our precedent, our analysis begins, as it should in every case addressing the reasonableness of a warrantless search, with the basic rule that “searches conducted outside the judicial process, without prior approval by judge or magistrate, are <em>per se </em>unreasonable under the Fourth Amendment — subject only to a few specifically established and well-delineated exceptions.” <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (1967) (footnote omitted). Among the exceptions to the warrant requirement is a search incident to a lawful arrest. See <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span> (1914). The exception derives from interests in officer safety and evidence preservation that are typically implicated in arrest situations. See <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#230" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 230-234</a></span> (1973); <em>Chimel, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span>.</p>
<p id="b439-4"><page-number citation-index="1" label="339">*339</page-number>In <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>, </em>we held that a search incident to arrest may only include “the arrestee’s person and the area ‘within his immediate control’ — construing that phrase to mean the area from within which he might gain possession of a weapon or destructible evidence.” <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Ibid.</a></span> </em>That limitation, which continues to define the boundaries of the exception, ensures that the scope of a search incident to arrest is commensurate with its purposes of protecting arresting officers and safeguarding any evidence of the offense of arrest that an arrestee might conceal or destroy. See <em>ibid, </em>(noting that searches incident to arrest are reasonable <em>“in order to </em>remove any weapons [the arrestee] might seek to use” and <em>“in order to prevent </em>[the] concealment or destruction” of evidence (emphasis added)). If there is no possibility that an arrestee could reach into the area that law enforcement officers seek to search, both justifications for the search-incident-to-arrest exception are absent and the rule does not apply. <em>E. g., Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367-368</a></span> (1964).</p>
<p id="b439-5">In <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>, </em>we considered ChimeVs application to the automobile context. A lone police officer in that case stopped a speeding car in which Belton was one of four occupants. While asking for the driver’s license and registration, the officer smelled burnt marijuana and observed an envelope on the car floor marked “Supergold” — a name he associated with marijuana. Thus having probable cause to believe the occupants had committed a drug offense, the officer ordered them out of the vehicle, placed them under arrest, and patted them down. Without handcuffing the arrestees,<footnotemark>1</footnotemark> the officer “ ‘split them up into four separate areas of the Thruway ... so they would not be in physical touching area of each other’ ” and searched the vehicle, including the pocket of a jacket on the backseat, in which he found cocaine. <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#456" aria-description="Citation for case: New York v. Belton">453 U. S., at 456</a></span>.</p>
<p id="b440-4"><page-number citation-index="1" label="340">*340</page-number>The New York Court of Appeals found the search unconstitutional, concluding that after the occupants were arrested the vehicle and its contents were “safely within the exclusive custody and control of the police.” <em>State </em>v. <em>Belton, </em>50 N. Y. 2d 447, 452, <span class="citation" data-id="5533089"><a href="/opinion/5684296/people-v-belton/#423" aria-description="Citation for case: People v. Belton">407 N. E. 2d 420, 423</a></span> (1980). The State asked this Court to consider whether the exception recognized in <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>permits an officer to search “a jacket found inside an automobile while the automobile’s four occupants, all under arrest, are standing unsecured around the vehicle.” Brief in No. 80-328, p. <em>i. </em>We granted certiorari because “courts ha[d] found no workable definition of ‘the area within the immediate control of the arrestee’ when that area arguably includes the interior of an automobile.” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460</a></span>.</p>
<p id="b440-5">In its brief, the State argued that the Court of Appeals erred in concluding that the jacket was under the officer’s exclusive control. Focusing on the number of arrestees and their proximity to the vehicle, the State asserted that it was reasonable for the officer to believe the arrestees could have accessed the vehicle and its contents, making the search permissible under <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>. </em>Brief in No. 80-328, at 7-8. The United States, as <em>amicus curiae </em>in support of the State, argued for a more permissive standard, but it maintained that any search incident to arrest must be “ ‘substantially contemporaneous’ ” with the arrest — a requirement it deemed “satisfied if the search occurs during the period in which the arrest is being consummated and before the situation has so stabilized that it could be said that the arrest was completed.” Brief for United States as <em>Amicus Curiae </em>in <em>New York </em>v. <em>Belton, </em>O. T. 1980, No. 80-328, p. 14. There was no suggestion by the parties or <em>amici </em>that <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>authorizes a vehicle search incident to arrest when there is no realistic possibility that an arrestee could access his vehicle.</p>
<p id="b440-6">After considering these arguments, we held that when an officer lawfully arrests “the occupant of an automobile, he may, as a contemporaneous incident of that arrest, search the <page-number citation-index="1" label="341">*341</page-number>passenger compartment of the automobile” and any containers therein. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460</a></span> (footnote omitted). That holding was based in large part on our assumption “that articles inside the relatively narrow compass of the passenger compartment of an automobile are in fact generally, even if not inevitably, within ‘the area into which an arrestee might reach.’ ” <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Ibid.</a></span></em></p>
<p id="b441-5">The Arizona Supreme Court read our decision in <em>Belton </em>as merely delineating “the proper scope of a search of the interior of an automobile” incident to an arrest, <em>id., </em>at 459. That is, <em>when </em>the passenger compartment is within an arrestee’s reaching distance, <em>Belton </em>supplies the generalization that the entire compartment and any containers therein may be reached. On that view of <em>Belton, </em>the state court concluded that the search of Gant’s car was unreasonable because Gant clearly could not have accessed his car at the time of the search. It also found that no other exception to the warrant requirement applied in this case.</p>
<p id="b441-6">Gant now urges us to adopt the reading of <em>Belton </em>followed by the Arizona Supreme Court.</p>
<p id="b441-7">Ill</p>
<p id="b441-8">Despite the textual and evidentiary support for the Arizona Supreme Court’s reading of <em>Belton, </em>our opinion has been widely understood to allow a vehicle search incident to the arrest of a recent occupant even if there is no possibility the arrestee could gain access to the vehicle at the time of the search. This reading may be attributable to Justice Brennan’s dissent in <em>Belton, </em>in which he characterized the Court’s holding as resting on the “fiction... that the interior of a car is <em>always </em>within the immediate control of an arrestee who has recently been in the car.” <em>Id., </em>at 466. Under the majority’s approach, he argued, “the result would presumably be the same even if [the officer] had handcuffed Belton and his companions in the patrol car” before conducting the search. <em>Id., </em>at 468.</p>
<p id="b442-4"><page-number citation-index="1" label="342">*342</page-number>Since we decided <em>Belton, </em>Courts of Appeals have given different answers to the question whether a vehicle must be within an arrestee’s reach to justify a vehicle search incident to arrest,<footnotemark>2</footnotemark> but Justice Brennan’s reading of the Court’s opinion has predominated. As Justice O’Connor observed, “lower court decisions seem now to treat the ability to search a vehicle incident to the arrest of a recent occupant as a police entitlement rather than as an exception justified by the twin rationales of <em>Chimel.” Thornton, </em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/#624" aria-description="Citation for case: Thornton v. United States">541 U. S., at 624</a></span> (opinion concurring in part). Justice Scalia has similarly noted that, although it is improbable that an arrestee could gain access to weapons stored in his vehicle after he has been handcuffed and secured in the backseat of a patrol car, cases allowing a search in “this precise factual scenario . . . are legion.” <span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/#628" aria-description="Citation for case: Thornton v. United States"><em>Id., </em>at 628</a></span> (opinion concurring in judgment) (collecting cases).<footnotemark>3</footnotemark> Indeed, some courts have upheld searches <page-number citation-index="1" label="343">*343</page-number>under <em>Belton </em>“even when . . . the handcuffed arrestee has already left the scene.” <span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/#628" aria-description="Citation for case: Thornton v. United States">541 U. S., at 628</a></span> (same).</p>
<p id="b443-5">Under this broad reading of <em>Belton, </em>a vehicle search would be authorized incident to every arrest of a recent occupant notwithstanding that in most cases the vehicle’s passenger compartment will not be within the arrestee’s reach at the time of the search. To read <em>Belton </em>as authorizing a vehicle search incident to every recent occupant’s arrest would thus untether the rule from the justifications underlying the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>exception — a result clearly incompatible with our statement in <em>Belton </em>that it “in no way alters the fundamental principles established in the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>case regarding the basic scope of searches incident to lawful custodial arrests.” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460, n. 3</a></span>. Accordingly, we reject this reading of <em>Belton </em>and hold that the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>rationale authorizes police to search a vehicle incident to a recent occupant’s arrest only when the arrestee is unsecured and within reaching distance of the passenger compartment at the time of the search.<footnotemark>4</footnotemark></p>
<p id="b443-6">Although it does not follow from <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>, </em>we also conclude that circumstances unique to the vehicle context justify a search incident to a lawful arrest when it is “reasonable to believe evidence relevant to the crime of arrest might be found in the vehicle.” <em>Thornton, </em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/#632" aria-description="Citation for case: Thornton v. United States">541 U. S., at 632</a></span> (Scalia, J., concurring in judgment). In many cases, as when a recent occupant is arrested for a traffic violation, there will be no reasonable basis to believe the vehicle contains relevant evidence. See, <em>e. g., Atwater </em>v. <em>Lago Vista, </em><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/#324" aria-description="Citation for case: Atwater v. City of Lago Vista">532 U. S. 318, <page-number citation-index="1" label="344">*344</page-number>324</a></span> (2001); <em>Knowles </em>v. <em>Iowa, </em><span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/#118" aria-description="Citation for case: Knowles v. Iowa">525 U. S. 113, 118</a></span> (1998). But in others, including <em>Belton </em>and <em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">Thornton</a></span>, </em>the offense of arrest will supply a basis for searching the passenger compartment of an arrestee’s vehicle and any containers therein.</p>
<p id="b444-5">Neither the possibility of access nor the likelihood of discovering offense-related evidence authorized the search in this case. Unlike in <em>Belton, </em>which involved a single officer confronted with four unsecured arrestees, the five officers in this case outnumbered the three arrestees, all of whom had been handcuffed and secured in separate patrol cars before the officers searched Gant’s car. Under those circumstances, Gant clearly was not within reaching distance of his car at the time of the search. An evidentiary basis for the search was also lacking in this case. Whereas Belton and Thornton were arrested for drug offenses, Gant was arrested for driving with a suspended license — an offense for which police could not expect to find evidence in the passenger compartment of Gant’s car. Cf. <em>Knowles, </em><span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/#118" aria-description="Citation for case: Knowles v. Iowa">525 U. S., at 118</a></span>. Because police could not reasonably have believed either that Gant could have accessed his car at the time of the search or that evidence of the offense for which he was arrested might have been found therein, the search in this case was unreasonable.</p>
<p id="b444-6">IV</p>
<p id="b444-7">The State does not seriously disagree with the Arizona Supreme Court’s conclusion that Gant could not have accessed his vehicle at the time of the search, but it nevertheless asks us to uphold the search of his vehicle under the broad reading of <em>Belton </em>discussed above. The State argues that <em>Belton </em>searches are reasonable regardless of the possibility of access in a given case because that expansive rule correctly balances law enforcement interests, including the interest in a bright-line rule, with an arrestee’s limited privacy interest in his vehicle.</p>
<p id="b444-8">For several reasons, we reject the State’s argument. First, the State seriously undervalues the privacy interests <page-number citation-index="1" label="345">*345</page-number>at stake. Although we have recognized that a motorist’s privacy interest in his vehicle is less substantial than in his home, see <em>New York </em>v. Class, <span class="citation" data-id="9430353"><a href="/opinion/111600/new-york-v-class/#112" aria-description="Citation for case: New York v. Class">475 U. S. 106, 112-113</a></span> (1986), the former interest is nevertheless important and deserving of constitutional protection, see <em>Knowles, </em><span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/#117" aria-description="Citation for case: Knowles v. Iowa">525 U. S., at 117</a></span>. It is particularly significant that <em>Belton </em>searches authorize police officers to search not just the passenger compartment but every purse, briefcase, or other container within that space. A rule that gives police the power to conduct such a search whenever an individual is caught committing a traffic offense, when there is no basis for believing evidence of the offense might be found in the vehicle, creates a serious and recurring threat to the privacy of countless individuals. Indeed, the character of that threat implicates the central concern underlying the Fourth Amendment — the concern about giving police officers unbridled discretion to rummage at will among a person’s private effects.<footnotemark>5</footnotemark></p>
<p id="b445-5">At the same time as it undervalues these privacy concerns, the State exaggerates the clarity that its reading of <em>Belton </em>provides. Courts that have read <em>Belton </em>expansively are at odds regarding how close in time to the arrest and how prox<page-number citation-index="1" label="346">*346</page-number>imate to the arrestee’s vehicle an officer’s first contact with the arrestee must be to bring the encounter within Belton’s purview<footnotemark>6</footnotemark> and whether a search is reasonable when it commences or continues after the arrestee has been removed from the scene.<footnotemark>7</footnotemark> The rule has thus generated a great deal of uncertainty, particularly for a rule touted as providing a “bright line.” See 3 LaFave §7.1(c), at 514-524.</p>
<p id="b446-5">Contrary to the State’s suggestion, a broad reading of <em>Belton </em>is also unnecessary to protect law enforcement safety and evidentiary interests. Under our view, <em>Belton </em>and <em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">Thornton</a></span> </em>permit an officer to conduct a vehicle search when an arrestee is within reaching distance of the vehicle or it is reasonable to believe the vehicle contains evidence of the offense of arrest. Other established exceptions to the warrant requirement authorize a vehicle search under additional circumstances when safety or evidentiary concerns demand. For instance, <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983), permits an officer to search a vehicle’s passenger compartment when he has reasonable suspicion that an individual, whether or not the arrestee, is “dangerous” and might access the vehi<page-number citation-index="1" label="347">*347</page-number>cle to “gain immediate control of weapons.” <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Id.,</a></span> </em>at 1049 (citing <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 21</a></span> (1968)). If there is probable cause to believe a vehicle contains evidence of criminal activity, <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#820" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 820-821</a></span> (1982), authorizes a search of any area of the vehicle in which the evidence might be found. Unlike the searches permitted by Justice Scalia’s opinion concurring in the judgment in <em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">Thornton</a></span>, </em>which we conclude today are reasonable for purposes of the Fourth Amendment, <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>allows searches for evidence relevant to offenses other than the offense of arrest, and the scope of the search authorized is broader. Finally, there may be still other circumstances in which safety or evidentiary interests would justify a search. Cf. <em>Maryland </em>v. <em>Buie, </em><span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#334" aria-description="Citation for case: Maryland v. Buie">494 U. S. 325, 334</a></span> (1990) (holding that, incident to arrest, an officer may conduct a limited protective sweep of those areas of a house in which he reasonably suspects a dangerous person may be hiding).</p>
<p id="b447-5">These exceptions together ensure that officers may search a vehicle when genuine safety or evidentiary concerns encountered during the arrest of a vehicle’s recent occupant justify a search. Construing <em>Belton </em>broadly to allow vehicle searches incident to any arrest would serve no purpose except to provide a police entitlement, and it is anathema to the Fourth Amendment to permit a warrantless search on that basis. For these reasons, we are unpersuaded by the State’s arguments that a broad reading of <em>Belton </em>would meaningfully further law enforcement interests and justify a substantial intrusion on individuals’ privacy.<footnotemark>8</footnotemark></p>
<p id="b448-4"><page-number citation-index="1" label="348">*348</page-number>V</p>
<p id="b448-5">Our dissenting colleagues argue that the doctrine of <em>stare decisis </em>requires adherence to a broad reading of <em>Belton </em>even though the justifications for searching a vehicle incident to arrest are in most cases absent.<footnotemark>9</footnotemark> The doctrine of <em>stare decisis </em>is of course “essential to the respect accorded to the judgments of the Court and to the stability of the law,” but it does not compel us to follow a past decision when its rationale no longer withstands “careful analysis.” <em>Lawrence </em>v. <em>Texas, </em><span class="citation" data-id="9434509"><a href="/opinion/130160/lawrence-v-texas/#577" aria-description="Citation for case: Lawrence v. Texas">539 U. S. 558, 577</a></span> (2003).</p>
<p id="b448-6">We have never relied on <em>stare decisis </em>to justify the continuance of an unconstitutional police practice. And we would be particularly loath to uphold an unconstitutional result in a case that is so easily distinguished from the decisions that arguably compel it. The safety and evidentiary interests that supported the search in <em>Belton </em>simply are not present in this case. Indeed, it is hard to imagine two cases that are factually more distinct, as <em>Belton </em>involved one officer confronted by four unsecured arrestees suspected of committing a drug offense, and this case involves several officers confronted with a securely detained arrestee apprehended for driving with a suspended license. This case is also distinguishable from <em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">Thornton</a></span>, </em>in which the petitioner was <page-number citation-index="1" label="349">*349</page-number>arrested for a drug offense. It is thus unsurprising that Members of this Court who concurred in the judgments in <em>Belton </em>and <em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">Thornton</a></span> </em>also concur in the decision in this case.<footnotemark>10</footnotemark></p>
<p id="b449-5">We do not agree with the contention in Justice Alito’s dissent (hereinafter dissent) that consideration of police reliance interests requires a different result. Although it appears that the State’s reading of <em>Belton </em>has been widely taught in police academies and that law enforcement officers have relied on the rule in conducting vehicle searches during the past 28 years,* <footnotemark>11</footnotemark> many of these searches were not justified by the reasons underlying the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>exception. Countless individuals guilty of nothing more serious than a traffic violation have had their constitutional right to the security of their private effects violated as a result. The fact that the law enforcement community may view the State’s version of the <em>Belton </em>rule as an entitlement does not establish the sort of reliance interest that could outweigh the countervailing interest that all individuals share in having their constitutional rights fully protected. If it is clear that a practice is unlawful, individuals’ interest in its discontinuance clearly outweighs any law enforcement “entitlement” to its persistence. Cf. <em>Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 393</a></span> (1978) (“[T]he mere fact that law enforcement may be made more efficient can never by itself justify disregard of the Fourth Amendment”). The dissent’s reference in this regard to the reliance interests cited in <em>Dickerson </em>v. <em>United States, </em><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428</a></span> (2000), is misplaced. See <em>post, </em>at 358-359. In ob<page-number citation-index="1" label="350">*350</page-number>serving that <em>“Miranda </em>has become embedded in routine police practice to the point where the warnings have become part of our national culture,” <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#443" aria-description="Citation for case: Dickerson v. United States">530 U. S., at 443</a></span>, the Court was referring not to police reliance on a rule requiring them to provide warnings but to the broader societal reliance on that individual right.</p>
<p id="b450-5">The dissent also ignores the checkered history of the search-incident-to-arrest exception. Police authority to search the place in which a lawful arrest is made was broadly asserted in <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span> (1927), and limited a few years later in <em>Go-Bart Importing Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span> (1931), and <em>United States </em>v. <em>Lefkowitz, </em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452</a></span> (1932). The limiting views expressed in <em>Go-Bart </em>and <em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">Lefkowitz</a></span> </em>were in turn abandoned in <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span> (1947), which upheld a search of a four-room apartment incident to the occupant’s arrest. Only a year later the Court in <em>Trupiano </em>v. <em>United States, </em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#708" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699, 708</a></span> (1948), retreated from that holding, noting that the search-incident-to-arrest exception is “a strictly limited” one that must be justified by “something more in the way of necessity than merely a lawful arrest.” And just two years after that, in <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span> (1950), the Court again reversed course and upheld the search of an entire apartment. Finally, our opinion in <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>overruled <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>and what remained of <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>and established the present boundaries of the search-incident-to-arrest exception. Notably, none of the dissenters in <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>or the cases that preceded it argued that law enforcement reliance interests outweighed the interest in protecting individual constitutional rights so as to warrant fidelity to an unjustifiable rule.</p>
<p id="b450-6">The experience of the 28 years since we decided <em>Belton </em>has shown that the generalization underpinning the broad reading of that decision is unfounded. We now know that articles inside the passenger compartment are rarely “within 'the area into which an arrestee might reach,’ ” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at <page-number citation-index="1" label="351">*351</page-number>460</a></span>, and blind adherence to <em>Belton’s </em>faulty assumption would authorize myriad unconstitutional searches. The doctrine of <em>stare decisis </em>does not require us to approve routine constitutional violations.</p>
<p id="b451-5">VI</p>
<p id="b451-6">Police may search a vehicle incident to a recent occupant’s arrest only if the arrestee is within reaching distance of the passenger compartment at the time of the search or it is reasonable to believe the vehicle contains evidence of the offense of arrest. When these justifications are absent, a search of an arrestee’s vehicle will be unreasonable unless police obtain a warrant or show that another exception to the warrant requirement applies. The Arizona Supreme Court correctly held that this case involved an unreasonable search. Accordingly, the judgment of the State Supreme Court is affirmed.</p>
<p id="b451-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b439-6"> The officer was unable to handcuff the occupants because he had only one set of handcuffs. See Brief for Petitioner in <em>New York </em>v. <em>Belton, </em>O. T. 1980, No. 80-328, p. 3 (hereinafter Brief in No. 80-328).</p>
</footnote>
<footnote label="2">
<p id="b442-5"> Compare <em>United States </em>v. <em>Green, </em><span class="citation" data-id="30547"><a href="/opinion/30547/united-states-v-green/#379" aria-description="Citation for case: United States v. Green">324 F. 3d 375, 379</a></span> (CA5 2003) (holding that <em>Belton </em>did not authorize a search of an arrestee’s vehicle when he was handcuffed and lying facedown on the ground surrounded by four police officers 6-to-10 feet from the vehicle), <em>United States </em>v. <em>Edwards, </em><span class="citation" data-id="6994169"><a href="/opinion/7088754/united-states-v-edwards/#938" aria-description="Citation for case: United States v. Edwards">242 F. 3d 928, 938</a></span> (CA10 2001) (finding unauthorized a vehicle search conducted while the arrestee was handcuffed in the back of a patrol car), and <em>United States </em>v. <em>Vasey, </em><span class="citation" data-id="498214"><a href="/opinion/498214/united-states-v-michael-allen-vasey/#787" aria-description="Citation for case: United States v. Michael Allen Vasey">834 F. 2d 782, 787</a></span> (CA9 1987) (finding unauthorized a vehicle search conducted 30-to-45 minutes after an arrest and after the arrestee had been handcuffed and secured in the back of a police car), with <em>United States </em>v. <em>Hrasky, </em><span class="citation" data-id="9499027"><a href="/opinion/794927/united-states-v-zachary-hrasky/#1102" aria-description="Citation for case: United States v. Zachary Hrasky">453 F. 3d 1099, 1102</a></span> (CA8 2006) (upholding a search conducted an hour after the arrestee was apprehended and after he had been handcuffed and placed in the back of a patrol car), <em>United States </em>v. <em>Weaver, </em><span class="citation" data-id="792893"><a href="/opinion/792893/united-states-v-hollie-lynn-weaver-aka-hollie-lynn-brawner-maiden/#1106" aria-description="Citation for case: United States v. Hollie Lynn Weaver, A/K/A Hollie Lynn...">433 F. 3d 1104, 1106</a></span> (CA9 2006) (upholding a search conducted 10-to-15 minutes after an arrest and after the arrestee had been handcuffed and secured in the back of a patrol car), and <em>United States </em>v. <em>White, </em><span class="citation" data-id="520415"><a href="/opinion/520415/united-states-v-james-allen-white-jr/#44" aria-description="Citation for case: United States v. James Allen White, Jr.">871 F. 2d 41, 44</a></span> (CA6 1989) (upholding a search conducted after the arrestee had been handcuffed and secured in the back of a police cruiser).</p>
</footnote>
<footnote label="3">
<p id="b442-6"> The practice of searching vehicles incident to arrest after the arrestee has been handcuffed and secured in a patrol car has not abated since we decided <em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">Thornton</a></span>. </em>See, <em>e.g., United States </em>v. <em>Murphy, </em><span class="citation" data-id="168860"><a href="/opinion/168860/united-states-v-murphy/#717" aria-description="Citation for case: United States v. Murphy">221 Fed. Appx. 715, 717</a></span> (CA10 2007); <em>Hrasky, </em><span class="citation" data-id="9499027"><a href="/opinion/794927/united-states-v-zachary-hrasky/#1100" aria-description="Citation for case: United States v. Zachary Hrasky">453 F. 3d, at 1100</a></span>; <em>Weaver, </em><span class="citation" data-id="792893"><a href="/opinion/792893/united-states-v-hollie-lynn-weaver-aka-hollie-lynn-brawner-maiden/#1105" aria-description="Citation for case: United States v. Hollie Lynn Weaver, A/K/A Hollie Lynn...">433 F. 3d, at 1105</a></span>; <em>United States </em>v. <em>Williams, </em><span class="citation" data-id="9813827"><a href="/opinion/2973559/united-states-v-williams/#401" aria-description="Citation for case: United States v. Williams">170 Fed. Appx. 399, 401</a></span> (CA6 2006); <em>United States </em>v. <em>Dorsey, </em><span class="citation" data-id="9498265"><a href="/opinion/791442/united-states-v-nikos-delano-dorsey/#1041" aria-description="Citation for case: United States v. Nikos Delano Dorsey">418 F. 3d 1038, 1041</a></span> (CA9 2005); <em>United States </em>v. <page-number citation-index="1" label="343">*343</page-number><em>Osife, </em><span class="citation" data-id="789343"><a href="/opinion/789343/united-states-v-dale-juan-osife/#1144" aria-description="Citation for case: United States v. Dale Juan Osife">398 F. 3d 1143, 1144</a></span> (CA9 2005); <em>United States </em>v. <em>Sumrall, </em><span class="citation" data-id="165144"><a href="/opinion/165144/united-states-v-sumrall/#24" aria-description="Citation for case: United States v. Sumrall">115 Fed. Appx. 22, 24</a></span> (CA10 2004).</p>
</footnote>
<footnote label="4">
<p id="b443-9"> Because officers have many means of ensuring the safe arrest of vehicle occupants, it will be the rare case in which an officer is unable to fully effectuate an arrest so that a real possibility of access to the arrestee’s vehicle remains. Cf. 3 W. LaFave, Search and Seizure § 7.1(c), p. 525 (4th ed. 2004) (hereinafter LaFave) (noting that the availability of protective measures “ensur[es] the nonexistence of circumstances in which the arrestee’s ‘control’ of the car is in doubt”). But in such a case a search incident to arrest is reasonable under the Fourth Amendment.</p>
</footnote>
<footnote label="5">
<p id="b445-6"> See <em>Maryland </em>v. <em>Garrison, </em><span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#84" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79, 84</a></span> (1987); <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#760" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 760-761</a></span> (1969); <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#480" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 480-484</a></span> (1965); <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#389" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 389-392</a></span> (1914); <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 624-625</a></span> (1886); see also 10 C. Adams, The Works of John Adams 247-248 (1856). Many have observed that a broad reading of <em>Belton </em>gives police limitless discretion to conduct exploratory searches. See 3 LaFave § 7.1(c), at 527 (observing that <em>Belton </em>creates the risk “that police will make custodial arrests which they otherwise would not make as a cover for a search which the Fourth Amendment otherwise prohibits”); see also <em>United States </em>v. <em>McLaughlin, </em><span class="citation" data-id="9491975"><a href="/opinion/762479/united-states-of-america-plaintiff-appellant-v-john-lee-mclaughlin/#894" aria-description="Citation for case: UNITED STATES of America, Plaintiff-Appellant, v. John...">170 F. 3d 889, 894</a></span> (CA9 1999) (Trott, J., concurring) (observing that <em>Belton </em>has been applied to condone “purely exploratory searches of vehicles during which officers with no definite objective or reason for the search are allowed to rummage around in a ear to see what they might find”); <em>State </em>v. <em>Pallone, </em><span class="citation" data-id="9655955"><a href="/opinion/1581652/state-v-trawitzki/#87" aria-description="Citation for case: State v. Trawitzki">2001 WI 77, ¶¶ 87-90</a></span>,<span class="citation" data-id="9739954"><a href="/opinion/2221553/state-v-pallone/#203" aria-description="Citation for case: State v. Pallone">236 Wis. 2d 162, 203-204</a></span>, and n. 9, <span class="citation" data-id="9739954"><a href="/opinion/2221553/state-v-pallone/#588" aria-description="Citation for case: State v. Pallone">613 N. W. 2d 568, 588</a></span>, and n. 9 (2000) (Abrahamson, C. J., dissenting) (same); <em>State </em>v. <em>Pierce, </em>136 N. J. 184, 211, <span class="citation" data-id="9517913"><a href="/opinion/2009627/state-v-pierce/#961" aria-description="Citation for case: State v. Pierce">642 A. 2d 947, 961</a></span> (1994) (same).</p>
</footnote>
<footnote label="6">
<p id="b446-6"> Compare <em>United States </em>v. <em>Caseres, </em><span class="citation" data-id="1234081"><a href="/opinion/1234081/united-states-v-caseres/#1072" aria-description="Citation for case: United States v. Caseres">533 F. 3d 1064, 1072</a></span> (CA9 2008) (declining to apply <em>Belton </em>when the arrestee was approached by police after he had exited his vehicle and reached his residence), with <em>Rainey </em>v. <em>Commonwealth, </em><span class="citation" data-id="9620606"><a href="/opinion/1399986/rainey-v-commonwealth/#94" aria-description="Citation for case: Rainey v. Commonwealth">197 S. W. 3d 89, 94-95</a></span> (Ky. 2006) (applying <em>Belton </em>when the arrestee was apprehended 50 feet from the vehicle), and <em>Black </em>v. <em>State, </em><span class="citation" data-id="852893"><a href="/opinion/852893/black-v-state/#716" aria-description="Citation for case: Black v. State">810 N. E. 2d 713, 716</a></span> (Ind. 2004) (applying <em>Belton </em>when the arrestee was apprehended inside an auto repair shop and the vehicle was parked outside).</p>
</footnote>
<footnote label="7">
<p id="b446-7"> Compare <em>McLaughlin, </em><span class="citation" data-id="9491975"><a href="/opinion/762479/united-states-of-america-plaintiff-appellant-v-john-lee-mclaughlin/#890" aria-description="Citation for case: UNITED STATES of America, Plaintiff-Appellant, v. John...">170 F. 3d, at 890-891</a></span> (upholding a search that commenced five minutes after the arrestee was removed from the scene), <em>United States </em>v. <em>Snook, </em><span class="citation" data-id="721372"><a href="/opinion/721372/united-states-v-wayne-steven-snook/#608" aria-description="Citation for case: United States v. Wayne Steven Snook">88 F. 3d 605, 608</a></span> (CA8 1996) (same), and <em>United States </em>v. <em>Doward, </em><span class="citation" data-id="195782"><a href="/opinion/195782/united-states-v-doward/#793" aria-description="Citation for case: United States v. Doward">41 F. 3d 789, 793</a></span> (CA1 1994) (upholding a search that continued after the arrestee was removed from the scene), with <em>United States </em>v. <em>Lugo, </em><span class="citation" data-id="593396"><a href="/opinion/593396/united-states-v-david-m-lugo/#634" aria-description="Citation for case: United States v. David M. Lugo">978 F. 2d 631, 634</a></span> (CA10 1992) (holding invalid a search that commenced after the arrestee was removed from the scene), and <em>State </em>v. <em>Badgett, </em><span class="citation" data-id="7839713"><a href="/opinion/7892532/state-v-badgett/#427" aria-description="Citation for case: State v. Badgett">200 Conn. 412, 427-428</a></span>, <span class="citation" data-id="7839713"><a href="/opinion/7892532/state-v-badgett/#169" aria-description="Citation for case: State v. Badgett">512 A. 2d 160, 169</a></span> (1986) (holding invalid a search that continued after the arrestee was removed from the scene).</p>
</footnote>
<footnote label="8">
<p id="b447-6"> At least eight States have reached the same conclusion. Vermont, New Jersey, New Mexico, Nevada, Pennsylvania, New York, Oregon, and Wyoming have declined to follow a broad reading of <em>Belton </em>under their state constitutions. See <em>State </em>v. <em>Bander, </em><span class="citation multiple-matches"><a href="/c/Vt./181/392/">181 Vt. 392</a></span>, 401, <span class="citation multiple-matches"><a href="/c/A.%202d/924/38/">924 A. 2d 38</a></span>, 46-47 (2007); <em>State </em>v. <em>Eckel, </em>185 N. J. 523, 540, <span class="citation" data-id="2112994"><a href="/opinion/2112994/state-v-eckel/#1277" aria-description="Citation for case: State v. Eckel">888 A. 2d 1266, 1277</a></span> (2006); <em>Camacho </em>v. <em>State, </em><span class="citation" data-id="9788695"><a href="/opinion/2598312/camacho-v-state/#399" aria-description="Citation for case: Camacho v. State">119 Nev. 395, 399-400</a></span>, <span class="citation" data-id="9788695"><a href="/opinion/2598312/camacho-v-state/#373" aria-description="Citation for case: Camacho v. State">75 P. 3d 370, 373-374</a></span> (2003); <em>Vasquez </em>v. <em>State, </em><span class="citation" data-id="9793472"><a href="/opinion/2615534/vasquez-v-state/#488" aria-description="Citation for case: Vasquez v. State">990 P. 2d 476, 488-489</a></span> (Wyo. 1999); <em>State </em>v. <em>Arredondo, </em><span class="citation" data-id="1223809"><a href="/opinion/1223809/state-v-arredondo/" aria-description="Citation for case: State v. Arredondo">1997-NMCA-081</a></span>, 123 N. M. 628, 636 (Ct. App.), overruled on other grounds by <em>State </em>v. <em>Steinzig, </em><span class="citation" data-id="1401546"><a href="/opinion/1401546/state-v-steinzig/" aria-description="Citation for case: State v. Steinzig">1999-NMCA-107</a></span>, 127 N. M. 752 (Ct. App.); <page-number citation-index="1" label="348">*348</page-number><em>Commonwealth </em>v. <em>White, </em><span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/#57" aria-description="Citation for case: Commonwealth v. White">543 Pa. 45, 57</a></span>, <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/#902" aria-description="Citation for case: Commonwealth v. White">669 A. 2d 896, 902</a></span> (1995); <em>People </em>v. <em>Blasich, </em>73 N. Y. 2d 673, 678, <span class="citation" data-id="5538778"><a href="/opinion/5689505/people-v-blasich/#43" aria-description="Citation for case: People v. Blasich">541 N. E. 2d 40, 43</a></span> (1989); <em>State </em>v. <em>Fesler, </em><span class="citation" data-id="9627414"><a href="/opinion/1427013/state-v-fesler/#612" aria-description="Citation for case: State v. Fesler">68 Ore. App. 609, 612</a></span>, <span class="citation" data-id="9627414"><a href="/opinion/1427013/state-v-fesler/#1016" aria-description="Citation for case: State v. Fesler">685 P. 2d 1014, 1016-1017</a></span> (1984). And a Massachusetts statute provides that a search incident to arrest may be made only for the purposes of seizing weapons or evidence of the offense of arrest. See <em>Commonwealth </em>v. <em>Toole, </em><span class="citation" data-id="2080120"><a href="/opinion/2080120/commonwealth-v-toole/#161" aria-description="Citation for case: Commonwealth v. Toole">389 Mass. 159, 161-162</a></span>, <span class="citation" data-id="2080120"><a href="/opinion/2080120/commonwealth-v-toole/#1266" aria-description="Citation for case: Commonwealth v. Toole">448 N. E. 2d 1264, 1266-1267</a></span> (1983) (citing Mass. Gen. Laws, ch. 276, § 1 (West 2006)).</p>
</footnote>
<footnote label="9">
<p id="b448-14"> Justice Auto’s dissenting opinion also accuses us of “overruling]” <em>Belton </em>and <em>Thornton </em>v. <em>United States, </em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">541 U. S. 615</a></span> (2004), “even though respondent Gant has not asked us to do so.” <em>Post, </em>at 355. Contrary to that claim, the narrow reading of <em>Belton </em>we adopt today is precisely the result Gant has urged. That Justice Auto has chosen to describe this decision as overruling our earlier cases does not change the fact that the resulting rule of law is the one advocated by respondent.</p>
</footnote>
<footnote label="10">
<p id="b449-6"> Justice Stevens concurred in the judgment in <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#463" aria-description="Citation for case: New York v. Belton">453 U. S., at 463</a></span>, for the reasons stated in his dissenting opinion in <em>Robbins </em>v. <em>California, </em><span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#444" aria-description="Citation for case: Robbins v. California">453 U. S. 420, 444</a></span> (1981), Justice Thomas joined the Court’s opinion in <em>Thornton, </em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">541 U. S. 615</a></span>, and Justice Scaua and Justice Ginsburg concurred in the judgment in that case, <span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/#625" aria-description="Citation for case: Thornton v. United States"><em>id., </em>at 625</a></span>.</p>
</footnote>
<footnote label="11">
<p id="b449-7"> Because a broad reading of <em>Belton </em>has been widely accepted, the doctrine of qualified immunity will shield officers from liability for searches conducted in reasonable reliance on that understanding.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Arizona v. Johnson.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Arizona v. Johnson"
type: case
citation: "555 U.S. 323 (2009)"
parallel_cite: "129 S. Ct. 781; 172 L. Ed. 2d 694"
neutral_cite: 2009 U.S. LEXIS 868
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-01-26
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2009-01-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Arizona v. Johnson
  varies_by_point: false
  scope_note: "Good law. During a lawful traffic stop every occupant is seized for the stop's duration, so the first Terry condition is satisfied without separate suspicion that a passenger is committing a crime; to frisk that passenger the officer needs reasonable suspicion the passenger is armed and dangerous."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145912/arizona-v-johnson/"
  cluster_id: 145912
  opinion_id: 145912
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Progeny"
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Related (cross-doctrine)"
related: ["[[Terry v. Ohio]]", "[[Brendlin v. California]]", "[[Maryland v. Wilson]]", "[[Pennsylvania v. Mimms]]"]
aliases: []
tags: ["case", "fourth-amendment", "traffic-stop", "frisk", "passenger", "terry-stop"]
holding: "During a lawful traffic stop, a passenger is seized for the duration of the stop (satisfying Terry's first condition without separate suspicion of the passenger's criminal activity); an officer may frisk the passenger on reasonable suspicion that the passenger is armed and dangerous."
lake:
  record_id: Arizona v. Johnson
  status: verified
  projected_at: 2026-07-06
---

# Arizona v. Johnson

*555 U.S. 323 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Members of an Arizona gang task force stopped a car near a Crips neighborhood in Tucson after a plate check showed the registration was suspended — a civil infraction warranting only a citation. The car had three occupants, including back-seat passenger Lemon Johnson. Officer Trevizo learned that Johnson was from a town with a Crips gang, had a police scanner in his jacket, and gave answers suggesting gang affiliation. Suspecting he was armed, she had him step out and patted him down, finding a gun. Johnson was convicted of unlawful gun possession; the Arizona Court of Appeals reversed, reasoning that because the encounter had become consensual and Johnson was not suspected of separate criminal activity, the frisk was unlawful.

## Issue
Whether, during a lawful traffic stop, an officer may frisk a passenger for weapons when the officer has reasonable suspicion the passenger is armed and dangerous but lacks suspicion that the passenger is independently engaged in criminal activity.

## Rule
Yes. A *[[Terry v. Ohio|Terry]]* stop and frisk requires two things: "The Court upheld 'stop and frisk' as constitutionally permissible if two conditions are met. First, the investigatory stop must be lawful. . . . Second, to proceed from a stop to a frisk, the police officer must reasonably suspect that the person stopped is armed and dangerous." — 555 U.S. at 326–327. ^pin-326

In the traffic-stop setting both conditions are satisfied on the stop alone plus armed-and-dangerous suspicion: "in a traffic-stop setting, the first *Terry* condition — a lawful investigatory stop — is met whenever it is lawful for police to detain an automobile and its occupants pending inquiry into a vehicular violation. The police need not have, in addition, cause to believe any occupant of the vehicle is involved in criminal activity. To justify a patdown of the driver or a passenger during a traffic stop, however, just as in the case of a pedestrian reasonably suspected of criminal activity, the police must harbor reasonable suspicion that the person subjected to the frisk is armed and dangerous." — *Id.* at 327. ^pin-327

That is so because "[f]or the duration of a traffic stop, . . . a police officer effectively seizes 'everyone in the vehicle,' the driver and all passengers." — *Id.* (quoting *Brendlin v. California*). ^pin-327b

## Application
The task-force officers lawfully stopped the car for a registration violation, and that stop seized all of its occupants — including Johnson — for its duration. Johnson therefore remained lawfully detained even though the officers had no suspicion he was independently committing a crime; the encounter had not become a consensual one merely because he was cooperative. Because Trevizo developed reasonable suspicion that Johnson was armed and dangerous (gang indicia, a scanner, evasive gang-related answers), she was entitled to pat him down for weapons. The Court reversed the Arizona Court of Appeals and [[Reading and Citing Cases#on-remand|remanded]], leaving the appeals court free to revisit whether Trevizo in fact had reasonable suspicion that Johnson was armed — a point that court had only assumed.

## Conclusion
The frisk did not require separate suspicion that the passenger was engaged in criminal activity; a lawful traffic stop seizes the passenger, and the frisk is justified by reasonable suspicion the passenger is armed and dangerous. Reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Johnson* confirms and combines [[Pennsylvania v. Mimms]], [[Maryland v. Wilson]], and [[Brendlin v. California]] for the traffic-stop context and applies the frisk standard of [[Terry v. Ohio]] to passengers.

## Appears on
- [[Traffic Stops]] — *Progeny*
- [[Terry Stops and Reasonable Suspicion]] — *Related (cross-doctrine)*

## Sources
- *Arizona v. Johnson*, 555 U.S. 323 (2009) — https://www.courtlistener.com/opinion/145912/arizona-v-johnson/ — pinpoints: 326–327.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "48342b44a7dac19a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Arizona v. Johnson"}, "payload": {"all": [{"cite": "555 U.S. 323", "page": "323", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "555"}, {"cite": "129 S. Ct. 781", "page": "781", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "129"}, {"cite": "172 L. Ed. 2d 694", "page": "694", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "172"}, {"cite": "2009 U.S. LEXIS 868", "page": "868", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2009"}], "display": "555 U.S. 323", "official": {"cite": "555 U.S. 323", "page": "323", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "555"}, "official_selection_present": true, "record_id": "Arizona v. Johnson"}}
{"assertion_id": "21380b1679d852e3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-327b", "record_id": "Arizona v. Johnson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-327b", "pinpoint_status": "slip-only", "quote": "[f]or the duration of a traffic stop, . . . a police officer effectively seizes 'everyone in the vehicle,' the driver and all passengers.", "quote_fidelity": "mismatch", "record_id": "Arizona v. Johnson", "star_marker": null}}
{"assertion_id": "2e8c572896556963", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-326", "record_id": "Arizona v. Johnson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-326", "pinpoint_status": "slip-only", "quote": "--- # Arizona v. Johnson *555 U.S. 323 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Members of an Arizona gang task force stopped a car near a Crips neighborhood in Tucson after a plate check showed the registration was suspended — a civil infraction warranting only a citation. The car had three occupants, including back-seat passenger Lemon Johnson. Officer Trevizo learned that Johnson was from a town with a Crips gang, had a police scanner in his jacket, and gave answers suggesting gang affiliation. Suspecting he was armed, she had him step out and patted him down, finding a gun. Johnson was convicted of unlawful gun possession; the Arizona Court of Appeals reversed, reasoning that because the encounter had become consensual and Johnson was not suspected of separate criminal activity, the frisk was unlawful. ## Issue Whether, during a lawful traffic stop, an officer may frisk a passenger for weapons when the officer has reasonable suspicion the passenger is armed and dangerous but lacks suspicion that the passenger is independently engaged in criminal activity. ## Rule Yes. A *Terry* stop and frisk requires two things:", "quote_fidelity": "mismatch", "record_id": "Arizona v. Johnson", "star_marker": null}}
{"assertion_id": "e6bbfadcb4d5bf86", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-327", "record_id": "Arizona v. Johnson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-327", "pinpoint_status": "slip-only", "quote": "in a traffic-stop setting, the first *Terry* condition — a lawful investigatory stop — is met whenever it is lawful for police to detain an automobile and its occupants pending inquiry into a vehicular violation. The police need not have, in addition, cause to believe any occupant of the vehicle is involved in criminal activity. To justify a patdown of the driver or a passenger during a traffic stop, however, just as in the case of a pedestrian reasonably suspected of criminal activity, the police must harbor reasonable suspicion that the person subjected to the frisk is armed and dangerous.", "quote_fidelity": "mismatch", "record_id": "Arizona v. Johnson", "star_marker": null}}
{"assertion_id": "72acb5231045fae3", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Arizona v. Johnson"}, "payload": {"as_of_content": "2009-01-26", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Arizona v. Johnson", "scope_note": "Good law. During a lawful traffic stop every occupant is seized for the stop's duration, so the first Terry condition is satisfied without separate suspicion that a passenger is committing a crime; to frisk that passenger the officer needs reasonable suspicion the passenger is armed and dangerous.", "varies_by_point": false}}
```

### lake record — Arizona v. Johnson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arizona v. Johnson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Arizona v. Johnson",
    "case_name_short": "",
    "case_name_full": "Arizona v. Johnson",
    "input_case_name": "Arizona v. Johnson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-01-26",
    "year": 2009,
    "docket": null,
    "cluster_id": 145912,
    "lead_opinion_id": 145912,
    "sibling_ids": [
      145912
    ],
    "absolute_url": "/opinion/145912/arizona-v-johnson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "555 U.S. 323",
      "volume": "555",
      "reporter": "U.S.",
      "page": "323",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "129 S. Ct. 781",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "781",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "172 L. Ed. 2d 694",
        "volume": "172",
        "reporter": "L. Ed. 2d",
        "page": "694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 868",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "868",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "555 U.S. 323",
        "volume": "555",
        "reporter": "U.S.",
        "page": "323",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 781",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "781",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "172 L. Ed. 2d 694",
        "volume": "172",
        "reporter": "L. Ed. 2d",
        "page": "694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 868",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "868",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "555 U.S. 323",
    "official_selection": {
      "court_class": "scotus",
      "selected": "555 U.S. 323",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-326",
      "page": null,
      "quote": "--- # Arizona v. Johnson *555 U.S. 323 (2009)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Members of an Arizona gang task force stopped a car near a Crips neighborhood in Tucson after a plate check showed the registration was suspended \u2014 a civil infraction warranting only a citation. The car had three occupants, including back-seat passenger Lemon Johnson. Officer Trevizo learned that Johnson was from a town with a Crips gang, had a police scanner in his jacket, and gave answers suggesting gang affiliation. Suspecting he was armed, she had him step out and patted him down, finding a gun. Johnson was convicted of unlawful gun possession; the Arizona Court of Appeals reversed, reasoning that because the encounter had become consensual and Johnson was not suspected of separate criminal activity, the frisk was unlawful. ## Issue Whether, during a lawful traffic stop, an officer may frisk a passenger for weapons when the officer has reasonable suspicion the passenger is armed and dangerous but lacks suspicion that the passenger is independently engaged in criminal activity. ## Rule Yes. A *Terry* stop and frisk requires two things:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-327",
      "page": null,
      "quote": "in a traffic-stop setting, the first *Terry* condition \u2014 a lawful investigatory stop \u2014 is met whenever it is lawful for police to detain an automobile and its occupants pending inquiry into a vehicular violation. The police need not have, in addition, cause to believe any occupant of the vehicle is involved in criminal activity. To justify a patdown of the driver or a passenger during a traffic stop, however, just as in the case of a pedestrian reasonably suspected of criminal activity, the police must harbor reasonable suspicion that the person subjected to the frisk is armed and dangerous.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-327b",
      "page": null,
      "quote": "[f]or the duration of a traffic stop, . . . a police officer effectively seizes 'everyone in the vehicle,' the driver and all passengers.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2009-01-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Arizona v. Johnson",
    "varies_by_point": false,
    "scope_note": "Good law. During a lawful traffic stop every occupant is seized for the stop's duration, so the first Terry condition is satisfied without separate suspicion that a passenger is committing a crime; to frisk that passenger the officer needs reasonable suspicion the passenger is armed and dangerous.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Iowa v. Juan Daniel Salcedo",
          "cluster_id": 4678847,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Juan Daniel Salcedo",
          "cluster_id": 4677110,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane1_negative"
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
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manuel De Jesus Ortega Melendr v. Joseph M. Arpaio",
          "cluster_id": 809224,
          "cite": [
            "695 F.3d 990",
            "2012 WL 4358727",
            "2012 U.S. App. LEXIS 20120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gonzalez Ex Rel. Gonzalez v. City of Anaheim",
          "cluster_id": 2658912,
          "cite": [
            "747 F.3d 789",
            "2014 WL 1274551",
            "2014 U.S. App. LEXIS 5895"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Harmon",
          "cluster_id": 4670342,
          "cite": [
            "2019 COA 156"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kelly v. Borough of Carlisle",
          "cluster_id": 176451,
          "cite": [
            "622 F.3d 248",
            "38 Media L. Rep. (BNA) 2473",
            "2010 U.S. App. LEXIS 20430",
            "2010 WL 3835209"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Castleberry",
          "cluster_id": 2282066,
          "cite": [
            "332 S.W.3d 460",
            "2011 Tex. Crim. App. LEXIS 283",
            "2011 WL 709697"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Hicks, M., Aplt.",
          "cluster_id": 4625130,
          "cite": [
            "208 A.3d 916"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lewis",
          "cluster_id": 626016,
          "cite": [
            "674 F.3d 1298",
            "2012 WL 967969"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Decarlos George",
          "cluster_id": 1085503,
          "cite": [
            "732 F.3d 296",
            "2013 WL 5630234",
            "2013 U.S. App. LEXIS 20902"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dancy v. McGinley",
          "cluster_id": 4327925,
          "cite": [
            "843 F.3d 93",
            "2016 U.S. App. LEXIS 21753",
            "2016 WL 7118403"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Colyar",
          "cluster_id": 2643140,
          "cite": [
            "2013 IL 111835"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. White",
          "cluster_id": 172784,
          "cite": [
            "584 F.3d 935",
            "2009 U.S. App. LEXIS 23296",
            "2009 WL 3381528"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vinton",
          "cluster_id": 187527,
          "cite": [
            "594 F.3d 14",
            "389 U.S. App. D.C. 199",
            "2010 U.S. App. LEXIS 2450",
            "2010 WL 392347"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Liberal v. Estrada",
          "cluster_id": 183026,
          "cite": [
            "632 F.3d 1064",
            "2011 U.S. App. LEXIS 957",
            "2011 WL 149348"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Mark Dunbar (077839) (Monmouth and Statewide",
          "cluster_id": 4407425,
          "cite": [
            "229 N.J. 521",
            "163 A.3d 875",
            "2017 WL 2962256",
            "2017 N.J. LEXIS 747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Cochrane",
          "cluster_id": 814022,
          "cite": [
            "702 F.3d 334",
            "2012 U.S. App. LEXIS 25980"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Palmer",
          "cluster_id": 3196774,
          "cite": [
            "820 F.3d 640",
            "2016 WL 1594793"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gomez",
          "cluster_id": 8443636,
          "cite": [
            "877 F.3d 76"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estrada v. Rhode Island",
          "cluster_id": 204167,
          "cite": [
            "594 F.3d 56",
            "102 A.L.R. 6th 845",
            "2010 U.S. App. LEXIS 2390",
            "2010 WL 376978"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145912) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTU3OTY0ODAwMDAwJnM9NDYyMDQyMiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145912%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      },
      "lane2_top_cited": {
        "query": "cites:(145912)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04MyZzPTQ0NzY3OTAmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145912%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145912)",
        "reviewed": 85,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 85,
        "triage_read": 0,
        "triage_snippet_classified": 85
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145912)",
    "indexed_citing_opinions": 743,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145912,
        "count": 743,
        "count_source": "search"
      }
    ],
    "citation_count": 1709,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/arizona-v-johnson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNjI2NDImcz0xMDM1NzIwOSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145912%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145912,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 118086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 118250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 142878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 145712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 2600240,
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
    "date_created": "2026-07-04T18:30:31Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:30:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:30:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:35:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:30:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Arizona v. Johnson

```
(Slip Opinion)              OCTOBER TERM, 2008                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                         ARIZONA v. JOHNSON

      CERTIORARI TO THE COURT OF APPEALS OF ARIZONA

 No. 07–1122. Argued December 9, 2008—Decided January 26, 2009
In Terry v. Ohio, 392 U. S. 1, this Court held that a “stop and frisk”
  may be conducted without violating the Fourth Amendment’s ban on
  unreasonable searches and seizures if two conditions are met. First,
  the investigatory stop (temporary detention) must be lawful, a re
  quirement met in an on-the-street encounter when a police officer
  reasonably suspects that the person apprehended is committing or
  has committed a crime. Second, to proceed from a stop to a frisk
  (patdown for weapons), the officer must reasonably suspect that the
  person stopped is armed and dangerous. For the duration of a traffic
  stop, the Court recently confirmed, a police officer effectively seizes
  “everyone in the vehicle,” the driver and all passengers. Brendlin v.
  California, 551 U. S. 249, 255.
     While patrolling near a Tucson neighborhood associated with the
  Crips gang, police officers serving on Arizona’s gang task force
  stopped an automobile for a vehicular infraction warranting a cita
  tion. At the time of the stop, the officers had no reason to suspect the
  car’s occupants of criminal activity. Officer Trevizo attended to re
  spondent Johnson, the back-seat passenger, whose behavior and
  clothing caused Trevizo to question him. After learning that Johnson
  was from a town with a Crips gang and had been in prison, Trevizo
  asked him get out of the car in order to question him further, out of
  the hearing of the front-seat passenger, about his gang affiliation.
  Because she suspected that he was armed, she patted him down for
  safety when he exited the car. During the patdown, she felt the butt
  of a gun. At that point, Johnson began to struggle, and Trevizo hand
  cuffed him. Johnson was charged with, inter alia, possession of a
  weapon by a prohibited possessor. The trial court denied his motion
  to suppress the evidence, concluding that the stop was lawful and
  that Trevizo had cause to suspect Johnson was armed and dangerous.
2                        ARIZONA v. JOHNSON

                                 Syllabus

    Johnson was convicted. The Arizona Court of Appeals reversed.
    While recognizing that Johnson was lawfully seized, the court found
    that, prior to the frisk, the detention had evolved into a consensual
    conversation about his gang affiliation. Trevizo, the court therefore
    concluded, had no right to pat Johnson down even if she had reason
    to suspect he was armed and dangerous. The Arizona Supreme
    Court denied review.
Held: Officer Trevizo’s patdown of Johnson did not violate the Fourth
 Amendment’s prohibition on unreasonable searches and seizures.
 Pp. 5–9.
    (a) Terry established that, in an investigatory stop based on rea
 sonably grounded suspicion of criminal activity, the police must be
 positioned to act instantly if they have reasonable cause to suspect
 that the persons temporarily detained are armed and dangerous. 392
 U. S., at 24. Because a limited search of outer clothing for weapons
 serves to protect both the officer and the public, a patdown is consti
 tutional. Id., at 23–24, 27, 30–31. Traffic stops, which “resemble, in
 duration and atmosphere, the kind of brief detention authorized in
 Terry,” Berkemer v. McCarty, 468 U. S. 420, 439, n. 29, are “especially
 fraught with danger to police officers,” Michigan v. Long, 463 U. S.
 1032, 1047, who may minimize the risk of harm by exercising “ ‘un
 questioned command of the situation,’ ” Maryland v. Wilson, 519 U. S.
 408, 414. Three decisions cumulatively portray Terry’s application in
 a traffic-stop setting. In Pennsylvania v. Mimms, 434 U. S. 106 (per
 curiam), the Court held that “once a motor vehicle has been lawfully
 detained for a traffic violation, the police officers may order the driver
 to get out of the vehicle without violating the Fourth Amendment,”
 id., at 111, n. 6, because the government’s “legitimate and weighty”
 interest in officer safety outweighs the “de minimis” additional intru
 sion of requiring a driver, already lawfully stopped, to exit the vehi
 cle, id., at 110–111. Citing Terry, the Court further held that a
 driver, once outside the stopped vehicle, may be patted down for
 weapons if the officer reasonably concludes that the driver might be
 armed and dangerous. 434 U. S., at 112. Wilson, 519 U. S., at 413,
 held that the Mimms rule applies to passengers as well as drivers,
 based on “the same weighty interest in officer safety.” Brendlin, 551
 U. S., at 263, held that a passenger is seized, just as the driver is,
 “from the moment [a car stopped by the police comes] to a halt on the
 side of the road.” A passenger’s motivation to use violence during the
 stop to prevent apprehension for a crime more grave than a traffic
 violation is just as great as that of the driver. 519 U. S., at 414. And
 as “the passengers are already stopped by virtue of the stop of the
 vehicle,” id., at 413–414, “the additional intrusion on the passenger is
 minimal,” id., at 415. Pp. 5–7.
                     Cite as: 555 U. S. ____ (2009)                     3

                                Syllabus

     (b) The Arizona Court of Appeals recognized that, initially, Johnson
  was lawfully detained incident to the legitimate stop of the vehicle in
  which he was a passenger, but concluded that once Officer Trevizo
  began questioning him on a matter unrelated to the traffic stop, pat
  down authority ceased to exist, absent reasonable suspicion that
  Johnson had engaged, or was about to engage, in criminal activity.
  The court portrayed the interrogation as consensual, and, Johnson
  emphasizes, Trevizo testified that Johnson could have refused to exit
  the vehicle and to submit to the patdown. But Trevizo also testified
  that she never advised Johnson he did not have to answer her ques
  tions or otherwise cooperate with her. A lawful roadside stop begins
  when a vehicle is pulled over for investigation of a traffic violation.
  The temporary seizure of driver and passengers ordinarily continues,
  and remains reasonable, for the duration of the stop. Normally, the
  stop ends when the police have no further need to control the scene,
  and inform the driver and passengers they are free to leave. An offi
  cer’s inquiries into matters unrelated to the justification for the traf
  fic stop do not convert the encounter into something other than a law
  ful seizure, so long as the inquiries do not measurably extend the
  stop’s duration. See Muehler v. Mena, 544 U. S. 93, 100–101. A rea
  sonable passenger would understand that during the time a car is
  lawfully stopped, he or she is not free to terminate the encounter
  with the police and move about at will. Nothing occurred in this case
  that would have conveyed to Johnson that, prior to the frisk, the traf
  fic stop had ended or that he was otherwise free “to depart without
  police permission.” Brendlin, 551 U. S., at 257. Trevizo was not re
  quired by the Fourth Amendment to give Johnson an opportunity to
  depart without first ensuring that, in so doing, she was not permit
  ting a dangerous person to get behind her. Pp. 7–9.
217 Ariz. 58, 170 P. 3d 667, reversed and remanded.

  GINSBURG, J., delivered the opinion for a unanimous Court.
                        Cite as: 555 U. S. ____ (2009)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 07–1122
                                   _________________


     ARIZONA, PETITIONER v. LEMON MONTREA 

                    JOHNSON 

   ON WRIT OF CERTIORARI TO THE COURT OF APPEALS OF 

                 ARIZONA, DIVISION TWO

                               [January 26, 2009]

  JUSTICE GINSBURG delivered the opinion of the Court.
  This case concerns the authority of police officers to
“stop and frisk” a passenger in a motor vehicle temporarily
seized upon police detection of a traffic infraction. In a
pathmarking decision, Terry v. Ohio, 392 U. S. 1 (1968),
the Court considered whether an investigatory stop (tem
porary detention) and frisk (patdown for weapons) may be
conducted without violating the Fourth Amendment’s ban
on unreasonable searches and seizures. The Court upheld
“stop and frisk” as constitutionally permissible if two
conditions are met. First, the investigatory stop must be
lawful. That requirement is met in an on-the-street en
counter, Terry determined, when the police officer rea
sonably suspects that the person apprehended is commit
ting or has committed a criminal offense. Second, to
proceed from a stop to a frisk, the police officer must rea
sonably suspect that the person stopped is armed and
dangerous.
  For the duration of a traffic stop, we recently confirmed,
a police officer effectively seizes “everyone in the vehicle,”
the driver and all passengers. Brendlin v. California, 551
2                  ARIZONA v. JOHNSON

                    Opinion of the Court

U. S. 249, 255 (2007). Accordingly, we hold that, in a
traffic-stop setting, the first Terry condition—a lawful
investigatory stop—is met whenever it is lawful for police
to detain an automobile and its occupants pending inquiry
into a vehicular violation. The police need not have, in
addition, cause to believe any occupant of the vehicle is
involved in criminal activity. To justify a patdown of the
driver or a passenger during a traffic stop, however, just
as in the case of a pedestrian reasonably suspected of
criminal activity, the police must harbor reasonable suspi
cion that the person subjected to the frisk is armed and
dangerous.
                              I
   On April 19, 2002, Officer Maria Trevizo and Detectives
Machado and Gittings, all members of Arizona’s gang task
force, were on patrol in Tucson near a neighborhood asso
ciated with the Crips gang. At approximately 9 p.m., the
officers pulled over an automobile after a license plate
check revealed that the vehicle’s registration had been
suspended for an insurance-related violation. Under
Arizona law, the violation for which the vehicle was
stopped constituted a civil infraction warranting a cita
tion. At the time of the stop, the vehicle had three occu
pants—the driver, a front-seat passenger, and a passenger
in the back seat, Lemon Montrea Johnson, the respondent
here. In making the stop the officers had no reason to
suspect anyone in the vehicle of criminal activity. See
App. 29–30.
   The three officers left their patrol car and approached
the stopped vehicle. Machado instructed all of the occu
pants to keep their hands visible. Id., at 14. He asked
whether there were any weapons in the vehicle; all re
sponded no. Id., at 15. Machado then directed the driver
to get out of the car. Gittings dealt with the front-seat
passenger, who stayed in the vehicle throughout the stop.
                 Cite as: 555 U. S. ____ (2009)            3

                     Opinion of the Court

See id., at 31. While Machado was getting the driver’s
license and information about the vehicle’s registra
tion and insurance, see id., at 42–43, Trevizo attended to
Johnson.
   Trevizo noticed that, as the police approached, Johnson
looked back and kept his eyes on the officers. Id., at 12.
When she drew near, she observed that Johnson was
wearing clothing, including a blue bandana, that she
considered consistent with Crips membership. Id., at 17.
She also noticed a scanner in Johnson’s jacket pocket,
which “struck [her] as highly unusual and cause [for]
concern,” because “most people” would not carry around a
scanner that way “unless they’re going to be involved in
some kind of criminal activity or [are] going to try to evade
the police by listening to the scanner.” Id., at 16. In
response to Trevizo’s questions, Johnson provided his
name and date of birth but said he had no identification
with him. He volunteered that he was from Eloy, Arizona,
a place Trevizo knew was home to a Crips gang. Johnson
further told Trevizo that he had served time in prison for
burglary and had been out for about a year. 217 Ariz. 58,
60, 170 P. 3d 667, 669 (App. 2007).
   Trevizo wanted to question Johnson away from the
front-seat passenger to gain “intelligence about the gang
[Johnson] might be in.” App. 19. For that reason, she
asked him to get out of the car. Ibid. Johnson complied.
Based on Trevizo’s observations and Johnson’s answers to
her questions while he was still seated in the car, Trevizo
suspected that “he might have a weapon on him.” Id., at
20. When he exited the vehicle, she therefore “patted him
down for officer safety.” Ibid. During the patdown, Tre
vizo felt the butt of a gun near Johnson’s waist. 217 Ariz.,
at 60, 170 P. 3d, at 669. At that point Johnson began to
struggle, and Trevizo placed him in handcuffs. Ibid.
   Johnson was charged in state court with, inter alia,
possession of a weapon by a prohibited possessor. He
4                   ARIZONA v. JOHNSON

                     Opinion of the Court

moved to suppress the evidence as the fruit of an unlawful
search. The trial court denied the motion, concluding that
the stop was lawful and that Trevizo had cause to suspect
Johnson was armed and dangerous. See App. 74–78. A
jury convicted Johnson of the gun-possession charge. See
217 Ariz., at 60–61, 170 P. 3d, at 669–670.
   A divided panel of the Arizona Court of Appeals re
versed Johnson’s conviction. Id., at 59, 170 P. 3d, at 668.
Recognizing that “Johnson was [lawfully] seized when the
officers stopped the car,” id., at 62, 170 P. 3d, at 671, the
court nevertheless concluded that prior to the frisk the
detention had “evolved into a separate, consensual en
counter stemming from an unrelated investigation by
Trevizo of Johnson’s possible gang affiliation,” id., at 64,
170 P. 3d, at 673. Absent “reason to believe Johnson was
involved in criminal activity,” the Arizona appeals court
held, Trevizo “had no right to pat him down for weapons,
even if she had reason to suspect he was armed and dan
gerous.” Ibid.
   Judge Espinosa dissented. He found it “highly unrealis
tic to conclude that merely because [Trevizo] was courte
ous and Johnson cooperative, the ongoing and virtually
simultaneous chain of events [had] somehow ‘evolved into
a consensual encounter’ in the few short moments in
volved.” Id., at 66, 170 P. 3d, at 675. Throughout the
episode, he stressed, Johnson remained “seized as part of
[a] valid traffic stop.” Ibid. Further, he maintained,
Trevizo “had a reasonable basis to consider [Johnson]
dangerous,” id., at 67, 170 P. 3d, at 676, and could there
fore ensure her own safety and that of others at the scene
by patting down Johnson for weapons.
   The Arizona Supreme Court denied review. No. CR–07–
0290–PR, 2007 Ariz. LEXIS 154 (Nov. 29, 2007). We
granted certiorari, 554 U. S. ___ (2008), and now reverse
the judgment of the Arizona Court of Appeals.
                 Cite as: 555 U. S. ____ (2009)            5

                     Opinion of the Court

                               II 

                               A

   We begin our consideration of the constitutionality of
Officer Trevizo’s patdown of Johnson by looking back to
the Court’s leading decision in Terry v. Ohio, 392 U. S. 1
(1968). Terry involved a stop for interrogation of men
whose conduct had attracted the attention of a patrolling
police officer. The officer’s observation led him reasonably
to suspect that the men were casing a jewelry shop in
preparation for a robbery. He conducted a patdown, which
disclosed weapons concealed in the men’s overcoat pockets.
This Court upheld the lower courts’ determinations that
the interrogation was warranted and the patdown, per
missible. See id., at 8.
   Terry established the legitimacy of an investigatory stop
“in situations where [the police] may lack probable cause
for an arrest.” Id., at 24. When the stop is justified by
suspicion (reasonably grounded, but short of probable
cause) that criminal activity is afoot, the Court explained,
the police officer must be positioned to act instantly on
reasonable suspicion that the persons temporarily de
tained are armed and dangerous. Ibid. Recognizing that
a limited search of outer clothing for weapons serves to
protect both the officer and the public, the Court held the
patdown reasonable under the Fourth Amendment. Id., at
23–24, 27, 30–31.
   “[M]ost traffic stops,” this Court has observed, “resem
ble, in duration and atmosphere, the kind of brief deten
tion authorized in Terry.” Berkemer v. McCarty, 468 U. S.
420, 439, n. 29 (1984). Furthermore, the Court has recog
nized that traffic stops are “especially fraught with danger
to police officers.” Michigan v. Long, 463 U. S. 1032, 1047
(1983). “ ‘The risk of harm to both the police and the occu
pants [of a stopped vehicle] is minimized,’ ” we have
stressed, “ ‘if the officers routinely exercise unquestioned
command of the situation.’ ” Maryland v. Wilson, 519 U. S.
6                   ARIZONA v. JOHNSON

                      Opinion of the Court

408, 414 (1997) (quoting Michigan v. Summers, 452 U. S.
692, 702–703 (1981)); see Brendlin, 551 U. S., at 258.
Three decisions cumulatively portray Terry’s application
in a traffic-stop setting: Pennsylvania v. Mimms, 434 U. S.
106 (1977) (per curiam); Maryland v. Wilson, 519 U. S. 408
(1997); and Brendlin v. California, 551 U. S. 249 (2007).
  In Mimms, the Court held that “once a motor vehicle
has been lawfully detained for a traffic violation, the police
officers may order the driver to get out of the vehicle
without violating the Fourth Amendment’s proscription of
unreasonable searches and seizures.” 434 U. S., at 111,
n. 6. The government’s “legitimate and weighty” interest
in officer safety, the Court said, outweighs the “de mini
mis” additional intrusion of requiring a driver, already
lawfully stopped, to exit the vehicle. Id., at 110–111.
Citing Terry as controlling, the Court further held that a
driver, once outside the stopped vehicle, may be patted
down for weapons if the officer reasonably concludes that
the driver “might be armed and presently dangerous.” 434
U. S., at 112.
  Wilson held that the Mimms rule applied to passengers
as well as to drivers. Specifically, the Court instructed
that “an officer making a traffic stop may order passengers
to get out of the car pending completion of the stop.” 519
U. S., at 415. “[T]he same weighty interest in officer
safety,” the Court observed, “is present regardless of
whether the occupant of the stopped car is a driver or
passenger.” Id., at 413.
  It is true, the Court acknowledged, that in a lawful
traffic stop, “[t]here is probable cause to believe that the
driver has committed a minor vehicular offense,” but
“there is no such reason to stop or detain the passengers.”
Ibid. On the other hand, the Court emphasized, the risk
of a violent encounter in a traffic-stop setting “stems not
from the ordinary reaction of a motorist stopped for a
speeding violation, but from the fact that evidence of a
                 Cite as: 555 U. S. ____ (2009)            7

                     Opinion of the Court

more serious crime might be uncovered during the stop.”
Id., at 414. “[T]he motivation of a passenger to employ
violence to prevent apprehension of such a crime,” the
Court stated, “is every bit as great as that of the driver.”
Ibid. Moreover, the Court noted, “as a practical matter,
the passengers are already stopped by virtue of the stop of
the vehicle,” id., at 413–414, so “the additional intrusion
on the passenger is minimal,” id., at 415.
  Completing the picture, Brendlin held that a passenger
is seized, just as the driver is, “from the moment [a car
stopped by the police comes] to a halt on the side of the
road.” 551 U. S., at 263. A passenger therefore has stand
ing to challenge a stop’s constitutionality. Id., at 256–259.
  After Wilson, but before Brendlin, the Court had stated,
in dictum, that officers who conduct “routine traffic
stop[s]” may “perform a ‘patdown’ of a driver and any
passengers upon reasonable suspicion that they may be
armed and dangerous.” Knowles v. Iowa, 525 U. S. 113,
117–118 (1998). That forecast, we now confirm, accurately
captures the combined thrust of the Court’s decisions in
Mimms, Wilson, and Brendlin.
                              B
  The Arizona Court of Appeals recognized that, initially,
Johnson was lawfully detained incident to the legitimate
stop of the vehicle in which he was a passenger. See 217
Ariz., at 64, 170 P. 3d, at 673. But, that court concluded,
once Officer Trevizo undertook to question Johnson on a
matter unrelated to the traffic stop, i.e., Johnson’s gang
affiliation, patdown authority ceased to exist, absent
reasonable suspicion that Johnson had engaged, or was
about to engage, in criminal activity. See id., at 65, 170
P. 3d, at 674. In support of the Arizona court’s portrayal
of Trevizo’s interrogation of Johnson as “consensual,”
Johnson emphasizes Trevizo’s testimony at the suppres
sion hearing. Responding to the prosecutor’s questions,
8                      ARIZONA v. JOHNSON

                         Opinion of the Court

Trevizo affirmed her belief that Johnson could have “re
fused to get out of the car” and “to turn around for the pat
down.” App. 41.
   It is not clear why the prosecutor, in opposing the sup
pression motion, sought to portray the episode as consen
sual. Cf. Florida v. Bostick, 501 U. S. 429 (1991) (holding
that police officers’ search of a bus passenger’s luggage can
be based on consent). In any event, Trevizo also testified
that she never advised Johnson he did not have to answer
her questions or otherwise cooperate with her. See App.
45. And during cross-examination, Trevizo did not dis
agree when defense counsel asked “in fact you weren’t
seeking [Johnson’s] permission . . . ?” Id., at 36. As the
dissenting judge observed, “consensual” is an “unrealistic”
characterization of the Trevizo-Johnson interaction.
“[T]he encounter . . . took place within minutes of the
stop”; the patdown followed “within mere moments” of
Johnson’s exit from the vehicle; beyond genuine debate,
the point at which Johnson could have felt free to leave
had not yet occurred. See 217 Ariz., at 66, 170 P. 3d, at
675.1
   A lawful roadside stop begins when a vehicle is pulled
over for investigation of a traffic violation. The temporary
seizure of driver and passengers ordinarily continues, and
remains reasonable, for the duration of the stop. Nor
mally, the stop ends when the police have no further need
to control the scene, and inform the driver and passengers
they are free to leave. See Brendlin, 551 U. S., at 258. An
officer’s inquiries into matters unrelated to the justifica
tion for the traffic stop, this Court has made plain, do not
——————
  1 The Court of Appeals majority did not assert that Johnson reasona

bly could have felt free to leave. Instead, the court said “a reasonable
person in Johnson’s position would have felt free to remain in the
vehicle.” 217 Ariz. 58, 64, 170 P. 3d 667, 673 (2007). That position,
however, appears at odds with our decision in Maryland v. Wilson, 519
U. S. 408 (1997). See supra, at 6–7.
                   Cite as: 555 U. S. ____ (2009)                  9

                       Opinion of the Court

convert the encounter into something other than a lawful
seizure, so long as those inquiries do not measurably
extend the duration of the stop. See Muehler v. Mena, 544
U. S. 93, 100–101 (2005).
  In sum, as stated in Brendlin, a traffic stop of a car
communicates to a reasonable passenger that he or she is
not free to terminate the encounter with the police and
move about at will. See 551 U. S., at 257. Nothing oc
curred in this case that would have conveyed to Johnson
that, prior to the frisk, the traffic stop had ended or that
he was otherwise free “to depart without police permis
sion.” Ibid. Officer Trevizo surely was not constitution
ally required to give Johnson an opportunity to depart the
scene after he exited the vehicle without first ensuring
that, in so doing, she was not permitting a dangerous
person to get behind her.2
                       *     *    *
  For the reasons stated, the judgment of the Arizona
Court of Appeals is reversed, and the case is remanded for
further proceedings not inconsistent with this opinion.

                                                    It is so ordered.




——————
 2 The  Arizona Court of Appeals assumed, “without deciding, that
Trevizo had reasonable suspicion that Johnson was armed and danger
ous.” 217 Ariz., at 64, 170 P. 3d, at 673. We do not foreclose the
appeals court’s consideration of that issue on remand.

```

---

## GROUP: _overhaul2/lake/cases/Arizona v. Mauro.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Arizona v. Mauro"
type: case
citation: "481 U.S. 520 (1987)"
parallel_cite: "107 S. Ct. 1931; 95 L. Ed. 2d 458"
neutral_cite: 1987 U.S. LEXIS 1933
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-06-26
docket: 85-2121
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-06-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Arizona v. Mauro
  varies_by_point: false
  scope_note: "Good law; allowing a suspect who has invoked Miranda to speak with his spouse in an officer's presence (recorded) is not interrogation or its functional equivalent under Innis."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111878/arizona-v-mauro/"
  cluster_id: 111878
  opinion_id: 9430952
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Rhode Island v. Innis]]", "[[Miranda v. Arizona]]", "[[Edwards v. Arizona]]", "[[Oregon v. Elstad]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "interrogation", "functional-equivalent", "custodial-interrogation"]
holding: "Allowing a suspect who has invoked his Miranda rights to speak with his wife, with a police officer present and a recorder running, is not 'interrogation' or its functional equivalent; officers do not interrogate a suspect merely by hoping he will incriminate himself, so the resulting volunteered statements are admissible."
lake:
  record_id: Arizona v. Mauro
  status: verified
  projected_at: 2026-07-09
---

# Arizona v. Mauro

*481 U.S. 520 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Mauro was arrested after admitting he had killed his son. After receiving [[Miranda and Custodial Interrogation|Miranda warnings]] he invoked his right to counsel, and questioning stopped. His wife, who was being questioned in another room, insisted on speaking with him. Officers tried to discourage her but relented, requiring that a detective be present and that a tape recorder be running in plain view. During the conversation Mauro made incriminating statements, which the prosecution later used to rebut his insanity defense. The Arizona Supreme Court held that allowing the spousal meeting was the functional equivalent of interrogation under [[Rhode Island v. Innis]].

## Issue
Whether permitting a suspect who has invoked his [[Miranda and Custodial Interrogation|Miranda rights]] to speak with his spouse, in the presence of an officer with a recorder, constitutes interrogation or its functional equivalent.

## Rule
No. "We think it is clear under both *Miranda* and *Innis* that Mauro was not interrogated. . . . There is no evidence that the officers sent Mrs. Mauro in to see her husband for the purpose of eliciting incriminating statements." — 481 U.S. at 527–528. ^pin-528

Merely creating an opportunity is not interrogation: "Officers do not interrogate a suspect simply by hoping that he will incriminate himself." — [*Id.* at 529](https://www.courtlistener.com/opinion/111878/arizona-v-mauro/#:~:text=Officers%20do%20not%20interrogate%20a). ^pin-529

Because "Mauro was not subjected to compelling influences, psychological ploys, or direct questioning[,] . . . his volunteered statements cannot properly be considered the result of police interrogation." — *Id.*

## Application
The tape showed the detective asked Mauro no questions about the crime, and nothing suggested the officers used the meeting as a psychological ploy — they had discouraged the wife and "yielded to her insistent demands," and the officer's presence served legitimate, security-related reasons. Viewed from Mauro's perspective, a suspect told his wife may speak with him would not feel coerced to incriminate himself. The conduct was "far less questionable than the 'subtle compulsion'" held not to be interrogation in *[[Rhode Island v. Innis|Innis]]*, and did not implicate Miranda's purpose of preventing the coercive use of confinement to extract confessions. The officers therefore "acted reasonably and lawfully," and the Constitution did not bar the statements.

## Conclusion
Mauro was not interrogated; his statements to his wife were admissible. The judgment of the Arizona Supreme Court was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Mauro* applies the functional-equivalent-of-interrogation test of [[Rhode Island v. Innis]] (the "words or actions . . . reasonably likely to elicit an incriminating response" standard) within the [[Miranda v. Arizona]] / [[Edwards v. Arizona]] framework, and reflects the volunteered-statements principle echoed in [[Oregon v. Elstad]].

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Arizona v. Mauro*, 481 U.S. 520 (1987) — https://www.courtlistener.com/opinion/111878/arizona-v-mauro/ — pinpoints: 527–530.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ea8a34da6045d6b4", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Arizona v. Mauro"}, "payload": {"all": [{"cite": "481 U.S. 520", "page": "520", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "481"}, {"cite": "107 S. Ct. 1931", "page": "1931", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "107"}, {"cite": "95 L. Ed. 2d 458", "page": "458", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "95"}, {"cite": "1987 U.S. LEXIS 1933", "page": "1933", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1987"}], "display": "481 U.S. 520", "official": {"cite": "481 U.S. 520", "page": "520", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "481"}, "official_selection_present": true, "record_id": "Arizona v. Mauro"}}
{"assertion_id": "22948f4647520838", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-529", "record_id": "Arizona v. Mauro"}, "payload": {"fragment": "#:~:text=Officers%20do%20not%20interrogate%20a", "page": null, "pin_id": "pin-529", "pinpoint_status": "star-verified", "quote": "Officers do not interrogate a suspect simply by hoping that he will incriminate himself.", "quote_fidelity": "matched", "record_id": "Arizona v. Mauro", "star_marker": "529"}}
{"assertion_id": "5bcc36189a3d45df", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-528", "record_id": "Arizona v. Mauro"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-528", "pinpoint_status": "slip-only", "quote": "--- # Arizona v. Mauro *481 U.S. 520 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Mauro was arrested after admitting he had killed his son. After receiving Miranda warnings he invoked his right to counsel, and questioning stopped. His wife, who was being questioned in another room, insisted on speaking with him. Officers tried to discourage her but relented, requiring that a detective be present and that a tape recorder be running in plain view. During the conversation Mauro made incriminating statements, which the prosecution later used to rebut his insanity defense. The Arizona Supreme Court held that allowing the spousal meeting was the functional equivalent of interrogation under [[Rhode Island v. Innis]]. ## Issue Whether permitting a suspect who has invoked his Miranda rights to speak with his spouse, in the presence of an officer with a recorder, constitutes interrogation or its functional equivalent. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Arizona v. Mauro", "star_marker": null}}
{"assertion_id": "a823daac3d82812e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Arizona v. Mauro"}, "payload": {"as_of_content": "1987-06-26", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Arizona v. Mauro", "scope_note": "Good law; allowing a suspect who has invoked Miranda to speak with his spouse in an officer's presence (recorded) is not interrogation or its functional equivalent under Innis.", "varies_by_point": false}}
```

### lake record — Arizona v. Mauro

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arizona v. Mauro",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Arizona v. Mauro",
    "case_name_short": "Mauro",
    "case_name_full": "Arizona v. Mauro",
    "input_case_name": "Arizona v. Mauro",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-06-26",
    "year": 1987,
    "docket": "85-2121",
    "cluster_id": 111878,
    "lead_opinion_id": 9430952,
    "sibling_ids": [
      111878,
      9430952,
      9430953
    ],
    "absolute_url": "/opinion/111878/arizona-v-mauro/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9070020,
        "score": 10,
        "case_name": "Arizona v. Mauro"
      },
      {
        "cluster_id": 9070019,
        "score": 10,
        "case_name": "Arizona v. Mauro"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "481 U.S. 520",
      "volume": "481",
      "reporter": "U.S.",
      "page": "520",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 1931",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1931",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "95 L. Ed. 2d 458",
        "volume": "95",
        "reporter": "L. Ed. 2d",
        "page": "458",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 1933",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1933",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "481 U.S. 520",
        "volume": "481",
        "reporter": "U.S.",
        "page": "520",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 1931",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1931",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "95 L. Ed. 2d 458",
        "volume": "95",
        "reporter": "L. Ed. 2d",
        "page": "458",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 1933",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1933",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "481 U.S. 520",
    "official_selection": {
      "court_class": "scotus",
      "selected": "481 U.S. 520",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-528",
      "page": null,
      "quote": "--- # Arizona v. Mauro *481 U.S. 520 (1987)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Mauro was arrested after admitting he had killed his son. After receiving Miranda warnings he invoked his right to counsel, and questioning stopped. His wife, who was being questioned in another room, insisted on speaking with him. Officers tried to discourage her but relented, requiring that a detective be present and that a tape recorder be running in plain view. During the conversation Mauro made incriminating statements, which the prosecution later used to rebut his insanity defense. The Arizona Supreme Court held that allowing the spousal meeting was the functional equivalent of interrogation under [[Rhode Island v. Innis]]. ## Issue Whether permitting a suspect who has invoked his Miranda rights to speak with his spouse, in the presence of an officer with a recorder, constitutes interrogation or its functional equivalent. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-529",
      "page": null,
      "quote": "Officers do not interrogate a suspect simply by hoping that he will incriminate himself.",
      "star_marker": "529",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 18639,
      "fragment": "#:~:text=Officers%20do%20not%20interrogate%20a",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-06-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Arizona v. Mauro",
    "varies_by_point": false,
    "scope_note": "Good law; allowing a suspect who has invoked Miranda to speak with his spouse in an officer's presence (recorded) is not interrogation or its functional equivalent under Innis.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Colon",
          "cluster_id": 4671866,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Patrick Broom a/k/a Patrick Brown v. United States",
          "cluster_id": 2809687,
          "cite": [
            "118 A.3d 207",
            "2015 D.C. App. LEXIS 265",
            "2015 WL 3768885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Quarles",
          "cluster_id": 1057961,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Damon Kimbrough",
          "cluster_id": 796843,
          "cite": [
            "477 F.3d 144",
            "2007 U.S. App. LEXIS 3488",
            "2007 WL 495026"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Alexander",
          "cluster_id": 167490,
          "cite": [
            "447 F.3d 1290",
            "2006 U.S. App. LEXIS 11993",
            "2006 WL 1314663"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Julian Galindo-Gallegos, AKA Jose Reyes-Olague, AKA Aurelio Garcia-Chairez, AKA Jose Olague Reyes",
          "cluster_id": 772608,
          "cite": [
            "244 F.3d 728",
            "2001 Daily Journal DAR 3047",
            "2001 U.S. App. LEXIS 4891",
            "2001 WL 289956"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Muniz",
          "cluster_id": 112464,
          "cite": [
            "110 L. Ed. 2d 528",
            "110 S. Ct. 2638",
            "496 U.S. 582",
            "1990 U.S. LEXIS 3211"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Linton",
          "cluster_id": 944931,
          "cite": [
            "56 Cal. 4th 1146",
            "302 P.3d 927",
            "158 Cal. Rptr. 3d 521",
            "2013 WL 3214690",
            "2013 Cal. LEXIS 5338"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Leger",
          "cluster_id": 1592017,
          "cite": [
            "936 So. 2d 108",
            "2006 WL 1883421"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Davis",
          "cluster_id": 2575950,
          "cite": [
            "115 P.3d 417",
            "31 Cal. Rptr. 3d 96",
            "36 Cal. 4th 510",
            "2005 Cal. Daily Op. Serv. 6393",
            "2005 Daily Journal DAR 8733",
            "2005 Cal. LEXIS 7963"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ray",
          "cluster_id": 1130099,
          "cite": [
            "13 Cal. 4th 313",
            "914 P.2d 846",
            "96 Daily Journal DAR 5231",
            "52 Cal. Rptr. 2d 296",
            "96 Cal. Daily Op. Serv. 3222",
            "1996 Cal. LEXIS 1906"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Leonard",
          "cluster_id": 2632907,
          "cite": [
            "157 P.3d 973",
            "58 Cal. Rptr. 3d 368",
            "40 Cal. 4th 1370",
            "2007 Cal. Daily Op. Serv. 5424",
            "2007 Cal. LEXIS 5071"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Francisco Sangineto-Miranda, (87-5667) Luray Betts, (87-5668) Enrique Vargas, (87-5711) & Benjamin Nelson, (87-5712)",
          "cluster_id": 513263,
          "cite": [
            "859 F.2d 1501"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Woodward v. State",
          "cluster_id": 1611371,
          "cite": [
            "533 So. 2d 418",
            "1988 WL 28413"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Clark",
          "cluster_id": 1121458,
          "cite": [
            "857 P.2d 1099",
            "5 Cal. 4th 950",
            "22 Cal. Rptr. 2d 689",
            "93 Daily Journal DAR 11122",
            "93 Cal. Daily Op. Serv. 6528",
            "1993 Cal. LEXIS 4179"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Medina",
          "cluster_id": 2610902,
          "cite": [
            "799 P.2d 1282",
            "51 Cal. 3d 870",
            "274 Cal. Rptr. 849",
            "90 Cal. Daily Op. Serv. 8358",
            "1990 Cal. LEXIS 5054"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Enraca",
          "cluster_id": 844219,
          "cite": [
            "269 P.3d 543",
            "53 Cal. 4th 735",
            "137 Cal. Rptr. 3d 117",
            "2012 WL 360555",
            "2012 Cal. LEXIS 1078"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gallego",
          "cluster_id": 1351145,
          "cite": [
            "802 P.2d 169",
            "52 Cal. 3d 115",
            "276 Cal. Rptr. 679",
            "90 Daily Journal DAR 14576",
            "90 Cal. Daily Op. Serv. 9269",
            "1990 Cal. LEXIS 5484"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dennis Rosa Collazo v. Wayne Estelle, Warden, California Mens Colony",
          "cluster_id": 565270,
          "cite": [
            "940 F.2d 411",
            "91 Daily Journal DAR 8681",
            "91 Cal. Daily Op. Serv. 5640",
            "1991 U.S. App. LEXIS 15265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Dement",
          "cluster_id": 844239,
          "cite": [
            "264 P.3d 292",
            "53 Cal. 4th 1",
            "133 Cal. Rptr. 3d 496",
            "2011 Cal. LEXIS 12151"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Tate",
          "cluster_id": 2512108,
          "cite": [
            "234 P.3d 428",
            "49 Cal. 4th 635",
            "112 Cal. Rptr. 3d 156",
            "2010 Cal. LEXIS 6548"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Jessie Dotson",
          "cluster_id": 2738561,
          "cite": [
            "450 S.W.3d 1",
            "2014 Tenn. LEXIS 694"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Doll",
          "cluster_id": 5642287,
          "cite": [
            "21 N.Y.3d 665",
            "998 N.E.2d 384"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jaturun Siripongs v. Arthur Calderon, Warden",
          "cluster_id": 678556,
          "cite": [
            "35 F.3d 1308"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jenkins v. Commonwealth",
          "cluster_id": 1420585,
          "cite": [
            "423 S.E.2d 360",
            "244 Va. 445",
            "9 Va. Law Rep. 480",
            "1992 Va. LEXIS 111"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Turner",
          "cluster_id": 4326929,
          "cite": [
            "2016 Ohio 7983"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Copeland",
          "cluster_id": 1678832,
          "cite": [
            "530 So. 2d 526",
            "1988 WL 31771"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Snow v. State",
          "cluster_id": 1695079,
          "cite": [
            "800 So. 2d 472",
            "2001 WL 1137390"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adkins v. Commonwealth",
          "cluster_id": 1377595,
          "cite": [
            "96 S.W.3d 779",
            "2003 Ky. LEXIS 13",
            "2003 WL 367054"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harold S. Alston v. Walter Redman, Warden Charles M. Oberly, Iii, Attorney General of the State of Delaware and the State of Delaware",
          "cluster_id": 677798,
          "cite": [
            "34 F.3d 1237",
            "1994 U.S. App. LEXIS 24171",
            "1994 WL 480728"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Mauro:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111878 OR 9430952 OR 9430953) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01OTY5Mzc2MDAwMDAmcz0xMzQ5MzM1JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111878+OR+9430952+OR+9430953%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111878 OR 9430952 OR 9430953)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02OSZzPTQ5ODA0NyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111878+OR+9430952+OR+9430953%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111878 OR 9430952 OR 9430953)",
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
    "complete_query": "cites:(111878 OR 9430952 OR 9430953)",
    "indexed_citing_opinions": 268,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111878,
        "count": 230,
        "count_source": "search"
      },
      {
        "opinion_id": 9430952,
        "count": 43,
        "count_source": "search"
      },
      {
        "opinion_id": 9430953,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 419,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/arizona-v-mauro.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY1MjI0NDcmcz00Njc1NDk4JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111878+OR+9430952+OR+9430953%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111878,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 111796,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 111798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 1160581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111878,
        "cited_id": 1169190,
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
    "date_created": "2026-07-04T18:35:04Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:35:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:35:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:40:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:35:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Arizona v. Mauro

```
<opinion type="majority">
<author id="b581-9">Justice Powell</author>
<p id="A30">delivered the opinion of the Court.</p>
<p id="b581-10">While respondent in this case was in police custody, he indicated that he did not wish to answer any questions until a lawyer was present. The issue presented is whether, in the circumstances of this case, officers interrogated respondent in violation of the Fifth and Fourteenth Amendments when they allowed him to speak with his wife in the presence of a police officer.</p>
<p id="b581-11">I</p>
<p id="b581-12">On November 23, 1982, the Flagstaff Police Department received a telephone call from a local K mart store. The caller stated that a man had entered the store claiming to have killed his son. When officers reached the store, respondent Mauro freely admitted that he had killed his son. He directed the officers to the child’s body, and then was arrested and advised of his constitutional rights pursuant to <page-number citation-index="1" label="522">*522</page-number><em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). The officers then took Mauro to the pólice station, where he was advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights again. At that point, Mauro told the officers that he did not wish to make any more statements without having a lawyer present. All questioning then ceased. As no secure detention area was available, Mauro was held in the office of the police captain.</p>
<p id="b582-5">At the same time, one of the officers, Detective Manson, was questioning Mauro’s wife in another room. After she finished speaking with Manson, Mrs. Mauro asked if she could speak to her husband. Manson was reluctant to allow the meeting, but after Mrs. Mauro insisted, he discussed the request with his supervisor, Sergeant Allen. Allen testified that he “saw no harm in it and suggested to [Manson] that if she really sincerely wanted to talk to him to go ahead and allow it.” App. 74. Allen instructed Manson not to leave Mr. and Mrs. Mauro alone and suggested that Manson tape-record the conversation.</p>
<p id="b582-6">Manson then “told both Mr. and Mrs. Mauro that they could speak together only if an officer were present in the room to observe and hear what was going on.” <em>Id., </em>at 218 (findings of trial court). He brought Mrs. Mauro into the room and seated himself at a desk, placing a tape recorder in plain sight on the desk. He recorded their brief conversation, in which she expressed despair about their situation. During the conversation, Mauro told his wife not to answer questions until a lawyer was present.<footnotemark>1</footnotemark></p>
<p id="b583-4"><page-number citation-index="1" label="523">*523</page-number>Mauro’s defense at trial was that he had been insane at the time of the crime. In rebuttal, the prosecution played the tape of the meeting between Mauro and his wife, arguing that it demonstrated that Mauro was sane on the day of the murder. Mauro sought suppression of the recording on the ground that it was a product of police interrogation in violation of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. The trial court refused to suppress the recording. First, it explained the basis of the officers’ decision to allow Mrs. Mauro to meet with her husband in the presence of a policeman:</p>
<blockquote id="b583-5">“The police counseled [Mrs. Mauro] not to [speak with her husband], but she was adamant about that. They finally yielded to her insistent demands. The Police Station lacked a secure interview room. The police justifiably appeared <em>[sic] </em>for Mrs. Mauro’s . . . safety, and they were also concerned about security, both in terms of whether Mr. and Mrs. Mauro might cook up a lie or <page-number citation-index="1" label="524">*524</page-number>swap statements with each other that shouldn’t have been allowed, and whether some escape attempt might have been made, or whether there might have been an attempt to smuggle in a weapon. They really had no idea what to expect along those lines.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></em></blockquote>
<p id="b584-5">In light of these justifications, the trial court found “that this procedure was not a ruse, nor a subterfuge by the police. They did not create this situation <em>[i. e., </em>allowing the meeting] as an indirect means of avoiding the dictates of Miranda.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span> </em>Accordingly, the trial court admitted the evidence. Mauro was convicted of murder and child abuse, and sentenced to death.</p>
<p id="b584-6">The Arizona Supreme Court reversed. <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/" aria-description="Citation for case: State v. Mauro">149 Ariz. 24</a></span>, <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/" aria-description="Citation for case: State v. Mauro">716 P. 2d 393</a></span> (1986). It found that by allowing Mauro to speak with his wife in the presence of a police officer, the detectives interrogated Mauro within the meaning of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>This interrogation was impermissible, the court said, because Mauro previously had invoked the right to have counsel present before being questioned further. The court noted that both detectives had acknowledged in pretrial hearings that they knew it was “possible” that Mauro might make incriminating statements if he saw his wife.<footnotemark>2</footnotemark> The court relied <page-number citation-index="1" label="525">*525</page-number>on our statement in <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291</a></span> (1980), that interrogation includes a “practice that the police should know is reasonably likely to evoke an incriminating response from a suspect,” <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis"><em>id., </em>at 301</a></span>. The court then concluded that the officers’ testimony demonstrated that there had been interrogation, because “[t]hey both knew that if the conversation took place, incriminating statements were likely to be made.” <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/#31" aria-description="Citation for case: State v. Mauro">149 Ariz., at 31</a></span>, <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/#400" aria-description="Citation for case: State v. Mauro">716 P. 2d, at 400</a></span>. Therefore, it held that the tape recording was not properly admitted at Mauro’s trial.</p>
<p id="AeK">Arizona filed a petition for a writ of certiorari. Because the decision below appeared to misconstrue our decision in <em>Rhode Island </em>v. <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis, supra,</a></span> </em>we granted the petition, <span class="citation multiple-matches"><a href="/c/U.%20S./479/811/">479 U. S. 811</a></span> (1986). We now reverse.</p>
<p id="AFJX">HH 1 — 1</p>
<p id="Abe">We begin by summarizing the relevant legal principles. The Fifth Amendment provides that no “person . . . shall be compelled in any criminal case to be a witness against himself.”<footnotemark>3</footnotemark> In <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), the Court concluded that “without proper safeguards the process of in-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual’s will to resist and to compel him to speak where he would not otherwise do so freely. ” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 467</a></span>. “Accordingly, the Court formulated the now-familiar ‘procedural safeguards effective to secure the privilege against self-incrimination.’” <em>Colorado </em>v. <em>Spring, </em><span class="citation" data-id="9430793"><a href="/opinion/111798/colorado-v-spring/#572" aria-description="Citation for case: Colorado v. Spring">479 U. S. 564, 572</a></span> (1987) (quoting <em>Miranda </em>v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Arizona, supra, </em>at 444</a></span>). Among these is the rule that when an accused has “expressed his desire to deal with the police only through counsel, [he] is not subject to further interrogation by the authori<page-number citation-index="1" label="526">*526</page-number>ties until counsel has been made available to him, unless the accused himself initiates further communication, exchanges, or conversations with the police.” <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477, 484-485</a></span> (1981).</p>
<p id="b586-5">One of the questions frequently presented in cases in this area is whether particular police conduct constitutes “interrogation.” In <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>the Court suggested in one passage that “interrogation” referred only to actual “questioning initiated by law enforcement officers.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444</a></span>. But this statement was clarified in <em>Rhode Island </em>v. <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis, supra.</a></span> </em>In that case, the Court reviewed the police practices that had evoked the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court’s concern about the coerciveness of the “‘interrogation environment.’” <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">446 U. S., at 299</a></span> (quoting <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#457" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 457</a></span>). The questioned practices included “the use of lineups in which a coached witness would pick the defendant as the perpetrator . . .[,] the so-called ‘reverse line-up’ in which a defendant would be identified by coached witnesses as the perpetrator of a fictitious crime,” and a variety of “psychological ploys, such as to ‘posi[t]’ ‘the guilt of the subject,’ to ‘minimize the moral seriousness of the offense,’ and ‘to cast blame on the victim or on society.’” <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">446 U. S., at 299</a></span> (quoting <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#450" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 450</a></span>) (brackets by <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span> </em>Court). None of these techniques involves express questioning, and yet the Court found that any of them, coupled with the “interrogation environment,” was likely to “‘subjugate the individual to the will of his examiner’ and thereby undermine the privilege against compulsory self-incrimination.” 466 U. S., at 399 (quoting <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#457" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 457</a></span>). Thus, the <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span> </em>Court concluded that the goals of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>safeguards could be effectuated if those safeguards extended not only to express questioning, but also to “its functional equivalent.” <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis">446 U. S., at 301</a></span>. The Court explained the phrase “functional equivalent” of interrogation as including “any words or actions on the part of the police (other than those normally attendant to arrest and custody) that the police should know are reasonably likely to elicit an <page-number citation-index="1" label="527">*527</page-number>incriminating response from the suspect.” <em>Ibid, </em>(footnotes omitted). Finally, it noted that “[t]he latter portion of this definition focuses primarily upon the perceptions of the suspect, rather than the intent of the police.” <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Ibid.</a></span></em></p>
<p id="AW2">1 — 1 <em>I </em>— I hH</p>
<p id="Aeal">We now turn to the case before us. The officers gave Mauro the warnings required by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>Mauro indicated that he did not wish to be questioned further without a lawyer present. Mauro never waived his right to have a lawyer present. The sole issue, then, is whether the officers’ subsequent actions rose to the level of interrogation — that is, in the language of <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span>, </em>whether they were the “functional equivalent” of police interrogation. We think it is clear under both <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span> </em>that Mauro was not interrogated. The tape recording of the conversation between Mauro and his wife shows that Detective Manson asked Mauro no questions about the crime or his conduct.<footnotemark>4</footnotemark> Nor is it suggested — or supported by any evidence — that Sergeant Allen’s decision to allow Mauro’s wife to see him was the kind of psychological ploy that properly could be treated as the functional equivalent of interrogation.<footnotemark>5</footnotemark></p>
<p id="b588-4"><page-number citation-index="1" label="528">*528</page-number>There is no evidence that the officers sent Mrs. Mauro in to see her husband for the purpose of eliciting incriminating statements. As the trial court found, the officers tried to discourage her from talking to her husband, but finally “yielded to her insistent demands,” App. 218. Nor was Detective Manson’s presence improper. His testimony, that the trial court found credible, indicated a number of legitimate reasons — not related to securing incriminating statements — for having a police officer present. See <em>supra, </em>at 523-524 (quoting App. 218). Finally, the weakness of Mauro’s claim that he was interrogated is underscored by examining the situation from his perspective. Cf. <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis">446 U. S., at 301</a></span> (suggesting that the suspect’s perspective may be relevant in some cases in determining whether police actions constitute interrogation). We doubt that a suspect, told by officers that his wife will be allowed to speak to him, would feel that he was being coerced to incriminate himself in any way.</p>
<p id="b588-5">The Arizona Supreme Court was correct to note that there was a “possibility” that Mauro would incriminate himself while talking to his wife. It also emphasized that the officers were aware of that possibility when they agreéd to allow the Mauros to talk to each other.<footnotemark>6</footnotemark> But the actions in this case <page-number citation-index="1" label="529">*529</page-number>were far less questionable than the “subtle compulsion” that we held <em>not </em>to be interrogation in <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span>. </em>See <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#303" aria-description="Citation for case: Rhode Island v. Innis"><em>id., </em>at 303</a></span>. Officers do not interrogate a suspect simply by hoping that he will incriminate himself. In <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>and again in <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span>, </em>the Court emphasized:</p>
<blockquote id="b589-5">“Confessions remain a proper element in law enforcement. Any statement given freely and voluntarily without any compelling influences is, of course, admissible in evidence. The fundamental import of the privilege while an individual is in custody is not whether he is allowed to talk to the police without the benefit of warnings and counsel, but whether he can be interrogated. . . . Volunteered statements of any kind are not barred by the Fifth Amendment and their admissibility is not affected by our holding today.” <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#478" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 478</a></span>, quoted in <em>Rhode Island </em>v. <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#299" aria-description="Citation for case: Rhode Island v. Innis"><em>Innis, supra, </em>at 299-300</a></span>.</blockquote>
<p id="b589-7">See <em>Oregon </em>v. <em>Elstad, </em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#305" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 305</a></span> (1985). (“‘[F]ar from being prohibited by the Constitution, admissions of guilt by wrongdoers, if not coerced, are inherently desirable’” (quoting <em>United States </em>v. <em>Washington, </em><span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#187" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 187</a></span> (1977))). Mauro was not subjected to compelling influences, psychological ploys, or direct questioning. Thus, his volunteered statements cannot properly be considered the result of police interrogation.</p>
<p id="b589-9">In deciding whether particular police conduct is interrogation, we must remember the purpose behind our decisions in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>: </em>preventing government officials from <page-number citation-index="1" label="530">*530</page-number>using the coercive nature of confinement to extract confessions that would not be given in an unrestrained environment. The government actions in this case do not implicate this purpose in any way. Police departments need not adopt inflexible rules barring suspects from speaking with their spouses, nor must they ignore legitimate security concerns by allowing spouses to meet in private. In short, the officers in this case acted reasonably and lawfully by allowing Mrs. Mauro to speak with her husband. In this situation, the Federal Constitution does not forbid use of Mauro’s subsequent statements at his criminal trial.</p>
<p id="A4x">I — I &lt;!</p>
<p id="A_p">The judgment of the Arizona Supreme Court is reversed. The case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b590-4">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b582-7"> The entire conversation proceeded as follows:</p>
<p id="b582-8">“MRS. MAURO: Please — please, I don’t know what to do. We should have put David [the victim] in the hospital. Please — I don’t know what we’re going to do. We should have went for help — we should have went for help.</p>
<p id="b582-9">“[MR. MAURO]: You tried as best you could to stop it.</p>
<p id="b582-10">“MRS. MAURO: I-</p>
<p id="b582-11">“[MR. MAURO]: Shut up.</p>
<p id="b582-12">“MRS. MAURO: —taken him to a mental hospital or something. What’ll we do?</p>
<p id="Aqd"><page-number citation-index="1" label="523">*523</page-number>“[MR. MAURO]: Shut up.</p>
<p id="A1c">“DET. MANSON: Do you know a reverend or a priest or someone you can talk to — take care of David?</p>
<p id="AWq">“MRS. MAURO: No.</p>
<p id="AQX">“[MR. MAURO]: Don’t answer questions until you get rights of attorney before you find out whats <em>[sic] </em>going on. You tried to stop me as best you can. What are you going to do, kill me? You tried the best you can to stop me.</p>
<p id="AyE">“MRS. MAURO: I don’t — we don’t — I don’t have money.</p>
<p id="A57">“[MR. MAURO]: There’s a public attorney.</p>
<p id="Aq_">“MRS. MAURO: I don’t know.</p>
<p id="AB0">“[MR. MAURO]: There’s a public attorney. Why don’t you just be quiet.</p>
<p id="AnT">“MRS. MAURO: I don’t have any money to bury him. I don’t have any money. All I got is enough money for the rent for the children and that’s it.</p>
<p id="Ahfh">“DET. MANSON: Did you want to talk to your husband any more?</p>
<p id="AFZ">“MRS. MAURO: No, I can’t talk to him.</p>
<p id="AUR">“[MR. MAURO]: Then don’t talk to me — get out.</p>
<p id="A4Y">“MRS. MAURO: I don’t know what to do. O.K.”</p>
<p id="A-O"><span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/#30" aria-description="Citation for case: State v. Mauro">149 Ariz. 24, 30-31</a></span>, <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/#399" aria-description="Citation for case: State v. Mauro">716 P. 2d 393, 399-400</a></span> (1986).</p>
</footnote>
<footnote label="2">
<p id="b584-7"> The court relied on testimony of the officers at the hearing in the trial court on the suppression motion. Sergeant Allen testified as follows:</p>
<p id="b584-8">“Q. [C]ertainly when you sent an officer in there to listen to that conversation, you knew that it was possible that he might make incriminating statements?</p>
<p id="b584-9"><em>“A. </em>That’s correct.</p>
<p id="b584-10">“Q. And obviously, you wanted to record that conversation so as to have a record of those incriminating statements.</p>
<p id="b584-11">“A. That’s correct.” <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/#30" aria-description="Citation for case: State v. Mauro"><em>Id., </em>at 30</a></span>, <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/#399" aria-description="Citation for case: State v. Mauro">716 P. 2d, at 399</a></span>. Detective Manson’s testimony was as follows:</p>
<p id="b584-13">“Q. [Detective Manson], certainly you were aware that during the conversation either [Mrs. Mauro] or my client may have given an incriminating statement?</p>
<p id="b584-14">“A. Yes.</p>
<p id="b584-15">“Q. And obviously one of the purposes of your tape recording the interview was to take down any such statements?</p>
<p id="A4dC"><page-number citation-index="1" label="525">*525</page-number>“A. Yes, sir.” <em><span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/" aria-description="Citation for case: State v. Mauro">Ibid.</a></span></em></p>
</footnote>
<footnote label="3">
<p id="b585-5"> In <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964), the Court held that the Fourteenth Amendment requires observance of this privilege in state-court proceedings.</p>
</footnote>
<footnote label="4">
<p id="b587-4"> In the course of the conversation, that apparently lasted only a few minutes, Manson made two statements, both apparently directed at Mauro’s wife. See n. 1, <em>supra.</em></p>
</footnote>
<footnote label="5">
<p id="b587-6"> Justice Stevens suggests that the officers “employed a powerful psychological ploy.” <em>Post, </em>at 531. He bases this statement on his reading of the record that the officers “failed to give respondent any advance warning that Mrs. Mauro was coming to talk to him, that a police officer would accompany her, or that their conversation would be recorded.” <em>Ibid. </em>This reading is difficult to reconcile with the trial court’s conclusion that the officers “told both Mr. and Mrs. Mauro that they could speak together only if an officer were present in the room to observe and hear what was going on.” App. 218. This sentence seems to indicate that Mauro received advance warning. But accepting the facts as Justice Stevens states them, the opinion still makes it clear that Mauro was fully informed before the conversation began. Similarly, it may be that the officers did not give Mr. Mauro advance warning that they would record the eonversa<page-number citation-index="1" label="528">*528</page-number>tion, but the trial court noted that “[t]he officer who was present produced a tape recorder and told the couple that their conversation would be recorded and put that tape recorder down on the desk in plain sight and taped their conversation, so they had knowledge that that was going on.” <em>Ibid. </em>Justice Stevens also implies that respondent was forced against his will to talk to his wife. <em>Post, </em>at 581. But, as the trial court observed, “[t]he defendant, with knowledge that the police were listening, could have chosen not to speak to his wife. Instead, he chose to speak.” App. 219. In short, the trial court’s findings completely rebut the atmosphere of oppressive police conduct portrayed by the dissent.</p>
</footnote>
<footnote label="6">
<p id="b588-11"> The dissent suggests that the Arizona Supreme Court found as a fact that the officers intended to interrogate Mauro and faults us for reversing this allegedly factual finding. With due respect, we disagree with this reading of the record. The Arizona Supreme Court did not conclude that the officers intended to interrogate Mauro. Rather it concluded that <page-number citation-index="1" label="529">*529</page-number>“[t]hey both knew that . . . incriminating statements were likely to be made.” <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/#31" aria-description="Citation for case: State v. Mauro">149 Ariz., at 31</a></span>, <span class="citation" data-id="1169190"><a href="/opinion/1169190/state-v-mauro/#400" aria-description="Citation for case: State v. Mauro">716 P. 2d, at 400</a></span>. Taken in context, this is a determination that the facts known to the officers satisfied the legal standard we established in <em>Rhode Island </em>v. <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span>. </em>Our decision today does not overturn any of the factual findings of the Arizona Supreme Court. Rather, it rests on a determination that the facts of this case do not present a sufficient likelihood of incrimination to satisfy the legal standard articulated in <em>Miranda </em>v. <em>Arizona </em>and in <em>Rhode Island </em>v. <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span>.</em></p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Arizona v. Roberson.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Arizona v. Roberson"
type: case
citation: "486 U.S. 675 (1988)"
parallel_cite: "108 S. Ct. 2093; 100 L. Ed. 2d 704; 56 U.S.L.W. 4590"
neutral_cite: 1988 U.S. LEXIS 2726
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1988
date_decided: 1988-06-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1988-06-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Arizona v. Roberson
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112100/arizona-v-roberson/"
  cluster_id: 112100
  opinion_id: 9431349
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Edwards v. Arizona]]", "[[Minnick v. Mississippi]]", "[[Maryland v. Shatzer]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "right-to-counsel", "interrogation"]
holding: "The Edwards bar is not offense-specific — once a suspect invokes counsel, police may not interrogate him about ANY offense, including an…"
lake:
  record_id: Arizona v. Roberson
  status: verified
  projected_at: 2026-07-06
---

# Arizona v. Roberson

*486 U.S. 675 (1988)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Roberson was arrested at the scene of a burglary and, after [[Miranda and Custodial Interrogation|Miranda warnings]], said he wanted a lawyer before answering any questions. Three days later, while he was still in custody, a different officer — unaware of the earlier invocation — gave fresh [[Miranda and Custodial Interrogation|Miranda warnings]] and questioned Roberson about a *different* burglary, and Roberson made an incriminating statement. He moved to suppress it.

## Issue
Whether the *[[Edwards v. Arizona|Edwards]]* rule barring police-initiated interrogation after a suspect invokes counsel applies when the later interrogation concerns a separate offense or investigation.

## Rule
Yes — the *[[Edwards v. Arizona|Edwards]]* bar is not offense-specific. "[T]he presumption raised by a suspect's request for counsel — that he considers himself unable to deal with the pressures of custodial interrogation without legal assistance — does not disappear simply because the police have approached the suspect, still in custody, still without counsel, about a separate investigation." — 486 U.S. at 683. ^pin-683

"That a suspect's request for counsel should apply to any questions the police wish to pose follows, we think, not only from *Edwards* and *Miranda* . . . ." — *Id.* at 684. ^pin-684

## Application
Roberson had asked for a lawyer before answering "any questions," and the presumption that he could not face custodial interrogation without counsel did not evaporate merely because a second officer approached him — still in custody, still without counsel — about a different burglary three days later. Fresh [[Miranda and Custodial Interrogation|Miranda warnings]] did not cure the bar, and the second officer's ignorance of the earlier invocation was irrelevant. The statement was therefore inadmissible.

## Conclusion
The *[[Edwards v. Arizona|Edwards]]* bar applied to the separate-investigation questioning; the suppression of Roberson's statement was upheld and the Arizona Court of Appeals affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Roberson* extends [[Edwards v. Arizona]] so that a counsel invocation bars police-initiated interrogation about **any** offense. The broader *[[Edwards v. Arizona|Edwards]]* line was later refined by [[Maryland v. Shatzer]] (a 14-day break in Miranda custody ends the *[[Edwards v. Arizona|Edwards]]* bar).

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *Arizona v. Roberson*, 486 U.S. 675 (1988) — https://www.courtlistener.com/opinion/112100/arizona-v-roberson/ — pinpoints: 683, 684.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ae22d491e13a15c8", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Arizona v. Roberson"}, "payload": {"all": [{"cite": "486 U.S. 675", "page": "675", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "486"}, {"cite": "108 S. Ct. 2093", "page": "2093", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "108"}, {"cite": "100 L. Ed. 2d 704", "page": "704", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "100"}, {"cite": "1988 U.S. LEXIS 2726", "page": "2726", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1988"}, {"cite": "56 U.S.L.W. 4590", "page": "4590", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "56"}], "display": "486 U.S. 675", "official": {"cite": "486 U.S. 675", "page": "675", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "486"}, "official_selection_present": true, "record_id": "Arizona v. Roberson"}}
{"assertion_id": "609fd7544cbb0ce5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-684", "record_id": "Arizona v. Roberson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-684", "pinpoint_status": "slip-only", "quote": "That a suspect's request for counsel should apply to any questions the police wish to pose follows, we think, not only from *Edwards* and *Miranda* . . . .", "quote_fidelity": "mismatch", "record_id": "Arizona v. Roberson", "star_marker": null}}
{"assertion_id": "db790b9d975d673a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-683", "record_id": "Arizona v. Roberson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-683", "pinpoint_status": "slip-only", "quote": "--- # Arizona v. Roberson *486 U.S. 675 (1988)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Roberson was arrested at the scene of a burglary and, after Miranda warnings, said he wanted a lawyer before answering any questions. Three days later, while he was still in custody, a different officer — unaware of the earlier invocation — gave fresh Miranda warnings and questioned Roberson about a *different* burglary, and Roberson made an incriminating statement. He moved to suppress it. ## Issue Whether the *Edwards* rule barring police-initiated interrogation after a suspect invokes counsel applies when the later interrogation concerns a separate offense or investigation. ## Rule Yes — the *Edwards* bar is not offense-specific.", "quote_fidelity": "mismatch", "record_id": "Arizona v. Roberson", "star_marker": null}}
{"assertion_id": "4ee8a793e87ddb2f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Arizona v. Roberson"}, "payload": {"as_of_content": "1988-06-15", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Arizona v. Roberson", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Arizona v. Roberson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arizona v. Roberson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Arizona v. Roberson",
    "case_name_short": "Roberson",
    "case_name_full": "Arizona v. Roberson",
    "input_case_name": "Arizona v. Roberson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1988-06-15",
    "year": 1988,
    "docket": null,
    "cluster_id": 112100,
    "lead_opinion_id": 9431349,
    "sibling_ids": [
      112100,
      9431349,
      9431350
    ],
    "absolute_url": "/opinion/112100/arizona-v-roberson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9074843,
        "score": 10,
        "case_name": "Arizona v. Roberson"
      },
      {
        "cluster_id": 9074842,
        "score": 10,
        "case_name": "Arizona v. Roberson"
      },
      {
        "cluster_id": 9074378,
        "score": 10,
        "case_name": "Arizona v. Roberson"
      },
      {
        "cluster_id": 9074377,
        "score": 10,
        "case_name": "Arizona v. Roberson"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "486 U.S. 675",
      "volume": "486",
      "reporter": "U.S.",
      "page": "675",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "108 S. Ct. 2093",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "2093",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 L. Ed. 2d 704",
        "volume": "100",
        "reporter": "L. Ed. 2d",
        "page": "704",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 U.S.L.W. 4590",
        "volume": "56",
        "reporter": "U.S.L.W.",
        "page": "4590",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1988 U.S. LEXIS 2726",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "2726",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "486 U.S. 675",
        "volume": "486",
        "reporter": "U.S.",
        "page": "675",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 S. Ct. 2093",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "2093",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 L. Ed. 2d 704",
        "volume": "100",
        "reporter": "L. Ed. 2d",
        "page": "704",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 U.S. LEXIS 2726",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "2726",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 U.S.L.W. 4590",
        "volume": "56",
        "reporter": "U.S.L.W.",
        "page": "4590",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "486 U.S. 675",
    "official_selection": {
      "court_class": "scotus",
      "selected": "486 U.S. 675",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-683",
      "page": null,
      "quote": "--- # Arizona v. Roberson *486 U.S. 675 (1988)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Roberson was arrested at the scene of a burglary and, after Miranda warnings, said he wanted a lawyer before answering any questions. Three days later, while he was still in custody, a different officer \u2014 unaware of the earlier invocation \u2014 gave fresh Miranda warnings and questioned Roberson about a *different* burglary, and Roberson made an incriminating statement. He moved to suppress it. ## Issue Whether the *Edwards* rule barring police-initiated interrogation after a suspect invokes counsel applies when the later interrogation concerns a separate offense or investigation. ## Rule Yes \u2014 the *Edwards* bar is not offense-specific.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-684",
      "page": null,
      "quote": "That a suspect's request for counsel should apply to any questions the police wish to pose follows, we think, not only from *Edwards* and *Miranda* . . . .",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1988-06-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Arizona v. Roberson",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. DeJong",
          "cluster_id": 2669581,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Garcia",
          "cluster_id": 2713978,
          "cite": [
            "2013 SD 46",
            "834 N.W.2d 821",
            "2013 WL 3226703",
            "2013 S.D. LEXIS 71"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane1_negative"
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
        "journal_ref": "Arizona v. Roberson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gobert",
          "cluster_id": 1947904,
          "cite": [
            "244 S.W.3d 861",
            "2008 Tex. App. LEXIS 742",
            "2008 WL 269448"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Van Hook v. Carl S. Anderson, Warden",
          "cluster_id": 793987,
          "cite": [
            "444 F.3d 830",
            "2006 U.S. App. LEXIS 9628",
            "2006 WL 997203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Houston v. State",
          "cluster_id": 1678067,
          "cite": [
            "185 S.W.3d 917",
            "2006 Tex. App. LEXIS 1352",
            "2006 WL 358070"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Moran v. State",
          "cluster_id": 1560713,
          "cite": [
            "171 S.W.3d 382",
            "2005 WL 1583847"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory Johnson, A/K/A Little Greg, United States of America v. Gregory Johnson, A/K/A Little Greg",
          "cluster_id": 789459,
          "cite": [
            "400 F.3d 187",
            "2005 WL 526889"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane1_negative"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dickerson v. United States",
          "cluster_id": 118380,
          "cite": [
            "147 L. Ed. 2d 405",
            "120 S. Ct. 2326",
            "530 U.S. 428",
            "2000 U.S. LEXIS 4305"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harper v. Virginia Department of Taxation",
          "cluster_id": 112890,
          "cite": [
            "125 L. Ed. 2d 74",
            "113 S. Ct. 2510",
            "509 U.S. 86",
            "1993 U.S. LEXIS 4212",
            "7 Fla. L. Weekly Fed. S 456",
            "16 Employee Benefits Cas. (BNA) 2313",
            "93 Daily Journal DAR 7730",
            "93 Cal. Daily Op. Serv. 4491",
            "61 U.S.L.W. 4664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Waidla",
          "cluster_id": 1316339,
          "cite": [
            "996 P.2d 46",
            "94 Cal. Rptr. 2d 396",
            "22 Cal. 4th 690",
            "22 Cal. 690",
            "2000 Daily Journal DAR 3605",
            "2000 Cal. Daily Op. Serv. 2687",
            "2000 Cal. LEXIS 2229"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Saffle v. Parks",
          "cluster_id": 112390,
          "cite": [
            "108 L. Ed. 2d 415",
            "110 S. Ct. 1257",
            "494 U.S. 484",
            "1990 U.S. LEXIS 1178",
            "58 U.S.L.W. 4322"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cunningham",
          "cluster_id": 2587254,
          "cite": [
            "25 P.3d 519",
            "108 Cal. Rptr. 2d 291",
            "25 Cal. 4th 926"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Perkins",
          "cluster_id": 112452,
          "cite": [
            "110 L. Ed. 2d 243",
            "110 S. Ct. 2394",
            "496 U.S. 292",
            "1990 U.S. LEXIS 2885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnick v. Mississippi",
          "cluster_id": 112513,
          "cite": [
            "112 L. Ed. 2d 489",
            "111 S. Ct. 486",
            "498 U.S. 146",
            "1990 U.S. LEXIS 6118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leif Taylor v. Thomas M. Maddox, Interim Director George Galaza Cal Terhune",
          "cluster_id": 786028,
          "cite": [
            "366 F.3d 992",
            "2004 U.S. App. LEXIS 9068",
            "2004 WL 1043343"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Crittenden",
          "cluster_id": 2614001,
          "cite": [
            "885 P.2d 887",
            "9 Cal. 4th 83",
            "36 Cal. Rptr. 2d 474",
            "94 Daily Journal DAR 18013",
            "94 Cal. Daily Op. Serv. 9702",
            "1994 Cal. LEXIS 6570"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Shatzer",
          "cluster_id": 1734,
          "cite": [
            "175 L. Ed. 2d 1045",
            "130 S. Ct. 1213",
            "559 U.S. 98",
            "2010 U.S. LEXIS 1899"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Butler v. McKellar",
          "cluster_id": 112387,
          "cite": [
            "108 L. Ed. 2d 347",
            "110 S. Ct. 1212",
            "494 U.S. 407",
            "1990 U.S. LEXIS 1246"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1801669,
          "cite": [
            "49 Cal. 4th 405",
            "2010 D.A.R. 10",
            "111 Cal. Rptr. 3d 589",
            "233 P.3d 1000",
            "2010 Cal. LEXIS 5970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "J. D. B. v. North Carolina",
          "cluster_id": 218925,
          "cite": [
            "180 L. Ed. 2d 310",
            "131 S. Ct. 2394",
            "564 U.S. 261",
            "2011 U.S. LEXIS 4557",
            "22 Fla. L. Weekly Fed. S 1135",
            "79 U.S.L.W. 4504"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herron v. State",
          "cluster_id": 2351946,
          "cite": [
            "86 S.W.3d 621",
            "2002 Tex. Crim. App. LEXIS 197",
            "2002 WL 31255420"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Spotz",
          "cluster_id": 2074443,
          "cite": [
            "896 A.2d 1191",
            "587 Pa. 1",
            "2006 Pa. LEXIS 659"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1407706,
          "cite": [
            "14 Cal. 4th 1005",
            "929 P.2d 544",
            "97 Daily Journal DAR 899",
            "97 Cal. Daily Op. Serv. 520",
            "60 Cal. Rptr. 2d 225",
            "1997 Cal. LEXIS 9"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Roberson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112100 OR 9431349 OR 9431350) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDE2NTgyNDAwMDAwJnM9MTgyMTk3MiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112100+OR+9431349+OR+9431350%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112100 OR 9431349 OR 9431350)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMTYmcz0zMTU5OTk1JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112100+OR+9431349+OR+9431350%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112100 OR 9431349 OR 9431350)",
        "reviewed": 11,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 11,
        "triage_read": 0,
        "triage_snippet_classified": 11
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112100 OR 9431349 OR 9431350)",
    "indexed_citing_opinions": 589,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112100,
        "count": 547,
        "count_source": "search"
      },
      {
        "opinion_id": 9431349,
        "count": 53,
        "count_source": "search"
      },
      {
        "opinion_id": 9431350,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 963,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/arizona-v-roberson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY3NTc0MTcmcz00NzUxMDkzJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112100+OR+9431349+OR+9431350%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112100,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 110809,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 110987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111796,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 111798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 419689,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 484283,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 487174,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1177179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1278606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1305977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1314131,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1434323,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1615933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1713623,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1721254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1817395,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112100,
        "cited_id": 1983609,
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
    "date_created": "2026-07-04T18:40:48Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:41:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:41:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:46:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:41:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Arizona v. Roberson

```
<opinion type="majority">
<author id="b735-8">Justice Stevens</author>
<p id="ADqQ">delivered the opinion of the Court.</p>
<p id="b735-9">In <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477, 484-485</a></span> (1981), we held that a suspect who has “expressed his desire to deal with the police only through counsel is not subject to further interrogation by the authorities until counsel has been made available to him, unless the accused himself initiates further communication, exchanges, or conversations with the police.” In this case Arizona asks us to craft an exception to that rule for cases in which the police want to interrogate a suspect about an offense that is unrelated to the subject of their initial interrogation. Several years ago the Arizona Supreme Court considered, and rejected, a similar argument, stating:</p>
<blockquote id="b735-10">“The only difference between Edwards and the appellant is that Edwards was questioned about the same of<page-number citation-index="1" label="678">*678</page-number>fense after a request for counsel while the appellant was reinterrogated about an unrelated offense. We do not believe that this factual distinction holds any legal significance for fifth amendment purposes. ” <em>State </em>v. <em>Routhier, </em><span class="citation" data-id="1177179"><a href="/opinion/1177179/state-v-routhier/#97" aria-description="Citation for case: State v. Routhier">137 Ariz. 90, 97</a></span>, <span class="citation" data-id="1177179"><a href="/opinion/1177179/state-v-routhier/#75" aria-description="Citation for case: State v. Routhier">669 P. 2d 68, 75</a></span> (1983), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./464/1073/">464 U. S. 1073</a></span> (1984).</blockquote>
<p id="b736-9">We agree with the Arizona Supreme Court’s conclusion.</p>
<p id="b736-10">PH</p>
<p id="b736-3">On April 16, 1985, respondent was arrested at the scene of a just-completed burglary. The arresting officer advised him that he had a constitutional right to remain silent and also the right to have an attorney present during any interrogation. See <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 467-479</a></span> (1966). Respondent replied that he “wanted a lawyer before answering any questions.”<footnotemark>1</footnotemark> This fact was duly recorded in the officer’s written report of the incident. In due course, respondent was convicted of the April 16, 1985, burglary.</p>
<p id="b736-4">On April 19, 1985, while respondent was still in custody pursuant to the arrest three days earlier, a different officer interrogated him about a different burglary that had occurred on April 15. That officer was not aware of the fact that respondent had requested the assistance of counsel three days earlier. After advising respondent of his rights, the officer obtained an incriminating statement concerning the April 15 burglary. In the prosecution for that offense, the trial court suppressed that statement. In explaining his ruling, the trial judge relied squarely on the Arizona Supreme Court’s opinion in <em>State </em>v. <em>Routhier, </em><span class="citation" data-id="1177179"><a href="/opinion/1177179/state-v-routhier/#97" aria-description="Citation for case: State v. Routhier">137 Ariz., at 97</a></span>, <span class="citation" data-id="1177179"><a href="/opinion/1177179/state-v-routhier/#75" aria-description="Citation for case: State v. Routhier">669 P. 2d, at 75</a></span>, characterizing the rule of the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>case as “clear and unequivocal.”<footnotemark>2</footnotemark></p>
<p id="b737-4"><page-number citation-index="1" label="679">*679</page-number>The Arizona Court of Appeals affirmed the suppression order in a brief opinion, stating:</p>
<blockquote id="b737-5">“In <em><span class="citation" data-id="1177179"><a href="/opinion/1177179/state-v-routhier/" aria-description="Citation for case: State v. Routhier">Routhier</a></span>, </em>as in the instant case, the accused was continuously in police custody from the time of asserting his Fifth Amendment right through the time of the impermissible questioning. The coercive environment never dissipated.” App. to Pet. for Cert. 24.</blockquote>
<p id="b737-6">The Arizona Supreme Court denied a petition for review. <em>Id., </em>at 25. We granted certiorari to resolve a conflict with certain other state court decisions.<footnotemark>3</footnotemark> <span class="citation multiple-matches"><a href="/c/U.%20S./484/975/">484 U. S. 975</a></span> (1987). We now affirm.</p>
<p id="b738-9"><page-number citation-index="1" label="680">*680</page-number>hH HH</p>
<p id="b738-1">A major purpose of the Court’s opinion in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#441" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 441-442</a></span>, was “to give concrete constitutional guidelines for law enforcement agencies and courts to follow.” “As we have stressed on numerous occasions, ‘[o]ne of the principal advantages’ of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>is the ease and clarity of its application. <em>Berkemer </em>v. <em>McCarty, </em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#430" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 430</a></span> (1984); see also <em>New York </em>v. <em>Quarles, </em>[<span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#662" aria-description="Citation for case: New York v. Quarles">467 U. S. 649, 662-664</a></span> (1984)] (concurring opinion); <em>Fare </em>v. <em>Michael C., </em>442 U. S. [707, 718 (1979)].” <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#425" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 425</a></span> (1986).</p>
<p id="b738-2">The rule of the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>case came as a corollary to <em>Miranda's, </em>admonition that “[i]f the individual states that he wants an attorney, the interrogation must cease until an attorney is present.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 474</a></span>. In such an instance, we had concluded in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>“[i]f the interrogation continues without the presence of an attorney and a statement is taken, a heavy burden rests on the government to demonstrate that the defendant knowingly and intelligently waived his privilege against self-incrimination and his right to retained or appointed counsel.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 475</a></span>. In <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>, </em>we “reconfirmed] these views and, to lend them substance, emphasize[d] that it is inconsistent with <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and its progeny for the authorities, at their instance, to reinterro-gate an accused in custody if he has clearly asserted his right to counsel.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#485" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 485</a></span>. We concluded that re-interrogation may only occur if “the accused himself initiates <page-number citation-index="1" label="681">*681</page-number>farther communication, exchanges, or conversations with the police.” <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Ibid.</a></span> </em>Thus, the prophylactic protections that the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings provide to counteract the “inherently compelling pressures” of custodial interrogation and to “permit a full opportunity to exercise the privilege against self-incrimination,” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>, are implemented by the application of the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>corollary that if a suspect believes that he is not capable of undergoing such questioning without advice of counsel, then it is presumed that any subsequent waiver that has come at the authorities’ behest, and not at the suspect’s own instigation, is itself the product of the “inherently compelling pressures” and not the purely voluntary choice of the suspect. As Justice White has explained, “the accused having expressed his own view that he is not competent to deal with the authorities without legal advice, a later decision at the authorities’ insistence to make a statement without counsel’s presence may properly be viewed with skepticism.” <em>Michigan </em>v. <em>Mosley, </em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#110" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 110, n. 2</a></span> (1975) (concurring in result).</p>
<p id="b739-5">We have repeatedly emphasized the virtues of a bright-line rule in cases following <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>as well as <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>See <em>Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#634" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625, 634</a></span> (1986); <em>Smith </em>v. <em>Illinois, </em><span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#98" aria-description="Citation for case: Smith v. Illinois">469 U. S. 91, 98</a></span> (1984) <em>(per curiam); Solem </em>v. <em>Stumes, </em><span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/#646" aria-description="Citation for case: Solem v. Stumes">465 U. S. 638, 646</a></span> (1984); see also <em>Shea </em>v. <em>Louisiana, </em><span class="citation" data-id="9429912"><a href="/opinion/111355/shea-v-louisiana/" aria-description="Citation for case: Shea v. Louisiana">470 U. S. 51</a></span> (1985); <em>Oregon </em>v. <em>Bradshaw, </em><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1044" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S. 1039, 1044</a></span> (1983) (plurality opinion) (Rehnquist, J.). In <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#718" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 718</a></span> (1979), we explained that the “relatively rigid requirement that interrogation must cease upon the accused’s request for an attorney . . . has the virtue of informing police and prosecutors with specificity as to what they may do in conducting custodial interrogation, and of informing courts under what circumstances statements obtained during such interrogation are not admissible. This gain in specificity, which benefits the accused and the State alike, has been thought to outweigh the burdens that the de-<page-number citation-index="1" label="682">*682</page-number>cisión in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>imposes on law enforcement agencies and the courts by requiring the suppression of trustworthy and highly probative evidence even though the confession might be voluntary under traditional Fifth Amendment analysis.”<footnotemark>4</footnotemark> The <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule thus serves the purpose of providing “clear and unequivocal” guidelines to the law enforcement profession. Surely there is nothing ambiguous about the requirement that after a person in custody has expressed his desire to deal with the police only through counsel, he “is not subject to further interrogation by the authorities until counsel has been made available to him, unless the accused himself initiates further communication, exchanges, or conversations with the police.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484-485</a></span>.</p>
<p id="b740-10">I » — I HH</p>
<p id="b740-3">Petitioner contends that the bright-line, prophylactic <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule should not apply when the police-initiated interrogation following a suspect’s request for counsel occurs in the context of a separate investigation. According to petitioner, both our cases and the nature of the factual setting compel this distinction. We are unpersuaded.</p>
<p id="b741-4"><page-number citation-index="1" label="683">*683</page-number>Petitioner points to our holding in <em>Michigan </em>v. <em>Mosley, </em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">423 U. S., at 103</a></span>-104 (quoting <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 479</a></span>), that when a suspect asserts his right to cut off questioning, the police may “ ‘scrupulously honor’ ” that right by “immediately ceas[ing] the interrogation, resum[ing] questioning only after the passage of a significant period of time and the provision of a fresh set of warnings, and restrict[ing] the second interrogation to a crime that had not been a subject of the earlier interrogation.” <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#106" aria-description="Citation for case: Michigan v. Mosley">423 U. S., at 106</a></span>. The police in this case followed precisely that course, claims the State. However, as <em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">Mosley</a></span> </em>made clear, a suspect’s decision to cut off questioning, unlike his request for counsel, does not raise the presumption that he is unable to proceed without a lawyer’s advice. See <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#101" aria-description="Citation for case: Michigan v. Mosley"><em>id., </em>at 101, n. 7</a></span>; <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#110" aria-description="Citation for case: Michigan v. Mosley"><em>id., </em>at 110, n. 2</a></span> (White, J., concurring in result), quoted <em>supra, </em>at 681.</p>
<p id="b741-5">Petitioner points as well to <em>Connecticut </em>v. <em>Barrett, </em><span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/#525" aria-description="Citation for case: Connecticut v. Barrett">479 U. S. 523, 525</a></span> (1987), which concerned a suspect who had “told the officers that he would not give a written statement unless his attorney was present but had ‘no problem’ talking about the incident.” We held that this was a limited request for counsel, that Barrett himself had drawn a distinction between oral and written statements and thus that the officers could continue to question him. Petitioner argues that Roberson’s request for counsel was similarly limited, this time to the investigation pursuant to which the request was made. This argument is flawed both factually and legally. As a matter of fact, according to the initial police report, respondent stated that “he wanted a lawyer before answering <em>any </em>questions.”<footnotemark>5</footnotemark> As a matter of law, the presumption raised by a suspect’s request for counsel — that he considers himself unable to deal with the pressures of custodial interrogation without legal assistance — does not disappear simply because the police have approached the suspect, still in custody, still without counsel, about a separate investigation.</p>
<p id="b742-4"><page-number citation-index="1" label="684">*684</page-number>That a suspect’s request for counsel should apply to any questions the police wish to pose follows, we think, not only from <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>and <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>but also from a case decided the same day as <em><span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/" aria-description="Citation for case: Connecticut v. Barrett">Barrett</a></span>. </em>In <em>Colorado </em>v. <em>Spring, </em><span class="citation" data-id="9430793"><a href="/opinion/111798/colorado-v-spring/#577" aria-description="Citation for case: Colorado v. Spring">479 U. S. 564, 577</a></span> (1987), we held that “a suspect’s awareness of all the possible subjects of questioning in advance of interrogation is not relevant to determining whether the suspect voluntarily, knowingly, and intelligently waived his Fifth Amendment privilege.” In the face of the warning'that anything he said could be used as evidence against him, Spring’s willingness to answer questions, without limiting such a waiver, see <em>Connecticut </em>v. <em><span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/" aria-description="Citation for case: Connecticut v. Barrett">Barrett, supra,</a></span> </em>indicated that he felt comfortable enough with the pressures of custodial interrogation both to answer questions and to do so without an attorney. Since there is “no qualification of [the] broad and explicit warning” that <em>“anything </em>[a suspect] says may be used against him,” 479 U. S., at 577 (emphasis in original), Spring’s decision to talk was properly considered to be equally unqualified. Conversely, Roberson’s unwillingness to answer any questions without the advice of counsel, without limiting his request for counsel, indicated that he did not feel sufficiently comfortable with the pressures of custodial interrogation to answer questions without an attorney. This discomfort is precisely the state of mind that <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>presumes to persist unless the suspect himself initiates further conversation about the investigation; unless he otherwise states, see <em>Connecticut </em>v. <em><span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/" aria-description="Citation for case: Connecticut v. Barrett">Barrett, supra,</a></span> </em>there is no reason to assume that a suspect’s state of mind is in any' way investigation-specific, see <em>Colorado </em>v. <em><span class="citation" data-id="9430793"><a href="/opinion/111798/colorado-v-spring/" aria-description="Citation for case: Colorado v. Spring">Spring, supra.</a></span></em></p>
<p id="b742-5">Finally, petitioner raises the case of <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#161" aria-description="Citation for case: Maine v. Moulton">474 U. S. 159, 161</a></span> (1985), which held that Moulton’s “Sixth Amendment right to the assistance of counsel was violated by the admission at trial of incriminating statements made by him to his codefendant, a secret government informant, after indictment and at a meeting of the two to plan defense strategy for the upcoming trial.” That case did not involve any <page-number citation-index="1" label="685">*685</page-number><em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>issue because Moulton was not in custody. In our opinion, we rejected an argument that the statements should be admissible because the police were seeking information regarding both the crime for which Moulton had already been indicted, and a separate, inchoate scheme. Following <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#207" aria-description="Citation for case: Massiah v. United States">377 U. S. 201, 207</a></span> (1964), we recognized, though, that the continuing investigation of uncharged offenses did not violate the defendant’s Sixth Amendment right to the assistance of counsel. Our recognition of that fact, however, surely lends no support to petitioner’s argument that in the Fifth Amendment context, “statements about different offenses, developed at different times, by different investigators, in the course of two wholly independent investigations, should not be treated the same.” Brief for Petitioner 32. This argument overlooks the difference between the Sixth Amendment right to counsel and the Fifth Amendment right against self-incrimination. The former arises from the fact that the suspect has been formally charged with a particular crime and thus is facing a state apparatus that has been geared up to prosecute him. The latter is protected by the prophylaxis of having an attorney present to counteract the inherent pressures of custodial interrogation, which arise from the fact of such interrogation and exist regardless of the number of crimes under investigation or whether those crimes have resulted in formal charges.</p>
<p id="b743-6">In sum, our cases do not support petitioner’s position.</p>
<p id="b743-8"><em>&gt; </em>HH</p>
<p id="b743-3">Petitioner’s attempts at distinguishing the factual setting here from that in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>are equally unavailing. Petitioner first relies on the plurality opinion in <em>Oregon </em>v. <em>Bradshaw, </em><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1044" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S., at 1044</a></span> (Rehnquist, J.), which stated that <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>laid down “a prophylactic rule, designed to protect an accused in police custody from being badgered by police officers in the manner in which the defendant in <em>Ed</em><page-number citation-index="1" label="686">*686</page-number><em>wards </em>was.” Petitioner reasons that “the chances that an accused will be questioned so repeatedly and in such quick succession that it will ‘undermine the will’ of the person questioned, or will constitute ‘badger[ing],’ are so minute as not to warrant consideration, if the officers are truly pursuing separate investigations.” Brief for Petitioner 16. It is by no means clear, though, that police engaged in separate investigations will be any less eager than police involved in only one inquiry to question a suspect in custody. Further, to a suspect who has indicated his inability to cope with the pressures of custodial interrogation by requesting counsel, any further interrogation without counsel having been provided will surely exacerbate whatever compulsion to speak the suspect may be feeling. Thus, we also disagree with petitioner’s contention that fresh sets of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings will “reassure” a suspect who has been denied the counsel he has clearly requested that his rights have remained untrammeled. See <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">ibid.</a></span> </em>Especially in a case such as this, in which a period of three days elapsed between the unsatisfied request for counsel and the interrogation about a second offense, there is a serious risk that the mere repetition of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings would not overcome the presumption of coercion that is created by prolonged police custody.<footnotemark>6</footnotemark></p>
<p id="b745-4"><page-number citation-index="1" label="687">*687</page-number>The United States, as <em>amicus curiae </em>supporting petitioner, suggests that a suspect in custody might have “good reasons for wanting to speak with the police about the offenses involved in the new investigation, or at least to learn from the police what the new investigation is about so that he can decide whether it is in his interest to make a statement about that matter without the assistance of counsel.” Brief for United States as <em>Amicus Curiae </em>11. The simple answer is that the suspect, having requested counsel, can determine how to deal with the separate investigations with counsel’s advice. Further, even if the police have decided temporarily not to provide counsel, see n. 6, <em>supra, </em>they are free to inform the suspect of the facts of the second investigation as long as such communication does not constitute interrogation, see <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291</a></span> (1980). As we have made clear, any “further communication, exchanges, or conversations with the police” that the suspect himself initiates, <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#485" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 485</a></span>, are perfectly valid.</p>
<p id="b745-5">Finally, we attach no significance to the fact that the officer who conducted the second interrogation did not know that respondent had made a request for counsel. In addition to the fact that <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>focuses on the state of mind of the suspect and not of the police, custodial interrogation must be conducted pursuant to established procedures, and those procedures in turn must enable an officer who proposes to initiate an interrogation to determine whether the suspect has previously requested counsel. In this case respondent’s request had been properly memorialized in a written report but the officer who conducted the interrogation simply failed to examine that report. Whether a contemplated reinterrogation concerns the same or a different offense, or whether the same or different law enforcement authorities are involved in the second investigation, the same need to determine <page-number citation-index="1" label="688">*688</page-number>whether the suspect has requested counsel exists.<footnotemark>7</footnotemark> The police department’s failure to honor that request cannot be justified by the lack of diligence of a particular officer. Cf. <em>Giglio </em>v. <em>United States, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 154</a></span> (1972).</p>
<p id="b746-5">The judgment of the Arizona Court of Appeals is</p>
<p id="b746-6">
<em>Affirmed.</em>
</p>
<p id="b746-7">Justice O’Connor took no part in the consideration or decision of this case.</p>
<footnote label="1">
<p id="b736-5"> Tr. 26 (Apr. 3, 1986).</p>
</footnote>
<footnote label="2">
<p id="b736-6"> “Routhier was based on Edwards versus Arizona which held that once the defendant has invoked his right to counsel, he may not be re-<page-number citation-index="1" label="679">*679</page-number>interrogated unless counsel has been made available to him or he initiates the conversation.</p>
<blockquote id="b737-8">“The Routhier court states that whether the defendant is re-interrogated about the same offense or an unrelated offense makes no difference for Fifth Amendment purposes.</blockquote>
<blockquote id="b737-9">“The Routhier court further stated that Edwards is clear and unequivocal, there is to be no further interrogation by authorities once the right to counsel is invoked. The Court in that ease finding that the assertion of the right to counsel is an assertion by the accused that he is not competent to deal with authorities without legal advice. And that the resumption of questioning by the police without the requested attorney being provided, strongly suggests to the accused that he has no choice but to answer.” App. to Pet. for Cert. 15-16.</blockquote>
</footnote>
<footnote label="3">
<p id="b737-10"> See <em>State </em>v. <em>Dampier, </em><span class="citation" data-id="1314131"><a href="/opinion/1314131/state-v-dampier/" aria-description="Citation for case: State v. Dampier">314 N. C. 292</a></span>, <span class="citation" data-id="1314131"><a href="/opinion/1314131/state-v-dampier/" aria-description="Citation for case: State v. Dampier">333 S. E. 2d 230</a></span> (1985) <em>(Edwards </em>inapplicable to interrogation by authorities from different State concerning unrelated matter); <em>McFadden </em>v. <em>Commonwealth, </em><span class="citation" data-id="1305977"><a href="/opinion/1305977/mcfadden-v-commonwealth/" aria-description="Citation for case: McFadden v. Commonwealth">225 Va. 103</a></span>, <span class="citation" data-id="1305977"><a href="/opinion/1305977/mcfadden-v-commonwealth/" aria-description="Citation for case: McFadden v. Commonwealth">300 S. E. 2d 924</a></span> (1983) <em>(Edwards </em>inapplicable when authorities from different county question suspect about different crime); see also <em>Lofton </em>v. <em>State, </em><span class="citation" data-id="1817395"><a href="/opinion/1817395/lofton-v-state/" aria-description="Citation for case: Lofton v. State">471 So. 2d 665</a></span> (Fla. App.) (no <em>Edwards </em>violation when suspect is represented by attorney in unrelated matter, then questioned without counsel present), review denied, <span class="citation no-link">480 So. 2d 1294</span> (Fla. 1985); <em>State </em>v. <em>Newton, </em><span class="citation" data-id="1278606"><a href="/opinion/1278606/state-v-newton/" aria-description="Citation for case: State v. Newton">682 P. 2d 295</a></span> (Utah 1984) (same); <em>State </em>v. <em>Cornethan, </em><span class="citation" data-id="1434323"><a href="/opinion/1434323/state-v-cornethan/" aria-description="Citation for case: State v. Cornethan">38 Wash. App. 231</a></span>, <span class="citation" data-id="1434323"><a href="/opinion/1434323/state-v-cornethan/" aria-description="Citation for case: State v. Cornethan">684 P. 2d 1355</a></span> (1984) (alternative holding: <em>Edwards </em>inapplicable to interrogation in unrelated investigation; court also holds that representation by attorney in unrelated matter does not suffice as request for counsel for <em>Edwards </em>purposes); cf. <em>State </em>v. <em>Harriman, </em><span class="citation" data-id="1721254"><a href="/opinion/1721254/state-v-harriman/" aria-description="Citation for case: State v. Harriman">434 So. 2d 551</a></span> (La. App.) (adopts petitioner’s view here, but only after holding that suspect had initiated conversation regarding second investigation), writ denied, <span class="citation multiple-matches"><a href="/c/So.%202d/440/729/">440 So. 2d 729</a></span> (La. <page-number citation-index="1" label="680">*680</page-number>1983); but see <em>United States ex rel. Espinoza </em>v. <em>Fairman, </em><span class="citation" data-id="484283"><a href="/opinion/484283/united-states-of-america-ex-rel-miguel-a-espinoza-v-jw-fairman-warden/#124" aria-description="Citation for case: United States of America Ex Rel. Miguel A. Espinoza v....">813 F. 2d 117, 124-126</a></span> (CA7) (same rule as Arizona), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./483/1010/">483 U. S. 1010</a></span> (1987); <em>Luman </em>v. <span class="citation" data-id="1713623"><a href="/opinion/1713623/luman-v-state/" aria-description="Citation for case: Luman v. State"><em>State, 447 </em>So. 2d 428</a></span> (Fla. App. 1984). (same); <em>Radovsky </em>v. <em>State, </em><span class="citation" data-id="1983609"><a href="/opinion/1983609/radovsky-v-state/" aria-description="Citation for case: Radovsky v. State">296 Md. 386</a></span>, <span class="citation" data-id="1983609"><a href="/opinion/1983609/radovsky-v-state/" aria-description="Citation for case: Radovsky v. State">464 A. 2d 239</a></span> (1983) (same); see also <em>Boles </em>v. <em>Foltz, </em><span class="citation" data-id="9476074"><a href="/opinion/487174/robert-lee-boles-jr-v-dale-foltz-warden/#1137" aria-description="Citation for case: Robert Lee Boles, Jr. v. Dale Foltz, Warden">816 F. 2d 1132, 1137-1141</a></span> (CA6) (Gibson, J., dissenting) (same; majority does not reach issue), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./484/857/">484 U. S. 857</a></span> (1987); cf. <em>United States </em>v. <em>Scalf, </em><span class="citation" data-id="419689"><a href="/opinion/419689/united-states-v-george-a-scalf-jr/#1544" aria-description="Citation for case: United States v. George A. Scalf, Jr.">708 F. 2d 1540, 1544</a></span> (CA10 1983) (knowledge of request for counsel “is imputed to all law enforcement officers who subsequently deal with the suspect”); <em>State </em>v. <em>Arceneaux, </em><span class="citation" data-id="1615933"><a href="/opinion/1615933/state-v-arceneaux/" aria-description="Citation for case: State v. Arceneaux">425 So. 2d 740</a></span> (La. 1983) (same).</p>
</footnote>
<footnote label="4">
<p id="b740-4"> It is significant that our explanation of the basis for the <em>“per se </em>aspect of <em>Miranda” </em>in <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#719" aria-description="Citation for case: Fare v. Michael C.">442 U. S., at 719</a></span>, applies to the application of the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule in a case such as this. As we stated in <em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/" aria-description="Citation for case: Fare v. Michael C.">Fare</a></span>:</em></p>
<blockquote id="b740-5">“The rule in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> . . </em>. was based on this Court’s perception that the lawyer occupies a critical position in our legal system because of his unique ability to protect the Fifth Amendment rights of a client undergoing custodial interrogation. Because of this special ability of the lawyer to help the client preserve his Fifth Amendment rights once the client becomes enmeshed in the adversary process, the Court found that ‘the right to have counsel present at the interrogation is indispensable to the protection of the Fifth Amendment privilege under the system’ established by the Court. [384 U. S.], at 469. Moreover, the lawyer’s presence helps guard against overreaching by the police and ensures that any statements actually obtained are accurately transcribed for presentation into evidence. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#470" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 470</a></span>.</blockquote>
<blockquote id="b740-6">“The <em>per se </em>aspect of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was thus based on the unique role the lawyer plays in the adversary system of criminal justice in this country.” <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#719" aria-description="Citation for case: Fare v. Michael C.">442 U. S., at 719</a></span>.</blockquote>
</footnote>
<footnote label="5">
<p id="b741-6"> Tr. 26 (Apr. 3, 1986) (emphasis added); see <em>id., </em>at 23; Tr. 12 (Oct. 17, 1985, a.m.).</p>
</footnote>
<footnote label="6">
<p id="b744-5"> The United States, as <em>amicus curiae </em>supporting petitioner, suggests similarly that “respondent’s failure to reiterate his request for counsel to [the officer involved in the second investigation], even, after [that officer] gave respondent complete <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, could not have been the result of any doubt on respondent’s part that the police would honor a request for counsel if one were made.” Brief for United States as <em>Amicus Curiae </em>10. This conclusion is surprising, considering that respondent had not been provided with the attorney he had already requested, despite having been subjected to police-initiated interrogation with respect to the first investigation as well. See n. 7, <em>infra. </em>We reiterate here, though, that the “right” to counsel to protect the Fifth Amendment right against self-incrimination is not absolute; that is, “[i]f authorities conclude that they will not provide counsel during a reasonable period of time in which investigation in the field is carried out, they may refrain from doing so without violating the person’s Fifth Amendment privilege so long as they <page-number citation-index="1" label="687">*687</page-number>do not question him during that time.” <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 474</a></span> (1966).</p>
</footnote>
<footnote label="7">
<p id="b746-10"> Indeed, the facts of this case indicate that different officers investigating the same offense are just as likely to bypass proper procedures as an officer investigating a different offense, inasmuch as the record discloses no less than five violations of the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule, four concerning the April 16 burglary and only one concerning the April 15 burglary. See Tr. 23-24, 49 (Apr. 3, 1986); Tr. 8-12 (Oct. 17, 1985, p.m.). It is only the last violation that is at issue in this case.</p>
</footnote>
</opinion>
```

---
