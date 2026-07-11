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

## GROUP: content/cases/Chavez v. Martinez.md  (`case`, 7 assertions)

### content_page

```
---
title: "Chavez v. Martinez"
type: case
citation: "538 U.S. 760 (2003)"
parallel_cite: "123 S. Ct. 1994; 155 L. Ed. 2d 984"
neutral_cite: 2003 U.S. LEXIS 4274
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2003
date_decided: 2003-05-27
docket: 01-1444
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2003-05-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Chavez v. Martinez
  varies_by_point: false
  scope_note: "Fractured decision; the Self-Incrimination holding was reaffirmed and clarified by Vega v. Tekoh (2022). Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/127927/chavez-v-martinez/"
  cluster_id: 127927
  opinion_id: 127927
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny"
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Progeny"
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Related (cross-doctrine)"
related: ["[[Vega v. Tekoh]]", "[[Dickerson v. United States]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "self-incrimination", "section-1983", "qualified-immunity"]
holding: "The Self-Incrimination Clause is a trial right: coercive police questioning that produces no statement used against the suspect in a criminal case is not, by itself, a completed Fifth Amendment violation, so it cannot ground a § 1983 claim. Any remedy for the coercion lies (if at all) in substantive due process — remanded."
lake:
  record_id: Chavez v. Martinez
  status: verified
  projected_at: 2026-07-09
---

# Chavez v. Martinez

*538 U.S. 760 (2003)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officer Chavez questioned Martinez, who had been shot during a police encounter and was receiving emergency treatment, persistently and without [[Miranda and Custodial Interrogation|Miranda warnings]] while Martinez screamed in pain and begged for treatment. Martinez was never charged with a crime and his statements were never used against him in any criminal proceeding. He sued under 42 U.S.C. § 1983, alleging the coercive interrogation violated his Fifth and Fourteenth Amendment rights; the Ninth Circuit denied Chavez [[Qualified Immunity|qualified immunity]].

## Issue
Whether coercive police questioning that yields no statement ever used against the suspect in a criminal case violates the Fifth Amendment's Self-Incrimination Clause (or substantive due process) so as to support a § 1983 damages action.

## Rule
No completed Self-Incrimination Clause violation occurs from the questioning alone. The Fifth Amendment provides that no person "shall be compelled in any criminal case to be a witness against himself," and a plurality concluded: "We fail to see how, based on the text of the Fifth Amendment, Martinez can allege a violation of this right, since Martinez was never prosecuted for a crime, let alone compelled to be a witness against himself in a criminal case." — 538 U.S. at 766 (plurality opinion). ^pin-766

Statements compelled by interrogation may not be used at trial, "but it is not until their use in a criminal case that a violation of the Self-Incrimination Clause occurs" — the privilege is "a fundamental trial right." — [*Id.* at 767](https://www.courtlistener.com/opinion/127927/chavez-v-martinez/#:~:text=but%20it%20is%20not%20until%20their) (plurality op.) (quoting *United States v. Verdugo-Urquidez*). ^pin-767

Because the constitutional self-incrimination claim failed, the officer could not be liable under § 1983 on that theory. A separate question — whether the coercive interrogation independently violated **substantive due process** ("shocks the conscience") — was left open and [[Reading and Citing Cases#on-remand|remanded]].

## Application
On Martinez's own facts the Self-Incrimination Clause was never triggered: he was never prosecuted and his answers were never admitted as testimony against him in a criminal case, so he "was never made to be a 'witness' against himself." Accordingly his § 1983 claim premised on a Fifth Amendment self-incrimination violation could not proceed, and Chavez was entitled to [[Qualified Immunity|qualified immunity]] on that claim. The Court [[Reading and Citing Cases#on-remand|remanded]] Martinez's substantive-due-process claim for the lower courts to address in the first instance.

## Conclusion
Coercive interrogation, standing alone and without use of the statements in a criminal case, is not a completed Fifth Amendment violation and cannot support a § 1983 self-incrimination claim. The judgment was reversed in part and the case [[Reading and Citing Cases#on-remand|remanded]] on the due-process theory. (Fractured Court; Justice Thomas announced the judgment, with Justice Souter (joined by Justice Breyer) supplying the controlling rationale and the remand.)

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The Self-Incrimination-as-trial-right holding was carried forward and sharpened in [[Vega v. Tekoh]] (a Miranda violation is not itself a § 1983-actionable constitutional deprivation). *Chavez* remains the anchor for "no § 1983 self-incrimination claim absent use of the statement in a criminal case."

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny*
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny*
- [[Due-Process Voluntariness of Confessions]] — *Related (cross-doctrine)*

## Sources
- *Chavez v. Martinez*, 538 U.S. 760 (2003) — https://www.courtlistener.com/opinion/127927/chavez-v-martinez/ — pinpoints: 766, 767 (plurality opinion).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5c5d4d31056ac67e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "538 U.S. 760 (2003)", "court": "U.S. Supreme Court", "neutral_cite": "2003 U.S. LEXIS 4274", "official_citation_present": true, "parallel_cite": "123 S. Ct. 1994; 155 L. Ed. 2d 984", "title": "Chavez v. Martinez", "year": "2003"}}
{"assertion_id": "1784226a30be144b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Self-Incrimination Clause is a trial right: coercive police questioning that produces no statement used against the suspect in a criminal case is not, by itself, a completed Fifth Amendment violation, so it cannot ground a § 1983 claim. Any remedy for the coercion lies (if at all) in substantive due process — remanded.", "title": "Chavez v. Martinez"}}
{"assertion_id": "82423a41b40747d2", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Progeny", "title": "Chavez v. Martinez"}}
{"assertion_id": "a016ae008ac1d5bd", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Key — Progeny", "title": "Chavez v. Martinez"}}
{"assertion_id": "de5e18b00172b37b", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Related (cross-doctrine)", "title": "Chavez v. Martinez"}}
{"assertion_id": "3590881f1ea2b8e4", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Chavez v. Martinez"}}
{"assertion_id": "b6cd7b2b4304f222", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2003-05-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Chavez v. Martinez", "field_i_validity": "good_law", "scope_note": "Fractured decision; the Self-Incrimination holding was reaffirmed and clarified by Vega v. Tekoh (2022). Good law.", "title": "Chavez v. Martinez", "varies_by_point": "false"}}
```

### lake record — Chavez v. Martinez

