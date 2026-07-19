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

## GROUP: content/cases/Michigan v. DeFillippo.md  (`case`, 5 assertions)

### content_page

```
---
title: "Michigan v. DeFillippo"
type: case
citation: "443 U.S. 31 (1979)"
parallel_cite: "99 S. Ct. 2627; 61 L. Ed. 2d 343"
neutral_cite: 1979 U.S. LEXIS 135
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-06-25
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1979-06-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Michigan v. DeFillippo
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110127/michigan-v-defillippo/"
  cluster_id: 110127
  opinion_id: 110127
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Leon]]", "[[Illinois v. Krull]]", "[[Herring v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "probable-cause", "arrest", "good-faith"]
holding: "An arrest based on a presumptively valid ordinance later declared unconstitutional was valid (supported by probable cause at the time),…"
lake:
  record_id: Michigan v. DeFillippo
  status: verified
  projected_at: 2026-07-06
---

# Michigan v. DeFillippo

*443 U.S. 31 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Detroit ordinance made it a crime for a person to refuse to identify himself to police under certain circumstances. Officers found DeFillippo in an alley with a woman, and when he repeatedly refused to identify himself they arrested him under the ordinance; a search incident to that arrest turned up drugs. The identification ordinance was later held unconstitutionally vague.

## Issue
Whether evidence seized in a search incident to an arrest under a presumptively valid ordinance must be suppressed once the ordinance is later declared unconstitutional.

## Rule
No. "The subsequently determined invalidity of the Detroit ordinance on vagueness grounds does not undermine the validity of the arrest made for violation of that ordinance, and the evidence discovered in the search of respondent should not have been suppressed." — 443 U.S. at 40. ^pin-40

At the time of the arrest the officers had probable cause to believe DeFillippo was violating a presumptively valid ordinance; police are charged to enforce ordinances until they are judicially declared invalid.

## Application
When the officers arrested DeFillippo, the identification ordinance had not yet been declared unconstitutional, so his refusal to identify himself gave them probable cause to arrest under a presumptively valid law. The search that produced the drugs was incident to that lawful arrest, and the ordinance's later invalidation did not retroactively render the arrest or search unlawful; the evidence should not have been suppressed.

## Conclusion
Reversed; suppression of the evidence was unwarranted.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *DeFillippo* anticipates the good-faith line of [[United States v. Leon]] and the reliance-on-a-statute analysis of [[Illinois v. Krull]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *Michigan v. DeFillippo*, 443 U.S. 31 (1979) — https://www.courtlistener.com/opinion/110127/michigan-v-defillippo/ — pinpoint: 40.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7766ca2d05eb9770", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "443 U.S. 31 (1979)", "court": "U.S. Supreme Court", "neutral_cite": "1979 U.S. LEXIS 135", "official_citation_present": true, "parallel_cite": "99 S. Ct. 2627; 61 L. Ed. 2d 343", "title": "Michigan v. DeFillippo", "year": "1979"}}
{"assertion_id": "2f456d9b20448573", "dimension": "support", "kind": "home_role", "locator": {"home": "The Good-Faith Exception"}, "payload": {"home": "The Good-Faith Exception", "role": "Key — Progeny / Refinement", "title": "Michigan v. DeFillippo"}}
{"assertion_id": "bd888edd85f09432", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An arrest based on a presumptively valid ordinance later declared unconstitutional was valid (supported by probable cause at the time),…", "title": "Michigan v. DeFillippo"}}
{"assertion_id": "04137c7d9294cd87", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Michigan v. DeFillippo"}}
{"assertion_id": "df49459243479fa9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1979-06-25", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Michigan v. DeFillippo", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Michigan v. DeFillippo", "varies_by_point": "false"}}
```

### lake record — Michigan v. DeFillippo

```json
{
  "schema_version": "s2.v1",
  "record_id": "Michigan v. DeFillippo",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Michigan v. DeFillippo",
    "case_name_short": "DeFillippo",
    "case_name_full": "MICHIGAN v. DeFILLIPPO",
    "input_case_name": "Michigan v. DeFillippo",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-06-25",
    "year": 1979,
    "docket": null,
    "cluster_id": 110127,
    "lead_opinion_id": 110127,
    "sibling_ids": [
      110127,
      9427654,
      9427655,
      9427656
    ],
    "absolute_url": "/opinion/110127/michigan-v-defillippo/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "443 U.S. 31",
      "volume": "443",
      "reporter": "U.S.",
      "page": "31",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 2627",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2627",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 343",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "343",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 135",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "135",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "443 U.S. 31",
        "volume": "443",
        "reporter": "U.S.",
        "page": "31",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 2627",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2627",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 343",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "343",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 135",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "135",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "443 U.S. 31",
    "official_selection": {
      "court_class": "scotus",
      "selected": "443 U.S. 31",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-40",
      "page": null,
      "quote": "--- # Michigan v. DeFillippo *443 U.S. 31 (1979)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Detroit ordinance made it a crime for a person to refuse to identify himself to police under certain circumstances. Officers found DeFillippo in an alley with a woman, and when he repeatedly refused to identify himself they arrested him under the ordinance; a search incident to that arrest turned up drugs. The identification ordinance was later held unconstitutionally vague. ## Issue Whether evidence seized in a search incident to an arrest under a presumptively valid ordinance must be suppressed once the ordinance is later declared unconstitutional. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-06-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Michigan v. DeFillippo",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Mickel",
          "cluster_id": 10680424,
          "cite": [
            "321 Ga. 751"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pat Reed, Commissioner of the WV DMV v. Joseph M. Winesburg",
          "cluster_id": 4597286,
          "cite": [
            "825 S.E.2d 85"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Marlow Humbert v. Mayor and City Council of Baltimore City",
          "cluster_id": 4416687,
          "cite": [
            "866 F.3d 546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lauren Graham v. C. Gagnon",
          "cluster_id": 4242146,
          "cite": [
            "831 F.3d 176",
            "2016 U.S. App. LEXIS 13672",
            "2016 WL 4011156"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Glenda Smith v. City of Wyoming",
          "cluster_id": 3194781,
          "cite": [
            "821 F.3d 697",
            "2016 FED App. 0094P",
            "2016 U.S. App. LEXIS 6833",
            "2016 WL 1533998"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Arredondo",
          "cluster_id": 6238731,
          "cite": [
            "199 Cal. Rptr. 3d 563",
            "245 Cal. App. 4th 186",
            "2016 Cal. App. LEXIS 153"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mocek v. City of Albuquerque",
          "cluster_id": 3164764,
          "cite": [
            "813 F.3d 912",
            "2015 U.S. App. LEXIS 22435",
            "2015 WL 9298662"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Cahaly v. Paul LaRosa, III",
          "cluster_id": 2823574,
          "cite": [
            "796 F.3d 399",
            "2015 WL 4646922"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kenneth Lee Douds v. State",
          "cluster_id": 2983813,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fadul",
          "cluster_id": 7306139,
          "cite": [
            "16 F. Supp. 3d 270",
            "2014 WL 1584044"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Hogan v. City of Corpus Christi, Texas",
          "cluster_id": 1033766,
          "cite": [
            "722 F.3d 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
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
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
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
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennhurst State School and Hospital v. Halderman",
          "cluster_id": 111094,
          "cite": [
            "79 L. Ed. 2d 67",
            "104 S. Ct. 900",
            "465 U.S. 89",
            "1984 U.S. LEXIS 4",
            "52 U.S.L.W. 4155"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kolender v. Lawson",
          "cluster_id": 110926,
          "cite": [
            "75 L. Ed. 2d 903",
            "103 S. Ct. 1855",
            "461 U.S. 352",
            "1983 U.S. LEXIS 159",
            "51 U.S.L.W. 4532"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
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
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kim D. Lee v. Luis Ferraro",
          "cluster_id": 75789,
          "cite": [
            "284 F.3d 1188",
            "2002 U.S. App. LEXIS 3438",
            "2002 WL 340670"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Krull",
          "cluster_id": 111835,
          "cite": [
            "94 L. Ed. 2d 364",
            "107 S. Ct. 1160",
            "480 U.S. 340",
            "1987 U.S. LEXIS 1061",
            "55 U.S.L.W. 4291"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
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
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Howard",
          "cluster_id": 5684310,
          "cite": [
            "50 N.Y.2d 583",
            "408 N.E.2d 908",
            "430 N.Y.S.2d 578",
            "1980 N.Y. LEXIS 2454"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heien v. North Carolina",
          "cluster_id": 2760668,
          "cite": [
            "190 L. Ed. 2d 475",
            "135 S. Ct. 530",
            "2014 U.S. LEXIS 8306",
            "83 U.S.L.W. 4021",
            "25 Fla. L. Weekly Fed. S 20"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cindy Abbott v. Sangamon County",
          "cluster_id": 816250,
          "cite": [
            "705 F.3d 706",
            "2013 WL 322920",
            "2013 U.S. App. LEXIS 1963"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katherine Gardenhire and Walter Gardenhire v. Donald Schubert, in His Individual and Official Capacity as Chief of Police",
          "cluster_id": 767858,
          "cite": [
            "205 F.3d 303",
            "2000 U.S. App. LEXIS 3126",
            "2000 WL 232311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wheeler v. Lawson",
          "cluster_id": 1427057,
          "cite": [
            "539 F.3d 629",
            "2008 U.S. App. LEXIS 17792",
            "2008 WL 3866950"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Club Retro, L.L.C. v. Hilton",
          "cluster_id": 1459439,
          "cite": [
            "568 F.3d 181",
            "2009 U.S. App. LEXIS 9864",
            "2006 WL 6245546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James N. Gramenos v. Jewel Companies, Inc.",
          "cluster_id": 474259,
          "cite": [
            "797 F.2d 432"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. White",
          "cluster_id": 1194272,
          "cite": [
            "640 P.2d 1061",
            "97 Wash. 2d 92",
            "1982 Wash. LEXIS 1262"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 1104481,
          "cite": [
            "461 So. 2d 686"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
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
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Huddleston",
          "cluster_id": 2435833,
          "cite": [
            "924 S.W.2d 666",
            "1996 Tenn. LEXIS 387",
            "1996 WL 328642"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicole Schneyder v. Gina Smith",
          "cluster_id": 222150,
          "cite": [
            "653 F.3d 313",
            "2011 U.S. App. LEXIS 15831",
            "2011 WL 3211504"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Peterson Novelties, Inc v. City of Berkley",
          "cluster_id": 2179551,
          "cite": [
            "672 N.W.2d 351",
            "259 Mich. App. 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gonzalez v. City of Elgin",
          "cluster_id": 1456587,
          "cite": [
            "578 F.3d 526",
            "2009 U.S. App. LEXIS 18724",
            "2009 WL 2525565"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark A. Criss v. The City of Kent Rick Haury, Officer, Kent City Police Department",
          "cluster_id": 518124,
          "cite": [
            "867 F.2d 259",
            "1988 U.S. App. LEXIS 17645",
            "1988 WL 146871"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gaetano Modica",
          "cluster_id": 396890,
          "cite": [
            "663 F.2d 1173",
            "1981 U.S. App. LEXIS 16444"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110127 OR 9427654 OR 9427655 OR 9427656) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjU5ODg0ODAwMDAwJnM9MTg3NDkzJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110127+OR+9427654+OR+9427655+OR+9427656%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110127 OR 9427654 OR 9427655 OR 9427656)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMTImcz02ODI3NTImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110127+OR+9427654+OR+9427655+OR+9427656%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110127 OR 9427654 OR 9427655 OR 9427656)",
        "reviewed": 35,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 35,
        "triage_read": 1,
        "triage_snippet_classified": 34
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110127 OR 9427654 OR 9427655 OR 9427656)",
    "indexed_citing_opinions": 840,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110127,
        "count": 747,
        "count_source": "search"
      },
      {
        "opinion_id": 9427654,
        "count": 102,
        "count_source": "search"
      },
      {
        "opinion_id": 9427655,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427656,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1695,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/michigan-v-defillippo.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3MzA1NzUmcz05NDg4OTE4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110127+OR+9427654+OR+9427655+OR+9427656%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110127,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107607,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 108348,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 108894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 297732,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 332469,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 1284752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
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
    "date_created": "2026-07-05T13:21:37Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:21:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:21:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:24:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:21:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Michigan v. DeFillippo

```
<div>
<center><b><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">443 U.S. 31</a></span> (1979)</b></center>
<center><h1>MICHIGAN<br>
v.<br>
DEFILLIPPO.</h1></center>
<center>No. 77-1680.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 21, 1979.</center>
<center>Decided June 25, 1979.</center>
CERTIORARI TO THE COURT OF APPEALS OF MICHIGAN.
<p><span class="star-pagination">*32</span> <i>Timothy A. Baughman</i> argued the cause for petitioner. with him on the briefs was <i>William L. Cahalan.</i></p>
<p><i>James C. Howarth,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./439/976/">439 U. S. 976</a></span>, argued the cause and filed a brief for respondent.<sup>[*]</sup></p>
<p><span class="star-pagination">*33</span> MR. CHIEF JUSTICE BURGER delivered the opinion of the Court.</p>
<p>The question presented by this case is whether an arrest made in good-faith reliance on an ordinance, which at the time had not been declared unconstitutional, is valid regardless of a subsequent judicial determination of its unconstitutionality.</p>
<p></p>
<h2>I</h2>
<p>At approximately 10 p. m. on September 14, 1976, Detroit police officers on duty in a patrol car received a radio call to investigate two persons reportedly appearing to be intoxicated in an alley. When they arrived at the alley, they found respondent and a young woman. The woman was in the process of lowering her slacks. One of the officers asked what they were doing, and the woman replied that she was about to relieve herself. The officer then asked respondent for identification; respondent asserted that he was Sergeant Mash, of the Detroit Police Department; he also purported to give his badge number, but the officer was unable to hear it. When respondent again was asked for identification, he changed his answer and said either that he worked for or that he knew Sergeant Mash. Respondent did not appear to be intoxicated.</p>
<p>Section 39-1-52.3 of the Code of the City of Detroit provides that a police officer may stop and question an individual if he has reasonable cause to believe that the individual's behavior warrants further investigation for criminal activity. In 1976 the Detroit Common Council amended § 39-1-52.3 to provide that it should be unlawful for any person stopped pursuant thereto to refuse to identify himself and produce evidence of his identity.<sup>[1]</sup></p>
<p><span class="star-pagination">*34</span> When he failed to identify himself, respondent was taken into custody for violation of § 39-1-52.3;<sup>[2]</sup> he was searched by one of the officers who found a package of marihuana in one of respondent's shirt pockets, and a tinfoil packet secreted inside a cigarette package in the other. The tinfoil packet subsequently was opened at the station; an analysis established that it contained phencyclidine, another controlled substance.</p>
<p>Respondent was charged with possession of the controlled substance phencyclidine. At the preliminary examination, he moved to suppress the evidence obtained in the search following the arrest; the trial court denied the motion. The Michigan Court of Appeals allowed an interlocutory appeal and reversed. It held that the Detroit ordinance, § 39-1-52.3, was unconstitutionally vague and concluded that since respondent had been arrested pursuant to that ordinance, both the arrest and the search were invalid.</p>
<p>The court expressly rejected the contention that an arrest made in good-faith reliance on a presumptively valid ordinance is valid regardless of whether the ordinance subsequently is declared unconstitutional. Accordingly, the Michigan Court of Appeals remanded with instructions to suppress the evidence <span class="star-pagination">*35</span> and quash the information. <span class="citation" data-id="1284752"><a href="/opinion/1284752/people-v-defillippo/" aria-description="Citation for case: People v. DeFillippo">80 Mich. App. 197</a></span>, <span class="citation" data-id="1284752"><a href="/opinion/1284752/people-v-defillippo/" aria-description="Citation for case: People v. DeFillippo">262 N. W. 2d 921</a></span> (1977).</p>
<p>The Michigan Supreme Court denied leave to appeal. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./439/816/">439 U. S. 816</a></span> (1978), to review the Michigan court's holding that evidence should be suppressed on federal constitutional grounds, although it was obtained as a result of an arrest pursuant to a presumptively valid ordinance. That holding was contrary to the holdings of the United States Court of Appeals for the Fifth Circuit that such arrests are valid. See <i>United States</i> v. <i>Carden,</i> <span class="citation" data-id="332469"><a href="/opinion/332469/united-states-v-roy-eugene-carden-winfred-eugene-carden-and-robert-lee/" aria-description="Citation for case: United States v. Roy Eugene Carden, Winfred Eugene...">529 F. 2d 443</a></span> (1976); <i>United States</i> v. <i>Kilgen,</i> <span class="citation" data-id="297732"><a href="/opinion/297732/united-states-v-robert-h-kilgen-jr/" aria-description="Citation for case: United States v. Robert H. Kilgen, Jr.">445 F. 2d 287</a></span> (1971).</p>
<p></p>
<h2>II</h2>
<p>Respondent was not charged with or tried for violation of the Detroit ordinance. The State contends that because of the violation of the ordinance, <i>i. e.,</i> refusal to identify himself, which respondent committed in the presence of the officers, respondent was subject to a valid arrest. The search that followed being incidental to that arrest, the State argues that it was equally valid and the drugs found should not have been suppressed. Respondent contends that since the ordinance which he was arrested for violating has been found unconstitutionally vague on its face, the arrest and search were invalid as violative of his rights under the Fourth and Fourteenth Amendments. Accordingly, he contends the drugs found in the search were correctly suppressed.</p>
<p>Under the Fourth and Fourteenth Amendments, an arresting officer may, without a warrant, search a person validly arrested. <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973); <i>Gustafson</i> v. <i>Florida,</i> <span class="citation" data-id="9425477"><a href="/opinion/108894/gustafson-v-florida/" aria-description="Citation for case: Gustafson v. Florida">414 U. S. 260</a></span> (1973). The constitutionality of a search incident to an arrest does not depend on whether there is any indication that the person arrested possesses weapons or evidence. The fact of a lawful arrest, standing alone, authorizes a search. <i>United States</i> v. <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson"><i>Robinson, supra,</i> at 235</a></span>. Here the officer effected the arrest of respondent <span class="star-pagination">*36</span> for his refusal to identify himself; contraband drugs were found as a result of the search of respondent's person incidental to that arrest. If the arrest was valid when made, the search was valid and the illegal drugs are admissible in evidence.</p>
<p>Whether an officer is authorized to make an arrest ordinarily depends, in the first instance, on state law. <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#37" aria-description="Citation for case: Ker v. California">374 U. S. 23, 37</a></span> (1963); <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#15" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 15</a></span>, and n. 5 (1948). Respondent does not contend, however, that the arrest was not authorized by Michigan law. See <span class="citation no-link">Mich. Comp. Laws § 764.15</span> (1970). His sole contention is that since the arrest was for allegedly violating a Detroit ordinance later held unconstitutional, the search was likewise invalid.</p>
<p></p>
<h2>III</h2>
<p>It is not disputed that the Constitution permits an officer to arrest a suspect without a warrant if there is probable cause to believe that the suspect has committed or is committing an offense. <i>Adams</i> v. <i>Williams,</i> <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#148" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 148-149</a></span> (1972); <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#91" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 91</a></span> (1964). The validity of the arrest does not depend on whether the suspect actually committed a crime; the mere fact that the suspect is later acquitted of the offense for which he is arrested is irrelevant to the validity of the arrest. We have made clear that the kinds and degree of proof and the procedural requirements necessary for a conviction are not prerequisites to a valid arrest. See <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#119" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 119-123</a></span> (1975); <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 174-176</a></span> (1949).</p>
<p>When the officer arrested respondent, he had abundant probable cause to believe that respondent's conduct violated the terms of the ordinance. The ordinance provides that a person commits an offense if (a) an officer has reasonable cause to believe that given behavior warrants further investigation, (b) the officer stops him, and (c) the suspect refuses to identify himself. The offense is then complete.</p>
<p><span class="star-pagination">*37</span> Respondent's presence with a woman, in the circumstances described, in an alley at 10 p. m. was clearly, in the words of the ordinance, "behavior. . . warrant[ing] further investigation." Respondent's inconsistent and evasive responses to the officer's request that he identify himself, stating first that he was Sergeant Mash of the Detroit Police Department and then that he worked for or knew Sergeant Mash, constituted a refusal by respondent to identify himself as the ordinance required. Assuming, <i>arguendo,</i> that a person may not constitutionally be required to answer questions put by an officer in some circumstances, the false identification violated the plain language of the Detroit ordinance.</p>
<p>The remaining question, then, is whether, in these circumstances, it can be said that the officer lacked probable cause to believe that the conduct he observed and the words spoken constituted a violation of law simply because he should have known the ordinance was invalid and would be judicially declared unconstitutional. The answer is clearly negative.</p>
<p>This Court repeatedly has explained that "probable cause" to justify an arrest means facts and circumstances within the officer's knowledge that are sufficient to warrant a prudent person, or one of reasonable caution, in believing, in the circumstances shown, that the suspect has committed, is committing, or is about to commit an offense. See <i>Gerstein</i> v. <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#111" aria-description="Citation for case: Gerstein v. Pugh"><i>Pugh, supra,</i> at 111</a></span>; <i>Adams</i> v. <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#148" aria-description="Citation for case: Adams v. Williams"><i>Williams, supra,</i> at 148</a></span>; <i>Beck</i> v. <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#91" aria-description="Citation for case: Beck v. Ohio"><i>Ohio, supra,</i> at 91</a></span>; <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#313" aria-description="Citation for case: Draper v. United States">358 U. S. 307, 313</a></span> (1959); <i>Brinegar</i> v. <i>United States, supra,</i> at 175-176; <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#162" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 162</a></span> (1925).</p>
<p>On this record there was abundant probable cause to satisfy the constitutional prerequisite for an arrest. At that time, of course, there was no controlling precedent that this ordinance was or was not constitutional, and hence the conduct observed violated a presumptively valid ordinance. A prudent officer, in the course of determining whether respondent had committed an offense under all the circumstances shown <span class="star-pagination">*38</span> by this record, should not have been required to anticipate that a court would later hold the ordinance unconstitutional.</p>
<p>Police are charged to enforce laws until and unless they are declared unconstitutional. The enactment of a law forecloses speculation by enforcement officers concerning its constitutionality with the possible exception of a law so grossly and flagrantly unconstitutional that any person of reasonable prudence would be bound to see its flaws. Society would be ill-served if its police officers took it upon themselves to determine which laws are and which are not constitutionally entitled to enforcement.</p>
<p>In <i>Pierson</i> v. <i>Ray,</i> <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547</a></span> (1967), persons who had been arrested for violating a statute later declared unconstitutional by this Court sought damages for false arrest under state law and for violation of the Fourteenth Amendment under <span class="citation no-link">42 U. S. C. § 1983</span>. Mr. Chief Justice Warren speaking for the Court, in holding that police action based on a presumptively valid law was subject to a valid defense of good faith, observed: "A policeman's lot is not so unhappy that he must choose between being charged with dereliction of duty if he does not arrest when he has probable cause, and being mulcted in damages if he does." <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#555" aria-description="Citation for case: Pierson v. Ray">386 U. S., at 555</a></span>. The Court held that "the defense of good faith and probable cause, which the Court of Appeals found available to the officers in the common-law action for false arrest and imprisonment, is also available to them in the action under § 1983." <i>Id.,</i> at 557. Here, the police were not required to risk "being charged with dereliction of duty if [they did] not arrest when [they had] probable cause" on the basis of the conduct observed.<sup>[3]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*39</span> IV</h2>
<p>We have held that the exclusionary rule required suppression of evidence obtained in searches carried out pursuant to statutes, not previously declared unconstitutional, which purported to authorize the searches in question without probable cause and without a valid warrant. See, <i>e. g., </i><i>Torres</i> v. <i>Puerto Rico,</i> <span class="citation" data-id="9795098"><a href="/opinion/2620876/torres-v-puerto-rico/" aria-description="Citation for case: Torres v. Puerto Rico">442 U. S. 465</a></span> (1979); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973); <i>Sibron</i> v. <i>New York,</i> <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span> (1968); <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967). Our holding today is not inconsistent with these decisions; the statutes involved in those cases bore a different relationship to the challenged searches than did the Detroit ordinance to respondent's arrest and search.</p>
<p>Those decisions involved statutes which, by their own terms, authorized searches under circumstances which did not satisfy the traditional warrant and probable-cause requirements of the Fourth Amendment. For example, in <i>Almeida-Sanchez</i> v. <i>United States, supra</i><i>,</i> we held invalid a search pursuant to a federal statute which authorized the Border Patrol to search any vehicle within a "reasonable distance" of the border, without a warrant or probable cause. The Attorney General, by regulation, fixed 100 miles as a "reasonable distance" from the border. <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#268" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S., at 268</a></span>. We held a search so distant from the point of entry was unreasonable under the Constitution. In <i>Berger</i> v. <i>New York</i> we struck down a statute authorizing searches under warrants which did not "particularly describ[e] the place to be searched, and the persons or things to be seized," as required by the Fourth and Fourteenth Amendments. <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#55" aria-description="Citation for case: Berger v. New York">388 U. S., at 55-56</a></span>.</p>
<p>In contrast, the ordinance here declared it a misdemeanor for one stopped for "investigation" to "refuse to identify himself"; it did not directly authorize the arrest or search.<sup>[4]</sup> Once <span class="star-pagination">*40</span> respondent refused to identify himself as the presumptively valid ordinance required, the officer had probable cause to believe respondent was committing an offense in his presence, and Michigan's general arrest statute, <span class="citation no-link">Mich. Comp. Laws § 764.15</span> (1970), authorized the arrest of respondent, independent of the ordinance. The search which followed was valid because it was incidental to that arrest. The ordinance is relevant to the validity of the arrest and search only as it pertains to the "facts and circumstances" we hold constituted probable cause for arrest.</p>
<p>The subsequently determined invalidity of the Detroit ordinance on vagueness grounds does not undermine the validity of the arrest made for violation of that ordinance, and the evidence discovered in the search of respondent should not have been suppressed. Accordingly, the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>Reversed and remanded.</i></p>
<p>MR. JUSTICE BLACKMUN, concurring.</p>
<p>I join the Court's opinion, but add a few words about the concern so evident in MR. JUSTICE BRENNAN'S dissenting opinion that today's decision will allow States and municipalities to circumvent the probable-cause requirement of the Fourth Amendment. There is some danger, I acknowledge, that the police will use a stop-and-identify ordinance to arrest persons for improper identification; that they will then conduct a search pursuant to the arrest; that if they discover contraband or other evidence of crime, the arrestee will be charged with some other offense; and that if they do not discover contraband or other evidence of crime, the arrestee will be released. In this manner, if the arrest for violation of the stop-and-identify <span class="star-pagination">*41</span> ordinance is not open to challenge, the ordinance itself could perpetually evade constitutional review.</p>
<p>There is no evidence in this case, however, that the Detroit ordinance is being used in such a pretextual manner. See Tr. of Oral Arg. 8. If a defendant in a proper case showed that the police habitually arrest, but do not prosecute, under a stop-and-identify ordinance, then I think this would suffice to rebut any claim that the police were acting in reasonable, good-faith reliance on the constitutionality of the ordinance. The arrestee could then challenge the validity of the ordinance, and, if the court concluded it was unconstitutional, could have the evidence obtained in the search incident to the arrest suppressed.</p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE MARSHALL and MR. JUSTICE STEVENS join, dissenting.</p>
<p>I disagree with the Court's conclusion that the Detroit police had constitutional authority to arrest and search respondent because respondent refused to identify himself in violation of the Detroit ordinance. In my view, the police conduct, whether or not authorized by state law, exceeded the bounds set by the Constitution and violated respondent's Fourth Amendment rights.</p>
<p>At the time of respondent's arrest, Detroit City Code § 39-1-52.3 (1976) read as follows:</p>
<blockquote>"When a police officer has reasonable cause to believe that the behavior of an individual warrants further investigation for criminal activity, the officer may stop and question such person. It shall be unlawful for any person stopped pursuant to this section to refuse to identify himself, and to produce verifiable documents or other evidence of such identification. In the event that such person is unable to provide reasonable evidence of his true identity, the police officer may transport him to the nearest precinct in order to ascertain his identity."</blockquote>
<p><span class="star-pagination">*42</span> Detroit police, acting purely on suspicion, stopped respondent Gary DeFillippo on the authority of this ordinance and demanded that he identify himself and furnish proof of his identity. When respondent rebuffed their inquiries the police arrested him for violation of the ordinance. Thereafter, police searched respondent and discovered drugs.</p>
<p>Respondent challenges the constitutionality of the ordinance and his arrest and search pursuant to it. The Court assumes the unconstitutionality of the ordinance but upholds respondent's arrest nonetheless. The Court reasons that the police had probable cause to believe that respondent's actions violated the ordinance, that the police could not have been expected to know that the ordinance was unconstitutional, and that the police actions were therefore reasonable.</p>
<p>The Court errs, in my view, in focusing on the good faith of the arresting officers and on whether they were entitled to rely upon the validity of the Detroit ordinance. For the dispute in this case is not between the arresting officers and respondent. Cf. <i>Pierson</i> v. <i>Ray,</i> <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547</a></span> (1967).<sup>[1]</sup> The dispute is between respondent and the State of Michigan. <span class="star-pagination">*43</span> The ultimate issue is whether the State gathered evidence against respondent through unconstitutional means. Since the State is responsible for the actions of its legislative bodies as well as for the actions of its police, the State can hardly defend against this charge of unconstitutional conduct by arguing that the constitutional defect was the product of legislative action and that the police were merely executing the laws in good faith. See <i>Torres</i> v. <i>Puerto Rico,</i> <span class="citation" data-id="9795098"><a href="/opinion/2620876/torres-v-puerto-rico/" aria-description="Citation for case: Torres v. Puerto Rico">442 U. S. 465</a></span> (1979); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973); <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967). States "may not . . . authorize police conduct which trenches upon Fourth Amendment rights, regardless of the labels which it attaches to such conduct. The question in this Court upon review of a state-approved search or seizure `is not whether the search [or seizure] was authorized by state law. The question is rather whether the search [or seizure] was reasonable under the Fourth Amendment.'" <i>Sibron</i> v. <i>New York,</i> <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#61" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 61</a></span> (1968), quoting in part from <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 61</a></span> (1967).</p>
<p>If the Court's inquiry were so directed and had not asked whether the arresting officers faithfully applied state law, invalidation of respondent's arrest and search would have been inescapable. For the Court's assumption that the Detroit ordinance is unconstitutional is well founded; the ordinance is indeed unconstitutional and patently so. And if the reasons for that constitutional infirmity had only been explored, rather than simply assumed, it would have been obvious that the application of the ordinance to respondent by Detroit police in this case trenched upon respondent's Fourth Amendment rights and resulted in an unreasonable search and seizure.</p>
<p>The touchstone of the Fourth Amendment's protection of privacy interests and prohibition against unreasonable police searches and seizures is the requirement that such police intrusions be based upon probable cause"`the best compromise that has been found for accommodating [the] often <span class="star-pagination">*44</span> opposing interests' in `safeguard[ing] citizens from rash and unreasonable interferences with privacy' and in `seek[ing] to give fair leeway for enforcing the law in the community's protection.'" <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#208" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 208</a></span> (1979), quoting from <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949).</p>
<p>Because of this requirement and the constitutional policies underlying it, the authority of police to accost citizens on the basis of suspicion is "narrowly drawn," <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 27</a></span> (1968), and carefully circumscribed. See <i>Dunaway</i> v. <i>New York, supra</i><i>.</i> Police may not conduct searches when acting on less than probable cause. Even weapons frisks in these circumstances are permissible only if the police have reason to believe that they are dealing with an armed and dangerous individual. See <i>Terry</i> v. <i>Ohio, supra,</i> at 24. Furthermore, while a person may be briefly detained against his will on the basis of reasonable suspicion "while pertinent questions are directed to him . . . the person stopped is not obliged to answer, answers may not be compelled, and refusal to answer furnishes no basis for an arrest . . . ." <i>Terry</i> v. <i>Ohio, supra,</i> at 34 (WHITE, J., concurring). In the context of criminal investigation, the privacy interest in remaining silent simply cannot be overcome at the whim of any suspicious police officer.<sup>[2]</sup> "[W]hile the police have the right to request citizens to answer voluntarily questions concerning unsolved crimes they have no right to compel them to answer." <span class="star-pagination">*45</span> <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span>, 727 n. 6 (1969).</p>
<p>In sum then, individuals accosted by police on the basis merely of reasonable suspicion have a right not to be searched, a right to remain silent, and, as a corollary, a right not to be searched if they choose to remain silent.</p>
<p>It is plain that the Detroit ordinance and the police conduct that it purports to authorize abridge these rights and their concomitant limitations upon police authority. The ordinance authorizes police, acting on the basis of suspicion, to demand answers from suspects and authorizes arrest, search, and conviction for those who refuse to comply. The ordinance therefore commands that which the Constitution denies the State power to command and makes "a crime out of what under the Constitution cannot be a crime." <i>Coates</i> v. <i>Cincinnati,</i> <span class="citation" data-id="9424583"><a href="/opinion/108348/coates-v-city-of-cincinnati/#616" aria-description="Citation for case: Coates v. City of Cincinnati">402 U. S. 611, 616</a></span> (1971). Furthermore, the ordinance, by means of a transparent expedientmaking the constitutionally protected refusal to answer itself a substantive offensesanctions circumvention by the police of the Court's holding that refusal to answer police inquiries during a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop furnishes no basis for a full-scale search and seizure. Clearly, this is a sheer piece of legislative legerdemain not to be countenanced. See <i>Davis</i> v. <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#726" aria-description="Citation for case: Davis v. Mississippi"><i>Mississippi, supra,</i> at 726-727</a></span>; <i>Sibron</i> v. <i>New York, supra</i><i>.</i></p>
<p>The Court does not dispute this analysis. Rather, it assumes that respondent had a constitutional right to refuse to cooperate with the police inquiries, that the ordinance is unconstitutional, and that henceforward the ordinance shall be regarded as null and void. Yet, the Court holds that arrests and searches pursuant to the ordinance prior to its invalidation by the Michigan Court of Appeals are constitutionally valid. Given the Court's assumptions concerning the invalidity of the ordinance, its conclusion must rest on the tacit assumption that the defects requiring invalidation of the ordinance and of convictions entered pursuant to it do not also require the invalidation of arrests pursuant to the ordinance. But only a brief reflection upon the pervasiveness of the ordinance's <span class="star-pagination">*46</span> constitutional infirmities demonstrates the fallacy of that assumption.</p>
<p>A major constitutional defect of the ordinance is that it forces individuals accosted by police solely on the basis of suspicion to choose between forgoing their right to remain silent and forgoing their right not to be searched if they choose to remain silent. Clearly, a constitutional prohibition merely against prosecutions under the ordinance and not against arrests under the ordinance as well would not solve this dilemma. For the fact would remain that individuals who chose to remain silent would be forced to relinquish their right not to be searched (and indeed would risk conviction on the basis of any evidence seized from them), while those who chose not to be searched would be forced to forgo their constitutional right to remain silent. This Hobson's choice can be avoided only by invalidating such police intrusions whether or not authorized by ordinance and holding fast to the rule of <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> and its progeny: that police acting on less than probable cause may not search, compel answers, or search those who refuse to answer their questions.<sup>[3]</sup></p>
<p>The conduct of Detroit police in this case plainly violated Fourth Amendment limitations. The police commanded respondent to relinquish his constitutional right to remain silent and then arrested and searched him when he refused to do so. The Detroit ordinance does not validate that constitutionally impermissible conduct. Accordingly, I would affirm the judgment of the Michigan Court of Appeals invalidating respondent's arrest and suppressing its fruits.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> urging reversal were filed by <i>Frank Carrington, Wayne W. Schmidt, Glen R. Murphy, Thomas Hendrickson, James P. Costello,</i> and <i>Richard F. Mayer</i> for Americans for Effective Law Enforcement, Inc., et al.; and by <i>Evelle J. Younger,</i> Attorney General, <i>Jack R. Winkler,</i> Chief Assistant Attorney General, <i>Daniel J. Kremer,</i> Assistant Attorney General, and <i>Harley D. Mayfield</i> and <i>Karl Phaler,</i> Deputy Attorneys General, for the State of California.
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed by <i>Edward M. Wise</i> for the American Civil Liberties Union Fund of Michigan; and by <i>John J. Cleary</i> for California Attorneys for Criminal Justice et al.</p>
<p><i>Laurance S. Smith</i> filed a brief for the National Legal Aid and Defender Association as <i>amicus curiae.</i></p>
<p>[1]  As amended, Code of the City of Detroit § 39-1-52.3 provided:
</p>
<p>"When a police officer has reasonable cause to believe that the behavior of an individual warrants further investigation for criminal activity, the officer may stop and question such person. It shall be unlawful for any person stopped pursuant to this section to refuse to identify himself, and to produce verifiable documents or other evidence of such identification. In the event that such person is unable to provide reasonable evidence of his true identity, the police officer may transport him to the nearest precinct in order to ascertain his identity."</p>
<p>While holding the ordinance unconstitutional, the Michigan Court of Appeals construed the ordinance to make refusal to identify oneself a crime meriting arrest. <span class="citation" data-id="1284752"><a href="/opinion/1284752/people-v-defillippo/" aria-description="Citation for case: People v. DeFillippo">80 Mich. App. 197</a></span>, 201 n. 1, <span class="citation" data-id="1284752"><a href="/opinion/1284752/people-v-defillippo/" aria-description="Citation for case: People v. DeFillippo">262 N. W. 2d 921</a></span>, 923 n. 1 (1977).</p>
<p>The preamble to the amendment indicates that it was enacted in response to an emergency caused by a marked increase in crime, particularly street crime by gangs of juveniles.</p>
<p>[2]  The woman was arrested on a charge of disorderly conduct; she is not involved in this case.</p>
<p>[3]  The purpose of the exclusionary rule is to deter unlawful police action. No conceivable purpose of deterrence would be served by suppressing evidence which, at the time it was found on the person of the respondent, was the product of a lawful arrest and a lawful search. To deter police from enforcing a presumptively valid statute was never remotely in the contemplation of even the most zealous advocate of the exclusionary rule.</p>
<p>[4]  In terms of the ordinance, § 39-1-52.3 authorizes officers to detain an individual who is "unable to provide reasonable evidence of his true identity." However, the State disclaims reliance on this provision to authorize the arrest of a person who, like respondent, "refuse[s] to identify himself." Tr. of Oral Arg. 5.</p>
<p>[1]  The Court's reliance upon <i>Pierson</i> v. <i>Ray,</i> <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#555" aria-description="Citation for case: Pierson v. Ray">386 U. S., at 555</a></span>, exposes the fallacy of its constitutional analysis. The Court assumes that respondent had a constitutional right to refuse to answer the questions put to him by the police, see <i>ante,</i> at 37, but nonetheless, relying upon <i>Pierson</i> v. <i><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Ray</a></span></i><i>,</i> upholds respondent's arrest and search for exercising this constitutional right. But <i><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Pierson</a></span></i> involved an action for damages against individual police officers and held only that it would be unfair to penalize those officers for actions undertaken in a good-faith, though mistaken, interpretation of the Constitution. Since the officer who arrested respondent in this case is not being mulcted for damages or penalized in any way for his actions, <i><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Pierson</a></span></i> does not support the Court's position. Rather, since respondent is the one who is being penalized for the exercise of what he reasonably believed to be his constitutional rights, <i><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Pierson</a></span></i> counsels for invalidation of respondent's arrest and not for its validation. For if it is unfair to penalize a police officer for actions undertaken pursuant to a good-faith, though mistaken, interpretation of the Constitution, then surely it is unfair to penalize respondent for actions undertaken pursuant to a good-faith and <i>correct</i> interpretation of the Constitution.</p>
<p>[2]  In addition to the Fourth Amendment, see <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), the right to remain silent when detained by police on the basis of suspicion may find its source in the Fifth Amendment's privilege against self-incrimination see <i>Haynes</i> v. <i>United States,</i> <span class="citation" data-id="9423609"><a href="/opinion/107608/haynes-v-united-states/" aria-description="Citation for case: Haynes v. United States">390 U. S. 85</a></span> (1968); <i>Grosso</i> v. <i>United States,</i> <span class="citation" data-id="9423605"><a href="/opinion/107607/grosso-v-united-states/" aria-description="Citation for case: Grosso v. United States">390 U. S. 62</a></span> (1968); <i>Albertson</i> v. <i>SACB,</i> <span class="citation" data-id="9423096"><a href="/opinion/107110/albertson-v-subversive-activities-control-board/" aria-description="Citation for case: Albertson v. Subversive Activities Control Board">382 U. S. 70</a></span> (1965), or, more generally, in "the right to be let alonethe most comprehensive of rights and the right most valued by civilized men." <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#478" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 478</a></span> (1928) (Brandeis, J., dissenting). See also <i>Griswold</i> v. <i>Connecticut,</i> <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/#494" aria-description="Citation for case: Griswold v. Connecticut">381 U. S. 479, 494</a></span> (1965) (Goldberg, J., concurring).</p>
<p>[3]  There is also the risk that if stop-and-identify ordinances cannot be challenged in collateral proceedings they may never be presented for judicial review. Jurisdictions so minded may avoid prosecuting under them and use them merely as investigative tools to gather evidence of other crimes through pretextual arrests and searches. The possibility of such evasion is yet another reason that demonstrates the constitutional error of the Court's approval of respondent's arrest.</p>

