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

## GROUP: _overhaul2/lake/cases/Henry v. United States (1959).json  (`lake-record`, 7 assertions)

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
{"assertion_id": "3f8f1bc363f4a605", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Henry v. United States (1959)"}, "payload": {"all": [{"cite": "361 U.S. 98", "page": "98", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "361"}, {"cite": "80 S. Ct. 168", "page": "168", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "80"}, {"cite": "4 L. Ed. 2d 134", "page": "134", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "4"}, {"cite": "1959 U.S. LEXIS 89", "page": "89", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1959"}], "display": "361 U.S. 98", "official": {"cite": "361 U.S. 98", "page": "98", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "361"}, "official_selection_present": true, "record_id": "Henry v. United States (1959)"}}
{"assertion_id": "1d84db4cfd1eada3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-104b", "record_id": "Henry v. United States (1959)"}, "payload": {"fragment": "#:~:text=The%20fact%20that%20packages%20have", "page": null, "pin_id": "pin-104b", "pinpoint_status": "star-verified", "quote": "The fact that packages have been stolen does not make every man who carries a package subject to arrest nor the package subject to seizure.", "quote_fidelity": "matched", "record_id": "Henry v. United States (1959)", "star_marker": "104"}}
{"assertion_id": "2c642c8da35edc02", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-103", "record_id": "Henry v. United States (1959)"}, "payload": {"fragment": "#:~:text=When%20the%20officers%20interrupted%20the", "page": null, "pin_id": "pin-103", "pinpoint_status": "star-verified", "quote": "When the officers interrupted the two men and restricted their liberty of movement, the arrest, for purposes of this case, was complete. It is, therefore, necessary to determine whether at or before that time they had reasonable cause to believe that a crime had been committed.", "quote_fidelity": "matched", "record_id": "Henry v. United States (1959)", "star_marker": "103"}}
{"assertion_id": "390b82467b84f060", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-104", "record_id": "Henry v. United States (1959)"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-104", "pinpoint_status": "slip-only", "quote": "[A]n arrest is not justified by what the subsequent search discloses. Under our system suspicion is not enough for an officer to lay hands on a citizen.", "quote_fidelity": "mismatch", "record_id": "Henry v. United States (1959)", "star_marker": null}}
{"assertion_id": "8994b96d3617869d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-102", "record_id": "Henry v. United States (1959)"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-102", "pinpoint_status": "slip-only", "quote": "--- # Henry v. United States (1959) *361 U.S. 98 (1959)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background FBI agents investigating the theft of whisky from an interstate shipment had a vague tip implicating Henry's companion, Pierotti. Over a period of surveillance the agents watched the two men drive to an alley in a residential section, load cartons into a car, drive off, return, and load more cartons. The agents stopped the car, and only afterward — looking through the open door — saw cartons bearing interstate shipping labels, which they then searched and seized. Henry was convicted of unlawful possession of stolen goods and moved to suppress the cartons as the fruit of an arrest without probable cause. ## Issue At what point was Henry arrested, and whether the facts known to the agents at that moment amounted to probable cause for a warrantless arrest. ## Rule Probable cause is measured at the moment of the seizure by the facts then known.", "quote_fidelity": "mismatch", "record_id": "Henry v. United States (1959)", "star_marker": null}}
{"assertion_id": "fd258239dc09764c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-103b", "record_id": "Henry v. United States (1959)"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-103b", "pinpoint_status": "slip-only", "quote": "Riding in the car, stopping in an alley, picking up packages, driving away — these were all acts that were outwardly innocent.", "quote_fidelity": "mismatch", "record_id": "Henry v. United States (1959)", "star_marker": null}}
{"assertion_id": "1f12652be7d39153", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Henry v. United States (1959)"}, "payload": {"as_of_content": "1959-11-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Henry v. United States (1959)", "scope_note": "Good law. Probable cause for a warrantless arrest is measured by the facts known to the officer at the moment of arrest; outwardly innocent conduct does not supply it, and an arrest cannot be justified by what the ensuing search reveals. Year-suffixed filename to disambiguate from the reversed-party case United States v. Henry, 447 U.S. 264 (1980).", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/Hernandez v. Mesa.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Hernandez v. Mesa
type: case
citation: "589 U.S. 93 (2020)"
parallel_cite: "140 S. Ct. 735; 206 L. Ed. 2d 29"
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2020
date_decided: ""
docket: 17-1678
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
  opinion_url: "https://www.courtlistener.com/opinion/9231296/hernandez-v-mesa/"
  cluster_id: 9231296
  opinion_id: null
  identity_checked: true
lake:
  record_id: Hernandez v. Mesa
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Suing Federal Officers]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Bivens v. Six Unknown Named Agents]]"
tags:
  - case
  - bivens
  - cross-border-shooting
  - national-security
  - federal-officer-liability
  - section-1983
holding: "Bivens does not extend to a damages claim arising from a cross-border shooting: such a claim arises in a markedly new context with foreign-relations and national-security implications, and Congress's reluctance to create remedies for tortious conduct abroad counsels against implying a cause of action."
---

# Hernandez v. Mesa

*589 U.S. 93 (2020)* (No. 17-1678) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9231296 → opinion 9226104; quote string-matched to the CL opinion text 2026-07-07 (CL text carries S. Ct. star-pagination, 140 S. Ct. 735). S9 promotes. -->

## Background
Sergio Adrián Hernández Güereca, a fifteen-year-old Mexican national, was playing in the concrete culvert that separates El Paso, Texas, from Ciudad Juárez, Mexico. U.S. Border Patrol Agent Jesus Mesa, standing on the U.S. side, fired across the border and killed Hernández, who was on the Mexican side. Hernández's parents sued Mesa for damages under *[[Bivens v. Six Unknown Named Agents|Bivens]]*, alleging violations of the Fourth and Fifth Amendments. The [[Reading and Citing Cases#en-banc|en banc]] Fifth Circuit refused to recognize a *[[Bivens v. Six Unknown Named Agents|Bivens]]* remedy, and the Supreme Court granted review.

## Issue
Whether *[[Bivens v. Six Unknown Named Agents|Bivens]]* should be extended to provide a damages remedy against a federal officer for a cross-border shooting.

## Rule
Recognizing an implied *[[Bivens v. Six Unknown Named Agents|Bivens]]* cause of action is disfavored, and separation-of-powers principles require caution before extending it to any "new context" — one that differs meaningfully from the three settings in which the Court has recognized a *[[Bivens v. Six Unknown Named Agents|Bivens]]* remedy. A cross-border shooting is such a new context, and it carries foreign-relations and national-security implications that a court is ill-suited to weigh. The Court accordingly held: "Because of the distinctive characteristics of cross-border shooting claims, we refuse to extend *Bivens* into this new field." — 589 U.S. at 99. ^pin-99

## Application
A cross-border shooting is "by definition an international incident" affecting the interests of two nations, and such incidents are addressed through diplomatic channels (here, the U.S.–Mexico Border Violence Prevention Council and bilateral Human Rights Dialogue) that a judicially created damages remedy could disrupt. Congress, moreover, has been "notably hesitant" to create causes of action for tortious conduct abroad — declining, for instance, to make the Federal Tort Claims Act reach injuries in foreign countries. Because these special factors counsel hesitation, and no equally strong reason favors a judicial remedy, the Court refused to imply a *[[Bivens v. Six Unknown Named Agents|Bivens]]* action; it declined to decide the antecedent Fourth Amendment question.

