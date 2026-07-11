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

## GROUP: _overhaul2/lake/cases/Maryland v. King.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Maryland v. King"
type: case
citation: ""
parallel_cite: "133 S. Ct. 1958; 186 L. Ed. 2d 1; 569 U.S. 435; 24 Fla. L. Weekly Fed. S 234; 81 U.S.L.W. 4343"
neutral_cite: "2013 U.S. LEXIS 4165; 2013 WL 2371466"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2013
date_decided: 2013-06-03
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2013-06-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Maryland v. King
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/873669/maryland-v-king/"
  cluster_id: 873669
  opinion_id: 873669
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Investigative Genetic Genealogy]]"
    role: "Key — cross-ref (nearest DNA anchor)"
related: ["[[Schmerber v. California]]", "[[Florence v. Board of Chosen Freeholders]]", "[[Skinner v. Railway Labor Executives Association]]"]
aliases: []
tags: ["case", "fourth-amendment", "dna", "booking", "arrestee", "special-needs"]
holding: "Taking a buccal (cheek) DNA swab from a person arrested for a serious offense and held in custody is a reasonable booking procedure…"
lake:
  record_id: Maryland v. King
  status: verified
  projected_at: 2026-07-06
---

# Maryland v. King

*569 U.S. 435 (2013)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
King was arrested in Maryland on assault charges and, under the Maryland DNA Collection Act, a buccal (cheek) swab was taken from him during booking. The DNA profile matched evidence from an unsolved rape, and King was convicted of that crime. He argued that taking his DNA without a warrant or individualized suspicion violated the Fourth Amendment.

## Issue
Whether, under the Fourth Amendment, police may take and analyze a cheek swab of the DNA of a person arrested for a serious offense as part of routine booking.

## Rule
Yes. "When officers make an arrest supported by probable cause to hold for a serious offense and they bring the suspect to the station to be detained in custody, taking and analyzing a cheek swab of the arrestee's DNA is, like fingerprinting and photographing, a legitimate police booking procedure that is reasonable under the Fourth Amendment." — 569 U.S. at 465–466. ^pin-465

In the context of a valid arrest supported by probable cause, the arrestee's expectations of privacy are diminished and the brief cheek swab is a minimal intrusion outweighed by the State's substantial interest in identifying those in its custody.

## Application
King had been arrested on probable cause for a serious offense (assault) and was in custody at the station when the swab was taken. Weighed against his diminished privacy interest as an arrestee, the minor intrusion of a quick cheek swab was reasonable given the State's interest in accurately identifying him and informing decisions about his pretrial custody. Taking and analyzing his DNA was therefore a legitimate booking procedure, and the resulting match was admissible.

## Conclusion
Reversed: DNA cheek-swabbing of arrestees held for serious offenses is a reasonable booking procedure under the Fourth Amendment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *King* extends the diminished-privacy / reasonable-booking logic seen in [[Florence v. Board of Chosen Freeholders]] to DNA identification and remains the controlling authority on arrestee DNA collection.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*
- [[Investigative Genetic Genealogy]] — *Key — cross-ref (nearest DNA anchor)*

