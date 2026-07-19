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

## GROUP: content/cases/Lo-Ji Sales, Inc. v. New York.md  (`case`, 6 assertions)

### content_page

```
---
title: "Lo-Ji Sales, Inc. v. New York"
type: case
citation: "442 U.S. 319 (1979)"
parallel_cite: "99 S. Ct. 2319; 60 L. Ed. 2d 920; 5 Media L. Rep. (BNA) 1177"
neutral_cite: 1979 U.S. LEXIS 107
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-06-11
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1979-06-11
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Lo-Ji Sales, Inc. v. New York"
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110100/lo-ji-sales-inc-v-new-york/"
  cluster_id: 110100
  opinion_id: 110100
  identity_checked: true
homes:
  - page: "[[The Neutral and Detached Magistrate]]"
    role: "Key — Progeny / Refinement"
  - page: "[[The Good-Faith Exception]]"
    role: "Related (cross-doctrine)"
related: ["[[Coolidge v. New Hampshire]]", "[[Groh v. Ramirez]]", "[[United States v. Leon]]"]
aliases: ["Lo-Ji Sales", "Lo-Ji"]
tags: ["case", "fourth-amendment", "warrant-requirement", "neutral-and-detached-magistrate", "general-warrant", "particularity"]
holding: "A magistrate who abandons the neutral-and-detached role — here the Town Justice joined and effectively led the search party, conducting…"
lake:
  record_id: "Lo-Ji Sales, Inc. v. New York"
  status: verified
  projected_at: 2026-07-06
---

# Lo-Ji Sales, Inc. v. New York

*442 U.S. 319 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Town Justice issued a warrant to search an adult bookstore based on two films an investigator said were obscene, but the warrant otherwise left the items to be seized open-ended. The Town Justice then personally accompanied the police to the store and spent hours viewing films and inspecting magazines, deciding on the spot which additional items were obscene and directing officers to seize them and "similar" items.

## Issue
Whether a search conducted under an open-ended warrant is valid where the issuing magistrate abandons his neutral and detached role by joining and directing the search.

## Rule
A warrant-issuing magistrate must remain neutral and detached and may not become part of the search. "The Town Justice did not manifest that neutrality and detachment demanded of a judicial officer when presented with a warrant application for a search and seizure." — 442 U.S. at 326. ^pin-326

Here "He allowed himself to become a member, if not the leader, of the search party which was essentially a police operation. . . . he was not acting as a judicial officer but as an adjunct law enforcement officer." — *Id.* at 327. ^pin-327

## Application
The warrant the Town Justice issued was a forbidden open-ended (general) warrant as to most items, and rather than standing apart from its execution he went to the store and personally conducted a generalized search — viewing materials, deciding what was obscene, and directing the seizures. By making himself a leader of what was essentially a police operation, he forfeited the neutral and detached posture the Fourth Amendment requires of the issuing officer, so the search and seizures were invalid.

## Conclusion
The search violated the Fourth Amendment; the seized materials should have been suppressed. A magistrate who leads the search is no neutral and detached magistrate, and an open-ended warrant is an unconstitutional general warrant.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Lo-Ji* remains a leading illustration of two failures: the loss of the **neutral and detached magistrate** (cf. [[Coolidge v. New Hampshire]]) and the **general-warrant / [[Particularity|particularity]]** defect (cf. [[Groh v. Ramirez]]). On the exclusionary-rule side it marks a boundary of the [[United States v. Leon]] [[The Good-Faith Exception|good-faith exception]] — good faith fails where the issuing magistrate has wholly abandoned the judicial role.

## Appears on
- [[The Neutral and Detached Magistrate]] — *Key — Progeny / Refinement*
- [[The Exclusionary Rule]] — *Related (cross-doctrine)*

## Sources
- *Lo-Ji Sales, Inc. v. New York*, 442 U.S. 319 (1979) — https://www.courtlistener.com/opinion/110100/lo-ji-sales-inc-v-new-york/ — pinpoints: 326, 327.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d77db0201a78680a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "442 U.S. 319 (1979)", "court": "U.S. Supreme Court", "neutral_cite": "1979 U.S. LEXIS 107", "official_citation_present": true, "parallel_cite": "99 S. Ct. 2319; 60 L. Ed. 2d 920; 5 Media L. Rep. (BNA) 1177", "title": "Lo-Ji Sales, Inc. v. New York", "year": "1979"}}
{"assertion_id": "4a242a2f1d1cbf11", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A magistrate who abandons the neutral-and-detached role — here the Town Justice joined and effectively led the search party, conducting…", "title": "Lo-Ji Sales, Inc. v. New York"}}
{"assertion_id": "e3a2b9df1d0244c4", "dimension": "support", "kind": "home_role", "locator": {"home": "The Neutral and Detached Magistrate"}, "payload": {"home": "The Neutral and Detached Magistrate", "role": "Key — Progeny / Refinement", "title": "Lo-Ji Sales, Inc. v. New York"}}
{"assertion_id": "fdde17ccecec2f5d", "dimension": "support", "kind": "home_role", "locator": {"home": "The Good-Faith Exception"}, "payload": {"home": "The Good-Faith Exception", "role": "Related (cross-doctrine)", "title": "Lo-Ji Sales, Inc. v. New York"}}
{"assertion_id": "d2a8e90148599cbd", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Lo-Ji Sales, Inc. v. New York"}}
{"assertion_id": "d9bef53cb407c0dc", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1979-06-11", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Lo-Ji Sales, Inc. v. New York", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Lo-Ji Sales, Inc. v. New York", "varies_by_point": "false"}}
```

### lake record — Lo-Ji Sales, Inc. v. New York

