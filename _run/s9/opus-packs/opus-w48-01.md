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

## GROUP: content/cases/New York v. Quarles.md  (`case`, 5 assertions)

### content_page

```
---
title: "New York v. Quarles"
type: case
citation: "467 U.S. 649 (1984)"
parallel_cite: "104 S. Ct. 2626; 81 L. Ed. 2d 550; 52 U.S.L.W. 4790"
neutral_cite: 1984 U.S. LEXIS 111
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-06-12
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-06-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: New York v. Quarles
  varies_by_point: false
  scope_note: "Establishes the public-safety exception to Miranda; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111214/new-york-v-quarles/"
  cluster_id: 111214
  opinion_id: 9429664
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[Berkemer v. McCarty]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "public-safety-exception", "interrogation"]
holding: "There is a \"public safety\" exception to Miranda — when officers ask questions reasonably prompted by an immediate threat to public…"
lake:
  record_id: New York v. Quarles
  status: verified
  projected_at: 2026-07-06
---

# New York v. Quarles

*467 U.S. 649 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A woman told officers she had just been raped by an armed man who had entered a supermarket. An officer chased and apprehended Quarles inside the store, found he was wearing an empty shoulder holster, handcuffed him, and — before giving *[[Miranda v. Arizona|Miranda]]* warnings — asked where the gun was. Quarles nodded toward some cartons and said "the gun is over there"; the officer retrieved a loaded revolver.

## Issue
Whether there is an exception to *[[Miranda v. Arizona|Miranda]]* for questions reasonably prompted by a concern for public safety.

## Rule
Yes. "We hold that on these facts there is a 'public safety' exception to the requirement that *Miranda* warnings be given before a suspect's answers may be admitted into evidence, . . . and that the availability of that exception does not depend upon the motivation of the individual officers involved." — 467 U.S. at 655–56. ^pin-655

"We conclude that the need for answers to questions in a situation posing a threat to the public safety outweighs the need for the prophylactic rule protecting the Fifth Amendment's privilege against self-incrimination." — *Id.* at 657. ^pin-657

## Application
The unholstered, hidden gun in a public supermarket posed an immediate danger to the public and police, so the officer's question about its location fell within the public-safety exception. Both the statement "the gun is over there" and the gun itself were admissible despite the absence of *[[Miranda v. Arizona|Miranda]]* warnings, and the officer's actual motivation for asking was irrelevant.

## Conclusion
The statement and the gun were admissible under the public-safety exception; the New York Court of Appeals' suppression order was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Quarles* carves a public-safety exception out of [[Miranda v. Arizona]], turning on the objective existence of a public-safety concern rather than the officer's subjective motive.

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *New York v. Quarles*, 467 U.S. 649 (1984) — https://www.courtlistener.com/opinion/111214/new-york-v-quarles/ — pinpoints: 655–56, 657.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bf10aef400c8053d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "467 U.S. 649 (1984)", "court": "U.S. Supreme Court", "neutral_cite": "1984 U.S. LEXIS 111", "official_citation_present": true, "parallel_cite": "104 S. Ct. 2626; 81 L. Ed. 2d 550; 52 U.S.L.W. 4790", "title": "New York v. Quarles", "year": "1984"}}
{"assertion_id": "cfb65942142d6085", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "There is a \\\"public safety\\\" exception to Miranda — when officers ask questions reasonably prompted by an immediate threat to public…", "title": "New York v. Quarles"}}
{"assertion_id": "eb9c12f79f731433", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Progeny / Refinement", "title": "New York v. Quarles"}}
{"assertion_id": "31ddc38c6041b7f2", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1984-06-12", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "New York v. Quarles", "field_i_validity": "good_law", "scope_note": "Establishes the public-safety exception to Miranda; good law.", "title": "New York v. Quarles", "varies_by_point": "false"}}
{"assertion_id": "6e8ad13af71bb25a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "New York v. Quarles"}}
```

### lake record — New York v. Quarles

```json
{
  "schema_version": "s2.v1",
  "record_id": "New York v. Quarles",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "New York v. Quarles",
    "case_name_short": "Quarles",
    "case_name_full": "New York v. Quarles",
    "input_case_name": "New York v. Quarles",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-06-12",
    "year": 1984,
    "docket": null,
    "cluster_id": 111214,
    "lead_opinion_id": 9429664,
    "sibling_ids": [
      111214,
      9429664,
      9429665,
      9429666
    ],
    "absolute_url": "/opinion/111214/new-york-v-quarles/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "467 U.S. 649",
      "volume": "467",
      "reporter": "U.S.",
      "page": "649",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 2626",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2626",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 L. Ed. 2d 550",
        "volume": "81",
        "reporter": "L. Ed. 2d",
        "page": "550",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4790",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4790",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 111",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "111",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "467 U.S. 649",
        "volume": "467",
        "reporter": "U.S.",
        "page": "649",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 2626",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2626",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 L. Ed. 2d 550",
        "volume": "81",
        "reporter": "L. Ed. 2d",
        "page": "550",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 111",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "111",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4790",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4790",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "467 U.S. 649",
    "official_selection": {
      "court_class": "scotus",
      "selected": "467 U.S. 649",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-655",
      "page": null,
      "quote": "; the officer retrieved a loaded revolver. ## Issue Whether there is an exception to *Miranda* for questions reasonably prompted by a concern for public safety. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-657",
      "page": null,
      "quote": "We conclude that the need for answers to questions in a situation posing a threat to the public safety outweighs the need for the prophylactic rule protecting the Fifth Amendment's privilege against self-incrimination.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-06-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "New York v. Quarles",
    "varies_by_point": false,
    "scope_note": "Establishes the public-safety exception to Miranda; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Earl",
          "cluster_id": 9404588,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane1_negative"
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
        "journal_ref": "New York v. Quarles:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Castano",
          "cluster_id": 4432551,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane1_negative"
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
        "journal_ref": "New York v. Quarles:lane1_negative"
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
        "journal_ref": "New York v. Quarles:lane1_negative"
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
        "journal_ref": "New York v. Quarles:lane1_negative"
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
        "journal_ref": "New York v. Quarles:lane1_negative"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Berkemer v. McCarty",
          "cluster_id": 111249,
          "cite": [
            "82 L. Ed. 2d 317",
            "104 S. Ct. 3138",
            "468 U.S. 420",
            "1984 U.S. LEXIS 140",
            "52 U.S.L.W. 5023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Heller",
          "cluster_id": 145777,
          "cite": [
            "171 L. Ed. 2d 637",
            "128 S. Ct. 2783",
            "554 U.S. 570",
            "2008 U.S. LEXIS 5268"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Ritchie",
          "cluster_id": 111822,
          "cite": [
            "94 L. Ed. 2d 40",
            "107 S. Ct. 989",
            "480 U.S. 39",
            "1987 U.S. LEXIS 558",
            "55 U.S.L.W. 4180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chavez v. Martinez",
          "cluster_id": 127927,
          "cite": [
            "155 L. Ed. 2d 984",
            "123 S. Ct. 1994",
            "538 U.S. 760",
            "2003 U.S. LEXIS 4274"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Coffman",
          "cluster_id": 2623595,
          "cite": [
            "96 P.3d 30",
            "17 Cal. Rptr. 3d 710",
            "34 Cal. 4th 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Howes v. Fields",
          "cluster_id": 623144,
          "cite": [
            "182 L. Ed. 2d 17",
            "132 S. Ct. 1181",
            "565 U.S. 499",
            "2012 U.S. LEXIS 1077",
            "2012 WL 538280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Walton",
          "cluster_id": 2355344,
          "cite": [
            "41 S.W.3d 75",
            "2001 Tenn. LEXIS 222"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duckworth v. Eagan",
          "cluster_id": 112322,
          "cite": [
            "106 L. Ed. 2d 166",
            "109 S. Ct. 2875",
            "492 U.S. 195",
            "1989 U.S. LEXIS 3196",
            "57 U.S.L.W. 4942"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Withrow v. Williams",
          "cluster_id": 112847,
          "cite": [
            "123 L. Ed. 2d 407",
            "113 S. Ct. 1745",
            "507 U.S. 680",
            "1993 U.S. LEXIS 2980"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Panah",
          "cluster_id": 2509294,
          "cite": [
            "107 P.3d 790",
            "25 Cal. Rptr. 3d 672",
            "35 Cal. 4th 395",
            "2005 Cal. Daily Op. Serv. 2194",
            "2005 Daily Journal DAR 3023",
            "2005 Cal. LEXIS 2712"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Connecticut v. Barrett",
          "cluster_id": 111796,
          "cite": [
            "93 L. Ed. 2d 920",
            "107 S. Ct. 828",
            "479 U.S. 523",
            "1987 U.S. LEXIS 419",
            "55 U.S.L.W. 4151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111214 OR 9429664 OR 9429665 OR 9429666) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzA3NjY0MDAwMDAwJnM9NTk2ODYyOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111214+OR+9429664+OR+9429665+OR+9429666%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111214 OR 9429664 OR 9429665 OR 9429666)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNjEmcz0xMjQ0NzUyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111214+OR+9429664+OR+9429665+OR+9429666%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111214 OR 9429664 OR 9429665 OR 9429666)",
        "reviewed": 53,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 53,
        "triage_read": 0,
        "triage_snippet_classified": 53
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111214 OR 9429664 OR 9429665 OR 9429666)",
    "indexed_citing_opinions": 925,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111214,
        "count": 782,
        "count_source": "search"
      },
      {
        "opinion_id": 9429664,
        "count": 160,
        "count_source": "search"
      },
      {
        "opinion_id": 9429665,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429666,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1468,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/new-york-v-quarles.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3MzIwNTEmcz05NDkzMDI5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111214+OR+9429664+OR+9429665+OR+9429666%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111214,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 100474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 103320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 104010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108846,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109207,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109590,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110667,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 111023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 111051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 111105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 336178,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 375540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 1173989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 2499246,
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
    "date_created": "2026-07-05T15:48:41Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:48:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:48:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:52:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:48:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — New York v. Quarles

```
<opinion type="majority">
<author id="b709-4"><page-number citation-index="1" label="651">*651</page-number>Justice Rehnquist</author>
<p id="Ani">delivered the opinion of the Court.</p>
<p id="b709-5">Respondent Benjamin Quarles was charged in the New York trial court with criminal possession of a weapon. The trial court suppressed the gun in question, and a statement made by respondent, because the statement was obtained by police before they read respondent his <em>“Miranda </em>rights.” That ruling was affirmed on appeal through the New York Court of Appeals. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./461/942/">461 U. S. 942</a></span> (1983), and we now reverse.<footnotemark>1</footnotemark> We conclude that under the circumstances involved in this case, overriding considerations of public safety justify the officer’s failure to provide <em>Miranda </em>warnings before he asked questions devoted to locating the abandoned weapon.</p>
<p id="b709-6">On September 11, 1980, at approximately 12:30 a. m., Officer Frank Kraft and Officer Sal Scarring were on road patrol in Queens, N. Y., when a young woman approached their car. She told them that she had just been raped by a black male, approximately six feet tall, who was wearing a black jacket with the name “Big Ben” printed in yellow letters on the back. She told the officers that the man had just entered <page-number citation-index="1" label="652">*652</page-number>an A &amp; P supermarket located nearby and that the man was carrying a gun.</p>
<p id="b710-5">The officers drove the woman to the supermarket, and Officer Kraft entered the store while Officer Scarring radioed for assistance. Officer Kraft quickly spotted respondent, who matched the description given by the woman, approaching a checkout counter. Apparently upon seeing the officer, respondent turned and ran toward the rear of the store, and Officer Kraft pursued him with a drawn gun. When respondent turned the corner at the end of an aisle, Officer Kraft lost sight of him for several seconds, and upon regaining sight of respondent, ordered him to stop and put his hands over his head.</p>
<p id="b710-6">Although more than three other officers had arrived on the scene by that time, Officer Kraft was the first to reach respondent. He frisked him and discovered that he was wearing a shoulder holster which was then empty. After handcuffing him, Officer Kraft asked him where the gun was. Respondent nodded in the direction of some empty cartons and responded, “the gun is over there.” Officer Kraft thereafter retrieved a loaded .38-caliber revolver from one of the cartons, formally placed respondent under arrest, and read him his <em>Miranda </em>rights from a printed card. Respondent indicated that he would be willing to answer questions without an attorney present. Officer Kraft then asked respondent if he owned the gun and where he had purchased it. Respondent answered that he did own it and that he had purchased it in Miami, Fla.</p>
<p id="b710-7">In the subsequent prosecution of respondent for criminal possession of a weapon,<footnotemark>2</footnotemark> the judge excluded the statement, “the gun is over there,” and the gun because the officer had not given respondent the warnings required by our decision in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), before asking <page-number citation-index="1" label="653">*653</page-number>him where the gun was located. The judge excluded the other statements about respondent’s ownership of the gun and the place of purchase, as evidence tainted by the prior <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>violation. The Appellate Division of the Supreme Court of New York affirmed without opinion. 85 App. Div. 2d 936, 447 N. Y. S. 2d 84 (1981).</p>
<p id="A6W">The Court of Appeals granted leave to appeal and affirmed by a 4-3 vote. 58 N. Y. 2d 664, <span class="citation" data-id="5535302"><a href="/opinion/5686260/people-v-quarles/" aria-description="Citation for case: People v. Quarles">444 N. E. 2d 984</a></span> (1982). It concluded that respondent was in “custody” within the meaning of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>during all questioning and rejected the State’s argument that the exigencies of the situation justified Officer Kraft’s failure to read respondent his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights until after he had located the gun. The court declined to recognize an exigency exception to the usual requirements of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>because it found no indication from Officer Kraft’s testimony at the suppression hearing that his subjective motivation in asking the question was to protect his own safety or the safety of the public. 58 N. Y. 2d, at 666, <span class="citation" data-id="5535302"><a href="/opinion/5686260/people-v-quarles/#985" aria-description="Citation for case: People v. Quarles">444 N. E. 2d, at 985</a></span>. For the reasons which follow, we believe that this case presents a situation where concern for public safety must be paramount to adherence to the literal language of the prophylactic rules enunciated in Miranda.<footnotemark>3</footnotemark></p>
<p id="b712-4"><page-number citation-index="1" label="654">*654</page-number>The Fifth Amendment guarantees that “[n]o person . . . shall be compelled in any criminal case to be a witness against himself.” In <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>this Court for the first time extended the Fifth Amendment privilege against compulsory self-incrimination to individuals subjected to custodial interrogation by the police. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#460" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 460-461, 467</a></span>. The Fifth Amendment itself does not prohibit all incriminating admissions; “[ajbsent some officially <em>coerced </em>self-accusation, the Fifth Amendment privilege is not violated by even the most damning admissions.” <em>United States </em>v. <em>Washington, </em><span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#187" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 187</a></span> (1977) (emphasis added). The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court, however, presumed that interrogation in certain custodial circumstances<footnotemark>4</footnotemark> is inherently coercive and held that statements made under those circumstances are inadmissible unless the suspect is specifically informed of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights and freely decides to forgo those rights. The prophylactic <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings therefore are “not themselves rights protected by the Constitution but [are] instead measures to insure that the right against compulsory self-incrimination [is] protected.” <em>Michigan </em>v. <em>Tucker, </em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 444</a></span> (1974); see <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#492" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477, 492</a></span> (1981) (Powell, J., concurring). Requiring <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings before custodial interrogation provides “practical reinforcement” for the Fifth Amendment right. <em>Michigan </em>v. <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker"><em>Tucker, supra, </em>at 444</a></span>.</p>
<p id="b712-6">In this case we have before us no claim that respondent’s statements were actually compelled by police conduct which overcame his will to resist. See <em>Beckwith </em>v. <em>United States, </em><span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/#347" aria-description="Citation for case: Beckwith v. United States">425 U. S. 341, 347-348</a></span> (1976); <em>Davis </em>v. <em>North Carolina, </em><span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737</a></span> (1966). Thus the only issue before us is whether <page-number citation-index="1" label="655">*655</page-number>Officer Kraft was justified in failing to make available to respondent the procedural safeguards associated with the privilege against compulsory self-incrimination since Miranda.<footnotemark>5</footnotemark></p>
<p id="b713-5">The New York Court of Appeals was undoubtedly correct in deciding that the facts of this case come within the ambit of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>decision as we have subsequently interpreted it. We agree that respondent was in police custody because we have noted that “the ultimate inquiry is simply whether there is a ‘formal arrest or restraint on freedom of movement’ of the degree associated with a formal arrest,” <em>California </em>v. <em>Beheler, </em><span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler">463 U. S. 1121, 1125</a></span> (1983) <em>(per curiam), </em>quoting <em>Oregon </em>v. <em>Mathiason, </em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492, 495</a></span> (1977) <em>(per curiam). </em>Here Quarles was surrounded by at least four police officers and was handcuffed when the questioning at issue took place. As the New York Court of Appeals observed, there was nothing to suggest that any of the officers were any longer concerned for their own physical safety. 58 N. Y. 2d, at 666, <span class="citation" data-id="5535302"><a href="/opinion/5686260/people-v-quarles/#985" aria-description="Citation for case: People v. Quarles">444 N. E. 2d, at 985</a></span>. The New York Court of Appeals’ majority declined to express an opinion as to whether there might be an exception to the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rule if the police had been acting to protect the public, because the lower courts in New York had made no factual determination that the police had acted with that motive. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></em></p>
<p id="b713-6">We hold that on these facts there is a “public safety” exception to the requirement that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings be given before a suspect’s answers may be admitted into evidence, <page-number citation-index="1" label="656">*656</page-number>and that the availability of that exception does not depend upon the motivation of the individual officers involved. In a kaleidoscopic situation such as the one confronting these officers, where spontaneity rather than adherence to a police manual is necessarily the order of the day, the application of the exception which we recognize today should not be made to depend on <em>post hoc </em>findings at a suppression hearing concerning the subjective motivation of the arresting officer.<footnotemark>6</footnotemark> Undoubtedly most police officers, if placed in Officer Kraft’s position, would act out of a host of different, instinctive, and largely unverifiable motives — their own safety, the safety of others, and perhaps as well the desire to obtain incriminating evidence from the suspect.</p>
<p id="b714-5">Whatever the motivation of individual officers in such a situation, we do not believe that the doctrinal underpinnings of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>require that it be applied in all its rigor to a situation in which police officers ask questions reasonably prompted by a concern for the public safety. The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>decision was based in large part on this Court’s view that the warnings which it required police to give to suspects in custody would reduce the likelihood that the suspects would fall victim to constitutionally impermissible practices of police interrogation in the presumptively coercive environment of the station house. 384 U. S., at 455-458. The dissenters warned that the requirement of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings would have the effect of decreasing the number of suspects who respond to police questioning. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#504" aria-description="Citation for case: Miranda v. Arizona">Id., at 504, 516-517</a></span> (Harlan, J., joined by Stewart and White, JJ., dissenting). The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>majority, however, apparently felt that whatever the <page-number citation-index="1" label="657">*657</page-number>cost to society in terms of fewer convictions of guilty suspects, that cost would simply have to be borne in the interest of enlarged protection for the Fifth Amendment privilege.</p>
<p id="b715-5">The police in this case, in the very act of apprehending a suspect, were confronted with the immediate necessity of ascertaining the whereabouts of a gun which they had every reason to believe the suspect had just removed from his empty holster and discarded in the supermarket. So long as the gun was concealed somewhere in the supermarket, with its actual whereabouts unknown, it obviously posed more than one danger to the public safety: an accomplice might make use of it, a customer or employee might later come upon it.</p>
<p id="b715-6">In such a situation, if the police are required to recite the familiar <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings before asking the whereabouts of the gun, suspects in Quarles’ position might well be deterred from responding. Procedural safeguards which deter a suspect from responding were deemed acceptable in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>in order to protect the Fifth Amendment privilege; when the primary social cost of those added protections is the possibility of fewer convictions, the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>majority was willing to bear that cost. Here, had <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings deterred Quarles from responding to Officer Kraft’s question about the whereabouts of the gun, the cost would have been something more than merely the failure to obtain evidence useful in convicting Quarles. Officer Kraft needed an answer to his question not simply to make his case against Quarles but to insure that further danger to the public did not result from the concealment of the gun in a public area.</p>
<p id="b715-7">We conclude that the need for answers to questions in a situation posing a threat to the public safety outweighs the need for the prophylactic rule protecting the Fifth Amendment’s privilege against self-incrimination. We decline to place officers such as Officer Kraft in the untenable position of having to consider, often in a matter of seconds, whether it best serves society for them to ask the necessary questions without the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and render whatever proba<page-number citation-index="1" label="658">*658</page-number>tive evidence they uncover inadmissible, or for them to give the warnings in order to preserve the admissibilty of evidence they might uncover but possibly damage or destroy their ability to obtain that evidence and neutralize the volatile situation confronting them.<footnotemark>7</footnotemark> ■</p>
<p id="b716-5">In recognizing a narrow exception to the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rule in this case, we acknowledge that to some degree we lessen the desirable clarity of that rule. At least in part in order to preserve its clarity, we have over the years refused to sanction attempts to expand our <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>holding. See, <em>e. g., Minnesota </em>v. <em>Murphy, </em><span class="citation" data-id="9429504"><a href="/opinion/111105/minnesota-v-murphy/" aria-description="Citation for case: Minnesota v. Murphy">465 U. S. 420</a></span> (1984) (refusal to extend <em>Miranda </em>requirements to interviews with probation officers); <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707</a></span> (1979) (refusal to equate request to see a probation officer with request to see a lawyer for <em>Miranda </em>purposes); <em>Beckwith </em>v. <em>United States, </em><span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/" aria-description="Citation for case: Beckwith v. United States">425 U. S. 341</a></span> (1976) (refusal to extend <em>Miranda </em>requirements to questioning in noncustodial circumstances). As we have in other contexts, we recognize here the importance of a workable rule “to guide police officers, who have only limited time and expertise to reflect on and balance the social and individual interests involved in the specific circumstances they confront.” <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#213" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 213-214</a></span> (1979). But as we have pointed out, we believe that the exception which we recognize today lessens the necessity of that on-the-scene balancing process. The exception will not be difficult for police officers to apply because in each case it will be circumscribed by the exigency which justifies it. We think police officers can and will distinguish almost in<page-number citation-index="1" label="659">*659</page-number>stinctively between questions necessary to secure their own safety or the safety of the public and questions designed solely to elicit testimonial evidence from a suspect.</p>
<p id="b717-5">The facts of this case clearly demonstrate that distinction and an officer’s ability to recognize it. Officer Kraft asked only the question necessary to locate the missing gun before advising respondent of his rights. It was only after securing the loaded revolver and giving the warnings that he continued with investigatory questions about the ownership and place of purchase of the gun. The exception which we recognize today, far from complicating the thought processes and the on-the-scene judgments of police officers, will simply free them to follow their legitimate instincts when confronting situations presenting a danger to the public safety.<footnotemark>8</footnotemark></p>
<p id="b717-6">We hold that the Court of Appeals in this case erred in excluding the statement, “the gun is over there,” and the gun because of the officer’s failure to read respondent his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights before attempting to locate the weapon. Ac<page-number citation-index="1" label="660">*660</page-number>cordingly we hold that it also erred in excluding the subsequent statements as illegal fruits of a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>violation.<footnotemark>9</footnotemark> We therefore reverse and remand for further proceedings not inconsistent with this opinion.</p>
<p id="b718-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b709-7"> Although respondent has yet to be tried in state court, the suppression ruling challenged herein is a “final judgment” within the meaning of <span class="citation no-link">28 U. S. C. § 1257</span>(3), and we have jurisdiction over this case. In <em>Cox Broadcasting Corp. </em>v. <em>Cohn, </em><span class="citation" data-id="9426016"><a href="/opinion/109207/cox-broadcasting-corp-v-cohn/#477" aria-description="Citation for case: Cox Broadcasting Corp. v. Cohn">420 U. S. 469, 477</a></span> (1975), we identified four categories of cases where the Court will treat a decision of the highest state court as final for § 1257 purposes even though further proceedings are anticipated in the lower state courts. This ease, which comes to this Court in the same posture as <em>Michigan </em>v. <em>Clifford, </em><span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/" aria-description="Citation for case: Michigan v. Clifford">464 U. S. 287</a></span> (1984), decided earlier this Term, falls within the category which includes “those situations where the federal claim has been finally decided . . . but in which later review of the federal issue cannot be had, whatever the ultimate outcome of the case.” <span class="citation" data-id="9426016"><a href="/opinion/109207/cox-broadcasting-corp-v-cohn/#481" aria-description="Citation for case: Cox Broadcasting Corp. v. Cohn">420 U. S., at 481</a></span>. In this case should the State convict respondent at trial, its claim that certain evidence was wrongfully suppressed will be moot. Should respondent be acquitted at trial, the State will be precluded from pressing its federal claim again on appeal. See <em>California </em>v. <em>Stewart, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#498" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 498, n. 71</a></span> (1966) (decided with <em>Miranda </em>v. <em>Arizona).</em></p>
</footnote>
<footnote label="2">
<p id="b710-8"> The State originally charged respondent with rape, but the record provides no information as to why the State failed to pursue that charge.</p>
</footnote>
<footnote label="3">
<p id="Aq9"> We have long recognized an exigent-circumstances exception to the warrant requirement in the Fourth Amendment context. See, <em>e. g., Michigan </em>v. <em>Tyler, </em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#509" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 509</a></span> (1978); <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298-300</a></span> (1967); <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14-15</a></span> (1948). We have found the warrant requirement of the Fourth Amendment inapplicable in cases where the “ ‘exigencies of the situation’ make the needs of law enforcement so compelling that the warrantless search is objectively reasonable under the Fourth Amendment.” <em>Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#394" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 394</a></span> (1978), quoting <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#456" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 456</a></span> (1948). Although “the Fifth Amendment’s strictures, unlike the Fourth’s, are not removed by showing reasonableness,” <em>Fisher </em>v. <em>United States, </em><span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#400" aria-description="Citation for case: Fisher v. United States">425 U. S. 391, 400</a></span> (1976), we conclude today that there are limited circumstances where the judicially imposed strictures of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>are inapplicable.</p>
</footnote>
<footnote label="4">
<p id="b712-7"> <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>on its facts applies to station house questioning, but we have not so limited it in our subsequent cases, often over strong dissent. See, <em>e. g., Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291</a></span> (1980) (police car); <em>Orozco </em>v. <em>Texas, </em><span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">394 U. S. 324</a></span> (1969) (defendant’s bedroom); <em>Mathis </em>v. <em>United States, </em><span class="citation" data-id="9423682"><a href="/opinion/107676/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">391 U. S. 1</a></span> (1968) (prison cell during defendant’s sentence for an unrelated offense); but see <em>Orozco </em>v. <span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/#328" aria-description="Citation for case: Orozco v. Texas"><em>Texas, supra, </em>at 328-331</a></span> (White, J., dissenting).</p>
</footnote>
<footnote label="5">
<p id="b713-7"> The dissent curiously takes us to task for “endors[ing] the introduction of coerced self-incriminating statements in criminal prosecutions,” <em>post, </em>at 674, and for “sanction[ing] <em>sub silentio </em>criminal prosecutions based on compelled self-incriminating statements.” <em>Post, </em>at 686. Of course our decision today does nothing of the kind. As the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court itself recognized, the failure to provide <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings in and of itself does not render a confession involuntary, <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#457" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 457</a></span>, and respondent is certainly free on remand to argue that his statement was coerced under traditional due process standards. Today we merely reject the only argument that respondent has raised to support the exclusion of his statement, that the statement must be <em>presumed </em>compelled because of Officer Kraft’s failure to read him his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings.</p>
</footnote>
<footnote label="6">
<p id="b714-6"> Similar approaches have been rejected in other contexts. See <em>Rhode Island </em>v. <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis"><em>Innis, supra, </em>at 301</a></span> (officer’s subjective intent to incriminate not determinative of whether “interrogation” occurred); <em>United States </em>v. <em>Men-denhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 554</a></span>, and n. 6 (1980) (opinion of Stewart, J.) (officer’s subjective intent to detain not determinative of whether a “seizure” occurred within the meaning of the Fourth Amendment); <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#236" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 236</a></span>, and n. 7 (1973) (officer’s subjective fear not determinative of necessity for “search incident to arrest” exception to the Fourth Amendment warrant requirement).</p>
</footnote>
<footnote label="7">
<p id="b716-6"> The dissent argues that a public safety exception to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>is unnecessary because in every case an officer can simply ask the necessary questions to protect himself or the public, and then the prosecution can decline to introduce any incriminating responses at a subsequent trial. <em>Post, </em>at 686. But absent actual coercion by the officer, there is no constitutional imperative requiring the exclusion of the evidence that results from police inquiry of this kind; and we do not believe that the doctrinal underpinnings of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>require us to exclude the evidence, thus penalizing officers for asking the very questions which are the most crucial to their efforts to protect themselves and the public.</p>
</footnote>
<footnote label="8">
<p id="b717-7"> Although it involves police questions in part relating to the whereabouts of a gun, <em>Orozco </em>v. <em>Texas, </em><span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">394 U. S. 324</a></span> (1969), is in no sense inconsistent with our disposition of this ease. In <em><span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">Orozco</a></span> </em>four hours after a murder had been committed at a restaurant, four police officers entered the defendant’s boardinghouse and awakened the defendant, who was sleeping in his bedroom. Without giving him <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, they began vigorously to interrogate him about whether he had been present at the scene of the shooting and whether he owned a gun. The defendant eventually admitted that he had been present at the scene and directed the officers to a washing machine in the backroom of the boardinghouse where he had hidden the gun. We held that all the statements should have been suppressed. In <em><span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">Orozco</a></span>, </em>however, the questions about the gun were clearly investigatory; they did not in any way relate to an objectively reasonable need to protect the police or the public from any immediate danger associated with the weapon. In short there was no exigency requiring immediate action by the officers beyond the normal need expeditiously to solve a serious crime.</p>
<p id="b717-8"><em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291</a></span> (1980), also involved the whereabouts of a missing weapon, but our holding in that case depended entirely on our conclusion that no police interrogation took place so as to require consideration of the applicability of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>prophylactic.</p>
</footnote>
<footnote label="9">
<p id="b718-8"> Because we hold that there is no violation of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>in this case, we have no occasion to reach arguments made by the State and the United States as <em>amicus curiae </em>that the gun is admissible either because it is nontestimonial or because the police would inevitably have discovered it absent their questioning.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Nieves v. Bartlett.md  (`case`, 5 assertions)

