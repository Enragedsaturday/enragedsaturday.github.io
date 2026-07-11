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

## GROUP: _overhaul2/lake/cases/Lo-Ji Sales, Inc. v. New York.json  (`lake-record`, 4 assertions)

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
{"assertion_id": "20ede11b27831daf", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Lo-Ji Sales, Inc. v. New York"}, "payload": {"all": [{"cite": "442 U.S. 319", "page": "319", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "442"}, {"cite": "99 S. Ct. 2319", "page": "2319", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "99"}, {"cite": "60 L. Ed. 2d 920", "page": "920", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "60"}, {"cite": "1979 U.S. LEXIS 107", "page": "107", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1979"}, {"cite": "5 Media L. Rep. (BNA) 1177", "page": "1177", "reporter": "Media L. Rep. (BNA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "5"}], "display": "442 U.S. 319", "official": {"cite": "442 U.S. 319", "page": "319", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "442"}, "official_selection_present": true, "record_id": "Lo-Ji Sales, Inc. v. New York"}}
{"assertion_id": "834d6d64d14a519c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-327", "record_id": "Lo-Ji Sales, Inc. v. New York"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-327", "pinpoint_status": "slip-only", "quote": "He allowed himself to become a member, if not the leader, of the search party which was essentially a police operation. . . . he was not acting as a judicial officer but as an adjunct law enforcement officer.", "quote_fidelity": "mismatch", "record_id": "Lo-Ji Sales, Inc. v. New York", "star_marker": null}}
{"assertion_id": "c271ee9d35980e76", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-326", "record_id": "Lo-Ji Sales, Inc. v. New York"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-326", "pinpoint_status": "slip-only", "quote": "items. ## Issue Whether a search conducted under an open-ended warrant is valid where the issuing magistrate abandons his neutral and detached role by joining and directing the search. ## Rule A warrant-issuing magistrate must remain neutral and detached and may not become part of the search.", "quote_fidelity": "mismatch", "record_id": "Lo-Ji Sales, Inc. v. New York", "star_marker": null}}
{"assertion_id": "e573f77b27b6d0c1", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Lo-Ji Sales, Inc. v. New York"}, "payload": {"as_of_content": "1979-06-11", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Lo-Ji Sales, Inc. v. New York", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/Lombardo v. City of St. Louis.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Lombardo v. City of St. Louis
type: case
citation: "594 U.S. 464 (2021)"
parallel_cite: "210 L. Ed. 2d 609; 141 S. Ct. 2239"
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2021
date_decided: ""
docket: 20-391
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
  opinion_url: "https://www.courtlistener.com/opinion/4895266/lombardo-v-st-louis/"
  cluster_id: 4895266
  opinion_id: null
  identity_checked: true
lake:
  record_id: Lombardo v. City of St. Louis
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Use of Force]]"
    role: Recent development
related:
  - "[[Graham v. Connor]]"
  - "[[Use of Force]]"
tags:
  - case
  - excessive-force
  - use-of-force
  - section-1983
  - fourteenth-amendment
holding: "A § 1983 excessive-force challenge to a fatal prone restraint of a handcuffed, leg-shackled detainee must be analyzed under the fact-specific Kingsley reasonableness factors — including the force's kind, intensity, and duration — rather than treated as per se constitutional whenever a detainee appears to resist; summary judgment for the officers was vacated and remanded."
---

# Lombardo v. City of St. Louis

*594 U.S. 464 (2021)* (No. 20-391) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4895266 → opinion 4699045 (per curiam); quote string-matched to the CL opinion text 2026-07-07 (CL carries the slip opinion, 594 U.S. ___; pin cited slip-style per S2 A3). S9 promotes. -->

## Background
Nicholas Gilbert was arrested on a minor charge and held in a St. Louis police station cell. After officers saw him acting as though he might harm himself, they entered to restrain him; a struggle ensued, and the officers handcuffed and leg-shackled Gilbert and then moved him to a prone (face-down) position on the floor. Three officers held his limbs while at least one pressed on his back and torso for roughly fifteen minutes; Gilbert said "It hurts. Stop," stopped moving, and died. His parents sued the officers under 42 U.S.C. § 1983 for excessive force. The District Court granted the officers summary judgment, and the Eighth Circuit affirmed, holding that the use of a prone restraint was not objectively unreasonable given Gilbert's resistance.

## Issue
Whether the Eighth Circuit properly analyzed the excessive-force claim under the fact-specific reasonableness factors of *[[Kingsley v. Hendrickson]]*, or instead applied a categorical rule treating prone restraint of a resisting detainee as constitutional regardless of the surrounding circumstances.

## Rule
Excessive-force reasonableness turns on a careful, case-specific balancing of the relevant *[[Kingsley v. Hendrickson|Kingsley]]* factors — including the relationship between the need for force and the amount used, the severity of the security problem, the threat reasonably perceived, and any effort to temper the force. A court may not short-circuit that inquiry with a categorical rule. As the Court put it: "Although the Eighth Circuit cited the Kingsley factors, it is unclear whether the court thought the use of a prone restraint — no matter the kind, intensity, duration, or surrounding circumstances — is per se constitutional so long as an individual appears to resist officers' efforts to subdue him." — 594 U.S. 464 (slip op., at 3). ^pin-3

