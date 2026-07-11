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

## GROUP: _overhaul2/lake/cases/Horton v. California.json  (`lake-record`, 6 assertions)

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
{"assertion_id": "c5acee3ac1d7d160", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Horton v. California"}, "payload": {"all": [{"cite": "496 U.S. 128", "page": "128", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "496"}, {"cite": "110 S. Ct. 2301", "page": "2301", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}, {"cite": "110 L. Ed. 2d 112", "page": "112", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}, {"cite": "1990 U.S. LEXIS 2937", "page": "2937", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1990"}], "display": "496 U.S. 128", "official": {"cite": "496 U.S. 128", "page": "128", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "496"}, "official_selection_present": true, "record_id": "Horton v. California"}}
{"assertion_id": "1f3c7aec20092b6b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-136a", "record_id": "Horton v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-136a", "pinpoint_status": "slip-only", "quote": "First, not only must the item be in plain view; its incriminating character must also be 'immediately apparent.'", "quote_fidelity": "mismatch", "record_id": "Horton v. California", "star_marker": null}}
{"assertion_id": "8624ca714e2acd09", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-130", "record_id": "Horton v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-130", "pinpoint_status": "slip-only", "quote": "--- # Horton v. California *496 U.S. 128 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A police officer had probable cause to search Horton's home for both the proceeds of an armed robbery and the weapons used in it, but the warrant he obtained described only the proceeds. Executing the warrant, the officer did not find the proceeds but did find the weapons (including a stun gun) in plain view and seized them. The officer admitted he had expected to find the weapons, so their discovery was not inadvertent. ## Issue Whether the warrantless seizure of evidence in plain view is barred by the Fourth Amendment when the officer's discovery of that evidence was not inadvertent. ## Rule No. The Court rejected inadvertence as a requirement:", "quote_fidelity": "mismatch", "record_id": "Horton v. California", "star_marker": null}}
{"assertion_id": "87d86fd5bc53da4d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-137", "record_id": "Horton v. California"}, "payload": {"fragment": "#:~:text=Second%2C%20not%20only%20must%20the", "page": null, "pin_id": "pin-137", "pinpoint_status": "star-verified", "quote": "Second, not only must the officer be lawfully located in a place from which the object can be plainly seen, but he or she must also have a lawful right of access to the object itself.", "quote_fidelity": "matched", "record_id": "Horton v. California", "star_marker": "137"}}
{"assertion_id": "d0721f4c986a551b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-136", "record_id": "Horton v. California"}, "payload": {"fragment": "#:~:text=It%20is%2C%20of%20course%2C%20an", "page": null, "pin_id": "pin-136", "pinpoint_status": "star-verified", "quote": "It is, of course, an essential predicate to any valid warrantless seizure of incriminating evidence that the officer did not violate the Fourth Amendment in arriving at the place from which the evidence could be plainly viewed.", "quote_fidelity": "matched", "record_id": "Horton v. California", "star_marker": "136"}}
{"assertion_id": "4480f9a9fb4feb16", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Horton v. California"}, "payload": {"as_of_content": "1990-06-04", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Horton v. California", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/Howes v. Fields.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Howes v. Fields"
type: case
citation: "565 U.S. 499 (2012)"
parallel_cite: "132 S. Ct. 1181; 182 L. Ed. 2d 17"
neutral_cite: "2012 U.S. LEXIS 1077; 2012 WL 538280"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2012
date_decided: 2012-02-21
docket: 10-680
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2012-02-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Howes v. Fields
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/623144/howes-v-fields/"
  cluster_id: 623144
  opinion_id: 623144
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Maryland v. Shatzer]]", "[[Berkemer v. McCarty]]", "[[Miranda v. Arizona]]", "[[Mathis v. United States]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "custody", "prisoners"]
holding: "Imprisonment alone does not make questioning custodial for Miranda; whether an inmate is \"in custody\" depends on the totality — here,…"
lake:
  record_id: Howes v. Fields
  status: verified
  projected_at: 2026-07-09
---

# Howes v. Fields

*565 U.S. 499 (2012)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Randall Fields, serving a sentence in a Michigan jail, was taken from his cell to a conference room and questioned by two sheriff's deputies for five to seven hours about conduct that allegedly occurred before he came to prison. He was told more than once that he was free to leave and return to his cell, was not restrained, and was given food and water; he confessed without receiving *[[Miranda v. Arizona|Miranda]]* warnings. The Sixth Circuit held that questioning a prisoner in isolation about outside conduct is custodial [[Common Legal Terms#per-se|per se]].

## Issue
Whether a prisoner is "in custody" for *[[Miranda v. Arizona|Miranda]]* purposes — requiring warnings — simply because he is incarcerated and is questioned in private about events occurring outside the prison.

## Rule
No; there is no categorical rule, and imprisonment by itself is not *[[Miranda v. Arizona|Miranda]]* custody. "Not all restraints on freedom of movement amount to custody for purposes of Miranda." — *Howes v. Fields*, 565 U.S. 499 (2012) (slip op., at 9). ^pin-op9