### content_page

```
---
title: Nieves v. Bartlett
type: case
citation: "587 U.S. 391 (2019)"
parallel_cite: 139 S. Ct. 1715
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2019
date_decided: ""
docket: 17-1174
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
  opinion_url: "https://www.courtlistener.com/opinion/9231236/nieves-v-bartlett/"
  cluster_id: 9231236
  opinion_id: null
  identity_checked: true
lake:
  record_id: Nieves v. Bartlett
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Retaliatory Arrest]]"
    role: Key
related:
  - "[[Gonzalez v. Trevino]]"
  - "[[Retaliatory Arrest]]"
tags:
  - case
  - first-amendment
  - retaliatory-arrest
  - probable-cause
  - section-1983
holding: "A First Amendment retaliatory-arrest plaintiff must generally plead and prove the absence of probable cause for the arrest, subject to a narrow exception when he presents objective evidence that otherwise similarly situated individuals not engaged in the same protected speech were not arrested."
---

# Nieves v. Bartlett

*587 U.S. 391 (2019)* (No. 17-1174) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9231236 → opinion 9226038; quote string-matched to the CL opinion text 2026-07-07 (CL text carries S. Ct. star-pagination; U.S. pincite corroborated by Gonzalez v. Trevino, 602 U.S. 653). S9 promotes. -->

## Background
Russell Bartlett was arrested for disorderly conduct and resisting arrest during "Arctic Man," a raucous winter sports festival in Alaska, after tense encounters with two state troopers — he had declined to speak with one officer and had intervened when the other questioned a minor. Bartlett sued under 42 U.S.C. § 1983, alleging the officers arrested him in retaliation for that protected speech in violation of the First Amendment. The Ninth Circuit held that the existence of probable cause did not defeat his retaliatory-arrest claim.

## Issue
Whether probable cause defeats a First Amendment retaliatory-arrest claim under § 1983, and if so, whether any exception exists.

## Rule
As a general rule, a plaintiff bringing a retaliatory-arrest claim "must plead and prove the absence of probable cause for the arrest." 587 U.S., at 402. Because the presence of probable cause will be at issue in virtually every such case and its objective character screens out weak claims of retaliatory animus, the no-probable-cause requirement is the threshold a plaintiff must clear. The Court recognized one narrow exception: "we conclude that the no-probable-cause requirement should not apply when a plaintiff presents objective evidence that he was arrested when otherwise similarly situated individuals not engaged in the same sort of protected speech had not been." — 587 U.S. at 406. ^pin-406

## Application
Bartlett's claim failed at the threshold. Probable cause supported his arrest for disorderly conduct and resisting, and he offered no objective evidence that officers typically exercise their discretion not to arrest others engaged in similar conduct but not in protected speech. Absent that comparative showing, the general no-probable-cause bar controlled and his retaliatory-arrest claim could not proceed. The Court grounded the rule in the practical difficulty of disentangling protected speech from legitimate arrest justifications and in the analogous causation framework of *Hartman v. Moore*.

## Conclusion
The judgment of the Ninth Circuit was **reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Roberts, C.J., delivered the opinion of the Court; Justices Thomas, Gorsuch, and Ginsburg concurred in part and/or dissented in part, and Justice Sotomayor dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Nieves* remains the controlling framework for retaliatory-arrest claims; the Supreme Court construed its exception in *[[Gonzalez v. Trevino]]* (2024), rejecting a demand for narrow comparator evidence.

## Appears on
- [[Retaliatory Arrest]] — *Key*

## Sources
- [*Nieves v. Bartlett*, 587 U.S. 391 (2019)](https://www.courtlistener.com/opinion/9231236/nieves-v-bartlett/) — pinpoint: 406 (exception; Opinion of the Court). Quote string-matched to the CL opinion text (139 S. Ct. 1715, at 1727) 2026-07-07; U.S.-reporter pincite corroborated by *Gonzalez v. Trevino*, 602 U.S. 653, 658 (2024).
- [*Gonzalez v. Trevino*, 602 U.S. 653 (2024)](https://www.courtlistener.com/opinion/10600071/gonzalez-v-trevino/) — construing the *Nieves* exception.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "99829aba1c00843b", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "587 U.S. 391 (2019)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "139 S. Ct. 1715", "title": "Nieves v. Bartlett", "year": "2019"}}
{"assertion_id": "66d2cea9a4441883", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A First Amendment retaliatory-arrest plaintiff must generally plead and prove the absence of probable cause for the arrest, subject to a narrow exception when he presents objective evidence that otherwise similarly situated individuals not engaged in the same protected speech were not arrested.", "title": "Nieves v. Bartlett"}}
{"assertion_id": "ae0afcf0b2451871", "dimension": "support", "kind": "home_role", "locator": {"home": "Retaliatory Arrest"}, "payload": {"home": "Retaliatory Arrest", "role": "Key", "title": "Nieves v. Bartlett"}}
{"assertion_id": "5398c4dff6f2dc48", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Nieves v. Bartlett"}}
{"assertion_id": "bb97c191b80a8916", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Nieves v. Bartlett", "varies_by_point": "false"}}
```

### lake record — Nieves v. Bartlett

