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

## GROUP: content/cases/Johnson v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Johnson v. United States"
type: case
citation: "333 U.S. 10 (1948)"
parallel_cite: "68 S. Ct. 367; 92 L. Ed. 2d 436; 92 L. Ed. 436"
neutral_cite: 1948 U.S. LEXIS 2583
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1948
date_decided: 1948-02-02
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1948-02-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Johnson v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/104504/johnson-v-united-states/"
  cluster_id: 104504
  opinion_id: 104504
  identity_checked: true
homes:
  - page: "[[The Neutral and Detached Magistrate]]"
    role: "Key — Anchor"
related: ["[[Katz v. United States]]", "[[Coolidge v. New Hampshire]]", "[[Payton v. New York]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant", "neutral-magistrate", "probable-cause"]
holding: "Probable-cause inferences must be drawn by a neutral and detached magistrate, not by the officer engaged in ferreting out crime."
lake:
  record_id: Johnson v. United States
  status: verified
  projected_at: 2026-07-06
---

# Johnson v. United States

*333 U.S. 10 (1948)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers, acting on an informant's tip, detected the distinctive odor of burning opium coming from a hotel room. Without a warrant, they knocked, entered when the occupant opened the door, arrested Johnson, and searched the room, finding opium and smoking apparatus. Johnson challenged the warrantless search.

## Issue
Whether officers who have probable cause may conduct a warrantless search of a home or hotel room, or whether the probable-cause determination must instead be made by a neutral magistrate issuing a warrant.

## Rule
The probable-cause inference must be drawn by a neutral magistrate, not the investigating officer. "The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime." — 333 U.S. at 13–14. ^pin-13

"Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers." — *Id.* at 14. ^pin-14

## Application
The opium odor may well have furnished probable cause, but the officers — not a magistrate — made that judgment and searched the room without a warrant. No exceptional circumstances excused the failure to obtain a warrant: there was no consent, no search incident to a valid arrest (the arrest itself depended on the entry), and no risk of evidence destruction shown. Because the officers, rather than a neutral magistrate, drew the probable-cause inference, the warrantless search was unreasonable.

## Conclusion
The warrantless search was invalid; the conviction resting on the seized evidence was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Johnson*'s neutral-and-detached-magistrate principle remains a cornerstone of the warrant requirement and is invoked across the modern Fourth Amendment cases, including [[Katz v. United States]] and [[Coolidge v. New Hampshire]].

## Appears on
- [[The Neutral and Detached Magistrate]] — *Key — Anchor*