## Sources
- *Maryland v. King*, 569 U.S. 435 (2013) — https://www.courtlistener.com/opinion/873669/maryland-v-king/ — pinpoint: 465–466.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c0b2dc8e1b82bb8d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Maryland v. King"}, "payload": {"all": [{"cite": "133 S. Ct. 1958", "page": "1958", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "133"}, {"cite": "186 L. Ed. 2d 1", "page": "1", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "186"}, {"cite": "2013 U.S. LEXIS 4165", "page": "4165", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2013"}, {"cite": "569 U.S. 435", "page": "435", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "569"}, {"cite": "24 Fla. L. Weekly Fed. S 234", "page": "234", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "24"}, {"cite": "81 U.S.L.W. 4343", "page": "4343", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "81"}, {"cite": "2013 WL 2371466", "page": "2371466", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2013"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Maryland v. King"}}
{"assertion_id": "62452290a6307e27", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-465", "record_id": "Maryland v. King"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-465", "pinpoint_status": "slip-only", "quote": "--- # Maryland v. King *569 U.S. 435 (2013)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background King was arrested in Maryland on assault charges and, under the Maryland DNA Collection Act, a buccal (cheek) swab was taken from him during booking. The DNA profile matched evidence from an unsolved rape, and King was convicted of that crime. He argued that taking his DNA without a warrant or individualized suspicion violated the Fourth Amendment. ## Issue Whether, under the Fourth Amendment, police may take and analyze a cheek swab of the DNA of a person arrested for a serious offense as part of routine booking. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Maryland v. King", "star_marker": null}}
{"assertion_id": "ce45ff0fc55c3dca", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Maryland v. King"}, "payload": {"as_of_content": "2013-06-03", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Maryland v. King", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Maryland v. King

```json
{
  "schema_version": "s2.v1",
  "record_id": "Maryland v. King",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Maryland v. King",
    "case_name_short": "King",
    "case_name_full": "MARYLAND, Petitioner v. Alonzo Jay KING, Jr.",
    "input_case_name": "Maryland v. King",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2013-06-03",
    "year": 2013,
    "docket": null,
    "cluster_id": 873669,
    "lead_opinion_id": 873669,
    "sibling_ids": [
      873669
    ],
    "absolute_url": "/opinion/873669/maryland-v-king/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9240852,
        "score": 20,
        "case_name": "Maryland v. King"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "133 S. Ct. 1958",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "1958",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "186 L. Ed. 2d 1",
        "volume": "186",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "569 U.S. 435",
        "volume": "569",
        "reporter": "U.S.",
        "page": "435",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 234",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "234",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 U.S.L.W. 4343",
        "volume": "81",
        "reporter": "U.S.L.W.",
        "page": "4343",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2013 U.S. LEXIS 4165",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "4165",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 WL 2371466",
        "volume": "2013",
        "reporter": "WL",
        "page": "2371466",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "133 S. Ct. 1958",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "1958",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "186 L. Ed. 2d 1",
        "volume": "186",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 U.S. LEXIS 4165",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "4165",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "569 U.S. 435",
        "volume": "569",
        "reporter": "U.S.",
        "page": "435",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 234",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "234",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 U.S.L.W. 4343",
        "volume": "81",
        "reporter": "U.S.L.W.",
        "page": "4343",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 WL 2371466",
        "volume": "2013",
        "reporter": "WL",
        "page": "2371466",
        "type": 7,
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
      "id": "pin-465",
      "page": null,
      "quote": "--- # Maryland v. King *569 U.S. 435 (2013)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background King was arrested in Maryland on assault charges and, under the Maryland DNA Collection Act, a buccal (cheek) swab was taken from him during booking. The DNA profile matched evidence from an unsolved rape, and King was convicted of that crime. He argued that taking his DNA without a warrant or individualized suspicion violated the Fourth Amendment. ## Issue Whether, under the Fourth Amendment, police may take and analyze a cheek swab of the DNA of a person arrested for a serious offense as part of routine booking. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2013-06-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Maryland v. King",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Maryland v. King:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Alan William Null v. the State of Texas",
          "cluster_id": 6445822,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Strudwick",
          "cluster_id": 10018712,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Strudwick",
          "cluster_id": 5293509,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane1_negative"
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
        "journal_ref": "Maryland v. King:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Alfonzo Williams",
          "cluster_id": 4327223,
          "cite": [
            "842 F.3d 1143",
            "2016 U.S. App. LEXIS 21621",
            "2016 WL 7046754"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Ryan Mark Thompson",
          "cluster_id": 4311783,
          "cite": [
            "886 N.W.2d 224",
            "2016 Minn. LEXIS 656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Washington",
          "cluster_id": 6317368,
          "cite": [
            "53 Misc. 3d 572",
            "37 N.Y.S.3d 867"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane1_negative"
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
        "journal_ref": "Maryland v. King:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Lunden",
          "cluster_id": 2824187,
          "cite": [
            "87 Mass. App. Ct. 823"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Norton",
          "cluster_id": 2815787,
          "cite": [
            "443 Md. 517",
            "117 A.3d 1055",
            "2015 Md. LEXIS 482"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Valdez",
          "cluster_id": 4382347,
          "cite": [
            "2017 COA 41",
            "405 P.3d 413",
            "2017 WL 1279747",
            "2017 Colo. App. LEXIS 394"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jenkins v. State",
          "cluster_id": 5447023,
          "cite": [
            "493 S.W.3d 583",
            "2016 Tex. Crim. App. LEXIS 108",
            "2016 WL 3563879"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
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
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cregan",
          "cluster_id": 2681818,
          "cite": [
            "2014 IL 113600"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Quartavious Davis",
          "cluster_id": 2798570,
          "cite": [
            "785 F.3d 498",
            "2015 WL 2058977"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. William Robert Bernard, Jr.",
          "cluster_id": 2778772,
          "cite": [
            "859 N.W.2d 762",
            "2015 Minn. LEXIS 46",
            "2015 WL 543160"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hinkle v. Beckham County Board of County",
          "cluster_id": 4762695,
          "cite": [
            "962 F.3d 1204"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bailey",
          "cluster_id": 2654019,
          "cite": [
            "743 F.3d 322",
            "2014 WL 657932"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salmon v. Blesser",
          "cluster_id": 8442397,
          "cite": [
            "802 F.3d 249",
            "2015 WL 5254851"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Martinez",
          "cluster_id": 6243814,
          "cite": [
            "570 S.W.3d 278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Tench",
          "cluster_id": 7178800,
          "cite": [
            "123 N.E.3d 955",
            "156 Ohio St. 3d 85",
            "2018 Ohio 5205"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Paulo Lara",
          "cluster_id": 3182466,
          "cite": [
            "815 F.3d 605",
            "2016 U.S. App. LEXIS 3995",
            "2016 WL 828100"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ganias",
          "cluster_id": 3207604,
          "cite": [
            "824 F.3d 199",
            "117 A.F.T.R.2d (RIA) 1841",
            "2016 U.S. App. LEXIS 9706",
            "2016 WL 3031285"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anne Marie Gennusa v. Brian Canova",
          "cluster_id": 2669144,
          "cite": [
            "748 F.3d 1103",
            "2014 WL 1363541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leaders of Beautiful Struggle v. Baltimore Police Department",
          "cluster_id": 4894627,
          "cite": [
            "2 F.4th 330"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Simonson",
          "cluster_id": 4255842,
          "cite": [
            "148 A.3d 792",
            "2016 Pa. Super. 207",
            "2016 Pa. Super. LEXIS 527",
            "2016 WL 4743498"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reynaldo Castillo v. United States",
          "cluster_id": 3185536,
          "cite": [
            "816 F.3d 1300",
            "2016 U.S. App. LEXIS 4684",
            "2016 WL 1014220"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ganias",
          "cluster_id": 2678675,
          "cite": [
            "755 F.3d 125",
            "2014 WL 2722618",
            "115 A.F.T.R.2d (RIA) 1500",
            "2014 U.S. App. LEXIS 11222"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Williams",
          "cluster_id": 4637553,
          "cite": [
            "930 F.3d 44"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bain",
          "cluster_id": 4434458,
          "cite": [
            "874 F.3d 1",
            "2017 WL 4563821",
            "2017 U.S. App. LEXIS 20032"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Banks",
          "cluster_id": 3217553,
          "cite": [
            "146 A.3d 1",
            "321 Conn. 821",
            "2016 Conn. LEXIS 184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Yong Shik Won",
          "cluster_id": 3158283,
          "cite": [
            "137 Haw. 330",
            "372 P.3d 1065",
            "2015 Haw. LEXIS 352"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. King:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(873669) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDI0MTMxMjAwMDAwJnM9NDI2MzMyMyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28873669%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(873669)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMSZzPTQyNDkxMjcmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28873669%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(873669)",
        "reviewed": 45,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 45,
        "triage_read": 1,
        "triage_snippet_classified": 44
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(873669)",
    "indexed_citing_opinions": 301,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 873669,
        "count": 301,
        "count_source": "search"
      }
    ],
    "citation_count": 675,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/maryland-v-king.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3MTE0MDUmcz05NTQwODAwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28873669%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 873669,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 109592,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 110127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 111380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 111891,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 112220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 112384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 112464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 112585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 118100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 118277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 118405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 134746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 136990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 145640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 145860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 145887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 262430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 582564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 787362,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 856347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 1564887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 2303018,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 2342928,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 3579530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 873669,
        "cited_id": 4734292,
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
    "date_created": "2026-07-05T11:59:34Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:59:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:59:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T12:04:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:59:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Maryland v. King

```
(Slip Opinion)              OCTOBER TERM, 2012                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                           MARYLAND v. KING

     CERTIORARI TO THE COURT OF APPEALS OF MARYLAND

     No. 12–207.      Argued February 26, 2013—Decided June 3, 2013
After his 2009 arrest on first- and second-degree assault charges, re-
  spondent King was processed through a Wicomico County, Maryland,
  facility, where booking personnel used a cheek swab to take a DNA
  sample pursuant to the Maryland DNA Collection Act (Act). The
  swab was matched to an unsolved 2003 rape, and King was charged
  with that crime. He moved to suppress the DNA match, arguing that
  the Act violated the Fourth Amendment, but the Circuit Court Judge
  found the law constitutional. King was convicted of rape. The Mary-
  land Court of Appeals set aside the conviction, finding unconstitu-
  tional the portions of the Act authorizing DNA collection from felony
  arrestees.
Held: When officers make an arrest supported by probable cause to hold
 for a serious offense and bring the suspect to the station to be de-
 tained in custody, taking and analyzing a cheek swab of the ar-
 restee’s DNA is, like fingerprinting and photographing, a legitimate
 police booking procedure that is reasonable under the Fourth
 Amendment. Pp. 3–28.
    (a) DNA testing may “significantly improve both the criminal jus-
 tice system and police investigative practices,” District Attorney’s Of-
 fice for Third Judicial Dist. v. Osborne, 557 U. S. 52, 55, by making it
 “possible to determine whether a biological tissue matches a suspect
 with near certainty,” id., at 62. Maryland’s Act authorizes law en-
 forcement authorities to collect DNA samples from, as relevant here,
 persons charged with violent crimes, including first-degree assault.
 A sample may not be added to a database before an individual is ar-
 raigned, and it must be destroyed if, e.g., he is not convicted. Only
 identity information may be added to the database. Here, the officer
 collected a DNA sample using the common “buccal swab” procedure,
 which is quick and painless, requires no “surgical intrusio[n] beneath
2                           MARYLAND v. KING

                                   Syllabus

    the skin,” Winston v. Lee, 470 U. S. 753, 760, and poses no threat to
    the arrestee’s “health or safety,” id., at 763. Respondent’s identifica-
    tion as the rapist resulted in part through the operation of the Com-
    bined DNA Index System (CODIS), which connects DNA laboratories
    at the local, state, and national level, and which standardizes the
    points of comparison, i.e., loci, used in DNA analysis. Pp. 3–7.
       (b) The framework for deciding the issue presented is well estab-
    lished. Using a buccal swab inside a person’s cheek to obtain a DNA
    sample is a search under the Fourth Amendment. And the fact that
    the intrusion is negligible is of central relevance to determining
    whether the search is reasonable, “the ultimate measure of the con-
    stitutionality of a governmental search,” Vernonia School Dist. 47J v.
    Acton, 515 U. S. 646, 652. Because the need for a warrant is greatly
    diminished here, where the arrestee was already in valid police cus-
    tody for a serious offense supported by probable cause, the search is
    analyzed by reference to “reasonableness, not individualized suspi-
    cion,” Samson v. California, 547 U. S. 843, 855, n. 4, and reasonable-
    ness is determined by weighing “the promotion of legitimate govern-
    mental interests” against “the degree to which [the search] intrudes
    upon an individual’s privacy,” Wyoming v. Houghton, 526 U. S. 295,
    300. Pp. 7–10.
       (c) In this balance of reasonableness, great weight is given to both
    the significant government interest at stake in the identification of
    arrestees and DNA identification’s unmatched potential to serve that
    interest. Pp. 10–23.
          (1) The Act serves a well-established, legitimate government in-
    terest: the need of law enforcement officers in a safe and accurate
    way to process and identify persons and possessions taken into cus-
    tody. “[P]robable cause provides legal justification for arresting a
    [suspect], and for a brief period of detention to take the administra-
    tive steps incident to arrest,” Gerstein v. Pugh, 420 U. S. 103, 113–
    114; and the “validity of the search of a person incident to a lawful
    arrest” is settled, United States v. Robinson, 414 U. S. 218, 224. In-
    dividual suspicion is not necessary. The “routine administrative pro-
    cedure[s] at a police station house incident to booking and jailing the
    suspect” have different origins and different constitutional justifica-
    tions than, say, the search of a place not incident to arrest, Illinois v.
    Lafayette, 462 U. S. 640, 643, which depends on the “fair probability
    that contraband or evidence of a crime will be found in a particular
    place,” Illinois v. Gates, 462 U. S. 213, 238. And when probable cause
    exists to remove an individual from the normal channels of society
    and hold him in legal custody, DNA identification plays a critical role
    in serving those interests. First, the government has an interest in
    properly identifying “who has been arrested and who is being tried.”
                   Cite as: 569 U. S. ____ (2013)                     3

                              Syllabus

Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty., 542 U. S.
177, 191. Criminal history is critical to officers who are processing a
suspect for detention. They already seek identity information
through routine and accepted means: comparing booking photo-
graphs to sketch artists’ depictions, showing mugshots to potential
witnesses, and comparing fingerprints against electronic databases of
known criminals and unsolved crimes. The only difference between
DNA analysis and fingerprint databases is the unparalleled accuracy
DNA provides. DNA is another metric of identification used to con-
nect the arrestee with his or her public persona, as reflected in rec-
ords of his or her actions that are available to the police. Second, of-
ficers must ensure that the custody of an arrestee does not create
inordinate “risks for facility staff, for the existing detainee popula-
tion, and for a new detainee.” Florence v. Board of Chosen Freehold-
ers of County of Burlington, 566 U. S. ___, ___. DNA allows officers to
know the type of person being detained. Third, “the Government has
a substantial interest in ensuring that persons accused of crimes are
available for trials.” Bell v. Wolfish, 441 U. S. 520, 534. An arrestee
may be more inclined to flee if he thinks that continued contact with
the criminal justice system may expose another serious offense.
Fourth, an arrestee’s past conduct is essential to assessing the dan-
ger he poses to the public, which will inform a court’s bail determina-
tion. Knowing that the defendant is wanted for a previous violent
crime based on DNA identification may be especially probative in this
regard. Finally, in the interests of justice, identifying an arrestee as
the perpetrator of some heinous crime may have the salutary effect of
freeing a person wrongfully imprisoned. Pp. 10–18.
     (2) DNA identification is an important advance in the techniques
long used by law enforcement to serve legitimate police concerns. Po-
lice routinely have used scientific advancements as standard proce-
dures for identifying arrestees. Fingerprinting, perhaps the most di-
rect historical analogue to DNA technology, has, from its advent,
been viewed as a natural part of “the administrative steps incident to
arrest.” County of Riverside v. McLaughlin, 500 U. S. 44, 58. How-
ever, DNA identification is far superior. The additional intrusion up-
on the arrestee’s privacy beyond that associated with fingerprinting
is not significant, and DNA identification is markedly more accurate.
It may not be as fast as fingerprinting, but rapid fingerprint analysis
is itself of recent vintage, and the question of how long it takes to
process identifying information goes to the efficacy of the search for
its purpose of prompt identification, not the constitutionality of the
search. Rapid technical advances are also reducing DNA processing
times. Pp. 18–23.
   (d) The government interest is not outweighed by respondent’s pri-
4                          MARYLAND v. KING

                                  Syllabus

    vacy interests. Pp. 23–28.
         (1) By comparison to the substantial government interest and the
    unique effectiveness of DNA identification, the intrusion of a cheek
    swab to obtain a DNA sample is minimal. Reasonableness must be
    considered in the context of an individual’s legitimate privacy expec-
    tations, which necessarily diminish when he is taken into police cus-
    tody. Bell, supra, at 557. Such searches thus differ from the so-
    called special needs searches of, e.g., otherwise law-abiding motorists
    at checkpoints. See Indianapolis v. Edmond, 531 U. S. 32. The rea-
    sonableness inquiry considers two other circumstances in which par-
    ticularized suspicion is not categorically required: “diminished expec-
    tations of privacy [and a] minimal intrusion.” Illinois v. McArthur,
    531 U. S. 326, 330. An invasive surgery may raise privacy concerns
    weighty enough for the search to require a warrant, notwithstanding
    the arrestee’s diminished privacy expectations, but a buccal swab,
    which involves a brief and minimal intrusion with “virtually no risk,
    trauma, or pain,” Schmerber v. California, 384 U. S. 757, 771, does
    not increase the indignity already attendant to normal incidents of
    arrest. Pp. 23–26.
         (2) The processing of respondent’s DNA sample’s CODIS loci also
    did not intrude on his privacy in a way that would make his DNA
    identification unconstitutional. Those loci came from noncoding DNA
    parts that do not reveal an arrestee’s genetic traits and are unlikely
    to reveal any private medical information. Even if they could provide
    such information, they are not in fact tested for that end. Finally, the
    Act provides statutory protections to guard against such invasions of
    privacy. Pp. 26–28.
425 Md. 550, 42 A. 3d 549, reversed.

   KENNEDY, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and THOMAS, BREYER, and ALITO, JJ., joined. SCALIA, J., filed a
dissenting opinion, in which GINSBURG, SOTOMAYOR, and KAGAN, JJ.,
joined.
                       Cite as: 569 U. S. ____ (2013)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash­
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 12–207
                                  _________________


 MARYLAND, PETITIONER v. ALONZO JAY KING, JR.
  ON WRIT OF CERTIORARI TO THE COURT OF APPEALS OF 

                     MARYLAND

                                [June 3, 2013]


   JUSTICE KENNEDY delivered the opinion of the Court.
   In 2003 a man concealing his face and armed with a gun
broke into a woman’s home in Salisbury, Maryland. He
raped her. The police were unable to identify or appre­
hend the assailant based on any detailed description or
other evidence they then had, but they did obtain from the
victim a sample of the perpetrator’s DNA.
   In 2009 Alonzo King was arrested in Wicomico County,
Maryland, and charged with first- and second-degree
assault for menacing a group of people with a shotgun. As
part of a routine booking procedure for serious offenses,
his DNA sample was taken by applying a cotton swab or
filter paper—known as a buccal swab—to the inside of his
cheeks. The DNA was found to match the DNA taken
from the Salisbury rape victim. King was tried and con­
victed for the rape. Additional DNA samples were taken
from him and used in the rape trial, but there seems to be
no doubt that it was the DNA from the cheek sample
taken at the time he was booked in 2009 that led to his
first having been linked to the rape and charged with its
commission.
   The Court of Appeals of Maryland, on review of King’s
2                   MARYLAND v. KING

                    Opinion of the Court

rape conviction, ruled that the DNA taken when King was
booked for the 2009 charge was an unlawful seizure be­
cause obtaining and using the cheek swab was an unrea­
sonable search of the person. It set the rape conviction
aside. This Court granted certiorari and now reverses the
judgment of the Maryland court.
                             I
   When King was arrested on April 10, 2009, for menac­
ing a group of people with a shotgun and charged in state
court with both first- and second-degree assault, he was
processed for detention in custody at the Wicomico County
Central Booking facility. Booking personnel used a cheek
swab to take the DNA sample from him pursuant to provi­
sions of the Maryland DNA Collection Act (or Act).
   On July 13, 2009, King’s DNA record was uploaded to
the Maryland DNA database, and three weeks later, on
August 4, 2009, his DNA profile was matched to the DNA
sample collected in the unsolved 2003 rape case. Once the
DNA was matched to King, detectives presented the foren­
sic evidence to a grand jury, which indicted him for the
rape. Detectives obtained a search warrant and took a
second sample of DNA from King, which again matched
the evidence from the rape. He moved to suppress the
DNA match on the grounds that Maryland’s DNA collec­
tion law violated the Fourth Amendment. The Circuit
Court Judge upheld the statute as constitutional. King
pleaded not guilty to the rape charges but was convicted
and sentenced to life in prison without the possibility of
parole.
   In a divided opinion, the Maryland Court of Appeals
struck down the portions of the Act authorizing collection
of DNA from felony arrestees as unconstitutional. The
majority concluded that a DNA swab was an unreasonable
search in violation of the Fourth Amendment because
King’s “expectation of privacy is greater than the State’s
                 Cite as: 569 U. S. ____ (2013)            3

                     Opinion of the Court

purported interest in using King’s DNA to identify him.”
425 Md. 550, 561, 42 A. 3d 549, 556 (2012). In reach-
ing that conclusion the Maryland Court relied on the deci­
sions of various other courts that have concluded that
DNA identification of arrestees is impermissible. See, e.g.,
People v. Buza, 129 Cal. Rptr. 3d 753 (App. 2011) (offi­
cially depublished); Mario W. v. Kaipio, 228 Ariz. 207,
265 P. 3d 389 (App. 2011).
   Both federal and state courts have reached differing
conclusions as to whether the Fourth Amendment prohib­
its the collection and analysis of a DNA sample from
persons arrested, but not yet convicted, on felony charges.
This Court granted certiorari, 568 U. S. ___ (2012), to
address the question. King is the respondent here.
                              II
   The advent of DNA technology is one of the most signifi­
cant scientific advancements of our era. The full potential
for use of genetic markers in medicine and science is still
being explored, but the utility of DNA identification in the
criminal justice system is already undisputed. Since the
first use of forensic DNA analysis to catch a rapist and
murderer in England in 1986, see J. Butler, Fundamentals
of Forensic DNA Typing 5 (2009) (hereinafter Butler), law
enforcement, the defense bar, and the courts have
acknowledged DNA testing’s “unparalleled ability both to
exonerate the wrongly convicted and to identify the guilty.
It has the potential to significantly improve both the
criminal justice system and police investigative practices.”
District Attorney’s Office for Third Judicial Dist. v. Os-
borne, 557 U. S. 52, 55 (2009).
                             A
   The current standard for forensic DNA testing relies on
an analysis of the chromosomes located within the nucleus
of all human cells. “The DNA material in chromosomes is
4                    MARYLAND v. KING

                     Opinion of the Court

composed of ‘coding’ and ‘noncoding’ regions. The coding
regions are known as genes and contain the information
necessary for a cell to make proteins. . . . Non-protein­
coding regions . . . are not related directly to making pro­
teins, [and] have been referred to as ‘junk’ DNA.” Butler
25. The adjective “junk” may mislead the layperson, for
in fact this is the DNA region used with near certainty to
identify a person. The term apparently is intended to
indicate that this particular noncoding region, while use­
ful and even dispositive for purposes like identity, does not
show more far-reaching and complex characteristics like
genetic traits.
   Many of the patterns found in DNA are shared among
all people, so forensic analysis focuses on “repeated DNA
sequences scattered throughout the human genome,”
known as “short tandem repeats” (STRs). Id., at 147–148.
The alternative possibilities for the size and frequency of
these STRs at any given point along a strand of DNA are
known as “alleles,” id., at 25; and multiple alleles are
analyzed in order to ensure that a DNA profile matches
only one individual. Future refinements may improve pres-
ent technology, but even now STR analysis makes it
 “possible to determine whether a biological tissue match­
es a suspect with near certainty.” Osborne, supra, at 62.
   The Act authorizes Maryland law enforcement author­
ities to collect DNA samples from “an individual who is
charged with . . . a crime of violence or an attempt to
commit a crime of violence; or . . . burglary or an attempt
to commit burglary.” Md. Pub. Saf. Code Ann. §2–
504(a)(3)(i) (Lexis 2011). Maryland law defines a crime of
violence to include murder, rape, first-degree assault,
kidnaping, arson, sexual assault, and a variety of other
serious crimes. Md. Crim. Law Code Ann. §14–101 (Lexis
2012). Once taken, a DNA sample may not be processed
or placed in a database before the individual is arraigned
(unless the individual consents). Md. Pub. Saf. Code Ann.
                  Cite as: 569 U. S. ____ (2013)            5

                      Opinion of the Court

§2–504(d)(1) (Lexis 2011). It is at this point that a judicial
officer ensures that there is probable cause to detain the
arrestee on a qualifying serious offense. If “all qualifying
criminal charges are determined to be unsupported by
probable cause . . . the DNA sample shall be immediately
destroyed.” §2–504(d)(2)(i). DNA samples are also de­
stroyed if “a criminal action begun against the individual
. . . does not result in a conviction,” “the conviction is
finally reversed or vacated and no new trial is permitted,”
or “the individual is granted an unconditional pardon.”
§2–511(a)(1).
    The Act also limits the information added to a DNA
database and how it may be used. Specifically, “[o]nly
DNA records that directly relate to the identification of
individuals shall be collected and stored.” §2–505(b)(1).
No purpose other than identification is permissible: “A
person may not willfully test a DNA sample for infor­
mation that does not relate to the identification of indi­
viduals as specified in this subtitle.” §2–512(c). Tests for
familial matches are also prohibited. See §2–506(d) (“A
person may not perform a search of the statewide DNA
data base for the purpose of identification of an offender
in connection with a crime for which the offender may be
a biological relative of the individual from whom the DNA
sample was acquired”). The officers involved in taking
and analyzing respondent’s DNA sample complied with
the Act in all respects.
    Respondent’s DNA was collected in this case using a
common procedure known as a “buccal swab.” “Buccal cell
collection involves wiping a small piece of filter paper or a
cotton swab similar to a Q-tip against the inside cheek of
an individual’s mouth to collect some skin cells.” Butler
86. The procedure is quick and painless. The swab touches
inside an arrestee’s mouth, but it requires no “surgical
intrusio[n] beneath the skin,” Winston v. Lee, 470 U. S.
753, 760 (1985), and it poses no “threa[t] to the health or
6                     MARYLAND v. KING

                       Opinion of the Court

safety” of arrestees, id., at 763.
                             B
   Respondent’s identification as the rapist resulted in part
through the operation of a national project to standardize
collection and storage of DNA profiles. Authorized by
Congress and supervised by the Federal Bureau of Inves­
tigation, the Combined DNA Index System (CODIS) con­
nects DNA laboratories at the local, state, and national
level. Since its authorization in 1994, the CODIS system
has grown to include all 50 States and a number of federal
agencies. CODIS collects DNA profiles provided by local
laboratories taken from arrestees, convicted offenders, and
forensic evidence found at crime scenes. To participate
in CODIS, a local laboratory must sign a memorandum of
understanding agreeing to adhere to quality standards
and submit to audits to evaluate compliance with the
federal standards for scientifically rigorous DNA testing.
Butler 270.
   One of the most significant aspects of CODIS is the
standardization of the points of comparison in DNA analy­
sis. The CODIS database is based on 13 loci at which
the STR alleles are noted and compared. These loci make
possible extreme accuracy in matching individual samples,
with a “random match probability of approximately 1 in
100 trillion (assuming unrelated individuals).” Ibid. The
CODIS loci are from the non-protein coding junk regions
of DNA, and “are not known to have any association
with a genetic disease or any other genetic predisposition.
Thus, the information in the database is only useful for
human identity testing.” Id., at 279. STR information
is recorded only as a “string of numbers”; and the DNA
identification is accompanied only by information denoting
the laboratory and the analyst responsible for the submis­
sion. Id., at 270. In short, CODIS sets uniform national
standards for DNA matching and then facilitates connec­
                 Cite as: 569 U. S. ____ (2013)           7

                     Opinion of the Court

tions between local law enforcement agencies who can
share more specific information about matched STR
profiles.
   All 50 States require the collection of DNA from felony
convicts, and respondent does not dispute the validity of
that practice. See Brief for Respondent 48. Twenty-eight
States and the Federal Government have adopted laws
similar to the Maryland Act authorizing the collection of
DNA from some or all arrestees. See Brief for State of
California et al. as Amici Curiae 4, n. 1 (States Brief)
(collecting state statutes). Although those statutes vary
in their particulars, such as what charges require a DNA
sample, their similarity means that this case implicates
more than the specific Maryland law. At issue is a stand­
ard, expanding technology already in widespread use
throughout the Nation.
                             III

                              A

   Although the DNA swab procedure used here presents a
question the Court has not yet addressed, the framework
for deciding the issue is well established. The Fourth
Amendment, binding on the States by the Fourteenth
Amendment, provides that “[t]he right of the people to
be secure in their persons, houses, papers, and effects,
against unreasonable searches and seizures, shall not be
violated.” It can be agreed that using a buccal swab on the
inner tissues of a person’s cheek in order to obtain DNA
samples is a search. Virtually any “intrusio[n] into the
human body,” Schmerber v. California, 384 U. S. 757, 770
(1966), will work an invasion of “ ‘cherished personal secu­
rity’ that is subject to constitutional scrutiny,” Cupp v.
Murphy, 412 U. S. 291, 295 (1973) (quoting Terry v. Ohio,
392 U. S. 1, 24–25 (1968)). The Court has applied the
Fourth Amendment to police efforts to draw blood, see
Schmerber, supra; Missouri v. McNeely, 569 U. S. ___
8                   MARYLAND v. KING

                     Opinion of the Court

(2013), scraping an arrestee’s fingernails to obtain trace
evidence, see Cupp, supra, and even to “a breathalyzer
test, which generally requires the production of alveolar
or ‘deep lung’ breath for chemical analysis,” Skinner v.
Railway Labor Executives’ Assn., 489 U. S. 602, 616
(1989).
   A buccal swab is a far more gentle process than a veni­
puncture to draw blood. It involves but a light touch on
the inside of the cheek; and although it can be deemed
a search within the body of the arrestee, it requires no
“surgical intrusions beneath the skin.” Winston, 470 U. S.,
at 760. The fact than an intrusion is negligible is of cen­
tral relevance to determining reasonableness, although it
is still a search as the law defines that term.
                              B
   To say that the Fourth Amendment applies here is the
beginning point, not the end of the analysis. “[T]he Fourth
Amendment’s proper function is to constrain, not against
all intrusions as such, but against intrusions which are
not justified in the circumstances, or which are made in an
improper manner.” Schmerber, supra, at 768. “As the text
of the Fourth Amendment indicates, the ultimate measure
of the constitutionality of a governmental search is ‘rea­
sonableness.’ ” Vernonia School Dist. 47J v. Acton, 515
U. S. 646, 652 (1995). In giving content to the inquiry
whether an intrusion is reasonable, the Court has pre­
ferred “some quantum of individualized suspicion . . . [as]
a prerequisite to a constitutional search or seizure. But
the Fourth Amendment imposes no irreducible require­
ment of such suspicion.” United States v. Martinez-Fuerte,
428 U. S. 543, 560–561 (1976) (citation and footnote
omitted).
   In some circumstances, such as “[w]hen faced with
special law enforcement needs, diminished expectations of
privacy, minimal intrusions, or the like, the Court has
                  Cite as: 569 U. S. ____ (2013)            9

                      Opinion of the Court

found that certain general, or individual, circumstances
may render a warrantless search or seizure reasonable.”
Illinois v. McArthur, 531 U. S. 326, 330 (2001). Those
circumstances diminish the need for a warrant, either
because “the public interest is such that neither a warrant
nor probable cause is required,” Maryland v. Buie, 494
U. S. 325, 331 (1990), or because an individual is already
on notice, for instance because of his employment, see
Skinner, supra, or the conditions of his release from gov­
ernment custody, see Samson v. California, 547 U. S. 843
(2006), that some reasonable police intrusion on his pri­
vacy is to be expected. The need for a warrant is perhaps
least when the search involves no discretion that could
properly be limited by the “interpo[lation of] a neutral
magistrate between the citizen and the law enforcement
officer.” Treasury Employees v. Von Raab, 489 U. S. 656,
667 (1989).
   The instant case can be addressed with this background.
The Maryland DNA Collection Act provides that, in order
to obtain a DNA sample, all arrestees charged with seri­
ous crimes must furnish the sample on a buccal swab
applied, as noted, to the inside of the cheeks. The arrestee
is already in valid police custody for a serious offense
supported by probable cause. The DNA collection is not
subject to the judgment of officers whose perspective
might be “colored by their primary involvement in ‘the
often competitive enterprise of ferreting out crime.’ ” Terry,
supra, at 12 (quoting Johnson v. United States, 333 U. S.
10, 14 (1948)). As noted by this Court in a different
but still instructive context involving blood testing, “[b]oth
the circumstances justifying toxicological testing and the
permissible limits of such intrusions are defined nar-
rowly and specifically in the regulations that authorize
them . . . . Indeed, in light of the standardized nature of
the tests and the minimal discretion vested in those
charged with administering the program, there are virtu­
10                   MARYLAND v. KING

                     Opinion of the Court

ally no facts for a neutral magistrate to evaluate.” Skin-
ner, supra, at 622. Here, the search effected by the buccal
swab of respondent falls within the category of cases
this Court has analyzed by reference to the proposition
that the “touchstone of the Fourth Amendment is reason­
ableness, not individualized suspicion.” Samson, supra, at
855, n. 4.
   Even if a warrant is not required, a search is not beyond
Fourth Amendment scrutiny; for it must be reasonable in
its scope and manner of execution. Urgent government
interests are not a license for indiscriminate police behav­
ior. To say that no warrant is required is merely to
acknowledge that “rather than employing a per se rule of
unreasonableness, we balance the privacy-related and law
enforcement-related concerns to determine if the intrusion
was reasonable.” McArthur, supra, at 331. This applica­
tion of “traditional standards of reasonableness” requires a
court to weigh “the promotion of legitimate governmen­
tal interests” against “the degree to which [the search]
intrudes upon an individual’s privacy.” Wyoming v. Hough-
ton, 526 U. S. 295, 300 (1999). An assessment of reasona­
bleness to determine the lawfulness of requiring this class
of arrestees to provide a DNA sample is central to the
instant case.
                            IV 

                             A

  The legitimate government interest served by the Mary­
land DNA Collection Act is one that is well established:
the need for law enforcement officers in a safe and accu­
rate way to process and identify the persons and posses­
sions they must take into custody. It is beyond dispute
that “probable cause provides legal justification for arrest­
ing a person suspected of crime, and for a brief period of
detention to take the administrative steps incident to
arrest.” Gerstein v. Pugh, 420 U. S. 103, 113–114 (1975).
                 Cite as: 569 U. S. ____ (2013)           11

                     Opinion of the Court

Also uncontested is the “right on the part of the Govern­
ment, always recognized under English and American law,
to search the person of the accused when legally arrested.”
Weeks v. United States, 232 U. S. 383, 392 (1914), over­
ruled on other grounds, Mapp v. Ohio, 367 U. S. 643
(1961). “The validity of the search of a person incident to
a lawful arrest has been regarded as settled from its
first enunciation, and has remained virtually unchallenged.”
United States v. Robinson, 414 U. S. 218, 224 (1973).
Even in that context, the Court has been clear that indi­
vidual suspicion is not necessary, because “[t]he constitu­
tionality of a search incident to an arrest does not depend
on whether there is any indication that the person ar­
rested possesses weapons or evidence. The fact of a lawful
arrest, standing alone, authorizes a search.” Michigan v.
DeFillippo, 443 U. S. 31, 35 (1979).
   The “routine administrative procedure[s] at a police sta­
tion house incident to booking and jailing the suspect”
derive from different origins and have different constitu­
tional justifications than, say, the search of a place, Illi-
nois v. Lafayette, 462 U. S. 640, 643 (1983); for the search
of a place not incident to an arrest depends on the “fair
probability that contraband or evidence of a crime will be
found in a particular place,” Illinois v. Gates, 462 U. S.
213, 238 (1983). The interests are further different when
an individual is formally processed into police custody.
Then “the law is in the act of subjecting the body of the
accused to its physical dominion.” People v. Chiagles, 237
N. Y. 193, 197, 142 N. E. 583, 584 (1923) (Cardozo, J.).
When probable cause exists to remove an individual from
the normal channels of society and hold him in legal cus­
tody, DNA identification plays a critical role in serving
those interests.
   First, “[i]n every criminal case, it is known and must be
known who has been arrested and who is being tried.”
Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt
12                   MARYLAND v. KING

                      Opinion of the Court

Cty., 542 U. S. 177, 191 (2004). An individual’s identity is
more than just his name or Social Security number, and
the government’s interest in identification goes beyond
ensuring that the proper name is typed on the indictment.
Identity has never been considered limited to the name on
the arrestee’s birth certificate. In fact, a name is of little
value compared to the real interest in identification at
stake when an individual is brought into custody. “It is
a well recognized aspect of criminal conduct that the per­
petrator will take unusual steps to conceal not only his
conduct, but also his identity. Disguises used while com­
mitting a crime may be supplemented or replaced by
changed names, and even changed physical features.”
Jones v. Murray, 962 F. 2d 302, 307 (CA4 1992). An “ar­
restee may be carrying a false ID or lie about his identity,”
and “criminal history records . . . can be inaccurate or
incomplete.” Florence v. Board of Chosen Freeholders of
County of Burlington, 566 U. S. ___, ___ (2012) (slip op.,
at 16).
   A suspect’s criminal history is a critical part of his iden­
tity that officers should know when processing him for
detention. It is a common occurrence that “[p]eople de­
tained for minor offenses can turn out to be the most
devious and dangerous criminals. Hours after the Okla­
homa City bombing, Timothy McVeigh was stopped by a
state trooper who noticed he was driving without a license
plate. Police stopped serial killer Joel Rifkin for the same
reason. One of the terrorists involved in the September 11
attacks was stopped and ticketed for speeding just two
days before hijacking Flight 93.” Id., at ___ (slip op., at
14) (citations omitted). Police already seek this crucial
identifying information. They use routine and accepted
means as varied as comparing the suspect’s booking pho­
tograph to sketch artists’ depictions of persons of interest,
showing his mugshot to potential witnesses, and of course
making a computerized comparison of the arrestee’s fin­
                 Cite as: 569 U. S. ____ (2013)           13

                     Opinion of the Court

gerprints against electronic databases of known criminals
and unsolved crimes. In this respect the only difference
between DNA analysis and the accepted use of fingerprint
databases is the unparalleled accuracy DNA provides.
   The task of identification necessarily entails searching
public and police records based on the identifying infor­
mation provided by the arrestee to see what is already
known about him. The DNA collected from arrestees is
an irrefutable identification of the person from whom it
was taken. Like a fingerprint, the 13 CODIS loci are not
themselves evidence of any particular crime, in the way
that a drug test can by itself be evidence of illegal narcot­
ics use. A DNA profile is useful to the police because it
gives them a form of identification to search the records
already in their valid possession. In this respect the use of
DNA for identification is no different than matching an
arrestee’s face to a wanted poster of a previously unidenti­
fied suspect; or matching tattoos to known gang symbols
to reveal a criminal affiliation; or matching the arrestee’s
fingerprints to those recovered from a crime scene. See
Tr. of Oral Arg. 19. DNA is another metric of identifica­
tion used to connect the arrestee with his or her public
persona, as reflected in records of his or her actions that
are available to the police. Those records may be linked to
the arrestee by a variety of relevant forms of identifica­
tion, including name, alias, date and time of previous
convictions and the name then used, photograph, Social
Security number, or CODIS profile. These data, found in
official records, are checked as a routine matter to produce
a more comprehensive record of the suspect’s complete
identity. Finding occurrences of the arrestee’s CODIS
profile in outstanding cases is consistent with this com­
mon practice. It uses a different form of identification
than a name or fingerprint, but its function is the same.
   Second, law enforcement officers bear a responsibility
for ensuring that the custody of an arrestee does not cre­
14                   MARYLAND v. KING

                     Opinion of the Court

ate inordinate “risks for facility staff, for the existing
detainee population, and for a new detainee.” Florence,
supra, at ___ (slip op., at 10). DNA identification can
provide untainted information to those charged with de­
taining suspects and detaining the property of any felon.
For these purposes officers must know the type of person
whom they are detaining, and DNA allows them to make
critical choices about how to proceed.
     “Knowledge of identity may inform an officer that a
     suspect is wanted for another offense, or has a record
     of violence or mental disorder. On the other hand,
     knowing identity may help clear a suspect and al­
     low the police to concentrate their efforts elsewhere.
     Identity may prove particularly important in [certain
     cases, such as] where the police are investigating
     what appears to be a domestic assault. Officers called
     to investigate domestic disputes need to know whom
     they are dealing with in order to assess the situation,
     the threat to their own safety, and possible danger to
     the potential victim.” Hiibel, supra, at 186.
Recognizing that a name alone cannot address this inter­
est in identity, the Court has approved, for example, “a
visual inspection for certain tattoos and other signs of
gang affiliation as part of the intake process,” because
“[t]he identification and isolation of gang members before
they are admitted protects everyone.” Florence, supra, at
___ (slip op., at 11).
   Third, looking forward to future stages of criminal
prosecution, “the Government has a substantial interest in
ensuring that persons accused of crimes are available for
trials.” Bell v. Wolfish, 441 U. S. 520, 534 (1979). A per­
son who is arrested for one offense but knows that he has
yet to answer for some past crime may be more inclined to
flee the instant charges, lest continued contact with the
criminal justice system expose one or more other serious
                 Cite as: 569 U. S. ____ (2013)          15

                     Opinion of the Court

offenses. For example, a defendant who had committed a
prior sexual assault might be inclined to flee on a burglary
charge, knowing that in every State a DNA sample would
be taken from him after his conviction on the burglary
charge that would tie him to the more serious charge of
rape. In addition to subverting the administration of
justice with respect to the crime of arrest, this ties back
to the interest in safety; for a detainee who absconds
from custody presents a risk to law enforcement officers,
other detainees, victims of previous crimes, witnesses, and
society at large.
   Fourth, an arrestee’s past conduct is essential to an
assessment of the danger he poses to the public, and this
will inform a court’s determination whether the individual
should be released on bail. “The government’s interest in
preventing crime by arrestees is both legitimate and com­
pelling.” United States v. Salerno, 481 U. S. 739, 749
(1987). DNA identification of a suspect in a violent crime
provides critical information to the police and judicial
officials in making a determination of the arrestee’s future
dangerousness. This inquiry always has entailed some
scrutiny beyond the name on the defendant’s driver’s
license. For example, Maryland law requires a judge to
take into account not only “the nature and circumstances
of the offense charged” but also “the defendant’s family
ties, employment status and history, financial resources,
reputation, character and mental condition, length of res­
idence in the community.” 1 Md. Rules 4–216(f)(1)(A),
(C) (2013). Knowing that the defendant is wanted for a
previous violent crime based on DNA identification is
especially probative of the court’s consideration of “the
danger of the defendant to the alleged victim, another
person, or the community.”        Rule 4–216(f)(1)(G); see
also 18 U. S. C. §3142 (2006 ed. and Supp. V) (similar
requirements).
   This interest is not speculative. In considering laws to
16                  MARYLAND v. KING

                     Opinion of the Court

require collecting DNA from arrestees, government agen­
cies around the Nation found evidence of numerous
cases in which felony arrestees would have been identified
as violent through DNA identification matching them
to previous crimes but who later committed additional
crimes because such identification was not used to detain
them. See Denver’s Study on Preventable Crimes (2009)
(three examples), online at http://www.denverda.org/DNA_
Documents / Denver%27s%20Preventable%20Crimes%20
Study.pdf (all Internet materials as visited May 31,
2013, and available in Clerk of Court’s case file); Chi­
cago’s Study on Preventable Crimes (2005) (five exam-
ples), online at http://www.denverda.org/DNA_Documents/
Arrestee_Database / Chicago%20Preventable%20Crimes-
Final.pdf; Maryland Study on Preventable Crimes (2008)
(three examples), online at http://www.denverda.org/DNA_
Documents/MarylandDNAarresteestudy.pdf.
   Present capabilities make it possible to complete a DNA
identification that provides information essential to de­
termining whether a detained suspect can be released
pending trial. See, e.g., States Brief 18, n. 10 (“DNA iden­
tification database samples have been processed in as few
as two days in California, although around 30 days has
been average”). Regardless of when the initial bail deci­
sion is made, release is not appropriate until a further
determination is made as to the person’s identity in the
sense not only of what his birth certificate states but also
what other records and data disclose to give that identity
more meaning in the whole context of who the person
really is. And even when release is permitted, the back­
ground identity of the suspect is necessary for determining
what conditions must be met before release is allowed. If
release is authorized, it may take time for the conditions
to be met, and so the time before actual release can be
substantial. For example, in the federal system, defend­
ants released conditionally are detained on average for
                  Cite as: 569 U. S. ____ (2013)            17

                      Opinion of the Court

112 days; those released on unsecured bond for 37 days;
on personal recognizance for 36 days; and on other finan­
cial conditions for 27 days. See Dept. of Justice, Bureau of
Justice Statistics, Compendium of Federal Justice Statis­
tics 45 (NCJ–213476, Dec. 2006) online at http://bjs.gov/
content/pub/pdf/cfjs04.pdf. During this entire period, ad­
ditional and supplemental data establishing more about
the person’s identity and background can provide critical
information relevant to the conditions of release and
whether to revisit an initial release determination. The
facts of this case are illustrative. Though the record is not
clear, if some thought were being given to releasing the
respondent on bail on the gun charge, a release that would
take weeks or months in any event, when the DNA report
linked him to the prior rape, it would be relevant to the
conditions of his release. The same would be true with a
supplemental fingerprint report.
    Even if an arrestee is released on bail, development of
DNA identification revealing the defendant’s unknown
violent past can and should lead to the revocation of his
conditional release. See 18 U. S. C. §3145(a) (providing for
revocation of release); see also States Brief 11–12 (discuss­
ing examples where bail and diversion determinations
were reversed after DNA identified the arrestee’s vio­
lent history). Pretrial release of a person charged with a
dangerous crime is a most serious responsibility. It is reason­
able in all respects for the State to use an accepted data­
base to determine if an arrestee is the object of suspicion
in other serious crimes, suspicion that may provide a
strong incentive for the arrestee to escape and flee.
    Finally, in the interests of justice, the identification of
an arrestee as the perpetrator of some heinous crime may
have the salutary effect of freeing a person wrongfully
imprisoned for the same offense. “[P]rompt [DNA] testing
. . . would speed up apprehension of criminals before they
commit additional crimes, and prevent the grotesque
18                   MARYLAND v. KING

                      Opinion of the Court

detention of . . . innocent people.” J. Dwyer, P. Neufeld, &
B. Scheck, Actual Innocence 245 (2000).
   Because proper processing of arrestees is so important
and has consequences for every stage of the criminal
process, the Court has recognized that the “governmen-
tal interests underlying a station-house search of the ar­
restee’s person and possessions may in some circumstances
be even greater than those supporting a search imme­
diately following arrest.” Lafayette, 462 U. S., at 645.
Thus, the Court has been reluctant to circumscribe the
authority of the police to conduct reasonable booking
searches. For example, “[t]he standards traditionally
governing a search incident to lawful arrest are not . . .
commuted to the stricter Terry standards.” Robinson,
414 U. S., at 234. Nor are these interests in identifica-
tion served only by a search of the arrestee himself.
“[I]nspection of an arrestee’s personal property may assist
the police in ascertaining or verifying his identity.” Lafa-
yette, supra, at 646. And though the Fifth Amendment’s
protection against self-incrimination is not, as a general
rule, governed by a reasonableness standard, the Court
has held that “questions . . . reasonably related to the
police’s administrative concerns . . . fall outside the protec­
tions of Miranda [v. Arizona, 384 U. S. 436 (1966)] and the
answers thereto need not be suppressed.” Pennsylvania v.
Muniz, 496 U. S. 582, 601–602 (1990).
                            B
  DNA identification represents an important advance
in the techniques used by law enforcement to serve le­
gitimate police concerns for as long as there have been
arrests, concerns the courts have acknowledged and ap­
proved for more than a century.        Law enforcement
agencies routinely have used scientific advancements in
their standard procedures for the identification of ar­
restees. “Police had been using photography to capture
                  Cite as: 569 U. S. ____ (2013)            19

                      Opinion of the Court

the faces of criminals almost since its invention.” S. Cole,
Suspect Identities 20 (2001). Courts did not dispute that
practice, concluding that a “sheriff in making an arrest for
a felony on a warrant has the right to exercise a discretion
. . . , [if] he should deem it necessary to the safe-keeping of
a prisoner, and to prevent his escape, or to enable him the
more readily to retake the prisoner if he should escape, to
take his photograph.” State ex rel. Bruns v. Clausmier,
154 Ind. 599, 601, 603, 57 N. E. 541, 542 (1900). By the
time that it had become “the daily practice of the police
officers and detectives of crime to use photographic pic­
tures for the discovery and identification of criminals,” the
courts likewise had come to the conclusion that “it would
be [a] matter of regret to have its use unduly restricted
upon any fanciful theory or constitutional privilege.”
Shaffer v. United States, 24 App. D. C. 417, 426 (1904).
    Beginning in 1887, some police adopted more exacting
means to identify arrestees, using the system of precise
physical measurements pioneered by the French anthro­
pologist Alphonse Bertillon. Bertillon identification con­
sisted of 10 measurements of the arrestee’s body, along
with a “scientific analysis of the features of the face and
an exact anatomical localization of the various scars,
marks, &c., of the body.” Defense of the Bertillon System,
N. Y. Times, Jan. 20, 1896, p. 3. “[W]hen a prisoner was
brought in, his photograph was taken according to the
Bertillon system, and his body measurements were then
made. The measurements were made . . . and noted down
on the back of a card or a blotter, and the photograph of
the prisoner was expected to be placed on the card. This
card, therefore, furnished both the likeness and descrip­
tion of the prisoner, and was placed in the rogues’ gallery,
and copies were sent to various cities where similar rec­
ords were kept.” People ex rel. Jones v. Diehl, 53 App. Div.
645, 646, 65 N. Y. S. 801, 802 (1900). As in the present
case, the point of taking this information about each ar­
20                  MARYLAND v. KING

                     Opinion of the Court

restee was not limited to verifying that the proper name
was on the indictment. These procedures were used to
“facilitate the recapture of escaped prisoners,” to aid “the
investigation of their past records and personal history,”
and “to preserve the means of identification for . . . fu-
ture supervision after discharge.” Hodgeman v. Olsen, 86
Wash. 615, 619, 150 P. 1122, 1124 (1915); see also McGov-
ern v. Van Riper, 137 N. J. Eq. 24, 33–34, 43 A. 2d 514,
519 (Ch. 1945) (“[C]riminal identification is said to have
two main purposes: (1) The identification of the accused as
the person who committed the crime for which he is being
held; and, (2) the identification of the accused as the same
person who has been previously charged with, or convicted
of, other offenses against the criminal law”).
   Perhaps the most direct historical analogue to the DNA
technology used to identify respondent is the familiar
practice of fingerprinting arrestees. From the advent of
this technique, courts had no trouble determining that
fingerprinting was a natural part of “the administrative
steps incident to arrest.” County of Riverside v. McLaugh-
lin, 500 U. S. 44, 58 (1991). In the seminal case of United
States v. Kelly, 55 F. 2d 67 (CA2 1932), Judge Augustus
Hand wrote that routine fingerprinting did not violate the
Fourth Amendment precisely because it fit within the
accepted means of processing an arrestee into custody:
        “Finger printing seems to be no more than an exten­
     sion of methods of identification long used in dealing
     with persons under arrest for real or supposed vio­
     lations of the criminal laws. It is known to be a very
     certain means devised by modern science to reach the
     desired end, and has become especially important in a
     time when increased population and vast aggrega­
     tions of people in urban centers have rendered the no­
     toriety of the individual in the community no longer a
     ready means of identification.
                 Cite as: 569 U. S. ____ (2013)             21

                        Opinion of the Court

        .           .               .             .     .
      “We find no ground in reason or authority for inter­
    fering with a method of identifying persons charged
    with crime which has now become widely known and
    frequently practiced.” Id., at 69–70.
By the middle of the 20th century, it was considered “ele­
mentary that a person in lawful custody may be required
to submit to photographing and fingerprinting as part of
routine identification processes.” Smith v. United States,
324 F. 2d 879, 882 (CADC 1963) (Burger, J.) (citations
omitted).
   DNA identification is an advanced technique superior to
fingerprinting in many ways, so much so that to insist on
fingerprints as the norm would make little sense to either
the forensic expert or a layperson. The additional intru­
sion upon the arrestee’s privacy beyond that associated
with fingerprinting is not significant, see Part V, infra,
and DNA is a markedly more accurate form of identifying
arrestees. A suspect who has changed his facial features
to evade photographic identification or even one who has
undertaken the more arduous task of altering his finger­
prints cannot escape the revealing power of his DNA.
   The respondent’s primary objection to this analogy is
that DNA identification is not as fast as fingerprinting,
and so it should not be considered to be the 21st-century
equivalent. See Tr. of Oral Arg. 53. But rapid analysis of
fingerprints is itself of recent vintage. The FBI’s vaunted
Integrated Automated Fingerprint Identification System
(IAFIS) was only “launched on July 28, 1999. Prior to this
time, the processing of . . . fingerprint submissions was
largely a manual, labor-intensive process, taking weeks or
months to process a single submission.” Federal Bureau of
Investigation, Integrated Automated Fingerprint Identifi­
cation System, online at http://www.fbi.gov/about-us/cjis/
fingerprints_biometrics/iafis/iafis. It was not the advent of
22                  MARYLAND v. KING

                     Opinion of the Court

this technology that rendered fingerprint analysis consti­
tutional in a single moment. The question of how long it
takes to process identifying information obtained from a
valid search goes only to the efficacy of the search for its
purpose of prompt identification, not the constitutionality
of the search. Cf. Ontario v. Quon, 560 U. S. ___, ___
(2010) (slip op., at 15). Given the importance of DNA in
the identification of police records pertaining to arrestees
and the need to refine and confirm that identity for its
important bearing on the decision to continue release on
bail or to impose of new conditions, DNA serves an essen­
tial purpose despite the existence of delays such as the
one that occurred in this case. Even so, the delay in
processing DNA from arrestees is being reduced to a sub­
stantial degree by rapid technical advances. See, e.g., At­
torney General DeWine Announces Significant Drop in DNA
Turnaround Time (Jan. 4, 2013) (DNA processing time
reduced from 125 days in 2010 to 20 days in 2012), online at
http://ohioattorneygeneral.gov/Media/News-Releases/January-
2013/Attorney- General - DeWine -Announces- Significant-
Drop; Gov. Jindal Announces Elimination of DNA
Backlog, DNA Unit Now Operating in Real Time (Nov. 17,
2011) (average DNA report time reduced from a year
or more in 2009 to 20 days in 2011), online at http://
www.gov.state.la.us/index.cfm?md=newsroom&tmp=detail
&articleID=3102. And the FBI has already begun testing
devices that will enable police to process the DNA of ar­
restees within 90 minutes. See Brief for National District
Attorneys Association as Amicus Curiae 20–21; Tr. of Oral
Arg. 17. An assessment and understanding of the reason­
ableness of this minimally invasive search of a person
detained for a serious crime should take account of these
technical advances. Just as fingerprinting was constitu­
tional for generations prior to the introduction of IAFIS,
DNA identification of arrestees is a permissible tool of law
enforcement today. New technology will only further
                  Cite as: 569 U. S. ____ (2013)           23

                      Opinion of the Court

improve its speed and therefore its effectiveness. And, as
noted above, actual release of a serious offender as a rou­
tine matter takes weeks or months in any event. By iden­
tifying not only who the arrestee is but also what other
available records disclose about his past to show who he is,
the police can ensure that they have the proper person
under arrest and that they have made the necessary
arrangements for his custody; and, just as important, they
can also prevent suspicion against or prosecution of the
innocent.
   In sum, there can be little reason to question “the legit­
imate interest of the government in knowing for an abso­
lute certainty the identity of the person arrested, in
knowing whether he is wanted elsewhere, and in ensuring
his identification in the event he flees prosecution.” 3 W.
LaFave, Search and Seizure §5.3(c), p. 216 (5th ed. 2012).
To that end, courts have confirmed that the Fourth
Amendment allows police to take certain routine “admin­
istrative steps incident to arrest—i.e., . . . book[ing], pho­
tograph[ing], and fingerprint[ing].”      McLaughlin, 500
U. S., at 58. DNA identification of arrestees, of the type
approved by the Maryland statute here at issue, is “no
more than an extension of methods of identification long
used in dealing with persons under arrest.” Kelly, 55
F. 2d, at 69. In the balance of reasonableness required by
the Fourth Amendment, therefore, the Court must give
great weight both to the significant government interest at
stake in the identification of arrestees and to the un­
matched potential of DNA identification to serve that
interest.
                           V

                           A

  By comparison to this substantial government interest
and the unique effectiveness of DNA identification, the
intrusion of a cheek swab to obtain a DNA sample is a
24                   MARYLAND v. KING

                     Opinion of the Court

minimal one. True, a significant government interest does
not alone suffice to justify a search. The government
interest must outweigh the degree to which the search in­
vades an individual’s legitimate expectations of privacy.
In considering those expectations in this case, however,
the necessary predicate of a valid arrest for a serious
offense is fundamental. “Although the underlying com­
mand of the Fourth Amendment is always that searches
and seizures be reasonable, what is reasonable depends on
the context within which a search takes place.” New
Jersey v. T. L. O., 469 U. S. 325, 337 (1985). “[T]he legiti­
macy of certain privacy expectations vis-à-vis the State
may depend upon the individual’s legal relationship with
the State.” Vernonia School Dist. 47J, 515 U. S., at 654.
   The reasonableness of any search must be considered
in the context of the person’s legitimate expectations of
privacy. For example, when weighing the invasiveness of
urinalysis of high school athletes, the Court noted that
“[l]egitimate privacy expectations are even less with re­
gard to student athletes. . . . Public school locker rooms,
the usual sites for these activities, are not notable for the
privacy they afford.” Id., at 657. Likewise, the Court
has used a context-specific benchmark inapplicable to the
public at large when “the expectations of privacy of cov­
ered employees are diminished by reason of their participa­
tion in an industry that is regulated pervasively,” Skinner,
489 U. S., at 627, or when “the ‘operational realities of
the workplace’ may render entirely reasonable certain
work-related intrusions by supervisors and co-workers
that might be viewed as unreasonable in other contexts,”
Von Raab, 489 U. S., at 671.
   The expectations of privacy of an individual taken into
police custody “necessarily [are] of a diminished scope.”
Bell, 441 U. S., at 557. “[B]oth the person and the property
in his immediate possession may be searched at the
station house.” United States v. Edwards, 415 U. S. 800,
                  Cite as: 569 U. S. ____ (2013)             25

                      Opinion of the Court

803 (1974). A search of the detainee’s person when he is
booked into custody may “ ‘involve a relatively extensive
exploration,’ ” Robinson, 414 U. S., at 227, including “re­
quir[ing] at least some detainees to lift their genitals or
cough in a squatting position,” Florence, 566 U. S., at ___
(slip op., at 13).
   In this critical respect, the search here at issue differs
from the sort of programmatic searches of either the public
at large or a particular class of regulated but otherwise
law-abiding citizens that the Court has previously labeled
as “ ‘special needs’ ” searches. Chandler v. Miller, 520
U. S. 305, 314 (1997). When the police stop a motorist at
a checkpoint, see Indianapolis v. Edmond, 531 U. S. 32
(2000), or test a political candidate for illegal narcotics, see
Chandler, supra, they intrude upon substantial expecta­
tions of privacy. So the Court has insisted on some pur­
pose other than “to detect evidence of ordinary criminal
wrongdoing” to justify these searches in the absence of
individualized suspicion. Edmond, supra, at 38. Once an
individual has been arrested on probable cause for a dan­
gerous offense that may require detention before trial,
however, his or her expectations of privacy and freedom
from police scrutiny are reduced. DNA identification like
that at issue here thus does not require consideration of
any unique needs that would be required to justify search­
ing the average citizen. The special needs cases, though
in full accord with the result reached here, do not have a
direct bearing on the issues presented in this case, be­
cause unlike the search of a citizen who has not been
suspected of a wrong, a detainee has a reduced expectation
of privacy.
   The reasonableness inquiry here considers two other
circumstances in which the Court has held that particular­
ized suspicion is not categorically required: “diminished
expectations of privacy [and] minimal intrusions.” McAr-
thur, 531 U. S., at 330. This is not to suggest that any
26                  MARYLAND v. KING

                     Opinion of the Court

search is acceptable solely because a person is in custody.
Some searches, such as invasive surgery, see Winston, 470
U. S. 753, or a search of the arrestee’s home, see Chimel v.
California, 395 U. S. 752 (1969), involve either greater
intrusions or higher expectations of privacy than are
present in this case. In those situations, when the Court
must “balance the privacy-related and law enforcement­
related concerns to determine if the intrusion was rea­
sonable,” McArthur, supra, at 331, the privacy-related
concerns are weighty enough that the search may require a
warrant, notwithstanding the diminished expectations of
privacy of the arrestee.
  Here, by contrast to the approved standard procedures
incident to any arrest detailed above, a buccal swab in­
volves an even more brief and still minimal intrusion. A
gentle rub along the inside of the cheek does not break the
skin, and it “involves virtually no risk, trauma, or pain.”
Schmerber, 384 U. S., at 771. “A crucial factor in analyz­
ing the magnitude of the intrusion . . . is the extent to
which the procedure may threaten the safety or health of
the individual,” Winston, supra, at 761, and nothing sug­
gests that a buccal swab poses any physical danger what­
soever. A brief intrusion of an arrestee’s person is subject
to the Fourth Amendment, but a swab of this nature does
not increase the indignity already attendant to normal
incidents of arrest.
                             B
  In addition the processing of respondent’s DNA sam­
ple’s 13 CODIS loci did not intrude on respondent’s privacy
in a way that would make his DNA identification
unconstitutional.
  First, as already noted, the CODIS loci come from non­
coding parts of the DNA that do not reveal the genetic
traits of the arrestee. While science can always progress
further, and those progressions may have Fourth Amend­
                  Cite as: 569 U. S. ____ (2013)           27

                      Opinion of the Court

ment consequences, alleles at the CODIS loci “are not
at present revealing information beyond identification.”
Katsanis & Wagner, Characterization of the Standard and
Recommended CODIS Markers, 58 J. Forensic Sci. S169,
S171 (2013). The argument that the testing at issue in
this case reveals any private medical information at all is
open to dispute.
   And even if non-coding alleles could provide some in­
formation, they are not in fact tested for that end. It is
undisputed that law enforcement officers analyze DNA for
the sole purpose of generating a unique identifying num­
ber against which future samples may be matched. This
parallels a similar safeguard based on actual practice in
the school drug-testing context, where the Court deemed it
“significant that the tests at issue here look only for drugs,
and not for whether the student is, for example, epileptic,
pregnant, or diabetic.” Vernonia School Dist. 47J, 515
U. S., at 658. If in the future police analyze samples to
determine, for instance, an arrestee’s predisposition for a
particular disease or other hereditary factors not relevant
to identity, that case would present additional privacy
concerns not present here.
   Finally, the Act provides statutory protections that
guard against further invasion of privacy. As noted above,
the Act requires that “[o]nly DNA records that directly
relate to the identification of individuals shall be collected
and stored.” Md. Pub. Saf. Code Ann. §2–505(b)(1). No
purpose other than identification is permissible: “A person
may not willfully test a DNA sample for information that
does not relate to the identification of individuals as speci­
fied in this subtitle.” §2–512(c). This Court has noted
often that “a ‘statutory or regulatory duty to avoid unwar­
ranted disclosures’ generally allays . . . privacy concerns.”
NASA v. Nelson, 562 U. S. ___, ___ (2011) (slip op., at 20)
(quoting Whalen v. Roe, 429 U. S. 589, 605 (1977)). The
Court need not speculate about the risks posed “by a
28                   MARYLAND v. KING

                      Opinion of the Court

system that did not contain comparable security provi­
sions.” Id., at 606. In light of the scientific and statutory
safeguards, once respondent’s DNA was lawfully collected
the STR analysis of respondent’s DNA pursuant to CODIS
procedures did not amount to a significant invasion of
privacy that would render the DNA identification imper­
missible under the Fourth Amendment.
                         *    *     *
   In light of the context of a valid arrest supported by
probable cause respondent’s expectations of privacy were
not offended by the minor intrusion of a brief swab of his
cheeks. By contrast, that same context of arrest gives rise
to significant state interests in identifying respondent not
only so that the proper name can be attached to his charges
but also so that the criminal justice system can make
informed decisions concerning pretrial custody. Upon
these considerations the Court concludes that DNA identi­
fication of arrestees is a reasonable search that can be
considered part of a routine booking procedure. When
officers make an arrest supported by probable cause to
hold for a serious offense and they bring the suspect to the
station to be detained in custody, taking and analyzing a
cheek swab of the arrestee’s DNA is, like fingerprinting
and photographing, a legitimate police booking procedure
that is reasonable under the Fourth Amendment.
   The judgment of the Court of Appeals of Maryland is
reversed.
                                              It is so ordered.
                 Cite as: 569 U. S. ____ (2013)            1

                     SCALIA, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 12–207
                         _________________


 MARYLAND, PETITIONER v. ALONZO JAY KING, JR.
   ON WRIT OF CERTIORARI TO THE COURT OF APPEALS OF 

                      MARYLAND

                        [June 3, 2013]


  JUSTICE SCALIA, with whom JUSTICE GINSBURG,
JUSTICE SOTOMAYOR, and JUSTICE KAGAN join, dissenting.
  The Fourth Amendment forbids searching a person for
evidence of a crime when there is no basis for believing the
person is guilty of the crime or is in possession of incrimi-
nating evidence. That prohibition is categorical and with-
out exception; it lies at the very heart of the Fourth
Amendment. Whenever this Court has allowed a suspi-
cionless search, it has insisted upon a justifying motive
apart from the investigation of crime.
  It is obvious that no such noninvestigative motive exists
in this case. The Court’s assertion that DNA is being
taken, not to solve crimes, but to identify those in the
State’s custody, taxes the credulity of the credulous. And
the Court’s comparison of Maryland’s DNA searches to
other techniques, such as fingerprinting, can seem apt
only to those who know no more than today’s opinion
has chosen to tell them about how those DNA searches
actually work.
                             I

                             A

  At the time of the Founding, Americans despised the
British use of so-called “general warrants”—warrants not
grounded upon a sworn oath of a specific infraction by a
particular individual, and thus not limited in scope and
2                    MARYLAND v. KING

                     SCALIA, J., dissenting

application. The first Virginia Constitution declared that
“general warrants, whereby any officer or messenger may
be commanded to search suspected places without evi-
dence of a fact committed,” or to search a person “whose
offence is not particularly described and supported by
evidence,” “are grievous and oppressive, and ought not be
granted.” Va. Declaration of Rights §10 (1776), in 1 B.
Schwartz, The Bill of Rights: A Documentary History 234,
235 (1971). The Maryland Declaration of Rights similarly
provided that general warrants were “illegal.” Md. Decla-
ration of Rights §XXIII (1776), in id., at 280, 282.
   In the ratification debates, Antifederalists sarcastically
predicted that the general, suspicionless warrant would be
among the Constitution’s “blessings.” Blessings of the New
Government, Independent Gazetteer, Oct. 6, 1787, in 13
Documentary History of the Ratification of the Constitu-
tion 345 (J. Kaminski & G. Saladino eds. 1981). “Brutus”
of New York asked why the Federal Constitution con-
tained no provision like Maryland’s, Brutus II, N. Y. Jour-
nal, Nov. 1, 1787, in id., at 524, and Patrick Henry warned
that the new Federal Constitution would expose the citi-
zenry to searches and seizures “in the most arbitrary
manner, without any evidence or reason.” 3 Debates on
the Federal Constitution 588 (J. Elliot 2d ed. 1854).
   Madison’s draft of what became the Fourth Amendment
answered these charges by providing that the “rights of
the people to be secured in their persons . . . from all un-
reasonable searches and seizures, shall not be violated by
warrants issued without probable cause . . . or not particu-
larly describing the places to be searched.” 1 Annals of
Cong. 434–435 (1789). As ratified, the Fourth Amend-
ment’s Warrant Clause forbids a warrant to “issue” except
“upon probable cause,” and requires that it be “particula[r]”
(which is to say, individualized) to “the place to be
searched, and the persons or things to be seized.” And we
have held that, even when a warrant is not constitution-
                 Cite as: 569 U. S. ____ (2013)            3

                     SCALIA, J., dissenting

ally necessary, the Fourth Amendment’s general prohibition
of “unreasonable” searches imports the same requirement
of individualized suspicion. See Chandler v. Miller, 520
U. S. 305, 308 (1997).
    Although there is a “closely guarded category of consti-
tutionally permissible suspicionless searches,” id., at 309,
that has never included searches designed to serve “the
normal need for law enforcement,” Skinner v. Railway
Labor Executives’ Assn., 489 U. S. 602, 619 (1989) (inter-
nal quotation marks omitted). Even the common name for
suspicionless searches—“special needs” searches—itself
reflects that they must be justified, always, by concerns
“other than crime detection.” Chandler, supra, at 313–
314. We have approved random drug tests of railroad
employees, yes—but only because the Government’s need
to “regulat[e] the conduct of railroad employees to ensure
safety” is distinct from “normal law enforcement.” Skin-
ner, supra, at 620. So too we have approved suspicionless
searches in public schools—but only because there the
government acts in furtherance of its “responsibilities . . .
as guardian and tutor of children entrusted to its care.”
Vernonia School Dist. 47J v. Acton, 515 U. S. 646, 665
(1995).
    So while the Court is correct to note (ante, at 8–9) that
there are instances in which we have permitted searches
without individualized suspicion, “[i]n none of these cases
. . . did we indicate approval of a [search] whose primary
purpose was to detect evidence of ordinary criminal
wrongdoing.” Indianapolis v. Edmond, 531 U. S. 32, 38
(2000). That limitation is crucial. It is only when a gov-
ernmental purpose aside from crime-solving is at stake
that we engage in the free-form “reasonableness” inquiry
that the Court indulges at length today. To put it another
way, both the legitimacy of the Court’s method and the
correctness of its outcome hinge entirely on the truth of a
single proposition: that the primary purpose of these DNA
4                    MARYLAND v. KING

                     SCALIA, J., dissenting

searches is something other than simply discovering evi-
dence of criminal wrongdoing. As I detail below, that
proposition is wrong.
                                B
  The Court alludes at several points (see ante, at 11, 25)
to the fact that King was an arrestee, and arrestees may
be validly searched incident to their arrest. But the Court
does not really rest on this principle, and for good reason:
The objects of a search incident to arrest must be either (1)
weapons or evidence that might easily be destroyed, or (2)
evidence relevant to the crime of arrest. See Arizona v.
Gant, 556 U. S. 332, 343–344 (2009); Thornton v. United
States, 541 U. S. 615, 632 (2004) (SCALIA, J., concurring in
judgment). Neither is the object of the search at issue
here.
  The Court hastens to clarify that it does not mean to
approve invasive surgery on arrestees or warrantless
searches of their homes. Ante, at 25. That the Court feels
the need to disclaim these consequences is as damning a
criticism of its suspicionless-search regime as any I can
muster. And the Court’s attempt to distinguish those
hypothetical searches from this real one is unconvincing.
We are told that the “privacy-related concerns” in the
search of a home “are weighty enough that the search may
require a warrant, notwithstanding the diminished expec-
tations of privacy of the arrestee.” Ante, at 26. But why
are the “privacy-related concerns” not also “weighty” when
an intrusion into the body is at stake? (The Fourth
Amendment lists “persons” first among the entities pro-
tected against unreasonable searches and seizures.) And
could the police engage, without any suspicion of wrongdo-
ing, in a “brief and . . . minimal” intrusion into the home of
an arrestee—perhaps just peeking around the curtilage a
bit? See ante, at 26. Obviously not.
  At any rate, all this discussion is beside the point. No
                      Cite as: 569 U. S. ____ (2013)                      5

                          SCALIA, J., dissenting

matter the degree of invasiveness, suspicionless searches
are never allowed if their principal end is ordinary crime-
solving. A search incident to arrest either serves other
ends (such as officer safety, in a search for weapons) or
is not suspicionless (as when there is reason to believe
the arrestee possesses evidence relevant to the crime of
arrest).
   Sensing (correctly) that it needs more, the Court elabo-
rates at length the ways that the search here served the
special purpose of “identifying” King.1 But that seems to
me quite wrong—unless what one means by “identifying”
someone is “searching for evidence that he has committed
crimes unrelated to the crime of his arrest.” At points the
Court does appear to use “identifying” in that peculiar
sense—claiming, for example, that knowing “an arrestee’s
past conduct is essential to an assessment of the danger
he poses.” Ante, at 15. If identifying someone means
finding out what unsolved crimes he has committed, then
identification is indistinguishable from the ordinary law-
enforcement aims that have never been thought to justify
a suspicionless search. Searching every lawfully stopped
car, for example, might turn up information about un-
solved crimes the driver had committed, but no one would
say that such a search was aimed at “identifying” him, and


——————
  1 The Court’s insistence (ante, at 25) that our special-needs cases “do
not have a direct bearing on the issues presented in this case” is per-
plexing. Why spill so much ink on the special need of identification if a
special need is not required? Why not just come out and say that any
suspicionless search of an arrestee is allowed if it will be useful to solve
crimes? The Court does not say that because most Members of the
Court do not believe it. So whatever the Court’s major premise—the
opinion does not really contain what you would call a rule of decision—
the minor premise is “this search was used to identify King.” The
incorrectness of that minor premise will therefore suffice to demon-
strate the error in the Court’s result.
6                   MARYLAND v. KING

                     SCALIA, J., dissenting

no court would hold such a search lawful. I will therefore
assume that the Court means that the DNA search at
issue here was useful to “identify” King in the normal
sense of that word—in the sense that would identify the
author of Introduction to the Principles of Morals and
Legislation as Jeremy Bentham.
                              1
   The portion of the Court’s opinion that explains the
identification rationale is strangely silent on the actual
workings of the DNA search at issue here. To know those
facts is to be instantly disabused of the notion that what
happened had anything to do with identifying King.
   King was arrested on April 10, 2009, on charges unre-
lated to the case before us. That same day, April 10, the
police searched him and seized the DNA evidence at issue
here. What happened next? Reading the Court’s opinion,
particularly its insistence that the search was necessary to
know “who [had] been arrested,” ante, at 11, one might
guess that King’s DNA was swiftly processed and his
identity thereby confirmed—perhaps against some master
database of known DNA profiles, as is done for finger-
prints. After all, was not the suspicionless search here
crucial to avoid “inordinate risks for facility staff” or to
“existing detainee population,” ante, at 14? Surely, then—
surely—the State of Maryland got cracking on those grave
risks immediately, by rushing to identify King with his
DNA as soon as possible.
   Nothing could be further from the truth. Maryland
officials did not even begin the process of testing King’s
DNA that day. Or, actually, the next day. Or the day
after that. And that was for a simple reason: Maryland
law forbids them to do so. A “DNA sample collected from
an individual charged with a crime . . . may not be tested
or placed in the statewide DNA data base system prior to
the first scheduled arraignment date.” Md. Pub. Saf. Code
                 Cite as: 569 U. S. ____ (2013)            7

                     SCALIA, J., dissenting

Ann. §2–504(d)(1) (Lexis 2011) (emphasis added). And
King’s first appearance in court was not until three days
after his arrest. (I suspect, though, that they did not wait
three days to ask his name or take his fingerprints.)
  This places in a rather different light the Court’s solemn
declaration that the search here was necessary so that
King could be identified at “every stage of the criminal
process.” Ante, at 18. I hope that the Maryland officials
who read the Court’s opinion do not take it seriously.
Acting on the Court’s misperception of Maryland law could
lead to jail time. See Md. Pub. Saf. Code Ann. §2–512(c)–(e)
(punishing by up to five years’ imprisonment anyone who
obtains or tests DNA information except as provided by
statute). Does the Court really believe that Maryland
did not know whom it was arraigning? The Court’s re-
sponse is to imagine that release on bail could take so long
that the DNA results are returned in time, or perhaps that
bail could be revoked if the DNA test turned up incrimi-
nating information. Ante, at 16–17. That is no answer at
all. If the purpose of this Act is to assess “whether [King]
should be released on bail,” ante, at 15, why would it
possibly forbid the DNA testing process to begin until King
was arraigned? Why would Maryland resign itself to
simply hoping that the bail decision will drag out long
enough that the “identification” can succeed before the
arrestee is released? The truth, known to Maryland and
increasingly to the reader: this search had nothing to do
with establishing King’s identity.
  It gets worse. King’s DNA sample was not received by
the Maryland State Police’s Forensic Sciences Division
until April 23, 2009—two weeks after his arrest. It sat in
that office, ripening in a storage area, until the custodians
got around to mailing it to a lab for testing on June 25,
2009—two months after it was received, and nearly three
since King’s arrest. After it was mailed, the data from the
lab tests were not available for several more weeks, until
8                   MARYLAND v. KING

                     SCALIA, J., dissenting

July 13, 2009, which is when the test results were entered
into Maryland’s DNA database, together with information
identifying the person from whom the sample was taken.
Meanwhile, bail had been set, King had engaged in dis-
covery, and he had requested a speedy trial—presumably
not a trial of John Doe. It was not until August 4, 2009—
four months after King’s arrest—that the forwarded sam-
ple transmitted (without identifying information) from the
Maryland DNA database to the Federal Bureau of Investi-
gation’s national database was matched with a sample
taken from the scene of an unrelated crime years earlier.
   A more specific description of exactly what happened at
this point illustrates why, by definition, King could
not have been identified by this match. The FBI’s
DNA database (known as CODIS) consists of two distinct
collections. FBI, CODIS and NDIS Fact Sheet, http://
www.fbi.gov/about-us/lab/codis/codis-and-ndis-fact-sheet
(all Internet materials as visited May 31, 2013, and avail-
able in Clerk of Court’s case file). One of them, the one to
which King’s DNA was submitted, consists of DNA sam-
ples taken from known convicts or arrestees. I will refer
to this as the “Convict and Arrestee Collection.” The other
collection consists of samples taken from crime scenes; I
will refer to this as the “Unsolved Crimes Collection.” The
Convict and Arrestee Collection stores “no names or other
personal identifiers of the offenders, arrestees, or detain-
ees.” Ibid. Rather, it contains only the DNA profile itself,
the name of the agency that submitted it, the laboratory
personnel who analyzed it, and an identification number
for the specimen. Ibid. This is because the submitting
state laboratories are expected already to know the identi-
ties of the convicts and arrestees from whom samples are
taken. (And, of course, they do.)
   Moreover, the CODIS system works by checking to see
whether any of the samples in the Unsolved Crimes Col-
lection match any of the samples in the Convict and Ar-
                     Cite as: 569 U. S. ____ (2013)                   9

                         SCALIA, J., dissenting

restee Collection. Ibid. That is sensible, if what one
wants to do is solve those cold cases, but note what it
requires: that the identity of the people whose DNA has
been entered in the Convict and Arrestee Collection al-
ready be known.2 If one wanted to identify someone in
custody using his DNA, the logical thing to do would be to
compare that DNA against the Convict and Arrestee
Collection: to search, in other words, the collection that
could be used (by checking back with the submitting
state agency) to identify people, rather than the collection
of evidence from unsolved crimes, whose perpetrators are
by definition unknown. But that is not what was done.
And that is because this search had nothing to do with
identification.
  In fact, if anything was “identified” at the moment that
the DNA database returned a match, it was not King—his
identity was already known. (The docket for the original
criminal charges lists his full name, his race, his sex, his
height, his weight, his date of birth, and his address.)
Rather, what the August 4 match “identified” was the
previously-taken sample from the earlier crime. That
sample was genuinely mysterious to Maryland; the State
knew that it had probably been left by the victim’s attack-
er, but nothing else. King was not identified by his associ-
ation with the sample; rather, the sample was identified
by its association with King. The Court effectively de-
stroys its own “identification” theory when it acknowledges
that the object of this search was “to see what [was] al-
ready known about [King].” King was who he was, and

——————
  2 By the way, this procedure has nothing to do with exonerating the

wrongfully convicted, as the Court soothingly promises. See ante, at 17.
The FBI CODIS database includes DNA from unsolved crimes. I know
of no indication (and the Court cites none) that it also includes DNA
from all—or even any—crimes whose perpetrators have already been
convicted.
10                  MARYLAND v. KING

                     SCALIA, J., dissenting

volumes of his biography could not make him any more or
any less King. No minimally competent speaker of Eng-
lish would say, upon noticing a known arrestee’s similarity
“to a wanted poster of a previously unidentified suspect,”
ante, at 13, that the arrestee had thereby been identified.
It was the previously unidentified suspect who had been
identified—just as, here, it was the previously unidentified
rapist.
                               2
   That taking DNA samples from arrestees has nothing to
do with identifying them is confirmed not just by actual
practice (which the Court ignores) but by the enabling
statute itself (which the Court also ignores). The Mary-
land Act at issue has a section helpfully entitled “Purpose
of collecting and testing DNA samples.” Md. Pub. Saf.
Code Ann. §2–505. (One would expect such a section to
play a somewhat larger role in the Court’s analysis of the
Act’s purpose—which is to say, at least some role.) That
provision lists five purposes for which DNA samples may
be tested. By this point, it will not surprise the reader to
learn that the Court’s imagined purpose is not among
them.
   Instead, the law provides that DNA samples are collected
and tested, as a matter of Maryland law, “as part of an
official investigation into a crime.” §2–505(a)(2). (Or, as
our suspicionless-search cases would put it: for ordinary
law-enforcement purposes.) That is certainly how every-
one has always understood the Maryland Act until today.
The Governor of Maryland, in commenting on our deci-
sion to hear this case, said that he was glad, because
“[a]llowing law enforcement to collect DNA samples . . . is
absolutely critical to our efforts to continue driving down
crime,” and “bolsters our efforts to resolve open investiga-
tions and bring them to a resolution.” Marbella, Supreme
Court Will Review Md. DNA Law, Baltimore Sun, Nov. 10,
                  Cite as: 569 U. S. ____ (2013)            11

                      SCALIA, J., dissenting

2012, pp. 1, 14. The attorney general of Maryland re-
marked that he “look[ed] forward to the opportunity to
defend this important crime-fighting tool,” and praised the
DNA database for helping to “bring to justice violent
perpetrators.” Ibid. Even this Court’s order staying the
decision below states that the statute “provides a valuable
tool for investigating unsolved crimes and thereby helping
to remove violent offenders from the general population”—
with, unsurprisingly, no mention of identity. 567 U. S.
___, ___ (2012) (ROBERTS, C. J., in chambers) (slip op.,
at 3).
   More devastating still for the Court’s “identification”
theory, the statute does enumerate two instances in which
a DNA sample may be tested for the purpose of identifica-
tion: “to help identify human remains,” §2–505(a)(3) (em-
phasis added), and “to help identify missing individuals,”
§2–505(a)(4) (emphasis added). No mention of identifying
arrestees. Inclusio unius est exclusio alterius. And note
again that Maryland forbids using DNA records “for any
purposes other than those specified”—it is actually a crime
to do so. §2–505(b)(2).
   The Maryland regulations implementing the Act con-
firm what is now monotonously obvious: These DNA
searches have nothing to do with identification. For ex-
ample, if someone is arrested and law enforcement deter-
mines that “a convicted offender Statewide DNA Data
Base sample already exists” for that arrestee, “the agency
is not required to obtain a new sample.” Code of Md.
Regs., tit. 29, §05.01.04(B)(4) (2011). But how could the
State know if an arrestee has already had his DNA sample
collected, if the point of the sample is to identify who he is?
Of course, if the DNA sample is instead taken in order to
investigate crimes, this restriction makes perfect sense:
Having previously placed an identified someone’s DNA on
file to check against available crime-scene evidence, there
is no sense in going to the expense of taking a new sample.
12                    MARYLAND v. KING

                      SCALIA, J., dissenting

Maryland’s regulations further require that the “individ-
ual collecting a sample . . . verify the identity of the indi-
vidual from whom a sample is taken by name and,
if applicable, State identification (SID) number.”
§05.01.04(K). (But how?) And after the sample is taken, it
continues to be identified by the individual’s name, finger-
prints, etc., see §05.01.07(B)—rather than (as the Court
believes) being used to identify individuals.                See
§05.01.07(B)(2) (“Records and specimen information shall
be identified by . . . [the] [n]ame of the donor” (emphasis
added)).
  So, to review: DNA testing does not even begin until
after arraignment and bail decisions are already made.
The samples sit in storage for months, and take weeks to
test. When they are tested, they are checked against the
Unsolved Crimes Collection—rather than the Convict and
Arrestee Collection, which could be used to identify them.
The Act forbids the Court’s purpose (identification), but
prescribes as its purpose what our suspicionless-search
cases forbid (“official investigation into a crime”). Against
all of that, it is safe to say that if the Court’s identification
theory is not wrong, there is no such thing as error.
                             II
  The Court also attempts to bolster its identification
theory with a series of inapposite analogies. See ante, at
18–23.
  Is not taking DNA samples the same, asks the Court, as
taking a person’s photograph? No—because that is not a
Fourth Amendment search at all. It does not involve a
physical intrusion onto the person, see Florida v.
Jardines, 569 U. S. 1, ___ (2013) (slip op., at 3), and we
have never held that merely taking a person’s photograph
invades any recognized “expectation of privacy,” see Katz
v. United States, 389 U. S. 347 (1967). Thus, it is unsur-
prising that the cases the Court cites as authorizing photo-
                    Cite as: 569 U. S. ____ (2013)                  13

                         SCALIA, J., dissenting

taking do not even mention the Fourth Amendment. See
State ex rel. Bruns v. Clausmier, 154 Ind. 599, 57 N. E.
541 (1900) (libel), Shaffer v. United States, 24 App. D. C.
417 (1904) (Fifth Amendment privilege against self-
incrimination).
   But is not the practice of DNA searches, the Court asks,
the same as taking “Bertillon” measurements—noting an
arrestee’s height, shoe size, and so on, on the back of a
photograph? No, because that system was not, in the
ordinary case, used to solve unsolved crimes. It is possi-
ble, I suppose, to imagine situations in which such meas-
urements might be useful to generate leads. (If witnesses
described a very tall burglar, all the “tall man” cards could
then be pulled.) But the obvious primary purpose of such
measurements, as the Court’s description of them makes
clear, was to verify that, for example, the person arrested
today is the same person that was arrested a year ago.
Which is to say, Bertillon measurements were actually
used as a system of identification, and drew their primary
usefulness from that task.3
   It is on the fingerprinting of arrestees, however, that the
Court relies most heavily. Ante, at 20–23. The Court does
not actually say whether it believes that taking a person’s
fingerprints is a Fourth Amendment search, and our cases
provide no ready answer to that question. Even assuming
so, however, law enforcement’s post-arrest use of finger-
prints could not be more different from its post-arrest
use of DNA. Fingerprints of arrestees are taken primarily
to identify them (though that process sometimes solves

——————
  3 Puzzlingly, the Court’s discussion of photography and Bertillon

measurements repeatedly cites state cases (such as Clausmier) that
were decided before the Fourth Amendment was held to be applicable
to the States. See Wolf v. Colorado, 338 U. S. 25 (1949); Mapp v. Ohio,
367 U. S. 643 (1961). Why the Court believes them relevant to the
meaning of that Amendment is therefore something of a mystery.
14                     MARYLAND v. KING

                        SCALIA, J., dissenting

crimes); the DNA of arrestees is taken to solve crimes
(and nothing else). Contrast CODIS, the FBI’s nationwide
DNA database, with IAFIS, the FBI’s Integrated
Automated Fingerprint Identification System. See FBI,
Integrated Automated Fingerprint Identification System,
http://www.fbi.gov/about-us/cjis/fingerprints_biometrics/iafis/iafis
(hereinafter IAFIS).

       Fingerprints                       DNA Samples
The “average response            DNA analysis can take
time for an electronic           months—far too long to be
criminal fingerprint             useful for identifying someone.
submission is about 27
minutes.” IAFIS.

IAFIS includes detailed          CODIS contains “[n]o names
identification information,      or other personal identifiers of
including “criminal histo-       the offenders, arrestees, or
ries; mug shots; scars and       detainees.” See CODIS and
tattoo photos; physical          NDIS Fact Sheet.
characteristics like
height, weight, and hair
and eye color.”

“Latent prints” recovered        The entire point of the DNA
from crime scenes are not        database is to check crime
systematically compared          scene evidence against the
against the database of          profiles of arrestees and
known fingerprints, since        convicts as they come in.
that requires further
forensic work.4

——————
  4 See,e.g., FBI, Privacy Impact Assessment: Integrated Automated
Fingerprint Identification System (IAFIS)/Next Generation Identifica-
tion (NGI) Repository for Individuals of Special Concern (RISC),
                      Cite as: 569 U. S. ____ (2013)                    15

                          SCALIA, J., dissenting

   The Court asserts that the taking of fingerprints was
“constitutional for generations prior to the introduction” of
the FBI’s rapid computer-matching system. Ante, at 22.
This bold statement is bereft of citation to authority
because there is none for it. The “great expansion in finger-
printing came before the modern era of Fourth Amend-
ment jurisprudence,” and so we were never asked to decide
the legitimacy of the practice. United States v. Kincade,
379 F. 3d 813, 874 (CA9 2004) (Kozinski, J., dissenting).
As fingerprint databases expanded from convicted
criminals, to arrestees, to civil servants, to immigrants,
to everyone with a driver’s license, Americans simply
“became accustomed to having our fingerprints on file
in some government database.” Ibid. But it is wrong
to suggest that this was uncontroversial at the time, or
that this Court blessed universal fingerprinting for
“generations” before it was possible to use it effectively for
identification.
   The Court also assures us that “the delay in processing
DNA from arrestees is being reduced to a substantial
degree by rapid technical advances.” Ante, at 22. The
idea, presumably, is that the snail’s pace in this case is
atypical, so that DNA is now readily usable for identifica-
tion. The Court’s proof, however, is nothing but a pair of
press releases—each of which turns out to undercut this
argument. We learn in them that reductions in backlog
have enabled Ohio and Louisiana crime labs to analyze a
submitted DNA sample in twenty days.5 But that is still
——————
http://www.fbi.gov/foia/privacy-impact-assessments/iafis-ngi-risc (searches
of the “Unsolved Latent File” may “take considerably more time”).
   5 See Attorney General DeWine Announces Significant Drop in