## Application
Facts the Eighth Circuit had brushed aside as "insignificant" were potentially decisive under *[[Kingsley v. Hendrickson|Kingsley]]*: Gilbert was already handcuffed and leg-shackled when moved to the prone position, was held there for fifteen minutes, and was subjected to back pressure even though St. Louis trains its officers that pressing on a prone subject's back can cause suffocation — and that a prone subject's struggles may reflect oxygen deprivation rather than defiance. Because it was unclear whether the court below had weighed these facts or instead applied a [[Common Legal Terms#per-se|per se]] rule, the Court declined to resolve the excessive-force question itself and returned the case for a proper, fact-specific analysis.

## Conclusion
The judgment was **[[Reading and Citing Cases#vacated|vacated]]** and the case **[[Reading and Citing Cases#on-remand|remanded]]** for the lower courts to apply the *[[Kingsley v. Hendrickson|Kingsley]]* reasonableness inquiry to the specific facts. The opinion was **[[Common Legal Terms#per-curiam|per curiam]]**; Alito, J., joined by Thomas and Gorsuch, JJ., dissented, arguing the Court should have decided the question rather than remand.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Lombardo* is a pretrial-detainee (Fourteenth Amendment) excessive-force decision governed by *[[Kingsley v. Hendrickson|Kingsley]]*'s objective-reasonableness standard, the detention analog to *[[Graham v. Connor]]*; it reaffirms that prone-restraint reasonableness is fact-specific, not categorical.

## Appears on
- [[Use of Force]] — *Recent development*

## Sources
- [*Lombardo v. City of St. Louis*, 594 U.S. 464 (2021)](https://www.courtlistener.com/opinion/4895266/lombardo-v-st-louis/) — pinpoint: slip op., at 3 (per curiam); quote string-matched to the CL slip-opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c59c9ef0a930fedd", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Lombardo v. City of St. Louis"}, "payload": {"all": [{"cite": "594 U.S. 464", "page": "464", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "594"}, {"cite": "210 L. Ed. 2d 609", "page": "609", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "210"}, {"cite": "141 S. Ct. 2239", "page": "2239", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "141"}], "display": "594 U.S. 464", "official": {"cite": "594 U.S. 464", "page": "464", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "594"}, "official_selection_present": true, "record_id": "Lombardo v. City of St. Louis"}}
{"assertion_id": "acc09be79dcd6404", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Lombardo v. City of St. Louis"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Lombardo v. City of St. Louis", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Lombardo v. City of St. Louis

```json
{
  "schema_version": "s2.v1",
  "record_id": "Lombardo v. City of St. Louis",
  "status": "under_review",
  "identity": {
    "case_name": "Lombardo v. St. Louis",
    "case_name_short": "Lombardo",
    "case_name_full": "",
    "input_case_name": "Lombardo v. City of St. Louis",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2021,
    "docket": "20-391",
    "cluster_id": 4895266,
    "lead_opinion_id": 4699045,
    "sibling_ids": [],
    "absolute_url": "/opinion/4895266/lombardo-v-st-louis/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "594 U.S. 464",
      "volume": "594",
      "reporter": "U.S.",
      "page": "464",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "210 L. Ed. 2d 609",
        "volume": "210",
        "reporter": "L. Ed. 2d",
        "page": "609",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 2239",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "2239",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "594 U.S. 464",
        "volume": "594",
        "reporter": "U.S.",
        "page": "464",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "210 L. Ed. 2d 609",
        "volume": "210",
        "reporter": "L. Ed. 2d",
        "page": "609",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 2239",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "2239",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "594 U.S. 464",
    "official_selection": {
      "court_class": "scotus",
      "selected": "594 U.S. 464",
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
    "date_created": "2026-07-06T12:10:28Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:10:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:10:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:10:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:10:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "lombardo-v-city-of-st-louis--4895266",
      "to_record_id": "Lombardo v. City of St. Louis",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Lombardo v. City of St. Louis

```
                      Cite as: 594 U. S. ____ (2021)                     1

                                Per Curiam

SUPREME COURT OF THE UNITED STATES
    JODY LOMBARDO, ET AL. v. CITY OF ST. LOUIS,
               MISSOURI, ET AL.
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED
   STATES COURT OF APPEALS FOR THE EIGHTH CIRCUIT
                  No. 20–391.    Decided June 28, 2021

   PER CURIAM.
   On the afternoon of December 8, 2015, St. Louis police
officers arrested Nicholas Gilbert for trespassing in a con-
demned building and failing to appear in court for a traffic
ticket.1 Officers brought him to the St. Louis Metropolitan
Police Department’s central station and placed him in a
holding cell. At some point, an officer saw Gilbert tie a piece
of clothing around the bars of his cell and put it around his
neck, in an apparent attempt to hang himself. Three offic-
ers responded and entered Gilbert’s cell. One grabbed Gil-
bert’s wrist to handcuff him, but Gilbert evaded the officer
and began to struggle. The three officers brought Gilbert,
who was 5’3” and 160 pounds, down to a kneeling position
over a concrete bench in the cell and handcuffed his arms
behind his back. Gilbert reared back, kicking the officers
and hitting his head on the bench. After Gilbert kicked one
of the officers in the groin, they called for more help and leg
shackles. While Gilbert continued to struggle, two officers
shackled his legs together. Emergency medical services
personnel were phoned for assistance.
   Several more officers responded. They relieved two of the
original three officers, leaving six officers in the cell with


——————
  1 Because this case was decided by summary judgment, the evidence

here recounted is viewed “ ‘in the light most favorable’ ” to the nonmoving
party (here, Gilbert’s parents, the petitioners). Tolan v. Cotton, 572
U. S. 650, 655–656 (2014) (per curiam).
2                     LOMBARDO v. ST. LOUIS

                              Per Curiam

Gilbert, who was now handcuffed and in leg irons. The of-
ficers moved Gilbert to a prone position, face down on the
floor. Three officers held Gilbert’s limbs down at the shoul-
ders, biceps, and legs. At least one other placed pressure
on Gilbert’s back and torso. Gilbert tried to raise his chest,
saying, “ ‘It hurts. Stop.’ ” Lombardo v. Saint Louis City,
361 F. Supp. 3d 882, 898 (ED Mo. 2019).
   After 15 minutes of struggling in this position, Gilbert’s
breathing became abnormal and he stopped moving. The
officers rolled Gilbert onto his side and then his back to
check for a pulse. Finding none, they performed chest com-
pressions and rescue breathing. An ambulance eventually
transported Gilbert to the hospital, where he was pro-
nounced dead.
   Gilbert’s parents sued, alleging that the officers had used
excessive force against him. The District Court granted
summary judgment in favor of the officers, concluding that
they were entitled to qualified immunity because they did
not violate a constitutional right that was clearly estab-
lished at the time of the incident. Id., at 895. The U. S.
Court of Appeals for the Eighth Circuit affirmed on differ-
ent grounds, holding that the officers did not apply uncon-
stitutionally excessive force against Gilbert. 956 F. 3d
1009, 1014 (2020).
   In assessing a claim of excessive force, courts ask
“whether the officers’ actions are ‘objectively reasonable’ in
light of the facts and circumstances confronting them.”
Graham v. Connor, 490 U. S. 386, 397 (1989).2 “A court

——————
  2 Petitioners brought their excessive force claims under both the

Fourth and Fourteenth Amendments. See, e.g., First Amended Com-
plaint in No. 4:16–cv–01637, ECF Doc. 28 (ED Mo.), p. 46. We need not
address whether the Fourth or Fourteenth Amendment provides the
proper basis for a claim of excessive force against a pretrial detainee in
Gilbert’s position. Whatever the source of law, in analyzing an excessive
force claim, a court must determine whether the force was objectively
unreasonable in light of the “ ‘facts and circumstances of each particular
                     Cite as: 594 U. S. ____ (2021)                    3

                              Per Curiam

(judge or jury) cannot apply this standard mechanically.”
Kingsley v. Hendrickson, 576 U. S. 389, 397 (2015). Rather,
the inquiry “requires careful attention to the facts and cir-
cumstances of each particular case.” Graham, 490 U. S., at
396. Those circumstances include “the relationship be-
tween the need for the use of force and the amount of force
used; the extent of the plaintiff ’s injury; any effort made by
the officer to temper or to limit the amount of force; the se-
verity of the security problem at issue; the threat reasona-
bly perceived by the officer; and whether the plaintiff was
actively resisting.” Kingsley, 576 U. S., at 397.
   Although the Eighth Circuit cited the Kingsley factors, it
is unclear whether the court thought the use of a prone re-
straint—no matter the kind, intensity, duration, or sur-
rounding circumstances—is per se constitutional so long as
an individual appears to resist officers’ efforts to subdue
him. The court cited Circuit precedent for the proposition
that “the use of prone restraint is not objectively unreason-
able when a detainee actively resists officer directives and
efforts to subdue the detainee.” 956 F. 3d, at 1013. The
court went on to describe as “insignificant” facts that may
distinguish that precedent and appear potentially im-
portant under Kingsley, including that Gilbert was already
handcuffed and leg shackled when officers moved him to the
prone position and that officers kept him in that position for
15 minutes. See 956 F. 3d, at 1013–1015.
   Such details could matter when deciding whether to
grant summary judgment on an excessive force claim.
Here, for example, record evidence (viewed in the light most
favorable to Gilbert’s parents) shows that officers placed
pressure on Gilbert’s back even though St. Louis instructs
its officers that pressing down on the back of a prone subject
can cause suffocation. The evidentiary record also includes
——————
case.’ ” Kingsley v. Hendrickson, 576 U. S. 389, 397 (2015) (quoting Gra-
ham, 490 U. S., at 396).
4                      LOMBARDO v. ST. LOUIS

                               Per Curiam

well-known police guidance recommending that officers get
a subject off his stomach as soon as he is handcuffed be-
cause of that risk. The guidance further indicates that the
struggles of a prone suspect may be due to oxygen defi-
ciency, rather than a desire to disobey officers’ commands.
Such evidence, when considered alongside the duration of
the restraint and the fact that Gilbert was handcuffed and
leg shackled at the time, may be pertinent to the relation-
ship between the need for the use of force and the amount
of force used, the security problem at issue, and the
threat—to both Gilbert and others—reasonably perceived
by the officers. Having either failed to analyze such evi-
dence or characterized it as insignificant, the court’s opin-
ion could be read to treat Gilbert’s “ongoing resistance” as
controlling as a matter of law.3 Id., at 1014. Such a per se
rule would contravene the careful, context-specific analysis
required by this Court’s excessive force precedent.
   We express no view as to whether the officers used un-
constitutionally excessive force or, if they did, whether Gil-
bert’s right to be free of such force in these circumstances
was clearly established at the time of his death. We instead
grant the petition for certiorari, vacate the judgment of the
Eighth Circuit, and remand the case to give the court the
opportunity to employ an inquiry that clearly attends to the
facts and circumstances in answering those questions in the
first instance.
                                               It is so ordered.




——————
   3 While the dissent suggests we should give the Eighth Circuit the ben-

efit of the doubt, in assessing the appropriateness of review in this fact-
bound context, it is more prudent to afford the Eighth Circuit an oppor-
tunity to clarify its opinion rather than to speculate as to its basis.
                  Cite as: 594 U. S. ____ (2021)            1

                      ALITO, J., dissenting

SUPREME COURT OF THE UNITED STATES
   JODY LOMBARDO, ET AL. v. CITY OF ST. LOUIS,
              MISSOURI, ET AL.
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED
   STATES COURT OF APPEALS FOR THE EIGHTH CIRCUIT
               No. 20–391.   Decided June 28, 2021

   JUSTICE ALITO, with whom JUSTICE THOMAS and
JUSTICE GORSUCH join, dissenting.
   I cannot approve the Court’s summary disposition be-
cause it unfairly interprets the Court of Appeals’ decision
and evades the real issue that this case presents: whether
the record supports summary judgment in favor of the de-
fendant police officers and the city of St. Louis. The Court
of Appeals held that the defendants were entitled to sum-
mary judgment because a reasonable jury would neces-
sarily find that the police officers used reasonable force in
attempting to subdue petitioner Lombardo’s son, Nicholas
Gilbert, when he was attempting to hang himself in his cell.
In reaching this conclusion, the Court of Appeals applied
the correct legal standard and made a judgment call on a
sensitive question. This case, therefore, involves the appli-
cation of “a properly stated rule of law” to a particular fac-
tual record, and our rules say that we “rarely” review such
questions. See this Court’s Rule 10. But “rarely” does not
mean “never,” and if this Court is unwilling to allow the de-
cision below to stand, the proper course is to grant the peti-
tion, receive briefing and argument, and decide the real
question that this case presents.
   That is the course I would take. I do not think that this
Court is above occasionally digging into the type of fact-
bound questions that make up much of the work of the
lower courts, and a decision by this Court on the question
presented here could be instructive.
   The Court, unfortunately, is unwilling to face up to the
2                  LOMBARDO v. ST. LOUIS

                      ALITO, J., dissenting

choice between denying the petition (and bearing the criti-
cism that would inevitably elicit) and granting plenary re-
view (and doing the work that would entail). Instead, it
claims to be uncertain whether the Court of Appeals actu-
ally applied the correct legal standard, and for that reason
it vacates the judgment below and remands the case.
   This course of action may be convenient for this Court,
but it is unfair to the Court of Appeals. If we expect the
lower courts to respect our decisions, we should not twist
their opinions to make our job easier.
   When the Court of Appeals’ opinion is read in the way we
hope our opinions will be interpreted, it is clear that the
Court of Appeals understood and applied the correct stand-
ard for excessive-force claims. The per curiam acknowl-
edges that the Court of Appeals correctly cited the factors
that must be taken into account in determining whether the
officers’ actions were objectively reasonable. Ante, at 3; see
956 F. 3d 1009, 1013 (CA8 2020). But the per curiam finds
it “unclear whether the [Court of Appeals] thought the use
of a prone restraint—no matter the kind, intensity, dura-
tion, or surrounding circumstances—is per se constitutional
so long as an individual appears to resist officers’ efforts to
subdue him.” Ante, at 3.
   Can the Court seriously think that the Eighth Circuit
adopted such a strange and extreme position—that the use
of prone restraint on a resisting detainee is always reason-
able no matter how much force is used, no matter how long
that force is employed, no matter the physical condition of
the detainee, and no matter whether the detainee is obvi-
ously suffering serious or even life-threatening harm? Sup-
pose officers with a combined weight of 1,000 pounds knelt
on the back of a frail and infirm detainee, used all their
might to press his chest and face into a concrete floor for
over an hour, did not desist when the detainee cried, “You’re
killing me,” and ended up inflicting fatal injuries. Does the
Court really believe that the Court of Appeals might have
                 Cite as: 594 U. S. ____ (2021)            3

                     ALITO, J., dissenting

thought that this extreme use of force would be reasonable?
Is there any support for that interpretation in the Court of
Appeals’ opinion?
  The per curiam latches onto this sentence in the opinion
below: “This Court has previously held that the use of prone
restraint is not objectively unreasonable when a detainee
actively resists officer directives and efforts to subdue the
detainee.” 956 F. 3d, at 1013; see ante, at 3. Read in con-
text, its meaning is apparent.
  The sentence recounts and cites to what the Eighth Cir-
cuit had held in an earlier case, Ryan v. Armstrong, 850
F. 3d 419 (2017), in which a resisting detainee had been
held in a prone position for a period of time. In order to
understand the sentence in the opinion below, it is neces-
sary to look at that prior decision. And when the language
in the decision below is read in that way, what it obviously
means is that the use of prone restraint is not objectively
unreasonable per se when a detainee is actively resisting.
That is exactly what the appellees, citing Ryan, had argued:
“No court has held that placing a resisting prisoner in a
prone position while restrained is per se unreasonable.”
Brief for Appellees in No. 19–1469 (CA8), p. 24. That is a
correct reading of Ryan, and that is how the opinion below
interpreted it.
  Ryan held only that the use of force in that case was rea-
sonable based on “the totality of th[e] circumstances,” in-
cluding the detainee’s resistance. 850 F. 3d, at 428. The
Ryan court explained:
    “Several factors support the foregoing conclusion.
    Among the most important is the observation that [the
    detainee] was actively resisting the extraction proce-
    dure by ignoring directives to lie down on his bunk and
    resisting the defendants’ efforts to subdue him once
    they entered his cell.” Ibid. (emphasis added).
  Thus, Ryan clearly did not adopt any sort of blanket rule,
4                      LOMBARDO v. ST. LOUIS

                          ALITO, J., dissenting

and the sentence in this case that the per curiam seizes
upon did not purport to go beyond Ryan.
  This Court’s per curiam refers to one other statement in
the opinion below. The per curiam states:
     “The [Eighth Circuit] went on to describe as ‘insignifi-
     cant’ facts that may distinguish [Ryan] and appear po-
     tentially important under Kingsley, including that Gil-
     bert was already handcuffed and leg shackled when
     officers moved him to the prone position and that offic-
     ers kept him in that position for 15 minutes.” Ante, at
     3 (quoting 956 F. 3d, at 1014).
  Here, again, the per curiam strains to give the Eighth
Circuit’s opinion a possible interpretation that can justify a
remand. But when this sentence is read in context, what it
plainly means is not that the duration of the officers’ use of
force or the fact that Gilbert had been handcuffed and
shackled were irrelevant but that certain factual differ-
ences between this case and Ryan were not significant in
the sense that they did not call for a different result.
  The court used the term “insignificant” in responding to
Lombardo’s efforts to distinguish Ryan. Lombardo argued
that this case is different because Gilbert was restrained for
a longer period and, unlike the detainee in Ryan, had al-
ready been handcuffed and shackled. See 956 F. 3d, at
1014; Brief for Plaintiffs-Appellants in No. 19–1469 (CA8),
pp. 14–15. What the Eighth Circuit characterized as “in-
significant” were these factual differences between the two
cases.*

——————
  *The Eighth Circuit wrote:
  “Lombardo argues that Ryan is not on point. Specifically, Lombardo
argues that, unlike Ryan, in which the detainee was held in prone re-
straint for approximately three minutes until he was handcuffed, . . . Gil-
bert was held in prone restraint for fifteen minutes and was placed in
this position only after he had been handcuffed and leg-shackled. Lom-
bardo also argues that she presented expert testimony that Gilbert’s
                      Cite as: 594 U. S. ____ (2021)                      5

                           ALITO, J., dissenting

  Without carefully studying the record, I cannot be certain
whether I would have agreed with the Eighth Circuit panel
that summary judgment for the defendants was correct.
The officers plainly had a reasonable basis for using some
degree of force to restrain Gilbert so that he would not harm
himself, and it appears that Gilbert, despite his slight stat-
ure, put up a fierce and prolonged resistance. See 956 F. 3d,
at 1011–1014. On the other hand, the officers’ use of force
inflicted serious injuries, and the medical evidence on the
cause of death was conflicting. See id., at 1012.
  We have two respectable options: deny review of the fact-
bound question that the case presents or grant the petition,
have the case briefed and argued, roll up our sleeves, and
decide the real issue. I favor the latter course, but what we
should not do is take the easy out that the Court has chosen.




——————
cause of death was forcible restraint inducing asphyxia whereas the un-
disputed cause of death in Ryan was sudden unexpected death during
restraint. . . . We find these differences to be insignificant. This Court
has previously noted that ‘[h]andcuffs limit but do not eliminate a per-
son’s ability to perform harmful acts.’ United States v. Pope, 910 F. 3d
413, 417 (8th Cir. 2018), cert. denied, [589 U. S. ___ (2019)]. As discussed
above, the undisputed facts show that Gilbert continued to violently
struggle even after being handcuffed and leg-shackled. Specifically, after
being handcuffed, he thrashed his head on the concrete bench, causing
him to suffer a gash on his forehead, and he continued to violently thrash
and kick after being leg-shackled. Because of this ongoing resistance,
the Officers moved Gilbert to the prone position so as to minimize the
harm he could inflict on himself and others.” 956 F. 3d, at 1014.

```

---

## GROUP: _overhaul2/lake/cases/Los Angeles County v. Rettele.json  (`lake-record`, 6 assertions)

### content_page

```
---
title: "Los Angeles County v. Rettele"
type: case
citation: ""
parallel_cite: "550 U.S. 609; 127 S. Ct. 1989; 167 L. Ed. 2d 974; 75 U.S.L.W. 3619; 20 Fla. L. Weekly Fed. S 281"
neutral_cite: 2007 U.S. LEXIS 5900
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2007
date_decided: 2007-05-21
docket: 06-605
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2007-05-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Los Angeles County v. Rettele
  varies_by_point: false
  scope_note: "Controlling: officers executing a valid warrant may briefly detain occupants and exercise unquestioned command — including ordering them, unclothed, out of bed for a few minutes — to secure the scene without violating the Fourth Amendment, so long as the detention is not prolonged."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145728/los-angeles-county-california-v-rettele/"
  cluster_id: 145728
  opinion_id: 145728
  identity_checked: true
homes:
  - page: "[[Detention and Search of Persons at the Scene]]"
    role: "Key — Progeny"
  - page: "[[Securing the Scene]]"
    role: "Related (scene-securing overlap)"
  - page: "[[Qualified Immunity]]"
    role: "Related (cross-doctrine)"
related: ["[[Michigan v. Summers]]", "[[Muehler v. Mena]]", "[[Bailey v. United States]]"]
aliases: ["Los Angeles County, California v. Rettele"]
tags: ["case", "fourth-amendment", "securing-the-scene", "warrant-execution", "detention", "qualified-immunity"]
holding: "Officers executing a valid search warrant may briefly detain the occupants and exercise unquestioned command of the situation to protect themselves — including ordering unclothed occupants out of bed for a few minutes while securing the room — without violating the Fourth Amendment, provided the detention is not prolonged."
lake:
  record_id: Los Angeles County v. Rettele
  status: verified
  projected_at: 2026-07-06
---

# Los Angeles County v. Rettele

*550 U.S. 609 (2007)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Sheriff's deputies obtained a valid warrant to search a house in a fraud/identity-theft investigation; the suspects were African-American and one was believed to own a handgun. Unknown to the deputies, the house had recently been sold to Rettele and Sadler, who were white. Executing the warrant in the early morning, deputies entered the bedroom and ordered Rettele and Sadler — naked in bed — to get up and stand, holding them at gunpoint for a couple of minutes while securing the room before letting them dress. Realizing the suspects were not there, the deputies left within 15 minutes. The Retteles sued under § 1983.

## Issue
Do deputies executing a valid search warrant violate the Fourth Amendment by briefly detaining the home's occupants at gunpoint — including ordering them, unclothed, out of bed — while securing the residence?

## Rule
No. "The deputies needed a moment to secure the room and ensure that other persons were not close by or did not present a danger," and "[d]eputies were not required to turn their backs to allow Rettele and Sadler to retrieve clothing or to cover themselves with the sheets[;] [r]ather, '[t]he risk of harm to both the police and the occupants is minimized if the officers routinely exercise unquestioned command of the situation.'" — 127 S. Ct. at 1993 (quoting *Michigan v. Summers*). ^pin-1993

The detention may not be prolonged beyond necessity, but here there was "no accusation that the detention . . . was prolonged[;] [t]he deputies left the home less than 15 minutes after arriving." — *Id.* ^pin-1993b

The governing principle: "When officers execute a valid warrant and act in a reasonable manner to protect themselves from harm . . . , the Fourth Amendment is not violated." — *Id.* at 1993–94. ^pin-1994

And because "respondents' constitutional rights were not violated, 'there is no necessity for further inquiries concerning qualified immunity.'" — *Id.* at 1994. ^pin-1994b

## Application
The deputies reasonably believed armed suspects might be inside, so ordering the occupants out of bed and briefly holding them while securing the room was a reasonable safety measure. That the occupants turned out to be innocent, of a different race than the suspects, and unclothed did not make the brief detention unreasonable: valid warrants issue on probable cause, not certainty, and innocent residents sometimes bear the cost. The occupants were unclothed for only about two minutes and the whole episode lasted under 15 minutes — far shorter and less restrictive than the two-to-three-hour handcuff detention upheld in *[[Muehler v. Mena]]*. No constitutional violation occurred.

## Conclusion
The deputies' conduct in executing the valid warrant did not violate the Fourth Amendment; the judgment of the Ninth Circuit was reversed and the case [[Reading and Citing Cases#on-remand|remanded]]. (Justice Stevens, joined by Justice Ginsburg, would have reversed solely on qualified-immunity grounds.)

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Rettele* remains controlling on the authority to detain occupants and secure the scene while executing a warrant, applying [[Michigan v. Summers]] and situating the intrusion below the detention upheld in [[Muehler v. Mena]]. The scope of *[[Michigan v. Summers|Summers]]* detention authority was later cabined geographically in [[Bailey v. United States]]. No negative treatment.

## Appears on
- [[Securing the Scene]] — *Progeny*
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *Los Angeles County v. Rettele*, 550 U.S. 609 (2007) (per curiam) — https://www.courtlistener.com/opinion/145728/los-angeles-county-california-v-rettele/ — pinpoints (S. Ct. reporter, per CL copy): 1993, 1994.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6265762ea702064f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Los Angeles County v. Rettele"}, "payload": {"all": [{"cite": "550 U.S. 609", "page": "609", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "550"}, {"cite": "127 S. Ct. 1989", "page": "1989", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "127"}, {"cite": "167 L. Ed. 2d 974", "page": "974", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "167"}, {"cite": "2007 U.S. LEXIS 5900", "page": "5900", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2007"}, {"cite": "75 U.S.L.W. 3619", "page": "3619", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "75"}, {"cite": "20 Fla. L. Weekly Fed. S 281", "page": "281", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "20"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Los Angeles County v. Rettele"}}
{"assertion_id": "5a93193f9093648c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1993", "record_id": "Los Angeles County v. Rettele"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1993", "pinpoint_status": "slip-only", "quote": "--- # Los Angeles County v. Rettele *550 U.S. 609 (2007)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Sheriff's deputies obtained a valid warrant to search a house in a fraud/identity-theft investigation; the suspects were African-American and one was believed to own a handgun. Unknown to the deputies, the house had recently been sold to Rettele and Sadler, who were white. Executing the warrant in the early morning, deputies entered the bedroom and ordered Rettele and Sadler — naked in bed — to get up and stand, holding them at gunpoint for a couple of minutes while securing the room before letting them dress. Realizing the suspects were not there, the deputies left within 15 minutes. The Retteles sued under § 1983. ## Issue Do deputies executing a valid search warrant violate the Fourth Amendment by briefly detaining the home's occupants at gunpoint — including ordering them, unclothed, out of bed — while securing the residence? ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Los Angeles County v. Rettele", "star_marker": null}}
{"assertion_id": "92bcf225da79b543", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1993b", "record_id": "Los Angeles County v. Rettele"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1993b", "pinpoint_status": "slip-only", "quote": "no accusation that the detention . . . was prolonged[;] [t]he deputies left the home less than 15 minutes after arriving.", "quote_fidelity": "mismatch", "record_id": "Los Angeles County v. Rettele", "star_marker": null}}
{"assertion_id": "96da889f210676d6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1994b", "record_id": "Los Angeles County v. Rettele"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1994b", "pinpoint_status": "slip-only", "quote": "respondents' constitutional rights were not violated, 'there is no necessity for further inquiries concerning qualified immunity.'", "quote_fidelity": "mismatch", "record_id": "Los Angeles County v. Rettele", "star_marker": null}}
{"assertion_id": "ab2d1f7202e9be14", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1994", "record_id": "Los Angeles County v. Rettele"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1994", "pinpoint_status": "slip-only", "quote": "When officers execute a valid warrant and act in a reasonable manner to protect themselves from harm . . . , the Fourth Amendment is not violated.", "quote_fidelity": "mismatch", "record_id": "Los Angeles County v. Rettele", "star_marker": null}}
{"assertion_id": "1bd1b2db01bae463", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Los Angeles County v. Rettele"}, "payload": {"as_of_content": "2007-05-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Los Angeles County v. Rettele", "scope_note": "Controlling: officers executing a valid warrant may briefly detain occupants and exercise unquestioned command — including ordering them, unclothed, out of bed for a few minutes — to secure the scene without violating the Fourth Amendment, so long as the detention is not prolonged.", "varies_by_point": false}}
```

### lake record — Los Angeles County v. Rettele

```json
{
  "schema_version": "s2.v1",
  "record_id": "Los Angeles County v. Rettele",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Los Angeles County, California v. Rettele",
    "case_name_short": "Rettele",
    "case_name_full": "LOS ANGELES COUNTY, CALIFORNIA, Et Al. v. RETTELE Et Al.",
    "input_case_name": "Los Angeles County v. Rettele",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2007-05-21",
    "year": 2007,
    "docket": "06-605",
    "cluster_id": 145728,
    "lead_opinion_id": 145728,
    "sibling_ids": [
      145728,
      9435063,
      9435064
    ],
    "absolute_url": "/opinion/145728/los-angeles-county-california-v-rettele/",
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
        "cite": "550 U.S. 609",
        "volume": "550",
        "reporter": "U.S.",
        "page": "609",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "127 S. Ct. 1989",
        "volume": "127",
        "reporter": "S. Ct.",
        "page": "1989",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "167 L. Ed. 2d 974",
        "volume": "167",
        "reporter": "L. Ed. 2d",
        "page": "974",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 U.S.L.W. 3619",
        "volume": "75",
        "reporter": "U.S.L.W.",
        "page": "3619",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 Fla. L. Weekly Fed. S 281",
        "volume": "20",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "281",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2007 U.S. LEXIS 5900",
        "volume": "2007",
        "reporter": "U.S. LEXIS",
        "page": "5900",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "550 U.S. 609",
        "volume": "550",
        "reporter": "U.S.",
        "page": "609",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "127 S. Ct. 1989",
        "volume": "127",
        "reporter": "S. Ct.",
        "page": "1989",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "167 L. Ed. 2d 974",
        "volume": "167",
        "reporter": "L. Ed. 2d",
        "page": "974",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2007 U.S. LEXIS 5900",
        "volume": "2007",
        "reporter": "U.S. LEXIS",
        "page": "5900",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 U.S.L.W. 3619",
        "volume": "75",
        "reporter": "U.S.L.W.",
        "page": "3619",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 Fla. L. Weekly Fed. S 281",
        "volume": "20",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "281",
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
      "id": "pin-1993",
      "page": null,
      "quote": "--- # Los Angeles County v. Rettele *550 U.S. 609 (2007)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Sheriff's deputies obtained a valid warrant to search a house in a fraud/identity-theft investigation; the suspects were African-American and one was believed to own a handgun. Unknown to the deputies, the house had recently been sold to Rettele and Sadler, who were white. Executing the warrant in the early morning, deputies entered the bedroom and ordered Rettele and Sadler \u2014 naked in bed \u2014 to get up and stand, holding them at gunpoint for a couple of minutes while securing the room before letting them dress. Realizing the suspects were not there, the deputies left within 15 minutes. The Retteles sued under \u00a7 1983. ## Issue Do deputies executing a valid search warrant violate the Fourth Amendment by briefly detaining the home's occupants at gunpoint \u2014 including ordering them, unclothed, out of bed \u2014 while securing the residence? ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1993b",
      "page": null,
      "quote": "no accusation that the detention . . . was prolonged[;] [t]he deputies left the home less than 15 minutes after arriving.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1994",
      "page": null,
      "quote": "When officers execute a valid warrant and act in a reasonable manner to protect themselves from harm . . . , the Fourth Amendment is not violated.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1994b",
      "page": null,
      "quote": "respondents' constitutional rights were not violated, 'there is no necessity for further inquiries concerning qualified immunity.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2007-05-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Los Angeles County v. Rettele",
    "varies_by_point": false,
    "scope_note": "Controlling: officers executing a valid warrant may briefly detain occupants and exercise unquestioned command \u2014 including ordering them, unclothed, out of bed for a few minutes \u2014 to secure the scene without violating the Fourth Amendment, so long as the detention is not prolonged.",
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
        "journal_ref": "Los Angeles County v. Rettele:lane1_negative"
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
        "journal_ref": "Los Angeles County v. Rettele:lane1_negative"
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
        "journal_ref": "Los Angeles County v. Rettele:lane1_negative"
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
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Curley v. Klem",
          "cluster_id": 1362944,
          "cite": [
            "499 F.3d 199",
            "2007 U.S. App. LEXIS 20213",
            "2007 WL 2404803"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
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
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
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
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
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
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Weigel v. Broad",
          "cluster_id": 171335,
          "cite": [
            "544 F.3d 1143",
            "2008 U.S. App. LEXIS 21877",
            "2008 WL 4631920"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baird v. Renbarger",
          "cluster_id": 1188789,
          "cite": [
            "576 F.3d 340",
            "2009 U.S. App. LEXIS 17215",
            "2009 WL 2357882"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colbruno v. Kessler",
          "cluster_id": 4636000,
          "cite": [
            "928 F.3d 1155"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mlodzinski Ex Rel. J.M. v. Lewis",
          "cluster_id": 2451581,
          "cite": [
            "648 F.3d 24",
            "2011 U.S. App. LEXIS 11117",
            "2011 WL 2150741"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
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
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jennings",
          "cluster_id": 1313899,
          "cite": [
            "544 F.3d 815",
            "2008 U.S. App. LEXIS 19560",
            "2008 WL 4192887"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jennifer Cox v. Evansville Police Department and The City of Evansville Babi Beyer v. The City of Fort Wayne",
          "cluster_id": 4534961,
          "cite": [
            "107 N.E.3d 453"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kamel Chaney-Snell v. Andrew Young",
          "cluster_id": 9493618,
          "cite": [
            "98 F.4th 699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Norris",
          "cluster_id": 216168,
          "cite": [
            "640 F.3d 295",
            "2011 U.S. App. LEXIS 9222",
            "2011 WL 1675801"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Z. J. v. Kansas City Brd of Police Comm",
          "cluster_id": 4642838,
          "cite": [
            "931 F.3d 672"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brian Lawrence",
          "cluster_id": 2805131,
          "cite": [
            "788 F.3d 234",
            "2015 U.S. App. LEXIS 9160",
            "2015 WL 3463089"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Erin Osmon v. United States",
          "cluster_id": 9392722,
          "cite": [
            "66 F.4th 144"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maria Yanez-Marquez v. Loretta Lynch",
          "cluster_id": 2808824,
          "cite": [
            "789 F.3d 434",
            "2015 U.S. App. LEXIS 10107",
            "2015 WL 3719105"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kennedy v. State",
          "cluster_id": 2546934,
          "cite": [
            "338 S.W.3d 84",
            "2011 Tex. App. LEXIS 1755",
            "2011 WL 832122"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Siciliano",
          "cluster_id": 203974,
          "cite": [
            "578 F.3d 61",
            "2009 U.S. App. LEXIS 19121",
            "2009 WL 2605704"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bancroft v. City of Mount Vernon",
          "cluster_id": 2308267,
          "cite": [
            "672 F. Supp. 2d 391",
            "2009 U.S. Dist. LEXIS 112652",
            "2009 WL 4277268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sanchez v. Canales",
          "cluster_id": 1359367,
          "cite": [
            "574 F.3d 1169",
            "2009 D.A.R. 11",
            "2009 U.S. App. LEXIS 16897"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jennen",
          "cluster_id": 1303041,
          "cite": [
            "596 F.3d 594",
            "2010 U.S. App. LEXIS 3784",
            "2010 WL 625041"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rush v. City of Mansfield",
          "cluster_id": 2474513,
          "cite": [
            "771 F. Supp. 2d 827",
            "2011 U.S. Dist. LEXIS 13689",
            "2011 WL 609802"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martinez-Cortes",
          "cluster_id": 1470540,
          "cite": [
            "566 F.3d 767",
            "2009 U.S. App. LEXIS 11656",
            "2009 WL 1424106"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145728 OR 9435063 OR 9435064) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 59,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 59,
        "triage_read": 3,
        "triage_snippet_classified": 56
      },
      "lane2_top_cited": {
        "query": "cites:(145728 OR 9435063 OR 9435064)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01JnM9MTczNDc3JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28145728+OR+9435063+OR+9435064%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145728 OR 9435063 OR 9435064)",
        "reviewed": 4,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 4,
        "triage_read": 0,
        "triage_snippet_classified": 4
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145728 OR 9435063 OR 9435064)",
    "indexed_citing_opinions": 91,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145728,
        "count": 69,
        "count_source": "search"
      },
      {
        "opinion_id": 9435063,
        "count": 22,
        "count_source": "search"
      },
      {
        "opinion_id": 9435064,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 229,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/los-angeles-county-v-rettele.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjYyNTk3NDUmcz00NjA5ODM5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28145728+OR+9435063+OR+9435064%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145728,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145728,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145728,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145728,
        "cited_id": 142878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145728,
        "cited_id": 675827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145728,
        "cited_id": 726621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145728,
        "cited_id": 781793,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145728,
        "cited_id": 782720,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145728,
        "cited_id": 1654997,
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
    "date_created": "2026-07-05T11:01:38Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:01:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:01:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:05:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:01:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Los Angeles County v. Rettele

```
                 Cite as: 550 U. S. ____ (2007)          1

                            Per Curiam

SUPREME COURT OF THE UNITED STATES
   LOS ANGELES COUNTY, CALIFORNIA, ET AL. v. 

             MAX RETTELE ET AL. 

   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE NINTH CIRCUIT

              No. 06–605.    Decided May 21, 2007 


  PER CURIAM.
  Deputies of the Los Angeles County Sheriff’s Depart
ment obtained a valid warrant to search a house, but they
were unaware that the suspects being sought had moved
out three months earlier. When the deputies searched the
house, they found in a bedroom two residents who were of
a different race than the suspects. The deputies ordered
these innocent residents, who had been sleeping un
clothed, out of bed. The deputies required them to stand
for a few minutes before allowing them to dress.
  The residents brought suit under Rev. Stat. §1979, 42
U. S. C. §1983, naming the deputies and other parties and
accusing them of violating the Fourth Amendment right to
be free from unreasonable searches and seizures. The
District Court granted summary judgment to all named
defendants. The Court of Appeals for the Ninth Circuit
reversed, concluding both that the deputies violated the
Fourth Amendment and that they were not entitled to
qualified immunity because a reasonable deputy would
have stopped the search upon discovering that respon
dents were of a different race than the suspects and be
cause a reasonable deputy would not have ordered respon
dents from their bed. We grant the petition for certiorari
and reverse the judgment of the Court of Appeals by this
summary disposition.
                         I
  From September to December 2001, Los Angeles County
2            LOS ANGELES COUNTY v. RETTELE

                        Per Curiam

Sheriff’s Department Deputy Dennis Watters investigated
a fraud and identity-theft crime ring. There were four
suspects of the investigation. One had registered a 9
millimeter Glock handgun. The four suspects were known
to be African-Americans.
   On December 11, Watters obtained a search warrant for
two houses in Lancaster, California, where he believed he
could find the suspects. The warrant authorized him to
search the homes and three of the suspects for documents
and computer files. In support of the search warrant an
affidavit cited various sources showing the suspects re
sided at respondents’ home. The sources included De
partment of Motor Vehicles reports, mailing address list
ings, an outstanding warrant, and an Internet telephone
directory. In this Court respondents do not dispute the
validity of the warrant or the means by which it was
obtained.
   What Watters did not know was that one of the houses
(the first to be searched) had been sold in September to a
Max Rettele. He had purchased the home and moved into
it three months earlier with his girlfriend Judy Sadler and
Sadler’s 17-year-old son Chase Hall. All three, respon
dents here, are Caucasians.
   On the morning of December 19, Watters briefed six
other deputies in preparation for the search of the houses.
Watters informed them they would be searching for three
African-American suspects, one of whom owned a regis
tered handgun. The possibility a suspect would be armed
caused the deputies concern for their own safety. Watters
had not obtained special permission for a night search, so
he could not execute the warrant until 7 a.m. See Cal.
Penal Code Ann. §1533 (West 2000). Around 7:15 Watters
and six other deputies knocked on the door and announced
their presence. Chase Hall answered. The deputies en
tered the house after ordering Hall to lie face down on the
ground.
                 Cite as: 550 U. S. ____ (2007)           3

                          Per Curiam

   The deputies’ announcement awoke Rettele and Sadler.
The deputies entered their bedroom with guns drawn and
ordered them to get out of their bed and to show their
hands. They protested that they were not wearing clothes.
Rettele stood up and attempted to put on a pair of sweat
pants, but deputies told him not to move. Sadler also
stood up and attempted, without success, to cover herself
with a sheet. Rettele and Sadler were held at gunpoint for
one to two minutes before Rettele was allowed to retrieve
a robe for Sadler. He was then permitted to dress. Rettele
and Sadler left the bedroom within three to four minutes
to sit on the couch in the living room.
   By that time the deputies realized they had made a
mistake. They apologized to Rettele and Sadler, thanked
them for not becoming upset, and left within five minutes.
They proceeded to the other house the warrant authorized
them to search, where they found three suspects. Those
suspects were arrested and convicted.
   Rettele and Sadler, individually and as guardians ad
litem for Hall, filed this §1983 suit against Los Angeles
County, the Los Angeles County Sheriff’s Department,
Deputy Watters, and other members of the sheriff’s de
partment. Respondents alleged petitioners violated their
Fourth Amendment rights by obtaining a warrant in
reckless fashion and conducting an unreasonable search
and detention. The District Court held that the warrant
was obtained by proper procedures and the search was
reasonable. It concluded in the alternative that any
Fourth Amendment rights the deputies violated were not
clearly established and that, as a result, the deputies were
entitled to qualified immunity.
   On appeal respondents did not challenge the validity of
the warrant; they did argue that the deputies had con
ducted the search in an unreasonable manner. A divided
panel of the Court of Appeals for the Ninth Circuit re
versed in an unpublished opinion. 186 Fed. Appx. 765
4           LOS ANGELES COUNTY v. RETTELE

                        Per Curiam

(2006). The majority held that
    “because (1) no African-Americans lived in [respon
    dents’] home; (2) [respondents], a Caucasian couple,
    purchased the residence several months before the
    search and the deputies did not conduct an ownership
    inquiry; (3) the African-American suspects were not
    accused of a crime that required an emergency search;
    and (4) [respondents] were ordered out of bed naked
    and held at gunpoint while the deputies searched
    their bedroom for the suspects and a gun, we find that
    a reasonable jury could conclude that the search and
    detention were ‘unnecessarily painful, degrading, or
    prolonged,’ and involved ‘an undue invasion of pri
    vacy,’ Franklin v. Foxworth, 31 F. 3d 873, 876 (9th
    Cir. 1994).” Id., at 766.
Turning to whether respondents’ Fourth Amendment
rights were clearly established, the majority held that a
reasonable deputy should have known the search and
detention were unlawful.
  Judge Cowen dissented. In his view the deputies had
authority to detain respondents for the duration of the
search and were justified in ordering respondents from
their bed because weapons could have been concealed
under the bedcovers. He also concluded that, assuming
a constitutional violation, the law was not clearly
established.
  The Court of Appeals denied rehearing and rehearing en
banc.
                             II
  Because respondents were of a different race than the
suspects the deputies were seeking, the Court of Appeals
held that “[a]fter taking one look at [respondents], the
deputies should have realized that [respondents] were not
the subjects of the search warrant and did not pose a
threat to the deputies’ safety.” Ibid. We need not pause
                 Cite as: 550 U. S. ____ (2007)            5

                          Per Curiam

long in rejecting this unsound proposition. When the
deputies ordered respondents from their bed, they had no
way of knowing whether the African-American suspects
were elsewhere in the house. The presence of some Cau
casians in the residence did not eliminate the possibility
that the suspects lived there as well. As the deputies
stated in their affidavits, it is not uncommon in our society
for people of different races to live together. Just as peo
ple of different races live and work together, so too might
they engage in joint criminal activity. The deputies, who
were searching a house where they believed a suspect
might be armed, possessed authority to secure the prem
ises before deciding whether to continue with the search.
  In Michigan v. Summers, 452 U. S. 692 (1981), this
Court held that officers executing a search warrant for
contraband may “detain the occupants of the premises
while a proper search is conducted.” Id., at 705. In weigh
ing whether the search in Summers was reasonable the
Court first found that “detention represents only an in
cremental intrusion on personal liberty when the search of
a home has been authorized by a valid warrant.” Id., at
703. Against that interest, it balanced “preventing flight
in the event that incriminating evidence is found”; “mini
mizing the risk of harm to the officers”; and facilitating
“the orderly completion of the search.” Id., at 702–703; see
Muehler v. Mena, 544 U. S. 93 (2005).
  In executing a search warrant officers may take reason
able action to secure the premises and to ensure their own
safety and the efficacy of the search. Id., at 98–100; see
also id., at 103 (KENNEDY, J., concurring); Summers,
supra, at 704–705. The test of reasonableness under the
Fourth Amendment is an objective one. Graham v. Con
nor, 490 U. S. 386, 397 (1989) (addressing the reasonable
ness of a seizure of the person). Unreasonable actions
include the use of excessive force or restraints that cause
unnecessary pain or are imposed for a prolonged and
6            LOS ANGELES COUNTY v. RETTELE

                         Per Curiam

unnecessary period of time. Mena, supra, at 100; Graham,
supra, at 396–399.
   The orders by the police to the occupants, in the context
of this lawful search, were permissible, and perhaps nec
essary, to protect the safety of the deputies. Blankets and
bedding can conceal a weapon, and one of the suspects was
known to own a firearm, factors which underscore this
point. The Constitution does not require an officer to
ignore the possibility that an armed suspect may sleep
with a weapon within reach. The reports are replete with
accounts of suspects sleeping close to weapons. See
United States v. Enslin, 327 F. 3d 788, 791 (CA9 2003)
(“When [the suspect] put his hands in the air and began to
sit up, his movement shifted the covers and the marshals
could see a gun in the bed next to him”); see also United
States v. Jones, 336 F. 3d 245, 248 (CA3 2003) (suspect
kept a 9-millimeter Luger under his pillow while he slept);
United States v. Hightower, 96 F. 3d 211 (CA7 1996) (sus
pect kept a loaded five-shot handgun under his pillow);
State v. Willis, 36,759–KA, p. 3 (La. App. 4/9/03), 843
So. 2d 592, 595 (officers “pulled back the bed covers and
found a .38 caliber Model 10 Smith and Wesson revolver
located near where defendant’s left hand had been”); State
v. Kypreos, 115 Wash. App. 207, 61 P. 3d 352 (2002) (sus
pect kept a handgun in the bed).
   The deputies needed a moment to secure the room and
ensure that other persons were not close by or did not
present a danger. Deputies were not required to turn
their backs to allow Rettele and Sadler to retrieve clothing
or to cover themselves with the sheets. Rather, “[t]he risk
of harm to both the police and the occupants is minimized
if the officers routinely exercise unquestioned command of
the situation.” Summers, 452 U. S., at 702–703.
   This is not to say, of course, that the deputies were free
to force Rettele and Sadler to remain motionless and
standing for any longer than necessary. We have recog
                 Cite as: 550 U. S. ____ (2007)            7

                          Per Curiam

nized that “special circumstances, or possibly a prolonged
detention” might render a search unreasonable. See id.,
at 705, n. 21. There is no accusation that the detention
here was prolonged. The deputies left the home less than
15 minutes after arriving. The detention was shorter and
less restrictive than the 2- to 3-hour handcuff detention
upheld in Mena. See 544 U. S., at 100. And there is no
allegation that the deputies prevented Sadler and Rettele
from dressing longer than necessary to protect their
safety. Sadler was unclothed for no more than two min
utes, and Rettele for only slightly more time than that.
Sadler testified that once the police were satisfied that no
immediate threat was presented, “they wanted us to get
dressed and they were pressing us really fast to hurry up
and get some clothes on.” Deposition of Judy Lorraine
Sadler in No. CV–0206262–RSWL (RNBX) (CD Cal., June
10, 2003), Doc. 26, Exh. 4, p. 55.
  The Fourth Amendment allows warrants to issue on
probable cause, a standard well short of absolute cer
tainty. Valid warrants will issue to search the innocent,
and people like Rettele and Sadler unfortunately bear the
cost. Officers executing search warrants on occasion enter
a house when residents are engaged in private activity;
and the resulting frustration, embarrassment, and hu
miliation may be real, as was true here. When officers
execute a valid warrant and act in a reasonable manner to
protect themselves from harm, however, the Fourth
Amendment is not violated.
  As respondents’ constitutional rights were not violated,
“there is no necessity for further inquiries concerning
qualified immunity.” Saucier v. Katz, 533 U. S. 194, 201
(2001). The judgment of the Court of Appeals is reversed,
and the case is remanded for further proceedings consis
tent with this opinion.
                                            It is so ordered.
  JUSTICE SOUTER would deny the petition for a writ of
certiorari.
                      Cite as: 550 U. S. ____ (2007)                     1

                  STEVENS, J., concurring in judgment

SUPREME COURT OF THE UNITED STATES
    LOS ANGELES COUNTY, CALIFORNIA, ET AL. v. 

              MAX RETTELE ET AL. 

   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE NINTH CIRCUIT

                  No. 06–605.    Decided May 21, 2007 


   JUSTICE STEVENS, with whom JUSTICE GINSBURG joins,
concurring in the judgment.
   This case presents two separate questions: (1) whether
the four circumstances identified in the Court of Appeals’
unpublished opinion established a genuine issue of mate
rial fact as to whether the seizure violated respondents’
Fourth Amendment rights, see ante, at 4; (2) whether the
officers were nevertheless entitled to qualified immunity
because the right was not clearly established. The fact
that the judges on the Court of Appeals disagreed on both
questions convinces me that they should not have an
nounced their decision in an unpublished opinion.
   In answering the first question, the Ninth Circuit major
ity relied primarily on Franklin v. Foxworth, 31 F. 3d 873
(CA9 1994). As Judge Cowen’s discussion of Franklin
demonstrates, that case surely does not clearly establish
the unconstitutionality of the officers’ conduct.* Conse
——————
   * See 186 Fed. Appx. 765, 767 (2006) (dissenting opinion) (“In Frank
lin v. Foxworth, 31 F.3d 873 (9th Cir. 1994), we found unconstitutional
the officers’ failure to provide clothing to a gravely ill man before
exposing his genitals to twenty-three strangers for over two hours,
under circumstances where there was no reason why the man was not
given clothing. Id. at 876–78. We concluded that the detention was
conducted in ‘a manner that wantonly and callously subjected an
obviously ill and incapacitated person to entirely unnecessary and
unjustifiable degradation and suffering.’ Id. at 878. Here, in contrast,
Plaintiffs were not gravely ill, and their brief exposure, which lasted, at
most, three or four minutes, was outweighed by the safety risks associ
ated with allowing two occupants to remain in bed under covers during
2               LOS ANGELES COUNTY v. RETTELE

                  STEVENS, J., concurring in judgment

quently, regardless of the proper answer to the constitu
tional question, the defendants were entitled to qualified
immunity. I would reverse on that ground and disavow
the unwise practice of deciding constitutional questions in
advance of the necessity for doing so. See County of Sac
ramento v. Lewis, 523 U. S. 833, 859 (1998) (STEVENS, J.,
concurring in judgment). Accordingly, I concur in the
Court’s judgment.




—————— 

execution of a search warrant”). 


```

---

## GROUP: _overhaul2/lake/cases/Lozman v. City of Riviera Beach.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Lozman v. City of Riviera Beach
type: case
citation: "585 U.S. 87 (2018)"
parallel_cite: "138 S. Ct. 1945; 201 L. Ed. 2d 342"
neutral_cite: 2018 U.S. LEXIS 3691
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2018
date_decided: 2018-06-18
docket: No. 17-21
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
  opinion_url: "https://www.courtlistener.com/opinion/4508137/lozman-v-riviera-beach/"
  cluster_id: 4508137
  opinion_id: null
  identity_checked: true
lake:
  record_id: Lozman v. City of Riviera Beach
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Retaliatory Arrest]]"
    role: Anchor
related:
  - "[[Retaliatory Arrest]]"
  - "[[Nieves v. Bartlett]]"
tags:
  - case
  - first-amendment
  - retaliatory-arrest
  - probable-cause
  - section-1983
  - municipal-policy
holding: "Where a plaintiff alleges that a municipality arrested him pursuant to an official policy of retaliation, formed well before the arrest, in response to speech high in the hierarchy of First Amendment values, the existence of probable cause for the arrest does not bar his First Amendment retaliatory-arrest claim; the Court did not decide the elements of retaliatory-arrest claims in other contexts."
aliases:
  - Lozman v. City of Riviera Beach
  - "Lozman v. City of Riviera Beach (2018)"
  - Lozman v. Riviera Beach
---

# Lozman v. City of Riviera Beach

*585 U.S. 87 (2018)* (No. 17-21) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4508137 → lead opinion 4285390 (Kennedy, J.; 585 U.S. 87, decided June 18, 2018). Rule quote string-matched to the CL opinion text 2026-07-07; the CL text is the slip opinion (585 U.S. ___), so the pin is slip-style per S2 A3 — slip op. at 12 (the holding falls on slip page 12, before the "13" page header). S9 promotes. -->

## Background
Fane Lozman was an outspoken critic of the Riviera Beach, Florida city government: he had sued the City over open-meetings violations and repeatedly criticized officials in public. During the public-comment period of a City Council meeting, he refused to stop speaking and was arrested. Lozman alleged that, months earlier in a closed-door session, the City had formed an official policy to intimidate him in retaliation for his protected speech, and that his arrest carried out that policy. He conceded there was probable cause to arrest him. The Eleventh Circuit held that the existence of probable cause defeated his First Amendment retaliatory-arrest claim as a matter of law.

## Issue
Whether probable cause for an arrest bars a First Amendment retaliatory-arrest claim where the plaintiff alleges the arrest was made pursuant to an official municipal policy of retaliation.

## Rule
Deciding the case on a deliberately narrow ground, the Court held: "For these reasons, Lozman need not prove the absence of probable cause to maintain a claim of retaliatory arrest against the City." — slip op. at 12. ^pin-op12

## Application
The Court stressed how unusual Lozman's claim was: he alleged an *official municipal policy* of intimidation, premeditated and formed well before the arrest, directed at speech high in the hierarchy of First Amendment values (his petitioning and criticism of government), and supported by objective evidence able to survive summary judgment. In that limited class of cases the causation concerns that ordinarily attend retaliatory-arrest claims are diminished, and *Mt. Healthy* supplies the governing standard — so the mere existence of probable cause does not automatically defeat the claim. The Court expressly declined to define the elements of retaliatory-arrest claims in the more typical case of an on-the-spot arrest by an individual officer.

## Conclusion
The judgment was **[[Reading and Citing Cases#vacated|vacated]]** and the case [[Reading and Citing Cases#on-remand|remanded]]. Kennedy, J., delivered the opinion of the Court; Thomas, J., dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Lozman* is narrow and fact-bound; it left the general probable-cause question open. The Court answered that broader question the next Term in *[[Nieves v. Bartlett]]* (2019): probable cause generally defeats a retaliatory-arrest claim, subject to a narrow exception where police typically exercise discretion not to arrest for the conduct at issue. Teach *Lozman* as the official-municipal-policy sliver and *[[Nieves v. Bartlett|Nieves]]* as the general rule.

## Appears on
- [[Retaliatory Arrest]] — *Anchor*

## Sources
- [*Lozman v. City of Riviera Beach*, 585 U.S. 87 (2018)](https://www.courtlistener.com/opinion/4508137/lozman-v-riviera-beach/) — pinpoint: slip op. at 12 (Kennedy, J., for the Court; the CL opinion text is the slip opinion, 585 U.S. ___, with the holding on slip page 12 — the U.S. Reports pagination is not present in the CL text, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7f69d00c9bf1ecf3", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Lozman v. City of Riviera Beach"}, "payload": {"all": [{"cite": "585 U.S. 87", "page": "87", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "585"}, {"cite": "138 S. Ct. 1945", "page": "1945", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "138"}, {"cite": "201 L. Ed. 2d 342", "page": "342", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "201"}, {"cite": "2018 U.S. LEXIS 3691", "page": "3691", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2018"}], "display": "585 U.S. 87", "official": {"cite": "585 U.S. 87", "page": "87", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "585"}, "official_selection_present": true, "record_id": "Lozman v. City of Riviera Beach"}}
{"assertion_id": "424d9b3dc8fe9d09", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Lozman v. City of Riviera Beach"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Lozman v. City of Riviera Beach", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Lozman v. City of Riviera Beach

```json
{
  "schema_version": "s2.v1",
  "record_id": "Lozman v. City of Riviera Beach",
  "status": "under_review",
  "identity": {
    "case_name": "Lozman v. Riviera Beach",
    "case_name_short": "Lozman",
    "case_name_full": "",
    "input_case_name": "Lozman v. City of Riviera Beach",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2018-06-18",
    "year": 2018,
    "docket": "No. 17-21",
    "cluster_id": 4508137,
    "lead_opinion_id": 4285390,
    "sibling_ids": [],
    "absolute_url": "/opinion/4508137/lozman-v-riviera-beach/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "585 U.S. 87",
      "volume": "585",
      "reporter": "U.S.",
      "page": "87",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "138 S. Ct. 1945",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "1945",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "201 L. Ed. 2d 342",
        "volume": "201",
        "reporter": "L. Ed. 2d",
        "page": "342",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2018 U.S. LEXIS 3691",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "3691",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "585 U.S. 87",
        "volume": "585",
        "reporter": "U.S.",
        "page": "87",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "138 S. Ct. 1945",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "1945",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "201 L. Ed. 2d 342",
        "volume": "201",
        "reporter": "L. Ed. 2d",
        "page": "342",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2018 U.S. LEXIS 3691",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "3691",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "585 U.S. 87",
    "official_selection": {
      "court_class": "scotus",
      "selected": "585 U.S. 87",
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
    "date_created": "2026-07-06T13:17:07Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:17:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:17:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:17:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:17:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "lozman-v-city-of-riviera-beach--4508137",
      "to_record_id": "Lozman v. City of Riviera Beach",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Lozman v. City of Riviera Beach

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

     LOZMAN v. CITY OF RIVIERA BEACH, FLORIDA

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                THE ELEVENTH CIRCUIT

     No. 17–21. Argued February 27, 2018—Decided June 18, 2018
After petitioner Lozman towed his floating home into a slip in a marina
  owned by the city of Riviera Beach, he became an outspoken critic of
  the City’s plan to use its eminent domain power to seize waterfront
  homes for private development and often made critical comments
  about officials during the public-comment period of city council meet-
  ings. He also filed a lawsuit alleging that the City Council’s approval
  of an agreement with developers violated Florida’s open-meetings
  laws. In June 2006 the Council held a closed-door session, in part to
  discuss Lozman’s lawsuit. He alleges that the meeting’s transcript
  shows that councilmembers devised an official plan to intimidate
  him, and that many of his subsequent disputes with city officials and
  employees were part of the City’s retaliation plan. Five months after
  the closed-door meeting, the Council held a public meeting. During
  the public-comment session, Lozman began to speak about the ar-
  rests of officials from other jurisdictions. When he refused a coun-
  cilmember’s request to stop making his remarks, the councilmember
  told the police officer in attendance to “carry him out.” The officer
  handcuffed Lozman and ushered him out of the meeting. The City
  contends that he was arrested for violating the City Council’s rules of
  procedure by discussing issues unrelated to the City and then refus-
  ing to leave the podium. Lozman claims that his arrest was to retali-
  ate for his lawsuit and his prior public criticisms of city officials. The
  State’s attorney determined that there was probable cause for his ar-
  rest, but decided to dismiss the charges.
     Lozman then filed suit under 42 U. S. C. §1983, alleging a number
  of incidents that, under his theory, showed the City’s purpose was to
  harass him, including by initiating an admiralty lawsuit against his
  floating home, see Lozman v. Riviera Beach, 568 U. S. 115. The jury
2                   LOZMAN v. RIVIERA BEACH

                                Syllabus

 returned a verdict for the City on all of the claims. The District
 Court instructed the jury that, for Lozman to prevail on his claim of a
 retaliatory arrest at the city council meeting, he had to prove that the
 arresting officer was motivated by impermissible animus against
 Lozman’s protected speech and that the officer lacked probable cause
 to make the arrest. The Eleventh Circuit affirmed, concluding that
 any error the District Court made when it instructed the jury to con-
 sider the officer’s retaliatory animus was harmless because the jury
 necessarily determined that the arrest was supported by probable
 cause when it found for the City on Lozman’s other claims. The ex-
 istence of probable cause, the court ruled, defeated a First Amend-
 ment claim for retaliatory arrest.
Held: The existence of probable cause does not bar Lozman’s First
 Amendment retaliation claim under the circumstances of this case.
 Pp. 5–13.
    (a) The issue here is narrow. Lozman concedes that there was
 probable cause for his arrest. Nonetheless, he claims, the arrest vio-
 lated the First Amendment because it was ordered in retaliation for
 his earlier, protected speech: his open-meetings lawsuit and his prior
 public criticisms of city officials. Pp. 5–6.
    (b) In a §1983 case, a city or other local governmental entity cannot
 be subject to liability unless the harm was caused in the implementa-
 tion of “official municipal policy.” Monell v. New York City Dept. of
 Social Servs., 436 U. S. 658, 691. The Court assumes that Lozman’s
 arrest was taken pursuant to an official city policy.
    Two major precedents bear on the issue whether the conceded ex-
 istence of probable cause for the arrest bars recovery regardless of
 any intent or purpose to retaliate for past speech. Lozman argues
 that the controlling rule is found in Mt. Healthy City Bd. of Ed. v.
 Doyle, 429 U. S. 274, a civil case in which a city board of education
 decided not to rehire an untenured teacher after a series of incidents,
 including a telephone call to a local radio station. The phone call was
 protected speech, but, the Court held, there was no liability unless
 the alleged constitutional violation was a but-for cause of the em-
 ployment termination. Id., at 285287. The City counters that the
 applicable precedent is Hartman v. Moore, 547 U. S. 250, where the
 Court held that a plaintiff alleging a retaliatory prosecution must
 show the absence of probable cause for the underlying criminal
 charge, id., at 265266. If there was probable cause, the case ends.
 If the plaintiff proves the absence of probable cause, then the Mt.
 Healthy test governs. Pp. 6–10.
    (c) Whether Hartman or Mt. Healthy governs here is a determina-
 tion that must await a different case. For Lozman’s claim is far
 afield from the typical retaliatory arrest claim, and the difficulties
                     Cite as: 585 U. S. ____ (2018)                      3

                                Syllabus

  that might arise if Mt. Healthy is applied to the mine run of arrests
  made by police officers are not present here. Lozman alleges that the
  City itself retaliated against him pursuant to an “official municipal
  policy” of intimidation. Monell, supra, at 691. The fact that he must
  prove the existence and enforcement of an official policy motivated by
  retaliation separates his claim from the typical retaliatory arrest
  claim. An official retaliatory policy can be long term and pervasive,
  unlike an ad hoc, on-the-spot decision by an individual officer. And it
  can be difficult to dislodge. A citizen can seek to have an individual
  officer disciplined or removed from service, but there may be little
  practical recourse when the government itself orchestrates the retali-
  ation. Lozman’s allegations, if proved, also alleviate the problems
  that the City says will result from applying Mt. Healthy in retaliatory
  arrest cases, for it is unlikely that the connection between the alleged
  animus and injury in a case like this will be “weakened . . . by [an of-
  ficial’s] legitimate consideration of speech,” Reichle v. Howards, 566
  U. S. 658, 668, and there is little risk of a flood of retaliatory arrest
  suits against high-level policymakers. Because Lozman alleges that
  the City deprived him of the right to petition, “ ‘one of the most pre-
  cious of the liberties safeguarded by the Bill of Rights,’ ” BE&K Con-
  str. Co. v. NLRB, 536 U. S. 516, 524, his speech is high in the hierar-
  chy of First Amendment values. On these facts, Mt. Healthy provides
  the correct standard for assessing a retaliatory arrest claim. On re-
  mand, the Eleventh Circuit may consider any arguments in support
  of the District Court’s judgment that have been preserved by the
  City, including whether a reasonable juror could find that the City
  formed a retaliatory policy to intimidate Lozman during its closed-
  door session, whether a reasonable juror could find that the arrest
  constituted an official act by the City, and whether, under Mt.
  Healthy, the City has proved that it would have arrested Lozman re-
  gardless of any retaliatory animus. Pp. 10–13.
681 Fed. Appx. 746, vacated and remanded.

  KENNEDY, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and GINSBURG, BREYER, ALITO, SOTOMAYOR, KAGAN, and GORSUCH,
JJ., joined. THOMAS, J., filed a dissenting opinion.
                       Cite as: 585 U. S. ____ (2018)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash-
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                   No. 17–21
                                  _________________


  FANE LOZMAN, PETITIONER v. CITY OF RIVIERA 

              BEACH, FLORIDA

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

          APPEALS FOR THE ELEVENTH CIRCUIT

                                [June 18, 2018] 


   JUSTICE KENNEDY delivered the opinion of the Court.
   This case requires the Court to address the intersection
of principles that define when arrests are lawful and
principles that prohibit the government from retaliating
against a person for having exercised the right to free
speech. An arrest deprives a person of essential liberties,
but if there is probable cause to believe the person has
committed a criminal offense there is often no recourse for
the deprivation. See, e.g., Devenpeck v. Alford, 543 U. S.
146, 153 (2004). At the same time, the First Amendment
prohibits government officials from retaliating against
individuals for engaging in protected speech. Crawford-El
v. Britton, 523 U. S. 574, 592 (1998).
   The petitioner in this case alleges that high-level city
policymakers adopted a plan to retaliate against him for
protected speech and then ordered his arrest when he
attempted to make remarks during the public-comment
portion of a city council meeting. The petitioner now
concedes there was probable cause for the arrest. The
question is whether the presence of probable cause
bars petitioner’s retaliatory arrest claim under these
2                LOZMAN v. RIVIERA BEACH

                     Opinion of the Court

circumstances.
                                I
   The city of Riviera Beach is on the Atlantic coast of
Florida, about 75 miles north of Miami. The petitioner
here is Fane Lozman. In 2006 Lozman towed his floating
home into a slip in the City-owned marina, where he
became a resident. Thus began his contentious relation-
ship with the City’s elected officials.
   Soon after his arrival Lozman became an outspoken
critic of the City’s plan to use its eminent domain power to
seize homes along the waterfront for private development.
Lozman often spoke during the public-comment period at
city council meetings and criticized councilmembers, the
mayor, and other public employees. He also filed a lawsuit
alleging that the Council’s approval of an agreement with
developers violated Florida’s open-meetings laws.
   In June 2006 the Council held a closed-door session, in
part to discuss the open-meetings lawsuit that Lozman
recently had filed. According to the transcript of the
meeting, Councilmember Elizabeth Wade suggested that
the City use its resources to “intimidate” Lozman and
others who had filed lawsuits against the City. App. 176.
Later in the meeting a different councilmember asked
whether there was “a consensus of what Ms. Wade is
saying,” and others responded in the affirmative. Id., at
181182. Lozman alleges that these remarks formed an
official plan to intimidate him. The City, on the other
hand, maintains that the only consensus reached during
the meeting was to invest the money and resources neces-
sary to prevail in the litigation against it.
   In all events, Lozman became embroiled in a number of
disputes with city officials and employees over the ensuing
years, many of which Lozman says were part of the City’s
plan of retaliation. The dispute that led to this litigation
took place in 2006. In November of that year, five months
                 Cite as: 585 U. S. ____ (2018)           3

                     Opinion of the Court

after the closed-door meeting where the “intimidate” com-
ment was made, the City Council held a public meeting.
The agenda included a public-comment session in which
citizens could address the Council for a few minutes. As
he had done on earlier occasions and would do more than
200 times over the coming years, see Tr. in No. 9:08–cv–
80134 (SD Fla.), Doc. 785, p. 61, Lozman stepped up to the
podium to give remarks. He began to discuss the recent
arrest of a former county official. Councilmember Wade
interrupted Lozman, directing him to stop making those
remarks. Lozman continued speaking, this time about the
arrest of a former official from the city of West Palm
Beach. Wade then called for the assistance of the police
officer in attendance. The officer approached Lozman and
asked him to leave the podium. Lozman refused. So
Wade told the officer to “carry him out.” The officer hand-
cuffed Lozman and ushered him out of the meeting. The
incident was recorded on video. See Record, Def. Exh. 505,
Doc. 687, available at https://www.supremecourt.gov/media/
video/mp4files/Lozman_v_RivieraBeach.mp4. According to
the City, Lozman was arrested because he violated the
City Council’s rules of procedure by discussing issues
unrelated to the City and then refused to leave the po-
dium. According to Lozman, the arrest was to retaliate for
his open-meetings lawsuit against the City and his prior
public criticisms of city officials.
   Under arrest, Lozman was escorted to police headquar-
ters. He was charged with disorderly conduct and resist-
ing arrest without violence and then released. Later, the
State’s attorney determined there was probable cause to
arrest Lozman for those offenses but decided to dismiss
the charges.
   Lozman filed this lawsuit under Rev. Stat. §1979, 42
U. S. C. §1983. The complaint described a number of
alleged incidents that, under Lozman’s theory, showed the
City’s purpose to harass him in different ways. These
4                LOZMAN v. RIVIERA BEACH

                     Opinion of the Court

ranged from a city employee telling Lozman that his dog
needed a muzzle to the City’s initiation of an admiralty
lawsuit against Lozman’s floating home—the latter result-
ing in an earlier decision by this Court. See Lozman v.
Riviera Beach, 568 U. S. 115 (2013). The evidence and
arguments presented by both parties with respect to all
the matters alleged in Lozman’s suit consumed 19 days of
trial before a jury. The jury returned a verdict for the City
on all of the claims.
   Before this Court, Lozman seeks a reversal only as to
the City’s alleged retaliatory arrest at the November 2006
city council meeting. The District Court instructed the
jury that, for Lozman to prevail on this claim, he had to
prove that the arresting officer was himself motivated by
impermissible animus against Lozman’s protected speech
and that the officer lacked probable cause to make the
arrest. The District Court determined that the evidence
was insufficient as a matter of law to support probable
cause for the offenses charged at the time of the arrest
(disorderly conduct and resisting arrest without violence).
But the District Court concluded that there may have
been probable cause to arrest Lozman for violating a
Florida statute that prohibits interruptions or disturb-
ances in schools, churches, or other public assemblies.
Fla. Stat. §871.01 (2017). (The City had brought this
statute to the District Court’s attention during the course
of the litigation.) The District Court allowed the jury to
decide whether there was probable cause to arrest for the
public-disturbance offense.
   Judgment having been entered for the City after the
jury’s verdict, Lozman appealed. The Court of Appeals for
the Eleventh Circuit affirmed. 681 Fed. Appx. 746 (2017).
As relevant here, the Court of Appeals assumed that the
District Court erred when it instructed the jury that the
officer, rather than the City, must have harbored the
retaliatory animus. But the Court of Appeals held that
                 Cite as: 585 U. S. ____ (2018)           5

                     Opinion of the Court

any error was harmless because the jury necessarily de-
termined that the arrest was supported by probable cause
when it found for the City on some of Lozman’s other
claims—specifically, his claims that the arrest violated the
Fourth Amendment and state law. Id., at 751752. And,
under precedents which the Court of Appeals deemed
controlling, the existence of probable cause defeated a
First Amendment claim for retaliatory arrest. See id., at
752 (citing Dahl v. Holley, 312 F. 3d 1228, 1236 (CA11
2002)).
  This Court granted certiorari, 583 U. S. ___ (2017), on
the issue whether the existence of probable cause defeats a
First Amendment claim for retaliatory arrest under §1983.
The Court considered this issue once before, see Reichle v.
Howards, 566 U. S. 658, 663 (2012), but resolved the case
on different grounds.
                              II
   The issue before the Court is a narrow one. In this
Court Lozman does not challenge the constitutionality of
Florida’s statute criminalizing disturbances at public
assemblies. He does not argue that the statute is overly
broad, e.g., Terminiello v. Chicago, 337 U. S. 1 (1949);
Watchtower Bible & Tract Soc. of N. Y., Inc. v. Village of
Stratton, 536 U. S. 150 (2002); or that it impermissibly
targets speech based on its content or viewpoint, e.g.,
Texas v. Johnson, 491 U. S. 397 (1989); Cohen v. Califor-
nia, 403 U. S. 15 (1971); or that it was enforced in a way
that curtailed Lozman’s right to peaceful assembly, e.g.,
Brown v. Louisiana, 383 U. S. 131 (1966). Lozman, fur-
thermore, does not challenge the validity of the City Coun-
cil’s asserted limitations on the subjects speakers may
discuss during the public-comment portion of city council
meetings (although he continues to dispute whether those
limitations in fact existed).
   Instead Lozman challenges only the lawfulness of his
6                LOZMAN v. RIVIERA BEACH

                      Opinion of the Court

arrest, and even that challenge is a limited one. There is
no contention that the City ordered Lozman’s arrest to
discriminate against him based on protected classifica-
tions, or that the City denied Lozman his equal protection
rights by placing him in a “class of one.” See Village of
Willowbrook v. Olech, 528 U. S. 562 (2000) (per curiam).
Lozman, moreover, now concedes that there was probable
cause for the arrest. Although Lozman does not indicate
what facts he believes support this concession, it appears
that the existence of probable cause must be based on the
assumption that Lozman failed to depart the podium after
receiving a lawful order to leave.
   Lozman’s claim is that, notwithstanding the presence of
probable cause, his arrest at the city council meeting
violated the First Amendment because the arrest was
ordered in retaliation for his earlier, protected speech: his
open-meetings lawsuit and his prior public criticisms of
city officials. The question this Court is asked to consider
is whether the existence of probable cause bars that First
Amendment retaliation claim.
                              III
   It is well established that in a §1983 case a city or other
local governmental entity cannot be subject to liability at
all unless the harm was caused in the implementation of
“official municipal policy.” Monell v. New York City Dept.
of Social Servs., 436 U. S. 658, 691 (1978); see Los Angeles
County v. Humphries, 562 U. S. 29, 36 (2010). Lozman’s
§1983 damages claim is against only the City itself, based
on the acts of its officers and employees—here, the mem-
bers of the City Council. Lozman says that the City,
through its city councilmembers, formed an official policy
to retaliate against him and ordered his arrest. The Court
assumes in the discussion to follow that the arrest was
taken pursuant to an official city policy, but whether there
was such a policy and what its content may have been are
                  Cite as: 585 U. S. ____ (2018)             7

                      Opinion of the Court

issues not decided here.
  This brings the discussion to the issue the parties deem
central to the case: whether the conceded existence of
probable cause for the arrest bars recovery regardless of
any intent or purpose to retaliate for past speech. Two
major precedents could bear on this point, and the parties
disagree on which should be applicable here. The first is
this Court’s decision in Mt. Healthy City Bd. of Ed. v.
Doyle, 429 U. S. 274 (1977). See also Board of Comm’rs,
Wabaunsee Cty. v. Umbehr, 518 U. S. 668 (1996). Lozman
urges that the rule of Mt. Healthy should control and that
under it he is entitled to recover. The second is this
Court’s decision in Hartman v. Moore, 547 U. S. 250
(2006), which the City cites for the proposition that once
there is probable cause there can be no further claim that
the arrest was retaliation for protected speech.
  Mt. Healthy arose in a civil, not criminal, context. A city
board of education decided not to rehire an untenured
school teacher after a series of incidents indicating unpro-
fessional demeanor. 429 U. S., at 281283. One of the
incidents was a telephone call the teacher made to a local
radio station to report on a new school policy. Id., at 282.
Because the board of education did not suggest that the
teacher violated any established policy in making the call,
this Court accepted a finding by the District Court that
the call was protected speech. Id., at 284. The Court went
on to hold, however, that since the other incidents, stand-
ing alone, would have justified the dismissal, relief could
not be granted if the board could show that the discharge
would have been ordered even without reference to the
protected speech. Id., at 285287. In terms of precepts in
the law of torts, the Court held that even if retaliation
might have been a substantial motive for the board’s
action, still there was no liability unless the alleged consti-
tutional violation was a but-for cause of the employment
termination. Ibid.; see also Umbehr, supra, at 675.
8                LOZMAN v. RIVIERA BEACH

                      Opinion of the Court

   The City resists the applicability of the Mt. Healthy test
as the sole determinant here. It contends that, where
there was probable cause for the arrest, the applicable
precedent is Hartman—a case that was in the criminal
sphere and that turned on the existence of probable cause.
   The background in Hartman was that a company and its
chief executive, William Moore, had engaged in an exten-
sive lobbying and governmental relations campaign oppos-
ing a particular postal service policy. 547 U. S., at
252253. Moore and the company were later prosecuted
for violating federal statutes in the course of that lobbying.
Id., at 253254. After being acquitted, Moore filed suit
against five postal inspectors, alleging that they had
violated his First Amendment rights when they instigated
his prosecution in retaliation for his criticisms of the
Postal Service. Id., at 254. This Court held that a plain-
tiff alleging a retaliatory prosecution must show the ab-
sence of probable cause for the underlying criminal
charge. Id., at 265266. If there was probable cause, the
case ends. If the plaintiff proves the absence of probable
cause, then the Mt. Healthy test governs: The plaintiff
must show that the retaliation was a substantial or moti-
vating factor behind the prosecution, and, if that showing
is made, the defendant can prevail only by showing that
the prosecution would have been initiated without respect
to retaliation. See 547 U. S., at 265–266.
   The Court in Hartman deemed it necessary to inquire as
to the existence of probable cause because proving the link
between the defendant’s retaliatory animus and the plain-
tiff ’s injury in retaliatory prosecution cases “is usually
more complex than it is in other retaliation cases.” Id., at
261. An action for retaliatory prosecution “will not be
brought against the prosecutor, who is absolutely immune
from liability for the decision to prosecute.” Id., at
261262. Instead, the plaintiff must sue some other gov-
ernment official and prove that the official “induced the
                  Cite as: 585 U. S. ____ (2018)            9

                      Opinion of the Court

prosecutor to bring charges that would not have been
initiated without his urging.” Id., at 262. Noting that
inquiries with respect to probable cause are commonplace
in criminal cases, the Court determined that requiring
plaintiffs in retaliatory prosecution cases to prove the lack
of probable cause would help “bridge the gap between the
nonprosecuting government agent’s motive and the prose-
cutor’s action.” Id., at 263.
   The City’s argument here is that, just as probable cause
is a bar in retaliatory prosecution cases, so too should it be
a bar in this case, involving a retaliatory arrest. There is
undoubted force in the City’s position. Reichle, 566 U. S.,
at 667–668. There are on average about 29,000 arrests
per day in this country. Dept. of Justice–FBI, Uniform
Crime Report, Crime in the United States, 2016 (Fall
2017). In deciding whether to arrest, police officers often
make split-second judgments. The content of the suspect’s
speech might be a consideration in circumstances where
the officer must decide whether the suspect is ready to
cooperate, or, on the other hand, whether he may present
a continuing threat to interests that the law must protect.
See, e.g., District of Columbia v. Wesby, 583 U. S. ___, ___
(2018) (slip op., at 10) (“suspect’s untruthful and evasive
answers to police questioning could support probable
cause” (internal quotation marks omitted)).
   For these reasons retaliatory arrest claims, much like
retaliatory prosecution claims, can “present a tenuous
causal connection between the defendant’s alleged animus
and the plaintiff ’s injury.” Reichle, 566 U. S., at 668.
That means it can be difficult to discern whether an arrest
was caused by the officer’s legitimate or illegitimate con-
sideration of speech. Ibid. And the complexity of proving
(or disproving) causation in these cases creates a risk that
the courts will be flooded with dubious retaliatory arrest
suits. See Brief for District of Columbia et al. as Amici
Curiae 511.
10               LOZMAN v. RIVIERA BEACH

                     Opinion of the Court

   At the same time, there are substantial arguments that
Hartman’s framework is inapt in retaliatory arrest cases,
and that Mt. Healthy should apply without a threshold
inquiry into probable cause. For one thing, the causation
problem in retaliatory arrest cases is not the same as the
problem identified in Hartman. Hartman relied in part on
the fact that, in retaliatory prosecution cases, the causal
connection between the defendant’s animus and the prose-
cutor’s decision to prosecute is weakened by the “presump-
tion of regularity accorded to prosecutorial decisionmak-
ing.” 547 U. S., at 263. That presumption does not apply
in this context. See Reichle, supra, at 669. In addition,
there is a risk that some police officers may exploit the
arrest power as a means of suppressing speech. See Brief
for Institute for Free Speech as Amicus Curiae.
                             IV
   The parties’ arguments raise difficult questions about
the scope of First Amendment protections when speech is
made in connection with, or contemporaneously to, crimi-
nal activity. But whether in a retaliatory arrest case the
Hartman approach should apply, thus barring a suit
where probable cause exists, or, on the other hand, the
inquiry should be governed only by Mt. Healthy is a de-
termination that must await a different case. For Loz-
man’s claim is far afield from the typical retaliatory arrest
claim, and the difficulties that might arise if Mt. Healthy
is applied to the mine run of arrests made by police offi-
cers are not present here.
   Here Lozman does not sue the officer who made the
arrest. Indeed, Lozman likely could not have maintained
a retaliation claim against the arresting officer in these
circumstances, because the officer appears to have acted in
good faith, and there is no showing that the officer had
any knowledge of Lozman’s prior speech or any motive to
arrest him for his earlier expressive activities.
                   Cite as: 585 U. S. ____ (2018)             11

                       Opinion of the Court

   Instead Lozman alleges more governmental action than
simply an arrest. His claim is that the City itself retali-
ated against him pursuant to an “official municipal policy” of
intimidation. Monell, 436 U. S., at 691. In particular, he
alleges that the City, through its legislators, formed a
premeditated plan to intimidate him in retaliation for his
criticisms of city officials and his open-meetings lawsuit.
And he asserts that the City itself, through the same high
officers, executed that plan by ordering his arrest at the
November 2006 city council meeting.
   The fact that Lozman must prove the existence and
enforcement of an official policy motivated by retaliation
separates Lozman’s claim from the typical retaliatory
arrest claim. An official retaliatory policy is a particularly
troubling and potent form of retaliation, for a policy can be
long term and pervasive, unlike an ad hoc, on-the-spot
decision by an individual officer. An official policy also can
be difficult to dislodge. A citizen who suffers retaliation by
an individual officer can seek to have the officer disci-
plined or removed from service, but there may be little
practical recourse when the government itself orchestrates
the retaliation.      For these reasons, when retaliation
against protected speech is elevated to the level of official
policy, there is a compelling need for adequate avenues of
redress.
   In addition, Lozman’s allegations, if proved, alleviate
the problems that the City says will result from applying
Mt. Healthy in retaliatory arrest cases. The causation
problem in arrest cases is not of the same difficulty where,
as is alleged here, the official policy is retaliation for prior,
protected speech bearing little relation to the criminal
offense for which the arrest is made. In determining
whether there was probable cause to arrest Lozman for
disrupting a public assembly, it is difficult to see why a
city official could have legitimately considered that Loz-
man had, months earlier, criticized city officials or filed a
12                LOZMAN v. RIVIERA BEACH

                      Opinion of the Court

lawsuit against the City. So in a case like this one it is
unlikely that the connection between the alleged animus
and injury will be “weakened . . . by [an official’s] legiti-
mate consideration of speech.” Reichle, 566 U. S., at 668.
This unique class of retaliatory arrest claims, moreover,
will require objective evidence of a policy motivated by
retaliation to survive summary judgment. Lozman, for
instance, cites a transcript of a closed-door city council
meeting and a video recording of his arrest. There is thus
little risk of a flood of retaliatory arrest suits against high-
level policymakers.
   As a final matter, it must be underscored that this
Court has recognized the “right to petition as one of the
most precious of the liberties safeguarded by the Bill of
Rights.” BE&K Constr. Co. v. NLRB, 536 U. S. 516, 524
(2002) (internal quotation marks omitted). Lozman alleges
the City deprived him of this liberty by retaliating against
him for his lawsuit against the City and his criticisms of
public officials. Thus, Lozman’s speech is high in the
hierarchy of First Amendment values. See Connick v.
Myers, 461 U. S. 138, 145 (1983).
   For these reasons, Lozman need not prove the absence
of probable cause to maintain a claim of retaliatory arrest
against the City. On facts like these, Mt. Healthy provides
the correct standard for assessing a retaliatory arrest
claim. The Court need not, and does not, address the
elements required to prove a retaliatory arrest claim in
other contexts.
   This is not to say, of course, that Lozman is ultimately
entitled to relief or even a new trial. On remand, the
Court of Appeals, applying Mt. Healthy and other relevant
precedents, may consider any arguments in support of the
District Court’s judgment that have been preserved by the
City. Among other matters, the Court of Appeals may
wish to consider (1) whether any reasonable juror could
find that the City actually formed a retaliatory policy to
                 Cite as: 585 U. S. ____ (2018)           13

                     Opinion of the Court

intimidate Lozman during its June 2006 closed-door ses-
sion; (2) whether any reasonable juror could find that the
November 2006 arrest constituted an official act by the
City; and (3) whether, under Mt. Healthy, the City has
proved that it would have arrested Lozman regardless of
any retaliatory animus—for example, if Lozman’s conduct
during prior city council meetings had also violated valid
rules as to proper subjects of discussion, thus explaining
his arrest here.
   For these reasons, the judgment of the Court of Appeals
is vacated, and the case is remanded for further proceed-
ings consistent with this opinion.
                                            It is so ordered.
                  Cite as: 585 U. S. ____ (2018)            1

                     THOMAS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 17–21
                          _________________


  FANE LOZMAN, PETITIONER v. CITY OF RIVIERA 

              BEACH, FLORIDA

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

          APPEALS FOR THE ELEVENTH CIRCUIT

                         [June 18, 2018] 


   JUSTICE THOMAS, dissenting.
   We granted certiorari to decide “whether the existence
of probable cause defeats a First Amendment claim for
retaliatory arrest under [42 U. S. C.] §1983.” Ante, at 5.
Instead of resolving that question, the Court decides that
probable cause should not defeat a “unique class of retalia-
tory arrest claims.” Ante, at 12. To fall within this unique
class, a claim must involve objective evidence, of an official
municipal policy of retaliation, formed well before the
arrest, in response to highly protected speech, that has
little relation to the offense of arrest. See ante, at 11–12.
No one briefed, argued, or even hinted at the rule that the
Court announces today. Instead of dreaming up our own
rule, I would have answered the question presented and
held that plaintiffs must plead and prove a lack of prob-
able cause as an element of a First Amendment retaliatory-
arrest claim. I respectfully dissent.
                              I
  The petition for certiorari asked us to resolve whether
“the existence of probable cause defeat[s] a First Amend-
ment retaliatory-arrest claim as a matter of law.” Pet. for
Cert. i. That question has divided the federal courts for
decades. See id., at 10–13. We granted certiorari to con-
sider it six years ago in Reichle v. Howards, 566 U. S. 658,
2                    LOZMAN v. RIVIERA BEACH

                         THOMAS, J., dissenting

663 (2012). But we did not resolve it then because the
petitioner’s second question presented—whether qualified
immunity applied—fully resolved the case. Ibid. Since
Reichle, the split in the federal courts has widened. See
Pet. for Cert. 12–13. In this case, we again granted certio-
rari, 538 U. S. ___ (2017), this time only on the question of
probable cause, see Pet. for Cert. i.
  Yet the Court chooses not to resolve that question,
leaving in place the decades-long disagreement among the
federal courts. The parties concentrated all their argu-
ments on this question in their briefs and at oral argu-
ment. Neither party suggested that there was something
special about Fane Lozman’s claim that would justify a
narrower rule. See, e.g., Tr. of Oral Arg. 15–16 (refusing
to take the “fallback position” that this “is some special
kind of case”). Yet the Court does that work for them by
defining a “unique class of retaliatory arrest claims” that
do not require plaintiffs to plead and prove a lack of prob-
able cause. Ante, at 12.
  By my count, the Court has identified five conditions
that are necessary to trigger its new rule. First, there
must be “an ‘official municipal policy’ of intimidation.”
Ante, at 11 (quoting Monell v. New York City Dept. of
Social Servs., 436 U. S. 658, 691 (1978)). Second, the
policy must be “premeditated” and formed well before the
arrest—here, for example, the policy was formed “months
earlier.” Ante, at 11.1 Third, there must be “objective
evidence” of such a policy. Ante, at 12. Fourth, there must
be “little relation” between the “protected speech” that
prompted the retaliatory policy and “the criminal offense
——————
  1 This requirement suggests that the Court’s rule does not apply

when the “policy” that the plaintiff challenges is an on-the-spot decision
by a single official with final policymaking authority, like the “policy”
that this Court recognized in Pembaur v. Cincinnati, 475 U. S. 469
(1986). See id., at 484–485 (holding that a county prosecutor’s order to
forcibly enter the plaintiff’s clinic was a “municipal policy”).
                     Cite as: 585 U. S. ____ (2018)                     3

                         THOMAS, J., dissenting

for which the arrest is made.” Ante, at 11. Finally, the
protected speech that provoked the retaliatory policy must
be “high in the hierarchy of First Amendment values.”
Ante, at 12. Where all these features are present, the
Court explains, there is not the same “causation problem”
that exists for other retaliatory-arrest claims. Ante, at 11.
  I find it hard to believe that there will be many cases
where this rule will even arguably apply, and even harder
to believe that the plaintiffs in those cases will actually
prove all five requirements. Not even Lozman’s case is a
good fit, as the Court admits when it discusses the rele-
vant considerations for remand. See ante, at 12–13. In
my view, we should not have gone out of our way to fash-
ion a complicated rule with no apparent applicability to
this case or any other.
                               II
   Turning to the question presented, I would hold that
plaintiffs bringing a First Amendment retaliatory-arrest
claim must plead and prove an absence of probable cause.2
This Court has “repeatedly noted that 42 U. S. C. §1983
creates ‘ “a species of tort liability.” ’ ” Memphis Commu-
nity School Dist. v. Stachura, 477 U. S. 299, 305 (1986)
(footnote omitted). Accordingly, we “defin[e] the contours
and prerequisites of a §1983 claim” by “look[ing] first to
the common law of torts.” Manuel v. Joliet, 580 U. S. ___,
___ (2017) (slip op., at 12); see, e.g., Heck v. Humphrey,
512 U. S. 477, 484 (1994) (analogizing to the “common-law
cause of action for malicious prosecution”); id., at 491
(THOMAS, J., concurring) (emphasizing that the decision
——————
   2 I am skeptical that 42 U. S. C. §1983 recognizes a claim for retalia-

tory arrests under the First Amendment. I adhere to the view that “no
‘intent-based’ constitutional tort would have been actionable under the
§1983 that Congress enacted.” Crawford-El v. Britton, 523 U. S. 574,
612 (1998) (Scalia, J., dissenting). But because no party presses this
argument, I assume that such claims are actionable under §1983.
4                LOZMAN v. RIVIERA BEACH

                     THOMAS, J., dissenting

was “consistent . . . with the state of the common law at
the time §1983 was enacted”).
   When §1983 was enacted, there was no common-law tort
for retaliatory arrest in violation of the freedom of speech.
See Hartman v. Moore, 547 U. S. 250, 259 (2006). I would
therefore look to the common-law torts that “provid[e] the
closest analogy” to this claim. Heck, supra, at 484. The
closest analogs here are the three arrest-based torts under
the common law: false imprisonment, malicious prosecu-
tion, and malicious arrest. In defining the elements of
these three torts, 19th-century courts emphasized the
importance of probable cause.
   Consider first the tort of false imprisonment. Common-
law courts stressed the need to shape this tort with an
“indulgence” for peace officers, who are “specially charged
with a duty in the enforcement of the laws.” T. Cooley,
Law of Torts 175 (1880) (Cooley); see, e.g., Hogg v. Ward, 3
H. & N. 417, 423, 157 Eng. Rep. 533, 536 (Ex. 1858) (opin-
ion of Watson, B.) (stressing “the utmost importance that
the police throughout the country should be supported in
the execution of their duty”). Accordingly, private citizens
were always liable for false imprisonment if the arrestee
had not actually committed a felony, but constables were
“excused” if they had “made [the arrest] on reasonable
grounds of belief ”—i.e., probable cause. Cooley 175; ac-
cord, 2 C. Addison, Law of Torts §803, p. 18 (1876); 1 F.
Hilliard, The Law of Torts or Private Wrongs §18, pp. 207–
208, and n. (a) (1866). As Lord Mansfield explained, it
was “of great consequence to the police” that probable
cause shield officers from false-imprisonment claims, as “it
would be a terrible thing” if the threat of liability dissuaded
them from performing their official duties. Ledwith v.
Catchpole, 2 Cald. 291, 295 (K. B. 1783). This concern
outweighed “the mischief and inconvenience to the public”
from the reality that “[m]any an innocent man has and
may be taken up upon suspicion.” Ibid. Many State Su-
                  Cite as: 585 U. S. ____ (2018)            5

                     THOMAS, J., dissenting

preme Courts agreed with Lord Mansfield’s reasoning.
See, e.g., Burns v. Erben, 40 N. Y. 463, 469 (1869) (opinion
of Woodruff, J.) (quoting Ledwith); Brockway v. Crawford,
48 N. C. 433, 437 (1856) (“[The] exempt[ion] for responsi-
bility” for arrests based on probable cause “encourages . . .
a sharp look-out for the apprehension of felons”). As one
court put it, “How, in the great cities of this land, could
police power be exercised, if every peace officer is liable to
civil action for false imprisonment” whenever “persons
arrested upon probable cause shall afterwards be found
innocent?” Hawley v. Butler, 54 Barb. 490, 496 (N. Y. Sup.
1868).
   Courts also stressed the importance of probable cause
when defining the torts of malicious prosecution and
malicious arrest. See, e.g., Ahern v. Collins, 39 Mo. 145,
150 (1866) (holding that “malice and want of probable
cause are necessary ingredients of both”). For the tort of
malicious prosecution, courts emphasized the “necessity”
of both the “allegation” and “proof ” of probable cause, in
light of the public interest “that criminals should be
brought to justice.” Hogg v. Pinckney, 16 S. C. 387, 393
(1882); see also Chrisman v. Carney, 33 Ark. 316, 326
(1878) (“The existence of probable cause is of itself alone a
complete defense . . . . The interest which society has in
the enforcement of the criminal laws requires this rule”).
Similarly, if the element of probable cause were not
“strictly guarded,” “ill consequences would ensue to the
public, for no one would willingly undertake to vindicate a
breach of the public law and discharge his duty to society,
with the prospect of an annoying suit staring him in the
face.” Ventress v. Rosser, 73 Ga. 534, 541 (1884); accord,
Cardival v. Smith, 109 Mass. 158 (1872). The element of
probable cause also played an evidentiary role for both
torts. Lack of probable cause provided “evidence of malice,
though inconclusive,” Herman v. Brookerhoff, 8 Watts 240,
241 (Pa. 1839), because “[m]alice may be inferred from a
6                 LOZMAN v. RIVIERA BEACH

                      THOMAS, J., dissenting

total want of probable cause,” Ventress, supra, at 541;
accord, Ahern, supra, at 150.
  In sum, when §1983 was enacted, the common law
recognized probable cause as an important element for
ensuring that arrest-based torts did not unduly interfere
with the objectives of law enforcement. Common-law
courts were wary of “throw[ing] down the bars which
protect public officers from suits for acts done within the
scope of their duty and authority, by recognizing the right
of every one who chooses to imagine or assert that he is
aggrieved by their doings, to make use of an allegation
that they were malicious in motive to harass them with
suits on that ground.” Chelsey v. King, 74 Me. 164, 175–
176 (1882).
  Applying that principle here, it follows that plaintiffs
bringing a First Amendment retaliatory-arrest claim
under §1983 should have to plead and prove a lack of
probable cause. I see no justification for deviating from
the historical practice simply because an arrest claim is
framed in terms of the First Amendment. Even under a
First Amendment theory, “the significance of probable
cause or the lack of it looms large.” Hartman, 547 U. S., at
265. The presence of probable cause will tend to disprove
that the arrest was done out of retaliation for the plaintiff ’s
speech, and the absence of probable cause will tend to
prove the opposite. See id., at 261. Because “[p]robable
cause or its absence will be at least an evidentiary issue in
practically all such cases” and “[b]ecause showing [its]
absence . . . will have high probative force, and can be
made mandatory with little or no added cost,” the absence
of probable cause should be an “element” of the plaintiff ’s
case. Id., at 265–266; see also id., at 264, n. 10 (refusing
to carve out an exception for unusual cases).
  Moreover, as with the traditional arrest-based torts,
police officers need the safe harbor of probable cause in
the First Amendment context to be able to do their jobs
                  Cite as: 585 U. S. ____ (2018)            7

                     THOMAS, J., dissenting

effectively. Police officers almost always exchange words
with suspects before arresting them. And often a suspect’s
“speech provides evidence of a crime or suggests a poten-
tial threat.” Reichle, 566 U. S., at 668. If probable cause
were not required, the threat of liability might deter an
officer from arresting a suspected criminal who, for exam-
ple, has a political bumper sticker on his car, cf. Kilpatrick
v. United States, 432 Fed. Appx. 937 (CA11 2011); is par-
ticipating in a politically tinged protest, Morse v. San
Francisco Bay Area Rapid Transit Dist., 2014 WL 572352
(ND Cal., Feb. 11, 2014); or confronts and criticizes the
officer during the arrest of a third party, Holland v. San
Francisco, 2013 WL 968295 (ND Cal., Mar. 12, 2013).
Allowing plaintiffs to bring a retaliatory-arrest claim in
such circumstances, without pleading and proving a lack
of probable cause, would permit plaintiffs to harass offi-
cers with the kind of suits that common-law courts deemed
intolerable.
                      *    *    *
  Because we should have answered the question presented
and held that probable cause necessarily defeats First
Amendment retaliatory-arrest claims, I respectfully
dissent.

```

---
