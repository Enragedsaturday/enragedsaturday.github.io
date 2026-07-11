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

## GROUP: _overhaul2/lake/cases/United States v. Salvucci.json  (`lake-record`, 3 assertions)

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
{"assertion_id": "0e0d6321b80b5bed", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Salvucci"}, "payload": {"all": [{"cite": "448 U.S. 83", "page": "83", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "448"}, {"cite": "100 S. Ct. 2547", "page": "2547", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "100"}, {"cite": "65 L. Ed. 2d 619", "page": "619", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "65"}, {"cite": "1980 U.S. LEXIS 141", "page": "141", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1980"}], "display": "448 U.S. 83", "official": {"cite": "448 U.S. 83", "page": "83", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "448"}, "official_selection_present": true, "record_id": "United States v. Salvucci"}}
{"assertion_id": "3d3b2f3bbba4bf2c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-85", "record_id": "United States v. Salvucci"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-85", "pinpoint_status": "slip-only", "quote": "to challenge the search that produced the evidence, without showing that his own Fourth Amendment rights were violated. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "United States v. Salvucci", "star_marker": null}}
{"assertion_id": "1ede9cfeab68a444", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Salvucci"}, "payload": {"as_of_content": "1980-06-25", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Salvucci", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/United States v. Sandoval.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "United States v. Sandoval"
type: case
citation: "200 F.3d 659 (2000)"
parallel_cite: 2000 Daily Journal DAR 907
neutral_cite: "2000 Cal. Daily Op. Serv. 581; 2000 U.S. App. LEXIS 805; 2000 WL 48991"
court: "U.S. Court of Appeals, Ninth Circuit"
court_level: coa
circuit: 9th
year: 2000
date_decided: 2000-01-24
docket: ""
authority_weight: "Binding in-circuit — 9th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2000-01-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Sandoval
  varies_by_point: false
  scope_note: "Circuit split: the 10th Cir. reached a different conclusion in United States v. Ruckman, 806 F.2d 1471."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/767260/united-states-v-rodrigo-sandoval/"
  cluster_id: 767260
  opinion_id: 767260
  identity_checked: true
homes:
  - page: "[[Tents]]"
    role: "Key — Anchor"
related: ["[[Katz v. United States]]", "[[California v. Ciraolo]]", "[[United States v. Gooch]]"]
aliases: ["United States v. Sandoval (9th Cir. 2000)", "United States v. Rodrigo Sandoval"]
tags: ["case", "fourth-amendment", "tents", "expectation-of-privacy", "public-land", "blm", "ninth-circuit"]
holding: "(Persuasive (outside circuit) — 9th Cir.) A reasonable expectation of privacy in a tent on public (BLM) land does not turn on whether the camper had permission to be there; denial of suppression reversed."
lake:
  record_id: United States v. Sandoval
  status: verified
  projected_at: 2026-07-06
---

# United States v. Sandoval

*200 F.3d 659 (9th Cir. 2000)* · U.S. Court of Appeals, Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During a multi-site marijuana-grow investigation in Idaho, federal agents searching a grow on Bureau of Land Management (BLM) land entered a makeshift tent and found a medicine bottle bearing Sandoval's name. The tent was closed on all four sides and sat in heavy vegetation; the bottle could not be seen from outside. Sandoval moved to suppress, arguing the agents entered without a warrant. The district court denied the motion, holding that because the tent was on BLM land, Sandoval had no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]].

## Issue
Whether a camper has a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in a closed tent on public (BLM) land, and whether that expectation depends on whether he had permission to be there.

## Rule
A camper has a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in a closed tent, and that expectation does not turn on whether he had permission to be on the public land. Applying the two-part *[[Katz v. United States|Katz]]* test (subjective expectation society recognizes as reasonable), the court held: "we do not believe the reasonableness of Sandoval's expectation of privacy turns on whether he had permission to camp on public land. Such a distinction would mean that a camper who overstayed his permit in a public campground would lose his Fourth Amendment rights, while his neighbor, whose permit had not expired, would retain those rights." — *United States v. Sandoval*, 200 F.3d 659, 661 (9th Cir. 2000). ^pin-661

## Application
The closed, four-sided tent in dense vegetation, the bottle's invisibility from outside, and Sandoval's leaving a personal prescription bottle inside all showed a subjective expectation of privacy that the government's "illegal activity / no permission" arguments did not defeat. Extending the circuit's tent cases (*[[LaDuke v. Nelson|LaDuke]]* — private property; *[[United States v. Gooch|Gooch]]* — public campground), the court held the expectation objectively reasonable even on BLM land, regardless of permission. The warrantless entry therefore violated the Fourth Amendment.

## Conclusion
The district court erred in denying suppression; the Ninth Circuit reversed Sandoval's conviction and [[Reading and Citing Cases#on-remand|remanded]] for a new trial.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 9th Cir.**
- No negative treatment within the circuit. **Circuit split:** the court noted that the Tenth Circuit reached a different conclusion in *[[United States v. Ruckman]]*, 806 F.2d 1471 (10th Cir. 1986) (no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] for a person occupying a cave on public land). *Sandoval* anchors the rule that a closed tent on public land retains Fourth Amendment protection independent of the camper's permission to be there.

## Appears on
- [[Tents]] — *Key — Anchor*

