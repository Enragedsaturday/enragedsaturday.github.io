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

## GROUP: content/cases/Ryburn v. Huff.md  (`case`, 6 assertions)

### content_page

```
---
title: "Ryburn v. Huff"
type: case
citation: "565 U.S. 469 (2012)"
parallel_cite: "132 S. Ct. 987; 181 L. Ed. 2d 966"
neutral_cite: 2012 U.S. LEXIS 910
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2012
date_decided: 2012-01-23
docket: 11-208
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2012-01-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Ryburn v. Huff
  varies_by_point: false
  scope_note: "Per curiam. Good law; consistent with the emergency-aid line and the qualified-immunity 'reasonable officer on the scene' standard."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/622303/ryburn-v-huff/"
  cluster_id: 622303
  opinion_id: 622303
  identity_checked: true
homes:
  - page: "[[Emergency Aid]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Qualified Immunity]]"
    role: "Related (cross-doctrine)"
related: ["[[Brigham City v. Stuart]]", "[[Michigan v. Fisher]]", "[[Graham v. Connor]]", "[[Caniglia v. Strom]]"]
aliases: []
tags: ["case", "fourth-amendment", "emergency-aid", "exigent-circumstances", "qualified-immunity", "section-1983"]
holding: "Officers may make a warrantless entry into a home when they have an objectively reasonable basis to fear that violence is imminent; viewed from the perspective of a reasonable officer making a split-second on-scene judgment (not with hindsight), such an entry is reasonable, and the officers here were entitled to qualified immunity."
lake:
  record_id: Ryburn v. Huff
  status: verified
  projected_at: 2026-07-06
---

# Ryburn v. Huff

*565 U.S. 469 (2012)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police investigated a report that a high-school student, Vincent Huff, was rumored to have threatened to "shoot up" his school. At the Huff home, no one answered the door or the family's phones. The mother eventually stepped outside; when an officer asked whether there were any guns in the house, she immediately turned and ran back inside. Concerned for their safety and that of others, officers entered behind her. The Huffs sued under § 1983 for an unlawful warrantless entry. The District Court found the entry reasonable (and the officers protected by [[Qualified Immunity|qualified immunity]]); a divided Ninth Circuit panel reversed, holding the officers were not entitled to [[Qualified Immunity|qualified immunity]].

## Issue
Whether officers who reasonably believe, on the scene, that violence is imminent may make a warrantless entry into a home, and whether the officers here were entitled to [[Qualified Immunity|qualified immunity]].

## Rule
Yes. "A reasonable police officer could read these decisions to mean that the Fourth Amendment permits an officer to enter a residence if the officer has a reasonable basis for concluding that there is an imminent threat of violence." — 565 U.S. at 476. ^pin-476

Reasonableness is judged from the officer's on-scene perspective, not in hindsight (quoting *Graham v. Connor*), and: "In sum, reasonable police officers in petitioners' position could have come to the conclusion that the Fourth Amendment permitted them to enter the Huff residence if there was an objectively reasonable basis for fearing that violence was imminent. And a reasonable officer could have come to such a conclusion based on the facts as found by the District Court." — *Id.* at 477. ^pin-477

## Application
The Ninth Circuit erred by recasting the District Court's findings, by treating lawful conduct (the mother's refusal to answer and her sudden flight inside) as no cause for alarm, by analyzing each event in isolation rather than as a whole ("a combination of events each of which is mundane when viewed in isolation may paint an alarming picture"), and by second-guessing the officers' on-scene judgment with hindsight. Judged from the perspective of a reasonable officer facing a rapidly unfolding situation that culminated in the mother running into the house after refusing to answer about guns, the belief that entry was necessary to avoid injury was "eminently reasonable."

## Conclusion
Reversed and [[Reading and Citing Cases#on-remand|remanded]] for entry of judgment for the officers (per curiam). A warrantless entry on an objectively reasonable belief of imminent violence is reasonable, and the officers were entitled to [[Qualified Immunity|qualified immunity]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- No negative treatment. *Ryburn* applies the emergency-aid/[[Exigent Circumstances and Hot Pursuit|exigency]] line of [[Brigham City v. Stuart]] and [[Michigan v. Fisher]] and the qualified-immunity "reasonable officer on the scene" standard of [[Graham v. Connor]]; it is consistent with the later home-entry caretaking limit of [[Caniglia v. Strom]] (welfare entries must route through [[Emergency Aid|emergency aid]] / [[Exigent Circumstances and Hot Pursuit|exigency]]).

## Appears on
- [[Emergency Aid]] — *Key — Progeny / Refinement*
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *Ryburn v. Huff*, 565 U.S. 469 (2012) — https://www.courtlistener.com/opinion/622303/ryburn-v-huff/ — pinpoints: 476, 477.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7df673055c32f01e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "565 U.S. 469 (2012)", "court": "U.S. Supreme Court", "neutral_cite": "2012 U.S. LEXIS 910", "official_citation_present": true, "parallel_cite": "132 S. Ct. 987; 181 L. Ed. 2d 966", "title": "Ryburn v. Huff", "year": "2012"}}
{"assertion_id": "6cff88df50ad8b73", "dimension": "support", "kind": "home_role", "locator": {"home": "Emergency Aid"}, "payload": {"home": "Emergency Aid", "role": "Key — Progeny / Refinement", "title": "Ryburn v. Huff"}}
{"assertion_id": "8aee4966b13093c6", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Related (cross-doctrine)", "title": "Ryburn v. Huff"}}
{"assertion_id": "9a50c02a9d3bd572", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Officers may make a warrantless entry into a home when they have an objectively reasonable basis to fear that violence is imminent; viewed from the perspective of a reasonable officer making a split-second on-scene judgment (not with hindsight), such an entry is reasonable, and the officers here were entitled to qualified immunity.", "title": "Ryburn v. Huff"}}
{"assertion_id": "3776a8597f8698cb", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2012-01-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Ryburn v. Huff", "field_i_validity": "good_law", "scope_note": "Per curiam. Good law; consistent with the emergency-aid line and the qualified-immunity 'reasonable officer on the scene' standard.", "title": "Ryburn v. Huff", "varies_by_point": "false"}}
{"assertion_id": "5ee0f23371fa6e6f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Ryburn v. Huff"}}
```

### lake record — Ryburn v. Huff

```json
{
  "schema_version": "s2.v1",
  "record_id": "Ryburn v. Huff",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Ryburn v. Huff",
    "case_name_short": "Ryburn",
    "case_name_full": "RYBURN Et Al. v. HUFF Et Al.",
    "input_case_name": "Ryburn v. Huff",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2012-01-23",
    "year": 2012,
    "docket": "11-208",
    "cluster_id": 622303,
    "lead_opinion_id": 622303,
    "sibling_ids": [
      622303
    ],
    "absolute_url": "/opinion/622303/ryburn-v-huff/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 621715,
        "score": 20,
        "case_name": "Ryburn v. Huff"
      },
      {
        "cluster_id": 621349,
        "score": 20,
        "case_name": "Ryburn v. Huff"
      },
      {
        "cluster_id": 621292,
        "score": 20,
        "case_name": "Ryburn v. Huff"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "565 U.S. 469",
      "volume": "565",
      "reporter": "U.S.",
      "page": "469",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "132 S. Ct. 987",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "987",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "181 L. Ed. 2d 966",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "966",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2012 U.S. LEXIS 910",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "910",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "132 S. Ct. 987",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "987",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "181 L. Ed. 2d 966",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "966",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "565 U.S. 469",
        "volume": "565",
        "reporter": "U.S.",
        "page": "469",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 U.S. LEXIS 910",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "910",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "565 U.S. 469",
    "official_selection": {
      "court_class": "scotus",
      "selected": "565 U.S. 469",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-476",
      "page": null,
      "quote": "his school. At the Huff home, no one answered the door or the family's phones. The mother eventually stepped outside; when an officer asked whether there were any guns in the house, she immediately turned and ran back inside. Concerned for their safety and that of others, officers entered behind her. The Huffs sued under \u00a7 1983 for an unlawful warrantless entry. The District Court found the entry reasonable (and the officers protected by qualified immunity); a divided Ninth Circuit panel reversed, holding the officers were not entitled to qualified immunity. ## Issue Whether officers who reasonably believe, on the scene, that violence is imminent may make a warrantless entry into a home, and whether the officers here were entitled to qualified immunity. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-477",
      "page": null,
      "quote": "In sum, reasonable police officers in petitioners' position could have come to the conclusion that the Fourth Amendment permitted them to enter the Huff residence if there was an objectively reasonable basis for fearing that violence was imminent. And a reasonable officer could have come to such a conclusion based on the facts as found by the District Court.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2012-01-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Ryburn v. Huff",
    "varies_by_point": false,
    "scope_note": "Per curiam. Good law; consistent with the emergency-aid line and the qualified-immunity 'reasonable officer on the scene' standard.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Cole v. State",
          "cluster_id": 5446855,
          "cite": [
            "490 S.W.3d 918",
            "2016 Tex. Crim. App. LEXIS 84",
            "2016 WL 3018203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Caple",
          "cluster_id": 2820305,
          "cite": [
            "121 A.3d 511",
            "2015 WL 4497915"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Parker Chad Ross v. Commonwealth of Virginia",
          "cluster_id": 1061425,
          "cite": [
            "61 Va. App. 752",
            "739 S.E.2d 910",
            "2013 WL 1564533",
            "2013 Va. App. LEXIS 115"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Storey v. Garcia",
          "cluster_id": 3062104,
          "cite": [
            "696 F.3d 987",
            "2012 WL 4478784",
            "2012 U.S. App. LEXIS 20471"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane1_negative"
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
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
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
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gonzalez Ex Rel. Gonzalez v. City of Anaheim",
          "cluster_id": 2658912,
          "cite": [
            "747 F.3d 789",
            "2014 WL 1274551",
            "2014 U.S. App. LEXIS 5895"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "E.W. v. Rosemary Dolgos",
          "cluster_id": 4467174,
          "cite": [
            "884 F.3d 172"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
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
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
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
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Martha Romero v. City of Grapevine, Texas",
          "cluster_id": 4488919,
          "cite": [
            "888 F.3d 170"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
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
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jim Maxwell v. County of San Diego",
          "cluster_id": 820536,
          "cite": [
            "708 F.3d 1075",
            "2013 WL 542756"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salvatore Palma, Jr. v. Matthew Johns",
          "cluster_id": 6445970,
          "cite": [
            "27 F.4th 419"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Than Orn v. City of Tacoma",
          "cluster_id": 4723681,
          "cite": [
            "949 F.3d 1167"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Batyukova v. Doege",
          "cluster_id": 4875692,
          "cite": [
            "994 F.3d 717"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roque v. Harvel",
          "cluster_id": 4870008,
          "cite": [
            "993 F.3d 325"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Dunn",
          "cluster_id": 2690881,
          "cite": [
            "2012 Ohio 1008",
            "131 Ohio St. 3d 325"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ryan Bonivert v. City of Clarkston",
          "cluster_id": 4471017,
          "cite": [
            "883 F.3d 865"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sandoval v. Las Vegas Metropolitan Police Department",
          "cluster_id": 2681571,
          "cite": [
            "756 F.3d 1154",
            "2014 WL 2936254",
            "2014 U.S. App. LEXIS 12395"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Eric Mueller v. City of Boise",
          "cluster_id": 808184,
          "cite": [
            "700 F.3d 1180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sonia Garcia v. Wesley Blevins",
          "cluster_id": 4750052,
          "cite": [
            "957 F.3d 596"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ellison Ex Rel. Estate of Ellison v. Lesher",
          "cluster_id": 2824534,
          "cite": [
            "796 F.3d 910",
            "2015 U.S. App. LEXIS 13714",
            "2015 WL 4645667"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Weems, Daniel James",
          "cluster_id": 3207097,
          "cite": [
            "493 S.W.3d 574",
            "2016 WL 2997333",
            "2016 Tex. Crim. App. LEXIS 85"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alan Hoover v. Timothy Walsh",
          "cluster_id": 802155,
          "cite": [
            "682 F.3d 481",
            "2012 WL 2122485",
            "2012 U.S. App. LEXIS 11929"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Azucena Zamorano Aleman v. City of Charlotte",
          "cluster_id": 9421054,
          "cite": [
            "80 F.4th 264"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ronald Mitchell v. Justin Schlabach",
          "cluster_id": 4409996,
          "cite": [
            "864 F.3d 416"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ryburn v. Huff:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(622303) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 81,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 81,
        "triage_read": 4,
        "triage_snippet_classified": 77
      },
      "lane2_top_cited": {
        "query": "cites:(622303)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNCZzPTQ4MDA1OTgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28622303%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(622303)",
        "reviewed": 15,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 15,
        "triage_read": 0,
        "triage_snippet_classified": 15
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(622303)",
    "indexed_citing_opinions": 101,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 622303,
        "count": 101,
        "count_source": "search"
      }
    ],
    "citation_count": 193,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/ryburn-v-huff.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcyMjEzNjQmcz00ODc1NjkyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28622303%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 622303,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622303,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622303,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622303,
        "cited_id": 145669,
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
    "date_created": "2026-07-05T17:52:58Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:53:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:19:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T18:21:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:19:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Ryburn v. Huff

```
                 Cite as: 565 U. S. ____ (2012)           1

                           Per Curiam

SUPREME COURT OF THE UNITED STATES
  DARIN RYBURN, ET AL. v. GEORGE R. HUFF, ET AL.
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE NINTH CIRCUIT


             No. 11–208.   Decided January 23, 2012

                                                   


  PER CURIAM.
  Petitioners Darin Ryburn and Edmundo Zepeda, along
with two other officers from the Burbank Police Depart-
ment, responded to a call from Bellarmine-Jefferson High
School in Burbank, California. When the officers arrived
at the school, the principal informed them that a stu-
dent, Vincent Huff, was rumored to have written a letter
threatening to “shoot up” the school. App. to Pet. for Cert.
2. The principal reported that many parents, after hear-
ing the rumor, had decided to keep their children at home.
Ibid. The principal expressed concern for the safety of her
students and requested that the officers investigate the
threat. Id., at 42, 54–55.
  In the course of conducting interviews with the principal
and two of Vincent’s classmates, the officers learned that
Vincent had been absent from school for two days and
that he was frequently subjected to bullying. Id., at 2. The
officers additionally learned that one of Vincent’s class-
mates believed that Vincent was capable of carrying out
the alleged threat. Id., at 44. The officers found Vincent’s
absences from school and his history of being subjected to
bullying as cause for concern. The officers had received
training on targeted school violence and were aware that
these characteristics are common among perpetrators of
school shootings. Id., at 56–58, 63.
  The officers decided to continue the investigation by
interviewing Vincent. When the officers arrived at Vin-
cent’s house, Officer Zepeda knocked on the door and
announced several times that the officers were with the
2                     RYBURN v. HUFF

                         Per Curiam

Burbank Police Department. No one answered the door or
otherwise responded to Officer Zepeda’s knocks. Sergeant
Ryburn then called the home telephone. The officers could
hear the phone ringing inside the house, but no one an-
swered. Id., at 2.
   Sergeant Ryburn next tried calling the cell phone of
Vincent’s mother, Mrs. Huff. When Mrs. Huff answered
the phone, Sergeant Ryburn identified himself and in-
quired about her location. Mrs. Huff informed Sergeant
Ryburn that she was inside the house. Sergeant Ryburn
then inquired about Vincent’s location, and Mrs. Huff
informed him that Vincent was inside with her. Sergeant
Ryburn told Mrs. Huff that he and the other officers were
outside and requested to speak with her, but Mrs. Huff
hung up the phone. Id., at 2–3.
   One or two minutes later, Mrs. Huff and Vincent walked
out of the house and stood on the front steps. Officer
Zepeda advised Vincent that he and the other officers were
there to discuss the threats. Vincent, apparently aware of
the rumor that was circulating at his school, responded,
“I can’t believe you’re here for that.” Id., at 3. Sergeant
Ryburn asked Mrs. Huff if they could continue the discus-
sion inside the house, but she refused. Ibid. In Sergeant
Ryburn’s experience as a juvenile bureau sergeant, it was
“extremely unusual” for a parent to decline an officer’s
request to interview a juvenile inside. Id., at 3, 73–74.
Sergeant Ryburn also found it odd that Mrs. Huff never
asked the officers the reason for their visit. Id., at 73–74.
   After Mrs. Huff declined Sergeant Ryburn’s request to
continue the discussion inside, Sergeant Ryburn asked her
if there were any guns in the house. Mrs. Huff responded
by “immediately turn[ing] around and r[unning] into the
house.” Id., at 3. Sergeant Ryburn, who was “scared
because [he] didn’t know what was in that house” and had
“seen too many officers killed,” entered the house behind
her. Id., at 75. Vincent entered the house behind Ser-
                 Cite as: 565 U. S. ____ (2012)            3

                          Per Curiam

geant Ryburn, and Officer Zepeda entered after Vincent.
Officer Zepeda was concerned about “officer safety” and
did not want Sergeant Ryburn to enter the house alone.
Id., at 3. The two remaining officers, who had been stand-
ing out of earshot while Sergeant Ryburn and Officer
Zepeda talked to Vincent and Mrs. Huff, entered the house
last, on the assumption that Mrs. Huff had given Sergeant
Ryburn and Officer Zepeda permission to enter. Id., at
3–4.
   Upon entering the house, the officers remained in the
living room with Mrs. Huff and Vincent. Eventually,
Vincent’s father entered the room and challenged the
officers’ authority to be there. The officers remained in-
side the house for a total of 5 to 10 minutes. During that
time, the officers talked to Mr. Huff and Vincent. They
did not conduct any search of Mr. Huff, Mrs. Huff, or
Vincent, or any of their property. The officers ultimately
concluded that the rumor about Vincent was false, and
they reported their conclusion to the school. Id., at 4.
   The Huffs brought this action against the officers under
Rev. Stat. §1979, 42 U. S. C. §1983. The complaint alleges
that the officers violated the Huffs’ Fourth Amendment
rights by entering their home without a warrant. Follow-
ing a 2-day bench trial, the District Court entered judg-
ment in favor of the officers. The District Court resolved
conflicting testimony regarding Mrs. Huff’s response to
Sergeant Ryburn’s inquiry about guns by finding that Mrs.
Huff “immediately turned around and ran into the house.”
App. to Pet. for Cert. 3. The District Court concluded that
the officers were entitled to qualified immunity because
Mrs. Huff’s odd behavior, combined with the information
the officers gathered at the school, could have led reason-
able officers to believe “that there could be weapons inside
the house, and that family members or the officers them-
selves were in danger.” Id., at 6. The District Court noted
that “[w]ithin a very short period of time, the officers were
4                     RYBURN v. HUFF

                         Per Curiam

confronted with facts and circumstances giving rise to
grave concern about the nature of the danger they were
confronting.” Id., at 6–7. With respect to this kind of
“rapidly evolving incident,” the District Court explained,
courts should be especially reluctant “to fault the police for
not obtaining a warrant.” Id., at 7.
   A divided panel of the Ninth Circuit affirmed the Dis-
trict Court as to the two officers who entered the house on
the assumption that Mrs. Huff had consented, but re-
versed as to petitioners. The majority upheld the District
Court’s findings of fact, but disagreed with the District
Court’s conclusion that petitioners were entitled to quali-
fied immunity. The majority acknowledged that police
officers are allowed to enter a home without a warrant if
they reasonably believe that immediate entry is necessary
to protect themselves or others from serious harm, even if
the officers lack probable cause to believe that a crime has
been or is about to be committed. Id., at 24. But the
majority determined that, in this case, “any belief that
the officers or other family members were in serious, im-
minent harm would have been objectively unreasonable”
given that “[Mrs. Huff] merely asserted her right to end
her conversation with the officers and returned to her
home.” Id., at 25.
   Judge Rawlinson dissented. She explained that “the