```json
{
  "schema_version": "s2.v1",
  "record_id": "Nieves v. Bartlett",
  "status": "under_review",
  "identity": {
    "case_name": "Nieves v. Bartlett",
    "case_name_short": "Nieves",
    "case_name_full": "Luis A. NIEVES v. Russell P. BARTLETT",
    "input_case_name": "Nieves v. Bartlett",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2019,
    "docket": "17-1174",
    "cluster_id": 9231236,
    "lead_opinion_id": 9226038,
    "sibling_ids": [],
    "absolute_url": "/opinion/9231236/nieves-v-bartlett/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "587 U.S. 391",
      "volume": "587",
      "reporter": "U.S.",
      "page": "391",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "139 S. Ct. 1715",
        "volume": "139",
        "reporter": "S. Ct.",
        "page": "1715",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "587 U.S. 391",
        "volume": "587",
        "reporter": "U.S.",
        "page": "391",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "139 S. Ct. 1715",
        "volume": "139",
        "reporter": "S. Ct.",
        "page": "1715",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "587 U.S. 391",
    "official_selection": {
      "court_class": "scotus",
      "selected": "587 U.S. 391",
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
    "date_created": "2026-07-06T12:14:24Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:14:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:14:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:14:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:14:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "nieves-v-bartlett--9231236",
      "to_record_id": "Nieves v. Bartlett",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Nieves v. Bartlett

```
<opinion type="majority">
<author id="p-7">Chief Justice ROBERTS delivered the opinion of the Court.</author>
<p id="p-8"><a class="page-label" data-citation-index="1" data-label="1720" href="#p1720" id="p1720">*1720</a>Respondent Russell Bartlett sued petitioners-two police officers-alleging that they retaliated against him for his protected First Amendment speech by arresting him for disorderly conduct and resisting arrest. The officers had probable cause to arrest Bartlett, and we now decide whether that fact defeats Bartlett's First Amendment claim as a matter of law.</p>
<p id="p-9">I</p>
<p id="p-10">A</p>
<p id="p-11">Bartlett was arrested during "Arctic Man," a weeklong winter sports festival held in the remote Hoodoo Mountains near Paxson, Alaska. Paxson is a small community that normally consists of a few dozen residents. But once a year, upwards of 10,000 people descend on the area for Arctic Man, an event known for both extreme sports and extreme alcohol consumption. The mainstays are high-speed ski and snowmobile races, bonfires, and parties. During that week, the Arctic Man campground briefly becomes one of the largest and most raucous cities in Alaska.</p>
<p id="p-12">The event poses special challenges for law enforcement. Snowmobiles, alcohol, and freezing temperatures do not always mix well, and officers spend much of the week responding to snowmobile crashes, breaking up fights, and policing underage drinking. Given the remote location of the event, Alaska flies in additional officers from around the State to provide support. Still, the number of police remains limited. Even during the busiest periods of the event, only six to eight officers are on patrol at a time.</p>
<p id="p-13">On the last night of Arctic Man 2014, Sergeant Luis Nieves and Trooper Bryce Weight arrested Bartlett. The parties dispute certain details about the arrest but agree on the general course of events, some of which were captured on video by a local news reporter.</p>
<p id="p-14">At around 1:30 a.m., Sergeant Nieves and Bartlett first crossed paths. Nieves was asking some partygoers to move their beer keg inside their RV because minors had been making off with alcohol. According to Nieves, Bartlett began belligerently yelling to the RV owners that they should not speak with the police. Nieves approached Bartlett to explain the situation, but Bartlett was highly intoxicated and yelled at him to leave. Rather than escalate the situation, Nieves left. Bartlett disputes that account. According to Bartlett, he was not drunk at that time and never yelled at Nieves. He claims it was Nieves who became aggressive when Bartlett refused to speak with him.</p>
<p id="p-15">Several minutes later, Bartlett saw Trooper Weight asking a minor whether he and his underage friends had been drinking. According to Weight, Bartlett approached in an aggressive manner, stood between Weight and the teenager, and yelled with slurred speech that Weight should not speak with the minor. Weight claims that Bartlett then stepped very close to him in a combative way, so Weight pushed him back. Sergeant Nieves saw the <a class="page-label" data-citation-index="1" data-label="1721" href="#p1721" id="p1721">*1721</a>confrontation and rushed over, arriving right after Weight pushed Bartlett. Nieves immediately initiated an arrest, and when Bartlett was slow to comply with his orders, the officers forced him to the ground and threatened to tase him.</p>
<p id="p-16">Again, Bartlett tells a different story. He denies being aggressive, and claims that he stood close to Weight only in an effort to speak over the loud background music. And he was slow to comply with Nieves's orders, not because he was resisting arrest, but because he did not want to aggravate a back injury. After Bartlett was handcuffed, he claims that Nieves said: "[B]et you wish you would have talked to me now." <extracted-citation index="0" url="https://cite.case.law/citations/?q=712%20Fed.%20Appx.%20613"><span class="citation" data-id="4213549"><a href="/opinion/4436296/russell-bartlett-v-luis-nieves/" aria-description="Citation for case: Russell Bartlett v. Luis Nieves">712 Fed. Appx. 613</a></span></extracted-citation>, 616 (C.A.9 2017).</p>
<p id="p-17">The officers took Bartlett to a holding tent, where he was charged with disorderly conduct and resisting arrest. He had sustained no injuries during the episode and was released a few hours later.</p>
<p id="p-18">B</p>
<p id="p-19">The State ultimately dismissed the criminal charges against Bartlett, and Bartlett then sued the officers under <extracted-citation index="1" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation>, which provides a cause of action for state deprivations of federal rights. As relevant here, he claimed that the officers violated his First Amendment rights by arresting him in retaliation for his speech. The protected speech, according to Bartlett, was his refusal to speak with Nieves earlier in the evening and his intervention in Weight's discussion with the underage partygoer. The officers responded that they arrested Bartlett because he interfered with an investigation and initiated a physical confrontation with Weight. The District Court granted summary judgment for the officers. The court determined that the officers had probable cause to arrest Bartlett and held that the existence of probable cause precluded Bartlett's First Amendment retaliatory arrest claim.</p>
<p id="p-20">The Ninth Circuit disagreed. <extracted-citation index="2" url="https://cite.case.law/citations/?q=712%20Fed.%20Appx.%20613"><span class="citation" data-id="4213549"><a href="/opinion/4436296/russell-bartlett-v-luis-nieves/" aria-description="Citation for case: Russell Bartlett v. Luis Nieves">712 Fed. Appx. 613</a></span></extracted-citation>. Relying on its prior decision in <em>Ford v. Yakima</em> , <extracted-citation case-ids="3662237" index="3" url="https://cite.case.law/f3d/706/1188/"><span class="citation" data-id="9502716"><a href="/opinion/820004/eddie-ford-v-city-of-yakima/" aria-description="Citation for case: Eddie Ford v. City of Yakima">706 F. 3d 1188</a></span></extracted-citation> (2013), the court held that a plaintiff can prevail on a First Amendment retaliatory arrest claim even in the face of probable cause for the arrest. According to the Ninth Circuit, Bartlett needed to show only (1) that the officers' conduct would "chill a person of ordinary firmness from future First Amendment activity," and (2) that he had advanced evidence that would "enable him ultimately to prove that the officers' desire to chill his speech was a but-for cause" of the arrest. <extracted-citation index="4" url="https://cite.case.law/citations/?q=712%20Fed.%20Appx.%20613"><span class="citation" data-id="4213549"><a href="/opinion/4436296/russell-bartlett-v-luis-nieves/#616" aria-description="Citation for case: Russell Bartlett v. Luis Nieves">712 Fed. Appx. at 616</a></span></extracted-citation> (internal quotation marks omitted). The court concluded that Bartlett had satisfied both requirements: A retaliatory arrest is sufficiently chilling, and Bartlett had presented enough evidence that his speech was a but-for cause of the arrest. The only causal evidence relied on by the court was Bartlett's affidavit alleging that Sergeant Nieves said "bet you wish you would have talked to me now." If that allegation were true, the court reasoned, a jury might conclude that the officers arrested Bartlett in retaliation for his statements earlier that night.</p>
<p id="p-21">The officers petitioned for review in this Court, and we granted certiorari. 585 U.S. ----, <extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="5" url="https://cite.case.law/s-ct/138/2709/"><span class="citation multiple-matches"><a href="/c/S.Ct./138/2709/">138 S.Ct. 2709</a></span></extracted-citation>, <extracted-citation index="6" url="https://cite.case.law/citations/?q=201%20L.%20Ed.%202d%201095"><span class="citation no-link">201 L.Ed.2d 1095</span></extracted-citation> (2018).</p>
<p id="p-22">II</p>
<p id="p-23">We are asked to resolve whether probable cause to make an arrest defeats a claim that the arrest was in retaliation for speech protected by the First Amendment. We have considered this issue twice in recent years. On the first occasion, we ultimately left the question unanswered because we decided the case on the alternative ground of qualified immunity. See <a class="page-label" data-citation-index="1" data-label="1722" href="#p1722" id="p1722">*1722</a><em>Reichle v. Howards</em> , <extracted-citation case-ids="12190092" index="7" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">566 U.S. 658</a></span></extracted-citation>, <extracted-citation case-ids="12190092" index="8" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">132 S.Ct. 2088</a></span></extracted-citation>, <extracted-citation case-ids="12190092" index="9" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">182 L.Ed.2d 985</a></span></extracted-citation> (2012). We took up the question again last Term in <em>Lozman v.Riviera Beach,</em> 585 U.S. ----, <extracted-citation case-ids="12612344" index="10" url="https://cite.case.law/s-ct/138/1945/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct. 1945</a></span></extracted-citation>, <extracted-citation case-ids="12612344" index="11" url="https://cite.case.law/s-ct/138/1945/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">201 L.Ed.2d 342</a></span></extracted-citation> (2018). <em>Lozman</em> involved unusual circumstances in which the plaintiff was arrested pursuant to an alleged "official municipal policy" of retaliation. <em><extracted-citation case-ids="12612344" index="12" url="https://cite.case.law/s-ct/138/1945/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="13" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct., at 1954</a></span></extracted-citation>. Because those facts were "far afield from the typical retaliatory arrest claim," we reserved judgment on the broader question presented and limited our holding to arrests that result from official policies of retaliation. <em><extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="14" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="15" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct., at 1953</a></span>-1954</extracted-citation>. In such cases, we held, probable cause does not categorically bar a plaintiff from suing the municipality. <em><extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="16" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">Id.,</a></span></extracted-citation></em> at ---- - ----, <extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="17" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct., at 1954</a></span>-1955</extracted-citation>. We now take up the question once again, this time in a more representative case.</p>
<p id="p-24">A</p>
<p id="p-25">"[A]s a general matter the First Amendment prohibits government officials from subjecting an individual to retaliatory actions" for engaging in protected speech. <em>Hartman v. Moore</em> , <extracted-citation case-ids="3275855" index="18" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. 250</a></span></extracted-citation>, 256, <extracted-citation case-ids="3275855" index="19" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="20" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">164 L.Ed.2d 441</a></span></extracted-citation> (2006). If an official takes adverse action against someone based on that forbidden motive, and "non-retaliatory grounds are in fact insufficient to provoke the adverse consequences," the injured person may generally seek relief by bringing a First Amendment claim. <em><extracted-citation case-ids="3275855" index="21" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Ibid.</a></span></extracted-citation></em> (citing <em>Crawford-El v. Britton</em> , <extracted-citation case-ids="11503978" index="22" url="https://cite.case.law/us/523/574/#p593"><span class="citation" data-id="9433625"><a href="/opinion/118203/crawford-el-v-britton/" aria-description="Citation for case: Crawford-El v. Britton">523 U.S. 574</a></span></extracted-citation>, 593, <extracted-citation case-ids="11503978" index="23" url="https://cite.case.law/us/523/574/#p593"><span class="citation" data-id="9433625"><a href="/opinion/118203/crawford-el-v-britton/" aria-description="Citation for case: Crawford-El v. Britton">118 S.Ct. 1584</a></span></extracted-citation>, <extracted-citation case-ids="11503978" index="24" url="https://cite.case.law/us/523/574/#p593"><span class="citation" data-id="9433625"><a href="/opinion/118203/crawford-el-v-britton/" aria-description="Citation for case: Crawford-El v. Britton">140 L.Ed.2d 759</a></span></extracted-citation> (1998) ; <em>Mt. Healthy City Bd. of Ed. v. Doyle</em> , <extracted-citation case-ids="8150" index="25" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">429 U.S. 274</a></span></extracted-citation>, 283-284, <extracted-citation case-ids="8150" index="26" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">97 S.Ct. 568</a></span></extracted-citation>, <extracted-citation case-ids="8150" index="27" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">50 L.Ed.2d 471</a></span></extracted-citation> (1977) ).</p>
<p id="p-26">To prevail on such a claim, a plaintiff must establish a "causal connection" between the government defendant's "retaliatory animus" and the plaintiff's "subsequent injury." <em>Hartman</em> , <extracted-citation case-ids="3275855" index="28" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. at 259</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="29" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>. It is not enough to show that an official acted with a retaliatory motive and that the plaintiff was injured-the motive must <em>cause</em> the injury. Specifically, it must be a "but-for" cause, meaning that the adverse action against the plaintiff would not have been taken absent the retaliatory motive. <em><extracted-citation case-ids="3275855" index="30" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="3275855" index="30" url="https://cite.case.law/us/547/250/#p256"> at 260</extracted-citation>, <extracted-citation case-ids="3275855" index="31" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation> (recognizing that although it "may be dishonorable to act with an unconstitutional motive," an official's "action colored by some degree of bad motive does not amount to a constitutional tort if that action would have been taken anyway").</p>
<p id="p-27">For example, in <em>Mt. Healthy</em> , a teacher claimed that a school district refused to rehire him in retaliation for his protected speech. We held that even if the teacher's "protected conduct played a part, substantial or otherwise, in [the] decision not to rehire," he was not entitled to reinstatement "if the same decision would have been reached" absent his protected speech. <extracted-citation case-ids="8150" index="32" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">429 U.S. at 285</a></span></extracted-citation>, <extracted-citation case-ids="8150" index="33" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">97 S.Ct. 568</a></span></extracted-citation>. Regardless of the motives of the school district, we concluded that the First Amendment "principle at stake is sufficiently vindicated if such an employee is placed in no worse a position than if he had not engaged in the [protected speech]." <em><extracted-citation case-ids="8150" index="34" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="8150" index="34" url="https://cite.case.law/us/429/274/#p283"> at 285-286</extracted-citation>, <extracted-citation case-ids="8150" index="35" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">97 S.Ct. 568</a></span></extracted-citation>.</p>
<p id="p-28">For a number of retaliation claims, establishing the causal connection between a defendant's animus and a plaintiff's injury is straightforward. Indeed, some of our cases in the public employment context "have simply taken the evidence of the motive and the discharge as sufficient for a circumstantial demonstration that the one caused the other," shifting the burden to the defendant to show he would have taken the challenged action even without the impermissible motive. <em>Hartman</em> , <extracted-citation case-ids="3275855" index="36" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. at 260</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="37" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation> (citing <em>Mt. Healthy</em> , <extracted-citation case-ids="8150" index="38" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">429 U.S. at 287</a></span></extracted-citation>, <extracted-citation case-ids="8150" index="39" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">97 S.Ct. 568</a></span></extracted-citation> ;</p>
<p id="p-29"><a class="page-label" data-citation-index="1" data-label="1723" href="#p1723" id="p1723">*1723</a><em>Arlington Heights v. Metropolitan Housing Development Corp.</em> , <extracted-citation case-ids="6951" index="40" url="https://cite.case.law/us/429/252/#p270"><span class="citation" data-id="9426633"><a href="/opinion/109573/village-of-arlington-heights-v-metropolitan-housing-development-corp/" aria-description="Citation for case: Village of Arlington Heights v. Metropolitan Housing...">429 U.S. 252</a></span></extracted-citation>, 270, n. 21, <extracted-citation case-ids="6951" index="41" url="https://cite.case.law/us/429/252/#p270"><span class="citation" data-id="9426633"><a href="/opinion/109573/village-of-arlington-heights-v-metropolitan-housing-development-corp/" aria-description="Citation for case: Village of Arlington Heights v. Metropolitan Housing...">97 S.Ct. 555</a></span></extracted-citation>, <extracted-citation case-ids="6951" index="42" url="https://cite.case.law/us/429/252/#p270"><span class="citation" data-id="9426633"><a href="/opinion/109573/village-of-arlington-heights-v-metropolitan-housing-development-corp/" aria-description="Citation for case: Village of Arlington Heights v. Metropolitan Housing...">50 L.Ed.2d 450</a></span></extracted-citation> (1977) ). But the consideration of causation is not so straightforward in other types of retaliation cases.</p>
<p id="p-30">In <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> , for example, we addressed retaliatory prosecution cases, where "proving the link between the defendant's retaliatory animus and the plaintiff's injury ... 'is usually more complex than it is in other retaliation cases.' " <em>Lozman</em> , 585 U.S., at ----, <extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="43" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct., at 1952</a></span>-1953</extracted-citation> (quoting <em>Hartman</em> , <extracted-citation case-ids="3275855" index="44" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. at 261</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="45" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation> ). Unlike most retaliation cases, in retaliatory prosecution cases the official with the malicious motive does not carry out the retaliatory action himself-the decision to bring charges is instead made by a prosecutor, who is generally immune from suit and whose decisions receive a presumption of regularity. <em>Lozman</em> , 585 U.S., at ---- - ----, <extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="46" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct., at 1952</a></span>-1953</extracted-citation><em>.</em> Thus, even when an officer's animus is clear, it does not necessarily show that the officer "induced the action of a prosecutor who would not have pressed charges otherwise." <em>Hartman</em> , <extracted-citation case-ids="3275855" index="47" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. at 263</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="48" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>.</p>
<p id="p-31">To account for this "problem of causation" in retaliatory prosecution claims, <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> adopted the requirement that plaintiffs plead and prove the absence of probable cause for the underlying criminal charge. <em><extracted-citation case-ids="3275855" index="49" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Ibid.</a></span></extracted-citation></em> ; see <em><extracted-citation case-ids="3275855" index="50" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">id.,</a></span></extracted-citation></em><extracted-citation case-ids="3275855" index="50" url="https://cite.case.law/us/547/250/#p256"> at 265-266</extracted-citation>, <extracted-citation case-ids="3275855" index="51" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>. As <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> explained, that showing provides a "distinct body of highly valuable circumstantial evidence" that is "apt to prove or disprove" whether retaliatory animus actually caused the injury: "Demonstrating that there was no probable cause for the underlying criminal charge will tend to reinforce the retaliation evidence and show that retaliation was the but-for basis for instigating the prosecution, while establishing the existence of probable cause will suggest that prosecution would have occurred even without a retaliatory motive." <em><extracted-citation case-ids="3275855" index="52" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="3275855" index="52" url="https://cite.case.law/us/547/250/#p256"> at 261</extracted-citation>, <extracted-citation case-ids="3275855" index="53" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>. Requiring plaintiffs to plead and prove the absence of probable cause made sense, we reasoned, because the existence of probable cause will be at issue in "practically all" retaliatory prosecution cases, has "high probative force," and thus "can be made mandatory with little or no added cost." <em><extracted-citation case-ids="3275855" index="54" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="3275855" index="54" url="https://cite.case.law/us/547/250/#p256"> at 265</extracted-citation>, <extracted-citation case-ids="3275855" index="55" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>. Moreover, imposing that burden on plaintiffs was necessary to suspend the presumption of regularity underlying the prosecutor's charging decision-a presumption we "do not lightly discard." <em><extracted-citation case-ids="3275855" index="56" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="3275855" index="56" url="https://cite.case.law/us/547/250/#p256"> at 263</extracted-citation>, <extracted-citation case-ids="3275855" index="57" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation> ; see also <em><extracted-citation case-ids="3275855" index="58" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">id.,</a></span></extracted-citation></em><extracted-citation case-ids="3275855" index="58" url="https://cite.case.law/us/547/250/#p256"> at 265</extracted-citation>, <extracted-citation case-ids="3275855" index="59" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>. Thus, <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> requires plaintiffs in retaliatory prosecution cases to show more than the subjective animus of an officer and a subsequent injury; plaintiffs must also prove as a threshold matter that the decision to press charges was objectively unreasonable because it was not supported by probable cause.</p>
<p id="p-32">B</p>
<p id="p-33">Officers Nieves and Weight argue that the same no-probable-cause requirement should apply to First Amendment retaliatory arrest claims. Their primary contention is that retaliatory arrest claims involve causal complexities akin to those we identified in <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> , and thus warrant the same requirement that plaintiffs plead and prove the absence of probable cause. Brief for Petitioners 20-30.</p>
<p id="p-34">As a general matter, we agree. As we recognized in <em><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">Reichle</a></span></em> and reaffirmed in <em>Lozman</em> , retaliatory arrest claims face some of the same challenges we identified in <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> : Like retaliatory prosecution cases, "retaliatory arrest cases also present a tenuous causal connection between the defendant's alleged animus and the plaintiff's injury." <em>Reichle</em> , <extracted-citation case-ids="12190092" index="60" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">566 U.S. at 668</a></span></extracted-citation>, <extracted-citation case-ids="12190092" index="61" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">132 S.Ct. 2088</a></span></extracted-citation>. The causal inquiry is complex <a class="page-label" data-citation-index="1" data-label="1724" href="#p1724" id="p1724">*1724</a>because protected speech is often a "wholly legitimate consideration" for officers when deciding whether to make an arrest. <em><extracted-citation case-ids="12190092" index="62" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">Ibid.</a></span></extracted-citation></em> ; <em>Lozman</em> , 585 U.S., at ----, <extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="63" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct., at 1953</a></span></extracted-citation>. Officers frequently must make "split-second judgments" when deciding whether to arrest, and the content and manner of a suspect's speech may convey vital information-for example, if he is "ready to cooperate" or rather "present[s] a continuing threat." <em><extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="64" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">Id.</a></span></extracted-citation></em> , at ----, <extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="65" url="https://cite.case.law/s-ct/138/2709/">138 S.Ct., at </extracted-citation>1953 (citing <em>District of Columbiav.Wesby</em> , 583 U.S. ----, ----, <extracted-citation case-ids="12615996" index="66" url="https://cite.case.law/s-ct/138/577/#p587"><span class="citation" data-id="4238107"><a href="/opinion/4460854/district-of-columbia-v-wesby/" aria-description="Citation for case: District of Columbia v. Wesby">138 S.Ct. 577</a></span></extracted-citation>, 587-588, <extracted-citation case-ids="12615996" index="67" url="https://cite.case.law/s-ct/138/577/#p587"><span class="citation" data-id="4238107"><a href="/opinion/4460854/district-of-columbia-v-wesby/" aria-description="Citation for case: District of Columbia v. Wesby">199 L.Ed.2d 453</a></span></extracted-citation> (2018) ("suspect's untruthful and evasive answers to police questioning could support probable cause")). Indeed, that kind of assessment happened in this case. The officers testified that they perceived Bartlett to be a threat based on a combination of the content and tone of his speech, his combative posture, and his apparent intoxication.</p>
<p id="p-35">In addition, "[l]ike retaliatory prosecution cases, evidence of the presence or absence of probable cause for the arrest will be available in virtually every retaliatory arrest case." <em>Reichle,</em> <extracted-citation case-ids="12190092" index="68" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">566 U.S. at 668</a></span></extracted-citation>, <extracted-citation case-ids="12190092" index="69" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">132 S.Ct. 2088</a></span></extracted-citation>. And because probable cause speaks to the objective reasonableness of an arrest, see <em>Ashcroft v. al-Kidd</em> , <extracted-citation case-ids="5924024,12459540" index="70" url="https://cite.case.law/us/563/731/"><span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/" aria-description="Citation for case: Ashcroft v. al-Kidd">563 U.S. 731</a></span></extracted-citation>, 736, <extracted-citation case-ids="5924024,12459540" index="71" url="https://cite.case.law/us/563/731/"><span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/" aria-description="Citation for case: Ashcroft v. al-Kidd">131 S.Ct. 2074</a></span></extracted-citation>, <extracted-citation case-ids="5924024,12459540" index="72" url="https://cite.case.law/us/563/731/"><span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/" aria-description="Citation for case: Ashcroft v. al-Kidd">179 L.Ed.2d 1149</a></span></extracted-citation> (2011), its absence will-as in retaliatory prosecution cases-generally provide weighty evidence that the officer's animus caused the arrest, whereas the presence of probable cause will suggest the opposite.</p>
<p id="p-36">To be sure, <em><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">Reichle</a></span></em> and <em>Lozman</em> also recognized that the two claims give rise to complex causal inquiries for somewhat different reasons. Unlike retaliatory prosecution cases, retaliatory arrest cases do not implicate the presumption of prosecutorial regularity or necessarily involve multiple government actors (although this case did). <em>Reichle</em> , <extracted-citation case-ids="12190092" index="73" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">566 U.S. at 668</a></span>-669</extracted-citation>, <extracted-citation case-ids="12190092" index="74" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">132 S.Ct. 2088</a></span></extracted-citation> ; <em>Lozman</em> , 585 U.S., at ----, 138 S.Ct., at 1953-1954. But regardless of the source of the causal complexity, the ultimate problem remains the same. For both claims, it is particularly difficult to determine whether the adverse government action was caused by the officer's malice or the plaintiff's potentially criminal conduct. See <em>id.</em> , at ----, 138 S.Ct., at 1953 (referring to "the complexity of proving (or disproving) causation" in retaliatory arrest cases). Because of the "close relationship" between the two claims, <em>Reichle</em> , <extracted-citation case-ids="12190092" index="75" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">566 U.S. at 667</a></span></extracted-citation>, <extracted-citation case-ids="12190092" index="76" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">132 S.Ct. 2088</a></span></extracted-citation>, their related causal challenge should lead to the same solution: The plaintiff pressing a retaliatory arrest claim must plead and prove the absence of probable cause for the arrest.</p>
<p id="p-37">Bartlett, in defending the decision below, argues that the "causation in retaliatory-arrest cases is not inherently complex" because the "factfinder simply must determine whether the officer intended to punish the plaintiff for the plaintiff's protected speech." Brief for Respondent 36-37; see also <em>post</em> , at 1737 - 1738 (SOTOMAYOR, J., dissenting). That approach fails to account for the fact that protected speech is often a legitimate consideration when deciding whether to make an arrest, and disregards the resulting causal complexity previously recognized by this Court. See <em>Reichle</em> , <extracted-citation case-ids="12190092" index="77" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">566 U.S. at 668</a></span></extracted-citation>, <extracted-citation case-ids="12190092" index="78" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">132 S.Ct. 2088</a></span></extracted-citation> ; <em>Lozman</em> , 585 U.S., at ----, 138 S.Ct., at 1953.</p>
<p id="p-38">Bartlett's approach dismisses the need for any threshold showing, moving directly to consideration of the subjective intent of the officers. In the Fourth Amendment context, however, "we have almost uniformly rejected invitations to probe subjective intent." <em>al-Kidd</em> , <extracted-citation case-ids="5924024,12459540" index="79" url="https://cite.case.law/us/563/731/"><span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/" aria-description="Citation for case: Ashcroft v. al-Kidd">563 U.S. at 737</a></span></extracted-citation>, <extracted-citation case-ids="5924024,12459540" index="80" url="https://cite.case.law/us/563/731/"><span class="citation multiple-matches"><a href="/c/S.Ct./131/2074/">131 S.Ct. 2074</a></span></extracted-citation> ; see also <em>Kentucky v. King</em> , <extracted-citation case-ids="5911971,12458997" index="81" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">563 U.S. 452</a></span></extracted-citation>, 464, <extracted-citation case-ids="5911971,12458997" index="82" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">131 S.Ct. 1849</a></span></extracted-citation>, <extracted-citation case-ids="5911971,12458997" index="83" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">179 L.Ed.2d 865</a></span></extracted-citation> (2011) ("Legal tests based <a class="page-label" data-citation-index="1" data-label="1725" href="#p1725" id="p1725">*1725</a>on reasonableness are generally objective, and this Court has long taken the view that evenhanded law enforcement is best achieved by the application of objective standards of conduct, rather than standards that depend upon the subjective state of mind of the officer." (internal quotation marks omitted)). Police officers conduct approximately 29,000 arrests every day-a dangerous task that requires making quick decisions in "circumstances that are tense, uncertain, and rapidly evolving." <em>Graham v. Connor</em> , <extracted-citation case-ids="605535" index="84" url="https://cite.case.law/us/490/386/#p397"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U.S. 386</a></span></extracted-citation>, 397, <extracted-citation case-ids="605535" index="85" url="https://cite.case.law/us/490/386/#p397"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">109 S.Ct. 1865</a></span></extracted-citation>, <extracted-citation case-ids="605535" index="86" url="https://cite.case.law/us/490/386/#p397"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">104 L.Ed.2d 443</a></span></extracted-citation> (1989). To ensure that officers may go about their work without undue apprehension of being sued, we generally review their conduct under objective standards of reasonableness. See <em>Atwater v. Lago Vista</em> , <extracted-citation case-ids="9301256" index="87" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">532 U.S. 318</a></span></extracted-citation>, 351, and n. 22, <extracted-citation case-ids="9301256" index="88" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">121 S.Ct. 1536</a></span></extracted-citation>, <extracted-citation case-ids="9301256" index="89" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">149 L.Ed.2d 549</a></span></extracted-citation> (2001) ; <em>Harlow v. Fitzgerald</em> , <extracted-citation case-ids="6194865" index="90" url="https://cite.case.law/us/457/800/#p814"><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">457 U.S. 800</a></span></extracted-citation>, 814-819, <extracted-citation case-ids="6194865" index="91" url="https://cite.case.law/us/457/800/#p814"><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">102 S.Ct. 2727</a></span></extracted-citation>, <extracted-citation case-ids="6194865" index="92" url="https://cite.case.law/us/457/800/#p814"><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">73 L.Ed.2d 396</a></span></extracted-citation> (1982). Thus, when reviewing an arrest, we ask "whether the circumstances, viewed objectively, justify [the challenged] action," and if so, conclude "that action was reasonable <em>whatever</em> the subjective intent motivating the relevant officials." <em>al-Kidd</em> , <span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/#736" aria-description="Citation for case: Ashcroft v. al-Kidd">563 U.S. at 736</a></span>, <extracted-citation case-ids="5924024,12459540" index="93" url="https://cite.case.law/us/563/731/"><span class="citation multiple-matches"><a href="/c/S.Ct./131/2074/">131 S.Ct. 2074</a></span></extracted-citation> (internal quotation marks omitted). A particular officer's state of mind is simply "irrelevant," and it provides "no basis for invalidating an arrest." <em>Devenpeck v. Alford</em> , <extracted-citation case-ids="5916678" index="94" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">543 U.S. 146</a></span></extracted-citation>, 153, 155, <extracted-citation case-ids="5916678" index="95" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">125 S.Ct. 588</a></span></extracted-citation>, <extracted-citation case-ids="5916678" index="96" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">160 L.Ed.2d 537</a></span></extracted-citation> (2004).</p>
<p id="p-39">Bartlett's purely subjective approach would undermine that precedent by allowing even doubtful retaliatory arrest suits to proceed based solely on allegations about an arresting officer's mental state. See <em>Lozman</em> , 585 U.S., at ----, 138 S.Ct., at 1953. Because a state of mind is "easy to allege and hard to disprove," <em>Crawford-El</em> , <extracted-citation case-ids="11503978" index="97" url="https://cite.case.law/us/523/574/#p593"><span class="citation" data-id="9433625"><a href="/opinion/118203/crawford-el-v-britton/" aria-description="Citation for case: Crawford-El v. Britton">523 U.S. at 585</a></span></extracted-citation>, <extracted-citation case-ids="11503978" index="98" url="https://cite.case.law/us/523/574/#p593"><span class="citation" data-id="9433625"><a href="/opinion/118203/crawford-el-v-britton/" aria-description="Citation for case: Crawford-El v. Britton">118 S.Ct. 1584</a></span></extracted-citation>, a subjective inquiry would threaten to set off "broad-ranging discovery" in which "there often is no clear end to the relevant evidence," <em>Harlow</em> , <extracted-citation case-ids="6194865" index="99" url="https://cite.case.law/us/457/800/#p814"><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">457 U.S. at 817</a></span></extracted-citation>, <extracted-citation case-ids="6194865" index="100" url="https://cite.case.law/us/457/800/#p814"><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">102 S.Ct. 2727</a></span></extracted-citation>. As a result, policing certain events like an unruly protest would pose overwhelming litigation risks. Any inartful turn of phrase or perceived slight during a legitimate arrest could land an officer in years of litigation. Bartlett's standard would thus "dampen the ardor of all but the most resolute, or the most irresponsible, in the unflinching discharge of their duties." <em>Gregoire v. Biddle</em> , <extracted-citation case-ids="1166269" index="101" url="https://cite.case.law/f2d/177/579/#p581"><span class="citation" data-id="1507366"><a href="/opinion/1507366/gregoire-v-biddle/" aria-description="Citation for case: Gregoire v. Biddle">177 F. 2d 579</a></span></extracted-citation>, 581 (C.A.2 1949) (Learned Hand, C.J.). It would also compromise evenhanded application of the law by making the constitutionality of an arrest "vary from place to place and from time to time" depending on the personal motives of individual officers. <em>Devenpeck</em> , <extracted-citation case-ids="5916678" index="102" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">543 U.S. at 154</a></span></extracted-citation>, <extracted-citation case-ids="5916678" index="103" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">125 S.Ct. 588</a></span></extracted-citation>. Yet another "predictable consequence" of such a rule is that officers would simply minimize their communication during arrests to avoid having their words scrutinized for hints of improper motive-a result that would leave everyone worse off. <em><extracted-citation case-ids="5916678" index="104" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="5916678" index="104" url="https://cite.case.law/us/543/146/#p153"> at 155</extracted-citation>, <extracted-citation case-ids="5916678" index="105" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">125 S.Ct. 588</a></span></extracted-citation>.</p>
<p id="p-40">Adopting <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> 's no-probable-cause rule in this closely related context addresses those familiar concerns. Absent such a showing, a retaliatory arrest claim fails. But if the plaintiff establishes the absence of probable cause, "then the <em><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">Mt. Healthy</a></span></em> test governs: The plaintiff must show that the retaliation was a substantial or motivating factor behind the [arrest], and, if that showing is made, the defendant can prevail only by showing that the [arrest] would have been initiated without respect to retaliation." <em>Lozman</em> , 585 U.S., at ----, 138 S.Ct., at 1952-1953 (citing <em>Hartman</em> , <extracted-citation case-ids="3275855" index="106" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. at 265</a></span>-266</extracted-citation>, <extracted-citation case-ids="3275855" index="107" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation> ).<footnotemark>1</footnotemark></p>
<p id="p-41"><a class="page-label" data-citation-index="1" data-label="1726" href="#p1726" id="p1726">*1726</a>C</p>
<p id="p-42">Our conclusion is confirmed by the common law approach to similar tort claims. When defining the contours of a claim under § 1983, we look to "common-law principles that were well settled at the time of its enactment." <em>Kalina v. Fletcher</em> , <extracted-citation case-ids="11470940" index="108" url="https://cite.case.law/us/522/118/#p123"><span class="citation" data-id="9433547"><a href="/opinion/118156/kalina-v-fletcher/" aria-description="Citation for case: Kalina v. Fletcher">522 U.S. 118</a></span></extracted-citation>, 123, <extracted-citation case-ids="11470940" index="109" url="https://cite.case.law/us/522/118/#p123"><span class="citation" data-id="9433547"><a href="/opinion/118156/kalina-v-fletcher/" aria-description="Citation for case: Kalina v. Fletcher">118 S.Ct. 502</a></span></extracted-citation>, <extracted-citation case-ids="11470940" index="110" url="https://cite.case.law/us/522/118/#p123"><span class="citation" data-id="9433547"><a href="/opinion/118156/kalina-v-fletcher/" aria-description="Citation for case: Kalina v. Fletcher">139 L.Ed.2d 471</a></span></extracted-citation> (1997) ; <em>Manuelv.Joliet</em> , 580 U.S. ----, ----, <extracted-citation case-ids="12609962" index="111" url="https://cite.case.law/s-ct/137/911/#p1920"><span class="citation" data-id="9873459"><a href="/opinion/4376986/manuel-v-city-of-joliet/" aria-description="Citation for case: Manuel v. City of Joliet">137 S.Ct. 911</a></span></extracted-citation>, 1920-1921, <extracted-citation case-ids="12609962" index="112" url="https://cite.case.law/s-ct/137/911/#p1920"><span class="citation" data-id="9873459"><a href="/opinion/4376986/manuel-v-city-of-joliet/" aria-description="Citation for case: Manuel v. City of Joliet">197 L.Ed.2d 312</a></span></extracted-citation> (2017) (common law principles "guide" the definition of claims under § 1983 ).</p>
<p id="p-43">As the parties acknowledge, when § 1983 was enacted in 1871, there was no common law tort for retaliatory arrest based on protected speech. See Brief for Petitioners 43; Brief for Respondent 20. We therefore turn to the common law torts that provide the "closest analogy" to retaliatory arrest claims. <em>Heck v. Humphrey</em> , <extracted-citation case-ids="39868" index="113" url="https://cite.case.law/us/512/477/#p484"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. 477</a></span></extracted-citation>, 484, <extracted-citation case-ids="39868" index="114" url="https://cite.case.law/us/512/477/#p484"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>, <extracted-citation case-ids="39868" index="115" url="https://cite.case.law/us/512/477/#p484"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">129 L.Ed.2d 383</a></span></extracted-citation> (1994). The parties dispute whether the better analog is false imprisonment or malicious prosecution. At common law, false imprisonment arose from a "detention without legal process," whereas malicious prosecution was marked "by <em>wrongful institution</em> of legal process." <em>Wallace v. Kato</em> , <extracted-citation case-ids="3553763" index="116" url="https://cite.case.law/us/549/384/#p389"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. 384</a></span></extracted-citation>, 389-390, <extracted-citation case-ids="3553763" index="117" url="https://cite.case.law/us/549/384/#p389"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>, <extracted-citation case-ids="3553763" index="118" url="https://cite.case.law/us/549/384/#p389"><span class="citation no-link">166 L.Ed.2d 973</span></extracted-citation> (2007).<footnotemark>2</footnotemark> Here, both claims suggest the same result: The presence of probable cause should generally defeat a First Amendment retaliatory arrest claim. See generally <em>Lozman</em> , 585 U.S., at ---- - ----, 138 S.Ct., at 1950-1951 (THOMAS, J., dissenting).</p>
<p id="p-44">Malicious prosecution required the plaintiff to show that the criminal charge against him "was unfounded, and that it was made without reasonable or probable cause, and that the defendant in making or instigating it was actuated by malice." <em>Wheeler v. Nesbitt</em> , <extracted-citation case-ids="3463673" index="119" url="https://cite.case.law/us/65/544/"><span class="citation" data-id="87431"><a href="/opinion/87431/wheeler-v-nesbitt/" aria-description="Citation for case: Wheeler v. Nesbitt">65 U.S. 544</a></span></extracted-citation>, <extracted-citation case-ids="3463673" index="120" url="https://cite.case.law/us/65/544/"><span class="citation" data-id="87431"><a href="/opinion/87431/wheeler-v-nesbitt/" aria-description="Citation for case: Wheeler v. Nesbitt">24 How. 544</a></span></extracted-citation>, 549-550, <extracted-citation case-ids="3463673" index="121" url="https://cite.case.law/us/65/544/"><span class="citation" data-id="87431"><a href="/opinion/87431/wheeler-v-nesbitt/" aria-description="Citation for case: Wheeler v. Nesbitt">16 L.Ed. 765</a></span></extracted-citation> (1861) ; see also Restatement of Torts § 653 (1938). It has long been "settled law" that malicious prosecution requires proving "the want of probable cause," and Bartlett does not argue otherwise. <em>Brown v. Selfridge</em> , <extracted-citation case-ids="3668822" index="122" url="https://cite.case.law/us/224/189/#p191"><span class="citation" data-id="97600"><a href="/opinion/97600/brown-v-selfridge/" aria-description="Citation for case: Brown v. Selfridge">224 U.S. 189</a></span></extracted-citation>, 191, <extracted-citation case-ids="3668822" index="123" url="https://cite.case.law/us/224/189/#p191"><span class="citation" data-id="97600"><a href="/opinion/97600/brown-v-selfridge/" aria-description="Citation for case: Brown v. Selfridge">32 S.Ct. 444</a></span></extracted-citation>, <extracted-citation case-ids="3668822" index="124" url="https://cite.case.law/us/224/189/#p191"><span class="citation" data-id="97600"><a href="/opinion/97600/brown-v-selfridge/" aria-description="Citation for case: Brown v. Selfridge">56 L.Ed. 727</a></span></extracted-citation> (1912) ; see also <em>Wheeler</em> , <extracted-citation case-ids="3463673" index="125" url="https://cite.case.law/us/65/544/"><span class="citation" data-id="87431"><a href="/opinion/87431/wheeler-v-nesbitt/#550" aria-description="Citation for case: Wheeler v. Nesbitt">24 How. at 550</a></span></extracted-citation> (noting that "[w]ant of reasonable and probable cause" is an "element in the action for a malicious criminal prosecution").</p>
<p id="p-45">For claims of false imprisonment, the presence of probable cause was generally a complete defense for peace officers. See T. Cooley, Law of Torts 175 (1880); 1 F. Hilliard, The Law of Torts or Private Wrongs 207-208, and n. (a) (1859). In such cases, arresting officers were protected from liability if the arrest was "privileged." At common law, peace officers were privileged to make warrantless arrests based on probable cause of the commission of a felony or certain misdemeanors. See Restatement of Torts §§ 118, 119, 121 (1934) ; see also Cooley, Law of Torts, at 175-176 (stating that peace officers who make arrests <a class="page-label" data-citation-index="1" data-label="1727" href="#p1727" id="p1727">*1727</a>based on probable cause "will be excused, even though it appear afterwards that in fact no felony had been committed"); see generally <em>Atwater</em> , <extracted-citation case-ids="9301256" index="126" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">532 U.S. at 340</a></span>-345</extracted-citation>, <extracted-citation case-ids="9301256" index="127" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">121 S.Ct. 1536</a></span></extracted-citation> (reviewing the history of warrantless arrests for misdemeanors). Although the exact scope of the privilege varied somewhat depending on the jurisdiction, the consistent rule was that officers were not liable for arrests they were privileged to make based on probable cause.</p>
<p id="p-46">D</p>
<p id="p-47">Although probable cause should generally defeat a retaliatory arrest claim, a narrow qualification is warranted for circumstances where officers have probable cause to make arrests, but typically exercise their discretion not to do so. In such cases, an unyielding requirement to show the absence of probable cause could pose "a risk that some police officers may exploit the arrest power as a means of suppressing speech." <em>Lozman</em> , 585 U.S., at ----, 138 S.Ct., at 1953-1954.</p>
<p id="p-48">When § 1983 was adopted, officers were generally privileged to make warrantless arrests for misdemeanors only in limited circumstances. See Restatement of Torts § 121, Comments <em>e</em> , <em>h</em> , at 262-263. Today, however, "statutes in all 50 States and the District of Columbia permit warrantless misdemeanor arrests" in a much wider range of situations-often whenever officers have probable cause for "even a very minor criminal offense." <em>Atwater</em> , <extracted-citation case-ids="9301256" index="128" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/#344" aria-description="Citation for case: Atwater v. City of Lago Vista">532 U.S. at 344-345</a></span>, 354</extracted-citation>, <extracted-citation case-ids="9301256" index="129" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">121 S.Ct. 1536</a></span></extracted-citation> ; see <em><extracted-citation case-ids="9301256" index="130" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">id.,</a></span></extracted-citation></em><extracted-citation case-ids="9301256" index="130" url="https://cite.case.law/us/532/318/#p351"> at 355-360</extracted-citation>, <extracted-citation case-ids="9301256" index="131" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">121 S.Ct. 1536</a></span></extracted-citation> (listing state statutes).</p>
<p id="p-49">For example, at many intersections, jaywalking is endemic but rarely results in arrest. If an individual who has been vocally complaining about police conduct is arrested for jaywalking at such an intersection, it would seem insufficiently protective of First Amendment rights to dismiss the individual's retaliatory arrest claim on the ground that there was undoubted probable cause for the arrest. In such a case, because probable cause does little to prove or disprove the causal connection between animus and injury, applying <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> 's rule would come at the expense of <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> 's logic.</p>
<p id="p-50">For those reasons, we conclude that the no-probable-cause requirement should not apply when a plaintiff presents objective evidence that he was arrested when otherwise similarly situated individuals not engaged in the same sort of protected speech had not been. Cf. <em>United States v. Armstrong</em> , <extracted-citation case-ids="11745202" index="132" url="https://cite.case.law/us/517/456/#p465"><span class="citation" data-id="9433285"><a href="/opinion/118022/united-states-v-armstrong/" aria-description="Citation for case: United States v. Armstrong">517 U.S. 456</a></span></extracted-citation>, 465, <extracted-citation case-ids="11745202" index="133" url="https://cite.case.law/us/517/456/#p465"><span class="citation" data-id="9433285"><a href="/opinion/118022/united-states-v-armstrong/" aria-description="Citation for case: United States v. Armstrong">116 S.Ct. 1480</a></span></extracted-citation>, <extracted-citation case-ids="11745202" index="134" url="https://cite.case.law/us/517/456/#p465"><span class="citation" data-id="9433285"><a href="/opinion/118022/united-states-v-armstrong/" aria-description="Citation for case: United States v. Armstrong">134 L.Ed.2d 687</a></span></extracted-citation> (1996). That showing addresses <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> 's causal concern by helping to establish that "non-retaliatory grounds [we]re in fact insufficient to provoke the adverse consequences." <extracted-citation case-ids="3275855" index="135" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. at 256</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="136" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>. And like a probable cause analysis, it provides an objective inquiry that avoids the significant problems that would arise from reviewing police conduct under a purely subjective standard. Because this inquiry is objective, the statements and motivations of the particular arresting officer are "irrelevant" at this stage. <em>Devenpeck</em> , <extracted-citation case-ids="5916678" index="137" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">543 U.S. at 153</a></span></extracted-citation>, <extracted-citation case-ids="5916678" index="138" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">125 S.Ct. 588</a></span></extracted-citation>. After making the required showing, the plaintiff's claim may proceed in the same manner as claims where the plaintiff has met the threshold showing of the absence of probable cause. See <em>Lozman</em> , 585 U.S., at ----, 138 S.Ct., at 1952-1953.</p>
<p id="p-51">* * *</p>
<p id="p-52">In light of the foregoing, Bartlett's retaliation claim cannot survive summary judgment. As an initial matter, the record contains insufficient evidence of retaliation on the part of Trooper Weight. The <em>only</em> evidence of retaliatory animus <a class="page-label" data-citation-index="1" data-label="1728" href="#p1728" id="p1728">*1728</a>identified by the Ninth Circuit was Bartlett's affidavit stating that Sergeant Nieves said "bet you wish you would have talked to me now." <extracted-citation index="139" url="https://cite.case.law/citations/?q=712%20Fed.%20Appx.%20613"><span class="citation" data-id="4213549"><a href="/opinion/4436296/russell-bartlett-v-luis-nieves/" aria-description="Citation for case: Russell Bartlett v. Luis Nieves">712 Fed. Appx. at 616</a></span></extracted-citation>. But that allegation about <em>Nieves</em> says nothing about what motivated <em>Weight</em> , who had no knowledge of Bartlett's prior run-in with Nieves. Cf. <em>Lozman</em> , 585 U.S., at ----, 138 S.Ct., at 1953-1954 (plaintiff "likely could not have maintained a retaliation claim against the arresting officer" when there was "no showing that the officer had any knowledge of [the plaintiff's] prior speech").</p>
<p id="p-53">In any event, Bartlett's claim against both officers cannot succeed because they had probable cause to arrest him. As the Court of Appeals explained:</p>
<blockquote id="p-54">"When Sergeant Nieves initiated Bartlett's arrest, he knew that Bartlett had been drinking, and he observed Bartlett speaking in a loud voice and standing close to Trooper Weight. He also saw Trooper Weight push Bartlett back.... [T]he test is whether the information the officer had at the time of making the arrest gave rise to probable cause. We agree with the district court that it did; a reasonable officer in Sergeant Nieves's position could have concluded that Bartlett stood close to Trooper Weight and spoke loudly in order to challenge him, provoking Trooper Weight to push him back." <extracted-citation index="140" url="https://cite.case.law/citations/?q=712%20Fed.%20Appx.%20613"><span class="citation" data-id="4213549"><a href="/opinion/4436296/russell-bartlett-v-luis-nieves/#615" aria-description="Citation for case: Russell Bartlett v. Luis Nieves">712 Fed. Appx. at 615</a></span></extracted-citation> (citations and internal quotation marks omitted).</blockquote>
<p id="p-55">Because there was probable cause to arrest Bartlett, his retaliatory arrest claim fails as a matter of law. Accordingly, the judgment of the United States Court of Appeals for the Ninth Circuit is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="p-56">It is so ordered.</p>
<p id="p-57">Justice THOMAS, concurring in part and concurring in the judgment.</p>
<p id="p-58">When <extracted-citation index="141" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation> was enacted, "the common law recognized probable cause as an important element for ensuring that arrest-based torts did not unduly interfere with the objectives of law enforcement." <em>Lozman v.Riviera Beach</em> , 585 U.S. ----, ----, <extracted-citation case-ids="12612344" index="142" url="https://cite.case.law/s-ct/138/1945/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct. 1945</a></span></extracted-citation>, 1958, <extracted-citation case-ids="12612344" index="143" url="https://cite.case.law/s-ct/138/1945/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">201 L.Ed.2d 342</a></span></extracted-citation> (2018) (THOMAS, J., dissenting). Applying that principle resolves this case: "[P]laintiffs bringing a First Amendment retaliatory-arrest claim under § 1983 should have to plead and prove a lack of probable cause." <em><extracted-citation case-ids="12612344" index="144" url="https://cite.case.law/s-ct/138/1945/">Ibid.</extracted-citation></em> The Court acknowledges as much, <em>ante,</em> at 1726 - 1727, and I join the portions of the Court's opinion adopting that rule.<footnotemark>1</footnotemark> I do not join Part II-D, however, because I do not agree that "a narrow qualification is warranted for circumstances where officers have probable cause to make arrests, but typically exercise their discretion not to do so." <em>Ante,</em> at 1727. That qualification has no basis in either the common law or our First Amendment precedents.</p>
<p id="p-59">As the Court explains, "[w]hen defining the contours of a claim under § 1983, we look to 'common-law principles that were well settled at the time of its enactment.' " <em>Ante,</em> at 1726. Because no common-law tort for retaliatory arrest in violation of the freedom of speech existed when § 1983 was enacted, we "look to the common-law torts that 'provid[e] the closest analogy' to this claim." <em>Lozman</em> , 585 U.S., at ----, 138 S.Ct., at 1957 (opinion of THOMAS, J.). Here, those torts are false imprisonment, <a class="page-label" data-citation-index="1" data-label="1729" href="#p1729" id="p1729">*1729</a>malicious arrest, and malicious prosecution. <em>Ibid.</em></p>
<p id="p-60">The existence of probable cause generally excused an officer from liability for these three torts, without regard to the treatment of similarly situated individuals. For instance, a constable who made an arrest "on reasonable grounds of belief" that a felony had been committed was "excused" from liability for false imprisonment. T. Cooley, Law of Torts 175 (1879) (Cooley); <em>Lozman</em> , <em>supra,</em> at 1721 - 1722, 138 S.Ct., at 1957-1958 (opinion of THOMAS, J.). And the absence of probable cause was central to both malicious arrest and malicious prosecution. Cooley 180-181; <em>Lozman</em> , <em>supra,</em> at 1722 - 1723, 138 S.Ct., at 1957-1958 (opinion of THOMAS, J.). As the Court puts it, "the consistent rule was that officers were not liable for arrests they were privileged to make based on probable cause." <em>Ante,</em> at 1727.</p>
<p id="p-61">Rather than adhere to this rule, the majority carves out an exception to the no-probable-cause requirement for plaintiffs who "presen[t] objective evidence" that they were "arrested when otherwise similarly situated individuals not engaged in the same sort of protected speech had not been." <em>Ante,</em> at 1727. The common law provides no support for this exception. Indeed, the majority cites not a single common-law case that supports imposing liability based on an officer's treatment of similarly situated individuals. The majority instead suggests that its exception responds to the fact that States today " 'permit warrantless misdemeanor arrests' " for many " 'minor criminal offense[s],' " whereas "[w]hen § 1983 was adopted, officers were generally privileged to make warrantless arrests for misdemeanors only in limited circumstances." <em>Ibid</em> . But discomfort with the number of warrantless arrests that are privileged today is an issue for state legislatures, not a license for this Court to fashion an exception to a previously "consistent rule." <em>Ante,</em> at 1726 - 1727.</p>
<p id="p-62">The majority's exception is also untethered from our First Amendment precedents. In <em>Hartman v. Moore</em> , <extracted-citation case-ids="3275855" index="145" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. 250</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="146" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="147" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">164 L.Ed.2d 441</a></span></extracted-citation> (2006), we expressly declined to create <em>any</em> exceptions to the rule that a plaintiff alleging retaliatory prosecution in violation of the First Amendment must plead and prove the absence of probable cause. See <em><extracted-citation case-ids="3275855" index="148" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">id.</a></span></extracted-citation></em> , at 264-266, and n. 10, <extracted-citation case-ids="3275855" index="149" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>. The majority today imports its "qualification" from our jurisprudence on selective-prosecution claims. <em>Ante</em> , at 1727 - 1728, 1729 - 1730 (citing <em>United States v. Armstrong</em> , <extracted-citation case-ids="11745202" index="150" url="https://cite.case.law/us/517/456/#p465"><span class="citation" data-id="9433285"><a href="/opinion/118022/united-states-v-armstrong/" aria-description="Citation for case: United States v. Armstrong">517 U.S. 456</a></span></extracted-citation>, 465, <extracted-citation case-ids="11745202" index="151" url="https://cite.case.law/us/517/456/#p465"><span class="citation" data-id="9433285"><a href="/opinion/118022/united-states-v-armstrong/" aria-description="Citation for case: United States v. Armstrong">116 S.Ct. 1480</a></span></extracted-citation>, <extracted-citation case-ids="11745202" index="152" url="https://cite.case.law/us/517/456/#p465"><span class="citation" data-id="9433285"><a href="/opinion/118022/united-states-v-armstrong/" aria-description="Citation for case: United States v. Armstrong">134 L.Ed.2d 687</a></span></extracted-citation> (1996) ). But "[t]he requirements for a selective-prosecution claim draw on 'ordinary equal protection standards,' " not the First Amendment. <em><extracted-citation case-ids="11745202" index="153" url="https://cite.case.law/us/517/456/#p465"><span class="citation" data-id="9433285"><a href="/opinion/118022/united-states-v-armstrong/" aria-description="Citation for case: United States v. Armstrong">Id.</a></span></extracted-citation></em> , at 465, <extracted-citation case-ids="11745202" index="154" url="https://cite.case.law/us/517/456/#p465"><span class="citation" data-id="9433285"><a href="/opinion/118022/united-states-v-armstrong/" aria-description="Citation for case: United States v. Armstrong">116 S.Ct. 1480</a></span></extracted-citation>. That jurisprudence therefore is not relevant here. Cf. <em>Whren v. United States</em> , <extracted-citation case-ids="11746960" index="155" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U.S. 806</a></span></extracted-citation>, 813, <extracted-citation case-ids="11746960" index="156" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S.Ct. 1769</a></span></extracted-citation>, <extracted-citation case-ids="11746960" index="157" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L.Ed.2d 89</a></span></extracted-citation> (1996) ("[T]he constitutional basis for objecting to intentionally discriminatory application of laws is the Equal Protection Clause ... ").</p>
<p id="p-63">With no guidance from the common law or relevant precedents, the majority crafts its exception as a matter of policy. But this "narrow" qualification threatens to derail our retaliation jurisprudence in several ways. For one, although the majority's stated concern is with " 'warrantless misdemeanor arrests' " for " 'very minor' " offenses like "jaywalking," <em>ante,</em> at 1727 - 1728, its exception apparently applies to <em>all</em> offenses, including serious felonies. This overbroad exception thus is likely to encourage protracted litigation about which individuals are "similarly situated," <em><extracted-citation case-ids="11746960" index="158" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">ibid.</a></span></extracted-citation></em> , while doing little to vindicate First Amendment rights. Moreover, the majority's rule risks chilling law enforcement officers from making arrests for fear of <a class="page-label" data-citation-index="1" data-label="1730" href="#p1730" id="p1730">*1730</a>liability, thus flouting the reasoning behind the emphasis on probable cause in arrest-based torts at common law. <em>Lozman</em> , <em>supra,</em> at 1721 - 1722, 138 S.Ct., at 1957-1958 (opinion of THOMAS, J.). In short, the majority's exception lacks the support of history, precedent, and sound policy.</p>
<p id="p-64">* * *</p>
<p id="p-65">The requirement that plaintiffs bringing First Amendment retaliatory-arrest claims plead and prove the absence of probable cause is supported by the common law and our First Amendment precedents. The majority's new exception has no basis in either. Accordingly, I join all but Part II-D of the majority opinion.</p>
<footnote label="1">
<p id="p-130">Justice SOTOMAYOR would have us extend <em><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">Mt. Healthy</a></span></em> and rely on that "tried and true" approach as the exclusive standard in the retaliatory arrest context. See <em>post</em> , at 1735 - 1737, 1742 (dissenting opinion). But not even respondent Bartlett argues for such a rule. And since our decisions in <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> and <em><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">Reichle</a></span></em> , no court of appeals has applied that approach in retaliatory arrest cases of this sort. Justice SOTOMAYOR criticizes the Court for spending "[m]uch of its opinion ... analogizing to <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> ," <em>post,</em> at 1736 - 1737, but of course <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> is our precedent most directly on point. To the extent retaliatory arrest cases raise concerns distinct from that precedent, we have departed from <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> to afford greater First Amendment protection. See <em>infra</em> , at 1741 - 1742.</p>
</footnote>
<footnote label="2">
<p id="p-131">For our purposes, we need not distinguish between the torts of false imprisonment and false arrest, which are "virtually synonymous." 35 C.J. S., False Imprisonment § 2, p. 522 (2009) ; see also <em>Wallace</em> , <extracted-citation case-ids="3553763" index="159" url="https://cite.case.law/us/549/384/#p389"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. at 388</a></span>-389</extracted-citation>, <extracted-citation case-ids="3553763" index="160" url="https://cite.case.law/us/549/384/#p389"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>.</p>
</footnote>
<footnote label="1">
<p id="p-133">The majority implies that the Ninth Circuit does not apply <em><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">Mt. Healthy</a></span></em> . <em>Ante,</em> at 1725, n. 1 ("since ... <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> and <em><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">Reichle</a></span></em> , no court of appeals has applied [the <em><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">Mt. Healthy</a></span></em> ] approach"). That is not readily apparent. Because <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> 's no-probable-cause requirement does not apply to retaliatory police action in the Ninth Circuit, such claims are handled as " 'ordinary' retaliation claim[s]," <em>Skoog v. County of Clackamas</em> , <extracted-citation case-ids="3757279" index="161" url="https://cite.case.law/f3d/469/1221/#p1234"><span class="citation" data-id="3039576"><a href="/opinion/3039576/skoog-v-county-of-clackamas/" aria-description="Citation for case: Skoog v. County of Clackamas">469 F. 3d 1221</a></span></extracted-citation>, 1234 (2006), which in the Ninth Circuit (as elsewhere) means that retaliatory motive must be the "but-for cause of the defendant's action," <em><extracted-citation case-ids="3757279" index="162" url="https://cite.case.law/f3d/469/1221/#p1234"><span class="citation" data-id="3039576"><a href="/opinion/3039576/skoog-v-county-of-clackamas/" aria-description="Citation for case: Skoog v. County of Clackamas">id.,</a></span></extracted-citation></em><extracted-citation case-ids="3757279" index="162" url="https://cite.case.law/f3d/469/1221/#p1234"> at 1232</extracted-citation>. That but-for causation requirement for retaliation claims derives from <em><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">Mt. Healthy</a></span></em> . See <em>Hartman v. Moore</em> , <extracted-citation case-ids="3275855" index="163" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. 250</a></span></extracted-citation>, 260, <extracted-citation case-ids="3275855" index="164" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="165" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">164 L.Ed.2d 441</a></span></extracted-citation> (2006) ; <em>Crawford-El v. Britton</em> , <extracted-citation case-ids="11503978" index="166" url="https://cite.case.law/us/523/574/#p593"><span class="citation" data-id="9433625"><a href="/opinion/118203/crawford-el-v-britton/" aria-description="Citation for case: Crawford-El v. Britton">523 U.S. 574</a></span></extracted-citation>, 593, <extracted-citation case-ids="11503978" index="167" url="https://cite.case.law/us/523/574/#p593"><span class="citation" data-id="9433625"><a href="/opinion/118203/crawford-el-v-britton/" aria-description="Citation for case: Crawford-El v. Britton">118 S.Ct. 1584</a></span></extracted-citation>, <extracted-citation case-ids="11503978" index="168" url="https://cite.case.law/us/523/574/#p593"><span class="citation" data-id="9433625"><a href="/opinion/118203/crawford-el-v-britton/" aria-description="Citation for case: Crawford-El v. Britton">140 L.Ed.2d 759</a></span></extracted-citation> (1998) ; see also <em>Lacey v. Maricopa County</em> , <extracted-citation case-ids="3518590" index="169" url="https://cite.case.law/f3d/693/896/#p916"><span class="citation" data-id="9501261"><a href="/opinion/807646/michael-lacey-v-joseph-arpaio/" aria-description="Citation for case: Michael Lacey v. Joseph Arpaio">693 F. 3d 896</a></span></extracted-citation>, 916-917 (C.A.9 2012) (en banc) (retaliatory arrest plaintiff must show that deterrence of speech "was a substantial or motivating factor" and also "ultimately" be able to show " 'but-for causation' " (quoting <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> 's discussion of <em><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">Mt. Healthy</a></span></em> )).</p>
<p id="p-134">In any event, the majority's criticism is a red herring. There is nothing novel about applying <em><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">Mt. Healthy</a></span></em> in the retaliatory arrest context. <em>E.g.,</em> <em>Lozmanv.Riviera Beach</em> , 585 U.S. ----, ---- - ----, <extracted-citation case-ids="12612344" index="170" url="https://cite.case.law/s-ct/138/1945/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct. 1945</a></span></extracted-citation>, 1954-1955, <extracted-citation case-ids="12612344" index="171" url="https://cite.case.law/s-ct/138/1945/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">201 L.Ed.2d 342</a></span></extracted-citation> (2018). The same cannot be said of the test concocted by the majority.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Nix v. Williams.md  (`case`, 5 assertions)