```json
{
  "schema_version": "s2.v1",
  "record_id": "Lo-Ji Sales, Inc. v. New York",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Lo-Ji Sales, Inc. v. New York",
    "case_name_short": "Lo-Ji Sales",
    "case_name_full": "Lo-Ji Sales, Inc. v. New York",
    "input_case_name": "Lo-Ji Sales, Inc. v. New York",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-06-11",
    "year": 1979,
    "docket": null,
    "cluster_id": 110100,
    "lead_opinion_id": 110100,
    "sibling_ids": [
      110100
    ],
    "absolute_url": "/opinion/110100/lo-ji-sales-inc-v-new-york/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9021606,
        "score": 20,
        "case_name": "Lo-Ji Sales, Inc. v. New York"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "442 U.S. 319",
      "volume": "442",
      "reporter": "U.S.",
      "page": "319",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 2319",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2319",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 L. Ed. 2d 920",
        "volume": "60",
        "reporter": "L. Ed. 2d",
        "page": "920",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "5 Media L. Rep. (BNA) 1177",
        "volume": "5",
        "reporter": "Media L. Rep. (BNA)",
        "page": "1177",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 107",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "107",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "442 U.S. 319",
        "volume": "442",
        "reporter": "U.S.",
        "page": "319",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 2319",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2319",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 L. Ed. 2d 920",
        "volume": "60",
        "reporter": "L. Ed. 2d",
        "page": "920",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 107",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "107",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "5 Media L. Rep. (BNA) 1177",
        "volume": "5",
        "reporter": "Media L. Rep. (BNA)",
        "page": "1177",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "442 U.S. 319",
    "official_selection": {
      "court_class": "scotus",
      "selected": "442 U.S. 319",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-326",
      "page": null,
      "quote": "items. ## Issue Whether a search conducted under an open-ended warrant is valid where the issuing magistrate abandons his neutral and detached role by joining and directing the search. ## Rule A warrant-issuing magistrate must remain neutral and detached and may not become part of the search.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-327",
      "page": null,
      "quote": "He allowed himself to become a member, if not the leader, of the search party which was essentially a police operation. . . . he was not acting as a judicial officer but as an adjunct law enforcement officer.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-06-11",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Lo-Ji Sales, Inc. v. New York",
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
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tyrone Melvin Servance, Jr.",
          "cluster_id": 788829,
          "cite": [
            "394 F.3d 222",
            "2005 U.S. App. LEXIS 496",
            "2005 WL 57971"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Luis Perez",
          "cluster_id": 788740,
          "cite": [
            "393 F.3d 457",
            "2004 U.S. App. LEXIS 27095",
            "2004 WL 2998770"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Terry Burton Kimbrough",
          "cluster_id": 707532,
          "cite": [
            "69 F.3d 723",
            "1995 WL 662084"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Noel Lee Decker, Barbara K. Decker",
          "cluster_id": 577733,
          "cite": [
            "956 F.2d 773",
            "1992 U.S. App. LEXIS 1519",
            "1992 WL 19476"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Marsala",
          "cluster_id": 7894150,
          "cite": [
            "216 Conn. 150",
            "579 A.2d 58",
            "1990 Conn. LEXIS 308"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rocky Dale McKeever Brenda Gayle McKeever and Stephen C. Newman",
          "cluster_id": 543608,
          "cite": [
            "906 F.2d 129",
            "1990 U.S. App. LEXIS 11153",
            "1990 WL 90224"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Rodriguez",
          "cluster_id": 3987775,
          "cite": [
            "580 N.E.2d 1127",
            "64 Ohio App. 3d 183",
            "1989 Ohio App. LEXIS 3270"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane1_negative"
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
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
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
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
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
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
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
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Murphy",
          "cluster_id": 111105,
          "cite": [
            "79 L. Ed. 2d 409",
            "104 S. Ct. 1136",
            "465 U.S. 420",
            "1984 U.S. LEXIS 33",
            "52 U.S.L.W. 4246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
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
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'CONNOR v. Ortega",
          "cluster_id": 111851,
          "cite": [
            "94 L. Ed. 2d 714",
            "107 S. Ct. 1492",
            "480 U.S. 709",
            "1987 U.S. LEXIS 1507",
            "1 I.E.R. Cas. (BNA) 1617",
            "55 U.S.L.W. 4405",
            "42 Empl. Prac. Dec. (CCH) 36,891"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Evans",
          "cluster_id": 117905,
          "cite": [
            "131 L. Ed. 2d 34",
            "115 S. Ct. 1185",
            "514 U.S. 1",
            "1995 U.S. LEXIS 1806"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
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
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Andreas",
          "cluster_id": 111013,
          "cite": [
            "77 L. Ed. 2d 1003",
            "103 S. Ct. 3319",
            "463 U.S. 765",
            "1983 U.S. LEXIS 106",
            "51 U.S.L.W. 5157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. MacOn",
          "cluster_id": 111477,
          "cite": [
            "86 L. Ed. 2d 370",
            "105 S. Ct. 2778",
            "472 U.S. 463",
            "1985 U.S. LEXIS 110",
            "53 U.S.L.W. 4783"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lockett v. State",
          "cluster_id": 1148135,
          "cite": [
            "517 So. 2d 1317",
            "1987 WL 778"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Eugene Allen",
          "cluster_id": 768626,
          "cite": [
            "211 F.3d 970",
            "2000 U.S. App. LEXIS 8795",
            "2000 WL 547599"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Abram v. State",
          "cluster_id": 1096122,
          "cite": [
            "606 So. 2d 1015",
            "1992 WL 223914"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cynthia Archer v. John Chisholm",
          "cluster_id": 4422481,
          "cite": [
            "870 F.3d 603",
            "2017 WL 3709149",
            "2017 U.S. App. LEXIS 16493"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. George Wuagneux",
          "cluster_id": 406519,
          "cite": [
            "683 F.2d 1343",
            "1982 U.S. App. LEXIS 16435",
            "11 Fed. R. Serv. 334"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Enrique Espinosa",
          "cluster_id": 493363,
          "cite": [
            "827 F.2d 604",
            "23 Fed. R. Serv. 963",
            "1987 U.S. App. LEXIS 12164"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory James Freeman and David Lyle Boese, A/K/A Dennis Phillip Stevens and David Sterling",
          "cluster_id": 407601,
          "cite": [
            "685 F.2d 942",
            "1982 U.S. App. LEXIS 26042"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe v. Broderick",
          "cluster_id": 2967256,
          "cite": [
            "225 F.3d 440",
            "2000 U.S. App. LEXIS 22165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dracy Lamont McKneely Andrew Ellis, and Alandis Bennett, Also Known as Torjano Akines",
          "cluster_id": 654640,
          "cite": [
            "6 F.3d 1447",
            "1993 U.S. App. LEXIS 26177",
            "1993 WL 403544"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fort Wayne Books, Inc. v. Indiana",
          "cluster_id": 112195,
          "cite": [
            "103 L. Ed. 2d 34",
            "109 S. Ct. 916",
            "489 U.S. 46",
            "1989 U.S. LEXIS 648",
            "57 U.S.L.W. 4180",
            "16 Media L. Rep. (BNA) 1337"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. F. Thomas Little, United States of America v. Peter Chernik, United States of America v. Harold Grutchfield",
          "cluster_id": 447563,
          "cite": [
            "753 F.2d 1420"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Corey Martin",
          "cluster_id": 75908,
          "cite": [
            "297 F.3d 1308",
            "15 Fla. L. Weekly Fed. C 786"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lo-Ji Sales, Inc. v. New York:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110100) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01OTA4ODk2MDAwMDAmcz0yMjI4NTkzJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110100%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110100)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTImcz0xNjMyODY0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110100%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110100)",
        "reviewed": 6,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 6,
        "triage_read": 1,
        "triage_snippet_classified": 5
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110100)",
    "indexed_citing_opinions": 426,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110100,
        "count": 426,
        "count_source": "search"
      }
    ],
    "citation_count": 642,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/lo-ji-sales-inc-v-new-york.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU5NDUxMDkmcz00NTMxNTE1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110100%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110100,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110100,
        "cited_id": 106287,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110100,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110100,
        "cited_id": 106878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110100,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110100,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110100,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110100,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110100,
        "cited_id": 108582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110100,
        "cited_id": 108853,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110100,
        "cited_id": 108854,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110100,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110100,
        "cited_id": 109866,
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
    "date_created": "2026-07-05T10:57:39Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:57:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:57:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:01:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:57:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Lo-Ji Sales, Inc. v. New York

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b367-4">
<span citation-index="1" class="star-pagination" label="321"> 
   *321
   </span>
  Mr. Chief Justice Burger
 </author>
<p id="AaK">
  delivered the opinion of the Court.
 </p>
<p id="b367-5">
  We granted certiorari on claims that the seizure of magazines, films, and other objects from petitioner's bookstore violated guarantees of the First, Fourth, and Fourteenth Amendments. <span class="citation multiple-matches"><a href="/c/U.%20S./439/978/">439 U. S. 978</a></span> (1978).
 </p>
<p id="b367-6">
  I
 </p>
<p id="b367-7">
  On June 20, 1976, an investigator for the New York State Police purchased two reels of film from petitioner’s so-called “adult” bookstore. Upon viewing them, he concluded the films violated New York’s obscenity laws. On June 25, he took them to a Town Justice for a determination whether there was reasonable cause to believe the films violated the state obscenity laws so as to justify a warrant to search the seller’s store. The Town Justice viewed both films in their entirety, and he apparently concluded they were obscene. Based upon an affidavit of the investigator subscribed before the Town Justice after this viewing, a warrant issued authorizing the search of petitioner’s store and the seizure of other copies of the two films exhibited to the Town Justice.
 </p>
<p id="b367-8">
  The investigator’s affidavit also contained an assertion that “similar” films and printed matter portraying similar activities could be found on the premises, and a statement of the affiant’s belief that the items were possessed in violation of the obscenity laws. The warrant application requested that the Town Justice accompany the investigator to petitioner’s store for the execution of the search warrant. The stated purpose was to allow the Town Justice to determine independently if any other items at the store were possessed in violation of law and subject to seizure. The Town Justice agreed. Accordingly, the warrant also contained a recital that authorized the seizure of “[t]he following items that the Court
  <span citation-index="1" class="star-pagination" label="322"> 
   *322
   </span>
  independently [on examination] has determined to be possessed in violation of Article 235 of the Penal Law .
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  However, at the time the Town Justice signed the warrant there were no items listed or described following this statement. As noted earlier, the only “things to be seized” that were described in the warrant were copies of the two films the state investigator had purchased. Before going to the store, the Town Justice also signed a warrant for the arrest of the clerk who operated the store for having sold the two films to the investigator.
 </p>
<p id="b368-6">
  The Town Justice and the investigator enlisted three other State Police investigators, three uniformed State Police officers, and three members of the local prosecutor’s office — a total of 11 — and the search party converged on the bookstore. The store clerk was immediately placed under arrest and advised of the search warrant. He was the only employee present; he was free to continue working in the store to the extent the search permitted, and the store remained open to the public while the party conducted its search mission which was to last nearly six hours.
 </p>
<p id="b368-7">
  The search began in an area of the store which contained booths in which silent films were shown by coin-operated projectors. The clerk adjusted the machines so that the films could be viewed by the Town Justice without coins; it is disputed whether he volunteered or did so under compulsion of the arrest or the warrant. See
  <em>
   infra,
  </em>
  at 329. The Town Justice viewed 23 films for two to three minutes each and, satisfied there was probable cause to believe they were obscene, then ordered the films and the projectors seized.
 </p>
<p id="b368-8">
  The Town Justice next focused on another area containing four coin-operated projectors showing both soundless and sound films. After viewing each film for two to five minutes,
  <span citation-index="1" class="star-pagination" label="323"> 
   *323
   </span>
  again without paying, he ordered them seized along with their projectors.
 </p>
<p id="b369-5">
  The search party then moved to an area in which books and magazines were on display. The magazines were encased in clear plastic or cellophane wrappers which the Town Justice had two police officers remove prior to his examination of the books. Choosing only magazines that did not contain significant amounts of written material, he spent not less than 10 seconds nor more than a minute looking through each one. When he was satisfied that probable cause existed, he immediately ordered the copy which he had reviewed, along with other copies of the same or “similar” magazines, seized. An investigator wrote down the titles of the items seized. All told, 397 magazines were taken.
 </p>
<p id="b369-6">
  The final area searched was one in which petitioner displayed films and other items for sale behind a glass enclosed case. When it was announced that each box of film would be opened, the clerk advised that a picture on the outside of the box was representative of what the film showed. Therefore, if satisfied from the picture that there was probable cause to believe the film in the box was obscene, the Town Justice ordered the seizure of all copies of that film. As with the magazines, an investigator wrote down the titles of the films seized, a total of 431 reels.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  Miscellaneous other items, including business records, were also seized, but no issue concerning them is raised here.
 </p>
<p id="b369-7">
  Throughout the day, two or three marked police cars were parked in front of the store and persons who entered the store were asked to show identification and their names were taken by the police. Not surprisingly, no sales were made during the period the search party was at the store, and no customers or potential customers remained in the store for any appreciable time after becoming aware of the police presence.
 </p>
<p id="b370-4">
<span citation-index="1" class="star-pagination" label="324"> 
   *324
   </span>
  After the search and seizure was completed, the seized items were taken to a State Police barracks where they were inventoried. Each item was then listed on the search warrant, and late the same night the completed warrant was given to the Town Justice. The warrant, which had consisted of 2 pages when he signed it before the search, by late in the day contained 16 pages. It is clear, therefore, that the particular description of “things to be seized” was entered in the document after the seizure and impoundment of the books and other articles.
 </p>
<p id="b370-5">
  The items seized formed the basis for a three-count information charging petitioner with obscenity in the second degree under New York law.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  The counts were based upon the three main groups of items seized: the magazines, Count I; the films for sale to the public, Count II; and the films and coin-operated projectors, Count III. Before trial, petitioner moved to suppress all the evidence upon which the three counts were based because it had been searched for and seized in violation of the First, Fourth, and Fourteenth Amendments. The motion was denied. Petitioner then entered a guilty plea to all three counts and was fined $1,000 on each. Accordingly, the obscenity of the magazines and films having been the subject of a judicial confession, there is no issue of obscenity in the case.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  Only the validity of the warrant and the search and seizure of the property are before us.
 </p>
<p id="b371-4">
<span citation-index="1" class="star-pagination" label="325"> 
   *325
   </span>
  New York permits appeal of a denial of a motion to suppress even after a plea of guilty to the charge. N. Y. Crim. Proc. Law §710.70 (2) (McKinney 1971). Pursuant to this procedure, petitioner appealed and the intermediate appellate court for that judicial district affirmed the convictions. A timely application for leave to appeal to the New York Court of Appeals was denied.
 </p>
<p id="b371-5">
  II
 </p>
<p id="b371-6">
  This search warrant and what followed the entry on petitioner’s premises are reminiscent of the general warrant or writ of assistance of the 18th century against which the Fourth Amendment was intended to protect. See
  <em>
   Marshall
  </em>
  v.
  <em>
   Barlow’s, Inc.,
  </em>
  <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#311" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 311</a></span> (1978);
  <em>
   Stanford
  </em>
  v.
  <em>
   Texas,
  </em>
  <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481</a></span> (1965);
  <em>
   Marcus
  </em>
  v.
  <em>
   Search Warrant,
  </em>
  <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#724" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, 724</a></span> (1961). Except for the specification of copies of the two films previously purchased, the warrant did not purport to “particularly describ[e] . . . the . . . things to be seized.” U. S. Const., Arndt. 4. Based on the conclusory statement of the police investigator that other similarly obscene materials would be found at the store, the warrant left it entirely to the discretion of the officials conducting the search to decide what items were likely obscene and to accomplish their seizure. The Fourth Amendment does not permit such action.
  <em>
   Roaden
  </em>
  v.
  <em>
   Kentucky,
  </em>
  <span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/#502" aria-description="Citation for case: Roaden v. Kentucky">413 U. S. 496, 502</a></span> (1973);
  <em>
   Stanford
  </em>
  v.
  <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas"><em>
   Texas, supra,
  </em>
  at 485</a></span>;
  <em>
   Marcus
  </em>
  v.
  <em>
   Search Warrant, supra,
  </em>
  at 732. Nor does the Fourth Amendment countenance open-ended warrants, to be completed while a search is being conducted and items seized or after the seizure has been carried out.
 </p>
<p id="b371-7">
  This search began when the local justice and his party entered the premises. But at that time there was not sufficient probable cause to pursue a search beyond looking for additional copies of the two specified films, assuming the validity of searching even for those. And the record is clear
  <span citation-index="1" class="star-pagination" label="326"> 
   *326
   </span>
  that the search began and progressed pursuant to the sweeping open-ended authorization in the warrant. It was not limited at the outset as a search for other copies of the two “sample” films; it expanded into a more extensive search because other items were found that the local justice deemed illegal. Therefore, we have no occasion to decide whether in this context the “plain view” doctrine might be applicable. See
  <em>
   Coolidge
  </em>
  v.
  <em>
   New Hampshire,
  </em>
  <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#465" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 465</a></span> (1971).
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  Nor can it reasonably be argued that the search was incident to arrest of the store clerk.
  <em>
   Chimel
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969).
 </p>
<p id="b372-5">
  Ill
 </p>
<p id="b372-6">
  We have repeatedly said that a warrant authorized by a neutral and detached judicial officer is “a more reliable safeguard against improper searches than the hurried judgment of a law enforcement officer ‘engaged in the often competitive enterprise of ferreting out crime.’
  <em>
   Johnson
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948).”
  <em>
   United States
  </em>
  v.
  <em>
   Chadwick,
  </em>
  <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 9</a></span> (1977). See also
  <em>
   Coolidge
  </em>
  v.
  <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#450" aria-description="Citation for case: Coolidge v. New Hampshire"><em>
   New Hampshire, supra,
  </em>
  at 450</a></span>. The State contends that the presence and participation of the Town Justice in the search ensured that no items would be seized absent probable cause to believe they were obscene, and that his presence enabled petitioner to enjoy an immediate adversary hearing on the issue.
 </p>
<p id="b372-7">
  The Town Justice did not manifest that neutrality and detachment demanded of a judicial officer when presented with a warrant application for a search and seizure.
  <em>
   Coolidge
  </em>
  v.
  <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#449" aria-description="Citation for case: Coolidge v. New Hampshire"><em>
   New Hampshire, supra,
  </em>
  at 449</a></span>. We need not question the
  <span citation-index="1" class="star-pagination" label="327"> 
   *327
   </span>
  subjective belief of the Town Justice in the propriety of his actions, but the objective facts of record manifest an erosion of whatever neutral and detached posture existed at the outset. He allowed himself to become a member, if not the leader, of the search party which was essentially a police operation. Once in the store, he conducted a generalized search under authority of an invalid warrant; he was not acting as a judicial officer but as an adjunct law enforcement officer. When he ordered an item seized because he believed it was obscene, he instructed the police officers to seize all “similar” items as well, leaving determination of what was “similar” to the officer’s discretion. Indeed, he yielded to the State Police even the completion of the general provision of the warrant. Though it would not have validated the warrant in any event, the Town Justice admitted at the hearing to suppress evidence that he could not verify that the inventory prepared by the police and presented to him late that evening accurately reflected what he had ordered seized.
 </p>
<p id="b373-5">
  We also cannot accept the State’s contention that it acted in compliance with
  <em>
   Heller
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="9425413"><a href="/opinion/108853/heller-v-new-york/" aria-description="Citation for case: Heller v. New York">413 U. S. 483</a></span> (1973). There, based on police reports of probable violation of state law, a judge viewed a film in a theater as an ordinary paying patron; on the basis of his observation of the entire performance, he then issued a warrant for the seizure of the particular viewed film as evidence. There was no claim that seizure of the single copy impeded the exhibitor’s continued business pending decision on the issue of obscenity. Heller’s claim was that not even one of his films could be lawfully seized without a prior adversary hearing. We rejected that claim and held that seizure on the warrant so issued by a neutral judicial officer on probable cause after viewing one film was constitutionally permissible so long as, on request, a prompt adversary hearing was available on the issue of obscenity. “With such safeguards, we do not perceive that an adversary hearing
  <em>
   prior
  </em>
  to a seizure [of a single sample film] by lawful
  <span citation-index="1" class="star-pagination" label="328"> 
   *328
   </span>
  warrant would materially increase First Amendment protection.”
  <span class="citation" data-id="9425413"><a href="/opinion/108853/heller-v-new-york/#493" aria-description="Citation for case: Heller v. New York"><em>
   Id.,
  </em>
  at 493</a></span>. We also took pains to point out:
 </p>
<blockquote id="b374-5">
  “Courts will scrutinize any large-scale seizure of books, films, or other materials presumptively protected under the First Amendment to be certain that the requirements of
  <em>
   A Quantity of Books
  </em>
  [v.
  <em>
   Kansas,
  </em>
  <span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">378 U. S. 205</a></span> (1964),] and
  <em>
   Marcus
  </em>
  [v.
  <em>
   Search Warrant,
  </em>
  <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717</a></span> (1961),] are fully met. . . .
 </blockquote>
<blockquote id="b374-6">
  “But seizing films to destroy them or to block their distribution or exhibition is a very different matter from seizing a single copy of a film for the
  <em>
   bona fide
  </em>
  purpose of preserving it as evidence in a criminal proceeding, particularly where, as here, there is no showing or pretrial claim that the seizure of the copy prevented continuing exhibition of the film.”
  <em>
   Id.,
  </em>
  at 491-492.
 </blockquote>
<p id="b374-7">
  In contrast, the local justice here undertook to telescope the processes of the application for a warrant, the issuance of the warrant, and its execution. It is difficult to discern when he was acting as a “neutral and detached” judicial officer and when he was one with the police and prosecutors in the executive seizure, and indeed even whether he thought he was conducting,
  <em>
   ex parte,
  </em>
  the “prompt” postseizure hearings on obscenity called for by
  <span class="citation" data-id="9425413"><a href="/opinion/108853/heller-v-new-york/#492" aria-description="Citation for case: Heller v. New York"><em>
   Heller, supra,
  </em>
  at 492</a></span>.
  <em>
   <span class="citation" data-id="9425413"><a href="/opinion/108853/heller-v-new-york/" aria-description="Citation for case: Heller v. New York">Heller</a></span>
  </em>
  does not permit the kind of activities revealed by this record.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
</p>
<p id="b374-8">
  IV
 </p>
<p id="b374-9">
  Perhaps anticipating our disposition of the case, the State
  <span citation-index="1" class="star-pagination" label="329"> 
   *329
   </span>
  raises a different theory from the one advanced in its opposition to the petition for certiorari and on which it had relied in the state courts. The suggestion is that by virtue of its display of the items at issue to the general public in areas of its store open to them, petitioner had no legitimate expectation of privacy against governmental intrusion, see
  <em>
   Rakas
  </em>
  v.
  <em>
   Illinois,
  </em>
  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978), and that accordingly no warrant was needed. But there is no basis for the notion that because a retail store invites the public to enter, it consents to wholesale searches and seizures that do not conform to Fourth Amendment guarantees. See
  <em>
   Lewis
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/#211" aria-description="Citation for case: Lewis v. United States">385 U. S. 206, 211</a></span> (1966). The Town Justice viewed the films, not as a customer, but without the payment a member of the public would be required to make. Similarly, in examining the books and in the manner of viewing the containers in which the films were packaged for sale, he was not seeing them as a customer would ordinarily see them.
 </p>
<p id="b375-5">
  Any suggestion that petitioner through its clerk consented to the sweeping search also comes too late. After Lo-Ji’s agent was placed under arrest and was aware of the presumed authority of the search warrant, his conduct complying with official requests cannot, on this record, be considered free and voluntary. Any “consent” given in the face of “colorably lawful coercion” cannot validate the illegal acts shown here.
  <em>
   Bumper
  </em>
  v.
  <em>
   North Carolina,
  </em>
  <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#549" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543, 549-550</a></span> (1968). Our society is better able to tolerate the admittedly pornographic business of petitioner than a return to the general warrant era; violations of law must be dealt with within the framework of constitutional guarantees.
 </p>
<p id="b375-6">
  The judgment of the Appellate Term of the Supreme Court of the State of New York for the Ninth and Tenth Judicial Districts is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.
 </p>
<p id="b375-7">
<em>
   Reversed and
  </em>
  remanded.
 </p>






<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b368-9">
   New York Penal Law § 235.00 (McKinney Supp. 1978-1979) is the definitional section of the State’s obscenity law. Petitioner was later charged with obscenity in the second degree, § 235.05. See n. 3,
   <em>
    infra.
   </em>
</p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b369-8">
   The State’s brief asserts approximately 474 films were taken, but from the inventory filed in the case it appears the number was 431.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b370-6">
   New York Penal Law § 235.05 (McKinney Supp. 1978-1979) defines obscenity in the second degree as follows:
  </p>
<blockquote id="b370-7">
   “A person is guilty of obscenity in the second degree when, knowing its content and character, he:
  </blockquote>
<blockquote id="b370-8">
   “1. Promotes, or possesses with intent to promote, any obscene material . . . .”
  </blockquote>
<p id="b370-9">
   Section 235.00 of the Penal Law states:
  </p>
<blockquote id="b370-10">
   “4. ‘Promote’ means to manufacture, issue, sell, give, provide, lend, mail, deliver, transfer, transmute, publish, distribute, circulate, disseminate, present, exhibit or advertise, or to offer or agree to do the same.”
  </blockquote>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b370-11">
   The clerk arrested at petitioner’s store entered a guilty plea to a
   <span citation-index="1" class="star-pagination" label="325"> 
    *325
    </span>
   charge of disorderly conduct for selling the two films to the State Police investigator. He did not appeal.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b372-8">
   Of course, contraband may be seized without a warrant under the “plain view” doctrine. See,
   <em>
    e. g., Ker
   </em>
   v.
   <em>
    California,
   </em>
   <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#42" aria-description="Citation for case: Ker v. California">374 U. S. 23, 42-43</a></span> (1963). But we have recognized special constraints upon searches for and seizures of material arguably protected by the First Amendment,
   <em>
    e. g., Heller
   </em>
   v.
   <em>
    New York,
   </em>
   <span class="citation" data-id="9425413"><a href="/opinion/108853/heller-v-new-york/" aria-description="Citation for case: Heller v. New York">413 U. S. 483</a></span> (1973);
   <em>
    Marcus
   </em>
   v.
   <em>
    Search Warrant,
   </em>
   <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#731" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, 731-732</a></span> (1961); materials normally may not be seized on the basis of alleged obscenity without a warrant.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b374-10">
   Wc do not suggest, of course, that a “neutral and detached magistrate/’
   <em>
    Shadwick
   </em>
   v.
   <em>
    Tampa,
   </em>
   <span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/#350" aria-description="Citation for case: Shadwick v. City of Tampa">407 U. S. 345, 350</a></span> (1972), loses his character as such merely because he leaves his regular office in order to make himself readily available to law enforcement officers who may wish to seek the issuance of warants by him. For example, in
   <em>
    <span class="citation" data-id="9425413"><a href="/opinion/108853/heller-v-new-york/" aria-description="Citation for case: Heller v. New York">Heller</a></span>,
   </em>
   the judge signed the search warrant for the seizure of the film in the theater itself. But as we have just pointed out,
   <em>
    <span class="citation" data-id="9425413"><a href="/opinion/108853/heller-v-new-york/" aria-description="Citation for case: Heller v. New York">Heller</a></span>
   </em>
   cannot control this case where the local Town Justice undertook not merely to issue a warrant, but to participate with the police and prosecutors in its execution.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Lynumn v. Illinois.md  (`case`, 5 assertions)

### content_page

```
---
title: "Lynumn v. Illinois"
type: case
citation: "372 U.S. 528 (1963)"
parallel_cite: "83 S. Ct. 917; 9 L. Ed. 2d 922"
neutral_cite: 1963 U.S. LEXIS 1907
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1963
date_decided: 1963-03-25
docket: 9
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1963-03-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Lynumn v. Illinois
  varies_by_point: false
  scope_note: "Good law; a leading totality-of-circumstances coercion case — threats to cut off welfare aid and take a suspect's children render a confession involuntary."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106558/lynumn-v-illinois/"
  cluster_id: 106558
  opinion_id: 106558
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brown v. Mississippi]]", "[[Chambers v. Florida]]", "[[Spano v. New York]]", "[[Ashcraft v. Tennessee]]"]
aliases: []
tags: ["case", "fifth-amendment", "fourteenth-amendment", "confessions", "voluntariness", "due-process", "coercion"]
holding: "A confession is involuntary and coerced where police obtain it by threatening that the suspect will lose state financial aid for her children and have her children taken away unless she cooperates, given to a person with no prior criminal experience, alone and encircled by officers."
lake:
  record_id: Lynumn v. Illinois
  status: verified
  projected_at: 2026-07-06
---

# Lynumn v. Illinois

*372 U.S. 528 (1963)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Lynumn was arrested in her apartment on a charge of selling marijuana. Three police officers and an informer who had purportedly "set her up" encircled her, and the officers told her that state financial aid (ADC) for her infant children would be cut off and her children taken from her if she did not "cooperate." She had no prior experience with the criminal law and no friend or adviser present. She then made an oral confession, which was admitted at her bench trial.

## Issue
Whether a confession obtained after police threaten that the suspect will lose state aid for, and custody of, her children unless she cooperates is voluntary under the Due Process Clause.

## Rule
No — such a confession is coerced. "It is thus abundantly clear that the petitioner's oral confession was made only after the police had told her that state financial aid for her infant children would be cut off, and her children taken from her, if she did not 'cooperate.' . . . We think it clear that a confession made under such circumstances must be deemed not voluntary, but coerced. That is the teaching of our cases. We have said that the question in [each] case is whether the defendant's will was overborne at the time he confessed." — 372 U.S. at 534. ^pin-534

If the will was overborne, "the confession cannot be deemed 'the product of a rational intellect and a free will.'" — *Id.* (quoting *Blackburn v. Alabama*, 361 U.S. 199, 208 (1960)). ^pin-534a

## Application
On these facts the totality of circumstances overbore Lynumn's will: the threat to terminate aid for and remove her children, made by three officers and the informer who had framed her, to a person with no criminal-law experience and no adviser present, who had no reason to doubt the police could carry out the threats. The State conceded the circumstances had an "impellingly coercive" effect. Because her conviction rested in part on that coerced confession, it could not stand.