## Conclusion
The judgment of the Fifth Circuit was **affirmed**. Alito, J., delivered the opinion of the Court; Thomas, J., joined by Gorsuch, J., concurred (urging reconsideration of *[[Bivens v. Six Unknown Named Agents|Bivens]]* itself); Ginsburg, J., joined by Breyer, Sotomayor, and Kagan, JJ., dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Hernández v. Mesa* is part of the Court's line — with *[[Ziglar v. Abbasi]]* (2017) and *[[Egbert v. Boule]]* (2022) — sharply confining *[[Bivens v. Six Unknown Named Agents|Bivens]]* and refusing to extend implied damages remedies against federal officers into new, sensitive contexts.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Hernández v. Mesa*, 589 U.S. 93 (2020)](https://www.courtlistener.com/opinion/9231296/hernandez-v-mesa/) — pinpoint: 99 (holding, Opinion of the Court); CL text carries S. Ct. star-pagination (140 S. Ct. 735), the holding sitting just before the confirmed *741 page-label; quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "062a60562846ec86", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Hernandez v. Mesa"}, "payload": {"all": [{"cite": "589 U.S. 93", "page": "93", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "589"}, {"cite": "140 S. Ct. 735", "page": "735", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "140"}, {"cite": "206 L. Ed. 2d 29", "page": "29", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "206"}], "display": "589 U.S. 93", "official": {"cite": "589 U.S. 93", "page": "93", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "589"}, "official_selection_present": true, "record_id": "Hernandez v. Mesa"}}
{"assertion_id": "681916f89a73b2cc", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Hernandez v. Mesa"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Hernandez v. Mesa", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Hernandez v. Mesa

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hernandez v. Mesa",
  "status": "under_review",
  "identity": {
    "case_name": "Hernandez v. Mesa",
    "case_name_short": "Hernandez",
    "case_name_full": "Jesus C. HERNANDEZ v. Jesus MESA, Jr.",
    "input_case_name": "Hernandez v. Mesa",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2020,
    "docket": "17-1678",
    "cluster_id": 9231296,
    "lead_opinion_id": 9226104,
    "sibling_ids": [],
    "absolute_url": "/opinion/9231296/hernandez-v-mesa/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "589 U.S. 93",
      "volume": "589",
      "reporter": "U.S.",
      "page": "93",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "140 S. Ct. 735",
        "volume": "140",
        "reporter": "S. Ct.",
        "page": "735",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "206 L. Ed. 2d 29",
        "volume": "206",
        "reporter": "L. Ed. 2d",
        "page": "29",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "589 U.S. 93",
        "volume": "589",
        "reporter": "U.S.",
        "page": "93",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "140 S. Ct. 735",
        "volume": "140",
        "reporter": "S. Ct.",
        "page": "735",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "206 L. Ed. 2d 29",
        "volume": "206",
        "reporter": "L. Ed. 2d",
        "page": "29",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "589 U.S. 93",
    "official_selection": {
      "court_class": "scotus",
      "selected": "589 U.S. 93",
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
    "date_created": "2026-07-06T12:09:39Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:09:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:09:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:09:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:09:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "hernandez-v-mesa--9231296",
      "to_record_id": "Hernandez v. Mesa",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Hernandez v. Mesa (truncated)

```
<opinion type="majority">
<author id="p-7">Justice ALITO delivered the opinion of the Court.</author>
<p id="p-8"><a class="page-label" data-citation-index="1" data-label="739" href="#p739" id="p739">*739</a>We are asked in this case to extend <em>Bivens v. Six Unknown Fed. Narcotics Agents</em> , <extracted-citation case-ids="12027206" index="0" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. 388</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="1" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="2" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">29 L.Ed.2d 619</a></span></extracted-citation> (1971), and create a damages remedy for a cross-border shooting. As we have made clear in many prior cases, however, the Constitution's separation of powers requires us to exercise caution before extending <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> to a new "context," and a claim based on a cross-border shooting arises in a context that is markedly new. Unlike any previously recognized <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> claim, a cross-border shooting claim has foreign relations and national security implications. In addition, Congress has been notably hesitant to create claims based on allegedly tortious conduct abroad. Because of the distinctive characteristics of cross-border shooting claims, we refuse to extend <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> into this new field.</p>
<p id="p-9">I</p>
<p id="p-10">The facts of this tragic case are set forth in our earlier opinion in this matter, <a class="page-label" data-citation-index="1" data-label="740" href="#p740" id="p740">*740</a><em>Hernández v.</em> <em>Mesa</em> , 582 U.S. ----, <extracted-citation case-ids="12605122" index="3" url="https://cite.case.law/s-ct/137/2003/"><span class="citation" data-id="9876889"><a href="/opinion/4403795/hernandez-v-mesa/" aria-description="Citation for case: Hernandez v. Mesa">137 S.Ct. 2003</a></span></extracted-citation>, <extracted-citation case-ids="12605122" index="4" url="https://cite.case.law/s-ct/137/2003/"><span class="citation" data-id="9876889"><a href="/opinion/4403795/hernandez-v-mesa/" aria-description="Citation for case: Hernandez v. Mesa">198 L.Ed.2d 625</a></span></extracted-citation> (2017) (<em>per curiam</em> ). Sergio Adrián Hernández Güereca, a 15-year-old Mexican national, was with a group of friends in a concrete culvert that separates El Paso, Texas, from Ciudad Juarez, Mexico. The border runs through the center of the culvert, which was designed to hold the waters of the Rio Grande River but is now largely dry. Border Patrol Agent Jesus Mesa, Jr., detained one of Hernández's friends who had run onto the United States' side of the culvert. After Hernández, who was also on the United States' side, ran back across the culvert onto Mexican soil, Agent Mesa fired two shots at Hernández; one struck and killed him on the other side of the border.</p>
<p id="p-11">Petitioners and Agent Mesa disagree about what Hernández and his friends were doing at the time of shooting. According to petitioners, they were simply playing a game, running across the culvert, touching the fence on the U.S. side, and then running back across the border. According to Agent Mesa, Hernández and his friends were involved in an illegal border crossing attempt, and they pelted him with rocks.<footnotemark>1</footnotemark></p>
<p id="p-12">The shooting quickly became an international incident, with the United States and Mexico disagreeing about how the matter should be handled. On the United States' side, the Department of Justice conducted an investigation. When it finished, the Department, while expressing regret over Hernández's death, concluded that Agent Mesa had not violated Customs and Border Patrol policy or training, and it declined to bring charges or take other action against him. Mexico was not and is not satisfied with the U.S. investigation. It requested that Agent Mesa be extradited to face criminal charges in a Mexican court, a request that the United States has denied.</p>
<p id="p-13">Petitioners, Hernández's parents, were also dissatisfied</p>
<p id="p-14">and therefore brought suit for damages in the United States District Court for the Western District of Texas. Among other claims, they sought recovery of damages under <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> , alleging that Mesa violated Hernández's Fourth and Fifth Amendment rights. The District Court granted Mesa's motion to dismiss, and the Court of Appeals for the Fifth Circuit sitting en banc has twice affirmed this dismissal.</p>
<p id="p-15">On the first occasion, the court held that Hernández was not entitled to Fourth Amendment protection because he was "a Mexican citizen who had no 'significant voluntary connection' to the United States" and "was on Mexican soil at the time he was shot." <em>Hernandez v. United States</em> , <extracted-citation case-ids="4182853" index="5" url="https://cite.case.law/f3d/785/117/#p119"><span class="citation" data-id="9807043"><a href="/opinion/2796556/jesus-hernandez-v-unknown-named-agents-et/" aria-description="Citation for case: Jesus Hernandez v. Unknown Named Agents, et">785 F.3d 117</a></span></extracted-citation>, 119 (C.A.5 2015) (<em>per curiam</em> ). It further concluded that Mesa was entitled to qualified immunity on petitioners' Fifth Amendment claim. <em><extracted-citation case-ids="4182853" index="6" url="https://cite.case.law/f3d/785/117/#p119"><span class="citation" data-id="9807043"><a href="/opinion/2796556/jesus-hernandez-v-unknown-named-agents-et/" aria-description="Citation for case: Jesus Hernandez v. Unknown Named Agents, et">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="4182853" index="6" url="https://cite.case.law/f3d/785/117/#p119"> at 120</extracted-citation>.</p>
<p id="p-16">After granting review, we vacated the Fifth Circuit's decision and remanded the case, instructing the court "to consider how the reasoning and analysis" of <em>Ziglar v.</em> <em>Abbasi</em> , 582 U.S. ----, <extracted-citation case-ids="12604999" index="7" url="https://cite.case.law/s-ct/137/1843/"><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">137 S.Ct. 1843</a></span></extracted-citation>, <extracted-citation case-ids="12604999" index="8" url="https://cite.case.law/s-ct/137/1843/"><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">198 L.Ed.2d 290</a></span></extracted-citation> (2017), our most recent explication of <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> , "[might] bear on this case." <em><span class="citation" data-id="9876889"><a href="/opinion/4403795/hernandez-v-mesa/" aria-description="Citation for case: Hernandez v. Mesa">Hernández</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 2006. We found it "appropriate for the Court of Appeals, rather than this Court, to address the <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> question in the first instance." <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Ibid.</a></span></em> And with the <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> issue unresolved, we thought it "imprudent" to resolve the "sensitive"</p>
<p id="p-17"><a class="page-label" data-citation-index="1" data-label="741" href="#p741" id="p741">*741</a>question whether the Fourth Amendment applies to a cross-border shooting. <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Ibid.</a></span></em> In addition, while rejecting the ground on which the Court of Appeals had held that Agent Mesa was entitled to qualified immunity, we declined to decide whether he was entitled to qualified immunity on a different ground or whether petitioners' claim was cognizable under the Fifth Amendment. <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Id.,</a></span></em> at ---- - ----, 137 S.Ct., at 2006-2008</p>
<p id="p-18">On remand, the en banc Fifth Circuit evaluated petitioners' case in light of <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> and refused to recognize a <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> claim for a cross-border shooting. <extracted-citation case-ids="12516361" index="9" url="https://cite.case.law/f3d/885/811/"><span class="citation" data-id="8410662"><a href="/opinion/8439846/hernandez-v-mesa/" aria-description="Citation for case: Hernandez v. Mesa">885 F.3d 811</a></span></extracted-citation> (C.A.5 2018). The court reasoned that such an incident presents a " 'new context' " and that multiple factors-including the incident's relationship to foreign affairs and national security, the extraterritorial aspect of the case, and Congress's "repeated refusals" to create a damages remedy for injuries incurred on foreign soil-counseled against an extension of <em>Bivens</em> . <extracted-citation case-ids="12516361" index="10" url="https://cite.case.law/f3d/885/811/"><span class="citation" data-id="8410662"><a href="/opinion/8439846/hernandez-v-mesa/" aria-description="Citation for case: Hernandez v. Mesa">885 F.3d at 816</a></span>-823</extracted-citation>.</p>
<p id="p-19">We granted certiorari, 587 U.S. ----, <extracted-citation case-ids="12621056,12621057,12621058,12621059,12621060" index="11" url="https://cite.case.law/s-ct/139/2636/"><span class="citation multiple-matches"><a href="/c/S.Ct./139/2636/">139 S.Ct. 2636</a></span></extracted-citation>, <extracted-citation case-ids="12621056,12621186,12621058,12621061,12621063,12621227,12621228" index="12" url="https://cite.case.law/l-ed-2d/204/282/"><span class="citation multiple-matches"><a href="/c/L.Ed.2d/204/282/">204 L.Ed.2d 282</a></span></extracted-citation> (2019), and now affirm.</p>
<p id="p-20">II</p>
<p id="p-21">In <em>Bivens v. Six Unknown Fed. Narcotics Agents</em> , <extracted-citation case-ids="12027206" index="13" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. 388</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="14" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="15" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">29 L.Ed.2d 619</a></span></extracted-citation>, the Court broke new ground by holding that a person claiming to be the victim of an unlawful arrest and search could bring a Fourth Amendment claim for damages against the responsible agents even though no federal statute authorized such a claim. The Court subsequently extended <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> to cover two additional constitutional claims: in <em>Davis v. Passman</em> , <extracted-citation case-ids="1532130" index="16" url="https://cite.case.law/us/442/228/"><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">442 U.S. 228</a></span></extracted-citation>, <extracted-citation case-ids="1532130" index="17" url="https://cite.case.law/us/442/228/"><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">99 S.Ct. 2264</a></span></extracted-citation>, <extracted-citation case-ids="1532130" index="18" url="https://cite.case.law/us/442/228/"><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">60 L.Ed.2d 846</a></span></extracted-citation> (1979), a former congressional staffer's Fifth Amendment claim of dismissal based on sex, and in <em>Carlson v. Green</em> , <extracted-citation case-ids="6180250" index="19" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">446 U.S. 14</a></span></extracted-citation>, <extracted-citation case-ids="6180250" index="20" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">100 S.Ct. 1468</a></span></extracted-citation>, <extracted-citation case-ids="6180250" index="21" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">64 L.Ed.2d 15</a></span></extracted-citation> (1980), a federal prisoner's Eighth Amendment claim for failure to provide adequate medical treatment. After those decisions, however, the Court changed course.</p>
<p id="p-22"><em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> , <em><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">Davis</a></span></em> , and <em><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">Carlson</a></span></em> were the products of an era when the Court routinely inferred "causes of action" that were "not explicit" in the text of the provision that was allegedly violated. <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1855. As <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> recounted:</p>
<blockquote id="p-23">"During this '<em>ancien regime</em> ,' ... the Court assumed it to be a proper judicial function to 'provide such remedies as are necessary to make effective' a statute's purpose .... Thus, as a routine matter with respect to statutes, the Court would imply causes of action not explicit in the statutory text itself." <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Ibid.</a></span></em> (quoting <em>Alexander v. Sandoval</em> , <extracted-citation case-ids="9301210" index="22" url="https://cite.case.law/us/532/275/#p287"><span class="citation" data-id="9795078"><a href="/opinion/2620697/alexander-v-sandoval/" aria-description="Citation for case: Alexander v. Sandoval">532 U.S. 275</a></span></extracted-citation>, 287, <extracted-citation case-ids="9301210" index="23" url="https://cite.case.law/us/532/275/#p287"><span class="citation" data-id="9795078"><a href="/opinion/2620697/alexander-v-sandoval/" aria-description="Citation for case: Alexander v. Sandoval">121 S.Ct. 1511</a></span></extracted-citation>, <extracted-citation case-ids="9301210" index="24" url="https://cite.case.law/us/532/275/#p287"><span class="citation" data-id="9795078"><a href="/opinion/2620697/alexander-v-sandoval/" aria-description="Citation for case: Alexander v. Sandoval">149 L.Ed.2d 517</a></span></extracted-citation> (2001) ; <em>J. I. Case Co. v. Borak</em> , <extracted-citation case-ids="6170359" index="25" url="https://cite.case.law/us/377/426/#p433"><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">377 U.S. 426</a></span></extracted-citation>, 433, <extracted-citation case-ids="6170359" index="26" url="https://cite.case.law/us/377/426/#p433"><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">84 S.Ct. 1555</a></span></extracted-citation>, <extracted-citation case-ids="6170359" index="27" url="https://cite.case.law/us/377/426/#p433"><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">12 L.Ed.2d 423</a></span></extracted-citation> (1964) ).</blockquote>
<p id="p-24"><em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> extended this practice to claims based on the Constitution itself. 582 U.S., at ----, 137 S.Ct., at 1855 ; <em>Bivens</em> , <extracted-citation case-ids="12027206" index="28" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. at 402</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="29" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation> (Harlan, J., concurring in judgment) (Court can infer availability of damages when, "in its view, damages are necessary to effectuate" the "policy underpinning the substantive provisio[n]").</p>
<p id="p-25">In later years, we came to appreciate more fully the tension between this practice and the Constitution's separation of legislative and judicial power. The Constitution grants legislative power to Congress; this Court and the lower federal courts, by contrast, have only "judicial Power." Art. III, § 1. But when a court recognizes an implied claim for damages on the ground that doing so furthers the "purpose" of the law, the court risks arrogating legislative power. No law " 'pursues <a class="page-label" data-citation-index="1" data-label="742" href="#p742" id="p742">*742</a>its purposes at all costs.' " <em>American Express Co. v. Italian Colors Restaurant</em> , <extracted-citation case-ids="12698468" index="30" url="https://cite.case.law/us/570/228/#p234"><span class="citation" data-id="9515841"><a href="/opinion/903973/american-express-co-v-italian-colors-restaurant/" aria-description="Citation for case: American Express Co. v. Italian Colors Restaurant">570 U.S. 228</a></span></extracted-citation>, 234, <extracted-citation case-ids="12698468" index="31" url="https://cite.case.law/us/570/228/#p234"><span class="citation" data-id="9515841"><a href="/opinion/903973/american-express-co-v-italian-colors-restaurant/" aria-description="Citation for case: American Express Co. v. Italian Colors Restaurant">133 S.Ct. 2304</a></span></extracted-citation>, <extracted-citation case-ids="12698468" index="32" url="https://cite.case.law/us/570/228/#p234"><span class="citation" data-id="9515841"><a href="/opinion/903973/american-express-co-v-italian-colors-restaurant/" aria-description="Citation for case: American Express Co. v. Italian Colors Restaurant">186 L.Ed.2d 417</a></span></extracted-citation> (2013) (quoting <em>Rodriguez v. United States</em> , <extracted-citation case-ids="1131066" index="33" url="https://cite.case.law/us/480/522/#p525"><span class="citation" data-id="111840"><a href="/opinion/111840/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">480 U.S. 522</a></span></extracted-citation>, 525-526, <extracted-citation case-ids="1131066" index="34" url="https://cite.case.law/us/480/522/#p525"><span class="citation" data-id="111840"><a href="/opinion/111840/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">107 S.Ct. 1391</a></span></extracted-citation>, <extracted-citation case-ids="1131066" index="35" url="https://cite.case.law/us/480/522/#p525"><span class="citation" data-id="111840"><a href="/opinion/111840/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">94 L.Ed.2d 533</a></span></extracted-citation> (1987) (<em>per curiam</em> )). Instead, lawmaking involves balancing interests and often demands compromise. See <em>Board of Governors, FRS v. Dimension Financial Corp.</em> , <extracted-citation case-ids="6205521" index="36" url="https://cite.case.law/us/474/361/#p373"><span class="citation" data-id="111557"><a href="/opinion/111557/board-of-governors-of-the-federal-reserve-system-v-dimension-financial/" aria-description="Citation for case: Board of Governors of the Federal Reserve System v....">474 U.S. 361</a></span></extracted-citation>, 373-374, <extracted-citation case-ids="6205521" index="37" url="https://cite.case.law/us/474/361/#p373"><span class="citation" data-id="111557"><a href="/opinion/111557/board-of-governors-of-the-federal-reserve-system-v-dimension-financial/" aria-description="Citation for case: Board of Governors of the Federal Reserve System v....">106 S.Ct. 681</a></span></extracted-citation>, <extracted-citation case-ids="6205521" index="38" url="https://cite.case.law/us/474/361/#p373"><span class="citation" data-id="111557"><a href="/opinion/111557/board-of-governors-of-the-federal-reserve-system-v-dimension-financial/" aria-description="Citation for case: Board of Governors of the Federal Reserve System v....">88 L.Ed.2d 691</a></span></extracted-citation> (1986). Thus, a lawmaking body that enacts a provision that creates a right or prohibits specified conduct may not wish to pursue the provision's purpose to the extent of authorizing private suits for damages. For this reason, finding that a damages remedy is implied by a provision that makes no reference to that remedy may upset the careful balance of interests struck by the lawmakers. See <em><extracted-citation case-ids="6205521" index="39" url="https://cite.case.law/us/474/361/#p373"><span class="citation" data-id="111557"><a href="/opinion/111557/board-of-governors-of-the-federal-reserve-system-v-dimension-financial/" aria-description="Citation for case: Board of Governors of the Federal Reserve System v....">ibid.</a></span></extracted-citation></em></p>
<p id="p-26">This problem does not exist when a common-law court, which exercises a degree of lawmaking authority, fleshes out the remedies available for a common-law tort. Analogizing <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> to the work of a common-law court, petitioners and some of their <em>amici</em> make much of the fact that common-law claims against federal officers for intentional torts were once available. See, <em>e.g.</em> , Brief for Petitioners 10-20. But <em>Erie R. Co. v. Tompkins</em> , <extracted-citation case-ids="10687" index="40" url="https://cite.case.law/us/304/64/#p78"><span class="citation" data-id="9418969"><a href="/opinion/103012/erie-railroad-v-tompkins/" aria-description="Citation for case: Erie Railroad v. Tompkins">304 U.S. 64</a></span></extracted-citation>, 78, <extracted-citation case-ids="10687" index="41" url="https://cite.case.law/us/304/64/#p78"><span class="citation" data-id="9418969"><a href="/opinion/103012/erie-railroad-v-tompkins/" aria-description="Citation for case: Erie Railroad v. Tompkins">58 S.Ct. 817</a></span></extracted-citation>, <extracted-citation case-ids="10687" index="42" url="https://cite.case.law/us/304/64/#p78"><span class="citation" data-id="9418969"><a href="/opinion/103012/erie-railroad-v-tompkins/" aria-description="Citation for case: Erie Railroad v. Tompkins">82 L.Ed. 1188</a></span></extracted-citation> (1938), held that "[t]here is no federal general common law," and therefore federal courts today cannot fashion new claims in the way that they could before 1938. See <em>Alexander</em> , <extracted-citation case-ids="9301210" index="43" url="https://cite.case.law/us/532/275/#p287"><span class="citation" data-id="9795078"><a href="/opinion/2620697/alexander-v-sandoval/" aria-description="Citation for case: Alexander v. Sandoval">532 U.S. at 287</a></span></extracted-citation>, <extracted-citation case-ids="9301210" index="44" url="https://cite.case.law/us/532/275/#p287"><span class="citation" data-id="9795078"><a href="/opinion/2620697/alexander-v-sandoval/" aria-description="Citation for case: Alexander v. Sandoval">121 S.Ct. 1511</a></span></extracted-citation> (" 'Raising up causes of action where a statute has not created them may be a proper function for common-law courts, but not for federal tribunals' ").</p>
<p id="p-27">With the demise of federal general common law, a federal court's authority to recognize a damages remedy must rest at bottom on a statute enacted by Congress, see <em><extracted-citation case-ids="9301210" index="45" url="https://cite.case.law/us/532/275/#p287"><span class="citation" data-id="9795078"><a href="/opinion/2620697/alexander-v-sandoval/" aria-description="Citation for case: Alexander v. Sandoval">id.,</a></span></extracted-citation></em><extracted-citation case-ids="9301210" index="45" url="https://cite.case.law/us/532/275/#p287"> at 286</extracted-citation>, <extracted-citation case-ids="9301210" index="46" url="https://cite.case.law/us/532/275/#p287"><span class="citation" data-id="9795078"><a href="/opinion/2620697/alexander-v-sandoval/" aria-description="Citation for case: Alexander v. Sandoval">121 S.Ct. 1511</a></span></extracted-citation> ("private rights of action to enforce federal law must be created by Congress"), and no statute expressly creates a <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> remedy. Justice Harlan's <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> concurrence argued that this power is inherent in the grant of federal question jurisdiction, see <extracted-citation case-ids="12027206" index="47" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. at 396</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="48" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation> (majority opinion); <em><extracted-citation case-ids="12027206" index="49" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">id.</a></span></extracted-citation></em> , at 405, <extracted-citation case-ids="12027206" index="50" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation> (opinion of Harlan, J.), but our later cases have demanded a clearer manifestation of congressional intent, see <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ---- - ----, 137 S.Ct., at 1856-1858.</p>
<p id="p-28">In both statutory and constitutional cases, our watchword is caution. For example, in <em>Jesner v.</em> <em>Arab Bank, PLC</em> , 584 U.S. ----, ---- - ----, <extracted-citation case-ids="12611257" index="51" url="https://cite.case.law/s-ct/138/1386/#p1391"><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">138 S.Ct. 1386</a></span></extracted-citation>, 1391-1403, <extracted-citation case-ids="12611257" index="52" url="https://cite.case.law/s-ct/138/1386/#p1391"><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">200 L.Ed.2d 612</a></span></extracted-citation> (2018) we expressed doubt about our authority to recognize any causes of action not expressly created by Congress. See also <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span>,</em> 582 U.S.<em>,</em> at ----, 137 S.Ct., at 1856 ("If the statute does not itself so provide, a private cause of action will not be created through judicial mandate"). And we declined to recognize a claim against a foreign corporation under the Alien Tort Statute. <em><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">Jesner</a></span></em> , 584 U.S., at ----, <extracted-citation case-ids="12611257" index="53" url="https://cite.case.law/s-ct/138/1386/#p1391"><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">138 S.Ct., at 1408</a></span></extracted-citation>.</p>
<p id="p-29">In constitutional cases, we have been at least equally reluctant to create new causes of action. We have recognized that Congress is best positioned to evaluate "whether, and the extent to which, monetary and other liabilities should be imposed upon individual officers and employees of the Federal Government" based on constitutional torts. <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1856. We have stated that expansion of <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> is "a 'disfavored' judicial activity," 582 U.S., at ----, 137 S.Ct., at 1857 (quoting <em>Ashcroft v. Iqbal</em> , <extracted-citation case-ids="3653744" index="54" url="https://cite.case.law/us/556/662/#p675"><span class="citation" data-id="9435339"><a href="/opinion/145875/ashcroft-v-iqbal/" aria-description="Citation for case: Ashcroft v. Iqbal">556 U.S. 662</a></span></extracted-citation>, 675, <extracted-citation case-ids="3653744" index="55" url="https://cite.case.law/us/556/662/#p675"><span class="citation" data-id="9435339"><a href="/opinion/145875/ashcroft-v-iqbal/" aria-description="Citation for case: Ashcroft v. Iqbal">129 S.Ct. 1937</a></span></extracted-citation>, <extracted-citation case-ids="3653744" index="56" url="https://cite.case.law/us/556/662/#p675"><span class="citation" data-id="9435339"><a href="/opinion/145875/ashcroft-v-iqbal/" aria-description="Citation for case: Ashcroft v. Iqbal">173 L.Ed.2d 868</a></span></extracted-citation> (2009) ), and have gone so far as to observe that if "the Court's three <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> cases [had] been ... decided today," it is doubtful that we would have <a class="page-label" data-citation-index="1" data-label="743" href="#p743" id="p743">*743</a>reached the same result, 582 U.S., at ----, 137 S.Ct., at 1856. And for almost 40 years, we have consistently rebuffed requests to add to the claims allowed under <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> . See 582 U.S., at ----, 137 S.Ct., at 1863-1864 ; <em>Minneci v. Pollard</em> , <extracted-citation case-ids="12445441,12185990" index="57" url="https://cite.case.law/us/565/118/"><span class="citation" data-id="7268271"><a href="/opinion/7350292/minneci-v-pollard/" aria-description="Citation for case: Minneci v. Pollard">565 U.S. 118</a></span></extracted-citation>, <extracted-citation case-ids="12445441,12185990" index="58" url="https://cite.case.law/us/565/118/"><span class="citation" data-id="7268271"><a href="/opinion/7350292/minneci-v-pollard/" aria-description="Citation for case: Minneci v. Pollard">132 S.Ct. 617</a></span></extracted-citation>, <extracted-citation case-ids="12445441,12185990" index="59" url="https://cite.case.law/us/565/118/"><span class="citation" data-id="7268271"><a href="/opinion/7350292/minneci-v-pollard/" aria-description="Citation for case: Minneci v. Pollard">181 L.Ed.2d 606</a></span></extracted-citation> (2012) ; <em>Wilkie v. Robbins</em> , <extracted-citation case-ids="3573210" index="60" url="https://cite.case.law/us/551/537/"><span class="citation" data-id="9435015"><a href="/opinion/145705/wilkie-v-robbins/" aria-description="Citation for case: Wilkie v. Robbins">551 U.S. 537</a></span></extracted-citation>, <extracted-citation case-ids="3573210" index="61" url="https://cite.case.law/us/551/537/"><span class="citation" data-id="9435015"><a href="/opinion/145705/wilkie-v-robbins/" aria-description="Citation for case: Wilkie v. Robbins">127 S.Ct. 2588</a></span></extracted-citation>, <extracted-citation case-ids="3573210" index="62" url="https://cite.case.law/us/551/537/"><span class="citation" data-id="9435015"><a href="/opinion/145705/wilkie-v-robbins/" aria-description="Citation for case: Wilkie v. Robbins">168 L.Ed.2d 389</a></span></extracted-citation> (2007) ; <em>Correctional Services Corp. v. Malesko</em> , <extracted-citation case-ids="9107996" index="63" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">534 U.S. 61</a></span></extracted-citation>, <extracted-citation case-ids="9107996" index="64" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">122 S.Ct. 515</a></span></extracted-citation>, <extracted-citation case-ids="9107996" index="65" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">151 L.Ed.2d 456</a></span></extracted-citation> (2001) ; <em>FDIC v. Meyer</em> , <extracted-citation case-ids="230419" index="66" url="https://cite.case.law/us/510/471/"><span class="citation" data-id="112931"><a href="/opinion/112931/federal-deposit-insurance-v-meyer/" aria-description="Citation for case: Federal Deposit Insurance v. Meyer">510 U.S. 471</a></span></extracted-citation>, <extracted-citation case-ids="230419" index="67" url="https://cite.case.law/us/510/471/"><span class="citation" data-id="112931"><a href="/opinion/112931/federal-deposit-insurance-v-meyer/" aria-description="Citation for case: Federal Deposit Insurance v. Meyer">114 S.Ct. 996</a></span></extracted-citation>, <extracted-citation case-ids="230419" index="68" url="https://cite.case.law/us/510/471/"><span class="citation" data-id="112931"><a href="/opinion/112931/federal-deposit-insurance-v-meyer/" aria-description="Citation for case: Federal Deposit Insurance v. Meyer">127 L.Ed.2d 308</a></span></extracted-citation> (1994) ; <em>Schweiker v. Chilicky</em> , <extracted-citation case-ids="1775175" index="69" url="https://cite.case.law/us/487/412/"><span class="citation" data-id="9431421"><a href="/opinion/112132/schweiker-v-chilicky/" aria-description="Citation for case: Schweiker v. Chilicky">487 U.S. 412</a></span></extracted-citation>, <extracted-citation case-ids="1775175" index="70" url="https://cite.case.law/us/487/412/"><span class="citation" data-id="9431421"><a href="/opinion/112132/schweiker-v-chilicky/" aria-description="Citation for case: Schweiker v. Chilicky">108 S.Ct. 2460</a></span></extracted-citation>, <extracted-citation case-ids="1775175" index="71" url="https://cite.case.law/us/487/412/"><span class="citation" data-id="9431421"><a href="/opinion/112132/schweiker-v-chilicky/" aria-description="Citation for case: Schweiker v. Chilicky">101 L.Ed.2d 370</a></span></extracted-citation> (1988) ; <em>United States v. Stanley</em> , <extracted-citation case-ids="28195" index="72" url="https://cite.case.law/us/483/669/"><span class="citation" data-id="9431121"><a href="/opinion/111954/united-states-v-stanley/" aria-description="Citation for case: United States v. Stanley">483 U.S. 669</a></span></extracted-citation>, <extracted-citation case-ids="28195" index="73" url="https://cite.case.law/us/483/669/"><span class="citation" data-id="9431121"><a href="/opinion/111954/united-states-v-stanley/" aria-description="Citation for case: United States v. Stanley">107 S.Ct. 3054</a></span></extracted-citation>, <extracted-citation case-ids="28195" index="74" url="https://cite.case.law/us/483/669/"><span class="citation" data-id="9431121"><a href="/opinion/111954/united-states-v-stanley/" aria-description="Citation for case: United States v. Stanley">97 L.Ed.2d 550</a></span></extracted-citation> (1987) ; <em>Chappell v. Wallace</em> , <extracted-citation case-ids="6187620" index="75" url="https://cite.case.law/us/462/296/"><span class="citation" data-id="110960"><a href="/opinion/110960/chappell-v-wallace/" aria-description="Citation for case: Chappell v. Wallace">462 U.S. 296</a></span></extracted-citation>, <extracted-citation case-ids="6187620" index="76" url="https://cite.case.law/us/462/296/"><span class="citation" data-id="110960"><a href="/opinion/110960/chappell-v-wallace/" aria-description="Citation for case: Chappell v. Wallace">103 S.Ct. 2362</a></span></extracted-citation>, <extracted-citation case-ids="6187620" index="77" url="https://cite.case.law/us/462/296/"><span class="citation" data-id="110960"><a href="/opinion/110960/chappell-v-wallace/" aria-description="Citation for case: Chappell v. Wallace">76 L.Ed.2d 586</a></span></extracted-citation> (1983) ; <em>Bush v. Lucas</em> , <extracted-citation case-ids="6188608" index="78" url="https://cite.case.law/us/462/367/"><span class="citation" data-id="9429240"><a href="/opinion/110965/bush-v-lucas/" aria-description="Citation for case: Bush v. Lucas">462 U.S. 367</a></span></extracted-citation>, <extracted-citation case-ids="6188608" index="79" url="https://cite.case.law/us/462/367/"><span class="citation" data-id="9429240"><a href="/opinion/110965/bush-v-lucas/" aria-description="Citation for case: Bush v. Lucas">103 S.Ct. 2404</a></span></extracted-citation>, <extracted-citation case-ids="6188608" index="80" url="https://cite.case.law/us/462/367/"><span class="citation" data-id="9429240"><a href="/opinion/110965/bush-v-lucas/" aria-description="Citation for case: Bush v. Lucas">76 L.Ed.2d 648</a></span></extracted-citation> (1983).</p>
<p id="p-30">When asked to extend <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> , we engage in a two-step inquiry. We first inquire whether the request involves a claim that arises in a "new context" or involves a "new category of defendants." <em>Malesko</em> , <extracted-citation case-ids="9107996" index="81" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">534 U.S. at 68</a></span></extracted-citation>, <extracted-citation case-ids="9107996" index="82" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">122 S.Ct. 515</a></span></extracted-citation>. And our understanding of a "new context" is broad. We regard a context as "new" if it is "different in a meaningful way from previous <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> cases decided by this Court." <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1859.</p>
<p id="p-31">When we find that a claim arises in a new context, we proceed to the second step and ask whether there are any " ' "special factors [that] counse[l] hesitation" ' " about granting the extension. <em>Id.</em> , at ----, 137 S.Ct., at 1857 (quoting <em>Carlson</em> , <extracted-citation case-ids="6180250" index="83" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">446 U.S. at 18</a></span></extracted-citation>, <extracted-citation case-ids="6180250" index="84" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">100 S.Ct. 1468</a></span></extracted-citation>, in turn quoting <em>Bivens</em> , <extracted-citation case-ids="12027206" index="85" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. at 396</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="86" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation> ). If there are-that is, if we have reason to pause before applying <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> in a new context or to a new class of defendants-we reject the request.</p>
<p id="p-32">We have not attempted to "create an exhaustive list" of factors that may provide a reason not to extend <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> , but we have explained that "central to [this] analysis" are "separation-of-powers principles." <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1857. We thus consider the risk of interfering with the authority of the other branches, and we ask whether "there are sound reasons to think Congress might doubt the efficacy or necessity of a damages remedy," <em>id.,</em> at ----, 137 S.Ct., at 1858, and "whether the Judiciary is well suited, absent congressional action or instruction, to consider and weigh the costs and benefits of allowing a damages action to proceed," <em>id.,</em> at ----, 137 S.Ct., at 1858</p>
<p id="p-33">III</p>
<p id="p-34">A</p>
<p id="p-35">The <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> claims in this case assuredly arise in a new context. Petitioners contend that their Fourth and Fifth Amendment claims do not involve a new context because <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> and <em><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">Davis</a></span></em> involved claims under those same two amendments, but that argument rests on a basic misunderstanding of what our cases mean by a new context. A claim may arise in a new context even if it is based on the same constitutional provision as a claim in a case in which a damages remedy was previously recognized. Compare <em>Carlson</em> , <extracted-citation case-ids="6180250" index="87" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">446 U.S. at 16</a></span>-18</extracted-citation>, <extracted-citation case-ids="6180250" index="88" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">100 S.Ct. 1468</a></span></extracted-citation> (allowing <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> remedy for an Eighth Amendment claim for failure to provide adequate medical treatment), with <em>Malesko</em> , <extracted-citation case-ids="9107996" index="89" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">534 U.S. at 71</a></span>-74</extracted-citation>, <extracted-citation case-ids="9107996" index="90" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">122 S.Ct. 515</a></span></extracted-citation> (declining to create a <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> remedy in similar circumstances because the suit was against a private prison operator, not federal officials). And once we look beyond the constitutional provisions invoked in <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> , <em><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">Davis</a></span></em> , and the present case, it is glaringly obvious that petitioners' claims involve a new context, <em>i.e.</em> , one that is meaningfully different.</p>
<p id="p-36"><a class="page-label" data-citation-index="1" data-label="744" href="#p744" id="p744">*744</a><em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> concerned an allegedly unconstitutional arrest and search carried out in New York City, <extracted-citation case-ids="12027206" index="91" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. at 389</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="92" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation> ; <em><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">Davis</a></span></em> concerned alleged sex discrimination on Capitol Hill, <extracted-citation case-ids="1532130" index="93" url="https://cite.case.law/us/442/228/"><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">442 U.S. at 230</a></span></extracted-citation>, <extracted-citation case-ids="1532130" index="94" url="https://cite.case.law/us/442/228/"><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">99 S.Ct. 2264</a></span></extracted-citation>. There is a world of difference between those claims and petitioners' cross-border shooting claims, where "the risk of disruptive intrusion by the Judiciary into the functioning of other branches" is significant. <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1860 ; see Parts III-B and III-C, <em>infra</em> .</p>
<p id="p-37">Because petitioners assert claims that arise in a new context, we must proceed to the next step and ask whether there are factors that counsel hesitation. As we will explain, there are multiple, related factors that raise warning flags.</p>
<p id="p-38">B</p>
<p id="p-39">The first is the potential effect on foreign relations. "The political branches, not the Judiciary, have the responsibility and institutional capacity to weigh foreign-policy concerns." <em><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">Jesner</a></span></em> , 584 U.S., at ----, <extracted-citation case-ids="12611257" index="95" url="https://cite.case.law/s-ct/138/1386/#p1391"><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">138 S.Ct., at 1403</a></span></extracted-citation>. Indeed, we have said that "matters relating 'to the conduct of foreign relations ... are so exclusively entrusted to the political branches of government as to be largely immune from judicial inquiry or interference.' " <em>Haig v. Agee</em> , <extracted-citation case-ids="11722549" index="96" url="https://cite.case.law/us/453/280/#p292"><span class="citation" data-id="9428473"><a href="/opinion/110554/haig-v-agee/" aria-description="Citation for case: Haig v. Agee">453 U.S. 280</a></span></extracted-citation>, 292, <extracted-citation case-ids="11722549" index="97" url="https://cite.case.law/us/453/280/#p292"><span class="citation" data-id="9428473"><a href="/opinion/110554/haig-v-agee/" aria-description="Citation for case: Haig v. Agee">101 S.Ct. 2766</a></span></extracted-citation>, <extracted-citation case-ids="11722549" index="98" url="https://cite.case.law/us/453/280/#p292"><span class="citation" data-id="9428473"><a href="/opinion/110554/haig-v-agee/" aria-description="Citation for case: Haig v. Agee">69 L.Ed.2d 640</a></span></extracted-citation> (1981) (quoting <em>Harisiades v. Shaughnessy</em> , <extracted-citation case-ids="641171" index="99" url="https://cite.case.law/us/342/580/#p589"><span class="citation" data-id="9420696"><a href="/opinion/104980/harisiades-v-shaughnessy/" aria-description="Citation for case: Harisiades v. Shaughnessy">342 U.S. 580</a></span></extracted-citation>, 589, <extracted-citation case-ids="641171" index="100" url="https://cite.case.law/us/342/580/#p589"><span class="citation" data-id="9420696"><a href="/opinion/104980/harisiades-v-shaughnessy/" aria-description="Citation for case: Harisiades v. Shaughnessy">72 S.Ct. 512</a></span></extracted-citation>, <extracted-citation index="101" url="https://cite.case.law/citations/?q=96%20L.%20Ed.%20586"><span class="citation no-link">96 L.Ed. 586</span></extracted-citation> (1952) ). "Thus, unless Congress specifically has provided otherwise, courts traditionally have been reluctant to intrude upon the authority of the Executive in [these matters]." <em>Department of Navy v. Egan</em> , <extracted-citation case-ids="601280" index="102" url="https://cite.case.law/us/484/518/#p530"><span class="citation" data-id="9431176"><a href="/opinion/111990/department-of-the-navy-v-egan/" aria-description="Citation for case: Department of the Navy v. Egan">484 U.S. 518</a></span></extracted-citation>, 530, <extracted-citation case-ids="601280" index="103" url="https://cite.case.law/us/484/518/#p530"><span class="citation" data-id="9431176"><a href="/opinion/111990/department-of-the-navy-v-egan/" aria-description="Citation for case: Department of the Navy v. Egan">108 S.Ct. 818</a></span></extracted-citation>, <extracted-citation case-ids="601280" index="104" url="https://cite.case.law/us/484/518/#p530"><span class="citation" data-id="9431176"><a href="/opinion/111990/department-of-the-navy-v-egan/" aria-description="Citation for case: Department of the Navy v. Egan">98 L.Ed.2d 918</a></span></extracted-citation> (1988). We must therefore be especially wary before allowing a <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> remedy that impinges on this arena.</p>
<p id="p-40">A cross-border shooting is by definition an international incident; it involves an event that occurs simultaneously in two countries and affects both countries' interests. Such an incident may lead to a disagreement between those countries, as happened in this case.</p>
<p id="p-41">The United States, through the Executive Branch, which has " 'the lead role in foreign policy,' " <em>Medellín v. Texas</em> , <extracted-citation case-ids="3675774" index="105" url="https://cite.case.law/us/552/491/#p524"><span class="citation" data-id="9435251"><a href="/opinion/145822/medellin-v-texas/" aria-description="Citation for case: Medellin v. Texas">552 U.S. 491</a></span></extracted-citation>, 524, <extracted-citation case-ids="3675774" index="106" url="https://cite.case.law/us/552/491/#p524"><span class="citation" data-id="9435251"><a href="/opinion/145822/medellin-v-texas/" aria-description="Citation for case: Medellin v. Texas">128 S.Ct. 1346</a></span></extracted-citation>, <extracted-citation case-ids="3675774" index="107" url="https://cite.case.law/us/552/491/#p524"><span class="citation" data-id="9435251"><a href="/opinion/145822/medellin-v-texas/" aria-description="Citation for case: Medellin v. Texas">170 L.Ed.2d 190</a></span></extracted-citation> (2008) (alteration omitted), has taken the position that this incident should be handled in a particular way-namely, that Agent Mesa should not face charges in the United States nor be extradited to stand trial in Mexico. As noted, the Executive decided not to take action against Agent Mesa because it found that he "did not act inconsistently with [Border Patrol] policy or training regarding use of force." DOJ Press Release. We presume that Border Patrol policy and training incorporate both the Executive's understanding of the Fourth Amendment's prohibition of unreasonable seizures and the Executive's assessment of circumstances at the border. Thus, the Executive judged Agent Mesa's conduct by what it regards as reasonable conduct by an agent under the circumstances that Mesa faced at the time of the shooting, and based on the application of those standards, it declined to prosecute. The Executive does not want a Mexican criminal court to judge Agent Mesa's conduct by whatever standards would be applicable under Mexican law; nor does it want a jury in a <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> action to apply its own understanding of what constituted reasonable conduct by a Border Patrol agent under the circumstances of this case. Such a jury determination, the Executive claims, would risk the " ' "embarrassment of our government abroad" through "multifarious pronouncements by various departments on one question." ' " Brief for United States as <em>Amicus Curiae</em> 18 (quoting <em>Sanchez-Espinoza v. Reagan</em> , <extracted-citation case-ids="332853,3600966" index="108" url="https://cite.case.law/f2d/770/202/"><span class="citation" data-id="9473867"><a href="/opinion/457042/javier-sanchez-espinoza-v-ronald-wilson-reagan-president-of-the-united/" aria-description="Citation for case: Javier Sanchez-Espinoza v. Ronald Wilson Reagan,...">770 F.2d 202</a></span></extracted-citation>, 209 (C.A.D.C. 1985) (Scalia, J.)).</p>
<p id="p-42"><a class="page-label" data-citation-index="1" data-label="745" href="#p745" id="p745">*745</a>The Government of Mexico has taken a different view of what should be done. It has requested that Agent Mesa be extradited for criminal prosecution in a Mexican court under Mexican law, and it has supported petitioners' <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> suit. In a brief filed in this Court, Mexico suggests that shootings by Border Patrol agents are a persistent problem and argues that the United States has an obligation under international law, specifically Article 6(1) of the International Covenant on Civil and Political Rights, Dec. 19, 1966, S. Treaty Doc. No. 95-20, 999 U. N. T. S. 174, to provide a remedy for the shooting in this case. Brief for Government of United Mexican States as <em>Amicus Curiae</em> 2, 20-22. Mexico states that it "has a responsibility to look after the well-being of its nationals" and that "it is a priority to Mexico to see that the United States provides adequate means to hold the agents accountable and to compensate the victims." <em><extracted-citation case-ids="332853,3600966" index="109" url="https://cite.case.law/f2d/770/202/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Id.</a></span></extracted-citation></em> , at 3.</p>
<p id="p-43">Both the United States and Mexico have legitimate and important interests that may be affected by the way in which this matter is handled. The United States has an interest in ensuring that agents assigned the difficult and important task of policing the border are held to standards and judged by procedures that satisfy United States law and do not undermine the agents' effectiveness and morale. Mexico has an interest in exercising sovereignty over its territory and in protecting and obtaining justice for its nationals. It is not our task to arbitrate between them.</p>
<p id="p-44">In the absence of judicial intervention, the United States and Mexico would attempt to reconcile their interests through diplomacy-and that has occurred. The broad issue of violence along the border, the occurrence of crossborder shootings, and this particular matter have been addressed through diplomatic channels. In 2014, Mexico and the United States established a joint Border Violence Prevention Council, and the two countries have addressed cross-border shootings through the United States-Mexico bilateral Human Rights Dialogue.<footnotemark>2</footnotemark> Following the Justice Department investigation in the present case, the United States reaffirmed its commitment to "work with the Mexican government within existing mechanisms and agreements to prevent future incidents." DOJ Press Release.</p>
<p id="p-45">For these reasons, petitioners' assertion that their claims have "nothing to do with the substance or conduct of U.S. foreign ... policy," Brief for Petitioners 29, is plainly wrong.<footnotemark>3</footnotemark></p>
<p id="p-46">C</p>
<p id="p-47">Petitioners are similarly incorrect in deprecating the Fifth Circuit's conclusion <a class="page-label" data-citation-index="1" data-label="746" href="#p746" id="p746">*746</a>that the issue here implicates an element of national security.</p>
<p id="p-48">One of the ways in which the Executive protects this country is by attempting to control the movement of people and goods across the border, and that is a daunting task. The United States' border with Mexico extends for 1,900 miles, and every day thousands of persons and a large volume of goods enter this country at ports of entry on the southern border.<footnotemark>4</footnotemark> The lawful passage of people and goods in both directions across the border is beneficial to both countries.</p>
<p id="p-49">Unfortunately, there is also a large volume of illegal</p>
<p id="p-50">cross-border traffic. During the last fiscal year, approximately 850,000 persons were apprehended attempting to enter the United States illegally from Mexico,<footnotemark>5</footnotemark> and large quantities of drugs were smuggled across the border.<footnotemark>6</footnotemark> In addition, powerful criminal organizations operating on both sides of the border present a serious law enforcement problem for both countries.<footnotemark>7</footnotemark></p>
<p id="p-51">On the United States' side, the responsibility for attempting to prevent the illegal entry of dangerous persons and goods rests primarily with the U.S. Customs and Border Protection Agency, and one of its main responsibilities is to "detect, respond to, and interdict terrorists, drug smugglers and traffickers, human smugglers and traffickers, and other persons who may undermine the security of the United States." <extracted-citation index="110" url="https://cite.case.law/citations/?q=6%20U.S.C.%20%C2%A7%20211"><span class="citation no-link">6 U.S.C. § 211</span></extracted-citation>(c)(5). While Border Patrol agents often work miles from the border, some, like Agent Mesa, are stationed right at the border and have the responsibility of attempting to prevent illegal entry. For these reasons, the conduct of agents positioned at the border has a clear and strong connection to national security, as the Fifth Circuit understood. <extracted-citation case-ids="12516361" index="111" url="https://cite.case.law/f3d/885/811/"><span class="citation" data-id="8410662"><a href="/opinion/8439846/hernandez-v-mesa/" aria-description="Citation for case: Hernandez v. Mesa">885 F.3d at 819</a></span></extracted-citation>.</p>
<p id="p-52">Petitioners protest that " 'shooting people who are just walking down a street in Mexico' " does not involve national security, Brief for Petitioners 28, but that misses the point. The question is not whether national security requires such conduct-of course, it does not-but whether the Judiciary should alter the framework established by the political branches for addressing cases in which it is alleged that lethal force was unlawfully employed by an agent at the border. Cf. <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1861 (explaining that "[n]ational-security policy is the prerogative of the Congress and President").</p>
<p id="p-53">We have declined to extend <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> where doing so would interfere with the <a class="page-label" data-citation-index="1" data-label="747" href="#p747" id="p747">*747</a>system of military discipline created by statute and regulation, see <em>Chappell</em> , <extracted-citation case-ids="6187620" index="112" url="https://cite.case.law/us/462/296/"><span class="citation" data-id="110960"><a href="/opinion/110960/chappell-v-wallace/" aria-description="Citation for case: Chappell v. Wallace">462 U.S. 296</a></span></extracted-citation>, <extracted-citation case-ids="6187620" index="113" url="https://cite.case.law/us/462/296/"><span class="citation" data-id="110960"><a href="/opinion/110960/chappell-v-wallace/" aria-description="Citation for case: Chappell v. Wallace">103 S.Ct. 2362</a></span></extracted-citation> ; <em>Stanley</em> , <extracted-citation case-ids="28195" index="114" url="https://cite.case.law/us/483/669/"><span class="citation" data-id="9431121"><a href="/opinion/111954/united-states-v-stanley/" aria-description="Citation for case: United States v. Stanley">483 U.S. 669</a></span></extracted-citation>, <extracted-citation case-ids="28195" index="115" url="https://cite.case.law/us/483/669/"><span class="citation" data-id="9431121"><a href="/opinion/111954/united-states-v-stanley/" aria-description="Citation for case: United States v. Stanley">107 S.Ct. 3054</a></span></extracted-citation>, and a similar consideration is applicable here. Since regulating the conduct of agents at the border unquestionably has national security implications, the risk of undermining border security provides reason to hesitate before extending <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> into this field. See <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1861 ("Judicial inquiry into the national-security realm raises 'concerns for the separation of powers' " (quoting <em>Christopher v. Harbury</em> , <extracted-citation case-ids="1254643" index="116" url="https://cite.case.law/us/536/403/#p417"><span class="citation" data-id="9434290"><a href="/opinion/121160/christopher-v-harbury/" aria-description="Citation for case: Christopher v. Harbury">536 U.S. 403</a></span></extracted-citation>, 417, <extracted-citation case-ids="1254643" index="117" url="https://cite.case.law/us/536/403/#p417"><span class="citation" data-id="9434290"><a href="/opinion/121160/christopher-v-harbury/" aria-description="Citation for case: Christopher v. Harbury">122 S.Ct. 2179</a></span></extracted-citation>, <extracted-citation case-ids="1254643" index="118" url="https://cite.case.law/us/536/403/#p417"><span class="citation" data-id="9434290"><a href="/opinion/121160/christopher-v-harbury/" aria-description="Citation for case: Christopher v. Harbury">153 L.Ed.2d 413</a></span></extracted-citation> (2002) )).</p>
<p id="p-54">D</p>
<p id="p-55">Our reluctance to take that step is reinforced by our survey of what Congress has done in statutes addressing related matters. We frequently "loo[k] to analogous statutes for guidance on the appropriate boundaries of judge-made causes of action." <em><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">Jesner</a></span></em> , 584 U.S., at ----, <extracted-citation case-ids="12611257" index="119" url="https://cite.case.law/s-ct/138/1386/#p1391"><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/#1403" aria-description="Citation for case: Jesner v. Arab Bank, PLC">138 S.Ct., at 1403</a></span></extracted-citation> (opinion of Kennedy, J.). When foreign relations are implicated, it "is even more important ... 'to look for legislative guidance before exercising innovative authority over substantive law.' " <em><extracted-citation case-ids="12611257" index="120" url="https://cite.case.law/s-ct/138/1386/#p1391"><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12611257" index="121" url="https://cite.case.law/s-ct/138/1386/#p1391"><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">138 S.Ct., at 1403</a></span></extracted-citation> (quoting <em>Sosa v. Alvarez-Machain</em> , <extracted-citation case-ids="5862480" index="122" url="https://cite.case.law/us/542/692/#p726"><span class="citation" data-id="9434694"><a href="/opinion/137006/sosa-v-alvarez-machain/" aria-description="Citation for case: Sosa v. Alvarez-Machain">542 U.S. 692</a></span></extracted-citation>, 726, <extracted-citation case-ids="5862480" index="123" url="https://cite.case.law/us/542/692/#p726"><span class="citation" data-id="9434694"><a href="/opinion/137006/sosa-v-alvarez-machain/" aria-description="Citation for case: Sosa v. Alvarez-Machain">124 S.Ct. 2739</a></span></extracted-citation>, <extracted-citation case-ids="5862480" index="124" url="https://cite.case.law/us/542/692/#p726"><span class="citation" data-id="9434694"><a href="/opinion/137006/sosa-v-alvarez-machain/" aria-description="Citation for case: Sosa v. Alvarez-Machain">159 L.Ed.2d 718</a></span></extracted-citation> (2004) ). Accordingly, it is "telling," <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1862, that Congress has repeatedly declined to authorize the award of damages for injury inflicted outside our borders.</p>
<p id="p-56">A leading example is <extracted-citation index="125" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation>, which permits the recovery of damages for constitutional violations by officers acting under color of <em>state</em> law. We have described <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> as a "more limited" "federal analog" to § 1983. <em>Hartman v. Moore</em> , <extracted-citation case-ids="3275855" index="126" url="https://cite.case.law/us/547/250/#p254"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. 250</a></span></extracted-citation>, 254, n. 2, <extracted-citation case-ids="3275855" index="127" url="https://cite.case.law/us/547/250/#p254"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="128" url="https://cite.case.law/us/547/250/#p254"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">164 L.Ed.2d 441</a></span></extracted-citation> (2006). It is therefore instructive that Congress chose to make § 1983 available only to "citizen[s] of the United States or other person[s] within the jurisdiction thereof." It would be "anomalous to impute ... a judicially implied cause of action beyond the bounds [Congress has] delineated for [a] comparable express caus[e] of action." <em>Blue Chip Stamps v. Manor Drug Stores</em> , <extracted-citation case-ids="541651" index="129" url="https://cite.case.law/us/421/723/#p736"><span class="citation" data-id="9426100"><a href="/opinion/109267/blue-chip-stamps-v-manor-drug-stores/" aria-description="Citation for case: Blue Chip Stamps v. Manor Drug Stores">421 U.S. 723</a></span></extracted-citation>, 736, <extracted-citation case-ids="541651" index="130" url="https://cite.case.law/us/421/723/#p736"><span class="citation" data-id="9426100"><a href="/opinion/109267/blue-chip-stamps-v-manor-drug-stores/" aria-description="Citation for case: Blue Chip Stamps v. Manor Drug Stores">95 S.Ct. 1917</a></span></extracted-citation>, <extracted-citation case-ids="541651" index="131" url="https://cite.case.law/us/421/723/#p736"><span class="citation" data-id="9426100"><a href="/opinion/109267/blue-chip-stamps-v-manor-drug-stores/" aria-description="Citation for case: Blue Chip Stamps v. Manor Drug Stores">44 L.Ed.2d 539</a></span></extracted-citation> (1975). Thus, the limited scope of § 1983 weighs against recognition of the <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> claim at issue here.</p>
<p id="p-57">Section 1983's express limitation to the claims brought by citizens and persons subject to United States jurisdiction is especially significant, but even if this explicit limitation were lacking, we would presume that § 1983 did not apply abroad. See <em>RJR Nabisco, Inc. v. European Community</em> , 579 U.S. ----, ----, <extracted-citation case-ids="12597929" index="132" url="https://cite.case.law/s-ct/136/2090/#p2100"><span class="citation" data-id="8137991"><a href="/opinion/8176209/rjr-nabisco-inc-v-european-cmty/" aria-description="Citation for case: RJR Nabisco, Inc. v. European Cmty.">136 S.Ct. 2090</a></span></extracted-citation>, 2100, <extracted-citation case-ids="12597929" index="133" url="https://cite.case.law/s-ct/136/2090/#p2100"><span class="citation" data-id="3214778"><a href="/opinion/3214884/rjr-nabisco-inc-v-european-community/" aria-description="Citation for case: RJR Nabisco, Inc. v. European Community">195 L.Ed.2d 476</a></span></extracted-citation> (2016) ("Absent clearly expressed congressional intent to the contrary, federal laws will be construed to have only domestic application"). We presume that statutes do not apply extraterritorially to "ensure that the Judiciary does not erroneously adopt an interpretation of U.S. law that carries foreign policy consequences not clearly intended by the political branches." <em>Kiobel v. Royal Dutch Petroleum Co.</em> , <extracted-citation case-ids="12697039" index="134" url="https://cite.case.law/us/569/108/#p116"><span class="citation" data-id="9506050"><a href="/opinion/858289/kiobel-v-royal-dutch-petroleum-co/" aria-description="Citation for case: Kiobel v. Royal Dutch Petroleum Co.">569 U.S. 108</a></span></extracted-citation>, 116, <extracted-citation case-ids="12697039" index="135" url="https://cite.case.law/us/569/108/#p116"><span class="citation" data-id="9506050"><a href="/opinion/858289/kiobel-v-royal-dutch-petroleum-co/" aria-description="Citation for case: Kiobel v. Royal Dutch Petroleum Co.">133 S.Ct. 1659</a></span></extracted-citation>, <extracted-citation case-ids="12697039" index="136" url="https://cite.case.law/us/569/108/#p116"><span class="citation" data-id="9506050"><a href="/opinion/858289/kiobel-v-royal-dutch-petroleum-co/" aria-description="Citation for case: Kiobel v. Royal Dutch Petroleum Co.">185 L.Ed.2d 671</a></span></extracted-citation> (2013) ; see also <em>EEOC v. Arabian American Oil Co.</em> , <extracted-citation case-ids="11318695" index="137" url="https://cite.case.law/us/499/244/#p248"><span class="citation" data-id="9432237"><a href="/opinion/112565/equal-employment-opportunity-commission-v-arabian-american-oil-co/" aria-description="Citation for case: Equal Employment Opportunity Commission v. Arabian...">499 U.S. 244</a></span></extracted-citation>, 248, <extracted-citation case-ids="11318695" index="138" url="https://cite.case.law/us/499/244/#p248"><span class="citation" data-id="9432237"><a href="/opinion/112565/equal-employment-opportunity-commission-v-arabian-american-oil-co/" aria-description="Citation for case: Equal Employment Opportunity Commission v. Arabian...">111 S.Ct. 1227</a></span></extracted-citation>, <extracted-citation case-ids="11318695" index="139" url="https://cite.case.law/us/499/244/#p248"><span class="citation" data-id="9432237"><a href="/opinion/112565/equal-employment-opportunity-commission-v-arabian-american-oil-co/" aria-description="Citation for case: Equal Employment Opportunity Commission v. Arabian...">113 L.Ed.2d 274</a></span></extracted-citation> (1991).</p>
<p id="p-58">If this danger provides a reason for caution when Congress has enacted a statute but has not provided expressly whether it applies abroad, we have even greater reason for hesitation in deciding whether to extend a judge-made cause of action beyond our borders. "[T]he danger of unwarranted judicial interference in the conduct of foreign policy is magnified" where "the question is not what Congress has <a class="page-label" data-citation-index="1" data-label="748" href="#p748" id="p748">*748</a>done but instead what courts may do." <em>Kiobel</em> , <extracted-citation case-ids="12697039" index="140" url="https://cite.case.law/us/569/108/#p116"><span class="citation" data-id="9506050"><a href="/opinion/858289/kiobel-v-royal-dutch-petroleum-co/" aria-description="Citation for case: Kiobel v. Royal Dutch Petroleum Co.">569 U.S. at 116</a></span></extracted-citation>, <extracted-citation case-ids="12697039" index="141" url="https://cite.case.law/us/569/108/#p116"><span class="citation" data-id="9506050"><a href="/opinion/858289/kiobel-v-royal-dutch-petroleum-co/" aria-description="Citation for case: Kiobel v. Royal Dutch Petroleum Co.">133 S.Ct. 1659</a></span></extracted-citation>. Where Congress has not spoken at all, the likelihood of impinging on its foreign affairs authority is especially acute.</p>
<p id="p-59">Congress's treatment of ordinary tort claims against federal officers is also revealing. As petitioners and their <em>amici</em> stress, the traditional way in which civil litigation addressed abusive conduct by federal officers was by subjecting them to liability for common-law torts. See Brief for Petitioners 10-17. For many years, such claims could be raised in state or federal court,<footnotemark>8</footnotemark> and this Court occasionally considered tort suits against federal officers for extraterritorial injuries. See, <em>e.g.</em> , <em>Mitchell v. Harmony</em> , <extracted-citation case-ids="3361041" index="142" url="https://cite.case.law/us/54/115/"><span class="citation" data-id="9416513"><a href="/opinion/86727/mitchell-v-harmony/" aria-description="Citation for case: Mitchell v. Harmony">13 How. 115</a></span></extracted-citation>, <extracted-citation case-ids="3361041" index="143" url="https://cite.case.law/us/54/115/"><span class="citation" data-id="9416513"><a href="/opinion/86727/mitchell-v-harmony/" aria-description="Citation for case: Mitchell v. Harmony">14 L.Ed. 75</a></span></extracted-citation> (1852) (affirming award in trespass suit brought by U.S. citizen against U.S. Army officer who seized personal property in Mexico during the Mexican-American war). After <em>Erie</em> , federal common-law claims were out, but we recognized the continuing viability of state-law tort suits against federal officials as recently as <em>Westfall v. Erwin</em> , <extracted-citation case-ids="602224" index="144" url="https://cite.case.law/us/484/292/"><span class="citation" data-id="111980"><a href="/opinion/111980/westfall-v-erwin/" aria-description="Citation for case: Westfall v. Erwin">484 U.S. 292</a></span></extracted-citation>, <extracted-citation case-ids="602224" index="145" url="https://cite.case.law/us/484/292/"><span class="citation" data-id="111980"><a href="/opinion/111980/westfall-v-erwin/" aria-description="Citation for case: Westfall v. Erwin">108 S.Ct. 580</a></span></extracted-citation>, <extracted-citation case-ids="602224" index="146" url="https://cite.case.law/us/484/292/"><span class="citation" data-id="111980"><a href="/opinion/111980/westfall-v-erwin/" aria-description="Citation for case: Westfall v. Erwin">98 L.Ed.2d 619</a></span></extracted-citation> (1988).</p>
<p id="p-60">In response to that decision, Congress passed the so-called Westfall Act, formally the Federal Employees Liability Reform and Tort Compensation Act of 1988, <extracted-citation index="147" url="https://cite.case.law/citations/?q=28%20U.S.C.%20%C2%A7%202679"><span class="citation no-link">28 U.S.C. § 2679</span></extracted-citation>. That Act makes the Federal Tort Claims Act (FTCA) "the exclusive remedy for most claims against Government employees arising out of their official conduct." <em>Hui v. Castaneda</em> , <extracted-citation case-ids="3582219,12448446" index="148" url="https://cite.case.law/us/559/799/"><span class="citation" data-id="145448"><a href="/opinion/145448/hui-v-castaneda/" aria-description="Citation for case: Hui v. Castaneda">559 U.S. 799</a></span></extracted-citation>, 806, <extracted-citation case-ids="3582219,12448446" index="149" url="https://cite.case.law/us/559/799/"><span class="citation" data-id="145448"><a href="/opinion/145448/hui-v-castaneda/" aria-description="Citation for case: Hui v. Castaneda">130 S.Ct. 1845</a></span></extracted-citation>, <extracted-citation case-ids="3582219,12448446" index="150" url="https://cite.case.law/us/559/799/"><span class="citation" data-id="145448"><a href="/opinion/145448/hui-v-castaneda/" aria-description="Citation for case: Hui v. Castaneda">176 L.Ed.2d 703</a></span></extracted-citation> (2010).<footnotemark>9</footnotemark> Thus, a person injured by a federal employee may seek recovery directly from the United States under the FTCA, but the FTCA bars "[a]ny claim arising in a foreign country." § 2680(k).<footnotemark>10</footnotemark> The upshot is that claims that would otherwise permit the recovery of damages are barred if the injury occurred abroad.</p>
<p id="p-61">Yet another example is provided by the Torture Victim Protection Act of 1991, note following <extracted-citation index="151" url="https://cite.case.law/citations/?q=28%20U.S.C.%20%C2%A7%201350"><span class="citation no-link">28 U.S.C. § 1350</span></extracted-citation>, which created a cause of action that may be brought by an alien in a U.S. court under the Alien Tort Statute, § 1350. Under the Torture Victim Protection Act, a damages action may be brought by or on behalf of a victim of torture or an extrajudicial killing carried out by a person who acted under the authority of a foreign <a class="page-label" data-citation-index="1" data-label="749" href="#p749" id="p749">*749</a>state. Consequently, this provision, which is often employed to seek redress for acts committed abroad,<footnotemark>11</footnotemark> cannot be used to sue a United States officer. See <em>Meshal v. Higgenbotham</em> , <extracted-citation case-ids="4357472,12309896" index="152" url="https://cite.case.law/f3d/804/417/"><span class="citation" data-id="9864161"><a href="/opinion/3148973/amir-meshal-v-chris-higgenbotham/" aria-description="Citation for case: Amir Meshal v. Chris Higgenbotham">804 F.3d 417</a></span></extracted-citation>, 430 (C.A.D.C. 2015) (KAVANAUGH, J., concurring).</p>
<p id="p-62">These statutes form a pattern that is important for present purposes. When Congress has enacted statutes creating a damages remedy for persons injured by United States Government officers, it has taken care to preclude claims for injuries that occurred abroad.</p>
<p id="p-63">Instead, when Congress has provided compensation for injuries suffered by aliens outside the United States, it has done so by empowering Executive Branch officials to make payments under circumstances found to be appropriate. Thus, the Foreign Claims Act, <extracted-citation index="153" url="https://cite.case.law/citations/?q=10%20U.S.C.%20%C2%A7%202734"><span class="citation no-link">10 U.S.C. § 2734</span></extracted-citation>, first enacted during World War II, ch. 645, <extracted-citation index="154" url="https://cite.case.law/citations/?q=55%20Stat.%20880"><span class="citation no-link">55 Stat. 880</span></extracted-citation>, allows the Secretary of Defense to appoint claims commissions to settle and pay claims for personal injury and property damage resulting from the noncombat activities of the Armed Forces outside this country. § 2734(a). Similarly, § 2734a allows the Secretary of Defense and the Secretary of Homeland Security to make payments pursuant to "an international agreement which provides for the settlement or adjudication and cost sharing of claims against the United States" that arise out of "acts or omissions" of the Armed Forces. § 2734a(a); see also <extracted-citation index="155" url="https://cite.case.law/citations/?q=22%20U.S.C.%20%C2%A7%202669"><span class="citation no-link">22 U.S.C. § 2669</span></extracted-citation>(b) (State Department may settle and pay certain claims for death, injury, or property loss or damage "for the purpose of promoting and maintaining friendly relations with foreign countries"); § 2669-1 (Secretary of State has authority to pay tort claims arising in foreign countries in connection with State Department operations); <extracted-citation index="156" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%20904"><span class="citation no-link">21 U.S.C. § 904</span></extracted-citation> (Attorney General has authority to pay tort claims arising in connection with the operations of the Drug Enforcement Administration abroad).</p>
<p id="p-64">This pattern of congressional action-refraining from authorizing damages actions for injury inflicted abroad by Government officers, while providing alternative avenues for compensation in some situations-gives us further reason to hesitate about extending <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> in this case.</p>
<p id="p-65">E</p>
<p id="p-66">In sum, this case features multiple factors that counsel hesitation about extending <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> <em>,</em> but they can all be condensed to one concern-respect for the separation of powers. See <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1857-1858. "Foreign policy and national security decisions are 'delicate, complex, and involve large elements of prophecy' for which 'the Judiciary has neither aptitude, facilities[,] nor responsibility.' " <em><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">Jesner</a></span></em> , 584 U.S., at ----, <extracted-citation case-ids="12611257" index="157" url="https://cite.case.law/s-ct/138/1386/#p1391"><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/#1414" aria-description="Citation for case: Jesner v. Arab Bank, PLC">138 S.Ct., at 1414</a></span></extracted-citation> (GORSUCH, J., concurring part and concurring in judgment) (quoting <em>Chicago &amp; Southern Air Lines, Inc. v. Waterman S. S. Corp.</em> , <extracted-citation case-ids="6157296" index="158" url="https://cite.case.law/us/333/103/#p111"><span class="citation" data-id="9420099"><a href="/opinion/104510/chicago-southern-air-lines-inc-v-waterman-steamship-corp/" aria-description="Citation for case: Chicago &amp; Southern Air Lines, Inc. v. Waterman Steamship...">333 U.S. 103</a></span></extracted-citation>, 111, <extracted-citation case-ids="6157296" index="159" url="https://cite.case.law/us/333/103/#p111"><span class="citation" data-id="9420099"><a href="/opinion/104510/chicago-southern-air-lines-inc-v-waterman-steamship-corp/" aria-description="Citation for case: Chicago &amp; Southern Air Lines, Inc. v. Waterman Steamship...">68 S.Ct. 431</a></span></extracted-citation>, <extracted-citation index="160" url="https://cite.case.law/citations/?q=92%20L.%20Ed.%20568"><span class="citation no-link">92 L.Ed. 568</span></extracted-citation> (1948) ). To avoid upsetting the delicate web of international relations, we typically presume that even congressionally crafted causes of action do not apply outside our borders. These concerns are only heightened when judges are asked to fashion constitutional remedies. Congress, which has authority in the field of foreign affairs, has chosen not to create liability in similar statutes, leaving the resolution of extraterritorial <a class="page-label" data-citation-index="1" data-label="750" href="#p750" id="p750">*750</a>claims brought by foreign nationals to executive officials and the diplomatic process.</p>
<p id="p-67">Congress's decision not to provide a judicial remedy does not compel us to step into its shoes. "The absence of statutory relief for a constitutional violation ... does not by any means necessarily imply that courts should award money damages against the officers responsible for the violation." <em>Schweiker</em> , <extracted-citation case-ids="1775175" index="161" url="https://cite.case.law/us/487/412/"><span class="citation" data-id="9431421"><a href="/opinion/112132/schweiker-v-chilicky/" aria-description="Citation for case: Schweiker v. Chilicky">487 U.S. at 421</a></span>-422</extracted-citation>, <extracted-citation case-ids="1775175" index="162" url="https://cite.case.law/us/487/412/"><span class="citation" data-id="9431421"><a href="/opinion/112132/schweiker-v-chilicky/" aria-description="Citation for case: Schweiker v. Chilicky">108 S.Ct. 2460</a></span></extracted-citation> ; see also <em>Stanley</em> , <extracted-citation case-ids="28195" index="163" url="https://cite.case.law/us/483/669/"><span class="citation" data-id="9431121"><a href="/opinion/111954/united-states-v-stanley/" aria-description="Citation for case: United States v. Stanley">483 U.S. at 683</a></span></extracted-citation>, <extracted-citation case-ids="28195" index="164" url="https://cite.case.law/us/483/669/"><span class="citation" data-id="9431121"><a href="/opinion/111954/united-states-v-stanley/" aria-description="Citation for case: United States v. Stanley">107 S.Ct. 3054</a></span></extracted-citation> ("[I]t is irrelevant to a 'special factors' analysis whether the laws currently on the books afford [plaintiff] an 'adequate' federal remedy for his injuries").<footnotemark>12</footnotemark></p>
<p id="p-68">When evaluating whether to extend <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span>,</em> the most important question "is 'who should decide' whether to provide for a damages remedy, Congress or the courts?" <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1857 (quoting <em>Bush</em> , <span class="citation" data-id="9429240"><a href="/opinion/110965/bush-v-lucas/#380" aria-description="Citation for case: Bush v. Lucas">462 U.S. at 380</a></span>, <extracted-citation case-ids="6188608" index="165" url="https://cite.case.law/us/462/367/"><span class="citation" data-id="9429240"><a href="/opinion/110965/bush-v-lucas/" aria-description="Citation for case: Bush v. Lucas">103 S.Ct. 2404</a></span></extracted-citation> ). The correct "answer most often will be Congress." 582 U.S., at ----, 137 S.Ct., at 1857<em>.</em> That is undoubtedly the answer here.</p>
<p id="p-69">* * *</p>
<p id="p-70">The judgment of the United States Court of Appeals for the Fifth Circuit is affirmed.</p>
<p id="p-71">It is so ordered.</p>
<p id="p-72">Justice THOMAS, with whom Justice GORSUCH joins, concurring.</p>
<p id="p-73">The Court correctly applies our precedents to conclude that the implied cause of action created in <em>Bivens v. Six Unknown Fed. Narcotics Agents</em> , <extracted-citation case-ids="12027206" index="166" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. 388</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="167" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="168" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">29 L.Ed.2d 619</a></span></extracted-citation> (1971), should not be extended to cross-border shootings. I therefore join its opinion.</p>
<p id="p-74">I write separately because, in my view, the time has come to consider discarding the <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> doctrine altogether. The foundation for <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> -the practice of creating implied causes of action in the statutory context-has already been abandoned. And the Court has consistently refused to extend the <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> doctrine for nearly 40 years, even going so far as to suggest that <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> and its progeny were wrongly decided. <em>Stare decisis</em> provides no "veneer of respectability to our continued application of [these] demonstrably incorrect precedents." <em>Gamble</em> <em>v.</em> <em>United States</em> , 587 U.S. ----, ----, <extracted-citation case-ids="12620232" index="169" url="https://cite.case.law/s-ct/139/1960/#p1981"><span class="citation" data-id="9888741"><a href="/opinion/4630267/gamble-v-united-states/" aria-description="Citation for case: Gamble v. United States">139 S.Ct. 1960</a></span></extracted-citation>, 1981, <extracted-citation index="170" url="https://cite.case.law/citations/?q=204%20L.%20Ed.%202d%20322"><span class="citation" data-id="9888741"><a href="/opinion/4630267/gamble-v-united-states/" aria-description="Citation for case: Gamble v. United States">204 L.Ed.2d 322</a></span></extracted-citation> (2019) (THOMAS, J., concurring). To ensure that we are not "perpetuat[ing] a usurpation of the legislative power," <em><extracted-citation index="171" url="https://cite.case.law/citations/?q=204%20L.%20Ed.%202d%20322"><span class="citation" data-id="9888741"><a href="/opinion/4630267/gamble-v-united-states/" aria-description="Citation for case: Gamble v. United States">id.</a></span></extracted-citation></em> , at ----, <span class="citation" data-id="9888741"><a href="/opinion/4630267/gamble-v-united-states/#1984" aria-description="Citation for case: Gamble v. United States">139 S.Ct., at 1984</a></span>, we should reevaluate our continued recognition of even a limited form of the <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> doctrine.</p>
<p id="p-75">" ' <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> is a relic of the heady days in which this Court assumed common-law powers to create causes of action.' " <em>Wilkie v. Robbins</em> , <extracted-citation case-ids="3573210" index="172" url="https://cite.case.law/us/551/537/"><span class="citation" data-id="9435015"><a href="/opinion/145705/wilkie-v-robbins/" aria-description="Citation for case: Wilkie v. Robbins">551 U.S. 537</a></span></extracted-citation>, 568, <extracted-citation case-ids="3573210" index="173" url="https://cite.case.law/us/551/537/"><span class="citation" data-id="9435015"><a href="/opinion/145705/wilkie-v-robbins/" aria-description="Citation for case: Wilkie v. Robbins">127 S.Ct. 2588</a></span></extracted-citation>, <extracted-citation case-ids="3573210" index="174" url="https://cite.case.law/us/551/537/"><span class="citation" data-id="9435015"><a href="/opinion/145705/wilkie-v-robbins/" aria-description="Citation for case: Wilkie v. Robbins">168 L.Ed.2d 389</a></span></extracted-citation> (2007) (THOMAS, J., concurring) (quoting <em>Correctional Services Corp. v. Malesko</em> , <extracted-citation case-ids="9107996" index="175" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">534 U.S. 61</a></span></extracted-citation>, 75, <extracted-citation case-ids="9107996" index="176" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">122 S.Ct. 515</a></span></extracted-citation>, <extracted-citation case-ids="9107996" index="177" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">151 L.Ed.2d 456</a></span></extracted-citation> (2001) (Scalia, J., concurring)). In the decade preceding <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> , the Court believed that it had a duty "to be alert to provide such remedies as are necessary to make effective" Congress' purposes in enacting a statute. <em>J. I. Case Co. v. Borak</em> , <extracted-citation case-ids="6170359" index="178" url="https://cite.case.law/us/377/426/#p433"><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">377 U.S. 426</a></span></extracted-citation>, 433, <extracted-citation case-ids="6170359" index="179" url="https://cite.case.law/us/377/426/#p433"><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">84 S.Ct. 1555</a></span></extracted-citation>, <extracted-citation case-ids="6170359" index="180" url="https://cite.case.law/us/377/426/#p433"><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">12 L.Ed.2d 423</a></span></extracted-citation> (1964). Accordingly, the Court freely created implied private causes of action for damages under federal statutes. See, <em>e.g.,</em> <a class="page-label" data-citation-index="1" data-label="751" href="#p751" id="p751">*751</a><em>Sullivan v. Little Hunting Park, Inc.</em> , <extracted-citation case-ids="11331541" index="181" url="https://cite.case.law/us/396/229/#p239"><span class="citation" data-id="9424129"><a href="/opinion/108017/sullivan-v-little-hunting-park-inc/" aria-description="Citation for case: Sullivan v. Little Hunting Park, Inc.">396 U.S. 229</a></span></extracted-citation>, 239, <extracted-citation case-ids="11331541" index="182" url="https://cite.case.law/us/396/229/#p239"><span class="citation" data-id="9424129"><a href="/opinion/108017/sullivan-v-little-hunting-park-inc/" aria-description="Citation for case: Sullivan v. Little Hunting Park, Inc.">90 S.Ct. 400</a></span></extracted-citation>, <extracted-citation case-ids="11331541" index="183" url="https://cite.case.law/us/396/229/#p239"><span class="citation" data-id="9424129"><a href="/opinion/108017/sullivan-v-little-hunting-park-inc/" aria-description="Citation for case: Sullivan v. Little Hunting Park, Inc.">24 L.Ed.2d 386</a></span></extracted-citation> (1969) ; <em>Allen v. State Bd. of Elections</em> , <extracted-citation case-ids="11320219" index="184" url="https://cite.case.law/us/393/544/#p557"><span class="citation" data-id="9423914"><a href="/opinion/107846/allen-v-state-board-of-elections/" aria-description="Citation for case: Allen v. State Board of Elections">393 U.S. 544</a></span></extracted-citation>, 557, <extracted-citation case-ids="11320219" index="185" url="https://cite.case.law/us/393/544/#p557"><span class="citation" data-id="9423914"><a href="/opinion/107846/allen-v-state-board-of-elections/" aria-description="Citation for case: Allen v. State Board of Elections">89 S.Ct. 817</a></span></extracted-citation>, <extracted-citation case-ids="11320219" index="186" url="https://cite.case.law/us/393/544/#p557"><span class="citation" data-id="9423914"><a href="/opinion/107846/allen-v-state-board-of-elections/" aria-description="Citation for case: Allen v. State Board of Elections">22 L.Ed.2d 1</a></span></extracted-citation> (1969).</p>
<p id="p-76">This misguided approach to implied causes of action in the statutory context formed the backdrop of the Court's decision in <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> . There, the Court held that federal officers who conducted a warrantless search and arrest in violation of the Fourth Amendment could be sued for damages. <em>Bivens</em> , <extracted-citation case-ids="12027206" index="187" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. at 397</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="188" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation>. The Court acknowledged that Congress had not provided a statutory cause of action for damages against federal officers and that "the Fourth Amendment does not in so many words provide for its enforcement by an award of money damages." <em><extracted-citation case-ids="12027206" index="189" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Id.</a></span></extracted-citation></em> , at 396-397, <extracted-citation case-ids="12027206" index="190" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation>. But it concluded, consistent with the then-prevailing understanding of implied causes of action in the statutory context, that federal courts could infer such a "remedial mechanism." <em><extracted-citation case-ids="12027206" index="191" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Id.</a></span></extracted-citation></em> , at 397, <extracted-citation case-ids="12027206" index="192" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation> (citing <em>Borak</em> , <extracted-citation case-ids="6170359" index="193" url="https://cite.case.law/us/377/426/#p433"><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">377 U.S. at 433</a></span></extracted-citation>, <extracted-citation case-ids="6170359" index="194" url="https://cite.case.law/us/377/426/#p433"><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">84 S.Ct. 1555</a></span></extracted-citation> ).</p>
<p id="p-77">This holding "broke new ground." <em>Ante</em> , at 741. From the ratification of the Bill of Rights until 1971, the Court did not create "implied private action[s] for damages against federal officers alleged to have violated a citizen's constitutional rights." <em>Malesko</em> , <extracted-citation case-ids="9107996" index="195" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">534 U.S. at 66</a></span></extracted-citation>, <extracted-citation case-ids="9107996" index="196" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">122 S.Ct. 515</a></span></extracted-citation>. Suits to recover such damages were generally brought under state tort law. See <em>Wheeldin v. Wheeler</em> , <extracted-citation case-ids="11719775" index="197" url="https://cite.case.law/us/373/647/#p652"><span class="citation" data-id="9422624"><a href="/opinion/106628/wheeldin-v-wheeler/" aria-description="Citation for case: Wheeldin v. Wheeler">373 U.S. 647</a></span></extracted-citation>, 652, <extracted-citation case-ids="11719775" index="198" url="https://cite.case.law/us/373/647/#p652"><span class="citation" data-id="9422624"><a href="/opinion/106628/wheeldin-v-wheeler/" aria-description="Citation for case: Wheeldin v. Wheeler">83 S.Ct. 1441</a></span></extracted-citation>, <extracted-citation case-ids="11719775" index="199" url="https://cite.case.law/us/373/647/#p652"><span class="citation" data-id="9422624"><a href="/opinion/106628/wheeldin-v-wheeler/" aria-description="Citation for case: Wheeldin v. Wheeler">10 L.Ed.2d 605</a></span></extracted-citation> (1963). <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> thus opened the door to a new avenue for recovering damages from federal officers. In the wake of that decision, the Court recognized an implied cause of action for damages against a Member of Congress accused of sex discrimination in violation of the Fifth Amendment's Due Process Clause, <em>Davis v. Passman</em> , <extracted-citation case-ids="1532130" index="200" url="https://cite.case.law/us/442/228/"><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">442 U.S. 228</a></span></extracted-citation>, <extracted-citation case-ids="1532130" index="201" url="https://cite.case.law/us/442/228/"><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">99 S.Ct. 2264</a></span></extracted-citation>, <extracted-citation case-ids="1532130" index="202" url="https://cite.case.law/us/442/228/"><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">60 L.Ed.2d 846</a></span></extracted-citation> (1979), and against prison officials accused of denying medical care in violation of the Eighth Amendment's Cruel and Unusual Punishments Clause, <em>Carlson v. Green</em> , <extracted-citation case-ids="6180250" index="203" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">446 U.S. 14</a></span></extracted-citation>, <extracted-citation case-ids="6180250" index="204" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">100 S.Ct. 1468</a></span></extracted-citation>, <extracted-citation case-ids="6180250" index="205" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">64 L.Ed.2d 15</a></span></extracted-citation> (1980). Given this Court's trend of creating implied causes of action, "there was a possibility that the Court would keep expanding <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> until it became the substantial equivalent of <extracted-citation index="206" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation>." <em>Ziglar</em> <em>v.</em> <em>Abbasi</em> , 582 U.S. ----, ----, <extracted-citation case-ids="12604999" index="207" url="https://cite.case.law/s-ct/137/1843/"><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">137 S.Ct. 1843</a></span></extracted-citation>, 1855, <extracted-citation case-ids="12604999" index="208" url="https://cite.case.law/s-ct/137/1843/"><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">198 L.Ed.2d 290</a></span></extracted-citation> (2017) (internal quotation marks omitted).</p>
<p id="p-78">The Court, however, eventually corrected course. In the statutory context, the Court "retreated from [its] previous willingness to imply a cause of action where Congress has not provided one." <em>Malesko</em> , <extracted-citation case-ids="9107996" index="209" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/#67" aria-description="Citation for case: Correctional Services Corp. v. Malesko">534 U.S. at 67</a></span>, n. 3</extracted-citation>, <extracted-citation case-ids="9107996" index="210" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">122 S.Ct. 515</a></span></extracted-citation>. After a series of decisions limiting courts' discretion to create statut

[...TRUNCATED 90943 of 210943 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Herring v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Herring v. United States"
type: case
citation: "555 U.S. 135 (2009)"
parallel_cite: "129 S. Ct. 695; 172 L. Ed. 2d 496"
neutral_cite: 2009 U.S. LEXIS 581
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-01-14
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2009-01-14
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Herring v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145922/herring-v-united-states/"
  cluster_id: 145922
  opinion_id: 145922
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Collective Knowledge and the Fellow-Officer Rule]]"
    role: "Key (non-exclusive; imputation limit)"
related: ["[[United States v. Leon]]", "[[Arizona v. Evans]]", "[[Mapp v. Ohio]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "good-faith", "deterrence"]
holding: "Suppression is warranted only where deterrence benefits outweigh costs; isolated, attenuated police negligence (a recordkeeping error)…"
lake:
  record_id: Herring v. United States
  status: verified
  projected_at: 2026-07-06
---

# Herring v. United States

*555 U.S. 135 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigator Anderson asked a neighboring county's warrant clerk whether there was any outstanding warrant for Bennie Herring; the clerk reported one and Anderson arrested Herring, and a search incident to the arrest produced methamphetamine and a pistol. Within minutes the clerk discovered the warrant had been recalled months earlier and never removed from the database — a negligent bookkeeping error. Herring moved to suppress the gun and drugs as the fruit of an arrest unsupported by a valid warrant.

## Issue
Whether the exclusionary rule requires suppression of evidence found incident to an arrest made in objectively reasonable reliance on a police recordkeeping error — a warrant that had been recalled but, through isolated negligence, was left listed as active.

## Rule
No. Suppression turns on the culpability of the police conduct and the deterrence to be gained, not on the mere fact of a Fourth Amendment violation. "To trigger the exclusionary rule, police conduct must be sufficiently deliberate that exclusion can meaningfully deter it, and sufficiently culpable that such deterrence is worth the price paid by the justice system." — 555 U.S. at 144. ^pin-144

"As laid out in our cases, the exclusionary rule serves to deter deliberate, reckless, or grossly negligent conduct, or in some circumstances recurring or systemic negligence." — *Id.* ^pin-144a

## Application
The error here was a single, isolated bookkeeping mistake attenuated from the arrest, not deliberate, reckless, or grossly negligent conduct and not shown to be routine or systemic. Because the police conduct was not culpable enough for exclusion to yield deterrence worth its cost, the methamphetamine and pistol found incident to Herring's arrest were not suppressed.

## Conclusion
The evidence was admissible; the judgment denying suppression was affirmed. Negligent, attenuated recordkeeping error does not trigger the exclusionary rule.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Herring* extends the cost-benefit, deterrence-focused approach of [[United States v. Leon]] and [[Arizona v. Evans]], tying exclusion to the culpability of the police conduct.

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *Herring v. United States*, 555 U.S. 135 (2009) — https://www.courtlistener.com/opinion/145922/herring-v-united-states/ — pinpoint: 144.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4b06bbdc88b4fdf8", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Herring v. United States"}, "payload": {"all": [{"cite": "555 U.S. 135", "page": "135", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "555"}, {"cite": "129 S. Ct. 695", "page": "695", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "129"}, {"cite": "172 L. Ed. 2d 496", "page": "496", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "172"}, {"cite": "2009 U.S. LEXIS 581", "page": "581", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2009"}], "display": "555 U.S. 135", "official": {"cite": "555 U.S. 135", "page": "135", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "555"}, "official_selection_present": true, "record_id": "Herring v. United States"}}
{"assertion_id": "ad986bbec0334708", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-144", "record_id": "Herring v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-144", "pinpoint_status": "slip-only", "quote": "--- # Herring v. United States *555 U.S. 135 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigator Anderson asked a neighboring county's warrant clerk whether there was any outstanding warrant for Bennie Herring; the clerk reported one and Anderson arrested Herring, and a search incident to the arrest produced methamphetamine and a pistol. Within minutes the clerk discovered the warrant had been recalled months earlier and never removed from the database — a negligent bookkeeping error. Herring moved to suppress the gun and drugs as the fruit of an arrest unsupported by a valid warrant. ## Issue Whether the exclusionary rule requires suppression of evidence found incident to an arrest made in objectively reasonable reliance on a police recordkeeping error — a warrant that had been recalled but, through isolated negligence, was left listed as active. ## Rule No. Suppression turns on the culpability of the police conduct and the deterrence to be gained, not on the mere fact of a Fourth Amendment violation.", "quote_fidelity": "mismatch", "record_id": "Herring v. United States", "star_marker": null}}
{"assertion_id": "b19f9d16aa103d01", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-144a", "record_id": "Herring v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-144a", "pinpoint_status": "slip-only", "quote": "As laid out in our cases, the exclusionary rule serves to deter deliberate, reckless, or grossly negligent conduct, or in some circumstances recurring or systemic negligence.", "quote_fidelity": "mismatch", "record_id": "Herring v. United States", "star_marker": null}}
{"assertion_id": "9be630675e36dabd", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Herring v. United States"}, "payload": {"as_of_content": "2009-01-14", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Herring v. United States", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Herring v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Herring v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Herring v. United States",
    "case_name_short": "Herring",
    "case_name_full": "Herring v. United States",
    "input_case_name": "Herring v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-01-14",
    "year": 2009,
    "docket": null,
    "cluster_id": 145922,
    "lead_opinion_id": 145922,
    "sibling_ids": [
      145922,
      9435413,
      9435414,
      9435415
    ],
    "absolute_url": "/opinion/145922/herring-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "555 U.S. 135",
      "volume": "555",
      "reporter": "U.S.",
      "page": "135",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "129 S. Ct. 695",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "695",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "172 L. Ed. 2d 496",
        "volume": "172",
        "reporter": "L. Ed. 2d",
        "page": "496",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 581",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "581",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "555 U.S. 135",
        "volume": "555",
        "reporter": "U.S.",
        "page": "135",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 695",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "695",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "172 L. Ed. 2d 496",
        "volume": "172",
        "reporter": "L. Ed. 2d",
        "page": "496",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 581",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "581",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "555 U.S. 135",
    "official_selection": {
      "court_class": "scotus",
      "selected": "555 U.S. 135",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-144",
      "page": null,
      "quote": "--- # Herring v. United States *555 U.S. 135 (2009)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigator Anderson asked a neighboring county's warrant clerk whether there was any outstanding warrant for Bennie Herring; the clerk reported one and Anderson arrested Herring, and a search incident to the arrest produced methamphetamine and a pistol. Within minutes the clerk discovered the warrant had been recalled months earlier and never removed from the database \u2014 a negligent bookkeeping error. Herring moved to suppress the gun and drugs as the fruit of an arrest unsupported by a valid warrant. ## Issue Whether the exclusionary rule requires suppression of evidence found incident to an arrest made in objectively reasonable reliance on a police recordkeeping error \u2014 a warrant that had been recalled but, through isolated negligence, was left listed as active. ## Rule No. Suppression turns on the culpability of the police conduct and the deterrence to be gained, not on the mere fact of a Fourth Amendment violation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-144a",
      "page": null,
      "quote": "As laid out in our cases, the exclusionary rule serves to deter deliberate, reckless, or grossly negligent conduct, or in some circumstances recurring or systemic negligence.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2009-01-14",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Herring v. United States",
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
        "journal_ref": "Herring v. United States:lane1_negative"
      },
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
        "journal_ref": "Herring v. United States:lane1_negative"
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
        "journal_ref": "Herring v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 218926,
          "cite": [
            "180 L. Ed. 2d 285",
            "131 S. Ct. 2419",
            "564 U.S. 229",
            "2011 U.S. LEXIS 4560"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
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
        "journal_ref": "Herring v. United States:lane2_top_cited"
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
        "journal_ref": "Herring v. United States:lane2_top_cited"
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
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Warshak",
          "cluster_id": 181032,
          "cite": [
            "631 F.3d 266",
            "2010 U.S. App. LEXIS 25415",
            "2010 WL 5071766"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
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
        "journal_ref": "Herring v. United States:lane2_top_cited"
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
        "journal_ref": "Herring v. United States:lane2_top_cited"
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
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fadwa Safar v. Lisa Tingle",
          "cluster_id": 4398025,
          "cite": [
            "859 F.3d 241",
            "2017 WL 2453257",
            "2017 U.S. App. LEXIS 10114"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Brown",
          "cluster_id": 4582900,
          "cite": [
            "302 Neb. 53",
            "921 N.W.2d 804"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. McCane",
          "cluster_id": 172450,
          "cite": [
            "573 F.3d 1037",
            "2009 U.S. App. LEXIS 16557",
            "2009 WL 2231658"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Handy",
          "cluster_id": 2559301,
          "cite": [
            "18 A.3d 179",
            "206 N.J. 39",
            "2011 N.J. LEXIS 566"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Albert White",
          "cluster_id": 4438318,
          "cite": [
            "874 F.3d 490",
            "2017 FED App. 0242P",
            "2017 WL 4848911",
            "2017 U.S. App. LEXIS 21332"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Burnett",
          "cluster_id": 4581383,
          "cite": [
            "2019 CO 2",
            "432 P.3d 617"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vilar",
          "cluster_id": 1039434,
          "cite": [
            "729 F.3d 62",
            "92 A.L.R. Fed. 2d 661",
            "2013 WL 4608948",
            "2013 U.S. App. LEXIS 18143"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ruehle",
          "cluster_id": 1266839,
          "cite": [
            "583 F.3d 600",
            "2009 U.S. App. LEXIS 21450",
            "2009 WL 3152971"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Talkington",
          "cluster_id": 2784485,
          "cite": [
            "301 Kan. 453",
            "345 P.3d 258",
            "2015 Kan. LEXIS 167",
            "2015 WL 968451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dupree",
          "cluster_id": 152453,
          "cite": [
            "617 F.3d 724",
            "2010 U.S. App. LEXIS 16310",
            "2010 WL 3063290"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Leak (Slip Opinion)",
          "cluster_id": 3170709,
          "cite": [
            "2016 Ohio 154",
            "145 Ohio St. 3d 165",
            "47 N.E.3d 821"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Afana",
          "cluster_id": 2584726,
          "cite": [
            "233 P.3d 879"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bershchansky",
          "cluster_id": 8442239,
          "cite": [
            "788 F.3d 102",
            "2015 U.S. App. LEXIS 9383",
            "2015 WL 3513759"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Earl Davis",
          "cluster_id": 2968788,
          "cite": [
            "690 F.3d 226",
            "2012 WL 3518479",
            "2012 U.S. App. LEXIS 17217"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Farias-Gonzalez",
          "cluster_id": 78275,
          "cite": [
            "556 F.3d 1181",
            "2009 U.S. App. LEXIS 2060",
            "2009 WL 232328"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Comprehensive Drug Testing, Inc.",
          "cluster_id": 175207,
          "cite": [
            "621 F.3d 1162",
            "2010 WL 3529247"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 2637645,
          "cite": [
            "224 P.3d 55",
            "47 Cal. 4th 1104",
            "104 Cal. Rptr. 3d 727",
            "2010 Cal. LEXIS 114"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145922 OR 9435413 OR 9435414 OR 9435415) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTU4MzEwNDAwMDAwJnM9NDYyMTQ0NCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145922+OR+9435413+OR+9435414+OR+9435415%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(145922 OR 9435413 OR 9435414 OR 9435415)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NCZzPTE3MjA5NyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145922+OR+9435413+OR+9435414+OR+9435415%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145922 OR 9435413 OR 9435414 OR 9435415)",
        "reviewed": 88,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 88,
        "triage_read": 3,
        "triage_snippet_classified": 85
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145922 OR 9435413 OR 9435414 OR 9435415)",
    "indexed_citing_opinions": 826,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145922,
        "count": 639,
        "count_source": "search"
      },
      {
        "opinion_id": 9435413,
        "count": 200,
        "count_source": "search"
      },
      {
        "opinion_id": 9435414,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9435415,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1552,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/herring-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzMjk3NTYmcz0xMDQyMjQ1NyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145922+OR+9435413+OR+9435414+OR+9435415%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145922,
        "cited_id": 77746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 101320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 109302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 109925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 110267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 110317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 111263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 111835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 117905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 118235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 145646,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 1662274,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 2574654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 3580565,
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
    "date_created": "2026-07-05T06:58:33Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:58:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:58:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:03:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:58:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Herring v. United States

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

                   HERRING v. UNITED STATES

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                THE ELEVENTH CIRCUIT

    No. 07–513.     Argued October 7, 2008—Decided January 14, 2009
Officers in Coffee County arrested petitioner Herring based on a war
  rant listed in neighboring Dale County’s database. A search incident
  to that arrest yielded drugs and a gun. It was then revealed that the
  warrant had been recalled months earlier, though this information
  had never been entered into the database. Herring was indicted on
  federal gun and drug possession charges and moved to suppress the
  evidence on the ground that his initial arrest had been illegal. As
  suming that there was a Fourth Amendment violation, the District
  Court concluded that the exclusionary rule did not apply and denied
  the motion to suppress. The Eleventh Circuit affirmed, finding that
  the arresting officers were innocent of any wrongdoing, and that Dale
  County’s failure to update the records was merely negligent. The
  court therefore concluded that the benefit of suppression would be
  marginal or nonexistent and that the evidence was admissible under
  the good-faith rule of United States v. Leon, 468 U. S. 897.
Held: When police mistakes leading to an unlawful search are the re
 sult of isolated negligence attenuated from the search, rather than
 systemic error or reckless disregard of constitutional requirements,
 the exclusionary rule does not apply. Pp. 4–13.
    (a) The fact that a search or arrest was unreasonable does not nec
 essarily mean that the exclusionary rule applies. Illinois v. Gates,
 462 U. S. 213, 223. The rule is not an individual right and applies
 only where its deterrent effect outweighs the substantial cost of let
 ting guilty and possibly dangerous defendants go free. Leon, 468
 U. S., at 908–909. For example, it does not apply if police acted “in
 objectively reasonable reliance” on an invalid warrant. Id., at 922.
 In applying Leon’s good-faith rule to police who reasonably relied on
 mistaken information in a court’s database that an arrest warrant
2                     HERRING v. UNITED STATES

                                  Syllabus

    was outstanding, Arizona v. Evans, 514 U. S. 1, 14–15, the Court left
    unresolved the issue confronted here: whether evidence should be
    suppressed if the police committed the error, id., at 16, n. 5. Pp. 4–7.
       (b) The extent to which the exclusionary rule is justified by its de
    terrent effect varies with the degree of law enforcement culpability.
    See, e.g., Leon, supra, at 911. Indeed, the abuses that gave rise to the
    rule featured intentional conduct that was patently unconstitutional.
    See, e.g., Weeks v. United States, 232 U. S 383. An error arising from
    nonrecurring and attenuated negligence is far removed from the core
    concerns that led to the rule’s adoption. Pp. 7–9.
       (c) To trigger the exclusionary rule, police conduct must be suffi
    ciently deliberate that exclusion can meaningfully deter it, and suffi
    ciently culpable that such deterrence is worth the price paid by the
    justice system. The pertinent analysis is objective, not an inquiry
    into the arresting officers’ subjective awareness. See, e.g., Leon, su
    pra, at 922, n. 23. Pp. 9–11.
       (d) The conduct here was not so objectively culpable as to require
    exclusion. The marginal benefits that might follow from suppressing
    evidence obtained in these circumstances cannot justify the substan
    tial costs of exclusion. Leon, supra, at 922. Pp. 11–13.
492 F. 3d 1212, affirmed.

  ROBERTS, C. J., delivered the opinion of the Court, in which SCALIA,
KENNEDY, THOMAS, and ALITO, JJ., joined. GINSBURG, J., filed a dissent
ing opinion, in which STEVENS, SOUTER, and BREYER, JJ., joined.
BREYER, J., filed a dissenting opinion, in which SOUTER, J., joined.
                        Cite as: 555 U. S. ____ (2009)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 07–513
                                   _________________


 BENNIE DEAN HERRING, PETITIONER v. UNITED 

                 STATES 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

          APPEALS FOR THE ELEVENTH CIRCUIT

                               [January 14, 2009] 


   CHIEF JUSTICE ROBERTS delivered the opinion of the
Court.
   The Fourth Amendment forbids “unreasonable searches
and seizures,” and this usually requires the police to have
probable cause or a warrant before making an arrest.
What if an officer reasonably believes there is an out
standing arrest warrant, but that belief turns out to be
wrong because of a negligent bookkeeping error by an
other police employee? The parties here agree that the
ensuing arrest is still a violation of the Fourth Amend
ment, but dispute whether contraband found during a
search incident to that arrest must be excluded in a later
prosecution.
   Our cases establish that such suppression is not an
automatic consequence of a Fourth Amendment violation.
Instead, the question turns on the culpability of the police
and the potential of exclusion to deter wrongful police
conduct. Here the error was the result of isolated negli
gence attenuated from the arrest. We hold that in these
circumstances the jury should not be barred from consid
ering all the evidence.
2               HERRING v. UNITED STATES

                     Opinion of the Court

                              I
   On July 7, 2004, Investigator Mark Anderson learned
that Bennie Dean Herring had driven to the Coffee County
Sheriff’s Department to retrieve something from his im
pounded truck. Herring was no stranger to law enforce
ment, and Anderson asked the county’s warrant clerk,
Sandy Pope, to check for any outstanding warrants for
Herring’s arrest. When she found none, Anderson asked
Pope to check with Sharon Morgan, her counterpart in
neighboring Dale County. After checking Dale County’s
computer database, Morgan replied that there was an
active arrest warrant for Herring’s failure to appear on a
felony charge. Pope relayed the information to Anderson
and asked Morgan to fax over a copy of the warrant as
confirmation. Anderson and a deputy followed Herring as
he left the impound lot, pulled him over, and arrested him.
A search incident to the arrest revealed methampheta
mine in Herring’s pocket, and a pistol (which as a felon he
could not possess) in his vehicle. App. 17–23.
   There had, however, been a mistake about the warrant.
The Dale County sheriff’s computer records are supposed
to correspond to actual arrest warrants, which the office
also maintains. But when Morgan went to the files to
retrieve the actual warrant to fax to Pope, Morgan was
unable to find it. She called a court clerk and learned that
the warrant had been recalled five months earlier. Nor
mally when a warrant is recalled the court clerk’s office or
a judge’s chambers calls Morgan, who enters the informa
tion in the sheriff’s computer database and disposes of the
physical copy. For whatever reason, the information about
the recall of the warrant for Herring did not appear in the
database. Morgan immediately called Pope to alert her to
the mixup, and Pope contacted Anderson over a secure
radio. This all unfolded in 10 to 15 minutes, but Herring
had already been arrested and found with the gun and
drugs, just a few hundred yards from the sheriff’s office.
                 Cite as: 555 U. S. ____ (2009)           3

                     Opinion of the Court

Id., at 26, 35–42, 54–55.
  Herring was indicted in the District Court for the Mid
dle District of Alabama for illegally possessing the gun
and drugs, violations of 18 U. S. C. §922(g)(1) and 21
U. S. C. §844(a). He moved to suppress the evidence on
the ground that his initial arrest had been illegal because
the warrant had been rescinded. The Magistrate Judge
recommended denying the motion because the arresting
officers had acted in a good-faith belief that the warrant
was still outstanding. Thus, even if there were a Fourth
Amendment violation, there was “no reason to believe that
application of the exclusionary rule here would deter the
occurrence of any future mistakes.” App. 70. The District
Court adopted the Magistrate Judge’s recommendation,
451 F. Supp. 2d 1290 (2005), and the Court of Appeals for
the Eleventh Circuit affirmed, 492 F. 3d 1212 (2007).
  The Eleventh Circuit found that the arresting officers in
Coffee County “were entirely innocent of any wrongdoing
or carelessness.” id., at 1218. The court assumed that
whoever failed to update the Dale County sheriff’s records
was also a law enforcement official, but noted that “the
conduct in question [wa]s a negligent failure to act, not a
deliberate or tactical choice to act.” Ibid. Because the
error was merely negligent and attenuated from the ar
rest, the Eleventh Circuit concluded that the benefit of
suppressing the evidence “would be marginal or nonexis
tent,” ibid. (internal quotation marks omitted), and the
evidence was therefore admissible under the good-faith
rule of United States v. Leon, 468 U. S. 897 (1984).
  Other courts have required exclusion of evidence ob
tained through similar police errors, e.g., Hoay v. State,
348 Ark. 80, 86–87, 71 S. W. 3d 573, 577 (2002), so we
granted Herring’s petition for certiorari to resolve the
conflict, 552 U. S. ___ (2008). We now affirm the Eleventh
Circuit’s judgment.
4               HERRING v. UNITED STATES 


                     Opinion of the Court 


                             II 

  When a probable-cause determination was based on
reasonable but mistaken assumptions, the person sub
jected to a search or seizure has not necessarily been the
victim of a constitutional violation. The very phrase
“probable cause” confirms that the Fourth Amendment
does not demand all possible precision. And whether the
error can be traced to a mistake by a state actor or some
other source may bear on the analysis. For purposes of
deciding this case, however, we accept the parties’ as
sumption that there was a Fourth Amendment violation.
The issue is whether the exclusionary rule should be
applied.
                              A
  The Fourth Amendment protects “[t]he right of the
people to be secure in their persons, houses, papers, and
effects, against unreasonable searches and seizures,” but
“contains no provision expressly precluding the use of
evidence obtained in violation of its commands,” Arizona v.
Evans, 514 U. S. 1, 10 (1995). Nonetheless, our decisions
establish an exclusionary rule that, when applicable,
forbids the use of improperly obtained evidence at trial.
See, e.g., Weeks v. United States, 232 U. S. 383, 398 (1914).
We have stated that this judicially created rule is “de
signed to safeguard Fourth Amendment rights generally
through its deterrent effect.” United States v. Calandra,
414 U. S. 338, 348 (1974).
  In analyzing the applicability of the rule, Leon admon
ished that we must consider the actions of all the police
officers involved. 468 U. S., at 923, n. 24 (“It is necessary
to consider the objective reasonableness, not only of the
officers who eventually executed a warrant, but also of the
officers who originally obtained it or who provided infor
mation material to the probable-cause determination”).
The Coffee County officers did nothing improper. Indeed,
                      Cite as: 555 U. S. ____ (2009)                     5

                          Opinion of the Court

the error was noticed so quickly because Coffee County
requested a faxed confirmation of the warrant.
  The Eleventh Circuit concluded, however, that some
body in Dale County should have updated the computer
database to reflect the recall of the arrest warrant. The
court also concluded that this error was negligent, but did
not find it to be reckless or deliberate. 492 F. 3d, at 1218.1
That fact is crucial to our holding that this error is not
enough by itself to require “the extreme sanction of exclu
sion.” Leon, supra, at 916.
                              B
   1. The fact that a Fourth Amendment violation oc
curred—i.e., that a search or arrest was unreasonable—
does not necessarily mean that the exclusionary rule
applies. Illinois v. Gates, 462 U. S. 213, 223 (1983). In
deed, exclusion “has always been our last resort, not our
first impulse,” Hudson v. Michigan, 547 U. S. 586, 591
(2006), and our precedents establish important principles
that constrain application of the exclusionary rule.
   First, the exclusionary rule is not an individual right
and applies only where it “ ‘result[s] in appreciable deter
rence.’ ” Leon, supra, at 909 (quoting United States v.
Janis, 428 U. S. 433, 454 (1976)). We have repeatedly
rejected the argument that exclusion is a necessary conse
quence of a Fourth Amendment violation. Leon, supra, at
905–906; Evans, supra, at 13–14; Pennsylvania Bd. of
Probation and Parole v. Scott, 524 U. S. 357, 363 (1998).
Instead we have focused on the efficacy of the rule in
——————
  1 At an earlier point in its opinion, the Eleventh Circuit described the
error as “ ‘at the very least negligent,’ ” 492 F. 3d 1212, 1217 (2007)
(quoting Michigan v. Tucker, 417 U. S. 433, 447 (1974)). But in the
next paragraph, it clarified that the error was “a negligent failure to
act, not a deliberate or tactical choice to act,” 492 F. 3d, at 1218. The
question presented treats the error as a “negligen[t]” one, see Pet. for
Cert. i; Brief in Opposition (I), and both parties briefed the case on that
basis.
6                   HERRING v. UNITED STATES

                          Opinion of the Court

deterring Fourth Amendment violations in the future. See
Calandra, supra, at 347–355; Stone v. Powell, 428 U. S.
465, 486 (1976).2
   In addition, the benefits of deterrence must outweigh
the costs. Leon, supra, at 910. “We have never suggested
that the exclusionary rule must apply in every circum
stance in which it might provide marginal deterrence.”
Scott, supra, at 368. “[T]o the extent that application of
the exclusionary rule could provide some incremental
deterrent, that possible benefit must be weighed against
[its] substantial social costs.” Illinois v. Krull, 480 U. S.
340, 352–353 (1987) (internal quotation marks omitted).
The principal cost of applying the rule is, of course, letting
guilty and possibly dangerous defendants go free—
something that “offends basic concepts of the criminal
justice system.” Leon, supra, at 908. “[T]he rule’s costly
toll upon truth-seeking and law enforcement objectives
presents a high obstacle for those urging [its] application.”
Scott, supra, at 364–365 (internal quotation marks omit
ted); see also United States v. Havens, 446 U. S. 620, 626–
627 (1980); United States v. Payner, 447 U. S. 727, 734
(1980).
   These principles are reflected in the holding of Leon:
When police act under a warrant that is invalid for lack of
probable cause, the exclusionary rule does not apply if the
police acted “in objectively reasonable reliance” on the
subsequently invalidated search warrant. 468 U. S., at
922. We (perhaps confusingly) called this objectively
——————
    2 JUSTICEGINSBURG’s dissent champions what she describes as “ ‘a
more majestic conception’ of . . . the exclusionary rule,” post, at 5
(quoting Arizona v. Evans, 514 U. S. 1, 18 (1995) (STEVENS, J., dissent
ing)), which would exclude evidence even where deterrence does not
justify doing so. Majestic or not, our cases reject this conception, see,
e.g., United States v. Leon, 468 U. S. 897, 921, n. 22 (1984), and perhaps
for this reason, her dissent relies almost exclusively on previous dis
sents to support its analysis.
                     Cite as: 555 U. S. ____ (2009)                   7

                         Opinion of the Court

reasonable reliance “good faith.” Ibid., n. 23. In a com
panion case, Massachusetts v. Sheppard, 468 U. S. 981
(1984), we held that the exclusionary rule did not apply
when a warrant was invalid because a judge forgot to
make “clerical corrections” to it. Id., at 991.
  Shortly thereafter we extended these holdings to war
rantless administrative searches performed in good-faith
reliance on a statute later declared unconstitutional.
Krull, supra, at 349–350. Finally, in Evans, 514 U. S. 1,
we applied this good-faith rule to police who reasonably
relied on mistaken information in a court’s database that
an arrest warrant was outstanding. We held that a mis
take made by a judicial employee could not give rise to
exclusion for three reasons: The exclusionary rule was
crafted to curb police rather than judicial misconduct;
court employees were unlikely to try to subvert the Fourth
Amendment; and “most important, there [was] no basis for
believing that application of the exclusionary rule in
[those] circumstances” would have any significant effect in
deterring the errors. Id., at 15. Evans left unresolved
“whether the evidence should be suppressed if police
personnel were responsible for the error,”3 an issue not
argued by the State in that case, id., at 16, n. 5, but one
that we now confront.
  2. The extent to which the exclusionary rule is justified
by these deterrence principles varies with the culpability
of the law enforcement conduct. As we said in Leon, “an

——————
   3 We thus reject JUSTICE BREYER’s suggestion that Evans was entirely

“premised on a distinction between judicial errors and police errors,”
post, at 1 (dissenting opinion). Were that the only rationale for our
decision, there would have been no reason for us expressly and care
fully to leave police error unresolved. In addition, to the extent Evans
is viewed as presaging a particular result here, it is noteworthy that
the dissent’s view in that case was that the distinction JUSTICE BREYER
regards as determinative was instead “artificial.” 514 U. S., at 29
(GINSBURG, J., dissenting).
8               HERRING v. UNITED STATES

                     Opinion of the Court

assessment of the flagrancy of the police misconduct con
stitutes an important step in the calculus” of applying the
exclusionary rule. 468 U. S., at 911. Similarly, in Krull
we elaborated that “evidence should be suppressed ‘only if
it can be said that the law enforcement officer had knowl
edge, or may properly be charged with knowledge, that the
search was unconstitutional under the Fourth Amend
ment.’ ” 480 U. S., at 348–349 (quoting United States v.
Peltier, 422 U. S. 531, 542 (1975)).
   Anticipating the good-faith exception to the exclusionary
rule, Judge Friendly wrote that “[t]he beneficent aim of
the exclusionary rule to deter police misconduct can be
sufficiently accomplished by a practice . . . outlawing
evidence obtained by flagrant or deliberate violation of
rights.” The Bill of Rights as a Code of Criminal Proce
dure, 53 Calif. L. Rev. 929, 953 (1965) (footnotes omitted);
see also Brown v. Illinois, 422 U. S. 590, 610–611 (1975)
(Powell, J., concurring in part) (“[T]he deterrent value of
the exclusionary rule is most likely to be effective” when
“official conduct was flagrantly abusive of Fourth Amend
ment rights”).
   Indeed, the abuses that gave rise to the exclusionary
rule featured intentional conduct that was patently un
constitutional. In Weeks, 232 U. S. 383, a foundational
exclusionary rule case, the officers had broken into the
defendant’s home (using a key shown to them by a
neighbor), confiscated incriminating papers, then returned
again with a U. S. Marshal to confiscate even more. Id., at
386. Not only did they have no search warrant, which the
Court held was required, but they could not have gotten
one had they tried. They were so lacking in sworn and
particularized information that “not even an order of court
would have justified such procedure.” Id., at 393–394.
Silverthorne Lumber Co. v. United States, 251 U. S. 385
(1920), on which petitioner repeatedly relies, was similar;
federal officials “without a shadow of authority” went to
                      Cite as: 555 U. S. ____ (2009)                      9

                           Opinion of the Court

the defendants’ office and “made a clean sweep” of every
paper they could find. Id., at 390. Even the Government
seemed to acknowledge that the “seizure was an outrage.”
Id., at 391.
   Equally flagrant conduct was at issue in Mapp v. Ohio,
367 U. S. 643 (1961), which overruled Wolf v. Colorado,
338 U. S. 25 (1949), and extended the exclusionary rule to
the States. Officers forced open a door to Ms. Mapp’s
house, kept her lawyer from entering, brandished what
the court concluded was a false warrant, then forced her
into handcuffs and canvassed the house for obscenity. 367
U. S., at 644–645. See Friendly, supra, at 953, and n. 127
(“[T]he situation in Mapp” featured a “flagrant or deliber
ate violation of rights”). An error that arises from nonre
curring and attenuated negligence is thus far removed
from the core concerns that led us to adopt the rule in the
first place. And in fact since Leon, we have never applied
the rule to exclude evidence obtained in violation of the
Fourth Amendment, where the police conduct was no more
intentional or culpable than this.
   3. To trigger the exclusionary rule, police conduct must
be sufficiently deliberate that exclusion can meaningfully
deter it, and sufficiently culpable that such deterrence is
worth the price paid by the justice system. As laid out in
our cases, the exclusionary rule serves to deter deliberate,
reckless, or grossly negligent conduct, or in some circum
stances recurring or systemic negligence. The error in this
case does not rise to that level.4
   Our decision in Franks v. Delaware, 438 U. S. 154
——————
   4 We do not quarrel with JUSTICE GINSBURG’s claim that “liability for

negligence . . . creates an incentive to act with greater care,” post, at 7,
and we do not suggest that the exclusion of this evidence could have no
deterrent effect. But our cases require any deterrence to “be weighed
against the ‘substantial social costs exacted by the exclusionary rule,’ ”
Illinois v. Krull, 480 U. S. 340, 352–353 (1987) (quoting Leon, 468 U. S.,
at 907), and here exclusion is not worth the cost.
10              HERRING v. UNITED STATES

                     Opinion of the Court

(1978), provides an analogy. Cf. Leon, supra, at 914. In
Franks, we held that police negligence in obtaining a
warrant did not even rise to the level of a Fourth Amend
ment violation, let alone meet the more stringent test for
triggering the exclusionary rule. We held that the Consti
tution allowed defendants, in some circumstances, “to
challenge the truthfulness of factual statements made in
an affidavit supporting the warrant,” even after the war
rant had issued. 438 U. S., at 155–156. If those false
statements were necessary to the Magistrate Judge’s
probable-cause determination, the warrant would be
“voided.” Ibid. But we did not find all false statements
relevant: “There must be allegations of deliberate false
hood or of reckless disregard for the truth,” and
“[a]llegations of negligence or innocent mistake are insuf
ficient.” Id., at 171.
   Both this case and Franks concern false information
provided by police. Under Franks, negligent police mis
communications in the course of acquiring a warrant do
not provide a basis to rescind a warrant and render a
search or arrest invalid. Here, the miscommunications
occurred in a different context—after the warrant had
been issued and recalled—but that fact should not require
excluding the evidence obtained.
   The pertinent analysis of deterrence and culpability is
objective, not an “inquiry into the subjective awareness of
arresting officers,” Reply Brief for Petitioner 4–5. See also
post, at 10, n. 7 (GINSBURG, J., dissenting). We have
already held that “our good-faith inquiry is confined to the
objectively ascertainable question whether a reasonably
well trained officer would have known that the search was
illegal” in light of “all of the circumstances.” Leon, 468
U. S., at 922, n. 23. These circumstances frequently in
clude a particular officer’s knowledge and experience, but
that does not make the test any more subjective than the
one for probable cause, which looks to an officer’s knowl
                  Cite as: 555 U. S. ____ (2009)           11

                      Opinion of the Court

edge and experience, Ornelas v. United States, 517 U. S.
690, 699–700 (1996), but not his subjective intent, Whren
v. United States, 517 U. S. 806, 812–813 (1996).
   4. We do not suggest that all recordkeeping errors by
the police are immune from the exclusionary rule. In this
case, however, the conduct at issue was not so objectively
culpable as to require exclusion. In Leon we held that “the
marginal or nonexistent benefits produced by suppressing
evidence obtained in objectively reasonable reliance on a
subsequently invalidated search warrant cannot justify
the substantial costs of exclusion.” 468 U. S., at 922. The
same is true when evidence is obtained in objectively
reasonable reliance on a subsequently recalled warrant.
   If the police have been shown to be reckless in maintain
ing a warrant system, or to have knowingly made false
entries to lay the groundwork for future false arrests,
exclusion would certainly be justified under our cases
should such misconduct cause a Fourth Amendment viola
tion. We said as much in Leon, explaining that an officer
could not “obtain a warrant on the basis of a ‘bare bones’
affidavit and then rely on colleagues who are ignorant of
the circumstances under which the warrant was obtained
to conduct the search.” Id., at 923, n. 24 (citing Whiteley v.
Warden, Wyo. State Penitentiary, 401 U. S. 560, 568
(1971)). Petitioner’s fears that our decision will cause
police departments to deliberately keep their officers
ignorant, Brief for Petitioner 37–39, are thus unfounded.
   The dissent also adverts to the possible unreliability of a
number of databases not relevant to this case. Post, at 8–
9. In a case where systemic errors were demonstrated, it
might be reckless for officers to rely on an unreliable
warrant system. See Evans, 514 U. S., at 17 (O’Connor,
J., concurring) (“Surely it would not be reasonable for the
police to rely . . . on a recordkeeping system . . . that rou
tinely leads to false arrests” (second emphasis added));
Hudson, 547 U. S., at 604 (KENNEDY, J., concurring) (“If a
12                  HERRING v. UNITED STATES

                          Opinion of the Court

widespread pattern of violations were shown . . . there
would be reason for grave concern” (emphasis added)).
But there is no evidence that errors in Dale County’s
system are routine or widespread. Officer Anderson testi
fied that he had never had reason to question information
about a Dale County warrant, App. 27, and both Sandy
Pope and Sharon Morgan testified that they could remem
ber no similar miscommunication ever happening on their
watch, id., at 33, 61–62. That is even less error than in
the database at issue in Evans, where we also found reli
ance on the database to be objectively reasonable. 514
U. S., at 15 (similar error “every three or four years”).
Because no such showings were made here, see 451
F. Supp. 2d, at 1292,5 the Eleventh Circuit was correct to
affirm the denial of the motion to suppress.
                        *     *     *
   Petitioner’s claim that police negligence automatically
triggers suppression cannot be squared with the principles
underlying the exclusionary rule, as they have been ex
plained in our cases. In light of our repeated holdings that
the deterrent effect of suppression must be substantial
and outweigh any harm to the justice system, e.g., Leon,
468 U. S., at 909–910, we conclude that when police mis
takes are the result of negligence such as that described
here, rather than systemic error or reckless disregard of
——————
  5 JUSTICE GINSBURG notes that at an earlier suppression hearing Mor
gan testified—apparently in confusion—that there had been miscom
munications “[s]everal times.” Post, at 3, n. 2 (quoting App. to Pet. for
Cert. 17a). When she later realized that she had misspoken, Morgan
emphatically corrected the record. App. 61–62. Noting this, the Dis
trict Court found that “Morgan’s ‘several times’ statement is confusing
and essentially unhelpful,” and concluded that there was “no credible
evidence of routine problems with disposing of recalled warrants.” 451
F. Supp. 2d, at 1292. This factual determination, supported by the
record and credited by the Court of Appeals, see 492 F. 3d, at 1219, is of
course entitled to deference.
                  Cite as: 555 U. S. ____ (2009)           13

                      Opinion of the Court

constitutional requirements, any marginal deterrence does
not “pay its way.” Id., at 907–908, n. 6 (internal quotation
marks omitted). In such a case, the criminal should not
“go free because the constable has blundered.” People v.
Defore, 242 N. Y. 13, 21, 150 N. E. 585, 587 (1926) (opinion
of the Court by Cardozo, J.).
   The judgment of the Court of Appeals for the Eleventh
Circuit is affirmed.
                                             It is so ordered.
                 Cite as: 555 U. S. ____ (2009)           1

                   GINSBURG, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 07–513
                         _________________


 BENNIE DEAN HERRING, PETITIONER v. UNITED 

                 STATES 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

          APPEALS FOR THE ELEVENTH CIRCUIT

                      [January 14, 2009] 


    JUSTICE GINSBURG, with whom JUSTICE STEVENS,
JUSTICE SOUTER, and JUSTICE BREYER join, dissenting.
    Petitioner Bennie Dean Herring was arrested, and
subjected to a search incident to his arrest, although no
warrant was outstanding against him, and the police
lacked probable cause to believe he was engaged in crimi
nal activity. The arrest and ensuing search therefore
violated Herring’s Fourth Amendment right “to be secure
. . . against unreasonable searches and seizures.” The
Court of Appeals so determined, and the Government does
not contend otherwise. The exclusionary rule provides
redress for Fourth Amendment violations by placing the
government in the position it would have been in had
there been no unconstitutional arrest and search. The
rule thus strongly encourages police compliance with the
Fourth Amendment in the future. The Court, however,
holds the rule inapplicable because careless recordkeeping
by the police—not flagrant or deliberate misconduct—
accounts for Herring’s arrest.
    I would not so constrict the domain of the exclusionary
rule and would hold the rule dispositive of this case: “[I]f
courts are to have any power to discourage [police] error of
[the kind here at issue], it must be through the application
of the exclusionary rule.” Arizona v. Evans, 514 U. S. 1,
22–23 (1995) (STEVENS, J., dissenting). The unlawful
2               HERRING v. UNITED STATES

                   GINSBURG, J., dissenting

search in this case was contested in court because the
police found methamphetamine in Herring’s pocket and a
pistol in his truck. But the “most serious impact” of the
Court’s holding will be on innocent persons “wrongfully
arrested based on erroneous information [carelessly main
tained] in a computer data base.” Id., at 22.
                               I
  A warrant for Herring’s arrest was recalled in February
2004, apparently because it had been issued in error. See
Brief for Petitioner 3, n. 1 (citing App. 63). The warrant
database for the Dale County Sheriff’s Department, how
ever, does not automatically update to reflect such
changes. App. 39–40, 43, 45. A member of the Dale
County Sheriff’s Department—whom the parties have not
identified—returned the hard copy of the warrant to the
County Circuit Clerk’s office, but did not correct the De
partment’s database to show that the warrant had been
recalled. Id., at 60. The erroneous entry for the warrant
remained in the database, undetected, for five months.
  On a July afternoon in 2004, Herring came to the Coffee
County Sheriff’s Department to retrieve his belongings
from a vehicle impounded in the Department’s lot. Id., at
17. Investigator Mark Anderson, who was at the Depart
ment that day, knew Herring from prior interactions:
Herring had told the district attorney, among others, of
his suspicion that Anderson had been involved in the
killing of a local teenager, and Anderson had pursued
Herring to get him to drop the accusations. Id., at 63–64.
Informed that Herring was in the impoundment lot,
Anderson asked the Coffee County warrant clerk whether
there was an outstanding warrant for Herring’s arrest.
Id., at 18. The clerk, Sandy Pope, found no warrant. Id.,
at 19.
  Anderson then asked Pope to call the neighboring Dale
County Sheriff’s Department to inquire whether a warrant
                     Cite as: 555 U. S. ____ (2009)                     3

                        GINSBURG, J., dissenting

to arrest Herring was outstanding there. Upon receiving
Pope’s phone call, Sharon Morgan, the warrant clerk for
the Dale County Department, checked her computer data
base. As just recounted, that Department’s database
preserved an error. Morgan’s check therefore showed—
incorrectly—an active warrant for Herring’s arrest. Id., at
41. Morgan gave the misinformation to Pope, ibid., who
relayed it to Investigator Anderson, id., at 35. Armed with
the report that a warrant existed, Anderson promptly
arrested Herring and performed an incident search min
utes before detection of the error.
  The Court of Appeals concluded, and the Government
does not contest, that the “failure to bring the [Dale
County Sheriff’s Department] records up to date [was] ‘at
the very least negligent.’ ” 492 F. 3d 1212, 1217 (CA11
2007) (quoting Michigan v. Tucker, 417 U. S. 433, 447
(1974)). And it is uncontested here that Herring’s arrest
violated his Fourth Amendment rights. The sole question
presented, therefore, is whether evidence the police ob
tained through the unlawful search should have been
suppressed.1 The Court holds that suppression was un
warranted because the exclusionary rule’s “core concerns”
are not raised by an isolated, negligent recordkeeping
error attenuated from the arrest. Ante, at 9, 12.2 In my
view, the Court’s opinion underestimates the need for a
forceful exclusionary rule and the gravity of recordkeeping
——————
  1 That   the recordkeeping error occurred in Dale County rather than
Coffee County is inconsequential in the suppression analysis. As the
Court notes, “we must consider the actions of all the police officers
involved.” Ante, at 4. See also United States v. Leon, 468 U. S. 897,
923, n. 24 (1984).
   2 It is not altogether clear how “isolated” the error was in this case.

When the Dale County Sheriff’s Department warrant clerk was first
asked: “[H]ow many times have you had or has Dale County had
problems, any problems with communicating about warrants,” she
responded: “Several times.” App. to Pet. for Cert. 17a (internal quota
tion marks omitted).
4                HERRING v. UNITED STATES

                    GINSBURG, J., dissenting

errors in law enforcement.
                               II 

                               A

  The Court states that the exclusionary rule is not a
defendant’s right, ante, at 5; rather, it is simply a remedy
applicable only when suppression would result in appre
ciable deterrence that outweighs the cost to the justice
system, ante, at 12. See also ante, at 9 (“[T]he exclusion
ary rule serves to deter deliberate, reckless, or grossly
negligent conduct, or in some circumstances recurring or
systemic negligence.”).
  The Court’s discussion invokes a view of the exclusion
ary rule famously held by renowned jurists Henry J.
Friendly and Benjamin Nathan Cardozo. Over 80 years
ago, Cardozo, then seated on the New York Court of Ap
peals, commented critically on the federal exclusionary
rule, which had not yet been applied to the States. He
suggested that in at least some cases the rule exacted too
high a price from the criminal justice system. See People
v. Defore, 242 N. Y. 13, 24–25, 150 N. E. 585, 588–589
(1926).    In words often quoted, Cardozo questioned
whether the criminal should “go free because the constable
has blundered.” Id., at 21, 150 N. E., at 587.
  Judge Friendly later elaborated on Cardozo’s query.
“The sole reason for exclusion,” Friendly wrote, “is that
experience has demonstrated this to be the only effective
method for deterring the police from violating the Consti
tution.” The Bill of Rights as a Code of Criminal Proce
dure, 53 Calif. L. Rev. 929, 951 (1965). He thought it
excessive, in light of the rule’s aim to deter police conduct,
to require exclusion when the constable had merely “blun
dered”—when a police officer committed a technical error
in an on-the-spot judgment, id., at 952, or made a “slight
and unintentional miscalculation,” id., at 953. As the
Court recounts, Judge Friendly suggested that deterrence
                 Cite as: 555 U. S. ____ (2009)            5

                   GINSBURG, J., dissenting

of police improprieties could be “sufficiently accomplished”
by confining the rule to “evidence obtained by flagrant or
deliberate violation of rights.” Ibid.; ante, at 8.
                             B
   Others have described “a more majestic conception” of
the Fourth Amendment and its adjunct, the exclusionary
rule. Evans, 514 U. S., at 18 (STEVENS, J., dissenting).
Protective of the fundamental “right of the people to be
secure in their persons, houses, papers, and effects,” the
Amendment “is a constraint on the power of the sovereign,
not merely on some of its agents.” Ibid. (internal quota
tion marks omitted); see Stewart, The Road to Mapp v.
Ohio and Beyond: The Origins, Development and Future
of the Exclusionary Rule in Search-and-Seizure Cases, 83
Colum. L. Rev. 1365 (1983). I share that vision of the
Amendment.
   The exclusionary rule is “a remedy necessary to ensure
that” the Fourth Amendment’s prohibitions “are observed
in fact.” Id., at 1389; see Kamisar, Does (Did) (Should)
The Exclusionary Rule Rest On A “Principled Basis”
Rather Than An “Empirical Proposition”? 16 Creighton
L. Rev. 565, 600 (1983). The rule’s service as an essential
auxiliary to the Amendment earlier inclined the Court to
hold the two inseparable. See Whiteley v. Warden, Wyo.
State Penitentiary, 401 U. S. 560, 568–569 (1971). Cf.
Olmstead v. United States, 277 U. S. 438, 469–471 (1928)
(Holmes, J., dissenting); id., at 477–479, 483–485
(Brandeis, J., dissenting).
   Beyond doubt, a main objective of the rule “is to deter—
to compel respect for the constitutional guaranty in the
only effectively available way—by removing the incentive
to disregard it.” Elkins v. United States, 364 U. S. 206,
217 (1960). But the rule also serves other important
purposes: It “enabl[es] the judiciary to avoid the taint of
partnership in official lawlessness,” and it “assur[es] the
6               HERRING v. UNITED STATES

                   GINSBURG, J., dissenting

people—all potential victims of unlawful government
conduct—that the government would not profit from its
lawless behavior, thus minimizing the risk of seriously
undermining popular trust in government.” United States
v. Calandra, 414 U. S. 338, 357 (1974) (Brennan, J., dis
senting). See also Terry v. Ohio, 392 U. S. 1, 13 (1968) (“A
rule admitting evidence in a criminal trial, we recognize,
has the necessary effect of legitimizing the conduct which
produced the evidence, while an application of the exclu
sionary rule withholds the constitutional imprimatur.”);
Kamisar, supra, at 604 (a principal reason for the exclu
sionary rule is that “the Court’s aid should be denied ‘in
order to maintain respect for law [and] to preserve the
judicial process from contamination’ ” (quoting Olmstead,
277 U. S., at 484 (Brandeis, J., dissenting)).
  The exclusionary rule, it bears emphasis, is often the
only remedy effective to redress a Fourth Amendment
violation. See Mapp v. Ohio, 367 U. S. 643, 652 (1961)
(noting “the obvious futility of relegating the Fourth
Amendment to the protection of other remedies”); Amster
dam, Perspectives on the Fourth Amendment, 58 Minn.
L. Rev. 349, 360 (1974) (describing the exclusionary rule
as “the primary instrument for enforcing the [F]ourth
[A]mendment”). Civil liability will not lie for “the vast
majority of [F]ourth [A]mendment violations—the fre
quent infringements motivated by commendable zeal, not
condemnable malice.” Stewart, 83 Colum. L. Rev., at
1389. Criminal prosecutions or administrative sanctions
against the offending officers and injunctive relief against
widespread violations are an even farther cry. See id., at
1386–1388.
                            III
  The Court maintains that Herring’s case is one in which
the exclusionary rule could have scant deterrent effect and
therefore would not “pay its way.” Ante, at 13 (internal
                 Cite as: 555 U. S. ____ (2009)            7

                    GINSBURG, J., dissenting

quotation marks omitted). I disagree.
                               A
   The exclusionary rule, the Court suggests, is capable of
only marginal deterrence when the misconduct at issue is
merely careless, not intentional or reckless. See ante, at 9,
11. The suggestion runs counter to a foundational premise
of tort law—that liability for negligence, i.e., lack of due
care, creates an incentive to act with greater care. The
Government so acknowledges. See Brief for United States
21; cf. Reply Brief 12.
   That the mistake here involved the failure to make a
computer entry hardly means that application of the
exclusionary rule would have minimal value. “Just as the
risk of respondeat superior liability encourages employers
to supervise . . . their employees’ conduct [more carefully],
so the risk of exclusion of evidence encourages policymak
ers and systems managers to monitor the performance of
the systems they install and the personnel employed to
operate those systems.” Evans, 514 U. S., at 29, n. 5
(GINSBURG, J., dissenting).
   Consider the potential impact of a decision applying the
exclusionary rule in this case. As earlier observed, see
supra, at 2, the record indicates that there is no electronic
connection between the warrant database of the Dale
County Sheriff’s Department and that of the County Cir
cuit Clerk’s office, which is located in the basement of the
same building. App. 39–40, 43, 45. When a warrant is
recalled, one of the “many different people that have ac
cess to th[e] warrants,” id., at 60, must find the hard copy
of the warrant in the “two or three different places” where
the department houses warrants, id., at 41, return it to
the Clerk’s office, and manually update the Department’s
database, see id., at 60. The record reflects no routine
practice of checking the database for accuracy, and the
failure to remove the entry for Herring’s warrant was not
8               HERRING v. UNITED STATES

                   GINSBURG, J., dissenting

discovered until Investigator Anderson sought to pursue
Herring five months later. Is it not altogether obvious
that the Department could take further precautions to
ensure the integrity of its database? The Sheriff’s De
partment “is in a position to remedy the situation and
might well do so if the exclusionary rule is there to remove
the incentive to do otherwise.” 1 W. LaFave, Search and
Seizure §1.8(e), p. 313 (4th ed. 2004). See also Evans, 514
U. S., at 21 (STEVENS, J., dissenting).
                             B
   Is the potential deterrence here worth the costs it im
poses? See ante, at 9. In light of the paramount impor
tance of accurate recordkeeping in law enforcement, I
would answer yes, and next explain why, as I see it,
Herring’s motion presents a particularly strong case for
suppression.
   Electronic databases form the nervous system of con
temporary criminal justice operations. In recent years,
their breadth and influence have dramatically expanded.
Police today can access databases that include not only the
updated National Crime Information Center (NCIC), but
also terrorist watchlists, the Federal Government’s em
ployee eligibility system, and various commercial data
bases. Brief for Electronic Privacy Information Center
(EPIC) et al. as Amicus Curiae 6. Moreover, States are
actively expanding information sharing between jurisdic
tions. Id., at 8–13. As a result, law enforcement has an
increasing supply of information within its easy electronic
reach. See Brief for Petitioner 36–37.
   The risk of error stemming from these databases is not
slim. Herring’s amici warn that law enforcement data
bases are insufficiently monitored and often out of date.
Brief for Amicus EPIC 13–28. Government reports de
                     Cite as: 555 U. S. ____ (2009)                     9

                        GINSBURG, J., dissenting

scribe, for example, flaws in NCIC databases,3 terrorist
watchlist databases,4 and databases associated with the
Federal Government’s employment eligibility verification
system.5
   Inaccuracies in expansive, interconnected collections of
electronic information raise grave concerns for individual
liberty. “The offense to the dignity of the citizen who is
arrested, handcuffed, and searched on a public street
simply because some bureaucrat has failed to maintain
an accurate computer data base” is evocative of the use
of general warrants that so outraged the authors of our
Bill of Rights. Evans, 514 U. S., at 23 (STEVENS, J.,
dissenting).
                              C
  The Court assures that “exclusion would certainly be
justified” if “the police have been shown to be reckless in
maintaining a warrant system, or to have knowingly
made false entries to lay the groundwork for future false
arrests.” Ante, at 11. This concession provides little
comfort.
  First, by restricting suppression to bookkeeping errors
that are deliberate or reckless, the majority leaves Her
ring, and others like him, with no remedy for violations of

——————
   3 See Dept. of Justice, Bureau of Justice Statistics, P. Brien, Improv

ing Access to and Integrity of Criminal History Records, NCJ 200581
(July 2005), available at http://www.ojp.usdoj.gov/bjs/pub/pdf/iaichr.pdf
(All Internet materials as visited Jan. 12, 2009, and included in Clerk
of Court’s case file.).
   4 See Dept. of Justice, Office of Inspector General, Audit of the U. S.

Department of Justice Terrorist Watchlist Nomination Processes, Audit
Rep. 08–16 (Mar. 2008), http://www.usdoj.gov/oig/reports/plus/a0816/
final.pdf.
   5 See Social Security Admin., Office of Inspector General, Congres

sional Response Report: Accuracy of the Social Security Administra
tion’s Numident File, A–08–06–26100 (Dec. 2006), http://www.ssa.gov/
oig/ADOBEPDF/A–08–06–26100.pdf.
10                  HERRING v. UNITED STATES

                        GINSBURG, J., dissenting

their constitutional rights. See supra, at 6. There can be
no serious assertion that relief is available under 42
U. S. C. §1983. The arresting officer would be sheltered by
qualified immunity, see Harlow v. Fitzgerald, 457 U. S.
800 (1982), and the police department itself is not liable
for the negligent acts of its employees, see Monell v. New
York City Dept. of Social Servs., 436 U. S. 658 (1978).
Moreover, identifying the department employee who com
mitted the error may be impossible.
   Second, I doubt that police forces already possess suffi
cient incentives to maintain up-to-date records. The Gov
ernment argues that police have no desire to send officers
out on arrests unnecessarily, because arrests consume
resources and place officers in danger. The facts of this
case do not fit that description of police motivation. Here
the officer wanted to arrest Herring and consulted the
Department’s records to legitimate his predisposition. See
App. 17–19.6
   Third, even when deliberate or reckless conduct is afoot,
the Court’s assurance will often be an empty promise: How
is an impecunious defendant to make the required show
ing? If the answer is that a defendant is entitled to dis
covery (and if necessary, an audit of police databases), see
Tr. of Oral Arg. 57–58, then the Court has imposed a
considerable administrative burden on courts and law
enforcement.7


——————
  6 It has been asserted that police departments have become suffi

ciently “professional” that they do not need external deterrence to avoid
Fourth Amendment violations. See Tr. of Oral Arg. 24–25; cf. Hudson
v. Michigan, 547 U. S. 586, 598–599 (2006). But professionalism is a
sign of the exclusionary rule’s efficacy—not of its superfluity.
  7 It is not clear how the Court squares its focus on deliberate conduct

with its recognition that application of the exclusionary rule does not
require inquiry into the mental state of the police. See ante, at 10;
Whren v. United States, 517 U. S. 806, 812–813 (1996).
                 Cite as: 555 U. S. ____ (2009)         11

                   GINSBURG, J., dissenting

                             IV
   Negligent recordkeeping errors by law enforcement
threaten individual liberty, are susceptible to deterrence
by the exclusionary rule, and cannot be remedied effec
tively through other means. Such errors present no occa
sion to further erode the exclusionary rule. The rule “is
needed to make the Fourth Amendment something real; a
guarantee that does not carry with it the exclusion of
evidence obtained by its violation is a chimera.” Ca
landra, 414 U. S., at 361 (Brennan, J., dissenting). In
keeping with the rule’s “core concerns,” ante, at 9, sup
pression should have attended the unconstitutional search
in this case.
                        *     *   *
   For the reasons stated, I would reverse the judgment of
the Eleventh Circuit.
                 Cite as: 555 U. S. ____ (2009)           1

                    BREYER, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 07–513
                         _________________


 BENNIE DEAN HERRING, PETITIONER v. UNITED 

                 STATES 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

          APPEALS FOR THE ELEVENTH CIRCUIT

                      [January 14, 2009] 


   JUSTICE BREYER, with whom JUSTICE SOUTER joins,
dissenting.
   I agree with JUSTICE GINSBURG and join her dissent. I
write separately to note one additional supporting factor
that I believe important. In Arizona v. Evans, 514 U. S. 1
(1995), we held that recordkeeping errors made by a court
clerk do not trigger the exclusionary rule, so long as the
police reasonably relied upon the court clerk’s recordkeep
ing. Id., at 14; id., at 16–17 (O’Connor, J., concurring).
The rationale for our decision was premised on a distinc
tion between judicial errors and police errors, and we gave
several reasons for recognizing that distinction.
   First, we noted that “the exclusionary rule was histori
cally designed as a means of deterring police misconduct,
not mistakes by court employees.” Id., at 14 (emphasis
added). Second, we found “no evidence that court employ
ees are inclined to ignore or subvert the Fourth Amend
ment or that lawlessness among these actors requires
application of the extreme sanction of exclusion.” Id., at
14–15. Third, we recognized that there was “no basis for
believing that application of the exclusionary rule. . .
[would] have a significant effect on court employees re
sponsible for informing the police that a warrant has been
quashed. Because court clerks are not adjuncts to the law
enforcement team engaged in the often competitive enter
2               HERRING v. UNITED STATES

                     BREYER, J., dissenting

prise of ferreting out crime, they have no stake in the
outcome of particular criminal prosecutions.” Id., at 15
(citation omitted). Taken together, these reasons explain
why police recordkeeping errors should be treated differ
ently than judicial ones.
   Other cases applying the “good faith” exception to the
exclusionary rule have similarly recognized the distinction
between police errors and errors made by others, such as
judicial officers or legislatures. See United States v. Leon,
468 U. S. 897 (1984) (police reasonably relied on magis
trate’s issuance of warrant); Massachusetts v. Sheppard,
468 U. S. 981 (1984) (same); Illinois v. Krull, 480 U. S. 340
(1987) (police reasonably relied on statute’s constitutional
ity).
   Distinguishing between police recordkeeping errors and
judicial ones not only is consistent with our precedent, but
also is far easier for courts to administer than THE CHIEF
JUSTICE’s case-by-case, multifactored inquiry into the
degree of police culpability. I therefore would apply the
exclusionary rule when police personnel are responsible
for a recordkeeping error that results in a Fourth Amend
ment violation.
   The need for a clear line, and the recognition of such a
line in our precedent, are further reasons in support of the
outcome that JUSTICE GINSBURG’s dissent would reach.

```

---

## GROUP: _overhaul2/lake/cases/Hester v. United States.json  (`lake-record`, 4 assertions)

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
{"assertion_id": "2c09c9dca1829584", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Hester v. United States"}, "payload": {"all": [{"cite": "265 U.S. 57", "page": "57", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "265"}, {"cite": "44 S. Ct. 445", "page": "445", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "44"}, {"cite": "68 L. Ed. 898", "page": "898", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "68"}, {"cite": "1924 U.S. LEXIS 2577", "page": "2577", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1924"}], "display": "265 U.S. 57", "official": {"cite": "265 U.S. 57", "page": "57", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "265"}, "official_selection_present": true, "record_id": "Hester v. United States"}}
{"assertion_id": "90ebef2ad4f32761", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-58", "record_id": "Hester v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-58", "pinpoint_status": "slip-only", "quote": "--- # Hester v. United States *265 U.S. 57 (1924)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Revenue officers, acting on information, went toward the house of Hester's father, where Hester lived, and concealed themselves fifty to one hundred yards away. They saw Hester hand a bottle to one Henderson; when an alarm was given, both men fled and dropped containers — a jug and a bottle — which broke but retained whiskey the officers recognized as illicitly distilled moonshine. A jar of whiskey was also found outside the house. The officers had no warrant, and Hester argued the examination occurred on his father's land. ## Issue Whether the warrantless observation and examination of containers a fleeing suspect discarded in a field outside the house violated the Fourth Amendment, where it was assumed the field belonged to the defendant's father. ## Rule No. A fleeing suspect who throws away containers abandons any Fourth Amendment interest in them:", "quote_fidelity": "mismatch", "record_id": "Hester v. United States", "star_marker": null}}
{"assertion_id": "9ea44ad7ece39b9d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-59", "record_id": "Hester v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-59", "pinpoint_status": "slip-only", "quote": "the special protection accorded by the Fourth Amendment to the people in their 'persons, houses, papers, and effects,' is not extended to the open fields. The distinction between the latter and the house is as old as the common law.", "quote_fidelity": "mismatch", "record_id": "Hester v. United States", "star_marker": null}}
{"assertion_id": "6b73aec8af104c74", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Hester v. United States"}, "payload": {"as_of_content": "1924-05-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Hester v. United States", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
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