### content_page

```
---
title: "Nix v. Williams"
type: case
citation: "467 U.S. 431 (1984)"
parallel_cite: "104 S. Ct. 2501; 81 L. Ed. 2d 377; 52 U.S.L.W. 4732"
neutral_cite: 1984 U.S. LEXIS 101
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-06-11
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-06-11
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Nix v. Williams
  varies_by_point: false
  scope_note: "Establishes the inevitable-discovery exception to the exclusionary rule; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111204/nix-v-williams/"
  cluster_id: 111204
  opinion_id: 9429647
  identity_checked: true
homes:
  - page: "[[Inevitable Discovery & Independent Source]]"
    role: "Key — Progeny / Refinement"
related: ["[[Murray v. United States]]", "[[Brewer v. Williams]]", "[[Segura v. United States]]", "[[Wong Sun v. United States]]"]
aliases: []
tags: ["case", "exclusionary-rule", "inevitable-discovery", "fruit-of-the-poisonous-tree"]
holding: "Inevitable discovery: unlawfully obtained evidence is admissible if the prosecution proves by a preponderance it would inevitably have…"
lake:
  record_id: Nix v. Williams
  status: verified
  projected_at: 2026-07-06
---

# Nix v. Williams

*467 U.S. 431 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After his arrest for the murder of a 10-year-old girl, Williams was subjected to the "Christian burial speech" that led him to direct police to the body — interrogation later held to have violated his right to counsel (*[[Brewer v. Williams]]*). At the same time, a large organized volunteer search party was systematically searching the area and was within a few miles of the body. At Williams's retrial, the body-related evidence was admitted on an inevitable-discovery theory.

## Issue
Whether evidence obtained as the fruit of a constitutional violation is nevertheless admissible if it would inevitably have been discovered by lawful means.

## Rule
Yes. "If the prosecution can establish by a preponderance of the evidence that the information ultimately or inevitably would have been discovered by lawful means . . . then the deterrence rationale has so little basis that the evidence should be received." — 467 U.S. at 444. ^pin-444

The prosecution need not also prove the absence of police bad faith.

## Application
The volunteer search party was conducting an organized, systematic search and, in the normal course, would have discovered the body in essentially the same condition; the State proved by a preponderance that the body and related evidence would inevitably have been found by lawful means. The evidence was therefore admissible despite the antecedent right-to-counsel violation.

## Conclusion
The body-related evidence was admissible under the inevitable-discovery doctrine; the grant of [[Common Legal Terms#habeas-corpus|habeas]] relief was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Nix* establishes [[Inevitable Discovery and Independent Source|inevitable discovery]] as a sibling of the independent-source doctrine ([[Murray v. United States]]), both grounded in restoring the police to the position they would have occupied absent the illegality.

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *Nix v. Williams*, 467 U.S. 431 (1984) — https://www.courtlistener.com/opinion/111204/nix-v-williams/ — pinpoint: 444.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "286b5310ae1d15b6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "467 U.S. 431 (1984)", "court": "U.S. Supreme Court", "neutral_cite": "1984 U.S. LEXIS 101", "official_citation_present": true, "parallel_cite": "104 S. Ct. 2501; 81 L. Ed. 2d 377; 52 U.S.L.W. 4732", "title": "Nix v. Williams", "year": "1984"}}
{"assertion_id": "9175e7bd2b63c398", "dimension": "support", "kind": "home_role", "locator": {"home": "Inevitable Discovery & Independent Source"}, "payload": {"home": "Inevitable Discovery & Independent Source", "role": "Key — Progeny / Refinement", "title": "Nix v. Williams"}}
{"assertion_id": "cce52c2981bc8c3c", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Inevitable discovery: unlawfully obtained evidence is admissible if the prosecution proves by a preponderance it would inevitably have…", "title": "Nix v. Williams"}}
{"assertion_id": "14f672d3ed4e3b29", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Nix v. Williams"}}
{"assertion_id": "ae2917f0bd1bc012", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1984-06-11", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Nix v. Williams", "field_i_validity": "good_law", "scope_note": "Establishes the inevitable-discovery exception to the exclusionary rule; good law.", "title": "Nix v. Williams", "varies_by_point": "false"}}
```