DNA Turnaround Time (Jan. 4, 2013), http://ohioattorneygeneral.gov/
Media/News-Releases/January-2013/Attorney-General-DeWine-Announces-
Significant-Drop; Gov. Jindal Announces Elimination of DNA Backlog
16                     MARYLAND v. KING

                       SCALIA, J., dissenting

longer than the eighteen days that Maryland needed to
analyze King’s sample, once it worked its way through the
State’s labyrinthine bureaucracy. What this illustrates is
that these times do not take into account the many other
sources of delay. So if the Court means to suggest that
Maryland is unusual, that may be right—it may qualify in
this context as a paragon of efficiency. (Indeed, the Gov-
ernor of Maryland was hailing the elimination of that
State’s backlog more than five years ago. See Wheeler,
O’Malley Wants to Expand DNA Testing, Baltimore Sun,
Jan. 11, 2008, p. 5B.) Meanwhile, the Court’s holding
will result in the dumping of a large number of arrestee
samples—many from minor offenders—onto an already over-
burdened system: Nearly one-third of Americans will be
arrested for some offense by age 23. See Brame, Turner,
Paternoster, & Bushway, Cumulative Prevalence of Arrest
From Ages 8 to 23 in a National Sample, 129 Pediatrics 21
(2011).
  The Court also accepts uncritically the Government’s