```json
{
  "schema_version": "s2.v1",
  "record_id": "Chavez v. Martinez",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Chavez v. Martinez",
    "case_name_short": "Chavez",
    "case_name_full": "Chavez v. Martinez",
    "input_case_name": "Chavez v. Martinez",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2003-05-27",
    "year": 2003,
    "docket": "01-1444",
    "cluster_id": 127927,
    "lead_opinion_id": 127927,
    "sibling_ids": [
      127927,
      9434450,
      9434451,
      9434452,
      9434453,
      9434454,
      9434455
    ],
    "absolute_url": "/opinion/127927/chavez-v-martinez/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 127891,
        "score": 20,
        "case_name": "Ben Chavez v. Oliverio Martinez"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "538 U.S. 760",
      "volume": "538",
      "reporter": "U.S.",
      "page": "760",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "123 S. Ct. 1994",
        "volume": "123",
        "reporter": "S. Ct.",
        "page": "1994",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "155 L. Ed. 2d 984",
        "volume": "155",
        "reporter": "L. Ed. 2d",
        "page": "984",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2003 U.S. LEXIS 4274",
        "volume": "2003",
        "reporter": "U.S. LEXIS",
        "page": "4274",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "538 U.S. 760",
        "volume": "538",
        "reporter": "U.S.",
        "page": "760",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "123 S. Ct. 1994",
        "volume": "123",
        "reporter": "S. Ct.",
        "page": "1994",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "155 L. Ed. 2d 984",
        "volume": "155",
        "reporter": "L. Ed. 2d",
        "page": "984",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2003 U.S. LEXIS 4274",
        "volume": "2003",
        "reporter": "U.S. LEXIS",
        "page": "4274",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "538 U.S. 760",
    "official_selection": {
      "court_class": "scotus",
      "selected": "538 U.S. 760",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-766",
      "page": null,
      "quote": "--- # Chavez v. Martinez *538 U.S. 760 (2003)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officer Chavez questioned Martinez, who had been shot during a police encounter and was receiving emergency treatment, persistently and without Miranda warnings while Martinez screamed in pain and begged for treatment. Martinez was never charged with a crime and his statements were never used against him in any criminal proceeding. He sued under 42 U.S.C. \u00a7 1983, alleging the coercive interrogation violated his Fifth and Fourteenth Amendment rights; the Ninth Circuit denied Chavez qualified immunity. ## Issue Whether coercive police questioning that yields no statement ever used against the suspect in a criminal case violates the Fifth Amendment's Self-Incrimination Clause (or substantive due process) so as to support a \u00a7 1983 damages action. ## Rule No completed Self-Incrimination Clause violation occurs from the questioning alone. The Fifth Amendment provides that no person",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-767",
      "page": null,
      "quote": "but it is not until their use in a criminal case that a violation of the Self-Incrimination Clause occurs",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 21039,
      "fragment": "#:~:text=but%20it%20is%20not%20until%20their",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2003-05-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Chavez v. Martinez",
    "varies_by_point": false,
    "scope_note": "Fractured decision; the Self-Incrimination holding was reaffirmed and clarified by Vega v. Tekoh (2022). Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Iowa v. Colby Davis Laub",
          "cluster_id": 9493043,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Colby Davis Laub",
          "cluster_id": 9473742,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jamie Peterson v. David Heymes",
          "cluster_id": 4642776,
          "cite": [
            "931 F.3d 546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Anthony Johnson v. Edward Winstead",
          "cluster_id": 4526340,
          "cite": [
            "900 F.3d 428"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chhay Lim",
          "cluster_id": 4522500,
          "cite": [
            "897 F.3d 673"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
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
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kelly Park v. Karen Thompson",
          "cluster_id": 4375052,
          "cite": [
            "851 F.3d 910",
            "2017 WL 971806",
            "2017 U.S. App. LEXIS 4426"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cruz, Adelfo Ramirez",
          "cluster_id": 2950538,
          "cite": [
            "461 S.W.3d 531",
            "2015 Tex. Crim. App. LEXIS 561",
            "2015 WL 2236982"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Marrero-Rodriguez v. Municipality of San Juan",
          "cluster_id": 799410,
          "cite": [
            "677 F.3d 497",
            "2012 U.S. App. LEXIS 9273",
            "2012 WL 1571234"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Uribe",
          "cluster_id": 5810602,
          "cite": [
            "199 Cal. App. 4th 836",
            "132 Cal. Rptr. 3d 102",
            "2011 Cal. App. LEXIS 1253"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Smith v. Almada",
          "cluster_id": 177469,
          "cite": [
            "640 F.3d 931",
            "2011 WL 941606"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Crowe v. County of San Diego",
          "cluster_id": 3065383,
          "cite": [
            "593 F.3d 841",
            "2010 WL 293758"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mayle v. Felix",
          "cluster_id": 799989,
          "cite": [
            "162 L. Ed. 2d 582",
            "125 S. Ct. 2562",
            "545 U.S. 644",
            "2005 U.S. LEXIS 5016"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Seibert",
          "cluster_id": 137002,
          "cite": [
            "159 L. Ed. 2d 643",
            "124 S. Ct. 2601",
            "542 U.S. 600",
            "2004 U.S. LEXIS 4578"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.",
          "cluster_id": 136990,
          "cite": [
            "159 L. Ed. 2d 292",
            "124 S. Ct. 2451",
            "542 U.S. 177",
            "2004 U.S. LEXIS 4385",
            "17 Fla. L. Weekly Fed. S 406",
            "72 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
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
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Patane",
          "cluster_id": 137003,
          "cite": [
            "159 L. Ed. 2d 667",
            "124 S. Ct. 2620",
            "542 U.S. 630",
            "2004 U.S. LEXIS 4577"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittany Morrow v. Barry Balaski",
          "cluster_id": 891221,
          "cite": [
            "719 F.3d 160",
            "98 A.L.R. 6th 777",
            "2013 WL 2466892",
            "2013 U.S. App. LEXIS 11246"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maldonado v. Fontanes",
          "cluster_id": 203857,
          "cite": [
            "568 F.3d 263",
            "2009 U.S. App. LEXIS 12716",
            "2009 WL 1547737"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harold Hall v. City of Los Angeles",
          "cluster_id": 809053,
          "cite": [
            "697 F.3d 1059",
            "83 Fed. R. Serv. 3d 930",
            "2012 WL 4335936",
            "2012 U.S. App. LEXIS 19980"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe Ex Rel. Magee v. Covington County School District",
          "cluster_id": 626050,
          "cite": [
            "675 F.3d 849",
            "2012 U.S. App. LEXIS 6080",
            "2012 WL 976349"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dias v. City and County of Denver",
          "cluster_id": 172192,
          "cite": [
            "567 F.3d 1169",
            "2009 U.S. App. LEXIS 11163",
            "2009 WL 1490359"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Koch v. City of Del City",
          "cluster_id": 616534,
          "cite": [
            "660 F.3d 1228",
            "2011 U.S. App. LEXIS 22095",
            "2011 WL 5176164"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Higazy v. Templeton",
          "cluster_id": 1384819,
          "cite": [
            "505 F.3d 161",
            "2007 WL 3024811"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crowe v. County of San Diego",
          "cluster_id": 148932,
          "cite": [
            "608 F.3d 406",
            "2010 U.S. App. LEXIS 12917",
            "2010 WL 2431842"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Conway",
          "cluster_id": 2718013,
          "cite": [
            "763 F.3d 115",
            "2014 WL 3953234",
            "2014 U.S. App. LEXIS 15589"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Neal",
          "cluster_id": 2588587,
          "cite": [
            "72 P.3d 280",
            "1 Cal. Rptr. 3d 650",
            "31 Cal. 4th 63",
            "2003 Daily Journal DAR 7693",
            "2003 Cal. Daily Op. Serv. 6149",
            "2003 Cal. LEXIS 4426",
            "2003 WL 21639167"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tashiri Wayne Williams",
          "cluster_id": 793121,
          "cite": [
            "435 F.3d 1148",
            "2006 U.S. App. LEXIS 2235",
            "2006 WL 213852"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Seering",
          "cluster_id": 1787414,
          "cite": [
            "701 N.W.2d 655",
            "2005 Iowa Sup. LEXIS 105",
            "2005 WL 1790924"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matthew Livers v. Tim Dunning",
          "cluster_id": 811594,
          "cite": [
            "700 F.3d 340"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hopkins v. Bonvicino",
          "cluster_id": 1448451,
          "cite": [
            "573 F.3d 752",
            "2009 U.S. App. LEXIS 15689",
            "2009 WL 2052987"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Knight Ex Rel. Kerr v. Miami-Dade County",
          "cluster_id": 4389467,
          "cite": [
            "856 F.3d 795",
            "103 Fed. R. Serv. 388",
            "97 Fed. R. Serv. 3d 1086",
            "2017 WL 1755573",
            "2017 U.S. App. LEXIS 8036"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffrey McKinley v. City of Mansfield",
          "cluster_id": 789901,
          "cite": [
            "404 F.3d 418",
            "22 I.E.R. Cas. (BNA) 1254",
            "2005 U.S. App. LEXIS 5875",
            "2005 WL 819969"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sornberger v. City Of Knoxville",
          "cluster_id": 792982,
          "cite": [
            "434 F.3d 1006",
            "2006 U.S. App. LEXIS 1394"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. Earle",
          "cluster_id": 37873,
          "cite": [
            "405 F.3d 278",
            "2005 WL 730071"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lawrence Antelope, United States of America v. Lawrence Antelope",
          "cluster_id": 789030,
          "cite": [
            "395 F.3d 1128",
            "2005 WL 170738"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(127927 OR 9434450 OR 9434451 OR 9434452 OR 9434453 OR 9434454 OR 9434455) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjQ4MzkzNjAwMDAwJnM9MjU5MDM5OCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28127927+OR+9434450+OR+9434451+OR+9434452+OR+9434453+OR+9434454+OR+9434455%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(127927 OR 9434450 OR 9434451 OR 9434452 OR 9434453 OR 9434454 OR 9434455)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDcmcz0xMzQ2MzEyJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28127927+OR+9434450+OR+9434451+OR+9434452+OR+9434453+OR+9434454+OR+9434455%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(127927 OR 9434450 OR 9434451 OR 9434452 OR 9434453 OR 9434454 OR 9434455)",
        "reviewed": 34,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 34,
        "triage_read": 2,
        "triage_snippet_classified": 32
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(127927 OR 9434450 OR 9434451 OR 9434452 OR 9434453 OR 9434454 OR 9434455)",
    "indexed_citing_opinions": 403,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 127927,
        "count": 326,
        "count_source": "search"
      },
      {
        "opinion_id": 9434450,
        "count": 85,
        "count_source": "search"
      },
      {
        "opinion_id": 9434451,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434452,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434453,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434454,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434455,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 902,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/chavez-v-martinez.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MTkwMDkmcz0xMDAyNzkyNiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28127927+OR+9434450+OR+9434451+OR+9434452+OR+9434453+OR+9434454+OR+9434455%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 127927,
        "cited_id": 88493,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 93425,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 100474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 103368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 103748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 104135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 104585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 104813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 104849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 105456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 107238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 107419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 107526,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 107694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 107738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 107739,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 108066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 108301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 108882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 109130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 109400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 109683,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 110821,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 111105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 111549,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 111796,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 111891,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 112341,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 112382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 112699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 112833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 112847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 112924,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 118101,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 118144,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 118242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 121146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 244463,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 340844,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 516470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 583447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 676039,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 775485,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 1634761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 1635158,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 1992428,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 2285307,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "RU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-04T23:57:49Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:58:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:58:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:04:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:58:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Chavez v. Martinez (truncated)

```
<p class="case_cite"><span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/" aria-description="Citation for case: Chavez v. Martinez">538 U.S. 760</a></span></p>
    <p class="parties">CHAVEZ<br>v.<br>MARTINEZ.</p>
    <p class="docket">No. 01-1444.</p>
    <p class="court">Supreme Court of United States.</p>
    <p class="date">Argued December 4, 2002.</p>
    <p class="date">Decided May 27, 2003.</p>
    <div class="prelims">
      <p class="indent">While respondent Martinez was being treated for gunshot wounds received during an altercation with police, he was interrogated by petitioner Chavez, a patrol supervisor. Martinez admitted that he used heroin and had taken an officer's gun during the incident. At no point was Martinez given <i>Miranda</i> warnings. Although he was never charged with a crime, and his answers were never used against him in any criminal proceeding, Martinez filed a <span class="citation no-link">42 U. S. C. &#167; 1983</span> suit, maintaining, among other things, that Chavez's actions violated his Fifth Amendment right not to be "compelled in any criminal case to be a witness against himself," and his Fourteenth Amendment substantive due process right to be free from coercive questioning. The District Court ruled that Chavez was not entitled to qualified immunity, and the Ninth Circuit affirmed, finding that Chavez's coercive questioning violated Martinez's Fifth Amendment rights even though his statements were not used against him in a criminal proceeding, and that a police officer violates due process when he obtains a confession by coercive conduct, regardless of whether the confession is subsequently used at trial.</p>
      <p class="indent"><i>Held:</i> The judgment is reversed, and the case is remanded.</p>
      <p class="indent"><span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police...">270 F. 3d 852</a></span>, reversed and remanded.</p>
      <p class="indent">JUSTICE THOMAS, joined by THE CHIEF JUSTICE, JUSTICE O'CONNOR, and JUSTICE SCALIA, concluded in Part II-A that Chavez did not deprive Martinez of his Fifth Amendment rights. Pp. 766-773.</p>
    </div>
    <div class="num" id="p1">
      <span class="num">1</span>
      <p class="indent">(a) An officer is entitled to qualified immunity if his alleged conduct did not violate a constitutional right. See <i>Saucier</i> v. <i>Katz,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./533/194/">533 U. S. 194</a></span>, 201. The text of the Fifth Amendment's Self-Incrimination Clause cannot support the Ninth Circuit's view that mere compulsive questioning violates the Constitution. A "criminal case" at the very least requires the initiation of legal proceedings, and police questioning does not constitute such a case. Statements compelled by police interrogation may not be used against a defendant in a criminal case, but it is not until such use that the Self-Incrimination Clause is violated, see <i>United States</i> v. <i>Verdugo-Urquidez,</i> <span class="citation" data-id="9431925"><a href="/opinion/112382/united-states-v-verdugo-urquidez/#264" aria-description="Citation for case: United States v. Verdugo-Urquidez">494 U. S. 259, 264</a></span>. Martinez was never made to be a "witness" against himself because his statements were never admitted as testimony against him in a criminal case. Nor was he ever placed under oath and exposed to "`the cruel trilemma of self-accusation, perjury or contempt.'" <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#445" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 445</a></span>. Pp. 766-767.</p>
    </div>
    <div class="num" id="p2">
      <span class="num">2</span>
      <p class="indent">(b) The Ninth Circuit's approach is also irreconcilable with this Court's case law. The government may compel witnesses to testify at trial or before a grand jury, on pain of contempt, so long as the witness is not the target of the criminal case in which he testifies, see, <i>e. g., Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#443" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 443</a></span>; and this Court has long permitted the compulsion of incriminating testimony so long as the statements (or evidence derived from them) cannot be used against the speaker in a criminal case, <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#458" aria-description="Citation for case: Kastigar v. United States"><i>id.,</i> at 458</a></span>. Martinez was no more compelled in a criminal case to be a witness against himself than an immunized witness forced to testify on pain of contempt. That an immunized witness knows that his statements may not be used against him, while Martinez likely did not, does not make the immunized witness' statements any less compelled and lends no support to the Ninth Circuit's conclusion that coercive police interrogations alone violate the Fifth Amendment. Moreover, those subjected to coercive interrogations have an automatic protection from the use of their involuntary statements in any subsequent criminal trial, <i>e. g., Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#307" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 307-308</a></span>, which is coextensive with the use and derivative use immunity mandated by <i>Kastigar.</i> Pp. 767-770.</p>
    </div>
    <div class="num" id="p3">
      <span class="num">3</span>
      <p class="indent">(c) The fact that the Court has permitted the Fifth Amendment privilege to be asserted in noncriminal cases does not alter the conclusion in this case. Judicially created prophylactic rules &#8212; such as the rule allowing a witness to insist on an immunity agreement before being compelled to give testimony in noncriminal cases, and the exclusionary rule &#8212; are designed to safeguard the core constitutional right protected by the Self-Incrimination Clause. They do not extend the scope of that right itself, just as violations of such rules do not violate a person's constitutional rights. Accordingly, Chavez's failure to read <i>Miranda</i> warnings to Martinez did not violate Martinez's constitutional rights and cannot be grounds for a &#167; 1983 action. And the absence of a "criminal case" in which Martinez was compelled to be a "witness" against himself defeats his core Fifth Amendment claim. Pp. 770-773.</p>
    </div>
    <div class="num" id="p4">
      <span class="num">4</span>
      <p class="indent">JUSTICE SOUTER delivered the opinion of the Court with respect to Part II, concluding that the issue whether Martinez may pursue a claim of liability for a substantive due process violation should be addressed on remand. Pp. 779-780.</p>
    </div>
    <div class="num" id="p5">
      <span class="num">5</span>
      <p class="indent">JUSTICE SOUTER, joined by JUSTICE BREYER, concluded in Part I that Martinez's claim that his questioning alone was a violation of the Fifth and Fourteenth Amendments subject to redress by a <span class="citation no-link">42 U. S. C. &#167; 1983</span> damages action, though outside the core of Fifth Amendment protection, could be recognized if a core guarantee, or the judicial capacity to protect it, would be placed at risk absent complementary protection, see, <i>e. g., McCarthy</i> v. <i>Arndstein,</i> <span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/#40" aria-description="Citation for case: McCarthy v. Arndstein">266 U. S. 34, 40</a></span>. However, Martinez cannot make the "powerful showing" necessary to expand protection of the privilege against self-incrimination to the point of the civil liability he requests. Inherent in his purely Fifth Amendment claim is the risk of global application in every instance of interrogation producing a statement inadmissible under the Fifth and Fourteenth Amendments, or violating one of the complementary rules this Court has accepted in aid of the core privilege. And Martinez has offered no reason to believe that this new rule is necessary in aid of the basic guarantee. Pp. 777-779.</p>
    </div>
    <div class="num" id="p6">
      <span class="num">6</span>
      <p class="indent">THOMAS, J., announced the judgment of the Court and delivered an opinion, which was joined by REHNQUIST, C. J., in full, by O'CONNOR, J., as to Parts I and II-A, and by SCALIA, J., as to Parts I and II. SOUTER, J., delivered an opinion, Part II of which was for the Court and was joined by STEVENS, KENNEDY, GINSBURG, and BREYER, JJ., and Part I of which concurred in the judgment and was joined by BREYER, J., <i>post,</i> p. 777. SCALIA, J., filed an opinion concurring in part in the judgment, <i>post,</i> p. 780. STEVENS, J., filed an opinion concurring in part and dissenting in part, <i>post,</i> p. 783. KENNEDY, J., filed an opinion concurring in part and dissenting in part, which was joined by STEVENS, J., in full and by GINSBURG, J., as to Parts II and III, <i>post,</i> p. 789. GINSBURG, J., filed an opinion concurring in part and dissenting in part, <i>post,</i> p. 799.</p>
    </div>
    <div class="num" id="p7">
      <span class="num">7</span>
      <p class="indent">CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.</p>
    </div>
    <div class="num" id="p8">
      <span class="num">8</span>
      <p class="indent"><i>Lawrence S. Robbins</i> argued the cause for petitioner. With him on the briefs were <i>Roy T. Englert, Jr., Kathryn S. Zecca, Alan E. Wisotsky, Jeffrey Held,</i> and <i>Gary L. Gillig.</i></p>
    </div>
    <div class="num" id="p9">
      <span class="num">9</span>
      <p class="indent"><i>Deputy Solicitor General Clement</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Olson, Assistant Attorney General Chertoff, Assistant Attorney General McCallum, John P. Elwood, Barbara L. Herwig,</i> and <i>Peter R. Maier.</i></p>
    </div>
    <div class="num" id="p10">
      <span class="num">10</span>
      <p class="indent"><i>Richard S. Paz</i> argued the cause for respondent. With him on the brief was <i>Sonia Mercado.</i><a class="footnote" href="#fn-s-3" id="fn-s-3_ref">*</a></p>
    </div>
    <div class="num" id="p11">
      <span class="num">11</span>
      <p class="indent">JUSTICE THOMAS announced the judgment of the Court and delivered an opinion.<a class="footnote" href="#fn-s-4" id="fn-s-4_ref">*</a></p>
    </div>
    <div class="num" id="p12">
      <span class="num">12</span>
      <p class="indent">This case involves a <span class="citation no-link">42 U. S. C. &#167; 1983</span> suit arising out of petitioner Ben Chavez's allegedly coercive interrogation of respondent Oliverio Martinez. The United States Court of Appeals for the Ninth Circuit held that Chavez was not entitled to a defense of qualified immunity because he violated Martinez's clearly established constitutional rights. We conclude that Chavez did not deprive Martinez of a constitutional right.</p>
    </div>
    <div class="num" id="p13">
      <span class="num">13</span>
      <p class="indent">* On November 28, 1997, police officers Maria Pe&#241;a and Andrew Salinas were near a vacant lot in a residential area of Oxnard, California, investigating suspected narcotics activity. While Pe&#241;a and Salinas were questioning an individual, they heard a bicycle approaching on a darkened path that crossed the lot. They ordered the rider, respondent Martinez, to dismount, spread his legs, and place his hands behind his head. Martinez complied. Salinas then conducted a patdown frisk and discovered a knife in Martinez's waistband. An altercation ensued.<a class="footnote" href="#fn1" id="fn1_ref">1</a></p>
    </div>
    <div class="num" id="p14">
      <span class="num">14</span>
      <p class="indent">There is some dispute about what occurred during the altercation. The officers claim that Martinez drew Salinas' gun from its holster and pointed it at them; Martinez denies this. Both sides agree, however, that Salinas yelled, "`He's got my gun!'" App. to Pet. for Cert. 3a. Pe&#241;a then drew her gun and shot Martinez several times, causing severe injuries that left Martinez permanently blinded and paralyzed from the waist down. The officers then placed Martinez under arrest.</p>
    </div>
    <div class="num" id="p15">
      <span class="num">15</span>
      <p class="indent">Petitioner Chavez, a patrol supervisor, arrived on the scene minutes later with paramedics. Chavez accompanied Martinez to the hospital and then questioned Martinez there while he was receiving treatment from medical personnel. The interview lasted a total of about 10 minutes, over a 45-minute period, with Chavez leaving the emergency room for periods of time to permit medical personnel to attend to Martinez.</p>
    </div>
    <div class="num" id="p16">
      <span class="num">16</span>
      <p class="indent">At first, most of Martinez's answers consisted of "I don't know," "I am dying," and "I am choking." App. 14, 17, 18. Later in the interview, Martinez admitted that he took the gun from the officer's holster and pointed it at the police. <span class="citation no-link"><i>Id.,</i> at 16</span>. He also admitted that he used heroin regularly. <span class="citation no-link"><i>Id.,</i> at 18</span>. At one point, Martinez said "I am not telling you anything until they treat me," yet Chavez continued the interview. <span class="citation no-link"><i>Id.,</i> at 14</span>. At no point during the interview was Martinez given warnings under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). App. to Pet. for Cert. 4a.</p>
    </div>
    <div class="num" id="p17">
      <span class="num">17</span>
      <p class="indent">Martinez was never charged with a crime, and his answers were never used against him in any criminal prosecution. Nevertheless, Martinez filed suit under Rev. Stat. &#167; 1979, <span class="citation no-link">42 U. S. C. &#167; 1983</span>, maintaining that Chavez's actions violated his Fifth Amendment right not to be "compelled in any criminal case to be a witness against himself," as well as his Fourteenth Amendment substantive due process right to be free from coercive questioning. The District Court granted summary judgment to Martinez as to Chavez's qualified immunity defense on both the Fifth and Fourteenth Amendment claims. Chavez took an interlocutory appeal to the Ninth Circuit, which affirmed the District Court's denial of qualified immunity. <i>Martinez</i> v. <i>Oxnard,</i> <span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police...">270 F. 3d 852</a></span> (2001). Applying <i>Saucier</i> v. <i>Katz,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./533/194/">533 U. S. 194</a></span> (2001), the Ninth Circuit first concluded that Chavez's actions, as alleged by Martinez, deprived Martinez of his rights under the Fifth and Fourteenth Amendments. The Ninth Circuit did not attempt to explain how Martinez had been "compelled in any criminal case to be a witness against himself." Instead, the Ninth Circuit reiterated the holding of an earlier Ninth Circuit case, <i>Cooper</i> v. <i>Dupnik,</i> <span class="citation" data-id="9000842"><a href="/opinion/9008075/cooper-v-dupnik/#1229" aria-description="Citation for case: Cooper v. Dupnik">963 F. 2d 1220, 1229</a></span> (1992) (en banc), that "the Fifth Amendment's purpose is to prevent coercive interrogation practices that are destructive of human dignity," <span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/#857" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police...">270 F. 3d, at 857</a></span> (internal quotation marks omitted), and found that Chavez's "coercive questioning" of Martinez violated his Fifth Amendment rights, "[e]ven though Martinez's statements were not used against him in a criminal proceeding," <i><span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police...">ibid.</a></span></i> As to Martinez's due process claim, the Ninth Circuit held that "a police officer violates the Fourteenth Amendment when he obtains a confession by coercive conduct, regardless of whether the confession is subsequently used at trial." <i><span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police...">Ibid.</a></span></i></p>
    </div>
    <div class="num" id="p18">
      <span class="num">18</span>
      <p class="indent">The Ninth Circuit then concluded that the Fifth and Fourteenth Amendment rights asserted by Martinez were clearly established by federal law, explaining that a reasonable officer "would have known that persistent interrogation of the suspect despite repeated requests to stop violated the suspect's Fifth and Fourteenth Amendment right to be free from coercive interrogation." <span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/#858" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police..."><i>Id.,</i> at 858</a></span>.</p>
    </div>
    <div class="num" id="p19">
      <span class="num">19</span>
      <p class="indent">We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./535/1111/">535 U. S. 1111</a></span> (2002).</p>
    </div>
    <p>II</p>
    <div class="num" id="p20">
      <span class="num">20</span>
      <p class="indent">In deciding whether an officer is entitled to qualified immunity, we must first determine whether the officer's alleged conduct violated a constitutional right. See <i>Katz,</i> 533 U. S., at 201. If not, the officer is entitled to qualified immunity, and we need not consider whether the asserted right was "clearly established." <i>Ibid.</i> We conclude that Martinez's allegations fail to state a violation of his constitutional rights.</p>
    </div>
    <div class="num" id="p21">
      <span class="num">21</span>
      <p>* 1</p>
    </div>
    <div class="num" id="p22">
      <span class="num">22</span>
      <p class="indent">The Fifth Amendment, made applicable to the States by the Fourteenth Amendment, <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964), requires that "[n]o person ... shall be compelled <i>in any criminal case</i> to be a <i>witness</i> against himself." U. S. Const., Amdt. 5 (emphases added). We fail to see how, based on the text of the Fifth Amendment, Martinez can allege a violation of this right, since Martinez was never prosecuted for a crime, let alone compelled to be a witness against himself in a criminal case.</p>
    </div>
    <div class="num" id="p23">
      <span class="num">23</span>
      <p class="indent">Although Martinez contends that the meaning of "criminal case" should encompass the entire criminal investigatory process, including police interrogations, Brief for Respondent 23, we disagree. In our view, a "criminal case" at the very least requires the initiation of legal proceedings. See <i>Blyew</i> v. <i>United States,</i> <span class="citation" data-id="9416852"><a href="/opinion/88493/blyew-v-united-states/#595" aria-description="Citation for case: Blyew v. United States">13 Wall. 581, 595</a></span> (1872) ("The words `case' and `cause' are constantly used as synonyms in statutes and judicial decisions, each meaning <i>a proceeding in court, a suit, or action</i>" (emphasis added)); Black's Law Dictionary 215 (6th ed. 1990) (defining "[c]ase" as "[a] general term for an action, cause, suit, or controversy at law ...; a question <i>contested before a court of justice</i>" (emphasis added)). We need not decide today the precise moment when a "criminal case" commences; it is enough to say that police questioning does not constitute a "case" any more than a private investigator's precomplaint activities constitute a "civil case." Statements compelled by police interrogations of course may not be used against a defendant at trial, see <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#286" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278, 286</a></span> (1936), but it is not until their use in a criminal case that a violation of the Self-Incrimination Clause occurs, see <i>United States</i> v. <i>Verdugo-Urquidez,</i> <span class="citation" data-id="9431925"><a href="/opinion/112382/united-states-v-verdugo-urquidez/#264" aria-description="Citation for case: United States v. Verdugo-Urquidez">494 U. S. 259, 264</a></span> (1990) ("The privilege against self-incrimination guaranteed by the Fifth Amendment is <i>a fundamental trial right</i> of criminal defendants. Although conduct by law enforcement officials prior to trial may ultimately impair that right, <i>a constitutional violation occurs only at trial</i>" (emphases added; citations omitted)); <i>Withrow</i> v. <i>Williams,</i> <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#692" aria-description="Citation for case: Withrow v. Williams">507 U. S. 680, 692</a></span> (1993) (describing the Fifth Amendment as a "`trial right'"); <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#705" aria-description="Citation for case: Withrow v. Williams"><i>id.,</i> at 705</a></span> (O'CONNOR, J., concurring in part and dissenting in part) (describing "true Fifth Amendment claims" as "the extraction <i>and use</i> of compelled testimony" (emphasis altered)).</p>
    </div>
    <div class="num" id="p24">
      <span class="num">24</span>
      <p class="indent">Here, Martinez was never made to be a "witness" against himself in violation of the Fifth Amendment's Self-Incrimination Clause because his statements were never admitted as testimony against him in a criminal case. Nor was he ever placed under oath and exposed to "`the cruel trilemma of self-accusation, perjury or contempt.'" <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#445" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 445</a></span> (1974) (quoting <i>Murphy</i> v. <i>Waterfront Comm'n of N. Y. Harbor,</i> <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#55" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 55</a></span> (1964)). The text of the Self-Incrimination Clause simply cannot support the Ninth Circuit's view that the mere use of compulsive questioning, without more, violates the Constitution.</p>
    </div>
    <p>2</p>
    <div class="num" id="p25">
      <span class="num">25</span>
      <p class="indent">Nor can the Ninth Circuit's approach be reconciled with our case law. It is well established that the government may compel witnesses to testify at trial or before a grand jury, on pain of contempt, so long as the witness is not the target of the criminal case in which he testifies. See <i>Minnesota</i> v. <i>Murphy,</i> <span class="citation" data-id="9429504"><a href="/opinion/111105/minnesota-v-murphy/#427" aria-description="Citation for case: Minnesota v. Murphy">465 U. S. 420, 427</a></span> (1984); <i>Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#443" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 443</a></span> (1972). Even for persons who have a legitimate fear that their statements may subject them to criminal prosecution, we have long permitted the compulsion of incriminating testimony so long as those statements (or evidence derived from those statements) cannot be used against the speaker in any criminal case. See <i>Brown</i> v. <i>Walker,</i> <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#602" aria-description="Citation for case: Brown v. Walker">161 U. S. 591, 602-604</a></span> (1896); <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#458" aria-description="Citation for case: Kastigar v. United States"><i>Kastigar, supra,</i> at 458</a></span>; <i>United States</i> v. <i>Balsys,</i> <span class="citation" data-id="9433709"><a href="/opinion/118242/united-states-v-balsys/#671" aria-description="Citation for case: United States v. Balsys">524 U. S. 666, 671-672</a></span> (1998). We have also recognized that governments may penalize public employees and government contractors (with the loss of their jobs or government contracts) to induce them to respond to inquiries, so long as the answers elicited (and their fruits) are immunized from use in any criminal case against the speaker. See <i>Lefkowitz</i> v. <i>Turley,</i> <span class="citation" data-id="108882"><a href="/opinion/108882/lefkowitz-v-turley/#84" aria-description="Citation for case: Lefkowitz v. Turley">414 U. S. 70, 84-85</a></span> (1973) ("[T]he State may insist that [contractors] ... either respond to relevant inquiries about the performance of their contracts or suffer cancellation"); <i>Lefkowitz</i> v. <i>Cunningham,</i> <span class="citation" data-id="9426845"><a href="/opinion/109683/lefkowitz-v-cunningham/#806" aria-description="Citation for case: Lefkowitz v. Cunningham">431 U. S. 801, 806</a></span> (1977) ("Public employees may constitutionally be discharged for refusing to answer potentially incriminating questions concerning their official duties if they have not been required to surrender their constitutional immunity" against later use of statements in criminal proceedings).<a class="footnote" href="#fn2" id="fn2_ref">2</a> By contrast, no "penalty" may ever be imposed on someone who exercises his core Fifth Amendment right not to be a "witness" against himself in a "criminal case." See <i>Griffin</i> v. <i>California,</i> <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/#614" aria-description="Citation for case: Griffin v. California">380 U. S. 609, 614</a></span> (1965) (the trial court's and the prosecutor's comments on the defendant's failure to testify violates the Self-Incrimination Clause of the Fifth Amendment). Our holdings in these cases demonstrate that, contrary to the Ninth Circuit's view, mere coercion does not violate the text of the Self-Incrimination Clause absent use of the compelled statements in a criminal case against the witness.</p>
    </div>
    <div class="num" id="p26">
      <span class="num">26</span>
      <p class="indent">We fail to see how Martinez was any more "compelled in any criminal case to be a witness against himself" than an immunized witness forced to testify on pain of contempt. One difference, perhaps, is that the immunized witness <i>knows</i> that his statements will not, and may not, be used against him, whereas Martinez likely did not. But this does not make the statements of the immunized witness any less "compelled" and lends no support to the Ninth Circuit's conclusion that coercive police interrogations, absent the use of the involuntary statements in a criminal case, violate the Fifth Amendment's Self-Incrimination Clause. Moreover, our cases provide that those subjected to coercive police interrogations have an <i>automatic</i> protection from the use of their involuntary statements (or evidence derived from their statements) in any subsequent criminal trial. <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#307" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 307-308</a></span> (1985); <i>United States</i> v. <i>Blue,</i> <span class="citation" data-id="107238"><a href="/opinion/107238/united-states-v-blue/#255" aria-description="Citation for case: United States v. Blue">384 U. S. 251, 255</a></span> (1966); <i>Leyra</i> v. <i>Denno,</i> <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/#558" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556, 558</a></span> (1954); <i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/#155" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143, 155</a></span> (1944). See also <i>Pillsbury Co.</i> v. <i>Conboy,</i> <span class="citation" data-id="9428983"><a href="/opinion/110821/pillsbury-co-v-conboy/#278" aria-description="Citation for case: Pillsbury Co. v. Conboy">459 U. S. 248, 278</a></span> (1983) (Blackmun, J., concurring in judgment); <i>Williams</i> v. <i>United States,</i> <span class="citation" data-id="9424503"><a href="/opinion/108301/williams-v-united-states/#662" aria-description="Citation for case: Williams v. United States">401 U. S. 646, 662</a></span> (1971) (Brennan, J., concurring in result). This protection is, in fact, coextensive with the use and derivative use immunity mandated by <i><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span></i> when the government compels testimony from a reluctant witness. See <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#453" aria-description="Citation for case: Kastigar v. United States">406 U. S., at 453</a></span>. Accordingly, the fact that Martinez did not <i>know</i> his statements could not be used against him does not change our view that no violation of the Fifth Amendment's Self-Incrimination Clause occurred here.</p>
    </div>
    <p>3</p>
    <div class="num" id="p27">
      <span class="num">27</span>
      <p class="indent">Although our cases have permitted the Fifth Amendment's self-incrimination privilege to be asserted in noncriminal cases, see <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#444" aria-description="Citation for case: Kastigar v. United States"><i>id.,</i> at 444-445</a></span> (recognizing that the "Fifth Amendment privilege against compulsory self-incrimination ... <i>can be asserted in any proceeding,</i> civil or criminal, administrative or judicial, investigatory or adjudicatory ..."); <i>Lefkowitz</i> v. <span class="citation" data-id="108882"><a href="/opinion/108882/lefkowitz-v-turley/#77" aria-description="Citation for case: Lefkowitz v. Turley"><i>Turley, supra,</i> at 77</a></span> (stating that the Fifth Amendment privilege allows one "not to answer official questions put to him in any other proceeding, civil or criminal, formal or informal, where the answers might incriminate him in future criminal proceedings"), that does not alter our conclusion that a violation of the constitutional <i>right</i> against self-incrimination occurs only if one has been compelled to be a witness against himself in a criminal case.</p>
    </div>
    <div class="num" id="p28">
      <span class="num">28</span>
      <p class="indent">In the Fifth Amendment context, we have created prophylactic rules designed to safeguard the core constitutional right protected by the Self-Incrimination Clause. See, <i>e. g., Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S., at 444</a></span> (describing the "procedural safeguards" required by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> as "not themselves rights protected by the Constitution but ... measures to insure that the right against compulsory self-incrimination was protected" to "provide practical reinforcement for the right"); <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#306" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 306</a></span> (stating that "[t]he <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> exclusionary rule ... serves the Fifth Amendment and sweeps more broadly than the Fifth Amendment itself"). Among these rules is an evidentiary privilege that protects witnesses from being forced to give incriminating testimony, even in noncriminal cases, unless that testimony has been immunized from use and derivative use in a future criminal proceeding before it is compelled. See <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#453" aria-description="Citation for case: Kastigar v. United States"><i>Kastigar, supra,</i> at 453</a></span>; <i>Maness</i> v. <i>Meyers,</i> <span class="citation" data-id="9425898"><a href="/opinion/109130/maness-v-meyers/#461" aria-description="Citation for case: Maness v. Meyers">419 U. S. 449, 461-462</a></span> (1975) (noting that the Fifth Amendment privilege may be asserted if one is "compelled to produce evidence which later <i>may</i> be used against him as an accused in a criminal action" (emphasis added)).</p>
    </div>
    <div class="num" id="p29">
      <span class="num">29</span>
      <p class="indent">By allowing a witness to insist on an immunity agreement <i>before</i> being compelled to give incriminating testimony in a noncriminal case, the privilege preserves the core Fifth Amendment right from invasion by the use of that compelled testimony in a subsequent criminal case. See <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#440" aria-description="Citation for case: Michigan v. Tucker"><i>Tucker, supra,</i> at 440-441</a></span> ("Testimony obtained in civil suits, or before administrative or legislative committees, could [absent a grant of immunity] prove so incriminating that a person compelled to give such testimony might readily be convicted on the basis of those disclosures in a subsequent criminal proceeding"). Because the failure to assert the privilege will often forfeit the right to exclude the evidence in a subsequent "criminal case," see <i>Murphy,</i> <span class="citation" data-id="9429504"><a href="/opinion/111105/minnesota-v-murphy/#440" aria-description="Citation for case: Minnesota v. Murphy">465 U. S., at 440</a></span>; <i>Garner</i> v. <i>United States,</i> <span class="citation" data-id="9426311"><a href="/opinion/109400/garner-v-united-states/#650" aria-description="Citation for case: Garner v. United States">424 U. S. 648, 650</a></span> (1976) (failure to claim privilege against self-incrimination before disclosing incriminating information on tax returns forfeited the right to exclude that information in a criminal prosecution); <i>United States</i> v. <i>Kordel,</i> <span class="citation" data-id="108066"><a href="/opinion/108066/united-states-v-kordel/#7" aria-description="Citation for case: United States v. Kordel">397 U. S. 1, 7</a></span> (1970) (criminal defendant forfeited his right to assert Fifth Amendment privilege with regard to answers he gave to interrogatories in a prior civil proceeding), it is necessary to allow assertion of the privilege prior to the commencement of a "criminal case" to safeguard the core Fifth Amendment trial right. If the privilege could not be asserted in such situations, testimony given in those judicial proceedings would be deemed "voluntary," see <i>Rogers</i> v. <i>United States,</i> <span class="citation" data-id="9420532"><a href="/opinion/104849/rogers-v-united-states/#371" aria-description="Citation for case: Rogers v. United States">340 U. S. 367, 371</a></span> (1951); <i>United States</i> v. <i>Monia,</i> <span class="citation" data-id="9419281"><a href="/opinion/103748/united-states-v-monia/#427" aria-description="Citation for case: United States v. Monia">317 U. S. 424, 427</a></span> (1943); hence, insistence on a prior grant of immunity is essential to memorialize the fact that the testimony had indeed been compelled and therefore protected from use against the speaker in any "criminal case."</p>
    </div>
    <div class="num" id="p30">
      <span class="num">30</span>
      <p class="indent">Rules designed to safeguard a constitutional right, however, do not extend the scope of the constitutional right itself, just as violations of judicially crafted prophylactic rules do not violate the constitutional rights of any person. As we explained, we have allowed the Fifth Amendment privilege to be asserted by witnesses in noncriminal cases in order to safeguard the core constitutional right defined by the Self-Incrimination Clause &#8212; the right not to be compelled in any criminal case to be a witness against oneself.<a class="footnote" href="#fn3" id="fn3_ref">3</a> We have likewise established the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> exclusionary rule as a prophylactic measure to prevent violations of the right protected by the text of the Self-Incrimination Clause &#8212; the admission into evidence in a criminal case of confessions obtained through coercive custodial questioning. See <i>Warren</i> v. <i>Lincoln,</i> <span class="citation" data-id="9478572"><a href="/opinion/516470/jackson-warren-v-city-of-lincoln-nebraska-james-breen-sandra-l-myers-and/#1442" aria-description="Citation for case: Jackson Warren v. City of Lincoln, Nebraska James Breen...">864 F. 2d 1436, 1442</a></span> (CA8 1989) (alleged <i>Miranda</i> violation not actionable under &#167; 1983); <i>Giuffre</i> v. <i>Bissell,</i> <span class="citation" data-id="676039"><a href="/opinion/676039/james-j-giuffre-v-nicholas-bissell-richard-thornburg-robert-smith-russ/#1256" aria-description="Citation for case: James J. Giuffre v. Nicholas Bissell Richard Thornburg...">31 F. 3d 1241, 1256</a></span> (CA3 1994) (same); <i>Bennett</i> v. <i>Passic,</i> <span class="citation" data-id="340844"><a href="/opinion/340844/howard-smith-bennett-v-albert-passic-sheriff-etc/#1263" aria-description="Citation for case: Howard Smith Bennett v. Albert Passic, Sheriff, Etc.">545 F. 2d 1260, 1263</a></span> (CA10 1976) (same); see also <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#686" aria-description="Citation for case: New York v. Quarles">467 U. S. 649, 686</a></span> (1984) (Marshall, J., dissenting) ("All the Fifth Amendment forbids is the introduction of coerced statements at trial"). Accordingly, Chavez's failure to read <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings to Martinez did not violate Martinez's constitutional rights and cannot be grounds for a &#167; 1983 action. See <i>Connecticut</i> v. <i>Barrett,</i> <span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/#528" aria-description="Citation for case: Connecticut v. Barrett">479 U. S. 523, 528</a></span> (1987) (<i>Miranda</i>'s warning requirement is "not itself required by the Fifth Amendmen[t] ... but is instead justified only by reference to its prophylactic purpose"); <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker"><i>Tucker, supra,</i> at 444</a></span> (<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span>'s safeguards "were not themselves rights protected by the Constitution but were instead measures to insure that the right against compulsory self-incrimination was protected"). And the absence of a "criminal case" in which Martinez was compelled to be a "witness" against himself defeats his core Fifth Amendment claim. The Ninth Circuit's view that mere compulsion violates the Self-Incrimination Clause, see <span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/#857" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police...">270 F. 3d, at 857</a></span>; <i>California Attorneys for Criminal Justice</i> v. <i>Butts,</i> <span class="citation" data-id="6984365"><a href="/opinion/7079352/california-attorneys-for-criminal-justice-v-butts/#1045" aria-description="Citation for case: California Attorneys for Criminal Justice v. Butts">195 F. 3d 1039, 1045-1046</a></span> (1999); <i>Cooper,</i> <span class="citation" data-id="9000842"><a href="/opinion/9008075/cooper-v-dupnik/#1243" aria-description="Citation for case: Cooper v. Dupnik">963 F. 2d, at 1243-1244</a></span>, finds no support in the text of the Fifth Amendment and is irreconcilable with our case law.<a class="footnote" href="#fn4" id="fn4_ref">4</a> Because we find that Chavez's alleged conduct did not violate the Self-Incrimination Clause, we reverse the Ninth Circuit's denial of qualified immunity as to Martinez's Fifth Amendment claim.</p>
    </div>
    <div class="num" id="p31">
      <span class="num">31</span>
      <p class="indent">Our views on the proper scope of the Fifth Amendment's Self-Incrimination Clause do not mean that police torture or other abuse that results in a confession is constitutionally permissible so long as the statements are not used at trial; it simply means that the Fourteenth Amendment's Due Process Clause, rather than the Fifth Amendment's Self-Incrimination Clause, would govern the inquiry in those cases and provide relief in appropriate circumstances.<a class="footnote" href="#fn5" id="fn5_ref">5</a></p>
    </div>
    <p class="center">B</p>
    <div class="num" id="p32">
      <span class="num">32</span>
      <p class="indent">The Fourteenth Amendment provides that no person shall be deprived "of life, liberty, or property, without due process of law." Convictions based on evidence obtained by methods that are "so brutal and so offensive to human dignity" that they "shoc[k] the conscience" violate the Due Process Clause. <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#172" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 172, 174</a></span> (1952) (overturning conviction based on evidence obtained by involuntary stomach pumping). See also <i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#435" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 435</a></span> (1957) (reiterating that evidence obtained through conduct that "`shock[s] the conscience'" may not be used to support a criminal conviction). Although <i><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span></i> did not establish a civil remedy for abusive police behavior, we recognized in <i>County of Sacramento</i> v. <i>Lewis,</i> <span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#846" aria-description="Citation for case: County of Sacramento v. Lewis">523 U. S. 833, 846</a></span> (1998), that deprivations of liberty caused by "the most egregious official conduct," <span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#846" aria-description="Citation for case: County of Sacramento v. Lewis"><i>id.,</i> at 846, 847-848, n. 8</a></span>, may violate the Due Process Clause. While we rejected, in <i><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">Lewis</a></span>,</i> a &#167; 1983 plaintiff's contention that a police officer's deliberate indifference during a high-speed chase that caused the death of a motorcyclist violated due process, <i>id.,</i> at 854, we left open the possibility that unauthorized police behavior in other contexts might "shock the conscience" and give rise to &#167; 1983 liability. <i>Id.,</i> at 850.</p>
    </div>
    <div class="num" id="p33">
      <span class="num">33</span>
      <p class="indent">We are satisfied that Chavez's questioning did not violate Martinez's due process rights. Even assuming, <i>arguendo,</i> that the persistent questioning of Martinez somehow deprived him of a liberty interest, we cannot agree with Martinez's characterization of Chavez's behavior as "egregious" or "conscience shocking." As we noted in <i><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">Lewis</a></span>,</i> the official conduct "most likely to rise to the conscience-shocking level" is the "conduct intended to injure in some way unjustifiable by any government interest." <span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#849" aria-description="Citation for case: County of Sacramento v. Lewis"><i>Id.,</i> at 849</a></span>. Here, there is no evidence that Chavez acted with a purpose to harm Martinez by intentionally interfering with his medical treatment. Medical personnel were able to treat Martinez throughout the interview, App. to Pet. for Cert. 4a, 18a, and Chavez ceased his questioning to allow tests and other procedures to be performed. <i><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">Id.,</a></span></i> at 4a. Nor is there evidence that Chavez's conduct exacerbated Martinez's injuries or prolonged his stay in the hospital. Moreover, the need to investigate whether there had been police misconduct constituted a justifiable government interest given the risk that key evidence would have been lost if Martinez had died without the authorities ever hearing his side of the story.</p>
    </div>
    <div class="num" id="p34">
      <span class="num">34</span>
      <p class="indent">The Court has held that the Due Process Clause also protects certain "fundamental liberty interest[s]" from deprivation by the government, regardless of the procedures provided, unless the infringement is narrowly tailored to serve a compelling state interest. <i>Washington</i> v. <i>Glucksberg,</i> <span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/#721" aria-description="Citation for case: Washington v. Glucksberg">521 U. S. 702, 721</a></span> (1997). Only fundamental rights and liberties which are "`deeply rooted in this Nation's history and tradition'" and "`implicit in the concept of ordered liberty'" qualify for such protection. <i><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">Ibid.</a></span></i> Many times, however, we have expressed our reluctance to expand the doctrine of substantive due process, see <span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#842" aria-description="Citation for case: County of Sacramento v. Lewis"><i>Lewis, supra,</i> at 842</a></span>; <span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/#720" aria-description="Citation for case: Washington v. Glucksberg"><i>Glucksberg, supra,</i> at 720</a></span>; <i>Albright</i> v. <i>Oliver,</i> <span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/#271" aria-description="Citation for case: Albright v. Oliver">510 U. S. 266, 271</a></span> (1994); <i>Reno</i> v. <i>Flores,</i> <span class="citation" data-id="9432751"><a href="/opinion/112833/reno-v-flores/#302" aria-description="Citation for case: Reno v. Flores">507 U. S. 292, 302</a></span> (1993); in large part "because guideposts for responsible decisionmaking in this unchartered area are scarce and open-ended," <i>Collins</i> v. <i>Harker Heights,</i> <span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/#125" aria-description="Citation for case: Collins v. City of Harker Heights">503 U. S. 115, 125</a></span> (1992). See also <i>Regents of Univ. of Mich.</i> v. <i>Ewing,</i> <span class="citation" data-id="9430245"><a href="/opinion/111549/regents-of-the-university-of-michigan-v-ewing/#225" aria-description="Citation for case: Regents of the University of Michigan v. Ewing">474 U. S. 214, 225-226</a></span> (1985).</p>
    </div>
    <div class="num" id="p35">
      <span class="num">35</span>
      <p class="indent"><i><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">Glucksberg</a></span></i> requires a "`careful description'" of the asserted fundamental liberty interest for the purposes of substantive due process analysis; vague generalities, such as "the right not to be talked to," will not suffice. <span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/#721" aria-description="Citation for case: Washington v. Glucksberg">521 U. S., at 721</a></span>. We therefore must take into account the fact that Martinez was hospitalized and in severe pain during the interview, but also that Martinez was a critical nonpolice witness to an altercation resulting in a shooting by a police officer, and that the situation was urgent given the perceived risk that Martinez might die and crucial evidence might be lost. In these circumstances, we can find no basis in our prior jurisprudence, see, <i>e. g., Miranda,</i> 384 U. S., at 477-478 ("It is an act of responsible citizenship for individuals to give whatever information they may have to aid in law enforcement"), or in our Nation's history and traditions to suppose that freedom from unwanted police questioning is a right so fundamental that it cannot be abridged absent a "compelling state interest." <span class="citation" data-id="9432751"><a href="/opinion/112833/reno-v-flores/#302" aria-description="Citation for case: Reno v. Flores"><i>Flores, supra,</i> at 302</a></span>. We have never required such a justification for a police interrogation, and we decline to do so here. The lack of any "guideposts for responsible decisionmaking" in this area, and our oft-stated reluctance to expand the doctrine of substantive due process, further counsel against recognizing a new "fundamental liberty interest" in this case.</p>
    </div>
    <div class="num" id="p36">
      <span class="num">36</span>
      <p class="indent">We conclude that Martinez has failed to allege a violation of the Fourteenth Amendment, and it is therefore unnecessary to inquire whether the right asserted by Martinez was clearly established.</p>
    </div>
    <p>III</p>
    <div class="num" id="p37">
      <span class="num">37</span>
      <p class="indent">Because Chavez did not violate Martinez's Fifth and Fourteenth Amendment rights, he was entitled to qualified immunity. The judgment of the Court of Appeals for the Ninth Circuit is therefore reversed, and the case is remanded for further proceedings.</p>
    </div>
    <div class="num" id="p38">
      <span class="num">38</span>
      <p class="indent">
        <i>It is so ordered.</i>
      </p>
    </div>
    <div class="footnotes">
      <div class="footnote">
        <p>Notes:</p>
      </div>
      <div class="footnote" id="fn-s-3">
        <a class="footnote" href="#fn-s-3_ref">*</a>
        <p> Briefs of<i>amici curiae</i> urging reversal were filed for the State of California <i>ex rel.</i> Bill Lockyer by <i>Mr. Lockyer,</i> Attorney General, <i>pro se, Robert R. Anderson,</i> Chief Assistant Attorney General, <i>Jo Graves,</i> Senior Assistant Attorney General, <i>Stan Cross,</i> Supervising Deputy Attorney General, and <i>Lee E. Seale</i> and <i>Patrick J. Whalen,</i> Deputy Attorneys General; for the City of Escondido by <i>Jeffrey R. Epp</i> and <i>Richard J. Schneider;</i> for 50 California Cities et al. by <i>Girard Fisher;</i> for the Criminal Justice Legal Foundation by <i>Kent S. Scheidegger</i> and <i>Charles L. Hobson;</i> and for the National Association of Police Organizations by <i>Devallis Rutledge</i> and <i>William J. Johnson.</i></p>
        <p class="indent">Briefs of <i>amici curiae</i> urging affirmance were filed for the American Civil Liberties Union Foundation et al. by <i>Mark D. Rosenbaum, Steven R. Shapiro, Susan N. Herman, John T. Philipsborn,</i> and <i>Erwin Chemerinsky;</i> for the Association of Trial Lawyers of America by <i>Jeffrey L. Needle;</i> and for the National Police Accountability Project et al. by <i>Susan R. Klein</i> and <i>Michael Avery.</i></p>
      </div>
      <div class="footnote" id="fn-s-4">
        <a class="footnote" href="#fn-s-4_ref">*</a>
        <p> THE CHIEF JUSTICE joins this opinion in its entirety. JUSTICE O'CONNOR joins Parts I and II-A of this opinion. JUSTICE SCALIA joins Parts I and II of this opinion</p>
      </div>
      <div class="footnote" id="fn1">
        <a class="footnote" href="#fn1_ref">1</a>
        <p> The parties disagree over what triggered the altercation. The officers maintain that Martinez ran away from them and that they tackled him while in pursuit; Martinez asserts that he never attempted to flee and Salinas tackled him without warning</p>
      </div>
      <div class="footnote" id="fn2">
        <a class="footnote" href="#fn2_ref">2</a>
        <p> The government may not, however, penalize public employees and government contractors to induce them to waive their<i>immunity</i> from the use of their compelled statements in subsequent criminal proceedings. See <i>Uniformed Sanitation Men Assn., Inc.</i> v. <i>Commissioner of Sanitation of City of New York,</i> <span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">392 U. S. 280</a></span> (1968); <i>Lefkowitz</i> v. <i>Turley,</i> <span class="citation" data-id="108882"><a href="/opinion/108882/lefkowitz-v-turley/" aria-description="Citation for case: Lefkowitz v. Turley">414 U. S. 70</a></span> (1973), and this is true even though immunity is not itself a right secured by the text of the Self-Incrimination Clause, but rather a prophylactic rule we have constructed to protect the Fifth Amendment's right from invasion. See Part II-A-3, <i>infra.</i> Once an immunity waiver is signed, the signatory is unable to assert a Fifth Amendment objection to the subsequent use of his statements in a criminal case, even if his statements were in fact compelled. A waiver of immunity is therefore a prospective waiver of the core self-incrimination right in any subsequent criminal proceeding, and States cannot condition public employment on the waiver of constitutional rights, <i>Lefkowitz, supra,</i> at 85.</p>
      </div>
      <div class="footnote" id="fn3">
        <a class="footnote" href="#fn3_ref">3</a>
        <p> That the privilege is a prophylactic one does not alter our penalty cases jurisprudence, which allows such privilege to be asserted prior to, and outside of, criminal proceedings</p>
      </div>
      <div class="footnote" id="fn4">
        <a class="footnote" href="#fn4_ref">4</a>
        <p> It is JUSTICE KENNEDY'S indifference to the text of the Self-Incrimination Clause, as well as a conspicuous absence of a single citation to the actual text of the Fifth Amendment, that permits him to adopt the Ninth Circuit's interpretation</p>
        <p class="indent"><i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span> (1978), on which JUSTICE KENNEDY and JUSTICE GINSBURG rely in support of their reading of the Fifth Amendment, was a case addressing the <i>admissibility</i> of a coerced confession under the <i>Due Process</i> Clause. <i><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Mincey</a></span></i> did not even mention the Fifth Amendment or the Self-Incrimination Clause, and refutes JUSTICE KENNEDY'S and JUSTICE GINSBURG'S assertions that their interpretation of that Clause would have been known to any reasonable officer at the time Chavez conducted his interrogation.</p>
      </div>
      <div class="footnote" id="fn5">
        <a class="footnote" href="#fn5_ref">5</a>
        <p> We also do not see how, in light of<i>Graham</i> v. <i>Connor,</i> <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U. S. 386</a></span> (1989), JUSTICE KENNEDY can insist that "the Self-Incrimination Clause is applicable at the time and place police use compulsion to extract a statement from a suspect" while at the same time maintaining that the use of "torture or its equivalent in an attempt to induce a statement" violates the Due Process Clause. <i>Post,</i> at 795, 796 (opinion concurring in part and dissenting in part). <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> foreclosed the use of substantive due process analysis in claims involving the use of excessive force in effecting an arrest and held that such claims are governed <i>solely</i> by the Fourth Amendment's prohibitions against "unreasonable" seizures, because the Fourth Amendment provided the explicit source of constitutional protection against such conduct. <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#394" aria-description="Citation for case: Graham v. Connor">490 U. S., at 394-395</a></span>. If, as JUSTICE KENNEDY believes, the Fifth Amendment's Self-Incrimination Clause governs coercive police interrogation even absent use of compelled statements in a criminal case, then <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> suggests that the Due Process Clause would not.</p>
        <p>JUSTICE SOUTER delivered an opinion, Part II of which is the opinion of the Court and Part I of which is an opinion concurring in the judgment.<a class="footnote" href="#fn-s-5" id="fn-s-5_ref">*</a></p>
      </div>
      <div class="footnote" id="fn-s-5">
        <a class="footnote" href="#fn-s-5_ref">*</a>
        <p class="indent"> Respondent Martinez's claim under <span class="citation no-link">42 U. S. C. &#167; 1983</span> for violation of his privilege against compelled self-incrimination should be rejected and his case remanded for further proceedings. I write separately because I believe that our decision requires a degree of discretionary judgment greater than JUSTICE THOMAS acknowledges. As he points out, the text of the Fifth Amendment (applied here under the doctrine of Fourteenth Amendment incorporation) focuses on courtroom use of a criminal defendant's compelled, self-incriminating testimony, and the core of the guarantee against compelled self-incrimination is the exclusion of any such evidence. JUSTICE GINSBURG makes it clear that the present case is very close to<i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span> (1978), and Martinez's testimony would clearly be inadmissible if offered in evidence against him. But Martinez claims more than evidentiary protection in asking this Court to hold that the questioning alone was a completed violation of the Fifth and Fourteenth Amendments subject to redress by an action for damages under &#167; 1983.</p>
        <p class="indent">To recognize such a constitutional cause of action for compensation would, of course, be well outside the core of Fifth Amendment protection, but that alone is not a sufficient reason to reject Martinez's claim. As Justice Harlan explained in his dissent in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), "extension[s]" of the bare guarantee may be warranted, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#510" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 510</a></span>, if clearly shown to be desirable means to protect the basic right against the invasive pressures of contemporary society, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#515" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 515</a></span>. In this light, we can make sense of a variety of Fifth Amendment holdings: barring compulsion to give testimonial evidence in a civil proceeding, see <i>McCarthy</i> v. <i>Arndstein,</i> <span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/#40" aria-description="Citation for case: McCarthy v. Arndstein">266 U. S. 34, 40</a></span> (1924); requiring a grant of immunity in advance of any testimonial proffer, see <i>Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#446" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 446-447</a></span> (1972); precluding threats or impositions of penalties that would undermine the right to immunity, see, <i>e. g., Uniformed Sanitation Men Assn., Inc.</i> v. <i>Commissioner of Sanitation of City of New York,</i> <span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/#284" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">392 U. S. 280, 284-285</a></span> (1968); <i>Lefkowitz</i> v. <i>Turley,</i> <span class="citation" data-id="108882"><a href="/opinion/108882/lefkowitz-v-turley/#77" aria-description="Citation for case: Lefkowitz v. Turley">414 U. S. 70, 77-79</a></span> (1973); <i>Lefkowitz</i> v. <i>Cunningham,</i> <span class="citation" data-id="9426845"><a href="/opinion/109683/lefkowitz-v-cunningham/#804" aria-description="Citation for case: Lefkowitz v. Cunningham">431 U. S. 801, 804-806</a></span> (1977); <i>McKune</i> v. <i>Lile,</i> <span class="citation" data-id="9434264"><a href="/opinion/121146/mckune-v-lile/#35" aria-description="Citation for case: McKune v. Lile">536 U. S. 24, 35</a></span> (2002) (plurality opinion); and conditioning admissibility on warnings and waivers to promote intelligent choices and to simplify subsequent inquiry into voluntariness, see <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda, supra.</a></span></i> All of this law is outside the Fifth Amendment's core, with each case expressing a judgment that the core guarantee, or the judicial capacity to protect it, would be placed at some risk in the absence of such complementary protection.</p>
      </div>
      <div class="footnote">
        <a class="footnote">I</a>
        <p class="indent"> do not, however, believe that Martinez can make the "powerful showing," subject to a realistic assessment of costs and risks, necessary to expand protection of the privilege against compelled self-incrimination to the point of the civil liability he asks us to recognize here. See<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#515" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 515, 517</a></span> (Harlan, J., dissenting). The most obvious drawback inherent in Martinez's purely Fifth Amendment claim to damages is its risk of global application in every instance of interrogation producing a statement inadmissible under Fifth and Fourteenth Amendment principles, or violating one of the complementary rules we have accepted in aid of the privilege against evidentiary use. If obtaining Martinez's statement is to be treated as a stand-alone violation of the privilege subject to compensation, why should the same not be true whenever the police obtain any involuntary self-incriminating statement, or whenever the government so much as threatens a penalty in derogation of the right to immunity, or whenever the police fail to honor <i>Miranda?</i><a class="footnote" href="#fn-s-6" id="fn-s-6_ref">*</a> Martinez offers no limiting principle or reason to foresee a stopping place short of liability in all such cases.</p>
        <p class="indent">Recognizing an action for damages in every such instance not only would revolutionize Fifth and Fourteenth Amendment law, but would beg the question that must inform every extension or recognition of a complementary rule in service of the core privilege: why is this new rule necessary in aid of the basic guarantee? Martinez has offered no reason to believe that the guarantee has been ineffective in all or many of those circumstances in which its vindication has depended on excluding testimonial admissions or barring penalties. And I have no reason to believe the law has been systemically defective in this respect.</p>
        <p class="indent">But if there is no failure of efficacy infecting the existing body of Fifth Amendment law, any argument for a damages remedy in this case must depend not on its Fifth Amendment feature but upon the particular charge of outrageous conduct by the police, extending from their initial encounter with Martinez through the questioning by Chavez. That claim, however, if it is to be recognized as a constitutional one that may be raised in an action under &#167; 1983, must sound in substantive due process. See generally <i>County of Sacramento</i> v. <i>Lewis,</i> <span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#849" aria-description="Citation for case: County of Sacramento v. Lewis">523 U. S. 833, 849</a></span> (1998) ("[C]onduct intended to injure in some way unjustifiable by any government interest is the sort of official action most likely to rise to the conscience-shocking level"). Here, it is enough to say that JUSTICE STEVENS shows that Martinez has a serious argument in support of such a position.</p>
        <p>II</p>
        <p class="indent">Whether Martinez may pursue a claim of liability for a substantive due process violation is thus an issue that should be addressed on remand, along with the scope and merits of any such action that may be found open to him.</p>
        <p>Notes:</p>
      </div>
      <div class="footnote" id="fn-s-6">
        <a class="footnote" href="#fn-s-6_ref">*</a>
        <p> JUSTICE BREYER joins this opinion in its entirety. JUSTICE STEVENS, JUSTICE KENNEDY, and JUSTICE GINSBURG join Part II of this opinion</p>
      </div>
      <div class="footnote">
        <a class="footnote">*</a>
        <p> The question whether the absence of<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> warnings may be a basis for a &#167; 1983 action under any circumstance is not before the Court.</p>
        <p class="indent">JUSTICE SCALIA, concurring in part in the judgment.</p>
      </div>
      <div class="footnote">
        <a class="footnote">I</a>
        <p class="indent"> agree with the Court's rejection of Martinez's Fifth Amendment claim, that is, his claim that Chavez violated his right not to be compelled in any criminal case to be a witness against himself<a class="footnote" href="#fn1-1" id="fn1-1_ref">1</a> See <i>ante,</i> at 766-767 (plurality opinion); <i>ante,</i> at 777-779 (SOUTER, J., concurring in judgment). And without a violation of the right protected by the text of the Self-Incrimination Clause (what the plurality and JUSTICE SOUTER call the Fifth Amendment's "core"), Martinez's <span class="citation no-link">42 U. S. C. &#167; 1983</span> action is doomed. Section 1983 does not provide remedies for violations of judicially created prophylactic rules, such as the rule of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), as the Court today holds, see <i>ante,</i> at 772 (plurality opinion); <i>post,</i> at 789-790 (KENNEDY, J., concurring in part and dissenting in part); nor is it concerned with "extensions" of constitutional provisions designed to safeguard actual constitutional rights, cf. <i>ante,</i> at 777-778 (SOUTER, J., concurring in judgment).<a class="footnote" href="#fn2-1" id="fn2-1_ref">2</a> Rather, a plaintiff seeking redress through &#167; 1983 must establish the violation of a federal constitutional or statutory <i>right.</i> See <i>Blessing</i> v. <i>Freestone,</i> <span class="citation" data-id="9842134"><a href="/opinion/118101/blessing-v-freestone/#340" aria-description="Citation for case: Blessing v. Freestone">520 U. S. 329, 340</a></span> (1997); <i>Golden State Transit Corp.</i> v. <i>Los Angeles,</i> <span class="citation" data-id="9431857"><a href="/opinion/112341/golden-state-transit-corp-v-city-of-los-angeles/#106" aria-description="Citation for case: Golden State Transit Corp. v. City of Los Angeles">493 U. S. 103, 106</a></span> (1989).</p>
        <p class="indent">My reasons for rejecting Martinez's Fifth Amendment claim are those set forth in JUSTICE THOMAS'S opinion. I join Parts I and II of that opinion, including Part II-B, which deals with substantive due process. Consideration and rejection of that constitutional claim is absolutely necessary to support reversal of the Ninth Circuit's judgment. For after discussing (and erroneously deciding) Martinez's Fifth Amendment claim, the Ninth Circuit continued as follows:</p>
        <p class="indent">"Likewise, a police officer violates the Fourteenth Amendment when he obtains a confession by coercive conduct, regardless of whether the confession is subsequently used at trial. `The due process violation caused by coercive behavior of law-enforcement officers in pursuit of a confession is <i>complete with the coercive behavior itself.... The actual use or attempted use of that coerced statement in a court of law is not necessary to complete the affront to the Constitution.' Cooper v. Dupnik,</i> <span class="citation" data-id="9000842"><a href="/opinion/9008075/cooper-v-dupnik/#1244" aria-description="Citation for case: Cooper v. Dupnik">963 F. 2d at 1244-45</a></span> (emphasis added). Mr. Martinez has thus stated a <i>prima facie</i> case that Sergeant Chavez violated his Fifth and Fourteenth Amendment rights to be free from police coercion in pursuit of a confession." <span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/#857" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police...">270 F. 3d 852, 857</a></span> (2001).</p>
        <p class="indent">It seems to me impossible to interpret this passage as anything other than an invocation of the doctrine of "substantive due process," which makes unlawful certain government conduct, regardless of whether the procedural guarantees of the Fifth Amendment (or the guarantees of any of the other provisions of the Bill of Rights) have been violated. See <i>Washington</i> v. <i>Glucksberg,</i> <span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">521 U. S. 702</a></span> (1997). To be sure, the term "substantive due process" is not used in the quoted passage, but the passage's technically false dichotomy between Fifth Amendment and Fourteenth Amendment rights uses "Fourteenth Amendment rights" as a stand-in for <i>that aspect</i> of the Fourteenth Amendment which consists of the doctrine of substantive due process. (JUSTICE THOMAS uses similar shorthand in the concluding sentence of his analysis: "Our views on the proper scope of the Fifth Amendment's Self-Incrimination Clause do not mean that police torture or other abuse that results in a confession is constitutionally permissible so long as the statements are not used at trial; it simply means that the Fourteenth Amendment's Due Process Clause, rather than the Fifth Amendment's Self-Incrimination Clause, would govern the inquiry in those cases." <i>Ante,</i> at 773.) What other <i>possible meaning</i> could the passage possess? Surely the Ninth Circuit was not expending a paragraph to make the utterly useless observation that, in addition to violating the Fifth Amendment (because that is incorporated in the Fourteenth) Chavez violated the Fourteenth Amendment (because that incorporates the Fifth). That <i>substantive due process</i> was the point is confirmed by the fact that the sole authority cited to support violation of "the Fourteenth Amendment" is <i>Cooper</i> v. <i>Dupnik,</i> <span class="citation" data-id="9000842"><a href="/opinion/9008075/cooper-v-dupnik/#1244" aria-description="Citation for case: Cooper v. Dupnik">963 F. 2d 1220, 1244-1245</a></span> (1992), a Ninth Circuit case that explicitly recognized a substantive-due-process right to be free from coercive police questioning. See <span class="citation" data-id="9000842"><a href="/opinion/9008075/cooper-v-dupnik/#1244" aria-description="Citation for case: Cooper v. Dupnik"><i>id.,</i> at 1244-1250</a></span>.</p>
        <p class="indent">Since the Ninth Circuit's Fourteenth Amendment holding rested upon substantive due process, we are without authority to disturb that court's judgment solely because of our disagreement with its Fifth Amendment (Self-Incrimination Clause) analysis; the substantive-due-process holding provides an independent ground supporting the decision that Chavez was not entitled to qualified immunity. While JUSTICE SOUTER declines to address that independent ground &#8212; even though the parties extensively briefed the issue, Brief for Petitioner 21-36; Brief for Respondent 29-40; Reply Brief for Petitioner 8-12; Brief for United States as <i>Amicus Curiae</i> 17-23, and even though JUSTICE STEVENS discusses it in dissent, <i>post,</i> at 787-788 (opinion concurring in part and dissenting in part) &#8212; I believe that addressing it, and resolving it against respondent, is essential to the Court's disposition, which reverses the Ninth Circuit's judgment in its entirety.</p>
      </div>
      <div class="footnote">
        <a class="footnote">I</a>
        <p class="indent"> therefore see no basis for a remand to determine "[w]hether Martinez may pursue a claim of liability for a substantive due process violation."<i>Ante,</i> at 779 (majority opinion). That question has already been decided by the Ninth Circuit, and we today reverse its decision. My disagreement with the Court, however, is of little consequence, because Martinez will not be able to prevail on remand by raising anew his substantive-due-process claim. Not only is the claim meritless, as JUSTICE THOMAS demonstrates, <i>ante,</i> at 774-776, but Martinez already had his chance to press a substantive-due-process theory in the Court of Appeals and chose not to, even though Ninth Circuit precedent clearly established substantive due process (including &#8212; contrary to the Government's assertion at oral argument, see Tr. of Oral Arg. 26 &#8212; a "shocks the conscience" criterion) as an available theory of liability under the Fourteenth Amendment. See <span class="citation" data-id="9000842"><a href="/opinion/9008075/cooper-v-dupnik/#1248" aria-description="Citation for case: Cooper v. Dupnik"><i>Cooper, supra,</i> at 1248</a></span> ("There is a second Fourteenth Amendment substantive due process yardstick available to Cooper as a theory of &#167; 1983 liability. The test is whether the Task Force's conduct `shocks the conscience'"). Nowhere did respondent's appellate brief mention the words "substantive due process"; the only rights it asserted were the right against self-incrimination and the right to warnings under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Appellees' Responding Brief in No. 00-56520 (CA9), pp. 28-32, 36-43. If, as JUSTICE SOUTER apparently believes, the opinion below did not address respondent's "substantive due process" claim, that claim has been forfeited.</p>
        <p>Notes:</p>
      </div>
      <div class="footnote" id="fn1-1">
        <a class="footnote" href="#fn1-1_ref">1</a>
        <p> While occasionally referring to this as a "Fifth Amendment claim," a convention commonly followed, JUSTICE THOMAS and JUSTICE SOUTER acknowledge that technically it is a Fourteenth Amendment claim, since it is only<i>through</i> the Fourteenth Amendment that the Fifth is "made applicable to the States," <i>ante,</i> at 766 (opinion of THOMAS, J.), citing <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964).</p>
      </div>
      <div class="footnote" id="fn2-1">
        <a class="footnote" href="#fn2-1_ref">2</a>
        <p> Still less does &#167; 1983 provide a remedy for actions inconsistent with the perceived "purpose" of a constitutional provision. Cf<i>Martinez</i> v. <i>Oxnard,</i> <span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/#857" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police...">270 F. 3d 852, 857</a></span> (CA9 2001) ("[T]he Fifth Amendment's purpose is to prevent coercive interrogation practices that are destructive of human dignity" (internal quotation marks omitted)).</p>
        <p class="indent">JUSTICE STEVENS, concurring in part and dissenting in part.</p>
        <p class="indent">As a matter of fact, the interrogation of respondent was the functional equivalent of an attempt to obtain an involuntary confession from a prisoner by torturous methods. As a matter of law, that type of brutal police conduct constitutes an immediate deprivation of the prisoner's constitutionally protected interest in liberty. Because these propositions are so clear, the District Court and the Court of Appeals correctly held that petitioner is not entitled to qualified immunity.</p>
      </div>
      <div class="footnote">
        <a class="footnote">*</a>
        <p class="indent"> What follows is an English translation of portions of the tape-recorded questioning in Spanish that occurred in the emergency room of the hospital when, as is evident from the text, both parties believed that respondent was about to die:</p>
        <p class="indent">"Chavez: What happened? Olivero, tell me what happened.</p>
        <p class="indent">"O[liverio] M[artinez]: I don't know.</p>
        <p class="indent">"Chavez: I don't know what happened (sic)?</p>
        <p class="indent">"O.M.: Ay! I am dying. Ay! What are you doing to me?</p>
        <p class="indent">"No, ...! (unintelligible scream).</p>
        <p class="indent">"Chavez: What happened, sir?</p>
        <p class="indent">"O.M.: My foot hurts ...</p>
        <p class="indent">"Chavez: Olivera. Sir, what happened?</p>
        <p class="indent">"O.M.: I am choking.</p>
        <p class="indent">"Chavez: Tell me what happened.</p>
        <p class="indent">"O.M.: I don't know.</p>
        <p class="indent">"Chavez: `I don't know.'</p>
        <p class="indent">"O.M.: My leg hurts.</p>
        <p class="indent">"Chavez: I don't know what happened (sic)?</p>
        <p class="indent">"O.M.: It hurts ...</p>
        <p class="indent">"Chavez: Hey, hey look.</p>
        <p class="indent">"O.M.: I am choking.</p>
        <p class="indent">"Chavez: Can you hear? look listen, I am Benjamin Chavez with the police here in Oxnard, look.</p>
        <p class="indent">"O. M.: I am dying, please.</p>
        <p class="indent">"Chavez: OK, yes, tell me what happened. If you are going to die, tell me what happened. Look I need to tell (sic) what happened.</p>
        <p class="indent">"O. M.: I don't know.</p>
        <p class="indent">"Chavez: You don't know, I don't know what happened (sic)? Did you talk to the police?</p>
        <p class="indent">"O. M.: Yes.</p>
        <p class="indent">"Chavez: What happened with the police?</p>
        <p class="indent">"O. M.: We fought.</p>
        <p class="indent">"Chavez: Huh? What happened with the police?</p>
        <p class="indent">"O. M.: The police shot me.</p>
        <p class="indent">"Chavez: Why?</p>
        <p class="indent">"O. M.: Because I was fighting with him.</p>
        <p class="indent">"Chavez: Oh, why were you fighting with the police?</p>
        <p class="indent">"O. M.: I am dying ...</p>
        <p class="indent">"Chavez: OK, yes you are dying, but tell me why you are fighting, were you fighting with the police?</p>
        <p>. . . . .</p>
        <p class="indent">"O. M.: Doctor, please I want air, I am dying.</p>
        <p class="indent">"Chavez: OK, OK. I want to know if you pointed the gun [to yourself] at the police.</p>
        <p class="indent">"O. M.: Yes.</p>
        <p class="indent">"Chavez: Yes, and you pointed it [to yourself]? (sic) at the police pointed the gun? (sic) Huh?</p>
        <p class="indent">"O. M.: I am dying, please . . .</p>
        <p>. . . . .</p>
        <p class="indent">"Chavez: OK, listen, listen I want to know what happened, ok??</p>
        <p class="indent">"O. M.: I want them to treat me.</p>
        <p class="indent">"Chavez: OK, they are do it (sic), look when you took out the gun from the tape (sic) of the police ...</p>
        <p class="indent">"O. M.: I am dying ...</p>
        <p class="indent">"Chavez: Ok, look, what I want to know if you took out (sic) the gun of the police?</p>
        <p class="indent">"O. M.: I am not telling you anything until they treat me.</p>
        <p class="indent">"Chavez: Look, tell me what happened, I want to know, look well don't you want the police know (sic) what happened with you? "O. M.: Uuuggghhh! my belly hurts ...</p>
        <p>. . . . .</p>
        <p class="indent">"Chavez: Nothing, why did you run (sic) from the police?</p>
        <p class="indent">"O. M.: I don't want to say anything anymore.</p>
        <p class="indent">"Chavez: No?</p>
        <p class="indent">"O. M.: I want them to treat me, it hurts a lot, please.</p>
        <p class="indent">"Chavez: You don't want to tell (sic) what happened with you over there?</p>
        <p class="indent">"O. M.: I don't want to die, I don't want to die.</p>
        <p class="indent">"Chavez: Well if you are going to die tell me what happened, and right now you think you are going to die?</p>
        <p class="indent">"O. M.: No.</p>
        <p class="indent">"Chavez: No, do you think you are going to die?</p>
        <p class="indent">"O. M.: Aren't you going to treat me or what?</p>
        <p class="indent">"Chavez: Look, think you are going to die, (sic) that's all I want to know, if you think you are going to die? Right now, do you think you are going to die?</p>
        <p class="indent">"O. M.: My belly hurts, please treat me.</p>
        <p class="indent">"Chavez: Sir?</p>
        <p class="indent">"O. M.: If you treat me I tell you everything, if not, no.</p>
        <p class="indent">"Chavez: Sir, I want to know if you think you are going to die right now?</p>
        <p class="indent">"O. M.: I think so.</p>
        <p class="indent">"Chavez: You think (sic) so? Ok. Look, the doctors are going to help you with all they can do, Ok?. That they can do.</p>
        <p class="indent">"O. M.: Get moving, I am dying, can't you see me? come on.</p>
        <p class="indent">"Chavez: Ah, huh, right now they are giving you medication." App. 8-22.</p>
        <p class="indent">The sound recording of this interrogation, which has been lodged with the Court, vividly demonstrates that respondent was suffering severe pain and mental anguish throughout petitioner's persistent questioning.</p>
        <p class="center">II</p>
        <p class="indent">The Due Process Clause of the Fourteenth Amendment protects individuals against state action that either "`shocks the conscience,' <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#172" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 172</a></span> (1952), or interferes with rights `implicit in the concept of ordered liberty,' <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319, 325-326</a></span> (1937)." <i>United States</i> v. <i>Salerno,</i> <span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/#746" aria-description="Citation for case: United States v. Salerno">481 U. S. 739, 746</a></span> (1987). In <i><span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">Palko</a></span>,</i> the majority of the Court refused to hold that every violation of the Fifth Amendment satisfied the second standard. In a host of other cases, however, the Court has held that unusually coercive police interrogation procedures do violate that standard.<a class="footnote" href="#fn1-2" id="fn1-2_ref">1</a></p>
        <p class="indent">By its terms, the Fifth Amendment itself has no application to the States. It is, however, one source of the protections against state actions that deprive individuals of rights "implicit in the concept of ordered liberty" that the Fourteenth Amendment guarantees. Indeed, as I pointed out in my dissent in <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#371" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 371</a></span> (1985), it is the most specific provision in the Bill of Rights "that protects all citizens from the kind of custodial interrogation that was once employed by the Star Chamber, by `the Germans of the 1930's and early 1940's,' and by some of our own police departments only a few decades ago."<a class="footnote" href="#fn2-2" id="fn2-2_ref">2</a> Whenever it occurs, as it did here, official interrogation of that character is a classic example of a violation of a constitutional right "implicit in the concept of ordered liberty."<a class="footnote" href="#fn3-1" id="fn3-1_ref">3</a></p>
      </div>
      <div class="footnote">
        <a class="footnote">I</a>
        <p class="indent"> respectfully dissent, but for the reasons articulated by JUSTICE KENNEDY,<i>post,</i> at 799, concur in Part II of JUSTICE SOUTER'S opinion.</p>
        <p>Notes:</p>
      </div>
      <div class="footnote" id="fn1-2">
        <a class="footnote" href="#fn1-2_ref">1</a>
        <p> JUSTICE O'CONNOR listed many of these cases, as well as cases from state courts, in<i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#312" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 312-313, n. 3</a></span> (1985): <i>"Darwin</i> v. <i>Connecticut,</i> <span class="citation" data-id="9423713"><a href="/opinion/107694/darwin-v-connecticut/" aria-description="Citation for case: Darwin v. Connecticut">391 U. S. 346</a></span> (1968) (suspect interrogated for 48 hours incommunicado while officers denied access to counsel); <i>Beecher</i> v. <i>Alabama,</i> <span class="citation" data-id="9423505"><a href="/opinion/107526/beecher-v-alabama/#36" aria-description="Citation for case: Beecher v. Alabama">389 U. S. 35, 36</a></span> (1967) (officer fired rifle next to suspect's ear and said `If you don't tell the truth I am going to kill you'); <i>Clewis</i> v. <i>Texas,</i> <span class="citation" data-id="107419"><a href="/opinion/107419/clewis-v-texas/" aria-description="Citation for case: Clewis v. Texas">386 U. S. 707</a></span> (1967) (suspect was arrested without probable cause, interrogated for nine days with little food or sleep, and gave three unwarned `confessions' each of which he immediately retracted); <i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/#439" aria-description="Citation for case: Reck v. Pate">367 U. S. 433, 439-440, n. 3</a></span> (1961) (mentally retarded youth interrogated incommunicado for a week `during which time he was frequently ill, fainted several times, vomited blood on the floor of the police station and was twice taken to the hospital on a stretcher').... <i>Cagle</i> v. <i>State,</i> <span class="citation" data-id="1635158"><a href="/opinion/1635158/cagle-v-state/#4" aria-description="Citation for case: Cagle v. State">45 Ala. App. 3, 4</a></span>, <span class="citation" data-id="1635158"><a href="/opinion/1635158/cagle-v-state/#120" aria-description="Citation for case: Cagle v. State">221 So. 2d 119, 120</a></span> (1969) (police interrogated wounded suspect at police station for one hour before obtaining statement, took him to hospital to have his severe wounds treated, only then giving the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings; suspect prefaced second statement with `I have already give the Chief a statement and I might as well give one to you, too'), cert. denied, <span class="citation multiple-matches"><a href="/c/Ala./284/727/">284 Ala. 727</a></span>, <span class="citation multiple-matches"><a href="/c/So.%202d/221/121/">221 So. 2d 121</a></span> (1969); <i>People</i> v. <i>Saiz,</i> <span class="citation" data-id="9558965"><a href="/opinion/1196896/people-v-saiz/" aria-description="Citation for case: People v. Saiz">620 P. 2d 15</a></span> (Colo. 1980) (two hours' unwarned custodial interrogation of 16-year-old in violation of state law requiring parent's presence, culminating in visit to scene of crime); <i>People</i> v. <i>Bodner,</i> 75 App. Div. 2d 440, 430 N. Y. S. 2d 433 (1980) (confrontation at police station and at scene of crime between police and retarded youth with mental age of eight or nine); <i>State</i> v. <i>Badger,</i> <span class="citation" data-id="2285307"><a href="/opinion/2285307/state-v-badger/#441" aria-description="Citation for case: State v. Badger">141 Vt. 430, 441</a></span>, <span class="citation" data-id="2285307"><a href="/opinion/2285307/state-v-badger/#343" aria-description="Citation for case: State v. Badger">450 A. 2d 336, 343</a></span> (1982) (unwarned `close and intense' station house questioning of 15-year-old, including threats and promises, resulted in confession at 1:20 a.m.; court held `[w]arnings ... were insufficient to cure such blatant abuse or compensate for the coercion in this case')."</p>
      </div>
      <div class="footnote" id="fn2-2">
        <a class="footnote" href="#fn2-2_ref">2</a>
        <p> Adding to the cases cited by JUSTICE O'CONNOR, I appended this footnote: "See,<i>e. g., Leyra</i> v. <i>Denno,</i> <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556</a></span> (1954); <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span> (1945); <i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span> (1944); <i>Ward</i> v. <i>Texas,</i> <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/" aria-description="Citation for case: Ward v. Texas">316 U. S. 547</a></span> (1942); <i>Vernon</i> v. <i>Alabama,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./313/547/">313 U. S. 547</a></span> (1941); <i>White</i> v. <i>Texas,</i> <span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/" aria-description="Citation for case: White v. Texas">310 U. S. 530</a></span> (1940); <i>Canty</i> v. <i>Alabama,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./309/629/">309 U. S. 629</a></span> (1940); <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span> (1940); <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936); <i>Wakat</i> v. <i>Harlib,</i> <span class="citation" data-id="244463"><a href="/opinion/244463/leslie-george-wakat-v-peter-f-harlib-irwin-haviland-harold-t-thompsen/" aria-description="Citation for case: Leslie George Wakat v. Peter F. Harlib, Irwin Haviland,...">253 F. 2d 59</a></span> (CA7 1958); <i>People</i> v. <i>La Frana,</i> <span class="citation" data-id="1992428"><a href="/opinion/1992428/people-v-la-frana/" aria-description="Citation for case: People v. La Frana">4 Ill. 2d 261</a></span>, <span class="citation" data-id="1992428"><a href="/opinion/1992428/people-v-la-frana/" aria-description="Citation for case: People v. La Frana">122 N. E. 2d 583</a></span> (1954); cf. <i>People</i> v. <i>Portelli,</i> 15 N. Y. 2d 235, <span class="citation" data-id="5521593"><a href="/opinion/5674064/people-v-portelli/" aria-description="Citation for case: People v. Portelli">205 N. E. 2d 857</a></span> (1965) (potential witness tortured by police). Such custodial interrogation is, of course, closer to that employed by the Soviet Union than that which our constitutional scheme tolerates. See <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#15" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1, 15-16</a></span> (1970) (opinion of Douglas, J.) (`In [Russia] detention <i>incommunicado</i> is the common practice, and the period of permissible detention now extends for nine months. Where there is custodial interrogation, it is clear that the critical stage of the trial takes place long before the courtroom formalities commence. That is apparent to one who attends criminal trials in Russia. Those that I viewed never put in issue the question of guilt; guilt was an issue resolved in the inner precincts of a prison under questioning by the police')." <i>Id.,</i> at 371-372, n. 19 (dissenting opinion).</p>
      </div>
      <div class="footnote" id="fn3-1">
        <a class="footnote" href="#fn3-1_ref">3</a>
        <p> A person's constitutional right to remain silent is an interest in liberty that is protected against federal impairment by the Fifth Amendment and from state impairment by the Due Process Clause of the Fourteenth Amendment. JUSTICE THOMAS' opinion is fundamentally flawed in two respects. It incorrectly assumes that the claim it rejects is not a due process claim,<i>ante,</i> at 772-773, and it incorrectly assumes that coercive interrogation is not unconstitutional when it occurs because it merely violates a judge-made "prophylactic" rule. But the violation in this case is far more serious than a mere failure to advise respondent of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights; moreover, the Court disavowed the "prophylactic" characterization of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in <i>Dickerson</i> v. <i>United States,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#437" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428, 437-439</a></span> (2000).</p>
        <p class="indent">JUSTICE KENNEDY, with whom JUSTICE STEVENS joins, and with whom JUSTICE GINSBURG joins as to Parts II and III, concurring in part and dissenting in part.</p>
      </div>
      <div class="footnote">
        <a class="footnote">A</a>
        <p class="indent"> single police interrogation now presents us with two issues: first, whether failure to give a required warning under<i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), was itself a completed constitutional violation actionable under <span class="citation no-link">42 U. S. C. &#167; 1983</span>; and second, whether an actionable violation arose at once under the Self-Incrimination Clause (applicable to the States through the Fourteenth Amendment) when the police, after failing to warn, used severe compulsion or extraordinary pressure in an attempt to elicit a statement or confession.</p>
      </div>
      <div class="footnote">
        <a class="footnote">I</a>
        <p class="indent"> agree with JUSTICE THOMAS that failure to give a<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> warning does not, without more, establish a completed violation when the unwarned interrogation ensues. As to the second aspect of the case, which does not involve the simple failure to give a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning, it is my respectful submission that JUSTICE SOUTER and JUSTICE THOMAS are incorrect. They conclude that a violation of the Self-Incrimination Clause does not arise until a privileged statement is introduced at some later criminal proceeding.</p>
      </div>
      <div class="footnote">
        <a class="footnote">A</a>
        <p class="indent"> constitutional right is traduced the moment torture or its close equivalents are brought to bear. Constitutional protection for a tortured suspect is not held in abeyance until some later criminal proceeding takes place. These are the premises of this separate opinion</p>
      </div>
      <div class="footnote">
        <a class="footnote">*</a>
        <p class="indent"> The<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> warning, as is now well settled, is a constitutional requirement adopted to reduce the risk of a coerced confession and to implement the Self-Incrimination Clause. <i>Dickerson</i> v. <i>United States,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#444" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428, 444</a></span> (2000); <i>Miranda</i> v. <i>Arizona, supra,</i> at 467. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> mandates a rule of exclusion. It must be so characterized, for it has significant exceptions that can only be assessed and determined in the course of trial. Unwarned custodial interrogation does not in every instance violate <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> See, <i>e. g., New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U. S. 649</a></span> (1984) (statement admissible if questioning was immediately necessary for public safety). Furthermore, statements secured in violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> are admissible in some instances. See, <i>e. g., Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971) (statement admissible for purposes of impeachment). The identification of a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation and its consequences, then, ought to be determined at trial. The exclusion of unwarned statements, when not within an exception, is a complete and sufficient remedy.</p>
        <p>II</p>
        <p class="indent">JUSTICE SOUTER and JUSTICE THOMAS are wrong, in my view, to maintain that in all instances a violation of the Self-Incrimination Clause simply does not occur unless and until a statement is introduced at trial, no matter how severe the pain or how direct and commanding the official compulsion used to extract it.</p>
        <p class="indent">It must be remembered that the Self-Incrimination Clause of the Fifth Amendment is applicable to the States in its full text through the Due Process Clause of the Fourteenth Amendment. <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#6" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 6</a></span> (1964); <i>Griffin</i> v. <i>California,</i> <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/#615" aria-description="Citation for case: Griffin v. California">380 U. S. 609, 615</a></span> (1965). The question is the proper interpretation of the Self-Incrimination Clause in the context of the present dispute.</p>
        <p class="indent">Our cases and our legal tradition establish that the Self-Incrimination Clause is a substantive constraint on the conduct of the government, not merely an evidentiary rule governing the work of the courts. The Clause must provide more than mere assurance that a compelled statement will not be introduced against its declarant in a criminal trial. Otherwise there will be too little protection against the compulsion the Clause prohibits. The Clause protects an individual from being forced to give answers demanded by an official in any context when the answers might give rise to criminal liability in the future. "It can be asserted in any proceeding, civil or criminal, administrative or judicial, investigatory or adjudicatory; and it protects against any disclosures that the witness reasonably believes could be used in a criminal prosecution or could lead to other evidence that might be so used." <i>Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#444" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 444-445</a></span> (1972) (footnotes omitted). The decision in <i><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span></i> described the Self-Incrimination Clause as an exemption from the testimonial duty. <i><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Ibid.</a></span></i> As the duty is immediate, so must be the privilege. Furthermore, the exercise of the privilege depends on what the witness reasonably believes will be the future use of a statement. <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#445" aria-description="Citation for case: Kastigar v. United States"><i>Id.,</i> at 445</a></span>. Again, this indicates the existence of a present right.</p>
        <p class="indent">The Clause provides both assurance that a person will not be compelled to testify against himself in a criminal proceeding and a continuing right against government conduct intended to bring about self-incrimination. <i>Lefkowitz</i> v. <i>Turley,</i> <span class="citation" data-id="108882"><a href="/opinion/108882/lefkowitz-v-turley/#77" aria-description="Citation for case: Lefkowitz v. Turley">414 U. S. 70, 77</a></span> (1973) ("The Amendment not only protects the individual against being involuntarily called as a witness against himself in a criminal prosecution but also privileges him not to answer official questions put to him in any other proceeding, civil or criminal, formal or informal, where the answers might incriminate him in future criminal proceedings"); accord, <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#542" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 542-543</a></span> (1897); <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#562" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 562</a></span> (1892). The principle extends to forbid policies which exert official compulsion that might induce a person into forfeiting his rights under the Clause. <i>Lefkowitz</i> v. <i>Cunningham,</i> <span class="citation" data-id="9426845"><a href="/opinion/109683/lefkowitz-v-cunningham/#806" aria-description="Citation for case: Lefkowitz v. Cunningham">431 U. S. 801, 806</a></span> (1977) ("These cases settle that government cannot penalize assertion of the constitutional privilege against compelled self-incrimination by imposing sanctions to compel testimony which has not been immunized"); accord, <i>Uniformed Sanitation Men Assn., Inc.</i> v. <i>Commissioner of Sanitation of City of New York,</i> <span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">392 U. S. 280</a></span> (1968); <i>Gardner</i> v. <i>Broderick,</i> <span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/#279" aria-description="Citation for case: Gardner v. Broderick">392 U. S. 273, 279</a></span> (1968). JUSTICE SOUTER and JUSTICE THOMAS acknowledge a future privilege. <i>Ante,</i> at 777-778; <i>ante,</i> at 769. That does not end the matter. A future privilege does not negate a present right.</p>
        <p class="indent">Their position finds some support in a single statement in <i>United States</i> v. <i>Verdugo-Urquidez,</i> <span class="citation" data-id="9431925"><a href="/opinion/112382/united-states-v-verdugo-urquidez/#264" aria-description="Citation for case: United States v. Verdugo-Urquidez">494 U. S. 259, 264</a></span> (1990) ("Although conduct by law enforcement officials prior to trial may ultimately impair that right [against compelled self-incrimination], a constitutional violation occurs only at trial"). That case concerned the application of the Fourth Amendment, and the extent of the right secured under the Self-Incrimination Clause was not then before the Court. <i><span class="citation" data-id="9431925"><a href="/opinion/112382/united-states-v-verdugo-urquidez/" aria-description="Citation for case: United States v. Verdugo-Urquidez">Ibid.</a></span></i> Furthermore, <i><span class="citation" data-id="9431925"><a href="/opinion/112382/united-states-v-verdugo-urquidez/" aria-description="Citation for case: United States v. Verdugo-Urquidez">Verdugo-Urquidez</a></span></i> involved a prosecution in the United States arising from a criminal investigation in another country, <span class="citation" data-id="9431925"><a href="/opinion/112382/united-states-v-verdugo-urquidez/#274" aria-description="Citation for case: United States v. Verdugo-Urquidez"><i>id.,</i> at 274-275</a></span>, so there was a special reason for the Court to be concerned about the application of the Clause in that context, <span class="citation" data-id="9431925"><a href="/opinion/112382/united-states-v-verdugo-urquidez/#269" aria-description="Citation for case: United States v. Verdugo-Urquidez"><i>id.,</i> at 269</a></span> (noting the Court had "rejected the claim that aliens are entitled to Fifth Amendment rights outside the sovereign territory of the United States" (citing <i>Johnson</i> v. <i>Eisentrager,</i> <span class="citation" data-id="104813"><a href="/opinion/104813/johnson-v-eisentrager/" aria-description="Citation for case: Johnson v. Eisentrager">339 U. S. 763</a></span> (1950))). In any event, the decision cannot be read to support the proposition that the application of the Clause is limited in the way JUSTICE SOUTER and JUSTICE THOMAS describe today.</p>
      </div>
      <div class="footnote">
        <a class="footnote">A</a>
        <p class="indent"> recent case illustrates that a violation of the Self-Incrimination Clause may have immediate consequences. Just last Term, nine Justices all proceeded from the premise that a present, completed violation of the Self-Incrimination Clause could occur if an incarcerated prisoner were required to admit to past crimes on pain of forfeiting certain privileges or being assigned harsher conditions of confinement<i>McKune</i> v. <i>Lile,</i> <span class="citation" data-id="9434264"><a href="/opinion/121146/mckune-v-lile/" aria-description="Citation for case: McKune v. Lile">536 U. S. 24</a></span> (2002); <span class="citation" data-id="9434264"><a href="/opinion/121146/mckune-v-lile/#48" aria-description="Citation for case: McKune v. Lile"><i>id.,</i> at 48</a></span> (O'CONNOR, J., concurring in judgment); <span class="citation" data-id="9434264"><a href="/opinion/121146/mckune-v-lile/#54" aria-description="Citation for case: McKune v. Lile"><i>id.,</i> at 54</a></span> (STEVENS, J., dissenting). Although there was disagreement over whether a violation occurred in the circumstances of that case, there was no disagreement that a present violation could have taken place. No Member of the Court suggested that the absence of a pending criminal proceeding made the Self-Incrimination Clause inquiry irrelevant.</p>
        <p class="indent">This is not to say all questions as to the meaning and extent of the Clause are simple of resolution, or that all of the cited cases are easy to reconcile. Many questions about the application of the Self-Incrimination Clause are close and difficult. There are instances, moreover, when incriminating statements can be required from a reluctant witness, see, <span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/#276" aria-description="Citation for case: Gardner v. Broderick"><i>e. g., Gardner, supra,</i> at 276</a></span>, and others where information may be required even absent a promise of immunity, see, <i>e. g., Shapiro</i> v. <i>United States,</i> <span class="citation" data-id="9420211"><a href="/opinion/104585/shapiro-v-united-states/#19" aria-description="Citation for case: Shapiro v. United States">335 U. S. 1, 19</a></span> (1948). JUSTICE SOUTER and JUSTICE THOMAS are correct to note that testimony may be ordered, on pain of contempt, if appropriate immunity is granted. It does not follow that the Clause establishes no present right. The immunity rule simply shows that the right is not absolute.</p>
        <p class="indent">The conclusion that the Self-Incrimination Clause is not violated until the government seeks to use a statement in some later criminal proceeding strips the Clause of an essential part of its force and meaning. This is no small matter. It should come as an unwelcome surprise to judges, attorneys, and the citizenry as a whole that if a legislative committee or a judge in a civil case demands incriminating testimony without offering immunity, and even imposes sanctions for failure to comply, that the witness and counsel cannot insist the right against compelled self-incrimination is applicable then and there. JUSTICE SOUTER and JUSTICE THOMAS, I submit, should be more respectful of the understanding that has prevailed for generations now. To tell our whole legal system that when conducting a criminal investigation police officials can use severe compulsion or even torture with no present violation of the right against compelled self-incrimination can only diminish a celebrated provision in the Bill of Rights. A Constitution survives over time because the people share a common, historic commitment to certain simple but fundamental principles which preserve their freedom. Today's decision undermines one of those respected precepts.</p>
        <p class="indent">Dean Griswold explained the place the Self-Incrimination Clause has secured in our legal heritage:</p>
        <p class="indent">"The Fifth Amendment has been very nearly a lone sure rock in a time of storm. It has been one thing which has held quite firm, although something like a juggernaut has pushed upon it. It has, thus, through all its vicissitudes, been a symbol of the ultimate moral sense of the community, upholding the best in us, when otherwise there was a good deal of wavering under the pressures of the times." E. Griswold, The Fifth Amendment Today 73 (1955).</p>
        <p class="indent">It damages the law, and the vocabulary with which we impart our legal tradition from one generation to the next, to downgrade our understanding of what the Fifth Amendment requires.</p>
        <p class="indent">There is some authority, it must be acknowledged, for the proposition that the act of torturing to obtain a confession is not comprehended within the Self-Incrimination Clause itself. In <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936), the Court held that convictions based upon tortured confessions could not stand, but it identified the Due Process Clause, and not the Self-Incrimination Clause, as the source for its ruling. <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#285" aria-description="Citation for case: Brown v. Mississippi"><i>Id.,</i> at 285</a></span>. The Court interpreted the Self-Incrimination Clause as limited to "the processes of justice by which the accused may be called as a witness and required to testify. Compulsion by torture to extort a confession is a different matter." <i><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Ibid.</a></span></i> The decision in <i>Brown</i> antedated the incorporation of the Clause and the ensuing understanding of its fundamental role in our legal system.</p>
        <p class="indent">The views expressed by JUSTICE SOUTER and JUSTICE THOMAS also have some academic support. Professor McNaughton, in his revision of Professor Wigmore's treatise on the law of evidence, recites various rationales for the Self-Incrimination Clause, declaring all of them insufficient. 8 J. Wigmore, Evidence &#167; 2251 (J. McNaughton rev. ed. 1961). The 11th justification he discusses is the prevention of torture, <i>id.,</i> at 315, a practice Professor McNaughton simply assures us will not be revived, <i>ibid.</i></p>
        <p class="indent">This is not convincing. The Constitution is based upon the theory that when past abuses are forbidden the resulting right has present meaning. A police officer's interrogation is different in a formal sense from interrogation ordered by an official inquest, but the close relation between the two ought not to be so quickly discounted. Even if some think the abuses of the Star Chamber cannot revive, the specter of Sheriff Screws, see <i>Screws</i> v. <i>United States,</i> <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">325 U. S. 91</a></span> (1945), or of the deputies who beat the confessions out of the defendants in <i>Brown</i> v. <i><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Mississippi</a></span>,</i> is not so easily banished. See <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#312" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 312, n. 3</a></span> (1985); <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#371" aria-description="Citation for case: Oregon v. Elstad"><i>id.,</i> at 371-372, n. 19

