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

## GROUP: content/cases/Colorado v. Connelly.md  (`case`, 5 assertions)

### content_page

```
---
title: "Colorado v. Connelly"
type: case
citation: "479 U.S. 157 (1986)"
parallel_cite: "107 S. Ct. 515; 93 L. Ed. 2d 473; 55 U.S.L.W. 4043"
neutral_cite: 1986 U.S. LEXIS 23
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1986
date_decided: 1986-12-10
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1986-12-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Colorado v. Connelly
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111779/colorado-v-connelly/"
  cluster_id: 111779
  opinion_id: 9430748
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brown v. Mississippi]]", "[[Chambers v. Florida]]", "[[Ashcraft v. Tennessee]]", "[[Arizona v. Fulminante]]"]
aliases: []
tags: ["case", "fifth-amendment", "due-process", "confessions", "voluntariness", "police-coercion", "state-action"]
holding: "A confession is \"involuntary\" for due-process purposes only when there is COERCIVE POLICE ACTIVITY; a suspect's mental illness or…"
lake:
  record_id: Colorado v. Connelly
  status: verified
  projected_at: 2026-07-06
---

# Colorado v. Connelly

*479 U.S. 157 (1986)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Connelly approached a Denver officer and, unprompted, confessed to a murder. He was later found to have been suffering from chronic schizophrenia and to have confessed in response to "command hallucinations" that he believed were the voice of God. The Colorado courts suppressed the statements as involuntary on the ground that his mental illness had overborne his free will, without any police misconduct.

## Issue
Whether a confession can be "involuntary" under the Due Process Clause based solely on the speaker's mental illness, absent any coercive police conduct.

## Rule
No; due-process involuntariness requires state coercion. "We hold that coercive police activity is a necessary predicate to the finding that a confession is not 'voluntary' within the meaning of the Due Process Clause of the Fourteenth Amendment." — 479 U.S. 157, 167. ^pin-167

A defendant's mental condition, by itself and apart from its relation to official coercion, does not make a confession involuntary; reliability concerns are governed by state evidence law, not the Due Process Clause.

## Application
Connelly's statements were the product of his psychosis, not of any pressure by the police, who had done nothing to elicit or coerce them. Because there was no coercive police activity linked to the confession, its admission did not violate due process on these facts, however impaired Connelly's decision to speak may have been.

## Conclusion
The confession was not constitutionally involuntary; the Colorado Supreme Court's suppression was reversed. Coercive police activity is the indispensable predicate of a due-process voluntariness claim.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Connelly* cabins the voluntariness line of [[Brown v. Mississippi]], [[Chambers v. Florida]], and [[Ashcraft v. Tennessee]] by requiring state coercion; [[Arizona v. Fulminante]] later subjected an erroneously admitted coerced confession to harmless-error review.

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Colorado v. Connelly*, 479 U.S. 157 (1986) — https://www.courtlistener.com/opinion/111779/colorado-v-connelly/ — pinpoint: 167.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "78fb2d0a7162fa7e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "479 U.S. 157 (1986)", "court": "U.S. Supreme Court", "neutral_cite": "1986 U.S. LEXIS 23", "official_citation_present": true, "parallel_cite": "107 S. Ct. 515; 93 L. Ed. 2d 473; 55 U.S.L.W. 4043", "title": "Colorado v. Connelly", "year": "1986"}}
{"assertion_id": "020410249cb3fe94", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A confession is \\\"involuntary\\\" for due-process purposes only when there is COERCIVE POLICE ACTIVITY; a suspect's mental illness or…", "title": "Colorado v. Connelly"}}
{"assertion_id": "e036a591d2b226e7", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Progeny / Refinement", "title": "Colorado v. Connelly"}}
{"assertion_id": "279d7e69d9aa452a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1986-12-10", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Colorado v. Connelly", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Colorado v. Connelly", "varies_by_point": "false"}}
{"assertion_id": "8d572b1ab528a6e6", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Colorado v. Connelly"}}
```

### lake record — Colorado v. Connelly

```json
{
  "schema_version": "s2.v1",
  "record_id": "Colorado v. Connelly",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Colorado v. Connelly",
    "case_name_short": "Connelly",
    "case_name_full": "Colorado v. Connelly",
    "input_case_name": "Colorado v. Connelly",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-12-10",
    "year": 1986,
    "docket": null,
    "cluster_id": 111779,
    "lead_opinion_id": 9430748,
    "sibling_ids": [
      111779,
      9430748,
      9430749,
      9430750,
      9430751
    ],
    "absolute_url": "/opinion/111779/colorado-v-connelly/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9060076,
        "score": 20,
        "case_name": "Colorado v. Connelly"
      },
      {
        "cluster_id": 111587,
        "score": 20,
        "case_name": "Colorado v. Connelly"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "479 U.S. 157",
      "volume": "479",
      "reporter": "U.S.",
      "page": "157",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 515",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "515",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 473",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "473",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4043",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4043",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 23",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "23",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "479 U.S. 157",
        "volume": "479",
        "reporter": "U.S.",
        "page": "157",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 515",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "515",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 473",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "473",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 23",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "23",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4043",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4043",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "479 U.S. 157",
    "official_selection": {
      "court_class": "scotus",
      "selected": "479 U.S. 157",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-167",
      "page": null,
      "quote": "under the Due Process Clause based solely on the speaker's mental illness, absent any coercive police conduct. ## Rule No; due-process involuntariness requires state coercion.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1986-12-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Colorado v. Connelly",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Baez",
          "cluster_id": 10283156,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Barrett",
          "cluster_id": 4629724,
          "cite": [
            "442 P.3d 492"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ex parte Lalonde",
          "cluster_id": 6243862,
          "cite": [
            "570 S.W.3d 716"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Mateo",
          "cluster_id": 2006639,
          "cite": [
            "811 N.E.2d 1053",
            "2 N.Y.3d 383",
            "779 N.Y.S.2d 399",
            "2 N.Y. 383",
            "2004 N.Y. LEXIS 263"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
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
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 6883327,
          "cite": [
            "80 Ohio St. 3d 89"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
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
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
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
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
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
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
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
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
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
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cockrell v. State",
          "cluster_id": 1517348,
          "cite": [
            "933 S.W.2d 73",
            "1996 Tex. Crim. App. LEXIS 182",
            "1996 WL 514836"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
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
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alvarado v. State",
          "cluster_id": 1676536,
          "cite": [
            "912 S.W.2d 199",
            "1995 Tex. Crim. App. LEXIS 116",
            "1995 WL 675552"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Penry v. State",
          "cluster_id": 2372264,
          "cite": [
            "903 S.W.2d 715",
            "1995 WL 68622"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
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
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. District Court in & for First Judicial District, Jefferson County",
          "cluster_id": 1138536,
          "cite": [
            "785 P.2d 141",
            "14 Brief Times Rptr. 75",
            "1990 Colo. LEXIS 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Glen Coe, Petitioner-Appellee/cross-Appellant v. Ricky Bell, Warden, Respondent-Appellant/cross-Appellee",
          "cluster_id": 759483,
          "cite": [
            "161 F.3d 320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Leonard",
          "cluster_id": 6893283,
          "cite": [
            "104 Ohio St. 3d 54"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
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
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
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
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oursbourn v. State",
          "cluster_id": 2334003,
          "cite": [
            "259 S.W.3d 159",
            "2008 Tex. Crim. App. LEXIS 686",
            "2008 WL 2261744"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Byron Halsey v. Frank Pfeiffer",
          "cluster_id": 2671183,
          "cite": [
            "750 F.3d 273",
            "2014 WL 1622769",
            "2014 U.S. App. LEXIS 7696"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
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
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lane v. State",
          "cluster_id": 1517312,
          "cite": [
            "933 S.W.2d 504",
            "1996 Tex. Crim. App. LEXIS 225",
            "1996 WL 649142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Weaver",
          "cluster_id": 2633370,
          "cite": [
            "29 P.3d 103",
            "111 Cal. Rptr. 2d 2",
            "26 Cal. 4th 876",
            "2001 D.A.R. 8853",
            "2001 Daily Journal DAR 8853",
            "2001 Cal. Daily Op. Serv. 7228",
            "2001 Cal. LEXIS 5263"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Guerra",
          "cluster_id": 2633286,
          "cite": [
            "129 P.3d 321",
            "40 Cal. Rptr. 3d 118",
            "37 Cal. 4th 1067",
            "2006 Cal. Daily Op. Serv. 1802",
            "2006 Daily Journal DAR 2547",
            "2006 Cal. LEXIS 2872"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Antwine",
          "cluster_id": 2364064,
          "cite": [
            "743 S.W.2d 51",
            "1987 Mo. LEXIS 374",
            "1987 WL 2721"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111779 OR 9430748 OR 9430749 OR 9430750 OR 9430751) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTUyODY3MjAwMDAwJnM9NDYwMDc4MCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111779+OR+9430748+OR+9430749+OR+9430750+OR+9430751%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111779 OR 9430748 OR 9430749 OR 9430750 OR 9430751)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNzYmcz0yNDE3NTEyJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111779+OR+9430748+OR+9430749+OR+9430750+OR+9430751%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111779 OR 9430748 OR 9430749 OR 9430750 OR 9430751)",
        "reviewed": 99,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 99,
        "triage_read": 1,
        "triage_snippet_classified": 98
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111779 OR 9430748 OR 9430749 OR 9430750 OR 9430751)",
    "indexed_citing_opinions": 2352,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111779,
        "count": 2044,
        "count_source": "search"
      },
      {
        "opinion_id": 9430748,
        "count": 338,
        "count_source": "search"
      },
      {
        "opinion_id": 9430749,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430750,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430751,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4020,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/colorado-v-connelly.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyMDAzMzgmcz0xMDM0MDIzOCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111779+OR+9430748+OR+9430749+OR+9430750+OR+9430751%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111779,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 100929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 105589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 106544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 106881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 107526,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 107650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 107890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 108111,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 108429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 108967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 109430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 110065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 110179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 110267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 110314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 111017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 111542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 111587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 111625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 1153782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
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
    "date_created": "2026-07-05T00:39:03Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:39:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:39:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:43:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:39:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Colorado v. Connelly

```
<opinion type="majority">
<author id="b313-4"><page-number citation-index="1" label="159">*159</page-number>Chief Justice Rehnquist</author>
<p id="Akp">delivered the opinion of the Court.</p>
<p id="b313-5">In this case, the Supreme Court of Colorado held that the United States Constitution requires a court to suppress a confession when the mental state of the defendant, at the time he made the confession, interfered with his “rational intellect” and his “free will.” Because this decision seemed to conflict with prior holdings of this Court, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./474/1050/">474 U. S. 1050</a></span> (1986). We conclude that the admissibility of this kind of statement is governed by state rules of evidence, rather than by our previous decisions regarding coerced confessions and <em>Miranda </em>waivers. We therefore reverse.</p>
<p id="b314-3"><page-number citation-index="1" label="160">*160</page-number>I</p>
<p id="Adql">On August 18, 1983, Officer Patrick Anderson of the Denver Police Department was in uniform, working in an off-duty capacity in downtown Denver. Respondent Francis Connelly approached Officer Anderson and, without any prompting, stated that he had murdered someone and wanted to talk about it. Anderson immediately advised respondent that he had the right to remain silent, that anything he said could be used against him in court, and that he had the right to an attorney prior to any police questioning. See <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Respondent stated that he understood these rights but he still wanted to talk about the murder. Understandably bewildered by this confession, Officer Anderson asked respondent several questions. Connelly denied that he had been drinking, denied that he had been taking any drugs, and stated that, in the past, he had been a patient in several mental hospitals. Officer Anderson again told Connelly that he was under no obligation to say anything. Connelly replied that it was “all right,” and that he would talk to Officer Anderson because his conscience had been bothering him. To Officer Anderson, respondent appeared to understand fully the nature of his acts. Tr. 19.</p>
<p id="b314-4">Shortly thereafter, Homicide Detective Stephen Antuna arrived. Respondent was again advised of his rights, and Detective Antuna asked him “what he had on his mind.” <em>Id., </em>at 24. Respondent answered that he had come all the way from Boston to confess to the murder of Mary Ann Junta, a young girl whom he had killed in Denver sometime during November 1982. Respondent was taken to police headquarters, and a search of police records revealed that the body of an unidentified female had been found in April 1983. Respondent openly detailed his story to Detective Antuna and Sergeant Thomas Haney, and readily agreed to take the officers to the scene of the killing. Under Con-nelly’s sole direction, the two officers and respondent pro-<page-number citation-index="1" label="161">*161</page-number>eeeded in a police vehicle to the location of the crime. Respondent pointed out the exact location of the murder. Throughout this episode, Detective Antuna perceived no indication whatsoever that respondent was suffering from any kind of mental illness. <em>Id., </em>at 33-34.</p>
<p id="b315-5">Respondent was held overnight. During an interview with the public defender’s office the following morning, he became visibly disoriented. He began giving confused answers to questions, and for the first time, stated that “voices” had told him to come to Denver and that he had followed the directions of these voices in confessing. <em>Id., </em>at 42. Respondent was sent to a state hospital for evaluation. He was initially found incompetent to assist in his own defense. By March 1984, however, the doctors evaluating respondent determined that he was competent to proceed to trial.</p>
<p id="b315-6">At a preliminary hearing, respondent moved to suppress all of his statements. Dr. Jeffrey Metzner, a psychiatrist employed by the state hospital, testified that respondent was suffering from chronic schizophrenia and was in a psychotic state at least as of August 17, 1983, the day before he confessed. Metzner’s interviews with respondent revealed that respondent was following the “voice of God.” This voice instructed respondent to withdraw money from the bank, to buy an airplane ticket, and to fly from Boston to Denver. When respondent arrived from Boston, God’s voice became stronger and told respondent either to confess to the killing or to commit suicide. Reluctantly following the command of the voices, respondent approached Officer Anderson and confessed.</p>
<p id="b315-7">Dr. Metzner testified that, in his expert opinion, respondent was experiencing “command hallucinations.” <em>Id., </em>at 56. This condition interfered with respondent’s “volitional abilities; that is, his ability to make free and rational choices.” <em>Ibid. </em>Dr. Metzner further testified that Connelly’s illness did not significantly impair his cognitive abilities. Thus, respondent understood the rights he had when Officer Ander<page-number citation-index="1" label="162">*162</page-number>son and Detective Antuna advised him that he need not speak. <em>Id., </em>at 56-57. Dr. Metzner admitted that the “voices” could in reality be Connelly’s interpretation of his own guilt, but explained that in his opinion, Connelly’s psychosis motivated his confession.</p>
<p id="b316-5">On the basis of this evidence the Colorado trial court decided that respondent’s statements must be suppressed because they were “involuntary.” Relying on our decisions in <em>Townsend </em>v. <em>Sain, </em><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293</a></span> (1963), and <em>Culombe </em>v. <em>Connecticut, </em><span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568</a></span> (1961), the court ruled that a confession is admissible only if it is a product of the defendant’s rational intellect and “free will.” Tr. 88. Although the court found that the police had done nothing wrong or coercive in securing respondent’s confession, Connelly’s illness destroyed his volition and compelled him to confess. <em>Id., </em>at 89. The trial court also found that Connelly’s mental state vitiated his attempted waiver of the right to counsel and the privilege against compulsory self-incrimination. Accordingly, respondent’s initial statements and his custodial confession were suppressed. <em>Id., </em>at 90.</p>
<p id="b316-6">The Colorado Supreme Court affirmed. <span class="citation" data-id="9538999"><a href="/opinion/1153782/people-v-connelly/" aria-description="Citation for case: People v. Connelly">702 P. 2d 722</a></span> (1985). In that court’s view, the proper test for admissibility is whether the statements are “the product of a rational intellect and a free will.” <span class="citation" data-id="9538999"><a href="/opinion/1153782/people-v-connelly/#728" aria-description="Citation for case: People v. Connelly"><em>Id., </em>at 728</a></span>. Indeed, “the absence of police coercion or duress does not foreclose a finding of involuntariness. One’s capacity for rational judgment and free choice may be overborne as much by certain forms of severe mental illness as by external pressure.” <em><span class="citation" data-id="9538999"><a href="/opinion/1153782/people-v-connelly/" aria-description="Citation for case: People v. Connelly">Ibid.</a></span> </em>The court found that the very admission of the evidence in a court of law was sufficient state action to implicate the Due Process Clause of the Fourteenth Amendment to the United States Constitution. The evidence fully supported the conclusion that respondent’s initial statement was not the product of a rational intellect and a free will. The court then considered respondent’s attempted waiver of his constitutional rights and found that respondent’s mental condition precluded his <page-number citation-index="1" label="163">*163</page-number>ability to make a valid waiver. <span class="citation" data-id="9538999"><a href="/opinion/1153782/people-v-connelly/#729" aria-description="Citation for case: People v. Connelly"><em>Id., </em>at 729</a></span>. The Colorado Supreme Court thus affirmed the trial court’s decision to suppress all of Connelly’s statements.</p>
<p id="b317-5">II</p>
<p id="b317-6">The Due Process Clause of the Fourteenth Amendment provides that no State shall “deprive any person of life, liberty, or property, without due process of law.” Just last Term, in <em>Miller </em>v. <em>Fenton, </em><span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#109" aria-description="Citation for case: Miller v. Fenton">474 U. S. 104, 109</a></span> (1985), we held that by virtue of the Due Process Clause “certain interrogation techniques, either in isolation or as applied to the unique characteristics of a particular suspect, are so offensive to a civilized system of justice that they must be condemned.” See also <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#432" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 432-434</a></span> (1986).</p>
<p id="b317-7">Indeed, coercive government misconduct was the catalyst for this Court’s seminal confession case, <em>Brown </em>v. <em>Mississippi, </em><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936). In that case, police officers extracted confessions from the accused through brutal torture. The Court had little difficulty concluding that even though the Fifth Amendment did not at that time apply to the States, the actions of the police were “revolting to the sense of justice.” <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#286" aria-description="Citation for case: Brown v. Mississippi"><em>Id., </em>at 286</a></span>. The Court has retained this due process focus, even after holding, in <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964), that the Fifth Amendment privilege against compulsory self-incrimination applies to the States. See <em>Miller </em>v. <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#109" aria-description="Citation for case: Miller v. Fenton"><em>Fenton, supra, </em>at 109-110</a></span>.</p>
<p id="b317-8">Thus the cases considered by this Court over the 50 years since <em>Brown </em>v. <em><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Mississippi</a></span> </em>have focused upon the crucial element of police overreaching.<footnotemark>1</footnotemark> While each confession case <page-number citation-index="1" label="164">*164</page-number>has turned on its own set of factors justifying the conclusion that police conduct was oppressive, all have contained a substantial element of coercive police conduct. Absent police conduct causally related to the confession, there is simply no basis for concluding that any state actor has deprived a criminal defendant of due process of law.<footnotemark>2</footnotemark> Respondent correctly notes that as interrogators have turned to more subtle forms of psychological persuasion, courts have found the mental condition of the defendant a more significant factor in the “voluntariness” calculus. See <em>Spano </em>v. <em>New York, </em><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span> (1959). But this fact does not justify a conclusion that a defendant’s mental condition, by itself and apart from its relation to official coercion, should ever dispose of the inquiry into constitutional “voluntariness.”</p>
<p id="b318-5">Respondent relies on <em>Blackburn </em>v. <em>Alabama, </em><span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199</a></span> (1960), and <em>Townsend </em>v. <em>Sain, </em><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293</a></span> (1963), for the proposition that the “deficient mental condition of the defendants in those cases was sufficient to render their confessions involuntary.” Brief for Respondent 20. But respondent’s reading of <em><span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/" aria-description="Citation for case: Blackburn v. Alabama">Blackburn</a></span> </em>and <em><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">Townsend</a></span> </em>ignores the integral element of police overreaching present in both cases. In <em><span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/" aria-description="Citation for case: Blackburn v. Alabama">Blackburn</a></span>, </em>the Court found that the petitioner was probably insane at the time of his confession and the police learned during the interrogation that he had a history of mental prob<page-number citation-index="1" label="165">*165</page-number>lems. The police exploited this weakness with coercive tactics: “the eight- to nine-hour sustained interrogation in a tiny room which was upon occasion literally filled with police officers; the absence of Blackburn’s friends, relatives, or legal counsel; [and] the composition of the confession by the Deputy Sheriff rather than by Blackburn.” <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#207" aria-description="Citation for case: Blackburn v. Alabama">361 U. S., at 207-208</a></span>. These tactics supported a finding that the confession was involuntary. Indeed, the Court specifically condemned police activity that “wrings a confession out of an accused against his will.” <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama"><em>Id., </em>at 206-207</a></span>. <em><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">Townsend</a></span> </em>presented a similar instance of police wrongdoing. In that case, a police physician had given Townsend a drug with truth-serum properties. <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/#298" aria-description="Citation for case: Townsend v. Sain">372 U. S., at 298-299</a></span>. The subsequent confession, obtained by officers who knew that Townsend had been given drugs, was held involuntary. These two cases demonstrate that while mental condition is surely relevant to an individual’s susceptibility to police coercion, mere examination of the confessant’s state of mind can never conclude the due process inquiry.</p>
<p id="b319-5">Our “involuntary confession” jurisprudence is entirely consistent with the settled law requiring some sort of “state action” to support a claim of violation of the Due Process Clause of the Fourteenth Amendment. The Colorado trial court, of course, found that the police committed no wrongful acts, and that finding has been neither challenged by respondent nor disturbed by the Supreme Court of Colorado. The latter court, however, concluded that sufficient state action was present by virtue of the admission of the confession into evidence in a court of the State. <span class="citation" data-id="9538999"><a href="/opinion/1153782/people-v-connelly/#728" aria-description="Citation for case: People v. Connelly">702 P. 2d, at 728-729</a></span>.</p>
<p id="b319-6">The difficulty with the approach of the Supreme Court of Colorado is that it fails to recognize the essential link between coercive activity of the State, on the one hand, and a resulting confession by a defendant, on the other. The flaw in respondent’s constitutional argument is that it would expand our previous line of “voluntariness” cases into a far-ranging requirement that courts must divine a defendant’s <page-number citation-index="1" label="166">*166</page-number>motivation for speaking or acting as he did even though there be no claim that governmental conduct coerced his decision.</p>
<p id="b320-5">The most outrageous behavior by a private party seeking to secure evidence against a defendant does not make that evidence inadmissible under the Due Process Clause. See <em>Walter </em>v. <em>United States, </em><span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#656" aria-description="Citation for case: Walter v. United States">447 U. S. 649, 656</a></span> (1980); <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#487" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 487-488</a></span> (1971); <em>Burdeau </em>v. <em>McDowell, </em><span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/#476" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465, 476</a></span> (1921). We have also observed that “[j Jurists and scholars uniformly have recognized that the exclusionary rule imposes a substantial cost on the societal interest in law enforcement by its proscription of what concededly is relevant evidence.” <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#448" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 448-449</a></span> (1976). See also <em>United States </em>v. <em>Havens, </em><span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#627" aria-description="Citation for case: United States v. Havens">446 U. S. 620, 627</a></span> (1980); <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U. S. 338</a></span> (1974). Moreover, suppressing respondent’s statements would serve absolutely no purpose in enforcing constitutional guarantees. The purpose of excluding evidence seized in violation of the Constitution is to substantially deter future violations of the Constitution. See <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 906-913</a></span> (1984). Only if we were to establish a brand new constitutional right — the right of a criminal defendant to confess to his crime only when totally rational and properly motivated — could respondent’s present claim be sustained.</p>
<p id="b320-6">We have previously cautioned against expanding “currently applicable exclusionary rules by erecting additional barriers to placing truthful and probative evidence before state juries . . . .” <em>Lego </em>v. <em>Twomey, </em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#488" aria-description="Citation for case: Lego v. Twomey">404 U. S. 477, 488-489</a></span> (1972). We abide by that counsel now. “[T]he central purpose of a criminal trial is to decide the factual question of the defendant’s guilt or innocence,” <em>Delaware </em>v. <em>Van Arsdall, </em><span class="citation" data-id="9430412"><a href="/opinion/111625/delaware-v-van-arsdall/#681" aria-description="Citation for case: Delaware v. Van Arsdall">475 U. S. 673, 681</a></span> (1986), and while we have previously held that exclusion of evidence may be necessary to protect constitutional guarantees, both the necessity for the collateral inquiry and the exclusion of evidence deflect a criminal trial from its basic purpose. Respondent would now have us re<page-number citation-index="1" label="167">*167</page-number>quire sweeping inquiries into the state of mind of a criminal defendant who has confessed, inquiries quite divorced from any coercion brought to bear on the defendant by the State. We think the Constitution rightly leaves this sort of inquiry to be resolved by state laws governing the admission of evidence and erects no standard of its own in this area. A statement rendered by one in the condition of respondent might be proved to be quite unreliable, but this is a matter to be governed by the evidentiary laws of the forum, see, <em>e. g., </em>Fed. Rule Evid. 601, and not by the Due Process Clause of the Fourteenth Amendment. “The aim of the requirement of due process is not to exclude presumptively false evidence, but to prevent fundamental unfairness in the use of evidence, whether true or false.” <em>Lisenba </em>v. <em>California, </em><span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#236" aria-description="Citation for case: Lisenba v. California">314 U. S. 219, 236</a></span> (1941).</p>
<p id="b321-5">We hold that coercive police activity is a necessary predicate to the finding that a confession is not “voluntary” within the meaning of the Due Process Clause of the Fourteenth Amendment. We also conclude that the taking of respondent’s statements, and their admission into evidence, constitute no violation of that Clause.</p>
<p id="b321-6">III</p>
<p id="b321-7">A</p>
<p id="b321-8">The Supreme Court of Colorado went on to affirm the trial court’s ruling that respondent’s later statements made while in custody should be suppressed because respondent had not waived his right to consult an attorney and his right to remain silent. That court held that the State must bear its burden of proving waiver of these <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights by “clear and convincing evidence.” <span class="citation" data-id="9538999"><a href="/opinion/1153782/people-v-connelly/#729" aria-description="Citation for case: People v. Connelly">702 P. 2d, at 729</a></span>. Although we have stated in passing that the State bears a “heavy” burden in proving waiver, <em>Tague </em>v. <em>Louisiana, </em><span class="citation" data-id="110179"><a href="/opinion/110179/tague-v-louisiana/" aria-description="Citation for case: Tague v. Louisiana">444 U. S. 469</a></span> (1980) <em>(per curiam); North Carolina </em>v. <em>Butler </em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#373" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369, 373</a></span> (1979); <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 475</a></span>, we have never <page-number citation-index="1" label="168">*168</page-number>held that the “clear and convincing evidence” standard is the appropriate one.</p>
<p id="b322-5">In <em>Lego </em>v. <em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">Twomey, supra,</a></span> </em>this Court upheld a procedure in which the State established the voluntariness of a confession by no more than a preponderance of the evidence. We upheld it for two reasons. First, the voluntariness determination has nothing to do with the reliability of jury verdicts; rather, it is designed to determine the presence of police coercion. Thus, voluntariness is irrelevant to the presence or absence of the elements of a crime, which must be proved beyond a reasonable doubt. See <em>In re Winship, </em><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">397 U. S. 358</a></span> (1970). Second, we rejected Lego’s assertion that a high burden of proof was required to serve the values protected by the exclusionary rule. We surveyed the various reasons for excluding evidence, including a violation of the requirements of <em>Miranda </em>v. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona, supra,</a></span> </em>and we stated that “[i]n each instance, and without regard to its probative value, evidence is kept from the trier of guilt or innocence for reasons wholly apart from enhancing the reliability of verdicts.” <em>Lego </em>v. <em>Twomey, </em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#488" aria-description="Citation for case: Lego v. Twomey">404 U. S., at 488</a></span>. Moreover, we rejected the argument that “the importance of the values served by exclusionary rules is itself sufficient demonstration that the Constitution also requires admissibility to be proved beyond a reasonable doubt.” <em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">Ibid.</a></span> </em>Indeed, the Court found that “no substantial evidence has accumulated that federal rights have suffered from determining admissibility by a preponderance of the evidence.” <em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">Ibid.</a></span></em></p>
<p id="b322-6">We now reaffirm our holding in <em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">Lego</a></span>: </em>Whenever the State bears the burden of proof in a motion to suppress a statement that the defendant claims was obtained in violation of our <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>doctrine, the State need prove waiver only by a preponderance of the evidence. See <em>Nix </em>v. <em>Williams, </em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#444" aria-description="Citation for case: Nix v. Williams">467 U. S. 431, 444</a></span>, and n. 5 (1984); <em>United States </em>v. <em>Matlock, </em><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/#178" aria-description="Citation for case: United States v. Matlock">415 U. S. 164, 178, n. 14</a></span> (1974) (“[T]he controlling burden of proof at suppression hearings should impose no greater burden than proof by a preponderance of the evidence . . .”). <page-number citation-index="1" label="169">*169</page-number>Cf. <em>Moore </em>v. <em>Michigan, </em><span class="citation" data-id="9841953"><a href="/opinion/105589/moore-v-michigan/#161" aria-description="Citation for case: Moore v. Michigan">355 U. S. 155, 161-162</a></span> (1957). If, as we held in <em>Lego </em>v. <em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">Twomey, supra,</a></span> </em>the voluntariness of a confession need be established only by a preponderance of the evidence, then a waiver of the auxiliary protections established in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>should require no higher burden of proof. “[Exclusionary rules are very much aimed at deterring lawless conduct by police and prosecution and it is very doubtful that escalating the prosecution’s burden of proof in . . . suppression hearings would be sufficiently productive in this respect to outweigh the public interest in placing probative evidence before juries for the purpose of arriving at truthful decisions about guilt or innocence.” <em>Lego </em>v. <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#489" aria-description="Citation for case: Lego v. Twomey"><em>Twomey, supra, </em>at 489</a></span>. See also <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon">468 U. S., at 906-913</a></span>.</p>
<p id="b323-5">B</p>
<p id="b323-6">We also think that the Supreme Court of Colorado was mistaken in its analysis of the question whether respondent had waived his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights in this case.<footnotemark>3</footnotemark> Of course, a waiver must at a minimum be “voluntary” to be effective against an accused. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 444, 476</a></span>; <em>North Carolina </em>v. <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#373" aria-description="Citation for case: North Carolina v. Butler"><em>Butler, supra, </em>at 373</a></span>. The Supreme Court of Colorado in addressing this question relied on the testimony of the court-appointed psychiatrist to the effect that respondent was not capable of making a “free decision with respect to his constitutional right of silence . . . and his constitutional right to confer with a lawyer before talking to the police.” <span class="citation" data-id="9538999"><a href="/opinion/1153782/people-v-connelly/#729" aria-description="Citation for case: People v. Connelly">702 P. 2d, at 729</a></span>.</p>
<p id="b323-7">We think that the Supreme Court of Colorado erred in importing into this area of constitutional law notions of “free will” that have no place there. There is obviously no reason to require more in the way of a “voluntariness” inquiry in the <page-number citation-index="1" label="170">*170</page-number><em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver context than in the Fourteenth Amendment confession context. The sole concern of the Fifth Amendment, on which <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was based, is governmental coercion. See <em>United States </em>v. <em>Washington, </em><span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#187" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 187</a></span> (1977); <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#460" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 460</a></span>. Indeed, the Fifth Amendment privilege is not concerned “with moral and psychological pressures to confess emanating from sources other than official coercion.” <em>Oregon </em>v. <em>Elstad, </em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#305" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 305</a></span> (1985). The voluntariness of a waiver of this privilege has always depended on the absence of police overreaching, not on “free choice” in any broader sense of the word. See <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#421" aria-description="Citation for case: Moran v. Burbine">475 U. S., at 421</a></span> (“[T]he relinquishment of the right must have been voluntary in the sense that it was the product of a free and deliberate choice rather than intimidation, coercion or deception. . . . [T]he record is devoid of any suggestion that police resorted to physical or psychological pressure to elicit the statements”); <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#726" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 726-727</a></span> (1979) (The defendant was “not worn down by improper interrogation tactics or lengthy questioning or by trickery or deceit. . . . The officers did not intimidate or threaten respondent in any way. Their questioning was restrained and free from the abuses that so concerned the Court in <em>Miranda”).</em></p>
<p id="b324-5">. Respondent urges this Court to adopt his “free will” rationale, and to find an attempted waiver invalid Whenever the defendant feels compelled to waive his rights by reason of any compulsion, even if the compulsion does not flow from the police. But such a treatment of the waiver issue would “cut this Court’s holding in <em>[Miranda] </em>completely loose from its own explicitly stated rationale.” <em>Beckwith </em>v. <em>United States, </em><span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/#345" aria-description="Citation for case: Beckwith v. United States">425 U. S. 341, 345</a></span> (1976). <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>protects defendants against government coercion leading them to surrender rights protected by the Fifth Amendment; it goes no further than that. Respondent’s perception of coercion flowing from the “voice of God,” however important or significant such a <page-number citation-index="1" label="171">*171</page-number>perception may be in other disciplines, is a matter to which the United States Constitution does not speak.</p>
<p id="b325-14"><em>I </em>— i &lt;1</p>
<p id="b325-3">The judgment of the Supreme Court of Colorado is accordingly reversed, and the cause is remanded for further proceedings not inconsistent with this opinion.<footnotemark>4</footnotemark></p>
<p id="b325-4">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b317-9"><em> E. g., Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span> (1978) (defendant subjected to 4-hour interrogation while incapacitated and sedated in intensive-care unit); <em>Greenwald </em>v. <em>Wisconsin, </em><span class="citation" data-id="9423651"><a href="/opinion/107650/greenwald-v-wisconsin/" aria-description="Citation for case: Greenwald v. Wisconsin">390 U. S. 519</a></span> (1968) (defendant, on medication, interrogated for over 18 hours without food or sleep); <em>Beecher </em>v. <em>Alabama, </em><span class="citation" data-id="9423505"><a href="/opinion/107526/beecher-v-alabama/" aria-description="Citation for case: Beecher v. Alabama">389 U. S. 35</a></span> (1967) (police officers held gun to the head of wounded eonfessant to extract confession); <em>Davis </em>v. <em>North Carolina, </em><span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737</a></span> (1966) (16 days of incommunicado interrogation in closed cell without windows, limited food, and coercive tactics); <em>Reck </em>v. <em>Pate, </em><span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/" aria-description="Citation for case: Reck v. Pate">367 U. S. 433</a></span> (1961) <page-number citation-index="1" label="164">*164</page-number>(defendant held for four days with inadequate food and medical attention until confession obtained); <em>Culombe </em>v. <em>Connecticut, </em><span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568</a></span> (1961) (defendant held for five days of repeated questioning during which police employed coercive tactics); <em>Payne </em>v. <em>Arkansas, </em><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span> (1958) (defendant held incommunicado for three days with little food; confession obtained when officers informed defendant that Chief of Police was preparing to admit lynch mob into jail); <em>Ashcraft </em>v. <em>Tennessee, </em><span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span> (1944) (defendant questioned by relays of officers for 36 hours without an opportunity for sleep).</p>
</footnote>
<footnote label="2">
<p id="b318-7"> Even where there is causal connection between police misconduct and a defendant’s confession, it does not automatically follow that there has been a violation of the Due Process Clause. See, <em>e. g., Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#739" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 739</a></span> (1969).</p>
</footnote>
<footnote label="3">
<p id="b323-8"> Petitioner conceded at oral argument that when Officer Anderson handcuffed respondent, the custody requirement of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was satisfied. For purposes of our decision we accept that concession, and we similarly assume that the police officers “interrogated” respondent within the meaning of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</em></p>
</footnote>
<footnote label="4">
<p id="b325-10"> It is possible to read the opinion of the Supreme Court of Colorado as finding respondent’s <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver invalid on other grounds. Even if that is the ease, however, we nonetheless reverse the judgment in its entirety because of our belief that the Supreme Court of Colorado’s analysis was influenced by its mistaken view of “voluntariness” in the constitutional sense. Reconsideration of other issues, not inconsistent with our opinion, is of course open to the Supreme Court of Colorado on remand.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Colorado v. Spring.md  (`case`, 5 assertions)