discrete incident that precipitated the entry in this case
was Mrs. Huff’s response to the question regarding wheth-
er there were guns in the house.” Id., at 31. She faulted
the majority for “recit[ing] a sanitized account of this
event” that differed markedly from the District Court’s
findings of fact, which the majority had conceded must be
credited. Judge Rawlinson looked to “cases that specifi-
cally address the scenario where officer safety concerns
prompted the entry” and concluded that, under the ra-
tionale articulated in those cases, “a police officer could
have reasonably believed that he was justified in making a
                 Cite as: 565 U. S. ____ (2012)            5

                          Per Curiam

warrantless entry to ensure that no one inside the house
had a gun after Mrs. Huff ran into the house without
answering the question of whether anyone had a weapon.”
Id., at 31, 33, 37.
   Judge Rawlinson’s analysis of the qualified immunity
issue was correct. No decision of this Court has found a
Fourth Amendment violation on facts even roughly com-
parable to those present in this case. On the contrary,
some of our opinions may be read as pointing in the oppo-
site direction.
   In Brigham City v. Stuart, 547 U. S. 398, 400 (2006), we
held that officers may enter a residence without a warrant
when they have “an objectively reasonable basis for believ-
ing that an occupant is . . . imminently threatened with
[serious injury].” We explained that “ ‘[t]he need to protect
or preserve life or avoid serious injury is justification
for what would be otherwise illegal absent an exigency or
emergency.’ ” Id., at 403 (quoting Mincey v. Arizona, 437
U. S. 385, 392 (1978)). In addition, in Georgia v. Ran-
dolph, 547 U. S. 103, 118 (2006), the Court stated that “it
would be silly to suggest that the police would commit a
tort by entering [a residence] . . . to determine whether
violence . . . is about to (or soon will) occur.”
   A reasonable police officer could read these decisions to
mean that the Fourth Amendment permits an officer to en-
ter a residence if the officer has a reasonable basis for
concluding that there is an imminent threat of violence.
In this case, the District Court concluded that petitioners
had such an objectively reasonable basis for reaching such
a conclusion. The District Court wrote:
    “[T]he officers testified that a number of factors led
    them to be concerned for their own safety and for the
    safety of other persons in the residence: the unusual
    behavior of the parents in not answering the door or
    the telephone; the fact that Mrs. Huff did not inquire
6                    RYBURN v. HUFF

                        Per Curiam

    about the reason for their visit or express concern that
    they were investigating her son; the fact that she
    hung up the telephone on the officer; the fact that
    she refused to tell them whether there were guns in
    the house; and finally, the fact that she ran back into
    the house while being questioned. That behavior,
    combined with the information obtained at the
    school—that Vincent was a student who was a victim
    of bullying, who had been absent from school for two
    days, and who had threatened to ‘shoot up’ the
    school—led the officers to believe that there could be
    weapons inside the house, and that family members
    or the officers themselves were in danger.” App. to
    Pet. for Cert. 6.
This belief, the District Court held, was “objectively rea-
sonable,” particularly since the situation was “rapidly
evolving” and the officers had to make quick decisions.
Id., at 6–7.
   The panel majority—far removed from the scene and
with the opportunity to dissect the elements of the situa-
tion—confidently concluded that the officers really had no
reason to fear for their safety or that of anyone else. As
the panel majority saw things, it was irrelevant that the
Huffs did not respond when the officers knocked on the
door and announced their presence and when they called
the home phone because the Huffs had no legal obligation
to respond to a knock on the door or to answer the phone.
The majority attributed no significance to the fact that,
when the officers finally reached Mrs. Huff on her cell
phone, she abruptly hung up in the middle of their conver-
sation. And, according to the majority, the officers should
not have been concerned by Mrs. Huff’s reaction when
they asked her if there were any guns in the house be-
cause Mrs. Huff “merely asserted her right to end her
conversation with the officers and returned to her home.”
                 Cite as: 565 U. S. ____ (2012)            7

                          Per Curiam

Id., at 25.
   Confronted with the facts found by the District Court,
reasonable officers in the position of petitioners could have
come to the conclusion that there was an imminent threat
to their safety and to the safety of others. The Ninth
Circuit’s contrary conclusion was flawed for numerous
reasons.
   First, although the panel majority purported to accept
the findings of the District Court, it changed those find-
ings in several key respects. As Judge Rawlinson correctly
observed, “the discrete incident that precipitated the entry
in this case was Mrs. Huff’s response to the question
regarding whether there were guns in the house.” Id., at
31. The District Court’s finding that Mrs. Huff “immedi-
ately turned around and ran into the house” implicitly
rejected Mrs. Huff’s contrary testimony that she walked
into the house after telling the officers that she was going
to get her husband. Id., at 3. The panel majority upheld
the District Court’s findings of fact and acknowledged that
it could not reverse the District Court simply because it
“may have weighed the testimony of the witnesses and
other evidence in another manner.” Id., at 15. But the
panel majority’s determination that petitioners were not
entitled to qualified immunity rested on an account of
the facts that differed markedly from the District Court’s
finding. According to the panel majority, Mrs. Huff “mere-
ly asserted her right to end her conversation with the
officers and returned to her home” after telling the officers
“that she would go get her husband.” Id., at 12, 25.
   Second, the panel majority appears to have taken the
view that conduct cannot be regarded as a matter of con-
cern so long as it is lawful. Accordingly, the panel ma-
jority concluded that Mrs. Huff’s response to the question
whether there were any guns in the house (immediately
turning around and running inside) was not a reason for
alarm because she was under no legal obligation to con-
8                     RYBURN v. HUFF

                         Per Curiam

tinue her conversation with the police. It should go with-
out saying, however, that there are many circumstances in
which lawful conduct may portend imminent violence.
   Third, the panel majority’s method of analyzing the
string of events that unfolded at the Huff residence was
entirely unrealistic. The majority looked at each separate
event in isolation and concluded that each, in itself, did
not give cause for concern. But it is a matter of common
sense that a combination of events each of which is mun-
dane when viewed in isolation may paint an alarming
picture.
   Fourth, the panel majority did not heed the District
Court’s wise admonition that judges should be cautious
about second-guessing a police officer’s assessment, made
on the scene, of the danger presented by a particular
situation. With the benefit of hindsight and calm deliber-
ation, the panel majority concluded that it was unreason-
able for petitioners to fear that violence was imminent.
But we have instructed that reasonableness “must be
judged from the perspective of a reasonable officer on the
scene, rather than with the 20/20 vision of hindsight” and
that “[t]he calculus of reasonableness must embody allow-
ance for the fact that police officers are often forced to
make split-second judgments—in circumstances that are
tense, uncertain, and rapidly evolving.” Graham v. Con-
nor, 490 U. S. 386, 396–397 (1989). Judged from the
proper perspective of a reasonable officer forced to make a
split-second decision in response to a rapidly unfolding
chain of events that culminated with Mrs. Huff turning
and running into the house after refusing to answer a
question about guns, petitioners’ belief that entry was
necessary to avoid injury to themselves or others was
eminently reasonable.
   In sum, reasonable police officers in petitioners’ position
could have come to the conclusion that the Fourth
Amendment permitted them to enter the Huff residence if
                 Cite as: 565 U. S. ____ (2012)                  9

                          Per Curiam

there was an objectively reasonable basis for fearing that
violence was imminent. And a reasonable officer could
have come to such a conclusion based on the facts as found
by the District Court.
  The petition for certiorari is granted, the judgment of
the Ninth Circuit is reversed, and the case is remanded for
the entry of judgment in favor of petitioners.

                                                  It is so ordered.

```

---

## GROUP: content/cases/Sabbath v. United States.md  (`case`, 6 assertions)

### content_page

```
---
title: "Sabbath v. United States"
type: case
citation: "391 U.S. 585 (1968)"
parallel_cite: "88 S. Ct. 1755; 20 L. Ed. 2d 828"
neutral_cite: 1968 U.S. LEXIS 1472
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1968
date_decided: 1968-06-03
docket: 898
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1968-06-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Sabbath v. United States
  varies_by_point: false
  scope_note: "The definition of an unannounced 'breaking' — including opening a closed but unlocked door — remains good law. The suppression remedy Sabbath applied for knock-and-announce violations was later sharply limited (for Fourth Amendment violations) by Hudson v. Michigan (2006), which does not disturb Sabbath's substantive holding."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107718/sabbath-v-united-states/"
  cluster_id: 107718
  opinion_id: 107718
  identity_checked: true
homes:
  - page: "[[Knock-and-Announce]]"
    role: "Progeny"
  - page: "[[Arrest in the Home]]"
    role: "Related (cross-doctrine)"
related: ["[[Wilson v. Arkansas]]", "[[Richards v. Wisconsin]]", "[[Hudson v. Michigan]]", "[[United States v. Ramirez]]"]
aliases: []
tags: ["case", "fourth-amendment", "knock-and-announce", "warrant-requirement", "arrest-in-home"]
holding: "An unannounced 'breaking' for knock-and-announce purposes is not limited to forcible entry; opening a closed but unlocked door without first announcing authority and purpose is an unannounced intrusion governed by the announcement requirement of 18 U.S.C. § 3109."
lake:
  record_id: Sabbath v. United States
  status: verified
  projected_at: 2026-07-09
---

# Sabbath v. United States

*391 U.S. 585 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After customs agents arrested William Jones at the border with cocaine, Jones implicated "Johnny" (Sabbath) and agreed to a controlled delivery. Wired for sound, Jones entered Sabbath's apartment while agents waited outside. A few minutes later the agents went to the door, knocked, waited only a few seconds, and — receiving no response — opened the closed but unlocked door and entered with guns drawn, arresting Sabbath and finding cocaine under a cushion. The Ninth Circuit held that opening an unlocked door was not a "break[ing]" under 18 U.S.C. § 3109.

## Issue
Does opening a closed but unlocked door to enter and arrest, without first announcing authority and purpose, constitute a "breaking" subject to the announcement requirement of § 3109 (codifying the common-law [[Knock-and-Announce|knock-and-announce]] rule)?

## Rule
Yes. "An unannounced intrusion into a dwelling — what § 3109 basically proscribes — is no less an unannounced intrusion whether officers break down a door, force open a chain lock on a partially open door, open a locked door by use of a passkey, or, as here, open a closed but unlocked door." — 391 U.S. at 590. ^pin-590

The statute's protections must be "governed by something more than the fortuitous circumstance of an unlocked door." — [*Id.*](https://www.courtlistener.com/opinion/107718/sabbath-v-united-states/#:~:text=governed%20by%20something%20more%20than) (quoting *Keiningham v. United States*). ^pin-590b

The Court accordingly "h[e]ld that the method of entry vitiated the arrest and therefore that evidence seized in the subsequent search incident thereto should not have been admitted." — *Id.* at 585–86. ^pin-585

## Application
The agents knocked, waited only seconds, and then opened the closed but unlocked door without announcing their identity and purpose, entering with weapons drawn. That was an unannounced intrusion within § 3109 — the manner of entry, not the lock, controls. No exception to the announcement rule (such as a demonstrated danger to the informant or officers) was established on this record. Because the entry violated the announcement requirement, the arrest was unlawful and the cocaine found in the search incident to it was inadmissible.

## Conclusion
The entry violated § 3109; the evidence should have been suppressed, and the judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Sabbath*'s definition of an unannounced "breaking" — reaching the opening of a closed but unlocked door — remains sound and feeds the constitutional [[Knock-and-Announce|knock-and-announce]] rule recognized in [[Wilson v. Arkansas]] and refined in [[Richards v. Wisconsin]]. The suppression remedy *Sabbath* applied for such violations was later curtailed for Fourth Amendment [[Knock-and-Announce|knock-and-announce]] violations by [[Hudson v. Michigan]] (2006), which does not disturb *Sabbath*'s substantive holding about what counts as an unannounced entry.

## Appears on
- [[Knock-and-Announce]] — *Progeny*
- [[Arrest in the Home]] — *Related (cross-doctrine)*