[...TRUNCATED 18337 of 138337 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/Chiaverini v. City of Napoleon.md  (`case`, 5 assertions)

### content_page

```
---
title: Chiaverini v. City of Napoleon
type: case
citation: "602 U.S. 556 (2024)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2024
date_decided: ""
docket: 23-50
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
  opinion_url: "https://www.courtlistener.com/opinion/10600074/chiaverini-v-city-of-napoleon/"
  cluster_id: 10600074
  opinion_id: 11066663
  identity_checked: true
lake:
  record_id: Chiaverini v. City of Napoleon
  status: under_review
  projected_at: 2026-07-09
homes:
  - page: "[[Malicious Prosecution under the Fourth Amendment]]"
    role: Key
related:
  - "[[Thompson v. Clark]]"
  - "[[Heck v. Humphrey]]"
  - "[[Malicious Prosecution under the Fourth Amendment]]"
tags:
  - case
  - fourth-amendment
  - malicious-prosecution
  - section-1983
  - probable-cause
holding: "The presence of probable cause for one charge does not categorically defeat a Fourth Amendment malicious-prosecution claim under §1983 challenging a separate, baseless charge; courts evaluate each charge on its own."
---

# Chiaverini v. City of Napoleon

*602 U.S. 556 (2024)* (No. 23-50) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10600074 → opinion 11066663; quotes string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Jascha Chiaverini, who ran a jewelry store in Napoleon, Ohio, was charged by local police with three offenses arising from his purchase of a ring: two misdemeanors (receiving stolen property and dealing in precious metals without a license) and a felony count of money laundering. The officers obtained an arrest warrant and Chiaverini was detained for three days; the charges were later dismissed after the county prosecutors failed to present the case to a grand jury in time. He sued the officers under 42 U.S.C. § 1983, alleging a Fourth Amendment malicious-prosecution claim and contending that the felony money-laundering charge lacked probable cause. The District Court granted the officers summary judgment, and the Sixth Circuit affirmed on the ground that probable cause supporting the two misdemeanor charges defeated the malicious-prosecution claim as to any charge.

## Issue
Whether the presence of probable cause for one charge in a criminal proceeding categorically defeats a Fourth Amendment malicious-prosecution claim under § 1983 that is based on a separate charge lacking probable cause.

## Rule
A Fourth Amendment malicious-prosecution claim under § 1983 — the claim recognized in *[[Thompson v. Clark]]* — requires a plaintiff to show that an official brought a charge without probable cause that caused an unreasonable seizure of his person. The existence of probable cause for one charge does not categorically defeat that claim as to another, baseless charge. Drawing on both Fourth Amendment law (an invalid charge that starts or prolongs a detention is an unreasonable seizure even when a valid charge is also brought) and the common-law malicious-prosecution tort as it stood in 1871 (which assessed probable cause charge by charge), the Court held that "[c]onsistent with both the Fourth Amendment and traditional common-law practice, courts should evaluate suits like Chiaverini's charge by charge." — 602 U.S. at 562. ^pin-562

## Application
The Sixth Circuit's categorical rule — that a single valid charge insulates officers from a malicious-prosecution claim based on any other charge, however baseless — drew support from neither half of the claim's name, and even the defendant officers and the United States agreed it was wrong. The Court did not, however, resolve the separate **causation** element: whether the assertedly invalid felony charge actually caused Chiaverini's three-day detention given the concededly valid misdemeanor charges. Because the parties advanced competing causation tests (a taint theory, a but-for test, and a stricter "could-have-authorized" test) that the court below had not addressed, the Court left that question for the Sixth Circuit [[Reading and Citing Cases#on-remand|on remand]].

## Conclusion
The judgment of the Court of Appeals was **[[Reading and Citing Cases#vacated|vacated]]** and the case **[[Reading and Citing Cases#on-remand|remanded]]** for further proceedings on the causation question. Kagan, J., delivered the opinion of the Court; Thomas, J., joined by Alito, J., dissented, adhering to the view that a malicious-prosecution claim cannot be based on the Fourth Amendment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. The decision [[Reading and Citing Cases#vacated|vacated]] the Sixth Circuit's judgment and [[Reading and Citing Cases#on-remand|remanded]]; the Fourth Amendment causation standard for multi-charge malicious-prosecution claims remains open in the lower courts.

## Appears on
- [[Malicious Prosecution under the Fourth Amendment]] — *Key*

## Sources
- [*Chiaverini v. City of Napoleon*, 602 U.S. 556 (2024)](https://www.courtlistener.com/opinion/10600074/chiaverini-v-city-of-napoleon/) — pinpoint: 562 (charge-by-charge holding, Opinion of the Court); quote string-matched to the CL opinion text 2026-07-07.
- [*Thompson v. Clark*, 596 U.S. 36 (2022)](https://www.courtlistener.com/opinion/6457347/thompson-v-clark/) — the Fourth Amendment malicious-prosecution claim on which *Chiaverini* builds.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ce0dbf4cd91d05af", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "602 U.S. 556 (2024)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Chiaverini v. City of Napoleon", "year": "2024"}}
{"assertion_id": "154ef3172f800956", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The presence of probable cause for one charge does not categorically defeat a Fourth Amendment malicious-prosecution claim under §1983 challenging a separate, baseless charge; courts evaluate each charge on its own.", "title": "Chiaverini v. City of Napoleon"}}
{"assertion_id": "c6df5a8f089e9c56", "dimension": "support", "kind": "home_role", "locator": {"home": "Malicious Prosecution under the Fourth Amendment"}, "payload": {"home": "Malicious Prosecution under the Fourth Amendment", "role": "Key", "title": "Chiaverini v. City of Napoleon"}}
{"assertion_id": "ba3d36fb325ef084", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Chiaverini v. City of Napoleon"}}
{"assertion_id": "e4192dd7cb27321b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Chiaverini v. City of Napoleon", "varies_by_point": "false"}}
```

### lake record — Chiaverini v. City of Napoleon

```json
{
  "schema_version": "s2.v1",
  "record_id": "Chiaverini v. City of Napoleon",
  "status": "under_review",
  "identity": {
    "case_name": "Chiaverini v. City of Napoleon",
    "case_name_short": "Chiaverini",
    "case_name_full": "",
    "input_case_name": "Chiaverini v. City of Napoleon",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2024,
    "docket": "23-50",
    "cluster_id": 10600074,
    "lead_opinion_id": 11066663,
    "sibling_ids": [],
    "absolute_url": "/opinion/10600074/chiaverini-v-city-of-napoleon/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "602 U.S. 556",
      "volume": "602",
      "reporter": "U.S.",
      "page": "556",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "602 U.S. 556",
        "volume": "602",
        "reporter": "U.S.",
        "page": "556",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "602 U.S. 556",
    "official_selection": {
      "court_class": "scotus",
      "selected": "602 U.S. 556",
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
    "date_created": "2026-07-06T12:12:08Z",
    "date_modified": "2026-07-09T23:29:56Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:12:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:12:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "chiaverini-v-city-of-napoleon--10600074",
      "to_record_id": "Chiaverini v. City of Napoleon",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Chiaverini v. City of Napoleon

```
                   PRELIMINARY PRINT

             Volume 602 U. S. Part 1
                             Pages 556–571




       OFFICIAL REPORTS
                                    OF


   THE SUPREME COURT
                               June 20, 2024


Page Proof Pending Publication


                   REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D.C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
556                      OCTOBER TERM, 2023

                                  Syllabus


CHIAVERINI et al. v. CITY OF NAPOLEON, OHIO,
                     et al.
certiorari to the united states court of appeals for
                  the sixth circuit
       No. 23–50. Argued April 15, 2024—Decided June 20, 2024
This case involves a dispute between petitioner Jascha Chiaverini and po-
  lice offcers from Napoleon, Ohio. The offcers charged Chiaverini, a
  jewelry store owner, with three crimes: receiving stolen property, a mis-
  demeanor; dealing in precious metals without a license, also a misde-
  meanor; and money laundering, a felony. After obtaining a warrant,
  the police arrested Chiaverini and detained him for three days. But
  county prosecutors later dropped the case. Chiaverini, believing that
  his arrest and detention were unjustifed, then sued the offcers, alleging
  what is known as a Fourth Amendment malicious-prosecution claim
  under 42 U. S. C. § 1983. To prevail on this claim, he had to show that
  the offcers brought criminal charges against him without probable
  cause, leading to an unreasonable seizure of his person. The District
Page Proof Pending Publication
  Court, however, granted summary judgment to the offcers, and the
  Court of Appeals for the Sixth Circuit affrmed. The Court of Appeals
  held that Chiaverini's prosecution was supported by probable cause. In
  holding this, the court did not address whether the offcers had prob-
  able cause to bring the money-laundering charge. In its view, there
  was clearly probable cause to charge Chiaverini with the two misde-
  meanors. And so long as one charge was supported by probable cause,
  it thought, a malicious-prosecution claim based on any other charge
  must fail.
Held: The presence of probable cause for one charge in a criminal pro-
 ceeding does not categorically defeat a Fourth Amendment malicious-
 prosecution claim relating to another, baseless charge. The parties, and
 the United States as amicus curiae, all agree with this conclusion,
 which follows from both the Fourth Amendment and traditional
 common-law practice.
    Under the Fourth Amendment, a pretrial detention counts as an un-
 reasonable seizure, and so is illegal, unless it is based on probable cause.
 See Manuel v. Joliet, 580 U. S. 357, 364–369. Even when a detention
 is justifed at the outset, moreover, it may become unreasonably pro-
 longed if the reason for it lapses. Rodriguez v. United States, 575 U. S.
 348, 354–357. So if an invalid charge causes a detention to start or
 continue, then the Fourth Amendment is violated. Bringing the invalid
 charge alongside a valid one does not categorically preclude this possi-
                      Cite as: 602 U. S. 556 (2024)                   557

                                Syllabus

  bility. As the starkest possible example, consider a person detained on
  a drug offense supported by probable cause and a gun offense that is
  not. If the prosecutor drops the (valid) drug charge, leaving the person
  in jail on the (invalid) gun charge alone, then the baseless charge has
  caused a constitutional violation by unreasonably extending the deten-
  tion. The person should not be categorically barred from bringing a
  Fourth Amendment malicious-prosecution claim just because the base-
  less charge was brought along with a good one.
     The same conclusion follows from the common-law principles govern-
  ing malicious-prosecution suits. This Court has analogized claims like
  Chiaverini's to the common-law tort of malicious prosecution, and has
  explained that the tort can inform courts' understanding of this type of
  claim. Thompson v. Clark, 596 U. S. 36, 43–44. A plaintiff bringing a
  common-law malicious-prosecution suit had to show that an offcial initi-
  ated a charge without probable cause. But he did not have to show
  that every charge brought against him lacked an adequate basis. See,
  e. g., Barron v. Mason, 31 Vt. 189, 198 (it was no “defen[s]e that there
  was probable cause for part of the prosecution”).
     These uncontested points suffce to doom the Sixth Circuit's categori-
  cal rule barring a Fourth Amendment malicious-prosecution claim if any

Page Proof Pending Publication
  charge is valid. Of course, a Fourth Amendment malicious-prosecution
  suit depends not just on an unsupported charge, but on that charge's
  causing a seizure—like the arrest and three-day detention here. The
  parties and amicus curiae offer three different views of how that causa-
  tion element is met when a valid charge is also in the picture. But this
  issue is not properly before the Court, so the Sixth Circuit should ad-
  dress it on remand. Pp. 561–565.
Vacated and remanded.

   Kagan, J., delivered the opinion of the Court, in which Roberts, C. J.,
and Sotomayor, Kavanaugh, Barrett, and Jackson, JJ., joined.
Thomas, J., fled a dissenting opinion, in which Alito, J., joined, post,
p. 565. Gorsuch, J., fled a dissenting opinion, post, p. 569.

  Easha Anand argued the cause for petitioners. With her
on the briefs were Jeffrey L. Fisher, Pamela S. Karlan, Mi-
chael H. Stahl, and George C. Rogers.
  Vivek Suri argued the cause for the United States as ami-
cus curiae urging vacatur and remand. With him on the
brief were Solicitor General Prelogar, Assistant Attorney
General Clarke, Principal Deputy Assistant Attorney Gen-
558             CHIAVERINI v. CITY OF NAPOLEON

                          Opinion of the Court

eral Boynton, Deputy Solicitor General Gannon, Mark B.
Stern, Erin H. Flynn, and Brant S. Levine.
  Megan M. Wold argued the cause for respondents. With
her on the brief were Teresa L. Grigsby and Jennifer A.
McHugh.*

   Justice Kagan delivered the opinion of the Court.
  This case involves what is often called a Fourth Amend-
ment malicious-prosecution claim under 42 U. S. C. § 1983.
To succeed on such a claim, a plaintiff must show that a gov-
ernment offcial charged him without probable cause, leading
to an unreasonable seizure of his person. See Thompson v.
Clark, 596 U. S. 36, 43, and n. 2 (2022). The question pre-
sented here arises when the offcial brings multiple charges,
only one of which lacks probable cause. Do the valid
charges insulate the offcial from a Fourth Amendment
malicious-prosecution claim relating to the invalid charge?
Page         Proof Pending Publication
 *Briefs of amici curiae urging reversal were fled for the Cato Institute
by Steve Art and David B. Owens; for the Constitutional Accountability
Center by Elizabeth B. Wydra, Brianne J. Gorod, and Brian R. Frazelle;
for the Institute for Justice by Marie Miller, Anya Bidwell, and Patrick
Jaicomo; for the National Association of Criminal Defense Lawyers by
Zachary D. Tripp, Joshua M. Wesneski, and Jeffrey T. Green; and for the
National Police Accountability Project by Charles A. Rothfeld and Eugene
R. Fidell.
   Briefs of amici curiae urging affrmance were fled for the State of Iowa
et al. by Brenna Bird, Attorney General of Iowa, Eric Wessan, Solicitor
General, Patrick C. Valencia, Deputy Solicitor General, and Alexa Den
Herder, Assistant Solicitor General, and by the Attorneys General for
their respective States as follows: Steve Marshall of Alabama, Tim Griffn
of Arkansas, Ashley Moody of Florida, Christopher M. Carr of Georgia,
Raúl R. Labrador of Idaho, Todd Rokita of Indiana, Kris Kobach of Kan-
sas, Russell Coleman of Kentucky, Elizabeth B. Murrill of Louisiana,
Austin Knudsen of Montana, Michael T. Hilgers of Nebraska, Dave Yost
of Ohio, Gentner Drummond of Oklahoma, Alan Wilson of South Caro-
lina, Marty J. Jackley of South Dakota, Jonathan Skrmetti of Tennessee,
Ken Paxton of Texas, and Sean D. Reyes of Utah; and for the Local Gov-
ernment Legal Center et al. by Gregory G. Garre.
                   Cite as: 602 U. S. 556 (2024)             559

                      Opinion of the Court

The answer is no: The valid charges do not create a categori-
cal bar. We leave for another day the follow-on question of
how to determine in those circumstances whether the base-
less charge caused the requisite seizure.

                                I
   This dispute began with a set of peculiar interactions be-
tween a jewelry store owner and police offcers in Napoleon,
Ohio. See generally App. to Pet. for Cert. 2a–7a. The jew-
eler, Jascha Chiaverini, bought a ring for $45 from a (petty)
jewel thief. The ring's rightful owners found out about the
sale, and asked Chiaverini to return their property. Chiav-
erini said no, so the owners contacted the police. Two off-
cers, on a later visit to the store, directed Chiaverini to sur-
render the ring to its owners. But Chiaverini refused their
request too, saying that it contradicted a letter he had just
received from the police department telling him to retain the
Page Proof Pending Publication
ring as evidence. And when repeating his refusal to another
offcer the next day, Chiaverini suggested (for reasons un-
clear) that he was operating his store without a license. The
result of that (shall we say, unproftable) exchange was that
the police turned their attention from the original theft to
Chiaverini's business.
   Soon afterward, the offcers launched a criminal proceed-
ing against Chiaverini in municipal court. They fled three
complaints, each charging him with a separate offense. Two
were misdemeanors: receiving stolen property and dealing
in precious metals without a license. The third was a felony:
money laundering. To support their accompanying applica-
tion for an arrest warrant, the offcers submitted an affdavit
making the case for probable cause on all three charges, but
focusing on the felony. See App. 16–17. For that charge to
succeed, Chiaverini must have known when he bought the
ring that the transaction involved the proceeds of unlawful
activity. See Ohio Rev. Code Ann. § 1315.55(A)(1) (Lexis
2018). In support of that element, the offcers averred that
560          CHIAVERINI v. CITY OF NAPOLEON

                     Opinion of the Court

Chiaverini always suspected the ring was stolen. The judge
issued the requested warrant, and the offcers arrested Chi-
averini. He remained in custody for three days, until his
arraignment. At a later preliminary hearing, the judge
heard testimony about the evidence supporting the offcers'
probable-cause allegations. See App. to Pet. for Cert. 6a–
7a. The offcers maintained that Chiaverini had admitted in
their interview to suspecting the ring was stolen; Chiaverini
denied making any such statement. At the hearing's conclu-
sion, the judge again found probable cause, and set the three
charges for trial.
   The county prosecutors, though, decided that they had
higher priorities. They failed to present the case to a grand
jury in the required time. The court therefore dismissed
the charges.
   But Chiaverini decided not to let matters lie. After all,
he had been arrested and held for three days, he thought
Page Proof Pending Publication
unjustifably. So he sued the offcers under § 1983, alleging
what is known as a Fourth Amendment claim for malicious
prosecution. To prevail on that claim, he had to show
(among other things) that the offcers brought criminal
charges against him without probable cause. See Thomp-
son, 596 U. S., at 43–44. In addressing that issue, he gave
special attention to the felony charge for money laundering.
According to Chiaverini, the offcers lacked probable cause
for that charge for two reasons. First, they had no reason
to think he knew the ring was stolen; indeed, he said, their
claim that he had admitted as much was an out-and-out lie.
And second, they could not show—as, in his view, Ohio law
required—that the ring was worth more than $1,000; its
value was far less, more in line with its $45 purchase price.
So Chiaverini concluded that his suit satisfed the “without
probable cause” element of a Fourth Amendment malicious-
prosecution claim.
   After the District Court granted summary judgment to
the offcers, the Court of Appeals for the Sixth Circuit af-
                   Cite as: 602 U. S. 556 (2024)             561

                      Opinion of the Court

frmed. It did so without addressing either of Chiaverini's
arguments about the felony charge's basis. In the Sixth Cir-
cuit's view, there was clearly probable cause to support the
two misdemeanor charges the offcers had fled. See App.
to Pet. for Cert. 11a–16a. And because that was true, the
court thought, the validity of the felony charge did not mat-
ter. “So long as probable cause supports at least one charge
against Chiaverini (like his receipt-of-stolen-property viola-
tion),” then his malicious-prosecution claim “based on other
charges (like his money-laundering charge) also fail[s].” Id.,
at 10a. Or said another way, a single valid charge in a pro-
ceeding would insulate offcers from a Fourth Amendment
malicious-prosecution claim relating to any other charges, no
matter how baseless.
   In taking that position, the Sixth Circuit stepped out on
its own. Three other Courts of Appeals have held that the
presence of probable cause for one charge does not automati-
cally defeat a Fourth Amendment malicious-prosecution
Page Proof Pending Publication
claim alleging the absence of probable cause for another
charge. See Williams v. Aguirre, 965 F. 3d 1147, 1159–1162
(CA11 2020); Johnson v. Knorr, 477 F. 3d 75, 83–85 (CA3
2007); Posr v. Doherty, 944 F. 2d 91, 100 (CA2 1991).
   We granted certiorari to resolve that circuit split, 601
U. S. ––– (2023), and we now vacate the decision below.

                                II
   Section 1983 enables an individual to recover damages
from a state or local offcial for the deprivation of a constitu-
tional right. Such a suit is of course premised on a constitu-
tional violation. But its elements and rules may also be
shaped by common-law tort principles, against whose back-
drop § 1983 was enacted. See Manuel v. Joliet, 580 U. S.
357, 370 (2017). To determine the precise contours of a con-
stitutional claim under § 1983, we have held, a court should
identify the “most analogous” common-law tort to the consti-
tutional harm alleged. Ibid. And the court should incorpo-
562          CHIAVERINI v. CITY OF NAPOLEON

                      Opinion of the Court

rate that tort's requirements to the extent consistent with
“the values and purposes of the constitutional right at issue.”
Ibid.; Thompson, 596 U. S., at 43.
   The claim Chiaverini brought—a Fourth Amendment
malicious-prosecution claim—emerged from that method.
The constitutional violation alleged in such a suit is a type
of unreasonable seizure—an arrest and detention of a person
based on a criminal charge lacking probable cause. In
Thompson v. Clark, we analogized a suit alleging that
Fourth Amendment wrong to the common-law tort of mali-
cious prosecution. See id., at 43–44. The “gravamen” of
both, we reasoned, is “the wrongful initiation of charges
without probable cause” (though in the Fourth Amendment
context, those charges must cause a seizure as well). Id.,
at 43, and n. 2. Because of that similarity, the malicious-
prosecution tort can inform a court's understanding of the
kind of claim Chiaverini has brought.
Page Proof Pending Publication
   The question here is whether a Fourth Amendment
malicious-prosecution claim may succeed when a baseless
charge is accompanied by a valid charge. The Court of Ap-
peals, as described above, answered that question with a cat-
egorical no: Even if the felony count lacked probable cause,
the Sixth Circuit held, Chiaverini could not recover because
the misdemeanor counts were adequately supported. See
supra, at 560–561. But a funny thing happened on the way
to this Court. The offcers now agree with Chiaverini that
there is no such fat bar. See Brief for Offcers 24–27; Brief
for Chiaverini 2–3. And the United States as amicus cu-
riae also argues that the Sixth Circuit rule is wrong. See
Brief for United States 10. We agree with them all. Con-
sistent with both the Fourth Amendment and traditional
common-law practice, courts should evaluate suits like Chi-
averini's charge by charge.
   Consider frst how that result follows from established
Fourth Amendment law. Under that Amendment, a pretrial
detention (like the one Chiaverini suffered) must be based
                   Cite as: 602 U. S. 556 (2024)           563

                      Opinion of the Court

on probable cause. See Manuel, 580 U. S., at 364–369.
Otherwise, such a detention counts as an unreasonable sei-
zure. And even when a detention is justifed at the outset,
it may become unreasonably prolonged if the reason for it
lapses. See Rodriguez v. United States, 575 U. S. 348, 354–
357 (2015). So if an invalid charge—say, one fabricated by
police offcers—causes a detention either to start or to con-
tinue, then the Fourth Amendment is violated. And that is
so even when a valid charge has also been brought (although,
as soon noted, that charge may well complicate the causation
issue, see infra, at 564–565). Take the starkest possible ex-
ample. A person is detained on two charges—a drug offense
supported by probable cause and a gun offense built on lies.
The prosecutor, for whatever reason, drops the (valid) drug
charge, leaving the person in jail on the (invalid) gun charge
alone. The inclusion of the baseless charge—though
brought along with a good charge—has thus caused a consti-
Page Proof Pending Publication
tutional violation, by unreasonably extending the pretrial
detention. Even the Napoleon offcers agree, offering a sim-
ilar example. See Brief for Offcers 25; see also Brief for
United States 17–18. So the bringing of one valid charge in
a criminal proceeding should not categorically preclude a
claim based on the Fourth Amendment.
   And the same conclusion follows from the common-law
principles governing malicious-prosecution suits when § 1983
was enacted. As noted above, a plaintiff in such a suit had
to show that an offcial initiated a charge without probable
cause. See Thompson, 596 U. S., at 44; supra, at 562. He
did not have to show, however, that every charge brought
against him lacked an adequate basis. Rather, courts in
that era assessed probable cause charge by charge. “[I]f
groundless charges” are “coupled with others which are well
founded,” explained one State Supreme Court, the ground-
less ones could still “constitute a valid cause of action.”
Boogher v. Bryant, 86 Mo. 42, 49 (1885). Another agreed: It
was no “defen[s]e that there was probable cause for part of
564          CHIAVERINI v. CITY OF NAPOLEON

                      Opinion of the Court

the prosecution.” Barron v. Mason, 31 Vt. 189, 198 (1858).
Or as a leading treatise from the era summarized the rule:
“It is not necessary that the whole proceedings be utterly
groundless.” 2 S. Greenleaf, Law of Evidence 400 (10th ed.
1868); see 1 F. Hilliard, Law of Torts or Private Wrongs
§ 1, p. 435, n. (b) (4th ed. 1874). One bad charge, even if
joined with good ones, was enough to satisfy the malicious-
prosecution tort's “without probable cause” element.
   All that dooms the Sixth Circuit's categorical rule barring
a Fourth Amendment malicious-prosecution claim if any
charge is valid. That rule receives support from neither
half of the claim's name—neither from the Fourth Amend-
ment nor from the malicious-prosecution tort we have in-
voked as an analogy. And the question is not close, as
shown by the parties' decision not to contest it in this Court.
   The parties, almost needless to say, have found a sub-
stitute ground of disagreement, involving the element of cau-
Page Proof Pending Publication
sation. As noted earlier, a Fourth Amendment malicious-
prosecution suit depends not just on an unsupported charge,
but on that charge's causing a seizure—like the arrest and
three-day detention here. See supra, at 562. The parties
and amicus curiae offer three different views of how that
causation element is met when a valid charge is also in the
picture. Chiaverini's test is the easiest to satisfy. On his
view, when both valid and invalid charges are brought before
a judge for a probable cause determination, the warrant the
judge issues is irretrievably tainted; so any detention de-
pending on that warrant is the result of the invalid charge.
See Reply Brief 10–11 (citing Williams, 965 F. 3d, at 1165);
Tr. of Oral Arg. 5–6, 26–28. The United States disagrees,
arguing for the use of a but-for test to discover whether the
invalid charge, apart from the valid ones, caused a detention.
See id., at 41–43. The question then would be whether the
judge “in fact [would] have authorized” the detention had
the invalid charge not been present. Id., at 43. And fnally,
the offcers urge a still stricter test. In their view, the ques-
                  Cite as: 602 U. S. 556 (2024)           565

                     Thomas, J., dissenting

tion is whether the judge, absent the invalid charge, could
have legally authorized the detention—regardless of what he
really would have done. See Brief for Offcers 20–21.
   But that new dispute is not now ft for our resolution.
The test for fnding causation is no part of the question we
agreed to review. For that reason, it was not fully briefed.
And most important, the court below did not address the
matter, nor have many others. “[W]e are a court of review,
not of frst view.” Cutter v. Wilkinson, 544 U. S. 709, 718,
n. 7 (2005). So we leave the causation question in the hands
of the Sixth Circuit, as it further considers Chiaverini's
Fourth Amendment malicious-prosecution claim.
   We accordingly vacate the judgment of the Court of Ap-
peals and remand the case for further proceedings consistent
with this opinion.
                                            It is so ordered.

  Justice Thomas, with whom Justice Alito joins,
Page
dissenting. Proof Pending Publication
   Jascha Chiaverini sued several city offcials for damages
under 42 U. S. C. § 1983. He alleged that they violated his
Fourth Amendment rights by subjecting him to a mali-
cious prosecution. I continue to adhere to my belief that a
“malicious prosecution claim cannot be based on the Fourth
Amendment.” Manuel v. Joliet, 580 U. S. 357, 378 (2017)
(Alito, J., joined by Thomas, J., dissenting). Accordingly, I
would affrm the dismissal of Chiaverini's claim.
   To raise a successful claim under § 1983, a plaintiff must
allege the deprivation of “rights, privileges, or immunities
secured” to him by the Constitution. 42 U. S. C. § 1983.
“In order to fesh out the elements of th[e alleged] constitu-
tional tort,” the Court generally analogizes to common-law
torts. Manuel, 580 U. S., at 378 (opinion of Alito, J.); see
also Heck v. Humphrey, 512 U. S. 477, 483–484 (1994). In
this case, Chiaverini claims that he was seized without prob-
able cause in violation of the Fourth Amendment. Chiaver-
566           CHIAVERINI v. CITY OF NAPOLEON

                       Thomas, J., dissenting

ini principally relies on this Court's decision in Thompson v.
Clark, 596 U. S. 36 (2022), to argue that the appropriate tort
analog for this claim is malicious prosecution. In Thomp-
son, the Court held that malicious prosecution, a tort ad-
dressing “the wrongful initiation of charges without proba-
ble cause,” is most analogous to a Fourth Amendment
unreasonable-seizure claim. Id., at 43.
   Thompson was wrongly decided. A malicious-prosecution
claim bears little resemblance to an unreasonable seizure
under the Fourth Amendment. Consider what is required
to establish a claim of malicious prosecution. A plaintiff
must show that “(i) the suit or proceeding was `instituted
without any probable cause'; (ii) the `motive in instituting'
the suit `was malicious,' . . . ; and (iii) the prosecution `termi-
nated in the acquittal or discharge of the accused.' ” Id.,
at 44 (quoting T. Cooley, Law of Torts 181 (1880)). These
elements have no overlap with what is required to establish
Page Proof Pending Publication
a Fourth Amendment seizure violation.
   First, an unreasonable seizure can occur without any
prosecution—for instance, if a person “is arrested without
probable cause” and “released before any charges are fled.”
596 U. S., at 51–52 (Alito, J., dissenting). Second, an unrea-
sonable seizure does not depend on the seizing offcial's mo-
tives. “[W]hile subjective bad faith, i.e., malice, is the core
element of a malicious prosecution claim, it is frmly estab-
lished that the Fourth Amendment standard of reasonable-
ness is fundamentally objective.” Manuel, 580 U. S., at 379
(opinion of Alito, J.). Thus, “[i]f a law enforcement offcer
makes an arrest without probable cause, the arrest is unrea-
sonable and therefore unconstitutional even if the offcer har-
bors no ill will for the arrestee. Likewise, if an offcer
makes an arrest with probable cause, there is no Fourth
Amendment violation regardless of the `actual motivations
of the individual offcers involved.' ” Thompson, 596 U. S.,
at 52 (opinion of Alito, J.) (quoting Whren v. United States,
517 U. S. 806, 813 (1996)). Third, an unreasonable seizure
                   Cite as: 602 U. S. 556 (2024)           567

                     Thomas, J., dissenting

violates the Constitution regardless of how any subsequent
prosecution is resolved. See Manuel, 580 U. S., at 379 (opin-
ion of Alito, J.).
   Nor is an unreasonable seizure necessary to prove a
malicious-prosecution claim. A malicious prosecution can
occur without any seizure at all. For example, “[t]here are
cases in which defendants charged with nonviolent crimes
agree to appear for arraignment and are then released pend-
ing trial on their own recognizance. These defendants . . .
may bring a common-law suit for malicious prosecution . . . ,
but they are not seized.” Thompson, 596 U. S., at 52–53.
And, “since a malicious-prosecution claim does not require a
seizure, it obviously does not require proof that the per-
son bringing suit was seized without probable cause.” Id.,
at 53.
   Malicious prosecution is therefore not an appropriate tort
analog for a § 1983 claim alleging a seizure in violation of
Page Proof Pending Publication
the Fourth Amendment. The Court has never provided a
fulsome explanation for why it has concluded otherwise.
When the Court frst recognized a malicious-prosecution
claim under the Fourth Amendment in Thompson, it essen-
tially adopted the holdings of certain lower courts. Id., at
43. The Court offered two meager sentences to justify
doing so. It reasoned that “the gravamen of the Fourth
Amendment claim for malicious prosecution . . . is the wrong-
ful initiation of charges without probable cause. And the
wrongful initiation of charges without probable cause is like-
wise the gravamen of the tort of malicious prosecution.”
Ibid. That is incorrect. A malicious-prosecution claim pro-
tects against the malicious initiation of charges, but the
Fourth Amendment protects against unreasonable searches
and seizures—it does not matter whether the offcial acted
with malice or charges are ever initiated. See id., at 54–
55 (opinion of Alito, J.). Today, the Court rests solely on
Thompson's mistaken reasoning to conclude that Chiaverini
can raise his claim. See ante, at 562.
568             CHIAVERINI v. CITY OF NAPOLEON

                          Thomas, J., dissenting

   The Court's decision to forge ahead with combining the
malicious-prosecution and Fourth Amendment frameworks
will inevitably create confusion. As I have explained, an un-
reasonable seizure under the Fourth Amendment requires a
seizure; a malicious-prosecution claim does not. Supra, at
566. To resolve this mismatch, the Court has decided that
a plaintiff must show that a malicious prosecution caused an
unreasonable seizure. See Thompson, 596 U. S., at 43, n. 2;
ante, at 558, 564. While that grafting solved one problem,
it created several more. Because the Court has mixed two
distinct legal frameworks, it is unclear what doctrines actu-
ally govern its requirement that a malicious prosecution
cause a seizure. For example, if a plaintiff has multiple
charges, how does a court determine whether a particular
unfounded charge caused the seizure? See ante, at 564–565
(listing three possible causation theories). What type of ev-
idence is relevant? See Brief for Petitioners 40 (arguing
Page Proof Pending Publication
that Chiaverini would not have been seized absent the un-
founded charge since a similar defendant with a credible
charge was not seized). And, what happens if an unfounded
charge merely changes the nature of the seizure? See Brief
for United States as Amicus Curiae 18 (arguing that an un-
founded charge causes a seizure if it results in a more force-
ful arrest). The Court's claim for malicious prosecution
under the Fourth Amendment requires resolving these ques-
tions and more. To date, the Court has offered little guid-
ance on how to do so.* And, because the claim at issue is
the Court's own creation, lower courts cannot turn to the

   *The Court purports to offer some guidance today by rejecting the
Sixth Circuit's “categorical rule barring a Fourth Amendment malicious-
prosecution claim if any charge is valid.” Ante, at 564. But, it is not
clear that the Sixth Circuit even has such a rule. See Howse v. Hodous,
953 F. 3d 402, 409, n. 3 (2020) (recognizing that the underlying inquiry is
whether an unfounded charge “change[s] the nature of the seizure”); see
2023 WL 152477, *4 (Jan. 11, 2023) (citing Howse). It is thus unclear what,
if any, doctrinal progress today's decision makes.
                    Cite as: 602 U. S. 556 (2024)             569

                      Gorsuch, J., dissenting

common law or Fourth Amendment doctrine for answers.
Instead, they are left to make their best guess at how the
Court would defne its novel claim.
  I would take a far simpler course. Instead of forcing a
square peg into a round hole by judging an unreasonable
seizure based on the malicious-prosecution tort, I would
“hold that a malicious-prosecution claim may not be brought
under the Fourth Amendment.” Thompson, 596 U. S., at 60
(opinion of Alito, J.). I respectfully dissent.

  Justice Gorsuch, dissenting.
  Section 1983 performs vital work by permitting individu-
als to vindicate their constitutional rights in federal court.
But it does not authorize this Court to expound new rights
of its own creation. As this Court has put it, § 1983 does
not turn the Constitution into a “ ` “font of tort law.” ' ” Al-
bright v. Oliver, 510 U. S. 266, 284 (1994) (Kennedy, J., con-
Page Proof Pending Publication
curring in judgment) (quoting Parratt v. Taylor, 451 U. S.
527, 544 (1981)).
  Despite that settled rule, the Court today doubles down
on a new tort of its own recent invention—what it calls a
“Fourth Amendment malicious-prosecution” cause of action.
Ante, at 558; see Thompson v. Clark, 596 U. S. 36, 43–44
(2022). Respectfully, it is hard to know where this tort
comes from. Stare for as long as you like at the Fourth
Amendment and you won't see anything about prosecutions,
malicious or otherwise. Instead, the Amendment provides
that “[t]he right of the people to be secure . . . against unrea-
sonable searches and seizures, shall not be violated.”
  As its language suggests, the Fourth Amendment supplies
nothing like a common-law claim for malicious prosecution.
Ante, at 566 (Thomas, J., dissenting); see Cordova v. Albu-
querque, 816 F. 3d 645, 662–663 (CA10 2016) (Gorsuch, J.,
concurring in judgment). Just consider some of the differ-
ences. This Court has long held that the touchstone of the
Fourth Amendment is objective reasonableness. But a
570          CHIAVERINI v. CITY OF NAPOLEON

                     Gorsuch, J., dissenting

common-law malicious-prosecution claim focuses on the
defendant's subjective intent. Ante, at 566 (opinion of
Thomas, J.). The Fourth Amendment addresses the per-
missibility of a seizure. But a common-law malicious-
prosecution claim can (and usually does) proceed without
one. Ante, at 567. A seizure in violation of the Fourth
Amendment can (and often does) take place without the initi-
ation of any judicial process. But the whole point of a
malicious-prosecution claim is to contest the appropriateness
of past judicial proceedings. Ante, at 566. For all these
reasons, it's “pretty hard to see how you might squeeze any-
thing that looks quite like the common law tort of malicious
prosecution into the Fourth Amendment.” Cordova, 816
F. 3d, at 663 (opinion of Gorsuch, J.).
   That is not to say no constitutional hook exists for a § 1983