### content_page

```
---
title: "Colorado v. Spring"
type: case
citation: "479 U.S. 564 (1987)"
parallel_cite: "107 S. Ct. 851; 93 L. Ed. 2d 954; 55 U.S.L.W. 4162"
neutral_cite: 1987 U.S. LEXIS 418
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-01-27
docket: 85-1517
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-01-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Colorado v. Spring
  varies_by_point: false
  scope_note: Good law.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111798/colorado-v-spring/"
  cluster_id: 111798
  opinion_id: 9430793
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny"
related: ["[[Moran v. Burbine]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "waiver"]
holding: "A Miranda waiver is knowing and intelligent even though police did not tell the suspect all of the crimes or subjects the interrogation would cover; awareness of every possible subject of questioning is not a prerequisite to a valid waiver, and silence about the subject matter is not trickery."
lake:
  record_id: Colorado v. Spring
  status: verified
  projected_at: 2026-07-06
---

# Colorado v. Spring

*479 U.S. 564 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Spring was arrested by federal agents on firearms charges. After [[Miranda and Custodial Interrogation|Miranda warnings]], he waived his rights and answered questions; the agents also asked him about an unrelated Colorado murder, which he eventually admitted. Spring argued his waiver was invalid because the agents had not told him in advance that they intended to question him about the homicide.

## Issue
Whether a suspect's waiver of his [[Miranda and Custodial Interrogation|Miranda rights]] is rendered invalid (not knowing and intelligent) because the police did not inform him beforehand of all the subjects or offenses the interrogation would cover.

## Rule
No. A valid waiver requires that it be voluntary and that it be made with full awareness of the *nature* of the right abandoned and the consequences of doing so — not awareness of every tactical detail. "[A] suspect's awareness of all the possible subjects of questioning in advance of interrogation is not relevant to determining whether the suspect voluntarily, knowingly, and intelligently waived his Fifth Amendment privilege." — 479 U.S. at 577. ^pin-577

The *[[Miranda v. Arizona|Miranda]]* warnings themselves convey the nature of the privilege and the consequences of abandoning it (anything he says may be used against him), so a suspect need not also be told *which* crimes will be discussed. Mere police silence about the subject matter of the interrogation is not the kind of trickery or deception that would invalidate an otherwise valid waiver.

## Application
Spring received and understood the *[[Miranda v. Arizona|Miranda]]* warnings and voluntarily waived his rights. The agents' failure to forewarn him that they would also ask about the Colorado murder did not affect the knowing-and-intelligent character of that waiver: he knew he could remain silent and that anything he said could be used against him. His admissions were therefore the product of a valid waiver.

## Conclusion
The waiver was knowing and intelligent despite the suspect's ignorance of all the topics to be covered. The judgment of the Colorado Supreme Court was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Consistent with [[Moran v. Burbine]] (a waiver is not invalidated by the police withholding information — there, that an attorney was trying to reach the suspect): the validity of a *[[Miranda v. Arizona|Miranda]]* waiver turns on the suspect's understanding of the right itself, not on full information about the investigation.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny*

## Sources
- *Colorado v. Spring*, 479 U.S. 564 (1987) — https://www.courtlistener.com/opinion/111798/colorado-v-spring/ — pinpoint: 577.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e698a0c51a6cd8bd", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "479 U.S. 564 (1987)", "court": "U.S. Supreme Court", "neutral_cite": "1987 U.S. LEXIS 418", "official_citation_present": true, "parallel_cite": "107 S. Ct. 851; 93 L. Ed. 2d 954; 55 U.S.L.W. 4162", "title": "Colorado v. Spring", "year": "1987"}}
{"assertion_id": "3a509bd8636fd531", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A Miranda waiver is knowing and intelligent even though police did not tell the suspect all of the crimes or subjects the interrogation would cover; awareness of every possible subject of questioning is not a prerequisite to a valid waiver, and silence about the subject matter is not trickery.", "title": "Colorado v. Spring"}}
{"assertion_id": "87b545b6eac94877", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny", "title": "Colorado v. Spring"}}
{"assertion_id": "386e6388b80151ca", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Colorado v. Spring"}}
{"assertion_id": "debf84222102e7f7", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1987-01-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Colorado v. Spring", "field_i_validity": "good_law", "scope_note": "Good law.", "title": "Colorado v. Spring", "varies_by_point": "false"}}
```

### lake record — Colorado v. Spring

```json
{
  "schema_version": "s2.v1",
  "record_id": "Colorado v. Spring",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Colorado v. Spring",
    "case_name_short": "Spring",
    "case_name_full": "Colorado v. Spring",
    "input_case_name": "Colorado v. Spring",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-01-27",
    "year": 1987,
    "docket": "85-1517",
    "cluster_id": 111798,
    "lead_opinion_id": 9430793,
    "sibling_ids": [
      111798,
      9430793,
      9430794
    ],
    "absolute_url": "/opinion/111798/colorado-v-spring/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "479 U.S. 564",
      "volume": "479",
      "reporter": "U.S.",
      "page": "564",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 851",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "851",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 954",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "954",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4162",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4162",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 418",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "418",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "479 U.S. 564",
        "volume": "479",
        "reporter": "U.S.",
        "page": "564",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 851",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "851",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 954",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "954",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 418",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "418",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4162",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4162",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "479 U.S. 564",
    "official_selection": {
      "court_class": "scotus",
      "selected": "479 U.S. 564",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-577",
      "page": null,
      "quote": "--- # Colorado v. Spring *479 U.S. 564 (1987)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Spring was arrested by federal agents on firearms charges. After Miranda warnings, he waived his rights and answered questions; the agents also asked him about an unrelated Colorado murder, which he eventually admitted. Spring argued his waiver was invalid because the agents had not told him in advance that they intended to question him about the homicide. ## Issue Whether a suspect's waiver of his Miranda rights is rendered invalid (not knowing and intelligent) because the police did not inform him beforehand of all the subjects or offenses the interrogation would cover. ## Rule No. A valid waiver requires that it be voluntary and that it be made with full awareness of the *nature* of the right abandoned and the consequences of doing so \u2014 not awareness of every tactical detail.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-01-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Colorado v. Spring",
    "varies_by_point": false,
    "scope_note": "Good law.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Colorado v. Spring:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Luis Fernando Ortiz",
          "cluster_id": 4472662,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Moore, 07ca093 (11-26-2008)",
          "cluster_id": 3983329,
          "cite": [
            "2008 Ohio 6238"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane1_negative"
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
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ruiz",
          "cluster_id": 121166,
          "cite": [
            "153 L. Ed. 2d 586",
            "122 S. Ct. 2450",
            "536 U.S. 622",
            "2002 U.S. LEXIS 4650"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Male Juvenile (95-Cr-1074)",
          "cluster_id": 744606,
          "cite": [
            "121 F.3d 34",
            "1997 U.S. App. LEXIS 19219",
            "1997 WL 416548"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
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
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Boyette",
          "cluster_id": 2544386,
          "cite": [
            "58 P.3d 391",
            "127 Cal. Rptr. 2d 544",
            "29 Cal. 4th 381"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Penry v. State",
          "cluster_id": 2372264,
          "cite": [
            "903 S.W.2d 715",
            "1995 WL 68622"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. District Court in & for First Judicial District, Jefferson County",
          "cluster_id": 1138536,
          "cite": [
            "785 P.2d 141",
            "14 Brief Times Rptr. 75",
            "1990 Colo. LEXIS 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Tibbetts",
          "cluster_id": 6889013,
          "cite": [
            "92 Ohio St. 3d 146",
            "749 N.E.2d 226"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Mauro",
          "cluster_id": 111878,
          "cite": [
            "95 L. Ed. 2d 458",
            "107 S. Ct. 1931",
            "481 U.S. 520",
            "1987 U.S. LEXIS 1933"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Koedatich",
          "cluster_id": 2159212,
          "cite": [
            "548 A.2d 939",
            "112 N.J. 225",
            "1988 N.J. LEXIS 83"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Traylor v. State",
          "cluster_id": 1765408,
          "cite": [
            "596 So. 2d 957",
            "1992 WL 4873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Musselwhite",
          "cluster_id": 1225502,
          "cite": [
            "17 Cal. 4th 1216",
            "954 P.2d 475",
            "98 Daily Journal DAR 4745",
            "98 Cal. Daily Op. Serv. 3452",
            "74 Cal. Rptr. 2d 212",
            "1998 Cal. LEXIS 2622"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lee Moore v. Betty Mitchell",
          "cluster_id": 2981722,
          "cite": [
            "708 F.3d 760",
            "2013 U.S. App. LEXIS 3915",
            "2013 WL 673524"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Van Tran",
          "cluster_id": 2428819,
          "cite": [
            "864 S.W.2d 465",
            "1993 Tenn. LEXIS 343"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ian Gordon, United States of America v. Ian Gordon",
          "cluster_id": 536184,
          "cite": [
            "895 F.2d 932"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Clark",
          "cluster_id": 1121458,
          "cite": [
            "857 P.2d 1099",
            "5 Cal. 4th 950",
            "22 Cal. Rptr. 2d 689",
            "93 Daily Journal DAR 11122",
            "93 Cal. Daily Op. Serv. 6528",
            "1993 Cal. LEXIS 4179"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leza v. State",
          "cluster_id": 2541167,
          "cite": [
            "351 S.W.3d 344",
            "2011 Tex. Crim. App. LEXIS 1372",
            "2011 WL 4809816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramirez v. State",
          "cluster_id": 1706879,
          "cite": [
            "739 So. 2d 568",
            "1999 WL 506949"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Wash",
          "cluster_id": 1158185,
          "cite": [
            "861 P.2d 1107",
            "6 Cal. 4th 215",
            "24 Cal. Rptr. 2d 421",
            "93 Cal. Daily Op. Serv. 8554",
            "93 Daily Journal DAR 14629",
            "1993 Cal. LEXIS 5807"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Goodwin",
          "cluster_id": 1667339,
          "cite": [
            "774 N.W.2d 733",
            "278 Neb. 945"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brenton-Farley",
          "cluster_id": 147727,
          "cite": [
            "607 F.3d 1294",
            "2010 U.S. App. LEXIS 11125",
            "2010 WL 2179617"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ripkowski v. State",
          "cluster_id": 1588890,
          "cite": [
            "61 S.W.3d 378",
            "2001 Tex. Crim. App. LEXIS 98",
            "2001 WL 1360126"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hill",
          "cluster_id": 1190445,
          "cite": [
            "839 P.2d 984",
            "3 Cal. 4th 959",
            "13 Cal. Rptr. 2d 475",
            "92 Daily Journal DAR 15770",
            "92 Cal. Daily Op. Serv. 9338",
            "1992 Cal. LEXIS 5500"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Humphrey",
          "cluster_id": 2588759,
          "cite": [
            "132 P.3d 352",
            "2006 WL 988349"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dennis Rosa Collazo v. Wayne Estelle, Warden, California Mens Colony",
          "cluster_id": 565270,
          "cite": [
            "940 F.2d 411",
            "91 Daily Journal DAR 8681",
            "91 Cal. Daily Op. Serv. 5640",
            "1991 U.S. App. LEXIS 15265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111798 OR 9430793 OR 9430794) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjIzNDI0MDAwMDAwJnM9MjkzOTkzNSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111798+OR+9430793+OR+9430794%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111798 OR 9430793 OR 9430794)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTEmcz0xNzQyMDIzJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111798+OR+9430793+OR+9430794%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111798 OR 9430793 OR 9430794)",
        "reviewed": 23,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 23,
        "triage_read": 0,
        "triage_snippet_classified": 23
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111798 OR 9430793 OR 9430794)",
    "indexed_citing_opinions": 627,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111798,
        "count": 546,
        "count_source": "search"
      },
      {
        "opinion_id": 9430793,
        "count": 89,
        "count_source": "search"
      },
      {
        "opinion_id": 9430794,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1070,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/colorado-v-spring.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyNTA2OTUmcz05Mzk3NjI0JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111798+OR+9430793+OR+9430794%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111798,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 110065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 111779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 291902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 334838,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 388110,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 392980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 431718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 2605185,
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
    "date_created": "2026-07-05T00:43:36Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:43:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:43:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:47:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:43:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Colorado v. Spring

```
<opinion type="majority">
<author id="b720-6">Justice Powell</author>
<p id="A9W">delivered the opinion of the Court.</p>
<p id="b720-7">In <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), the Court held that a suspect's waiver of the Fifth Amendment privilege against self-incrimination is valid only if it is made voluntarily, knowingly, and intelligently. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 444</a></span>. This case presents the question whether the suspect’s awareness of all the crimes about which he may be questioned is relevant to determining the validity of his decision to waive the Fifth Amendment privilege.</p>
<p id="b720-8">I</p>
<p id="b720-9">In February 1979, respondent John Leroy Spring and a companion shot and killed Donald Walker during a hunting trip in Colorado. Shortly thereafter, an informant told agents of the Bureau of Alcohol, Tobacco, and Firearms (ATF) that Spring was engaged in the interstate transportation of stolen firearms. The informant also told the agents that Spring had discussed his participation in the Colorado killing. At the time the ATF agents received this information, Walker’s body had not been found and the police had received no report of his disappearance. Based on the information received from the informant relating to the firearms violations, the ATF agents set up an undercover operation to purchase firearms from Spring. On March 30, 1979, ATF agents arrested Spring in Kansas City, Missouri, during the undercover purchase.</p>
<p id="b721-4"><page-number citation-index="1" label="567">*567</page-number>An ATF agent on the scene of the arrest advised Spring of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights.<footnotemark>1</footnotemark> Spring was advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights a second time after he was transported to the ATF office in Kansas City. At the ATF office, the agents also advised Spring that he had the right to stop the questioning at any time or to stop the questioning until the presence of an attorney could be secured. Spring then signed a written form stating that he understood and waived his rights, and that he was willing to make a statement and answer questions.</p>
<p id="b721-5">ATF agents first questioned Spring about the firearms transactions that led to his arrest. They then asked Spring if he had a criminal record. He admitted that he had a juvenile record for shooting his aunt when he was 10 years old. The agents asked if Spring had ever shot anyone else. Spring ducked his head and mumbled, “I shot another guy once.” The agents asked Spring if he had ever been to Colorado. Spring said no. The agents asked Spring whether he had shot a man named Walker in Colorado and thrown his body into a snowbank. Spring paused and then ducked his head again and said no. The interview ended at this point.</p>
<p id="b721-6">On May 26, 1979, Colorado law enforcement officials visited Spring while he was in jail in Kansas City pursuant to his arrest on the firearms offenses. The officers gave Spring the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, and Spring again signed a written form indicating that he understood his rights and was willing to waive them. The officers informed Spring that they wanted to question him about the Colorado homicide. Spring indicated that he “wanted to get it off his chest.” In an interview that lasted approximately IV2 hours, Spring confessed to the Colorado murder. During that time, Spring <page-number citation-index="1" label="568">*568</page-number>talked freely to the officers, did not indicate a desire to terminate the questioning, and never requested counsel. The officers prepared a written statement summarizing the interview. Spring read, edited, and signed the statement.</p>
<p id="b722-5">Spring was charged in Colorado state court with first-degree murder. Spring moved to suppress both statements on the ground that his waiver of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights was invalid. The trial court found that the ATF agents’ failure to inform Spring before the March 30 interview that they would question him about the Colorado murder did not affect his waiver of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights:</p>
<blockquote id="b722-6">“[T]he questions themselves suggested the topic of inquiry. The questions dealt with ‘shooting anyone’ and specifically killing a man named Walker and throwing his body in a snowbank in Colorado. The questions were not designed to gather information relating to a subject that was not readily evident or apparent to Spring. Spring had been advised of his right to remain silent, his right to stop answering questions, and to have an Attorney present during interrogation. He did not elect to exercise his right to remain silent or to refuse to answer questions relating to the homicide, nor did he request Counsel during interrogation.” App. to Pet. for Cert. 4-A.</blockquote>
<p id="b722-7">Accordingly, the trial court concluded that the March 30 statement should not be suppressed on Fifth Amendment grounds. The trial court, however, subsequently ruled that Spring’s statement that he “shot another guy once” was irrelevant, and that the context of the discussion did not support the inference that the statement related to the Walker homicide. For that reason, the March 30 statement was not admitted at Spring’s trial. The court concluded that the May 26 statement “was made freely, voluntarily, and intelligently, after [Spring’s] being properly and fully advised of his rights, and that the statement should not be suppressed, but should <page-number citation-index="1" label="569">*569</page-number>be admitted in evidence.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span> </em>at 5-A. The May 26 statement was admitted into evidence at trial, and Spring was convicted of first-degree murder.<footnotemark>2</footnotemark></p>
<p id="b723-5">Spring argued on appeal that his waiver of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights before the March 30 statement was invalid because he was not informed that he would be questioned about the Colorado murder. Although this statement was not introduced at trial, he claimed that its validity was relevant because the May 26 statement that was admitted against him was the illegal “fruit” of the March 30 statement, see <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), and therefore should have been suppressed. The Colorado Court of Appeals agreed with Spring, holding that the ATF agents “had a duty to inform Spring that he was a suspect, or to readvise him of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, before questioning him about the murder.” <span class="citation" data-id="9790096"><a href="/opinion/2605185/people-v-spring/#966" aria-description="Citation for case: People v. Spring">671 P. 2d 965, 966</a></span> (1983). Because they failed to do so before the March 30 interview, “any waiver of rights in regard to questions designed to elicit information about Walker’s death was not given knowingly or intelligently.” <span class="citation" data-id="9790096"><a href="/opinion/2605185/people-v-spring/#967" aria-description="Citation for case: People v. Spring"><em>Id., </em>at 967</a></span>. The court held that the March 30 statement was inadmissible and that the State had failed to meet its burden of proving that the May 26 statement was not the product of the prior illegal statement. The court reversed Spring’s conviction and remanded the case for a new trial, directing that if the State sought to introduce the May 26 statement into evidence, the trial court should determine whether the “taint” of <page-number citation-index="1" label="570">*570</page-number>the March 30 statement was sufficiently attenuated to allow introduction of the May 26 statement.</p>
<p id="b724-5">The Colorado Supreme Court affirmed the judgment of the Court of Appeals, although its reasoning differed in some respects. <span class="citation" data-id="9562845"><a href="/opinion/1209392/people-v-spring/" aria-description="Citation for case: People v. Spring">713 P. 2d 865</a></span> (1985). The court found:</p>
<blockquote id="b724-6">“[T]he validity of Spring’s waiver of constitutional rights must be determined upon an examination of the totality of the circumstances surrounding the making of the statement to determine if the waiver was voluntary, knowing and intelligent. No one factor is always determinative in that analysis. Whether, and to what extent, a suspect has been informed or is aware of the subject matter of the interrogation prior to its commencement is simply one factor in the court’s evaluation of the total circumstances, although it may be a major or even a determinative factor in some situations.” <span class="citation" data-id="9562845"><a href="/opinion/1209392/people-v-spring/#872" aria-description="Citation for case: People v. Spring"><em>Id., </em>at 872-873</a></span> (citations omitted).</blockquote>
<p id="b724-7">The <em>court </em>concluded:</p>
<blockquote id="b724-8">“Here, the absence of an advisement to Spring that he would be questioned about the Colorado homicide, and the lack of any basis to conclude that at the time of the execution of the waiver, he reasonably could have expected that the interrogation would extend to that subject, <em>are </em>determinative factors in undermining the validity of the waiver.” <span class="citation" data-id="9562845"><a href="/opinion/1209392/people-v-spring/#874" aria-description="Citation for case: People v. Spring"><em>Id., </em>at 874</a></span> (emphasis in original).</blockquote>
<p id="b724-9">Justice Erickson, joined by Justice Rovira, dissented as to the resolution of this issue, stating:</p>
<blockquote id="b724-10">“Law enforcement officers have no duty under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>to inform a person in custody of all charges being investigated prior to questioning him. All that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requires is that the suspect be advised that he has the right <em>to </em>remain silent, that anything he says can and will be used against him in court, that he has the right to consult with a lawyer and to have the lawyer present during interrogation, and that if he cannot afford a law<page-number citation-index="1" label="571">*571</page-number>yer one will be appointed to represent him.” <em>Id., </em>at 880 (citations omitted).</blockquote>
<p id="b725-5">The dissenting justices found “ample evidence to support the trial court’s conclusion that Spring waived his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights” and rejected “the majority’s conclusion that Spring’s waiver of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights on March 30, 1979 was invalid simply because he was not informed of all matters that would be reviewed when he was questioned by the police.” <em>Id., </em>at 881. The court remanded the case for further proceedings consistent with its opinion.</p>
<p id="b725-6">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./476/1104/">476 U. S. 1104</a></span> (1986), to resolve an arguable Circuit conflict<footnotemark>3</footnotemark> and to review the Colorado Supreme Court’s determination that a suspect’s awareness of the possible subjects of questioning is a relevant and sometimes determinative consideration in assessing whether a waiver of the Fifth Amendment privilege is valid. We now reverse.</p>
<p id="b725-7">II</p>
<p id="b725-8">There is no dispute that the police obtained the May 26 confession after complete <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and after informing Spring that he would be questioned about the Colorado homicide. The Colorado Supreme Court nevertheless held that the confession should have been suppressed because it was the illegal “fruit” of the March 30 statement. A confession cannot be “fruit of the poisonous tree” if the tree itself is not <page-number citation-index="1" label="572">*572</page-number>poisonous. Our inquiry, therefore, centers on the validity of the March 30 statement.<footnotemark>4</footnotemark></p>
<p id="b726-4">A</p>
<p id="b726-5">The Fifth Amendment of the United States Constitution provides that no person “shall be compelled in any criminal case to be a witness against himself.”<footnotemark>5</footnotemark> This privilege “is fully applicable during a period of custodial interrogation.” <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#460" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 460-461</a></span>.<footnotemark>6</footnotemark> In <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>the Court concluded that “without proper safeguards the process of in-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual’s will to resist and to compel him to speak where he would not otherwise do so freely.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">Id., at 467</a></span>. Accordingly, the Court formulated the now-familiar “procedural safeguards effective to secure the privilege against self-incrimination.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 444</a></span>. The Court’s fundamental aim in designing the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings was “to assure that the individual’s right to choose between silence and speech remains unfettered throughout the interrogation process.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#469" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 469</a></span>.</p>
<p id="b726-6">Consistent with this purpose, a suspect may waive his Fifth Amendment privilege, “provided the waiver is made voluntarily, knowingly and intelligently.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 444</a></span>. In this case, the law enforcement officials twice informed Spring <page-number citation-index="1" label="573">*573</page-number>of his Fifth Amendment privilege in precisely the manner specified by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>As we have noted, Spring indicated that he understood the enumerated rights and signed a written form expressing his intention to waive his Fifth Amendment privilege. The trial court specifically found that “there was no element of duress or coercion used to induce Spring’s statements [on March 30, 1978].” App. to Pet. for Cert. 3-A. Despite the explicit warnings and the finding by the trial court, Spring argues that his March 30 statement was in effect compelled in violation of his Fifth Amendment privilege because he signed the waiver form without being aware that he would be questioned about the Colorado homicide. Spring’s argument strains the meaning of compulsion past the breaking point.</p>
<p id="b727-5">B</p>
<p id="b727-6">A statement is not “compelled” within the meaning of the Fifth Amendment if an individual “voluntarily, knowingly and intelligently” waives his constitutional privilege. <em>Miranda </em>v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Arizona, supra, </em>at 444</a></span>. The inquiry whether a waiver is coerced “has two distinct dimensions.” <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#421" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 421</a></span> (1986):</p>
<blockquote id="b727-7">“First the relinquishment of the right must have been voluntary in the sense that it was the product of a free and deliberate choice rather than intimidation, coercion, or deception. Second, the waiver must have been made with a full awareness both of the nature of the right being abandoned and the consequences of the decision to abandon it. Only if the ‘totality of the circumstances surrounding the interrogation’ reveal both an uncoerced choice and the requisite level of comprehension may a court properly conclude that the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights have been waived.” <em>Ibid, </em>(quoting <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#725" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 725</a></span> (1979)).</blockquote>
<p id="b727-8">There is no doubt that Spring’s decision to waive his Fifth Amendment privilege was voluntary. He alleges no “coer<page-number citation-index="1" label="574">*574</page-number>cion of a confession by physical violence or other deliberate means calculated to break [his] will,” <em>Oregon </em>v. <em>Elstad, </em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#312" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 312</a></span> (1985), and the trial court found none. His allegation that the police failed to supply him with certain information does not relate to any of the traditional indicia of coercion: “the duration and conditions of detention . . . , the manifest attitude of the police toward him, his physical and mental state, the diverse pressures which sap or sustain his powers of resistance and self-control.” <em>Culombe </em>v. <em>Connecticut, </em><span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#602" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568, 602</a></span> (1961) (opinion of Frankfurter, J.). Absent evidence that Spring’s “will [was] overborne and his capacity for self-determination critically impaired” because of coercive police conduct, <em>ibid.; </em>see <em>Colorado </em>v. <em>Connelly, </em><span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/#163" aria-description="Citation for case: Colorado v. Connelly">479 U. S. 157, 163-164</a></span> (1986), his waiver of his Fifth Amendment privilege was voluntary under this Court’s decision in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</em></p>
<p id="b728-5">There also is no doubt that Spring’s waiver of his Fifth Amendment privilege was knowingly and intelligently made: that is, that Spring understood that he had the right to remain silent and that anything he said could be used as evidence against him. The Constitution does not require that a criminal suspect know and understand every possible consequence of a waiver of the Fifth Amendment privilege. <em>Moran </em>v. <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#422" aria-description="Citation for case: Moran v. Burbine"><em>Burbine, supra, </em>at 422</a></span>; <em>Oregon </em>v. <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#316" aria-description="Citation for case: Oregon v. Elstad"><em>Elstad, supra, </em>at 316-317</a></span>. The Fifth Amendment’s guarantee is both simpler and more fundamental: A defendant may not be compelled to be a witness against himself in any respect. The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings protect this privilege by ensuring that a suspect knows that he may choose not to talk to law enforcement officers, to talk only with counsel present, or to discontinue talking at any time. The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings ensure that a waiver of these rights is knowing and intelligent by requiring that the suspect be fully advised of this constitutional privilege, including the critical advice that whatever he chooses to say may be used as evidence against him.</p>
<p id="b729-6"><page-number citation-index="1" label="575">*575</page-number>In this case there is no allegation that Spring failed to understand the basic privilege guaranteed by the Fifth Amendment. Nor is there any allegation that he misunderstood the consequences of speaking freely to the law enforcement officials. In sum, we think that the trial court was indisputably correct in finding that Spring’s waiver was made knowingly and intelligently within the meaning of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</em></p>
<p id="b729-7">hH b-1</p>
<p id="b729-1">A</p>
<p id="Apm">Spring relies on this Court’s statement in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>that “any evidence that the accused was threatened, tricked, or cajoled into a waiver will. . . show that the defendant did not voluntarily waive his privilege. ” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#476" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 476</a></span>. He contends that the failure to inform him of the potential subjects of interrogation constitutes the police trickery and deception condemned in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>thus rendering his waiver of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights invalid. Spring, however, reads this statement in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>out of context and without due regard to the constitutional privilege the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings were designed to protect.</p>
<p id="b729-2">We note first that the Colorado courts made no finding of official trickery.<footnotemark>7</footnotemark> In fact, as noted above, the trial court expressly found that “there was no element of duress or coercion used to induce Spring’s statements.” <em>Supra, </em>at 573. <page-number citation-index="1" label="576">*576</page-number>Spring nevertheless insists that the failure of the ATF agents to inform him that he would be questioned about the murder constituted official “trickery” sufficient to invalidate his waiver of his Fifth Amendment privilege, even if the official conduct did not amount to “coercion.” Even assuming that Spring’s proposed distinction has merit, we reject his conclusion. This Court has never held that mere silence by law enforcement officials as to the subject matter of an interrogation is “trickery” sufficient to invalidate a suspect’s waiver of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, and we expressly decline so to hold today.<footnotemark>8</footnotemark></p>
<p id="b730-5">Once <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings are given, it is difficult to see how official silence could cause a suspect to misunderstand the nature of his constitutional right — “his right to refuse to answer any question which might incriminate him.” <em>United States </em>v. Washington, <span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#188" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 188</a></span> (1977). “Indeed, it seems self-evident that one who is told he is free to refuse to answer questions is in a curious posture to later complain that his answers were compelled.” <em><span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/" aria-description="Citation for case: United States v. Washington">Ibid.</a></span> </em>We have held that a valid waiver does not require that an individual be informed of all information “useful” in making his decision or all information that “might . . . affec[t] his decision to confess.” <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#422" aria-description="Citation for case: Moran v. Burbine">475 U. S., at 422</a></span>. “[W]e have never read the Constitution to require that the police supply a suspect with a flow of information to help him calibrate his self-interest in <page-number citation-index="1" label="577">*577</page-number>deciding whether to speak or stand by his rights.” <em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">Ibid.</a></span></em><footnotemark><em>9</em></footnotemark><em> </em>Here, the additional information could affect only the wisdom of a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver, not its essentially voluntary and knowing nature. Accordingly, the failure of the law enforcement officials to inform Spring of the subject matter of the interrogation could not affect Spring’s decision to waive his Fifth Amendment privilege in a constitutionally significant manner.</p>
<p id="b731-10">B</p>
<p id="b731-11">This Court’s holding in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>specifically required that the police inform a criminal suspect that he has the right to remain silent and that <em>anything </em>he says may be used against him. There is no qualification of this broad and explicit warning. The warning, as formulated in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>conveys to a suspect the nature of his constitutional privilege and the consequences of.abandoning it. Accordingly, we hold that a suspect’s awareness of all the possible subjects of questioning in advance of interrogation is not relevant to determining whether the suspect voluntarily, knowingly, and intelligently waived his Fifth Amendment privilege.</p>
<p id="b731-12">f — I &lt;1</p>
<p id="b731-3">The judgment of the Colorado Supreme Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b731-4">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b721-7"> Under this Court’s decision in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), prior to a custodial interrogation a criminal suspect must “be warned that he has a right to remain silent, that any statement he does make may be used as evidence against him, and that he has a right to the presence of an attorney, either retained or appointed.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 444</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b723-6"> Spring also moved to suppress a third statement made on July 13, 1979, after he had pleaded guilty to the federal firearms offenses and after an information charging him with murder had been issued in Colorado. The Colorado Supreme Court unanimously concluded that the statement should be suppressed because the questioning officials made no effort “to reaffirm Spring’s decision to waive his constitutional rights after he declined to answer particular questions.” <span class="citation" data-id="9562845"><a href="/opinion/1209392/people-v-spring/#878" aria-description="Citation for case: People v. Spring">713 P. 2d 865, 878</a></span> (1985). We granted certiorari only on the question whether the second statement should have been admitted into evidence. <span class="citation multiple-matches"><a href="/c/U.%20S./476/1104/">476 U. S. 1104</a></span> (1986). Accordingly, the admissibility of the third statement is not before us.</p>
</footnote>
<footnote label="3">
<p id="b725-9"> The Colorado Supreme Court followed the lead of several Federal Courts of Appeals in holding that a suspect’s awareness of the subject matter of the interrogation is one factor to be considered in determining whether a waiver of the Fifth Amendment privilege is valid. <em>United States </em>v. <em>Burger, </em><span class="citation" data-id="431718"><a href="/opinion/431718/united-states-v-tibor-burger-aka-tom-singer/#141" aria-description="Citation for case: United States v. Tibor Burger, A/K/A &quot;Tom Singer&quot;">728 F. 2d 140, 141</a></span> (CA2 1984); <em>Carter </em>v. <em>Garrison, </em><span class="citation" data-id="392980"><a href="/opinion/392980/andrew-thomas-carter-sr-v-sam-p-garrison-attorney-general-of-the-state/#70" aria-description="Citation for case: Andrew Thomas Carter, Sr. v. Sam P. Garrison Attorney...">656 F. 2d 68, 70</a></span> (CA4 1981) <em>(per curiam), </em>cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./455/952/">455 U. S. 952</a></span> (1982); <em>United States </em>v. <em>McCrary, </em><span class="citation" data-id="9467693"><a href="/opinion/388110/united-states-v-billy-ray-mccrary/#328" aria-description="Citation for case: United States v. Billy Ray McCrary">643 F. 2d 323, 328</a></span> (CA5 1981). Other Courts of Appeals have found that a suspect’s awareness of the subject matter of interrogation is not a relevant factor in determining the validity of a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver. <em>United States </em>v. <em>Anderson, </em>175 U. S. App. D. C. 75, 77, n. 3, <span class="citation" data-id="334838"><a href="/opinion/334838/united-states-v-willie-anderson/#1212" aria-description="Citation for case: United States v. Willie Anderson">533 F. 2d 1210, 1212, n. 3</a></span> (1976); <em>United States </em>v. <em>Campbell, </em><span class="citation" data-id="291902"><a href="/opinion/291902/united-states-v-william-scott-campbell/#99" aria-description="Citation for case: United States v. William Scott Campbell">431 F. 2d 97, 99, n. 1</a></span> (CA9 1970).</p>
</footnote>
<footnote label="4">
<p id="b726-7"> The State argued for the first time in its petition for rehearing to the Colorado Supreme Court that this Court’s decision in <em>Oregon </em>v. <em>Elstad, </em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), renders the May 26 statement admissible without regard to the validity of the March 30 waiver. The Colorado Supreme Court noted that the State would be free to make this argument to the trial court on remand. <span class="citation" data-id="9562845"><a href="/opinion/1209392/people-v-spring/#876" aria-description="Citation for case: People v. Spring">713 P. 2d, at 876</a></span>. The question whether our decision in <em>Oregon </em>v. <em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span> </em>provides an independent basis for admitting the May 26 statement therefore is not before us in this case.</p>
</footnote>
<footnote label="5">
<p id="b726-9"> This privilege is applicable to the States through the Due Process Clause of the Fourteenth Amendment of the Constitution. <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964).</p>
</footnote>
<footnote label="6">
<p id="b726-10"> The State does not dispute that the statement at issue was obtained during a “custodial interrogation” within the meaning of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</em></p>
</footnote>
<footnote label="7">
<p id="b729-3"> The trial court found: “Though it is true that [the ATF agents] did not specifically advise Spring that a part of their interrogation would include questions about the Colorado homicide, the questions themselves suggested the topic of inquiry.” App. to Pet. for Cert. 4-A. According to the Colorado Supreme Court, “It is unclear whether Spring was told by the agents that they wanted to question him specifically about the firearms violations for which he was arrested or whether the agents simply began questioning Spring without making any statement concerning the subject matter of the interrogation. What is clear is that the agents did not tell Spring that they were going to ask him questions about the killing of Walker before Spring made his original decision to waive his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights.” <span class="citation" data-id="9562845"><a href="/opinion/1209392/people-v-spring/#871" aria-description="Citation for case: People v. Spring">713 P. 2d, at 871</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b730-6"> In certain circumstances, the Court has found affirmative misrepresentations by the police sufficient to invalidate a suspect’s waiver of the Fifth Amendment privilege. See, <em>e. g., Lynumn </em>v. <em>Illinois, </em><span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528</a></span> (1963) (misrepresentation by police officers that a suspect would be deprived of state financial aid for her dependent child if she failed to cooperate with authorities rendered the subsequent confession involuntary); <em>Spano </em>v. <em>New York, </em><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span> (1959) (misrepresentation by the suspect’s friend that the friend would lose his job as a police officer if the suspect failed to cooperate rendered his statement involuntary). In this case, we are not confronted with an affirmative misrepresentation by law enforcement officials as to the scope of the interrogation and do not reach the question whether a waiver of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights would be valid in such a circumstance.</p>
</footnote>
<footnote label="9">
<p id="b731-7"> Such an extension of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>would spawn numerous problems of interpretation because any number of factors could affect a suspect’s decision to waive his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. The requirement would also vitiate to a great extent the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rule’s important “virtue of informing police and prosecutors with specificity” as to how a pretrial questioning of a suspect must be conducted. <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#718" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 718</a></span> (1979).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Commonwealth v. Herlth.md  (`case`, 5 assertions)