"If a break in custody can occur while a prisoner is serving an uninterrupted term of imprisonment, it must follow that imprisonment alone is not enough to create a custodial situation within the meaning of Miranda." — *Id.* (slip op., at [10](https://www.courtlistener.com/opinion/623144/howes-v-fields/#:~:text=If%20a%20break%20in%20custody%20can%20occur%20while)). ^pin-op10

Whether a prisoner is in custody depends on all the features of the interrogation, asking whether the environment presents the same inherently coercive pressures as station-house questioning.

## Application
Taking account of all the circumstances of Fields's interrogation — he was repeatedly told he could leave and return to his cell, was not physically restrained, was questioned in a well-lit conference room sometimes left open, and was offered food and water — a reasonable person in his position would have felt free to terminate the interview and go back to his cell, subject to the ordinary restraints of prison life. He was therefore not in custody, and no *[[Miranda v. Arizona|Miranda]]* warnings were required.

## Conclusion
Fields was not in *[[Miranda v. Arizona|Miranda]]* custody; the categorical rule applied below was rejected and the judgment reversed. Imprisonment alone does not make questioning custodial.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Howes* draws on [[Maryland v. Shatzer]] and [[Berkemer v. McCarty]] to hold that custody for [[Miranda v. Arizona]] turns on the totality of the interrogation's circumstances, not on the bare fact of incarceration.

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Howes v. Fields*, 565 U.S. 499 (2012) — https://www.courtlistener.com/opinion/623144/howes-v-fields/ — pinpoints given as slip-opinion pages (slip op., at 9, 10); CourtListener carries the slip opinion, paginated by slip page (opinion 623144).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a1f335c89ee7ff37", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Howes v. Fields"}, "payload": {"all": [{"cite": "132 S. Ct. 1181", "page": "1181", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "132"}, {"cite": "182 L. Ed. 2d 17", "page": "17", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "182"}, {"cite": "565 U.S. 499", "page": "499", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "565"}, {"cite": "2012 U.S. LEXIS 1077", "page": "1077", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2012"}, {"cite": "2012 WL 538280", "page": "538280", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2012"}], "display": "565 U.S. 499", "official": {"cite": "565 U.S. 499", "page": "499", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "565"}, "official_selection_present": true, "record_id": "Howes v. Fields"}}
{"assertion_id": "4be947150f1df0b6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op9", "record_id": "Howes v. Fields"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op9", "pinpoint_status": "slip-only", "quote": "for *Miranda* purposes — requiring warnings — simply because he is incarcerated and is questioned in private about events occurring outside the prison. ## Rule No; there is no categorical rule, and imprisonment by itself is not *Miranda* custody.", "quote_fidelity": "mismatch", "record_id": "Howes v. Fields", "star_marker": null}}
{"assertion_id": "7651d1a14fe69181", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op10", "record_id": "Howes v. Fields"}, "payload": {"fragment": "#:~:text=If%20a%20break%20in%20custody%20can%20occur%20while", "page": null, "pin_id": "pin-op10", "pinpoint_status": "slip-only", "quote": "If a break in custody can occur while a prisoner is serving an uninterrupted term of imprisonment, it must follow that imprisonment alone is not enough to create a custodial situation within the meaning of Miranda.", "quote_fidelity": "matched", "record_id": "Howes v. Fields", "star_marker": null}}
{"assertion_id": "3ac6d5f77d68d136", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Howes v. Fields"}, "payload": {"as_of_content": "2012-02-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Howes v. Fields", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Howes v. Fields

```json
{
  "schema_version": "s2.v1",
  "record_id": "Howes v. Fields",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Howes v. Fields",
    "case_name_short": "Howes",
    "case_name_full": "Howes, Warden v. Fields",
    "input_case_name": "Howes v. Fields",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2012-02-21",
    "year": 2012,
    "docket": "10-680",
    "cluster_id": 623144,
    "lead_opinion_id": 623144,
    "sibling_ids": [
      623144,
      9485375,
      9485376
    ],
    "absolute_url": "/opinion/623144/howes-v-fields/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "565 U.S. 499",
      "volume": "565",
      "reporter": "U.S.",
      "page": "499",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "132 S. Ct. 1181",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "1181",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "182 L. Ed. 2d 17",
        "volume": "182",
        "reporter": "L. Ed. 2d",
        "page": "17",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2012 U.S. LEXIS 1077",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "1077",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 WL 538280",
        "volume": "2012",
        "reporter": "WL",
        "page": "538280",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "132 S. Ct. 1181",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "1181",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "182 L. Ed. 2d 17",
        "volume": "182",
        "reporter": "L. Ed. 2d",
        "page": "17",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "565 U.S. 499",
        "volume": "565",
        "reporter": "U.S.",
        "page": "499",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 U.S. LEXIS 1077",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "1077",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 WL 538280",
        "volume": "2012",
        "reporter": "WL",
        "page": "538280",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "565 U.S. 499",
    "official_selection": {
      "court_class": "scotus",
      "selected": "565 U.S. 499",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op9",
      "page": null,
      "quote": "for *Miranda* purposes \u2014 requiring warnings \u2014 simply because he is incarcerated and is questioned in private about events occurring outside the prison. ## Rule No; there is no categorical rule, and imprisonment by itself is not *Miranda* custody.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op10",
      "page": null,
      "quote": "If a break in custody can occur while a prisoner is serving an uninterrupted term of imprisonment, it must follow that imprisonment alone is not enough to create a custodial situation within the meaning of Miranda.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 26225,
      "fragment": "#:~:text=If%20a%20break%20in%20custody%20can%20occur%20while",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2012-02-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Howes v. Fields",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Howes v. Fields:lane1_negative"
      },
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
        "journal_ref": "Howes v. Fields:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Cawthron",
          "cluster_id": 4500714,
          "cite": [
            "97 N.E.3d 671",
            "479 Mass. 612"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Mattox",
          "cluster_id": 4478290,
          "cite": [
            "2018 Ohio 992",
            "108 N.E.3d 1139"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane1_negative"
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
        "journal_ref": "Howes v. Fields:lane1_negative"
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
        "journal_ref": "Howes v. Fields:lane1_negative"
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
        "journal_ref": "Howes v. Fields:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Soto",
          "cluster_id": 4401346,
          "cite": [
            "2017 Ohio 4348",
            "93 N.E.3d 204"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane1_negative"
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
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Davis",
          "cluster_id": 4667521,
          "cite": [
            "2019 CO 84"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Todd Peterson v. Timothy Douma",
          "cluster_id": 2708669,
          "cite": [
            "751 F.3d 524",
            "2014 WL 1778150",
            "2014 U.S. App. LEXIS 8524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Ortiz, Octavio",
          "cluster_id": 2945879,
          "cite": [
            "382 S.W.3d 367",
            "2012 Tex. Crim. App. LEXIS 1386",
            "2012 WL 5348503"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
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
        "journal_ref": "Howes v. Fields:lane2_top_cited"
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
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Caro",
          "cluster_id": 4629272,
          "cite": [
            "248 Cal. Rptr. 3d 96",
            "7 Cal. 5th 463",
            "442 P.3d 316"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
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
        "journal_ref": "Howes v. Fields:lane2_top_cited"
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
        "journal_ref": "Howes v. Fields:lane2_top_cited"
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
        "journal_ref": "Howes v. Fields:lane2_top_cited"
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
        "journal_ref": "Howes v. Fields:lane2_top_cited"
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
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dishon McNary v. Marcus Hardy",
          "cluster_id": 821295,
          "cite": [
            "708 F.3d 905",
            "2013 WL 673653",
            "2013 U.S. App. LEXIS 3885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Andrew v. White",
          "cluster_id": 10318017,
          "cite": [
            "604 U.S. 86",
            "220 L. Ed. 2d 340",
            "145 S. Ct. 75"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Campbell v. Bradshaw",
          "cluster_id": 625704,
          "cite": [
            "674 F.3d 578",
            "2012 WL 913788",
            "2012 U.S. App. LEXIS 5735"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Timothy E. Dobbs",
          "cluster_id": 4765836,
          "cite": [
            "945 N.W.2d 609",
            "392 Wis. 2d 505",
            "2020 WI 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Owens v. Trammell",
          "cluster_id": 2814864,
          "cite": [
            "792 F.3d 1234",
            "2015 U.S. App. LEXIS 11687",
            "2015 WL 4081123"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William Morva v. David Zook",
          "cluster_id": 3201023,
          "cite": [
            "821 F.3d 517",
            "2016 U.S. App. LEXIS 8336",
            "2016 WL 2587362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Budder v. Addison",
          "cluster_id": 4377018,
          "cite": [
            "851 F.3d 1047",
            "2017 U.S. App. LEXIS 4988",
            "2017 WL 1056094"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. John Edward Barritt",
          "cluster_id": 4525400,
          "cite": [
            "926 N.W.2d 811",
            "325 Mich. App. 556"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Smith",
          "cluster_id": 4408805,
          "cite": [
            "2016 IL 119659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "BAUMRUK v. State",
          "cluster_id": 2546714,
          "cite": [
            "364 S.W.3d 518",
            "2012 WL 1339359",
            "2012 Mo. LEXIS 94"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ryan Holness",
          "cluster_id": 820254,
          "cite": [
            "706 F.3d 579",
            "2013 WL 491944",
            "2013 U.S. App. LEXIS 2834"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. William Little",
          "cluster_id": 3216832,
          "cite": [
            "499 Mich. 332"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Saldana",
          "cluster_id": 6239325,
          "cite": [
            "228 Cal. Rptr. 3d 1",
            "19 Cal. App. 5th 432"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Howes v. Fields:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(623144 OR 9485375 OR 9485376) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDc2NDAzMjAwMDAwJnM9NDMxMjM3MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28623144+OR+9485375+OR+9485376%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(623144 OR 9485375 OR 9485376)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNyZzPTQzMzEzNTkmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28623144+OR+9485375+OR+9485376%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(623144 OR 9485375 OR 9485376)",
        "reviewed": 61,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 61,
        "triage_read": 0,
        "triage_snippet_classified": 61
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(623144 OR 9485375 OR 9485376)",
    "indexed_citing_opinions": 331,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 623144,
        "count": 212,
        "count_source": "search"
      },
      {
        "opinion_id": 9485375,
        "count": 122,
        "count_source": "search"
      },
      {
        "opinion_id": 9485376,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 785,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/howes-v-fields.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxNjY5OTkmcz0xMDMxMzM5NSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28623144+OR+9485375+OR+9485376%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 623144,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 107676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 109587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 111023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 112452,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 117843,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 117982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 134748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 145122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 173739,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623144,
        "cited_id": 275662,
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
    "date_created": "2026-07-05T07:30:59Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:31:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:31:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:37:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:31:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Howes v. Fields

```
(Slip Opinion)              OCTOBER TERM, 2011                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                    HOWES, WARDEN v. FIELDS

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE SIXTH CIRCUIT

   No. 10–680.      Argued October 4, 2011—Decided February 21, 2012
Respondent Fields, a Michigan state prisoner, was escorted from his
  prison cell by a corrections officer to a conference room where he was
  questioned by two sheriff’s deputies about criminal activity he had al-
  legedly engaged in before coming to prison. At no time was Fields
  given Miranda warnings or advised that he did not have to speak
  with the deputies. As relevant here: Fields was questioned for be-
  tween five and seven hours; Fields was told more than once that he
  was free to leave and return to his cell; the deputies were armed, but
  Fields remained free of restraints; the conference room door was
  sometimes open and sometimes shut; several times during the inter-
  view Fields stated that he no longer wanted to talk to the deputies,
  but he did not ask to go back to his cell; after Fields confessed and
  the interview concluded, he had to wait an additional 20 minutes for
  an escort and returned to his cell well after the hour when he gener-
  ally retired.
    The trial court denied Fields’ motion to suppress his confession
  under Miranda v. Arizona, 384 U. S. 436, and he was convicted. The
  Michigan Court of Appeals affirmed, rejecting Fields’ contention that
  his statements should have been suppressed because he was subject-
  ed to custodial interrogation without a Miranda warning. The Unit-
  ed States District Court for the Eastern District of Michigan subse-
  quently granted Fields habeas relief under 28 U. S. C. §2254(d)(1).
  Affirming, the Sixth Circuit held that the interview was a custodial
  interrogation within the meaning of Miranda, reasoning that Mathis
  v. United States, 391 U. S. 1, “clearly established,” §2254(d)(1), that
  isolation from the general prison population, combined with question-
  ing about conduct occurring outside the prison, makes any such in-
  terrogation custodial per se.
2                         HOWES v. FIELDS

                                Syllabus

Held:
    1. This Court’s precedents do not clearly establish the categorical
 rule on which the Sixth Circuit relied. The Court has repeatedly de-
 clined to adopt any such rule. See, e.g., Illinois v. Perkins, 496 U. S.
 292. The Sixth Circuit misread Mathis, which simply held, as rele-
 vant here, that a prisoner who otherwise meets the requirements for
 Miranda custody is not taken outside the scope of Miranda because
 he was incarcerated for an unconnected offense. It did not hold that
 imprisonment alone constitutes Miranda custody. Nor does the
 statement in Maryland v. Shatzer, 559 U. S. ___, ___, that “[n]o one
 questions that [inmate] Shatzer was in custody for Miranda purpos-
 es” support a per se rule. It means only that the issue of custody was
 not contested in that case. Finally, contrary to respondent’s sugges-
 tion, Miranda itself did not hold that the inherently compelling pres-
 sures of custodial interrogation are always present when a prisoner is
 taken aside and questioned about events outside the prison walls.
 Pp. 4–7.
    2. The Sixth Circuit’s categorical rule—that imprisonment, ques-
 tioning in private, and questioning about events in the outside world
 create a custodial situation for Miranda purposes—is simply wrong.
 Pp. 8–13.
       (a) The initial step in determining whether a person is in Miran-
 da custody is to ascertain, given “all of the circumstances surround-
 ing the interrogation,” how a suspect would have gauged his freedom
 of movement. Stansbury v. California, 511 U. S. 318, 322, 325. How-
 ever, not all restraints on freedom of movement amount to Miranda
 custody. See, e.g., Berkemer v. McCarty, 468 U. S. 420, 423. Shatzer,
 distinguishing between restraints on freedom of movement and Mi-
 randa custody, held that a break in Miranda custody between a sus-
 pect’s invocation of the right to counsel and the initiation of subse-
 quent questioning may occur while a suspect is serving an
 uninterrupted term of imprisonment. If a break in custody can occur,
 it must follow that imprisonment alone is not enough to create a cus-
 todial situation within the meaning of Miranda. At least three strong
 grounds support this conclusion: Questioning a person who is already
 in prison does not generally involve the shock that very often accom-
 panies arrest; a prisoner is unlikely to be lured into speaking by a
 longing for prompt release; and a prisoner knows that his questioners
 probably lack authority to affect the duration of his sentence. Thus,
 service of a prison term, without more, is not enough to constitute
 Miranda custody. Pp. 8–12.
       (b) The other two elements in the Sixth Circuit’s rule are like-
 wise insufficient. Taking a prisoner aside for questioning may neces-
 sitate some additional limitations on the prisoner’s freedom of move-
                     Cite as: 565 U. S. ____ (2012)                     3

                                Syllabus

  ment, but it does not necessarily convert a noncustodial situation into
  Miranda custody. Isolation may contribute to a coercive atmosphere
  when a nonprisoner is questioned, but questioning a prisoner in pri-
  vate does not generally remove him from a supportive atmosphere
  and may be in his best interest. Neither does questioning a prisoner
  about criminal activity outside the prison have a significantly greater
  potential for coercion than questioning under otherwise identical cir-
  cumstances about criminal activity within the prison walls. The co-
  ercive pressure that Miranda guards against is neither mitigated nor
  magnified by the location of the conduct about which questions are
  asked. Pp. 12–13.
     3. When a prisoner is questioned, the determination of custody
  should focus on all of the features of the interrogation. The record in
  this case reveals that respondent was not taken into custody for Mi-
  randa purposes. While some of the facts lend support to his argu-
  ment that Miranda’s custody requirement was met, they are offset by
  others. Most important, he was told at the outset of the interroga-
  tion, and reminded thereafter, that he was free to leave and could go
  back to his cell whenever he wanted. Moreover, he was not physical-
  ly restrained or threatened, was interviewed in a well-lit, average-
  sized conference room where the door was sometimes left open, and
  was offered food and water. These facts are consistent with an envi-
  ronment in which a reasonable person would have felt free to termi-
  nate the interview and leave, subject to the ordinary restraints of life
  behind bars. Pp. 13–16.
617 F. 3d 813, reversed.

   ALITO, J., delivered the opinion of the Court, in which ROBERTS, C. J.,
and SCALIA, KENNEDY, THOMAS, and KAGAN, JJ., joined. GINSBURG, J.,
filed an opinion concurring in part and dissenting in part, in which
BREYER and SOTOMAYOR, JJ., joined.
                        Cite as: 565 U. S. ____ (2012)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 10–680
                                   _________________


CAROL HOWES, WARDEN, PETITIONER v. RANDALL
               LEE FIELDS
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE SIXTH CIRCUIT

                              [February 21, 2012]


   JUSTICE ALITO delivered the opinion of the Court.
   The United States Court of Appeals for the Sixth Circuit
held that our precedents clearly establish that a prisoner
is in custody within the meaning of Miranda v. Arizona,
384 U. S. 436 (1966), if the prisoner is taken aside and
questioned about events that occurred outside the prison
walls. Our decisions, however, do not clearly establish
such a rule, and therefore the Court of Appeals erred in
holding that this rule provides a permissible basis for
federal habeas relief under the relevant provision of the
Antiterrorism and Effective Death Penalty Act of 1996
(AEDPA), 28 U. S. C. §2254(d)(1). Indeed, the rule ap-
plied by the court below does not represent a correct inter-
pretation of our Miranda case law. We therefore reverse.
                                          I
  While serving a sentence in a Michigan jail, Randall
Fields was escorted by a corrections officer to a conference
room where two sheriff’s deputies questioned him about
allegations that, before he came to prison, he had engaged
in sexual conduct with a 12-year-old boy. In order to get to
the conference room, Fields had to go down one floor and
2                         HOWES v. FIELDS

                          Opinion of the Court

pass through a locked door that separated two sections
of the facility. See App. to Pet. for Cert. 66a, 69a. Fields
arrived at the conference room between 7 p.m. and 9 p.m.1
and was questioned for between five and seven hours.2
  At the beginning of the interview, Fields was told that
he was free to leave and return to his cell. See id., at 70a.
Later, he was again told that he could leave whenever he
wanted. See id., at 90a. The two interviewing deputies
were armed during the interview, but Fields remained free
of handcuffs and other restraints. The door to the confer-
ence room was sometimes open and sometimes shut. See
id., at 70a–75a.
  About halfway through the interview, after Fields had
been confronted with the allegations of abuse, he became
agitated and began to yell. See id., at 80a, 125a. Fields
testified that one of the deputies, using an expletive, told
him to sit down and said that “if [he] didn’t want to coop-
erate, [he] could leave.” Id., at 89a; see also id., at 70a–
71a. Fields eventually confessed to engaging in sex acts
with the boy. According to Fields’ testimony at a suppres-
sion hearing, he said several times during the interview
that he no longer wanted to talk to the deputies, but he
did not ask to go back to his cell prior to the end of the
interview. See id., at 92a–93a.
  When he was eventually ready to leave, he had to wait
——————
  1 Fields testified that he left his cell around 8 p.m. and that the in-

terview began around 8:30 p.m. App. to Pet. for Cert. 77a. Both the
Michigan Court of Appeals and the Sixth Circuit stated that the inter-
view began between 7 p.m. and 9 p.m. See id., at 4a, 54a.
  2 The Court of Appeals stated that the interview lasted for approxi-

mately seven hours, see id., at 4a, a figure that appears to be based
on the testimony of one of the interviewing deputies, see id., at 123a.
Fields put the number of hours between five and five and a half, saying
the interview began around 8:30 p.m. and continued until 1:30 a.m. or 2
a.m. See id., at 77a. The Michigan Court of Appeals stated that the
interview ended around midnight, which would put the length of the
interview at between three and five hours.
                    Cite as: 565 U. S. ____ (2012)                  3

                        Opinion of the Court

an additional 20 minutes or so because a corrections of-
ficer had to be summoned to escort him back to his cell,
and he did not return to his cell until well after the hour
when he generally retired.3 At no time was Fields given
Miranda warnings or advised that he did not have to
speak with the deputies.
   The State of Michigan charged Fields with criminal
sexual conduct. Relying on Miranda, Fields moved to
suppress his confession, but the trial court denied his
motion. Over the renewed objection of defense counsel,
one of the interviewing deputies testified at trial about
Fields’ admissions. The jury convicted Fields of two
counts of third-degree criminal sexual conduct, and the
judge sentenced him to a term of 10 to 15 years of impris-
onment. On direct appeal, the Michigan Court of Appeals
affirmed, rejecting Fields’ contention that his statements
should have been suppressed because he was subjected to
custodial interrogation without a Miranda warning. The
court ruled that Fields had not been in custody for pur-
poses of Miranda during the interview, so no Miranda
warnings were required. The court emphasized that
Fields was told that he was free to leave and return to his
cell but that he never asked to do so. The Michigan Su-
preme Court denied discretionary review.
   Fields then filed a petition for a writ of habeas corpus in
Federal District Court, and the court granted relief. The
Sixth Circuit affirmed, holding that the interview in the
conference room was a “custodial interrogation” within
the meaning of Miranda because isolation from the general
prison population combined with questioning about con-
duct occurring outside the prison makes any such interro-
gation custodial per se. The Court of Appeals reasoned
that this Court clearly established in Mathis v. United
——————
  3 Fields testified that his normal bedtime was 10:30 p.m. or 11 p.m.

See id., at 78a.
4                     HOWES v. FIELDS

                     Opinion of the Court

States, 391 U. S. 1 (1968), that “Miranda warnings must
be administered when law enforcement officers remove an
inmate from the general prison population and interrogate
him regarding criminal conduct that took place outside the
jail or prison.” 617 F. 3d 813, 820 (CA6 2010); see also id.,
at 818 (“The central holding of Mathis is that a Miranda
warning is required whenever an incarcerated individual
is isolated from the general prison population and interro-
gated, i.e.[,] questioned in a manner likely to lead to self-
incrimination, about conduct occurring outside of the
prison”). Because Fields was isolated from the general
prison population and interrogated about conduct occur-
ring in the outside world, the Court of Appeals found that
the state court’s decision was contrary to clearly estab-
lished federal law as determined by this Court in Mathis.
617 F. 3d, at 823.
   We granted certiorari. 562 U. S. ___ (2011).
                              II
  Under AEDPA, a federal court may grant a state pris-
oner’s application for a writ of habeas corpus if the state-
court adjudication pursuant to which the prisoner is held
“resulted in a decision that was contrary to, or involved an
unreasonable application of, clearly established Federal
law, as determined by the Supreme Court of the United
States.” 28 U. S. C. §2254(d)(1). In this context, “clearly
established law” signifies “the holdings, as opposed to the
dicta, of this Court’s decisions.” Williams v. Taylor, 529
U. S. 362, 412 (2000).
  In this case, it is abundantly clear that our precedents
do not clearly establish the categorical rule on which the
Court of Appeals relied, i.e., that the questioning of a
prisoner is always custodial when the prisoner is removed
from the general prison population and questioned about
events that occurred outside the prison. On the contrary,
we have repeatedly declined to adopt any categorical rule
                 Cite as: 565 U. S. ____ (2012)           5

                     Opinion of the Court

with respect to whether the questioning of a prison inmate
is custodial.
   In Illinois v. Perkins, 496 U. S. 292 (1990), where we
upheld the admission of un-Mirandized statements elicit-
ed from an inmate by an undercover officer masquerading
as another inmate, we noted that “[t]he bare fact of cus-
tody may not in every instance require a warning even when
the suspect is aware that he is speaking to an official, but
we do not have occasion to explore that issue here.” Id., at
299 (emphasis added). Instead, we simply “reject[ed] the
argument that Miranda warnings are required whenever
a suspect is in custody in a technical sense and converses
with someone who happens to be a government agent.”
Id., at 297.
   Most recently, in Maryland v. Shatzer, 559 U. S. ___
(2010), we expressly declined to adopt a bright-line rule
for determining the applicability of Miranda in prisons.
Shatzer considered whether a break in custody ends the
presumption of involuntariness established in Edwards v.
Arizona, 451 U. S. 477 (1981), and, if so, whether a prison-
er’s return to the general prison population after a custo-
dial interrogation constitutes a break in Miranda custody.
See 559 U. S., at ___ (slip op., at 3–4). In considering the
latter question, we noted first that “[w]e have never decid-
ed whether incarceration constitutes custody for Miranda
purposes, and have indeed explicitly declined to address
the issue.” Id., at ___ (slip op., at 13) (citing Perkins,
supra, at 299; emphasis added). The answer to this ques-
tion, we noted, would “depen[d] upon whether [incar-
ceration] exerts the coercive pressure that Miranda was
designed to guard against—the ‘danger of coercion [that]
results from the interaction of custody and official inter-
rogation.’ ” 559 U. S., at ___ (slip op., at 13) (quoting
Perkins, supra, at 297).
   In concluding that our precedents establish a categorical
rule, the Court of Appeals placed great weight on the
6                         HOWES v. FIELDS

                          Opinion of the Court

decision in Mathis, but the Court of Appeals misread the
holding in that case. In Mathis, an inmate in a state
prison was questioned by an Internal Revenue agent and
was subsequently convicted for federal offenses. The
Court of Appeals held that Miranda did not apply to this
interview for two reasons: A criminal investigation had
not been commenced at the time of the interview, and
the prisoner was incarcerated for an “unconnected offense.”
Mathis v. United States, 376 F. 2d 595, 597 (CA5 1967).
This Court rejected both of those grounds for distinguish-
ing Miranda, 391 U. S., at 4, and thus the holding in
Mathis is simply that a prisoner who otherwise meets the
requirements for Miranda custody is not taken outside the
scope of Miranda by either of the two factors on which
the Court of Appeals had relied. Mathis did not hold
that imprisonment, in and of itself, is enough to constitute
Miranda custody.4 Nor, contrary to respondent’s submis-
sion, see Brief for Respondent 14, did Oregon v. Mathia-
son, 429 U. S. 492, 494 (1977) (per curiam), which simply
restated in dictum the holding in Mathis.
   The Court of Appeals purported to find support for its
per se rule in Shatzer, relying on our statement that “[n]o
one questions that Shatzer was in custody for Miranda
purposes” when he was interviewed. 559 U. S., at ___ (slip
op., at 13). But this statement means only that the issue
of custody was not contested before us. It strains credulity
to read the statement as constituting an “unambiguous
conclusion” or “finding” by this Court that Shatzer was in
custody. 617 F. 3d, at 822.
   Finally, contrary to respondent’s suggestion, see Brief
for Respondent 12–15, Miranda itself did not clearly es-

——————
    4 Indeed,
            it is impossible to tell from either the opinion of this Court
or that of the court below whether the prisoner’s interview was routine
or whether there were special features that may have created an
especially coercive atmosphere.
                     Cite as: 565 U. S. ____ (2012)                    7

                          Opinion of the Court

tablish the rule applied by the Court of Appeals. Miranda
adopted a “set of prophylactic measures” designed to ward
off the “ ‘inherently compelling pressures’ of custodial
interrogation,” Shatzer, supra, at ___ (slip op., at 4) (quot-
ing Miranda, 384 U. S., at 467), but Miranda did not hold
that such pressures are always present when a prisoner
is taken aside and questioned about events outside the
prison walls. Indeed, Miranda did not even establish that
police questioning of a suspect at the station house is
always custodial. See Mathiason, supra, at 495 (declining
to find that Miranda warnings are required “simply be-
cause the questioning takes place in the station house, or
because the questioned person is one whom the police
suspect”).
  In sum, our decisions do not clearly establish that a
prisoner is always in custody for purposes of Miranda
whenever a prisoner is isolated from the general prison
population and questioned about conduct outside the
prison.5
——————
   5 The state-court decision applied the traditional context-specific

analysis to determine whether the circumstances of respondent’s
interrogation gave rise to “the coercive pressure that Miranda was
designed to guard against.” Shatzer, 559 U. S., at ___ (slip op., at 13).
The court first observed: “That a defendant is in prison for an unrelated
offense when being questioned does not, without more, mean that he
was in custody for the purpose of determining whether Miranda warn-
ings were required.” App. to Pet. for Cert. 56a (internal quotation
marks omitted and emphasis added). In this case, the court noted, the
“defendant was unquestionably in custody, but on a matter unrelated to
the interrogation.” Ibid. The Sixth Circuit concluded that the state
court thereby limited Miranda in a way rejected by Mathis v. United
States, 391 U. S. 1 (1968), and “curtail[ed] the warnings to be given
persons under interrogation by officers based on the reason why the
person is in custody.” Id., at 4–5. We think the better reading is that
the state court merely meant to draw a distinction between incarcera-
tion and Miranda custody. This reading is supported by the state
court’s subsequent consideration of whether the facts of the case were
likely to create an atmosphere of coercion. App. to Pet. for Cert. 56a.
8                     HOWES v. FIELDS

                     Opinion of the Court 


                            III

  Not only does the categorical rule applied below go well
beyond anything that is clearly established in our prior
decisions, it is simply wrong. The three elements of that
rule—(1) imprisonment, (2) questioning in private, and (3)
questioning about events in the outside world—are not
necessarily enough to create a custodial situation for
Miranda purposes.
                             A
   As used in our Miranda case law, “custody” is a term of
art that specifies circumstances that are thought generally
to present a serious danger of coercion. In determining
whether a person is in custody in this sense, the initial
step is to ascertain whether, in light of “the objective cir-
cumstances of the interrogation,” Stansbury v. Califor-
nia, 511 U. S. 318, 322–323, 325 (1994) (per curiam), a
“reasonable person [would] have felt he or she was not at
liberty to terminate the interrogation and leave.” Thomp-
son v. Keohane, 516 U. S. 99, 112 (1995). And in order to
determine how a suspect would have “gauge[d]” his “free-
dom of movement,” courts must examine “all of the cir-
cumstances surrounding the interrogation.” Stansbury,
supra, at 322, 325 (internal quotation marks omitted).
Relevant factors include the location of the questioning,
see Shatzer, supra, at ___–___ (slip op., at 13–16), its
duration, see Berkemer v. McCarty, 468 U. S. 420, 437–438
(1984), statements made during the interview, see Mathi-
ason, supra, at 495; Yarborough v. Alvarado, 541 U. S.
652, 665 (2004); Stansbury, supra, at 325, the presence or
absence of physical restraints during the questioning, see
New York v. Quarles, 467 U. S. 649, 655 (1984), and the
release of the interviewee at the end of the questioning,
see California v. Beheler, 463 U. S. 1121, 1122–1123
(1983) (per curiam).
   Determining whether an individual’s freedom of move-
                  Cite as: 565 U. S. ____ (2012)             9

                      Opinion of the Court

ment was curtailed, however, is simply the first step in the
analysis, not the last. Not all restraints on freedom of
movement amount to custody for purposes of Miranda.
We have “decline[d] to accord talismanic power” to the
freedom-of-movement inquiry, Berkemer, supra, at 437,
and have instead asked the additional question whether
the relevant environment presents the same inherently
coercive pressures as the type of station house questioning
at issue in Miranda. “Our cases make clear . . . that the
freedom-of-movement test identifies only a necessary and
not a sufficient condition for Miranda custody.” Shatzer,
559 U. S., at ___ (slip op., at 14).
   This important point is illustrated by our decision in
Berkemer v. McCarty, supra. In that case, we held that
the roadside questioning of a motorist who was pulled over
in a routine traffic stop did not constitute custodial inter-
rogation. Id., at 423, 441–442. We acknowledged that “a
traffic stop significantly curtails the ‘freedom of action’ of
the driver and the passengers,” and that it is generally “a
crime either to ignore a policeman’s signal to stop one’s car
or, once having stopped, to drive away without permis-
sion.” Id., at 436. “[F]ew motorists,” we noted, “would feel
free either to disobey a directive to pull over or to leave the
scene of a traffic stop without being told they might do so.”
Ibid. Nevertheless, we held that a person detained as a
result of a traffic stop is not in Miranda custody because
such detention does not “sufficiently impair [the detained
person’s] free exercise of his privilege against self-
incrimination to require that he be warned of his consti-
tutional rights.” 468 U. S., at 437. As we later put it,
the “temporary and relatively nonthreatening detention in-
volved in a traffic stop or Terry stop does not constitute
Miranda custody,” Shatzer, supra, at ___ (slip op., at 14)
(citation omitted). See Terry v. Ohio, 392 U. S. 1 (1968).
   It may be thought that the situation in Berkemer—the
questioning of a motorist subjected to a brief traffic stop—
10                    HOWES v. FIELDS

                      Opinion of the Court

is worlds away from those present when an inmate is
questioned in a prison, but the same cannot be said of
Shatzer, where we again distinguished between restraints
on freedom of movement and Miranda custody. Shatzer,
as noted, concerned the Edwards prophylactic rule, which
limits the ability of the police to initiate further question-
ing of a suspect in Miranda custody once the suspect
invokes the right to counsel. We held in Shatzer that this
rule does not apply when there is a sufficient break in
custody between the suspect’s invocation of the right to
counsel and the initiation of subsequent questioning. See
559 U. S., at ___ (slip op., at 13-16). And, what is signifi-
cant for present purposes, we further held that a break
in custody may occur while a suspect is serving a term in
prison. If a break in custody can occur while a prisoner is
serving an uninterrupted term of imprisonment, it must
follow that imprisonment alone is not enough to create a
custodial situation within the meaning of Miranda.
   There are at least three strong grounds for this conclu-
sion. First, questioning a person who is already serving a
prison term does not generally involve the shock that very
often accompanies arrest. In the paradigmatic Miranda
situation—a person is arrested in his home or on the
street and whisked to a police station for questioning—
detention represents a sharp and ominous change, and the
shock may give rise to coercive pressures. A person who is
“cut off from his normal life and companions,” Shatzer,
supra, at ___ (slip op., at 7), and abruptly transported from
the street into a “police-dominated atmosphere,” Miranda,
384 U. S., at 456, may feel coerced into answering
questions.
   By contrast, when a person who is already serving a
term of imprisonment is questioned, there is usually no
such change. “Interrogated suspects who have previously
been convicted of crime live in prison.” Shatzer, 559 U. S.,
at ___ (slip op., at 14). For a person serving a term of
                  Cite as: 565 U. S. ____ (2012)           11

                      Opinion of the Court

incarceration, we reasoned in Shatzer, the ordinary re-
strictions of prison life, while no doubt unpleasant, are
expected and familiar and thus do not involve the same
“inherently compelling pressures” that are often present
when a suspect is yanked from familiar surroundings in
the outside world and subjected to interrogation in a police
station. Id., at ___ (slip op., at 4).
  Second, a prisoner, unlike a person who has not been
sentenced to a term of incarceration, is unlikely to be
lured into speaking by a longing for prompt release. When
a person is arrested and taken to a station house for inter-
rogation, the person who is questioned may be pressured
to speak by the hope that, after doing so, he will be al-
lowed to leave and go home. On the other hand, when a
prisoner is questioned, he knows that when the question-
ing ceases, he will remain under confinement. Id., at ___–
___, n. 8 (slip op., at 14–15, n. 8).
  Third, a prisoner, unlike a person who has not been
convicted and sentenced, knows that the law enforcement
officers who question him probably lack the authority to
affect the duration of his sentence. Id., at ___–___ (slip
op., at 14–15). And “where the possibility of parole exists,”
the interrogating officers probably also lack the power to
bring about an early release. Ibid. “When the suspect has
no reason to think that the listeners have official power
over him, it should not be assumed that his words are
motivated by the reaction he expects from his listeners.”
Perkins, 496 U. S., at 297. Under such circumstances,
there is little “basis for the assumption that a suspect . . .
will feel compelled to speak by the fear of reprisal for
remaining silent or in the hope of [a] more lenient treat-
ment should he confess.” Id., at 296–297.
  In short, standard conditions of confinement and associ-
ated restrictions on freedom will not necessarily implicate
the same interests that the Court sought to protect when
it afforded special safeguards to persons subjected to
12                    HOWES v. FIELDS

                     Opinion of the Court

custodial interrogation. Thus, service of a term of impris-
onment, without more, is not enough to constitute Miran-
da custody.
                               B
   The two other elements included in the Court of Ap-
peals’ rule—questioning in private and questioning about
events that took place outside the prison—are likewise
insufficient.
   Taking a prisoner aside for questioning—as opposed
to questioning the prisoner in the presence of fellow in-
mates—does not necessarily convert a “noncustodial situa-
tion . . . to one in which Miranda applies.” Mathiason, 429
U. S., at 495. When a person who is not serving a prison
term is questioned, isolation may contribute to a coercive
atmosphere by preventing family members, friends, and
others who may be sympathetic from providing either
advice or emotional support. And without any such assis-
tance, the person who is questioned may feel overwhelm-
ing pressure to speak and to refrain from asking that the
interview be terminated.
   By contrast, questioning a prisoner in private does not
generally remove the prisoner from a supportive atmos-
phere. Fellow inmates are by no means necessarily
friends. On the contrary, they may be hostile and, for a
variety of reasons, may react negatively to what the ques-
tioning reveals. In the present case, for example, would
respondent have felt more at ease if he had been ques-
tioned in the presence of other inmates about the sexual
abuse of an adolescent boy? Isolation from the general
prison population is often in the best interest of the inter-
viewee and, in any event, does not suggest on its own
the atmosphere of coercion that concerned the Court in
Miranda.
   It is true that taking a prisoner aside for questioning
may necessitate some additional limitations on his free-
                 Cite as: 565 U. S. ____ (2012)           13

                     Opinion of the Court

dom of movement. A prisoner may, for example, be re-
moved from an exercise yard and taken, under close
guard, to the room where the interview is to be held. But
such procedures are an ordinary and familiar attribute of
life behind bars. Escorts and special security precautions
may be standard procedures regardless of the purpose for
which an inmate is removed from his regular routine and
taken to a special location. For example, ordinary prison
procedure may require such measures when a prisoner is
led to a meeting with an attorney.
   Finally, we fail to see why questioning about criminal
activity outside the prison should be regarded as having a
significantly greater potential for coercion than question-
ing under otherwise identical circumstances about crimi-
nal activity within the prison walls. In both instances,
there is the potential for additional criminal liability and
punishment. If anything, the distinction would seem to
cut the other way, as an inmate who confesses to miscon-
duct that occurred within the prison may also incur ad-
ministrative penalties, but even this is not enough to tip
the scale in the direction of custody. “The threat to a
citizen’s Fifth Amendment rights that Miranda was de-
signed to neutralize” is neither mitigated nor magnified by
the location of the conduct about which questions are
asked. Berkemer, 468 U. S., at 435, n. 22.
   For these reasons, the Court of Appeals’ categorical rule
is unsound.
                             IV 

                              A

   When a prisoner is questioned, the determination of
custody should focus on all of the features of the interroga-
tion. These include the language that is used in summon-
ing the prisoner to the interview and the manner in which
the interrogation is conducted. See Yarborough, 541 U. S.,
at 665. An inmate who is removed from the general prison
14                    HOWES v. FIELDS

                      Opinion of the Court

population for questioning and is “thereafter . . . subjected
to treatment” in connection with the interrogation “that
renders him ‘in custody’ for practical purposes . . . will be
entitled to the full panoply of protections prescribed by
Miranda.” Berkemer, 468 U. S., at 440.
   “Fidelity to the doctrine announced in Miranda requires
that it be enforced strictly, but only in those types of situa-
tions in which the concerns that powered the decision are
implicated.” Id., at 437; see Shatzer, 559 U. S., at ___ (slip
op., at 9); Mathiason, supra, at 495. Confessions voluntar-
ily made by prisoners in other situations should not be
suppressed. “Voluntary confessions are not merely a
proper element in law enforcement, they are an unmiti-
gated good, essential to society’s compelling interest in
finding, convicting, and punishing those who violate the
law.” Shatzer, supra, at ___ (slip op., at 9) (internal quota-
tion marks and citations omitted).
                              B
   The record in this case reveals that respondent was not
taken into custody for purposes of Miranda. To be sure,
respondent did not invite the interview or consent to it in
advance, and he was not advised that he was free to de-
cline to speak with the deputies. The following facts also
lend some support to respondent’s argument that Miran-
da’s custody requirement was met: The interview lasted
for between five and seven hours in the evening and con-
tinued well past the hour when respondent generally went
to bed; the deputies who questioned respondent were
armed; and one of the deputies, according to respondent,
“[u]sed a very sharp tone,” App. to Pet. for Cert. 76a, and,
on one occasion, profanity, see id., at 77a.
   These circumstances, however, were offset by others.
Most important, respondent was told at the outset of the
interrogation, and was reminded again thereafter, that he
could leave and go back to his cell whenever he wanted.
                     Cite as: 565 U. S. ____ (2012)                  15

                         Opinion of the Court

See id., at 89a–90a (“I was told I could get up and leave
whenever I wanted”); id., at 70a–71a. Moreover, respond-
ent was not physically restrained or threatened and was
interviewed in a well-lit, average-sized conference room,
where he was “not uncomfortable.” Id., at 90a; see id., at
71a, 88a–89a. He was offered food and water, and the
door to the conference room was sometimes left open. See
id., at 70a, 74a. “All of these objective facts are consistent
with an interrogation environment in which a reasonable
person would have felt free to terminate the interview and
leave.” Yarborough, supra, at 664–665.
   Because he was in prison, respondent was not free to
leave the conference room by himself and to make his own
way through the facility to his cell. Instead, he was es-
corted to the conference room and, when he ultimately
decided to end the interview, he had to wait about 20
minutes for a corrections officer to arrive and escort him to
his cell. But he would have been subject to this same
restraint even if he had been taken to the conference room
for some reason other than police questioning; under no
circumstances could he have reasonably expected to be
able to roam free.6 And while respondent testified that he
——————
    6 Respondent did not testify to the contrary. The following colloquy

occurred at his Miranda hearing:
“Q. You’re not generally allowed to just roam around Lenawee County
Jail on your own, are you?
“A. No, I never have.
“Q. So wouldn’t it make sense to you, since you had that experience,
that in fact you would have been escorted just like you were escorted
. . . into this conference room?
“A. That makes common sense.
“Q. So when they said that you were free to leave and you get up—
could get up and go and all you had to do was tell them you wanted to
go, in your mind, did you understand that to mean that somebody
would come get you and take you back to your cell?
“A. But that doesn’t give me freedom to just get up and walk away.
“Q. I understand it doesn’t—
“A. So, no.
16                        HOWES v. FIELDS

                         Opinion of the Court

“was told . . . if I did not want to cooperate, I needed to go
back to my cell,” these words did not coerce cooperation by
threatening harsher conditions. App. to Pet. for Cert. 71a;
see id., at 89a (“I was told, if I didn’t want to cooperate,
I could leave”). Returning to his cell would merely have
returned him to his usual environment. See Shatzer,
supra, at ___ (slip op., at 14) (“Interrogated suspects who
have previously been convicted of crime live in prison.
When they are released back into the general prison popu-
lation, they return to their accustomed surroundings and
daily routine—they regain the degree of control they had
over their lives prior to the interrogation”).
  Taking into account all of the circumstances of the
questioning—including especially the undisputed fact that
respondent was told that he was free to end the question-
ing and to return to his cell—we hold that respondent was
not in custody within the meaning of Miranda.
                         *    *     * 

     The judgment of the Court of Appeals is

                                                             Reversed.

—————— 

“Q. The question is this, sir, not whether you had freedom to get up

and walk away, but did you understand that what that meant was that

a jailer would come get you and— 

“A. No— 

“Q. —take you back to your cell?

“A. I did not understand that. 

“Q. You didn’t? 

“A. No. 

“Q. Why not? That’s how you got there.

“A. Because I did not know if a jailer would take me back or if one of

those gentlemen would take me back. 

“Q. But you understood that, if you asked, one of them or a jailer would 

take you back to your cell? 

“A. I assumed that. 

“Q. And you believed that to be true?

“A. I assumed that.” App. to Pet. for Cert. 91a–92a.

                 Cite as: 565 U. S. ____ (2012)           1

                    Opinion of GINSBURG, J.

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 10–680
                         _________________


CAROL HOWES, WARDEN, PETITIONER v. RANDALL
               LEE FIELDS
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE SIXTH CIRCUIT

                     [February 21, 2012]


   JUSTICE GINSBURG, with whom JUSTICE BREYER and
JUSTICE SOTOMAYOR join, concurring in part and dissent-
ing in part.
   Given this Court’s controlling decisions on what counts
as “custody” for Miranda purposes, I agree that the law is
not “clearly established” in respondent Fields’s favor. See,
e.g., Maryland v. Shatzer, 559 U. S. ___, ___ (2010) (slip
op., at 13–16); Thompson v. Keohane, 516 U. S. 99, 112
(1995). But I disagree with the Court’s further determina-
tion that Fields was not in custody under Miranda. Were
the case here on direct review, I would vote to hold that
Miranda precludes the State’s introduction of Fields’s
confession as evidence against him.
   Miranda v. Arizona, 384 U. S. 436 (1966), reacted to
police interrogation tactics that eroded the Fifth Amend-
ment’s ban on compulsory self-incrimination. The opinion
did so by requiring interrogators to convey to suspects
the now-familiar warnings: The suspect is to be informed,
prior to interrogation, that he “has a right to remain si-
lent, that any statement he does make may be used as
evidence against him, and that he has a right to the pres-
ence of an attorney, either retained or appointed.” Id., at
444.
   Under what circumstances are Miranda warnings re-
quired? Miranda tells us “in all settings in which [a per-
2                     HOWES v. FIELDS

                    Opinion of GINSBURG, J.

son’s] freedom of action is curtailed in any significant
way.” Id., at 467. Given the reality that police interroga-
tors “trad[e] on the weakness of individuals,” i.e., their
“insecurity about [themselves] or [their] surroundings,”
id., at 455, the Court found the preinterrogation warnings
set out in the opinion “indispensable,” id., at 469. Those
warnings, the Court elaborated, are “an absolute prerequi-
site in overcoming the inherent pressures of the interroga-
tion atmosphere,” id., at 468; they “insure” that the sus-
pect is timely told of his Fifth Amendment privilege, and
his freedom to exercise it, id., at 469.
   Fields, serving time for disorderly conduct, was, of
course, “i[n] custody,” but not “for purposes of Miranda,”
the Court concludes. Ante, at 14. I would not train, as the
Court does, on the question whether there can be custody
within custody. Instead, I would ask, as Miranda put it,
whether Fields was subjected to “incommunicado interro-
gation . . . in a police-dominated atmosphere,” 384 U. S., at
445, whether he was placed, against his will, in an inher-
ently stressful situation, see id., at 468, and whether his
“freedom of action [was] curtailed in any significant way,”
id., at 467. Those should be the key questions, and to each
I would answer “Yes.”
   As the Court acknowledges, Fields did not invite or
consent to the interview. Ante, at 14. He was removed
from his cell in the evening, taken to a conference room in
the sheriff ’s quarters, and questioned by two armed depu-
ties long into the night and early morning. Ibid. He was
not told at the outset that he had the right to decline to
speak with the deputies. Ibid. Shut in with the armed
officers, Fields felt “trapped.” App. to Pet. for Cert. 71a.
Although told he could return to his cell if he did not want
to cooperate, id., at 71a–72a, Fields believed the deputies
“would not have allowed [him] to leave the room,” id., at
72a. And with good reason. More than once, “he told the
officers . . . he did not want to speak with them anymore.”
                   Cite as: 565 U. S. ____ (2012)                 3

                      Opinion of GINSBURG, J.

617 F. 3d 813, 815 (CA6 2010). He was given water, App.
to Pet. for Cert. 74a, but not his evening medications,
id., at 79a.* Yet the Court concludes that Fields was in
“an interrogation environment in which a reasonable person
would have felt free to terminate the interview and leave.”
Ante, at 15 (quoting Yarborough v. Alvarado, 541 U. S.
652, 665 (2004)).
  Critical to the Court’s judgment is “the undisputed fact
that [Fields] was told that he was free to end the question-
ing and to return to his cell.” Ante, at 17. Never mind
the facts suggesting that Fields’s submission to the over-
night interview was anything but voluntary. Was Fields
“held for interrogation”? See Miranda, 384 U. S., at 471.
Brought to, and left alone with, the gun-bearing deputies,
he surely was in my judgment.
  Miranda instructed that such a person “must be clearly
informed that he has the right to consult with a lawyer
and to have the lawyer with him during interrogation.”
Ibid. Those warnings, along with “warnings of the right
to remain silent and that anything stated can be used in
evidence against [the speaker],” Miranda explained, are
necessary “prerequisite[s] to [an] interrogation” compati-
ble with the Fifth Amendment. Ibid. Today, for people
already in prison, the Court finds it adequate for the police
to say: “You are free to terminate this interrogation and
return to your cell.” Such a statement is no substitute for
one ensuring that an individual is aware of his rights.
  For the reasons stated, I would hold that the “incommu-
nicado interrogation [of Fields] in a police-dominated
atmosphere,” id., at 445, without informing him of his
rights, dishonored the Fifth Amendment privilege Miran-
da was designed to safeguard.
——————
  * Each night, Fields took an antidepressant and, due to his kidney
transplant surgery, two antirejection medications. App. to Pet. for
Cert. 79a.

```

---

## GROUP: _overhaul2/lake/cases/Hudson v. Michigan.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Hudson v. Michigan"
type: case
citation: "547 U.S. 586 (2006)"
parallel_cite: "126 S. Ct. 2159; 165 L. Ed. 2d 56"
neutral_cite: 2006 U.S. LEXIS 4677
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2006
date_decided: 2006-06-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2006-06-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hudson v. Michigan
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145646/hudson-v-michigan/"
  cluster_id: 145646
  opinion_id: 145646
  identity_checked: true
homes:
  - page: "[[Knock-and-Announce]]"
    role: "Key — Progeny / Refinement"
related: ["[[Wilson v. Arkansas]]", "[[Richards v. Wisconsin]]", "[[Mapp v. Ohio]]", "[[United States v. Leon]]"]
aliases: []
tags: ["case", "fourth-amendment", "knock-and-announce", "exclusionary-rule", "warrant"]
holding: "A knock-and-announce violation does NOT require suppression of the evidence found inside; the interests protected by knock-and-announce…"
lake:
  record_id: Hudson v. Michigan
  status: verified
  projected_at: 2026-07-06
---

# Hudson v. Michigan

*547 U.S. 586 (2006)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police executing a valid search warrant at Hudson's home announced their presence but waited only a short time — about three to five seconds — before entering. They found drugs and a firearm. Hudson moved to suppress, arguing the premature entry violated the Fourth Amendment's [[Knock-and-Announce|knock-and-announce]] requirement.

## Issue
Whether a violation of the [[Knock-and-Announce|knock-and-announce]] rule requires suppression of the evidence found in the ensuing search.

## Rule
No. The interests protected by the [[Knock-and-Announce|knock-and-announce]] rule are not the interests served by suppression. "What the knock-and-announce rule has never protected, however, is one's interest in preventing the government from seeing or taking evidence described in a warrant." — 547 U.S. at 594. ^pin-594

"Since the interests that were violated in this case have nothing to do with the seizure of the evidence, the exclusionary rule is inapplicable." — *Id.* ^pin-594a

## Application
The police had a valid warrant and would have discovered and seized the drugs and firearm regardless of how long they waited at the door; the [[Knock-and-Announce|knock-and-announce]] violation protected only interests in privacy, dignity, and avoiding property damage — not Hudson's interest in keeping the police from finding the described evidence. Because suppression would not vindicate the interests the rule protects and its deterrence benefits did not outweigh its substantial social costs, the evidence was not suppressed.

## Conclusion
A [[Knock-and-Announce|knock-and-announce]] violation does not trigger the exclusionary rule; the denial of suppression was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hudson* leaves the [[Knock-and-Announce|knock-and-announce]] requirement of [[Wilson v. Arkansas]] and [[Richards v. Wisconsin]] intact but withholds the exclusionary remedy for its violation, applying the cost-benefit, deterrence-focused approach of the modern exclusionary-rule cases.

## Appears on
- [[Knock-and-Announce]] — *Key — Progeny / Refinement*

## Sources
- *Hudson v. Michigan*, 547 U.S. 586 (2006) — https://www.courtlistener.com/opinion/145646/hudson-v-michigan/ — pinpoint: 594.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8c2eb1e7a9241197", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Hudson v. Michigan"}, "payload": {"all": [{"cite": "547 U.S. 586", "page": "586", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "547"}, {"cite": "126 S. Ct. 2159", "page": "2159", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "126"}, {"cite": "165 L. Ed. 2d 56", "page": "56", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "165"}, {"cite": "2006 U.S. LEXIS 4677", "page": "4677", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2006"}], "display": "547 U.S. 586", "official": {"cite": "547 U.S. 586", "page": "586", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "547"}, "official_selection_present": true, "record_id": "Hudson v. Michigan"}}
{"assertion_id": "3b368ebef1a6b3b8", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-594a", "record_id": "Hudson v. Michigan"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-594a", "pinpoint_status": "slip-only", "quote": "Since the interests that were violated in this case have nothing to do with the seizure of the evidence, the exclusionary rule is inapplicable.", "quote_fidelity": "mismatch", "record_id": "Hudson v. Michigan", "star_marker": null}}
{"assertion_id": "f45fba80f5288721", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-594", "record_id": "Hudson v. Michigan"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-594", "pinpoint_status": "slip-only", "quote": "--- # Hudson v. Michigan *547 U.S. 586 (2006)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police executing a valid search warrant at Hudson's home announced their presence but waited only a short time — about three to five seconds — before entering. They found drugs and a firearm. Hudson moved to suppress, arguing the premature entry violated the Fourth Amendment's knock-and-announce requirement. ## Issue Whether a violation of the knock-and-announce rule requires suppression of the evidence found in the ensuing search. ## Rule No. The interests protected by the knock-and-announce rule are not the interests served by suppression.", "quote_fidelity": "mismatch", "record_id": "Hudson v. Michigan", "star_marker": null}}
{"assertion_id": "192383edae71525a", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Hudson v. Michigan"}, "payload": {"as_of_content": "2006-06-15", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Hudson v. Michigan", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Hudson v. Michigan

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hudson v. Michigan",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hudson v. Michigan",
    "case_name_short": "Hudson",
    "case_name_full": "Hudson v. Michigan",
    "input_case_name": "Hudson v. Michigan",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2006-06-15",
    "year": 2006,
    "docket": null,
    "cluster_id": 145646,
    "lead_opinion_id": 145646,
    "sibling_ids": [
      145646,
      9434934,
      9434935,
      9434936
    ],
    "absolute_url": "/opinion/145646/hudson-v-michigan/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "547 U.S. 586",
      "volume": "547",
      "reporter": "U.S.",
      "page": "586",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "126 S. Ct. 2159",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "2159",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "165 L. Ed. 2d 56",
        "volume": "165",
        "reporter": "L. Ed. 2d",
        "page": "56",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2006 U.S. LEXIS 4677",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "4677",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "547 U.S. 586",
        "volume": "547",
        "reporter": "U.S.",
        "page": "586",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "126 S. Ct. 2159",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "2159",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "165 L. Ed. 2d 56",
        "volume": "165",
        "reporter": "L. Ed. 2d",
        "page": "56",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2006 U.S. LEXIS 4677",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "4677",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "547 U.S. 586",
    "official_selection": {
      "court_class": "scotus",
      "selected": "547 U.S. 586",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-594",
      "page": null,
      "quote": "--- # Hudson v. Michigan *547 U.S. 586 (2006)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police executing a valid search warrant at Hudson's home announced their presence but waited only a short time \u2014 about three to five seconds \u2014 before entering. They found drugs and a firearm. Hudson moved to suppress, arguing the premature entry violated the Fourth Amendment's knock-and-announce requirement. ## Issue Whether a violation of the knock-and-announce rule requires suppression of the evidence found in the ensuing search. ## Rule No. The interests protected by the knock-and-announce rule are not the interests served by suppression.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-594a",
      "page": null,
      "quote": "Since the interests that were violated in this case have nothing to do with the seizure of the evidence, the exclusionary rule is inapplicable.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2006-06-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hudson v. Michigan",
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
        "journal_ref": "Hudson v. Michigan:lane1_negative"
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
        "journal_ref": "Hudson v. Michigan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Christian",
          "cluster_id": 4643309,
          "cite": [
            "445 P.3d 183"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Sasiadek",
          "cluster_id": 7330153,
          "cite": [
            "310 F. Supp. 3d 371"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane1_negative"
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
        "journal_ref": "Hudson v. Michigan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Turpin",
          "cluster_id": 4423584,
          "cite": [
            "2017 Ohio 7435",
            "96 N.E.3d 1171"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Matthew Elliot Cohagan",
          "cluster_id": 4421478,
          "cite": [
            "162 Idaho 717",
            "404 P.3d 659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 4316369,
          "cite": [
            "2016 COA 150",
            "417 P.3d 868"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Johnny James Tims v. State of Florida",
          "cluster_id": 4302086,
          "cite": [
            "204 So. 3d 536",
            "2016 Fla. App. LEXIS 14742"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lajai Pridgette",
          "cluster_id": 4244999,
          "cite": [
            "831 F.3d 1253",
            "2016 U.S. App. LEXIS 14408",
            "2016 WL 4151222"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "McDonald v. City of Chicago",
          "cluster_id": 149702,
          "cite": [
            "177 L. Ed. 2d 894",
            "130 S. Ct. 3020",
            "561 U.S. 742",
            "2010 U.S. LEXIS 5523",
            "22 Fla. L. Weekly Fed. S 619",
            "78 U.S.L.W. 4844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Corley v. United States",
          "cluster_id": 145888,
          "cite": [
            "173 L. Ed. 2d 443",
            "129 S. Ct. 1558",
            "556 U.S. 303",
            "2009 U.S. LEXIS 2512"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Fred Snow, Marcus Snow, Rahad Ross",
          "cluster_id": 795598,
          "cite": [
            "462 F.3d 55",
            "2006 U.S. App. LEXIS 22613"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. State",
          "cluster_id": 2106367,
          "cite": [
            "311 S.W.3d 452",
            "2010 Tex. Crim. App. LEXIS 685",
            "2010 WL 715253"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terebesi v. Torreso",
          "cluster_id": 8441937,
          "cite": [
            "764 F.3d 217",
            "2014 U.S. App. LEXIS 16133",
            "2014 WL 4099309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Fayed",
          "cluster_id": 4741522,
          "cite": [
            "9 Cal. 5th 147",
            "260 Cal. Rptr. 3d 761",
            "460 P.3d 1149"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Justin Barrett Hill",
          "cluster_id": 795398,
          "cite": [
            "459 F.3d 966",
            "2006 U.S. App. LEXIS 20584",
            "2006 WL 2328721"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Frazier",
          "cluster_id": 842682,
          "cite": [
            "733 N.W.2d 713",
            "478 Mich. 231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Anstey",
          "cluster_id": 845579,
          "cite": [
            "719 N.W.2d 579",
            "476 Mich. 436"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ernest Edgar Black Jeff Wigington",
          "cluster_id": 3171438,
          "cite": [
            "811 F.3d 1259",
            "2016 U.S. App. LEXIS 1057",
            "2016 WL 278918"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roger Trent v. Steven Wade",
          "cluster_id": 2774855,
          "cite": [
            "776 F.3d 368",
            "2015 WL 394096"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Johnston",
          "cluster_id": 2276813,
          "cite": [
            "336 S.W.3d 649",
            "2011 Tex. Crim. App. LEXIS 388",
            "2011 WL 891324"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Reyes Fabian Olivera-Mendez",
          "cluster_id": 797553,
          "cite": [
            "484 F.3d 505",
            "2007 U.S. App. LEXIS 10492",
            "2007 WL 1296781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "110OAG40",
          "cluster_id": 10638768,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane3_recency"
      },
      {
        "citing_case": {
          "name": "Maryland Attorney General Opinion 110OAG40",
          "cluster_id": 10848272,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane3_recency"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145646 OR 9434934 OR 9434935 OR 9434936) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDY2MzgwODAwMDAwJnM9MzIxNDg4MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145646+OR+9434934+OR+9434935+OR+9434936%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(145646 OR 9434934 OR 9434935 OR 9434936)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTAmcz04NDQzNjM2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28145646+OR+9434934+OR+9434935+OR+9434936%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145646 OR 9434934 OR 9434935 OR 9434936)",
        "reviewed": 52,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 52,
        "triage_read": 4,
        "triage_snippet_classified": 48
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145646 OR 9434934 OR 9434935 OR 9434936)",
    "indexed_citing_opinions": 714,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145646,
        "count": 582,
        "count_source": "search"
      },
      {
        "opinion_id": 9434934,
        "count": 143,
        "count_source": "search"
      },
      {
        "opinion_id": 9434935,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434936,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1223,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hudson-v-michigan.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwNDMzMDUmcz0xMDE2MDgzNSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145646+OR+9434934+OR+9434935+OR+9434936%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145646,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 101156,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 101963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109572,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 110317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 111259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 111265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 111779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 111834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 112136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 112209,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 112350,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 112413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 112416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 112454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 117905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 118103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 118180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 118235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 118466,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 121167,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 121169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 127919,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 131146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 161659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 770457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 791612,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 793669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 1237532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 1693561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 1854815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 1934151,
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
    "date_created": "2026-07-05T07:37:58Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:38:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:38:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:43:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:38:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hudson v. Michigan

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

                         HUDSON v. MICHIGAN

     CERTIORARI TO THE COURT OF APPEALS OF MICHIGAN

  No. 04–1360. Argued January 9, 2006—Reargued May 18, 2006—

                     Decided June 15, 2006 

Detroit police executing a search warrant for narcotics and weapons
 entered petitioner Hudson’s home in violation of the Fourth Amend
 ment’s “knock-and-announce” rule. The trial court granted Hudson’s
 motion to suppress the evidence seized, but the Michigan Court of
 Appeals reversed on interlocutory appeal. Hudson was convicted of
 drug possession. Affirming, the State Court of Appeals rejected Hud
 son’s renewed Fourth Amendment claim.
Held: The judgment is affirmed.
Affirmed.
     JUSTICE SCALIA delivered the opinion of the Court with respect to
  Parts I, II, and III, concluding that violation of the “knock-and
  announce” rule does not require suppression of evidence found in a
  search. Pp. 2–13.
     (a) Because Michigan has conceded that the entry here was a
  knock-and-announce violation, the only issue is whether the exclu
  sionary rule is appropriate for such a violation. Pp. 2–3.
     (b) This Court has rejected “[i]ndiscriminate application” of the ex
  clusionary rule, United States v. Leon, 468 U. S. 897, 908, holding it
  applicable only “where its deterrence benefits outweigh its ‘substan
  tial social costs,’ ” Pennsylvania Bd. of Probation and Parole v. Scott,
  524 U. S. 357, 363. Exclusion may not be premised on the mere fact
  that a constitutional violation was a “but-for” cause of obtaining the
  evidence. The illegal entry here was not the but-for cause, but even if
  it were, but-for causation can be too attenuated to justify exclusion.
  Attenuation can occur not only when the causal connection is remote,
  but also when suppression would not serve the interest protected by
  the constitutional guarantee violated. The interests protected by the
  knock-and-announce rule include human life and limb (because an
2                        HUDSON v. MICHIGAN

                                 Syllabus

    unannounced entry may provoke violence from a surprised resident),
    property (because citizens presumably would open the door upon an
    announcement, whereas a forcible entry may destroy it), and privacy
    and dignity of the sort that can be offended by a sudden entrance.
    But the rule has never protected one’s interest in preventing the gov
    ernment from seeing or taking evidence described in a warrant.
    Since the interests violated here have nothing to do with the seizure
    of the evidence, the exclusionary rule is inapplicable. Pp. 3–7.
       (c) The social costs to be weighed against deterrence are consider
    able here. In addition to the grave adverse consequence that exclud
    ing relevant incriminating evidence always entails—the risk of re
    leasing dangerous criminals—imposing such a massive remedy would
    generate a constant flood of alleged failures to observe the rule, and
    claims that any asserted justification for a no-knock entry had inade
    quate support. Another consequence would be police officers’ refrain
    ing from timely entry after knocking and announcing, producing pre
    ventable violence against the officers in some cases, and the
    destruction of evidence in others. Next to these social costs are the
    deterrence benefits. The value of deterrence depends on the strength
    of the incentive to commit the forbidden act. That incentive is mini
    mal here, where ignoring knock-and-announce can realistically be
    expected to achieve nothing but the prevention of evidence destruc
    tion and avoidance of life-threatening resistance, dangers which sus
    pend the requirement when there is “reasonable suspicion” that they
    exist, Richards v. Wisconsin, 520 U. S. 385, 394. Massive deterrence
    is hardly necessary. Contrary to Hudson’s argument that without
    suppression there will be no deterrence, many forms of police mis
    conduct are deterred by civil-rights suits, and by the consequences of
    increasing professionalism of police forces, including a new emphasis
    on internal police discipline. Pp. 8–13.
       JUSTICE SCALIA, joined by THE CHIEF JUSTICE, JUSTICE THOMAS, and
    JUSTICE ALITO, concluded in Part IV that Segura v. United States, 468
    U. S. 796, New York v. Harris, 495 U. S. 14, and United States v.
    Ramirez, 523 U. S. 65, confirm the conclusion that suppression is
    unwarranted in this case. Pp. 13–16.

   SCALIA, J., delivered the opinion of the Court with respect to Parts I,
II, and III, in which ROBERTS, C. J., and KENNEDY, THOMAS, and ALITO,
JJ., joined, and an opinion with respect to Part IV, in which ROBERTS,
C. J., and THOMAS and ALITO, JJ., joined. KENNEDY, J., filed an opinion
concurring in part and concurring in the judgment. BREYER, J., filed a
dissenting opinion, in which STEVENS, SOUTER, and GINSBURG, JJ.,
joined.
                       Cite as: 547 U. S. ____ (2006)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 04–1360
                                  _________________


BOOKER T. HUDSON, JR., PETITIONER v. MICHIGAN
  ON WRIT OF CERTIORARI TO THE COURT OF APPEALS OF 

                     MICHIGAN

                                [June 15, 2006] 


  JUSTICE SCALIA delivered the opinion of the Court,
except as to Part IV.
  We decide whether violation of the “knock-and
announce” rule requires the suppression of all evidence
found in the search.
                             I
  Police obtained a warrant authorizing a search for drugs
and firearms at the home of petitioner Booker Hudson.
They discovered both. Large quantities of drugs were
found, including cocaine rocks in Hudson’s pocket. A
loaded gun was lodged between the cushion and armrest of
the chair in which he was sitting. Hudson was charged
under Michigan law with unlawful drug and firearm
possession.
  This case is before us only because of the method of
entry into the house. When the police arrived to execute
the warrant, they announced their presence, but waited
only a short time—perhaps “three to five seconds,” App.
15—before turning the knob of the unlocked front door
and entering Hudson’s home. Hudson moved to suppress
all the inculpatory evidence, arguing that the premature
entry violated his Fourth Amendment rights.
2                   HUDSON v. MICHIGAN

                      Opinion of the Court

  The Michigan trial court granted his motion. On inter
locutory review, the Michigan Court of Appeals reversed,
relying on Michigan Supreme Court cases holding that
suppression is inappropriate when entry is made pursuant
to warrant but without proper “ ‘knock and announce.’ ”
App. to Pet. for Cert. 4 (citing People v. Vasquez, 461 Mich.
235, 602 N. W. 2d 376 (1999) (per curiam); People v. Ste
vens, 460 Mich. 626, 597 N. W. 2d 53 (1999)). The Michi
gan Supreme Court denied leave to appeal. 465 Mich.
932, 639 N. E. 2d 255 (2001). Hudson was convicted of
drug possession. He renewed his Fourth Amendment
claim on appeal, but the Court of Appeals rejected it and
affirmed the conviction. App. to Pet. for Cert. 1–2. The
Michigan Supreme Court again declined review. 472
Mich. 862, 692 N. W. 2d 385 (2005). We granted certio
rari. 545 U. S. ___ (2005).
                              II
  The common-law principle that law enforcement officers
must announce their presence and provide residents an
opportunity to open the door is an ancient one. See Wilson
v. Arkansas, 514 U. S. 927, 931–932 (1995). Since 1917,
when Congress passed the Espionage Act, this traditional
protection has been part of federal statutory law, see 40
Stat. 229, and is currently codified at 18 U. S. C. §3109. We
applied that statute in Miller v. United States, 357 U. S. 301
(1958), and again in Sabbath v. United States, 391 U. S. 585
(1968). Finally, in Wilson, we were asked whether the rule
was also a command of the Fourth Amendment. Tracing its
origins in our English legal heritage, 514 U. S., at 931–936,
we concluded that it was.
  We recognized that the new constitutional rule we had
announced is not easily applied. Wilson and cases follow
ing it have noted the many situations in which it is not
necessary to knock and announce. It is not necessary
when “circumstances presen[t] a threat of physical vio
                  Cite as: 547 U. S. ____ (2006)             3

                      Opinion of the Court

lence,” or if there is “reason to believe that evidence would
likely be destroyed if advance notice were given,” id., at
936, or if knocking and announcing would be “futile,”
Richards v. Wisconsin, 520 U. S. 385, 394 (1997). We re
quire only that police “have a reasonable suspicion . . . under
the particular circumstances” that one of these grounds for
failing to knock and announce exists, and we have acknowl
edged that “[t]his showing is not high.” Ibid.
   When the knock-and-announce rule does apply, it is not
easy to determine precisely what officers must do. How
many seconds’ wait are too few? Our “reasonable wait time”
standard, see United States v. Banks, 540 U. S. 31, 41
(2003), is necessarily vague. Banks (a drug case, like this
one) held that the proper measure was not how long it
would take the resident to reach the door, but how long it
would take to dispose of the suspected drugs—but that such
a time (15 to 20 seconds in that case) would necessarily be
extended when, for instance, the suspected contraband was
not easily concealed. Id., at 40–41. If our ex post evaluation
is subject to such calculations, it is unsurprising that, ex
ante, police officers about to encounter someone who may
try to harm them will be uncertain how long to wait.
   Happily, these issues do not confront us here. From the
trial level onward, Michigan has conceded that the entry
was a knock-and-announce violation. The issue here is
remedy. Wilson specifically declined to decide whether the
exclusionary rule is appropriate for violation of the knock-
and-announce requirement. 514 U. S., at 937, n. 4. That
question is squarely before us now.
                            III 

                             A

   In Weeks v. United States, 232 U. S. 383 (1914), we
adopted the federal exclusionary rule for evidence that was
unlawfully seized from a home without a warrant in viola
tion of the Fourth Amendment. We began applying the
4                   HUDSON v. MICHIGAN

                      Opinion of the Court

same rule to the States, through the Fourteenth Amend
ment, in Mapp v. Ohio, 367 U. S. 643 (1961).
   Suppression of evidence, however, has always been our
last resort, not our first impulse. The exclusionary rule
generates “substantial social costs,” United States v. Leon,
468 U. S. 897, 907 (1984), which sometimes include setting
the guilty free and the dangerous at large. We have there
fore been “cautio[us] against expanding” it, Colorado v.
Connelly, 479 U. S. 157, 166 (1986), and “have repeatedly
emphasized that the rule’s ‘costly toll’ upon truth-seeking
and law enforcement objectives presents a high obstacle
for those urging [its] application,” Pennsylvania Bd. of
Probation and Parole v. Scott, 524 U. S. 357, 364–365
(1998) (citation omitted). We have rejected “[i]ndiscrimi
nate application” of the rule, Leon, supra, at 908, and have
held it to be applicable only “where its remedial objectives
are thought most efficaciously served,” United States v.
Calandra, 414 U. S. 338, 348 (1974)—that is, “where its
deterrence benefits outweigh its ‘substantial social costs,’ ”
Scott, supra, at 363 (quoting Leon, supra, at 907).
   We did not always speak so guardedly. Expansive dicta
in Mapp, for example, suggested wide scope for the exclu
sionary rule. See, e.g., 367 U. S., at 655 (“[A]ll evidence
obtained by searches and seizures in violation of the Con
stitution is, by that same authority, inadmissible in a
state court”). Whiteley v. Warden, Wyo. State Penitentiary,
401 U. S. 560, 568–569 (1971), was to the same effect. But
we have long since rejected that approach. As explained
in Arizona v. Evans, 514 U. S. 1, 13 (1995): “In Whiteley,
the Court treated identification of a Fourth Amendment
violation as synonymous with application of the exclusion
ary rule to evidence secured incident to that violation.
Subsequent case law has rejected this reflexive application
of the exclusionary rule.” (Citation omitted.) We had said
as much in Leon, a decade earlier, when we explained that
“[w]hether the exclusionary sanction is appropriately
                  Cite as: 547 U. S. ____ (2006)            5

                      Opinion of the Court

imposed in a particular case, . . . is ‘an issue separate from
the question whether the Fourth Amendment rights of the
party seeking to invoke the rule were violated by police
conduct.’ ” 468 U. S., at 906 (quoting Illinois v. Gates, 462
U. S. 213, 223 (1983)).
   In other words, exclusion may not be premised on the
mere fact that a constitutional violation was a “but-for”
cause of obtaining evidence. Our cases show that but-for
causality is only a necessary, not a sufficient, condition for
suppression. In this case, of course, the constitutional
violation of an illegal manner of entry was not a but-for
cause of obtaining the evidence. Whether that prelimi
nary misstep had occurred or not, the police would have
executed the warrant they had obtained, and would have
discovered the gun and drugs inside the house. But even
if the illegal entry here could be characterized as a but-for
cause of discovering what was inside, we have “never held
that evidence is ‘fruit of the poisonous tree’ simply because
‘it would not have come to light but for the illegal actions
of the police.’ ” Segura v. United States, 468 U. S. 796, 815
(1984). See also id., at 829 (STEVENS, J., dissenting) (“We
have not . . . mechanically applied the [exclusionary] rule to
every item of evidence that has a causal connection with
police misconduct”). Rather, but-for cause, or “causation in
the logical sense alone,” United States v. Ceccolini, 435
U. S. 268, 274 (1978), can be too attenuated to justify exclu
sion, id., at 274–275. Even in the early days of the exclu
sionary rule, we declined to
    “hold that all evidence is ‘fruit of the poisonous tree’
    simply because it would not have come to light but for
    the illegal actions of the police. Rather, the more apt
    question in such a case is ‘whether, granting estab
    lishment of the primary illegality, the evidence to
    which instant objection is made has been come at by
    exploitation of that illegality or instead by means suf
6                  HUDSON v. MICHIGAN

                     Opinion of the Court

    ficiently distinguishable to be purged of the primary
    taint.’ ” Wong Sun v. United States, 371 U. S. 471, 487–
    488 (1963) (quoting J. Maguire, Evidence of Guilt 221
    (1959) (emphasis added)).
   Attenuation can occur, of course, when the causal con
nection is remote. See, e.g., Nardone v. United States, 308
U. S. 338, 341 (1939). Attenuation also occurs when, even
given a direct causal connection, the interest protected by
the constitutional guarantee that has been violated would
not be served by suppression of the evidence obtained.
“The penalties visited upon the Government, and in turn
upon the public, because its officers have violated the law
must bear some relation to the purposes which the law is
to serve.” Ceccolini, supra, at 279. Thus, in New York v.
Harris, 495 U. S. 14 (1990), where an illegal warrantless
arrest was made in Harris’ house, we held that
    “suppressing [Harris’] statement taken outside the
    house would not serve the purpose of the rule that
    made Harris’ in-house arrest illegal. The warrant re
    quirement for an arrest in the home is imposed to pro
    tect the home, and anything incriminating the police
    gathered from arresting Harris in his home, rather
    than elsewhere, has been excluded, as it should have
    been; the purpose of the rule has thereby been vindi
    cated.” Id., at 20.
For this reason, cases excluding the fruits of unlawful
warrantless searches, see, e.g., Boyd v. United States, 116
U. S. 616 (1886); Weeks, 232 U. S. 383; Silverthorne Lumber
Co. v. United States, 251 U. S. 385 (1920); Mapp, supra, say
nothing about the appropriateness of exclusion to vindi
cate the interests protected by the knock-and-announce
requirement. Until a valid warrant has issued, citizens
are entitled to shield “their persons, houses, papers, and
effects,” U. S. Const., Amdt. 4, from the government’s
scrutiny. Exclusion of the evidence obtained by a war
                 Cite as: 547 U. S. ____ (2006)           7

                     Opinion of the Court

rantless search vindicates that entitlement. The interests
protected by the knock-and-announce requirement are
quite different—and do not include the shielding of poten
tial evidence from the government’s eyes.
   One of those interests is the protection of human life
and limb, because an unannounced entry may provoke
violence in supposed self-defense by the surprised resi
dent. See, e.g., McDonald v. United States, 335 U. S. 451,
460–461 (1948) (Jackson, J., concurring). See also Sabbath,
391 U. S., at 589; Miller, 357 U. S., at 313, n. 12. Another
interest is the protection of property. Breaking a house (as
the old cases typically put it) absent an announcement
would penalize someone who “ ‘did not know of the process,
of which, if he had notice, it is to be presumed that he
would obey it . . . .’ ” Wilson, 514 U. S., at 931–932 (quot
ing Semayne’s Case, 5 Co. Rep. 91a, 91b, 77 Eng. Rep. 194,
195–196 (K. B. 1603)). The knock-and-announce rule gives
individuals “the opportunity to comply with the law and to
avoid the destruction of property occasioned by a forcible
entry.” Richards, 520 U. S., at 393, n. 5. See also Banks,
540 U. S., at 41. And thirdly, the knock-and-announce rule
protects those elements of privacy and dignity that can be
destroyed by a sudden entrance. It gives residents the
“opportunity to prepare themselves for” the entry of the
police. Richards, 520 U. S., at 393, n. 5. “The brief inter
lude between announcement and entry with a warrant
may be the opportunity that an individual has to pull on
clothes or get out of bed.” Ibid. In other words, it assures
the opportunity to collect oneself before answering the
door.
   What the knock-and-announce rule has never protected,
however, is one’s interest in preventing the government
from seeing or taking evidence described in a warrant.
Since the interests that were violated in this case have
nothing to do with the seizure of the evidence, the exclu
sionary rule is inapplicable.
8                  HUDSON v. MICHIGAN

                     Opinion of the Court

                               B
  Quite apart from the requirement of unattenuated
causation, the exclusionary rule has never been applied
except “where its deterrence benefits outweigh its ‘sub
stantial social costs,’ ” Scott, 524 U. S., at 363 (quoting
Leon, 468 U. S., at 907). The costs here are considerable.
In addition to the grave adverse consequence that exclu
sion of relevant incriminating evidence always entails
(viz., the risk of releasing dangerous criminals into soci
ety), imposing that massive remedy for a knock-and
announce violation would generate a constant flood of
alleged failures to observe the rule, and claims that any
asserted Richards justification for a no-knock entry, see
520 U. S., at 394, had inadequate support. Cf. United
States v. Singleton, 441 F. 3d 290, 293–294 (CA4 2006).
The cost of entering this lottery would be small, but the
jackpot enormous: suppression of all evidence, amounting
in many cases to a get-out-of-jail-free card. Courts would
experience as never before the reality that “[t]he exclu
sionary rule frequently requires extensive litigation to
determine whether particular evidence must be excluded.”
Scott, supra, at 366. Unlike the warrant or Miranda
requirements, compliance with which is readily deter
mined (either there was or was not a warrant; either the
Miranda warning was given, or it was not), what consti
tuted a “reasonable wait time” in a particular case, Banks,
supra, at 41 (or, for that matter, how many seconds the
police in fact waited), or whether there was “reasonable
suspicion” of the sort that would invoke the Richards
exceptions, is difficult for the trial court to determine and
even more difficult for an appellate court to review.
  Another consequence of the incongruent remedy Hudson
proposes would be police officers’ refraining from timely
entry after knocking and announcing. As we have ob
served, see supra, at 3, the amount of time they must wait
is necessarily uncertain. If the consequences of running
                  Cite as: 547 U. S. ____ (2006)             9

                      Opinion of the Court

afoul of the rule were so massive, officers would be in
clined to wait longer than the law requires—producing
preventable violence against officers in some cases, and
the destruction of evidence in many others. See Gates, 462
U. S., at 258. We deemed these consequences severe
enough to produce our unanimous agreement that a mere
“reasonable suspicion” that knocking and announcing
“under the particular circumstances, would be dangerous
or futile, or that it would inhibit the effective investigation
of the crime,” will cause the requirement to yield. Rich
ards, supra, at 394.
   Next to these “substantial social costs” we must consider
the deterrence benefits, existence of which is a necessary
condition for exclusion. (It is not, of course, a sufficient
condition: “[I]t does not follow that the Fourth Amend
ment requires adoption of every proposal that might deter
police misconduct.” Calandra, 414 U. S., at 350; see also
Leon, supra, at 910.) To begin with, the value of deter
rence depends upon the strength of the incentive to com
mit the forbidden act. Viewed from this perspective,
deterrence of knock-and-announce violations is not worth
a lot. Violation of the warrant requirement sometimes
produces incriminating evidence that could not otherwise
be obtained. But ignoring knock-and-announce can realis
tically be expected to achieve absolutely nothing except
the prevention of destruction of evidence and the avoid
ance of life-threatening resistance by occupants of the
premises—dangers which, if there is even “reasonable
suspicion” of their existence, suspend the knock-and
announce requirement anyway. Massive deterrence is
hardly required.
   It seems to us not even true, as Hudson contends, that
without suppression there will be no deterrence of knock-
and-announce violations at all. Of course even if this
assertion were accurate, it would not necessarily justify
suppression. Assuming (as the assertion must) that civil
10                 HUDSON v. MICHIGAN

                     Opinion of the Court

suit is not an effective deterrent, one can think of many
forms of police misconduct that are similarly “undeterred.”
When, for example, a confessed suspect in the killing of a
police officer, arrested (along with incriminating evidence)
in a lawful warranted search, is subjected to physical
abuse at the station house, would it seriously be suggested
that the evidence must be excluded, since that is the only
“effective deterrent”? And what, other than civil suit, is
the “effective deterrent” of police violation of an already-
confessed suspect’s Sixth Amendment rights by denying
him prompt access to counsel? Many would regard these
violated rights as more significant than the right not to be
intruded upon in one’s nightclothes—and yet nothing but
“ineffective” civil suit is available as a deterrent. And the
police incentive for those violations is arguably greater
than the incentive for disregarding the knock-and
announce rule.
  We cannot assume that exclusion in this context is
necessary deterrence simply because we found that it was
necessary deterrence in different contexts and long ago.
That would be forcing the public today to pay for the sins
and inadequacies of a legal regime that existed almost half
a century ago. Dollree Mapp could not turn to 42 U. S. C.
§1983 for meaningful relief; Monroe v. Pape, 365 U. S. 167
(1961), which began the slow but steady expansion of that
remedy, was decided the same Term as Mapp. It would be
another 17 years before the §1983 remedy was extended to
reach the deep pocket of municipalities, Monell v. New
York City Dept. of Social Servs., 436 U. S. 658 (1978).
Citizens whose Fourth Amendment rights were violated
by federal officers could not bring suit until 10 years after
Mapp, with this Court’s decision in Bivens v. Six Unknown
Fed. Narcotics Agents, 403 U. S. 388 (1971).
  Hudson complains that “it would be very hard to find a
lawyer to take a case such as this,” Tr. of Oral Arg. 7, but
42 U. S. C. §1988(b) answers this objection. Since some
                  Cite as: 547 U. S. ____ (2006)           11

                      Opinion of the Court

civil-rights violations would yield damages too small to
justify the expense of litigation, Congress has authorized
attorney’s fees for civil-rights plaintiffs. This remedy was
unavailable in the heydays of our exclusionary-rule juris
prudence, because it is tied to the availability of a cause of
action. For years after Mapp, “very few lawyers would
even consider representation of persons who had civil
rights claims against the police,” but now “much has
changed. Citizens and lawyers are much more willing to
seek relief in the courts for police misconduct.” M. Avery,
D. Rudovsky, & K. Blum, Police Misconduct: Law and
Litigation, p. v (3d ed. 2005); see generally N. Aron, Lib
erty and Justice for All: Public Interest Law in the 1980s
and Beyond (1989) (describing the growth of public-
interest law). The number of public-interest law firms and
lawyers who specialize in civil-rights grievances has
greatly expanded.
  Hudson points out that few published decisions to date
announce huge awards for knock-and-announce violations.
But this is an unhelpful statistic. Even if we thought that
only large damages would deter police misconduct (and
that police somehow are deterred by “damages” but indif
ferent to the prospect of large §1988 attorney’s fees), we do
not know how many claims have been settled, or indeed
how many violations have occurred that produced any
thing more than nominal injury. It is clear, at least, that
the lower courts are allowing colorable knock-and
announce suits to go forward, unimpeded by assertions of
qualified immunity. See, e.g., Green v. Butler, 420 F. 3d
689, 700–701 (CA7 2005) (denying qualified immunity in a
knock-and-announce civil suit); Holland ex rel. Overdorff
v. Harrington, 268 F. 3d 1179, 1193–1196 (CA10 2001)
(same); Mena v. Simi Valley, 226 F. 3d 1031, 1041–1042
(CA9 2000) (same); Gould v. Davis, 165 F. 3d 265, 270–271
(CA4 1998) (same). As far as we know, civil liability is an
effective deterrent here, as we have assumed it is in other
12                  HUDSON v. MICHIGAN

                      Opinion of the Court

contexts. See, e.g., Correctional Services Corp. v. Malesko,
534 U. S. 61, 70 (2001) (“[T]he threat of litigation and liabil
ity will adequately deter federal officers for Bivens purposes
no matter that they may enjoy qualified immunity” (as
violators of knock-and-announce do not)); see also Nix v.
Williams, 467 U. S. 431, 446 (1984).
   Another development over the past half-century that
deters civil-rights violations is the increasing professional
ism of police forces, including a new emphasis on internal
police discipline. Even as long ago as 1980 we felt it
proper to “assume” that unlawful police behavior would
“be dealt with appropriately” by the authorities, United
States v. Payner, 447 U. S. 727, 733–734, n. 5 (1980), but
we now have increasing evidence that police forces across
the United States take the constitutional rights of citizens
seriously. There have been “wide-ranging reforms in the
education, training, and supervision of police officers.” S.
Walker, Taming the System: The Control of Discretion in
Criminal Justice 1950–1990, p. 51 (1993). Numerous
sources are now available to teach officers and their su
pervisors what is required of them under this Court’s
cases, how to respect constitutional guarantees in various
situations, and how to craft an effective regime for inter
nal discipline. See, e.g., D. Waksman & D. Goodman, The
Search and Seizure Handbook (2d ed. 2006); A. Stone & S.
DeLuca, Police Administration: An Introduction (2d ed.
1994); E. Thibault, L. Lynch, & R. McBridge, Proactive
Police Management (4th ed. 1998). Failure to teach and
enforce constitutional requirements exposes municipalities
to financial liability. See Canton v. Harris, 489 U. S. 378,
388 (1989). Moreover, modern police forces are staffed
with professionals; it is not credible to assert that internal
discipline, which can limit successful careers, will not have
a deterrent effect. There is also evidence that the increas
ing use of various forms of citizen review can enhance
police accountability.
                 Cite as: 547 U. S. ____ (2006)           13

                     Opinion of SCALIA, J.

  In sum, the social costs of applying the exclusionary rule
to knock-and-announce violations are considerable; the
incentive to such violations is minimal to begin with, and
the extant deterrences against them are substantial—
incomparably greater than the factors deterring
warrantless entries when Mapp was decided. Resort to
the massive remedy of suppressing evidence of guilt is
unjustified.
                              IV
   A trio of cases—Segura v. United States, 468 U. S. 796
(1984); New York v. Harris, 495 U. S. 14 (1990); and United
States v. Ramirez, 523 U. S. 65 (1998)—confirms our con
clusion that suppression is unwarranted in this case.
   Like today’s case, Segura involved a concededly illegal
entry. Police conducting a drug crime investigation waited
for Segura outside an apartment building; when he ar
rived, he denied living there. The police arrested him and
brought him to the apartment where they suspected illegal
activity. An officer knocked. When someone inside
opened the door, the police entered, taking Segura with
them. They had neither a warrant nor consent to enter,
and they did not announce themselves as police—an entry
as illegal as can be. Officers then stayed in the apartment
for 19 hours awaiting a search warrant. 468 U. S., at 800–
801; id., at 818–819 (STEVENS, J., dissenting). Once
alerted that the search warrant had been obtained, the
police—still inside, having secured the premises so that no
evidence could be removed—conducted a search. Id., at
801. We refused to exclude the resulting evidence. We
recognized that only the evidence gained from the particu
lar violation could be excluded, see id., at 799, 804–805,
and therefore distinguished the effects of the illegal entry
from the effects of the legal search: “None of the informa
tion on which the warrant was secured was derived from
or related in any way to the initial entry into petitioners’
14                      HUDSON v. MICHIGAN

                          Opinion of SCALIA, J.

apartment . . . .” Id., at 814. It was therefore “beyond
dispute that the information possessed by the agents
before they entered the apartment constituted an inde
pendent source for the discovery and seizure of the evi
dence now challenged.” Ibid.
  If the search in Segura could be “wholly unrelated to the
prior entry,” ibid., when the only entry was warrantless, it
would be bizarre to treat more harshly the actions in this
case, where the only entry was with a warrant. If the
probable cause backing a warrant that was issued later in
time could be an “independent source” for a search that
proceeded after the officers illegally entered and waited, a
search warrant obtained before going in must have at least
this much effect.1
  In the second case, Harris, the police violated the defen
dant’s Fourth Amendment rights by arresting him at
home without a warrant, contrary to Payton v. New York,
445 U. S. 573 (1980). Once taken to the station house, he
gave an incriminating statement. See 495 U. S., at 15–16.
We refused to exclude it. Like the illegal entry which led
——————
  1 JUSTICE  BREYER’s insistence that the warrant in Segura was “ob
tained independently without use of any information found during the
illegal entry,” post, at 14 (dissenting opinion), entirely fails to distin
guish it from the warrant in the present case. Similarly inapposite is
his appeal to Justice Frankfurter’s statement in Wolf v. Colorado, 338
U. S. 25, 28 (1949), that the “knock at the door, . . . as a prelude to a
search, without authority of law . . . [is] inconsistent with the concep
tion of human rights enshrined in [our] history,” see post, at 17. “How
much the more offensive,” JUSTICE BREYER asserts, “when the search
takes place without any knock at all,” ibid. But a no-knock entry
“without authority of law” (i.e., without a search warrant) describes not
this case, but Segura—where the evidence was admitted anyway.
   JUSTICE BREYER’s assertion that Segura, unlike our decision in the
present case, had no effect on deterrence, see post, at 23, does not
comport with the views of the Segura dissent. See, e.g., 468 U. S., at
817 (STEVENS, J., dissenting) (“The Court’s disposition, I fear, will
provide government agents with an affirmative incentive to engage in
unconstitutional violations of the privacy of the home”).
                      Cite as: 547 U. S. ____ (2006)                     15

                           Opinion of SCALIA, J.

to discovery of the evidence in today’s case, the illegal
arrest in Harris began a process that culminated in acqui
sition of the evidence sought to be excluded. While Har
ris’s statement was “the product of an arrest and being in
custody,” it “was not the fruit of the fact that the arrest
was made in the house rather than someplace else.” Id.,
at 20. Likewise here: While acquisition of the gun and
drugs was the product of a search pursuant to warrant, it
was not the fruit of the fact that the entry was not pre
ceded by knock and announce.2
   United States v. Ramirez, supra, involved a claim that
police entry violated the Fourth Amendment because it was
effected by breaking a window. We ultimately concluded
that the property destruction was, under all the circum
stances, reasonable, but in the course of our discussion we
unanimously said the following: “[D]estruction of property
in the course of a search may violate the Fourth Amend
ment, even though the entry itself is lawful and the fruits of
the search are not subject to suppression.” Id., at 71. Had
the breaking of the window been unreasonable, the Court
said, it would have been necessary to determine whether
there had been a “sufficient causal relationship between the
breaking of the window and the discovery of the guns to
warrant suppression of the evidence.” Id., at 72, n. 3. What
clearer expression could there be of the proposition that an

——————
  2 Harris undermines two key points of the dissent. First, the claim

that “whether the interests underlying the knock-and-announce rule
are implicated in any given case is, in a sense, beside the point,” post, at
18. This is flatly refuted by Harris’s plain statement that the reason
for a rule must govern the sanctions for the rule’s violation. 495 U. S.,
at 17, 20; see also supra, at 6. Second, the dissent’s attempt to turn
Harris into a vindication of the sanctity of the home, see post, at 24.
The whole point of the case was that a confession that police obtained
by illegally removing a man from the sanctity of his home was admissi
ble against him.
16                 HUDSON v. MICHIGAN

                     Opinion of SCALIA, J.

impermissible manner of entry does not necessarily trigger
the exclusionary rule?
                      *    *    *
 For the foregoing reasons we affirm the judgment of the
Michigan Court of Appeals.
                                          It is so ordered.
                  Cite as: 547 U. S. ____ (2006)            1

                     Opinion of KENNEDY, J.

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 04–1360
                          _________________


BOOKER T. HUDSON, JR., PETITIONER v. MICHIGAN
   ON WRIT OF CERTIORARI TO THE COURT OF APPEALS OF 

                      MICHIGAN

                         [June 15, 2006] 


  JUSTICE KENNEDY, concurring in part and concurring in
the judgment.
  Two points should be underscored with respect to to
day’s decision. First, the knock-and-announce require
ment protects rights and expectations linked to ancient
principles in our constitutional order. See Wilson v. Ar
kansas, 514 U. S. 927, 934 (1995). The Court’s decision
should not be interpreted as suggesting that violations of
the requirement are trivial or beyond the law’s concern.
Second, the continued operation of the exclusionary rule,
as settled and defined by our precedents, is not in doubt.
Today’s decision determines only that in the specific con
text of the knock-and-announce requirement, a violation is
not sufficiently related to the later discovery of evidence to
justify suppression.
  As to the basic right in question, privacy and security in
the home are central to the Fourth Amendment’s guaran
tees as explained in our decisions and as understood since
the beginnings of the Republic. This common understand
ing ensures respect for the law and allegiance to our insti
tutions, and it is an instrument for transmitting our Con
stitution to later generations undiminished in meaning
and force. It bears repeating that it is a serious matter if
law enforcement officers violate the sanctity of the home
by ignoring the requisites of lawful entry. Security must
not be subject to erosion by indifference or contempt.
2                  HUDSON v. MICHIGAN

                   Opinion of KENNEDY, J.

   Our system, as the Court explains, has developed proce
dures for training police officers and imposing discipline
for failures to act competently and lawfully. If those
measures prove ineffective, they can be fortified with more
detailed regulations or legislation. Supplementing these
safeguards are civil remedies, such as those available
under 42 U. S. C. §1983, that provide restitution for dis
crete harms. These remedies apply to all violations, in
cluding, of course, exceptional cases in which unan
nounced entries cause severe fright and humiliation.
   Suppression is another matter. Under our precedents
the causal link between a violation of the knock-and
announce requirement and a later search is too attenuated
to allow suppression. Cf. United States v. Ramirez, 523
U. S. 65, 72, n. 3 (1998) (application of the exclusionary
rule depends on the existence of a “sufficient causal rela
tionship” between the unlawful conduct and the discovery
of evidence). When, for example, a violation results from
want of a 20-second pause but an ensuing, lawful search
lasting five hours discloses evidence of criminality, the
failure to wait at the door cannot properly be described as
having caused the discovery of evidence.
   Today’s decision does not address any demonstrated
pattern of knock-and-announce violations. If a widespread
pattern of violations were shown, and particularly if those
violations were committed against persons who lacked the
means or voice to mount an effective protest, there would
be reason for grave concern. Even then, however, the
Court would have to acknowledge that extending the
remedy of exclusion to all the evidence seized following a
knock-and-announce violation would mean revising the
requirement of causation that limits our discretion in
applying the exclusionary rule. That type of extension
also would have significant practical implications, adding
to the list of issues requiring resolution at the criminal
trial questions such as whether police officers entered a
                 Cite as: 547 U. S. ____ (2006)           3

                    Opinion of KENNEDY, J.

home after waiting 10 seconds or 20.
  In this case the relevant evidence was discovered not
because of a failure to knock-and-announce, but because of
a subsequent search pursuant to a lawful warrant. The
Court in my view is correct to hold that suppression was
not required. While I am not convinced that Segura v.
United States, 468 U. S. 796 (1984), and New York v. Harris,
495 U. S. 14 (1990), have as much relevance here as
JUSTICE SCALIA appears to conclude, the Court’s holding is
fully supported by Parts I through III of its opinion. I ac
cordingly join those Parts and concur in the judgment.
                 Cite as: 547 U. S. ____ (2006)           1

                    BREYER, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 04–1360
                         _________________


BOOKER T. HUDSON, JR., PETITIONER v. MICHIGAN
  ON WRIT OF CERTIORARI TO THE COURT OF APPEALS OF 

                     MICHIGAN

                        [June 15, 2006] 


  JUSTICE BREYER, with whom JUSTICE STEVENS, JUSTICE
SOUTER, and JUSTICE GINSBURG join, dissenting.
   In Wilson v. Arkansas, 514 U. S. 927 (1995), a unani
mous Court held that the Fourth Amendment normally
requires law enforcement officers to knock and announce
their presence before entering a dwelling. Today’s opinion
holds that evidence seized from a home following a viola
tion of this requirement need not be suppressed
   As a result, the Court destroys the strongest legal incen
tive to comply with the Constitution’s knock-and-announce
requirement. And the Court does so without significant
support in precedent. At least I can find no such support
in the many Fourth Amendment cases the Court has
decided in the near century since it first set forth the
exclusionary principle in Weeks v. United States, 232 U. S.
383 (1914). See Appendix, infra.
   Today’s opinion is thus doubly troubling. It represents a
significant departure from the Court’s precedents. And it
weakens, perhaps destroys, much of the practical value of
the Constitution’s knock-and-announce protection.
                                I
  This Court has set forth the legal principles that ought
to have determined the outcome of this case in two sets of
basic Fourth Amendment cases. I shall begin by describ
2                  HUDSON v. MICHIGAN

                     BREYER, J., dissenting

ing that underlying case law.
                               A
   The first set of cases describes the constitutional knock-
and-announce requirement, a requirement that this Court
initially set forth only 11 years ago in Wilson v. Arkansas,
supra. Cf. Sabbath v. United States, 391 U. S. 585 (1968)
(suppressing evidence seized in violation of federal statu
tory knock-and-announce requirement); Miller v. United
States, 357 U. S. 301 (1958) (same). In Wilson, tracing the
lineage of the knock-and-announce rule back to the 13th
century, 514 U. S., at 932, we wrote that
    “[a]n examination of the common law of search and
    seizure leaves no doubt that the reasonableness of a
    search of a dwelling may depend in part on whether
    law enforcement officers announced their presence
    and authority prior to entering.” Id., at 931.
   We noted that this “basic principle” was agreed upon by
“[s]everal prominent founding-era commentators,” id., at
932, and “was woven quickly into the fabric of early
American law” via state constitutions and statutes, id., at
933. 	We further concluded that there was
    “little doubt that the Framers of the Fourth Amend
    ment thought that the method of an officer’s entry
    into a dwelling was among the factors to be considered
    in assessing the reasonableness of a search or sei
    zure.” Id., at 934.
  And we held that the “common-law ‘knock and an
nounce’ principle forms a part of the reasonableness in
quiry under the Fourth Amendment.” Id., at 929. Thus,
“a search or seizure of a dwelling might be constitutionally
defective if police officers enter without prior announce
ment.” Id., at 936; see United States v. Banks, 540 U. S.
31, 36 (2003); United States v. Ramirez, 523 U. S. 65, 70
(1998); Richards v. Wisconsin, 520 U. S. 385, 387 (1997).
                 Cite as: 547 U. S. ____ (2006)           3

                    BREYER, J., dissenting

                             B
  The second set of cases sets forth certain well-
established principles that are relevant here. They in
clude:
  Boyd v. United States, 116 U. S. 616 (1886). In this semi
nal Fourth Amendment case, decided 120 years ago, the
Court wrote, in frequently quoted language, that the
Fourth Amendment’s prohibitions apply
    “to all invasions on the part of the government and its
    employés of the sanctity of a man’s home and the pri
    vacies of life. It is not the breaking of his doors, and
    the rummaging of his drawers, that constitutes the
    essence of the offence; but it is the invasion of his in
    defeasible right of personal security, personal liberty
    and private property.” Id., at 630.
   Weeks, supra. This case, decided 28 years after Boyd,
originated the exclusionary rule. The Court held that the
Federal Government could not retain evidence seized
unconstitutionally and use that evidence in a federal
criminal trial. The Court pointed out that “[i]f letters and
private documents” could be unlawfully seized from a
home “and used in evidence against a citizen accused of an
offense, the protection of the Fourth Amendment declaring
his right to be secure against such searches and seizures is
of no value, and . . . might as well be stricken from the
Constitution.” 232 U. S., at 393.
   Silverthorne Lumber Co. v. United States, 251 U. S. 385
(1920). This case created an exception to (or a qualifica
tion of) Weeks’ exclusionary rule. The Court held that the
Government could not use information obtained during an
illegal search to subpoena documents that they illegally
viewed during that search. Writing for the Court, Justice
Holmes noted that the exclusionary rule “does not mean
that the facts [unlawfully] obtained become sacred and
inaccessible. If knowledge of them is gained from an
4                    HUDSON v. MICHIGAN

                      BREYER, J., dissenting

independent source they may be proved like any
others . . . .” 251 U. S., at 392. Silverthorne thus stands
for the proposition that the exclusionary rule does not
apply if the evidence in question (or the “fruits” of that
evidence) was obtained through a process unconnected
with, and untainted by, the illegal search. Cf. Nix v. Wil
liams, 467 U. S. 431, 444 (1984) (describing related “inevi
table discovery” exception).
   Wolf v. Colorado, 338 U. S. 25 (1949), and Mapp v. Ohio,
367 U. S. 643 (1961). Both of these cases considered
whether Weeks’ exclusionary rule applies to the States. In
Wolf, the Court held that it did not. It said that “[t]he
security of one’s privacy against arbitrary intrusion by the
police . . . is . . . implicit in ‘the concept of ordered liberty’
and as such enforceable against the States through the
Due Process Clause.” 338 U. S., at 27–28. But the Court
held that the exclusionary rule is not enforceable against
the States as “an essential ingredient of the right.” Id., at
29. In Mapp, the Court overruled Wolf. Experience, it
said, showed that alternative methods of enforcing the
Fourth Amendment’s requirements had failed. See 367
U. S., at 651–653; see, e.g., People v. Cahan, 44 Cal. 2d
434, 447, 282 P. 2d 905, 913 (1955) (Traynor, C. J.) (“Ex
perience [in California] has demonstrated, however, that
neither administrative, criminal nor civil remedies are
effective in suppressing lawless searches and seizures”).
The Court consequently held that “all evidence obtained
by searches and seizures in violation of the Constitution
is, by that same authority, inadmissible in a state court.”
Mapp, 367 U. S., at 655. “To hold otherwise,” the Court
added, would be “to grant the right but in reality to with
hold its privilege and enjoyment.” Id., at 656.
                              II
  Reading our knock-and-announce cases, Part I–A, su
pra, in light of this foundational Fourth Amendment case
                 Cite as: 547 U. S. ____ (2006)            5

                     BREYER, J., dissenting

law, Part I–B, supra, it is clear that the exclusionary rule
should apply. For one thing, elementary logic leads to
that conclusion. We have held that a court must “con-
side[r]” whether officers complied with the knock-and
announce requirement “in assessing the reasonableness of
a search or seizure.” Wilson, 514 U. S., at 934 (emphasis
added); see Banks, 540 U. S., at 36. The Fourth Amend
ment insists that an unreasonable search or seizure is,
constitutionally speaking, an illegal search or seizure.
And ever since Weeks (in respect to federal prosecutions)
and Mapp (in respect to state prosecutions), “the use of
evidence secured through an illegal search and seizure” is
“barred” in criminal trials. Wolf, supra, at 28 (citing
Weeks); see Mapp, supra, at 655.
  For another thing, the driving legal purpose underlying
the exclusionary rule, namely, the deterrence of unlawful
government behavior, argues strongly for suppression.
See Elkins v. United States, 364 U. S. 206, 217 (1960) (pur
pose of the exclusionary rule is “to deter—to compel re
spect for the constitutional guaranty . . . by removing the
incentive to disregard it”). In Weeks, Silverthorne, and
Mapp, the Court based its holdings requiring suppression
of unlawfully obtained evidence upon the recognition that
admission of that evidence would seriously undermine the
Fourth Amendment’s promise. All three cases recognized
that failure to apply the exclusionary rule would make
that promise a hollow one, see Mapp, supra, at 657, reduc
ing it to “a form of words,” Silverthorne, supra, at 392, “of
no value” to those whom it seeks to protect, Weeks, supra,
at 393. Indeed, this Court in Mapp held that the exclu
sionary rule applies to the States in large part due to its
belief that alternative state mechanisms for enforcing the
Fourth Amendment’s guarantees had proved “worthless
and futile.” 367 U. S., at 652.
  Why is application of the exclusionary rule any the less
necessary here? Without such a rule, as in Mapp, police
6                   HUDSON v. MICHIGAN

                     BREYER, J., dissenting

know that they can ignore the Constitution’s requirements
without risking suppression of evidence discovered after
an unreasonable entry. As in Mapp, some government
officers will find it easier, or believe it less risky, to pro
ceed with what they consider a necessary search immedi
ately and without the requisite constitutional (say, war
rant or knock-and-announce) compliance. Cf. Mericli, The
Apprehension of Peril Exception to the Knock and An
nounce Rule—Part I, 16 Search and Seizure L. Rep. 129,
130 (1989) (hereinafter Mericili) (noting that some “[d]rug
enforcement authorities believe that safety for the police
lies in a swift, surprising entry with overwhelming force—
not in announcing their official authority”).
   Of course, the State or the Federal Government may
provide alternative remedies for knock-and-announce
violations. But that circumstance was true of Mapp as
well. What reason is there to believe that those remedies
(such as private damages actions under 42 U. S. C. §1983),
which the Court found inadequate in Mapp, can ade
quately deter unconstitutional police behavior here? See
Kamisar, In Defense of the Search and Seizure Exclusion
ary Rule, 26 Harv. J. L. & Pub. Pol’y 119, 126–129 (2003)
(arguing that “five decades of post-Weeks ‘freedom’ from
the inhibiting effect of the federal exclusionary rule failed
to produce any meaningful alternative to the exclusionary
rule in any jurisdiction” and that there is no evidence that
“times have changed” post-Mapp).
   The cases reporting knock-and-announce violations are
legion. See, e.g., 34 Geo. L. J. Ann. Rev. Crim. Proc. 31–35
(2005) (collecting court of appeals cases); Annot., 85
A. L. R. 5th 1 (2001) (collecting state-court cases); Brief for
Petitioner 16–17 (collecting federal and state cases).
Indeed, these cases of reported violations seem sufficiently
frequent and serious as to indicate “a widespread pattern.”
Ante, at 2 (KENNEDY, J., concurring in part and concurring
in judgment). Yet the majority, like Michigan and the
                  Cite as: 547 U. S. ____ (2006)            7

                     BREYER, J., dissenting

United States, has failed to cite a single reported case in
which a plaintiff has collected more than nominal dam
ages solely as a result of a knock-and-announce violation.
Even Michigan concedes that, “in cases like the present
one . . . , damages may be virtually non-existent.” Brief for
Respondent 35, n. 66; And Michigan’s amici further con
cede that civil immunities prevent tort law from being an
effective substitute for the exclusionary rule at this time.
Brief for Criminal Justice Legal Foundation 10; see also
Hope v. Pelzer, 536 U. S. 730, 739 (2002) (difficulties of
overcoming qualified immunity defenses).
  As Justice Stewart, the author of a number of signifi
cant Fourth Amendment opinions, explained, the deter
rent effect of damage actions “can hardly be said to be
great,” as such actions are “expensive, time-consuming,
not readily available, and rarely successful.” Stewart, The
Road to Mapp v. Ohio and Beyond: The Origins, Develop
ment and Future of the Exclusionary Rule in Search-and-
Seizure Cases, 83 Colum. L. Rev. 1365, 1388 (1983). The
upshot is that the need for deterrence—the critical factor
driving this Court’s Fourth Amendment cases for close to a
century—argues with at least comparable strength for
evidentiary exclusion here.
  To argue, as the majority does, that new remedies, such
as 42 U. S. C. §1983 actions or better trained police, make
suppression unnecessary is to argue that Wolf, not Mapp,
is now the law. (The Court recently rejected a similar
argument in Dickerson v. United States, 530 U. S. 428, 441–
442 (2000).) To argue that there may be few civil suits
because violations may produce nothing “more than nomi
nal injury” is to confirm, not to deny, the inability of civil
suits to deter violations. See ante, at 11. And to argue
without evidence (and despite myriad reported cases of
violations, no reported case of civil damages, and Michi
gan’s concession of their nonexistence) that civil suits may
provide deterrence because claims may “have been settled”
8                   HUDSON v. MICHIGAN

                     BREYER, J., dissenting

is, perhaps, to search in desperation for an argument. See
ibid. Rather, the majority, as it candidly admits, has
simply “assumed” that, “[a]s far as [it] know[s], civil liabil
ity is an effective deterrent,” ibid., a support-free assump
tion that Mapp and subsequent cases make clear does not
embody the Court’s normal approach to difficult questions
of Fourth Amendment law.
   It is not surprising, then, that after looking at virtually
every pertinent Supreme Court case decided since Weeks, I
can find no precedent that might offer the majority sup
port for its contrary conclusion. The Court has, of course,
recognized that not every Fourth Amendment violation
necessarily triggers the exclusionary rule. Ante, at 4–5; cf.
Illinois v. Gates, 462 U. S. 213, 223 (1983) (application of
the exclusionary rule is a separate question from whether
the Fourth Amendment has been violated). But the class
of Fourth Amendment violations that do not result in
suppression of the evidence seized, however, is limited.
   The Court has declined to apply the exclusionary rule
only:
     (1) where there is a specific reason to believe that ap
    plication of the rule would “not result in appreciable
    deterrence,” United States v. Janis, 428 U. S. 433, 454
    (1976); see, e.g., United States v. Leon, 468 U. S. 897,
    919–920 (1984) (exception where searching officer exe
    cutes defective search warrant in “good faith”); Ari
    zona v. Evans, 514 U. S. 1, 14 (1995) (exception for
    clerical errors by court employees); Walder v. United
    States, 347 U. S. 62 (1954) (exception for impeach
    ment purposes), or
    (2) where admissibility in proceedings other than
    criminal trials was at issue, see, e.g., Pennsylvania
    Bd. of Probation and Parole v. Scott, 524 U. S. 357,
    364 (1998) (exception for parole revocation proceed
    ings); INS v. Lopez-Mendoza, 468 U. S. 1032, 1050
                  Cite as: 547 U. S. ____ (2006)             9

                     BREYER, J., dissenting

    (1984) (plurality opinion) (exception for deportation
    proceedings); Janis, supra, at 458 (exception for civil
    tax proceedings); United States v. Calandra, 414 U. S.
    338, 348–350 (1974) (exception for grand jury proceed
    ings); Stone v. Powell, 428 U. S. 465, 493–494 (1976)
    (exception for federal habeas proceedings).
   Neither of these two exceptions applies here. The sec
ond does not apply because this case is an ordinary crimi
nal trial. The first does not apply because (1) officers who
violate the rule are not acting “as a reasonable officer
would and should act in similar circumstances,” Leon,
supra, at 920, (2) this case does not involve government
employees other than police, Evans, supra, and (3), most
importantly, the key rationale for any exception, “lack of
deterrence,” is missing, see Pennsylvania Bd. of Probation,
supra, at 364 (noting that the rationale for not applying
the rule in noncriminal cases has been that the deterrence
achieved by having the rule apply in those contexts is
“minimal” because “application of the rule in the criminal
trial context already provides significant deterrence of
unconstitutional searches”); Michigan v. Tucker, 417 U. S.
433, 447 (1974) (noting that deterrence rationale would not
be served if rule applied to police officers acting in good
faith, as the “deterrent purpose of the exclusionary rule
necessarily assumes that the police have engaged in willful,
or at the very least negligent, conduct”). That critical latter
rationale, which underlies every exception, does not apply
here, as there is no reason to think that, in the case of
knock-and-announce violations by the police, “the exclu
sion of evidence at trial would not sufficiently deter future
errors,” Evans, supra, at 14, or “ ‘further the ends of the
exclusionary rule in any appreciable way,’ ” Leon, supra, at
919–920.
   I am aware of no other basis for an exception. The
Court has decided more than 300 Fourth Amendment
10                 HUDSON v. MICHIGAN

                     BREYER, J., dissenting

cases since Weeks. The Court has found constitutional
violations in nearly a third of them. See W. Greenhalgh,
The Fourth Amendment Handbook: A Chronological Sur
vey of Supreme Court Decisions 27–130 (2d ed. 2003)
(collecting and summarizing 332 post-Weeks cases decided
between 1914 and 2002). The nature of the constitutional
violation varies. In most instances officers lacked a war
rant; in others, officers possessed a warrant based on false
affidavits; in still others, the officers executed the search
in an unconstitutional manner. But in every case involv
ing evidence seized during an illegal search of a home
(federally since Weeks, nationally since Mapp), the Court,
with the exceptions mentioned, has either explicitly or
implicitly upheld (or required) the suppression of the
evidence at trial. See Appendix, infra. In not one of those
cases did the Court “questio[n], in the absence of a more
efficacious sanction, the continued application of the [ex
clusionary] rule to suppress evidence from the State’s
case” in a criminal trial. Franks v. Delaware, 438 U. S.
154, 171 (1978).
   I can find nothing persuasive in the majority’s opinion
that could justify its refusal to apply the rule. It certain-
ly is not a justification for an exception here (as the major
ity finds) to find odd instances in other areas of law that
do not automatically demand suppression. Ante, at 10
(suspect confesses, police beat him up afterwards; sus-
pect confesses, then police apparently arrest him, take
him to station, and refuse to tell him of his right to coun
sel). Nor can it justify an exception to say that some
police may knock at the door anyway (to avoid being
mistaken for a burglar), for other police (believing
quick entry is the most secure, effective entry) will not
voluntarily do so. Cf. Mericli 130 (describing Special
Weapons and Tactics (SWAT) team practices); R.
Balko, No SWAT (Apr. 6, 2006), available at
http://www.cato.org/pub_display.php?pub_id=6344 (all In
                  Cite as: 547 U. S. ____ (2006)           11

                     BREYER, J., dissenting

ternet materials as visited June 7, 2006, and available in
Clerk of Court’s case file).
   Neither can the majority justify its failure to respect the
need for deterrence, as set forth consistently in the Court’s
prior case law, through its claim of “substantial social
costs”—at least if it means that those “social costs” are
somehow special here. The only costs it mentions are
those that typically accompany any use of the Fourth
Amendment’s exclusionary principle: (1) that where the
constable blunders, a guilty defendant may be set free
(consider Mapp itself); (2) that defendants may assert
claims where Fourth Amendment rights are uncertain
(consider the Court’s qualified immunity jurisprudence),
and (3) that sometimes it is difficult to decide the merits of
those uncertain claims. See ante, at 8–9. In fact, the “no
knock” warrants that are provided by many States, by
diminishing uncertainty, may make application of the
knock-and-announce principle less “cost[ly]” on the whole
than application of comparable Fourth Amendment prin
ciples, such as determining whether a particular war
rantless search was justified by exigency. The majority’s
“substantial social costs” argument is an argument
against the Fourth Amendment’s exclusionary principle
itself. And it is an argument that this Court, until now,
has consistently rejected.
                            III
  The majority, Michigan, and the United States make
several additional arguments. In my view, those argu
ments rest upon misunderstandings of the principles
underlying this Court’s precedents.
                             A
   The majority first argues that “the constitutional viola
tion of an illegal manner of entry was not a but-for cause
of obtaining the evidence.” Ante, at 5. But taking causa
12                 HUDSON v. MICHIGAN

                     BREYER, J., dissenting

tion as it is commonly understood in the law, I do not see
how that can be so. See W. Keeton, D. Dobbs, R. Keeton,
& D. Owen, Prosser and Keeton on Law of Torts 266 (5th
ed. 1984). Although the police might have entered Hud
son’s home lawfully, they did not in fact do so. Their
unlawful behavior inseparably characterizes their actual
entry; that entry was a necessary condition of their pres
ence in Hudson’s home; and their presence in Hudson’s
home was a necessary condition of their finding and seiz
ing the evidence. At the same time, their discovery of
evidence in Hudson’s home was a readily foreseeable
consequence of their entry and their unlawful presence
within the home. Cf. 2 Restatement (Second) of Torts
§435 (1963–1964).
   Moreover, separating the “manner of entry” from the
related search slices the violation too finely. As noted,
Part I–A, supra, we have described a failure to comply
with the knock-and-announce rule, not as an independ
ently unlawful event, but as a factor that renders the
search “constitutionally defective.” Wilson, 514 U. S., at
936; see also id., at 934 (compliance with the knock-and
announce requirement is one of the “factors to be consid
ered in assessing the reasonableness of a search or seizure”
(emphasis added)); Ker v. California, 374 U. S. 23, 53 (1963)
(opinion of Brennan, J.) (“[A] lawful entry is the indispensa
ble predicate of a reasonable search”).
   The Court nonetheless accepts Michigan’s argument
that the requisite but-for-causation is not satisfied in this
case because, whether or not the constitutional violation
occurred (what the Court refers to as a “preliminary mis
step”), “the police would have executed the warrant they
had obtained, and would have discovered the gun and
drugs inside the house.” Ante, at 5. As support for this
proposition, Michigan rests on this Court’s inevitable
discovery cases.
   This claim, however, misunderstands the inevitable
                 Cite as: 547 U. S. ____ (2006)          13

                    BREYER, J., dissenting

discovery doctrine. Justice Holmes in Silverthorne, in
discussing an “independent source” exception, set forth the
principles underlying the inevitable discovery rule. See
supra, at 4. That rule does not refer to discovery that
would have taken place if the police behavior in question
had (contrary to fact) been lawful. The doctrine does not
treat as critical what hypothetically could have happened
had the police acted lawfully in the first place. Rather,
“independent” or “inevitable” discovery refers to discovery
that did occur or that would have occurred (1) despite (not
simply in the absence of) the unlawful behavior and (2)
independently of that unlawful behavior. The government
cannot, for example, avoid suppression of evidence seized
without a warrant (or pursuant to a defective warrant)
simply by showing that it could have obtained a valid
warrant had it sought one. See, e.g., Coolidge v. New
Hampshire, 403 U. S. 443, 450–451 (1971). Instead, it
must show that the same evidence “inevitably would have
been discovered by lawful means.” Nix v. Williams, 467
U. S., at 444 (emphasis added). “What a man could do is
not at all the same as what he would do.” Austin, Ifs And
Cans, 42 Proceedings of the British Academy 109, 111–112
(1956).
  The inevitable discovery exception rests upon the prin
ciple that the remedial purposes of the exclusionary rule
are not served by suppressing evidence discovered through
a “later, lawful seizure” that is “genuinely independent of
an earlier, tainted one.” Murray v. United States, 487
U. S. 533, 542 (1988) (emphasis added); see also id., at 545
(Marshall, J., joined by STEVENS and O’Connor, JJ., dis
senting) (“When the seizure of the evidence at issue is
‘wholly independent of’ the constitutional violation, then
exclusion arguably will have no effect on a law enforce
ment officer’s incentive to commit an unlawful search”).
  Case law well illustrates the meaning of this principle.
In Nix, supra, police officers violated a defendant’s Sixth
14                 HUDSON v. MICHIGAN

                    BREYER, J., dissenting

Amendment right by eliciting incriminating statements
from him after he invoked his right to counsel. Those
statements led to the discovery of the victim’s body. The
Court concluded that evidence obtained from the victim’s
body was admissible because it would ultimately or inevi
tably have been discovered by a volunteer search party
effort that was ongoing—whether or not the Sixth Amend
ment violation had taken place. Id., at 449. In other
words, the evidence would have been found despite, and
independent of, the Sixth Amendment violation.
   In Segura v. United States, 468 U. S. 796 (1984), one of
the “trio of cases” JUSTICE SCALIA says “confirms [the
Court’s] conclusion,” ante, at 13, the Court held that an
earlier illegal entry into an apartment did not require
suppression of evidence that police later seized when
executing a search warrant obtained on the basis of infor
mation unconnected to the initial entry. The Court rea
soned that the “evidence was discovered the day following
the entry, during the search conducted under a valid
warrant”—i.e., a warrant obtained independently without
use of any information found during the illegal entry—and
that “it was the product of that search, wholly unrelated to
the prior [unlawful] entry.” Segura, supra, at 814 (em
phasis added).
   In Murray, supra, the Court upheld the admissibility of
seized evidence where agents entered a warehouse with
out a warrant, and then later returned with a valid war
rant that was not obtained on the basis of evidence ob
served during the first (illegal) entry. The Court reasoned
that while the agents’ “[k]nowledge that the marijuana
was in the warehouse was assuredly acquired at the time
of the unlawful entry . . . it was also acquired at the time
of entry pursuant to the warrant, and if that later acquisi
tion was not the result of the earlier entry there is no rea
son why the independent source doctrine should not ap
ply.” Id., at 541 (emphasis added).
                 Cite as: 547 U. S. ____ (2006)          15

                    BREYER, J., dissenting

   Thus, the Court’s opinion reflects a misunderstanding of
what “inevitable discovery” means when it says, “[i]n this
case, of course, the constitutional violation of an illegal
manner of entry was not a but-for cause of obtaining the
evidence.” Ante, at 5. The majority rests this conclusion
on its next statement: “Whether that preliminary misstep
has occurred or not, the police . . . would have discovered
the gun and the drugs inside the house.” Ibid. Despite
the phrase “of course,” neither of these statements is
correct. It is not true that, had the illegal entry not oc
curred, “police would have discovered the guns and drugs
inside the house.” Without that unlawful entry they
would not have been inside the house; so there would have
been no discovery. See supra, at 12.
   Of course, had the police entered the house lawfully,
they would have found the gun and drugs. But that fact is
beside the point. The question is not what police might
have done had they not behaved unlawfully. The question
is what they did do. Was there set in motion an independ
ent chain of events that would have inevitably led to the
discovery and seizure of the evidence despite, and inde
pendent of, that behavior? The answer here is “no.”
                             B
   The majority, Michigan, and the United States point out
that the officers here possessed a warrant authorizing a
search. Ante, at 5. That fact, they argue, means that the
evidence would have been discovered independently or
somehow diminishes the need to suppress the evidence.
But I do not see why that is so. The warrant in question
was not a “no-knock” warrant, which many States (but not
Michigan) issue to assure police that a prior knock is not
necessary. Richards, 520 U. S., at 396, n. 7 (collecting
state statutes). It did not authorize a search that fails to
comply with knock-and-announce requirements. Rather,
it was an ordinary search warrant. It authorized a search
16                HUDSON v. MICHIGAN

                    BREYER, J., dissenting

that complied with, not a search that disregarded, the
Constitution’s knock-and-announce rule.
  Would a warrant that authorizes entry into a home on
Tuesday permit the police to enter on Monday? Would a
warrant that authorizes entry during the day authorize
the police to enter during the middle of the night? It is
difficult for me to see how the presence of a warrant that
does not authorize the entry in question has anything to
do with the “inevitable discovery” exception or otherwise
diminishes the need to enforce the knock-and-announce
requirement through suppression.
                             C
   The majority and the United States set forth a policy-
related variant of the causal connection theme: The
United States argues that the law should suppress evi
dence only insofar as a Fourth Amendment violation
causes the kind of harm that the particular Fourth
Amendment rule seeks to protect against. It adds that the
constitutional purpose of the knock-and-announce rule is
to prevent needless destruction of property (such as break
ing down a door) and to avoid unpleasant surprise. And it
concludes that the exclusionary rule should suppress
evidence of, say, damage to property, the discovery of a
defendant in an “intimate or compromising moment,” or
an excited utterance from the occupant caught by surprise,
but nothing more. Brief for United States as Amicus
Curiae 12, 28.
   The majority makes a similar argument. It says that
evidence should not be suppressed once the causal connec
tion between unlawful behavior and discovery of the evi
dence becomes too “attenuated.” Ante, at 5. But the ma
jority then makes clear that it is not using the word
“attenuated” to mean what this Court’s precedents have
typically used that word to mean, namely, that the discov
ery of the evidence has come about long after the unlawful
                 Cite as: 547 U. S. ____ (2006)          17

                    BREYER, J., dissenting

behavior took place or in an independent way, i.e., through
“ ‘means sufficiently distinguishable to be purged of the
primary taint.’ ” Wong Sun v. United States, 371 U. S. 471,
487–488 (1963); see Brown v. Illinois, 422 U. S. 590, 603–
604 (1975).
   Rather, the majority gives the word “attenuation” a new
meaning (thereby, in effect, making the same argument as
the United States). “Attenuation,” it says, “also occurs
when, even given a direct causal connection, the interest
protected by the constitutional guarantee that has been
violated would not be served by suppression of the evi
dence obtained.” Ante, at 6. The interests the knock-and
announce rule seeks to protect, the Court adds, are “hu
man life” (at stake when a householder is “surprised”),
“property” (such as the front door), and “those elements of
privacy and dignity that can be destroyed by a sudden
entrance,” namely, “the opportunity to collect oneself
before answering the door.” Ante, at 7. Since none of
those interests led to the discovery of the evidence seized
here, there is no reason to suppress it.
   There are three serious problems with this argument.
First, it does not fully describe the constitutional values,
purposes, and objectives underlying the knock-and
announce requirement. That rule does help to protect
homeowners from damaged doors; it does help to protect
occupants from surprise. But it does more than that. It
protects the occupants’ privacy by assuring them that
government agents will not enter their home without
complying with those requirements (among others) that
diminish the offensive nature of any such intrusion. Many
years ago, Justice Frankfurter wrote for the Court that
the “knock at the door, . . . as a prelude to a search, with
out authority of law . . . [is] inconsistent with the concep
tion of human rights enshrined in [our] history” and Con
stitution. Wolf, 338 U. S., at 28. How much the more
offensive when the search takes place without any knock
18                  HUDSON v. MICHIGAN

                     BREYER, J., dissenting

at all. Cf. Wilson, 514 U. S., at 931 (knock-and-announce
rule recognizes that “the common law generally protected
a man’s house as ‘his castle of defence and asylum’ ” (quot
ing 3 W. Blackstone, Commentaries *288)); Miller, 357
U. S., at 313 (federal knock-and-announce statute “codi
f[ied] a tradition embedded in Anglo-American law” that
reflected “the reverence of the law for the individual’s
right of privacy in his house”).
   Over a century ago this Court wrote that “it is not the
breaking of his doors” that is the “essence of the offence,”
but the “invasions on the part of the government . . . of the
sanctity of a man’s home and the privacies of life.” Boyd,
116 U. S., at 630. And just this Term we have reiterated
that “it is beyond dispute that the home is entitled to
special protection as the center of the private lives of our
people.” Georgia v. Randolph, 547 U. S. ___, ___ (2006)
(slip op., at 10) (quoting Minnesota v. Carter, 525 U. S. 83,
99 (1998) (KENNEDY, J., concurring)). The knock-and
announce requirement is no less a part of the “centuries
old principle” of special protection for the privacy of the
home than the warrant requirement. See 547 U. S., at ___
(slip op., at 10) (citing Miller, supra, at 307). The Court is
therefore wrong to reduce the essence of its protection to
“the right not to be intruded upon in one’s nightclothes.”
Ante, at 10; see Richards, 520 U. S., at 393, n. 5
(“[I]ndividual privacy interest[s]” protected by the rule
are “not inconsequential” and “should not be unduly
minimized”).
   Second, whether the interests underlying the knock-
and-announce rule are implicated in any given case is, in a
sense, beside the point. As we have explained, failure to
comply with the knock-and-announce rule renders the
related search unlawful. Wilson, supra, at 936. And
where a search is unlawful, the law insists upon suppres
sion of the evidence consequently discovered, even if that
evidence or its possession has little or nothing to do with
                 Cite as: 547 U. S. ____ (2006)           19

                     BREYER, J., dissenting

the reasons underlying the unconstitutionality of a search.
The Fourth Amendment does not seek to protect contra
band, yet we have required suppression of contraband
seized in an unlawful search. See, e.g., Kyllo v. United
States, 533 U. S. 27, 40 (2001); Coolidge, 403 U. S., at 473.
That is because the exclusionary rule protects more gen
eral “privacy values through deterrence of future police
misconduct.” James v. Illinois, 493 U. S. 307, 319 (1990).
The same is true here.
   Third, the majority’s interest-based approach departs
from prior law. Ordinarily a court will simply look to see
if the unconstitutional search produced the evidence. The
majority does not refer to any relevant case in which,
beyond that, suppression turned on the far more detailed
relation between, say, (1) a particular materially false
statement made to the magistrate who issued a (conse
quently) invalid warrant and (2) evidence found after a
search with that warrant. But cf. ante, at 15, n. 2 (plural
ity opinion) (citing New York v. Harris, 495 U. S. 14
(1990), as such a case in section of opinion that JUSTICE
KENNEDY does not join). And the majority’s failure does
not surprise me, for such efforts to trace causal connec
tions at retail could well complicate Fourth Amendment
suppression law, threatening its workability.
                             D
  The United States, in its brief and at oral argument, has
argued that suppression is “an especially harsh remedy
given the nature of the violation in this case.” Brief for
United States as Amicus Curiae 28; see also id., at 24.
This argument focuses upon the fact that entering a house
after knocking and announcing can, in some cases, prove
dangerous to a police officer. Perhaps someone inside has
a gun, as turned out to be the case here. The majority
adds that police officers about to encounter someone who
may try to harm them will be “uncertain” as to how long to
20                 HUDSON v. MICHIGAN

                     BREYER, J., dissenting

wait. Ante, at 9. It says that, “[i]f the consequences of
running afoul” of the knock-and-announce “rule were so
massive,” i.e., would lead to the exclusion of evidence, then
“officers would be inclined to wait longer than the law
requires—producing preventable violence against officers
in some cases.” Ante, at 8–9.
  To argue that police efforts to assure compliance with
the rule may prove dangerous, however, is not to argue
against evidence suppression. It is to argue against the
validity of the rule itself. Similarly, to argue that en
forcement means uncertainty, which in turn means the
potential for dangerous and longer-than-necessary delay,
is (if true) to argue against meaningful compliance with
the rule.
  The answer to the first argument is that the rule itself
does not require police to knock or to announce their pres
ence where police have a “reasonable suspicion” that doing
so “would be dangerous or futile” or “would inhibit the
effective investigation of the crime by, for example, allow
ing the destruction of evidence.” Richards, supra, at 394;
see Banks, 540 U. S., at 36–37; Wilson, supra, at 935–936.
  The answer to the second argument is that States can,
and many do, reduce police uncertainty while assuring a
neutral evaluation of concerns about risks to officers or the
destruction of evidence by permitting police to obtain a
“no-knock” search warrant from a magistrate judge,
thereby assuring police that a prior announcement is not
necessary. Richards, 520 U. S., at 396, n. 7 (collecting
state statutes). While such a procedure cannot remove all
uncertainty, it does provide an easy way for officers to
comply with the knock-and-announce rule.
  Of course, even without such a warrant, police maintain
the backup “authority to exercise independent judgment
concerning the wisdom of a no-knock entry at the time the
warrant is being executed.” Ibid. “[I]f circumstances
support a reasonable suspicion of exigency when the offi
                 Cite as: 547 U. S. ____ (2006)          21

                    BREYER, J., dissenting

cers arrive at the door, they may go straight in.” Banks,
supra, at 37. And “[r]easonable suspicion is a less de
manding standard than probable cause . . . .” Alabama v.
White, 496 U. S. 325, 330 (1990); see Terry v. Ohio, 392
U. S. 1, 21–22 (1968) (no Fourth Amendment violation
under the reasonable suspicion standard if “the facts
available to the officer at the moment of the seizure or the
search ‘warrant a man of reasonable caution in the belief’
that the action taken was appropriate”).
  Consider this very case. The police obtained a search
warrant that authorized a search, not only for drugs, but
also for guns. App. 5. If probable cause justified a search
for guns, why would it not also have justified a no-knock
warrant, thereby diminishing any danger to the officers?
Why (in a State such as Michigan that lacks no-knock
warrants) would it not have justified the very no-knock
entry at issue here? Indeed, why did the prosecutor not
argue in this very case that, given the likelihood of guns,
the no-knock entry was lawful? From what I have seen in
the record, he would have won. And had he won, there
would have been no suppression here.
  That is the right way to win. The very process of argu
ing the merits of the violation would help to clarify the
contours of the knock-and-announce rule, contours that
the majority believes are too fuzzy. That procedural fact,
along with no-knock warrants, back up authority to enter
without knocking regardless, and use of the “reasonable
suspicion” standard for doing so should resolve the gov
ernment’s problems with the knock-and-announce rule
while reducing the “uncertain[ty]” that the majority dis
cusses to levels beneath that found elsewhere in Fourth
Amendment law (e.g., exigent circumstances). Ante, at 8.
Regardless, if the Court fears that effective enforcement of
a constitutional requirement will have harmful conse
quences, it should face those fears directly by addressing
the requirement itself. It should not argue, “the require
22                 HUDSON v. MICHIGAN

                    BREYER, J., dissenting

ment is fine, indeed, a serious matter, just don’t enforce
it.”
                              E
   It should be apparent by now that the three cases upon
which JUSTICE SCALIA relies—Segura v. United States,
468 U. S. 796; New York v. Harris, 495 U. S. 14; and Ra
mirez, 523 U. S. 65—do not support his conclusion. See
ante, at 13–15. Indeed, JUSTICE KENNEDY declines to join
this section of the lead opinion because he fails to see the
relevance of Segura and Harris, though he does rely on
Ramirez. Ante, at 3 (opinion concurring in part and con
curring in judgment).
   JUSTICE SCALIA first argues that, if the “search in
Segura could be ‘wholly unrelated to the prior entry, . . .
when the only entry was warrantless, it would be bizarre
to treat more harshly the actions in this case, where the
only entry was with a warrant.” Ante, at 14. Then it says
that, “[i]f the probable cause backing a warrant that was
issued later in time could be an ‘independent source’ for a
search that proceeded after the officers illegally entered
and waited, a search warrant obtained before going in
must have at least this much effect.” Ibid. I do not under
stand these arguments. As I have explained, the presence
of a warrant that did not authorize a search that fails to
comply with knock-and-announce requirements is beside
the point. See Part III–B, supra. And the timing of the
warrant in Segura made no difference to the case. The
relevant fact about the warrant there was that it was
lawfully obtained and arguably set off an independent
chain of events that led the police to seize the evidence.
468 U. S., at 814; see also id., at 814–815 (“The valid
warrant search was a ‘means sufficiently distinguishable’
to purge the evidence of any ‘taint’ arising from the entry”
(citations omitted)). As noted, there is no such independ
ent event, or intervening chain of events that would purge
                 Cite as: 547 U. S. ____ (2006)          23

                    BREYER, J., dissenting

the taint of the illegal entry, present here. See supra, at
15. The search that produced the relevant evidence here
is the very search that the knock-and-announce violation
rendered unlawful. There simply is no “independent
source.”
   As importantly, the Court in Segura said nothing to
suggest it intended to create a major exclusionary rule
exception, notwithstanding the impact of such an excep
tion on deterrence. Indeed, such an exception would be
inconsistent with a critical rationale underlying the inde
pendent source and inevitable discovery rules, which was
arguably available in Segura, and which is clearly absent
here. That rationale concerns deterrence. The threat of
inadmissibility deters unlawful police behavior; and the
existence of an exception applicable where evidence is
found through an untainted independent route will rarely
undercut that deterrence. That is because the police can
rarely rely upon such an exception—at least not often
enough to change the deterrence calculus. See Murray,
487 U. S., at 540 (“We see the incentives differently. An
officer with probable cause sufficient to obtain a search
warrant would be foolish to enter the premises in an
unlawful manner. By doing so, he would risk suppression
of all evidence on the premises . . . ”); Nix, 467 U. S., at
445 (“A police officer who is faced with the opportunity to
obtain evidence illegally will rarely, if ever, be in a posi
tion to calculate whether the evidence sought would inevi
tably be discovered”); id., at 444 (“If the prosecution can
establish by a preponderance of the evidence that the
information ultimately or inevitably would have been
discovered by lawful means—here the volunteers’ search—
then the deterrence rationale has so little basis that the
evidence should be received”).
   Segura’s police officers would have been foolish to have
entered the apartment unlawfully with the ex ante hope
that an independent causal chain of events would later
24                 HUDSON v. MICHIGAN

                    BREYER, J., dissenting

occur and render admissible the evidence they found. By
way of contrast, today’s holding will seriously undermine
deterrence in knock-and-announce cases. Officers will
almost always know ex ante that they can ignore the
knock-and-announce requirement without risking the
suppression of evidence discovered after their unlawful
entry. That fact is obvious, and this Court has never
before today—not in Segura or any other post-Weeks (or
post-Mapp) case—refused to apply the exclusionary rule
where its absence would so clearly and so significantly
impair government officials’ incentive to comply with
comparable Fourth Amendment requirements.
  Neither does New York v. Harris, supra, support the
Court’s result. See ante, at 6, 14; but see ante, at 3 (opin
ion of KENNEDY, J.) (declining to join section relying on
Harris). In Harris, police officers arrested the defendant
at his home without a warrant, in violation of Payton v.
New York, 445 U. S. 573 (1980). Harris made several
incriminating statements: a confession in his home, a
written inculpatory statement at the stationhouse, and a
videotaped interview conducted by the district attorney at
the stationhouse. 495 U. S., at 16. The trial court sup
pressed the statements given by Harris in the house and
on the videotape, and the State did not challenge either of
those rulings. Ibid. The sole question in the case was
whether the written statement given later at the station-
house should also have been suppressed. The Court held
that this later, outside-the-home statement “was admissi
ble because Harris was in legal custody . . . and because
the statement, while the product of an arrest and being in
custody, was not the fruit of the fact that the arrest was
made in the house rather than someplace else.” Id., at 20.
Immediately after the Court stated its holding, it ex
plained:
     “To put the matter another way, suppressing the
                  Cite as: 547 U. S. ____ (2006)           25

                     BREYER, J., dissenting

    statement taken outside the house would not serve
    the purpose of the rule that made Harris’ in-house ar
    rest illegal. The warrant requirement for an arrest in
    the home is imposed to protect the home, and anything
    incriminating the police gathered from arresting Har
    ris in his home, rather than elsewhere, has been ex
    cluded, as it should have been; the purpose of the rule
    has thereby been vindicated.” Ibid. (emphasis added).
   How can JUSTICE SCALIA maintain that the evidence
here—a gun and drugs seized in the home—is “ ‘not the
fruit’ ” of the illegal entry? Ante, at 14. The officers’ fail
ure to knock and announce rendered the entire search
unlawful, Wilson, 514 U. S., at 936, and that unlawful
search led to the discovery of evidence in petitioner’s
home. Thus, Harris compels the opposite result than that
reached by the Court today. Like the Payton rule at issue
in Harris, the knock-and-announce rule reflects the “rev
erence of the law for the individual’s right of privacy in his
house.” Miller, 357 U. S., at 313; cf. Harris, 495 U. S., at
17 (“Payton itself emphasized that our holding in that case
stemmed from the ‘overriding respect for the sanctity of
the home that has been embedded in our traditions since
the origins of the Republic’ ”). Like the confession that was
“excluded, as it should have been,” in Harris, id., at 20, the
evidence in this case was seized in the home, immediately
following the illegal entry. And like Harris, nothing in
petitioner’s argument would require the suppression of
evidence obtained outside the home following a knock-and
announce violation should be suppressed, precisely be
cause officers have a remaining incentive to follow the rule
to avoid the suppression of any evidence obtained from the
very place they are searching. Cf. ibid. (“Even though we
decline to suppress statements made outside the home
following a Payton violation, the principle incentive to
obey Payton still obtains: the police know that a war
26                  HUDSON v. MICHIGAN

                      BREYER, J., dissenting

rantless entry will lead to the suppression of any evidence
found, or statements taken, inside the home”).
  I concede that United States v. Ramirez, 523 U. S. 65,
offers the majority its last best hope. Ante, at 14–15. But
not even that case can offer the majority significant sup
port. The majority focuses on the Court’s isolated state
ment that “destruction of property in the course of a
search may violate the Fourth Amendment, even though
the entry itself is lawful and the fruits of the search are not
subject to suppression.” Ramirez, supra, at 71 (emphasis
added). But even if I accept this dictum, the entry here is
unlawful, not lawful. Wilson, 514 U. S., at 931, 934. It is
one thing to say (in an appropriate case) that destruction
of property after proper entry has nothing to do with
discovery of the evidence, and to refuse to suppress. It
would be quite another thing to say that improper entry
had nothing to do with discovery of the evidence in this
case. Moreover, the deterrence analysis for the property
destruction cases (where, by definition, there will almost
always be quantifiable damages) might well differ.
                             IV
   There is perhaps one additional argument implicit in
the majority’s approach. The majority says, for example,
that the “cost” to a defendant of “entering this lottery,” i.e.,
of claiming a “knock-and-announce” violation, “would be
small, but the jackpot enormous”—namely, a potential
“get-out-of-jail-free card.” Ante, at 8. It adds that the
“social costs” of applying the exclusionary rule here are
not worth the deterrence benefits. Ante, at 13. Leaving
aside what I believe are invalid arguments based on
precedent or the majority’s own estimate that suppression
is not necessary to deter constitutional violations, one is
left with a simple unvarnished conclusion, namely, that in
this kind of case, a knock-and-announce case, “[r]esort to
the massive remedy of suppressing evidence of guilt is
                 Cite as: 547 U. S. ____ (2006)           27

                     BREYER, J., dissenting

unjustified.” Ibid. Why is that judicial judgment, taken
on its own, inappropriate? Could it not be argued that the
knock-and-announce rule, a subsidiary Fourth Amend
ment rule, is simply not important enough to warrant a
suppression remedy? Could the majority not simply claim
that the suppression game is not worth the candle?
  The answer, I believe, is “no.” That “no” reflects history,
a history that shows the knock-and-announce rule is
important. See Wilson, supra, at 931–936. That “no”
reflects precedent, precedent that shows there is no pre
existing legal category of exceptions to the exclusionary
rule into which the knock-and-announce cases might fit.
See supra, at 8–9. That “no” reflects empirical fact, ex
perience that provides confirmation of what common sense
suggests: without suppression there is little to deter
knock-and-announce violations. See supra, at 6–7.
  There may be instances in the law where text or history
or tradition leaves room for a judicial decision that rests
upon little more than an unvarnished judicial instinct.
But this is not one of them. Rather, our Fourth Amend
ment traditions place high value upon protecting privacy
in the home. They emphasize the need to assure that its
constitutional protections are effective, lest the Amend
ment ‘sound the word of promise to the ear but break it to
the hope.’ They include an exclusionary principle, which
since Weeks has formed the centerpiece of the criminal
law’s effort to ensure the practical reality of those prom
ises. That is why the Court should assure itself that any
departure from that principle is firmly grounded in logic,
in history, in precedent, and in empirical fact. It has not
done so. That is why, with respect, I dissent.
28                  HUDSON v. MICHIGAN

                Appendix to opinion of BREYER, J.

        APPENDIX TO OPINION OF BREYER, J.
  Fourth Amendment decisions from 1914 to present
requiring suppression of evidence seized (or remanding for
lower court to make suppression determination) in a pri
vate home following an illegal arrest or search:
      1. 	 eeks v. United States, 232 U. S. 383 (1914) (war
          W
          rantless search)
      2. 	 mos v. United States, 255 U. S. 313 (1921) (war
          A
          rantless arrest and search)
      3. 	 gnello v. United States, 269 U. S. 20 (1925) (war
          A
          rantless search)
      4. 	 yars v. United States, 273 U. S. 28 (1927) (inva
          B
          lid warrant)
      5. 	 nited States v. Berkeness, 275 U. S. 149 (1927)
          U
          (invalid warrant; insufficient affidavit)
      6. 	 aylor v. United States, 286 U. S. 1 (1932) (war
          T
          rantless search)
      7. 	 rau v. United States, 287 U. S. 124 (1932) (inva
          G
          lid warrant; insufficient affidavit)
      8. 	 athanson v. United States, 290 U. S. 41 (1933)
          N
          (invalid warrant; insufficient affidavit)
      9. 	 cDonald v. United States, 335 U. S. 451 (1948)
          M
          (warrantless arrest and search)
     10. 	Kremen v. United States, 353 U. S. 346 (1957) (per
          curiam) (warrantless search)
     11. 	Elkins v. United States, 364 U. S. 206 (1960)
          (search beyond scope of warrant)
     12. 	Silverman v. United States, 365 U. S. 505 (1961)
          (warrantless use of electronic device)
     13. 	Chapman v. United States, 365 U. S. 610 (1961)
          (warrantless search)
     14. 	Mapp v. Ohio, 367 U. S. 643 (1961) (warrantless
          search)
     15. 	Wong Sun v. United States, 371 U. S. 471 (1963)
          (warrantless search and arrest)
             Cite as: 547 U. S. ____ (2006)          29

           Appendix to opinion of BREYER, J.

16. 	Fahy v. Connecticut, 375 U. S. 85 (1963) (war
     rantless search)
17. 	Aguilar v. Texas, 378 U. S. 108 (1964) (invalid
     warrant; insufficient affidavit)
18. 	Stanford v. Texas, 379 U. S. 476 (1965) (invalid
     warrant; particularity defect)
19. 	James v. Louisiana, 382 U. S. 36 (1965) (per cu
     riam) (warrantless search)
20. 	Riggan v. Virginia, 384 U. S. 152 (1966) (per cu
     riam) (invalid warrant; insufficient affidavit)
21. 	Bumper v. North Carolina, 391 U. S. 543 (1968)
     (lack of valid consent to search)
22. 	Recznik v. City of Lorain, 393 U. S. 166 (1968)
     (per curiam) (warrantless search)
23. 	Chimel v. California, 395 U. S. 752 (1969) (invalid
     search incident to arrest)
24. 	Von Cleef v. New Jersey, 395 U. S. 814 (1969) (per
     curiam) (invalid search incident to arrest)
25. 	Shipley v. California, 395 U. S. 818 (1969) (per
     curiam) (invalid search incident to arrest)
26. 	Vale v. Louisiana, 399 U. S. 30 (1970) (invalid
     search incident to arrest)
27. 	Connally v. Georgia, 429 U. S. 245 (1977) (per cu
     riam) (invalid warrant; magistrate judge not neu
     tral)
28. 	Michigan v. Tyler, 436 U. S. 499 (1978) (war
     rantless search)
29. 	Mincey v. Arizona, 437 U. S. 385 (1978) (war
     rantless search)
30. 	Franks v. Delaware, 438 U. S. 154 (1978) (invalid
     warrant; obtained through perjury)
31. 	Payton v. New York, 445 U. S. 573 (1980) (war
     rantless arrest)
32. 	Steagald v. United States, 451 U. S. 204 (1981)
     (warrantless search)
33. 	Michigan v. Clifford, 464 U. S. 287 (1984) (war
30                  HUDSON v. MICHIGAN

                Appendix to opinion of BREYER, J.

          rantless search)
     34. 	Welsh v. Wisconsin, 466 U. S. 740 (1984) (war
          rantless entry into home without exigent circum
          stances)
     35. 	Thompson v. Louisiana, 469 U. S. 17 (1984) (per
          curiam) (warrantless search)
     36. 	Arizona v. Hicks, 480 U. S. 321 (1987) (unreason
          able search)
     37. 	Minnesota v. Olson, 495 U. S. 91 (1990) (war
          rantless entry into home)
     38. 	Flippo v. West Virginia, 528 U. S. 11 (1999) (per
          curiam) (warrantless search)
     39. 	Kyllo v. United States, 533 U. S. 27 (2001) (war
          rantless use of heat-imaging technology)
     40. 	Kirk v. Louisiana, 536 U. S. 635 (2002) (per cu
          riam) (warrantless arrest and search)
     41. 	Kaupp v. Texas, 538 U. S. 626 (2003) (per curiam)
          (warrantless search)

```

---

## GROUP: _overhaul2/lake/cases/Hudson v. Palmer.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Hudson v. Palmer"
type: case
citation: "468 U.S. 517 (1984)"
parallel_cite: "104 S. Ct. 3194; 82 L. Ed. 2d 393; 52 U.S.L.W. 5052"
neutral_cite: 1984 U.S. LEXIS 143
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-07-03
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-07-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hudson v. Palmer
  varies_by_point: false
  scope_note: "Good law; a prisoner has no Fourth Amendment reasonable expectation of privacy in his cell. (The companion holding on intentional property deprivations and adequate post-deprivation remedies — the Parratt-Hudson doctrine — is a Fourteenth Amendment due-process matter outside this Fourth Amendment home.)"
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111252/hudson-v-palmer/"
  cluster_id: 111252
  opinion_id: 9429735
  identity_checked: true
homes:
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Key — REP boundary"
related: ["[[Katz v. United States]]", "[[Maryland v. King]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "prisoner", "reasonable-expectation-of-privacy", "prison-cell"]
holding: "A prisoner has no reasonable expectation of privacy in his prison cell; the Fourth Amendment's proscription against unreasonable searches does not apply within the cell."
lake:
  record_id: Hudson v. Palmer
  status: verified
  projected_at: 2026-07-06
---

# Hudson v. Palmer

*468 U.S. 517 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A prison officer conducted a "shakedown" search of inmate Palmer's cell and locker and, Palmer alleged, destroyed some of his noncontraband personal property. Palmer sued under § 1983, claiming the search violated his Fourth Amendment privacy rights and the property destruction violated due process.

## Issue
Whether a prisoner has a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in his prison cell entitling him to Fourth Amendment protection against searches of the cell.

## Rule
No. "[W]e hold that society is not prepared to recognize as legitimate any subjective expectation of privacy that a prisoner might have in his prison cell and that, accordingly, the Fourth Amendment proscription against unreasonable searches does not apply within the confines of the prison cell. The recognition of privacy rights for prisoners in their individual cells simply cannot be reconciled with the concept of incarceration and the needs and objectives of penal institutions." — 468 U.S. at 526. ^pin-526

## Application
The officer's shakedown of Palmer's cell could not be a Fourth Amendment violation because Palmer had no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the cell at all. The close and continual surveillance necessary to maintain institutional security and internal order is fundamentally incompatible with any such expectation; a prisoner's cell is not a constitutionally protected private space. (Palmer's distinct claim that the officer destroyed his property was analyzed under the Due Process Clause, not the Fourth Amendment.)

## Conclusion
A prison cell is outside the Fourth Amendment's protection against unreasonable searches; the shakedown stated no Fourth Amendment claim. *Hudson* marks the outer boundary of the reasonable-expectation-of-privacy inquiry in the custodial setting.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Defines a boundary of the [[Katz v. United States]] reasonable-expectation-of-privacy test; the diminished privacy of those in custody also informs arrestee-search cases such as [[Maryland v. King]].

## Appears on
- [[Reasonable Expectation of Privacy]] — *Key — REP boundary*

## Sources
- *Hudson v. Palmer*, 468 U.S. 517 (1984) — https://www.courtlistener.com/opinion/111252/hudson-v-palmer/ — pinpoint: 526.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "09b6951890d25156", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Hudson v. Palmer"}, "payload": {"all": [{"cite": "468 U.S. 517", "page": "517", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "468"}, {"cite": "104 S. Ct. 3194", "page": "3194", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "82 L. Ed. 2d 393", "page": "393", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "82"}, {"cite": "1984 U.S. LEXIS 143", "page": "143", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}, {"cite": "52 U.S.L.W. 5052", "page": "5052", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "52"}], "display": "468 U.S. 517", "official": {"cite": "468 U.S. 517", "page": "517", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "468"}, "official_selection_present": true, "record_id": "Hudson v. Palmer"}}
{"assertion_id": "5d336012368db30e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-526", "record_id": "Hudson v. Palmer"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-526", "pinpoint_status": "slip-only", "quote": "search of inmate Palmer's cell and locker and, Palmer alleged, destroyed some of his noncontraband personal property. Palmer sued under § 1983, claiming the search violated his Fourth Amendment privacy rights and the property destruction violated due process. ## Issue Whether a prisoner has a reasonable expectation of privacy in his prison cell entitling him to Fourth Amendment protection against searches of the cell. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Hudson v. Palmer", "star_marker": null}}
{"assertion_id": "04b9b316da378422", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Hudson v. Palmer"}, "payload": {"as_of_content": "1984-07-03", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Hudson v. Palmer", "scope_note": "Good law; a prisoner has no Fourth Amendment reasonable expectation of privacy in his cell. (The companion holding on intentional property deprivations and adequate post-deprivation remedies — the Parratt-Hudson doctrine — is a Fourteenth Amendment due-process matter outside this Fourth Amendment home.)", "varies_by_point": false}}
```

### lake record — Hudson v. Palmer

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hudson v. Palmer",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hudson v. Palmer",
    "case_name_short": "Hudson",
    "case_name_full": "Hudson v. Palmer",
    "input_case_name": "Hudson v. Palmer",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-07-03",
    "year": 1984,
    "docket": null,
    "cluster_id": 111252,
    "lead_opinion_id": 9429735,
    "sibling_ids": [
      111252,
      9429735,
      9429736,
      9429737
    ],
    "absolute_url": "/opinion/111252/hudson-v-palmer/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "468 U.S. 517",
      "volume": "468",
      "reporter": "U.S.",
      "page": "517",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 3194",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3194",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 393",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "393",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 5052",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "5052",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 143",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "143",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "468 U.S. 517",
        "volume": "468",
        "reporter": "U.S.",
        "page": "517",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 3194",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3194",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 393",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "393",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 143",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "143",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 5052",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "5052",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "468 U.S. 517",
    "official_selection": {
      "court_class": "scotus",
      "selected": "468 U.S. 517",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-526",
      "page": null,
      "quote": "search of inmate Palmer's cell and locker and, Palmer alleged, destroyed some of his noncontraband personal property. Palmer sued under \u00a7 1983, claiming the search violated his Fourth Amendment privacy rights and the property destruction violated due process. ## Issue Whether a prisoner has a reasonable expectation of privacy in his prison cell entitling him to Fourth Amendment protection against searches of the cell. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-07-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hudson v. Palmer",
    "varies_by_point": false,
    "scope_note": "Good law; a prisoner has no Fourth Amendment reasonable expectation of privacy in his cell. (The companion holding on intentional property deprivations and adequate post-deprivation remedies \u2014 the Parratt-Hudson doctrine \u2014 is a Fourteenth Amendment due-process matter outside this Fourth Amendment home.)",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4603999,
          "cite": [
            "119 N.E.3d 669",
            "481 Mass. 710"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "in the Interest of L.N.C & K.N.M., Children",
          "cluster_id": 4586474,
          "cite": [
            "573 S.W.3d 309"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Louisiana v. Keith C. Kisack",
          "cluster_id": 4435443,
          "cite": [
            "236 So. 3d 1201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Adrian King, Jr. v. Jim Rubenstein",
          "cluster_id": 3210222,
          "cite": [
            "825 F.3d 206",
            "2016 U.S. App. LEXIS 10276",
            "2016 WL 3165598"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Farmer v. Brennan",
          "cluster_id": 1087956,
          "cite": [
            "128 L. Ed. 2d 811",
            "114 S. Ct. 1970",
            "511 U.S. 825",
            "1994 U.S. LEXIS 4274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. McMillian",
          "cluster_id": 112693,
          "cite": [
            "117 L. Ed. 2d 156",
            "112 S. Ct. 995",
            "503 U.S. 1",
            "1992 U.S. LEXIS 1372"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Daniels v. Williams",
          "cluster_id": 111555,
          "cite": [
            "88 L. Ed. 2d 662",
            "106 S. Ct. 662",
            "474 U.S. 327",
            "1986 U.S. LEXIS 43",
            "54 U.S.L.W. 4090"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
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
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whitley v. Albers",
          "cluster_id": 111610,
          "cite": [
            "89 L. Ed. 2d 251",
            "106 S. Ct. 1078",
            "475 U.S. 312",
            "1986 U.S. LEXIS 28",
            "54 U.S.L.W. 4236"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zinermon v. Burch",
          "cluster_id": 2620710,
          "cite": [
            "108 L. Ed. 2d 100",
            "110 S. Ct. 975",
            "494 U.S. 113",
            "1990 U.S. LEXIS 1171"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. City of Harker Heights",
          "cluster_id": 112699,
          "cite": [
            "117 L. Ed. 2d 261",
            "112 S. Ct. 1061",
            "503 U.S. 115",
            "1992 U.S. LEXIS 1376"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williamson County Regional Planning Commission v. Hamilton Bank of Johnson City",
          "cluster_id": 111501,
          "cite": [
            "87 L. Ed. 2d 126",
            "105 S. Ct. 3108",
            "473 U.S. 172",
            "1985 U.S. LEXIS 87",
            "53 U.S.L.W. 4969"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
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
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alden v. Maine",
          "cluster_id": 118318,
          "cite": [
            "144 L. Ed. 2d 636",
            "119 S. Ct. 2240",
            "527 U.S. 706",
            "1999 U.S. LEXIS 4374"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davidson v. Cannon",
          "cluster_id": 111556,
          "cite": [
            "88 L. Ed. 2d 677",
            "106 S. Ct. 668",
            "474 U.S. 344",
            "1986 U.S. LEXIS 44",
            "54 U.S.L.W. 4095"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Washington v. Harper",
          "cluster_id": 112381,
          "cite": [
            "108 L. Ed. 2d 178",
            "110 S. Ct. 1028",
            "494 U.S. 210",
            "1990 U.S. LEXIS 1174"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania Department of Corrections v. Yeskey",
          "cluster_id": 118228,
          "cite": [
            "141 L. Ed. 2d 215",
            "118 S. Ct. 1952",
            "524 U.S. 206",
            "1998 U.S. LEXIS 3888"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan Department of State Police v. Sitz",
          "cluster_id": 112459,
          "cite": [
            "110 L. Ed. 2d 412",
            "110 S. Ct. 2481",
            "496 U.S. 444",
            "1990 U.S. LEXIS 3144",
            "58 U.S.L.W. 4781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Villarreal v. State",
          "cluster_id": 2365320,
          "cite": [
            "935 S.W.2d 134",
            "1996 Tex. Crim. App. LEXIS 237",
            "1996 WL 668593"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clarence Erwin Copeland v. Mark MacHulis James Stephens",
          "cluster_id": 697696,
          "cite": [
            "57 F.3d 476",
            "1995 U.S. App. LEXIS 14483",
            "1995 WL 351078"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
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
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cleavinger v. Saxner",
          "cluster_id": 111547,
          "cite": [
            "88 L. Ed. 2d 507",
            "106 S. Ct. 496",
            "474 U.S. 193",
            "1985 U.S. LEXIS 148",
            "54 U.S.L.W. 4048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gee v. Pacheco",
          "cluster_id": 178001,
          "cite": [
            "627 F.3d 1178",
            "2010 WL 4909644"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Overton v. Bazzetta",
          "cluster_id": 130150,
          "cite": [
            "156 L. Ed. 2d 162",
            "123 S. Ct. 2162",
            "539 U.S. 126",
            "2003 U.S. LEXIS 4781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Edward Hoefling, Jr. v. City of Miami",
          "cluster_id": 3171918,
          "cite": [
            "811 F.3d 1271",
            "93 Fed. R. Serv. 3d 1022",
            "2016 U.S. App. LEXIS 1177",
            "2016 WL 285358"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Samson v. California",
          "cluster_id": 145640,
          "cite": [
            "165 L. Ed. 2d 250",
            "126 S. Ct. 2193",
            "547 U.S. 843",
            "2006 U.S. LEXIS 4885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "L.R. Bretz v. Zollie Kelman, Jack R. Lande, Eugene R. Welborn",
          "cluster_id": 458756,
          "cite": [
            "773 F.2d 1026",
            "1985 U.S. App. LEXIS 23482"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111252 OR 9429735 OR 9429736 OR 9429737) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDQ1Mjk5MjAwMDAwJnM9MzEzMjc0MSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111252+OR+9429735+OR+9429736+OR+9429737%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111252 OR 9429735 OR 9429736 OR 9429737)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MDEmcz02NjE3MzQmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111252+OR+9429735+OR+9429736+OR+9429737%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111252 OR 9429735 OR 9429736 OR 9429737)",
        "reviewed": 37,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 37,
        "triage_read": 0,
        "triage_snippet_classified": 37
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111252 OR 9429735 OR 9429736 OR 9429737)",
    "indexed_citing_opinions": 2514,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111252,
        "count": 2245,
        "count_source": "search"
      },
      {
        "opinion_id": 9429735,
        "count": 301,
        "count_source": "search"
      },
      {
        "opinion_id": 9429736,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429737,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 8082,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hudson-v-palmer.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MTQ1MzQmcz0xMDAyNDc3NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111252+OR+9429735+OR+9429736+OR+9429737%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111252,
        "cited_id": 99464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 103017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 103870,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 104557,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 106425,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 106629,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 106889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 107122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 107630,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 107840,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108414,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108431,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108484,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109008,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109080,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109402,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109921,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109969,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110085,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110362,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110518,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110593,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110657,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110753,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110770,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110829,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 111121,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 111167,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 111195,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 111224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 111227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 306226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 310105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 311474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 312857,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 321294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 327723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 328221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 328865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 340703,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 343130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 355329,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 356030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 392146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 393729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 395225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 400069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 403393,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 403670,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 407932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 410403,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 413271,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 413393,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 414190,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 416902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 421697,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 431085,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 1302147,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 1304356,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 1384033,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 1443669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 1460980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 1686657,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 1870743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 1905445,
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
    "date_created": "2026-07-05T07:43:25Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:43:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:43:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:47:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:43:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hudson v. Palmer

```
<opinion type="majority">
<author id="A0R">Chief Justice Burger</author>
<p id="AGO">delivered the opinion of the Court.</p>
<p id="ApP">We granted certiorari in No. 82-1630 to decide whether a prison inmate has a reasonable expectation of privacy in his prison cell entitling him to the protection of the Fourth Amendment against unreasonable searches and seizures. We also granted certiorari in No. 82-6695, the cross-petition, to determine whether our decision in <em>Parratt </em>v. <em>Taylor, </em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">451 U. S. 527</a></span> (1981), which held that a negligent deprivation of property by state officials does not violate the Fourteenth Amendment if an adequate postdeprivation state remedy exists, should extend to intentional deprivations of property.</p>
<p id="Ach">I</p>
<p id="A0V">The facts underlying this dispute are relatively simple. Respondent Palmer is an inmate at the Bland Correctional Center in Bland, Va., serving sentences for forgery, uttering, grand larceny, and bank robbery convictions. On September 16, 1981, petitioner Hudson, an officer at the Correctional Center, with a fellow officer, conducted a “shakedown” search of respondent’s prison locker and cell for contraband. During the “shakedown,” the officers discovered a ripped pillowcase in a trash can near respondent’s cell bunk. Charges <page-number citation-index="1" label="520">*520</page-number>against Palmer were instituted under the prison disciplinary-procedures for destroying state property. After a hearing, Palmer was found guilty on the charge and was ordered to reimburse the State for the cost of the material destroyed; in addition, a reprimand was entered on his prison record.</p>
<p id="b562-5">Palmer subsequently brought this <em>pro se </em>action in United States District Court under <span class="citation no-link">42 U. S. C. § 1983</span>. Respondent claimed that Hudson had conducted the shakedown search of his cell and had brought a false charge against him solely to harass him, and that, in violation of his Fourteenth Amendment right not to be deprived of property without due process of law, Hudson had intentionally destroyed certain of his noncontraband personal property during the September 16 search. Hudson denied each allegation; he moved for and was granted summary judgment. The District Court accepted respondent’s allegations as true but held nonetheless, relying on <em>Parratt </em>v. <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Taylor, supra,</a></span> </em>that the alleged destruction of respondent’s property, even if intentional, did not violate the Fourteenth Amendment because there were state tort remedies available to redress the deprivation, App. 31<footnotemark>1</footnotemark> and that the alleged harassment did not "rise to the level of a constitutional deprivation,” <em>id., </em>at 32.</p>
<p id="b562-6">The Court of Appeals affirmed in part, reversed in part, and remanded for further proceedings. <span class="citation" data-id="413271"><a href="/opinion/413271/russell-thomas-palmer-jr-v-ted-s-hudson-officer/" aria-description="Citation for case: Russell Thomas Palmer, Jr. v. Ted S. Hudson, Officer">697 F. 2d 1220</a></span> (CA4 1983). The court affirmed the District Court’s holding that respondent was not deprived of his property without due process. The court acknowledged that we considered only a claim of negligent property deprivation in <em>Parratt </em>v. <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Taylor, supra.</a></span> </em>It agreed with the District Court, however, that the logic of <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span> </em>applies equally to unauthorized intentional deprivations of property by state officials: “[O]nce it is as<page-number citation-index="1" label="521">*521</page-number>sumed that a postdeprivation remedy can cure an unintentional but negligent act causing injury, inflicted by a state agent which is unamenable to prior review, then that principle applies as well to random and unauthorized intentional acts.” <span class="citation" data-id="413271"><a href="/opinion/413271/russell-thomas-palmer-jr-v-ted-s-hudson-officer/#1223" aria-description="Citation for case: Russell Thomas Palmer, Jr. v. Ted S. Hudson, Officer">697 F. 2d, at 1223</a></span>.<footnotemark>2</footnotemark> The Court of Appeals did not discuss the availability and adequacy of existing state-law remedies; it presumably accepted as correct the District Court’s statement of the remedies available under Virginia law.<footnotemark>3</footnotemark></p>
<p id="b563-5">The Court of Appeals reversed the summary judgment on respondent’s claim that the shakedown search was unreasonable. The court recognized that <em>Bell </em>v. <em>Wolfish, </em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#555" aria-description="Citation for case: Bell v. Wolfish">441 U. S. 520, 555-557</a></span> (1979), authorized irregular unannounced shakedown searches of prison cells. But the court held that an individual prisoner has a “limited privacy right” in his cell entitling him to protection against searches conducted solely to harass or to humiliate. <span class="citation" data-id="413271"><a href="/opinion/413271/russell-thomas-palmer-jr-v-ted-s-hudson-officer/#1225" aria-description="Citation for case: Russell Thomas Palmer, Jr. v. Ted S. Hudson, Officer">697 F. 2d, at 1225</a></span>.<footnotemark>4</footnotemark> The shakedown of a single prisoner’s property, said the court, is permissible <page-number citation-index="1" label="522">*522</page-number>only if “done pursuant to an established program of conducting random searches of single cells or groups of cells reasonably designed to deter or discover the possession of contraband” or upon reasonable belief that the particular prisoner possessed contraband. <span class="citation" data-id="413271"><a href="/opinion/413271/russell-thomas-palmer-jr-v-ted-s-hudson-officer/#1224" aria-description="Citation for case: Russell Thomas Palmer, Jr. v. Ted S. Hudson, Officer"><em>Id., </em>at 1224</a></span>. Because the Court of Appeals concluded that the record reflected a factual dispute over whether the search of respondent’s cell was routine or conducted to harass respondent, it held that summary judgment was inappropriate, and that a remand was necessary to determine the purpose of the cell search.</p>
<p id="b564-4">We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./463/1206/">463 U. S. 1206</a></span> (1983). We affirm in part and reverse in part.</p>
<p id="b564-5">II</p>
<p id="b564-6">A</p>
<p id="b564-7">The first question we address is whether respondent has a right of privacy in his prison cell entitling him to the protection of the Fourth Amendment against unreasonable searches.<footnotemark>5</footnotemark> As we have noted, the Court of Appeals held that the District Court’s summary judgment in petitioner’s favor was premature because respondent had a “limited privacy right” in his cell that might have been breached. The court concluded that, to protect this privacy right, shakedown searches of an individual’s cell should be performed only “pursuant to an established program of conducting ran<page-number citation-index="1" label="523">*523</page-number>dom searches . . . reasonably designed to deter or discover the possession of contraband” or upon reasonable belief that the prisoner possesses contraband. Petitioner contends that the Court of Appeals erred in holding that respondent had even a limited privacy right in his cell, and urges that we adopt the “bright line” rule that prisoners have no legitimate expectation of privacy in their individual cells that would entitle them to Fourth Amendment protection.</p>
<p id="b565-5">We have repeatedly held that prisons are not beyond the reach of the Constitution. No “iron curtain” separates one from the other. <em>Wolff </em>v. <em>McDonnell, </em><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#555" aria-description="Citation for case: Wolff v. McDonnell">418 U. S. 539, 555</a></span> (1974). Indeed, we have insisted that prisoners be accorded those rights not fundamentally inconsistent with imprisonment itself or incompatible with the objectives of incarceration. For example, we have held that invidious racial discrimination is as intolerable within a prison as outside, except as may be essential to “prison security and discipline.” <em>Lee </em>v. <em>Washington, </em><span class="citation" data-id="9423632"><a href="/opinion/107630/lee-v-washington/" aria-description="Citation for case: Lee v. Washington">390 U. S. 333</a></span> (1968) <em>(per curiam). </em>Like others, prisoners have the constitutional right to petition the Government for redress of their grievances, which includes a reasonable right of access to the courts. <em>Johnson </em>v. <em>Avery, </em><span class="citation" data-id="9423904"><a href="/opinion/107840/johnson-v-avery/" aria-description="Citation for case: Johnson v. Avery">393 U. S. 483</a></span> (1969).</p>
<p id="b565-6">Prisoners must be provided “reasonable opportunities” to exercise their religious freedom guaranteed under the First Amendment. <em>Cruz </em>v. <em>Beto, </em><span class="citation" data-id="9424773"><a href="/opinion/108484/cruz-v-beto/" aria-description="Citation for case: Cruz v. Beto">405 U. S. 319</a></span> (1972) <em>(per curiam). </em>Similarly, they retain those First Amendment rights of speech “not inconsistent with [their] status as . . . prisoners] or with the legitimate penological objectives of the corrections system.” <em>Pell </em>v. <em>Procunier, </em><span class="citation" data-id="9425783"><a href="/opinion/109079/pell-v-procunier/#822" aria-description="Citation for case: Pell v. Procunier">417 U. S. 817, 822</a></span> (1974). They enjoy the protection of due process. <em>Wolff </em>v. <em><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/" aria-description="Citation for case: Wolff v. McDonnell">McDonnell, supra;</a></span> Haines </em>v. <em>Kerner, </em><span class="citation" data-id="108432"><a href="/opinion/108432/haines-v-kerner/" aria-description="Citation for case: Haines v. Kerner">404 U. S. 519</a></span> (1972). And the Eighth Amendment ensures that they will not be subject to “cruel and unusual punishments.” <em>Estelle </em>v. <em>Gamble, </em><span class="citation" data-id="9426610"><a href="/opinion/109561/estelle-v-gamble/" aria-description="Citation for case: Estelle v. Gamble">429 U. S. 97</a></span> (1976). The continuing guarantee of these substantial rights to prison inmates is testimony to a belief that the way a society treats those who have trans<page-number citation-index="1" label="524">*524</page-number>gressed against it is evidence of the essential character of that society.</p>
<p id="b566-5">However, while persons imprisoned for crime enjoy many protections of the Constitution, it is also clear that imprisonment carries with it the circumscription or loss of many significant rights. See <em>Bell </em>v. <em>Wolfish, </em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#545" aria-description="Citation for case: Bell v. Wolfish">441 U. S., at 545</a></span>. These constraints on inmates, and in some cases the complete withdrawal of certain rights, are “justified by the considerations underlying our penal system.” <em>Price </em>v. <em>Johnston, </em><span class="citation" data-id="9420168"><a href="/opinion/104557/price-v-johnston/#285" aria-description="Citation for case: Price v. Johnston">334 U. S. 266, 285</a></span> (1948); see also <em>Bell </em>v. <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Wolfish, supra,</a></span> </em>at 545-546 and cases cited; <em>Wolff </em>v. <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#555" aria-description="Citation for case: Wolff v. McDonnell"><em>McDonnell, supra, </em>at 555</a></span>. The curtailment of certain rights is necessary, as a practical matter, to accommodate a myriad of “institutional needs and objectives” of prison facilities, <em>Wolff </em>v. <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#555" aria-description="Citation for case: Wolff v. McDonnell"><em>McDonnell, supra, </em>at 555</a></span>, chief among which is internal security, see <em>Pell </em>v. <span class="citation" data-id="9425783"><a href="/opinion/109079/pell-v-procunier/#823" aria-description="Citation for case: Pell v. Procunier"><em>Procunier, supra, </em>at 823</a></span>. Of course, these restrictions or retractions also serve, incidentally, as reminders that, under our system of justice, deterrence and retribution are factors in addition to correction.</p>
<p id="b566-6">We have not before been called upon to decide the specific question whether the Fourth Amendment applies within a prison cell,<footnotemark>6</footnotemark> but the nature of our inquiry is well defined. <page-number citation-index="1" label="525">*525</page-number>We must determine here, as in other Fourth Amendment contexts, if a “justifiable” expectation of privacy is at stake. <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967). The applicability of the Fourth Amendment turns on whether “the person invoking its protection can claim a ‘justifiable/ a ‘reasonable/ or a ‘legitimate expectation of privacy’ that has been invaded by government action.” <em>Smith </em>v. <em>Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#740" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735, 740</a></span> (1979), and cases cited. We must decide, in Justice Harlan’s words, whether a prisoner’s expectation of privacy in his prison cell is the kind of expectation that “society is prepared to recognize as ‘reasonable.’ ” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States"><em>Katz, supra, </em>at 360, 361</a></span> (concurring opinion).<footnotemark>7</footnotemark></p>
<p id="b567-5">Notwithstanding our caution in approaching claims that the Fourth Amendment is inapplicable in a given context, we <page-number citation-index="1" label="526">*526</page-number>hold that society is not prepared to recognize as legitimate any subjective expectation of privacy that a prisoner might have in his prison cell and that, accordingly, the Fourth Amendment proscription against unreasonable searches does not apply within the confines of the prison cell. The recognition of privacy rights for prisoners in their individual cells simply cannot be reconciled with the concept of incarceration and the needs and objectives of penal institutions.</p>
<p id="b568-5">Prisons, by definition, are places of involuntary confinement of persons who have a demonstrated proclivity for antisocial criminal, and often violent, conduct. Inmates have necessarily shown a lapse in ability to control and conform their behavior to the legitimate standards of society by the normal impulses of self-restraint; they have shown an inability to regulate their conduct in a way that reflects either a respect for law or an appreciation of the rights of others. Even a partial survey of the statistics on violent crime in our Nation’s prisons illustrates the magnitude of the problem. During 1981 and the first half of 1982, there were over 120 prisoners murdered by fellow inmates in state and federal prisons. A number of prison personnel were murdered by prisoners during this period. Over 29 riots or similar disturbances were reported in these facilities for the same time frame. And there were over 125 suicides in these institutions. See Prison Violence, 7 Corrections Compendium (Mar. 1983). Additionally, informal statistics from the United States Bureau of Prisons show that in the federal system during 1983, there were 11 inmate homicides, 359 inmate assaults on other inmates, 227 inmate assaults on prison staff, and 10 suicides. There were in the same system in 1981 and 1982 over 750 inmate assaults on other inmates and over 570 inmate assaults on prison personnel.</p>
<p id="b568-6">Within this volatile “community,” prison administrators are to take all necessary steps to ensure the safety of not only the prison staffs and administrative personnel, but also visitors. They are under an obligation to take reasonable <page-number citation-index="1" label="527">*527</page-number>measures to guarantee the safety of the inmates themselves. They must be ever alert to attempts to introduce drugs and other contraband into the premises which, we can judicially notice, is one of the most perplexing problems of prisons today; they must prevent, so far as possible, the flow of illicit weapons into the prison; they must be vigilant to detect escape plots, in which drugs or weapons may be involved, before the schemes materialize. In addition to these monumental tasks, it is incumbent upon these officials at the same time to maintain as sanitary an environment for the inmates as feasible, given the difficulties of the circumstances.</p>
<p id="b569-5">The administration of a prison, we have said, is “at best an extraordinarily difficult undertaking.” <em>Wolff </em>v. <em>McDonnell, </em><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#566" aria-description="Citation for case: Wolff v. McDonnell">418 U. S., at 566</a></span>; <em>Hewitt </em>v. <em>Helms, </em><span class="citation" data-id="9429000"><a href="/opinion/110829/hewitt-v-helms/#467" aria-description="Citation for case: Hewitt v. Helms">459 U. S. 460, 467</a></span> (1983). But it would be literally impossible to accomplish the prison objectives identified above if inmates retained a right of privacy in their cells. Virtually the only place inmates can conceal weapons, drugs, and other contraband is in their cells. Unfettered access to these cells by prison officials, thus, is imperative if drugs and contraband are to be ferreted out and sanitary surroundings are to be maintained.</p>
<p id="b569-6">Determining whether an expectation of privacy is “legitimate” or “reasonable” necessarily entails a balancing of interests. The two interests here are the interest of society in the security of its penal institutions and the interest of the prisoner in privacy within his cell. The latter interest, of course, is already limited by the exigencies of the circumstances: A prison “shares none of the attributes of privacy of a home, an automobile, an office, or a hotel room.” <em>Lanza </em>v. <em>New York, </em><span class="citation" data-id="9422429"><a href="/opinion/106425/lanza-v-new-york/#143" aria-description="Citation for case: Lanza v. New York">370 U. S. 139, 143-144</a></span> (1962). We strike the balance in favor of institutional security, which we have noted is “central to all other corrections goals,” <em>Pell </em>v. <em>Procunier, </em><span class="citation" data-id="9425783"><a href="/opinion/109079/pell-v-procunier/#823" aria-description="Citation for case: Pell v. Procunier">417 U. S., at 823</a></span>. A right of privacy in traditional Fourth Amendment terms is fundamentally incompatible with the close and continual surveillance of inmates and their cells <page-number citation-index="1" label="528">*528</page-number>required to ensure institutional security and internal order.<footnotemark>8</footnotemark> We are satisfied that society would insist that the prisoner's expectation of privacy always yield to what must be considered the paramount interest in institutional security. We believe that it is accepted by our society that “[l]oss of freedom of choice and privacy are inherent incidents of confinement.” <em>Bell </em>v. Wolfish, <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#537" aria-description="Citation for case: Bell v. Wolfish">441 U. S., at 537</a></span>.</p>
<p id="b570-5">The Court of Appeals was troubled by the possibility of searches conducted solely to harass inmates; it reasoned that a requirement that searches be conducted only pursuant to an established policy or upon reasonable suspicion would prevent such searches to the maximum extent possible. Of course, there is a risk of maliciously motivated searches, and of course, intentional harassment of even the most hardened criminals cannot be tolerated by a civilized society. However, we disagree with the court’s proposed solution. The uncertainty that attends random searches of cells renders these searches perhaps the most effective weapon of the prison administrator in the constant fight against the proliferation of knives and guns, illicit drugs, and other contraband. The Court of Appeals candidly acknowledged that “the device [of random cell searches] is of. . . obvious utility in achieving the goal of prison security.” <span class="citation" data-id="413271"><a href="/opinion/413271/russell-thomas-palmer-jr-v-ted-s-hudson-officer/#1224" aria-description="Citation for case: Russell Thomas Palmer, Jr. v. Ted S. Hudson, Officer">697 F. 2d, at 1224</a></span>.</p>
<p id="b571-4"><page-number citation-index="1" label="529">*529</page-number>A requirement that even random searches be conducted pursuant to an established plan would seriously undermine the effectiveness of this weapon. It is simply naive to believe that prisoners would not eventually decipher any plan officials might devise for “planned random searches,” and thus be able routinely to anticipate searches. The Supreme Court of Virginia identified the shortcomings of an approach such as that adopted by the Court of Appeals and the necessity of allowing prison administrators flexibility:</p>
<blockquote id="b571-5">“For one to advocate that prison searches must be conducted only pursuant to an enunciated general policy or when suspicion is directed at a particular inmate is to ignore the realities of prison operation. Random searches of inmates, individually or collectively, and their cells and lockers are valid and necessary to ensure the security of the institution and the safety of inmates and all others within its boundaries. This type of search allows prison officers flexibility and prevents inmates from anticipating, and thereby thwarting, a search for contraband.” <em>Marrero </em>v. <em>Commonwealth, </em><span class="citation" data-id="1302147"><a href="/opinion/1302147/marrero-v-commonwealth/#757" aria-description="Citation for case: Marrero v. Commonwealth">222 Va. 754, 757</a></span>, <span class="citation" data-id="1302147"><a href="/opinion/1302147/marrero-v-commonwealth/#811" aria-description="Citation for case: Marrero v. Commonwealth">284 S. E. 2d 809, 811</a></span> (1981).</blockquote>
<p id="b571-6">We share the concerns so well expressed by the Supreme Court and its view that wholly random searches are essential to the effective security of penal institutions. We, therefore, cannot accept even the concededly limited holding of the Court of Appeals.</p>
<p id="b571-7">Respondent acknowledges that routine shakedowns of prison cells are essential to the effective administration of prisons. Brief for Respondent and Cross-Petitioner 7, n. 5. He contends, however, that he is constitutionally entitled not to be subjected to searches conducted only to harass. The crux of his claim is that “because searches and seizures to harass are unreasonable, a prisoner has a reasonable expectation of privacy not to have his cell, locker, personal effects, person invaded for such a purpose.”, <em>Id., </em>at 24. This argu<page-number citation-index="1" label="530">*530</page-number>ment, which assumes the answer to the predicate question whether a prisoner has a legitimate expectation of privacy in his prison cell at all, is merely a challenge to the reasonableness of the particular search of respondent’s cell. Because we conclude that prisoners have no legitimate expectation of privacy and that the Fourth Amendment’s prohibition on unreasonable searches does not apply in prison cells, we need not address this issue.</p>
<p id="b572-5">Our holding that respondent does not have a reasonable expectation of privacy enabling him to invoke the protections of the Fourth Amendment does not mean that he is without a remedy for calculated harassment unrelated to prison needs. Nor does it mean that prison attendants can ride roughshod over inmates’ property rights with impunity. The Eighth Amendment always stands as a protection against “cruel and unusual punishments.” By the same token, there are adequate state tort and common-law remedies available to respondent to redress the alleged destruction of his personal property. See discussion <em>infra, </em>at 534-536.<footnotemark>9</footnotemark></p>
<p id="b572-6">B</p>
<p id="b572-7">In his complaint in the District Court, in addition to his claim that the shakedown search of his cell violated his Fourth and Fourteenth Amendment privacy rights, respondent alleged under <span class="citation no-link">42 U. S. C. § 1983</span> that petitioner intentionally destroyed certain of his personal property during the search. This destruction, respondent contended, deprived him of property without due process, in violation of the Due Process Clause of the Fourteenth Amendment. The District Court dismissed this portion of respondent’s complaint for failure to state a claim. Reasoning under <em>Parratt </em>v. <em>Taylor, </em><page-number citation-index="1" label="531">*531</page-number><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">451 U. S. 527</a></span> (1981), it held that even an intentional destruction of property by a state employee does not violate due process if the state provides a meaningful postdeprivation remedy. The Court of Appeals affirmed. The question presented for our review in Palmer’s cross-petition is whether our decision in <em>Parratt </em>v. <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Taylor</a></span> </em>should extend, as the Court of Appeals held, to intentional deprivations of property by state employees acting under color of state law.<footnotemark>10</footnotemark></p>
<p id="b573-5">In <em>Parratt </em>v. <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Taylor</a></span>, </em>a state prisoner sued prison officials under <span class="citation no-link">42 U. S. C. § 1988</span>, alleging that their negligent loss of a hobby kit he ordered from a mail-order catalog deprived him of property without due process of law, in violation of the Fourteenth Amendment. The Court of Appeals for the Eighth Circuit had affirmed the District Court’s summary judgment in the prisoner’s favor. We reversed, holding that the Due Process Clause of the Fourteenth Amendment is not violated when a state employee negligently deprives an individual of property, provided that the state makes available a meaningful postdeprivation remedy.<footnotemark>11</footnotemark></p>
<p id="b573-6">We viewed our decision in <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span> </em>as consistent with prior cases recognizing that</p>
<blockquote id="b573-7">“either the necessity of quick action by the State or the impracticality of providing any meaningful predeprivation process, when coupled with the availability of some <page-number citation-index="1" label="532">*532</page-number>meaningful means by which to assess the propriety of the State’s action at some time after the initial taking . . . satisfies] the requirements of procedural due process.” <span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/#539" aria-description="Citation for case: Parratt v. Taylor">451 U. S., at 539</a></span> (footnote omitted).</blockquote>
<p id="b574-5">We reasoned that where a loss of property is occasioned by a random, unauthorized act by a state employee, rather than by an established state procedure, the state cannot predict when the loss will occur. <span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/#541" aria-description="Citation for case: Parratt v. Taylor"><em>Id., </em>at 541</a></span>. Under these circumstances, we observed:</p>
<blockquote id="b574-6">“It is difficult to conceive of how the State could provide a meaningful hearing before the deprivation takes place. The loss of property, although attributable to the State as action under ‘color of law,’ is in almost all cases beyond the control of the State. Indeed, in most cases it is not only impracticable, but impossible, to provide a meaningful hearing before the deprivation.” <span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Ibid.</a></span><footnotemark>12</footnotemark></blockquote>
<p id="b574-7">Two Terms ago, we reaffirmed our holding in <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span> </em>in <em>Logan </em>v. <em>Zimmerman Brush Co., </em><span class="citation" data-id="9428680"><a href="/opinion/110657/logan-v-zimmerman-brush-co/" aria-description="Citation for case: Logan v. Zimmerman Brush Co.">455 U. S. 422</a></span> (1982), in the course of holding that postdeprivation remedies do not satisfy due process where a deprivation of property is caused by conduct pursuant to established state procedure, rather than random and unauthorized action.<footnotemark>13</footnotemark></p>
<p id="b575-4"><page-number citation-index="1" label="533">*533</page-number>While <em>Parrott </em>is necessarily limited by its facts to negligent deprivations of property, it is evident, as the Court of Appeals recognized, that its reasoning applies as well to intentional deprivations of property. The underlying rationale of <em>Parrott </em>is that when deprivations of property are effected through random and unauthorized conduct of a state employee, predeprivation procedures are simply “impracticable” since the state cannot know when such deprivations will occur. We can discern no logical distinction between negligent and intentional deprivations of property insofar as the “practicability” of affording predeprivation process is concerned. The state can no more anticipate and control in advance the random and unauthorized intentional conduct of its employees than it can anticipate similar negligent conduct. Arguably, intentional acts are even more difficult to anticipate because one bent on intentionally depriving a person of his property might well take affirmative steps to avoid signalling his intent.</p>
<p id="b575-5">If negligent deprivations of property do not violate the Due Process Clause because predeprivation process is impracticable, it follows that intentional deprivations do not violate that Clause provided, of course, that adequate state post-deprivation remedies are available. Accordingly, we hold that an unauthorized intentional deprivation of property by a state employee does not constitute a violation of the procedural requirements of the Due Process Clause of the Fourteenth Amendment if a meaningful postdeprivation remedy for the loss is available. For intentional, as for negligent deprivations of property by state employees, the state’s action is not complete until and unless it provides or refuses to provide a suitable postdeprivation remedy.<footnotemark>14</footnotemark></p>
<p id="b576-4"><page-number citation-index="1" label="534">*534</page-number>Respondent presses two arguments that require at least brief comment. First, he contends that, because an agent of the state who intends to deprive a person of his property <em>“can </em>provide predeprivation process, then as a matter of due process he must do so.” Brief for Respondent and Cross-Petitioner 8 (emphasis in original). This argument reflects a fundamental misunderstanding of <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span>. </em>There we held that postdeprivation procedures satisfy due process because the <em>state </em>cannot possibly know in advance of a negligent deprivation of property. Whether an individual employee himself is able to foresee a deprivation is simply of no consequence. The controlling inquiry is solely whether the state is in a position to provide for predeprivation process.</p>
<p id="b576-5">Respondent also contends, citing to <em>Logan </em>v. <em>Zimmerman Brush Co., supra, </em>that the deliberate destruction of his property by petitioner constituted a due process violation despite the availability of postdeprivation remedies. Brief for Respondent and Cross-Petitioner 8. In <em><span class="citation" data-id="9428680"><a href="/opinion/110657/logan-v-zimmerman-brush-co/" aria-description="Citation for case: Logan v. Zimmerman Brush Co.">Logan</a></span>, </em>we decided a question about which our decision in <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span> </em>left little doubt, that is, whether a postdeprivation state remedy satisfies due process where the property deprivation is effected pursuant to an established state procedure. We held that it does not. <em><span class="citation" data-id="9428680"><a href="/opinion/110657/logan-v-zimmerman-brush-co/" aria-description="Citation for case: Logan v. Zimmerman Brush Co.">Logan</a></span> </em>plainly has no relevance here. Respondent does not even allege that the asserted destruction of his property occurred pursuant to a state procedure.</p>
<p id="b576-6">Having determined that <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span> </em>extends to intentional deprivations of property, we need only decide whether the Commonwealth of Virginia provides respondent an adequate postdeprivation remedy for the alleged destruction of his property. Both the District Court and, at least implicitly, the Court of Appeals held that several common-law remedies <page-number citation-index="1" label="535">*535</page-number>available to respondent would provide adequate compensation for his property loss. We have no reason to question that determination, particularly given the speculative nature of respondent’s arguments.</p>
<p id="b577-5">Palmer does not seriously dispute the adequacy of the existing state-law remedies themselves. He asserts in this respect only that, because certain of his legal papers allegedly taken “may have contained things irreplacable <em>[sic], </em>and incompensable” or “may also have involved sentimental items which are of equally intangible value,” Brief for Respondent and Cross-Petitioner 10-11, n. 10, a suit in tort, for example, would not “necessarily” compensate him fully. If the loss is “incompensable,” this is as much so under § 1983 as it would be under any other remedy. In any event, that Palmer might not be able to recover under these remedies the full amount which he might receive in a § 1983 action is not, as we have said, determinative of the adequacy of the state remedies. See <em>Parratt, </em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/#544" aria-description="Citation for case: Parratt v. Taylor">451 U. S., at 544</a></span>.</p>
<p id="b577-6">Palmer contends also that relief under applicable state law “is far from certain and complete” because a state court might hold that petitioner, as a state employee, is entitled to sovereign immunity. Brief for Respondent and Cross-Petitioner 11. This suggestion is unconvincing. The District Court and the Court of Appeals held that respondent’s claim would not be barred by sovereign immunity. As the District Court noted, under Virginia law, “a State employee may be held liable for his intentional torts,” <em>Elder </em>v. <em>Holland, </em><span class="citation" data-id="1384033"><a href="/opinion/1384033/elder-v-holland/#19" aria-description="Citation for case: Elder v. Holland">208 Va. 15, 19</a></span>, <span class="citation" data-id="1384033"><a href="/opinion/1384033/elder-v-holland/#372" aria-description="Citation for case: Elder v. Holland">155 S. E. 2d 369, 372-373</a></span> (1967); see also <em>Short </em>v. <em>Griffitts, </em><span class="citation" data-id="1304356"><a href="/opinion/1304356/short-v-griffitts/" aria-description="Citation for case: Short v. Griffitts">220 Va. 53</a></span>, <span class="citation" data-id="1304356"><a href="/opinion/1304356/short-v-griffitts/" aria-description="Citation for case: Short v. Griffitts">255 S. E. 2d 479</a></span> (1979). Indeed, respondent candidly acknowledges that it is “probable that a Virginia trial court would rule that there should be no immunity bar in the present case.” Brief for Respondent and Cross-Petitioner 14.</p>
<p id="b577-7">Respondent attempts to cast doubt on the obvious breadth of <em><span class="citation" data-id="1384033"><a href="/opinion/1384033/elder-v-holland/" aria-description="Citation for case: Elder v. Holland">Elder</a></span> </em>through the naked assertion that “the phrase ‘may <page-number citation-index="1" label="536">*536</page-number>be held liable’ could have meant . . . only the possibility of liability under certain circumstances rather than a blanket rule . . . Brief for Respondent and Cross-Petitioner 13. We are equally unpersuaded by this speculation. The language of <em><span class="citation" data-id="1384033"><a href="/opinion/1384033/elder-v-holland/" aria-description="Citation for case: Elder v. Holland">Elder</a></span> </em>is unambiguous that employees of the Commonwealth do not enjoy sovereign immunity for their intentional torts, and <em><span class="citation" data-id="1384033"><a href="/opinion/1384033/elder-v-holland/" aria-description="Citation for case: Elder v. Holland">Elder</a></span> </em>has been so read by a number of federal courts, as respondent concedes, see Brief for Respondent and Cross-Petitioner 13, n. 13. See, <em>e. g., Holmes </em>v. <em>Wampler, </em><span class="citation" data-id="1870743"><a href="/opinion/1870743/holmes-v-wampler/#504" aria-description="Citation for case: Holmes v. Wampler">546 F. Supp. 500, 504</a></span> (ED Va. 1982); <em>Irshad </em>v. <em>Spann, </em><span class="citation" data-id="1460980"><a href="/opinion/1460980/al-mustafa-irshad-v-spann/#928" aria-description="Citation for case: Al-Mustafa Irshad v. Spann">543 F. Supp. 922, 928</a></span> (ED Va. 1982); <em>Frazier </em>v. <em>Collins, </em><span class="citation" data-id="1686657"><a href="/opinion/1686657/frazier-v-collins/#110" aria-description="Citation for case: Frazier v. Collins">544 F. Supp. 109, 110</a></span> (ED Va. 1982); <em>Whorley </em>v. <em>Karr, </em><span class="citation" data-id="1443669"><a href="/opinion/1443669/whorley-v-karr/#89" aria-description="Citation for case: Whorley v. Karr">534 F. Supp. 88, 89</a></span> (WD Va. 1981); <em>Daughtry </em>v. <em>Arlington County, Va., </em><span class="citation" data-id="1905445"><a href="/opinion/1905445/daughtry-v-arlington-county-va/" aria-description="Citation for case: Daughtry v. Arlington County, Va.">490 F. Supp. 307</a></span> (DC 1980).<footnotemark>15</footnotemark> In sum, it is evident here, as in <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span>, </em>that the State has provided an adequate postdeprivation remedy for the alleged destruction of property.</p>
<p id="b578-5">Ill</p>
<p id="b578-6">We hold that the Fourth Amendment has no applicability to a prison cell. We hold also that, even if petitioner intentionally destroyed respondent’s personal property during the challenged shakedown search, the destruction did not violate the Fourteenth Amendment since the Commonwealth of Virginia has provided respondent an adequate postdeprivation remedy.</p>
<p id="b578-7">Accordingly, the judgment of the Court of Appeals reversing and remanding the District Court’s judgment on respond<page-number citation-index="1" label="537">*537</page-number>ent’s claim under the Fourth and Fourteenth Amendments is reversed. The judgment affirming the District Court’s decision that respondent has not been denied due process under the Fourteenth Amendment is affirmed.</p>
<p id="b579-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b562-7"> The District Court determined that Palmer could proceed against Hudson in state court either for conversion or for detinue, and that under applicable Virginia law, see <em>Elder </em>v. <em>Holland, </em><span class="citation" data-id="1384033"><a href="/opinion/1384033/elder-v-holland/" aria-description="Citation for case: Elder v. Holland">208 Va. 15</a></span>, <span class="citation" data-id="1384033"><a href="/opinion/1384033/elder-v-holland/" aria-description="Citation for case: Elder v. Holland">155 S. E. 2d 369</a></span> (1967), Hudson would not be entitled to immunity for the alleged intentional tort.</p>
</footnote>
<footnote label="2">
<p id="b563-6"> The Court of Appeals observed that “there is no practical mechanism by which Virginia could prevent its guards from conducting personal vendettas against prisoners other than by punishing them after the fact.. . .” <span class="citation" data-id="413271"><a href="/opinion/413271/russell-thomas-palmer-jr-v-ted-s-hudson-officer/#1223" aria-description="Citation for case: Russell Thomas Palmer, Jr. v. Ted S. Hudson, Officer">697 F. 2d, at 1223</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b563-7"> See n. 1, <em>supra.</em></p>
</footnote>
<footnote label="4">
<p id="b563-8"> Petitioner maintains that the Court of Appeals’ decision rests at least in part upon a finding of an independent right of privacy for prisoners under the Fourteenth Amendment alone. Arguably, it is not entirely clear whether the Court of Appeals believed that the limited privacy right it recognized was guaranteed solely by the Fourth Amendment, and applicable to the States only through the Fourteenth Amendment, or whether the right emanated from the Fourteenth Amendment alone, or both. The court’s opinion, however, explicitly speaks to the “primary purpose of the Fourth and Fourteenth Amendments,” <span class="citation" data-id="413271"><a href="/opinion/413271/russell-thomas-palmer-jr-v-ted-s-hudson-officer/#1224" aria-description="Citation for case: Russell Thomas Palmer, Jr. v. Ted S. Hudson, Officer">697 F. 2d, at 1224</a></span>, and nowhere does it suggest an intention to draw a distinction between the Fourth and Fourteenth Amendment right of privacy in prison cells. Under the circumstances, we assume, since there is no suggestion to the contrary, that the court did not mean to imply in this context that any right of privacy that might exist under the Fourteenth Amendment alone exceeds that which exists under the Fourth Amendment.</p>
</footnote>
<footnote label="5">
<p id="b564-8"> The majority of the Courts of Appeals have held that a prisoner retains at least a minimal degree <em>of </em>Fourth Amendment protection in his cell. See <em>United States </em>v. <em>Chamorro, </em><span class="citation" data-id="407932"><a href="/opinion/407932/united-states-v-sergio-chamorro-aka-sergio-hernandez/" aria-description="Citation for case: United States v. Sergio Chamorro A/K/A Sergio Hernandez">687 F. 2d 1</a></span> (CA1 1982); <em>United States </em>v. <em>Hinckley, </em>217 U. S. App. D. C. 262, <span class="citation" data-id="400069"><a href="/opinion/400069/united-states-v-john-w-hinckley-jr-united-states-of-america-v-john-w/" aria-description="Citation for case: United States v. John W. Hinckley, Jr. United States of...">672 F. 2d 115</a></span> (1982); <em>United States </em>v. <em>Lilly, </em><span class="citation" data-id="9464833"><a href="/opinion/356030/united-states-v-sherry-marie-lilly-united-states-of-america-v-merrilyn/" aria-description="Citation for case: United States v. Sherry Marie Lilly, United States of...">576 F. 2d 1240</a></span> (CA5 1978); <em>United States </em>v. <em>Stumes, </em><span class="citation" data-id="343130"><a href="/opinion/343130/united-states-v-norman-stumes/" aria-description="Citation for case: United States v. Norman Stumes">549 F. 2d 831</a></span> (CA8 1977); <em>Bonner </em>v. <em>Coughlin, </em><span class="citation" data-id="9461858"><a href="/opinion/328221/alonzo-bonner-v-joseph-coughlin/" aria-description="Citation for case: Alonzo Bonner v. Joseph Coughlin">517 F. 2d 1311</a></span> (CA7 1975) (vacating District Court judgment), on rehearing, <span class="citation" data-id="9463304"><a href="/opinion/340703/alonzo-bonner-v-joseph-coughlin/" aria-description="Citation for case: Alonzo Bonner v. Joseph Coughlin">545 F. 2d 565</a></span> (1976) (en banc) (affirming District Court on other grounds), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./435/932/">435 U. S. 932</a></span> (1978). The Second and Ninth Circuits, however, have held that the Fourth Amendment does not apply in a prison cell. See <em>Christman </em>v. <em>Skinner, </em><span class="citation" data-id="9458823"><a href="/opinion/306226/miles-christman-v-albert-skinner/" aria-description="Citation for case: Miles Christman v. Albert Skinner">468 F. 2d 723</a></span> (CA2 1972); <em>United States </em>v. <em>Hitchcock, </em><span class="citation" data-id="305965"><a href="/opinion/305965/united-states-v-benjamin-hitchcock/" aria-description="Citation for case: United States v. Benjamin Hitchcock">467 F. 2d 1107</a></span> (CA9 1972), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./410/916/">410 U. S. 916</a></span> (1973).</p>
</footnote>
<footnote label="6">
<p id="b566-7"> In <em>Lanza </em>v. <em>New York, </em><span class="citation" data-id="9422429"><a href="/opinion/106425/lanza-v-new-york/#143" aria-description="Citation for case: Lanza v. New York">370 U. S. 139, 143-144</a></span> (1962), a plurality of the Court termed as “at best a novel argument” the assertion that a prison “is a place where [one] can claim constitutional immunity from search or seizure of his person, his papers, or his effects.” This observation, however, was plainly dictum. In fact, three Members of the Court specifically dissented from what they characterized as the Court’s “gratuitous exposition of several grave constitutional issues . . . .” <span class="citation" data-id="9422429"><a href="/opinion/106425/lanza-v-new-york/#150" aria-description="Citation for case: Lanza v. New York"><em>Id., </em>at 150</a></span> (Brennan, J., dissenting, joined by Warren, C. J., and Douglas, J.).</p>
<p id="b566-8">In upholding a room search rule against a Fourth Amendment challenge by pretrial detainees in <em>Bell </em>v. <em>Wolfish, </em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">441 U. S. 520</a></span> (1979), the Court acknowledged the plausibility of an argument that “a person confined in a detention facility has no reasonable expectation of privacy with respect to his room or cell and that therefore the Fourth Amendment provides no protection for such a person.” <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#556" aria-description="Citation for case: Bell v. Wolfish"><em>Id., </em>at 556-557</a></span>. However, as in <em><span class="citation" data-id="9422429"><a href="/opinion/106425/lanza-v-new-york/" aria-description="Citation for case: Lanza v. New York">Lanza</a></span>, </em>it was unnecessary to reach the issue of the Fourth Amendment’s general <page-number citation-index="1" label="525">*525</page-number>applicability in a prison cell. We simply assumed, <em>arguendo, </em>that a pretrial detainee retained at least a “diminished expectation of privacy.” <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#557" aria-description="Citation for case: Bell v. Wolfish">441 U. S., at 557</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b567-9"> In <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>Justice Harlan suggested that an expectation of privacy is “justifiable” if the person concerned has “exhibited an actual (subjective) expectation of privacy” and the expectation is one that “society is prepared to recognize as ‘reasonable.’ ” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States">389 U. S., at 360, 361</a></span> (concurring opinion). The Court has always emphasized the second of these two requirements. As Justice White said, writing for the plurality in <em>United States </em>v. <em>White, </em><span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/" aria-description="Citation for case: United States v. White">401 U. S. 745</a></span> (1971): “Our problem is not what the privacy expectations of particular defendants in particular situations may be or the extent to which they may in fact have relied on the discretion of their companions. . . . Our problem, in terms of the principles announced in <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>is what expectations of privacy are constitutionally ‘justifiable’. . . .” <em>Id., </em>at 751-752. In the same case, even Justice Harlan stressed the controlling importance of the second of these two requirements: “The analysis must, in my view, transcend the search for subjective expectations .... [W]e should not, as judges, merely recite the expectations and risks without examining the desirability of saddling them upon society.” <em>United States </em>v. <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#768" aria-description="Citation for case: United States v. White"><em>White, supra, </em>at 768, 786</a></span> (dissenting opinion).</p>
<p id="b567-10">The Court’s refusal to adopt a test of “subjective expectation” is understandable; constitutional rights are generally not defined by the subjective intent of those asserting the rights. The problems inherent in such a standard are self-evident. See, <em>e. g., Smith </em>v. <em>Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#740" aria-description="Citation for case: Smith v. Maryland">442 U. S., at 740-741, n. 5</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b570-6"> Respondent contends also that the destruction of his personal property constituted an unreasonable <em>seizure </em>of that property violative of the Fourth Amendment. Assuming that the Fourth Amendment protects against the destruction of property, in addition to its mere seizure, the same reasons that lead us to conclude that the Fourth Amendment’s proscription against unreasonable searches is inapplicable in a prison cell, apply with controlling force to seizures. Prison officials must be free to seize from cells any articles which, in their view, disserve legitimate institutional interests.</p>
<p id="b570-7">That the Fourth Amendment does not protect against seizures in a prison cell does not mean that an inmate’s property can be destroyed with impunity. We note, for example, that even apart from inmate grievance procedures, see n. 9, <em>infra, </em>respondent has adequate state remedies for the alleged destruction of his property. See discussion <em>infra, </em>at 534-536.</p>
</footnote>
<footnote label="9">
<p id="b572-8"> The Commonwealth has a new inmate grievance procedure that was effective as of October 12, 1982, see n. 14, <em>infra. </em>But it appears that at the time of the alleged deprivation of respondent’s property, a very similar procedure was in effect that would also have afforded respondent relief for any destruction of his property. See Reply Brief for Petitioner and Cross-Respondent 13, n. 14.</p>
</footnote>
<footnote label="10">
<p id="b573-8"> Four Circuits, including the Fourth Circuit in these cases, have held that <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span> </em>extends to intentional deprivations of property. See <em>Wolf-Lillie </em>v. <em>Sonquist, </em><span class="citation" data-id="414190"><a href="/opinion/414190/arlene-c-wolf-lillie-v-gerald-m-sonquist-kenosha-county-sheriff/" aria-description="Citation for case: Arlene C. Wolf-Lillie v. Gerald M. Sonquist, Kenosha...">699 F. 2d 864</a></span> (CA7 1983); <em>Engblom </em>v. <em>Carey, </em><span class="citation" data-id="8915132"><a href="/opinion/8925582/engblom-v-carey/" aria-description="Citation for case: Engblom v. Carey">677 F. 2d 957</a></span> (CA2 1982); <em>Rutledge </em>v. <em>Arizona Board of Regents, </em><span class="citation" data-id="8914062"><a href="/opinion/8924683/rutledge-v-arizona-board-of-regents/" aria-description="Citation for case: Rutledge v. Arizona Board of Regents">660 F. 2d 1345</a></span> (CA9 1981), aff’d <em>sub nom. Kush </em>v. <em>Rutledge, </em><span class="citation" data-id="110900"><a href="/opinion/110900/kush-v-rutledge/" aria-description="Citation for case: Kush v. Rutledge">460 U. S. 719</a></span> (1983). Three Circuits have held that it does not. <em>Brewer </em>v. <em>Blackwell, </em><span class="citation" data-id="410403"><a href="/opinion/410403/joseph-brewer-v-m-prentiss-blackwell/" aria-description="Citation for case: Joseph Brewer v. M. Prentiss Blackwell">692 F. 2d 387</a></span> (CA5 1982); <em>Weiss </em>v. <em>Lehman, </em><span class="citation" data-id="9469157"><a href="/opinion/403393/e-b-weiss-v-r-c-lehman-and-wayne-larue/" aria-description="Citation for case: E. B. Weiss v. R. C. Lehman and Wayne Larue">676 F. 2d 1320</a></span> (CA9 1982); <em>Madyun </em>v. <em>Thompson, </em><span class="citation" data-id="393729"><a href="/opinion/393729/yusuf-asad-madyun-v-james-r-thompson-governor/" aria-description="Citation for case: Yusuf Asad Madyun v. James R. Thompson, Governor">657 F. 2d 868</a></span> (CA7 1981).</p>
</footnote>
<footnote label="11">
<p id="b573-9"> Nebraska had provided respondent with a tort remedy for his alleged property deprivation. <span class="citation no-link">Neb. Rev. Stat. § 81-8</span>,209 <em>et seq. </em>(1976). We held that this remedy was entirely adequate to satisfy due process, even though we recognized that it might not provide respondent all the relief to which he might have been entitled under § 1983. <span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/#543" aria-description="Citation for case: Parratt v. Taylor">451 U. S., at 543-544</a></span>.</p>
</footnote>
<footnote label="12">
<p id="b574-8"> In reaching our conclusion in <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span>, </em>we expressly relied on then-judge Stevens’ opinion for the Seventh Circuit in <em>Bonner </em>v. <em>Coughlin, </em><span class="citation" data-id="9461858"><a href="/opinion/328221/alonzo-bonner-v-joseph-coughlin/" aria-description="Citation for case: Alonzo Bonner v. Joseph Coughlin">517 F. 2d 1311</a></span> (1975), modified en banc, <span class="citation" data-id="9463304"><a href="/opinion/340703/alonzo-bonner-v-joseph-coughlin/" aria-description="Citation for case: Alonzo Bonner v. Joseph Coughlin">545 F. 2d 565</a></span> (1976), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./435/932/">435 U. S. 932</a></span> (1978), holding that, where an individual has been negligently deprived of property by a state employee, the state’s action is not complete unless or until the state fails to provide an adequate postdeprivation remedy for the property loss. <span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/#541" aria-description="Citation for case: Parratt v. Taylor">451 U. S., at 541-542</a></span>.</p>
</footnote>
<footnote label="13">
<p id="b574-9"> In <em><span class="citation" data-id="9428680"><a href="/opinion/110657/logan-v-zimmerman-brush-co/" aria-description="Citation for case: Logan v. Zimmerman Brush Co.">Logan</a></span>, </em>we examined a claim that the terms of an Illinois statute deprived the petitioner of an opportunity to pursue his employment discrimination claim. We specifically distinguished the case from <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span> </em>by noting that <em>“Parratt. . . </em>was dealing with a. . . ‘random and unauthorized act by a state employee... [and was] not a result of some established state procedure.’” <span class="citation" data-id="9428680"><a href="/opinion/110657/logan-v-zimmerman-brush-co/" aria-description="Citation for case: Logan v. Zimmerman Brush Co.">455 U. S., at 435</a></span>-436 (quoting <em>Parratt, </em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/#541" aria-description="Citation for case: Parratt v. Taylor">451 U. S., at 541</a></span>). <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span>, </em>we said, “was not designed to reach ... a situation” where the <page-number citation-index="1" label="533">*533</page-number>deprivation is the result of an established state procedure. <span class="citation" data-id="9428680"><a href="/opinion/110657/logan-v-zimmerman-brush-co/#436" aria-description="Citation for case: Logan v. Zimmerman Brush Co.">455 U. S., at 436</a></span>.</p>
</footnote>
<footnote label="14">
<p id="b575-7"> Our holding that an intentional deprivation of property does not give rise to a violation of the Due Process Clause if the state provides an adequate postdeprivation remedy was foreshadowed by our discussion of <page-number citation-index="1" label="534">*534</page-number><em>Ingraham </em>v. <em>Wright, </em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651</a></span> (1977), in <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span>. </em>We noted that our analysis was “quite consistent” with that in <em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">Ingraham</a></span>, </em>a case that, we observed, involved intentional conduct on behalf of state officials. <span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/#542" aria-description="Citation for case: Parratt v. Taylor">451 U. S., at 542</a></span>.</p>
</footnote>
<footnote label="15">
<p id="b578-8"> It is noteworthy that the Commonwealth has enacted the State Tort Claims Act, Va. Code §8.01-195.1 <em>et seq. </em>(Supp. 1983), which, in defined circumstances, waives sovereign immunity. Additionally, as of October 12, 1982, the State has in place an inmate grievance procedure that received the certification of the Attorney General of the United States as in compliance with the Civil Rights of Institutionalized Persons Act, 42 U. S. C. § 1997e. Although apparently neither of these avenues was open to this respondent, both are potential sources of relief for persons in respondent’s position in the future.</p>
</footnote>
</opinion>
```

---