## Sources
- *Sabbath v. United States*, 391 U.S. 585 (1968) — https://www.courtlistener.com/opinion/107718/sabbath-v-united-states/ — pinpoints: 585–586, 590.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "73867d5f706164bd", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "391 U.S. 585 (1968)", "court": "U.S. Supreme Court", "neutral_cite": "1968 U.S. LEXIS 1472", "official_citation_present": true, "parallel_cite": "88 S. Ct. 1755; 20 L. Ed. 2d 828", "title": "Sabbath v. United States", "year": "1968"}}
{"assertion_id": "4e26a439a901c8f3", "dimension": "support", "kind": "home_role", "locator": {"home": "Knock-and-Announce"}, "payload": {"home": "Knock-and-Announce", "role": "Progeny", "title": "Sabbath v. United States"}}
{"assertion_id": "5b0f2b92202ad9c4", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Related (cross-doctrine)", "title": "Sabbath v. United States"}}
{"assertion_id": "5cb73083df502e8b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An unannounced 'breaking' for knock-and-announce purposes is not limited to forcible entry; opening a closed but unlocked door without first announcing authority and purpose is an unannounced intrusion governed by the announcement requirement of 18 U.S.C. § 3109.", "title": "Sabbath v. United States"}}
{"assertion_id": "5e947115d7794bd6", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Sabbath v. United States"}}
{"assertion_id": "be8fa794a0471c71", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1968-06-03", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Sabbath v. United States", "field_i_validity": "good_law", "scope_note": "The definition of an unannounced 'breaking' — including opening a closed but unlocked door — remains good law. The suppression remedy Sabbath applied for knock-and-announce violations was later sharply limited (for Fourth Amendment violations) by Hudson v. Michigan (2006), which does not disturb Sabbath's substantive holding.", "title": "Sabbath v. United States", "varies_by_point": "false"}}
```

### lake record — Sabbath v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Sabbath v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Sabbath v. United States",
    "case_name_short": "Sabbath",
    "case_name_full": "Sabbath v. United States",
    "input_case_name": "Sabbath v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-06-03",
    "year": 1968,
    "docket": "898",
    "cluster_id": 107718,
    "lead_opinion_id": 107718,
    "sibling_ids": [
      107718
    ],
    "absolute_url": "/opinion/107718/sabbath-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "391 U.S. 585",
      "volume": "391",
      "reporter": "U.S.",
      "page": "585",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 1755",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1755",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 828",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "828",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 1472",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1472",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "391 U.S. 585",
        "volume": "391",
        "reporter": "U.S.",
        "page": "585",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 1755",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1755",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 828",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "828",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 1472",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1472",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "391 U.S. 585",
    "official_selection": {
      "court_class": "scotus",
      "selected": "391 U.S. 585",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-590",
      "page": null,
      "quote": "subject to the announcement requirement of \u00a7 3109 (codifying the common-law knock-and-announce rule)? ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-590b",
      "page": null,
      "quote": "governed by something more than the fortuitous circumstance of an unlocked door.",
      "star_marker": "590",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 8809,
      "fragment": "#:~:text=governed%20by%20something%20more%20than",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-585",
      "page": null,
      "quote": "h[e]ld that the method of entry vitiated the arrest and therefore that evidence seized in the subsequent search incident thereto should not have been admitted.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1968-06-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Sabbath v. United States",
    "varies_by_point": false,
    "scope_note": "The definition of an unannounced 'breaking' \u2014 including opening a closed but unlocked door \u2014 remains good law. The suppression remedy Sabbath applied for knock-and-announce violations was later sharply limited (for Fourth Amendment violations) by Hudson v. Michigan (2006), which does not disturb Sabbath's substantive holding.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Southerland, Vince",
          "cluster_id": 186774,
          "cite": [
            "373 U.S. App. D.C. 305",
            "466 F.3d 1083",
            "2006 U.S. App. LEXIS 26978",
            "2006 WL 3069122"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Price, Gilbert Colman v. State",
          "cluster_id": 2927694,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Price v. State",
          "cluster_id": 1891038,
          "cite": [
            "93 S.W.3d 358",
            "2002 Tex. App. LEXIS 8436",
            "2002 WL 31043513"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cantu",
          "cluster_id": 22035,
          "cite": [
            "230 F.3d 148",
            "2000 WL 1481157"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Valentine",
          "cluster_id": 3945655,
          "cite": [
            "598 N.E.2d 82",
            "74 Ohio App. 3d 110",
            "1991 Ohio App. LEXIS 2465"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Oscar Arboleda",
          "cluster_id": 383729,
          "cite": [
            "633 F.2d 985",
            "1980 U.S. App. LEXIS 13254"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. German Fidel Cueto",
          "cluster_id": 372938,
          "cite": [
            "611 F.2d 1056",
            "1980 U.S. App. LEXIS 20484",
            "5 Fed. R. Serv. 1081"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cadena",
          "cluster_id": 8919342,
          "cite": [
            "585 F.2d 1252",
            "1979 A.M.C. 1934"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hoyt Albert Gaultney and Francis Gilmere",
          "cluster_id": 358808,
          "cite": [
            "581 F.2d 1137",
            "1978 U.S. App. LEXIS 8522"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nancy Reed and Morris Goldsmith, A/K/A \"Marlowe,\"",
          "cluster_id": 354014,
          "cite": [
            "572 F.2d 412",
            "3 Fed. R. Serv. 155",
            "1978 U.S. App. LEXIS 11727"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane1_negative"
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
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
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
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Winston Bryant McConney",
          "cluster_id": 431931,
          "cite": [
            "728 F.2d 1195",
            "1984 U.S. App. LEXIS 25576"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
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
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
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
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
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
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Banks",
          "cluster_id": 131146,
          "cite": [
            "157 L. Ed. 2d 343",
            "124 S. Ct. 521",
            "540 U.S. 31",
            "2003 U.S. LEXIS 8966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradley",
          "cluster_id": 1123090,
          "cite": [
            "460 P.2d 129",
            "1 Cal. 3d 80",
            "81 Cal. Rptr. 457",
            "1969 Cal. LEXIS 194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sonya Evette Singleton",
          "cluster_id": 754623,
          "cite": [
            "144 F.3d 1343",
            "1998 U.S. App. LEXIS 15451",
            "1998 WL 350507"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Daniel J. Leichtnam",
          "cluster_id": 571305,
          "cite": [
            "948 F.2d 370",
            "1991 U.S. App. LEXIS 27434",
            "1991 WL 242204"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Berkowitz, Paul D'alessandro, Kevin Van Coughnett, Bisan Vafaie, and Wendall Howell",
          "cluster_id": 396333,
          "cite": [
            "662 F.2d 1127",
            "9 Fed. R. Serv. 864",
            "1981 U.S. App. LEXIS 15433"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
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
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
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
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Patrick Wayde Mealy and Lance B. Spotts",
          "cluster_id": 508775,
          "cite": [
            "851 F.2d 890",
            "26 Fed. R. Serv. 305",
            "1988 U.S. App. LEXIS 9479"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Cundriff",
          "cluster_id": 2042454,
          "cite": [
            "415 N.E.2d 172",
            "382 Mass. 137",
            "17 A.L.R. 4th 287",
            "1980 Mass. LEXIS 1398"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Edward Mapp, A/K/A Sonny Woods",
          "cluster_id": 310049,
          "cite": [
            "476 F.2d 67",
            "1973 U.S. App. LEXIS 10838"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Francisco Bustamante-Gamez, United States of America v. Abelardo Garcia-Ramirez",
          "cluster_id": 315322,
          "cite": [
            "488 F.2d 4",
            "1973 U.S. App. LEXIS 7396"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Finch",
          "cluster_id": 610951,
          "cite": [
            "998 F.2d 349",
            "1993 U.S. App. LEXIS 16174",
            "1993 WL 239386"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Larry J. Leaf, Individually and as Personal Representative of the Estate of John P. Leaf, Deceased, Martha A. Leaf, John P. Leaf v. Ronald Shelnutt",
          "cluster_id": 789551,
          "cite": [
            "400 F.3d 1070",
            "2005 U.S. App. LEXIS 4513",
            "2005 WL 628217"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John C. Mueller",
          "cluster_id": 540816,
          "cite": [
            "902 F.2d 336",
            "1990 U.S. App. LEXIS 8344",
            "1990 WL 66485"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Hall",
          "cluster_id": 2155249,
          "cite": [
            "323 N.E.2d 319",
            "366 Mass. 790",
            "1975 Mass. LEXIS 1141"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Thompson",
          "cluster_id": 414469,
          "cite": [
            "700 F.2d 944",
            "1983 U.S. App. LEXIS 29939"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Stevens",
          "cluster_id": 1693561,
          "cite": [
            "597 N.W.2d 53",
            "460 Mich. 626"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Phillip Moore",
          "cluster_id": 577749,
          "cite": [
            "956 F.2d 843",
            "1992 U.S. App. LEXIS 5431",
            "1992 WL 23161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sabbath v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107718) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzY1OTg0MDAwMDAmcz0xOTA1OTg2JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107718%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107718)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04NiZzPTM4OTMxMyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107718%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107718)",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 0,
        "triage_read": 0,
        "triage_snippet_classified": 0
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107718)",
    "indexed_citing_opinions": 360,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107718,
        "count": 360,
        "count_source": "search"
      }
    ],
    "citation_count": 529,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/sabbath-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjE1MDU0MiZzPTIzNjAzNzcmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28107718%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107718,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107718,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107718,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107718,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107718,
        "cited_id": 262481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107718,
        "cited_id": 262919,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107718,
        "cited_id": 269628,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107718,
        "cited_id": 270969,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107718,
        "cited_id": 273233,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107718,
        "cited_id": 276554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107718,
        "cited_id": 1266674,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107718,
        "cited_id": 1444858,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107718,
        "cited_id": 1457039,
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
    "date_created": "2026-07-05T18:21:45Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T18:22:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:22:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T18:27:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:22:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Sabbath v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b632-5">
  Mr. Justice Marshall
 </author>
<p id="AUV">
  delivered the opinion of the Court.
 </p>
<p id="b632-6">
  The issue in this case is whether petitioner's arrest was invalid because federal officers opened the closed but unlocked door of petitioner's apartment and entered in order to arrest him without first announcing their identity and purpose. We hold that the method of entry vitiated the arrest and therefore that evidence seized in the subsequent search incident thereto should not have been admitted at petitioner’s trial.
 </p>
<p id="b632-7">
  On February 19, 1966, one William Jones was detained at the border between California and Mexico by United States customs agents, who found in his possession an ounce of cocaine. After some questioning, Jones told the agents that he had been given the narcotics in Tijuana, Mexico, by a person named “Johnny," whom he had accompanied there from Los Angeles. He said he was to transport the narcotics to “Johnny” in the latter city.
 </p>
<p id="b632-8">
  Also found in Jones’ possession was a card on which was written the name “Johnny” and a Los Angeles telephone number. On the following day at about 3 p. m., Jones made a call to the telephone number listed on the card; a customs agent dialed the number, and with Jones’ permission, listened to the ensuing conversation. A male voice answered the call, and Jones addressed the man as “Johnny.” Jones said he was in San Diego, and still had “his thing.” The man asked Jones if he had “any trouble getting through the line.” Jones replied that he had not. Jones inquired whether “Johnny” planned to remain at home, and upon receiving an affirmative answer, indicated that he was on his way to Los Angeles, and would go to the man’s apartment.
 </p>
<p id="b633-4">
<span citation-index="1" class="star-pagination" label="587"> 
   *587
   </span>
  At about 7:30 that evening, the customs agents went with Jones to an apartment building in Los Angeles. The agents returned to Jones the cocaine they had seized from him, and placed a small broadcasting device on him. The agents waited outside the building, listening on a receiving apparatus. Jones knocked on the apartment door; a woman answered. Jones asked if “Johnny” was in, and was told to wait a minute. Steps were heard and then a man asked Jones something about “getting through the line.” Because of noise from a phonograph in the apartment, reception from the broadcasting device on Jones’ person was poor, but agents did hear the word “package.”
 </p>
<p id="b633-5">
  The customs agents waited outside for five to 10 minutes, and- then proceeded to the apartment door. One knocked, waited a few seconds, and, receiving no response, opened the unlocked door, and entered the apartment with his gun drawn. Other agents followed, at least one of whom also had his gun drawn. They saw petitioner sitting on a couch, in the process of withdrawing his hand from under the adjacent cushion. After placing petitioner under arrest, an agent found the package of cocaine under the cushion, and subsequently other items (e.
  <em>
   g.,
  </em>
  small pieces of tin foil) were found in the apartment; officers testified at trial they were adapted to packaging narcotics.
 </p>
<p id="b633-6">
  Petitioner and Jones were indicted for knowingly importing the cocaine into this country and concealing it, in violation of § 2 of the Narcotic Drugs Import and Export Act, as amended, <span class="citation no-link">35 Stat. 614</span>, <span class="citation no-link">21 U. S. C. §§ 173</span> and 174. Petitioner was tried alone. The narcotics seized at petitioner’s apartment were admitted into evidence, over objection. On appeal, following the conviction, the Court of Appeals for the Ninth Circuit ruled that the officers, in effecting entry to petitioner’s apartment by opening the closed but unlocked door, did not “break open” the door within the meaning of 18
  <span citation-index="1" class="star-pagination" label="588"> 
   *588
   </span>
  U. S. C. § 3109 and therefore were not required by that statute to make a prior announcement of “authority and purpose.” <span class="citation" data-id="276554"><a href="/opinion/276554/johnny-sabbath-v-united-states/" aria-description="Citation for case: Johnny Sabbath v. United States">380 F. 2d 108</a></span>. We granted certiorari, 389 TJ. S. 1003 (1967), to consider the somewhat uncomplicated but nonetheless significant issue of whether the agents’ entry was consonant with federal law.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  We hold that it was not, and therefore reverse.
 </p>
<p id="b634-6">
  The statute here involved, <span class="citation no-link">18 U. S. C. § 3109</span>,
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  deals with the entry of federal officers into a dwelling in terms only in regard to the execution of a search warrant. This Court has held, however, that the validity of such an entry of a federal officer to effect an arrest without a warrant “must be tested by criteria identical with those embodied in” that statute.
  <em>
   Miller
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#306" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 306</a></span> (1958);
  <em>
   Wong Sun
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#482" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 482-484</a></span> (1963).
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  We therefore agree with
  <span citation-index="1" class="star-pagination" label="589"> 
   *589
   </span>
  the parties and with the court below that we must look to § 3109 as controlling.
 </p>
<p id="b635-5">
  In
  <em>
   Miller
  </em>
  v.
  <em>
   United States, supra,
  </em>
  the commonlaw background to § 3109 was extensively examined.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  The Court there concluded,
  <em>
   id.,
  </em>
  at 313:
 </p>
<blockquote id="b635-6">
  “The requirement of prior notice of authority and purpose before forcing entry into a home is deeply rooted in our heritage and should not be given grudging application. Congress, codifying a tradition embedded in Anglo-American law, had declared in § 3109 the reverence of the law for the individual’s right of privacy in his house.”
 </blockquote>
<p id="b635-7">
  It was also noted,
  <em>
   id.,
  </em>
  at 313, n. 12, that another facet of the rule of announcement was, generally, to safeguard officers, who might be mistaken, upon an unannounced intrusion into a home, for someone with no right to be there. See also
  <em>
   McDonald
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#460" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 460-461</a></span> (concurring opinion).
 </p>
<p id="b635-8">
  Considering the purposes of § 3109, it would indeed be a “grudging application” to hold, as the Government urges, that the use of “force” is an indispensable element of the statute. To be sure, the statute uses the phrase “break open” and that connotes some use of force. But linguistic analysis seldom is adequate when a statute is designed to incorporate fundamental values and the ongoing development of the common law.
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  Thus, the
  <span citation-index="1" class="star-pagination" label="590"> 
   *590
   </span>
  California Supreme Court has recently interpreted the common-law rule of announcement codified in a state statute identical in relevant terms to § 3109 to apply to an entry by police through a closed but unlocked door.
  <em>
   People
  </em>
  v.
  <em>
   Rosales,
  </em>
  <span class="citation" data-id="9846791"><a href="/opinion/1266674/people-v-rosales/" aria-description="Citation for case: People v. Rosales">68 Cal. 2d 299</a></span>, <span class="citation" data-id="9846791"><a href="/opinion/1266674/people-v-rosales/" aria-description="Citation for case: People v. Rosales">437 P. 2d 489</a></span> (1968). And it has been held that § 3109 applies to entries effected by the use of a passkey,
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
  which requires no more force than does the turning of a doorknob. An unannounced intrusion into a dwelling — what § 3109 basically proscribes — is no less an unannounced intrusion whether officers break down a door, force open a chain lock on a partially open door, open a locked door by use of a passkey, or, as here, open a closed but unlocked door.
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  The protection afforded by, and the values inherent in, § 3109 must be “governed by something more than the fortuitous circumstance of an unlocked door.”
  <em>
   Keiningham
  </em>
  v.
  <em>
   United States,
  </em>
  109 U. S. App. D. C. 272, 276, <span class="citation" data-id="6920640"><a href="/opinion/7019595/keiningham-v-united-states/#130" aria-description="Citation for case: Keiningham v. United States">287 F. 2d 126, 130</a></span> (1960).
 </p>
<p id="b637-4">
<span citation-index="1" class="star-pagination" label="591"> 
   *591
   </span>
  The Government seeks to invoke an exception to the rule of announcement, contending that the agents’ lack of compliance with the statute is excused because an announcement might have endangered the informant Jones or the officers themselves. See,
  <em>
   e. g., Gilbert
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9452205"><a href="/opinion/273233/jesse-james-gilbert-v-united-states/#931" aria-description="Citation for case: Jesse James Gilbert v. United States">366 F. 2d 923, 931</a></span> (C. A. 9th Cir. 1966), cert, denied, <span class="citation multiple-matches"><a href="/c/U.%20S./388/922/">388 U. S. 922</a></span> (1967); cf.
  <em>
   Ker
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#39" aria-description="Citation for case: Ker v. California">374 U. S. 23, 39-40</a></span> (1963) (opinion of Clark, J.);
  <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#47" aria-description="Citation for case: Ker v. California"><em>
   id.,
  </em>
  at 47</a></span> (opinion of Brennan, J.). However, whether or not “exigent circumstances,”
  <em>
   Miller
  </em>
  v.
  <em>
   United States, supra,
  </em>
  at 309, would excuse compliance with § 3109,
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
  this record does not reveal any substantial basis for excusing the failure of the agents here to announce their authority and purpose. The agents had no basis for assuming petitioner was armed or might resist arrest, or that Jones was in any danger. Nor, as to the former, did the agents make any independent investigation of petitioner prior to setting the stage for his arrest with the narcotics in his possession.
 </p>
<p id="b637-5">
  The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.
 </p>
<p id="b637-6">
<em>
   Reversed and remanded.
  </em>
</p>
<judges id="b637-7">
  Mr. Justice Black dissents.
 </judges>








<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b634-7">
   The Government contends in this Court that petitioner did not adequately raise at trial the issue of the agents’ manner of entry, and therefore that it did not have sufficient opportunity to indicate the full circumstances surrounding the entry and petitioner’s arrest. However, petitioner’s trial counsel, in the course of objecting, clearly stated there were no facts “sufficient to justify this officer’s breaking into” the apartment, and his objection was truncated by a ruling of the trial judge. In any event, the Government met the issue on the merits in the Court of Appeals, and apparently did not there contend the record was inadequate for its resolution; and the Court of Appeals decided the issue on the merits. In these circumstances, we are justified in likewise doing so.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b634-8">
   “The officer may break open any outer or inner door or window of a house, or any part of a house, or anything therein, to execute a search warrant, if, after notice of his authority and purpose, he is refused admittance or when necessary to liberate himself or a person aiding him in the execution of the warrant.”
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b634-9">
   See also,
   <em>
    e. g., Ng Pui Yu
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="269628"><a href="/opinion/269628/ng-pui-yu-v-united-states/#631" aria-description="Citation for case: Ng Pui Yu v. United States">352 F. 2d 626, 631</a></span> (C. A. 9th Cir. 1965);
   <em>
    Gatlin
   </em>
   v.
   <em>
    United States,
   </em>
   117 U. S. App. D. C. 123, 130, <span class="citation" data-id="262919"><a href="/opinion/262919/paul-w-gatlin-v-united-states-of-america-dennis-o-miller-v-united/#673" aria-description="Citation for case: Paul W. Gatlin v. United States of America, Dennis O....">326 F. 2d 666, 673</a></span> (C. A. D. C. Cir. 1963);
   <em>
    United States
   </em>
   v.
   <em>
    Cruz,
   </em>
   <span class="citation" data-id="1457039"><a href="/opinion/1457039/united-states-v-cruz/#21" aria-description="Citation for case: United States v. Cruz">265 F. Supp. 15, 21</a></span> (W. D. Tex. 1967).
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b635-9">
   See also
   <em>
    Ker
   </em>
   v.
   <em>
    California,
   </em>
   <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#47" aria-description="Citation for case: Ker v. California">374 U. S. 23, 47-59</a></span> (1963) (opinion of BreNNAN, J.).
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b635-10">
   While distinctions are obvious, a useful analogy is nonetheless afforded by the common and case law development of the law of burglary: a forcible entry has generally been eliminated as an element of that crime under statutes using the word “break,” or similar words. See R. Perkins, Criminal Law 149-150 (1957); J. Michael &amp; H. Wechsler, Criminal Law and Its Administration 367-382 (1940); Note, A Rationale of the Law of Burglary, 51 Col. L. Rev. 1009, 1012-1015 (1951). Commentators on the law of arrest have
   <span citation-index="1" class="star-pagination" label="590"> 
    *590
    </span>
   viewed the development of that body of law as similar. See EL Voorhees, Law of Arrest §§ 159, 172-173 (1904); Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 798</span>, 806 (1924):
  </p>
<p id="b636-6">
   “What constitutes ‘breaking’ seems to be the same as in burglary: lifting a latch, turning a door knob, unhooking a chain or hasp, removing a prop to, or pushing open, a closed door of entrance to the house, — even a closed screen door ... is a breaking . . . .” (Footnotes omitted.)
  </p>
<p id="b636-8">
   See generally Blakey, The Rule of Announcement and Unlawful Entry, <span class="citation no-link">112 U. Pa. L. Rev. 499</span> (1964).
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b636-9">
   See, e.
   <em>
    g., Munoz
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="262481"><a href="/opinion/262481/john-munoz-v-united-states/#26" aria-description="Citation for case: John Munoz v. United States">325 F. 2d 23, 26</a></span> (C. A. 9th Cir. 1963);
   <em>
    United States
   </em>
   v.
   <em>
    Sims,
   </em>
   <span class="citation" data-id="1444858"><a href="/opinion/1444858/united-states-v-sims/#254" aria-description="Citation for case: United States v. Sims">231 F. Supp. 251, 254</a></span> (D. C. Md. 1964); cf.
   <em>
    People
   </em>
   v.
   <em>
    Stephens,
   </em>
   <span class="citation" data-id="2190677"><a href="/opinion/2190677/people-v-stephens/" aria-description="Citation for case: People v. Stephens">249 Cal. App. 2d 113</a></span>, <span class="citation" data-id="2190677"><a href="/opinion/2190677/people-v-stephens/" aria-description="Citation for case: People v. Stephens">57 Cal. Rptr. 66</a></span> (1967). See also
   <em>
    Ker
   </em>
   v.
   <em>
    California,
   </em>
   <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#38" aria-description="Citation for case: Ker v. California">374 U. S., at 38</a></span>.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b636-10">
   We do not deal here with entries obtained by ruse, which have been viewed as involving no “breaking.” See,
   <em>
    e. g., Smith
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="270969"><a href="/opinion/270969/willis-smith-and-resolute-insurance-company-of-hartford-connecticut-v/" aria-description="Citation for case: Willis Smith and Resolute Insurance Company of Hartford,...">357 F. 2d 486</a></span>, 488 n. 1 (C. A. 5th Cir. 1966);
   <em>
    Leahy
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9447103"><a href="/opinion/249453/charles-f-leahy-v-united-states/#489" aria-description="Citation for case: Charles F. Leahy v. United States">272 F. 2d 487, 489</a></span> (C. A. 9th Cir. 1959). See also Wilgus, n. 5,
   <em>
    supra,
   </em>
   at 806.
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b637-8">
   Exceptions to any possible constitutional rule relating to announcement and entry have been recognized, see
   <em>
    Ker
   </em>
   v.
   <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#47" aria-description="Citation for case: Ker v. California"><em>
    California, supra,
   </em>
   at 47</a></span> (opinion of BreNNAN, J.), and there is little reason why those limited exceptions might not also apply to § 3109, since they existed at common law, of which the statute is a codification. See generally Blakey, n. 5,
   <em>
    supra.
   </em>
</p>
</div></div></opinion>
```

---

## GROUP: content/cases/Safford Unified School District v. Redding.md  (`case`, 6 assertions)

### content_page

```
---
title: "Safford Unified School District v. Redding"
type: case
citation: ""
parallel_cite: "557 U.S. 364; 129 S. Ct. 2633; 174 L. Ed. 2d 354; 21 Fla. L. Weekly Fed. S 1011; 77 U.S.L.W. 4591"
neutral_cite: 2009 U.S. LEXIS 4735
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-06-25
docket: 08-479
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2009-06-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Safford Unified School District v. Redding
  varies_by_point: false
  scope_note: "Good law; applies and cabins the New Jersey v. T.L.O. school-search standard to strip searches."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145852/safford-unified-school-district-1-v-redding/"
  cluster_id: 145852
  opinion_id: 9435302
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Progeny (school searches)"
  - page: "[[Qualified Immunity]]"
    role: "Related (qualified immunity)"
related: ["[[New Jersey v. T.L.O.]]"]
aliases: ["Safford Unified School District No. 1 v. Redding"]
tags: ["case", "fourth-amendment", "special-needs", "school-search", "strip-search", "qualified-immunity"]
holding: "Under the T.L.O. school-search standard, a strip search of a student must be justified by reasonable suspicion that matches its intrusiveness; strip-searching a 13-year-old for common pain relievers, absent reason to believe they were dangerous or hidden in her underwear, was unreasonable — but the officials had qualified immunity because the right was not clearly established."
lake:
  record_id: Safford Unified School District v. Redding
  status: verified
  projected_at: 2026-07-09
---

# Safford Unified School District v. Redding

*557 U.S. 364 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A 13-year-old student, Savana Redding, was strip-searched at Safford Middle School after another student, caught with pills, said Savana had given them to her. The pills were prescription-strength ibuprofen (400 mg) and over-the-counter naproxen — both banned under school rules without permission. The assistant principal had Savana's backpack and outer clothing searched (nothing found), then directed female staff to have her pull out and shake her bra and underwear, partially exposing her breasts and pelvic area. Nothing was found. Savana sued under § 1983.

## Issue
Whether the strip search of a student for common pain-relief pills was reasonable under the Fourth Amendment school-search standard of *[[New Jersey v. T.L.O.]]*, and whether the officials who conducted it were entitled to [[Qualified Immunity|qualified immunity]].

## Rule
A school search must be reasonable in scope as well as inception: "the search as actually conducted [be] reasonably related in scope to the circumstances which justified the interference in the first place." — *[[New Jersey v. T.L.O.]]*, 469 U.S. at 341 (applied in *Safford*). A strip search is "categorically distinct," and its degree of intrusion must be matched by the suspicion supporting it.

"[W]hat was missing from the suspected facts that pointed to Savana was any indication of danger to the students from the power of the drugs or their quantity, and any reason to suppose that Savana was carrying pills in her underwear. We think that the combination of these deficiencies was fatal to finding the search reasonable." — 557 U.S. at 376–377. ^pin-376

But the unconstitutionality was not clearly established: "because there is reason to question the clarity with which the right was established, the official who ordered the unconstitutional search is entitled to qualified immunity from liability." — [*Id.* at 368](https://www.courtlistener.com/opinion/145852/safford-unified-school-district-1-v-redding/#:~:text=because%20there%20is%20reason%20to). ^pin-368

## Application
Reasonable suspicion supported searching Savana's backpack and outer clothing, but extending the search to her bra and underwear demanded a justification matching that intrusion. "Savana's subjective expectation of privacy … is inherent in her account of it as embarrassing, frightening, and humiliating." — 557 U.S. at 374–375. ^pin-374

The drugs at issue were common pain relievers posing no obvious danger, nothing indicated they were hidden in her underwear, and there was no individualized reason to expect contraband there. The intrusion thus outran the suspicion, making the strip search unreasonable. Because lower courts had genuinely divided over such searches, however, the right was not clearly established, so the individual officials kept [[Qualified Immunity|qualified immunity]]; the case was [[Reading and Citing Cases#on-remand|remanded]] on the district's potential liability.

## Conclusion
The strip search violated the Fourth Amendment, but the officials had [[Qualified Immunity|qualified immunity]]; affirmed in part, reversed in part, and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Safford* applies and sharpens the [[New Jersey v. T.L.O.]] reasonableness standard for the categorically more intrusive strip search, holding the intrusion must match the suspicion, while granting the officials [[Qualified Immunity|qualified immunity]] on the unsettled state of the law.

## Appears on
- [[Special Needs and Administrative Searches]] — *Progeny (school searches)*
- [[Section 1983 Liability and Qualified Immunity]] — *Related ([[Qualified Immunity|qualified immunity]])*

## Sources
- *Safford Unified School District No. 1 v. Redding*, 557 U.S. 364 (2009) — https://www.courtlistener.com/opinion/145852/safford-unified-school-district-1-v-redding/ — pinpoints: 368, 374–375, 376–377.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "851b6385ce9cf236", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2009 U.S. LEXIS 4735", "official_citation_present": false, "parallel_cite": "557 U.S. 364; 129 S. Ct. 2633; 174 L. Ed. 2d 354; 21 Fla. L. Weekly Fed. S 1011; 77 U.S.L.W. 4591", "title": "Safford Unified School District v. Redding", "year": "2009"}}
{"assertion_id": "800adb00b9fb8e8d", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Related (qualified immunity)", "title": "Safford Unified School District v. Redding"}}
{"assertion_id": "8755d028bbc67f9c", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Progeny (school searches)", "title": "Safford Unified School District v. Redding"}}
{"assertion_id": "8790fb5e48c9695b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Under the T.L.O. school-search standard, a strip search of a student must be justified by reasonable suspicion that matches its intrusiveness; strip-searching a 13-year-old for common pain relievers, absent reason to believe they were dangerous or hidden in her underwear, was unreasonable — but the officials had qualified immunity because the right was not clearly established.", "title": "Safford Unified School District v. Redding"}}
{"assertion_id": "79f33c19408320dc", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2009-06-25", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Safford Unified School District v. Redding", "field_i_validity": "good_law", "scope_note": "Good law; applies and cabins the New Jersey v. T.L.O. school-search standard to strip searches.", "title": "Safford Unified School District v. Redding", "varies_by_point": "false"}}
{"assertion_id": "b4c59d95f1d99c8a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Safford Unified School District v. Redding"}}
```