### content_page

```
---
title: "Commonwealth v. Herlth"
type: case
citation: "2026 Pa. Super. 114 (2026)"
parallel_cite: ""
neutral_cite: 2026 Pa. Super. 114
court: Pennsylvania Superior Court
court_level: state
circuit: ""
year: 2026
date_decided: 2026-06-05
docket: 183 MDA 2024
authority_weight: "Persuasive — state, illustrative"
treatment:
  field_i_validity: good_law
  as_of_content: 2026-06-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Commonwealth v. Herlth
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10870804/com-v-herlth-j/"
  cluster_id: 10870804
  opinion_id: 11338267
  identity_checked: true
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Key — Progeny / Refinement"
related: ["[[Horton v. California]]", "[[Arizona v. Hicks]]", "[[Coolidge v. New Hampshire]]", "[[Caniglia v. Strom]]"]
aliases: ["Com. v. Herlth", "Commonwealth v. Herlth (Pa. Super. 2026)"]
tags: ["case", "fourth-amendment", "plain-view", "immediately-apparent", "closed-container", "pennsylvania", "state-appellate"]
holding: "A closed, opaque shoebox with a one-inch manufacturer's hole, inside a residence, retains a reasonable expectation of privacy; a trooper…"
lake:
  record_id: Commonwealth v. Herlth
  status: verified
  projected_at: 2026-07-09
---

# Commonwealth v. Herlth

*2026 PA Super 114 (Pa. Super. Ct. June 5, 2026)* · Pennsylvania Superior Court · **Persuasive — state, illustrative** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A state trooper entered Herlth's residence in a community-caretaking capacity while EMS treated Herlth for a drug overdose. Inside, the trooper saw a closed, opaque shoebox bearing a one-inch manufacturer's hole and shined a flashlight through the hole to view the contents — "scramble pills" — which became the basis for charges. Herlth moved to suppress; the trial court denied the motion and Herlth appealed.

## Issue
Whether the [[Plain View Doctrine|plain-view doctrine]] permitted the trooper to illuminate and view the interior of a closed, opaque container through a small hole, where the container's contents were not visible from a lawful vantage point.

## Rule
No. The [[Reading and Citing Cases#en-banc|en banc]] court restated the three-part plain-view test: "The plain view doctrine authorizes a warrantless seizure of evidence when (1) the police must observe the object from a lawful vantage point; (2) the incriminating character of the object must be immediately apparent; and (3) the police must have a lawful right of access to the object." — 2026 PA Super 114 (slip op., at 26) (quoting *Commonwealth v. Graham*, citing *Horton v. California*). ^pin-26

Applying it: "Trooper Adams failed to satisfy the second prong of the plain view test, because the object of the search, the closed shoebox, was not immediately incriminating in appearance. To the contrary, this container, a mere shoebox, appeared completely innocuous, so there was no reason to search inside it. In other words, Trooper Adams lacked probable cause to search the shoebox." — *Id.* (slip op., at [29](https://www.courtlistener.com/opinion/10870804/com-v-herlth-j/#:~:text=Trooper%20Adams%20failed%20to%20satisfy)). ^pin-29

The court rejected the "tiniest crack" theory: the Commonwealth's argument "would allow police officers to search the interior of any object from a lawful vantage point, so long as the object had even the tiniest crack or perforation. Precedent does not allow for such an unlawful intrusion." — *Id.* (slip op., at [31](https://www.courtlistener.com/opinion/10870804/com-v-herlth-j/#:~:text=tiniest%20crack)). ^pin-31

## Application
The trooper was lawfully in the living room, but the closed opaque shoebox was innocuous on its face; its incriminating character was not immediately apparent without the additional act of shining a flashlight through the manufacturer's hole. Because that additional step was itself a search the [[Plain View Doctrine|plain-view doctrine]] could not justify, and the trooper had neither a warrant nor probable cause to open the box, the search of the shoebox was unlawful on these facts.

## Conclusion
The flashlight-aided search of the closed shoebox exceeded the plain-view exception; the Superior Court held the trial court erred in denying suppression and reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Persuasive — state, illustrative** (Pennsylvania Superior Court, [[Reading and Citing Cases#en-banc|en banc]]). A recent state decision applying the immediately-apparent and lawful-access prongs of [[Horton v. California]] / [[Arizona v. Hicks]] to a closed container.

## Appears on
- [[Plain View Doctrine]] — *Key — Progeny / Refinement*

## Sources
- *Commonwealth v. Herlth*, 2026 PA Super 114 (Pa. Super. Ct. June 5, 2026) (en banc) — https://www.courtlistener.com/opinion/10870804/com-v-herlth-j/ — pinpoints: slip op., at 26, 29, 31 (CL carries the slip opinion, paginated as the Superior Court slip; cluster 10870804 → lead opinion 11338267).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fd66f1d72f53f51c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "2026 Pa. Super. 114 (2026)", "court": "Pennsylvania Superior Court", "neutral_cite": "2026 Pa. Super. 114", "official_citation_present": true, "parallel_cite": "", "title": "Commonwealth v. Herlth", "year": "2026"}}
{"assertion_id": "2efd4fda539b4c03", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A closed, opaque shoebox with a one-inch manufacturer's hole, inside a residence, retains a reasonable expectation of privacy; a trooper…", "title": "Commonwealth v. Herlth"}}
{"assertion_id": "894fad99baf3e76d", "dimension": "support", "kind": "home_role", "locator": {"home": "Plain View Doctrine"}, "payload": {"home": "Plain View Doctrine", "role": "Key — Progeny / Refinement", "title": "Commonwealth v. Herlth"}}
{"assertion_id": "ae0f48428dbecdfd", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2026-06-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Commonwealth v. Herlth", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Commonwealth v. Herlth", "varies_by_point": "false"}}
{"assertion_id": "fb5d05eec5860568", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Persuasive — state, illustrative", "title": "Commonwealth v. Herlth"}}
```

### lake record — Commonwealth v. Herlth

```json
{
  "schema_version": "s2.v1",
  "record_id": "Commonwealth v. Herlth",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Com. v. Herlth, J.",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "Commonwealth v. Herlth",
    "court": "Pennsylvania Superior Court",
    "court_id": "pasuperct",
    "court_level": "state",
    "circuit": null,
    "state": null,
    "date_decided": "2026-06-05",
    "year": 2026,
    "docket": "183 MDA 2024",
    "cluster_id": 10870804,
    "lead_opinion_id": 11338267,
    "sibling_ids": [
      11338267,
      11338268
    ],
    "absolute_url": "/opinion/10870804/com-v-herlth-j/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "2026 Pa. Super. 114",
      "volume": "2026",
      "reporter": "Pa. Super.",
      "page": "114",
      "type": 8,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2026 Pa. Super. 114",
        "volume": "2026",
        "reporter": "Pa. Super.",
        "page": "114",
        "type": 8,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "2026 Pa. Super. 114",
        "volume": "2026",
        "reporter": "Pa. Super.",
        "page": "114",
        "type": 8,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "2026 Pa. Super. 114",
    "official_selection": {
      "court_class": "state",
      "selected": "2026 Pa. Super. 114",
      "reason": "selected_rank_3"
    }
  },
  "pinpoints": [
    {
      "id": "pin-26",
      "page": null,
      "quote": "\u2014 which became the basis for charges. Herlth moved to suppress; the trial court denied the motion and Herlth appealed. ## Issue Whether the plain-view doctrine permitted the trooper to illuminate and view the interior of a closed, opaque container through a small hole, where the container's contents were not visible from a lawful vantage point. ## Rule No. The en banc court restated the three-part plain-view test:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-29",
      "page": null,
      "quote": "Trooper Adams failed to satisfy the second prong of the plain view test, because the object of the search, the closed shoebox, was not immediately incriminating in appearance. To the contrary, this container, a mere shoebox, appeared completely innocuous, so there was no reason to search inside it. In other words, Trooper Adams lacked probable cause to search the shoebox.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 49513,
      "fragment": "#:~:text=Trooper%20Adams%20failed%20to%20satisfy",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-31",
      "page": null,
      "quote": "tiniest crack",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 52854,
      "fragment": "#:~:text=tiniest%20crack",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2026-06-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Commonwealth v. Herlth",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(11338267 OR 11338268) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR pa OR pasuperct OR pacommwct)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(11338267 OR 11338268)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(11338267 OR 11338268)",
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
    "complete_query": "cites:(11338267 OR 11338268)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 11338267,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 11338268,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/commonwealth-v-herlth.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 11338268,
        "cited_id": 148417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 1508320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 2104711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 9423752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 9429131,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 9432041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 9534347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 9692042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 9759249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 9854442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 9888627,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 148417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 856347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1169275,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1183387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1206533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1354211,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1460504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1494964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1508320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1521287,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1993436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 2107943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 2149587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 2367721,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 2981297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 4710946,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 4968781,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 4969273,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 5128806,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 5132906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 8410300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9423552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9423752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9427853,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9429131,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9429812,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9430502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9430862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9430865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9432041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9432823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9460223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9534347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9554002,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9629612,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9634816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9635383,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9702263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9759249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9805406,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9854442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9887288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9888754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 10746023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 10794952,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 10802947,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "C",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T01:42:17Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T01:42:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T01:42:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T01:42:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T01:42:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Commonwealth v. Herlth

```
J-E03003-25

                               2026 PA Super 114

 COMMONWEALTH OF PENNSYLVANIA            :   IN THE SUPERIOR COURT OF
                                         :        PENNSYLVANIA
                                         :
              v.                         :
                                         :
                                         :
 JAMES LEE HERLTH                        :
                                         :
                   Appellant             :   No. 183 MDA 2024

     Appeal from the Judgment of Sentence Entered December 7, 2023
               In the Court of Common Pleas of York County
             Criminal Division at No: CP-67-CR-0005812-2022

BEFORE: BOWES, J., OLSON, J., STABILE, J., DUBOW, J., KUNSELMAN, J.,
        NICHOLS, J., MURRAY, J., McLAUGHLIN, J., and BECK, J.

OPINION BY STABILE, J.:                              FILED: JUNE 5, 2026

     Appellant, James Lee Herlth, appeals from his judgment of sentence of

7-14 years’ imprisonment for possession of controlled substances with intent

to deliver (“PWID”). Appellant contends that the trial court erred by denying

his motion to suppress evidence that a state trooper found during a

warrantless search of a shoebox in Appellant’s residence. We conclude that

(1) Appellant had a reasonable expectation of privacy in the contents of the

shoebox; (2) the trooper conducted a search by shining a flashlight into a

small hole in the shoebox, and (3) the search was improper under the

community caretaking and plain view exceptions to the Fourth Amendment.

We reverse the order denying suppression, vacate Appellant’s judgment of

sentence and remand for further proceedings.

     On August 31, 2020, the Pennsylvania State Police filed a criminal

complaint against Appellant charging him with PWID under 35 P.S. § 780-
J-E03003-25



113(a)(30).     On March 16, 2023, the court presided over a suppression

hearing in which the sole witness was Trooper Dylan Adams.

       Trooper Adams testified that he had been a trooper with the

Pennsylvania State Police for about six years. N.T., 3/16/23, at 4. On August

31, 2020, the trooper was on duty conducting a patrol to respond to calls in

the area. Id. At around 5:00 a.m., he responded to a report of an overdose

at 138 East Broadway in Red Lion, Pennsylvania.1 Id. This address was a

duplex, a “single building with two doors.” Id. at 5. The trooper entered one

of the doors into a living room. Three EMS paramedics were already there

providing emergency care to Appellant for an overdose. Id. at 11. The living

room was small, so the trooper could only stand in one spot and spin around

in a circle. Id. at 6.

       Trooper Adams testified that he was present to provide security to EMS

personnel because some overdose patients become violent when they are

revived with Narcan. Id. at 10. When asked whether he was assisting in any

medical capacity, Trooper Adams responded, “No, I was not. I’m not medically

trained like EMS are. We allow them to do this job.” Id. He also testified,

“We go there to see what [the patient] overdosed on to possibly make an

investigation further, anything that’s in plain view that we can see.” Id.

____________________________________________


1 The trial court did not make any findingof fact whether this address was
Appellant’s residence. Id. at 26-27 (announcement of court’s decision). The
Commonwealth acknowledges, however, that this was Appellant’s residence,
Commonwealth’s Brief at 8, 12, 22, so we will accept this as true for purposes
of this opinion.

                                           -2-
J-E03003-25



       While standing at Appellant’s feet, Trooper Adams saw a shoebox with

a closed lid.2 Id. at 6. The shoebox was “maybe not even a foot away from

me. It was sitting right next to my left leg.” Id.

       The closed shoebox had a one-inch3 manufacturer’s hole. Trooper

Adams shined his flashlight into the hole and recognized “scramble” capsules,

a narcotic consisting normally of “a mixture of different drugs but mostly

fentanyl.” Id. at 5. The scramble was directly under the hole through which

he shined his flashlight. Id. at 7. The Commonwealth does not claim that

Trooper Adams could have seen the scramble without a flashlight.         See

Commonwealth’s Brief at 19 (“all Trooper Adams needed to do in order to see

the scramble pills in the shoebox was look down and shine a flashlight through

the manufacturers’ hole”) (emphasis added). Nor does the record indicate

that the living room was dark or that a flashlight was necessary to see inside

the living room.

       It “made sense” to Trooper Adams that Appellant overdosed on

scramble. N.T., 3/16/23, at 7. He “opened the [shoe]box and seized [its

contents],” id., 117 scramble capsules in a plastic bag. Id. at 9.

____________________________________________


2 The trial court did not make any finding of fact as to whether the shoebox

belonged to Appellant. N.T., 3/16/23, at 26-27.             The Commonwealth
acknowledges, however, that the shoebox belonged to Appellant and that the
box was located where Appellant chose to place it. Commonwealth’s Brief at
13 (Appellant “placed the box. . . in the middle of his living room”).

3 Although Trooper Adams did not testify that the hole was one inch, the court

stated that the hole was one inch. Id. at 27. Furthermore, both parties assert
in their briefs that the hole was one inch.

                                           -3-
J-E03003-25



      At the conclusion of the suppression hearing, the Commonwealth argued

that Trooper Adams conducted a valid search under the plain view doctrine.

Id. at 24-26.    The trial court denied Appellant’s motion to suppress the

evidence seized from the shoebox. Id. at 26-27. The court did not find or

address whether the trooper shined his flashlight into the shoebox to help EMS

personnel provide medical assistance to Appellant.      The court simply ruled

that the trooper performed a valid search under the plain view doctrine. Id.

      A jury found Appellant guilty of PWID, and on December 7, 2023, the

court entered sentence.    On Monday, December 18, 2023, Appellant filed

timely post-sentence motions. On January 5, 2024, the court denied these

motions. On February 1, 2024, Appellant filed a timely notice of appeal. Both

Appellant and the trial court complied with Pa.R.A.P. 1925.

      Appellant raises a single issue in this appeal:

      The trial court erred when it denied Appellant’s motion to suppress
      evidence because the drugs and cash found in a closed shoebox
      in Appellant’s home were not in plain view. The officer’s use of a
      flashlight to illuminate the inside of the closed shoebox through a
      manufacturer’s hole in the box to identify the contraband was a
      search without probable cause and no exception to the warrant
      requirement applied. The search violated Appellant’s rights under
      the 4th Amendment to the U.S. Constitution and Article I, Section
      8 of the Pennsylvania Constitution.

Appellant’s Brief at 4.

      In reviewing the denial of a suppression motion,

      we are limited to determining whether the suppression court’s
      factual findings are supported by the record and whether the legal
      conclusions drawn from those facts are correct. Thus, [the]
      review of questions of law is de novo. [The] scope of review is to

                                     -4-
J-E03003-25


     consider only the evidence of the Commonwealth and so much of
     the evidence for the defense as remains uncontradicted when read
     in the context of the suppression record as a whole.

Commonwealth v. Shaffer, 653 Pa. 258, 209 A.3d 957, 968–69 (Pa. 2019).

     The Fourth Amendment provides, “The right of the people to be secure

in their persons, houses, papers, and effects, against unreasonable searches

and seizures, shall not be violated. . .”    U.S. Const., amend. IV.     “The

touchstone of Fourth Amendment analysis is whether a person has a

‘constitutionally protected reasonable expectation of privacy.’” California v.

Ciraolo, 476 U.S. 207, 211, 106 S.Ct. 1809, 90 L.Ed.2d 210 (1986) (quoting

Katz v. United States, 389 U.S. 347, 360, 88 S.Ct. 507, 19 L.Ed.2d 576

(1967) (Harlan, J., concurring)). “Protection of reasonable expectations of

privacy is the primary purpose of the prohibition against unreasonable

searches and seizures.” Commonwealth v. Saunders, 326 A.3d 888, 896

(Pa. 2024) (cleaned up). A search or seizure conducted without a warrant is

presumptively unreasonable, subject to a few specifically established, well-

delineated exceptions. Id.

     We begin by examining whether Appellant had a reasonable expectation

of privacy in the shoebox, an issue disputed by the parties to this appeal. A

person who challenges a search or seizure on Fourth Amendment grounds

must demonstrate (1) that he had a subjective expectation of privacy, and (2)

that his subjective expectation of privacy is one that society is prepared to

recognize as reasonable and legitimate. Commonwealth v. Perel, 107 A.3d

185, 188 (Pa. Super. 2014). The Fourth Amendment


                                    -5-
J-E03003-25


     protects the individual’s privacy in a variety of settings. In none
     is the zone of privacy more clearly defined than when bounded by
     the unambiguous physical dimensions of an individual’s home—a
     zone that finds its roots in clear and specific constitutional terms:
     ‘The right of the people to be secure in their . . . houses . . . shall
     not be violated.’

Payton v. New York, 445 U.S. 573, 589, 100 S.Ct. 1371, 63 L.Ed.2d 639

(1980); see also Florida v. Jardines, 569 U.S. 1, 6, 133 S.Ct. 1409, 185

L.Ed.2d 495 (2013) (“when it comes to the Fourth Amendment, the home is

first among equals”). In addition, “what a person knowingly exposes to the

public, even in his own home or office, is not a subject of Fourth Amendment

protection.” Katz, 389 U.S. at 351 (majority opinion).

     It also is well settled that “[t]he Fourth Amendment provides protection

to the owner of every container that conceals its contents from plain view.”

New Jersey v. T.L.O., 469 U.S. 325, 337 (1985). “An understanding that

personal, private effects are commonly stored in purses, backpacks, luggage,

and duffel bags can be gleaned from a casual stroll down any sidewalk. The

contents of persons’ closed containers are obscured from public view and

generally are recognized as private.” Perel, 107 A.3d at 190.

     Based on Appellant’s right to be secure in his residence, Payton,

Jardines, and the protection provided to him as an owner of the closed

shoebox, T.L.O., Perel, Appellant had a reasonable expectation of privacy in

the shoebox found in his residence.         The Commonwealth contends that

Appellant lacked a reasonable expectation of privacy because he placed the

closed shoebox in the middle of his living room, where guests were most likely

                                      -6-
J-E03003-25


to see it, instead of his bedroom. Commonwealth’s Brief at 13, 15, 65. The

plain language of the Fourth Amendment, however, guarantees an individual’s

right to be secure in his “house”. This right extends to his entire house, not

merely his bedroom, Payton, Jardines, and to the curtilage of the house as

well. Commonwealth v. Bowmaster, 101 A.3d 789, 792 (Pa. Super. 2014).

The fact that Appellant placed the closed container in his living room does not

mean that he exposed its contents to the public.

      The Commonwealth also argues that the one-inch manufacturer’s hole

“render[ed] the shoebox, even when the lid [was] shut, more analogous to an

open or clear container than a closed container,” Commonwealth’s Brief at 8,

making its contents visible to any “casual observer” and leaving Appellant