## Conclusion
The confession was coerced and involuntary; the judgment of conviction was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Lynumn* is a frequently cited totality-of-circumstances coercion case in the due-process line anchored by [[Brown v. Mississippi]] and [[Chambers v. Florida]], alongside the psychological-coercion analysis of [[Spano v. New York]] and the relentless-interrogation analysis of [[Ashcraft v. Tennessee]].

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Lynumn v. Illinois*, 372 U.S. 528 (1963) — https://www.courtlistener.com/opinion/106558/lynumn-v-illinois/ — pinpoint: 534.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "337f1add5c9bcf17", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "372 U.S. 528 (1963)", "court": "U.S. Supreme Court", "neutral_cite": "1963 U.S. LEXIS 1907", "official_citation_present": true, "parallel_cite": "83 S. Ct. 917; 9 L. Ed. 2d 922", "title": "Lynumn v. Illinois", "year": "1963"}}
{"assertion_id": "6d005dd2040fac1f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A confession is involuntary and coerced where police obtain it by threatening that the suspect will lose state financial aid for her children and have her children taken away unless she cooperates, given to a person with no prior criminal experience, alone and encircled by officers.", "title": "Lynumn v. Illinois"}}
{"assertion_id": "b22dd23b45be33aa", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Progeny / Refinement", "title": "Lynumn v. Illinois"}}
{"assertion_id": "7090df8cc73ceba4", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1963-03-25", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Lynumn v. Illinois", "field_i_validity": "good_law", "scope_note": "Good law; a leading totality-of-circumstances coercion case — threats to cut off welfare aid and take a suspect's children render a confession involuntary.", "title": "Lynumn v. Illinois", "varies_by_point": "false"}}
{"assertion_id": "fe4dccf890ae3640", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Lynumn v. Illinois"}}
```

### lake record — Lynumn v. Illinois

```json
{
  "schema_version": "s2.v1",
  "record_id": "Lynumn v. Illinois",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Lynumn v. Illinois",
    "case_name_short": "Lynumn",
    "case_name_full": "Lynumn v. Illinois",
    "input_case_name": "Lynumn v. Illinois",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1963-03-25",
    "year": 1963,
    "docket": "9",
    "cluster_id": 106558,
    "lead_opinion_id": 106558,
    "sibling_ids": [
      106558
    ],
    "absolute_url": "/opinion/106558/lynumn-v-illinois/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "372 U.S. 528",
      "volume": "372",
      "reporter": "U.S.",
      "page": "528",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "83 S. Ct. 917",
        "volume": "83",
        "reporter": "S. Ct.",
        "page": "917",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "9 L. Ed. 2d 922",
        "volume": "9",
        "reporter": "L. Ed. 2d",
        "page": "922",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1963 U.S. LEXIS 1907",
        "volume": "1963",
        "reporter": "U.S. LEXIS",
        "page": "1907",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "372 U.S. 528",
        "volume": "372",
        "reporter": "U.S.",
        "page": "528",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 S. Ct. 917",
        "volume": "83",
        "reporter": "S. Ct.",
        "page": "917",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "9 L. Ed. 2d 922",
        "volume": "9",
        "reporter": "L. Ed. 2d",
        "page": "922",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1963 U.S. LEXIS 1907",
        "volume": "1963",
        "reporter": "U.S. LEXIS",
        "page": "1907",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "372 U.S. 528",
    "official_selection": {
      "court_class": "scotus",
      "selected": "372 U.S. 528",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-534",
      "page": null,
      "quote": "She had no prior experience with the criminal law and no friend or adviser present. She then made an oral confession, which was admitted at her bench trial. ## Issue Whether a confession obtained after police threaten that the suspect will lose state aid for, and custody of, her children unless she cooperates is voluntary under the Due Process Clause. ## Rule No \u2014 such a confession is coerced.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-534a",
      "page": null,
      "quote": "the confession cannot be deemed 'the product of a rational intellect and a free will.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1963-03-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Lynumn v. Illinois",
    "varies_by_point": false,
    "scope_note": "Good law; a leading totality-of-circumstances coercion case \u2014 threats to cut off welfare aid and take a suspect's children render a confession involuntary.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Vasquez-Santiago",
          "cluster_id": 10133179,
          "cite": [
            "301 Or. App. 90",
            "456 P.3d 270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane1_negative"
      },
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
        "journal_ref": "Lynumn v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jalonte Little v. United States",
          "cluster_id": 3153940,
          "cite": [
            "125 A.3d 1119",
            "2015 D.C. App. LEXIS 526"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane1_negative"
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
        "journal_ref": "Lynumn v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Maine v. William A. Wiley",
          "cluster_id": 2680025,
          "cite": [
            "2013 ME 30",
            "61 A.3d 750",
            "2013 WL 979505",
            "2013 Me. LEXIS 30"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane1_negative"
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
        "journal_ref": "Lynumn v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gonzalez",
          "cluster_id": 1888318,
          "cite": [
            "986 A.2d 235",
            "2010 R.I. LEXIS 8",
            "2010 WL 114218"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Michael Eugene Thompson v. Michael W. Haley",
          "cluster_id": 75545,
          "cite": [
            "255 F.3d 1292",
            "2001 U.S. App. LEXIS 14817",
            "2001 WL 747407"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Fiedler v. State",
          "cluster_id": 1533838,
          "cite": [
            "991 S.W.2d 70",
            "1998 WL 1058889"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Russell Ledbetter v. Ron Edwards, Warden",
          "cluster_id": 678531,
          "cite": [
            "35 F.3d 1062",
            "1994 U.S. App. LEXIS 26229",
            "1994 WL 511213"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Miranda v. Arizona",
          "cluster_id": 107252,
          "cite": [
            "16 L. Ed. 2d 694",
            "86 S. Ct. 1602",
            "384 U.S. 436",
            "1966 U.S. LEXIS 2817",
            "10 Ohio Misc. 9",
            "36 Ohio Op. 2d 237",
            "10 A.L.R. 3d 974"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chapman v. California",
          "cluster_id": 107359,
          "cite": [
            "17 L. Ed. 2d 705",
            "87 S. Ct. 824",
            "386 U.S. 18",
            "1967 U.S. LEXIS 2198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brady v. United States",
          "cluster_id": 108137,
          "cite": [
            "25 L. Ed. 2d 747",
            "90 S. Ct. 1463",
            "397 U.S. 742",
            "1970 U.S. LEXIS 45"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Fulminante",
          "cluster_id": 112566,
          "cite": [
            "113 L. Ed. 2d 302",
            "111 S. Ct. 1246",
            "499 U.S. 279",
            "1991 U.S. LEXIS 1854"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Escobedo v. Illinois",
          "cluster_id": 106883,
          "cite": [
            "12 L. Ed. 2d 977",
            "84 S. Ct. 1758",
            "378 U.S. 478",
            "1964 U.S. LEXIS 827",
            "4 Ohio Misc. 197",
            "32 Ohio Op. 2d 31"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
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
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malloy v. Hogan",
          "cluster_id": 106862,
          "cite": [
            "12 L. Ed. 2d 653",
            "84 S. Ct. 1489",
            "378 U.S. 1",
            "1964 U.S. LEXIS 993"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Yarborough v. Alvarado",
          "cluster_id": 134748,
          "cite": [
            "158 L. Ed. 2d 938",
            "124 S. Ct. 2140",
            "541 U.S. 652",
            "2004 U.S. LEXIS 3843"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garrity v. New Jersey",
          "cluster_id": 107336,
          "cite": [
            "17 L. Ed. 2d 562",
            "87 S. Ct. 616",
            "385 U.S. 493",
            "1967 U.S. LEXIS 2882"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haynes v. Washington",
          "cluster_id": 106625,
          "cite": [
            "10 L. Ed. 2d 513",
            "83 S. Ct. 1336",
            "373 U.S. 503",
            "1963 U.S. LEXIS 1439"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
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
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Maury",
          "cluster_id": 2598797,
          "cite": [
            "68 P.3d 1",
            "133 Cal. Rptr. 2d 561",
            "30 Cal. 4th 342"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Spring",
          "cluster_id": 111798,
          "cite": [
            "93 L. Ed. 2d 954",
            "107 S. Ct. 851",
            "479 U.S. 564",
            "1987 U.S. LEXIS 418",
            "55 U.S.L.W. 4162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Dorado",
          "cluster_id": 1177555,
          "cite": [
            "62 Cal. 2d 338",
            "42 Cal. Rptr. 169",
            "398 P.2d 361",
            "1965 Cal. LEXIS 253"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
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
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Terrazas",
          "cluster_id": 2278739,
          "cite": [
            "4 S.W.3d 720",
            "1999 Tex. Crim. App. LEXIS 93",
            "1999 WL 722548"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Juan H. v. Walter Allen III",
          "cluster_id": 790372,
          "cite": [
            "408 F.3d 1262"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Willner v. Committee on Character and Fitness, Appellate Div. of Supreme Court of NY, First Judicial Dept.",
          "cluster_id": 106599,
          "cite": [
            "10 L. Ed. 2d 224",
            "83 S. Ct. 1175",
            "373 U.S. 96",
            "1963 U.S. LEXIS 1616",
            "2 A.L.R. 3d 1254"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Love v. State",
          "cluster_id": 1169864,
          "cite": [
            "457 P.2d 622",
            "1969 Alas. LEXIS 194"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cahill",
          "cluster_id": 1244769,
          "cite": [
            "853 P.2d 1037",
            "5 Cal. 4th 478",
            "20 Cal. Rptr. 2d 582",
            "93 Daily Journal DAR 8304",
            "93 Cal. Daily Op. Serv. 4902",
            "1993 Cal. LEXIS 3087"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cruz",
          "cluster_id": 2584939,
          "cite": [
            "44 Cal. 4th 636",
            "187 P.3d 970",
            "80 Cal. Rptr. 3d 126",
            "2008 Cal. LEXIS 9079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Merrill",
          "cluster_id": 1861263,
          "cite": [
            "274 N.W.2d 99",
            "1978 Minn. LEXIS 1209"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McWhorter",
          "cluster_id": 2590326,
          "cite": [
            "47 Cal. 4th 318",
            "212 P.3d 692",
            "97 Cal. Rptr. 3d 412",
            "2009 Cal. LEXIS 8029"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Smith",
          "cluster_id": 2632408,
          "cite": [
            "150 P.3d 1224",
            "54 Cal. Rptr. 3d 245",
            "40 Cal. 4th 483",
            "2007 Cal. Daily Op. Serv. 1275",
            "2007 Daily Journal DAR 1761",
            "2007 Cal. LEXIS 749"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Frank M. Miller, Jr. v. Peter J. Fenton, Superintendent, Rahway State Prison, Irwin I. Kimmelman, Attorney General, State of New Jersey",
          "cluster_id": 474012,
          "cite": [
            "796 F.2d 598",
            "1986 U.S. App. LEXIS 26633",
            "55 U.S.L.W. 2079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lynumn v. Illinois:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106558) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02OTgzNzEyMDAwMDAmcz01NzgyNTYmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106558%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106558)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTEmcz0yMTQzMzQmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28106558%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106558)",
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
    "complete_query": "cites:(106558)",
    "indexed_citing_opinions": 510,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106558,
        "count": 510,
        "count_source": "search"
      }
    ],
    "citation_count": 792,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/lynumn-v-illinois.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY4NjcxNDMmcz00NzcxMTExJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106558%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106558,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106558,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106558,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106558,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106558,
        "cited_id": 104712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106558,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106558,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106558,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106558,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106558,
        "cited_id": 106342,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106558,
        "cited_id": 2148133,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106558,
        "cited_id": 2243037,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106558,
        "cited_id": 3414047,
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
    "date_created": "2026-07-05T11:05:34Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:05:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:05:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:09:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:05:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Lynumn v. Illinois

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b593-4">
<span citation-index="1" class="star-pagination" label="529"> 
   *529
   </span>
  Mr. Justice Stewart
 </author>
<p id="ADm">
  delivered the opinion of the Court.
 </p>
<p id="b593-5">
  The petitioner was tried in the Criminal Court of Cook County, Illinois, on an indictment charging her with the unlawful possession and sale of marijuana. She was convicted and sentenced to the penitentiary for “not less than ten nor more than eleven years.” The judgment of conviction was affirmed on appeal by the Illinois Supreme Court. <span class="citation" data-id="2148133"><a href="/opinion/2148133/the-people-v-lynumn/" aria-description="Citation for case: The PEOPLE v. Lynumn">21 Ill. 2d 63</a></span>, <span class="citation" data-id="2148133"><a href="/opinion/2148133/the-people-v-lynumn/" aria-description="Citation for case: The PEOPLE v. Lynumn">171 N. E. 2d 17</a></span>. We granted cer-tiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./370/933/">370 U. S. 933</a></span>. For the reasons stated in this opinion, we hold that the petitioner’s trial did not meet the demands of due process of law, and we accordingly set aside the judgment before us.
 </p>
<p id="b593-6">
  On January 17, 1959, three Chicago police officers arrested James Zeno for unlawful possession of narcotics. They took him to a district police station. There they told him that if he “would set somebody up for them, they would go light” on him. He agreed to “cooperate” and telephoned the petitioner, telling her that he was coming over to her apartment. The officers and Zeno then went to the petitioner’s apartment house, and Zeno went upstairs to the third floor while the officers waited below. Some time later, variously estimated as from five to 20 minutes, Zeno emerged from the petitioner’s third floor apartment with a package containing a substance later determined to be marijuana. The officers took the package and told Zeno to return to the petitioner’s apartment on the pretext that he had left his glasses there. When the petitioner walked out into the hallway in response to Zeno’s call, one of the officers seized her and placed her under arrest.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The officers and
  <span citation-index="1" class="star-pagination" label="530"> 
   *530
   </span>
  Zeno then entered the petitioner's apartment.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  The petitioner at first denied she had sold the marijuana to Zeno, insisting that while he was in her apartment Zeno had merely repaid a loan. After further conversations with the officers, however, she told them that she had sold the marijuana to Zeno.
 </p>
<p id="b594-4">
  The officers testified to this oral confession at the petitioner’s trial, and it is this testimony which, we now hold, fatally infected the petitioner’s conviction. The petitioner testified at the trial that she had not in fact sold any marijuana to Zeno, that Zeno had merely repaid a long-standing loan.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  She also testified, however, that she
  <span citation-index="1" class="star-pagination" label="531"> 
   *531
   </span>
  had told the officers on the day of her arrest that she had sold Zeno marijuana, describing the circumstances under which this statement was made as follows:
 </p>
<blockquote id="b595-5">
  “I told him [Officer Sims] I hadn’t sold Zeno; I didn’t know anything about narcotics and I had no source of supply. He kept insisting I had a source of supply and had been dealing in narcotics. I kept telling him I did not and that I knew nothing about it. Then he started telling me I could get 10 years and the children could be taken away, and after I got out they would be taken away and strangers would have them, and if I could cooperate he would see they weren’t; and he would recommend leniency and I had better do what they told me if I wanted to see my kids again. The two children are three and four years old. Their father is dead; they live with me. I love my children very much. I have never been arrested for anything in my whole life before. I did not know how much power a policeman had in a recommendation to the State’s Attorney or to the Court. I did not know that a Court and a State’s Attorney are not bound by a police officer’s recommendations. I did not know anything about it. All the officers talked to me about my children and the time I could get for not cooperating. All three officers did. After that conversation I believed that if I cooperated with them and answered the questions the way they wanted me to answer, I believed that I would not be prosecuted. They had said I had better say what they wanted me to, or I would lose the kids. I said I would say anything they wanted me to say. I asked what I was to say. I was told to
  <span citation-index="1" class="star-pagination" label="532"> 
   *532
   </span>
  say ‘You must admit you gave Zeno the package’ so I said, ‘Yes, I gave it to him.’
 </blockquote>
<blockquote id="b596-4">
  “. . . The only reason I had for admitting it to the police was the hope of saving myself from going to jail and being taken away from my children. The statement I made to the police after they promised that they would intercede for me, the statements admitting the crime, were false.
 </blockquote>
<blockquote id="b596-5">
  “. . . My statement to the police officers that I sold the marijuana to Zeno was false. I lied to the police at that time. I lied because the police told me they were going to send me to jail for 10 years and take my children, and I would never see them again; so I agreed to say whatever they wanted me to say.”
 </blockquote>
<p id="b596-6">
  The police officers did not deny that these were the circumstances under which the petitioner told them that she had sold marijuana to Zeno. To the contrary, their testimony largely corroborated the petitioner’s testimony. Officer Sims testified:
 </p>
<blockquote id="b596-7">
  “I told her then that Zeno had been trapped and we asked him to cooperate; that he had made a phone call to her and subsequently had purchased the evidence from her. I told her then if she wished to cooperate, we would be willing to recommend to the State leniency in her case. At that time, she said, ‘Yes, I did sell it to him.’
 </blockquote>
<blockquote id="b596-8">
  “. . . While I was talking to her in the bedroom, she told me that she had children and she had taken the children over to her mother-in-law, to keep her children.
 </blockquote>
<blockquote id="b597-5">
<span citation-index="1" class="star-pagination" label="533"> 
   *533
   </span>
  “Q. Did you or anybody in your presence indicate or suggest or say to her that her children would be taken away from her if she didn’t do what you asked her to do?
 </blockquote>
<blockquote id="b597-6">
  “Witness: I believe there was some mention of her children being taken away from her if she was arrested.
 </blockquote>
<blockquote id="b597-7">
  “The Court: By whom? Who made mention of it?
 </blockquote>
<blockquote id="b597-8">
  “The Witness: I believe Officer Bryson made that statement and I think I made the statement at some time during the course of our discussion that her children could be taken from her. We did not say if she cooperated they wouldn’t be taken. I don’t know whether Kobar said that to her or not. I don’t recall if Kobar said that to her or not.
 </blockquote>
<blockquote id="b597-9">
  “I asked her who the clothing belonged to. She said they were her children’s. I asked how many she had and she said 2. I asked her where they were or who took care of them. She said the children were over at the mother’s or mother-in-law. I asked her how did she take care of herself and she said she was on ADC. I told her that if we took her into the station and charged her with the offense, that the ADC would probably be cut off and also that she would probably lose custody of her children. That was not before I said if she cooperated, it would go light on her. It was during the same conversation.
 </blockquote>
<blockquote id="b597-10">
  "... I made the statement to her more than once; but I don’t know how many times, that she had been set up and if she cooperated we would go light with her.”
 </blockquote>
<p id="b598-3">
<span citation-index="1" class="star-pagination" label="534"> 
   *534
   </span>
  Officer Bryson testified:
 </p>
<blockquote id="b598-4">
  “Miss Lynumn said she was thinking about her children and she didn’t want to go to jail. I was present and heard something pertaining to her being promised leniency if she would cooperate. I don’t know exactly who said it. I could have, myself, or Sims.”
 </blockquote>
<p id="b598-5">
  It is thus abundantly clear that the petitioner’s oral confession was made only after the police had told her that state financial aid for her infant children would be cut off, and her children taken from her, if she did not “cooperate.” These threats were made while she was encircled in her apartment by three police officers and a twice convicted felon who had purportedly “set her up.” There was no friend or adviser to whom she might turn. She had had no previous experience with the criminal law, and had no reason not to believe that the police had ample power to carry out their threats.
 </p>
<p id="b598-6">
  We think it clear that a confession made under such circumstances must be deemed not voluntary, but coerced. That is the teaching of our cases. We have said that the question in epch case is whether the defendant’s will was overborne at the time he confessed.
  <em>
   Chambers
  </em>
  v.
  <em>
   Florida,
  </em>
  <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span>;
  <em>
   Watts
  </em>
  v.
  <em>
   Indiana,
  </em>
  <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#52" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 52, 53</a></span>;
  <em>
   Leyra
  </em>
  v.
  <em>
   Denno,
  </em>
  <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/#558" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556, 558</a></span>. If so, the confession cannot be deemed “the product of a rational intellect and a free will.”
  <em>
   Blackburn
  </em>
  v.
  <em>
   Alabama,
  </em>
  <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#208" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 208</a></span>. See also
  <em>
   Spano
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span>;
  <em>
   Ashcraft
  </em>
  v.
  <em>
   Tennessee,
  </em>
  <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span>; and see particularly,
  <em>
   Harris
  </em>
  v.
  <em>
   South Carolina,
  </em>
  <span class="citation" data-id="9420383"><a href="/opinion/104712/harris-v-south-carolina/#70" aria-description="Citation for case: Harris v. South Carolina">338 U. S. 68, 70</a></span>.
 </p>
<p id="b598-7">
  In this case counsel for the State of Illinois has conceded, at least for purposes of argument, that the totality of the circumstances disclosed by the record must be deemed to have combined to produce an impellingly coer
  <span citation-index="1" class="star-pagination" label="535"> 
   *535
   </span>
  cive effect upon the petitioner at the time she told the officers she had sold marijuana to Zeno. But counsel for the State argues that we should nonetheless affirm the judgment before us upon either of two alternative grounds. It is contended first that the petitioner did not properly assert or preserve her federal constitutional claim in accord with established rules of Illinois procedure, and that her conviction therefore rests upon an adequate and independent foundation of state law. Secondly, it is urged that the petitioner’s conviction “does not rest in whole or in any part upon petitioner’s confession.” We find both of these contentions without validity.
 </p>
<p id="b599-5">
  It is true that the record in this case does not show that the petitioner explicitly asserted her federal constitutional claim in the trial court. And it is said that in Illinois the procedural rule is settled that where a constitutional claim which is based not upon the alleged unconstitutionality of a statute, but upon the facts of a particular case, is not clearly and appropriately raised in the trial court, the claim will not be considered on appeal by the Supreme Court of Illinois. In other words, such a claim of constitutional right, it is said, must be asserted in the trial court or it will be deemed upon appellate review to have been waived.
  <em>
   People
  </em>
  v.
  <em>
   Touhy,
  </em>
  <span class="citation" data-id="3414047"><a href="/opinion/3417789/the-people-v-touhy/" aria-description="Citation for case: The People v. Touhy">397 Ill. 19</a></span>, <span class="citation" data-id="3414047"><a href="/opinion/3417789/the-people-v-touhy/" aria-description="Citation for case: The People v. Touhy">72 N. E. 2d 827</a></span>.
 </p>
<p id="b599-6">
  If all we had to go on were the record in the Illinois trial and appellate courts, there would indeed be color to the claim of counsel for the State, and we would be squarely faced with the necessity of determining what the Illinois procedural rule actually is, and whether the rule constituted an adequate independent ground in support of the judgment affirming the petitioner’s conviction. But that is not necessary in this case. For there is here a short and complete answer to the respondent’s argument. Before acting upon the petition for certiorari, we entered an order directed to this very problem. The order
  <span citation-index="1" class="star-pagination" label="536"> 
   *536
   </span>
  accorded counsel for the petitioner “opportunity to secure a certificate from the Supreme Court of Illinois as to whether the judgment herein was intended to rest on an adequate and independent state ground, or whether decision of the federal claim . . . was necessary to the judgment rendered.” <span class="citation multiple-matches"><a href="/c/U.%20S./368/908/">368 U. S. 908</a></span>. The answer of the Supreme Court of Illinois was unambiguous. On June 8, 1962, that court issued the following “Response to Request for Certificate”:
 </p>
<blockquote id="b600-6">
  “In response to a request by counsel for the plaintiff in error we hereby certify that decision of the federal claim referred to in the order of the United States Supreme Court dated November 13, 1961, was necessary to our judgment in this case.”
 </blockquote>
<p id="b600-7">
  We decline to search behind this certificate of the Supreme Court of Illinois.
 </p>
<p id="b600-8">
  The State’s contention that the petitioner’s conviction did not rest in any part upon her confession is quite without merit. The case was tried by the court without a jury. The record shows that twice during the trial the petitioner’s counsel moved to strike the testimony of the police officers as to the petitioner’s oral statement to them. On the first occasion the trial judge reserved a ruling on the motion “until the close of the State’s case.” When the motion was renewed, the record states that “[t]he motion to strike was denied.” Thus the record affirmatively shows that the evidence of the petitioner’s confession was admitted and considered by the trial court.
 </p>
<p id="b600-9">
  On appeal, the Supreme Court of Illinois, which has power independently to assess the evidence of guilt in a criminal case,
  <em>
   People
  </em>
  v.
  <em>
   Ware,
  </em>
  <span class="citation" data-id="2243037"><a href="/opinion/2243037/the-people-v-ware/" aria-description="Citation for case: The PEOPLE v. Ware">23 Ill. 2d 59</a></span>, <span class="citation" data-id="2243037"><a href="/opinion/2243037/the-people-v-ware/" aria-description="Citation for case: The PEOPLE v. Ware">177 N. E. 2d 362</a></span>, included in its summary of the prosecution’s evidence in this case the statement that “[t]he police officers also testified to certain admissions of guilt made to them by
  <span citation-index="1" class="star-pagination" label="537"> 
   *537
   </span>
  defendant on January 17, 1959.” <span class="citation" data-id="2148133"><a href="/opinion/2148133/the-people-v-lynumn/#67" aria-description="Citation for case: The PEOPLE v. Lynumn">21 Ill. 2d, at 67</a></span>, <span class="citation" data-id="2148133"><a href="/opinion/2148133/the-people-v-lynumn/#19" aria-description="Citation for case: The PEOPLE v. Lynumn">171 N. E. 2d, at 19</a></span>. Later in its opinion, the court stated:
 </p>
<blockquote id="b601-5">
  “A review of the record does indicate, however, that strong suggestions of leniency were made to defendant subsequent to her arrest and prior to her admissions. Even in the absence of defendant’s statements, there is clear proof by Zeno and the police officers that defendant gave Zeno a package containing marijuana. Upon a review of the entire record, we are convinced that the evidence fully supports the judgment of the trial court. . . .” <span class="citation" data-id="2148133"><a href="/opinion/2148133/the-people-v-lynumn/#68" aria-description="Citation for case: The PEOPLE v. Lynumn">21 Ill. 2d, at 68</a></span>, <span class="citation" data-id="2148133"><a href="/opinion/2148133/the-people-v-lynumn/#20" aria-description="Citation for case: The PEOPLE v. Lynumn">171 N. E. 2d, at 20</a></span>.
 </blockquote>
<p id="b601-6">
  While this statement is not free from ambiguity, we take it to express the view that even if the testimony as to the petitioner’s confession was erroneously admitted, the error was a harmless one in the light of other evidence of the petitioner’s guilt.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  That is an impermissible doctrine. As was said in
  <em>
   Payne
  </em>
  v.
  <em>
   Arkansas,
  </em>
  “this Court has uniformly held that even though there may have been sufficient evidence, apart from the coerced confession, to support a judgment of conviction, the admission in evidence, over objection, of the coerced confession vitiates the judgment because it violates the Due Process Clause of the Fourteenth Amendment.” <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#568" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560, at 568</a></span>.
  <span citation-index="1" class="star-pagination" label="538"> 
   *538
   </span>
  See
  <em>
   Spano
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#324" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 324</a></span>;
  <em>
   Watts
  </em>
  v.
  <em>
   Indiana,
  </em>
  <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#50" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 50, n. 2</a></span>;
  <em>
   Haley
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#599" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596, 599</a></span>.
 </p>
<p id="b602-6">
  The judgment is set aside, and the case is remanded to the Supreme Court of Illinois for further proceedings not inconsistent with this opinion.
 </p>
<p id="b602-7">
<em>
   It is so ordered.
  </em>
</p>




<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b593-7">
   Officer Sims testified as follows: “He called Beatrice and said he had left his glasses in the apartment; she opened the door and as she came out into the hall, I was standing in the common hall, in the vestibule part with the door partly closed. As she walked down the hallway toward Zeno, I opened the door and stepped into the hall
   <span citation-index="1" class="star-pagination" label="530"> 
    *530
    </span>
   way. I told her she was under arrest and I grabbed her by her hands, both hands. At this point, I told her that she had been set up, that she had just made a sale and I showed her the package.”
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b594-6">
   Officer Sims testified: “I had complete physical possession of her two hands. I had turned her hands loose when we went into the apartment. I went in ahead of her. The door was still open. The apartment door was still ajar and I walked into the apartment and she followed me in. We were together but I was beside her. I believe Bryson and Zeno were behind her. She was between two police officers. We proceeded in that fashion to enter her apartment.”
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b594-7">
   Her testimony on this subject was as follows: “On January 17th Zeno called me. He owed me money, $23.00. I had loaned him this money about three months previously. He said he was being evicted and had money en route from his sister and if I could lend him the money, he could pay his rent; and I haven’t seen him since. That was three months previously. On this day he told me on the phone he was sorry he had not been around to pay the money but he had been in pretty bad shape. But now he had come into some money and would come and pay me.
  </p>
<blockquote id="b594-8">
<em>
    .
   </em>
   . On that day I did not give to Zeno, nor did Mr. Zeno ask me in the telephone conversation in which he said he was going to pay me the money he owed me, he did not say anything about having a can ready for him or anything like that.
  </blockquote>
<blockquote id="b594-9">
   “He said here is the money I owe you. He owed me $23.00. When he gave me the money, he gave me $28.00. I asked him what the $5.00 was for and he said it was because I had it so long. I did not
   <span citation-index="1" class="star-pagination" label="531"> 
    *531
    </span>
   say to Mr. Zeno let’s go into the kitchen. Nothing like that. I did not have any transaction with him in the kitchen nothing even like that.”
  </blockquote>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b601-7">
   It is difficult, however, to perceive how the admission of evidence of the confession could be considered harmless. The only other evidence of substance against the petitioner was that given by Zeno, a twice convicted felon who testified that he was eager in his own self-interest to cooperate with the police by “setting up” someone. While it was undisputed that Zeno was in possession of the package of marijuana when he emerged from the petitioner’s apartment, it was far from clear that Zeno obtained the marijuana from the petitioner. Zeno was out of the police officers’ sight for a period of from five to 20 minutes, and there were other apartments in the building where Zeno might have obtained the package.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Maine v. Moulton.md  (`case`, 5 assertions)

### content_page

```
---
title: "Maine v. Moulton"
type: case
citation: "474 U.S. 159 (1985)"
parallel_cite: "106 S. Ct. 477; 88 L. Ed. 2d 481; 54 U.S.L.W. 4039"
neutral_cite: 1985 U.S. LEXIS 147
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-12-10
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-12-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Maine v. Moulton
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111546/maine-v-moulton/"
  cluster_id: 111546
  opinion_id: 9430241
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny / Refinement"
related: ["[[Massiah v. United States]]", "[[Kuhlmann v. Wilson]]", "[[United States v. Henry]]", "[[Brewer v. Williams]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "deliberate-elicitation", "informant"]
holding: "The Sixth Amendment is violated when the State knowingly exploits an opportunity to confront the accused without counsel — it makes no…"
lake:
  record_id: Maine v. Moulton
  status: verified
  projected_at: 2026-07-06
---

# Maine v. Moulton

*474 U.S. 159 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Moulton was indicted and released on bail. His codefendant, Colson, secretly agreed to cooperate with police, who had him record telephone calls with Moulton and then wear a body wire to a meeting the two arranged to plan their defense. At that recorded meeting Colson prompted Moulton to recount details of the crimes. The recordings were used against Moulton at trial. The State argued the surveillance was justified by an investigation of other, uncharged crimes.

## Issue
Whether the Sixth Amendment is violated when the State, through an informant, obtains incriminating statements about pending charges from an indicted defendant, where the State claims it was also investigating other crimes.

## Rule
Knowing exploitation of a confrontation without counsel violates the right: "the Sixth Amendment is not violated whenever — by luck or happenstance — the State obtains incriminating statements from the accused after the right to counsel has attached." — 474 U.S. at 176. ^pin-176

But "knowing exploitation by the State of an opportunity to confront the accused without counsel being present is as much a breach of the State's obligation not to circumvent the right to the assistance of counsel as is the intentional creation of such an opportunity. Accordingly, the Sixth Amendment is violated when the State obtains incriminating statements by knowingly circumventing the accused's right to have counsel present in a confrontation between the accused and a state agent." — *Id.* ^pin-176a

## Application
Moulton had been indicted, so his right to counsel had attached on the charged offenses. The police did not merely come upon his statements by chance: they suggested the recordings, equipped Colson with a wire, and knew the recorded meeting was for the express purpose of discussing the pending charges. By knowingly exploiting that opportunity to confront Moulton about the charged crimes without counsel present, the State violated the Sixth Amendment, and the State's additional interest in investigating other crimes did not cure the violation as to the pending charges.

## Conclusion
The use of the deliberately elicited statements on the pending charges violated the Sixth Amendment; the conviction was affirmed below on that ground and the State's judgment to suppress was upheld. The "other crimes" investigative motive was irrelevant to the charged-offense violation.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Moulton* extends [[Massiah v. United States]] from intentional creation of a confrontation to **knowing exploitation** of one, and supplies the "luck or happenstance" / passive-listening boundary that [[Kuhlmann v. Wilson]] applied the next Term.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny / Refinement*

## Sources
- *Maine v. Moulton*, 474 U.S. 159 (1985) — https://www.courtlistener.com/opinion/111546/maine-v-moulton/ — pinpoint: 176.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "cdad127ed290aa0d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "474 U.S. 159 (1985)", "court": "U.S. Supreme Court", "neutral_cite": "1985 U.S. LEXIS 147", "official_citation_present": true, "parallel_cite": "106 S. Ct. 477; 88 L. Ed. 2d 481; 54 U.S.L.W. 4039", "title": "Maine v. Moulton", "year": "1985"}}
{"assertion_id": "4e05d92746fd0fe4", "dimension": "support", "kind": "home_role", "locator": {"home": "Sixth Amendment Right to Counsel"}, "payload": {"home": "Sixth Amendment Right to Counsel", "role": "Key — Progeny / Refinement", "title": "Maine v. Moulton"}}
{"assertion_id": "f0c37ecdfc1e1a4d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Sixth Amendment is violated when the State knowingly exploits an opportunity to confront the accused without counsel — it makes no…", "title": "Maine v. Moulton"}}
{"assertion_id": "3f5c478302065709", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Maine v. Moulton"}}
{"assertion_id": "77f1fe0130e30048", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1985-12-10", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Maine v. Moulton", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Maine v. Moulton", "varies_by_point": "false"}}
```

### lake record — Maine v. Moulton

```json
{
  "schema_version": "s2.v1",
  "record_id": "Maine v. Moulton",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Maine v. Moulton",
    "case_name_short": "Moulton",
    "case_name_full": "Maine v. Moulton",
    "input_case_name": "Maine v. Moulton",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-12-10",
    "year": 1985,
    "docket": null,
    "cluster_id": 111546,
    "lead_opinion_id": 9430241,
    "sibling_ids": [
      111546,
      9430241,
      9430242
    ],
    "absolute_url": "/opinion/111546/maine-v-moulton/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9053194,
        "score": 20,
        "case_name": "Maine v. Moulton"
      },
      {
        "cluster_id": 9052337,
        "score": 20,
        "case_name": "Maine v. Moulton"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "474 U.S. 159",
      "volume": "474",
      "reporter": "U.S.",
      "page": "159",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "106 S. Ct. 477",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "477",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 L. Ed. 2d 481",
        "volume": "88",
        "reporter": "L. Ed. 2d",
        "page": "481",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4039",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4039",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 147",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "147",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "474 U.S. 159",
        "volume": "474",
        "reporter": "U.S.",
        "page": "159",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 477",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "477",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 L. Ed. 2d 481",
        "volume": "88",
        "reporter": "L. Ed. 2d",
        "page": "481",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 147",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "147",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4039",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4039",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "474 U.S. 159",
    "official_selection": {
      "court_class": "scotus",
      "selected": "474 U.S. 159",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-176",
      "page": null,
      "quote": "--- # Maine v. Moulton *474 U.S. 159 (1985)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Moulton was indicted and released on bail. His codefendant, Colson, secretly agreed to cooperate with police, who had him record telephone calls with Moulton and then wear a body wire to a meeting the two arranged to plan their defense. At that recorded meeting Colson prompted Moulton to recount details of the crimes. The recordings were used against Moulton at trial. The State argued the surveillance was justified by an investigation of other, uncharged crimes. ## Issue Whether the Sixth Amendment is violated when the State, through an informant, obtains incriminating statements about pending charges from an indicted defendant, where the State claims it was also investigating other crimes. ## Rule Knowing exploitation of a confrontation without counsel violates the right:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-176a",
      "page": null,
      "quote": "knowing exploitation by the State of an opportunity to confront the accused without counsel being present is as much a breach of the State's obligation not to circumvent the right to the assistance of counsel as is the intentional creation of such an opportunity. Accordingly, the Sixth Amendment is violated when the State obtains incriminating statements by knowingly circumventing the accused's right to have counsel present in a confrontation between the accused and a state agent.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-12-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Maine v. Moulton",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Harvin",
          "cluster_id": 9352546,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Harvin",
          "cluster_id": 9329344,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Harvin",
          "cluster_id": 8465498,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Benton",
          "cluster_id": 10134904,
          "cite": [
            "317 Or. App. 384",
            "505 P.3d 975"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Justin Barrett Blakeney v. State of Mississippi",
          "cluster_id": 4442047,
          "cite": [
            "236 So. 3d 11"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amended September 20, 2016 State of Iowa v. Justin Alexander Marshall",
          "cluster_id": 4472001,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Justin Alexander Marshall",
          "cluster_id": 3218790,
          "cite": [
            "882 N.W.2d 68",
            "2016 Iowa Sup. LEXIS 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. Stephens",
          "cluster_id": 7317930,
          "cite": [
            "157 F. Supp. 3d 623",
            "2016 U.S. Dist. LEXIS 3888",
            "2016 WL 147919"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Justin Alexander Marshall",
          "cluster_id": 2806802,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
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
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Basu",
          "cluster_id": 2662288,
          "cite": [
            "881 F. Supp. 2d 1",
            "2012 WL 2244875",
            "2012 U.S. Dist. LEXIS 84114"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Basciano",
          "cluster_id": 2470094,
          "cite": [
            "763 F. Supp. 2d 303",
            "2011 U.S. Dist. LEXIS 2901",
            "2011 WL 114865"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Tlasek",
          "cluster_id": 6589376,
          "cite": [
            "77 Mass. App. Ct. 298",
            "930 N.E.2d 170",
            "2010 Mass. App. LEXIS 999"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Ramirez",
          "cluster_id": 3145133,
          "cite": [
            "402 Ill. App. 3d 638",
            "343 Ill. Dec. 405",
            "934 N.E.2d 1008",
            "2010 Ill. App. LEXIS 587"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gonzalez",
          "cluster_id": 1888318,
          "cite": [
            "986 A.2d 235",
            "2010 R.I. LEXIS 8",
            "2010 WL 114218"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kansas v. Ventris",
          "cluster_id": 145880,
          "cite": [
            "173 L. Ed. 2d 801",
            "129 S. Ct. 1841",
            "556 U.S. 586",
            "2009 U.S. LEXIS 3299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Maldonado",
          "cluster_id": 2334216,
          "cite": [
            "259 S.W.3d 184",
            "2008 Tex. Crim. App. LEXIS 685",
            "2008 WL 2261776"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Arabzadegan v. State",
          "cluster_id": 2166816,
          "cite": [
            "240 S.W.3d 44",
            "2007 WL 2066225"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martin v. Giurbino",
          "cluster_id": 8642780,
          "cite": [
            "237 F. App'x 299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane1_negative"
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
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
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
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
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
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wesbrook v. State",
          "cluster_id": 1473130,
          "cite": [
            "29 S.W.3d 103",
            "2000 Tex. Crim. App. LEXIS 86",
            "2000 WL 1346901"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
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
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
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
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Jackson",
          "cluster_id": 111622,
          "cite": [
            "89 L. Ed. 2d 631",
            "106 S. Ct. 1404",
            "475 U.S. 625",
            "1986 U.S. LEXIS 91",
            "54 U.S.L.W. 4334"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kuhlmann v. Wilson",
          "cluster_id": 111726,
          "cite": [
            "91 L. Ed. 2d 364",
            "106 S. Ct. 2616",
            "477 U.S. 436",
            "1986 U.S. LEXIS 65",
            "54 U.S.L.W. 4809"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
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
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
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
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
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
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Frye",
          "cluster_id": 5607916,
          "cite": [
            "18 Cal. 4th 894",
            "98 Cal. Daily Op. Serv. 5949",
            "959 P.2d 183",
            "98 Daily Journal DAR 8259",
            "77 Cal. Rptr. 2d 25",
            "1998 Cal. LEXIS 4688"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
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
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Iowa v. Tovar",
          "cluster_id": 134725,
          "cite": [
            "158 L. Ed. 2d 209",
            "124 S. Ct. 1379",
            "541 U.S. 77",
            "2004 U.S. LEXIS 1837"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
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
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
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
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bing",
          "cluster_id": 5690131,
          "cite": [
            "76 N.Y.2d 331",
            "558 N.E.2d 1011",
            "559 N.Y.S.2d 474",
            "1990 N.Y. LEXIS 1488"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gonzalez",
          "cluster_id": 2612406,
          "cite": [
            "800 P.2d 1159",
            "51 Cal. 3d 1179",
            "275 Cal. Rptr. 729",
            "90 Daily Journal DAR 13736",
            "90 Cal. Daily Op. Serv. 8746",
            "1990 Cal. LEXIS 5233"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Cobb",
          "cluster_id": 118417,
          "cite": [
            "149 L. Ed. 2d 321",
            "121 S. Ct. 1335",
            "532 U.S. 162",
            "2001 U.S. LEXIS 2696"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "George Thomas Franklin v. Jim Fox Martin Murray Robert Morse Bryan Cassandro John Cuneo, Sergeant Eileen Franklin-Lipsker",
          "cluster_id": 780047,
          "cite": [
            "312 F.3d 423",
            "2002 Daily Journal DAR 13381",
            "2002 Cal. Daily Op. Serv. 11479",
            "2002 U.S. App. LEXIS 24254",
            "2002 WL 31663614"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Memro",
          "cluster_id": 1375029,
          "cite": [
            "905 P.2d 1305",
            "11 Cal. 4th 786",
            "47 Cal. Rptr. 2d 219",
            "95 Daily Journal DAR 15919",
            "95 Cal. Daily Op. Serv. 9091",
            "1995 Cal. LEXIS 6793"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Voigt",
          "cluster_id": 722380,
          "cite": [
            "89 F.3d 1050",
            "78 A.F.T.R.2d (RIA) 5577",
            "1996 U.S. App. LEXIS 16287",
            "1996 WL 380609"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Teel",
          "cluster_id": 2376013,
          "cite": [
            "793 S.W.2d 236",
            "1990 Tenn. LEXIS 216"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
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
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Morris",
          "cluster_id": 1454621,
          "cite": [
            "807 P.2d 949",
            "53 Cal. 3d 152",
            "279 Cal. Rptr. 720",
            "91 Daily Journal DAR 3869",
            "91 Cal. Daily Op. Serv. 2303",
            "1991 Cal. LEXIS 1218"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maine v. Moulton:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111546 OR 9430241 OR 9430242) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTQ3MzA1NjAwMDAwJnM9MjAyNTkwMyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111546+OR+9430241+OR+9430242%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 19,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 19,
        "triage_snippet_classified": 181
      },
      "lane2_top_cited": {
        "query": "cites:(111546 OR 9430241 OR 9430242)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yODMmcz0xMzQ1OTc5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111546+OR+9430241+OR+9430242%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111546 OR 9430241 OR 9430242)",
        "reviewed": 17,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 17,
        "triage_read": 0,
        "triage_snippet_classified": 17
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111546 OR 9430241 OR 9430242)",
    "indexed_citing_opinions": 825,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111546,
        "count": 719,
        "count_source": "search"
      },
      {
        "opinion_id": 9430241,
        "count": 125,
        "count_source": "search"
      },
      {
        "opinion_id": 9430242,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1260,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/maine-v-moulton.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgwNjEyMDQmcz05MzUzOTk3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111546+OR+9430241+OR+9430242%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111546,
        "cited_id": 102061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 109302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 110300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 110372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 111193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 111375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 258052,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 331822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 334742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 338566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 339956,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 411762,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 411966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 424746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 440311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 449567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 1127309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 1127374,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 1334560,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 1378224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 1379716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 1516878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 1973022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 2009182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111546,
        "cited_id": 3580565,
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
    "date_created": "2026-07-05T11:09:00Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:09:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:09:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:17:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:09:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Maine v. Moulton

```
<opinion type="majority">
<author id="b299-13">Justice Brennan</author>
<p id="AIV">delivered the opinion of the Court.</p>
<p id="b299-14">The question presented in this case is whether respondent’s Sixth Amendment right to the assistance of counsel was violated by the admission at trial of incriminating statements made by him to his codefendant, a secret government informant, after indictment and at a meeting of the two to plan defense strategy for the upcoming trial.</p>
<p id="b299-3">I</p>
<p id="AvCZ">On the night of January 15, 1981, police officers in Belfast, Maine, responded to a fire call in the vicinity of the Belfast Dodge automobile dealership. Arriving at the scene, the officers discovered a burning Chevrolet dump truck which they recognized as a vehicle that had been reported stolen.<footnotemark>1</footnotemark> <page-number citation-index="1" label="162">*162</page-number>After examining the burning truck, the officers searched a building located on the Belfast Dodge property. This building was not part of the dealership, but was leased to respondent Perley Moulton and his codefendant Gary Colson who were using the space to restore and sell old Ford Mustangs. Inside, the officers discovered evidence of several recent automobile and automobile-related thefts.</p>
<p id="b300-5">On April 7, 1981, a Waldo County grand jury returned indictments charging Moulton and Colson with four counts of theft by receiving in violation of Me. Rev. Stat. Ann., Tit. 17-A, § 359 (1983). Specifically, the indictments alleged that Moulton and Colson received, retained, or disposed of a 1978 Ford pickup truck, a 1978 Chevrolet dump truck, a 1970 Ford Mustang automobile, and assorted Ford Motor Company automotive parts knowing these to be stolen and intending to deprive the owners of possession. On April 9, Moulton and Colson, represented by retained counsel, appeared before the Maine Superior Court for Waldo County and entered pleas of not guilty. Both were enlarged on bail pending trial. Numerous proceedings, unnecessary to detail here, occurred during the ensuing year and a half.</p>
<p id="b300-6">On November 4, 1982, Colson complained by telephone to Robert Keating, Chief of the Belfast Police Department, that he had received anonymous threatening telephone calls regarding the charges pending against him and Moulton, and indicated that he wished to talk to the police about the charges. Keating told Colson to speak with his lawyer and to call back.</p>
<p id="b300-7">On November 6, Colson met with Moulton at a Belfast restaurant to plan for their upcoming trial. According to Colson, Moulton suggested the possibility of killing Gary Elwell, a State’s witness, and they discussed how to commit the murder.</p>
<p id="b300-8">On November 9 and 10, Colson, accompanied by his lawyer, met with Police Chief Keating and State Police Detective Rexford Kelley. At these meetings, Colson gave full <page-number citation-index="1" label="163">*163</page-number>confessions of his participation with Moulton in committing the crimes for which they had been indicted. In addition, Colson admitted that he and Moulton had not merely received stolen automotive parts, but also had broken into the local Ford dealership to steal the parts. Colson also stated that he and Moulton had set fire to the dump truck and had committed other thefts. The officers offered Colson a deal: no further charges would be brought against him if he would testify against Moulton and otherwise cooperate in the prosecution of Moulton on the pending charges. Colson agreed to cooperate.<footnotemark>2</footnotemark></p>
<p id="b301-5">Colson also discussed with Keating and Kelley the anonymous threats he had received and Moulton’s inchoate plan to kill Gary Elwell. Keating requested, and Colson consented, to have a recording device placed on Colson’s telephone. Colson was instructed to turn the recording device on whenever he received a telephone call, but to turn it off immediately unless it was a threat from the anonymous caller or a call from Moulton.</p>
<p id="b301-6">The recording device was on Colson’s telephone for over a month. Although he received no threats, Colson spoke to Moulton three times during this period, and the tapes of these calls were turned over to the police. The first conversation, on November 22, concerned primarily personal matters. The only reference to the pending criminal charges was Colson’s question whether Moulton had “heard anything from the lawyer,” and Moulton’s response that he had not, but that he had “come up with a method” that he “ha[d] to work out the details on,” and that “[s]ome day [he’d] like to get together and talk to [Colson] about it.” Moulton, then <page-number citation-index="1" label="164">*164</page-number>living in New Hampshire, said that he was planning to visit Belfast around Christmas.</p>
<p id="b302-5">The second telephone conversation, on December 2, was prompted by Moulton’s receipt of copies of statements of three of the State’s witnesses, including Elwell; Colson had not yet received copies of the statements. Most of their talk (on Moulton’s side particularly) was about the statements of Elwell and Elwell’s brother, which accused Moulton and Colson of being guilty of the pending charges and which Moulton complained were an attempt to frame him and Colson. After reading Colson a statement by Elwell that he had received a threatening phone call, Moulton commented “[t]his is a big joke, man.”<footnotemark>3</footnotemark> When Colson jokingly suggested that they flee to Acapulco, Moulton vehemently rejected the suggestion, stating: “No, I’m gonna stay here and I’m gonna fight it man. I’m gonna fight it man. I ain’t gonna get framed for nothing.” Colson assented to this and suggested, “we’ll have to get together sometime . . . .” Moulton reminded Colson that he would be visiting at Christmas, and the conversation ended without Moulton having said anything that incriminated him.</p>
<p id="b302-6">The third telephone conversation, which took place on December 14, was similar to the second one. Most of the conversation concerned the pending charges, but Moulton said nothing inculpatory and continued to insist that he and Colson were being framed. Moulton asked Colson to set aside an entire day so that the two of them could meet and plan their defense. They agreed to meet on Sunday, December 26.</p>
<p id="b302-7">After learning from the telephone recordings about the meeting planned for December 26, the police obtained Colson’s consent to be equipped with a body wire transmitter to record what was said at the meeting. Chief Keating later testified that he did this for Colson’s safety in case Moulton <page-number citation-index="1" label="165">*165</page-number>realized that Colson was cooperating with the police, and to record any further conversation concerning threats to witnesses. Keating also testified that he was aware that Moulton and Colson were meeting to discuss the charges for which Moulton was already under indictment. Colson was instructed “not to attempt to question Perley Moulton, just be himself in his conversation . . . .”</p>
<p id="b303-5">The December 26 meeting, as was to be expected from the recorded telephone conversations, consisted of a prolonged discussion of the pending charges — what actually had occurred, what the State’s evidence would show, and what Moulton and Colson should do to obtain a verdict of acquittal. The idea of eliminating witnesses was briefly mentioned early in the conversation. After a short discussion, encouraged by Colson,<footnotemark>4</footnotemark> Moulton concluded that he did not think the plan would work. The remainder of the lengthy meeting was spent discussing the case. Moulton and Colson decided to create false alibis as their defense at trial. Because they sought to conform these alibis as closely as possible to what really happened, much of their discussion involved recounting the crimes. Although Colson had described what had happened in detail when he confessed to the police a month earlier, he now frequently professed to be unable to recall the <page-number citation-index="1" label="166">*166</page-number>events. Apologizing for his poor memory, he repeatedly asked Moulton to remind him about the details of what had happened, and this technique caused Moulton to make numerous incriminating statements.<footnotemark>5</footnotemark> Nor were all of Colson’s memory lapses related to events that required discussion to fabricate convincing alibis. Colson also “reminisced” about events surrounding the various thefts, and this technique too elicited additional incriminating statements from Moulton. For example, Colson asked Moulton how many locks they had drilled to steal a truck, a fact obviously not relevant to developing an alibi. Similarly, Colson questioned Moulton about whether it was the Mustang or the pickup truck that did not have a heater. Later, Colson jokingly drew forth admissions from Moulton concerning the dumping of a stolen truck into a pond after it had been scavenged for parts, and the dumping of a load of potatoes from another stolen truck onto the road. Each of these statements was later admitted into evidence against Moulton at trial.</p>
<p id="b304-5">Moulton filed a pretrial motion to suppress recorded statements he made to Colson in the three telephone conversations and at the December 26 meeting, arguing, <em>inter alia, </em>that the statements were obtained in violation of the Sixth and Fourteenth Amendments. After a hearing, the trial court denied the motion. The trial court found that the recordings were made “in order to gather information concerning the anonymous threats that Mr. Colson had been <page-number citation-index="1" label="167">*167</page-number>receiving, to protect Mr. Colson and to gather information concerning defendant Moulton’s plans to kill Gary Elwell.”</p>
<p id="b305-5">Meanwhile, after Colson’s role as an informant had been revealed to Moulton, the State had the pending indictments dismissed and obtained seven new indictments against Moul-ton. These indictments realleged the pending charges, and charged Moulton in addition with burglary, arson, and three more thefts. Moulton pleaded guilty to the charges contained in two of these indictments, and the trial court dismissed two more for improper venue. Moulton waived his right to a jury and proceeded to trial on the remaining three indictments, which covered the subjects of the original indictments and charged him with burglary, arson, and theft. At the trial, the State did not offer into evidence anything from the recorded telephone conversations, but did offer portions of the tapes of the December 26 meeting, principally those involving direct discussion of the thefts for which Moulton was originally indicted. The State did not offer the portion of the meeting during which Moulton and Colson discussed the possibility of killing witnesses and offered only one portion of the discussion about developing false testimony. At the conclusion of the trial, the court dismissed one more count of theft for improper venue and found Moulton not guilty of the arson charge. The court found Moulton guilty, however, of burglary and theft in connection with the Ford pickup truck, the Chevrolet dump truck, and the Ford automotive parts.</p>
<p id="b305-6">Moulton appealed these convictions on the ground that the admission into evidence of his statements to Colson violated his Sixth Amendment right to the assistance of counsel. The State filed a cross-appeal objecting to the dismissal of charges for improper venue. The Supreme Judicial Court of Maine granted both appeals and remanded for a new trial. <span class="citation" data-id="2009182"><a href="/opinion/2009182/state-v-moulton/" aria-description="Citation for case: State v. Moulton">481 A. 2d 155</a></span> (1984). Regarding the admission of Moulton’s recorded statements to Colson, the court agreed that there was “ample evidence” to support the trial court’s finding that <page-number citation-index="1" label="168">*168</page-number>the police wired Colson for legitimate purposes, but held that “[r]eference to the State’s legitimate motive may be relevant to, but cannot wholly refute, the alleged infringement of Moulton’s right to counsel.” <span class="citation" data-id="2009182"><a href="/opinion/2009182/state-v-moulton/#160" aria-description="Citation for case: State v. Moulton"><em>Id., </em>at 160</a></span>. The court held that the State cannot use against Moulton at trial recordings of conversations where the State “knew, or should have known” that Moulton would make incriminating statements regarding crimes as to which charges were already pending. Pointing to Moulton’s close relationship with Colson, the fact that the purpose of their meeting was to discuss the pending charges, and the fact that at the time of the meeting Colson was “fully cooperating with the police and no longer stood in the same adversarial position as did Moulton,” the court held:</p>
<blockquote id="b306-5">“When the police recommended the use of the body wire to Colson they intentionally created a situation that they knew, or should have known, was likely to result in Moulton’s making incriminating statements during his meeting with Colson. The police’s valid purpose in investigating threats against witnesses does not immunize the recordings of Moulton’s incriminating statements from constitutional attack. Those statements may be admissible in the investigation or prosecution of charges for which, at the time the recordings were made, adversary proceedings had not yet commenced. But as to the charges for which Moulton’s right to counsel had already attached, his incriminating statements should have been ruled inadmissible at trial, given the circumstances in which they were acquired.” <span class="citation" data-id="2009182"><a href="/opinion/2009182/state-v-moulton/#161" aria-description="Citation for case: State v. Moulton"><em>Id., </em>at 161</a></span>.</blockquote>
<p id="b306-6">We granted the State’s petition for certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./469/1206/">469 U. S. 1206</a></span>. We affirm.</p>
<p id="b306-8">II</p>
<p id="AQt">
<em>A</em>
</p>
<p id="b306-7">The right to the assistance of counsel guaranteed by the Sixth and Fourteenth Amendments is indispensable to the fair administration of our adversarial system of criminal jus<page-number citation-index="1" label="169">*169</page-number>tice.<footnotemark>6</footnotemark> Embodying “a realistic recognition of the obvious truth that the average defendant does not have the professional legal skill to protect himself,” <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#462" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 462-463</a></span> (1938), the right to counsel safeguards the other rights deemed essential for the fair prosecution of a criminal proceeding. Justice Sutherland’s oft-quoted explanation in <em>Powell </em>v. <em>Alabama, </em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span> (1932), bears repetition here:</p>
<blockquote id="b307-5">“The right to be heard would be, in many cases, of little avail if it did not comprehend the right to be heard by counsel. Even the intelligent and educated layman has small and sometimes no skill in the science of law. If charged with crime, he is incapable, generally, of determining for himself whether the indictment is good or bad. He is unfamiliar with the rules of evidence. Left without the aid of counsel he may be put on trial without a proper charge, and convicted upon incompetent evidence, or evidence irrelevant to the issue or otherwise inadmissible. He lacks both the skill and knowledge adequately to prepare his defense, even though he have a perfect one. He requires the guiding hand of counsel at every stage of the proceedings against him.” <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#68" aria-description="Citation for case: Powell v. Alabama"><em>Id., </em><page-number citation-index="1" label="170">*170</page-number>at 68-69</a></span> (quoted in <em>Gideon </em>v. <em>Wainwright, </em><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#344" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335, 344-345</a></span> (1963)).</blockquote>
<p id="b308-6">As indicated in the last sentence of this paragraph, the Court has also recognized that the assistance of counsel cannot be limited to participation in a trial; to deprive a person of counsel during the period prior to trial may be more damaging than denial of counsel during the trial itself. Recognizing that the right to the assistance of counsel is shaped by the need for the assistance of counsel, we have found that the right attaches at earlier, “critical” stages in the criminal justice process “where the results might well settle the accused’s fate and reduce the trial itself to a mere formality.” <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#224" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 224</a></span> (1967) (quoted in <em>United States </em>v. <em>Gouveia, </em><span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#189" aria-description="Citation for case: United States v. Gouveia">467 U. S. 180, 189</a></span> (1984)). See, <em>e. g., Coleman </em>v. <em>Alabama, </em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970); <em>Hamilton </em>v. <em>Alabama, </em><span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span> (1961); <em>White </em>v. <em>Maryland, </em><span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span> (1963); <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964); <em>Kirby </em>v. <em>Illinois, </em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682</a></span> (1972). And, “[wjhatever else it may mean, the right to counsel granted by the Sixth and Fourteenth Amendments means at least that a person is entitled to the help of a lawyer at or after the time that judicial proceedings have been initiated against him . . . .” <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#398" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387, 398</a></span> (1977). This is because, after the initiation of adversary criminal proceedings, “‘the government has committed itself to prosecute, and . . . the adverse positions of government and defendant have solidified. It is then that a defendant finds himself faced with the pros-ecutorial forces of organized society, and immersed in the intricacies of substantive and procedural criminal law.’” <em><span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/" aria-description="Citation for case: United States v. Gouveia">Gouveia, supra,</a></span> </em>at 189 (quoting <em>Kirby </em>v. <em>Illinois, supra, </em>at 689).</p>
<p id="b308-7">B</p>
<p id="b308-8">Once the right to counsel has attached and been asserted, the State must of course honor it.<footnotemark>7</footnotemark> This means more than <page-number citation-index="1" label="171">*171</page-number>simply that the State cannot prevent the accused from obtaining the assistance of counsel. The Sixth Amendment also imposes on the State an affirmative obligation to respect and preserve the accused’s choice to seek this assistance. We have on several occasions been called upon to clarify the scope of the State’s obligation in this regard, and have made clear that, at the very least, the prosecutor and police have an affirmative obligation not to act in a manner that circumvents and thereby dilutes the protection afforded by the right to counsel.</p>
<p id="b309-4">In <em>Spano </em>v. <em>New York, </em><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span> (1959), the defendant, who had already been indicted, was coercively interrogated by police until the early hours of the morning despite his repeated requests to see his lawyer. A unanimous Court reversed his conviction on the ground that the confession obtained by this interrogation was involuntary and therefore should not have been admitted into evidence at trial. Four Justices, in two concurring opinions, stated that they would also have reached this result on the ground that Spano’s Sixth Amendment right to the assistance of counsel was violated. These Justices reasoned that to permit police to “produce the vital evidence in the form of a confession which is useful or necessary to obtain a conviction” in the absence of counsel, after the right to counsel has attached, is to deny the accused “effective representation by counsel at the only stage when legal aid and advice would help him.” <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#325" aria-description="Citation for case: Spano v. New York"><em>Id., </em>at 325-326</a></span> (Douglas, J., concurring, joined by Black and Brennan, JJ.); see also, <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#326" aria-description="Citation for case: Spano v. New York"><em>id., </em>at 326-327</a></span> (Stewart, J., concurring, joined by Douglas and Brennan, JJ.). As Justice Douglas succinctly put the point, “what use is a defendant’s right to effective counsel at every stage of a criminal case if, while he is held awaiting trial, he can be questioned in the absence of counsel until he confesses?” <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#326" aria-description="Citation for case: Spano v. New York"><em>Id., </em>at 326</a></span>.</p>
<p id="b310-4"><page-number citation-index="1" label="172">*172</page-number>The position of the concurring Justices in <em><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">Spano</a></span> </em>was adopted by the Court in <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964). Massiah was indicted, along with a man named Colson,<footnotemark>8</footnotemark> for conspiracy to possess and to distribute cocaine. Massiah retained a lawyer, pleaded not guilty and was released on bail. Colson, meanwhile, decided to cooperate with Government agents in their continuing investigation of the narcotics activity in which Massiah and others were thought to be engaged. Colson permitted a Government agent to install a radio transmitter under the front seat of his automobile. Massiah held a lengthy conversation with Colson in this automobile while a Government agent listened over the radio. Massiah made several incriminating statements, and these were brought before the jury through the testimony of the Government agent. We reversed Massiah’s conviction on the ground that the incriminating statements were obtained in violation of Massiah’s rights under the Sixth Amendment. The Court stressed the fact that the interview took place after indictment, at a time when Massiah was clearly entitled to the assistance of counsel. Relying on Justice Douglas’ <em><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">Spano</a></span> </em>concurrence, the Court concluded that the need for, and consequently the right to, the assistance of counsel applied equally in this extrajudicial setting as at the trial itself. 877 U. S., at 204.<footnotemark>9</footnotemark> Consequently, the Court held:</p>
<blockquote id="b311-4"><page-number citation-index="1" label="173">*173</page-number>“[Massiah] was denied the basic protections of [the right to the assistance of counsel] when there was used against him at trial evidence of his own incriminating words, which federal agents had deliberately elicited from him after he had been indicted and in the absence of his counsel.” <em>Id., </em>at 206.</blockquote>
<p id="b311-5">We applied this principle most recently in <em>United States </em>v. <em>Henry, </em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">447 U. S. 264</a></span> (1980). Henry was arrested and indicted for bank robbery. Counsel was appointed, and Henry was held in jail pending trial. Nichols, an inmate at the same jail and a paid informant for the Federal Bureau of Investigation, told a Government agent that he was housed in the same cellblock as several federal prisoners, including Henry. The agent told Nichols to pay attention to statements made by these prisoners, but expressly instructed Nichols not to initiate any conversations and not to question Henry regarding the bank robbery. Nichols and Henry subsequently engaged in some conversations during which Henry told Nichols about the robbery. Nichols testified about these conversations at Henry’s trial, and Henry was convicted.</p>
<p id="b311-6">This Court reversed, finding that the Government had “ ‘deliberately elicited’ incriminating statements from Henry within the meaning of <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span>. </em>” <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#270" aria-description="Citation for case: Massiah v. United States"><em>Id., </em>at 270</a></span>. Several facts were emphasized in The Chief Justice’s opinion for the Court: that Nichols was acting as an informant for the Government and therefore had an incentive to produce useful information; that Henry was unaware of Nichols’ role as a Government informant; and, finally, that Henry and Nichols were incarcerated together at the time the conversations took place. With respect to this last fact, the Court reasoned that “confinement may bring into play subtle influences that will make [an individual] particularly susceptible to the ploys of undercover Government agents,” influences that were facilitated by Nichols’ “apparent status as a person sharing a common plight.” <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#274" aria-description="Citation for case: Massiah v. United States"><em>Id., </em>at 274</a></span>. Considering Nich<page-number citation-index="1" label="174">*174</page-number>ols’ conversations with Henry in light of these circumstances, the Court concluded that Nichols “deliberately used his position to secure incriminating information from Henry when counsel was not present” in violation of the Sixth Amendment. <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#270" aria-description="Citation for case: Massiah v. United States"><em>Id., </em>at 270-271</a></span>. The Government argued that it should not be held responsible for Nichols’ conduct because its agent had instructed Nichols not to question Henry and had not intended that Nichols take affirmative steps to obtain incriminating statements. We rejected this argument, finding that, under the circumstances, the agent “must have known” that Nichols would take affirmative steps to secure incriminating information. <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#271" aria-description="Citation for case: Massiah v. United States"><em>Id., </em>at 271</a></span>. Consequently, the Court held, “[b]y intentionally creating a situation likely to induce Henry to make incriminating statements without the assistance of counsel, the Government violated Henry’s Sixth Amendment right to counsel.” <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#274" aria-description="Citation for case: Massiah v. United States"><em>Id., </em>at 274</a></span>.</p>
<p id="b312-5">C</p>
<p id="b312-6">The State contends that the decisive fact in <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>and <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span> </em>was that the police set up the confrontation between the accused and a police agent at which incriminating statements were elicited. Supported by the United States as <em>amicus curiae, </em>the State maintains that the Sixth Amendment is violated only when police intentionally take this or some equivalent step. Because Moulton rather than Colson initiated the recorded telephone conversations and requested the December 26 meeting, the State concludes that Moulton’s Sixth Amendment rights were not violated here.</p>
<p id="b312-7">In the first place, the identity of the party who instigated the meeting at which the Government obtained incriminating statements was not decisive or even important to our decisions in <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>or <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span>. </em>Thus, while in <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>it may have been the Government agent who was responsible for setting up the meeting with the defendant,<footnotemark>10</footnotemark> one discovers <page-number citation-index="1" label="175">*175</page-number>this only by looking to the opinions of the Court of Appeals. It is not mentioned in this Court’s opinion since the issue of who set up the meeting with whom was not pertinent to our disposition. Moreover, four years after <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span>, </em>the Court summarily reversed a conviction where the defendant requested the meeting and initiated and led the conversation in which incriminating statements were made to an undercover informant. <em>Beatty </em>v. <em>United States, </em><span class="citation" data-id="1379716"><a href="/opinion/1379716/beatty-v-united-states/" aria-description="Citation for case: Beatty v. United States">389 U. S. 45</a></span> (1967) <em>(per curiam). </em>In that case, the Solicitor General made the same argument that he and the State make today, see Brief in Opposition, <em>Beatty </em>v. <em>United States, </em>O. T. 1967, No. 338, pp. 5-8; we rejected this argument in an opinion that simply cited Massiah.<footnotemark>11</footnotemark> Finally, in <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span>, </em>we deemed it “irrelevant that in <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>the agent had to arrange the meeting between Massiah and his codefendant while here the agents were fortunate enough to have an undercover informant already in close proximity to the accused.” <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#272" aria-description="Citation for case: United States v. Henry">447 U. S., at 272, n. 10</a></span>.</p>
<p id="b314-4"><page-number citation-index="1" label="176">*176</page-number>Beyond this, the State’s attempt to limit our holdings in <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>and <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span> </em>fundamentally misunderstands the nature of the right we recognized in those cases. The Sixth Amendment guarantees the accused, at least after the initiation of formal charges, the right to rely on counsel as a “medium” between him and the State. As noted above, this guarantee includes the State’s affirmative obligation not to act in a manner that circumvents the protections accorded the accused by invoking this right. The determination whether particular action by state agents violates the accused’s right to the assistance of counsel must be made in light of this obligation. Thus, the Sixth Amendment is not violated whenever — by luck or happenstance — the State obtains incriminating statements from the accused after the right to counsel has attached. See <em>Henry, </em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#276" aria-description="Citation for case: United States v. Henry">447 U. S., at 276</a></span> (Powell, J., concurring). However, knowing exploitation by the State of an opportunity to confront the accused without counsel being present is as much a breach of the State’s obligation not to circumvent the right to the assistance of counsel as is the intentional creation of such an opportunity. Accordingly, the Sixth Amendment is violated when the State obtains incriminating statements by knowingly circumventing the accused’s right to have counsel present in a confrontation between the accused and a state agent.<footnotemark>12</footnotemark></p>
<p id="b314-5">Ill</p>
<p id="b314-6">Applying this principle to the case at hand, it is clear that the State violated Moulton’s Sixth Amendment right when it arranged to record conversations between Moulton and its undercover informant, Colson. It was the police who suggested to Colson that he record his telephone conversations with Moulton. Having learned from these recordings that <page-number citation-index="1" label="177">*177</page-number>Moulton and Colson were going to meet, the police asked Colson to let them put a body wire transmitter on him to record what was said. Police Chief Keating admitted that, when they made this request, the police knew — as they must have known from the recorded telephone conversations— that Moulton and Colson were meeting for the express purpose of discussing the pending charges and planning a defense for the trial.<footnotemark>13</footnotemark> The police thus knew that Moulton would make statements that he had a constitutional right not to make to their agent prior to consulting with counsel. As in <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span>, </em>the fact that the police were “fortunate enough to have an undercover informant already in close proximity to the accused” does not excuse their conduct under these circumstances. <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#272" aria-description="Citation for case: United States v. Henry">447 U. S., at 272, n. 10</a></span>. By concealing the fact that Colson was an agent of the State, the police denied Moulton the opportunity to consult with counsel and thus denied him the assistance of counsel guaranteed by the Sixth Amendment.<footnotemark>14</footnotemark></p>
<p id="b316-7"><page-number citation-index="1" label="178">*178</page-number><em>&gt; </em>hH</p>
<p id="b316-1">The Solicitor General argues that the incriminating statements obtained by the Maine police nevertheless should not be suppressed because the police had other, legitimate reasons for listening to Moulton’s conversations with Colson, namely, to investigate Moulton’s alleged plan to kill Gary Elwell and to insure Colson’s safety. In <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span>, </em>the Government also contended that incriminating statements obtained as a result of its deliberate efforts should not be excluded because law enforcement agents had “the right, if not indeed the duty, to continue their investigation of [Massiah] and his alleged criminal associates . . . <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#206" aria-description="Citation for case: Massiah v. United States">377 U. S., at 206</a></span>. There, as here, the Government argued that this circumstance justified its surveillance and cured any improper acts or purposes. We rejected this argument, and held:</p>
<blockquote id="b317-4"><page-number citation-index="1" label="179">*179</page-number>“We do not question that in this case, as in many cases, it was entirely proper to continue an investigation of the suspected criminal activities of the defendant and his alleged confederates, even though the defendant had already been indicted. All that we hold is that the defendant’s own incriminating statements, obtained by federal agents under the circumstances here disclosed, could not constitutionally be used by the prosecution as evidence against him at his trial.” <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#207" aria-description="Citation for case: Massiah v. United States"><em>Id., </em>at 207</a></span> (emphasis omitted).</blockquote>
<p id="b317-5">We reaffirm this holding, which states a sensible solution to a difficult problem. The police have an interest in the thorough investigation of crimes for which formal charges have already been filed. They also have an interest in investigating new or additional crimes. Investigations of either type of crime may require surveillance of individuals already under indictment. Moreover, law enforcement officials investigating an individual suspected of committing one crime and formally charged with having committed another crime obviously seek to discover evidence useful at a trial of either crime.<footnotemark>15</footnotemark> In seeking evidence pertaining to pending charges, <page-number citation-index="1" label="180">*180</page-number>however, the Government’s investigative powers are limited by the Sixth Amendment rights of the accused. To allow the admission of evidence obtained from the accused in violation of his Sixth Amendment rights whenever the police assert an alternative, legitimate reason for their surveillance invites abuse by law enforcement personnel in the form of fabricated investigations and risks the evisceration of the Sixth Amendment right recognized in <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span>. </em>On the other hand, to exclude evidence pertaining to charges as to which the Sixth Amendment right to counsel had not attached at the time the evidence was obtained, simply because other charges were pending at that time, would unnecessarily frustrate the public’s interest in the investigation of criminal activities. Consequently, incriminating statements pertaining to pending charges are inadmissible at the trial of those charges, notwithstanding the fact that the police were also investigating other crimes, if, in obtaining this evidence, the State violated the Sixth Amendment by knowingly circumventing the accused’s right to the assistance of counsel.<footnotemark>16</footnotemark></p>
<p id="b318-5">Because we hold that the Maine police knowingly circumvented Moulton’s right to have counsel present at a confrontation between Moulton and a police agent, the fact that the police had additional reasons for recording Moulton’s meeting with Colson is irrelevant. The decision of the Supreme Judicial Court of Maine is affirmed.</p>
<p id="b318-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b299-5"> Indeed, in pursuing an anonymous tip received earlier that day that the stolen truck could be found at Belfast Dodge, one of the officers had conducted a consent search of the main building of the dealership facility.</p>
</footnote>
<footnote label="2">
<p id="b301-7"> Seven months after the conclusion of Moulton’s trial, Colson pleaded guilty to two counts of theft. The prosecutor recommended that Colson be sentenced to 2 years’ imprisonment, all but 15 days to be suspended, and placed on probation for 2 years. Colson also agreed to make restitution up to $2,000 diming the probationary period. The trial court accepted this recommendation and sentenced Colson accordingly.</p>
</footnote>
<footnote label="3">
<p id="b302-8"> Colson testified that he never told Moulton about the threatening calls that he had received.</p>
</footnote>
<footnote label="4">
<p id="b303-6"> The exchange went as follows:</p>
<p id="b303-7">“[Moulton:] You know I thought of a way to eliminate them. Remember we were talking about it before?</p>
<p id="b303-8">“[Colson:] Yes, you thought of a way?</p>
<p id="b303-9">“[Moulton:] Yeah, but... I don’t think we ought to go for it.</p>
<p id="b303-10">“[Colson:] Is it foolproof?</p>
<p id="b303-11">“[Moulton:] No.</p>
<p id="b303-12">“[Colson:] Is it, is it fairly foolproof?</p>
<p id="b303-13">“[Moulton:] I like it. I think its just for the ....</p>
<p id="b303-14">“[Colson:] Well let me [hear it].”</p>
<p id="b303-15">Moulton explained that he had considered using air rifles to shoot poisoned darts and the conversation then turned to joking about a magazine that instructed readers how to build bombs to kill large numbers of people. Exh. S-4, Tr. of Dec. 26 Meeting 18-19.</p>
</footnote>
<footnote label="5">
<p id="b304-6"> Colson began doing this immediately after Moulton vetoed the plan to eliminate witnesses. Colson indicated that he did not have copies of all the discovery materials, and Moulton went outside to his car to get his copies. While Moulton was gone, Colson sighed heavily and whispered “[o]h boy, I just hope I can make it through this” into the microphone. Then, when Moulton returned moments later, Colson immediately stated, slowly and deliberately: “I want you to help me with some dates. One date I cannot remember Caps [Moulton’s nickname], just can’t remember, I know it was in December, what night did we break into Lothrop Ford? What date?” <em>Id,., </em>at 23.</p>
</footnote>
<footnote label="6">
<p id="b307-6"> Justice Black explained in <em>Gideon </em>v. <em>Wainwright, </em><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span> (1963):</p>
<p id="AZ8">“[R]eason and reflection require us to recognize that in our adversary system of criminal justice, any person haled into court. . . cannot be assured a fair trial unless counsel is provided for him. This seems to us to be an obvious truth. Governments, both state and federal, quite properly spend vast sums of money to establish machinery to try defendants accused of crime. Lawyers to prosecute are everywhere deemed essential to protect the public’s interest in an orderly society. Similarly, there are few defendants charged with crime, few indeed, who fail to hire the best lawyers they can get to prepare and present their defenses. That government hires lawyers to prosecute and defendants who have the money hire lawyers to defend are the strongest indications of the widespread belief that lawyers in criminal courts are necessities, not luxuries. The right of one charged with crime to counsel may not be deemed fundamental and essential to fair trials in some countries, but it is in ours.” <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#344" aria-description="Citation for case: Gideon v. Wainwright"><em>Id., </em>at 344</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b308-9"> Cf. <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387</a></span> (1977): “[T]he lawyer is the essential medium through which the demands and commitments of the sover<page-number citation-index="1" label="171">*171</page-number>eign are communicated to the citizen. If, in the long run, we are seriously concerned about the individual’s effective representation by counsel, the State cannot be permitted to dishonor its promise to this lawyer.” <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#415" aria-description="Citation for case: Brewer v. Williams"><em>Id., </em>at 415</a></span> (Stevens, J., concurring) (footnote omitted).</p>
</footnote>
<footnote label="8">
<p id="b310-5"> The parties have taken pains to assure us that Massiah’s friend Colson and Moulton’s friend Colson are unrelated.</p>
</footnote>
<footnote label="9">
<p id="b310-6"> Justice Stewart noted that this view of the right to counsel “no more than reflects a constitutional principle established as long ago as <em>Powell </em>v. <em>Alabama, </em>” where the Court noted that</p>
<p id="b310-7">“ ‘during perhaps the most critical period of the proceedings . . . that is to say, from the time of their arraignment until the beginning of their trial, when consultation, thoroughgoing investigation and preparation [are] vitally important, the defendants [are] as much entitled to such aid [of counsel] ... as at the trial itself.’” <em>Massiah, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S., at 205</a></span> (quoting <em>Powell </em>v. <em>Alabama, </em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#57" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 57</a></span> (1932)).</p>
</footnote>
<footnote label="10">
<p id="b312-8"> It is not clear whether the informant asked to meet with Massiah or vice versa. Both the opinion for the Second Circuit and the dissent state <page-number citation-index="1" label="175">*175</page-number>only that, on the instructions of a Government agent, Colson invited Massiah into his ear to discuss their case; neither opinion establishes who requested the meeting in the first place. See <em>United States </em>v. <em>Massiah, </em><span class="citation" data-id="9448761"><a href="/opinion/258052/united-states-v-winston-massiah-mitchell-anfield-leonard-royal-aiken-and/#66" aria-description="Citation for case: United States v. Winston Massiah, Mitchell Anfield,...">307 F. 2d 62, 66</a></span> (1962); <span class="citation" data-id="9448761"><a href="/opinion/258052/united-states-v-winston-massiah-mitchell-anfield-leonard-royal-aiken-and/#72" aria-description="Citation for case: United States v. Winston Massiah, Mitchell Anfield,..."><em>id., </em>at 72</a></span> (Hays, J., dissenting). It is quite plausible that Massiah asked to see Colson who then proposed meeting in his car. In fact, there is nothing in the record in <em>Massiah </em>to support even the assertion of the Court of Appeals that Colson rather than Massiah suggested meeting in Colson’s car, although the inference is logical enough. See App. to Brief for United States in <em>Massiah </em>v. <em>United States, </em>O. T. 1963, No. 199, pp. 125a-175a (testimony of Agent Murphy).</p>
</footnote>
<footnote label="11">
<p id="b313-6"> In his <em>amicus </em>brief for the United States in this case, the Solicitor General suggests that <em><span class="citation" data-id="1379716"><a href="/opinion/1379716/beatty-v-united-states/" aria-description="Citation for case: Beatty v. United States">Beatty</a></span> </em>did not survive <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387</a></span> (1977), which, he contends, modified <em>Massiah </em>to require affirmative interrogation by the Government. Brief for United States as <em>Amicus Curiae </em>17, n. 12. <em>That </em>argument, however, was expressly rejected when the Solicitor General made it in <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span>. </em>See <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#271" aria-description="Citation for case: United States v. Henry">447 U. S., at 271</a></span> (“While affirmative interrogation, absent waiver, would certainly satisfy <em>Massiah, </em>we are not persuaded, as the Government contends, that <em>Brewer </em>v. <em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">Williams</a></span> . . . </em>modified Massiah’s ‘deliberately elicited’ test”). Cf. also, Brief for United States in <em>United States </em>v. <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span>, </em>O. T. 1979, No. 121, p. 26, n. 12.</p>
</footnote>
<footnote label="12">
<p id="b314-7"> Direct proof of the State’s knowledge will seldom be available to the accused. However, as <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span> </em>makes clear, proof that the State “must have known” that its agent was likely to obtain incriminating statements from the accused in the absence of counsel suffices to establish a Sixth Amendment violation. See <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#271" aria-description="Citation for case: United States v. Henry">447 U. S., at 271</a></span>.</p>
</footnote>
<footnote label="13">
<p id="b315-5"> Because Moulton thought of Colson only as his codefendant, Colson’s engaging Moulton in active conversation about their upcoming trial was certain to elicit statements that Moulton would not intentionally reveal— and had a constitutional right not to reveal — to persons known to be police agents. Under these circumstances, Colson’s merely participating in this conversation was “the functional equivalent of interrogation.” <em>Henry, </em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#277" aria-description="Citation for case: United States v. Henry">447 U. S., at 277</a></span> (Powell, J., concurring). In addition, the tapes disclose and the Supreme Judicial Court of Maine found that Colson “frequently pressed Moulton for details of various thefts and in so doing elicited much incriminating information that the State later used at trial.” <span class="citation" data-id="2009182"><a href="/opinion/2009182/state-v-moulton/#161" aria-description="Citation for case: State v. Moulton">481 A. 2d, at 161</a></span>. Thus, as in <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#271" aria-description="Citation for case: United States v. Henry"><em>Henry, supra, </em>at 271, n. 9</a></span>, we need not reach the situation where the “listening post” cannot or does not participate in active conversation and prompt particular replies.</p>
</footnote>
<footnote label="14">
<p id="b315-6"> The State argues that it took steps to prevent Colson from inducing Moulton to make incriminating admissions by instructing Colson to “be himself,” “act normal,” and “not interrogate” Moulton. Tr. of Hearing on Motion to Suppress 42, 51, 56. In <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span>, </em>we rejected this same argument although the likelihood that the accused would talk about the pending charges to a cellmate was less than here, where the accused invited his co-defendant to discuss the upcoming trial, and although the instructions to the agent were far more explicit. See <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#268" aria-description="Citation for case: United States v. Henry">447 U. S., at 268, 271</a></span>. More im<page-number citation-index="1" label="178">*178</page-number>portantly, under the circumstances of this ease, the instructions given to Colson were necessarily inadequate. The Sixth Amendment protects the right of the accused not to be confronted by an agent of the State regarding matters as to which the right to counsel has attached without counsel being present. This right was violated as soon as the State’s agent engaged Moulton in conversation about the charges pending against him. Because these charges were the only subject to be discussed at Colson’s December 26 meeting with Moulton, a Sixth Amendment violation was inevitable once Colson agreed to this meeting with Moulton.</p>
<p id="b316-4">In any event, we reject the State’s suggestion that these instructions were designed to protect Moulton’s constitutional rights. The instructions were obviously motivated by the police’s concern that Colson, who had never before served as an undercover agent, might behave unnaturally or ask too many questions, thereby tipping Moulton off to the fact that Colson was cooperating with the police. Thus, rather than explain to Colson that actively questioning Moulton might taint any evidence obtained, the police simply told Colson to “be himself,” and to “act normal.” Tr. of Hearing on Motion to Suppress 42, 51, 56. In addition, the instructions were not limited to questions concerning the pending charges, the only matters as to which active questioning might create problems. On the contrary, according to Chief Keating, Colson was instructed that he could engage Moulton in a conversation but should not try to draw him out on “elimination of witnesses or anything.” <em>Id., </em>at 51.</p>
</footnote>
<footnote label="15">
<p id="b317-6"> In his brief, the Solicitor General assumes that the only claim made by the Government and answered by the Court in <em>Massiah </em>was that the Government was engaged in a continuing investigation of crimes as to which charges were already pending. He concedes that this was an inadequate justification which “had the flavor of a post hoc rationalization of conduct that, at its inception, in fact had as a primary purpose the obtaining of evidence for use at trial on the pending charges.” Brief for United States as <em>Amicus Curiae </em>23-24. So saying, he asks us to distinguish from that justification the justification that law enforcement officials are investigating “separate” crimes. In <em>Massiah, </em>however, the Government’s assertion was that it needed to continue its investigation in order to discover the identities of Massiah’s intended buyer and of others who were importing narcotics as well as to find additional evidence of Massiah’s crimes. Brief for United States in <em>Massiah </em>v. <em>United States, </em>O. T. 1963, No. 199, pp. 26-27. The Court in <em>Massiah </em>was thus faced with the very same argument made by the Solicitor General in this case. Even were the Solicitor General’s characterization of the issue posed in <em>Massiah </em>correct, however, <page-number citation-index="1" label="180">*180</page-number>we would not draw the distinction he asks us to make. The likelihood of <em>post hoc </em>rationalizing is the same whether police claim to be investigating other examples of the same crime or some allegedly “separate” crime. We take what we feel is a more realistic view of police investigations, and instead accept that dual purposes may exist whenever police have more than one reason to investigate someone.</p>
</footnote>
<footnote label="16">
<p id="b318-8"> Incriminating statements pertaining to other crimes, as to which the Sixth Amendment right has not yet attached, are, of course, admissible at a trial of those offenses.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Malley v. Briggs.md  (`case`, 6 assertions)

### content_page

```
---
title: "Malley v. Briggs"
type: case
citation: "475 U.S. 335 (1986)"
parallel_cite: "106 S. Ct. 1092; 89 L. Ed. 2d 271; 54 U.S.L.W. 4243"
neutral_cite: 1986 U.S. LEXIS 29
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1986
date_decided: 1986-03-05
docket: 84-1586
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1986-03-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Malley v. Briggs
  varies_by_point: false
  scope_note: "Good law: officers applying for warrants get qualified, not absolute, immunity; the 'no reasonably competent officer' standard governs."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111611/malley-v-briggs/"
  cluster_id: 111611
  opinion_id: 9430379
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Franks Challenges]]"
    role: "Related (cross-doctrine)"
related: ["[[Messerschmidt v. Millender]]", "[[United States v. Leon]]", "[[Harlow v. Fitzgerald]]"]
aliases: []
tags: ["case", "section-1983", "qualified-immunity", "warrant", "probable-cause", "objective-reasonableness"]
holding: "An officer who applies for a warrant on an affidavit so lacking in probable cause that no reasonably competent officer would have sought it loses qualified immunity; warrant-applying officers get qualified, not absolute, immunity."
lake:
  record_id: Malley v. Briggs
  status: verified
  projected_at: 2026-07-06
---

# Malley v. Briggs

*475 U.S. 335 (1986)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Rhode Island state trooper Malley, relying on court-authorized wiretap intercepts, drew up felony complaints and supporting affidavits charging James and Louise Briggs with a marijuana offense. A state judge signed the arrest warrants and the Briggses were arrested, but the grand jury did not indict and the charges were dropped. The Briggses sued Malley under § 1983, alleging the affidavit did not establish probable cause. Malley claimed he was absolutely immune because a judge had issued the warrant.

## Issue
Whether an officer who applies for and obtains an arrest warrant is entitled to absolute immunity from a § 1983 damages suit, or only to [[Qualified Immunity|qualified immunity]] — and if the latter, what the standard is.

## Rule
The officer gets **qualified**, not absolute, immunity, judged by the objective-reasonableness standard of *[[Harlow v. Fitzgerald|Harlow]]* and *[[United States v. Leon|Leon]]*. "Defendants will not be immune if, on an objective basis, it is obvious that no reasonably competent officer would have concluded that a warrant should issue; but if officers of reasonable competence could disagree on this issue, immunity should be recognized." — 475 U.S. at 341. ^pin-341

The magistrate's approval does not automatically immunize the officer: the question is "whether a reasonably well-trained officer in petitioner's position would have known that his affidavit failed to establish probable cause and that he should not have applied for the warrant." — *Id.* at 345. ^pin-345

[[Qualified Immunity|Qualified immunity]] thus protects "all but the plainly incompetent or those who knowingly violate the law." — *Id.* at 341.

## Application
Malley argued that by presenting the affidavit to a judge he passed responsibility to the magistrate and earned absolute immunity. The Court rejected that: an officer who submits an affidavit that no reasonably competent officer would think establishes probable cause "created the unnecessary danger of an unlawful arrest" and cannot hide behind the magistrate's signature. Whether Malley's affidavit met that standard was a question for trial, so the Court [[Reading and Citing Cases#on-remand|remanded]] for application of the objective-reasonableness test.

## Conclusion
Affirmed in part and [[Reading and Citing Cases#on-remand|remanded]]. Officers who apply for warrants enjoy only [[Qualified Immunity|qualified immunity]]; immunity is lost where no reasonably competent officer would have concluded the warrant should issue.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Malley* supplies the warrant-application immunity standard later applied in [[Messerschmidt v. Millender]] and paired with the good-faith analysis of [[United States v. Leon]]; the "plainly incompetent or those who knowingly violate the law" formulation is a staple of the [[Harlow v. Fitzgerald]] qualified-immunity line. No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*
- [[Franks Challenges]] — *Related (cross-doctrine)*

## Sources
- *Malley v. Briggs*, 475 U.S. 335 (1986) — https://www.courtlistener.com/opinion/111611/malley-v-briggs/ — pinpoints: 341, 345.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "825208ef990459f7", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "475 U.S. 335 (1986)", "court": "U.S. Supreme Court", "neutral_cite": "1986 U.S. LEXIS 29", "official_citation_present": true, "parallel_cite": "106 S. Ct. 1092; 89 L. Ed. 2d 271; 54 U.S.L.W. 4243", "title": "Malley v. Briggs", "year": "1986"}}
{"assertion_id": "13b35631dc2f80bc", "dimension": "support", "kind": "home_role", "locator": {"home": "Franks Challenges"}, "payload": {"home": "Franks Challenges", "role": "Related (cross-doctrine)", "title": "Malley v. Briggs"}}
{"assertion_id": "64eaa1939625b08d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An officer who applies for a warrant on an affidavit so lacking in probable cause that no reasonably competent officer would have sought it loses qualified immunity; warrant-applying officers get qualified, not absolute, immunity.", "title": "Malley v. Briggs"}}
{"assertion_id": "885bf935483d1381", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "Malley v. Briggs"}}
{"assertion_id": "b33820badd4a0dca", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Malley v. Briggs"}}
{"assertion_id": "ee2289ee10660c87", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1986-03-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Malley v. Briggs", "field_i_validity": "good_law", "scope_note": "Good law: officers applying for warrants get qualified, not absolute, immunity; the 'no reasonably competent officer' standard governs.", "title": "Malley v. Briggs", "varies_by_point": "false"}}
```

### lake record — Malley v. Briggs

```json
{
  "schema_version": "s2.v1",
  "record_id": "Malley v. Briggs",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Malley v. Briggs",
    "case_name_short": "Malley",
    "case_name_full": "MALLEY Et Al. v. BRIGGS Et Al.",
    "input_case_name": "Malley v. Briggs",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-03-05",
    "year": 1986,
    "docket": "84-1586",
    "cluster_id": 111611,
    "lead_opinion_id": 9430379,
    "sibling_ids": [
      111611,
      9430379,
      9430380
    ],
    "absolute_url": "/opinion/111611/malley-v-briggs/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "475 U.S. 335",
      "volume": "475",
      "reporter": "U.S.",
      "page": "335",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "106 S. Ct. 1092",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1092",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 271",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "271",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4243",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4243",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 29",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "29",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "475 U.S. 335",
        "volume": "475",
        "reporter": "U.S.",
        "page": "335",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 1092",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1092",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 271",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "271",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 29",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "29",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4243",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4243",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "475 U.S. 335",
    "official_selection": {
      "court_class": "scotus",
      "selected": "475 U.S. 335",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-341",
      "page": null,
      "quote": "--- # Malley v. Briggs *475 U.S. 335 (1986)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Rhode Island state trooper Malley, relying on court-authorized wiretap intercepts, drew up felony complaints and supporting affidavits charging James and Louise Briggs with a marijuana offense. A state judge signed the arrest warrants and the Briggses were arrested, but the grand jury did not indict and the charges were dropped. The Briggses sued Malley under \u00a7 1983, alleging the affidavit did not establish probable cause. Malley claimed he was absolutely immune because a judge had issued the warrant. ## Issue Whether an officer who applies for and obtains an arrest warrant is entitled to absolute immunity from a \u00a7 1983 damages suit, or only to qualified immunity \u2014 and if the latter, what the standard is. ## Rule The officer gets **qualified**, not absolute, immunity, judged by the objective-reasonableness standard of *Harlow* and *Leon*.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-345",
      "page": null,
      "quote": "whether a reasonably well-trained officer in petitioner's position would have known that his affidavit failed to establish probable cause and that he should not have applied for the warrant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1986-03-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Malley v. Briggs",
    "varies_by_point": false,
    "scope_note": "Good law: officers applying for warrants get qualified, not absolute, immunity; the 'no reasonably competent officer' standard governs.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "C.M. v. Commissioner of the Department of Children and Families",
          "cluster_id": 4747689,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Harris County, Texas and Kevin Vailes v. Barbara Coats, Individually, as Personal Representative of the Estate of Jamail Amron, and as Heir to the Estate of Jamail Amron, And Ali Amron, Individually and as Heir to the Estate of Jamail Amron, Barbara Coats",
          "cluster_id": 4725124,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Heck v. Humphrey",
          "cluster_id": 117864,
          "cite": [
            "129 L. Ed. 2d 383",
            "114 S. Ct. 2364",
            "512 U.S. 477",
            "1994 U.S. LEXIS 4824"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anderson v. Creighton",
          "cluster_id": 111953,
          "cite": [
            "97 L. Ed. 2d 523",
            "107 S. Ct. 3034",
            "483 U.S. 635",
            "1987 U.S. LEXIS 2894",
            "55 U.S.L.W. 5092"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hope v. Pelzer",
          "cluster_id": 121169,
          "cite": [
            "153 L. Ed. 2d 666",
            "122 S. Ct. 2508",
            "536 U.S. 730",
            "2002 U.S. LEXIS 4884"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Lacey v. Joseph Arpaio",
          "cluster_id": 807646,
          "cite": [
            "693 F.3d 896"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mullenix v. Luna",
          "cluster_id": 3153112,
          "cite": [
            "577 U.S. 7",
            "136 S. Ct. 305",
            "193 L. Ed. 2d 255",
            "2015 U.S. LEXIS 7160",
            "84 U.S.L.W. 4003",
            "25 Fla. L. Weekly Fed. S 555"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hunter v. Bryant",
          "cluster_id": 112671,
          "cite": [
            "116 L. Ed. 2d 589",
            "112 S. Ct. 534",
            "502 U.S. 224",
            "1991 U.S. LEXIS 7262"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ziglar v. Abbasi",
          "cluster_id": 4403804,
          "cite": [
            "582 U.S. 120",
            "2017 U.S. LEXIS 3874",
            "137 S. Ct. 1843",
            "198 L. Ed. 2d 290",
            "26 Fla. L. Weekly Fed. S 655",
            "85 U.S.L.W. 4360",
            "2017 WL 2621317"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ashcroft v. al-Kidd",
          "cluster_id": 217703,
          "cite": [
            "179 L. Ed. 2d 1149",
            "131 S. Ct. 2074",
            "563 U.S. 731",
            "2011 U.S. LEXIS 4021"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
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
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Buckley v. Fitzsimmons",
          "cluster_id": 112894,
          "cite": [
            "125 L. Ed. 2d 209",
            "113 S. Ct. 2606",
            "509 U.S. 259",
            "1993 U.S. LEXIS 4400"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
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
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Burns v. Reed",
          "cluster_id": 112606,
          "cite": [
            "114 L. Ed. 2d 547",
            "111 S. Ct. 1934",
            "500 U.S. 478",
            "1991 U.S. LEXIS 3018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miller v. Gammie",
          "cluster_id": 8437592,
          "cite": [
            "335 F.3d 889",
            "2003 WL 21540416"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barbara Payne v. Michael Pauley",
          "cluster_id": 782880,
          "cite": [
            "337 F.3d 767",
            "2003 U.S. App. LEXIS 13807",
            "2003 WL 21540424"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Groh v. Ramirez",
          "cluster_id": 131161,
          "cite": [
            "157 L. Ed. 2d 1068",
            "124 S. Ct. 1284",
            "540 U.S. 551",
            "2004 U.S. LEXIS 1624",
            "2004 WL 330057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kalina v. Fletcher",
          "cluster_id": 118156,
          "cite": [
            "139 L. Ed. 2d 471",
            "118 S. Ct. 502",
            "522 U.S. 118",
            "1997 U.S. LEXIS 7498"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kathleen Hansen v. Ronald L. Black",
          "cluster_id": 529383,
          "cite": [
            "885 F.2d 642",
            "1989 U.S. App. LEXIS 13906",
            "1989 WL 106525"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miller v. Gammie",
          "cluster_id": 782687,
          "cite": [
            "335 F.3d 889",
            "2003 Daily Journal DAR 7566",
            "2003 U.S. App. LEXIS 13720"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Lancaster v. Chambers",
          "cluster_id": 1524989,
          "cite": [
            "883 S.W.2d 650",
            "37 Tex. Sup. Ct. J. 980",
            "1994 Tex. LEXIS 101",
            "1994 WL 264968"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wyatt v. Cole",
          "cluster_id": 112733,
          "cite": [
            "118 L. Ed. 2d 504",
            "112 S. Ct. 1827",
            "504 U.S. 158",
            "1992 U.S. LEXIS 2702"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Weyant v. Okst",
          "cluster_id": 7040522,
          "cite": [
            "101 F.3d 845",
            "1996 WL 689976"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spavone v. New York State Department of Correctional Services",
          "cluster_id": 903750,
          "cite": [
            "719 F.3d 127",
            "2013 WL 3064853",
            "2013 U.S. App. LEXIS 12549"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Owens v. Baltimore City State's Attorneys Office",
          "cluster_id": 2736472,
          "cite": [
            "767 F.3d 379",
            "2014 U.S. App. LEXIS 18294",
            "2014 WL 4723803"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Messerschmidt v. Millender",
          "cluster_id": 623242,
          "cite": [
            "182 L. Ed. 2d 47",
            "132 S. Ct. 1235",
            "565 U.S. 535",
            "2012 U.S. LEXIS 1687"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Weyant v. Okst",
          "cluster_id": 730829,
          "cite": [
            "101 F.3d 845",
            "1996 U.S. App. LEXIS 31034"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malley v. Briggs:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111611 OR 9430379 OR 9430380) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTY4Njc4NDAwMDAwJnM9NDY2MTQzNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111611+OR+9430379+OR+9430380%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111611 OR 9430379 OR 9430380)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NTEmcz02NjAxNjYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111611+OR+9430379+OR+9430380%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111611 OR 9430379 OR 9430380)",
        "reviewed": 94,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 94,
        "triage_read": 0,
        "triage_snippet_classified": 94
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111611 OR 9430379 OR 9430380)",
    "indexed_citing_opinions": 3310,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111611,
        "count": 2834,
        "count_source": "search"
      },
      {
        "opinion_id": 9430379,
        "count": 512,
        "count_source": "search"
      },
      {
        "opinion_id": 9430380,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6783,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/malley-v-briggs.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNzc4NzImcz0xMDM2ODAxMiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111611+OR+9430379+OR+9430380%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111611,
        "cited_id": 86704,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 107411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 108582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 109199,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 109387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 109516,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 109932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 110100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 110132,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 110236,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 110885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 111224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111611,
        "cited_id": 444547,
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
    "date_created": "2026-07-05T11:17:05Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:17:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:17:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:23:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:17:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Malley v. Briggs

```
<opinion type="majority">
<author id="AJd"><page-number citation-index="1" label="337">*337</page-number>Justice White</author>
<p id="ASt">delivered the opinion of the Court.</p>
<p id="ACR">This case presents the question of the degree of immunity accorded a defendant police officer in a damages action under <span class="citation no-link">42 U. S. C. § 1983</span> when it is alleged that the officer caused the plaintiffs to be unconstitutionally arrested by presenting a judge with a complaint and a supporting affidavit which failed to establish probable cause.</p>
<p id="ANhr">) — I</p>
<p id="Ava">In December 1980, the Rhode Island State Police were conducting a court-authorized wiretap on the telephone of one Paul Driscoll, an acquaintance of respondents’ daughter. On December 20, the police intercepted a call to Driscoll from an unknown individual who identified himself as “Dr. Shogun.” The police logsheet summarizes the call as follows: “General conversation re. a party they went to last night. . . caller says I can’t believe I was token <em>[sic] </em>in front of Jimmy Briggs — caller states he passed it to Louisa . . . Paul says Nancy was sitting in his lap rolling her thing.” App. 78.</p>
<p id="Ar_7">Petitioner Edward Malley (hereafter petitioner) was the Rhode Island state trooper in charge of the investigation of Driscoll. After reviewing the logsheet for December 20, petitioner decided that the call from “Dr. Shogun” was incriminating, because in drug parlance “toking” means smoking marihuana and “rolling her thing” refers to rolling a mari<page-number citation-index="1" label="338">*338</page-number>huana cigarette. Petitioner also concluded that another call monitored the same day showed that the party discussed by Driscoll and “Dr. Shogun” took place at respondents’ house. On the basis of these two calls, petitioner drew up felony complaints charging that respondents and Paul Driscoll “did unlawfully conspire to violate the uniform controlled substance act of the State of Rhode Island by having [marihuana] in their possession . . . .” <span class="citation no-link"><em>Id., </em>at 74</span>. These complaints were presented to a State District Court Judge in February 1981, after the wiretap of Driscoll’s phone had been terminated. Accompanying the complaints were unsigned warrants for each respondent’s arrest, and supporting affidavits describing the two intercepted calls and petitioner’s interpretation of them. The judge signed warrants for the arrest of respondents and 20 other individuals charged by petitioner as a result of information gathered through the wiretap.</p>
<p id="b420-5">Respondents were arrested at their home shortly before six o’clock on the morning of March 19, 1981. They were taken to a police station, booked, held for several hours, arraigned, and released. Local and statewide newspapers published the fact that respondents, who are prominent members of their community, had been arrested and charged with drug possession. The charges against repondents were subsequently dropped when the grand jury to which the case was presented did not return an indictment.</p>
<p id="b420-6">Respondents brought an action under <span class="citation no-link">42 U. S. C. § 1983</span> in the United States District Court for the District of Rhode Island charging, <em>inter alia, </em>that petitioner, in applying for warrants for their arrest, violated their rights under the Fourth and Fourteenth Amendments. The case was tried to a jury, and at the close of respondents’ evidence, petitioner moved for and was granted a directed verdict.<footnotemark>1</footnotemark> The District <page-number citation-index="1" label="339">*339</page-number>Court’s primary justification for directing a verdict was that the act of the judge in issuing the arrest warrants for respondents broke the causal chain between petitioner’s filing of a complaint and respondents’ arrest. The court also stated that an officer who believes that the facts stated in his affidavit are true and who submits them to a neutral magistrate may thereby be entitled to immunity under the “objective reasonableness” standard of <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800</a></span> (1982).</p>
<p id="b421-5">The United States Court of Appeals for the First Circuit reversed, holding that an officer who seeks an arrest warrant by submitting a complaint and supporting affidavit to a judge is not entitled to immunity unless the officer has an objectively reasonable basis for believing that the facts alleged in his affidavit are sufficient to establish probable cause. <span class="citation" data-id="9472839"><a href="/opinion/444547/james-r-briggs-and-louisa-briggs-v-edward-malley/" aria-description="Citation for case: James R. Briggs and Louisa Briggs v. Edward Malley">748 F. 2d 715</a></span> (1984). We granted certiorari in order to review the First Circuit’s application of the “objective reasonableness” standard in this context. <span class="citation multiple-matches"><a href="/c/U.%20S./471/1124/">471 U. S. 1124</a></span> (1985). We affirm.</p>
<p id="b421-6">II</p>
<p id="b421-7">Petitioner urges reversal on two grounds: first, that in this context, he is absolutely immune from liability for damages; second, that he is at least entitled to qualified immunity in this case. We reject both propositions and address first the absolute immunity issue.</p>
<p id="b421-8">A</p>
<p id="b421-9">Our general approach to questions of immunity under § 1983 is by now well established. Although the statute on its face admits of no immunities, we have read it “in harmony with general principles of tort immunities and defenses rather than in derogation of them.” <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#418" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409, 418</a></span> (1976). Our initial inquiry is whether an official claiming immunity under §1983 can point to a <page-number citation-index="1" label="340">*340</page-number>common-law counterpart to the privilege he asserts. <em>Tower </em>v. <em>Glover, </em><span class="citation" data-id="9842065"><a href="/opinion/111224/tower-v-glover/" aria-description="Citation for case: Tower v. Glover">467 U. S. 914</a></span> (1984). If “an official was accorded immunity from tort actions at common law when the Civil Rights Act was enacted in 1871, the Court next considers whether §1983’s history or purposes nonetheless counsel against recognizing the same immunity in § 1983 actions.” <em>Id., </em>at 920. Thus, while we look to the common law for guidance, we do not assume that Congress intended to incorporate every common-law immunity into §1983 in unaltered form.</p>
<p id="b422-5">Our cases also make plain that “[f]or executive officers in general, . . . qualified immunity represents the norm.” <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#807" aria-description="Citation for case: Harlow v. Fitzgerald"><em>Harlow, supra, </em>at 807</a></span>.<footnotemark>2</footnotemark> Like federal officers, state officers who “seek absolute exemption from personal liability for unconstitutional conduct must bear the burden of showing that public policy requires an exemption of that scope.” <em>Butz </em>v. <em>Economou, </em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#506" aria-description="Citation for case: Butz v. Economou">438 U. S. 478, 506</a></span> (1978).</p>
<p id="b422-6">B</p>
<p id="b422-7">Although we have previously held that police officers sued under § 1983 for false arrest are qualifiedly immune, <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#557" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547, 557</a></span> (1967), petitioner urges that he should be absolutely immune because his function in seeking an arrest warrant was similar to that of a complaining witness. The difficulty with this submission is that complaining witnesses were not absolutely immune at common law. In 1871, the generally accepted rule was that one who procured the issuance of an arrest warrant by submitting a complaint could be held liable if the complaint was made maliciously and <page-number citation-index="1" label="341">*341</page-number>without probable cause.<footnotemark>3</footnotemark> Given malice and the lack of probable cause, the complainant enjoyed no immunity. The common law thus affords no support for petitioner.</p>
<p id="b423-5">Nor are we moved by petitioner’s argument that policy considerations require absolute immunity for the officer applying for a warrant. As the qualified immunity defense has evolved, it provides ample protection to all but the plainly incompetent or those who knowingly violate the law. At common law, in cases where probable cause to arrest was lacking, a complaining witness’ immunity turned on the issue of malice, which was a jury question.<footnotemark>4</footnotemark> Under the <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>standard, on the other hand, an allegation of malice is not sufficient to defeat immunity if the defendant acted in an objectively reasonable manner. The <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>standard is specifically designed to “avoid excessive disruption of government and permit the resolution of many insubstantial claims on summary judgment,” and we believe it sufficiently serves this goal. Defendants will not be immune if, on an objective basis, it is obvious that no reasonably competent officer would have concluded that a warrant should issue; but if officers of reasonable competence could disagree on this issue, immunity should be recognized.</p>
<p id="b423-6">C</p>
<p id="b423-7">As an alternative ground for claiming absolute immunity, petitioner draws an analogy between an officer requesting a warrant and a prosecutor who asks a grand jury to indict a suspect. Like the prosecutor, petitioner argues, the officer must exercise a discretionary judgment based on the evi<page-number citation-index="1" label="342">*342</page-number>dence before him, and like the prosecutor, the officer may not exercise his best judgment if the threat of retaliatory lawsuits hangs over him. Thus, petitioner urges us to read § 1983 as giving the officer the same absolute immunity enjoyed by the prosecutor. Cf. <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409</a></span> (1976).</p>
<p id="b424-5">We reemphasize that our role is to interpret the intent of Congress in enacting § 1983, not to make a freewheeling policy choice, and that we are guided in interpreting Congress’ intent by the common-law tradition. In <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Imbler, supra,</a></span> </em>we concluded that at common law “[t]he general rule was, and is, that a prosecutor is absolutely immune from suit for malicious prosecution.” <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#437" aria-description="Citation for case: Imbler v. Pachtman"><em>Id., </em>at 437</a></span>. We do not find a comparable tradition of absolute immunity for one whose complaint causes a warrant to issue. See n. 3, <em>supra. </em>While this observation may seem unresponsive to petitioner’s policy argument, it is, we believe, an important guide to interpreting § 1983. Since the statute on its face does not provide for <em>any </em>immunities, we would be going far to read into it an absolute immunity for conduct which was only accorded qualified immunity in 1871.</p>
<p id="b424-6">Even were we to overlook the fact that petitioner is inviting us to expand what was a qualified immunity at common law into an absolute immunity, we would find his analogy between himself and a prosecutor untenable. We have interpreted § 1983 to give absolute immunity to functions “intimately associated with the <em>judicial </em>phase of the criminal process,” <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#430" aria-description="Citation for case: Imbler v. Pachtman"><em>Imbler, supra, </em>at 430</a></span> (emphasis added), not from an exaggerated esteem for those who perform these functions, and certainly not from a desire to shield abuses of office, but because any lesser degree of immunity could impair the judicial process itself. <em>Briscoe </em>v. <em>LaHue, </em><span class="citation" data-id="9429107"><a href="/opinion/110885/briscoe-v-lahue/#334" aria-description="Citation for case: Briscoe v. LaHue">460 U. S. 325, 334-335</a></span> (1983). We intend no disrespect to the officer applying for a warrant by observing that his action, while a vital part of the administration of criminal justice, is further removed from the judicial phase of criminal proceedings than <page-number citation-index="1" label="343">*343</page-number>the act of a prosecutor in seeking an indictment. Furthermore, petitioner’s analogy, while it has some force, does not take account of the fact that the prosecutor’s act in seeking an indictment is but the first step in the process of seeking a conviction. Exposing the prosecutor to liability for the initial phase of his prosecutorial work could interfere with his exercise of independent judgment at every phase of his work, since the prosecutor might come to see later decisions in terms of their effect on his potential liability. Thus, we shield the prosecutor seeking an indictment because any lesser immunity could impair the performance of a central actor in the judicial process.<footnotemark>5</footnotemark></p>
<p id="b425-5">In the case of the officer applying for a warrant, it is our judgment that the judicial process will on the whole benefit from a rule of qualified rather than absolute immunity. We do not believe that the <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>standard, which gives ample room for mistaken judgments, will frequently deter an officer from submitting an affidavit when probable cause to make an arrest is present. True, an officer who knows that objectively unreasonable decisions will be actionable may be motivated to reflect, before submitting a request for a warrant, upon whether he has a reasonable basis for believing that his affidavit establishes probable cause. But such reflection is desirable, because it reduces the likelihood that the officer’s request for a warrant will be premature. Premature requests for warrants are at best a waste of judicial resources; at worst, they lead to premature arrests, which may injure the <page-number citation-index="1" label="344">*344</page-number>innocent or, by giving the basis for a suppression motion, benefit the guilty.</p>
<p id="b426-5">Furthermore, it would be incongruous to test police behavior by the “objective reasonableness” standard in a suppression hearing, see <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U. S. 897</a></span> (1984), while exempting police conduct in applying for an arrest or search warrant from any scrutiny whatsoever in a § 1988 damages action.<footnotemark>6</footnotemark> While we believe the exclusionary rule serves a necessary purpose, it obviously does so at a considerable cost to society as a whole, because it excludes evidence probative of guilt. On the other hand, a damages remedy for an arrest following an objectively unreasonable request for a warrant imposes a cost directly on the officer responsible for the unreasonable request, without the side effect of hampering a criminal prosecution. Also, in the case of the § 1983 action, the likelihood is obviously greater than at the suppression hearing that the remedy is benefiting the victim of police misconduct one would think most deserving of a remedy — the person who in fact has done no wrong, and has been arrested for no reason, or a bad reason. See <em>Owen </em>v. <em>City of Independence, </em><span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/#653" aria-description="Citation for case: Owen v. City of Independence">445 U. S. 622, 653</a></span> (1980).</p>
<p id="b426-6">Accordingly, we hold that the same standard of objective reasonableness that we applied in the context of a suppression hearing in <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon, supra,</a></span> </em>defines the qualified immunity accorded an officer whose request for a warrant allegedly caused an unconstitutional arrest.<footnotemark>7</footnotemark> Only where the warrant <page-number citation-index="1" label="345">*345</page-number>application is so lacking in indicia of probable cause as to render official belief in its existence unreasonable, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#923" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 923</a></span>, will the shield of immunity be lost.</p>
<p id="ApC">I — I f — H HH</p>
<p id="AHK">We also reject petitioner’s argument that if an officer is entitled to only qualified immunity in cases like this, he is nevertheless shielded from damages liability because the act of applying for a warrant is <em>per se </em>objectively reasonable, provided that the officer believes that the facts alleged in his affidavit are true. Petitioner insists that he is entitled to rely on the judgment of a judicial officer in finding that probable cause exists and hence issuing the warrant. This view of objective reasonableness is at odds with our development of that concept in <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>and <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>. </em>In <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>, </em>we stated that “our good-faith inquiry is confined to the objectively ascertainable question whether a reasonably well-trained officer would have known that the search was illegal despite the magistrate’s authorization.” <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon">468 U. S., at 922, n. 23</a></span>. The analogous question in this case is whether a reasonably well-trained officer in petitioner’s position would have known that his affidavit failed to establish probable cause and that he should not have applied for the warrant.<footnotemark>8</footnotemark> If such was the case, the officer’s application for a warrant was not objectively reasonable, because it created the unnecessary danger of an unlawful arrest. It is true that in an ideal system an unreasonable request for a warrant would be harmless, because no judge would approve it. But ours is not an ideal system, and it is possible that a magistrate, working under <page-number citation-index="1" label="346">*346</page-number>docket pressures, will fail to perform as a magistrate should. We find it reasonable to require the officer applying for the warrant to minimize this danger by exercising reasonable professional judgment.<footnotemark>9</footnotemark></p>
<p id="Aog">The judgment of the Court of Appeals is affirmed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="AxXz">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b420-7"> Respondents’ complaint also named the State of Rhode Island as a defendant. At the close of respondents’ evidence, Rhode Island moved for and was granted a directed verdict on Eleventh Amendment grounds. Re<page-number citation-index="1" label="339">*339</page-number>spondents have not contested the propriety of the directed verdict for the State.</p>
</footnote>
<footnote label="2">
<p id="b422-8"> <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>was a suit against federal, not state, officials, but as we stated in deciding the case, it is “ ‘untenable to draw a distinction for purposes of immunity law between suits brought against state officials under § 1983 and suits brought directly under the Constitution against federal officials.”’ <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 818</a></span>, n. 30 (quoting <em>Butz </em>v. <em>Economou, </em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#504" aria-description="Citation for case: Butz v. Economou">438 U. S. 478, 504</a></span> (1978)).</p>
</footnote>
<footnote label="3">
<p id="b423-8"> See, <em>e. g., Dinsman </em>v. <em>Wilkes, </em><span class="citation" data-id="86704"><a href="/opinion/86704/dinsman-v-wilkes/#402" aria-description="Citation for case: Dinsman v. Wilkes">12 How. 390, 402</a></span> (1852); <em>Randall </em>v. <em>Henry, </em><span class="citation" data-id="6531883"><a href="/opinion/6654686/randall-v-henry/#378" aria-description="Citation for case: Randall v. Henry">5 Stew. <em>&amp; </em>P. 367, 378</a></span> (Ala. 1834); <em>Bell v. Keepers, </em><span class="citation" data-id="7886960"><a href="/opinion/7936501/bell-v-keepers/" aria-description="Citation for case: Bell v. Keepers">37 Kan. 64</a></span>, <span class="citation no-link">14 P. 542</span> (1887); <em>Finn </em>v. <em>Frink, </em><span class="citation" data-id="4935290"><a href="/opinion/5116603/finn-v-frink/" aria-description="Citation for case: Finn v. Frink">84 Me. 261</a></span>, <span class="citation" data-id="4935290"><a href="/opinion/5116603/finn-v-frink/" aria-description="Citation for case: Finn v. Frink">24 A. 851</a></span> (1892); 4 W. Wait, Actions and Defenses 352-356 (1878). The same rule applied in the case of search warrants. See, <em>e. g., Barker </em>v. <em>Stetson, </em><span class="citation" data-id="6411056"><a href="/opinion/6537336/barker-v-stetson/#54" aria-description="Citation for case: Barker v. Stetson">73 Mass. 53, 54</a></span> (1856); <em>Carey </em>v. <em>Sheets, </em><span class="citation" data-id="7043175"><a href="/opinion/7135561/carey-v-sheets/#378" aria-description="Citation for case: Carey v. Sheets">67 Ind. 375, 378-379</a></span> (1879).</p>
</footnote>
<footnote label="4">
<p id="b423-9"> See 4 Wait, <em>supra, </em>at 345 (‘Whether malice is proved or not is a question of fact for the jury”).</p>
</footnote>
<footnote label="5">
<p id="b425-6"> The organized bar’s development and enforcement of professional standards for prosecutors also lessen the danger that absolute immunity will become a shield for prosecutorial misconduct. As we observed in <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Imbler</a></span>, </em>“a prosecutor stands perhaps unique, among officials whose acts could deprive persons of constitutional rights, in his amenability to professional discipline by an association of his peers. ” <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#429" aria-description="Citation for case: Imbler v. Pachtman">424 U. S., at 429</a></span> (footnote omitted). The absence of a comparably well-developed and pervasive mechanism for controlling police misconduct weighs against allowing absolute immunity for the officer.</p>
</footnote>
<footnote label="6">
<p id="b426-7"> Although the case before us only concerns a damages action for an officer’s part in obtaining an allegedly unconstitutional arrest warrant, the distinction between a search warrant and an arrest warrant would not make a difference in the degree of immunity accorded the officer who applied for the warrant.</p>
</footnote>
<footnote label="7">
<p id="b426-8"> Petitioner has not pressed the argument that in a case like this the officer should not be liable because the judge’s decision to issue the warrant breaks the causal chain between the application for the warrant and the improvident arrest. It should be clear, however, that the District Court’s “no causation” rationale in this case is inconsistent with our interpretation of § 1983. As we stated in <em>Monroe </em>v. <em>Pape, </em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#187" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167, 187</a></span> (1961), <page-number citation-index="1" label="345">*345</page-number>§ 1983 “should be read against the background of tort liability that makes a man responsible for the natural consequences of his actions.” Since the common law recognized the causal link between the submission of a complaint and an ensuing arrest, we read § 1983 as recognizing the same causal link.</p>
</footnote>
<footnote label="8">
<p id="A5R"> The question is not presented to us, nor do we decide, whether petitioner’s conduct in this case was in fact objectively reasonable. That issue must be resolved on remand.</p>
</footnote>
<footnote label="9">
<p id="AHX"> Notwithstanding petitioner’s protestations, the rule we adopt in no way “requires the police officer to assume a role even more skilled . . . than the magistrate. ” Brief for Petitioners 33. It is a sound presumption that “the magistrate is more qualified than the police officer to make a probable cause determination,” <em>ibid., </em>and it goes without saying that where a magistrate acts mistakenly in issuing a warrant but -within the range of professional competence of a magistrate, the officer who requested the warrant cannot be held liable. But it is different if no officer of reasonable competence would have requested the warrant, <em>i. e., </em>his request is outside the range of the professional competence expected of an officer. If the magistrate issues the warrant in such a ease, his action is not just a reasonable mistake, but an unacceptable error indicating gross incompetence or neglect of duty. The officer then cannot excuse his own default by pointing to the greater incompetence of the magistrate.</p>
</footnote>
</opinion>
```

---