### lake record — Safford Unified School District v. Redding

```json
{
  "schema_version": "s2.v1",
  "record_id": "Safford Unified School District v. Redding",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Safford Unified School District 1 v. Redding",
    "case_name_short": "Redding",
    "case_name_full": "SAFFORD UNIFIED SCHOOL DISTRICT #1 Et Al. v. REDDING",
    "input_case_name": "Safford Unified School District v. Redding",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-06-25",
    "year": 2009,
    "docket": "08-479",
    "cluster_id": 145852,
    "lead_opinion_id": 9435302,
    "sibling_ids": [
      145852,
      9435302,
      9435303,
      9435304,
      9435305
    ],
    "absolute_url": "/opinion/145852/safford-unified-school-district-1-v-redding/",
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
        "cite": "557 U.S. 364",
        "volume": "557",
        "reporter": "U.S.",
        "page": "364",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 2633",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "2633",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "174 L. Ed. 2d 354",
        "volume": "174",
        "reporter": "L. Ed. 2d",
        "page": "354",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "21 Fla. L. Weekly Fed. S 1011",
        "volume": "21",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "1011",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 U.S.L.W. 4591",
        "volume": "77",
        "reporter": "U.S.L.W.",
        "page": "4591",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 4735",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "4735",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "557 U.S. 364",
        "volume": "557",
        "reporter": "U.S.",
        "page": "364",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 2633",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "2633",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "174 L. Ed. 2d 354",
        "volume": "174",
        "reporter": "L. Ed. 2d",
        "page": "354",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 4735",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "4735",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "21 Fla. L. Weekly Fed. S 1011",
        "volume": "21",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "1011",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 U.S.L.W. 4591",
        "volume": "77",
        "reporter": "U.S.L.W.",
        "page": "4591",
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
      "id": "pin-376",
      "page": null,
      "quote": "and its degree of intrusion must be matched by the suspicion supporting it.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-368",
      "page": null,
      "quote": "because there is reason to question the clarity with which the right was established, the official who ordered the unconstitutional search is entitled to qualified immunity from liability.",
      "star_marker": "368",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 691,
      "fragment": "#:~:text=because%20there%20is%20reason%20to",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-374",
      "page": null,
      "quote": "Savana's subjective expectation of privacy \u2026 is inherent in her account of it as embarrassing, frightening, and humiliating.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2009-06-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Safford Unified School District v. Redding",
    "varies_by_point": false,
    "scope_note": "Good law; applies and cabins the New Jersey v. T.L.O. school-search standard to strip searches.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Ward",
          "cluster_id": 4433423,
          "cite": [
            "2017 Ohio 8141",
            "98 N.E.3d 1257"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. King",
          "cluster_id": 8441539,
          "cite": [
            "736 F.3d 805",
            "2013 WL 4516751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Marcel King",
          "cluster_id": 854814,
          "cite": [
            "711 F.3d 986",
            "2013 WL 886161",
            "2013 U.S. App. LEXIS 4730"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Morgan v. Swanson",
          "cluster_id": 8441074,
          "cite": [
            "659 F.3d 359",
            "2011 U.S. App. LEXIS 19656",
            "2011 WL 4470233"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re D.H.",
          "cluster_id": 5280981,
          "cite": [
            "306 S.W.3d 955"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane1_negative"
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
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Natasha Whitley v. John Hanna",
          "cluster_id": 1036944,
          "cite": [
            "726 F.3d 631",
            "2013 WL 4029134",
            "2013 U.S. App. LEXIS 16485"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
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
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roe v. Elyea",
          "cluster_id": 183790,
          "cite": [
            "631 F.3d 843",
            "78 Fed. R. Serv. 3d 874",
            "2011 U.S. App. LEXIS 1781",
            "2011 WL 256978"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Emerson v. City of New York",
          "cluster_id": 2473879,
          "cite": [
            "740 F. Supp. 2d 385",
            "2010 U.S. Dist. LEXIS 74318",
            "2010 WL 2910661"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alan Baynes v. Brandon Cleland",
          "cluster_id": 2829925,
          "cite": [
            "799 F.3d 600",
            "2015 FED App. 0205P",
            "2015 U.S. App. LEXIS 14824",
            "2015 WL 5000615"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
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
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bull v. City and County of San Francisco",
          "cluster_id": 1313115,
          "cite": [
            "595 F.3d 964",
            "2010 WL 431790"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shari Guertin v. State of Mich.",
          "cluster_id": 4578962,
          "cite": [
            "912 F.3d 907"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
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
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Pack",
          "cluster_id": 150729,
          "cite": [
            "612 F.3d 341",
            "2010 U.S. App. LEXIS 14562",
            "2010 WL 2777061"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Allen Quigley v. Tuong Thai",
          "cluster_id": 821001,
          "cite": [
            "707 F.3d 675",
            "2013 WL 627207",
            "2013 U.S. App. LEXIS 3615"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Outlaw v. City of Hartford",
          "cluster_id": 4475062,
          "cite": [
            "884 F.3d 351"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillips v. Community Ins. Corp.",
          "cluster_id": 798871,
          "cite": [
            "678 F.3d 513",
            "2012 WL 1449675",
            "2012 U.S. App. LEXIS 8582"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edgerly v. City and County of San Francisco",
          "cluster_id": 409,
          "cite": [
            "599 F.3d 946",
            "2010 U.S. App. LEXIS 5697",
            "2010 WL 986764"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe v. Woodard",
          "cluster_id": 4578612,
          "cite": [
            "912 F.3d 1278"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bettina Littell v. Houston Independent Sch",
          "cluster_id": 4511891,
          "cite": [
            "894 F.3d 616"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffrey Leiser v. Karen Kloth",
          "cluster_id": 4645048,
          "cite": [
            "933 F.3d 696"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Maciel-Figueroa",
          "cluster_id": 4372448,
          "cite": [
            "361 Or. 163",
            "389 P.3d 1121",
            "2017 Ore. LEXIS 166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "C. B. v. City of Sonora",
          "cluster_id": 2743611,
          "cite": [
            "769 F.3d 1005",
            "89 Fed. R. Serv. 3d 1624",
            "2014 U.S. App. LEXIS 19757",
            "2014 WL 5151632"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vincent v. Yelich Earley v. Annucci",
          "cluster_id": 875349,
          "cite": [
            "718 F.3d 157"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony Novak v. City of Parma",
          "cluster_id": 4643674,
          "cite": [
            "932 F.3d 421"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Christopher Cantu v. City of Dothan, Alabama",
          "cluster_id": 4782328,
          "cite": [
            "974 F.3d 1217"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wesby v. District of Columbia",
          "cluster_id": 2722589,
          "cite": [
            "412 U.S. App. D.C. 246",
            "765 F.3d 13",
            "2014 U.S. App. LEXIS 16893",
            "2014 WL 4290316"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Safford Unified School District v. Redding:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145852 OR 9435302 OR 9435303 OR 9435304 OR 9435305) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 157,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 157,
        "triage_read": 5,
        "triage_snippet_classified": 152
      },
      "lane2_top_cited": {
        "query": "cites:(145852 OR 9435302 OR 9435303 OR 9435304 OR 9435305)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00OSZzPTI4MzA5MjMmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145852+OR+9435302+OR+9435303+OR+9435304+OR+9435305%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145852 OR 9435302 OR 9435303 OR 9435304 OR 9435305)",
        "reviewed": 12,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 12,
        "triage_read": 0,
        "triage_snippet_classified": 12
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145852 OR 9435302 OR 9435303 OR 9435304 OR 9435305)",
    "indexed_citing_opinions": 191,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145852,
        "count": 150,
        "count_source": "search"
      },
      {
        "opinion_id": 9435302,
        "count": 46,
        "count_source": "search"
      },
      {
        "opinion_id": 9435303,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9435304,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9435305,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 367,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/safford-unified-school-district-v-redding.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY3MDY3NDgmcz00NzM5ODgwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28145852+OR+9435302+OR+9435303+OR+9435304+OR+9435305%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145852,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 107841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 109136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 109776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 111305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 111549,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 112448,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 112595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 112699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 117957,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 118277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 118474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 121169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 121171,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 145626,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 145669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 145707,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 145814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 145918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 382282,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 438820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 548401,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 563694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 741842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 781346,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 1262302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 1429635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 1467104,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145852,
        "cited_id": 2620702,
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
    "date_created": "2026-07-05T18:27:23Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T18:27:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:27:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T18:30:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:27:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Safford Unified School District v. Redding

```
<opinion data-order="10" data-type="opinion" id="x999-2" type="majority">
<author id="b416-3"><page-number citation-index="1" label="368">*368</page-number>Justice Souter</author>
<p id="AoF">delivered the opinion of the Court.</p>
<p id="b416-4">The issue here is whether a 13-year-old student’s Fourth Amendment right was violated when she was subjected to a search of her bra and underpants by school officials acting on reasonable suspicion that she had brought forbidden prescription and over-the-counter drugs to school. Because there were no reasons to suspect the drugs presented a danger or were concealed in her underwear, we hold that the search did violate the Constitution, but because there is reason to question the clarity with which the right was established, the official who ordered the unconstitutional search is entitled to qualified immunity from liability.</p>
<p id="b416-5">I</p>
<p id="b416-6">The events immediately prior to the search in question began in 13-year-old Savana Redding’s math class at Safford Middle School one October day in 2003. The assistant principal of the school, Kerry Wilson, came into the room and asked Savana to go to his office. There, he showed her a day planner, unzipped and open flat on his desk, in which there were several knives, lighters, a permanent marker, and a cigarette. Wilson asked Savana whether the planner was hers; she said it was, but that a few days before she had lent it to her Mend, Marissa Glines. Savana stated that none of the items in the planner belonged to her.</p>
<p id="b416-7">Wilson then showed Savana four white prescription-strength ibuprofen 400-mg pills, and one over-the-counter blue naproxen 200-mg pill, all used for pain and inflammation but banned under school rules without advance permission. He asked Savana if she knew anything about the pills. Savana answered that she did not. Wilson then told Savana that he had received a report that she was giving these pills to fellow students; Savana denied it and agreed to let Wilson search her belongings. Helen Romero, an administrative assistant, came into the office, and together with Wilson they searched Savana’s backpack, finding nothing.</p>
<p id="b417-4"><page-number citation-index="1" label="369">*369</page-number>At that point, Wilson instructed Romero to take Savana to the school nurse’s office to search her clothes for pills. Romero and the nurse, Peggy Sehwallier, asked Savana to remove her jacket, socks, and shoes, leaving her in stretch pants and a T-shirt (both without pockets), which she was then asked to remove. Finally, Savana was told to pull her bra out and to the side and shake it, and to pull out the elastic on her underpants, thus exposing her breasts and pelvic area to some degree. No pills were found.</p>
<p id="b417-5">Savana’s mother filed suit against Safford Unified School District #1, Wilson, Romero, and Sehwallier for conducting a strip search in violation of Savana’s Fourth Amendment rights. The individuals (hereinafter petitioners) moved for summary judgment, raising a defense of qualified immunity. The District Court for the District of Arizona granted the motion on the ground that there was no Fourth Amendment violation, and a panel of the Ninth Circuit affirmed. <span class="citation" data-id="9627996"><a href="/opinion/1429635/redding-v-safford-unified-school-district-1/" aria-description="Citation for case: Redding v. Safford Unified School District 1">504 F. 3d 828</a></span> (2007).</p>
<p id="b417-6">A closely divided Circuit sitting en bane, however, reversed. Following the two-step protocol for evaluating claims of qualified immunity, see <em>Saucier </em>v. <em>Katz, </em><span class="citation multiple-matches"><a href="/c/U.%20S./533/194/">533 U. S. 194</a></span>, 200 (2001), the Ninth Circuit held that the strip search was unjustified under the Fourth Amendment test for searches of children by school officials set out in <em>New Jersey </em>v. <em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325</a></span> (1985). <span class="citation" data-id="9635255"><a href="/opinion/1467104/redding-v-safford-unified-school-dist-no-1/#1081" aria-description="Citation for case: Redding v. Safford Unified School Dist. No. 1">531 F. 3d 1071, 1081-1087</a></span> (2008). The Circuit then applied the test for qualified immunity, and found that Savana’s right was clearly established at the time of the search: “ '[tjhese notions of personal privacy are “clearly established” in that they inhere in all of us, particularly middle school teenagers, and are inherent in the privacy component of the Fourth Amendment’s proscription against unreasonable searches.’” <em><span class="citation" data-id="9635255"><a href="/opinion/1467104/redding-v-safford-unified-school-dist-no-1/" aria-description="Citation for case: Redding v. Safford Unified School Dist. No. 1">Id.,</a></span> </em>at 1088-1089 (quoting <em>Brannum </em>v. <em>Overton Cty. School Bd., </em><span class="citation" data-id="1262302"><a href="/opinion/1262302/brannum-ex-rel-brannum-v-overton-county-school-board/#499" aria-description="Citation for case: Brannum Ex Rel. Brannum v. Overton County School Board">516 F. 3d 489, 499</a></span> (CA6 2008)). The upshot was reversal of summary judgment as to Wilson, while affirming the judgments in favor of Sehwallier, the school nurse, and Romero, the administrative <page-number citation-index="1" label="370">*370</page-number>assistant, since they had not acted as independent decision-makers. <span class="citation" data-id="9635255"><a href="/opinion/1467104/redding-v-safford-unified-school-dist-no-1/#1089" aria-description="Citation for case: Redding v. Safford Unified School Dist. No. 1">531 F. 3d, at 1089</a></span>.</p>
<p id="b418-4">We granted certiorari, <span class="citation no-link">555 U. S. 1130</span> (2009), and now affirm in part, reverse in part, and remand.</p>
<p id="b418-5">II</p>
<p id="b418-6">The Fourth Amendment “right of the people to be secure in their persons . . . against unreasonable searches and seizures” generally requires a law enforcement officer to have probable cause for conducting a search. “Probable cause exists where ‘the facts and circumstances within [an officer’s] knowledge and of which [he] had reasonably trustworthy information [are] sufficient in themselves to warrant a man of reasonable caution in the belief that’ an offense has been or is being committed,” <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175-176</a></span> (1949) (quoting <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#162" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 162</a></span> (1925)), <em>and </em>that evidence bearing on that offense will be found in the place to be searched.</p>
<p id="b418-7">In <em>T. L. O., </em>we recognized that the school setting “requires some modification of the level of suspicion of illicit activity needed to justify a search,” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#340" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 340</a></span>, and held that for searches by school officials “a careful balancing of governmental and private interests suggests that the public interest is best served by a Fourth Amendment standard of reasonableness that stops short of probable cause,” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#341" aria-description="Citation for case: New Jersey v. T. L. O."><em>id., </em>at 341</a></span>. We have thus applied a standard of reasonable suspicion to determine the legality of a school administrator’s search of a student, <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#342" aria-description="Citation for case: New Jersey v. T. L. O."><em>id., </em>at 342, 345</a></span>, and have held that a school search “will be permissible in its scope when the measures adopted are reasonably related to the objectives of the search and not excessively intrusive in light of the age and sex of the student and the nature of the infraction,” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#342" aria-description="Citation for case: New Jersey v. T. L. O."><em>id., </em>at 342</a></span>.</p>
<p id="b418-8">A number of our cases on probable cause have an implicit bearing on the reliable knowledge element of reasonable suspicion, as we have attempted to flesh out the knowledge com<page-number citation-index="1" label="371">*371</page-number>ponent by looking to the degree to which known facts imply prohibited conduct, see, <em>e. g., Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#148" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 148</a></span> (1972); <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#160" aria-description="Citation for case: Adams v. Williams"><em>id., </em>at 160, n. 9</a></span> (Marshall, J., dissenting), the specificity of the information received, see, <em>e. g., Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#416" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410, 416-417</a></span> (1969), and the reliability of its source, see, <em>e. g., Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#114" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 114</a></span> (1964). At the end of the day, however, we have realized that these factors cannot rigidly control, <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#230" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 230</a></span> (1983), and we have come back to saying that the standards are “fluid concepts that take their substantive content from the particular contexts” in which they are being assessed, <em>Ornelas </em>v. <em>United States, </em><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#696" aria-description="Citation for case: Ornelas v. United States">517 U. S. 690, 696</a></span> (1996).</p>
<p id="b419-5">Perhaps the best that can be said generally about the required knowledge component of probable cause for a law enforcement officer’s evidence search is that it raise a “fair probability,” <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#238" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 238</a></span>, or a “substantial chance,” <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#244" aria-description="Citation for case: Illinois v. Gates"><em>id., </em>at 244, n. 13</a></span>, of discovering evidence of criminal activity. The lesser standard for school searches could as readily be described as a moderate chance of finding evidence of wrongdoing.</p>
<p id="b419-6">Ill</p>
<p id="b419-7">A</p>
<p id="b419-8">In this case, the school’s policies strictly prohibit the non-medical use, possession, or sale of any drug on school grounds, including “‘[a]ny prescription or over-the-counter drug, except those for which permission to use in school has been granted pursuant to Board policy.’ ” App. to Pet. for Cert. 128a.<footnotemark>1</footnotemark> A week before Savana was searched, another <page-number citation-index="1" label="372">*372</page-number>student, Jordan Romero (no relation of the school’s administrative assistant), told the principal and Assistant Principal Wilson that “certain students were bringing drugs and weapons on campus,” and that he had been sick after taking some pills that “he got from a classmate.” App. 8a. On the morning of October 8, the same boy handed Wilson a white pill that he said Marissa Glines had given him. He told Wilson that students were planning to take the pills at lunch.</p>
<p id="b420-4">Wilson learned from Peggy Schwallier, the school nurse, that the pill was ibuprofen 400 mg, available only by prescription. Wilson then called Marissa out of class. Outside the classroom, Marissa’s teacher handed Wilson the day planner, found within Marissa’s reach, containing various contraband items. Wilson escorted Marissa back to his office.</p>
<p id="b420-5">In the presence of Helen Romero, Wilson requested Marissa to turn out her pockets and open her wallet. Marissa produced a blue pill, several white ones, and a razor blade. Wilson asked where the blue pill came from, and Marissa answered, “ ‘I guess it slipped in when <em>she </em>gave me the IBU 400s.’” <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Id.,</a></span> </em>at 13a. When Wilson asked whom she meant, Marissa replied, “‘Savana Redding.’” <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Ibid.</a></span> </em>Wilson then enquired about the day planner and its contents; Marissa denied knowing anything about them. Wilson did not ask Marissa any followup questions to determine whether there was any likelihood that Savana presently had pills: neither asking when Marissa received the pills from Savana nor where Savana might be hiding them.</p>
<p id="b421-4"><page-number citation-index="1" label="373">*373</page-number>Sehwallier did not immediately recognize the blue pill, but information provided through a poison control hotline<footnotemark>2</footnotemark> indicated that the pill was a 200-mg dose of an antiinflammatory drug, generically called naproxen, available over the counter. At Wilson’s direction, Marissa was then subjected to a search of her bra and underpants by Romero and Sehwallier, as Savana was later on. The search revealed no additional pills.</p>
<p id="b421-5">It was at this juncture that Wilson called Savana into his office and showed her the day planner. Their conversation established that Savana and Marissa were on friendly terms: while she denied knowledge of the contraband, Savana admitted that the day planner was hers and that she had lent it to Marissa. Wilson had other reports of their friendship from staff members, who had identified Savana and Marissa as part of an unusually rowdy group at the school’s opening dance in August, during which alcohol and cigarettes were found in the girls’ bathroom. Wilson had reason to connect the girls with this contraband, for Wilson knew that Jordan Romero had told the principal that before the dance, he had been at a party at Savana’s house where alcohol was served. Marissa’s statement that the pills came from Savana was thus sufficiently plausible to warrant suspicion that Savana was involved in pill distribution.</p>
<p id="b421-6">This suspicion of Wilson’s was enough to justify a search of Savana’s backpack and outer clothing.<footnotemark>3</footnotemark> If a student is <page-number citation-index="1" label="374">*374</page-number>reasonably suspected of giving out contraband pills, she is reasonably suspected of carrying them on her person and in the carryall that has become an item of student uniform in most places today. If Wilson’s reasonable suspicion of pill distribution were not understood to support searches of outer clothes and backpack, it would not justify any search worth making. And the look into Savana’s bag, in her presence and in the relative privacy of Wilson’s office, was not excessively intrusive, any more than Romero’s subsequent search of her outer clothing.</p>
<p id="b422-4">B</p>
<p id="b422-5">Here it is that the parties part company, with Savana’s claim that extending the search at Wilson’s behest to the point of making her pull out her underwear was constitutionally unreasonable. The exact label for this final step in the intrusion is not important, though strip search is a fair way to speak of it. Romero and Schwallier directed Savana to remove her clothes down to her underwear, and then “pull out” her bra and the elastic band on her underpants. <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Id.,</a></span> </em>at 23a. Although Romero and Schwallier stated that they did not see anything when Savana followed their instructions, App. to Pet. for Cert. 135a, we would not define strip search and its Fourth Amendment consequences in a way that would guarantee litigation about who was looking and how much was seen. The very fact of Savana’s pulling her underwear away from her body in the presence of the two officials who were able to see her necessarily exposed her breasts and pelvic area to some degree, and both subjective and reasonable societal expectations of personal privacy support the treatment of such a search as categorically distinct, requiring distinct elements of justification on the part of school authorities for going beyond a search of outer clothing and belongings.</p>
<p id="b422-6">Savana’s subjective expectation of privacy against such a search is inherent in her account of it as embarrassing, <page-number citation-index="1" label="375">*375</page-number>frightening, and humiliating. The reasonableness of her expectation (required by the Fourth Amendment standard) is indicated by the consistent experiences of other young people similarly searched, whose adolescent vulnerability intensifies the patent intrusiveness of the exposure. See Brief for National Association of Social Workers et al. as <em>Amici Curiae </em>6-14; Hyman &amp; Perone, The Other Side of School Violence: Educator Policies and Practices that may Contribute to Student Misbehavior, 36 J. School Psychology 7, 13 (1998) (strip search can “result in serious emotional damage”). The common reaction of these adolescents simply registers the obviously different meaning of a search exposing the body from the experience of nakedness or near undress in other school circumstances. Changing for gym is getting ready for play; exposing for a search is responding to an accusation reserved for suspected wrongdoers and fairly understood as so degrading that a number of communities have decided that strip searches in schools are never reasonable and have banned them no matter what the facts may be, see, <em>e.g., </em>New York City Dept. of Education, Reg. No. A-432, p. 2 (2005), online at http://docs.nycenet.edu/docushare/dsweb/Get/Document-21/A-432.pdf (“Under no circumstances shall a strip-search of a student be conducted”).</p>
<p id="b423-5">The indignity of the search does not, of course, outlaw it, but it does implicate the rule of reasonableness as stated in <em>T. L. O., </em>that “the search as actually conducted [be] reasonably related in scope to the circumstances which justified the interference in the first place.” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#341" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 341</a></span> (internal quotation marks omitted). The scope will be permissible, that is, when it is “not excessively intrusive in light of the age and sex of the student and the nature of the infraction.” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#342" aria-description="Citation for case: New Jersey v. T. L. O."><em>Id., </em>at 342</a></span>.</p>
<p id="b423-6">Here, the content of the suspicion failed to match the degree of intrusion. Wilson knew beforehand that the pills were prescription-strength ibuprofen and over-the-counter naproxen, common pain relievers equivalent to two Advil, or <page-number citation-index="1" label="376">*376</page-number>one Aleve.<footnotemark>4</footnotemark> He must have been aware of the nature and limited threat of the specific drugs he was searching for, and while just about anything can be taken in quantities that will do real harm, Wilson had no reason to suspect that large amounts of the drugs were being passed around, or that individual students were receiving great numbers of pills.</p>
<p id="b424-4">Nor could Wilson have suspected that Savana was hiding common painkillers in her underwear. Petitioners suggest, as a truth universally acknowledged, that “students ... hid[e] contraband in or under their clothing,” Reply Brief for Petitioners 8, and cite a smattering of eases of students with contraband in their underwear, <em>id., </em>at 8-9. But when the categorically extreme intrusiveness of a search down to the body of an adolescent requires some justification in suspected facts, general background possibilities fall short; a reasonable search that extensive calls for suspicion that it will pay off. But nondangerous school contraband does not raise the specter of stashes in intimate places, and there is no evidence in the record of any general practice among Safford Middle School students of hiding that sort of thing in underwear; neither Jordan nor Marissa suggested to Wilson that Savana was doing that, and the preceding search of Marissa that Wilson ordered yielded nothing. Wilson never even determined when Marissa had received the pills from Savana; if it had been a few days before, that would weigh heavily against any reasonable conclusion that Savana presently had the pills on her person, much less in her underwear.</p>
<p id="b424-5">In sum, what was missing from the suspected facts that pointed to Savana was any indication of danger to the students from the power of the drugs or their quantity, and any reason to suppose that Savana was carrying pills in her <page-number citation-index="1" label="377">*377</page-number>underwear. We think that the combination of these deficiencies was fatal to finding the search reasonable.</p>
<p id="b425-5">In so holding, we mean to cast no ill reflection on the assistant principal, for the record raises no doubt that his motive throughout was to eliminate drugs from his school and protect students from what Jordan Romero had gone through. Parents are known to overreact to protect their children from danger, and a school official with responsibility for safety may tend to do the same. The difference is that the Fourth Amendment places limits on the official, even with the high degree of deference that courts must pay to the educator’s professional judgment.</p>
<p id="b425-6">We do mean, though, to make it clear that the <em>T L. O. </em>concern to limit a school search to reasonable scope requires the support of reasonable suspicion of danger or of resort to underwear for hiding evidence of wrongdoing before a search can reasonably make the quantum leap from outer clothes and backpacks to exposure of intimate parts. The meaning of such a search, and the degradation its subject may reasonably feel, place a search that intrusive in a category of its own demanding its own specific suspicions.</p>
<p id="b425-7">IV</p>
<p id="b425-8">A school official searching a student is “entitled to qualified immunity where clearly established law does not show that the search violated the Fourth Amendment.” <em>Pearson </em>v. <em>Callahan, </em><span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/#243" aria-description="Citation for case: Pearson v. Callahan">555 U. S. 223, 243-244</a></span> (2009). To be established clearly, however, there is no need that “the very action in question [have] previously been held unlawful.” <em>Wilson </em>v. <em>Layne, </em><span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#615" aria-description="Citation for case: Wilson v. Layne">526 U. S. 603, 615</a></span> (1999). The unconstitutionality of outrageous conduct obviously will be unconstitutional, this being the reason, as Judge Posner has said, that “[t]he easiest cases don’t even arise.” <em>K. H. </em>v. <em>Morgan, </em><span class="citation multiple-matches"><a href="/c/F.%202d/914/846/">914 F. 2d 846</a></span>, 851 (CA7 1990). But even as to action less than an outrage, “officials can still be on notice that their conduct violates es<page-number citation-index="1" label="378">*378</page-number>tablished law ... in novel factual circumstances.” <em>Hope </em>v. <em>Pelzer, </em><span class="citation" data-id="9434318"><a href="/opinion/121169/hope-v-pelzer/#741" aria-description="Citation for case: Hope v. Pelzer">536 U. S. 730, 741</a></span> (2002).</p>
<p id="b426-4"><em>T. L. O. </em>directed school officials to limit the intrusiveness of a search, “in light of the age and sex of the student and the nature of the infraction,” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#342" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 342</a></span>, and as we have just said at some length, the intrusiveness of the strip search here cannot be seen as justifiably related to the circumstances. But we realize that the lower courts have reached divergent conclusions regarding how the <em>T L. O. </em>standard applies to such searches.</p>
<p id="b426-5">A number of judges have read <em>T L. O. </em>as the en banc minority of the Ninth Circuit did here. The Sixth Circuit upheld a strip search of a high school student for a drug, without any suspicion that drugs were hidden next to her body. <em>Williams </em>v. <em>Ellington, </em><span class="citation" data-id="563694"><a href="/opinion/563694/angela-lee-williams-a-minor-by-her-father-and-next-friend-william-hardy/#882" aria-description="Citation for case: Angela Lee Williams, a Minor, by Her Father and Next...">936 F. 2d 881, 882-883, 887</a></span> (1991). And other courts considering qualified immunity for strip searches have read <em>T. L. O. </em>as “a series of abstractions, on the one hand, and a declaration of seeming deference to the judgments of school officials, on the other,” <em>Jenkins </em>v. <em>Talladega City Bd. of Ed., </em><span class="citation multiple-matches"><a href="/c/F.%203d/115/821/">115 F. 3d 821</a></span>, 828 (CA11 1997) (en banc), which made it impossible “to establish clearly the contours of a Fourth Amendment right... [in] the wide variety of possible school settings different from those involved in <em>T. L. </em>O.” itself, <em>ibid. </em>See also <em>Thomas </em>v. <em>Roberts, </em><span class="citation multiple-matches"><a href="/c/F.%203d/323/950/">323 F. 3d 950</a></span> (CA11 2003) (granting qualified immunity to a teacher and police officer who conducted a group strip search of a fifth grade class when looking for a missing $26).</p>
<p id="b426-6">We think these differences of opinion from our own are substantial enough to require immunity for the school officials in this case. We would not suggest that entitlement to qualified immunity is the guaranteed product of disuniform views of the law in the other federal, or state, courts, and the fact that a single judge, or even a group of judges, disagrees about the contours of a right does not automatically render the law unclear if we have been clear. That said, however, the cases viewing school strip searches differently <page-number citation-index="1" label="379">*379</page-number>from the way we see them are numerous enough, with well-reasoned majority and dissenting opinions, to counsel doubt that we were sufficiently clear in the prior statement of law. We conclude that qualified immunity is warranted.</p>
<p id="b427-5">V</p>
<p id="b427-6">The strip search of Savana Redding was unreasonable and a violation of the Fourth Amendment, but petitioners Wilson, Romero, and Schwallier are nevertheless protected from liability through qualified immunity. Our conclusions here do not resolve, however, the question of the liability of petitioner Safford Unified School District #1 under <em>Monell </em>v. <em>New York City Dept. of Social Servs., </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658, 694</a></span> (1978), a claim the Ninth Circuit did not address. The judgment of the Ninth Circuit is therefore affirmed in part and reversed in part, and this case .is remanded for consideration of the <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>claim.</p>
<p id="b427-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b419-9"> When the object of a school search is the enforcement of a school rule, a valid search assumes, of course, the rule’s legitimacy. But the legitimacy of the rule usually goes without saying as it does here. The Court said plainly in <em>New Jersey </em>v. <em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#342" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 342, n. 9</a></span> (1985), that standards of conduct for schools are for school administrators to determine ■without second-guessing by courts lacking the experience to appreciate what may be needed. Except in patently arbitrary instances, Fourth <page-number citation-index="1" label="372">*372</page-number>Amendment analysis takes the rule as a given, as it obviously should do in this ease. There is no need here either to explain the imperative of keeping drugs out of schools, or to explain the reasons for the school’s rule banning all drugs, no matter how benign, without advance permission. Teachers are not pharmacologists trained to identify pills and powders, and an effective drug ban has to be enforceable fast. The plenary ban makes sense, and there is no basis to claim that the search was unreasonable owing to some defect or shortcoming of the rule it was aimed at enforcing.</p>
</footnote>
<footnote label="2">
<p id="b421-7"> Poison control centers across the country maintain 24-hour help hotlines to provide “immediate access to poison exposure management instructions and information on potential poisons.” American Association of Poison Control Centers, online at http://www.aapcc.org/dnn/About/ tabid/74/Default.aspx (all Internet materials as visited June 19, 2009, and available in Clerk of Court’s ease file).</p>
</footnote>
<footnote label="3">
<p id="b421-13"> There is no question here that justification for the school officials’ search was required in accordance with the <em>T. L. O. </em>standard of reasonable suspicion, for it is common ground that Savana had a reasonable expectation of privacy covering the personal things she chose to carry in her backpack, cf. <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#339" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 339</a></span>, and that Wilson’s decision to look through it was a “search” within the meaning of the Fourth Amendment.</p>
</footnote>
<footnote label="4">
<p id="b424-6"> An Advil tablet, caplet, or gel caplet contains 200 mg ibuprofen. See 2007 Physicians’ Desk Reference for Nonprescription Drugs, Dietary Supplements, and Herbs 674 (28th ed. 2006). An Aleve caplet contains 200 mg naproxen and 20 mg sodium. See <em>id., </em>at 675.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Salinas v. Texas.md  (`case`, 5 assertions)

### content_page

```
---
title: "Salinas v. Texas"
type: case
citation: ""
parallel_cite: "133 S. Ct. 2174; 186 L. Ed. 2d 376; 570 U.S. 178; 81 U.S.L.W. 4467; 24 Fla. L. Weekly Fed. S 294"
neutral_cite: "2013 U.S. LEXIS 4697; 2013 WL 2922119"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2013
date_decided: 2013-06-17
docket: 12-246
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2013-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Salinas v. Texas
  varies_by_point: false
  scope_note: "Fractured 5-4 (Alito plurality of three; Thomas & Scalia concurring in the judgment on a broader ground). The express-invocation holding governs."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/903977/salinas-v-texas/"
  cluster_id: 903977
  opinion_id: 903977
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny"
related: ["[[Berghuis v. Thompkins]]", "[[Doyle v. Ohio]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "self-incrimination", "silence", "invocation", "pre-custody"]
holding: "Pre-custody, pre-Miranda silence during voluntary, noncustodial questioning is not protected by the Fifth Amendment unless the suspect expressly invokes the privilege; a suspect who simply falls silent without invoking may have that silence used against him at trial."
lake:
  record_id: Salinas v. Texas
  status: verified
  projected_at: 2026-07-06
---

# Salinas v. Texas

*570 U.S. 178 (2013)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Salinas voluntarily went to the police station and answered questions about a double murder; he was not under arrest and had not been given [[Miranda and Custodial Interrogation|Miranda warnings]]. When an officer asked whether shotgun shells found at the scene would match his gun, Salinas said nothing — he looked down, shuffled his feet, and bit his lip. At his murder trial the prosecutor used his silence and reaction as evidence of guilt. Salinas argued this violated his Fifth Amendment privilege against self-incrimination.

## Issue
Whether the Fifth Amendment bars the prosecution from using, as evidence of guilt, a suspect's silence during voluntary, noncustodial police questioning where the suspect did not expressly invoke the privilege against self-incrimination.

## Rule
No — absent an express invocation, the silence is not protected. The privilege is generally not self-executing: a witness who wants its protection ordinarily must claim it. "A witness does not expressly invoke the privilege by standing mute." — 133 S. Ct. at 2179 (plurality opinion). ^pin-2179

The plurality held that Salinas's "Fifth Amendment claim fails because he did not expressly invoke the privilege against self-incrimination" in response to the officer's question. — 133 S. Ct. at 2178 (plurality opinion). ^pin-2178

The express-invocation requirement applies even when the questioner has reason to suspect the answer would be incriminating; the recognized exceptions (a criminal defendant's silence at his own trial under *[[Griffin v. Wisconsin|Griffin]]*, and silence in the face of official compulsion) did not reach Salinas's voluntary, noncustodial silence.

## Application
Salinas was free to leave and was not subjected to the compulsion that excuses an express claim of the privilege. He simply went quiet when asked about the shells, never telling officers he was relying on the Fifth Amendment. Because he did not invoke the privilege when he could have, his silence fell outside the *[[Griffin v. Wisconsin|Griffin]]* no-comment rule, and the State could use it against him. (Justices Thomas and Scalia concurred in the judgment on the broader ground that comment on precustodial silence does not compel self-incrimination at all.)

## Conclusion
A suspect must expressly invoke the Fifth Amendment to keep his precustodial, pre-*[[Miranda v. Arizona|Miranda]]* silence out of evidence; Salinas did not, so the conviction stood. The Texas court's judgment was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Consistent with [[Berghuis v. Thompkins]] (a suspect must unambiguously invoke even the right to remain silent). Distinguish [[Doyle v. Ohio]], which protects **post**-arrest, **post**-*[[Miranda v. Arizona|Miranda]]* silence; *Salinas* concerns **pre**-custody silence with no invocation.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny*

## Sources
- *Salinas v. Texas*, 570 U.S. 178 (2013) — https://www.courtlistener.com/opinion/903977/salinas-v-texas/ — pinpoints: 133 S. Ct. at 2178–2179 (plurality opinion). (CourtListener's plurality text carries S. Ct. star-pagination; U.S. Reports cite 570 U.S. 178.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "07075c076758ae7e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2013 U.S. LEXIS 4697; 2013 WL 2922119", "official_citation_present": false, "parallel_cite": "133 S. Ct. 2174; 186 L. Ed. 2d 376; 570 U.S. 178; 81 U.S.L.W. 4467; 24 Fla. L. Weekly Fed. S 294", "title": "Salinas v. Texas", "year": "2013"}}
{"assertion_id": "5b318ef362aacce5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Pre-custody, pre-Miranda silence during voluntary, noncustodial questioning is not protected by the Fifth Amendment unless the suspect expressly invokes the privilege; a suspect who simply falls silent without invoking may have that silence used against him at trial.", "title": "Salinas v. Texas"}}
{"assertion_id": "8f300ff9b832b613", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny", "title": "Salinas v. Texas"}}
{"assertion_id": "aae0edfd72f98b33", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Salinas v. Texas"}}
{"assertion_id": "c65fca86350164c2", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2013-06-17", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Salinas v. Texas", "field_i_validity": "good_law", "scope_note": "Fractured 5-4 (Alito plurality of three; Thomas & Scalia concurring in the judgment on a broader ground). The express-invocation holding governs.", "title": "Salinas v. Texas", "varies_by_point": "false"}}
```

### lake record — Salinas v. Texas

```json
{
  "schema_version": "s2.v1",
  "record_id": "Salinas v. Texas",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Salinas v. Texas",
    "case_name_short": "",
    "case_name_full": "Genovevo SALINAS, Petitioner v. TEXAS.",
    "input_case_name": "Salinas v. Texas",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2013-06-17",
    "year": 2013,
    "docket": "12-246",
    "cluster_id": 903977,
    "lead_opinion_id": 903977,
    "sibling_ids": [
      903977
    ],
    "absolute_url": "/opinion/903977/salinas-v-texas/",
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
        "cite": "133 S. Ct. 2174",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "2174",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "186 L. Ed. 2d 376",
        "volume": "186",
        "reporter": "L. Ed. 2d",
        "page": "376",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "570 U.S. 178",
        "volume": "570",
        "reporter": "U.S.",
        "page": "178",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 U.S.L.W. 4467",
        "volume": "81",
        "reporter": "U.S.L.W.",
        "page": "4467",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 294",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "294",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2013 U.S. LEXIS 4697",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "4697",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 WL 2922119",
        "volume": "2013",
        "reporter": "WL",
        "page": "2922119",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "133 S. Ct. 2174",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "2174",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "186 L. Ed. 2d 376",
        "volume": "186",
        "reporter": "L. Ed. 2d",
        "page": "376",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 U.S. LEXIS 4697",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "4697",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "570 U.S. 178",
        "volume": "570",
        "reporter": "U.S.",
        "page": "178",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 U.S.L.W. 4467",
        "volume": "81",
        "reporter": "U.S.L.W.",
        "page": "4467",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 294",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "294",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 WL 2922119",
        "volume": "2013",
        "reporter": "WL",
        "page": "2922119",
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
      "id": "pin-2179",
      "page": null,
      "quote": "--- # Salinas v. Texas *570 U.S. 178 (2013)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Salinas voluntarily went to the police station and answered questions about a double murder; he was not under arrest and had not been given Miranda warnings. When an officer asked whether shotgun shells found at the scene would match his gun, Salinas said nothing \u2014 he looked down, shuffled his feet, and bit his lip. At his murder trial the prosecutor used his silence and reaction as evidence of guilt. Salinas argued this violated his Fifth Amendment privilege against self-incrimination. ## Issue Whether the Fifth Amendment bars the prosecution from using, as evidence of guilt, a suspect's silence during voluntary, noncustodial police questioning where the suspect did not expressly invoke the privilege against self-incrimination. ## Rule No \u2014 absent an express invocation, the silence is not protected. The privilege is generally not self-executing: a witness who wants its protection ordinarily must claim it.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-2178",
      "page": null,
      "quote": "Fifth Amendment claim fails because he did not expressly invoke the privilege against self-incrimination",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2013-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Salinas v. Texas",
    "varies_by_point": false,
    "scope_note": "Fractured 5-4 (Alito plurality of three; Thomas & Scalia concurring in the judgment on a broader ground). The express-invocation holding governs.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Orr",
          "cluster_id": 10367163,
          "cite": [
            "305 Ga. 729"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane1_negative"
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
        "journal_ref": "Salinas v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Richared E. Ladue",
          "cluster_id": 4489460,
          "cite": [
            "168 A.3d 430",
            "2017 VT 20",
            "2017 Vt. LEXIS 23"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Adam John Lilienthal",
          "cluster_id": 4345669,
          "cite": [
            "889 N.W.2d 780",
            "2017 WL 432937",
            "2017 Minn. LEXIS 50"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Washington v. Sergio Magana, Jr.",
          "cluster_id": 4331725,
          "cite": [
            "197 Wash. App. 189",
            "389 P.3d 654"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Samuel Williams v. Christopher Epps",
          "cluster_id": 2821157,
          "cite": [
            "797 F.3d 276",
            "2015 WL 4546858"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mark Douglas Robison v. State",
          "cluster_id": 2772649,
          "cite": [
            "461 S.W.3d 194"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth, Aplt. v. Molina, M.",
          "cluster_id": 2753817,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth, Aplt. v. Molina, M.",
          "cluster_id": 2753816,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Sessoms v. Grounds",
          "cluster_id": 8442084,
          "cite": [
            "776 F.3d 615",
            "2015 WL 294273"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Tio Sessoms v. D Runnels",
          "cluster_id": 2736109,
          "cite": [
            "768 F.3d 882",
            "2014 U.S. App. LEXIS 18237",
            "2014 WL 4668005"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Tom",
          "cluster_id": 2718098,
          "cite": [
            "59 Cal. 4th 1210",
            "331 P.3d 303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Medunjanin",
          "cluster_id": 2675041,
          "cite": [
            "752 F.3d 576",
            "2014 U.S. App. LEXIS 9306",
            "2014 WL 2054016"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Jessie Dotson",
          "cluster_id": 2738561,
          "cite": [
            "450 S.W.3d 1",
            "2014 Tenn. LEXIS 694"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "BOSSE v. STATE",
          "cluster_id": 4438014,
          "cite": [
            "400 P.3d 834",
            "2017 OK CR 10",
            "2017 WL 2376976",
            "2017 Okla. Crim. App. LEXIS 11"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knapp",
          "cluster_id": 2649391,
          "cite": [
            "73 M.J. 33",
            "2014 WL 184989",
            "2014 CAAF LEXIS 54"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "BOSSE v. STATE",
          "cluster_id": 4396433,
          "cite": [
            "2017 OK CR 10"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth, Aplt. v. Molina, M.",
          "cluster_id": 2753815,
          "cite": [
            "104 A.3d 430",
            "628 Pa. 465",
            "2014 Pa. LEXIS 3035"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leo Abby v. Carol Howe",
          "cluster_id": 2651692,
          "cite": [
            "742 F.3d 221",
            "2014 WL 321866",
            "2014 U.S. App. LEXIS 1842"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Adams, S., Aplt.",
          "cluster_id": 2753839,
          "cite": [
            "104 A.3d 511",
            "628 Pa. 600",
            "2014 Pa. LEXIS 3041"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mario Wilchcombe",
          "cluster_id": 4302304,
          "cite": [
            "838 F.3d 1179",
            "2016 U.S. App. LEXIS 17971",
            "2016 WL 5750924"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Cruz Buentello v. State",
          "cluster_id": 4329019,
          "cite": [
            "512 S.W.3d 508",
            "2016 WL 7164021",
            "2016 Tex. App. LEXIS 13030"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Torres. ICA s.d.o., filed 05/23/2018, 142 Haw. 355.",
          "cluster_id": 4608716,
          "cite": [
            "439 P.3d 234"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Jason M. Lovejoy",
          "cluster_id": 2679907,
          "cite": [
            "2014 ME 48",
            "89 A.3d 1066",
            "2014 WL 1257079",
            "2014 Me. LEXIS 55"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Rondon Athayde",
          "cluster_id": 6621361,
          "cite": [
            "277 A.3d 387",
            "2022 ME 41"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Florida v. Donna Horwitz",
          "cluster_id": 3200851,
          "cite": [
            "191 So. 3d 429",
            "41 Fla. L. Weekly Supp. 211",
            "2016 WL 2586307",
            "2016 Fla. LEXIS 955"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Okatan",
          "cluster_id": 1038349,
          "cite": [
            "728 F.3d 111",
            "2013 WL 4504587"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Schiller-Munneman",
          "cluster_id": 3218962,
          "cite": [
            "359 Or. 808",
            "377 P.3d 554",
            "2016 Ore. LEXIS 404"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "BOSSE v. STATE",
          "cluster_id": 3132663,
          "cite": [
            "2015 OK CR 14",
            "360 P.3d 1203",
            "2015 Okla. Crim. App. LEXIS 14",
            "2015 WL 6143204"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Stevens",
          "cluster_id": 2772763,
          "cite": [
            "2014 IL 116300"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Salinas v. Texas:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(903977) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 107,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 13,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 107,
        "triage_read": 13,
        "triage_snippet_classified": 94
      },
      "lane2_top_cited": {
        "query": "cites:(903977)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04JnM9MjY5MjI5MCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28903977%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(903977)",
        "reviewed": 25,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 25,
        "triage_read": 0,
        "triage_snippet_classified": 25
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(903977)",
    "indexed_citing_opinions": 118,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 903977,
        "count": 118,
        "count_source": "search"
      }
    ],
    "citation_count": 293,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/salinas-v-texas.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyNDc4MyZzPTkzOTYxNDkmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28903977%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 903977,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 100991,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 101083,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 104849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 104912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 105305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 106393,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 107336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 107606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 107607,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 107934,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 108033,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 108066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 108882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 109400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 109491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 109683,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 110234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 110298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 110426,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 110832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 111105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 112464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 117863,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 118168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 118278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 137003,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 147529,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 173867,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 316702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 387369,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 568540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 577243,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 599386,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 689174,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 694385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 903977,
        "cited_id": 733232,
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
    "date_created": "2026-07-05T18:30:51Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T18:31:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:31:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T18:34:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:31:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Salinas v. Texas

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

                            SALINAS v. TEXAS

CERTIORARI TO THE COURT OF CRIMINAL APPEALS OF TEXAS

            No. 12–246.      Argued April 17, 2013—Decided June 17, 2013
Petitioner, without being placed in custody or receiving Miranda warn-
  ings, voluntarily answered some of a police officer’s questions about a
  murder, but fell silent when asked whether ballistics testing would
  match his shotgun to shell casings found at the scene of the crime. At
  petitioner’s murder trial in Texas state court, and over his objection,
  the prosecution used his failure to answer the question as evidence of
  guilt. He was convicted, and both the State Court of Appeals and
  Court of Criminal Appeals affirmed, rejecting his claim that the pros-
  ecution’s use of his silence in its case in chief violated the Fifth
  Amendment.
Held: The judgment is affirmed.
369 S. W. 3d 176, affirmed.
     JUSTICE ALITO, joined by THE CHIEF JUSTICE and JUSTICE KENNEDY,
  concluded that petitioner’s Fifth Amendment claim fails because he
  did not expressly invoke the privilege in response to the officer’s
  question. Pp. 3−12.
     (a) To prevent the privilege against self-incrimination from shield-
  ing information not properly within its scope, a witness who “ ‘desires
  the protection of the privilege . . . must claim it’ ” at the time he relies
  on it. Minnesota v. Murphy, 465 U. S. 420, 427. This Court has rec-
  ognized two exceptions to that requirement. First, a criminal de-
  fendant need not take the stand and assert the privilege at his own
  trial. Griffin v. California, 380 U. S. 609, 613–615. Petitioner’s si-
  lence falls outside this exception because he had no comparable un-
  qualified right not to speak during his police interview. Second, a
  witness’ failure to invoke the privilege against self-incrimination
  must be excused where governmental coercion makes his forfeiture of
  the privilege involuntary. See, e.g., Miranda v. Arizona, 384 U. S.
  436, 467−468, and n. 37. Petitioner cannot benefit from this principle
2                            SALINAS v. TEXAS

                                   Syllabus

    because it is undisputed that he agreed to accompany the officers to
    the station and was free to leave at any time. Pp. 3−6.
       (b) Petitioner seeks a third exception to the express invocation re-
    quirement for cases where the witness chooses to stand mute rather
    than give an answer that officials suspect would be incriminating,
    but this Court’s cases all but foreclose that argument. A defendant
    normally does not invoke the privilege by remaining silent. See Rob-
    erts v. United States, 445 U. S. 552, 560. And the express invocation
    requirement applies even when an official has reason to suspect that
    the answer to his question would incriminate the witness. See Mur-
    phy, supra, at 427−428. For the same reasons that neither a witness’
    silence nor official suspicion is sufficient by itself to relieve a witness
    of the obligation to expressly invoke the privilege, they do not do so
    together. The proposed exception also would be difficult to reconcile
    with Berghuis v. Thompkins, 560 U. S. 370, where this Court held in
    the closely related context of post-Miranda silence that a defendant
    failed to invoke his right to cut off police questioning when he re-
    mained silent for 2 hours and 45 minutes. Id., at ___.
       Petitioner claims that reliance on the Fifth Amendment privilege is
    the most likely explanation for silence in a case like his, but such si-
    lence is “insolubly ambiguous.” See Doyle v. Ohio, 426 U. S. 610, 617.
    To be sure, petitioner might have declined to answer the officer’s
    question in reliance on his constitutional privilege. But he also might
    have done so because he was trying to think of a good lie, because he
    was embarrassed, or because he was protecting someone else. Not
    every such possible explanation for silence is probative of guilt, but
    neither is every possible explanation protected by the Fifth Amend-
    ment. Petitioner also suggests that it would be unfair to require a
    suspect unschooled in the particulars of legal doctrine to do anything
    more than remain silent in order to invoke his “right to remain si-
    lent.” But the Fifth Amendment guarantees that no one may be
    “compelled in any criminal case to be a witness against himself,” not
    an unqualified “right to remain silent.” In any event, it is settled
    that forfeiture of the privilege against self-incrimination need not be
    knowing. Murphy, 465 U. S., at 427–428. Pp. 6−10.
       (c) Petitioner’s argument that applying the express invocation re-
    quirement in this context will be unworkable is also unpersuasive.
    The Court has long required defendants to assert the privilege in or-
    der to subsequently benefit from it, and this rule has not proved diffi-
    cult to apply in practice. Pp. 10−12.
       JUSTICE THOMAS, joined by JUSTICE SCALIA, concluded that peti-
    tioner’s claim would fail even if he invoked the privilege because the
    prosecutor’s comments regarding his precustodial silence did not
    compel him to give self-incriminating testimony. Griffin v. Califor-
                     Cite as: 570 U. S. ____ (2013)                      3

                                Syllabus

  nia, 380 U. S. 609, in which this Court held that the Fifth Amend-
  ment prohibits a prosecutor or judge from commenting on a defend-
  ant’s failure to testify, should not be extended to a defendant’s silence
  during a precustodial interview because Griffin “lacks foundation in
  the Constitution’s text, history, or logic.” See Mitchell v. United
  States, 526 U. S. 314, 341 (THOMAS, J., dissenting). Pp. 1−2.

   ALITO, J., announced the judgment of the Court and delivered an
opinion, in which ROBERTS, C. J., and KENNEDY, J., joined. THOMAS, J.,
filed an opinion concurring in the judgment, in which SCALIA, J., joined.
BREYER, J., filed a dissenting opinion, in which GINSBURG, SOTOMAYOR,
and KAGAN, JJ., joined.
                        Cite as: 570 U. S. ____ (2013)                              1

                              Opinion of ALITO, J.

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 12–246
                                   _________________


    GENOVEVO SALINAS, PETITIONER v. TEXAS
    ON WRIT OF CERTIORARI TO THE COURT OF CRIMINAL

                   APPEALS OF TEXAS

                                 [June 17, 2013] 


   JUSTICE ALITO announced the judgment of the Court
and delivered an opinion in which THE CHIEF JUSTICE and
JUSTICE KENNEDY join.
   Without being placed in custody or receiving Miranda
warnings, petitioner voluntarily answered the questions
of a police officer who was investigating a murder. But
petitioner balked when the officer asked whether a ballis-
tics test would show that the shell casings found at the
crime scene would match petitioner’s shotgun. Petitioner
was subsequently charged with murder, and at trial pros-
ecutors argued that his reaction to the officer’s question
suggested that he was guilty. Petitioner claims that this
argument violated the Fifth Amendment, which guaran-
tees that “[n]o person . . . shall be compelled in any crimi-
nal case to be a witness against himself.”
   Petitioner’s Fifth Amendment claim fails because he
did not expressly invoke the privilege against self-
incrimination in response to the officer’s question. It has
long been settled that the privilege “generally is not self-
executing” and that a witness who desires its protection
“ ‘must claim it.’ ” Minnesota v. Murphy, 465 U. S. 420,
425, 427 (1984) (quoting United States v. Monia, 317 U. S.
2                     SALINAS v. TEXAS

                       Opinion of ALITO, J.

424, 427 (1943)). Although “no ritualistic formula is nec-
essary in order to invoke the privilege,” Quinn v. United
States, 349 U. S. 155, 164 (1955), a witness does not do so
by simply standing mute. Because petitioner was required
to assert the privilege in order to benefit from it, the
judgment of the Texas Court of Criminal Appeals rejecting
petitioner’s Fifth Amendment claim is affirmed.
                                I
  On the morning of December 18, 1992, two brothers
were shot and killed in their Houston home. There were
no witnesses to the murders, but a neighbor who heard
gunshots saw someone run out of the house and speed
away in a dark-colored car. Police recovered six shotgun
shell casings at the scene. The investigation led police to
petitioner, who had been a guest at a party the victims
hosted the night before they were killed. Police visited
petitioner at his home, where they saw a dark blue car in
the driveway. He agreed to hand over his shotgun for
ballistics testing and to accompany police to the station
for questioning.
  Petitioner’s interview with the police lasted approxi-
mately one hour. All agree that the interview was noncusto-
dial, and the parties litigated this case on the assumption
that he was not read Miranda warnings. See Mi-
randa v. Arizona, 384 U. S. 436 (1966). For most of the
interview, petitioner answered the officer’s questions. But
when asked whether his shotgun “would match the shells
recovered at the scene of the murder,” App. 17, petitioner
declined to answer. Instead, petitioner “[l]ooked down at
the floor, shuffled his feet, bit his bottom lip, cl[e]nched his
hands in his lap, [and] began to tighten up.” Id., at 18.
After a few moments of silence, the officer asked addition-
al questions, which petitioner answered. Ibid.
  Following the interview, police arrested petitioner on
outstanding traffic warrants. Prosecutors soon concluded
                 Cite as: 570 U. S. ____ (2013)            3

                      Opinion of ALITO, J.

that there was insufficient evidence to charge him with
the murders, and he was released. A few days later, police
obtained a statement from a man who said he had heard
petitioner confess to the killings. On the strength of
that additional evidence, prosecutors decided to charge peti-
tioner, but by this time he had absconded. In 2007, police
discovered petitioner living in the Houston area under an
assumed name.
   Petitioner did not testify at trial. Over his objection,
prosecutors used his reaction to the officer’s question dur-
ing the 1993 interview as evidence of his guilt. The jury
found petitioner guilty, and he received a 20-year sen-
tence. On direct appeal to the Court of Appeals of
Texas, petitioner argued that prosecutors’ use of his si-
lence as part of their case in chief violated the Fifth
Amendment. The Court of Appeals rejected that argu-
ment, reasoning that petitioner’s prearrest, pre-Miranda
silence was not “compelled” within the meaning of the
Fifth Amendment. 368 S. W. 3d 550, 557–559 (2011). The
Texas Court of Criminal Appeals took up this case and
affirmed on the same ground. 369 S. W. 3d 176 (2012).
   We granted certiorari, 568 U. S. ___ (2013), to resolve
a division of authority in the lower courts over whether
the prosecution may use a defendant’s assertion of the
privilege against self-incrimination during a noncustodial
police interview as part of its case in chief. Compare, e.g.,
United States v. Rivera, 944 F. 2d 1563, 1568 (CA11 1991),
with United States v. Moore, 104 F. 3d 377, 386 (CADC
1997). But because petitioner did not invoke the privilege
during his interview, we find it unnecessary to reach that
question.
                             II
                              A
  The privilege against self-incrimination “is an exception
to the general principle that the Government has the right
4                     SALINAS v. TEXAS

                       Opinion of ALITO, J.

to everyone’s testimony.” Garner v. United States, 424
U. S. 648, 658, n. 11 (1976). To prevent the privilege from
shielding information not properly within its scope, we
have long held that a witness who “ ‘desires the protection
of the privilege . . . must claim it’ ” at the time he relies on
it. Murphy, 465 U. S., at 427 (quoting Monia, 317 U. S., at
427). See also United States ex rel. Vajtauer v. Commis-
sioner of Immigration, 273 U. S. 103, 113 (1927).
   That requirement ensures that the Government is put
on notice when a witness intends to rely on the privilege
so that it may either argue that the testimony sought
could not be self-incriminating, see Hoffman v. United
States, 341 U. S. 479, 486 (1951), or cure any potential
self-incrimination through a grant of immunity, see Kasti-
gar v. United States, 406 U. S. 441, 448 (1972). The ex-
press invocation requirement also gives courts tasked with
evaluating a Fifth Amendment claim a contemporaneous
record establishing the witness’ reasons for refusing to
answer. See Roberts v. United States, 445 U. S. 552, 560,
n. 7 (1980) (“A witness may not employ the privilege to
avoid giving testimony that he simply would prefer not
to give”); Hutcheson v. United States, 369 U. S. 599, 610–
611 (1962) (declining to treat invocation of due process as
proper assertion of the privilege). In these ways, insisting
that witnesses expressly invoke the privilege “assures that
the Government obtains all the information to which it is
entitled.” Garner, supra, at 658, n. 11.
   We have previously recognized two exceptions to the
requirement that witnesses invoke the privilege, but
neither applies here. First, we held in Griffin v. Califor-
nia, 380 U. S. 609, 613–615 (1965), that a criminal de-
fendant need not take the stand and assert the privilege at
his own trial. That exception reflects the fact that a crim-
inal defendant has an “absolute right not to testify.”
Turner v. United States, 396 U. S. 398, 433 (1970) (Black,
J., dissenting); see United States v. Patane, 542 U. S. 630,
                  Cite as: 570 U. S. ____ (2013)            5

                       Opinion of ALITO, J.

637 (2004) (plurality opinion). Since a defendant’s reasons
for remaining silent at trial are irrelevant to his constitu-
tional right to do so, requiring that he expressly invoke
the privilege would serve no purpose; neither a showing
that his testimony would not be self-incriminating nor a
grant of immunity could force him to speak. Because pe-
titioner had no comparable unqualified right during his
interview with police, his silence falls outside the Griffin
exception.
   Second, we have held that a witness’ failure to invoke
the privilege must be excused where governmental coer-
cion makes his forfeiture of the privilege involuntary.
Thus, in Miranda, we said that a suspect who is subjected
to the “inherently compelling pressures” of an unwarned
custodial interrogation need not invoke the privilege. 384
U. S., at 467–468, and n. 37. Due to the uniquely coercive
nature of custodial interrogation, a suspect in custody
cannot be said to have voluntarily forgone the privilege
“unless [he] fails to claim [it] after being suitably warned.”
Murphy, supra, at 429–430.
   For similar reasons, we have held that threats to with-
draw a governmental benefit such as public employment
sometimes make exercise of the privilege so costly that it
need not be affirmatively asserted. Garrity v. New Jersey,
385 U. S. 493, 497 (1967) (public employment). See also
Lefkowitz v. Cunningham, 431 U. S. 801, 802–804 (1977)
(public office); Lefkowitz v. Turley, 414 U. S. 70, 84–85
(1973) (public contracts). And where assertion of the
privilege would itself tend to incriminate, we have allowed
witnesses to exercise the privilege through silence. See,
e.g., Leary v. United States, 395 U. S. 6, 28–29 (1969) (no
requirement that taxpayer complete tax form where doing
so would have revealed income from illegal activities);
Albertson v. Subversive Activities Control Bd., 382 U. S.
70, 77–79 (1965) (members of the Communist Party not
required to complete registration form “where response to
6                    SALINAS v. TEXAS

                      Opinion of ALITO, J.

any of the form’s questions . . . might involve [them] in the
admission of a crucial element of a crime”). The principle
that unites all of those cases is that a witness need not
expressly invoke the privilege where some form of official
compulsion denies him “a ‘free choice to admit, to deny,
or to refuse to answer.’ ” Garner, 424 U. S., at 656–657
(quoting Lisenba v. California, 314 U. S. 219, 241 (1941)).
   Petitioner cannot benefit from that principle because it
is undisputed that his interview with police was volun-
tary. As petitioner himself acknowledges, he agreed to
accompany the officers to the station and “was free to
leave at any time during the interview.” Brief for Peti-
tioner 2–3 (internal quotation marks omitted). That places
petitioner’s situation outside the scope of Miranda and
other cases in which we have held that various forms of
governmental coercion prevented defendants from volun-
tarily invoking the privilege. The dissent elides this point
when it cites our precedents in this area for the proposi-
tion that “[c]ircumstances, rather than explicit invocation,
trigger the protection of the Fifth Amendment.” Post,
at 7–8 (opinion of BREYER, J.). The critical question is
whether, under the “circumstances” of this case, petitioner
was deprived of the ability to voluntarily invoke the Fifth
Amendment. He was not. We have before us no allegation
that petitioner’s failure to assert the privilege was invol-
untary, and it would have been a simple matter for him to
say that he was not answering the officer’s question on
Fifth Amendment grounds. Because he failed to do so, the
prosecution’s use of his noncustodial silence did not violate
the Fifth Amendment.
                             B
   Petitioner urges us to adopt a third exception to the in-
vocation requirement for cases in which a witness stands
mute and thereby declines to give an answer that of-
ficials suspect would be incriminating. Our cases all but
                     Cite as: 570 U. S. ____ (2013)                   7

                          Opinion of ALITO, J.

foreclose such an exception, which would needlessly bur-
den the Government’s interests in obtaining testimony
and prosecuting criminal activity. We therefore decline
petitioner’s invitation to craft a new exception to the
“general rule” that a witness must assert the privilege to
subsequently benefit from it. Murphy, 465 U. S., at 429.
   Our cases establish that a defendant normally does not
invoke the privilege by remaining silent. In Roberts v.
United States, 445 U. S. 552, for example, we rejected the
Fifth Amendment claim of a defendant who remained
silent throughout a police investigation and received a
harsher sentence for his failure to cooperate. In so ruling,
we explained that “if [the defendant] believed that his
failure to cooperate was privileged, he should have said so
at a time when the sentencing court could have deter-
mined whether his claim was legitimate.” Id., at 560. See
also United States v. Sullivan, 274 U. S. 259, 263–264
(1927); Vajtauer, 273 U. S., at 113.1 A witness does not
expressly invoke the privilege by standing mute.
   We have also repeatedly held that the express invoca-
tion requirement applies even when an official has reason
to suspect that the answer to his question would incrim-
inate the witness. Thus, in Murphy we held that the
defendant’s self-incriminating answers to his probation of-
ficer were properly admitted at trial because he failed to
invoke the privilege. 465 U. S., at 427–428. In reaching
that conclusion, we rejected the notion “that a witness
——————
   1 The dissent argues that in these cases “neither the nature of the

questions nor the circumstances of the refusal to answer them provided
any basis to infer a tie between the silence and the Fifth Amendment.”
Post, at 5–6 (opinion of BREYER, J.). But none of our precedents sug-
gests that governmental officials are obliged to guess at the meaning of
a witness’ unexplained silence when implicit reliance on the Fifth
Amendment seems probable. Roberts does not say as much, despite its
holding that the defendant in that case was required to explain the
Fifth Amendment basis for his failure to cooperate with an investiga-
tion that led to his prosecution. 445 U. S., at 559.
8                         SALINAS v. TEXAS

                          Opinion of ALITO, J.

must ‘put the Government on notice by formally availing
himself of the privilege’ only when he alone ‘is reasonably
aware of the incriminating tendency of the questions.’ ”
Id., at 428 (quoting Roberts, supra, at 562, n.* (Brennan,
J., concurring)). See also United States v. Kordel, 397
U. S. 1, 7 (1970).2
   Petitioner does not dispute the vitality of either of those
lines of precedent but instead argues that we should adopt
an exception for cases at their intersection. Thus, peti-
tioner would have us hold that although neither a wit-
ness’ silence nor official suspicions are enough to excuse
the express invocation requirement, the invocation require-
ment does not apply where a witness is silent in the face of
official suspicions. For the same reasons that neither
of those factors is sufficient by itself to relieve a witness of
the obligation to expressly invoke the privilege, we con-
clude that they do not do so together. A contrary result
would do little to protect those genuinely relying on the
Fifth Amendment privilege while placing a needless new
burden on society’s interest in the admission of evidence
that is probative of a criminal defendant’s guilt.
   Petitioner’s proposed exception would also be very diffi-
cult to reconcile with Berghuis v. Thompkins, 560 U. S.
370 (2010). There, we held in the closely related context of
post-Miranda silence that a defendant failed to invoke the
——————
   2 Our cases do not support the distinction the dissent draws between

silence and the failure to invoke the privilege before making incriminat-
ing statements. See post, at 7 (BREYER, J., dissenting). For example,
Murphy, a case in which the witness made incriminating statements
after failing to invoke the privilege, repeatedly relied on Roberts
and Vajtauer—two cases in which witnesses remained silent and did
not make incriminating statements. 465 U. S., at 427, 429, 455–456,
n. 20. Similarly, Kordel cited Vajtauer, among other cases, for the
proposition that the defendant’s “failure at any time to assert the
constitutional privilege leaves him in no position to complain now that
he was compelled to give testimony against himself.” 397 U. S., at 10,
and n. 18.
                    Cite as: 570 U. S. ____ (2013)                   9

                         Opinion of ALITO, J.

privilege when he refused to respond to police questioning
for 2 hours and 45 minutes. 560 U. S., at ___ (slip op., at
3, 8–10). If the extended custodial silence in that case did
not invoke the privilege, then surely the momentary si-
lence in this case did not do so either.
   Petitioner and the dissent attempt to distinguish Berg-
huis by observing that it did not concern the admissi-
bility of the defendant’s silence but instead involved the
admissibility of his subsequent statements. Post, at 8–9
(opinion of BREYER, J.). But regardless of whether prose-
cutors seek to use silence or a confession that follows, the
logic of Berghuis applies with equal force: A suspect who
stands mute has not done enough to put police on notice
that he is relying on his Fifth Amendment privilege.3
   In support of their proposed exception to the invocation
requirement, petitioner and the dissent argue that reli-
ance on the Fifth Amendment privilege is the most likely
explanation for silence in a case such as this one. Reply
Brief 17; see post, at 9–10 (BREYER, J., dissenting). But
whatever the most probable explanation, such silence is
“insolubly ambiguous.” See Doyle, v. Ohio, 426 U. S. 610,
617 (1976). To be sure, someone might decline to answer a
police officer’s question in reliance on his constitutional
privilege. But he also might do so because he is trying to
think of a good lie, because he is embarrassed, or because
he is protecting someone else. Not every such possible
explanation for silence is probative of guilt, but neither is
every possible explanation protected by the Fifth Amend-
ment. Petitioner alone knew why he did not answer the
officer’s question, and it was therefore his “burden . . . to
——————
  3 Petitioner is correct that due process prohibits prosecutors from

pointing to the fact that a defendant was silent after he heard Miranda
warnings, Doyle v. Ohio, 426 U. S. 610, 617–618 (1976), but that rule
does not apply where a suspect has not received the warnings’ implicit
promise that any silence will not be used against him, Jenkins v.
Anderson, 447 U. S. 231, 240 (1980).
10                        SALINAS v. TEXAS

                          Opinion of ALITO, J.

make a timely assertion of the privilege.” Garner, 424
U. S., at 655.
   At oral argument, counsel for petitioner suggested that
it would be unfair to require a suspect unschooled in the
particulars of legal doctrine to do anything more than
remain silent in order to invoke his “right to remain si-
lent.” Tr. of Oral Arg. 26–27; see post, at 10 (BREYER, J.,
dissenting); Michigan v. Tucker, 417 U. S. 433, 439 (1974)
(observing that “virtually every schoolboy is familiar with
the concept, if not the language” of the Fifth Amendment).
But popular misconceptions notwithstanding, the Fifth
Amendment guarantees that no one may be “compelled in
any criminal case to be a witness against himself ”; it does
not establish an unqualified “right to remain silent.” A
witness’ constitutional right to refuse to answer questions
depends on his reasons for doing so, and courts need to
know those reasons to evaluate the merits of a Fifth
Amendment claim. See Hoffman, 341 U. S., at 486–487.4
   In any event, it is settled that forfeiture of the privilege
against self-incrimination need not be knowing. Murphy,
465 U. S., at 427–428; Garner, supra, at 654, n. 9. State-
ments against interest are regularly admitted into evi-
dence at criminal trials, see Fed. Rule of Evid. 804(b)(3),
and there is no good reason to approach a defendant’s
silence any differently.
                               C
     Finally, we are not persuaded by petitioner’s arguments

——————
  4 The dissent suggests that officials in this case had no “special need
to know whether the defendant sought to rely on the protections of the
Fifth Amendment.” Post, at 4 (opinion of BREYER, J.). But we have
never said that the government must demonstrate such a need on a
case-by-case basis for the invocation requirement to apply. Any such
rule would require judicial hypothesizing about the probable strategic
choices of prosecutors, who often use immunity to compel testimony
from witnesses who invoke the Fifth Amendment.
                  Cite as: 570 U. S. ____ (2013)             11

                       Opinion of ALITO, J.

that applying the usual express invocation requirement
where a witness is silent during a noncustodial police
interview will prove unworkable in practice. Petitioner
and the dissent suggest that our approach will “unleash
complicated and persistent litigation” over what a suspect
must say to invoke the privilege, Reply Brief 18; see post,
at 11–12 (opinion of BREYER, J.), but our cases have
long required that a witness assert the privilege to subse-
quently benefit from it. That rule has not proved difficult to
apply. Nor did the potential for close cases dissuade us
from adopting similar invocation requirements for sus-
pects who wish to assert their rights and cut off police
questioning during custodial interviews. Berghuis, 560
U. S., at ___ (slip op., at 8–10) (requiring suspect to unam-
biguously assert privilege against self-incrimination to cut
off custodial questioning); Davis v. United States, 512
U. S. 452, 459 (1994) (same standard for assertions of the
right to counsel).
   Notably, petitioner’s approach would produce its own
line-drawing problems, as this case vividly illustrates.
When the interviewing officer asked petitioner if his
shotgun would match the shell casings found at the crime
scene, petitioner did not merely remain silent; he made
movements that suggested surprise and anxiety. At pre-
cisely what point such reactions transform “silence” into
expressive conduct would be a difficult and recurring
question that our decision allows us to avoid.
   We also reject petitioner’s argument that an express
invocation requirement will encourage police officers to
“ ‘unfairly “tric[k]” ’ ” suspects into cooperating. Reply Brief
21 (quoting South Dakota v. Neville, 459 U. S. 553, 566
(1983)). Petitioner worries that officers could unduly
pressure suspects into talking by telling them that their
silence could be used in a future prosecution. But as
petitioner himself concedes, police officers “have done
nothing wrong” when they “accurately stat[e] the law.”
12                    SALINAS v. TEXAS

                      Opinion of ALITO, J.

Brief for Petitioner 32. We found no constitutional infir-
mity in government officials telling the defendant in Mur-
phy that he was required to speak truthfully to his parole
officer, 465 U. S., at 436–438, and we see no greater dan-
ger in the interview tactics petitioner identifies. So long
as police do not deprive a witness of the ability to volun-
tarily invoke the privilege, there is no Fifth Amendment
violation.
                         *   *     *
  Before petitioner could rely on the privilege against self-
incrimination, he was required to invoke it. Because he
failed to do so, the judgment of the Texas Court of Crimi-
nal Appeals is affirmed.
                                             It is so ordered.
                 Cite as: 570 U. S. ____ (2013)            1

               THOMAS, J., concurring in judgment

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 12–246
                          _________________


    GENOVEVO SALINAS, PETITIONER v. TEXAS
    ON WRIT OF CERTIORARI TO THE COURT OF CRIMINAL

                   APPEALS OF TEXAS

                        [June 17, 2013] 


   JUSTICE THOMAS, with whom JUSTICE SCALIA joins, con-
curring in the judgment.
   We granted certiorari to decide whether the Fifth Amend-
ment privilege against compulsory self-incrimination
prohibits a prosecutor from using a defendant’s pre-
custodial silence as evidence of his guilt. The plurality
avoids reaching that question and instead concludes that
Salinas’ Fifth Amendment claim fails because he did not
expressly invoke the privilege. Ante, at 3. I think there is
a simpler way to resolve this case. In my view, Salinas’
claim would fail even if he had invoked the privilege be-
cause the prosecutor’s comments regarding his precusto-
dial silence did not compel him to give self-incriminating
testimony.
   In Griffin v. California, 380 U. S. 609 (1965), this Court
held that the Fifth Amendment prohibits a prosecutor or
judge from commenting on a defendant’s failure to testify.
Id., at 614. The Court reasoned that such comments, and
any adverse inferences drawn from them, are a “penalty”
imposed on the defendant’s exercise of his Fifth Amend-
ment privilege. Ibid. Salinas argues that we should
extend Griffin’s no-adverse-inference rule to a defendant’s
silence during a precustodial interview. I have previously
explained that the Court’s decision in Griffin “lacks foun-
dation in the Constitution’s text, history, or logic” and
should not be extended. See Mitchell v. United States, 526
2                     SALINAS v. TEXAS

               THOMAS, J., concurring in judgment

U. S. 314, 341 (1999) (dissenting opinion). I adhere to that
view today.
   Griffin is impossible to square with the text of the Fifth
Amendment, which provides that “[n]o person . . . shall be
compelled in any criminal case to be a witness against
himself.” A defendant is not “compelled . . . to be a witness
against himself ” simply because a jury has been told that
it may draw an adverse inference from his silence. See
Mitchell, supra, at 331 (SCALIA, J., dissenting) (“[T]he
threat of an adverse inference does not ‘compel’ anyone to
testify. . . . Indeed, I imagine that in most instances, a
guilty defendant would choose to remain silent despite
the adverse inference, on the theory that it would do
him less damage than his cross-examined testimony”);
Carter v. Kentucky, 450 U. S. 288, 306 (1981) (Powell,
J., concurring) (“[N]othing in the [Self-Incrimination]
Clause requires that jurors not draw logical inferences
when a defendant chooses not to explain incriminating
circumstances”).
   Nor does the history of the Fifth Amendment support
Griffin. At the time of the founding, English and Ameri-
can courts strongly encouraged defendants to give un-
sworn statements and drew adverse inferences when they
failed to do so. See Mitchell, supra, at 332 (SCALIA, J.,
dissenting); Alschuler, A Peculiar Privilege in Historical
Perspective, in The Privilege Against Self-Incrimination
204 (R. Hemholz et al. eds. 1997). Given Griffin’s indefen-
sible foundation, I would not extend it to a defendant’s
silence during a precustodial interview. I agree with the
plurality that Salinas’ Fifth Amendment claim fails and,
therefore, concur in the judgment.
                 Cite as: 570 U. S. ____ (2013)            1

                     BREYER, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 12–246
                         _________________


    GENOVEVO SALINAS, PETITIONER v. TEXAS
    ON WRIT OF CERTIORARI TO THE COURT OF CRIMINAL

                   APPEALS OF TEXAS

                        [June 17, 2013] 


  JUSTICE BREYER, with whom JUSTICE GINSBURG,
JUSTICE SOTOMAYOR, and JUSTICE KAGAN join, dissenting.
  In my view the Fifth Amendment here prohibits the
prosecution from commenting on the petitioner’s silence in
response to police questioning. And I dissent from the
Court’s contrary conclusion.
                               I
   In January 1993, Houston police began to suspect peti-
tioner Genovevo Salinas of having committed two murders
the previous month. They asked Salinas to come to the
police station “to take photographs and to clear him as [a]
suspect.” App. 3. At the station, police took Salinas into
what he describes as “an interview room.” Brief for Peti-
tioner 3. Because he was “free to leave at that time,” App.
14, they did not give him Miranda warnings. The police
then asked Salinas questions. And Salinas answered until
the police asked him whether the shotgun from his home
“would match the shells recovered at the scene of the
murder.” Id., at 17. At that point Salinas fell silent. Ibid.
   Salinas was later tried for, and convicted of, murder. At
closing argument, drawing on testimony he had elicited
earlier, the prosecutor pointed out to the jury that Salinas,
during his earlier questioning at the police station, had
remained silent when asked about the shotgun. The
prosecutor told the jury, among other things, that “ ‘[a]n
2                    SALINAS v. TEXAS

                     BREYER, J., dissenting

innocent person’ ” would have said, “ ‘What are you talking
about? I didn’t do that. I wasn’t there.’ ” 368 S. W. 3d
550, 556 (Tex. Ct. App. 2011). But Salinas, the prosecutor
said, “ ‘didn’t respond that way.’ ” Ibid. Rather, “ ‘[h]e
wouldn’t answer that question.’ ” Ibid.
                              II
  The question before us is whether the Fifth Amendment
prohibits the prosecutor from eliciting and commenting
upon the evidence about Salinas’ silence. The plurality
believes that the Amendment does not bar the evidence
and comments because Salinas “did not expressly invoke
the privilege against self-incrimination” when he fell silent
during the questioning at the police station. Ante, at 1.
But, in my view, that conclusion is inconsistent with this
Court’s case law and its underlying practical rationale.
                             A
  The Fifth Amendment prohibits prosecutors from com-
menting on an individual’s silence where that silence
amounts to an effort to avoid becoming “a witness against
himself.” This Court has specified that “a rule of evidence”
permitting “commen[t] . . . by counsel” in a criminal case
upon a defendant’s failure to testify “violates the Fifth
Amendment.” Griffin v. California, 380 U. S. 609, 610,
n. 2, 613 (1965) (internal quotation marks omitted). See
also United States v. Patane, 542 U. S. 630, 637 (2004)
(plurality opinion); Turner v. United States, 396 U. S. 398,
433 (1970) (Black, J., dissenting). And, since “it is imper-
missible to penalize an individual for exercising his Fifth
Amendment privilege when he is under police custodial
interrogation,” the “prosecution may not . . . use at trial
the fact that he stood mute or claimed his privilege in the
face of accusation.” Miranda v. Arizona, 384 U. S. 436,
468, n. 37 (1966) (emphasis added).
  Particularly in the context of police interrogation, a
                 Cite as: 570 U. S. ____ (2013)           3

                    BREYER, J., dissenting

contrary rule would undermine the basic protection that
the Fifth Amendment provides. Cf. Kastigar v. United
States, 406 U. S. 441, 461 (1972) (“The privilege . . . usu-
ally operates to allow a citizen to remain silent when asked
a question requiring an incriminatory answer”). To permit
a prosecutor to comment on a defendant’s constitutionally
protected silence would put that defendant in an impossi-
ble predicament. He must either answer the question or
remain silent. If he answers the question, he may well
reveal, for example, prejudicial facts, disreputable associ-
ates, or suspicious circumstances—even if he is innocent.
See, e.g., Griffin, supra, at 613; Kassin, Inside Interroga-
tion: Why Innocent People Confess, 32 Am. J. Trial Advoc.
525, 537 (2009). If he remains silent, the prosecutor may
well use that silence to suggest a consciousness of guilt.
And if the defendant then takes the witness stand in order
to explain either his speech or his silence, the prosecution
may introduce, say for impeachment purposes, a prior
conviction that the law would otherwise make inadmissi-
ble. Thus, where the Fifth Amendment is at issue, to
allow comment on silence directly or indirectly can compel
an individual to act as “a witness against himself ”—very
much what the Fifth Amendment forbids. Cf. Pennsylva-
nia v. Muniz, 496 U. S. 582, 596–597 (1990) (definition of
“testimonial” includes responses to questions that require
a suspect to communicate an express or implied assertion
of fact or belief). And that is similarly so whether the
questioned individual, as part of his decision to remain
silent, invokes the Fifth Amendment explicitly or implic-
itly, through words, through deeds, or through reference to
surrounding circumstances.
                            B
  It is consequently not surprising that this Court, more
than half a century ago, explained that “no ritualistic
formula is necessary in order to invoke the privilege.”
4                     SALINAS v. TEXAS

                     BREYER, J., dissenting

Quinn v. United States, 349 U. S. 155, 164 (1955). Thus,
a prosecutor may not comment on a defendant’s failure to
testify at trial—even if neither the defendant nor anyone
else ever mentions a Fifth Amendment right not to do so.
Circumstances, not a defendant’s statement, tie the de-
fendant’s silence to the right. Similarly, a prosecutor may
not comment on the fact that a defendant in custody, after
receiving Miranda warnings, “stood mute”—regardless of
whether he “claimed his privilege” in so many words.
Miranda, supra, at 468, n. 37. Again, it is not any explicit
statement but, instead, the defendant’s deeds (silence) and
circumstances (receipt of the warnings) that tie together
silence and constitutional right. Most lower courts have so
construed the law, even where the defendant, having
received Miranda warnings, answers some questions
while remaining silent as to others. See, e.g., Hurd v.
Terhune, 619 F. 3d 1080, 1087 (CA9 2010); United States
v. May, 52 F. 3d 885, 890 (CA10 1995); United States v.
Scott, 47 F. 3d 904, 907 (CA7 1995); United States v. Can-
terbury, 985 F. 2d 483, 486 (CA10 1993); Grieco v. Hall,
641 F. 2d 1029, 1034 (CA1 1981); United States v. Ghiz,
491 F. 2d 599, 600 (CA4 1974). But see, e.g., United States
v. Harris, 956 F. 2d 177, 181 (CA8 1992).
   The cases in which this Court has insisted that a de-
fendant expressly mention the Fifth Amendment by name
in order to rely on its privilege to protect silence are cases
where (1) the circumstances surrounding the silence (un-
like the present case) did not give rise to an inference that
the defendant intended, by his silence, to exercise his Fifth
Amendment rights; and (2) the questioner greeted by the
silence (again unlike the present case) had a special need
to know whether the defendant sought to rely on the
protections of the Fifth Amendment. See ante, at 4 (ex-
plaining that, in such cases, the government needs to
know the basis for refusing to answer “so that it may
either argue that the testimony sought could not be self-
                 Cite as: 570 U. S. ____ (2013)            5

                     BREYER, J., dissenting

incriminating or cure any potential self-incrimination
through a grant of immunity” (citation omitted)). These
cases include Roberts, Rogers, Sullivan, Vajtauer, and
Jenkins—all of which at least do involve the protection of
silence—and also include cases emphasized by the plural-
ity that are not even about silence—namely, Murphy and
Garner.
   In Roberts and Rogers, the individual refused to answer
questions that government investigators (in Roberts) and a
grand jury (in Rogers) asked, principally because the
individual wanted to avoid incriminating other persons.
Roberts v. United States, 445 U. S. 552, 553–556 (1980);
Rogers v. United States, 340 U. S. 367, 368–370, and n. 4
(1951). But the Fifth Amendment does not protect some-
one from incriminating others; it protects against self-
incrimination. In turn, neither the nature of the questions
nor the circumstances of the refusal to answer them pro-
vided any basis to infer a tie between the silence and the
Fifth Amendment, while knowledge of any such tie would
have proved critical to the questioner’s determination as to
whether the defendant had any proper legal basis for
claiming Fifth Amendment protection.
   In Sullivan, the defendant’s silence consisted of his
failure to file a tax return—a return, he later claimed, that
would have revealed his illegal activity as a bootlegger.
United States v. Sullivan, 274 U. S. 259, 262–264 (1927).
The circumstances did not give rise to an inference of a tie
between his silence (in the form of failing to file a tax
return) and the Fifth Amendment; and, if he really did
want to rely on the Fifth Amendment, then the govern-
ment would have had special need to know of any such tie
in order to determine whether, for example, the assertion
of privilege was valid and, perhaps, an offer of immunity
was appropriate.
   In Vajtauer, an alien refused to answer questions asked
by an immigration official at a deportation proceeding.
6                    SALINAS v. TEXAS

                    BREYER, J., dissenting

United States ex rel. Vajtauer v. Commissioner of Immi-
gration, 273 U. S. 103, 113 (1927). Here, the circumstances
gave rise to a distinct inference that the alien was not
invoking any Fifth Amendment privilege: The alien’s
lawyer had stated quite publicly at the hearing that he
advised his client to remain silent not on Fifth Amend-
ment grounds; rather, the lawyer “ ‘advise[d] the alien not
to answer any further questions until the evidence upon
which the warrant is based will be presented here.’ ” Id.,
at 106–107 (quoting the lawyer). This statement weak-
ened or destroyed the possibility of a silence-Fifth
Amendment linkage; the Government could not challenge
his right to invoke the Fifth Amendment; and this Court
described its later invocation as “evidently an after-
thought.” Id., at 113.
  Perhaps most illustrative is Jenkins, a case upon which
the plurality relies, ante, at 9, n. 3, and upon which the
Texas Court of Criminal Appeals relied almost exclusively,
369 S. W. 3d 176, 178–179 (2012). Jenkins killed some-
one, and was not arrested until he turned himself in two
weeks later. Jenkins v. Anderson, 447 U. S. 231, 232
(1980). On cross-examination at his trial, Jenkins claimed
that his killing was in self-defense after being attacked.
Id., at 232–233. The prosecutor then asked why he did not
report the alleged attack, and in closing argument sug-
gested that Jenkins’ failure to do so cast doubt on his
claim to have acted in self-defense. Id., at 233–234. We
explained that this unusual form of “prearrest silence”
was not constitutionally protected from use at trial. Id., at
240. Perhaps even more aptly, Justice Stevens’ concur-
rence noted that “the privilege against compulsory self-
incrimination is simply irrelevant” in such circumstances.
Id., at 241 (footnote omitted). How would anyone have
known that Jenkins, while failing to report an attack, was
relying on the Fifth Amendment? And how would the
government have had any way of determining whether his
                  Cite as: 570 U. S. ____ (2013)            7

                     BREYER, J., dissenting

claim was valid? In Jenkins, as in Roberts, Rogers, Sulli-
van, and Vajtauer, no one had any reason to connect si-
lence to the Fifth Amendment; and the government had no
opportunity to contest any alleged connection.
   Still further afield from today’s case are Murphy and
Garner, neither of which involved silence at all. Rather, in
both cases, a defendant had earlier answered questions
posed by the government—in Murphy, by speaking with a
probation officer, and in Garner, by completing a tax
return. Minnesota v. Murphy, 465 U. S. 420, 422–425
(1984); Garner v. United States, 424 U. S. 648, 649–650
(1976). At the time of providing answers, neither circum-
stances nor deeds nor words suggested reliance on the
Fifth Amendment: Murphy simply answered questions
posed by his probation officer; Garner simply filled out a
tax return.      They did not argue that their self-
incriminating statements had been “compelled” in viola-
tion of the Fifth Amendment until later, at trial. Murphy,
supra, at 425, 431; Garner, supra, at 649, 665. The Court
held that those statements were not compelled. Murphy,
supra, at 440; Garner, supra, at 665. The circumstances
indicated that the defendants had affirmatively chosen to
speak and to write.
   Thus, we have two sets of cases: One where express
invocation of the Fifth Amendment was not required to tie
one’s silence to its protections, and another where some-
thing like express invocation was required, because cir-
cumstances demanded some explanation for the silence
(or the statements) in order to indicate that the Fifth
Amendment was at issue.
   There is also a third set of cases, cases that may well fit
into the second category but where the Court has held that
the Fifth Amendment both applies and does not require
express invocation despite ambiguous circumstances. The
Court in those cases has made clear that an individual,
when silent, need not expressly invoke the Fifth Amend-
8                     SALINAS v. TEXAS

                     BREYER, J., dissenting

ment if there are “inherently compelling pressures” not to
do so. Miranda, 384 U. S., at 467. Thus, in Garrity v.
New Jersey, 385 U. S. 493, 497 (1967), the Court held that
no explicit assertion of the Fifth Amendment was required
where, in the course of an investigation, such assertion
would, by law, have cost police officers their jobs. Similarly,
this Court did not require explicit assertion in response
to a grand jury subpoena where that assertion would have
cost two architects their public contracts or a political
official his job. Lefkowitz v. Turley, 414 U. S. 70, 75–76
(1973); Lefkowitz v. Cunningham, 431 U. S. 801, 802–804
(1977). In Leary v. United States, 395 U. S. 6, 28–29
(1969), the Court held that the Fifth Amendment did not
require explicit assertion of the privilege against self-
incrimination because, in the context of the Marihuana
Tax Act, such assertion would have been inherently in-
criminating. In Albertson v. Subversive Activities Control
Bd., 382 U. S. 70, 77–79 (1965), we held the same where
explicit assertion of the Fifth Amendment would have
required, as a first step, the potentially incriminating
admission of membership in the Communist Party. The
Court has also held that gamblers, without explicitly
invoking the Fifth Amendment, need not comply with tax
requirements that would, inherently and directly, lead to
self-incrimination. Marchetti v. United States, 390 U. S.
39, 60–61 (1968); Grosso v. United States, 390 U. S. 62,
67–68 (1968). All told, this third category of cases receives
the same treatment as the first: Circumstances, rather
than explicit invocation, trigger the protection of the Fifth
Amendment. So, too, in today’s case.
  The plurality refers to one additional case, namely
Berghuis v. Thompkins, 560 U. S. 370 (2010). See ante, at
8. But that case is here beside the point. In Berghuis, the
defendant was in custody, he had been informed of his
Miranda rights, and he was subsequently silent in the
face of 2 hours and 45 minutes of questioning before he
                 Cite as: 570 U. S. ____ (2013)            9

                     BREYER, J., dissenting

offered any substantive answers. Id., at ___–___ (slip op.,
at 2–4). The Court held that he had waived his Fifth
Amendment rights in respect to his later speech. The
Court said nothing at all about a prosecutor’s right to
comment on his preceding silence and no prosecutor
sought to do so. Indeed, how could a prosecutor lawfully
have tried to do so, given this Court’s statement in Mi-
randa itself that a prosecutor cannot comment on the fact
that, after receiving Miranda warnings, the suspect “stood
mute”? 384 U. S., at 468, n. 37.
  We end where we began. “[N]o ritualistic formula is
necessary in order to invoke the privilege.” Quinn, 349
U. S., at 164. Much depends on the circumstances of the
particular case, the most important circumstances being:
(1) whether one can fairly infer that the individual being
questioned is invoking the Amendment’s protection; (2) if
that is unclear, whether it is particularly important for
the questioner to know whether the individual is doing so;
and (3) even if it is, whether, in any event, there is a good
reason for excusing the individual from referring to the
Fifth Amendment, such as inherent penalization simply
by answering.
                             C
  Applying these principles to the present case, I would
hold that Salinas need not have expressly invoked the
Fifth Amendment. The context was that of a criminal
investigation. Police told Salinas that and made clear that
he was a suspect. His interrogation took place at the
police station. Salinas was not represented by counsel.
The relevant question—about whether the shotgun from
Salinas’ home would incriminate him—amounted to a
switch in subject matter. And it was obvious that the new
question sought to ferret out whether Salinas was guilty of
murder. See 368 S. W. 3d, at 552–553.
  These circumstances give rise to a reasonable inference
10                   SALINAS v. TEXAS

                    BREYER, J., dissenting

that Salinas’ silence derived from an exercise of his Fifth
Amendment rights. This Court has recognized repeatedly
that many, indeed most, Americans are aware that they
have a constitutional right not to incriminate themselves
by answering questions posed by the police during an
interrogation conducted in order to figure out the perpe-
trator of a crime. See Dickerson v. United States, 530
U. S. 428, 443 (2000); Brogan v. United States, 522 U. S.
398, 405 (1998); Michigan v. Tucker, 417 U. S. 433, 439
(1974). The nature of the surroundings, the switch of
topic, the particular question—all suggested that the right
we have and generally know we have was at issue at the
critical moment here. Salinas, not being represented by
counsel, would not likely have used the precise words
“Fifth Amendment” to invoke his rights because he would
not likely have been aware of technical legal require-
ments, such as a need to identify the Fifth Amendment by
name.
  At the same time, the need to categorize Salinas’ silence
as based on the Fifth Amendment is supported here by the
presence, in full force, of the predicament I discussed
earlier, namely that of not forcing Salinas to choose be-
tween incrimination through speech and incrimination
through silence. That need is also supported by the ab-
sence of any special reason that the police had to know,
with certainty, whether Salinas was, in fact, relying on the
Fifth Amendment—such as whether to doubt that there
really was a risk of self-incrimination, see Hoffman v.
United States, 341 U. S. 479, 486 (1951), or whether to
grant immunity, see Kastigar, 406 U. S., at 448. Given
these circumstances, Salinas’ silence was “sufficient to put
the [government] on notice of an apparent claim of the
privilege.” Quinn, supra, at 164. That being so, for rea-
sons similar to those given in Griffin, the Fifth Amend-
ment bars the evidence of silence admitted against Salinas
and mentioned by the prosecutor. See 380 U. S., at 614–615.
                 Cite as: 570 U. S. ____ (2013)          11

                    BREYER, J., dissenting 


                              D

   I recognize that other cases may arise where facts and
circumstances surrounding an individual’s silence present
a closer question. The critical question—whether those
circumstances give rise to a fair inference that the silence
rests on the Fifth Amendment—will not always prove easy
to administer. But that consideration does not support the
plurality’s rule-based approach here, for the administra-
tive problems accompanying the plurality’s approach are
even worse.
   The plurality says that a suspect must “expressly invoke
the privilege against self-incrimination.” Ante, at 1. But
does it really mean that the suspect must use the exact
words “Fifth Amendment”? How can an individual who is
not a lawyer know that these particular words are legally
magic? Nor does the Solicitor General help when he adds
that the suspect may “mak[e] the claim ‘in any language
that [the questioner] may reasonably be expected to un-
derstand as an attempt to invoke the privilege.’ ” Brief for
United States as Amicus Curiae 22 (quoting Quinn, supra,
at 162–163; alteration in original). What counts as “mak-
ing the claim”? Suppose the individual says, “Let’s discuss
something else,” or “I’m not sure I want to answer that”; or
suppose he just gets up and leaves the room. Cf. Davis v.
Mississippi, 394 U. S. 721, 727, n. 6 (1969) (affirming “the
settled principle that while the police have the right to
request citizens to answer voluntarily questions concern-
ing unsolved crimes[,] they have no right to compel them
to answer”); Berkemer v. McCarty, 468 U. S. 420, 439
(1984) (noting that even someone detained in a Terry stop
“is not obliged to respond” to police questions); Florida v.
Royer, 460 U. S. 491, 497–498 (1983) (plurality opinion).
How is simple silence in the present context any different?
   The basic problem for the plurality is that an effort to
have a simple, clear “explicit statement” rule poses a
serious obstacle to those who, like Salinas, seek to assert
12                   SALINAS v. TEXAS

                    BREYER, J., dissenting

their basic Fifth Amendment right to remain silent, for
they are likely unaware of any such linguistic detail. At
the same time, acknowledging that our case law does not
require use of specific words, see ante, at 2, leaves the
plurality without the administrative benefits it might
hope to find in requiring that detail.
   Far better, in my view, to pose the relevant question
directly: Can one fairly infer from an individual’s silence
and surrounding circumstances an exercise of the Fifth
Amendment’s privilege? The need for simplicity, the
constitutional importance of applying the Fifth Amend-
ment to those who seek its protection, and this Court’s
case law all suggest that this is the right question to ask
here. And the answer to that question in the circumstances
of today’s case is clearly: yes.
   For these reasons, I believe that the Fifth Amendment
prohibits a prosecutor from commenting on Salinas’s
silence. I respectfully dissent from the Court’s contrary
conclusion.

```

---