### lake record — Nix v. Williams

```json
{
  "schema_version": "s2.v1",
  "record_id": "Nix v. Williams",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Nix v. Williams",
    "case_name_short": "Nix",
    "case_name_full": "Nix, Warden of the Iowa State Penitentiary v. Williams",
    "input_case_name": "Nix v. Williams",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-06-11",
    "year": 1984,
    "docket": null,
    "cluster_id": 111204,
    "lead_opinion_id": 9429647,
    "sibling_ids": [
      111204,
      9429647,
      9429648,
      9429649,
      9429650
    ],
    "absolute_url": "/opinion/111204/nix-v-williams/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "467 U.S. 431",
      "volume": "467",
      "reporter": "U.S.",
      "page": "431",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 2501",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2501",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 L. Ed. 2d 377",
        "volume": "81",
        "reporter": "L. Ed. 2d",
        "page": "377",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4732",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4732",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 101",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "101",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "467 U.S. 431",
        "volume": "467",
        "reporter": "U.S.",
        "page": "431",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 2501",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2501",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 L. Ed. 2d 377",
        "volume": "81",
        "reporter": "L. Ed. 2d",
        "page": "377",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 101",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "101",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4732",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4732",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "467 U.S. 431",
    "official_selection": {
      "court_class": "scotus",
      "selected": "467 U.S. 431",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-444",
      "page": null,
      "quote": "that led him to direct police to the body \u2014 interrogation later held to have violated his right to counsel (*Brewer v. Williams*). At the same time, a large organized volunteer search party was systematically searching the area and was within a few miles of the body. At Williams's retrial, the body-related evidence was admitted on an inevitable-discovery theory. ## Issue Whether evidence obtained as the fruit of a constitutional violation is nevertheless admissible if it would inevitably have been discovered by lawful means. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-06-11",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Nix v. Williams",
    "varies_by_point": false,
    "scope_note": "Establishes the inevitable-discovery exception to the exclusionary rule; good law.",
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
        "journal_ref": "Nix v. Williams:lane1_negative"
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
        "journal_ref": "Nix v. Williams:lane1_negative"
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
        "journal_ref": "Nix v. Williams:lane1_negative"
      },
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
        "journal_ref": "Nix v. Williams:lane1_negative"
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
        "journal_ref": "Nix v. Williams:lane1_negative"
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
        "journal_ref": "Nix v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Wallace",
          "cluster_id": 6239020,
          "cite": [
            "222 Cal. Rptr. 3d 795",
            "15 Cal. App. 5th 82",
            "2017 Cal. App. LEXIS 775"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane1_negative"
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
        "journal_ref": "Nix v. Williams:lane1_negative"
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
        "journal_ref": "Nix v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ornelas v. United States",
          "cluster_id": 118030,
          "cite": [
            "134 L. Ed. 2d 911",
            "116 S. Ct. 1657",
            "517 U.S. 690",
            "1996 U.S. LEXIS 3391"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Connelly",
          "cluster_id": 111779,
          "cite": [
            "93 L. Ed. 2d 473",
            "107 S. Ct. 515",
            "479 U.S. 157",
            "1986 U.S. LEXIS 23",
            "55 U.S.L.W. 4043"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bourjaily v. United States",
          "cluster_id": 111938,
          "cite": [
            "97 L. Ed. 2d 144",
            "107 S. Ct. 2775",
            "483 U.S. 171",
            "1987 U.S. LEXIS 2874",
            "22 Fed. R. Serv. 1105",
            "55 U.S.L.W. 4962"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
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
        "journal_ref": "Nix v. Williams:lane2_top_cited"
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
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. United States",
          "cluster_id": 112136,
          "cite": [
            "101 L. Ed. 2d 472",
            "108 S. Ct. 2529",
            "487 U.S. 533",
            "1988 U.S. LEXIS 2881",
            "56 U.S.L.W. 4801"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Dominguez-Castor",
          "cluster_id": 4691722,
          "cite": [
            "2020 COA 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. Michigan",
          "cluster_id": 145646,
          "cite": [
            "165 L. Ed. 2d 56",
            "126 S. Ct. 2159",
            "547 U.S. 586",
            "2006 U.S. LEXIS 4677"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Medina v. California",
          "cluster_id": 112775,
          "cite": [
            "120 L. Ed. 2d 353",
            "112 S. Ct. 2572",
            "505 U.S. 437",
            "1992 U.S. LEXIS 3696"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Arkansas",
          "cluster_id": 117936,
          "cite": [
            "131 L. Ed. 2d 976",
            "115 S. Ct. 1914",
            "514 U.S. 927",
            "1995 U.S. LEXIS 3464"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
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
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Coffman",
          "cluster_id": 2623595,
          "cite": [
            "96 P.3d 30",
            "17 Cal. Rptr. 3d 710",
            "34 Cal. 4th 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
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
        "journal_ref": "Nix v. Williams:lane2_top_cited"
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
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Zapien",
          "cluster_id": 1367717,
          "cite": [
            "846 P.2d 704",
            "4 Cal. 4th 929",
            "17 Cal. Rptr. 2d 122",
            "93 Daily Journal DAR 2940",
            "93 Cal. Daily Op. Serv. 1612",
            "1993 Cal. LEXIS 756"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
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
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hayes v. Florida",
          "cluster_id": 111382,
          "cite": [
            "84 L. Ed. 2d 705",
            "105 S. Ct. 1643",
            "470 U.S. 811",
            "1985 U.S. LEXIS 1523",
            "53 U.S.L.W. 4382"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Montoya",
          "cluster_id": 1202376,
          "cite": [
            "753 P.2d 729",
            "12 Brief Times Rptr. 482",
            "1988 Colo. LEXIS 39",
            "1988 WL 25119"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aaron Lindh v. James P. Murphy, Warden",
          "cluster_id": 726705,
          "cite": [
            "96 F.3d 856",
            "1996 U.S. App. LEXIS 24136",
            "1996 WL 517290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Boyer",
          "cluster_id": 2515839,
          "cite": [
            "133 P.3d 581",
            "42 Cal. Rptr. 3d 677",
            "38 Cal. 4th 412",
            "2006 Daily Journal DAR 5671",
            "2006 Cal. Daily Op. Serv. 3863",
            "2006 Cal. LEXIS 5397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Sutherland",
          "cluster_id": 2036519,
          "cite": [
            "860 N.E.2d 178",
            "223 Ill. 2d 187",
            "307 Ill. Dec. 524"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Moody",
          "cluster_id": 867478,
          "cite": [
            "94 P.3d 1119",
            "208 Ariz. 424"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ramirez",
          "cluster_id": 118180,
          "cite": [
            "140 L. Ed. 2d 191",
            "118 S. Ct. 992",
            "523 U.S. 65",
            "1998 U.S. LEXIS 1600"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brimage v. State",
          "cluster_id": 2417512,
          "cite": [
            "918 S.W.2d 466",
            "1996 Tex. Crim. App. LEXIS 5",
            "1994 WL 511395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
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
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111204 OR 9429647 OR 9429648 OR 9429649 OR 9429650) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDkyNzMyODAwMDAwJnM9NDM4NjA3OSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111204+OR+9429647+OR+9429648+OR+9429649+OR+9429650%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(111204 OR 9429647 OR 9429648 OR 9429649 OR 9429650)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNDAmcz0xNDMyMjk0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111204+OR+9429647+OR+9429648+OR+9429649+OR+9429650%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111204 OR 9429647 OR 9429648 OR 9429649 OR 9429650)",
        "reviewed": 69,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 69,
        "triage_read": 2,
        "triage_snippet_classified": 67
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111204 OR 9429647 OR 9429648 OR 9429649 OR 9429650)",
    "indexed_citing_opinions": 1839,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111204,
        "count": 1618,
        "count_source": "search"
      },
      {
        "opinion_id": 9429647,
        "count": 249,
        "count_source": "search"
      },
      {
        "opinion_id": 9429648,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429649,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429650,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3080,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/nix-v-williams.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwMTE3NyZzPTEwMTMyOTkxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111204+OR+9429647+OR+9429648+OR+9429649+OR+9429650%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111204,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 107423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 108429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 108846,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 108967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 109310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 109590,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 109757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 110067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 110230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 110300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 110372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 110589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 110676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 111169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 260072,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 260805,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 289216,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 354373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 374338,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 382927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 393006,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 405982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 410451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 414450,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 414492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 416957,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 1669210,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 1764351,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 1861096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 2115457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 2118871,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 2216952,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
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
    "date_created": "2026-07-05T15:53:21Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:53:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:53:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:56:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:53:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Nix v. Williams

```
<opinion type="majority">
<author id="A9P"><page-number citation-index="1" label="434">*434</page-number>Chief Justice Burger</author>
<p id="ABT">delivered the opinion of the Court.</p>
<p id="Aji">We granted certiorari to consider whether, at respondent Williams’ second murder trial in state court, evidence pertaining to the discovery and condition of the victim’s body was properly admitted on the ground that it would ultimately or inevitably have been discovered even if no violation of any constitutional or statutory provision had taken place.</p>
<p id="Alq">On December 24, 1968, 10-year-old Pamela Powers disappeared from a YMCA building in Des Moines, Iowa, where she had accompanied her parents to watch an athletic contest. Shortly after she disappeared, Williams was seen leaving the YMCA carrying a large bundle wrapped in a blanket; a 14-year-old boy who had helped Williams open his car door reported that he had seen “two legs in it and they were skinny and white.”</p>
<p id="Ad8q">Williams’ car was found the next day 160 miles east of Des Moines in Davenport, Iowa. Later several items of clothing belonging to the child, some of Williams’ clothing, and an army blanket like the one used to wrap the bundle that Williams carried out of the YMCA were found at a rest stop on <page-number citation-index="1" label="435">*435</page-number>Interstate 80 near Grinnell, between Des Moines and Davenport. A warrant was issued for Williams’ arrest.</p>
<p id="b493-5">Police surmised that Williams had left Pamela Powers or her body somewhere between Des Moines and the Grinnell rest stop where some of the young girl’s clothing had been found. On December 26, the Iowa Bureau of Criminal Investigation initiated a large-scale search. Two hundred volunteers divided into teams began the search 21 miles east of Grinnell, covering an area several miles to the north and south of Interstate 80. They moved westward from Poweshiek County, in which Grinnell was located, into Jasper County. Searchers were instructed to check all roads, abandoned farm buildings, ditches, culverts, and any other place in which the body of a small child could be hidden.</p>
<p id="b493-6">Meanwhile, Williams surrendered to local police in Davenport, where he was promptly arraigned. Williams contacted a Des Moines attorney who arranged for an attorney in Davenport to meet Williams at the Davenport police station. Des Moines police informed counsel they would pick Williams up in Davenport and return him to Des Moines without questioning him. Two Des Moines detectives then drove to Davenport, took Williams into custody, and proceeded to drive him back to Des Moines.</p>
<p id="b493-7">During the return trip, one of the policemen, Detective Learning, began a conversation with Williams, saying:</p>
<blockquote id="b493-8">“I want to give you something to think about while we’re traveling down the road. .. . They are predicting several inches of snow for tonight, and I feel that you yourself are the only person that knows where this little girl’s body is . . . and if you get a snow on top of it you yourself may be unable to find it. And since we will be going right past the area [where the body is] on the way into Des Moines, I feel that we could stop and locate the body, that the parents of this little girl should be entitled to a Christian burial for the little girl who was snatched away from them on Christmas [E]ve and murdered. . . . <page-number citation-index="1" label="436">*436</page-number>[A]fter a snow storm [we may not be] able to find it at all.”</blockquote>
<p id="b494-5">Learning told Williams he knew the body was in the area of Mitchellville — a town they would be passing on the way to Des Moines. He concluded the conversation by saying: “I do not want you to answer me. . . . Just think about it . . . .”</p>
<p id="b494-6">Later, as the police car approached Grinnell, Williams asked Learning whether the police had found the young girl’s shoes. After Learning replied that he was unsure, Williams directed the police to a point near a service station where he said he had left the shoes; they were not found. As they continued the drive to Des Moines, Williams asked whether the blanket had been found and then directed the officers to a rest area in Grinnell where he said he had disposed of the blanket; they did not find the blanket. At this point Learning and his party were joined by the officers in charge of the search. As they approached Mitchellville, Williams, without any further conversation, agreed to direct the officers to the child’s body.</p>
<p id="b494-7">The officers directing the search had called off the search at 3 p. m., when they left the Grinnell Police Department to join Learning at the rest area. At that time, one search team near the Jasper County-Polk County line was only two and one-half miles from where Williams soon guided Learning and his party to the body. The child’s body was found next to a culvert in a ditch beside a gravel road in Polk County, about two miles south of Interstate 80, and essentially within the area to be searched.</p>
<p id="b494-8">B</p>
<p id="b494-9">
<em>First Trial</em>
</p>
<p id="b494-10">In February 1969 Williams was indicted for first-degree murder. Before trial in the Iowa court, his counsel moved to suppress evidence of the body and all related evidence including the condition of the body as shown by the autopsy. The ground for the motion was that such evidence was the “fruit” <page-number citation-index="1" label="437">*437</page-number>or product of Williams’ statements made during the automobile ride from Davenport to Des Moines and prompted by Learning’s statements. The motion to suppress was denied.</p>
<p id="b495-5">The jury found Williams guilty of first-degree murder; the judgment of conviction was affirmed by the Iowa Supreme Court. <em>State </em>v. <em>Williams, </em><span class="citation" data-id="9720125"><a href="/opinion/2115457/state-v-williams/" aria-description="Citation for case: State v. Williams">182 N. W. 2d 396</a></span> (1970). Williams then sought release on habeas corpus in the United States District Court for the Southern District of Iowa. That court concluded that the evidence in question had been wrongly admitted at Williams’ trial, <em>Williams </em>v. <em>Brewer, </em><span class="citation" data-id="1669210"><a href="/opinion/1669210/williams-v-brewer/" aria-description="Citation for case: Williams v. Brewer">375 F. Supp. 170</a></span> (1974); a divided panel of the Court of Appeals for the Eighth Circuit agreed. <span class="citation" data-id="9461373"><a href="/opinion/324530/robert-anthony-williams-aka-anthony-erthel-williams-v-lou-v-brewer/" aria-description="Citation for case: Robert Anthony Williams, A/K/A Anthony Erthel Williams v....">509 F. 2d 227</a></span> (1974).</p>
<p id="b495-6">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./423/1031/">423 U. S. 1031</a></span> (1975), and a divided Court affirmed, holding that Detective Learning had obtained incriminating statements from Williams by what was viewed as interrogation in violation of his right to counsel. <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387</a></span> (1977). This Court’s opinion noted, however, that although Williams’ incriminating statements could not be introduced into evidence at a second trial, evidence of the body’s location and condition “might well be admissible on the theory that the body would have been discovered in any event, even had incriminating statements not been elicited from Williams.” <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#407" aria-description="Citation for case: Brewer v. Williams"><em>Id., </em>at 407, n. 12</a></span>.</p>
<p id="b495-7">C</p>
<p id="b495-8">
<em>Second Trial</em>
</p>
<p id="b495-9">At Williams’ second trial in 1977 in the Iowa court, the prosecution did not offer Williams’ statements into evidence, nor did it seek to show that Williams had directed the police to the child’s body. However, evidence of the condition of her body as it was found, articles and photographs of her clothing, and the results of post mortem medical and chemical tests on the body were admitted. The trial court concluded that the State had proved by a preponderance of the evidence that, if the search had not been suspended and Williams had not led the police to the victim, her body would have been <page-number citation-index="1" label="438">*438</page-number>discovered <em>“within a short time” </em>in essentially the same condition as it was actually found. The trial court also ruled that if the police had not located the body, “the search would clearly have been taken up again where it left off, given the extreme circumstances of this case and the body would [have] been found <em>in short order” </em>App. 86 (emphasis added).</p>
<p id="b496-5">In finding that the body would have been discovered in essentially the same condition as it was actually found, the court noted that freezing temperatures had prevailed and tissue deterioration would have been suspended. <em>Id., </em>at 87. The challenged evidence was admitted and the jury again found Williams guilty of first-degree murder; he was sentenced to life in prison.</p>
<p id="b496-6">On appeal, the Supreme Court of Iowa again affirmed. <span class="citation" data-id="2118871"><a href="/opinion/2118871/state-v-williams/" aria-description="Citation for case: State v. Williams">285 N. W. 2d 248</a></span> (1979). That court held that there was in fact a “hypothetical independent source” exception to the exclusionary rule:</p>
<blockquote id="b496-7">“After the defendant has shown unlawful conduct on the part of the police, the State has the burden to show by a preponderance of the evidence that (1) the police did not act in bad faith for the purpose of hastening discovery of the evidence in question, and (2) that the evidence in question would have been discovered by lawful means.” <span class="citation" data-id="2118871"><a href="/opinion/2118871/state-v-williams/#260" aria-description="Citation for case: State v. Williams"><em>Id., </em>at 260</a></span>.</blockquote>
<p id="b496-8">As to the first element, the Iowa Supreme Court, having reviewed the relevant cases, stated:</p>
<blockquote id="b496-9">“The issue of the propriety of the police conduct in this case, as noted earlier in this opinion, has caused the closest possible division of views in every appellate court which has considered the question. In light of the legitimate disagreement among individuals well versed in the law of criminal procedure who were given the opportunity for calm deliberation, it cannot be said that the actions of the police were taken in bad faith.” <span class="citation" data-id="2118871"><a href="/opinion/2118871/state-v-williams/#260" aria-description="Citation for case: State v. Williams"><em>Id., </em>at 260-261</a></span>.</blockquote>
<p id="b497-4"><page-number citation-index="1" label="439">*439</page-number>The Iowa court then reviewed the evidence <em>de </em>novo<footnotemark>1</footnotemark> and concluded that the State had shown by a preponderance of the evidence that, even if Williams had not guided police to the child’s body, it would inevitably have been found by lawful activity of the search party before its condition had materially changed.</p>
<p id="b497-5">In 1980 Williams renewed his attack on the state-court conviction by seeking a writ of habeas corpus in the United States District Court for the Southern District of Iowa. The District Court conducted its own independent review of the evidence and concluded, as had the state courts, that the body would inevitably have been found by the searchers in essentially the same condition it was in when Williams led police to its discovery. The District Court denied Williams’ petition. <span class="citation" data-id="1764351"><a href="/opinion/1764351/williams-v-nix/" aria-description="Citation for case: Williams v. Nix">528 F. Supp. 664</a></span> (1981).</p>
<p id="b497-6">The Court of Appeals for the Eighth Circuit reversed, <span class="citation" data-id="9470326"><a href="/opinion/414492/robert-anthony-williams-v-crispus-nix-warden-of-the-iowa-state/" aria-description="Citation for case: Robert Anthony Williams v. Crispus Nix, Warden of the...">700 F. 2d 1164</a></span> (1983); an equally divided court denied rehearing en banc. <span class="citation" data-id="9470326"><a href="/opinion/414492/robert-anthony-williams-v-crispus-nix-warden-of-the-iowa-state/#1175" aria-description="Citation for case: Robert Anthony Williams v. Crispus Nix, Warden of the..."><em>Id., </em>at 1175</a></span>. That court assumed, without deciding, that there is an inevitable discovery exception to the exclusionary rule and that the Iowa Supreme Court correctly stated that exception to require proof that the police did not act in bad faith and that the evidence would have been discovered absent any constitutional violation. In reversing the District Court’s denial of habeas relief, the Court of Appeals stated:</p>
<blockquote id="b497-7">“We hold that the State has not met the first requirement. It is therefore unnecessary to decide whether the state courts’ finding that the body would have been discovered anyway is fairly supported by the record. It is also unnecessary to decide whether the State must prove the two elements of the exception by clear and <page-number citation-index="1" label="440">*440</page-number>convincing evidence, as defendant argues, or by a preponderance of the evidence, as the state courts held.</blockquote>
<blockquote id="A-J">“The state trial court, in denying the motion to suppress, made no finding one way or the other on the question of bad faith. Its opinion does not even mention the issue and seems to proceed on the assumption — contrary to the rule of law later laid down by the Supreme Court of Iowa — that the State needed to show only that the body would have been discovered in any event. The Iowa Supreme Court did expressly address the issue . . . and a finding by an appellate court of a state is entitled to the same presumption of correctness that attaches to trial-court findings under <span class="citation no-link">28 U. S. C. § 2254</span>(d). . . . We conclude, however, that the state Supreme Court’s finding that the police did not act in bad faith is not entitled to the shield of §2254(d) . . . .” <em>Id., </em>at 1169-1170 (footnotes omitted).</blockquote>
<p id="AMx">We granted the State’s petition for certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./461/956/">461 U. S. 956</a></span> (1983), and we reverse.</p>
<p id="AQIK">a</p>
<p id="Ai2">
<em>&gt;</em>
</p>
<p id="A68">The Iowa Supreme Court correctly stated that the “vast majority” of all courts, both state and federal, recognize an inevitable discovery exception to the exclusionary rule.<footnotemark>2</footnotemark> We <page-number citation-index="1" label="441">*441</page-number>are now urged to adopt and apply the so-called ultimate or inevitable discovery exception to the exclusionary rule.</p>
<p id="b499-5">Williams contends that evidence of the body’s location and condition is “fruit of the poisonous tree,” <em>i. e., </em>the “fruit” or product of Detective Learning’s plea to help the child’s parents give her “a Christian burial,” which this Court had already held equated to interrogation. He contends that admitting the challenged evidence violated the Sixth Amendment whether it would have been inevitably discovered or not. Williams also contends that, if the inevitable discovery doctrine is constitutionally permissible, it must include a threshold showing of police good faith.</p>
<p id="b499-6">B</p>
<p id="b499-7">The doctrine requiring courts to suppress evidence as the tainted “fruit” of unlawful governmental conduct had its genesis in <em>Silverthome Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920); there, the Court held that the exclusionary rule applies not only to the illegally obtained evidence itself, but also to other incriminating evidence derived from the primary evidence. The holding of <em>Silverthome </em>was carefully limited, however, for the Court emphasized that such information does not automatically become “sacred and inaccessible.” <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States"><em>Id., </em>at 392</a></span>.</p>
<blockquote id="b499-8">“If knowledge of [such facts] is gained from an <em>independent source, </em>they may be proved like any others . . . .” <em>Ibid, </em>(emphasis added).</blockquote>
<p id="b499-9"><em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), extended the exclusionary rule to evidence that was the indirect product or “fruit” of unlawful police conduct, but there again the Court emphasized that evidence that has been illegally obtained need not always be suppressed, stating:</p>
<blockquote id="b500-4"><page-number citation-index="1" label="442">*442</page-number>“We need not hold that all evidence is ‘fruit of the poisonous tree’ simply because it would not have come to light <em>but for the illegal actions </em>of the police. Rather, the more apt question in such a case is ‘whether, granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint. <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#487" aria-description="Citation for case: Wong Sun v. United States"><em>Id., </em>at 487-488</a></span> (emphasis added) (quoting J. Maguire, Evidence of Guilt 221 (1959)).</blockquote>
<p id="b500-5">The Court thus pointedly negated the kind of good-faith requirement advanced by the Court of Appeals in reversing the District Court.</p>
<p id="b500-6">Although <em>Silverthorne </em>and <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span> </em>involved violations of the Fourth Amendment, the “fruit of the poisonous tree” doctrine has not been limited to cases in which there has been a Fourth Amendment violation. The Court has applied the doctrine where the violations were of the Sixth Amendment, see <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), as well as of the Fifth Amendment.<footnotemark>3</footnotemark></p>
<p id="b500-7">The core rationale consistently advanced by this Court for extending the exclusionary rule to evidence that is the fruit of unlawful police conduct has been that this admittedly drastic and socially costly course is needed to deter police from <page-number citation-index="1" label="443">*443</page-number>violations of constitutional and statutory protections. This Court has accepted the argument that the way to ensure such protections is to exclude evidence seized as a result of such violations notwithstanding the high social cost of letting persons obviously guilty go unpunished for their crimes. On this rationale, the prosecution is not to be put in a better position than it would have been in if no illegality had transpired.</p>
<p id="b501-5">By contrast, the derivative evidence analysis ensures that the prosecution is not put in a <em>worse </em>position simply because of some earlier police error or misconduct. The independent source doctrine allows admission of evidence that has been discovered by means wholly independent of any constitutional violation. That doctrine, although closely related to the inevitable discovery doctrine, does not apply here; Williams’ statements to Learning indeed led police to the child’s body, but that is not the whole story. The independent source doctrine teaches us that the interest of society in deterring unlawful police conduct and the public interest in having juries receive all probative evidence of a crime are properly balanced by putting the police in the same, not a <em>worse, </em>position that they would have been in if no police error or misconduct had occurred.<footnotemark>4</footnotemark> See <em>Murphy </em>v. <em>Waterfront Comm’n of New York Harbor, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#79" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 79</a></span> (1964); <em>Kastigar </em>v. <em>United States, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#457" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 457, 458-459</a></span> (1972). When the challenged evidence has an independent source, exclusion of such evidence would put the police in a worse position than they would have been in absent any error or violation. There <page-number citation-index="1" label="444">*444</page-number>is a functional similarity between these two doctrines in that exclusion of evidence that would inevitably have been discovered would also put the government in a worse position, because the police would have obtained that evidence if no misconduct had taken place. Thus, while the independent source exception would not justify admission of evidence in this case, its rationale is wholly consistent with and justifies our adoption of the ultimate or inevitable discovery exception to the exclusionary rule.</p>
<p id="b502-5">It is clear that the cases implementing the exclusionary rule “begin with the premise that the challenged evidence is <em>in some sense </em>the product of illegal governmental activity.” <em>United States </em>v. <em>Crews, </em><span class="citation" data-id="9427838"><a href="/opinion/110230/united-states-v-crews/#471" aria-description="Citation for case: United States v. Crews">445 U. S. 463, 471</a></span> (1980) (emphasis added). Of course, this does not end the inquiry. If the prosecution can establish by a preponderance of the evidence that the information ultimately or inevitably would have been discovered by lawful means — here the volunteers’ search— then the deterrence rationale has so little basis that the evidence should be received.<footnotemark>5</footnotemark> Anything less would reject logic, experience, and common sense.</p>
<p id="b503-4"><page-number citation-index="1" label="445">*445</page-number>The requirement that the prosecution must prove the absence of bad faith, imposed here by the Court of Appeals, would place courts in the position of withholding from juries relevant and undoubted truth that would have been available to police absent any unlawful police activity. Of course, that view would put the police in a <em>worse </em>position than they would have been in if no unlawful conduct had transpired. And, of equal importance, it wholly fails to take into account the enormous societal cost of excluding truth in the search for truth in the administration of justice. Nothing in this Court’s prior holdings supports any such formalistic, pointless, and punitive approach.</p>
<p id="b503-5">The Court of Appeals concluded, without analysis, that if an absence-of-bad-faith requirement were not imposed, “the temptation to risk deliberate violations of the Sixth Amendment would be too great, and the deterrent effect of the Exclusionary Rule reduced too far.” <span class="citation" data-id="9470326"><a href="/opinion/414492/robert-anthony-williams-v-crispus-nix-warden-of-the-iowa-state/#1169" aria-description="Citation for case: Robert Anthony Williams v. Crispus Nix, Warden of the...">700 F. 2d, at 1169, n. 5</a></span>. We reject that view. A police officer who is faced with the opportunity to obtain evidence illegally will rarely, if ever, be in a position to calculate whether the evidence sought would inevitably be discovered. Cf. <em>United States </em>v. <em>Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#283" aria-description="Citation for case: United States v. Ceccolini">435 U. S. 268, 283</a></span> (1978):</p>
<blockquote id="b503-6">“[T]he concept of effective deterrence assumes that the police officer consciously realizes the probable consequences of a presumably impermissible course of conduct” (opinion concurring in judgment).</blockquote>
<p id="b503-7">On the other hand, when an officer is aware that the evidence will inevitably be discovered, he will try to avoid engaging in <page-number citation-index="1" label="446">*446</page-number>any questionable practice. In that situation, there will be little to gain from taking any dubious “shortcuts” to obtain the evidence. Significant disincentives to obtaining evidence illegally — including the possibility of departmental discipline and civil liability — also lessen the likelihood that the ultimate or inevitable discovery exception will promote police misconduct. See <em>Bivens </em>v. <em>Six Unknown Federal Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#397" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388, 397</a></span> (1971). In these circumstances, the societal costs of the exclusionary rule far outweigh any possible benefits to deterrence that a good-faith requirement might produce.</p>
<p id="b504-5">Williams contends that because he did not waive his right to the assistance of counsel, the Court may not balance competing values in deciding whether the challenged evidence was properly admitted. He argues that, unlike the exclusionary rule in the Fourth Amendment context, the essential purpose of which is to deter police misconduct, the Sixth Amendment exclusionary rule is designed to protect the right to a fair trial and the integrity of the factfinding process. Williams contends that, when those interests are at stake, the societal costs of excluding evidence obtained from responses presumed involuntary are irrelevant in determining whether such evidence should be excluded. We disagree.</p>
<p id="b504-6">Exclusion of physical evidence that would inevitably have been discovered adds nothing to either the integrity or fairness of a criminal trial. The Sixth Amendment right to counsel protects against unfairness by preserving the adversary process in which the reliability of proffered evidence may be tested in cross-examination. See <em>United States </em>v. <em>Ash, </em><span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/#314" aria-description="Citation for case: United States v. Ash">413 U. S. 300, 314</a></span> (1973); <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#241" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 241</a></span> (1973). Here, however, Detective Learning’s conduct did nothing to impugn the reliability of the evidence in question — the body of the child and its condition as it was found, articles of clothing found on the body, and the autopsy. No one would seriously contend that the presence of counsel in the police car when Learning appealed to Wil<page-number citation-index="1" label="447">*447</page-number>liams’ decent human instincts would have had any bearing on the reliability of the body as evidence. Suppression, in these circumstances, would do nothing whatever to promote the integrity of the trial process, but would inflict a wholly unacceptable burden on the administration of criminal justice.</p>
<p id="b505-5">Nor would suppression ensure fairness on the theory that it tends to safeguard the adversary system of justice. To assure the fairness of trial proceedings, this Court has held that assistance of counsel must be available at pretrial confrontations where “the subsequent trial [cannot] cure a[n otherwise] one-sided confrontation between prosecuting authorities and the uncounseled defendant.” <em>United States </em>v. <span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/#315" aria-description="Citation for case: United States v. Ash"><em>Ash, supra, </em>at 315</a></span>. Fairness can be assured by placing the State and the accused in the same positions they would have been in had the impermissible conduct not taken place. However, if the government can prove that the evidence would have been obtained inevitably and, therefore, would have been admitted regardless of any overreaching by the police, there is no rational basis to keep that evidence from the jury in order to ensure the fairness of the trial proceedings. In that situation, the State has gained no advantage at trial and the defendant has suffered no prejudice. Indeed, suppression of the evidence would operate to undermine the adversary system by putting the State in a <em>worse </em>position than it would have occupied without any police misconduct. Williams’ argument that inevitable discovery constitutes impermissible balancing of values is without merit.</p>
<p id="b505-6">More than a half century ago, Judge, later Justice, Cardozo made his seminal observation that under the exclusionary rule “[t]he criminal is to go free because the constable has blundered.” <em>People </em>v. <em>Defore, </em><span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#21" aria-description="Citation for case: People v. Defore">242 N. Y. 13, 21</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#587" aria-description="Citation for case: People v. Defore">150 N. E. 585, 587</a></span> (1926). Prophetically, he went on to consider “how far-reaching in its effect upon society” the exclusionary rule would be when</p>
<blockquote id="b505-7">“[t]he pettiest peace officer would have it in his power through overzeal or indiscretion to confer immunity upon <page-number citation-index="1" label="448">*448</page-number>an offender for crimes the most flagitious.” <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#23" aria-description="Citation for case: People v. Defore"><em>Id., </em>at 23</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#588" aria-description="Citation for case: People v. Defore">150 N. E., at 588</a></span>.</blockquote>
<p id="b506-5">Some day, Cardozo speculated, some court might press the exclusionary rule to the outer limits of its logic — or beyond— and suppress evidence relating to the “body of a murdered” victim because of the means by which it was found. <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#23" aria-description="Citation for case: People v. Defore"><em>Id., </em>at 23-24</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#588" aria-description="Citation for case: People v. Defore">150 N. E., at 588</a></span>. Cardozo’s prophecy was fulfilled in <em>Killough </em>v. <em>United States, </em>114 U. S. App. D. C. 305, 309, <span class="citation" data-id="9449118"><a href="/opinion/260072/james-w-killough-v-united-states/#245" aria-description="Citation for case: James W. Killough v. United States">315 F. 2d 241, 245</a></span> (1962) (en banc). But when, as here, the evidence in question would inevitably have been discovered without reference to the police error or misconduct, there is no nexus sufficient to provide a taint and the evidence is admissible.</p>
<p id="b506-6">C</p>
<p id="b506-7">The Court of Appeals did not find it necessary to consider whether the record fairly supported the finding that the volunteer search party would ultimately or inevitably have discovered the victim’s body. However, three courts independently reviewing the evidence have found that the body of the child inevitably would have been found by the searchers. Williams challenges these findings, asserting that the record contains only the <em>“post hoc </em>rationalization” that the search efforts would have proceeded two and one-half miles into Polk County where Williams had led police to the body.</p>
<p id="b506-8">When that challenge was made at the suppression hearing preceding Williams’ second trial, the prosecution offered the testimony of Agent Ruxlow of the Iowa Bureau of Criminal Investigation. Ruxlow had organized and directed some 200 volunteers who were searching for the child’s body. Tr. of Hearings on Motion to Suppress in <em>State </em>v. <em>Williams, </em>No. CR 55805, p. 34 (May 31, 1977). The searchers were instructed “to check all the roads, the ditches, any culverts .... If they came upon any abandoned farm buildings, they were instructed to go onto the property and search those abandoned farm buildings or any other places where a <page-number citation-index="1" label="449">*449</page-number>small child could be secreted.” <em>Id., </em>at 35. Ruxlow testified that he marked off highway maps of Poweshiek and Jasper Counties in grid fashion, divided the volunteers into teams of four to six persons, and assigned each team to search specific grid areas. <em>Id., </em>at 34. Ruxlow also testified that, if the search had not been suspended because of Williams’ promised cooperation, it would have continued into Polk County, using the same grid system. <em>Id., </em>at 36, 39-40. Although he had previously marked off into grids only the highway maps of Poweshiek and Jasper Counties, Ruxlow had obtained a map of Polk County, which he said he would have marked off in the same manner had it been necessary for the search to continue. <em>Id., </em>at 39.</p>
<p id="b507-5">The search had commenced at approximately 10 a. m. and moved westward through Poweshiek County into Jasper County. At approximately 3 p. m., after Williams had volunteered to cooperate with the police, Detective Learning, who was in the police car with Williams, sent word to Ruxlow and the other Special Agent directing the search to meet him at the Grinnell truck stop and the search was suspended at that time. <em>Id., </em>at 51-52. Ruxlow also stated that he was “under the impression that there was a possibility” that Williams would lead them to the child’s body at that time. Id., at 61. The search was not resumed once it was learned that Williams had led the police to the body, <em>id., </em>at 57, which was found two and one-half miles from where the search had stopped in what would have been the easternmost grid to be searched in Polk County, <em>id., </em>at 39. There was testimony that it would have taken an additional three to five hours to discover the body if the search had continued, <em>id., </em>at 41; the body was found near a culvert, one of the kinds of places the teams had been specifically directed to search.</p>
<p id="b507-6">On this record it is clear that the search parties were approaching the actual location of the body, and we are satisfied, along with three courts earlier, that the volunteer search teams would have resumed the search had Williams <page-number citation-index="1" label="450">*450</page-number>not earlier led the police to the body and the body inevitably would have been found. The evidence asserted by Williams as newly discovered, <em>i. e., </em>certain photographs of the body and deposition testimony of Agent Ruxlow made in connection with the federal habeas proceeding, does not demonstrate that the material facts were inadequately developed in the suppression hearing in state court or that Williams was denied a full, fair, and adequate opportunity to present all relevant facts at the suppression hearing.<footnotemark>6</footnotemark></p>
<p id="b508-5">The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.<footnotemark>7</footnotemark></p>
<p id="b508-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b497-8"> Iowa law provides for <em>de novo </em>appellate review of factual as well as legal determinations in cases raising constitutional challenges. See, <em>e. g., Armento </em>v. <em>Baughman, </em><span class="citation" data-id="2216952"><a href="/opinion/2216952/armento-v-baughman/#15" aria-description="Citation for case: Armento v. Baughman">290 N. W. 2d 11, 15</a></span> (Iowa 1980); <em>State </em>v. <em>Ege, </em><span class="citation" data-id="9689598"><a href="/opinion/1861096/state-v-ege/#352" aria-description="Citation for case: State v. Ege">274 N. W. 2d 350, 352</a></span> (Iowa 1979).</p>
</footnote>
<footnote label="2">
<p id="AGm"> Every Federal Court of Appeals having jurisdiction over criminal matters, including the Eighth Circuit in a case decided after the instant case, has endorsed the inevitable discovery doctrine. See <em>Wayne </em>v. <em>United States, </em>115 U. S. App. D. C. 234, 238, <span class="citation" data-id="9449370"><a href="/opinion/260805/lewis-l-wayne-v-united-states/#209" aria-description="Citation for case: Lewis L. Wayne v. United States">318 F. 2d 205, 209</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./375/860/">375 U. S. 860</a></span> (1963); <em>United States </em>v. <em>Bienvenue, </em><span class="citation" data-id="382927"><a href="/opinion/382927/united-states-v-donald-bienvenue/#914" aria-description="Citation for case: United States v. Donald Bienvenue">632 F. 2d 910, 914</a></span> (CA1 1980); <em>United States </em>v. <em>Fisher, </em><span class="citation" data-id="414450"><a href="/opinion/414450/united-states-v-howard-fisher/#784" aria-description="Citation for case: United States v. Howard Fisher">700 F. 2d 780, 784</a></span> (CA2 1983); <em>Government of Virgin Islands </em>v. <em>Gereau, </em><span class="citation" data-id="8173389"><a href="/opinion/8210936/government-of-virgin-islands-v-gereau/#927" aria-description="Citation for case: Government of Virgin Islands v. Gereau">502 F. 2d 914, 927-928</a></span> (CA3 1974), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./420/909/">420 U. S. 909</a></span> (1975); <em>United States </em>v. <em>Seohnlein, </em><span class="citation" data-id="289216"><a href="/opinion/289216/united-states-v-charles-w-seohnlein/#1053" aria-description="Citation for case: United States v. Charles W. Seohnlein">423 F. 2d 1051, 1053</a></span> (CA4), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./399/913/">399 U. S. 913</a></span> (1970); <em>United States </em>v. <em>Brookins, </em><span class="citation" data-id="9466472"><a href="/opinion/374338/united-states-v-wayne-garfield-brookins-iii/#1042" aria-description="Citation for case: United States v. Wayne Garfield Brookins, III">614 F. 2d 1037, 1042, 1044</a></span> (CA5 1980); <em>Papp </em>v. <em>Jago, </em><span class="citation" data-id="393006"><a href="/opinion/393006/timothy-papp-v-arnold-r-jago-supt/#222" aria-description="Citation for case: Timothy Papp v. Arnold R. Jago, Supt.">656 F. 2d 221, 222</a></span> (CA6 1981); <em>United States ex rel. Owens </em>v. <em>Twomey, </em><span class="citation" data-id="324383"><a href="/opinion/324383/united-states-of-america-ex-rel-jesse-owens-v-john-j-twomey-warden/#865" aria-description="Citation for case: United States of America Ex Rel. Jesse Owens v. John J....">508 F. 2d 858, 865-866</a></span> (CA7 1974); <em>United States </em>v. <em>Apker, </em><span class="citation" data-id="8916749"><a href="/opinion/8926961/united-states-v-apker/#306" aria-description="Citation for case: United States v. Apker">705 F. 2d 293, 306-307</a></span> (CA8 1983); <page-number citation-index="1" label="441">*441</page-number><em>United States </em>v. <em>Schmidt, </em><span class="citation" data-id="9464701"><a href="/opinion/354373/united-states-v-richard-a-schmidt/#1065" aria-description="Citation for case: United States v. Richard A. Schmidt">573 F. 2d 1057, 1065-1066, n. 9</a></span> (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./439/881/">439 U. S. 881</a></span> (1978); <em>United States </em>v. <em>Romero, </em><span class="citation" data-id="410451"><a href="/opinion/410451/united-states-v-carlos-richard-romero-united-states-of-america-v-joseph/#704" aria-description="Citation for case: United States v. Carlos Richard Romero, United States of...">692 F. 2d 699, 704</a></span> (CA10 1982); <em>United States </em>v. <em>Roper, </em><span class="citation" data-id="405982"><a href="/opinion/405982/united-states-v-james-morrow-roper-christian-matthew-newton-john-jackson/#1358" aria-description="Citation for case: United States v. James Morrow Roper, Christian Matthew...">681 F. 2d 1354, 1358</a></span> (CA11 1982).</p>
</footnote>
<footnote label="3">
<p id="b500-8"> In <em>Murphy </em>v. <em>Waterfront Comm’n of New York Harbor, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#79" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 79</a></span> (1964), the Court held that “a state witness may not be compelled to give testimony which may be incriminating under federal law unless the compelled testimony and its fruits cannot be used in any manner by federal officials in connection with a criminal prosecution against him.” The Court added, however, that “[o]nce a defendant demonstrates that he has testified, under a state grant of immunity, to matters related to the federal prosecution, the federal authorities have the burden of showing that their evidence is not tainted by establishing that they had an independent, legitimate source for the disputed evidence.” <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#79" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor"><em>Id., </em>at 79, n. 18</a></span>; see <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#103" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor"><em>id., </em>at 103</a></span> (White, J., concurring). Application of the independent source doctrine in the Fifth Amendment context was reaffirmed in <em>Kastigar </em>v. <em>United States, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#460" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 460-461</a></span> (1972).</p>
</footnote>
<footnote label="4">
<p id="b501-6"> The ultimate or inevitable discovery exception to the exclusionary rule is closely related in purpose to the harmless-error rule of <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#22" aria-description="Citation for case: Chapman v. California">386 U. S. 18, 22</a></span> (1967). The harmless-constitutional-error rule “serve[s] a very useful purpose insofar as [it] block[s] setting aside convictions for small errors or defects that have little, if any, likelihood of having changed the result of the trial.” The purpose of the inevitable discovery rule is to block setting aside convictions that would have been obtained without police misconduct.</p>
</footnote>
<footnote label="5">
<p id="b502-6"> As to the quantum of proof, we have already established some relevant guidelines. In <em>United States </em>v. <em>Matlock, </em><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/#178" aria-description="Citation for case: United States v. Matlock">415 U. S. 164, 178, n. 14</a></span> (1974) (emphasis added), we stated that “the controlling burden of proof at suppression hearings should impose <em>no greater burden </em>than proof by a preponderance of the evidence.” In <em>Lego </em>v. <em>Twomey, </em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#488" aria-description="Citation for case: Lego v. Twomey">404 U. S. 477, 488</a></span> (1972), we observed “from our experience [that] no substantial evidence has accumulated that federal rights have suffered from determining admissibility by a preponderance of the evidence” and held that the prosecution must prove by a preponderance of the evidence that a confession sought to be used at trial was voluntary. We are unwilling to impose added burdens on the already difficult task of proving guilt in criminal cases by enlarging the barrier to placing evidence of unquestioned truth before juries.</p>
<p id="b502-7">Williams argues that the preponderance-of-the-evidence standard used by the Iowa courts is inconsistent with <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967). In requiring clear and convincing evidence of an independent source for an in-court identification, the Court gave weight to the effect an uncounseled pretrial identification has in “crystallizing] the witnesses’ identification of the defendant for future reference.” <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#240" aria-description="Citation for case: United States v. Wade"><em>Id., </em>at 240</a></span>. The <page-number citation-index="1" label="445">*445</page-number>Court noted as well that possible unfairness at the lineup “may be the sole means of attack upon the unequivocal courtroom identification,” <em>ibid., </em>and recognized the difficulty of determining whether an in-court identification was based on independent recollection unaided by the lineup identification, <em>■id., </em>at 240-241. By contrast, inevitable discovery involves no speculative elements but focuses on demonstrated historical facts capable of ready verification or impeachment and does not require a departure from the usual burden of proof at suppression hearings.</p>
</footnote>
<footnote label="6">
<p id="b508-9"> Williams had presented to the District Court newly discovered evidence consisting of “previously overlooked photographs of the body at the site of its discovery and recent deposition testimony of the investigative officer in charge of the search [Ruxlow].” <span class="citation" data-id="1764351"><a href="/opinion/1764351/williams-v-nix/#671" aria-description="Citation for case: Williams v. Nix">528 F. Supp., at 671, n. 6</a></span>. He contends that Ruxlow’s testimony was no more than <em>“post hoc </em>rationalization” and challenges Ruxlow’s credibility. However, the state trial court and Federal District Court that heard Ruxlow’s testimony credited it. The District Court found that the newly discovered evidence “neither adds much to nor subtracts much from the suppression hearing evidence.” <em><span class="citation" data-id="1764351"><a href="/opinion/1764351/williams-v-nix/" aria-description="Citation for case: Williams v. Nix">Ibid.</a></span></em></p>
</footnote>
<footnote label="7">
<p id="b508-10"> In view of our holding that the challenged evidence was admissible under the inevitable discovery exception to the exclusionary rule, we find it unnecessary to decide whether <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U. S. 465</a></span> (1976), should be extended to bar federal habeas corpus review of Williams’ Sixth Amendment claim, and we express no view on that issue.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/North Carolina v. Butler.md  (`case`, 5 assertions)

