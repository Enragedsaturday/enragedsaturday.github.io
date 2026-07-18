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

## GROUP: content/cases/Henry v. United States (1959).md  (`case`, 5 assertions)

### content_page

```
---
title: "Henry v. United States (1959)"
type: case
citation: "361 U.S. 98 (1959)"
parallel_cite: "80 S. Ct. 168; 4 L. Ed. 2d 134"
neutral_cite: 1959 U.S. LEXIS 89
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1959
date_decided: 1959-11-23
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1959-11-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Henry v. United States (1959)"
  varies_by_point: false
  scope_note: "Good law. Probable cause for a warrantless arrest is measured by the facts known to the officer at the moment of arrest; outwardly innocent conduct does not supply it, and an arrest cannot be justified by what the ensuing search reveals. Year-suffixed filename to disambiguate from the reversed-party case United States v. Henry, 447 U.S. 264 (1980)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/105963/henry-v-united-states/"
  cluster_id: 105963
  opinion_id: 105963
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Anchor"
related: ["[[Brinegar v. United States]]", "[[Carroll v. United States]]", "[[Johnson v. United States]]", "[[Draper v. United States]]"]
aliases: ["Henry v. United States"]
tags: ["case", "fourth-amendment", "probable-cause", "warrantless-arrest", "seizure"]
holding: "Probable cause for a warrantless arrest is judged by the facts known at the moment of arrest; outwardly innocent conduct (mere package movement) does not supply it, and an arrest is not justified by what the subsequent search discloses."
lake:
  record_id: "Henry v. United States (1959)"
  status: verified
  projected_at: 2026-07-09
---

# Henry v. United States (1959)

*361 U.S. 98 (1959)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
FBI agents investigating the theft of whisky from an interstate shipment had a vague tip implicating Henry's companion, Pierotti. Over a period of surveillance the agents watched the two men drive to an alley in a residential section, load cartons into a car, drive off, return, and load more cartons. The agents stopped the car, and only afterward — looking through the open door — saw cartons bearing interstate shipping labels, which they then searched and seized. Henry was convicted of unlawful possession of stolen goods and moved to suppress the cartons as the fruit of an arrest without probable cause.

## Issue
At what point was Henry arrested, and whether the facts known to the agents at that moment amounted to probable cause for a warrantless arrest.

## Rule
Probable cause is measured at the moment of the seizure by the facts then known. "Probable cause exists if the facts and circumstances known to the officer warrant a prudent man in believing that the offense has been committed." — 361 U.S. at 102. ^pin-102

The arrest occurred when the car was stopped, and probable cause is judged as of that moment — not by what the later search turned up: "When the officers interrupted the two men and restricted their liberty of movement, the arrest, for purposes of this case, was complete. It is, therefore, necessary to determine whether at or before that time they had reasonable cause to believe that a crime had been committed." — [*Id.* at 103](https://www.courtlistener.com/opinion/105963/henry-v-united-states/#:~:text=When%20the%20officers%20interrupted%20the). ^pin-103

"[A]n arrest is not justified by what the subsequent search discloses. Under our system suspicion is not enough for an officer to lay hands on a citizen." — *Id.* at 104. ^pin-104

## Application
Measured at the moment the car was stopped, the agents had only outwardly innocent conduct to go on: "Riding in the car, stopping in an alley, picking up packages, driving away — these were all acts that were outwardly innocent." — *Id.* at 103. ^pin-103b

The tip about Pierotti was too vague to support even a warrant, Henry had not previously been suspected, and the cartons gave no outward sign of containing contraband — "The fact that packages have been stolen does not make every man who carries a package subject to arrest nor the package subject to seizure." — [*Id.* at 104](https://www.courtlistener.com/opinion/105963/henry-v-united-states/#:~:text=The%20fact%20that%20packages%20have). ^pin-104b

Because contraband was identified only after the arrest, it could not supply the probable cause the arrest required, and the evidence had to be suppressed.

## Conclusion
The arrest was complete when the car was stopped, probable cause did not exist at that moment, and the seized cartons were the fruit of an unlawful arrest. The conviction was reversed. Probable cause must precede the seizure and rest on more than outwardly innocent activity.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Henry*'s moment-of-arrest, facts-then-known rule for probable cause remains foundational and is applied in the totality-of-circumstances analyses of [[Brinegar v. United States]], [[Draper v. United States]], and later cases such as [[Maryland v. Pringle]] and [[Devenpeck v. Alford]].
- *Disambiguation:* distinct from the reversed-party case *[[United States v. Henry]]*, 447 U.S. 264 (1980) (Sixth Amendment, deliberate elicitation by a jailhouse informant); bare `[[Henry v. United States]]` resolves here via alias.

## Appears on
- [[Probable Cause]] — *Anchor*

## Sources
- *Henry v. United States*, 361 U.S. 98 (1959) — https://www.courtlistener.com/opinion/105963/henry-v-united-states/ — pinpoints: 102, 103, 104.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "103babbae1dd82c7", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "361 U.S. 98 (1959)", "court": "U.S. Supreme Court", "neutral_cite": "1959 U.S. LEXIS 89", "official_citation_present": true, "parallel_cite": "80 S. Ct. 168; 4 L. Ed. 2d 134", "title": "Henry v. United States (1959)", "year": "1959"}}
{"assertion_id": "6d0efb297c2084fb", "dimension": "support", "kind": "home_role", "locator": {"home": "Probable Cause"}, "payload": {"home": "Probable Cause", "role": "Anchor", "title": "Henry v. United States (1959)"}}
{"assertion_id": "ecfc0bc4740104b0", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Probable cause for a warrantless arrest is judged by the facts known at the moment of arrest; outwardly innocent conduct (mere package movement) does not supply it, and an arrest is not justified by what the subsequent search discloses.", "title": "Henry v. United States (1959)"}}
{"assertion_id": "2be7bdd4240bdf25", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1959-11-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Henry v. United States (1959)", "field_i_validity": "good_law", "scope_note": "Good law. Probable cause for a warrantless arrest is measured by the facts known to the officer at the moment of arrest; outwardly innocent conduct does not supply it, and an arrest cannot be justified by what the ensuing search reveals. Year-suffixed filename to disambiguate from the reversed-party case United States v. Henry, 447 U.S. 264 (1980).", "title": "Henry v. United States (1959)", "varies_by_point": "false"}}
{"assertion_id": "f77873216e186f37", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Henry v. United States (1959)"}}
```

### lake record — Henry v. United States (1959)

```json
{
  "schema_version": "s2.v1",
  "record_id": "Henry v. United States (1959)",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Henry v. United States",
    "case_name_short": "Henry",
    "case_name_full": "Henry v. United States",
    "input_case_name": "Henry v. United States (1959)",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1959-11-23",
    "year": 1959,
    "docket": null,
    "cluster_id": 105963,
    "lead_opinion_id": 105963,
    "sibling_ids": [
      105963,
      9421885,
      9421886
    ],
    "absolute_url": "/opinion/105963/henry-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8946152,
        "score": 20,
        "case_name": "Ostheimer v. United States"
      },
      {
        "cluster_id": 8946189,
        "score": 20,
        "case_name": "Philco Corp. v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "361 U.S. 98",
      "volume": "361",
      "reporter": "U.S.",
      "page": "98",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "80 S. Ct. 168",
        "volume": "80",
        "reporter": "S. Ct.",
        "page": "168",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 L. Ed. 2d 134",
        "volume": "4",
        "reporter": "L. Ed. 2d",
        "page": "134",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1959 U.S. LEXIS 89",
        "volume": "1959",
        "reporter": "U.S. LEXIS",
        "page": "89",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "361 U.S. 98",
        "volume": "361",
        "reporter": "U.S.",
        "page": "98",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 S. Ct. 168",
        "volume": "80",
        "reporter": "S. Ct.",
        "page": "168",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 L. Ed. 2d 134",
        "volume": "4",
        "reporter": "L. Ed. 2d",
        "page": "134",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1959 U.S. LEXIS 89",
        "volume": "1959",
        "reporter": "U.S. LEXIS",
        "page": "89",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "361 U.S. 98",
    "official_selection": {
      "court_class": "scotus",
      "selected": "361 U.S. 98",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-102",
      "page": null,
      "quote": "--- # Henry v. United States (1959) *361 U.S. 98 (1959)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background FBI agents investigating the theft of whisky from an interstate shipment had a vague tip implicating Henry's companion, Pierotti. Over a period of surveillance the agents watched the two men drive to an alley in a residential section, load cartons into a car, drive off, return, and load more cartons. The agents stopped the car, and only afterward \u2014 looking through the open door \u2014 saw cartons bearing interstate shipping labels, which they then searched and seized. Henry was convicted of unlawful possession of stolen goods and moved to suppress the cartons as the fruit of an arrest without probable cause. ## Issue At what point was Henry arrested, and whether the facts known to the agents at that moment amounted to probable cause for a warrantless arrest. ## Rule Probable cause is measured at the moment of the seizure by the facts then known.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-103",
      "page": null,
      "quote": "When the officers interrupted the two men and restricted their liberty of movement, the arrest, for purposes of this case, was complete. It is, therefore, necessary to determine whether at or before that time they had reasonable cause to believe that a crime had been committed.",
      "star_marker": "103",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 10151,
      "fragment": "#:~:text=When%20the%20officers%20interrupted%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-104",
      "page": null,
      "quote": "[A]n arrest is not justified by what the subsequent search discloses. Under our system suspicion is not enough for an officer to lay hands on a citizen.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-103b",
      "page": null,
      "quote": "Riding in the car, stopping in an alley, picking up packages, driving away \u2014 these were all acts that were outwardly innocent.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-104b",
      "page": null,
      "quote": "The fact that packages have been stolen does not make every man who carries a package subject to arrest nor the package subject to seizure.",
      "star_marker": "104",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 11767,
      "fragment": "#:~:text=The%20fact%20that%20packages%20have",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1959-11-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Henry v. United States (1959)",
    "varies_by_point": false,
    "scope_note": "Good law. Probable cause for a warrantless arrest is measured by the facts known to the officer at the moment of arrest; outwardly innocent conduct does not supply it, and an arrest cannot be justified by what the ensuing search reveals. Year-suffixed filename to disambiguate from the reversed-party case United States v. Henry, 447 U.S. 264 (1980).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Kelm",
          "cluster_id": 890265,
          "cite": [
            "2013 MT 115",
            "370 Mont. 61",
            "300 P.3d 687",
            "2013 WL 1804265",
            "2013 Mont. LEXIS 142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Porter v. State",
          "cluster_id": 1759540,
          "cite": [
            "255 S.W.3d 234",
            "2008 WL 553648"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rodriguez, Gustavo",
          "cluster_id": 2939134,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ballman",
          "cluster_id": 1465159,
          "cite": [
            "157 S.W.3d 65",
            "2004 WL 2914999"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Glenn v. State",
          "cluster_id": 2433495,
          "cite": [
            "967 S.W.2d 467",
            "1998 WL 156968"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Terry v. Ohio",
          "cluster_id": 107729,
          "cite": [
            "20 L. Ed. 2d 889",
            "88 S. Ct. 1868",
            "392 U.S. 1",
            "1968 U.S. LEXIS 1345",
            "44 Ohio Op. 2d 383"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wong Sun v. United States",
          "cluster_id": 106515,
          "cite": [
            "9 L. Ed. 2d 441",
            "83 S. Ct. 407",
            "371 U.S. 471",
            "1963 U.S. LEXIS 2431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
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
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
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
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beck v. Ohio",
          "cluster_id": 106936,
          "cite": [
            "13 L. Ed. 2d 142",
            "85 S. Ct. 223",
            "379 U.S. 89",
            "1964 U.S. LEXIS 151",
            "3 Ohio Misc. 71",
            "31 Ohio Op. 2d 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
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
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sibron v. New York",
          "cluster_id": 107730,
          "cite": [
            "20 L. Ed. 2d 917",
            "88 S. Ct. 1889",
            "392 U.S. 40",
            "1968 U.S. LEXIS 1346",
            "44 Ohio Op. 2d 402"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
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
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
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
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dunaway v. New York",
          "cluster_id": 110096,
          "cite": [
            "60 L. Ed. 2d 824",
            "99 S. Ct. 2248",
            "442 U.S. 200",
            "1979 U.S. LEXIS 126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
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
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warden, Maryland Penitentiary v. Hayden",
          "cluster_id": 107465,
          "cite": [
            "18 L. Ed. 2d 782",
            "87 S. Ct. 1642",
            "387 U.S. 294",
            "1967 U.S. LEXIS 2753"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bumper v. North Carolina",
          "cluster_id": 107716,
          "cite": [
            "20 L. Ed. 2d 797",
            "88 S. Ct. 1788",
            "391 U.S. 543",
            "1968 U.S. LEXIS 1470",
            "46 Ohio Op. 2d 382"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sharpe",
          "cluster_id": 111378,
          "cite": [
            "84 L. Ed. 2d 605",
            "105 S. Ct. 1568",
            "470 U.S. 675",
            "1985 U.S. LEXIS 74",
            "53 U.S.L.W. 4346"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. De Bour",
          "cluster_id": 5682261,
          "cite": [
            "40 N.Y.2d 210",
            "386 N.Y.S.2d 375",
            "1976 N.Y. LEXIS 2873",
            "352 N.E.2d 562"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
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
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
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
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Summers",
          "cluster_id": 110534,
          "cite": [
            "69 L. Ed. 2d 340",
            "101 S. Ct. 2587",
            "452 U.S. 692",
            "1981 U.S. LEXIS 118",
            "49 U.S.L.W. 4776"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. United States",
          "cluster_id": 109860,
          "cite": [
            "56 L. Ed. 2d 168",
            "98 S. Ct. 1717",
            "436 U.S. 128",
            "1978 U.S. LEXIS 89"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
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
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCray v. Illinois",
          "cluster_id": 107394,
          "cite": [
            "18 L. Ed. 2d 62",
            "87 S. Ct. 1056",
            "386 U.S. 300",
            "1967 U.S. LEXIS 1983"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Abel v. United States",
          "cluster_id": 106021,
          "cite": [
            "4 L. Ed. 2d 668",
            "80 S. Ct. 683",
            "362 U.S. 217",
            "1960 U.S. LEXIS 1412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cantor",
          "cluster_id": 5681132,
          "cite": [
            "36 N.Y.2d 106",
            "324 N.E.2d 872",
            "365 N.Y.S.2d 509",
            "1975 N.Y. LEXIS 3100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vale v. Louisiana",
          "cluster_id": 108183,
          "cite": [
            "26 L. Ed. 2d 409",
            "90 S. Ct. 1969",
            "399 U.S. 30",
            "1970 U.S. LEXIS 18"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Montoya De Hernandez",
          "cluster_id": 111509,
          "cite": [
            "87 L. Ed. 2d 381",
            "105 S. Ct. 3304",
            "473 U.S. 531",
            "1985 U.S. LEXIS 120",
            "53 U.S.L.W. 5048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Henry v. United States (1959):lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(105963 OR 9421885 OR 9421886) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04NDM3ODI0MDAwMDAmcz0xODU2ODAwJnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28105963+OR+9421885+OR+9421886%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      },
      "lane2_top_cited": {
        "query": "cites:(105963 OR 9421885 OR 9421886)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zODcmcz0xNTE2NTcxJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28105963+OR+9421885+OR+9421886%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(105963 OR 9421885 OR 9421886)",
        "reviewed": 10,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 10,
        "triage_read": 0,
        "triage_snippet_classified": 10
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(105963 OR 9421885 OR 9421886)",
    "indexed_citing_opinions": 1330,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 105963,
        "count": 1259,
        "count_source": "search"
      },
      {
        "opinion_id": 9421885,
        "count": 107,
        "count_source": "search"
      },
      {
        "opinion_id": 9421886,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1968,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/henry-v-united-states-1959.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY5ODgyNTYmcz00ODAwNzQ0JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28105963+OR+9421885+OR+9421886%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 105963,
        "cited_id": 89833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105963,
        "cited_id": 100265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105963,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105963,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105963,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105963,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105963,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105963,
        "cited_id": 105820,
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
    "date_created": "2026-07-05T06:55:21Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:55:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:55:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:58:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:55:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Henry v. United States (1959)

```
<div>
<center><b><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U.S. 98</a></span> (1959)</b></center>
<center><h1>HENRY<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 17.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 20-21, 1959.</center>
<center>Decided November 23, 1959.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SEVENTH CIRCUIT.
<p><i>Edward J. Calihan, Jr.</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Kirby W. Patterson</i> argued the cause for the United States. With him on the brief were <i>Solicitor General Rankin, Assistant Attorney General Wilkey</i> and <i>Beatrice Rosenberg.</i></p>
<p>MR. JUSTICE DOUGLAS delivered the opinion of the Court.</p>
<p>Petitioner stands convicted of unlawfully possessing three cartons of radios valued at more than $100 which had been stolen from an interstate shipment. See <span class="citation no-link">18 U. S. C. § 659</span>. The issue in the case is whether there was probable cause for the arrest leading to the search that produced the evidence on which the conviction rests. A timely motion to suppress the evidence was made by <span class="star-pagination">*99</span> petitioner and overruled by the District Court; and the judgment of conviction was affirmed by the Court of Appeals on a divided vote. <span class="citation" data-id="9446431"><a href="/opinion/246196/united-states-v-john-patrick-henry-and-albert-rudolph-pierotti/" aria-description="Citation for case: United States v. John Patrick Henry and Albert Rudolph...">259 F. 2d 725</a></span>. The case is here on a petition for a writ of certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./359/904/">359 U. S. 904</a></span>.</p>
<p>There was a theft from an interstate shipment of whisky at a terminal in Chicago. The next day two FBI agents were in the neighborhood investigating it. They saw petitioner and one Pierotti walk across a street from a tavern and get into an automobile. The agents had been given, by the employer of Pierotti, information of an undisclosed nature "concerning the implication of the defendant Pierotti with interstate shipments." But, so far as the record shows, he never went so far as to tell the agents he suspected Pierotti of any such thefts. The agents followed the car and saw it enter an alley and stop. Petitioner got out of the car, entered a gangway leading to residential premises and returned in a few minutes with some cartons. He placed them in the car and he and Pierotti drove off. The agents were unable to follow the car. But later they found it parked at the same place near the tavern. Shortly they saw petitioner and Pierotti leave the tavern, get into the car, and drive off. The car stopped in the same alley as before; petitioner entered the same gangway and returned with more cartons. The agents observed this transaction from a distance of some 300 feet and could not determine the size, number or contents of the cartons. As the car drove off the agents followed it and finally, when they met it, waved it to a stop. As he got out of the car, petitioner was heard to say, "Hold it; it is the G's." This was followed by, "Tell him he [you] just picked me up." The agents searched the car, placed the cartons (which bore the name "Admiral" and were addressed to an out-of-state company) in their car, took the merchandise and petitioner and Pierotti to their office and held them for about two hours when the agents learned that the cartons contained <span class="star-pagination">*100</span> stolen radios. They then placed the men under formal arrest.</p>
<p>The statutory authority of FBI officers and agents to make felony arrests without a warrant is restricted to offenses committed "in their presence" or to instances where they have "reasonable grounds to believe that the person to be arrested has committed or is committing" a felony. <span class="citation no-link">18 U. S. C. § 3052</span>. The statute states the constitutional standard, for it is the command of the Fourth Amendment that no warrants for either searches or arrests shall issue except "upon probable cause, supported by oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</p>
<p>The requirement of probable cause has roots that are deep in our history. The general warrant,<sup>[1]</sup> in which the name of the person to be arrested was left blank, and the writs of assistance, against which James Otis inveighed,<sup>[2]</sup> both perpetuated the oppressive practice of allowing the police to arrest and search on suspicion. Police control took the place of judicial control, since no showing of "probable cause" before a magistrate was required. The Virginia Declaration of Rights, adopted June 12, 1776, rebelled against that practice:</p>
<blockquote>"That general warrants, whereby any officer or messenger may be commanded to search suspected places without evidence of a fact committed, or to seize any person or persons not named, or whose offence is not particularly described and supported by evidence, are grievous and oppressive, and ought not to be granted."</blockquote>
<p><span class="star-pagination">*101</span> The Maryland Declaration of Rights (1776), Art. XXIII, was equally emphatic:</p>
<blockquote>"That all warrants, without oath or affirmation, to search suspected places, or to seize any person or property, are grievous and oppressive; and all general warrantsto search suspected places, or to apprehend suspected persons, without naming or describing the place, or the person in specialare illegal, and ought not to be granted."</blockquote>
<p>And see North Carolina Declaration of Rights (1776), Art. XI; Pennsylvania Constitution (1776), Art. X; Massachusetts Constitution (1780), Pt. I, Art. XIV.</p>
<p>That philosophy later was reflected in the Fourth Amendment. And as the early American decisions both before<sup>[3]</sup> and immediately after<sup>[4]</sup> its adoption show, common rumor or report, suspicion, or even "strong reason to suspect"<sup>[5]</sup> was not adequate to support a warrant for arrest. And that principle has survived to this day. See <i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#593" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 593-595</a></span>; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-15</a></span>; <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#486" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 486</a></span>. Its high water was <i>Johnson</i> v. <i>United States, supra</i><i>,</i> where the smell of opium coming from a closed room was not enough to support an arrest and search without a warrant. It was against this background that two scholars recently wrote, "Arrest on mere suspicion collides violently with the basic human right of liberty."<sup>[6]</sup></p>
<p><span class="star-pagination">*102</span> Evidence required to establish guilt is not necessary. <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span>; <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span>. On the other hand, good faith on the part of the arresting officers is not enough. Probable cause exists if the facts and circumstances known to the officer warrant a prudent man in believing that the offense has been committed. <i>Stacey</i> v. <i>Emery,</i> <span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/#645" aria-description="Citation for case: Stacey v. Emery">97 U. S. 642, 645</a></span>. And see <i>Director General</i> v. <i>Kastenbaum,</i> <span class="citation" data-id="100265"><a href="/opinion/100265/director-general-of-railroads-v-kastenbaum/#28" aria-description="Citation for case: Director General of Railroads v. Kastenbaum">263 U. S. 25, 28</a></span>; <i>United States</i> v. <i>Di Re, supra,</i> at 592; <i>Giordenello</i> v. <i>United States, supra,</i> at 486. It is important, we think, that this requirement be strictly enforced, for the standard set by the Constitution protects both the officer and the citizen. If the officer acts with probable cause, he is protected even though it turns out that the citizen is innocent. <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 156</a></span>. And while a search without a warrant is, within limits, permissible if incident to a lawful arrest, if an arrest without a warrant is to support an incidental search, it must be made with probable cause. <i>Carroll</i> v. <i>United States, supra,</i> at 155-156. This immunity of officers cannot fairly be enlarged without jeopardizing the privacy or security of the citizen. We turn then to the question whether prudent men in the shoes of these officers (<i>Brinegar</i> v. <i>United States, supra,</i> at 175) would have seen enough to permit them to believe that petitioner was violating or had violated the law. We think not.</p>
<p><span class="star-pagination">*103</span> The prosecution conceded below, and adheres to the concession here,<sup>[7]</sup> that the arrest took place when the federal agents stopped the car. That is our view on the facts of this particular case. When the officers interrupted the two men and restricted their liberty of movement, the arrest, for purposes of this case, was complete. It is, therefore, necessary to determine whether at or before that time they had reasonable cause to believe that a crime had been committed. The fact that afterwards contraband was discovered is not enough. An arrest is not justified by what the subsequent search discloses, as <i>Johnson</i> v. <i>United States, supra</i><i>,</i> holds.</p>
<p>It is true that a federal crime had been committed at a terminal in the neighborhood, whisky having been stolen from an interstate shipment. Petitioner's friend, Pierotti, had been suspected of some implication in some interstate shipments, as we have said. But as this record stands, what those shipments were and the manner in which he was implicated remain unexplained and undefined. The rumor about him is therefore practically meaningless. On the record there was far from enough evidence against him to justify a magistrate in issuing a warrant. So far as the record shows, petitioner had not even been suspected of criminal activity prior to this time. Riding in the car, stopping in an alley, picking up packages, driving awaythese were all acts that were outwardly innocent. Their movements in the car had no mark of fleeing men or men acting furtively. The case might be different if the packages had been taken from a terminal or from an interstate trucking platform. But they were not. As we have said, the alley where the packages were picked up was in a residential section. <span class="star-pagination">*104</span> The fact that packages have been stolen does not make every man who carries a package subject to arrest nor the package subject to seizure. The police must have reasonable grounds to believe that the particular package carried by the citizen is contraband. Its shape and design might at times be adequate. The weight of it and the manner in which it is carried might at times be enough. But there was nothing to indicate that the cartons here in issue probably contained liquor. The fact that they contained other contraband appeared only some hours after the arrest. What transpired at or after the time the car was stopped by the officers is, as we have said, irrelevant to the narrow issue before us. To repeat, an arrest is not justified by what the subsequent search discloses. Under our system suspicion is not enough for an officer to lay hands on a citizen. It is better, so the Fourth Amendment teaches, that the guilty sometimes go free than that citizens be subject to easy arrest.</p>
<p>The fact that the suspects were in an automobile is not enough. <i>Carroll</i> v. <i>United States, supra</i><i>,</i> liberalized the rule governing searches when a moving vehicle is involved. But that decision merely relaxed the requirements for a warrant on grounds of practicality. It did not dispense with the need for probable cause.</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE BLACK concurs in the result.</p>
<p>MR. JUSTICE CLARK, whom THE CHIEF JUSTICE joins, dissenting.</p>
<p>The Court decides this case on the narrow ground that the arrest took place at the moment the Federal Bureau of Investigation agents stopped the car in which petitioner was riding and at that time probable cause for it did not exist. While the Government, unnecessarily it seems to me, conceded that the arrest was made at the <span class="star-pagination">*105</span> time the car was stopped, this Court is not bound by the Government's mistakes.<sup>[*]</sup></p>
<p>The record shows beyond dispute that the agents had received information from co-defendant Pierotti's employer implicating Pierotti with interstate shipments. The agents began a surveillance of petitioner and Pierotti after recognizing them as they came out of a bar. Later the agents observed them loading cartons into an automobile from a gangway up an alley in Chicago. The agents had been trailing them, and after it appeared that they had delivered the first load of cartons, the suspects returned to the same platform by a circuitous route through streets and alleys. The agents then saw petitioner load another set of cartons into the car and drive off with the same. A few minutes later the agents stopped the car, alighted from their own car, and approached the petitioner. As they did so, petitioner was overheard to say: "Hold it; it is the G's," and "Tell him he [you] just picked me up." Since the agents had actually seen the two suspects together for several hours, it was apparent to them that the statement was untrue. Upon being questioned, the defendants stated that they had borrowed the car from a friend. During the questioning and after petitioner had stepped out of the car one of the agents happened to look through the door of the car which petitioner had left open and saw three cartons stacked up inside which resembled those petitioner had just loaded into the car from the gangway. The agent saw that the cartons bore Admiral shipping labels and were addressed to a company in Cincinnati, Ohio. Upon further questioning, the agent was told that the cartons <span class="star-pagination">*106</span> were in the car when the defendants borrowed it. Knowing this to be untrue, the agents then searched the car, arrested petitioner and his companion, and seized the cartons.</p>
<p>The Court seems to say that the mere stopping of the car amounted to an arrest of the petitioner. I cannot agree. The suspicious activities of the petitioner during the somewhat prolonged surveillance by the agents warranted the stopping of the car. The sighting of the cartons with their interstate labels in the car gave the agents reasonable ground to believe that a crime was in the course of its commission in their very presence. The search of the car and the subsequent arrest were therefore lawful and the motion to suppress was properly overruled.</p>
<p>In my view, the time at which the agents were required to have reasonable grounds to believe that petitioner was committing a felony was when they began the search of the automobile, which was after they had seen the cartons with interstate labels in the car. The earlier events certainly disclosed ample grounds to justify the following of the car, the subsequent stopping thereof, and the questioning of petitioner by the agents. This interrogation, together with the sighting of the cartons and the labels, gave the agents indisputable probable cause for the search and arrest.</p>
<p>When an investigation proceeds to the point where an agent has reasonable grounds to believe that an offense is being committed in his presence, he is obligated to proceed to make such searches, seizures, and arrests as the circumstances require. It is only by such alertness that crime is discovered, interrupted, prevented, and punished. We should not place additional burdens on law enforcement agencies.</p>
<p>I would affirm the judgments on the rationale of <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949), and <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925).</p>
<h2>NOTES</h2>
<p>[1]  Declared illegal by the House of Commons in 1766. 16 Hansard, Parl. Hist. Eng. 207.</p>
<p>[2]  Quincy's Mass. Rep. 1761-1772, Appendix, p. 469.</p>
<p>[3]  <i>Frisbie</i> v. <i>Butler,</i> Kirby's Rep. (Conn.) 1785-1788, p. 213.</p>
<p>[4]  <i>Conner</i> v. <i>Commonwealth,</i> 3 Binn (Pa.) 38; <i>Grumon</i> v. <i>Raymond,</i> <span class="citation" data-id="6572959"><a href="/opinion/6693083/grumon-v-raymond/" aria-description="Citation for case: Grumon v. Raymond">1 Conn. 40</a></span>; <i>Commonwealth</i> v. <i>Dana,</i> 2 Met. (Mass.) 329.</p>
<p>[5]  <i>Conner</i> v. <i>Commonwealth, supra,</i> note 4, at 43.</p>
<p>[6]  Hogan and Snee, The McNabb-Mallory Rule: Its Rise, Rationale and Rescue, 47 Geo. L. J. 1, 22.
</p>
<p>Uniform Crime Reports for the United States, compiled by the Federal Bureau of Investigation (Vol. XXVIII, No. 1, Semiannual Bull., 1957), pp. 64, 65, shows 1956 <i>arrest</i> statistics for 1,025 cities in the United States, including 26 cities over 250,000 population and 458 cities under 10,000 population.</p>
<p>The report states that 111,274 were arrested on suspicion (but not in connection with any specific offense) and subsequently released without prosecution. This was at the rate of 280.4 per 100,000 inhabitants.</p>
<p>The grand total of persons arrestedboth for a specific offense (but excluding traffic offenses) and on suspicion aloneand released without being held for prosecution was 264,601. This was at the rate of 666.7 per 100,000 inhabitants.</p>
<p>[7]  An alternative theory that the arrest took place at a subsequent time was discussed by the Government only to make clear that it would press that position on the facts of another case now pending here, No. 52, <i>Rios</i> v. <i>United States.</i></p>
<p>[*]  It may be that the Government is doing some wishful thinking in regard to the relaxation of the standards incident to the "probable cause" requirement by making this a test case. We should not lend ourselves to such indulgence.</p>