claim addressing the malicious use of process. Rather, it
seems to me only that such a claim would be more properly
Page Proof Pending Publication
housed in the Fourteenth Amendment. See Albright, 510
U. S., at 283 (opinion of Kennedy, J.). After all, unlike the
Fourth Amendment, that provision does focus on judicial
proceedings, guaranteeing those who come before our courts
“due process” of law. See ibid.; Thompson, 596 U. S., at 43,
n. 2; Cordova, 816 F. 3d, at 662 (opinion of Gorsuch, J.). In-
hering in due process is a promise that courts will respect,
at the least, those “customary procedures to which freemen
were entitled by the old law of England.” Sessions v. Di-
maya, 584 U. S. 148, 176 (2018) (Gorsuch, J., concurring in
part and concurring in judgment) (internal quotation marks
omitted). And the common law has long recognized a tort
of malicious prosecution to protect against the abuse of judi-
cial proceedings. Albright, 510 U. S., at 283 (opinion of
Kennedy, J.).
   Admittedly, a procedural due process claim for malicious
prosecution may come with its own set of limitations. After
all, when a State provides exactly the tort claim the plaintiff
seeks, it provides him with all the process he is due. See
                    Cite as: 602 U. S. 556 (2024)             571

                      Gorsuch, J., dissenting