without any reasonable expectation of privacy.         Id. at 12, 16 (citing

Commonwealth v. Heidelberg, 267 A.3d 492, 504 (Pa. Super. 2021) (no

reasonable expectation of privacy in clear plastic baggies left in plain view in

automobile). We do not consider Trooper Adams’ inspection of the shoebox

“casual observation.” The contents of the shoebox were not visible to the

naked eye; Trooper Adams had to use a flashlight to peer inside the shoebox

and discern its contents.    The fact that the lid was closed indicates that

Appellant intended to “conceal its contents from plain view.” T.L.O., Perel,

supra. We therefore conclude that Appellant in fact possessed a reasonable

expectation of privacy in the shoebox whose contents were not open or visible

to any “casual observer”.


                                     -7-
J-E03003-25


      Having determined that Appellant had an expectation of privacy in the

contents of the shoe box, we next examine whether Trooper Adams performed

a search of the shoebox. The Commonwealth argues that he did not:

      Trooper Adams, from a lawful vantage point in [Appellant’s]
      residence pursuant to the emergency aid exception, merely shined
      his flashlight into the manufacturer’s hole of a shoebox laying
      beside [Appellant]. He did not manipulate or disturb the shoebox
      in any way prior to illuminating it with his flashlight. He didn’t
      even need to bend over or maneuver his body in any way to
      recognize the illuminated contraband through the manufacturer’s
      hole in the shoebox … [T]rooper Adams’ mere use of a flashlight
      was not a search.

Commonwealth’s Brief at 22.

      We disagree. Trooper Adams’ act of shining a flashlight into the hole of

the closed shoebox was a search. “A search takes place when police intrude

upon a constitutionally protected area without the individual’s explicit or

implicit permission.” Commonwealth v. Prater, 256 A.3d 1274, 1286 (Pa.

Super. 2021) (citing Jardines, 569 U.S. at 6). “[I]f contraband is left in open

view and is observed by a police officer from a lawful vantage point, there has

been no invasion of a legitimate expectation of privacy and thus no ‘search’

within the meaning of the Fourth Amendment—or at least no search

independent of the initial intrusion that gave the officers their vantage point.”

Minnesota v. Dickerson, 508 U.S. 366, 375, 113 S.Ct. 2130, 124 L.Ed.2d

334 (1993).

      Trooper Adams was inside Appellant’s residence for a proper reason,

namely, to provide security to EMS personnel while they provided medical


                                      -8-
J-E03003-25


treatment to Appellant. Thus, the trooper viewed the shoebox from a lawful

vantage point inside Appellant’s living room.     At that point, however, he

performed a search by shining a flashlight into a small hole of a closed

container found inside the living room, a “constitutionally protected area” in

which Appellant had a reasonable expectation of privacy. Prater, 256 A.3d

at 1286.

      We are not aware of any Pennsylvania decision that addresses whether

a law enforcement officer conducts a search by shining a flashlight inside a

residence into a small hole of a closed container. Although the parties refer

us to two Pennsylvania cases in which police officers used technological aids

outside of residences to inspect residential interiors, the facts in those cases

bear little resemblance to the present case.        See Commonwealth v.

Lemanski, 529      A.2d 1085     (Pa. Super. 1987); Commonwealth v.

Gindlesperger, 560 Pa. 222, 743 A.2d 898 (1998).

      In Lemanski, police observed marijuana growing in a secluded

greenhouse approximately 200 feet from the road by finding an opening in

the brush and shrubbery along the property line of the house and using

binoculars and a zoom lens through the opening. We held that the search

violated the Fourth Amendment, because the police infringed upon the

homeowner’s reasonable expectation of privacy by peering through a hole in

the shrubbery with sophisticated technology from a distance of 200 feet. Id.,

529 A.2d at 1092-93. Subsequently, in Gindlesperger, the police received


                                     -9-
J-E03003-25


tips from a confidential informant that the defendant was growing marijuana

in his basement with artificial lighting. The police used an infrared imaging

device called a “WASP” to detect the presence of unexplained heat emanating

from the basement.4 They then obtained a search warrant that resulted in

seizure of marijuana from the basement. Our Supreme Court held that use of

the WASP ran afoul of the Fourth Amendment by violating the defendant’s

reasonable expectation of privacy “in the heat-generating activities occurring

within his home.” Id., 743 A.2d at 903. We do not consider these decisions

on point, because the vantage point for the searches in these cases was

outside the residence instead of inside, and the technology used in these cases

was far more sophisticated than the flashlight herein.5

       In our view, the most persuasive decisions on the issue before us are

from other jurisdictions: State v. Tarantino, 322 N.C. 386, 368 S.E.2d 588

(1988), and People v. Hagestedt, 2025 IL 130286, 270 N.E.3d 334 (2025).6

____________________________________________


4 The opinion in Gindlesperger does not explicitly state that the police were

outside the defendant’s residence at the time they used the WASP, but it is
reasonable to infer this from the circumstances of the case. Had they been
inside the residence, they could have viewed the plants with their own eyes
and would not have needed to use the WASP.

5 The Commonwealth cites many other cases for the proposition that Trooper

Adams did not perform a search. We discuss these cases, infra.

6 “When confronted with a question heretofore unaddressed by the courts of

this Commonwealth, we may turn to the courts of other jurisdictions.
Although we are not bound by those decisions, we may use decisions from
other jurisdictions for guidance to the degree we find them useful and not
(Footnote Continued Next Page)


                                          - 10 -
J-E03003-25


       In Tarantino, a police detective (Detective Baker) received a tip that

marijuana plants were growing inside a building. The front door of the building

was padlocked, the back doors were nailed shut, and the windows were

boarded up. There were, however, quarter-inch cracks in a wall left uncovered

by wooden boarding. Detective Baker shined a flashlight through the cracks

and saw marijuana plants.          He obtained a search warrant and seized the

marijuana.

       The trial court granted Tarantino’s motion to suppress on the ground

that Detective Baker conducted a search with his flashlight that violated his

Fourth Amendment rights. The North Carolina Supreme Court affirmed. The

court distinguished Tarantino’s case from United States v. Dunn, 480 U.S.

294, 107 S.Ct. 1134, 94 L.Ed.2d 326 (1987), in which DEA agents shined

flashlights into an “essentially open front” of the defendant’s barn7 and saw a

drug laboratory. Id. at 305. The Dunn court held that the DEA agents did

not violate the Fourth Amendment because the barn’s interior was exposed to

the public from an unprotected vantage point. Id. at 304-05. The officers

were not required to “shield their eyes” from that which was exposed to public

view. Id. at 304. In contrast,


____________________________________________


incompatible with Pennsylvania law.” Commonwealth v. Choice, 345 A.3d
719, 733 n.18 (Pa. Super. 2025).

7 There was a locked waist-high gate barring entry into the barn proper, but

the interior of the barn was visible because there only was netting material
between the top of the gate and the ceiling. Id., 480 U.S. at 297.

                                          - 11 -
J-E03003-25


     [Tarantino] had a reasonable expectation of privacy in the building
     which Detective Baker inspected. The building’s padlocked front
     door, nailed back doors, and boarded windows indicate that
     [Tarantino] had a subjective expectation of privacy in his
     building’s interior. This expectation was not unreasonable even
     though there were small cracks between the boards in the
     building’s back wall. The presence of tiny cracks near the floor on
     the interior wall of a second-floor porch is not the kind of exposure
     which serves to eliminate a reasonable expectation of privacy. To
     hold otherwise would result in an unfairly exacting standard. It
     would require owners of non-residential buildings who want to
     enjoy their Fourth Amendment rights to maintain their structures
     almost as airtight containers. The Supreme Court has never
     imposed such a standard, and we decline to do so in this case.

     Nothing in the Supreme Court’s Dunn decision suggests that an
     expectation of privacy is eliminated by quarter-inch cracks in the
     back wall of an otherwise sealed building. The inquiry in Dunn
     centered on the Fourth Amendment’s requirements when law
     enforcement officials are faced with an open barn front obstructed
     only with see-through netting. The barn’s interior was fully
     exposed to anyone standing next to the netting…

     By contrast, in the instant case, Detective Baker confronted a
     nearly solid wall when he entered [Tarantino]’s porch. Boarded
     windows and nailed doors prohibited observation of the inside
     from all but the most rigorous scrutiny. To make his observations,
     Detective Baker had to bend and peer with a flashlight through
     quarter-inch cracks near the floor. Nothing indicates, as in Dunn,
     that had Detective Baker conducted his investigation during the
     day he could have viewed the building’s interior without making
     the same searching inquiry. These facts distinguish this case from
     Dunn in a constitutionally significant way. Far from demanding
     Detective Baker to avert his eyes to avoid viewing the building’s
     interior, the cracks near the porch floor required him to make a
     probing examination in order to see inside. Under these
     circumstances [Tarantino]’s reasonable expectation of privacy
     remained intact.

Id., 368 S.E.2d at 591-92.

     The Tarantino court further observed:




                                    - 12 -
J-E03003-25


      Our decision is consistent with those of other jurisdictions. In
      United States v. Bradshaw, the Fourth Circuit held that the
      defendant’s reasonable expectation of privacy in his truck’s
      interior was not eliminated by the presence of a crack where the
      back doors did not fit snugly. 490 F.2d 1097, 1101 (4th Cir.)…
      The court concluded that police officers violated the Fourth
      Amendment when they looked through the crack without a
      warrant, saw moonshine whiskey jugs, and seized them. The
      court acknowledged that the officers had a right to approach and
      stand next to the truck, but it concluded they went beyond lawful
      investigation when peering through the small space. Id. In State
      v. Kaaheena, the Hawaii Supreme Court concluded the
      defendant’s Fourth Amendment rights were violated when the
      police stood on a crate and looked through a one-inch hole in the
      drapes and blinds of a building which housed a “commercial
      establishment and some rental apartments.” 59 Haw. 23, 575
      P.2d 462, 466 (1978).          Although the police made their
      observations from a public vantage point, the court held that the
      search was impermissible because the defendant maintained his
      reasonable expectation of privacy in the building’s interior. Id.,
      575 P.2d at 467; see also Kroehler v. Scott, 391 F.Supp. 1114
      (E.D.Pa.1975) (violation of Fourth Amendment for officers to peer
      through small ceiling vents); Lorenzana v. Superior Court of
      Los Angeles County, 9 Cal.3d 626, 108 Cal.Rptr. 585, 511 P.2d
      33 (1973) (officers violated Fourth Amendment by peering
      through drawn curtains); People v. Triggs, 8 Cal.3d 884, 106
      Cal.Rptr. 408, 506 P.2d 232 (1973) (illegal search where officers
      in maintenance access area peered through vents); People v.
      Lovelace, 116 Cal.App.3d 541, 172 Cal.Rptr. 65 (1981)
      (reasonable expectation of privacy not eliminated by knotholes
      and cracks in six foot high wooden fence); State v. Biggar, 716
      P.2d 493 (1986) (reasonable expectation of privacy not eliminated
      by crack one half to one inch wide where toilet stall door did not
      close properly).

Id. at 592-93 (cleaned up).

      The critical point in Tarantino was that a small hole in an otherwise

closed building does not defeat the defendant’s reasonable expectation of

privacy in the building’s interior.    Police intrusion into such an area via

flashlight constitutes a search under the Fourth Amendment. Analogously, a

                                      - 13 -
J-E03003-25


small hole in a closed container inside an individual’s residence does not defeat

his reasonable expectation of privacy in the container.          Thus, shining a

flashlight into the hole, as Trooper Adams did here, constitutes a search.

      Hagestedt is equally as persuasive as Tarantino. Police officers in

Hagestedt entered the defendant’s residence without a warrant to assist the

fire department in investigating a reported gas leak.         One of the officers

examined the stove and saw no damage. He observed a cabinet across from

the stove that was secured shut with a chain and padlock. The cabinet was

ajar about one inch. The officer shined his flashlight through the gap and saw

marijuana in a container inside the cabinet. Id., 270 N.E.3d at 338. A second

officer pulled on the cabinet door handles, and the doors opened another inch

or two. Id. at 339. The second officer looked inside and saw marijuana inside

a container. Id. The trial court denied the defendant’s motion to suppress.

The court held that the first officer’s act of shining a flashlight was valid under

the plain view doctrine. Id. The court ruled that the second officer’s act of

pulling the cabinet open further constituted an illegal search in violation of the

Fourth Amendment, but the error was harmless because the first officer had

spotted marijuana during the flashlight search.         Id.   Subsequently, the

defendant was convicted of possession of a controlled substance.

      The Illinois Supreme Court held that the defendant had a reasonable

expectation of privacy in the cabinet. Id. at 343 (“[b]y chaining and locking

a cabinet in his kitchen, defendant took actions to protect his privacy and had


                                      - 14 -
J-E03003-25


shown that he sought to preserve the contents of the cabinet as

private…Society recognizes as reasonable a defendant’s expectation of privacy

in items concealed from plain view in closed containers, especially in a

defendant’s own home”). The court cited Tarantino for the principle that “a

defendant’s reasonable expectation of privacy is not eliminated by small

openings in otherwise closed areas.” Id. at 347.

      The court also held that the officers performed a search of the cabinet.

The court found instructive the United States Supreme Court’s analysis in

Arizona v. Hicks, 480 U.S. 321, 107 S.Ct. 1149, 94 L.Ed.2d 347 (1987). In

Hicks, police officers responded to the defendant’s apartment after a bullet

was fired through the floor of his apartment, striking and injuring a man in

the apartment below. Police officers entered the apartment, searching for the

shooter, other victims, and weapons. While in the apartment, one of police

officers noticed expensive stereo components that seemed out of place. The

officer moved some of the components and read and recorded their serial

numbers. One item was seized immediately as stolen, while the remaining

components were seized later pursuant to a warrant. The defendant filed a

motion to suppress all seized evidence.        The trial court suppressed the

evidence, and a state appellate court affirmed, finding that the officer’s act of

obtaining the serial numbers was an additional search unrelated to the exigent

circumstance of the shooting. The United States Supreme Court affirmed.

The Court reasoned that merely inspecting the parts of the stereo components


                                     - 15 -
J-E03003-25


that were visible, while lawfully in the apartment, would not be an independent

search because “it would have produced no additional invasion of defendant’s

privacy interest.” Id. at 325. When the officer moved one of the components

to view a concealed serial number, however, he conducted a search. Id. at

324-25 (“taking action, unrelated to the objectives of the authorized intrusion,

which exposed to view concealed portions of the apartment or its contents,

did produce a new invasion of defendant’s privacy unjustified by the exigent

circumstance that validated the entry”).

      The Illinois court emphasized that although Hicks concerned stereo

equipment that was moved to expose the serial number, its holding was not

limited to whether the components were moved. Instead, said the Illinois

court, Hicks found that there was a new invasion of the defendant’s privacy

when the officer took action that was “unrelated to the objectives of the

authorized intrusion.” Hagestedt, 270 N.E.3d at 345-46 (citing Hicks, 480

U.S. at 325).

      The Hagestedt court held that the officer who shined a flashlight into

the kitchen cabinet, like the officer in Hicks, took action that was unrelated

to the original objective for entering the defendant’s house.      The original

reason for entering the house, investigation of a reported gas leak, was a

proper community caretaking or public safety exception to the Fourth

Amendment. Id. at 344. By shining a flashlight into the cabinet, however,

the officer “took deliberate action that was unrelated to his authorized


                                     - 16 -
J-E03003-25


intrusion[,] [and this] constituted an independent search.” Id. at 347. The

court elaborated:

      While the cabinet itself was in plain view, its contents were not.
      The cabinet was secured with a chain and a padlock, and the chain
      was wrapped tightly around the cabinet handles. Neither [officer]
      observed the contents of the cabinet prior to taking any action.
      [The second officer’s] action was to open the doors further, which
      the trial court correctly determined was a search. [The first
      officer’s] action was to use his flashlight and an angled view
      through a small gap in an otherwise closed and locked cabinet.
      There was also no evidence that the gas leak was potentially
      coming from the locked cabinet…Thus, [the first officer] was not
      looking for a gas leak in the cabinet, nor was the cabinet
      proximate to the stove so that the use of a flashlight to illuminate
      behind the stove would have illuminated the interior of the
      cabinet. There was no testimony that the flashlight in this case
      was necessary to investigate the gas leak…Rather, the officer saw
      an admittedly suspicious cabinet, locked with a chain, and used
      his flashlight to try to see in through a small gap.

Id. at 347-48.

      Trooper Adams’ conduct was similar to the conduct of the officer in

Hagestedt who shined a flashlight into the kitchen cabinet. The officer in

Hagestedt properly entered the defendant’s residence due to an emergency

(the gas leak), but his act of shining a flashlight into the kitchen cabinet was

“unrelated to his authorized intrusion” and thus constituted an independent

search. Hagestedt, 270 N.E.3d at 347. Similarly, Trooper Adams properly

entered Appellant’s residence due to an emergency (Appellant’s overdose),

but his act of shining his flashlight into a hole in the shoebox was unrelated to

“the objectives of [his] authorized intrusion.” Id. Shining his flashlight thus




                                     - 17 -
J-E03003-25


constituted “an independent search,” id., into an area where Appellant

enjoyed a reasonable expectation of privacy. Id. at 343.

      The decisions cited by the Commonwealth for the proposition that

Trooper Adams did not perform a search, see Commonwealth’s Brief at 21-

32, are distinguishable, because the police in those cases intruded into areas

in which the defendant did not enjoy a reasonable expectation of privacy, such

as plainly visible automobile interiors or other locations visible from lawful

vantage points.

      For example, in Commonwealth v. Milyak, 508 Pa. 2, 493 A.2d 1346

(1985), our Supreme Court held that officers properly seized stolen items that

they observed in a vehicle with the aid of a flashlight. Milyak held that “no

search triggering the protection of the Fourth Amendment is conducted where

an officer observes the plainly viewable interior of a vehicle,” because

      there is no reason [a police officer] should be precluded from
      observing as an officer what would be entirely visible to him as a
      private citizen. There is no legitimate expectation of privacy ...
      shielding that portion of the interior of an automobile which may
      be viewed from outside the vehicle by either inquisitive passersby
      or diligent police officers.

Id., 493 A.2d at 1348.       Under the Fourth Amendment, however, “the

expectation of privacy with respect to one’s automobile is significantly less

than that relating to one’s home…”    Commonwealth v. Gary, 625 Pa. 183,




                                     - 18 -
J-E03003-25


91 A.3d 102, 111 (2014).8 Thus, Milyak does not apply to the search herein

of a closed container inside Appellant’s residence. Multiple other decisions

cited by the Commonwealth are inapplicable for the same reason. See Texas

v. Brown, 460 U.S. 730, 733, 103 S.Ct. 1535, 75 L.Ed.20 502 (1983)

(plurality opinion) (officer shined flashlight into car and observed balloon

containing drugs); Commonwealth v. Merkt, 600 A.2d 1297, 1299 (Pa.

Super. 1992) (citing Milyak) (officer shined flashlight into vehicle and saw

gun); see also United States v. Poller, 129 F.4th 169, 175 (2nd Cir. 2025)

(officer shined flashlight into car); United States v. Harper, 488 Fed. Appx.

63, 66-67 (6th Cir. 2012) (same); United States v. McCoy, 824 F. Supp.

467, 475 (D. Del. 1993) (same); People v. Dickinson, 928 P.2d 1309, 1312

(Colo. 1996) (same); Commonwealth v. Sergienko, 503 N.E.2d 1282,

1285-86 (Mass. 1987) (same).

       Other decisions cited by the Commonwealth are distinguishable because

the police officers shined lights from a public place or lawful vantage point into

an area or on an object in which the defendant did not have a reasonable

expectation of privacy. See United States v. Lee, 274 U.S. 559, 563, 47

S.Ct. 746, 71 L.Ed.2d 1202 (1927) (Coast Guard vessel shined searchlight



____________________________________________


8 Our Supreme Court has held that individuals enjoy a greater expectation of

privacy in their automobiles under Article I, Section 8 of the Pennsylvania
Constitution than under the Fourth Amendment.            Commonwealth v.
Alexander, 664 Pa. 145, 243 A.3d 177, 202-03 (2020). The present
discussion, however, does not concern Article I, Section 8.

                                          - 19 -
J-E03003-25


onto deck of motorboat 24 miles off Massachusetts coast, illuminating cans of

alcohol; “there was [no] exploration below decks or under hatches”);

Commonwealth v. Jones, 978 A.2d 1000, 1005 (Pa. Super. 2009) (shining

spotlight at night onto front porch of residence ten feet away did not violate

Fourth Amendment; spotlight was shined from lawful vantage point on public

street, and illuminated area would have been in plain view in daytime);

United States v. De Jesus Cruz-Mendez, 467 F.3d 1260, 1263, 1266 (10th

Cir. 2006) (officer lawfully inside residence observed cell phone in plain view

and shined flashlight on its dark screen); United States v. Law, 384 Fed.

Appx. 121, 123-24 (3rd Cir. 2010) (police officer lawfully inside apartment to

investigate domestic argument shined flashlight into open bag partially inside

open closet); State v. Johnson, 171 N.J. 192, 793 A.2d 619, 630 (2002)

(police officers investigating report of drug-dealing at night shined flashlight

and searchlight from public street; officer holding flashlight observed

defendant place object in support post of porch; without losing sight of post,

officer walked onto porch, shined flashlight into post, and found container with

drugs inside); State v. Rose, 128 Wash.2d 388, 909 P.2d 280, 283-85 (1996)

(officer who was lawfully on front porch of residence shined flashlight through

unobstructed window and saw drugs inside; no reasonable expectation of




                                     - 20 -
J-E03003-25


privacy under these circumstances, and use of flashlight did not transform

observations into a search).9

       For these reasons, the decisions advanced by the Commonwealth fail to

convince us that Trooper Adams did not perform a search.

       The dissent maintains that Trooper Adams did not perform a search.

The dissent observes that the officers in Hagestedt and Tarantino had to

“strain themselves and move their bodies, in addition to using a flashlight, in

order to see items secreted behind solidly closed objects.”       Dissent at 9.

Trooper Adams, the dissent continues, “simply illuminated his flashlight.” Id.

at 11. “The use of a flashlight to brighten an object,” the dissent concludes,

“is not, by itself, a ‘search’ as that term is used for constitutional purposes.”

Id. at 9. We disagree for two reasons.

       First, we believe the dissent misinterprets Hagestedt and Tarantino

by asserting that that the items in these cases were “secreted behind solidly

closed objects.” Dissent at 9. The objects were not solidly closed. There

were small holes through which the officers in these cases shined flashlights,

just as there was a small hole through which Trooper Adams shined his

flashlight.



____________________________________________


9 This Court reached a result similar to Rose in Commonwealth v. Shannon,

467 A.2d 850 (Pa. Super. 1983), a decision not cited by the Commonwealth.
Id. at 852 (where officers were lawfully in driveway and observed fight
through kitchen window, “the occupants’ failure to close [the] window largely
negates their expectation of privacy”).

                                          - 21 -
J-E03003-25


      Furthermore, and perhaps even more importantly, the dissent concedes

that Appellant had a reasonable expectation of privacy in the contents inside

the shoebox. Id. at 3. The shoebox was closed, reflecting an attempt to

conceal its contents from view.      There is no evidence that Trooper Adams

could see the contents inside the shoebox with his naked eye. He had to use

his flashlight to look through a small hole in the shoebox to see its contents.

To borrow the dissent’s euphemisms, even if he did not “strain himself” or

“move his body,” his use of an artificial aid to “brighten” the shoebox interior

still constituted an unlawful search into an area in which Appellant enjoyed a

reasonable expectation of privacy. See Prater, 256 A.3d at 1286 (search

occurs when “police intrude upon a constitutionally protected area without the

individual’s explicit or implicit permission”).

      The Commonwealth next argues that Trooper Adams’ presence in the

Appellant’s residence under the community caretaking doctrine to render

emergency aid gave him a lawful right of access to the shoe box. We agree

that Trooper Adams was authorized to enter Appellant’s residence without a

warrant under the community caretaking doctrine, a narrow exception to the

Fourth Amendment. We conclude, however, that Trooper Adams’ search of

the shoebox exceeded his authority under the community caretaking doctrine.

      This Court has defined the community caretaking doctrine as follows:

      Under the Fourth Amendment, searches and seizures without a
      warrant are presumptively unreasonable, subject only to
      specifically established exceptions. Certain of these exceptions
      arise in the context of law enforcement and are related to the

                                      - 22 -
J-E03003-25


     detection, investigation and prevention of criminal activity, such
     as the exigent circumstances exception, the plain view exception,
     searches incident to arrest, consent searches, automobile
     searches, and the imminent criminal activity exception.

     In addition to these crime-related exceptions, law enforcement
     officers legitimately perform community caretaking activities that
     also necessitate exception to the warrant requirement. The
     community caretaking doctrine has been characterized as
     encompassing three specific exceptions to the warrant
     requirement: the emergency aid exception, the public servant
     exception, and the automobile impoundment/inventory exception.
     Each of these exceptions contemplates that police officers engage
     in a wide variety of activities relating to the health and safety of
     citizens unrelated to the detection, investigation and prevention
     of criminal activity. Nevertheless, community caretaking activities
     must be performed in strict accordance with the Fourth
     Amendment.

     [T]he emergency aid exception . . . permits police officers to make
     warrantless entries and searches when they reasonably believe
     that a person is in need of immediate aid. As with all of the
     community caretaking exceptions, actions by police pursuant to
     the emergency aid exception must be independent from the
     detection, investigation, and acquisition of criminal evidence.

Commonwealth v. Davenport, 266 A.3d 707, 709-10 (Pa. Super. 2021)

(citations and quotations omitted).

     A warrantless intrusion under the emergency aid exception must be

commensurate with, and limited to, the perceived need to provide immediate

assistance. Commonwealth v. Wilmer, 648 Pa. 577, 194 A.3d 564, 571

(2018). In other words,

     the right of entry into the private dwelling by law enforcement
     officers terminates when either the necessary emergency
     assistance has been provided or it has been confirmed that no one
     inside needs emergency assistance. At that point, law
     enforcement officers must leave the residence unless some



                                      - 23 -
J-E03003-25


      other exception to the warrant requirement permits their
      continued presence.

Id. at 572 (emphasis in original).

      Under the community caretaking doctrine, Trooper Adams properly

entered Appellant’s residence without a warrant to help if Appellant became

violent while receiving emergency treatment from EMS paramedics for his

overdose.   The community caretaking doctrine, however, did not entitle

Trooper Adams to shine his flashlight into the shoebox.          Hagestedt is

persuasive on this point. One of the officers in Hagestedt shined his flashlight

into a small opening in a kitchen cabinet that was unrelated to the gas leak,

a “deliberate action that was unrelated to his authorized intrusion.” Id., 270

N.E.3d at 347. Similarly, Trooper Adams shined his flashlight into a hole in

the shoebox, an act unrelated to his reason for entering the residence under

the community caretaking doctrine, which was to provide help if Appellant

became violent.

      The Commonwealth insists that Trooper Adams’ purpose in shining his

flashlight into the shoebox was to assist EMS personnel, thus validating this

act under the community caretaking doctrine. See Commonwealth’s Brief at

51 (“Trooper Adams immediately recognized scramble pills; at that moment,

the contents of the shoebox became important intelligence for EMS as to what

[Appellant] overdosed on, and potentially how he overdosed on it. Opening

the shoebox potentially reveals more clues that could help EMS treat

[Appellant]”) & at 52 (“Opening the shoebox to reveal its contents served an

                                     - 24 -
J-E03003-25


essential function in that emergency aid – attempting to discern what

[Appellant] used, and how he may have used it, to better help EMS render

emergency services”). No evidence supports this thesis. Trooper Adams, the

sole witness during the suppression hearing, admitted that he did not enter

the residence to provide medical assistance, because he was not trained as

an EMT, and because three EMS workers were already providing medical

treatment to Appellant.     Trooper Adams did not testify that EMS personnel

needed to know what substance caused the overdose or asked him to find or

identify this substance.   Nor did Trooper Adams testify that he told EMS

personnel what he found in the shoebox—testimony he naturally would have

given had his role been to assist in medical treatment.

      The sole reason that Trooper Adams gave for shining his flashlight into

the box—“we go there to see what [the patient] overdosed on to possibly

make an investigation further, anything that’s in plain view that we can

see,” N.T., 3/16/23, at 10 (emphasis added)—was for the purpose of criminal

investigation, not medical assistance. This was how the prosecutor and the

trial court interpreted the trooper’s testimony. The prosecutor argued that

the trooper’s conduct was proper under the plain view doctrine. Id. at 24-26.

The prosecutor did not contend that the trooper shined his flashlight to provide

medical assistance. Similarly, the trial court stated, “The issue in this case is

limited to whether the shoebox with the round hole would be a situation where

the plain view doctrine would grant an exception to the need for a search


                                     - 25 -
J-E03003-25


warrant.” Id. at 27. Thus, by searching the interior of the shoebox with his

flashlight, Trooper Adams exceeded his authority under the community

caretaking exception.

       Finally, we consider whether the search of the shoebox was permissible

under the “plain view” exception to the Fourth Amendment. We conclude that

it was not.

       The plain view doctrine authorizes a warrantless seizure of evidence

when (1) the police must observe the object from a lawful vantage point; (2)

the incriminating character of the object must be immediately apparent10; and

(3) the police must have a lawful right of access to the object.

Commonwealth v. Graham, 721 A.2d 1075, 1079 (Pa. 1998) (citing Horton

v. California, 496 U.S. 128, 136-37 (1990)). Since any evidence seized by

police will be in plain view at the moment of seizure, the “question of whether

property in plain view of the police may be seized therefore must turn on the

legality of the intrusion that enables them to perceive and physically seize the

property in question.” Graham, 721 A.2d at 1079 (citing Texas v. Brown,

460 U.S. 730, 737 (1983)). “Plain view” provides grounds for seizure of an

item


____________________________________________


10 In other words, “the observing officer must have probable cause to believe

the evidence in question is contraband or incriminating evidence”).
Saunders, 326 A.3d at 897 (citations omitted). Probable cause exists “where
the facts and circumstances within the officer's knowledge are sufficient to
warrant a person of reasonable caution in the belief that an offense has been
or is being committed.” Id. (citations omitted).

                                          - 26 -
J-E03003-25


      when an officer’s access to an object has some prior justification
      under the Fourth Amendment. “Plain view” is perhaps better
      understood, therefore, not as an independent “exception” to the
      warrant clause, but simply as an extension of whatever the prior
      justification for an officer’s “access to an object” may be.

Graham, 721 A.2d at 1079 (citing Brown, 460 U.S. at 738-39). Graham

observed that the plain view doctrine “establishes an exception to the

requirement of a warrant not to search for an item, but to seize it.” Id. at

1080. This distinction “highlights the principle that the plain view doctrine

permits police officers to seize contraband that is in their purview if an

independent justification gives the officer a lawful right of access to the item,

but cannot, on its own, justify an officer extending his or her search for that

item.” Id.

      Trooper Adams satisfied the first prong of the plain view test,

observation from a lawful vantage point, because he was lawfully in the living

room inside Appellant’s home for a “community caretaking” function.

      Graham and our Supreme Court’s decision in Commonwealth v.