### content_page

```
---
title: "North Carolina v. Butler"
type: case
citation: "441 U.S. 369 (1979)"
parallel_cite: "99 S. Ct. 1755; 60 L. Ed. 2d 286"
neutral_cite: 1979 U.S. LEXIS 91
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-04-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1979-04-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: North Carolina v. Butler
  varies_by_point: false
  scope_note: "Implied-waiver rule; reaffirmed in Berghuis v. Thompkins; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110065/north-carolina-v-butler/"
  cluster_id: 110065
  opinion_id: 9427547
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[Berghuis v. Thompkins]]", "[[Moran v. Burbine]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "waiver", "implied-waiver"]
holding: "An express written or oral waiver is not required; a valid Miranda waiver may be inferred from the suspect's words and conduct — but…"
lake:
  record_id: North Carolina v. Butler
  status: verified
  projected_at: 2026-07-06
---

# North Carolina v. Butler

*441 U.S. 369 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After his arrest, Butler was advised of his *[[Miranda v. Arizona|Miranda]]* rights and given a waiver form. He said he understood his rights but refused to sign the waiver, stating that he would talk but would not sign any form. He then made inculpatory statements without expressly waiving and without requesting counsel.

## Issue
Whether an explicit (signed or spoken) statement of waiver is necessary for a valid *[[Miranda v. Arizona|Miranda]]* waiver, or whether waiver may be inferred from the suspect's words and conduct.

## Rule
An express waiver is not required. "An express written or oral statement of waiver of the right to remain silent or of the right to counsel is usually strong proof of the validity of that waiver, but is not inevitably either necessary or sufficient to establish waiver." — 441 U.S. at 373. ^pin-373

"The courts must presume that a defendant did not waive his rights; the prosecution's burden is great; but in at least some cases waiver can be clearly inferred from the actions and words of the person interrogated." — *Id.* ^pin-373b

## Application
Butler's refusal to sign the waiver form did not, by itself, defeat waiver. His statement that he would talk — made after he acknowledged understanding his rights and without invoking counsel — could support a finding that he waived his rights through his words and conduct. The Court rejected the North Carolina Supreme Court's [[Common Legal Terms#per-se|per se]] rule requiring an explicit waiver and [[Reading and Citing Cases#on-remand|remanded]] for a determination under the proper standard.

## Conclusion
The state court's [[Common Legal Terms#per-se|per se]] rule requiring an express waiver was rejected; reversed and [[Reading and Citing Cases#on-remand|remanded]] to assess waiver from the totality of Butler's words and conduct.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Butler*'s implied-waiver principle was reaffirmed and extended in [[Berghuis v. Thompkins]], and operates within the voluntary/knowing-and-intelligent framework of [[Moran v. Burbine]].

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *North Carolina v. Butler*, 441 U.S. 369 (1979) — https://www.courtlistener.com/opinion/110065/north-carolina-v-butler/ — pinpoint: 373.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "388b598aadc320a3", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "441 U.S. 369 (1979)", "court": "U.S. Supreme Court", "neutral_cite": "1979 U.S. LEXIS 91", "official_citation_present": true, "parallel_cite": "99 S. Ct. 1755; 60 L. Ed. 2d 286", "title": "North Carolina v. Butler", "year": "1979"}}
{"assertion_id": "176fc7fa22af0975", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An express written or oral waiver is not required; a valid Miranda waiver may be inferred from the suspect's words and conduct — but…", "title": "North Carolina v. Butler"}}
{"assertion_id": "e3ab53ee9b3e3af4", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny / Refinement", "title": "North Carolina v. Butler"}}
{"assertion_id": "5a4f75c666274174", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "North Carolina v. Butler"}}
{"assertion_id": "e1a4896d717204ff", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1979-04-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "North Carolina v. Butler", "field_i_validity": "good_law", "scope_note": "Implied-waiver rule; reaffirmed in Berghuis v. Thompkins; good law.", "title": "North Carolina v. Butler", "varies_by_point": "false"}}
```