id., at 284; Cordova, 816 F. 3d, at 662 (opinion of Gorsuch, J.).
And, consistent with the common law, many States recognize
claims for malicious prosecution. Indeed, the relevant State
here (Ohio) permits such a cause of action. Notably, too,
unlike the tort this Court seeks to cobble together under the
aegis of the Fourth Amendment, Ohio's tort does not require
a plaintiff to prove that he was seized. Compare Trussell
v. General Motors Corp., 53 Ohio St. 3d 142, 145–146, 559
N. E. 2d 732, 735–736 (1990), with ante, at 558 (majority opin-
ion). Of course, should a State fail to provide a malicious-
prosecution claim to secure his procedural due process
rights, or a fair forum for entertaining such a claim, a federal
court may need to act to vindicate § 1983 and the promise of
procedural due process. Cordova, 816 F. 3d, at 665 (opinion
of Gorsuch, J.). But in many cases (this one included), a
State malicious-prosecution claim may be both easier for a
plaintiff to prove than anything the Court today provides
and suffcient to ensure any process he is due. Albright, 510
Page Proof Pending Publication
U. S., at 285–286 (opinion of Kennedy, J.); Cordova, 816 F. 3d,
at 662 (opinion of Gorsuch, J.).
   For these reasons, I respectfully dissent.
                            Reporter’s Note

  The attached opinion has been revised to refect the usual publication
and citation style of the United States Reports. The revised pagination
makes available the offcial United States Reports citation in advance of
publication. The syllabus has been prepared by the Reporter of Decisions
for the convenience of the reader and constitutes no part of the opinion of
Page Proof Pending Publication
the Court. A list of counsel who argued or fled briefs in this case, and
who were members of the bar of this Court at the time this case was
argued, has been inserted following the syllabus. Other revisions may
include adjustments to formatting, captions, citation form, and any errant
punctuation. The following additional edits were made:

p. 557, line 3: “gun” is replaced with “(valid) drug”
p. 557, line 4: “drug” is replaced with “(invalid) gun”

