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

## GROUP: content/cases/Oliver v. United States.md  (`case`, 6 assertions)

### content_page

```
---
title: "Oliver v. United States"
type: case
citation: "466 U.S. 170 (1984)"
parallel_cite: "104 S. Ct. 1735; 80 L. Ed. 2d 214; 52 U.S.L.W. 4425"
neutral_cite: 1984 U.S. LEXIS 55
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-04-17
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-04-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Oliver v. United States
  varies_by_point: false
  scope_note: "Reaffirms the open-fields doctrine and the curtilage distinction; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111146/oliver-v-united-states/"
  cluster_id: 111146
  opinion_id: 9429563
  identity_checked: true
homes:
  - page: "[[Open Fields]]"
    role: "Key — Anchor"
  - page: "[[Curtilage]]"
    role: "Key"
related: ["[[Hester v. United States]]", "[[United States v. Dunn]]", "[[Florida v. Jardines]]", "[[California v. Ciraolo]]"]
aliases: []
tags: ["case", "fourth-amendment", "open-fields", "curtilage", "search"]
holding: "Reaffirms that open fields get no Fourth Amendment protection — even fenced, posted 'No Trespassing' land; only curtilage carries the home's protection."
lake:
  record_id: Oliver v. United States
  status: verified
  projected_at: 2026-07-06
---

# Oliver v. United States

*466 U.S. 170 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Acting on a tip, officers went onto Oliver's farm, drove past his house, went around a locked gate marked with a "No Trespassing" sign, and walked along a footpath into a secluded field, where they found a marijuana crop more than a mile from his house. (Decided together with *Maine v. Thornton*.)

## Issue
Whether the open-fields doctrine applies even to fields that are fenced, posted with "No Trespassing" signs, and secluded.

## Rule
Yes. "[O]pen fields do not provide the setting for those intimate activities that the Amendment is intended to shelter from government interference or surveillance." — 466 U.S. at 179. ^pin-179

Fencing and posting do not change that: "It is not generally true that fences or 'No Trespassing' signs effectively bar the public from viewing open fields." — *Id.* ^pin-179b

The common law "distinguished 'open fields' from the 'curtilage,' the land immediately surrounding and associated with the home," and "[t]he distinction implies that only the curtilage, not the neighboring open fields, warrants the Fourth Amendment protections that attach to the home." — *Id.* at 180. ^pin-180

## Application
The marijuana field, located more than a mile from Oliver's house and outside the [[Curtilage|curtilage]], was an open field. The locked gate and "No Trespassing" sign did not give it Fourth Amendment protection, so the officers' entry onto the land and observation of the crop were not a "search." The evidence was not subject to suppression on Fourth Amendment grounds.

## Conclusion
Because the field was an open field outside the [[Curtilage|curtilage]], no Fourth Amendment search occurred; the open-fields doctrine controlled.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Oliver* reaffirms the open-fields rule of [[Hester v. United States]] and frames the open-fields/[[Curtilage|curtilage]] line later refined by the four-factor test of [[United States v. Dunn]]; [[Curtilage|curtilage]]'s protection at the home's entrance was reinforced in [[Florida v. Jardines]].

## Appears on
- [[Curtilage]] — *Key — Progeny / Refinement*

## Sources
- *Oliver v. United States*, 466 U.S. 170 (1984) — https://www.courtlistener.com/opinion/111146/oliver-v-united-states/ — pinpoints: 179, 180.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "dff300802bb5e5c8", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "466 U.S. 170 (1984)", "court": "U.S. Supreme Court", "neutral_cite": "1984 U.S. LEXIS 55", "official_citation_present": true, "parallel_cite": "104 S. Ct. 1735; 80 L. Ed. 2d 214; 52 U.S.L.W. 4425", "title": "Oliver v. United States", "year": "1984"}}
{"assertion_id": "931e9eb14ca7ece1", "dimension": "support", "kind": "home_role", "locator": {"home": "Curtilage"}, "payload": {"home": "Curtilage", "role": "Key", "title": "Oliver v. United States"}}
{"assertion_id": "9703f0fa53cc3fd7", "dimension": "support", "kind": "home_role", "locator": {"home": "Open Fields"}, "payload": {"home": "Open Fields", "role": "Key — Anchor", "title": "Oliver v. United States"}}
{"assertion_id": "f9abd2cc0e5582e8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Reaffirms that open fields get no Fourth Amendment protection — even fenced, posted 'No Trespassing' land; only curtilage carries the home's protection.", "title": "Oliver v. United States"}}
{"assertion_id": "8611f81071037222", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1984-04-17", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Oliver v. United States", "field_i_validity": "good_law", "scope_note": "Reaffirms the open-fields doctrine and the curtilage distinction; good law.", "title": "Oliver v. United States", "varies_by_point": "false"}}
{"assertion_id": "c3ac9b2f89124b5c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Oliver v. United States"}}
```