representation at oral argument that it is developing
devices that will be able to test DNA in mere minutes. At
most, this demonstrates that it may one day be possible to
design a program that uses DNA for a purpose other than
crime-solving—not that Maryland has in fact designed
such a program today. And that is the main point, which
the Court’s discussion of the brave new world of instant
DNA analysis should not obscure. The issue before us is
not whether DNA can some day be used for identification;
nor even whether it can today be used for identification;
but whether it was used for identification here.
  Today, it can fairly be said that fingerprints really are
used to identify people—so well, in fact, that there would

—————— 

(Nov. 17, 2011), http://www.gov.state.la.us/index.cfm?md=newsroom& 

tmp=detail&articleID=3102.

                 Cite as: 569 U. S. ____ (2013)           17

                     SCALIA, J., dissenting

be no need for the expense of a separate, wholly redundant
DNA confirmation of the same information. What DNA
adds—what makes it a valuable weapon in the law-
enforcement arsenal—is the ability to solve unsolved
crimes, by matching old crime-scene evidence against the
profiles of people whose identities are already known.
That is what was going on when King’s DNA was taken,
and we should not disguise the fact. Solving unsolved
crimes is a noble objective, but it occupies a lower place in
the American pantheon of noble objectives than the pro-
tection of our people from suspicionless law-enforcement
searches. The Fourth Amendment must prevail.
                          *    *   *
   The Court disguises the vast (and scary) scope of its
holding by promising a limitation it cannot deliver. The
Court repeatedly says that DNA testing, and entry into a
national DNA registry, will not befall thee and me, dear
reader, but only those arrested for “serious offense[s].”
Ante, at 28; see also ante, at 1, 9, 14, 17, 22, 23, 24 (re-
peatedly limiting the analysis to “serious offenses”). I
cannot imagine what principle could possibly justify this
limitation, and the Court does not attempt to suggest any.
If one believes that DNA will “identify” someone arrested
for assault, he must believe that it will “identify” someone
arrested for a traffic offense. This Court does not base its
judgments on senseless distinctions. At the end of the
day, logic will out. When there comes before us the taking
of DNA from an arrestee for a traffic violation, the Court
will predictably (and quite rightly) say, “We can find no
significant difference between this case and King.” Make
no mistake about it: As an entirely predictable conse-
quence of today’s decision, your DNA can be taken and
entered into a national DNA database if you are ever
arrested, rightly or wrongly, and for whatever reason.
   The most regrettable aspect of the suspicionless search
18                     MARYLAND v. KING

                        SCALIA, J., dissenting

that occurred here is that it proved to be quite unneces-
sary. All parties concede that it would have been entirely
permissible, as far as the Fourth Amendment is con-
cerned, for Maryland to take a sample of King’s DNA as a
consequence of his conviction for second-degree assault.
So the ironic result of the Court’s error is this: The only
arrestees to whom the outcome here will ever make a
difference are those who have been acquitted of the crime
of arrest (so that their DNA could not have been taken
upon conviction). In other words, this Act manages to
burden uniquely the sole group for whom the Fourth
Amendment’s protections ought to be most jealously
guarded: people who are innocent of the State’s accusations.
   Today’s judgment will, to be sure, have the beneficial
effect of solving more crimes; then again, so would the
taking of DNA samples from anyone who flies on an air-
plane (surely the Transportation Security Administration
needs to know the “identity” of the flying public), applies
for a driver’s license, or attends a public school. Perhaps
the construction of such a genetic panopticon is wise. But
I doubt that the proud men who wrote the charter of our
liberties would have been so eager to open their mouths
for royal inspection.
   I therefore dissent, and hope that today’s incursion upon
the Fourth Amendment, like an earlier one,6 will some day
be repudiated.




——————
  6 Compare, New York v. Belton, 453 U. S. 454 (1981) (suspicionless

search of a car permitted upon arrest of the driver), with Arizona v.
Gant, 556 U. S. 332 (2009) (on second thought, no).

```

---

## GROUP: _overhaul2/lake/cases/Maryland v. Macon.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Maryland v. Macon"
type: case
citation: "472 U.S. 463 (1985)"
parallel_cite: "105 S. Ct. 2778; 86 L. Ed. 2d 370; 53 U.S.L.W. 4783"
neutral_cite: 1985 U.S. LEXIS 110
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-06-17
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Maryland v. Macon
  varies_by_point: false
  scope_note: "Good law; an undercover over-the-counter purchase of materials exposed for public sale is neither a search nor a seizure."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111477/maryland-v-macon/"
  cluster_id: 111477
  opinion_id: 9430099
  identity_checked: true
homes:
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
  - page: "[[Consent Searches]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Jacobsen]]", "[[Lo-Ji Sales, Inc. v. New York]]"]
aliases: ["Maryland v. MacOn"]
tags: ["case", "fourth-amendment", "search", "seizure", "undercover", "first-amendment-materials"]
holding: "An undercover officer's purchase of magazines from a public store is neither a search (no REP in wares exposed to the public) nor a seizure (the seller voluntarily transferred possession)."
lake:
  record_id: Maryland v. Macon
  status: verified
  projected_at: 2026-07-06
---

# Maryland v. Macon

*472 U.S. 463 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Plain-clothes detectives entered an adult bookstore open to the public, browsed, and one bought two magazines from a clerk with a marked $50 bill. After determining the magazines were obscene, the detectives returned, arrested the clerk (Macon), and retrieved the marked bill from the register. Macon argued the warrantless purchase amounted to an unconstitutional search and seizure of presumptively protected First Amendment materials.

## Issue
Whether an undercover officer's entry into a store open to the public and purchase of allegedly obscene magazines exposed for sale constitutes a Fourth Amendment search or seizure.

## Rule
**No search.** "The officer's action in entering the bookstore and examining the wares that were intentionally exposed to all who frequent the place of business did not infringe a legitimate expectation of privacy and hence did not constitute a search within the meaning of the Fourth Amendment." — 472 U.S. at 469. ^pin-469

**No seizure.** "Nor was the subsequent purchase a seizure within the meaning of the Fourth Amendment. . . . Here, respondent voluntarily transferred any possessory interest he may have had in the magazines to the purchaser upon the receipt of the funds." — *Id.* ^pin-469a

## Application
The detectives entered a store open to the public and examined magazines deliberately displayed for sale — conduct that invaded no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]]. The over-the-counter sale transferred the seller's possessory interest in the magazines in exchange for the money, so the officer "interfered" with nothing the Fourth Amendment protects. Judged objectively, the transaction was an ordinary retail sale; the officer's subjective plan to later retrieve the marked bill did not retroactively transform the purchase into a seizure.

## Conclusion
The undercover purchase was neither a search nor a seizure; the magazines were properly admitted. Acquiring evidence by a routine public purchase, like an invited undercover entry, does not trigger the Fourth Amendment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Applies the seizure definition of [[United States v. Jacobsen]] and the misplaced-trust/invited-entry reasoning of *[[Lewis v. United States (1966)|Lewis v. United States]]* (1966); distinguishes the unconstitutional wholesale magistrate-led seizure in [[Lo-Ji Sales, Inc. v. New York]].

## Appears on
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*
- [[Consent Searches]] — *Related (cross-doctrine)*

## Sources
- *Maryland v. Macon*, 472 U.S. 463 (1985) — https://www.courtlistener.com/opinion/111477/maryland-v-macon/ — pinpoint: 469.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7ea80cd310fa0880", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Maryland v. Macon"}, "payload": {"all": [{"cite": "472 U.S. 463", "page": "463", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "472"}, {"cite": "105 S. Ct. 2778", "page": "2778", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "105"}, {"cite": "86 L. Ed. 2d 370", "page": "370", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "86"}, {"cite": "1985 U.S. LEXIS 110", "page": "110", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1985"}, {"cite": "53 U.S.L.W. 4783", "page": "4783", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "53"}], "display": "472 U.S. 463", "official": {"cite": "472 U.S. 463", "page": "463", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "472"}, "official_selection_present": true, "record_id": "Maryland v. Macon"}}
{"assertion_id": "828315d2a9c70211", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-469a", "record_id": "Maryland v. Macon"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-469a", "pinpoint_status": "slip-only", "quote": "Nor was the subsequent purchase a seizure within the meaning of the Fourth Amendment. . . . Here, respondent voluntarily transferred any possessory interest he may have had in the magazines to the purchaser upon the receipt of the funds.", "quote_fidelity": "mismatch", "record_id": "Maryland v. Macon", "star_marker": null}}
{"assertion_id": "f15a6f2ebc1c9128", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-469", "record_id": "Maryland v. Macon"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-469", "pinpoint_status": "slip-only", "quote": "--- # Maryland v. Macon *472 U.S. 463 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Plain-clothes detectives entered an adult bookstore open to the public, browsed, and one bought two magazines from a clerk with a marked $50 bill. After determining the magazines were obscene, the detectives returned, arrested the clerk (Macon), and retrieved the marked bill from the register. Macon argued the warrantless purchase amounted to an unconstitutional search and seizure of presumptively protected First Amendment materials. ## Issue Whether an undercover officer's entry into a store open to the public and purchase of allegedly obscene magazines exposed for sale constitutes a Fourth Amendment search or seizure. ## Rule **No search.**", "quote_fidelity": "mismatch", "record_id": "Maryland v. Macon", "star_marker": null}}
{"assertion_id": "d735060468023a6f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Maryland v. Macon"}, "payload": {"as_of_content": "1985-06-17", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Maryland v. Macon", "scope_note": "Good law; an undercover over-the-counter purchase of materials exposed for public sale is neither a search nor a seizure.", "varies_by_point": false}}
```

### lake record — Maryland v. Macon