## Sources
- *United States v. Sandoval*, 200 F.3d 659 (9th Cir. 2000) — https://www.courtlistener.com/opinion/767260/united-states-v-rodrigo-sandoval/ — pinpoint: 661.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bd69b2a4fe3ec8cd", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Sandoval"}, "payload": {"all": [{"cite": "200 F.3d 659", "page": "659", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "200"}, {"cite": "2000 Cal. Daily Op. Serv. 581", "page": "581", "reporter": "Cal. Daily Op. Serv.", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2000"}, {"cite": "2000 Daily Journal DAR 907", "page": "907", "reporter": "Daily Journal DAR", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "2000"}, {"cite": "2000 U.S. App. LEXIS 805", "page": "805", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2000"}, {"cite": "2000 WL 48991", "page": "48991", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2000"}], "display": "200 F.3d 659", "official": {"cite": "200 F.3d 659", "page": "659", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "200"}, "official_selection_present": true, "record_id": "United States v. Sandoval"}}
{"assertion_id": "c68cb0b8fb5aa5c1", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-661", "record_id": "United States v. Sandoval"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-661", "pinpoint_status": "slip-only", "quote": "--- # United States v. Sandoval *200 F.3d 659 (9th Cir. 2000)* · U.S. Court of Appeals, Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background During a multi-site marijuana-grow investigation in Idaho, federal agents searching a grow on Bureau of Land Management (BLM) land entered a makeshift tent and found a medicine bottle bearing Sandoval's name. The tent was closed on all four sides and sat in heavy vegetation; the bottle could not be seen from outside. Sandoval moved to suppress, arguing the agents entered without a warrant. The district court denied the motion, holding that because the tent was on BLM land, Sandoval had no reasonable expectation of privacy. ## Issue Whether a camper has a reasonable expectation of privacy in a closed tent on public (BLM) land, and whether that expectation depends on whether he had permission to be there. ## Rule A camper has a reasonable expectation of privacy in a closed tent, and that expectation does not turn on whether he had permission to be on the public land. Applying the two-part *Katz* test (subjective expectation society recognizes as reasonable), the court held:", "quote_fidelity": "mismatch", "record_id": "United States v. Sandoval", "star_marker": null}}
{"assertion_id": "08f7932d10d43663", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Sandoval"}, "payload": {"as_of_content": "2000-01-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Sandoval", "scope_note": "Circuit split: the 10th Cir. reached a different conclusion in United States v. Ruckman, 806 F.2d 1471.", "varies_by_point": false}}
```

### lake record — United States v. Sandoval

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Sandoval",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Rodrigo Sandoval",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Rodrigo SANDOVAL, Defendant-Appellant",
    "input_case_name": "United States v. Sandoval",
    "court": "U.S. Court of Appeals, Ninth Circuit",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "9th",
    "state": null,
    "date_decided": "2000-01-24",
    "year": 2000,
    "docket": null,
    "cluster_id": 767260,
    "lead_opinion_id": 767260,
    "sibling_ids": [
      767260
    ],
    "absolute_url": "/opinion/767260/united-states-v-rodrigo-sandoval/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "200 F.3d 659",
      "volume": "200",
      "reporter": "F.3d",
      "page": "659",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "2000 Daily Journal DAR 907",
        "volume": "2000",
        "reporter": "Daily Journal DAR",
        "page": "907",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2000 Cal. Daily Op. Serv. 581",
        "volume": "2000",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "581",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 U.S. App. LEXIS 805",
        "volume": "2000",
        "reporter": "U.S. App. LEXIS",
        "page": "805",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 WL 48991",
        "volume": "2000",
        "reporter": "WL",
        "page": "48991",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "200 F.3d 659",
        "volume": "200",
        "reporter": "F.3d",
        "page": "659",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 Cal. Daily Op. Serv. 581",
        "volume": "2000",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "581",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 Daily Journal DAR 907",
        "volume": "2000",
        "reporter": "Daily Journal DAR",
        "page": "907",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 U.S. App. LEXIS 805",
        "volume": "2000",
        "reporter": "U.S. App. LEXIS",
        "page": "805",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 WL 48991",
        "volume": "2000",
        "reporter": "WL",
        "page": "48991",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "200 F.3d 659",
    "official_selection": {
      "court_class": "coa",
      "selected": "200 F.3d 659",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-661",
      "page": null,
      "quote": "--- # United States v. Sandoval *200 F.3d 659 (9th Cir. 2000)* \u00b7 U.S. Court of Appeals, Ninth Circuit \u00b7 **Binding in-circuit \u2014 9th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background During a multi-site marijuana-grow investigation in Idaho, federal agents searching a grow on Bureau of Land Management (BLM) land entered a makeshift tent and found a medicine bottle bearing Sandoval's name. The tent was closed on all four sides and sat in heavy vegetation; the bottle could not be seen from outside. Sandoval moved to suppress, arguing the agents entered without a warrant. The district court denied the motion, holding that because the tent was on BLM land, Sandoval had no reasonable expectation of privacy. ## Issue Whether a camper has a reasonable expectation of privacy in a closed tent on public (BLM) land, and whether that expectation depends on whether he had permission to be there. ## Rule A camper has a reasonable expectation of privacy in a closed tent, and that expectation does not turn on whether he had permission to be on the public land. Applying the two-part *Katz* test (subjective expectation society recognizes as reasonable), the court held:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2000-01-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Sandoval",
    "varies_by_point": false,
    "scope_note": "Circuit split: the 10th Cir. reached a different conclusion in United States v. Ruckman, 806 F.2d 1471.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Sandoval:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America, State of California, Intervenor v. Raphyal Crawford, AKA Aarmyl Crawford",
          "cluster_id": 786677,
          "cite": [
            "372 F.3d 1048",
            "2004 U.S. App. LEXIS 12116",
            "2004 WL 1375521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Piedad Barajas-Avalos, AKA Piedad Barajas-Avaslos",
          "cluster_id": 787179,
          "cite": [
            "377 F.3d 1040",
            "2004 U.S. App. LEXIS 15362",
            "2004 WL 1656517"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whiting v. State",
          "cluster_id": 1479286,
          "cite": [
            "885 A.2d 785",
            "389 Md. 334",
            "2005 Md. LEXIS 643"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raphyal Crawford",
          "cluster_id": 781330,
          "cite": [
            "323 F.3d 700",
            "2003 WL 735531"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hughston",
          "cluster_id": 2285590,
          "cite": [
            "168 Cal. App. 4th 1062",
            "85 Cal. Rptr. 3d 890",
            "2008 Cal. App. LEXIS 2361"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Nishi",
          "cluster_id": 5811207,
          "cite": [
            "207 Cal. App. 4th 954",
            "143 Cal. Rptr. 3d 882",
            "2012 WL 2870591",
            "2012 Cal. App. LEXIS 806"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Linton",
          "cluster_id": 2209670,
          "cite": [
            "812 A.2d 382",
            "356 N.J. Super. 255"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leora Price v. Frank Vance Turner El Dorado County",
          "cluster_id": 774483,
          "cite": [
            "260 F.3d 1144",
            "2001 Cal. Daily Op. Serv. 7031",
            "2001 Daily Journal DAR 8607",
            "2001 U.S. App. LEXIS 18314",
            "2001 WL 909299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Naranjibhai Patel v. City of Los Angeles",
          "cluster_id": 2647586,
          "cite": [
            "738 F.3d 1058",
            "2013 WL 6768090",
            "2013 U.S. App. LEXIS 25609"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dellas",
          "cluster_id": 2453315,
          "cite": [
            "355 F. Supp. 2d 1095",
            "2005 U.S. Dist. LEXIS 1882",
            "2005 WL 310398"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Slavin",
          "cluster_id": 3145304,
          "cite": [
            "2011 IL App (2d) 100764"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State Of Washington v. William R. Pippin",
          "cluster_id": 4433202,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Slavin",
          "cluster_id": 2437214,
          "cite": [
            "964 N.E.2d 150",
            "357 Ill. Dec. 787"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sandoval:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(767260) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca9)",
        "reviewed": 5,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 5,
        "triage_read": 1,
        "triage_snippet_classified": 4
      },
      "lane2_top_cited": {
        "query": "cites:(767260)",
        "reviewed": 15,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 14,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(767260)",
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
    "complete_query": "cites:(767260)",
    "indexed_citing_opinions": 15,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 767260,
        "count": 15,
        "count_source": "search"
      }
    ],
    "citation_count": 27,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-sandoval.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 15,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 767260,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 767260,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 767260,
        "cited_id": 452994,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 767260,
        "cited_id": 480405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 767260,
        "cited_id": 654273,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 767260,
        "cited_id": 744560,
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
    "date_created": "2026-07-06T02:48:44Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:50:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:50:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:52:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:50:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Sandoval

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b698-4">
  MICHAEL DALY HAWKINS, Circuit Judge:
 </author>
<p id="b698-5">
  Rodrigo Sandoval appeals his conviction on drug and conspiracy charges, alleging that the district court erred in denying his motion to suppress evidence obtained during the search of a tent. Because we agree that the district court erred in denying Sandoval’s motion, we reverse his conviction and remand for a new trial.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b698-6">
  In early 1997, state and federal officials began an investigation into marijuana growing in Idaho that led to the seizure of marijuana from sixteen growing sites (“grows”) and the indictment of 18 defendants, including Sandoval. During the seizure of one of the grows, which was located on Bureau of Land Management (“BLM”) land, federal agents entered a makeshift tent and found a medicine bottle bearing Sandoval’s name. The tent was closed on all four sides, and the bottle could not be seen from outside. Before trial, Sandoval filed a motion to suppress, alleging that agents had entered the tent without a search warrant and that the evidence was therefore inadmissible. The district court denied the motion, holding that because the tent was on BLM land, Sandoval did not have a reasonable expectation of privacy. Therefore, the court concluded, a search warrant was not required, and the evidence was admissible.
 </p>
<p id="b698-7">
  We review de novo the district court’s denial of a motion to suppress.
  <em>
   See United States v. Kemmish,
  </em>
  <span class="citation" data-id="6952928"><a href="/opinion/7049571/united-states-v-kemmish/#939" aria-description="Citation for case: United States v. Kemmish">120 F.3d 937, 939</a></span> (9th Cir.1997). We review the trial court’s factual findings for clear error.
  <em>
   See <span class="citation" data-id="6952928"><a href="/opinion/7049571/united-states-v-kemmish/" aria-description="Citation for case: United States v. Kemmish">id.</a></span>
  </em>
</p>
<p id="b698-8">
  To determine whether a warrant-less search violates the Fourth Amendment, we must ask two questions: “[Fjirst, has the individual manifested a subjective expectation of privacy in the object of the challenged search? Second, is society willing to recognize that expectation as reasonable?”
  <em>
   California v. Ciraolo,
  </em>
  <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#211" aria-description="Citation for case: California v. Ciraolo">476 U.S. 207, 211</a></span>, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">106 S.Ct. 1809</a></span>, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">90 L.Ed.2d 210</a></span> (1986) (citing
  <em>
   Katz v. United States,
  </em>
  <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States">389 U.S. 347, 360-61</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L.Ed.2d 576</a></span> (1967) (Harlan, J., concurring)). Only if both the subjective and objective tests are met can we find that a Fourth Amendment interest has been violated.
 </p>
<p id="b698-12">
  In this case, several factors indicate that Sandoval had a subjective expectation of privacy. First, the tent was located in an area that was heavily covered by vegetation and virtually impenetrable. Second, the makeshift tent was closed on all four sides, and the bottle could not be seen from outside. Third, Sandoval left a prescription medicine bottle inside the tent; a person who lacked a subjective expectation of privacy would likely not leave such an item lying around. The government counters that Sandoval could not have had a subjective expectation of privacy because he was growing marijuana illegally and was not authorized to camp on BLM land. However, we have previously rejected the argument that a person lacks a subjective expectation of privacy simply because he is engaged in illegal activity or could have expected the police to intrude on his privacy.
  <em>
   See United States v. Gooch,
  </em>
  <span class="citation" data-id="9485948"><a href="/opinion/654273/united-states-v-kenneth-d-gooch/#677" aria-description="Citation for case: United States v. Kenneth D. Gooch">6 F.3d 673, 677</a></span> (9th Cir.1993). “According to this view, no lawbreaker would have a subjective expectation of privacy in any place because the expectation of arrest is always imminent.”
  <em>
   <span class="citation" data-id="9485948"><a href="/opinion/654273/united-states-v-kenneth-d-gooch/" aria-description="Citation for case: United States v. Kenneth D. Gooch">Id.</a></span>
  </em>
</p>
<p id="b698-13">
  Sandoval’s expectation of privacy was also objectively reasonable. In
  <em>
   LaDuke v. Nelson,
  </em>
  <span class="citation" data-id="452994"><a href="/opinion/452994/charles-laduke-v-alan-c-nelson-etc/" aria-description="Citation for case: Charles Laduke v. Alan C. Nelson, Etc.">762 F.2d 1318</a></span>, 1326 n. 11, 1332 n. 19 (9th Cir.1985), we held that a person can have an objectively reasonable expectation of privacy in a tent on private property. In
  <em>
   Gooch,
  </em>
  <span class="citation" data-id="9485948"><a href="/opinion/654273/united-states-v-kenneth-d-gooch/#677" aria-description="Citation for case: United States v. Kenneth D. Gooch">6 F.3d at 677</a></span>, we extended that holding to find a reasonable expectation of privacy in a tent on a public campground. Here, the tent was
  <span citation-index="1" class="star-pagination" label="661"> 
   *661
   </span>
  located on BLM land, not on a public campground, and it is unclear whether Sandoval had permission to be there.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  However, we do not believe the reasonableness of Sandoval’s expectation of privacy turns on whether he had permission to camp on public land.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  Such a distinction would mean that a camper who overstayed his permit in a public campground would lose his Fourth Amendment rights, while his neighbor, whose permit had not expired, would retain those rights.
 </p>
<p id="b699-4">
  We note that in
  <em>
   Zimmerman v. Bishop Estate,
  </em>
  <span class="citation" data-id="6930933"><a href="/opinion/7029033/zimmerman-v-bishop-estate/#787" aria-description="Citation for case: Zimmerman v. Bishop Estate">25 F.3d 784, 787-88</a></span> (9th Cir.1994), this court held that a squatter in a residential home did not have an objectively reasonable expectation of privacy because he had no legal right to occupy the home. However, we find
  <em>
   <span class="citation" data-id="6930933"><a href="/opinion/7029033/zimmerman-v-bishop-estate/" aria-description="Citation for case: Zimmerman v. Bishop Estate">Zimmerman</a></span>
  </em>
  distinguishable on two grounds. First, camping on public land, even without permission, is far different from squatting in a private residence. A private residence is easily identifiable and clearly off-limits, whereas public land is often unmarked and may appear to be open to camping. Thus, we think it much more likely that society would recognize an expectation of privacy for the camper on public land than for the squatter in a private residence.
 </p>
<p id="b699-5">
  Second, the facts of
  <em>
   <span class="citation" data-id="6930933"><a href="/opinion/7029033/zimmerman-v-bishop-estate/" aria-description="Citation for case: Zimmerman v. Bishop Estate">Zimmerman</a></span>
  </em>
  contrast starkly with the facts presented here. In
  <em>
   <span class="citation" data-id="6930933"><a href="/opinion/7029033/zimmerman-v-bishop-estate/" aria-description="Citation for case: Zimmerman v. Bishop Estate">Zimmerman</a></span>,
  </em>
  the appellants were asked on several occasions over the course of eight months to vacate the premises, and there was “no dispute of material fact regarding the ownership of the property or whether the [owners] acquiesced in the presence of the [appellants].”
  <span class="citation" data-id="6930933"><a href="/opinion/7029033/zimmerman-v-bishop-estate/#788" aria-description="Citation for case: Zimmerman v. Bishop Estate"><em>
   Id.
  </em>
  at 788</a></span>. By contrast, though Sandoval did not obtain permission to camp on BLM land, he was never instructed to vacate or risk eviction, and the record does not establish any applicable rules, regulations or practices concerning recreational or other use of BLM land. Indeed, whether Sandoval was legally permitted to be on the land was a matter in dispute.
 </p>
<p id="b699-10">
  Because Sandoval had a subjective expectation of privacy and because that expectation was objectively reasonable, we conclude that the district court erred in denying Sandoval’s motion to suppress. His conviction is REVERSED, and the case is REMANDED for a new trial.
 </p>



<div class="footnotes"><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b698-9">
   . Sandoval makes several other claims that we have addressed in a separate, unpublished memorandum disposition filed contemporaneously herewith.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b699-6">
   . The district court assumed that Sandoval lacked authority to erect a tent on BLM land. However, it is unclear whether explicit permission was required.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b699-17">
   . The Tenth Circuit reached a different conclusion in
   <em>
    United States v. Ruckman,
   </em>
   <span class="citation" data-id="9475634"><a href="/opinion/480405/united-states-v-frank-william-ruckman/#1472" aria-description="Citation for case: United States v. Frank William Ruckman">806 F.2d 1471, 1472-73</a></span> (10th Cir.1986). However, we find Judge McKay's dissent in that case more persuasive.
   <span class="citation" data-id="9475634"><a href="/opinion/480405/united-states-v-frank-william-ruckman/#1475" aria-description="Citation for case: United States v. Frank William Ruckman"><em>
    See id.
   </em>
   at 1475-79</a></span> (McKay, J., dissenting).
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Santana.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Santana"
type: case
citation: "427 U.S. 38 (1976)"
parallel_cite: "96 S. Ct. 2406; 49 L. Ed. 2d 300"
neutral_cite: 1976 U.S. LEXIS 71
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-06-24
docket: 75-19
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-06-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Santana
  varies_by_point: false
  scope_note: "Hot-pursuit reading for misdemeanor pursuits limited by Lange v. California (2021) — no longer categorical; the threshold/public-place and felony hot-pursuit holdings are intact."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109504/united-states-v-santana/"
  cluster_id: 109504
  opinion_id: 109504
  identity_checked: true
homes:
  - page: "[[Arrest in the Home]]"
    role: "Key — Anchor"
  - page: "[[Exigent Circumstances and Hot Pursuit]]"
    role: "Key — Anchor"
  - page: "[[Curtilage]]"
    role: "Related — threshold/public-place line"
related: ["[[United States v. Watson]]", "[[Payton v. New York]]", "[[Lange v. California]]", "[[Hester v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest-in-the-home", "hot-pursuit", "exigent-circumstances", "doorway", "public-place"]
holding: "A suspect standing in her own doorway/threshold is in a 'public' place for Fourth Amendment purposes; she cannot defeat a lawful arrest…"
lake:
  record_id: United States v. Santana
  status: verified
  projected_at: 2026-07-06
---

# United States v. Santana

*427 U.S. 38 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After an undercover officer's controlled heroin buy through an intermediary who took marked money to "Mom Santana's" house, officers arrested the intermediary (who said "Mom has the money") and drove to Santana's house. They saw Santana standing in her doorway holding a brown paper bag, pulled up, got out shouting "police," and displayed identification. Santana retreated into the vestibule; the officers followed through the open door, caught her, and heroin packets fell from the bag. Marked money was found on her. The District Court suppressed the evidence; the Government appealed.

## Issue
Whether police with probable cause may make a warrantless arrest of a suspect standing in her doorway, and whether they may follow her into the house when she retreats, on a hot-pursuit theory.

## Rule
A suspect standing in her own doorway is in a "public" place for arrest purposes: "While it may be true that under the common law of property the threshold of one's dwelling is 'private,' . . . it is nonetheless clear that under the cases interpreting the Fourth Amendment Santana was in a 'public' place. She was not in an area where she had any expectation of privacy. . . . She was not merely visible to the public but was as exposed to public view, speech, hearing, and touch as if she had been standing completely outside her house." — 427 U.S. at 42. ^pin-42

And a suspect cannot defeat a lawful public arrest by retreating indoors; [[Exigent Circumstances and Hot Pursuit|hot pursuit]] justifies the warrantless entry: "We thus conclude that a suspect may not defeat an arrest which has been set in motion in a public place, and is therefore proper under *Watson*, by the expedient of escaping to a private place." — 427 U.S. at 43. ^pin-43

## Application
Santana was standing in her open doorway with the bag when officers who had probable cause approached to arrest her; she was therefore in a public place and the arrest was proper under [[United States v. Watson]]. When she retreated into the vestibule, the officers' immediate pursuit was a true [[Exigent Circumstances and Hot Pursuit|hot pursuit]] that justified the warrantless entry. The heroin that fell from the bag and the marked money found on her were lawfully seized incident to that arrest.

## Conclusion
The warrantless entry and arrest were valid; the Supreme Court reversed the suppression order.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Santana* establishes the doorway-as-public-place rule and the hot-pursuit entry. [[Payton v. New York]] (1980) later held that a warrantless arrest **inside** the home requires a warrant absent [[Exigent Circumstances and Hot Pursuit|exigency]], and [[Lange v. California]] (2021) held that pursuit of a fleeing **misdemeanant** is not a categorical [[Exigent Circumstances and Hot Pursuit|exigency]] — but neither disturbs *Santana*'s threshold/felony hot-pursuit holding.

## Appears on
- [[Arrest in the Home]] — *Key — Anchor*
- [[Exigent Circumstances and Hot Pursuit]] — *Key — Anchor*

## Sources
- *United States v. Santana*, 427 U.S. 38 (1976) — https://www.courtlistener.com/opinion/109504/united-states-v-santana/ — pinpoints: 42, 43 (parallel 96 S. Ct. 2406).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b36b4a58496185de", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Santana"}, "payload": {"all": [{"cite": "427 U.S. 38", "page": "38", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "427"}, {"cite": "96 S. Ct. 2406", "page": "2406", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "96"}, {"cite": "49 L. Ed. 2d 300", "page": "300", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "49"}, {"cite": "1976 U.S. LEXIS 71", "page": "71", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1976"}], "display": "427 U.S. 38", "official": {"cite": "427 U.S. 38", "page": "38", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "427"}, "official_selection_present": true, "record_id": "United States v. Santana"}}
{"assertion_id": "745af473a8223efb", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-42", "record_id": "United States v. Santana"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-42", "pinpoint_status": "slip-only", "quote": "and displayed identification. Santana retreated into the vestibule; the officers followed through the open door, caught her, and heroin packets fell from the bag. Marked money was found on her. The District Court suppressed the evidence; the Government appealed. ## Issue Whether police with probable cause may make a warrantless arrest of a suspect standing in her doorway, and whether they may follow her into the house when she retreats, on a hot-pursuit theory. ## Rule A suspect standing in her own doorway is in a", "quote_fidelity": "mismatch", "record_id": "United States v. Santana", "star_marker": null}}
{"assertion_id": "b5412068a6dc4376", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-43", "record_id": "United States v. Santana"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-43", "pinpoint_status": "slip-only", "quote": "We thus conclude that a suspect may not defeat an arrest which has been set in motion in a public place, and is therefore proper under *Watson*, by the expedient of escaping to a private place.", "quote_fidelity": "mismatch", "record_id": "United States v. Santana", "star_marker": null}}
{"assertion_id": "f68d2c13d5134315", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Santana"}, "payload": {"as_of_content": "1976-06-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Santana", "scope_note": "Hot-pursuit reading for misdemeanor pursuits limited by Lange v. California (2021) — no longer categorical; the threshold/public-place and felony hot-pursuit holdings are intact.", "varies_by_point": false}}
```

### lake record — United States v. Santana

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Santana",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Santana",
    "case_name_short": "Santana",
    "case_name_full": "UNITED STATES v. SANTANA Et Al.",
    "input_case_name": "United States v. Santana",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-06-24",
    "year": 1976,
    "docket": "75-19",
    "cluster_id": 109504,
    "lead_opinion_id": 109504,
    "sibling_ids": [
      109504,
      9426490,
      9426491,
      9426492,
      9426493
    ],
    "absolute_url": "/opinion/109504/united-states-v-santana/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "427 U.S. 38",
      "volume": "427",
      "reporter": "U.S.",
      "page": "38",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 2406",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "2406",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 300",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "300",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 71",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "71",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "427 U.S. 38",
        "volume": "427",
        "reporter": "U.S.",
        "page": "38",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 2406",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "2406",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 300",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "300",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 71",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "71",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "427 U.S. 38",
    "official_selection": {
      "court_class": "scotus",
      "selected": "427 U.S. 38",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-42",
      "page": null,
      "quote": "and displayed identification. Santana retreated into the vestibule; the officers followed through the open door, caught her, and heroin packets fell from the bag. Marked money was found on her. The District Court suppressed the evidence; the Government appealed. ## Issue Whether police with probable cause may make a warrantless arrest of a suspect standing in her doorway, and whether they may follow her into the house when she retreats, on a hot-pursuit theory. ## Rule A suspect standing in her own doorway is in a",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-43",
      "page": null,
      "quote": "We thus conclude that a suspect may not defeat an arrest which has been set in motion in a public place, and is therefore proper under *Watson*, by the expedient of escaping to a private place.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-06-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Santana",
    "varies_by_point": false,
    "scope_note": "Hot-pursuit reading for misdemeanor pursuits limited by Lange v. California (2021) \u2014 no longer categorical; the threshold/public-place and felony hot-pursuit holdings are intact.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Santana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Martin",
          "cluster_id": 4406527,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Paul Allen Decker v. State of Indiana",
          "cluster_id": 2745993,
          "cite": [
            "19 N.E.3d 368",
            "2014 Ind. App. LEXIS 515",
            "2014 WL 5461790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Lujano",
          "cluster_id": 2721019,
          "cite": [
            "229 Cal. App. 4th 175",
            "2014 D.A.R. 11",
            "176 Cal. Rptr. 3d 534",
            "2014 Cal. App. LEXIS 771"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fadul",
          "cluster_id": 7306139,
          "cite": [
            "16 F. Supp. 3d 270",
            "2014 WL 1584044"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Hogan v. City of Corpus Christi, Texas",
          "cluster_id": 1033766,
          "cite": [
            "722 F.3d 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Agbodjan",
          "cluster_id": 8716573,
          "cite": [
            "871 F. Supp. 2d 95",
            "2012 WL 2552140"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Finnicum",
          "cluster_id": 890584,
          "cite": [
            "206 P.3d 501",
            "147 Idaho 137",
            "2009 Ida. App. LEXIS 35"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Delaware v. Prouse",
          "cluster_id": 110045,
          "cite": [
            "59 L. Ed. 2d 660",
            "99 S. Ct. 1391",
            "440 U.S. 648",
            "1979 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
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
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martinez-Fuerte",
          "cluster_id": 109541,
          "cite": [
            "49 L. Ed. 2d 1116",
            "96 S. Ct. 3074",
            "428 U.S. 543",
            "1976 U.S. LEXIS 87"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
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
        "journal_ref": "United States v. Santana:lane2_top_cited"
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
        "journal_ref": "United States v. Santana:lane2_top_cited"
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
        "journal_ref": "United States v. Santana:lane2_top_cited"
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
        "journal_ref": "United States v. Santana:lane2_top_cited"
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
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ledesma",
          "cluster_id": 1228080,
          "cite": [
            "729 P.2d 839",
            "43 Cal. 3d 171",
            "233 Cal. Rptr. 404",
            "1987 Cal. LEXIS 278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
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
        "journal_ref": "United States v. Santana:lane2_top_cited"
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
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ramsey",
          "cluster_id": 109675,
          "cite": [
            "52 L. Ed. 2d 617",
            "97 S. Ct. 1972",
            "431 U.S. 606",
            "1977 U.S. LEXIS 101"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stanton v. Sims",
          "cluster_id": 2641101,
          "cite": [
            "187 L. Ed. 2d 341",
            "134 S. Ct. 3",
            "2013 U.S. LEXIS 7773",
            "82 U.S.L.W. 4003",
            "571 U.S. 3",
            "24 Fla. L. Weekly Fed. S 473",
            "2013 WL 5878007"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Henning",
          "cluster_id": 1060855,
          "cite": [
            "975 S.W.2d 290",
            "1998 Tenn. LEXIS 370",
            "1998 WL 324318"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
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
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chew v. Gates",
          "cluster_id": 7029311,
          "cite": [
            "27 F.3d 1432",
            "94 Cal. Daily Op. Serv. 4853",
            "94 Daily Journal DAR 9043",
            "1994 U.S. App. LEXIS 16020",
            "1994 WL 280292"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James N. Gramenos v. Jewel Companies, Inc.",
          "cluster_id": 474259,
          "cite": [
            "797 F.2d 432"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Louis Lalonde v. County of Riverside, Robert Moquin, and Jason Horton, Opinion",
          "cluster_id": 767803,
          "cite": [
            "204 F.3d 947",
            "2000 Daily Journal DAR 2031",
            "2000 Cal. Daily Op. Serv. 1433",
            "2000 U.S. App. LEXIS 2778",
            "2000 WL 217552"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Frierson",
          "cluster_id": 1434797,
          "cite": [
            "599 P.2d 587",
            "25 Cal. 3d 142",
            "158 Cal. Rptr. 281",
            "1979 Cal. LEXIS 302"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Francisco Sangineto-Miranda, (87-5667) Luray Betts, (87-5668) Enrique Vargas, (87-5711) & Benjamin Nelson, (87-5712)",
          "cluster_id": 513263,
          "cite": [
            "859 F.2d 1501"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Joe Whitten, John Elmer Gaiefsky, Jack Wayne Gish, Richard Lawrence Shimel",
          "cluster_id": 418069,
          "cite": [
            "706 F.2d 1000",
            "13 Fed. R. Serv. 384",
            "1983 U.S. App. LEXIS 27369"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Davis",
          "cluster_id": 1142777,
          "cite": [
            "666 P.2d 802",
            "295 Or. 227",
            "1983 Ore. LEXIS 1342"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Troy Cooper v. C. J. Fitzharris",
          "cluster_id": 360922,
          "cite": [
            "586 F.2d 1325",
            "1978 U.S. App. LEXIS 7347"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gutierrez v. Luna County",
          "cluster_id": 4321034,
          "cite": [
            "841 F.3d 895",
            "96 Fed. R. Serv. 3d 126",
            "2016 U.S. App. LEXIS 20466",
            "2016 WL 6694533"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Santana:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109504 OR 9426490 OR 9426491 OR 9426492 OR 9426493) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTgwMDUxMjAwMDAwJnM9Mjk3NTMzNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109504+OR+9426490+OR+9426491+OR+9426492+OR+9426493%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109504 OR 9426490 OR 9426491 OR 9426492 OR 9426493)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzAmcz0xODgxNDk2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109504+OR+9426490+OR+9426491+OR+9426492+OR+9426493%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109504 OR 9426490 OR 9426491 OR 9426492 OR 9426493)",
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
    "complete_query": "cites:(109504 OR 9426490 OR 9426491 OR 9426492 OR 9426493)",
    "indexed_citing_opinions": 871,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109504,
        "count": 774,
        "count_source": "search"
      },
      {
        "opinion_id": 9426490,
        "count": 113,
        "count_source": "search"
      },
      {
        "opinion_id": 9426491,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426492,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426493,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1384,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-santana.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyNDA2NjYmcz05Mzk1NjYwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109504+OR+9426490+OR+9426491+OR+9426492+OR+9426493%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109504,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 106850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 108135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 108605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 108713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109504,
        "cited_id": 109186,
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
    "date_created": "2026-07-06T02:52:01Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:52:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:52:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:59:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:52:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Santana

```
<div>
<center><b><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">427 U.S. 38</a></span> (1976)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
SANTANA ET AL.</h1></center>
<center>No. 75-19.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued April 27, 1976.</center>
<center>Decided June 24, 1976.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE THIRD CIRCUIT.
<p><span class="star-pagination">*39</span> <i>Frank H. Easterbrook</i> argued the cause for the United States <i>pro hac vice.</i> With him on the brief were <i>Solicitor General Bork, Assistant Attorney General Thornburgh, Deputy Solicitor General Frey,</i> and <i>Peter M. Shannon, Jr.</i></p>
<p><i>Dennis H. Eisman</i> argued the cause for respondent Santana. With him on the brief was <i>Gerald A. Stein.</i><sup>[*]</sup></p>
<p>MR. JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p></p>
<h2>I</h2>
<p>On August 16, 1974, Michael Gilletti, an undercover officer with the Philadelphia Narcotics Squad arranged a heroin "buy" with one Patricia McCafferty (from whom he had purchased narcotics before). McCafferty told him it would cost $115 "and we will go down to Mom Santana's for the dope."</p>
<p>Gilletti notified his superiors of the impending transaction, recorded the serial numbers of $110 (<i>sic</i>) in marked bills, and went to meet McCafferty at a prearranged location. She got in his car and directed him to drive to 2311 North Fifth Street, which, as she had <span class="star-pagination">*40</span> previously informed him, was respondent Santana's residence.</p>
<p>McCafferty took the money and went inside the house, stopping briefly to speak to respondent Alejandro who was sitting on the front steps. She came out shortly afterwards and got into the car. Gilletti asked for the heroin; she thereupon extracted from her bra several glassine envelopes containing a brownish-white powder and gave them to him.</p>
<p>Gilletti then stopped the car, displayed his badge, and placed McCafferty under arrest. He told her that the police were going back to 2311 North Fifth Street and that he wanted to know where the money was. She said, "Mom has the money." At this point Sergeant Pruitt and other officers came up to the car. Gilletti showed them the envelope and said "Mom Santana has the money." Gilletti then took McCafferty to the police station.</p>
<p>Pruitt and the others then drove approximately two blocks back to 2311 North Fifth Street. They saw Santana standing in the doorway of the house<sup>[1]</sup> with a brown paper bag in her hand. They pulled up to within 15 feet of Santana and got out of their van, shouting "police," and displaying their identification. As the officers approached, Santana retreated into the vestibule of her house.</p>
<p>The officers followed through the open door, catching her in the vestibule. As she tried to pull away, the bag tilted and "two bundles of glazed paper packets with a white powder" fell to the floor. Respondent <span class="star-pagination">*41</span> Alejandro tried to make off with the dropped envelopes but was forcibly restrained. When Santana was told to empty her pockets she produced $135, $70 of which could be identified as Gilletti's marked money. The white powder in the bag was later determined to be heroin.</p>
<p>An indictment was filed in the United States District Court for the Eastern District of Pennsylvania charging McCafferty with distribution of heroin, in violation of <span class="citation no-link">21 U. S. C. § 841</span>, and respondents with possession of heroin with intent to distribute in violation of the same section. McCafferty pleaded guilty. Santana and Alejandro moved to suppress the heroin and money found during and after their arrests.</p>
<p>The District Court granted respondents' motion.<sup>[2]</sup> In an oral opinion the court found that "[t]here was strong probable cause that Defendant Santana had participated in the transaction with Defendant McCafferty." However, the court continued:</p>
<blockquote>"One of the police officers . . . testified that the mission was to arrest Defendant Santana. Another police officer testified that the mission was to recover the bait money. Either one would require a warrant, one a warrant of arrest under ordinary circumstances and one a search warrant."</blockquote>
<p>The court further held that Santana's "reentry from the doorway into the house" did not support allowing the police to make a warrantless entry into the house on the grounds of "hot pursuit," because it took "hot pursuit" to mean "a chase in and about public streets." The court did find, however, that the police <span class="star-pagination">*42</span> acted under "extreme emergency" conditions. The Court of Appeals affirmed this decision without opinion.</p>
<p></p>
<h2>II</h2>
<p>In <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976), we held that the warrantless arrest of an individual in a public place upon probable cause did not violate the Fourth Amendment. Thus the first question we must decide is whether, when the police first sought to arrest Santana, she was in a public place.</p>
<p>While it may be true that under the common law of property the threshold of one's dwelling is "private," as is the yard surrounding the house, it is nonetheless clear that under the cases interpreting the Fourth Amendment Santana was in a "public" place. She was not in an area where she had any expectation of privacy. "What a person knowingly exposes to the public, even in his own house or office, is not a subject of Fourth Amendment protection." <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967). She was not merely visible to the public but was as exposed to public view, speech, hearing, and touch as if she had been standing completely outside her house. <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#59" aria-description="Citation for case: Hester v. United States">265 U. S. 57, 59</a></span> (1924). Thus, when the police, who concededly had probable cause to do so, sought to arrest her, they merely intended to perform a function which we have approved in <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span>.</i></p>
<p>The only remaining question is whether her act of retreating into her house could thwart an otherwise proper arrest. We hold that it could not. In <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967), we recognized the right of police, who had probable cause to believe that an armed robber had entered a house a few minutes before, to make a warrantless entry to arrest the robber and to search for weapons. This case, involving a true "hot <span class="star-pagination">*43</span> pursuit,"<sup>[3]</sup> is clearly governed by <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Warden</a></span>;</i> the need to act quickly here is even greater than in that case while the intrusion is much less. The District Court was correct in concluding that "hot pursuit" means some sort of a chase, but it need not be an extended hue and cry "in and about [the] public streets." The fact that the pursuit here ended almost as soon as it began did not render it any the less a "hot pursuit" sufficient to justify the warrantless entry into Santana's house. Once Santana saw the police, there was likewise a realistic expectation that any delay would result in destruction of evidence. See <i>Vale</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#35" aria-description="Citation for case: Vale v. Louisiana">399 U. S. 30, 35</a></span> (1970). Once she had been arrested the search, incident to that arrest, which produced the drugs and money was clearly justified. <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973); <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 762-763</a></span> (1969).</p>
<p>We thus conclude that a suspect may not defeat an arrest which has been set in motion in a public place, and is therefore proper under <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span>,</i> by the expedient of escaping to a private place. The judgment of the Court of Appeals is</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE WHITE, concurring.</p>
<p>It is not disputed here that the officers had probable cause to arrest Santana and to believe that she was in the house. In these circumstances, a warrant was not required to enter the house to make the arrest, at least <span class="star-pagination">*44</span> where entry by force was not required. This has been the longstanding statutory or judicial rule in the majority of jurisdictions in the United States, see ALI, A Model Code of Pre-arraignment Procedure 306-314, 696-697 (1975), and has been deemed consistent with state constitutions, as well as the Fourth Amendment. It is also the Institute's recommended rule. <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Id.,</a></span></i> § 120.6. I agree with the Court that the arrest here did not violate the Fourth Amendment.</p>
<p>My Brother MARSHALL, <i>post,</i> p. 45, and <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#433" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 433</a></span> (1976) (dissenting opinion), would reinterpret the Fourth Amendment to sweep aside this widely held rule and to establish a constitutional standard requiring warrants for arrests except where exigent circumstances clearly exist. The States are, of course, free to limit warrantless arrests, as is Congress; but I would not impose his suggested nationwide edict, founded as it is on a belief in the superior wisdom of the Members of this Court and their power to divine that the country's practice to this date with respect to arrests is unreasonable within the meaning of the Fourth Amendment.</p>
<p>MR. JUSTICE STEVENS, with whom MR. JUSTICE STEWART joins, concurring.</p>
<p>When Officer Gilletti placed McCafferty under arrest, the police had sufficient information to obtain a warrant for the arrest of Santana in her home. It is therefore important to note that their failure to obtain a warrant at that juncture was both (a) a justifiable police decision, and (b) even if not justifiable, harmless.</p>
<p>The decision was justified by the significant risk that the marked money would no longer be in Santana's possession if the police waited until a warrant could be obtained. The failure to seek a warrant was harmless <span class="star-pagination">*45</span> because it would have been proper to keep the Santana residence under surveillance while the warrant was being sought; since she ventured into plain view, a warrantless arrest would have been justified before the warrant could have been procured.</p>
<p>I therefore join the opinion of the Court.</p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE BRENNAN joins, dissenting.</p>
<p>Earlier this Term, I expressed the view that, in the absence of exigent circumstances, the police may not arrest a suspect without a warrant. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#433" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 433</a></span> (1976) (dissenting opinion). For this reason, I cannot join either the opinion of the Court or that of MR. JUSTICE WHITE, each of which disregards whether exigency justified the police decision to approach Santana's home without a warrant for the purpose of arresting her. Nor can I accept MR. JUSTICE STEVENS' approach, for while acknowledging that some notion of exigency must be asserted to justify the police conduct in this case, MR. JUSTICE STEVENS fails to consider that the exigency present in this case was produced solely by police conduct. I would remand the case to allow the District Court to determine whether that police conduct was justifiable or was solely an attempt to circumvent the warrant requirement.</p>
<p>The Court declines today to settle the oft-reserved question of whether and under what circumstances a police officer may enter the home of a suspect in order to make a warrantless arrest. <i>United States</i> v. <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson, supra,</a></span></i> at 418 n. 6; <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span>, 113 n. 13 (1975); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#480" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 480-481</a></span> (1971); <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499-500</a></span> (1958). Seizing upon the fortuity that Santana was standing in her doorway when the police <span class="star-pagination">*46</span> approached her home for the purpose of entering and arresting her, the Court ignores MR. JUSTICE WHITE'S repeated advocacy of the common-law rule on warrantless entries, <i>ante,</i> p. 43; <i>Coolidge</i> v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#511" aria-description="Citation for case: Coolidge v. New Hampshire"><i>New Hampshire, supra,</i> at 511-512, n. 1</a></span> (WHITE, J., concurring and dissenting),<sup>[1]</sup> and treats this case as a simple application of <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span>.</i></p>
<p>It is somewhat more than that, for the Court takes the opportunity to refine the contours of that decision. Thus, if I correctly read the Court's citation to the "open fields" doctrine of <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#59" aria-description="Citation for case: Hester v. United States">265 U. S. 57, 59</a></span> (1924), the Court holds that the police may enter upon private property to make warrantless arrests of persons who are in plain view and outdoors; and the Court applies that doctrine today to persons who are arguably within their homes but who are "as exposed" to the public as if they were outside. But the Court's encroachment upon the reserved question is limited. <span class="star-pagination">*47</span> Thus, the Court's citation of <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967), does not suggest that a plain view of a suspect is alone sufficient to justify warrantless entry and seizure in the home. Indeed, the Court's rejection of sight alone as a basis for warrantless entry and arrest is made patent, in MR. JUSTICE STEWART'S phrase, by negative implication from the Court's need to elaborate a hot pursuit justification for the police following Santana into her home. Cf. <i>Coolidge</i> v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#480" aria-description="Citation for case: Coolidge v. New Hampshire"><i>New Hampshire, supra,</i> at 480-481</a></span>. Presumably, if plain view were the touchstone, Santana would have been just as liable to warrantless arrest as she retreated several feet inside her open door as she was when standing in the doorway.</p>
<p>The Court's doctrine, then, appears <i>sui generis,</i> useful only in arresting persons who are "as exposed to public view, speech, hearing, and touch," <i>ante,</i> at 42, as though in the unprotected outdoors. Narrow though it may be, however, the Court's approach does not depend on whether exigency justifies an arrest on private property, and thus I cannot join it.</p>
<p>MR. JUSTICE STEVENS focuses on what I believe to be the right question in this casewhether there were exigent circumstancesand reaches an affirmative answer because he finds a "significant risk that the marked money would no longer be in Santana's possession if the police waited until a warrant could be obtained." <i>Ante,</i> at 44. I agree that there were exigent circumstances in this case. McCafferty was arrested a block and a half down the street from Santana's home. Although the arresting officers did not see anyone in Santana's home watching the arrest, App. 16, one officer testified: "We were a block and a half from her home when the arrest was made. I am sure that the word would have been back within a matter of seconds or minutes." <i>Id.,</i> at 51. That is undoubtedly a reasonable conclusion to draw <span class="star-pagination">*48</span> from the facts of the arrest; and the danger that the evidence would be destroyed and the suspects gone before a warrant could be obtained would ordinarily justify the police's quick return to Santana's home and the warrantless entry and arrest. If that is the basis of the "significant risk" to which MR. JUSTICE STEVENS refers, I have no difference with him on that score.<sup>[2]</sup></p>
<p>I do not believe, however, that these exigent circumstances automatically validate Santana's arrest. The exigency that justified the entry and arrest was solely a product of police conduct. Had Officer Gilletti driven McCafferty to a more remote location before arresting her, it appears that no exigency would have been created by the arrest; in such an event a warrant would have been necessary, in my view, before Santana could have been arrested. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#433" aria-description="Citation for case: United States v. Watson">423 U. S., at 433</a></span> (MARSHALL, J., dissenting). It is not apparent on this record why Officer Gilletti arrested McCafferty so close to Santana's home when the arresting officers were clearly aware that such a nearby arrest would necessitate the prompt arrest of Santana. App. 51. While a police decision that the time is right to arrest a suspect should properly be given great deference, cf. <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#310" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 310</a></span> (1966), the power to arrest is an awesome one and is subject to abuse. An arrest may permit a search of premises incident to the arrest, a search that otherwise could be carried out only upon probable cause and pursuant to a search warrant. Likewise, an arrest in circumstances such as those presented here may create exigency that may justify a search <span class="star-pagination">*49</span> or another arrest. When an arrest is so timed that it is no more than an attempt to circumvent the warrant requirement, I would hold the subsequent arrest or search unlawful. See <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#469" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 469-471</a></span>; <i>Vale</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#35" aria-description="Citation for case: Vale v. Louisiana">399 U. S. 30, 35</a></span> (1970); <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#767" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 767</a></span> (1969); <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span>, 226 and 230 (1960); <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#82" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 82</a></span> (1950) (Frankfurter, J., dissenting); <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#467" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 467</a></span> (1932). Accordingly, I would remand this case for consideration of whether the police decision to arrest McCafferty a block and a half from Santana's home was for the sole purpose of creating the exigent circumstances that otherwise would justify Santana's subsequent arrest.<sup>[3]</sup></p>
<h2>NOTES</h2>
<p>[*]  <i>Frank Carrington, Wayne W. Schmidt, Vernon S. Gill,</i> and <i>William K. Lambie</i> filed a brief for the Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging reversal.</p>
<p>[1]  An Officer Strohm testified that he recognized Santana, whom he had seen before. He also indicated that she was standing directly in the doorwayone step forward would have put her outside, one step backward would have put her in the vestibule of her residence.</p>
<p>[2]  It is not apparent on what grounds respondent Alejandro had standing to protest the seizures. However, the Government did not raise this issue below and consequently we do not reach it.</p>
<p>[3]  <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Warden</a></span></i> was based upon the "exigencies of the situation," <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S., at 298</a></span>, and did not use the term "hot pursuit" or even involve a "hot pursuit" in the sense that that term would normally be understood. That phrase first appears in <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, 16 n. 7 (1948), where it was recognized that some element of a chase will usually be involved in a "hot pursuit" case.</p>
<p>[1]  MR. JUSTICE WHITE would have us bequeath our duty to interpret the Constitution to the States and Congress. As I said in response to a similar argument in <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span>:</i>
</p>
<p>"[T]he doctrine of deference that the Court invokes is contrary to the principles of constitutional analysis practiced since <i>Marbury</i> v. <i>Madison,</i> <span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/" aria-description="Citation for case: Marbury v. Madison">1 Cranch 137</a></span> (1803). . . . [I]t is well settled that the mere existence of statutes or practice, even of long standing, is no defense to an unconstitutional practice. `[N]o one acquires a vested or protected right in violation of the Constitution by long use, even when that span of time covers our entire national existence and indeed predates it.' <i>Walz</i> v. <i>Tax Comm'n,</i> <span class="citation" data-id="9841980"><a href="/opinion/108135/walz-v-tax-commn-of-city-of-new-york/#678" aria-description="Citation for case: Walz v. Tax Comm&#x27;n of City of New York">397 U. S. 664, 678</a></span> (1970). See also <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973); <i>Roe</i> v. <i>Wade,</i> <span class="citation" data-id="9425157"><a href="/opinion/108713/roe-v-wade/" aria-description="Citation for case: Roe v. Wade">410 U. S. 113</a></span> (1973); <i>Furman</i> v. <i>Georgia,</i> <span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/" aria-description="Citation for case: Furman v. Georgia">408 U. S. 238</a></span> (1972); <i>Reynolds</i> v. <i>Sims,</i> <span class="citation" data-id="9422829"><a href="/opinion/106850/reynolds-v-sims/" aria-description="Citation for case: Reynolds v. Sims">377 U. S. 533</a></span> (1964). Our function in constitutional cases is weightier than the Court today suggests: where reasoned analysis shows a practice to be constitutionally deficient, our obligation is to the Constitution, not the Congress." <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#443" aria-description="Citation for case: United States v. Watson">423 U. S., at 443</a></span> (dissenting opinion) (footnote omitted).</p>
<p>[2]  I assume that MR. JUSTICE STEVENS is not suggesting that exigent circumstances justifying a warrantless search or arrest are always presentregardless of whether the suspect is aware the police are on his trailwhenever police have probable cause to believe the suspect is in possession of evidence. Cf. <i>Vale</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/" aria-description="Citation for case: Vale v. Louisiana">399 U. S. 30</a></span> (1970).</p>
<p>[3]  Because I cannot agree that police may arrest a suspect in a public place solely upon probable cause, I cannot agree with MR. JUSTICE STEVENS that any police error in deciding to return to Santana's home for the purpose of entering and arresting her was harmless.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Satterfield.json  (`lake-record`, 2 assertions)

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
{"assertion_id": "f045d89534e83ed7", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Satterfield"}, "payload": {"all": [{"cite": "743 F.2d 827", "page": "827", "reporter": "F.2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "743"}, {"cite": "53 U.S.L.W. 2212", "page": "2212", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "53"}], "display": "743 F.2d 827", "official": {"cite": "743 F.2d 827", "page": "827", "reporter": "F.2d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "743"}, "official_selection_present": true, "record_id": "United States v. Satterfield"}}
{"assertion_id": "933c37472de61e4d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Satterfield"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Satterfield", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
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