```

---

## GROUP: content/cases/Chimel v. California.md  (`case`, 5 assertions)

### content_page

```
---
title: "Chimel v. California"
type: case
citation: "395 U.S. 752 (1969)"
parallel_cite: "89 S. Ct. 2034; 23 L. Ed. 2d 685"
neutral_cite: 1969 U.S. LEXIS 1166
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1969
date_decided: 1969-06-23
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1969-06-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Chimel v. California
  varies_by_point: false
  scope_note: "Good law and the foundational SITA rule; Gant (relying on Chimel's reaching-distance rationale) cabined the broad Belton reading of vehicle searches. Chimel's core is undisturbed."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107979/chimel-v-california/"
  cluster_id: 107979
  opinion_id: 9841975
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Key — Anchor"
related: ["[[Arizona v. Gant]]", "[[New York v. Belton]]", "[[Riley v. California]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "immediate-control", "warrantless-search"]
holding: "Foundational scope of search incident to arrest: the arrestee's person and the area 'within his immediate control' — meaning the area…"
lake:
  record_id: Chimel v. California
  status: verified
  projected_at: 2026-07-09
---

# Chimel v. California

*395 U.S. 752 (1969)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers arrested Chimel in his home on a burglary warrant, then — over his objection and without a search warrant — searched the entire three-bedroom house, including drawers, directing his wife to open them so they could view the contents. Coins and other items seized in the search were admitted at his burglary trial.

## Issue
Whether, incident to a lawful arrest, officers may search the arrestee's entire home without a warrant.

## Rule
No; the [[Search Incident to Arrest|search incident to arrest]] is limited to the arrestee's person and the area within his immediate reach. "There is ample justification, therefore, for a search of the arrestee's person and the area 'within his immediate control' — construing that phrase to mean the area from within which he might gain possession of a weapon or destructible evidence." — 395 U.S. 752, 763. ^pin-763

"There is no comparable justification, however, for routinely searching any room other than that in which an arrest occurs — or, for that matter, for searching through all the desk drawers or other closed or concealed areas in that room itself." — [*Id.*](https://www.courtlistener.com/opinion/107979/chimel-v-california/#:~:text=There%20is%20no%20comparable%20justification%2C) ^pin-763a

## Application
The search of Chimel's entire house — every room, drawers opened on command — reached far beyond his person and the area from which he could have grabbed a weapon or destroyed evidence while under arrest. Because nothing justified that house-wide search as incident to the arrest, and the officers had no search warrant, the seizure of items throughout the home was unconstitutional.

## Conclusion
The warrantless, house-wide [[Search Incident to Arrest|search incident to arrest]] was unreasonable; the conviction was reversed. *Chimel* fixed the officer-safety/evidence-preservation rationale and the "immediate control" scope of [[Search Incident to Arrest|search incident to arrest]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of *Chimel* itself. [[Arizona v. Gant]] **relied on** *Chimel*'s reaching-distance rationale to **narrow** the broad reading of [[New York v. Belton]] for vehicle searches; *Chimel*'s core person-and-immediate-control rule remains controlling.

## Appears on
- [[SIA Persons]] — *Key — Anchor*

## Sources
- *Chimel v. California*, 395 U.S. 752 (1969) — https://www.courtlistener.com/opinion/107979/chimel-v-california/ — pinpoint: 763.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f08a4a93a812671d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "395 U.S. 752 (1969)", "court": "U.S. Supreme Court", "neutral_cite": "1969 U.S. LEXIS 1166", "official_citation_present": true, "parallel_cite": "89 S. Ct. 2034; 23 L. Ed. 2d 685", "title": "Chimel v. California", "year": "1969"}}
{"assertion_id": "42642a8773078928", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Foundational scope of search incident to arrest: the arrestee's person and the area 'within his immediate control' — meaning the area…", "title": "Chimel v. California"}}
{"assertion_id": "c8a82fe4ff7beac1", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Persons"}, "payload": {"home": "SIA Persons", "role": "Key — Anchor", "title": "Chimel v. California"}}
{"assertion_id": "3435531275b2751a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Chimel v. California"}}
{"assertion_id": "8939f7f030a2e7f0", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1969-06-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Chimel v. California", "field_i_validity": "good_law", "scope_note": "Good law and the foundational SITA rule; Gant (relying on Chimel's reaching-distance rationale) cabined the broad Belton reading of vehicle searches. Chimel's core is undisturbed.", "title": "Chimel v. California", "varies_by_point": "false"}}
```

### lake record — Chimel v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Chimel v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Chimel v. California",
    "case_name_short": "Chimel",
    "case_name_full": "Chimel v. California",
    "input_case_name": "Chimel v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1969-06-23",
    "year": 1969,
    "docket": null,
    "cluster_id": 107979,
    "lead_opinion_id": 9841975,
    "sibling_ids": [
      107979,
      9841975,
      9841976,
      9841977
    ],
    "absolute_url": "/opinion/107979/chimel-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8974742,
        "score": 20,
        "case_name": "Chimel v. California"
      },
      {
        "cluster_id": 8973648,
        "score": 20,
        "case_name": "Chimel v. California"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "395 U.S. 752",
      "volume": "395",
      "reporter": "U.S.",
      "page": "752",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "89 S. Ct. 2034",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "2034",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "23 L. Ed. 2d 685",
        "volume": "23",
        "reporter": "L. Ed. 2d",
        "page": "685",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1969 U.S. LEXIS 1166",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "1166",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "395 U.S. 752",
        "volume": "395",
        "reporter": "U.S.",
        "page": "752",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 S. Ct. 2034",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "2034",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "23 L. Ed. 2d 685",
        "volume": "23",
        "reporter": "L. Ed. 2d",
        "page": "685",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1969 U.S. LEXIS 1166",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "1166",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "395 U.S. 752",
    "official_selection": {
      "court_class": "scotus",
      "selected": "395 U.S. 752",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-763",
      "page": null,
      "quote": "--- # Chimel v. California *395 U.S. 752 (1969)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers arrested Chimel in his home on a burglary warrant, then \u2014 over his objection and without a search warrant \u2014 searched the entire three-bedroom house, including drawers, directing his wife to open them so they could view the contents. Coins and other items seized in the search were admitted at his burglary trial. ## Issue Whether, incident to a lawful arrest, officers may search the arrestee's entire home without a warrant. ## Rule No; the search incident to arrest is limited to the arrestee's person and the area within his immediate reach.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-763a",
      "page": null,
      "quote": "There is no comparable justification, however, for routinely searching any room other than that in which an arrest occurs \u2014 or, for that matter, for searching through all the desk drawers or other closed or concealed areas in that room itself.",
      "star_marker": "763",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 28275,
      "fragment": "#:~:text=There%20is%20no%20comparable%20justification%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1969-06-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Chimel v. California",
    "varies_by_point": false,
    "scope_note": "Good law and the foundational SITA rule; Gant (relying on Chimel's reaching-distance rationale) cabined the broad Belton reading of vehicle searches. Chimel's core is undisturbed.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Rosario-Santiago",
          "cluster_id": 4666565,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane1_negative"
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
        "journal_ref": "Chimel v. California:lane1_negative"
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
        "journal_ref": "Chimel v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andre Anderson v. State of Indiana",
          "cluster_id": 4327181,
          "cite": [
            "64 N.E.3d 903",
            "2016 Ind. App. LEXIS 432",
            "2016 WL 7078344"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane1_negative"
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
        "journal_ref": "Chimel v. California:lane1_negative"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Royer",
          "cluster_id": 110890,
          "cite": [
            "75 L. Ed. 2d 229",
            "103 S. Ct. 1319",
            "460 U.S. 491",
            "1983 U.S. LEXIS 151",
            "51 U.S.L.W. 4293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chimel v. California",
          "cluster_id": 107979,
          "cite": [
            "23 L. Ed. 2d 685",
            "89 S. Ct. 2034",
            "395 U.S. 752",
            "1969 U.S. LEXIS 1166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stanley v. Illinois",
          "cluster_id": 108497,
          "cite": [
            "31 L. Ed. 2d 551",
            "92 S. Ct. 1208",
            "405 U.S. 645",
            "1972 U.S. LEXIS 70"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chambers v. Maroney",
          "cluster_id": 108184,
          "cite": [
            "26 L. Ed. 2d 419",
            "90 S. Ct. 1975",
            "399 U.S. 42",
            "1970 U.S. LEXIS 19"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gerstein v. Pugh",
          "cluster_id": 109186,
          "cite": [
            "43 L. Ed. 2d 54",
            "95 S. Ct. 854",
            "420 U.S. 103",
            "1975 U.S. LEXIS 29",
            "19 Fed. R. Serv. 2d 1499"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robinson",
          "cluster_id": 108893,
          "cite": [
            "38 L. Ed. 2d 427",
            "94 S. Ct. 467",
            "414 U.S. 218",
            "1973 U.S. LEXIS 21",
            "66 Ohio Op. 2d 202"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Opperman",
          "cluster_id": 109537,
          "cite": [
            "49 L. Ed. 2d 1000",
            "96 S. Ct. 3092",
            "428 U.S. 364",
            "1976 U.S. LEXIS 15"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chadwick",
          "cluster_id": 109714,
          "cite": [
            "53 L. Ed. 2d 538",
            "97 S. Ct. 2476",
            "433 U.S. 1",
            "1977 U.S. LEXIS 133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cady v. Dombrowski",
          "cluster_id": 108850,
          "cite": [
            "37 L. Ed. 2d 706",
            "93 S. Ct. 2523",
            "413 U.S. 433",
            "1973 U.S. LEXIS 48"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Watson",
          "cluster_id": 109352,
          "cite": [
            "46 L. Ed. 2d 598",
            "96 S. Ct. 820",
            "423 U.S. 411",
            "1976 U.S. LEXIS 121"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
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
        "journal_ref": "Chimel v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whiteley v. Warden, Wyoming State Penitentiary",
          "cluster_id": 108297,
          "cite": [
            "28 L. Ed. 2d 306",
            "91 S. Ct. 1031",
            "401 U.S. 560",
            "1971 U.S. LEXIS 65",
            "58 Ohio Op. 2d 434"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chimel v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107979 OR 9841975 OR 9841976 OR 9841977) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDQxODQzMjAwMDAwJnM9MzEzMzE3NiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107979+OR+9841975+OR+9841976+OR+9841977%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 6,
        "triage_snippet_classified": 194
      },
      "lane2_top_cited": {
        "query": "cites:(107979 OR 9841975 OR 9841976 OR 9841977)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjE2JnM9MTEwOTc2JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107979+OR+9841975+OR+9841976+OR+9841977%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107979 OR 9841975 OR 9841976 OR 9841977)",
        "reviewed": 58,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 58,
        "triage_read": 0,
        "triage_snippet_classified": 58
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107979 OR 9841975 OR 9841976 OR 9841977)",
    "indexed_citing_opinions": 4230,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107979,
        "count": 3919,
        "count_source": "search"
      },
      {
        "opinion_id": 9841975,
        "count": 423,
        "count_source": "search"
      },
      {
        "opinion_id": 9841976,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9841977,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6512,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/chimel-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyMDk0NDEmcz0xMDMzMDIyMCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28107979+OR+9841975+OR+9841976+OR+9841977%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9841976,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841976,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 237181,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 1272352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 1481331,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841975,
        "cited_id": 1893679,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 88122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 103705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 103831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 226125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 227881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 229424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 237181,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 244962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 246794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 1272352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 1481331,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 1893679,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 9416821,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 9419320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107979,
        "cited_id": 9841975,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 88122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 103705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 103831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 107102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 226125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 227881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 229424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 244962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 246794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 9416821,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9841977,
        "cited_id": 9419320,
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
    "date_created": "2026-07-05T00:04:45Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:05:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:05:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:07:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:05:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Chimel v. California

```
<opinion type="majority">
<author id="b827-8">Mb. Justice Stewakt</author>
<p id="AyX">delivered the opinion of the Court.</p>
<p id="b827-9">This case raises basic questions concerning the permissible scope under the Fourth Amendment of a search incident to a lawful arrest.</p>
<p id="b827-10">The relevant facts are essentially undisputed. Late in the afternoon of September 13, 1965, three police officers arrived at the Santa Ana, California, home of the petitioner with a warrant authorizing his arrest for the burglary of a coin shop. The officers knocked on the door, identified themselves to the petitioner’s wife, and asked if they might come inside. She ushered them into the house, where they waited 10 or 15 minutes until the petitioner returned home from work. When the petitioner entered the house, one of the officers handed him the arrest warrant and asked for permission to “look around.” The petitioner objected, but was advised that <page-number citation-index="1" label="754">*754</page-number>“on the basis of the lawful arrest,” the officers would nonetheless conduct a search. No search warrant had been issued.</p>
<p id="b828-5">Accompanied by the petitioner’s wife, the officers then looked through the entire three-bedroom house, including the attic, the garage, and a small workshop. In some rooms the search was relatively cursory. In the master bedroom and sewing room, however, the officers directed the petitioner’s wife to open drawers and “to physically move contents of the drawers from side to side so that [they] might view any items that would have come from [the] burglary.” After completing the search, they seized numerous items — primarily coins, but also several medals, tokens, and a few other objects. The entire search took between 45 minutes and an hour.</p>
<p id="b828-6">At the petitioner’s subsequent state trial on two charges of burglary, the items taken from his house were admitted into evidence against him, over his objection that they had been unconstitutionally seized. He was convicted, and the judgments of conviction were affirmed by both the California Court of Appeal, <span class="citation no-link">61 Cal. Rptr. 714</span>, and the California Supreme Court, <span class="citation" data-id="9848415"><a href="/opinion/1272352/people-v-chimel/" aria-description="Citation for case: People v. Chimel">68 Cal. 2d 436</a></span>, <span class="citation" data-id="9848415"><a href="/opinion/1272352/people-v-chimel/" aria-description="Citation for case: People v. Chimel">439 P. 2d 333</a></span>. Both courts accepted the petitioner’s contention that the arrest warrant was invalid because the supporting affidavit was set out in conclusory terms,<footnotemark>1</footnotemark> but held that since the arresting officers had procured the warrant “in good faith,” and since in any event they had had sufficient information to constitute probable cause for the petitioner’s arrest, that arrest had been lawful. From this conclusion the appellate courts went on to hold that the search of the petitioner’s home <page-number citation-index="1" label="755">*755</page-number>had been justified, despite the absence of a search warrant, on the ground that it had been incident to a valid arrest. We granted certiorari in order to consider the petitioner’s substantial constitutional claims. <span class="citation multiple-matches"><a href="/c/U.%20S./393/958/">393 U. S. 958</a></span>.</p>
<p id="b829-5">Without deciding the question, we proceed on the hypothesis that the California courts were correct in holding that the arrest of the petitioner was valid under the Constitution. This brings us directly to the question whether the warrantless search of the petitioner’s entire house can be constitutionally justified as incident to that arrest. The decisions of this Court bearing upon that question have been far from consistent, as even the most cursory review makes evident.</p>
<p id="b829-6">Approval of a warrantless search incident to a lawful arrest seems first to have been articulated by the Court in 1914 as dictum in <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, in which the Court stated:</p>
<blockquote id="b829-7">“What then is the present case? Before answering that inquiry specifically, it may be well by a process of exclusion to state what it is not. It is not an assertion of the right on the part of the Government, always recognized under English and American law, to search the person of the accused when legally arrested to discover and seize the fruits or evidences of crime.” <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States"><em>Id., </em>at 392</a></span>.</blockquote>
<p id="b829-8">That statement made no reference to any right to search the <em>place </em>where an arrest occurs, but was limited to a right to search the “person.” Eleven years later the case of <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>, brought the following embellishment of the <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>statement:</p>
<blockquote id="AmR">“When a man is legally arrested for an offense, whatever is found upon his person <em>or in his control </em>which it is unlawful for him to have and which may be used to prove the offense may be seized and held <page-number citation-index="1" label="756">*756</page-number>as evidence in the prosecution.” <em>Id., </em>at 158. (Emphasis added.)</blockquote>
<p id="b830-5">Still, that assertion too was far from a claim that the “place” where one is arrested may be searched so long as the arrest is valid. Without explanation, however, the principle emerged in expanded form a few months later in <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span> — although still by way of dictum:</p>
<blockquote id="b830-6">“The right without a search warrant contemporaneously to search persons lawfully arrested while committing crime and to search the place where the arrest is made in order to find and seize things connected with the crime as its fruits or as the means by which it was committed, as well as weapons and other things to effect an escape from custody, is not to be doubted. See <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 158</a></span>; <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span>.” <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S., at 30</a></span>.</blockquote>
<p id="b830-7">And in <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span>, two years later, the dictum of <em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">Agnello</a></span> </em>appeared to be the foundation of the Court’s decision. In that case federal agents had secured a search, warrant authorizing the seizure of liquor and certain articles used in its manufacture. When they arrived at the premises to be searched, they saw “that the place was used for retailing and drinking intoxicating liquors.” <em>Id., </em>at 194. They proceeded to arrest the person in charge and to execute the warrant. In searching a closet for the items listed in the warrant they came across an incriminating ledger, concededly not covered by the warrant, which they also seized. The Court upheld the seizure of the ledger by holding that since the agents had made a lawful arrest, “[t]hey had a right without a warrant contemporaneously to search the place in order to find and seize the things used to carry on the criminal enterprise.” <em>Id., </em>at 199.</p>
<p id="b831-4"><page-number citation-index="1" label="757">*757</page-number>That the <em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">Marron</a></span> </em>opinion did not mean all that it seemed to say became evident, however, a few years later in <em>Go-Bart Importing Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span>, and <em>United States </em>v. <em>Lefkowitz, </em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452</a></span>. In each of those cases the opinion of the Court was written by Mr. Justice Butler, the author of the opinion in <em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">Marron</a></span>. </em>In <em>Go-Bart, </em>agents had searched the office of persons whom they had lawfully arrested,<footnotemark>2</footnotemark> and had taken several papers from a desk, a safe, and other parts of the office. The Court noted that no crime had been committed in the agents’ presence, and that although the agent in charge “had an abundance of information and time to swear out a valid [search] warrant, he failed to do so.” <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#358" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S., at 358</a></span>. In holding the search and seizure unlawful, the Court stated:</p>
<blockquote id="b831-5">“Plainly the case before us is essentially different from <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span>. There, officers executing a valid search warrant for intoxicating liquors found and arrested one Birdsall who in pursuance of a conspiracy was actually engaged in running a saloon. As an incident to the arrest they seized a ledger in a closet where the liquor or some of it was kept and some bills beside the cash register. These things were visible and accessible and in the offender’s immediate custody. There was no threat of force or general search or rummaging of the place.” <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#358" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S., at 358</a></span>.</blockquote>
<p id="b831-6">This limited characterization of <em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">Marron</a></span> </em>was reiterated in <em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">Lefkowitz</a></span>, </em>a case in which the Court held unlawful a search of desk drawers and a cabinet despite the fact that the search had accompanied a lawful arrest. <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#465" aria-description="Citation for case: United States v. Lefkowitz">285 U. S., at 465</a></span>.</p>
<p id="b831-7">The limiting views expressed in <em>Go-Bart </em>and <em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">Lefkowitz</a></span> </em>were thrown to the winds, however, in <em>Harris </em>v. <em>United </em><page-number citation-index="1" label="758">*758</page-number><em>States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span>, decided in 1947. In that case, officers had obtained a warrant for Harris’ arrest on the basis of his alleged involvement with the cashing and interstate transportation of a forged check. He was arrested in the living room of his four-room apartment, and in an attempt to recover two canceled checks thought to have been used in effecting the forgery, the officers undertook a thorough search of the entire apartment. Inside a desk drawer they found a sealed envelope marked “George Harris, personal papers.” The envelope, which was then torn open, was found to contain altered Selective Service documents, and those documents were used to secure Harris’ conviction for violating the Selective Training and Service Act of 1940. The Court rejected Harris’ Fourth Amendment claim, sustaining the search as “incident to arrest.” <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#151" aria-description="Citation for case: Harris v. United States"><em>Id., </em>at 151</a></span>.</p>
<p id="b832-5">Only a year after <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span>, </em>however, the pendulum swung again. In <em>Trupiano </em>v. <em>United States, </em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span>, agents raided the site of an illicit distillery, saw one of several conspirators operating the still, and arrested him, contemporaneously “seiz[ing] the illicit distillery.” <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#702" aria-description="Citation for case: Trupiano v. United States"><em>Id., </em>at 702</a></span>. The Court held that the arrest and others made subsequently had been valid, but that the unexplained failure of the agents to procure a search warrant — in spite of the fact that they had had more than enough time before the raid to do so — rendered the search unlawful. The opinion stated:</p>
<blockquote id="b832-6">“It is a cardinal rule that, in seizing goods and articles, law enforcement agents must secure and use search warrants wherever reasonably practicable. . . . This rule rests upon the desirability of having magistrates rather than police officers determine when searches and seizures are permissible and what limitations should be placed upon such activities. ... To provide the necessary security against unreasonable intrusions upon the private lives of <page-number citation-index="1" label="759">*759</page-number>individuals, the framers of the Fourth Amendment required adherence to judicial processes wherever possible. And subsequent history has confirmed the wisdom of that requirement.</blockquote>
<blockquote id="b833-5">“A search or seizure without a warrant as an incident to a lawful arrest has always been considered to be a strictly limited right. It grows out of the inherent necessities of the situation at the time of the arrest. But there must be something more in the way of necessity than merely a lawful arrest.” <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#705" aria-description="Citation for case: Trupiano v. United States"><em>Id., </em>at 705, 708</a></span>.</blockquote>
<p id="b833-6">In 1950, two years after Trupiano,<footnotemark>3</footnotemark> came <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>, the decision upon which California primarily relies in the case now before us. In <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span>, </em>federal authorities had been informed that the defendant was dealing in stamps bearing forged overprints. On the basis of that information they secured a warrant for his arrest, which they executed at his one-room business office. At the time of the arrest, the officers “searched the desk, safe, and file cabinets in the office for about an hour and a half,” <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#59" aria-description="Citation for case: United States v. Rabinowitz"><em>id., </em>at 59</a></span>, and seized 573 stamps with forged overprints. The stamps were admitted into evidence at the defendant’s trial, and this Court affirmed his conviction, rejecting the contention that the warrantless search had been unlawful. The Court held that the search in its entirety fell within the principle giving law enforcement authorities “[t]he right 'to search the place where the arrest is made in order to find and seize things connected with the crime ....’” <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#61" aria-description="Citation for case: United States v. Rabinowitz"><em>Id., </em>at 61</a></span>. <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>was regarded as “ample authority” for that conclusion. <em>Id., </em>at 63. The opinion rejected the rule of <em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span> </em>that “in seizing goods and articles, law enforcement agents must secure and use search war<page-number citation-index="1" label="760">*760</page-number>rants wherever reasonably practicable.” The test, said the Court, “is not whether it is reasonable to procure a search warrant, but whether the search was reasonable.” <em>Id., </em>at 66.</p>
<p id="b834-5"><em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>has come to stand for the proposition, <em>inter alia, </em>that a warrantless search “incident to a lawful arrest” may generally extend to the area that is considered to be in the “possession” or under the “control” of the person arrested.<footnotemark>4</footnotemark> And it was on the basis of that proposition that the California courts upheld the search of the petitioner’s entire house in this case. That doctrine, however, at least in the broad sense in which it was applied by the California courts in this case, can withstand neither historical nor rational analysis.</p>
<p id="b834-6">Even limited to its own facts, the <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>decision was, as we have seen, hardly founded on an unimpeachable line of authority. As Mr. Justice Frankfurter commented in dissent in that case, the “hint” contained in <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>was, without persuasive justification, “loosely turned into dictum and finally elevated to a decision.” <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#76" aria-description="Citation for case: United States v. Rabinowitz">339 U. S., at 76</a></span>. And the approach taken in cases such as <em>Go-Bart, Lefkowitz, </em>and <em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span> </em>was essentially disregarded by the <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>Court.</p>
<p id="b834-7">Nor is the rationale by which the State seeks here to sustain the search of the petitioner’s house supported by a reasoned view of the background and purpose of the Fourth Amendment. Mr. Justice Frankfurter wisely pointed out in his <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>dissent that the Amendment’s proscription of “unreasonable searches and sei<page-number citation-index="1" label="761">*761</page-number>zures” must be read in light of “the history that gave rise to the words” — a history of “abuses so deeply felt by the Colonies as to be one of the potent causes of the Revolution . . . .” <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#69" aria-description="Citation for case: United States v. Rabinowitz">339 U. S., at 69</a></span>. The Amendment was in large part a reaction to the general warrants and war-rantless searches that had so alienated the colonists and had helped speed the movement for independence.<footnotemark>5</footnotemark> In the scheme of the Amendment, therefore, the requirement that “no Warrants shall issue, but upon probable cause,” plays a crucial part. As the Court put it in <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>:</p>
<blockquote id="b835-5">“We are not dealing with formalities. The presence of a search warrant serves a high function. Absent some grave emergency, the Fourth Amendment has interposed a magistrate between the citizen and the police. This was done not to shield criminals nor to make the home a safe haven for illegal activities. It was done so that an objective mind might weigh the need to invade that privacy in order to enforce the law. The right of privacy was deemed too precious to entrust to the discretion of those whose job is the detection of crime and the arrest of criminals. . . . And so the Constitution requires a magistrate to pass on the desires of the police before they violate the privacy of the home. We cannot be true to that constitutional requirement and excuse the absence of a search warrant without a showing by those who seek exemption from the constitutional mandate that the exigencies of the situation made that course imperative.” <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States"><em>Id., </em>at 455-456</a></span>.</blockquote>
<p id="ArJ"><page-number citation-index="1" label="762">*762</page-number>Even in the <em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">Agnello</a></span> </em>case the Court relied upon the rule that “[b]elief, however well founded, that an article sought is concealed in a dwelling house furnishes no justification for a search of that place without a warrant. And such searches are held unlawful notwithstanding facts unquestionably showing probable cause.” <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S., at 33</a></span>. Clearly, the general requirement that a search warrant be obtained is not lightly to be dispensed with, and “the burden is on those seeking [an] exemption [from the requirement] to show the need for it . . . .” <em>United States </em>v. <em>Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span>.</p>
<p id="b836-5">Only last Term in <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span>, we emphasized that “the police must, whenever practicable, obtain advance judicial approval of searches and seizures through the warrant procedure,” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><em>id., </em>at 20</a></span>,<footnotemark>6</footnotemark> and that “[t]he scope of [a] search must be ‘strictly tied to and justified by’ the circumstances which rendered its initiation permissible.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 19</a></span>. The search undertaken by the officer in that “stop and frisk” case was sustained under that test, because it was no more than a “protective . . . search for weapons.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 29</a></span>. But in a companion case, <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span>, we applied the same standard to another set of facts and reached a contrary result, holding that a policeman’s action in thrusting his hand into a suspect’s pocket had been neither motivated by nor limited to the objective of protection.<footnotemark>7</footnotemark> Rather, the search had been made in order to find narcotics, which were in fact found.</p>
<p id="b836-6">A similar analysis underlies the “search incident to arrest” principle, and marks its proper extent. When an <page-number citation-index="1" label="763">*763</page-number>arrest is made, it is reasonable for the arresting officer to search the person arrested in order to remove any weapons that the latter might seek to use in order to resist arrest or effect his escape. Otherwise, the officer’s safety might well be endangered, and the arrest itself frustrated. In addition, it is entirely reasonable for the arresting officer to search for and seize any evidence on the arrestee’s person in order to prevent its concealment or destruction. And the area into which an arrestee might reach in order to grab a weapon or evidentiary items must, of course, be governed by a like rule. A gun on a table or in a drawer in front of one who is arrested can be as dangerous to the arresting officer as one concealed in the clothing of the person arrested. There is ample justification, therefore, for a search of the arrestee’s person and the area “within his immediate control” — construing that phrase to mean the area from within which he might gain possession of a weapon or destructible evidence.</p>
<p id="b837-5">There is no comparable justification, however, for routinely searching any room other than that in which an arrest occurs — or, for that matter, for searching through all the desk drawers or other closed or concealed areas in that room itself. Such searches, in the absence of well-recognized exceptions, may be made only under the authority of a search warrant.<footnotemark>8</footnotemark> The “adherence to judicial processes” mandated by the Fourth Amendment requires no less.</p>
<p id="b837-6">This is the principle that underlay our decision in <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span>. In that case three men had been arrested in a parked car, which had later been towed to a garage and searched by police. We held the search to have been unlawful under the Fourth Amendment, despite the contention that it had <page-number citation-index="1" label="764">*764</page-number>been incidental to a valid arrest. Our reasoning was straightforward:</p>
<blockquote id="b838-6">“The rule allowing contemporaneous searches is justified, for example, by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crime— things which might easily happen where the weapon or evidence is on the accused’s person or under his immediate control. But these justifications are absent where a search is remote in time or place from the arrest.” <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States"><em>Id., </em>at 367</a></span>.<footnotemark>9</footnotemark></blockquote>
<p id="b838-7">The same basic principle was reflected in our opinion last Term in <em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">Sibron</a></span>. </em>That opinion dealt with <em>Peters </em>v. <em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">New York</a></span>, </em>No. 74, as well as with Sibron’s case, and <em>Peters </em>involved a search that we upheld as incident to a proper arrest. We sustained the search, however, only because its scope had been “reasonably limited” by the “need to seize weapons” and “to prevent the destruction of evidence,” to which <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston</a></span> </em>had referred. We emphasized that the arresting officer “did not engage in an unrestrained and thoroughgoing examination of Peters and his personal effects. He seized him to cut short his flight, and he searched him primarily for weapons.” 392 U. S., at 67.</p>
<p id="b838-8">It is argued in the present case that it is “reasonable” to search a man’s house when he is arrested in it. But that argument is founded on little more than a subjective view regarding the acceptability of certain sorts of police <page-number citation-index="1" label="765">*765</page-number>conduct, and not on considerations relevant to Fourth Amendment interests. Under such an unconfined analysis, Fourth Amendment protection in this area would approach the evaporation point. It is not easy to explain why, for instance, it is less subjectively “reasonable” to search a man’s house when he is arrested on his front lawn — or just down the street — than it is when he happens to be in the house at the time of arrest.<footnotemark>10</footnotemark> As Mr. Justice Frankfurter put it:</p>
<blockquote id="b839-5">“To say that the search must be reasonable is to require some criterion of reason. It is no guide at all either for a jury or for district judges or the police to say that an 'unreasonable search’ is forbidden— that the search must be reasonable. What is the test of reason which makes a search reasonable? The test is the reason underlying and expressed by the Fourth Amendment: the history and the experience which it embodies and the safeguards afforded by it against the evils to which it was a response.” <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#83" aria-description="Citation for case: United States v. Rabinowitz">339 U. S., at 83</a></span> (dissenting opinion).</blockquote>
<p id="b839-6">Thus, although “[t]he recurring questions of the reasonableness of searches” depend upon “the facts and circumstances — -the total atmosphere of the case,” <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#63" aria-description="Citation for case: United States v. Rabinowitz"><em>id., </em>at 63, 66</a></span> (opinion of the Court), those facts and circumstances must be viewed in the light of established Fourth Amendment principles.</p>
<p id="b840-5"><page-number citation-index="1" label="766">*766</page-number>It would be possible, of course, to draw a line between <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>and <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>on the one hand, and this case on the other. For <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>involved a single room, and <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>a four-room apartment, while in the case before us an entire house was searched. But such a distinction would be highly artificial. The rationale that allowed the searches and seizures in <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>and <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>would allow the searches and seizures in this case. No consideration relevant to the Fourth Amendment suggests any point of rational limitation, once the search is allowed to go beyond the area from which the person arrested might obtain weapons or evidentiary items.<footnotemark>11</footnotemark> The only reasoned distinction is one between a search of the person arrested and the area within his reach on the one hand, and more extensive searches on the other.<footnotemark>12</footnotemark></p>
<p id="b841-4"><page-number citation-index="1" label="767">*767</page-number>The petitioner correctly points out that one result of decisions such as <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>and <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>is to give law enforcement officials the opportunity to engage in searches not justified by probable cause, by the simple expedient of arranging to arrest suspects at home rather than elsewhere. We do not suggest that the petitioner is necessarily correct in his assertion that such a strategy was utilized here,<footnotemark>13</footnotemark> but the fact remains that had he been arrested earlier in the day, at his place of employment rather than at home, no search of his house could have been made without a search warrant. In any event, even apart from the possibility of such police tactics, the general point so forcefully made by Judge Learned Hand in <em>United States </em>v. <em>Kirschenblatt, </em><span class="citation" data-id="1481331"><a href="/opinion/1481331/united-states-v-kirschenblatt/" aria-description="Citation for case: United States v. Kirschenblatt">16 F. 2d 202</a></span>, remains:</p>
<blockquote id="b841-5">“After arresting a man in his house, to rummage at will among his papers in search of whatever will convict him, appears to us to be indistinguishable from what might be done under a general warrant; indeed, the warrant would give more protection, for presumably it must be issued by a magistrate. True, by hypothesis the power would not exist, if the supposed offender were not found on the prem<page-number citation-index="1" label="768">*768</page-number>ises; but it is small consolation to know that one’s papers are safe only so long as one is not at home.” <span class="citation" data-id="1481331"><a href="/opinion/1481331/united-states-v-kirschenblatt/#203" aria-description="Citation for case: United States v. Kirschenblatt"><em>Id., </em>at 203</a></span>.</blockquote>
<p id="b842-4"><em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>and <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>have been the subject of critical commentary for many years,<footnotemark>14</footnotemark> and have been relied upon less and less in our own decisions.<footnotemark>15</footnotemark> It is time, for the reasons we have stated, to hold that on their own facts, and insofar as the principles they stand for are inconsistent with those that we have endorsed today, they are no longer to be followed.</p>
<p id="b842-5">Application of sound Fourth Amendment principles to the facts of this case produces a clear result. The search here went far beyond the petitioner’s person and the area from within which he might have obtained either a weapon or something that could have been used as evidence against him. There was no constitutional justification, in the absence of a search warrant, for extending the search beyond that area. The scope of the search was, therefore, “unreasonable” under the Fourth and Fourteenth Amendments, and the petitioner’s conviction cannot stand.<footnotemark>16</footnotemark> <em>Reversed.</em></p>
<footnote label="1">
<p id="b828-7"> The affidavit supporting the warrant is set out in the opinion of the Court of Appeal, 61 Cal. Rptr., at 715-716, n. 1, and the State does not challenge its insufficiency under the principles of <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span>, and <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b831-8"> The Court assumed that the arrests were lawful. <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#356" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S., at 356</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b833-7"> See also <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b834-8"> Decisions of this Court since <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>have applied the abstract doctrine of that case to various factual situations with divergent results. Compare <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#42" aria-description="Citation for case: Ker v. California">374 U. S. 23, 42</a></span>; <em>Abel </em>v. <em>United States, </em><span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span>; and <em>Draper </em>v. <em>United States, </em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span>, with <em>Kremen </em>v. <em>United States, </em><span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span> <em>(per curiam). </em>Cf. <em>Chapman </em>v. <em>United States, </em><span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span>; <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499-500</a></span>.</p>
</footnote>
<footnote label="5">
<p id="b835-6"> See generally <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 624-625</a></span>; <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#389" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 389-391</a></span>; <em>Davis </em>v. <em>United States, </em><span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#603" aria-description="Citation for case: Davis v. United States">328 U. S. 582, 603-605</a></span> (dissenting opinion); <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#157" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 157-162</a></span> (dissenting opinion); <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481-482</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b836-7"> See also <em>Davis </em>v. <em>Mississippi, </em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#728" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 728</a></span>; <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#356" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 356-358</a></span>; <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#299" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 299</a></span>; <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b836-8"> Our <em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">Sibron</a></span> </em>opinion dealt with two cases. We refer here to No. 63, involving the appellant Sibron. See <em>infra, </em>at 764.</p>
</footnote>
<footnote label="8">
<p id="b837-7"> See <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357-358</a></span>.</p>
</footnote>
<footnote label="9">
<p id="b838-9"> Our holding today is of course entirely consistent with the recognized principle that, assuming the existence of probable cause, automobiles and other vehicles may be searched without warrants “where it is not practicable to secure a warrant because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought.” <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153</a></span>; see <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b839-7"> Some courts have carried the <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>approach to just such lengths. See, <em>e. g., Clifton </em>v. <em>United States, </em><span class="citation" data-id="237181"><a href="/opinion/237181/robert-francis-clifton-v-united-states/" aria-description="Citation for case: Robert Francis Clifton v. United States">224 F. 2d 329</a></span> (C. A. 4th Cir.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./350/894/">350 U. S. 894</a></span> (purchaser of illicit whiskey arrested in back yard of seller; search of one room of house sustained); <em>United States </em>v. <em>Jackson, </em><span class="citation" data-id="1893679"><a href="/opinion/1893679/united-states-v-jackson/" aria-description="Citation for case: United States v. Jackson">149 F. Supp. 937</a></span> (D. C. D. C.), rev’d on other grounds, 102 U. S. App. D. C. 109, <span class="citation multiple-matches"><a href="/c/F.%202d/250/772/">250 F. 2d 772</a></span> (suspect arrested half a block from his rented room; search of room upheld). But see <em>James </em>v. <em>Louisiana, </em><span class="citation" data-id="107102"><a href="/opinion/107102/james-v-louisiana/" aria-description="Citation for case: James v. Louisiana">382 U. S. 36</a></span> <em>(per curiam).</em></p>
</footnote>
<footnote label="11">
<p id="b840-6"> Cf. Mr. Justice Jackson’s dissenting comment in <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span>:</em></p>
<p id="b840-7">“The difficulty with this problem for me is that once the search is allowed to go beyond the person arrested and the objects upon him or in his immediate physical control, I see no practical limit short of that set in the opinion of the Court — and that means to me no limit at all.” <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#197" aria-description="Citation for case: Harris v. United States">331 U. S., at 197</a></span>.</p>
</footnote>
<footnote label="12">
<p id="b840-9"> It is argued in dissent that so long as there is probable cause to search the place where an arrest occurs, a search of that place should be permitted even though no search warrant has been obtained. This position seems to be based principally on two premises: first, that once an arrest has been made, the additional invasion of privacy stemming from the accompanying search is “relatively minor”; and second, that the victim of the search may “shortly thereafter” obtain a judicial determination of whether the search was justified by probable cause. With respect to the second premise, one may initially question whether all of the States in fact provide the speedy suppression procedures the dissent assumes. More fundamentally, however, we cannot accept the view that Fourth Amendment interests are vindicated so long as “the rights of the criminal” are “protected] . . . against introduction of evidence seized without probable cause.” The Amendment is designed to prevent, not simply to redress, unlawful police action. In any event, we cannot join in characterizing the invasion <page-number citation-index="1" label="767">*767</page-number>of privacy that results from a top-to-bottom search of a man’s house as “minor.” And we can see no reason why, simply because some interference with an individual’s privacy and freedom of movement has lawfully taken place, further intrusions should automatically be allowed despite the absence of a warrant that the Fourth Amendment would otherwise require.</p>
</footnote>
<footnote label="13">
<p id="b841-7"> Although the warrant was issued at 10:39 a. m. and the arrest was not made until late in the afternoon, the State suggests that the delay is accounted for by normal police procedures and by the heavy workload of the officer in charge. In addition, that officer testified that he and his colleagues went to the petitioner’s house “to keep from approaching him at his place of business to cause him any problem there.”</p>
</footnote>
<footnote label="14">
<p id="b842-6"> See, <em>e. g., </em>J. Landynski, Search and Seizure and the Supreme Court 87-117 (1966); Way, Increasing Scope of Search Incidental to Arrest, 1959 Wash. U. L. Q. 261; Note, Scope Limitations for Searches Incident to Arrest, 78 Yale L. J. 433 (1969); Note, The Supreme Court 1966 Term, <span class="citation no-link">81 Harv. L. Rev. 69</span>, 117-122 (1967).</p>
</footnote>
<footnote label="15">
<p id="b842-7"> Cf. <em>Dyke </em>v. <em>Taylor Implement Mfg. Co., </em><span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/#220" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S. 216, 220</a></span>; <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S., at 357-358, n. 20</a></span>; <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#299" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S., at 299</a></span>; <em>Stoner </em>v. <em>California, </em><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#487" aria-description="Citation for case: Stoner v. California">376 U. S. 483, 487</a></span>. But see <em>Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#62" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 62</a></span>; <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#42" aria-description="Citation for case: Ker v. California">374 U. S., at 42</a></span> (opinion of Clark, J.); cf. <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#91" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 91</a></span>; <em>Abel </em>v. <em>United States, </em><span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#236" aria-description="Citation for case: Abel v. United States">362 U. S., at 236-239</a></span>; <em>Giordenello </em>v. <em>United States, </em><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#488" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 488</a></span>.</p>
</footnote>
<footnote label="16">
<p id="b842-8"> The State has made various subsidiary contentions, including arguments that it would have been unduly burdensome to obtain a warrant specifying the coins to be seized and that introduction of the fruits of the search was harmless error. We reject those contentions as being without merit.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/City and County of San Francisco v. Sheehan.md  (`case`, 5 assertions)

### content_page

```
---
title: "City and County of San Francisco v. Sheehan"
type: case
citation: ""
parallel_cite: "575 U.S. 600; 135 S. Ct. 1765; 191 L. Ed. 2d 856; 83 U.S.L.W. 4303; 25 Fla. L. Weekly Fed. S 254"
neutral_cite: 2015 U.S. LEXIS 3200
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2015
date_decided: 2015-05-18
docket: 13-1412
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2015-05-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: City and County of San Francisco v. Sheehan
  varies_by_point: false
  scope_note: "Good law: QI for force against an armed, mentally ill suspect; the ADA-accommodation question was dismissed as improvidently granted (left open)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2801435/city-and-county-of-san-francisco-v-sheehan/"
  cluster_id: 2801435
  opinion_id: 2801435
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Progeny / Refinement"
related: ["[[Graham v. Connor]]", "[[Plumhoff v. Rickard]]", "[[Mullenix v. Luna]]"]
aliases: ["San Francisco v. Sheehan"]
tags: ["case", "use-of-force", "qualified-immunity", "mentally-ill", "clearly-established", "ada"]
holding: "Officers who used force against an armed, mentally ill suspect after a second entry into her room were entitled to qualified immunity because they violated no clearly established Fourth Amendment right; the ADA-accommodation question was dismissed as improvidently granted."
lake:
  record_id: City and County of San Francisco v. Sheehan
  status: verified
  projected_at: 2026-07-06
---

# City and County of San Francisco v. Sheehan

*575 U.S. 600 (2015)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Teresa Sheehan, who suffered from a schizoaffective disorder, lived in a San Francisco group home. After she threatened a social worker with a knife, Sergeant Kimberly Reynolds and Officer Kathrine Holder came to take her for psychiatric evaluation. They entered her room; Sheehan grabbed a knife and threatened to kill them, so they withdrew and closed the door. Fearing she might escape or gather more weapons, they reopened the door (a "second entry") rather than waiting; when Sheehan again advanced with the knife, they used pepper spray and then shot her several times (she survived). She sued under the Americans with Disabilities Act and under § 1983 for excessive force.

## Issue
Whether the officers were entitled to [[Qualified Immunity|qualified immunity]] for the force used after re-entering Sheehan's room (and whether the ADA's accommodation requirement applies to arrests).

## Rule
The Court declined to resolve the ADA question and held the officers immune. "we dismiss the first question as improvidently granted. We decide the second question and hold that the officers are entitled to qualified immunity because they did not violate any clearly established Fourth Amendment rights." — 575 U.S. at 600. ^pin-600

Even assuming the second entry could be found unreasonable, "no precedent clearly established that there was not 'an objective need for immediate entry' here," and "[w]ithout that 'fair notice,' an officer is entitled to qualified immunity." "In sum, we hold that qualified immunity applies because these officers had no 'fair and clear warning of what the Constitution requires.'" — 135 S. Ct. at 1778. ^pin-1778

## Application
The Ninth Circuit had relied on general circuit precedent to deny immunity, but no decision clearly established that reopening the door of an armed, violent, mentally ill suspect — to keep her from escaping or arming herself further — was unlawful. That the officers may have departed from their training in handling the mentally ill did not negate immunity, because an expert's view that a confrontation could have been handled differently cannot defeat immunity where a reasonable officer could have believed the conduct justified. The ADA question, whether accommodation duties apply when officers arrest an armed and dangerous suspect, was left unresolved as improvidently granted.

## Conclusion
Reversed in part; the first (ADA) question dismissed as improvidently granted. The officers were entitled to [[Qualified Immunity|qualified immunity]] on the Fourth Amendment claim because they violated no clearly established law.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Sheehan* applies the [[Graham v. Connor]] reasonableness standard and the high-specificity qualified-immunity approach of [[Mullenix v. Luna]] and [[Plumhoff v. Rickard]] to force against a mentally ill suspect, while expressly leaving open whether the ADA requires accommodation during an arrest. No negative treatment.

## Appears on
- [[Use of Force]] — *Key — Progeny / Refinement*
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *City and County of San Francisco v. Sheehan*, 575 U.S. 600 (2015) — https://www.courtlistener.com/opinion/2801435/city-and-county-of-san-francisco-v-sheehan/ — pinpoints: 600 (U.S. Reports, opening holding); 135 S. Ct. at 1778 (parallel reporter page-label confirmed in CL for the QI conclusion).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bf8287977e4d5bc4", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2015 U.S. LEXIS 3200", "official_citation_present": false, "parallel_cite": "575 U.S. 600; 135 S. Ct. 1765; 191 L. Ed. 2d 856; 83 U.S.L.W. 4303; 25 Fla. L. Weekly Fed. S 254", "title": "City and County of San Francisco v. Sheehan", "year": "2015"}}
{"assertion_id": "0edaaef590c81dfb", "dimension": "support", "kind": "home_role", "locator": {"home": "Use of Force"}, "payload": {"home": "Use of Force", "role": "Key — Progeny / Refinement", "title": "City and County of San Francisco v. Sheehan"}}
{"assertion_id": "57d9d175800a9d79", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Officers who used force against an armed, mentally ill suspect after a second entry into her room were entitled to qualified immunity because they violated no clearly established Fourth Amendment right; the ADA-accommodation question was dismissed as improvidently granted.", "title": "City and County of San Francisco v. Sheehan"}}
{"assertion_id": "37db8a8dc835a2da", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "City and County of San Francisco v. Sheehan"}}
{"assertion_id": "722a8ff0c679ac71", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2015-05-18", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "City and County of San Francisco v. Sheehan", "field_i_validity": "good_law", "scope_note": "Good law: QI for force against an armed, mentally ill suspect; the ADA-accommodation question was dismissed as improvidently granted (left open).", "title": "City and County of San Francisco v. Sheehan", "varies_by_point": "false"}}
```

### lake record — City and County of San Francisco v. Sheehan

```json
{
  "schema_version": "s2.v1",
  "record_id": "City and County of San Francisco v. Sheehan",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "City and County of San Francisco v. Sheehan",
    "case_name_short": "Sheehan",
    "case_name_full": "CITY AND COUNTY OF SAN FRANCISCO, CALIFORNIA, Et Al., Petitioners v. Teresa SHEEHAN.",
    "input_case_name": "City and County of San Francisco v. Sheehan",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2015-05-18",
    "year": 2015,
    "docket": "13-1412",
    "cluster_id": 2801435,
    "lead_opinion_id": 2801435,
    "sibling_ids": [
      2801435
    ],
    "absolute_url": "/opinion/2801435/city-and-county-of-san-francisco-v-sheehan/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "575 U.S. 600",
        "volume": "575",
        "reporter": "U.S.",
        "page": "600",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 S. Ct. 1765",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "1765",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "191 L. Ed. 2d 856",
        "volume": "191",
        "reporter": "L. Ed. 2d",
        "page": "856",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4303",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4303",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 254",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "254",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2015 U.S. LEXIS 3200",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "3200",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "575 U.S. 600",
        "volume": "575",
        "reporter": "U.S.",
        "page": "600",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 S. Ct. 1765",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "1765",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "191 L. Ed. 2d 856",
        "volume": "191",
        "reporter": "L. Ed. 2d",
        "page": "856",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 U.S. LEXIS 3200",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "3200",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4303",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4303",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 254",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "254",
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
      "id": "pin-600",
      "page": null,
      "quote": ") rather than waiting; when Sheehan again advanced with the knife, they used pepper spray and then shot her several times (she survived). She sued under the Americans with Disabilities Act and under \u00a7 1983 for excessive force. ## Issue Whether the officers were entitled to qualified immunity for the force used after re-entering Sheehan's room (and whether the ADA's accommodation requirement applies to arrests). ## Rule The Court declined to resolve the ADA question and held the officers immune.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1778",
      "page": null,
      "quote": "no precedent clearly established that there was not 'an objective need for immediate entry' here,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2015-05-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "City and County of San Francisco v. Sheehan",
    "varies_by_point": false,
    "scope_note": "Good law: QI for force against an armed, mentally ill suspect; the ADA-accommodation question was dismissed as improvidently granted (left open).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Morrow v. Meachum",
          "cluster_id": 8443910,
          "cite": [
            "917 F.3d 870"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Eunice Winzer v. Kaufman County",
          "cluster_id": 4591565,
          "cite": [
            "916 F.3d 464"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Michael Kingsley v. Stan Hendrickson",
          "cluster_id": 2898269,
          "cite": [
            "801 F.3d 828",
            "2015 U.S. App. LEXIS 15963",
            "2015 WL 5210679"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Barton Ex Rel. Estate of Barton v. Taber",
          "cluster_id": 3198370,
          "cite": [
            "820 F.3d 958",
            "2016 WL 1658098"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Benavidez v. County of San Diego",
          "cluster_id": 4872698,
          "cite": [
            "993 F.3d 1134"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Reese, Jr. v. County of Sacramento",
          "cluster_id": 4489118,
          "cite": [
            "888 F.3d 1030"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fleet Hamby v. Steven Hammond",
          "cluster_id": 3199645,
          "cite": [
            "821 F.3d 1085",
            "2016 U.S. App. LEXIS 7894",
            "2016 WL 1730532"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katie Joseph v. John Doe",
          "cluster_id": 4821017,
          "cite": [
            "981 F.3d 319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffery Mays v. Ronald Sprinkle",
          "cluster_id": 4869132,
          "cite": [
            "992 F.3d 295"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gutierrez v. Luna County",
          "cluster_id": 4321034,
          "cite": [
            "841 F.3d 895",
            "96 Fed. R. Serv. 3d 126",
            "2016 U.S. App. LEXIS 20466",
            "2016 WL 6694533"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Damon Wilson v. Prince George's County, Md",
          "cluster_id": 4508229,
          "cite": [
            "893 F.3d 213"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joan Kedra v. Richard Schroeter",
          "cluster_id": 4446761,
          "cite": [
            "876 F.3d 424"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Austin Gates v. Hassan Khokar",
          "cluster_id": 4476683,
          "cite": [
            "884 F.3d 1290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Vos v. City of Newport Beach",
          "cluster_id": 4506067,
          "cite": [
            "892 F.3d 1024"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott Lee Rudlaff v. Brandon Gillispie",
          "cluster_id": 2813642,
          "cite": [
            "791 F.3d 638",
            "2015 FED App. 0133p",
            "2015 U.S. App. LEXIS 11304",
            "2015 WL 3981335"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jamie Kirkpatrick v. County of Washoe",
          "cluster_id": 4328788,
          "cite": [
            "843 F.3d 784",
            "2016 U.S. App. LEXIS 21925",
            "2016 WL 7176654"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Knight Ex Rel. Kerr v. Miami-Dade County",
          "cluster_id": 4389467,
          "cite": [
            "856 F.3d 795",
            "103 Fed. R. Serv. 388",
            "97 Fed. R. Serv. 3d 1086",
            "2017 WL 1755573",
            "2017 U.S. App. LEXIS 8036"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Darrell Frederick v. City of Rogers, Arkansas",
          "cluster_id": 4434883,
          "cite": [
            "873 F.3d 641",
            "2017 WL 4622313",
            "2017 U.S. App. LEXIS 20221"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicole Haberle v. Daniel Troxell",
          "cluster_id": 4479031,
          "cite": [
            "885 F.3d 170"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Randy Cole v. Michael Hunter",
          "cluster_id": 4654098,
          "cite": [
            "935 F.3d 444"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Yvette Felarca v. Robert Birgeneau",
          "cluster_id": 4502868,
          "cite": [
            "891 F.3d 809"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Debbie Latits v. Lowell Phillips",
          "cluster_id": 4455479,
          "cite": [
            "878 F.3d 541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathan Capp v. County of San Diego",
          "cluster_id": 4667181,
          "cite": [
            "940 F.3d 1046"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harmon v. City of Arlington",
          "cluster_id": 5292775,
          "cite": [
            "16 F.4th 1159"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
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
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leonard Young, Jr. v. Deputy Superintendent Greene S",
          "cluster_id": 2898025,
          "cite": [
            "801 F.3d 172",
            "2015 U.S. App. LEXIS 15922",
            "2015 WL 5202968"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Entler v. Christine Gregoire",
          "cluster_id": 4432666,
          "cite": [
            "872 F.3d 1031",
            "2017 WL 4448218",
            "2017 U.S. App. LEXIS 19657"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City and County of San Francisco v. Sheehan:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2801435) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDM5ODU2MDAwMDAwJnM9MjgyODAxMSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%282801435%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      },
      "lane2_top_cited": {
        "query": "cites:(2801435)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDcmcz00Njg4Nzk3JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%282801435%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2801435)",
        "reviewed": 43,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 43,
        "triage_read": 0,
        "triage_snippet_classified": 43
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2801435)",
    "indexed_citing_opinions": 271,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2801435,
        "count": 271,
        "count_source": "search"
      }
    ],
    "citation_count": 1024,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/city-and-county-of-san-francisco-v-sheehan.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxOTQyNzImcz0xMDMyNTMyNSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%282801435%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2801435,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 112524,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 118228,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 118407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 145738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 145918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 195798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 670832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 674655,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 768131,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 769161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 775749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 777936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 796573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2801435,
        "cited_id": 796758,
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
    "date_created": "2026-07-05T00:07:42Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:07:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:07:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:11:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:07:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — City and County of San Francisco v. Sheehan

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

          CITY AND COUNTY OF SAN FRANCISCO, 

             CALIFORNIA, ET AL. v. SHEEHAN


CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE NINTH CIRCUIT

     No. 13–1412. Argued March 23, 2015—Decided May 18, 2015
Respondent Sheehan lived in a group home for individuals with mental
  illness. After Sheehan began acting erratically and threatened to kill
  her social worker, the City and County of San Francisco (San Fran-
  cisco) dispatched police officers Reynolds and Holder to help escort
  Sheehan to a facility for temporary evaluation and treatment. When
  the officers first entered Sheehan’s room, she grabbed a knife and
  threatened to kill them. They retreated and closed the door. Con-
  cerned about what Sheehan might do behind the closed door, and
  without considering if they could accommodate her disability, the of-
  ficers reentered her room. Sheehan, knife in hand, again confronted
  them. After pepper spray proved ineffective, the officers shot
  Sheehan multiple times. Sheehan later sued petitioner San Francis-
  co for, among other things, violating Title II of the Americans with
  Disabilities Act of 1990 (ADA) by arresting her without accommodat-
  ing her disability. See 42 U. S. C. §12132. She also sued petitioners
  Reynolds and Holder in their personal capacities under 42 U. S. C.
  §1983, claiming that they violated her Fourth Amendment rights.
  The District Court granted summary judgment because it concluded
  that officers making an arrest are not required to determine whether
  their actions would comply with the ADA before protecting them-
  selves and others, and also that Reynolds and Holder did not violate
  the Constitution. Vacating in part, the Ninth Circuit held that the
  ADA applied and that a jury must decide whether San Francisco
  should have accommodated Sheehan. The court also held that Reyn-
  olds and Holder are not entitled to qualified immunity because it is
  clearly established that, absent an objective need for immediate en-
  try, officers cannot forcibly enter the home of an armed, mentally ill
2             CITY AND COUNTY OF SAN FRANCISCO
                         v. SHEEHAN
                            Syllabus

    person who has been acting irrationally and has threatened anyone
    who enters.
Held:
    1. The question whether §12132 “requires law enforcement officers
 to provide accommodations to an armed, violent, and mentally ill
 suspect in the course of bringing the suspect into custody,” Pet. for
 Cert. i, is dismissed as improvidently granted. Certiorari was grant-
 ed on the understanding that San Francisco would argue that Title II
 of the ADA does not apply when an officer faces an armed and dan-
 gerous individual. Instead, San Francisco merely argues that
 Sheehan was not “qualified” for an accommodation, §12132, because
 she “pose[d] a direct threat to the health or safety of others,” which
 threat could not “be eliminated by a modification of policies, practices
 or procedures, or by the provision of auxiliary aids or services,” 28
 CFR §§35.139(a), 35.104. This argument was not passed on by the
 court below. The decision to dismiss this question as improvidently
 granted, moreover, is reinforced by the parties’ failure to address the
 related question whether a public entity can be vicariously liable for
 damages under Title II for an arrest made by its police officers.
 Pp. 7–10.
    2. Reynolds and Holder are entitled to qualified immunity from lia-
 bility for the injuries suffered by Sheehan. Public officials are im-
 mune from suit under 42 U. S. C. §1983 unless they have “violated a
 statutory or constitutional right that was ‘ “ ‘clearly established’ ” ’ at
 the time of the challenged conduct,” Plumhoff v. Rickard, 572 U. S.
 ___, ___, an exacting standard that “gives government officials
 breathing room to make reasonable but mistaken judgments,” Ash-
 croft v. al-Kidd, 563 U. S. ___, ___. The officers did not violate the
 Fourth Amendment when they opened Sheehan’s door the first time,
 and there is no doubt that they could have opened her door the sec-
 ond time without violating her rights had Sheehan not been disabled.
 Their use of force was also reasonable. The only question therefore is
 whether they violated the Fourth Amendment when they decided to
 reopen Sheehan’s door rather than attempt to accommodate her dis-
 ability. Because any such Fourth Amendment right, even assuming
 it exists, was not clearly established, Reynolds and Holder are enti-
 tled to qualified immunity. Likewise, an alleged failure on the part of
 the officers to follow their training does not itself negate qualified
 immunity where it would otherwise be warranted. Pp. 10–17.
Certiorari dismissed in part; 743 F. 3d 1211, reversed in part and re-
  manded.

  ALITO, J., delivered the opinion of the Court, in which ROBERTS, C. J.,
and KENNEDY, THOMAS, GINSBURG, and SOTOMAYOR, JJ., joined. SCALIA,
                     Cite as: 575 U. S. ____ (2015)                    3

                                Syllabus

J., filed an opinion concurring in part and dissenting in part, in which
KAGAN, J., joined. BREYER, J., took no part in the consideration or deci-
sion of the case.
                       Cite as: 575 U. S. ____ (2015)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash-
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 13–1412
                                  _________________


       CITY AND COUNTY OF SAN FRANCISCO, 

         CALIFORNIA, ET AL., PETITIONERS v.

                TERESA SHEEHAN

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE NINTH CIRCUIT

                                [May 18, 2015] 


  JUSTICE ALITO delivered the opinion of the Court.
  We granted certiorari to consider two questions relating
to the manner in which San Francisco police officers ar-
rested a woman who was suffering from a mental illness
and had become violent. After reviewing the parties’
submissions, we dismiss the first question as improvidently
granted. We decide the second question and hold that
the officers are entitled to qualified immunity because
they did not violate any clearly established Fourth
Amendment rights.
                             I
   Petitioners are the City and County of San Francisco,
California (San Francisco), and two police officers, Ser-
geant Kimberly Reynolds and Officer Kathrine Holder.
Respondent is Teresa Sheehan, a woman who suffers from
a schizoaffective disorder. Because this case arises in a
summary judgment posture, we view the facts in the light
most favorable to Sheehan, the nonmoving party. See,
e.g., Plumhoff v. Rickard, 572 U. S. ___, ___–___ (2014)
(slip op., at 1–2).
2          CITY AND COUNTY OF SAN FRANCISCO
                       v. SHEEHAN
                    Opinion of the Court

  In August 2008, Sheehan lived in a group home for
people dealing with mental illness. Although she shared
common areas of the building with others, she had a pri-
vate room. On August 7, Heath Hodge, a social worker
who supervised the counseling staff in the building, at-
tempted to visit Sheehan to conduct a welfare check.
Hodge was concerned because Sheehan had stopped tak-
ing her medication, no longer spoke with her psychiatrist,
and reportedly was no longer changing her clothes or
eating. See 743 F. 3d 1211, 1218 (CA9 2014); App. 23–24.
  Hodge knocked on Sheehan’s door but received no an-
swer. He then used a key to enter her room and found
Sheehan on her bed. Initially, she would not respond to
questions. But she then sprang up, reportedly yelling,
“Get out of here! You don’t have a warrant! I have a
knife, and I’ll kill you if I have to.” Hodge left without
seeing whether she actually had a knife, and Sheehan
slammed the door shut behind him. See 743 F. 3d, at
1218.
  Sheehan, Hodge realized, required “some sort of inter-
vention,” App. 96, but he also knew that he would need
help. Hodge took steps to clear the building of other peo-
ple and completed an application to have Sheehan de-
tained for temporary evaluation and treatment. See Cal.
Welf. & Inst. Code Ann. §5150 (West 2015 Cum. Supp.)
(authorizing temporary detention of someone who “as a
result of a mental health disorder, is a danger to others, or
to himself or herself, or gravely disabled”). On that appli-
cation, Hodge checked off boxes indicating that Sheehan
was a “threat to others” and “gravely disabled,” but he did
not mark that she was a danger to herself. 743 F. 3d, at
1218. He telephoned the police and asked for help to take
Sheehan to a secure facility.
  Officer Holder responded to police dispatch and headed
toward the group home. When she arrived, Holder re-
viewed the temporary-detention application and spoke
                  Cite as: 575 U. S. ____ (2015)            3

                      Opinion of the Court

with Hodge. Holder then sought assistance from Sergeant
Reynolds, a more experienced officer. After Reynolds
arrived and was brought up to speed, Hodge spoke with a
nurse at the psychiatric emergency services unit at San
Francisco General Hospital who said that the hospital
would be able to admit Sheehan.
  Accompanied by Hodge, the officers went to Sheehan’s
room, knocked on her door, announced who they were, and
told Sheehan that “we want to help you.” App. 36. When
Sheehan did not answer, the officers used Hodge’s key to
enter the room. Sheehan reacted violently. She grabbed a
kitchen knife with an approximately 5-inch blade and
began approaching the officers, yelling something along
the lines of “I am going to kill you. I don’t need help. Get
out.” Ibid. See also id., at 284 (“[Q.] Did you tell them I’ll
kill you if you don’t get out of here? A. Yes”). The offic-
ers—who did not have their weapons drawn—“retreated
and Sheehan closed the door, leaving Sheehan in her room
and the officers and Hodge in the hallway.” 743 F. 3d, at
1219. The officers called for backup and sent Hodge
downstairs to let in reinforcements when they arrived.
  The officers were concerned that the door to Sheehan’s
room was closed. They worried that Sheehan, out of their
sight, might gather more weapons—Reynolds had already
observed other knives in her room, see App. 228—or even
try to flee through the back window, id., at 227. Because
Sheehan’s room was on the second floor, she likely would
have needed a ladder to escape. Fire escapes, however,
are common in San Francisco, and the officers did not
know whether Sheehan’s room had such an escape. (Nei-
ther officer asked Hodge about a fire escape, but if they
had, it seems he “probably” would have said there was
one, id., at 117). With the door closed, all that Reynolds
and Holder knew for sure was that Sheehan was unstable,
she had just threatened to kill three people, and she had a
4             CITY AND COUNTY OF SAN FRANCISCO
                          v. SHEEHAN
                       Opinion of the Court

weapon.1
  Reynolds and Holder had to make a decision. They
could wait for backup—indeed, they already heard sirens.
Or they could quickly reenter the room and try to subdue
Sheehan before more time elapsed. Because Reynolds
believed that the situation “required [their] immediate
attention,” id., at 235, the officers chose reentry. In mak-
ing that decision, they did not pause to consider whether
Sheehan’s disability should be accommodated. See 743
F. 3d, at 1219. The officers obviously knew that Sheehan
was unwell, but in Reynolds’ words, that was “a secondary
issue” given that they were “faced with a violent woman
who had already threatened to kill her social worker” and
“two uniformed police officers.” App. 235.
  The officers ultimately decided that Holder—the larger
officer—should push the door open while Reynolds used
pepper spray on Sheehan. With pistols drawn, the officers
moved in. When Sheehan, knife in hand, saw them, she
again yelled for them to leave. She may also have again
said that she was going to kill them. Sheehan is “not
sure” if she threatened death a second time, id., at 284,
but “concedes that it was her intent to resist arrest and to
use the knife,” 743 F. 3d, at 1220. In any event, Reynolds
began pepper-spraying Sheehan in the face, but Sheehan
would not drop the knife. When Sheehan was only a few
——————
   1 The officers also may have feared that another person was with

Sheehan. Reynolds testified that the officers had not been “able to do a
complete assessment of the entire room.” App. 38. Sheehan, by con-
trast, testified during a deposition that the officers “could see . . . that
no one else was in the room.” Id., at 279. Before the Ninth Circuit,
Sheehan conceded that some of her deposition testimony “smacks of
irrationality that begs the question whether any of it is credible.” Brief
for Appellant in No. 11–16401 (CA9), p. 41; see also Reply Brief in No.
11–16401, p. 17 (explaining that “the inherent inconsistences in her
testimony cast suspicion over all of it”). We need not decide whether
there is a genuine dispute of fact here because the officers’ other,
independent concerns make this point immaterial.
                     Cite as: 575 U. S. ____ (2015)                   5

                         Opinion of the Court

feet away, Holder shot her twice, but she did not collapse.
Reynolds then fired multiple shots.2 After Sheehan finally
fell, a third officer (who had just arrived) kicked the knife
out of her hand. Sheehan survived.
   Sometime later, San Francisco prosecuted Sheehan for
assault with a deadly weapon, assault on a peace officer
with a deadly weapon, and making criminal threats. The
jury acquitted Sheehan of making threats but was unable
to reach a verdict on the assault counts, and prosecutors
decided not to retry her.
   Sheehan then brought suit, alleging, among other
things, that San Francisco violated the Americans with
Disabilities Act of 1990 (ADA), 104 Stat. 327, 42 U. S. C.
§12101 et seq., by subduing her in a manner that did not
reasonably accommodate her disability. She also sued
Reynolds and Holder in their personal capacities under
Rev. Stat. §1979, 42 U. S. C. §1983, for violating her
Fourth Amendment rights. In support of her claims, she
offered testimony from a former deputy police chief, Lou
Reiter, who contended that Reynolds and Holder fell short
of their training by not using practices designed to mini-
mize the risk of violence when dealing with the mentally
ill.
   The District Court granted summary judgment for
petitioners. Relying on Hainze v. Richards, 207 F. 3d 795
(CA5 2000), the court held that officers making an arrest
are not required “to first determine whether their actions
would comply with the ADA before protecting themselves
and others.” App. to Pet. for Cert. 80. The court also held
that the officers did not violate the Fourth Amendment.
The court wrote that the officers “had no way of knowing

——————
  2 There  is a dispute regarding whether Sheehan was on the ground
for the last shot. This dispute is not material: “Even if Sheehan was on
the ground, she was certainly not subdued.” 743 F. 3d 1211, 1230 (CA9
2014).
6          CITY AND COUNTY OF SAN FRANCISCO
                       v. SHEEHAN
                    Opinion of the Court

whether [Sheehan] might escape through a back window
or fire escape, whether she might hurt herself, or whether
there was anyone else in her room whom she might hurt.”
Id., at 71. In addition, the court observed that Holder did
not begin shooting until it was necessary for her to do so in
order “to protect herself ” and that “Reynolds used deadly
force only after she found that pepper spray was not
enough force to contain the situation.” Id., at 75, 76–77.
  On appeal, the Ninth Circuit vacated in part. Relevant
here, the panel held that because the ADA covers public
“services, programs, or activities,” §12132, the ADA’s
accommodation requirement should be read to “to encom-
pass ‘anything a public entity does,’ ” 743 F. 3d, at 1232.
The Ninth Circuit agreed “that exigent circumstances
inform the reasonableness analysis under the ADA,” ibid.,
but concluded that it was for a jury to decide whether San
Francisco should have accommodated Sheehan by, for
instance, “respect[ing] her comfort zone, engag[ing] in non-
threatening communications and us[ing] the passage of
time to defuse the situation rather than precipitating a
deadly confrontation.” Id., at 1233.
  As to Reynolds and Holder, the panel held that their
initial entry into Sheehan’s room was lawful and that,
after the officers opened the door for the second time, they
reasonably used their firearms when the pepper spray
failed to stop Sheehan’s advance. Nonetheless, the panel
also held that a jury could find that the officers “provoked”
Sheehan by needlessly forcing that second confrontation.
Id., at 1216, 1229. The panel further found that it was
clearly established that an officer cannot “forcibly enter
the home of an armed, mentally ill subject who had been
acting irrationally and had threatened anyone who en-
tered when there was no objective need for immediate
entry.” Id., at 1229. Dissenting in part, Judge Graber
would have held that the officers were entitled to qualified
immunity.
                  Cite as: 575 U. S. ____ (2015)             7

                      Opinion of the Court

  San Francisco and the officers petitioned for a writ of
certiorari and asked us to review two questions. We
granted the petition. 574 U. S. ___ (2014).
                              II
   Title II of the ADA commands that “no qualified indi-
vidual with a disability shall, by reason of such disability,
be excluded from participation in or be denied the benefits
of the services, programs, or activities of a public entity, or
be subjected to discrimination by any such entity.” 42
U. S. C. §12132. The first question on which we granted
review asks whether this provision “requires law enforce-
ment officers to provide accommodations to an armed,
violent, and mentally ill suspect in the course of bringing
the suspect into custody.” Pet. for Cert. i. When we
granted review, we understood this question to embody
what appears to be the thrust of the argument that San
Francisco made in the Ninth Circuit, namely that “ ‘Title II
does not apply to an officer’s on-the-street responses to
reported disturbances or other similar incidents, whether
or not those calls involve subjects with mental disabilities,
prior to the officer’s securing the scene and ensuring that
there is no threat to human life.’ ” Brief for Appellees in
No. 11–16401 (CA9), p. 36 (quoting Hainze, supra, at 801;
emphasis added); see also Brief for Appellees in No. 11–
16401, at 37 (similar).
   As San Francisco explained in its reply brief at the
certiorari stage, resolving its “question presented” “does
not require a fact-intensive ‘reasonable accommodation’
inquiry,” since “the only question for this Court to resolve
is whether any accommodation of an armed and violent
individual is reasonable or required under Title II of the
ADA.” Reply to Brief in Opposition 3.
   Having persuaded us to grant certiorari, San Francisco
chose to rely on a different argument than what it pressed
below. In its brief in this Court, San Francisco focuses on
8          CITY AND COUNTY OF SAN FRANCISCO
                       v. SHEEHAN
                    Opinion of the Court

the statutory phrase “qualified individual,” §12132, and a
regulation declaring that Title II “does not require a public
entity to permit an individual to participate in or benefit
from the services, programs, or activities of that public
entity when that individual poses a direct threat to the
health or safety of others.” 28 CFR §35.139(a) (2014).
Another regulation defines a “direct threat” as “a signifi-
cant risk to the health or safety of others that cannot be
eliminated by a modification of policies, practices or proce-
dures, or by the provision of auxiliary aids or services.”
§35.104. Putting these authorities together, San Fran-
cisco argues that “a person who poses a direct threat or
significant risk to the safety of others is not qualified for
accommodations under the ADA,” Brief for Petitioners 17.
Contending that Sheehan clearly posed a “direct threat,”
San Francisco concludes that she was therefore not “quali-
fied” for an accommodation.
   Though, to be sure, this “qualified” argument does ap-
pear in San Francisco’s certiorari petition, San Francisco
never hinted at it in the Ninth Circuit. The Court does
not ordinarily decide questions that were not passed on
below. More than that, San Francisco’s new argument
effectively concedes that the relevant provision of the
ADA, 42 U. S. C. §12132, may “requir[e] law enforcement
officers to provide accommodations to an armed, violent,
and mentally ill suspect in the course of bringing the
suspect into custody.” Pet. for Cert. i. This is so because
there may be circumstances in which any “significant risk”
presented by “an armed, violent, and mentally ill suspect”
can be “eliminated by a modification of policies, practices
or procedures, or by the provision of auxiliary aids or
services.”
   The argument that San Francisco now advances is
predicated on the proposition that the ADA governs the
manner in which a qualified individual with a disability is
arrested. The relevant provision provides that a public
                  Cite as: 575 U. S. ____ (2015)             9

                      Opinion of the Court

entity may not “exclud[e]” a qualified individual with a
disability from “participat[ing] in,” and may not “den[y]”
that individual the “benefits of[,] the services, programs,
or activities of a public entity.” §12132. This language
would apply to an arrest if an arrest is an “activity” in
which the arrestee “participat[es]” or from which the
arrestee may “benefi[t].”
   This same provision also commands that “no qualified
individual with a disability shall be . . . subjected to dis-
crimination by any [public] entity.” Ibid. This part of the
statute would apply to an arrest if the failure to arrest an
individual with a mental disability in a manner that
reasonably accommodates that disability constitutes “dis-
crimination.” Ibid.
   Whether the statutory language quoted above applies to
arrests is an important question that would benefit from
briefing and an adversary presentation. But San Fran-
cisco, the United States as amicus curiae, and Sheehan all
argue (or at least accept) that §12132 applies to arrests.
No one argues the contrary view. As a result, we do not
think that it would be prudent to decide the question in
this case.
   Our decision not to decide whether the ADA applies to
arrests is reinforced by the parties’ failure to address a
related question: whether a public entity can be liable for
damages under Title II for an arrest made by its police
officers. Only public entities are subject to Title II, see,
e.g., Pennsylvania Dept. of Corrections v. Yeskey, 524 U. S.
206, 208 (1998), and the parties agree that such an entity
can be held vicariously liable for money damages for the
purposeful or deliberately indifferent conduct of its em-
ployees. See Tr. of Oral Arg. 10–12, 22. But we have
never decided whether that is correct, and we decline to do
so here, in the absence of adversarial briefing.
   Because certiorari jurisdiction exists to clarify the law,
its exercise “is not a matter of right, but of judicial discre-
10           CITY AND COUNTY OF SAN FRANCISCO
                         v. SHEEHAN
                      Opinion of the Court

tion.” Supreme Court Rule 10. Exercising that discretion,
we dismiss the first question presented as improvidently
granted. See, e.g., Board of Trustees of Univ. of Ala. v.
Garrett, 531 U. S. 356, 360, n. 1 (2001) (partial dismissal);
Parker v. Dugger, 498 U. S. 308, 323 (1991) (same).
                             III
   The second question presented is whether Reynolds and
Holder can be held personally liable for the injuries that
Sheehan suffered. We conclude they are entitled to quali-
fied immunity.3
   Public officials are immune from suit under 42 U. S. C.
§1983 unless they have “violated a statutory or constitu-
tional right that was clearly established at the time of the
challenged conduct.” Plumhoff, 572 U. S., at ___ (slip op.,
at 12) (internal quotation marks omitted). An officer
“cannot be said to have violated a clearly established right
unless the right’s contours were sufficiently definite that
any reasonable official in [his] shoes would have under-
——————
   3 Not satisfied with dismissing question one, which concerns San

Francisco’s liability, our dissenting colleagues would further punish
San Francisco by dismissing question two as well. See post, at 3
(opinion of SCALIA, J.) (arguing that deciding the second question would
“reward” San Francisco and “spar[e it] the significant expense of
defending the suit, and satisfying any judgment, against the individual
petitioners”). But question two concerns the liability of the individual
officers. Whatever contractual obligations San Francisco may (or may
not) have to represent and indemnify the officers are not our concern.
At a minimum, these officers have a personal interest in the correctness
of the judgment below, which holds that they may have violated the
Constitution. Moreover, when we granted the petition, we determined
that both questions independently merited review. Because of the
importance of qualified immunity “to society as a whole,” Harlow v.
Fitzgerald, 457 U. S. 800, 814 (1982), the Court often corrects lower
courts when they wrongly subject individual officers to liability. See,
e.g., Carroll v. Carman, 574 U. S. ___ (2014) (per curiam); Wood v.
Moss, 572 U. S. ___ (2014); Plumhoff v. Rickard, 572 U. S. ___ (2014);
Stanton v. Sims, 571 U. S. ___ (2013) (per curiam); Reichle v. Howards,
566 U. S. ___ (2012).
                 Cite as: 575 U. S. ____ (2015)          11

                     Opinion of the Court

stood that he was violating it,” ibid., meaning that “exist-
ing precedent . . . placed the statutory or constitutional
question beyond debate.” Ashcroft v. al-Kidd, 563 U. S.
___, ___ (2011) (slip op., at 9). This exacting standard
“gives government officials breathing room to make rea-
sonable but mistaken judgments” by “protect[ing] all but
the plainly incompetent or those who knowingly violate
the law.” Id., at ___ (slip op., at 12).
   In this case, although we disagree with the Ninth Cir-
cuit’s ultimate conclusion on the question of qualified
immunity, we agree with its analysis in many respects.
For instance, there is no doubt that the officers did not
violate any federal right when they opened Sheehan’s door
the first time. See 743 F. 3d, at 1216, 1223. Reynolds and
Holder knocked on the door, announced that they were
police officers, and informed Sheehan that they wanted to
help her. When Sheehan did not come to the door, they
entered her room. This was not unconstitutional. “[L]aw
enforcement officers may enter a home without a warrant
to render emergency assistance to an injured occupant or
to protect an occupant from imminent injury.” Brigham
City v. Stuart, 547 U. S. 398, 403 (2006). See also Ken-
tucky v. King, 563 U. S. ___, ___ (2011) (slip op., at 6).
   Nor is there any doubt that had Sheehan not been dis-
abled, the officers could have opened her door the second
time without violating any constitutional rights. For one
thing, “because the two entries were part of a single,
continuous search or seizure, the officers [were] not re-
quired to justify the continuing emergency with respect to
the second entry.” 743 F. 3d, at 1224 (following Michigan
v. Tyler, 436 U. S. 499, 511 (1978)). In addition, Reynolds
and Holder knew that Sheehan had a weapon and had
threatened to use it to kill three people. They also knew
that delay could make the situation more dangerous. The
Fourth Amendment standard is reasonableness, and it is
reasonable for police to move quickly if delay “would
12         CITY AND COUNTY OF SAN FRANCISCO
                       v. SHEEHAN
                    Opinion of the Court

gravely endanger their lives or the lives of others.” War-
den, Md. Penitentiary v. Hayden, 387 U. S. 294, 298–299
(1967). This is true even when, judged with the benefit of
hindsight, the officers may have made “some mistakes.”
Heien v. North Carolina, 574 U. S. ___, ___ (2014) (slip op.,
at 5). The Constitution is not blind to “the fact that police
officers are often forced to make split-second judgments.”
Plumhoff, supra, at ___ (slip op., at 8).
   We also agree with the Ninth Circuit that after the
officers opened Sheehan’s door the second time, their use
of force was reasonable.         Reynolds tried to subdue
Sheehan with pepper spray, but Sheehan kept coming at
the officers until she was “only a few feet from a cornered
Officer Holder.” 743 F. 3d, at 1229. At this point, the use
of potentially deadly force was justified. See Scott v.
Harris, 550 U. S. 372, 384 (2007). Nothing in the Fourth
Amendment barred Reynolds and Holder from protecting
themselves, even though it meant firing multiple rounds.
See Plumhoff, supra, at ___ (slip op., at 11).
   The real question, then, is whether, despite these dan-
gerous circumstances, the officers violated the Fourth
Amendment when they decided to reopen Sheehan’s door
rather than attempting to accommodate her disability.
Here we come to another problem. San Francisco, whose
attorneys represent Reynolds and Holder, devotes scant
briefing to this question. Instead, San Francisco argues
almost exclusively that even if it is assumed that there
was a Fourth Amendment violation, the right was not
clearly established. This Court, of course, could decide the
constitutional question anyway. See Pearson v. Callahan,
555 U. S. 223, 242 (2009) (recognizing discretion). But
because this question has not been adequately briefed, we
decline to do so. See id., at 239. Rather, we simply decide
whether the officers’ failure to accommodate Sheehan’s
illness violated clearly established law. It did not.
   To begin, nothing in our cases suggests the constitu-
                 Cite as: 575 U. S. ____ (2015)           13

                     Opinion of the Court

tional rule applied by the Ninth Circuit. The Ninth Circuit
focused on Graham v. Connor, 490 U. S. 386 (1989), but
Graham holds only that the “ ‘objective reasonableness’ ”
test applies to excessive-force claims under the Fourth
Amendment. See id., at 388. That is far too general a
proposition to control this case. “We have repeatedly told
courts—and the Ninth Circuit in particular—not to define
clearly established law at a high level of generality.” al-
Kidd, supra, at ___ (citation omitted) (slip op., at 10); cf.
Lopez v. Smith, 574 U. S. ___, ___ (2014) (per curiam) (slip
op., at 5). Qualified immunity is no immunity at all if
“clearly established” law can simply be defined as the
right to be free from unreasonable searches and seizures.
   Even a cursory glance at the facts of Graham confirms
just how different that case is from this one. That case did
not involve a dangerous, obviously unstable person mak-
ing threats, much less was there a weapon involved.
There is a world of difference between needlessly with-
holding sugar from an innocent person who is suffering
from an insulin reaction, see Graham, supra, at 388–389,
and responding to the perilous situation Reynolds and
Holder confronted. Graham is a nonstarter.
   Moving beyond Graham, the Ninth Circuit also turned
to two of its own cases. But even if “a controlling circuit
precedent could constitute clearly established federal law
in these circumstances,” Carroll v. Carman, 574 U. S. ___,
___ (2014) (per curiam) (slip op., at 4), it does not do so
here.
   The Ninth Circuit first pointed to Deorle v. Rutherford,
272 F. 3d 1272 (CA9 2001), but from the very first para-
graph of that opinion we learn that Deorle involved an
officer’s use of a beanbag gun to subdue “an emotionally
disturbed” person who “was unarmed, had not attacked or
even touched anyone, had generally obeyed the instruc-
tions given him by various police officers, and had not
committed any serious offense.” Id., at 1275. The officer
14            CITY AND COUNTY OF SAN FRANCISCO
                          v. SHEEHAN
                       Opinion of the Court

there, moreover, “observed Deorle at close proximity for
about five to ten minutes before shooting him” in the face.
See id., at 1281. Whatever the merits of the decision in
Deorle, the differences between that case and the case
before us leap from the page. Unlike Deorle, Sheehan was
dangerous, recalcitrant, law-breaking, and out of sight.
   The Ninth Circuit also leaned on Alexander v. City and
County of San Francisco, 29 F. 3d 1355 (CA9 1994), an-
other case involving mental illness. There, officials from
San Francisco attempted to enter Henry Quade’s home
“for the primary purpose of arresting him” even though
they lacked an arrest warrant. Id., at 1361. Quade, in
response, fired a handgun; police officers “shot back, and
Quade died from gunshot wounds shortly thereafter.” Id.,
at 1358. The panel concluded that a jury should decide
whether the officers used excessive force. The court rea-
soned that the officers provoked the confrontation because
there were no “exigent circumstances” excusing their
entrance. Id., at 1361.
   Alexander too is a poor fit. As Judge Graber observed
below in her dissent, the Ninth Circuit has long read
Alexander narrowly. See 743 F. 3d, at 1235 (Graber, J.,
concurring in part and dissenting in part) (citing Billing-
ton v. Smith, 292 F. 3d 1177 (CA9 2002)). Under Ninth
Circuit law,4 an entry that otherwise complies with the
Fourth Amendment is not rendered unreasonable because
it provokes a violent reaction. See id., at 1189–1190.
——————
   4 Our citation to Ninth Circuit cases should not be read to suggest our

agreement (or, for that matter, disagreement) with them. The Ninth
Circuit’s “provocation” rule, for instance, has been sharply questioned
elsewhere. See Livermore v. Lubelan, 476 F. 3d 397, 406–407 (CA6
2007); see also, e.g., Hector v. Watt, 235 F. 3d 154, 160 (CA3 2001) (“[I]f
the officers’ use of force was reasonable given the plaintiff’s acts, then
despite the illegal entry, the plaintiff’s own conduct would be an inter-
vening cause”). Whatever their merits, all that matters for our quali-
fied immunity analysis is that they do not clearly establish any right
that the officers violated.
                 Cite as: 575 U. S. ____ (2015)           15

                     Opinion of the Court

Under this rule, qualified immunity necessarily applies
here because, as explained above, competent officers could
have believed that the second entry was justified under
both continuous search and exigent circumstance ration-
ales. Indeed, even if Reynolds and Holder misjudged the
situation, Sheehan cannot “establish a Fourth Amend-
ment violation based merely on bad tactics that result in a
deadly confrontation that could have been avoided.” Id.,
at 1190. Courts must not judge officers with “the 20/20
vision of hindsight.’ ” Ibid. (quoting Graham, 490 U. S., at
396).
   When Graham, Deorle, and Alexander are viewed to-
gether, the central error in the Ninth Circuit’s reasoning
is apparent. The panel majority concluded that these
three cases “would have placed any reasonable, competent
officer on notice that it is unreasonable to forcibly enter
the home of an armed, mentally ill suspect who had been
acting irrationally and had threatened anyone who en-
tered when there was no objective need for immediate
entry.” 743 F. 3d, at 1229. But even assuming that is
true, no precedent clearly established that there was not
“an objective need for immediate entry” here. No matter
how carefully a reasonable officer read Graham, Deorle,
and Alexander beforehand, that officer could not know
that reopening Sheehan’s door to prevent her from escap-
ing or gathering more weapons would violate the Ninth
Circuit’s test, even if all the disputed facts are viewed in
respondent’s favor. Without that “fair notice,” an officer is
entitled to qualified immunity. See, e.g., Plumhoff, 572
U. S., at ___ (slip op., at 13).
   Nor does it matter for purposes of qualified immunity
that Sheehan’s expert, Reiter, testified that the officers
did not follow their training. According to Reiter, San
Francisco trains its officers when dealing with the mentally
ill to “ensure that sufficient resources are brought to the
scene,” “contain the subject” and “respect the suspect’s
16          CITY AND COUNTY OF SAN FRANCISCO
                        v. SHEEHAN
                     Opinion of the Court

“comfort zone,” “use time to their advantage,” and “employ
non-threatening verbal communication and open-ended
questions to facilitate the subject’s participation in com-
munication.” Brief for Respondent 7. Likewise, San Fran-
cisco’s policy is “ ‘to use hostage negotiators’ ” when dealing
with “ ‘a suspect [who] resists arrest by barricading him-
self.’ ” Id., at 8 (quoting San Francisco Police Department
General Order 8.02, §II(B) (Aug. 3, 1994), online at
http://www.sf-police.org (as visited May 14, 2015, and
available in Clerk of Court’s case file)).
   Even if an officer acts contrary to her training, however,
(and here, given the generality of that training, it is not at
all clear that Reynolds and Holder did so), that does not
itself negate qualified immunity where it would otherwise
be warranted. Rather, so long as “a reasonable officer
could have believed that his conduct was justified,” a
plaintiff cannot “avoi[d] summary judgment by simply
producing an expert’s report that an officer’s conduct
leading up to a deadly confrontation was imprudent,
inappropriate, or even reckless.” Billington, supra, at
1189. Cf. Saucier v. Katz, 533 U. S. 194, 216, n. 6 (2001)
(GINSBURG, J., concurring in judgment) (“ ‘[I]n close cases,
a jury does not automatically get to second-guess these life
and death decisions, even though a plaintiff has an expert
and a plausible claim that the situation could better have
been handled differently’ ” (quoting Roy v. Inhabitants of
Lewiston, 42 F. 3d 691, 695 (CA1 1994))). Considering the
specific situation confronting Reynolds and Holder, they
had sufficient reason to believe that their conduct was
justified.
   Finally, to the extent that a “robust consensus of cases
of persuasive authority” could itself clearly establish the
federal right respondent alleges, al-Kidd, 563 U. S., at ___
(slip op., at 10), no such consensus exists here. If any-
thing, the opposite may be true. See, e.g., Bates v. Ches-
terfield County, 216 F. 3d 367, 372 (CA4 2000)
                 Cite as: 575 U. S. ____ (2015)           17

                     Opinion of the Court

(“Knowledge of a person’s disability simply cannot fore-
close officers from protecting themselves, the disabled
person, and the general public”); Sanders v. Minneapolis,
474 F. 3d 523, 527 (CA8 2007) (following Bates, supra);
Menuel v. Atlanta, 25 F. 3d 990 (CA11 1994) (upholding
use of deadly force to try to apprehend a mentally ill man
who had a knife and was hiding behind a door).
  In sum, we hold that qualified immunity applies be-
cause these officers had no “fair and clear warning of what
the Constitution requires.” al-Kidd, supra, at ___ (KEN-
NEDY, J., concurring) (slip op., at 3). Because the qualified
immunity analysis is straightforward, we need not decide
whether the Constitution was violated by the officers’
failure to accommodate Sheehan’s illness.
                      *     *    *
  For these reasons, the first question presented is dis-
missed as improvidently granted. On the second question,
we reverse the judgment of the Ninth Circuit. The case is
remanded for further proceedings consistent with this
opinion.
                                          It is so ordered.

  JUSTICE BREYER took no part in the consideration or
decision of this case.
                 Cite as: 575 U. S. ____ (2015)           1

                     Opinion of SCALIA, J.

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 13–1412
                         _________________


       CITY AND COUNTY OF SAN FRANCISCO, 

         CALIFORNIA, ET AL., PETITIONERS v.

                TERESA SHEEHAN

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE NINTH CIRCUIT

                        [May 18, 2015] 


  JUSTICE SCALIA, with whom JUSTICE KAGAN joins,
concurring in part and dissenting in part.
  The first question presented (QP) in the petition for
certiorari was “Whether Title II of the Americans with
Disabilities Act [(ADA)] requires law enforcement officers
to provide accommodations to an armed, violent, and
mentally ill suspect in the course of bringing the suspect
into custody.” Pet. for Cert. i. The petition assured us
(quite accurately), and devoted a section of its argument to
the point, that “The Circuits Are In Conflict On This
Question.” Id., at 18. And petitioners faulted the Ninth
Circuit for “holding that the ADA’s reasonable accommo-
dation requirement applies to officers facing violent cir-
cumstances,” a conclusion that was “in direct conflict with
the categorical prohibition on such claims adopted by the
Fifth and Sixth Circuits.” Ibid. Petitioners had expressly
advocated for the Fifth and Sixth Circuits’ position in the
Court of Appeals. See Appellees’ Answering Brief in No.
11–16401 (CA9), pp. 35–37 (“[T]he ADA does not apply to
police officers’ responses to violent individuals who happen
to be mentally ill, where officers have not yet brought the
violent situation under control”).
  Imagine our surprise, then, when the petitioners’ prin-
cipal brief, reply brief, and oral argument had nary a word
2          CITY AND COUNTY OF SAN FRANCISCO
                            v. SHEEHAN
        SCALIA, J., concurring
                        Opinion inof
                                   part and,dissenting
                                     SCALIA J.         in part

to say about that subject. Instead, petitioners bluntly
announced in their principal brief that they “do not assert
that the actions of individual police officers [in arresting
violent and armed disabled persons] are never subject to
scrutiny under Title II,” and proclaimed that “[t]he only
ADA issue here is what Title II requires of individual
officers who are facing an armed and dangerous suspect.”
Brief for Petitioners 34 (emphasis added). In other words,
the issue is not (as the petition had asserted) whether Title
II applies to arrests of violent, mentally ill individuals, but
rather how it applies under the circumstances of this case,
where the plaintiff threatened officers with a weapon. We
were thus deprived of the opportunity to consider, and
settle, a controverted question of law that has divided the
Circuits, and were invited instead to decide an ADA ques-
tion that has relevance only if we assume the Ninth Cir-
cuit correctly resolved the antecedent, unargued question
on which we granted certiorari. The Court is correct to
dismiss the first QP as improvidently granted.
   Why, one might ask, would a petitioner take a position
on a Circuit split that it had no intention of arguing, or at
least was so little keen to argue that it cast the argument
aside uninvited? The answer is simple. Petitioners in-
cluded that issue to induce us to grant certiorari. As the
Court rightly observes, there are numerous reasons why
we would not have agreed to hear petitioners’ first QP if
their petition for certiorari presented it in the same form
that it was argued on the merits. See ante, at 7–10. But it
is also true that there was little chance that we would
have taken this case to decide only the second, fact-bound
QP—that is, whether the individual petitioners are en-
titled to qualified immunity on respondent’s Fourth
Amendment claim.
   This Court’s Rule 10, entitled “Considerations Govern-
ing Review on Certiorari,” says that certiorari will be
granted “only for compelling reasons,” which include the
                     Cite as: 575 U. S. ____ (2015)                     3

          SCALIA, J., concurring
                          Opinioninof
                                    part and,dissenting
                                      SCALIA J.         in part

existence of conflicting decisions on issues of law among
federal courts of appeals, among state courts of last resort,
or between federal courts of appeals and state courts of
last resort. The Rule concludes: “A petition for a writ of
certiorari is rarely granted when the asserted error con-
sists of erroneous factual findings or the misapplication of
a properly stated rule of law.” The second QP implicates,
at most, the latter. It is unlikely that we would have
granted certiorari on that question alone.
   But (and here is what lies beneath the present case)
when we do grant certiorari on a question for which there
is a “compelling reason” for our review, we often also grant
certiorari on attendant questions that are not inde-
pendently “certworthy,” but that are sufficiently connected
to the ultimate disposition of the case that the efficient
administration of justice supports their consideration. In
other words, by promising argument on the Circuit conflict
that their first question presented, petitioners got us to
grant certiorari not only on the first question but also on
the second.
   I would not reward such bait-and-switch tactics by
proceeding to decide the independently “uncertworthy”
second question. And make no mistake about it: Today’s
judgment is a reward. It gives the individual petitioners
all that they seek, and spares San Francisco the signifi-
cant expense of defending the suit, and satisfying any
judgment, against the individual petitioners.* I would not
encourage future litigants to seek review premised on
arguments they never plan to press, secure in the
knowledge that once they find a toehold on this Court’s
docket, we will consider whatever workaday arguments
——————
   * San Francisco will still be subject to liability under the ADA if the
trial court determines that the facts demanded accommodation. The
Court of Appeals vacated the District Court’s judgment that the ADA
was inapplicable to police arrests of violent and armed disabled per-
sons, and remanded for the accommodation determination.
4          CITY AND COUNTY OF SAN FRANCISCO
                            v. SHEEHAN
        SCALIA, J., concurring
                        Opinion inof
                                   part and,dissenting
                                     SCALIA J.         in part

they choose to present in their merits briefs.
   There is no injustice in my vote to dismiss both ques-
tions as improvidently granted. To be sure, ex post—after
the Court has improvidently decided the uncertworthy
question—it appears that refusal to reverse the judgment
below would have left a wrong unrighted. Ex ante, how-
ever—before we considered and deliberated upon the second
QP but after petitioners’ principal brief made clear that
they would not address the Circuit conflict presented by
the first QP—we had no more assurance that this question
was decided incorrectly than we do for the thousands of
other uncertworthy questions we refuse to hear each
Term. Many of them have undoubtedly been decided
wrongly, but we are not, and for well over a century have
not been, a court of error correction. The fair course—the
just course—is to treat this now-nakedly uncertworthy
question the way we treat all others: by declining to decide
it. In fact, there is in this case an even greater reason to
decline: to avoid being snookered, and to deter future
snookering.
   Because I agree with the Court that “certiorari jurisdic-
tion exists to clarify the law,” ante, at 9 (emphasis added),
I would dismiss both questions presented as improvidently
granted.

```

---