## Sources
- *Johnson v. United States*, 333 U.S. 10 (1948) — https://www.courtlistener.com/opinion/104504/johnson-v-united-states/ — pinpoints: 13, 14.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ee22b8330ee40de4", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "333 U.S. 10 (1948)", "court": "U.S. Supreme Court", "neutral_cite": "1948 U.S. LEXIS 2583", "official_citation_present": true, "parallel_cite": "68 S. Ct. 367; 92 L. Ed. 2d 436; 92 L. Ed. 436", "title": "Johnson v. United States", "year": "1948"}}
{"assertion_id": "3236643db48a28c7", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Probable-cause inferences must be drawn by a neutral and detached magistrate, not by the officer engaged in ferreting out crime.", "title": "Johnson v. United States"}}
{"assertion_id": "af716069610c6913", "dimension": "support", "kind": "home_role", "locator": {"home": "The Neutral and Detached Magistrate"}, "payload": {"home": "The Neutral and Detached Magistrate", "role": "Key — Anchor", "title": "Johnson v. United States"}}
{"assertion_id": "6cd0e9d17e96e783", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Johnson v. United States"}}
{"assertion_id": "fda4a69fad4a3a52", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1948-02-02", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Johnson v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Johnson v. United States", "varies_by_point": "false"}}
```

### lake record — Johnson v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Johnson v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Johnson v. United States",
    "case_name_short": "",
    "case_name_full": "Johnson v. United States",
    "input_case_name": "Johnson v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1948-02-02",
    "year": 1948,
    "docket": null,
    "cluster_id": 104504,
    "lead_opinion_id": 104504,
    "sibling_ids": [
      104504
    ],
    "absolute_url": "/opinion/104504/johnson-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8202565,
        "score": 20,
        "case_name": "Johnson v. United States"
      },
      {
        "cluster_id": 8202381,
        "score": 20,
        "case_name": "Johnson v. United States"
      },
      {
        "cluster_id": 104507,
        "score": 20,
        "case_name": "Johnson v. United States"
      },
      {
        "cluster_id": 8202305,
        "score": 20,
        "case_name": "Johnson v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "333 U.S. 10",
      "volume": "333",
      "reporter": "U.S.",
      "page": "10",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "68 S. Ct. 367",
        "volume": "68",
        "reporter": "S. Ct.",
        "page": "367",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 2d 436",
        "volume": "92",
        "reporter": "L. Ed. 2d",
        "page": "436",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 436",
        "volume": "92",
        "reporter": "L. Ed.",
        "page": "436",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1948 U.S. LEXIS 2583",
        "volume": "1948",
        "reporter": "U.S. LEXIS",
        "page": "2583",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "333 U.S. 10",
        "volume": "333",
        "reporter": "U.S.",
        "page": "10",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 S. Ct. 367",
        "volume": "68",
        "reporter": "S. Ct.",
        "page": "367",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 2d 436",
        "volume": "92",
        "reporter": "L. Ed. 2d",
        "page": "436",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1948 U.S. LEXIS 2583",
        "volume": "1948",
        "reporter": "U.S. LEXIS",
        "page": "2583",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 436",
        "volume": "92",
        "reporter": "L. Ed.",
        "page": "436",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "333 U.S. 10",
    "official_selection": {
      "court_class": "scotus",
      "selected": "333 U.S. 10",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-13",
      "page": null,
      "quote": "--- # Johnson v. United States *333 U.S. 10 (1948)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers, acting on an informant's tip, detected the distinctive odor of burning opium coming from a hotel room. Without a warrant, they knocked, entered when the occupant opened the door, arrested Johnson, and searched the room, finding opium and smoking apparatus. Johnson challenged the warrantless search. ## Issue Whether officers who have probable cause may conduct a warrantless search of a home or hotel room, or whether the probable-cause determination must instead be made by a neutral magistrate issuing a warrant. ## Rule The probable-cause inference must be drawn by a neutral magistrate, not the investigating officer.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-14",
      "page": null,
      "quote": "Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1948-02-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Johnson v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Hilton",
          "cluster_id": 10018723,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hilton",
          "cluster_id": 5144554,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Sorenson",
          "cluster_id": 4806437,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Charlotte Lynn Frazier And Andrea Parks",
          "cluster_id": 4538535,
          "cite": [
            "558 S.W.3d 145"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The People v. Sean Garvin",
          "cluster_id": 4436829,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Harte v. Board Comm'rs Cnty of Johnson",
          "cluster_id": 4411980,
          "cite": [
            "864 F.3d 1154",
            "2017 WL 3138494"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4409778,
          "cite": [
            "2017 COA 93"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amended July 5, 2017 State of Iowa v. Maurice D. Angel and Kemia B. McDowell",
          "cluster_id": 4471947,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Maurice D. Angel and Kemia B. McDowell",
          "cluster_id": 4384931,
          "cite": [
            "893 N.W.2d 904",
            "2017 WL 1422692",
            "2017 Iowa Sup. LEXIS 41"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Otis Sams, Jr. v. State of Indiana",
          "cluster_id": 4369368,
          "cite": [
            "71 N.E.3d 372",
            "2017 WL 677723",
            "2017 Ind. App. LEXIS 70"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
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
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pyon v. State",
          "cluster_id": 2791489,
          "cite": [
            "222 Md. App. 412",
            "112 A.3d 1130",
            "2015 Md. App. LEXIS 50"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
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
        "journal_ref": "Johnson v. United States:lane1_negative"
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
        "journal_ref": "Johnson v. United States:lane1_negative"
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
        "journal_ref": "Johnson v. United States:lane1_negative"
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
        "journal_ref": "Johnson v. United States:lane1_negative"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aguilar v. Texas",
          "cluster_id": 106865,
          "cite": [
            "12 L. Ed. 2d 723",
            "84 S. Ct. 1509",
            "378 U.S. 108",
            "1964 U.S. LEXIS 994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mendenhall",
          "cluster_id": 110264,
          "cite": [
            "64 L. Ed. 2d 497",
            "100 S. Ct. 1870",
            "446 U.S. 544",
            "1980 U.S. LEXIS 102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brinegar v. United States",
          "cluster_id": 104716,
          "cite": [
            "93 L. Ed. 2d 1879",
            "69 S. Ct. 1302",
            "338 U.S. 160",
            "1949 U.S. LEXIS 2084"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adams v. Williams",
          "cluster_id": 108571,
          "cite": [
            "32 L. Ed. 2d 612",
            "92 S. Ct. 1921",
            "407 U.S. 143",
            "1972 U.S. LEXIS 2206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ventresca",
          "cluster_id": 106990,
          "cite": [
            "13 L. Ed. 2d 684",
            "85 S. Ct. 741",
            "380 U.S. 102",
            "1965 U.S. LEXIS 2438",
            "16 A.F.T.R.2d (RIA) 5787"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Matlock",
          "cluster_id": 108967,
          "cite": [
            "39 L. Ed. 2d 242",
            "94 S. Ct. 988",
            "415 U.S. 164",
            "1974 U.S. LEXIS 8"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(104504) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzk0NDk2MDAwMDAwJnM9MjcwODgyNSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28104504%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 16,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 17,
        "triage_snippet_classified": 183
      },
      "lane2_top_cited": {
        "query": "cites:(104504)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMzk2JnM9MTExMzAxJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28104504%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(104504)",
        "reviewed": 39,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 39,
        "triage_read": 0,
        "triage_snippet_classified": 39
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(104504)",
    "indexed_citing_opinions": 2463,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 104504,
        "count": 2463,
        "count_source": "search"
      }
    ],
    "citation_count": 3856,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/johnson-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4MTA0Mzkmcz0xMDY4ODU2NyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28104504%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 104504,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 3994178,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 3998924,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 4001986,
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
    "date_created": "2026-07-05T08:55:56Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:56:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:56:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:59:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:56:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Johnson v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b89-11">
  Mr. Justice Jackson
 </author>
<p id="AnP">
  delivered the opinion of the Court.
 </p>
<p id="b89-12">
  Petitioner was convicted on four counts charging violation of federal narcotic laws.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The only question which brings the case here is whether it was lawful, without a warrant of any kind, to arrest petitioner and to search her living quarters.
 </p>
<p id="b90-5">
<span citation-index="1" class="star-pagination" label="12"> 
   *12
   </span>
  Taking the Government’s version of disputed events, decision would rest on these facts:
 </p>
<p id="b90-6">
  At about 7:30 p. m. Detective Lieutenant Belland, an officer of the Seattle police force narcotic detail, received information from a confidential informer, who was also a known narcotic user, that unknown persons were smoking opium in the Europe Hotel. The informer was taken back to the hotel to interview the manager, but he returned at once saying he could smell burning opium in the hallway. Belland communicated with federal narcotic agents and between 8:30 and 9 o’clock went back to the hotel with four such agents. All were experienced in narcotic work and recognized at once a strong odor of burning opium which to them was distinctive and unmistakable. The odor led to Room 1. The officers did not know who was occupying that room. They knocked and a voice inside asked who was there. “Lieutenant Bel-land,” was the reply. There was a slight delay, some “shuffling or noise” in the room and then the defendant opened the door. The officer said, “I want to talk to you a little bit.” She then, as he describes it, “stepped back acquiescently and admitted us.” He said, “I want to talk to you about this opium smell in the room here.” She denied that there was such a smell. Then he said, “I want you to consider yourself under arrest because we are going to search the room.” The search turned up incriminating opium and smoking apparatus, the latter being warm, apparently from recent use. This evidence the District Court refused to suppress before trial and admitted over defendant’s objection at the trial. Conviction resulted and the Circuit Court of Appeals affirmed.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b90-7">
  The defendant challenged the search of her home as a violation of the rights secured to her, in common with others, by the Fourth Amendment to the Constitution.
  <span citation-index="1" class="star-pagination" label="13"> 
   *13
   </span>
  The Government defends the search as legally justifiable, more particularly as incident to what it urges was a lawful arrest of the person.
 </p>
<p id="b91-5">
  I.
 </p>
<p id="b91-6">
  The Fourth Amendment to the Constitution of the United States provides:
 </p>
<blockquote id="b91-7">
  “The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”
 </blockquote>
<p id="b91-8">
  Entry to defendant’s living quarters, which was the beginning of the search, was demanded under color of office. It was granted in submission to authority rather than as an understanding and intentional waiver of a constitutional right. Cf.
  <em>
   Amos
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span>.
 </p>
<p id="b91-9">
  At the time entry was demanded the officers were possessed of evidence which a magistrate might have found to be probable cause for issuing a search warrant. We cannot sustain defendant’s contention, erroneously made, on the strength of
  <em>
   Taylor
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">286 U. S. 1</a></span>, that odors cannot be evidence sufficient to constitute probable grounds for any search. That decision held only that odors alone do not authorize a search without warrant. If the presence of odors is testified to before a magistrate and he finds the affiant qualified to know the odor, and it is one sufficiently distinctive to identify a forbidden substance, this Court has never held such a basis insufficient to justify issuance of a search warrant. Indeed it might very well be found to be evidence of most persuasive character.
 </p>
<p id="b91-10">
  The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law en
  <span citation-index="1" class="star-pagination" label="14"> 
   *14
   </span>
  forcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  Any assumption that evidence sufficient to support a magistrate’s disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people’s homes secure only in the discretion of police officers.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  Crime, even in the privacy of one’s own quarters, is, of course, of grave concern to society, and the law allows such crime to be reached on proper showing. The right of officers to thrust themselves into a home is also a grave concern, not only to the individual but to a society which chooses to dwell in reasonable security and freedom from surveillance. When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent.
 </p>
<p id="b92-4">
  There are exceptional circumstances in which, on balancing the need for effective law enforcement against the
  <span citation-index="1" class="star-pagination" label="15"> 
   *15
   </span>
  right of privacy, it may be contended that a magistrate’s warrant for search may be dispensed with. But this is not such a case. No reason is offered for not obtaining a search warrant except the inconvenience to the officers and some slight delay necessary to prepare papers and present the evidence to a magistrate. These are never very convincing reasons and, in these circumstances, certainly are not enough to by-pass the constitutional requirement. No suspect was fleeing or likely to take flight. The search was of permanent premises, not of a movable vehicle. No evidence or contraband was threatened with removal or destruction, except perhaps the fumes which we suppose in time would disappear. But they were not capable at any time of being reduced to possession for presentation to court. The evidence of their existence before the search was adequate and the testimony of the officers to that effect would not perish from the delay of getting a warrant.
 </p>
<p id="b93-5">
  If the officers in this case were excused from the constitutional duty of presenting their evidence to a magistrate, it is difficult to think of a case in which it should be required.
 </p>
<p id="b93-6">
  II.
 </p>
<p id="b93-7">
  The Government contends, however, that this search without warrant must be held valid because incident to an arrest. This alleged ground of validity requires examination of the facts to determine whether the arrest itself was lawful. Since it was without warrant, it could be valid only if for a crime committed in the presence of the arresting officer or for a felony of which he had reasonable cause to believe defendant guilty.
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
</p>
<p id="b94-5">
<span citation-index="1" class="star-pagination" label="16"> 
   *16
   </span>
  The Government, in effect, concedes that the arresting officer did not have probable cause to arrest petitioner until he had entered her room and found her to be the sole occupant.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
  It points out specifically, referring to the time just before entry, “For at that time the agents did not know whether there was one or several persons in the room. It was reasonable to believe that the room might have been an opium smoking den.” And it says, “. . . that when the agents were admitted into the room and found only petitioner present they had a reasonable basis for believing that she had been smoking opium and thus illicitly possessed the narcotic.” Thus the Government quite properly stakes the right to arrest, not on the informer’s tip and the smell the officers recognized before entry, but on the knowledge that she was alone in the room, gained only after, and wholly by reason of, their entry of her home. It was therefore their observations inside of her quarters, after they had obtained admission under color of their police authority, on which they made the arrest.
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
</p>
<p id="b94-6">
  Thus the Government is obliged to justify the arrest by the search and at the same time to justify the search by
  <span citation-index="1" class="star-pagination" label="17"> 
   *17
   </span>
  the arrest. This will not do. An officer gaining access to private living quarters under color of his office and of the law which he personifies must then have some valid basis in law for the intrusion. Any other rule would undermine “the right of the people to be secure in their persons, houses, papers, and effects,”
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
  and would obliterate one of the most fundamental distinctions between our form of government, where officers are under the law, and the police-state where they are the law.
 </p>
<p id="b95-5">
<em>
   Reversed.
  </em>
</p>
<judges id="b95-6">
  The Chief Justice, Mr. Justice Black, Mr. Justice Reed and Mr. Justice Burton dissent.
 </judges>








<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b89-13">
   Two counts charged violation of § 2553 (a) of the Internal Revenue Code (<span class="citation no-link">26 U. S. C. § 2553</span> (a)) and two counts charged violation of the Narcotic Drugs Import and Export Act as amended (<span class="citation no-link">21 U. S. C. §174</span>).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b90-8">
   <span class="citation" data-id="6896359"><a href="/opinion/6997439/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">162 F. 2d 562</a></span>.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b92-5">
   In
   <em>
    United States
   </em>
   v.
   <em>
    Lefkowitz,
   </em>
   <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#464" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 464</a></span>, this Court said:
  </p>
<blockquote id="b92-6">
   . . the informed and deliberate determinations of magistrates empowered to issue warrants as to what searches and seizures are permissible under the Constitution are to be preferred over the hurried action of officers and others who may happen to make arrests. Security against unlawful searches is more likely to be attained by resort to search warrants than by reliance upon the caution and sagacity of petty officers while acting under the excitement that attends the capture of persons accused of crime. . . .”
  </blockquote>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b92-7">
   “Belief, however well founded, that an article sought is concealed in a dwelling house furnishes no justification for a search of that place without a warrant. And such searches are held unlawful notwithstanding facts unquestionably showing probable cause.”
   <em>
    Agnello
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span>.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b93-8">
   This is the Washington law.
   <em>
    State
   </em>
   v.
   <em>
    Symes,
   </em>
   <span class="citation" data-id="4724347"><a href="/opinion/4917761/state-v-symes/" aria-description="Citation for case: State v. Symes">20 Wash. 484</a></span>, <span class="citation" data-id="4724347"><a href="/opinion/4917761/state-v-symes/" aria-description="Citation for case: State v. Symes">55 P. 626</a></span>;
   <em>
    State
   </em>
   v.
   <em>
    Lindsey,
   </em>
   <span class="citation" data-id="4001986"><a href="/opinion/4225695/state-v-lindsey/" aria-description="Citation for case: State v. Lindsey">192 Wash. 356</a></span>, <span class="citation" data-id="4001986"><a href="/opinion/4225695/state-v-lindsey/" aria-description="Citation for case: State v. Lindsey">73 P. 2d 738</a></span>;
   <em>
    State
   </em>
   v.
   <em>
    Krantz,
   </em>
   <span class="citation" data-id="3998924"><a href="/opinion/4223178/state-v-krantz/" aria-description="Citation for case: State v. Krantz">24 Wash. 2d 350</a></span>, <span class="citation" data-id="3998924"><a href="/opinion/4223178/state-v-krantz/" aria-description="Citation for case: State v. Krantz">164 P. 2d 453</a></span>;
   <em>
    State
   </em>
   v.
   <em>
    Robbins,
   </em>
   <span class="citation" data-id="3994178"><a href="/opinion/4219303/state-v-robbins/" aria-description="Citation for case: State v. Robbins">25 Wash. 2d 110</a></span>, <span class="citation" data-id="3994178"><a href="/opinion/4219303/state-v-robbins/" aria-description="Citation for case: State v. Robbins">169 P. 2d 246</a></span>. State law determines the validity of arrests without warrant.
   <em>
    United States
   </em>
   v.
   <em>
    Di Re,
   </em>
   <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/" aria-description="Citation for case: United States v. Di Re">332 U. S. 581</a></span>.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b94-7">
   The Government brief states that the question presented is “Whether there was probable cause for the arrest of petitioner for possessing opium prepared for smoking and the search of her room in a hotel incident thereto for the contraband opium, where experienced narcotic agents unmistakably detected and traced the pungent, identifiable odor of burning opium emanating from her room and knew, before they arrested her, that she was the only person in. the room.”
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b94-8">
   The Government also suggests that “In a sense, the arrest was made in ‘hot pursuit.’ . . .” However, we find no element of “hot pursuit” in the arrest of one who was not in flight, was completely surrounded by agents before she knew of their presence, who claims without denial that she was in bed at the time, and who made no attempt to escape. Nor would these facts seem to meet the requirements of the Washington “Uniform Law on Fresh Pursuit.” Session Laws 1943, ch. 261.
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b95-7">
   In
   <em>
    Gouled
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#304" aria-description="Citation for case: Gouled v. United States">255 U. S. 303, 304</a></span>, this Court said: “It would not be possible to add to the emphasis with which the framers of our Constitution and this court (in
   <em>
    Boyd
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U.S. 616</a></span>, in
   <em>
    Weeks
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, and in
   <em>
    Silver-thorne Lumber Co.
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>) have declared the importance to political liberty and to the welfare of our country of the due observance of the rights guaranteed under the Constitution by these two [Fourth and Fifth] Amendments. The effect of the decisions cited is: .that such rights are declared to be indispensable to the ‘full enjoyment of personal security, personal liberty and private property’; that they are to be regarded as of the very essence of constitutional liberty; and that the guaranty of them is as important and as imperative as are the guaranties of the other fundamental rights of the individual citizen, — the right, to trial by jury, to the writ of
   <em>
    habeas corpus
   </em>
   and to due process of law. It has been repeatedly decided that these Amendments should receive a liberal construction, so as to prevent stealthy encroachment upon or ‘gradual depreciation’ of the rights secured by them, by imperceptible practice of courts or by well-intentioned but mistakenly over-zealous executive officers.”
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Kansas v. Ventris.md  (`case`, 5 assertions)

### content_page

```
---
title: Kansas v. Ventris
type: case
citation: "556 U.S. 586 (2009)"
parallel_cite: "129 S. Ct. 1841; 173 L. Ed. 2d 801"
neutral_cite: 2009 U.S. LEXIS 3299
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-04-29
docket: No. 07-1356
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
  opinion_url: "https://www.courtlistener.com/opinion/145880/kansas-v-ventris/"
  cluster_id: 145880
  opinion_id: null
  identity_checked: true
lake:
  record_id: Kansas v. Ventris
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: Anchor
related:
  - "[[Sixth Amendment Right to Counsel]]"
  - "[[Massiah v. United States]]"
tags:
  - case
  - sixth-amendment
  - right-to-counsel
  - impeachment
  - jailhouse-informant
  - massiah
holding: "A statement obtained from a defendant in violation of the Sixth Amendment right to counsel — here, by a jailhouse informant — is inadmissible in the prosecution's case-in-chief but may be used to impeach the defendant's conflicting testimony if he takes the stand at trial."
aliases:
  - Kansas v. Ventris
  - "Kansas v. Ventris (2009)"
---

# Kansas v. Ventris

*556 U.S. 586 (2009)* (No. 07-1356) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 145880 → majority opinion 145880 (Scalia, J.; 556 U.S. 586, decided Apr. 29, 2009). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*594` precedes the holding paragraph, `*595` opens the dissent). S9 promotes. -->

## Background
Donnie Ray Ventris and a companion were charged with murder and aggravated robbery. Before trial, officers placed an informant in Ventris's holding cell, who elicited incriminating statements from him. At trial Ventris testified and placed the blame on his companion. The State conceded that the informant's statements had been obtained in violation of Ventris's Sixth Amendment right to counsel under *[[Massiah v. United States]]*, but it introduced them to impeach his testimony. The Kansas Supreme Court held the statements inadmissible for any purpose.

## Issue
Whether a statement taken from a defendant in violation of his Sixth Amendment right to counsel may be used to impeach his inconsistent testimony at trial.

## Rule
Analogizing to the impeachment exceptions the Court has recognized for other unlawfully obtained evidence, the Court held: "We hold that the informant's testimony, concededly elicited in violation of the Sixth Amendment, was admissible to challenge Ventris's inconsistent testimony at trial." — 556 U.S. at 594. ^pin-594

## Application
The Court reasoned that the Sixth Amendment violation was complete at the time of the uncounseled interrogation; suppression from the prosecution's case-in-chief is the remedy for that wrong. Excluding the statement even for impeachment would add little deterrence — officers gain little by planting an informant on the off chance the defendant later testifies inconsistently — while handing the defendant a shield behind which to commit perjury unchallenged. Weighing those interests as it had with evidence tainted under *[[Miranda v. Arizona|Miranda]]* and the Fourth Amendment, the Court allowed impeachment use.

## Conclusion
The judgment of the Kansas Supreme Court was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]]. Scalia, J., delivered the opinion of the Court; Stevens, J. (joined by Ginsburg, J.), dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Ventris* extends the **impeachment exception** (familiar from *[[Harris v. New York]]* and, for the Sixth Amendment, *Michigan v. Harvey*) to statements obtained through a *[[Massiah v. United States|Massiah]]* violation: barred from the case-in-chief, but usable to impeach a defendant who testifies inconsistently. Teach it as the counsel-clause counterpart to the *[[Miranda v. Arizona|Miranda]]* and Fourth Amendment impeachment rules.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Anchor*

## Sources
- [*Kansas v. Ventris*, 556 U.S. 586 (2009)](https://www.courtlistener.com/opinion/145880/kansas-v-ventris/) — pinpoint: 594 (Scalia, J., for the Court; the CL opinion text places the reporter star `*594` before the holding paragraph and `*595` at the start of the dissent, fixing the holding on 594). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "48bb6e36a36b14dc", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "556 U.S. 586 (2009)", "court": "U.S. Supreme Court", "neutral_cite": "2009 U.S. LEXIS 3299", "official_citation_present": true, "parallel_cite": "129 S. Ct. 1841; 173 L. Ed. 2d 801", "title": "Kansas v. Ventris", "year": "2009"}}
{"assertion_id": "7e1ac528cbb4f8e7", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A statement obtained from a defendant in violation of the Sixth Amendment right to counsel — here, by a jailhouse informant — is inadmissible in the prosecution's case-in-chief but may be used to impeach the defendant's conflicting testimony if he takes the stand at trial.", "title": "Kansas v. Ventris"}}
{"assertion_id": "b7cc18a1e75ca39d", "dimension": "support", "kind": "home_role", "locator": {"home": "Sixth Amendment Right to Counsel"}, "payload": {"home": "Sixth Amendment Right to Counsel", "role": "Anchor", "title": "Kansas v. Ventris"}}
{"assertion_id": "a7a7b7a6c9010d25", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Kansas v. Ventris", "varies_by_point": "false"}}
{"assertion_id": "c7a73ca510b894ed", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Kansas v. Ventris"}}
```

### lake record — Kansas v. Ventris

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kansas v. Ventris",
  "status": "under_review",
  "identity": {
    "case_name": "Kansas v. Ventris",
    "case_name_short": "Ventris",
    "case_name_full": "Kansas v. Ventris",
    "input_case_name": "Kansas v. Ventris",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-04-29",
    "year": 2009,
    "docket": "No. 07-1356",
    "cluster_id": 145880,
    "lead_opinion_id": 145880,
    "sibling_ids": [],
    "absolute_url": "/opinion/145880/kansas-v-ventris/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "556 U.S. 586",
      "volume": "556",
      "reporter": "U.S.",
      "page": "586",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "129 S. Ct. 1841",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "1841",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 801",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "801",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 3299",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "3299",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "556 U.S. 586",
        "volume": "556",
        "reporter": "U.S.",
        "page": "586",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 1841",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "1841",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 801",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "801",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 3299",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "3299",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "556 U.S. 586",
    "official_selection": {
      "court_class": "scotus",
      "selected": "556 U.S. 586",
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
    "date_created": "2026-07-06T13:45:04Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:45:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:45:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "kansas-v-ventris--145880",
      "to_record_id": "Kansas v. Ventris",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Kansas v. Ventris

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

                           KANSAS v. VENTRIS

         CERTIORARI TO THE SUPREME COURT OF KANSAS

    No. 07–1356. Argued January 21, 2009—Decided April 29, 2009
Respondent Donnie Ray Ventris and Rhonda Theel were charged with
  murder and other crimes. Prior to trial, an informant planted in
  Ventris’s cell heard him admit to shooting and robbing the victim, but
  Ventris testified at trial that Theel committed the crimes. When the
  State sought to call the informant to testify to his contradictory
  statement, Ventris objected. The State conceded that Ventris’s Sixth
  Amendment right to counsel had likely been violated, but argued that
  the statement was admissible for impeachment purposes. The trial
  court allowed the testimony. The jury convicted Ventris of aggra
  vated burglary and aggravated robbery. Reversing, the Kansas Su
  preme Court held that the informant’s statements were not admissi
  ble for any reason, including impeachment.
Held: Ventris’s statement to the informant, concededly elicited in viola
 tion of the Sixth Amendment, was admissible to impeach his incon
 sistent testimony at trial. Pp. 3–7.
    (a) Whether a confession that was not admissible in the prosecu
 tion’s case in chief nonetheless can be admitted for impeachment
 purposes depends on the nature of the constitutional guarantee vio
 lated. The Fifth Amendment guarantee against compelled self
 incrimination is violated by introducing a coerced confession at trial,
 whether by way of impeachment or otherwise. New Jersey v. Por
 tash, 440 U. S. 450, 458–459. But for the Fourth Amendment guar
 antee against unreasonable searches or seizures, where exclusion
 comes by way of deterrent sanction rather than to avoid violation of
 the substantive guarantee, admissibility is determined by an exclu
 sionary-rule balancing test. See Walder v. United States, 347 U. S.
 62, 65. The same is true for violations of the Fifth and Sixth
 Amendment prophylactic rules forbidding certain pretrial police con
 duct. See, e.g., Harris v. New York, 401 U. S. 222, 225–226. The core
2                          KANSAS v. VENTRIS

                                  Syllabus

    of the Sixth Amendment right to counsel is a trial right, but the right
    covers pretrial interrogations to ensure that police manipulation does
    not deprive the defendant of “ ‘effective representation by counsel at
    the only stage when legal aid and advice would help him.’ ” Massiah
    v. United States, 377 U. S. 201, 204. This right to be free of uncoun
    seled interrogation is infringed at the time of the interrogation, not
    when it is admitted into evidence. It is that deprivation that de
    mands the remedy of exclusion from the prosecution’s case in chief.
    Pp. 3–6.
       (b) The interests safeguarded by excluding tainted evidence for im
    peachment purposes are “outweighed by the need to prevent perjury
    and to assure the integrity of the trial process.” Stone v. Powell, 428
    U. S. 465, 488. Once the defendant testifies inconsistently, denying
    the prosecution “the traditional truth-testing devices of the adversary
    process,” Harris, supra, at 225, is a high price to pay for vindicating
    the right to counsel at the prior stage. On the other hand, preventing
    impeachment use of statements taken in violation of Massiah would
    add little appreciable deterrence for officers, who have an incentive to
    comply with the Constitution, since statements lawfully obtained can
    be used for all purposes, not simply impeachment. In every other
    context, this Court has held that tainted evidence is admissible for
    impeachment. See, e.g., Oregon v. Hass, 420 U. S. 714, 723. No dis
    tinction here alters that balance. Pp. 6–7.
285 Kan. 595, 176 P. 3d 920, reversed and remanded.

  SCALIA, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and KENNEDY, SOUTER, THOMAS, BREYER, and ALITO, JJ., joined.
STEVENS, J., filed a dissenting opinion, in which GINSBURG, J., joined.
                       Cite as: 556 U. S. ____ (2009)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 07–1356
                                  _________________


  KANSAS, PETITIONER v. DONNIE RAY VENTRIS
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                       KANSAS

                                [April 29, 2009] 


  JUSTICE SCALIA delivered the opinion of the Court.
  We address in this case the question whether a defen
dant’s incriminating statement to a jailhouse informant,
concededly elicited in violation of Sixth Amendment stric
tures, is admissible at trial to impeach the defendant’s
conflicting statement.
                             I
  In the early hours of January 7, 2004, after two days of
no sleep and some drug use, Rhonda Theel and respondent
Donnie Ray Ventris reached an ill-conceived agreement to
confront Ernest Hicks in his home. The couple testified
that the aim of the visit was simply to investigate rumors
that Hicks abused children, but the couple may have been
inspired by the potential for financial gain: Theel had
recently learned that Hicks carried large amounts of cash.
  The encounter did not end well. One or both of the pair
shot and killed Hicks with shots from a .38-caliber re
volver, and the companions drove off in Hicks’s truck with
approximately $300 of his money and his cell phone. On
receiving a tip from two friends of the couple who had
helped transport them to Hicks’s home, officers arrested
Ventris and Theel and charged them with various crimes,
2                    KANSAS v. VENTRIS

                     Opinion of the Court

chief among them murder and aggravated robbery. The
State dropped the murder charge against Theel in ex
change for her guilty plea to the robbery charge and her
testimony identifying Ventris as the shooter.
   Prior to trial, officers planted an informant in Ventris’s
holding cell, instructing him to “keep [his] ear open and
listen” for incriminating statements. App. 146. According
to the informant, in response to his statement that Ventris
appeared to have “something more serious weighing in on
his mind,” Ventris divulged that “[h]e’d shot this man in
his head and in his chest” and taken “his keys, his wallet,
about $350.00, and . . . a vehicle.” Id., at 154, 150.
   At trial, Ventris took the stand and blamed the robbery
and shooting entirely on Theel. The government sought to
call the informant, to testify to Ventris’s prior contradic
tory statement; Ventris objected. The State conceded that
there was “probably a violation” of Ventris’s Sixth
Amendment right to counsel but nonetheless argued that
the statement was admissible for impeachment purposes
because the violation “doesn’t give the Defendant . . . a
license to just get on the stand and lie.” Id., at 143. The
trial court agreed and allowed the informant’s testimony,
but instructed the jury to “consider with caution” all tes
timony given in exchange for benefits from the State. Id.,
at 30. The jury ultimately acquitted Ventris of felony
murder and misdemeanor theft but returned a guilty
verdict on the aggravated burglary and aggravated rob
bery counts.
   The Kansas Supreme Court reversed the conviction,
holding that “[o]nce a criminal prosecution has com
menced, the defendant’s statements made to an under
cover informant surreptitiously acting as an agent for the
State are not admissible at trial for any reason, including
the impeachment of the defendant’s testimony.” 285 Kan.
595, 606, 176 P. 3d 920, 928 (2008).            Chief Justice
McFarland dissented, id., at 611, 176 P. 3d, at 930. We
                 Cite as: 556 U. S. ____ (2009)            3

                     Opinion of the Court

granted the State’s petition for certiorari, 554 U. S. ___
(2008).
                              II
   The Sixth Amendment, applied to the States through
the Fourteenth Amendment, guarantees that “[i]n all
criminal prosecutions, the accused shall . . . have the
Assistance of Counsel for his defence.” The core of this
right has historically been, and remains today, “the oppor
tunity for a defendant to consult with an attorney and to
have him investigate the case and prepare a defense for
trial.” Michigan v. Harvey, 494 U. S. 344, 348 (1990). We
have held, however, that the right extends to having
counsel present at various pretrial “critical” interactions
between the defendant and the State, United States v.
Wade, 388 U. S. 218, 224 (1967), including the deliberate
elicitation by law enforcement officers (and their agents) of
statements pertaining to the charge, Massiah v. United
States, 377 U. S. 201, 206 (1964). The State has conceded
throughout these proceedings that Ventris’s confession
was taken in violation of Massiah’s dictates and was
therefore not admissible in the prosecution’s case in chief.
Without affirming that this concession was necessary, see
Kuhlmann v. Wilson, 477 U. S. 436, 459–460 (1986), we
accept it as the law of the case. The only question we
answer today is whether the State must bear the addi
tional consequence of inability to counter Ventris’s contra
dictory testimony by placing the informant on the stand.
                            A
  Whether otherwise excluded evidence can be admitted
for purposes of impeachment depends upon the nature of
the constitutional guarantee that is violated. Sometimes
that explicitly mandates exclusion from trial, and some
times it does not. The Fifth Amendment guarantees that
no person shall be compelled to give evidence against
himself, and so is violated whenever a truly coerced con
4                    KANSAS v. VENTRIS

                     Opinion of the Court

fession is introduced at trial, whether by way of impeach
ment or otherwise. New Jersey v. Portash, 440 U. S. 450,
458–459 (1979). The Fourth Amendment, on the other
hand, guarantees that no person shall be subjected to
unreasonable searches or seizures, and says nothing about
excluding their fruits from evidence; exclusion comes by
way of deterrent sanction rather than to avoid violation of
the substantive guarantee. Inadmissibility has not been
automatic, therefore, but we have instead applied an
exclusionary-rule balancing test. See Walder v. United
States, 347 U. S. 62, 65 (1954). The same is true for viola
tions of the Fifth and Sixth Amendment prophylactic rules
forbidding certain pretrial police conduct. See Harris v.
New York, 401 U. S. 222, 225–226 (1971); Harvey, supra,
at 348–350.
    Respondent argues that the Sixth Amendment’s right to
counsel is a “right an accused is to enjoy a[t] trial.” Brief
for Respondent 11. The core of the right to counsel is
indeed a trial right, ensuring that the prosecution’s case is
subjected to “the crucible of meaningful adversarial test
ing.” United States v. Cronic, 466 U. S. 648, 656 (1984).
See also Powell v. Alabama, 287 U. S. 45, 57–58 (1932).
But our opinions under the Sixth Amendment, as under
the Fifth, have held that the right covers pretrial interro
gations to ensure that police manipulation does not render
counsel entirely impotent—depriving the defendant of
“ ‘effective representation by counsel at the only stage
when legal aid and advice would help him.’ ” Massiah,
supra, at 204 (quoting Spano v. New York, 360 U. S. 315,
326 (1959) (Douglas, J., concurring)). See also Miranda v.
Arizona, 384 U. S. 436, 468–469 (1966).
    Our opinion in Massiah, to be sure, was equivocal on
what precisely constituted the violation. It quoted various
authorities indicating that the violation occurred at the
moment of the postindictment interrogation because such
questioning “ ‘contravenes the basic dictates of fairness in
                  Cite as: 556 U. S. ____ (2009)            5

                      Opinion of the Court

the conduct of criminal causes.’ ” 377 U. S., at 205 (quot
ing People v. Waterman, 9 N. Y. 2d 561, 565, 175 N. E. 2d
445, 448 (1961)). But the opinion later suggested that the
violation occurred only when the improperly obtained
evidence was “used against [the defendant] at his trial.”
377 U. S., at 206–207. That question was irrelevant to the
decision in Massiah in any event. Now that we are con
fronted with the question, we conclude that the Massiah
right is a right to be free of uncounseled interrogation, and
is infringed at the time of the interrogation. That, we
think, is when the “Assistance of Counsel” is denied.
   It is illogical to say that the right is not violated until
trial counsel’s task of opposing conviction has been un
dermined by the statement’s admission into evidence. A
defendant is not denied counsel merely because the prose
cution has been permitted to introduce evidence of guilt—
even evidence so overwhelming that the attorney’s job of
gaining an acquittal is rendered impossible. In such
circumstances the accused continues to enjoy the assis
tance of counsel; the assistance is simply not worth much.
The assistance of counsel has been denied, however, at the
prior critical stage which produced the inculpatory evi
dence. Our cases acknowledge that reality in holding that
the stringency of the warnings necessary for a waiver of
the assistance of counsel varies according to “the useful
ness of counsel to the accused at the particular [pretrial]
proceeding.” Patterson v. Illinois, 487 U. S. 285, 298
(1988). It is that deprivation which demands a remedy.
   The United States insists that “post-charge deliberate
elicitation of statements without the defendant’s counsel
or a valid waiver of counsel is not intrinsically unlawful.”
Brief for United States as Amicus Curiae 17, n. 4. That is
true when the questioning is unrelated to charged
crimes—the Sixth Amendment right is “offense specific,”
McNeil v. Wisconsin, 501 U. S. 171, 175 (1991). We have
never said, however, that officers may badger counseled
6                    KANSAS v. VENTRIS

                     Opinion of the Court

defendants about charged crimes so long as they do not
use information they gain. The constitutional violation
occurs when the uncounseled interrogation is conducted.
                              B
   This case does not involve, therefore, the prevention of a
constitutional violation, but rather the scope of the remedy
for a violation that has already occurred. Our precedents
make clear that the game of excluding tainted evidence for
impeachment purposes is not worth the candle. The inter
ests safeguarded by such exclusion are “outweighed by the
need to prevent perjury and to assure the integrity of the
trial process.” Stone v. Powell, 428 U. S. 465, 488 (1976).
“It is one thing to say that the Government cannot make
an affirmative use of evidence unlawfully obtained. It is
quite another to say that the defendant can . . . provide
himself with a shield against contradiction of his un
truths.” Walder, supra, at 65. Once the defendant testi
fies in a way that contradicts prior statements, denying
the prosecution use of “the traditional truth-testing de
vices of the adversary process,” Harris, supra, at 225, is a
high price to pay for vindication of the right to counsel at
the prior stage.
   On the other side of the scale, preventing impeachment
use of statements taken in violation of Massiah would add
little appreciable deterrence. Officers have significant
incentive to ensure that they and their informants comply
with the Constitution’s demands, since statements law
fully obtained can be used for all purposes rather than
simply for impeachment. And the ex ante probability that
evidence gained in violation of Massiah would be of use for
impeachment is exceedingly small. An investigator would
have to anticipate both that the defendant would choose to
testify at trial (an unusual occurrence to begin with) and
that he would testify inconsistently despite the admissibil
ity of his prior statement for impeachment. Not likely to
                     Cite as: 556 U. S. ____ (2009)                   7

                         Opinion of the Court

happen—or at least not likely enough to risk squandering
the opportunity of using a properly obtained statement for
the prosecution’s case in chief.
   In any event, even if “the officer may be said to have
little to lose and perhaps something to gain by way of
possibly uncovering impeachment material,” we have
multiple times rejected the argument that this “specula
tive possibility” can trump the costs of allowing perjurious
statements to go unchallenged. Oregon v. Hass, 420 U. S.
714, 723 (1975). We have held in every other context that
tainted evidence—evidence whose very introduction does
not constitute the constitutional violation, but whose
obtaining was constitutionally invalid—is admissible for
impeachment. See ibid.; Walder, 347 U. S., at 65; Harris,
401 U. S., at 226; Harvey, 494 U. S., at 348. We see no
distinction that would alter the balance here.*
                         *    *    *
   We hold that the informant’s testimony, concededly
elicited in violation of the Sixth Amendment, was admis
sible to challenge Ventris’s inconsistent testimony at trial.
The judgment of the Kansas Supreme Court is reversed,
and the case is remanded for further proceedings not
inconsistent with this opinion.
                                             It is so ordered.
——————
  * Respondent’s amicus insists that jailhouse snitches are so inher
ently unreliable that this Court should craft a broader exclusionary
rule for uncorroborated statements obtained by that means. Brief for
National Association of Criminal Defense Lawyers 25–26. Our legal
system, however, is built on the premise that it is the province of the
jury to weigh the credibility of competing witnesses, and we have long
purported to avoid “establish[ing] this Court as a rule-making organ for
the promulgation of state rules of criminal procedure.” Spencer v.
Texas, 385 U. S. 554, 564 (1967). It would be especially inappropriate
to fabricate such a rule in this case, where it appears the jury took to
heart the trial judge’s cautionary instruction on the unreliability of
rewarded informant testimony by acquitting Ventris of felony murder.
                      Cite as: 556 U. S. ____ (2009)       1

                         STEVENS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                               _________________

                               No. 07–1356
                               _________________


   KANSAS, PETITIONER v. DONNIE RAY VENTRIS
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                       KANSAS

                             [April 29, 2009] 


   JUSTICE STEVENS, with whom JUSTICE GINSBURG joins,
dissenting.
   In Michigan v. Harvey, 494 U. S. 344 (1990), the Court
held that a statement obtained from a defendant in viola
tion of the Sixth Amendment could be used to impeach his
testimony at trial. As I explained in a dissent joined by
three other Members of the Court, that holding eroded the
principle that “those who are entrusted with the power of
government have the same duty to respect and obey the
law as the ordinary citizen.” Id., at 369. It was my view
then, as it is now, that “the Sixth Amendment is violated
when the fruits of the State’s impermissible encounter
with the represented defendant are used for impeachment
just as it is when the fruits are used in the prosecutor’s
case in chief.” Id., at 355.
   In this case, the State has conceded that it violated the
Sixth Amendment as interpreted in Massiah v. United
States, 377 U. S. 201, 206 (1964), when it used a jailhouse
informant to elicit a statement from the defendant. No
Miranda warnings were given to the defendant,1 nor was
he otherwise alerted to the fact that he was speaking to a
state agent. Even though the jury apparently did not
credit the informant’s testimony, the Kansas Supreme
Court correctly concluded that the prosecution should not
——————
 1 See   Miranda v. Arizona, 384 U. S. 436 (1966).
2                    KANSAS v. VENTRIS

                     STEVENS, J., dissenting

be allowed to exploit its pretrial constitutional violation
during the trial itself. The Kansas Court’s judgment
should be affirmed.
   This Court’s contrary holding relies on the view that a
defendant’s pretrial right to counsel is merely “prophylac
tic” in nature. See ante, at 4. The majority argues that
any violation of this prophylactic right occurs solely at the
time the State subjects a counseled defendant to an un
counseled interrogation, not when the fruits of the encoun
ter are used against the defendant at trial. Ante, at 5.
This reasoning is deeply flawed.
   The pretrial right to counsel is not ancillary to, or of
lesser importance than, the right to rely on counsel at
trial. The Sixth Amendment grants the right to counsel
“[i]n all criminal prosecutions,” and we have long recog
nized that the right applies in periods before trial com
mences, see United States v. Wade, 388 U. S. 218, 224
(1967). We have never endorsed the notion that the pre
trial right to counsel stands at the periphery of the Sixth
Amendment. To the contrary, we have explained that the
pretrial period is “perhaps the most critical period of the
proceedings” during which a defendant “requires the
guiding hand of counsel.” Powell v. Alabama, 287 U. S.
45, 57, 69 (1932); see Maine v. Moulton, 474 U. S. 159, 176
(1985) (recognizing the defendant’s “right to rely on coun
sel as a ‘medium’ between him and the State” in all critical
stages of prosecution). Placing the prophylactic label on a
core Sixth Amendment right mischaracterizes the sweep
of the constitutional guarantee.
   Treating the State’s actions in this case as a violation of
a prophylactic right, the Court concludes that introducing
the illegally obtained evidence at trial does not itself
violate the Constitution. I strongly disagree. While the
constitutional breach began at the time of interrogation,
the State’s use of that evidence at trial compounded the
violation. The logic that compels the exclusion of the
                      Cite as: 556 U. S. ____ (2009)                     3

                         STEVENS, J., dissenting

evidence during the State’s case in chief extends to any
attempt by the State to rely on the evidence, even for
impeachment. The use of ill-gotten evidence during any
phase of criminal prosecution does damage to the adver
sarial process—the fairness of which the Sixth Amend
ment was designed to protect. See Strickland v. Washing
ton, 466 U. S. 668, 685 (1984); see also Adams v. United
States ex rel. McCann, 317 U. S. 269, 276 (1942) (“[The]
procedural devices rooted in experience were written into
the Bill of Rights not as abstract rubrics in an elegant code
but in order to assure fairness and justice before any
person could be deprived of ‘life, liberty, or property’ ”).
   When counsel is excluded from a critical pretrial inter
action between the defendant and the State, she may be
unable to effectively counter the potentially devastating,
and potentially false,2 evidence subsequently introduced at
trial. Inexplicably, today’s Court refuses to recognize that
this is a constitutional harm.3 Yet in Massiah, the Court
forcefully explained that a defendant is “denied the basic
protections of the [Sixth Amendment] guarantee when
there [is] used against him at his trial evidence of his own
incriminating words” that were “deliberately elicited from

——————
  2 The likelihood that evidence gathered by self-interested jailhouse

informants may be false cannot be ignored. See generally Brief for
National Association of Criminal Defense Lawyers as Amicus Curiae.
Indeed, by deciding to acquit respondent of felony murder, the jury
seems to have dismissed the informant’s trial testimony as unreliable.
  3 In the majority’s telling, “simply” having counsel whose help is “not

worth much” is not a Sixth Amendment concern. Ante, at 5. Of course,
the Court points to no precedent for this stingy view of the Counsel
Clause, for we have never held that the Sixth Amendment only protects
a defendant from actual denials of counsel. Indeed our venerable
ineffective-assistance-of-counsel jurisprudence is built on a more
realistic understanding of what the Constitution guarantees. See
Strickland v. Washington, 466 U. S. 668 (1984); McMann v. Richard
son, 397 U. S. 759, 771, n. 14 (1970) (“[T]he right to counsel is the right
to the effective assistance of counsel”).
4                    KANSAS v. VENTRIS

                     STEVENS, J., dissenting

him after he had been indicted and in the absence of coun
sel.” 377 U. S., at 206. Sadly, the majority has retreated
from this robust understanding of the right to counsel.
   Today’s decision is lamentable not only because of its
flawed underpinnings, but also because it is another occa
sion in which the Court has privileged the prosecution at
the expense of the Constitution. Permitting the State to
cut corners in criminal proceedings taxes the legitimacy of
the entire criminal process. “The State’s interest in truth
seeking is congruent with the defendant’s interest in
representation by counsel, for it is an elementary premise
of our system of criminal justice ‘that partisan advocacy on
both sides of a case will best promote the ultimate objec
tive that the guilty be convicted and the innocent go free.’ ”
Harvey, 494 U. S., at 357 (STEVENS, J., dissenting) (quot
ing United States v. Cronic, 466 U. S. 648, 655 (1984)).
Although the Court may not be concerned with the use of
ill-gotten evidence in derogation of the right to counsel, I
remain convinced that such shabby tactics are intolerable
in all cases. I respectfully dissent.

```

---

## GROUP: content/cases/Katz v. United States.md  (`case`, 7 assertions)

### content_page

```
---
title: "Katz v. United States"
type: case
citation: "389 U.S. 347 (1967)"
parallel_cite: "88 S. Ct. 507; 19 L. Ed. 2d 576"
neutral_cite: 1967 U.S. LEXIS 2
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-12-18
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-12-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Katz v. United States
  varies_by_point: false
  scope_note: "Katz's reasonable-expectation-of-privacy framework remains the governing search test; the trespass theory it displaced was later revived as an additional (not exclusive) basis in United States v. Jones (2012) and Carpenter (2018) without disturbing Katz."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107564/katz-v-united-states/"
  cluster_id: 107564
  opinion_id: 9423552
  identity_checked: true
homes:
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Key — Anchor"
  - page: "[[Standing to Challenge a Search]]"
    role: "Related (cross-doctrine)"
  - page: "[[Electronic Surveillance and Title III]]"
    role: "Key — cross-ref (overruled Olmstead; wiretap is a search)"
related: ["[[United States v. Jones]]", "[[Carpenter v. United States]]", "[[Rakas v. Illinois]]", "[[Smith v. Maryland]]"]
aliases: []
tags: ["case", "fourth-amendment", "reasonable-expectation-of-privacy", "search", "standing"]
holding: "Electronic eavesdropping that invades a justified expectation of privacy is a search even with no physical trespass; overruled…"
lake:
  record_id: Katz v. United States
  status: verified
  projected_at: 2026-07-06
---

# Katz v. United States

*389 U.S. 347 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
FBI agents attached an electronic listening-and-recording device to the outside of a public telephone booth from which Katz placed wagering calls, and used the recordings of his end of the conversations to convict him of transmitting wagering information. There was no physical penetration of the booth.

## Issue
Whether Fourth Amendment protection turns on intrusion into a "constitutionally protected area," and whether electronic eavesdropping on a conversation in a public phone booth, accomplished without any physical trespass, is a search and seizure subject to the Amendment.

## Rule
The inquiry is personal, not spatial: "the Fourth Amendment protects people, not places. What a person knowingly exposes to the public, even in his own home or office, is not a subject of Fourth Amendment protection. . . . But what he seeks to preserve as private, even in an area accessible to the public, may be constitutionally protected." — 389 U.S. at 351. ^pin-351

Justice Harlan's [[Common Legal Terms#concurring-opinion|concurrence]] supplied the now-governing test: there is "a twofold requirement, first that a person have exhibited an actual (subjective) expectation of privacy and, second, that the expectation be one that society is prepared to recognize as 'reasonable.'" — *Id.* at 361 (Harlan, J., concurring). ^pin-361

## Application
Katz justifiably relied on the privacy of the closed telephone booth when he placed his calls; he sought to exclude "the uninvited ear," not the eye. The government's electronic monitoring of his conversation violated that privacy upon which he justifiably relied and thus constituted a search and seizure, even though it involved no physical trespass into the booth. Because the agents acted without a warrant, the surveillance was unreasonable on these facts.

## Conclusion
The warrantless electronic eavesdropping violated the Fourth Amendment; the conviction was reversed. Fourth Amendment coverage follows the person's justified expectation of privacy, not the presence of a physical trespass.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Katz* displaced the trespass-based rule of *[[Olmstead v. United States|Olmstead]]* and *Goldman*. Its reasonable-expectation-of-privacy test remains the central search standard and is the conceptual anchor for modern standing analysis ([[Rakas v. Illinois]]: standing turns on the defendant's **own** legitimate expectation of privacy).
- The property/trespass approach was later **revived as an additional, alternative basis** (not a replacement) in [[United States v. Jones]] (2012) and [[Carpenter v. United States]] (2018), leaving *Katz* intact.

## Appears on
- [[Reasonable Expectation of Privacy]] — *Key — Anchor*
- [[Standing to Challenge a Search]] — *Related (cross-doctrine)*
- [[Electronic Surveillance and Title III]] — *Key — cross-ref (overruled Olmstead; wiretap is a search)*

## Sources
- *Katz v. United States*, 389 U.S. 347 (1967) — https://www.courtlistener.com/opinion/107564/katz-v-united-states/ — pinpoints: 351, 361 (Harlan, J., concurring).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0305e93c4887584d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "389 U.S. 347 (1967)", "court": "U.S. Supreme Court", "neutral_cite": "1967 U.S. LEXIS 2", "official_citation_present": true, "parallel_cite": "88 S. Ct. 507; 19 L. Ed. 2d 576", "title": "Katz v. United States", "year": "1967"}}
{"assertion_id": "327ca137487941a0", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Electronic eavesdropping that invades a justified expectation of privacy is a search even with no physical trespass; overruled…", "title": "Katz v. United States"}}
{"assertion_id": "57027ff0271c5aff", "dimension": "support", "kind": "home_role", "locator": {"home": "Electronic Surveillance and Title III"}, "payload": {"home": "Electronic Surveillance and Title III", "role": "Key — cross-ref (overruled Olmstead; wiretap is a search)", "title": "Katz v. United States"}}
{"assertion_id": "729679e1e7688593", "dimension": "support", "kind": "home_role", "locator": {"home": "Standing to Challenge a Search"}, "payload": {"home": "Standing to Challenge a Search", "role": "Related (cross-doctrine)", "title": "Katz v. United States"}}
{"assertion_id": "ad5f3fb4fabf8363", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Key — Anchor", "title": "Katz v. United States"}}
{"assertion_id": "6d527a8a4e314861", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Katz v. United States"}}
{"assertion_id": "d34c2c05728b86cf", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1967-12-18", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Katz v. United States", "field_i_validity": "good_law", "scope_note": "Katz's reasonable-expectation-of-privacy framework remains the governing search test; the trespass theory it displaced was later revived as an additional (not exclusive) basis in United States v. Jones (2012) and Carpenter (2018) without disturbing Katz.", "title": "Katz v. United States", "varies_by_point": "false"}}
```

### lake record — Katz v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Katz v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Katz v. United States",
    "case_name_short": "Katz",
    "case_name_full": "Katz v. United States",
    "input_case_name": "Katz v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-12-18",
    "year": 1967,
    "docket": null,
    "cluster_id": 107564,
    "lead_opinion_id": 9423552,
    "sibling_ids": [
      107564,
      9423552,
      9423553,
      9423554,
      9423555,
      9423556
    ],
    "absolute_url": "/opinion/107564/katz-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8968016,
        "score": 20,
        "case_name": "Katz v. United States"
      },
      {
        "cluster_id": 107431,
        "score": 20,
        "case_name": "Katz v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "389 U.S. 347",
      "volume": "389",
      "reporter": "U.S.",
      "page": "347",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 507",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "507",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "19 L. Ed. 2d 576",
        "volume": "19",
        "reporter": "L. Ed. 2d",
        "page": "576",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 2",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "389 U.S. 347",
        "volume": "389",
        "reporter": "U.S.",
        "page": "347",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 507",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "507",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "19 L. Ed. 2d 576",
        "volume": "19",
        "reporter": "L. Ed. 2d",
        "page": "576",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 2",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "389 U.S. 347",
    "official_selection": {
      "court_class": "scotus",
      "selected": "389 U.S. 347",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-351",
      "page": null,
      "quote": "and whether electronic eavesdropping on a conversation in a public phone booth, accomplished without any physical trespass, is a search and seizure subject to the Amendment. ## Rule The inquiry is personal, not spatial:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-361",
      "page": null,
      "quote": "a twofold requirement, first that a person have exhibited an actual (subjective) expectation of privacy and, second, that the expectation be one that society is prepared to recognize as 'reasonable.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-12-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Katz v. United States",
    "varies_by_point": false,
    "scope_note": "Katz's reasonable-expectation-of-privacy framework remains the governing search test; the trespass theory it displaced was later revived as an additional (not exclusive) basis in United States v. Jones (2012) and Carpenter (2018) without disturbing Katz.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "People v. Dozier",
          "cluster_id": 10746140,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Katz v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 10740496,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Katz v. United States:lane1_negative"
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
        "journal_ref": "Katz v. United States:lane1_negative"
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
        "journal_ref": "Katz v. United States:lane1_negative"
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
        "journal_ref": "Katz v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Lepage",
          "cluster_id": 9503197,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Katz v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jordan",
          "cluster_id": 9487045,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Katz v. United States:lane1_negative"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harlow v. Fitzgerald",
          "cluster_id": 110763,
          "cite": [
            "73 L. Ed. 2d 396",
            "102 S. Ct. 2727",
            "457 U.S. 800",
            "1982 U.S. LEXIS 139"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bell v. Wolfish",
          "cluster_id": 110075,
          "cite": [
            "60 L. Ed. 2d 447",
            "99 S. Ct. 1861",
            "441 U.S. 520",
            "1979 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mitchell v. Forsyth",
          "cluster_id": 111481,
          "cite": [
            "86 L. Ed. 2d 411",
            "105 S. Ct. 2806",
            "472 U.S. 511",
            "1985 U.S. LEXIS 113",
            "53 U.S.L.W. 4798",
            "2 Fed. R. Serv. 3d 221"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mendenhall",
          "cluster_id": 110264,
          "cite": [
            "64 L. Ed. 2d 497",
            "100 S. Ct. 1870",
            "446 U.S. 544",
            "1980 U.S. LEXIS 102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roe v. Wade",
          "cluster_id": 108713,
          "cite": [
            "35 L. Ed. 2d 147",
            "93 S. Ct. 705",
            "410 U.S. 113",
            "1973 U.S. LEXIS 159"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kimmelman v. Morrison",
          "cluster_id": 111724,
          "cite": [
            "91 L. Ed. 2d 305",
            "106 S. Ct. 2574",
            "477 U.S. 365",
            "1986 U.S. LEXIS 63",
            "54 U.S.L.W. 4789"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane2_top_cited"
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
        "journal_ref": "Katz v. United States:lane3_recency"
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
        "journal_ref": "Katz v. United States:lane3_recency"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107564 OR 9423552 OR 9423553 OR 9423554 OR 9423555 OR 9423556) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzAyNTk4NDAwMDAwJnM9OTQ1MjU5OCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107564+OR+9423552+OR+9423553+OR+9423554+OR+9423555+OR+9423556%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(107564 OR 9423552 OR 9423553 OR 9423554 OR 9423555 OR 9423556)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMzA2JnM9MTEwMTE4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107564+OR+9423552+OR+9423553+OR+9423554+OR+9423555+OR+9423556%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107564 OR 9423552 OR 9423553 OR 9423554 OR 9423555 OR 9423556)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzE0NjA4MDAwMDAwJnM9OTQ5ODg1OCZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107564+OR+9423552+OR+9423553+OR+9423554+OR+9423555+OR+9423556%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107564 OR 9423552 OR 9423553 OR 9423554 OR 9423555 OR 9423556)",
    "indexed_citing_opinions": 8405,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107564,
        "count": 7414,
        "count_source": "search"
      },
      {
        "opinion_id": 9423552,
        "count": 1162,
        "count_source": "search"
      },
      {
        "opinion_id": 9423553,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423554,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423555,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423556,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 13311,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/katz-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0ODYzNDQmcz0xMDY1MTUyOCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28107564+OR+9423552+OR+9423553+OR+9423554+OR+9423555+OR+9423556%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9423554,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423554,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423554,
        "cited_id": 101320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423554,
        "cited_id": 103664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423554,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423554,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423554,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423554,
        "cited_id": 107319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423554,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 101320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 103664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 104314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 104623,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 104917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 105746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 105848,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 106146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 107312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 107319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 107325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 268411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 273830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 1455097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 1497017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423552,
        "cited_id": 1748896,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 101320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 103664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 104314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 104623,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 104917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 105021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 105746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 105848,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 106146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 107312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 107319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 107325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 268411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 273830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 1455097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 1497017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 1748896,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 9423307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107564,
        "cited_id": 9423552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423555,
        "cited_id": 105021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423555,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423555,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423555,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423555,
        "cited_id": 9423307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423556,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423556,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423556,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423556,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423556,
        "cited_id": 101320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423556,
        "cited_id": 103664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423556,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423556,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423556,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423556,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423556,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423556,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423556,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423556,
        "cited_id": 9420337,
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
    "date_created": "2026-07-05T09:08:01Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T09:08:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T09:08:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T09:12:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T09:08:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Katz v. United States

```
<opinion type="majority">
<author id="b458-6">Mr. Justice Stewart</author>
<p id="A9Y">delivered the opinion of the Court.</p>
<p id="b458-7">The petitioner was convicted in the District Court for the Southern District of California under an eight-count indictment charging him with transmitting wagering information by telephone from Los Angeles to Miami and Boston, in violation of a federal statute.<footnotemark>1</footnotemark> At trial the Government was permitted, over the petitioner’s objection, to introduce evidence of the petitioner’s end of telephone conversations, overheard by FBI agents who had attached an electronic listening and recording device to the outside of the public telephone booth from which he had placed his calls. In affirming his conviction, the Court of Appeals rejected the contention that the recordings had been obtained in violation of the Fourth Amend<page-number citation-index="1" label="349">*349</page-number>ment, because “[tjhere was no physical entrance into the area occupied by [the petitioner].”<footnotemark>2</footnotemark> We granted certiorari in order to consider the constitutional questions thus presented.<footnotemark>3</footnotemark></p>
<p id="b459-5">The petitioner has phrased those questions as follows:</p>
<blockquote id="b459-6">“A. Whether a public telephone booth is a constitutionally protected area so that evidence obtained by attaching an electronic listening recording device to the top of such a booth is obtained in violation of the right to privacy of the user of the booth.</blockquote>
<blockquote id="b460-5"><page-number citation-index="1" label="350">*350</page-number>“B. Whether physical penetration of a constitutionally protected area is necessary before a search and seizure can be said to be violative of the Fourth Amendment to the United States Constitution.”</blockquote>
<p id="b460-6">We decline to adopt this formulation of the issues. In the first place, the correct solution of Fourth Amendment problems is not necessarily promoted by incantation of the phrase “constitutionally protected area.” Secondly, the Fourth Amendment cannot be translated into a general constitutional “right to privacy.” That Amendment protects individual privacy against certain kinds of governmental intrusion, but its protections go further, and often have nothing to do with privacy at all.<footnotemark>4</footnotemark> Other provisions of the Constitution protect personal privacy from other forms of governmental invasion.<footnotemark>5</footnotemark> But the protection of a person’s <em>general </em>right to privacy— his right to be let alone by other people<footnotemark>6</footnotemark> — is, like the <page-number citation-index="1" label="351">*351</page-number>protection of his property and of his very life, left largely to the law of the individual States.<footnotemark>7</footnotemark></p>
<p id="b461-5">Because of the misleading way the issues have been formulated, the parties have attached great significance to the characterization of the telephone booth from which the petitioner placed his calls. The petitioner has strenuously argued that the booth was a “constitutionally protected area.” The Government has maintained with equal vigor that it was not.<footnotemark>8</footnotemark> But this effort to decide whether or not a given “area,” viewed in the abstract, is “constitutionally protected” deflects attention from the problem presented by this case.<footnotemark>9</footnotemark> For the Fourth Amendment protects people, not places. What a person knowingly exposes to the public, even in his own home or office, is not a subject of Fourth Amendment protection. See <em>Lewis </em>v. <em>United States, </em><span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/#210" aria-description="Citation for case: Lewis v. United States">385 U. S. 206, 210</a></span>; <em>United States </em>v. <em>Lee, </em><span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/#563" aria-description="Citation for case: United States v. Lee">274 U. S. 559, 563</a></span>. But what he seeks-to preserve as private, even in an area accessible to the public, may be constitutionally pro<page-number citation-index="1" label="352">*352</page-number>tected. See <em>Rios </em>v. <em>United States, </em><span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/" aria-description="Citation for case: Rios v. United States">364 U. S. 253</a></span>; <em>Ex parte Jackson, </em><span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727, 733</a></span>.</p>
<p id="b462-6">The Government stresses the fact that the telephone booth from which the petitioner made his calls was constructed partly of glass, so that he was as visible after he entered it as he would have been if he had remained outside. But what he sought to exclude when he entered the booth was not the intruding eye — it was the uninvited ear. He did not shed his right to do so simply because he made his calls from a place where he might be seen. No less than an individual in a business office,<footnotemark>10</footnotemark> in a friend’s apartment,<footnotemark>11</footnotemark> or in a taxicab,<footnotemark>12</footnotemark> a person in a telephone booth may rely upon the protection of the Fourth Amendment. One who occupies it, shuts the door behind him, and pays the toll that permits him to place a call is surely entitled to assume that the words he utters into the mouthpiece will not be broadcast to the world. To read the Constitution more narrowly is to ignore the vital role that the public telephone has come to play in private communication.</p>
<p id="b462-7">The Government contends, however, that the activities of its agents in this case should not be tested by Fourth Amendment requirements, for the surveillance technique they employed involved no physical penetration of the telephone booth from which the petitioner placed his calls. It is true that the absence of such penetration was at one time thought to foreclose further Fourth Amendment inquiry, <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#457" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 457, 464, 466</a></span>; <em>Goldman </em>v. <em>United States, </em><span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/#134" aria-description="Citation for case: Goldman v. United States">316 U. S. 129, 134-136</a></span>, for that Amendment was thought to limit only searches and seizures of tangible <page-number citation-index="1" label="353">*353</page-number>property.<footnotemark>13</footnotemark> But “[t]he premise that property interests control the right of the Government to search and seize has been discredited.” <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#304" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 304</a></span>. Thus, although a closely divided Court supposed in <em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">Olmstead</a></span> </em>that surveillance without any trespass and without the seizure of any material object fell outside the ambit of the Constitution, we have since departed from the narrow view on which that decision rested. Indeed, we have expressly held that the Fourth Amendment governs not only the seizure of tangible items, but extends as well to the recording of oral statements, overheard without any “technical trespass under . . . local property law.” <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511</a></span>. Once this much is acknowledged, and once it is recognized that the Fourth Amendment protects people— and not simply “areas” — against unreasonable searches and seizures, it becomes clear that the reach of that Amendment cannot turn upon the presence or absence of a physical intrusion into any given enclosure.</p>
<p id="b463-5">We conclude that the underpinnings of <em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">Olmstead</a></span> </em>and <em><span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">Goldman</a></span> </em>have been so eroded by our subsequent decisions that the “trespass” doctrine there enunciated can no longer be regarded as controlling. The Government’s activities in electronically listening to and recording the petitioner’s words violated the privacy upon which he justifiably relied while using the telephone booth and thus constituted a “search and seizure” within the meaning of the Fourth Amendment. The fact that the electronic device employed to achieve that end did not happen to penetrate the wall of the booth can have no constitutional significance.</p>
<p id="b464-5"><page-number citation-index="1" label="354">*354</page-number>The question remaining for decision, then, is whether the search and seizure conducted in this case complied with constitutional standards. In that regard, the Government’s position is that its agents acted in an entirely defensible manner: They did not begin their electronic surveillance until investigation of the petitioner’s activities had established a strong probability that he was using the telephone in question to transmit gambling information to persons in other States, in violation of federal law. Moreover, the surveillance was limited, both in scope and in duration, to the specific purpose of establishing the contents of the petitioner’s unlawful telephonic communications. The agents confined their surveillance to the brief periods during which he used the telephone booth,<footnotemark>14</footnotemark> and they took great care to overhear only the conversations of the petitioner himself.<footnotemark>15</footnotemark></p>
<p id="b464-6">Accepting this account of the Government’s actions as accurate, it is clear that this surveillance was so narrowly circumscribed that a duly authorized magistrate, properly notified of the need for such investigation, specifically informed of the basis on which it was to proceed, and clearly apprised of the precise intrusion it would entail, could constitutionally have authorized, with appropriate safeguards, the very limited search and seizure that the Government asserts in fact took place. Only last Term we sustained the validity of <page-number citation-index="1" label="355">*355</page-number>such an authorization, holding that, under sufficiently “precise and discriminate circumstances,” a federal court may empower government agents to employ a concealed electronic device “for the narrow and particularized purpose of ascertaining the truth of the . . . allegations” of a “detailed factual affidavit alleging the commission of a specific criminal offense.” <em>Osborn </em>v. <em>United States, </em><span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/#329" aria-description="Citation for case: Osborn v. United States">385 U. S. 323, 329-330</a></span>. Discussing that holding, the Court in <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span>, said that “the order authorizing the use of the electronic device” in <em><span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/" aria-description="Citation for case: Osborn v. United States">Osborn</a></span> </em>“afforded similar protections to those ... of conventional warrants authorizing the seizure of tangible evidence.” Through those protections, “no greater invasion of privacy was permitted than was necessary under the circumstances.” <em>Id., </em>at 57.<footnotemark>16</footnotemark> Here, too, a similar <page-number citation-index="1" label="356">*356</page-number>judicial order could have accommodated “the legitimate needs of law enforcement” <footnotemark>17</footnotemark> by authorizing the carefully limited use of electronic surveillance.</p>
<p id="b466-6">The Government urges that, because its agents relied upon the decisions in <em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">Olmstead</a></span> </em>and <em><span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">Goldman</a></span>, </em>and because they did no more here than they might properly have done with prior judicial sanction, we should retroactively validate their conduct. That we cannot do. It is apparent that the agents in this case acted with restraint. Yet the inescapable fact is that this restraint was imposed by the agents themselves, not by a judicial officer. They were not required, before commencing the search, to present their estimate of probable cause for detached scrutiny by a neutral magistrate. They were not compelled, during the conduct of the search itself, to observe precise limits established in advance by a specific court order. Nor were they directed, after the search had been completed, to notify the authorizing magistrate in detail of all that had been seized. In the absence of such safeguards, this Court has never sustained a search upon the sole ground that officers reasonably expected to find evidence of a particular crime and voluntarily confined their activities to the least intrusive <page-number citation-index="1" label="357">*357</page-number>means consistent with that end. Searches conducted without warrants have been held unlawful “notwithstanding facts unquestionably showing probable cause,” <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span>, for the Constitution requires “that the deliberate, impartial judgment of a judicial officer ... be interposed between the citizen and the police . . ..” <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#481" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 481-82</a></span>. “Over and again this Court has emphasized that the mandate of the [Fourth] Amendment requires adherence to judicial processes,” <em>United States </em>v. <em>Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span>, and that searches conducted outside the judicial process, without prior approval by judge or magistrate, are <em>per se </em>unreasonable under the Fourth Amendment<footnotemark>18</footnotemark> — subject only to a few specifically established and well-delineated exceptions.<footnotemark>19</footnotemark></p>
<p id="b467-5">It is difficult to imagine how any of those exceptions could ever apply to the sort of search and seizure involved in this case. Even electronic surveillance substantially contemporaneous with an individual’s arrest could hardly be deemed an “incident” of that arrest.<footnotemark>20</footnotemark> <page-number citation-index="1" label="358">*358</page-number>Nor could the use of electronic surveillance without prior authorization be justified on grounds of “hot pursuit.” <footnotemark>21</footnotemark> And, of course, the very nature of electronic surveillance precludes its use pursuant to the suspect’s consent.<footnotemark>22</footnotemark></p>
<p id="b468-6">The Government does not question these basic principles. Rather, it urges the creation of a new exception to cover this case.<footnotemark>23</footnotemark> It argues that surveillance of a telephone booth should be exempted from the usual requirement of advance authorization by a magistrate upon a showing of probable cause. We cannot agree. Omission of such authorization</p>
<blockquote id="b468-7">“bypasses the safeguards provided by an objective predetermination of probable cause, and substitutes instead the far less reliable procedure of an after-the-event justification for the . . . search, too likely to be subtly influenced by the familiar shortcomings of hindsight judgment.” <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96</a></span>.</blockquote>
<p id="b468-8">And bypassing a neutral predetermination of the <em>scope </em>of a search leaves individuals secure from Fourth Amend<page-number citation-index="1" label="359">*359</page-number>ment violations “only in the discretion of the police.” <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#97" aria-description="Citation for case: Beck v. Ohio"><em>Id., </em>at 97</a></span>.</p>
<p id="b469-5">These considerations do not vanish when the search in question is transferred from the setting of a home, an office, or a hotel room to that of a telephone booth. Wherever a man may be, he is entitled to know that he will remain free from unreasonable searches and seizures. The government agents here ignored “the procedure of antecedent justification . . . that is central to the Fourth Amendment,” <footnotemark>24</footnotemark> a procedure that we hold to be a constitutional precondition of the kind of electronic surveillance involved in this case. Because the surveillance here failed to meet that condition, and because it led to the petitioner’s conviction, the judgment must be reversed.</p>
<p id="b469-6">
<em>It is so ordered.</em>
</p>
<judges id="b469-7">Mr. Justice Marshall took no part in the consideration or decision of this case.</judges>
<footnote label="1">
<p id="b458-8"> <span class="citation no-link">18 U. S. C. § 1084</span>. That statute provides in pertinent part:</p>
<blockquote id="b458-9">“(a) Whoever being engaged in the business of betting or wagering knowingly uses a wire communication facility for the transmission in interstate or foreign commerce of bets or wagers or information assisting in the placing of bets or wagers on any sporting event or contest, or for the transmission of a wire communication which entitles the recipient to receive money or credit as a result of bets or wagers, or for information assisting in the placing of bets or wagers, shall be fined not more than $10,000 or imprisoned not more than two years, or both.</blockquote>
<blockquote id="b458-10">“(b) Nothing in this section shall be construed to prevent the transmission in interstate or foreign commerce of information for use in news reporting of sporting events or contests, or for the transmission of information assisting in the placing of bets or wagers on a sporting event or contest from a State where betting on that sporting event or contest is legal into a State in which such betting is legal.”</blockquote>
</footnote>
<footnote label="2">
<p id="b459-7"> <span class="citation" data-id="273830"><a href="/opinion/273830/charles-katz-v-united-states/#134" aria-description="Citation for case: Charles Katz v. United States">369 F. 2d 130, 134</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b459-8"> <span class="citation multiple-matches"><a href="/c/U.%20S./386/954/">386 U. S. 954</a></span>. The petition for certiorari also challenged the validity of a warrant authorizing the search of the petitioner’s premises. In light of our disposition of this ease, we do not reach that issue.</p>
<p id="b459-9">We find no merit in the petitioner’s further suggestion that his indictment must be dismissed. After his conviction was affirmed by the Court of Appeals, he testified before a federal grand jury concerning the charges involved here. Because he was compelled to testify pursuant to a grant of immunity, <span class="citation no-link">48 Stat. 1096</span>, as amended, 47 TJ. S. C. § <em>409(l), </em>it is clear that the fruit of his testimony cannot be used against him in any future trial. But the petitioner asks for more. He contends that his conviction must be vacated and the charges against him dismissed lest he be “subjected to [a] penalty . . . on account of [a] . . . matter . . . concerning which he [was] compelled ... to testify . . . .” <span class="citation no-link">47 U. S. C. §409</span> <em>(l). Frank </em>v. <em>United States, </em><span class="citation" data-id="268411"><a href="/opinion/268411/john-j-frank-v-united-states-of-america-oliver-w-angelone-v-united/" aria-description="Citation for case: John J. Frank v. United States of America, Oliver W....">347 F. 2d 486</a></span>. We disagree. In relevant part, § 409 <em>(l) </em>substantially repeats the language of the Compulsory Testimony Act of 1893, <span class="citation no-link">27 Stat. 443</span>, <span class="citation no-link">49 U. S. C. § 46</span>, which was Congress’ response to this Court’s statement that an immunity statute can supplant the Fifth Amendment privilege against self-incrimination only if it affords adequate protection from future prosecution or conviction. <em>Counselman </em>v. <em>Hitchcock, </em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#585" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 585-586</a></span>. The statutory provision here involved was designed to provide such protection, see <em>Brown </em>v. <em>United States, </em><span class="citation" data-id="9421773"><a href="/opinion/105848/brown-v-united-states/#45" aria-description="Citation for case: Brown v. United States">359 U. S. 41, 45-46</a></span>, not to confer immunity from punishment pursuant to a <em>prior </em>prosecution and adjudication of guilt. Cf. <em>Reina </em>v. <em>United States, </em><span class="citation" data-id="9422092"><a href="/opinion/106146/reina-v-united-states/#513" aria-description="Citation for case: Reina v. United States">364 U. S. 507, 513-514</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b460-7"> “The average man would very likely not have his feelings soothed any more by having his property seized openly than by having it seized privately and by stealth. . . . And a person can be just as much, if not more, irritated, annoyed and injured by an unceremonious public arrest by a policeman as he is by a seizure in the privacy of his office or home.” <em>Griswold </em>v. <em>Connecticut, </em><span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/#509" aria-description="Citation for case: Griswold v. Connecticut">381 U. S. 479, 509</a></span> (dissenting opinion of Mr. Justice Black).</p>
</footnote>
<footnote label="5">
<p id="b460-8"> The First Amendment, for example, imposes limitations upon governmental abridgment of “freedom to associate and privacy in one’s associations.” <em>NAACP </em>v. <em>Alabama, </em><span class="citation" data-id="105746"><a href="/opinion/105746/national-assn-for-the-advancement-of-colored-people-v-alabama-ex-rel/#462" aria-description="Citation for case: National Ass&#x27;n for the Advancement of Colored People v....">357 U. S. 449, 462</a></span>. The Third Amendment’s prohibition against the unconsented peacetime quartering of soldiers protects another aspect of privacy from governmental intrusion. To some extent, the Fifth Amendment too “reflects the Constitution’s concern for . the right of each individual “to a private enclave where he may lead a private life.” ’ ” <em>Tehan </em>v. <em>Shott, </em><span class="citation multiple-matches"><a href="/c/U.%20S./382/406/">382 U. S. 406</a></span>, 416. Virtually every governmental action interferes with personal privacy to some degree. The question in each case is whether that interference violates a command of the United States Constitution.</p>
</footnote>
<footnote label="6">
<p id="b460-11"> See Warren &amp; Brandéis, The Right to Privacy, <span class="citation no-link">4 Harv. L. Rev. 193</span> (1890).</p>
</footnote>
<footnote label="7">
<p id="b461-6"> See, <em>e. g., Time, Inc. </em>v. <em>Hill, </em><span class="citation" data-id="9423311"><a href="/opinion/107325/time-inc-v-hill/" aria-description="Citation for case: Time, Inc. v. Hill">385 U. S. 374</a></span>. Cf. <em>Breard </em>v. <em>Alexandria, </em><span class="citation" data-id="9420616"><a href="/opinion/104917/breard-v-alexandria/" aria-description="Citation for case: Breard v. Alexandria">341 U. S. 622</a></span>; <em>Kovacs </em>v. <em>Cooper, </em><span class="citation" data-id="9420278"><a href="/opinion/104623/kovacs-v-cooper/" aria-description="Citation for case: Kovacs v. Cooper">336 U. S. 77</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b461-7"> In support of their respective claims, the parties have compiled competing lists of “protected areas” for our consideration. It appears to be common ground that a private home is such an area, <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, but that an open field is not. <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span>. Defending the inclusion of a telephone booth in his fist the petitioner cites <em>United States </em>v. <em>Stone, </em><span class="citation" data-id="1748896"><a href="/opinion/1748896/united-states-v-stone/" aria-description="Citation for case: United States v. Stone">232 F. Supp. 396</a></span>, and <em>United States </em>v. <em>Madison, </em>32 L. W. 2243 (D. C. Ct. Gen. Sess.). Urging that the telephone booth should be excluded, the Government finds support in <em>United States </em>v. <em>Borgese, </em><span class="citation" data-id="1455097"><a href="/opinion/1455097/united-states-v-borgese/" aria-description="Citation for case: United States v. Borgese">235 F. Supp. 286</a></span>.</p>
</footnote>
<footnote label="9">
<p id="b461-8"> It is true that this Court has occasionally described its conclusions in terms of “constitutionally protected areas,” see, <em>e. g., Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#510" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 510, 512</a></span>; <em>Lopez </em>v. <em>United States, </em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#438" aria-description="Citation for case: Lopez v. United States">373 U. S. 427, 438-439</a></span>; <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#57" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 57, 59</a></span>, but we have never suggested that this concept can serve as a talismanic solution to every Fourth Amendment problem.</p>
</footnote>
<footnote label="10">
<p id="b462-8"> <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>.</p>
</footnote>
<footnote label="11">
<p id="b462-9"> <em>Jones v. United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span>.</p>
</footnote>
<footnote label="12">
<p id="b462-10"><em> Rios </em>v. <em>United States, </em><span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/" aria-description="Citation for case: Rios v. United States">364 U. S. 253</a></span>.</p>
</footnote>
<footnote label="13">
<p id="b463-6"> See <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#464" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 464-466</a></span>. We do not deal in this case with the law of detention or arrest under the Fourth Amendment.</p>
</footnote>
<footnote label="14">
<p id="b464-7"> Based upon their previous visual observations of the petitioner, the agents correctly predicted that he would use the telephone booth for several minutes at approximately the same time each morning. The petitioner was subjected to electronic surveillance only during this predetermined period. Six recordings, averaging some three minutes each, were obtained and admitted in evidence. They preserved the petitioner’s end of conversations concerning the placing of bets and the receipt of wagering information.</p>
</footnote>
<footnote label="15">
<p id="b464-8"> On the single occasion when the statements of another person were inadvertently intercepted, the agents refrained from listening to them.</p>
</footnote>
<footnote label="16">
<p id="b465-5"> Although the protections afforded the petitioner in <em><span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/" aria-description="Citation for case: Osborn v. United States">Osborn</a></span> </em>were <em>“similar </em>... to those ... of conventional warrants,” they were not identical. A conventional warrant ordinarily serves to notify the suspect of an intended search. But if Osborn had been told in advance that federal officers intended to record his conversations, the point of making such recordings would obviously have been lost; the evidence in question could not have been obtained. In omitting any requirement of advance notice, the federal court that authorized electronic surveillance in <em><span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/" aria-description="Citation for case: Osborn v. United States">Osborn</a></span> </em>simply recognized, as has this Court, that officers need not announce their purpose before conducting an otherwise authorized search if such an announcement would provoke the escape of the suspect or the destruction of critical evidence. See <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#37" aria-description="Citation for case: Ker v. California">374 U. S. 23, 37-41</a></span>.</p>
<p id="b465-6">Although some have thought that this “exception to the notice requirement where exigent circumstances are present,” <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#39" aria-description="Citation for case: Ker v. California"><em>id., </em>at 39</a></span>, should be deemed inapplicable where police enter a home before its occupants are aware that officers are present, <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#55" aria-description="Citation for case: Ker v. California"><em>id., </em>at 55-58</a></span> (opinion of Mr. Justice BrenNAN), the reasons for such a limitation have no bearing here. However true it may be that “[i]nnocent citizens should not suffer the shock, fright or embarrassment attendant upon an unannounced police intrusion,” <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#57" aria-description="Citation for case: Ker v. California"><em>id., </em>at 57</a></span>, and that “the requirement of awareness . . . serves to minimize the hazards of the officers’ dangerous calling,” <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#57" aria-description="Citation for case: Ker v. California"><em>id., </em>at 57-58</a></span>, these considerations are not rele<page-number citation-index="1" label="356">*356</page-number>vant to the problems presented by judicially authorized electronic surveillance.</p>
<p id="b466-8">Nor do the Federal Rules of Criminal Procedure impose an inflexible requirement of prior notice. Rule 41 (d) does require federal officers to serve upon the person searched a copy of the warrant and a receipt describing the material obtained, but it does not invariably require that this be done before the search takes place. <em>Nordelli </em>v. <em>United States, </em><span class="citation" data-id="1497017"><a href="/opinion/1497017/nordelli-v-united-states/#666" aria-description="Citation for case: Nordelli v. United States">24 F. 2d 665, 666-667</a></span>.</p>
<p id="b466-9">Thus the fact that the petitioner in <em><span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/" aria-description="Citation for case: Osborn v. United States">Osborn</a></span> </em>was unaware that his words were being electronically transcribed did not prevent this Court from sustaining his conviction, and did not prevent the Court in <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span> </em>from reaching the conclusion that the use of the recording device sanctioned in <em><span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/" aria-description="Citation for case: Osborn v. United States">Osborn</a></span> </em>was entirely lawful. <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#57" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 57</a></span>.</p>
</footnote>
<footnote label="17">
<p id="b466-10"> <em>Lopez </em>v. <em>United States, </em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#464" aria-description="Citation for case: Lopez v. United States">373 U. S. 427, 464</a></span> (dissenting opinion of Me. Justice BRENNAN).</p>
</footnote>
<footnote label="18">
<p id="b467-6"> See, <em>e. g., Jones </em>v. <em>United States, </em><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#497" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 497-499</a></span>; <em>Rios </em>v. <em>United States, </em><span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/#261" aria-description="Citation for case: Rios v. United States">364 U. S. 253, 261</a></span>; <em>Chapman </em>v. <em>United States, </em><span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/#613" aria-description="Citation for case: Chapman v. United States">365 U. S. 610, 613-615</a></span>; <em>Stoner </em>v. <em>California, </em><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#486" aria-description="Citation for case: Stoner v. California">376 U. S. 483, 486-487</a></span>.</p>
</footnote>
<footnote label="19">
<p id="b467-7"> See, e. <em>g., Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153, 156</a></span>; <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#454" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 454-456</a></span>; <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, <em>174-177; Cooper </em></a></span>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span>; <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298-300</a></span>.</p>
</footnote>
<footnote label="20">
<p id="b467-8"> In <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span>, the Court stated:</p>
<blockquote id="AVRE">“The right without a search warrant contemporaneously to search persons lawfully arrested while committing crime and to search the place where the arrest is made in order to find and seize things connected with the crime as its fruits or as the means by which it was committed, as well as weapons and other things to effect an escape from custody, is not to be doubted.”</blockquote>
<p id="b467-9">Whatever one’s view of “the long-standing practice of searching for other proofs of guilt within the control of the accused found upon arrest,” <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#61" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 61</a></span>; cf. <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#71" aria-description="Citation for case: United States v. Rabinowitz"><em>id., </em>at <page-number citation-index="1" label="358">*358</page-number>71-79</a></span> (dissenting opinion of Mr. Justice Frankfurter), the concept of an “incidental’’ search cannot readily be extended to include surreptitious surveillance of an individual either immediately before, or immediately after, his arrest.</p>
</footnote>
<footnote label="21">
<p id="b468-10"> Although “[t]he Fourth Amendment does not require police officers to delay in the course of an investigation if to do so would gravely endanger their lives or the lives of others,” <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298-299</a></span>, there seems little likelihood that electronic surveillance would be a realistic possibility in a situation so fraught with urgency.</p>
</footnote>
<footnote label="22">
<p id="b468-11"> A search to which an individual consents meets Fourth Amendment requirements, <em>Zap </em>v. <em>United States, </em><span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/" aria-description="Citation for case: Zap v. United States">328 U. S. 624</a></span>, but of course “the usefulness of electronic surveillance depends on lack of notice to the suspect.” <em>Lopez </em>v. <em>United States, </em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#463" aria-description="Citation for case: Lopez v. United States">373 U. S. 427, 463</a></span> (dissenting opinion of MR. Justice BreNNAn).</p>
</footnote>
<footnote label="23">
<p id="b468-12"> Whether safeguards other than prior authorization by a magistrate would satisfy the Fourth Amendment in a situation involving the national security is a question not presented by this case.</p>
</footnote>
<footnote label="24">
<p id="b469-11"> See <em>Osborn </em>v. <em>United States, </em><span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/#330" aria-description="Citation for case: Osborn v. United States">385 U. S. 323, 330</a></span>.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Kentucky v. King.md  (`case`, 9 assertions)

### content_page

```
---
title: "Kentucky v. King"
type: case
citation: "563 U.S. 452 (2011)"
parallel_cite: "131 S. Ct. 1849; 179 L. Ed. 2d 865"
neutral_cite: 2011 U.S. LEXIS 3541
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2011
date_decided: 2011-05-16
docket: 09-1272
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2011-05-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Kentucky v. King
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/216733/kentucky-v-king/"
  cluster_id: 216733
  opinion_id: 9441559
  identity_checked: true
homes:
  - page: "[[Destruction of Evidence]]"
    role: "Key — Anchor"
  - page: "[[Exigent Circumstances and Hot Pursuit]]"
    role: "Related (no-police-created-exigency outer limit)"
  - page: "[[Arrest in the Home]]"
    role: "Related (cross-doctrine)"
  - page: "[[Knock and Talk]]"
    role: "Related (cross-doctrine)"
  - page: "[[Curtilage]]"
    role: "Related (cross-doctrine)"
related: ["[[Brigham City v. Stuart]]", "[[Lange v. California]]", "[[Payton v. New York]]"]
aliases: []
tags: ["case", "fourth-amendment", "exigent-circumstances", "police-created-exigency", "destruction-of-evidence"]
holding: "The exigent-circumstances rule applies even where police 'created' the exigency, SO LONG AS the police did not create it by engaging or…"
lake:
  record_id: Kentucky v. King
  status: verified
  projected_at: 2026-07-09
---

# Kentucky v. King

*563 U.S. 452 (2011)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers pursuing a suspected drug dealer into an apartment breezeway smelled burnt marijuana coming from one apartment. They banged on that door and announced "police." They then heard noises they believed indicated the destruction of evidence, kicked in the door, and found drugs. King argued the officers had impermissibly "created" the [[Exigent Circumstances and Hot Pursuit|exigency]] by knocking and announcing.

## Issue
Whether the exigent-circumstances exception is forfeited under the "police-created exigency" doctrine when it is the officers' own [[Knock-and-Announce|knock-and-announce]] that prompts the occupants to begin destroying evidence.

## Rule
The test keys on whether the police acted lawfully before the [[Exigent Circumstances and Hot Pursuit|exigency]] arose: "a warrantless entry based on exigent circumstances is reasonable when the police did not create the exigency by engaging or threatening to engage in conduct violating the Fourth Amendment." — 563 U.S. at ___ (slip op., at 8). ^pin-op8

Conduct such as knocking on a door and announcing one's presence — which any private citizen may do — does not violate or threaten to violate the Fourth Amendment, and so does not impermissibly manufacture the [[Exigent Circumstances and Hot Pursuit|exigency]].

## Application
The officers' decision to knock loudly on the apartment door and announce "police" was lawful conduct that any occupant was free to ignore; the officers did not demand entry or otherwise threaten a Fourth Amendment violation before the sounds of evidence destruction began. Because the police thus did not create the [[Exigent Circumstances and Hot Pursuit|exigency]] by unlawful or threatened-unlawful conduct, their reliance on the destruction-of-evidence [[Exigent Circumstances and Hot Pursuit|exigency]] was permissible (the Court [[Reading and Citing Cases#on-remand|remanded]] for the state courts to determine whether an [[Exigent Circumstances and Hot Pursuit|exigency]] in fact existed).

## Conclusion
The judgment suppressing the evidence was reversed and the case [[Reading and Citing Cases#on-remand|remanded]]; lawful police conduct that prompts an occupant to destroy evidence does not forfeit the exigent-circumstances exception.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. [[Lange v. California]] (2021) later addressed a different [[Exigent Circumstances and Hot Pursuit|exigency]] question (categorical [[Exigent Circumstances and Hot Pursuit|hot pursuit]] of fleeing misdemeanants) and cited *King* for the case-specific "compelling need" standard, leaving *King*'s police-created-[[Exigent Circumstances and Hot Pursuit|exigency]] holding intact.

## Appears on
- [[Exigent Circumstances and Hot Pursuit]] — *Key — Anchor*
- [[Arrest in the Home]] — *Related (cross-doctrine)*
- [[Knock and Talk]] — *Related (cross-doctrine)*

## Sources
- *Kentucky v. King*, 563 U.S. 452 (2011) — https://www.courtlistener.com/opinion/216733/kentucky-v-king/ — pinpoint given as slip-opinion page (slip op., at 8); CourtListener carries the slip opinion, paginated by slip page (opinion 216733).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a3196bacc67503cf", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "563 U.S. 452 (2011)", "court": "U.S. Supreme Court", "neutral_cite": "2011 U.S. LEXIS 3541", "official_citation_present": true, "parallel_cite": "131 S. Ct. 1849; 179 L. Ed. 2d 865", "title": "Kentucky v. King", "year": "2011"}}
{"assertion_id": "010f34ad6984dd67", "dimension": "support", "kind": "home_role", "locator": {"home": "Exigent Circumstances and Hot Pursuit"}, "payload": {"home": "Exigent Circumstances and Hot Pursuit", "role": "Related (no-police-created-exigency outer limit)", "title": "Kentucky v. King"}}
{"assertion_id": "03672bb0ec7ff7ea", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The exigent-circumstances rule applies even where police 'created' the exigency, SO LONG AS the police did not create it by engaging or…", "title": "Kentucky v. King"}}
{"assertion_id": "56cf13878d59c45a", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Related (cross-doctrine)", "title": "Kentucky v. King"}}
{"assertion_id": "57c72db70f1b4c19", "dimension": "support", "kind": "home_role", "locator": {"home": "Knock and Talk"}, "payload": {"home": "Knock and Talk", "role": "Related (cross-doctrine)", "title": "Kentucky v. King"}}
{"assertion_id": "67e62ea4b0bed52e", "dimension": "support", "kind": "home_role", "locator": {"home": "Destruction of Evidence"}, "payload": {"home": "Destruction of Evidence", "role": "Key — Anchor", "title": "Kentucky v. King"}}
{"assertion_id": "c337fbc5052c2d19", "dimension": "support", "kind": "home_role", "locator": {"home": "Curtilage"}, "payload": {"home": "Curtilage", "role": "Related (cross-doctrine)", "title": "Kentucky v. King"}}
{"assertion_id": "62a9edd921d890df", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Kentucky v. King"}}
{"assertion_id": "a5e078853a5970a7", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2011-05-16", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Kentucky v. King", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Kentucky v. King", "varies_by_point": "false"}}
```

### lake record — Kentucky v. King

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kentucky v. King",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Kentucky v. King",
    "case_name_short": "King",
    "case_name_full": "Kentucky v. King",
    "input_case_name": "Kentucky v. King",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2011-05-16",
    "year": 2011,
    "docket": "09-1272",
    "cluster_id": 216733,
    "lead_opinion_id": 9441559,
    "sibling_ids": [
      216733,
      9441559,
      9441560
    ],
    "absolute_url": "/opinion/216733/kentucky-v-king/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 7341385,
        "score": 20,
        "case_name": "Kentucky v. King"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "563 U.S. 452",
      "volume": "563",
      "reporter": "U.S.",
      "page": "452",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "131 S. Ct. 1849",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "1849",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "179 L. Ed. 2d 865",
        "volume": "179",
        "reporter": "L. Ed. 2d",
        "page": "865",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2011 U.S. LEXIS 3541",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "3541",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "131 S. Ct. 1849",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "1849",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "179 L. Ed. 2d 865",
        "volume": "179",
        "reporter": "L. Ed. 2d",
        "page": "865",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "563 U.S. 452",
        "volume": "563",
        "reporter": "U.S.",
        "page": "452",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 U.S. LEXIS 3541",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "3541",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "563 U.S. 452",
    "official_selection": {
      "court_class": "scotus",
      "selected": "563 U.S. 452",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op8",
      "page": null,
      "quote": "doctrine when it is the officers' own knock-and-announce that prompts the occupants to begin destroying evidence. ## Rule The test keys on whether the police acted lawfully before the exigency arose:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2011-05-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kentucky v. King",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 10740496,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kentucky v. King:lane1_negative"
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
        "journal_ref": "Kentucky v. King:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Privette",
          "cluster_id": 9387170,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kentucky v. King:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Portulano",
          "cluster_id": 10135231,
          "cite": [
            "320 Or. App. 335",
            "514 P.3d 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kentucky v. King:lane1_negative"
      },
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
        "journal_ref": "Kentucky v. King:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jerel Chinedu Igboji v. State",
          "cluster_id": 4789820,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kentucky v. King:lane1_negative"
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
        "journal_ref": "Kentucky v. King:lane2_top_cited"
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
        "journal_ref": "Kentucky v. King:lane2_top_cited"
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
        "journal_ref": "Kentucky v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henry v. Purnell",
          "cluster_id": 220962,
          "cite": [
            "652 F.3d 524",
            "2011 U.S. App. LEXIS 14391",
            "2011 WL 2725816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kentucky v. King:lane2_top_cited"
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
        "journal_ref": "Kentucky v. King:lane2_top_cited"
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
        "journal_ref": "Kentucky v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Turrubiate v. State",
          "cluster_id": 2948365,
          "cite": [
            "399 S.W.3d 147",
            "2013 WL 1438172",
            "2013 Tex. Crim. App. LEXIS 635"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kentucky v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Constance Westfall v. Jose Luna",
          "cluster_id": 4534975,
          "cite": [
            "903 F.3d 534"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kentucky v. King:lane2_top_cited"
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
        "journal_ref": "Kentucky v. King:lane2_top_cited"
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
        "journal_ref": "Kentucky v. King:lane2_top_cited"
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
        "journal_ref": "Kentucky v. King:lane2_top_cited"
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
        "journal_ref": "Kentucky v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tiffanie Hupp v. State Trooper Seth Cook",
          "cluster_id": 4642928,
          "cite": [
            "931 F.3d 307"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kentucky v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Americans for Prosperity Foundation v. Bonta",
          "cluster_id": 4896549,
          "cite": [
            "594 U.S. 595",
            "210 L. Ed. 2d 716",
            "141 S. Ct. 2373"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kentucky v. King:lane2_top_cited"
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
        "journal_ref": "Kentucky v. King:lane2_top_cited"
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
        "journal_ref": "Kentucky v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Perea-Rey",
          "cluster_id": 801335,
          "cite": [
            "680 F.3d 1179",
            "2012 U.S. App. LEXIS 10941",
            "2012 WL 1948973"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kentucky v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Norman Carpenter v. Deputy Harold Gage",
          "cluster_id": 805384,
          "cite": [
            "686 F.3d 644",
            "2012 WL 3052832",
            "2012 U.S. App. LEXIS 15534"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kentucky v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Julie Peffer v. Mike Stephens",
          "cluster_id": 4459807,
          "cite": [
            "880 F.3d 256"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kentucky v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ulbricht",
          "cluster_id": 4395694,
          "cite": [
            "858 F.3d 71",
            "2017 WL 2346566"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kentucky v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Christopher Covey v. Assessor of Ohio County",
          "cluster_id": 2773276,
          "cite": [
            "777 F.3d 186",
            "2015 WL 309598",
            "2015 U.S. App. LEXIS 1113"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kentucky v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Lemaricus Devall Davidson",
          "cluster_id": 4331383,
          "cite": [
            "509 S.W.3d 156",
            "2016 Tenn. LEXIS 913"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kentucky v. King:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neil Morgan v. Fairfield Cty., Ohio",
          "cluster_id": 4532978,
          "cite": [
            "903 F.3d 553"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kentucky v. King:lane2_top_cited"
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
        "journal_ref": "Kentucky v. King:lane2_top_cited"
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
        "journal_ref": "Kentucky v. King:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(216733 OR 9441559 OR 9441560) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTcxOTYxNjAwMDAwJnM9NDY3MzA5NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28216733+OR+9441559+OR+9441560%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(216733 OR 9441559 OR 9441560)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04NiZzPTQ0NzEwMTcmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28216733+OR+9441559+OR+9441560%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(216733 OR 9441559 OR 9441560)",
        "reviewed": 89,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 89,
        "triage_read": 2,
        "triage_snippet_classified": 87
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(216733 OR 9441559 OR 9441560)",
    "indexed_citing_opinions": 758,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 216733,
        "count": 565,
        "count_source": "search"
      },
      {
        "opinion_id": 9441559,
        "count": 209,
        "count_source": "search"
      },
      {
        "opinion_id": 9441560,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1458,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kentucky-v-king.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyOTc2OTImcz0xMDM3NTkyMCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28216733+OR+9441559+OR+9441560%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 216733,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 108854,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 112416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 112448,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 118103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 121153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 121167,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 131146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 131161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 145669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 506171,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 512577,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 543784,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 550088,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 785789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 788970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 793261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 1024793,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 1603113,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 216733,
        "cited_id": 2342951,
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
    "date_created": "2026-07-05T09:15:59Z",
    "date_modified": "2026-07-09T05:52:34Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T09:16:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T09:16:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T09:19:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T09:16:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Kentucky v. King

```
<opinion type="majority">
<author id="b535-4"><page-number citation-index="1" label="455">*455</page-number>Justice Alito</author>
<p id="ANq">delivered the opinion of the Court.</p>
<p id="b535-5">It is well established that “exigent circumstances,” including the need to prevent the destruction of evidence, permit police officers to conduct an otherwise permissible search without first obtaining a warrant. In this case, we consider whether this rule applies when police, by knocking on the door of a residence and announcing their presence, cause the occupants to attempt to destroy evidence. The Kentucky Supreme Court held that the exigent circumstances rule does not apply in the case at hand because the police should have foreseen that their conduct would prompt the occupants to attempt to destroy evidence. We reject this interpretation of the exigent circumstances rule. The conduct of the police prior to their entry into the apartment was entirely lawful. They did not violate the Fourth Amendment or threaten to do so. In such a situation, the exigent circumstances rule applies.</p>
<p id="b535-6">I</p>
<p id="b535-7">A</p>
<p id="b535-8">This case concerns the search of an apartment in Lexington, Kentucky. Police officers set up a controlled buy of crack cocaine outside an apartment complex. Undercover <page-number citation-index="1" label="456">*456</page-number>Officer Gibbons watched the deal take place from an unmarked car in a nearby parking lot. After the deal occurred, Gibbons radioed uniformed officers to move in on the suspect. He told the officers that the suspect was moving quickly toward the breezeway of an apartment building, and he urged them to “hurry up and get there” before the suspect entered an apartment. App. 20.</p>
<p id="b536-5">In response to the radio alert, the uniformed officers drove into the nearby parking lot, left their vehicles, and ran to the breezeway. Just as they entered the breezeway, they heard a door shut and detected a very strong odor of burnt marijuana. At the end of the breezeway, the officers saw two apartments, one on the left and one on the right, and they did not know which apartment the suspect had entered. Gibbons had radioed that the suspect was running into the apartment on the right, but the officers did not hear this statement because they had already left their vehicles. Because they smelled marijuana smoke emanating from the apartment on the left, they approached the door of that apartment.</p>
<p id="b536-6">Officer Steven Cobb, one of the uniformed officers who approached the door, testified that the officers banged on the left apartment door “as loud as [they] could” and announced, “ ‘This is the police’ ” or “ ‘Police, police, police.’ ” <em>Id., </em>at 22-23. Cobb said that “[a]s soon as [the officers] started banging on the door,” they “could hear people inside moving,” and “[i]t sounded as [though] things were being moved inside the apartment.” <em>Id., </em>at 24. These noises, Cobb testified, led the officers to believe that drug-related evidence was about to be destroyed.</p>
<p id="b536-7">At that point, the officers announced that they “were going to make entry inside the apartment.” <em>Ibid. </em>Cobb then kicked in the door, the officers entered the apartment, and they found three people in the front room: respondent Hollis King, respondent’s girlfriend, and a guest who was smoking <page-number citation-index="1" label="457">*457</page-number>marijuana.<footnotemark>1</footnotemark> The officers performed a protective sweep of the apartment during which they saw marijuana and powder cocaine in plain view. In a subsequent search, they also discovered crack cocaine, cash, and drug paraphernalia.</p>
<p id="b537-5">Police eventually entered the apartment on the right. Inside, they found the suspected drug dealer who was the initial target of their investigation.</p>
<p id="b537-6">B</p>
<p id="b537-7">In the Fayette County Circuit Court, a grand jury charged respondent with trafficking in marijuana, first-degree trafficking in a controlled substance, and second-degree persistent felony offender status. Respondent filed a motion to suppress the evidence from the warrantless search, but the Circuit Court denied the motion. The Circuit Court concluded that the officers had probable cause to investigate the marijuana odor and that the officers “properly conducted [the investigation] by initially knocking on the door of the apartment unit and awaiting the response or consensual entry.” App. to Pet. for Cert. 9a. Exigent circumstances justified the warrantless entry, the court held, because “there was no response at all to the knocking,” and because “Officer Cobb heard movement in the apartment which he reasonably concluded were persons in the act of destroying evidence, particularly narcoties because of the smell.” <em>Ibid. </em>Respondent then entered a conditional guilty plea, reserving his right to appeal the denial of his suppression motion. The court sentenced respondent to 11 years’ imprisonment.</p>
<p id="b537-8">The Kentucky Court of Appeals affirmed. It held that exigent circumstances justified the warrantless entry be<page-number citation-index="1" label="458">*458</page-number>cause the police reasonably believed that evidence would be destroyed. The police did not impermissibly create the exigency, the court explained, because they did not deliberately evade the warrant requirement.</p>
<p id="b538-5">The Supreme Court of Kentucky reversed. <span class="citation" data-id="5108786"><a href="/opinion/5280908/king-v-commonwealth/" aria-description="Citation for case: King v. Commonwealth">302 S. W. 3d 649</a></span> (2010). As a preliminary matter, the court observed that there was “certainly some question as to whether the sound of persons moving [inside the apartment] was sufficient to establish that evidence was being destroyed.” <span class="citation" data-id="5108786"><a href="/opinion/5280908/king-v-commonwealth/#655" aria-description="Citation for case: King v. Commonwealth"><em>Id., </em>at 655</a></span>. But the court did not answer that question. Instead, it “assume[d] for the purpose of argument that exigent circumstances existed.” <em><span class="citation" data-id="5108786"><a href="/opinion/5280908/king-v-commonwealth/" aria-description="Citation for case: King v. Commonwealth">Ibid.</a></span></em></p>
<p id="b538-6">To determine whether police impermissibly created the exigency, the Supreme Court of Kentucky announced a two-part test. First, the court held, police cannot “deliberately creat[e] the exigent circumstances with the bad faith intent to avoid the warrant requirement.” <span class="citation" data-id="5108786"><a href="/opinion/5280908/king-v-commonwealth/#656" aria-description="Citation for case: King v. Commonwealth"><em>Id., </em>at 656</a></span> (internal quotation marks omitted). Second, even absent bad faith, the court concluded, police may not rely on exigent circumstances if “it was reasonably foreseeable that the investigative tactics employed by the police would create the exigent circumstances.” <em>Ibid, </em>(internal quotation marks omitted). Although the court found no evidence of bad faith, it held that exigent circumstances could not justify the search because it was reasonably foreseeable that the occupants would destroy evidence when the police knocked on the door and announced their presence. <em><span class="citation" data-id="5108786"><a href="/opinion/5280908/king-v-commonwealth/" aria-description="Citation for case: King v. Commonwealth">Ibid.</a></span></em></p>
<p id="b538-7">We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./561/1057/">561 U. S. 1057</a></span> (2010).<footnotemark>2</footnotemark></p>
<p id="b539-4"><page-number citation-index="1" label="459">*459</page-number>II</p>
<p id="b539-5">A</p>
<p id="b539-6">The Fourth Amendment provides:</p>
<blockquote id="b539-7">“The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”</blockquote>
<p id="b539-8">The text of the Amendment thus expressly imposes two requirements. First, all searches and seizures must be reasonable. Second, a warrant may not be issued unless probable cause is properly established and the scope of the authorized search is set out with particularity. See <em>Payton </em>v. <em>New York, </em><span class="citation multiple-matches"><a href="/c/U.%20S./445/578/">445 U. S. 578</a></span>, 584 (1980).</p>
<p id="b539-9">Although the text of the Fourth Amendment does not specify when a search warrant must be obtained, this Court has inferred that a warrant must generally be secured. “It is a ‘basic principle of Fourth Amendment law/” we have often said, “ ‘that searches and seizures inside a home without a warrant are presumptively unreasonable.’ ” <em>Brigham City </em>v. <em>Stuart, </em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#403" aria-description="Citation for case: Brigham City v. Stuart">547 U. S. 398, 403</a></span> (2006) (quoting <em>Groh </em>v. <em>Ramirez, </em><span class="citation" data-id="9434540"><a href="/opinion/131161/groh-v-ramirez/#559" aria-description="Citation for case: Groh v. Ramirez">540 U. S. 551, 559</a></span> (2004)). But we have also recognized that this presumption may be overcome in some circumstances because “the ultimate touchstone of the Fourth Amendment is ‘reasonableness.’” <span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#403" aria-description="Citation for case: Brigham City v. Stuart"><em>Brigham City, supra, </em>at 403</a></span>; see also <em>Michigan </em>v. <em>Fisher, </em><span class="citation" data-id="9413217"><a href="/opinion/1755/michigan-v-fisher/#47" aria-description="Citation for case: Michigan v. Fisher">558 U. S. 45, 47</a></span> (2009) <em>(per curiam). </em>Accordingly, the warrant requirement is subject to certain reasonable exceptions. <span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#403" aria-description="Citation for case: Brigham City v. Stuart"><em>Brigham City, supra, </em>at 403</a></span>.</p>
<p id="b540-4"><page-number citation-index="1" label="460">*460</page-number>One well-recognized exception applies when “ ‘the exigencies of the situation’ make the needs of law enforcement so compelling that [a] warrantless search is objectively reasonable under the Fourth Amendment.” <em>Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#394" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 394</a></span> (1978); see also <em>Payton, supra, </em>at 590 (‘‘[T]he Fourth Amendment has drawn a firm line at the entrance to the house. Absent exigent circumstances, that threshold may not reasonably be crossed without a warrant”).</p>
<p id="b540-5">This Court has identified several exigencies that may justify a warrantless search of a home. See <em>Brigham City, </em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#403" aria-description="Citation for case: Brigham City v. Stuart">547 U. S., at 403</a></span>. Under the “emergency aid” exception, for example, “officers may enter a home without a warrant to render emergency assistance to an injured occupant or to protect an occupant from imminent injury.” <em>Ibid.; </em>see also, <span class="citation" data-id="9413217"><a href="/opinion/1755/michigan-v-fisher/#49" aria-description="Citation for case: Michigan v. Fisher"><em>e. g., Fisher, supra, </em>at 49</a></span> (upholding warrantless home entry based on emergency aid exception). Police officers may enter premises without a warrant when they are in hot pursuit of a fleeing suspect. See <em>United States </em>v. <em>Santana, </em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#42" aria-description="Citation for case: United States v. Santana">427 U. S. 38, 42-43</a></span> (1976). And—what is relevant here—the need “to prevent the imminent destruction of evidence” has long been recognized as a sufficient justification for a warrantless search. <span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#403" aria-description="Citation for case: Brigham City v. Stuart"><em>Brigham City, supra, </em>at 403</a></span>; see also <em>Georgia </em>v. <span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/#116" aria-description="Citation for case: Georgia v. Randolph"><em>Randolph, 547 </em>U. S. 103, 116, n. 6</a></span> (2006); <em>Minnesota </em>v. <em>Olson, </em><span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/#100" aria-description="Citation for case: Minnesota v. Olson">495 U. S. 91, 100</a></span> (1990).<footnotemark>3</footnotemark></p>
<p id="AE"><page-number citation-index="1" label="461">*461</page-number>B</p>
<p id="b541-4">Over the years, lower courts have developed an exception to the exigent circumstances rule, the so-called “police-created exigency” doctrine. Under this doctrine, police may not rely on the need to prevent destruction of evidence when that exigency was “created” or “manufactured” by the conduct of the police. See, <em>e. g., United States </em>v. <em>Chambers, </em><span class="citation" data-id="4174077"><a href="/opinion/4396824/lang-v-rogue-valley-medical-centerasante/#566" aria-description="Citation for case: Lang v. Rogue Valley Medical Center/Asante">395 P. 3d 563, 566</a></span> (CA6 2005) (“[F]or a warrantless search to stand, law enforcement officers must be responding to an unanticipated exigency rather than simply creating the exigency for themselves”); <em>United States </em>v. <em>Gould, </em><span class="citation" data-id="9496885"><a href="/opinion/785789/united-states-v-kelly-donald-gould/#590" aria-description="Citation for case: United States v. Kelly Donald Gould">364 F. 3d 578, 590</a></span> (CA5 2004) (en banc) (“[Although exigent circumstances may justify a warrantless probable cause entry into the home, they will not do so if the exigent circumstances were manufactured by the agents” (internal quotation marks omitted)).</p>
<p id="b541-5">In applying this exception for the “creation” or “manufacturing” of an exigency by the police, courts require something more than mere proof that fear of detection by the police caused the destruction of evidence. An additional showing is.' obviously needed because, as the Eighth Circuit has recognized, “in some sense the police always create the exigent circumstances.” <em>United States </em>v. <em>Duchi, </em><span class="citation no-link">906 P. 2d 1278</span>, 1284 (1990). That is to say, in the vast majority of cases in which evidence is destroyed by persons who are engaged in illegal conduct, the reason for the destruction is fear that the evidence will fall into the hands of law enforcement. Destruction of evidence issues probably occur most frequently in drug cases because drugs may be easily destroyed by flushing them down a toilet or rinsing them down a drain. Persons in possession of valuable drugs are unlikely to destroy them unless they fear discovery by the police. Consequently, a rule that precludes the police from making a warrantless entry to prevent the destruction of evidence whenever their conduct causes the exigency would <page-number citation-index="1" label="462">*462</page-number>unreasonably shrink the reach of this well-established exception to the warrant requirement.</p>
<p id="b542-5">Presumably for the purpose of avoiding such a result, the lower courts have held that the police-created exigency doctrine requires more than simple causation, but the lower courts have not agreed on the test to be applied. Indeed, the petition in this case maintains that “[tjhere are currently five different tests being used by the United States Courts of Appeals,” Pet. for Cert. 11, and that some state courts have crafted additional tests, <em>id., </em>at 19-20.</p>
<p id="b542-6">Ill</p>
<p id="b542-7">A</p>
<p id="b542-8">Despite the welter of tests devised by the lower courts, the answer to the question presented in this case follows directly and clearly from the’ principle that permits warrant-less searches in the first place. As previously noted, warrantless searches are allowed when the circumstances make it reasonable, within the meaning of the Fourth Amendment, to dispense with the warrant requirement. Therefore, the answer to the question before us is that the exigent circumstances rule justifies a warrantless search when the conduct of the police preceding the exigency is reasonable in the same sense. Where, as here, the police did not create the exigency by engaging or threatening to engage in conduct that violates the Fourth Amendment, warrantless entry to prevent the destruction of evidence is reasonable and thus allowed.<footnotemark>4</footnotemark></p>
<p id="b542-9">We have taken a similar approach in other cases involving warrantless searches. For example, we have held that law <page-number citation-index="1" label="463">*463</page-number>enforcement officers may seize evidence in plain view, provided that they have not violated the Fourth Amendment in arriving at the spot from which the observation of the evidence is made. See <em>Horton </em>v. <em>California, </em><span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#136" aria-description="Citation for case: Horton v. California">496 U. S. 128, 136-140</a></span> (1990). As we put it in <em><span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/" aria-description="Citation for case: Horton v. California">Horton</a></span>, </em>“[i]t is ... an essential predicate to any valid warrantless seizure of incriminating evidence that the officer did not violate the Fourth Amendment in arriving at the place from which the evidence could be plainly viewed.” <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#136" aria-description="Citation for case: Horton v. California"><em>Id., </em>at 136</a></span>. So long as this prerequisite is satisfied, however, it does not matter that the officer who makes the observation may have gone to the spot from which the evidence was seen with the hope of being able to view and seize the evidence. See <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#138" aria-description="Citation for case: Horton v. California"><em>id., </em>at 138</a></span> (“The fact that an officer is interested in an item of evidence and fully expects to find it in the course of a search should not invalidate its seizure”). Instead, the Fourth Amendment requires only that the steps preceding the seizure be lawful. See <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#136" aria-description="Citation for case: Horton v. California"><em>id., </em>at 136-137</a></span>.</p>
<p id="b543-5">Similarly, officers may seek consent-based encounters if they are lawfully present in the place where the consensual encounter occurs. See <em>INS </em>v. <em>Delgado, </em><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#217" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 217, n. 5</a></span> (1984) (noting that officers who entered into consent-based encounters with employees in a factory building were “lawfully present [in the factory] pursuant to consent or a warrant”). If consent is freely given, it makes no difference that an officer may have approached the person with the hope or expectation of obtaining consent. See <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#216" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><em>id., </em>at 216</a></span> (“While most citizens will respond to a police request, the fact that people do so, and do so without being told they are free not to respond, hardly eliminates the consensual nature of the response”).</p>
<p id="b543-6">B</p>
<p id="b543-7">Some lower courts have adopted a rule that is similar to the one that we recognize today. See <em>United States </em>v. <em>MacDonald, </em><span class="citation" data-id="9480901"><a href="/opinion/550088/united-states-v-errol-macdonald/#772" aria-description="Citation for case: United States v. Errol MacDonald">916 F. 2d 766, 772</a></span> (CA2 1990) (en banc) (law enforcement officers “do not impermissibly create exigent circum<page-number citation-index="1" label="464">*464</page-number>stances” when they “act in an entirely lawful manner”); <em>State </em>v. <em>Robinson, </em><span class="citation" data-id="9658187"><a href="/opinion/1603113/state-v-robinson/#32" aria-description="Citation for case: State v. Robinson">2010 WI 80, ¶ 32</a></span>, <span class="citation" data-id="9658187"><a href="/opinion/1603113/state-v-robinson/#326" aria-description="Citation for case: State v. Robinson">327 Wis. 2d 302, 326-328</a></span>, <span class="citation" data-id="9658187"><a href="/opinion/1603113/state-v-robinson/#475" aria-description="Citation for case: State v. Robinson">786 N. W. 2d 463, 475-476</a></span> (2010). But others, including the Kentucky Supreme Court, have imposed additional requirements that are unsound and that we now reject.</p>
<p id="b544-5"><em>Bad faith. Some </em>courts, including the Kentucky Supreme Court, ask whether law enforcement officers “ ‘deliberately created the exigent circumstances with the bad faith intent to avoid the warrant requirement.’ ” <span class="citation" data-id="5108786"><a href="/opinion/5280908/king-v-commonwealth/" aria-description="Citation for case: King v. Commonwealth">302 S. W. 3d, at 656</a></span> (quoting <em>Gould, </em><span class="citation" data-id="9496885"><a href="/opinion/785789/united-states-v-kelly-donald-gould/#590" aria-description="Citation for case: United States v. Kelly Donald Gould">364 F. 3d, at 590</a></span>); see also, <em>e. g., Chambers, </em>395 F. 3d, at 566; <em>United States </em>v. <em>Socey, </em><span class="citation" data-id="506171"><a href="/opinion/506171/united-states-v-robert-socey-and-daniel-socey/#1448" aria-description="Citation for case: United States v. Robert Socey and Daniel Socey">846 F. 2d 1439, 1448</a></span> (CADC 1988); <em>United States </em>v. <em>Rengifo, </em><span class="citation" data-id="8963819"><a href="/opinion/8972232/united-states-v-rengifo/#804" aria-description="Citation for case: United States v. Rengifo">858 F. 2d 800, 804</a></span> (CA1 1988).</p>
<p id="b544-6">This approach is fundamentally inconsistent with our Fourth Amendment jurisprudence. “Our cases have repeatedly rejected” a subjective approach, asking only whether “the circumstances, viewed <em>objectively, </em>justify the action.” <em>Brigham City, </em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#404" aria-description="Citation for case: Brigham City v. Stuart">547 U. S., at 404</a></span> (alteration and internal quotation marks omitted); see also <em>Fisher, </em><span class="citation" data-id="9413217"><a href="/opinion/1755/michigan-v-fisher/#47" aria-description="Citation for case: Michigan v. Fisher">558 U. S., at 47-49</a></span>. Indeed, we have never held, outside limited contexts such as an “inventory search or administrative inspection . . . , that an officer’s motive invalidates objectively justifiable behavior under the Fourth Amendment.” <em>Whren </em>v. <em>United States, </em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#812" aria-description="Citation for case: Whren v. United States">517 U. S. 806, 812</a></span> (1996); see also <span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#405" aria-description="Citation for case: Brigham City v. Stuart"><em>Brigham City, supra, </em>at 405</a></span>.</p>
<p id="b544-7">The reasons for looking to objective factors, rather than subjective intent, are clear. Legal tests based on reasonableness are generally objective, and this Court has long taken the view that “evenhanded law enforcement is best achieved by the application of objective standards of conduct, rather than standards that depend upon the subjective state of mind of the officer.” <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#138" aria-description="Citation for case: Horton v. California"><em>Horton, supra, </em>at 138</a></span>.</p>
<p id="b544-8"><em>Reasonable foreseeability. </em>Some courts, again including the Kentucky Supreme Court, hold that police may not rely on an exigency if “‘it was reasonably foreseeable that the investigative tactics employed by the police would create the <page-number citation-index="1" label="465">*465</page-number>exigent circumstances.’” <span class="citation" data-id="5108786"><a href="/opinion/5280908/king-v-commonwealth/" aria-description="Citation for case: King v. Commonwealth">302 S. W. 3d, at 656</a></span> (quoting <em>Mann </em>v. <em>State, </em><span class="citation" data-id="9756543"><a href="/opinion/2342951/mann-v-state/#172" aria-description="Citation for case: Mann v. State">357 Ark. 159, 172</a></span>, <span class="citation" data-id="9756543"><a href="/opinion/2342951/mann-v-state/#834" aria-description="Citation for case: Mann v. State">161 S. W. 3d 826, 834</a></span> (2004)); see also, <em>e. g., United States </em>v. <em>Mowatt, </em><span class="citation" data-id="1024793"><a href="/opinion/1024793/united-states-v-mowatt/#402" aria-description="Citation for case: United States v. Mowatt">513 F. 3d 395, 402</a></span> (CA4 2008). Courts applying this test have invalidated warrantless home searches on the ground that it was reasonably foreseeable that police officers, by knocking on the door and announcing their presence, would lead a drug suspect to destroy evidence. See, <span class="citation" data-id="1024793"><a href="/opinion/1024793/united-states-v-mowatt/#402" aria-description="Citation for case: United States v. Mowatt"><em>e. g., id., </em>at 402-403</a></span>; <span class="citation" data-id="5108786"><a href="/opinion/5280908/king-v-commonwealth/#656" aria-description="Citation for case: King v. Commonwealth">302 S. W. 3d, at 656</a></span>.</p>
<p id="b545-5">Contrary to this reasoning, however, we have rejected the notion that police may seize evidence without a warrant only when they come across the evidence by happenstance. In <em><span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/" aria-description="Citation for case: Horton v. California">Horton</a></span>, </em>as noted, we held that the police may seize evidence in plain view even though the officers may be “interested in an item of evidence and fully expec[t] to find it in the course of a search.” <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#138" aria-description="Citation for case: Horton v. California">496 U. S., at 138</a></span>.</p>
<p id="b545-6">Adoption of a reasonable foreseeability test would also introduce an unacceptable degree of unpredictability. For example, whenever law enforcement officers knock on the door of premises occupied by a person who may be involved in the drug trade, there is <em>some </em>possibility that the occupants may possess drugs and may seek to destroy them. Under a reasonable foreseeability test, it would be necessary to quantify the degree of predictability that must be reached before the police-created exigency doctrine comes into play.</p>
<p id="b545-7">A simple example illustrates the difficulties that such an approach would produce. Suppose that the officers in the present case did not smell marijuana smoke and thus knew only that there was a <em>50% </em>chance that the fleeing suspect had entered the apartment on the left rather than the apartment on the right. Under those circumstances, would it have been reasonably foreseeable that the occupants of the apartment on the left would seek to destroy evidence upon learning that the police were at the door? Or suppose that the officers knew only that the suspect had disappeared into one of the apartments on a floor with 3, 5, 10, or even 20 <page-number citation-index="1" label="466">*466</page-number>units? If the police chose a door at random and knocked for the purpose of asking the occupants if they knew a person who fit the description of the suspect, would it have been reasonably foreseeable that the occupants would seek to destroy evidence?</p>
<p id="b546-5">We have noted that “[t]he calculus of reasonableness must embody allowance for the fact that police officers are often forced to make split-second judgments — in circumstances that are tense, uncertain, and rapidly evolving.” <em>Graham </em>v. <em>Connor, </em><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor">490 U. S. 386, 396-397</a></span> (1989). The reasonable foreseeability test would create unacceptable and unwarranted difficulties for law enforcement officers who must make quick decisions in the field, as well as for judges who would be required to determine after the fact whether the destruction of evidence in response to a knock on the door was reasonably foreseeable based on what the officers knew at the time.</p>
<p id="b546-6"><em>Probable cause and time to secure a warrant. </em>Some courts, in applying the police-created exigency doctrine, fault law enforcement officers if, after acquiring evidence that is sufficient to establish probable cause to search particular premises, the officers do not seek a warrant but instead knock on the door and seek either to speak with an occupant or to obtain consent to search. See, <em>e. g., Chambers, supra, </em>at 569 (citing “[t]he failure to seek a warrant in the face of plentiful probable cause” as a factor indicating that the police deliberately created the exigency).</p>
<p id="b546-7">This approach unjustifiably interferes with legitimate law enforcement strategies. There are many entirely proper reasons why police may not want to seek a search warrant as soon as the bare minimum of evidence needed to establish probable cause is acquired. Without attempting to provide a comprehensive list of these reasons, we note a few.</p>
<p id="b546-8">First, the police may wish to speak with the occupants of a dwelling before deciding whether it is worthwhile to seek authorization for a search. They may think that a short and simple conversation may obviate the need to apply for and <page-number citation-index="1" label="467">*467</page-number>execute a warrant. See <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#228" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 228</a></span> (1973). Second, the police may want to ask an occupant of the premises for consent to search because doing so is simpler, faster, and less burdensome than applying for a warrant. A consensual search also “may result in considerably less inconvenience” and embarrassment to the occupants than a search conducted pursuant to a warrant. <em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Ibid.</a></span> </em>Third, law enforcement officers may wish to obtain more evidence before submitting what might otherwise be considered a marginal warrant application. Fourth, prosecutors may wish to wait until they acquire evidence that can justify a search that is broader in scope than the search that a judicial officer is likely to authorize based on the evidence then available. ' And finally, in many cases, law enforcement may not want to execute a search that will disclose the existence of an investigation because doing so may interfere with the acquisition of additional evidence against those already under suspicion or evidence about additional but as yet unknown participants in a criminal scheme.</p>
<p id="b547-5">We have said that “[l]aw enforcement officers are under no constitutional duty to call a halt to criminal investigation the moment they have the minimum evidence to establish probable cause.” <em>Hoffa </em>v. <em>United States, </em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#310" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 310</a></span> (1966). Faulting the police for failing to apply for a search warrant at the earliest possible time after obtaining probable cause imposes a duty that is nowhere to be found in the Constitution.</p>
<p id="b547-6"><em>Standard or good investigative tactics. </em>Finally, some lower court cases suggest that law enforcement officers may be found to have created or manufactured an exigency if the court concludes that the course of their investigation was “contrary to standard or good law enforcement practices (or to the policies or practices of their jurisdictions).” <em>Gould, </em><span class="citation" data-id="9496885"><a href="/opinion/785789/united-states-v-kelly-donald-gould/#591" aria-description="Citation for case: United States v. Kelly Donald Gould">364 F. 3d, at 591</a></span>. This approach fails to provide clear guidance for law enforcement officers and authorizes courts to make judgments on matters that are the province of those <page-number citation-index="1" label="468">*468</page-number>who are responsible for federal and state law enforcement agencies.</p>
<p id="b548-5">C</p>
<p id="b548-6">Respondent argues for a rule that differs from those discussed above, but his rule is also flawed. Respondent contends that law enforcement officers impermissibly create an exigency when they “engage in conduct that would cause a reasonable person to believe that entry is imminent and inevitable.” Brief for Respondent 24. In respondent’s view, relevant factors include the officers’ tone of voice in announcing their presence and the forcefulness of their knocks. But the ability of law enforcement officers to respond to an exigency cannot turn on such subtleties.</p>
<p id="b548-7">Police officers may have a very good reason to announce their presence loudly and to knock on the door with some force. A forceful knock may be necessary to alert the occupants that someone is at the door. Cf. <em>United States </em>v. <em>Banks, </em><span class="citation" data-id="131146"><a href="/opinion/131146/united-states-v-banks/#33" aria-description="Citation for case: United States v. Banks">540 U. S. 31, 33</a></span> (2003) (Police “rapped hard enough on the door to be heard by officers at the back door” and announced their presence, but defendant “was in the shower and testified that he heard nothing”). Furthermore, unless police officers identify themselves loudly enough, occupants may not know who is at their doorstep. Officers are permitted — indeed, encouraged — to identify themselves to citizens, and “in many circumstances this is cause for assurance, not discomfort.” <em>United States </em>v. <em>Drayton, </em><span class="citation" data-id="9434276"><a href="/opinion/121153/united-states-v-drayton/#204" aria-description="Citation for case: United States v. Drayton">536 U. S. 194, 204</a></span> (2002). Citizens who are startled by an unexpected knock on the door or by the sight of unknown persons in plain clothes on their doorstep may be relieved to learn that these persons are police officers. Others may appreciate the opportunity to make an informed decision about whether to answer the door to the police.</p>
<p id="b548-8">If respondent’s test were adopted, it would be extremely difficult for police officers to know how loudly they may announce their presence or how forcefully they may knock on a door without running afoul of the police-created exigency <page-number citation-index="1" label="469">*469</page-number>rule. And in most cases, it would be nearly impossible for a court to determine whether that threshold had been passed. The Fourth Amendment does not require the nebulous and impractical test that respondent proposes.<footnotemark>5</footnotemark></p>
<p id="b549-4">D</p>
<p id="b549-5">For these reasons, we conclude that the exigent circumstances rule applies when the police do not gain entry to premises by means of an actual or threatened violation of the Fourth Amendment. This holding provides ample protection for the privacy rights that the Amendment protects.</p>
<p id="b549-6">When law enforcement officers who are not armed with a warrant knock on a door, they do no more than any private citizen might do. And whether the person who knocks on the door and requests the opportunity to speak is a police officer or a private citizen, the occupant has no obligation to <page-number citation-index="1" label="470">*470</page-number>open the door or to speak. Cf. <em>Florida </em>v. Royer, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#497" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 497-498</a></span> (1983) (“[H]e may decline to listen to the questions at all and may go on his way”). When the police knock on a door but the occupants choose not to respond or to speak, “the investigation will have reached a conspicuously low point,” and the occupants “will have the kind of warning that even the most elaborate security system cannot provide.” <em>Chambers, </em>395 F. 3d, at 577 (Sutton, J., dissenting). And even if an occupant chooses to open the door and speak with the officers, the occupant need not allow the officers to enter the premises and may refuse to answer any questions at any time.</p>
<p id="b550-5">Occupants who choose not to stand on their constitutional rights but instead elect to attempt to destroy evidence have only themselves to blame for the warrantless exigent circumstances search that may ensue.</p>
<p id="b550-6">IV</p>
<p id="b550-7">We now apply our interpretation of the police-created exigency doctrine to the facts of this ease.</p>
<p id="b550-8">A</p>
<p id="b550-9">We need not decide whether exigent circumstances existed in this case. Any warrantless entry based on exigent circumstances must, of course, be supported by a genuine exigency. See <em>Brigham City, </em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#406" aria-description="Citation for case: Brigham City v. Stuart">547 U. S., at 406</a></span>. The trial court and the Kentucky Court of Appeals found that there was a real exigency in this case, but the Kentucky Supreme Court expressed doubt on this issue, observing that there was “certainly some question as to whether the sound of persons moving [inside the apartment] was sufficient to establish that evidence was being destroyed.” <span class="citation" data-id="5108786"><a href="/opinion/5280908/king-v-commonwealth/#655" aria-description="Citation for case: King v. Commonwealth">302 S. W. 3d, at 655</a></span>. The Kentucky Supreme Court “assum[ed] for the purpose of argument that exigent circumstances existed,” <em>ibid., </em>and it held that the police had impermissibly manufactured the exigency.</p>
<p id="b551-4"><page-number citation-index="1" label="471">*471</page-number>We, too, assume for purposes of argument that an exigency existed. We decide only the question on which the Kentucky Supreme Court ruled and on which we granted certiorari: Under what circumstances do police impermissibly create an exigency? Any question about whether an exigency actually existed is better addressed by the Kentucky Supreme Court on remand. See <em>Kirk </em>v. <em>Louisiana, </em><span class="citation" data-id="121167"><a href="/opinion/121167/kirk-v-louisiana/#638" aria-description="Citation for case: Kirk v. Louisiana">536 U. S. 635, 638</a></span> (2002) <em>(per curiam) </em>(reversing state-court judgment that exigent circumstances were not required for warrantless home entry and remanding for state court to determine whether exigent circumstances were present).</p>
<p id="b551-5">B</p>
<p id="b551-6">In this case, we see no evidence that the officers either violated the Fourth Amendment or threatened to do so prior to the point when they entered the apartment. Officer Cobb testified without contradiction that the officers “banged on the door as loud as [they] could” and announced either “ ‘Police, police, police’” or “‘This is the police.’” App. 22-23. This conduct was entirely consistent with the Fourth Amendment, and we are aware of no other evidence that might show that the officers either violated the Fourth Amendment or threatened to do so (for example, by announcing that they would break down the door if the occupants did not open the door voluntarily).</p>
<p id="b551-7">Respondent argues that the officers “demanded” entry to the apartment, but he has not pointed to any evidence in the record that supports this assertion. He relies on a passing statement made by the trial court in its opinion denying respondent’s motion to suppress. See App. to Pet. for Cert. 3a-4a. In recounting the events that preceded the search, the judge wrote that the officers “banged on the door of the apartment on the back left of the breezeway identifying themselves as police officers and <em>demanding </em>that the door be opened by the persons inside.” <em>Ibid, </em>(emphasis added and deleted). However, at a later point in this opinion, the <page-number citation-index="1" label="472">*472</page-number>judge stated that the officers “initially knock[ed] on the door of the apartment unit and await[ed] the response or consensual entry.” <em><span class="citation" data-id="121167"><a href="/opinion/121167/kirk-v-louisiana/" aria-description="Citation for case: Kirk v. Louisiana">Id.,</a></span> </em>at 9a. This later statement is consistent with the testimony at the suppression hearing and with the findings of the state appellate courts. See <span class="citation" data-id="5108786"><a href="/opinion/5280908/king-v-commonwealth/#651" aria-description="Citation for case: King v. Commonwealth">302 S. W. 3d, at 651</a></span> (The officers “knocked loudly on the back left apartment door and announced 'police’”); App. to Pet. for Cert. 14a (The officers “knock[ed] on the door and announc[ed] themselves as police”); App. 22-24. There is no evidence of a “demand” of any sort, much less a demand that amounts to a threat to violate the Fourth Amendment. If there is contradictory evidence that has not been brought to our attention, the state court may elect to address that matter on remand.</p>
<p id="b552-5">Finally, respondent claims that the officers “explained to [the occupants that the officers] were going to make entry inside the apartment,” <em>id., </em>at 24, but the record is clear that the officers did not make this statement until after the exigency arose. As Officer Cobb testified, the officers “knew that there was possibly something that was going to be destroyed inside the apartment,” and <em>“/aJt that point, . . . </em>[they] explained . . . [that they] were going to make entry.” <em>Ibid, </em>(emphasis added). Given that this announcement was made <em>after </em>the exigency arose, it could not have created the exigency.</p>
<p id="b552-6">* * *</p>
<p id="b552-7">Like the court below, we assume for purposes of argument that an exigency existed. Because the officers in this case did not violate or threaten to violate the Fourth Amendment prior to the exigency, we hold that the exigency justified the warrantless search of the apartment.</p>
<p id="b552-8">The judgment of the Kentucky Supreme Court is reversed, and the ease is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b552-9">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b537-9"> Respondent’s girlfriend leased the apartment, but respondent stayed there part of the time, and his child lived there. Based on these facts, Kentucky conceded in state court that respondent has Fourth Amendment standing to challenge the search. See App. to Pet. for Cert. 7a; see also <span class="citation" data-id="5108786"><a href="/opinion/5280908/king-v-commonwealth/#652" aria-description="Citation for case: King v. Commonwealth">302 S. W. 3d 649,652</a></span> (Ky. 2010).</p>
</footnote>
<footnote label="2">
<p id="b538-8"> After we granted certiorari, respondent filed a motion to dismiss the petition as improvidently granted, which we denied. <span class="citation multiple-matches"><a href="/c/U.%20S./562/1042/">562 U. S. 1042</a></span> (2010). Respondent’s principal argument was that the case was moot because, after the Kentucky Supreme Court reversed his conviction, the Circuit Court dismissed the charges against him. Respondent’s argument is foreclosed by <em>United States </em>v. <em>Villamonte-Marquez, </em><span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/#581" aria-description="Citation for case: United States v. Villamonte-Marquez">462 U. S. 579, 581, n. 2</a></span> (1983). As we explained in <em><span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/" aria-description="Citation for case: United States v. Villamonte-Marquez">Villamonte-Marquez</a></span>, </em>our reversal of the Kentucky Supreme Court’s decision “would reinstate the judgment of conviction and the sentence entered” by the Circuit Court. <em><span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/" aria-description="Citation for case: United States v. Villamonte-Marquez">Ibid.</a></span> </em>The absence <page-number citation-index="1" label="459">*459</page-number>of an indictment does not change matters. See <em><span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/" aria-description="Citation for case: United States v. Villamonte-Marquez">ibid.</a></span> </em>(“Upon respondents’ conviction and sentence, the indictment that was returned against them was merged into their convictions and sentences”).</p>
</footnote>
<footnote label="3">
<p id="b540-6"> Preventing the destruction of evidence may also justify dispensing with Fourth Amendment requirements in other contexts. See, e. <em>g., Richards </em>v. <em>Wisconsin, </em><span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/#395" aria-description="Citation for case: Richards v. Wisconsin">520 U. S. 385, 395-396</a></span> (1997) (failure to comply with the knock-and-announee requirement was justified because “the circumstances . . . show[ed] that the officers had a reasonable suspicion that [a suspect] might destroy evidence if given further opportunity to do so”); <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 770-771</a></span> (1966) (warrantless testing for blood-alcohol content was justified based on potential destruction of evidence); cf. <em>United States </em>v. <em>Banks, </em><span class="citation" data-id="131146"><a href="/opinion/131146/united-states-v-banks/#37" aria-description="Citation for case: United States v. Banks">540 U. S. 31, 37-40</a></span> (2003) (15 to 20 seconds was a reasonable time for officers to wait after knocking and announcing their presence where there was a risk that suspect would dispose of cocaine).</p>
</footnote>
<footnote label="4">
<p id="b542-10"> There is a strong argument to be made that, at least’in most circumstances, the exigent circumstances rule should not apply where the police, without a warrant or any legally sound basis for a warrantless entry, threaten that they will enter without permission unless admitted. In this case, however, no such actual threat was made, and therefore we have no need to reach that question.</p>
</footnote>
<footnote label="5">
<p id="b549-7"> Contrary to respondent’s argument, see Brief for Respondent 13-18, <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948), does not require affirmance in this case. In <em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson</a></span>, </em>officers noticed the smell of burning opium emanating from a hotel room. They then knocked on the door and demanded entry. Upon seeing that Johnson was the only occupant of the room, they placed her under arrest, searched the room, and discovered opium and drug paraphernalia. <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#11" aria-description="Citation for case: Johnson v. United States"><em>Id., </em>at 11</a></span>.</p>
<p id="b549-8">Defending the legality of the search, the Government attempted to justify the warrantless search of the room as a valid search incident to a lawful arrest. See Brief for United States in <em>Johnson </em>v. <em>United States, </em>O. T. 1947, No. 329, pp. 13, 16, 36. The Government did not contend that the officers entered the room in order to prevent the destruction of evidence. Although the officers said that they heard a “‘shuffling’” noise inside the room after they knocked on the door, <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#12" aria-description="Citation for case: Johnson v. United States">333 U. S., at 12</a></span>, the Government did not claim that this particular noise was a noise that would have led a reasonable officer to think that evidence was about to be destroyed. Thus, <em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson</a></span> </em>is simply not a case about exigent circumstances. See <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States"><em>id., </em>at 14-15</a></span> (noting that if “exceptional circumstances” existed — for example, if a “suspect was fleeing or likely to take flight” or if “evidence or contraband was threatened with removal or destruction” — then “it may be contended that a magistrate’s warrant for search may be dispensed with”).</p>
</footnote>
</opinion>
```

---