Norris, 498 Pa. 308, 446 A.2d 246 (1982), help resolve the second and third

plain view prongs. In Norris, two police officers heard loud music emanating

from the defendant’s apartment. The officers knocked on the door for several

minutes and identified themselves before breaking down the door and

conducting a limited search of the apartment. One officer seized a knife seen

on a nightstand.    The officers then thoroughly searched the bedroom and

found a gun under a mattress.         Our Supreme Court held that exigent


                                     - 27 -
J-E03003-25


circumstances justified the forcible entry into and limited search of the

apartment. Moreover, the plain view doctrine authorized the seizure of the

knife on the nightstand, because the exigencies of the situation had already

justified the intrusion into the bedroom where the knife was discovered. Id.,

446 A.2d at 250. The Court found, however, that the plain view doctrine did

not authorize the search under the mattress and the seizure of the gun,

because “[t]he gun could not have been seen without a thorough search of

the bedroom. That search occurred after defendant was securely held and

after it was apparent there was no one else in the apartment to endanger the

officers.” Id.

      In Graham, a police officer realized that an arrest warrant was issued

for one of three men he observed on a porch. He approached the group and

directed the man who was the subject of the warrant to lie down. He then

patted down one of the other men, the defendant, for weapons. After finding

no weapons, the officer shined a flashlight down into the defendant’s pocket

and found a Lifesavers Holes container. The container later was determined

to contain crack cocaine. Our Supreme Court held that the pat-down of the

defendant was a valid search to protect the officer’s safety, relying on Terry

v. Ohio, 392 U.S. 1 (1968).        The Court further held, however, that no

justification existed for shining a flashlight into the defendant’s pocket:

      [The officer] completed the search for weapons authorized under
      Terry before using his flashlight. The subsequent act of shining
      the flashlight was part and parcel of the search that put the
      contraband into plain view. Thus, the Commonwealth seeks to

                                     - 28 -
J-E03003-25


      use the plain view doctrine, not to validate seizing an already
      exposed object, but to justify an extended search and subsequent
      seizure of contraband discovered in the course of a Terry stop.
      Since the plain view doctrine cannot justify extending a
      warrantless search, we find that it cannot legitimize [the officer’s]
      flashlight-aided search of [the defendant’s] backpocket.

Graham, 721 A.2d at 1080. The Court found these facts distinguishable from

Commonwealth v. Burton, 436 A.2d 1010 (Pa. Super. 1981), in which a

police officer shined a flashlight into the backseat of a car during a nighttime

search:

      The [Commonwealth cites Burton] for the proposition that an
      officer lawfully in a position to make an observation may enhance
      his ability to see by the use of a flashlight. Burton involved a
      police officer searching a car incident to a lawful arrest for
      possession of a handgun without a permit. There, the officer
      shined his flashlight into the backseat, revealing contraband.
      The Superior Court found that seizure of the contraband was
      justified by the plain view exception even though the officer
      needed a flashlight to illuminate the contraband. However, the
      reasoning behind Burton, that a flashlight may properly
      illuminate items that would be in plain view during
      daylight hours, does not apply here, as the Lifesavers
      Holes container was not an exposed object.

Graham, 721 A.2d at 1080 (emphasis added).

      In the present case, Trooper Adams failed to satisfy the second prong of

the plain view test, because the object of the search, the closed shoebox, was

not immediately incriminating in appearance. To the contrary, this container,

a mere shoebox, appeared completely innocuous, so there was no reason to

search inside it.   In other words, Trooper Adams lacked probable cause to

search the shoebox. Saunders, 326 A.3d at 897 (equating second prong of

plain view test with probable cause). Nor did Trooper Adams satisfy the third

                                     - 29 -
J-E03003-25


prong because he lacked a lawful right of access to the scramble pills inside the

container. The trooper was only present to provide help if Appellant became

unruly during emergency treatment for a drug overdose.             Under these

circumstances, the trooper had no reason to shine his flashlight into the

manufacturer’s hole of the container, and there was no way for him to see the

scramble pills inside the container without taking this unjustified step. Nor did

the trooper possess a warrant to search the box or demonstrate probable cause

under exigent circumstances that justified a warrantless search of the shoebox.

      Norris and Graham support our decision. In both cases, police officers

conducted an initial search that was proper under the Fourth Amendment.

The items subsequently seized and suppressed were not in plain view despite

the officers having a lawful right to be in the place searched. The present

case is slightly different, because Trooper Adams did not enter the home to

conduct a valid search but instead entered under the community caretaking

doctrine. The initial search herein was Trooper Adams’ flashlight search of the

shoebox, which plainly was improper under the second and third prongs of the

plain view doctrine. As in Norris and Graham, the proper remedy for this

illegal search is suppression of the evidence seized during the search.

      The Commonwealth cites multiple cases which held that the plain view

doctrine was satisfied where a police officer shined a flashlight at night to

illuminate objects that would have been plainly visible during daytime. See,

e.g., Jones, 978 A.2d at 1005; Merkt, 600 A.2d at 1299. We acknowledge,


                                    - 30 -
J-E03003-25


as did Graham, that a police officer can shine his flashlight at nighttime to

illuminate items that would be plainly visible during the daytime.       This

principle, however, does not apply here, because the scramble pills were in a

closed container and would not have been plainly visible with or without the

use of a flashlight had the room been dark and then illuminated at the time

the shoebox was searched.

      The    Commonwealth     argues    that   Norris   and    Graham     are

distinguishable from the present case because the officers in these cases

moved or manipulated objects to reveal incriminating evidence that were not

previously visible, while Trooper Adams did not move anything. We disagree.

Although the officers in Norris and Graham moved or manipulated some

object in order to find incriminating evidence, we know of no requirement that

an officer must move or manipulate an object in order to invalidate a search

under plain view principles. Furthermore, taken to its logical extreme, the

Commonwealth’s argument would allow police officers to search the interior

of any object from a lawful vantage point, so long as the object had even the

tiniest crack or perforation. Precedent does not allow for such an unlawful

intrusion.

      For these reasons, we hold that the trial court erred by denying

Appellant’s motion to suppress. We reverse the order denying suppression,

vacate Appellant’s judgment of sentence and remand to the trial court for

further proceedings.


                                    - 31 -
J-E03003-25


      Order denying suppression reversed. Judgment of sentence vacated.

Case remanded for further proceedings. Jurisdiction relinquished.

      Judge Olson, Judge Dubow, Judge Kunselman, Judge Murray, and Judge

Beck join the opinion.

      Judge Bowes files a dissenting opinion, which Judge Nichols and Judge

McLaughlin join.




Judgment Entered.




Benjamin D. Kohler, Esq.
Prothonotary



Date: 06/05/2026




                                   - 32 -

```

---

## GROUP: content/cases/Cone v. Bell.md  (`case`, 5 assertions)

### content_page

```
---
title: "Cone v. Bell"
type: case
citation: "556 U.S. 449 (2009)"
parallel_cite: "129 S. Ct. 1769; 173 L. Ed. 2d 701"
neutral_cite: 2009 U.S. LEXIS 3298
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-04-28
docket: 07-1114
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2009-04-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Cone v. Bell
  varies_by_point: false
  scope_note: "Good law. Confirms Brady's disclosure duty reaches evidence material to punishment, not just guilt, and that a state court's mistaken 'previously determined' ruling does not procedurally bar federal habeas review of the Brady claim."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145883/cone-v-bell/"
  cluster_id: 145883
  opinion_id: 145883
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[United States v. Bagley]]", "[[Kyles v. Whitley]]", "[[Strickler v. Greene]]", "[[Banks v. Dretke]]", "[[Giglio v. United States]]"]
aliases: []
tags: ["case", "brady", "giglio", "materiality", "sentencing", "procedural-default", "due-process", "capital"]
holding: "Brady's disclosure obligation extends to evidence material to punishment as well as guilt; a state court's mistaken belief that a claim was 'previously determined' does not bar federal habeas review. Although the suppressed drug-impairment evidence was not material to guilt, the lower courts failed to assess its materiality to the death sentence, requiring remand."
lake:
  record_id: Cone v. Bell
  status: verified
  projected_at: 2026-07-06
---

# Cone v. Bell

*556 U.S. 449 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gary Cone was convicted of the 1980 murders of an elderly Memphis couple and sentenced to death. His defense was that chronic amphetamine addiction — which he traced to combat service in Vietnam — left him impaired or insane. Years later, after gaining access to the prosecutor's file, Cone discovered witness statements and documents the State had suppressed that corroborated his drug impairment around the time of the crimes. The Tennessee courts treated his *[[Brady v. Maryland|Brady]]* claim as "previously determined," and the federal courts found it defaulted and, in any event, not material to guilt.

## Issue
Whether Cone's *[[Brady v. Maryland|Brady]]* claim was procedurally barred from federal [[Common Legal Terms#habeas-corpus|habeas]] review, and whether the suppressed evidence — even if not material to guilt — had to be assessed for materiality to his death sentence.

## Rule
*[[Brady v. Maryland|Brady]]* reaches evidence material to punishment. "[W]hen the State withholds from a criminal defendant evidence that is material to his guilt or punishment, it violates his right to due process of law in violation of the Fourteenth Amendment." — 556 U.S. at 469. ^pin-469

Materiality follows the unified *[[United States v. Bagley|Bagley]]* test: "evidence is 'material' within the meaning of *Brady* when there is a reasonable probability that, had the evidence been disclosed, the result of the proceeding would have been different." — 556 U.S. at 470. ^pin-470

The Court added that disclosure obligations may run broader than the constitutional floor: "the obligation to disclose evidence favorable to the defense may arise more broadly under a prosecutor's ethical or statutory obligations." — 556 U.S. at 470 n.15. ^pin-470b

A mistaken state procedural ruling does not bar review. Because Cone "properly preserved and exhausted his *Brady* claim in the state court," it was "not defaulted," and the state courts' erroneous belief that the claim had been "previously determined" created no obstacle to federal merits review. — 556 U.S. at 469.

## Application
The Court held the *[[Brady v. Maryland|Brady]]* claim was not procedurally defaulted: Cone raised it in state court, and the state courts' "previously determined" disposition rested on a mistaken premise, so it did not bar federal review. On the merits, the suppressed witnesses' statements and documents all "strengthen[ed] the inference that Cone was impaired by his use of drugs." While that evidence was not material to whether Cone committed murder with the requisite mental state, the District Court and Court of Appeals never separately assessed whether the same evidence was material to his *sentence* — i.e., whether it might have led at least one juror to choose life over death. Because the suppressed evidence "may well have been material to the jury's assessment of the proper punishment," a full review was required.