### lake record — North Carolina v. Butler

```json
{
  "schema_version": "s2.v1",
  "record_id": "North Carolina v. Butler",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "North Carolina v. Butler",
    "case_name_short": "",
    "case_name_full": "North Carolina v. Butler",
    "input_case_name": "North Carolina v. Butler",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-04-24",
    "year": 1979,
    "docket": null,
    "cluster_id": 110065,
    "lead_opinion_id": 9427547,
    "sibling_ids": [
      110065,
      9427547,
      9427548,
      9427549
    ],
    "absolute_url": "/opinion/110065/north-carolina-v-butler/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9021516,
        "score": 20,
        "case_name": "North Carolina v. Butler"
      },
      {
        "cluster_id": 9020876,
        "score": 20,
        "case_name": "North Carolina v. Butler"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "441 U.S. 369",
      "volume": "441",
      "reporter": "U.S.",
      "page": "369",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 1755",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1755",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 L. Ed. 2d 286",
        "volume": "60",
        "reporter": "L. Ed. 2d",
        "page": "286",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 91",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "91",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "441 U.S. 369",
        "volume": "441",
        "reporter": "U.S.",
        "page": "369",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 1755",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1755",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 L. Ed. 2d 286",
        "volume": "60",
        "reporter": "L. Ed. 2d",
        "page": "286",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 91",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "91",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "441 U.S. 369",
    "official_selection": {
      "court_class": "scotus",
      "selected": "441 U.S. 369",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-373",
      "page": null,
      "quote": "--- # North Carolina v. Butler *441 U.S. 369 (1979)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After his arrest, Butler was advised of his *Miranda* rights and given a waiver form. He said he understood his rights but refused to sign the waiver, stating that he would talk but would not sign any form. He then made inculpatory statements without expressly waiving and without requesting counsel. ## Issue Whether an explicit (signed or spoken) statement of waiver is necessary for a valid *Miranda* waiver, or whether waiver may be inferred from the suspect's words and conduct. ## Rule An express waiver is not required.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-373b",
      "page": null,
      "quote": "The courts must presume that a defendant did not waive his rights; the prosecution's burden is great; but in at least some cases waiver can be clearly inferred from the actions and words of the person interrogated.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-04-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "North Carolina v. Butler",
    "varies_by_point": false,
    "scope_note": "Implied-waiver rule; reaffirmed in Berghuis v. Thompkins; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Dias v. Boone",
          "cluster_id": 10680524,
          "cite": [
            "912 S.E.2d 547",
            "320 Ga. 785"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Delossantos",
          "cluster_id": 9405989,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "1A Auto, Inc. v. Director of the Office of Campaign and Political Finance",
          "cluster_id": 4533242,
          "cite": [
            "105 N.E.3d 1175",
            "480 Mass. 423"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Saldierna",
          "cluster_id": 4527726,
          "cite": [
            "817 S.E.2d 174",
            "371 N.C. 407"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane1_negative"
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
        "journal_ref": "North Carolina v. Butler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 2830722,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 2828358,
          "cite": [
            "413 S.C. 458",
            "776 S.E.2d 367",
            "2015 S.C. LEXIS 302"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth, Aplt v. Hill, E.",
          "cluster_id": 2754405,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Garcia, Irving Magana",
          "cluster_id": 2949812,
          "cite": [
            "429 S.W.3d 604",
            "2014 WL 1375457",
            "2014 Tex. Crim. App. LEXIS 540"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane1_negative"
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
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Connelly",
          "cluster_id": 111779,
          "cite": [
            "93 L. Ed. 2d 473",
            "107 S. Ct. 515",
            "479 U.S. 157",
            "1986 U.S. LEXIS 23",
            "55 U.S.L.W. 4043"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
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
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
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
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fare v. Michael C.",
          "cluster_id": 110117,
          "cite": [
            "61 L. Ed. 2d 197",
            "99 S. Ct. 2560",
            "442 U.S. 707",
            "1979 U.S. LEXIS 133"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
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
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Clover Leaf Creamery Co.",
          "cluster_id": 110380,
          "cite": [
            "66 L. Ed. 2d 659",
            "101 S. Ct. 715",
            "449 U.S. 456",
            "1981 U.S. LEXIS 14"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
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
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
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
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mays v. State",
          "cluster_id": 1523430,
          "cite": [
            "904 S.W.2d 920",
            "1995 Tex. App. LEXIS 1814",
            "1995 WL 470664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albert L. Wilson v. Edward Murray, Director of the Virginia Department of Corrections",
          "cluster_id": 480360,
          "cite": [
            "806 F.2d 1232",
            "1986 U.S. App. LEXIS 34712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beverly A. Seymour v. Diane Walker,respondent-Appellee",
          "cluster_id": 770145,
          "cite": [
            "224 F.3d 542",
            "2000 U.S. App. LEXIS 20170",
            "2000 WL 1154017"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Stephenson",
          "cluster_id": 2410270,
          "cite": [
            "878 S.W.2d 530",
            "1994 Tenn. LEXIS 143"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Solem v. Stumes",
          "cluster_id": 111112,
          "cite": [
            "79 L. Ed. 2d 579",
            "104 S. Ct. 1338",
            "465 U.S. 638",
            "1984 U.S. LEXIS 36",
            "52 U.S.L.W. 4307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Connecticut v. Barrett",
          "cluster_id": 111796,
          "cite": [
            "93 L. Ed. 2d 920",
            "107 S. Ct. 828",
            "479 U.S. 523",
            "1987 U.S. LEXIS 419",
            "55 U.S.L.W. 4151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Bomar",
          "cluster_id": 1989353,
          "cite": [
            "826 A.2d 831",
            "573 Pa. 426",
            "2003 Pa. LEXIS 920"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. State",
          "cluster_id": 2382336,
          "cite": [
            "504 A.2d 1096",
            "1986 Del. LEXIS 1040"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Powell",
          "cluster_id": 2690788,
          "cite": [
            "2012 Ohio 2577",
            "132 Ohio St. 3d 233"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garcia v. State",
          "cluster_id": 2459967,
          "cite": [
            "919 S.W.2d 370",
            "1996 Tex. Crim. App. LEXIS 35",
            "1994 WL 706957"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
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
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holland v. State",
          "cluster_id": 1784340,
          "cite": [
            "587 So. 2d 848",
            "1991 WL 178413"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Pena",
          "cluster_id": 1229684,
          "cite": [
            "869 P.2d 932",
            "232 Utah Adv. Rep. 3",
            "1994 Utah LEXIS 6",
            "1994 WL 46544"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Watkins v. Sowders",
          "cluster_id": 110371,
          "cite": [
            "66 L. Ed. 2d 549",
            "101 S. Ct. 654",
            "449 U.S. 341",
            "1981 U.S. LEXIS 53",
            "49 U.S.L.W. 4082"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Russel William Burket v. Ronald Angelone, Director, Virginia Department of Corrections",
          "cluster_id": 768204,
          "cite": [
            "208 F.3d 172",
            "2000 U.S. App. LEXIS 5116",
            "2000 WL 309299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110065 OR 9427547 OR 9427548 OR 9427549) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzQ0ODE2MDAwMDAwJnM9ODQ0MTU2JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110065+OR+9427547+OR+9427548+OR+9427549%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(110065 OR 9427547 OR 9427548 OR 9427549)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNjEmcz0xMjQ0NzUyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110065+OR+9427547+OR+9427548+OR+9427549%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110065 OR 9427547 OR 9427548 OR 9427549)",
        "reviewed": 46,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 46,
        "triage_read": 1,
        "triage_snippet_classified": 45
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110065 OR 9427547 OR 9427548 OR 9427549)",
    "indexed_citing_opinions": 1355,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110065,
        "count": 1169,
        "count_source": "search"
      },
      {
        "opinion_id": 9427547,
        "count": 212,
        "count_source": "search"
      },
      {
        "opinion_id": 9427548,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427549,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2173,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/north-carolina-v-butler.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwNDQ4MDgmcz0xMDI3NjE4OCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110065+OR+9427547+OR+9427548+OR+9427549%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110065,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 277766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 278912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 280792,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 288244,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 294040,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 296344,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 300514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 300899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 305663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 315587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 319939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 320109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 320439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 324438,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 328787,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 339071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 340511,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1163905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1180267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1191424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1224771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1259789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1264180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1275041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1338200,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1413276,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1414808,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1424568,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1434456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1575075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1657897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1658656,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1662874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1728481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1824562,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1885915,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1891400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1892749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 2157474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 2232976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 2327606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 2610043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 2616723,
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
    "date_created": "2026-07-05T15:56:28Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:56:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:56:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:00:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:56:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — North Carolina v. Butler

```
<opinion type="majority">
<author id="b428-5">Me. Justice Stewart</author>
<p id="ATY">delivered the opinion of the Court.</p>
<p id="b428-6">In evident conflict with the present view of every other court that has considered the issue, the North Carolina Supreme Court has held that <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, requires that no statement of a person under custodial interrogation may be admitted in evidence against him unless, at the time the statement was made, he explicitly waived the right to the presence of a lawyer. We granted certiorari to consider whether this <em>per se </em>rule reflects a proper understanding of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>decision. <span class="citation multiple-matches"><a href="/c/U.%20S./439/1046/">439 U. S. 1046</a></span>.</p>
<p id="b428-7">The respondent was convicted in a North Carolina trial court of kidnaping, armed robbery, and felonious assault. The evidence at his trial showed that he and a man named Elmer Lee had robbed a gas station in Goldsboro, N. C., in December 1976, and had shot the station attendant as he was attempting to escape. The attendant was paralyzed, but survived to testify against the respondent.</p>
<p id="b428-8">The prosecution also produced evidence of incriminating statements made by the respondent shortly after his arrest by Federal Bureau of Investigation agents in the Bronx, N. Y., on the basis of a North Carolina fugitive warrant. Outside the presence of the jury, FBI Agent Martinez testified that at the time of the arrest he fully advised the respondent of the rights delineated in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>case. According to the uncontroverted testimony of Martinez, the agents then took the respondent to the FBI office in nearby New Rochelle, N. Y. There, after the agents determined that the respondent had an 11th grade education and was literate, he was given the Bureau’s “Advice of Rights” form <page-number citation-index="1" label="371">*371</page-number>which he read.<footnotemark>1</footnotemark> When asked if he understood his rights, he replied that he did. The respondent refused to sign the waiver at the bottom of the form. He was told that he need neither speak nor sign the form, but that the agents would like him to talk to them. The respondent replied: “I will talk to you but I am not signing any form.” He then made inculpatory statements.<footnotemark>2</footnotemark> Agent Martinez testified that the respondent said nothing when advised of his right to the assistance of a lawyer. At no time did the respondent request counsel or attempt to terminate the agents’ questioning.</p>
<p id="b429-5">At the conclusion of this testimony the respondent moved to suppress the evidence of his incriminating statements on the ground that he had not waived his right to the assistance of counsel at the time the statements were made. The court denied the motion, finding that</p>
<blockquote id="b429-6">“the statement made by the defendant, William Thomas Butler, to Agent David C. Martinez, was made freely and voluntarily to said agent after having been advised of his rights as required by the Miranda ruling, including his right to an attorney being present at the time of the inquiry and that the defendant, Butler, understood his <page-number citation-index="1" label="372">*372</page-number>rights; [and] that he effectively waived his rights, including the right to have an attorney present during the questioning by his indication that he was willing to answer questions, having read the rights form together with the Waiver of Rights . . . App. A-22 to A-23.</blockquote>
<p id="b430-5">The respondent’s statements were then admitted into evidence, and the jury ultimately found the respondent guilty of each offense charged.</p>
<p id="b430-6">On appeal, the North Carolina Supreme Court reversed the convictions and ordered a new trial. It found that the statements had been admitted in violation of the requirements of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>decision, noting that the respondent had refused to waive in writing his right to have counsel present and that there had not been a <em>specific </em>oral waiver. As it had in at least two earlier cases, the court read the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion as</p>
<blockquote id="b430-7">“provid [ing] in plain language that waiver of the right to counsel during interrogation will not be recognized unless such waiver is 'specifically made’ after the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings have been given.” <span class="citation" data-id="1338200"><a href="/opinion/1338200/state-v-butler/#255" aria-description="Citation for case: State v. Butler">295 N. C. 250, 255</a></span>, <span class="citation" data-id="1338200"><a href="/opinion/1338200/state-v-butler/#413" aria-description="Citation for case: State v. Butler">244 S. E. 2d 410, 413</a></span> (1978).</blockquote>
<p id="b430-8">See <em>State </em>v. <em>Blackmon, </em><span class="citation" data-id="1275041"><a href="/opinion/1275041/state-v-blackmon/#49" aria-description="Citation for case: State v. Blackmon">280 N. C. 42, 49-50</a></span>, <span class="citation" data-id="1275041"><a href="/opinion/1275041/state-v-blackmon/#127" aria-description="Citation for case: State v. Blackmon">185 S. E. 2d 123, 127-128</a></span> (1971); <em>State </em>v. <em>Thacker, </em><span class="citation" data-id="1224771"><a href="/opinion/1224771/state-v-thacker/#453" aria-description="Citation for case: State v. Thacker">281 N. C. 447, 453-454</a></span>, <span class="citation" data-id="1224771"><a href="/opinion/1224771/state-v-thacker/#149" aria-description="Citation for case: State v. Thacker">189 S. E. 2d 145, 149-150</a></span> (1972).<footnotemark>3</footnotemark></p>
<p id="b430-9">We conclude that the North Carolina Supreme Court erred in its reading of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion. There, this Court said:</p>
<blockquote id="b430-10">“If the interrogation continues without the presence of an attorney and a statement is taken, a heavy burden <page-number citation-index="1" label="373">*373</page-number>rests on the government to demonstrate that the defendant knowingly and intelligently waived his privilege against self-incrimination and his right to retained or appointed counsel.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 475</a></span>.</blockquote>
<p id="b431-4">The Court’s opinion went on to say:</p>
<blockquote id="b431-5">“An express statement that the individual is willing to make a statement and does not want an attorney followed closely by a statement could constitute a waiver. But a valid waiver will not be presumed simply from the silence of the accused after warnings are given or simply from the fact that a confession was in fact eventually obtained.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></em></blockquote>
<p id="b431-6">Thus, the Court held that an express statement can constitute a waiver, and that silence alone after such warnings cannot do so. But the Court did not hold that such an express statement is indispensable to a finding of waiver.</p>
<p id="b431-7">An express written or oral statement of waiver of the right to remain silent or of the right to counsel is usually strong proof of the validity of that waiver, but is not inevitably either necessary or sufficient to establish waiver. The question is not one of form, but rather whether the defendant in fact knowingly and voluntarily waived the rights delineated in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>case. As was unequivocally said in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>mere silence is not enough. That does not mean that the defendant’s silence, coupled with an understanding of his rights and a course of conduct indicating waiver, may never support a conclusion that a defendant has waived his rights. The courts must presume that a defendant did not waive his rights; the prosecution’s burden is great; but in at least some cases waiver can be clearly inferred from the actions and words of the person interrogated.<footnotemark>4</footnotemark></p>
<p id="b432-4"><page-number citation-index="1" label="374">*374</page-number>The Court’s opinion in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>explained the reasons for the prophylactic rules it created:</p>
<blockquote id="b432-5">“We have concluded that without proper safeguards the process of in-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual’s will to resist and to compel him to speak where he would not otherwise do so freely. In order to combat these pressures and to permit a full opportunity to exercise the privilege against self-incrimination, the accused must be adequately and effectively apprised of his rights and the exercise of those rights must be fully honored.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 467</a></span>.</blockquote>
<p id="b432-6">The <em>per se </em>rule that the North Carolina Supreme Court has found in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>does not speak to these concerns. There is no doubt that this respondent was adequately and effectively apprised of his rights. The only question is whether he waived the exercise of one of those rights, the right to the presence of a lawyer. Neither the state court nor the respondent has offered any reason why there must be a negative answer to that question in the absence of an <em>express </em>waiver. This is not the first criminal case to question whether a defendant waived his constitutional rights. It is an issue with which courts must repeatedly deal. Even when a right scr fundamental as that to counsel at trial is involved, the question of waiver must be determined on “the particular facts and circumstances surrounding that case, including the back<page-number citation-index="1" label="375">*375</page-number>ground, experience, and conduct of the accused.” <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 464</a></span>. See also <em>United States </em>v. <em>Washington, </em><span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#188" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 188</a></span>; <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span>; <em>Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#739" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 739</a></span>.</p>
<p id="b433-4">We see no reason to discard that standard and replace it with an inflexible <em>per se </em>rule in a case such as this. As stated at the outset of this opinion, it appears that every court that has considered this question has now reached the same conclusion. Ten of the eleven United States Courts of Appeals<footnotemark>5</footnotemark> and the courts of at least 17 States<footnotemark>6</footnotemark> have held that an explicit state<page-number citation-index="1" label="376">*376</page-number>ment of waiver is not invariably necessary to support a finding that the defendant waived the right to remain silent or the right to counsel guaranteed by the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>case. By creating an inflexible rule that no implicit waiver can ever suffice, the North Carolina Supreme Court has gone beyond the requirements of federal organic law. It follows that its judgment cannot stand, since a state court can neither add to nor subtract from the mandates of the United States Constitution. <em>Oregon </em>v. <em>Hass, </em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span>.<footnotemark>7</footnotemark></p>
<p id="b434-5">Accordingly, the judgment is vacated, and the case is remanded to the North Carolina Supreme Court for further proceedings not inconsistent with this opinion.</p>
<p id="b434-6">
<em>It is so ordered.</em>
</p>
<judges id="b434-7">Mr. Justice Powell took no part in the consideration or decision of this case.</judges>
<footnote label="1">
<p id="b429-7"> The parties disagree over whether the respondent was also orally advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights at the New Rochelle office. There is no dispute that he was given those warnings orally at the scene of the arrest, or that he read the “Advice of Rights” form in the New Rochelle office. This factual controversy, therefore, is not relevant to the basic issue in this case.</p>
<p id="b429-8">The dissenting opinion points out, <em>post, </em>at 378, that at oral argument the respondent’s counsel disputed the fact that the respondent is literate. But the trial court specifically found that “it had been . . . determined by Agent Martinez that the defendant has an Eleventh Grade Education and that he could read and write . . . .” App. A-21. This finding, based upon uncontroverted evidence, is binding on this Court.</p>
</footnote>
<footnote label="2">
<p id="b429-9"> The respondent admitted to the agents that he and Lee had been drinking heavily on' the day of the robbery. He acknowledged that they had decided to rob a gas station, but denied that he had actually participated in the robbery. His friend, he said, had shot the attendant.</p>
</footnote>
<footnote label="3">
<p id="b430-11"> But see <em>State </em>v. <em>Siler, </em><span class="citation" data-id="1259789"><a href="/opinion/1259789/state-v-siler/#550" aria-description="Citation for case: State v. Siler">292 N. C. 543, 550</a></span>, <span class="citation" data-id="1259789"><a href="/opinion/1259789/state-v-siler/#738" aria-description="Citation for case: State v. Siler">234 S. E. 2d 733, 738</a></span> (1977). In that case, the North Carolina Supreme Court adhered to the interpretation of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>it first expressed in <em><span class="citation" data-id="1275041"><a href="/opinion/1275041/state-v-blackmon/" aria-description="Citation for case: State v. Blackmon">Blackmon</a></span>, </em>but acknowledged that it might find waiver without an express written or oral statement if the defendant’s subsequent comments revealed that his earlier silence had been meant as a waiver. Although <em><span class="citation" data-id="1259789"><a href="/opinion/1259789/state-v-siler/" aria-description="Citation for case: State v. Siler">Siler</a></span> </em>was cited by the State Supreme Court in the present case, that portion of the <em><span class="citation" data-id="1259789"><a href="/opinion/1259789/state-v-siler/" aria-description="Citation for case: State v. Siler">Siler</a></span> </em>opinion was not discussed.</p>
</footnote>
<footnote label="4">
<p id="b431-8"> We do not today even remotely question the holding in <em>Carnley </em>v. <em>Cochran, </em><span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/" aria-description="Citation for case: Carnley v. Cochran">369 U. S. 506</a></span>, which was specificaEy approved in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 475</a></span>. In that case, decided before <em>Gideon </em>v. <em>Wainwright, </em><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>, the Court held that the defendant had a <page-number citation-index="1" label="374">*374</page-number>constitutional right to counsel under the Fourteenth Amendment. The Florida Supreme Court had presumed that his right had been waived because there was no evidence in the record that he had requested counsel. The Court refused to allow a presumption of waiver from a silent record. It said: “The record must show, or there must be an allegation and evidence which show, that an accused was offered counsel but intelligently and understandingly rejected the offer.” <span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/#516" aria-description="Citation for case: Carnley v. Cochran">369 U. S., at 516</a></span>. This statement is consistent with our decision today, which is merely that a court <em>may </em>find an intelligent and understanding rejection of counsel in situations where the defendant did not <em>expressly </em>state as much.</p>
</footnote>
<footnote label="5">
<p id="b433-5"> <em>United States </em>v. <em>Speaks, </em><span class="citation" data-id="300899"><a href="/opinion/300899/united-states-v-albert-philip-speaks/" aria-description="Citation for case: United States v. Albert Philip Speaks">453 F. 2d 966</a></span> (CA1 1972); <em>United States </em>v. <em>Boston, </em>508. F. 2d 1171 (CA2 1974); <em>United States </em>v. <em>Stuckey, </em><span class="citation" data-id="296344"><a href="/opinion/296344/united-states-v-jusse-j-stuckey/" aria-description="Citation for case: United States v. Jusse J. Stuckey">441 F. 2d 1104</a></span> (CA3 1971); <em>Blackmon </em>v. <em>Blackledge, </em><span class="citation" data-id="339071"><a href="/opinion/339071/johnny-james-blackmon-v-stanley-blackledge-warden-central-prison/" aria-description="Citation for case: Johnny James Blackmon v. Stanley Blackledge, Warden,...">541 F. 2d 1070</a></span> (CA4 1976); <em>United States </em>v. <em>Hayes, </em><span class="citation" data-id="277766"><a href="/opinion/277766/united-states-v-maynard-francis-hayes/" aria-description="Citation for case: United States v. Maynard Francis Hayes">385 F. 2d 375</a></span> (CA4 1967); <em>United States </em>v. <em>Cavallino, </em><span class="citation" data-id="320109"><a href="/opinion/320109/united-states-v-ronald-anthony-cavallino/" aria-description="Citation for case: United States v. Ronald Anthony Cavallino">498 F. 2d 1200</a></span> (CA5 1974); <em>United States </em>v. <em>Montos, </em><span class="citation" data-id="288244"><a href="/opinion/288244/united-states-v-kenneth-george-montos/" aria-description="Citation for case: United States v. Kenneth George Montos">421 F. 2d 215</a></span> (CA5 1970); <em>United States </em>v. <em>Ganter, </em><span class="citation" data-id="294040"><a href="/opinion/294040/united-states-v-steven-ganter/" aria-description="Citation for case: United States v. Steven Ganter">436 F. 2d 364</a></span> (CA7 1970); <em>United States </em>v. <em>Marchildon, </em><span class="citation" data-id="328787"><a href="/opinion/328787/united-states-v-robert-dale-marchildon/" aria-description="Citation for case: United States v. Robert Dale Marchildon">519 F. 2d 337</a></span> (CA8 1975); <em>Hughes </em>v. <em>Swenson, </em><span class="citation" data-id="300514"><a href="/opinion/300514/dennis-paul-hughes-v-harold-r-swenson-warden/" aria-description="Citation for case: Dennis Paul Hughes v. Harold R. Swenson, Warden">452 F. 2d 866</a></span> (CA8 1971); <em>United States </em>v. <em>Moreno-Lopez, </em><span class="citation" data-id="305663"><a href="/opinion/305663/united-states-v-isabel-moreno-lopez/" aria-description="Citation for case: United States v. Isabel Moreno-Lopez">466 F. 2d 1205</a></span> (CA9 1972); <em>United States </em>v. <em>Hilliker, </em><span class="citation" data-id="293991"><a href="/opinion/293991/united-states-v-gary-lee-hilliker/" aria-description="Citation for case: United States v. Gary Lee Hilliker">436 F. 2d 101</a></span> (CA9 1970); <em>Bond </em>v. <em>United States, </em><span class="citation" data-id="280792"><a href="/opinion/280792/roy-gene-bond-v-united-states/" aria-description="Citation for case: Roy Gene Bond v. United States">397 F. 2d 162</a></span> (CA10 1968) (but see <em>Sullins </em>v. <em>United States, </em><span class="citation" data-id="9453346"><a href="/opinion/278912/howard-douglas-sullins-james-floyd-williams-audrey-louise-gillingham-v/" aria-description="Citation for case: Howard Douglas Sullins, James Floyd Williams, Audrey...">389 F. 2d 985</a></span> (CA10 1968)); <em>United States </em>v. <em>Cooper, </em>163 U. S. App. D. C. 55, <span class="citation" data-id="9460787"><a href="/opinion/320439/united-states-v-donald-m-cooper/" aria-description="Citation for case: United States v. Donald M. Cooper">499 F. 2d 1060</a></span> (1974). In <em>Blackmon </em>v. <em><span class="citation" data-id="339071"><a href="/opinion/339071/johnny-james-blackmon-v-stanley-blackledge-warden-central-prison/" aria-description="Citation for case: Johnny James Blackmon v. Stanley Blackledge, Warden,...">Blackledge, supra,</a></span> </em>the Court of Appeals for the Fourth Circuit specifically rejected the North Carolina Supreme Court’s inflexible view that only express waivers of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights can be valid.</p>
<p id="b433-6">The Courts of Appeals have unanimously rejected the similar argument that refusal to sign a written waiver form precludes a finding of waiver. See <em>United States </em>v. <em><span class="citation" data-id="300899"><a href="/opinion/300899/united-states-v-albert-philip-speaks/" aria-description="Citation for case: United States v. Albert Philip Speaks">Speaks, supra;</a></span> United States </em>v. <em>Boston, supra; United States </em>v. <em><span class="citation" data-id="296344"><a href="/opinion/296344/united-states-v-jusse-j-stuckey/" aria-description="Citation for case: United States v. Jusse J. Stuckey">Stuckey, supra;</a></span> United States </em>v. <em>Thompson, </em><span class="citation" data-id="286880"><a href="/opinion/286880/united-states-v-vernon-thompson/" aria-description="Citation for case: United States v. Vernon Thompson">417 F. 2d 196</a></span> (CA4 1969); <em>United States </em>v. <em>Guzman-Guzman, </em><span class="citation" data-id="315587"><a href="/opinion/315587/united-states-v-arturo-guzman-guzman/" aria-description="Citation for case: United States v. Arturo Guzman-Guzman">488 F. 2d 965</a></span> (CA5 1974); <em>United States </em>v. <em>Caulton, </em><span class="citation" data-id="319939"><a href="/opinion/319939/united-states-v-james-raymond-caulton/" aria-description="Citation for case: United States v. James Raymond Caulton">498 F. 2d 412</a></span> (CA6 1974); <em>United States </em>v. <em>Crisp, </em><span class="citation" data-id="293647"><a href="/opinion/293647/united-states-v-donald-roy-crisp/" aria-description="Citation for case: United States v. Donald Roy Crisp">435 F. 2d 354</a></span> (CA7 1970); <em>United States </em>v. <em>Zamarripa, </em><span class="citation" data-id="340511"><a href="/opinion/340511/united-states-v-antonio-valentino-zamarripa/" aria-description="Citation for case: United States v. Antonio Valentino Zamarripa">544 F. 2d 978</a></span> (CA8 1976); <em>United States </em>v. <em><span class="citation" data-id="305663"><a href="/opinion/305663/united-states-v-isabel-moreno-lopez/" aria-description="Citation for case: United States v. Isabel Moreno-Lopez">Moreno-Lopez, supra;</a></span> Bond </em>v. <em>United States, supra; </em>and <em>United States </em>v. <em><span class="citation" data-id="9460787"><a href="/opinion/320439/united-states-v-donald-m-cooper/" aria-description="Citation for case: United States v. Donald M. Cooper">Cooper, supra.</a></span></em></p>
</footnote>
<footnote label="6">
<p id="b433-7"><em> Sullivan </em>v. <em>State, </em><span class="citation" data-id="1658656"><a href="/opinion/1658656/sullivan-v-state/" aria-description="Citation for case: Sullivan v. State">351 So. 2d 659</a></span> (Ala. Crim. App.), cert. denied, <span class="citation" data-id="1657897"><a href="/opinion/1657897/ex-parte-sullivan/" aria-description="Citation for case: Ex Parte Sullivan">351 So. 2d 665</a></span> (Ala. 1977); <em>State </em>v. <em>Pineda, </em><span class="citation" data-id="1180267"><a href="/opinion/1180267/state-v-pineda/" aria-description="Citation for case: State v. Pineda">110 Ariz. 342</a></span>, <span class="citation" data-id="1180267"><a href="/opinion/1180267/state-v-pineda/" aria-description="Citation for case: State v. Pineda">519 P. 2d 41</a></span> (1974); <em>State ex rel. Berger </em>v. <em>Superior Court, </em><span class="citation multiple-matches"><a href="/c/Ariz./109/506/">109 Ariz. 506</a></span>, <span class="citation multiple-matches"><a href="/c/P.%202d/513/935/">513 P. 2d 935</a></span> (1973); <em>People </em>v. <em>Johnson, </em><span class="citation" data-id="9624615"><a href="/opinion/1413276/people-v-johnson/" aria-description="Citation for case: People v. Johnson">70 Cal. 2d 541</a></span>, <span class="citation" data-id="9624615"><a href="/opinion/1413276/people-v-johnson/" aria-description="Citation for case: People v. Johnson">450 P. 2d 865</a></span> (1969) (reversing lower court on other grounds); <em>People </em>v. <em>Weaver, </em><span class="citation" data-id="2616723"><a href="/opinion/2616723/people-v-weaver/" aria-description="Citation for case: People v. Weaver">179 Colo. 331</a></span>, <span class="citation" data-id="2616723"><a href="/opinion/2616723/people-v-weaver/" aria-description="Citation for case: People v. Weaver">500 P. 2d 980</a></span> (1972); <page-number citation-index="1" label="376">*376</page-number><em>Reed </em>v. <em>People, </em><span class="citation" data-id="2610043"><a href="/opinion/2610043/reed-v-people/" aria-description="Citation for case: Reed v. People">171 Colo. 421</a></span>, <span class="citation" data-id="2610043"><a href="/opinion/2610043/reed-v-people/" aria-description="Citation for case: Reed v. People">467 P. 2d 809</a></span> (1970); <em>State </em>v. <em>Craig, </em><span class="citation" data-id="1824562"><a href="/opinion/1824562/state-v-craig/" aria-description="Citation for case: State v. Craig">237 So. 2d 737</a></span> (Fla. 1970); <em>Peek </em>v. <em>State, </em><span class="citation" data-id="1424568"><a href="/opinion/1424568/peek-v-state/" aria-description="Citation for case: Peek v. State">239 Ga. 422</a></span>, <span class="citation" data-id="1424568"><a href="/opinion/1424568/peek-v-state/" aria-description="Citation for case: Peek v. State">238 S. E. 2d 12</a></span> (1977); <em>People </em>v. <em>Brooks, </em><span class="citation" data-id="2157474"><a href="/opinion/2157474/people-v-brooks/" aria-description="Citation for case: People v. Brooks">51 Ill. 2d 156</a></span>, <span class="citation" data-id="2157474"><a href="/opinion/2157474/people-v-brooks/" aria-description="Citation for case: People v. Brooks">281 N. E. 2d 326</a></span> (1972); <em>State </em>v. <em>Wilson, </em><span class="citation" data-id="1163905"><a href="/opinion/1163905/state-v-wilson/" aria-description="Citation for case: State v. Wilson">215 Kan. 28</a></span>, <span class="citation" data-id="1163905"><a href="/opinion/1163905/state-v-wilson/" aria-description="Citation for case: State v. Wilson">523 P. 2d 337</a></span> (1974); <em>State </em>v. <em>Hazelton, </em><span class="citation" data-id="2359781"><a href="/opinion/2359781/state-v-hazelton/" aria-description="Citation for case: State v. Hazelton">330 A. 2d 919</a></span> (Me. 1975); <em>Miller </em>v. <em>State, </em><span class="citation" data-id="9754194"><a href="/opinion/2327606/miller-v-state/" aria-description="Citation for case: Miller v. State">251 Md. 362</a></span>, <span class="citation" data-id="9754194"><a href="/opinion/2327606/miller-v-state/" aria-description="Citation for case: Miller v. State">247 A. 2d 530</a></span> (1968); <em>Commonwealth </em>v. <em>Murray, </em><span class="citation" data-id="2232976"><a href="/opinion/2232976/commonwealth-v-murray/" aria-description="Citation for case: Commonwealth v. Murray">359 Mass. 541</a></span>, <span class="citation" data-id="2232976"><a href="/opinion/2232976/commonwealth-v-murray/" aria-description="Citation for case: Commonwealth v. Murray">269 N. E. 2d 641</a></span> (1971); <em>State </em>v. <em>Alewine, </em><span class="citation" data-id="1662874"><a href="/opinion/1662874/state-v-alewine/" aria-description="Citation for case: State v. Alewine">474 S. W. 2d 848</a></span> (Mo. 1971); <em>Burnside </em>v. <em>State, </em><span class="citation" data-id="1728481"><a href="/opinion/1728481/burnside-v-state/" aria-description="Citation for case: Burnside v. State">473 S. W. 2d 697</a></span> (Mo. 1971); <em>Shirey </em>v. <em>State, </em><span class="citation" data-id="1191424"><a href="/opinion/1191424/shirey-v-state/" aria-description="Citation for case: Shirey v. State">520 P. 2d 701</a></span> (Okla. Crim. App. 1974); <em>State </em>v. <em>Davidson, </em><span class="citation" data-id="1434456"><a href="/opinion/1434456/state-v-davidson/" aria-description="Citation for case: State v. Davidson">252 Ore. 617</a></span>, <span class="citation" data-id="1434456"><a href="/opinion/1434456/state-v-davidson/" aria-description="Citation for case: State v. Davidson">451 P. 2d 481</a></span> (1969); <em>Commonwealth </em>v. <em>Garnett, </em><span class="citation" data-id="1892749"><a href="/opinion/1892749/commonwealth-v-garnett/" aria-description="Citation for case: Commonwealth v. Garnett">458 Pa. 4</a></span>, <span class="citation" data-id="1892749"><a href="/opinion/1892749/commonwealth-v-garnett/" aria-description="Citation for case: Commonwealth v. Garnett">326 A. 2d 335</a></span> (1974); <em>Bowling </em>v. <em>State, </em><span class="citation" data-id="1575075"><a href="/opinion/1575075/bowling-v-state/" aria-description="Citation for case: Bowling v. State">458 S. W. 2d 639</a></span> (Tenn. Crim. App. 1970); <em>State </em>v. <em>Young, </em><span class="citation" data-id="1414808"><a href="/opinion/1414808/state-v-young/" aria-description="Citation for case: State v. Young">89 Wash. 2d 613</a></span>, <span class="citation" data-id="1414808"><a href="/opinion/1414808/state-v-young/" aria-description="Citation for case: State v. Young">574 P. 2d 1171</a></span> (1978). See also <em>Aaron </em>v. <em>State, </em><span class="citation" data-id="1885915"><a href="/opinion/1885915/aaron-v-state/" aria-description="Citation for case: Aaron v. State">275 A. 2d 791</a></span> (Del. 1971); <em>State </em>v. <em>Nelson, </em><span class="citation" data-id="1891400"><a href="/opinion/1891400/state-v-nelson/" aria-description="Citation for case: State v. Nelson">257 N. W. 2d 356</a></span> (Minn. 1977); <em>Land </em>v. <em>Commonwealth, </em><span class="citation" data-id="1264180"><a href="/opinion/1264180/land-v-commonwealth/" aria-description="Citation for case: Land v. Commonwealth">211 Va. 223</a></span>, <span class="citation" data-id="1264180"><a href="/opinion/1264180/land-v-commonwealth/" aria-description="Citation for case: Land v. Commonwealth">176 S. E. 2d 586</a></span> (1970) (reversing lower court on other grounds).</p>
</footnote>
<footnote label="7">
<p id="b434-11"> By the same token this Court must accept whatever construction of a state constitution is placed upon it by the highest court of the State.</p>
</footnote>
</opinion>
```

---
