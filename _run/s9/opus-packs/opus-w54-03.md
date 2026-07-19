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

## GROUP: content/cases/United States v. Salvucci.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Salvucci"
type: case
citation: "448 U.S. 83 (1980)"
parallel_cite: "100 S. Ct. 2547; 65 L. Ed. 2d 619"
neutral_cite: 1980 U.S. LEXIS 141
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-06-25
docket: 79-244
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1980-06-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Salvucci
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110325/united-states-v-salvucci/"
  cluster_id: 110325
  opinion_id: 9428036
  identity_checked: true
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: "Key — Progeny / Refinement"
related: ["[[Rakas v. Illinois]]", "[[Jones v. United States]]", "[[Rawlings v. Kentucky]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "automatic-standing", "possessory-offense", "expectation-of-privacy"]
holding: "Abolished automatic standing; a defendant charged with a possessory crime must show that his own Fourth Amendment rights (a legitimate…"
lake:
  record_id: United States v. Salvucci
  status: verified
  projected_at: 2026-07-06
---

# United States v. Salvucci

*448 U.S. 83 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Salvucci and Zackular were charged with possessing stolen mail (12 checks), seized by police from an apartment rented by Zackular's mother during a search conducted under a warrant. They moved to suppress the checks, arguing the warrant affidavit failed to establish probable cause. The government responded that they lacked [[Standing to Challenge a Search|standing to challenge]] the search. Relying on *[[Jones v. United States]]* (1960), the First Circuit held that, because they were charged with possessory crimes, they had "automatic standing" to challenge the search without showing any privacy interest in the apartment.

## Issue
Whether a defendant charged with a possessory offense has "automatic standing" to challenge the search that produced the evidence, without showing that his own Fourth Amendment rights were violated.

## Rule
No. "Today we hold that defendants charged with crimes of possession may only claim the benefits of the exclusionary rule if their own Fourth Amendment rights have in fact been violated. The automatic standing rule of *Jones v. United States*, supra, is therefore overruled." — 448 U.S. at 85. ^pin-85

Consistent with *[[Rakas v. Illinois]]*, the dispositive question is whether the defendant had a legitimate expectation of privacy in the area searched — not whether he possessed the item seized.

## Application
Because Salvucci and Zackular were charged with possessing the stolen checks, they could no longer rely on automatic standing. To suppress the checks, they had to establish that their own legitimate expectation of privacy in the searched apartment had been violated. The Court reversed and [[Reading and Citing Cases#on-remand|remanded]] so that question could be addressed.

## Conclusion
Automatic standing is overruled; a defendant charged with a possessory crime must show a violation of his **own** Fourth Amendment rights. The Supreme Court reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Salvucci* — decided the same day as *[[Rawlings v. Kentucky]]* — completes the absorption of "standing" into substantive Fourth Amendment analysis begun in [[Rakas v. Illinois]]: possession of the seized goods alone no longer confers standing. It **overrules** the automatic-standing rule of [[Jones v. United States]] (1960).

## Appears on
- [[Standing to Challenge a Search]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Salvucci*, 448 U.S. 83 (1980) — https://www.courtlistener.com/opinion/110325/united-states-v-salvucci/ — pinpoint: 85 (parallel 100 S. Ct. 2547).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "12539b76a89ca087", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "448 U.S. 83 (1980)", "court": "U.S. Supreme Court", "neutral_cite": "1980 U.S. LEXIS 141", "official_citation_present": true, "parallel_cite": "100 S. Ct. 2547; 65 L. Ed. 2d 619", "title": "United States v. Salvucci", "year": "1980"}}
{"assertion_id": "5632344912ab45b4", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Abolished automatic standing; a defendant charged with a possessory crime must show that his own Fourth Amendment rights (a legitimate…", "title": "United States v. Salvucci"}}
{"assertion_id": "639ba27a6bc64919", "dimension": "support", "kind": "home_role", "locator": {"home": "Standing to Challenge a Search"}, "payload": {"home": "Standing to Challenge a Search", "role": "Key — Progeny / Refinement", "title": "United States v. Salvucci"}}
{"assertion_id": "270407f00bd6122b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1980-06-25", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Salvucci", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Salvucci", "varies_by_point": "false"}}
{"assertion_id": "9054f8219c49af03", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Salvucci"}}
```

### lake record — United States v. Salvucci

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Salvucci",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Salvucci",
    "case_name_short": "Salvucci",
    "case_name_full": "UNITED STATES v. SALVUCCI Et Al.",
    "input_case_name": "United States v. Salvucci",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-06-25",
    "year": 1980,
    "docket": "79-244",
    "cluster_id": 110325,
    "lead_opinion_id": 9428036,
    "sibling_ids": [
      110325,
      9428036,
      9428037
    ],
    "absolute_url": "/opinion/110325/united-states-v-salvucci/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "448 U.S. 83",
      "volume": "448",
      "reporter": "U.S.",
      "page": "83",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 2547",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2547",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 619",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 141",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "141",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "448 U.S. 83",
        "volume": "448",
        "reporter": "U.S.",
        "page": "83",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 2547",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2547",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 619",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 141",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "141",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "448 U.S. 83",
    "official_selection": {
      "court_class": "scotus",
      "selected": "448 U.S. 83",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-85",
      "page": null,
      "quote": "to challenge the search that produced the evidence, without showing that his own Fourth Amendment rights were violated. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1980-06-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Salvucci",
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
        "journal_ref": "United States v. Salvucci:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. DeJesus",
          "cluster_id": 4860242,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Scurry",
          "cluster_id": 4529581,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Pirk",
          "cluster_id": 7327733,
          "cite": [
            "282 F. Supp. 3d 585"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Louisiana v. Joseph Michael Moultrie",
          "cluster_id": 4405157,
          "cite": [
            "224 So. 3d 349",
            "2017 La. LEXIS 1382",
            "2017 WL 2836066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Haynes",
          "cluster_id": 2795871,
          "cite": [
            "116 A.3d 640",
            "2015 Pa. Super. 94",
            "2015 Pa. Super. LEXIS 207",
            "2015 WL 1814017"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Steven Maxwell",
          "cluster_id": 2780753,
          "cite": [
            "778 F.3d 719"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gary Webster v. State",
          "cluster_id": 3130306,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andrew Alan Weaver v. State",
          "cluster_id": 2854979,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Grady Leroy Martin v. State",
          "cluster_id": 2855775,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Zachary Daniel Harris A/K/A Zachary Harris v. State",
          "cluster_id": 2852672,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane1_negative"
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
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
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
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Salvucci",
          "cluster_id": 110325,
          "cite": [
            "65 L. Ed. 2d 619",
            "100 S. Ct. 2547",
            "448 U.S. 83",
            "1980 U.S. LEXIS 141"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Steagald v. United States",
          "cluster_id": 110464,
          "cite": [
            "68 L. Ed. 2d 38",
            "101 S. Ct. 1642",
            "451 U.S. 204",
            "1981 U.S. LEXIS 89",
            "49 U.S.L.W. 4418"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Carter",
          "cluster_id": 118249,
          "cite": [
            "142 L. Ed. 2d 373",
            "119 S. Ct. 469",
            "525 U.S. 83",
            "1998 U.S. LEXIS 7844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
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
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
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
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kothe v. State",
          "cluster_id": 1504839,
          "cite": [
            "152 S.W.3d 54",
            "2004 Tex. Crim. App. LEXIS 1749",
            "2004 WL 2347781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
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
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
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
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bryant, Smith and Wheeler",
          "cluster_id": 2720490,
          "cite": [
            "60 Cal. 4th 335",
            "178 Cal. Rptr. 3d 185",
            "334 P.3d 573",
            "2014 Cal. LEXIS 6110"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lance W.",
          "cluster_id": 1421847,
          "cite": [
            "694 P.2d 744",
            "37 Cal. 3d 873",
            "210 Cal. Rptr. 631",
            "1985 Cal. LEXIS 241"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 1718150,
          "cite": [
            "803 S.W.2d 272",
            "1990 WL 180807"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Carter",
          "cluster_id": 2629957,
          "cite": [
            "117 P.3d 476",
            "32 Cal. Rptr. 3d 759",
            "36 Cal. 4th 1114",
            "2005 Cal. Daily Op. Serv. 7196",
            "2005 Daily Journal DAR 9801",
            "2005 Cal. LEXIS 8908"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parks v. Commonwealth",
          "cluster_id": 1315235,
          "cite": [
            "270 S.E.2d 755",
            "221 Va. 492",
            "1980 Va. LEXIS 269"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
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
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Novembrino",
          "cluster_id": 1516571,
          "cite": [
            "519 A.2d 820",
            "105 N.J. 95",
            "1987 N.J. LEXIS 265"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
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
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Burton",
          "cluster_id": 2223932,
          "cite": [
            "848 N.E.2d 454",
            "6 N.Y.3d 584",
            "815 N.Y.S.2d 7"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. White",
          "cluster_id": 1194272,
          "cite": [
            "640 P.2d 1061",
            "97 Wash. 2d 92",
            "1982 Wash. LEXIS 1262"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCullough v. State",
          "cluster_id": 1782139,
          "cite": [
            "692 S.W.2d 504",
            "1985 Tex. Crim. App. LEXIS 1426"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Calloway v. State",
          "cluster_id": 2364085,
          "cite": [
            "743 S.W.2d 645",
            "1988 Tex. Crim. App. LEXIS 35",
            "1988 WL 4310"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Huddleston",
          "cluster_id": 2435833,
          "cite": [
            "924 S.W.2d 666",
            "1996 Tenn. LEXIS 387",
            "1996 WL 328642"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gaetano Modica",
          "cluster_id": 396890,
          "cite": [
            "663 F.2d 1173",
            "1981 U.S. App. LEXIS 16444"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. O'NEILL",
          "cluster_id": 2621477,
          "cite": [
            "62 P.3d 489"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Salvucci:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110325 OR 9428036 OR 9428037) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjE0MzUyMDAwMDAwJnM9MjQ2MTYxNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110325+OR+9428036+OR+9428037%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 11,
        "triage_snippet_classified": 189
      },
      "lane2_top_cited": {
        "query": "cites:(110325 OR 9428036 OR 9428037)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDkmcz03NzQ3MjcmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110325+OR+9428036+OR+9428037%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110325 OR 9428036 OR 9428037)",
        "reviewed": 21,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 21,
        "triage_read": 1,
        "triage_snippet_classified": 20
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110325 OR 9428036 OR 9428037)",
    "indexed_citing_opinions": 1291,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110325,
        "count": 1156,
        "count_source": "search"
      },
      {
        "opinion_id": 9428036,
        "count": 156,
        "count_source": "search"
      },
      {
        "opinion_id": 9428037,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1879,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-salvucci.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgwMTg3Njgmcz04NTE1NzkyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110325+OR+9428036+OR+9428037%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9428037,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428037,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428037,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428037,
        "cited_id": 108760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428037,
        "cited_id": 108970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428037,
        "cited_id": 110038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428037,
        "cited_id": 110267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428037,
        "cited_id": 110298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 96569,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 108602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 108760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 108970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 329973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 343457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 348314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 366911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 2046116,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 2054688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 2127838,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 8906856,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9428036,
        "cited_id": 9427384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 96569,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 108602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 108760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 108970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 110038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 110267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 110298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 276302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 329973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 343457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 348314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 366911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 2046116,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 2054688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 2127838,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 8906856,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 9427384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110325,
        "cited_id": 9428036,
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
    "date_created": "2026-07-06T02:43:58Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:44:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:44:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:48:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:44:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Salvucci

```
<opinion type="majority">
<author id="b116-11">Mr. Justice Rehnquist</author>
<p id="A8D">delivered the opinion of the Court. Relying on <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960), the Court of Appeals for the First Circuit held that since respondents were charged with crimes of possession, they were <page-number citation-index="1" label="85">*85</page-number>entitled to claim “automatic standing” to challenge the legality of the search which produced the evidence against them, without regard to whether they had an expectation of privacy in the premises searched. <span class="citation" data-id="366911"><a href="/opinion/366911/united-states-v-john-m-salvucci-jr-joseph-g-zackular/" aria-description="Citation for case: United States v. John M. Salvucci, Jr., Joseph G. Zackular">599 F. 2d 1094</a></span> (1979). Today we hold that defendants charged with crimes of possession may only claim the benefits of the exclusionary rule if their own Fourth Amendment rights have in fact been violated. The automatic standing, rule of <em>Jones </em>v. <em>United States, supra, </em>is therefore overruled.</p>
<p id="b117-5">I</p>
<p id="b117-6">Respondents, John Salvueci and Joseph Zaekular, were charged in a federal indictment with 12 counts of unlawful possession of stolen mail, in violation of 18 TJ. S. C. § 1708. The 12 checks which formed the basis of the indictment had been seized by the Massachusetts police during the search of an apartment rented by respondent Zackular’s mother. The search was conducted pursuant to a warrant.</p>
<p id="b117-7">Respondents filed a motion to suppress the checks on the ground that the affidavit supporting the application for the search warrant was inadequate to demonstrate probable cause. The District Court granted respondents’ motions and ordered that the checks be suppressed.<footnotemark>1</footnotemark> The Government sought reconsideration of the District Court’s ruling, contending that respondents lacked “standing” to challenge the constitutionality of the search. The District Court reaffirmed its suppression order and the Government appealed.</p>
<p id="b117-8">The Court of Appeals affirmed, holding that respondents had “standing” and the search warrant was constitutionally inadequate. The court found that the respondents were not required to establish a legitimate expectation of privacy in the premises searched or the property seized because they were entitled to assert “automatic standing” to object to the search <page-number citation-index="1" label="86">*86</page-number>and seizure under <em>Jones </em>v. <em>United States, supra. </em>The court observed that the vitality of the <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>doctrine had been challenged in recent years, but that “[u]ntil the Supreme Court rules on this question, we are not prepared to hold that the automatic standing rule of <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>has been . . . overruled. . . . That is an issue which the Supreme Court must resolve.” <span class="citation" data-id="366911"><a href="/opinion/366911/united-states-v-john-m-salvucci-jr-joseph-g-zackular/#1098" aria-description="Citation for case: United States v. John M. Salvucci, Jr., Joseph G. Zackular">599 F. 2d, at 1098</a></span>. The Court of Appeals was obviously correct in its characterization of the status of <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>, </em>and we granted certiorari in order to resolve the controversy.<footnotemark>2</footnotemark> <span class="citation multiple-matches"><a href="/c/U.%20S./444/989/">444 U. S. 989</a></span> (1979).</p>
<p id="b118-5">II</p>
<p id="b118-6">As early as 1907, this Court took the position that remedies for violations of constitutional rights would only be afforded to a person who “belongs to the class for whose sake the constitutional protection is given.” <em>Hatch </em>v. <em>Reardon, </em><span class="citation" data-id="96569"><a href="/opinion/96569/new-york-ex-rel-hatch-v-reardon/#160" aria-description="Citation for case: New York Ex Rel. Hatch v. Reardon">204 U. S. 152, 160</a></span>. The exclusionary rule is one form of remedy afforded for Fourth Amendment violations, and the Court in <em>Jones </em>v. <em>United States </em>held that the <em>Hatch </em>v. <em><span class="citation" data-id="96569"><a href="/opinion/96569/new-york-ex-rel-hatch-v-reardon/" aria-description="Citation for case: New York Ex Rel. Hatch v. Reardon">Reardon</a></span> </em>principle properly limited its availability. The Court reasoned that ordinarily “it is entirely proper to require of one who seeks to challenge the legality of a search as the basis for suppressing relevant evidence that he . . . establish, that he himself was the victim of an invasion of privacy.” <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States">362 U. S., at 261</a></span>. Subsequent attempts to vicariously assert violations of the Fourth Amendment rights of others have been repeatedly rejected by this Court. <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 174</a></span> (1969); <em>Brown </em>v. <em>United States, </em><span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/#230" aria-description="Citation for case: Brown v. United States">411 U. S. <page-number citation-index="1" label="87">*87</page-number>223, 230</a></span> (1973). Most recently, in <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978), we held that “it is proper to permit only defendants whose Fourth Amendment rights have been violated to benefit from the [exclusionary] rule’s protections.” <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#134" aria-description="Citation for case: Rakas v. Illinois"><em>Id., </em>at 134</a></span>.</p>
<p id="b119-5">Even though the Court in <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>recognized that the exclusionary rule should only be available to protect defendants who have been the victims of an illegal search or seizure, the Court thought it necessary to establish an exception. In cases where possession of the seized evidence was an essential element of the offense charged, the Court held that the defendant was not obligated to establish that his own Fourth Amendment rights had been violated, but only that the search and seizure of the evidence was unconstitutional.<footnotemark>3</footnotemark> Upon such a showing, the exclusionary rule would be available to prevent the admission of the evidence against the defendant.</p>
<p id="b119-6">The Court found that the prosecution of such possessory offenses presented a “special problem” which necessitated the departure from the then settled principles of Fourth Amendment “standing.” <footnotemark><em>4</em></footnotemark><em> </em>Two circumstances were found to require this exception. First, the Court found that in order to establish standing at a hearing on a motion to suppress, the defendant would often be “forced to allege facts the proof of which would tend, if indeed not be sufficient, to convict him,” since several Courts of Appeals had “pinioned a defendant within this dilemma” by holding that evidence adduced at the motion <page-number citation-index="1" label="88">*88</page-number>to suppress could be used against the defendant at trial. <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#262" aria-description="Citation for case: Jones v. United States">362 U. S., at 262</a></span>. The Court declined to embrace any rule which would require a defendant to assert his Fourth Amendment claims only at the risk of providing the prosecution with self-incriminating statements admissible at trial. The Court sought resolution of this dilemma by relieving the defendant of the obligation of establishing that his Fourth Amendment rights were violated by an illegal search or seizure.</p>
<p id="b120-5">The Court also commented that this rule would be beneficial for a second reason. Without a rule prohibiting a Government challenge to a defendant’s “standing” to invoke the exclusionary rule in a possessory offense prosecution, the Government would be allowed the “advantage of contradictory positions.” <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#263" aria-description="Citation for case: Jones v. United States"><em>Id., </em>at 263</a></span>. The Court reasoned that the Government ought not to be allowed to assert that the defendant possessed the goods for purposes of criminal liability, while simultaneously asserting that he did not possess them for the purposes of claiming the protections of the Fourth Amendment. The Court found that “[i]t is not consonant with the amenities, to put it mildly, of the administration of criminal justice to sanction such squarely contradictory assertions of power by the Government.” <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#263" aria-description="Citation for case: Jones v. United States"><em>Id., </em>at 263-264</a></span>. Thus in order to prevent both the risk that self-incrimination would attach to the assertion of Fourth Amendment rights, as well as to prevent the “vice of prosecutorial self-contradiction,” see <em>Brown </em>v. <em>United States, supra, </em>at 229, the Court adopted the rule of “automatic standing.”</p>
<p id="A5o">In the 20 years which have lapsed since the Court’s decision in <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>, </em>the two reasons which led the Court to the rule of automatic standing have likewise been affected 'by time. This Court has held that testimony given by a defendant in support of a motion to suppress cannot be admitted as evi-denee of his guilt at trial. <em>Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span> (1968). Developments in the principles of Fourth Amendment standing, as well, clarify that a prosecutor may, with legal consistency and legitimacy, assert that a defendant <page-number citation-index="1" label="89">*89</page-number>charged with possession of a seized item did not have a privacy interest violated in the course of the search and seizure. We are convinced not only that the original tenets of the <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>decision have eroded, but also that no alternative principles exist to support retention of the rule.</p>
<p id="b121-5">A</p>
<p id="b121-6">The “dilemma” identified in <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>, </em>that a defendant charged with a possessory offense might only be able to establish his standing to challenge a search and seizure by giving self-incriminating testimony admissible as evidence of his guilt, was eliminated by our decision in <em>Simmons </em>v. <em>United States, supra. </em>In <em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span>, </em>the defendant Garrett was charged with bank robbery. During the search of a codefendant's mother’s house, physical evidence used in the bank robbery, including a suitcase, was found in the basement and seized. In an effort to establish his standing to assert the illegality of the search, Garrett testified at the suppression hearing that the suitcase was similar to one he owned and that he was the owner of the clothing discovered inside the suitcase. Garrett’s motion to suppress was denied, but his testimony was admitted into evidence against him as part of the Government’s case-in-chief at trial. This Court reversed, finding that “a defendant who knows that his testimony may be admissible against him at trial will sometimes be deterred from presenting the testimonial proof of standing necessary to assert a Fourth Amendment claim.” <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#392" aria-description="Citation for case: Simmons v. United States">390 U. S., at 392-393</a></span>. The Court found that, in effect, the defendant was</p>
<blockquote id="b121-7">“obliged either to give up what he believed, with advice of counsel, to be a valid Fourth Amendment claim or, in legal effect, to waive his Fifth Amendment privilege against self-incrimination. In these circumstances, we find it intolerable that one constitutional right should have to be surrendered in order to assert another. We therefore hold that when a defendant testifies in support of a motion to suppress evidence on Fourth Amendment <page-number citation-index="1" label="90">*90</page-number>grounds, his testimony may not thereafter be admitted against him at trial on the issue of guilt unless he makes no objection.” <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#394" aria-description="Citation for case: Simmons v. United States"><em>Id., </em>at 394</a></span>.</blockquote>
<p id="b122-5">This Court’s ruling in <em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span> </em>thus not only extends protection against this risk of self-incrimination in all of the cases covered by <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>, </em>but also grants a form of “use immunity” to those defendants charged with nonpossessory crimes. In this respect, the protection of <em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span> </em>is therefore broader than that of <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>. </em>Thus, as we stated in <em>Brown </em>v. <em>United States, </em><span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/#228" aria-description="Citation for case: Brown v. United States">411 U. S., at 228</a></span>, “[t]he self-incrimination dilemma, so central to the <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>decision, can no longer occur under the prevailing interpretation of the Constitution [in Simmons].”</p>
<p id="b122-6">B</p>
<p id="b122-7">This Court has identified the self-incrimination rationale as the cornerstone of the <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>opinion. See <em>Brown </em>v. <em>United States, supra, </em>at 228. We need not belabor the question of whether the “vice” of prosecutorial contradiction could alone support a rule countenancing the exclusion of probative evidence on the grounds that someone other than the defendant was denied a Fourth Amendment right. The simple answer is that the decisions of this Court, especially our most recent decision in <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978), clearly establish that a prosecutor may simultaneously maintain that a defendant criminally possessed the seized good, but was not subject to a Fourth Amendment deprivation, without legal contradiction. To conclude that a prosecutor engaged in self-contradiction in <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>, </em>the Court necessarily relied on the unexamined assumption that a defendant’s possession of a seized good sufficient to establish criminal culpability was also sufficient to establish Fourth Amendment “standing.” This assumption, however, even if correct at the time, is no longer so.<footnotemark>5</footnotemark></p>
<p id="b123-4"><page-number citation-index="1" label="91">*91</page-number>The person in legal possession of a good seized during an illegal search has not necessarily been subject to a Fourth Amendment deprivation.<footnotemark>6</footnotemark> As we hold today in <em>Rawlings </em>v. <em>Kentucky, post, </em>p. 98, legal possession of a seized good is not a proxy for determining whether the owner had a Fourth Amendment interest, for it does not invariably represent the protected Fourth Amendment interest. This Court has repeatedly repudiated the notion that “arcane distinctions developed in property and tort law” ought to control our Fourth Amendment inquiry. <em>Rakas </em>v. <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois"><em>Illinois, supra, </em>at 143</a></span>. In another section of the opinion in <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>itself, the Court concluded that, “it is unnecessary and ill-advised to import into the law surrounding the constitutional right to be free from unreasonable searches and seizures subtle distinctions, developed and refined by the common law in evolving the body of private property law. . . .” <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States">362 U. S., at 266</a></span>. See also <em>Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364</a></span> (1968); <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967).</p>
<p id="b123-5">While property ownership is clearly a factor to be considered in determining whether an individual’s Fourth Amendment rights have been violated, see <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#144" aria-description="Citation for case: Rakas v. Illinois"><em>Rakas, supra, </em>at 144, n. 12</a></span>, property rights are neither the beginning nor the end of this Court’s inquiry. In <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>, </em>this Court held that an illegal search only violates the rights of those who have “a legitimate <page-number citation-index="1" label="92">*92</page-number>expectation of privacy in the invaded place.” <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#140" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 140</a></span>. See also <em>Mancusi </em>v. <em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">DeForte, supra.</a></span></em></p>
<p id="b124-5">We simply decline to use possession of a seized good as a substitute for a factual finding that the owner of the good had a legitimate expectation of privacy in the area searched. In <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>, </em>the Court held not only that automatic standing should be conferred on defendants charged with crimes of possession, but, alternatively, that Jones had actual standing because he was “legitimately on the premises” at the time of the search. In <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>, </em>this Court rejected the adequacy of this second <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>standard, finding that it was “too broad a gauge for measurement of Fourth Amendment rights.” 439 IJ. S., at 142. In language appropriate to our consideration of the automatic standing rule as well, we reasoned:</p>
<blockquote id="b124-6">“In abandoning 'legitimately on premises’ for the doctrine that we announce today, we are not forsaking a time-tested and workable rule, which has produced consistent results when applied, solely for the sake of fidelity to the values underlying the Fourth Amendment. Rather, we are rejecting blind adherence to a phrase which at most has superficial clarity and which conceals underneath that thin veneer all of the problems of line drawing which must be faced in any conscientious effort to apply the Fourth Amendment. Where the factual premises for a rule are so generally prevalent that little would be lost and much would be gained by abandoning case-by-case analysis, we have not hesitated to do so. .. . We would not wish to be understood as saying that legitimate presence on the premises is irrelevant to one’s expectation of privacy, but it cannot be deemed controlling.” <em>Id., </em>at 147-148.</blockquote>
<p id="b124-7">As in <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>, </em>we again reject “blind adherence” to the other underlying assumption in <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>that possession of the seized good is an acceptable measure of Fourth Amendment interests. As in <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>, </em>we find that the <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>standard “creates too <page-number citation-index="1" label="93">*93</page-number>broad a gauge for measurement of Fourth Amendment rights” and that we must instead engage in a “conscientious effort to apply the Fourth Amendment” by asking not merely whether the defendant had a possessory interest in the items seized, but whether he had an expectation of privacy in the area searched. Thus neither prosecutorial “vice,” nor the underlying assumption of <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>that possession of a seized good is the equivalent of Fourth Amendment “standing” to challenge the search, can save the automatic standing rule.</p>
<p id="b125-4">C</p>
<p id="b125-5">Even though the original foundations of <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>are no longer relevant, respondents assert that principles not articulated by the Court in <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>support retention of the rule. First, respondents maintain that while <em>Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span> (1968), eliminated the possibility that the prosecutor could use a defendant's testimony at a suppression hearing as substantive evidence of guilt at trial, <em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span> </em>did not eliminate other risks to the defendant which attach to giving testimony on a motion to suppress.<footnotemark>7</footnotemark> Principally, respondents assert that the prosecutor may still be permitted to use the defendant’s testimony to impeach him at trial.<footnotemark>8</footnotemark> This Court <page-number citation-index="1" label="94">*94</page-number>has not decided whether <em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span> </em>precludes the use of a defendant’s testimony at a suppression hearing to impeach his testimony at trial.<footnotemark>9</footnotemark> But the issue presented here is quite different from the one of whether “use immunity” extends only through the Government’s case-in-chief, or beyond that to the direct and cross-examination of a defendant in the event he chooses to take the stand. That issue need not be and is not resolved here, for it is an issue which more aptly relates to the proper breadth of the <em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span> </em>privilege, and not to the need for retaining automatic standing.</p>
<p id="b126-5">Respondents also seek to retain the <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>rule on the grounds that it is said to maximize the deterrence of illegal police conduct by permitting an expanded class of potential challengers. The same argument has been rejected by this Court as a sufficient basis for allowing persons whose Fourth Amendment rights were not violated to nevertheless claim the benefits of the exclusionary rule. In <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States">394 U. S., at 174-175</a></span>, we explicitly stated:</p>
<blockquote id="b126-6">“The deterrent values of preventing the incrimination of those whose rights the police have violated have been considered sufficient to justify the suppression of probative evidence even though the case against the defendant is weakened or destroyed. We adhere to that judgment. But we are not convinced that the additional benefits of extending the exclusionary rule to other defendants would justify further encroachment upon the public interest in prosecuting those accused of crime and having them acquitted or convicted on the basis of all the evidence which exposes the truth.”</blockquote>
<p id="b126-7">See also <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#137" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 137</a></span>; <em>United States </em>v. <em>Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#275" aria-description="Citation for case: United States v. Ceccolini">435 U. S. 268, 275-276</a></span> (1978); <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#350" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 350-351</a></span> (1974). Respondents’ de<page-number citation-index="1" label="95">*95</page-number>terrence argument carries no special force in the context of possessory offenses and we therefore again reject it.</p>
<p id="b127-5">We are convinced that the automatic standing rule of <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>has outlived its usefulness in this Court’s Fourth Amendment jurisprudence. The doctrine now serves only to afford a windfall to defendants whose Fourth Amendment rights have <em>not </em>been violated. We are unwilling to tolerate the exclusion of probative evidence under such circumstances since we adhere to the view of <em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">Alderman</a></span> </em>that the values of the Fourth Amendment are preserved by a rule which limits the availability of the exclusionary rule to defendants who have been subjected to a violation of their Fourth Amendment rights.</p>
<p id="b127-6">This action comes to us as a challenge to a pretrial decision suppressing evidence. The respondents relied on automatic standing and did not attempt to establish that they had a legitimate expectation of privacy in the areas of Zackular’s mother’s home where the goods were seized. We therefore think it appropriate to remand so that respondents will have an opportunity to demonstrate, if they can, that their own Fourth Amendment rights were violated. See <em>Combs </em>v. <em>United States, </em><span class="citation" data-id="108602"><a href="/opinion/108602/combs-v-united-states/" aria-description="Citation for case: Combs v. United States">408 U. S. 224</a></span> (1972).</p>
<p id="b127-7">
<em>Reversed and remanded.</em>
</p>
<footnote label="1">
<p id="b117-9"> The District Court held that the affidavit was deficient because the affiant relied on double hearsay, and failed to specify the dates on which information included in the affidavit had been obtained.</p>
</footnote>
<footnote label="2">
<p id="b118-7"> The Courts of Appeals have divided on the continued applicability of the automatic standing rule. The Sixth Circuit abandoned the rule after our decision in <em>Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span> (1968). See, <em>e. g., United States </em>v. <span class="citation" data-id="343457"><a href="/opinion/343457/united-states-v-sheryl-hunter-and-ezell-allen/" aria-description="Citation for case: United States v. Sheryl Hunter and Ezell Allen"><em>Hunter, 550 </em>F. 2d 1066</a></span> (1977). Most of the remaining Circuits appear to have retained the rule, but many with “misgivings.” See, <em>e. g., United States </em>v. <em>Oates, </em><span class="citation" data-id="348314"><a href="/opinion/348314/united-states-v-paul-v-oates/#52" aria-description="Citation for case: United States v. Paul v. Oates">560 F. 2d 45, 52</a></span> (CA2 1977) ; <em>United States </em>v. <span class="citation" data-id="8906856"><a href="/opinion/8918451/united-states-v-edwards/#892" aria-description="Citation for case: United States v. Edwards"><em>Edwards, 577 </em>F. 2d 883, 892</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./439/968/">439 U. S. 968</a></span> (1978).</p>
</footnote>
<footnote label="3">
<p id="b119-7"> In <em>Brown </em>v. <em>United States, </em><span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/#229" aria-description="Citation for case: Brown v. United States">411 U. S. 223, 229</a></span> (1973), this Court clarified that the automatic standing rule of <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>was applicable only where the offense charged “possession of the seized evidence at the time of the contested search and seizure.”</p>
</footnote>
<footnote label="4">
<p id="b119-8"> In <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>, </em>this Court discarded reliance on concepts of “standing” in determining whether a defendant is entitled to claim the protections of the exclusionary rule. The inquiry, after <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>, </em>is simply whether the defendant’s rights were violated by the allegedly illegal search or seizure. Because <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>was decided at a time when “standing” was designated as a separate inquiry, we use that term for the purposes of re-examining that opinion.</p>
</footnote>
<footnote label="5">
<p id="b122-8"> Respondent Salvncei cites this Court’s decision in <em>United States </em>v. <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers"><em>Jeffers, 342 </em>U. S. 48</a></span> (1951), as support for the view that legal ownership <page-number citation-index="1" label="91">*91</page-number>of the seized good was sufficient to confer Fourth Amendment “standing.” In <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>, </em>however, we stated that “[s]tanding in <em>Jeffers </em>was based on Jeffers’ possessory interest in <em>both </em>the premises searched and the property seized.” <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#136" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 136</a></span>. (Emphasis added.)</p>
</footnote>
<footnote label="6">
<p id="b123-10"> Legal possession of the seized good may be sufficient in some circumstances to entitle a defendant to seek the return of the seized property if the seizure, as opposed to the search, was illegal. See, <em>e. g., United States </em>v. <em>Lisk, </em><span class="citation" data-id="9462088"><a href="/opinion/329973/united-states-v-gerard-fredrick-lisk-jr/" aria-description="Citation for case: United States v. Gerard Fredrick Lisk, Jr.">522 F. 2d 228</a></span> (CA7 1975) (Stevens, J.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./423/1078/">423 U. S. 1078</a></span> (1976), although in that case the property was ultimately found not to have been illegally seized. We need not explore this issue since respondents did not challenge the constitutionality of the seizure of the evidence.</p>
</footnote>
<footnote label="7">
<p id="b125-6"> The respondents argue that the prosecutor’s access to the suppression testimony will unfairly provide the prosecutor with information advantageous to the preparation of his ease and trial strategy. This argument, however, is surely applicable equally to possessory and nonpossessory offenses. This Court has clearly declined to expand the <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>rule to other classes of offenses, <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span> (1969); <em>Brown </em>v. <em>United States, </em><span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/" aria-description="Citation for case: Brown v. United States">411 U. S. 223</a></span> (1973), and thus respondents’ rationale cannot support the retention of a special rule of automatic standing here.</p>
</footnote>
<footnote label="8">
<p id="b125-7"> A number of courts considering the question have held that such testimony is admissible as evidence of impeachment. <em>Gray </em>v. <em>State, </em><span class="citation" data-id="2054688"><a href="/opinion/2054688/gray-v-state/" aria-description="Citation for case: Gray v. State">43 Md. App. 238</a></span>, <span class="citation" data-id="2054688"><a href="/opinion/2054688/gray-v-state/" aria-description="Citation for case: Gray v. State">403 A. 2d 853</a></span> (1979); <em>People </em>v. <em>Douglas, </em><span class="citation" data-id="2127838"><a href="/opinion/2127838/people-v-douglas/" aria-description="Citation for case: People v. Douglas">66 Cal. App. 3d 998</a></span>, <span class="citation" data-id="2127838"><a href="/opinion/2127838/people-v-douglas/" aria-description="Citation for case: People v. Douglas">136 Cal. Rptr. 358</a></span> (1977); <em>People </em>v. <em>Sturgis, </em><span class="citation" data-id="9530537"><a href="/opinion/2046116/people-v-sturgis/" aria-description="Citation for case: People v. Sturgis">58 Ill. 2d 211</a></span>, <span class="citation" data-id="9530537"><a href="/opinion/2046116/people-v-sturgis/" aria-description="Citation for case: People v. Sturgis">317 N. E. 2d 545</a></span> (1974). See also <em>Woody </em>v. <em>United States, </em>126 U. S. App. D. C. 353, 354-355, 379 F, 2d 130, 131-132 (Burger, J.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./389/961/">389 U. S. 961</a></span> (1967).</p>
</footnote>
<footnote label="9">
<p id="b126-8"> This Court has held that “the protective shield of <em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span> </em>is not to be converted into a license for false representations. . . <em>United States </em>v. <em>Kahan, </em><span class="citation" data-id="9425609"><a href="/opinion/108970/united-states-v-kahan/#243" aria-description="Citation for case: United States v. Kahan">415 U. S. 239, 243</a></span> (1974).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Satterfield.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Satterfield
type: case
citation: "743 F.2d 827 (1984)"
parallel_cite: 53 U.S.L.W. 2212
neutral_cite: ""
court: "U.S. Court of Appeals, 11th Cir."
court_level: coa
circuit: ca11
year: 1984
date_decided: ""
docket: ""
authority_weight: "Binding in-circuit — 11th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/8934150/united-states-v-satterfield/"
  cluster_id: 8934150
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Satterfield
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Inevitable Discovery & Independent Source]]"
    role: Illustrates a circuit split
related:
  - "[[The Exclusionary Rule]]"
  - "[[Nix v. Williams]]"
  - "[[Wong Sun v. United States]]"
  - "[[Murray v. United States]]"
  - "[[Stone v. Powell]]"
tags:
  - case
  - fourth-amendment
  - exclusionary-rule
  - inevitable-discovery
  - circuit-split
  - warrantless-search
holding: "For the inevitable-discovery exception to the exclusionary rule to admit illegally seized evidence, the Eleventh Circuit requires not only a reasonable probability that the evidence would have been found by lawful means, but also that the lawful means were possessed by the police and were being actively pursued before the illegal conduct occurred; because officers obtained the search warrant only hours after the warrantless search, the shotgun was not admissible under inevitable discovery — though its erroneous admission was harmless in light of the overwhelming other evidence."
aliases:
  - United States v. Satterfield
  - "United States v. Satterfield (11th Cir. 1984)"
---

# United States v. Satterfield

*743 F.2d 827 (11th Cir. 1984)* · U.S. Court of Appeals for the Eleventh Circuit · **Binding in-circuit — 11th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 8934150 → majority opinion 8924377 (Kravitch, Circuit Judge; 743 F.2d 827, decided Oct. 3, 1984). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*846`). Frontier-split row (role: Illustrates a circuit split): in-circuit binding, persuasive elsewhere; the split posture is named in Treatment (LINT-21). S9 promotes. -->

## Background
After Satterfield and two others kidnapped Pauline Callaway (killing her boyfriend in the process), Alabama deputies traced her to a shack Satterfield had rented. Without an arrest or search warrant, the officers knocked, got no answer, entered, and arrested Satterfield; a brief search of the bedroom yielded clothing, shotgun shells, and a bloodstained pillow. After all occupants had been removed to patrol cars and the house was empty, the officers kept searching for nearly ten minutes and found a shotgun under the cushions of a sofa in an adjoining room. Several hours later, police obtained a warrant for bloodstained clothing. At trial the shotgun was admitted; Satterfield was convicted of kidnapping and challenged the search.

## Issue
Whether the warrantless search that produced the shotgun fell within an exception to the warrant requirement, and, if not, whether the shotgun was nonetheless admissible under the [[Inevitable Discovery and Independent Source|inevitable discovery]] exception to the exclusionary rule because a warrant later issued.

## Rule
The court first held the continued search unjustified by [[Exigent Circumstances and Hot Pursuit|exigent circumstances]], since the occupants were already in custody. It then addressed [[Inevitable Discovery and Independent Source|inevitable discovery]] under *[[Nix v. Williams|Nix]]*, and — reading its own precedent as consistent with *[[Nix v. Williams|Nix]]* — required more than a showing that the evidence would eventually have surfaced: "To qualify for admissibility, there must be a reasonable probability that the evidence in question would have been discovered by lawful means, and the prosecution must demonstrate that the lawful means which made discovery inevitable were possessed by the police and were being actively pursued *prior* to the occurrence of the illegal conduct." — 743 F.2d at 846. ^pin-846

## Application
Because the officers had not yet initiated — indeed did not yet possess — the lawful means (the warrant) that would later have led to the shotgun, the second element failed: the warrant issued only hours after the illegal search. Allowing the government to manufacture a lawful avenue after the fact, the court reasoned, would nearly destroy the requirement of a warrant *before* the search of a home, since a warrant can almost always be obtained afterward. The shotgun therefore should have been suppressed. The court nonetheless affirmed the conviction, holding the erroneous admission harmless [[Common Legal Terms#beyond-a-reasonable-doubt|beyond a reasonable doubt]] given the extensive other evidence of Satterfield's guilt.

## Conclusion
The convictions were **affirmed**; the court held the shotgun was seized unlawfully and should have been excluded, but that its admission was harmless error. Kravitch, Circuit Judge, wrote for the panel.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion.

**Illustrates a circuit split (in-circuit rule).** *Satterfield* states the Eleventh Circuit's rule — binding there, persuasive only elsewhere — that the [[Inevitable Discovery and Independent Source|inevitable discovery]] exception applies only when the police *possessed and were actively pursuing* a lawful means of discovery at the moment of the illegality. That reading of *[[Nix v. Williams]]* divides the circuits: several courts of appeals require such an independent, already-underway line of lawful investigation, while others read *[[Nix v. Williams|Nix]]* to impose no "active pursuit" prerequisite at all — asking only whether the evidence *would* inevitably have been discovered by lawful means, regardless of whether an independent investigation was afoot when the violation occurred. Teach *Satterfield* as one side of that split, not as a nationally settled rule, alongside the independent-source line (*[[Wong Sun v. United States]]*, *[[Murray v. United States]]*) and the deterrence rationale (*[[Stone v. Powell]]*).

## Appears on
- [[The Exclusionary Rule]] — *Illustrates a circuit split*

## Sources
- [*United States v. Satterfield*, 743 F.2d 827 (11th Cir. 1984)](https://www.courtlistener.com/opinion/8934150/united-states-v-satterfield/) — pinpoint: 846 (Kravitch, J.; the CL opinion text carries the reporter star `*846` immediately before the quoted statement of the inevitable discovery elements; "*prior*" preserves the opinion's original emphasis). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "79e94bea5462304c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "743 F.2d 827 (1984)", "court": "U.S. Court of Appeals, 11th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "53 U.S.L.W. 2212", "title": "United States v. Satterfield", "year": "1984"}}
{"assertion_id": "5b6df25000a9040b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "For the inevitable-discovery exception to the exclusionary rule to admit illegally seized evidence, the Eleventh Circuit requires not only a reasonable probability that the evidence would have been found by lawful means, but also that the lawful means were possessed by the police and were being actively pursued before the illegal conduct occurred; because officers obtained the search warrant only hours after the warrantless search, the shotgun was not admissible under inevitable discovery — though its erroneous admission was harmless in light of the overwhelming other evidence.", "title": "United States v. Satterfield"}}
{"assertion_id": "9afc420bf870d04c", "dimension": "support", "kind": "home_role", "locator": {"home": "Inevitable Discovery & Independent Source"}, "payload": {"home": "Inevitable Discovery & Independent Source", "role": "Illustrates a circuit split", "title": "United States v. Satterfield"}}
{"assertion_id": "60f487723e990b7b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Satterfield", "varies_by_point": "false"}}
{"assertion_id": "da3bb948455f3c1b", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 11th Cir.", "title": "United States v. Satterfield"}}
```

### lake record — United States v. Satterfield

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Satterfield",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Satterfield",
    "case_name_short": "Satterfield",
    "case_name_full": "United States v. Edward Eugene SATTERFIELD a/k/a \"Pig\" Satterfield, Perry Don Allison, Carlton Welden, In re UNITED STATES of America",
    "input_case_name": "United States v. Satterfield",
    "court": "U.S. Court of Appeals, 11th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca11",
    "state": null,
    "date_decided": null,
    "year": 1984,
    "docket": null,
    "cluster_id": 8934150,
    "lead_opinion_id": 8924377,
    "sibling_ids": [],
    "absolute_url": "/opinion/8934150/united-states-v-satterfield/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "743 F.2d 827",
      "volume": "743",
      "reporter": "F.2d",
      "page": "827",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "53 U.S.L.W. 2212",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "2212",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "743 F.2d 827",
        "volume": "743",
        "reporter": "F.2d",
        "page": "827",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 2212",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "2212",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "743 F.2d 827",
    "official_selection": {
      "court_class": "coa",
      "selected": "743 F.2d 827",
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
    "date_created": "2026-07-06T13:43:17Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:43:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:43:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:43:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:43:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-satterfield--8934150",
      "to_record_id": "United States v. Satterfield",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Satterfield (truncated)

```
<opinion type="majority">
<author id="b895-11">KRAVITCH, Circuit Judge:</author>
<p id="b895-12">I. FACTS AND PROCEEDINGS</p>
<p id="alj-dedup-1">In this appeal we consider a challenge to the constitutionality of the restitution provisions of the Victim and Witness Protection Act of 1982 (the “VWPA” or “Act”). Appellants Carlton Welden, Edward Eugene Satterfield and Perry Don Allison were convicted by a jury of one count of kidnapping in violation of <span class="citation no-link">18 U.S.C. § 1201</span>(a)(1). The court sentenced Satter-field to life imprisonment, Welden to twenty years and Allison to five years, but refused to order payment to the victim under the VWPA, <span class="citation no-link">18 U.S.C. §§ 3579</span> and 3580, declaring those provisions unconstitutional under the fifth, seventh and fourteenth amendments. Appellants challenge their convictions under the kidnapping statute; the Government cross-appeals the district court’s refusal to order restitution. The Government also petitioned for a writ of mandamus, which has been carried with the appeal, to compel the district court to comply with the restitution statute. We affirm the convictions of all three appellants, reverse the district court’s ruling on the constitutionality of the VWPA, remand to the district court for compliance with the restitution statute, and deny the petition for writ of mandamus in light of our decision on the Government’s cross-appeal.<footnotemark>1</footnotemark></p>
<p id="b895-16">At trial, the Government alleged that, in the early morning hours of April 7, 1983, Satterfield, Welden and Allison kidnapped Pauline Callaway from her trailer home in Hooker, Georgia, after killing her boyfriend, and forced her to accompany them to Flat Rock, Alabama. The evidence showed that the events leading to the kidnapping began at 10:00 p.m. on April 6, 1983, when appellant Allison accompanied his friend Dervin Little in Little’s wife’s 1979 red and maroon Malibu Classic to a graveyard in Georgia. In about ten minutes, they were joined by appellant Welden, who drove up in his automobile and asked to trade cars with Little for the evening. Little departed in Welden’s car, while Wel-den and Allison left in the Malibu. At around 3:00 a.m. the next morning, Pauline Callaway and her boyfriend returned from Callaway’s sister’s home to their trailer. Callaway went to bed immediately, while her boyfriend remained awake. Shortly thereafter, Satterfield, Welden and Allison arrived at the trailer in the Malibu. Allison, the driver, remained in the car while two masked men, later identified by Calla-way as Satterfield and Welden, broke into the trailer, shot and killed the boyfriend, went to the bedroom, and, after removing <page-number citation-index="1" label="832">*832</page-number>Callaway’s clothes, forced her onto the living room couch. When Callaway was unable to tell Satterfield where money and cocaine were hidden in the trailer, he hit her on the head with a shotgun, causing her to bleed profusely and black out.</p>
<p id="b896-4">Callaway awakened in the back seat of the Malibu. She was wearing only her boyfriend’s bluejean jacket, and two of her abductors were holding her at gunpoint. During the ride, she heard Satterfield tell her to keep her head down. She also heard Satterfield ask “Carlton” to lean toward him so he could whisper something in his ear. Later in the trip, she heard the one referred to as “Carlton” mention that they had just killed a man. Callaway could not see the driyer of the car, but observed that he had blondish-brown curly hair.</p>
<p id="b896-5">At one point Satterfield forced Callaway out of the car to perform oral sex, and when she returned she deliberately placed some of the blood from her head on the ear’s interior. When Satterfield later took off his mask, Callaway could see his face, but because it was dark she could not see it very clearly.</p>
<p id="b896-6">At 4:30 or 5:00 a.m., the three men took Callaway to a shack rented by Satterfield, at which time Welden and Allison left. Satterfield dragged Callaway into the unlighted house, threw her on the bed, laid down beside her and passed out. Meanwhile, Welden and Allison went to the home of Patricia Holcomb, Satterfield’s girlfriend. Holcomb spoke with Welden on the porch and saw the Malibu in her driveway with a man behind the wheel. Later that day she told an FBI agent that the man was Allison, but at trial she admitted that she was not certain. Welden told Holcomb that Satterfield, whom she knew as “Pig,” wanted to see her. Welden left, but returned about an hour later in the Malibu and drove Holcomb to Satterfield’s. By this time, Allison was no longer in the car. En route to Satterfield’s shack, Welden told Holcomb that he “might be in a little bit of trouble.”</p>
<p id="b896-7">After Welden let her out in front of Satterfield’s house, Holcomb went through the unlocked front door and found Satter-field with Callaway. Holcomb attempted to wake Satterfield, saying “Pig, Pig, wake up.” When Callaway realized that Satter-field could not be awakened, she tried to get as good a look at him as possible in the dark room. She then escaped and ran to a neighbor’s house to call the police.</p>
<p id="b896-9">Around 6:00 a.m. Deputy Sheriff John Moses of DeKalb County, Alabama, received the police call. He arrived at Satter-field’s neighbor’s house and found Calla-way in hysterics, her face covered with blood. When she calmed down, Callaway told him that three men, two of whom were named Pig and Carlton, had killed a man in Georgia, using a shotgun, and had kidnapped her. After verifying the murder with Georgia authorities, Moses and two other deputies went to Satterfield’s shack. Without an arrest warrant or search warrant, the men knocked on Satterfield’s front door, announced their presence, and, receiving no response, entered the house using a flashlight for illumination. Discovering Satterfield and Holcomb in the bedroom, they promptly arrested Satter-field and, following a brief search of the bedroom, seized a pair of trousers, shotgun shells, a bloodstained pillow and a torn shirt with blood on it. After the deputies took Satterfield and Holcomb to separate patrol cars and determined that the house was empty, they continued to search the shack for nearly ten minutes and found the shotgun underneath the cushions of a sofa in the room adjoining the bedroom. At trial, the Government showed that the bloodstains on the pillow and clothing found in Satterfield’s bedroom matched the blood type of Pauline Callaway, as did the bloodstains in the Malibu. The test on blood stains found on the shotgun, however, was inconclusive.</p>
<p id="b896-10">Carlton Welden was arrested the following day, April 8, 1983, and three days later, police arrested Perry Don Allison. FBI Agent Land testified that Allison was read his <em>Miranda </em>rights upon arrest, but refused to sign a waiver of rights form. The agent also testified that he engaged in cas<page-number citation-index="1" label="833">*833</page-number>ual conversation with Allison during the ride to the police station, during which Allison stated “that he wanted to make it clear that he was not really a mean man, but that he simply had too many people that got him into trouble.”</p>
<p id="b897-5">Following return of the guilty verdicts, appellants and their counsel were given copies of their presentence investigative reports, which included information concerning their financial status and a victim impact statement showing that Pauline Calla-way had incurred $599 in medical bills. The victim impact statement consisted of an unverified report by the Probation Service based upon information Callaway had supplied, and provided no other evidence of injuries sustained or expenses incurred by Callaway or any other victims of the incident. The district court acknowledged that payment of restitution to Callaway was justified under sections 3579 and 3580 of the VWPA, but refused to order payment of the $599 on grounds that the Act violated the defendants’ seventh amendment right to a jury trial, and fifth and fourteenth amendment rights to due process and equal protection of the laws. The court therefore ordered terms of imprisonment without restitution to the victim. In a memorandum opinion, <em>United States v. Welden, </em><span class="citation" data-id="2375645"><a href="/opinion/2375645/united-states-v-welden/" aria-description="Citation for case: United States v. Welden">568 F.Supp. 516</a></span> (N.D.Ala.1983), the trial court explained its holding that the restitution statute is unconstitutional.</p>
<p id="b897-6">The three defendants appealed their convictions under <span class="citation no-link">18 U.S.C. § 1201</span>(a)(1) on several grounds. Satterfield raises four grounds for reversal: (1) the shotgun was seized in violation of his rights under the fourth amendment; (2) he was entitled to a mistrial after the court mistakenly read an unedited version of the indictment that included references to his nickname “Pig”; (3) the introduction of Allison’s statement violated his right to confront his accuser under <em>Bruton v. United States, </em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">391 U.S. 123</a></span>, <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">88 S.Ct. 1620</a></span>, <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">20 L.Ed.2d 476</a></span> (1968); and (4) the in-court identification of him by Pauline Callaway should have been excluded because a previous photographic display during which she identified him was overly suggestive. Welden raises six issues: (1) the introduction of Allison’s statement violated his rights under <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span>; </em>(2) the Government did not prove that he kidnapped Callaway for “ransom or reward or otherwise” as required by <span class="citation no-link">18 U.S.C. § 1201</span>(a)(1); (3) the evidence was insufficient as a matter of law to identify him as one of the captors; (4) the court erred in its ruling on several objections made by his counsel and the prosecutor; (5) the court erroneously declined to give certain requested jury instructions; and (6) the court erred in its decision to sequester the jury during trial. Allison appeals on two grounds: (1) admission of his statement violated his fifth amendment rights; and (2) the evidence was insufficient as a matter of law to identify him as the driver of the vehicle used in the kidnapping.</p>
<p id="b897-8">The Government’s cross-appeal and petition for writ of mandamus challenge the district court’s refusal to order restitution, urging us to enforce the requirement of sections 3579 and 3580 of the VWPA that the sentencing judge order the defendants to pay restitution for specified personal injury or property losses caused by the crime, or state its reasons for ordering less than full restitution.</p>
<p id="b897-9">II. THE VICTIM AND WITNESS PROTECTION ACT OF 1982</p>
<p id="b897-10">Congress enacted the VWPA to improve the treatment of victims and witnesses in the federal criminal justice system. The Act is designed to protect witnesses from harassment and threats by the defendant, increase the involvement of victims in the decisions and progress of the case, and restore victims to as whole a position as possible. S.Rep. No. 532, 97th Cong., 2d Sess. 10, <em>reprinted in </em>1982 U.S. Code Cong. &amp; Ad.News 2515, 2516. One of the stated purposes of the VWPA is “to ensure that the Federal Government does all that is possible within limits of available resources to assist victims and witnesses of crime without infringing on the constitutional rights of the defendant.” <span class="citation no-link">18 U.S.C. § 1512</span> note.</p>
<p id="b898-3"><page-number citation-index="1" label="834">*834</page-number>Two major features of the Act are implicated in this case: (1) the Act broadens a victim’s restitution rights by permitting a sentencing judge to impose restitution in conjunction with any other sentence, <span class="citation no-link">18 U.S.C. §§ 3579</span> and 3580; and (2) the Act amends Rule 32 of the Federal Rules of Criminal Procedure to require the preparation of a victim impact statement as part of the presentence investigative report, to assess the effect of the defendant’s crime on the victim, Fed.R.Crim.P. 32(c)(2).</p>
<p id="b898-4">Restitution has always been one of the options available to a sentencing judge. Prior to the Act, however, restitution could be imposed only as a condition of probation under the Probation Act, <span class="citation no-link">18 U.S.C. § 3651</span>. In the Senate committee report submitted with the VWPA,<footnotemark>2</footnotemark> Congress criticized the courts’ limited use of restitution as a condition of probation, finding that federal criminal courts had “reduc[ed] restitution from being an inevitable if not exclusive sanction to being an occasional afterthought.” S.Rep. No. 532, 97th Cong., 2d Sess. 30, <em>reprinted in </em>1982 U.S.Code Cong. &amp; Ad. News 2536. Under the new legislation, restitution may be imposed not only in conjunction with probation, but also in addition to incarceration and/or fine, or even as an independent sentence. As a means of encouraging frequent use of the restitution option, the court is required to state its reasons on the record if it decides not to order full restitution to the crime victim in each case. <span class="citation no-link">18 U.S.C. § 3579</span>(a)(2).</p>
<p id="b898-15">The Act amends subsection (c)(2) of Fed. R.Crim.P. 32<footnotemark>3</footnotemark> to require that the presentence investigative report, which is prepared for the court by the Probation Service, include a statement containing information about the financial, social, psychological and medical impact on the victim of the crime, or any other information that may aid the court in ordering restitution. The court will use this victim impact statement to determine the defendant’s restitution liability. <em>See </em>S.Rep. No. 532, 97th Cong., 2d Sess. 11-13, <em>reprinted in </em>1982 U.S.Code Cong. &amp; Ad.News 2517-19.</p>
<p id="b898-16">The provisions of the VWPA authorizing restitution awards, §§ 3579 &amp; 3580, are set forth in their entirety in the margin.<footnotemark>4</footnotemark> Subsection 3579(a)(1) permits the court to order <page-number citation-index="1" label="835">*835</page-number>restitution in addition to or in lieu of any other sentence, and, if imprisonment is ordered, restitution may become a condition of subsequent parole or probation. <span class="citation no-link">18 U.S.C. § 3579</span>(a)(1), (g). Subsection 3579(b) enumerates the types of property damage and bodily injury expenses the victim may recover. The court also may order that restitution, including funeral expenses, be paid to the estate of a deceased victim, and, <page-number citation-index="1" label="836">*836</page-number>with the consent of the victim or his estate, make restitution payable in services in lieu of money. <span class="citation no-link">18 U.S.C. § 3579</span>(b)(3), (b)(4), (c).</p>
<p id="b900-4">Subsection 3580(a) broadly defines the factors the court may consider in ordering restitution. They include the amount of loss sustained by the victim as a result of the offense, the financial resources of the defendant, the financial needs and earning ability of the defendant and his dependents, and other factors the court deems appropriate. Subsection 3580(c) directs the court to disclose to the defendant and the Government “all portions” of the victim impact statement prepared by the Probation Service, and subsection 3580(d) specifies that any dispute about the proper amount or type of restitution should be resolved by the court by a preponderance of the evidence. The Government must carry the burden of proof as to the victim’s loss, and in mitigation the defendant may demonstrate the extent of his financial resources and needs.</p>
<p id="b900-5">According to subsection 3579(h), restitution orders may be enforced in a civil action by the victim or the United States. The Act also reduces the victim’s burden of establishing the defendant’s liability in a subsequent suit brought for additional damages for pain and suffering, punitive damages or other injuries not covered by the restitution order; subsection 3580(e) states that a defendant convicted of an offense for which restitution has been ordered shall be estopped from denying the essential allegations of that offense in a subsequent federal or state proceeding brought by the victim. To prevent double recovery, subsection 3579(e)(2) provides that an amount paid to a victim as restitution shall be set off against any compensatory damages later recovered in a civil proceeding.</p>
<p id="b900-6">III. CONSTITUTIONALITY OF THE VWPA</p>
<p id="b900-7">The district court declared sections 3579 and 3580 of the Act unconstitutional on their face under the seventh, fifth and fourteenth amendments. We address each in turn.</p>
<p id="b900-10">A. <em>Seventh Amendment</em></p>
<p id="b900-11">The seventh amendment guarantees the right to a jury trial in suits “at common law, where the value in controversy shall exceed twenty dollars.” U.S. Const, amend. VII. The district court held that the restitution statute violates this amendment by creating a civil action at common law without giving either the victim or the defendant the opportunity to have the defendant’s restitution liability determined by a jury. In so holding, the court was persuaded that the collateral estoppel and civil enforcement provisions of the Act converted an otherwise criminal sentencing hearing into a civil proceeding.<footnotemark>5</footnotemark></p>
<p id="b900-12">The characterization of a penalty as civil or criminal is a question of legislative intent. <em>United States v. Ward, </em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/#248" aria-description="Citation for case: United States v. Ward">448 U.S. 242, 248</a></span>, <span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/#2641" aria-description="Citation for case: United States v. Ward">100 S.Ct. 2636, 2641</a></span>, <span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/" aria-description="Citation for case: United States v. Ward">65 L.Ed.2d 742</a></span> (1980). In drafting the restitution provisions of the VWPA, Congress made clear in both the language of the statute and its accompanying legislative history that victim restitution would be imposed as a criminal, rather than civil, penalty. Subsection 3579(a)(1) allows the court to order restitution “in addition to or in lieu of any other penalty authorized by law” as part of the “sentencing” of a defendant. <span class="citation no-link">18 U.S.C. § 3579</span>(a)(1).</p>
<p id="b900-13">Consistent with this characterization of restitution as part of a criminal sentence are subsections 3580(a) and (b), which incorporate the restitution order into the traditional sentencing role of the court. Under subsection 3580(a), the court can order restitution only after it considers the financial resources of the defendant, his earning ability and the financial needs of his de<page-number citation-index="1" label="837">*837</page-number>pendents. These considerations, which help tailor restitution to the individuality of the defendant, are vital to the rehabilitation goals of sentencing,<footnotemark>6</footnotemark> but generally are not relevant in determining the amount of damages awarded in a civil case. Subsection 3580(b) authorizes the court to order its probation service to prepare and submit, as part of its presentence report, information pertaining to the loss of the victim and the financial status of the defendant. Congress’ decision to involve the probation service in the development of the facts supporting a restitution order further reveals an intent to treat restitution as one of the options available to the district court in imposing an appropriate sentence.<footnotemark>7</footnotemark></p>
<p id="b901-5">The legislative history of the VWPA reenforces our conclusion that Congress intended to make restitution an element of the criminal sentencing process and not an independent action civil in nature. The history is replete with references to restitution as part of the criminal sentence. <em>See, e.g., </em>S.Rep.No. 532, 97th Cong., 2d Sess. 30, <em>reprinted in </em>1982 U.S.Code Cong. &amp; Ad. News 2515, 2536 (“restitution ... lost its priority status in the sentencing procedures of our federal courts long ago”); <span class="citation no-link"><em>id. </em>at 32</span>, <em>reprinted in </em>1982 U.S.Code Cong. <em>&amp; </em>Ad. News 2515, 2538 (“permitting its use in conjunction with imprisonment, fine, suspended sentence, or other sentence imposed by the court”); 128 Cong.Rec. H8467 (daily ed. Oct. 1, 1982) (statement of Representative McCollum) (“Restitution would become a sentence that could, in and of itself, be imposed____ This legislation does not intend that restitution become a substitute for civil damages____”).<footnotemark>8</footnotemark> <em>See also United States v. Richard, </em><span class="citation" data-id="438777"><a href="/opinion/438777/united-states-v-john-edward-richard/#1122" aria-description="Citation for case: United States v. John Edward Richard">738 F.2d 1120 at 1122</a></span> (10th Cir.1984) (“order of restitution under sections 3579 and 3580 is a part of the sentencing process”).</p>
<p id="b901-12">There can be little doubt that Congress intended the restitution penalties of the VWPA to be incorporated into the traditional sentencing structure. Despite this demonstrated legislative intent, however, the district court held that by including a civil enforcement mechanism and a collateral estoppel provision in the statute Congress did not implement its scheme in a constitutional manner and essentially'created a hybrid proceeding having sufficient civil action characteristics to trigger the protections of the seventh amendment. We do not agree.</p>
<p id="b901-13">1. Collateral Estoppel</p>
<p id="b901-14">Subsection 3580(e) of the VWPA provides:</p>
<blockquote id="b901-15">A conviction of a defendant for an offense involving the act giving rise to restitution under this section shall estop the defendant from denying the essential allegations of that offense in any subsequent Federal civil proceeding or State civil proceeding, to the extent consistent with the State law, brought by the victim.</blockquote>
<p id="b901-16">The district court held that a hearing having collateral estoppel effects must be construed as the equivalent of a suit at common law. The court understood section 3580(e) as necessarily giving collateral es-toppel effect in subsequent civil actions to <page-number citation-index="1" label="838">*838</page-number>all of the facts underlying a restitution order. Were we to follow this interpretation, we might agree that the restitution order has the characteristics of a civil judgment, but we do not read the Act so broadly. The section merely states that a “conviction” of a defendant for an offense giving rise to a restitution order shall estop the defendant from denying “the essential allegations <em>of that offense” </em>in a subsequent civil proceeding. <span class="citation no-link">18 U.S.C. § 3580</span>(e) (emphasis added). The defendant is barred from challenging in a later proceeding only those facts underlying the criminal offense that were necessarily decided by the jury’s verdict. The Act’s collateral estoppel provision would not apply to those facts supporting the restitution <em>order </em>— e.g., the extent and nature of the victim’s injury or the value of damaged property — that were not part of the essential allegations underlying the criminal conviction.</p>
<p id="b902-4">Subsection 3580(e) does no more than codify the rule in this and other circuits that a criminal conviction may be used as conclusive proof of some issues in a subsequent civil litigation. <em>See, e.g., Raiford v. Abney, </em><span class="citation" data-id="411803"><a href="/opinion/411803/in-the-matter-of-harlan-charles-raiford-ii-harlan-charles-raiford-ii/#523" aria-description="Citation for case: In the Matter of Harlan Charles Raiford, Ii. Harlan...">695 F.2d 521, 523</a></span> (11th Cir.1983); <em>United States v. Podell, 572 </em>F.2d 31, 35 (2d Cir.1978). Under this doctrine of collateral estoppel, a party is precluded from litigating an issue only if the identical issue has been actually litigated in a prior suit that could not have been decided without resolving the issue. <em>Precision Air Parts, Inc. v. Avco Corp., </em><span class="citation" data-id="437359"><a href="/opinion/437359/precision-air-parts-inc-v-avco-corporation/#1501" aria-description="Citation for case: Precision Air Parts, Inc. v. Avco Corporation">736 F.2d 1499, 1501-02</a></span> (11th Cir.1984). What issues were actually litigated in the criminal proceeding is a factual question that must be determined on a case-by-case basis. <span class="citation" data-id="437359"><a href="/opinion/437359/precision-air-parts-inc-v-avco-corporation/#1502" aria-description="Citation for case: Precision Air Parts, Inc. v. Avco Corporation"><em>Id. </em>at 1502</a></span>. Subsection 3580(e) does not expand this rule. The facts underlying a criminal offense that gives rise to a restitution order will be given collateral estoppel effect only if they were fully and fairly litigated at the criminal trial, or stipulated through a guilty plea. <em>See Raiford, </em><span class="citation" data-id="411803"><a href="/opinion/411803/in-the-matter-of-harlan-charles-raiford-ii-harlan-charles-raiford-ii/#523" aria-description="Citation for case: In the Matter of Harlan Charles Raiford, Ii. Harlan...">695 F.2d at 523</a></span> (guilty plea given same collateral estoppel effect as any other criminal convictions; plea of <em>nolo contendere </em>distinguished). The collateral estoppel provision of the VWPA does not contravene congressional intent, convert the restitution aspect of the sentencing hearing into a civil proceeding, or deny the defendant his right to a jury trial under the seventh amendment.</p>
<p id="b902-6">2. Civil Enforcement</p>
<blockquote id="Al1">Subsection 3579(h) provides:</blockquote>
<blockquote id="b902-7">An order of restitution may be enforced by United States or a victim named in the order to receive the restitution in the same manner as a judgment in a civil action.</blockquote>
<p id="b902-8">The district court did not explain why this procedure for enforcing a restitution order transforms the criminal sentencing hearing into an action at common law. The provision simply makes the civil judgment enforcement mechanism available to the United States or the victim following an order of restitution.</p>
<p id="b902-9">In enacting the VWPA, Congress wanted to ensure that victims of crime would be restored to their prior state of well-being. S.Rep. No. 532, 97th Cong., 2d Sess. 30, <em>reprinted in </em>1982 U.S.Code Cong. &amp; Ad. News 2536. This goal would be accomplished only if victims were assured of recovering the restitution awarded by the court. Aware that restitution awards under the Probation Act, <span class="citation no-link">18 U.S.C. § 3651</span>, were infrequently used and indifferently enforced, Congress enacted subsection 3579(h) to remedy this problem and facilitate the collection process. S.Rep. No. 532, 97th Cong., 2d Sess. 30, <em>reprinted in </em>1982 U.S.Code Cong. &amp; Ad.News 2536.</p>
<p id="b902-10">Civil enforcement of criminal penalties is not a new concept. Section 3565 of Title 18 already gives the United States the right to collect a criminal penalty “by execution against jthe property of the defendant in like mahner as judgments in civil cases.” Under both section 3565 and subsection 3579(h), the Government may employ the enforcement procedures of Fed.R.Civ.P. 64 and 69(a) to collect criminal penalties. <em>See United States v. Thornton, </em><span class="citation" data-id="400067"><a href="/opinion/400067/united-states-v-benjamin-t-thornton-prince-georges-county-maryland/" aria-description="Citation for case: United States v. Benjamin T. Thornton, Prince George&#x27;s...">672 F.2d 101</a></span> (D.C.Cir.1982); S.Rep. No. 532, 97th Cong., 2d Sess. 33, <em>reprinted in </em>1982 U.S.Code Cong. &amp; Ad.News 2539. The VWPA mere<page-number citation-index="1" label="839">*839</page-number>ly extends this right to the victims themselves. The inclusion of this civil enforcement provision does not transform the restitution order into an action at common law.<footnotemark>9</footnotemark></p>
<p id="b903-5">B. <em>Due Process</em></p>
<p id="b903-6">The district court held tfrat the VWPA did not provide the sentencing judge with sufficiently “ascertainable standards” to comply with the due process requirements of fairness and non-arbitrary exercise of power. In an exhaustive review of the VWPA, the court found fault in the statute’s failure to address dozens of potentially troublesome issues such as the standard for admissibility of evidence, the possible applicability of discovery procedures, and the requirements for ensuring adequate notice to the defendant. The possibility that due process violations will occur in particular cases in the future, however, does not render the statute unconstitutional on its face.</p>
<p id="b903-11">We agree with the district court’s observation that the statute is written in general terms and creates many questions the courts will have to answer.<footnotemark>10</footnotemark> The statute presents unresolved questions affecting the defendant's ability to obtain prior notice of his potential restitution liability and his right to contest the facts supporting that liability before the award is made. Appellants specifically question the adequacy of the procedural safeguards at the sentencing phase,<footnotemark>11</footnotemark> where the Act provides few standards governing the procedures to be used for determining the restitution owing the victim or the ability of the defendant to pay. For instance, the statute does not prohibit the use of hearsay evidence and is silent on the defendant’s right, if any, to cross-examine or call his own witnesses.<footnotemark>12</footnotemark></p>
<p id="b904-3"><page-number citation-index="1" label="840">*840</page-number>In assessing the effect of these shortcomings of the YWPA on the fifth amendment rights of the defendant, we begin with the basic proposition that due process assures the defendant he will be given adequate notice and an opportunity to contest the facts relied upon to support his criminal penalty. <em>See Townsend v. Burke, </em><span class="citation" data-id="104579"><a href="/opinion/104579/townsend-v-burke/#741" aria-description="Citation for case: Townsend v. Burke">334 U.S. 736, 741</a></span>, <span class="citation" data-id="104579"><a href="/opinion/104579/townsend-v-burke/#1255" aria-description="Citation for case: Townsend v. Burke">68 S.Ct. 1252, 1255</a></span>, <span class="citation" data-id="104579"><a href="/opinion/104579/townsend-v-burke/" aria-description="Citation for case: Townsend v. Burke">92 L.Ed. 1690</a></span> (1948). It is now well settled that the sentencing process as well as the trial itself must satisfy these requirements. <em>See Shelton v. United States, </em><span class="citation" data-id="319328"><a href="/opinion/319328/charles-shelton-v-united-states/#159" aria-description="Citation for case: Charles Shelton v. United States">497 F.2d 156, 159</a></span> (5th Cir.1974). The defendant need not, however, be accorded the same degree of due process protections during the sentencing phase as was required at the criminal trial. <em>United States v. Stephens, </em><span class="citation" data-id="414135"><a href="/opinion/414135/united-states-v-james-michael-stephens/#537" aria-description="Citation for case: United States v. James Michael Stephens">699 F.2d 534, 537</a></span> (11th Cir.1983). <em>Cf. Proffitt v. Wainwright, </em><span class="citation" data-id="9469588"><a href="/opinion/407646/charles-william-proffitt-v-louie-l-wainwright-secretary-florida/#1254" aria-description="Citation for case: Charles William Proffitt v. Louie L. Wainwright,...">685 F.2d 1227, 1254-55</a></span> (11th Cir.1982) (due process protections greater at capital sentencing than at noncapital), <em>mod. on reh’g, </em><span class="citation" data-id="417826"><a href="/opinion/417826/charles-william-proffitt-v-louie-l-wainwright-secretary-florida/" aria-description="Citation for case: Charles William Proffitt v. Louie L. Wainwright,...">706 F.2d 311</a></span> (11th Cir.1983), <em>cert. denied, </em>— U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./104/508/">104 S.Ct. 508</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/78/697/">78 L.Ed.2d 697</a></span> (1984). The sole interest being protected is the right not to be sentenced on the basis of invalid premises or inaccurate information. <em>United States v. Hodges, </em><span class="citation" data-id="345753"><a href="/opinion/345753/united-states-v-marvin-eugene-hodges/#369" aria-description="Citation for case: United States v. Marvin Eugene Hodges">556 F.2d 366, 369</a></span> (5th Cir.1977), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./434/1016/">434 U.S. 1016</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./98/735/">98 S.Ct. 735</a></span>, <span class="citation no-link">54 L.Ed.2d 762</span> (1978). Because the sentencing procedure is not a trial, courts have limited this right in order to prevent the sentencing hearing from becoming a full-scale evidentiary hearing. <em>Stephens, </em><span class="citation" data-id="414135"><a href="/opinion/414135/united-states-v-james-michael-stephens/#537" aria-description="Citation for case: United States v. James Michael Stephens">699 F.2d at 537</a></span>; <em>United States v. Espinoza, </em><span class="citation" data-id="312279"><a href="/opinion/312279/united-states-v-eliseo-espinoza-jr/" aria-description="Citation for case: United States v. Eliseo Espinoza, Jr.">481 F.2d 553</a></span> (5th Cir.1973). The degree of protection required is only that which is necessary to ensure that the district court is sufficiently informed to enable it to exercise its sentencing discretion in an enlightened manner. <em>Stephens, </em><span class="citation" data-id="414135"><a href="/opinion/414135/united-states-v-james-michael-stephens/#537" aria-description="Citation for case: United States v. James Michael Stephens">699 F.2d at 537</a></span>.</p>
<p id="b904-6">Although we believe it is possible for a defendant in a particular case to have his right to a fair sentencing hearing violated by the arbitrary imposition of restitution, we conclude that the VWPA, together with the dictates of Rule 32, contains sufficient safeguards to ensure that a sentencing judge, exercising appropriate discretion, will award restitution based on accurate facts and premises. The Act supplies the basic framework for determining the amount of restitution. Subsection 3580(a) provides that before ordering restitution the court must consider the amount of loss sustained by the victims, the financial condition of the defendants, and any other factors the court deems appropriate. The Act places the burden on the Government to prove by a preponderance of the evidence the amount of loss resulting from the offense; the defendant must demonstrate the financial needs of himself and his dependents by the same standard. <span class="citation no-link">18 U.S.C. § 3580</span>(d). Although the only reference to the source of this relevant information is found at subsection 3580(b), which authorizes the court to order the Probation Service to prepare a victim impact statement as part of the presentence report, nothing in the statute prevents the court from hearing testimony or receiving other evidence relevant to its inquiry. Rule 32(a)(1)(C) creates additional procedural protection by assuring the defendant the opportunity “to make a statement in his own behalf and to present any information in mitigation of punishment.”</p>
<p id="b904-10">Although a noncapital defendant does not have a constitutional right to call and cross-examine witnesses to rebut information contained in the presentence report, <em>United States v. Ashley, </em><span class="citation" data-id="345503"><a href="/opinion/345503/united-states-v-joe-lee-ashley-aka-john-doe-gwenniece-leveritte-and/#466" aria-description="Citation for case: United States v. Joe Lee Ashley, A/K/A John Doe,...">555 F.2d 462, 466</a></span> (5th Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./434/869/">434 U.S. 869</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./98/210/">98 S.Ct. 210</a></span>, <span class="citation no-link">54 L.Ed.2d 147</span> (1977), Rule 32(c)(3)(A) gives him the right to comment on the report and correct any alleged factual inaccuracies contained in it. The right to rebut information contained in a presentence report also has been expressly recognized in the courts. <em>See United States v. Aguero-Segovia, </em><span class="citation" data-id="378250"><a href="/opinion/378250/united-states-v-david-aguero-segovia-and-armando-acosta-martinez/#132" aria-description="Citation for case: United States v. David Aguero-Segovia and Armando...">622 F.2d 131, 132</a></span> (5th Cir.1980). This right is especially important when, as is likely in the context of restitu<page-number citation-index="1" label="841">*841</page-number>tion, a sentencing judge explicitly relies on certain information in setting a sentence. <em>Espinoza, </em><span class="citation" data-id="312279"><a href="/opinion/312279/united-states-v-eliseo-espinoza-jr/#556" aria-description="Citation for case: United States v. Eliseo Espinoza, Jr.">481 F.2d at 556</a></span>. The defendant facing restitution is further protected by Rule 32(c)(3)(D), which requires the trial court to make a factual finding on the record if the defendant challenges the accuracy of the information contained in the presentence report and relied upon by the sentencing judge. This rule presumably will apply to the victim impact statement as well. This should facilitate appellate review and help ensure that the sentence will not be based on inaccurate facts. If the rights delineated in Rule 32 are enforced by the sentencing judge, the defendant should be afforded timely notice and an opportunity to respond to the statements made in that report.</p>
<p id="b905-4">Addressing the many other concerns of the district court, we conclude only that the VWPA and Rule 32 provide a sentencing judge with the basic tools necessary to award restitution constituting fair compensation to the victim while protecting the rights of the defendant. Congress wisely has determined that the court should be provided “some flexibility in determining the kind of restitution which would both satisfy the victim and provide maximum rehabilitative incentives to the offender.” S.Rep. No. 532, 97th Cong., 2d Sess. 32, <em>reprinted in </em>1982 U.S.Code Cong. &amp; Ad.News 2538. The sentencing judge should be given wide discretion to individualize the sentence to suit the defendant’s character, social history, and other peculiarities of the case,<footnotemark>13</footnotemark> and the statute was drafted without unduly inhibiting that freedom. The guidelines provided in the VWPA are more extensive and specific than any appearing in the restitution provision of the Probation Act,<footnotemark>14</footnotemark> which judges have been applying for years. As with any newly-enacted legislation, the courts will have to resolve many questions of interpretation, some of which have been foreshadowed by the district court in this case; but this lack of precision does not render the statute constitutionally deficient under the due process clause.</p>
<p id="b905-9">C. <em>Equal Protection</em></p>
<p id="b905-10">The district court also declared the restitution provisions of the VWPA unconstitutional under the equal protection clause of the fourteenth amendment. In the course of its discussion of various constitutional principles, the court raised two concerns that could be characterized as implicating the guarantee that no individual shall be denied equal protection of the laws. Neither of these concerns supports the court’s conclusion that the statute is unconstitutional on its face.</p>
<p id="b905-11">The court first held that the lack of ascertainable standards in the Act would result in such widely disparate sentences imposed by the various district courts that offenders necessarily would not be treated equally. Even if the court’s premise is correct, disparate treatment of similarly situated individuals at sentencing is hot constitutionally impermissible. The Supreme Court has recognized that the “Constitution permits qualitative differences in meting out punishment and there is no requirement that two persons convicted of the same offense receive identical sentences.” <em>Williams v. Illinois, </em><span class="citation" data-id="9424339"><a href="/opinion/108194/williams-v-illinois/" aria-description="Citation for case: Williams v. Illinois">399 U.S. 235</a></span>, <span class="citation" data-id="9424339"><a href="/opinion/108194/williams-v-illinois/#2023" aria-description="Citation for case: Williams v. Illinois">90 S.Ct. 2018, 2023</a></span>, <span class="citation" data-id="9424339"><a href="/opinion/108194/williams-v-illinois/" aria-description="Citation for case: Williams v. Illinois">26 L.Ed.2d 586</a></span> (1970). A sentencing authority must be given wide latitude in fixing the punishment for convicted offenders. The VWPA encourages individualized sentencing by directing the court to fix a restitution award based on the particular injuries inflicted on the victim and the financial needs of the defendant and his family. <span class="citation no-link">18 U.S.C. <page-number citation-index="1" label="842">*842</page-number>§ 3580</span>(a). When this discretion is carefully exercised, disparate results must be expected. The likelihood of disparate awards provides no basis for invalidating the statute.</p>
<p id="b906-4">The second equal protection issue raised below requires a construction of subsection 3579(g), which provides:</p>
<blockquote id="b906-5">If such defendant is placed on probation or parole under this title, any restitution ordered under this section shall be a condition of such probation or parole. <em>The court may revoke probation and the Parole Commission may revoke parole if the defendant fails to comply with such order. </em>In determining whether to revoke probation or parole, the court or Parole Commission shall consider the defendant’s employment status, earning ability, financial resources, the willfulness of the defendant’s failure to pay, and any other special circumstances that may have a bearing on the defendant’s ability to pay.</blockquote>
<p id="b906-6">This provision authorizes revocation of parole or probation if the defendant fails to comply with the restitution order. The only conditions the revoking body is required to consider are the defendant’s willfulness in failing to satisfy the order, his financial ability to pay and any other circumstances that might affect his ability to comply. The question arises whether this subsection must be held unconstitutional in light of the Supreme Court’s decision in <em>Bearden v. Georgia, </em><span class="citation" data-id="9429208"><a href="/opinion/110941/bearden-v-georgia/" aria-description="Citation for case: Bearden v. Georgia">461 U.S. 660</a></span>, <span class="citation" data-id="9429208"><a href="/opinion/110941/bearden-v-georgia/" aria-description="Citation for case: Bearden v. Georgia">103 S.Ct. 2064</a></span>, <span class="citation" data-id="9429208"><a href="/opinion/110941/bearden-v-georgia/" aria-description="Citation for case: Bearden v. Georgia">76 L.Ed.2d 221</a></span> (1983). In <em>Bear-den, </em>which was decided after the enactment of the VWPA but which concerned revocation of probation for failure to pay a fine and restitution ordered by a state court, the Court held that if a probationer has made all reasonable efforts to pay the fine or restitution, yet cannot do so through no fault of his own, it is fundamentally unfair to revoke probation automatically “without considering whether alternative methods of punishing the defendant are available.”<footnotemark>15</footnotemark> <em><span class="citation" data-id="9429208"><a href="/opinion/110941/bearden-v-georgia/" aria-description="Citation for case: Bearden v. Georgia">Id.</a></span> </em>461 U.S. at-, <span class="citation" data-id="9429208"><a href="/opinion/110941/bearden-v-georgia/#2071" aria-description="Citation for case: Bearden v. Georgia">103 S.Ct. at 2071</a></span>. Because subsection 3579(g) automatically makes a restitution award a condition of probation or parole, this principle of fairness should also apply to revocation of probation or parole follow-, ing the defendant’s failure to pay restitution awarded under the VWPA.</p>
<p id="Abs"><em><span class="citation" data-id="9429208"><a href="/opinion/110941/bearden-v-georgia/" aria-description="Citation for case: Bearden v. Georgia">Bearden</a></span> </em>creates two threshold criteria a court must consider in revocation proceedings: whether the defendant has made a bona fide effort to pay; and, if he has done so and still cannot comply, whether alternative measures of punishment are available. <em><span class="citation" data-id="9429208"><a href="/opinion/110941/bearden-v-georgia/" aria-description="Citation for case: Bearden v. Georgia">Id.</a></span> </em>461 U.S. at -, <span class="citation" data-id="9429208"><a href="/opinion/110941/bearden-v-georgia/#2073" aria-description="Citation for case: Bearden v. Georgia">103 S.Ct. at 2073</a></span>. Section 3579(g) incorporates the first consideration, but not the second. The court or the Parole Commission, under a strict application of subsection 3579(g), could revoke the probation or parole of an indigent who is making good faith efforts to pay his VWPA restitution liability, without considering means of punishment, other than imprisonment, that would satisfy the pena-logical interests of the Government. According to <em><span class="citation" data-id="9429208"><a href="/opinion/110941/bearden-v-georgia/" aria-description="Citation for case: Bearden v. Georgia">Bearden</a></span>, </em>revocation imposed under such circumstances would be unconstitutional.</p>
<p id="b906-13">The absence of an express requirement in subsection 3579(g) that revocation cannot occur unless alternative punishments are considered does not render the statute unconstitutional on its face, however, because the provision can, and should, be construed in a constitutional manner. <em>See International Association of Machinists v. Street, </em><span class="citation" data-id="9422287"><a href="/opinion/106288/international-assn-of-machinists-v-street/" aria-description="Citation for case: International Ass&#x27;n of MacHinists v. Street">367 U.S. 740</a></span>, <span class="citation" data-id="9422287"><a href="/opinion/106288/international-assn-of-machinists-v-street/#1790" aria-description="Citation for case: International Ass&#x27;n of MacHinists v. Street">81 S.Ct. 1784, 1790</a></span>, <span class="citation" data-id="9422287"><a href="/opinion/106288/international-assn-of-machinists-v-street/" aria-description="Citation for case: International Ass&#x27;n of MacHinists v. Street">6 L.Ed.2d 1141</a></span> (1961) (federal statutes are to be construed as to avoid serious doubt of their constitutionality). This section provides only that the court or Parole Commission “may” revoke probation or parole if the defendant does not make restitution, and that the revocation proceeding must take into account the defendant’s financial ability and willingness to pay. It does not preclude the revoking body from considering any other factors deemed relevant or <page-number citation-index="1" label="843">*843</page-number>constitutionally required. Under the Act, the court or Parole Commission may, and under <em><span class="citation" data-id="9429208"><a href="/opinion/110941/bearden-v-georgia/" aria-description="Citation for case: Bearden v. Georgia">Bearden</a></span> </em>must, consider alternative means of punishment before revoking probation or parole upon the defendant’s failure, despite good-faith efforts, to pay restitution to the victim.</p>
<p id="b907-5">Because the statute can be applied in a constitutional manner, we reverse the district court’s conclusion that it is unconstitutional on its face and remand for further proceedings.</p>
<p id="b907-6">. IV. ADMISSIBILITY OF SHOTGUN</p>
<p id="b907-7">Appellant Satterfield contends that the trial court erred in overruling his motion to suppress the shotgun seized from his residence at the time of his arrest. Deputy Sheriff John Moses testified that when he spoke with Callaway at 6:45 a.m., in the house next door to Satterfield’s, she told him that she had witnessed a murder, that the killers had used a shotgun, that a man named Pig was next door with a woman, and that another man named Carlton, who had participated in the murder and kidnapping, was no longer there. After verifying the homicide with the sheriff’s department, Moses called for assistance. Approximately thirty minutes later, he and two backup officers walked over to appellant’s house, announced their presence and, receiving no response, entered the home using a flashlight for illumination. Moses testified that they had obtained neither an arrest warrant nor a search warrant because a warrant probably could not have been acquired for several hours, during which time the occupants might have escaped. The officers moved through the living room, found Satterfield in bed with his girlfriend, Patricia Holcomb, and immediately arrested him.</p>
<p id="b907-8">Once inside the bedroom, the officers seized Satterfield’s trousers, shotgun shells in the pockets, a bloodstained pillow and a torn shirt. When a brief search failed to locate the shotgun in the bedroom, Satter-field and Holcomb were taken outside and placed in separate patrol cars. After the police had ascertained that there was no one else in the house, the search of Satter-field’s residence continued, and approximately ten minutes later the shotgun was discovered underneath the cushions of a sofa in a room adjoining the bedroom.</p>
<p id="b907-10">A. <em>The Exigent Circumstances Exception</em></p>
<p id="b907-11">Although a warrantless search and seizure in a home is presumed to be unreasonable, <em>Payton v. New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U.S. 573, 586</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1380" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371, 1380</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980), courts will uphold searches of homes based on both probable cause and exigent circumstances. <em>Vale v. Louisiana, </em><span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/" aria-description="Citation for case: Vale v. Louisiana">399 U.S. 30</a></span>, <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/" aria-description="Citation for case: Vale v. Louisiana">90 S.Ct. 1969</a></span>, <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/" aria-description="Citation for case: Vale v. Louisiana">26 L.Ed.2d 409</a></span> (1970); <em>Warden v. Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U.S. 294</a></span>, <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">87 S.Ct. 1642</a></span>, <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">18 L.Ed.2d 782</a></span> (1967). The existence of probable cause is not disputed. Callaway’s statement that a shotgun was used in the murder, coupled with the discovery of bloodstained items in Satterfield’s house, was sufficient for a reasonably cautious officer to believe that the shotgun was in the building. <em>See United States v. Rojas, </em><span class="citation" data-id="399468"><a href="/opinion/399468/united-states-v-maria-lilia-rojas/#165" aria-description="Citation for case: United States v. Maria Lilia Rojas">671 F.2d 159, 165</a></span> (5th Cir. Unit B 1982). The presence of exigent circumstances, however, is not as obvious. The Government maintains that an immediate search for the shotgun was justified because the officers knew at least one other suspect was still at large and could return to Satterfield’s home at any moment to retrieve the weapon, thus presenting a danger to their safety and the welfare of the community. Because only three policemen were present at the scene, two of whom were needed to transport appellant and Holcomb to the station, the Government asserts that it would have been difficult and dangerous for the remaining officer to secure the house against the other suspect for a period of several hours while a search warrant was being issued.</p>
<p id="b907-12">The exigent circumstances exception to the warrant requirement encompasses a variety of common situations, including hot pursuit of a suspect, <em>United States v. Santana, </em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#42" aria-description="Citation for case: United States v. Santana">427 U.S. 38, 42-43</a></span>, <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#2409" aria-description="Citation for case: United States v. Santana">96 S.Ct. 2406, 2409-2410</a></span>, <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">49 L.Ed.2d 300</a></span> (1976); mobility of a vehicle, <em>Chambers v. Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 <page-number citation-index="1" label="844">*844</page-number>U.S. 42</a></span>, <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">90 S.Ct. 1975</a></span>, <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">26 L.Ed.2d 419</a></span> (1970); risk of removal or destruction of evidence, <em>United States v. Rubin, </em><span class="citation" data-id="308715"><a href="/opinion/308715/united-states-v-paul-gary-rubin-united-states-of-america-v-louis-martin/" aria-description="Citation for case: United States v. Paul Gary Rubin United States of America...">474 F.2d 262</a></span> (3d Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./414/833/">414 U.S. 833</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./94/173/">94 S.Ct. 173</a></span>, <span class="citation no-link">38 L.Ed.2d 68</span> (1973); and danger to arresting officers or the public, <em>Warden v. Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U.S. 294</a></span>, <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">87 S.Ct. 1642</a></span>, <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">18 L.Ed.2d 782</a></span> (1967). Invoking the <em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span> </em>exception, as construed in <em>United States v. Burgos, </em><span class="citation" data-id="427222"><a href="/opinion/427222/united-states-v-noe-burgos/" aria-description="Citation for case: United States v. Noe Burgos">720 F.2d 1520</a></span> (11th Cir.1983), and <em>United States v. Quigley, </em><span class="citation" data-id="382343"><a href="/opinion/382343/united-states-v-neil-mathew-quigley-aka-charles-atchley-and-ted-roberts/" aria-description="Citation for case: United States v. Neil Mathew Quigley, A/K/A Charles...">631 F.2d 415</a></span> (5th Cir.1980), the Government contends that an immediate search of Satterfield’s house was justified because the delay involved in obtaining a warrant would have endangered the police or the public. We disagree.</p>
<p id="b908-4">The exigent circumstances doctrine applies only when the inevitable delay incident to obtaining a warrant must give way to an urgent need for <em>immediate action. Burgos, </em><span class="citation" data-id="427222"><a href="/opinion/427222/united-states-v-noe-burgos/#1526" aria-description="Citation for case: United States v. Noe Burgos">720 F.2d at 1526</a></span>. In <em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span>, </em>the seizures occurred as part of an effort to find a suspected felon believed to be armed within a house into which he had run only minutes before police arrived. The officers gained entry to the home by permission of the suspect’s mother and began searching the various rooms for the suspect and any weapons that might pose a danger to them. Simultaneously with the time the suspect was discovered and apprehended in an upstairs room, officers in other rooms were uncovering and seizing evidence later used at trial. The Court held that the search of the entire house was “reasonably necessary to prevent the dangers that the suspect at large ... may resist or escape.” <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#299" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U.S. at 299</a></span>, <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#1646" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">87 S.Ct. at 1646</a></span>. <em><span class="citation" data-id="382343"><a href="/opinion/382343/united-states-v-neil-mathew-quigley-aka-charles-atchley-and-ted-roberts/" aria-description="Citation for case: United States v. Neil Mathew Quigley, A/K/A Charles...">Quigley</a></span> </em>presented a similar situation. Pursuing an escaped felon, the police discovered the suspect in a motel room with his girlfriend and immediately placed him in handcuffs. Within forty-five seconds after the arrest, one of the officers found a pistol beneath the bed sheets. The former Fifth Circuit held the search was justified as a “cursory safety cheek” because the suspect was reasonably believed to be armed when he entered the motel room, and the girl in the room with him, who was unrestrained at the time, was reasonably believed to be his accomplice and could have gained access to any concealed weapons. <span class="citation" data-id="382343"><a href="/opinion/382343/united-states-v-neil-mathew-quigley-aka-charles-atchley-and-ted-roberts/#419" aria-description="Citation for case: United States v. Neil Mathew Quigley, A/K/A Charles...">631 F.2d at 419</a></span>.</p>
<p id="b908-6"><em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span> </em>and <em><span class="citation" data-id="382343"><a href="/opinion/382343/united-states-v-neil-mathew-quigley-aka-charles-atchley-and-ted-roberts/" aria-description="Citation for case: United States v. Neil Mathew Quigley, A/K/A Charles...">Quigley</a></span> </em>are distinguishable on two significant points. In both cases the police made the searches and seizures simultaneously with, or within seconds after, the defendants’ arrest, whereas Satter-field and his girlfriend were taken into custody approximately ten minutes before the shotgun was found. More important, at the time of the searches in <em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span> </em>and <em><span class="citation" data-id="382343"><a href="/opinion/382343/united-states-v-neil-mathew-quigley-aka-charles-atchley-and-ted-roberts/" aria-description="Citation for case: United States v. Neil Mathew Quigley, A/K/A Charles...">Quigley</a></span>, </em>the police had reason to believe that dangerous weapons were accessible to the suspect or an accomplice who waspresent, or may have been present, in the building. In the instant case, Satterfield and Holcomb were restrained in patrol cars while the house was being searched; neither could possibly have posed a threat to the arresting officers. Moreover, the officers had already determined that no one else was present in the building. Under these circumstances, the search for the shotgun was not justified by exigency.</p>
<p id="b908-7"><em><span class="citation" data-id="427222"><a href="/opinion/427222/united-states-v-noe-burgos/" aria-description="Citation for case: United States v. Noe Burgos">Burgos</a></span> </em>is distinguishable on similar grounds. Government agents in that ease observed a man purchase two crates of firearms from two gun shops and transfer them to the trunk of Burgos’ automobile. Burgos drove to his residence with the surveillance team following him. Together with another man, he then took the crates, which contained 45 guns, out of his trunk and into his house. As Burgos was exiting his home, three or four agents stopped him on the front porch, entered the house and seized the firearms. In upholding the seizure as lawful, the court found two critical facts creating exigent circumstances: (1) the agents were faced with a house “laden with arms and an unknown number of people inside,” thus presenting an immediate threat to the security of the entire neighborhood, and (2) they had reason to believe the house contained dangerous third persons who might pose a threat to their safety. <span class="citation" data-id="427222"><a href="/opinion/427222/united-states-v-noe-burgos/#1526" aria-description="Citation for case: United States v. Noe Burgos">720 F.2d at 1526</a></span>. Neither of these circumstances is present here. The police had no reason to believe that Satterfield’s residence contained more than one firearm, and they knew that the only occupants of <page-number citation-index="1" label="845">*845</page-number>the house were already in police custody outside.</p>
<p id="b909-5">An arrest within a home does not provide a license for the police to search the entire residence for evidence. <em>See Chimel v. California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U.S. 752</a></span>, <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">89 S.Ct. 2034</a></span>, <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">23 L.Ed.2d 685</a></span> (1969); <em>United States v. Cueto, </em><span class="citation" data-id="372938"><a href="/opinion/372938/united-states-v-german-fidel-cueto/#1062" aria-description="Citation for case: United States v. German Fidel Cueto">611 F.2d 1056, 1062</a></span> (5th Cir.1980). The test is whether the officers reasonably could have perceived that delay would endanger their lives or the lives of others. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U.S. at 298-99</a></span>, <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#1645" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">87 S.Ct. at 1645-46</a></span>. Under the facts presented here, it is clear that no immediate threat existed. The only potential danger emanated from Satterfield’s unknown accomplices, who might have returned to the house to claim the shotgun without the knowledge of the police. Protection against this remote eventuality is not the type of circumstance that creates an urgent need for immediate action. If three officers were inadequate to transport the suspects to the station and also stand guard at Satterfield’s house until a warrant was obtained, the police could have summoned additional support. <em>See Segura v. United States, </em>— U.S.-, <span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/#3391" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380, 3391</a></span>, <span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">82 L.Ed.2d 599</a></span> (1984) (police may conduct perimeter stakeout of home to prevent persons from obtaining evidence while search warrant is being issued). An immediate search of the house after all of the occupants had been taken into custody and removed from the building was not reasonably necessary to ensure the safety of the police officers or the area residents. We therefore hold that the search for the shotgun was not justified under the exigent circumstances exception to the warrant requirement.</p>
<p id="b909-8">B. <em>The Inevitable Discovery Exception</em></p>
<p id="Adqi">Under the exclusionary rule, the illegally seized shotgun would not have been admissible in evidence against Satterfield unless an exception to the rule applied. <em>Wong Sun v. United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U.S. 471</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">9 L.Ed.2d 441</a></span> (1963). The Government asserts that the weapon was properly admitted under the “inevitable discovery” exception, recognized by this circuit in <em>United States v. Roper, </em><span class="citation" data-id="405982"><a href="/opinion/405982/united-states-v-james-morrow-roper-christian-matthew-newton-john-jackson/" aria-description="Citation for case: United States v. James Morrow Roper, Christian Matthew...">681 F.2d 1354</a></span> (11th Cir.1982), and recently adopted by the Supreme Court in <em>Nix v. Williams, </em>— U.S. -, <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">104 S.Ct. 2501</a></span>, <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">81 L.Ed.2d 377</a></span> (1984). The Government maintains that the shotgun would have been found in any event because the police obtained a valid warrant for the search of Satterfield’s residence several hours after the illegal search was made. The warrant issued for the search of “bloodstained sheets and clothing” and asserted probable cause based upon information supplied by Calla-way that she saw the bloodstained items in the home on the previous night. Because the police might reasonably have expected that bloodstained clothing could be hidden under the sofa cushions where the gun was found, the Government asserts that the police undoubtedly would have uncovered the weapon during their search with the warrant.</p>
<p id="b909-12">The Supreme Court briefly explained the inevitable discovery doctrine in <em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">Nix</a></span>:</em></p>
<blockquote id="b909-13">If the prosecution can establish by a preponderance of the evidence that the information ultimately or inevitably would have been discovered by lawful means ... then the deterrence rationale has so little basis that the evidence should be received.</blockquote>
<p id="b909-14"><em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">Id.</a></span> </em>at-, 104 S.Ct. at 2509. In <em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">Nix</a></span>, </em>the suspect was subjected to an illegal interrogation during which he directed the police to the location of the murder victim. At the time the confession was being elicited, a wide-spread search party had closed to within two and one-half miles of the site on which the body was found. Applying a preponderance of the evidence standard, the Court held that the uncovered remains were properly admitted into evidence because the record indicated that the search party was methodically progressing to the location of the body and inevitably would have found the evidence within three or four hours. The Court stated without much elaboration that if the information “ultimately or inevitably would have been discovered by lawful means” the exclusionary rule should not be applied. <em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">Id.</a></span></em></p>
<p id="b910-3"><page-number citation-index="1" label="846">*846</page-number>Except for the application of its rule to the specific facts before the Court and its holding that the Government must establish the inevitability of discovery by a preponderance of the evidence, the Supreme Court was silent as to what constitutes an “inevitable” discovery under the doctrine. Because the <em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">Nix</a></span> </em>decision is consistent with the previous case law of this circuit, we look to our earlier decisions for guidance in determining whether the facts of this case come within the exception.</p>
<p id="b910-4">The elements of the inevitable discovery rule in this circuit were set forth in a former Fifth Circuit case, <em>United States v. Brookins, </em><span class="citation" data-id="9466472"><a href="/opinion/374338/united-states-v-wayne-garfield-brookins-iii/" aria-description="Citation for case: United States v. Wayne Garfield Brookins, III">614 F.2d 1037</a></span> (5th Cir.1980). To qualify for admissibility, there must be a reasonable probability that the evidence in question would have been discovered by lawful means, and the prosecution must demonstrate that the lawful means which made discovery inevitable were possessed by the police and were being actively pursued <em>prior </em>to the occurrence of the illegal conduct. <em><span class="citation" data-id="9466472"><a href="/opinion/374338/united-states-v-wayne-garfield-brookins-iii/" aria-description="Citation for case: United States v. Wayne Garfield Brookins, III">Id.</a></span> </em>at 1042 n. 2, 1048. <em>See also Roper, </em><span class="citation" data-id="405982"><a href="/opinion/405982/united-states-v-james-morrow-roper-christian-matthew-newton-john-jackson/#1358" aria-description="Citation for case: United States v. James Morrow Roper, Christian Matthew...">681 F.2d at 1358</a></span>. Because the second element is not satisfied here, we hold that the shotgun was not admissible under the inevitable discovery exception.</p>
<p id="b910-5">In <em><span class="citation" data-id="9466472"><a href="/opinion/374338/united-states-v-wayne-garfield-brookins-iii/" aria-description="Citation for case: United States v. Wayne Garfield Brookins, III">Brookins</a></span>, </em>the police obtained the identity of a key prosecution witness through the illegal interrogation of the defendant. The court held the witness’ testimony admissible because lawful police inquiries that were already “set in motion” probably would have disclosed the witness' identity. <span class="citation" data-id="9466472"><a href="/opinion/374338/united-states-v-wayne-garfield-brookins-iii/#1048" aria-description="Citation for case: United States v. Wayne Garfield Brookins, III">614 F.2d at 1048</a></span>. In <em><span class="citation" data-id="405982"><a href="/opinion/405982/united-states-v-james-morrow-roper-christian-matthew-newton-john-jackson/" aria-description="Citation for case: United States v. James Morrow Roper, Christian Matthew...">Roper</a></span>, </em>police arrested the defendant in the hall outside his motel room and, seconds later, seized a gun from a briefcase on the dresser inside the room after learning its location from a brief interrogation in violation of his <em>Miranda </em>rights. The court held that the gun was admissible because the police had the right to search the room immediately<footnotemark>16</footnotemark> and were about to perform that lawful search when the illegal inquiry revealed the location of the gun. <span class="citation" data-id="405982"><a href="/opinion/405982/united-states-v-james-morrow-roper-christian-matthew-newton-john-jackson/#1358" aria-description="Citation for case: United States v. James Morrow Roper, Christian Matthew...">681 F.2d at 1358</a></span>.</p>
<p id="b910-11">Operation of the exclusionary rule when the police probably would have discovered the evidence through pursuit of a legal right they already possessed and were actively pursuing would place the Government in a worse position than before the illegal conduct occurred. The Supreme Court condemned this result as contrary to the public interest. <em>See Nix, </em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#2509" aria-description="Citation for case: Nix v. Williams">104 S.Ct. at 2509</a></span>. Here the Government had not yet initiated the lawful means that would have led to the discovery of the evidence. Unlike both <em><span class="citation" data-id="9466472"><a href="/opinion/374338/united-states-v-wayne-garfield-brookins-iii/" aria-description="Citation for case: United States v. Wayne Garfield Brookins, III">Brookins</a></span> </em>and <em><span class="citation" data-id="405982"><a href="/opinion/405982/united-states-v-james-morrow-roper-christian-matthew-newton-john-jackson/" aria-description="Citation for case: United States v. James Morrow Roper, Christian Matthew...">Roper</a></span>, </em>at the time the Government violated Satterfield’s fourth amendment right, it did not possess the legal means that would have led to the discovery of the shotgun. That means did not exist until several hours later when the warrant was obtained.</p>
<p id="b910-12">Under <em><span class="citation" data-id="9466472"><a href="/opinion/374338/united-states-v-wayne-garfield-brookins-iii/" aria-description="Citation for case: United States v. Wayne Garfield Brookins, III">Brookins</a></span> </em>and <em><span class="citation" data-id="405982"><a href="/opinion/405982/united-states-v-james-morrow-roper-christian-matthew-newton-john-jackson/" aria-description="Citation for case: United States v. James Morrow Roper, Christian Matthew...">Roper</a></span>, </em>if evidence is obtained by illegal conduct, the illegality can be cured only if the police possessed and were pursuing a lawful means of discovery at the time the illegality occurred. <em>See also United States v. Parker, </em><span class="citation" data-id="427662"><a href="/opinion/427662/united-states-v-joe-willie-parker/" aria-description="Citation for case: United States v. Joe Willie Parker">722 F.2d 179</a></span>, 185 n. 4 (5th Cir.1983); <em>United States v. Shaw, </em><span class="citation" data-id="415225"><a href="/opinion/415225/united-states-v-ronald-glen-shaw/" aria-description="Citation for case: United States v. Ronald Glen Shaw">701 F.2d 367</a></span>, 379 n. 6 (5th Cir. 1983), <em>cert. denied, </em>— U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./104/1419/">104 S.Ct. 1419</a></span>, <span class="citation no-link">79 L.Ed.2d 744</span> (1984). The Government cannot later initiate a lawful avenue of obtaining the evidence and then claim that it should be admitted because its discovery was inevitable. This is a sound rule, especially when applied to a case in which a search warrant was constitutionally required. Because a valid search warrant nearly always can be obtained after the search has occurred, a contrary holding would practically destroy the requirement that a warrant for the search of a home be obtained <em>before </em>the search takes place. Our constitutionally-mandated preference for substituting the judgment of a detached and neutral magistrate for that of a searching officer, <em>United States v. Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#568" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U.S. 543, 568</a></span>, <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#3087" aria-description="Citation for case: United States v. Martinez-Fuerte">96 S.Ct. <page-number citation-index="1" label="847">*847</page-number>3074, 3087</a></span>, <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">49 L.Ed.2d 1116</a></span> (1976), would be greatly undermined.</p>
<p id="b911-5">The Supreme - Court’s recent pronouncement in <em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">Nix</a></span> </em>does not affect this result. In adopting its general statement of the inevitable discovery rule, the Court was not presented with a situation in which the lawful means leading to an “inevitable” discovery had not yet been acquired by the police at the time the illegal evidence was seized. The search party there was well on its way to uncovering the body when the suspect revealed its precise location. Thus <em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">Nix</a></span> </em>is not inconsistent with the rule in this circuit that the police must possess and be actively pursuing the lawful avenue of discovery when the illegality occurred.</p>
<p id="b911-6">C. <em>Harmless Error</em></p>
<p id="b911-7">Having concluded that the shotgun was seized in violation of Satterfield’s fourth amendment rights and should have been excluded from the evidence presented at his trial, we must determine whether this error warrants reversal of his conviction of kidnapping under <span class="citation no-link">18 U.S.C. § 1201</span>(a)(1). The Supreme Court in <em>Chapman v. California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U.S. 18</a></span>, <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">87 S.Ct. 824</a></span>, <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">17 L.Ed.2d 705</a></span> (1967), held that a conviction need not be reversed if the constitutional error was harmless. The purpose of the harmless error rule is to avoid “setting aside convictions for small errors or defects that have little, if any, likelihood of having changed the result.” <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#22" aria-description="Citation for case: Chapman v. California"><em>Id. </em>at 22</a></span>, 87 S.Ct. at 827. This is precisely such a case.</p>
<p id="b911-8">The evidence supporting Satterfield’s conviction was overwhelming. The victim positively identified him as the man who forced her out of the bedroom of her trailer, as one of two men who killed her boyfriend immediately prior to the abduction, as the man who hit her over the head, as one of the men who held her at gunpoint during the ride to his residence, as the man who forced her to perform oral sex, and as the man who pushed her onto his bed. Satterfield’s girlfriend, Patricia Holcomb, verified that Callaway was present in Sat-terfield’s house just prior to the time Calla-way called the police from the neighboring residence. In addition, while Callaway was being kept in Satterfield’s house, Callaway heard Holcomb refer to him by his nickname “Pig.” Substantial physical evidence, including items of clothing and a pillow from his bed, all stained with blood matching the victim’s, was found in his shack within minutes after the victim’s escape; and shotgun shells matching the type found in his trousers pockets were discovered at the trailer where Callaway’s boyfriend was murdered. Compared to all of the other evidence against Satterfield, the shotgun, although further evidence of his complicity in the crime, was not an important item of proof in the Government’s case. From our review of the record, we are convinced that the evidence against Satterfield was so extensive that the erroneous admission of the shotgun was harmless beyond reasonable doubt.</p>
<p id="b911-10">V. UNEDITED INDICTMENT</p>
<p id="b911-11">Appellant Satterfield contends that the district court should have granted a mistrial because it read to the jury venire an unedited indictment despite the magistrate’s granting of Satterfield’s motion to strike references to his nickname “Pig.” Satterfield filed a pretrial motion to strike the alias language “also known as ‘Pig’ Satterfield,” which appeared three times in the indictment. The motion was made on grounds that the language was “surplus-age in that all witnesses will identify said defendant under the one name of Edward Eugene ‘Eddie’ Satterfield,” and that the alias was immaterial, irrelevant and prejudicial. Following an unrecorded hearing, the magistrate granted the motion.</p>
<p id="b911-12">After the prospective jurors were sworn, the court mistakenly read the original, unedited version of the indictment without deleting the three references to Satter-field’s nickname. Satterfield’s counsel did not object until the judge had finished reading the indictment, at which time he informed the court that the magistrate had deleted the references. He then moved for a mistrial, arguing that the venire would be <page-number citation-index="1" label="848">*848</page-number>prejudiced by the negative connotations associated with the name “Pig.”</p>
<p id="b912-4">Following a period of discussion with Satterfield’s counsel and the prosecutor, the court denied the motion for a mistrial and, without again mentioning “Pig,” instructed the jury that the alias had previously been ordered stricken from the indictment and that they should disregard it. At the same time, the judge asked the veniremen whether anyone felt he or she would be influenced in any degree by the reference to a nickname of one of the defendants. All responded in the negative. Before opening statements, the court read the edited indictment to the empaneled jury, making no mention of the alias or the previous incident.</p>
<p id="b912-5">The decision to grant a mistrial lies within the sound discretion of the trial judge since he is in the best position to evaluate the prejudicial effect of a statement or evidence on the jury. <em>United States v. Hill, </em><span class="citation" data-id="320661"><a href="/opinion/320661/united-states-v-james-norman-hill/#739" aria-description="Citation for case: United States v. James Norman Hill">500 F.2d 733, 739-40</a></span> (5th Cir.1974), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./420/952/">420 U.S. 952</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./95/1336/">95 S.Ct. 1336</a></span>, <span class="citation no-link">43 L.Ed.2d 430</span> (1975). We agree with the district court that the prejudice to Satterfield resulting from the mistaken reading of the unedited indictment was minimal. It is permissible to include an alias in an indictment if the Government plans to introduce evidence of the alias as an identifying characteristic of the defendant. <em>United States v. Haydel, </em><span class="citation" data-id="390869"><a href="/opinion/390869/united-states-v-john-m-haydel-jr-aka-ice-cream-and-mugsy/" aria-description="Citation for case: United States v. John M. Haydel, Jr., A/K/A &quot;Ice Cream&quot;...">649 F.2d 1152</a></span>, 1156 n. 6 (5th Cir.1981). In response to appellant’s motion for a mistrial, the prosecutor informed the court that he intended to present witnesses identifying Satterfield as “Pig,” and in his opening statement he conveyed a similar intention to the jury. Indeed, during the course of the trial, at least six witnesses, including two defense witnesses, either verified Satterfield’s nickname or stated that one of the kidnappers had been called “Pig” during the perpetration of the crime. Because the Government’s evidence established that Satterfield and one of the abductors were referred to as “Pig,” the nickname was material, and the magistrate need not have ordered its deletion in the first place. Although it was error to read the unedited version because the magistrate had deleted the words, the prejudice resulting therefrom was insignificant in light of the multiple references to Satterfield as “Pig” throughout the course of the trial.</p>
<p id="b912-7">The slight prejudice that may have resulted from reading the stricken words was adequately remedied by the district court’s cautionary instruction to the jury and reading of the corrected version before opening statements. When an indictment improperly includes a reference to an alias, an appropriate jury instruction can cure possible prejudice. <em>Doelle v. United States, </em><span class="citation" data-id="258579"><a href="/opinion/258579/jerome-e-doelle-v-united-states/" aria-description="Citation for case: Jerome E. Doelle v. United States">309 F.2d 396</a></span> (5th Cir.1962). Shortly after the error, the district court instructed the jury that it should disregard any reference to an alias made during the court’s reading of the indictment. During the cautionary instruction, the court was careful not to mention the name again and asked the veniremen whether they would be influenced in any way by their knowledge that one of the defendants had been known by a nickname. Under these circumstances, the district court did not abuse its discretion in refusing to grant a mistrial.</p>
<p id="b912-8">YI. ADMISSIBILITY OF REDACTED STATEMENT</p>
<p id="b912-9">Appellants challenge the admission of testimony by FBI Agent Land relating a statement made by Allison to Land while en route to the police station. Allison contends that the statement was taken in violation of his <em>Miranda </em>rights; Satterfield and Welden maintain that Allison’s statement inculpated them and denied them their right of confrontation, in violation of <em>Bruton v. United States, </em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">391 U.S. 123</a></span>, <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">88 S.Ct. 1620</a></span>, <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">20 L.Ed.2d 476</a></span> (1968). Neither claim has merit.</p>
<p id="b912-10">During a mid-trial hearing on the admissibility of the statement, Land stated that he advised Allison of his <em>Miranda </em>rights immediately after his arrest. At the same time, he gave Allison an Advice of Rights form, which Allison read. The form repeated the <em>Miranda </em>warnings and also included a waiver of rights provision, which <page-number citation-index="1" label="849">*849</page-number>Allison did not sign. According to Land, during the ride to the county police station, Land and Allison engaged in “small talk” or “casual conversation” about topics such as sports, a summer concert and DeKalb County. In the course of the conversation, Allison told Land “that he wanted to make it clear that he was really not a mean person, but that he simply had too many friends that got him into trouble and some of them were not good friends.” He also said that “Pig Satterfield and Carlton Wel-den were mean when they got high.” After Allison made this statement, Land immediately readvised him of his <em>Miranda </em>rights. Land told the court at the hearing that neither he nor another FBI agent who was also in the car discussed the case or questioned Allison about the events that led to his arrest.</p>
<p id="b913-5">At the end of the hearing, the court found that Allison had initiated the conversation and had volunteered the statement. To avoid any <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span> </em>problems, however, the court redacted the statement so that at trial Land testified only that “Mr. Allison advised me that he wanted to make it clear that he was not really a mean man, but that he simply had too many people that got him into trouble." At the conclusion of Land’s trial testimony, the court instructed the jury that any statements allegedly made by Allison were not to be considered in the Government's case against the other two defendants.</p>
<p id="b913-6">From a review of the evidence presented to the trial court at the hearing, we conclude that the court did not err in admitting the statement against Allison. Volunteered statements are not barred by the fifth amendment. <em>Miranda v. Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#478" aria-description="Citation for case: Miranda v. Arizona">384 U.S. 436, 478</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#1629" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602, 1629</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L.Ed.2d 694</a></span> (1966); <em>United States v. Castro, </em><span class="citation" data-id="9471583"><a href="/opinion/429258/united-states-v-oscar-castro-charles-david-fraga-peter-diaz-and-thomas/#1530" aria-description="Citation for case: United States v. Oscar Castro, Charles David Fraga, Peter...">723 F.2d 1527, 1530</a></span> (11th Cir.1984). FBI Agent Land’s testimony indicates that Allison’s statement was volunteered. Incriminating statements made in the course of casual conversation are not products of a custodial interrogation. <em>See United States v. Menichino, </em><span class="citation" data-id="319744"><a href="/opinion/319744/united-states-v-andrew-carmen-menichino/" aria-description="Citation for case: United States v. Andrew Carmen Menichino">497 F.2d 935</a></span> (5th Cir.1974).</p>
<p id="b913-8">As to appellants Satterfield and Welden, a defendant’s right to confront his accuser is infringed by the admissibility of a statement against his codefendant only if the out-of-court statement directly implicates him. <em>United States v. Stewart, </em><span class="citation" data-id="357930"><a href="/opinion/357930/united-states-v-ronnie-lee-stewart-and-dan-edward-scott/#359" aria-description="Citation for case: United States v. Ronnie Lee Stewart and Dan Edward Scott">579 F.2d 356, 359</a></span> (5th Cir.1978), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./439/936/">439 U.S. 936</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./99/332/">99 S.Ct. 332</a></span>, <span class="citation" data-id="9013220"><a href="/opinion/9020020/barbarin-v-all-u-s-judges-of-eastern-district-of-louisiana/" aria-description="Citation for case: Barbarin v. All U. S. Judges of Eastern District of...">58 L.Ed.2d 332</a></span> (1979). For <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span> </em>to apply, a codefendant’s statement must be clearly inculpatory standing alone. <em>United States v. Slocum, </em><span class="citation" data-id="411862"><a href="/opinion/411862/united-states-v-robert-w-slocum/#655" aria-description="Citation for case: United States v. Robert W. Slocum">695 F.2d 650, 655</a></span> (2d Cir.1982), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./460/1015/">460 U.S. 1015</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./103/1260/">103 S.Ct. 1260</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/75/487/">75 L.Ed.2d 487</a></span> (1983). Allison’s statement that he “had too many people that got him into trouble” did not specifically name Satterfield or Welden, or describe them in such a way that a jury would identify them as among the “people” Allison was referring to. The out-of-court statement falls far short of directly implicating either Satterfield or Welden in the crime. The trial court redacted any references that might have implicated the other defendants, going so far as changing the word “friends” to the more general “people.” As an added precaution, the court’s cautionary instruction made clear that the statement was admissible only against defendant Allison. Under these circumstances, the <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span> </em>claims of Satterfield and Welden must fail.</p>
<p id="b913-9">VII. APPLICABILITY OF THE KIDNAP STATUTE</p>
<p id="b913-10"><span class="citation no-link">18 U.S.C. § 1201</span> requires that a kidnapping be “for ransom or reward or otherwise.” Appellant Welden claims that the statute does not apply to the Government’s case against him. In <em>Gooch v. United States, </em><span class="citation" data-id="102588"><a href="/opinion/102588/gooch-v-united-states/" aria-description="Citation for case: Gooch v. United States">297 U.S. 124</a></span>, <span class="citation" data-id="102588"><a href="/opinion/102588/gooch-v-united-states/" aria-description="Citation for case: Gooch v. United States">56 S.Ct. 395</a></span>, <span class="citation" data-id="102588"><a href="/opinion/102588/gooch-v-united-states/" aria-description="Citation for case: Gooch v. United States">80 L.Ed. 522</a></span> (1936), the Supreme Court held that Congress enacted the kidnapping statute to prevent the transportation in interstate commerce of persons who were unlawfully restrained for the purpose of the captor’s securing “some benefit” to himself. <span class="citation" data-id="102588"><a href="/opinion/102588/gooch-v-united-states/#128" aria-description="Citation for case: Gooch v. United States"><em>Id. </em>at 128</a></span>, <span class="citation" data-id="102588"><a href="/opinion/102588/gooch-v-united-states/#397" aria-description="Citation for case: Gooch v. United States">56 S.Ct. at 397</a></span>. The court examined the legislative history of the statute and noted that two years after its initial enactment Congress added the words “or otherwise” for the express pur<page-number citation-index="1" label="850">*850</page-number>pose of extending the Act to “persons who have been kidnapped and held, not only for reward, but for any other reason----” <em><span class="citation" data-id="102588"><a href="/opinion/102588/gooch-v-united-states/" aria-description="Citation for case: Gooch v. United States">Id.</a></span> </em>(quoting H.Rep. No. 1457, 73rd Cong.2d Sess.).</p>
<p id="b914-6">The statute broadly prohibits the interstate transportation of a person against his will if the captor hopes to obtain any benefit to himself from the abduction. The evidence supports the district court’s conclusion that Welden participated in the kidnapping to attain some benefit to himself. Callaway had just witnessed the murder of her boyfriend and therefore was a potential witness against the killers. Taking a person away from her home for the purpose of silencing her as a potential witness comes within the “or otherwise” proviso of the kidnapping statute. Hence Welden’s claim must fail.</p>
<p id="b914-7">VIII. SUFFICIENCY OF THE EVIDENCE AGAINST WELDEN AND ALLISON</p>
<p id="b914-8">Appellants Welden and Allison challenge the sufficiency of the evidence to convict them under <span class="citation no-link">18 U.S.C. § 1201</span>(a)(1). To obtain a conviction under the federal kidnapping statute, the Government must prove (1) knowing and willful kidnapping, (2) an intent to gain a benefit from the seizure, and (3) transportation of the victim in interstate or foreign commerce. <em>Hattaway v. United States, </em><span class="citation" data-id="281335"><a href="/opinion/281335/james-c-hattaway-v-united-states/#433" aria-description="Citation for case: James C. Hattaway v. United States">399 F.2d 431, 433</a></span> (5th Cir.1968). Appellants do not contest the sufficiency of the Government’s evidence proving that a group of men entered the trailer occupied by Pauline Callaway and transported her over the Georgia/Alabama border against her will. Their contention at trial and on appeal is that the evidence was not sufficient to identify them as two of those men.</p>
<p id="b914-9">Our review of the evidence is limited to determining whether a reasonable trier of fact could find that the evidence establishes guilt beyond a reasonable doubt. <em>United States v. Bell, </em><span class="citation" data-id="9469199"><a href="/opinion/403793/united-states-v-nelson-bell/" aria-description="Citation for case: United States v. Nelson Bell">678 F.2d 547</a></span> (5th Cir. Unit B 1982) (en banc), <em>aff'd on other grounds, </em><span class="citation" data-id="9429238"><a href="/opinion/110964/bell-v-united-states/" aria-description="Citation for case: Bell v. United States">462 U.S. 356</a></span>, <span class="citation" data-id="9429238"><a href="/opinion/110964/bell-v-united-states/" aria-description="Citation for case: Bell v. United States">103 S.Ct. 2398</a></span>, <span class="citation" data-id="9429238"><a href="/opinion/110964/bell-v-united-states/" aria-description="Citation for case: Bell v. United States">76 L.Ed.2d 638</a></span> (1983). In our respect for the jury’s verdict, we must view the evidence in the light most favorable to the Government, and we must allow the jury to choose among reasonable constructions of the evidence. <em>Glasser v. United States, </em><span class="citation" data-id="103597"><a href="/opinion/103597/glasser-v-united-states/#80" aria-description="Citation for case: Glasser v. United States">315 U.S. 60, 80</a></span>, <span class="citation" data-id="103597"><a href="/opinion/103597/glasser-v-united-states/#469" aria-description="Citation for case: Glasser v. United States">62 S.Ct. 457, 469</a></span>, <span class="citation" data-id="103597"><a href="/opinion/103597/glasser-v-united-states/" aria-description="Citation for case: Glasser v. United States">86 L.Ed. 680</a></span> (1942); <em>Bell, </em><span class="citation" data-id="9469199"><a href="/opinion/403793/united-states-v-nelson-bell/#549" aria-description="Citation for case: United States v. Nelson Bell">678 F.2d at 549</a></span>. Applying these standards, we conclude that the evidence was sufficient to allow a reasonable jury to find that Welden and Allison participated in the abduction of Pauline Callaway.</p>
<p id="b914-11">A. Welden</p>
<p id="b914-12">Pauline Callaway testified that two men wearing masks broke into her trailer in Hooker, Georgia, at around 3:00 a.m. on April 7, shot and killed her boyfriend, and forced her out of her home and into a red and maroon Chevrolet Malibu, which police later found with bloodstains matching Call-away’s in the interior. En route to their destination in Alabama, she observed three men inside the car; the two who had removed her from the trailer held her at gunpoint while the third drove. During the ride she heard the two gunmen speak to each other, one calling the other “Carlton,” Welden’s first name. She also noticed the length of her abductors’ hair and heard the one named Carlton speak to the others. Having seen and heard appellant Welden on previous occasions speaking with her boyfriend at a local bar, she recognized the voice and hair as Welden’s. Based upon her recognition of the hair, name and voice, she positively identified Welden at trial. Dervin Little testified that he loaned the vehicle eventually used in the incident, the Chevrolet Malibu, to Welden at 10:00 p.m. on April 6, approximately five hours before the kidnapping. Patricia Holcomb testified that Welden stopped by her house in the same car at around 5:00 a.m., only two hours after the crime. She also testified that about an hour later, he returned to drive her over to appellant Satterfield’s house where Callaway was being held. During the ride, Welden told Holcomb, “We might be in a little trouble.” Based upon this direct and circumstantial evidence, a jury could very well have conclud<page-number citation-index="1" label="851">*851</page-number>ed beyond a reasonable doubt that Welden was guilty of kidnapping Pauline Callaway.</p>
<p id="b915-5">B. Allison</p>
<p id="b915-6">The Government’s theory of the case placed Allison as the driver of the getaway vehicle. Dervin Little testified that he and Allison were parked in the Malibu at a graveyard on the night of the incident. When Welden switched cars with him in the graveyard at 10:00 p.m., Allison left with Welden in the Malibu. Defense witness Wayne McCarson testified that he saw Allison sitting in the Malibu in Welden’s driveway at 11:00 p.m. that same evening. The ear was discovered the following morning parked at the State Line Garage, an auto repair shop operated by Allison.</p>
<p id="b915-7">Patricia Holcomb testified that when Welden visited her at about 5:00 a.m. on April 7, she saw a man sitting in the driver’s seat of Little’s car. Although at trial she could not positively identify the man as Allison, she did testify that she told FBI Agent Land the man was Allison when he interviewed her on the afternoon of April 7. After he was arrested on April 11, Allison told the FBI agent that “he wanted to make it clear that he was not really a mean man, but he simply had too many people that got him into trouble.”</p>
<p id="b915-8">In addition to this circumstantial evidence, the Government’s case was strengthened by the weakness of Allison’s alibi. Three witnesses testified that they were with Allison at Wayne McCarson’s house drinking beer on the night of the kidnapping from 12:30 a.m. until 5:00 a.m. One of the witnesses, McCarson, gave inconsistent versions of where he picked up Allison to bring him to his house for the party. He first testified that he met Allison at Welden’s house and later indicated that they met at a liquor store. The other two witnesses related events that the jury may have considered implausible. Witnesses Baker and Posey testified that Posey picked up Baker and one other person at their homes at around midnight for the purpose of driving around the area drinking beer. When they drove by MeCarson’s house at 12:30 a.m. and saw the lights on, they decided to drop in, joining Allison and McCarson until the early morning hours.</p>
<p id="b915-10">There was no direct evidence incriminating Allison in the crime. Unlike Welden, Allison was not positively identified by Callaway as one of her abductors. She did testify, however, that the driver of the car had blondish-brown curly hair, a description that is not inconsistent with Allison’s appearance. Although each piece of circumstantial evidence, standing alone, would not have been enough to convict Allison, the totality of the evidence against him was sufficient to persuade a jury that he was guilty beyond a reasonable doubt. The jury reasonably could have disbelieved the testimony of his alibi witnesses, and the circumstantial evidence was sufficient to raise a reasonable inference that Allison was involved in the crime.</p>
<p id="b915-11">IX. OTHER CLAIMS</p>
<p id="b915-12">Appellants raise additional claims, including the admissibility of Callaway’s in-court and out-of-court identifications, the district court’s ruling on numerous objections made by counsel for appellants and the prosecutor, the court’s refusal to give certain jury instructions and its decision to sequester the jury. After reviewing the claims and the record, we find them all to be without merit.</p>
<p id="b915-13">Case number 83-7444 is AFFIRMED in part, REVERSED in part, and REMANDED. The Government’s petition for writ of mandamus, case number 83-7583, is DENIED.</p>
<footnote label="1">
<p id="b895-14">. Mandamus is appropriate only in "extraordinary cases” to remedy a "clear usurpation of power or abuse of discretion,” <em>In re Extradition of Ghandtchi, </em><span class="citation" data-id="413209"><a href="/opinion/413209/in-re-extradition-of-houchang-ghandtchi-united-states-of-america-v/#1038" aria-description="Citation for case: In Re Extradition of Houchang Ghandtchi. United States of...">697 F.2d 1037, 1038</a></span> (11th Cir.1983), and is available only when there is no other adequate means to obtain relief, <em>In re Oswalt, </em><span class="citation" data-id="370528"><a href="/opinion/370528/in-re-william-h-oswalt-dba-william-maxwell-construction-company/#648" aria-description="Citation for case: In Re William H. Oswalt, D/B/A William Maxwell...">607 F.2d 645, 648</a></span> (5th Cir.1979). Because we grant the Government’s cross-appeal and remand to the district court to comply with the restitution provisions of the VWPA, <em>infra, </em>resort to the mandamus procedure is unnecessary.</p>
</footnote>
<footnote label="2">
<p id="b898-5">. No House report was submitted with the legislation.</p>
</footnote>
<footnote label="3">
<p id="b898-6">. Fed.R.Crim.P. 32(c)(2) as amended, provides:</p>
<blockquote id="aaq-dedup-0">The presentence report shall contain—</blockquote>
<blockquote id="b898-7">(A) any prior criminal record of the defendant;</blockquote>
<blockquote id="b898-8">(B) a statement of the circumstances of the commission of the offense and circumstances affecting the defendant’s behavior;</blockquote>
<blockquote id="b898-9">(C) information concerning any harm, including financial, social, psychological, and physical harm, done to or loss suffered by any victim of the offense; and</blockquote>
<blockquote id="b898-10">(D) any other information that may aid the court in sentencing, including the restitution needs of any victim of the offense.</blockquote>
</footnote>
<footnote label="4">
<p id="b898-11">. <span class="citation no-link">18 U.S.C. § 3579</span> provides:</p>
<blockquote id="b898-12">(a)(1) The court, when sentencing a defendant convicted of an offense under this title or under subsection (h), (i), (j), or (n) of section 902 of the Federal Aviation Act of 1958 (49 U.S.C. 1472), may order, in addition to or in lieu of any other penalty authorized by law, that the defendant make restitution to any victim of the offense.</blockquote>
<blockquote id="b898-13">(2) If the court does not order restitution, or orders only partial restitution, under this section, the court shall state on the record the reasons therefor.</blockquote>
<blockquote id="b898-17">(b) The order may require that such defendant—</blockquote>
<p id="b898-18">(1) in the case of an offense resulting in damage to or loss or destruction of property of a victim of the offense—</p>
<blockquote id="b898-19">(A) return the property to the owner of the property or someone designated by the owner; or</blockquote>
<blockquote id="b898-20">(B) if return of the property under subpara-graph (A) is impossible, impractical, or inadequate, pay an amount equal to the greater of—</blockquote>
<blockquote id="b898-21">(1) the value of the property on the date of the damage, loss, or destruction, or</blockquote>
<blockquote id="b898-22">(ii) the value of the property on the date of sentencing, less the value (as of the date the property is returned) of any part of the property that is returned;</blockquote>
<p id="b898-23">(2) in the case of an offense resulting in bodily injury to a victim—</p>
<blockquote id="b898-24">(A) pay an amount equal to the cost of necessary medical and related professional services and devices relating to physical, psychiatric, and psychological care, including nonmedical care and treatment rendered in accordance with a method of healing recognized by the law of the place of treatment;</blockquote>
<blockquote id="b898-25">(B) pay an amount equal to the cost of necessary physical and occupational therapy and rehabilitation; and</blockquote>
<blockquote id="b899-5"><page-number citation-index="1" label="835">*835</page-number>(C) reimburse the victim for income lost by such victim as a result of such offense;</blockquote>
<p id="b899-6">(3) in the case of an offense resulting in bodily injury also results in the death of a victim, pay an amount equal to the cost of necessary funeral and related services; and</p>
<p id="b899-7">(4) in any case, if the victim (or if the victim is deceased, the victim’s estate) consents, make restitution in services in lieu of money, or make restitution to a person or organization designated by the victim or the estate.</p>
<blockquote id="b899-8">(c) If the Court decides to order restitution under this section, the court shall, if the victim is deceased, order that the restitution be made to the victim’s estate.</blockquote>
<blockquote id="b899-9">(d) The court shall impose an order of restitution to the extent that such order is as fair as possible to the victim and the imposition of such order will not unduly complicate or prolong the sentencing process.</blockquote>
<blockquote id="b899-10">(e) (1) The court shall not impose restitution with respect to a loss for which the victim has received or is to receive compensation, except that the court may, in the interest of justice, order restitution to any person who has compensated the victim for such loss to the extent that such person paid the compensation. An order of restitution shall require that all restitution to victims under such order be made before any restitution to any other person under such order is made.</blockquote>
<blockquote id="b899-11">(2) Any amount paid to a victim under an order of restitution shall be set off against any amount later recovered as compensatory damages by such victim in—</blockquote>
<blockquote id="b899-12">(A) any Federal civil proceeding; and</blockquote>
<blockquote id="b899-13">(B) any State civil proceeding, to the extent provided by the law of that State.</blockquote>
<blockquote id="b899-14">(f) (1) The court may require that such defendant make restitution under this section within a specified period or in specified installments.</blockquote>
<blockquote id="b899-15">(2) The end of such period or the last such installment shall not be later than—</blockquote>
<blockquote id="b899-16">(A) the end of the period of probation, if probation is ordered;</blockquote>
<blockquote id="b899-17">(B) five years after the end of the term of imprisonment imposed, if the court does not order probation; and</blockquote>
<blockquote id="b899-18">(C) five years after the date of sentencing in any other case.</blockquote>
<blockquote id="b899-19">(3) If not otherwise provided by the court under this subsection, restitution shall be made immediately.</blockquote>
<blockquote id="b899-20">(g) If such defendant is placed on probation or paroled under this title, any restitution ordered under this section shall be a condition of such probation or parole. The court may revoke probation and the Parole Commission may revoke parole if the defendant fails to comply with such order. In determining whether to revoke probation or parole, the court or Parole Commission shall consider the defendant’s employment status, earning ability, financial resources, the willfulness of the defendant’s failure to pay, and any other special circumstances that may have a bearing on the defendant’s ability to pay.</blockquote>
<blockquote id="b899-22">(h) An order of restitution may be enforced by United States or a victim named in the order to receive the restitution in the same manner as a judgment in a civil action.</blockquote>
<p id="b899-23"><span class="citation no-link">18 U.S.C. § 3580</span> provides:</p>
<blockquote id="b899-24">(a) The court, in determining whether to order restitution under section 3579 of this title and the amount of such restitution, shall consider the amount of the loss sustained by any victim as a result of the offense, the financial resources of the defendant, the financial needs and earning ability of the defendant and the defendant's dependents, and such other factors as the court deems appropriate.</blockquote>
<blockquote id="b899-25">(b) The court may order the probation service of the court to obtain information pertaining to the factors set forth in subsection (a) of this section. The probation service of the court shall include the information collected in the report of presentence investigation or in a separate report, as the court directs.</blockquote>
<blockquote id="b899-26">(c) The court shall disclose to both the defendant and the attorney for the Government all portions of the presentence or other report pertaining to the matters described in subsection (a) of this section.</blockquote>
<blockquote id="b899-27">(d) Any dispute as to the proper amount or type of restitution shall be resolved by the court by the preponderance of the evidence. The burden of demonstrating the amount of the loss sustained by a victim as a result of the offense shall be on the attorney for the Government. The burden of demonstrating the financial resources of the defendant and the financial needs of the defendant and such defendant’s dependents shall be on the defendant. The burden of demonstrating such other matters as the court deems appropriate shall be upon the party designated by the court as justice requires.</blockquote>
<blockquote id="b899-28">(e) A conviction of a defendant for an offense involving the act giving rise to restitution under this section shall estop the defendant from denying the essential allegations of that offense in any subsequent Federal civil proceeding or State civil proceeding, to the extent consistent with State law, brought by the victim.</blockquote>
</footnote>
<footnote label="5">
<p id="b900-8">. A district court in Pennsylvania recently has upheld the Act under a seventh amendment challenge. <em>See United States v. Brown, </em><span class="citation" data-id="1753058"><a href="/opinion/1753058/united-states-v-brown/" aria-description="Citation for case: United States v. Brown">587 F.Supp. 1005</a></span> (E.D.Pa.1984). In addition, the Second Circuit has reached the same conclusion in an opinion published subsequent to the filing of this opinion. <em>See United States v. Brown, </em><span class="citation" data-id="442090"><a href="/opinion/442090/united-states-v-wilbert-brown-jr/" aria-description="Citation for case: United States v. Wilbert Brown, Jr.">744 F.2d 905</a></span> (2d Cir. 1984).</p>
</footnote>
<footnote label="6">
<p id="b901-7">. <em>See </em>Harland, <em>Monetary Remedies for the Victims of Crime: Assessing the Role of the Criminal Courts, </em>30 U.C.L.A. L.Rev. 52, 92-93 (1982).</p>
</footnote>
<footnote label="7">
<p id="b901-8">. The types of losses recoverable under the VWPA also distinguish its restitution provisions from civil judgments. Whereas under the Act, speculative damages such as pain and suffering, <em>see </em>Implementation of the Restitution Provisions of the Victim and Witness Protection Act of 1982 at 9 (Aug. 29, 1983) (memorandum from D. Lowell Jensen, Associate Attorney General), and "loss of use” due to property damage, <span class="citation no-link">18 U.S.C. § 3579</span>(b)(1), may not be recovered, such damages are frequently sought in civil actions. <em>See generally </em>Project, Congress Opens a Pandora’s Box — The Restitution Provisions of the Victim and Witness Protection Act of 1982, 52 Fordham L.Rev. 507, 542 (1984).</p>
</footnote>
<footnote label="8">
<p id="b901-18"><em>. See also </em>128 Cong.Rec. SI 1436 (daily ed. Sept. 14, 1982) (remarks of Sen. Mathias) ("[the Act permits], for the first time, a Federal judge to order res

[...TRUNCATED 6451 of 126451 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/United States v. Sharpe.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Sharpe"
type: case
citation: "470 U.S. 675 (1985)"
parallel_cite: "105 S. Ct. 1568; 84 L. Ed. 2d 605; 53 U.S.L.W. 4346"
neutral_cite: 1985 U.S. LEXIS 74
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-03-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-03-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Sharpe
  varies_by_point: false
  scope_note: "Good law; the diligence test for the permissible duration of a Terry stop (no rigid time limit) remains controlling and underlies Rodriguez v. United States."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111378/united-states-v-sharpe/"
  cluster_id: 111378
  opinion_id: 9429956
  identity_checked: true
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Progeny (duration)"
related: ["[[Terry v. Ohio]]", "[[United States v. Place]]", "[[Florida v. Royer]]", "[[United States v. Hensley]]", "[[Rodriguez v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure", "terry-stop", "duration", "investigative-detention"]
holding: "There is no rigid time limit for a Terry stop; a 20-minute investigative detention was reasonable where police diligently pursued an investigation likely to confirm or dispel suspicion quickly."
lake:
  record_id: United States v. Sharpe
  status: verified
  projected_at: 2026-07-09
---

# United States v. Sharpe

*470 U.S. 675 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A DEA agent and a state patrolman, suspecting drug trafficking, tried to stop a Pontiac and an overloaded pickup traveling in tandem. The pickup's driver, Savage, evaded the patrolman and was stopped about half a mile ahead. The agent stayed with Sharpe (the Pontiac) and then drove to Savage's truck; Savage was detained roughly 20 minutes while the agent coordinated with the patrolman, after which the agent smelled marijuana and discovered bales in the truck. The Court of Appeals held the 20-minute detention too long to be a *[[Terry v. Ohio|Terry]]* stop.

## Issue
Whether a roughly 20-minute investigative detention exceeded the permissible bounds of a *[[Terry v. Ohio|Terry]]* stop and became a [[Common Legal Terms#de-facto|de facto]] arrest requiring probable cause.

## Rule
There is no fixed durational ceiling on a *[[Terry v. Ohio|Terry]]* stop: "But our cases impose no rigid time limitation on *Terry* stops." — 470 U.S. at 685. ^pin-685

The test is diligence, not the clock: "In assessing whether a detention is too long in duration to be justified as an investigative stop, we consider it appropriate to examine whether the police diligently pursued a means of investigation that was likely to confirm or dispel their suspicions quickly, during which time it was necessary to detain the defendant." — [*Id.* at 686](https://www.courtlistener.com/opinion/111378/united-states-v-sharpe/#:~:text=In%20assessing%20whether%20a%20detention). ^pin-686

## Application
The agent pursued his investigation diligently: during most of Savage's 20-minute detention he was attempting to reach the patrolman, and once they joined he proceeded expeditiously — checking documents, requesting consent, confirming the truck was overloaded, and detecting marijuana. Critically, much of the delay was attributable to Savage's own evasive driving, not to any dilatoriness by police. Because the officers acted reasonably and did not unnecessarily prolong the stop, the 20-minute detention was a valid investigative stop, not a [[Common Legal Terms#de-facto|de facto]] arrest; a *[[Common Legal Terms#per-se|per se]]* 20-minute rule would be at odds with the Court's flexible approach.

## Conclusion
The 20-minute detention was reasonable; the Court of Appeals erred in adopting an effective *[[Common Legal Terms#per-se|per se]]* time limit. *Sharpe* governs the duration of *[[Terry v. Ohio|Terry]]* stops through a diligence-and-necessity inquiry rather than a bright-line clock.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Develops the duration analysis of [[United States v. Place]] and distinguishes the de-facto-arrest findings of [[Florida v. Royer]]; the diligence principle underlies [[Rodriguez v. United States]] (a stop may not be prolonged beyond its traffic mission absent reasonable suspicion). See also [[United States v. Hensley]].

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Progeny (duration)*

## Sources
- *United States v. Sharpe*, 470 U.S. 675 (1985) — https://www.courtlistener.com/opinion/111378/united-states-v-sharpe/ — pinpoints: 685, 686.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3035ba654ab62ced", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "470 U.S. 675 (1985)", "court": "U.S. Supreme Court", "neutral_cite": "1985 U.S. LEXIS 74", "official_citation_present": true, "parallel_cite": "105 S. Ct. 1568; 84 L. Ed. 2d 605; 53 U.S.L.W. 4346", "title": "United States v. Sharpe", "year": "1985"}}
{"assertion_id": "cd72578ba9596f34", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "There is no rigid time limit for a Terry stop; a 20-minute investigative detention was reasonable where police diligently pursued an investigation likely to confirm or dispel suspicion quickly.", "title": "United States v. Sharpe"}}
{"assertion_id": "ec284990ec371c21", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Progeny (duration)", "title": "United States v. Sharpe"}}
{"assertion_id": "3a031fde67970a58", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1985-03-20", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Sharpe", "field_i_validity": "good_law", "scope_note": "Good law; the diligence test for the permissible duration of a Terry stop (no rigid time limit) remains controlling and underlies Rodriguez v. United States.", "title": "United States v. Sharpe", "varies_by_point": "false"}}
{"assertion_id": "dfa3913adf131a0f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Sharpe"}}
```

### lake record — United States v. Sharpe

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Sharpe",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Sharpe",
    "case_name_short": "Sharpe",
    "case_name_full": "UNITED STATES v. SHARPE Et Al.",
    "input_case_name": "United States v. Sharpe",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-03-20",
    "year": 1985,
    "docket": null,
    "cluster_id": 111378,
    "lead_opinion_id": 9429956,
    "sibling_ids": [
      111378,
      9429956,
      9429957,
      9429958,
      9429959,
      9429960
    ],
    "absolute_url": "/opinion/111378/united-states-v-sharpe/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "470 U.S. 675",
      "volume": "470",
      "reporter": "U.S.",
      "page": "675",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 1568",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1568",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 2d 605",
        "volume": "84",
        "reporter": "L. Ed. 2d",
        "page": "605",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4346",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4346",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 74",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "74",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "470 U.S. 675",
        "volume": "470",
        "reporter": "U.S.",
        "page": "675",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 1568",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1568",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 2d 605",
        "volume": "84",
        "reporter": "L. Ed. 2d",
        "page": "605",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 74",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "74",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4346",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4346",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "470 U.S. 675",
    "official_selection": {
      "court_class": "scotus",
      "selected": "470 U.S. 675",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-685",
      "page": null,
      "quote": "--- # United States v. Sharpe *470 U.S. 675 (1985)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A DEA agent and a state patrolman, suspecting drug trafficking, tried to stop a Pontiac and an overloaded pickup traveling in tandem. The pickup's driver, Savage, evaded the patrolman and was stopped about half a mile ahead. The agent stayed with Sharpe (the Pontiac) and then drove to Savage's truck; Savage was detained roughly 20 minutes while the agent coordinated with the patrolman, after which the agent smelled marijuana and discovered bales in the truck. The Court of Appeals held the 20-minute detention too long to be a *Terry* stop. ## Issue Whether a roughly 20-minute investigative detention exceeded the permissible bounds of a *Terry* stop and became a de facto arrest requiring probable cause. ## Rule There is no fixed durational ceiling on a *Terry* stop:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-686",
      "page": null,
      "quote": "In assessing whether a detention is too long in duration to be justified as an investigative stop, we consider it appropriate to examine whether the police diligently pursued a means of investigation that was likely to confirm or dispel their suspicions quickly, during which time it was necessary to detain the defendant.",
      "star_marker": "686",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 28085,
      "fragment": "#:~:text=In%20assessing%20whether%20a%20detention",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-03-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Sharpe",
    "varies_by_point": false,
    "scope_note": "Good law; the diligence test for the permissible duration of a Terry stop (no rigid time limit) remains controlling and underlies Rodriguez v. United States.",
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
        "journal_ref": "United States v. Sharpe:lane1_negative"
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
        "journal_ref": "United States v. Sharpe:lane1_negative"
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
        "journal_ref": "United States v. Sharpe:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Soriano-Lara",
          "cluster_id": 4881582,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Reed",
          "cluster_id": 10018647,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Reed",
          "cluster_id": 4731165,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Sokolow",
          "cluster_id": 112239,
          "cite": [
            "104 L. Ed. 2d 1",
            "109 S. Ct. 1581",
            "490 U.S. 1",
            "1989 U.S. LEXIS 1694",
            "57 U.S.L.W. 4401"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Carney",
          "cluster_id": 111423,
          "cite": [
            "85 L. Ed. 2d 406",
            "105 S. Ct. 2066",
            "471 U.S. 386",
            "1985 U.S. LEXIS 8",
            "53 U.S.L.W. 4521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. State",
          "cluster_id": 2419717,
          "cite": [
            "947 S.W.2d 240",
            "1997 Tex. Crim. App. LEXIS 43",
            "1997 WL 292676"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kothe v. State",
          "cluster_id": 1504839,
          "cite": [
            "152 S.W.3d 54",
            "2004 Tex. Crim. App. LEXIS 1749",
            "2004 WL 2347781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Balentine v. State",
          "cluster_id": 1662103,
          "cite": [
            "71 S.W.3d 763",
            "2002 WL 496960"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Amores v. State",
          "cluster_id": 1670855,
          "cite": [
            "816 S.W.2d 407",
            "1991 Tex. Crim. App. LEXIS 183",
            "1991 WL 183121"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Foote v. Spiegel",
          "cluster_id": 155036,
          "cite": [
            "118 F.3d 1416",
            "1997 U.S. App. LEXIS 16800",
            "1997 WL 374158"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hicks",
          "cluster_id": 5688381,
          "cite": [
            "68 N.Y.2d 234",
            "508 N.Y.S.2d 163",
            "500 N.E.2d 861",
            "1986 N.Y. LEXIS 21211"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mateen Yusuf Shabazz, A/K/A Edward L. Eberhart, A/K/A Edward Wallace, and Keith Lamar Parker",
          "cluster_id": 606689,
          "cite": [
            "993 F.2d 431",
            "1993 U.S. App. LEXIS 13132",
            "1993 WL 187994"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rhodes v. State",
          "cluster_id": 2427083,
          "cite": [
            "945 S.W.2d 115",
            "1997 Tex. Crim. App. LEXIS 26",
            "1997 WL 209529"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Degen v. United States",
          "cluster_id": 2621067,
          "cite": [
            "135 L. Ed. 2d 102",
            "116 S. Ct. 1777",
            "517 U.S. 820",
            "1996 U.S. LEXIS 3719"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory B. Bloomfield, Also Known as Earl Marcum Johnson",
          "cluster_id": 682770,
          "cite": [
            "40 F.3d 910",
            "1994 U.S. App. LEXIS 32273",
            "1994 WL 643872"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ortega-Rodriguez v. United States",
          "cluster_id": 112829,
          "cite": [
            "122 L. Ed. 2d 581",
            "113 S. Ct. 1199",
            "507 U.S. 234",
            "1993 U.S. LEXIS 1949"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donald Bennett v. City of Eastpointe",
          "cluster_id": 790530,
          "cite": [
            "410 F.3d 810",
            "2005 U.S. App. LEXIS 10587",
            "2005 WL 1384366"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Luis Guzman and Sonia Cruz-Lazo",
          "cluster_id": 516479,
          "cite": [
            "864 F.2d 1512",
            "1988 U.S. App. LEXIS 17681",
            "1988 WL 138644"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111378 OR 9429956 OR 9429957 OR 9429958 OR 9429959 OR 9429960) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTMzMTY4MDAwMDAwJnM9NDUyMzg4OSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111378+OR+9429956+OR+9429957+OR+9429958+OR+9429959+OR+9429960%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111378 OR 9429956 OR 9429957 OR 9429958 OR 9429959 OR 9429960)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNzAmcz0yMTkyODEwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111378+OR+9429956+OR+9429957+OR+9429958+OR+9429959+OR+9429960%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111378 OR 9429956 OR 9429957 OR 9429958 OR 9429959 OR 9429960)",
        "reviewed": 77,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 77,
        "triage_read": 0,
        "triage_snippet_classified": 77
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111378 OR 9429956 OR 9429957 OR 9429958 OR 9429959 OR 9429960)",
    "indexed_citing_opinions": 1882,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111378,
        "count": 1607,
        "count_source": "search"
      },
      {
        "opinion_id": 9429956,
        "count": 307,
        "count_source": "search"
      },
      {
        "opinion_id": 9429957,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429958,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429959,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429960,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2971,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-sharpe.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNDEzNDMmcz0xMDM0OTQxNiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111378+OR+9429956+OR+9429957+OR+9429958+OR+9429959+OR+9429960%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111378,
        "cited_id": 89440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 92216,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 96198,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 104029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 104442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 104717,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 104822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 108028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 108419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 109213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 111157,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 111226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 111280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 111305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 335159,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 383730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 395186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 399391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 405243,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 407760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 421705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 1930576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 2040129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 2090628,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 2107294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 2293646,
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
    "date_created": "2026-07-06T02:59:39Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:00:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:00:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:04:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:00:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Sharpe

```
<opinion type="majority">
<author id="b732-10">Chief Justice Burger</author>
<p id="Ajg">delivered the opinion of the Court.</p>
<p id="b732-11">We granted certiorari to decide whether an individual reasonably suspected of engaging in criminal activity may be <page-number citation-index="1" label="677">*677</page-number>detained for a period of 20 minutes, when the detention is necessary for law enforcement officers to conduct a limited investigation of the suspected criminal activity.</p>
<p id="ATs">I — I</p>
<p id="AqP">&lt;1</p>
<p id="AboI">On the morning of June 9, 1978, Agent Cooke of the Drug Enforcement Administration (DEA) was on patrol in an unmarked vehicle on a coastal road near Sunset Beach, North Carolina, an area under surveillance for suspected drug trafficking. At approximately 6:30 a. m., Cooke noticed a blue pickup truck with an attached camper shell traveling on the highway in tandem with a blue Pontiac Bonneville. Respondent Savage was driving the pickup, and respondent Sharpe was driving the Pontiac. The Pontiac also carried a passenger, Davis, the charges against whom were later dropped. Observing that the truck was riding low in the rear and that the camper did not bounce or sway appreciably when the truck drove over bumps or around curves, Agent Cooke concluded that it was heavily loaded. A quilted material covered the rear and side windows of the camper.</p>
<p id="Asq">Cooke’s suspicions were sufficiently aroused to follow the two vehicles for approximately 20 miles as they proceeded south into South Carolina. He then decided to make an “investigative stop” and radioed the State Highway Patrol for assistance. Officer Thrasher, driving a marked patrol car, responded to the call. Almost immediately after Thrasher caught up with the procession, the Pontiac and the pickup turned off the highway and onto a campground road.<footnotemark>1</footnotemark> Cooke and Thrasher followed the two vehicles as the latter drove along the road at 55 to 60 miles an hour, exceeding the speed limit of 35 miles an hour. The road eventually looped back to <page-number citation-index="1" label="678">*678</page-number>the highway, onto which Savage and Sharpe turned and continued to drive south.</p>
<p id="b734-5">At this point, all four vehicles were in the middle lane of the three right-hand lanes of the highway. Agent Cooke asked Officer Thrasher to signal both vehicles to stop. Thrasher pulled alongside the Pontiac, which was in the lead, turned on his flashing light, and motioned for the driver of the Pontiac to stop. As Sharpe moved the Pontiac into the right lane, the pickup truck cut between the Pontiac and Thrasher’s patrol car, nearly hitting the patrol car, and continued down the highway. Thrasher pursued the truck while Cooke pulled up behind the Pontiac.</p>
<p id="b734-6">Cooke approached the Pontiac and identified himself. He requested identification, and Sharpe produced a Georgia driver’s license bearing the name of Raymond J. Pavlo-vich. Cooke then attempted to radio Thrasher to determine whether he had been successful in stopping the pickup truck, but he was unable to make contact for several minutes, apparently because Thrasher was not in his patrol car. Cooke radioed the local police for assistance, and two officers from the Myrtle Beach Police Department arrived about 10 minutes later. Asking the two officers to “maintain the situation,” Cooke left to join Thrasher.</p>
<p id="b734-7">In the meantime, Thrasher had stopped the pickup truck about one-half mile down the road. After stopping the truck, Thrasher had approached it with his revolver drawn, ordered the driver, Savage, to get out and assume a “spread eagled” position against the side of the truck, and patted him down. Thrasher then holstered his gun and asked Savage for his driver’s license and the truck’s vehicle registration. Savage produced his own Florida driver’s license and a bill of sale for the truck bearing the name of Pavlovich. In response to questions from Thrasher concerning the ownership of the truck, Savage said that the truck belonged to a friend and that he was taking it to have its shock absorbers repaired. When Thrasher told Savage that he would be held <page-number citation-index="1" label="679">*679</page-number>until the arrival of Cooke, whom Thrasher identified as a DEA agent, Savage became nervous, said that he wanted to leave, and requested the return of his driver’s license. Thrasher replied that Savage was not free to leave at that time.</p>
<p id="b735-5">Agent Cooke arrived at the scene approximately 15 minutes after the truck had been stopped. Thrasher handed Cooke Savage’s license and the bill of sale for the truck; Cooke noted that the bill of sale bore the same name as Sharpe’s license. Cooke identified himself to Savage as a DEA agent and said that he thought the truck was loaded with marihuana. Cooke twice sought permission to search the camper, but Savage declined to give it, explaining that he was not the owner of the truck. Cooke then stepped on the rear of the truck and, observing that it did not sink any lower, confirmed his suspicion that it was probably overloaded. He put his nose against the rear window, which was covered from the inside, and reported that he could smell marihuana. Without seeking Savage’s permission, Cooke removed the keys from the ignition, opened the rear of the camper, and observed a large number of burlap-wrapped bales resembling bales of marihuana that Cooke had seen in previous investigations. Agent Cooke then placed Savage under arrest and left him with Thrasher.</p>
<p id="b735-6">Cooke returned to the Pontiac and arrested Sharpe and Davis. Approximately 30 to 40 minutes had elapsed between the time Cooke stopped the Pontiac and the time he returned to arrest Sharpe and Davis. Cooke assembled the various parties and vehicles and led them to the Myrtle Beach police station. That evening, DEA agents took the truck to the Federal Building in Charleston, South Carolina. Several days later, Cooke supervised the unloading of the truck, which contained 43 bales weighing a total of 2,629 pounds. Acting without a search warrant, Cooke had eight randomly selected bales opened and sampled. Chemical tests showed that the samples were marihuana.</p>
<p id="b736-4"><page-number citation-index="1" label="680">*680</page-number>B</p>
<p id="b736-5">Sharpe and Savage were charged with possession of a controlled substance with intent to distribute it in violation of <span class="citation no-link">21 U. S. C. § 841</span>(a)(1) and <span class="citation no-link">18 U. S. C. §2</span>. The United States District Court for the District of South Carolina denied respondents’ motion to suppress the contraband, and respondents were convicted.</p>
<p id="b736-6">A divided panel of the Court of Appeals for the Fourth Circuit reversed the convictions. <em>Sharpe </em>v. <em>United States, </em><span class="citation" data-id="9468447"><a href="/opinion/395186/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald...">660 F. 2d 967</a></span> (1981). The majority assumed that Cooke “had an articulable and reasonable suspicion that Sharpe and Savage were engaged in marijuana trafficking when he and Thrasher stopped the Pontiac and the truck.” <span class="citation" data-id="9468447"><a href="/opinion/395186/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/#970" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald..."><em>Id., </em>at 970</a></span>. But the court held the investigative stops unlawful because they “failed to meet the requirement of brevity” thought to govern detentions on less than probable cause. <em><span class="citation" data-id="9468447"><a href="/opinion/395186/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald...">Ibid.</a></span> </em>Basing its decision solely on the duration of the respondents’ detentions, the majority concluded that “the length of the detentions effectively transformed them into de facto arrests without bases in probable cause, unreasonable seizures under the Fourth Amendment.” <em><span class="citation" data-id="9468447"><a href="/opinion/395186/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald...">Ibid.</a></span> </em>The majority then determined that the samples of marihuana should have been suppressed as the fruit of respondents’ unlawful seizures. <span class="citation" data-id="9468447"><a href="/opinion/395186/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/#971" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald..."><em>Id., </em>at 971</a></span>. As an:alternative basis for its decision, the majority held that the warrantless search of the bales taken from the pickup violated <em>Robbins </em>v. <em>California, </em><span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/" aria-description="Citation for case: Robbins v. California">453 U. S. 420</a></span> (1981). Judge Russell dissented as to both grounds of the majority’s decision.</p>
<p id="b736-7">The Government petitioned for certiorari, asking this Court to review both of the alternative grounds held by the Court of Appeals to justify suppression. We granted the petition, vacated the judgment of the Court of Appeals, and remanded the case for further consideration in the light of the intervening decision in <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982). <em>United States </em>v. <em>Sharpe, </em><span class="citation" data-id="9032980"><a href="/opinion/9039645/united-states-v-sharpe/" aria-description="Citation for case: United States v. Sharpe">457 U. S. 1127</a></span> (1982).</p>
<p id="b737-4"><page-number citation-index="1" label="681">*681</page-number>On remand, a divided panel of the Court of Appeals again reversed the convictions. <span class="citation" data-id="9470889"><a href="/opinion/421705/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald...">712 F. 2d 65</a></span> (1983). The majority concluded that, in the light of <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>, </em>it was required to “disavow” its alternative holding disapproving the warrant-less search of the marihuana bales. But, “[fjinding that <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>does not adversely affect our primary holding” that the detentions of the two defendants constituted illegal seizures, the court readopted the prior opinion as modified. <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ibid.</a></span> </em>The majority declined “to reexamine our principal holding or to reargue the same issues that were addressed in detail in the original majority and dissenting opinions,” reasoning that its action complied with this Court’s mandate. The panel assumed that “[h]ad [this] Court felt that a reversal was in order, it could and would have said so.” <em>Id., </em>at 65, n. 1. Judge Russell again dissented.</p>
<p id="b737-5">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./467/1250/">467 U. S. 1250</a></span> (1984), and we reverse.<footnotemark>2</footnotemark></p>
<p id="b738-3"><page-number citation-index="1" label="682">*682</page-number>) — 1</p>
<p id="AK7q">A</p>
<p id="A0l">The Fourth Amendment is not, of course, a guarantee against <em>all </em>searches and seizures, but only against <em>unreasonable </em>searches and seizures. The authority and limits of the Amendment apply to investigative stops of vehicles such as occurred here. <em>United States </em>v. <em>Hensley, </em><span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#226" aria-description="Citation for case: United States v. Hensley">469 U. S. 221, 226</a></span> (1985); <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 417</a></span> (1981); <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 663</a></span> (1979); <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878, 880</a></span> (1975). In <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), we adopted a dual inquiry for evaluating the reasonableness of an investigative stop. Under this approach, we examine</p>
<blockquote id="A4U">“whether the officer’s action was justified at its inception, and whether it was reasonably related in scope to the circumstances which justified the interference in the first place.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 20</a></span>.</blockquote>
<p id="AlzC">As to the first part of this inquiry, the Court of Appeals assumed that the police had an articulable and reasonable suspicion that Sharpe and Savage were engaged in marihuana trafficking, given the setting and all the circumstances when the police attempted to stop the Pontiac and the pickup. <span class="citation" data-id="9468447"><a href="/opinion/395186/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/#970" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald...">660 F. 2d, at 970</a></span>. That assumption is abundantly supported by the record.<footnotemark>3</footnotemark> As to the second part of the in<page-number citation-index="1" label="683">*683</page-number>quiry, however, the court concluded that the 30- to 40-minute detention of Sharpe and the 20-minute detention of Savage “failed to meet the [Fourth Amendment’s] requirement of brevity.” <em><span class="citation" data-id="9468447"><a href="/opinion/395186/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald...">Ibid.</a></span></em></p>
<p id="b739-4">It is not necessary for us to decide whether the length of Sharpe’s detention was unreasonable, because that detention bears no causal relation to Agent Cooke’s discovery of the marihuana. The marihuana was in Savage’s pickup, not in Sharpe’s Pontiac; the contraband introduced at respondents’ trial cannot logically be considered the “fruit” of Sharpe’s detention. The only issue in this case, then, is whether it was reasonable under the circumstances facing Agent Cooke and Officer Thrasher to detain Savage, whose vehicle contained the challenged evidence, for approximately 20 minutes. We conclude that the detention of Savage clearly meets the Fourth Amendment’s standard of reasonableness.</p>
<p id="b739-5">The Court of Appeals did not question the reasonableness of Officer Thrasher’s or Agent Cooke’s conduct during their detention of Savage. Rather, the court concluded that the length of the detention alone transformed it from a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop into a <em>defacto </em>arrest. Counsel for respondents, as <em>ami-cus curiae, </em>assert that conclusion as their principal argument before this Court, relying particularly upon our decisions in <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979); <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983); and <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983). That reliance is misplaced.</p>
<p id="b739-6">In <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>, </em>the police picked up a murder suspect from a neighbor’s home and brought him to the police station, where, after being interrogated for an hour, he confessed. <page-number citation-index="1" label="684">*684</page-number>The State conceded that the police lacked probable cause when they picked up the suspect, but sought to justify the warrantless detention and interrogation as an investigative stop. The Court rejected this argument, concluding that the defendant’s detention was “in important respects indistinguishable from a traditional arrest.” <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 212</a></span>. <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span> </em>is simply inapposite here: the Court was not concerned with the length of the defendant’s detention, but with .events occurring during the detention.<footnotemark>4</footnotemark></p>
<p id="b740-5">In <em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span>, </em>government agents stopped the defendant in an airport, seized his luggage, and took him to a small room used for questioning, where a search of the luggage revealed narcotics. The Court held that the defendant’s detention constituted an arrest. See <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#503" aria-description="Citation for case: Florida v. Royer">460 U. S., at 503</a></span> (plurality opinion); <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#509" aria-description="Citation for case: Florida v. Royer"><em>id., </em>at 509</a></span> (Powell, J., concurring); <em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">ibid.</a></span> </em>(Brennan, J., concurring in result). As in <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>, </em>though, the focus was primarily on facts other than the duration of the defendant’s detention — particularly the fact that the police confined the defendant in a small airport room for questioning.</p>
<p id="b740-6">The plurality in <em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span> </em>did note that “an investigative detention must be temporary and last no longer than is necessary to effectuate the purpose of the stop.” <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer">460 U. S., at 500</a></span>. The Court followed a similar approach in <em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>. </em>In that case, law enforcement agents stopped the defendant after his arrival in an airport and seized his luggage for 90 minutes to take it to a narcotics detection dog for a “sniff test.” We decided that an investigative seizure of personal property could be justified under the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>doctrine, but that “[t]he length of the detention of respondent’s luggage alone precludes the conclusion that the seizure was reasonable in the absence of probable cause.” <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place">462 U. S., at 709</a></span>. However, the rationale underlying that conclusion was premised on the fact that the police knew of respondent’s arrival time <page-number citation-index="1" label="685">*685</page-number>for several hours beforehand, and the Court assumed that the police could have arranged for a trained narcotics dog in advance and thus avoided the necessity of holding respondent’s luggage for 90 minutes. “[I]n assessing the effect of the length of the detention, we take into account whether the police diligently pursue their investigation.” <em>Ibid.; </em>see also <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer"><em>Royer, supra, </em>at 500</a></span>.</p>
<p id="b741-5">Here, the Court of Appeals did not conclude that the police acted less than diligently, or that they <em>unnecessarily </em>prolonged Savage’s detention. <em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span> </em>and <em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span> </em>thus provide no support for the Court of Appeals’ analysis.</p>
<p id="b741-6">Admittedly, <em>Terry, Dunaway, Royer, </em>and <em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>, </em>considered together, may in some instances create difficult line-drawing problems in distinguishing an investigative stop from a <em>de facto </em>arrest. Obviously, if an investigative stop continues indefinitely, at some point it can no longer be justified as an investigative stop. But our cases impose no rigid time limitation on <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stops. While it is clear that “the brevity of the invasion of the individual’s Fourth Amendment interests is an important factor in determining whether the seizure is so minimally intrusive as to be justifiable on reasonable suspicion,” <em>United States </em>v. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place"><em>Place, supra, </em>at 709</a></span>, we have emphasized the need to consider the law enforcement purposes to be served by the stop as well as the time reasonably needed to effectuate those purposes. <em>United States </em>v. <em>Hensley, </em><span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#228" aria-description="Citation for case: United States v. Hensley">469 U. S., at 228-229, 234-235</a></span>; <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place"><em>Place, supra, </em>at 703-704, 709</a></span>; <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#700" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 700</a></span>, and n. 12 (1981) (quoting 3 W. LaFave, Search and Seizure § 9.2, pp. 36-37 (1978)). Much as a “bright line” rule would be desirable, in evaluating whether an investigative detention is unreasonable, common sense and ordinary human experience must govern over rigid criteria.</p>
<p id="b741-7">We sought to make this clear in <em>Michigan </em>v. <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers, supra:</a></span></em></p>
<blockquote id="b741-8">“If the purpose underlying a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop — investigating possible criminal activity — is to be served, the police must under certain circumstances be able to detain the <page-number citation-index="1" label="686">*686</page-number>individual for longer than the brief time period involved in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>and <em>Adams </em>[v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972)].” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#700" aria-description="Citation for case: Michigan v. Summers">452 U. S., at 700, n. 12</a></span>.</blockquote>
<p id="b742-5">Later, in <em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>, </em>we expressly rejected the suggestion that we adopt a hard-and-fast time limit for a permissible <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop:</p>
<blockquote id="b742-6">“We understand the desirability of providing law enforcement authorities with a clear rule to guide their conduct. Nevertheless, we question the wisdom of a rigid time limitation. Such a limit would undermine the equally important need to allow authorities to graduate their responses to the demands of any particular situation.” <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place">462 U. S., at 709, n. 10</a></span>.</blockquote>
<p id="b742-7">The Court of Appeals’ decision would effectively establish a <em>per se </em>rule that a 20-minute detention is too long to be justified under the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>doctrine. Such a result is clearly and fundamentally at odds with our approach in this area.</p>
<p id="b742-8">B</p>
<p id="b742-9">In assessing whether a detention is too long in duration to be justified as an investigative stop, we consider it appropriate to examine whether the police diligently pursued a means of investigation that was likely to confirm or dispel their suspicions quickly, during which time it was necessary to detain the defendant. See <em>Michigan </em>v. <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#701" aria-description="Citation for case: Michigan v. Summers"><em>Summers, supra, </em>at 701</a></span>, n. 14 (quoting 3 W. LaFave, Search and Seizure § 9.2, p. 40 (1978)); see also <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place">462 U. S., at 709</a></span>; <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer">460 U. S., at 500</a></span>. A court making this assessment should take care to consider whether the police are acting in a swiftly developing situation, and in such cases the court should not indulge in unrealistic second-guessing. See generally <em>post, </em>at 712-716 (Brennan, J., dissenting). A creative judge engaged in <em>post hoc </em>evaluation of police conduct can almost always imagine <page-number citation-index="1" label="687">*687</page-number>some alternative means by which the objectives of the police might have been accomplished. But “[t]he fact that the protection of the public might, in the abstract, have been accomplished by ‘less intrusive’ means does not, by itself, render the search unreasonable.” <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#447" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 447</a></span> (1973); see also <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#557" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 557, n. 12</a></span> (1976). The question is not simply whether some other alternative was available, but whether the police acted unreasonably in failing to recognize or to pursue it.</p>
<p id="b743-5">We readily conclude that, given the circumstances facing him, Agent Cooke pursued his investigation in a diligent and reasonable manner. During most of Savage’s 20-minute detention, Cooke was attempting to contact Thrasher and enlisting the help of the local police who remained with Sharpe while Cooke left to pursue Officer Thrasher and the pickup. Once Cooke reached Officer Thrasher and Savage,<footnotemark>5</footnotemark> he proceeded expeditiously: within the space of a few minutes, he examined Savage’s driver’s license and the truck’s bill of sale, requested (and was denied) permission to search the truck, stepped on the rear bumper and noted that the truck did not move, confirming his suspicion that it was probably overloaded. He then detected the odor of marihuana.</p>
<p id="b743-6">Clearly this case does not involve any delay unnecessary to the legitimate investigation of the law enforcement officers. Respondents presented no evidence that the officers were dilatory in their investigation. The delay in this case was <page-number citation-index="1" label="688">*688</page-number>attributable almost entirely to the evasive actions of Savage, who sought to elude the police as Sharpe moved his Pontiac to the side of the road.<footnotemark>6</footnotemark> Except for Savage’s maneuvers, only a short and certainly permissible pre-arrest detention would likely have taken place. The somewhat longer detention was simply the result of a “graduate[d] . . . respons[e] to the demands of [the] particular situation,” <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place"><em>Place, supra, </em>at 709, n. 10</a></span>.</p>
<p id="b744-4">We reject the contention that a 20-minute stop is unreasonable when the police have acted diligently and a suspect’s actions contribute to the added delay about which he complains. The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b744-5">
<em>Reversed and remanded.</em>
</p>
<footnote label="1">
<p id="A2Y"> Officer Thrasher testified that the respondents’ vehicles turned off the highway “[a]bout one minute” after he joined the procession. 4 Record 141. <page-number citation-index="1" label="682">*682</page-number>principle is wholly irrelevant when the defendant has had his conviction nullified and the government seeks review here. Thus, when confronted with precisely this situation in <em>Florida </em>v. <em>Rodriguez, </em><span class="citation" data-id="9429786"><a href="/opinion/111280/florida-v-rodriguez/" aria-description="Citation for case: Florida v. Rodriguez">469 U. S. 1</a></span> (1984) <em>(per curiam), </em>we did not hesitate to reach and decide the merits of the case; had we thought that we should decline to reach every constitutional issue that <em>might </em>become moot, we would have denied certiorari. Cf. <em>Eisler </em>v. <em>United States, </em><span class="citation" data-id="9420393"><a href="/opinion/104717/eisler-v-united-states/#194" aria-description="Citation for case: Eisler v. United States">338 U. S. 189, 194</a></span> (1949) (Murphy, J., dissenting) (“That the ease may become moot if a defendant does not return does not distinguish it from any other case we decide. For subsequent events may render any decision nugatory”).</p>
</footnote>
<footnote label="2">
<p id="b737-6"> We granted certiorari on June 18, 1984. On August 27, counsel for respondents notified the Court that respondents had become fugitives. On October 1, we directed counsel for respondents to file a brief as <em>amicus curiae </em>in support of affirmance of the Court of Appeals’ judgment. Because our reversal of the Court of Appeals’ judgment may lead to the reinstatement of respondents’ convictions, respondents’ fugitive status does not render this case moot. See <em>United States </em>v. <em>Villamonte-Marquez, </em><span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/#581" aria-description="Citation for case: United States v. Villamonte-Marquez">462 U. S. 579, 581-582, n. 2</a></span> (1983); <em>Molinaro </em>v. <em>New Jersey, </em><span class="citation" data-id="108028"><a href="/opinion/108028/molinaro-v-new-jersey/#366" aria-description="Citation for case: Molinaro v. New Jersey">396 U. S. 365, 366</a></span> (1970) <em>(per curiam).</em></p>
<p id="b737-7">Justice Stevens would have this Court adopt a rule that, whenever a respondent or appellee before the Court becomes a fugitive before we render a decision, we must vacate the judgment under review and remand with directions to dismiss the appeal. This theory is not supported by our precedents, and indeed would be a break with a recent decision. The line of authority upon which the dissent relies concerns the situation in which a fugitive defendant is the party seeking review here. In those very different cases, dismissal of the petition or appeal is based on the equitable principle that a fugitive from justice is “disentitled” to call upon this Court for a review of his conviction. See <em>United States </em>v. <em>Campos-Serrano, </em><span class="citation" data-id="9424706"><a href="/opinion/108419/united-states-v-campos-serrano/#294" aria-description="Citation for case: United States v. Campos-Serrano">404 U. S. 293, 294-295, n. 2</a></span> (1971); <span class="citation" data-id="108028"><a href="/opinion/108028/molinaro-v-new-jersey/#366" aria-description="Citation for case: Molinaro v. New Jersey"><em>Molinaro, supra, </em>at 366</a></span>; see also <em>Estelle </em>v. <em>Dorrough, </em><span class="citation" data-id="9426020"><a href="/opinion/109213/estelle-v-dorrough/#541" aria-description="Citation for case: Estelle v. Dorrough">420 U. S. 534, 541-542</a></span> (1975) <em>(per curiam). </em>This equitable</p>
</footnote>
<footnote label="3">
<p id="AT5"> Agent Cooke had observed the vehicles traveling in tandem for 20 miles in an area near the coast known to be frequented by drug traffickers. Cooke testified that pickup trucks with camper shells were' often used to <page-number citation-index="1" label="683">*683</page-number>transport large quantities of marihuana. App. 10. Savage’s pickup truck appeared to be heavily loaded, and the windows of the camper were covered with a quilted bed-sheet material rather than curtains. Finally, both vehicles took evasive actions and started speeding as soon as Officer Thrasher began following them in his marked car. See n. 1, <em>supra. </em>Perhaps none of these facts, standing alone, would give rise to a reasonable suspicion; but taken together as appraised by an experienced law enforcement officer, they provided clear justification to stop the vehicles and pursue a limited investigation.</p>
</footnote>
<footnote label="4">
<p id="b740-7"> The pertinent facts relied on by the Court in <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span> </em>were that (1) the defendant was taken from a private dwelling; (2) he was transported unwillingly to the police station; and (3) he there was subjected to custodial interrogation resulting in a confession. See <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 212</a></span>.</p>
</footnote>
<footnote label="5">
<p id="b743-7"> It was appropriate for Officer Thrasher to hold Savage for the brief period pending Cooke’s arrival. Thrasher could not be certain that he was aware of all of the facts that had aroused Cooke’s suspicions; and, as a highway patrolman, he lacked Cooke’s training and experience in dealing with narcotics investigations. In this situation, it cannot realistically be said that Thrasher, a state patrolman called in to assist a federal agent in making a stop, acted unreasonably because he did not release Savage based solely on his own limited investigation of the situation and without the consent of Agent Cooke.</p>
</footnote>
<footnote label="6">
<p id="b744-11"> Even if it could be inferred that Savage was not attempting to elude the police when he drove his car <em>between </em>Thrasher’s patrol car and Sharpe’s Pontiac — in the process nearly hitting the patrol car, see App. 17, 37 — such an assumption would not alter our analysis or our conclusion. The significance of Savage’s actions is that, whether innocent or purposeful, they made it necessary for Thrasher and Cooke to split up, placed Thrasher and Cooke out of contact with each other, and required Cooke to enlist the assistance of local police before he could join Thrasher and Savage.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Small.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Small
type: case
citation: "944 F.3d 490 (2019)"
parallel_cite: ""
neutral_cite: ""
court: 4th Cir.
court_level: coa
circuit: ca4
year: 2019
date_decided: 2019-12-06
docket: 18-4327
authority_weight: "Binding in-circuit — 4th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4684957/united-states-v-dontae-small/"
  cluster_id: 4684957
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Small
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Abandonment]]"
    role: Key
related:
  - "[[Abandonment]]"
  - "[[California v. Greenwood]]"
  - "[[Abel v. United States]]"
  - "[[Riley v. California]]"
  - "[[Katz v. United States]]"
tags:
  - case
  - fourth-amendment
  - abandonment
  - reasonable-expectation-of-privacy
  - cell-phone
  - digital-privacy
  - fourth-circuit
holding: "A person who intentionally discards property to evade capture abandons any reasonable expectation of privacy in it, and abandonment is assessed on the objective information available to officers at the time of the search, so where Small crashed through a security gate, fled on foot, and threw down his cell phone along with other belongings, the warrantless searches of the phone did not violate the Fourth Amendment and Riley did not preserve the phone's digital contents once the physical device was abandoned."
aliases:
  - United States v. Small
  - "United States v. Small (4th Cir. 2019)"
---

# United States v. Small

*944 F.3d 490 (4th Cir. 2019)* (No. 18-4327) · U.S. Court of Appeals for the Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4684957 → lead opinion 4462210 (944 F.3d 490, decided 2019-12-06); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — the CL opinion text is slip/paragraph-paginated). S9 promotes. -->

## Background
After crashing a vehicle through the gates of the National Security Agency at Fort Meade, Dontae Small fled on foot as the facility went into lockdown. During the ensuing manhunt, search personnel found items strewn along his path: a bloody shirt and hat near the crashed car, and — several hours later, around 5:00 a.m. — a cell phone lying about fifty yards away in a grassy area, not where a person would ordinarily set a phone down. Officers conducted warrantless searches of the phone, recovering location data and text messages later used against Small. He moved to suppress, arguing the searches violated the Fourth Amendment; the district court denied the motion, finding that Small had abandoned the phone, and he was convicted.

## Issue
Whether a fleeing suspect who discards his cell phone during flight retains a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the device — and in its digital contents — such that the warrantless searches of the phone violated the Fourth Amendment.

## Rule
Abandonment is an exception to the warrant requirement, and it turns not on formal property law but on whether the person retained a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the thing said to be abandoned, judged from the objective facts known to officers when they searched. As the panel put it: "A finding of abandonment is based 'not [on] whether all formal property rights have been relinquished, but whether the complaining party retains a reasonable expectation of privacy in the articles alleged to be abandoned.'" — 944 F.3d 490, slip op. at 18. ^pin-op18

## Application
The objective circumstances made the district court's abandonment finding sensible: Small fled from police after crashing through a secure gate where he had no right to be, leaving behind his car, a shirt, and a hat, and then his phone turned up nearby in a grassy area rather than somewhere a person's phone would ordinarily rest. A fleeing suspect has an obvious motive to ditch a phone whose GPS could lead officers to him, and shirts and hats do not fall off by accident at the same moments a car is abandoned. On those facts, known to the searchers at the time, Small no longer had a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the phone. Invoking Riley, Small argued that even if he abandoned the physical device he did not abandon its digital contents, but the court rejected the distinction: Riley itself recognized that case-specific exceptions may still justify a warrantless search of a phone, and abandonment is such an exception.

## Conclusion
The denial of suppression was **affirmed**: by deliberately discarding his phone during flight, Small relinquished his [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in both the device and its contents.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Small* carries the classic *[[Abandonment]]* doctrine — property discarded in flight loses Fourth Amendment protection (*[[California v. Greenwood|Greenwood]]*, *[[Abel v. United States|Abel]]*) — into the digital age: abandoning a **phone** abandons the expectation of privacy in its **data**, and *[[Riley v. California|Riley]]*'s warrant rule for [[Search Incident to Arrest|searches incident to arrest]] does not resurrect that expectation. Teach the objective, time-of-search inquiry and the physical-device-versus-digital-contents argument the court rejected.

## Appears on
- [[Abandonment]] — *Key*

## Sources
- [*United States v. Small*, 944 F.3d 490 (4th Cir. 2019)](https://www.courtlistener.com/opinion/4684957/united-states-v-dontae-small/) — pinpoint: slip op. at 18 (abandonment turns on retained expectation of privacy, judged on objective facts at the time of search; the CL opinion text carries slip/paragraph pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9042ef052119e1bc", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "944 F.3d 490 (2019)", "court": "4th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Small", "year": "2019"}}
{"assertion_id": "021fe4a72021915c", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A person who intentionally discards property to evade capture abandons any reasonable expectation of privacy in it, and abandonment is assessed on the objective information available to officers at the time of the search, so where Small crashed through a security gate, fled on foot, and threw down his cell phone along with other belongings, the warrantless searches of the phone did not violate the Fourth Amendment and Riley did not preserve the phone's digital contents once the physical device was abandoned.", "title": "United States v. Small"}}
{"assertion_id": "8405db8ee173f6af", "dimension": "support", "kind": "home_role", "locator": {"home": "Abandonment"}, "payload": {"home": "Abandonment", "role": "Key", "title": "United States v. Small"}}
{"assertion_id": "0d859278386319cc", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 4th Cir.", "title": "United States v. Small"}}
{"assertion_id": "9f98a8549c32634d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Small", "varies_by_point": "false"}}
```

### lake record — United States v. Small

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Small",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Dontae Small",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Small",
    "court": "4th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca4",
    "state": null,
    "date_decided": "2019-12-06",
    "year": 2019,
    "docket": "18-4327",
    "cluster_id": 4684957,
    "lead_opinion_id": 4462210,
    "sibling_ids": [],
    "absolute_url": "/opinion/4684957/united-states-v-dontae-small/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "944 F.3d 490",
      "volume": "944",
      "reporter": "F.3d",
      "page": "490",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "944 F.3d 490",
        "volume": "944",
        "reporter": "F.3d",
        "page": "490",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "944 F.3d 490",
    "official_selection": {
      "court_class": "coa",
      "selected": "944 F.3d 490",
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
    "date_created": "2026-07-07T18:17:58Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:17:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:17:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:17:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:17:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-small--4684957",
      "to_record_id": "United States v. Small",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Small

```
                                     PUBLISHED

                      UNITED STATES COURT OF APPEALS
                          FOR THE FOURTH CIRCUIT


                                     No. 18-4327


UNITED STATES OF AMERICA,

            Plaintiff – Appellee,

v.

DONTAE SMALL,

            Defendant – Appellant.



Appeal from the United States District Court for the District of Maryland, at Baltimore.
James K. Bredar, Chief District Judge. (1:16-cr-00086-JKB-1)


Argued: October 31, 2019                                   Decided: December 6, 2019


Before WILKINSON, KING, and HARRIS, Circuit Judges.


Affirmed by published opinion. Judge Wilkinson wrote the opinion, in which Judge King
and Judge Harris joined.


ARGUED: Brandon Lee Boxler, GIBSON, DUNN & CRUTCHER LLP, Washington,
D.C., for Appellant. Sandra Wilkinson, OFFICE OF THE UNITED STATES
ATTORNEY, Baltimore, Maryland, for Appellee. ON BRIEF: Paresh S. Patel, OFFICE
OF THE FEDERAL PUBLIC DEFENDER, Greenbelt, Maryland; David J. Debold, Travis
S. Andrews, Raymond D. Moss Jr., GIBSON, DUNN & CRUTCHER LLP, Washington,
D.C., for Appellant. Robert K. Hur, United States Attorney, Paul A. Riley, Assistant
United States Attorney, Charles Kassir, Law Clerk, OFFICE OF THE UNITED STATES
ATTORNEY, Baltimore, Maryland, for Appellee.




                                       2
WILKINSON, Circuit Judge:

       Following a six-day trial, a jury in the United States District Court for the District

of Maryland found defendant-appellant Dontae Small guilty of federal carjacking, in

violation of 18 U.S.C. § 2119(1); conspiracy to commit carjacking, in violation of 18

U.S.C. § 371; and destruction of government property, in violation of 18 U.S.C. § 1361.

       In the proceedings below, Small made several motions relevant to the instant appeal,

all of which were denied by the district court: (1) a motion for judgment of acquittal on the

carjacking and conspiracy charges; (2) a motion to suppress evidence related to a cell phone

search; and (3) a motion to excuse and question two jurors on Sixth Amendment grounds.

Small now appeals these denials and requests that we vacate his convictions. Because we

conclude that the district court did not err in denying these motions, Small’s convictions

are affirmed.

                                             I.

                                             A.

       On October 4, 2015, Baltimore resident Brandon Rowe turned around and saw “a

gun in my face.” J.A. 181. Rowe and his fiancée had just returned from vacation to their

house in Baltimore’s Federal Hill neighborhood. It was after 10:00 pm, and there were no

open parking spots in front of their home. They double-parked and quickly unloaded their

car, a silver Acura TSX. Then Rowe drove off alone in search of parking while his fiancée

went into the house. He parked the car in a spot roughly a block away and began walking

back. Within a minute, Rowe was confronted by three masked men, one armed with a “gray

silver gun.” J.A. 182. The gunman demanded that Rowe hand over everything he had.

                                             3
Rowe responded that he had only two sets of keys on him, his car keys and house keys. He

handed over his car keys but told his assailants that he wasn’t giving them his house keys.

The men patted Rowe down and felt his pockets to confirm that he had nothing else of

value. Throughout this entire interaction, the gun remained pointed at Rowe’s face.

       After taking Rowe’s car keys, the gunman ordered Rowe to follow his assailants,

who were walking toward the parked car. Rowe refused and instead turned around and

walked home. His assailants did not pursue him. Rowe called 911 after arriving home, and

officers responded rapidly. Later that night, Rowe was driven past the spot where he had

parked his Acura. The car was gone.

       Shortly before Rowe was confronted by his three masked assailants, an armed

robbery took place in the same neighborhood. Around 10:00 pm, Hannah Caswell and Joe

Dougherty were walking home from dinner. As Caswell and Dougherty were passing a

white minivan parked on the street, a masked man holding a silver gun stepped out in front

of them and blocked their path. He held the gun to Caswell’s head and demanded that

Caswell and Dougherty empty their pockets. When Dougherty refused to hand anything

over “until the gunmen took the gun out of [Caswell’s] face,” J.A. 238, a second man came

from behind the minivan and ripped open Dougherty’s pocket, causing his cell phone to

fall to the ground. The gunman picked up the phone and both assailants took off running.

The white minivan pulled out of its parking spot and followed. Dougherty and Caswell

used a neighbor’s phone to call the police. Their descriptions of the silver gun and the

assailants were consistent with Rowe’s.

                                            B.

                                            4
       On October 7, 2015, three days after the armed robbery and carjacking, a man later

identified as Dontae Small drove a silver Acura into the Arundel Mills Mall parking lot

shortly after 8:00 pm. Security cameras on the premises scanned the car’s license plate,

which revealed that it was Rowe’s stolen Acura. Police were called, and officers from the

Anne Arundel County Police Department set up a perimeter around the parked car and

waited for its driver to return. Small returned to the parking lot at approximately 8:50 pm,

unlocked the Acura, and got into the driver’s seat. At this point, one of the officers pulled

his marked squad car behind the Acura and activated his emergency equipment.

       Rather than surrender, Small drove the Acura over a curb and fled the scene.

Numerous officers followed in pursuit, and a high-speed chase ensued. After driving for

nearly five miles, Small sped through the outbound gate at Fort Meade. Once inside Fort

Meade, and with law enforcement still in pursuit, Small drove through a fence surrounding

the National Security Agency (“NSA”) facility and crashed down an embankment. Though

officers arrived at the scene of the crash “within [a] minute,” Small had disappeared. J.A.

63. Small would not be found until he emerged from a nearby sewer around 10:00 am the

following morning.

       Unable to immediately locate the driver of the Acura, police called for backup and

began to set up a perimeter. Beginning at around 10:00 pm and continuing for over twelve

hours, approximately 200 state and federal officers conducted an extensive search of the

area. Appellant’s Opening Br. at 9. During this time, the NSA was put “on a lock down”

until authorities could locate the driver. Appellee’s Br. at 28 (quoting Aff. in Supp. Search

Warrant, Dist. Ct. Docket #25, Ex. A).

                                             5
         Though the authorities did not immediately locate Small, they did find several items

of interest while searching the NSA grounds. At 1:45 am, officers found a black hat and a

white t-shirt stained with blood near the crash site. Later, at 4:52 am, search personnel

discovered a cell phone on the ground approximately fifty yards from the bloody shirt and

hat. J.A. 30, 32-33. Detective William Bailey of the Baltimore City Police Department, the

lead investigator on Rowe’s carjacking, retrieved the phone and took it to a “floating

command center.” J.A. 30-31.

         At the command center, NSA Special Agent Kristel Massengale observed that the

cell phone was receiving calls from a person identified on the screen as “Sincere my Wife.”

J.A. 167-68. At 5:18 am, without obtaining a warrant, Agent Massengale used the phone

to call “Sincere” back. Sincere, whose real name is Kimberly Duckfield, informed Agent

Massengale that the phone belonged to her husband, Dontae Small. Police quickly obtained

a photo of Small and found it matched security footage of the driver from the Arundel Mills

Mall. Based on this evidence, police concluded that Small was likely the driver of the stolen

Acura.

         Throughout the early morning hours, officers used the cell phone three more times

without obtaining a warrant. First, at 7:24 am, Detective Bailey called Duckfield and

inquired into whether Small had returned home. Duckfield said no. Next, at 8:21 am,

Duckfield called Small’s phone. Bailey answered and informed Duckfield that police were

looking for Small. Finally, Bailey removed the phone’s back casing and battery to locate

its serial number and other identifying information.



                                              6
       At approximately 10:00 am, Small emerged from the sewer system through a

manhole “a little bit” away from the locations of the crash and scattered items. J.A. 42.

Soon after, Small was spotted by NSA Police Officer Hugh McCall, who asked him to

identify himself. Small responded by fleeing on foot. After a brief chase, Officer McCall

caught Small and placed him under arrest.

       In the weeks following Small’s arrest, the government obtained three search

warrants relating to his cell phone. The warrant applications contained Small’s name and

the phone’s serial number—information that the government had learned from its use of

the phone during the manhunt. The warrants authorized the government to collect: (1) the

call history, text messages, internet browsing history, contacts, and deleted data from

Small’s phone; (2) the historical cell site location data for Small’s phone; and (3) records

of outgoing and incoming calls for a second cell phone that Small’s phone had called on

the day of the robberies. The government relied on evidence obtained pursuant to these

warrants at Small’s trial.

                                            C.

       After his arrest, Small was charged with the carjacking of Rowe’s Acura, in

violation of 18 U.S.C. § 2119(1); conspiracy to commit carjacking, in violation of 18

U.S.C. § 371; and destruction of government property for crashing through the NSA fence,

in violation of 18 U.S.C. § 1361.

       The district court empaneled a jury on October 16, 2017, with Small’s trial set to

begin the following day. The next morning, before proceedings began, jurors 5 and 11

approached the Courtroom Deputy to share their concerns that several individuals had been

                                             7
“watching” them as they exited the jury room the previous evening. J.A. 49. The jurors

noted that at least one of these individuals was carrying a cell phone, though they could not

tell if any videos or photographs were taken. The Courtroom Deputy relayed these concerns

to the district judge.

       In response, the district judge took two steps. First, he ensured that court security

officers (“CSOs”) were posted outside both the courtroom and the jury room. Second, he

directed the Courtroom Deputy to inform jurors 5 and 11 of the additional security

measures and that any further concerns should be brought to the attention of the CSOs or

the Courtroom Deputy. The district judge did not disclose the extra security precautions to

the rest of the jurors, nor did he inform them of jurors 5 and 11’s concerns. He believed

that doing so could cause “more harm than good” by drawing attention to concerns that

were “of a pretty vague nature” and possibly based on “misperceptions.” J.A. 51-52.

Immediately before opening statements, the district judge informed the parties of this

situation. Small’s counsel had no immediate objection to the remedial steps taken by the

district judge.

       Small’s trial commenced as scheduled on October 17. The government presented

testimony from Rowe, Caswell, Dougherty, law enforcement officers involved in the

manhunt at the NSA, a forensic expert in cellular data analysis, and others. Much of this

evidence sought to link Small to Rowe’s carjacking. A friend of Small’s, Jamia Butler,

testified that Small had borrowed a white minivan from her on the day of the carjacking

and armed robbery. She stated that Small told her he would be using the van to give his

associate, Ronald Hall, a ride, and that she saw Small and Hall drive off together that day.

                                             8
Caswell and Dougherty testified about the white minivan present during their robbery. The

government later presented evidence that Hall resembled the gunman who accosted Rowe.

       An expert in cellular analysis testified that Small and Hall’s cell phones were used

in the Federal Hill neighborhood around the time of the carjacking and robbery. Call data

showed that the two were in constant communication that night, exchanging multiple calls

and text messages. Shortly before masked assailants approached Rowe, Small sent Hall a

text message that read: “Get da dude cpming down da st.i parked on . . . .” J.A. 599. The

government also introduced incriminating excerpts from nine calls that Small made from

state custody in 2016. J.A. 458; see, e.g., J.A. 579-80 (“They said it was three people. All

of them had on masks. . . . It was four individuals babe. . . . I was the driver.”). On October

25, 2017, after the trial concluded, the jury found Small guilty of all three counts. He was

sentenced to 324 months in prison.

                                              D.

       During the course of proceedings before the district court, Small made three motions

relevant to the instant appeal. First, at the close of evidence, Small made a motion for a

judgment of acquittal on the carjacking and conspiracy charges on the grounds that the

government had failed to offer evidence sufficient to establish the mens rea element of

carjacking under 18 U.S.C. § 2119. Specifically, he asserted that no reasonable juror could

conclude that he or his coconspirators possessed § 2119’s requisite “intent to cause death

or serious bodily harm” during Rowe’s carjacking. The district court denied Small’s

motion, finding that the government’s evidence with respect to intent was sufficient to send

the question to the jury.

                                              9
       Second, prior to trial, Small filed a motion to suppress evidence derived from or

related to his cell phone. He asserted that the four warrantless searches of his phone violated

the Fourth Amendment, rendering all evidence stemming from those searches—including

his cell phone location data and text messages—inadmissible. 1 The district court denied

Small’s motion, concluding that no warrant was required for the searches because Small

had abandoned his phone.

       Third, shortly after trial began, Small moved to excuse and question jurors 5 and 11,

based on concerns that the incident outside the jury room “would influence their verdicts

in such a way that they would no longer be . . . fair and impartial jurors . . . .” J.A. 87-88.

The district court declined to take either step, finding that the defendant’s requested relief

was not warranted based on the sparse information presented.

       Small now appeals the district court’s denial of these three motions.

                                              II.

                                              A.

       Under 18 U.S.C. § 2119, a person commits the crime of federal carjacking if he or

she, “(1) with intent to cause death or serious bodily harm (2) took a motor vehicle (3) that

had been transported, shipped or received in interstate or foreign commerce (4) from the

person or presence of another (5) by force and violence or intimidation.” United States v.


       1
        At times, the government implies that its limited uses of Small’s phone prior to
obtaining a warrant did not qualify as searches for Fourth Amendment purposes. See
Appellee’s Br. at 14, 26-28. Because this issue was not fully briefed and ultimately does
not impact our holding, we will simply assume for the purposes of our analysis that four
warrantless searches of Small’s phone occurred. Infra Section III.

                                              10
Foster, 507 F.3d 233, 246-47 (4th Cir. 2007) (quoting United States v. Applewhaite, 195

F.3d 679, 685 (3d Cir. 1999)).

       Section 2119’s mens rea component, a specific intent requirement, is satisfied

whether the defendant unconditionally or conditionally “inten[ded] to cause death or

serious bodily harm,” 18 U.S.C. § 2119, during a carjacking. Holloway v. United States,

526 U.S. 1, 8, 12 (1999). That is, the government need not prove that the defendant intended

to cause death or serious harm “if unnecessary to steal the car,” so long as it shows that “at

the moment the defendant demanded or took control over the driver’s automobile the

defendant possessed the intent to seriously harm or kill the driver if necessary to steal the

car . . . .” Id. at 12 (emphasis added).

       To establish conditional intent, the government must provide evidence above and

beyond “an empty threat, or intimidating bluff” made by the defendant during the

carjacking. Holloway, 526 U.S. at 11. Section 2119’s “by force and violence or by

intimidation” actus reus requirement remains distinct from its mens rea requirement: an

empty threat would satisfy the former but not the latter. Id. at 11-12. If the defendant were

unwilling to follow through on an intimidating bluff, then he would lack the intent “to

seriously harm or kill the driver if that action had been necessary to complete the taking of

the car.” Id. With these points in mind, we turn to the facts of the case at hand.

                                              B.

       Small claims that there is insufficient evidence to sustain his conspiracy and

carjacking convictions, and that the district court erred in denying his motion to this effect.

Specifically, Small contends that the government failed to present sufficient evidence for

                                              11
a reasonable juror to find that he or his coconspirators acted with “intent to cause death or

serious bodily harm” as required by 18 U.S.C. § 2119.

       A defendant who challenges the sufficiency of the evidence “faces a heavy burden.”

Foster, 507 F.3d at 245. A jury verdict will be sustained so long as “there is substantial

evidence in the record to support it.” United States v. Wilson, 198 F.3d 467, 470 (4th Cir.

1999). When evaluating the sufficiency of the evidence, “we view the evidence in the light

most favorable to the government,” id., and ask whether “any rational trier of fact could

have found the essential elements of the crime beyond a reasonable doubt,” Jackson v.

Virginia, 443 U.S. 307, 319 (1979) (emphasis in original).

       Small fails to carry his burden. There is substantial evidence in the record from

which a reasonable juror could conclude that Small or his coconspirators intended to

seriously harm or kill Rowe if necessary to steal his vehicle. The facts of this case are

chilling: no ordinary vehicle theft took place here. Rowe was walking alone at night on a

deserted street. He was accosted by three men—wearing masks—one of whom was holding

a gun. The armed assailant demanded everything Rowe had while pointing the gun “in [his]

face.” J.A. 181. The gun would remain trained on Rowe, only a foot from his head,

throughout the entire interaction. Furthermore, the assailants made physical contact with

their victim; when Rowe said he had only keys on him, they “patted [him] down” and “felt

in [his] pockets.” J.A. 182-83. Even after Rowe’s assailants had his car keys, they tried to

make him follow them to another location. All of this evidence allowed the jury to infer

that Small or his coconspirators possessed the intent to seriously harm or kill Rowe if

necessary to steal his car.

                                             12
       Although juries evaluating intent are entitled to consider the entirety of the

circumstances surrounding a carjacking, see United States v. Fekete, 535 F.3d 471, 481

(6th Cir. 2008), two facts are of particular note in the case at hand: (1) an assailant pointed

a gun at Rowe; and (2) an assailant made physical contact with Rowe. First and foremost,

an assailant’s wielding a gun provides a strong indication of intent to inflict bodily harm if

met with resistance, particularly when “the perpetrator[] did not merely display a

gun . . . but rather pointed the gun at the [victim] in demanding car keys and other

possessions.” United States v. Franklin, 545 F. App’x 243, 249 (4th Cir. 2013); see also

United States v. Robinson, 855 F.3d 265, 269 (4th Cir. 2017) (finding “plenty of evidence

of . . . intent” when the defendant pointed a gun at the carjacking victim’s head and

threatened her); Foster, 507 F.3d at 247 (finding element of intent satisfied when the

defendant held a gun to the victim’s head, ordered him out of the car, and refused him

reentry).

       In addition, an assailant’s physical touching of a victim during a carjacking—

whether by hand or with a weapon—supports a jury’s finding of intent. See Franklin, 545

F. App’x at 249 (finding that a defendant’s “‘grop[ing]’ [of] one of the vehicle’s passengers

[while] searching for items to steal” supported the jury’s finding of intent); Fekete, 535

F.3d at 478 (noting that courts often look to “whether there was physical violence or

touching” to determine whether § 2119’s intent requirement is satisfied). And while the

gunman here did not touch his weapon to Rowe’s head, he very nearly did so by pointing

it from only a foot away. See United States v. Adams, 265 F.3d 420, 425 (6th Cir. 2001)

(adopting a general rule that “physically touching a victim with a weapon, standing

                                              13
alone, . . . indicates an intent on the part of the defendant to act violently” as required by

§ 2119); cf. United States v. Bailey, 819 F.3d 92, 97-98 (4th Cir. 2016) (declining to find

§ 2119’s intent element satisfied when the defendant held an object to the victim’s neck

but there was no evidence that it was a weapon).

          Small attempts to undermine the jury’s finding by noting several characteristics of

the carjacking at hand: first, Rowe’s assailants did not verbally threaten him; second, the

government did not present proof that the gun was loaded; and third, Rowe’s assailants did

not harm him when he failed to follow certain instructions. While it is true that these factors

are relevant to intent, none are dispositive. They speak to evidentiary weight, a matter that

belongs with the jury. Jackson, 443 U.S. at 318-19 (“Th[e] [sufficiency of the evidence]

standard gives full play to the responsibility of the trier of fact . . . to weigh the evidence,

and to draw reasonable inferences from basic facts to ultimate facts.”); Robinson, 855 F.3d

at 269.

          Take the lack of verbal threats. While verbally threatening the victim can certainly

help establish intent, see Robinson, 855 F.3d at 269, there is no bar to finding intent in

cases that lack verbal threats, see Foster, 507 F.3d at 247. Indeed, it is difficult to imagine

a more effective threat than holding a gun to someone’s head. A reasonable juror in the

case at hand could well conclude that Rowe’s assailants were letting the gun do the talking.

          Nor does the lack of proof that the gun was loaded decide this case. Fekete, 535

F.3d at 478 (“[T]he issue of whether a carjacker’s firearm was loaded has generally not

been treated by the courts as outcome-dispositive. Rather, the courts have looked at the

totality of the relevant circumstances . . . .”). The carjacking statute does not require the

                                               14
use of a loaded gun; it requires that a defendant have the “intent to cause death or serious

bodily harm.” 18 U.S.C. § 2119; see also Fekete, 535 F.3d at 480. Here, the government

presented testimony from gun owner Caswell and military veteran Dougherty indicating

that their masked assailant’s weapon was real. Rowe believed so as well. And as too many

crime victims know, even an unloaded firearm is capable of causing harm. See Fekete, 535

F.3d at 480 (noting the danger of pistol-whipping). Based on the evidence presented here,

a reasonable juror could conclude that—even if Rowe’s assailants carried an unloaded

gun—“[they] nonetheless had the requisite conditional intent to cause death or serious

bodily harm by other means (e.g., pistol-whipping or brute force),” id.

       Finally, Small alludes to the fact that Rowe’s assailants did not harm him when he

failed to follow their instructions. But this is not persuasive. Under § 2119, the defendant’s

intent is examined as of “the precise moment he demanded or took control over the car.”

Holloway, 526 U.S. at 8 (emphasis added). Although Rowe refused to give his assailants

his house keys, likely to avoid endangering his fiancée, he turned over his car keys instantly

and without protest. A reasonable juror could conclude that this scenario would have

played out differently, even tragically, if Rowe had also refused to turn over his car keys.

Similarly, while Rowe refused to follow his assailants to an unknown location, this

occurred after he had already handed over his car keys. A reasonable juror could conclude

that Rowe’s assailants felt no need to harm him at that point because they already had

something of value—his car keys.

       Small next argues that a finding of intent in the case at hand would place our circuit

in conflict with others. As Small notes, two circuits have held that merely brandishing a

                                             15
gun is insufficient as a matter of law to demonstrate an “intent to cause death or serious

bodily harm,” 18 U.S.C. § 2119. Fekete, 535 F.3d at 480-81 (“[I]n the absence of a physical

touching or direct proof that the firearm was loaded, the government must establish

‘brandishing-plus’ in order to satisfy § 2119’s specific intent element.”); United States v.

Randolph, 93 F.3d 656, 664 (9th Cir. 1996) (“We conclude that the brandishing of a

weapon, without more, does not support an inference of specific intent under § 2119.”),

abrogated by Holloway, 526 U.S. 1 (1999).

       As an initial matter, it is unclear that our holding conflicts with those of our sister

circuits. To the extent that “more” than brandishing is required to establish intent, Rowe’s

assailants did not merely “brandish” a gun. They pointed and trained it at his head. They

physically touched Rowe during the carjacking, when they patted him down. As such, the

“brandishing-plus” test from Fekete would not apply: it is used “in the absence of a physical

touching” of the victim. Fekete, 535 F.3d at 478, 480-81. If we have any disagreement with

our sister circuits—and it is not clear we do—it is limited to precisely when the question

of intent switches from one of fact for the jury, see Robinson, 855 F.3d at 269, to one of

law for the courts. Put another way, after a jury has found § 2119’s specific intent

requirement satisfied and returned a verdict of guilty under unexceptional instructions,

when can a court step in and proclaim that no reasonable jury could have reached that very

conclusion? Jurors excel in cases such as this, where they are asked to apply their common

sense to the factual scenario before them. Thus, we have cautioned that “[c]ourts must resist

invading the jury’s province by transforming questions of fact into matters of law.”

Robinson, 855 F.3d at 269. We decline to invade the jury’s province here. The carjacking

                                             16
and conspiracy charges against Small were properly submitted to the jury, and the jury

returned a verdict of guilty.

       Jury verdicts are entitled to respect. The jury here found that Small or his

coconspirators possessed the “intent to cause death or serious bodily harm,” 18 U.S.C.

§ 2119, when in the course of taking his car they demanded at gunpoint that Rowe hand

over everything he had. We decline to overturn the jury’s conclusion on this question of

fact, since “it is clearly the jury’s duty, not ours, to decide it.” Robinson, 855 F.3d at 269.

                                              III.

                                              A.

       We next address Small’s Fourth Amendment challenge. The Fourth Amendment

protects “[t]he right of the people to be secure in their persons, houses, papers, and effects,

against unreasonable searches and seizures.” U.S. Const. amend. IV. To safeguard this

right, courts apply an exclusionary rule, which dictates that “evidence obtained in violation

of the Fourth Amendment cannot be used in a criminal proceeding against the victim of

the illegal search and seizure.” United States v. Calandra, 414 U.S. 338, 347-48 (1974).

Although warrantless searches are generally considered “per se unreasonable under the

Fourth Amendment,” this generality is subject “to a few specifically established and well-

delineated exceptions.” Arizona v. Gant, 556 U.S. 332, 338 (2009) (quoting Katz v. United

States, 389 U.S. 347, 357 (1967)). One such exception is abandonment. Abel v. United

States, 362 U.S. 217, 241 (1960) (“There can be nothing unlawful in the Government’s

appropriation of . . . abandoned property.”); United States v. Leshuk, 65 F.3d 1105, 1111

(4th Cir. 1995) (“The law is well established that a person who voluntarily abandons

                                              17
property . . . is consequently precluded from seeking to suppress evidence seized from the

property.”).

       A finding of abandonment is based “not [on] whether all formal property rights have

been relinquished, but whether the complaining party retains a reasonable expectation of

privacy in the articles alleged to be abandoned.” United States v. Haynie, 637 F.2d 227,

237 (4th Cir. 1980) (quoting United States v. Wilson, 472 F.2d 901, 902 (9th Cir. 1973)).

To determine whether the defendant maintains a reasonable expectation of privacy in an

item, the court performs “an objective analysis” which considers the defendant’s actions

and intentions. United States v. Davis, 657 F. Supp. 2d 630, 647-48 (D. Md. 2009), aff’d,

690 F.3d 226 (4th Cir. 2012). “Intent [to abandon] may be inferred from words spoken,

acts done, and other objective facts.” Id. at 648 (quoting United States v. Hoey, 983 F.2d

890, 892 (8th Cir. 1993)).

                                             B.

       Small contends that the district court erred in denying his motion to suppress the

fruits of the warrantless searches of his cell phone. Specifically, Small alleges that there

was insufficient evidence for the court to conclude that the phone was abandoned and that

no warrant was required for the initial searches.

       In reviewing a district court’s denial of a motion to suppress, we review legal

determinations de novo and factual findings for clear error. United States v. Lull, 824 F.3d

109, 114 (4th Cir. 2016). The government bears the burden of proving the admissibility of

evidence obtained pursuant to a warrantless search by a preponderance of evidence. See



                                             18
United States v. Matlock, 415 U.S. 164, 178 n.14 (1974); United States v. Helms, 703 F.2d

759, 763-64, 766 (4th Cir. 1983).

       In determining whether this standard is met, we may consider both the evidence

before the district court at the suppression hearing and “evidence adduced at trial that

support[ed] the district judge’s ruling.” United States v. Han, 74 F.3d 537, 539 (4th Cir.

1996); see also Carroll v. United States, 267 U.S. 132, 162 (1925). Still, there are temporal

limitations on evidence used in our analysis: we evaluate whether the defendant intended

to abandon an item using only objective information available to officers at the time they

performed the warrantless search. United States v. Nowak, 825 F.3d 946, 948 (8th Cir.

2016) (per curiam); Bond v. United States, 77 F.3d 1009, 1013 (7th Cir. 1996). As the

Supreme Court has noted, the reasonableness of a search is evaluated based on “the facts

known to the police” at the time. United States v. Banks, 540 U.S. 31, 39-40 (2003). A

Fourth Amendment search “is good or bad when it starts.” United States v. Di Re, 332 U.S.

581, 595 (1948).

       Abandonment should not be casually inferred. People lose or misplace their cell

phones all the time. But the simple loss of a cell phone does not entail the loss of a

reasonable expectation of privacy. Thus, such ordinary mishaps do not constitute

“abandonments.” Rather, as the district court noted, “[t]here has to be some voluntary

aspect to the circumstances that lead to the phone being what could be called abandoned.”

J.A. 41. Here there clearly was.

       The evidence before the district court depicts a fleeing suspect tossing aside

personal items while attempting to evade capture. Small fled on foot after crashing through

                                             19
the NSA gates, leaving his vehicle and its contents behind. Search personnel would

continue to find Small’s personal items strewn about during the manhunt. At 1:45 am,

officers located a bloody shirt and hat in the vicinity of the crashed car. The obvious

conclusion is that these items—or, at the very least, the shirt—were purposefully removed

and tossed aside. Several hours later, around 5:00 am, officers located a cell phone only

fifty yards from the shirt and hat. The phone was found in a grassy area, not on a sidewalk

or “a place where [someone] normally might be.” J.A. 43.

       Based on these circumstances, the district court’s inference that Small abandoned

the phone seems sensible. Because a cell phone’s GPS tracking can “lead you to a

defendant,” J.A. 39, it is credible that a fleeing suspect might intentionally discard his

phone. And while phones occasionally slip out of pockets, shirts do not accidentally fall

off their wearers—at the exact same moments as hats—and cars do not ditch themselves

after a crash. The fleeing suspect’s relinquishment of the car, the hat, and the shirt near

where the cell phone was found support the district court’s finding of abandonment.

       The district court relied heavily on these circumstances to reach its conclusion that

Small no longer had a “reasonable expectation of privacy in th[e] phone.” J.A. 42-43. Small

“is fleeing from the police, he crashes through a gate in a place where he is not supposed

to be. He’s clearly left the car. Items are being left behind, the bloody shirt and hat being




                                             20
one of them.” J.A. 42. Further, the court noted that there was no evidence Small attempted

to retrieve his phone at any point, even though it wasn’t password protected. 2

       Evidence gleaned from trial testimony points in the same direction. This testimony

demonstrates why search personnel could reasonably conclude at the time of the search

that the phone belonged to the suspect-at-large. While the government briefly noted at the

suppression hearing that the NSA went on “lockdown” when Small crashed through the

fence, J.A. 27, trial testimony from several search personnel gave a more complete picture

of the scope of the manhunt. The testimony suggests that few people besides the suspect

and search personnel were out-and-about in the hours before the phone was found.

       As trial testimony established, the cell phone was found in a large crime scene, not

in a crowded public area. An Anne Arundel police officer radioed during the car chase for

“aviation assets” and “K-9 assets.” J.A. 74. After Small entered Fort Meade but before he

crashed through the NSA fence, an Army sergeant locked the Fort Meade gates and only

reopened them to allow entry by search personnel. After the crash, an NSA police captain

established a perimeter within the NSA and led a thorough, methodical search for the

suspect. Search personnel could well believe that this phone—located during the early




       2
         Citing Riley v. California, 134 S. Ct. 2473 (2014), Small contends that even if he
abandoned his physical phone, he did not abandon its digital contents. Appellant’s Opening
Br. at 44-45. We do not find this argument persuasive. While Riley held that “the search
incident to arrest exception does not apply to [digital information stored on] cell phones,”
it emphasized that “other case-specific exceptions may still justify a warrantless search of
a particular phone.” 134 S. Ct. at 2493-94. For the reasons noted, this is such a case.

                                            21
morning hours in a grassy area in a facility on lockdown—belonged to the fleeing suspect

who deliberately abandoned it during flight.

       When Small discarded the phone, he ran the risk that complete and total strangers

would come upon it. In tossing his phone, he relinquished his reasonable expectation of

privacy in it as well. The district court’s decision to deny suppression shall be affirmed.

                                             IV.

                                             A.

       The Sixth Amendment guarantees a criminal defendant the right to be tried before

an impartial jury. U.S. Const. amend. VI. In order to safeguard this right, the Supreme

Court has held that “[i]n a criminal case, any private communication, contact, or tampering,

directly or indirectly, with a juror during a trial about the matter pending before the jury

is . . . deemed presumptively prejudicial.” Remmer v. United States, 347 U.S. 227, 229

(1954). If the Remmer presumption is met, the defendant is entitled to an evidentiary

hearing in which the government bears the burden of showing “that such contact . . . was

harmless to the defendant.” Id. at 229-30; Haley v. Blue Ridge Transfer Co., 802 F.2d 1532,

1535 (4th Cir. 1986).

       Because it is difficult to fully shield juries from the outside world, see Smith v.

Phillips, 455 U.S. 209, 217 (1982), we tolerate certain instances of extrajudicial contact

that “amount to nothing more than innocuous interventions that simply could not justify a

presumption of prejudicial effect,” Haley, 802 F.2d at 1537 n.9; see also Stockton v.

Virginia, 852 F.2d 740, 747 (4th Cir. 1988). Thus, in order to trigger Remmer’s

presumption of prejudice, “the defendant must first establish both that an unauthorized

                                             22
contact was made and that it was of such a character as to reasonably draw into question

the integrity of the verdict.” Stockton, 852 F.2d at 743.

       To determine whether a contact was innocuous, we “turn to the [five] factors the

Supreme Court deemed important” in Remmer: “(1) any private communication; (2) any

private contact; (3) any tampering; (4) directly or indirectly with a juror during trial; (5)

about the matter before the jury.” United States v. Cheek, 94 F.3d 136, 141 (4th Cir. 1996).

                                              B.

       The day Small’s trial began, jurors 5 and 11 approached the Courtroom Deputy with

concerns that individuals outside the jury room had been “watching” them when they left

the courthouse the previous evening. J.A. 49. The jurors did not indicate much else. Small

contends that his Sixth Amendment right to an impartial jury was violated by the district

court’s failure to excuse and question jurors 5 and 11. For this reason, he requests that his

convictions be vacated and his case remanded for a new trial.

       We review the district court’s decision not to question or excuse jurors after

allegations of improper contact under “a ‘somewhat narrowed,’ modified abuse of

discretion standard” that allows the appellate court “more latitude to review the trial court’s

conclusion” on the potential for prejudice. Cheek, 94 F.3d at 140 (quoting Haley, 802 F.2d

at 1537 n.11-12); see also United States v. Basham, 561 F.3d 302, 319 (4th Cir. 2009).

       Under this standard, we see nothing problematic about the district court’s denial of

Small’s motion to voir dire and excuse jurors 5 and 11. To invoke the Remmer presumption

and the right to an evidentiary hearing, Small bore the initial burden of “introducing

competent evidence that the extrajudicial communications or contacts were ‘more than

                                              23
innocuous interventions.’” Cheek, 94 F.3d at 141 (quoting Haley, 802 F.2d at 1537 n.9).

He has failed to do so.

       As an initial matter, it is hardly clear that a vague report of “watching,” without

more, constitutes evidence of “extrajudicial communications or contacts,” Cheek, 94 F.3d

at 141; see also United States v. Baptiste, 596 F.3d 214, 220-21 (4th Cir. 2010) (declining

to reach the question of whether stares from a crowd constituted unauthorized contact). We

are unaware of any case where a defendant attempted to invoke the Remmer presumption

based on “watching” alone. “Watching” can hardly be described as “communication” or

“contact,” both of which imply an active exchange of information of some sort.

Unsurprisingly, most precedent discussing extrajudicial contact involves spoken words.

See, e.g., Basham, 561 F.3d at 316, 320 (juror called local news outlets about the trial

before the jury reached a verdict); Stockton, 852 F.2d at 742-43, 746 (local business owner

told the jurors that “they ought to fry the son of a bitch” in a death penalty case). Watching

may be done passively and, unless context indicates otherwise, conveys little information.

       Of course, “watching” may take on an extreme and sinister character, but here there

is no evidence that it was anything “more than [an] innocuous intervention[],” Cheek, 94

F.3d at 141. The episode occurred in a common area of a busy courthouse. There was no

reason for the jurors to associate the unknown individuals with Small. Indeed, there was

no indication that the incident was in any way related to Small’s case, “the matter before

the jury,” Cheek, 94 F.3d at 141.

       “The trial court must be afforded wide discretion in handling matters relating

to . . . the integrity of the jury.” United States v. Johnson, 657 F.2d 604, 606 (4th Cir. 1981).

                                               24
Here the district judge took reasonable steps based on the jurors’ reports. He did not dismiss

or trivialize their concerns. Instead, he increased security around the jury room. Further, he

ensured that jurors 5 and 11 were aware of where to find security personnel, encouraged

them to report any further concerns, and provided clear instructions on how to do so.

       The district judge had good reason to be wary of a more searching inquiry. As he

later noted:

       Stopping a trial to separately voir dire particular jurors about potential
       improper influence has its own potentially deleterious impact. Just that
       questioning process could plant in jurors’ minds the notion that perhaps
       something untoward is afoot. . . . In this case, the totality of the information
       presented to the [c]ourt did not warrant th[is] sort of inquiry . . . .

J.A. 765. We agree. The judge took a measured, thoughtful approach to the jurors’

concerns. These modest steps were proportionate to what the situation required. We find

that the district court did not abuse its discretion by declining to question and excuse jurors

5 and 11.

                                              V.

       For the foregoing reasons, we reject Small’s challenges to the proceedings below

and affirm his convictions.

                                                                                AFFIRMED




                                              25

```

---