## Conclusion
[[Reading and Citing Cases#vacated|Vacated]] and [[Reading and Citing Cases#on-remand|remanded]]. The *[[Brady v. Maryland|Brady]]* claim was not defaulted, and the lower courts had to determine in the first instance whether there was a reasonable probability the withheld evidence would have altered at least one juror's sentencing decision — *[[Brady v. Maryland|Brady]]* materiality is assessed as to punishment, not only guilt.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (Stevens, J.; Roberts, C.J., concurring in part; Thomas, J., joined in part by Alito, J., dissenting).
- *Cone* applies the [[Brady v. Maryland]] rule and the unified materiality standard of [[United States v. Bagley]] / [[Kyles v. Whitley]] / [[Strickler v. Greene]] to the sentencing phase, and cites [[Banks v. Dretke]] for the "put the whole case in such a different light" formulation. No negative treatment.

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Cone v. Bell*, 556 U.S. 449 (2009) — https://www.courtlistener.com/opinion/145883/cone-v-bell/ — pinpoints: 469, 470 (& n.15). (CourtListener carries the slip opinion, paginated "556 U.S. ___"; U.S. Reports pages supplied from the official reporter.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3cc8d649a998be12", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "556 U.S. 449 (2009)", "court": "U.S. Supreme Court", "neutral_cite": "2009 U.S. LEXIS 3298", "official_citation_present": true, "parallel_cite": "129 S. Ct. 1769; 173 L. Ed. 2d 701", "title": "Cone v. Bell", "year": "2009"}}
{"assertion_id": "c23941eb7d0850db", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key — Progeny / Refinement", "title": "Cone v. Bell"}}
{"assertion_id": "d262aae035884d4a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Brady's disclosure obligation extends to evidence material to punishment as well as guilt; a state court's mistaken belief that a claim was 'previously determined' does not bar federal habeas review. Although the suppressed drug-impairment evidence was not material to guilt, the lower courts failed to assess its materiality to the death sentence, requiring remand.", "title": "Cone v. Bell"}}
{"assertion_id": "2f6a7a7228a1d5dc", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Cone v. Bell"}}
{"assertion_id": "a1233d6bc9cbbd19", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2009-04-28", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Cone v. Bell", "field_i_validity": "good_law", "scope_note": "Good law. Confirms Brady's disclosure duty reaches evidence material to punishment, not just guilt, and that a state court's mistaken 'previously determined' ruling does not procedurally bar federal habeas review of the Brady claim.", "title": "Cone v. Bell", "varies_by_point": "false"}}
```

### lake record — Cone v. Bell

```json
{
  "schema_version": "s2.v1",
  "record_id": "Cone v. Bell",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Cone v. Bell",
    "case_name_short": "Cone",
    "case_name_full": "Cone v. Bell, Warden",
    "input_case_name": "Cone v. Bell",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-04-28",
    "year": 2009,
    "docket": "07-1114",
    "cluster_id": 145883,
    "lead_opinion_id": 145883,
    "sibling_ids": [
      145883,
      9435356,
      9435357,
      9435358
    ],
    "absolute_url": "/opinion/145883/cone-v-bell/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "556 U.S. 449",
      "volume": "556",
      "reporter": "U.S.",
      "page": "449",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "129 S. Ct. 1769",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "1769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 701",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "701",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 3298",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "3298",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "556 U.S. 449",
        "volume": "556",
        "reporter": "U.S.",
        "page": "449",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 1769",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "1769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 701",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "701",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 3298",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "3298",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "556 U.S. 449",
    "official_selection": {
      "court_class": "scotus",
      "selected": "556 U.S. 449",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-469",
      "page": null,
      "quote": "and the federal courts found it defaulted and, in any event, not material to guilt. ## Issue Whether Cone's *Brady* claim was procedurally barred from federal habeas review, and whether the suppressed evidence \u2014 even if not material to guilt \u2014 had to be assessed for materiality to his death sentence. ## Rule *Brady* reaches evidence material to punishment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-470",
      "page": null,
      "quote": "evidence is 'material' within the meaning of *Brady* when there is a reasonable probability that, had the evidence been disclosed, the result of the proceeding would have been different.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-470b",
      "page": null,
      "quote": "the obligation to disclose evidence favorable to the defense may arise more broadly under a prosecutor's ethical or statutory obligations.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2009-04-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Cone v. Bell",
    "varies_by_point": false,
    "scope_note": "Good law. Confirms Brady's disclosure duty reaches evidence material to punishment, not just guilt, and that a state court's mistaken 'previously determined' ruling does not procedurally bar federal habeas review of the Brady claim.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Scott Panetti v. Lorie Davis, Director",
          "cluster_id": 4408050,
          "cite": [
            "863 F.3d 366",
            "2017 WL 2953154",
            "2017 U.S. App. LEXIS 12390"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "JAMES J. DORSEY v. UNITED STATES",
          "cluster_id": 4370480,
          "cite": [
            "154 A.3d 106",
            "2017 WL 728705",
            "2017 D.C. App. LEXIS 14"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Taylor v. Connelly",
          "cluster_id": 7306337,
          "cite": [
            "18 F. Supp. 3d 242",
            "2014 WL 1814153",
            "2014 U.S. Dist. LEXIS 63236"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lebere v. Abbott",
          "cluster_id": 1085878,
          "cite": [
            "732 F.3d 1224",
            "2013 U.S. App. LEXIS 21131",
            "2013 WL 5663866"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Cain",
          "cluster_id": 620666,
          "cite": [
            "181 L. Ed. 2d 571",
            "132 S. Ct. 627",
            "565 U.S. 73",
            "2012 U.S. LEXIS 576"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffrey Wogenstahl v. Betty Mitchell",
          "cluster_id": 621975,
          "cite": [
            "668 F.3d 307",
            "2012 WL 310819",
            "2012 U.S. App. LEXIS 1905"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dennis v. Secretary, Pennsylvania Department of Corrections",
          "cluster_id": 4250271,
          "cite": [
            "834 F.3d 263",
            "2016 U.S. App. LEXIS 15434",
            "2016 WL 4440925"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Verdugo",
          "cluster_id": 1801961,
          "cite": [
            "50 Cal. 4th 263",
            "236 P.3d 1035",
            "113 Cal. Rptr. 3d 803",
            "2010 Cal. LEXIS 7524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Conway",
          "cluster_id": 2718013,
          "cite": [
            "763 F.3d 115",
            "2014 WL 3953234",
            "2014 U.S. App. LEXIS 15589"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Grant v. Royal",
          "cluster_id": 4482788,
          "cite": [
            "886 F.3d 874"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Turner v. United States",
          "cluster_id": 4403802,
          "cite": [
            "582 U.S. 313",
            "2017 U.S. LEXIS 4041",
            "137 S. Ct. 1885",
            "198 L. Ed. 2d 443",
            "26 Fla. L. Weekly Fed. S 700",
            "85 U.S.L.W. 4488",
            "2017 WL 2674152"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Moore",
          "cluster_id": 222130,
          "cite": [
            "651 F.3d 30",
            "397 U.S. App. D.C. 148",
            "2011 U.S. App. LEXIS 15666",
            "2011 WL 3211511"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jalowiec v. Bradshaw",
          "cluster_id": 613237,
          "cite": [
            "657 F.3d 293",
            "2011 U.S. App. LEXIS 18570",
            "2011 WL 3903439"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Verdugo",
          "cluster_id": 2389003,
          "cite": [
            "50 Cal. 4th 263"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Runningeagle v. Schriro",
          "cluster_id": 804607,
          "cite": [
            "686 F.3d 758",
            "2012 WL 2913810",
            "2012 U.S. App. LEXIS 14682"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marcos Poventud v. City of New York",
          "cluster_id": 2649520,
          "cite": [
            "750 F.3d 121",
            "2014 WL 182313",
            "2014 U.S. App. LEXIS 864"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brooks v. Tennessee",
          "cluster_id": 179722,
          "cite": [
            "626 F.3d 878",
            "2010 U.S. App. LEXIS 24025",
            "2010 WL 4721099"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Belnap v. Iasis Healthcare",
          "cluster_id": 4336218,
          "cite": [
            "844 F.3d 1272",
            "2017 WL 56277",
            "2017 U.S. App. LEXIS 180"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Downs v. Lape",
          "cluster_id": 613588,
          "cite": [
            "657 F.3d 97",
            "2011 U.S. App. LEXIS 18921",
            "2011 WL 4057173"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Caro",
          "cluster_id": 261,
          "cite": [
            "597 F.3d 608",
            "2010 U.S. App. LEXIS 5511",
            "2010 WL 963201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florencio Dominguez v. Scott Kernan",
          "cluster_id": 4546317,
          "cite": [
            "906 F.3d 1127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mason v. Allen",
          "cluster_id": 146270,
          "cite": [
            "605 F.3d 1114",
            "2010 U.S. App. LEXIS 9646",
            "2010 WL 1856165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henness v. Bagley",
          "cluster_id": 220347,
          "cite": [
            "644 F.3d 308",
            "2011 U.S. App. LEXIS 13656",
            "2011 WL 2621896"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
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
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicole Harris v. Sheryl Thompson",
          "cluster_id": 810477,
          "cite": [
            "698 F.3d 609",
            "2012 WL 4944325",
            "2012 U.S. App. LEXIS 21727"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Danberg",
          "cluster_id": 1380327,
          "cite": [
            "594 F.3d 210",
            "2010 U.S. App. LEXIS 2100",
            "2010 WL 337319"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shun Warren v. Michael Baenen",
          "cluster_id": 857090,
          "cite": [
            "712 F.3d 1090",
            "2013 WL 1316905",
            "2013 U.S. App. LEXIS 6674"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. WARRIOR",
          "cluster_id": 2330570,
          "cite": [
            "277 P.3d 1111",
            "294 Kan. 484",
            "2012 WL 1648899",
            "2012 Kan. LEXIS 255"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145883 OR 9435356 OR 9435357 OR 9435358) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzU1MDk3NjAwMDAwJnM9MTA0NTQ5NCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145883+OR+9435356+OR+9435357+OR+9435358%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(145883 OR 9435356 OR 9435357 OR 9435358)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05MCZzPTYxODQ2OSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145883+OR+9435356+OR+9435357+OR+9435358%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145883 OR 9435356 OR 9435357 OR 9435358)",
        "reviewed": 38,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 38,
        "triage_read": 0,
        "triage_snippet_classified": 38
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145883 OR 9435356 OR 9435357 OR 9435358)",
    "indexed_citing_opinions": 354,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145883,
        "count": 278,
        "count_source": "search"
      },
      {
        "opinion_id": 9435356,
        "count": 82,
        "count_source": "search"
      },
      {
        "opinion_id": 9435357,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9435358,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1062,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/cone-v-bell.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3NzQ4OTcmcz05NDk3MjcxJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28145883+OR+9435356+OR+9435357+OR+9435358%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145883,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 102436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 107015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 111822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 112640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 112642,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 112665,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 112773,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 117923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 118048,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 118296,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 118307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 118478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 118509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 130159,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 131165,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 134723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 137745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 145648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 145691,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 145719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 417963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 552438,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 571286,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 589636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 683594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 747610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 759546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 763114,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 772305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 772513,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 783551,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 789238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 793149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 797540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 799980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 1060393,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 1082314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 1446767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 1460405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 1505581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 1524614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 1687210,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 2438728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 2468521,
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
    "date_created": "2026-07-05T00:47:54Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:48:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:48:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:52:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:48:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Cone v. Bell

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

                       CONE v. BELL, WARDEN

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE SIXTH CIRCUIT

   No. 07–1114. Argued December 9, 2008—Decided April 28, 2009
After the State discredited petitioner Cone’s defense that he killed two
  people while suffering from acute psychosis caused by drug addiction,
  he was convicted and sentenced to death. The Tennessee Supreme
  Court affirmed on direct appeal and the state courts denied postcon
  viction relief. Later, in a second petition for state postconviction re
  lief, Cone raised the claim that the State had violated Brady v. Mary
  land, 373 U. S. 83, by suppressing witness statements and police
  reports that would have corroborated his insanity defense and bol
  stered his case in mitigation of the death penalty. The postconviction
  court denied him a hearing on the ground that the Brady claim had
  been previously determined, either on direct appeal or in earlier col
  lateral proceedings. The State Court of Criminal Appeals affirmed.
  Cone then filed a petition for a writ of habeas corpus in Federal Dis
  trict Court. That Court denied relief, holding the Brady claim proce
  durally barred because the state courts’ disposition rested on ade
  quate and independent state grounds: Cone had waived it by failing
  to present his claim in state court. Even if he had not defaulted the
  claim, ruled the court, it would fail on its merits because none of the
  withheld evidence would have cast doubt on his guilt. The Sixth Cir
  cuit agreed with the latter conclusion, but considered itself barred
  from reaching the claim’s merits because the state courts had ruled
  the claim previously determined or waived under state law.
Held:
    1. The state courts’ rejection of Cone’s Brady claim does not rest on
 a ground that bars federal review. Neither of the State’s asserted
 justifications for such a bar—that the claim was decided by the State
 Supreme Court on direct review or that Cone had waived it by never
 properly raising it in state court—provides an independent and ade
2                             CONE v. BELL

                                  Syllabus

    quate state ground for denying review of Cone’s federal claim. The
    state postconviction court’s denial of the Brady claim on the ground it
    had been previously determined in state court rested on a false prem
    ise: Cone had not presented the claim in earlier proceedings and, con
    sequently, the state courts had not passed on it. The Sixth Circuit’s
    rejection of the claim as procedurally defaulted because it had been
    twice presented to the Tennessee courts was thus erroneous. Also
    unpersuasive is the State’s alternative argument that federal review
    is barred because the Brady claim was properly dismissed by the
    state postconviction courts as waived. Those courts held only that
    the claim had been previously determined, and this Court will not
    second-guess their judgment. Because the claim was properly pre
    served and exhausted in state court, it is not defaulted. Pp. 15–19.
       2. The lower federal courts failed to adequately consider whether
    the withheld documents were material to Cone’s sentence. Both the
    quantity and quality of the suppressed evidence lend support to
    Cone’s trial position that he habitually used excessive amounts of
    drugs, that his addiction affected his behavior during the murders,
    and that the State’s contrary arguments were false and misleading.
    Nevertheless, even when viewed in the light most favorable to Cone,
    the evidence does not sustain his insanity defense: His behavior be
    fore, during, and after the crimes was inconsistent with the conten
    tion that he lacked substantial capacity either to appreciate the
    wrongfulness of his conduct or to conform it to the requirements of
    law. Because the likelihood that the suppressed evidence would have
    affected the jury’s verdict on the insanity issue is remote, the Sixth
    Circuit did not err by denying habeas relief on the ground that such
    evidence was immaterial to the jury’s guilt finding. The same cannot
    be said of that court’s summary treatment of Cone’s claim that the
    suppressed evidence would have influenced the jury’s sentencing rec
    ommendation. Because the suppressed evidence might have been
    material to the jury’s assessment of the proper punishment, a full re
    view of that evidence and its effect on the sentencing verdict is war
    ranted. Pp. 20–26.
492 F. 3d 743, vacated and remanded.

  STEVENS, J., delivered the opinion of the Court, in which KENNEDY,
SOUTER, GINSBURG, and BREYER, JJ., joined. ROBERTS, C. J., filed an
opinion concurring in the judgment. ALITO, J., filed an opinion concur
ring in part and dissenting in part. THOMAS, J., filed a dissenting opin
ion, in which SCALIA, J., joined.
                        Cite as: 556 U. S. ____ (2009)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 07–1114
                                   _________________


   GARY BRADFORD CONE, PETITIONER v. RICKY 

               BELL, WARDEN

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE SIXTH CIRCUIT

                                 [April 28, 2009] 


  JUSTICE STEVENS delivered the opinion of the Court.
  The right to a fair trial, guaranteed to state criminal
defendants by the Due Process Clause of the Fourteenth
Amendment, imposes on States certain duties consistent
with their sovereign obligation to ensure “that ‘justice
shall be done’ ” in all criminal prosecutions. United States
v. Agurs, 427 U. S. 97, 111 (1976) (quoting Berger v.
United States, 295 U. S. 78, 88 (1935)). In Brady v. Mary
land, 373 U. S. 83 (1963), we held that when a State sup
presses evidence favorable to an accused that is material
to guilt or to punishment, the State violates the defen
dant’s right to due process, “irrespective of the good faith
or bad faith of the prosecution.” Id., at 87.
  In this case, Gary Cone, a Vietnam veteran sentenced to
death, contends that the State of Tennessee violated his
right to due process by suppressing witness statements
and police reports that would have corroborated his trial
defense and bolstered his case in mitigation of the death
penalty. At his trial in 1982, Cone asserted an insanity
defense, contending that he had killed two people while
suffering from acute amphetamine psychosis, a disorder
2                      CONE v. BELL

                     Opinion of the Court

caused by drug addiction. The State of Tennessee discred
ited that defense, alleging that Cone’s drug addiction was
“baloney.” Ten years later, Cone learned that the State
had suppressed evidence supporting his claim of drug
addiction.
   Cone presented his new evidence to the state courts in a
petition for postconviction relief, but the Tennessee courts
denied him a hearing on the ground that his Brady claim
had been “previously determined,” either on direct appeal
from his conviction or in earlier collateral proceedings. On
application for a writ of habeas corpus pursuant to 28
U. S. C. §2254, the Federal District Court concluded that
the state courts’ disposition rested on an adequate and
independent state ground that barred further review in
federal court, and the Court of Appeals for the Sixth Cir
cuit agreed. Doubt concerning the correctness of that
holding, coupled with conflicting decisions from other
Courts of Appeals, prompted our grant of certiorari.
   After a complete review of the trial and postconviction
proceedings, we conclude that the Tennessee courts’ rejec
tion of petitioner’s Brady claim does not rest on a ground
that bars federal review. Furthermore, although the
District Court and the Court of Appeals passed briefly on
the merits of Cone’s claim, neither court distinguished the
materiality of the suppressed evidence with respect to
Cone’s guilt from the materiality of the evidence with
respect to his punishment. While we agree that the with
held documents were not material to the question whether
Cone committed murder with the requisite mental state,
the lower courts failed to adequately consider whether
that same evidence was material to Cone’s sentence.
Therefore, we vacate the decision of the Court of Appeals
and remand the case to the District Court to determine in
the first instance whether there is a reasonable probability
that the withheld evidence would have altered at least one
juror’s assessment of the appropriate penalty for Cone’s
                    Cite as: 556 U. S. ____ (2009)                   3

                         Opinion of the Court

crimes.
                             I
  On the afternoon of Saturday, August 10, 1980, Cone
robbed a jewelry store in downtown Memphis, Tennessee.
Fleeing the scene by car, he led police on a high-speed
chase into a residential neighborhood. Once there, he
abandoned his vehicle and shot a police officer.1 When a
bystander tried to impede his escape, Cone shot him, too,
before escaping on foot.
  A short time later, Cone tried to hijack a nearby car.
When that attempt failed (because the driver refused to
surrender his keys), Cone tried to shoot the driver and a
hovering police helicopter before realizing he had run out
of ammunition. He then fled the scene. Although police
conducted a thorough search, Cone was nowhere to be
found.
  Early the next morning, Cone reappeared in the same
neighborhood at the door of an elderly woman. He asked
to use her telephone, and when she refused, he drew a
gun. Before he was able to gain entry, the woman
slammed the door and called the police. By the time offi
cers arrived, however, Cone had once again disappeared.
  That afternoon, Cone gained entry to the home of 93
year-old Shipley Todd and his wife, 79-year-old Cleopatra
Todd. Cone beat the couple to death with a blunt instru
ment and ransacked the first floor of their home. Later,
he shaved his beard and escaped to the airport without
being caught. Cone then traveled to Florida, where he
was arrested several days later after robbing a drugstore
in Pompano Beach.
  A Tennessee grand jury charged Cone with two counts
——————
  1 From  the abandoned vehicle, police recovered stolen jewelry, large
quantities of illegal and prescription drugs, and approximately $2,400
in cash. Much of the cash was later connected to a grocery store rob
bery that had occurred on the previous day.
4                      CONE v. BELL

                     Opinion of the Court

of first-degree murder, two counts of murder in the perpe
tration of a burglary, three counts of assault with intent to
murder, and one count of robbery by use of deadly force.
At his jury trial in 1982, Cone did not challenge the over
whelming physical and testimonial evidence supporting
the charges against him. His sole defense was that he was
not guilty by reason of insanity.
  Cone’s counsel portrayed his client as suffering from
severe drug addiction attributable to trauma Cone had
experienced in Vietnam. Counsel argued that Cone had
committed his crimes while suffering from chronic am
phetamine psychosis, a disorder brought about by his drug
abuse. That defense was supported by the testimony of
three witnesses. First was Cone’s mother, who described
her son as an honorably discharged Vietnam veteran who
had changed following his return from service. She re
called Cone describing “how terrible” it had been to handle
the bodies of dead soldiers, and she explained that Cone
slept restlessly and sometimes “holler[ed]” in his sleep.
Tr. 1643–1645 (Apr. 20, 1982). She also described one
occasion, following Cone’s return from service, when a
package was shipped to him that contained marijuana.
Before the war, she asserted, Cone had not used drugs of
any kind.
  Two expert witnesses testified on Cone’s behalf. Mat
thew Jaremko, a clinical psychologist, testified that Cone
suffered from substance abuse and posttraumatic stress
disorders related to his military service in Vietnam. Ja
remko testified that Cone had expressed remorse for the
murders, and he opined that Cone’s mental disorder ren
dered him substantially incapable of conforming his con
duct to the law. Jonathan Lipman, a neuropharmacolo
gist, recounted at length Cone’s history of illicit drug use,
which began after Cone joined the Army and escalated to
the point where Cone was consuming “rather horrific”
quantities of drugs daily. App. 100. According to Lipman,
                    Cite as: 556 U. S. ____ (2009)                  5

                        Opinion of the Court

Cone’s drug abuse had led to chronic amphetamine psy
chosis, a disorder manifested through hallucinations and
ongoing paranoia that prevented Cone from obeying the
law and appreciating the wrongfulness of his actions.
   In rebutting Cone’s insanity defense the State’s strategy
throughout trial was to present Cone as a calculating,
intelligent criminal who was fully in control of his deci
sions and actions at the time of the crimes. A key compo
nent of that strategy involved discrediting Cone’s claims of
drug use.2 Through cross-examination, the State estab
lished that both defense experts’ opinions were based
solely on Cone’s representations to them about his drug
use rather than on any independently corroborated
sources, such as medical records or interviews with family
or friends. The prosecution also adduced expert and lay
testimony to establish that Cone was not addicted to drugs
and had acted rationally and intentionally before, during,
and after the Todd murders.
   Particularly damaging to Cone’s defense was the testi
mony of rebuttal witness Ilene Blankman, who had spent
time with Cone several months before the murders and at
whose home Cone had stayed in the days leading up to his
arrest in Florida. Blankman admitted to being a former
heroin addict but testified that she no longer used drugs
and tried to stay away from people who did. She testified
that she had never seen Cone use drugs, had never ob
served track marks on his body, and had never seen him
exhibit signs of paranoia.
   Emphasizing the State’s position with respect to Cone’s
——————
  2 The State also cast doubt on Cone’s defense by eliciting testimony

that Cone had enrolled in college following his return from Vietnam
and had graduated with high honors. Later, after serving time in
prison for an armed robbery, Cone gained admission to the University
of Arkansas Law School. The State suggested that Cone’s academic
success provided further proof that he was not impaired following his
return from war.
6                           CONE v. BELL

                         Opinion of the Court

alleged addiction, the prosecutor told the jury during
closing argument, “[Y]ou’re not dealing with a crazy per
son, an insane man. A man . . . out of his mind. You’re
dealing, I submit to you, with a premeditated, cool, delib
erate—and even cowardly, really—murderer.” Tr. 2084
(Apr. 22, 1982). Pointing to the quantity of drugs found in
Cone’s car, the prosecutor suggested that far from being a
drug addict, Cone was actually a drug dealer. The prose
cutor argued, “I’m not trying to be absurd, but he says he’s
a drug addict. I say baloney. He’s a drug seller. Doesn’t
the proof show that?” Id., at 107.3
   The jury rejected Cone’s insanity defense and found him
guilty on all counts. At the penalty hearing, the prosecu
tion asked the jury to find that Cone’s crime met the crite
ria for four different statutory aggravating factors, any
one of which would render him eligible for a capital sen
tence.4 Cone’s counsel called no witnesses but instead
rested on the evidence adduced during the guilt phase
proceedings. Acknowledging that the prosecution’s ex
perts had disputed the existence of Cone’s alleged mental
disorder, counsel nevertheless urged the jury to consider
Cone’s drug addiction when weighing the aggravating and
——————
  3 In his closing rebuttal argument, the prosecutor continued to press

the point, asserting: “There aren’t any charges for drug sales, but that
doesn’t mean that you can’t look and question in deciding whether or
not this man was, in fact, a drug user, or why he had those drugs. Did
he just have those drugs, or did he have those drugs and thousands of
dollars in that car? Among those drugs are there only the drugs he
used? How do we know if he used drugs? The only thing that we ever
had that he used drugs, period, is the fact that those drugs were in the
car and what he told people. What he told people. But according to
even what he told people, there are drugs in there he didn’t even use.”
Tr. 2068 (Apr. 22, 1982).
  4 The jury could impose a capital sentence only if it unanimously

determined that one or more statutory aggravating circumstances had
been proved by the State beyond a reasonable doubt, and that the
mitigating circumstances of the case did not outweigh any statutory
aggravating factors. Tenn. Code Ann. §39–2–203(g) (1982).
                     Cite as: 556 U. S. ____ (2009)                    7

                          Opinion of the Court

mitigating factors in the case.5 The jury found all four
aggravating factors and unanimously returned a sentence
of death.6
                            II
  On direct appeal Cone raised numerous challenges to
his conviction and sentence. Among those was a claim
that the prosecution violated state law by failing to dis
close a tape-recorded statement and police reports relating
to several trial witnesses. See App. 114–117. The Ten
nessee Supreme Court rejected each of Cone’s claims, and
affirmed his conviction and sentence. State v. Cone, 665
S. W. 2d 87 (1984).7 Cone then filed a petition for postcon
——————
   5 As defense counsel emphasized to the jury, one of the statutory miti

gating factors it was required to consider was whether “[t]he capacity of
the defendant to appreciate the wrongfulness of his conduct or to
conform his conduct to the requirements of the law was substantially
impaired as a result of mental disease or defect or intoxication which
was insufficient to establish a defense to the crime but which substan
tially affected his judgment.” §39–2404(j)(8).
   6 Specifically, the jury found Cone had committed one or more prior

felonies involving the use or threat of violence, see §39–2404(i)(2); the
murders had been committed for the purpose of avoiding, interfering
with, or preventing Cone’s lawful arrest or prosecution, see §39–
2404(i)(6); the murders were especially heinous, atrocious, or cruel in
that they involved torture and depravity of mind, see §39–2404(i)(5);
and Cone had knowingly created a risk of death to two or more persons,
other than the victim murdered, during his act of murder, see §39–
2404(i)(3). The Tennessee Supreme Court later observed that by
finding Cone guilty of murder in the first degree during the perpetra
tion of a burglary, the jury implicitly found the existence of an addi
tional statutory aggravating factor: that the murders occurred while
Cone was committing a burglary, §39–2404(i)(7). State v. Cone, 665
S. W. 2d 87, 94 (1984).
   7 In summarizing the trial proceedings the Tennessee Supreme Court

observed: “The only defense interposed on [Cone’s] behalf was that of
insanity, or lack of mental capacity, due to drug abuse and to stress
arising out of his previous service in the Vietnamese war, some eleven
years prior to the events involved in this case. This proved to be a
tenuous defense, at best, since neither of the expert witnesses who
8                            CONE v. BELL

                          Opinion of the Court

viction relief, primarily raising claims that his trial coun
sel had been ineffective; the Tennessee Court of Criminal
Appeals affirmed the denial of that petition in 1987. Cone
v. State, 747 S. W. 2d 353.
   In 1989, Cone, acting pro se, filed a second petition for
postconviction relief, raising myriad claims of error.
Among these was a claim that the State had failed to
disclose evidence in violation of his rights under the
United States Constitution. At the State’s behest, the
postconviction court summarily denied the petition, con
cluding that all the claims raised in it had either been
“previously determined” or “waived.” Order Dismissing
Petition for Post-Conviction Relief in Cone v. State, No. P–
06874 (Crim. Ct. Shelby Cty., Tenn., Jan. 2, 1990).8 At
that time, the court did not specify which claims fell into
which category.
   Cone appealed the denial of his petition to the Tennes
see Court of Criminal Appeals, asserting that the postcon
viction court had erred by dismissing 13 claims—his
——————
testified on his behalf had ever seen or heard of him until a few weeks
prior to the trial. Neither was a medical doctor or psychiatrist, and
neither had purported to treat him as a patient. Their testimony that
he lacked mental capacity was based purely upon his personal recita
tion to them of his history of military service and drug abuse.” Id., at
90.
   8 Under Tennessee law in effect at the time a criminal defendant was

entitled to collateral relief if his conviction or sentence violated “any
right guaranteed by the constitution of [Tennessee] or the Constitution
of the United States.” Tenn. Code Ann. §40–30–105 (1982); see also
§40–30–102. Any hearing on a petition for postconviction relief was
limited, however, to claims that had not been “waived or previously
determined.” See §40–30–111. A ground for relief was “previously
determined” if “a court of competent jurisdiction ha[d] ruled on the
merits [of the claim] after a full and fair hearing.” §40–30–112(a). The
claim was waived “if the petitioner knowingly and understandingly
failed to present it for determination in any proceeding before a court of
competent jurisdiction in which the ground could have been presented.”
§40–30–112(b)(1).
                    Cite as: 556 U. S. ____ (2009)                   9

                         Opinion of the Court

Brady claim among them—as previously determined
when, in fact, they had not been “previously addressed or
determined by any court.” Brief for Petitioner-Appellant
Gary Bradford Cone in No. P–06874, pp. 23–24, and n. 11.
In addition Cone urged the court to remand the case to
allow him, with the assistance of counsel, to rebut the
presumption that he had waived any of his claims by not
raising them at an earlier stage in the litigation. Id., at
24.9 The court agreed and remanded the case for further
proceedings.
  On remand counsel was appointed and an amended
petition was filed. The State once again urged the post
conviction court to dismiss Cone’s petition. Apparently
conflating the state-law disclosure claim Cone had raised
on direct appeal with his newly filed Brady claim, the
State represented that the Tennessee Supreme Court had
already decided the Brady issue and that Cone was there
fore barred from relitigating it. See App. 15–16.
  While that petition remained pending before the post
conviction court, the Tennessee Court of Appeals held for
the first time that the State’s Public Records Act allowed a
criminal defendant to review the prosecutor’s file in his
case. See Capital Case Resource Center of Tenn., Inc. v.
Woodall, No. 01–A–01–9104–CH–00150, 1992 WL 12217
(Jan. 29, 1992). Based on that holding, Cone obtained
access to the prosecutor’s files, in which he found proof
that evidence had indeed been withheld from him at trial.
Among the undisclosed documents Cone discovered were
statements from witnesses who had seen him several days
before and several days after the murders. The witnesses
described Cone’s appearance as “wild eyed,” App. 50, and
——————
  9 See Swanson v. State, 749 S. W. 2d 731, 734 (Tenn. 1988) (courts

should not dismiss postconviction petitions on technical grounds unless
the petitioner has first had “reasonable opportunity, with aid of coun
sel, to file amendments” and rebut presumption of waiver (internal
quotation marks omitted)).
10                          CONE v. BELL

                          Opinion of the Court

his behavior as “real weird,” id., at 49. One witness af
firmed that Cone had appeared “to be drunk or high.”
Ibid. The file also contained a police report describing
Cone’s arrest in Florida following the murders. In that
report, a police officer described Cone looking around “in a
frenzied manner,” and “walking in [an] agitated manner”
prior to his apprehension. Id., at 53. Multiple police
bulletins describing Cone as a “drug user” and a “heavy
drug user” were also among the undisclosed evidence. See
id., at 55–59.
   With the newly discovered evidence in hand, Cone
amended his postconviction petition once again in October
1993, expanding his Brady claim to allege more specifi
cally that the State had withheld exculpatory evidence
demonstrating that he “did in fact suffer drug problems
and/or drug withdrawal or psychosis both at the time of
the offense and in the past.” App. at 20. Cone pointed to
specific examples of evidence that had been withheld,
alleging the evidence was “exculpatory to both the jury’s
determination of petitioner’s guilt and its consideration of
the proper sentence,” and that there was “a reasonable
probability that, had the evidence not been withheld, the
jurors would not have convicted [him] and would not have
sentenced him to death.” Id., at 20–21.10 In a lengthy
affidavit submitted with his amended petition, Cone ex
plained that he had not raised his Brady claim in earlier
proceedings because the facts underlying it “ha[d] been
revealed through disclosure of the State’s files, which
occurred after the first post-conviction proceeding.” App.
18.
   After denying Cone’s request for an evidentiary hearing,
——————
  10 As examples of evidence that had been withheld, Cone pointed to

“statements of Charles and Debbie Slaughter, statements of Sue Cone,
statements of Lucille Tuech, statements of Herschel Dalton, and
patrolman Collins” and “statements contained in official police reports.”
App. 20.
                  Cite as: 556 U. S. ____ (2009)            11

                      Opinion of the Court

the postconviction court denied relief on each claim pre
sented in the amended petition. Many of the claims were
dismissed on the ground that they had been waived by
Cone’s failure to raise them in earlier proceedings; how
ever, consistent with the position urged by the State, the
court dismissed many others, including the Brady claim,
as mere “re-statements of previous grounds heretofore
determined and denied by the Tennessee Supreme Court
upon Direct Appeal or the Court of Criminal Appeals upon
the First Petition.” App. 22.
  Noting that “the findings of the trial court in post
conviction hearings are conclusive on appeal unless the
evidence preponderates against the judgment,” the Ten
nessee Court of Criminal Appeals affirmed. Cone v. State,
927 S. W. 2d 579, 581–582 (1995). The court concluded
that Cone had “failed to rebut the presumption of waiver
as to all claims raised in his second petition for post
conviction relief which had not been previously deter
mined.” Id., at 582 (emphasis added). Cone unsuccess
fully petitioned for review in the Tennessee Supreme
Court, and we denied certiorari. Cone v. Tennessee, 519
U. S. 934 (1996).
                               III
    In 1997, Cone filed a petition for a federal writ of habeas
corpus. Without disclosing to the District Court the con
trary position it had taken in the state-court proceedings,
the State acknowledged that Cone’s Brady claim had not
been raised prior to the filing of his second postconviction
petition. However, wrenching out of context the state
appellate court’s holding that Cone had “waived ‘all claims
. . . which had not been previously determined,’ ” the State
now asserted the Brady claim had been waived. App. 39
(quoting Cone, 927 S. W. 2d, at 581–582).
    In May 1998, the District Court denied Cone’s request
for an evidentiary hearing on his Brady claim. Lamenting
12                      CONE v. BELL

                      Opinion of the Court

that its consideration of Cone’s claims had been “made
more difficult” by the parties’ failure to articulate the state
procedural rules under which each of Cone’s claims had
allegedly been defaulted, App. to Pet. for Cert. 98a, the
District Court nevertheless held that the Brady claim was
procedurally barred. After parsing the claim into 11
separate subclaims based on 11 pieces of withheld evi
dence identified in the habeas petition, the District Court
concluded that Cone had waived each subclaim by failing
to present or adequately develop it in state court. App. to
Pet. for Cert. 112a–113a. Moreover, the court concluded
that even if Cone had not defaulted his Brady claim, it
would fail on its merits because none of the withheld
evidence would have cast doubt on Cone’s guilt. App. to
Pet. for Cert. 116a–119a. Throughout its opinion the
District Court repeatedly referenced factual allegations
contained in early versions of Cone’s second petition for
postconviction relief rather than the amended version of
the petition upon which the state court’s decision had
rested. See, e.g., id., at 112a.
   After the District Court dismissed the remainder of
Cone’s federal claims, the Court of Appeals for the Sixth
Circuit granted him permission to appeal several issues,
including the alleged suppression of Brady material.
Before the Court of Appeals, the State shifted its proce
dural default argument once more, this time contending
that Cone had “simply never raised” his Brady claim in
the state court because he failed to make adequate factual
allegations to support that claim in his second petition for
postconviction relief. App. 41. Repeating the District
Court’s error, the State directed the Court of Appeals’
attention to Cone’s pro se petition and to the petition
Cone’s counsel filed before he gained access to the prosecu
tion’s case file. Id., at 41–42, and n. 7. In other words,
instead of citing the October 1993 amended petition on
which the state court’s decision had been based and to
                 Cite as: 556 U. S. ____ (2009)          13

                     Opinion of the Court

which its order explicitly referred, the State pointed the
court to earlier, less developed versions of the same claim.
   The Court of Appeals concluded that Cone had proce
durally defaulted his Brady claim and had failed to show
cause and prejudice to overcome the default. Cone v. Bell,
243 F. 3d 961, 968 (2001). The court acknowledged that
Cone had raised his Brady claim. 243 F. 3d, at 969. Nev
ertheless, the court considered itself barred from reaching
the merits of the claim because the Tennessee courts had
concluded the claim was “previously determined or waived
under Tenn. Code Ann. §40–30–112.” Ibid.
   Briefly mentioning several isolated pieces of suppressed
evidence, the court summarily concluded that even if
Cone’s Brady claim had not been defaulted, the sup
pressed evidence would not undermine confidence in the
verdict (and hence was not Brady material) “because of
the overwhelming evidence of Cone’s guilt.” 243 F. 3d, at
968. The court did not discuss whether any of the undis
closed evidence was material with respect to Cone’s sen
tencing proceedings.
   Although the Court of Appeals rejected Cone’s Brady
claim, it held that he was entitled to have his death sen
tence vacated because of his counsel’s ineffective assis
tance at sentencing. See 243 F. 3d, at 975. In 2002, this
Court reversed that holding after concluding that the
Tennessee courts’ rejection of Cone’s ineffective
assistance-of-counsel claim was not “objectively unreason
able” within the meaning of the Antiterrorism and Effec
tive Death Penalty Act of 1996 (AEDPA). See Bell v. Cone,
535 U. S. 685, 699.
   In 2004, following our remand, the Court of Appeals
again entered judgment ordering a new sentencing hear
ing, this time based on the purported invalidity of an
aggravating circumstance found by the jury. Cone v. Bell,
359 F. 3d 785. Again we granted certiorari and reversed,
relying in part on the deferential standard that governs
14                          CONE v. BELL

                         Opinion of the Court

our review of state-court decisions under AEDPA. See
Bell v. Cone, 543 U. S. 447, 452–458 (2005) (per curiam).
  Following our second remand, the Court of Appeals
revisited Cone’s Brady claim. This time, the court divided
the claim into four separate subclaims: “(1) evidence re
garding [Cone’s] drug use; (2) evidence that might have
been useful to impeach the testimony and credibility of
prosecution witness Sergeant Ralph Roby; (3) FBI re
ports;[11] and (4) evidence showing that prosecution wit
ness Ilene Blankman was untruthful and biased.” 492 F.
3d 743, 753 (2007). Noting that it had previously found all
four subclaims to be procedurally defaulted, the court
declined to reconsider its earlier decision. See ibid. (citing
Cone, 243 F. 3d, at 968–970). At the same time, the court
reiterated that the withheld evidence “would not have
overcome the overwhelming evidence of Cone’s guilt in
committing a brutal double murder and the persuasive
testimony that Cone was not under the influence of
drugs.” 492 F. 3d, at 756. Summarily discounting Cone’s
contention that the withheld evidence was material with
respect to his sentence, the court concluded that the intro
duction of the suppressed evidence would not have altered
the jurors’ finding that Cone’s alleged drug use did not
“vitiate his specific intent to murder his victims and did
not mitigate his culpability sufficient to avoid the death
sentence.” Id., at 757.
  Judge Merritt dissented. He castigated the State not
only for withholding documents relevant to Cone’s sole
defense and plea for mitigation, but also for its “falsifica
——————
  11 In the course of federal habeas proceedings, Cone had obtained

access to files from the Federal Bureau of Investigation where he found
additional previously undisclosed evidence not contained in the state
prosecutor’s case file. The suppressed FBI documents make repeated
reference to Cone’s drug use and corroborate his expert’s representation
that he had used drugs during his prior incarceration for armed rob
bery. See id., at 26–28.
                 Cite as: 556 U. S. ____ (2009)           15

                     Opinion of the Court

tion of the procedural record . . . concerning the State’s
procedural default defense to the Brady claim.” Id., at
760. Over the dissent of seven judges, Cone’s petition for
rehearing en banc was denied. 505 F. 3d 610 (2007).
   We granted certiorari, 554 U. S. ___ (2008), to answer
the question whether a federal habeas claim is “proce
durally defaulted” when it is twice presented to the state
courts.
                              IV
   During the state and federal proceedings below, the
State of Tennessee offered two different justifications for
denying review of the merits of Cone’s Brady claim. First,
in connection with Cone’s amended petition for state
postconviction relief, the State argued that the Brady
claim was barred because it had been decided on direct
appeal. See App. 15–16. Then, in connection with Cone’s
federal habeas petition, the State argued that Cone’s claim
was waived because it had never been properly raised
before the state courts. See id., at 39. The District Court
and the Court of Appeals agreed that Cone’s claim was
procedurally barred, but for different reasons. The Dis
trict Court held that the claim had been waived, App. to
Pet. for Cert. 102a, while the Court of Appeals held that
the claim had been either waived or previously deter
mined, Cone, 243 F. 3d, at 969. We now conclude that
neither prior determination nor waiver provides an inde
pendent and adequate state ground for denying Cone
review of his federal claim.
   It is well established that federal courts will not review
questions of federal law presented in a habeas petition
when the state court’s decision rests upon a state-law
ground that “is independent of the federal question and
adequate to support the judgment.” Coleman v. Thomp
son, 501 U. S. 722, 729 (1991); Lee v. Kemna, 534 U. S.
362, 375 (2002). In the context of federal habeas proceed
16                      CONE v. BELL

                      Opinion of the Court

ings, the independent and adequate state ground doctrine
is designed to “ensur[e] that the States’ interest in correct
ing their own mistakes is respected in all federal habeas
cases.” Coleman, 501 U. S., at 732. When a petitioner
fails to properly raise his federal claims in state court, he
deprives the State of “an opportunity to address those
claims in the first instance” and frustrates the State’s
ability to honor his constitutional rights. Id., at 732, 748.
Therefore, consistent with the longstanding requirement
that habeas petitioners must exhaust available state
remedies before seeking relief in federal court, we have
held that when a petitioner fails to raise his federal claims
in compliance with relevant state procedural rules, the
state court’s refusal to adjudicate the claim ordinarily
qualifies as an independent and adequate state ground for
denying federal review. See id., at 731.
   That does not mean, however, that federal habeas re
view is barred every time a state court invokes a proce
dural rule to limit its review of a state prisoner’s claims.
We have recognized that “ ‘the adequacy of state proce
dural bars to the assertion of federal questions’ . . . is not
within the State’s prerogative finally to decide; rather,
adequacy ‘is itself a federal question.’ ” Lee, 534 U. S., at
375 (quoting Douglas v. Alabama, 380 U. S. 415, 422
(1965)); see also Coleman, 501 U. S., at 736 (“[F]ederal
habeas courts must ascertain for themselves if the peti
tioner is in custody pursuant to a state court judgment
that rests on independent and adequate state grounds”).
The question before us now is whether federal review of
Cone’s Brady claim is procedurally barred either because
the claim was twice presented to the state courts or be
cause it was waived, and thus not presented at all.
   First, we address the contention that the repeated pres
entation of a claim in state court bars later federal review.
The Tennessee postconviction court denied Cone’s Brady
claim after concluding it had been previously determined
                    Cite as: 556 U. S. ____ (2009)                 17

                        Opinion of the Court

following a full and fair hearing in state court. See Tenn.
Code Ann. §40–30–112(a) (1982). That conclusion rested
on a false premise: Contrary to the state courts’ finding,
Cone had not presented his Brady claim in earlier pro
ceedings and, consequently, the state courts had not
passed on it. The Sixth Circuit recognized that Cone’s
Brady claim had not been decided on direct appeal, see
Cone, 243 F. 3d, at 969, but felt constrained by the state
courts’ refusal to reach the merits of that claim on post
conviction review. The Court of Appeals concluded that
because the state postconviction courts had applied a state
procedural law to avoid reaching the merits of Cone’s
Brady claim, “an ‘independent and adequate’ state
ground” barred federal habeas review. 243 F. 3d, at 969.
In this Court the State does not defend that aspect of the
Court of Appeals’ holding, and rightly so.
   When a state court declines to review the merits of a
petitioner’s claim on the ground that it has done so al
ready, it creates no bar to federal habeas review. In Ylst
v. Nunnemaker, 501 U. S. 797, 804, n. 3 (1991), we ob
served in passing that when a state court declines to
revisit a claim it has already adjudicated, the effect of the
later decision upon the availability of federal habeas is
“nil” because “a later state decision based upon ineligibil
ity for further state review neither rests upon procedural
default nor lifts a pre-existing procedural default.”12
When a state court refuses to readjudicate a claim on the
ground that it has been previously determined, the court’s
——————
  12 With the exception of the Sixth Circuit, all Courts of Appeals to
have directly confronted the question both before and after Ylst, 501
U. S. 797, have agreed that a state court’s successive rejection of a
federal claim does not bar federal habeas review. See, e.g., Page v.
Frank, 343 F. 3d 901, 907 (CA7 2003); Brecheen v. Reynolds, 41 F. 3d
1343, 1358 (CA10 1994); Bennett v. Whitley, 41 F. 3d 1581, 1582 (CA5
1994); Silverstein v. Henderson, 706 F. 2d 361, 368 (CA2 1983). See
also Lambright v. Stewart, 241 F. 3d 1201, 1206 (CA9 2001).
18                          CONE v. BELL

                          Opinion of the Court

decision does not indicate that the claim has been proce
durally defaulted. To the contrary, it provides strong
evidence that the claim has already been given full consid
eration by the state courts and thus is ripe for federal
adjudication. See 28 U. S. C. §2254(b)(1)(A) (permitting
issuance of a writ of habeas corpus only after “the appli
cant has exhausted the remedies available in the courts of
the State”).
  A claim is procedurally barred when it has not been
fairly presented to the state courts for their initial consid
eration—not when the claim has been presented more
than once. Accordingly, insofar as the Court of Appeals
rejected Cone’s Brady claim as procedurally defaulted
because the claim had been twice presented to the Ten
nessee courts, its decision was erroneous.
  As an alternative (and contradictory) ground for barring
review of Cone’s Brady claim, the State has argued that
Cone’s claim was properly dismissed by the state postcon
viction court on the ground it had been waived. We are
not persuaded. The state appellate court affirmed the
denial of Cone’s Brady claim on the same mistaken ground
offered by the lower court—that the claim had been previ
ously determined.13 Contrary to the State’s assertion, the
——————
  13 As recounted earlier, Cone’s state postconviction petition contained
numerous claims of error. The state postconviction court dismissed
some of those claims as waived and others, including the Brady claim,
as having been previously determined. In affirming the denial of
Cone’s petition the Tennessee Court of Criminal Appeals summarily
stated that Cone had “failed to rebut the presumption of waiver as to
all claims raised in his second petition for post-conviction relief which
had not been previously determined.” Cone v. State, 927 S. W. 2d 579,
582 (1995). Pointing to that language, the State asserts that the
Tennessee Court of Criminal Appeals denied Cone’s Brady claim not
because it had been previously determined, but because it was waived
in the postconviction court proceedings. Not so. Without questioning
the trial court’s finding that Cone’s Brady claim had been previously
determined, the Court of Criminal Appeals affirmed the denial of
                     Cite as: 556 U. S. ____ (2009)                    19

                          Opinion of the Court

Tennessee appellate court did not hold that Cone’s Brady
claim was waived.
  When a state court declines to find that a claim has
been waived by a petitioner’s alleged failure to comply
with state procedural rules, our respect for the state-court
judgment counsels us to do the same. Although we have
an independent duty to scrutinize the application of state
rules that bar our review of federal claims, Lee, 534 U. S.,
at 375, we have no concomitant duty to apply state proce
dural bars where state courts have themselves declined to
do so. The Tennessee courts did not hold that Cone
waived his Brady claim, and we will not second-guess
their judgment.14
——————
Cone’s postconviction petition in its entirety. Nothing in that decision
suggests the appellate court believed the Brady claim had been waived
in the court below.
  Similarly, while JUSTICE ALITO’s parsing of the record persuades him
that Cone failed to adequately raise his Brady claim to the Tennessee
Court of Criminal Appeals, he does not argue that the court expressly
held that Cone waived the claim. A review of Cone’s opening brief
reveals that he made a broad challenge to the postconviction court’s
dismissal of his petition and plainly asserted that the court erred by
dismissing claims as previously determined on direct appeal or in his
initial postconviction petition. See Brief for Petitioner-Appellant in No.
02–C–01–9403–CR–00052 (Tenn. Crim. App.), pp. 7, 14. The state
appellate court did not state or suggest that Cone had waived his Brady
claim. Rather, after commending the postconviction court for its
“exemplary and meticulous treatment of the appellant’s petition,” Cone,
927 S. W. 2d, at 581, the appellate court simply adopted without
modification the lower court’s findings with respect to the application of
Tenn. Code Ann. §40–30–112 to the facts of this case. The best reading
of the Tennessee Court of Criminal Appeals’ decision is that it was
based on an approval of the postconviction court’s reasoning rather
than on an unmentioned failure by Cone to adequately challenge the
dismissal of his Brady claim on appeal.
  14 Setting aside the state courts’ mistaken belief that Cone’s Brady

claim had been previously determined, there are many reasons the
state courts might have rejected the State’s waiver argument. The
record establishes that the suppressed documents which form the basis
for Cone’s claim were not available to him until the Tennessee Court of
20                          CONE v. BELL

                          Opinion of the Court

  The State’s procedural objections to federal review of the
merits of Cone’s claim have resulted in a significant delay
in bringing this unusually protracted case to a conclusion.
Ultimately, however, they provide no obstacle to judicial
review. Cone properly preserved and exhausted his Brady
claim in the state court; therefore, it is not defaulted. We
turn now to the merits of that claim.
                             V
  Although the State is obliged to “prosecute with ear
nestness and vigor,” it “is as much [its] duty to refrain
from improper methods calculated to produce a wrongful
conviction as it is to use every legitimate means to bring
about a just one.” Berger, 295 U. S., at 88. Accordingly,
we have held that when the State withholds from a crimi
nal defendant evidence that is material to his guilt or
punishment, it violates his right to due process of law in
violation of the Fourteenth Amendment. See Brady, 373
U. S., at 87. In United States v. Bagley, 473 U. S. 667, 682
(1985) (opinion of Blackmun, J.), we explained that evi
dence is “material” within the meaning of Brady when
there is a reasonable probability that, had the evidence
been disclosed, the result of the proceeding would have
been different. In other words, favorable evidence is sub
ject to constitutionally mandated disclosure when it “could
reasonably be taken to put the whole case in such a differ
——————
Appeals’ 1992 decision interpreting the State’s Public Records Act as
authorizing the disclosure of prosecutorial records. Soon after obtain
ing access to the prosecutor’s file and discovering within it documents
that had not been disclosed prior to trial, Cone amended his petition for
postconviction relief, adding detailed allegations regarding the sup
pressed evidence recovered from the file, along with an affidavit ex
plaining the reason why his claim had not been filed sooner. See App.
13, 18. The State did not oppose the amendment of Cone’s petition on
the ground that it was untimely, and it appears undisputed that there
would have been no basis under state law for doing so. See Brief for
Petitioner 7, n. 1.
                     Cite as: 556 U. S. ____ (2009)                   21

                          Opinion of the Court

ent light as to undermine confidence in the verdict.” Kyles
v. Whitley, 514 U. S. 419, 435 (1995); accord, Banks v.
Dretke, 540 U. S. 668, 698–699 (2004); Strickler v. Greene,
527 U. S. 263, 290 (1999).15
  The documents suppressed by the State vary in kind,
but they share a common feature: Each strengthens the
inference that Cone was impaired by his use of drugs
around the time his crimes were committed. The sup
pressed evidence includes statements by witnesses ac
knowledging that Cone appeared to be “drunk or high,”
App. 49, “acted real weird,” ibid., and “looked wild eyed,”
id., at 50, in the two days preceding the murders.16 It also
includes documents that could have been used to impeach
——————
  15 Although the Due Process Clause of the Fourteenth Amendment, as

interpreted by Brady, only mandates the disclosure of material evi
dence, the obligation to disclose evidence favorable to the defense may
arise more broadly under a prosecutor’s ethical or statutory obligations.
See Kyles, 514 U. S., at 437 (“[T]he rule in Bagley (and, hence, in
Brady) requires less of the prosecution than the ABA Standards for
Criminal Justice Prosecution Function and Defense Function 3–3.11(a)
(3d ed. 1993)”). See also ABA Model Rule of Professional Conduct
3.8(d) (2008) (“The prosecutor in a criminal case shall” “make timely
disclosure to the defense of all evidence or information known to the
prosecutor that tends to negate the guilt of the accused or mitigates the
offense, and, in connection with sentencing, disclose to the defense and
to the tribunal all unprivileged mitigating information known to the
prosecutor, except when the prosecutor is relieved of this responsibility
by a protective order of the tribunal”). As we have often observed, the
prudent prosecutor will err on the side of transparency, resolving
doubtful questions in favor of disclosure. See Kyles, 514 U. S., at 439;
United States v. Bagley, 473 U. S. 667, 711, n. 4 (1985) (STEVENS, J.,
dissenting); United States v. Agurs, 427 U. S. 97, 108 (1976).
  16 The State contends that the statements were made by witnesses

who observed Cone during and immediately after he committed robber
ies; therefore, it is not surprising that Cone appeared less than “se
rene.” See Brief for Respondent 46. Although a jury would have been
free to infer that Cone’s behavior was attributable to his criminal
activity, the evidence is also consistent with Cone’s assertion that he
was suffering from chronic amphetamine psychosis at the time of the
crimes.
22                          CONE v. BELL

                         Opinion of the Court

witnesses whose trial testimony cast doubt on Cone’s drug
addiction. For example, Memphis police officer Ralph
Roby testified at trial that Cone had no needle marks on
his body when he was arrested—an observation that
bolstered the State’s argument that Cone was not a drug
user. The suppressed evidence reveals, however, that
Roby authorized multiple teletypes to law enforcement
agencies in the days following the murders in which he
described Cone as a “drug user” and a “heavy drug user.”
See id., at 55–58.17 A suppressed statement made by the
chief of police of Cone’s hometown also describes Cone as a
serious drug user. See Cone, 243 F. 3d, at 968. And un
disclosed notes of a police interview with Ilene Blankman
conducted several days after the murders reveal discrep
ancies between her initial statement and her trial testi
mony relevant to Cone’s alleged drug use. App. 72–73. In
sum, both the quantity and the quality of the suppressed
evidence lends support to Cone’s position at trial that he
habitually used excessive amounts of drugs, that his ad
diction affected his behavior during his crime spree, and
that the State’s arguments to the contrary were false and
misleading.
  Thus, the federal question that must be decided is
whether the suppression of that probative evidence de
prived Cone of his right to a fair trial. See Agurs, 427
——————
   17 As the dissent points out, Roby did not testify directly that Cone

was not a drug user and FBI Agent Eugene Flynn testified that, at the
time of Cone’s arrest in Pompano Beach, Cone reported that he had
used cocaine, Dilaudid, and Demerol and was suffering from “slight
withdrawal symptoms.” See post, at 7, 11. See also Tr. 1916, 1920
(Apr. 22, 1982). It is important to note, however, that neither Flynn
nor Roby corroborated Cone’s account of alleged drug use. Taken in
context, Roby’s statement that he had not observed any needle marks
on Cone’s body invited the jury to infer that Cone’s self-reported drug
use was either minimal or contrived. See id., at 1939. Therefore,
although the suppressed evidence does not directly contradict Roby’s
trial testimony, it does place it in a different light.
                    Cite as: 556 U. S. ____ (2009)                  23

                         Opinion of the Court

U. S., at 108. Because the Tennessee courts did not reach
the merits of Cone’s Brady claim, federal habeas review is
not subject to the deferential standard that applies under
AEDPA to “any claim that was adjudicated on the merits
in State court proceedings.” 28 U. S. C. §2254(d). Instead,
the claim is reviewed de novo. See, e.g., Rompilla v.
Beard, 545 U. S. 374, 390 (2005) (de novo review where
state courts did not reach prejudice prong under Strick
land v. Washington, 466 U. S. 668 (1984)); Wiggins v.
Smith, 539 U. S. 510, 534 (2003) (same).
   Contending that the Federal District Court and Court of
Appeals adequately and correctly resolved the merits of
that claim, the State urges us to affirm the Sixth Circuit’s
denial of habeas relief. In assessing the materiality of the
evidence suppressed by the State, the Court of Appeals
suggested that two facts outweighed the potential force of
the suppressed evidence. First, the evidence of Cone’s
guilt was overwhelming. Second, the evidence of Cone’s
drug use was cumulative because the jury had heard
evidence of Cone’s alleged addiction from witnesses and
from officers who interviewed Cone and recovered drugs
from his vehicle.18 The Court of Appeals did not thor
oughly review the suppressed evidence or consider what
its cumulative effect on the jury would have been. More
over, in concluding that the suppressed evidence was not
material within the meaning of Brady, the court did not
distinguish between the materiality of the evidence with
respect to guilt and the materiality of the evidence with
respect to punishment—an omission we find significant.
   Evidence that is material to guilt will often be material
——————
  18 In pointing to the trial evidence of Cone’s drug use, the Court of

Appeals made no mention of the fact that the State had discredited the
testimony of Cone’s experts on the ground that no independent evi
dence corroborated Cone’s alleged addiction and that the State had
argued that the drugs in Cone’s car were intended for resale, rather
than personal use.
24                     CONE v. BELL

                     Opinion of the Court

for sentencing purposes as well; the converse is not always
true, however, as Brady itself demonstrates. In our semi
nal case on the disclosure of prosecutorial evidence, defen
dant John Brady was indicted for robbery and capital
murder. At trial, Brady took the stand and confessed to
robbing the victim and being present at the murder but
testified that his accomplice had actually strangled the
victim. Brady v. State, 226 Md. 422, 425, 174 A. 2d 167,
168 (1961). After Brady was convicted and sentenced to
death he discovered that the State had suppressed the
confession of his accomplice, which included incriminating
statements consistent with Brady’s version of events. Id.,
at 426, 174 A. 2d, at 169. The Maryland Court of Appeals
concluded that Brady’s due process rights were violated by
the suppression of the accomplice’s confession but declined
to order a new trial on guilt. Observing that nothing in
the accomplice’s confession “could have reduced . . .
Brady’s offense below murder in the first degree,” the
state court ordered a new trial on the question of punish
ment only. Id., at 430, 174 A. 2d, at 171. We granted
certiorari and affirmed, rejecting Brady’s contention that
the state court’s limited remand violated his constitutional
rights. 373 U. S., at 88.
   As in Brady, the distinction between the materiality of
the suppressed evidence with respect to guilt and punish
ment is significant in this case. During the guilt phase of
Cone’s trial, the only dispute was whether Cone was “sane
under the law,” Tr. 2040 (Apr. 22, 1982), as his counsel
described the issue, or “criminally responsible” for his
conduct, App. 110, as the prosecutor argued. Under Ten
nessee law, Cone could not be held criminally responsible
for the murders if, “at the time of [his] conduct as a result
of mental disease or defect he lack[ed] substantial capacity
either to appreciate the wrongfulness of his conduct or to
conform his conduct to the requirements of law.” Graham
v. State, 547 S. W. 2d 531, 543 (Tenn. 1977). Although we
                 Cite as: 556 U. S. ____ (2009)          25

                     Opinion of the Court

take exception to the Court of Appeals’ failure to assess
the effect of the suppressed evidence “collectively” rather
than “item by item,” see Kyles, 514 U. S., at 436, we never
theless agree that even when viewed in the light most
favorable to Cone, the evidence falls short of being suffi
cient to sustain his insanity defense.
   Cone’s experts testified that his drug addiction and
posttraumatic stress disorder originated during his service
in Vietnam, more than 13 years before the Todds were
murdered. During those years, despite Cone’s drug use
and mental disorder, he managed to successfully complete
his education, travel, and (when not incarcerated) function
in civil society. The suppressed evidence may have
strengthened the inference that Cone was on drugs or
suffering from withdrawal at the time of the murders, but
his behavior before, during, and after the crimes was
inconsistent with the contention that he lacked substan
tial capacity either to appreciate the wrongfulness of his
conduct or to conform his conduct to the requirements of
law. See Graham, 547 S. W. 2d, at 543. The likelihood
that the suppressed evidence would have affected the
jury’s verdict on the issue of insanity is therefore remote.
Accordingly, we conclude that the Sixth Circuit did not err
by denying habeas relief on the ground that the sup
pressed evidence was immaterial to the jury’s finding of
guilt.
   The same cannot be said of the Court of Appeals’ sum
mary treatment of Cone’s claim that the suppressed evi
dence influenced the jury’s sentencing recommendation.
There is a critical difference between the high standard
Cone was required to satisfy to establish insanity as a
matter of Tennessee law and the far lesser standard that a
defendant must satisfy to qualify evidence as mitigating in
a penalty hearing in a capital case. See Bell, 535 U. S., at
712 (STEVENS, J., dissenting) (“[T]here is a vast difference
between insanity—which the defense utterly failed to
26                         CONE v. BELL

                         Opinion of the Court

prove—and the possible mitigating effect of drug addiction
incurred as a result of honorable service in the military”).
As defense counsel emphasized in his brief opening state
ment during penalty phase proceedings, the jury was
statutorily required to consider whether Cone’s “capacity
. . . to appreciate the wrongfulness of his conduct or to
conform his conduct to the requirements of the law was
substantially impaired as a result of mental disease or
defect or intoxication which was insufficient to establish a
defense to the crime but which substantially affected his
judgment.” Tenn. Code Ann. §39–2–203(j)(8) (1982). It is
possible that the suppressed evidence, viewed cumula
tively, may have persuaded the jury that Cone had a far
more serious drug problem than the prosecution was
prepared to acknowledge, and that Cone’s drug use played
a mitigating, though not exculpating, role in the crimes he
committed.19 The evidence might also have rebutted the
State’s suggestion that Cone had manipulated his expert
witnesses into falsely believing he was a drug addict when
in fact he did not struggle with substance abuse.
    Neither the Court of Appeals nor the District Court fully
considered whether the suppressed evidence might have
persuaded one or more jurors that Cone’s drug addiction—
especially if attributable to honorable service of his coun
try in Vietnam—was sufficiently serious to justify a deci
sion to imprison him for life rather than sentence him to
death. Because the evidence suppressed at Cone’s trial

——————
  19 We agree with the dissent that the standard to be applied by the

District Court in evaluating the merits of Cone’s Brady claim on re
mand is whether there is a reasonable probability that, had the sup
pressed evidence been disclosed, the result of the proceeding would
have been different. See post, at 5. Because neither the District Court
nor the Court of Appeals considered the merits of Cone’s claim with
respect to the effect of the withheld evidence on his sentence, it is
appropriate for the District Court, rather than this Court, to do so in
the first instance.
                 Cite as: 556 U. S. ____ (2009)           27

                     Opinion of the Court

may well have been material to the jury’s assessment of
the proper punishment in this case, we conclude that a
full review of the suppressed evidence and its effect is
warranted.
                             VI
  In the 27 years since Gary Cone was convicted of mur
der and sentenced to death, no Tennessee court has
reached the merits of his claim that state prosecutors
withheld evidence that would have bolstered his defense
and rebutted the State’s attempts to cast doubt on his
alleged drug addiction. Today we hold that the Tennessee
courts’ procedural rejection of Cone’s Brady claim does not
bar federal habeas review of the merits of that claim.
Although we conclude that the suppressed evidence was
not material to Cone’s conviction for first-degree murder,
the lower courts erred in failing to assess the cumulative
effect of the suppressed evidence with respect to Cone’s
capital sentence. Accordingly, the judgment of the Court
of Appeals is vacated, and the case is remanded to the
District Court with instructions to give full consideration
to the merits of Cone’s Brady claim.
                                            It is so ordered.
                  Cite as: 556 U. S. ____ (2009)            1

              ROBERTS, C. J., concurring in judgment

SUPREME COURT OF THE UNITED STATES
                           _________________

                          No. 07–1114
                           _________________


   GARY BRADFORD CONE, PETITIONER v. RICKY 

               BELL, WARDEN

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE SIXTH CIRCUIT

                         [April 28, 2009] 


  CHIEF JUSTICE ROBERTS, concurring in the judgment.
  The Court’s decision is grounded in unusual facts that
necessarily limit its reach. When issues under Brady v.
Maryland, 373 U. S. 83 (1963), are presented on federal
habeas, they usually have been previously addressed in
state proceedings. Federal review is accordingly sharply
limited by established principles of deference: If the claim
has been waived under state rules, that waiver typically
precludes federal review. If the claim has been decided in
the state system, federal review is restricted in light of the
state court’s legal and factual conclusions. The unique
procedural posture of this case presents a Brady claim
neither barred under state rules for failure to raise it nor
decided in the state system.
  When it comes to that claim, the Court specifies that the
appropriate legal standard is the one we set forth in Kyles
v. Whitley, 514 U. S. 419, 435 (1995) (whether “the favor
able evidence could reasonably be taken to put the whole
case in such a different light as to undermine confidence
in the verdict”). See ante, at 20–21, 26, n. 19. I do not
understand the majority to depart from that standard, and
the majority certainly does not purport to do so.
  That leaves only application of the accepted legal stan
dard to the particular facts. It is highly unusual for this
Court to engage in such an enterprise, see Kyles, supra, at
2                        CONE v. BELL

              ROBERTS, C. J., concurring in judgment

458 (SCALIA, J., dissenting), and the Court’s asserted basis
for doing so in this case is dubious, see post, at 1, 4–5
(THOMAS, J., dissenting).
  In any event, the Court’s review of the facts does not
lead it to conclude that Cone is entitled to relief—only that
the courts below did not adequately consider his claim
with respect to sentencing. See ante, at 26 (“Neither the
Court of Appeals nor the District Court fully considered
whether the suppressed evidence” undermines confidence
in Cone’s sentence). The Court simply reviews the facts in
the light most favorable to Cone, concludes that the evi
dence does not undermine confidence in the jury’s deter
mination that Cone is guilty, but sends the case back for
“full consideration” of whether the same is true as to the
jury’s sentence of death. Ante, at 25–27.
  So this is what we are left with: a fact-specific determi
nation, under the established legal standard, viewing the
unique facts in favor of the defendant, that the Brady
claim fails with respect to guilt, but might have merit as
to sentencing. In light of all this, I see no reason to quar
rel with the Court’s ruling on the Brady claim.
  In considering on remand whether the facts establish a
Brady violation, it is clear that the lower courts should
analyze the issue under the constitutional standards we
have set forth, not under whatever standards the Ameri
can Bar Association may have established. The ABA
standards are wholly irrelevant to the disposition of this
case, and the majority’s passing citation of them should
not be taken to suggest otherwise. See ante, at 21, n. 15.
                    Cite as: 556 U. S. ____ (2009)                  1

                         Opinion of ALITO, J.

SUPREME COURT OF THE UNITED STATES
                             _________________

                            No. 07–1114
                             _________________


   GARY BRADFORD CONE, PETITIONER v. RICKY 

               BELL, WARDEN

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE SIXTH CIRCUIT

                           [April 28, 2009] 


   JUSTICE ALITO, concurring in part and dissenting in
part.
   We granted certiorari in this case to answer two ques­
tions:
     “1. Is a federal habeas claim ‘procedurally defaulted’
     because it has been presented twice to the state
     courts?
     “2. Is a federal habeas court powerless to recognize
     that a state court erred in holding that state law pre­
     cludes reviewing a claim?” Pet. for Cert. i.
   Both of these questions are based on a factually incor­
rect premise, namely, that the Tennessee Court of Crimi­
nal Appeals, the highest state court to entertain peti­
tioner’s appeal from the denial of his second petition for
state postconviction relief,1 rejected petitioner’s Brady2
claim on the ground that the claim had been previously

——————
  1 Because  the Tennessee Supreme Court denied discretionary review
of the decision of the Tennessee Court of Criminal Appeals decision
affirming the denial of petitioner’s second amended petition for post­
conviction relief, we must look to the decision of the latter court to
determine if the decision below was based on an adequate and inde­
pendent state ground. See Baldwin v. Reese, 541 U. S. 27, 30–32
(2004); O’Sullivan v. Boerckel, 526 U. S. 838, 842–843 (1999).
  2 Brady v. Maryland, 373 U. S. 83 (1963).
2                      CONE v. BELL

                      Opinion of ALITO, J.

decided by the Tennessee Supreme Court in petitioner’s
direct appeal. Petitioner’s argument is that the State
Supreme Court did not decide any Brady issue on direct
appeal, that the Tennessee Court of Criminal Appeals
erred in holding otherwise, and that the Sixth Circuit
erred in concluding that the Brady claim had been proce­
durally defaulted on this ground. Petitioner is quite cor­
rect that his Brady claim was not decided on direct appeal,
and the Court in the present case is clearly correct in
holding that a second attempt to litigate a claim in state
court does not necessarily bar subsequent federal habeas
review. See ante, at 8–9.
  But all of this is beside the point because the Tennessee
Court of Criminal Appeals did not reject petitioner’s Brady
claim on the ground that the claim had been previously
determined on direct appeal. Rather, petitioner’s Brady
claim was simply never raised before the Tennessee Court
of Criminal Appeals, and that court did not rule on the
claim at all.
  Because the Sixth Circuit’s decision on the issue of
procedural default rests on the same mistaken premise
that the Tennessee Court of Criminal Appeals rejected
petitioner’s Brady claim on the ground that it had been
previously determined, I entirely agree with the majority
that the Sixth Circuit’s decision on that issue cannot be
sustained and that a remand is required. I cannot join the
Court’s opinion, however, for two chief reasons.
  First, the Court states without explanation that “Cone
properly preserved and exhausted his Brady claim in the
state court” and that therefore the claim has not been
defaulted. Ante, at 20. Because Cone never fairly raised
this claim in the Tennessee Court of Criminal Appeals, the
claim is either not exhausted (if Cone could now raise the
claim in state court) or is procedurally defaulted (if state
law now provides no avenue for further review). I would
leave these questions for resolution in the first instance on
                 Cite as: 556 U. S. ____ (2009)            3

                      Opinion of ALITO, J.

remand.
  Second, the Court, again without explanation, remands
this case to the District Court, not the Court of Appeals. I
see no justification for this step.
                              I
  In order to understand the tangled procedural default
issue presented in this case, it is necessary to review the
far-from-exemplary manner in which the attorneys for
petitioner and respondent litigated the Brady claim in the
state courts.
  On direct appeal, petitioner did not raise any Brady
claim. As the Court notes, petitioner did claim that the
State had violated a state discovery rule by failing to
provide prior statements given by certain witnesses and
that therefore the testimony of these witnesses should
have been stricken. App. 114–117; State v. Cone, 665
S. W. 2d 87, 94 (Tenn. 1984). Although this claim con­
cerned the State’s failure to turn over information, it is
clear that this was not a Brady claim.
  The first appearance of anything resembling the claim
now at issue occurred in 1993 when petitioner’s experi­
enced attorneys filed an amendment to his second petition
for postconviction relief in the Shelby County Criminal
Court. This petition included a long litany of tangled
claims. Paragraph 35 of this amended petition claimed,
among other things, that the State had wrongfully with­
held information demonstrating that one particular prose­
cution witness had testified falsely concerning “petitioner
and his drug use.” App. 13–14. This nondisclosure, the
petition stated, violated not only the Fifth and Fourteenth
Amendments to the Constitution of the United States
(which protect the due process right on which Brady is
based) but also the Fourth, Sixth, and Eighth Amend­
ments to the United States Constitution and four provi­
sions of the Tennessee Constitution.
4                          CONE v. BELL

                         Opinion of ALITO, J.

   Two months later, counsel for petitioner filed an
amendment adding 12 more claims, including one (¶41)
alleging that the State had abridged petitioner’s rights by
failing to disclose evidence that petitioner suffered from
drug problems. Id., at 20. According to this new submis­
sion, the nondisclosure violated, in addition to the previ­
ously cited provisions of the federal and state constitu­
tions, five more provisions of the state constitution,
including provisions regarding double jeopardy, see Tenn.
Const., Art. I, §10, ex post facto laws, §11, indictment, §14,
and open courts, §17.
   The Shelby County Criminal Court was faced with the
task of wading through the morass presented in the
amended petition. Under Tenn. Code Ann. §40–30–112
(1990) (repealed 1995),3 a claim could not be raised in a
postconviction proceeding if the claim had been “previ­
ously determined” or waived. Citing the State Supreme
Court’s rejection on direct appeal of petitioner’s claim that
the prosecution had violated a state discovery rule by
failing to turn over witness statements, the State incor­
rectly informed the court that the failure-to-disclose­
exculpatory-evidence claim set out in ¶41 had been “previ­
ously determined” on direct appeal. App. 15–16. The
Shelby County Criminal Court rejected the claim on this
ground, and held that all of petitioner’s claims had either
been previously determined or waived. Id., at 22.
   Given the importance now assigned to petitioner’s
Brady claim, one might think that petitioner’s attorneys
would have (a) stressed that claim in the opening brief
that they filed in the Tennessee Court of Criminal Ap­
——————
   3 Tennessee law has since changed. Currently, the Tennessee Post-

Conviction Procedure Act bars any second postconviction petition, see
Tenn. Code Ann. §40–30–102 (2006), and permits the reopening of a
petition only under limited circumstances, §40–30–117. These restric­
tions apply to any petition filed after the enactment of the Post-
Conviction Procedure Act, even if the conviction occurred long before.
                     Cite as: 556 U. S. ____ (2009)                     5

                          Opinion of ALITO, J.

peals, (b) pointed out the lower court’s clear error in con­
cluding that this claim had been decided in the direct
appeal, and (c) explained that information supporting the
claim had only recently come to light due to the production
of documents under the State’s public records act. But
counsel did none of these things. In fact, the Brady claim
was not mentioned at all.
  Nor was Brady cited in the reply brief filed by the same
attorneys. The reply brief did contain a passing reference
to “the withholding of exculpatory evidence,” but the brief
did not elaborate on this claim and again failed to mention
that this claim had never been previously decided and was
supported by newly discovered evidence.4
  The Tennessee Court of Criminal Appeals affirmed the
decision of the lower state court, but the appellate court
made no mention of the Brady claim, and I see no basis for
concluding that the court regarded the issue as having
been raised on appeal.
  Appellate courts generally do not reach out to decide
issues not raised by the appellant. Snell v. Tunnell, 920
F. 2d 673, 676 (CA10 1990); see Powers v. Hamilton Cty.
Public Defender Comm’n, 501 F. 3d 592, 609–610 (CA6
2007); see also Galvan v. Alaska Dept. of Corrections, 397
F. 3d 1198, 1204 (CA9 2005) (“Courts generally do not
decide issues not raised by the parties. If they granted
relief to petitioners on grounds not urged by petitioners,

——————
   4 After referring to a long list of claims (not including any claim for

the failure to disclose exculpatory evidence), the reply brief states:
“[I]t is clear that meritorious claims have been presented for adjudica­
tion. These claims have not been waived and a remand for a hearing is
essential in order to enable Mr. Cone to present evidence and prove the
factual allegations, including those relating to his claims of ineffective
assistance of counsel, Petition ¶¶15, 16, 44, R–67, 71 and 141 and of the
withholding of exculpatory evidence. Petition ¶41, R–139.” Reply Brief
of Petitioner-Appellant in No. 02–C–01–9403–CR–0052, p. 5 (emphasis
added) (hereinafter Reply Brief).
6                          CONE v. BELL

                          Opinion of ALITO, J.

respondents would be deprived of a fair opportunity to
respond, and the courts would be deprived of the benefit of
briefing” (footnote omitted)). Nor do they generally con­
sider issues first mentioned in a reply brief. Physicians
Comm. For Responsible Medicine v. Johnson, 436 F. 3d
326, 331, n. 6 (CA2 2006); Doe v. Beaumont Independent
School Dist., 173 F. 3d 274, 299, n. 13 (CA5 1999) (Garza,
J., dissenting); Doolin Security Sav. Bank, F. S. B. v.
Office of Thrift Supervision, 156 F. 3d 190, 191 (CADC
1998); Boone v. Carlsbad Bancorporation, Inc., 972 F. 2d
1545, 1554, n. 6 (CA10 1992). And it is common to prac­
tice for appellate courts to refuse to consider issues that
are mentioned only in passing. Reynolds v. Wagner, 128
F. 3d 166, 178 (CA3 1997) (citing authorities).
   The Tennessee Court of Criminal Appeals follows these
standard practices. Rule 10(b) of that court states quite
specifically: “Issues which are not supported by argument,
citation to authorities, or appropriate references to the
record will be treated as waived in this court.” The court
has applied this rule in capital cases, State v. Dellinger, 79
S. W. 3d 458, 495, 497, 503 (Tenn. 2002) (appendix to
majority opinion); Brimmer v. State, 29 S. W. 3d 497, 530
(1998), and in others. See, e.g., State v. Faulkner, 2001
WL 378540 (Tenn. Crim. App., Sept. 10, 2001) (73-year
sentence for first-degree murder). And in both capital and
noncapital cases, the court has refused to entertain
arguments raised for the first time in a reply brief. See
State v. Gerhardt, 2009 WL 160930 (Tenn. Crim. App.,
Jan. 23, 2009) (capital case); Carruthers v. State, 814 S. W.
2d 64, 68 (Tenn. Crim. App. 1991) (capital case); Cammon
v. State, 2007 WL 2409568, *6 (Tenn. Crim. App., Aug. 23,
2007) (noncapital case).5 Thus, unless the Tennessee
——————
  5 In a footnote in his reply brief, petitioner stated that he was not

waiving any claim presented in the court below and asked the appellate
court to consider all those claims. See Reply Brief 3, n. 1. But the
                    Cite as: 556 U. S. ____ (2009)                  7

                         Opinion of ALITO, J.

Court of Criminal Appeals departed substantially from its
general practice, that court did not regard petitioner’s
Brady claim as having been raised on appeal.
   In the decision now under review, the Sixth Circuit held
that “[t]he Tennessee courts found that Cone’s Brady
claims were ‘previously determined’ and, therefore, not
cognizable in [his] state post-conviction action.” 492 F. 3d
743, 756 (2007). In my judgment, however, there is no
basis for concluding that the Tennessee Court of Criminal
Appeals thought that any Brady issue was before it. A
contrary interpretation would mean that the Tennessee
Court of Criminal Appeals, disregarding its own rules and
standard practice, entertained an issue that was not men­
tioned at all in the appellant’s main brief and was men­
tioned only in passing and without any development in the
reply brief. It would mean that the Tennessee Court of
Criminal Appeals, having chosen to delve into the Brady
issue on its own, ruled on the issue without even mention­
ing it in its opinion and without bothering to check the
record to determine whether in fact the Brady issue had
been decided on direct appeal. Such an interpretation is
utterly implausible, and it is telling that the majority
in this case cites no support for such an interpretation in
the opinion of the Tennessee Court of Criminal Appeals’
opinion.
   The Sixth Circuit’s decision on the question of proce­
dural default rests on an erroneous premise and must
therefore be vacated.
                           II
  I also agree with the Court that we should not affirm
the decision below on the ground that the Brady claim
lacks substantive merit. After its erroneous discussion of
——————
Tennessee Court of Criminal Appeals has specifically held that claims
may not be raised on appeal in this manner. See Leonard v. State, 2007
WL 1946662, *21–*22 (Tenn. Crim. App., July 5, 2007).
8                          CONE v. BELL

                          Opinion of ALITO, J.

procedural default, the Sixth Circuit went on to discuss
the merits of petitioner’s Brady claim. In its 2001 opinion,
the Court of Appeals recognized that the prosecution’s
Brady obligation extends not only to evidence that is
material to guilt but also to evidence that is material to
punishment. See Cone v. Bell, 243 F. 3d 961, 968 (2001)
(citing Pennsylvania v. Ritchie, 480 U. S. 39, 57 (1987)).
But neither in that opinion nor in its 2006 opinion did the
court address the materiality of the information in ques­
tion here in relation to petitioner’s punishment. See 492
F. 3d, at 756 (“A review of the allegedly withheld docu­
ments shows that this evidence would not have overcome
the overwhelming evidence of Cone’s guilt in committing a
brutal double murder and the persuasive testimony that
Cone was not under the influence of drugs” (emphasis
added)). Therefore, despite the strength of the arguments
in JUSTICE THOMAS’ dissent, I would leave that question to
be decided by the Sixth Circuit on remand.
                             III
   The Court, however, does not simply vacate and remand
to the Sixth Circuit but goes further.
   First, the Court states without elaboration that peti­
tioner “preserved and exhausted his Brady claim in the
state court.” Ante, at 20. As I have explained, petitioner
did not fairly present his Brady claim in his prior appeal
to the Tennessee Court of Criminal Appeals, and therefore
that claim is either unexhausted or procedurally barred.
If the State is not now foreclosed from relying on the
failure to exhaust, see 28 U. S. C. §2254(b)(3), or on proce­
dural default,6 those questions may be decided on remand.
——————
  6 Unlike exhaustion, procedural default may be waived if it is not

raised as a defense. Banks v. Dretke, 540 U. S. 668, 705 (2004) (allow­
ing for waiver of “procedural default” “based on the State’s litigation
conduct” (citing Gray v. Netherland, 518 U. S. 152, 166 (1996))). Here,
it appears that the State has consistently argued that petitioner’s
                   Cite as: 556 U. S. ____ (2009)                 9

                        Opinion of ALITO, J.

   Second, the Court remands the case to the District
Court rather than the Court of Appeals. A remand to the
District Court would of course be necessary if petitioner
were entitled to an evidentiary hearing, but the Court
does not hold that an evidentiary hearing is either re­
quired or permitted. In my view, unless there is to be an
evidentiary hearing, there is no reason to remand this
case to the District Court. If the only purpose of remand is
to require an evaluation of petitioner’s Brady claim in
light of the present record, the District Court is not in a
superior position to conduct such a review. And even if
such a review is conducted in the first instance by the
District Court, that court’s decision would be subject to de
novo review in the Court of Appeals. 492 F. 3d, at 750;
Cone v. Bell, 243 F. 3d, at 966–967 (CA6 2001); see United
States v. Graham, 484 F. 3d 413 (CA6 2007); United States
v. Miller, 161 F. 3d 977, 987 (CA6 1998); United States v.
Phillip, 948 F. 2d 241, 250 (CA6 1991). Accordingly, I see
no good reason for remanding to the District Court rather
than the Court of Appeals. And if the majority has such a
reason, it is one that it has chosen to keep to itself.
                       *   *     *
  For these reasons, I would vacate the decision of the
Court of Appeals and remand to that court.




——————
Brady claim was procedurally defaulted, but the State’s supporting
arguments have shifted. Whether the question of procedural default
described in this opinion should be entertained under the particular
circumstances here is an intensely fact-bound matter that should be
left for the Sixth Circuit on remand.
                 Cite as: 556 U. S. ____ (2009)            1

                    THOMAS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 07–1114
                         _________________


   GARY BRADFORD CONE, PETITIONER v. RICKY 

               BELL, WARDEN

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE SIXTH CIRCUIT

                        [April 28, 2009] 


   JUSTICE THOMAS, with whom JUSTICE SCALIA joins,
dissenting.
   The Court affirms Gary Cone’s conviction for beating an
elderly couple to death with a blunt object. In so doing,
the majority correctly rejects Cone’s argument that his
guilty verdict was secured in violation of his rights under
Brady v. Maryland, 373 U. S. 83 (1963). The majority
declines, however, to decide whether the same evidence
that was insufficient under Brady to overturn his convic
tion provides a basis for overturning his death sentence.
The majority instead remands this question to the District
Court for further consideration because it finds that the
Court of Appeals engaged in a “summary treatment” of
Cone’s Brady sentencing claim. See ante, at 25–27.
   I respectfully dissent. The Court of Appeals’ allegedly
“summary treatment” of Cone’s sentencing claim does not
justify a remand to the District Court. Cone has failed to
establish “ ‘a reasonable probability that, had the evidence
been disclosed to the defense, the result of the [sentencing]
proceeding would have been different,’ ” Kyles v. Whitley,
514 U. S. 419, 435 (1995) (quoting United States v. Bagley,
473 U. S. 667, 682 (1985) (opinion of Blackmun, J.)). As a
result, I would affirm the judgment of the Court of Ap
2                           CONE v. BELL

                         THOMAS, J., dissenting

peals. 1
                                I
   This case arises from a crime spree 28 years ago that
began with Cone’s robbery of a jewelry store in Memphis,
Tennessee, and concluded with his robbery of a drugstore
in Pompano Beach, Florida. Along the way, Cone shot a
police officer and a bystander while trying to escape the
first robbery, attempted to shoot another man in a failed
carjacking attempt, unsuccessfully tried to force his way
into a woman’s apartment at gunpoint, and murdered 93
year-old Shipley Todd and his 79-year-old wife, Cleopatra.
When he was tried on two counts of first-degree murder in
1982, Cone’s sole defense was that he did not have the
requisite intent to commit first-degree murder because
he was in the grip of a chronic amphetamine psychosis.
The jury rejected the defense and convicted Cone of both
murders.
   At sentencing, the Tennessee jury found beyond a rea
sonable doubt that four statutory aggravating factors
applied to Cone’s offense: (1) Cone had been convicted of
one or more previous felonies involving the use or threat of
violence; (2) he had knowingly created a great risk of
death to two or more persons other than the victim during
his act of murder; (3) the murder was especially heinous,
atrocious or cruel in that it involved torture or depravity of
mind; and (4) the murder was committed for the purpose
of avoiding a lawful arrest. Tr. 2151–2152 (Apr. 23, 1982);
see also State v. Cone, 665 S. W. 2d 87, 94–96 (Tenn.


——————
   1 Because I would affirm on the basis of the Court of Appeals’ alterna

tive holding below, I do not reach the issues of procedural default
resolved by the majority. See United States v. Atlantic Research Corp.,
551 U. S. 128, 141, n. 8 (2007); Ayotte v. Planned Parenthood of North
ern New Eng., 546 U. S. 320, 332 (2006); Ardestani v. INS, 502 U. S.
129, 139 (1991).
                    Cite as: 556 U. S. ____ (2009)                   3

                        THOMAS, J., dissenting

1984). Tenn. Code Ann. §39–2-203(i) (1982).2 Cone ar
gued to the jury at sentencing that his “capacity . . . to
appreciate the wrongfulness of his conduct or to conform
his conduct to the requirements of the law was substan
tially impaired as a result of mental disease or defect or
intoxication which was insufficient to establish a defense
to the crime but which substantially affected his judg
ment.” See §39–2-203(j)(8). But the jury found that nei
ther this, nor any other mitigating factor, outweighed the
aggravating factors. The jury, as required by Tennessee
law, unanimously sentenced Cone to death. See §39–2
203(g).
   For almost three decades, Cone’s case has traveled
through the Tennessee and federal courts. This Court has
twice reversed decisions from the Court of Appeals that
invalidated Cone’s conviction and sentence. See Bell v.
Cone, 535 U. S. 685 (2002); Bell v. Cone, 543 U. S. 447
(2005) (per curiam). On remand from this Court’s latest
decision, the Court of Appeals directly considered whether
a handful of police reports, law enforcement bulletins, and
notes that were allegedly withheld from Cone’s trial attor
neys could have changed the result of Cone’s trial or sen
tencing. And, for the second time, the Court of Appeals
held that there was not a “ ‘reasonable probability’ ” that
the evidence would have altered the jury’s conclusion “that
Cone’s prior drug use did not vitiate his specific intent to
murder his victims and did not mitigate his culpability
sufficient to avoid the death sentence.” 492 F. 3d 743, 757
(CA6 2007). The Court of Appeals, therefore, held that
neither Cone’s conviction nor his sentence was invalid.
——————
  2 The Tennessee Supreme Court later concluded that the record in

Cone’s case was doubtful as to evidence supporting the second circum
stance given the lapse in time between the initial events of the escape
and the Todd murders. Cone, 665 S. W. 2d, at 95. The court, however,
determined that the existence of the other three factors rendered any
possible error in this factor harmless beyond a reasonable doubt. Ibid.
4                       CONE v. BELL

                     THOMAS, J., dissenting

See ibid.; Cone v. Bell, 243 F. 3d 961, 968 (CA6 2001). We
should affirm the Court of Appeals and put an end to this
litigation.
                               II
    According to the majority, the Court of Appeals’ decision
affirming Cone’s death sentence is too “summary,” ante, at
25, and the facts are such that, on further examination,
Cone “might” be able to demonstrate that it is “possible”
that the contested evidence would have persuaded the jury
to spare his life, ante, at 25–26. On this reasoning, the
majority remands the case directly to the District Court
for “full consideration [of] the merits of Cone’s [sentencing]
claim.” Ante, at 27. I disagree on all counts. Remanding
the sentencing issue to the District Court is an “unusual
step” for this Court to take. House v. Bell, 547 U. S. 518,
557 (2006) (ROBERTS, C. J., concurring in judgment in part
and dissenting in part). Furthermore, in this case, it is a
step that is legally and factually unjustified. There is not
“ ‘a reasonable probability that, had the evidence been
disclosed to the defense, the result of the proceeding would
have been different.’ ” Kyles, 514 U. S., at 433–434 (quot
ing Bagley, 473 U. S., at 682 (opinion of Blackmun, J.)).
                            A
  The majority’s criticism of the Court of Appeals’ alleg
edly “summary treatment” of the sentencing question is
misplaced. Before the Court of Appeals, Cone dedicated
eight pages of his opening brief to arguing that the impli
cated evidence was material to his guilt or innocence, but
spent only one paragraph arguing its materiality to his
death sentence. See Brief for Appellant in No. 99–5279
(CA6), pp. 40–48. The Court of Appeals’ focus on the guilt
phase, rather than the sentencing phase, simply followed
Cone’s lead. See 492 F. 3d, at 755 (“In his most recent
brief, claiming that his receiving the withheld evidence
                     Cite as: 556 U. S. ____ (2009)                     5

                         THOMAS, J., dissenting

would have resulted in a different sentence, Cone has
made only conclusory arguments”).3        There is nothing
defective about a judicial decision that summarily rejects
an abbreviated legal argument, especially where, as here,
the burden of proving the materiality of the contested
evidence was on Cone.4
                             B
  In remanding this matter to the District Court, the
majority makes two critical errors—one legal and one
factual—that leave the false impression that Cone’s Brady
claim has a chance of success. First, the majority states
that “[i]t is possible that the suppressed evidence” may
have convinced the jury that Cone’s substance abuse
played a mitigating role in his crime and “[t]he evidence
might also have rebutted the State’s suggestion” that
Cone’s experts were inaccurately depicting the depth of his
drug-induced impairment. Ante, at 26 (emphasis added);
see also ante, at 26–27 (remanding “[b]ecause the evidence
suppressed at Cone’s trial may well have been material to
the jury’s assessment of the proper punishment in this
case” (emphasis added)). But, as the majority implicitly
——————
  3 The assertion by the majority, ante, at 26, n. 19, and JUSTICE ALITO,

ante, at 8 (opinion concurring in part and dissenting in part), that the
Court of Appeals did not address the merits of the sentencing issue at
all is flatly wrong. See 492 F. 3d, at 757 (rejecting Cone’s Brady claim
because the proffered evidence would not have altered the jury’s con
clusion “that Cone’s prior drug use did not vitiate his specific intent to
murder his victims and did not mitigate his culpability sufficient to
avoid the death sentence” (emphasis added)).
  4 The majority does not attempt to justify its remand by contending

that it is necessary because the record is insufficient to decide the
claim. Nor could it persuasively contend a remand is necessary so that
the District Court can hold an evidentiary hearing. Such a hearing
would shed no additional light on the trial proceedings or the relative
impeachment value of the withheld documents. Cone himself agrees
that “this Court should resolve the merits of [his] Brady claim.” Reply
Brief for Petitioner 24; see also Brief for Respondent 26–27.
6                       CONE v. BELL

                     THOMAS, J., dissenting

acknowledges, see ante, at 26, n. 19, this is not the correct
legal test for evaluating a Brady claim: “The mere possibil
ity that an item of undisclosed information might have
helped the defense, or might have affected the outcome of
the trial, does not establish ‘materiality’ in the constitu
tional sense.” United States v. Agurs, 427 U. S. 97, 109–
110 (1976) (emphasis added).
   Rather, this Court has made clear that the legal stan
dard for adjudicating such a claim is whether there is a
“reasonable probability” that the jury would have been
persuaded by the allegedly withheld evidence. Kyles,
supra, at 435; Bagley, supra, at 682 (opinion of Blackmun,
J.). It simply is not sufficient, therefore, to claim that
“there is a reasonable possibility that . . . testimony might
have produced a different result . . . . [P]etitioner’s burden
is to establish a reasonable probability of a different re
sult.” Strickler v. Greene, 527 U. S. 263, 291 (1999) (em
phasis in original). To satisfy the “reasonable probability”
standard, Cone must show that “the favorable evidence
could reasonably be taken to put the whole case in such a
different light as to undermine confidence” in the jury’s
sentencing determination. Kyles, supra, at 435. The
Court must view the record “as a whole,” Sawyer v.
Whitley, 505 U. S. 333, 374 (1992) (STEVENS, J., concur
ring in judgment), and determine whether the absence of
the disclosure prevented Cone from receiving “ ‘a trial
resulting in a [sentence] worthy of confidence.’ ” Strickler,
supra, at 290 (quoting Kyles, 514 U. S., at 434).
   In the context of this case, for Cone to establish “ ‘a
reasonable probability that, had the evidence been dis
closed to the defense, the result of the [sentencing] pro
ceeding would have been different,’ ” id., at 435, he must
not only demonstrate that the withheld evidence would
have established that he was substantially impaired as a
result of drug abuse or withdrawal; Cone also must estab
lish that the addition of the allegedly withheld evidence
                      Cite as: 556 U. S. ____ (2009)                     7

                         THOMAS, J., dissenting

ultimately would have led the jury to conclude that any
mitigating factors (including substantial impairment)
outweighed all of the established aggravating factors. See
Tenn. Code Ann. §39–2-203(g).5
   Second, the majority incorrectly claims that to prevail
on his Brady claim, Cone must demonstrate simply that
the withheld evidence supported the inference that he
“was impaired by his use of drugs around the time his
crimes were committed.” See ante, at 21. This is factually
inaccurate because there was already significant evidence
of Cone’s drug use at trial. To establish that the allegedly
withheld evidence would reasonably have had any impact
on his case, Cone must instead show that the evidence
would have supported his claim of substantial mental
impairment from drug use.
   There was extensive evidence at trial that supported the
inference that Cone was not only a longstanding drug
user, but that he was in fact using drugs at the time of his
crimes. The State itself presented significant evidence on
this point. For example, it presented proof that officers
found marijuana cigarette butts, empty drug vials, and
loose syringes in the car that Cone abandoned immedi
ately after the jewelry store robbery. Tr. 1505–1509 (Apr.
19, 1982). The State also did not challenge testimony from
Cone’s mother that Cone used drugs. Id., at 1647, 1648–
1653 (Apr. 20, 1982). And, most tellingly, the State intro
duced evidence that Cone was abusing three drugs—
——————
  5 The majority asserts that the standard under Tennessee law for

demonstrating mental defect or intoxication as a mitigating factor at
sentencing is “far lesser” than the standard for demonstrating insanity
in the guilt phase of a criminal trial. Ante, at 25. But the mitigating
factor still requires a showing that Cone’s mental capacity was “sub
stantially impaired” as a result of mental defect. Tenn. Code Ann. §39–
2-203(j)(8). In any event, the only authority cited by the majority for its
assertion that the standard is “far” lesser than that for insanity is
JUSTICE STEVENS’ lone dissent in a prior appeal in this case. Ante, at
25.
8                           CONE v. BELL

                         THOMAS, J., dissenting

cocaine, Dilaudid, and Demerol—at the time of his arrest
and was suffering “slight withdrawal symptoms” from
them. Id., at 1915–1916, 1920 (Apr. 22, 1982). As the
Court of Appeals explained, “[i]t would not have been news
to the jurors, that Cone was a ‘drug user.’ ” 492 F. 3d, at
757.6
   In contrast, what was contested by the State during
trial was Cone’s defense that his drug use was so signifi
cant that it caused him to suffer from extreme ampheta
mine psychosis at the time of the murders. One of Cone’s
expert witnesses, a neuropharmacologist, testified that by
the summer of 1980, when the crimes occurred, Cone was
ingesting “ferociously large doses” of drugs and that his
increasing tolerance and use of amphetamines caused a
chronic amphetamine psychosis. Tr. 1736–1737, 1744–
1747, 1758–1759 (Apr. 21, 1982). The expert further
testified that if a person with chronic amphetamine psy
chosis were to go into withdrawal, he could suffer extreme
mood swings, “a crashing depression,” and a state of weak
ness so severe that “he could barely lift himself.” Id., at
1857–1859. In this expert’s view, these symptoms could
cause a person to “lose his mind.” Id., at 1859.
   The State contradicted that testimony with significant
——————
    6 Althoughthere were two occasions during closing arguments where
prosecutors intimated that Cone was not a drug user, see Tr. 2014–
2015, 2068 (Apr. 22, 1982), the State’s argument otherwise consistently
focused on the real issue in the case: that Cone was not so significantly
affected by his drug use around the time of his crimes that he was “out
of his mind” or “drug crazy” during the critical days of August 1980.
See id., at 2023–2024, 2071–2084. The majority’s focus on two brief
excerpts from the State’s closing argument fails to faithfully view the
record “as a whole” for purposes of a Brady analysis. See Sawyer v.
Whitley, 505 U. S. 333, 374 (1992) (STEVENS, J., concurring in judg
ment); see also Strickler v. Greene, 527 U. S. 263, 290–291 (1999)
(finding no reasonable probability of a different result even when
prosecutor’s closing argument relied on testimony that could have been
impeached by withheld material).
                 Cite as: 556 U. S. ____ (2009)            9

                    THOMAS, J., dissenting

evidence that Cone did not act like someone who was “out
of his mind” during the commission of his crimes. Rather,
the State argued, Cone behaved rationally during his
initial Tennessee robbery, his subsequent escape, his
flight from Tennessee to Florida after the Todd murders,
his Florida robbery, and his subsequent arrest. See, e.g.,
id., at 2074–2084 (Apr. 22, 1982). To substantiate this
argument, the State called FBI Special Agent Eugene
Flynn to the stand. Agent Flynn testified that, when
captured, Cone coherently detailed his travel from Ten
nessee to Florida, explained his efforts to evade detection
by shaving his beard and buying new clothes, and initi
ated negotiations for a plea bargain. Id., at 1918–1921.
The State also presented testimony from a friend of
Cone’s, Ilene Blankman, that she saw no indication that
Cone was under the influence of drugs or severe with
drawal in the days immediately following the murder of
the Todds. Id., at 1875–1876, 1882–1883 (Apr. 21, 1982).
   Viewing the record as a whole, then, it is apparent that
the contested issue at trial and sentencing was not
whether Cone used drugs, but rather the quantity of
Cone’s drug use and its effect on his mental state. Only if
the evidence allegedly withheld from Cone was relevant to
this question whether Cone suffered from extreme am
phetamine psychosis or other substantial impairment
would the evidence have been exculpatory for purposes of
Brady. See Order Denying Motion for Evidentiary Hear
ing and Order of Partial Dismissal, Cone v. Bell, No. 97–
2312–M1/A (WD Tenn., May 15, 1998), App. to Pet. for
Cert. 119a, n. 9 (explaining that “the issue at trial was not
whether Cone had ever abused any drugs (he clearly had),
but whether he was out of his mind on amphetamines at
the time of the murders”); Tr. 2115–2116 (Apr. 23, 1982).
                          III
  With the legal and factual issues correctly framed, it
10                     CONE v. BELL

                    THOMAS, J., dissenting

becomes clear that Cone cannot establish a reasonable
probability that admission of the evidence—viewed either
individually or cumulatively—would have caused the jury
to alter his sentence.
                             A
                             1
  Cone first argues that he was improperly denied police
reports that included witness statements regarding Cone’s
behavior around the time of his crime spree. The first
statement was given by a convenience store employee,
Robert McKinney, who saw Cone the day before he robbed
the Tennessee jewelry store. When asked whether Cone
appeared “to be drunk or high on anything,” McKinney
answered, “[w]ell he did, he acted real weird . . . he just
wandered around the store.” App. 49. But McKinney
subsequently clarified that Cone “didn’t sound drunk” and
that the reason Cone attracted his attention was because
he “wasn’t acting like a regular customer”; he was “just
kinda wandering” around the store. Motion to Expand the
Record in No. 97–2312–M1 (WD Tenn.), Exh. 2, pp. 3, 4.
Contrary to the majority’s assertion, this interview is not
convincing evidence “that Cone appeared to be ‘drunk or
high’ ” when McKinney saw him. Ante, at 21. McKinney’s
clarification that he had characterized Cone’s behavior as
“weird” because Cone appeared to be killing time rather
than acting like a normal shopper undermines the impli
cation of McKinney’s earlier statement that Cone looked
“weird” because he might have been drunk or on drugs.
Thus, there is little chance that McKinney’s statement
would have provided any significant additional evidence
that Cone was using drugs, let alone provide sentence
changing evidence that he was substantially impaired due
to amphetamine psychosis.
  The second statement was given by Charles and Debbie
Slaughter, who both witnessed Cone fleeing from police
                  Cite as: 556 U. S. ____ (2009)           11

                     THOMAS, J., dissenting

after the jewelry store robbery and reportedly told police
that he looked “wild eyed.” App. 50. Cone had just robbed
a jewelry store, shot a police officer and a bystander, and
was still fleeing from police when seen by the Slaughters.
It is thus unlikely that their observation of a “wild eyed”
man would have been interpreted by the jury to mean that
Cone “was suffering from chronic amphetamine psychosis
at the time of the crimes,” ante, at 21, n. 16, rather than to
mean that Cone looked like a man on the run.
   The third statement is contained in a police report
authored by an officer who helped apprehend Cone after
the Florida drugstore robbery. He reported that he saw a
suspect “at the rear of Sambos restaurant. Subject was
observed to be looking about in a frenzied manner and also
appeared to be looking for a place to run.” App. 53. Noth
ing in this police report either connects Cone to drug use
or appears otherwise capable of altering the jury’s under
standing of Cone’s mental state at the time of the crimes.
It certainly makes perfect sense that Cone was “looking
about in a frenzied manner,” ibid.; he had just robbed a
drugstore and was about to engage in a gun battle with
police in order to evade arrest. The police officer’s descrip
tion of Cone’s appearance under these circumstances thus
does not “undermine confidence” in Cone’s sentence.
Kyles, 514 U. S., at 435.
                             2
  The next category of documents that Cone relies upon to
establish his Brady claim are police bulletins. Some of the
bulletins were sent by Memphis Police Sergeant Roby to
neighboring jurisdictions on the day of the Todd murders
and the day after. The bulletins sought Cone’s apprehen
sion and alternatively described him as a “drug user” or a
“heavy drug user.” App. 55–58. Cone asserts that he
could have used these bulletins to impeach Sergeant
Roby’s trial testimony that the sergeant did not see any
12                         CONE v. BELL

                        THOMAS, J., dissenting

track marks when visiting Cone in jail a week later. Tr.
1939 (Apr. 22, 1982). Cone’s reasoning is faulty for two
key reasons. First, Sergeant Roby never testified that
Cone was not a drug user. His only trial testimony on this
point was simply that he observed no “needle marks” on
Cone’s arm when taking hair samples from him a few days
after Cone’s apprehension. Ibid. Second, the bulletins
establish only “that the police were initially cautious
regarding the characteristics of a person who had commit
ted several heinous crimes.” App. to Pet. for Cert. 119a, n.
9. The bulletins would not have tended to prove that the
fugitive Cone was, in fact, a heavy drug user—let alone
“out of his mind” or otherwise substantially impaired due
to amphetamine psychosis—at the time of his crimes.7
                              3
  Cone also argues that material was withheld that could
have been used to impeach Ilene Blankman’s testimony
that Cone did not appear to be high or in withdrawal when
she helped him obtain a Florida driver’s license during his
efforts to evade arrest in Florida. Tr. 1875–1882 (Apr. 21,
1982). But he again fails to meet the standard for excul
patory evidence set by Brady.
  Cone first points to police notes of a pre-trial interview
with Blankman, which did not reflect the statement she
gave at trial that she saw no track marks on Cone’s arm.
App. 72–73. But Blankman was questioned at trial about
——————
   7 Alert bulletins sent by the FBI similarly identified Cone as a “be

lieved heavy drug user” or a “drug user.” App. 62–70. Cone argues
that these bulletins could have been used to impeach FBI Agent Flynn’s
testimony about Cone’s arrest in Florida. The bulletins would not have
constituted material impeachment evidence, however, for the second
reason identified above. In addition, the bulletins would not have
contradicted any of FBI Agent Flynn’s testimony; he in fact stated at
trial that Cone reported using three drugs and was undergoing mild
drug withdrawal when he was captured in Florida. Tr. 1915–1916
(Apr. 22, 1982).
                  Cite as: 556 U. S. ____ (2009)            13

                     THOMAS, J., dissenting

her failure to initially disclose this fact to police, Tr. 1903
(Apr. 21, 1982), so the jury was fully aware of the omis
sion. Disclosure of the original copy of the police notes
thus could not have had any material effect on the jury’s
deliberations. Moreover, the missing notes also recorded a
damning statement by Blankman that Cone “never used
drugs around” her and she “never saw Cone with drug
paraphernalia.” App. 73. Thus, it is difficult to accept
Cone’s argument that he would have benefited from the
introduction of notes from Blackman’s pretrial interview.
If anything, these police notes would have undermined his
mitigation argument.
   Cone next relies on a report that describes a woman’s
confrontation with the prosecution team and Blankman at
a restaurant during trial. During the encounter, the
woman accused Blankman of lying on the stand in order to
frame Cone for the murders. Id., at 74–75. The report
indicates that the prosecutors politely declined the
woman’s numerous attempts to discuss the merits of the
case and that Blankman said nothing. Id., at 75. Nothing
about this encounter raises doubts about Blankman’s
credibility.
   Last, Cone points to “correspondence in the district
attorney’s files suggest[ing] that the prosecution had been
unusually solicitous of [Blankman’s] testimony.” Brief for
Petitioner 45. But the correspondence was completely
innocuous. One of the notes, sent in response to Blank
man’s request for a copy of her prior statement, expressed
to Blankman that her “cooperation in this particular
matter is appreciated.” App. 76. The prosecutor then sent
a letter to confirm that Blankman would testify at trial.
Id., at 77. And finally, after trial, the prosecutor sent a
note to inform Blankman of the verdict and indicate that
they “certainly appreciate[d] [her] cooperation with [them]
in the trial of Gary Bradford Cone.” Id., at 78. There is
nothing about these notes that “tend[s] to prove any fact
14                     CONE v. BELL

                    THOMAS, J., dissenting

that is both favorable to Cone and material to his guilt or
punishment.” App. to Pet. for Cert. 116a.
                               B
   Viewing the record as a whole, Cone has not come close
to demonstrating that there is a “reasonable probability”
that the withheld evidence, analyzed individually or cu
mulatively, would have changed the result of his sentenc
ing. Much of the impeachment evidence identified by
Cone is of no probative value whatsoever. The police
bulletins do not contradict any of the trial testimony; the
restaurant encounter was innocuous; and the correspon
dence sent by prosecutors to Blankman does not under
mine her testimony or call Cone’s mental state into doubt.
If the remaining evidence has any value to Cone, it is
marginal at best. There was testimony that Blankman
did not initially tell police that Cone lacked track marks.
See Tr. 1903 (Apr. 21, 1982). McKinney clarified in his
statement that Cone’s activity in the store was consistent
with a person killing time, not the use of drugs or alcohol.
And the behavior described by the Slaughters and the
Florida police officer is more naturally attributable to the
circumstances of Cone’s flight from the police than to any
inference that Cone was “out of his mind” or otherwise
substantially impaired due to amphetamine psychosis.
   Countering the trivial value of the alleged Brady mate
rial is the clear and overwhelming evidence that during
Cone’s crime spree, he was neither sufficiently insane to
avoid a conviction of murder nor substantially impaired by
his drug use or withdrawal-related psychosis. There was
substantial evidence that Cone carefully planned the
jewelry store robbery and was calm in carrying it out, Tr.
at 974–976, 1014 (Apr. 16, 1982), 1350–1352 (Apr. 17,
1982), 1501 (Apr. 19, 1982), 2075 (Apr. 22, 1982); that he
successfully eluded police after engaging them in a shoot
out, id., at 1053–1064 (Apr. 16, 1982); that, after hiding
                 Cite as: 556 U. S. ____ (2009)           15

                    THOMAS, J., dissenting

overnight, he concocted a ruse to try to gain illegal entry
to a residence, id., at 1205–1208 (Apr. 17, 1982); that he
murdered the Todds after they declined to cooperate with
his efforts to further elude police, id., at 1681 (Apr. 20,
1982); that he took steps to change his appearance at the
Todd residence and then successfully fled to Florida, id., at
1918–1919 (Apr. 22, 1982); that he arrived in Florida
exhibiting no signs of drug use or severe withdrawal, id.,
at 1875–1882 (Apr. 21, 1982); that he obtained false iden
tification in a further effort to avoid apprehension, id., at
1881–1882, and that he denied any memory lapses and
described undergoing only minor drug withdrawal when
police arrested him, id., at 1919–1920 (Apr. 22, 1982).
Given this wealth of evidence, there is no “reasonable
probability” that the jury would have found that Cone was
entitled to the substantial impairment mitigator had the
evidence he seeks been made available to him.
   And even if Cone could have presented this evidence to
the jury at sentencing and established an entitlement to
this mitigator, he still has not demonstrated a reasonable
probability that it would have outweighed all of the aggra
vating factors supporting the jury’s death sentence. See
id., at 2151–2154 (Apr. 23, 1982). In its decision on direct
appeal, the Tennessee Supreme Court was well aware of
the evidence regarding the “degree and extent of [Cone’s]
drug abuse.” Cone, 665 S. W. 2d, at 90. As part of its
required independent review of whether the mitigation
evidence was sufficiently substantial to outweigh the
aggravating factors, see Tenn. Code Ann. §39–2-205, the
Tennessee court nevertheless concluded that the sentence
was “not in any way disproportionate under all of the
circumstances, including the brutal murders of two elderly
defenseless persons by an escaping armed robber who had
terrorized a residential neighborhood for twenty-four
hours.” 665 S. W. 2d, at 95–96. None of Cone’s proffered
evidence places that conclusion, made by both the jury and
16                     CONE v. BELL

                    THOMAS, J., dissenting

the Tennessee Supreme Court, “in such a different light as
to undermine confidence” in Cone’s sentence. Kyles, 514
U. S., at 435; see also Strickler, 527 U. S., at 296.
                            IV
  This Court should not vacate and remand lower court
decisions based on nothing more than the vague suspicion
that error might be present, or because the court below
could have been more clear. This is especially so where, as
here, the record before the Court is adequate to evaluate
Cone’s Brady claims with respect to both the guilt and
sentencing phases of his trial. The Court’s willingness to
return the sentencing issue to the District Court without
any firm conviction that an error was committed by the
Court of Appeals is inconsistent with our established
practice and disrespectful to the lower courts that have
considered this case. Worse still, the inevitable result will
be years of additional delay in the execution of a death
sentence lawfully imposed by a Tennessee jury. Because I
would affirm the judgment below, I respectfully dissent.

```

---