</div>
```

---

## GROUP: content/cases/Hester v. United States.md  (`case`, 8 assertions)

### content_page

```
---
title: "Hester v. United States"
type: case
citation: "265 U.S. 57 (1924)"
parallel_cite: "44 S. Ct. 445; 68 L. Ed. 898"
neutral_cite: 1924 U.S. LEXIS 2577
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1924
date_decided: 1924-05-05
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1924-05-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hester v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/100413/hester-v-united-states/"
  cluster_id: 100413
  opinion_id: 100413
  identity_checked: true
homes:
  - page: "[[Open Fields]]"
    role: "Key — Anchor"
  - page: "[[Curtilage]]"
    role: "Key"
  - page: "[[Abandonment]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Abandonment]]"
    role: "Key — Progeny / Refinement"
related: ["[[Oliver v. United States]]", "[[United States v. Dunn]]", "[[California v. Greenwood]]", "[[Abel v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "open-fields", "curtilage", "abandonment"]
holding: "Origin of the open-fields doctrine — 4A protection of 'persons, houses, papers, and effects' does not extend to open fields; and a fleeing suspect who drops containers abandons any 4A interest in them."
lake:
  record_id: Hester v. United States
  status: verified
  projected_at: 2026-07-06
---

# Hester v. United States

*265 U.S. 57 (1924)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Revenue officers, acting on information, went toward the house of Hester's father, where Hester lived, and concealed themselves fifty to one hundred yards away. They saw Hester hand a bottle to one Henderson; when an alarm was given, both men fled and dropped containers — a jug and a bottle — which broke but retained whiskey the officers recognized as illicitly distilled moonshine. A jar of whiskey was also found outside the house. The officers had no warrant, and Hester argued the examination occurred on his father's land.

## Issue
Whether the warrantless observation and examination of containers a fleeing suspect discarded in a field outside the house violated the Fourth Amendment, where it was assumed the field belonged to the defendant's father.

## Rule
No. A fleeing suspect who throws away containers abandons any Fourth Amendment interest in them: "there was no seizure in the sense of the law when the officers examined the contents of each after it had been abandoned." — 265 U.S. at 58. ^pin-58

And Fourth Amendment protection does not reach open fields in any event: "the special protection accorded by the Fourth Amendment to the people in their 'persons, houses, papers, and effects,' is not extended to the open fields. The distinction between the latter and the house is as old as the common law." — *Id.* at 59. ^pin-59

## Application
Hester's and his associate's own acts — running and throwing away the jug and bottle — disclosed the containers, so the officers' examination of the abandoned vessels was no seizure. And even assuming the examination occurred on the father's land, that land was open field, not the house, so the special Fourth Amendment protection did not extend to it. The officers' testimony was therefore admissible.

## Conclusion
The judgment of conviction was affirmed. Discarded containers were abandoned, and open fields receive no Fourth Amendment protection.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The open-fields doctrine originating here was reaffirmed and elaborated in [[Oliver v. United States]] and [[United States v. Dunn]] (distinguishing the protected [[Curtilage|curtilage]] from unprotected open fields).

## Appears on
- [[Open Fields]] — *Key — Anchor*
- [[Curtilage]] — *Key*
- [[Abandonment]] — *Key — Progeny / Refinement*

## Sources
- *Hester v. United States*, 265 U.S. 57 (1924) — https://www.courtlistener.com/opinion/100413/hester-v-united-states/ — pinpoints: 58, 59.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "15fb128b6d39b31c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "265 U.S. 57 (1924)", "court": "U.S. Supreme Court", "neutral_cite": "1924 U.S. LEXIS 2577", "official_citation_present": true, "parallel_cite": "44 S. Ct. 445; 68 L. Ed. 898", "title": "Hester v. United States", "year": "1924"}}
{"assertion_id": "27cd21266e6d5829", "dimension": "support", "kind": "home_role", "locator": {"home": "Open Fields"}, "payload": {"home": "Open Fields", "role": "Key — Anchor", "title": "Hester v. United States"}}
{"assertion_id": "7a3b4b4e2e86e242", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Origin of the open-fields doctrine — 4A protection of 'persons, houses, papers, and effects' does not extend to open fields; and a fleeing suspect who drops containers abandons any 4A interest in them.", "title": "Hester v. United States"}}
{"assertion_id": "a70f80e2ccd8bba9", "dimension": "support", "kind": "home_role", "locator": {"home": "Curtilage"}, "payload": {"home": "Curtilage", "role": "Key", "title": "Hester v. United States"}}
{"assertion_id": "e2b05a4c94a3dcb5", "dimension": "support", "kind": "home_role", "locator": {"home": "Abandonment"}, "payload": {"home": "Abandonment", "role": "Key — Progeny / Refinement", "title": "Hester v. United States"}}
{"assertion_id": "f7697824aea707d1", "dimension": "support", "kind": "home_role", "locator": {"home": "Abandonment"}, "payload": {"home": "Abandonment", "role": "Key — Progeny / Refinement", "title": "Hester v. United States"}}
{"assertion_id": "3207a9c1be2ff00b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1924-05-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Hester v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Hester v. United States", "varies_by_point": "false"}}
{"assertion_id": "a5c8debc67647985", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Hester v. United States"}}
```

### lake record — Hester v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hester v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hester v. United States",
    "case_name_short": "Hester",
    "case_name_full": "Hester v. United States",
    "input_case_name": "Hester v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1924-05-05",
    "year": 1924,
    "docket": null,
    "cluster_id": 100413,
    "lead_opinion_id": 100413,
    "sibling_ids": [
      100413
    ],
    "absolute_url": "/opinion/100413/hester-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "265 U.S. 57",
      "volume": "265",
      "reporter": "U.S.",
      "page": "57",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "44 S. Ct. 445",
        "volume": "44",
        "reporter": "S. Ct.",
        "page": "445",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 L. Ed. 898",
        "volume": "68",
        "reporter": "L. Ed.",
        "page": "898",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1924 U.S. LEXIS 2577",
        "volume": "1924",
        "reporter": "U.S. LEXIS",
        "page": "2577",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "265 U.S. 57",
        "volume": "265",
        "reporter": "U.S.",
        "page": "57",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "44 S. Ct. 445",
        "volume": "44",
        "reporter": "S. Ct.",
        "page": "445",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 L. Ed. 898",
        "volume": "68",
        "reporter": "L. Ed.",
        "page": "898",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1924 U.S. LEXIS 2577",
        "volume": "1924",
        "reporter": "U.S. LEXIS",
        "page": "2577",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "265 U.S. 57",
    "official_selection": {
      "court_class": "scotus",
      "selected": "265 U.S. 57",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-58",
      "page": null,
      "quote": "--- # Hester v. United States *265 U.S. 57 (1924)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Revenue officers, acting on information, went toward the house of Hester's father, where Hester lived, and concealed themselves fifty to one hundred yards away. They saw Hester hand a bottle to one Henderson; when an alarm was given, both men fled and dropped containers \u2014 a jug and a bottle \u2014 which broke but retained whiskey the officers recognized as illicitly distilled moonshine. A jar of whiskey was also found outside the house. The officers had no warrant, and Hester argued the examination occurred on his father's land. ## Issue Whether the warrantless observation and examination of containers a fleeing suspect discarded in a field outside the house violated the Fourth Amendment, where it was assumed the field belonged to the defendant's father. ## Rule No. A fleeing suspect who throws away containers abandons any Fourth Amendment interest in them:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-59",
      "page": null,
      "quote": "the special protection accorded by the Fourth Amendment to the people in their 'persons, houses, papers, and effects,' is not extended to the open fields. The distinction between the latter and the house is as old as the common law.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1924-05-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hester v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Missouri, Plaintiff/Respondent v. Timothy A. Pierce",
          "cluster_id": 4254135,
          "cite": [
            "504 S.W.3d 766",
            "2016 Mo. App. LEXIS 864"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Milewski",
          "cluster_id": 3170756,
          "cite": [
            "194 So. 3d 376",
            "2016 Fla. App. LEXIS 701",
            "2016 WL 231314"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Piedad Barajas-Avalos, AKA Opinion Piedad Barajas-Avaslos",
          "cluster_id": 785295,
          "cite": [
            "359 F.3d 1204",
            "2004 U.S. App. LEXIS 4569",
            "2004 D.A.R. 3084"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Paxton",
          "cluster_id": 4020585,
          "cite": [
            "615 N.E.2d 1086",
            "83 Ohio App. 3d 818",
            "1992 Ohio App. LEXIS 5867"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kirchoff",
          "cluster_id": 2202269,
          "cite": [
            "587 A.2d 988",
            "156 Vt. 1",
            "1991 Vt. LEXIS 8"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Smith v. Ohio",
          "cluster_id": 112392,
          "cite": [
            "108 L. Ed. 2d 464",
            "110 S. Ct. 1288",
            "494 U.S. 541",
            "1990 U.S. LEXIS 1198"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Fuesting",
          "cluster_id": 504906,
          "cite": [
            "845 F.2d 664",
            "25 Fed. R. Serv. 680",
            "1988 U.S. App. LEXIS 5392",
            "1988 WL 35946"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Leal v. State",
          "cluster_id": 5244283,
          "cite": [
            "736 S.W.2d 903"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane1_negative"
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
        "journal_ref": "Hester v. United States:lane2_top_cited"
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
        "journal_ref": "Hester v. United States:lane2_top_cited"
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
        "journal_ref": "Hester v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carroll v. United States",
          "cluster_id": 100567,
          "cite": [
            "267 U.S. 132",
            "45 S. Ct. 280",
            "69 L. Ed. 543",
            "1925 U.S. LEXIS 361"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane2_top_cited"
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
        "journal_ref": "Hester v. United States:lane2_top_cited"
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
        "journal_ref": "Hester v. United States:lane2_top_cited"
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
        "journal_ref": "Hester v. United States:lane2_top_cited"
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
        "journal_ref": "Hester v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Olmstead v. United States",
          "cluster_id": 101320,
          "cite": [
            "277 U.S. 438",
            "48 S. Ct. 564",
            "72 L. Ed. 944",
            "1928 U.S. LEXIS 694",
            "66 A.L.R. 376"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane2_top_cited"
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
        "journal_ref": "Hester v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. United States",
          "cluster_id": 107625,
          "cite": [
            "19 L. Ed. 2d 1067",
            "88 S. Ct. 992",
            "390 U.S. 234",
            "1968 U.S. LEXIS 2283"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane2_top_cited"
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
        "journal_ref": "Hester v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Abel v. United States",
          "cluster_id": 106021,
          "cite": [
            "4 L. Ed. 2d 668",
            "80 S. Ct. 683",
            "362 U.S. 217",
            "1960 U.S. LEXIS 1412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brower Ex Rel. Estate of Caldwell v. County of Inyo",
          "cluster_id": 112218,
          "cite": [
            "103 L. Ed. 2d 628",
            "109 S. Ct. 1378",
            "489 U.S. 593",
            "1989 U.S. LEXIS 1569",
            "57 U.S.L.W. 4321"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Tyler",
          "cluster_id": 109874,
          "cite": [
            "56 L. Ed. 2d 486",
            "98 S. Ct. 1942",
            "436 U.S. 499",
            "1978 U.S. LEXIS 97"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Santana",
          "cluster_id": 109504,
          "cite": [
            "49 L. Ed. 2d 300",
            "96 S. Ct. 2406",
            "427 U.S. 38",
            "1976 U.S. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dunn",
          "cluster_id": 111833,
          "cite": [
            "94 L. Ed. 2d 326",
            "107 S. Ct. 1134",
            "480 U.S. 294",
            "1987 U.S. LEXIS 1057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Silverman v. United States",
          "cluster_id": 106187,
          "cite": [
            "5 L. Ed. 2d 734",
            "81 S. Ct. 679",
            "365 U.S. 505",
            "1961 U.S. LEXIS 1605",
            "97 A.L.R. 2d 1277"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 622304,
          "cite": [
            "181 L. Ed. 2d 911",
            "132 S. Ct. 945",
            "565 U.S. 400",
            "2012 U.S. LEXIS 1063"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lopez v. United States",
          "cluster_id": 106622,
          "cite": [
            "10 L. Ed. 2d 462",
            "83 S. Ct. 1381",
            "373 U.S. 427",
            "1963 U.S. LEXIS 2618"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knotts",
          "cluster_id": 110882,
          "cite": [
            "75 L. Ed. 2d 55",
            "103 S. Ct. 1081",
            "460 U.S. 276",
            "1983 U.S. LEXIS 135",
            "51 U.S.L.W. 4232"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donovan v. Dewey",
          "cluster_id": 110530,
          "cite": [
            "69 L. Ed. 2d 262",
            "101 S. Ct. 2534",
            "452 U.S. 594",
            "1980 U.S. LEXIS 58"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "G. M. Leasing Corp. v. United States",
          "cluster_id": 109579,
          "cite": [
            "50 L. Ed. 2d 530",
            "97 S. Ct. 619",
            "429 U.S. 338",
            "1977 U.S. LEXIS 33",
            "39 A.F.T.R.2d (RIA) 475"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "On Lee v. United States",
          "cluster_id": 105021,
          "cite": [
            "96 L. Ed. 2d 1270",
            "72 S. Ct. 967",
            "343 U.S. 747",
            "1952 U.S. LEXIS 2794"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rios v. United States",
          "cluster_id": 106108,
          "cite": [
            "4 L. Ed. 2d 1688",
            "80 S. Ct. 1431",
            "364 U.S. 253",
            "1960 U.S. LEXIS 766"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hester v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(100413) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MzM4NjU2MDAwMDAmcz00Nzk0MzMmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28100413%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(100413)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDcmcz0xMTIzOTImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28100413%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(100413)",
        "reviewed": 14,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 14,
        "triage_read": 0,
        "triage_snippet_classified": 14
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(100413)",
    "indexed_citing_opinions": 799,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 100413,
        "count": 799,
        "count_source": "search"
      }
    ],
    "citation_count": 1214,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hester-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc1ODEyNzUmcz0xMDYyODg5NSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28100413%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LRU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T07:03:00Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:03:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:03:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:06:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:03:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hester v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b101-13">
  Mr. Justice Holmes
 </author>
<p id="ABj">
  delivered the opinion of the Court.
 </p>
<p id="b101-14">
  The plaintiff in error, Hester, was convicted of concealing distilled spirits &amp;c. under Rev. Stats., § 3296. The case is brought here directly from the District Court on the single ground that by refusing to exclude the testimony of two witnesses and to direct a verdict for the defendant, the plaintiff in error, the Court violated his
  <span citation-index="1" class="star-pagination" label="58"> 
   *58
   </span>
  rights under the Fourth and Fifth Amendments of the Constitution of the United States.
 </p>
<p id="b102-6">
  The witnesses wh©se testimony is objected to were revenue officers. In consequence of information they went toward the house of Hester’s-father, where the plaintiff in error lived, and as they approached saw one Henderson drive near to the house. They concealed themselves from fifty to one hundred yards away and saw Hester come out and hand Henderson a quart bottle. An alarm was given. Hester went to a car standing near, took a gallon jug from it and he and Henderson ran. One of the officers pursued, and fired a pistol. Hester dropped his jug, which broke but kept about a quart of its contents. Henderson threw away his bottle also. The jug and bottle both contained what the officers, being experts, recognized as moonshine whiskey, that is whiskey illicitly distilled; said to be easily recognizable. The other officer entered the house, but being told there was no whiskey there left it, but found outside a jar that had been thrown out and broken and that also contained whiskey. While the officers were there other cars stopped at the house but were spoken to by Hester’s father and drove off. The officers had no warrant for search or arrest, and it is contended that this made their evidence inadmissible, it being assumed, on the strength of the pursuing officer’s saying that he supposed they were on Hester’s land, that such was the fact. It is obvious that even if there had been a trespass, the above testimony was not obtained by an illegal search or seizure. The defendant’s own acts, and those of his associates, disclosed the jug, the jar and the bottle — and there was no seizure in the sense of the law when the officers examined the contents of each after it had been abandoned. This evidence was not obtained by the entry into the house and it is immaterial to discuss that. The suggestion that the defendant was compelled to give evidence against himself
  <span citation-index="1" class="star-pagination" label="59"> 
   *59
   </span>
  does not require an answer. The only shadow of a ground for bringing up the case is drawn from the hypothesis that the examination of the vessels took place upon Hester’s father’s land. As to that, it is enough to say that, apart from the justification, the special protection accorded by the Fourth Amendment to the people in their
  <em>
   “
  </em>
  persons, houses, papers, and effects,” is not extended to the open fields. The distinction between the latter and the house is as old as the common law. 4 Bl. Comm. 223, 225, 226.
 </p>
<p id="b103-4">
<em>
   Judgment affirmed.
  </em>
</p>
</opinion>
```

---

## GROUP: content/cases/Hiibel v. Sixth Judicial Dist. Court.md  (`case`, 6 assertions)

### content_page

```
---
title: "Hiibel v. Sixth Judicial Dist. Court"
type: case
citation: ""
parallel_cite: "542 U.S. 177; 124 S. Ct. 2451; 159 L. Ed. 2d 292; 17 Fla. L. Weekly Fed. S 406; 72 U.S.L.W. 4509"
neutral_cite: 2004 U.S. LEXIS 4385
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-06-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-06-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hiibel v. Sixth Judicial Dist. Court
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/"
  cluster_id: 136990
  opinion_id: 136990
  identity_checked: true
homes:
  - page: "[[Stop-and-Identify]]"
    role: "Key — Anchor"
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Key-on (during a valid Terry stop)"
related: ["[[Terry v. Ohio]]", "[[Berkemer v. McCarty]]", "[[Brown v. Texas]]"]
aliases: ["Hiibel v. Sixth Judicial District Court of Nevada", "Hiibel v. Sixth Judicial District Court of Nevada, Humboldt County"]
tags: ["case", "fourth-amendment", "terry-stop", "stop-and-identify", "reasonable-suspicion"]
holding: "A state stop-and-identify law compelling a suspect to give his name during a valid *Terry* stop is consistent with the Fourth Amendment."
lake:
  record_id: Hiibel v. Sixth Judicial Dist. Court
  status: verified
  projected_at: 2026-07-06
---

# Hiibel v. Sixth Judicial Dist. Court

*542 U.S. 177 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A deputy investigating a reported domestic assault found Hiibel standing by a truck and, during a valid *[[Terry v. Ohio|Terry]]* stop, asked him eleven times to identify himself. Hiibel refused each time and was arrested and convicted under a Nevada "stop and identify" statute requiring a person detained on reasonable suspicion to disclose his name.

## Issue
Whether a state stop-and-identify law that compels a suspect to disclose his name during a valid *[[Terry v. Ohio|Terry]]* stop is consistent with the Fourth Amendment.

## Rule
Yes. "Obtaining a suspect's name in the course of a Terry stop serves important government interests." — 542 U.S. at 186. ^pin-186

The Court held that "[t]he principles of Terry permit a State to require a suspect to disclose his name in the course of a Terry stop." — *Id.* at 187. ^pin-187

Because the request for identity bears an immediate relation to the purpose and demands of the stop, "[a] state law requiring a suspect to disclose his name in the course of a valid Terry stop is consistent with Fourth Amendment prohibitions against unreasonable searches and seizures." — *Id.* at 188. ^pin-188

## Application
The deputy's request for Hiibel's name during a *[[Terry v. Ohio|Terry]]* stop based on reasonable suspicion of a domestic assault was a commonsense inquiry reasonably related to the circumstances justifying the stop — investigating the dispute and assessing safety. The Nevada statute did not change the stop's duration or location, so requiring Hiibel to give his name, on pain of arrest, did not contravene the Fourth Amendment.

## Conclusion
Hiibel's conviction did not violate the Fourth Amendment; the judgment was affirmed. A state may require disclosure of one's name during a valid *[[Terry v. Ohio|Terry]]* stop.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hiibel* builds on [[Terry v. Ohio]], confirming that identity questions are a routine and permissible part of a *[[Terry v. Ohio|Terry]]* stop and that a state may attach a criminal sanction to a refusal, so long as the request is reasonably related to the circumstances justifying the stop.

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Key — Progeny / Refinement*

## Sources
- *Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.*, 542 U.S. 177 (2004) — https://www.courtlistener.com/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/ — pinpoints: 186, 187, 188.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c1f38a8cae43ab7d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2004 U.S. LEXIS 4385", "official_citation_present": false, "parallel_cite": "542 U.S. 177; 124 S. Ct. 2451; 159 L. Ed. 2d 292; 17 Fla. L. Weekly Fed. S 406; 72 U.S.L.W. 4509", "title": "Hiibel v. Sixth Judicial Dist. Court", "year": "2004"}}
{"assertion_id": "01552802bad599e8", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Key-on (during a valid Terry stop)", "title": "Hiibel v. Sixth Judicial Dist. Court"}}
{"assertion_id": "7a3523404108456b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A state stop-and-identify law compelling a suspect to give his name during a valid *Terry* stop is consistent with the Fourth Amendment.", "title": "Hiibel v. Sixth Judicial Dist. Court"}}
{"assertion_id": "ba284213e55a2eb2", "dimension": "support", "kind": "home_role", "locator": {"home": "Stop-and-Identify"}, "payload": {"home": "Stop-and-Identify", "role": "Key — Anchor", "title": "Hiibel v. Sixth Judicial Dist. Court"}}
{"assertion_id": "a8877346246af4c7", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2004-06-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Hiibel v. Sixth Judicial Dist. Court", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Hiibel v. Sixth Judicial Dist. Court", "varies_by_point": "false"}}
{"assertion_id": "a969fb61f6ce74c4", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Hiibel v. Sixth Judicial Dist. Court"}}
```

### lake record — Hiibel v. Sixth Judicial Dist. Court

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hiibel v. Sixth Judicial Dist. Court",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.",
    "case_name_short": "Hiibel",
    "case_name_full": "HIIBEL v. SIXTH JUDICIAL DISTRICT COURT OF NEVADA, HUMBOLDT COUNTY, Et Al.",
    "input_case_name": "Hiibel v. Sixth Judicial Dist. Court",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-06-21",
    "year": 2004,
    "docket": null,
    "cluster_id": 136990,
    "lead_opinion_id": 136990,
    "sibling_ids": [
      136990,
      9434645,
      9434646,
      9434647
    ],
    "absolute_url": "/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/",
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
        "cite": "542 U.S. 177",
        "volume": "542",
        "reporter": "U.S.",
        "page": "177",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 2451",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2451",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "159 L. Ed. 2d 292",
        "volume": "159",
        "reporter": "L. Ed. 2d",
        "page": "292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fla. L. Weekly Fed. S 406",
        "volume": "17",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "406",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 U.S.L.W. 4509",
        "volume": "72",
        "reporter": "U.S.L.W.",
        "page": "4509",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 4385",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "4385",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "542 U.S. 177",
        "volume": "542",
        "reporter": "U.S.",
        "page": "177",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 2451",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2451",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "159 L. Ed. 2d 292",
        "volume": "159",
        "reporter": "L. Ed. 2d",
        "page": "292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 4385",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "4385",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fla. L. Weekly Fed. S 406",
        "volume": "17",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "406",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 U.S.L.W. 4509",
        "volume": "72",
        "reporter": "U.S.L.W.",
        "page": "4509",
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
      "id": "pin-186",
      "page": null,
      "quote": "statute requiring a person detained on reasonable suspicion to disclose his name. ## Issue Whether a state stop-and-identify law that compels a suspect to disclose his name during a valid *Terry* stop is consistent with the Fourth Amendment. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-187",
      "page": null,
      "quote": "[t]he principles of Terry permit a State to require a suspect to disclose his name in the course of a Terry stop.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-188",
      "page": null,
      "quote": "[a] state law requiring a suspect to disclose his name in the course of a valid Terry stop is consistent with Fourth Amendment prohibitions against unreasonable searches and seizures.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-06-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hiibel v. Sixth Judicial Dist. Court",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Tanguay",
          "cluster_id": 4598184,
          "cite": [
            "918 F.3d 1"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Young",
          "cluster_id": 4460263,
          "cite": [
            "2018 Ohio 164",
            "104 N.E.3d 128"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Carlos Gonzalez v. Able Huerta",
          "cluster_id": 3216824,
          "cite": [
            "826 F.3d 854",
            "2016 U.S. App. LEXIS 11530",
            "2016 WL 3457258"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
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
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
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
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
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
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Prall v. City of Boston",
          "cluster_id": 8729956,
          "cite": [
            "985 F. Supp. 2d 115",
            "2013 WL 6076462",
            "2013 U.S. Dist. LEXIS 166128"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kareen Rasul Griffin",
          "cluster_id": 809546,
          "cite": [
            "696 F.3d 1354",
            "2012 WL 4496817",
            "2012 U.S. App. LEXIS 20543"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Davis v. Washington",
          "cluster_id": 145641,
          "cite": [
            "165 L. Ed. 2d 224",
            "126 S. Ct. 2266",
            "547 U.S. 813",
            "2006 U.S. LEXIS 4886"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
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
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Caballes",
          "cluster_id": 137742,
          "cite": [
            "160 L. Ed. 2d 842",
            "125 S. Ct. 834",
            "543 U.S. 405",
            "2005 U.S. LEXIS 769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Bryant",
          "cluster_id": 2959736,
          "cite": [
            "179 L. Ed. 2d 93",
            "131 S. Ct. 1143",
            "562 U.S. 344",
            "2011 U.S. LEXIS 1713"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Laurie Tsao v. Desert Palace, Inc.",
          "cluster_id": 810771,
          "cite": [
            "698 F.3d 1128",
            "2012 WL 5200336"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
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
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
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
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scroggins",
          "cluster_id": 71470,
          "cite": [
            "599 F.3d 433",
            "2010 U.S. App. LEXIS 4551",
            "2010 WL 724688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
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
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
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
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cady, Davy v. Sheahan, Michael",
          "cluster_id": 2999846,
          "cite": [
            "467 F.3d 1057",
            "2006 WL 3113670"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Woodard",
          "cluster_id": 2540788,
          "cite": [
            "341 S.W.3d 404",
            "2011 Tex. Crim. App. LEXIS 447",
            "2011 WL 1261320"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hosvaldo Lopez",
          "cluster_id": 797423,
          "cite": [
            "482 F.3d 1067",
            "2007 WL 725641",
            "2007 U.S. App. LEXIS 5709"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
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
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Center for Bio-Ethical Reform, Inc. v. Los Angeles County Sheriff Department",
          "cluster_id": 1235108,
          "cite": [
            "533 F.3d 780",
            "2008 U.S. App. LEXIS 13975",
            "2008 WL 2599683"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Kerwick, Stacie Michelle",
          "cluster_id": 2948618,
          "cite": [
            "393 S.W.3d 270",
            "2013 WL 690840",
            "2013 Tex. Crim. App. LEXIS 430"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
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
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morris v. Noe",
          "cluster_id": 623700,
          "cite": [
            "672 F.3d 1185",
            "2012 WL 604170",
            "2012 U.S. App. LEXIS 3927"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Arnold",
          "cluster_id": 797722,
          "cite": [
            "486 F.3d 177",
            "73 Fed. R. Serv. 583",
            "2007 U.S. App. LEXIS 11616",
            "2007 WL 1452230"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Waters v. B. Madson",
          "cluster_id": 4609057,
          "cite": [
            "921 F.3d 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillip Turner v. Driver",
          "cluster_id": 4349754,
          "cite": [
            "848 F.3d 678",
            "2017 WL 650186",
            "2017 U.S. App. LEXIS 2769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Cameron Kincade",
          "cluster_id": 787362,
          "cite": [
            "379 F.3d 813",
            "2004 U.S. App. LEXIS 17191",
            "2004 WL 1837840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Derrick L. Foster",
          "cluster_id": 787028,
          "cite": [
            "376 F.3d 577",
            "65 Fed. R. Serv. 1",
            "2004 U.S. App. LEXIS 15267",
            "2004 WL 1606725"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. City of New York",
          "cluster_id": 2828542,
          "cite": [
            "798 F.3d 94",
            "2015 U.S. App. LEXIS 14517",
            "2015 WL 4924395"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(136990 OR 9434645 OR 9434646 OR 9434647) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzEzNDUyODAwMDAwJnM9Mjk5MTYwNCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28136990+OR+9434645+OR+9434646+OR+9434647%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(136990 OR 9434645 OR 9434646 OR 9434647)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTMmcz0xNDI3ODc4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28136990+OR+9434645+OR+9434646+OR+9434647%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(136990 OR 9434645 OR 9434646 OR 9434647)",
        "reviewed": 26,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 26,
        "triage_read": 0,
        "triage_snippet_classified": 26
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(136990 OR 9434645 OR 9434646 OR 9434647)",
    "indexed_citing_opinions": 480,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 136990,
        "count": 392,
        "count_source": "search"
      },
      {
        "opinion_id": 9434645,
        "count": 95,
        "count_source": "search"
      },
      {
        "opinion_id": 9434646,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434647,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 890,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hiibel-v-sixth-judicial-dist-court.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0NjEyODUmcz05NDI4NDMyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28136990+OR+9434645+OR+9434646+OR+9434647%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 136990,
        "cited_id": 93149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 104912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108472,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108965,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 109432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110426,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 111378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 111382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 112123,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 112464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 118326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 127927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 134724,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 1087666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 2621305,
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
    "date_created": "2026-07-05T07:06:13Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:06:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:06:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:10:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:06:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hiibel v. Sixth Judicial Dist. Court

```
<div>
<center><b><span class="citation" data-id="9434645"><a href="/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/" aria-description="Citation for case: Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.">542 U.S. 177</a></span> (2004)</b></center>
<center><h1>HIIBEL<br>
v.<br>
SIXTH JUDICIAL DISTRICT COURT OF NEVADA, HUMBOLDT COUNTY, ET AL.</h1></center>
<center>No. 03-5554.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 22, 2004.</center>
<center>Decided June 21, 2004.</center>
CERTIORARI TO THE SUPREME COURT OF NEVADA.
<p><span class="star-pagination">*178</span> <span class="star-pagination">*179</span> KENNEDY, J., delivered the opinion of the Court, in which REHNQUIST, C. J., and O'CONNOR, SCALIA, and THOMAS, JJ., joined. STEVENS, J., filed a dissenting opinion, <i>post,</i> p. 191. BREYER, J., filed a dissenting opinion, in which SOUTER and GINSBURG, JJ., joined, <i>post,</i> p. 197.</p>
<p><i>Robert E. Dolan</i> argued the cause for petitioner. With him on the briefs were <i>James P. Logan, Jr.,</i> and <i>Harriet E. Cummings.</i></p>
<p><i>Conrad Hafen,</i> Senior Deputy Attorney General of Nevada, argued the cause for respondents. With him on the brief were <i>Brian Sandoval,</i> Attorney General, and <i>David Allison.</i></p>
<p><i>Sri Srinivasan</i> argued the cause for the United States as <i>amicus curiae</i> urging affirmance. With him on the brief were <i>Solicitor General Olson, Assistant Attorney General</i> <span class="star-pagination">*180</span> <i>Wray, Deputy Solicitor General Dreeben,</i> and <i>Joel M. Gershowitz.</i><sup>[*]</sup></p>
<p>JUSTICE KENNEDY delivered the opinion of the Court.</p>
<p>The petitioner was arrested and convicted for refusing to identify himself during a stop allowed by <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). He challenges his conviction under the Fourth and Fifth Amendments to the United States Constitution, applicable to the States through the Fourteenth Amendment.</p>
<p></p>
<h2>I</h2>
<p>The sheriff's department in Humboldt County, Nevada, received an afternoon telephone call reporting an assault. The caller reported seeing a man assault a woman in a red and silver GMC truck on Grass Valley Road. Deputy Sheriff Lee Dove was dispatched to investigate. When the officer arrived at the scene, he found the truck parked on the side of the road. A man was standing by the truck, and a young woman was sitting inside it. The officer observed skid marks in the gravel behind the vehicle, leading him to believe it had come to a sudden stop.</p>
<p>The officer approached the man and explained that he was investigating a report of a fight. The man appeared to be <span class="star-pagination">*181</span> intoxicated. The officer asked him if he had "any identification on [him]," which we understand as a request to produce a driver's license or some other form of written identification. The man refused and asked why the officer wanted to see identification. The officer responded that he was conducting an investigation and needed to see some identification. The unidentified man became agitated and insisted he had done nothing wrong. The officer explained that he wanted to find out who the man was and what he was doing there. After continued refusals to comply with the officer's request for identification, the man began to taunt the officer by placing his hands behind his back and telling the officer to arrest him and take him to jail. This routine kept up for several minutes: The officer asked for identification 11 times and was refused each time. After warning the man that he would be arrested if he continued to refuse to comply, the officer placed him under arrest.</p>
<p>We now know that the man arrested on Grass Valley Road is Larry Dudley Hiibel. Hiibel was charged with "willfully resist[ing], delay[ing] or obstruct[ing] a public officer in discharging or attempting to discharge any legal duty of his office" in violation of Nev. Rev. Stat. (NRS) § 199.280 (2003). The government reasoned that Hiibel had obstructed the officer in carrying out his duties under § 171.123, a Nevada statute that defines the legal rights and duties of a police officer in the context of an investigative stop. Section 171.123 provides in relevant part:</p>
<blockquote>"1. Any peace officer may detain any person whom the officer encounters under circumstances which reasonably indicate that the person has committed, is committing or is about to commit a crime.</blockquote>
<blockquote>.   .   .   .   .</blockquote>
<blockquote>"3. The officer may detain the person pursuant to this section only to ascertain his identity and the suspicious circumstances surrounding his presence abroad. Any person so detained shall identify himself, but may not <span class="star-pagination">*182</span> be compelled to answer any other inquiry of any peace officer."</blockquote>
<p>Hiibel was tried in the Justice Court of Union Township. The court agreed that Hiibel's refusal to identify himself as required by § 171.123 "obstructed and delayed Dove as a public officer in attempting to discharge his duty" in violation of § 199.280. App. 5. Hiibel was convicted and fined $250. The Sixth Judicial District Court affirmed, rejecting Hiibel's argument that the application of § 171.123 to his case violated the Fourth and Fifth Amendments. On review the Supreme Court of Nevada rejected the Fourth Amendment challenge in a divided opinion. <span class="citation" data-id="8045666"><a href="/opinion/8085804/hiibel-v-sixth-judicial-district-court-of-the-state-of-nevada/" aria-description="Citation for case: Hiibel v. Sixth Judicial District Court of the State of...">118 Nev. 868</a></span>, <span class="citation multiple-matches"><a href="/c/P.%203d/59/1201/">59 P. 3d 1201</a></span> (2002). Hiibel petitioned for rehearing, seeking explicit resolution of his Fifth Amendment challenge. The petition was denied without opinion. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./540/965/">540 U. S. 965</a></span> (2003).</p>
<p></p>
<h2>II</h2>
<p>NRS § 171.123(3) is an enactment sometimes referred to as a "stop and identify" statute. See <span class="citation no-link">Ala. Code § 15-5-30</span> (West 2003); <span class="citation no-link">Ark. Code Ann. § 5-71-213</span>(a)(1) (2004); <span class="citation no-link">Colo. Rev. Stat. § 16-3-103</span>(1) (2003); Del. Code Ann., Tit. 11, §§ 1902(a), 1321(6) (2003); <span class="citation no-link">Fla. Stat. § 856.021</span>(2) (2003); <span class="citation no-link">Ga. Code Ann. § 16-11-36</span>(b) (2003); Ill. Comp. Stat., ch. 725, § 5/107-14 (2004); <span class="citation no-link">Kan. Stat. Ann. § 22-2402</span>(1) (2003); La. Code Crim. Proc. Ann., Art. 215.1(A) (West 2004); <span class="citation no-link">Mo. Rev. Stat. § 84.710</span>(2) (2003); <span class="citation no-link">Mont. Code Ann. § 46-5-401</span>(2)(a) (2003); <span class="citation no-link">Neb. Rev. Stat. § 29-829</span> (2003); N. H. Rev. Stat. Ann. §§ 594:2 and 644:6 (Lexis 2003); N. M. Stat. Ann. § 30-22-3 (2004); <span class="citation no-link">N.Y. Crim. Proc. Law § 140.50</span>(1) (West 2004); N. D. Cent. Code § 29-29-21 (2003); R. I. Gen. Laws § 12-7-1 (2003); <span class="citation no-link">Utah Code Ann. § 77-7-15</span> (2003); Vt. Stat. Ann., Tit. 24, § 1983 (Supp. 2003); <span class="citation no-link">Wis. Stat. § 968.24</span> (2003). See also Note, Stop and Identify Statutes: A New Form of an Inadequate Solution to an Old Problem, 12 Rutgers L. J. 585 (1981); Note, Stop-and-Identify Statutes After <i>Kolender v. Lawson:</i> Exploring <span class="star-pagination">*183</span> the Fourth and Fifth Amendment Issues, <span class="citation no-link">69 Iowa L. Rev. 1057</span> (1984).</p>
<p>Stop and identify statutes often combine elements of traditional vagrancy laws with provisions intended to regulate police behavior in the course of investigatory stops. The statutes vary from State to State, but all permit an officer to ask or require a suspect to disclose his identity. A few States model their statutes on the Uniform Arrest Act, a model code that permits an officer to stop a person reasonably suspected of committing a crime and "demand of him his name, address, business abroad and whither he is going." Warner, The Uniform Arrest Act, <span class="citation no-link">28 Va. L. Rev. 315</span>, 344 (1942). Other statutes are based on the text proposed by the American Law Institute as part of the Institute's Model Penal Code. See ALI, Model Penal Code § 250.6, Comment 4, pp. 392-393 (1980). The provision, originally designated § 250.12, provides that a person who is loitering "under circumstances which justify suspicion that he may be engaged or about to engage in crime commits a violation if he refuses the request of a peace officer that he identify himself and give a reasonably credible account of the lawfulness of his conduct and purposes." § 250.12 (Tent. Draft No. 13) (1961). In some States, a suspect's refusal to identify himself is a misdemeanor offense or civil violation; in others, it is a factor to be considered in whether the suspect has violated loitering laws. In other States, a suspect may decline to identify himself without penalty.</p>
<p>Stop and identify statutes have their roots in early English vagrancy laws that required suspected vagrants to face arrest unless they gave "a good Account of themselves," 15 Geo. 2, ch. 5, § 2 (1744), a power that itself reflected common-law rights of private persons to "arrest any suspicious night-walker, and detain him till he give a good account of himself...." 2 W. Hawkins, Pleas of the Crown, ch. 13, § 6, p. 130. (6th ed. 1787). In recent decades, the Court has found constitutional infirmity in traditional vagrancy laws. <span class="star-pagination">*184</span> In <i>Papachristou</i> v. <i>Jacksonville,</i> <span class="citation" data-id="108472"><a href="/opinion/108472/papachristou-v-city-of-jacksonville/" aria-description="Citation for case: Papachristou v. City of Jacksonville">405 U. S. 156</a></span> (1972), the Court held that a traditional vagrancy law was void for vagueness. Its broad scope and imprecise terms denied proper notice to potential offenders and permitted police officers to exercise unfettered discretion in the enforcement of the law. See <span class="citation" data-id="108472"><a href="/opinion/108472/papachristou-v-city-of-jacksonville/#167" aria-description="Citation for case: Papachristou v. City of Jacksonville"><i>id.,</i> at 167-171</a></span>.</p>
<p>The Court has recognized similar constitutional limitations on the scope and operation of stop and identify statutes. In <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#52" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 52</a></span> (1979), the Court invalidated a conviction for violating a Texas stop and identify statute on Fourth Amendment grounds. The Court ruled that the initial stop was not based on specific, objective facts establishing reasonable suspicion to believe the suspect was involved in criminal activity. See <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas"><i>id.,</i> at 51-52</a></span>. Absent that factual basis for detaining the defendant, the Court held, the risk of "arbitrary and abusive police practices" was too great and the stop was impermissible. <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#52" aria-description="Citation for case: Brown v. Texas"><i>Id.,</i> at 52</a></span>. Four Terms later, the Court invalidated a modified stop and identify statute on vagueness grounds. See <i>Kolender</i> v. <i>Lawson,</i> <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">461 U. S. 352</a></span> (1983). The California law in <i><span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">Kolender</a></span></i> required a suspect to give an officer "`credible and reliable'" identification when asked to identify himself. <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/#360" aria-description="Citation for case: Kolender v. Lawson"><i>Id.,</i> at 360</a></span>. The Court held that the statute was void because it provided no standard for determining what a suspect must do to comply with it, resulting in "`virtually unrestrained power to arrest and charge persons with a violation.'" <i><span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">Ibid.</a></span></i> (quoting <i>Lewis</i> v. <i>New Orleans,</i> <span class="citation" data-id="9425601"><a href="/opinion/108965/lewis-v-city-of-new-orleans/#135" aria-description="Citation for case: Lewis v. City of New Orleans">415 U. S. 130, 135</a></span> (1974) (Powell, J., concurring in result)).</p>
<p>The present case begins where our prior cases left off. Here there is no question that the initial stop was based on reasonable suspicion, satisfying the Fourth Amendment requirements noted in <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Brown</a></span>.</i> Further, the petitioner has not alleged that the statute is unconstitutionally vague, as in <i><span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">Kolender</a></span>.</i> Here the Nevada statute is narrower and more precise. The statute in <i><span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">Kolender</a></span></i> had been interpreted to require a suspect to give the officer "credible and reliable" <span class="star-pagination">*185</span> identification. In contrast, the Nevada Supreme Court has interpreted NRS § 171.123(3) to require only that a suspect disclose his name. See <span class="citation" data-id="8045666"><a href="/opinion/8085804/hiibel-v-sixth-judicial-district-court-of-the-state-of-nevada/#875" aria-description="Citation for case: Hiibel v. Sixth Judicial District Court of the State of...">118 Nev., at 875</a></span>, <span class="citation" data-id="8045666"><a href="/opinion/8085804/hiibel-v-sixth-judicial-district-court-of-the-state-of-nevada/#1206" aria-description="Citation for case: Hiibel v. Sixth Judicial District Court of the State of...">59 P. 3d, at 1206</a></span> (opinion of Young, C.J.) ("The suspect is not required to provide private details about his background, but merely to state his name to an officer when reasonable suspicion exists"). As we understand it, the statute does not require a suspect to give the officer a driver's license or any other document. Provided that the suspect either states his name or communicates it to the officer by other means  a choice, we assume, that the suspect may make  the statute is satisfied and no violation occurs. See <span class="citation" data-id="8045666"><a href="/opinion/8085804/hiibel-v-sixth-judicial-district-court-of-the-state-of-nevada/#876" aria-description="Citation for case: Hiibel v. Sixth Judicial District Court of the State of..."><i>id.,</i> at 876-877</a></span>, <span class="citation" data-id="8045666"><a href="/opinion/8085804/hiibel-v-sixth-judicial-district-court-of-the-state-of-nevada/#1206" aria-description="Citation for case: Hiibel v. Sixth Judicial District Court of the State of...">59 P. 3d, at 1206-1207</a></span>.</p>
<p></p>
<h2>III</h2>
<p>Hiibel argues that his conviction cannot stand because the officer's conduct violated his Fourth Amendment rights. We disagree.</p>
<p>Asking questions is an essential part of police investigations. In the ordinary course a police officer is free to ask a person for identification without implicating the Fourth Amendment. "[I]nterrogation relating to one's identity or a request for identification by the police does not, by itself, constitute a Fourth Amendment seizure." <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#216" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 216</a></span> (1984). Beginning with <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), the Court has recognized that a law enforcement officer's reasonable suspicion that a person may be involved in criminal activity permits the officer to stop the person for a brief time and take additional steps to investigate further. <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#216" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>Delgado, supra,</i> at 216</a></span>; <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 881</a></span> (1975). To ensure that the resulting seizure is constitutionally reasonable, a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop must be limited. The officer's action must be "`justified at its inception, and ... reasonably related in scope to the circumstances which justified the interference in the first place.'" <i>United States</i> v. <i>Sharpe,</i> <span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#682" aria-description="Citation for case: United States v. Sharpe">470 U. S. 675, 682</a></span> (1985) (quoting <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 20</a></span>). For example, the seizure cannot <span class="star-pagination">*186</span> continue for an excessive period of time, see <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place">462 U. S. 696, 709</a></span> (1983), or resemble a traditional arrest, see <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 212</a></span> (1979).</p>
<p>Our decisions make clear that questions concerning a suspect's identity are a routine and accepted part of many <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stops. See <i>United States</i> v. <i>Hensley,</i> <span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#229" aria-description="Citation for case: United States v. Hensley">469 U. S. 221, 229</a></span> (1985) ("[T]he ability to briefly stop [a suspect], ask questions, or check identification in the absence of probable cause promotes the strong government interest in solving crimes and bringing offenders to justice"); <i>Hayes</i> v. <i>Florida,</i> <span class="citation" data-id="9429967"><a href="/opinion/111382/hayes-v-florida/#816" aria-description="Citation for case: Hayes v. Florida">470 U. S. 811, 816</a></span> (1985) ("[I]f there are articulable facts supporting a reasonable suspicion that a person has committed a criminal offense, that person may be stopped in order to identify him, to question him briefly, or to detain him briefly while attempting to obtain additional information"); <i>Adams</i> v. <i>Williams,</i> <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 146</a></span> (1972) ("A brief stop of a suspicious individual, in order to determine his identity or to maintain the status quo momentarily while obtaining more information, may be most reasonable in light of the facts known to the officer at the time").</p>
<p>Obtaining a suspect's name in the course of a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop serves important government interests. Knowledge of identity may inform an officer that a suspect is wanted for another offense, or has a record of violence or mental disorder. On the other hand, knowing identity may help clear a suspect and allow the police to concentrate their efforts elsewhere. Identity may prove particularly important in cases such as this, where the police are investigating what appears to be a domestic assault. Officers called to investigate domestic disputes need to know whom they are dealing with in order to assess the situation, the threat to their own safety, and possible danger to the potential victim.</p>
<p>Although it is well established that an officer may ask a suspect to identify himself in the course of a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop, it has been an open question whether the suspect can be arrested <span class="star-pagination">*187</span> and prosecuted for refusal to answer. See <i>Brown,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#53" aria-description="Citation for case: Brown v. Texas">443 U. S., at 53, n. 3</a></span>. Petitioner draws our attention to statements in prior opinions that, according to him, answer the question in his favor. In <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> Justice White stated in a concurring opinion that a person detained in an investigative stop can be questioned but is "not obliged to answer, answers may not be compelled, and refusal to answer furnishes no basis for an arrest." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 34</a></span>. The Court cited this opinion in dicta in <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#439" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 439</a></span> (1984), a decision holding that a routine traffic stop is not a custodial stop requiring the protections of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). In the course of explaining why <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stops have not been subject to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the Court suggested reasons why <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stops have a "nonthreatening character," among them the fact that a suspect detained during a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop "is not obliged to respond" to questions. See <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#439" aria-description="Citation for case: Berkemer v. McCarty"><i>Berkemer, supra,</i> at 439, 440</a></span>. According to petitioner, these statements establish a right to refuse to answer questions during a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop.</p>
<p>We do not read these statements as controlling. The passages recognize that the Fourth Amendment does not impose obligations on the citizen but instead provides rights against the government. As a result, the Fourth Amendment itself cannot require a suspect to answer questions. This case concerns a different issue, however. Here, the source of the legal obligation arises from Nevada state law, not the Fourth Amendment. Further, the statutory obligation does not go beyond answering an officer's request to disclose a name. See NRS § 171.123(3) ("Any person so detained shall identify himself, but may not be compelled to answer any other inquiry of any peace officer"). As a result, we cannot view the dicta in <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i> or Justice White's concurrence in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> as answering the question whether a State can compel a suspect to disclose his name during a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop.</p>
<p>The principles of <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> permit a State to require a suspect to disclose his name in the course of a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop. The reasonableness <span class="star-pagination">*188</span> of a seizure under the Fourth Amendment is determined "by balancing its intrusion on the individual's Fourth Amendment interests against its promotion of legitimate government interests." <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979). The Nevada statute satisfies that standard. The request for identity has an immediate relation to the purpose, rationale, and practical demands of a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop. The threat of criminal sanction helps ensure that the request for identity does not become a legal nullity. On the other hand, the Nevada statute does not alter the nature of the stop itself: it does not change its duration, <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place"><i>Place, supra,</i> at 709</a></span>, or its location, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York"><i>Dunaway, supra,</i> at 212</a></span>. A state law requiring a suspect to disclose his name in the course of a valid <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop is consistent with Fourth Amendment prohibitions against unreasonable searches and seizures.</p>
<p>Petitioner argues that the Nevada statute circumvents the probable-cause requirement, in effect allowing an officer to arrest a person for being suspicious. According to petitioner, this creates a risk of arbitrary police conduct that the Fourth Amendment does not permit. Brief for Petitioner 28-33. These are familiar concerns; they were central to the opinion in <i><span class="citation" data-id="108472"><a href="/opinion/108472/papachristou-v-city-of-jacksonville/" aria-description="Citation for case: Papachristou v. City of Jacksonville">Papachristou</a></span>,</i> and also to the decisions limiting the operation of stop and identify statutes in <i><span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">Kolender</a></span></i> and <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Brown</a></span>.</i> Petitioner's concerns are met by the requirement that a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop must be justified at its inception and "reasonably related in scope to the circumstances which justified" the initial stop. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20</a></span>. Under these principles, an officer may not arrest a suspect for failure to identify himself if the request for identification is not reasonably related to the circumstances justifying the stop. The Court noted a similar limitation in <i><span class="citation" data-id="9429967"><a href="/opinion/111382/hayes-v-florida/" aria-description="Citation for case: Hayes v. Florida">Hayes</a></span>,</i> where it suggested that <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> may permit an officer to determine a suspect's identity by compelling the suspect to submit to fingerprinting only if there is "a reasonable basis for believing that fingerprinting will establish or negate the suspect's connection with that crime." 470 U. S., at 817. It is clear in this case that the <span class="star-pagination">*189</span> request for identification was "reasonably related in scope to the circumstances which justified" the stop. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 20</a></span>. The officer's request was a commonsense inquiry, not an effort to obtain an arrest for failure to identify after a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop yielded insufficient evidence. The stop, the request, and the State's requirement of a response did not contravene the guarantees of the Fourth Amendment.</p>
<p></p>
<h2>IV</h2>
<p>Petitioner further contends that his conviction violates the Fifth Amendment's prohibition on compelled self-incrimination. The Fifth Amendment states that "[n]o person ... shall be compelled in any criminal case to be a witness against himself." To qualify for the Fifth Amendment privilege, a communication must be testimonial, incriminating, and compelled. See <i>United States</i> v. <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#34" aria-description="Citation for case: United States v. Hubbell">530 U. S. 27, 34-38</a></span> (2000).</p>
<p>Respondents urge us to hold that the statements NRS § 171.123(3) requires are nontestimonial, and so outside the Clause's scope. We decline to resolve the case on that basis. "[T]o be testimonial, an accused's communication must itself, explicitly or implicitly, relate a factual assertion or disclose information." <i>Doe</i> v. <i>United States,</i> <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#210" aria-description="Citation for case: Doe v. United States">487 U.S. 201, 210</a></span> (1988). See also <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#35" aria-description="Citation for case: United States v. Hubbell">530 U. S., at 35</a></span>. Stating one's name may qualify as an assertion of fact relating to identity. Production of identity documents might meet the definition as well. As we noted in <i><span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/" aria-description="Citation for case: United States v. Hubbell">Hubbell</a></span>,</i> acts of production may yield testimony establishing "the existence, authenticity, and custody of items [the police seek]." <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#41" aria-description="Citation for case: United States v. Hubbell"><i>Id.,</i> at 41</a></span>. Even if these required actions are testimonial, however, petitioner's challenge must fail because in this case disclosure of his name presented no reasonable danger of incrimination.</p>
<p>The Fifth Amendment prohibits only compelled testimony that is incriminating. See <i>Brown</i> v. <i>Walker,</i> <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#598" aria-description="Citation for case: Brown v. Walker">161 U. S. 591, 598</a></span> (1896) (noting that where "the answer of the witness will not directly show his infamy, but only <i>tend</i> to disgrace him, <span class="star-pagination">*190</span> he is bound to answer"). A claim of Fifth Amendment privilege must establish</p>
<blockquote>"`reasonable ground to apprehend danger to the witness from his being compelled to answer . . . . [T]he danger to be apprehended must be real and appreciable, with reference to the ordinary operation of law in the ordinary course of things,  not a danger of an imaginary and unsubstantial character, having reference to some extraordinary and barely possible contingency, so improbable that no reasonable man would suffer it to influence his conduct.'" <i><span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/" aria-description="Citation for case: Brown v. Walker">Id.,</a></span></i> at 599-600 (quoting <i>Queen</i> v. <i>Boyes,</i> 1 B. &amp; S. 311, 330, 121 Eng. Rep. 730, 738 (Q. B. 1861) (Cockburn, C. J.)).</blockquote>
<p>As we stated in <i>Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#445" aria-description="Citation for case: Kastigar v. United States">406 U.S. 441, 445</a></span> (1972), the Fifth Amendment privilege against compulsory self-incrimination "protects against any disclosures that the witness reasonably believes could be used in a criminal prosecution or could lead to other evidence that might be so used." Suspects who have been granted immunity from prosecution may, therefore, be compelled to answer; with the threat of prosecution removed, there can be no reasonable belief that the evidence will be used against them. See <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#453" aria-description="Citation for case: Kastigar v. United States"><i>id.,</i> at 453</a></span>.</p>
<p>In this case petitioner's refusal to disclose his name was not based on any articulated real and appreciable fear that his name would be used to incriminate him, or that it "would furnish a link in the chain of evidence needed to prosecute" him. <i>Hoffman</i> v. <i>United States,</i> <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/#486" aria-description="Citation for case: Hoffman v. United States">341 U. S. 479, 486</a></span> (1951). As best we can tell, petitioner refused to identify himself only because he thought his name was none of the officer's business. Even today, petitioner does not explain how the disclosure of his name could have been used against him in a criminal case. While we recognize petitioner's strong belief that he should not have to disclose his identity, the Fifth <span class="star-pagination">*191</span> Amendment does not override the Nevada Legislature's judgment to the contrary absent a reasonable belief that the disclosure would tend to incriminate him.</p>
<p>The narrow scope of the disclosure requirement is also important. One's identity is, by definition, unique; yet it is, in another sense, a universal characteristic. Answering a request to disclose a name is likely to be so insignificant in the scheme of things as to be incriminating only in unusual circumstances. See <i>Baltimore City Dept. of Social Servs.</i> v. <i>Bouknight,</i> <span class="citation" data-id="9431889"><a href="/opinion/112360/baltimore-city-department-of-social-services-v-bouknight/#555" aria-description="Citation for case: Baltimore City Department of Social Services v. Bouknight">493 U. S. 549, 555</a></span> (1990) (suggesting that "fact[s] the State could readily establish" may render "any testimony regarding existence or authenticity [of them] insufficiently incriminating"); cf. <i>California</i> v. <i>Byers,</i> <span class="citation" data-id="9424566"><a href="/opinion/108335/california-v-byers/#432" aria-description="Citation for case: California v. Byers">402 U. S. 424, 432</a></span> (1971) (opinion of Burger, C. J.). In every criminal case, it is known and must be known who has been arrested and who is being tried. Cf. <i>Pennsylvania</i> v. <i>Muniz,</i> <span class="citation" data-id="9432075"><a href="/opinion/112464/pennsylvania-v-muniz/#601" aria-description="Citation for case: Pennsylvania v. Muniz">496 U. S. 582, 601-602</a></span> (1990) (principal opinion of Brennan, J.). Even witnesses who plan to invoke the Fifth Amendment privilege answer when their names are called to take the stand. Still, a case may arise where there is a substantial allegation that furnishing identity at the time of a stop would have given the police a link in the chain of evidence needed to convict the individual of a separate offense. In that case, the court can then consider whether the privilege applies, and, if the Fifth Amendment has been violated, what remedy must follow. We need not resolve those questions here.</p>
<p>The judgment of the Nevada Supreme Court is <i>Affirmed.</i></p>
<p>JUSTICE STEVENS, dissenting.</p>
<p>The Nevada law at issue in this case imposes a narrow duty to speak upon a specific class of individuals. The class includes only those persons detained by a police officer "under circumstances which reasonably indicate that the person has committed, is committing or is about to commit a <span class="star-pagination">*192</span> crime"<sup>[1]</sup>  persons who are, in other words, targets of a criminal investigation. The statute therefore is directed not "at the public at large," but rather "at a highly selective group inherently suspect of criminal activities." <i>Albertson</i> v. <i>Subversive Activities Control Bd.,</i> <span class="citation" data-id="9423096"><a href="/opinion/107110/albertson-v-subversive-activities-control-board/#79" aria-description="Citation for case: Albertson v. Subversive Activities Control Board">382 U. S. 70, 79</a></span> (1965).</p>
<p>Under the Nevada law, a member of the targeted class "may not be compelled to answer" any inquiry except a command that he "identify himself."<sup>[2]</sup> Refusal to identify oneself upon request is punishable as a crime.<sup>[3]</sup> Presumably the statute does not require the detainee to answer any other question because the Nevada Legislature realized that the Fifth Amendment prohibits compelling the target of a criminal investigation to make any other statement. In my judgment, the broad constitutional right to remain silent, which derives from the Fifth Amendment's guarantee that "[n]o person . . . shall be compelled in any criminal case to be a witness against himself,"<sup>[4]</sup> is not as circumscribed as the Court suggests, and does not admit even of the narrow exception defined by the Nevada statute.</p>
<p>"[T]here can be no doubt that the Fifth Amendment privilege is available outside of criminal court proceedings and serves to protect persons in all settings in which their freedom of action is curtailed in any significant way from being compelled to incriminate themselves." <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 467</a></span> (1966). It is a "settled principle" that "the police have the right to request citizens to answer voluntarily questions concerning unsolved crimes," but <span class="star-pagination">*193</span> "they have no right to compel them to answer." <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#727" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 727, n. 6</a></span> (1969). The protections of the Fifth Amendment are directed squarely toward those who are the focus of the government's investigative and prosecutorial powers. In a criminal trial, the indicted defendant has an unqualified right to refuse to testify and may not be punished for invoking that right. See <i>Carter</i> v. <i>Kentucky,</i> <span class="citation" data-id="9428216"><a href="/opinion/110426/carter-v-kentucky/#299" aria-description="Citation for case: Carter v. Kentucky">450 U. S. 288, 299-300</a></span> (1981). The unindicted target of a grand jury investigation enjoys the same constitutional protection even if he has been served with a subpoena. See <i>Chavez</i> v. <i>Martinez,</i> <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#767" aria-description="Citation for case: Chavez v. Martinez">538 U. S. 760, 767-768</a></span> (2003). So does an arrested suspect during custodial interrogation in a police station. <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>.</p>
<p>There is no reason why the subject of police interrogation based on mere suspicion, rather than probable cause, should have any lesser protection. Indeed, we have said that the Fifth Amendment's protections apply with equal force in the context of <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stops, see <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), where an officer's inquiry "must be `reasonably related in scope to the justification for [the stop's] initiation.'" <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#439" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 439</a></span> (1984) (some internal quotation marks omitted). "Typically, this means that the officer may ask the detainee a moderate number of questions to determine his identity and to try to obtain information confirming or dispelling the officer's suspicions. But the detainee is not obliged to respond." <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Ibid.</a></span></i> See also <i>Terry,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 34</a></span> (White, J., concurring) ("Of course, the person stopped is not obliged to answer, answers may not be compelled, and refusal to answer furnishes no basis for an arrest, although it may alert the officer to the need for continued observation"). Given our statements to the effect that citizens are not required to respond to police officers' questions during a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop, it is no surprise that petitioner assumed, as have we, that he had a right not to disclose his identity.</p>
<p>The Court correctly observes that a communication does not enjoy the Fifth Amendment privilege unless it is testimonial. <span class="star-pagination">*194</span> Although the Court declines to resolve this question, <i>ante,</i> at 189, I think it clear that this case concerns a testimonial communication. Recognizing that whether a communication is testimonial is sometimes a "difficult question," <i>Doe</i> v. <i>United States,</i> <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#214" aria-description="Citation for case: Doe v. United States">487 U. S. 201, 214-215</a></span> (1988), we have stated generally that "[i]t is the `extortion of information from the accused,' the attempt to force him `to disclose the contents of his own mind,' that implicates the Self-Incrimination Clause," <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#211" aria-description="Citation for case: Doe v. United States"><i>id.,</i> at 211</a></span> (citations omitted). While "[t]he vast majority of verbal statements thus will be testimonial and, to that extent at least, will fall within the privilege," <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#213" aria-description="Citation for case: Doe v. United States"><i>id.,</i> at 213-214</a></span>, certain acts and physical evidence fall outside the privilege.<sup>[5]</sup> In all instances, we have afforded Fifth Amendment protection if the disclosure in question was being admitted because of its content rather than some other aspect of the communication.<sup>[6]</sup></p>
<p>Considered in light of these precedents, the compelled statement at issue in this case is clearly testimonial. It is significant that the communication must be made in response <span class="star-pagination">*195</span> to a question posed by a police officer. As we recently explained, albeit in the different context of the Sixth Amendment's Confrontation Clause, "[w]hatever else the term [`testimonial'] covers, it applies at a minimum . . . to police interrogations." <i>Crawford</i> v. <i>Washington,</i> <span class="citation" data-id="9434566"><a href="/opinion/134724/crawford-v-washington/#68" aria-description="Citation for case: Crawford v. Washington">541 U. S. 36, 68</a></span> (2004). Surely police questioning during a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop qualifies as an interrogation, and it follows that responses to such questions are testimonial in nature.</p>
<p>Rather than determining whether the communication at issue is testimonial, the Court instead concludes that the State can compel the disclosure of one's identity because it is not "incriminating." <i>Ante,</i> at 189. But our cases have afforded Fifth Amendment protection to statements that are "incriminating" in a much broader sense than the Court suggests. It has "long been settled that [the Fifth Amendment's] protection encompasses compelled statements that lead to the discovery of incriminating evidence even though the statements themselves are not incriminating and are not introduced into evidence." <i>United States</i> v. <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#37" aria-description="Citation for case: United States v. Hubbell">530 U. S. 27, 37</a></span> (2000). By "incriminating" we have meant disclosures that "could be used in a criminal prosecution or could lead to other evidence that might be so used," <i>Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#445" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 445</a></span> (1972)  communications, in other words, that "would furnish a link in the chain of evidence needed to prosecute the claimant for a federal crime," <i>Hoffman</i> v. <i>United States,</i> <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/#486" aria-description="Citation for case: Hoffman v. United States">341 U. S. 479, 486</a></span> (1951). Thus, "[c]ompelled testimony that communicates information that may `lead to incriminating evidence' is privileged even if the information itself is not inculpatory." <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/" aria-description="Citation for case: United States v. Hubbell">530 U. S., at 38</a></span> (quoting <i>Doe,</i> <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#208" aria-description="Citation for case: Doe v. United States">487 U. S., at 208, n. 6</a></span>).</p>
<p>Given a proper understanding of the category of "incriminating" communications that fall within the Fifth Amendment privilege, it is clear that the disclosure of petitioner's identity is protected. The Court reasons that we should not assume that the disclosure of petitioner's "name would be used to incriminate him, or that it would furnish a link in [a] <span class="star-pagination">*196</span> chain of evidence needed to prosecute him." <i>Ante,</i> at 190 (internal quotation marks omitted). But why else would an officer ask for it? And why else would the Nevada Legislature require its disclosure only when circumstances "reasonably indicate that the person has committed, is committing or is about to commit a crime"?<sup>[7]</sup> If the Court is correct, then petitioner's refusal to cooperate did not impede the police investigation. Indeed, if we accept the predicate for the Court's holding, the statute requires nothing more than a useless invasion of privacy. I think that, on the contrary, the Nevada Legislature intended to provide its police officers with a useful law enforcement tool, and that the very existence of the statute demonstrates the value of the information it demands.</p>
<p>A person's identity obviously bears informational and incriminating worth, "even if the [name] itself is not inculpatory." <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#38" aria-description="Citation for case: United States v. Hubbell">530 U. S., at 38</a></span>. A name can provide the key to a broad array of information about the person, particularly in the hands of a police officer with access to a range of law enforcement databases. And that information, in turn, can be tremendously useful in a criminal prosecution. It is therefore quite wrong to suggest that a person's identity provides a link in the chain to incriminating evidence "only in unusual circumstances." <i>Ante,</i> at 191.</p>
<p>The officer in this case told petitioner, in the Court's words, that "he was conducting an investigation and needed to see some identification." <i>Ante,</i> at 181. As the target of that investigation, petitioner, in my view, acted well within his rights when he opted to stand mute. Accordingly, I respectfully dissent.</p>
<p><span class="star-pagination">*197</span> JUSTICE BREYER, with whom JUSTICE SOUTER and JUSTICE GINSBURG join, dissenting.</p>
<p>Notwithstanding the vagrancy statutes to which the majority refers, see <i>ante,</i> at 183-184, this Court's Fourth Amendment precedents make clear that police may conduct a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop only within circumscribed limits. And one of those limits invalidates laws that compel responses to police questioning.</p>
<p>In <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), the Court considered whether police, in the absence of probable cause, can stop, question, or frisk an individual at all. The Court recognized that the Fourth Amendment protects the "`right of every individual to the possession and control of his own person.'" <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Id.,</a></span></i> at 9 (quoting <i>Union Pacific R. Co.</i> v. <i>Botsford,</i> <span class="citation" data-id="93149"><a href="/opinion/93149/union-pacific-railway-co-v-botsford/#251" aria-description="Citation for case: Union Pacific Railway Co. v. Botsford">141 U. S. 250, 251</a></span> (1891)). At the same time, it recognized that in certain circumstances, public safety might require a limited "seizure," or stop, of an individual against his will. The Court consequently set forth conditions circumscribing when and how the police might conduct a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop. They include what has become known as the "reasonable suspicion" standard. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20-22</a></span>. Justice White, in a separate concurring opinion, set forth further conditions. Justice White wrote: "Of course, the person stopped is not obliged to answer, answers may not be compelled, and refusal to answer furnishes no basis for an arrest, although it may alert the officer to the need for continued observation." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 34</a></span>.</p>
<p>About 10 years later, the Court, in <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">443 U. S. 47</a></span> (1979), held that police lacked "any reasonable suspicion" to detain the particular petitioner and require him to identify himself. <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#53" aria-description="Citation for case: Brown v. Texas"><i>Id.,</i> at 53</a></span>. The Court noted that the trial judge had asked the following: "`I'm sure [officers conducting a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop] should ask everything they possibly could find out. <i>What I'm asking is what's the State's interest in putting a man in jail because he doesn't want to answer.</i> ...'" <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#54" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 54</a></span> (Appendix to opinion of the Court) (emphasis in <span class="star-pagination">*198</span> original). The Court referred to Justice White's <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> concurrence. <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#53" aria-description="Citation for case: Brown v. Texas">443 U. S., at 53, n. 3</a></span>. And it said that it "need not decide" the matter. <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Ibid.</a></span></i></p>
<p>Then, five years later, the Court wrote that an "officer may ask the <i>[Terry]</i> detainee a moderate number of questions to determine his identity and to try to obtain information confirming or dispelling the officer's suspicions. <i>But the detainee is not obliged to respond.</i>" <i>Berkemer</i> v. <i>Mc</i><i>Carty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#439" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 439</a></span> (1984) (emphasis added). See also <i>Kolender</i> v. <i>Lawson,</i> <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/#365" aria-description="Citation for case: Kolender v. Lawson">461 U. S. 352, 365</a></span> (1983) (Brennan, J., concurring) (<span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio"><i>Terry</i></a></span> suspect "must be free to ... decline to answer the questions put to him"); <i>Illinois</i> v. <i>Wardlow,</i> <span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/#125" aria-description="Citation for case: Illinois v. Wardlow">528 U. S. 119, 125</a></span> (2000) (stating that allowing officers to stop and question a fleeing person "is quite consistent with the individual's right to go about his business or to stay put and remain silent in the face of police questioning").</p>
<p>This lengthy history  of concurring opinions, of references, and of clear explicit statements  means that the Court's statement in <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span>,</i> while technically dicta, is the kind of strong dicta that the legal community typically takes as a statement of the law. And that law has remained undisturbed for more than 20 years.</p>
<p>There is no good reason now to reject this generation-old statement of the law. There are sound reasons rooted in Fifth Amendment considerations for adhering to this Fourth Amendment legal condition circumscribing police authority to stop an individual against his will. See <i>ante,</i> at 192-196 (STEVENS, J., dissenting). Administrative considerations also militate against change. Can a State, in addition to requiring a stopped individual to answer "What's your name?" also require an answer to "What's your license number?" or "Where do you live?" Can a police officer, who must know how to make a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop, keep track of the constitutional answers? After all, answers to any of these questions may, or may not, incriminate, depending upon the circumstances.</p>
<p><span class="star-pagination">*199</span> Indeed, as the Court points out, a name itself  even if it is not "Killer Bill" or "Rough 'em up Harry"  will sometimes provide the police with "a link in the chain of evidence needed to convict the individual of a separate offense." <i>Ante,</i> at 191. The majority reserves judgment about whether compulsion is permissible in such instances. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ibid.</a></span></i> How then is a police officer in the midst of a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop to distinguish between the majority's ordinary case and this special case where the majority reserves judgment?</p>
<p>The majority presents no evidence that the rule enunciated by Justice White and then by the <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i> Court, which for nearly a generation has set forth a settled <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i>-stop condition, has significantly interfered with law enforcement. Nor has the majority presented any other convincing justification for change. I would not begin to erode a clear rule with special exceptions.</p>
<p>I consequently dissent.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the American Civil Liberties Union by <i>Steven R. Shapiro, Lawrence S. Lustberg,</i> and <i>Mark A. Berman;</i> for the Cato Institute by <i>Timothy Lynch</i> and <i>M. Christine Klein;</i> for the National Law Center on Homelessness &amp; Poverty et al. by <i>Carter G. Phillips, Edward R. McNicholas,</i> and <i>Rebecca K. Troth;</i> and for John Gilmore by <i>James P. Harrison.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the Criminal Justice Legal Foundation by <i>Kent S. Scheidegger</i> and <i>Charles L. Hobson;</i> and for the National Association of Police Organizations by <i>Joel D. Bertocchi</i> and <i>Philip Allen Lacovara.</i></p>
<p>Briefs of <i>amici curiae</i> were filed for the Electronic Frontier Foundation by <i>Robert Weisberg;</i> for the Electronic Privacy Information Center et al. by <i>Marc Rotenberg</i> and <i>David L. Sobel;</i> and for Privacy Activism et al. by <i>William M. Simpich.</i></p>
<p>[1]  <span class="citation no-link">Nev. Rev. Stat. § 171.123</span>(1) (2003).</p>
<p>[2]  § 171.123(3).</p>
<p>[3]  In this case, petitioner was charged with violating § 199.280, which makes it a crime to "willfully resis[t], dela[y] or obstruc[t] a public officer in discharging or attempting to discharge any legal duty of his office." A violation of that provision is a misdemeanor unless a dangerous weapon is involved.</p>
<p>[4]  The Fifth Amendment's protection against compelled self-incrimination applies to the States through the Fourteenth Amendment's Due Process Clause. See <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#6" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 6</a></span> (1964).</p>
<p>[5]  A suspect may be made, for example, to provide a blood sample, <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#765" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 765</a></span> (1966), a voice exemplar, <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#7" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1, 7</a></span> (1973), or a handwriting sample, <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#266" aria-description="Citation for case: Gilbert v. California">388 U. S. 263, 266-267</a></span> (1967).</p>
<p>[6]  See <i>Pennsylvania</i> v. <i>Muniz,</i> <span class="citation" data-id="9432075"><a href="/opinion/112464/pennsylvania-v-muniz/#598" aria-description="Citation for case: Pennsylvania v. Muniz">496 U.S. 582, 598-599</a></span> (1990) (respondent's answer to the "birthday question" was protected because the "content of his truthful answer supported an inference that his mental faculties were impaired"); <i>Doe</i> v. <i>United States,</i> <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#211" aria-description="Citation for case: Doe v. United States">487 U. S. 201, 211, n. 10</a></span> (1988) ("The content itself must have testimonial significance"); <i>Fisher</i> v. <i>United States,</i> <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#410" aria-description="Citation for case: Fisher v. United States">425 U. S. 391, 410-411</a></span> (1976) ("[H]owever incriminating the contents of the accountant's workpapers might be, the act of producing them  the only thing which the taxpayer is compelled to do  would not itself involve testimonial self-incrimination"); <i>Gilbert,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#266" aria-description="Citation for case: Gilbert v. California">388 U. S., at 266-267</a></span> ("A mere handwriting exemplar, in contrast to the content of what is written, like the voice or body itself, is an identifying physical characteristic outside its protection"); <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#223" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 223</a></span> (1967) ("[I]t deserves emphasis that this case presents no question of the admissibility in evidence of anything Wade said or did at the lineup which implicates his privilege").</p>
<p>[7]  <span class="citation no-link">Nev. Rev. Stat. § 171.123</span>(1) (2003). The Court suggests that furnishing identification also allows the investigating officer to assess the threat to himself and others. See <i>ante,</i> at 186. But to the extent that officer or public safety is immediately at issue, that concern is sufficiently alleviated by the officer's ability to perform a limited patdown search for weapons. See <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#25" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1, 25-26</a></span> (1968).</p>

</div>
```

---

## GROUP: content/cases/Horton v. California.md  (`case`, 5 assertions)

### content_page

```
---
title: "Horton v. California"
type: case
citation: "496 U.S. 128 (1990)"
parallel_cite: "110 S. Ct. 2301; 110 L. Ed. 2d 112"
neutral_cite: 1990 U.S. LEXIS 2937
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-06-04
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1990-06-04
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Horton v. California
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112448/horton-v-california/"
  cluster_id: 112448
  opinion_id: 9432041
  identity_checked: true
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Key — Anchor"
related: ["[[Coolidge v. New Hampshire]]", "[[Arizona v. Hicks]]", "[[Texas v. Brown]]"]
aliases: []
tags: ["case", "fourth-amendment", "plain-view", "seizure", "warrant"]
holding: "Sets the modern plain-view SEIZURE test and DROPS the inadvertence requirement: a warrantless seizure of an item in plain view is lawful…"
lake:
  record_id: Horton v. California
  status: under_review
  projected_at: 2026-07-09
---

# Horton v. California

*496 U.S. 128 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A police officer had probable cause to search Horton's home for both the proceeds of an armed robbery and the weapons used in it, but the warrant he obtained described only the proceeds. Executing the warrant, the officer did not find the proceeds but did find the weapons (including a stun gun) in plain view and seized them. The officer admitted he had expected to find the weapons, so their discovery was not inadvertent.

## Issue
Whether the warrantless seizure of evidence in plain view is barred by the Fourth Amendment when the officer's discovery of that evidence was not inadvertent.

## Rule
No. The Court rejected inadvertence as a requirement: "even though inadvertence is a characteristic of most legitimate 'plain-view' seizures, it is not a necessary condition." — 496 U.S. at 130. ^pin-130

A lawful plain-view seizure requires a lawful vantage plus two further conditions. "It is, of course, an essential predicate to any valid warrantless seizure of incriminating evidence that the officer did not violate the Fourth Amendment in arriving at the place from which the evidence could be plainly viewed." — [*Id.* at 136](https://www.courtlistener.com/opinion/112448/horton-v-california/#:~:text=It%20is%2C%20of%20course%2C%20an). ^pin-136

"First, not only must the item be in plain view; its incriminating character must also be 'immediately apparent.'" — *Id.* ^pin-136a

"Second, not only must the officer be lawfully located in a place from which the object can be plainly seen, but he or she must also have a lawful right of access to the object itself." — [*Id.* at 137](https://www.courtlistener.com/opinion/112448/horton-v-california/#:~:text=Second%2C%20not%20only%20must%20the). ^pin-137

## Application
The officer was lawfully in Horton's home executing a valid warrant; the weapons were in plain view, their incriminating character was immediately apparent, and the officer had lawful access to them. That the officer expected — and thus did not inadvertently discover — the weapons did not invalidate the seizure, because inadvertence is not a condition of a lawful plain-view seizure. The seizure was therefore constitutional.

## Conclusion
The warrantless seizure of the weapons was lawful; the judgment was affirmed. Inadvertence is not required for a plain-view seizure.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Horton* states the modern plain-view seizure test and drops the inadvertence element suggested by the [[Coolidge v. New Hampshire]] plurality, building on [[Arizona v. Hicks]]'s "immediately apparent" requirement.

## Appears on
- [[Plain View Doctrine]] — *Key — Anchor*

## Sources
- *Horton v. California*, 496 U.S. 128 (1990) — https://www.courtlistener.com/opinion/112448/horton-v-california/ — pinpoints: 130, 136, 137.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5669f94320d3b509", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "496 U.S. 128 (1990)", "court": "U.S. Supreme Court", "neutral_cite": "1990 U.S. LEXIS 2937", "official_citation_present": true, "parallel_cite": "110 S. Ct. 2301; 110 L. Ed. 2d 112", "title": "Horton v. California", "year": "1990"}}
{"assertion_id": "3c90295fc5a50aa9", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Sets the modern plain-view SEIZURE test and DROPS the inadvertence requirement: a warrantless seizure of an item in plain view is lawful…", "title": "Horton v. California"}}
{"assertion_id": "5037b6996d19591d", "dimension": "support", "kind": "home_role", "locator": {"home": "Plain View Doctrine"}, "payload": {"home": "Plain View Doctrine", "role": "Key — Anchor", "title": "Horton v. California"}}
{"assertion_id": "4ddb43900d3daf0b", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Horton v. California"}}
{"assertion_id": "a13d3955342081c2", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1990-06-04", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Horton v. California", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Horton v. California", "varies_by_point": "false"}}
```

### lake record — Horton v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Horton v. California",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Horton v. California",
    "case_name_short": "Horton",
    "case_name_full": "Horton v. California",
    "input_case_name": "Horton v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-06-04",
    "year": 1990,
    "docket": null,
    "cluster_id": 112448,
    "lead_opinion_id": 9432041,
    "sibling_ids": [
      112448,
      9432041,
      9432042
    ],
    "absolute_url": "/opinion/112448/horton-v-california/",
    "identity_method": "pending",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "496 U.S. 128",
      "volume": "496",
      "reporter": "U.S.",
      "page": "128",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "110 S. Ct. 2301",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "2301",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 L. Ed. 2d 112",
        "volume": "110",
        "reporter": "L. Ed. 2d",
        "page": "112",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 2937",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "2937",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "496 U.S. 128",
        "volume": "496",
        "reporter": "U.S.",
        "page": "128",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 2301",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "2301",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 L. Ed. 2d 112",
        "volume": "110",
        "reporter": "L. Ed. 2d",
        "page": "112",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 2937",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "2937",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "496 U.S. 128",
    "official_selection": {
      "court_class": "scotus",
      "selected": "496 U.S. 128",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-130",
      "page": null,
      "quote": "--- # Horton v. California *496 U.S. 128 (1990)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A police officer had probable cause to search Horton's home for both the proceeds of an armed robbery and the weapons used in it, but the warrant he obtained described only the proceeds. Executing the warrant, the officer did not find the proceeds but did find the weapons (including a stun gun) in plain view and seized them. The officer admitted he had expected to find the weapons, so their discovery was not inadvertent. ## Issue Whether the warrantless seizure of evidence in plain view is barred by the Fourth Amendment when the officer's discovery of that evidence was not inadvertent. ## Rule No. The Court rejected inadvertence as a requirement:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-136",
      "page": null,
      "quote": "It is, of course, an essential predicate to any valid warrantless seizure of incriminating evidence that the officer did not violate the Fourth Amendment in arriving at the place from which the evidence could be plainly viewed.",
      "star_marker": "136",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 14955,
      "fragment": "#:~:text=It%20is%2C%20of%20course%2C%20an",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-136a",
      "page": null,
      "quote": "First, not only must the item be in plain view; its incriminating character must also be 'immediately apparent.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-137",
      "page": null,
      "quote": "Second, not only must the officer be lawfully located in a place from which the object can be plainly seen, but he or she must also have a lawful right of access to the object itself.",
      "star_marker": "137",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 16227,
      "fragment": "#:~:text=Second%2C%20not%20only%20must%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1990-06-04",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Horton v. California",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 9352593,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6620965,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6478743,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bock (A169480)",
          "cluster_id": 10134134,
          "cite": [
            "310 Or. App. 329",
            "485 P.3d 931"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Garrett",
          "cluster_id": 4552162,
          "cite": [
            "2018 Ohio 4530",
            "123 N.E.3d 327"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kennebrew v. State",
          "cluster_id": 10366687,
          "cite": [
            "304 Ga. 406"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wilson v. Layne",
          "cluster_id": 118289,
          "cite": [
            "143 L. Ed. 2d 818",
            "119 S. Ct. 1692",
            "526 U.S. 603",
            "1999 U.S. LEXIS 3633"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
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
        "journal_ref": "Horton v. California:lane2_top_cited"
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
        "journal_ref": "Horton v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kentucky v. King",
          "cluster_id": 216733,
          "cite": [
            "179 L. Ed. 2d 865",
            "131 S. Ct. 1849",
            "563 U.S. 452",
            "2011 U.S. LEXIS 3541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carpenter v. United States",
          "cluster_id": 4510032,
          "cite": [
            "585 U.S. 296",
            "138 S. Ct. 2206",
            "201 L. Ed. 2d 507",
            "2018 U.S. LEXIS 3844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
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
        "journal_ref": "Horton v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Kraft",
          "cluster_id": 2590211,
          "cite": [
            "5 P.3d 68",
            "99 Cal. Rptr. 2d 1",
            "23 Cal. 4th 978",
            "2000 Daily Journal DAR 8825",
            "2000 Cal. Daily Op. Serv. 6660",
            "2000 Cal. LEXIS 5822"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
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
        "journal_ref": "Horton v. California:lane2_top_cited"
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
        "journal_ref": "Horton v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marvin Berkowitz",
          "cluster_id": 557342,
          "cite": [
            "927 F.2d 1376",
            "1991 U.S. App. LEXIS 4135",
            "1991 WL 33079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
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
        "journal_ref": "Horton v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walter v. State",
          "cluster_id": 1755500,
          "cite": [
            "28 S.W.3d 538",
            "2000 Tex. Crim. App. LEXIS 84",
            "2000 WL 1348504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Carpenter",
          "cluster_id": 5607872,
          "cite": [
            "15 Cal. 4th 312",
            "935 P.2d 708",
            "63 Cal. Rptr. 2d 1",
            "97 Cal. Daily Op. Serv. 3058",
            "97 Daily Journal DAR 5375",
            "1997 Cal. LEXIS 1948"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Ray Bonds (91-3610) Mark Verdi (91-3609) and Steven Wayne Yee (91-3608)",
          "cluster_id": 659341,
          "cite": [
            "12 F.3d 540"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kutzner v. State",
          "cluster_id": 2454806,
          "cite": [
            "994 S.W.2d 180",
            "1999 Tex. Crim. App. LEXIS 71",
            "1999 WL 371396"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Dunn",
          "cluster_id": 1131042,
          "cite": [
            "850 P.2d 1201",
            "208 Utah Adv. Rep. 100",
            "1993 Utah LEXIS 54",
            "1993 WL 79651"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jones",
          "cluster_id": 1546066,
          "cite": [
            "988 A.2d 649",
            "605 Pa. 188",
            "2010 Pa. LEXIS 157"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Johnson",
          "cluster_id": 773999,
          "cite": [
            "256 F.3d 895",
            "2001 Daily Journal DAR 7479",
            "2001 Cal. Daily Op. Serv. 6099",
            "2001 U.S. App. LEXIS 16092",
            "2001 WL 817633"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
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
        "journal_ref": "Horton v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Safford Unified School District 1 v. Redding",
          "cluster_id": 145852,
          "cite": [
            "174 L. Ed. 2d 354",
            "129 S. Ct. 2633",
            "557 U.S. 364",
            "2009 U.S. LEXIS 4735",
            "21 Fla. L. Weekly Fed. S 1011",
            "77 U.S.L.W. 4591"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramos v. State",
          "cluster_id": 1657807,
          "cite": [
            "934 S.W.2d 358",
            "1996 Tex. Crim. App. LEXIS 91",
            "1996 WL 347976"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James G. Jackson v. City of Columbus, Gregory Lashutka, Thomas W. Rice, Sr.",
          "cluster_id": 766509,
          "cite": [
            "194 F.3d 737"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
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
        "journal_ref": "Horton v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Wright",
          "cluster_id": 1915693,
          "cite": [
            "961 A.2d 119",
            "599 Pa. 270",
            "2008 Pa. LEXIS 2316"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hector Vega-Rodriguez v. Puerto Rico Telephone Company",
          "cluster_id": 739069,
          "cite": [
            "110 F.3d 174",
            "12 I.E.R. Cas. (BNA) 1253",
            "1997 U.S. App. LEXIS 6517",
            "1997 WL 154362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Horton v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112448 OR 9432041 OR 9432042) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTI5NTM5MjAwMDAwJnM9NDUwOTQxMSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112448+OR+9432041+OR+9432042%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112448 OR 9432041 OR 9432042)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTUmcz01Njg1MDYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112448+OR+9432041+OR+9432042%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112448 OR 9432041 OR 9432042)",
        "reviewed": 83,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 83,
        "triage_read": 0,
        "triage_snippet_classified": 83
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112448 OR 9432041 OR 9432042)",
    "indexed_citing_opinions": 1881,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112448,
        "count": 1627,
        "count_source": "search"
      },
      {
        "opinion_id": 9432041,
        "count": 276,
        "count_source": "search"
      },
      {
        "opinion_id": 9432042,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2924,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/horton-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNDA0NTgmcz0xMDU4MDE3NSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28112448+OR+9432041+OR+9432042%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112448,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 100621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 107625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 107898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 108099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 111477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 111834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 112384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 112392,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 112416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 374770,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 398193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 459879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 486419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 492384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 492749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 493624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 518459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 521027,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 521039,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 528813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 536215,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 538794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 880574,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1097946,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1124643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1128971,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1156968,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1165264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1167087,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1168589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1176479,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1179588,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1191605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1196703,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1211385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1215622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1239224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1250315,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1261110,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1286575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1289643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1293789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1331807,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1339821,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1358902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1431923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1433513,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1566239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1596133,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1720400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1894142,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1958941,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1976203,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 1976585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 2002688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 2069851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 2076566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 2080643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 2089205,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 2101701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 2126375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 2173154,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 2180899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 2361656,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 2372230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 2404406,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 2409928,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 2434018,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112448,
        "cited_id": 2464243,
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
    "date_created": "2026-07-05T07:26:53Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:27:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:27:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:30:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:27:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Horton v. California

```
<opinion type="majority">
<author id="b172-5">Justice Stevens</author>
<p id="AsU">delivered the opinion of the Court.</p>
<p id="b172-6">In this case we revisit an issue that was considered, but not conclusively resolved, in <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971): Whether the warrantless seizure of evidence of crime in plain view is prohibited by the Fourth Amendment if the discovery of the evidence was not inadvertent. We conclude that even though inadvertence is a characteristic of most legitimate “plain-view” seizures, it is not a necessary condition.</p>
<p id="b172-7">I</p>
<p id="b172-8">Petitioner was convicted of the armed robbery of Erwin Wallaker, the treasurer of the San Jose Coin Club. When Wallaker returned to his home after the Club’s annual show, he entered his garage and was accosted by two masked men, one armed with a machine gun and the other with an electrical shocking device, sometimes referred to as a “stun gun.” The two men shocked Wallaker, bound and handcuffed him, and robbed him of jewelry and cash. During the encounter sufficient conversation took place to enable Wallaker subsequently to identify petitioner’s distinctive voice. His identification was partially corroborated by a witness who saw the robbers leaving the scene and by evidence that petitioner had attended the coin show.</p>
<p id="b172-9">Sergeant LaRault, an experienced police officer, investigated the crime and determined that there was probable cause to search petitioner’s home for the proceeds of the rob<page-number citation-index="1" label="131">*131</page-number>bery and for the weapons used by the robbers. His affidavit for a search warrant referred to police reports that described the weapons as well as the proceeds, but the warrant issued by the Magistrate only authorized a search for the proceeds, including three specifically described rings.</p>
<p id="b173-5">Pursuant to the warrant, LaRault searched petitioner’s residence, but he did not find the stolen property. During the course of the search, however, he discovered the weapons in plain view and seized them. Specifically, he seized an Uzi machine gun, a .38-caliber revolver, two stun guns, a handcuff key, a San Jose Coin Club advertising brochure, and a few items of clothing identified by the victim.<footnotemark>1</footnotemark> LaRault testified that while he was searching for the rings, he also was interested in finding other evidence connecting petitioner to the robbery. Thus, the seized evidence was not discovered “inadvertently.”</p>
<p id="b173-6">The trial court refused to suppress the evidence found in petitioner’s home and, after a jury trial, petitioner was found guilty and sentenced to prison. The California Court of Appeal affirmed. App. 43. It rejected petitioner’s argument that our decision in <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>required suppression of the seized evidence that had not been listed in the warrant because its discovery was not inadvertent. App. 52-53. The court relied on the California Supreme Court’s decision in <em>North </em>v. <em>Superior Court, </em><span class="citation" data-id="9577161"><a href="/opinion/1239224/north-v-superior-court/" aria-description="Citation for case: North v. Superior Court">8 Cal. 3d 301</a></span>, <span class="citation" data-id="9577161"><a href="/opinion/1239224/north-v-superior-court/" aria-description="Citation for case: North v. Superior Court">502 P. 2d 1305</a></span> (1972). In that case the court noted that the discussion of the inadvertence limitation on the “plain-view” doctrine in Justice Stewart’s opinion in <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>had been joined by only three other Members of this Court and therefore was not binding on it.<footnotemark>2</footnotemark> The California Supreme Court denied petitioner’s request for review. App. 78.</p>
<p id="b174-4"><page-number citation-index="1" label="132">*132</page-number>Because the California courts’ interpretation of the “plain-view” doctrine conflicts with the view of other courts,<footnotemark>3</footnotemark> and because the unresolved issue is important, we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./493/889/">493 U. S. 889</a></span> (1989).</p>
<p id="b175-11"><page-number citation-index="1" label="133">*133</page-number>II</p>
<p id="b175-3">The Fourth Amendment provides:</p>
<blockquote id="b175-4">“The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”</blockquote>
<p id="b175-5">The right to security in person and property protected by the Fourth Amendment may be invaded in quite different ways by searches and seizures. A search compromises the individual interest in privacy; a seizure deprives the individual of dominion over his or her person or property. <em>United States </em>v. <em>Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 113</a></span> (1984). The “plain-view” doctrine is often considered an exception to the general rule that warrantless searches are presumptively unreasonable,<footnotemark>4</footnotemark> but this characterization overlooks the important difference between searches and seizures.<footnotemark>5</footnotemark> If an article is already in plain view, neither its observation nor its seizure would involve any invasion of privacy. <em>Arizona </em>v. <em>Hicks, </em><page-number citation-index="1" label="134">*134</page-number><span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#325" aria-description="Citation for case: Arizona v. Hicks">480 U. S. 321, 325</a></span> (1987); <em>Illinois </em>v. <em>Andreas, </em><span class="citation" data-id="9429344"><a href="/opinion/111013/illinois-v-andreas/#771" aria-description="Citation for case: Illinois v. Andreas">463 U. S. 765, 771</a></span> (1983). A seizure of the article, however, would obviously invade the owner’s possessory interest. <em>Maryland </em>v. <em>Macon, </em><span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/#469" aria-description="Citation for case: Maryland v. MacOn">472 U. S. 463, 469</a></span> (1985); <em>Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U. S., at 113</a></span>. If “plain view” justifies an exception from an otherwise applicable warrant requirement, therefore, it must be an exception that is addressed to the concerns that are implicated by seizures rather than by searches.</p>
<p id="b176-5">The criteria that generally guide “plain-view” seizures were set forth in <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971). The Court held that the police, in seizing two automobiles parked in plain view on the defendant’s driveway in the course of arresting the defendant, violated the Fourth Amendment. Accordingly, particles of gunpowder that had been subsequently found in vacuum sweepings from one of the cars could not be introduced in evidence against the defendant. The State endeavored to justify the seizure of the automobiles, and their subsequent search at the police station, on four different grounds, including the “plain-view” doctrine.<footnotemark>6</footnotemark> The scope of that doctrine as it had developed in earlier cases was fairly summarized in these three paragraphs from Justice Stewart’s opinion:</p>
<blockquote id="b176-6">“It is well established that under certain circumstances the police may seize evidence in plain view without a warrant. But it is important to keep in mind that, in the vast majority of cases, <em>any </em>evidence seized by the police will be in plain view, at least at the moment of seizure. The problem with the ‘plain-view’ doctrine has been to identify the circumstances in which plain view <page-number citation-index="1" label="135">*135</page-number>has legal significance rather than being simply the normal concomitant of any search, legal or illegal.</blockquote>
<blockquote id="b177-5">“An example of the applicability of the ‘plain-view’ doctrine is the situation in which the police have a warrant to search a given area for specified objects, and in the course of the search come across some other article of incriminating character. Cf. <em>Go-Bart Importing Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#358" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 358</a></span> [(1931)]; <em>United States </em>v. <em>Lefkowitz, </em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#465" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 465</a></span> [(1932)]; <em>Steele </em>v. <em>United States, </em><span class="citation" data-id="100621"><a href="/opinion/100621/steele-v-united-states-no-1/" aria-description="Citation for case: Steele v. United States No. 1">267 U. S. 498</a></span> [(1925)]; <em>Stanley </em>v. <em>Georgia, </em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/#571" aria-description="Citation for case: Stanley v. Georgia">394 U. S. 557, 571</a></span> [(1969)] (Stewart, J., concurring in result). Where the initial intrusion that brings the police within plain view of such an article is supported, not by a warrant, but by one of the recognized exceptions to the warrant requirement, the seizure is also legitimate. Thus the police may inadvertently come across evidence while in ‘hot pursuit’ of a fleeing suspect. <em>Warden </em>v. <em>Hayden, </em>[<span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967)]; cf. <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> [(1924)]. And an object that comes into view during a search incident to arrest that is appropriately limited in scope under existing law may be seized without a warrant. <em>Chimel </em>v. <em>California, </em>395 U. S. [752,] 762-763 [(1969)]. Finally, the ‘plain-view’ doctrine has been applied where a police officer is not searching for evidence against the accused, but nonetheless inadvertently comes across an incriminating object. <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U. S. 234</a></span> [(1968)]; <em>Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731</a></span> [(1969)]; <em>Ker </em>v. <em>California, </em>374 U. S. [23,] 43 [(1963)]. Cf. <em>Lewis </em>v. <em>United States, </em><span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/" aria-description="Citation for case: Lewis v. United States">385 U. S. 206</a></span> [(1966)].</blockquote>
<blockquote id="b177-6">“What the ‘plain-view’ cases have in common is that the police officer in each of them had a prior justification for an intrusion in the course of which he came inadvertently across a piece of evidence incriminating the accused. The doctrine serves to supplement the prior justification—whether it be a warrant for- another object, <page-number citation-index="1" label="136">*136</page-number>hot pursuit, search incident to lawful arrest, or some other legitimate reason for being present unconnected with a search directed against the accused—and permits the warrantless seizure. Of course, the extension of the original justification is legitimate only where it is immediately apparent to the police that they have evidence before them; the ‘plain-view’ doctrine may not be used to extend a general exploratory search from one object to another until something incriminating at last emerges.” <em>Id., </em>at 465-466 (footnote omitted).</blockquote>
<p id="b178-5">Justice Stewart then described the two limitations on the doctrine that he found implicit in its rationale: First, that “plain view <em>alone </em>is never enough to justify the warrantless seizure of evidence,” <em>id., </em>at 468; and second, that “the discovery of evidence in plain view must be inadvertent.” <em>Id., </em>at 469.</p>
<p id="b178-6">Justice Stewart’s analysis of the “plain-view” doctrine did not command a majority, and a plurality of the Court has since made clear that the discussion is “not a binding precedent.” <em>Texas </em>v. <em>Brown, </em><span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#737" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 737</a></span> (1983) (opinion of Rehnquist, J.). Justice Harlan, who concurred in the Court’s judgment and in its response to the dissenting opinions, <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#473" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 473-484, 490-493</a></span>, did not join the plurality’s discussion of the “plain-view” doctrine. See <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#464" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 464-473</a></span>. The decision nonetheless is a binding precedent. Before discussing the second limitation, which is implicated in this case, it is therefore necessary to explain why the first adequately supports the Court’s judgment.</p>
<p id="b178-7">It is, of course, an essential predicate to any valid warrantless seizure of incriminating evidence that the officer did not violate the Fourth Amendment in arriving at the place from which the evidence could be plainly viewed. There are, moreover, two additional conditions that must be satisfied to justify the warrantless seizure. First, not only must the item be in plain view; its incriminating character must also be “immediately apparent.” <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#466" aria-description="Citation for case: Coolidge v. New Hampshire"><em>Id., </em>at 466</a></span>; see also <em>Arizona </em>v. <page-number citation-index="1" label="137">*137</page-number><em>Hicks, </em><span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#326" aria-description="Citation for case: Arizona v. Hicks">480 U. S., at 326-327</a></span>. Thus, in <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span>, </em>the cars were obviously in plain view, but their probative value remained uncertain until after the interiors were swept and examined microscopically. Second, not only must the officer be lawfully located in a place from which the object can be plainly seen, but he or she must also have a lawful right of access to the object itself.<footnotemark>7</footnotemark> As the United States has suggested, Justice Harlan’s vote in <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>may have rested on the fact that the seizure of the cars was accomplished by means of a warrantless trespass on the defendant’s property.<footnotemark>8</footnotemark> In all events, we are satisfied that the absence of inadvertence was not essential to the Court’s rejection of the State’s “plain-view” argument in <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span>.</em></p>
<p id="b179-10">III</p>
<p id="b179-3">Justice Stewart concluded that the inadvertence requirement was necessary to avoid a violation of the express constitutional requirement that a valid warrant must particularly describe the things to be seized. He explained:</p>
<blockquote id="b179-4">“The rationale of the exception to the warrant requirement, as just stated, is that a plain-view seizure will not turn an initially valid (and therefore limited) search into <page-number citation-index="1" label="138">*138</page-number>a ‘general’ one, while the inconvenience of procuring a warrant to cover an inadvertent discovery is great. But where the discovery is anticipated, where the police know in advance the location of the evidence and intend to seize it, the situation is altogether different. The requirement of a warrant to seize imposes no inconvenience whatever, or at least none which is constitutionally cognizable in a legal system that regards warrantless searches as <em>‘per se </em>unreasonable’ in the absence of ‘exigent circumstances.’</blockquote>
<blockquote id="b180-5">“If the initial intrusion is bottomed upon a warrant that fails to mention a particular object, though the police know its location and intend to seize it, then there is a violation of the express constitutional requirement of ‘Warrants . . . particularly describing . . . [the] things to be seized.’” <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#469" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 469-471</a></span>.</blockquote>
<p id="b180-6">We find two flaws in this reasoning. First, evenhanded law enforcement is best achieved by the application of objective standards of conduct, rather than standards that depend upon the subjective state of mind of the officer. The fact that an officer is interested in an item of evidence and fully expects to find it in the course of a search should not invalidate its seizure if the search is confined in area and duration by the terms of a warrant or a valid exception to the warrant requirement. If the officer has knowledge approaching certainty that the item will be found, we see no reason why he or she would deliberately omit a particular description of the item to be seized from the application for a search warrant.<footnotemark>9</footnotemark> Specification of the additional item could only permit the offi<page-number citation-index="1" label="139">*139</page-number>cer to expand the scope of the search. On the other hand, if he or she has a valid warrant to search for one item and merely a suspicion concerning the second, whether or not it amounts to probable cause, we fail to see why that suspicion should immunize the second item from seizure if it is found during a lawful search for the first. The hypothetical case put by Justice White in his concurring and dissenting opinion in <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>is instructive:</p>
<blockquote id="b181-5">“Let us suppose officers secure a warrant to search a house for a rifle. While staying well within the range of a rifle search, they discover two photographs of the murder victim, both in plain sight in the bedroom. Assume also that the discovery of the one photograph was inadvertent but finding the other was anticipated. The Court would permit the seizure of only one of the photographs. But in terms of the ‘minor’ peril to Fourth Amendment values there is surely no difference between these two photographs: the interference with possession is the same in each case and the officers’ appraisal of the photograph they expected to see is no less reliable than their judgment about the other. And in both situations the actual inconvenience and danger to evidence remain identical if the officers must depart and secure a warrant.” <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#516" aria-description="Citation for case: Coolidge v. New Hampshire"><em>Id., </em>at 516</a></span>.</blockquote>
<p id="b181-6">Second, the suggestion that the inadvertence requirement is necessary to prevent the police from conducting general searches, or from converting specific warrants into general warrants, is not persuasive because that interest is already served by the requirements that no warrant issue unless it “particularly describ[es] the place to be searched and the persons or things to be seized,” see <em>Maryland </em>v. <em>Garrison, </em><span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#84" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79, 84</a></span> (1987); <em>Steele </em>v. <em>United States No. 1, </em><span class="citation" data-id="100621"><a href="/opinion/100621/steele-v-united-states-no-1/#503" aria-description="Citation for case: Steele v. United States No. 1">267 U. S. 498, 503</a></span> (1925),<footnotemark>10</footnotemark> and that a warrantless search be circum<page-number citation-index="1" label="140">*140</page-number>scribed by the exigencies which justify its initiation. See, <em>e. g., Maryland </em>v. <em>Buie, </em><span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#332" aria-description="Citation for case: Maryland v. Buie">494 U. S. 325, 332-334</a></span> (1990); <em>Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 393</a></span> (1978). Scrupulous adherence to these requirements serves the interests in limiting the area and duration of the search that the inadvertence requirement inadequately protects. Once those commands have been satisfied and the officer has a lawful right of access, however, no additional Fourth Amendment interest is furthered by requiring that the discovery of evidence be inadvertent. If the scope of the search exceeds that permitted by the terms of a validly issued warrant or the character of the relevant exception from the warrant requirement, the subsequent seizure is unconstitutional without more. Thus, in the case of a search incident to a lawful arrest, “[i]f the police stray outside the scope of an authorized <em>Chimel </em>search they are already in violation of the Fourth Amendment, and evidence so seized will be excluded; adding a second reason for excluding evidence hardly seems worth the candle.” <em>Coolidge, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#517" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 517</a></span> (White, J., concurring and dissenting). Similarly, the object of a warrantless search of an automobile also defines its scope:</p>
<blockquote id="b182-5">“The scope of a warrantless search of an automobile thus is not defined by the nature of the container in which the contraband is secreted. Rather, it is defined by the object of the search and the places in which there is probable cause to believe that it may be found. Just as probable cause to believe that a stolen lawnmower may be found in a garage will not support a warrant to search an upstairs bedroom, probable cause to believe <page-number citation-index="1" label="141">*141</page-number>that undocumented aliens are being transported in a van will not justify a warrantless search of a suitcase. Probable cause to believe that a container placed in the trunk of a taxi contains contraband or evidence does not justify a search of the entire cab.” <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 824</a></span> (1982).</blockquote>
<p id="b183-5">In this case, the scope of the search was not enlarged in the slightest by the omission of any reference to the weapons in the warrant. Indeed, if the three rings and other items named in the warrant had been found at the outset—or if petitioner had them in his possession and had responded to the warrant by producing them immediately—no search for weapons could have taken place. Again, Justice White’s concurring and dissenting opinion in <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>is instructive:</p>
<blockquote id="b183-6">“Police with a warrant for a rifle may search only places where rifles might be and must terminate the search once the rifle is found; the inadvertence rule will in no way reduce the number of places into which they may lawfully look.” <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#517" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 517</a></span>.</blockquote>
<p id="b183-7">As we have already suggested, by hypothesis the seizure of an object in plain view does not involve an intrusion on privacy. <footnotemark><em>11</em></footnotemark><em> </em>If the interest in privacy has been invaded, the violation must have occurred before the object came into plain view and there is no need for an inadvertence limitation on seizures to condemn it. The prohibition against general searches and general warrants serves primarily as a protection against unjustified intrusions on privacy. But reliance <page-number citation-index="1" label="142">*142</page-number>on privacy concerns that support that prohibition is misplaced when the inquiry concerns the scope of an exception that merely authorizes an officer with a lawful right of access to an item to seize it without a warrant.</p>
<p id="b184-7">In this case the items seized from petitioner’s home were discovered during a lawful search authorized by a valid warrant. When they were discovered, it was immediately apparent to the officer that they constituted incriminating evidence. He had probable cause, not only to obtain a warrant to search for the stolen property, but also to believe that the weapons and handguns had been used in the crime he was investigating. The search was authorized by the warrant; the seizure was authorized by the “plain-view” doctrine. The judgment is affirmed.</p>
<p id="b184-8">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b173-7"> Although the officer viewed other handguns and rifles, he did not seize them because there was no probable cause to believe they were associated with criminal activity. App. 30; see <em>Arizona </em>v. <em>Hicks, </em><span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#327" aria-description="Citation for case: Arizona v. Hicks">480 U. S. 321, 327</a></span> (1987).</p>
</footnote>
<footnote label="2">
<p id="b173-8"> “In <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span>, </em>the police arrested a murder suspect in his house and thereupon seized his automobile and searched it later at the police station, <page-number citation-index="1" label="132">*132</page-number>finding physical evidence that the victim had been inside the vehicle. The record disclosed that the police had known for some time of the probable role of the car in the crime, and there were no ‘exigent circumstances’ to justify a warrantless search. Accordingly, the plurality opinion of Justice Stewart concluded that the seizure could not be justified on the theory that the vehicle was itself the ‘instrumentality’ of the crime and was discovered ‘in plain view’ of the officers. Justice Stewart was of the opinion that the ‘plain-view’ doctrine is applicable only to the <em>inadvertent </em>discovery of incriminating evidence.</p>
<p id="Adm">“If the plurality opinion in <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>were entitled to binding effect as precedent, we would have difficulty distinguishing its holding from the instant case, for the discovery of petitioner’s car was no more ‘inadvertent’ than in <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span>. </em>However, that portion of Justice Stewart’s plurality opinion which proposed the adoption of new restrictions to the ‘plain-view’ rule was signed by only four members of the court (Stewart, J., Douglas, J., Brennan, J., and Marshall, J.). Although concurring in the judgment, Justice Harlan declined to join in that portion of the opinion, and the four remaining justices expressly disagreed with Justice Stewart on this point.” <em>North </em>v. <em>Superior Court, 8 </em>Cal. 3d, at 307-308, <span class="citation" data-id="9577161"><a href="/opinion/1239224/north-v-superior-court/#1308" aria-description="Citation for case: North v. Superior Court">502 P. 2d, at 1308</a></span> (citations omitted).</p>
</footnote>
<footnote label="3">
<p id="b174-7"> See, <em>e. g., Wolfenbarger </em>v. <em>Williams, </em><span class="citation" data-id="8952961"><a href="/opinion/8961764/wolfenbarger-v-williams/" aria-description="Citation for case: Wolfenbarger v. Williams">826 F. 2d 930</a></span> (CA10 1987); <em>United States </em>v. <em>$10,000 in United States Currency, </em><span class="citation" data-id="8937180"><a href="/opinion/8946555/united-states-v-10000-in-united-states-currency/" aria-description="Citation for case: United States v. $10,000 in United States Currency">780 F. 2d 213</a></span> (CA2 1986); <em>United States </em>v. <em>Roberts, </em><span class="citation" data-id="9467742"><a href="/opinion/388408/united-states-v-james-willis-roberts/" aria-description="Citation for case: United States v. James Willis Roberts">644 F. 2d 683</a></span> (CA8), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/821/">449 U. S. 821</a></span> (1980); <em>United States </em>v. <em>Antill, </em><span class="citation" data-id="374770"><a href="/opinion/374770/united-states-v-barry-jay-antill/" aria-description="Citation for case: United States v. Barry Jay Antill">615 F. 2d 648</a></span> (CA5 1980); <em>Terry </em>v. <em>State, </em><span class="citation" data-id="7821649"><a href="/opinion/7876118/terry-v-state/" aria-description="Citation for case: Terry v. State">271 Ark. 715</a></span>, <span class="citation" data-id="7821649"><a href="/opinion/7876118/terry-v-state/" aria-description="Citation for case: Terry v. State">610 S. W. 2d 272</a></span> (App. 1981); <em>State </em>v. <em>Johnson, </em><span class="citation" data-id="1433513"><a href="/opinion/1433513/state-v-johnson/" aria-description="Citation for case: State v. Johnson">17 Wash. App. 153</a></span>, <span class="citation" data-id="1433513"><a href="/opinion/1433513/state-v-johnson/" aria-description="Citation for case: State v. Johnson">561 P. 2d 701</a></span> (1977); <em>Commonwealth </em>v. <em>Cefalo, </em><span class="citation" data-id="2089205"><a href="/opinion/2089205/commonwealth-v-cefalo/" aria-description="Citation for case: Commonwealth v. Cefalo">381 Mass. 319</a></span>, <span class="citation" data-id="2089205"><a href="/opinion/2089205/commonwealth-v-cefalo/" aria-description="Citation for case: Commonwealth v. Cefalo">409 N. E. 2d 719</a></span> (1980); <em>State </em>v. <em>Sanders, </em><span class="citation" data-id="1097946"><a href="/opinion/1097946/state-v-sanders/" aria-description="Citation for case: State v. Sanders">431 So. 2d 1034</a></span> (Fla. App. 1983); <em>State </em>v. <em>Galloway, </em><span class="citation" data-id="1165264"><a href="/opinion/1165264/state-v-galloway/" aria-description="Citation for case: State v. Galloway">232 Kan. 87</a></span>, <span class="citation" data-id="1165264"><a href="/opinion/1165264/state-v-galloway/" aria-description="Citation for case: State v. Galloway">652 P. 2d 673</a></span> (1982); <em>Clark </em>v. <em>State, </em><span class="citation" data-id="2209113"><a href="/opinion/2209113/clark-v-state/" aria-description="Citation for case: Clark v. State">498 N. E. 2d 918</a></span> (Ind. 1986); <em>State </em>v. <em>Eiseman, </em><span class="citation" data-id="2404406"><a href="/opinion/2404406/state-v-eiseman/#380" aria-description="Citation for case: State v. Eiseman">461 A. 2d 369, 380</a></span> (R. I. 1983); <em>State </em>v. <em>McColgan, </em><span class="citation" data-id="9665448"><a href="/opinion/1659679/state-v-mccolgan/" aria-description="Citation for case: State v. McColgan">631 S. W. 2d 151</a></span> (Tenn. Crim. App. 1981); <em>Tucker </em>v. <em>State, </em><span class="citation" data-id="1196703"><a href="/opinion/1196703/tucker-v-state/" aria-description="Citation for case: Tucker v. State">620 P. 2d 1314</a></span> (Okla. Crim. App. 1980); <em>State </em>v. <em>Dingle, </em>279 S. C. 278, <span class="citation" data-id="1289643"><a href="/opinion/1289643/state-v-dingle/" aria-description="Citation for case: State v. Dingle">306 S. E. 2d 223</a></span> (1983). See also the cases cited in the Appendices to Justice Brennan’s dissenting opinion, <em>post, </em>at 149-153. At least two other state courts have agreed with the California Supreme Court. See <em>State </em>v. <em>Pontier, </em><span class="citation" data-id="9533958"><a href="/opinion/1128971/state-v-pontier/#712" aria-description="Citation for case: State v. Pontier">95 Idaho 707, 712</a></span>, <span class="citation" data-id="9533958"><a href="/opinion/1128971/state-v-pontier/#974" aria-description="Citation for case: State v. Pontier">518 P. 2d 969, 974</a></span> (1974); <em>State </em>v. <em>Romero, </em><span class="citation" data-id="1119261"><a href="/opinion/1119261/state-v-romero/" aria-description="Citation for case: State v. Romero">660 P. 2d 715</a></span> (Utah 1983).</p>
</footnote>
<footnote label="4">
<p id="b175-6"> “We reaffirm the basic rule of Fourth Amendment jurisprudence stated by Justice Stewart for a unanimous Court in <em>Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#390" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 390</a></span> [(1978)]:</p>
<p id="b175-7">“‘The Fourth Amendment proscribes all unreasonable searches and seizures, and it is a cardinal principle that “searches conducted outside the judicial process, without prior approval by judge or magistrate, are <em>per se </em>unreasonable under the Fourth Amendment—subject only to a few specifically established and well-delineated exceptions.” <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> [(1967)] (footnotes omitted).’” <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 824-825</a></span> (1982).</p>
</footnote>
<footnote label="5">
<p id="b175-8"> “It is important to distinguish ‘plain view,’ as used in <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>to justify <em>seizure </em>of an object, from an officer’s mere observation of an item left in plain view. Whereas the latter generally involves no Fourth Amendment search, see <em>infra, </em>at 740; <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), the former generally does implicate the Amendment’s limitations upon seizures of personal property.” <em>Texas </em>v. <em>Brown, </em><span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#738" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 738, n. 4</a></span> (1983) (opinion of Rehnquist, J.).</p>
</footnote>
<footnote label="6">
<p id="b176-7"> The State primarily contended that the seizures were authorized by a warrant issued by the attorney general, but the Court held the warrant invalid because it had not been issued by “a neutral and detached magistrate.” <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#449" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 449-453</a></span>. In addition, the State relied on three exceptions from the warrant requirement: (1) search incident to arrest; (2) the automobile exception; and (3) the “plain-view” doctrine. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#453" aria-description="Citation for case: Coolidge v. New Hampshire"><em>Id., </em>at 453-473</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b179-5"> “This is simply a corollary of the familiar principle discussed above, that no amount of probable cause can justify a warrantless search or seizure absent ‘exigent circumstances.’ Incontrovertible testimony of the senses that an incriminating object is on premises belonging to a criminal suspect may establish the fullest possible measure of probable cause. But even where the object is contraband, this Court has repeatedly stated and enforced the basic rule that the police may not enter and make a warrantless seizure. <em>Taylor </em>v. <em>United States, </em><span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">286 U. S. 1</a></span> [(1932)]; <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> [(1948)]; <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span> [(1948)]; <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#497" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 497-498</a></span> [(1958)]; <em>Chapman </em>v. <em>United States, </em><span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span> [(1961)]; <em>Trupiano </em>v. <em>United States, </em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span> [(1948)].” <em>Coolidge, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#468" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 468</a></span>.</p>
<p id="b179-6">We have since applied the same rule to the arrest of a person in his home. See <em>Minnesota </em>v. <em>Olson, </em><span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">495 U. S. 91</a></span> (1990); <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980).</p>
</footnote>
<footnote label="8">
<p id="b179-7"> See Brief for United States as <em>Amicus Curiae </em>7, n. 4.</p>
</footnote>
<footnote label="9">
<p id="b180-7"> “If the police have probable cause to search for a photograph as well as a rifle and they proceed to seek a warrant, they could have no possible motive for deliberately including the rifle but omitting the photograph. Quite the contrary is true. Only oversight or careless mistake would explain the omission in the warrant application if the police were convinced they had probable cause to search for the photograph.” <em>Coolidge, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#517" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 517</a></span> (White, J., concurring and dissenting).</p>
</footnote>
<footnote label="10">
<p id="b181-7"> “The Warrant Clause of the Fourth Amendment categorically prohibits the issuance of any warrant except one ‘particularly describing the place to <page-number citation-index="1" label="140">*140</page-number>be searched and the persons or things to be seized.’ The manifest purpose of this particularity requirement was to prevent general searches. By limiting the authorization to search to the specific areas and things for which there is probable cause to search, the requirement ensures that the search will be carefully tailored to its justifications, and will not take on the character of the wide-ranging exploratory searches the Framers intended to prohibit.” <em>Maryland </em>v. <em>Garrison, </em><span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#84" aria-description="Citation for case: Maryland v. Garrison">480 U. S., at 84</a></span>.</p>
</footnote>
<footnote label="11">
<p id="b183-8"> Even if the item is a container, its seizure does not compromise the interest in preserving the privacy of its contents because it may only be opened pursuant to either a search warrant, see <em>Smith </em>v. <em>Ohio, </em><span class="citation" data-id="9431948"><a href="/opinion/112392/smith-v-ohio/" aria-description="Citation for case: Smith v. Ohio">494 U. S. 541</a></span> (1990); <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#701" aria-description="Citation for case: United States v. Place">462 U. S. 696, 701</a></span> (1983); <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span> (1979); <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977); <em>United States v. Van Leeuwen, </em><span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S. 249</a></span> (1970); <em>Ex parte Jackson, </em><span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727, 733</a></span> (1878), or one of the well-delineated exceptions to the warrant requirement. See <em>Colorado </em>v. <em>Bertine, </em><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">479 U. S. 367</a></span> (1987); <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982).</p>
</footnote>
</opinion>
```

---