### lake record — Oliver v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Oliver v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Oliver v. United States",
    "case_name_short": "Oliver",
    "case_name_full": "Oliver v. United States",
    "input_case_name": "Oliver v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-04-17",
    "year": 1984,
    "docket": null,
    "cluster_id": 111146,
    "lead_opinion_id": 9429563,
    "sibling_ids": [
      111146,
      9429563,
      9429564,
      9429565
    ],
    "absolute_url": "/opinion/111146/oliver-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9050194,
        "score": 20,
        "case_name": "Oliver v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "466 U.S. 170",
      "volume": "466",
      "reporter": "U.S.",
      "page": "170",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 1735",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "1735",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 2d 214",
        "volume": "80",
        "reporter": "L. Ed. 2d",
        "page": "214",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4425",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4425",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 55",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "55",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "466 U.S. 170",
        "volume": "466",
        "reporter": "U.S.",
        "page": "170",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 1735",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "1735",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 2d 214",
        "volume": "80",
        "reporter": "L. Ed. 2d",
        "page": "214",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 55",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "55",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4425",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4425",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "466 U.S. 170",
    "official_selection": {
      "court_class": "scotus",
      "selected": "466 U.S. 170",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-179",
      "page": null,
      "quote": "signs, and secluded. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-179b",
      "page": null,
      "quote": "It is not generally true that fences or 'No Trespassing' signs effectively bar the public from viewing open fields.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-180",
      "page": null,
      "quote": "distinguished 'open fields' from the 'curtilage,' the land immediately surrounding and associated with the home,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-04-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Oliver v. United States",
    "varies_by_point": false,
    "scope_note": "Reaffirms the open-fields doctrine and the curtilage distinction; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Poulson v. Commonwealth",
          "cluster_id": 10375911,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane1_negative"
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
        "journal_ref": "Oliver v. United States:lane1_negative"
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
        "journal_ref": "Oliver v. United States:lane1_negative"
      },
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
        "journal_ref": "Oliver v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rickey Beene",
          "cluster_id": 3183556,
          "cite": [
            "818 F.3d 157",
            "2016 U.S. App. LEXIS 4331",
            "2016 WL 890127"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4288590,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4287047,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4286131,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane1_negative"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyllo v. United States",
          "cluster_id": 118443,
          "cite": [
            "150 L. Ed. 2d 94",
            "121 S. Ct. 2038",
            "533 U.S. 27",
            "2001 U.S. LEXIS 4487"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Ciraolo",
          "cluster_id": 111666,
          "cite": [
            "90 L. Ed. 2d 210",
            "106 S. Ct. 1809",
            "476 U.S. 207",
            "1986 U.S. LEXIS 154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Greenwood",
          "cluster_id": 112067,
          "cite": [
            "100 L. Ed. 2d 30",
            "108 S. Ct. 1625",
            "486 U.S. 35",
            "1988 U.S. LEXIS 2279",
            "56 U.S.L.W. 4409"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shirley Presley v. City of Charlottesville Rivanna Trails Foundation",
          "cluster_id": 795822,
          "cite": [
            "464 F.3d 480",
            "2006 U.S. App. LEXIS 24048",
            "2006 WL 2709208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karo",
          "cluster_id": 111257,
          "cite": [
            "82 L. Ed. 2d 530",
            "104 S. Ct. 3296",
            "468 U.S. 705",
            "1984 U.S. LEXIS 148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ross",
          "cluster_id": 1060457,
          "cite": [
            "49 S.W.3d 833",
            "2001 Tenn. LEXIS 563",
            "2001 WL 760100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ramirez-Portoreal",
          "cluster_id": 2033638,
          "cite": [
            "666 N.E.2d 207",
            "88 N.Y.2d 99",
            "643 N.Y.S.2d 502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Pitman",
          "cluster_id": 2234418,
          "cite": [
            "813 N.E.2d 93",
            "211 Ill. 2d 502",
            "286 Ill. Dec. 36",
            "2004 Ill. LEXIS 989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Riley",
          "cluster_id": 112175,
          "cite": [
            "102 L. Ed. 2d 835",
            "109 S. Ct. 693",
            "488 U.S. 445",
            "1989 U.S. LEXIS 580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111146 OR 9429563 OR 9429564 OR 9429565) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDMwMjY1NjAwMDAwJnM9Mjc5NzI3NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111146+OR+9429563+OR+9429564+OR+9429565%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111146 OR 9429563 OR 9429564 OR 9429565)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMTYmcz0xNDM1NDY5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111146+OR+9429563+OR+9429564+OR+9429565%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111146 OR 9429563 OR 9429564 OR 9429565)",
        "reviewed": 40,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 40,
        "triage_read": 1,
        "triage_snippet_classified": 39
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111146 OR 9429563 OR 9429564 OR 9429565)",
    "indexed_citing_opinions": 1195,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111146,
        "count": 1026,
        "count_source": "search"
      },
      {
        "opinion_id": 9429563,
        "count": 201,
        "count_source": "search"
      },
      {
        "opinion_id": 9429564,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429565,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1924,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/oliver-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5OTk3NzImcz0xMDEyNDc3OCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111146+OR+9429563+OR+9429564+OR+9429565%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111146,
        "cited_id": 85272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 85827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 103355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 106538,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 108988,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 109032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 238889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 285923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 304813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 308561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 340832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 358699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 388191,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 393323,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 398901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 421926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 1092690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 1503690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 1557741,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 1852754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 1948051,
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
    "date_created": "2026-07-05T16:08:49Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:09:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:09:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:11:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:09:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Oliver v. United States

```
<opinion type="majority">
<author id="b233-7"><page-number citation-index="1" label="173">*173</page-number>Justice Powell</author>
<p id="Az-">delivered the opinion of the Court.</p>
<p id="b233-8">The “open fields” doctrine, first enunciated by this Court in <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924), permits police officers to enter and search a field without a warrant. We granted certiorari in these cases to clarify confusion that has arisen as to the continued vitality of the doctrine.</p>
<p id="b233-3">
<em>I</em>
</p>
<p id="AC-">No. 82-15.Acting on reports that marihuana was being raised on the farm of petitioner Oliver, two narcotics agents of the Kentucky State Police went to the farm to investigate.<footnotemark>1</footnotemark> Arriving at the farm, they drove past petitioner's house to a locked gate with a “No Trespassing” sign. A footpath led around one side of the gate. The agents walked around the gate and along the road for several hundred yards, passing a bam and a parked camper. At that point, someone standing in front of the camper shouted: “No hunting is allowed, come back up here.” The officers shouted back that they were Kentucky State Police officers, but found no one when they returned to the camper. The officers resumed their investigation of the farm and found a field of marihuana over a mile from petitioner’s home.</p>
<p id="b233-4">Petitioner was arrested and indicted for “manufacturing]” a “controlled substance.” <span class="citation no-link">21 U. S. C. § 841</span>(a)(1). After a pretrial hearing, the District Court suppressed evidence of the discovery of the marihuana field. Applying <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (1967), the court found that petitioner had a reasonable expectation that the field would remain private because petitioner “had done all that could be expected of him to assert his privacy in the area of farm that was searched.” He had posted “No Trespassing” signs at regular intervals and had locked the gate at the entrance to the center of the farm. App. to Pet. for Cert. in No. 82-15, <page-number citation-index="1" label="174">*174</page-number>pp. 23-24. Further, the court noted that the field itself is highly secluded: it is bounded on all sides by woods, fences, and embankments and cannot be seen from any point of public access. The court concluded that this was not an “open” field that invited casual intrusion.</p>
<p id="b234-5">The Court of Appeals for the Sixth Circuit, sitting en banc, reversed the District Court. <span class="citation multiple-matches"><a href="/c/F.%202d/686/356/">686 F. 2d 356</a></span> (1982).<footnotemark>2</footnotemark> The court concluded that <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>upon which the District Court relied, had not impaired the vitality of the open fields doctrine of <em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">Hester</a></span>. </em>Rather, the open fields doctrine was entirely compatible with <em>Katz’ </em>emphasis on privacy. The court reasoned that the “human relations that create the need for privacy do not ordinarily take place” in open fields, and that the property owner’s common-law right to exclude trespassers is insufficiently linked to privacy to warrant the Fourth Amendment’s protection. 686 F. 2d, at 360.<footnotemark>3</footnotemark> We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./459/1168/">459 U. S. 1168</a></span> (1983).</p>
<p id="b234-6"><em>No. 82-1273. </em>After receiving an anonymous tip that marihuana was being grown in the woods behind respondent Thornton’s residence, two police officers entered the woods by a path between this residence and a neighboring house. They followed a footpath through the woods until they reached two marihuana patches fenced with chicken wire. Later, the officers determined that the patches were on the property of respondent, obtained a warrant to search the property, and seized the marihuana. On the basis of this evidence, respondent was arrested and indicted.</p>
<p id="b235-4"><page-number citation-index="1" label="175">*175</page-number>The trial court granted respondent’s motion to suppress the fruits of the second search. The warrant for this search was premised on information that the police had obtained during their previous warrantless search, that the court found to be unreasonable.<footnotemark>4</footnotemark> “No Trespassing” signs and the secluded location of the marihuana patches evinced a reasonable expectation of privacy. Therefore, the court held, the open fields doctrine did not apply.</p>
<p id="b235-5">The Maine Supreme Judicial Court affirmed. <span class="citation" data-id="1948051"><a href="/opinion/1948051/state-v-thornton/" aria-description="Citation for case: State v. Thornton">453 A. 2d 489</a></span> (1982). It agreed with the trial court that the correct question was whether the search “is a violation of privacy on which the individual justifiably relied,” <span class="citation" data-id="1948051"><a href="/opinion/1948051/state-v-thornton/#493" aria-description="Citation for case: State v. Thornton"><em>id., </em>at 493</a></span>, and that the search violated respondent’s privacy. The court also agreed that the open fields doctrine did not justify the search. That doctrine applies, according to the court, only when officers are lawfully present on property and observe “open and patent” activity. <span class="citation" data-id="1948051"><a href="/opinion/1948051/state-v-thornton/#495" aria-description="Citation for case: State v. Thornton"><em>Id., </em>at 495</a></span>. In this case, the officers had trespassed upon defendant’s property, and the respondent had made every effort to conceal his activity. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./460/1068/">460 U. S. 1068</a></span> (1983).<footnotemark>5</footnotemark></p>
<p id="pAaq"><page-number citation-index="1" label="176">*176</page-number>h — I</p>
<p id="b236-3">The rule announced in <em>Hester </em>v. <em>United States </em>was founded upon the explicit language of the Fourth Amendment. That Amendment indicates with some precision the places and things encompassed by its protections. As Justice Holmes explained for the Court in his characteristically laconic style: “[T]he special protection accorded by the Fourth Amendment to the people in their ‘persons, houses, papers, and effects,’ is not extended to the open fields. The distinction between the latter and the house is as old as the common law.” <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#59" aria-description="Citation for case: Hester v. United States">265 U. S., at 59</a></span>.<footnotemark>6</footnotemark></p>
<p id="b236-4">Nor are the open fields “effects” within the meaning of the Fourth Amendment. In this respect, it is suggestive that James Madison’s proposed draft of what became the Fourth <page-number citation-index="1" label="177">*177</page-number>Amendment preserves “[t]he rights of the people to be secured in their persons, their houses, their papers, and their other property, from all unreasonable searches and seizures . . . .” See N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 100, n. 77 (1937). Although Congress’ revisions of Madison’s proposal broadened the scope of the Amendment in some respects, <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#100" aria-description="Citation for case: Hester v. United States"><em>id., </em>at 100-103</a></span>, the term “effects” is less inclusive than “property” and cannot be said to encompass open fields.<footnotemark>7</footnotemark> We conclude, as did the Court in deciding <em>Hester </em>v. <em>United States, </em>that the government’s intrusion upon the open fields is not one of those “unreasonable searches” proscribed by the text of the Fourth Amendment.</p>
<p id="pAku">hH HH</p>
<p id="b237-3">This interpretation of the Fourth Amendment’s language is consistent with the understanding of the right to privacy expressed in our Fourth Amendment jurisprudence. Since <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), the touchstone of Amendment analysis has been the question whether a person has a “constitutionally protected reasonable expectation of privacy.” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States"><em>Id., </em>at 360</a></span> (Harlan, J., concurring). The Amendment does not protect the merely subjective expectation of privacy, but only those “expectation[s] that society is prepared to recognize as ‘reasonable.’” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States"><em>Id., </em>at 361</a></span>. See also <em>Smith </em>v. <em>Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#740" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735, 740-741</a></span> (1979).</p>
<p id="b237-4">A</p>
<p id="b237-5">No single factor determines whether an individual legitimately may claim under the Fourth Amendment that a place should be free of government intrusion not authorized by warrant. See <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#152" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 152-153</a></span> <page-number citation-index="1" label="178">*178</page-number>(1978) (Powell, J., concurring). In assessing the degree to which a search infringes upon individual privacy, the Court has given weight to such factors as the intention of the Framers of the Fourth Amendment, <em>e. g., United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#7" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 7-8</a></span> (1977), the uses to which the individual has put a location, <em>e. g., Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#265" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 265</a></span> (1960), and our societal understanding that certain areas deserve the most scrupulous protection from government invasion, <em>e. g., Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980). These factors are equally relevant to determining whether the government’s intrusion upon open fields without a warrant or probable cause violates reasonable expectations of privacy and is therefore a search proscribed by the Amendment.</p>
<p id="b238-5">In this light, the rule of <em>Hester </em>v. <em>United States, supra, </em>that we reaffirm today, may be understood as providing that an individual may not legitimately demand privacy for activities conducted out of doors in fields, except in the area immediately surrounding the home. See also <em>Air Pollution Variance Bd. </em>v. <em>Western Alfalfa Corp., </em><span class="citation" data-id="109032"><a href="/opinion/109032/air-pollution-variance-bd-of-colo-v-western-alfalfa-corp/#865" aria-description="Citation for case: Air Pollution Variance Bd. of Colo. v. Western Alfalfa Corp.">416 U. S. 861, 865</a></span> (1974). This rule is true to the conception of the right to privacy embodied in the Fourth Amendment. The Amendment reflects the recognition of the Framers that certain enclaves should be free from arbitrary government interference. For example, the Court since the enactment of the Fourth Amendment has stressed “the overriding respect for the sanctity of the home that has been embedded in our traditions since the origins of the Republic.” <em>Payton </em>v. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#601" aria-description="Citation for case: Payton v. New York"><em>New York, supra, </em>at 601</a></span>.<footnotemark>8</footnotemark> See also <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511</a></span> (1961); <em>United States </em>v. <em>United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span> (1972).</p>
<p id="b239-4"><page-number citation-index="1" label="179">*179</page-number>In contrast, open fields do not provide the setting for those intimate activities that the Amendment is intended to shelter from government interference or surveillance. There is no societal interest in protecting the privacy of those activities, such as the cultivation of crops, that occur in open fields. Moreover, as a practical matter these lands usually are accessible to the public and the police in ways that a home, an office, or commercial structure would not be. It is not generally true that fences or “No Trespassing” signs effectively bar the public from viewing open fields in rural areas. And both petitioner Oliver and respondent Thornton concede that the public and police lawfully may survey lands from the air.<footnotemark>9</footnotemark> For these reasons, the asserted expectation of privacy in open fields is not an expectation that “society recognizes as reasonable.”<footnotemark>10</footnotemark></p>
<p id="b240-4"><page-number citation-index="1" label="180">*180</page-number>The historical underpinnings of the open fields doctrine also demonstrate that the doctrine is consistent with respect for “reasonable expectations of privacy. ” As Justice Holmes, writing for the Court, observed in <em>Hester, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#59" aria-description="Citation for case: Hester v. United States">265 U. S., at 59</a></span>, the common law distinguished “open fields” from the “curti-lage,” the land immediately surrounding and associated with the home. See 4 W. Blackstone, Commentaries *225. The distinction implies that only the curtilage, not the neighboring open fields, warrants the Fourth Amendment protections that attach to the home. At common law, the curtilage is the area to which extends the intimate activity associated with the “sanctity of a man’s home and the privacies of life,” <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span> (1886), and therefore has been considered part of the home itself for Fourth Amendment purposes. Thus, courts have extended Fourth Amendment protection to the curtilage; and they have defined the curtilage, as did the common law, by reference to the factors that determine whether an individual reasonably may expect that an area immediately adjacent to the home will remain private. See, <em>e. g., United States </em>v. <em>Van Dyke, </em><span class="citation" data-id="388191"><a href="/opinion/388191/united-states-v-larry-g-van-dyke/#993" aria-description="Citation for case: United States v. Larry G. Van Dyke">643 F. 2d 992, 993-994</a></span> (CA4 1981); <em>United States </em>v. <em>Williams, </em><span class="citation" data-id="358699"><a href="/opinion/358699/united-states-v-otis-williams/#453" aria-description="Citation for case: United States v. Otis Williams">581 F. 2d 451, 453</a></span> (CA5 1978); <em>Care </em>v. <em>United States, </em><span class="citation" data-id="238889"><a href="/opinion/238889/orval-care-v-united-states/#25" aria-description="Citation for case: Orval Care v. United States">231 F. 2d 22, 25</a></span> (CA10), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./351/932/">351 U. S. 932</a></span> (1956). Conversely, the common law implies, as we reaffirm today, that no expectation of privacy legitimately attaches to open fields.<footnotemark>11</footnotemark></p>
<p id="b241-4"><page-number citation-index="1" label="181">*181</page-number>We conclude, from the text of the Fourth Amendment and from the historical and contemporary understanding of its purposes, that an individual has no legitimate expectation that open fields will remain free from warrantless intrusion by government officers.</p>
<p id="b241-5">B</p>
<p id="b241-6">Petitioner Oliver and respondent Thornton contend, to the contrary, that the circumstances of a search sometimes may indicate that reasonable expectations of privacy were violated; and that courts therefore should analyze these circumstances on a case-by-case basis. The language of the Fourth Amendment itself answers their contention.</p>
<p id="b241-7">Nor would a case-by-case approach provide a workable accommodation between the needs of law enforcement and the interests protected by the Fourth Amendment. Under this approach, police officers would have to guess before every search whether landowners had erected fences sufficiently high, posted a sufficient number of warning signs, or located contraband in an area sufficiently secluded to establish a right of privacy. The lawfulness of a search would turn on “ ‘[a] highly sophisticated set of rules, qualified by all sorts of ifs, ands, and buts and requiring the drawing of subtle nuances and hairline distinctions . . . <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#458" aria-description="Citation for case: New York v. Belton">453 U. S. 454, 458</a></span> (1981) (quoting LaFave, “Case-By-Case Adjudication” versus “Standardized Procedures”: The Robinson Dilemma, 1974 S. Ct. Rev. 127, 142). This Court repeatedly has acknowledged the difficulties created for courts, police, and citizens by an ad hoc, case-by-case definition of Fourth Amendment standards to be applied in differing factual circumstances. See <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#458" aria-description="Citation for case: New York v. Belton"><em>Belton, supra, </em>at 458-460</a></span>; <em>Robbins </em>v. <em>California, </em><span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#430" aria-description="Citation for case: Robbins v. California">453 U. S. 420, 430</a></span> (1981) (Powell, J., concurring in judgment); <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#213" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 213-214</a></span> (1979); <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 235</a></span> (1973). The ad hoc approach not only makes it difficult for the policeman to discern the scope of his authority, <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton"><em>Belton, supra, </em>at 460</a></span>; it also creates a danger that consti<page-number citation-index="1" label="182">*182</page-number>tutional rights will be arbitrarily and inequitably enforced. Cf. <em>Smith </em>v. <em>Goguen, </em><span class="citation" data-id="9425639"><a href="/opinion/108988/smith-v-goguen/#572" aria-description="Citation for case: Smith v. Goguen">415 U. S. 566, 572-573</a></span> (1974).<footnotemark>12</footnotemark></p>
<p id="b242-5">IV</p>
<p id="b242-6">In any event, while the factors that petitioner Oliver and respondent Thornton urge the courts to consider may be relevant to Fourth Amendment analysis in some contexts, these factors cannot be decisive on the question whether the search of an open field is subject to the Amendment. Initially, we reject the suggestion that steps taken to protect privacy establish that expectations of privacy in an open field are legitimate. It is true, of course, that petitioner Oliver and respondent Thornton, in order to conceal their criminal activities, planted the marihuana upon secluded land and erected fences and “No Trespassing” signs around the property. And it may be that because of such precautions, few members of the public stumbled upon the marihuana crops seized by the police. Neither of these suppositions demonstrates, however, that the expectation of privacy was <em>legitimate </em>in the sense required by the Fourth Amendment. The test of legitimacy is not whether the individual chooses to conceal assertedly “private” activity.<footnotemark>13</footnotemark> Rather, the correct inquiry is whether the government’s intrusion infringes upon the per<page-number citation-index="1" label="183">*183</page-number>sonal and societal values protected by the Fourth Amendment. As we have explained, we find no basis for concluding that a police inspection of open fields accomplishes such an infringement.</p>
<p id="b243-5">Nor is the government’s intrusion upon an open field a “search” in the constitutional sense because that intrusion is a trespass at common law. The existence of a property right is but one element in determining whether expectations of privacy are legitimate. “ ‘The premise that property interests control the right of the Government to search and seize has been discredited.’” <em>Katz, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S., at 353</a></span> (quoting <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#304" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 304</a></span> (1967)). “[E]ven a property interest in premises may not be sufficient to establish a legitimate expectation of privacy with respect to particular items located on the premises or activity conducted thereon.” <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#144" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 144, n. 12</a></span>.</p>
<p id="b243-6">The common law may guide consideration of what areas are protected by the Fourth Amendment by defining areas whose invasion by others is wrongful. <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#153" aria-description="Citation for case: Rakas v. Illinois">Id., at 153</a></span> (Powell, J., concurring).<footnotemark>14</footnotemark> The law of trespass, however, forbids intrusions upon land that the Fourth Amendment would not proscribe. For trespass law extends to instances where the exercise of the right to exclude vindicates no legitimate privacy interest.<footnotemark>15</footnotemark> Thus, in the case of open fields, the general <page-number citation-index="1" label="184">*184</page-number>rights of property protected by the common law of trespass have little or no relevance to the applicability of the Fourth Amendment.</p>
<p id="b244-5">V</p>
<p id="b244-6">We conclude that the open fields doctrine, as enunciated in <em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">Hester</a></span>, </em>is consistent with the plain language of the Fourth Amendment and its historical purposes. Moreover, Justice Holmes’ interpretation of the Amendment in <em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">Hester</a></span> </em>accords with the “reasonable expectation of privacy” analysis developed in subsequent decisions of this Court. We therefore affirm <em>Oliver </em>v. <em>United States; Maine </em>v. <em>Thornton </em>is reversed and remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b244-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b233-5"> It is conceded that the police did not have a warrant authorizing the search, that there was no probable cause for the search, and that no exception to the warrant requirement is applicable.</p>
</footnote>
<footnote label="2">
<p id="b234-7"> A panel of the Sixth Circuit had affirmed the suppression order. <span class="citation" data-id="393323"><a href="/opinion/393323/united-states-v-ray-e-oliver-aka-edward-ray-oliver/" aria-description="Citation for case: United States v. Ray E. Oliver, A/K/A Edward Ray Oliver">657 F. 2d 85</a></span> (1981).</p>
</footnote>
<footnote label="3">
<p id="b234-8"> The four dissenting judges contended that the open fields doctrine did not apply where, as in this case, “reasonable effortfs] [have] been made to exclude the public.” 686 F. 2d, at 372. To that extent, the dissent considered that <em>Katz </em>v. <em>United States </em>implicitly had overruled previous holdings of this Court. The dissent then concluded that petitioner had established a “reasonable expectation of privacy” under the <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>standard. Judge Lively also wrote separately to argue that the open fields doctrine applied only to lands that could be viewed by the public.</p>
</footnote>
<footnote label="4">
<p id="b235-6"> The court also discredited other information, supplied by a confidential informant, upon which the police had based their warrant application.</p>
</footnote>
<footnote label="5">
<p id="b235-8"> Respondent contends that the decision below rests upon adequate and independent state-law grounds. We do not read that decision, however, as excluding the evidence because the search violated the State Constitution. The Maine Supreme Judicial Court referred only to the Fourth Amendment of the Federal Constitution and purported to apply the <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>test; the prior state cases that the court cited also construed the Federal Constitution. In any case, the Maine Supreme Judicial Court did not articulate an independent state ground with the clarity required by <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983).</p>
<p id="b235-9">Contrary to respondent’s assertion, we do not review here the state courts’ finding as a matter of “fact” that the area searched was not an “open field. ” Rather, the question before us is the appropriate legal standard for determining whether search of that area without a warrant was lawful under the Federal Constitution.</p>
<p id="b235-10">The conflict between the two cases that we review here is illustrative of the confusion the open fields doctrine has generated among the state and <page-number citation-index="1" label="176">*176</page-number>federal courts. Compare, <em>e. g., State </em>v. <em>Byers, </em><span class="citation" data-id="1852754"><a href="/opinion/1852754/state-v-byers/" aria-description="Citation for case: State v. Byers">359 So. 2d 84</a></span> (La. 1978) (refusing to apply open fields doctrine); <em>State </em>v. <em>Brady, </em><span class="citation" data-id="1092690"><a href="/opinion/1092690/state-v-brady/" aria-description="Citation for case: State v. Brady">406 So. 2d 1098</a></span> (Fla. 1981) (same), with <em>United States </em>v. <em>Lace, </em><span class="citation" data-id="9468813"><a href="/opinion/398901/united-states-v-david-t-lace-roger-r-ducharme-gary-d-butts-patricia/#50" aria-description="Citation for case: United States v. David T. Lace, Roger R. Ducharme, Gary...">669 F. 2d 46, 50-51</a></span> (CA2 1982); <em>United States </em>v. <em>Freie, </em><span class="citation" data-id="8900337"><a href="/opinion/8912486/united-states-v-freie/" aria-description="Citation for case: United States v. Freie">545 F. 2d 1217</a></span> (CA9 1976); <em>United States </em>v. <em>Brown, </em><span class="citation" data-id="308561"><a href="/opinion/308561/united-states-v-larry-joseph-brown/#954" aria-description="Citation for case: United States v. Larry Joseph Brown">473 F. 2d 952, 954</a></span> (CA5 1973); <em>Atwell </em>v. <em>United States, </em><span class="citation" data-id="285923"><a href="/opinion/285923/james-d-atwell-and-melvin-edmon-surrett-v-united-states/#138" aria-description="Citation for case: James D. Atwell and Melvin Edmon Surrett v. United States">414 F. 2d 136, 138</a></span> (CA5 1969).</p>
</footnote>
<footnote label="6">
<p id="b236-10"> The dissent offers no basis for its suggestion that <em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">Hester</a></span> </em>rests upon some narrow, unarticulated principle rather than upon the reasoning enunciated by the Court’s opinion in that case. Nor have subsequent cases discredited Hester*s reasoning. This Court frequently has relied on the explicit language of the Fourth Amendment as delineating the scope of its affirmative protections. See, <em>e. g., Robbins </em>v. <em>California, </em><span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#426" aria-description="Citation for case: Robbins v. California">453 U. S. 420, 426</a></span> (1981) (opinion of Stewart, J.); <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#589" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 589-590</a></span> (1980); <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#178" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 178-180</a></span> (1969). As these cases, decided after <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>indicate, <em>Katz’ </em>“reasonable expectation of privacy” standard did not sever Fourth Amendment doctrine from the Amendment’s language. <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>itself construed the Amendment’s protection of the person against unreasonable searches to encompass electronic eavesdropping of telephone conversations sought to be kept private; and <em>Katz’ </em>fundamental recognition that “the Fourth Amendment protects people — and not simply ‘areas’ — against unreasonable searches and seizures,” see <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U. S., at 353</a></span>, is faithful to the Amendment’s language. As <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>demonstrates, the Court fairly may respect the constraints of the Constitution’s language without wedding itself to an unreasoning literalism. In contrast, the dissent’s approach would ignore the language of the Constitution itself as well as overturn this Court’s governing precedent.</p>
</footnote>
<footnote label="7">
<p id="b237-6"> The Framers would have understood the term “effects” to be limited to personal, rather than real, property. See generally <em>Doe </em>v. <em>Dring, 2 M. &amp; </em>S. 448, 454, 105 Eng. Rep. 447, 449 (K. B. 1814) (discussing prior cases); 2 W. Blackstone, Commentaries *16, *384-*385.</p>
</footnote>
<footnote label="8">
<p id="b238-6"> The Fourth Amendment’s protection of offices and commercial buildings, in which there may be legitimate expectations of privacy, is also based upon societal expectations that have deep roots in the history of the Amendment. See <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#311" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 311</a></span> (1978); <em>G. M. Leasing Corp. </em>v. <em>United States, </em><span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#366" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 366</a></span> (1977).</p>
</footnote>
<footnote label="9">
<p id="b239-5"> Tr. of Oral Arg. 14-15, 58. See, <em>e. g., United States </em>v. <em>Allen, </em><span class="citation" data-id="8915013"><a href="/opinion/8925485/united-states-v-allen/#1380" aria-description="Citation for case: United States v. Allen">675 F. 2d 1373, 1380-1381</a></span> (CA9 1980); <em>United States </em>v. <em>DeBacker, </em><span class="citation" data-id="1557741"><a href="/opinion/1557741/united-states-v-debacker/#1081" aria-description="Citation for case: United States v. DeBacker">493 F. Supp. 1078, 1081</a></span> (WD Mich. 1980). In practical terms, petitioner Oliver’s and respondent Thornton’s analysis merely would require law enforcement officers, in most situations, to use aerial surveillance to gather the information necessary to obtain a warrant or to justify warrantless entry onto the property. It is not easy to see how such a requirement would advance legitimate privacy interests.</p>
</footnote>
<footnote label="10">
<p id="b239-6"> The dissent conceives of open fields as bustling with private activity as diverse as lovers’ trysts and worship services. <em>Post, </em>at 191-193. But in most instances police will disturb no one when they enter upon open fields. These fields, by their very character as open and unoccupied, are unlikely to provide the setting for activities whose privacy is sought to be protected by the Fourth Amendment. One need think only of the vast expanse of some western ranches or of the undeveloped woods of the Northwest to see the unreality of the dissent’s conception. Further, the Fourth Amendment provides ample protection to activities in the open fields that might implicate an individual’s privacy. An individual who enters a place defined to be “public” for Fourth Amendment analysis does not lose all claims to privacy or personal security. Cf. <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#766" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 766-767</a></span> (1979) (Burger, C. J., concurring in judgment). For example, the Fourth Amendment’s protections against unreasonable arrest or unreasonable seizure of effects upon the person remain fully applicable. See, <em>e. g., United States </em>v. <em>Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976).</p>
</footnote>
<footnote label="11">
<p id="b240-5"> Neither petitioner Oliver nor respondent Thornton has contended that the property searched was within the curtilage. Nor is it necessary in these cases to consider the scope of the curtilage exception to the open fields doctrine or the degree of Fourth Amendment protection afforded the curtilage, as opposed to the home itself. It is clear, however, that the term “open fields” may include any unoccupied or undeveloped area outside of the curtilage. An open field need be neither “open” nor a “field” as those terms are used in common speech. For example, contrary to respondent Thornton's suggestion, Tr. of Oral Arg. 21-22, a thickly wooded area nonetheless may be an open field as that term is used in construing the Fourth Amendment. See, <em>e. g., United States </em>v. <em>Pruitt, </em><span class="citation" data-id="304813"><a href="/opinion/304813/united-states-v-harry-william-pruitt/" aria-description="Citation for case: United States v. Harry William Pruitt">464 F. 2d 494</a></span> (CA9 1972); <em>Bedell </em>v. <em>State, </em><span class="citation" data-id="9642483"><a href="/opinion/1503690/bedell-v-state/" aria-description="Citation for case: Bedell v. State">257 Ark. 895</a></span>, <span class="citation" data-id="9642483"><a href="/opinion/1503690/bedell-v-state/" aria-description="Citation for case: Bedell v. State">521 S. W. 2d 200</a></span> (1975).</p>
</footnote>
<footnote label="12">
<p id="b242-7"> The clarity of the open fields doctrine that we reaffirm today is not sacrificed, as the dissent suggests, by our recognition that the curtilage remains within the protections of the Fourth Amendment. Most of the many millions of acres that are “open fields” are not close to any structure and so not arguably within the curtilage. And, for most homes, the boundaries of the curtilage will be clearly marked; and the conception defining the curtilage — as the area around the home to which the activity of home life extends — is a familiar one easily understood from our daily experience. The occasional difficulties that courts might have in applying this, like other, legal concepts, do not argue for the unprecedented expansion of the Fourth Amendment advocated by the dissent.</p>
</footnote>
<footnote label="13">
<p id="b242-8"> Certainly the Framers did not intend that the Fourth Amendment should shelter criminal activity wherever persons with criminal intent choose to erect barriers and post “No Trespassing” signs.</p>
</footnote>
<footnote label="14">
<p id="b243-7"> As noted above, the common-law conception of the “curtilage” has served this function.</p>
</footnote>
<footnote label="15">
<p id="b243-8"> The law of trespass recognizes the interest in possession and control of one’s property and for that reason permits exclusion of unwanted intruders. But it does not follow that the right to exclude conferred by trespass law embodies a privacy interest also protected by the Fourth Amendment. To the contrary, the common law of trespass furthers a range of interests that have nothing to do with privacy and that would not be served by applying the strictures of trespass law to public officers. Criminal laws against trespass are prophylactic: they protect against intruders who poach, steal livestock and crops, or vandalize property. And the civil action of trespass serves the important function of authorizing an owner to defeat claims of prescription by asserting his own title. See, <em>e. g., </em><page-number citation-index="1" label="184">*184</page-number>0. Holmes, The Common Law 98-100, 244-246 (1881). In any event, unlicensed use of property by others is presumptively unjustified, as anyone who wishes to use the property is free to bargain for the right to do so with the property owner, cf. R. Posner, Economic Analysis of Law 10-13, 21 (1973). For these reasons, the law of trespass confers protections from intrusion by others far broader than those required by Fourth Amendment interests.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Owen v. City of Independence.md  (`case`, 5 assertions)

### content_page

```
---
title: Owen v. City of Independence
type: case
citation: "445 U.S. 622 (1980)"
parallel_cite: "100 S. Ct. 1398; 63 L. Ed. 2d 673"
neutral_cite: 1980 U.S. LEXIS 14
court: U.S.
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-04-16
docket: 78-1779
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
  opinion_url: "https://www.courtlistener.com/opinion/110236/owen-v-city-of-independence/"
  cluster_id: 110236
  opinion_id: null
  identity_checked: true
lake:
  record_id: Owen v. City of Independence
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Anchor
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Monell v. Department of Social Services]]"
tags:
  - case
  - section-1983
  - municipal-liability
  - qualified-immunity
  - good-faith
  - monell
holding: "A municipality has no qualified immunity from § 1983 liability based on the good faith of its officers; it may not assert that its officials acted in good faith as a defense to liability for a constitutional deprivation."
aliases:
  - Owen v. City of Independence
  - "Owen v. City of Independence (1980)"
---

# Owen v. City of Independence

*445 U.S. 622 (1980)* (No. 78-1779) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 110236 → combined opinion 110236 (Brennan, J.; 445 U.S. 622, decided Apr. 16, 1980). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*639` follows the quoted sentence, placing it at 638). S9 promotes. -->

## Background
George Owen, the police chief of Independence, Missouri, was discharged without a hearing following a City Council investigation, amid public statements impugning his conduct. He sued the City under 42 U.S.C. § 1983, alleging that the manner of his dismissal deprived him of a liberty interest — a chance to clear his name — without due process. [[Reading and Citing Cases#on-remand|On remand]] after *[[Monell v. Department of Social Services|Monell]]*, the Court of Appeals held the City could invoke a [[Qualified Immunity|qualified immunity]] resting on the good faith of its officials. The Supreme Court granted [[Reading and Citing Cases#certiorari-cert|certiorari]].

## Issue
Whether a municipality sued under § 1983 may assert a [[Qualified Immunity|qualified immunity]], based on the good faith of its officers, as a defense to liability.

## Rule
Finding no common-law tradition of immunity for municipal corporations and no policy in § 1983 to support one, the Court held: "We hold, therefore, that the municipality may not assert the good faith of its officers or agents as a defense to liability under § 1983." — 445 U.S. at 638. ^pin-638

## Application
The individual immunities the Court has recognized under § 1983 were well established at common law when the statute was enacted; municipal immunity was not. And § 1983's purposes — compensating those whose constitutional rights are violated and spreading the loss across the community that benefits from government — are best served by holding the municipality answerable regardless of its officials' subjective good faith. A city therefore cannot escape § 1983 damages by showing that its agents acted in the honest belief that their conduct was lawful.

## Conclusion
The judgment was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]]. Brennan, J., delivered the opinion of the Court (5–4); Powell, J. (joined by Burger, C.J., and Stewart and Rehnquist, JJ.), dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Owen* establishes the sharp asymmetry in § 1983 immunity law: **individual** officers enjoy [[Qualified Immunity|qualified immunity]], but a **municipality does not** — good faith is no defense for the city. Teach it with *[[Monell v. Department of Social Services|Monell]]*: municipal liability requires a "policy or custom," but where that predicate is met, the city cannot fall back on the good faith of its officers.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Anchor*

## Sources
- [*Owen v. City of Independence*, 445 U.S. 622 (1980)](https://www.courtlistener.com/opinion/110236/owen-v-city-of-independence/) — pinpoint: 638 (Brennan, J., for the Court; the CL opinion text places the reporter star `*639` immediately after the quoted holding, fixing it on 638). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "382e233980cb5f10", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "445 U.S. 622 (1980)", "court": "U.S.", "neutral_cite": "1980 U.S. LEXIS 14", "official_citation_present": true, "parallel_cite": "100 S. Ct. 1398; 63 L. Ed. 2d 673", "title": "Owen v. City of Independence", "year": "1980"}}
{"assertion_id": "29e725685477505e", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Anchor", "title": "Owen v. City of Independence"}}
{"assertion_id": "8b7b6387ece64e0b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A municipality has no qualified immunity from § 1983 liability based on the good faith of its officers; it may not assert that its officials acted in good faith as a defense to liability for a constitutional deprivation.", "title": "Owen v. City of Independence"}}
{"assertion_id": "12d8f1dc9ee0be45", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Owen v. City of Independence", "varies_by_point": "false"}}
{"assertion_id": "8e54c4ae08b0b685", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Owen v. City of Independence"}}
```

### lake record — Owen v. City of Independence

```json
{
  "schema_version": "s2.v1",
  "record_id": "Owen v. City of Independence",
  "status": "under_review",
  "identity": {
    "case_name": "Owen v. City of Independence",
    "case_name_short": "Owen",
    "case_name_full": "OWEN v. CITY OF INDEPENDENCE, MISSOURI, Et Al.",
    "input_case_name": "Owen v. City of Independence",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-04-16",
    "year": 1980,
    "docket": "78-1779",
    "cluster_id": 110236,
    "lead_opinion_id": 9427858,
    "sibling_ids": [],
    "absolute_url": "/opinion/110236/owen-v-city-of-independence/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "445 U.S. 622",
      "volume": "445",
      "reporter": "U.S.",
      "page": "622",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 1398",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1398",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "63 L. Ed. 2d 673",
        "volume": "63",
        "reporter": "L. Ed. 2d",
        "page": "673",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 14",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "14",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "445 U.S. 622",
        "volume": "445",
        "reporter": "U.S.",
        "page": "622",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 1398",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1398",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "63 L. Ed. 2d 673",
        "volume": "63",
        "reporter": "L. Ed. 2d",
        "page": "673",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 14",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "14",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "445 U.S. 622",
    "official_selection": {
      "court_class": "scotus",
      "selected": "445 U.S. 622",
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
    "date_created": "2026-07-07T13:27:14Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:27:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:27:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:27:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:27:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "owen-v-city-of-independence--110236",
      "to_record_id": "Owen v. City of Independence",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Owen v. City of Independence

```
<opinion type="majority">
<author id="b684-6">Mr. Justice Brennan</author>
<p id="Anq">delivered the opinion of the Court.</p>
<p id="b684-7"><em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span> (1978), overruled <em>Monroe </em>v. <em>Pape, </em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span> (1961), insofar as <em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span> </em>held that local governments were not among the “persons” to whom 42 U. S. C. 11983 applies and were therefore wholly immune from suit under the statute.<footnotemark>1</footnotemark> <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>reserved decision, however, on the question whether local governments, although not entitled to an absolute immunity, should be afforded some form of official immunity in 1 1983 suits. <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#701" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 701</a></span>. In this action brought by petitioner in the District Court for the Western District of Missouri, the Court of Appeals for the Eighth Circuit held that respondent city of Independence, Mo., “is entitled to qualified immunity from liability” based on the good faith <page-number citation-index="1" label="625">*625</page-number>of its officials: “We extend the limited immunity the district court applied to the individual defendants to cover the City as well, because its officials acted in good faith and without malice.” <span class="citation" data-id="8908383"><a href="/opinion/8919777/owen-v-city-of-independence-missouri/#337" aria-description="Citation for case: Owen v. City of Independence, Missouri">589 F. 2d 335, 337-338</a></span> (1978). We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./444/822/">444 U. S. 822</a></span> (1979). We reverse.</p>
<p id="b685-5">I</p>
<p id="b685-6">The events giving rise to this suit are detailed in the District Court’s findings of fact, <span class="citation" data-id="1770095"><a href="/opinion/1770095/owen-v-city-of-independence-mo/" aria-description="Citation for case: Owen v. City of Independence, Mo.">421 F. Supp. 1110</a></span> (1976). On February 20, 1967, Robert L. Broucek, then City Manager of respondent city of Independence, Mo,, appointed petitioner George D. Owen to an indefinite term as Chief of Police.<footnotemark>2</footnotemark> In 1972, Owen and a new City Manager, Lyle W. Alberg, engaged in a dispute over petitioner’s administration of the Police Department’s property room. In March of that year, a handgun, which the records of the Department’s property room stated had been destroyed, turned up in Kansas City in the possession of a felon. This discovery prompted Al-berg to initiate an investigation of the management of the property room. Although the probe was initially directed by petitioner, Alberg soon transferred responsibility for the investigation to the city’s Department of Law, instructing the City Counselor to supervise its conduct and to inform him directly of its findings.</p>
<p id="b685-7">Sometime in early April 1972, Alberg received a written report on the investigation’s progress, along with copies of confidential witness statements. Although the City Auditor found that the Police Department’s records were insufficient to permit an adequate accounting of the goods contained in the property room, the City Counselor concluded that there was no evidence of any criminal acts or of any violation of <page-number citation-index="1" label="626">*626</page-number>state or municipal law in the administration of the property-room. Alberg discussed the results of the investigation at an informal meeting with several City Council members and advised them that he would take action at an appropriate time to correct any problems in the administration of the Police Department.</p>
<p id="b686-5">On April 10, Alberg asked petitioner to resign as Chief of Police and to accept another position within the Department, citing dissatisfaction with the manner in which petitioner had managed the Department, particularly his inadequate supervision of the property room. Alberg warned that if petitioner refused to take another position in the Department his employment would be terminated, to which petitioner responded that he did not intend to resign.</p>
<p id="b686-6">On April 13, Alberg issued a public statement addressed to the Mayor and the City Council concerning the results of the investigation. After referring to “discrepancies” found in the administration, handling, and security of public property, the release concluded that “[t]here appears to be no evidence to substantiate any allegations of a criminal nature” and offered assurances that “[sjteps have been initiated on an administrative level to correct these discrepancies.” <span class="citation" data-id="1770095"><a href="/opinion/1770095/owen-v-city-of-independence-mo/#1115" aria-description="Citation for case: Owen v. City of Independence, Mo."><em>Id., </em>at 1115</a></span>. Although Alberg apparently had decided by this time to replace petitioner as Police Chief, he took no formal action to that end and left for a brief vacation without informing the City Council of his decision.<footnotemark>3</footnotemark></p>
<p id="b686-7">While Alberg was away on the weekend of April 15 and 16, two developments occurred. Petitioner, having consulted with counsel, sent Alberg a letter demanding written notice of the charges against him and a public hearing with a reason<page-number citation-index="1" label="627">*627</page-number>able opportunity to respond to those charges.<footnotemark>4</footnotemark> At approximately the same time, City Councilman Paul L. Roberts asked for a copy of the investigative report on the Police Department property room. Although petitioner’s appeal received no immediate response, the Acting City Manager complied with Roberts’ request and supplied him with the audit report and witness statements.</p>
<p id="b687-5">On the evening of April 17, 1972, the City Council held its regularly scheduled meeting. After completion of the planned agenda, Councilman Roberts read a statement he had prepared on the investigation.<footnotemark>5</footnotemark> Among other allegations, <page-number citation-index="1" label="628">*628</page-number>Roberts charged that petitioner had misappropriated Police Department property for his own use, that narcotics and money had “mysteriously disappeared” from his office, that traffic tickets had been manipulated, that high ranking police officials had made “inappropriate” requests affecting the police court, and that “things have occurred causing the unusual release of felons.” At the close of his statement, Roberts moved that the investigative reports be released to the news media and turned over to the prosecutor for presentation to the grand jury, and that the City Manager “take all direct <page-number citation-index="1" label="629">*629</page-number>and appropriate action” against those persons “involved in illegal, wrongful, or gross inefficient activities brought out in the investigative reports.” After some discussion, the City Council passed Roberts’ motion with no dissents and one abstention.<footnotemark>6</footnotemark></p>
<p id="b689-5">City Manager Alberg discharged petitioner the very next day. Petitioner was not given any reason for his dismissal; he received only a written notice stating that his employment as Chief of Police was “[t]erminated under the provisions of Section 3.3(1) of the City Charter.”<footnotemark>7</footnotemark> Petitioner’s earlier demand for a specification of charges and a public hearing was ignored, and a subsequent request by his attorney for an appeal of the discharge decision was denied by the city on the grounds that “there is no appellate procedure or forum provided by the Charter or ordinances of the City of Independence, Missouri, relating to the dismissal of Mr. Owen.” App. 26-27.</p>
<p id="b689-6">The local press gave prominent coverage both to the City Council’s action and petitioner’s dismissal, linking the discharge to the investigation.<footnotemark>8</footnotemark> As instructed by the City Council, Alberg referred the investigative reports and witness statements to the Prosecuting Attorney of Jackson County, Mo., <page-number citation-index="1" label="630">*630</page-number>for consideration by a grand jury. The results of the audit and investigation were never released to the public, however. The grand jury subsequently returned a “no true bill,” and no further action was taken by either the City Council or City Manager Alberg.</p>
<p id="b690-5">II</p>
<p id="b690-6">Petitioner named the city of Independence, City Manager Alberg, and the present members of the City Council in their official capacities as defendants in this suit.<footnotemark>9</footnotemark> Alleging that he was discharged without notice of reasons and without a hearing in violation of his constitutional rights to procedural and substantive due process, petitioner sought declaratory and injunctive relief, including a hearing on his discharge, back-pay from the date of discharge, and attorney’s fees. The District Court, after a bench trial, entered judgment for respondents. <span class="citation" data-id="1770095"><a href="/opinion/1770095/owen-v-city-of-independence-mo/" aria-description="Citation for case: Owen v. City of Independence, Mo.">421 F. Supp. 1110</a></span> (1976).<footnotemark>10</footnotemark></p>
<p id="b691-4"><page-number citation-index="1" label="631">*631</page-number>The Court of Appeals initially reversed the District Court. <span class="citation multiple-matches"><a href="/c/F.%202d/560/925/">560 F. 2d 925</a></span> (1977).<footnotemark>11</footnotemark> Although it agreed with the District Court that under Missouri law petitioner possessed no property interest in continued employment as Police Chief, the Court of Appeals concluded that the city’s allegedly false public accusations had blackened petitioner’s name and reputation, thus depriving him of liberty without due process of law. That the stigmatizing charges did not come from the City Manager and were not included in the official discharge notice was, in the court’s view, immaterial. What was un-<page-number citation-index="1" label="632">*632</page-number>portant, the court explained, was that "the official actions of the city council released charges against [petitioner] contemporaneous and, in the eyes of the public, connected with that discharge.” <em>Id., </em>at 937.<footnotemark>12</footnotemark></p>
<p id="b692-5">Respondents petitioned for review of the Court of Appeals’ decision. Certiorari was granted, and the case was remanded for further consideration in light of our supervening decision in <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span> (1978). <span class="citation" data-id="9011579"><a href="/opinion/9018430/city-of-independence-v-owen/" aria-description="Citation for case: City of Independence v. Owen">438 U. S. 902</a></span> (1978). The Court of Ap<page-number citation-index="1" label="633">*633</page-number>peals on the remand reaffirmed its original determination that the city had violated petitioner’s rights under the Fourteenth Amendment, but held that all respondents, including the city, were entitled to qualified immunity from liability. <span class="citation" data-id="8908383"><a href="/opinion/8919777/owen-v-city-of-independence-missouri/" aria-description="Citation for case: Owen v. City of Independence, Missouri">589 F. 2d 335</a></span> (1978).</p>
<p id="b693-5"><em>Monell </em>held that <em>“a </em>local government may not be sued under § 1983 for an injury inflicted solely by its employees or agents. Instead, it is when execution of a government’s policy or custom, whether made by its lawmakers or by those whose edicts or acts may fairly be said to represent official policy, inflicts the injury that the government as an entity is responsible under § 1983.” <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 694</a></span>. The Court of Appeals held in the instant ease that the municipality’s official policy was responsible for the deprivation of petitioner’s constitutional rights: “[T]he stigma attached to [petitioner] in connection with his discharge was caused by the official conduct of the City’s lawmakers, or by those whose acts may fairly be said to represent official policy. Such conduct amounted to official policy causing the infringement of [petitioner’s] constitutional rights, in violation of section 1983.” <span class="citation" data-id="8908383"><a href="/opinion/8919777/owen-v-city-of-independence-missouri/#337" aria-description="Citation for case: Owen v. City of Independence, Missouri">589 F. 2d, at 337</a></span>.<footnotemark>13</footnotemark></p>
<p id="b694-4"><page-number citation-index="1" label="634">*634</page-number>Nevertheless, the Court of Appeals affirmed the judgment of the District Court denying petitioner any relief against the respondent city, stating:</p>
<blockquote id="b694-5">“The Supreme Court’s decisions in <em>Board of Regents </em>v. <em>Roth, </em><span class="citation" data-id="9425009"><a href="/opinion/108608/board-of-regents-of-state-colleges-v-roth/" aria-description="Citation for case: Board of Regents of State Colleges v. Roth">408 U. S. 564</a></span> . . . (1972), and <em>Perry </em>v. <em>Sindermann, </em><span class="citation" data-id="9425012"><a href="/opinion/108609/perry-v-sindermann/" aria-description="Citation for case: Perry v. Sindermann">408 U. S. 593</a></span> . . . (1972), crystallized the rule establishing the right to a name-clearing hearing for a government employee allegedly stigmatized in the course of his discharge. The Court decided those two cases two months after the discharge in the instant case. Thus, officials of the City of Independence could not have been aware of [petitioner’s] right to a name-clearing , hearing in connection with the discharge. The City of Independence should not be charged with predicting the future course of constitutional law. We extend the limited immunity the district court applied to the individual defendants to cover the City as well, because its officials acted in good faith and without malice. We hold the City not liable for actions it could not reasonably have known violated [petitioner’s] constitutional rights.” <em>Id., </em>at 338 (footnote and citations omitted).<footnotemark>14</footnotemark></blockquote>
<p id="b695-4"><page-number citation-index="1" label="635">*635</page-number>We turn now to the reasons for our disagreement with this holding.<footnotemark>15</footnotemark></p>
<p id="b695-5">Ill</p>
<p id="b695-6">Because the question of the scope of a municipality’s immunity from liability under § 1983 is essentially one of statutory construction, see <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#314" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308, 314, 316</a></span> (1975); <em>Tenney </em>v. <em>Brandhove, </em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#376" aria-description="Citation for case: Tenney v. Brandhove">341 U. S. 367, 376</a></span> (1951), the starting point in our analysis must be the language of the statute itself. <em>Andrus </em>v. <em>Allard, </em><span class="citation" data-id="110156"><a href="/opinion/110156/andrus-v-allard/#56" aria-description="Citation for case: Andrus v. Allard">444 U. S. 51, 56</a></span> (1979); <em>Blue Chip Stamps </em>v. <em>Manor Drug Stores, </em><span class="citation" data-id="9426100"><a href="/opinion/109267/blue-chip-stamps-v-manor-drug-stores/#756" aria-description="Citation for case: Blue Chip Stamps v. Manor Drug Stores">421 U. S. 723, 756</a></span> (1975) (Powell, J., concurring). By its terms, § 1983 “creates a species of tort liability that on its face admits of no immunities.” <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#417" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409, 417</a></span> (1976). Its language is absolute and unqualified; no mention is made of any privileges, immunities, or defenses that may be asserted. Bather, the Act imposes liability upon <em>“every person” </em>who, under color of state law or custom, “subjects, or causes to be subjected, any citizen of the United States ... to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws.”<footnotemark>16</footnotemark> And <em>Monell </em>held that these words were intended to encompass municipal corporations as well as natural “persons.”</p>
<p id="b695-7">Moreover, the congressional debates surrounding the passage of § 1 of the Civil Rights Act of 1871, <span class="citation no-link">17 Stat. 13</span> — the forerunner of § 1983 — confirm the expansive sweep of the stat<page-number citation-index="1" label="636">*636</page-number>utory language. Representative Shellabarger, the author and manager of the bill in the House, explained in his introductory remarks the breadth of construction that the Act was to receive:</p>
<blockquote id="b696-5">“I have a single remark to make in regard to the rule of interpretation of those provisions of the Constitution under which all the sections of the bill are framed. This act is remedial, and in aid of the preservation of human liberty and human rights. All statutes and constitutional provisions authorizing such statutes are liberally and beneficently construed. It would be most strange and, in civilized law, monstrous were this not the rule of interpretation. As has been again and again decided by your own Supreme Court of the United States, and everywhere else where there is wise judicial interpretation, the largest latitude consistent with the words employed is uniformly given in construing such statutes and constitutional provisions as are meant to protect and defend and give remedies for their wrongs to all the people.” Cong. Globe, 42d Cong., 1st Sess., App. 68 (1871) (hereinafter Globe App.).</blockquote>
<p id="b696-6">Similar views of the Act’s broad remedy for violations of federally protected rights were voiced by its supporters in both Houses of Congress. See <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#683" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 683-687</a></span>.<footnotemark>17</footnotemark></p>
<p id="b697-4"><page-number citation-index="1" label="637">*637</page-number>However, notwithstanding § 1983’s expansive language and the absence of any express incorporation of common-law immunities, we have, on several occasions, found that a tradition of immunity was so firmly rooted in the common law and was supported by such strong policy reasons that “Congress would have specifically so provided had it wished to abolish the doctrine.” <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#555" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547, 555</a></span> (1967). Thus in <em>Tenney </em>v. <em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">Brandhove, supra,</a></span> </em>after tracing the development of an absolute legislative privilege from its source in 16th-century England to its inclusion in the Federal and State Constitutions, we concluded that Congress “would [not] impinge on a tradition so well grounded in history and reason by covert inclusion in the general language” of § 1983. <span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#376" aria-description="Citation for case: Tenney v. Brandhove">341 U. S., at 376</a></span>.</p>
<p id="b697-5">Subsequent cases have required that we consider the personal liability of various other types of government officials. Noting that “[f]ew doctrines were more solidly established at common law than the immunity of judges from liability for damages for acts committed within their judicial jurisdiction,” <em>Pierson </em>v. <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#553" aria-description="Citation for case: Pierson v. Ray"><em>Ray, supra, </em>at 553-554</a></span>, held that the absolute immunity traditionally accorded judges was preserved under § 1983. In that same case, local police officers were held to enjoy a “good faith and probable cause” defense to § 1983 suits similar to that which existed in false arrest actions at common law. <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#555" aria-description="Citation for case: Pierson v. Ray">386 U. S., at 555-557</a></span>. Several more recent decisions have found immunities of varying scope appropriate for different state and local officials sued under § 1983. See <em>Procunier </em>v. <em>Navarette, </em><span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/" aria-description="Citation for case: Procunier v. Navarette">434 U. S. 555</a></span> (1978) (qualified im<page-number citation-index="1" label="638">*638</page-number>munity for prison officials and officers); <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409</a></span> (1976) (absolute immunity for prosecutors in initiating and presenting the State’s case); <em>O’Connor </em>v. <em>Donaldson, </em><span class="citation" data-id="9842006"><a href="/opinion/109303/oconnor-v-donaldson/" aria-description="Citation for case: O&#x27;Connor v. Donaldson">422 U. S. 563</a></span> (1975) (qualified immunity for superintendent of state hospital); <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308</a></span> (1975) (qualified immunity for local school board members) ; <em>Scheuer </em>v. <em>Rhodes, </em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232</a></span> (1974) (qualified “good-faith” immunity for state Governor and other executive officers for discretionary acts performed in the course of official conduct).</p>
<p id="b698-5">In each of these cases, our finding of § 1983 immunity “was predicated upon a considered inquiry into the immunity historically accorded the relevant official at common law and the interests behind it.” <em>Imbler </em>v. <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#421" aria-description="Citation for case: Imbler v. Pachtman"><em>Pachtman, supra, </em>at 421</a></span>. Where the immunity claimed by the defendant was well established at common law at the time § 1983 was enacted, and where its rationale was compatible with the purposes of the Civil Eights Act, we have construed the statute to incorporate that immunity. But there is no tradition of immunity for municipal corporations, and neither history nor policy supports a construction of § 1983 that would justify the qualified immunity accorded the city of Independence by the Court of Appeals. We hold, therefore, that the municipality may not assert the good faith of its officers or agents as a defense to liability under § 1983.<footnotemark>18</footnotemark></p>
<p id="b698-6">A</p>
<p id="b698-7">Since colonial times, a distinct feature of our Nation’s system of governance has been the conferral of political power upon public and municipal corporations for the management of matters of local concern. As <em>Monell </em>recounted, by 1871, <page-number citation-index="1" label="639">*639</page-number>municipalities — like private corporations — were treated as natural persons for virtually all purposes of constitutional and statutory analysis. In particular, they were routinely sued in both federal and state courts. See <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#687" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 687-688</a></span>. Cf. <em>Cowles </em>v. <em>Mercer County, </em><span class="citation" data-id="87989"><a href="/opinion/87989/cowles-v-mercer-county/" aria-description="Citation for case: Cowles v. Mercer County">7 Wall. 118</a></span> (1869). Local governmental units were regularly held to , answer in damages for a wide range of statutory and constitutional violations, as well as for common-law actions for breach of contract.<footnotemark>19</footnotemark> And although, as we discuss below,<footnotemark>20</footnotemark> a municipal<page-number citation-index="1" label="640">*640</page-number>ity was not subject to suit for all manner of tortious conduct, it is clear that at the time § 1983 was enacted, local governmental bodies did not enjoy the sort of “good-faith” qualified immunity extended to them by the Court of Appeals.</p>
<p id="b700-5">As a general rule, it was understood that a municipality’s tort liability in damages was identical to that of private corporations and individuals:</p>
<blockquote id="b700-6">“There is nothing in the character of a municipal corporation which entitles it to an immunity from liability for such malfeasances as private corporations or individuals would be liable for in a civil action. A municipal corporation is liable to the same extent as an individual for any act done by the express authority of the corporation, or of a branch of its government, empowered to act for it upon the subject to which the particular act relates, and for any act which, after it has been done, has been lawfully ratified by the corporation.” T. Shear-man &amp; A. Redfield, A Treatise on the Law of Negligence § 120, p. 139 (1869) (hereinafter Shearman &amp; Redfield).</blockquote>
<p id="b700-7">Accord, 2 Dillon § 764, at 875 (“But as respects <em>municipal corporations proper, </em>... it is, we think, universally considered, even in the absence of statute giving the action, that they are liable for acts of <em>misfeasance </em>positively injurious to individuals, done by their authorized agents or officers, in the course of the performance of corporate powers constitutionally conferred, or in the execution of corporate duties”) (emphasis in original). See 18 E. McQuillin, Municipal Corporations § 53.02 (3d rev. ed. 1977) (hereinafter McQuillin). Under this general theory of liability, a municipality was deemed responsible for any private losses generated through a wide variety of its operations and functions, from personal injuries due to its defective sewers, thoroughfares, and public utilities, to property damage caused by its trespasses and uncompensated takings.<footnotemark>21</footnotemark></p>
<p id="b701-4"><page-number citation-index="1" label="641">*641</page-number>Yet in the hundreds of cases from that era awarding damages against municipal governments for wrongs committed by them, one searches in vain for much mention of a qualified immunity based on the good faith of municipal officers. Indeed, where the issue was discussed at all, the courts had rejected the proposition that a municipality should be privileged where it reasonably believed its actions to be lawful. In the leading case of <em>Thayer </em>v. <em>Boston, </em><span class="citation" data-id="6407157"><a href="/opinion/6533444/thayer-v-city-of-boston/#515" aria-description="Citation for case: Thayer v. City of Boston">36 Mass. 511, 515-516</a></span> (1837), for example, Chief Justice Shaw explained:</p>
<blockquote id="b701-5">“There is a large class of cases, in which the rights of both the public and of individuals may be deeply involved, in which it cannot be known at the time the act is done, whether it is lawful or not. The event of a legal inquiry, in a court of justice, may show that it was unlawful. Still, if it was not known and understood to be! unlawful at the time, if it was an act done by the officers! having competent authority, either by express vote of \ the city government, or by the nature of the duties and ! functions with which they are charged, by their offices, to act upon the general subject matter, and especially if the j act was done with an honest view to obtain for the public j some lawful benefit or advantage, reason and justice ob- ¡ viously require that the city, in its corporate capacity, should be liable to make good the damage sustained by an individual, in consequence of the acts thus done.” ]</blockquote>
<p id="b701-6">The <em><span class="citation" data-id="6407157"><a href="/opinion/6533444/thayer-v-city-of-boston/" aria-description="Citation for case: Thayer v. City of Boston">Thayer</a></span> </em>principle was later reiterated by courts in several jurisdictions, and numerous decisions awarded damages against municipalities for violations expressly found to have been committed in good faith. See, <em>e. g., Town Council of Akron </em>v. <em>McComb, </em><span class="citation no-link">18 Ohio 229</span>, 230-231 (1849); <em>Horton </em>v. <em>Inhabitants of Ipswich, </em><span class="citation" data-id="6410190"><a href="/opinion/6536470/horton-v-inhabitants-of-ipswich/#489" aria-description="Citation for case: Horton v. Inhabitants of Ipswich">66 Mass. 488, 489, 492</a></span> (1853); <em>Elliot </em>v. <em>Concord, </em>27 N. H. 204 (1853); <em>Hurley </em>v. <em>Town of Texas, </em><span class="citation" data-id="6599597"><a href="/opinion/6718747/hurley-v-town-of-texas/#637" aria-description="Citation for case: Hurley v. Town of Texas">20 Wis. 634, 637-638</a></span> (1866); <em>Lee </em>v. <em>Village of Sandy Hill, </em><span class="citation" data-id="3597827"><a href="/opinion/3615537/lee-v-the-village-of-sandy-hill/#448" aria-description="Citation for case: Lee v. . the Village of Sandy Hill">40 N. Y. <page-number citation-index="1" label="642">*642</page-number>442, 448-451</a></span> (1869); <em>Billings </em>v. <em>Worcester, </em><span class="citation" data-id="6415781"><a href="/opinion/6542057/billings-v-city-of-worcester/#332" aria-description="Citation for case: Billings v. City of Worcester">102 Mass. 329, 332-333</a></span> (1869); <em>Squiers </em>v. <em>Village of Neenah, </em><span class="citation" data-id="6600295"><a href="/opinion/6719394/squiers-v-village-of-neenah/#593" aria-description="Citation for case: Squiers v. Village of Neenah">24 Wis. 588, 593</a></span> (1869); <em>Hawks </em>v. <em>Charlemont, </em><span class="citation" data-id="6416517"><a href="/opinion/6542791/hawks-v-inhabitants-of-charlemont/#417" aria-description="Citation for case: Hawks v. Inhabitants of Charlemont">107 Mass. 414, 417-418</a></span> (1871).<footnotemark>22</footnotemark></p>
<p id="b702-4">That municipal corporations were commonly held liable for damages in tort was also recognized by the 42d Congress. See <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#688" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 688</a></span>. For example, Senator Stevenson, in opposing the Sherman amendment’s creation of a municipal liability for the riotous acts of its inhabitants, stated the prevailing law: "Numberless cases are to be found where a statutory liability has been created against municipal corporations for injuries resulting from a neglect of corporate duty.” Cong. <page-number citation-index="1" label="643">*643</page-number>Globe, 42d Cong., 1st Sess., 762 (hereinafter Globe).<footnotemark>23</footnotemark> Nowhere in the debates, however, is there a suggestion that the common law excused a city from liability on account of the good faith of its authorized agents, much less an indication of a congressional intent to incorporate such an immunity into the Civil Rights Act.<footnotemark>24</footnotemark> The absence of any allusion to a municipal immunity assumes added significance in light of the objections raised by the opponents of § 1 of the Act that its unqualified language could be interpreted to abolish the traditional good-faith immunities enjoyed by legislators, judges, governors, sheriffs, and other public officers.<footnotemark>25</footnotemark> Had <page-number citation-index="1" label="644">*644</page-number>there been a similar common-law immunity for municipalities, the bill’s opponents doubtless would have raised the specter of its destruction, as well.</p>
<p id="b704-5">To be sure, there were two doctrines that afforded municipal corporations some measure of protection from tort liability. The first sought to distinguish betweeá a municipality’s “governmental” and “proprietary” functions; as to the former, the city was held immune, whereas in its exercise of the latter, the city was held to the same standards of liability as any private corporation. The second doctrine immunized a municipality for its “discretionary” or “legislative” activities, but not for those which were “ministerial” in nature. A brief examination of the application and the rationale underlying each of these doctrines demonstrates that Congress could not have intended them to limit a municipality’s liability under § 1983.</p>
<p id="b704-6">The governmental-proprietary distinction <footnotemark>26</footnotemark> owed its existence to the dual nature of the municipal corporation. On <page-number citation-index="1" label="645">*645</page-number>the one hand, the municipality was a corporate body, capable of performing the same “proprietary” functions as any private corporation, and liable for its torts in the same manner and to the same extent, as well. On the other hand, the municipality was an arm of the State, and when acting in that “governmental” or “public” capacity, it shared the immunity traditionally accorded the sovereign.<footnotemark>27</footnotemark> But the principle of sovereign immunity — itself a somewhat arid fountainhead for municipal immunity<footnotemark>28</footnotemark> — is necessarily nullified when the <page-number citation-index="1" label="646">*646</page-number>State expressly or impliedly allows itself, or its creation, to be sued. Municipalities were therefore liable not only for their “proprietary” acts, but also for those “governmental” functions as to which the State had withdrawn their immunity. And, by the end of the 19th century, courts regularly held that in imposing a specific duty on the municipality either in its charter or by statute, the State had impliedly withdrawn the city’s immunity from liability for the nonperformance or misperformance of its obligation. See, <em>e. g., Weightman </em>v. <em>The Corporation of Washington, </em><span class="citation" data-id="87436"><a href="/opinion/87436/weightman-v-corporation-of-washington/#50" aria-description="Citation for case: Weightman v. Corporation of Washington">1 Black 39, 50-52</a></span> (1862); <em>Providence </em>v. <em>Clapp, </em><span class="citation" data-id="86918"><a href="/opinion/86918/city-of-providence-v-clapp/#167" aria-description="Citation for case: City of Providence v. Clapp">17 How. 161, 167-169</a></span> (1855). See generally Shearman &amp; Redfield §§ 122-126; Note, Liability of Cities for the Negligence and Other Misconduct of their Officers and Agents, <span class="citation no-link">30 Am. St. Rep. 376</span>, 385 (1893). Thus, despite the nominal existence of an immunity for “governmental” functions, municipalities were found <page-number citation-index="1" label="647">*647</page-number>liable in damages in a multitude of cases involving such activities.</p>
<p id="b707-5">That the municipality’s common-law immunity for “governmental” functions derives from the principle of sovereign immunity also explains why that doctrine could not have served as the basis for the qualified privilege respondent city claims under § 1983. First, because, sovereign immunity insulates the municipality from unconsented suits altogether, the pres-enee or absence of good faith is simply irrelevant. The critical issue is whether injury occurred while the city was exercising- governmental, as opposed to pioprietary, powers or obligations — not whether its agents reasonably believed they were acting lawfully in so conducting themselves.<footnotemark>29</footnotemark> Morfundamentally, however, the municipality’s “governmental” immunity is obviously abrogated by the sovereign’s enacment of a statute making it amenable to suit. Section 1983 was just such a statute. By including municipalities within the class of “persons” subject to liability for violations of the Federal Constitution and laws, Congress — the supreme sovereign on matters of federal law<footnotemark>30</footnotemark> — abolished whatever ves<page-number citation-index="1" label="648">*648</page-number>tige of the State’s sovereign immunity the municipality possessed.</p>
<p id="b708-5">The second common-law distinction between municipal functions — that protecting the city from suits challenging “discretionary” decisions — was grounded not on the principle of sovereign immunity, but on a concern for separation of powers. A large part of the municipality’s responsibilities involved broad discretionary decisions on issues of public policy — decisions that affected large numbers of persons and called for a delicate balancing of competing considerations. For a court or jury, in the guise of a tort suit, to review the reasonableness of the city’s judgment on these matters would be an infringement upon the powers properly vested in a coordinate and coequal branch of government. See <em>Johnson </em>v. <em>State, </em><span class="citation multiple-matches"><a href="/c/Cal.%202d/69/782/">69 Cal. 2d 782</a></span>, 794, n. 8, <span class="citation" data-id="9574558"><a href="/opinion/1312748/johnson-v-state-of-california/#361" aria-description="Citation for case: Johnson v. State of California">447 P. 2d 352, 361, n. 8</a></span> (1968) (en banc) (“Immunity for ‘discretionary’ activities serves no purpose except to assure that courts refuse to pass judgment on policy decisions in the province of coordinate branches of government”). In order to ensure against any invasion into the legitimate sphere of the municipality’s policymaking processes, courts therefore refused to entertain suits against the city “either for the non-exercise of, or for the manner in which in good faith it exercises, <em>discretionary powers </em>of a public or legislative character.” 2 Dillon § 753, at 862.<footnotemark>31</footnotemark></p>
<p id="b708-6">Although many, if not all, of a municipality’s activities would seem to involve at least some measure of discretion, the influence of this doctrine on the city’s liability was not as significant as might be expected. For just as the courts <page-number citation-index="1" label="649">*649</page-number>implied an exception to the municipality’s immunity for its “governmental” functions, here, too, a distinction was made that had the effect of subjecting the city to liability for much of its tortious conduct. While the city retained its immunity for decisions as to whether the public interest required acting in one manner or another, once any particular decision was made, the city was fully liable for any injuries incurred in the execution of its judgment. See, <em>e. g., Hill </em>v. <em>Boston, </em><span class="citation" data-id="6418891"><a href="/opinion/6545160/hill-v-city-of-boston/#358" aria-description="Citation for case: Hill v. City of Boston">122 Mass. 344, 358-359</a></span> (1877) (dicta) (municipality would be immune from liability for damages resulting from its decision where to construct sewers, since that involved a discretionary judgment as to the general public interest; but city would be liable for neglect in the construction or repair of any particular sewer, as such activity is ministerial in nature). See generally C. Rhyne, Municipal Law § 30.4, pp. 736-737 (1957); Williams § 7. Thus municipalities remained liable in damages for a broad range of conduct implementing their disere-/ tionary decisions.</p>
<p id="b709-5">Once again, an understanding of the rationale underlying the common-law immunity for “discretionary” functions explains why that doctrine cannot serve as the foundation for a good-faith immunity under § 1983. That common-law doctrine merely prevented courts from substituting their own judgment on matters within the lawful discretion of the municipality. But a municipality has no “discretion” to violate the Federal Constitution; its dictates are absolute and imperative. And when a court passes judgment on the municipality’s conduct in a § 1983 action, it does not seek to second-guess the “reasonableness” of the city’s decision nor to interfere with the local government’s resolution of competing policy considerations. Rather, it looks only to whether the municipality has conformed to the requirements of the Federal Constitution and statutes. As was stated in <em>Sterling </em>v. <em>Constantin, </em><span class="citation" data-id="101991"><a href="/opinion/101991/sterling-v-constantin/#398" aria-description="Citation for case: Sterling v. Constantin">287 U. S. 378, 398</a></span> (1932): “When there is a substantial showing that the exertion of state power has <page-number citation-index="1" label="650">*650</page-number>overridden private rights secured by that Constitution, the subject is necessarily one for judicial inquiry in an appropriate proceeding directed against the individuals charged with the transgression.”</p>
<p id="b710-5">In sum, we can discern no “tradition so well grounded in history and-reason” that would warrant the conclusion that in enacting § 1 of the Civil Rights Act, the 42d Congress <em>sub silentio </em>extended to municipalities a qualified immunity based on the good faith of their officers. Absent any clearer indication that Congress intended so to limit the reach of a statute expressly designed to provide a “broad remedy for violations of federally protected civil rights,” <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#685" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 685</a></span>, we are unwilling to suppose that injuries occasioned by a municipality’s unconstitutional conduct were not also meant to be fully redressable through its sweep.<footnotemark>32</footnotemark></p>
<p id="b710-6">B</p>
<p id="b710-7">Our rejection of a construction of § 1983 that would accord municipalities a qualified immunity for their good-faith constitutional violations is compelled both by the legislative purpose in enacting the statute and by considerations of public policy. The central aim of the Civil Rights Act was to provide protection to those persons wronged by the “ ‘[mjisuse of power, possessed by virtue of state law and made possible only because the wrongdoer is clothed with the authority of state law.’ ” <em>Monroe </em>v. <em>Pape, </em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 184</a></span> (quoting <em>United States </em>v. <em>Classic, </em><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/#326" aria-description="Citation for case: United States v. Classic">313 U. S. 299, 326</a></span> (1941)). By creating an express federal remedy, Congress sought to “enforce provisions of the Fourteenth Amendment against those <page-number citation-index="1" label="651">*651</page-number>who carry a badge of authority of a State and represent it in some capacity, whether they act in accordance with their authority or misuse it.” <em>Monroe </em>v. <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#172" aria-description="Citation for case: Monroe v. Pape"><em>Pape, supra, </em>at 172</a></span>.</p>
<p id="b711-5">How “uniquely amiss” it would be, therefore, if the government itself — “the social organ to which all in our society look for the promotion of liberty, justice, fair and equal treatment, and the setting of worthy norms and goals for social conduct” — were permitted to disavow liability for the injury it has begotten. See <em>Adickes </em>v. <em>Kress &amp; Co., </em><span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#190" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U. S. 144, 190</a></span> (1970) (opinion of Brennan, J.). A damages remedy against the offending' party is a vital component of any scheme for vindicating cherished constitutional guarantees, and the importance of assuring its efficacy is only accentuated when the wrongdoer is the institution that has been established to protect the very rights it has transgressed: Yet owing to the qualified immunity enjoyed by most government officials, see <em>Scheuer </em>v. <em>Rhodes, </em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232</a></span> (1974), many victims of municipal malfeasance would be left remediless if the city were also allowed to assert a good-faith defense. Unless countervailing considerations counsel otherwise, the injustice of such a result should not be tolerated.<footnotemark>33</footnotemark></p>
<p id="b711-6">Moreover, § 1983 was intended not only to provide compensation to the victims of past abuses, but to serve as a deterrent against future constitutional deprivations, as well. See <em>Robertson </em>v. <em>Wegmann, </em><span class="citation" data-id="9427228"><a href="/opinion/109877/robertson-v-wegmann/#590" aria-description="Citation for case: Robertson v. Wegmann">436 U. S. 584, 590-591</a></span> (1978); <em>Carey </em>v. <em>Piphus, </em><span class="citation" data-id="109815"><a href="/opinion/109815/carey-v-piphus/#256" aria-description="Citation for case: Carey v. Piphus">435 U. S. 247, 256-257</a></span> (1978). The knowledge that a municipality will be liable for all of its injurious conduct, whether committed in good faith or not, should create <page-number citation-index="1" label="652">*652</page-number>an incentive for officials who may harbor doubts about the lawfulness of their intended actions to err on the side of protecting citizens’ constitutional rights.<footnotemark>34</footnotemark> Furthermore, the threat that damages might be levied against the city may encourage those in a policymaking position to institute internal rules and programs designed to minimize the likelihood of unintentional infringements on constitutional rights.<footnotemark>35</footnotemark> Such procedures are particularly beneficial in preventing those “systemic” injuries that result not so much from the conduct of any single individual, but from the interactive behavior of several government officials, each of whom may be acting in good faith. Cf. Note, Developments in the Law: Section 1983 and Federalism, <span class="citation no-link">90 Harv. L. Rev. 1133</span>, 1218-1219 (1977).<footnotemark>36</footnotemark></p>
<p id="b712-5">Our previous decisions conferring qualified immunities on various government officials, see <em>supra, </em>at 637-638, are not to <page-number citation-index="1" label="653">*653</page-number>be read as derogating the significance of the societal interest in compensating the innocent victims of governmental misconduct. Rather, in each case we concluded that overriding considerations of public policy nonetheless demanded that the official be given a measure of protection from personal liability. The concerns that justified those decisions, however, are less compelling, if not wholly inapplicable, when the liability of the municipal entity is at issue.<footnotemark>37</footnotemark></p>
<p id="b714-4"><page-number citation-index="1" label="654">*654</page-number>In <em>Scheuer </em>v. <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#240" aria-description="Citation for case: Scheuer v. Rhodes"><em>Rhodes, supra, </em>at 240</a></span>, The Chief Justice identified the two “mutually dependent rationales” on which the doctrine of official immunity rested:</p>
<blockquote id="b714-5">“(1) the injustice, particularly in the absence of bad faith, of subjecting to liability an officer who is required, by the legal obligations of his position, to exercise discretion; (2) the danger that the threat of such liability would deter his willingness to execute his office with the decisiveness and the judgment required by the public good.”<footnotemark>38</footnotemark></blockquote>
<p id="b714-6">The first consideration is simply not implicated when the damages award comes not from the official’s pocket, but from the public treasury. It hardly seems unjust to require a municipal defendant which has violated a citizen’s constitutional rights to compensate him for the injury suffered thereby. Indeed, Congress enacted § 1983 precisely to provide a remedy for such abuses of official power. See <em>Monroe </em>v. <em>Pape, </em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#171" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 171-172</a></span>. Elemental notions of fairness dictate that one who causes a loss should bear the loss.</p>
<p id="b714-7">It has been argued, however, that revenue raised by taxation for public use should not be diverted to the benefit of a single or discrete group of taxpayers, particularly where the municipality has at all times acted in good faith. On the contrary, the accepted view is that stated in <em>Thayer </em>v. <em>Boston </em>— " that the city, in its corporate capacity, should be liable to make good the damage sustained by an [unlucky] indi<page-number citation-index="1" label="655">*655</page-number>vidual, in consequence of the acts thus done.” <span class="citation" data-id="6407157"><a href="/opinion/6533444/thayer-v-city-of-boston/#515" aria-description="Citation for case: Thayer v. City of Boston">36 Mass., at 515</a></span>. After all, it is the public at large which enjoys the benefits of the government’s activities, and it is the public at large which is ultimately responsible for its administration. Thus, even where some constitutional development could not have been foreseen by municipal officials, it is fairer to allocate any resulting financial loss to the inevitable costs of government borne by all the taxpayers, than to allow its impact to be felt solely by those whose rights, albeit newly recognized, have been violated. See generally 3 K. Davis, Administrative Law Treatise §25.17 (1958 and Supp. 1970); Prosser § 131, at 978; Michelman, Property, Utility, and Fairness: Some Thoughts on the Ethical Foundations of “Just Compensation” Law, <span class="citation no-link">80 Harv. L. Rev. 1165</span> (1967).<footnotemark>39</footnotemark></p>
<p id="b715-5">The second rationale mentioned in <em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">Scheuer</a></span> </em>also loses its force when it is the municipality, in contrast to the official, whose liability is at issue. At the heart of this justification for a qualified immunity for the individual official is the concern that the threat of <em>personal </em>monetary liability will introduce an unwarranted and unconscionable consideration into the decisionmaking process, thus paralyzing the governing official’s decisiveness and distorting his judgment on matters <page-number citation-index="1" label="656">*656</page-number>of public policy.<footnotemark>40</footnotemark> The inhibiting effect is significantly reduced, if not eliminated, however, when the threat of personal liability is removed. First, as an empirical matter, it is questionable whether the hazard of municipal loss will deter a public officer from the conscientious exercise of his duties; city officials routinely make decisions that either require a large expenditure of municipal funds or involve a substantial risk of depleting the public fisc. See <em>Kostka </em>v. <em>Hogg, </em><span class="citation" data-id="348313"><a href="/opinion/348313/alan-s-kostka-v-david-w-hogg/#41" aria-description="Citation for case: Alan S. Kostka v. David W. Hogg">560 F. 2d 37, 41</a></span> (CA1 1977). More important, though, is the realization that consideration of the <em>municipality’s </em>liability for constitutional violations is quite properly the concern of its elected or appointed officials. Indeed, a decisionmaker would be derelict in his duties if, at some point, he did not consider whether his decision comports with constitutional mandates and did not weigh the risk that a violation might result in an award of damages from the public treasury. As one commentator aptly put it: “Whatever other concerns should shape a particular official's actions, certainly one of them should be the constitutional rights of individuals who will be affected by his actions. To criticize section 1983 liability because it leads decisionmakers to avoid the infringement of constitutional rights is to criticize one of the statute’s <em>raisons </em>d’etre.”<footnotemark>41</footnotemark></p>
<p id="b717-4"><page-number citation-index="1" label="657">*657</page-number>IV</p>
<p id="b717-5">In sum, our decision holding that municipalities have no immunity from damages liability flowing from their constitutional violations harmonizes well with developments in the common law and our own pronouncements on official immunities under § 1983. Doctrines of tort law have changed significantly over the past century, and our notions of governmental responsibility should properly reflect that evolution. No longer is individual “blameworthiness” the acid test of liability; the principle of equitable loss-spreading has.joined fault as a factor in distributing the costs of official misconduct.</p>
<p id="b717-6">We believe that today’s decision, together with prior precedents in this area, properly allocates these costs among the three principals in the scenario of the § 1983 cause of action: the victim of the constitutional deprivation; the officer whose conduct caused the injury; and the public, as represented by the municipal entity. The innocent individual who is harmed by an abuse of governmental authority is assured that he will be compensated for his injury. The offending official, so long as he conducts himself in good faith, may go about his business secure in the knowledge that a qualified immunity will protect him from personal liability for damages that are more appropriately chargeable to the populace as a whole. And the public will be forced to bear only the costs of injury inflicted by the “execution of a government’s policy or custom, whether made by its lawmakers or by those whose edicts or acts may fairly be said to represent official policy.” <page-number citation-index="1" label="658">*658</page-number><em>Monell </em>v. <em>New York City Dept. of Social Services, </em>436 U. S., at 694.</p>
<p id="b718-4">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b684-9"> Title <span class="citation no-link">42 U. S. C. § 1983</span> provides:</p>
<blockquote id="b684-10">“Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory, subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress.”</blockquote>
</footnote>
<footnote label="2">
<p id="b685-8"> Under § 3.3 (1) of the city’s charter, the City Manager has sole authority to “[a]ppoint, and when deemed necessary for the good of the service, lay off, suspend, demote, or remove all directors, or heads, of administrative departments and all other administrative officers and employees of the city. . . .”</p>
</footnote>
<footnote label="3">
<p id="b686-8"> Alberg returned from his vacation on the morning of April 17, and immediately met informally with four members of the City Council. Although the investigation of the Police Department was discussed, and although Alberg testified that he had found a replacement for petitioner by that time, he did not inform the Council members of his intention to discharge petitioner.</p>
</footnote>
<footnote label="4">
<p id="b687-6"> The letter, dated April 15,1972, stated in part:</p>
<blockquote id="b687-7">“My counsel . . . have advised me that even though the City Charter may give you authority to relieve me, they also say you cannot do so without granting me my constitutional rights of due process; which includes a written charge and specifications, together with a right to a public hearing and to be represented by counsel and to cross-examine those who may. appear against me.</blockquote>
<blockquote id="b687-8">"In spite of your recent investigation and your public statement given to the public press, your relief and discharge of me without a full public hearing upon written charges will leave in the minds of the public and those who might desire to have my services, a stigma of personal wrongdoing on my part.</blockquote>
<blockquote id="b687-9">“Such action by you would be in violation of my civil rights as granted by the Constitution and Congress of the United States and you would be liable in damages to me. Further it would be in violation of the Missouri Administrative Procedure Act.</blockquote>
<blockquote id="b687-10">“May I have an expression from you that you do not intend to relieve me or in the alternative give me a written charge and specifications of your basis for your grounds of intention to relieve me and to grant me a public hearing with a reasonable opportunity to respond to the charge and a right to be represented by counsel.”</blockquote>
<p id="b687-11">City Manager Alberg stated that he did not receive the letter until after petitioner's discharge.</p>
</footnote>
<footnote label="5">
<p id="b687-12"> Roberts’ statement, which is reproduced in full in <span class="citation" data-id="1770095"><a href="/opinion/1770095/owen-v-city-of-independence-mo/#1116" aria-description="Citation for case: Owen v. City of Independence, Mo.">421 F. Supp. 1110, 1116, n. 2</a></span> (1976), in part recited:</p>
<blockquote id="b687-13">“On April 2, 1972, the City Council was notified of the existence of an investigative report concerning the activities of the Chief of Police of the <page-number citation-index="1" label="628">*628</page-number>City of Independence, certain police officers and activities of one or more other City officials. On Saturday, April 15th for the first time I was able to see these 27 voluminous reports. The contents of these reports are astoundingly shocking and virtually unbelievable. They deal with the disappearance of 2 or more television sets from the police department and signed statement that they were taken by the Chief of Police for his own personal use.</blockquote>
<blockquote id="b688-6">“The reports show that numerous firearms properly in the police department custody found their way into the hands of others including undesirables and were later found by other law enforcement agencies.</blockquote>
<blockquote id="b688-7">“Reports whow [sic] that narcotics held by the Independence Missouri Chief of Police have mysteriously disappeared. Reports also indicate money has mysteriously disappeared. Reports show that traffic tickets have been manipulated. The reports show inappropriate requests affecting the police court have come from high ranking police officials. Reports indicate that things have occurred causing the unusual release of felons. The reports show gross inefficiencies on the part of a few of the high ranking officers of the police department.</blockquote>
<blockquote id="b688-8">“In view of the contents of these reports, I feel that the information in the reports backed up by signed statements taken by investigators is so bad that the council should immediately make available to the news media access to copies of all of these 27 voluminous investigative reports so the public can be told what has been going on in Independence. I further believe that copies of these reports should be turned over and referred to the prosecuting attorney of Jackson County, Missouri for consideration and presentation to the next Grand Jury. I further insist that the City Manager immediately take direct and appropriate action, permitted under the Charter, against such persons as are shown by the investigation to have been involved.”</blockquote>
</footnote>
<footnote label="6">
<p id="b689-7"> Ironically, the official minutes of the City Council meeting indicate that concern was expressed by some members about possible adverse legal consequences that could flow from their release of the reports to the media. The City Counselor assured the Council that although an action might be maintained against any witnesses who made unfounded accusations, “the City does have governmental immunity in this area . . . and neither the Council nor the City as a municipal corporation can be held liable for libelous slander.” App. 20-23.</p>
</footnote>
<footnote label="7">
<p id="b689-8"> See n. 2, <em>supra.</em></p>
</footnote>
<footnote label="8">
<p id="b689-9"> The investigation and its culmination in petitioner’s firing received front-page attention in the local press. See, e. <em>g., </em>“Lid Off Probe, Council Seeks Action,” Independence Examiner, Apr. 18, 1972, Tr. 24-25; “Independence Accusation. Police Probe Demanded,” Kansas City Times, Apr. 18, 1972, Tr. 25; “Probe Culminates in Chief’s Dismissal,” Independence Examiner, Apr. 19, 1972, Tr. 26; “Police Probe Continues; Chief Ousted,” Community Observer, Apr. 20, 1972, Tr. 26.</p>
</footnote>
<footnote label="9">
<p id="b690-7"> Petitioner did not join former Councilman Roberts in the instant litigation. A separate action seeking defamation damages was brought in state court against Roberts and Alberg in their individual capacities. Petitioner dismissed the state suit against Alberg and reached a financial settlement with Roberts. See <span class="citation multiple-matches"><a href="/c/F.%202d/560/925/">560 F. 2d 925</a></span>, 930 (CA8 1977).</p>
</footnote>
<footnote label="10">
<p id="b690-8"> The District Court, relying on <em>Monroe </em>v. <em>Pape, </em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span> (1961), and <em>City of Kenosha </em>v. <em>Bruno, </em><span class="citation" data-id="9425343"><a href="/opinion/108813/city-of-kenosha-v-bruno/" aria-description="Citation for case: City of Kenosha v. Bruno">412 U. S. 507</a></span> (1973), held that § 1983 did not create a cause of action against the city, but that petitioner could base his claim for relief directly on the Fourteenth Amendment. On the merits, however, the court determined that petitioner’s discharge did not deprive him of any constitutionally protected property interest because, as an untenured employee, he possessed neither a contractual nor a <em>de facto </em>right to continued employment as Chief of Police. Similarly, the court found that the circumstances of petitioner’s dismissal did not impose a stigma of illegal or immoral conduct on his professional reputation, and hence did not deprive him of any liberty interest.</p>
<p id="b690-9">The District Court offered three reasons to support its conclusion: First, because the actual discharge notice stated only that petitioner was “[t]er-minated under the provisions of Section 3.3 (1) of the City Charter,” nothing in his official record imputed any stigmatizing conduct to him. .Second, the court found that the City Council’s actions had no causal connection to petitioner’s discharge, for City Manager Alberg had apparently <page-number citation-index="1" label="631">*631</page-number>made his decision to hire a new Police Chief before the-Council’s April 17th meeting. Lastly, the District Court determined that petitioner was “completely exonerated” from any charges of illegal or immoral conduct by the City Counselor’s investigative report, Alberg’s public statements, and the grand jury’s return of a “no true bill.” <span class="citation" data-id="1770095"><a href="/opinion/1770095/owen-v-city-of-independence-mo/#1121" aria-description="Citation for case: Owen v. City of Independence, Mo.">421 F. Supp., at 1121-1122</a></span>.</p>
<p id="b691-6">As an alternative ground for denying relief, the District Court ruled that the city was entitled to assert, and had in fact established, a qualified immunity against liability based on the good faith of the individual defendants who acted as its agents: “[Defendants have clearly shown by a preponderance of the evidence that neither they, nor their predecessors, were aware, in April 1972, that, under the circumstances, the Fourteenth Amendment accorded plaintiff the procedural rights of notice and a hearing at the time of his discharge. Defendants have further proven that they cannot reasonably be charged with constructive notice of such rights since plaintiff was discharged prior to the publication of the Supreme Court decisions in <em>Roth </em>v. <em>Board of Regents, </em>[<span class="citation" data-id="9425009"><a href="/opinion/108608/board-of-regents-of-state-colleges-v-roth/" aria-description="Citation for case: Board of Regents of State Colleges v. Roth">408 U. S. 564</a></span> (1972)], and <em>Perry </em>v. <em>Sindermann, </em>[<span class="citation" data-id="9425012"><a href="/opinion/108609/perry-v-sindermann/" aria-description="Citation for case: Perry v. Sindermann">408 U. S. 593</a></span> (1972)].” <em>Id., </em>at 1123.</p>
</footnote>
<footnote label="11">
<p id="b691-7"> Both parties had appealed from, the District Court’s decision. On respondents’ challenge to the court’s assumption of subject-matter jurisdiction under <span class="citation no-link">28 U. S. C. § 1331</span>, the Court of Appeals held that the city was subject to suit for reinstatement and backpay under an implied right of action arising directly from the Fourteenth Amendment. <span class="citation" data-id="348313"><a href="/opinion/348313/alan-s-kostka-v-david-w-hogg/#932" aria-description="Citation for case: Alan S. Kostka v. David W. Hogg">560 F. 2d, at 932-934</a></span>. See <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971). Because the Court of Appeals concluded that petitioner’s claim could rest directly on the Fourteenth Amendment, it saw no need to decide whether he could recover backpay under § 1983 from the individual defendants in their official capacities as part of general equitable relief, even though the award would be paid by the city. <span class="citation" data-id="348313"><a href="/opinion/348313/alan-s-kostka-v-david-w-hogg/#932" aria-description="Citation for case: Alan S. Kostka v. David W. Hogg">560 F. 2d, at 932</a></span>.</p>
</footnote>
<footnote label="12">
<p id="b692-6"> As compensation for the denial of his constitutional rights, the Court of Appeals awarded petitioner damages in lieu of backpay. The court explained that petitioner’s termination without a hearing must be considered a nullity, and that ordinarily he ought to remain on the payroll and receive wages until a hearing is held and a proper determination on his retention is made. But because petitioner had reached the mandatory retirement age during the course of the litigation, he could not be reinstated to his former position. Thus the compensatory award was to be measured by the amount of money petitioner would likely have earned to retirement had he not been deprived of his good name by the city’s actions, subject to mitigation by the amounts actually earned, as well as by the recovery from Councilman Roberts in the state defamation suit.</p>
<p id="b692-7">The Court of Appeals rejected the municipality’s assertion of a good-faith defense, relying upon a footnote in <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#314" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308, 314-315, n. 6</a></span> (1975) (“immunity from damages does not ordinarily bar equitable relief as well”), and two of its own precedents awarding back-pay in § 1983 actions against school boards. See <em>Wellner </em>v. <em>Minnesota State Jr. College Bd., </em><span class="citation" data-id="9460015"><a href="/opinion/314754/gary-a-wellner-v-minnesota-state-junior-college-board/" aria-description="Citation for case: Gary A. Wellner v. Minnesota State Junior College Board">487 F. 2d 153</a></span> (CA8 1973); <em>Cooley </em>v. <em>Board of Educ. of Forrest City School Dist., </em><span class="citation" data-id="300696"><a href="/opinion/300696/j-f-cooley-appellant-v-the-board-of-education-of-the-forrest-city/" aria-description="Citation for case: J. F. COOLEY, Appellant, v. the BOARD OF EDUCATION OF the...">453 F. 2d 282</a></span> (CA8 1972). The court concluded that the primary justification for a qualified immunity — the fear that public officials might hesitate to discharge their duties if faced with the prospect of personal monetary liability — simply did not exist where the relief would be borne by a governmental unit rather than the individual officeholder. In addition, the Court of Appeals seemed to take issue with the District Court’s finding of good faith on the part of the City Council: “The city officials may have acted in good faith in refusing the hearing, but lack of good faith is evidenced by the nature of the unfair attack made upon the appellant by Roberts in the official conduct of the City’s business. The District Court did not address the good faith defense in light of Roberts’ defamatory remarks.” <span class="citation" data-id="348313"><a href="/opinion/348313/alan-s-kostka-v-david-w-hogg/#941" aria-description="Citation for case: Alan S. Kostka v. David W. Hogg">560 F. 2d, at 941</a></span>.</p>
</footnote>
<footnote label="13">
<p id="b693-6"> Although respondents did not cross petition on this issue, they have raised a belated challenge to the Court of Appeals’ ruling that petitioner was deprived of a protected “liberty” interest. See Brief for Respondents 45-46. We find no merit in their contention, however, and decline to disturb the determination of the court below.</p>
<p id="b693-7"><em>Wisconsin </em>v. <em>Constantineau, </em><span class="citation" data-id="9424387"><a href="/opinion/108230/wisconsin-v-constantineau/#437" aria-description="Citation for case: Wisconsin v. Constantineau">400 U. S. 433, 437</a></span> (1971), held that “[w]here a person’s good name, reputation, honor, or integrity is at stake because of what the government is doing to him, notice and an opportunity to be heard are essential.” In <em>Board of Regents </em>v. <em>Roth, </em><span class="citation" data-id="9425009"><a href="/opinion/108608/board-of-regents-of-state-colleges-v-roth/#573" aria-description="Citation for case: Board of Regents of State Colleges v. Roth">408 U. S. 564, 573</a></span> (1972), we explained that the dismissal of a government employee accompanied by a “charge against him that might seriously damage his standing and associations in his community” would qualify as something “the government is doing to him,” so as to trigger the due process right to a hearing at which the employee could refute the charges and publicly clear his name. In the present case, the city — through the unanimous resolution of the City Council — released to the public an allegedly false statement impugning petitioner’s honesty and integrity. Petitioner was discharged <page-number citation-index="1" label="634">*634</page-number>the next day. The Council’s accusations received extensive coverage in the press, and even if they did not in point of fact “cause” petitioner’s discharge, the defamatory and stigmatizing charges certainly “occur[red] in the course of the termination of employment.” Cf. <em>Paid </em>v. <em>Davis, </em><span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/#710" aria-description="Citation for case: Paul v. Davis">424 U. S. 693, 710</a></span> (1976). Yet the city twice refused petitioner’s request that he be given written specification of the charges against him and an opportunity to clear his name. Under the circumstances, we have no doubt that the Court of Appeals correctly concluded that the city’s actions deprived petitioner of liberty without due process of law.</p>
</footnote>
<footnote label="14">
<p id="b694-7"> Cf. <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#322" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308, 322</a></span> (1975) (“Therefore, in the specific context of school discipline, we hold that a school board member is not immune from liability for damages under § 1983 if he knew or reasonably should have known that the action he took within his sphere of official responsibility would violate the constitutional rights of the student affected, or if he took the action with the malicious intention to cause a deprivation of constitutional rights or other injury to the student”).</p>
</footnote>
<footnote label="15">
<p id="b695-8"> The Courts of Appeals are divided on the question whether local governmental units are entitled to a qualified immunity based on the good faith of their officials. Compare <em>Bertot </em>v. <em>School Dist. No. 1, </em><span class="citation" data-id="9466405"><a href="/opinion/373716/donna-bertot-v-school-district-no-1-albany-county-wyoming/" aria-description="Citation for case: Donna Bertot v. School District No. 1, Albany County,...">613 F. 2d 245</a></span> (CA10 1979) (en banc), <em>Hostrop </em>v. <em>Board of Junior College Dist. No. 615, </em><span class="citation" data-id="330296"><a href="/opinion/330296/richard-w-hostrop-v-board-of-junior-college-district-no-515-counties-of/" aria-description="Citation for case: Richard W. Hostrop v. Board of Junior College District...">523 F. 2d 569</a></span> (CA7 1975), and <em>Hander </em>v. <em>San Jacinto Jr. College, </em><span class="citation" data-id="9461921"><a href="/opinion/328776/lecil-hander-v-san-jacinto-junior-college-etc/" aria-description="Citation for case: Lecil Hander v. San Jacinto Junior College, Etc.">519 F. 2d 273</a></span> (CA5), rehearing denied, <span class="citation" data-id="329966"><a href="/opinion/329966/lecil-hander-v-san-jacinto-junior-college-etc/" aria-description="Citation for case: Lecil Hander v. San Jacinto Junior College, Etc.">522 F. 2d 204</a></span> (1975), all refusing to extend a qualified immunity to the governmental entity, with <em>Paxman </em>v. <em>Campbell, </em><span class="citation" data-id="8910764"><a href="/opinion/8921863/paxman-v-campbell/" aria-description="Citation for case: Paxman v. Campbell">612 F. 2d 848</a></span> (CA4 1980) (en banc), and <em>Seda </em>v. <em>County of Suffolk, </em><span class="citation" data-id="369082"><a href="/opinion/369082/diane-sala-v-county-of-suffolk-philip-f-corso-sheriff-of-the-county-of/" aria-description="Citation for case: Diane Sala v. County of Suffolk, Philip F. Corso, Sheriff...">604 F. 2d 207</a></span> (CA2 1979), granting defendants a “good-faith” immunity.</p>
</footnote>
<footnote label="16">
<p id="b695-9"> See n. 1, <em>supra.</em></p>
</footnote>
<footnote label="17">
<p id="b696-7"> As we noted in <em>Monell </em>v. <em>New York City Dept. of Social Services, </em>see 436 U. S., at 685-686, n. 45, even the opponents of § 1 acknowledged that its language conferred upon the federal courts the entire power that Congress possessed to remedy constitutional violations. The remarks of Senator Thurman are illustrative:</p>
<blockquote id="b696-8">“[This section’s] whole effect is to give to the Federal Judiciary that which now does not belong to it — a jurisdiction that may be constitutionally conferred upon it, I grant, but that has never yet been conferred upon it. It authorizes any person who is deprived of any right, privilege, or immunity secured to him by the Constitution of the United States, to bring an action <page-number citation-index="1" label="637">*637</page-number>against the wrong-doer in the Federal courts, and that without any limit whatsoever as to the amount in controversy. . . .</blockquote>
<blockquote id="b697-7"><em>. . </em>That is the language of this bill. Whether it is the intent or not I know not, but it is the language of the bill; for there is no limitation whatsoever upon the terms that are employed, and they are as comprehensive as can be used.” Globe App. 216-217.</blockquote>
</footnote>
<footnote label="18">
<p id="b698-8"> The governmental immunity at issue in the present case differs significantly from the official immunities involved in our previous decisions. In those cases, various government officers had been sued in their individual capacities, and the immunity served to insulate them from personal liability for damages. Here, in contrast, only the liability of the municipality itself is at issue, not that of its officers, and in the absence of an immunity, any recovery would come from public funds.</p>
</footnote>
<footnote label="19">
<p id="b699-5"> Primary among the constitutional suits heard in federal court were those based on a municipality’s violation of the Contract Clause, and the courts’ enforcement efforts often included “various forms of ‘positive’ relief, such as ordering that taxes be levied and collected to discharge federal-court judgments, once a constitutional infraction was found.” <em>Monell </em>v. <em>New York City Dept. of Social </em>Services, 436 U. S., at 681. Damages actions against municipalities for federal statutory violations were also entertained.. See, <em>e. g., Levy Court </em>v. <em>Coroner, </em><span class="citation" data-id="87666"><a href="/opinion/87666/levy-court-v-coroner/" aria-description="Citation for case: Levy Court v. Coroner">2 Wall. 501</a></span> (1865); <em>Corporation of New York </em>v. <em>Ransom, </em><span class="citation" data-id="87361"><a href="/opinion/87361/mayor-aldermen-and-commonalty-of-city-of-new-york-v-ransom/" aria-description="Citation for case: Mayor, Aldermen, and Commonalty, of City of New York v....">23 How. 487</a></span> (1860); <em>Bliss </em>v. <em>Brooklyn, </em><span class="citation" data-id="8628671"><a href="/opinion/8648861/bliss-v-brooklyn/" aria-description="Citation for case: Bliss v. Brooklyn">3 F. Cas. 706</a></span> (No. 1,544) (CC EDNY 1871). In addition, state constitutions and statutes, as well as municipal charters, imposed many obligations upon the local governments, the violation of which typically gave rise to damages actions against the city. See generally Note, Streets, Change of Grade, Liability of Cities for, <span class="citation no-link">30 Am. St. Rep. 835</span> (1893), and cases cited therein. With respect to authorized contracts — and even unauthorized contracts that are later ratified by the corporation — municipalities were liable in the same manner as individuals for their breaches. See generally 1 J. Dillon, Law of Municipal Corporations §§385, 394 (2d ed. 1873) (hereinafter Dillon). Of particular relevance to the instant case, included within the class of contract actions brought against a city were those for the wrongful discharge of a municipal employee, and where the claim was adjudged meritorious, damages in the nature of backpay were regularly awarded. See, <em>e. g., Richardson </em>v. <em>School Dist. No. 10, </em><span class="citation" data-id="6578118"><a href="/opinion/6698118/richardson-v-school-district-no-10/" aria-description="Citation for case: Richardson v. School District No. 10">38 Vt. 602</a></span> (1866); <em>Paul </em>v. <em>School Dist. No. 2, </em><span class="citation" data-id="6575930"><a href="/opinion/6695961/paul-v-school-district-no-2/" aria-description="Citation for case: Paul v. School District No. 2">28 Vt. 575</a></span> (1856); <em>Inhabitants of Searsmont </em>v. <em>Farwell, </em>3 Me. *450 (1825); see generally F. Burke, A Treatise on the Law of Public Schools 81-85 (1880). The most frequently litigated “breach of contract” suits, however, at least in federal court, were those for failure to pay interest on municipal bonds. See, <em>e. g., The Supervisors </em>v. <em>Durant, </em><span class="citation" data-id="88174"><a href="/opinion/88174/supervisors-v-durant/" aria-description="Citation for case: Supervisors v. Durant">9 Wall. 415</a></span> (1870); <em>Commissioners of Knox County </em>v. <em>Aspinwall, </em><span class="citation" data-id="9416661"><a href="/opinion/87248/board-of-commrs-of-knox-cty-v-aspinwall/" aria-description="Citation for case: Board of Comm&#x27;rs of Knox Cty. v. Aspinwall">21 How. 539</a></span> (1859).</p>
</footnote>
<footnote label="20">
<p id="b699-6"> See <em>infra, </em>at 644-650.</p>
</footnote>
<footnote label="21">
<p id="b700-8"> See generally C. Rhyne, Municipal Law 729-789 (1957); Shearman <em>&amp; </em><page-number citation-index="1" label="641">*641</page-number>Redfield §§ 143-152; W. Williams, Liability of Municipal Corporations for Tort (1901) (hereinafter Williams).</p>
</footnote>
<footnote label="22">
<p id="b702-5"> Accord, <em>Bunker </em>v. <em>City of Hudson, </em><span class="citation" data-id="8187937"><a href="/opinion/8224334/bunker-v-city-of-hudson/#54" aria-description="Citation for case: Bunker v. City of Hudson">122 Wis. 43, 54</a></span>, <span class="citation" data-id="8187937"><a href="/opinion/8224334/bunker-v-city-of-hudson/#452" aria-description="Citation for case: Bunker v. City of Hudson">99 N. W. 448, 452</a></span> (1904); <em>Oklahoma City </em>v. <em>Hill Bros., </em><span class="citation" data-id="3829428"><a href="/opinion/4071499/city-of-oklahoma-city-v-hill-bros/#137" aria-description="Citation for case: City of Oklahoma City v. Hill Bros.">6 Okla. 114, 137-139</a></span>, <span class="citation" data-id="3829428"><a href="/opinion/4071499/city-of-oklahoma-city-v-hill-bros/#249" aria-description="Citation for case: City of Oklahoma City v. Hill Bros.">50 P. 242, 249-250</a></span> (1897); <em>Schussler </em>v. <em>Board of Comm’rs of Hennepin County, </em><span class="citation" data-id="7969795"><a href="/opinion/8014737/schussler-v-board-of-commissioners/#417" aria-description="Citation for case: Schussler v. Board of Commissioners">67 Minn. 412, 417</a></span>, <span class="citation" data-id="7969795"><a href="/opinion/8014737/schussler-v-board-of-commissioners/#7" aria-description="Citation for case: Schussler v. Board of Commissioners">70 N. W. 6, 7</a></span> (1897); <em>McGraw </em>v. <em>Town of Marion, </em><span class="citation" data-id="7133323"><a href="/opinion/7221215/mcgraw-v-town-of-marion/#680" aria-description="Citation for case: McGraw v. Town of Marion">98 Ky. 673, 680-683</a></span>, <span class="citation" data-id="7133323"><a href="/opinion/7221215/mcgraw-v-town-of-marion/#20" aria-description="Citation for case: McGraw v. Town of Marion">34 S. W. 18, 20-21</a></span> (1896). See generally Note, Liability of Cities for the Negligence and Other Misconduct of their Officers and Agents, <span class="citation no-link">30 Am. St. Rep. 376</span>, 405-411 (1893).</p>
<p id="b702-6">Even in England, where the doctrine of official immunity followed by the American courts was first established, no immunity was granted where the damages award was to come from the public treasury. As Baron Bramwell stated in <em>Buck </em>v. <em>Williams, </em>3 H. &amp; N. 308, 320, 157 Eng. Rep. 488, 493 (Exch. 1858):</p>
<blockquote id="b702-7">“I can well understand if a person undertakes the office or duty of a Commissioner, and there are no means of indemnifying him against the consequences of a slip, it is reasonable to hold that he should not be responsible for it. I can also understand that, if one of several Commissioners does something not within the scope of his authority, the Commissioners as a body are not liable. But where Commissioners, who are a quasi corporate body, are not affected <em>[i. e., </em>personally] by the result of an action, inasmuch as they are authorized by act of parliament to raise a fund for payment of the damages, on what principle is it that, if an individual member of the public suffers from an act bona fide but erroneously done, he is not to be compensated? It seems to me inconsistent with actual justice, and not warranted by any principle of law.”</blockquote>
<p id="b702-8">See generally Shearman &amp; Redfield §§ 133, 178.</p>
</footnote>
<footnote label="23">
<p id="b703-5"> Senator Stevenson proceeded to read from the decision in <em>Prather </em>v. <em>Lexington, </em><span class="citation" data-id="7129316"><a href="/opinion/7217313/prather-v-city-of-lexington/#560" aria-description="Citation for case: Prather v. City of Lexington">52 Ky. 559, 560-562</a></span> (1852):</p>
<blockquote id="b703-6">“Where a particular act, operating injuriously to an individual, is authorized by a municipal corporation, by a delegation of power either general or special, it will be liable for the injury in its corporate capacity, where the acts done would warrant a like action against an individual. But as a general rule a corporation is not responsible for the unauthorized and unlawful acts of its officers, although done under the color of their office; to render it liable it must appear that it expressly authorized the acts to be done by them, or that they were done in pursuance of a general authority to act for the corporation, on the subject to which they relate. <em>(Thayer </em>v. <em>Boston, </em><span class="citation no-link">19 Pick., 511</span>.) It has also been held that cities are responsible to the same extent, and in the same manner, as natural persons for injuries occasioned by the negligence or unskillfulness of their agents jn the constmction .of works for their benefit.” Globe 762.</blockquote>
</footnote>
<footnote label="24">
<p id="b703-7"> At one point in the'debafesPSenator Stevenson did protest that the Sherman amendment would, for the first time, “create a corporate liability for personal injury which no prudence or foresight could have prevented.” <em><span class="citation no-link">Ibid.</span> As </em>his later remarks made clear, however, Stevenson’s objection went only to the novelty of the amendment’s creation of vicarious municipal liability for the unlawful acts of private individuals, “even if a municipality did not know of an impending or ensuing riot or did not have the wherewithal to do anything about it.” <em>Monell </em>v. <em>New York City Dept. of Social Services, </em>436 U. S., at 692-693, n. 57.</p>
</footnote>
<footnote label="25">
<p id="b703-8"> See, <em>e. g., </em>Globe 365 (remarks of Rep. Arthur) (“But if the Legislature enacts a law, if the Governor enforces it, if the judge upon the bench renders a judgment, if the sheriff levy an execution, execute a writ, serve a summons, or make an arrest, all acting under a solemn, official oath, <page-number citation-index="1" label="644">*644</page-number>though as pure in duty as a saint and as immaculate as a seraph, for a mere error in judgment, they are liable. . .”); <em>id., </em>at 385 (remarks of Rep. Lewis); Globe App. 217 (remarks of Sen. Thurman).</p>
</footnote>
<footnote label="26">
<p id="b704-8"> In actuality, the distinction between a municipality’s governmental and proprietary functions is better characterized not as a line, but as a succession of points. In efforts to avoid the often-harsh results occasioned by a literal application of the test, courts frequently created highly artificial and elusive distinctions of their own. The result was that the very same activity might be considered “governmental” in one jurisdiction, and “proprietary” in another. See 18 McQuillin § 53.02, at 105. See also W. Prosser, Law of Torts § 131, p. 979 (4th ed. 1971) (hereinafter Pros-ser) . As this Court stated, in reference to the “ ‘nongovernmental’-‘governmental’ quagmire that has long plagued the law of municipal corporations”: “A comparative study of the cases in the forty-eight States will disclose an irreconcilable conflict. More than that, the decisions in each of the States are disharmonious and disclose the inevitable chaos when courts try to apply a rule of law that is inherently unsound.” <em>Indian Towing Co. </em>v. <em>United States, </em><span class="citation" data-id="9421210"><a href="/opinion/105329/indian-towing-co-v-united-states/#65" aria-description="Citation for case: Indian Towing Co. v. United States">350 U. S. 61, 65</a></span> (1955) (on rehearing).</p>
</footnote>
<footnote label="27">
<p id="b705-5"> “While acting in their governmental capacity, municipal corporations proper are given the benefit of that same rule which is applied to the sovereign power itself, and are afforded complete immunity from civil responsibility for acts done or omitted, unless such responsibility is expressly created by statute. When, however, they are not acting in the exercise of their purely governmental functions, but are performing duties that pertain to the exercise of those private franchises, powers, and privileges which belong to them for theirown. corporate benefit, or are dealing with property held by them for their own corporate gain or emolument, then a different rule of liability is applied and they are generally held responsible for injuries arising from their negligent acts or their omissions to the same extent as a private corporation under like circumstances.” Williams §4, at 9. See generally 18 McQuillin §§53.02, 53.04, 53.24; Prosser § 131, at 977-983; James, Tort Liability of Governmental Units and Their Officers, <span class="citation no-link">22 U. Chi. L. Rev. 610</span>, 611-612, 622-629 (1955).</p>
</footnote>
<footnote label="28">
<p id="b705-6"> Although it has never been understood how the doctrine of sovereign immunity came to be adopted in the American democracy, it apparently stems from the personal immunity of the English Monarch as expressed in the maxim, “The King can do no wrong.” It has been suggested, however, that the meaning traditionally ascribed to this phrase is an ironic perversion of its original intent: “The maxim merely meant that the King was not privileged to do wrong. If his acts were against the law, they were <em>injuriae </em>(wrongs). Bracton, while ambiguous in his several statements as to the relation between the King and the law, did not intend .to convey the idea that he was incapable of committing a legal wrong.” Borchard, Government Liability in Tort, 34 Yale L. J. 1, 2, n. 2 (1924). See also Kates &amp; Kouba, Liability of Public Entities Under Section 1983 of the Civil Rights Act, <span class="citation no-link">45 S. Cal. L. Rev. 131</span>, 142 (1972).</p>
<p id="b705-7">In this country, “[t]he sovereign or governmental immunity doctrine, holding that the state, its subdivisions and municipal entities, may not be <page-number citation-index="1" label="646">*646</page-number>held liable for tortious acts, was never completely accepted by the courts, its underlying principle being deemed contrary to the basic concept of the law of torts that liability follows negligence, as well as foreign to the spirit of the constitutional guarantee that every person is entitled to a legal remedy for injuries he may receive in his person or property. As a result, the trend of judicial decisions was always to restrict, rather than to expand, the doctrine of municipal immunity.” 18 McQuillin § 53.02, at 104 (footnotes omitted). See also Prosser § 131, at 984 (“For well over a century the immunity of both the state and the local governments for their torts has been subjected to vigorous criticism, which at length has begun to have its effect”). The seminal opinion of the Florida Supreme Court in <em>Hargrove </em>v. <em>Town of Cocoa Beach, </em><span class="citation" data-id="1696303"><a href="/opinion/1696303/hargrove-v-town-of-cocoa-beach/" aria-description="Citation for case: Hargrove v. Town of Cocoa Beach">96 So. 2d 130</a></span> (1957), has spawned “a minor avalanche of decisions repudiating municipal immunity,” Prosser § 131, at 985, which, in conjunction with legislative abrogation of sovereign immunity, has resulted in the consequence that only a handful of States still cling to the old common-law rule of immunity for governmental functions. See K. Davis, Administrative Law of the Seventies §25.00 (1976 and Supp. 1977) (only two States adhere to the traditional common-law immunity from torts in the exercise of governmental functions); Harley &amp; Wasinger, Government Immunity: Despotic Mantle or Creature of Necessity, 16 Washburn L. J. 12, 34-53 (1976).</p>
</footnote>
<footnote label="29">
<p id="b707-6"> The common-law immunity for governmental functions is thus more comparable to an absolute immunity from liability for conduct of a certain character, which defeats a suit at the outset, than to a qualified immunity, which “depends upon the circumstances and motivations of [the official’s] actions, as established by the evidence at trial.” <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#419" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409, 419, n. 13</a></span> (1976).</p>
</footnote>
<footnote label="30">
<p id="b707-7"> Municipal defenses — including an assertion of sovereign immunity— to a federal right of action are, of course, controlled by federal law. See <em>Fitzpatrick </em>v. <em>Bitzer, </em><span class="citation" data-id="9426527"><a href="/opinion/109520/fitzpatrick-v-bitzer/#455" aria-description="Citation for case: Fitzpatrick v. Bitzer">427 U. S. 445, 455-456</a></span> (1976); <em>Hampton </em>v. <em>Chicago, </em><span class="citation multiple-matches"><a href="/c/F.%202d/484/602/">484 F. 2d 602</a></span>, 607 (CA7 1973) (Stevens, J.) (“Conduct by persons acting under color of state law which is wrongful under <span class="citation no-link">42 U. S. C. § 1983</span> or § 1985 (3) cannot be immunized by state law. A construction of the federal statute which permitted a state immunity defense to have controlling effect would transmute a basic guarantee into an illusory promise; and the supremacy clause of the Constitution insures that the proper construction may be enforced”).</p>
</footnote>
<footnote label="31">
<p id="b708-7"> See generally 18 McQuillin § 53.04a; Shearman &amp; Redfield §§ 127-130; Williams § 6, at 15-16. Like the govemmental/proprietary distinction, a clear line between the municipality’s “discretionary” and “ministerial” functions was often hard to discern, a difficulty which has been mirrored in the federal courts’ attempts to draw a similar distinction under the Federal Tort Claims Act, <span class="citation no-link">28 U. S. C. §2680</span> (a). See generally 3 K. Davis, Administrative Law Treatise §25.08 (1958 and Supp. 1970).</p>
</footnote>
<footnote label="32">
<p id="b710-8"> Cf. P. Bator, P. Mishkin, D. Shapiro, <em>&amp; </em>H. Wechsler, Hart and Wechsler’s The Federal Courts and the Federal System 336 (2d ed. 1973) (“[W]here constitutional rights are at stake the courts are properly astute, in construing statutes, to avoid the conclusion that Congress intended to use the privilege of immunity ... in order to defeat them”).</p>
</footnote>
<footnote label="33">
<p id="b711-7"> The absence of any damages remedy for violations of all but the most “clearly established” constitutional rights, see <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#322" aria-description="Citation for case: Wood v. Strickland">420 U. S., at 322</a></span>, could also have the deleterious effect of freezing constitutional law in its current state of development, for without a meaningful remedy aggrieved individuals will have little incentive to seek vindication of those constitutional deprivations that have not previously been clearly defined.</p>
</footnote>
<footnote label="34">
<p id="b712-6"> For example, given the discussion that preceded the Independence City Council’s adoption of the allegedly slanderous resolution impugning petitioner’s integrity, see n. 6, <em>supra, </em>one must wonder whether this entire litigation would have been necessary had the Council members thought that the city might be liable for their misconduct.</p>
</footnote>
<footnote label="35">
<p id="b712-7"> Cf. <em>Albemarle Paper Co. </em>v. <em>Moody, </em><span class="citation" data-id="9426162"><a href="/opinion/109299/albemarle-paper-co-v-moody/#417" aria-description="Citation for case: Albemarle Paper Co. v. Moody">422 U. S. 405, 417-418</a></span> (1975): “If employers faced only the prospect of an injunctive order, they would have little incentive to shun practices of dubious legality. It is the reasonably certain prospect of a backpay award that ‘provide[s] the spur or catalyst which causes employers and unions to self-examine and to self-evaluate their employment practices and. to endeavor to eliminate, so far as possible, the last vestiges of an unfortunate and ignominious page in this country’s history.’ <em>United States </em>v. <em>N. L. Industries, Inc., </em><span class="citation" data-id="8890222"><a href="/opinion/8903207/united-states-v-n-l-industries-inc/#379" aria-description="Citation for case: United States v. N. L. Industries, Inc.">479 F. 2d 354, 379</a></span> (CA8 1973).”</p>
</footnote>
<footnote label="36">
<p id="b712-8"> In addition, the threat of liability against the city ought to increase the attentiveness with which officials at the higher levels of government supervise the conduct of their subordinates. The need to institute system-wide measures in order to increase the vigilance with which otherwise indifferent municipal officials protect citizens’ constitutional rights Js, of course, particularly acute where the frontline officers are judgment-proof in their individual capacities.</p>
</footnote>
<footnote label="37">
<p id="b713-5"> On at least two previous occasions, this Court has expressly recognized that different considerations come into play when governmental rather than personal liability is threatened. <em>Hutto </em>v. <em>Finney, </em><span class="citation" data-id="9427304"><a href="/opinion/109919/hutto-v-finney/" aria-description="Citation for case: Hutto v. Finney">437 U. S. 678</a></span> (1978), affirmed an award of attorney’s fees out of state funds for a deprivation of constitutional rights, holding that such an assessment would not contravene the Eleventh Amendment. In response to the suggestion, adopted by the dissent, that any award should be borne by the government officials personally, the Court noted that such an allocation would not only be “manifestly unfair,” but would,“def[y] this Court’s insistence in a related context that imposing personal liability in the absence of bad faith may cause state officers to ‘exercise their discretion with undue timidity.’ <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#321" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308, 321</a></span>.” <em>Id., </em>at 699, n. 32. The Court thus acknowledged that imposing personal liability on public officials could have an undue chilling effect on the exercise of their decision-making responsibilities, but that no such pernicious consequences were likely to flow from the possibility of a recovery from public funds.</p>
<p id="b713-6">Our decision in <em>Lake Country Estates, Inc. </em>v. <em>Tahoe Regional Planning Agency, </em><span class="citation" data-id="9427483"><a href="/opinion/110033/lake-country-estates-inc-v-tahoe-regional-planning-agency/" aria-description="Citation for case: Lake Country Estates, Inc. v. Tahoe Regional Planning Agency">440 U. S. 391</a></span> (1979), also recognized that the justifications for immunizing officials from personal liability have little force when suit is brought against the governmental entity itself. Petitioners in that case had sought damages under § 1983 from a regional planning agency and the individual members of its governing agency. Relying on <em>Tenney </em>v. <em>Brand-hove, </em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">341 U. S. 367</a></span> (1951), the Court concluded that “to the extent the evidence discloses that these individuals were acting in a capacity comparable to that of members- of a state legislature, they are entitled to absolute immunity from federal damages liability.” <span class="citation" data-id="9427483"><a href="/opinion/110033/lake-country-estates-inc-v-tahoe-regional-planning-agency/#406" aria-description="Citation for case: Lake Country Estates, Inc. v. Tahoe Regional Planning Agency">440 U. S., at 406</a></span>. At the same time, however, we cautioned: “If the respondents have enacted unconstitutional legislation, there is no reason why relief against TRPA itself should not adequately vindicate petitioners’ interests. See <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span>.” <em>Id., </em>at 405, n. 29.</p>
</footnote>
<footnote label="38">
<p id="b714-8"> <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308</a></span> (1975), mentioned a third justification for extending a qualified immunity to public officials: the fear that the threat of personal liability might deter citizens from holding public office. See <span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#320" aria-description="Citation for case: Wood v. Strickland"><em>id., </em>at 320</a></span> (“The most capable candidates for school board positions might be deterred from seeking office if heavy burdens upon their private resources from monetary liability were a likely prospect during their tenure”). Such fears are totally unwarranted, of course, once the threat of personal liability is eliminated.</p>
</footnote>
<footnote label="39">
<p id="b715-6"> <em>Monell </em>v. <em>New York City Dept. of Social Services </em>indicated that the principle of loss-spreading was an insufficient justification for holding the municipality liable under § 1983 on a <em>respondeat superior </em>theory. 436 U. S., at 693-694. Here, of course, quite a different situation is presented. Petitioner does not seek to hold the city responsible for the unconstitutional actions of an individual official <em>“solely </em>because it employs a tortfeasor.” <em>Id., </em>at 691. Rather, liability is predicated on a determination that “the action that is alleged to be unconstitutional implements or executes a policy statement, ordinance, regulation, or decision officially adopted and promulgated by that body’s officers.” <em>Id., </em>at 690. In this circumstance — when it is the local government itself that is responsible for the constitutional deprivation — it is perfectly reasonable to distribute the loss to the public as a cost of the administration of government, rather than to let the entire burden fall on the injured individual.</p>
</footnote>
<footnote label="40">
<p id="b716-5"> “The imposition of monetary costs for mistakes which were not unreasonable in the light of all the circumstances would undoubtedly deter even the most conscientious school decisionmaker from exercising his judgment independently, forcefully, and in a manner best serving the long-term interest of the school and the students.” <em>Wood </em>v. <span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#319" aria-description="Citation for case: Wood v. Strickland"><em>Strickland, supra, </em>at 319-320</a></span>.</p>
</footnote>
<footnote label="41">
<p id="b716-6"> Note, Developments in the Law: Section 1983 and Federalism, <span class="citation no-link">90 Harv. L. Rev. 1133</span>, 1224 (1977). See also <em>Johnson </em>v. <em>State, </em><span class="citation multiple-matches"><a href="/c/Cal.%202d/69/782/">69 Cal. 2d 782</a></span>, 792-793, <span class="citation" data-id="9574558"><a href="/opinion/1312748/johnson-v-state-of-california/#359" aria-description="Citation for case: Johnson v. State of California">447 P. 2d 352, 359-360</a></span> (1968):</p>
<blockquote id="b716-7">“Nor do we deem an employee’s concern over the potential liability of his employer, the governmental unit, a justification for an expansive definition of 'discretionary/ and hence immune, acts. As a threshold matter, we consider it unlikely that the possibility of government liability will be <page-number citation-index="1" label="657">*657</page-number>a serious deterrent to the fearless exercise of judgment by the employee. In any event, however, to the extent that such a deterrent effect takes hold, it may be wholesome. An employee in a private enterprise naturally gives some consideration to the potential liability of his employer, and this attention unquestionably promotes careful work; the potential liability of a governmental entity, to the extent that it affects primary conduct at all, will similarly influence public employees.” (Citation and footnote omitted.)</blockquote>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Payton v. New York.md  (`case`, 7 assertions)

### content_page

```
---
title: "Payton v. New York"
type: case
citation: "445 U.S. 573 (1980)"
parallel_cite: "100 S. Ct. 1371; 63 L. Ed. 2d 639"
neutral_cite: 1980 U.S. LEXIS 13
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-04-15
docket: 78-5420
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1980-04-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Payton v. New York
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110235/payton-v-new-york/"
  cluster_id: 110235
  opinion_id: 110235
  identity_checked: true
homes:
  - page: "[[Arrest in the Home]]"
    role: "Key — Anchor"
  - page: "[[Entry to Arrest]]"
    role: "Key — Anchor"
  - page: "[[Securing the Scene]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Watson]]", "[[Steagald v. United States]]", "[[Maryland v. Buie]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest-in-the-home", "arrest-warrant", "warrant-requirement", "threshold"]
holding: "Warrantless, nonconsensual entry into a SUSPECT'S OWN home to make a routine felony arrest is presumptively unreasonable; an arrest…"
lake:
  record_id: Payton v. New York
  status: verified
  projected_at: 2026-07-09
---

# Payton v. New York

*445 U.S. 573 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
New York statutes authorized police to enter a private residence without a warrant, by force if necessary, to make a routine felony arrest. In Payton's case, detectives had probable cause that Theodore Payton murdered a gas-station manager; at 7:30 a.m. six officers went to his Bronx apartment without a warrant, got no answer, broke open the door, and seized a shell casing in plain view. (The consolidated *Riddick* case involved a similar warrantless home arrest.)

## Issue
Whether the Fourth Amendment permits police to make a warrantless and nonconsensual entry into a suspect's own home in order to make a routine felony arrest.

## Rule
No. The Fourth Amendment "prohibits the police from making a warrantless and nonconsensual entry into a suspect's home in order to make a routine felony arrest." — 445 U.S. at 576. ^pin-576

"In terms that apply equally to seizures of property and to seizures of persons, the Fourth Amendment has drawn a firm line at the entrance to the house. Absent exigent circumstances, that threshold may not reasonably be crossed without a warrant." — [445 U.S. at 590](https://www.courtlistener.com/opinion/110235/payton-v-new-york/#:~:text=In%20terms%20that%20apply%20equally). ^pin-590

## Application
The detectives had probable cause to arrest Payton but no warrant and no [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] when they forced entry into his apartment; the same was true of the warrantless entry to arrest Riddick in his home. Because the Fourth Amendment draws a firm line at the entrance to the house, those warrantless, nonconsensual entries to make routine felony arrests were unconstitutional, and the evidence obtained (including the shell casing seized in Payton's apartment) could not stand on that basis.

## Conclusion
Warrantless, nonconsensual home entry to make a routine felony arrest is presumptively unreasonable absent [[Exigent Circumstances and Hot Pursuit|exigent circumstances]]; the New York statutes were unconstitutional and the judgments were reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. An arrest warrant founded on probable cause implicitly carries the limited authority to enter a suspect's *own* dwelling to arrest when there is reason to believe he is within; entry to arrest in a *third party's* home additionally requires a search warrant ([[Steagald v. United States]]).

## Appears on
- [[Arrest in the Home]] — *Key — Anchor*
- [[Entry to Arrest]] — *Key — Anchor*
- [[Securing the Scene]] — *Related (cross-doctrine)*

## Sources
- *Payton v. New York*, 445 U.S. 573 (1980) — https://www.courtlistener.com/opinion/110235/payton-v-new-york/ — pinpoints: 576, 590.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9a34ba6bea1f8abc", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "445 U.S. 573 (1980)", "court": "U.S. Supreme Court", "neutral_cite": "1980 U.S. LEXIS 13", "official_citation_present": true, "parallel_cite": "100 S. Ct. 1371; 63 L. Ed. 2d 639", "title": "Payton v. New York", "year": "1980"}}
{"assertion_id": "42a1394b94233374", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Warrantless, nonconsensual entry into a SUSPECT'S OWN home to make a routine felony arrest is presumptively unreasonable; an arrest…", "title": "Payton v. New York"}}
{"assertion_id": "5cd40465f100f814", "dimension": "support", "kind": "home_role", "locator": {"home": "Entry to Arrest"}, "payload": {"home": "Entry to Arrest", "role": "Key — Anchor", "title": "Payton v. New York"}}
{"assertion_id": "a9026561baac9f22", "dimension": "support", "kind": "home_role", "locator": {"home": "Securing the Scene"}, "payload": {"home": "Securing the Scene", "role": "Related (cross-doctrine)", "title": "Payton v. New York"}}
{"assertion_id": "da4dc842219ed689", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Key — Anchor", "title": "Payton v. New York"}}
{"assertion_id": "101735b6e110e14f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1980-04-15", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Payton v. New York", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Payton v. New York", "varies_by_point": "false"}}
{"assertion_id": "f1426c83980a35f8", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Payton v. New York"}}
```

### lake record — Payton v. New York

```json
{
  "schema_version": "s2.v1",
  "record_id": "Payton v. New York",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Payton v. New York",
    "case_name_short": "Payton",
    "case_name_full": "Payton v. New York",
    "input_case_name": "Payton v. New York",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-04-15",
    "year": 1980,
    "docket": "78-5420",
    "cluster_id": 110235,
    "lead_opinion_id": 110235,
    "sibling_ids": [
      110235,
      9427853,
      9427854,
      9427855,
      9427856,
      9427857
    ],
    "absolute_url": "/opinion/110235/payton-v-new-york/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "445 U.S. 573",
      "volume": "445",
      "reporter": "U.S.",
      "page": "573",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 1371",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1371",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "63 L. Ed. 2d 639",
        "volume": "63",
        "reporter": "L. Ed. 2d",
        "page": "639",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 13",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "13",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "445 U.S. 573",
        "volume": "445",
        "reporter": "U.S.",
        "page": "573",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 1371",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1371",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "63 L. Ed. 2d 639",
        "volume": "63",
        "reporter": "L. Ed. 2d",
        "page": "639",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 13",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "13",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "445 U.S. 573",
    "official_selection": {
      "court_class": "scotus",
      "selected": "445 U.S. 573",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-576",
      "page": null,
      "quote": "--- # Payton v. New York *445 U.S. 573 (1980)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background New York statutes authorized police to enter a private residence without a warrant, by force if necessary, to make a routine felony arrest. In Payton's case, detectives had probable cause that Theodore Payton murdered a gas-station manager; at 7:30 a.m. six officers went to his Bronx apartment without a warrant, got no answer, broke open the door, and seized a shell casing in plain view. (The consolidated *Riddick* case involved a similar warrantless home arrest.) ## Issue Whether the Fourth Amendment permits police to make a warrantless and nonconsensual entry into a suspect's own home in order to make a routine felony arrest. ## Rule No. The Fourth Amendment",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-590",
      "page": null,
      "quote": "In terms that apply equally to seizures of property and to seizures of persons, the Fourth Amendment has drawn a firm line at the entrance to the house. Absent exigent circumstances, that threshold may not reasonably be crossed without a warrant.",
      "star_marker": "590",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 22362,
      "fragment": "#:~:text=In%20terms%20that%20apply%20equally",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1980-04-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Payton v. New York",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Poulson v. Commonwealth",
          "cluster_id": 10375911,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Payton v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jamin Kidron Stocker v. the State of Texas",
          "cluster_id": 9329108,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Payton v. New York:lane1_negative"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pembaur v. City of Cincinnati",
          "cluster_id": 111615,
          "cite": [
            "89 L. Ed. 2d 452",
            "106 S. Ct. 1292",
            "475 U.S. 469",
            "1986 U.S. LEXIS 33",
            "54 U.S.L.W. 4289"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Payton v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tennessee v. Garner",
          "cluster_id": 111397,
          "cite": [
            "85 L. Ed. 2d 1",
            "105 S. Ct. 1694",
            "471 U.S. 1",
            "1985 U.S. LEXIS 195",
            "53 U.S.L.W. 4410"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffith v. Kentucky",
          "cluster_id": 111785,
          "cite": [
            "93 L. Ed. 2d 649",
            "107 S. Ct. 708",
            "479 U.S. 314",
            "1987 U.S. LEXIS 283",
            "55 U.S.L.W. 4089"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. Wisconsin",
          "cluster_id": 111959,
          "cite": [
            "97 L. Ed. 2d 709",
            "107 S. Ct. 3164",
            "483 U.S. 868",
            "1987 U.S. LEXIS 2897",
            "55 U.S.L.W. 5156"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Welsh v. Wisconsin",
          "cluster_id": 111173,
          "cite": [
            "80 L. Ed. 2d 732",
            "104 S. Ct. 2091",
            "466 U.S. 740",
            "1984 U.S. LEXIS 82",
            "52 U.S.L.W. 4581"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Payton v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyllo v. United States",
          "cluster_id": 118443,
          "cite": [
            "150 L. Ed. 2d 94",
            "121 S. Ct. 2038",
            "533 U.S. 27",
            "2001 U.S. LEXIS 4487"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110235 OR 9427853 OR 9427854 OR 9427855 OR 9427856 OR 9427857) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTk5Njk2MDAwMDAwJnM9NDc4NDA1OCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110235+OR+9427853+OR+9427854+OR+9427855+OR+9427856+OR+9427857%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110235 OR 9427853 OR 9427854 OR 9427855 OR 9427856 OR 9427857)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTU4JnM9MTEyNzk1JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110235+OR+9427853+OR+9427854+OR+9427855+OR+9427856+OR+9427857%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110235 OR 9427853 OR 9427854 OR 9427855 OR 9427856 OR 9427857)",
        "reviewed": 117,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 117,
        "triage_read": 1,
        "triage_snippet_classified": 116
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110235 OR 9427853 OR 9427854 OR 9427855 OR 9427856 OR 9427857)",
    "indexed_citing_opinions": 4710,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110235,
        "count": 4214,
        "count_source": "search"
      },
      {
        "opinion_id": 9427853,
        "count": 568,
        "count_source": "search"
      },
      {
        "opinion_id": 9427854,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427855,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427856,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427857,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 7628,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/payton-v-new-york.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk1NDM0OTUmcz0xMDY3MzE4MiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110235+OR+9427853+OR+9427854+OR+9427855+OR+9427856+OR+9427857%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110235,
        "cited_id": 91470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 93880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 95265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 105925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 107718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 109352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 224194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 292572,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 292629,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 293653,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 301708,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 303979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 317251,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 348416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 354014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 354259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 358848,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 369038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1185860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1218237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1369726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1396585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1435637,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1442643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1527202,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1723936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1775149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1806892,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1836490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1860990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1927633,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1948493,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 2017555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 2064787,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 2106646,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 2226234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 2233048,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 2295125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 2583592,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 2616403,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 3953469,
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
    "date_created": "2026-07-05T16:36:39Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:36:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:36:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:40:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:36:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Payton v. New York (truncated)

```
<div>
<center><b><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U.S. 573</a></span> (1980)</b></center>
<center><h1>PAYTON<br>
v.<br>
NEW YORK.</h1></center>
<center>No. 78-5420.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 26, 1979.</center>
<center>Reargued October 9, 1979.</center>
<center>Decided April 15, 1980.<sup>[*]</sup></center>
APPEAL FROM THE COURT OF APPEALS OF NEW YORK.
<p><span class="star-pagination">*574</span> <i>William E. Hellerstein</i> reargued the cause for appellants in both cases. With him on the briefs was <i>David A. Lewis.</i></p>
<p><i>Peter L. Zimroth</i> reargued the cause for appellee in both cases. With him on the briefs were <i>John J. Santucci, Henry J. Steinglass, Brian Rosner,</i> and <i>Vivian Berger.</i></p>
<p>MR. JUSTICE STEVENS delivered the opinion of the Court.</p>
<p>These appeals challenge the constitutionality of New York statutes that authorize police officers to enter a private residence without a warrant and with force, if necessary, to make a routine felony arrest.</p>
<p>The important constitutional question presented by this challenge has been expressly left open in a number of our prior opinions. In <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span>, we upheld a warrantless "midday public arrest," expressly noting that the case did not pose "the still unsettled question <span class="star-pagination">*575</span>. . . `whether and under what circumstances an officer may enter a suspect's home to make a warrantless arrest.'" <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#418" aria-description="Citation for case: United States v. Watson"><i>Id.,</i> at 418, n. 6</a></span>.<sup>[1]</sup> The question has been answered in different ways by other appellate courts. The Supreme Court of Florida rejected the constitutional attack,<sup>[2]</sup> as did the New York Court of Appeals in this case. The courts of last resort in 10 other States, however, have held that unless special circumstances are present, warrantless arrests in the home are unconstitutional.<sup>[3]</sup> Of the seven United States Courts of Appeals that have considered the question, five have expressed the opinion that such arrests are unconstitutional.<sup>[4]</sup></p>
<p><span class="star-pagination">*576</span> Last Term we noted probable jurisdiction of these appeals in order to address that question. <span class="citation multiple-matches"><a href="/c/U.%20S./439/1044/">439 U. S. 1044</a></span>. After hearing oral argument, we set the case for reargument this Term. <span class="citation multiple-matches"><a href="/c/U.%20S./441/930/">441 U. S. 930</a></span>. We now reverse the New York Court of Appeals and hold that the Fourth Amendment to the United States Constitution, made applicable to the States by the Fourteenth Amendment, <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>; <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>, prohibits the police from making a warrantless and nonconsensual entry into a suspect's home in order to make a routine felony arrest.</p>
<p>We first state the facts of both cases in some detail and put to one side certain related questions that are not presented by these records. We then explain why the New York statutes are not consistent with the Fourth Amendment and why the reasons for upholding warrantless arrests in a public place do not apply to warrantless invasions of the privacy of the home.</p>
<p></p>
<h2>I</h2>
<p>On January 14, 1970, after two days of intensive investigation, New York detectives had assembled evidence sufficient to establish probable cause to believe that Theodore Payton had murdered the manager of a gas station two days earlier. At about 7:30 a. m. on January 15, six officers went to Payton's apartment in the Bronx, intending to arrest him. They had not obtained a warrant. Although light and music emanated from the apartment, there was no response to their knock on the metal door. They summoned emergency assistance and, about 30 minutes later, used crowbars to break open the door and enter the apartment. No one was there. In plain view, however, was a .30-caliber shell casing that was <span class="star-pagination">*577</span> seized and later admitted into evidence at Payton's murder trial.<sup>[5]</sup></p>
<p>In due course Payton surrendered to the police, was indicted for murder, and moved to suppress the evidence taken from his apartment. The trial judge held that the warrantless and forcible entry was authorized by the New York Code of Criminal Procedure,<sup>[6]</sup> and that the evidence in plain view was properly seized. He found that exigent circumstances justified the officers' failure to announce their purpose before entering the apartment as required by the statute.<sup>[7]</sup> He had no <span class="star-pagination">*578</span> occasion, however, to decide whether those circumstances also would have justified the failure to obtain a warrant, because he concluded that the warrantless entry was adequately supported by the statute without regard to the circumstances. The Appellate Division, First Department, summarily affirmed.<sup>[8]</sup></p>
<p>On March 14, 1974, Obie Riddick was arrested for the commission of two armed robberies that had occurred in 1971. He had been identified by the victims in June 1973, and in January 1974 the police had learned his address. They did not obtain a warrant for his arrest. At about noon on March 14, a detective, accompanied by three other officers, knocked on the door of the Queens house where Riddick was living. When his young son opened the door, they could see Riddick sitting in bed covered by a sheet. They entered the house and placed him under arrest. Before permitting him to dress, they opened a chest of drawers two feet from the bed in search of weapons and found narcotics and related paraphernalia. Riddick was subsequently indicted on narcotics charges. At a suppression hearing, the trial judge held that the warrantless entry into his home was authorized by the revised New York statute,<sup>[9]</sup> and that the search of the immediate <span class="star-pagination">*579</span> area was reasonable under <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>.<sup>[10]</sup> The Appellate Division, Second Department, affirmed the denial of the suppression motion.<sup>[11]</sup></p>
<p>The New York Court of Appeals, in a single opinion, affirmed the convictions of both Payton and Riddick. 45 N. Y. 2d 300, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/" aria-description="Citation for case: People v. Payton">380 N. E. 2d 224</a></span> (1978). The court recognized that the question whether and under what circumstances an officer may enter a suspect's home to make a warrantless arrest had not been settled either by that court or by this Court.<sup>[12]</sup> In answering that question, the majority of four judges relied primarily on its perception that there is a</p>
<blockquote>". . . substantial difference between the intrusion which attends an entry for the purpose of searching the premises and that which results from an entry for the purpose of <span class="star-pagination">*580</span> making an arrest, and [a] significant difference in the governmental interest in achieving the objective of the intrusion in the two instances." <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#310" aria-description="Citation for case: People v. Payton"><i>Id.,</i> at 310</a></span>, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#228" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 228-229</a></span>.<sup>[13]</sup></blockquote>
<p><span class="star-pagination">*581</span> The majority supported its holding by noting the "apparent historical acceptance" of warrantless entries to make felony arrests, both in the English common law and in the practice of many American States.<sup>[14]</sup></p>
<p>Three members of the New York Court of Appeals dissented on this issue because they believed that the Constitution requires the police to obtain a "warrant to enter a home in order to arrest or seize a person, unless there are exigent circumstances."<sup>[15]</sup> Starting from the premise that, except in carefully circumscribed instances, "the Fourth Amendment forbids police entry into a private home to search for and seize an object without a warrant,"<sup>[16]</sup> the dissenters reasoned that an arrest of the person involves an even greater invasion of privacy and should therefore be attended with at least as <span class="star-pagination">*582</span> great a measure of constitutional protection.<sup>[17]</sup> The dissenters noted "the existence of statutes and the American Law Institute imprimatur codifying the common-law rule authorizing warrantless arrests in private homes" and acknowledged that "the statutory authority of a police officer to make a warrantless arrest in this State has been in effect for almost 100 years," but concluded that "neither antiquity nor legislative unanimity can be determinative of the grave constitutional question presented" and "can never be a substitute for reasoned analysis."<sup>[18]</sup></p>
<p>Before addressing the narrow question presented by these appeals,<sup>[19]</sup> we put to one side other related problems that are <span class="star-pagination">*583</span> <i>not</i> presented today. Although it is arguable that the warrantless entry to effect Payton's arrest might have been justified by exigent circumstances, none of the New York courts relied on any such justification. The Court of Appeals majority treated both Payton's and Riddick's cases as involving routine arrests in which there was ample time to obtain a warrant,<sup>[20]</sup> and we will do the same. Accordingly, we have no occasion to consider the sort of emergency or dangerous situation, described in our cases as "exigent circumstances," that would justify a warrantless entry into a home for the purpose of either arrest or search.</p>
<p>Nor do these cases raise any question concerning the authority of the police, without either a search or arrest warrant, to enter a third party's home to arrest a suspect. The police broke into Payton's apartment intending to arrest Payton, and they arrested Riddick in his own dwelling. We also note that in neither case is it argued that the police lacked probable cause to believe that the suspect was at home when they entered. Finally, in both cases we are dealing with entries into homes made without the consent of any occupant. In <i>Payton,</i> the police used crowbars to break down the door and in <i>Riddick,</i> although his 3-year-old son answered the door; the police entered before Riddick had an opportunity either to object or to consent.</p>
<p></p>
<h2>II</h2>
<p>It is familiar history that indiscriminate searches and seizures conducted under the authority of "general warrants" were the immediate evils that motivated the framing and adoption of the Fourth Amendment.<sup>[21]</sup> Indeed, as originally <span class="star-pagination">*584</span> proposed in the House of Representatives, the draft contained only one clause, which directly imposed limitations on the issuance of warrants, but imposed no express restrictions on warrantless searches or seizures.<sup>[22]</sup> As it was ultimately adopted, however, the Amendment contained two separate clauses, the first protecting the basic right to be free from unreasonable searches and seizures and the second requiring that warrants be particular and supported by probable cause.<sup>[23]</sup> The Amendment provides:</p>
<blockquote>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches <span class="star-pagination">*585</span> and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</blockquote>
<p>It is thus perfectly clear that the evil the Amendment was designed to prevent was broader than the abuse of a general warrant. Unreasonable searches or seizures conducted without any warrant at all are condemned by the plain language of the first clause of the Amendment. Almost a century ago the Court stated in resounding terms that the principles reflected in the Amendment "reached farther than the concrete form" of the specific cases that gave it birth, and "apply to all invasions on the part of the government and its employees of the sanctity of a man's home and the privacies of life." <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span>. Without pausing to consider whether that broad language may require some qualification, it is sufficient to note that the warrantless arrest of a person is a species of seizure required by the Amendment to be reasonable. <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span>. Cf. <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648</a></span>. Indeed, as MR. JUSTICE POWELL noted in his concurrence in <i>United States</i> v. <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i><i>,</i> the arrest of a person is "quintessentially a seizure." <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#428" aria-description="Citation for case: United States v. Watson">423 U. S., at 428</a></span>.</p>
<p>The simple language of the Amendment applies equally to seizures of persons and to seizures of property. Our analysis in this case may therefore properly commence with rules that have been well established in Fourth Amendment litigation involving tangible items. As the Court reiterated just a few years ago, the "physical entry of the home is the chief evil against which the wording of the Fourth Amendment is directed." <i>United States</i> v. <i>United States District Court,</i> <span class="star-pagination">*586</span> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span>. And we have long adhered to the view that the warrant procedure minimizes the danger of needless intrusions of that sort.<sup>[24]</sup></p>
<p>It is a "basic principle of Fourth Amendment law" that searches and seizures inside a home without a warrant are presumptively unreasonable.<sup>[25]</sup> Yet it is also well settled that <span class="star-pagination">*587</span> objects such as weapons or contraband found in a public place may be seized by the police without a warrant. The seizure of property in plain view involves no invasion of privacy and is presumptively reasonable, assuming that there is probable cause to associate the property with criminal activity. The distinction between a warrantless seizure in an open area and such a seizure on private premises was plainly stated in <i>G. M. Leasing Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338</a></span>, 354:</p>
<blockquote>"It is one thing to seize without a warrant property resting in an open area or seizable by levy without an intrusion into privacy, and it is quite another thing to effect a warrantless seizure of property, even that owned by a corporation, situated on private premises to which access is not otherwise available for the seizing officer."</blockquote>
<p>As the late Judge Leventhal recognized, this distinction has equal force when the seizure of a person is involved. Writing on the constitutional issue now before us for the United States Court of Appeals for the District of Columbia Circuit sitting en banc, <i>Dorman</i> v. <i>United States,</i> 140 U. S. App. D. C. 313, <span class="citation" data-id="9456306"><a href="/opinion/293653/harold-b-dorman-v-united-states/" aria-description="Citation for case: Harold B. Dorman v. United States">435 F. 2d 385</a></span> (1970), Judge Leventhal first noted the settled rule that warrantless arrests in public places are valid. He immediately recognized, however, that</p>
<blockquote>"[a] greater burden is placed . . . on officials who enter a home or dwelling without consent. Freedom from intrusion into the home or dwelling is the archetype of the privacy protection secured by the Fourth Amendment." <i>Id.,</i> at 317, <span class="citation" data-id="9456306"><a href="/opinion/293653/harold-b-dorman-v-united-states/#389" aria-description="Citation for case: Harold B. Dorman v. United States">435 F. 2d, at 389</a></span>. (Footnote omitted.)</blockquote>
<p>His analysis of this question then focused on the long-settled premise that, absent exigent circumstances, a warrantless <span class="star-pagination">*588</span> entry to search for weapons or contraband is unconstitutional even when a felony has been committed and there is probable cause to believe that incriminating evidence will be found within.<sup>[26]</sup> He reasoned that the constitutional protection afforded to the individual's interest in the privacy of his own home is equally applicable to a warrantless entry for the purpose of arresting a resident of the house; for it is inherent in such an entry that a search for the suspect may be required before he can be apprehended.<sup>[27]</sup> Judge Leventhal concluded that an entry to arrest and an entry to search for and to seize property implicate the same interest in preserving the privacy and the sanctity of the home, and justify the same level of constitutional protection.</p>
<p>This reasoning has been followed in other Circuits.<sup>[28]</sup> Thus, the Second Circuit recently summarized its position:</p>
<blockquote>"To be arrested in the home involves not only the invasion <span class="star-pagination">*589</span> attendant to all arrests but also an invasion of the sanctity of the home. This is simply too substantial an invasion to allow without a warrant, at least in the absence of exigent circumstances, even when it is accomplished under statutory authority and when probable cause is clearly present." <i>United States</i> v. <i>Reed,</i> <span class="citation" data-id="354014"><a href="/opinion/354014/united-states-v-nancy-reed-and-morris-goldsmith-aka-marlowe/#423" aria-description="Citation for case: United States v. Nancy Reed and Morris Goldsmith, A/K/A...">572 F. 2d 412, 423</a></span> (1978), cert. denied <i>sub nom. </i><i>Goldsmith</i> v. <i>United States,</i> <span class="citation" data-id="9013020"><a href="/opinion/9019821/goldsmith-v-united-states/" aria-description="Citation for case: Goldsmith v. United States">439 U. S. 913</a></span>.</blockquote>
<p>We find this reasoning to be persuasive and in accord with this Court's Fourth Amendment decisions.</p>
<p>The majority of the New York Court of Appeals, however, suggested that there is a substantial difference in the relative intrusiveness of an entry to search for property and an entry to search for a person. See n. 13, <i>supra.</i> It is true that the area that may legally be searched is broader when executing a search warrant than when executing an arrest warrant in the home. See <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>. This difference may be more theoretical than real, however, because the police may need to check the entire premises for safety reasons, and sometimes they ignore the restrictions on searches incident to arrest.<sup>[29]</sup></p>
<p>But the critical point is that any differences in the intrusiveness of entries to search and entries to arrest are merely ones of degree rather than kind. The two intrusions share this fundamental characteristic: the breach of the entrance to an individual's home. The Fourth Amendment protects the individual's privacy in a variety of settings. In none is the zone of privacy more clearly defined than when bounded by the unambiguous physical dimensions of an individual's homeâ  a zone that finds its roots in clear and specific constitutional terms: "The right of the people to be secure in their . . . houses . . . shall not be violated." That language unequivocally establishes the proposition that "[a]t the very <span class="star-pagination">*590</span> core [of the Fourth Amendment] stands the right of a man to retreat into his own home and there be free from unreasonable governmental intrusion." <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511</a></span>. In terms that apply equally to seizures of property and to seizures of persons, the Fourth Amendment has drawn a firm line at the entrance to the house. Absent exigent circumstances, that threshold may not reasonably be crossed without a warrant.</p>
<p></p>
<h2>III</h2>
<p>Without contending that <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span>, decided the question presented by these appeals, New York argues that the reasons that support the <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i> holding require a similar result here. In <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i> the Court relied on (a) the well-settled common-law rule that a warrantless arrest in a public place is valid if the arresting officer had probable cause to believe the suspect is a felon;<sup>[30]</sup> (b) the clear consensus among the States adhering to that well-settled common-law rule;<sup>[31]</sup> and (c) the expression of the judgment of Congress that such an arrest is "reasonable."<sup>[32]</sup> We consider <span class="star-pagination">*591</span> each of these reasons as it applies to a warrantless entry into a home for the purpose of making a routine felony arrest.</p>
<p></p>
<h2>A</h2>
<p>An examination of the common-law understanding of an officer's authority to arrest sheds light on the obviously relevant, if not entirely dispositive,<sup>[33]</sup> consideration of what the Framers of the Amendment might have thought to be reasonable. Initially, it should be noted that the common-law rules of arrest developed in legal contexts that substantially differ from the cases now before us. In these cases, which involve application of the exclusionary rule, the issue is whether certain <span class="star-pagination">*592</span> evidence is admissible at trial.<sup>[34]</sup> See <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>. At common law, the question whether an arrest was authorized typically arose in civil damages actions for trespass or false arrest, in which a constable's authority to make the arrest was a defense. See, <i>e. g., </i><i>Leach</i> v. <i>Money,</i> 19 How. St. Tr. 1001, 97 Eng. Rep. 1075 (K. B. 1765). Additionally, if an officer was killed while attempting to effect an arrest, the question whether the person resisting the arrest was guilty of murder or manslaughter turned on whether the officer was acting within the bounds of his authority. See M. Foster, Crown Law 308, 312 (1762). See also <i>West</i> v. <i>Cabell,</i> <span class="citation" data-id="93880"><a href="/opinion/93880/west-v-cabell/#85" aria-description="Citation for case: West v. Cabell">153 U. S. 78, 85</a></span>.</p>
<p>A study of the common law on the question whether a constable had the authority to make warrantless arrests in the home on mere suspicion of a felonyâ  as distinguished from an officer's right to arrest for a crime committed in his presenceâ   reveals a surprising lack of judicial decisions and a deep divergence among scholars.</p>
<p>The most cited evidence of the common-law rule consists of an equivocal dictum in a case actually involving the sheriff's authority to enter a home to effect service of civil process. In <i>Semayne's Case,</i> 5 Co. Rep. 91a, 91b, 77 Eng. Rep. 194, 195-196 (K. B. 1603), the Court stated:</p>
<blockquote>"In all cases when the King is party, the Sheriff (if the doors be not open) may break the party's house, either to arrest him, or to do other execution of the K.'s process, if otherwise he cannot enter. But before he breaks it, he ought to signify the cause of his coming, and to make request to open doors; and that appears well by the stat. of Westm. 1. c. 17. (which is but an affirmance of the common law) as hereafter appears, for the law without a default in the owner abhors the destruction <span class="star-pagination">*593</span> or breaking of any house (which is for the habitation and safety of man) by which great damage and inconvenience might ensue to the party, when no default is in him; for perhaps he did not know of the process, of which, if he had notice, it is to be presumed that he would obey it, and that appears by the book in 18 E. 2. Execut. 252. where it is said, that the K's officer who comes to do execution, &amp;c. may open the doors which are shut, and break them, if he cannot have the keys; which proves, that he ought first to demand them, 7 E. 3. 16." (Footnotes omitted.)</blockquote>
<p>This passage has been read by some as describing an entry without a warrant. The context strongly implies, however, that the court was describing the extent of authority in executing the King's writ. This reading is confirmed by the phrase "either to arrest him, or to do <i>other</i> execution of the K.'s process" and by the further point that notice was necessary because the owner may "not know of the <i>process."</i> In any event, the passage surely cannot be said unambiguously to endorse warrantless entries.</p>
<p>The common-law commentators disagreed sharply on the subject.<sup>[35]</sup> Three distinct views were expressed. Lord Coke, <span class="star-pagination">*594</span> widely recognized by the American colonists "as the greatest authority of his time on the laws of England,"<sup>[36]</sup> clearly viewed a warrantless entry for the purpose of arrest to be illegal.<sup>[37]</sup><span class="star-pagination">*595</span> Burn, Foster, and Hawkins agreed,<sup>[38]</sup> as did East and Russell, though the latter two qualified their opinions by stating that if an entry to arrest was made without a warrant, the officer was perhaps immune from liability for the trespass if the suspect was actually guilty.<sup>[39]</sup> Blackstone, Chitty, and Stephen took the opposite view, that entry to arrest without a warrant was legal,<sup>[40]</sup> though Stephen relied on Blackstone who, along with Chitty, in turn relied exclusively on Hale. But Hale's view was not quite so unequivocally expressed.<sup>[41]</sup><span class="star-pagination">*596</span> Further, Hale appears to rely solely on a statement in an early Yearbook, quoted in <i>Burdett</i> v. <i>Abbot,</i> 14 East 1, 155, 104 Eng. Rep. 501, 560 (K. B. 1811):<sup>[42]</sup></p>
<blockquote>"`that for felony, or suspicion of felony, a man may break open the house to take the felon; for it is for the commonweal to take them.'"</blockquote>
<p>Considering the diversity of views just described, however, it is clear that the statement was never deemed authoritative. Indeed, in <i>Burdett,</i> the statement was described as an "extra-judicial opinion." <i><span class="citation" data-id="93880"><a href="/opinion/93880/west-v-cabell/" aria-description="Citation for case: West v. Cabell">Ibid.</a></span></i><sup>[43]</sup></p>
<p>It is obvious that the common-law rule on warrantless home arrests was not as clear as the rule on arrests in public places. Indeed, particularly considering the prominence of Lord Coke, the weight of authority as it appeared to the Framers was to the effect that a warrant was required, or at the minimum that there were substantial risks in proceeding without one. The common-law sources display a sensitivity to privacy interests that could not have been lost on the Framers. The zealous and frequent repetition of the adage that a "man's house is his castle," made it abundantly clear that both in England<sup>[44]</sup><span class="star-pagination">*597</span> and in the Colonies "the freedom of one's house" was one of the most vital elements of English liberty.<sup>[45]</sup></p>
<p>Thus, our study of the relevant common law does not provide the same guidance that was present in <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span>.</i> Whereas <span class="star-pagination">*598</span> the rule concerning the validity of an arrest in a public place was supported by cases directly in point and by the unanimous views of the commentators, we have found no direct authority supporting forcible entries into a home to make a routine arrest and the weight of the scholarly opinion is somewhat to the contrary. Indeed, the absence of any 17th- or 18th-century English cases directly in point, together with the unequivocal endorsement of the tenet that "a man's house is his castle," strongly suggests that the prevailing practice was not to make such arrests except in hot pursuit or when authorized by a warrant. Cf. <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span>. In all events, the issue is not one that can be said to have been definitively settled by the common law at the time the Fourth Amendment was adopted.</p>
<p></p>
<h2>B</h2>
<p>A majority of the States that have taken a position on the question permit warrantless entry into the home to arrest even in the absence of exigent circumstances. At this time, 24 States permit such warrantless entries;<sup>[46]</sup> 15 States clearly <span class="star-pagination">*599</span> prohibit them, though 3 States do so on federal constitutional grounds alone;<sup>[47]</sup> and 11 States have apparently taken no position on the question.<sup>[48]</sup></p>
<p>But these current figures reflect a significant decline during the last decade in the number of States permitting warrantless entries for arrest. Recent dicta in this Court raising questions about the practice, see n. 1, <i>supra,</i> and Federal Courts of Appeals' decisions on point, see n. 4, <i>supra,</i> have led state courts to focus on the issue. Virtually all of the state courts that have had to confront the constitutional issue directly have held warrantless entries into the home to arrest to be invalid in the absence of exigent circumstances. See nn. 2, 3, <i>supra.</i> Three state courts have relied on Fourth Amendment <span class="star-pagination">*600</span> grounds alone, while seven have squarely placed their decisions on both federal and state constitutional grounds.<sup>[49]</sup> A number of other state courts, though not having had to confront the issue directly, have recognized the serious nature of the constitutional question.<sup>[50]</sup> Apparently, only the Supreme Court of Florida and the New York Court of Appeals in this case have expressly upheld warrantless entries to arrest in the face of a constitutional challenge.<sup>[51]</sup></p>
<p>A longstanding, widespread practice is not immune from constitutional scrutiny. But neither is it to be lightly brushed aside. This is particularly so when the constitutional standard is as amorphous as the word "reasonable," and when custom and contemporary norms necessarily play such a large role in the constitutional analysis. In this case, although the weight of state-law authority is clear, there is by no means the kind of virtual unanimity on this question that was present in <i>United States</i> v. <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i><i>,</i> with regard to warrantless arrests in public places. See <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#422" aria-description="Citation for case: United States v. Watson">423 U. S., at 422-423</a></span>. Only 24 of the 50 States currently sanction warrantless entries into the home to arrest, see nn. 46-48, <i>supra,</i> and there is an obvious declining trend. Further, the strength of the trend is greater than the numbers alone indicate. Seven state courts have recently held that warrantless home arrests violate their respective <i>State</i> Constitutions. See n. 3, <i>supra.</i> That is significant because by invoking a state constitutional provision, a state court immunizes its decision from review by this Court.<sup>[52]</sup> This heightened degree of immutability underscores the depth of the principle underlying the result.</p>
<p></p>
<h2>
<span class="star-pagination">*601</span> C</h2>
<p>No congressional determination that warrantless entries into the home are "reasonable" has been called to our attention. None of the federal statutes cited in the <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i> opinion reflects any such legislative judgment.<sup>[53]</sup> Thus, that support for the <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i> holding finds no counterpart in this case.</p>
<p>MR. JUSTICE POWELL, concurring in <i>United States</i> v. <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#429" aria-description="Citation for case: United States v. Watson"><i>Watson, supra,</i> at 429</a></span>, stated:</p>
<blockquote>"But logic sometimes must defer to history and experience. The Court's opinion emphasizes the historical sanction accorded warrantless felony arrests [in public places]."</blockquote>
<p>In this case, however, neither history nor this Nation's experience requires us to disregard the overriding respect for the sanctity of the home that has been embedded in our traditions since the origins of the Republic.<sup>[54]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*602</span> IV</h2>
<p>The parties have argued at some length about the practical consequences of a warrant requirement as a precondition to a felony arrest in the home.<sup>[55]</sup> In the absence of any evidence that effective law enforcement has suffered in those States that already have such a requirement, see nn. 3, 47, <i>supra,</i> we are inclined to view such arguments with skepticism. More fundamentally, however, such arguments of policy must give way to a constitutional command that we consider to be unequivocal.</p>
<p>Finally, we note the State's suggestion that only a search warrant based on probable cause to believe the suspect is at home at a given time can adequately protect the privacy interests at stake, and since such a warrant requirement is manifestly impractical, there need be no warrant of any kind. We find this ingenious argument unpersuasive. It is true that an arrest warrant requirement may afford less protection than a search warrant requirement, but it will suffice to interpose the magistrate's determination of probable cause between the zealous officer and the citizen. If there is sufficient evidence of a citizen's participation in a felony to persuade a judicial officer that his arrest is justified, it is constitutionally reasonable <span class="star-pagination">*603</span> to require him to open his doors to the officers of the law. Thus, for Fourth Amendment purposes, an arrest warrant founded on probable cause implicitly carries with it the limited authority to enter a dwelling in which the suspect lives when there is reason to believe the suspect is within.</p>
<p>Because no arrest warrant was obtained in either of these cases, the judgments must be reversed and the cases remanded to the New York Court of Appeals for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE BLACKMUN, concurring.</p>
<p>I joined the Court's opinion in <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976), upholding, on probable cause, the warrantless arrest in a public place. I, of course, am still of the view that the decision in <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i> is correct. The Court's balancing of the competing governmental and individual interests properly occasioned that result. Where, however, the warrantless arrest is in the suspect's home, that same balancing requires that, absent exigent circumstances, the result be the other way. The suspect's interest in the sanctity of his home then outweighs the governmental interests.</p>
<p>I therefore join the Court's opinion, firm in the conviction that the result in <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i> and the result here, although opposite, are fully justified by history and by the Fourth Amendment.</p>
<p>MR. JUSTICE WHITE, with whom THE CHIEF JUSTICE and MR. JUSTICE REHNQUIST join, dissenting.</p>
<p>The Court today holds that absent exigent circumstances officers may never enter a home during the daytime to arrest for a dangerous felony unless they have first obtained a warrant. This hard-and-fast rule, founded on erroneous assumptions concerning the intrusiveness of home arrest entries, <span class="star-pagination">*604</span> finds little or no support in the common law or in the text and history of the Fourth Amendment. I respectfully dissent.</p>
<p></p>
<h2>I</h2>
<p>As the Court notes, <i>ante,</i> at 591, the common law of searches and seizures, as evolved in England, as transported to the Colonies, and as developed among the States, is highly relevant to the present scope of the Fourth Amendment. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#418" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 418-422</a></span> (1976); <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#425" aria-description="Citation for case: United States v. Watson"><i>id.,</i> at 425, 429</a></span> (POWELL, J., concurring); <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#111" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 111, 114</a></span> (1975); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 149-153</a></span> (1925); <i>Bad Elk</i> v. <i>United States,</i> <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/#534" aria-description="Citation for case: Bad Elk v. United States">177 U. S. 529, 534-535</a></span> (1900); <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#622" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 622-630</a></span> (1886); <i>Kurtz</i> v. <i>Moffitt,</i> <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/#498" aria-description="Citation for case: Kurtz v. Moffitt">115 U. S. 487, 498-499</a></span> (1885). Today's decision virtually ignores these centuries of common-law development, and distorts the historical meaning of the Fourth Amendment, by proclaiming for the first time a rigid warrant requirement for all nonexigent home arrest entries.</p>
<p></p>
<h2>A</h2>
<p>As early as the 15th century the common law had limited the Crown's power to invade a private dwelling in order to arrest. A Year Book case of 1455 held that in civil cases the sheriff could not break doors to arrest for debt or trespass, for the arrest was then only in the private interests of a party. Y. B. 13 Edw. IV, 9a. To the same effect is <i>Semayne's Case,</i> 5 Co. Rep. 91a, 77 Eng. Rep. 194 (K. B. 1603). The holdings of these cases were condensed in the maxim that "every man's house is his castle." H. Broom, Legal Maxims *321-*329.</p>
<p>However, this limitation on the Crown's power applied only to private civil actions. In cases directly involving the Crown, the rule was that "[t]he king's keys unlock all doors." Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 798</span>, 800 (1924). The Year Book case cited above stated a different rule for criminal cases: for a felony, or suspicion of felony, one may break into the dwelling house to take the felon, for <span class="star-pagination">*605</span> it is for the common weal and to the interest of the King to take him. Likewise, <i>Semayne's Case</i> stated in dictum:</p>
<blockquote>"In all cases when the King is party, the Sheriff (if the doors be not open) may break the party's house, either to arrest him, or to do other execution of the K[ing]'s process, if otherwise he cannot enter." 5 Co. Rep., at 91b, 77 Eng. Rep., at 195.</blockquote>
<p>Although these cases established the Crown's power to enter a dwelling in criminal cases, they did not directly address the question of whether a constable could break doors to arrest without authorization by a warrant. At common law, the constable's office was twofold. As conservator of the peace, he possessed, <i>virtute officii,</i> a "great original and inherent authority with regard to arrests," 4 W. Blackstone, Commentaries *292 (hereinafter Blackstone), and could "without any other warrant but from [himself] arrest felons, and those that [were] probably suspected of felonies," 2 M. Hale, Pleas of the Crown 85 (1736) (hereinafter Hale); see <i>United States</i> v. <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#418" aria-description="Citation for case: United States v. Watson"><i>Watson, supra,</i> at 418-419</a></span>. Second, as a subordinate public official, the constable performed ministerial tasks under the authorization and direction of superior officers. See 1 R. Burn, The Justice of the Peace and Parish Officer 295 (6th ed. 1758) (hereinafter Burn); 2 W. Hawkins, Pleas of the Crown 130-132 (6th ed. 1787) (hereinafter Hawkins). It was in this capacity that the constable executed warrants issued by justices of the peace. The warrant authorized the constable to take action beyond his inherent powers.<sup>[1]</sup> It also ensured that he actually carried out his instructions, by giving him clear notice of his duty, for the breach of which he could be punished, 4 Blackstone *291; 1 Burn 295; 2 Hale 88, and by relieving him from civil liability even if probable cause to <span class="star-pagination">*606</span> arrest were lacking, 4 Blackstone *291; 1 Burn 295-296; M. Dalton, The Country Justice 579 (1727 ed.) (hereinafter Dalton); 2 Hawkins 132-133. For this reason, warrants were sometimes issued even when the act commanded was within the constable's inherent authority. Dalton 576.</p>
<p>As the Court notes, commentators have differed as to the scope of the constable's inherent authority, when not acting under a warrant, to break doors in order to arrest. Probably the majority of commentators would permit arrest entries on probable suspicion even if the person arrested were not in fact guilty. 4 Blackstone *292; 1 Burn 87-88;<sup>[2]</sup> 1 J. Chitty, Criminal Law 23 (1816) (hereinafter Chitty); Dalton 426; 1 Hale 583; 2 <i>id.,</i> at 90-94. These authors, in short, would have permitted the type of home arrest entries that occurred in the present cases. The inclusion of Blackstone in this list is particularly significant in light of his profound impact on the minds of the colonists at the time of the framing of the Constitution and the ratification of the Bill of Rights.</p>
<p>A second school of thought, on which the Court relies, held that the constable could not break doors on mere "bare suspicion." M. Foster, Crown Law 321 (1762); 2 Hawkins 139; 1 E. East, Pleas of the Crown 321-322 (1806); 1 W. Russell, Treatise on Crimes and Misdemeanors 745 (1819) (hereinafter Russell). Cf. 4 E. Coke, Institutes *177. Although this doctrine <span class="star-pagination">*607</span> imposed somewhat greater limitations on the constable's inherent power, it does not support the Court's hard-and-fast rule against warrantless nonexigent home entries upon probable cause. East and Russell state explicitly what Foster and Hawkins imply: although mere "bare suspicion" will not justify breaking doors, the constable's action would be justifiable if the person arrested were <i>in fact</i> guilty of a felony. These authorities can be read as imposing a somewhat more stringent requirement of probable cause for arrests in the home than for arrests elsewhere. But they would not bar nonexigent, warrantless home arrests in all circumstances, as the Court does today. And Coke is flatly contrary to the Court's rule requiring a warrant, since he believed that even a warrant would not justify an arrest entry until the suspect had been indicted.</p>
<p>Finally, it bears nothing that the doctrine against home entries on bare suspicion developed in a period in which the validity of <i>any</i> arrest on bare suspicionâ  even one occurring outside the homeâ  was open to question. Not until Lord Mansfield's decision in <i>Samuel</i> v. <i>Payne,</i> <span class="citation" data-id="6629715"><a href="/opinion/6747612/green-v-graves/" aria-description="Citation for case: Green v. Graves">1 Doug. 359</a></span>, 99 Eng. Rep. 230 (K. B. 1780), was it definitively established that the constable could arrest on suspicion even if it turned out that no felony had been committed. To the extent that the commentators relied on by the Court reasoned from any general rule against warrantless arrests based on bare suspicion, the rationale for their position did not survive <i>Samuel</i> v. <i><span class="citation" data-id="6629715"><a href="/opinion/6747612/green-v-graves/" aria-description="Citation for case: Green v. Graves">Payne</a></span></i><i>.</i></p>
<p></p>
<h2>B</h2>
<p>The history of the Fourth Amendment does not support the rule announced today. At the time that Amendment was adopted the constable possessed broad inherent powers to arrest. The limitations on those powers derived, not from a warrant "requirement," but from the generally ministerial nature of the constable's office at common law. Far from restricting the constable's arrest power, the institution of the <span class="star-pagination">*608</span> warrant was used to expand that authority by giving the constable delegated powers of a superior officer such as a justice of the peace. Hence at the time of the Bill of Rights, the warrant functioned as a powerful tool of law enforcement rather than as a protection for the rights of criminal suspects.</p>
<p>In fact, it was the abusive use of the warrant power, rather than any excessive zeal in the discharge of peace officers' inherent authority, that precipitated the Fourth Amendment. That Amendment grew out of colonial opposition to the infamous general warrants known as writs of assistance, which empowered customs officers to search at will, and to break open receptacles or packages, wherever they suspected uncustomed goods to be. <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#7" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 7-8</a></span> (1977); N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 51-78 (1937) (hereinafter Lasson). The writs did not specify where searches could occur and they remained effective throughout the sovereign's lifetime. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#54" aria-description="Citation for case: United States v. Chadwick"><i>Id.,</i> at 54</a></span>. In effect, the writs placed complete discretion in the hands of executing officials. Customs searches of this type were beyond the inherent power of common-law officials and were the subject of court suits when performed by colonial customs agents not acting pursuant to a writ. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#55" aria-description="Citation for case: United States v. Chadwick"><i>Id.,</i> at 55</a></span>.</p>
<p>The common law was the colonists' ally in their struggle against writs of assistance. Hale and Blackstone had condemned general warrants, 1 Hale 580; 4 Blackstone *291, and fresh in the colonists' minds were decisions granting recovery to parties arrested or searched under general warrants on suspicion of seditious libel. <i>Entick</i> v. <i>Carrington,</i> 19 How. St. Tr. 1029, 95 Eng. Rep. 807 (K. B. 1765); <i>Huckle</i> v. <i>Money,</i> 2 Wils. 205, 95 Eng. Rep. 768 (K. B. 1763); <i>Wilkes</i> v. <i>Wood,</i> 19 How. St. Tr. 1153, 98 Eng. Rep. 489 (K. B. 1763). When James Otis, Jr., delivered his courtroom oration against writs of assistance in 1761, he looked to the common law in asserting that the writs, if not construed specially, were void as a <span class="star-pagination">*609</span> form of general warrant. 2 Legal Papers of John Adams 139-144 (L. Wroth &amp; H. Zobel eds. 1965).<sup>[3]</sup></p>
<p>Given the colonists' high regard for the common law, it is indeed unlikely that the Framers of the Fourth Amendment intended to derogate from the constable's inherent commonlaw authority. Such an argument was rejected in the important early case of <i>Rohan</i> v. <i>Sawin,</i> <span class="citation no-link">59 Mass. 281</span>, 284-285 (1851):</p>
<blockquote>"It has been sometimes contended, that an arrest of this character, without a warrant, was a violation of the great fundamental principles of our national and state constitutions, forbidding unreasonable searches and arrests, except by warrant founded upon a complaint made under oath. Those provisions doubtless had another and different purpose, being in restraint of general warrants to make searches, and requiring warrants to issue only upon a complaint made under oath. They do not conflict with the authority of constables or other peace-officers. . . to arrest without warrant those who have committed felonies. The public safety, and the due apprehension of criminals, charged with heinous offences, imperiously require that such arrests should be made without warrant by officers of the law."<sup>[4]</sup></blockquote>
<p><span class="star-pagination">*610</span> That the Framers were concerned about warrants, and not about the constable's inherent power to arrest, is also evident from the text and legislative history of the Fourth Amendment. That provision first reaffirms the basic principle of common law, that "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated. . . ." The Amendment does not here purport to limit or restrict the peace officer's inherent power to arrest or search, but rather assumes an existing right against actions in excess of that inherent power and ensures that it remain inviolable. As I have noted, it was not generally considered "unreasonable" at common law for officers to break doors in making warrantless felony arrests. The Amendment's second clause is directed at the actions of officers taken in their ministerial capacity pursuant to writs of assistance and other warrants. In contrast to the first Clause, the second Clause does purport to alter colonial practice: "and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</p>
<p>That the Fourth Amendment was directed towards safeguarding the rights at common law, and restricting the warrant practice which gave officers vast new powers beyond their inherent authority, is evident from the legislative history of that provision. As originally drafted by James Madison, it was directed <i>only</i> at warrants; so deeply ingrained was the basic common-law premise that it was not even expressed:</p>
<blockquote>"The rights of the people to be secured in their persons[,] their houses, their papers, and their other property, from all unreasonable searches and seizures, shall not be violated by warrants issued without probable cause, supported by oath or affirmation, or not particularly describing the places to be searched, or the persons or things to be seized." 1 Annals of Cong. 452 (1789).</blockquote>
<p><span class="star-pagination">*611</span> The Committee of Eleven reported the provision as follows:</p>
<blockquote>"The right of the people to be secured in their persons, houses, papers, and effects, shall not be violated by warrants issuing without probable cause, supported by oath or affirmation, and not particularly describing the place to be searched, and the persons or things to be seized." <i>Id.,</i> at 783.</blockquote>
<p>The present language was adopted virtually at the last moment by the Committee of Three, which had been appointed only to arrange the Amendments rather than to make substantive changes in them. Lasson 101. The Amendment passed the House; but "the House seems never to have consciously agreed to the Amendment in its present form." <i>Ibid.</i> In any event, because the sanctity of the common-law protections was assumed from the start, it is evident that the change made by the Committee of Three was a cautionary measure without substantive content.</p>
<p>In sum, the background, text, and legislative history of the Fourth Amendment demonstrate that the purpose was to restrict the abuses that had developed with respect to warrants; the Amendment preserved common-law rules of arrest. Because it was not considered generally unreasonable at common law for officers to break doors to effect a warrantless felony arrest, I do not believe that the Fourth Amendment was intended to outlaw the types of police conduct at issue in the present cases.</p>
<p></p>
<h2>C</h2>
<p>Probably because warrantless arrest entries were so firmly accepted at common law, there is apparently no recorded constitutional challenge to such entries in the 19th-century cases. Common-law authorities on both sides of the Atlantic, however, continued to endorse the validity of such arrests. <i>E. g.,</i> 1 J. Bishop, Commentaries on the Law of Criminal Procedure §§ 195-199 (2d ed. 1872); 1 Chitty 23; 1 J. Colby, A Practical Treatise upon the Criminal Law and Practice of the State <span class="star-pagination">*612</span> of New York 73-74 (1868); F. Heard, A Practical Treatise on the Authority and Duties of Trial Justices, District, Police, and Municipal Courts, in Criminal Cases 135, 148 (1879); 1 Russell 745. Like their predecessors, these authorities conflicted as to whether the officer would be liable in damages if it were shown that the person arrested was not guilty of a felony. But all agreed that warrantless home entries would be permissible in at least some circumstances. None endorsed the rule of today's decision that a warrant is always required, absent exigent circumstances, to effect a home arrest.</p>
<p>Apparently the first official pronouncement on the validity of warrantless home arrests came with the adoption of state codes of criminal procedure in the latter 19th and early 20th centuries. The great majority of these codes accepted and endorsed the inherent authority of peace officers to enter dwellings in order to arrest felons. By 1931, 24 of 29 state codes authorized such warrantless arrest entries.<sup>[5]</sup> By 1975, 31 of 37 state codes authorized warrantless home felony arrests.<sup>[6]</sup> The American Law Institute included such authority in its model legislation in 1931 and again in 1975.<sup>[7]</sup></p>
<p>The first direct judicial holding on the subject of warrantless home arrests seems to have been <i>Commonwealth</i> v. <i>Phelps,</i> <span class="citation" data-id="6431509"><a href="/opinion/6557761/commonwealth-v-phelps/" aria-description="Citation for case: Commonwealth v. Phelps">209 Mass. 396</a></span>, <span class="citation" data-id="6431509"><a href="/opinion/6557761/commonwealth-v-phelps/" aria-description="Citation for case: Commonwealth v. Phelps">95 N. E. 868</a></span> (1911). The holding in this case that such entries were constitutional became the settled rule in the States for much of the rest of the century. See Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 798</span>, 803 (1924). Opinions of this Court also assumed that such arrests were constitutional.<sup>[8]</sup></p>
<p><span class="star-pagination">*613</span> This Court apparently first questioned the reasonableness of warrantless nonexigent entries to arrest in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499-500</a></span> (1958), noting in dictum that such entries would pose a "grave constitutional question" if carried out at night.<sup>[9]</sup> In <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#480" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 480</a></span> (1971), the Court stated, again in dictum:</p>
<blockquote>"[I]f [it] is correct that it has generally been assumed that the Fourth Amendment is not violated by the warrantless entry of a man's house for purposes of arrest, it might be wise to re-examine the assumption. Such a re-examination `would confront us with a grave constitutional question, namely, whether the forcible nighttime entry into a dwelling to arrest a person reasonably believed within, upon probable cause that he had committed a felony, under circumstances where no reason appears why an arrest warrant could not have been sought, is consistent with the Fourth Amendment.' <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S., at 499-500</a></span>."</blockquote>
<p>Although <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span></i> and <i><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> both referred to the special problem of warrantless entries during the nighttime,<sup>[10]</sup> it is not surprising that state and federal courts have tended to read those dicta as suggesting a broader infirmity applying to daytime entries also, and that the majority of recent decisions have been against the constitutionality of all types of warrantless, nonexigent home arrest entries. As the Court concedes, <span class="star-pagination">*614</span> however, even despite <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span></i> and <i><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> it remains the case that</p>
<blockquote>"[a] majority of the States that have taken a position on the question permit warrantless entry into the home to arrest even in the absence of exigent circumstances. At this time, 24 States permit such warrantless entries; 15 States clearly prohibit them, though 3 States do so on federal constitutional grounds alone; and 11 States have apparently taken no position on the question." <i>Ante,</i> at 598-599 (footnotes omitted).</blockquote>
<p>This consensus, in the face of seemingly contrary dicta from this Court, is entitled to more deference than the Court today provides. Cf. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976).</p>
<p></p>
<h2>D</h2>
<p>In the present cases, as in <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span>,</i> the applicable federal statutes are relevant to the reasonableness of the type of arrest in question. Under <span class="citation no-link">18 U. S. C. § 3052</span>, specified federal agents may "make arrests without warrants for any offense against the United States committed in their presence, or for any felony cognizable under the laws of the United States, if they have reasonable grounds to believe that the person to be arrested has committed or is committing such felony." On its face this provision authorizes federal agents to make warrantless arrests anywhere, including the home. Particularly in light of the accepted rule at common law and among the States permitting warrantless home arrests, the absence of any explicit exception for the home from § 3052 is persuasive evidence that Congress intended to authorize warrantless arrests there a well as elsewhere.</p>
<p>Further, Congress has not been unaware of the special problems involved in police entries into the home. In <span class="citation no-link">18 U. S. C. § 3109</span>, it provided that</p>
<blockquote>"[t]he officer may break open any outer or inner door or window of a house, or any part of a house, or anything <span class="star-pagination">*615</span> therein, to execute a search warrant, if, after notice of his authority and purpose, he is refused admittance. . . ."</blockquote>
<p>See <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">357 U. S. 301</a></span> (1958). In explicitly providing authority to enter when executing a search warrant, Congress surely did not intend to derogate from the officers' power to effect an arrest entry either with or without a warrant. Rather, Congress apparently assumed that this power was so firmly established either at common law or by statute that no explicit grant of arrest authority was required in § 3109. In short, although the Court purports to find no guidance in the relevant federal statutes, I believe that fairly read they authorize the type of police conduct at issue in these cases.</p>
<p></p>
<h2>II</h2>
<p></p>
<h2>A</h2>
<p>Today's decision rests, in large measure, on the premise that warrantless arrest entries constitute a particularly severe invasion of personal privacy. I do not dispute that the home is generally a very private area or that the common law displayed a special "reverence . . . for the individual's right of privacy in his house." <i>Miller</i> v. <i>United States, supra,</i> at 313. However, the Fourth Amendment is concerned with protecting people, not places, and no talismanic significance is given to the fact that an arrest occurs in the home rather than elsewhere. Cf. <i>Ybarra</i> v. <i>Illinois,</i> <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85</a></span> (1979); <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967); <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S., at 630</a></span>. It is necessary in each case to assess realistically the actual extent of invasion of constitutionally protected privacy. Further, as MR. JUSTICE POWELL observed in <i>United States</i> v. <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#428" aria-description="Citation for case: United States v. Watson"><i>Watson, supra,</i> at 428</a></span> (concurring opinion), all arrests involve serious intrusions into an individual's privacy and dignity. Yet we settled in <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i> that the intrusiveness of a public arrest is not enough to mandate the obtaining of a warrant. The inquiry in the present case, therefore, is whether the incremental <span class="star-pagination">*616</span> intrusiveness that results from an arrest's being made <i>in the dwelling</i> is enough to support an inflexible constitutional rule requiring warrants for such arrests whenever exigent circumstances are not present.</p>
<p>Today's decision ignores the carefully crafted restrictions on the common-law power of arrest entry and thereby overestimates the dangers inherent in that practice. At common law, absent exigent circumstances, entries to arrest could be made only for felony. Even in cases of felony, the officers were required to announce their presence, demand admission, and be refused entry before they were entitled to break doors.<sup>[11]</sup> Further, it seems generally accepted that entries could be made only during daylight hours.<sup>[12]</sup> And, in my view, the officer entering to arrest must have reasonable grounds to believe, not only that the arrestee has committed a crime, but also that the person suspected is present in the house at the time of the entry.<sup>[13]</sup></p>
<p>These four restrictions on home arrestsâ  felony, knock and announce, daytime, and stringent probable causeâ  constitute powerful and complementary protections for the privacy interests associated with the home. The felony requirement guards against abusive or arbitrary enforcement and ensures that invasions of the home occur only in case of the most <span class="star-pagination">*617</span> serious crimes. The knock-and-announce and daytime requirements protect individuals against the fear, humiliation, and embarrassment of being roused from their beds in states of partial or complete undress. And these requirements allow the arrestee to surrender at his front door, thereby maintaining his dignity and preventing the officers from entering other rooms of the dwelling. The stringent probable-cause requirement would help ensure against the possibility that the police would enter when the suspect was not home, and, in searching for him, frighten members of the family or ransack parts of the house, seizing items in plain view. In short, these requirements, taken together, permit an individual suspected of a serious crime to surrender at the front door of his dwelling and thereby avoid most of the humiliation and indignity that the Court seems to believe necessarily accompany a house arrest entry. Such a front-door arrest, in my view, is no more intrusive on personal privacy than the public warrantless arrests which we found to pass constitutional muster in <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span>.</i><sup>[14]</sup></p>
<p>All of these limitations on warrantless arrest entries are satisfied on the facts of the present cases. The arrests here were for serious feloniesâ  murder and armed robberyâ  and both occurred during daylight hours. The authorizing statutes required that the police announce their business and demand entry; neither Payton nor Riddick makes any contention that these statutory requirements were not fulfilled. And it is not argued that the police had no probable cause to believe that both Payton and Riddick were in their dwellings at the time of the entries. Today's decision, therefore, sweeps away any possibility that warrantless home entries might be permitted in some limited situations other than those in which <span class="star-pagination">*618</span> exigent circumstances are present. The Court substitutes, in one sweeping decision, a rigid constitutional rule in place of the common-law approach, evolved over hundreds of years, which achieved a flexible accommodation between the demands of personal privacy and the legitimate needs of law enforcement.</p>
<p>A rule permitting warrantless arrest entries would not pose a danger that officers would use their entry power as a pretext to justify an otherwise invalid warrantless search. A search pursuant to a warrantless arrest entry will rarely, if ever, be as complete as one under authority of a search warrant. If the suspect surrenders at the door, the officers may not enter other rooms. Of course, the suspect may flee or hide, or may not be at home, but the officers cannot anticipate the first two of these possibilities and the last is unlikely given the requirement of probable cause to believe that the suspect is at home. Even when officers are justified in searching other rooms, they may seize only items within the arrestee's possession or immediate control or items in plain view discovered during the course of a search reasonably directed at discovering a hiding suspect. Hence a warrantless home entry is likely to uncover far less evidence than a search conducted under authority of a search warrant. Furthermore, an arrest entry will inevitably tip off the suspects and likely result in destruction or removal of evidence not uncovered during the arrest. I therefore cannot believe that the police would take the risk of losing valuable evidence through a pretextual arrest entry rather than applying to a magistrate for a search warrant.</p>
<p></p>
<h2>B</h2>
<p>While exaggerating the invasion of personal privacy involved in home arrests, the Court fails to account for the danger that its rule will "severely hamper effective law enforcement," <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#431" aria-description="Citation for case: United States v. Watson">423 U. S., at 431</a></span> (POWELL, J., concurring); <i>Gerstein</i> v. <i>Pugh</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#113" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 113</a></span>. The policeman <span class="star-pagination">*619</span> on his beat must now make subtle discriminations that perplex even judges in their chambers. As MR. JUSTICE POWELL noted, concurring in <i>United States</i> v. <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson, supra</a></span></i><i>,</i> police will sometimes delay making an arrest, even after probable cause is established, in order to be sure that they have enough evidence to convict. Then, if they suddenly have to arrest, they run the risk that the subsequent exigency will not excuse their prior failure to obtain a warrant. This problem cannot effectively be cured by obtaining a warrant as soon as probable cause is established because of the chance that the warrant will go state before the arrest is made.</p>
<p>Further, police officers will often face the difficult task of deciding whether the circumstances are sufficiently exigent to justify their entry to arrest without a warrant. This is a decision that must be made quickly in the most trying of circumstances. If the officers mistakenly decide that the circumstances are exigent, the arrest will be invalid and any evidence seized incident to the arrest or in plain view will be excluded at trial. On the other hand, if the officers mistakenly determine that exigent circumstances are lacking, they may refrain from making the arrest, thus creating the possibility that a dangerous criminal will escape into the community. The police could reduce the likelihood of escape by staking out all possible exits until the circumstances become clearly exigent or a warrant is obtained. But the costs of such a stakeout seem excessive in an era of rising crime and scarce police resources.</p>
<p>The uncertainty inherent in the exigent-circumstances determination burdens the judicial system as well. In the case of searches, exigent circumstances are sufficiently unusual that this Court has determined that the benefits of a warrant outweigh the burdens imposed, including the burdens on the judicial system. In contrast, arrests recurringly involve exigent circumstances, and this Court has heretofore held that a warrant can be dispensed with without undue sacrifice in Fourth Amendment values. The situation should be no different <span class="star-pagination">*620</span> with respect to arrests in the home. Under today's decision, whenever the police have made a warrantless home arrest there will be the possibility of "endless litigation with respect to the existence of exigent circumstances, whether it was practicable to get a warrant, whether the suspect was about to flee, and the like," <i>United States</i> v. <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#423" aria-description="Citation for case: United States v. Watson"><i>Watson, supra,</i> at 423-424</a></span>.</p>
<p>Our cases establish that the ultimate test under the Fourth Amendment is one of "reasonableness." <i>Marshall</i> v. <i>Barlow's, Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#315" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 315-316</a></span> (1978); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#539" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 539</a></span> (1967). I cannot join the Court in declaring unreasonable a practice which has been thought entirely reasonable by so many for so long. It would be far preferable to adopt a clear and simple rule: after knocking and announcing their presence, police may enter the home to make a daytime arrest without a warrant when there is probable cause to believe that the person to be arrested committed a felony and is present in the house. This rule would best comport with the common-law background, with the traditional practice in the States, and with the history and policies of the Fourth Amendment. Accordingly, I respectfully dissent.</p>
<p>MR. JUSTICE REHNQUIST, dissenting.</p>
<p>The Court today refers to both <i>Payton</i> and <i>Riddick</i> as involving "routine felony arrests." I have no reason to dispute the Court's characterization of these arrests, but cannot refrain from commenting on the social implications of the result reached by the Court. Payton was arrested for the murder of the manager of a gas station; Riddick was arrested for two armed robberies. If these are indeed "routine felony arrests," which culminated in convictions after trial upheld by the state courts on appeal, surely something is amiss in the process of the administration of criminal justice whereby these convictions are now set aside by this Court under the exclusionary rule which we have imposed upon the States under <span class="star-pagination">*621</span> the Fourth and Fourteenth Amendments to the United States Constitution.</p>
<p>I fully concur in and join the dissenting opinion of MR. JUSTICE WHITE. There is significant historical evidence that we have over the years misread the history of the Fourth Amendment in connection with searches, elevating the warrant requirement over the necessity for probable cause in a way which the Framers of that Amendment did not intend. See T. Taylor, Two Studies in Constitutional Interpretation 38-50 (1969). But one may accept all of that as <i>stare decisis,</i> and still feel deeply troubled by the transposition of these same errors into the area of actual arrests of felons within their houses with respect to whom there is probable cause to suspect guilt of the offense in question.</p>
<h2>NOTES</h2>
<p>[*]  Together with No. 78-5421, <i>Riddick</i> v. <i>New York,</i> also on appeal from the same court.</p>
<p>[1]  See also <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#433" aria-description="Citation for case: United States v. Watson">423 U. S., at 433</a></span> (STEWART, J., concurring); <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#432" aria-description="Citation for case: United States v. Watson"><i>id.,</i> at 432-433</a></span> (POWELL, J., concurring); <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#113" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 113, n. 13</a></span>; <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#474" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 474-481</a></span>; <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499-500</a></span>. Cf. <i>United States</i> v. <i>Santana,</i> <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">427 U. S. 38</a></span>.</p>
<p>[2]  See <i>State</i> v. <i>Perez,</i> <span class="citation" data-id="1836490"><a href="/opinion/1836490/state-v-perez/" aria-description="Citation for case: State v. Perez">277 So. 2d 778</a></span> (1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1064/">414 U. S. 1064</a></span>.</p>
<p>[3]  See <i>State</i> v. <i>Cook,</i> <span class="citation" data-id="9793807"><a href="/opinion/2616403/state-v-cook/" aria-description="Citation for case: State v. Cook">115 Ariz. 188</a></span>, <span class="citation" data-id="9793807"><a href="/opinion/2616403/state-v-cook/" aria-description="Citation for case: State v. Cook">564 P. 2d 877</a></span> (1977) (resting on both state and federal constitutional provisions); <i>People</i> v. <i>Ramey,</i> <span class="citation" data-id="9551973"><a href="/opinion/1185860/people-v-ramey/" aria-description="Citation for case: People v. Ramey">16 Cal. 3d 263</a></span>, <span class="citation" data-id="9551973"><a href="/opinion/1185860/people-v-ramey/" aria-description="Citation for case: People v. Ramey">545 P. 2d 1333</a></span> (1976), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/929/">429 U. S. 929</a></span> (state and federal); <i>People</i> v. <i>Moreno,</i> <span class="citation" data-id="9619146"><a href="/opinion/1396585/people-v-moreno/" aria-description="Citation for case: People v. Moreno">176 Colo. 488</a></span>, <span class="citation" data-id="9619146"><a href="/opinion/1396585/people-v-moreno/" aria-description="Citation for case: People v. Moreno">491 P. 2d 575</a></span> (1971) (federal only); <i>State</i> v. <i>Jones,</i> <span class="citation" data-id="1860990"><a href="/opinion/1860990/state-v-jones/" aria-description="Citation for case: State v. Jones">274 N. W. 2d 273</a></span> (Iowa 1979) (state and federal); <i>State</i> v. <i>Platten,</i> <span class="citation" data-id="1435637"><a href="/opinion/1435637/state-v-platten/" aria-description="Citation for case: State v. Platten">225 Kan. 764</a></span>, <span class="citation" data-id="1435637"><a href="/opinion/1435637/state-v-platten/" aria-description="Citation for case: State v. Platten">594 P. 2d 201</a></span> (1979) (state and federal); <i>Commonwealth</i> v. <i>Forde,</i> <span class="citation" data-id="9519710"><a href="/opinion/2017555/commonwealth-v-forde/" aria-description="Citation for case: Commonwealth v. Forde">367 Mass. 798</a></span>, <span class="citation" data-id="9519710"><a href="/opinion/2017555/commonwealth-v-forde/" aria-description="Citation for case: Commonwealth v. Forde">329 N. E. 2d 717</a></span> (1975) (federal only); <i>State</i> v. <i>Olson,</i> <span class="citation" data-id="1218237"><a href="/opinion/1218237/state-v-olson/" aria-description="Citation for case: State v. Olson">287 Ore. 157</a></span>, <span class="citation" data-id="1218237"><a href="/opinion/1218237/state-v-olson/" aria-description="Citation for case: State v. Olson">598 P. 2d 670</a></span> (1979) (state and federal); <i>Commonwealth</i> v. <i>Williams,</i> <span class="citation" data-id="9750792"><a href="/opinion/2295125/commonwealth-v-williams/" aria-description="Citation for case: Commonwealth v. Williams">483 Pa. 293</a></span>, <span class="citation" data-id="9750792"><a href="/opinion/2295125/commonwealth-v-williams/" aria-description="Citation for case: Commonwealth v. Williams">396 A. 2d 1177</a></span> (1978) (federal only); <i>State</i> v. <i>McNeal,</i> <span class="citation" data-id="9605191"><a href="/opinion/1369726/state-v-mcneal/" aria-description="Citation for case: State v. McNeal">251 S. E. 2d 484</a></span> (W. Va. 1978) (state and federal); <i>Laasch</i> v. <i>State,</i> <span class="citation" data-id="9718617"><a href="/opinion/2106646/laasch-v-state/" aria-description="Citation for case: Laasch v. State">84 Wis. 2d 587</a></span>, <span class="citation" data-id="9718617"><a href="/opinion/2106646/laasch-v-state/" aria-description="Citation for case: Laasch v. State">267 N. W. 2d 278</a></span> (1978) (state and federal).</p>
<p>[4]  Compare <i>United States</i> v. <i>Reed,</i> <span class="citation" data-id="354014"><a href="/opinion/354014/united-states-v-nancy-reed-and-morris-goldsmith-aka-marlowe/" aria-description="Citation for case: United States v. Nancy Reed and Morris Goldsmith, A/K/A...">572 F. 2d 412</a></span> (CA2 1978), cert. denied <i>sub nom. </i><i>Goldsmith</i> v. <i>United States,</i> <span class="citation" data-id="9013020"><a href="/opinion/9019821/goldsmith-v-united-states/" aria-description="Citation for case: Goldsmith v. United States">439 U. S. 913</a></span>; <i>United States</i> v. <i>Killebrew,</i> <span class="citation" data-id="348416"><a href="/opinion/348416/united-states-v-gerald-killebrew/" aria-description="Citation for case: United States v. Gerald Killebrew">560 F. 2d 729</a></span> (CA6 1977); <i>United States</i> v. <i>Shye,</i> <span class="citation" data-id="317251"><a href="/opinion/317251/united-states-v-reginald-jerome-shye/" aria-description="Citation for case: United States v. Reginald Jerome Shye">492 F. 2d 886</a></span> (CA6 1974); <i>United States</i> v. <i>Houte,</i> <span class="citation" data-id="369038"><a href="/opinion/369038/united-states-v-edward-corbit-houle/" aria-description="Citation for case: United States v. Edward Corbit Houle">603 F. 2d 1297</a></span> (CA8 1979); <i>United States</i> v. <i>Prescott,</i> <span class="citation" data-id="9465056"><a href="/opinion/358848/united-states-v-saundra-prescott/" aria-description="Citation for case: United States v. Saundra Prescott">581 F. 2d 1343</a></span> (CA9 1978); <i>Dorman</i> v. <i>United States,</i> 140 U. S. App. D. C. 313, <span class="citation" data-id="9456306"><a href="/opinion/293653/harold-b-dorman-v-united-states/" aria-description="Citation for case: Harold B. Dorman v. United States">435 F. 2d 385</a></span> (1970), with <i>United States</i> v. <i>Williams,</i> <span class="citation" data-id="354259"><a href="/opinion/354259/united-states-v-william-august-halm-williams/" aria-description="Citation for case: United States v. William August Halm Williams">573 F. 2d 348</a></span> (CA5 1978); <i>United States ex rel. Wright</i> v. <i>Woods,</i> <span class="citation" data-id="292629"><a href="/opinion/292629/united-states-of-america-ex-rel-charles-a-wright-v-joseph-woods/" aria-description="Citation for case: United States of America Ex Rel. Charles A. Wright v....">432 F. 2d 1143</a></span> (CA7 1970), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./401/966/">401 U. S. 966</a></span>. Three other Circuits have assumed without deciding that warrantless home arrests are unconstitutional. <i>United States</i> v. <i>Bradley,</i> <span class="citation" data-id="301708"><a href="/opinion/301708/united-states-v-charles-b-bradley-jr/" aria-description="Citation for case: United States v. Charles B. Bradley, Jr.">455 F. 2d 1181</a></span> (CA1 1972); <i>United States</i> v. <i>Davis,</i> <span class="citation" data-id="303979"><a href="/opinion/303979/united-states-v-kelley-davis-aka-tee-in-no-71-1778-and-inez-davis/" aria-description="Citation for case: United States v. Kelley Davis A/K/A Tee, in No. 71-1778,...">461 F. 2d 1026</a></span> (CA3 1972); <i>Vance</i> v. <i>North Carolina,</i> <span class="citation" data-id="292572"><a href="/opinion/292572/jacob-vance-jr-v-state-of-north-carolina/" aria-description="Citation for case: Jacob Vance, Jr. v. State of North Carolina">432 F. 2d 984</a></span> (CA4 1970). And one Circuit has upheld such an arrest without discussing the constitutional issue. <i>Michael</i> v. <i>United States,</i> <span class="citation" data-id="279701"><a href="/opinion/279701/joyce-marie-michael-v-united-states/" aria-description="Citation for case: Joyce Marie Michael v. United States">393 F. 2d 22</a></span> (CA10 1968).</p>
<p>[5]  A thorough search of the apartment resulted in the seizure of additional evidence tending to prove Payton's guilt, but the prosecutor stipulated that the officers' warrantless search of the apartment was illegal and that all the seized evidence except the shell casing should be suppressed.
</p>
<p>"MR. JACOBS: There's no question that the evidence that was found in bureau drawers and in the closet was illegally obtained. I'm perfectly willing to concede that, and I do so in my memorandum of law. There's no question about that." App. 4.</p>
<p>[6]  "At the time in question, January 15, 1970, the law applicable to the police conduct related above was governed by the Code of Criminal Procedure. Section 177 of the Code of Criminal Procedure as applicable to this case recited: `A peace officer may, without a warrant, arrest a person. . . 3. When a felony has in fact been committed, and he has reasonable cause for believing the person to be arrested to have committed it.' Section 178 of the Code of Criminal Procedure provided: `To make an arrest, as provided in the last section [177], the officer may break open an outer or inner door or window of a building, if, after notice of his office and purpose, he be refused admittance.'" <span class="citation" data-id="6197069"><a href="/opinion/6328523/people-v-payton/#974" aria-description="Citation for case: People v. Payton">84 Misc. 2d 973, 974-975</a></span>, 376 N. Y. S. 2d 779, 780 (Sup. Ct., Trial Term, N. Y. County, 1974).</p>
<p>[7]  "Although Detective Malfer knocked on the defendant's door, it is not established that at this time he announced that his purpose was to arrest the defendant. Such a declaration of purpose is unnecessary when exigent circumstances are present (<i>People</i> v. <i>Wojciechowski,</i> <span class="citation" data-id="5768902"><a href="/opinion/5911360/people-v-wojciechowski/" aria-description="Citation for case: People v. Wojciechowski">31 AD 2d 658</a></span>; <i>People</i> v. <i>McIlwain,</i> <span class="citation" data-id="5763049"><a href="/opinion/5905685/people-v-mcilwain/" aria-description="Citation for case: People v. McIlwain">28 AD 2d 711</a></span>).
</p>
<p>"`Case law has made exceptions from the statute or common-law rules for exigent circumstances which may allow dispensation with the notice . . . It has also been held or suggested that notice is not required if there is reason to believe that it will allow an escape or increase unreasonably the physical risk to the police or to innocent persons.' (<i>People</i> v. <i>Floyd,</i> <span class="citation" data-id="5525551"><a href="/opinion/5677661/people-v-floyd/#562" aria-description="Citation for case: People v. Floyd">26 NY 2d 558, 562</a></span>.)</p>
<p>"The facts of this matter indicate that a grave offense had been committed; that the suspect was reasonably believed to be armed and could be a danger to the community; that a clear showing of probable cause existed and that there was strong reason to believe that the suspect was in the premises being entered and that he would escape if not swiftly apprehended. From this fact the court finds that exigent circumstances existed to justify noncompliance with section 178. The court holds, therefore, that the entry into defendant's apartment was valid." <i>Id,</i> at 975, 376 N. Y. S. 2d, at 780-781.</p>
<p>[8]  55 App. Div. 2d 859 (1976).</p>
<p>[9]  New York Crim. Proc. Law § 140.15 (4) (McKinney 1971) provides, with respect to arrest without a warrant:
</p>
<p>"In order to effect such an arrest, a police officer may enter premises in which he reasonably believes such person to be present, under the same circumstances and in the same manner as would be authorized, by the provisions of subdivisions four and five of section 120.80, if he were attempting to make such arrest pursuant to a warrant of arrest."</p>
<p>Section 120.80, governing execution of arrest warrants, provides in relevant part:</p>
<p>"4. In order to effect the arrest, the police officer may, under circumstances and in a manner prescribed in this subdivision, enter any premises in which he reasonably believes the defendant to be present. Before such entry, he must give, or make reasonable effort to give, notice of his authority and purpose to an occupant thereof, unless there is reasonable cause to believe that the giving of such notice will:</p>
<p>"(a) Result in the defendant escaping or attempting to escape; or</p>
<p>"(b) Endanger the life or safety of the officer or another person; or</p>
<p>"(c) Result in the destruction, damaging or secretion of material evidence.</p>
<p>"5. If the officer is authorized to enter premises without giving notice of his authority and purpose, or if after giving such notice he is not admitted, he may enter such premises, and by a breaking if necessary."</p>
<p>[10]  App. 63-66.</p>
<p>[11]  56 App. Div. 2d 937, 392 N. Y. S. 2d 848 (1977). One justice dissented on the ground that the officers' failure to announce their authority and purpose before entering the house made the arrest illegal as a matter of state law.</p>
<p>[12]  45 N. Y. 2d, at 309-310, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#228" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 228</a></span>.</p>
<p>[13]  The majority continued:
</p>
<p>"In the case of the search, unless appropriately limited by the terms of a warrant, the incursion on the householder's domain normally will be both more extensive and more intensive and the resulting invasion of his privacy of greater magnitude than what might be expected to occur on an entry made for the purpose of effecting his arrest. A search by its nature contemplates a possibly thorough rummaging through possessions, with concurrent upheaval of the owner's chosen or random placement of goods and articles and disclosure to the searchers of a myriad of personal items and details which he would expect to be free from scrutiny by uninvited eyes. The householder by the entry and search of his residence is stripped bare, in greater or lesser degree, of the privacy which normally surrounds him in his daily living, and, if he should be absent, to an extent of which he will be unaware.</p>
<p>"Entry for the purpose of arrest may be expected to be quite different. While the taking into custody of the person of the householder is unquestionably of grave import, there is no accompanying prying into the area of expected privacy attending his possessions and affairs. That personal seizure alone does not require a warrant was established by <i>United States</i> v. <i>Watson</i> (<span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 US 411</a></span>, <i>supra),</i> which upheld a warrantless arrest made in a public place. In view of the minimal intrusion on the elements of privacy of the home which results from entry on the premises for making an arrest (as compared with the gross intrusion which attends the arrest itself), we perceive no sufficient reason for distinguishing between an arrest in a public place and an arrest in a residence. To the extent that an arrest will always be distasteful or offensive, there is little reason to assume that arrest within the home is any more so than arrest in a public place; on the contrary, it may well be that because of the added exposure the latter may be more objectionable.</p>
<p>"At least as important, and perhaps even more so, in concluding that entries to make arrests are not `unreasonable'â  the substantive test under the constitutional proscriptionsâ  is the objective for which they are made, viz., the arrest of one reasonably believed to have committed a felony, with resultant protection to the community. The `reasonableness' of any governmental intrusion is to be judged from two perspectivesâ  that of the defendant, considering the degree and scope of the invasion of his person or property; that of the People, weighing the objective and imperative of governmental action. The community's interest in the apprehension of criminal suspects is of a higher order than is its concern for the recovery of contraband or evidence; normally the hazards created by the failure to apprehend far exceed the risks which may follow nonrecovery." <i>Id.,</i> at 310-311, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#229" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 229</a></span>.</p>
<p>[14]  "The apparent historical acceptance in the English common law of warrantless entries to make felony arrests (2 Hale, Historia Placitorum Coronae, History of Pleas of Crown [1st Amer ed, 1847], p. 92; Chitty, Criminal Law [3d Amer, from 2d London, ed, 1836] 22-23), and the existence of statutory authority for such entries in this State since the enactment of the Code of Criminal Procedure in 1881 argue against a holding of unconstitutionality and substantiate the reasonableness of such procedure. . . .
</p>
<p>"Nor do we ignore the fact that a number of jurisdictions other than our own have also enacted statutes authorizing warrantless entries of buildings (without exception for homes) for purposes of arrest. The American Law Institute's Model Code of Pre-Arraignment Procedure makes similar provision in section 120.6, with suggested special restrictions only as to nighttime entries." <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#311" aria-description="Citation for case: People v. Payton"><i>Id.,</i> at 311-312</a></span>, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#229" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 229-230</a></span> (footnote omitted).</p>
<p>[15]  <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#315" aria-description="Citation for case: People v. Payton"><i>Id.,</i> at 315</a></span>, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#232" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 232</a></span> (Wachtler, J., dissenting).</p>
<p>[16]  <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#319" aria-description="Citation for case: People v. Payton"><i>Id.,</i> at 319-320</a></span>, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#235" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 235</a></span> (Cooke, J., dissenting).</p>
<p>[17]  "Although the point has not been squarely adjudicated since <i>Coolidge</i> [v. <i>New Hampshire</i><i>,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span>,] (see <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#418" aria-description="Citation for case: United States v. Watson">423 US 411, 418, n. 6</a></span>), its proper resolution, it is submitted, is manifest. At the core of the Fourth Amendment, whether in the context of a search or an arrest, is the fundamental concept that any governmental intrusion into an individual's home or expectation of privacy must be strictly circumscribed (see, <i>e. g., </i><i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 US 616, 630</a></span>; <i>Camara</i> v. <i>Municipal Ct.,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 US 523, 528</a></span>). To achieve that end, the framers of the amendment interposed the warrant requirement between the public and the police, reflecting their conviction that the decision to enter a dwelling should not rest with the officer in the field, but rather with a detached and disinterested Magistrate (<i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 US 451, 455-456</a></span>; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 US 10, 13-14</a></span>). Inasmuch as the purpose of the Fourth Amendment is to guard against arbitrary governmental invasions of the home, the necessity of prior judicial approval should control any contemplated entry, regardless of the purpose for which that entry is sought. By definition, arrest entries must be included within the scope of the amendment, for while such entries are for persons, not things, they are nonetheless, violations of privacy, the chief evil that the Fourth Amendment was designed to deter (<i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 US 505, 511</a></span>)." <i>Id.,</i> at 320-321, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#235" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 235-236</a></span> (Cooke, J., dissenting).</p>
<p>[18]  <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#324" aria-description="Citation for case: People v. Payton"><i>Id.,</i> at 324</a></span>, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#238" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 238</a></span> (Cooke, J., dissenting).</p>
<p>[19]  Although it is not clear from the record that appellants raised this constitutional issue in the trial courts, since the highest court of the State passed on it, there is no doubt that it is properly presented for review by this Court. See <i>Raley</i> v. <i>Ohio,</i> <span class="citation" data-id="105925"><a href="/opinion/105925/raley-v-ohio/#436" aria-description="Citation for case: Raley v. Ohio">360 U. S. 423, 436</a></span>.</p>
<p>[20]  45 N. Y. 2d, at 308, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#228" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 228</a></span>. Judge Wachtler in dissent, however, would have upheld the warrantless entry in Payton's case on exigency grounds, and therefore agreed with the majority's refusal to suppress the shell casing. See <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#315" aria-description="Citation for case: People v. Payton"><i>id.,</i> at 315</a></span>, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#232" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 232</a></span>.</p>
<p>[21]  "Vivid in the memory of the newly independent Americans were those general warrants known as writs of assistance under which officers of the Crown had so bedeviled the colonists. The hated writs of assistance had given customs officials blanket authority to search where they pleased for goods imported in violation of British tax laws. They were denounced by James Otis as `the worst instrument of arbitrary power, the most destructive of English liberty, and the fundamental principles of law, that ever was found in an English law book,' because they placed `the liberty of every man in the hands of every petty officer.' The historic occasion of that denunciation, in 1761 at Boston, has been characterized as `perhaps the most prominent event which inaugurated the resistance of the colonies to the oppressions of the mother country. "Then and there," said John Adams, "then and there was the first scene of the first act of opposition to the arbitrary claims of Great Britain. Then and there the child Independence was born."' <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#625" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 625</a></span>." <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481-482</a></span>.
</p>
<p>See also J. Landynski, Search and Seizure and the Supreme Court 19-48 (1966); N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 13-78 (1937); T. Taylor, Two Studies in Constitutional Interpretation 19-44 (1969).</p>
<p>[22]  "`The rights of the people to be secured in their persons, their houses, their papers, and their other property, from all unreasonable searches and seizures, shall not be violated by warrants issued without probable cause, supported by oath or affirmation, or not particularly describing the places to be searched, or the persons or things to be seized.' Annals of Cong., 1st Cong., 1st sess., p. 452." Lasson, <i>supra,</i> at 100, n. 77.</p>
<p>[23]  "The general right of security from unreasonable search and seizure was given a sanction of its own and the amendment thus intentionally given a broader scope. That the prohibition against `unreasonable searches' was intended, accordingly, to cover something other than the form of the warrant is a question no longer left to implication to be derived from the phraseology of the Amendment." Lasson, <i>supra,</i> at 103. (Footnote omitted.)</p>
<p>[24]  As Mr. Justice Jackson so cogently observed in <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, 13-14:
</p>
<p>"The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime. Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers. Crime, even in the privacy of one's own quarters, is, of course, of grave concern to society, and the law allows such crime to be reached on proper showing. The right of officers to thrust themselves into a home is also a grave concern, not only to the individual but to a society which chooses to dwell in reasonable security and freedom from surveillance. When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent." (Footnotes omitted.)</p>
<p>[25]  As the Court stated in <i>Coolidge</i> v. <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">New Hampshire</a></span></i><i>:</i>
</p>
<p>"Both sides to the controversy appear to recognize a distinction between searches and seizures that take place on a man's propertyâ  his home or officeâ  and those carried out elsewhere. It is accepted, at least as a matter of principle, that a search or seizure carried out on a suspect's premises without a warrant is <i>per se</i> unreasonable, unless the police can show that it falls within one of a carefully defined set of exceptions based on the presence of `exigent circumstances.'</p>
<p>.....</p>
<p>"It is clear, then, that the notion that the warrantless entry of a man's house in order to arrest him on probable cause is <i>per se</i> legitimate is in fundamental conflict with the basic principle of Fourth Amendment law that searches and seizures inside a man's house without warrant are <i>per se</i> unreasonable in the absence of some one of a number of well defined `exigent circumstances.'" <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#474" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 474-475, 477-478</a></span>.</p>
<p>Although Mr. Justice Harlan joined this portion of the Court's opinion, he expressly disclaimed any position on the issue now before us. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#492" aria-description="Citation for case: Coolidge v. New Hampshire"><i>Id.,</i> at 492</a></span> (concurring opinion).</p>
<p>[26]  As Mr. Justice Harlan wrote for the Court:
</p>
<p>"It is settled doctrine that probable cause for belief that certain articles subject to seizure are in a dwelling cannot of itself justify a search without a warrant. <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span>; <i>Taylor</i> v. <i>United States,</i> <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/#6" aria-description="Citation for case: Taylor v. United States">286 U. S. 1, 6</a></span>. The decisions of this Court have time and again underscored the essential purpose of the Fourth Amendment to shield the citizen from unwarranted intrusions into his privacy. See, <i>e. g., </i><i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span>; <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 455</a></span>; cf. <i>Giordenello</i> v. <i>United States,</i> [<span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span>]. This purpose is realized by Rule 41 of the Federal Rules of Criminal Procedure, which implements the Fourth Amendment by requiring that an impartial magistrate determine from an affidavit showing probable cause whether information possessed by law-enforcement officers justifies the issuance of a search warrant. Were federal officers free to search without a warrant merely upon probable cause to believe that certain articles were within a home, the provisions of the Fourth Amendment would become empty phrases, and the protection it affords largely nullified." <i>Jones</i> v. <i>United States,</i> 357 U. S., at 497-498 (footnote omitted).</p>
<p>[27]  See generally Rotenberg &amp; Tanzer, Searching for the Person to be Seized, 35 Ohio St. L. J. 56 (1974).</p>
<p>[28]  See n. 4, <i>supra.</i></p>
<p>[29]  See, <i>e. g.,</i> the facts in Payton's case, n. 5; <i>supra.</i></p>
<p>[30]  "The cases construing the Fourth Amendment thus reflect the ancient common-law rule that a peace officer was permitted to arrest without a warrant for a misdemeanor or felony committed in his presence as well as for a felony not committed in his presence if there was reasonable ground for making the arrest. 10 Halsbury's Laws of England 344-345 (3d ed. 1955); 4 W. Blackstone, Commentaries *292; 1 J. Stephen, A History of the Criminal Law of England 193 (1883); 2 M. Hale, Pleas of the Crown *72-74; Wilgus, Arrests Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 541</span>, 547-550, 686-688 (1924); <i>Samuel</i> v. <i>Payne,</i> <span class="citation" data-id="6629715"><a href="/opinion/6747612/green-v-graves/" aria-description="Citation for case: Green v. Graves">1 Doug. 359</a></span>, 99 Eng. Rep. 230 (K. B. 1780); <i>Beckwith</i> v. <i>Philby,</i> 6 Barn. &amp; Cress. 635, 108 Eng. Rep. 585 (K. B. 1827)." <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#418" aria-description="Citation for case: United States v. Watson">423 U. S., at 418-419</a></span>.</p>
<p>[31]  "The balance struck by the common law in generally authorizing felony arrests on probable cause, but without a warrant, has survived substantially intact. It appears in almost all of the States in the form of express statutory authorization." <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#421" aria-description="Citation for case: United States v. Watson"><i>Id.,</i> at 421-422</a></span>.</p>
<p>[32]  "This is the rule Congress has long directed its principal law enforcement officers to follow. Congress has plainly decided against conditioning warrantless arrest power on proof of exigent circumstances." <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#423" aria-description="Citation for case: United States v. Watson"><i>Id.,</i> at 423</a></span>.
</p>
<p>The Court added in a footnote:</p>
<p>"Until 1951, <span class="citation no-link">18 U. S. C. § 3052</span> conditioned the warrantless arrest powers of the agents of the Federal Bureau of Investigation on there being reasonable grounds to believe that the person would escape before a warrant could be obtained. The Act of Jan. 10, 1951, c. 1221, § 1, <span class="citation no-link">64 Stat. 1239</span>, eliminated this condition." <i>Id.,</i> at 423, n. 13.</p>
<p>[33]  There are important differences between the common-law rules relating to searches and seizures and those that have evolved through the process of interpreting the Fourth Amendment in light of contemporary norms and conditions. For example, whereas the kinds of property subject to seizure under warrants had been limited to contraband and the fruits or instrumentalities of crime, see <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#309" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 309</a></span>, the category of property that may be seized, consistent with the Fourth Amendment, has been expanded to include mere evidence. <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span>. Also, the prohibitions of the Amendment have been extended to protect against invasion by electronic eavesdropping of an individual's privacy in a phone booth not owned by him, <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span>, even though the earlier law had focused on the physical invasion of the individual's person or property interests in the course of a seizure of tangible objects. See <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#466" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 466</a></span>. Thus, this Court has not simply frozen into constitutional law those law enforcement practices that existed at the time of the Fourth Amendment's passage.</p>
<p>[34]  The issue is not whether a defendant must stand trial, because he must do so even if the arrest is illegal. See <i>United States</i> v. <i>Crews, ante,</i> at 474.</p>
<p>[35]  Those modern commentators who have carefully studied the early works agree with that assessment. See ALI, A Model Code of Pre-Arraignment Procedure 308 (Prop. Off. Draft 1975) (hereinafter ALI Code); Blakey, The Rule of Announcement and Unlawful Entry: <i>Miller</i> v. <i>United States</i> and <i>Ker</i> v. <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">California</a></span></i><i>,</i> <span class="citation no-link">112 U. Pa. L. Rev. 499</span>, 502 (1964); Comment, Forcible Entry to Effect a Warrantless Arrestâ  The Eroding Protection of the Castle, <span class="citation no-link">82 Dick. L. Rev. 167</span>, 168, n. 5 (1977); Note, The Constitutionality of Warrantless Home Arrests, <span class="citation no-link">78 Colum. L. Rev. 1550</span>, 1553 (1978) ("the major common-law commentators appear to be equally divided on the requirement of a warrant for a home arrest") (hereinafter Columbia Note); Recent Development, Warrantless Arrests by Police Survive a Constitutional Challengeâ  <i>United States</i> v. <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i><i>,</i> <span class="citation no-link">14 Am. Crim. L. Rev. 193</span>, 210-211 (1976). Accord, <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#307" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 307-308</a></span>; <i>Accarino</i> v. <i>United States,</i> 85 U. S. App. D. C. 394, 402, <span class="citation" data-id="224194"><a href="/opinion/224194/accarino-v-united-states/#464" aria-description="Citation for case: Accarino v. United States">179 F. 2d 456, 464</a></span> (1949).</p>
<p>[36]  "Foremost among the titles to be found in private libraries of the time were the works of Coke, the great expounder of Magna Carta, and similar books on English liberties. The inventory of the library of Arthur Spicer, who died in Richmond County, Virginia, in 1699, included Coke's <i>Institutes,</i> another work on Magna Carta, and a "Table to Cooks Reports.' The library of Colonel Daniel McCarty, a wealthy planter and member of the Virginia House of Burgesses who died in Westmoreland County in 1724, included Coke's <i>Reports,</i> an abridgment of Coke's <i>Reports, Coke on Littleton,</i> and `Rights of the Comons of England.' Captain Charles Colston, who died in Richmond County, Vi

[...TRUNCATED 24323 of 144323 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/Pennsylvania v. Mimms.md  (`case`, 5 assertions)

### content_page

```
---
title: "Pennsylvania v. Mimms"
type: case
citation: "434 U.S. 106 (1977)"
parallel_cite: "98 S. Ct. 330; 54 L. Ed. 2d 331"
neutral_cite: 1977 U.S. LEXIS 157
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-12-05
docket: 76-1830
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1977-12-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Pennsylvania v. Mimms
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109751/pennsylvania-v-mimms/"
  cluster_id: 109751
  opinion_id: 9427002
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Key — Anchor"
related: ["[[Maryland v. Wilson]]", "[[Terry v. Ohio]]", "[[Rodriguez v. United States]]", "[[Delaware v. Prouse]]"]
aliases: []
tags: ["case", "fourth-amendment", "traffic-stops", "officer-safety", "order-out-of-vehicle", "per-curiam"]
holding: "Once a vehicle is lawfully stopped for a traffic violation, an officer may order the driver out of the vehicle as a matter of course;…"
lake:
  record_id: Pennsylvania v. Mimms
  status: verified
  projected_at: 2026-07-06
---

# Pennsylvania v. Mimms

*434 U.S. 106 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Philadelphia officer stopped Mimms's car for an expired license plate to issue a summons. The officer asked Mimms to step out of the car; as Mimms got out, the officer noticed a large bulge under his jacket, frisked him, and found a loaded revolver. Mimms was convicted of carrying a concealed firearm.

## Issue
Whether, consistent with the Fourth Amendment, an officer may order a driver lawfully stopped for a traffic violation to get out of the vehicle as a matter of course.

## Rule
Yes. Ordering the driver out is at most a "*de minimis*" additional intrusion: "We think this additional intrusion can only be described as *de minimis*. . . . What is at most a mere inconvenience cannot prevail when balanced against legitimate concerns for the officer's safety." — 434 U.S. at 111. ^pin-111

"[O]nce a motor vehicle has been lawfully detained for a traffic violation, the police officers may order the driver to get out of the vehicle without violating the Fourth Amendment's proscription of unreasonable searches and seizures." — 434 U.S. at 111 n.6. ^pin-111a

## Application
Mimms was lawfully stopped for an expired plate, so the officer could order him out of the car as a matter of course. Once Mimms stepped out, the visible bulge under his jacket gave the officer reasonable suspicion that he was armed and dangerous, justifying the protective frisk that produced the revolver. Both the order to exit and the frisk were reasonable.

## Conclusion
An officer may routinely order a lawfully stopped driver out of the vehicle; the search and seizure were reasonable and the judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Mimms*'s order-out rule was extended to passengers in [[Maryland v. Wilson]].

## Appears on
- [[Traffic Stops]] — *Key — Anchor*

## Sources
- *Pennsylvania v. Mimms*, 434 U.S. 106 (1977) (per curiam) — https://www.courtlistener.com/opinion/109751/pennsylvania-v-mimms/ — pinpoints: 111, 111 n.6.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5d24451745073ecc", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "434 U.S. 106 (1977)", "court": "U.S. Supreme Court", "neutral_cite": "1977 U.S. LEXIS 157", "official_citation_present": true, "parallel_cite": "98 S. Ct. 330; 54 L. Ed. 2d 331", "title": "Pennsylvania v. Mimms", "year": "1977"}}
{"assertion_id": "3843799ea209f3a1", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Key — Anchor", "title": "Pennsylvania v. Mimms"}}
{"assertion_id": "c0106502ad4b2ed7", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Once a vehicle is lawfully stopped for a traffic violation, an officer may order the driver out of the vehicle as a matter of course;…", "title": "Pennsylvania v. Mimms"}}
{"assertion_id": "293aae019cca6cee", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1977-12-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Pennsylvania v. Mimms", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Pennsylvania v. Mimms", "varies_by_point": "false"}}
{"assertion_id": "8ba40f626b6f74ff", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Pennsylvania v. Mimms"}}
```

### lake record — Pennsylvania v. Mimms

```json
{
  "schema_version": "s2.v1",
  "record_id": "Pennsylvania v. Mimms",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Pennsylvania v. Mimms",
    "case_name_short": "Mimms",
    "case_name_full": "Pennsylvania v. Mimms",
    "input_case_name": "Pennsylvania v. Mimms",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-12-05",
    "year": 1977,
    "docket": "76-1830",
    "cluster_id": 109751,
    "lead_opinion_id": 9427002,
    "sibling_ids": [
      109751,
      9427002,
      9427003,
      9427004
    ],
    "absolute_url": "/opinion/109751/pennsylvania-v-mimms/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "434 U.S. 106",
      "volume": "434",
      "reporter": "U.S.",
      "page": "106",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "98 S. Ct. 330",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "330",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 L. Ed. 2d 331",
        "volume": "54",
        "reporter": "L. Ed. 2d",
        "page": "331",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 157",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "157",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "434 U.S. 106",
        "volume": "434",
        "reporter": "U.S.",
        "page": "106",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 S. Ct. 330",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "330",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 L. Ed. 2d 331",
        "volume": "54",
        "reporter": "L. Ed. 2d",
        "page": "331",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 157",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "157",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "434 U.S. 106",
    "official_selection": {
      "court_class": "scotus",
      "selected": "434 U.S. 106",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-111",
      "page": null,
      "quote": "--- # Pennsylvania v. Mimms *434 U.S. 106 (1977)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Philadelphia officer stopped Mimms's car for an expired license plate to issue a summons. The officer asked Mimms to step out of the car; as Mimms got out, the officer noticed a large bulge under his jacket, frisked him, and found a loaded revolver. Mimms was convicted of carrying a concealed firearm. ## Issue Whether, consistent with the Fourth Amendment, an officer may order a driver lawfully stopped for a traffic violation to get out of the vehicle as a matter of course. ## Rule Yes. Ordering the driver out is at most a",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-111a",
      "page": null,
      "quote": "[O]nce a motor vehicle has been lawfully detained for a traffic violation, the police officers may order the driver to get out of the vehicle without violating the Fourth Amendment's proscription of unreasonable searches and seizures.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1977-12-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Pennsylvania v. Mimms",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Long",
          "cluster_id": 4786330,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Whren v. United States",
          "cluster_id": 118036,
          "cite": [
            "135 L. Ed. 2d 89",
            "116 S. Ct. 1769",
            "517 U.S. 806",
            "1996 U.S. LEXIS 3720"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spencer v. Kemna",
          "cluster_id": 118176,
          "cite": [
            "140 L. Ed. 2d 43",
            "118 S. Ct. 978",
            "523 U.S. 1",
            "1998 U.S. LEXIS 1597"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Texas",
          "cluster_id": 110128,
          "cite": [
            "61 L. Ed. 2d 357",
            "99 S. Ct. 2637",
            "443 U.S. 47",
            "1979 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rawlings v. Kentucky",
          "cluster_id": 110326,
          "cite": [
            "65 L. Ed. 2d 633",
            "100 S. Ct. 2556",
            "448 U.S. 98",
            "1980 U.S. LEXIS 142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murphy v. Hunt",
          "cluster_id": 110660,
          "cite": [
            "71 L. Ed. 2d 353",
            "102 S. Ct. 1181",
            "455 U.S. 478",
            "1982 U.S. LEXIS 77"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brendlin v. California",
          "cluster_id": 145712,
          "cite": [
            "168 L. Ed. 2d 132",
            "127 S. Ct. 2400",
            "551 U.S. 249",
            "2007 U.S. LEXIS 7897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Atwater v. City of Lago Vista",
          "cluster_id": 2620702,
          "cite": [
            "149 L. Ed. 2d 549",
            "121 S. Ct. 1536",
            "532 U.S. 318",
            "2001 U.S. LEXIS 3366",
            "2001 Daily Journal DAR 3953",
            "2001 Colo. J. C.A.R. 2069",
            "14 Fla. L. Weekly Fed. S 193",
            "69 U.S.L.W. 4262",
            "2001 Cal. Daily Op. Serv. 3203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109751 OR 9427002 OR 9427003 OR 9427004) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTQ5NDExMjAwMDAwJnM9NDU4Nzk5MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109751+OR+9427002+OR+9427003+OR+9427004%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      },
      "lane2_top_cited": {
        "query": "cites:(109751 OR 9427002 OR 9427003 OR 9427004)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MTUmcz0xMTkxOTQ3JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109751+OR+9427002+OR+9427003+OR+9427004%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109751 OR 9427002 OR 9427003 OR 9427004)",
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
    "complete_query": "cites:(109751 OR 9427002 OR 9427003 OR 9427004)",
    "indexed_citing_opinions": 1974,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109751,
        "count": 1693,
        "count_source": "search"
      },
      {
        "opinion_id": 9427002,
        "count": 309,
        "count_source": "search"
      },
      {
        "opinion_id": 9427003,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427004,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3270,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/pennsylvania-v-mimms.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyODU0OTMmcz0xMDU5NzQ0MiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109751+OR+9427002+OR+9427003+OR+9427004%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109751,
        "cited_id": 103823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 107663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 107689,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 107900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 108894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 1311789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 2131784,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 2267362,
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
    "date_created": "2026-07-05T16:58:02Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:58:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:58:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:00:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:58:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Pennsylvania v. Mimms

```
<opinion type="majority">
<author id="Aqq">Per Curiam.</author>
<p id="b278-11">Petitioner Commonwealth seeks review of a judgment of the Supreme Court of Pennsylvania reversing respondent’s conviction for carrying a concealed deadly weapon and a firearm without a license. That court reversed the conviction because it held that respondent’s “revolver was seized in a <page-number citation-index="1" label="107">*107</page-number>manner which violated the Fourth Amendment to the Constitution of the United States.” <span class="citation" data-id="9747563"><a href="/opinion/2267362/commonwealth-v-mimms/#548" aria-description="Citation for case: Commonwealth v. Mimms">471 Pa. 546, 548</a></span>, <span class="citation" data-id="9747563"><a href="/opinion/2267362/commonwealth-v-mimms/#1158" aria-description="Citation for case: Commonwealth v. Mimms">370 A. 2d 1157, 1158</a></span> (1977). Because we disagree with this conclusion, we grant the Commonwealth’s petition for certiorari and reverse the judgment of the Supreme Court of Pennsylvania.</p>
<p id="b279-5">The facts are not in dispute. While on routine patrol, two Philadelphia police officers observed respondent Harry Mimms driving an automobile with an expired license plate. The officers stopped the vehicle for the purpose of issuing a traffic summons. One of the officers approached and asked respondent to step out of the car and produce his owner’s card and operator’s license. Respondent alighted, whereupon the officer noticed a large bulge under respondent’s sports jacket. Fearing that the bulge might be a weapon, the officer frisked respondent and discovered in his waistband a .38-caliber revolver loaded with five rounds of ammunition. The other occupant of the car was carrying a .32-caliber revolver. Respondent was immediately arrested and subsequently indicted for carrying a concealed deadly weapon and for unlawfully carrying a firearm without a license. His motion to suppress the revolver was denied; and, after a trial at which the revolver was introduced into evidence, respondent was convicted on both counts.</p>
<p id="b279-6">As previously indicated, the Supreme Court of Pennsylvania reversed respondent’s conviction, however, holding that the revolver should have been suppressed because it was seized contrary to the guarantees contained in the Fourth and Fourteenth Amendments to the United States Constitution.<footnotemark>1</footnotemark> The Pennsylvania court did not doubt that the officers acted reasonably in stopping the car. It was also willing to assume, <em>arguendo, </em>that the limited search for weapons was proper once the officer observed the bulge under respondent’s coat. But the court nonetheless thought the search constitutionally in<page-number citation-index="1" label="108">*108</page-number>firm because the officer's order to respondent to get out of the car was an impermissible “seizure.” This was so because the officer could not point to “objective observable facts to support a suspicion that criminal activity was afoot or that the occupants of the vehicle posed a threat to police safety.” <footnotemark>2</footnotemark> Since this unconstitutional intrusion led directly to observance of the bulge and to the subsequent “pat down,” the revolver was the fruit of an unconstitutional search, and, in the view of the Supreme Court of Pennsylvania, should have been suppressed.</p>
<p id="b280-5">We do not agree with this conclusion.<footnotemark>3</footnotemark> The touchstone of <page-number citation-index="1" label="109">*109</page-number>our analysis under the Fourth Amendment is always “the reasonableness in all the circumstances of the particular governmental invasion of a citizen’s personal security.” <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19</a></span> (1968). Reasonableness, of course, depends “on a balance between the public interest and the individual’s right to personal security free from arbitrary interference by law officers.” <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975).</p>
<p id="b281-5">In this case, unlike <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio</a></span>, </em>there is no question about the propriety of the initial restrictions on respondent’s freedom of movement. Respondent was driving an automobile with expired license tags in violation of the Pennsylvania Motor Vehicle Code.<footnotemark>4</footnotemark> Deferring for a moment the legality of the “frisk” once the bulge had been observed, we need presently deal only with the narrow question of whether the order to get out of the car, issued after the driver was lawfully detained, was reasonable and thus permissible under the Fourth Amendment. This inquiry must therefore focus not on the intrusion resulting from the request to stop the vehicle or from the later “pat down,” but on the incremental intrusion resulting from the request to get out of the car once the vehicle was lawfully stopped.</p>
<p id="b281-6">Placing the question in this narrowed frame, we look first to that side of the balance which bears the officer’s interest in taking the action that he did. The State freely concedes the officer had no reason to suspect foul play from the particular driver at the time of the stop, there having been nothing unusual or suspicious about his behavior. It was apparently <page-number citation-index="1" label="110">*110</page-number>his practice to order all drivers out of their vehicles as a matter of course whenever they had been stopped for a traffic violation. The State argues that this practice was adopted as a precautionary measure to afford a degree of protection to the officer and that it may be justified on that ground. Establishing a face-to-face confrontation diminishes the possibility, otherwise substantial, that the driver can make unobserved movements; this, in turn, reduces the likelihood that the officer will be the victim of an assault.<footnotemark>5</footnotemark></p>
<p id="b282-5">We think it too plain for argument that the State’s proffered justification — the safety of the officer — is both legitimate and weighty. “Certainly it would be unreasonable to require that police officers take unnecessary risks in the performance of their duties.” <em>Terry </em>v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#23" aria-description="Citation for case: Terry v. Ohio"><em>Ohio, supra, </em>at 23</a></span>. And we have specifically recognized the inordinate risk confronting an officer as he approaches a person seated in an automobile. “According to one study, approximately 30% of police shootings occurred when a police officer approached a suspect seated in an automobile. Bristow, Police Officer Shootings — A Tactical Evaluation, 54 J. Crim. L. C. &amp; P. S. 93 (1963).” <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span>, 148 n. 3 (1972). We are aware that not all these assaults occur when issuing traffic summons, but we have before expressly declined to accept the argument that traffic violations necessarily involve less danger to officers than other types of confrontations. <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#234" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 234</a></span> (1973). Indeed, it appears “that a significant percentage of murders of police officers occurs when the officers are making traffic stops.” <em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Id.,</a></span> </em>at 234 n. 5.</p>
<p id="b283-4"><page-number citation-index="1" label="111">*111</page-number>The hazard of accidental injury from passing traffic to an officer standing on the driver’s side of the vehicle may also be appreciable in some situations. Rather than conversing while standing exposed to moving traffic, the officer prudently may prefer to ask the driver of the vehicle to step out of the car and off onto the shoulder of the road where the inquiry may be pursued with greater safety to both.</p>
<p id="b283-5">Against this important interest we are asked to weigh the intrusion into the driver’s personal liberty occasioned not by the initial stop of the vehicle, which was admittedly justified, but by the order to get out of the car. We think this additional intrusion can only be described as <em>de minimis. </em>The driver is being asked to expose to view very little more of his person than is already exposed. The police have already lawfully decided that the driver shall be briefly detained; the only question is whether he shall spend that period sitting in the driver’s seat of his car or standing alongside it. Not only is the insistence of the police on the latter choice not a “serious intrusion upon the sanctity of the person,” but it hardly rises to the level of a “ ‘petty indignity.’ ” <em>Terry </em>v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#17" aria-description="Citation for case: Terry v. Ohio"><em>Ohio, supra, </em>at 17</a></span>. What is at most a mere inconvenience cannot prevail when balanced against legitimate concerns for the officer’s safety.<footnotemark>6</footnotemark></p>
<p id="b283-6">There remains the second question of the propriety of the search once the bulge in the jacket was observed. We have as little doubt on this point as on the first; the answer is controlled by <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra.</a></span> </em>In that case we thought the officer justified in conducting a limited search for weapons <page-number citation-index="1" label="112">*112</page-number>once he had reasonably concluded that the person whom he had legitimately stopped might be armed and presently dangerous. Under the standard enunciated in that case— whether “the facts available to the officer at the moment of the seizure or the search ‘warrant a man of reasonable caution in the belief’ that the action taken was appropriate” <footnotemark>7</footnotemark> — there is little question the officer was justified. The bulge in the jacket permitted the officer to conclude that Mimms was armed and thus posed a serious and present danger to the safety of the officer. In these circumstances, any man of “reasonable caution” would likely have conducted the “pat down.”</p>
<p id="b284-5">Respondent’s motion to proceed <em>in forma pauperis </em>is granted. The petition for writ of certiorari is granted, the judgment of the Supreme Court of Pennsylvania is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b284-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b279-7"> Three judges dissented on the federal constitutional issue.</p>
</footnote>
<footnote label="2">
<p id="b280-6"> <span class="citation" data-id="9747563"><a href="/opinion/2267362/commonwealth-v-mimms/#552" aria-description="Citation for case: Commonwealth v. Mimms">471 Pa., at 552</a></span>, <span class="citation" data-id="9747563"><a href="/opinion/2267362/commonwealth-v-mimms/#1160" aria-description="Citation for case: Commonwealth v. Mimms">370 A. 2d, at 1160</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b280-7"> We note that in his brief in opposition to a grant of certiorari respondent contends that this case is moot because he has already completed the 3-year maximum of the 1%- to 3-year sentence imposed. The case has, he argues, terminated against him for all purposes and for all time regardless of this Court’s disposition of the matter. See <em>St. Pierre </em>v. <em>United States, </em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">319 U. S. 41</a></span> (1943).</p>
<p id="b280-8">But cases such as <em>Sibron </em>v. <em>New </em>York, <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#53" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 53-57</a></span> (1968); <em>Street </em>v. <em>New York, </em><span class="citation" data-id="9423995"><a href="/opinion/107900/street-v-new-york/" aria-description="Citation for case: Street v. New York">394 U. S. 576</a></span> (1969); <em>Carafas </em>v. <em>LaVallee, </em><span class="citation" data-id="9423702"><a href="/opinion/107689/carafas-v-lavallee/" aria-description="Citation for case: Carafas v. LaVallee">391 U. S. 234</a></span> (1968); and <em>Ginsberg </em>v. <em>New York, </em><span class="citation" data-id="9423666"><a href="/opinion/107663/ginsberg-v-new-york/" aria-description="Citation for case: Ginsberg v. New York">390 U. S. 629</a></span> (1968), bear witness to the fact that this Court has long since departed from the rule announced in <em>St. <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">Pierre, supra.</a></span> </em>These more recent cases have held that the possibility of a criminal defendant’s suffering “collateral legal consequences” from a sentence already served permits him to have his claims reviewed here on the merits. If the prospect of the State’s visiting such collateral consequences on a criminal defendant who has served his sentence is a sufficient burden as to enable him to seek reversal of a decision affirming his conviction, the prospect of the State’s inability to impose such a burden following a reversal of the conviction of a criminal defendant in its own courts must likewise be sufficient to enable the State to obtain review of its claims on the merits here. In any future state criminal proceedings against respondent, this conviction may be relevant to setting bail and length of sentence, and to the availability of probation. 18 Pa. Cons. Stat. Ann. §§ 1321, 1322, 1331, 1332 (Purdon Supp. 1977); Pa. Rule Crim. Proc. 4004. In view of the fact that respondent, having fully served his state sentence, is presently incarcerated in the federal penitentiary at Lewisburg, Pa., we cannot say that such considerations are unduly specula<page-number citation-index="1" label="109">*109</page-number>tive even if a determination of mootness depended on a case-by-case analysis.</p>
</footnote>
<footnote label="4">
<p id="b281-9"> Operating an improperly licensed motor vehicle was at the time of the incident covered by 1959 Pa. Laws, No. 32, which was found in Pa. Stat. Ann., Tit. 75, §511 (a) (Purdon 1971), and has been repealed by 1976 Pa. Laws, No. 81, § 7, effective July 1, 1977. This offense now appears to be covered by 75 Pa. Cons. Stat. Ann. §§ 1301, 1302 (Purdon 1977).</p>
</footnote>
<footnote label="5">
<p id="b282-6"> The State does not, and need not, go so far as to suggest that an officer may frisk the occupants of any car stopped for a traffic violation. Rather, it only argues that it is permissible to order the driver out of the car. In this particular case, argues the State, once the driver alighted, the officer had independent reason to suspect criminal activity and present danger and it was upon this basis, and not the mere fact that respondent had committed a traffic violation, that he conducted the search.</p>
</footnote>
<footnote label="6">
<p id="b283-7"> Contrary to the suggestion in the dissent of our Brother Stevens, <em>post, </em>at 122, we do not hold today that “whenever an officer has an occasion to speak with the driver of a vehicle, he may also order the driver out of the car.” We hold only that once a motor vehicle has been lawfully detained for a traffic violation, the police officers may order the driver to get out of the vehicle without violating the Fourth Amendment’s proscription of unreasonable searches and seizures.</p>
</footnote>
<footnote label="7">
<p id="b284-10"> 392 U. S., at 21-22.</p>
</footnote>
</opinion>
```

---