```json
{
  "schema_version": "s2.v1",
  "record_id": "Maryland v. Macon",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Maryland v. MacOn",
    "case_name_short": "MacOn",
    "case_name_full": "Maryland v. MacOn",
    "input_case_name": "Maryland v. Macon",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-06-17",
    "year": 1985,
    "docket": null,
    "cluster_id": 111477,
    "lead_opinion_id": 9430099,
    "sibling_ids": [
      111477,
      9430099,
      9430100
    ],
    "absolute_url": "/opinion/111477/maryland-v-macon/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9051928,
        "score": 20,
        "case_name": "Maryland v. Macon"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "472 U.S. 463",
      "volume": "472",
      "reporter": "U.S.",
      "page": "463",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 2778",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "2778",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "86 L. Ed. 2d 370",
        "volume": "86",
        "reporter": "L. Ed. 2d",
        "page": "370",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4783",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4783",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 110",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "110",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "472 U.S. 463",
        "volume": "472",
        "reporter": "U.S.",
        "page": "463",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 2778",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "2778",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "86 L. Ed. 2d 370",
        "volume": "86",
        "reporter": "L. Ed. 2d",
        "page": "370",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 110",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "110",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4783",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4783",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "472 U.S. 463",
    "official_selection": {
      "court_class": "scotus",
      "selected": "472 U.S. 463",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-469",
      "page": null,
      "quote": "--- # Maryland v. Macon *472 U.S. 463 (1985)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Plain-clothes detectives entered an adult bookstore open to the public, browsed, and one bought two magazines from a clerk with a marked $50 bill. After determining the magazines were obscene, the detectives returned, arrested the clerk (Macon), and retrieved the marked bill from the register. Macon argued the warrantless purchase amounted to an unconstitutional search and seizure of presumptively protected First Amendment materials. ## Issue Whether an undercover officer's entry into a store open to the public and purchase of allegedly obscene magazines exposed for sale constitutes a Fourth Amendment search or seizure. ## Rule **No search.**",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-469a",
      "page": null,
      "quote": "Nor was the subsequent purchase a seizure within the meaning of the Fourth Amendment. . . . Here, respondent voluntarily transferred any possessory interest he may have had in the magazines to the purchaser upon the receipt of the funds.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Maryland v. Macon",
    "varies_by_point": false,
    "scope_note": "Good law; an undercover over-the-counter purchase of materials exposed for public sale is neither a search nor a seizure.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4578601,
          "cite": [
            "202 A.3d 125"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri v. Nicholas Carr",
          "cluster_id": 2731166,
          "cite": [
            "441 S.W.3d 166",
            "2014 Mo. App. LEXIS 997",
            "2014 WL 4411614"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Al-Kidd v. Ashcroft",
          "cluster_id": 1204118,
          "cite": [
            "580 F.3d 949",
            "2009 U.S. App. LEXIS 20000",
            "2009 WL 2836448"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Christopher Leon Christopher",
          "cluster_id": 4472742,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Eric Perez v. State",
          "cluster_id": 2922355,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Harsimrat Singh Randhir Singh Khangura",
          "cluster_id": 785673,
          "cite": [
            "363 F.3d 347",
            "2004 U.S. App. LEXIS 6332",
            "2004 WL 691524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane1_negative"
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
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Hicks",
          "cluster_id": 111834,
          "cite": [
            "94 L. Ed. 2d 347",
            "107 S. Ct. 1149",
            "480 U.S. 321",
            "1987 U.S. LEXIS 1056",
            "55 U.S.L.W. 4258"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Soldal v. Cook County",
          "cluster_id": 112795,
          "cite": [
            "121 L. Ed. 2d 450",
            "113 S. Ct. 538",
            "506 U.S. 56",
            "1992 U.S. LEXIS 7835",
            "92 Daily Journal DAR 16378",
            "61 U.S.L.W. 4019",
            "6 Fla. L. Weekly Fed. S 769",
            "92 Cal. Daily Op. Serv. 9794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Lee Rusher, United States of America v. Sarah Jean Shoemaker Rusher, A/K/A Sarah Anne Rusher, United States of America v. James Joseph Flannery, A/K/A James Joseph Fleming, A/K/A Richard J. Mutschler",
          "cluster_id": 584528,
          "cite": [
            "966 F.2d 868",
            "1992 U.S. App. LEXIS 12338"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Class",
          "cluster_id": 111600,
          "cite": [
            "89 L. Ed. 2d 81",
            "106 S. Ct. 960",
            "475 U.S. 106",
            "1986 U.S. LEXIS 5",
            "54 U.S.L.W. 4178"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alexander v. United States",
          "cluster_id": 112902,
          "cite": [
            "125 L. Ed. 2d 441",
            "113 S. Ct. 2766",
            "509 U.S. 544",
            "1993 U.S. LEXIS 4409"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Murad Nersesian",
          "cluster_id": 492031,
          "cite": [
            "824 F.2d 1294",
            "23 Fed. R. Serv. 487",
            "1987 U.S. App. LEXIS 8418"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garcia v. State",
          "cluster_id": 2428168,
          "cite": [
            "827 S.W.2d 937",
            "1992 Tex. Crim. App. LEXIS 83",
            "1992 WL 61756"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carlos Botero-Ospina",
          "cluster_id": 709242,
          "cite": [
            "71 F.3d 783",
            "1995 U.S. App. LEXIS 34347",
            "1995 WL 723102"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Luis Guzman and Sonia Cruz-Lazo",
          "cluster_id": 516479,
          "cite": [
            "864 F.2d 1512",
            "1988 U.S. App. LEXIS 17681",
            "1988 WL 138644"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cecil Ferguson",
          "cluster_id": 656143,
          "cite": [
            "8 F.3d 385",
            "1993 U.S. App. LEXIS 28306",
            "1993 WL 437691"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albert Woods v. City of Chicago, Officer Makowski, Chicago Police Officer 16971, Officer Alanis, Chicago Police Officer 5001",
          "cluster_id": 771403,
          "cite": [
            "234 F.3d 979",
            "55 Fed. R. Serv. 912",
            "2000 U.S. App. LEXIS 31315",
            "2000 WL 1801038"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Olsen v. Layton Hills Mall",
          "cluster_id": 162822,
          "cite": [
            "312 F.3d 1304",
            "2002 U.S. App. LEXIS 25446",
            "2002 WL 31768455"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. Miller",
          "cluster_id": 8442644,
          "cite": [
            "818 F.3d 49",
            "2016 U.S. App. LEXIS 4701",
            "2016 WL 963904"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
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
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Edelmiro Augustin Fernandez",
          "cluster_id": 664754,
          "cite": [
            "18 F.3d 874",
            "1994 U.S. App. LEXIS 4377",
            "1994 WL 74413"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Hassan El",
          "cluster_id": 653635,
          "cite": [
            "5 F.3d 726",
            "1993 U.S. App. LEXIS 23376",
            "1993 WL 345368"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory Lynn Cummins, United States of America v. Timothy Akins, A/K/A Michael Mayfield",
          "cluster_id": 552404,
          "cite": [
            "920 F.2d 498"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Timothy Andrew Smith, Stephen Lawrence Swindell",
          "cluster_id": 475352,
          "cite": [
            "799 F.2d 704",
            "1986 U.S. App. LEXIS 30726",
            "55 U.S.L.W. 2202"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'HARA v. State",
          "cluster_id": 2275765,
          "cite": [
            "27 S.W.3d 548",
            "2000 Tex. Crim. App. LEXIS 83",
            "2000 WL 1347932"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Meekins v. State",
          "cluster_id": 2544137,
          "cite": [
            "340 S.W.3d 454",
            "2011 Tex. Crim. App. LEXIS 592",
            "2011 WL 1663151"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Reginald James Causey",
          "cluster_id": 498394,
          "cite": [
            "834 F.2d 1179",
            "1987 U.S. App. LEXIS 17041",
            "1987 WL 23392"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alexis v. McDonald's Restaurants of Massachusetts, Inc.",
          "cluster_id": 196337,
          "cite": [
            "67 F.3d 341",
            "43 Fed. R. Serv. 315",
            "1995 U.S. App. LEXIS 28046",
            "1995 WL 584187"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Aguilar",
          "cluster_id": 8980450,
          "cite": [
            "883 F.2d 662"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. P. J. Video, Inc.",
          "cluster_id": 111635,
          "cite": [
            "89 L. Ed. 2d 871",
            "106 S. Ct. 1610",
            "475 U.S. 868",
            "1986 U.S. LEXIS 104",
            "54 U.S.L.W. 4396"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Macon:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111477 OR 9430099 OR 9430100) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NjcyMzIwMDAwMDAmcz0xMjA5OTQwJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111477+OR+9430099+OR+9430100%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111477 OR 9430099 OR 9430100)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzYmcz00ODI4NzAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111477+OR+9430099+OR+9430100%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111477 OR 9430099 OR 9430100)",
        "reviewed": 3,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 3,
        "triage_read": 0,
        "triage_snippet_classified": 3
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111477 OR 9430099 OR 9430100)",
    "indexed_citing_opinions": 403,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111477,
        "count": 372,
        "count_source": "search"
      },
      {
        "opinion_id": 9430099,
        "count": 40,
        "count_source": "search"
      },
      {
        "opinion_id": 9430100,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 626,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/maryland-v-macon.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjUzOTQyNjcmcz00Mzg4MDkwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111477+OR+9430099+OR+9430100%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111477,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 104977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 106287,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 106530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 107238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 107755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 108838,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 108839,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 108853,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 108854,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 110100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 110230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 372546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 1168654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 1235659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 1270714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 1355149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 2133248,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111477,
        "cited_id": 2272875,
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
    "date_created": "2026-07-05T12:04:37Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T12:04:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T12:04:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T12:09:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T12:04:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Maryland v. Macon

```
<opinion type="majority">
<author id="b474-10">Justice O’Connor</author>
<p id="A5cj">delivered the opinion of the Court.</p>
<p id="Abu">This case requires us to decide whether allegedly obscene magazines purchased by undercover officers shortly before <page-number citation-index="1" label="465">*465</page-number>the warrantless arrest of a salesclerk must be excluded from evidence at the clerk’s subsequent trial for distribution of obscene materials. Following a jury trial in the Circuit Court of Prince George’s County, Maryland, respondent was convicted of distribution of obscene materials in violation of Md. Ann. Code, Art. 27, § 418 (1982). The Maryland Court of Special Appeals reversed the conviction and ordered the charges dismissed on the ground that the magazines were improperly admitted in evidence. <span class="citation" data-id="2272875"><a href="/opinion/2272875/macon-v-state/" aria-description="Citation for case: MacOn v. State">57 Md. App. 705</a></span>, <span class="citation" data-id="2272875"><a href="/opinion/2272875/macon-v-state/" aria-description="Citation for case: MacOn v. State">471 A. 2d 1090</a></span> (1984). The Maryland Court of Appeals denied cer-tiorari. <span class="citation no-link">300 Md. 795</span>, <span class="citation no-link">481 A. 2d 240</span> (1984). We granted cer-tiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./469/1156/">469 U. S. 1156</a></span> (1985), to resolve a conflict among the state courts on the question whether a purchase of allegedly obscene matter by an undercover police officer constitutes a seizure under the Fourth Amendment. Finding that it does not, we reverse.</p>
<p id="b475-5">I</p>
<p id="b475-6">On May 6, 1981, three Prince George’s County police detectives went to the Silver News, Inc., an adult bookstore in Hyattsville, Maryland, as part of a police investigation of adult bookstores in the area. One of the detectives, who was not in uniform, entered the store, browsed for several minutes, and purchased two magazines from a clerk, Baxter Macon, with a marked $50 bill. The detective left the store and showed the two magazines to his fellow officers who were waiting nearby. Together they concluded that the magazines were obscene under the criteria previously used by them in warrant applications. The detectives returned to the store, arrested respondent Macon, who was the only attendant in the store, and retrieved from the cash register the $50 bill that had been used to make the purchase. The officers neglected to return the change received at the time of the purchase. Respondent escorted the remaining customers out and closed the bookstore before leaving with the detectives.</p>
<p id="b476-4"><page-number citation-index="1" label="466">*466</page-number>Prior to trial, Macon moved to suppress the magazines purchased by the officers and the $50 bill used to make the purchase. App. 21. The trial judge denied the motion on the grounds that the purchase was not a seizure within the meaning of the Fourth Amendment and that the warrantless arrest was lawful. <em>Id., </em>at 52. The magazines, but not the $50 bill, were subsequently introduced in evidence at trial. The jury found respondent guilty of distributing obscene materials. Respondent appealed, contending that a prior judicial determination of probable cause to believe the matter distributed was obscene was required to sustain a seizure and an arrest on charges related to obscenity. Absent such a determination, respondent argued, the allegedly obscene materials must be suppressed and the charges must be dismissed. Respondent did not challenge the jury’s finding that the magazines were obscene.</p>
<p id="b476-5">The Maryland Court of Special Appeals agreed that a warrant is required both to seize allegedly obscene materials and to arrest the distributor in order to provide a procedural safeguard for the First Amendment freedom of expression. <span class="citation" data-id="2272875"><a href="/opinion/2272875/macon-v-state/#710" aria-description="Citation for case: MacOn v. State">57 Md. App., at 710</a></span>, <span class="citation" data-id="2272875"><a href="/opinion/2272875/macon-v-state/#1092" aria-description="Citation for case: MacOn v. State">471 A. 2d, at 1092</a></span>. In cases involving First Amendment rights, the court reasoned, Fourth Amendment safeguards, including suppression of material acquired in connection with a warrantless arrest, must be applied more stringently. <em><span class="citation" data-id="2272875"><a href="/opinion/2272875/macon-v-state/" aria-description="Citation for case: MacOn v. State">Ibid.</a></span> </em>The court determined that the purchase of the magazines was a “constructive” seizure and that the proper remedy was to exclude the magazines from evidence at the subsequent trial. <span class="citation" data-id="2272875"><a href="/opinion/2272875/macon-v-state/#716" aria-description="Citation for case: MacOn v. State"><em>Id., </em>at 716</a></span>, <span class="citation" data-id="2272875"><a href="/opinion/2272875/macon-v-state/#1096" aria-description="Citation for case: MacOn v. State">471 A. 2d, at 1096</a></span>. Alternatively, the court held that the warrant-less arrest of respondent on obscenity charges required the exclusion of the publications from evidence. <span class="citation" data-id="2272875"><a href="/opinion/2272875/macon-v-state/#719" aria-description="Citation for case: MacOn v. State"><em>Id., </em>at 719</a></span>, <span class="citation" data-id="2272875"><a href="/opinion/2272875/macon-v-state/#1097" aria-description="Citation for case: MacOn v. State">471 A. 2d, at 1097</a></span>. The court accordingly reversed the conviction and ordered that the charges be dismissed because without the magazines the evidence was insufficient to sustain a conviction. <em><span class="citation" data-id="2272875"><a href="/opinion/2272875/macon-v-state/" aria-description="Citation for case: MacOn v. State">Ibid.</a></span></em></p>
<p id="b477-3"><page-number citation-index="1" label="467">*467</page-number>By holding that the purchase constituted a seizure within the meaning of the Fourth Amendment, the Maryland Court of Special Appeals rejected the position taken by the majority of state courts that have considered the issue. In evaluating the undercover purchase of allegedly obscene materials, most state courts have treated as self-evident the proposition that a purchase by an undercover officer is not a seizure, regardless of whether the funds used to make the purchase are later retrieved as evidence. See, <em>e. g., Baird </em>v. <em>State, </em><span class="citation" data-id="6550609"><a href="/opinion/6672386/baird-v-state/" aria-description="Citation for case: Baird v. State">12 Ark. App. 71</a></span>, <span class="citation" data-id="6550609"><a href="/opinion/6672386/baird-v-state/" aria-description="Citation for case: Baird v. State">671 S. W. 2d 191</a></span> (1984) (en banc); <em>Wood </em>v. <em>State, </em><span class="citation" data-id="1355149"><a href="/opinion/1355149/wood-v-state/" aria-description="Citation for case: Wood v. State">144 Ga. App. 236</a></span>, <span class="citation" data-id="1355149"><a href="/opinion/1355149/wood-v-state/" aria-description="Citation for case: Wood v. State">240 S. E. 2d 743</a></span> (1977), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./439/899/">439 U. S. 899</a></span> (1978); <em>People </em>v. <em>Ridens, </em><span class="citation" data-id="2133248"><a href="/opinion/2133248/people-v-ridens/" aria-description="Citation for case: People v. Ridens">51 Ill. 2d 410</a></span>, <span class="citation" data-id="2133248"><a href="/opinion/2133248/people-v-ridens/" aria-description="Citation for case: People v. Ridens">282 N. E. 2d 691</a></span> (1972), vacated and remanded on other grounds, <span class="citation" data-id="8986127"><a href="/opinion/8993864/court-v-wisconsin/" aria-description="Citation for case: Court v. Wisconsin">413 U. S. 912</a></span> (1973); <em>State </em>v. <em>Welke, </em><span class="citation" data-id="9847940"><a href="/opinion/1270714/state-v-welke/" aria-description="Citation for case: State v. Welke">298 Minn. 402</a></span>, <span class="citation" data-id="9847940"><a href="/opinion/1270714/state-v-welke/" aria-description="Citation for case: State v. Welke">216 N. W. 2d 641</a></span> (1974); <em>State </em>v. <em>Perry, </em><span class="citation" data-id="5049337"><a href="/opinion/5224878/state-v-perry/" aria-description="Citation for case: State v. Perry">567 S. W. 2d 380</a></span> (Mo. App. 1978); <em>State </em>v. <em>Dornblaser, </em><span class="citation" data-id="8514627"><a href="/opinion/8542026/state-v-dornblaser/" aria-description="Citation for case: State v. Dornblaser">26 Ohio Misc. 29</a></span>, <span class="citation" data-id="8514627"><a href="/opinion/8542026/state-v-dornblaser/" aria-description="Citation for case: State v. Dornblaser">267 N. E. 2d 434</a></span> (1971); <em>Cherokee News &amp; Arcade, Inc. </em>v. <em>State, </em><span class="citation" data-id="1235659"><a href="/opinion/1235659/cherokee-news-arcade-inc-v-state/" aria-description="Citation for case: Cherokee News &amp; Arcade, Inc. v. State">533 P. 2d 624</a></span> (Okla. Crim. App. 1974). But see <em>State </em>v. <em>Furuyama, </em><span class="citation" data-id="1168654"><a href="/opinion/1168654/state-v-furuyama/" aria-description="Citation for case: State v. Furuyama">64 Haw. 109</a></span>, <span class="citation" data-id="1168654"><a href="/opinion/1168654/state-v-furuyama/" aria-description="Citation for case: State v. Furuyama">637 P. 2d 1095</a></span> (1981) (reaching the contrary conclusion).</p>
<p id="b477-4">For the reasons set forth below, we conclude that the officer’s entry into the bookstore and later examination of materials offered for sale there did not constitute a search and that the purchase of two magazines did not effect a seizure. We do not decide whether a warrant is required to arrest a suspect on obscenity-related charges, because the magazines at issue were not the product of the warrantless arrest. Because we hold that the magazines were properly admitted in evidence at trial, we also do not address respondent’s contention that the Double Jeopardy Clause bars retrial.</p>
<p id="b477-5">II</p>
<p id="b477-6">The central issue presented is whether the magazines purchased by the undercover detectives before respondent’s arrest must be suppressed. If the publications were ob<page-number citation-index="1" label="468">*468</page-number>tained by means of an unreasonable search or seizure, or were the fruits of an unlawful arrest, the Fourth Amendment requires their exclusion from evidence. If, however, the evidence is not traceable to any Fourth Amendment violation, exclusion is unwarranted. See <em>United States </em>v. <em>Crews, </em><span class="citation" data-id="9427838"><a href="/opinion/110230/united-states-v-crews/#472" aria-description="Citation for case: United States v. Crews">445 U. S. 463, 472</a></span> (1980).</p>
<p id="b478-5">A</p>
<p id="b478-6">The First Amendment imposes special constraints on searches for and seizures of presumptively protected material, <em>Lo-Ji Sales, Inc. </em>v. <em>New York, </em><span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/#326" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York">442 U. S. 319, 326, n. 5</a></span> (1979), and requires that the Fourth Amendment be applied with “scrupulous exactitude” in such circumstances. <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 485</a></span> (1965). Consequently, the Court has imposed particularized rules applicable to searches for and seizures of allegedly obscene films, books, arid papers. See, <em>e. g., Roaden </em>v. <em>Kentucky, </em><span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/#497" aria-description="Citation for case: Roaden v. Kentucky">413 U. S. 496, 497</a></span> (1973) (“seizure of allegedly obscene material, contemporaneous with and as an incident to an arrest for the public exhibition of such material . . . may [not] be accomplished without a warrant”); <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717</a></span> (1961) (warrant to seize allegedly obscene magazines must be particularized and may not issue merely on officer’s conclusory assertion). Although we have not previously had an occasion to analyze the question whether a purchase of obscene material is properly classified as a seizure, some prior cases have involved seizures that followed bona fide undercover purchases. See, <em>e. g., Lo-Ji Sales, Inc. </em>v. <em>New <span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York">York, supra;</a></span> Marcus </em>v. <em>Search <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Warrant, supra.</a></span> </em>In those cases, the Court did not address the exclusion of the purchased materials, but only of the materials obtained through mass seizures conducted pursuant to unconstitutional open-ended warrants. Absent some action taken by government agents that can properly be classified as a “search” or a “seizure,” the Fourth Amendment rules designed to safeguard First Amendment freedoms do not <page-number citation-index="1" label="469">*469</page-number>apply. Cf. <em>Lo-Ji Sales, Inc. </em>v. <span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/#326" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York"><em>New York, supra, </em>at 326, n. 5</a></span>; <em>Roaden </em>v. <span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/#505" aria-description="Citation for case: Roaden v. Kentucky"><em>Kentucky, supra, </em>at 505</a></span> (sheriff seized a film from a commercial theater currently screening it).</p>
<p id="b479-5">A search occurs when “an expectation of privacy that society is prepared to consider reasonable is infringed.” <em>United States </em>v. <em>Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 113</a></span> (1984). Here, respondent did not have any reasonable expectation of privacy in areas of the store where the public was invited to enter and to transact business. Cf. <em>United States </em>v. <em>Knotts, </em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#281" aria-description="Citation for case: United States v. Knotts">460 U. S. 276, 281-282</a></span> (1983). The mere expectation that the possibly illegal nature of a product will not come to the attention of the authorities, whether because a customer will not complain or because undercover officers will not transact business with the store, is not one that society is prepared to recognize as reasonable. Cf. <em>United States </em>v. <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#122" aria-description="Citation for case: United States v. Jacobsen"><em>Jacobsen, supra, </em>at 122-123, n. 22</a></span>. The officer’s action in entering the bookstore and examining the wares that were intentionally exposed to all who frequent the place of business did not infringe a legitimate, expectation of privacy and hence did not constitute a search within the meaning of the Fourth Amendment. See <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967) (“What a person knowingly exposes to the public ... is not a subject of Fourth Amendment protection”).</p>
<p id="b479-6">Nor was the subsequent purchase a seizure within the meaning of the Fourth Amendment. A seizure occurs when “there is some meaningful interference with an individual’s possessory interests” in the property seized. <em>United States </em>v. <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen"><em>Jacobsen, supra, </em>at 113</a></span>. Here, respondent voluntarily transferred any possessory interest he may have had in the magazines to the purchaser upon the receipt of the funds. Cf. <em>Lewis </em>v. <em>United States, </em><span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/#210" aria-description="Citation for case: Lewis v. United States">385 U. S. 206, 210</a></span> (1966). Thereafter, whatever possessory interest the seller had was in the funds, not the magazines. At the time of the sale the officer did not “interfere” with any interest of the seller; he took only that which was intended as a necessary part of the exchange. See <span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/#211" aria-description="Citation for case: Lewis v. United States"><em>id., </em>at 211</a></span>.</p>
<p id="b480-4"><page-number citation-index="1" label="470">*470</page-number>The use of undercover officers is essential to the enforcement of vice laws. <em>Id,., </em>at 210, n. 6. An undercover officer does not violate the Fourth Amendment merely by accepting an offer to do business that is freely made to the public. “A government agent, in the same manner as a private person, may accept an invitation to do business and may enter upon the premises for the very purposes contemplated by the occupant.” <span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/#211" aria-description="Citation for case: Lewis v. United States"><em>Id., </em>at 211</a></span>; cf. <em>Lo-Ji Sales, Inc. </em>v. <span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/#329" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York"><em>New York, supra, </em>at 329</a></span>. Nor does the First Amendment suggest a different conclusion in this case. Although a police officer may not engage in a “wholesale searc[h] and seizur[e]” in these circumstances, <em>Lo-Ji Sales, Inc. </em>v. <span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/#329" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York"><em>New York, supra, </em>at 329</a></span>, nothing in our cases renders invalid under the Fourth Amendment or the First Amendment the purchase as here by the police of a few of a large number of magazines and other materials offered for sale. The risk of prior restraint, which is the underlying basis for the special Fourth Amendment protections accorded searches for and seizures of First Amendment materials, does not come into play in such cases, and the purchase is analogous to purchases of other unlawful substances previously found not to violate the Fourth Amendment. See <em>Lewis </em>v. <em>United States, supra, </em>at 210 (purchase of narcotics).</p>
<p id="b480-5">Notwithstanding that the magazines were obtained by a purchase, respondent argues that the bona fide nature of the purchase evaporated when the officers later seized the marked $50 bill and failed to return the change. Brief for Respondent 10. When the officer subjectively intends to retrieve the money while retaining the magazines, respondent maintains, the purchase is tantamount to a warrantless seizure. <em>Id., </em>at 11. This argument cannot withstand scrutiny. Whether a Fourth Amendment violation has occurred “turns on an objective assessment of the officer’s actions in light of the facts and circumstances confronting him at the time,” <em>Scott </em>v. <em>United States, </em><span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#136" aria-description="Citation for case: Scott v. United States">436 U. S. 128, 136</a></span> (1978), and not on the officer’s actual state of mind at the time the chai-<page-number citation-index="1" label="471">*471</page-number>lenged action was taken. <em><span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/" aria-description="Citation for case: Scott v. United States">Id.,</a></span> </em>at 138 and 139, n. 13. Objectively viewed, the transaction was a sale in the ordinary course of business. The sale is not retrospectively transformed into a warrantless seizure by virtue of the officer’s subjective intent to retrieve the purchase money to use as evidence. Assuming, <em>arguendo, </em>that the retrieval of the money incident to the arrest was wrongful,'the proper remedy is restitution or suppression of the $50 bill as evidence of the purchase, not exclusion from evidence of the previously purchased magazines.</p>
<p id="b481-5">B</p>
<p id="b481-6">The question remains whether respondent’s warrantless arrest after the purchase of the magazines requires their exclusion at trial. Again, assuming, <em>arguendo, </em>that the war-rantless arrest was an unreasonable seizure in violation of the Fourth Amendment — a question we do not decide — it yielded nothing of evidentiary value that was not already in the lawful possession of the police. “The exclusionary rule enjoins the Government from benefiting from evidence it has unlawfully obtained; it does not reach backward to taint information that was in official hands prior to any illegality. ” <em>United States </em>v. <em>Crews, </em><span class="citation" data-id="9427838"><a href="/opinion/110230/united-states-v-crews/#475" aria-description="Citation for case: United States v. Crews">445 U. S., at 475</a></span> (opinion of Brennan, J., joined by Stewart, and Stevens, JJ.). Here, the magazines were in police possession before the arrest, and the $50 bill, the only fruit of the arrest, was not introduced in evidence. We leave to another day the question whether the Fourth Amendment prohibits a warrantless arrest for the state law misdemeanor of distribution of obscene materials.</p>
<p id="b481-7">Because the undercover agents did not obtain possession of the allegedly obscene magazines by means of an unreasonable search or seizure and the magazines were not the fruit of an arrest, lawful or otherwise, the magazines were properly admitted in evidence at respondent’s trial for distribution of obscene materials. The judgment of the Maryland Court of Special Appeals is reversed.</p>
<p id="b481-8">
<em>It is so ordered.</em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Maryland v. Pringle.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Maryland v. Pringle"
type: case
citation: "540 U.S. 366 (2003)"
parallel_cite: "124 S. Ct. 795; 157 L. Ed. 2d 769"
neutral_cite: 2003 U.S. LEXIS 9198
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2003
date_decided: 2003-12-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2003-12-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Maryland v. Pringle
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/131150/maryland-v-pringle/"
  cluster_id: 131150
  opinion_id: 131150
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Key — Progeny / Refinement"
related: ["[[Ybarra v. Illinois]]", "[[Illinois v. Gates]]", "[[Devenpeck v. Alford]]", "[[Brinegar v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "probable-cause", "arrest", "common-enterprise"]
holding: "Where drugs and cash are found in a car and no occupant claims them, an officer has probable cause to arrest all the occupants on a…"
lake:
  record_id: Maryland v. Pringle
  status: verified
  projected_at: 2026-07-06
---

# Maryland v. Pringle

*540 U.S. 366 (2003)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An officer stopped a car with three occupants at 3:16 a.m. and, with consent, found $763 of rolled-up cash in the glove compartment in front of Pringle (the front-seat passenger) and five baggies of cocaine behind the back-seat armrest, accessible to all three. None of the men admitted ownership of the drugs or money, so the officer arrested all three. Pringle later confessed and argued his arrest lacked probable cause.

## Issue
Whether an officer has probable cause to arrest a vehicle's occupant for possession of drugs found in the car when no occupant admits ownership and the drugs are accessible to all.

## Rule
Yes — the circumstances support a reasonable inference of common possession. "We think it an entirely reasonable inference from these facts that any or all three of the occupants had knowledge of, and exercised dominion and control over, the cocaine. Thus, a reasonable officer could conclude that there was probable cause to believe Pringle committed the crime of possession of cocaine, either solely or jointly." — 540 U.S. at 372. ^pin-372

## Application
Three men were riding together at night in a relatively small space with cash in front of Pringle and cocaine accessible to all of them, and none offered any information about who owned the drugs or money. From these facts an officer could reasonably infer that any or all of the occupants knowingly possessed the cocaine in a common enterprise. That inference supplied probable cause to arrest Pringle, distinguishing the case from mere guilt by association (as in *[[Ybarra v. Illinois|Ybarra]]*) where the suspect was a bystander in a public place.

## Conclusion
Reversed: the officer had probable cause to arrest Pringle for possession of the cocaine, so his arrest — and the confession that followed — were lawful.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Pringle* applies the totality-of-the-circumstances probable-cause standard ([[Illinois v. Gates]]; [[Brinegar v. United States]]) to a confined common-enterprise setting and distinguishes the bystander situation of [[Ybarra v. Illinois]]; it remains good law.

## Appears on
- [[Probable Cause]] — *Key — Progeny / Refinement*

## Sources
- *Maryland v. Pringle*, 540 U.S. 366 (2003) — https://www.courtlistener.com/opinion/131150/maryland-v-pringle/ — pinpoint: 372.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e7cdb46ce3d3dba6", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Maryland v. Pringle"}, "payload": {"all": [{"cite": "540 U.S. 366", "page": "366", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "540"}, {"cite": "124 S. Ct. 795", "page": "795", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "124"}, {"cite": "157 L. Ed. 2d 769", "page": "769", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "157"}, {"cite": "2003 U.S. LEXIS 9198", "page": "9198", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2003"}], "display": "540 U.S. 366", "official": {"cite": "540 U.S. 366", "page": "366", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "540"}, "official_selection_present": true, "record_id": "Maryland v. Pringle"}}
{"assertion_id": "38a51469ec3551ff", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-372", "record_id": "Maryland v. Pringle"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-372", "pinpoint_status": "slip-only", "quote": "--- # Maryland v. Pringle *540 U.S. 366 (2003)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An officer stopped a car with three occupants at 3:16 a.m. and, with consent, found $763 of rolled-up cash in the glove compartment in front of Pringle (the front-seat passenger) and five baggies of cocaine behind the back-seat armrest, accessible to all three. None of the men admitted ownership of the drugs or money, so the officer arrested all three. Pringle later confessed and argued his arrest lacked probable cause. ## Issue Whether an officer has probable cause to arrest a vehicle's occupant for possession of drugs found in the car when no occupant admits ownership and the drugs are accessible to all. ## Rule Yes — the circumstances support a reasonable inference of common possession.", "quote_fidelity": "mismatch", "record_id": "Maryland v. Pringle", "star_marker": null}}
{"assertion_id": "7998bc08369f0b52", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Maryland v. Pringle"}, "payload": {"as_of_content": "2003-12-15", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Maryland v. Pringle", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Maryland v. Pringle

```json
{
  "schema_version": "s2.v1",
  "record_id": "Maryland v. Pringle",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Maryland v. Pringle",
    "case_name_short": "Pringle",
    "case_name_full": "Maryland v. Pringle",
    "input_case_name": "Maryland v. Pringle",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2003-12-15",
    "year": 2003,
    "docket": null,
    "cluster_id": 131150,
    "lead_opinion_id": 131150,
    "sibling_ids": [
      131150
    ],
    "absolute_url": "/opinion/131150/maryland-v-pringle/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 131050,
        "score": 20,
        "case_name": "Maryland v. Pringle"
      },
      {
        "cluster_id": 128150,
        "score": 20,
        "case_name": "Maryland v. Pringle"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "540 U.S. 366",
      "volume": "540",
      "reporter": "U.S.",
      "page": "366",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "124 S. Ct. 795",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "795",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 769",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2003 U.S. LEXIS 9198",
        "volume": "2003",
        "reporter": "U.S. LEXIS",
        "page": "9198",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "540 U.S. 366",
        "volume": "540",
        "reporter": "U.S.",
        "page": "366",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 795",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "795",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 769",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2003 U.S. LEXIS 9198",
        "volume": "2003",
        "reporter": "U.S. LEXIS",
        "page": "9198",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "540 U.S. 366",
    "official_selection": {
      "court_class": "scotus",
      "selected": "540 U.S. 366",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-372",
      "page": null,
      "quote": "--- # Maryland v. Pringle *540 U.S. 366 (2003)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An officer stopped a car with three occupants at 3:16 a.m. and, with consent, found $763 of rolled-up cash in the glove compartment in front of Pringle (the front-seat passenger) and five baggies of cocaine behind the back-seat armrest, accessible to all three. None of the men admitted ownership of the drugs or money, so the officer arrested all three. Pringle later confessed and argued his arrest lacked probable cause. ## Issue Whether an officer has probable cause to arrest a vehicle's occupant for possession of drugs found in the car when no occupant admits ownership and the drugs are accessible to all. ## Rule Yes \u2014 the circumstances support a reasonable inference of common possession.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2003-12-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Maryland v. Pringle",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Louisiana v. K.B.",
          "cluster_id": 10581696,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Michael Hodges v. State of Indiana",
          "cluster_id": 4633575,
          "cite": [
            "125 N.E.3d 578"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane1_negative"
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
        "journal_ref": "Maryland v. Pringle:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Knight",
          "cluster_id": 4499332,
          "cite": [
            "419 P.3d 637",
            "55 Kan. App. 2d 642"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane1_negative"
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
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Devenpeck v. Alford",
          "cluster_id": 137733,
          "cite": [
            "160 L. Ed. 2d 537",
            "125 S. Ct. 588",
            "543 U.S. 146",
            "2004 U.S. LEXIS 8272"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Pigford",
          "cluster_id": 1694070,
          "cite": [
            "922 So. 2d 517",
            "2006 WL 408710"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Harris",
          "cluster_id": 820744,
          "cite": [
            "185 L. Ed. 2d 61",
            "133 S. Ct. 1050",
            "568 U.S. 237",
            "2013 U.S. LEXIS 1121"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Laura Skop v. City of Atlanta, Georgia",
          "cluster_id": 77695,
          "cite": [
            "485 F.3d 1130",
            "2007 U.S. App. LEXIS 10341",
            "2007 WL 1288012"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460811,
          "cite": [
            "583 U.S. 48"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
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
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Byron Halsey v. Frank Pfeiffer",
          "cluster_id": 2671183,
          "cite": [
            "750 F.3d 273",
            "2014 WL 1622769",
            "2014 U.S. App. LEXIS 7696"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
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
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Perea",
          "cluster_id": 2640415,
          "cite": [
            "126 P.3d 241",
            "2005 Colo. App. LEXIS 1207",
            "2005 WL 1773880"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rodriguez v. State",
          "cluster_id": 1685476,
          "cite": [
            "232 S.W.3d 55",
            "2007 Tex. Crim. App. LEXIS 624",
            "2007 WL 1343066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Amador v. State",
          "cluster_id": 1450770,
          "cite": [
            "275 S.W.3d 872",
            "2009 Tex. Crim. App. LEXIS 4",
            "2009 WL 80204"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Scott",
          "cluster_id": 844257,
          "cite": [
            "257 P.3d 703",
            "52 Cal. 4th 452",
            "129 Cal. Rptr. 3d 91",
            "2011 Cal. LEXIS 8086"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
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
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ball",
          "cluster_id": 1742701,
          "cite": [
            "710 N.W.2d 592",
            "271 Neb. 140",
            "2006 Neb. LEXIS 37"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "A.M. Ex Rel. F.M. v. Holmes",
          "cluster_id": 4241340,
          "cite": [
            "830 F.3d 1123"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
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
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Pineiro",
          "cluster_id": 1980861,
          "cite": [
            "853 A.2d 887",
            "181 N.J. 13",
            "2004 N.J. LEXIS 931"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Thompson",
          "cluster_id": 2056760,
          "cite": [
            "985 A.2d 928",
            "604 Pa. 198",
            "2009 Pa. LEXIS 2793"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Price v. Sery",
          "cluster_id": 1272546,
          "cite": [
            "513 F.3d 962",
            "2008 U.S. App. LEXIS 1196",
            "2008 WL 170205"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Omar Paez v. Claudia Mulvey",
          "cluster_id": 4588729,
          "cite": [
            "915 F.3d 1276"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Brady",
          "cluster_id": 2387577,
          "cite": [
            "236 P.3d 312",
            "50 Cal. 4th 547",
            "113 Cal. Rptr. 3d 458",
            "2010 Cal. LEXIS 7625"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Freeman",
          "cluster_id": 3159439,
          "cite": [
            "128 A.3d 1231",
            "2015 Pa. Super. 252",
            "2015 Pa. Super. LEXIS 783",
            "2015 WL 7756864"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William Hawkins v. Rodney Mitchell",
          "cluster_id": 2708520,
          "cite": [
            "756 F.3d 983",
            "2014 WL 2808981",
            "2014 U.S. App. LEXIS 11906"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jones",
          "cluster_id": 2820294,
          "cite": [
            "121 A.3d 524",
            "2015 Pa. Super. 160",
            "2015 Pa. Super. LEXIS 424",
            "2015 WL 4503123"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Pringle:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(131150) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDk1NTg0MDAwMDAwJnM9NDM5NDExNCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28131150%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(131150)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTUmcz0zMTc2OTgwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28131150%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(131150)",
        "reviewed": 102,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 102,
        "triage_read": 1,
        "triage_snippet_classified": 101
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(131150)",
    "indexed_citing_opinions": 833,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 131150,
        "count": 833,
        "count_source": "search"
      }
    ],
    "citation_count": 1614,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/maryland-v-pringle.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNDE5ODYmcz0xMDU4MTY5NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28131150%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 131150,
        "cited_id": 85007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131150,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131150,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131150,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131150,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131150,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131150,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131150,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131150,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131150,
        "cited_id": 118277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131150,
        "cited_id": 1435281,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131150,
        "cited_id": 2376130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131150,
        "cited_id": 2620702,
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
    "date_created": "2026-07-05T12:09:02Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T12:09:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T12:09:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T12:12:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T12:09:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Maryland v. Pringle

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b579-11">
  Chief Justice Rehnquist
 </author>
<p id="ASqr">
  delivered the opinion of the Court.
 </p>
<p id="b579-12">
  In the early morning hours a passenger car occupied by three men was stopped for speeding by a police officer. The
  <span citation-index="1" class="star-pagination" label="368"> 
   *368
   </span>
  officer, upon searching the ear, seized $763 of rolled-up cash from the glove compartment and five glassine baggies of cocaine from between the back-seat armrest and the back seat. After all three men denied ownership of the cocaine and money, the officer arrested each of them. We hold that the officer had probable cause to arrest Pringle — one of the three men.
 </p>
<p id="b580-5">
  At 3:16 a.m. on August 7,1999, a Baltimore County Police officer stopped a Nissan Maxima for speeding. There were three occupants in the car: Donte Partlow, the driver and owner, respondent Pringle, the front-seat passenger, and Otis Smith, the back-seat passenger. The officer asked Partlow for his license and registration. When Partlow opened the glove compartment to retrieve the vehicle registration, the officer observed a large amount of rolled-up money in the glove compartment. The officer returned to his patrol car with Partlow’s license and registration to check the computer system for outstanding violations. The computer check did not reveal any violations. The officer returned to the stopped car, had Partlow get out, and issued him an oral warning.
 </p>
<p id="b580-6">
  After a second patrol car arrived, the officer asked Partlow if he had any weapons or narcotics in the vehicle. Partlow indicated that he did not. Partlow then consented to a search of the vehicle. The search yielded $763 from the glove compartment and five plastic glassine baggies containing cocaine from behind the back-seat armrest. When the officer began the search the armrest was in the upright position flat against the rear seat. The officer pulled down the armrest and found the drugs, which had been placed between the armrest and the back seat of the car.
 </p>
<p id="b580-7">
  The officer questioned all three men about the ownership of the drugs and money, and told them that if no one admitted to ownership of the drugs he was going to arrest them all. The men offered no information regarding the owner
  <span citation-index="1" class="star-pagination" label="369"> 
   *369
   </span>
  ship of the drugs or money. All three were placed under arrest and transported to the police station.
 </p>
<p id="b581-5">
  Later that morning, Pringle waived his rights under
  <em>
   Miranda
  </em>
  v.
  <em>
   Arizona,
  </em>
  <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and gave an oral and written confession in which he acknowledged that the cocaine belonged to him, that he and his friends were going to a party, and that he intended to sell the cocaine or “[u]se it for sex.” App. 26. Pringle maintained that the other occupants of the car did not know about the drugs, and they were released.
 </p>
<p id="b581-6">
  The trial court denied Pringle’s motion to suppress his confession as the fruit of an illegal arrest, holding that the officer had probable cause to arrest Pringle. A jury convicted Pringle of possession with intent to distribute cocaine and possession of cocaine. He was sentenced to 10 years’ incarceration without the possibility of parole. The Court of Special Appeals of Maryland affirmed. <span class="citation" data-id="2376130"><a href="/opinion/2376130/pringle-v-state/" aria-description="Citation for case: Pringle v. State">141 Md. App. 292</a></span>, <span class="citation" data-id="2376130"><a href="/opinion/2376130/pringle-v-state/" aria-description="Citation for case: Pringle v. State">785 A. 2d 790</a></span> (2001).
 </p>
<p id="b581-7">
  The Court of Appeals of Maryland, by divided vote, reversed, holding that, absent specific facts tending to show Pringle’s knowledge and dominion or control over the drugs, “the mere finding of cocaine in the back armrest when [Prin-gle] was a front seat passenger in a car being driven by its owner is insufficient to establish probable cause for an arrest for possession.” <span class="citation" data-id="9629409"><a href="/opinion/1435281/pringle-v-state/#545" aria-description="Citation for case: Pringle v. State">370 Md. 525, 545</a></span>, <span class="citation" data-id="9629409"><a href="/opinion/1435281/pringle-v-state/#1027" aria-description="Citation for case: Pringle v. State">805 A. 2d 1016, 1027</a></span> (2002). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./538/921/">538 U. S. 921</a></span> (2003), and now reverse.
 </p>
<p id="b581-8">
  Under the Fourth Amendment, made applicable to the States by the Fourteenth Amendment,
  <em>
   Mapp
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), the people are “to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, . . . and no Warrants shall issue, but upon probable cause ....” U. S. Const., Arndt. 4. Maryland law authorizes police officers to execute warrantless arrests,
  <em>
   inter alia,
  </em>
  for felonies committed in an officer’s presence or where an officer has probable cause to believe that a felony
  <span citation-index="1" class="star-pagination" label="370"> 
   *370
   </span>
  has been committed or is being committed in the officer’s presence. Md. Ann. Code, Art. 27, §594B (1996) (repealed 2001). A warrantless arrest of an individual in a public place for a felony, or a misdemeanor committed in the officer’s presence, is consistent with the Fourth Amendment if the arrest is supported by probable cause.
  <em>
   United States
  </em>
  v.
  <em>
   Watson,
  </em>
  <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#424" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 424</a></span> (1976); see
  <em>
   Atwater
  </em>
  v.
  <em>
   Lago Vista,
  </em>
  <span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/#354" aria-description="Citation for case: Atwater v. City of Lago Vista">532 U. S. 318, 354</a></span> (2001) (stating that “[i]f an officer has probable cause to believe that an individual has committed even a very minor criminal offense in his presence, he may, without violating the Fourth Amendment, arrest the offender”).
 </p>
<p id="b582-5">
  It is uncontested in the present case that the officer, upon recovering the five plastic glassine baggies containing suspected cocaine, had probable cause to believe a felony had been committed. Md. Ann. Code, Art. 27, §287 (1996) (repealed 2002) (prohibiting possession of controlled dangerous substances). The sole question is whether the officer had probable cause to believe that Pringle committed that crime.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
</p>
<p id="b582-6">
  The long-prevailing standard of probable cause protects “citizens from rash and unreasonable interferences with privacy and from unfounded charges of crime,” while giving “fair leeway for enforcing the law in the community’s protection.”
  <em>
   Brinegar
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949). On many occasions, we have reiterated that the probable-cause standard is a “‘practical, nontechnical conception’” that deals with “ ‘the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act.’ ”
  <em>
   Illinois
  </em>
  v.
  <em>
   Gates,
  </em>
  <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#231" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 231</a></span> (1983) (quoting
  <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States"><em>
   Brinegar, supra,
  </em>
  at 175-176</a></span>); see,
  <em>
   e. g., Ornelas
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#695" aria-description="Citation for case: Ornelas v. United States">517 U. S. 690, 695</a></span> (1996);
  <em>
   United States
  </em>
  v.
  <em>
   Sokolow,
  </em>
  <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#7" aria-description="Citation for case: United States v. Sokolow">490 U. S. 1, 7-8</a></span> (1989). “[P]robable cause is a fluid
  <span citation-index="1" class="star-pagination" label="371"> 
   *371
   </span>
  concept — turning on the assessment of probabilities in particular factual contexts — not readily, or even usefully, reduced to a neat set of legal rules.”
  <em>
   Gates,
  </em>
  <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#232" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 232</a></span>.
 </p>
<p id="b583-5">
  The probable-cause standard is incapable of precise definition or quantification into percentages because it deals with probabilities and depends on the totality of the circumstances. See
  <em>
   ibid.; Brinegar,
  </em>
  <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S., at 175</a></span>. We have stated, however, that “[t]he substance of all the definitions of probable cause is a reasonable ground for belief of guilt,”
  <em>
   ibid,
  </em>
  (internal quotation marks and citations omitted), and that the belief of guilt must be particularized with respect to the person to be searched or seized,
  <em>
   Ybarra
  </em>
  v.
  <em>
   Illinois,
  </em>
  <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/#91" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85, 91</a></span> (1979). In
  <em>
   Illinois
  </em>
  v.
  <em>
   <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Gates</a></span>,
  </em>
  we noted:
 </p>
<blockquote id="b583-6">
  “As early as
  <em>
   Locke
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/#348" aria-description="Citation for case: Locke v. United States">7 Cranch 339, 348</a></span> (1813), Chief Justice Marshall observed, in a closely related context: ‘[T]he term “probable cause,” according to its usual acceptation, means less than evidence which would justify condemnation .... It imports a seizure made under circumstances which warrant suspicion.’ More recently, we said that ‘the
  <em>
   quanta
  </em>
  ... of proof’ appropriate in ordinary judicial proceedings are inapplicable to the decision to issue a warrant.
  <em>
   Brinegar,
  </em>
  <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#173" aria-description="Citation for case: Brinegar v. United States">338 U. S., at 173</a></span>. Finely tuned standards such as proof beyond a reasonable doubt or by a preponderance of the evidence, useful in
  <em>
   formal trials, have no place in the
  </em>
  [probable-cause] decision.” <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#235" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 235</a></span>.
 </blockquote>
<p id="b583-9">
  To determine whether an officer had probable cause to arrest an individual, we examine the events leading up to the arrest, and then decide “whether these historical facts, viewed from the standpoint of an objectively reasonable police officer, amount to” probable cause,
  <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#696" aria-description="Citation for case: Ornelas v. United States"><em>
   Ornelas, supra,
  </em>
  at 696</a></span>.
 </p>
<p id="b583-10">
  In this case, Pringle was one of three men riding in a Nissan Maxima at 3:16 a.m. There was $763 of rolled-up cash
  <span citation-index="1" class="star-pagination" label="372"> 
   *372
   </span>
  in the glove compartment directly in front of Pringle.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  Five plastic glassine baggies of cocaine were behind the back-seat armrest and accessible to all three men. Upon questioning, the three men failed to offer any information with respect to the ownership of the cocaine or the money.
 </p>
<p id="b584-4">
  We think it an entirely reasonable inference from these facts that any or all three of the occupants had knowledge, of, and exercised dominion and control over, the cocaine. Thus, a reasonable officer could conclude that there was probable cause to believe Pringle committed the crime of possession of cocaine, either solely or jointly.
 </p>
<p id="b584-5">
  Pringle’s attempt to characterize this case as a guilt-by-association case is unavailing. His reliance on
  <em>
   Ybarra
  </em>
  v.
  <em>
   Illinois, supra,
  </em>
  and
  <em>
   United States
  </em>
  v.
  <em>
   Di Re,
  </em>
  <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/" aria-description="Citation for case: United States v. Di Re">332 U. S. 581</a></span> (1948), is misplaced. In
  <em>
   <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">Ybarra</a></span>,
  </em>
  police officers obtained a warrant to search a tavern and its bartender for evidence of possession of a controlled substance. Upon entering the tavern, the officers conducted patdown searches of the customers present in the tavern, including Ybarra. Inside a cigarette pack retrieved from Ybarra’s pocket, an officer found six tinfoil packets containing heroin. We stated:
 </p>
<blockquote id="b584-6">
  “[A] person’s mere propinquity to others independently suspected of criminal activity does not, without more,
  <span citation-index="1" class="star-pagination" label="373"> 
   *373
   </span>
  give rise to probable cause to search that person.
  <em>
   Sibron
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#62" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 62-63</a></span> (1968). Where the standard is probable cause, a search or seizure of a person must be supported by probable cause particularized with respect to that person. This requirement cannot be undercut or avoided by simply pointing to the fact that coincidentally there exists probable cause to search or seize another or to search the premises where the person may happen to be.” <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/#91" aria-description="Citation for case: Ybarra v. Illinois">444 U. S., at 91</a></span>.
 </blockquote>
<p id="b585-5">
  We held that the search warrant did not permit body searches of all of the tavern’s patrons and that the police could not pat down the patrons for weapons, absent individualized suspicion.
  <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/#92" aria-description="Citation for case: Ybarra v. Illinois"><em>
   Id.,
  </em>
  at 92</a></span>.
 </p>
<p id="b585-6">
  This case is quite different from
  <em>
   <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">Ybarra</a></span>.
  </em>
  Pringle and his two companions were in a relatively small automobile, not a public tavern. In
  <em>
   Wyoming
  </em>
  v.
  <em>
   Houghton,
  </em>
  <span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/" aria-description="Citation for case: Wyoming v. Houghton">526 U. S. 295</a></span> (1999), we noted that “a car passenger — unlike the unwitting tavern patron in
  <em>
   <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">Ybarra</a></span>
  </em>
  — will often be engaged in a common enterprise with the driver, and have the same interest in concealing the fruits or the evidence of their wrongdoing.”
  <em>
   Id.,
  </em>
  at 304-305. Here we think it was reasonable for the officer to infer a common enterprise among the three men. The quantity of drugs and cash in the car indicated the likelihood of drug dealing, an enterprise to which a dealer would be unlikely to admit an innocent person with the potential to furnish evidence against him. In
  <em>
   Di Re,
  </em>
  a federal investigator had been told by an informant, Reed, that he was to receive counterfeit gasoline ration coupons from a certain Buttitta at a particular place. The investigator went to the appointed place and saw Reed, the sole occupant of the rear seat of the car, holding gasoline ration coupons. There were two other occupants in the car: Buttitta in the driver’s seat and Di Re in the front passenger’s seat. Reed informed the investigator that Buttitta had given him counterfeit coupons. Thereupon, all three men were arrested and searched. After noting that the officers had no information implicating
  <span citation-index="1" class="star-pagination" label="374"> 
   *374
   </span>
  Di Re and no information pointing to Di Re’s possession of coupons, unless presence in the car warranted that inference, we concluded that the officer lacked probable cause to believe that Di Re was involved in the crime. <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#592" aria-description="Citation for case: United States v. Di Re">332 U. S., at 592-594</a></span>. We said “[a]ny inference that everyone on the scene of a crime is a party to it must disappear if the Government informer singles out the guilty person.”
  <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#594" aria-description="Citation for case: United States v. Di Re"><em>
   Id.,
  </em>
  at 594</a></span>. No such singling out occurred in this ease; none of the three men provided information with respect to the ownership of the cocaine or money.
 </p>
<p id="b586-5">
  We hold that the officer had probable cause to believe that Pringle had committed the crime of possession of a controlled substance. Pringle’s arrest therefore did not contravene the Fourth and Fourteenth Amendments. Accordingly, the judgment of the Court of Appeals of Maryland is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.
 </p>
<p id="b586-6">
<em>
   It is so ordered.
  </em>
</p>


<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b582-7">
   Maryland law defines “possession” as “the exercise of actual or constructive dominion or control over a thing by one or more persons.” Md. Ann. Code, Art. 27, § 277(s) (1996) (repealed 2002).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b584-7">
   The Court of Appeals of Maryland dismissed the $763 seized from the glove compartment as a factor in the probable-cause determination, stating that “[m]oney, without more, is innocuous.” <span class="citation" data-id="9629429"><a href="/opinion/1435335/muthukumarana-v-montgomery-county/#546" aria-description="Citation for case: Muthukumarana v. Montgomery County">370 Md. 524, 546</a></span>, <span class="citation" data-id="9629409"><a href="/opinion/1435281/pringle-v-state/#1028" aria-description="Citation for case: Pringle v. State">805 A. 2d 1016, 1028</a></span> (2002). The court’s consideration of the money in isolation, rather than as a factor in the totality of the circumstances, is mistaken in light of our precedents. See,
   <em>
    e. g., Illinois
   </em>
   v.
   <em>
    Gates,
   </em>
   <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#230" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 230-231</a></span> (1983) (opining that the totality of the circumstances approach is consistent with our prior treatment of probable cause);
   <em>
    Brinegar
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175-176</a></span> (1949) (“Probable cause exists where ‘the facts and circumstances within their [the officers’] knowledge and of which they had reasonably trustworthy information [are] sufficient in themselves to warrant a man of reasonable caution in the belief that’ an offense has been or is being committed”). We think it is abundantly clear from the facts that this case involves more than money alone.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Maryland v. Shatzer.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Maryland v. Shatzer"
type: case
citation: "559 U.S. 98 (2010)"
parallel_cite: "130 S. Ct. 1213; 175 L. Ed. 2d 1045"
neutral_cite: 2010 U.S. LEXIS 1899
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2010
date_decided: 2010-02-24
docket: 08-680
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2010-02-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Maryland v. Shatzer
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/1734/maryland-v-shatzer/"
  cluster_id: 1734
  opinion_id: 1734
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Edwards v. Arizona]]", "[[Arizona v. Roberson]]", "[[Minnick v. Mississippi]]", "[[Berghuis v. Thompkins]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "edwards-rule", "break-in-custody", "reinterrogation"]
holding: "Edwards protection ends after a 14-day break in Miranda custody; once 14 days pass, police may re-approach and seek a fresh waiver.…"
lake:
  record_id: Maryland v. Shatzer
  status: verified
  projected_at: 2026-07-06
---

# Maryland v. Shatzer

*559 U.S. 98 (2010)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A detective tried to question Shatzer, then a prison inmate, about allegations he had abused his son; Shatzer invoked his *[[Miranda v. Arizona|Miranda]]* right to counsel, and the interview ended. Shatzer remained in the general prison population. Nearly three years later, a different detective reopened the investigation, gave fresh *[[Miranda v. Arizona|Miranda]]* warnings, obtained a waiver, and Shatzer made incriminating statements. He argued *[[Edwards v. Arizona]]* barred the later interrogation.

## Issue
Whether the *[[Edwards v. Arizona|Edwards]]* prohibition on police-initiated reinterrogation after a suspect invokes counsel ends when there is a break in *[[Miranda v. Arizona|Miranda]]* custody, and if so, how long the break must be — and whether release back into the general prison population counts as such a break.

## Rule
The *[[Edwards v. Arizona|Edwards]]* presumption is not eternal; a sufficient break in custody ends it, and the Court fixed the period at 14 days: "It seems to us that period is 14 days. That provides plenty of time for the suspect to get reacclimated to his normal life, to consult with friends and counsel, and to shake off any residual coercive effects of his prior custody." — *Maryland v. Shatzer*, 559 U.S. 98 (2010) (slip op., at 11). ^pin-op11

The Court further held that release back into the general prison population constitutes a break in *[[Miranda v. Arizona|Miranda]]* custody, because lawful imprisonment on a conviction does not impose the coercive pressures of investigative custody that justify *[[Edwards v. Arizona|Edwards]]*.

## Application
After Shatzer invoked counsel, he was returned to the general prison population — his accustomed surroundings and routine — which the Court treated as a break in *[[Miranda v. Arizona|Miranda]]* custody that dissipated the coercive pressures *[[Edwards v. Arizona|Edwards]]* guards against. Because far more than 14 days (about two and a half years) elapsed before the second, separately *Mirandized* interrogation, the *[[Edwards v. Arizona|Edwards]]* presumption no longer applied, and Shatzer's later waiver and statements were admissible.

## Conclusion
Reversed: a 14-day break in *[[Miranda v. Arizona|Miranda]]* custody ends the *[[Edwards v. Arizona|Edwards]]* bar, and return to the general prison population is such a break; Shatzer's statements were not subject to suppression under *[[Edwards v. Arizona|Edwards]]*.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Shatzer* refines [[Edwards v. Arizona]] (and its companions [[Arizona v. Roberson]] and [[Minnick v. Mississippi]]) by adding a break-in-custody limit and a bright-line 14-day period; it remains good law.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *Maryland v. Shatzer*, 559 U.S. 98 (2010) — https://www.courtlistener.com/opinion/1734/maryland-v-shatzer/ — pinpoint given as slip-opinion page (slip op., at 11); CourtListener carries the slip opinion, paginated by slip page (opinion 1734).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6bfb09a4964c505b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Maryland v. Shatzer"}, "payload": {"all": [{"cite": "559 U.S. 98", "page": "98", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "559"}, {"cite": "130 S. Ct. 1213", "page": "1213", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "130"}, {"cite": "175 L. Ed. 2d 1045", "page": "1045", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "175"}, {"cite": "2010 U.S. LEXIS 1899", "page": "1899", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2010"}], "display": "559 U.S. 98", "official": {"cite": "559 U.S. 98", "page": "98", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "559"}, "official_selection_present": true, "record_id": "Maryland v. Shatzer"}}
{"assertion_id": "1c343debf32bca08", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op11", "record_id": "Maryland v. Shatzer"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op11", "pinpoint_status": "slip-only", "quote": "--- # Maryland v. Shatzer *559 U.S. 98 (2010)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A detective tried to question Shatzer, then a prison inmate, about allegations he had abused his son; Shatzer invoked his *Miranda* right to counsel, and the interview ended. Shatzer remained in the general prison population. Nearly three years later, a different detective reopened the investigation, gave fresh *Miranda* warnings, obtained a waiver, and Shatzer made incriminating statements. He argued *Edwards v. Arizona* barred the later interrogation. ## Issue Whether the *Edwards* prohibition on police-initiated reinterrogation after a suspect invokes counsel ends when there is a break in *Miranda* custody, and if so, how long the break must be — and whether release back into the general prison population counts as such a break. ## Rule The *Edwards* presumption is not eternal; a sufficient break in custody ends it, and the Court fixed the period at 14 days:", "quote_fidelity": "mismatch", "record_id": "Maryland v. Shatzer", "star_marker": null}}
{"assertion_id": "5c126ba11a534cd7", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Maryland v. Shatzer"}, "payload": {"as_of_content": "2010-02-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Maryland v. Shatzer", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Maryland v. Shatzer

```json
{
  "schema_version": "s2.v1",
  "record_id": "Maryland v. Shatzer",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Maryland v. Shatzer",
    "case_name_short": "Shatzer",
    "case_name_full": "Maryland v. Shatzer",
    "input_case_name": "Maryland v. Shatzer",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2010-02-24",
    "year": 2010,
    "docket": "08-680",
    "cluster_id": 1734,
    "lead_opinion_id": 1734,
    "sibling_ids": [
      1734,
      9413177,
      9413178,
      9413179
    ],
    "absolute_url": "/opinion/1734/maryland-v-shatzer/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "559 U.S. 98",
      "volume": "559",
      "reporter": "U.S.",
      "page": "98",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "130 S. Ct. 1213",
        "volume": "130",
        "reporter": "S. Ct.",
        "page": "1213",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "175 L. Ed. 2d 1045",
        "volume": "175",
        "reporter": "L. Ed. 2d",
        "page": "1045",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2010 U.S. LEXIS 1899",
        "volume": "2010",
        "reporter": "U.S. LEXIS",
        "page": "1899",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "559 U.S. 98",
        "volume": "559",
        "reporter": "U.S.",
        "page": "98",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "130 S. Ct. 1213",
        "volume": "130",
        "reporter": "S. Ct.",
        "page": "1213",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "175 L. Ed. 2d 1045",
        "volume": "175",
        "reporter": "L. Ed. 2d",
        "page": "1045",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 U.S. LEXIS 1899",
        "volume": "2010",
        "reporter": "U.S. LEXIS",
        "page": "1899",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "559 U.S. 98",
    "official_selection": {
      "court_class": "scotus",
      "selected": "559 U.S. 98",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op11",
      "page": null,
      "quote": "--- # Maryland v. Shatzer *559 U.S. 98 (2010)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A detective tried to question Shatzer, then a prison inmate, about allegations he had abused his son; Shatzer invoked his *Miranda* right to counsel, and the interview ended. Shatzer remained in the general prison population. Nearly three years later, a different detective reopened the investigation, gave fresh *Miranda* warnings, obtained a waiver, and Shatzer made incriminating statements. He argued *Edwards v. Arizona* barred the later interrogation. ## Issue Whether the *Edwards* prohibition on police-initiated reinterrogation after a suspect invokes counsel ends when there is a break in *Miranda* custody, and if so, how long the break must be \u2014 and whether release back into the general prison population counts as such a break. ## Rule The *Edwards* presumption is not eternal; a sufficient break in custody ends it, and the Court fixed the period at 14 days:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2010-02-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Maryland v. Shatzer",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Iowa v. Michael Hillery",
          "cluster_id": 4868029,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Michael Hillery",
          "cluster_id": 4865672,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Barksdale",
          "cluster_id": 4867083,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hinshaw",
          "cluster_id": 4545610,
          "cite": [
            "2018 Ohio 4226",
            "120 N.E.3d 514"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hallford",
          "cluster_id": 4444995,
          "cite": [
            "280 F. Supp. 3d 170"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hammonds",
          "cluster_id": 4430449,
          "cite": [
            "804 S.E.2d 438",
            "370 N.C. 158",
            "2017 WL 4322423",
            "2017 N.C. LEXIS 702"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. MacDonald",
          "cluster_id": 5309859,
          "cite": [
            "2017 UT App 124",
            "402 P.3d 91",
            "844 Utah Adv. Rep. 90",
            "2017 WL 3224516",
            "2017 Utah App. LEXIS 124"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "NYIA GORE v. UNITED STATES",
          "cluster_id": 4248978,
          "cite": [
            "145 A.3d 540",
            "2016 D.C. App. LEXIS 313",
            "2016 WL 4411321"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jovan'z Smith v. Ken Clark",
          "cluster_id": 3134205,
          "cite": [
            "804 F.3d 983",
            "2015 U.S. App. LEXIS 18335",
            "2015 WL 6387862"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane1_negative"
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
        "journal_ref": "Maryland v. Shatzer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Ledbetter",
          "cluster_id": 6294956,
          "cite": [
            "47 Misc. 3d 336",
            "998 N.Y.S.2d 286"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Burgos",
          "cluster_id": 2754022,
          "cite": [
            "470 Mass. 133",
            "19 N.E.3d 843"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Taylor",
          "cluster_id": 7306221,
          "cite": [
            "17 F. Supp. 3d 162",
            "2014 WL 1653194",
            "2014 U.S. Dist. LEXIS 57397"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane1_negative"
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
        "journal_ref": "Maryland v. Shatzer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Arizona v. David James Yonkman",
          "cluster_id": 2688514,
          "cite": [
            "233 Ariz. 369",
            "312 P.3d 1135"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tennison M. Silver",
          "cluster_id": 903129,
          "cite": [
            "155 Idaho 29",
            "304 P.3d 304",
            "2013 WL 2996126",
            "2013 Ida. App. LEXIS 56"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane1_negative"
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
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
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
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gamache",
          "cluster_id": 2523859,
          "cite": [
            "48 Cal. 4th 347",
            "227 P.3d 342",
            "106 Cal. Rptr. 3d 771",
            "2010 Cal. LEXIS 1914"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
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
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
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
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Martin",
          "cluster_id": 2445914,
          "cite": [
            "5 A.3d 177",
            "607 Pa. 165",
            "2010 Pa. LEXIS 2866"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
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
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
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
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Woodard, A., Aplt.",
          "cluster_id": 3159995,
          "cite": [
            "129 A.3d 480",
            "634 Pa. 162",
            "2015 Pa. LEXIS 2786",
            "2015 WL 7767271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
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
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Thomas",
          "cluster_id": 844168,
          "cite": [
            "54 Cal. 4th 908",
            "281 P.3d 361",
            "144 Cal. Rptr. 3d 366",
            "2012 WL 3043901",
            "2012 Cal. LEXIS 7089"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. David Hooper Climer, Jr.",
          "cluster_id": 1043889,
          "cite": [
            "400 S.W.3d 537",
            "2013 WL 1694804",
            "2013 Tenn. LEXIS 354"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Contreras",
          "cluster_id": 4471023,
          "cite": [
            "229 Cal. Rptr. 3d 249",
            "411 P.3d 445",
            "4 Cal. 5th 349"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Keaton",
          "cluster_id": 2301803,
          "cite": [
            "45 A.3d 1050",
            "615 Pa. 675"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vega v. Tekoh",
          "cluster_id": 6480695,
          "cite": [
            "597 U.S. 134",
            "213 L. Ed. 2d 479",
            "142 S. Ct. 2095"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hughes",
          "cluster_id": 214334,
          "cite": [
            "640 F.3d 428",
            "2011 U.S. App. LEXIS 7338",
            "2011 WL 1332061"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Zyriah Henry Floyd Schlitter",
          "cluster_id": 3212050,
          "cite": [
            "881 N.W.2d 380",
            "2016 Iowa Sup. LEXIS 70"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Krebs",
          "cluster_id": 4680693,
          "cite": [
            "452 P.3d 609",
            "255 Cal. Rptr. 3d 95",
            "8 Cal. 5th 265"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Elliott",
          "cluster_id": 2712696,
          "cite": [
            "494 Mich. 292",
            "833 N.W.2d 284",
            "2013 WL 3198007",
            "2013 Mich. LEXIS 938"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Robert Dale Lowe, Jr.",
          "cluster_id": 4472370,
          "cite": [
            "812 N.W.2d 554",
            "2012 Iowa Sup. LEXIS 8"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Molano",
          "cluster_id": 6240586,
          "cite": [
            "249 Cal. Rptr. 3d 1",
            "7 Cal. 5th 620",
            "443 P.3d 856"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tizon v. Commonwealth",
          "cluster_id": 1061710,
          "cite": [
            "723 S.E.2d 260",
            "60 Va. App. 1",
            "2012 WL 1080167",
            "2012 Va. App. LEXIS 105"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Nelson",
          "cluster_id": 844227,
          "cite": [
            "266 P.3d 1008",
            "53 Cal. 4th 367",
            "135 Cal. Rptr. 3d 312",
            "2012 Cal. LEXIS 4",
            "2012 WL 88552"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Straker",
          "cluster_id": 2832658,
          "cite": [
            "419 U.S. App. D.C. 210",
            "800 F.3d 570",
            "2015 WL 5099548"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Barnes",
          "cluster_id": 4498370,
          "cite": [
            "890 F.3d 910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Shatzer:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(1734 OR 9413177 OR 9413178 OR 9413179) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzYwMjgxNjAwMDAwJnM9MjY5MjQwMSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%281734+OR+9413177+OR+9413178+OR+9413179%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 16,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 16,
        "triage_snippet_classified": 184
      },
      "lane2_top_cited": {
        "query": "cites:(1734 OR 9413177 OR 9413178 OR 9413179)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNiZzPTQ0NzI0MDAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%281734+OR+9413177+OR+9413178+OR+9413179%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(1734 OR 9413177 OR 9413178 OR 9413179)",
        "reviewed": 34,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 34,
        "triage_read": 0,
        "triage_snippet_classified": 34
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(1734 OR 9413177 OR 9413178 OR 9413179)",
    "indexed_citing_opinions": 323,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 1734,
        "count": 254,
        "count_source": "search"
      },
      {
        "opinion_id": 9413177,
        "count": 72,
        "count_source": "search"
      },
      {
        "opinion_id": 9413178,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9413179,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 624,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/maryland-v-shatzer.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2MjYxNDUmcz05NDYxNDI3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%281734+OR+9413177+OR+9413178+OR+9413179%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 1734,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9422839,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9423233,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9423682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9423752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9423964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9424967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9425988,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9426230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9427635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9428324,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9429286,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9429516,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9429664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9429728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9429796,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9429912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9430407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9431349,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9431404,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9431937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9432050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9432151,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9432173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9432264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9432329,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9432992,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9433017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9433984,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9434063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9434450,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9434686,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9699927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9749372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9782269,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9842071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1734,
        "cited_id": 9842121,
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
    "date_created": "2026-07-05T12:12:56Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T12:13:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T12:13:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T12:16:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T12:13:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Maryland v. Shatzer

```
(Slip Opinion)              OCTOBER TERM, 2009                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                        MARYLAND v. SHATZER

     CERTIORARI TO THE COURT OF APPEALS OF MARYLAND

   No. 08–680.      Argued October 5, 2009—Decided February 24, 2010
In 2003, a police detective tried to question respondent Shatzer, who
  was incarcerated at a Maryland prison pursuant to a prior conviction,
  about allegations that he had sexually abused his son. Shatzer in
  voked his Miranda right to have counsel present during interroga
  tion, so the detective terminated the interview. Shatzer was released
  back into the general prison population, and the investigation was
  closed. Another detective reopened the investigation in 2006 and at
  tempted to interrogate Shatzer, who was still incarcerated. Shatzer
  waived his Miranda rights and made inculpatory statements. The
  trial court refused to suppress those statements, reasoning that Ed
  wards v. Arizona, 451 U. S. 477, did not apply because Shatzer had
  experienced a break in Miranda custody prior to the 2006 interroga
  tion. Shatzer was convicted of sexual child abuse. The Court of Ap
  peals of Maryland reversed, holding that the mere passage of time
  does not end the Edwards protections, and that, assuming, arguendo,
  a break-in-custody exception to Edwards existed, Shatzer’s release
  back into the general prison population did not constitute such a
  break.
Held: Because Shatzer experienced a break in Miranda custody lasting
 more than two weeks between the first and second attempts at inter
 rogation, Edwards does not mandate suppression of his 2006 state
 ments. Pp. 4–18.
    (a) Edwards created a presumption that once a suspect invokes the
 Miranda right to the presence of counsel, any waiver of that right in
 response to a subsequent police attempt at custodial interrogation is
 involuntary. Edwards’ fundamental purpose is to “[p]reserv[e] the
 integrity of an accused’s choice to communicate with police only
 through counsel,” Patterson v. Illinois, 487 U. S. 285, 291, by “pre
 vent[ing] police from badgering [him] into waiving his previously as
2                        MARYLAND v. SHATZER

                                  Syllabus

    serted Miranda rights,” Michigan v. Harvey, 494 U. S. 344, 350. It is
    easy to believe that a suspect’s later waiver was coerced or badgered
    when he has been held in uninterrupted Miranda custody since his
    first refusal to waive. He remains cut off from his normal life and
    isolated in a “police-dominated atmosphere,” Miranda v. Arizona, 384
    U. S. 436, 456, where his captors “appear to control [his] fate,” Illi
    nois v. Perkins, 496 U. S. 292, 297. But where a suspect has been re
    leased from custody and returned to his normal life for some time be
    fore the later attempted interrogation, there is little reason to think
    that his change of heart has been coerced. Because the Edwards pre
    sumption has been established by opinion of this Court, it is appro
    priate for this Court to specify the period of release from custody that
    will terminate its application. See County of Riverside v. McLaugh
    lin, 500 U. S. 44. The Court concludes that the appropriate period is
    14 days, which provides ample time for the suspect to get reaccli
    mated to his normal life, consult with friends and counsel, and shake
    off any residual coercive effects of prior custody. Pp. 4–13.
       (b) Shatzer’s release back into the general prison population consti
    tutes a break in Miranda custody. Lawful imprisonment imposed
    upon conviction does not create the coercive pressures produced by
    investigative custody that justify Edwards. When previously incar
    cerated suspects are released back into the general prison population,
    they return to their accustomed surroundings and daily routine—
    they regain the degree of control they had over their lives before the
    attempted interrogation. Their continued detention is relatively dis
    connected from their prior unwillingness to cooperate in an investiga
    tion. The “inherently compelling pressures” of custodial interrogation
    ended when Shatzer returned to his normal life. Pp. 13–16.
405 Md. 585, 954 A. 2d 1118, reversed and remanded.

   SCALIA, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and KENNEDY, GINSBURG, BREYER, ALITO, and SOTOMAYOR, JJ.,
joined, and in which THOMAS, J., joined as to Part III. THOMAS, J., filed
an opinion concurring in part and concurring in the judgment. STE-
VENS, J., filed an opinion concurring in the judgment.
                       Cite as: 559 U. S. ____ (2010)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash­
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 08–680
                                  _________________


   MARYLAND, PETITIONER v. MICHAEL BLAINE

                SHATZER, SR. 

  ON WRIT OF CERTIORARI TO THE COURT OF APPEALS OF

                     MARYLAND

                             [February 24, 2010] 


  JUSTICE SCALIA delivered the opinion of the Court.
  We consider whether a break in custody ends the pre­
sumption of involuntariness established in Edwards v.
Arizona, 451 U. S. 477 (1981).
                             I
  In August 2003, a social worker assigned to the Child
Advocacy Center in the Criminal Investigation Division of
the Hagerstown Police Department referred to the de­
partment allegations that respondent Michael Shatzer,
Sr., had sexually abused his 3-year-old son. At that time,
Shatzer was incarcerated at the Maryland Correctional
Institution-Hagerstown, serving a sentence for an unre­
lated child-sexual-abuse offense. Detective Shane Blank­
enship was assigned to the investigation and interviewed
Shatzer at the correctional institution on August 7, 2003.
Before asking any questions, Blankenship reviewed
Shatzer’s Miranda rights with him, and obtained a writ­
ten waiver of those rights. When Blankenship explained
that he was there to question Shatzer about sexually
abusing his son, Shatzer expressed confusion—he had
thought Blankenship was an attorney there to discuss the
2                 MARYLAND v. SHATZER

                     Opinion of the Court

prior crime for which he was incarcerated. Blankenship
clarified the purpose of his visit, and Shatzer declined to
speak without an attorney. Accordingly, Blankenship
ended the interview, and Shatzer was released back into
the general prison population.          Shortly thereafter,
Blankenship closed the investigation.
   Two years and six months later, the same social worker
referred more specific allegations to the department about
the same incident involving Shatzer. Detective Paul
Hoover, from the same division, was assigned to the inves­
tigation. He and the social worker interviewed the victim,
then eight years old, who described the incident in more
detail. With this new information in hand, on March 2,
2006, they went to the Roxbury Correctional Institute, to
which Shatzer had since been transferred, and inter­
viewed Shatzer in a maintenance room outfitted with a
desk and three chairs. Hoover explained that he wanted
to ask Shatzer about the alleged incident involving
Shatzer’s son. Shatzer was surprised because he thought
that the investigation had been closed, but Hoover ex­
plained they had opened a new file. Hoover then read
Shatzer his Miranda rights and obtained a written waiver
on a standard department form.
   Hoover interrogated Shatzer about the incident for
approximately 30 minutes. Shatzer denied ordering his
son to perform fellatio on him, but admitted to masturbat­
ing in front of his son from a distance of less than three
feet. Before the interview ended, Shatzer agreed to Hoo­
ver’s request that he submit to a polygraph examination.
At no point during the interrogation did Shatzer request
to speak with an attorney or refer to his prior refusal to
answer questions without one.
   Five days later, on March 7, 2006, Hoover and another
detective met with Shatzer at the correctional facility to
administer the polygraph examination. After reading
Shatzer his Miranda rights and obtaining a written
                     Cite as: 559 U. S. ____ (2010)                   3

                         Opinion of the Court

waiver, the other detective administered the test and
concluded that Shatzer had failed. When the detectives
then questioned Shatzer, he became upset, started to cry,
and incriminated himself by saying, “ ‘I didn’t force him. I
didn’t force him.’ ” 405 Md. 585, 590, 954 A. 2d 1118, 1121
(2008). After making this inculpatory statement, Shatzer
requested an attorney, and Hoover promptly ended the
interrogation.
   The State’s Attorney for Washington County charged
Shatzer with second-degree sexual offense, sexual child
abuse, second-degree assault, and contributing to condi­
tions rendering a child in need of assistance. Shatzer
moved to suppress his March 2006 statements pursuant to
Edwards. The trial court held a suppression hearing and
later denied Shatzer’s motion. The Edwards protections
did not apply, it reasoned, because Shatzer had experi­
enced a break in custody for Miranda purposes between
the 2003 and 2006 interrogations. No. 21–K–06–37799
(Cir. Ct. Washington Cty., Md., Sept. 14, 2006), App. 55.
Shatzer pleaded not guilty, waived his right to a jury trial,
and proceeded to a bench trial based on an agreed state­
ment of facts. In accordance with the agreement, the
State described the interview with the victim and
Shatzer’s 2006 statements to the detectives. Based on the
proffered testimony of the victim and the “admission of the
defendant as to the act of masturbation,” the trial court
found Shatzer guilty of sexual child abuse of his son.1 No.
21–K–06–37799 (Cir. Ct. Washington Cty., Md., Sept. 21,
2006), id., at 70, 79.
   Over the dissent of two judges, the Court of Appeals of
Maryland reversed and remanded. The court held that
“the passage of time alone is insufficient to [end] the pro­
——————
  1 The State filed a nolle prosequi to the second-degree sexual offense

charge, and consented to dismissal of the misdemeanor charges as
barred by the statute of limitations.
4                  MARYLAND v. SHATZER

                     Opinion of the Court

tections afforded by Edwards,” and that, assuming, ar
guendo, a break-in-custody exception to Edwards existed,
Shatzer’s release back into the general prison population
between interrogations did not constitute a break in cus­
tody. 405 Md., at 606–607, 954 A. 2d, at 1131. We
granted certiorari, 555 U. S. ___ (2009).
                             II
   The Fifth Amendment, which applies to the States by
virtue of the Fourteenth Amendment, Malloy v. Hogan,
378 U. S. 1, 6 (1964), provides that “[n]o person . . . shall
be compelled in any criminal case to be a witness against
himself.” U. S. Const., Amdt. 5. In Miranda v. Arizona,
384 U. S. 436 (1966), the Court adopted a set of prophylac­
tic measures to protect a suspect’s Fifth Amendment right
from the “inherently compelling pressures” of custodial
interrogation. Id., at 467. The Court observed that “in­
communicado interrogation” in an “unfamiliar,” “police­
dominated atmosphere,” id., at 456–457, involves psycho­
logical pressures “which work to undermine the individ­
ual’s will to resist and to compel him to speak where he
would not otherwise do so freely,” id., at 467. Conse­
quently, it reasoned, “[u]nless adequate protective devices
are employed to dispel the compulsion inherent in custo­
dial surroundings, no statement obtained from the defen­
dant can truly be the product of his free choice.” Id., at
458.
   To counteract the coercive pressure, Miranda an­
nounced that police officers must warn a suspect prior to
questioning that he has a right to remain silent, and a
right to the presence of an attorney. Id., at 444. After the
warnings are given, if the suspect indicates that he wishes
to remain silent, the interrogation must cease. Id., at
473–474. Similarly, if the suspect states that he wants an
attorney, the interrogation must cease until an attorney is
present. Id., at 474. Critically, however, a suspect can
                 Cite as: 559 U. S. ____ (2010)             5

                     Opinion of the Court

waive these rights. Id., at 475. To establish a valid
waiver, the State must show that the waiver was knowing,
intelligent, and voluntary under the “high standar[d] of
proof for the waiver of constitutional rights [set forth in]
Johnson v. Zerbst, 304 U. S. 458 (1938).” Id., at 475.
   In Edwards, the Court determined that Zerbst’s tradi­
tional standard for waiver was not sufficient to protect a
suspect’s right to have counsel present at a subsequent
interrogation if he had previously requested counsel;
“additional safeguards” were necessary. 451 U. S., at 484.
The Court therefore superimposed a “second layer of
prophylaxis,” McNeil v. Wisconsin, 501 U. S. 171, 176
(1991). Edwards held:
    “[W]hen an accused has invoked his right to have
    counsel present during custodial interrogation, a valid
    waiver of that right cannot be established by showing
    only that he responded to further police-initiated cus­
    todial interrogation even if he has been advised of his
    rights. . . . [He] is not subject to further interrogation
    by the authorities until counsel has been made avail­
    able to him, unless the accused himself initiates fur­
    ther communication, exchanges, or conversations with
    the police.” 451 U. S., at 484–485.
The rationale of Edwards is that once a suspect indicates
that “he is not capable of undergoing [custodial] question­
ing without advice of counsel,” “any subsequent waiver
that has come at the authorities’ behest, and not at the
suspect’s own instigation, is itself the product of the ‘in­
herently compelling pressures’ and not the purely volun­
tary choice of the suspect.” Arizona v. Roberson, 486 U. S.
675, 681 (1988). Under this rule, a voluntary Miranda
waiver is sufficient at the time of an initial attempted
interrogation to protect a suspect’s right to have counsel
present, but it is not sufficient at the time of subsequent
attempts if the suspect initially requested the presence of
6                  MARYLAND v. SHATZER

                      Opinion of the Court

counsel. The implicit assumption, of course, is that the
subsequent requests for interrogation pose a significantly
greater risk of coercion. That increased risk results not
only from the police’s persistence in trying to get the sus­
pect to talk, but also from the continued pressure that
begins when the individual is taken into custody as a
suspect and sought to be interrogated—pressure likely to
“increase as custody is prolonged,” Minnick v. Mississippi,
498 U. S. 146, 153 (1990). The Edwards presumption of
involuntariness ensures that police will not take advan­
tage of the mounting coercive pressures of “prolonged
police custody,” Roberson, 486 U. S., at 686, by repeatedly
attempting to question a suspect who previously requested
counsel until the suspect is “badgered into submission,”
id., at 690 (KENNEDY, J., dissenting).
   We have frequently emphasized that the Edwards rule
is not a constitutional mandate, but judicially prescribed
prophylaxis. See, e.g., Montejo v. Louisiana, 556 U. S. ___,
___ (2009) (slip op., at 7–8); Michigan v. Harvey, 494 U. S.
344, 349 (1990); Solem v. Stumes, 465 U. S. 638, 644, n. 4
(1984). Because Edwards is “our rule, not a constitutional
command,” “it is our obligation to justify its expansion.”
Roberson, supra, at 688 (KENNEDY, J., dissenting). Lower
courts have uniformly held that a break in custody ends
the Edwards presumption, see, e.g., People v. Storm, 28
Cal. 4th 1007, 1023–1024, and n. 6, 52 P. 3d 52, 61–62,
and n. 6 (2002) (collecting state and federal cases), but we
have previously addressed the issue only in dicta, see
McNeil, supra, at 177 (Edwards applies “assuming there
has been no break in custody”).
   A judicially crafted rule is “justified only by reference to
its prophylactic purpose,” Davis v. United States, 512 U. S.
452, 458 (1994) (internal quotation marks omitted), and
applies only where its benefits outweigh its costs, Montejo,
supra, at ___ (slip op., at 14). We begin with the benefits.
Edwards’ presumption of involuntariness has the inciden­
                      Cite as: 559 U. S. ____ (2010)                      7

                           Opinion of the Court

tal effect of “conserv[ing] judicial resources which would
otherwise be expended in making difficult determinations
of voluntariness.” Minnick, supra, at 151. Its fundamen­
tal purpose, however, is to “[p]reserv[e] the integrity of an
accused’s choice to communicate with police only through
counsel,” Patterson v. Illinois, 487 U. S. 285, 291 (1988), by
“prevent[ing] police from badgering a defendant into waiv­
ing his previously asserted Miranda rights,” Harvey,
supra, at 350. Thus, the benefits of the rule are measured
by the number of coerced confessions it suppresses that
otherwise would have been admitted. See Montejo, supra,
at ___ (slip op., at 14).
   It is easy to believe that a suspect may be coerced or
badgered into abandoning his earlier refusal to be ques­
tioned without counsel in the paradigm Edwards case.
That is a case in which the suspect has been arrested for a
particular crime and is held in uninterrupted pretrial
custody while that crime is being actively investigated.
After the initial interrogation, and up to and including the
second one, he remains cut off from his normal life and
companions, “thrust into” and isolated in an “unfamiliar,”
“police-dominated atmosphere,” Miranda, 384 U. S., at
456–457, where his captors “appear to control [his] fate,”
Illinois v. Perkins, 496 U. S. 292, 297 (1990). That was the
situation confronted by the suspects in Edwards,
Roberson, and Minnick, the three cases in which we have
held the Edwards rule applicable. Edwards was arrested
pursuant to a warrant and taken to a police station, where
he was interrogated until he requested counsel. Edwards,
451 U. S., at 478–479. The officer ended the interrogation
and took him to the county jail,2 but at 9:15 the next

——————
  2 Jail is a “local government’s detention center where persons await­
ing trial or those convicted of misdemeanors are confined.” Black’s Law
Dictionary 910 (9th ed. 2009). Prison, by contrast, is a “state or federal
facility of confinement for convicted criminals, esp. felons.” Id., at 1314.
8                      MARYLAND v. SHATZER

                          Opinion of the Court

morning, two of the officer’s colleagues reinterrogated
Edwards at the jail. Id., at 479. Roberson was arrested
“at the scene of a just-completed burglary” and interro­
gated there until he requested a lawyer. Roberson, 486
U. S., at 678. A different officer interrogated him three
days later while he “was still in custody pursuant to the
arrest.” Ibid. Minnick was arrested by local police and
taken to the San Diego jail, where two FBI agents interro­
gated him the next morning until he requested counsel.
Minnick, 498 U. S., at 148–149. Two days later a Missis­
sippi Deputy Sheriff reinterrogated him at the jail. Id., at
149. None of these suspects regained a sense of control or
normalcy after they were initially taken into custody for
the crime under investigation.
   When, unlike what happened in these three cases, a
suspect has been released from his pretrial custody and
has returned to his normal life for some time before the
later attempted interrogation, there is little reason to
think that his change of heart regarding interrogation
without counsel has been coerced. He has no longer been
isolated. He has likely been able to seek advice from an
attorney, family members, and friends.3 And he knows
from his earlier experience that he need only demand
counsel to bring the interrogation to a halt; and that in­
vestigative custody does not last indefinitely. In these
circumstances, it is far fetched to think that a police offi­
cer’s asking the suspect whether he would like to waive
his Miranda rights will any more “wear down the ac­
——————
    3 JUSTICESTEVENS points out, post, at 7 (opinion concurring in judg­
ment), that in Minnick, actual pre-reinterrogation consultation with an
attorney during continued custody did not suffice to avoid application of
Edwards. That does not mean that the ability to consult freely with
attorneys and others does not reduce the level of coercion at all, or that
it is “only questionably relevant,” post, at 7, to whether termination of
custody reduces the coercive pressure that is the basis for Edwards’
super-prophylactic rule.
                    Cite as: 559 U. S. ____ (2010)                 9

                        Opinion of the Court

cused,” Smith v. Illinois, 469 U. S. 91, 98 (1984) (per cu
riam), than did the first such request at the original at­
tempted interrogation—which is of course not deemed
coercive. His change of heart is less likely attributable to
“badgering” than it is to the fact that further deliberation
in familiar surroundings has caused him to believe
(rightly or wrongly) that cooperating with the investiga­
tion is in his interest. Uncritical extension of Edwards to
this situation would not significantly increase the number
of genuinely coerced confessions excluded. The “justifica­
tion for a conclusive presumption disappears when appli­
cation of the presumption will not reach the correct result
most of the time.” Coleman v. Thompson, 501 U. S. 722,
737 (1991).
   At the same time that extending the Edwards rule
yields diminished benefits, extending the rule also in­
creases its costs: the in-fact voluntary confessions it ex­
cludes from trial, and the voluntary confessions it deters
law enforcement officers from even trying to obtain. Vol­
untary confessions are not merely “a proper element in
law enforcement,” Miranda, supra, at 478, they are an
“unmitigated good,” McNeil, 501 U. S., at 181, “ ‘essential
to society’s compelling interest in finding, convicting, and
punishing those who violate the law,’ ” ibid. (quoting
Moran v. Burbine, 475 U. S. 412, 426 (1986)).
   The only logical endpoint of Edwards disability is ter­
mination of Miranda custody and any of its lingering
effects. Without that limitation—and barring some purely
arbitrary time-limit4—every Edwards prohibition of cus­
todial interrogation of a particular suspect would be eter­

——————
  4 The  State’s alternative argument in the present case is that the
substantial lapse in time between the 2003 and 2006 attempts at
interrogation independently ended the Edwards presumption. Our
disposition makes it unnecessary to address that argument.
10                    MARYLAND v. SHATZER

                          Opinion of the Court

nal. The prohibition applies, of course, when the subse­
quent interrogation pertains to a different crime,
Roberson, supra, when it is conducted by a different law
enforcement authority, Minnick, 498 U. S. 146, and even
when the suspect has met with an attorney after the first
interrogation, ibid. And it not only prevents questioning
ex ante; it would render invalid ex post, confessions invited
and obtained from suspects who (unbeknownst to the
interrogators) have acquired Edwards immunity previ­
ously in connection with any offense in any jurisdiction.5
In a country that harbors a large number of repeat offend­
ers,6 this consequence is disastrous.
  We conclude that such an extension of Edwards is not
justified; we have opened its “protective umbrella,” Solem,
465 U. S., at 644, n. 4, far enough. The protections offered
by Miranda, which we have deemed sufficient to ensure
that the police respect the suspect’s desire to have an
attorney present the first time police interrogate him,
adequately ensure that result when a suspect who initially
requested counsel is reinterrogated after a break in cus­
——————
   5 This assumes that Roberson’s extension of Edwards to subsequent

interrogation for a different crime, and Minnick’s extension of Edwards
to subsequent interrogation by a different law enforcement agency
would apply even when the place of custody and the identity of the
custodial agency are not the same (as they were in Roberson and
Minnick) as those of the original interrogation. That assumption would
seem reasonable if the Edwards-suspending effect of a termination of
custody is rejected. Reinterrogation in different custody or by a differ­
ent interrogating agency would seem, if anything, less likely than
termination of custody to reduce coercive pressures. At the original
site, and with respect to the original interrogating agency, the suspect
has already experienced cessation of interrogation when he demands
counsel—which he may have no reason to expect elsewhere.
   6 According to a recent study, 67.5% of prisoners released from 15

States in 1994 were rearrested within three years. See Dept. of Justice,
Bureau of Justice Statistics, Special Report, Recidivism of Prisoners
Released in 1994 (NCJ 193427, 2002).
                 Cite as: 559 U. S. ____ (2010)           11

                     Opinion of the Court

tody that is of sufficient duration to dissipate its coercive
effects.
  If Shatzer’s return to the general prison population
qualified as a break in custody (a question we address in
Part III, infra), there is no doubt that it lasted long
enough (2½ years) to meet that durational requirement.
But what about a break that has lasted only one year? Or
only one week? It is impractical to leave the answer to
that question for clarification in future case-by-case adju­
dication; law enforcement officers need to know, with
certainty and beforehand, when renewed interrogation is
lawful. And while it is certainly unusual for this Court to
set forth precise time limits governing police action, it is
not unheard-of. In County of Riverside v. McLaughlin,
500 U. S. 44 (1991), we specified 48 hours as the time
within which the police must comply with the requirement
of Gerstein v. Pugh, 420 U. S. 103 (1975), that a person
arrested without a warrant be brought before a magistrate
to establish probable cause for continued detention.
  Like McLaughlin, this is a case in which the requisite
police action (there, presentation to a magistrate; here,
abstention from further interrogation) has not been pre­
scribed by statute but has been established by opinion of
this Court. We think it appropriate to specify a period of
time to avoid the consequence that continuation of the
Edwards presumption “will not reach the correct result
most of the time.” Coleman, supra, at 737. It seems to us
that period is 14 days. That provides plenty of time for
the suspect to get reacclimated to his normal life, to con­
sult with friends and counsel, and to shake off any resid­
ual coercive effects of his prior custody.
  The 14-day limitation meets Shatzer’s concern that a
break-in-custody rule lends itself to police abuse. He
envisions that once a suspect invokes his Miranda right to
counsel, the police will release the suspect briefly (to end
the Edwards presumption) and then promptly bring him
12                    MARYLAND v. SHATZER

                         Opinion of the Court

back into custody for reinterrogation. But once the sus­
pect has been out of custody long enough (14 days) to
eliminate its coercive effect, there will be nothing to gain
by such gamesmanship—nothing, that is, except the en­
tirely appropriate gain of being able to interrogate a sus­
pect who has made a valid waiver of his Miranda rights.7
   Shatzer argues that ending the Edwards protections at
a break in custody will undermine Edwards’ purpose to
conserve judicial resources. To be sure, we have said that
“[t]he merit of the Edwards decision lies in the clarity of
its command and the certainty of its application.”
Minnick, 498 U. S., at 151. But clarity and certainty are
not goals in themselves. They are valuable only when
they reasonably further the achievement of some substan­
tive end—here, the exclusion of compelled confessions.
Confessions obtained after a 2-week break in custody and
a waiver of Miranda rights are most unlikely to be com­
pelled, and hence are unreasonably excluded. In any case,
a break-in-custody exception will dim only marginally, if
at all, the bright-line nature of Edwards. In every case
involving Edwards, the courts must determine whether
the suspect was in custody when he requested counsel and
when he later made the statements he seeks to suppress.
Now, in cases where there is an alleged break in custody,
they simply have to repeat the inquiry for the time be­
tween the initial invocation and reinterrogation. In most
cases that determination will be easy. And when it is

——————
  7 A defendant who experiences a 14-day break in custody after invok­

ing the Miranda right to counsel is not left without protection. Ed
wards establishes a presumption that a suspect’s waiver of Miranda
rights is involuntary. See Arizona v. Roberson, 486 U. S. 675, 681
(1988). Even without this “second layer of prophylaxis,” McNeil v.
Wisconsin, 501 U. S. 171, 176 (1991), a defendant is still free to claim
the prophylactic protection of Miranda—arguing that his waiver of
Miranda rights was in fact involuntary under Johnson v. Zerbst, 304
U. S. 458 (1938). See Miranda, 384 U. S., at 475.
                 Cite as: 559 U. S. ____ (2010)           13

                     Opinion of the Court

determined that the defendant pleading Edwards has
been out of custody for two weeks before the contested
interrogation, the court is spared the fact-intensive in­
quiry into whether he ever, anywhere, asserted his
Miranda right to counsel.
                             III
  The facts of this case present an additional issue. No
one questions that Shatzer was in custody for Miranda
purposes during the interviews with Detective
Blankenship in 2003 and Detective Hoover in 2006. Like­
wise, no one questions that Shatzer triggered the Edwards
protections when, according to Detective Blankenship’s
notes of the 2003 interview, he stated that “ ‘he would not
talk about this case without having an attorney present,’ ”
405 Md., at 589, 954 A. 2d, at 1120. After the 2003 inter­
view, Shatzer was released back into the general prison
population where he was serving an unrelated sentence.
The issue is whether that constitutes a break in Miranda
custody.
  We have never decided whether incarceration consti­
tutes custody for Miranda purposes, and have indeed
explicitly declined to address the issue. See Perkins, 496
U. S., at 299. See also Bradley v. Ohio, 497 U. S. 1011,
1013 (1990) (Marshall, J., dissenting from denial of certio­
rari). Whether it does depends upon whether it exerts the
coercive pressure that Miranda was designed to guard
against—the “danger of coercion [that] results from the
interaction of custody and official interrogation.” Perkins,
supra, at 297 (emphasis added). To determine whether a
suspect was in Miranda custody we have asked whether
“there is a ‘formal arrest or restraint on freedom of move­
ment’ of the degree associated with a formal arrest.” New
York v. Quarles, 467 U. S. 649, 655 (1984); see also Stans
bury v. California, 511 U. S. 318, 322 (1994) (per curiam).
This test, no doubt, is satisfied by all forms of incarcera­
14                    MARYLAND v. SHATZER

                         Opinion of the Court

tion. Our cases make clear, however, that the freedom-of­
movement test identifies only a necessary and not a suffi­
cient condition for Miranda custody. We have declined to
accord it “talismanic power,” because Miranda is to be
enforced “only in those types of situations in which the
concerns that powered the decision are implicated.”
Berkemer v. McCarty, 468 U. S. 420, 437 (1984). Thus, the
temporary and relatively nonthreatening detention in­
volved in a traffic stop or Terry stop, see Terry v. Ohio, 392
U. S. 1 (1968), does not constitute Miranda custody.
McCarty, supra, at 439–440. See also Perkins, supra, at
296.
   Here, we are addressing the interim period during
which a suspect was not interrogated, but was subject to a
baseline set of restraints imposed pursuant to a prior
conviction. Without minimizing the harsh realities of
incarceration, we think lawful imprisonment imposed
upon conviction of a crime does not create the coercive
pressures identified in Miranda.
   Interrogated suspects who have previously been con­
victed of crime live in prison. When they are released
back into the general prison population, they return to
their accustomed surroundings and daily routine—they
regain the degree of control they had over their lives prior
to the interrogation. Sentenced prisoners, in contrast to
the Miranda paradigm, are not isolated with their accus­
ers. They live among other inmates, guards, and workers,
and often can receive visitors and communicate with
people on the outside by mail or telephone.
   Their detention, moreover, is relatively disconnected
from their prior unwillingness to cooperate in an investi­
gation. The former interrogator has no power to increase
the duration of incarceration, which was determined at
sentencing.8 And even where the possibility of parole
——————
 8 We   distinguish the duration of incarceration from the duration of
                    Cite as: 559 U. S. ____ (2010)                 15

                        Opinion of the Court

exists, the former interrogator has no apparent power to
decrease the time served. This is in stark contrast to the
circumstances faced by the defendants in Edwards,
Roberson, and Minnick, whose continued detention as
suspects rested with those controlling their interrogation,
and who confronted the uncertainties of what final
charges they would face, whether they would be convicted,
and what sentence they would receive.
   Shatzer’s experience illustrates the vast differences
between Miranda custody and incarceration pursuant to
conviction. At the time of the 2003 attempted interroga­
tion, Shatzer was already serving a sentence for a prior
conviction. After that, he returned to the general prison
population in the Maryland Correctional Institution-
Hagerstown and was later transferred, for unrelated
reasons, down the street to the Roxbury Correctional
Institute. Both are medium-security state correctional
facilities. See Maryland Div. of Correction Inmate Hand­
book 7 (2007), online at http://dpscs.md.gov/rehabservs/
doc/pdfs/2007_Inmate_Handbook.pdf (all Internet materi­
als as visited Feb. 22, 2010, and available in Clerk of
Court’s case file). Inmates in these facilities generally can
visit the library each week, id., at 28; have regular exer­
cise and recreation periods, id., at 17; can participate
in basic adult education and occupational training, id.,
at 26, 7; are able to send and receive mail, id., at 21–22,
16; and are allowed to receive visitors twice a week,
see http://dpscs.md.gov/locations/mcih.shtml; http://www.
dpscs.state.md.us/locations/rci.shtml. His continued de­
——————
what might be termed interrogative custody. When a prisoner is
removed from the general prison population and taken to a separate
location for questioning, the duration of that separation is assuredly
dependent upon his interrogators. For which reason once he has
asserted a refusal to speak without assistance of counsel Edwards
prevents any efforts to get him to change his mind during that inter­
rogative custody.
16                 MARYLAND v. SHATZER

                      Opinion of the Court

tention after the 2003 interrogation did not depend on
what he said (or did not say) to Detective Blankenship,
and he has not alleged that he was placed in a higher level
of security or faced any continuing restraints as a result of
the 2003 interrogation. The “inherently compelling pres­
sures” of custodial interrogation ended when he returned
to his normal life.
                                IV
  A few words in response to JUSTICE STEVENS’ concur­
rence: It claims we ignore that “[w]hen police tell an indi­
gent suspect that he has the right to an attorney” and
then “reinterrogate” him without providing a lawyer, “the
suspect is likely to feel that the police lied to him and that
he really does not have any right to a lawyer.” Post, at 2
(opinion concurring in judgment) (hereinafter concur­
rence). See also post, at 4, 7, n. 11, 11, n. 16. The fallacy
here is that we are not talking about “reinterrogating” the
suspect; we are talking about asking his permission to be
interrogated. An officer has in no sense lied to a suspect
when, after advising, as Miranda requires, “You have the
right to remain silent, and if you choose to speak you have
the right to the presence of an attorney,” he promptly ends
the attempted interrogation because the suspect declines
to speak without counsel present, and then, two weeks
later, reapproaches the suspect and asks, “Are you now
willing to speak without a lawyer present?”
  The “concer[n] that motivated the Edwards line of
cases,” post, at 2–3, n. 2, is that the suspect will be coerced
into saying yes. That concern guides our decision today.
Contrary to the concurrence’s conclusion, post, at 3, 5–6,
there is no reason to believe a suspect will view confession
as “ ‘the only way to end his interrogation’ ” when, before
the interrogation begins, he is told that he can avoid it by
simply requesting that he not be interrogated without
counsel present—an option that worked before. If, as the
                 Cite as: 559 U. S. ____ (2010)           17

                     Opinion of the Court

concurrence argues will often be the case, post, at 5, a
break in custody does not change the suspect’s mind, he
need only say so.
   The concurrence also accuses the Court of “ignor[ing]
that when a suspect asks for counsel, until his request is
answered, there are still the same ‘inherently compelling’
pressures of custodial interrogation on which the Miranda
line of cases is based.” Post, at 4. We do not ignore these
pressures; nor do we suggest that they disappear when
custody is recommenced after a break, see post, at 5. But
if those pressures are merely “the same” as before, then
Miranda provides sufficient protection—as it did before.
The Edwards presumption of involuntariness is justified
only in circumstances where the coercive pressures have
increased so much that suspects’ waivers of Miranda
rights are likely to be involuntary most of the time. Con­
trary to the concurrence’s suggestion, post, at 3, it is only
in those narrow circumstances—when custody is unbro­
ken—that the Court has concluded a “fresh se[t] of
Miranda warnings” is not sufficient. See Roberson, 486
U. S., at 686.
   In the last analysis, it turns out that the concurrence
accepts our principal points. It agrees that Edwards
prophylaxis is not perpetual; it agrees that a break in
custody reduces the inherently compelling pressure upon
which Edwards was based; it agrees that Shatzer’s release
back into the general prison population constituted a
break in custody; and it agrees that in this case the break
was long enough to render Edwards inapplicable. Post, at
10–12. We differ in two respects: Instead of terminating
Edwards protection when the custodial pressures that
were the basis for that protection dissipate, the concur­
rence would terminate it when the suspect would no
longer “feel that he has ‘been denied the counsel he has
clearly requested,’ ” post, at 11. This is entirely unrelated
to the rationale of Edwards. If confidence in the police’s
18                 MARYLAND v. SHATZER

                      Opinion of the Court

promise to provide counsel were the touchstone, Edwards
would not have applied in Minnick, where the suspect in
continuing custody actually met with appointed counsel.
The concurrence’s rule is also entirely unrelated to the
existence of a break in custody. While that may relieve
the accumulated coercive pressures of custody that are the
foundation for Edwards, it is hard to see how it bolsters
the suspect’s confidence that if he asks for counsel he will
get one.
   And secondly, the concurrence differs from us in declin­
ing to say how long after a break in custody the termina­
tion of Edwards protection occurs. Two and one-half
years, it says, is clearly enough—but it gives law enforce­
ment authorities no further guidance. The concurrence
criticizes our use of 14 days as arbitrary and unexplained,
post, at 5, and n. 7. But in fact that rests upon the same
basis as the concurrence’s own approval of a 21⁄2-year
break in custody: how much time will justify “treating the
second interrogation as no more coercive than the first,”
post, at 10. Failure to say where the line falls short of 21⁄2
years, and leaving that for future case-by-case determina­
tion, is certainly less helpful, but not at all less arbitrary.
                        *     *     *
  Because Shatzer experienced a break in Miranda cus­
tody lasting more than two weeks between the first and
second attempts at interrogation, Edwards does not man­
date suppression of his March 2006 statements. Accord­
ingly, we reverse the judgment of the Court of Appeals of
Maryland, and remand the case for further proceedings
not inconsistent with this opinion.

                                              It is so ordered.
                 Cite as: 559 U. S. ____ (2010)           1

                    Opinion of THOMAS, J.

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 08–680
                         _________________


   MARYLAND, PETITIONER v. MICHAEL BLAINE

                SHATZER, SR. 

  ON WRIT OF CERTIORARI TO THE COURT OF APPEALS OF

                     MARYLAND

                     [February 24, 2010] 


   JUSTICE THOMAS, concurring in part and concurring in
the judgment.
   I join Part III of the Court’s opinion, which holds that
release into the general prison population constitutes a
break in custody. I do not join the Court’s decision to
extend the presumption of involuntariness established in
Edwards v. Arizona, 451 U. S. 477 (1981), for 14 days after
custody ends.
   It is not apparent to me that the presumption of in
voluntariness the Court recognized in Edwards is justifi
able even in the custodial setting to which Edwards ap
plies it. See, e.g., Minnick v. Mississippi, 498 U. S. 146,
160 (1990) (SCALIA, J., dissenting). Accordingly, I would
not extend the Edwards rule “beyond the circumstances
present in Edwards itself.” Id., at 162. But even if one
believes that the Court is obliged to apply Edwards to any
case involving continuing custody, the Court’s opinion
today goes well beyond that. It extends the presumption
of involuntariness Edwards applies in custodial settings to
interrogations that occur after custody ends.
   The Court concedes that this extension, like the Ed
wards presumption itself, is not constitutionally required.
The Court nevertheless defends the extension as a judi
cially created prophylaxis against compelled confessions.
Even if one accepts that such prophylaxis is both permis
2                     MARYLAND v. SHATZER

                         Opinion of THOMAS, J.

sible generally and advisable for some period following a
break in custody,1 the Court’s 14-day rule fails to satisfy
the criteria our precedents establish for the judicial crea
tion of such a safeguard.
   Our precedents insist that judicially created prophylac
tic rules like those in Edwards and Miranda v. Arizona,
384 U. S. 436 (1966), maintain “the closest possible fit”
between the rule and the Fifth Amendment interests they
seek to protect. United States v. Patane, 542 U. S. 630,
640–641 (2004) (plurality opinion); see generally Montejo
v. Louisiana, 556 U. S. ___, ___ (2009) (slip op., at 18);
Chavez v. Martinez, 538 U. S. 760, 772 (2003) (plurality
opinion). The Court’s 14-day rule does not satisfy this
test. The Court relates its 14-day rule to the Fifth
Amendment simply by asserting that 14 days between
release and recapture should provide “plenty of time for
the suspect . . . to shake off any residual coercive effects of
his prior custody,” ante, at 11.

——————
  1 At a minimum the latter proposition is questionable. I concede that

some police officers might badger a suspect during a subsequent inter
rogation after a break in custody, or might use catch-and-release tactics
to suggest they will not take no for an answer. But if a suspect reenters
custody after being questioned and released, he need only invoke his
right to counsel to ensure Edwards’ protection for the duration of the
subsequent detention. And, if law enforcement officers repeatedly
release and recapture a suspect to wear down his will—such that his
participation in a subsequent interrogation is no longer truly volun
tary—the “high standar[d] of proof for the waiver of constitutional
rights [set forth in] Johnson v. Zerbst, 304 U. S. 458 (1938),” will
protect against the admission of the suspect’s statements in court.
Miranda v. Arizona, 384 U. S. 436, 475 (1966). The Zerbst inquiry
takes into account the totality of the circumstances surrounding the
waiver—including any improper pressures by police. See id., at 464; cf.
ante, at 11–12, n. 6 (stating that “[e]ven without [Edwards’] second
layer of prophylaxis, a defendant is still free to claim the prophylactic
protection of Miranda—arguing that his waiver of Miranda rights was
in fact involuntary under Johnson v. Zerbst” (internal quotation marks
and citation omitted)).
                     Cite as: 559 U. S. ____ (2010)                    3

                         Opinion of THOMAS, J.

   This ipse dixit does not explain why extending the Ed
wards presumption for 14 days following a break in cus
tody—as opposed to 0, 10, or 100 days—provides the “clos
est possible fit” with the Self-Incrimination Clause,
Patane, supra, at 640–641; see ante, at 11 (merely stating
that “[i]t seems to us that” the appropriate “period is 14
days”). Nor does it explain how the benefits of a prophy
lactic 14-day rule (either on its own terms or compared
with other possible rules) “outweigh its costs” (which
would include the loss of law enforcement information as
well as the exclusion of confessions that are in fact volun
tary). Ante, at 6 (citing Montejo, supra, at __ (slip op., at
14)).
   To be sure, the Court’s rule has the benefit of providing
a bright line. Ante, at 12. But bright-line rules are not
necessary to prevent Fifth Amendment violations, as the
Court has made clear when refusing to adopt such rules in
cases involving other Miranda rights. See, e.g., Michigan
v. Mosley, 423 U. S. 96, 103–104 (1975). And an otherwise
arbitrary rule is not justifiable merely because it gives
clear instruction to law enforcement officers.2
   As the Court concedes, “clarity and certainty are not
goals in themselves. They are valuable only when they
reasonably further the achievement of some substantive
end—here, the exclusion of compelled confessions” that
the Fifth Amendment prohibits. Ante, at 12. The Court’s
arbitrary 14-day rule fails this test, even under the rela
tively permissive criteria set forth in our precedents.
Accordingly, I do not join that portion of the Court’s
opinion.
——————
   2 Though the Court asserts that its 14-day rule will tell “law enforce

ment officers . . . with certainty and beforehand, when renewed interro
gation is lawful,” ante, at 10, that is not so clear. Determining whether
a suspect was previously in custody, and when the suspect was re
leased, may be difficult without questioning the suspect, especially if
state and federal authorities are conducting simultaneous investiga
tions.
                      Cite as: 559 U. S. ____ (2010)                     1

                  STEVENS, J., concurring in judgment

SUPREME COURT OF THE UNITED STATES
                               _________________

                               No. 08–680
                               _________________


    MARYLAND, PETITIONER v. MICHAEL BLAINE

                 SHATZER, SR. 

   ON WRIT OF CERTIORARI TO THE COURT OF APPEALS OF

                      MARYLAND

                           [February 24, 2010] 


  JUSTICE STEVENS, concurring in the judgment.
  While I agree that the presumption from Edwards v.
Arizona, 451 U. S. 477 (1981), is not “eternal,” ante, at 9–
10, and does not mandate suppression of Shatzer’s state­
ment made after a 2½-year break in custody, I do not
agree with the Court’s newly announced rule: that Ed
wards always ceases to apply when there is a 14-day
break in custody, ante, at 11.
  In conducting its “cost-benefit” analysis, the Court
demeans Edwards as a “ ‘second layer’ ” of “judicially pre­
scribed prophylaxis,” ante, at 5, 6, 12, n. 7; see also ante, at
6 (describing Edwards as “ ‘our rule, not a constitutional
command’ ” (quoting Arizona v. Roberson, 486 U. S. 675,
688 (1988) (KENNEDY, J., dissenting))). The source of the
holdings in the long line of cases that includes both Ed
wards and Miranda, however, is the Fifth Amendment’s
protection against compelled self-incrimination applied to
the “compulsion inherent in custodial” interrogation,
Miranda v. Arizona, 384 U. S. 436, 458 (1966), and the
“significan[ce]” of “the assertion of the right to counsel,”
Edwards, 451 U. S., at 485.1 The Court’s analysis today is
——————
  1 SeeDickerson v. United States, 530 U. S. 428, 438 (2000) (holding
that “the protections announced in Miranda” are “constitutionally
required”); Shea v. Louisiana, 470 U. S. 51, 52 (1985) (“In Edwards . . . ,
this Court ruled that a criminal defendant’s rights under the Fifth and
2                      MARYLAND v. SHATZER

                  STEVENS, J., concurring in judgment

insufficiently sensitive to the concerns that motivated the
Edwards line of cases.
                               I
   The most troubling aspect of the Court’s time-based rule
is that it disregards the compulsion caused by a second (or
third, or fourth) interrogation of an indigent suspect who
was told that if he requests a lawyer, one will be provided
for him. When police tell an indigent suspect that he has
the right to an attorney, that he is not required to speak
without an attorney present, and that an attorney will be
provided to him at no cost before questioning, the police
have made a significant promise. If they cease question­
ing and then reinterrogate the suspect 14 days later with­
out providing him with a lawyer, the suspect is likely to
feel that the police lied to him and that he really does not
have any right to a lawyer.2
——————
Fourteenth Amendments were violated by the use of his confession
obtained by police-instigated interrogation—without counsel present—
after he requested an attorney”); Oregon v. Bradshaw, 462 U. S. 1039,
1043 (1983) (plurality opinion) (“[The] subsequent incriminating
statements made without [an] attorney present violated the rights
secured to the defendant by the Fifth and Fourteenth Amendments to
the United States Constitution”); Miranda, 384 U. S., at 458 (examin­
ing the “history and precedent underlying the Self-Incrimination
Clause to determine its applicability in this situation”).
   2 The Court states that this argument rests on a “fallacy” because “we

are not talking about ‘reinterrogating’ the suspect; we are talking about
asking his permission to be interrogated.” Ante, at 16 (emphasis
deleted). Because, however, a suspect always has the right to remain
silent, this is a distinction without a difference: Any time that the
police interrogate or reinterrogate, and read a suspect his Miranda
rights, the suspect may decline to speak. And if this is a “fallacy,” it is
the same “fallacy” upon which this Court has relied in the Edwards line
of cases that held that police may not continue to interrogate a suspect
who has requested a lawyer: Police may not continue to ask such a
suspect whether they may interrogate him until that suspect has a
lawyer present. The Court’s apparent belief that this is a “fallacy” only
underscores my concern that its analysis is insufficiently sensitive to
                    Cite as: 559 U. S. ____ (2010)                  3

                 STEVENS, J., concurring in judgment

   When officers informed Shatzer of his rights during the
first interrogation, they presumably informed him that if
he requested an attorney, one would be appointed for him
before he was asked any further questions. But if an
indigent suspect requests a lawyer, “any further interro­
gation” (even 14 days later) “without counsel having been
provided will surely exacerbate whatever compulsion to
speak the suspect may be feeling.” Roberson, 486 U. S., at
686. When police have not honored an earlier commit­
ment to provide a detainee with a lawyer, the detainee
likely will “understan[d] his (expressed) wishes to have
been ignored” and “may well see further objection as futile
and confession (true or not) as the only way to end his
interrogation.” Davis v. United States, 512 U. S. 452, 472–
473 (1994) (Souter, J., concurring in judgment). Cf. Coo
per v. Dupnik, 963 F. 2d 1220, 1225 (CA9 1992) (en banc)
(describing an elaborate police task force plan to ignore a
suspect’s requests for counsel, on the theory that such
would induce hopelessness and thereby elicit an admis­
sion). Simply giving a “fresh se[t] of Miranda warnings”
will not “ ‘reassure’ a suspect who has been denied the
counsel he has clearly requested that his rights have
remained untrammeled.” Roberson, 486 U. S., at 686.
                              II
  The Court never explains why its rule cannot depend on,
in addition to a break in custody and passage of time, a
concrete event or state of affairs, such as the police having
honored their commitment to provide counsel. Instead,
the Court simply decides to create a time-based rule, and
in so doing, disregards much of the analysis upon which
Edwards and subsequent decisions were based. “[T]he
assertion of the right to counsel” “[i]s a significant event.”3
——————
the concerns that motivated the Edwards line of cases.
  3 Indeed, a lawyer has a “unique ability to protect the Fifth Amend­

ment rights of a client undergoing custodial interrogation.” Fare v.
4                      MARYLAND v. SHATZER

                  STEVENS, J., concurring in judgment

Edwards, 451 U. S., at 485. As the Court today acknowl­
edges, the right to counsel, like the right to remain silent,
is one that police may “coerc[e] or badge[r],” ante, at 7, a
suspect into abandoning.4 However, as discussed above,
the Court ignores the effects not of badgering but of rein­
terrogating a suspect who took the police at their word
that he need not answer questions without an attorney
present. See Roberson, 486 U. S., at 686. The Court,
moreover, ignores that when a suspect asks for counsel,
until his request is answered, there are still the same
“inherently compelling” pressures of custodial interroga­
tion on which the Miranda line of cases is based, see 486
U. S., at 681,5 and that the concern about compulsion is
especially serious for a detainee who has requested a
lawyer, an act that signals his “inability to cope with the

——————
Michael C., 442 U. S. 707, 719 (1979). Counsel can curb an officer’s
overbearing conduct, advise a suspect of his rights, and ensure that
there is an accurate record of any interrogation. “Because of this
special ability of the lawyer to help the client preserve his Fifth
Amendment rights once the client becomes enmeshed in the adversary
process, the Court found that the right to have counsel present at the
interrogation is indispensible to the protection of the Fifth Amendment
privilege.” Arizona v. Roberson, 486 U. S. 675, 682, n. 4 (1988) (internal
quotation marks omitted). Thus, “once the accused has requested
counsel,” courts must be especially wary of “coercive form[s] of custodial
interrogation.” Bradshaw, 462 U. S., at 1051 (Powell, J., concurring in
judgment).
  4 See Michigan v. Harvey, 494 U. S. 344, 350 (1990) (subsequent con­

fession suggests the police “badger[ed] a defendant into waiving his
previously asserted Miranda rights”).
  5 See Minnick v. Mississippi, 498 U. S. 146, 155 (1990) (“[N]either

admissions nor waivers are effective unless there are both particular
and systemic assurances that the coercive pressures of custody were
not the inducing cause”); cf. Smith v. Illinois, 469 U. S. 91, 98 (1984)
(per curiam) (“[T]he authorities through ‘badger[ing]’ or ‘overreach­
ing’—explicit or subtle, deliberate or unintentional—might otherwise
wear down the accused and persuade him to incriminate himself
notwithstanding his earlier request for counsel’s assistance”).
                      Cite as: 559 U. S. ____ (2010)                       5

                   STEVENS, J., concurring in judgment

pressures of custodial interrogation,” id., at 686.6
   Instead of deferring to these well-settled understand­
ings of the Edwards rule, the Court engages in its own
speculation that a 14-day break in custody eliminates the
compulsion that animated Edwards. But its opinion gives
no strong basis for believing that this is the case.7 A 14­
day break in custody does not eliminate the rationale for
the initial Edwards rule: The detainee has been told that
he may remain silent and speak only through a lawyer
and that if he cannot afford an attorney, one will be pro­
vided for him. He has asked for a lawyer. He does not
have one. He is in custody. And police are still question­
ing him. A 14-day break in custody does not change the
fact that custodial interrogation is inherently compelling.
It is unlikely to change the fact that a detainee “considers
himself unable to deal with the pressures of custodial
interrogation without legal assistance.” Roberson, 486
U. S., at 683.8 And in some instances, a 14-day break in
——————
  6 See  Roberson, 486 U. S., at 681 (“[I]f a suspect believes that he is not
capable of undergoing such questioning without advice of counsel, then
it is presumed that any subsequent waiver that has come at the au­
thorities’ behest, and not at the suspect’s own instigation, is itself the
product of the ‘inherently compelling pressures’ ”); Michigan v. Mosley,
423 U. S. 96, 110, n. 2 (1975) (White, J., concurring in result) (“[T]he
accused having expressed his own view that he is not competent to deal
with the authorities without legal advice, a later decision at the au­
thorities’ insistence to make a statement without counsel’s presence
may properly be viewed with skepticism”).
   7 Today’s decision, moreover, offers no reason for its 14-day time pe­

riod. To be sure, it may be difficult to marshal conclusive evidence
when setting an arbitrary time period. But in light of the basis for
Edwards, we should tread carefully. Instead, the only reason for
choosing a 14-day time period, the Court tells us, is that “[i]t seems to
us that period is 14 days.” Ante, at 11. That time period is “plenty of
time for the suspect to get reacclimated to his normal life, to consult
with friends and counsel, and to shake off any residual coercive effects
of his prior custody.” Ibid. But the Court gives no reason for that
speculation, which may well prove inaccurate in many circumstances.
   8 In Roberson, for example, we observed that once a suspect has as­
6                       MARYLAND v. SHATZER

                   STEVENS, J., concurring in judgment

custody may make matters worse 9 “[w]hen a suspect
understands his (expressed) wishes to have been ignored”
and thus “may well see further objection as futile and
confession (true or not) as the only way to end his interro­
gation.” Davis, 512 U. S., at 472–473 (Souter, J., concur­
ring in judgment).10
  The Court ignores these understandings from the Ed
wards line of cases and instead speculates that if a suspect
is reinterrogated and eventually talks, it must be that
“further deliberation in familiar surroundings has caused
him to believe (rightly or wrongly) that cooperating with
the investigation is in his interest.” Ante, at 9. But it is
——————
serted his right to an attorney, courts must presume he does “not feel
sufficiently comfortable with the pressures of custodial interrogation to
answer questions without an attorney. This discomfort is precisely the
state of mind that Edwards presumes to persist . . . .” 486 U. S., at 684.
We held in Roberson that just because different police come to speak
about a different investigation, that presumption does not change:
“[T]here is no reason to assume that a suspect’s state of mind is in any
way investigation-specific.” Ibid. Nor is there any reason to believe
that it is arrest specific.
    9 The compulsion is heightened by the fact that “[t]he uncertainty of

fate that being released from custody and then reapprehended entails
is, in some circumstances, more coercive than continual custody.”
Strauss, Reinterrogation, 22 Hastings Const. L. Q. 359, 390 (1995).
    10 Not only is this a likely effect of reinterrogation, but police may use

this effect to their advantage. Indeed, the Court’s rule creates a
strange incentive to delay formal proceedings, in order to gain addi­
tional information by way of interrogation after the time limit lapses.
The justification for Fifth Amendment rules “must be consistent with
. . . practical realities,” Roberson, 486 U. S., at 688 (KENNEDY, J.,
dissenting), and the reality is that police may operate within the
confines of the Fifth Amendment in order to extract as many confes­
sions as possible, see Leo & White, Adapting to Miranda: Modern
Interrogators’ Strategies for Dealing with the Obstacles Posed by
Miranda, 84 Minn. L. Rev. 397 (1999). With a time limit as short as 14
days, police who hope that they can eventually extract a confession may
feel comfortable releasing a suspect for a short period of time. The
resulting delay will only increase the compelling pressures on the
suspect.
                     Cite as: 559 U. S. ____ (2010)                    7

                  STEVENS, J., concurring in judgment

not apparent why that is the case. The answer, we are
told, is that once a suspect has been out of Miranda cus­
tody for 14 days, “[h]e has likely been able to seek advice
from an attorney, family members, and friends.” Ante, at
8. This speculation, however, is overconfident and only
questionably relevant. As a factual matter, we do not
know whether the defendant has been able to seek advice:
First of all, suspects are told that if they cannot afford a
lawyer, one will be provided for them. Yet under the
majority’s rule, an indigent suspect who took the police at
their word when he asked for a lawyer will nonetheless be
assumed to have “been able to seek advice from an attor­
ney.” Second, even suspects who are not indigent cannot
necessarily access legal advice (or social advice as the
Court presumes) within 14 days. Third, suspects may not
realize that they need to seek advice from an attorney.
Unless police warn suspects that the interrogation will
resume in 14 days, why contact a lawyer? When a suspect
is let go, he may assume that the police were satisfied. In
any event, it is not apparent why interim advice matters.11
In Minnick v. Mississippi, 498 U. S. 146, 153 (1990), we
held that it is not sufficient that a detainee happened to
speak at some point with a lawyer. See ibid. (noting that
“consultation with an attorney” does not prevent “persis­
tent attempts by officials to persuade [a suspect] to waive
his rights” or shield against the “coercive pressures that
accompany custody”). If the actual interim advice of an
attorney is not sufficient, the hypothetical, interim advice
of “an attorney, family members, and friends,” ante, at 8,
is not enough.
——————
  11 It is important to distinguish this from the point that I make above

about indigent suspects. If the police promise to provide a lawyer and
never do so, it sends a message to the suspect that the police have lied
and that the rights read to him are hollow. But the mere fact that a
suspect consulted a lawyer does not itself reduce the compulsion when
police reinterrogate him.
8                      MARYLAND v. SHATZER

                  STEVENS, J., concurring in judgment

   The many problems with the Court’s new rule are exac­
erbated in the very situation in this case: a suspect who is
in prison. Even if, as the Court assumes, a trip to one’s
home significantly changes the Edwards calculus, a trip to
one’s prison cell is not the same. A prisoner’s freedom is
severely limited, and his entire life remains subject to
government control. Such an environment is not condu­
cive to “shak[ing] off any residual coercive effects of his
prior custody.” Ante, at 11.12 Nor can a prisoner easily
“seek advice from an attorney, family members, and
friends,” ante, at 8, especially not within 14 days; prison­
ers are frequently subject to restrictions on communica­
tions. Nor, in most cases, can he live comfortably knowing
that he cannot be badgered by police; prison is not like a
normal situation in which a suspect “is in control, and
need only shut his door or walk away to avoid police badg­
ering.” Montejo v. Louisiana, 556 U. S. ___, ___ (2009)
(slip op., at 16). Indeed, for a person whose every move is
controlled by the State, it is likely that “his sense of de­
pendence on, and trust in, counsel as the guardian of his
interests in dealing with government officials intensified.”
United States v. Green, 592 A. 2d 985, 989 (D. C. 1991); cf.
Minnick, 498 U. S., at 153 (explaining that coercive pres­
sures “may increase as custody is prolonged”).13 The Court
——————
   12 Cf. Orozco v. Texas, 394 U. S. 324, 326 (1969) (holding that a sus­

pect was in custody while being held in own home, despite his comfort
and familiarity with the surroundings); Mathis v. United States, 391
U. S. 1, 5 (1968) (holding that a person serving a prison sentence for
one crime was in custody when he was interrogated in prison about
another, unrelated crime); Miranda v. Arizona, 384 U. S. 436, 478
(1966) (“[W]hen an individual is . . . deprived of his freedom by the
authorities in any significant way and is subjected to questioning, the
privilege against self-incrimination is jeopardized”).
   13 Prison also presents a troubling set of incentives for police. First,

because investigators know that their suspect is also a prisoner, there
is no need formally to place him under arrest. Thus, police generally
can interview prisoners even without probable cause to hold them.
                     Cite as: 559 U. S. ____ (2010)                     9

                  STEVENS, J., concurring in judgment

ignores these realities of prison, and instead rests its
argument on the supposition that a prisoner’s “detention
. . . is relatively disconnected from their prior unwilling­
ness to cooperate in an investigation.” Ante, at 14. But
that is not necessarily the case. Prisoners are uniquely
vulnerable to the officials who control every aspect of their
lives; prison guards may not look kindly upon a prisoner
who refuses to cooperate with police. And cooperation
frequently is relevant to whether the prisoner can obtain
parole. See, e.g., Code of Md. Regs., tit. 12, §08.01.18(A)(3)
(2008). Moreover, even if it is true as a factual matter
that a prisoner’s fate is not controlled by the police who
come to interrogate him, how is the prisoner supposed to
know that? As the Court itself admits, compulsion is
likely when a suspect’s “captors appear to control [his]
fate,” ante, at 7 (internal quotation marks omitted). But
when a guard informs a suspect that he must go speak
with police, it will “appear” to the prisoner that the guard
and police are not independent. “Questioning by captors,
who appear to control the suspect’s fate, may create mutu­
ally reinforcing pressures that the Court has assumed will
weaken the suspect’s will.” Illinois v. Perkins, 496 U. S.
292, 297 (1990) (emphasis added).14
——————
This means that police can interrogate suspects with little or no evi­
dence of guilt, and police can do so time after time, without fear of
being sued for wrongful arrest. Second, because police know that their
suspect is otherwise detained, there is no need necessarily to resolve
the case quickly. Police can comfortably bide their time, interrogating
and reinterrogating their suspect until he slips up. Third, because
police need not hold their suspect, they do not need to arraign him or
otherwise initiate formal legal proceedings that would trigger various
protections.
   14 The Court attempts to distinguish detention in prison from the

“paradigm Edwards case,” ante, at 7, but it is not clear why that is so.
The difference cannot be simply that convicted prisoners’ “detention . . .
is relatively disconnected from their prior unwillingness to cooperate in
an investigation,” ante, at 14, because in many instances of pretrial
10                     MARYLAND v. SHATZER 


                  STEVENS, J., concurring in judgment


                             III 

  Because, at the very least, we do not know whether
Shatzer could obtain a lawyer, and thus would have felt
that police had lied about providing one, I cannot join the
Court’s opinion. I concur in today’s judgment, however, on
another ground: Even if Shatzer could not consult a law­
yer and the police never provided him one, the 2½-year
break in custody is a basis for treating the second interro­
gation as no more coercive than the first. Neither a break
in custody nor the passage of time has an inherent, cura­
——————
custody, the custody will continue regardless of whether a detainee
answers questions. Take Roberson for example. Roberson was arrested
and being held for one crime when, days later, a different officer inter­
rogated him about a different crime. 486 U. S., at 678. Regardless of
whether he cooperated with the second investigation, he was still being
held for the first crime. Yet under the Court’s analysis, had Roberson
been held long enough that he had become “accustomed” to the deten­
tion facility, ante, at 14, there would have been a break in custody
between each interrogation. Thus, despite the fact that coercive pres­
sures “may increase as custody is prolonged,” Minnick, 498 U. S., at
153, the real problem in Roberson may have been that the police did not
leave him sitting in jail for long enough.
   This problem of pretrial custody also highlights a tension with the
Court’s decision last Term in Montejo v. Louisiana, 556 U. S. ___
(2009). In Montejo, the Court overturned Michigan v. Jackson, 475
U. S. 625, 636 (1986), which had protected an accused’s Sixth Amend­
ment right to counsel by “forbidding police to initiate interrogation of a
criminal defendant once he has requested counsel at an arraignment or
similar proceeding.” 556 U. S., at ___ (slip op., at 1). In so doing, the
Court emphasized that because the Edwards “regime suffices to protect
the integrity of ‘a suspect’s voluntary choice not to speak outside his
lawyer’s presence,’ before his arraignment, it is hard to see why it
would not also suffice to protect that same choice after arraignment.”
556 U. S., at ___ (slip op., at 15) (quoting Texas v. Cobb, 532 U. S. 162,
175 (2001) (KENNEDY, J., concurring); citation omitted). But typically,
after arraignment, defendants are released on bail or placed in deten­
tion facilities, both of which, according to the majority’s logic, some­
times constitute breaks in custody. How then, under the Court’s
decision today, will Edwards serve the role that the Court placed on it
in Montejo?
                      Cite as: 559 U. S. ____ (2010)                    11

                  STEVENS, J., concurring in judgment

tive power. But certain things change over time. An
indigent suspect who took police at their word that they
would provide an attorney probably will feel that he has
“been denied the counsel he has clearly requested,”
Roberson, 486 U. S., at 686, when police begin to question
him, without a lawyer, only 14 days later.15 But, when a
suspect has been left alone for a significant period of time,
he is not as likely to draw such conclusions when the
police interrogate him again.16 It is concededly “impossi­
ble to determine with precision” where to draw such a line.
Barker v. Wingo, 407 U. S. 514, 521 (1972). In the case
before us, however, the suspect was returned to the gen­
eral prison population for 2½ years. I am convinced that
——————
   15 The Court responds that “[i]f confidence in the police’s promise to

provide counsel were the touchstone, Edwards would not have applied
in Minnick, where the suspect in continuing custody actually met with
appointed counsel.” Ante, at 17–18. But my view is not that “confi­
dence in the police’s promise to provide counsel” is “the touchtone.”
Ante, at 17. Rather, my view is that although an appropriate break in
custody will mitigate many of the reasons that custodial reinterrogation
of a suspect who requested counsel is inherently compelling, it will not
mitigate the effect of an indigent detainee believing that he has “been
denied the counsel he has clearly requested,” Roberson, 486 U. S., at
686. If police tell an indigent suspect that he is not required to speak
without an attorney, and that they will provide him with an attorney,
and that suspect asserts his right to an attorney, but police nonetheless
do not provide an attorney and reinterrogate him (even if there was a
break in custody between the interrogations), the indigent suspect is
likely to feel that the police lied to him or are ignoring his rights. This
view is not in tension with Minnick. Minnick holds only that consulta­
tion with an attorney between interrogations is not sufficient to end the
Edwards presumption and therefore that when there has been no break
in custody, “counsel’s presence at interrogation,” 498 U. S., at 152, is
necessary to address the compulsion with which the Edwards line of
cases is concerned.
    16 I do not doubt that some of the compulsion caused by reinterrogat­

ing an indigent suspect without providing a lawyer may survive even a
break in custody and a very long passage of time. The relevant point
here is more limited: A long break in time, far longer than 14 days,
diminishes, rather than eliminates, that compulsion.
12                MARYLAND v. SHATZER

              STEVENS, J., concurring in judgment

this period of time is sufficient. I therefore concur in the
judgment.

```

---