</div>
```

---

## GROUP: content/cases/Michigan v. Fisher.md  (`case`, 5 assertions)

### content_page

```
---
title: "Michigan v. Fisher"
type: case
citation: "558 U.S. 45 (2009)"
parallel_cite: "130 S. Ct. 546; 175 L. Ed. 2d 410"
neutral_cite: 2009 U.S. LEXIS 8773
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-12-07
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2009-12-07
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Michigan v. Fisher
  varies_by_point: false
  scope_note: "Per curiam; applies Brigham City v. Stuart."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/1755/michigan-v-fisher/"
  cluster_id: 1755
  opinion_id: 9413217
  identity_checked: true
homes:
  - page: "[[Emergency Aid]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brigham City v. Stuart]]", "[[Mincey v. Arizona]]", "[[Caniglia v. Strom]]"]
aliases: []
tags: ["case", "fourth-amendment", "emergency-aid", "warrantless-entry", "home", "per-curiam"]
holding: "Applies Brigham City: emergency-aid entry upheld where it was objectively reasonable to believe an occupant was injured or about to be;…"
lake:
  record_id: Michigan v. Fisher
  status: verified
  projected_at: 2026-07-06
---

# Michigan v. Fisher

*558 U.S. 45 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers responding to a disturbance found a household in chaos: a smashed pickup, broken windows, blood on the truck and a door, and Fisher inside screaming and throwing things, with a cut on his hand. He refused medical attention and told the officers to get a warrant. An officer pushed the door partway open, saw Fisher point a long gun, and withdrew. The state courts suppressed the resulting evidence, finding no emergency.

## Issue
Whether the emergency-aid exception justified the warrantless entry where officers had an objectively reasonable basis to believe a violent situation requiring aid was underway.

## Rule
Yes. Applying [[Brigham City v. Stuart]]: "Officers do not need ironclad proof of 'a likely serious, life-threatening' injury to invoke the emergency aid exception." — 558 U.S. at 48. ^pin-48

Law enforcement officers may enter a home without a warrant to render emergency assistance or to protect an occupant from imminent injury when they have an objectively reasonable basis for believing aid is needed, judged from the circumstances confronting them.

## Application
The officers confronted a residence in chaos — a wrecked truck, broken windows, fresh blood, and a man visibly injured, screaming, and hurling objects. Those circumstances gave an objectively reasonable basis to believe someone inside was injured or in danger. That the blood was only "mere drops," or that Fisher seemed able to tend to himself, did not negate that reasonable basis, so the warrantless entry was justified on these facts.

## Conclusion
Reversed; the warrantless entry was reasonable under the emergency-aid exception.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Fisher* (per curiam) **applies** [[Brigham City v. Stuart]], confirming that the emergency-aid inquiry is objective and does not require ironclad proof of injury. The home-entry caretaking limit of [[Caniglia v. Strom]] does not disturb it.

## Appears on
- [[Emergency Aid]] — *Key — Progeny / Refinement*

## Sources
- *Michigan v. Fisher*, 558 U.S. 45 (2009) — https://www.courtlistener.com/opinion/1755/michigan-v-fisher/ — pinpoint: 48. (CL carries the per curiam slip opinion; the "ironclad proof" passage is at 558 U.S. 48 / slip op. at 4.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "859514488a8114ae", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "558 U.S. 45 (2009)", "court": "U.S. Supreme Court", "neutral_cite": "2009 U.S. LEXIS 8773", "official_citation_present": true, "parallel_cite": "130 S. Ct. 546; 175 L. Ed. 2d 410", "title": "Michigan v. Fisher", "year": "2009"}}
{"assertion_id": "7d62d06ae067d442", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Applies Brigham City: emergency-aid entry upheld where it was objectively reasonable to believe an occupant was injured or about to be;…", "title": "Michigan v. Fisher"}}
{"assertion_id": "f4d0c60ab9e9a43e", "dimension": "support", "kind": "home_role", "locator": {"home": "Emergency Aid"}, "payload": {"home": "Emergency Aid", "role": "Key — Progeny / Refinement", "title": "Michigan v. Fisher"}}
{"assertion_id": "321d642a473b0904", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Michigan v. Fisher"}}
{"assertion_id": "d0a7831851f5ff23", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2009-12-07", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Michigan v. Fisher", "field_i_validity": "good_law", "scope_note": "Per curiam; applies Brigham City v. Stuart.", "title": "Michigan v. Fisher", "varies_by_point": "false"}}
```

### lake record — Michigan v. Fisher

```json
{
  "schema_version": "s2.v1",
  "record_id": "Michigan v. Fisher",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Michigan v. Fisher",
    "case_name_short": "Fisher",
    "case_name_full": "Michigan v. Fisher",
    "input_case_name": "Michigan v. Fisher",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-12-07",
    "year": 2009,
    "docket": null,
    "cluster_id": 1755,
    "lead_opinion_id": 9413217,
    "sibling_ids": [
      1755,
      9413217,
      9413218
    ],
    "absolute_url": "/opinion/1755/michigan-v-fisher/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "558 U.S. 45",
      "volume": "558",
      "reporter": "U.S.",
      "page": "45",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "130 S. Ct. 546",
        "volume": "130",
        "reporter": "S. Ct.",
        "page": "546",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "175 L. Ed. 2d 410",
        "volume": "175",
        "reporter": "L. Ed. 2d",
        "page": "410",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 8773",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "8773",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "558 U.S. 45",
        "volume": "558",
        "reporter": "U.S.",
        "page": "45",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "130 S. Ct. 546",
        "volume": "130",
        "reporter": "S. Ct.",
        "page": "546",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "175 L. Ed. 2d 410",
        "volume": "175",
        "reporter": "L. Ed. 2d",
        "page": "410",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 8773",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "8773",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "558 U.S. 45",
    "official_selection": {
      "court_class": "scotus",
      "selected": "558 U.S. 45",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-48",
      "page": null,
      "quote": "--- # Michigan v. Fisher *558 U.S. 45 (2009)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers responding to a disturbance found a household in chaos: a smashed pickup, broken windows, blood on the truck and a door, and Fisher inside screaming and throwing things, with a cut on his hand. He refused medical attention and told the officers to get a warrant. An officer pushed the door partway open, saw Fisher point a long gun, and withdrew. The state courts suppressed the resulting evidence, finding no emergency. ## Issue Whether the emergency-aid exception justified the warrantless entry where officers had an objectively reasonable basis to believe a violent situation requiring aid was underway. ## Rule Yes. Applying [[Brigham City v. Stuart]]:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2009-12-07",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Michigan v. Fisher",
    "varies_by_point": false,
    "scope_note": "Per curiam; applies Brigham City v. Stuart.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 4600764,
          "cite": [
            "119 N.E.3d 257",
            "481 Mass. 604"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gregory Mahrt v. Jeffrey Beard",
          "cluster_id": 4372117,
          "cite": [
            "849 F.3d 1164",
            "2017 WL 782447",
            "2017 U.S. App. LEXIS 3696"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tosh Toussaint",
          "cluster_id": 4259133,
          "cite": [
            "838 F.3d 503",
            "2016 U.S. App. LEXIS 17357",
            "2016 WL 5314862"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Kaeppeler",
          "cluster_id": 3166351,
          "cite": [
            "473 Mass. 396",
            "42 N.E.3d 1090"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane1_negative"
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
        "journal_ref": "Michigan v. Fisher:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Caple",
          "cluster_id": 2820305,
          "cite": [
            "121 A.3d 511",
            "2015 WL 4497915"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane1_negative"
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
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kiobel v. Royal Dutch Petroleum Co.",
          "cluster_id": 175476,
          "cite": [
            "621 F.3d 111",
            "2010 U.S. App. LEXIS 19382"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Goodwin Ex Rel. Nall v. City of Painesville",
          "cluster_id": 2787500,
          "cite": [
            "781 F.3d 314",
            "2015 FED App. 0048P",
            "2015 U.S. App. LEXIS 4417",
            "2015 WL 1245400"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fernandez v. California",
          "cluster_id": 2654534,
          "cite": [
            "188 L. Ed. 2d 25",
            "134 S. Ct. 1126",
            "2014 U.S. LEXIS 1636",
            "82 U.S.L.W. 4102",
            "571 U.S. 292",
            "24 Fla. L. Weekly Fed. S 553",
            "2014 WL 700100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Chavez",
          "cluster_id": 2380403,
          "cite": [
            "240 P.3d 448",
            "2010 Colo. App. LEXIS 213",
            "2010 WL 547625"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Teresa Sheehan v. City and County of San Francis",
          "cluster_id": 3066152,
          "cite": [
            "743 F.3d 1211",
            "2014 WL 667082",
            "2014 U.S. App. LEXIS 3321"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schreiber v. Moe",
          "cluster_id": 1304750,
          "cite": [
            "596 F.3d 323",
            "2010 U.S. App. LEXIS 4537",
            "2010 WL 724021"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
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
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Caniglia v. Strom",
          "cluster_id": 4883694,
          "cite": [
            "593 U.S. 194",
            "209 L. Ed. 2d 604",
            "141 S. Ct. 1596"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Krysta Sutterfield v. City of Milwaukee",
          "cluster_id": 2708650,
          "cite": [
            "751 F.3d 542",
            "2014 WL 1853080",
            "2014 U.S. App. LEXIS 8774"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Williams v. Brian Maurer",
          "cluster_id": 4958226,
          "cite": [
            "9 F.4th 416"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. City of Memphis",
          "cluster_id": 173982,
          "cite": [
            "617 F.3d 864",
            "2010 U.S. App. LEXIS 17658",
            "2010 WL 3305264"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Slaughter",
          "cluster_id": 827985,
          "cite": [
            "489 Mich. 302",
            "803 N.W.2d 171",
            "2011 Mich. LEXIS 1175"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Everett",
          "cluster_id": 1292,
          "cite": [
            "601 F.3d 484",
            "2010 U.S. App. LEXIS 7107",
            "2010 WL 1286770"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Dunn",
          "cluster_id": 2690881,
          "cite": [
            "2012 Ohio 1008",
            "131 Ohio St. 3d 325"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. McHugh",
          "cluster_id": 213881,
          "cite": [
            "639 F.3d 1250",
            "2011 U.S. App. LEXIS 6791",
            "2011 WL 1226486"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sandoval v. Las Vegas Metropolitan Police Department",
          "cluster_id": 2681571,
          "cite": [
            "756 F.3d 1154",
            "2014 WL 2936254",
            "2014 U.S. App. LEXIS 12395"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Troyer",
          "cluster_id": 5608112,
          "cite": [
            "51 Cal. 4th 599",
            "246 P.3d 901",
            "120 Cal. Rptr. 3d 770",
            "2011 Cal. LEXIS 1827"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heather Baker v. City of Trenton",
          "cluster_id": 4657308,
          "cite": [
            "936 F.3d 523"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Susan Stricker v. Twp. Of Cambridge",
          "cluster_id": 815266,
          "cite": [
            "710 F.3d 350",
            "2013 WL 141695"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Pirouz Sedaghaty",
          "cluster_id": 1038319,
          "cite": [
            "728 F.3d 885",
            "112 A.F.T.R.2d (RIA) 5864",
            "2013 U.S. App. LEXIS 22234",
            "2013 WL 4490922"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lange v. California",
          "cluster_id": 4894054,
          "cite": [
            "594 U.S. 295"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Thomas Lee Hutchison",
          "cluster_id": 3169888,
          "cite": [
            "482 S.W.3d 893"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Fisher:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(1755 OR 9413217 OR 9413218) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 155,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 155,
        "triage_read": 6,
        "triage_snippet_classified": 149
      },
      "lane2_top_cited": {
        "query": "cites:(1755 OR 9413217 OR 9413218)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MSZzPTY1ODA1MTQmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%281755+OR+9413217+OR+9413218%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(1755 OR 9413217 OR 9413218)",
        "reviewed": 24,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 24,
        "triage_read": 0,
        "triage_snippet_classified": 24
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(1755 OR 9413217 OR 9413218)",
    "indexed_citing_opinions": 190,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 1755,
        "count": 132,
        "count_source": "search"
      },
      {
        "opinion_id": 9413217,
        "count": 65,
        "count_source": "search"
      },
      {
        "opinion_id": 9413218,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 389,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/michigan-v-fisher.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc5MzE0MjEmcz05MzUzMTE4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%281755+OR+9413217+OR+9413218%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 1755,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1755,
        "cited_id": 131161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1755,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1755,
        "cited_id": 837001,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1755,
        "cited_id": 1914600,
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
    "date_created": "2026-07-05T13:24:37Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:25:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:25:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:27:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:25:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Michigan v. Fisher

```
<opinion type="majority">
<author id="b207-9">Per Curiam.</author>
<p id="b207-10">Police officers responded to a complaint of a disturbance near Allen Road in Brownstown, Michigan.<footnotemark>*</footnotemark> Officer Christopher Goolsby later testified that, as he and his partner approached the area, a couple directed them to a residence where a man was “going crazy.” Docket No. 276439, <span class="citation no-link">2008 WL 786515</span>, *1 (Mich. App., Mar. 25, 2008) <em>(per curiam) </em>(alteration and internal quotation marks omitted). Upon their arrival, the officers found a household in considerable chaos: a pickup truck in the driveway with its front smashed, damaged fenceposts along the side of the property, and three <page-number citation-index="1" label="46">*46</page-number>broken house windows, the glass still on the ground outside. The officers also noticed blood on the hood of the pickup and on clothes inside of it, as well as on one of the doors to the house. (It is disputed whether they noticed this immediately upon reaching the house, but undisputed that they noticed it before the allegedly unconstitutional entry.) Through a window, the officers could see respondent, Jeremy Fisher, inside the house, screaming and throwing things. The back door was locked, and a couch had been placed to block the front door.</p>
<p id="b208-5">The officers knocked, but Fisher refused to answer. They saw that Fisher had a cut on his hand, and they asked him whether he needed medical attention. Fisher ignored these questions and demanded, with accompanying profanity, that the officers go to get a search warrant. Officer Goolsby then pushed the front door partway open and ventured into the house. Through the window of the open door he saw Fisher pointing a long gun at him. Officer Goolsby withdrew.</p>
<p id="b208-6">Fisher was charged under Michigan law with assault with a dangerous weapon and possession of a firearm during the commission of a felony. The trial court concluded that Officer Goolsby violated the Fourth Amendment when he entered Fisher’s house, and granted Fisher’s motion to suppress the evidence obtained as a result — that is, Officer Goolsby’s statement that Fisher pointed a rifle at him. The Michigan Court of Appeals initially remanded for an evidentiary hearing, see Docket No. 256027, <span class="citation no-link">2005 WL 3481454</span> (Dec. 20, 2005) <em>(per curiam), </em>after which the trial court reinstated its order. The Court of Appeals then affirmed over a dissent by Judge Talbot. See <span class="citation no-link">2008 WL 786515</span>, at <em>*2; <span class="citation no-link">id.,</span> </em>at *2-*5. The Michigan Supreme Court granted leave to appeal, but, after hearing oral argument, it vacated its prior order and denied leave instead; three justices, however, would have taken the case and reversed on the ground that the Court of Appeals misapplied the Fourth Amendment. <page-number citation-index="1" label="47">*47</page-number>See <span class="citation multiple-matches"><a href="/c/Mich./483/1007/">483 Mich. 1007</a></span>, <span class="citation" data-id="9503589"><a href="/opinion/837001/people-v-fisher/" aria-description="Citation for case: People v. Fisher">765 N. W. 2d 19</a></span> (2009). Because the decision of the Michigan Court of Appeals is indeed contrary to our Fourth Amendment ease law, particularly <em>Brigham City </em>v. <em>Stuart, </em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">547 U. S. 398</a></span> (2006), we grant the State’s petition for certiorari and reverse.</p>
<p id="b209-5">“[T]he ultimate touchstone of the Fourth Amendment,” we have often said, “is ‘reasonableness.’ ” <span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#403" aria-description="Citation for case: Brigham City v. Stuart"><em>Id., </em>at 403</a></span>. Therefore, although “searches and seizures inside a home without a warrant are presumptively unreasonable,” <em>Groh </em>v. <em>Ramirez, </em><span class="citation" data-id="9434540"><a href="/opinion/131161/groh-v-ramirez/#559" aria-description="Citation for case: Groh v. Ramirez">540 U. S. 551, 559</a></span> (2004) (internal quotation marks omitted), that presumption can be overcome. For example, “the exigencies of the situation [may] make the needs of law enforcement so compelling that the warrantless search is objectively reasonable.” <em>Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 393-394</a></span> (1978) (internal quotation marks omitted).</p>
<p id="b209-6"><em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">Brigham City</a></span> </em>identified one such exigency: “the need to assist persons who are seriously injured or threatened with such injury.” <span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#403" aria-description="Citation for case: Brigham City v. Stuart">547 U. S., at 403</a></span>. Thus, law enforcement officers “may enter a home without a warrant to render emergency assistance to an injured occupant or to protect an occupant from imminent injury.” <em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">Ibid.</a></span> </em>This “emergency aid exception” does not depend on the officers’ subjective intent or the seriousness of any crime they are investigating when the emergency arises. <span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#404" aria-description="Citation for case: Brigham City v. Stuart"><em>Id., </em>at 404-405</a></span>. It requires only “an objectively reasonable basis for believing,” <span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#406" aria-description="Citation for case: Brigham City v. Stuart"><em>id., </em>at 406</a></span>, that “a person within [the house] is in need of immediate aid,” <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#392" aria-description="Citation for case: Mincey v. Arizona"><em>Mincey, supra, </em>at 392</a></span>.</p>
<p id="b209-7"><em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">Brigham City</a></span> </em>illustrates the application of this standard. There, police officers responded to a noise complaint in the early hours of the morning. “As they approached the house, they could hear from within an altercation occurring, some kind of fight.” <span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#406" aria-description="Citation for case: Brigham City v. Stuart">547 U. S., at 406</a></span> (internal quotation marks omitted). Following the tumult to the back of the house whence it came, the officers saw juveniles drinking beer in the backyard and a fight unfolding in the kitchen. They <page-number citation-index="1" label="48">*48</page-number>watched through the window as a juvenile broke free from the adults restraining him and punched another adult in the face, who recoiled to the sink, spitting blood. <em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">Ibid.</a></span> </em>Under these circumstances, we found it “plainly reasonable” for the officers to enter the house and quell the violence, for they had “an objectively reasonable basis for believing both that the injured adult might need help and that the violence in the kitchen was just beginning.” <em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">Ibid.</a></span></em></p>
<p id="b210-5">A straightforward application of the emergency aid exception, as in <em>Brigham, City, </em>dictates that the officer’s entry was reasonable. Just as in <em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">Brigham City</a></span>, </em>the police officers here were responding to a report of a disturbance. Just as in <em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">Brigham City</a></span>, </em>when they arrived on the scene they encountered a tumultuous situation in the house — and here they also found signs of a recent injury, perhaps from a car accident, outside. And just as in <em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">Brigham City</a></span>, </em>the officers could see violent behavior inside. Although Officer Goolsby and his partner did not see punches thrown, as did the officers in <em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">Brigham City</a></span>, </em>they did see Fisher screaming and throwing things. It would be objectively reasonable to believe that Fisher’s projectiles might have a human target (perhaps a spouse or a child), or that Fisher would hurt himself in the course of his rage. In short, we find it as plain here as we did in <em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">Brigham City</a></span> </em>that the officer’s entry was reasonable under the Fourth Amendment.</p>
<p id="b210-6">The Michigan Court of Appeals, however, thought the situation “did not rise to a level of emergency justifying the warrantless intrusion into a residence.” <span class="citation no-link">2008 WL 786515</span>, at *2. Although the Court of Appeals conceded that “there was evidence an injured person was on the premises,” it found it significant that “the mere drops of blood did not signal a likely serious, life-threatening injury.” <em><span class="citation no-link">Ibid.</span> </em>The court added that the cut Officer Goolsby observed on Fisher’s hand “likely explained the trail of blood” and that Fisher “was very much on his feet and apparently able to see to his own needs.” <em><span class="citation no-link">Ibid.</span></em></p>
<p id="b211-4"><page-number citation-index="1" label="49">*49</page-number>Even a casual review of <em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">Brigham City</a></span> </em>reveals the flaw in this reasoning. Officers do not need ironclad proof of “a likely serious, life-threatening” injury to invoke the emergency aid exception. The only injury police could confirm in <em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">Brigham City</a></span> </em>was the bloody lip they saw the juvenile inflict upon the adult. Fisher argues that the officers here could not have been motivated by a perceived need to provide medical assistance, since they never summoned emergency medical personnel. This would have no bearing, of course, upon their need to ensure that Fisher was not endangering someone else in the house. Moreover, even if the failure to summon medical personnel conclusively established that Goolsby did not subjectively believe, when he entered the house, that Fisher or someone else was seriously injured (which is doubtful), the test, as we have said, is not what Goolsby believed, but whether there was “an objectively reasonable basis for believing” that medical assistance was needed, or persons were in danger, <span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#406" aria-description="Citation for case: Brigham City v. Stuart"><em>Brigham City, supra, </em>at 406</a></span>; <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#392" aria-description="Citation for case: Mincey v. Arizona"><em>Mincey, supra, </em>at 392</a></span>.</p>
<p id="b211-5">It was error for the Michigan Court of Appeals to replace that objective inquiry into appearances with its hindsight determination that there was in fact no emergency. It does not meet the needs of law enforcement or the demands of public safety to require officers to walk away from a situation like the one they encountered here. Only when an apparent threat has become an actual harm can officers rule out innocuous explanations for ominous circumstances. But “[t]he role of a peace officer includes preventing violence and restoring order, not simply rendering first aid to casualties.” <span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#406" aria-description="Citation for case: Brigham City v. Stuart"><em>Brigham City, supra, </em>at 406</a></span>. It sufficed to invoke the emergency aid exception that it was reasonable to believe that Fisher had hurt himself (albeit nonfatally) and needed treatment that in his rage he was unable to provide, or that Fisher was about to hurt, or had already hurt, someone else. The Michigan Court of Appeals required more than what the Fourth Amendment demands.</p>
<p id="A15"><page-number citation-index="1" label="50">*50</page-number>* * *</p>
<p id="b212-4">The petition for certiorari is granted. The judgment of the Michigan Court of Appeals is reversed, and the ease is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b212-5">
<em>It is so ordered.</em>
</p>
<footnote label="*">
<p id="b207-11">We have taken the facts from the opinion of the Michigan Court of Appeals. Except where indicated, the parties do not dispute the facts.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Michigan v. Long.md  (`case`, 5 assertions)

### content_page

```
---
title: "Michigan v. Long"
type: case
citation: "463 U.S. 1032 (1983)"
parallel_cite: "103 S. Ct. 3469; 77 L. Ed. 2d 1201; 51 U.S.L.W. 5231"
neutral_cite: 1983 U.S. LEXIS 7
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-07-06
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1983-07-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Michigan v. Long
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111020/michigan-v-long/"
  cluster_id: 111020
  opinion_id: 9842054
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Key — Progeny / Refinement"
related: ["[[Terry v. Ohio]]", "[[Pennsylvania v. Mimms]]", "[[Maryland v. Wilson]]"]
aliases: []
tags: ["case", "fourth-amendment", "terry", "protective-search", "vehicle", "weapons"]
holding: "Terry's protective-frisk rationale extends to vehicles: on specific and articulable facts giving the officer a reasonable belief the…"
lake:
  record_id: Michigan v. Long
  status: verified
  projected_at: 2026-07-06
---

# Michigan v. Long

*463 U.S. 1032 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Late at night in a rural area, officers saw Long's car swerve into a ditch. Long, who appeared intoxicated, met them at the rear of the car and was unresponsive to questions. The officers saw a hunting knife on the floorboard, and when Long began moving toward the car's interior they conducted a protective search of the passenger compartment, finding marijuana.

## Issue
Whether *[[Terry v. Ohio|Terry]]*'s protective-search rationale permits an officer to search the passenger compartment of a vehicle for weapons during an investigative stop.

## Rule
Yes. "the search of the passenger compartment of an automobile, limited to those areas in which a weapon may be placed or hidden, is permissible if the police officer possesses a reasonable belief based on 'specific and articulable facts which, taken together with the rational inferences from those facts, reasonably warrant' the officer in believing that the suspect is dangerous and the suspect may gain immediate control of weapons." — 463 U.S. at 1049. ^pin-1049

Contraband discovered in the course of such a lawful protective search need not be suppressed.

## Application
The late hour, the rural setting, Long's erratic driving and apparent intoxication, his unresponsiveness, and the hunting knife in plain view gave the officers a reasonable belief that he was dangerous and could gain immediate control of a weapon if allowed back into the car. The protective search of the passenger compartment was therefore permissible, and the marijuana found in the process was lawfully seized.

## Conclusion
The protective vehicle search was valid; reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Long* extends the *[[Terry v. Ohio|Terry]]* protective-frisk rationale ([[Terry v. Ohio]]) from the person to the passenger compartment of a vehicle.

## Appears on
- [[Traffic Stops]] — *Key — Progeny / Refinement*

## Sources
- *Michigan v. Long*, 463 U.S. 1032 (1983) — https://www.courtlistener.com/opinion/111020/michigan-v-long/ — pinpoint: 1049.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e70a84295c4f3af3", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "463 U.S. 1032 (1983)", "court": "U.S. Supreme Court", "neutral_cite": "1983 U.S. LEXIS 7", "official_citation_present": true, "parallel_cite": "103 S. Ct. 3469; 77 L. Ed. 2d 1201; 51 U.S.L.W. 5231", "title": "Michigan v. Long", "year": "1983"}}
{"assertion_id": "043fcf7376a024ec", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Key — Progeny / Refinement", "title": "Michigan v. Long"}}
{"assertion_id": "acecd8252e84b18e", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Terry's protective-frisk rationale extends to vehicles: on specific and articulable facts giving the officer a reasonable belief the…", "title": "Michigan v. Long"}}
{"assertion_id": "2448dfe2548391fa", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1983-07-06", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Michigan v. Long", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Michigan v. Long", "varies_by_point": "false"}}
{"assertion_id": "420c2f432c5c2bc2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Michigan v. Long"}}
```

### lake record — Michigan v. Long

```json
{
  "schema_version": "s2.v1",
  "record_id": "Michigan v. Long",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Michigan v. Long",
    "case_name_short": "Long",
    "case_name_full": "Michigan v. Long",
    "input_case_name": "Michigan v. Long",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-07-06",
    "year": 1983,
    "docket": null,
    "cluster_id": 111020,
    "lead_opinion_id": 9842054,
    "sibling_ids": [
      111020,
      9842054,
      9842055
    ],
    "absolute_url": "/opinion/111020/michigan-v-long/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9042910,
        "score": 20,
        "case_name": "Michigan v. Long"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "463 U.S. 1032",
      "volume": "463",
      "reporter": "U.S.",
      "page": "1032",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 3469",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "3469",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 2d 1201",
        "volume": "77",
        "reporter": "L. Ed. 2d",
        "page": "1201",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 5231",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "5231",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 7",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "7",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "463 U.S. 1032",
        "volume": "463",
        "reporter": "U.S.",
        "page": "1032",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 3469",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "3469",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 2d 1201",
        "volume": "77",
        "reporter": "L. Ed. 2d",
        "page": "1201",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 7",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "7",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 5231",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "5231",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "463 U.S. 1032",
    "official_selection": {
      "court_class": "scotus",
      "selected": "463 U.S. 1032",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1049",
      "page": null,
      "quote": "--- # Michigan v. Long *463 U.S. 1032 (1983)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Late at night in a rural area, officers saw Long's car swerve into a ditch. Long, who appeared intoxicated, met them at the rear of the car and was unresponsive to questions. The officers saw a hunting knife on the floorboard, and when Long began moving toward the car's interior they conducted a protective search of the passenger compartment, finding marijuana. ## Issue Whether *Terry*'s protective-search rationale permits an officer to search the passenger compartment of a vehicle for weapons during an investigative stop. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-07-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Michigan v. Long",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Watt",
          "cluster_id": 9459195,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane1_negative"
      },
      {
        "citing_case": {
          "name": "McGirt v. Oklahoma",
          "cluster_id": 4766667,
          "cite": [
            "591 U. S. 894",
            "140 S. Ct. 2452",
            "207 L. Ed. 2d 985"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane1_negative"
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
        "journal_ref": "Michigan v. Long:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Owens",
          "cluster_id": 4425178,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Coleman v. Thompson",
          "cluster_id": 112640,
          "cite": [
            "115 L. Ed. 2d 640",
            "111 S. Ct. 2546",
            "501 U.S. 722",
            "1991 U.S. LEXIS 3640"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. Palmer",
          "cluster_id": 111252,
          "cite": [
            "82 L. Ed. 2d 393",
            "104 S. Ct. 3194",
            "468 U.S. 517",
            "1984 U.S. LEXIS 143",
            "52 U.S.L.W. 5052"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delaware v. Van Arsdall",
          "cluster_id": 111625,
          "cite": [
            "89 L. Ed. 2d 674",
            "106 S. Ct. 1431",
            "475 U.S. 673",
            "1986 U.S. LEXIS 94",
            "20 Fed. R. Serv. 1",
            "54 U.S.L.W. 4347"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Teague v. Lane",
          "cluster_id": 112206,
          "cite": [
            "103 L. Ed. 2d 334",
            "109 S. Ct. 1060",
            "489 U.S. 288",
            "1989 U.S. LEXIS 1043"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Finley",
          "cluster_id": 111880,
          "cite": [
            "95 L. Ed. 2d 539",
            "107 S. Ct. 1990",
            "481 U.S. 551",
            "1987 U.S. LEXIS 2058",
            "55 U.S.L.W. 4612"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
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
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carmouche v. State",
          "cluster_id": 1463452,
          "cite": [
            "10 S.W.3d 323",
            "2000 Tex. Crim. App. LEXIS 8",
            "2000 WL 60020"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. Reed",
          "cluster_id": 112205,
          "cite": [
            "103 L. Ed. 2d 308",
            "109 S. Ct. 1038",
            "489 U.S. 255",
            "1989 U.S. LEXIS 1044",
            "57 U.S.L.W. 4224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lopez",
          "cluster_id": 117927,
          "cite": [
            "131 L. Ed. 2d 626",
            "115 S. Ct. 1624",
            "514 U.S. 549",
            "1995 U.S. LEXIS 3039"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Caldwell v. Mississippi",
          "cluster_id": 111471,
          "cite": [
            "86 L. Ed. 2d 231",
            "105 S. Ct. 2633",
            "472 U.S. 320",
            "1985 U.S. LEXIS 96",
            "53 U.S.L.W. 4743"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Gant",
          "cluster_id": 145887,
          "cite": [
            "173 L. Ed. 2d 485",
            "129 S. Ct. 1710",
            "556 U.S. 332",
            "2009 U.S. LEXIS 3120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Dickerson",
          "cluster_id": 112873,
          "cite": [
            "124 L. Ed. 2d 334",
            "113 S. Ct. 2130",
            "508 U.S. 366",
            "1993 U.S. LEXIS 4018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
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
        "journal_ref": "Michigan v. Long:lane2_top_cited"
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
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hensley",
          "cluster_id": 111294,
          "cite": [
            "83 L. Ed. 2d 604",
            "105 S. Ct. 675",
            "469 U.S. 221",
            "1985 U.S. LEXIS 34",
            "53 U.S.L.W. 4053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brigham City v. Stuart",
          "cluster_id": 145654,
          "cite": [
            "164 L. Ed. 2d 650",
            "126 S. Ct. 1943",
            "547 U.S. 398",
            "2006 U.S. LEXIS 4155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Buie",
          "cluster_id": 112384,
          "cite": [
            "108 L. Ed. 2d 276",
            "110 S. Ct. 1093",
            "494 U.S. 325",
            "1990 U.S. LEXIS 1176"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ohio v. Robinette",
          "cluster_id": 118066,
          "cite": [
            "136 L. Ed. 2d 347",
            "117 S. Ct. 417",
            "519 U.S. 33",
            "1996 U.S. LEXIS 6971"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
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
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Milkovich v. Lorain Journal Co.",
          "cluster_id": 112470,
          "cite": [
            "111 L. Ed. 2d 1",
            "110 S. Ct. 2695",
            "497 U.S. 1",
            "1990 U.S. LEXIS 3296",
            "17 Media L. Rep. (BNA) 2009",
            "58 U.S.L.W. 4846"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Olson",
          "cluster_id": 112416,
          "cite": [
            "109 L. Ed. 2d 85",
            "110 S. Ct. 1684",
            "495 U.S. 91",
            "1990 U.S. LEXIS 2038",
            "58 U.S.L.W. 4464"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Johnson",
          "cluster_id": 145912,
          "cite": [
            "172 L. Ed. 2d 694",
            "129 S. Ct. 781",
            "555 U.S. 323",
            "2009 U.S. LEXIS 868"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Wilson",
          "cluster_id": 118086,
          "cite": [
            "137 L. Ed. 2d 41",
            "117 S. Ct. 882",
            "519 U.S. 408",
            "1997 U.S. LEXIS 1271"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Chesternut",
          "cluster_id": 112095,
          "cite": [
            "100 L. Ed. 2d 565",
            "108 S. Ct. 1975",
            "486 U.S. 567",
            "1988 U.S. LEXIS 2582",
            "56 U.S.L.W. 4558"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Long:lane2_top_cited"
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
        "journal_ref": "Michigan v. Long:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111020 OR 9842054 OR 9842055) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDY3MjQ0ODAwMDAwJnM9Mzc3NTg2NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111020+OR+9842054+OR+9842055%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111020 OR 9842054 OR 9842055)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NzYmcz0yMzE2Njk4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111020+OR+9842054+OR+9842055%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111020 OR 9842054 OR 9842055)",
        "reviewed": 58,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 58,
        "triage_read": 1,
        "triage_snippet_classified": 57
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111020 OR 9842054 OR 9842055)",
    "indexed_citing_opinions": 2137,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111020,
        "count": 1892,
        "count_source": "search"
      },
      {
        "opinion_id": 9842054,
        "count": 292,
        "count_source": "search"
      },
      {
        "opinion_id": 9842055,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3765,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/michigan-v-long.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyMzA3MDImcz0xMDMzOTE5MyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111020+OR+9842054+OR+9842055%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111020,
        "cited_id": 92881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 93015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 96285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 97658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 97878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 98886,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 98966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 99227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 101688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 102305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 102505,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 102747,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 103332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 105015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 105047,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 105403,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 107526,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 107889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 108622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 108726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 108894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 109730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 109759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110044,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110824,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110975,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 110987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 341408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 360888,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 1087618,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 1266827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 1270558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 1585735,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 1724817,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 1752565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 1851863,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 1938258,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 2041383,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 2115863,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 2128917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111020,
        "cited_id": 2354063,
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
    "date_created": "2026-07-05T13:30:29Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:30:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:30:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:34:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:30:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Michigan v. Long

```
<opinion type="majority">
<author id="b1082-11">Justice O’Connor</author>
<p id="Athp">delivered the opinion of the Court.</p>
<p id="b1082-12">In <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), we upheld the validity of a protective search for weapons in the absence of probable cause to arrest because it is unreasonable to deny a police officer the right “to neutralize the threat of physical harm,” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio"><em>id., </em>at 24</a></span>, when he possesses an articulable suspicion that an individual is armed and dangerous. We did not, however, expressly address whether such a protective search for weapons could extend to an area beyond the person in the absence of probable cause to arrest. In the present case, respondent David Long was convicted for possession of marihuana found by police in the passenger compartment and trunk of the <page-number citation-index="1" label="1035">*1035</page-number>automobile that he was driving. The police searched the passenger compartment because they had reason to believe that the vehicle contained weapons potentially dangerous to the officers. We hold that the protective search of the passenger compartment was reasonable under the principles articulated in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>and other decisions of this Court. We also examine Long’s argument that the decision below rests upon an adequate and independent state ground, and we decide in favor of our jurisdiction.</p>
<p id="AJsq">H</p>
<p id="AuBi">Deputies Howell and Lewis were on patrol in a rural area one evening when, shortly after midnight, they observed a car traveling erratically and at excessive speed.<footnotemark>1</footnotemark> The officers observed the car turning down a side road, where it swerved off into a shallow ditch. The officers stopped to investigate. Long, the only occupant of the automobile, met the deputies at the rear of the car, which was protruding <page-number citation-index="1" label="1036">*1036</page-number>from the ditch onto the road. The door on the driver’s side of the vehicle was left open.</p>
<p id="b1084-5">Deputy Howell requested Long to produce his operator’s license, but he did not respond. After the request was repeated, Long produced his license. Long again failed to respond when Howell requested him to produce the vehicle registration. After another repeated request, Long, who Howell thought “appeared to be under the influence of something,” <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#469" aria-description="Citation for case: People v. Long">413 Mich. 461, 469</a></span>, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#868" aria-description="Citation for case: People v. Long">320 N. W. 2d 866, 868</a></span> (1982), turned from the officers and began walking toward the open door of the vehicle. The officers followed Long and both observed a large hunting knife on the floorboard of the driver’s side of the car. The officers then stopped Long’s progress and subjected him to a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>protective patdown, which revealed no weapons.</p>
<p id="b1084-6">Long and Deputy Lewis then stood by the rear of the vehicle while Deputy Howell shined his flashlight into the interior of the vehicle, but did not actually enter it. The purpose of Howell’s action was “to search for other weapons.” <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#469" aria-description="Citation for case: People v. Long">413 Mich., at 469</a></span>, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#868" aria-description="Citation for case: People v. Long">320 N. W. 2d, at 868</a></span>. The officer noticed that something was protruding from under the armrest on the front seat. He knelt in the vehicle and lifted the armrest. He saw an open pouch on the front seat, and upon flashing his light on the pouch, determined that it contained what appeared to be marihuana. After Deputy Howell showed the pouch and its contents to Deputy Lewis, Long was arrested for possession of marihuana. A further search of the interior of the vehicle, including the glovebox, revealed neither more contraband nor the vehicle registration. The officers decided to impound the vehicle. Deputy Howell opened the trunk, which did not have a lock, and discovered inside it approximately 75 pounds of marihuana.</p>
<p id="b1084-7">The Barry County Circuit Court denied Long’s motion to suppress the marihuana taken from both the interior of the car and its trunk. He was subsequently convicted of possession of marihuana. The Michigan Court of Appeals affirmed Long’s conviction, holding that the search of the passenger <page-number citation-index="1" label="1037">*1037</page-number>compartment was valid as a protective search under <em>Terry, swpra, </em>and that the search of the trunk was valid as an inventory search under <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span> (1976). See <span class="citation" data-id="1938258"><a href="/opinion/1938258/people-v-long/" aria-description="Citation for case: People v. Long">94 Mich. App. 338</a></span>, <span class="citation" data-id="1938258"><a href="/opinion/1938258/people-v-long/" aria-description="Citation for case: People v. Long">288 N. W. 2d 629</a></span> (1979). The Michigan Supreme Court reversed. The court held that “the sole justification of the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>search, protection of the police officers and others nearby, cannot justify the search in this case.” <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#472" aria-description="Citation for case: People v. Long">413 Mich., at 472</a></span>, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#869" aria-description="Citation for case: People v. Long">320 N. W. 2d, at 869</a></span>. The marihuana found in Long’s trunk was considered by the court below to be the “fruit” of the illegal search of the interior, and was also suppressed.<footnotemark>2</footnotemark></p>
<p id="b1085-5">We granted certiorari in this case to consider the important question of the authority of a police officer to protect himself by conducting a <em>Terry-type </em>search of the passenger compartment of a motor vehicle during the lawful investigatory stop of the occupant of the vehicle. <span class="citation multiple-matches"><a href="/c/U.%20S./459/904/">459 U. S. 904</a></span> (1982).</p>
<p id="b1085-6">II</p>
<p id="b1085-7">Before reaching the merits, we must consider Long’s argument that we are without jurisdiction to decide this case because the decision below rests on an adequate and independent state ground. The court below referred twice to the State Constitution in its opinion, but otherwise relied exclusively on federal law.<footnotemark>3</footnotemark> Long argues that the Michigan <page-number citation-index="1" label="1038">*1038</page-number>courts have provided greater protection from searches and seizures under the State Constitution than is afforded under the Fourth Amendment, and the references to the State Constitution therefore establish an adequate and independent ground for the decision below.</p>
<p id="b1086-5">It is, of course, “incumbent upon this Court... to ascertain for itself . . . whether the asserted non-federal ground independently and adequately supports the judgment. ” <em>Abie State Bank </em>v. <em>Bryan, </em><span class="citation" data-id="101688"><a href="/opinion/101688/abie-state-bank-v-bryan/#773" aria-description="Citation for case: Abie State Bank v. Bryan">282 U. S. 765, 773</a></span> (1931). Although we have announced a number of principles in order to help us determine whether various forms of references to state law constitute adequate and independent state grounds,<footnotemark>4</footnotemark> we openly admit that we have thus far not developed a satisfying and consistent approach for resolving this vexing issue. In some instances, we have taken the strict view that if the ground of decision was at all unclear, we would dismiss the case. See, <em>e. g., Lynch </em>v. <em>New York ex rel. Pierson, </em><span class="citation" data-id="102305"><a href="/opinion/102305/lynch-v-new-york-ex-rel-pierson/" aria-description="Citation for case: Lynch v. New York Ex Rel. Pierson">293 U. S. 52</a></span> (1934). In other instances, we have vacated, <page-number citation-index="1" label="1039">*1039</page-number>see, <em>e. g., Minnesota </em>v. <em>National Tea Co, </em><span class="citation" data-id="9419097"><a href="/opinion/103332/minnesota-v-national-tea-co/" aria-description="Citation for case: Minnesota v. National Tea Co.">309 U. S. 551</a></span> (1940), or continued a case, see, e. <em>g., Herb </em>v. <em>Pitcairn, </em><span class="citation" data-id="1087618"><a href="/opinion/1087618/herb-v-pitcairn/" aria-description="Citation for case: Herb v. Pitcairn">324 U. S. 117</a></span> (1945), in order to obtain clarification about the nature of a state court decision. See also <em>California </em>v. <em>Krivda, </em><span class="citation" data-id="108622"><a href="/opinion/108622/california-v-krivda/" aria-description="Citation for case: California v. Krivda">409 U. S. 33</a></span> (1972). In more recent cases, we have ourselves examined state law to determine whether state courts have used federal law to guide their application of state law or to provide the actual basis for the decision that was reached. See <em>Texas </em>v. <em>Brown, </em><span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#732" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 732-733, n. 1</a></span> (1983) (plurality opinion). Cf. <em>South Dakota </em>v. <em>Neville, </em><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#569" aria-description="Citation for case: South Dakota v. Neville">459 U. S. 553, 569</a></span> (1983) (Stevens, J., dissenting). In <em>Oregon </em>v. <em>Kennedy, </em><span class="citation" data-id="9428773"><a href="/opinion/110714/oregon-v-kennedy/#670" aria-description="Citation for case: Oregon v. Kennedy">456 U. S. 667, 670-671</a></span> (1982), we rejected an invitation to remand to the state court for clarification even when the decision rested in part on a case from the state court, because we determined that the state case itself rested upon federal grounds. We added that “[e]ven if the case admitted of more doubt as to whether federal and state grounds for decision were intermixed, the fact that the state court relied to the extent it did on federal grounds requires us to reach the merits.” <span class="citation" data-id="9428773"><a href="/opinion/110714/oregon-v-kennedy/#671" aria-description="Citation for case: Oregon v. Kennedy"><em>Id., </em>at 671</a></span>.</p>
<p id="b1087-5">This ad hoc method of dealing with cases that involve possible adequate and independent state grounds is antithetical to the doctrinal consistency that is required when sensitive issues of federal-state relations are involved. Moreover, none of the various methods of disposition that we have employed thus far recommends itself as the preferred method that we should apply to the exclusion of others, and we therefore determine that it is appropriate to reexamine our treatment of this jurisdictional issue in order to achieve the consistency that is necessary.</p>
<p id="b1087-6">The process of examining state law is unsatisfactory because it requires us to interpret state laws with which we are generally unfamiliar, and which often, as in this case, have not been discussed at length by the parties. Vacation and continuance for clarification have also been unsatisfactory both because of the delay and decrease in efficiency of judi<page-number citation-index="1" label="1040">*1040</page-number>cial administration, see <em>Dixon </em>v. <em>Duffy, </em><span class="citation" data-id="9420814"><a href="/opinion/105047/dixon-v-duffy/" aria-description="Citation for case: Dixon v. Duffy">344 U. S. 143</a></span> (1952),<footnotemark>5</footnotemark> and, more important, because these methods of disposition place significant burdens on state courts to demonstrate the presence or absence of our jurisdiction. See <em>Philadelphia Newspapers, Inc. </em>v. <em>Jerome, </em><span class="citation" data-id="9427020"><a href="/opinion/109759/philadelphia-newspapers-inc-v-jerome/#244" aria-description="Citation for case: Philadelphia Newspapers, Inc. v. Jerome">434 U. S. 241, 244</a></span> (1978) (Rehnquist, J., dissenting); <em>Department of Motor Vehicles </em>v. <em>Rios, </em><span class="citation" data-id="9425183"><a href="/opinion/108726/department-of-motor-vehicles-of-cal-v-rios/#427" aria-description="Citation for case: Department of Motor Vehicles of Cal. v. Rios">410 U. S. 425, 427</a></span> (1973) (Douglas, J., dissenting). Finally, outright dismissal of cases is clearly not a panacea because it cannot be doubted that there is an important need for uniformity in federal law, and that this need goes unsatisfied when we fail to review an opinion that rests primarily upon federal grounds and where the <em>independence </em>of an alleged state ground is not apparent from the four corners of the opinion. We have long recognized that dismissal is inappropriate “where there is strong indication . . . that the federal constitution as judicially construed controlled the decision below.” <em>National Tea Co., supra, </em>at 556.</p>
<p id="b1088-5">Respect for the independence of state courts, as well as avoidance of rendering advisory opinions, have been the cornerstones of this Court’s refusal to decide cases where there is an adequate and independent state ground. It is precisely because of this respect for state courts, and this desire to avoid advisory opinions, that we do not wish to continue to decide issues of state law that go beyond the opinion that we review, or to require state courts to reconsider cases to clarify the grounds of their decisions. Accordingly, when, as in this case, a state court decision fairly appears to rest primarily on federal law, or to be interwoven with the federal law, and when the adequacy and independence of any possible <page-number citation-index="1" label="1041">*1041</page-number>state law ground is not clear from the face of the opinion, we will accept as the most reasonable explanation that the state court decided the case the way it did because it believed that federal law required it to do so. If a state court chooses merely to rely on federal precedents as it would on the precedents of all other jurisdictions, then it need only make clear by a plain statement in its judgment or opinion that the federal cases are being used only for the purpose of guidance, and do not themselves compel the result that the court has reached. In this way, both justice and judicial administration will be greatly improved. If the state court decision indicates clearly and expressly that it is alternatively based on bona fide separate, adequate, and independent grounds, we, of course, will not undertake to review the decision.</p>
<p id="b1089-5">This approach obviates in most instances the need to examine state law in order to decide the nature of the state court decision, and will at the same time avoid the danger of our rendering advisory opinions.<footnotemark>6</footnotemark> It also avoids the unsatisfactory and intrusive practice of requiring state courts to clarify their decisions to the satisfaction of this Court. We believe that such an approach will provide state judges with a clearer opportunity to develop state jurisprudence unimpeded by federal interference, and yet will preserve the integrity of federal law. “It is fundamental that state courts be left free and unfettered by us in interpreting their state constitutions. But it is equally important that ambiguous or obscure adjudications by state courts do not stand as barriers to a determination by this Court of the validity under the federal constitution of state action.” <em>National Tea Co., supra, </em>at 557.</p>
<p id="b1089-6">The principle that we will not review judgments of state courts that rest on adequate and independent state grounds <page-number citation-index="1" label="1042">*1042</page-number>is based, in part, on “the limitations of our own jurisdiction.” <em>Herb </em>v. <em>Pitcairn, </em><span class="citation" data-id="1087618"><a href="/opinion/1087618/herb-v-pitcairn/#125" aria-description="Citation for case: Herb v. Pitcairn">324 U. S. 117, 125</a></span> (1945).<footnotemark>7</footnotemark> The jurisdictional concern is that we not “render an advisory opinion, and if the same judgment would be rendered by the state court after we corrected its views of federal laws, our review could amount to nothing more than an advisory opinion.” <span class="citation" data-id="1087618"><a href="/opinion/1087618/herb-v-pitcairn/#126" aria-description="Citation for case: Herb v. Pitcairn"><em>Id., </em>at 126</a></span>. Our requirement of a “plain statement” that a decision rests upon adequate and independent state grounds does not in any way authorize the rendering of advisory opinions. Rather, in determining, as we must, whether we have jurisdiction to review a case that is alleged to rest on adequate and independent state grounds, see <em>Abie State Bank </em>v. <em>Bryan, </em><span class="citation" data-id="101688"><a href="/opinion/101688/abie-state-bank-v-bryan/#773" aria-description="Citation for case: Abie State Bank v. Bryan">282 U. S., at 773</a></span>, we merely assume that there are no such grounds when it is not clear from the opinion itself that the state court relied upon an adequate and independent state ground and when it fairly appears that the state court rested its decision primarily on federal law.<footnotemark>8</footnotemark></p>
<p id="b1091-4"><page-number citation-index="1" label="1043">*1043</page-number>Our review of the decision below under this framework leaves us unconvinced that it rests upon an independent state ground. Apart from its two citations to the State Constitution, the court below relied <em>exclusively </em>on its understanding of <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>and other federal cases. Not a single state case was cited to support the state court’s holding that the search of the passenger compartment was unconstitutional.<footnotemark>9</footnotemark> Indeed, <page-number citation-index="1" label="1044">*1044</page-number>the court declared that the search in this case was unconstitutional because “[t]he Court of Appeals erroneously applied the principles of <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio</a></span> </em>... to the search of the interior of the vehicle in this case.” <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#471" aria-description="Citation for case: People v. Long">413 Mich., at 471</a></span>, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#869" aria-description="Citation for case: People v. Long">320 N. W. 2d, at 869</a></span>. The references to the State Constitution in no way indicate that the decision below rested on grounds in any way <em>independent </em>from the state court’s interpretation of federal law. Even if we accept that the Michigan Constitution has been interpreted to provide independent protection for certain rights also secured under the Fourth Amendment, it fairly appears in this case that the Michigan Supreme Court rested its decision primarily on federal law.</p>
<p id="b1092-5">Rather than dismissing the case, or requiring that the state court reconsider its decision on our behalf solely because of a mere possibility that an adequate and independent ground supports the judgment, we find that we have jurisdiction in the absence of a plain statement that the decision below rested on an adequate and independent state ground. It appears to us that the state court “felt compelled by what it understood to be federal constitutional considerations to construe ... its own law in the manner it did.” <em>Zacchini </em>v. <em>Scripps-Howard Broadcasting Co., </em><span class="citation" data-id="9426968"><a href="/opinion/109730/zacchini-v-scripps-howard-broadcasting-co/#568" aria-description="Citation for case: Zacchini v. Scripps-Howard Broadcasting Co.">433 U. S. 562, 568</a></span> (1977).<footnotemark>10</footnotemark></p>
<p id="AFD"><page-number citation-index="1" label="1045">*1045</page-number>HH J — I HH</p>
<p id="ADWv">The court below held, and respondent Long contends, that Deputy Howell’s entry into the vehicle cannot be justified under the principles set forth in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>because <em>“Terry </em>authorized only a limited pat-down search of a <em>person </em>suspected of criminal activity” rather than a search of an area. <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#472" aria-description="Citation for case: People v. Long">413 <page-number citation-index="1" label="1046">*1046</page-number>Mich., at 472</a></span>, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#869" aria-description="Citation for case: People v. Long">320 N. W. 2d, at 869</a></span> (footnote omitted). Brief for Respondent 10. Although <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>did involve the protective frisk of a person, we believe that the police action in this case is justified by the principles that we have already established in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>and other cases.</p>
<p id="b1094-5">In <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>the Court examined the validity of a “stop and frisk” in the absence of probable cause and a warrant. The police officer in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>detained several suspects to ascertain their identities after the officer had observed the suspects for a brief period of time and formed the conclusion that they were about to engage in criminal activity. Because the officer feared that the suspects were armed, he patted down the outside of the suspects’ clothing and discovered two revolvers.</p>
<p id="b1094-6">Examining the reasonableness of the officer’s conduct in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</em><footnotemark><em>11</em></footnotemark><em> </em>we held that there is “‘no ready test for determining reasonableness other than by balancing the need to search [or seize] against the invasion which the search [or seizure] entails.’” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 21</a></span> (quoting <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#536" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 536-537</a></span> (1967)). Although the conduct of the officer in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>involved a “severe, though brief, intrusion upon cherished personal security,” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 24-25</a></span>, <page-number citation-index="1" label="1047">*1047</page-number>we found that the conduct was reasonable when we weighed the interest of the individual against the legitimate interest in “crime prevention and detection,” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio"><em>id., </em>at 22</a></span>, and the “need for law enforcement officers to protect themselves and other prospective victims of violence in situations where they may lack probable cause for an arrest.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 24</a></span>. When the officer has a reasonable belief “that the individual whose suspicious behavior he is investigating at close range is armed and presently dangerous to the officer or to others, it would appear to be clearly unreasonable to deny the officer the power to take necessary measures to determine whether the person is in fact carrying a weapon and to neutralize the threat of physical harm.” <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ibid.</a></span></em></p>
<p id="b1095-5">Although <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>itself involved the stop and subsequent patdown search of a person, we were careful to note that “[w]e need not develop at length in this case, however, the limitations which the Fourth Amendment places upon a protective search and seizure for weapons. These limitations will have to be developed in the concrete factual circumstances of individual cases. ” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 29</a></span>. Contrary to Long’s view, <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>need not be read as restricting the preventative search to the person of the detained suspect.<footnotemark>12</footnotemark></p>
<p id="b1095-6">In two cases in which we applied <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>to specific factual situations, we recognized that investigative detentions involving suspects in vehicles are especially fraught with danger to police officers. In <em>Pennsylvania </em>v. <em>Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106</a></span> (1977), we held that police may order persons out of <page-number citation-index="1" label="1048">*1048</page-number>an automobile during a stop for a traffic violation, and may frisk those persons for weapons if there is a reasonable belief that they are armed and dangerous. Our decision rested in part on the “inordinate risk confronting an officer as he approaches a person seated in an automobile.” <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#110" aria-description="Citation for case: Pennsylvania v. Mimms"><em>Id., </em>at 110</a></span>. In <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972), we held that the police, acting on an informant’s tip, may reach into the passenger compartment of an automobile to remove a gun from a driver’s waistband even where the gun was not apparent to police from outside the car and the police knew of its existence only because of the tip. Again, our decision rested in part on our view of the danger presented to police officers in “traffic stop” and automobile situations.<footnotemark>13</footnotemark></p>
<blockquote id="b1095-8"><page-number citation-index="1" label="1047">*1047</page-number>“The opinion in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>authorized the frisking of an overcoat worn by defendant because that was the issue presented by the facts. One could reasonably conclude that a different result would not have been constitutionally required if the overcoat had been carried, folded over the forearm, rather than worn. The constitutional principles stated in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>would still control.” <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#475" aria-description="Citation for case: People v. Long">413 Mich., at 475-476</a></span>, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#871" aria-description="Citation for case: People v. Long">320 N. W. 2d, at 871</a></span> (footnote omitted).</blockquote>
<p id="b1096-5"><page-number citation-index="1" label="1048">*1048</page-number>Finally, we have also expressly recognized that suspects may injure police officers and others by virtue of their access to weapons, even though they may not themselves be armed. In the Term following <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>we decided <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), which involved the limitations imposed on police authority to conduct a search incident to a valid arrest. Relying explicitly on <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>we held that when an arrest is made, it is reasonable for the arresting officer to search “the arrestee’s person and the area ‘within his immediate control’ — construing that phrase to mean the area from within which he might gain possession of a weapon or destructible evidence.” <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span>. We reasoned that “[a] gun on a table or in a drawer in front of one who is arrested can be as dangerous to the arresting officer as one concealed in the clothing of the person arrested.” <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Ibid.</a></span> </em>In <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981), we determined that the lower courts “have found no workable definition of ‘the area within the immediate control of the arrestee’ when <page-number citation-index="1" label="1049">*1049</page-number>that area arguably includes the interior of an automobile and the arrestee is its recent occupant.” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton"><em>Id., </em>at 460</a></span>. In order to provide a “workable rule,” <em>ibid., </em>we held that “articles inside the relatively narrow compass of the passenger compartment of an automobile are in fact generally, even if not inevitably, within ‘the area into which an arrestee might reach in order to grab a weapon’ . . . .” <em>Ibid, </em>(quoting <em>Chimel, swpra, </em>at 763). We also held that the police may examine the contents of any open or closed container found within the passenger compartment, “for if the passenger compartment is within the reach of the arrestee, so will containers in it be within his reach.” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460</a></span> (footnote omitted). See also <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 702</a></span> (1981).</p>
<p id="b1097-5">Our past cases indicate then that protection of police and others can justify protective searches when police have a reasonable belief that the suspect poses a danger, that roadside encounters between police and suspects are especially hazardous, and that danger may arise from the possible presence of weapons in the area surrounding a suspect. These principles compel our conclusion that the search of the passenger compartment of an automobile, limited to those areas in which a weapon may be placed or hidden, is permissible if the police officer possesses a reasonable belief based on “specific and articulable facts which, taken together with the rational inferences from those facts, reasonably warrant” the officer in believing that the suspect is dangerous and the suspect may gain immediate control of weapons.<footnotemark>14</footnotemark> See <em>Terry, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 <page-number citation-index="1" label="1050">*1050</page-number>U. S., at 21</a></span>. “[T]he issue is whether a reasonably prudent man in the circumstances would be warranted in the belief that his safety or that of others was in danger.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 27</a></span>. If a suspect is “dangerous,” he is no less dangerous simply because he is not arrested. If, while conducting a legitimate <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>search of the interior of the automobile, the officer should, as here, discover contraband other than weapons, he clearly cannot be required to ignore the contraband, and the Fourth Amendment does not require its suppression in such circumstances. <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#465" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 465</a></span> (1971); <em>Michigan </em>v. <em>Tyler, </em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#509" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 509</a></span> (1978); <em>Texas </em>v. <em>Brown, </em><span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#739" aria-description="Citation for case: Texas v. Brown">460 U. S., at 739</a></span> (plurality opinion by Rehnquist, J.); <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#746" aria-description="Citation for case: Texas v. Brown"><em>id., </em>at 746</a></span> (Powell, J., concurring in judgment).</p>
<p id="b1098-4">The circumstances of this case clearly justified Deputies Howell and Lewis in their reasonable belief that Long posed a danger if he were permitted to reenter his vehicle. The hour was late and the area rural. Long was driving his automobile at excessive speed, and his car swerved into a ditch. The officers had to repeat their questions to Long, who appeared to be “under the influence” of some intoxicant. Long was not frisked until the officers observed that there was a large knife in the interior of the car into which Long was about to reenter. The subsequent search of the car was restricted to those areas to which Long would generally have immediate control, and that could contain a weapon. The trial court determined that the leather pouch containing <page-number citation-index="1" label="1051">*1051</page-number>marihuana could have contained a weapon. App. 64a.<footnotemark>15</footnotemark> It is clear that the intrusion was “strictly circumscribed by the exigencies which justified] its initiation.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#26" aria-description="Citation for case: Terry v. Ohio"><em>Terry, supra, </em>at 26</a></span>.</p>
<p id="b1099-5">In evaulating the validity of an officer’s investigative or protective conduct under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>the “[tjouchstone of our analysis ... is always ‘the reasonableness in all the circumstances of the particular governmental invasion of a citizen’s personal security.’” <em>Pennsylvania </em>v. <em>Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S., at 108</a></span>-109 (quoting <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><em>Terry, supra, </em>at 19</a></span>). In this case, the officers did not act unreasonably in taking preventive measures to ensure that there were no other weapons within Long’s immediate grasp before permitting him to reenter his automobile. Therefore, the balancing required by <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>clearly weighs in favor of allowing the police to conduct an area search of the passenger compartment to uncover weapons, as long as they possess an articulable and objectively reasonable belief that the suspect is potentially dangerous.</p>
<p id="b1099-6">The Michigan Supreme Court appeared to believe that it was not reasonable for the officers to fear that Long could injure them, because he was effectively under their control during the investigative stop and could not get access to any weapons that might have been located in the automobile. See <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#472" aria-description="Citation for case: People v. Long">413 Mich., at 472</a></span>, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#869" aria-description="Citation for case: People v. Long">320 N. W. 2d, at 869</a></span>. This reasoning is mistaken in several respects. During any investigative detention, the suspect is “in the control” of the officers in the sense that he “may be briefly detained against his will. . . .” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio"><em>Terry, supra, </em>at 34</a></span> (White, J., concurring). Just as a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>suspect on the street may, despite being under the brief control of a police officer, reach into his clothing and retrieve a weapon, so might a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>suspect in Long’s position break away from police control and retrieve a weapon from his automobile. See <em>United States </em>v. <em>Rainone, </em><span class="citation" data-id="360888"><a href="/opinion/360888/united-states-v-mario-rainone-and-rocco-circelli/#1134" aria-description="Citation for case: United States v. Mario Rainone and Rocco Circelli">586 F. 2d 1132, 1134</a></span> (CA71978), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./440/980/">440 U. S. 980</a></span> (1979). In addi-</p>
<p id="AJsy"><page-number citation-index="1" label="1052">*1052</page-number>tion, if the suspect is not placed under arrest, he will be permitted to reenter his automobile, and he will then have access to any weapons inside. <em>United States </em>v. <em>Powless, </em><span class="citation" data-id="341408"><a href="/opinion/341408/united-states-v-herbert-g-powless/#795" aria-description="Citation for case: United States v. Herbert G. Powless">546 F. 2d 792, 795-796</a></span> (CA8), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./430/910/">430 U. S. 910</a></span> (1977). Or, as here, the suspect may be permitted to reenter the vehicle before the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>investigation is over, and again, may have access to weapons. In any event, we stress that a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>investigation, such as the one that occurred here, involves a police investigation “at close range,” <em>Terry, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 24</a></span>, when the officer remains particularly vulnerable in part <em>because </em>a full custodial arrest has not been effected, and the officer must make a “quick decision as to how to protect himself and others from possible danger . . . .” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#28" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 28</a></span>. In such circumstances, we have not required that officers adopt alternative means to ensure their safety in order to avoid the intrusion involved in a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>encounter.<footnotemark>16</footnotemark></p>
<p id="Av4"><page-number citation-index="1" label="1053">*1053</page-number>HH <em>&lt;</em></p>
<p id="A1N">The trial court and the Court of Appeals upheld the search of the trunk as a valid inventory search under this Court’s decision in <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span> (1976). The Michigan Supreme Court did not address this holding, and instead suppressed the marihuana taken from the trunk as a fruit of the illegal search of the interior of the automobile. Our holding that the initial search was justified under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>makes it necessary to determine whether the trunk search was permissible under the Fourth Amendment. However, we decline to address this question because it was not passed upon by the Michigan Supreme Court, whose decision we review in this case. See <em>Cardinale </em>v. <em>Louisiana, </em><span class="citation" data-id="107889"><a href="/opinion/107889/cardinale-v-louisiana/#438" aria-description="Citation for case: Cardinale v. Louisiana">394 U. S. 437, 438</a></span> (1969). We remand this issue to the court below, to enable it to determine whether the trunk search was permissible under <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman, supra,</a></span> </em>or other decisions of this Court. See, <em>e. g., United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982).<footnotemark>17</footnotemark></p>
<p id="b1102-4"><page-number citation-index="1" label="1054">*1054</page-number>V</p>
<p id="b1102-5">The judgment of the Michigan Supreme Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b1102-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="AYW"> It is clear, and the respondent concedes, that if the officers had arrested Long for speeding or for driving while intoxicated, they could have searched the passenger compartment under <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981), and the trunk under <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982), if they had probable cause to believe that the trunk contained contraband. See Tr. of Oral Arg. 41. However, at oral argument, the State informed us that while Long could have been arrested for a speeding violation under Michigan law, he was <em>not </em>arrested because “[a]s a matter of practice,” police in Michigan do not arrest for speeding violations unless “more” is involved. See <em>id., </em>at 6. The officers did issue Long an appearance ticket. The petitioner also confirmed that the officers could have arrested Long for driving while intoxicated but they “would have to go through a process to make a determination as to whether the party is intoxicated and then go from that point.” <em>Ibid.</em></p>
<p id="AmP">The court below treated this case as involving a protective search, and not a search justified by probable cause to arrest for speeding, driving while intoxicated, or any other offense. Further, the petitioner does not argue <em>that </em>if probable cause to arrest exists, but the officers do not actually effect the arrest, the police may nevertheless conduct a search as broad as those authorized by <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>and <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>. </em>Accordingly, we do not address that issue.</p>
</footnote>
<footnote label="2">
<p id="b1085-8"> Chief Justice Coleman dissented, arguing that <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), authorized the area search, and that the trunk search was a valid inventory search. See <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#473" aria-description="Citation for case: People v. Long">413 Mich., at 473-480</a></span>, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#870" aria-description="Citation for case: People v. Long">320 N. W. 2d, at 870-873</a></span>. Justice Moody concurred in the result on the ground that the trunk search was improper. He agreed with Chief Justice Coleman that the interior search was proper under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>. </em>See <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#480" aria-description="Citation for case: People v. Long">413 Mich., at 480-486</a></span>, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#873" aria-description="Citation for case: People v. Long">320 N. W. 2d, at 873-875</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b1085-9"> On the first occasion, the court merely cited in a footnote both the State and Federal Constitutions. See <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#471" aria-description="Citation for case: People v. Long"><em>id., </em>at 471, n. 4</a></span>, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#869" aria-description="Citation for case: People v. Long">320 N. W. 2d, at 869, n. 4</a></span>. On the second occasion, at the conclusion of the opinion, the court stated: “We hold, therefore, that the deputies’ search of the vehicle was proscribed by the Fourth Amendment to the United States Constitution and art. 1, §11 of the Michigan Constitution.” <em>Id., </em>at 472-473, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#870" aria-description="Citation for case: People v. Long">320 N. W. 2d, at 870</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b1086-6"> For example, we have long recognized that “where the judgment of a state court rests upon two grounds, one of which is federal and the other non-federal in character, our jurisdiction fails if the non-federal ground is independent of the federal ground and adequate to support the judgment.” <em>Fox Film Corp. </em>v. <em>Muller, </em><span class="citation" data-id="102505"><a href="/opinion/102505/fox-film-corp-v-muller/#210" aria-description="Citation for case: Fox Film Corp. v. Muller">296 U. S. 207, 210</a></span> (1935). We may review a state case decided on a federal ground even if it is clear that there was an available state ground for decision on which the state court could properly have relied. <em>Beecher </em>v. <em>Alabama, </em><span class="citation" data-id="9423505"><a href="/opinion/107526/beecher-v-alabama/#37" aria-description="Citation for case: Beecher v. Alabama">389 U. S. 35, 37, n. 3</a></span> (1967). Also, if, in our view, the state court “ ‘felt compelled by what it understood to be federal constitutional considerations to construe ... its own law in the manner it did,’ ” then we will not treat a normally adequate state ground as independent, and there will be no question about our jurisdiction. <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#653" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 653</a></span> (1979) (quoting <em>Zacchini </em>v. <em>Scripps-Howard Broadcasting Co., </em><span class="citation" data-id="9426968"><a href="/opinion/109730/zacchini-v-scripps-howard-broadcasting-co/#568" aria-description="Citation for case: Zacchini v. Scripps-Howard Broadcasting Co.">433 U. S. 562, 568</a></span> (1977)). See also <em>South Dakota </em>v. <em>Neville, </em><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#556" aria-description="Citation for case: South Dakota v. Neville">459 U. S. 553, 556-557, n. 3</a></span> (1983). Finally, “where the non-federal ground is so interwoven with the [federal ground] as not to be an independent matter, or is not of sufficient breadth to sustain the judgment without any decision of the other, our jurisdiction is plain.” <em>Enterprise Irrigation District </em>v. <em>Farmers Mutual Canal Co., </em><span class="citation" data-id="98886"><a href="/opinion/98886/enterprise-irrigation-district-v-farmers-mutual-canal-co/#164" aria-description="Citation for case: Enterprise Irrigation District v. Farmers Mutual Canal Co.">243 U. S. 157, 164</a></span> (1917).</p>
</footnote>
<footnote label="5">
<p id="b1088-6"> Indeed, <em>Dixon </em>v. <em><span class="citation" data-id="9420814"><a href="/opinion/105047/dixon-v-duffy/" aria-description="Citation for case: Dixon v. Duffy">Duffy</a></span> </em>is also illustrative of another difficulty involved in our requiring state courts to reconsider their decisions for purposes of clarification. In <em><span class="citation" data-id="9420814"><a href="/opinion/105047/dixon-v-duffy/" aria-description="Citation for case: Dixon v. Duffy">Dixon</a></span>, </em>we continued the case on two occasions in order to obtain clarification, but none was forthcoming: “[T]he California court advised petitioner’s counsel informally that it doubted its jurisdiction to render such a determination.” 344 U, S., at 145. We then vacated the judgment of the state court, and remanded.</p>
</footnote>
<footnote label="6">
<p id="b1089-7"> There may be certain circumstances in which clarification is necessary or desirable, and we will not be foreclosed from taking the appropriate action.</p>
</footnote>
<footnote label="7">
<p id="b1090-5"> In <em>Herb </em>v. <em>Pitcairn, </em><span class="citation" data-id="1087618"><a href="/opinion/1087618/herb-v-pitcairn/#128" aria-description="Citation for case: Herb v. Pitcairn">324 U. S., at 128</a></span>, the Court also wrote that it was desirable that state courts “be asked rather than told what they have intended. ” It is clear that we have already departed from that view in those cases in which we have examined state law to determine whether a particular result was guided or compelled by federal law. Our decision today departs further from <em><span class="citation" data-id="1087618"><a href="/opinion/1087618/herb-v-pitcairn/" aria-description="Citation for case: Herb v. Pitcairn">Herb</a></span> </em>insofar as we disfavor further requests to state courts for clarification, and we require a clear and express statement that a decision rests on adequate and independent state grounds. However, the “plain statement” rule protects the integrity of state courts for the reasons discussed above. The preference for clarification expressed in <em><span class="citation" data-id="1087618"><a href="/opinion/1087618/herb-v-pitcairn/" aria-description="Citation for case: Herb v. Pitcairn">Herb</a></span> </em>has failed to be a completely satisfactory means of protecting the state and federal interests that are involved.</p>
</footnote>
<footnote label="8">
<p id="b1090-6"> It is not unusual for us to employ certain presumptions in deciding jurisdictional issues. For instance, although the petitioner bears the burden of establishing our jurisdiction, <em>Durley </em>v. <em>Mayo, </em><span class="citation" data-id="9421301"><a href="/opinion/105403/durley-v-mayo/#285" aria-description="Citation for case: Durley v. Mayo">351 U. S. 277, 285</a></span> (1956), we have held that the party who alleges that a controversy before us has become moot has the “heavy burden” of establishing that we lack jurisdiction. <em>County of Los Angeles </em>v. <em>Davis, </em><span class="citation" data-id="9427506"><a href="/opinion/110044/county-of-los-angeles-v-davis/#631" aria-description="Citation for case: County of Los Angeles v. Davis">440 U. S. 625, 631</a></span> (1979). That is, we presume in those circumstances that we have jurisdiction until some party establishes that we do not for reasons of mootness.</p>
<p id="b1090-7">We also note that the rule that we announce today was foreshadowed by our opinions in <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648</a></span> (1979), and <em>Zacchini </em>v. <em>Scripps-Howard Broadcasting Co., </em><span class="citation" data-id="9426968"><a href="/opinion/109730/zacchini-v-scripps-howard-broadcasting-co/" aria-description="Citation for case: Zacchini v. Scripps-Howard Broadcasting Co.">433 U. S. 562</a></span> (1977). In these cases, <page-number citation-index="1" label="1043">*1043</page-number>the state courts relied on both state and federal law. We determined that we had jurisdiction to decide the cases because our reading of the opinions led us to conclude that each court “felt compelled by what it understood to be federal constitutional considerations to construe and apply its own law in the manner it did.” <span class="citation" data-id="9426968"><a href="/opinion/109730/zacchini-v-scripps-howard-broadcasting-co/#568" aria-description="Citation for case: Zacchini v. Scripps-Howard Broadcasting Co."><em>Zacchini, supra, </em>at 568</a></span>; <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#653" aria-description="Citation for case: Delaware v. Prouse"><em>Delaware, supra, </em>at 653</a></span>. In <em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Delaware</a></span>, </em>we referred to prior state decisions that confirmed our understanding of the opinion in that case, but our primary focus was on the face of the opinion. In <em><span class="citation" data-id="9426968"><a href="/opinion/109730/zacchini-v-scripps-howard-broadcasting-co/" aria-description="Citation for case: Zacchini v. Scripps-Howard Broadcasting Co.">Zacchini</a></span>, </em>we relied entirely on the syllabus and opinion of the state court.</p>
<p id="A8N">In dissent, Justice Stevens proposes the novel view that this Court should never review a state court decision unless the Court wishes to vindicate a federal right that has been endangered. The rationale of the dissent is not restricted to cases where the decision is arguably supported by adequate and independent state grounds. Rather, Justice Stevens appears to believe that even if the decision below rests exclusively on federal grounds, this Court should not review the decision as long as there is no federal right that is endangered.</p>
<p id="As9v">The state courts handle the vast bulk of all criminal litigation in this country. In 1982, more than 12 million criminal actions (excluding juvenile and traffic charges) were filed in the 50 state court systems and the District of Columbia. See 7 State Court Journal, No. 1, p. 18 (1983). By comparison, approximately 32,700 criminal suits were filed in federal courts during that same year. See Annual Report of the Director of the Administrative Office of the United States Courts 6 (1982). The state courts are required to apply federal constitutional standards, and they necessarily create a considerable body of “federal law” in the process. It is not surprising that this Court has become more interested in the application and development of federal law by state courts in the light of the recent significant expansion of federally created standards that we have imposed on the States.</p>
</footnote>
<footnote label="9">
<p id="b1091-8"> At oral argument, Long argued that the state court relied on its decision in <em>People </em>v. <em>Reed, </em><span class="citation" data-id="1851863"><a href="/opinion/1851863/people-v-reed/" aria-description="Citation for case: People v. Reed">393 Mich. 342</a></span>, <span class="citation" data-id="1851863"><a href="/opinion/1851863/people-v-reed/" aria-description="Citation for case: People v. Reed">224 N. W. 2d 867</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./422/1044/">422 U. S. 1044</a></span> (1975). See Tr. of Oral Arg. 29. However, the court cited that ease only in the context of a statement that the State did not seek to justify the search in this case “by reference to other exceptions to the war<page-number citation-index="1" label="1044">*1044</page-number>rant requirement.” <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#472" aria-description="Citation for case: People v. Long">413 Mich., at 472</a></span>, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#869" aria-description="Citation for case: People v. Long">320 N. W. 2d, at 869-870</a></span> (footnote omitted). The court then noted that <em><span class="citation" data-id="1851863"><a href="/opinion/1851863/people-v-reed/" aria-description="Citation for case: People v. Reed">Reed</a></span> </em>held that ‘“[a] warrantless search and seizure is unreasonable per se and violates the Fourth Amendment of the United States Constitution and Art. 1, § 11 of the state constitution unless shown to be within one of the exceptions to the rule.’ ” <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#472" aria-description="Citation for case: People v. Long">413 Mich., at 472-473, n. 8</a></span>, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#870" aria-description="Citation for case: People v. Long">320 N. W. 2d, at 870, n. 8</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b1092-7"> There is nothing unfair about requiring a plain statement of an independent state ground in this case. Even if we were to rest our decision on an evaluation of the state law relevant to Long’s claim, as we have sometimes done in the past, our understanding of Michigan law would also result in our finding that we have jurisdiction to decide this case. Under state search-and-seizure law, a “higher standard” is imposed under Art. 1, § 11, of the 1963 Michigan Constitution. See <em>People </em>v. <em>Secrest, </em><span class="citation" data-id="1585735"><a href="/opinion/1585735/people-v-secrest/#525" aria-description="Citation for case: People v. Secrest">413 Mich. 521, 525</a></span>, <span class="citation" data-id="1585735"><a href="/opinion/1585735/people-v-secrest/#369" aria-description="Citation for case: People v. Secrest">321 N. W. 2d 368, 369</a></span> (1982). If, however, the item seized is, <em>inter </em><page-number citation-index="1" label="1045">*1045</page-number><em>alia, </em>a “narcotic drug . . . seized by a peace officer outside the curtilage of any dwelling house in this state,” Art. 1, § 11, of the 1963 Michigan Constitution, then the seizure is governed by a standard identical to that imposed by the Fourth Amendment. See <em>People </em>v. <em>Moore, </em><span class="citation" data-id="1270558"><a href="/opinion/1270558/people-v-moore/#435" aria-description="Citation for case: People v. Moore">391 Mich. 426, 435</a></span>, <span class="citation" data-id="1270558"><a href="/opinion/1270558/people-v-moore/#775" aria-description="Citation for case: People v. Moore">216 N. W. 2d 770, 775</a></span> (1974).</p>
<p id="AV0v">Long argues that under the current Michigan Comp. Laws §333.7107 (1979), the definition of a “narcotic” does not include marihuana. The difficulty with this argument is that Long fails to cite any authority for the proposition that the term “narcotic” as used in the Michigan Constitution is dependent on current statutory definitions of that term. Indeed, it appears that just the opposite is true. The Michigan Supreme Court has held that constitutional provisions are presumed “to be interpreted in accordance with existing laws and legal usages of the time” of the passage of the provision. <em>Bacon </em>v. <em>Kent-Ottawa Authority, </em><span class="citation" data-id="9528131"><a href="/opinion/2041383/bacon-v-kent-ottawa-metropolitan-water-authority/#169" aria-description="Citation for case: Bacon v. Kent-Ottawa Metropolitan Water Authority">354 Mich. 159, 169</a></span>, <span class="citation" data-id="9528131"><a href="/opinion/2041383/bacon-v-kent-ottawa-metropolitan-water-authority/#497" aria-description="Citation for case: Bacon v. Kent-Ottawa Metropolitan Water Authority">92 N. W. 2d 492, 497</a></span> (1958). If the state legislature were able to change the interpretation of a constitutional provision by statute, then the legislature would have “the power of outright repeal of a duly-voted constitutional provision.” <em><span class="citation" data-id="9528131"><a href="/opinion/2041383/bacon-v-kent-ottawa-metropolitan-water-authority/" aria-description="Citation for case: Bacon v. Kent-Ottawa Metropolitan Water Authority">Ibid.</a></span> </em>Applying these principles, the Michigan courts have held that a statute passed subsequent to the applicable state constitutional provision is not relevant for interpreting its Constitution, and that a definition in a legislative Act pertains only to that Act. <em>Jones </em>v. <em>City of Ypsilanti, </em><span class="citation" data-id="2115863"><a href="/opinion/2115863/jones-v-city-of-ypsilanti/" aria-description="Citation for case: Jones v. City of Ypsilanti">26 Mich. App. 574</a></span>, <span class="citation" data-id="2115863"><a href="/opinion/2115863/jones-v-city-of-ypsilanti/" aria-description="Citation for case: Jones v. City of Ypsilanti">182 N. W. 2d 795</a></span> (1970). See also <em>Walber </em>v. <em>Piggins, </em><span class="citation" data-id="1724817"><a href="/opinion/1724817/walber-v-wayne-circuit-judge/" aria-description="Citation for case: Walber v. Wayne Circuit Judge">2 Mich. App. 145</a></span>, <span class="citation" data-id="1724817"><a href="/opinion/1724817/walber-v-wayne-circuit-judge/" aria-description="Citation for case: Walber v. Wayne Circuit Judge">138 N. W. 2d 772</a></span> (1966), aff’d, <span class="citation" data-id="2128917"><a href="/opinion/2128917/walber-v-wayne-circuit-judge/" aria-description="Citation for case: Walber v. Wayne Circuit Judge">381 Mich. 138</a></span>, <span class="citation" data-id="2128917"><a href="/opinion/2128917/walber-v-wayne-circuit-judge/" aria-description="Citation for case: Walber v. Wayne Circuit Judge">160 N. W. 2d 876</a></span> (1968). At the time that the 1963 Michigan Constitution was enacted, it is clear that marihuana was considered a narcotic drug. See 1961 Mich. Pub. Acts, No. 206, § 1(f). Indeed, it appears that marihuana was considered a narcotic drug in Michigan until 1978, when it was removed from the narcotic classification. We would conclude that the seizure of marihuana in Michigan is not subject to analysis under any “higher standard” than may be imposed on the seizure of other items. In the light of our holding in <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648</a></span> (1979), that an interpretation of state law in our view compelled by federal constitutional considerations is not an independent state ground, we would have jurisdiction to decide the case.</p>
</footnote>
<footnote label="11">
<p id="b1094-7"> Although we did not in any way weaken the warrant requirement, we acknowledged that the typical “stop and frisk” situation involves “an entire rubric of police conduct — necessarily swift action predicated upon the on-the-spot observations of the officer on the beat — which historically has not been, and as a practical matter could not be, subjected to the warrant procedure. Instead, the conduct in this case must be tested by the Fourth Amendment’s general proscription against unreasonable searches and seizures.” <em>Terry, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20</a></span> (footnote omitted). We have emphasized that the propriety of a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop and frisk is to be judged according to whether the officer acted as a “reasonably prudent man” in deciding that the intrusion was justified. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 27</a></span>. “A brief stop of a suspicious individual, in order to determine his identity or to maintain the status quo momentarily while obtaining more information, may be most reasonable in light of the facts known to the officer at the time.” <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 146</a></span> (1972).</p>
</footnote>
<footnote label="12">
<p id="b1095-7"> As Chief Justice Coleman noted in her dissenting opinion in the present case:</p>
</footnote>
<footnote label="13">
<p id="b1096-6"> According to one study, “approximately 30% of police shootings occurred when a police officer approached a suspect seated in an automobile. Bristow, Police Officer Shootings — A Tactical Evaluation, 54 J. Crim. L. C. &amp; P. S. 93 (1963).” <em>Adams </em>v. <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#148" aria-description="Citation for case: Adams v. Williams"><em>Williams, supra, </em>at 148, n. 3</a></span>.</p>
</footnote>
<footnote label="14">
<p id="b1097-6"> We stress that our decision does not mean that the police may conduct automobile searches <em>whenever </em>they conduct an investigative stop, although the “bright line” that we drew in <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>clearly authorizes such a search whenever officers effect a custodial arrest. An additional interest exists in the arrest context, <em>i. e., </em>preservation of evidence, and this justifies an “automatic” search. However, that additional interest does not exist in the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>context. A <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>search, “unlike a search without a warrant incident to a lawful arrest, is not justified by any need to prevent the disappearance or destruction of evidence of crime. . . . The sole justification of <page-number citation-index="1" label="1050">*1050</page-number>the search ... is the protection of the police officer and others nearby . . . .” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 29</a></span>. What we borrow now from <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), and <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>is merely the recognition that part of the reason to allow area searches incident to an arrest is that the arrestee, who may not himself be armed, may be able to gain access to weapons to injure officers or others nearby, or otherwise to hinder legitimate police activity. This recognition applies as well in the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>context. However, because the interest in collecting and preserving evidence is not present in the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>context, we require that officers who conduct area searches during investigative detentions must do so only when they have the level of suspicion identified in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</em></p>
</footnote>
<footnote label="15">
<p id="b1099-7"> Of course, our analysis would apply to justify the search of Long’s person that was conducted by the officers after the discovery of the knife.</p>
</footnote>
<footnote label="16">
<p id="b1100-5"> Long makes a number of arguments concerning the invalidity of the search of the passenger compartment. The thrust of these arguments is that <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>searches are limited in scope and that an area search is fundamentally inconsistent with this limited scope. We have recognized that <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>searches are limited insofar as they may not be conducted in the absence of an articulable suspicion that the intrusion is justified, see, <em>e. g., Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#65" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 65</a></span> (1968), and that they are protective in nature and limited to weapons, see <em>Ybarra </em>v. <em>Illinois, </em><span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/#93" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85, 93-94</a></span> (1979). However, neither of these concerns is violated by our decision. To engage in an area search, which is limited to seeking weapons, the officer must have an articulable suspicion that the suspect is potentially dangerous.</p>
<p id="b1100-6">Long also argues that there cannot be a legitimate <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>search based on the discovery of the hunting knife because Long possessed that weapon legally. See Brief for Respondent 17. Assuming, <em>arguendo, </em>that Long possessed the knife lawfully, we have expressly rejected the view that the validity of a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>search depends on whether the weapon is possessed in accordance with state law. See <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S., at 146</a></span>.</p>
<p id="b1100-7">Contrary to Justice Brennan’s suggestion in dissent, the reasoning of <em>Terry, Chimel, </em>and <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>points clearly to the direction that we have taken today. Although <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>involved a full custodial arrest, the rationale for <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>rested on the recognition in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>that it is unreasonable to prevent the police from taking reasonable steps to protect their safety.</p>
<p id="AhTD"><page-number citation-index="1" label="1053">*1053</page-number>Justice Brennan suggests that we are expanding the scope of a <em>Terry-type </em>search to include a search incident to a valid arrest. However, our opinion clearly indicates that the area search that we approve is limited to a search for weapons in circumstances where the officers have a reasonable belief that the suspect is potentially dangerous to them. Justice Brennan quotes at length from <em>Sibron, </em>but fails to recognize that the search in that case was a search for narcotics, and not a search for weapons.</p>
<p id="Aka">Justice Brennan concedes that “police should not be exposed to unnecessary danger in the performance of their duties,” <em>post, </em>at 1064, but then would require that police officers, faced with having to make quick determinations about self-protection and the defense of innocent citizens in the area, must also decide instantaneously what “less intrusive” alternative exists to ensure that any threat presented by the suspect will be neutralized. <em>Post, </em>at 1065. For the practical reasons explained in <em>Terry, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 24, 28</a></span>, we have never required police to adopt alternative measures to avoid a legitimate Terry-type intrusion.</p>
</footnote>
<footnote label="17">
<p id="ARpn"> Long suggests that the trunk search is invalid under state law. See Tr. of Oral Arg. 41, 43-44. The Michigan Supreme Court is, of course, free to determine the validity of that search under state law.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Michigan v. Mosley.md  (`case`, 5 assertions)

### content_page

```
---
title: "Michigan v. Mosley"
type: case
citation: "423 U.S. 96 (1975)"
parallel_cite: "96 S. Ct. 321; 46 L. Ed. 2d 313"
neutral_cite: 1975 U.S. LEXIS 100
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1975
date_decided: 1975-12-09
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1975-12-09
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Michigan v. Mosley
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109336/michigan-v-mosley/"
  cluster_id: 109336
  opinion_id: 109336
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[Edwards v. Arizona]]", "[[Berghuis v. Thompkins]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "right-to-silence", "invocation"]
holding: "After a suspect invokes the right to SILENCE, later statements are admissible if police \"scrupulously honored\" the invocation — here,…"
lake:
  record_id: Michigan v. Mosley
  status: verified
  projected_at: 2026-07-06
---

# Michigan v. Mosley

*423 U.S. 96 (1975)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Mosley was arrested for robberies and given *[[Miranda v. Arizona|Miranda]]* warnings; when he said he did not want to talk about the robberies, the detective immediately stopped questioning. More than two hours later, a different detective in another location gave fresh *[[Miranda v. Arizona|Miranda]]* warnings and questioned Mosley about an unrelated holdup murder, and Mosley made incriminating statements.

## Issue
Whether, after a suspect in custody invokes his right to remain silent, the police may later resume questioning on a different offense.

## Rule
The answer turns on whether the invocation was honored: "We therefore conclude that the admissibility of statements obtained after the person in custody has decided to remain silent depends under *Miranda* on whether his 'right to cut off questioning' was 'scrupulously honored.'" — 423 U.S. at 104. ^pin-104

## Application
When Mosley said he did not want to discuss the robberies, the first detective immediately ceased questioning and made no effort to wear down his resistance. After a significant interval, a different officer gave fresh *[[Miranda v. Arizona|Miranda]]* warnings and questioned Mosley about an unrelated murder. Because his original invocation of silence was scrupulously honored, the later statements were admissible.

## Conclusion
Reversed; the statements obtained at the second interrogation were admissible.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Mosley* supplies the "scrupulously honored" standard for resuming questioning after an invocation of the right to silence, distinct from the counsel-invocation rule of [[Edwards v. Arizona]].

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *Michigan v. Mosley*, 423 U.S. 96 (1975) — https://www.courtlistener.com/opinion/109336/michigan-v-mosley/ — pinpoint: 104.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "04cd8531af74cde6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "423 U.S. 96 (1975)", "court": "U.S. Supreme Court", "neutral_cite": "1975 U.S. LEXIS 100", "official_citation_present": true, "parallel_cite": "96 S. Ct. 321; 46 L. Ed. 2d 313", "title": "Michigan v. Mosley", "year": "1975"}}
{"assertion_id": "7ed62dd9b51acb8a", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny / Refinement", "title": "Michigan v. Mosley"}}
{"assertion_id": "8696c710b51ead32", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "After a suspect invokes the right to SILENCE, later statements are admissible if police \\\"scrupulously honored\\\" the invocation — here,…", "title": "Michigan v. Mosley"}}
{"assertion_id": "111db9e410bbef94", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Michigan v. Mosley"}}
{"assertion_id": "351ad0af30071cdb", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1975-12-09", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Michigan v. Mosley", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Michigan v. Mosley", "varies_by_point": "false"}}
```

### lake record — Michigan v. Mosley

```json
{
  "schema_version": "s2.v1",
  "record_id": "Michigan v. Mosley",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Michigan v. Mosley",
    "case_name_short": "Mosley",
    "case_name_full": "Michigan v. Mosley",
    "input_case_name": "Michigan v. Mosley",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1975-12-09",
    "year": 1975,
    "docket": null,
    "cluster_id": 109336,
    "lead_opinion_id": 109336,
    "sibling_ids": [
      109336,
      9426230,
      9426231,
      9426232
    ],
    "absolute_url": "/opinion/109336/michigan-v-mosley/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9001359,
        "score": 20,
        "case_name": "Michigan v. Mosley"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "423 U.S. 96",
      "volume": "423",
      "reporter": "U.S.",
      "page": "96",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 321",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "321",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "46 L. Ed. 2d 313",
        "volume": "46",
        "reporter": "L. Ed. 2d",
        "page": "313",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1975 U.S. LEXIS 100",
        "volume": "1975",
        "reporter": "U.S. LEXIS",
        "page": "100",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "423 U.S. 96",
        "volume": "423",
        "reporter": "U.S.",
        "page": "96",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 321",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "321",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "46 L. Ed. 2d 313",
        "volume": "46",
        "reporter": "L. Ed. 2d",
        "page": "313",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1975 U.S. LEXIS 100",
        "volume": "1975",
        "reporter": "U.S. LEXIS",
        "page": "100",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "423 U.S. 96",
    "official_selection": {
      "court_class": "scotus",
      "selected": "423 U.S. 96",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-104",
      "page": null,
      "quote": "--- # Michigan v. Mosley *423 U.S. 96 (1975)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Mosley was arrested for robberies and given *Miranda* warnings; when he said he did not want to talk about the robberies, the detective immediately stopped questioning. More than two hours later, a different detective in another location gave fresh *Miranda* warnings and questioned Mosley about an unrelated holdup murder, and Mosley made incriminating statements. ## Issue Whether, after a suspect in custody invokes his right to remain silent, the police may later resume questioning on a different offense. ## Rule The answer turns on whether the invocation was honored:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1975-12-09",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Michigan v. Mosley",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Roberson",
          "cluster_id": 9481866,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Gonzalez",
          "cluster_id": 4892536,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nader Abdallah",
          "cluster_id": 4574399,
          "cite": [
            "911 F.3d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Durand",
          "cluster_id": 4303284,
          "cite": [
            "475 Mass. 657",
            "59 N.E.3d 1152"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kevin Jones, Jr. v. K. Harrington",
          "cluster_id": 4240929,
          "cite": [
            "829 F.3d 1128",
            "2015 U.S. App. LEXIS 23120",
            "2016 WL 3947820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Pacheco",
          "cluster_id": 2794582,
          "cite": [
            "87 Mass. App. Ct. 286"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Savoy v. State",
          "cluster_id": 2686761,
          "cite": [
            "218 Md. App. 130",
            "96 A.3d 842",
            "2014 WL 3752115",
            "2014 Md. App. LEXIS 78"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Oquendo-Rivas",
          "cluster_id": 2670502,
          "cite": [
            "750 F.3d 12",
            "2014 WL 1613682",
            "2014 U.S. App. LEXIS 7352"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane1_negative"
      },
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
        "journal_ref": "Michigan v. Mosley:lane1_negative"
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
        "journal_ref": "Michigan v. Mosley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gonzalez",
          "cluster_id": 2319916,
          "cite": [
            "25 A.3d 648",
            "302 Conn. 287",
            "2011 Conn. LEXIS 355",
            "2011 WL 3802478"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Edwards v. Arizona",
          "cluster_id": 110475,
          "cite": [
            "68 L. Ed. 2d 378",
            "101 S. Ct. 1880",
            "451 U.S. 477",
            "1981 U.S. LEXIS 96"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rhode Island v. Innis",
          "cluster_id": 110254,
          "cite": [
            "64 L. Ed. 2d 297",
            "100 S. Ct. 1682",
            "446 U.S. 291",
            "1980 U.S. LEXIS 94"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul v. Davis",
          "cluster_id": 109402,
          "cite": [
            "47 L. Ed. 2d 405",
            "96 S. Ct. 1155",
            "424 U.S. 693",
            "1976 U.S. LEXIS 112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
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
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
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
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
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
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. DiGuilio",
          "cluster_id": 1807773,
          "cite": [
            "491 So. 2d 1129",
            "11 Fla. L. Weekly 339"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Mathiason",
          "cluster_id": 109587,
          "cite": [
            "50 L. Ed. 2d 714",
            "97 S. Ct. 711",
            "429 U.S. 492",
            "1977 U.S. LEXIS 38"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brewer v. Williams",
          "cluster_id": 109624,
          "cite": [
            "51 L. Ed. 2d 424",
            "97 S. Ct. 1232",
            "430 U.S. 387",
            "1977 U.S. LEXIS 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
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
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
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
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hernandez v. State",
          "cluster_id": 2424950,
          "cite": [
            "988 S.W.2d 770",
            "1999 Tex. Crim. App. LEXIS 33",
            "1999 WL 212791"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
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
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dowthitt v. State",
          "cluster_id": 1777832,
          "cite": [
            "931 S.W.2d 244",
            "1996 Tex. Crim. App. LEXIS 93",
            "1996 WL 347772"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Bradshaw",
          "cluster_id": 110987,
          "cite": [
            "77 L. Ed. 2d 405",
            "103 S. Ct. 2830",
            "462 U.S. 1039",
            "1983 U.S. LEXIS 82",
            "51 U.S.L.W. 4940"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Illinois",
          "cluster_id": 111288,
          "cite": [
            "83 L. Ed. 2d 488",
            "105 S. Ct. 490",
            "469 U.S. 91",
            "1984 U.S. LEXIS 167",
            "53 U.S.L.W. 3430"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Miller",
          "cluster_id": 109433,
          "cite": [
            "48 L. Ed. 2d 71",
            "96 S. Ct. 1619",
            "425 U.S. 435",
            "1976 U.S. LEXIS 148",
            "37 A.F.T.R.2d (RIA) 1261"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
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
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Roberson",
          "cluster_id": 112100,
          "cite": [
            "100 L. Ed. 2d 704",
            "108 S. Ct. 2093",
            "486 U.S. 675",
            "1988 U.S. LEXIS 2726",
            "56 U.S.L.W. 4590"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
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
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
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
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Harvey",
          "cluster_id": 112385,
          "cite": [
            "108 L. Ed. 2d 293",
            "110 S. Ct. 1176",
            "494 U.S. 344",
            "1990 U.S. LEXIS 1229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
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
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neal v. State",
          "cluster_id": 1869722,
          "cite": [
            "451 So. 2d 743"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Marko",
          "cluster_id": 3008904,
          "cite": [
            "2015 COA 139",
            "434 P.3d 618"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Mosley:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109336 OR 9426230 OR 9426231 OR 9426232) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzAzMjU3NjAwMDAwJnM9MjE1MTEzJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109336+OR+9426230+OR+9426231+OR+9426232%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109336 OR 9426230 OR 9426231 OR 9426232)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMjgmcz0zNDIyODMmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109336+OR+9426230+OR+9426231+OR+9426232%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109336 OR 9426230 OR 9426231 OR 9426232)",
        "reviewed": 29,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 29,
        "triage_read": 1,
        "triage_snippet_classified": 28
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109336 OR 9426230 OR 9426231 OR 9426232)",
    "indexed_citing_opinions": 1649,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109336,
        "count": 1501,
        "count_source": "search"
      },
      {
        "opinion_id": 9426230,
        "count": 184,
        "count_source": "search"
      },
      {
        "opinion_id": 9426231,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426232,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2562,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/michigan-v-mosley.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2OTk2MTkmcz05NDgxODY2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109336+OR+9426230+OR+9426231+OR+9426232%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109336,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 107951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 108137,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 108138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 108139,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 108416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 108429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 108762,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 109309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 279322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 304272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 316371,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 1166074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 1180572,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 1192799,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 1203861,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 1244888,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 1246504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 1270289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 1580188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 1633109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 1674847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 1720652,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 1837757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 1958523,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 2007024,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 2041775,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 2281071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 2301022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 2341485,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 2455151,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109336,
        "cited_id": 2596192,
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
    "date_created": "2026-07-05T13:34:04Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:34:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:34:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:38:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:34:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Michigan v. Mosley

```
<div>
<center><b><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">423 U.S. 96</a></span> (1975)</b></center>
<center><h1>MICHIGAN<br>
v.<br>
MOSLEY.</h1></center>
<center>No. 74-653.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 6, 1975.</center>
<center>Decided December 9, 1975.</center>
CERTIORARI TO THE COURT OF APPEALS OF MICHIGAN.
<p><i>Thomas M. Khalil</i> argued the cause for petitioner. With him on the brief were <i>William L. Cahalan, Dominick R. Carnovale,</i> and <i>Robert A. Reuther.</i></p>
<p><i>Carl Ziemba</i> argued the cause and filed a brief for respondent.<sup>[*]</sup></p>
<p><span class="star-pagination">*97</span> MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>The respondent, Richard Bert Mosley, was arrested in Detroit, Mich., in the early afternoon of April 8, 1971, in connection with robberies that had recently occurred at the Blue Goose Bar and the White Tower Restaurant on that city's lower east side. The arresting officer, Detective James Cowie of the Armed Robbery Section of the Detroit Police Department, was acting on a tip implicating Mosley and three other men in the robberies.<sup>[1]</sup> After effecting the arrest, Detective Cowie brought Mosley to the Robbery, Breaking and Entering Bureau of the Police Department, located on the fourth floor of the departmental headquarters building. The officer advised Mosley of his rights under this Court's decision in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, and had him read and sign the department's constitutional rights notification certificate. After filling out the necessary arrest papers, Cowie began questioning Mosley about the robbery of the White Tower Restaurant. When Mosley said he did not want to answer any questions about the robberies, Cowie promptly ceased the interrogation. The completion of the arrest papers and the questioning of Mosley together took approximately 20 minutes. At no time during the questioning did Mosley indicate a desire to consult with a lawyer, and there is no claim that the procedures followed to this point did not fully comply with the strictures of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion. Mosley was then taken to a ninth-floor cell block.</p>
<p>Shortly after 6 p. m., Detective Hill of the Detroit <span class="star-pagination">*98</span> Police Department Homicide Bureau brought Mosley from the cell block to the fifth-floor office of the Homicide Bureau for questioning about the fatal shooting of a man named Leroy Williams. Williams had been killed on January 9, 1971, during a holdup attempt outside the 101 Ranch Bar in Detroit. Mosley had not been arrested on this charge or interrogated about it by Detective Cowie.<sup>[2]</sup> Before questioning Mosley about this homicide, Detective Hill carefully advised him of his "<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> rights." Mosley read the notification form both silently and aloud, and Detective Hill then read and explained the warnings to him and had him sign the form. Mosley at first denied any involvement in the Williams murder, but after the officer told him that Anthony Smith had confessed to participating in the slaying and had named him as the "shooter," Mosley made a statement implicating himself in the homicide.<sup>[3]</sup> The interrogation by Detective Hill lasted approximately 15 minutes, and at no time during its course did Mosley ask to consult with a lawyer or indicate that he did not want to discuss the homicide. In short, there is no claim that the procedures followed during Detective Hill's interrogation of Mosley, standing alone, did not fully comply with the strictures of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion.<sup>[4]</sup></p>
<p>Mosley was subsequently charged in a one-count information with first-degree murder. Before the trial he moved to suppress his incriminating statement on a number of grounds, among them the claim that under the doctrine of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> case it was constitutionally <span class="star-pagination">*99</span> impermissible for Detective Hill to question him about the Williams murder after he had told Detective Cowie that he did not want to answer any questions about the robberies.<sup>[5]</sup> The trial court denied the motion to suppress after an evidentiary hearing, and the incriminating statement was subsequently introduced in evidence against Mosley at his trial. The jury convicted Mosley of first-degree murder, and the court imposed a mandatory sentence of life imprisonment.</p>
<p>On appeal to the Michigan Court of Appeals, Mosley renewed his previous objections to the use of his incriminating statement in evidence. The appellate court reversed the judgment of conviction, holding that Detective Hill's interrogation of Mosley had been a <i>per se</i> violation of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> doctrine. Accordingly, without reaching Mosley's other contentions, the Court remanded the case for a new trial with instructions that Mosley's statement be suppressed as evidence. <span class="citation" data-id="1674847"><a href="/opinion/1674847/people-v-mosley/" aria-description="Citation for case: People v. Mosley">51 Mich. App. 105</a></span>, <span class="citation" data-id="1674847"><a href="/opinion/1674847/people-v-mosley/" aria-description="Citation for case: People v. Mosley">214 N. W. 2d 564</a></span>. After further appeal was denied by the Michigan Supreme Court, <span class="citation no-link">392 Mich. 764</span>, the State filed a petition for certiorari here. We granted the writ because of the important constitutional question presented. <span class="citation multiple-matches"><a href="/c/U.%20S./419/1119/">419 U. S. 1119</a></span>.</p>
<p>In the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> case this Court promulgated a set of safeguards to protect the there-delineated constitutional rights of persons subjected to custodial police interrogation. In sum, the Court held in that case that unless law enforcement officers give certain specified warnings before <span class="star-pagination">*100</span> questioning a person in custody,<sup>[6]</sup> and follow certain specified procedures during the course of any subsequent interrogation, any statement made by the person in custody cannot over his objection be admitted in evidence against him as a defendant at trial, even though the statement may in fact be wholly voluntary. See <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#443" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 443</a></span>.</p>
<p>Neither party in the present case challenges the continuing validity of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decision, or of any of the so-called guidelines it established to protect what the Court there said was a person's constitutional privilege against compulsory self-incrimination. The issue in this case, rather, is whether the conduct of the Detroit police that led to Mosley's incriminating statement did in fact violate the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> "guidelines," so as to render the statement inadmissible in evidence against Mosley at his trial. Resolution of the question turns almost entirely on the interpretation of a single passage in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion, upon which the Michigan appellate court relied in finding a <i>per se</i> violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>:</i></p>
<blockquote>"Once warnings have been given, the subsequent procedure is clear. If the individual indicates in any manner, at any time prior to or during questioning, that he wishes to remain silent, the interrogation must cease. At this point he has shown that he intends to exercise his Fifth Amendment privilege; any statement taken after the person invokes his privilege cannot be other than the product of compulsion, subtle or otherwise. Without the right to cut off questioning, the setting of in-custody <span class="star-pagination">*101</span> interrogation operates on the individual to overcome free choice in producing a statement after the privilege has been once invoked." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#473" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 473-474</a></span>.<sup>[7]</sup></blockquote>
<p>This passage states that "the interrogation must cease" when the person in custody indicates that "he wishes to remain silent." It does not state under what circumstances, if any, a resumption of questioning is permissible.<sup>[8]</sup> The passage could be literally read to mean that <span class="star-pagination">*102</span> a person who has invoked his "right to silence" can never again be subjected to custodial interrogation by any police officer at any time or place on any subject. Another possible construction of the passage would characterize "any statement taken after the person invokes his privilege" as "the product of compulsion" and would therefore mandate its exclusion from evidence, even if it were volunteered by the person in custody without any further interrogation whatever. Or the passage could be interpreted to require only the immediate cessation of questioning, and to permit a resumption of interrogation after a momentary respite.</p>
<p>It is evident that any of these possible literal interpretations would lead to absurd and unintended results. To permit the continuation of custodial interrogation after a momentary cessation would clearly frustrate the purposes of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> by allowing repeated rounds of questioning to undermine the will of the person being questioned. At the other extreme, a blanket prohibition against the taking of voluntary statements or a permanent immunity from further interrogation, regardless of the circumstances, would transform the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> safeguards into wholly irrational obstacles to legitimate police investigative activity, and deprive suspects of an opportunity to make informed and intelligent assessments of their interests. Clearly, therefore, neither this passage nor any other passage in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion can sensibly be read to create a <i>per se</i> proscription of indefinite duration upon any further questioning by any <span class="star-pagination">*103</span> police officer on any subject, once the person in custody has indicated a desire to remain silent.<sup>[9]</sup></p>
<p>A reasonable and faithful interpretation of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion must rest on the intention of the Court in that case to adopt "fully effective means . . . to notify the person of his right of silence and to assure that the exercise of the right will be scrupulously honored . . . ." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 479</a></span>. The critical safeguard identified in the passage at issue is a person's "right to cut off questioning." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 474</a></span>. Through the exercise of his option to terminate questioning he can control the time at <span class="star-pagination">*104</span> which questioning occurs, the subjects discussed, and the duration of the interrogation. The requirement that law enforcement authorities must respect a person's exercise of that option counteracts the coercive pressures of the custodial setting. We therefore conclude that the admissibility of statements obtained after the person in custody has decided to remain silent depends under <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> on whether his "right to cut off questioning" was "scrupulously honored."<sup>[10]</sup></p>
<p>A review of the circumstances leading to Mosley's confession reveals that his "right to cut off questioning" was fully respected in this case. Before his initial interrogation, Mosley was carefully advised that he was under no obligation to answer any questions and could remain silent if he wished. He orally acknowledged that he understood the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and then signed a printed notification-of-rights form. When Mosley stated that he did not want to discuss the robberies, Detective Cowie immediately ceased the interrogation and did not try either to resume the questioning or in any way to persuade Mosley to reconsider his position. After an interval of more than two hours, Mosley was questioned by another police officer at another location about an unrelated holdup murder. He was given full and complete <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings at the outset of the second interrogation. He was thus reminded again that he could remain silent and could consult with a lawyer, <span class="star-pagination">*105</span> and was carefully given a full and fair opportunity to exercise these options. The subsequent questioning did not undercut Mosley's previous decision not to answer Detective Cowie's inquiries. Detective Hill did not resume the interrogation about the White Tower Restaurant robbery or inquire about the Blue Goose Bar robbery, but instead focused exclusively on the Leroy Williams homicide, a crime different in nature and in time and place of occurrence from the robberies for which Mosley had been arrested and interrogated by Detective Cowie. Although it is not clear from the record how much Detective Hill knew about the earlier interrogation, his questioning of Mosley about an unrelated homicide was quite consistent with a reasonable interpretation of Mosley's earlier refusal to answer any questions about the robberies.<sup>[11]</sup></p>
<p>This is not a case, therefore, where the police failed to honor a decision of a person in custody to cut off questioning, either by refusing to discontinue the interrogation upon request or by persisting in repeated efforts to <span class="star-pagination">*106</span> wear down his resistance and make him change his mind. In contrast to such practices, the police here immediately ceased the interrogation, resumed questioning only after the passage of a significant period of time and the provision of a fresh set of warnings, and restricted the second interrogation to a crime that had not been a subject of the earlier interrogation.</p>
<p>The Michigan Court of Appeals viewed this case as factually similar to <i>Westover</i> v. <i>United States,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, a companion case to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> But the controlling facts of the two cases are strikingly different.</p>
<p>In <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Westover</a></span>,</i> the petitioner was arrested by the Kansas City police at 9:45 p. m. and taken to the police station. Without giving any advisory warnings of any kind to Westover, the police questioned him that night and throughout the next morning about various local robberies. At noon, three FBI agents took over, gave advisory warnings to Westover, and proceeded to question him about two California bank robberies. After two hours of questioning, the petitioner confessed to the California crimes. The Court held that the confession obtained by the FBI was inadmissible because the interrogation leading to the petitioner's statement followed on the heels of prolonged questioning that was commenced and continued by the Kansas City police without preliminary warnings to Westover of any kind. The Court found that "the federal authorities were the beneficiaries of the pressure applied by the local in-custody interrogation" and that the belated warnings given by the federal officers were "not sufficient to protect" Westover because from his point of view "the warnings came at the end of the interrogation process." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#497" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 497, 496</a></span>.</p>
<p>Here, by contrast, the police gave full "<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> warnings" to Mosley at the very outset of each interrogation, subjected him to only a brief period of initial questioning, <span class="star-pagination">*107</span> and suspended questioning entirely for a significant period before beginning the interrogation that led to his incriminating statement. The cardinal fact of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Westover</a></span></i> the failure of the police officers to give any warnings whatever to the person in their custody before embarking on an intense and prolonged interrogation of himwas simply not present in this case. The Michigan Court of Appeals was mistaken, therefore, in believing that Detective Hill's questioning of Mosley was "not permitted" by the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Westover</a></span></i> decision. <span class="citation" data-id="1674847"><a href="/opinion/1674847/people-v-mosley/#108" aria-description="Citation for case: People v. Mosley">51 Mich. App., at 108</a></span>, <span class="citation" data-id="1674847"><a href="/opinion/1674847/people-v-mosley/#566" aria-description="Citation for case: People v. Mosley">214 N. W. 2d, at 566</a></span>.</p>
<p>For these reasons, we conclude that the admission in evidence of Mosley's incriminating statement did not violate the principles of <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span></i><i>.</i> Accordingly, the judgment of the Michigan Court of Appeals is vacated, and the case is remanded to that court for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE WHITE, concurring in the result.</p>
<p>I concur in the result and in much of the majority's reasoning. However, it appears to me that, in an effort to make only a limited holding in this case, the majority has implied that some custodial confessions will be suppressed even though they follow an informed and voluntary waiver of the defendant's rights. The majority seems to say that a statement obtained within some unspecified time after an assertion by an individual of his "right to silence" is always inadmissible, even if it was the result of an informed and voluntary decisionfollowing, for example, a disclosure to such an individual of a piece of information bearing on his waiver decision which the police had failed to give him prior to his assertion of the privilege but which they gave him immediately thereafter. Indeed, <i>ante,</i> at 102, the majority characterizes <span class="star-pagination">*108</span> as "absurd" any contrary rule. I disagree. I do not think the majority's conclusion is compelled by <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and I suspect that in the final analysis the majority will adopt voluntariness as the standard by which to judge the waiver of the right to silence by a properly informed defendant. I think the Court should say so now.</p>
<p><i>Miranda</i> holds that custody creates an inherent compulsion on an individual to incriminate himself in response to questions, and that statements obtained under such circumstances are therefore obtained in violation of the Fifth Amendment privilege against compelled testimonial self-incrimination unless the privilege is "knowingly and intelligently waived." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#471" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 471, 475</a></span>. It also holds that an individual will not be deemed to have made a knowing and intelligent waiver of his "right to silence" unless the authorities have first informed him, <i>inter alia,</i> of that right"the threshold requirement for an intelligent decision as to its exercise." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#468" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 468</a></span>. I am no more convinced that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was required by the United States Constitution than I was when it was decided. However, there is at least some support in the law both before and after <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> for the proposition that some rights will never be deemed waived unless the defendant is first expressly advised of their existence. <i>E. g., </i><i>Carnley</i> v. <i>Cochran,</i> <span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/" aria-description="Citation for case: Carnley v. Cochran">369 U. S. 506</a></span> (1962); <i>Boykin</i> v. <i>Alabama,</i> <span class="citation" data-id="9424054"><a href="/opinion/107951/boykin-v-alabama/" aria-description="Citation for case: Boykin v. Alabama">395 U. S. 238</a></span> (1969); Fed. Rules Crim. Proc. 11, 32 (a) (2). There is little support in the law or in common sense for the proposition that an <i>informed</i> waiver of a right may be ineffective even where voluntarily made. Indeed, the law is exactly to the contrary, <i>e. g., </i><i>Tollett</i> v. <i>Henderson,</i> <span class="citation" data-id="9425244"><a href="/opinion/108762/tollett-v-henderson/" aria-description="Citation for case: Tollett v. Henderson">411 U. S. 258</a></span> (1973); <i>Brady</i> v. <i>United States,</i> <span class="citation" data-id="108137"><a href="/opinion/108137/brady-v-united-states/" aria-description="Citation for case: Brady v. United States">397 U. S. 742</a></span> (1970); <i>McMann</i> v. <i>Richardson,</i> <span class="citation" data-id="9424256"><a href="/opinion/108138/mcmann-v-richardson/" aria-description="Citation for case: McMann v. Richardson">397 U. S. 759</a></span> (1970); <i>Parker</i> v. <i>North Carolina,</i> <span class="citation" data-id="9424258"><a href="/opinion/108139/parker-v-north-carolina/" aria-description="Citation for case: Parker v. North Carolina">397 U. S. 790</a></span> (1970). Unless an individual is <span class="star-pagination">*109</span> incompetent, we have in the past rejected any paternalistic rule protecting a defendant from his intelligent and voluntary decisions about his own criminal case. <i>Faretta</i> v. <i>California,</i> <span class="citation" data-id="9426191"><a href="/opinion/109309/faretta-v-california/" aria-description="Citation for case: Faretta v. California">422 U. S. 806</a></span> (1975). To do so would be to "imprison a man in his privileges,"<sup>[1]</sup><i>Adams</i> v. <i>United States ex rel. McCann,</i> <span class="citation" data-id="9419274"><a href="/opinion/103735/adams-v-united-states-ex-rel-mccann/#280" aria-description="Citation for case: Adams v. United States Ex Rel. McCann">317 U. S. 269, 280</a></span> (1942), and to disregard " `that respect for the individual which is the lifeblood of the law,' " <i>Faretta</i> v. <span class="citation" data-id="9426191"><a href="/opinion/109309/faretta-v-california/#834" aria-description="Citation for case: Faretta v. California"><i>California, supra,</i> at 834</a></span>. I am very reluctant to conclude that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> stands for such a proposition.</p>
<p>The language of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> no more compels such a result than does its basic rationale. As the majority points out, the statement in <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 474</a></span>, requiring interrogation to <i>cease</i> after an assertion of the "right to silence" tells us nothing because it does not indicate how soon this interrogation may resume. The Court showed in the very next paragraph, moreover, that when it wanted to create a <i>per se</i> rule against further interrogation after assertion of a right, it knew how to do so. The Court there said "[i]f the individual states that he <span class="star-pagination">*110</span> wants an attorney, the interrogation must cease <i>until an attorney is present.</i>" <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i><sup>[2]</sup> However, when the individual indicates that <i>he</i> will decide unaided by counsel whether or not to assert his "right to silence" the situation is different. In such a situation, the Court in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> simply said: "If the interrogation continues without the presence of an attorney and a statement is taken, a heavy burden rests on the government to demonstrate that the defendant knowingly and intelligently waived his privilege against self-incrimination and his right to retained or appointed counsel." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 475</a></span>. Apparently, although placing a heavy burden on the government, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> intended waiver of the "right to silence" to be tested by the normal standards. In any event, insofar as the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decision might be read to require interrogation to cease for some magical and unspecified period of time following an assertion of the "right to silence," and to reject voluntariness as the standard by which to judge informed waivers of that right, it should be disapproved as inconsistent with otherwise uniformly applied legal principles.</p>
<p>In justifying the implication that questioning must inevitably cease for some unspecified period of time following an exercise of the "right to silence," the majority <span class="star-pagination">*111</span> says only that such a requirement would be necessary to avoid "undermining" "the will of the person being questioned." Yet surely a waiver of the "right to silence" obtained by "undermining the will" of the person being questioned would be considered an involuntary waiver. Thus, in order to achieve the majority's only stated purpose, it is sufficient to exclude all confessions which are the result of involuntary waivers. To exclude any others is to deprive the factfinding process of highly probative information for no reason at all. The "repeated rounds" of questioning following an assertion of the privilege, which the majority is worried about, would, of course, count heavily against the State in any determination of voluntarinessparticularly if no reason (such as new facts communicated to the accused or a new incident being inquired about) appeared for repeated questioning. There is no reason, however, to rob the accused of the choice to answer questions voluntarily for some unspecified period of time following his own previous contrary decision. The Court should now so state.</p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE MARSHALL joins, dissenting.</p>
<p>The Court focuses on the correct passage from <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#473" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 473-474</a></span> (1966) (footnote omitted):</p>
<blockquote>"Once warnings have been given, the subsequent procedure is clear. If the individual indicates in any manner, at any time prior to or during questioning, that he wishes to remain silent, the interrogation must cease. At this point he has shown that he intends to exercise his Fifth Amendment privilege; any statement taken after the person invokes his privilege cannot be other than the product of compulsion, subtle or otherwise. Without the right to <span class="star-pagination">*112</span> cut off questioning, the setting of in-custody interrogation operates on the individual to overcome free choice in producing a statement after the privilege has been once invoked."</blockquote>
<p>But the process of eroding <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, begun with <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971), continues with today's holding that police may renew the questioning of a suspect who has once exercised his right to remain silent, provided the suspect's right to cut off questioning has been "scrupulously honored." Today's distortion of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s constitutional principles can be viewed only as yet another step in the erosion and, I suppose, ultimate overruling of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s enforcement of the privilege against self-incrimination.</p>
<p>The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> guidelines were necessitated by the inherently coercive nature of in-custody questioning. As in <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964), "we sought a protective device to dispel the compelling atmosphere of the interrogation." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#465" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 465</a></span>. We "concluded that without proper safeguards the process of in-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual's will to resist and to compel him to speak where he would not otherwise do so freely." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 467</a></span>.<sup>[1]</sup> To assure safeguards that promised to dispel the "inherently compelling pressures" of in-custody interrogation, a prophylactic rule was fashioned to supplement the traditional determination of voluntariness on the facts of each case. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> held that any confession obtained when not preceded by the required warnings <span class="star-pagination">*113</span> or an adequate substitute safeguard was <i>per se</i> inadmissible in evidence. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#468" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 468-469, 479</a></span>. Satisfaction of this prophylactic rule, therefore, was necessary, though not sufficient, for the admission of a confession. Certiorari was expressly granted in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> "to give concrete constitutional guidelines for law enforcement agencies and courts to follow," <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#441" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 441-442</a></span>, that is, clear, objective standards that might be applied to avoid the vagaries of the traditional voluntariness test.</p>
<p>The task that confronts the Court in this case is to satisfy the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> approach by establishing "concrete constitutional guidelines" governing the resumption of questioning a suspect who, while in custody, has once clearly and unequivocally "indicate[d] . . . that he wishes to remain silent . . . ." As the Court today continues to recognize, under <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the cost of assuring voluntariness by procedural tests, independent of any actual inquiry into voluntariness, is that some voluntary statements will be excluded. <i>Ante,</i> at 99-100. Thus the consideration in the task confronting the Court is not whether voluntary statements will be excluded, but whether the procedures approved will be sufficient to assure with reasonable certainty that a confession is not obtained under the influence of the compulsion inherent in interrogation and detention. The procedures approved by the Court today fail to provide that assurance.</p>
<p>We observed in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>:</i> "Whatever the testimony of the authorities as to waiver of rights by an accused, the fact of lengthy interrogation or incommunicado incarceration before a statement is made is strong evidence that the accused did not validly waive his rights. In these circumstances the fact that the individual eventually made a statement is consistent with the conclusion that the compelling influence of the interrogation finally forced him to do so. It is inconsistent with any notion <span class="star-pagination">*114</span> of a voluntary relinquishment of the privilege." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#476" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 476</a></span>. And, as that portion of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> which the majority finds controlling observed, "the setting of in-custody interrogation operates on the individual to overcome free choice in producing a statement after the privilege has been once invoked." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 474</a></span>. Thus, as to statements which are the product of renewed questioning, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> established a virtually irrebuttable presumption of compulsion, see <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">id.,</a></span></i> at 474 n. 44, and that presumption stands strongest where, as in this case, a suspect, having initially determined to remain silent, is subsequently brought to confess his crime. Only by adequate procedural safeguards could the presumption be rebutted.</p>
<p>In formulating its procedural safeguard, the Court skirts the problem of compulsion and thereby fails to join issue with the dictates of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> The language which the Court finds controlling in this case teaches that renewed questioning itself is part of the process which invariably operates to overcome the will of a suspect. That teaching is embodied in the form of a proscription on any further questioning once the suspect has exercised his right to remain silent. Today's decision uncritically abandons that teaching. The Court assumes, contrary to the controlling language, that "scrupulously honoring" an initial exercise of the right to remain silent preserves the efficaciousness of initial and future warnings despite the fact that the suspect has once been subjected to interrogation and then has been detained for a lengthy period of time.</p>
<p>Observing that the suspect can control the circumstances of interrogation "[t]hrough the exercise of his option to terminate questioning," the Court concludes "that the admissibility of statements obtained after the person in custody has decided to remain silent depends . . . <span class="star-pagination">*115</span> on whether his `right to cut off questioning' was `scrupulously honored.' " <i>Ante,</i> at 103, 104. But scrupulously honoring exercises of the right to cut off questioning is only meaningful insofar as the suspect's will to exercise that right remains wholly unfettered. The Court's formulation thus assumes the very matter at issue here: whether renewed questioning following a lengthy period of detention acts to overbear the suspect's will, irrespective of giving the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings a second time (and scrupulously honoring them), thereby rendering inconsequential any failure to exercise the right to remain silent. For the Court it is enough conclusorily to assert that "[t]he subsequent questioning did not undercut Mosley's previous decision not to answer Detective Cowie's inquiries." <i>Ante,</i> at 105. Under <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> however, Mosley's failure to exercise the right upon renewed questioning is presumptively the consequence of an overbearing in which detention and that subsequent questioning played central roles.</p>
<p>I agree that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is not to be read, on the one hand, to impose an absolute ban on resumption of questioning "at any time or place on any subject," <i>ante,</i> at 102, or on the other hand, "to permit a resumption of interrogation after a momentary respite," <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">ibid.</a></span></i> But this surely cannot justify adoption of a vague and ineffective procedural standard that falls somewhere between those absurd extremes, for <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in flat and unambiguous terms requires that questioning "cease" when a suspect exercises the right to remain silent. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s terms, however, are not so uncompromising as to preclude the fashioning of guidelines to govern this case. Those guidelines must, of course, necessarily be sensitive to the reality that "[a]s a practical matter, the compulsion to speak in the isolated setting of the police station may well be greater than in courts or other official investigations, <span class="star-pagination">*116</span> where there are often impartial observers to guard against intimidation or trickery." 384 U. S. , at 461 (footnote omitted).</p>
<p>The fashioning of guidelines for this case is an easy task. Adequate procedures are readily available. Michigan law requires that the suspect be arraigned before a judicial officer "without unnecessary delay,"<sup>[2]</sup> certainly not a burdensome requirement. Alternatively, a requirement that resumption of questioning should await appointment and arrival of counsel for the suspect would be an acceptable and readily satisfied precondition to resumption.<sup>[3]</sup><i>Miranda</i> expressly held that "[t]he presence of counsel . . . would be the adequate protective device necessary to make the process of police interrogation conform to the dictates of the privilege [against self-incrimination]." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#466" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 466</a></span>. The Court expediently bypasses this alternative in its search for circumstances where renewed questioning would be permissible.<sup>[4]</sup></p>
<p>Indeed, language in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> suggests that the <span class="star-pagination">*117</span> presence of counsel is the only appropriate alternative. In categorical language we held in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>:</i> "If the individual indicates in any manner, at any time prior to or during questioning, that he wishes to remain silent, the interrogation must cease." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#473" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 473-474</a></span>. We then immediately observed:</p>
<blockquote>"If an individual indicates his desire to remain silent but has an attorney present, there <i>may</i> be some circumstances in which further questioning would be permissible. In the absence of evidence of overbearing, statements then made in the presence of counsel <i>might</i> be free of the compelling influence of the interrogation process and <i>might</i> fairly be construed as a waiver of the privilege for purposes of these statements." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span></i> at 474 n. 44 (emphasis added).</blockquote>
<p>This was the only circumstance in which we at all suggested that questioning could be resumed, and even then, further questioning was not permissible in all such circumstances, for compulsion was still the presumption not easily dissipated.<sup>[5]</sup></p>
<p><span class="star-pagination">*118</span> These procedures would be wholly consistent with the Court's rejection of a "<i>per se</i> proscription of indefinite duration," <i>ante,</i> at 102 a rejection to which I fully subscribe. Today's decision, however, virtually empties <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> of principle, for plainly the decision encourages police asked to cease interrogation to continue the suspect's detention until the police station's coercive atmosphere does its work and the suspect responds to resumed questioning.<sup>[6]</sup> Today's rejection of that reality of life contrasts sharply with the Court's acceptance only two years ago that "[i]n <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> the Court found that the techniques of police questioning and the nature of custodial surroundings produce an inherently coercive situation." <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#247" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 247</a></span> (1973). I can only conclude that today's decision signals rejection of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s basic premise.</p>
<p>My concern with the Court's opinion does not end with its treatment of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> but extends to its treatment of the facts in this case. The Court's effort to have the Williams homicide appear as "an unrelated holdup murder," <i>ante,</i> at 104, is patently unsuccessful. The anonymous tip received by Detective Cowie, conceded by the Court to be the sole basis for Mosley's arrest, <i>ante,</i> at 97 n. 1, embraced both the robberies covered in Cowie's interrogation <span class="star-pagination">*119</span> and the robbery-murder of Williams, <i>ante,</i> at 98 n. 2, about which Detective Hill questioned Mosley. Thus, when Mosley was apprehended, Cowie suspected him of being involved in the Williams robbery-murder in addition to the robberies about which he tried to examine Mosley. On another matter, the Court treats the second interrogation as being "at another location," <i>ante,</i> at 104. Yet the fact is that it was merely a different floor of the same building, <i>ante,</i> at 97-98.<sup>[7]</sup></p>
<p>I also find troubling the Court's finding that Mosley never indicated that he did not want to discuss the robbery-murder, see <i>ante,</i> at 104-106. I cannot read Cowie's testimony as the Court does. Cowie testified that Mosley <span class="star-pagination">*120</span> declined to answer " `[a]nything about the robberies,' " <i>ante,</i> at 105 n. 11. That can be read only against the background of the anonymous tip that implicated Mosley in the Williams incident. Read in that light, it may reasonably be inferred that Cowie understood "[a]nything" to include the Williams episode, since the anonymous tip embraced that episode. More than this, the Court's reading of Cowie's testimony is not even faithful to the standard it articulates here today. "Anything about the robberies" may more than reasonably be interpreted as comprehending the Williams murder which occurred during a robbery. To interpret Mosley's alleged statement to the contrary, therefore, hardly honors "scrupulously" the suspect's rights.</p>
<p>In light of today's erosion of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> standards as a matter of federal constitutional law, it is appropriate to observe that no State is precluded by the decision from adhering to higher standards under state law. Each State has power to impose higher standards governing police practices under state law than is required by the Federal Constitution. See <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#719" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714, 719</a></span> (1975);<sup>[8]</sup><i>Lego</i> v. <i>Twomey,</i> <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#489" aria-description="Citation for case: Lego v. Twomey">404 U. S. 477, 489</a></span> (1972); <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#62" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 62</a></span> (1967). A decision particularly bearing upon the question of the adoption of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> as state law is <i>Commonwealth</i> v. <i>Ware,</i> <span class="citation" data-id="9749246"><a href="/opinion/2281071/commonwealth-v-ware/" aria-description="Citation for case: Commonwealth v. Ware">446 Pa. 52</a></span>, <span class="citation" data-id="9749246"><a href="/opinion/2281071/commonwealth-v-ware/" aria-description="Citation for case: Commonwealth v. Ware">284 A. 2d 700</a></span> (1971). There the Pennsylvania Supreme Court adopted an aspect of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> as state law. This Court on March 20, <span class="star-pagination">*121</span> 1972, granted the Commonwealth's petition for certiorari to review that decision. <span class="citation multiple-matches"><a href="/c/U.%20S./405/987/">405 U. S. 987</a></span>. A month later, however, the error of the grant having been made apparent, the Court vacated the order of March 20, "it appearing that the judgment below rests upon an adequate state ground." <span class="citation multiple-matches"><a href="/c/U.%20S./406/910/">406 U. S. 910</a></span>. Understandably, state courts and legislatures are, as matters of state law, increasingly according protections once provided as federal rights but now increasingly depreciated by decisions of this Court. See, <i>e. g., </i><i>State</i> v. <i>Santiago,</i> <span class="citation" data-id="1166074"><a href="/opinion/1166074/state-v-santiago/" aria-description="Citation for case: State v. Santiago">53 Haw. 254</a></span>, <span class="citation" data-id="1166074"><a href="/opinion/1166074/state-v-santiago/" aria-description="Citation for case: State v. Santiago">492 P. 2d 657</a></span> (1971) (rejecting <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971)); <i>People</i> v. <i>Beavers,</i> <span class="citation" data-id="2041775"><a href="/opinion/2041775/people-v-beavers/" aria-description="Citation for case: People v. Beavers">393 Mich. 554</a></span>, <span class="citation" data-id="2041775"><a href="/opinion/2041775/people-v-beavers/" aria-description="Citation for case: People v. Beavers">227 N. W. 2d 511</a></span> (1975), cert. denied, <i>post,</i> p. 878 (rejecting <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/" aria-description="Citation for case: United States v. White">401 U. S. 745</a></span> (1971)); <i>State</i> v. <i>Johnson,</i> 68 N. J. 349, <span class="citation" data-id="9751378"><a href="/opinion/2301022/state-v-johnson/" aria-description="Citation for case: State v. Johnson">346 A. 2d 66</a></span> (1975) (rejecting <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973)); <i>Commonwealth</i> v. <i>Campana,</i> <span class="citation" data-id="6260900"><a href="/opinion/6390962/commonwealth-v-campana/" aria-description="Citation for case: Commonwealth v. Campana">455 Pa. 622</a></span>, <span class="citation" data-id="6260900"><a href="/opinion/6390962/commonwealth-v-campana/" aria-description="Citation for case: Commonwealth v. Campana">314 A. 2d 854</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./417/969/">417 U. S. 969</a></span> (1974) (adopting "same transaction or occurrence" view of Double Jeopardy Clause). I note that Michigan's Constitution has its own counterpart to the privilege against self-incrimination. Mich. Const., Art. 1, § 17; see <i>State</i> v. <i><span class="citation" data-id="9751378"><a href="/opinion/2301022/state-v-johnson/" aria-description="Citation for case: State v. Johnson">Johnson, supra</a></span></i><i>.</i></p>
<h2>NOTES</h2>
<p>[*]  <i>Frank Carrington, Fred E. Inbau, William K. Lambie,</i> and <i>Wayne W. Schmidt</i> filed a brief for Americans for Effective Law Enforcement, Inc., as <i>amicus curiae</i> urging reversal.</p>
<p>[1]  The officer testified that information supplied by an anonymous caller was the sole basis for his arrest of Mosley.</p>
<p>[2]  The original tip to Detective Cowie had, however, implicated Mosley in the Williams murder.</p>
<p>[3]  During cross-examination by Mosley's counsel at the evidentiary hearing, Detective Hill conceded that Smith in fact had not confessed but had "denied a physical participation in the robbery."</p>
<p>[4]  But see n. 5, <i>infra.</i></p>
<p>[5]  In addition to the claim that Detective Hill's questioning violated <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> Mosley contended that the statement was the product of an illegal arrest, that the statement was inadmissible because he had not been taken before a judicial officer without unnecessary delay, and that it had been obtained through trickery and promises of leniency. He argued that these circumstances, either independently or in combination, required the suppression of his incriminating statement.</p>
<p>[6]  The warnings must inform the person in custody "that he has a right to remain silent, that any statement he does make may be used as evidence against him, and that he has a right to the presence of an attorney, either retained or appointed." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444</a></span>.</p>
<p>[7]  The present case does not involve the procedures to be followed if the person in custody asks to consult with a lawyer, since Mosley made no such request at any time. Those procedures are detailed in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion as follows:
</p>
<p>"If the individual states that he wants an attorney, the interrogation must cease until an attorney is present. At that time, the individual must have an opportunity to confer with the attorney and to have him present during any subsequent questioning. If the individual cannot obtain an attorney and he indicates that he wants one before speaking to police, they must respect his decision to remain silent.</p>
<p>"This does not mean, as some have suggested, that each police station must have a `station house lawyer' present at all times to advise prisoners. It does mean, however, that if police propose to interrogate a person they must make known to him that he is entitled to a lawyer and that if he cannot afford one, a lawyer will be provided for him prior to any interrogation. If authorities conclude that they will not provide counsel during a reasonable period of time in which investigation in the field is carried out, they may refrain from doing so without violating the person's Fifth Amendment privilege so long as they do not question him during that time." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 474</a></span>.</p>
<p>[8]  The Court did state in a footnote:
</p>
<p>"If an individual indicates his desire to remain silent, but has an attorney present, there may be some circumstances in which further questioning would be permissible. In the absence of evidence of overbearing, statements then made in the presence of counsel might be free of the compelling influence of the interrogation process and might fairly be construed as a waiver of the privilege for purposes of these statements." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span></i> at 474 n. 44.</p>
<p>This footnote in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion is not relevant to the present case, since Mosley did not have an attorney present at the time he declined to answer Detective Cowie's questions, and the officer did not continue to question Mosley but instead ceased the interrogation in compliance with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s dictates.</p>
<p>[9]  It is instructive to note that the vast majority of federal and state courts presented with the issue have concluded that the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion does not create a <i>per se</i> proscription of any further interrogation once the person being questioned has indicated a desire to remain silent. See <i>Hill</i> v. <i>Whealon,</i> <span class="citation" data-id="316371"><a href="/opinion/316371/william-d-hill-v-w-j-whealon-superintendent-southern-ohio/#630" aria-description="Citation for case: William D. Hill v. W. J. Whealon, Superintendent,...">490 F. 2d 629, 630, 635</a></span> (CA6 1974); <i>United States</i> v. <i>Collins,</i> <span class="citation" data-id="9458357"><a href="/opinion/304272/united-states-v-ray-allen-collins/#802" aria-description="Citation for case: United States v. Ray Allen Collins">462 F. 2d 792, 802</a></span> (CA2 1972) (en banc); <i>Jennings</i> v. <i>United States,</i> <span class="citation" data-id="9453450"><a href="/opinion/279322/jacob-jennings-v-united-states/#515" aria-description="Citation for case: Jacob Jennings v. United States">391 F. 2d 512, 515-516</a></span> (CA5 1968); <i>United States</i> v. <i>Choice,</i> <span class="citation" data-id="1580188"><a href="/opinion/1580188/united-states-v-choice/#466" aria-description="Citation for case: United States v. Choice">392 F. Supp. 460, 466-467</a></span> (ED Pa. 1975); <i>McIntyre</i> v. <i>New York,</i> <span class="citation" data-id="2596192"><a href="/opinion/2596192/mcintyre-v-state-of-new-york/#13" aria-description="Citation for case: McIntyre v. State of New York">329 F. Supp. 9, 13-14</a></span> (EDNY 1971); <i>People</i> v. <i>Naranjo,</i> <span class="citation" data-id="1192799"><a href="/opinion/1192799/people-v-naranjo/#277" aria-description="Citation for case: People v. Naranjo">181 Colo. 273, 277-278</a></span>, <span class="citation" data-id="1192799"><a href="/opinion/1192799/people-v-naranjo/#1237" aria-description="Citation for case: People v. Naranjo">509 P. 2d 1235, 1237</a></span> (1973); <i>People</i> v. <i>Pittman,</i> <span class="citation" data-id="2007024"><a href="/opinion/2007024/people-v-pittman/#54" aria-description="Citation for case: People v. Pittman">55 Ill. 2d 39, 54-56</a></span>, <span class="citation" data-id="2007024"><a href="/opinion/2007024/people-v-pittman/#16" aria-description="Citation for case: People v. Pittman">302 N. E. 2d 7, 16-17</a></span> (1973); <i>State</i> v. <i>McClelland,</i> <span class="citation" data-id="9672961"><a href="/opinion/1720652/state-v-mcclelland/#192" aria-description="Citation for case: State v. McClelland">164 N. W. 2d 189, 192-196</a></span> (Iowa 1969); <i>State</i> v. <i>Law,</i> <span class="citation" data-id="1246504"><a href="/opinion/1246504/state-v-law/#647" aria-description="Citation for case: State v. Law">214 Kan. 643, 647-649</a></span>, <span class="citation" data-id="1246504"><a href="/opinion/1246504/state-v-law/#324" aria-description="Citation for case: State v. Law">522 P. 2d 320, 324-325</a></span> (1974); <i>Conway</i> v. <i>State,</i> <span class="citation" data-id="1958523"><a href="/opinion/1958523/conway-v-state/#405" aria-description="Citation for case: Conway v. State">7 Md. App. 400, 405-411</a></span>, <span class="citation" data-id="1958523"><a href="/opinion/1958523/conway-v-state/#181" aria-description="Citation for case: Conway v. State">256 A. 2d 178, 181-184</a></span> (1969); <i>State</i> v. <i>O'Neill,</i> <span class="citation" data-id="1270289"><a href="/opinion/1270289/state-v-oneill/#70" aria-description="Citation for case: State v. O&#x27;NEILL">299 Minn. 60, 70-71</a></span>, <span class="citation" data-id="1270289"><a href="/opinion/1270289/state-v-oneill/#829" aria-description="Citation for case: State v. O&#x27;NEILL">216 N. W. 2d 822, 829</a></span> (1974); <i>State</i> v. <i>Godfrey,</i> <span class="citation" data-id="1244888"><a href="/opinion/1244888/state-v-godfrey/#454" aria-description="Citation for case: State v. Godfrey">182 Neb. 451, 454-457</a></span>, <span class="citation" data-id="1244888"><a href="/opinion/1244888/state-v-godfrey/#440" aria-description="Citation for case: State v. Godfrey">155 N. W. 2d 438, 440-442</a></span> (1968); <i>People</i> v. <i>Gary,</i> 31 N. Y. 2d 68, 69-70, <span class="citation" data-id="5527700"><a href="/opinion/5679482/people-v-gary/#264" aria-description="Citation for case: People v. Gary">286 N. E. 2d 263, 264</a></span> (1972); <i>State</i> v. <i>Bishop,</i> <span class="citation" data-id="1203861"><a href="/opinion/1203861/state-v-bishop/#296" aria-description="Citation for case: State v. Bishop">272 N. C. 283, 296-297</a></span>, <span class="citation" data-id="1203861"><a href="/opinion/1203861/state-v-bishop/#520" aria-description="Citation for case: State v. Bishop">158 S. E. 2d 511, 520</a></span> (1968); <i>Commonwealth</i> v. <i>Grandison,</i> <span class="citation" data-id="2341485"><a href="/opinion/2341485/commonwealth-v-grandison/#233" aria-description="Citation for case: Commonwealth v. Grandison">449 Pa. 231, 233-234</a></span>, <span class="citation" data-id="2341485"><a href="/opinion/2341485/commonwealth-v-grandison/#731" aria-description="Citation for case: Commonwealth v. Grandison">296 A. 2d 730, 731</a></span> (1972); <i>State</i> v. <i>Robinson,</i> 87 S. D. 375, 378, <span class="citation" data-id="9661953"><a href="/opinion/1633109/state-v-robinson/#375" aria-description="Citation for case: State v. Robinson">209 N. W. 2d 374, 375-377</a></span> (1973); <i>Hill</i> v. <i>State,</i> <span class="citation" data-id="2455151"><a href="/opinion/2455151/hill-v-state/#486" aria-description="Citation for case: Hill v. State">429 S. W. 2d 481, 486-487</a></span> (Tex. Crim. App. 1968); <i>State</i> v. <i>Estrada,</i> <span class="citation" data-id="1837757"><a href="/opinion/1837757/state-v-estrada/#486" aria-description="Citation for case: State v. Estrada">63 Wis. 2d 476, 486-488</a></span>, <span class="citation" data-id="1837757"><a href="/opinion/1837757/state-v-estrada/#365" aria-description="Citation for case: State v. Estrada">217 N. W. 2d 359, 365-366</a></span> (1974). See also <i>People</i> v. <i>Fioritto,</i> <span class="citation" data-id="9550209"><a href="/opinion/1180572/people-v-fioritto/#717" aria-description="Citation for case: People v. Fioritto">68 Cal. 2d 714, 717-720</a></span>, <span class="citation" data-id="9550209"><a href="/opinion/1180572/people-v-fioritto/#626" aria-description="Citation for case: People v. Fioritto">441 P. 2d 625, 626-628</a></span> (1968) (permitting the suspect but not the police to initiate further questioning).
</p>
<p>Citation of the above cases does not imply a view of the merits of any particular decision.</p>
<p>[10]  The dissenting opinion asserts that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> established a requirement that once a person has indicated a desire to remain silent, questioning may be resumed only when counsel is present. <i>Post,</i> at 116-117. But clearly the Court in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> imposed no such requirement, for it distinguished between the procedural safeguards triggered by a request to remain silent and a request for an attorney and directed that "the interrogation must cease until an attorney is present" only "[i]f the individual states that he wants an attorney." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 474</a></span>.</p>
<p>[11]  Detective Cowie gave the only testimony at the suppression hearing concerning the scope of Mosley's earlier refusal to answer his questions:
</p>
<p>"A. I think at that time he declined to answer whether he had been involved.</p>
<p>"Q. He declined to answer?</p>
<p>"A. Yes. Anything about the robberies."</p>
<p>At the suppression hearing, Mosley did not in any way dispute Cowie's testimony. Not until trial, after the judge had denied the motion to suppress the incriminating statement, did Mosley offer a somewhat different version of his earlier refusal to answer Detective Cowie's questions. The briefs submitted by Mosley's counsel to the Michigan Court of Appeals and to this Court accepted Detective Cowie's account of the interrogation as correct, and the Michigan Court of Appeals decided the case on that factual premise. At oral argument before this Court, both counsel discussed the case solely in terms of Cowie's description of the events.</p>
<p>[1]  The majority's rule may cause an accused injury. Although a recently arrested individual may have indicated an initial desire not to answer questions, he would nonetheless want to know immediately if it were truethat his ability to explain a particular incriminating fact or to supply an alibi for a particular time period would result in his immediate release. Similarly, he might wish to knowif it were truethat (1) the case against him was unusually strong and that (2) his immediate cooperation with the authorities in the apprehension and conviction of others or in the recovery of property would redound to his benefit in the form of a reduced charge. Certainly the individual's lawyer, if he had one, would be interested in such information, even if communication of such information followed closely on an assertion of the "right to silence." Where the individual has not requested counsel and has chosen instead to make his own decisions regarding his conversations with the authorities, he should not be deprived even temporarily of any information relevant to the decision.</p>
<p>[2]  The question of the proper procedure following expression by an individual of his desire to consult counsel is not presented in this case. It is sufficient to note that the reasons to keep the lines of communication between the authorities and the accused open when the accused has chosen to make his own decisions are not present when he indicates instead that he wishes legal advice with respect thereto. The authorities may then communicate with him through an attorney. More to the point, the accused having expressed his own view that he is not competent to deal with the authorities without legal advice, a later decision at the authorities' insistence to make a statement without counsel's presence may properly be viewed with skepticism.</p>
<p>[1]  The Court said further:
</p>
<p>"Unless adequate protective devices are employed to dispel the compulsion inherent in custodial surroundings, no statement obtained from the defendant can truly be the product of his free choice." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 458</a></span>.</p>
<p>[2]  <span class="citation no-link">Mich. Comp. Laws §§ 764.13</span>, 764.26 (1970); Mich. Stat. Ann. §§ 28.871 (1), 28.885 (1972). Detective Cowie's testimony indicated that a judge was available across the street from the police station in which Mosley was held from 2:15 p.m. until 4 p.m. or 4:30 p. m. App. 13. The actual interrogation of Mosley, however, covered only 15 or 20 minutes of this time. <i>Id.,</i> at 14. The failure to comply with a simple state-law requirement in these circumstances is totally at odds with the holding that the police "scrupulously honored" Mosley's rights.</p>
<p>[3]  In addition, a break in custody for a substantial period of time would permitindeed it would requirelaw enforcement officers to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings a second time.</p>
<p>[4]  I do not mean to imply that counsel may be forced on a suspect who does not request an attorney. I suggest only that either arraignment or counsel must be provided before resumption of questioning to eliminate the coercive atmosphere of in-custody interrogation. The Court itself apparently proscribes resuming questioning until counsel is present if an accused has exercised the right to have an attorney present at questioning. <i>Ante,</i> at 101 n. 7.</p>
<p>[5]  The Court asserts that this language is not relevant to the present case, for "Mosley did not have an attorney present at the time he declined to answer Detective Cowie's questions." <i>Ante,</i> at 102 n. 8. The language, however, does not compel a reading that it is applicable only if counsel is present when the suspect initially exercises his right to remain silent. Even if it did, this would only indicate that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> placed even stiffer limits on the circumstances when questioning may be resumed than I suggest here. Moreover, since the concern in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was with assuring the absence of compulsion upon renewed questioning, it makes little difference whether counsel is initially present. Thus, even if the language does not specifically address the situation where counsel is not initially present, it certainly contemplates that situation.
</p>
<p>The Court also asserts that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> "directed that `the interrogation must cease until an attorney is present' only `[i]f the individual states that he wants an attorney.' " <i>Ante,</i> at 104 n. 10 (quoting <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 474</a></span>). This is patently inaccurate. The language from the quoted portion of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> actually reads: "If the individual states that he wants an attorney, the interrogation must cease until an attorney is present."</p>
<p>[6]  I do not suggest that the Court's opinion is to be read as permitting unreasonably lengthy detention without arraignment so long as any exercise of rights by a suspect is "scrupulously honored." The question of whether there is some constitutional limitation on the length of time police may detain a suspect without arraignment, cf. <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span> (1975); <i>Mallory</i> v. <i>United States,</i> <span class="citation" data-id="105545"><a href="/opinion/105545/mallory-v-united-states/" aria-description="Citation for case: Mallory v. United States">354 U. S. 449</a></span> (1957); <i>McNabb</i> v. <i>United States,</i> <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U. S. 332</a></span> (1943), is an open one and is not now before the Court.</p>
<p>[7]  See <i>Westover</i> v. <i>United States,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#494" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 494</a></span> (1966), where Westover confessed after being turned over to the FBI following questioning by local police. We said:
</p>
<p>"Although the two law enforcement authorities are legally distinct and the crimes for which they interrogated Westover were different, the impact on him was that of a continuous period of questioning. . . .</p>
<p>"We do not suggest that law enforcement authorities are precluded from questioning any individual who has been held for a period of time by other authorities and interrogated by them without appropriate warnings. A different case would be presented if an accused were taken into custody by the second authority, removed both in time and place from his original surroundings, and then adequately advised of his rights and given an opportunity to exercise them. But here the FBI interrogation was conducted immediately following the state interrogation in the same police stationin the same compelling surroundings. Thus, in obtaining a confession from Westover the federal authorities were the beneficiaries of the pressure applied by the local in-custody interrogation. In these circumstances the giving of warnings alone was not sufficient to protect the privilege." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#496" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 496-497</a></span>.</p>
<p>It is no answer to say that the questioning was resumed by a second police officer. Surely <i>Santobello</i> v. <i>New York,</i> <span class="citation" data-id="9424699"><a href="/opinion/108416/santobello-v-new-york/#262" aria-description="Citation for case: Santobello v. New York">404 U. S. 257, 262</a></span> (1971), requires that the case be decided as if it involved two interrogation sessions by a single law enforcement officer.</p>
<p>[8]  Although my Brother MARSHALL correctly argued in <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#728" aria-description="Citation for case: Oregon v. Hass">420 U. S., at 728</a></span> (dissenting), that we should have remanded for the state court to clarify whether it was relying on state or federal law, such a disposition is not required here. In <i><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">Hass</a></span></i> the state court cited both federal and state authority; in this case Mosley's counsel has conceded that the self-incrimination argument in the state court was based solely on the Fifth Amendment to the Federal Constitution. Tr. of Oral Arg. 44.</p>

</div>
```

---
