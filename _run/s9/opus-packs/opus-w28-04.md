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

## GROUP: content/cases/California v. Hodari D..md  (`case`, 5 assertions)

### content_page

```
---
title: "California v. Hodari D."
type: case
citation: "499 U.S. 621 (1991)"
parallel_cite: "111 S. Ct. 1547; 113 L. Ed. 2d 690; 59 U.S.L.W. 4335; 91 Daily Journal DAR 4665"
neutral_cite: "1991 U.S. LEXIS 2397; 91 Cal. Daily Op. Serv. 2893"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1991
date_decided: 1991-04-23
docket: 89-1632
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1991-04-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: California v. Hodari D.
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112579/california-v-hodari-d/"
  cluster_id: 112579
  opinion_id: 112579
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Key — Progeny / Refinement"
related: ["[[Terry v. Ohio]]", "[[United States v. Mendenhall]]", "[[Brendlin v. California]]"]
aliases: ["California v. Hodari D", "Hodari D."]
tags: ["case", "fourth-amendment", "seizure", "show-of-authority", "flight"]
holding: "A show-of-authority seizure is not complete until the suspect submits; contraband discarded while still fleeing is not the fruit of a seizure."
lake:
  record_id: California v. Hodari D.
  status: verified
  projected_at: 2026-07-06
---

# California v. Hodari D.

*499 U.S. 621 (1991)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A group of youths fled at the approach of an unmarked police car. An officer chased Hodari on foot. Just before the officer caught and tackled him, Hodari tossed away a small rock of crack cocaine. Hodari argued he had been "seized" the moment he saw the officer giving chase, so the discarded cocaine was the fruit of an unlawful seizure.

## Issue
Whether a suspect who does not yield to a police show of authority is "seized" under the Fourth Amendment before any physical force is applied.

## Rule
"The narrow question before us is whether, with respect to a show of authority as with respect to application of physical force, a seizure occurs even though the subject does not yield. We hold that it does not." — 499 U.S. at 626. ^pin-626

"An arrest requires either physical force (as described above) or, where that is absent, submission to the assertion of authority." — *Id.* ^pin-626b

## Application
Hodari was not touched until after he had thrown away the cocaine, and he had not submitted to the chasing officer's show of authority before then. Because neither physical force nor submission had occurred at the moment he discarded the cocaine, he was not yet seized, and the cocaine was not the fruit of a seizure.

## Conclusion
No seizure had occurred when Hodari abandoned the cocaine; the judgment suppressing it was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hodari D.* refines the seizure framework of [[Terry v. Ohio]] and [[United States v. Mendenhall]] by adding the submission requirement for show-of-authority seizures.

## Appears on
- [[Seizure of the Person]] — *Key — Progeny / Refinement*

## Sources
- *California v. Hodari D.*, 499 U.S. 621 (1991) — https://www.courtlistener.com/opinion/112579/california-v-hodari-d/ — pinpoint: 626.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f4101bd4f97e3aef", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "499 U.S. 621 (1991)", "court": "U.S. Supreme Court", "neutral_cite": "1991 U.S. LEXIS 2397; 91 Cal. Daily Op. Serv. 2893", "official_citation_present": true, "parallel_cite": "111 S. Ct. 1547; 113 L. Ed. 2d 690; 59 U.S.L.W. 4335; 91 Daily Journal DAR 4665", "title": "California v. Hodari D.", "year": "1991"}}
{"assertion_id": "5615abc329600c4d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A show-of-authority seizure is not complete until the suspect submits; contraband discarded while still fleeing is not the fruit of a seizure.", "title": "California v. Hodari D."}}
{"assertion_id": "7795c5dc53a82240", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Key — Progeny / Refinement", "title": "California v. Hodari D."}}
{"assertion_id": "2f6113744cf6f820", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "California v. Hodari D."}}
{"assertion_id": "8e5806757504126a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1991-04-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "California v. Hodari D.", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "California v. Hodari D.", "varies_by_point": "false"}}
```

### lake record — California v. Hodari D.

```json
{
  "schema_version": "s2.v1",
  "record_id": "California v. Hodari D.",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "California v. Hodari D.",
    "case_name_short": "",
    "case_name_full": "California v. Hodari D.",
    "input_case_name": "California v. Hodari D.",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1991-04-23",
    "year": 1991,
    "docket": "89-1632",
    "cluster_id": 112579,
    "lead_opinion_id": 112579,
    "sibling_ids": [
      112579,
      9432255,
      9432256
    ],
    "absolute_url": "/opinion/112579/california-v-hodari-d/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "499 U.S. 621",
      "volume": "499",
      "reporter": "U.S.",
      "page": "621",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "111 S. Ct. 1547",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "1547",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 L. Ed. 2d 690",
        "volume": "113",
        "reporter": "L. Ed. 2d",
        "page": "690",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "59 U.S.L.W. 4335",
        "volume": "59",
        "reporter": "U.S.L.W.",
        "page": "4335",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 Daily Journal DAR 4665",
        "volume": "91",
        "reporter": "Daily Journal DAR",
        "page": "4665",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1991 U.S. LEXIS 2397",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "2397",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 Cal. Daily Op. Serv. 2893",
        "volume": "91",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "2893",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "499 U.S. 621",
        "volume": "499",
        "reporter": "U.S.",
        "page": "621",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "111 S. Ct. 1547",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "1547",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 L. Ed. 2d 690",
        "volume": "113",
        "reporter": "L. Ed. 2d",
        "page": "690",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 U.S. LEXIS 2397",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "2397",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 Cal. Daily Op. Serv. 2893",
        "volume": "91",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "2893",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "59 U.S.L.W. 4335",
        "volume": "59",
        "reporter": "U.S.L.W.",
        "page": "4335",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 Daily Journal DAR 4665",
        "volume": "91",
        "reporter": "Daily Journal DAR",
        "page": "4665",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "499 U.S. 621",
    "official_selection": {
      "court_class": "scotus",
      "selected": "499 U.S. 621",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-626",
      "page": null,
      "quote": "under the Fourth Amendment before any physical force is applied. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-626b",
      "page": null,
      "quote": "An arrest requires either physical force (as described above) or, where that is absent, submission to the assertion of authority.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1991-04-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "California v. Hodari D.",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Dorado",
          "cluster_id": 10133856,
          "cite": [
            "307 Or. App. 641",
            "477 P.3d 1209"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Evelyn",
          "cluster_id": 4786331,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Matta",
          "cluster_id": 4671437,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fredericq",
          "cluster_id": 4613398,
          "cite": [
            "121 N.E.3d 166",
            "482 Mass. 70"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane1_negative"
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
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County of Sacramento v. Lewis",
          "cluster_id": 118214,
          "cite": [
            "140 L. Ed. 2d 1043",
            "118 S. Ct. 1708",
            "523 U.S. 833",
            "1998 U.S. LEXIS 3404"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Bostick",
          "cluster_id": 112631,
          "cite": [
            "115 L. Ed. 2d 389",
            "111 S. Ct. 2382",
            "501 U.S. 429",
            "1991 U.S. LEXIS 3625",
            "59 U.S.L.W. 4708",
            "91 Daily Journal DAR 7328",
            "91 Cal. Daily Op. Serv. 4671",
            "1991 WL 105224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Wardlow",
          "cluster_id": 118326,
          "cite": [
            "145 L. Ed. 2d 570",
            "120 S. Ct. 673",
            "528 U.S. 119",
            "2000 U.S. LEXIS 504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
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
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
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
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Drayton",
          "cluster_id": 121153,
          "cite": [
            "153 L. Ed. 2d 242",
            "122 S. Ct. 2105",
            "536 U.S. 194",
            "2002 U.S. LEXIS 4420"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manuel v. City of Joliet",
          "cluster_id": 4376986,
          "cite": [
            "580 U.S. 357",
            "137 S. Ct. 911",
            "197 L. Ed. 2d 312",
            "2017 U.S. LEXIS 2021",
            "26 Fla. L. Weekly Fed. S 476",
            "85 U.S.L.W. 4130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wyoming v. Houghton",
          "cluster_id": 118277,
          "cite": [
            "143 L. Ed. 2d 408",
            "119 S. Ct. 1297",
            "526 U.S. 295",
            "1999 U.S. LEXIS 2347"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
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
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McGee v. Commonwealth",
          "cluster_id": 1067400,
          "cite": [
            "487 S.E.2d 259",
            "25 Va. App. 193",
            "1997 Va. App. LEXIS 444"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Garcia-Cantu",
          "cluster_id": 1769810,
          "cite": [
            "253 S.W.3d 236",
            "2008 Tex. Crim. App. LEXIS 581",
            "2008 WL 1958956"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hollman",
          "cluster_id": 5690698,
          "cite": [
            "79 N.Y.2d 181"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Laura Skop v. City of Atlanta, Georgia",
          "cluster_id": 77695,
          "cite": [
            "485 F.3d 1130",
            "2007 U.S. App. LEXIS 10341",
            "2007 WL 1288012"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crain v. State",
          "cluster_id": 2353970,
          "cite": [
            "315 S.W.3d 43",
            "2010 Tex. Crim. App. LEXIS 794",
            "2010 WL 2595077"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ehly",
          "cluster_id": 1448102,
          "cite": [
            "854 P.2d 421",
            "317 Or. 66",
            "1993 Ore. LEXIS 91"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Retherford",
          "cluster_id": 4001886,
          "cite": [
            "639 N.E.2d 498",
            "93 Ohio App. 3d 586",
            "1994 Ohio App. LEXIS 1066"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bora",
          "cluster_id": 2243377,
          "cite": [
            "634 N.E.2d 168",
            "83 N.Y.2d 531",
            "611 N.Y.S.2d 796",
            "1994 N.Y. LEXIS 703"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cheryl James v. Wilkes Barre City",
          "cluster_id": 812864,
          "cite": [
            "700 F.3d 675",
            "2012 U.S. App. LEXIS 24592",
            "2012 WL 5954632"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cindy Abbott v. Sangamon County",
          "cluster_id": 816250,
          "cite": [
            "705 F.3d 706",
            "2013 WL 322920",
            "2013 U.S. App. LEXIS 1963"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gene Autrey Adams v. Paul Metiva",
          "cluster_id": 675736,
          "cite": [
            "31 F.3d 375",
            "1994 U.S. App. LEXIS 19686",
            "1994 WL 394087"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 1676406,
          "cite": [
            "912 S.W.2d 227",
            "1995 Tex. Crim. App. LEXIS 115",
            "1995 WL 675559"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katherine Gardenhire and Walter Gardenhire v. Donald Schubert, in His Individual and Official Capacity as Chief of Police",
          "cluster_id": 767858,
          "cite": [
            "205 F.3d 303",
            "2000 U.S. App. LEXIS 3126",
            "2000 WL 232311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sanchez-Llamas v. Oregon",
          "cluster_id": 145628,
          "cite": [
            "165 L. Ed. 2d 557",
            "126 S. Ct. 2669",
            "548 U.S. 331",
            "2006 U.S. LEXIS 5177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kaupp v. Texas",
          "cluster_id": 127919,
          "cite": [
            "155 L. Ed. 2d 814",
            "123 S. Ct. 1843",
            "538 U.S. 626",
            "2003 U.S. LEXIS 3670"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Hodari D.:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112579 OR 9432255 OR 9432256) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTA3MTYxNjAwMDAwJnM9NDQzMjY0MyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112579+OR+9432255+OR+9432256%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112579 OR 9432255 OR 9432256)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMzAmcz0xMDU3MTU1JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112579+OR+9432255+OR+9432256%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112579 OR 9432255 OR 9432256)",
        "reviewed": 82,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 82,
        "triage_read": 0,
        "triage_snippet_classified": 82
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112579 OR 9432255 OR 9432256)",
    "indexed_citing_opinions": 2003,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112579,
        "count": 1741,
        "count_source": "search"
      },
      {
        "opinion_id": 9432255,
        "count": 286,
        "count_source": "search"
      },
      {
        "opinion_id": 9432256,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3675,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/california-v-hodari-d.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNzMzMDEmcz0xMDM2MjU3NiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28112579+OR+9432255+OR+9432256%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112579,
        "cited_id": 85464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 88142,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 88824,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 94447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112579,
        "cited_id": 112218,
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
    "date_created": "2026-07-04T23:18:53Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:19:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:19:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:22:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:19:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — California v. Hodari D.

```
<div>
<center><b><span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/" aria-description="Citation for case: California v. Hodari D.">499 U.S. 621</a></span> (1991)</b></center>
<center><h1>CALIFORNIA<br>
v.<br>
HODARI D.</h1></center>
<center>No. 89-1632.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued January 14, 1991.</center>
<center>Decided April 23, 1991.</center>
CERTIORARI TO THE COURT OF APPEAL OF CALIFORNIA, FIRST APPELLATE DISTRICT
<p><span class="star-pagination">*622</span> <i>Ronald E. Niver,</i> Deputy Attorney General of California, argued the cause for petitioner. With him on the briefs were <i>John K. Van de Kamp,</i> Attorney General, <i>Richard B. Iglehart,</i> Chief Assistant Attorney General, <i>John H. Sugiyama,</i> Senior Assistant Attorney General, and <i>Clifford K. Thompson, Jr.,</i> and <i>Morris Beatus,</i> Deputy Attorneys General.</p>
<p><i>Clifford M. Sloan</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. On the brief were <i>Solicitor General Starr, Assistant Attorney General Mueller, Deputy Solicitor General Bryson,</i> and <i>Paul J. Larkin, Jr.</i></p>
<p><i>James L. Lozenski,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./498/935/">498 U. S. 935</a></span>, argued the cause for respondent. With him on the brief was <i>J. Bradley O'Connell.</i><sup>[*]</sup></p>
<p>JUSTICE SCALIA delivered the opinion of the Court.</p>
<p>Late one evening in April 1988, Officers Brian McColgin and Jerry Pertoso were on patrol in a high-crime area of Oakland, California. They were dressed in street clothes but wearing jackets with "Police" embossed on both front and back. Their unmarked car proceeded west on Foothill Boulevard, and turned south onto 63rd Avenue. As they rounded the corner, they saw four or five youths huddled around a small red car parked at the curb. When the youths <span class="star-pagination">*623</span> saw the officers' car approaching they apparently panicked, and took flight. The respondent here, Hodari D., and one companion ran west through an alley; the others fled south. The red car also headed south, at a high rate of speed.</p>
<p>The officers were suspicious and gave chase. McColgin remained in the car and continued south on 63rd Avenue; Pertoso left the car, ran back north along 63rd, then west on Foothill Boulevard, and turned south on 62nd Avenue. Hodari, meanwhile, emerged from the alley onto 62nd and ran north. Looking behind as he ran, he did not turn and see Pertoso until the officer was almost upon him, whereupon he tossed away what appeared to be a small rock. A moment later, Pertoso tackled Hodari, handcuffed him, and radioed for assistance. Hodari was found to be carrying $130 in cash and a pager; and the rock he had discarded was found to be crack cocaine.</p>
<p>In the juvenile proceeding brought against him, Hodari moved to suppress the evidence relating to the cocaine. The court denied the motion without opinion. The California Court of Appeal reversed, holding that Hodari had been "seized" when he saw Officer Pertoso running towards him, that this seizure was unreasonable under the Fourth Amendment, and that the evidence of cocaine had to be suppressed as the fruit of that illegal seizure. The California Supreme Court denied the State's application for review. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./498/807/">498 U. S. 807</a></span> (1990).</p>
<p>As this case comes to us, the only issue presented is whether, at the time he dropped the drugs, Hodari had been "seized" within the meaning of the Fourth Amendment.<sup>[1]</sup> If <span class="star-pagination">*624</span> so, respondent argues, the drugs were the fruit of that seizure and the evidence concerning them was properly excluded. If not, the drugs were abandoned by Hodari and lawfully recovered by the police, and the evidence should have been admitted. (In addition, of course, Pertoso's seeing the rock of cocaine, at least if he recognized it as such, would provide reasonable suspicion for the unquestioned seizure that occurred when he tackled Hodari. Cf. <i>Rios</i> v. <i>United States,</i> <span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/" aria-description="Citation for case: Rios v. United States">364 U. S. 253</a></span> (1960).)</p>
<p>We have long understood that the Fourth Amendment's protection against "unreasonable . . . seizures" includes seizure of the person, see <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 100</a></span> (1959). From the time of the founding to the present, the word "seizure" has meant a "taking possession," 2 N. Webster, An American Dictionary of the English Language 67 (1828); 2 J. Bouvier, A Law Dictionary 510 (6th ed. 1856); Webster's Third New International Dictionary 2057 (1981). For most purposes at common law, the word connoted not merely grasping, or applying physical force to, the animate or inanimate object in question, but actually bringing it within physical control. A ship still fleeing, even though under attack, would not be considered to have been seized as a war prize. Cf. <i>The Josefa Segunda,</i> <span class="citation" data-id="85464"><a href="/opinion/85464/the-josefa-segunda/#325" aria-description="Citation for case: The Josefa Segunda">10 Wheat. 312, 325-326</a></span> (1825). A res capable of manual delivery was not seized until "tak[en] into custody." <i>Pelham</i> v. <i>Rose,</i> <span class="citation" data-id="88142"><a href="/opinion/88142/pelham-v-rose/#106" aria-description="Citation for case: Pelham v. Rose">9 Wall. 103, 106</a></span> (1870). To constitute an arrest, howeverthe quintessential "seizure of the person" under our Fourth Amendment jurisprudencethe mere grasping or application of physical force with lawful authority, whether or not it succeeded in subduing the arrestee, was sufficient. See, <i>e. g., </i><i>Whitehead</i> v. <i>Keyes,</i> <span class="citation" data-id="6413260"><a href="/opinion/6539539/whithead-v-keyes/#501" aria-description="Citation for case: Whithead v. Keyes">85 Mass. 495, 501</a></span> (1862) ("[A]n officer effects an arrest of a person whom he has authority to arrest, by laying his hand on him for the purpose of arresting him, though he may not succeed in stopping and holding him"); 1 <span class="star-pagination">*625</span> Restatement of Torts § 41, Comment <i>h</i> (1934). As one commentator has described it:</p>
<blockquote>"There can be constructive detention, which will constitute an arrest, although the party is never actually brought within the physical control of the party making an arrest. This is accomplished by merely touching, however slightly, the body of the accused, by the party making the arrest and for that purpose, although he does not succeed in stopping or holding him even for an instant; as where the bailiff had tried to arrest one who fought him off by a fork, the court said, `If the bailiff had touched him, that had been an arrest . . . .'" A. Cornelius, Search and Seizure 163-164 (2d ed. 1930) (footnote omitted).</blockquote>
<p>To say that an arrest is effected by the slightest application of physical force, despite the arrestee's escape, is not to say that for Fourth Amendment purposes there is a <i>continuing</i> arrest during the period of fugitivity. If, for example, Pertoso had laid his hands upon Hodari to arrest him, but Hodari had broken away and had <i>then</i> cast away the cocaine, it would hardly be realistic to say that that disclosure had been made during the course of an arrest. Cf. <i>Thompson</i> v. <i>Whitman,</i> <span class="citation" data-id="88824"><a href="/opinion/88824/thompson-v-whitman/#471" aria-description="Citation for case: Thompson v. Whitman">18 Wall. 457, 471</a></span> (1874) ("A seizure is a single act, and not a continuous fact"). The present case, however, is even one step further removed. It does not involve the application of any physical force; Hodari was untouched by Officer Pertoso at the time he discarded the cocaine. His defense relies instead upon the proposition that a seizure occurs "when the officer, by means of physical force <i>or show of authority,</i> has in some way restrained the liberty of a citizen." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19, n. 16</a></span> (1968) (emphasis added). Hodari contends (and we accept as true for purposes of this decision) that Pertoso's pursuit qualified as a "show of authority" <span class="star-pagination">*626</span> calling upon Hodari to halt. The narrow question before us is whether, with respect to a show of authority as with respect to application of physical force, a seizure occurs even though the subject does not yield. We hold that it does not.</p>
<p>The language of the Fourth Amendment, of course, cannot sustain respondent's contention. The word "seizure" readily bears the meaning of a laying on of hands or application of physical force to restrain movement, even when it is ultimately unsuccessful. ("She seized the purse-snatcher, but he broke out of her grasp.") It does not remotely apply, however, to the prospect of a policeman yelling "Stop, in the name of the law!" at a fleeing form that continues to flee. That is no seizure.<sup>[2]</sup> Nor can the result respondent wishes to achieve be producedindirectly, as it wereby suggesting that Pertoso's uncomplied-with show of authority was a common-law arrest, and then appealing to the principle that all common-law arrests are seizures. An arrest requires <i>either</i> physical force (as described above) <i>or,</i> where that is absent, <i>submission</i> to the assertion of authority.</p>
<blockquote>"Mere words will not constitute an arrest, while, on the other hand, no actual, physical touching is essential. The apparent inconsistency in the two parts of this statement is explained by the fact that an assertion of authority and purpose to arrest followed by submission of the arrestee constitutes an arrest. There can be no arrest <span class="star-pagination">*627</span> without either touching or submission." Perkins, The Law of Arrest, <span class="citation no-link">25 Iowa L. Rev. 201</span>, 206 (1940) (footnotes omitted).</blockquote>
<p>We do not think it desirable, even as a policy matter, to stretch the Fourth Amendment beyond its words and beyond the meaning of arrest, as respondent urges.<sup>[3]</sup> Street pursuits always place the public at some risk, and compliance with police orders to stop should therefore be encouraged. Only a few of those orders, we must presume, will be without adequate basis, and since the addressee has no ready means of identifying the deficient ones it almost invariably is the responsible course to comply. Unlawful orders will not be deterred, moreover, by sanctioning through the exclusionary rule those of them that are <i>not</i> obeyed. Since policemen do not command "Stop!" expecting to be ignored, or give chase hoping to be outrun, it fully suffices to apply the deterrent to their genuine, successful seizures.</p>
<p>Respondent contends that his position is sustained by the so-called <i>Mendenhall</i> test, formulated by Justice Stewart's opinion in <i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 554</a></span> (1980), and adopted by the Court in later cases, see <i>Michigan</i> v. <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#573" aria-description="Citation for case: Michigan v. Chesternut">486 U. S. 567, 573</a></span> (1988); <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#215" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 215</a></span> (1984): "[A] person has been `seized' within the <span class="star-pagination">*628</span> meaning of the Fourth Amendment only if, in view of all the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave." <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S., at 554</a></span>. See also <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#502" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 502</a></span> (1983) (opinion of WHITE, J.). In seeking to rely upon that test here, respondent fails to read it carefully. It says that a person has been seized "only if," not that he has been seized "whenever"; it states a <i>necessary,</i> but not a <i>sufficient,</i> condition for seizureor, more precisely, for seizure effected through a "show of authority." <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span></i> establishes that the test for existence of a "show of authority" is an objective one: not whether the citizen perceived that he was being ordered to restrict his movement, but whether the officer's words and actions would have conveyed that to a reasonable person. Application of this objective test was the basis for our decision in the other case principally relied upon by respondent, <i><span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/" aria-description="Citation for case: Michigan v. Chesternut">Chesternut, supra,</a></span></i> where we concluded that the police cruiser's slow following of the defendant did not convey the message that he was not free to disregard the police and go about his business. We did not address in <i><span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/" aria-description="Citation for case: Michigan v. Chesternut">Chesternut</a></span>,</i> however, the question whether, if the <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span></i> test was metif the message that the defendant was not free to leave <i>had</i> been conveyeda Fourth Amendment seizure would have occurred. See <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#577" aria-description="Citation for case: Michigan v. Chesternut">486 U. S., at 577</a></span> (KENNEDY, J., concurring).</p>
<p>Quite relevant to the present case, however, was our decision in <i>Brower</i> v. <i>Inyo County,</i> <span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/#596" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo">489 U. S. 593, 596</a></span> (1989). In that case, police cars with flashing lights had chased the decedent for 20 milessurely an adequate "show of authority"but he did not stop until his fatal crash into a police-erected blockade. The issue was whether his death could be held to be the consequence of an unreasonable seizure in violation of the Fourth Amendment. We did not even consider the possibility that a seizure could have occurred during the course of the chase because, as we explained, that "show of authority" did not produce his stop. <span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/#597" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo"><i>Id.,</i> at 597</a></span>. And we discussed, <span class="star-pagination">*629</span> <i>ibid.,</i> an opinion of Justice Holmes, involving a situation not much different from the present case, where revenue agents had picked up containers dropped by moonshiners whom they were pursuing without adequate warrant. The containers were not excluded as the product of an unlawful seizure because "[t]he defendant's own acts, and those of his associates, disclosed the jug, the jar and the bottleand there was no seizure in the sense of the law when the officers examined the contents of each after they had been abandoned." <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#58" aria-description="Citation for case: Hester v. United States">265 U. S. 57, 58</a></span> (1924). The same is true here.</p>
<p>In sum, assuming that Pertoso's pursuit in the present case constituted a "show of authority" enjoining Hodari to halt, since Hodari did not comply with that injunction he was not seized until he was tackled. The cocaine abandoned while he was running was in this case not the fruit of a seizure, and his motion to exclude evidence of it was properly denied. We reverse the decision of the California Court of Appeal, and remand for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE STEVENS, with whom JUSTICE MARSHALL joins, dissenting.</p>
<p>The Court's narrow construction of the word "seizure" represents a significant, and in my view, unfortunate, departure from prior case law construing the Fourth Amendment.<sup>[1]</sup> Almost a quarter of a century ago, in two landmark cases one broadening the protection of individual privacy,<sup>[2]</sup> and the other broadening the powers of law enforcement officers<sup>[3]</sup> we rejected the method of Fourth Amendment analysis that <span class="star-pagination">*630</span> today's majority endorses. In particular, the Court now adopts a definition of "seizure" that is unfaithful to a long line of Fourth Amendment cases. Even if the Court were defining seizure for the first time, which it is not, the definition that it chooses today is profoundly unwise. In its decision, the Court assumes, without acknowledging, that a police officer may now fire his weapon at an innocent citizen and not implicate the Fourth Amendmentas long as he misses his target.</p>
<p>For the purposes of decision, the following propositions are not in dispute. First, when Officer Pertoso began his pursuit of respondent,<sup>[4]</sup> the officer did not have a lawful basis for either stopping or arresting respondent. See App. 138-140; <i>ante,</i> at 623, n. 1. Second, the officer's chase amounted to a "show of authority" as soon as respondent saw the officer nearly upon him. See <i>ante,</i> at 625-626, 629. Third, the act of discarding the rock of cocaine was the direct consequence of the show of authority. See Pet. for Cert. 48-49, 52. Fourth, as the Court correctly demonstrates, no common-law arrest occurred until the officer tackled respondent. See <i>ante,</i> at 624-625. Thus, the Court is quite right in concluding that the abandonment of the rock was not the fruit of a common-law arrest.</p>
<p>It is equally clear, however, that if the officer had succeeded in touching respondent before he dropped the rock <span class="star-pagination">*631</span> even if he did not subdue himan arrest would have occurred.<sup>[5]</sup> See <i>ante,</i> at 624-625, 626. In that event (assuming the touching precipitated the abandonment), the evidence would have been the fruit of an unlawful common-law arrest. The distinction between the actual case and the hypothetical case is the same as the distinction between the common-law torts of assault and batterya touching converts the former into the latter.<sup>[6]</sup> Although the distinction between assault and battery was important for pleading purposes, see 2 J. Chitty, Pleading *372-*376, the distinction should not take on constitutional dimensions. The Court mistakenly allows this common-law distinction to define its interpretation of the Fourth Amendment.</p>
<p>At the same time, the Court fails to recognize the existence of another, more telling, common-law distinctionthe distinction between an arrest and an attempted arrest. As the Court teaches us, the distinction between battery and assault was critical to a correct understanding of the common law of arrest. See <i>ante,</i> at 626 ("An arrest requires <i>either</i> physical force . . . <i>or,</i> where that is absent, <i>submission</i> to the assertion of authority"). However, the facts of this case do not describe an actual arrest, but rather an unlawful <i>attempt</i> to take a presumptively innocent person into custody. Such an <span class="star-pagination">*632</span> attempt was unlawful at common law.<sup>[7]</sup> Thus, if the Court wants to define the scope of the Fourth Amendment based on the common law, it should look, not to the common law of arrest, but to the common law of attempted arrest, according to the facts of this case.</p>
<p>The first question, then, is whether the common law should define the scope of the outer boundaries of the constitutional protection against unreasonable seizures. Even if, contrary to settled precedent, traditional common-law analysis were controlling, it would still be necessary to decide whether the unlawful attempt to make an arrest should be considered a seizure within the meaning of the Fourth Amendment, and whether the exclusionary rule should apply to unlawful attempts.</p>
<p></p>
<h2>I</h2>
<p>The Court today takes a narrow view of "seizure," which is at odds with the broader view adopted by this Court almost 25 years ago. In <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), the Court considered whether electronic surveillance conducted "without any trespass and without the seizure of any material object fell outside the ambit of the Constitution." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 353</a></span>. Over Justice Black's powerful dissent, we rejected that "narrow view" of the Fourth Amendment and held that electronic eavesdropping is a "search and seizure" within the meaning of the Amendment. <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 353-354</a></span>. We thus endorsed the position expounded by two of the dissenting Justices in <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span> (1928):</p>
<blockquote>
<span class="star-pagination">*633</span> "Time and again, this Court in giving effect to the principle underlying the Fourth Amendment, has refused to place an unduly literal construction upon it." <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#476" aria-description="Citation for case: Olmstead v. United States"><i>Id.,</i> at 476</a></span> (Brandeis, J., dissenting).</blockquote>
<blockquote>"The direct operation or literal meaning of the words used do not measure the purpose or scope of its provisions. Under the principles established and applied by this Court, the Fourth Amendment safeguards against all evils that are like and equivalent to those embraced within the ordinary meaning of its words." <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#488" aria-description="Citation for case: Olmstead v. United States"><i>Id.,</i> at 488</a></span> (Butler, J., dissenting).</blockquote>
<p>Writing for the Court in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> Justice Stewart explained:</p>
<blockquote>"Thus, although a closely divided Court supposed in <i><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">Olmstead</a></span></i> that surveillance without any trespass and without the seizure of any material object fell outside the ambit of the Constitution, we have since departed from the narrow view on which that decision rested. Indeed, we have expressly held that the Fourth Amendment governs not only the seizure of tangible items, but extends as well to the recording of oral statements, overheard without any `technical trespass under . . . local property law.' <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511</a></span>. Once this much is acknowledged, and once it is recognized that the Fourth Amendment protects peopleand not simply `areas'against unreasonable searches and seizures, it becomes clear that the reach of that Amendment cannot turn upon the presence or absence of a physical intrusion into any given enclosure.</blockquote>
<blockquote>"We conclude that the underpinnings of <i><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">Olmstead</a></span></i> and <i>Goldman</i> have been so eroded by our subsequent decisions that the `trespass' doctrine there enunciated can no longer be regarded as controlling. The Government's activities in electronically listening to and recording the petitioner's words violated the privacy upon which he justifiably relied while using the telephone <span class="star-pagination">*634</span> booth and thus constituted a `search and seizure' within the meaning of the Fourth Amendment. The fact that the electronic device employed to achieve that end did not happen to penetrate the wall of the booth can have no constitutional significance.</blockquote>
<blockquote>"The question remaining for decision, then, is whether the search and seizure conducted in this case complied with constitutional standards." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U. S., at 353-354</a></span>.</blockquote>
<p>Significantly, in the <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> opinion, the Court repeatedly used the word "seizure" to describe the process of recording sounds that could not possibly have been the subject of a common-law seizure. See <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#356" aria-description="Citation for case: Katz v. United States"><i>id.,</i> at 356, 357</a></span>.</p>
<p>Justice Black's reasoning, which was rejected by the Court in 1967, is remarkably similar to the reasoning adopted by the Court today. After criticizing "language-stretching judges," <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#366" aria-description="Citation for case: Katz v. United States"><i>id.,</i> at 366</a></span>, Justice Black wrote:</p>
<blockquote>"I do not deny that common sense requires and that this Court often has said that the Bill of Rights' safeguards should be given a liberal construction. This principle, however, does not justify construing the search and seizure amendment as applying to eavesdropping or the `seizure' of conversations." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#366" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 366-367</a></span>.</blockquote>
<blockquote>"Since I see no way in which the words of the Fourth Amendment can be construed to apply to eavesdropping, that closes the matter for me. In interpreting the Bill of Rights, I willingly go as far as a liberal construction of the language takes me, but I simply cannot in good conscience give a meaning to words which they have never before been thought to have and which they certainly do not have in common ordinary usage. I will not distort the words of the Amendment in order to `keep the Constitution up to date' or `to bring it into harmony with the times.' It was never meant that this Court have such power, which in effect would make us a continuously functioning constitutional convention." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#373" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 373</a></span>.</blockquote>
<p><span class="star-pagination">*635</span> The expansive construction of the word "seizure" in the <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> case provided an appropriate predicate for the Court's holding in <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), the following year.<sup>[8]</sup> Prior to <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> the Fourth Amendment proscribed any seizure of the person that was not supported by the same probable-cause showing that would justify a custodial arrest.<sup>[9]</sup> See <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#207" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 207-209</a></span> (1979). Given the fact that street encounters between citizens and police officers "are incredibly rich in diversity," <i>Terry,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#13" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 13</a></span>, the Court recognized the need for flexibility and held that "reasonable" suspiciona quantum of proof less demanding than probable causewas adequate to justify a stop for investigatory purposes. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 21-22</a></span>. As a corollary to the lesser justification for the stop, the Court necessarily concluded that the word "seizure" in the Fourth Amendment encompasses official restraints on individual freedom that fall short of a common-law arrest. Thus, <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> broadened the range of encounters between the police and the citizen encompassed within the term "seizure," while at the same time, lowering the standard of proof necessary to justify a "stop" in the newly expanded category of seizures <span class="star-pagination">*636</span> now covered by the Fourth Amendment.<sup>[10]</sup> The Court explained:</p>
<blockquote>"Our first task is to establish at what point in this encounter the Fourth Amendment becomes relevant. That is, we must decide whether and when Officer McFadden `seized' Terry and whether and when he conducted a `search.' There is some suggestion in the use of such terms as `stop' and `frisk' that such police conduct is outside the purview of the Fourth Amendment because neither action rises to the level of a `search' or `seizure' within the meaning of the Constitution. We emphatically reject this notion. It is quite plain that the Fourth Amendment governs `seizures' of the person which do not eventuate in a trip to the station house and prosecution for crime`arrests' in traditional terminology. It must be recognized that whenever a police officer accosts an individual and restrains his freedom to walk away, he has `seized' that person." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 16</a></span> (footnote omitted).</blockquote>
<blockquote>"The distinctions of classical `stop-and-frisk' theory thus serve to divert attention from the central inquiry under the Fourth Amendmentthe reasonableness in all the circumstances of the particular governmental invasion of a citizen's personal security. `Search' and `seizure' are not talismans. We therefore reject the notions that the Fourth Amendment does not come into play at all as a limitation upon police conduct if the officers stop short of something called a `technical arrest' or a `full-blown search.'" <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 19</a></span>.</blockquote>
<p><span class="star-pagination">*637</span> The decisions in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> and <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> unequivocally reject the notion that the common law of arrest defines the limits of the term "seizure" in the Fourth Amendment. In <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> the Court abandoned the narrow view that would have limited a seizure to a material object, and, instead, held that the Fourth Amendment extended to the recording of oral statements. And in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> the Court abandoned its traditional view that a seizure under the Fourth Amendment required probable cause, and, instead, expanded the definition of a seizure to include an investigative stop made on less than probable cause. Thus, the major premise underpinning the majority's entire analysis todaythat the common law of arrest should define the term "seizure" for Fourth Amendment purposes, see <i>ante,</i> at 624-625is seriously flawed. The Court mistakenly hearkens back to common law, while ignoring the expansive approach that the Court has taken in Fourth Amendment analysis since <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> and <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</i><sup>[11]</sup></p>
<p></p>
<h2>II</h2>
<p>The Court fares no better when it tries to explain why the proper definition of the term "seizure" has been an open question until today. In <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> in addition to stating that a seizure occurs "whenever a police officer accosts an individual and restrains his freedom to walk away," <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 16</a></span>, the Court noted that a seizure occurs "when the officer, by means of physical force or show of authority, has in some way restrained the liberty of a citizen. . . ." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 19, n. 16</a></span>. The touchstone of a seizure is the restraint of an individual's personal liberty <i>"in some way." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ibid.</a></span></i> (emphasis added).<sup>[12]</sup> Today the Court's reaction to respondent's reliance on <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> <span class="star-pagination">*638</span> is to demonstrate that in "show of force" cases no common-law arrest occurs unless the arrestee <i>submits.</i> See <i>ante,</i> at 626-627. That answer, however, is plainly insufficient given the holding in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> that the Fourth Amendment applies to stops that need not be justified by probable cause in the absence of a full-blown arrest.</p>
<p>In <i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544</a></span> (1980), the Court "adhere[d] to the view that a person is `seized' only when, by means of physical force or a show of authority, his freedom of movement is restrained." <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#553" aria-description="Citation for case: United States v. Mendenhall"><i>Id.,</i> at 553</a></span>. The Court looked to whether the citizen who is questioned "remains free to disregard the questions and walk away," and if he or she is able to do so, then "there has been no intrusion upon that person's liberty or privacy" that would require some "particularized and objective justification" under the Constitution. <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall"><i>Id.,</i> at 554</a></span>. The test for a "seizure," as formulated by the Court in <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span>,</i> was whether, "in view of all of the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave." <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Ibid.</a></span></i> Examples of seizures include "the threatening presence of several officers, the display of a weapon by an officer, some physical touching of the person of the citizen, or the use of language or tone of voice indicating that compliance with the officer's request might be compelled." <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Ibid.</a></span></i> The Court's unwillingness today to adhere to the "reasonable person" standard, as formulated by Justice Stewart in <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span>,</i> marks an unnecessary departure from Fourth Amendment case law.</p>
<p>The Court today draws the novel conclusion that even though no seizure can occur <i>unless</i> the <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span></i> reasonable person standard is met, see <i>ante,</i> at 628, the fact that the standard has been met does not necessarily mean that a seizure has occurred. See <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">ibid.</a></span> (Mendenhall</i> "states a <i>necessary,</i> but not a <i>sufficient</i> condition for seizure . . . effected <span class="star-pagination">*639</span> through a `show of authority'"). If it were true that a seizure requires more than whether a reasonable person felt free to leave, then the following passage from the Court's opinion in <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210</a></span> (1984), is at best, seriously misleading:</p>
<blockquote>"As we have noted elsewhere: `Obviously, not all personal intercourse between policemen and citizens involves "seizures" of persons. Only when the officer, by means of physical force or show of authority, has restrained the liberty of a citizen may we conclude that a "seizure" has occurred.' <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i> at 19, n. 16</a></span>. While applying such a test is relatively straightforward in a situation resembling a traditional arrest, see <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 212-216</a></span> (1979), the protection against unreasonable seizures also extends to `seizures that involve only a brief detention short of traditional arrest.' <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975). What has evolved from our cases is a determination that an initially consensual encounter between a police officer and a citizen can be transformed into a seizure or detention within the meaning of the Fourth Amendment, `if, in view of all the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave.' <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall"><i>Mendenhall, supra,</i> at 554</a></span> (footnote omitted); see <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#502" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 502</a></span> (1983) (plurality opinion)." <i>Id.,</i> at 215.</blockquote>
<p>More importantly, in <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983), a plurality of the Court adopted Justice Stewart's formulation in <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span></i> as the appropriate standard for determining when police questioning crosses the threshold from a consensual encounter to a forcible stop. In <i><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span>,</i> the Court held that an illegal seizure had occurred. As a <span class="star-pagination">*640</span> predicate for that holding, JUSTICE WHITE, in his opinion for the plurality, explained that the citizen "may not be detained <i>even momentarily</i> without reasonable, objective grounds for doing so; and his refusal to listen or answer does not, without more, furnish those grounds. <i>United States</i> v. <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#556" aria-description="Citation for case: United States v. Mendenhall"><i>Mendenhall, supra,</i> at 556</a></span> (opinion of Stewart, J.)." <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#498" aria-description="Citation for case: Florida v. Royer">460 U. S., at 498</a></span> (emphasis added). The rule looks, not to the subjective perceptions of the person questioned, but rather, to the objective characteristics of the encounter that may suggest whether a reasonable person would have felt free to leave.</p>
<p>Even though momentary, a seizure occurs whenever an objective evaluation of a police officer's show of force conveys the message that the citizen is not entirely free to leavein other words, that his or her liberty is being restrained in a significant way. That the Court understood the <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span></i> definition as both necessary and sufficient to describe a Fourth Amendment seizure is evident from this passage in our opinion in <i>United States</i> v. <i>Jacobsen,</i> <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109</a></span> (1984):</p>
<blockquote>"A `seizure' of property occurs when there is some meaningful interference with an individual's possessory interests in that property.5</blockquote>
<p>5 "See <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983); <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#716" aria-description="Citation for case: United States v. Place"><i>id.,</i> at 716</a></span> (BRENNAN, J., concurring in result); <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#747" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 747-748</a></span> (1983) (STEVENS, J., concurring in judgment); see also <i>United States v. Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 13-14, n. 8</a></span> (1977); <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#76" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 76</a></span> (1906). While the concept of a `seizure' of property is not much discussed in our cases, this definition follows from our oftrepeated definition of the `seizure' of a person within the meaning of the Fourth Amendmentmeaningful interference, however brief, with an individual's freedom of movement. See <i>Michigan</i> v. <i>Summers,</i> <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#696" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 696</a></span> (1981); <i>Reid</i> v. <i>Georgia,</i> <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#440" aria-description="Citation for case: Reid v. Georgia">448 U. S. 438, 440</a></span>, n. (1980) <i>(per curiam); </i><i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#551" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 551-554</a></span> (1980) (opinion of Stewart, J.); <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#50" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 50</a></span> (1979); <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975); <i>Cupp</i> v. <i>Murphy,</i> <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#294" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291, 294-295</a></span> (1973); <i>Davis</i> v. <i>Mississippi,</i> <span class="star-pagination">*641</span> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#726" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 726-727</a></span> (1969); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 16, 19, n. 16</a></span>." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#113" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 113</a></span>, and n. 5.</p>
<p>Finally, it is noteworthy that in <i>Michigan</i> v. <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/" aria-description="Citation for case: Michigan v. Chesternut">486 U. S. 567</a></span> (1988), the State asked us to repudiate the reasonable person standard developed in <i>Terry, Mendenhall, Delgado,</i> and <i><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span>.</i><sup>[13]</sup> We decided, however, to "adhere to our traditional contextual approach," <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#573" aria-description="Citation for case: Michigan v. Chesternut">486 U. S., at 573</a></span>. In our opinion, we described Justice Stewart's analysis in <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span></i> as "a test to be applied in determining whether `a person has been "seized" within the meaning of the Fourth Amendment'" and noted that "[t]he Court has since embraced this test." <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#573" aria-description="Citation for case: Michigan v. Chesternut">486 U. S., at 573</a></span>. Moreover, in commenting on the virtues of the test, we explained that it focused on the police officer's conduct:</p>
<blockquote>"The test's objective standardlooking to the reasonable man's interpretation of the conduct in questionallows the police to determine in advance whether the conduct contemplated will implicate the Fourth Amendment." <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#574" aria-description="Citation for case: Michigan v. Chesternut"><i>Id.,</i> at 574</a></span>.</blockquote>
<p>Expressing his approval of the Court's rejection of Michigan's argument in <i><span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/" aria-description="Citation for case: Michigan v. Chesternut">Chesternut</a></span>,</i> Professor LaFave observed:</p>
<blockquote>"The `free to leave' concept, in other words, has nothing to do with a particular suspect's choice to flee rather than submit or with his assessment of the probability of successful flight. Were it otherwise, police would be encouraged to utilize a very threatening but sufficiently slow chase as an evidence-gathering technique whenever they lack even the reasonable suspicion needed for a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop." 3 W. LaFave, Search and Seizure § 9.2, p. 61 (2d ed. 1987, Supp. 1991).</blockquote>
<p><span class="star-pagination">*642</span> Whatever else one may think of today's decision, it unquestionably represents a departure from earlier Fourth Amendment case law. The notion that our prior cases contemplated a distinction between seizures effected by a touching on the one hand, and those effected by a show of force on the other hand, and that all of our repeated descriptions of the <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span></i> test stated only a necessary, but not a sufficient, condition for finding seizures in the latter category, is nothing if not creative lawmaking. Moreover, by narrowing the definition of the term seizure, instead of enlarging the scope of reasonable justifications for seizures, the Court has significantly limited the protection provided to the ordinary citizen by the Fourth Amendment. As we explained in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>:</i></p>
<blockquote>"The danger in the logic which proceeds upon distinctions between a `stop' and an `arrest,' or `seizure' of the person, and between a `frisk' and a `search' is twofold. It seeks to isolate from constitutional scrutiny the initial stages of the contact between the policeman and the citizen. And by suggesting a rigid all-or-nothing model of justification and regulation under the Amendment, it obscures the utility of limitations upon the scope, as well as the initiation, of police action as a means of constitutional regulation." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#17" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 17</a></span>.</blockquote>
<p></p>
<h2>III</h2>
<p>In this case the officer's show of forcetaking the form of a head-on chaseadequately conveyed the message that respondent was not free to leave.<sup>[14]</sup> Whereas in <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span>,</i> there was "nothing in the record [to] sugges[t] that the respondent <span class="star-pagination">*643</span> had any objective reason to believe that she was not free to end the conversation in the concourse and proceed on her way," <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#555" aria-description="Citation for case: United States v. Mendenhall">446 U. S., at 555</a></span>, here, respondent attempted to end "the conversation" before it began and soon found himself literally "not free to leave" when confronted by an officer running toward him head-on who eventually tackled him to the ground. There was an interval of time between the moment that respondent saw the officer fast approaching and the moment when he was tackled, and thus brought under the control of the officer. The question is whether the Fourth Amendment was implicated at the earlier or the later moment.</p>
<p>Because the facts of this case are somewhat unusual, it is appropriate to note that the same issue would arise if the show of force took the form of a command to "freeze," a warning shot, or the sound of sirens accompanied by a patrol car's flashing lights. In any of these situations, there may be a significant time interval between the initiation of the officer's show of force and the complete submission by the citizen. At least on the facts of this case, the Court concludes that the timing of the seizure is governed by the citizen's reaction, rather than by the officer's conduct. See <i>ante,</i> at 626-627. One consequence of this conclusion is that the point at which the interaction between citizen and police officer becomes a seizure occurs, not when a reasonable citizen believes he or she is no longer free to go, but, rather, only after the officer exercises control over the citizen.</p>
<p>In my view, our interests in effective law enforcement and in personal liberty<sup>[15]</sup> would be better served by adhering to a standard that "allows the police to determine in advance whether the conduct contemplated will implicate the Fourth <span class="star-pagination">*644</span> Amendment." <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#574" aria-description="Citation for case: Michigan v. Chesternut">486 U. S., at 574</a></span>. The range of possible responses to a police show of force, and the multitude of problems that may arise in determining whether, and at which moment, there has been "submission," can only create uncertainty and generate litigation.</p>
<p>In some cases, of course, it is immediately apparent at which moment the suspect submitted to an officer's show of force. For example, if the victim is killed by an officer's gunshot,<sup>[16]</sup> as in <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#11" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1, 11</a></span> (1985) ("A police officer may not seize an unarmed, nondangerous suspect by shooting him dead"),<sup>[17]</sup> or by a hidden roadblock, as in <i>Brower</i> v. <i>Inyo County,</i> <span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo">489 U. S. 593</a></span> (1989), the submission is unquestionably complete. But what if, for example, William James Caldwell (Brower) had just been wounded before being apprehended? Would it be correct to say that no seizure had occurred and therefore the Fourth Amendment was not implicated even if the pursuing officer had no justification whatsoever for initiating the chase? The Court's opinion in <i><span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo">Brower</a></span></i> suggests that the officer's responsibility should not depend on the character of the victim's evasive action. The Court wrote:</p>
<blockquote>"Brower's independent decision to continue the chase can no more eliminate respondents' responsibility for the termination of his movement effected by the roadblock than Garner's independent decision to flee eliminated the Memphis police officer's responsibility for the termination of his movement effected by the bullet." <span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/#595" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo"><i>Id.,</i> at 595</a></span>.</blockquote>
<p><span class="star-pagination">*645</span> It seems equally clear to me that the constitutionality of a police officer's show of force should be measured by the conditions that exist at the time of the officer's action. A search must be justified on the basis of the facts available at the time it is initiated; the subsequent discovery of evidence does not retroactively validate an unconstitutional search. The same approach should apply to seizures; the character of the citizen's response should not govern the constitutionality of the officer's conduct.</p>
<p>If an officer effects an arrest by touching a citizen, apparently the Court would accept the fact that a seizure occurred, even if the arrestee should thereafter break loose and flee. In such a case, the constitutionality of the seizure would be evaluated as of the time the officer acted. That category of seizures would then be analyzed in the same way as searches, namely, was the police action justified when it took place? It is anomalous, at best, to fashion a different rule for the subcategory of "show of force" arrests.</p>
<p>In cases within this new subcategory, there will be a period of time during which the citizen's liberty has been restrained, but he or she has not yet completely submitted to the show of force. A motorist pulled over by a highway patrol car cannot come to an immediate stop, even if the motorist intends to obey the patrol car's signal. If an officer decides to make the kind of random stop forbidden by <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648</a></span> (1979), and, after flashing his lights, but before the vehicle comes to a complete stop, sees that the license plate has expired, can he justify his action on the ground that the seizure became lawful after it was initiated but before it was completed? In an airport setting, may a drug enforcement agent now approach a group of passengers with his gun drawn, announce a "baggage search," and rely on the passengers' reactions to justify his investigative stops? The holding of today's majority fails to recognize the coercive and intimidating nature of such behavior and creates a rule that may allow such behavior to go unchecked.</p>
<p><span class="star-pagination">*646</span> The deterrent purposes of the exclusionary rule focus on the conduct of law enforcement officers and on discouraging improper behavior on their part,<sup>[18]</sup> and not on the reaction of the citizen to the show of force. In the present case, if Officer Pertoso had succeeded in tackling respondent before he dropped the rock of cocaine, the rock unquestionably would have been excluded as the fruit of the officer's unlawful seizure. Instead, under the Court's logic-chopping analysis, the exclusionary rule has no application because an attempt to make an unconstitutional seizure is beyond the coverage of the Fourth Amendment, no matter how outrageous or unreasonable the officer's conduct may be.</p>
<p>It is too early to know the consequences of the Court's holding. If carried to its logical conclusion, it will encourage unlawful displays of force that will frighten countless innocent citizens into surrendering whatever privacy rights they <span class="star-pagination">*647</span> may still have. It is not too soon, however, to note the irony in the fact that the Court's own justification for its result is its analysis of the rules of the common law of arrest that antedated our decisions in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> and <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</i> Yet, even in those days the common law provided the citizen with protection against an attempt to make an unlawful arrest. See nn. 5 and 7, <i>supra.</i> The central message of <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> and <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> was that the protection the Fourth Amendment provides to the average citizen is not rigidly confined by ancient common-law precept. The message that today's literal-minded majority conveys is that the common law, rather than our understanding of the Fourth Amendment as it has developed over the last quarter of a century, defines, and limits, the scope of a seizure. The Court today defines a seizure as commencing, not with egregious police conduct, but rather with submission by the citizen. Thus, it both delays the point at which "the Fourth Amendment becomes relevant"<sup>[19]</sup> to an encounter and limits the range of encounters that will come under the heading of "seizure." Today's qualification of the Fourth Amendment means that innocent citizens may remain "secure in their persons . . . against unreasonable searches and seizures" only at the discretion of the police.<sup>[20]</sup></p>
<p>Some sacrifice of freedom always accompanies an expansion in the Executive's unreviewable<sup>[21]</sup> law enforcement powers. <span class="star-pagination">*648</span> A court more sensitive to the purposes of the Fourth Amendment would insist on greater rewards to society before decreeing the sacrifice it makes today. Alexander Bickel presciently wrote that "many actions of government have two aspects: their immediate, necessarily intended, practical effects, and their perhaps unintended or unappreciated bearing on values we hold to have more general and permanent interest."<sup>[22]</sup> The Court's immediate concern with containing criminal activity poses a substantial, though unintended, threat to values that are fundamental and enduring.</p>
<p>I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> urging reversal were filed for the Criminal Justice Legal Foundation by <i>Kent S. Scheidegger</i> and <i>Charles L. Hobson;</i> and for the Wayne County Prosecuting Attorney by <i>John D. O'Hair, pro se,</i> and <i>Timothy A. Baughman.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the California Attorneys for Criminal Justice by <i>Paul L. Gabbert;</i> and for the National Association of Criminal Defense Lawyers by <i>Paul Morris.</i></p>
<p>Briefs of <i>amici curiae</i> were filed for the Appellate Committee of the California District Attorneys Association by <i>Ira Reiner</i> and <i>Harry B. Sondheim;</i> and for <i>Marvin Cahn, pro se.</i></p>
<p>[1]  California conceded below that Officer Pertoso did not have the "reasonable suspicion" required to justify stopping Hodari, see <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). That it would be unreasonable to stop, for brief inquiry, young men who scatter in panic upon the mere sighting of the police is not self-evident, and arguably contradicts proverbial common sense. See Proverbs 28:1 ("The wicked flee when no man pursueth"). We do not decide that point here, but rely entirely upon the State's concession.</p>
<p>[2]  For this simple reasonwhich involves neither "logic-chopping," <i>post,</i> at 646, nor any arcane knowledge of legal historyit is irrelevant that English law proscribed "an unlawful <i>attempt</i> to take a presumptively innocent person into custody." <i>Post,</i> at 631. We have consulted the common law to explain the meaning of seizureand, contrary to the dissent's portrayal, to expand rather than contract that meaning (since one would not normally think that the mere touching of a person would suffice). But neither usage nor common-law tradition makes an <i>attempted</i> seizure a seizure. The common law may have made an attempted seizure unlawful in certain circumstances; but it made many things unlawful, very few of which were elevated to constitutional proscriptions.</p>
<p>[3]  Nor have we ever done so. The dissent is wrong in saying that <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), "broadened the range of encounters . . . encompassed within the term `seizure,'" <i>post,</i> at 635. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> unquestionably involved conduct that would constitute a common-law seizure; its novelty (if any) was in expanding the acceptable <i>justification</i> for such a seizure, beyond probable cause. The dissent is correct that <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), "unequivocally reject[s] the notion that the common law of arrest defines the limits of the term `seizure' in the Fourth Amendment," <i>post,</i> at 637. But we do not assert that it defines the limits of the term "seizure"; only that it defines the limits of a <i>seizure of the person.</i> What <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> stands for is the proposition that items which could not be subject to seizure at common law (<i>e. g.,</i> telephone conversations) can be seized under the Fourth Amendment. That is quite different from saying that what constitutes an arrest (a seizure of the person) has changed.</p>
<p>[1]  The Fourth Amendment to the Constitution protects "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures . . . ."</p>
<p>[2]  <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967).</p>
<p>[3]  <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968).</p>
<p>[4]  The Court's gratuitous quotation from Proverbs 28:1, see <i>ante,</i> at 623, n. 1, mistakenly assumes that innocent residents have no reason to fear the sudden approach of strangers. We have previously considered, and rejected, this ivory-towered analysis of the real world for it fails to describe the experience of many residents, particularly if they are members of a minority. See generally Johnson, Race and the Decision To Detain a Suspect, 93 Yale L. J. 214 (1983). It has long been "a matter of common knowledge that men who are entirely innocent do sometimes fly from the scene of a crime through fear of being apprehended as the guilty parties, or from an unwillingness to appear as witnesses. Nor is it true as an accepted axiom of criminal law that `the wicked flee when no man pursueth, but the righteous are as bold as a lion.'" <i>Alberty</i> v. <i>United States,</i> <span class="citation" data-id="94447"><a href="/opinion/94447/alberty-v-united-states/#511" aria-description="Citation for case: Alberty v. United States">162 U. S. 499, 511</a></span> (1896).</p>
<p>[5]  "[I]f the officer pronounces words of arrest without an actual touching and the other immediately runs away, there is no escape (in the technical sense) because there was no arrest. It would be otherwise had the officer touched the arrestee for the purpose of apprehending him, because touching for the manifested purpose of arrest by one having lawful authority completes the apprehension, `although he does not succeed in stopping or holding him even for an instant.'" Perkins, The Law of Arrest, <span class="citation no-link">25 Iowa L. Rev. 201</span>, 206 (1940) (footnotes omitted).</p>
<p>[6]  "One who undertakes to make an arrest without lawful authority, or who attempts to do so in an unlawful manner, is guilty of an assault if the other is ordered to submit to the asserted authority, is guilty of battery if he lays hands on the other for this unlawful purpose . . . ." <span class="citation no-link"><i>Id.,</i> at 263</span> (footnotes omitted).</p>
<p>[7]  "[E]ven without touching the other, the officer may subject himself to liability if he undertakes to make an arrest without being privileged by law to do so.3
</p>
<p>"3 For example, an officer might be guilty of an assault because of an attempted arrest, without privilege, even if he did not succeed in touching the other. Furthermore, if the other submitted to such an arrest without physical contact, the officer is liable for false imprisonment. Gold v. Bissell, <span class="citation" data-id="5512913"><a href="/opinion/5665934/gold-v-bissell/" aria-description="Citation for case: Gold v. Bissell">1 Wend. 210</a></span> (N. Y. Sup. Ct. 1828)." <i>Id.,</i> at 201.</p>
<p>[8]  "We have recently held that `the Fourth Amendment protects people, not places,' <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967), and wherever an individual may harbor a reasonable `expectation of privacy,' <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States"><i>id.,</i> at 361</a></span> (MR. JUSTICE HARLAN, concurring), he is entitled to be free from unreasonable governmental intrusion. Of course, the specific content and incidents of this right must be shaped by the context in which it is asserted. For `what the Constitution forbids is not all searches and seizures, but unreasonable searches and seizures.' <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#222" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 222</a></span> (1960)." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#9" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 9</a></span>.</p>
<p>[9]  <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924), the case on which the majority largely relies, was decided over 40 years before <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</i> In that case, the defendant did not even argue that there was a seizure of his person. The Court's holding in <i><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">Hester</a></span></i> that the abandoned moonshine whiskey had not been seized simply did not address the question whether it would have been the fruit of a constitutional violation if there had been a seizure of the person before the whiskey was abandoned.</p>
<p>[10]  The Court applied this principle in <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">443 U. S. 47</a></span> (1979):
</p>
<p>"We have recognized that in some circumstances an officer may detain a suspect briefly for questioning, although he does not have `probable cause' to believe that the suspect is involved in criminal activity, as is required for a traditional arrest. However, we have required the officers to have a reasonable suspicion, based on objective facts, that the individual is involved in criminal activity." <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas"><i>Id.,</i> at 51</a></span> (citations omitted).</p>
<p>[11]  It is noteworthy that the Court has relied so heavily on cases and commentary that antedated <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> and <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</i></p>
<p>[12]  "The essential teaching of the Court's decision in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i>that an individual's right to personal security and freedom must be respected even in encounters with the police that fall short of full arresthas been consistently reaffirmed." <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#227" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 227</a></span> (1984) (Brennan, J., concurring in part and dissenting in part).</p>
<p>[13]  "Petitioner argues that the Fourth Amendment is never implicated until an individual stops in response to the police's show of authority. Thus, petitioner would have us rule that a lack of objective and particularized suspicion would not poison police conduct, no matter how coercive, as long as the police did not succeed in actually apprehending the individual." <i>Michigan</i> v. <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#572" aria-description="Citation for case: Michigan v. Chesternut">486 U. S., at 572</a></span>.</p>
<p>[14]  The California Court of Appeal noted:
</p>
<p>"This case involves more than a pursuit, as Officer Pertoso did not pursue [respondent], but ran in such a fashion as to cut him off and confront him head on. Under the rationale of <i><span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/" aria-description="Citation for case: Michigan v. Chesternut">Chesternut</a></span>,</i> this action is reasonably perceived as an intrusion upon one's freedom of movement and as a maneuver intended to block or `otherwise control the direction or speed' of one's movement." App. A to Pet. for Cert. 9.</p>
<p>[15]  "To determine the constitutionality of a seizure `[w]e must balance the nature and quality of the intrusion on the individual's Fourth Amendment interests against the importance of the governmental interests alleged to justify the intrusion.'" <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#8" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1, 8</a></span> (1985) (citation omitted).</p>
<p>[16]  Even under the common law, "If an officer shoots at an arrestee when he is not privileged to do so, he is guilty of an aggravated assault. And if death results from an arrest, or attempted arrest, which was not authorized at all, . . . the arrester is guilty of manslaughter or, in extreme cases, of murder." Perkins, 25 Iowa L. Rev., at 263-264.</p>
<p>[17]  In <i>Tennessee</i> v. <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span></i><i>,</i> even the dissent agreed with the majority that the police officer who shot at a fleeing suspect had "`seized' [the suspect] by shooting him." <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#25" aria-description="Citation for case: Tennessee v. Garner">471 U. S., at 25</a></span> (O'CONNOR, J., dissenting).</p>
<p>[18]  The purpose of the Fourth Amendment is "`to prevent arbitrary and oppressive interference by enforcement officials with the privacy and personal security of individuals.'" <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S., at 215</a></span> (quoting <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#554" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 554</a></span> (1976)); see <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#553" aria-description="Citation for case: United States v. Mendenhall">446 U. S., at 553-554</a></span> (same); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#12" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 12</a></span> ("Ever since its inception, the rule excluding evidence seized in violation of the Fourth Amendment has been recognized as a principal mode of discouraging lawless police conduct"); 4 W. LaFave, Search and Seizure § 11.4(j), pp. 459-460 (2d ed. 1987) ("Incriminating admissions and attempts to dispose of incriminating evidence are common and predictable consequences of illegal arrests and searches, and thus to admit such evidence would encourage such Fourth Amendment violations in future cases").
</p>
<p>Justice Brandeis wrote eloquently about the overarching purpose of the Fourth Amendment:</p>
<p>"The makers of our Constitution . . . sought to protect Americans in their beliefs, their thoughts, their emotions and their sensations. They conferred, as against the Government, the right to be let alonethe most comprehensive of rights and the right most valued by civilized men. To protect that right, every unjustifiable intrusion by the Government upon the privacy of the individual, whatever the means employed, must be deemed a violation of the Fourth Amendment." <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#478" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 478</a></span> (1928) (dissenting opinion).</p>
<p>Today's opinion has lost sight of these purposes.</p>
<p>[19]  <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 16</a></span>.</p>
<p>[20]  Justice Jackson presaged this development when he wrote:
</p>
<p>"[A]n illegal search and seizure usually is a single incident, perpetrated by surprise, conducted in haste, kept purposely beyond the court's supervision and limited only by the judgment and moderation of officers whose own interests and records are often at stake in the search . . . . The citizen's choice is quietly to submit to whatever the officers undertake or to resist at risk of arrest or immediate violence." <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#182" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 182</a></span> (1949) (dissenting opinion).</p>
<p>[21]  "[T]he right to be secure against searches and seizures is one of the most difficult to protect. Since the officers are themselves the chief invaders, there is no enforcement outside of court . . . . There may be, and I am convinced that there are, many unlawful searches of homes and automobiles of innocent people which turn up nothing incriminating, in which no arrest is made, about which courts do nothing, and about which we never hear." <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#181" aria-description="Citation for case: Brinegar v. United States"><i>Id.,</i> at 181</a></span> (Jackson, J., dissenting).</p>
<p>[22]  The Least Dangerous Branch 24 (1962).</p>

</div>
```

---

## GROUP: content/cases/California v. Prysock.md  (`case`, 5 assertions)

### content_page

```
---
title: "California v. Prysock"
type: case
citation: "453 U.S. 355 (1981)"
parallel_cite: "101 S. Ct. 2806; 69 L. Ed. 2d 696; 49 U.S.L.W. 3964"
neutral_cite: 1981 U.S. LEXIS 131
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1981
date_decided: 1981-06-29
docket: 80-1846
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1981-06-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: California v. Prysock
  varies_by_point: false
  scope_note: "Reaffirmed and applied by Duckworth v. Eagan (1989) and Florida v. Powell (2010); good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110556/california-v-prysock/"
  cluster_id: 110556
  opinion_id: 9428478
  identity_checked: false
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny"
related: ["[[Duckworth v. Eagan]]", "[[Florida v. Powell]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "warning-adequacy"]
holding: "Miranda warnings need not be a verbatim recital of the language in Miranda; a warning that reasonably conveys the suspect's rights is adequate — no talismanic incantation is required."
lake:
  record_id: California v. Prysock
  status: under_review
  projected_at: 2026-07-06
---

# California v. Prysock

*451 U.S. 355 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Randall Prysock, a juvenile murder suspect, was given [[Miranda and Custodial Interrogation|Miranda warnings]] before questioning. He was told he had the right to a lawyer before and during questioning and the right to have a lawyer appointed at no cost if he could not afford one. The California Court of Appeal held the warnings defective because the appointed-counsel advice was not expressly tied to a point *before* questioning, and suppressed his statements.

## Issue
Whether [[Miranda and Custodial Interrogation|Miranda warnings]] are inadequate simply because the advice about the right to appointed counsel was not given in the precise language or sequence used in *[[Miranda v. Arizona|Miranda]]* itself.

## Rule
No. [[Miranda and Custodial Interrogation|Miranda warnings]] need not track an exact script; a warning that reasonably conveys the rights suffices. "This Court has never indicated that the 'rigidity' of *Miranda* extends to the precise formulation of the warnings given a criminal defendant." — 451 U.S. at 359. ^pin-359

"*Miranda* itself indicated that no talismanic incantation was required to satisfy its strictures." — *Id.* ^pin-359a

Reviewing courts examine the warnings actually given to determine whether they reasonably conveyed the right to appointed counsel, rather than demanding "a verbatim recital of the words of the *Miranda* opinion." — *Id.*

## Application
The warnings given Prysock told him he had the right to a lawyer before and during questioning and the right to have a lawyer appointed without cost. Nothing in those warnings linked the appointment of counsel to a future time *after* interrogation (the defect that had invalidated warnings in cases like *People v. Bolinski*). Read as a whole, the warnings conveyed that Prysock could have appointed counsel present prior to and during questioning, so they satisfied *[[Miranda v. Arizona|Miranda]]*.

## Conclusion
The warnings were adequate. The judgment of the California Court of Appeal was reversed and the case [[Reading and Citing Cases#on-remand|remanded]]. Miranda compliance turns on whether the warnings reasonably convey the rights, not on verbatim recital.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The "reasonably conveys" rule was reaffirmed and applied in [[Duckworth v. Eagan]] (warnings adequate despite "if and when you go to court" language) and [[Florida v. Powell]] (warnings need not be verbatim).

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny*

## Sources
- *California v. Prysock*, 451 U.S. 355 (1981) (per curiam) — https://www.courtlistener.com/opinion/110556/california-v-prysock/ — pinpoint: 359.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "cd0983dc0c49bbb6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "453 U.S. 355 (1981)", "court": "U.S. Supreme Court", "neutral_cite": "1981 U.S. LEXIS 131", "official_citation_present": true, "parallel_cite": "101 S. Ct. 2806; 69 L. Ed. 2d 696; 49 U.S.L.W. 3964", "title": "California v. Prysock", "year": "1981"}}
{"assertion_id": "b9f397885a0711b8", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Progeny", "title": "California v. Prysock"}}
{"assertion_id": "c1d01d2fc8ac7a00", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Miranda warnings need not be a verbatim recital of the language in Miranda; a warning that reasonably conveys the suspect's rights is adequate — no talismanic incantation is required.", "title": "California v. Prysock"}}
{"assertion_id": "3eaec743bca9e56f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "California v. Prysock"}}
{"assertion_id": "e39732f0668ddf66", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1981-06-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "California v. Prysock", "field_i_validity": "good_law", "scope_note": "Reaffirmed and applied by Duckworth v. Eagan (1989) and Florida v. Powell (2010); good law.", "title": "California v. Prysock", "varies_by_point": "false"}}
```

### lake record — California v. Prysock

```json
{
  "schema_version": "s2.v1",
  "record_id": "California v. Prysock",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "California v. Prysock",
    "case_name_short": "Prysock",
    "case_name_full": "California v. Prysock",
    "input_case_name": "California v. Prysock",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1981-06-29",
    "year": 1981,
    "docket": "80-1846",
    "cluster_id": 110556,
    "lead_opinion_id": 9428478,
    "sibling_ids": [
      110556,
      9428478,
      9428479
    ],
    "absolute_url": "/opinion/110556/california-v-prysock/",
    "identity_method": "name+docket",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 110503,
        "score": 20,
        "case_name": "California v. Prysock"
      }
    ],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "453 U.S. 355",
      "volume": "453",
      "reporter": "U.S.",
      "page": "355",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "101 S. Ct. 2806",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2806",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 696",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "696",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 U.S.L.W. 3964",
        "volume": "49",
        "reporter": "U.S.L.W.",
        "page": "3964",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1981 U.S. LEXIS 131",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "131",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "453 U.S. 355",
        "volume": "453",
        "reporter": "U.S.",
        "page": "355",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 S. Ct. 2806",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2806",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 696",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "696",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1981 U.S. LEXIS 131",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "131",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 U.S.L.W. 3964",
        "volume": "49",
        "reporter": "U.S.L.W.",
        "page": "3964",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "453 U.S. 355",
    "official_selection": {
      "court_class": "scotus",
      "selected": "453 U.S. 355",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-359",
      "page": null,
      "quote": "--- # California v. Prysock *451 U.S. 355 (1981)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Randall Prysock, a juvenile murder suspect, was given Miranda warnings before questioning. He was told he had the right to a lawyer before and during questioning and the right to have a lawyer appointed at no cost if he could not afford one. The California Court of Appeal held the warnings defective because the appointed-counsel advice was not expressly tied to a point *before* questioning, and suppressed his statements. ## Issue Whether Miranda warnings are inadequate simply because the advice about the right to appointed counsel was not given in the precise language or sequence used in *Miranda* itself. ## Rule No. Miranda warnings need not track an exact script; a warning that reasonably conveys the rights suffices.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-359a",
      "page": null,
      "quote": "*Miranda* itself indicated that no talismanic incantation was required to satisfy its strictures.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1981-06-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "California v. Prysock",
    "varies_by_point": false,
    "scope_note": "Reaffirmed and applied by Duckworth v. Eagan (1989) and Florida v. Powell (2010); good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Larry Loucious",
          "cluster_id": 4347647,
          "cite": [
            "847 F.3d 1146",
            "2017 WL 510457",
            "2017 U.S. App. LEXIS 2166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane1_negative"
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
        "journal_ref": "California v. Prysock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ramirez",
          "cluster_id": 3958382,
          "cite": [
            "732 N.E.2d 1064",
            "135 Ohio App. 3d 89"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas v. State",
          "cluster_id": 1112339,
          "cite": [
            "625 So. 2d 1149",
            "1992 Ala. Crim. App. LEXIS 243",
            "1992 WL 92475"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Mattson",
          "cluster_id": 1345979,
          "cite": [
            "789 P.2d 983",
            "50 Cal. 3d 826",
            "268 Cal. Rptr. 802",
            "1990 Cal. LEXIS 1844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Valdivia",
          "cluster_id": 5807063,
          "cite": [
            "180 Cal. App. 3d 657",
            "226 Cal. Rptr. 144",
            "1986 Cal. App. LEXIS 1537"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane1_negative"
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
        "journal_ref": "California v. Prysock:lane2_top_cited"
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
        "journal_ref": "California v. Prysock:lane2_top_cited"
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
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rupe",
          "cluster_id": 1159824,
          "cite": [
            "683 P.2d 571",
            "101 Wash. 2d 664",
            "1984 Wash. LEXIS 1675"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Wader",
          "cluster_id": 1447881,
          "cite": [
            "854 P.2d 80",
            "5 Cal. 4th 610",
            "20 Cal. Rptr. 2d 788",
            "93 Daily Journal DAR 8799",
            "93 Cal. Daily Op. Serv. 5245",
            "1993 Cal. LEXIS 3188"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Louisias",
          "cluster_id": 5845572,
          "cite": [
            "29 A.D.3d 1017",
            "815 N.Y.S.2d 727"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Powell",
          "cluster_id": 1736,
          "cite": [
            "175 L. Ed. 2d 1009",
            "130 S. Ct. 1195",
            "559 U.S. 50",
            "2010 U.S. LEXIS 1898"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
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
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Thompson",
          "cluster_id": 1138459,
          "cite": [
            "785 P.2d 857",
            "50 Cal. 3d 134",
            "266 Cal. Rptr. 309",
            "1990 Cal. LEXIS 518"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Penry v. State",
          "cluster_id": 1565146,
          "cite": [
            "691 S.W.2d 636",
            "1985 Tex. Crim. App. LEXIS 1198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Price v. State.",
          "cluster_id": 1707117,
          "cite": [
            "725 So. 2d 1063",
            "1998 WL 560257"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ex Parte Siebert",
          "cluster_id": 1816780,
          "cite": [
            "555 So. 2d 780",
            "1989 WL 163740"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Foust",
          "cluster_id": 2689896,
          "cite": [
            "2004 Ohio 7006",
            "105 Ohio St. 3d 137",
            "823 N.E.2d 836"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Terrance Anderson",
          "cluster_id": 558038,
          "cite": [
            "929 F.2d 96",
            "1991 U.S. App. LEXIS 5371",
            "1991 WL 43249"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nollie Lee Martin v. Louie L. Wainwright",
          "cluster_id": 457158,
          "cite": [
            "770 F.2d 918",
            "78 A.L.R. Fed. 515",
            "1985 U.S. App. LEXIS 21452"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Kelly",
          "cluster_id": 2612432,
          "cite": [
            "800 P.2d 516",
            "51 Cal. 3d 931",
            "275 Cal. Rptr. 160",
            "90 Cal. Daily Op. Serv. 8544",
            "1990 Cal. LEXIS 5814"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stanley Street",
          "cluster_id": 77537,
          "cite": [
            "472 F.3d 1298",
            "2006 WL 3734533"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Colon-Cruz",
          "cluster_id": 2153683,
          "cite": [
            "562 N.E.2d 797",
            "408 Mass. 533",
            "1990 Mass. LEXIS 472"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
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
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garrett v. State",
          "cluster_id": 2460932,
          "cite": [
            "682 S.W.2d 301",
            "1984 Tex. Crim. App. LEXIS 735"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cruz, Jose, United States of America v. Alverio, Julian Miguel",
          "cluster_id": 546224,
          "cite": [
            "910 F.2d 1072"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hensley",
          "cluster_id": 2686689,
          "cite": [
            "59 Cal. 4th 788",
            "330 P.3d 296",
            "175 Cal. Rptr. 3d 213",
            "2014 WL 3747139",
            "2014 Cal. LEXIS 5317"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ex Parte Gardner",
          "cluster_id": 1785392,
          "cite": [
            "959 S.W.2d 189",
            "1998 Tex. Crim. App. LEXIS 14",
            "1996 WL 692075"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Billy Joe Battie v. W. J. Estelle, Jr., Director, Texas Department of Corrections",
          "cluster_id": 392853,
          "cite": [
            "655 F.2d 692",
            "1981 U.S. App. LEXIS 17825"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110556 OR 9428478 OR 9428479) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NzQwNzY4MDAwMDAmcz0xNTY1MTQ2JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110556+OR+9428478+OR+9428479%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110556 OR 9428478 OR 9428479)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NyZzPTU0NDczNyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110556+OR+9428478+OR+9428479%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110556 OR 9428478 OR 9428479)",
        "reviewed": 10,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 10,
        "triage_read": 0,
        "triage_snippet_classified": 10
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110556 OR 9428478 OR 9428479)",
    "indexed_citing_opinions": 288,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110556,
        "count": 252,
        "count_source": "search"
      },
      {
        "opinion_id": 9428478,
        "count": 39,
        "count_source": "search"
      },
      {
        "opinion_id": 9428479,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 537,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/california-v-prysock.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY0MzgxNjYmcz00NjU3Nzk3JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110556+OR+9428478+OR+9428479%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110556,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110556,
        "cited_id": 109997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110556,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110556,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110556,
        "cited_id": 276591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110556,
        "cited_id": 291232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110556,
        "cited_id": 291907,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110556,
        "cited_id": 296899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110556,
        "cited_id": 375540,
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
    "date_created": "2026-07-04T23:22:08Z",
    "date_modified": "2026-07-06T07:29:13Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:22:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:22:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:26:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:22:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — California v. Prysock

```
<opinion type="majority">
<author id="b397-7">Per Curiam.</author>
<p id="b397-8">This case presents the question whether the warnings given to respondent prior to a recorded conversation with a police officer satisfied the requirements of <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Although ordinarily this Court would not be inclined to review a case involving application of that precedent to a particular set of facts, see <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="109997"><a href="/opinion/109997/fare-acting-chief-probation-officer-v-michael-c/#1314" aria-description="Citation for case: Fare, Acting Chief Probation Officer v. Michael C.">439 U. S. 1310, 1314</a></span> (1978) (Rehnquist, J., in chambers, opinion of Court at <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707</a></span> (1979)), the opinion of the California Court of Appeal essentially laid down a flat rule requiring that the content of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings be a virtual incantation of the precise language contained in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion. Because such a rigid rule was not mandated by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>or any other decision of this Court, and is not required to serve the purposes of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>we grant the motion <page-number citation-index="1" label="356">*356</page-number>of respondent for leave to proceed <em>in forma -pauperis </em>and the petition for certiorari and reverse.</p>
<p id="b398-5">On January 30, 1978, Mrs. Donna Iris Erickson was brutally murdered. Later that evening respondent and a co-defendant were apprehended for commission of the offense. Respondent was brought to a substation of the Tulare County Sheriff's Department and advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. He declined to talk and, since he was a minor, his parents were notified. Respondent’s parents arrived and after meeting with them respondent decided to answer police questions. An officer questioned respondent, on tape, with respondent’s parents present. The tape reflects that the following warnings were given prior to any questioning:</p>
<blockquote id="b398-6">“Sgt. Byrd: . . . Mr. Randall James Prysock, earlier today I advised you of your legal rights and at that time you advised me you did not wish to talk to me, is that correct?</blockquote>
<blockquote id="b398-7">“Randall P.: Yeh.</blockquote>
<blockquote id="b398-8">“Sgt. Byrd: And, uh, during, at the first interview your folks were not present, they are now present. I want to go through your legal rights again with you and after each legal right I would like for you to answer whether you understand it or not. . . . Your legal rights, Mr. Prysock, is [sic] follows: Number One, you have the right to remain silent. This means you don’t have to talk to me at all unless you so desire. Do you understand this?</blockquote>
<blockquote id="b398-9">“Randall P.: Yeh.</blockquote>
<blockquote id="b398-10">“Sgt. Byrd: If you give up your right to remain silent, anything you say can and will be used as evidence against you in a court of law. Do you understand this?</blockquote>
<blockquote id="b398-11">“Randall P.: Yes.</blockquote>
<blockquote id="b398-12">“Sgt. Byrd: You have the right to talk to a lawyer before you are questioned, have him present with you while you are being questioned, and all during the questioning. Do you understand this?</blockquote>
<blockquote id="b399-5"><page-number citation-index="1" label="357">*357</page-number>“Randall P.: Yes.</blockquote>
<blockquote id="b399-6">“Sgt. Byrd: You also, being a juvenile, you have the right to have your parents present, which they are. Do you understand this?</blockquote>
<blockquote id="b399-7">“Randall P.: Yes.</blockquote>
<blockquote id="b399-8">“Sgt. Byrd: Even if they weren’t here, you’d have this right. Do you understand this?</blockquote>
<blockquote id="b399-9">“Randall P.: Yes.</blockquote>
<blockquote id="b399-10">“Sgt. Byrd: You all, uh, — if,—you have the right to have a lawyer appointed to represent you at no cost to yourself. Do you understand this?</blockquote>
<blockquote id="b399-11">“Randall P.: Yes.</blockquote>
<blockquote id="b399-12">“Sgt. Byrd: Now, having all these legal rights in mind, do you wish to talk to me at this time?</blockquote>
<blockquote id="b399-13">“Randall P.: Yes.” App. A to Pet. for Cert, i-iii.</blockquote>
<p id="b399-14">At this point, at the request of Mrs. Prysock, a conversation took place with the tape recorder turned off. According to Sgt. Byrd, Mrs. Prysock asked if respondent could still have an attorney at a later time if he gave a statement now without one. Sgt. Byrd assured Mrs. Prysock that respondent would have an attorney when he went to court and that “he could have one at this time if he wished one.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span> </em>at ll.<footnotemark>1</footnotemark></p>
<p id="b400-4"><page-number citation-index="1" label="358">*358</page-number>At trial in the Superior Court of Tulare County the court denied respondent’s motion to suppress the taped statement. Respondent was convicted by a jury of first-degree murder with two special circumstances — torture and robbery. Cal. Penal Code Ann. §§ 187, 190.2, 12022 (b) (West Supp. 1981). He was also convicted of robbery with the use of a dangerous weapon, §§ 211, 12022 (b), burglary with the use of a deadly weapon, §§ 459, 12022 (b), automobile theft, Cal. Veh. Code Ann. § 10851 (West Supp. 1981), escape from a youth facility, Cal. Welf. &amp; Inst. Code Ann. § 871 (West 1972), and destruction of evidence, Cal. Penal Code Ann. § 135 (West 1970).</p>
<p id="b400-5">The Court of Appeal for the Fifth Appellate District reversed respondent’s convictions and ordered a new trial because of what it thought to be error under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>App. A to Pet. for Cert. 4. The Court of Appeal ruled that respondent’s recorded incriminating statements, given with his parents present, had to be excluded from consideration by the jury because respondent was not properly advised of his right to the services of a free attorney before and during interrogation. Although respondent was indisputably informed that he had “the right to talk to a lawyer before you are questioned, have him present with you while you are being questioned, and all during the questioning,” and further informed that he had “the right to have a lawyer appointed to represent you at no cost to yourself,” the Court of Appeal ruled that these warnings were inadequate because respondent <page-number citation-index="1" label="359">*359</page-number>was not explicitly informed of his right to have an attorney appointed before further questioning. The Court of Appeal stated that “[o]ne of <em>[Miranda’s,] </em>virtues is its precise requirements which are so easily met,” and quoted from <em>Harryman </em>v. <em>Estelle, </em><span class="citation" data-id="9466546"><a href="/opinion/375540/burley-clifton-harryman-v-w-j-estelle-jr-director-texas-department/#873" aria-description="Citation for case: Burley Clifton Harryman v. W. J. Estelle, Jr., Director,...">616 F. 2d 870, 873-874</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/860/">449 U. S. 860</a></span> (1980), that “ 'the rigidity of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rules and the way in which they are to be applied was conceived of and continues to be recognized as the decision’s greatest strength.’ ” App. A to Pet. for Cert. 12. Relying on two previous decisions of the California Court of Appeal, <em>People </em>v. <em>Bolinski, </em><span class="citation no-link">260 Cal. App. 2d 706</span>, <span class="citation" data-id="2210787"><a href="/opinion/2210787/people-v-bolinski/" aria-description="Citation for case: People v. Bolinski">67 Cal. Rptr. 347</a></span> (1968), and <em>People </em>v. <em>Stewart, </em><span class="citation" data-id="2209476"><a href="/opinion/2209476/people-v-stewart/" aria-description="Citation for case: People v. Stewart">267 Cal. App. 2d 366</a></span>, <span class="citation" data-id="2209476"><a href="/opinion/2209476/people-v-stewart/" aria-description="Citation for case: People v. Stewart">73 Cal. Rptr. 484</a></span> (1968), the court ruled that the requirements of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>were not met in this case.<footnotemark>2</footnotemark> The California Supreme Court denied a petition for hearing, with two justices dissenting. App. D to Pet. for Cert.</p>
<p id="b401-5">This Court has never indicated that the “rigidity” of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>extends to the precise formulation of the warnings given a criminal defendant. See, <em>e. g., United States </em>v. <em>Lamia, </em><span class="citation" data-id="291232"><a href="/opinion/291232/united-states-v-robert-anthony-lamia/#375" aria-description="Citation for case: United States v. Robert Anthony Lamia">429 F. 2d 373, 375-376</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./400/907/">400 U. S. 907</a></span> (1970). This Court and others <em>have </em>stressed as one virtue of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>the fact that the giving of the warnings obviates the need for a case-by-case inquiry into the actual voluntariness of the admissions of the accused. See <em>Fare </em>v. <em>Michael C., </em>42 U. S., at 718; <em>Harryman </em>v. <em><span class="citation" data-id="9466546"><a href="/opinion/375540/burley-clifton-harryman-v-w-j-estelle-jr-director-texas-department/" aria-description="Citation for case: Burley Clifton Harryman v. W. J. Estelle, Jr., Director,...">Estelle, supra.</a></span> </em>Nothing in these observations suggests any desirable rigidity in the <em>form </em>of the required warnings.</p>
<p id="b401-6">Quite the contrary, <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>itself indicated that no talis-manic incantation was required to satisfy its strictures. The Court in that case stated that “[t]he warnings required and the waiver necessary in accordance with our opinion today <page-number citation-index="1" label="360">*360</page-number>are, <em>in the absence of a fully effective equivalent, </em>prerequisites to the admissibility of any statement made by a defendant.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#476" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 476</a></span> (emphasis supplied). See also <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona"><em>id., </em>at 479</a></span>. Just last Term in considering when <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>applied we noted that that decision announced procedural safeguards including “the now familiar <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings <em>... or their equivalent.” Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#297" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 297</a></span> (1980) (emphasis supplied).</p>
<p id="b402-5">Other courts considering the precise question presented by this case — whether a criminal defendant was adequately informed of his right to the presence of appointed counsel prior to and during interrogation — have not required a verbatim recital of the words of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion but rather have examined the warnings given to determine if the reference to the right to appointed counsel was linked with some future point in time after the police interrogation. In <em>United States </em>v. <em>Garcia, </em><span class="citation" data-id="291907"><a href="/opinion/291907/united-states-v-irene-rubio-garcia/" aria-description="Citation for case: United States v. Irene Rubio Garcia">431 F. 2d 134</a></span> (CA9 1970) <em>(per </em>curiam), for example, the court found inadequate advice to the defendant that she could “have an attorney appointed to represent you when you first appear before the U. S. Commissioner or the Court.” <em>People </em>v. <em><span class="citation" data-id="2210787"><a href="/opinion/2210787/people-v-bolinski/" aria-description="Citation for case: People v. Bolinski">Bolinski, supra,</a></span> </em>relied upon by the court below, is a case of this type. Two separate sets of warnings were ruled inadequate. In the first, the defendant was advised that <em>“if he was charged </em>... he would be appointed counsel.” <span class="citation" data-id="2210787"><a href="/opinion/2210787/people-v-bolinski/#718" aria-description="Citation for case: People v. Bolinski">260 Cal. App. 2d, at 718</a></span>, <span class="citation" data-id="2210787"><a href="/opinion/2210787/people-v-bolinski/#355" aria-description="Citation for case: People v. Bolinski">67 Cal. Rptr., at 355</a></span> (emphasis supplied). In the second, the defendant, then in Illinois and about to be moved to California, was advised that “ 'the court would appoint [an attorney] <em>in Riverside County </em>[, California].’ ” <em>Id., </em>at 723, <span class="citation" data-id="2210787"><a href="/opinion/2210787/people-v-bolinski/#359" aria-description="Citation for case: People v. Bolinski">67 Cal. Rptr., at 359</a></span> (emphasis supplied). In both instances the reference to appointed counsel was linked to a future point in time after police interrogation, and therefore did not fully advise the suspect of his right to appointed counsel before such interrogation.</p>
<p id="b402-6">Here, in contrast, nothing in the warnings given respondent suggested any limitation on the right to the presence of <page-number citation-index="1" label="361">*361</page-number>appointed counsel different from the clearly conveyed rights to a lawyer in general, including the right “to a lawyer before you are questioned, . . . while you are being questioned, and all during the questioning.” App. A to Pet. for Cert. 9-10; ii. Like <em>United States </em>v. <em>Noa, </em><span class="citation" data-id="1447295"><a href="/opinion/1447295/levy-v-kimball/" aria-description="Citation for case: Levy v. Kimball">443 P. 2d 144</a></span> (CA9 1971), where the warnings given were substantially similar to those given here and defendant’s argument was the same as that adopted by the Court of Appeal, “[t]his is not a case in which the defendant was not informed of his right to the presence of an attorney during questioning ... or in which the offer of an appointed attorney was associated with a future time in court . . . .” <span class="citation" data-id="1447295"><a href="/opinion/1447295/levy-v-kimball/#146" aria-description="Citation for case: Levy v. Kimball"><em>Id., </em>at 146</a></span>.</p>
<p id="b403-5">It is clear that the police in this case fully conveyed to respondent his rights as required by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>He was told of his right to have a lawyer present prior to and during interrogation, and his right to have a lawyer appointed at no cost if he coüld not afford one. These warnings conveyed to respondent his right to have a lawyer appointed if he could not afford one prior to and during interrogation. The Court of Appeal erred in holding that the warnings were inadequate simply because of the order in which they were given.<footnotemark>3</footnotemark></p>
<p id="b404-4"><page-number citation-index="1" label="362">*362</page-number>Because respondent was given the warnings required by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>the decision of the California Court of Appeal to the contrary is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b404-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b399-15"> The tape reflects the following concerning the off-the-record discussion:</p>
<blockquote id="b399-16">“Sgt. Byrd: . . . Okay, Mrs. Prysock, you asked to get off the tape During that time you asked, decided you wanted some time to think about getting, whether to hire a lawyer or not.</blockquote>
<blockquote id="b399-17">“Mrs. P.: ’Cause I didn’t understand it.</blockquote>
<blockquote id="b399-18">“Sgt. Byrd: And you have decided now that you want to go ahead and you do not wish a lawyer present at this time?</blockquote>
<blockquote id="b399-19">“Mrs. P.: That’s right.</blockquote>
<blockquote id="b399-20">“Sgt. Byrd: And I have not persuaded you in any way, is that correct?</blockquote>
<blockquote id="b399-21">“Mrs. P.: No, you have not.</blockquote>
<blockquote id="b399-22">“Sgt. Byrd: And, Mr. Prysock is that correct that I have done nothing to persuade you not to, to hire a lawyer or to go on with this?</blockquote>
<blockquote id="b399-23">“Mr. P.: That’s right.</blockquote>
<blockquote id="b400-6"><page-number citation-index="1" label="358">*358</page-number>“Sgt. Byrd: Okay, everything we’re doing here is strictly in accordance with Randall and yourselves, is that correct?</blockquote>
<blockquote id="b400-7">“Mr. P.: That is correct.</blockquote>
<blockquote id="b400-8">“Sgt. Byrd: Okay. Uh, all right, Randy, I can’t remember where I left off, I think I asked you, uh, with your legal rights in mind, do you wish to talk to me at this time? This is with everything I told you, all your legal rights, your right to an attorney, your right, and your right to remain silent, and all these, I mean do you wish to talk to me at this time about the case?</blockquote>
<blockquote id="b400-9">“Randall P.: Yes.” App. A to Pet. for Cert, iii-iv.</blockquote>
</footnote>
<footnote label="2">
<p id="b401-7"> Contrary to respondent’s suggestion, it is clear that the decision below was based on federal law. The Court of Appeal stated that it was reversing and ordering a new trial “because of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>error.” <em>Id., </em>at 4.</p>
</footnote>
<footnote label="3">
<p id="b403-6"> The dissent, arguing that the Court of Appeal opinion is unfairly criticized as requiring mimicking of <em>Miranda, post, </em>at 365-366, ignores substantial portions of the opinion below and substitutes arguments of its own for those articulated by the Court of Appeal. For example, the dissent makes no mention of the lower court’s stress on the “precise requirements” of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>or its “rigidity” in this area, and ignores the portion of the opinion in which the court quotes from <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and then criticizes the officer for not repeating the exact language in advising respondent of his rights. See App. A to Pet. for Cert. 12-14. The Court of Appeal did conclude that respondent was not advised of his right to appointed counsel prior to and during interrogation, but this was <em>because </em>the officer did not parrot the language of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>The more substantive reasons suggested by the dissent are implausible. The reference to “appointed” counsel has never been considered as suggesting that the availability of counsel was postponed, and Mrs. Prysock’s off-the-record conversation was occasioned by her fear that waiving the right to counsel at interrogation <page-number citation-index="1" label="362">*362</page-number>would occasion a waiver of the right to counsel later in court, Ápp. A to Pet. for Cert. 11, clearly indicating that the officer conveyed the right to counsel at interrogation.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/California v. Trombetta.md  (`case`, 5 assertions)

### content_page

```
---
title: California v. Trombetta
type: case
citation: "467 U.S. 479 (1984)"
parallel_cite: "104 S. Ct. 2528; 81 L. Ed. 2d 413; 52 U.S.L.W. 4744"
neutral_cite: 1984 U.S. LEXIS 103
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-06-11
docket: No. 83-305
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
  opinion_url: "https://www.courtlistener.com/opinion/111206/california-v-trombetta/"
  cluster_id: 111206
  opinion_id: null
  identity_checked: true
lake:
  record_id: California v. Trombetta
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Brady and Giglio]]"
    role: Anchor
related:
  - "[[Brady and Giglio]]"
  - "[[Arizona v. Youngblood]]"
tags:
  - case
  - fourteenth-amendment
  - due-process
  - preservation-of-evidence
  - brady
  - dui
holding: "The Due Process Clause does not require law enforcement to preserve breath samples taken from suspected drunk drivers, because the constitutional duty to preserve evidence reaches only evidence whose exculpatory value was apparent before it was destroyed and that the defendant cannot replace by other reasonably available means."
aliases:
  - California v. Trombetta
  - "California v. Trombetta (1984)"
---

# California v. Trombetta

*467 U.S. 479 (1984)* (No. 83-305) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 111206 → combined opinion 111206 (Marshall, J.; 467 U.S. 479, decided June 11, 1984). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*489`). S9 promotes. -->

## Background
The respondents were arrested for driving while intoxicated after failing breath-analysis tests on an Intoxilyzer machine. Under California's testing practices, the breath samples themselves were not preserved after the machine produced its blood-alcohol reading. The respondents moved to suppress the test results, arguing that the State's failure to save the samples — which they might have tested independently — deprived them of potentially [[Brady and Giglio|exculpatory]] evidence in violation of due process. The California Court of Appeal agreed and held the results inadmissible.

## Issue
Whether the Due Process Clause requires the police to preserve breath samples of suspected drunk drivers so that defendants may subject them to independent testing.

## Rule
The Court held that whatever duty the Constitution imposes to preserve evidence is a limited one, defined by two requirements the lost evidence must meet: "evidence must both possess an exculpatory value that was apparent before the evidence was destroyed, and be of such a nature that the defendant would be unable to obtain comparable evidence by other reasonably available means." — 467 U.S. at 489. ^pin-489

## Application
Breath samples satisfied neither requirement. Given the Intoxilyzer's demonstrated and certified accuracy, the chance that a preserved sample would have been [[Brady and Giglio|exculpatory]] was "extremely low" — so any [[Brady and Giglio|exculpatory]] value was speculative, not apparent. And defendants had other, comparable ways to challenge a reading: inspecting the machine's calibration and operation, and cross-examining the officer who administered the test. Because the samples were neither apparently [[Brady and Giglio|exculpatory]] nor irreplaceable, the State's failure to preserve them did not offend due process.

## Conclusion
The judgment was **reversed**. Marshall, J., delivered the opinion of a unanimous Court; O'Connor, J., filed a [[Common Legal Terms#concurring-opinion|concurring opinion]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Trombetta* fixes the duty-to-preserve standard for evidence of **apparent [[Brady and Giglio|exculpatory]] value**. Its companion rule — for evidence that is only **potentially useful**, where the defendant must instead prove **bad faith** — arrived four years later in *[[Arizona v. Youngblood]]* (1988). Teach the two as a pair: *Trombetta* sets the materiality gate; *[[Arizona v. Youngblood|Youngblood]]* supplies the bad-faith gate for everything short of apparent [[Brady and Giglio|exculpatory]] value.

## Appears on
- [[Brady and Giglio]] — *Anchor*

## Sources
- [*California v. Trombetta*, 467 U.S. 479 (1984)](https://www.courtlistener.com/opinion/111206/california-v-trombetta/) — pinpoint: 489 (Marshall, J., for the Court; the CL opinion text carries the reporter star `*489` immediately before the two-part standard). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "efa543d44f33d4b9", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "467 U.S. 479 (1984)", "court": "U.S. Supreme Court", "neutral_cite": "1984 U.S. LEXIS 103", "official_citation_present": true, "parallel_cite": "104 S. Ct. 2528; 81 L. Ed. 2d 413; 52 U.S.L.W. 4744", "title": "California v. Trombetta", "year": "1984"}}
{"assertion_id": "912576b3d3cb9b71", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Anchor", "title": "California v. Trombetta"}}
{"assertion_id": "c1e0ab70a26b6647", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Due Process Clause does not require law enforcement to preserve breath samples taken from suspected drunk drivers, because the constitutional duty to preserve evidence reaches only evidence whose exculpatory value was apparent before it was destroyed and that the defendant cannot replace by other reasonably available means.", "title": "California v. Trombetta"}}
{"assertion_id": "9a244feaac8aae25", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "California v. Trombetta", "varies_by_point": "false"}}
{"assertion_id": "a5a5fa051f1028f6", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "California v. Trombetta"}}
```

### lake record — California v. Trombetta

```json
{
  "schema_version": "s2.v1",
  "record_id": "California v. Trombetta",
  "status": "under_review",
  "identity": {
    "case_name": "California v. Trombetta",
    "case_name_short": "Trombetta",
    "case_name_full": "CALIFORNIA v. TROMBETTA Et Al.",
    "input_case_name": "California v. Trombetta",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-06-11",
    "year": 1984,
    "docket": "No. 83-305",
    "cluster_id": 111206,
    "lead_opinion_id": 9429651,
    "sibling_ids": [],
    "absolute_url": "/opinion/111206/california-v-trombetta/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "467 U.S. 479",
      "volume": "467",
      "reporter": "U.S.",
      "page": "479",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 2528",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2528",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 L. Ed. 2d 413",
        "volume": "81",
        "reporter": "L. Ed. 2d",
        "page": "413",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4744",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4744",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 103",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "103",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "467 U.S. 479",
        "volume": "467",
        "reporter": "U.S.",
        "page": "479",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 2528",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2528",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 L. Ed. 2d 413",
        "volume": "81",
        "reporter": "L. Ed. 2d",
        "page": "413",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 103",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "103",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4744",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4744",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "467 U.S. 479",
    "official_selection": {
      "court_class": "scotus",
      "selected": "467 U.S. 479",
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
    "date_created": "2026-07-06T13:45:34Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:45:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:45:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "california-v-trombetta--111206",
      "to_record_id": "California v. Trombetta",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — California v. Trombetta

```
<opinion type="majority">
<author id="b538-10">Justice Marshall</author>
<p id="AHv">delivered the opinion of the Court.</p>
<p id="b538-11">The Due Process Clause of the Fourteenth Amendment requires the State to disclose to criminal defendants favorable evidence that is material either to guilt or to punishment. <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">427 U. S. 97</a></span> (1976); <em>Brady </em>v. <page-number citation-index="1" label="481">*481</page-number><em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963). This case raises the question whether the Fourteenth Amendment also demands that the State preserve potentially exculpatory evidence on behalf of defendants. In particular, the question presented is whether the Due Process Clause requires law enforcement agencies to preserve breath samples of suspected drunken drivers in order for the results of breath-analysis tests to be admissible in criminal prosecutions.</p>
<p id="b539-8">f — I</p>
<p id="b539-3">The Omicron Intoxilyzer (Intoxilyzer) is a device used in California to measure the concentration of alcohol in the blood of motorists suspected of driving while under the influence of intoxicating liquor.<footnotemark>1</footnotemark> The Intoxilyzer analyzes the suspect’s breath. To operate the device, law enforcement officers follow these procedures:</p>
<blockquote id="b539-4">“Prior to any test, the device is purged by pumping clean air through it until readings of 0.00 are obtained. The breath test requires a sample of‘alveolar’ (deep lung) air; to assure that such a sample is obtained, the subject is required to blow air into the intoxilyzer at a constant pressure for a period of several seconds. A breath sample is captured in the intoxilyzer’s chamber and infrared light is used to sense the alcohol level. Two samples are taken, and the result of each is indicated on a printout card. The two tests must register within 0.02 of each other in order to be admissible in court. After each test, the chamber is purged with clean air and then <page-number citation-index="1" label="482">*482</page-number>checked for a reading of zero alcohol. The machine is calibrated weekly, and the calibration results, as well as a portion of the calibration samples, are available to the defendant.” <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#141" aria-description="Citation for case: People v. Trombetta">142 Cal. App. 3d 138, 141-142</a></span>, <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#321" aria-description="Citation for case: People v. Trombetta">190 Cal. Rptr. 319, 321</a></span> (1983) (citations omitted).</blockquote>
<p id="b540-5">In unrelated incidents in 1980 and 1981, each of the respondents in this case was stopped on suspicion of drunken driving on California highways. Each respondent submitted to an Intoxilyzer test.<footnotemark>2</footnotemark> Each respondent registered a blood-alcohol concentration substantially higher than 0.10 percent. Under California law at that time, drivers with higher than 0.10 percent blood-alcohol concentrations were presumed to be intoxicated. Cal. Veh. Code Ann. § 23126(a)(3) (West 1971) (amended 1981). Respondents were all charged with driving while intoxicated in violation of Cal. Veh. Code Ann. §23102 (West 1971) (amended 1981).</p>
<p id="b540-6">Prior to trial in Municipal Court, each respondent filed a motion to suppress the Intoxilyzer test results on the ground that the arresting officers had failed to preserve samples of respondents' breath. Although preservation of breath samples is technically feasible,<footnotemark>3</footnotemark> California law enforcement offi<page-number citation-index="1" label="483">*483</page-number>cers do not ordinarily preserve breath samples, and made no effort to do so in these cases. Respondents each claimed that, had a breath sample been preserved, he would have been able to impeach the incriminating Intoxilyzer results. All of respondents’ motions to suppress were denied. Respondents Ward and Berry then submitted their cases on the police records and were convicted. Ward and Berry subsequently petitioned the California Court of Appeal for writs of habeas corpus. Respondents Trombetta and Cox did not submit to trial. They sought direct appeal from the Municipal Court orders, and their appeals were eventually transferred to the Court of Appeal to be consolidated with the Ward and Berry petitions.<footnotemark>4</footnotemark></p>
<p id="b541-5">The California Court of Appeal ruled in favor of respondents. After implicitly accepting that breath samples would be useful to respondents’ defenses, the court reviewed the available technologies and determined that the arresting officers had the capacity to preserve breath samples for respondents. <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#141" aria-description="Citation for case: People v. Trombetta">142 Cal. App. 3d, at 141-142</a></span>, <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#320" aria-description="Citation for case: People v. Trombetta">190 Cal. Rptr., at 320-321</a></span>. Relying heavily on the California Supreme Court’s decision in <em>People </em>v. <em>Hitch, </em><span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/" aria-description="Citation for case: People v. Hitch">12 Cal. 3d 641</a></span>, <span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/" aria-description="Citation for case: People v. Hitch">527 P. 2d 361</a></span> (1974), the Court of Appeal concluded: “Due process demands simply that where evidence is collected by the state, as it is with the intoxilyzer, or any other breath testing device, law enforcement agencies must establish and follow rigorous and <page-number citation-index="1" label="484">*484</page-number>systematic procedures to preserve the captured evidence or its equivalent for the use of the defendant.” <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#144" aria-description="Citation for case: People v. Trombetta">142 Cal. App. 3d, at 144</a></span>, <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#323" aria-description="Citation for case: People v. Trombetta">190 Cal. Rptr., at 323</a></span>.<footnotemark>5</footnotemark> The court granted respondents Ward and Berry new trials, and ordered that the Intoxilyzer results not be admitted as evidence against the other two respondents. The State unsuccessfully petitioned for certiorari in the California Supreme Court, and then petitioned for review in this Court. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./464/1037/">464 U. S. 1037</a></span> (1984), and now reverse.</p>
<p id="b543-4"><page-number citation-index="1" label="485">*485</page-number>II</p>
<p id="b543-5">Under the Due Process Clause of the Fourteenth Amendment, criminal prosecutions must comport with prevailing notions of fundamental fairness. We have long interpreted this standard of fairness to require that criminal defendants be afforded a meaningful opportunity to present a complete defense. To safeguard that right, the Court has developed “what might loosely be called the area of constitutionally guaranteed access to evidence.” <em>United States </em>v. <em>Valenzuela-Bernal, </em><span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/#867" aria-description="Citation for case: United States v. Valenzuela-Bernal">458 U. S. 858, 867</a></span> (1982). Taken together, this group of constitutional privileges delivers exculpatory evidence into the hands of the accused, thereby protecting the innocent from erroneous conviction and ensuring the integrity of our criminal justice system.</p>
<p id="b543-6">The most rudimentary of the access-to-evidence cases impose upon the prosecution a constitutional obligation to report to the defendant and to the trial court whenever government witnesses lie under oath. <em>Napue </em>v. <em>Illinois, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264, 269-272</a></span> (1959); see also <em>Mooney </em>v. <em>Holohan, </em><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103</a></span> (1935). But criminal defendants are entitled to much more than protection against perjury. A defendant has a constitutionally protected privilege to request and obtain from the prosecution evidence that is either material to the guilt of the defendant or relevant to the punishment to be imposed. <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>. Even in the absence of a specific request, the prosecution has a constitutional duty to turn over exculpatory evidence that would raise a reasonable doubt about the defendant’s guilt. <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#112" aria-description="Citation for case: United States v. Agurs">427 U. S., at 112</a></span>. The prosecution must also reveal the contents of plea agreements with key government witnesses, see <em>Giglio </em>v. <em>United States, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">405 U. S. 150</a></span> (1972), and under some circumstances may be required to disclose the identity of undercover informants who possess evidence critical to the defense, <em>Roviaro </em>v. <em>United States, </em><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">353 U. S. 53</a></span> (1957).</p>
<p id="b544-4"><page-number citation-index="1" label="486">*486</page-number>Less clear from our access-to-evidence cases is the extent to which the Due Process Clause imposes on the government the additional responsibility of guaranteeing criminal defendants access to exculpatory evidence beyond the government’s possession. On a few occasions, we have suggested that the Federal Government might transgress constitutional limitations if it exercised its sovereign powers so as to hamper a criminal defendant’s preparation for trial. For instance, in <em>United States </em>v. <em>Marion, </em><span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#324" aria-description="Citation for case: United States v. Marion">404 U. S. 307, 324</a></span> (1971), and in <em>United States </em>v. <em>Lovasco, </em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#795" aria-description="Citation for case: United States v. Lovasco">431 U. S. 783, 795, n. 17</a></span> (1977), we intimated that a due process violation might occur if the Government delayed an indictment for so long that the defendant’s ability to mount an effective defense was impaired. Similarly, in <em>United States </em>v. <em><span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/" aria-description="Citation for case: United States v. Valenzuela-Bernal">Valenzuela-Bernal, supra,</a></span> </em>we acknowledged that the Government could offend the Due Process Clause of the Fifth Amendment if, by deporting potential witnesses, it diminished a defendant’s opportunity to put on an effective defense.<footnotemark>6</footnotemark> <span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/#873" aria-description="Citation for case: United States v. Valenzuela-Bernal">458 U. S., at 873</a></span>.</p>
<p id="b544-5">We have, however, never squarely addressed the government’s duty to take affirmative steps to preserve evidence on behalf of criminal defendants. The absence of doctrinal development in this area reflects, in part, the difficulty of developing rules to deal with evidence destroyed through prosecutorial neglect or oversight. Whenever potentially exculpatory evidence is permanently lost, courts face the treacherous task of divining the import of materials whose contents are unknown and, very often, disputed. Cf. <em>United States </em>v. <span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/#870" aria-description="Citation for case: United States v. Valenzuela-Bernal"><em>Valenzuela-Bernal, supra, </em>at 870</a></span>. Moreover, fashioning remedies for the illegal destruction of evidence can pose troubling choices. In nondisclosure cases, a court can <page-number citation-index="1" label="487">*487</page-number>grant the defendant a new trial at which the previously suppressed evidence may be introduced. But when evidence has been destroyed in violation of the Constitution, the court must choose between barring further prosecution or suppressing — as the California Court of Appeal did in this case— the State’s most probative evidence. '</p>
<p id="b545-5">One case in which we have discussed due process constraints on the Government’s failure to preserve potentially exculpatory evidence is <em>Killian </em>v. <em>United States, </em><span class="citation" data-id="9422314"><a href="/opinion/106310/killian-v-united-states/" aria-description="Citation for case: Killian v. United States">368 U. S. 231</a></span> (1961). In <em><span class="citation" data-id="9422314"><a href="/opinion/106310/killian-v-united-states/" aria-description="Citation for case: Killian v. United States">Killian</a></span>, </em>the petitioner had been convicted of giving false testimony in violation of <span class="citation no-link">18 U. S. C. § 1001</span>. A key element of the Government’s case was an investigatory report prepared by the Federal Bureau of Investigation. The Solicitor General conceded that, prior to petitioner’s trial, the F. B. I. agents who prepared the investigatory report destroyed the preliminary, notes they had made while interviewing witnesses. The petitioner argued that these notes would have been helpful to his defense and that the agents had violated the Due Process Clause by destroying this exculpatory evidence. While not denying that the notes might have contributed to the petitioner’s defense, the Court ruled that their destruction did not rise to the level of constitutional violation:</p>
<blockquote id="b545-6">“If the agents’ notes . . . were made only for the purpose of transferring the data thereon . . . , and if, having served that purpose, they were destroyed by the agents in good faith and in accord with their normal practices, it would be clear that their destruction did not constitute an impermissible destruction of evidence nor deprive petitioner of any right.” <span class="citation no-link"><em>Id., </em>at 242</span>.</blockquote>
<p id="b545-7">In many respects the instant case is reminiscent of <em>Killian </em>v. <em>United States. </em>To the extent that respondents’ breath samples came into the possession of California authorities, it was for the limited purpose of providing raw data to the <page-number citation-index="1" label="488">*488</page-number>Intoxilyzer.<footnotemark>7</footnotemark> The evidence to be presented at trial was not the breath itself but rather the Intoxilyzer results obtained from the breath samples. As the petitioner in <em><span class="citation" data-id="9422314"><a href="/opinion/106310/killian-v-united-states/" aria-description="Citation for case: Killian v. United States">Killian</a></span> </em>wanted the agents’ notes hi order to impeach their final reports, respondents here seek the breath samples in order to challenge incriminating tests results produced with the Intoxilyzer.</p>
<p id="b546-4">Given our precedents in this area, we cannot agree with the California Court of Appeal that the State’s failure to retain breath samples for respondents constitutes a violation of the Federal Constitution. To begin with, California authorities in this case did not destroy respondents’ breath samples in a calculated effort to circumvent the disclosure requirements established by <em>Brady </em>v. <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Maryland</a></span> </em>and its progeny. In failing to preserve breath samples for respondents, the officers here were acting “in good faith and in accord with their normal practice.” <em>Killian </em>v. <em>United States, supra, </em>at 242. The record contains no allegation of official animus towards respondents or of a conscious effort to suppress exculpatory evidence.</p>
<p id="b546-5">More importantly, California’s policy of not preserving breath samples is without constitutional defect. Whatever duty the Constitution imposes on the States to preserve evidence, that duty must be limited to evidence that might be expected to play a significant role in the suspect’s defense.<footnotemark>8</footnotemark> <page-number citation-index="1" label="489">*489</page-number>To meet this standard of constitutional materiality, see <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#109" aria-description="Citation for case: United States v. Agurs">427 U. S., at 109-110</a></span>, evidence must both possess an exculpatory value that was apparent before the evidence was destroyed, and be of such a nature that the defendant would be unable to obtain comparable evidence by other reasonably available means. Neither of these conditions is met on the facts of this case.</p>
<p id="b547-5">Although the preservation of breath samples might conceivably have contributed to respondents’ defenses, a dispassionate review of the Intoxilyzer and the California testing procedures can only lead one to conclude that the chances are extremely low that preserved samples would have been exculpatory. The accuracy of the Intoxilyzer has been reviewed and certified by the California Department of Health.<footnotemark>9</footnotemark> To protect suspects against machine malfunctions, the Department has developed test procedures that include two independent measurements (which must be closely correlated for the results to be admissible) bracketed by blank runs designed to ensure that the machine is purged of alcohol traces from previous tests. See <em>supra, </em>at 481-482. In all but a tiny fraction of cases, preserved breath samples would simply confirm the Intoxilyzer’s determination that the defendant had a high level of blood-alcohol concentration at the time of the test. Once the Intoxilyzer indicated that respondents were legally drunk, breath samples were much more likely to provide inculpatory than exculpatory evidence.<footnotemark>10</footnotemark></p>
<p id="b548-4"><page-number citation-index="1" label="490">*490</page-number>Even if one were to assume that the Intoxilyzer results in this case were inaccurate and that breath samples might therefore have been exculpatory, it does not follow that respondents were without alternative means of demonstrating their innocence. Respondents and <em>amici </em>have identified only a limited number of ways in which an Intoxilyzer might malfunction: faulty calibration, extraneous interference with machine measurements, and operator error. See Brief for Respondents 32-34; Brief for California Public Defender’s Association et al. as <em>Amici Curiae </em>25-40. Respondents were perfectly capable of raising these issues without resort to preserved breath samples. To protect against faulty calibration, California gives drunken driving defendants the opportunity to inspect the machine used to test their breath as well as that machine’s weekly calibration results and the breath samples used in the calibrations. See <em>supra, </em>at 481-482. Respondents could have utilized these data to impeach the machine’s reliability. As to improper measurements, the parties have identified only two sources capable of interfering with test results: radio waves and chemicals that appear in the blood of those who are dieting. For defendants whose test results might have been affected by either of these factors, it remains possible to introduce at trial evidence demonstrating that the defendant was dieting at the time of the test or that the test was conducted near a source of radio waves. Finally, as to operator error, the defendant retains the right to cross-examine the law enforcement officer who administered the Intoxilyzer test, and to attempt to raise doubts in the mind of the factfinder whether the test was properly administered.<footnotemark>11</footnotemark></p>
<p id="ABc"><page-number citation-index="1" label="491">*491</page-number>H-1 I — H</p>
<p id="Avg">We conclude, therefore, that the Due Process Clause of the Fourteenth Amendment does not require that law enforcement agencies preserve breath samples in order to introduce the results of breath-analysis tests at trial.<footnotemark>12</footnotemark> Accordingly, the judgment of the California Court of Appeal is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="Abc">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b539-5"> Law enforcement agencies in California are obliged to use breath-analysis equipment that has been approved by the State’s Department of Health. See 17 <span class="citation no-link">Cal. Admin. Code § 1221</span> (1976). The Department has approved a number of blood-alcohol testing devices employing a variety of technologies, see List of Instruments and Related Accessories Approved for Breath Alcohol Analysis (Dec. 20, 1979), reprinted in App. 238-247, of which the Omicron Intoxilyzer is the most popular model, see Brief for Petitioner 6, n. 6.</p>
</footnote>
<footnote label="2">
<p id="b540-7"> Under California law, drunken driving suspects are given the choice of having their blood-alcohol concentraton determined by either a blood test, a urine test, or a breath test. Cal. Veh. Code Ann. § 13353 (West 1971 and Supp. 1984). Suspects who refuse to submit to any test are liable to have their driving licenses suspended. <em>Ibid.</em></p>
</footnote>
<footnote label="3">
<p id="b540-8"> The California Department of Health has approved a device, known as an Intoximeter Field Crimper-Indium Tube Encapsulation Kit (Kit), which officers can use to preserve breath samples. App. 247. To use the Kit, a suspect must breathe directly into an indium tube, which preserves samples in three separate chambers. See <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#142" aria-description="Citation for case: People v. Trombetta">142 Cal. App. 3d 138, 142</a></span>, <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#321" aria-description="Citation for case: People v. Trombetta">190 Cal. Rptr. 319, 321</a></span> (1983). The breath trapped in each chamber can later be used to determine the suspect’s blood-alcohol concentration through the use of a laboratory instrument known as a Gas Chromatograph Intoxi-meter, which has also been approved by the California Department of Health. App. 242-243. Because the suspect must breathe directly into the indium tube, the Kit cannot be used to preserve the same breath sample used in an Intoxilyzer test. See, <em>supra, </em>at 481-482. Other devices, <page-number citation-index="1" label="483">*483</page-number>similar in function to the Kit, can be attached to an Intoxilyzer and used to collect the air that the Intoxilyzer purges, see Brief for Respondents 18-19, but none of these devices has yet received approval from the California Department of Health, see Reply Brief for Petitioner 3-4.</p>
</footnote>
<footnote label="4">
<p id="b541-9"> The California Court of Appeal expressed some doubt whether respondents Trombetta and Cox were entitled to appeal their suppression orders and ultimately ordered that their appeals be dismissed. <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#140" aria-description="Citation for case: People v. Trombetta">142 Cal. App. 3d, at 140, 143</a></span>, <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#320" aria-description="Citation for case: People v. Trombetta">190 Cal. Rptr., at 320, 323</a></span>. The court, however, ruled on the merits of their claims and thereby exercised jurisdiction over their appeals. <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#144" aria-description="Citation for case: People v. Trombetta"><em>Id., </em>at 144</a></span>, <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#323" aria-description="Citation for case: People v. Trombetta">190 Cal. Rptr., at 323</a></span>. As to Trombetta and Cox, the Court of Appeal decision was comparable to a judgment affirming a suppression order, which is reviewable in this Court under <span class="citation no-link">28 U. S. C. § 1257</span>(3). Cf., <em>e. g., Michigan </em>v. <em>Clifford, </em><span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/" aria-description="Citation for case: Michigan v. Clifford">464 U. S. 287</a></span> (1984).</p>
</footnote>
<footnote label="5">
<p id="b542-5"> <em>People </em>v. <em><span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/" aria-description="Citation for case: People v. Hitch">Hitch</a></span> </em>involved another device used to measure blood-alcohol concentrations. With that device, a suspect’s breath bubbles through a glass ampoule containing special chemicals that change colors depending on the amount of alcohol in the suspect’s blood. <span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/#644" aria-description="Citation for case: People v. Hitch">12 Cal. 3d, at 644</a></span>, <span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/#363" aria-description="Citation for case: People v. Hitch">527 P. 2d, at 363-364</a></span>. In keeping with California procedures, law enforcement officials in <em><span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/" aria-description="Citation for case: People v. Hitch">Hitch</a></span> </em>discarded the ampoule after they had completed their testing, even though the ampoule might have been saved for retesting by the defendant. Relying on this Court’s decisions in <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), and <em>Giglio </em>v. <em>United States, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#153" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 153-154</a></span> (1972), the California Supreme Court concluded that the Due Process Clause is implicated when a State intentionally destroys evidence that might have proved favorable to a criminal defendant. <span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/#645" aria-description="Citation for case: People v. Hitch">12 Cal. 3d, at 645-650</a></span>, <span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/#364" aria-description="Citation for case: People v. Hitch">527 P. 2d, at 364-370</a></span>. The <em><span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/" aria-description="Citation for case: People v. Hitch">Hitch</a></span> </em>decision was noteworthy in that it extrapolated from <em>Brady’s </em>disclosure requirement an additional constitutional duty on the part of prosecutors to preserve potentially exculpatory evidence. See Note, The Right to Independent Testing: A New Hitch in the Preservation of Evidence Doctrine, <span class="citation no-link">75 Colum. L. Rev. 1355</span>, 1364-1368 (1975); cf. <em>United States </em>v. <em>Bryant, </em>142 U. S. App. D. C. 132, 141, <span class="citation" data-id="9456634"><a href="/opinion/295318/united-states-v-carlton-e-bryant-united-states-of-america-v-william-e/#651" aria-description="Citation for case: United States v. Carlton E. Bryant, United States of...">439 F. 2d 642, 651</a></span> (1971) (Wright, J.) (Government must make “ ‘earnest efforts’ to pre serve crucial materials and to find them once a discovery request is made”).</p>
<p id="b542-6">For a number of years, there was uncertainty whether the California courts would extend the <em><span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/" aria-description="Citation for case: People v. Hitch">Hitch</a></span> </em>decision to the Intoxilyzer. In <em>People </em>v. <em>Miller, </em><span class="citation" data-id="2140951"><a href="/opinion/2140951/people-v-miller/" aria-description="Citation for case: People v. Miller">52 Cal. App. 3d 666</a></span>, <span class="citation" data-id="2140951"><a href="/opinion/2140951/people-v-miller/" aria-description="Citation for case: People v. Miller">125 Cal. Rptr. 341</a></span> (1975), a Court of Appeal panel refused to extend <em><span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/" aria-description="Citation for case: People v. Hitch">Hitch</a></span> </em>because the Intoxilyzer does not reduce breath samples to a preservable form comparable to the ampoules created with the device involved in <em><span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/" aria-description="Citation for case: People v. Hitch">Hitch</a></span>. </em>The Court of Appeal in <em>Trombetta </em>declined to follow <em><span class="citation" data-id="2140951"><a href="/opinion/2140951/people-v-miller/" aria-description="Citation for case: People v. Miller">Miller</a></span>, </em>and reasoned that as long as there were other methods of preserving specimens (such as the Indium Tube Kit, see n. 3, <em>supra), </em>the State was obliged to preserve a breath sample equivalent to the one used in the Intoxilyzer. <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#143" aria-description="Citation for case: People v. Trombetta">142 Cal. App. 3d, at 143-144</a></span>, <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#322" aria-description="Citation for case: People v. Trombetta">190 Cal. Rptr., at 322-323</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b544-6"> In related cases arising under the Sixth and Fourteenth Amendments, we have recognized that criminal defendants are entitled to call witnesses on their own behalf and to cross-examine witnesses who have testified on the government’s behalf. See <em>Davis </em>v. <em>Alaska, </em><span class="citation" data-id="9425616"><a href="/opinion/108974/davis-v-alaska/" aria-description="Citation for case: Davis v. Alaska">415 U. S. 308</a></span> (1974); <em>Washington </em>v. <em>Texas, </em><span class="citation" data-id="9423455"><a href="/opinion/107481/washington-v-texas/" aria-description="Citation for case: Washington v. Texas">388 U. S. 14</a></span> (1967).</p>
</footnote>
<footnote label="7">
<p id="b546-6"> We accept the California Court of Appeal’s conclusion that the Intox-ilyzer procedure brought respondents’ breath samples into the possession of California officials. The capacity to preserve breath samples is equivalent to the actual possession of samples. See n. 5, <em>supra.</em></p>
</footnote>
<footnote label="8">
<p id="b546-7"> In our prosecutorial disclosure cases, we have imposed a similar requirement of materiality, <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">427 U. S. 97</a></span> (1976), and have rejected the notion that a “prosecutor has a constitutional duty routinely to deliver his entire file to defense counsel.” <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#111" aria-description="Citation for case: United States v. Agurs"><em>Id., </em>at 111</a></span>; see also <em>Moore </em>v. <em>Illinois, </em><span class="citation" data-id="9425027"><a href="/opinion/108613/moore-v-illinois/#795" aria-description="Citation for case: Moore v. Illinois">408 U. S. 786, 795</a></span> (1972) (“We know of no constitutional requirement that the prosecution make a complete and detailed accounting to the defense of all police investigatory work on a case”).</p>
</footnote>
<footnote label="9">
<p id="b547-6"> The Intoxilyzer has also passed accuracy requirements established by the National Highway Traffic Safety Administration of the Department of Transportation. See <span class="citation no-link">38 Fed. Reg. 30459</span> (1973); A. Flores, Results of the First Semi-Annual Qualification Testing of Devices to Measure Breath Alcohol 10 (Dept, of Transportation 1975).</p>
</footnote>
<footnote label="10">
<p id="b547-7"> The materiality of breath samples is directly related to the reliability of the Intoxilyzer itself. The degree to which preserved samples are material depends on how reliable the Intoxilyzer is. This correlation suggests that a more direct constitutional attack might be made on the sufficiency of the evidence underlying the State’s case. After all, if the Intoxilyzer were <page-number citation-index="1" label="490">*490</page-number>truly prone to erroneous readings, then Intoxilyzer results without more might be insufficient to establish guilt beyond a reasonable doubt. <em>Jackson </em>v. <em>Virginia, </em><span class="citation" data-id="9427680"><a href="/opinion/110138/jackson-v-virginia/" aria-description="Citation for case: Jackson v. Virginia">443 U. S. 307</a></span> (1979).</p>
</footnote>
<footnote label="11">
<p id="b548-6"> Respondents could also have protected themselves from erroneous on-the-scene testing by electing to submit to urine or blood tests, see n. 2, <em>supra, </em>because the State automatically would have preserved urine and <page-number citation-index="1" label="491">*491</page-number>blood samples for retesting by respondents. Respondents, however, were not informed of the difference between the various testing procedures when they were asked to select among the three available methods of testing blood-alcohol concentrations. But see Cal. Veh. Code Ann. § 13353.5 (West 1971) (enacted in 1983) (requiring suspects to be informed that samples will be retained only in urine and blood tests). To the extent that this and other access-to-evidence cases turn on the underlying fairness of governmental procedures, it would be anomalous to permit the State to justify its actions by relying on procedural alternatives that were available, but unknown to the defendant. Similarly, it is irrelevant to our inquiry that California permits an accused drunken driver to have a second blood-alcohol test conducted by independent experts, since there is no evidence on this record that respondents were aware of this alternative.</p>
</footnote>
<footnote label="12">
<p id="AdNB"> State courts and legislatures, of course, remain free to adopt more rigorous safeguards governing the admissibility of scientific evidence than those imposed by the Federal Constitution. See, <em>e. g., Lauderdale </em>v. <em>State, </em><span class="citation" data-id="1351919"><a href="/opinion/1351919/lauderdale-v-state/" aria-description="Citation for case: Lauderdale v. State">548 P. 2d 376</a></span> (Alaska 1976); <em>City of Lodi </em>v. <em>Hine, </em><span class="citation" data-id="1800375"><a href="/opinion/1800375/city-of-lodi-v-hine/" aria-description="Citation for case: City of Lodi v. Hine">107 Wis. 2d 118</a></span>, <span class="citation" data-id="1800375"><a href="/opinion/1800375/city-of-lodi-v-hine/" aria-description="Citation for case: City of Lodi v. Hine">318 N. W. 2d 383</a></span> (1982).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Camara v. Municipal Court.md  (`case`, 5 assertions)

### content_page

```
---
title: "Camara v. Municipal Court"
type: case
citation: "387 U.S. 523 (1967)"
parallel_cite: "87 S. Ct. 1727; 18 L. Ed. 2d 930"
neutral_cite: 1967 U.S. LEXIS 1254
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-06-05
docket: 92
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-06-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Camara v. Municipal Court
  varies_by_point: false
  scope_note: "Overruled Frank v. Maryland; remains the foundational administrative-warrant case."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/"
  cluster_id: 107473
  opinion_id: 107473
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Anchor"
related: ["[[See v. City of Seattle]]", "[[City of Los Angeles v. Patel]]", "[[New York v. Burger]]"]
aliases: ["Camara v. Municipal Court of City and County of San Francisco"]
tags: ["case", "fourth-amendment", "administrative-search", "inspection", "warrant"]
holding: "Administrative inspections of private property generally require a warrant, but it may be an \"area warrant\" issued on reasonable…"
lake:
  record_id: Camara v. Municipal Court
  status: under_review
  projected_at: 2026-07-06
---

# Camara v. Municipal Court

*387 U.S. 523 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A San Francisco housing inspector sought to enter Camara's residence for a routine code inspection without a warrant. Camara refused entry on three occasions and was criminally charged under the ordinance for refusing to permit the warrantless inspection. He challenged the constitutionality of compelling a warrantless administrative inspection.

## Issue
Whether administrative inspections of private property require a warrant, and on what showing of "probable cause" such a warrant may issue.

## Rule
Administrative inspections require a warrant procedure: "we hold that administrative searches of the kind at issue here are significant intrusions upon the interests protected by the Fourth Amendment, that such searches when authorized and conducted without a warrant procedure lack the traditional safeguards which the Fourth Amendment guarantees to the individual". — 387 U.S. at 534. ^pin-534

But probable cause for such a warrant can rest on reasonable area standards rather than individualized suspicion: "'probable cause' to issue a warrant to inspect must exist if reasonable legislative or administrative standards for conducting an area inspection are satisfied with respect to a particular dwelling." — *Id.* at 538. ^pin-538

## Application
Camara had a constitutional right to insist on a warrant before the housing inspection, so he could not be criminally punished for refusing a warrantless one. Because the inspection program's goals could be met through area warrants issued on reasonable administrative standards, requiring a warrant did not frustrate the program; the warrantless-inspection scheme could not be enforced against him.

## Conclusion
A warrant was required for the administrative inspection; Camara's conviction for refusing the warrantless inspection could not stand (overruling *Frank v. Maryland*).

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Camara* **overruled** *[[Frank v. Maryland]]*, was extended to commercial premises in [[See v. City of Seattle]], and its pre-compliance-review principle was applied in [[City of Los Angeles v. Patel]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Anchor*

## Sources
- *Camara v. Municipal Court*, 387 U.S. 523 (1967) — https://www.courtlistener.com/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/ — pinpoints: 534, 538.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "94d26715eb3b0f5a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "387 U.S. 523 (1967)", "court": "U.S. Supreme Court", "neutral_cite": "1967 U.S. LEXIS 1254", "official_citation_present": true, "parallel_cite": "87 S. Ct. 1727; 18 L. Ed. 2d 930", "title": "Camara v. Municipal Court", "year": "1967"}}
{"assertion_id": "70d521bc6c047d86", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key — Anchor", "title": "Camara v. Municipal Court"}}
{"assertion_id": "8810173adb747dea", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Administrative inspections of private property generally require a warrant, but it may be an \\\"area warrant\\\" issued on reasonable…", "title": "Camara v. Municipal Court"}}
{"assertion_id": "1f4675eebe8a1b37", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1967-06-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Camara v. Municipal Court", "field_i_validity": "good_law", "scope_note": "Overruled Frank v. Maryland; remains the foundational administrative-warrant case.", "title": "Camara v. Municipal Court", "varies_by_point": "false"}}
{"assertion_id": "f8e0f9411832584d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Camara v. Municipal Court"}}
```

### lake record — Camara v. Municipal Court

```json
{
  "schema_version": "s2.v1",
  "record_id": "Camara v. Municipal Court",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Camara v. Municipal Court of City and County of San Francisco",
    "case_name_short": "Camara",
    "case_name_full": "Camara v. Municipal Court of the City and County of San Francisco",
    "input_case_name": "Camara v. Municipal Court",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-06-05",
    "year": 1967,
    "docket": "92",
    "cluster_id": 107473,
    "lead_opinion_id": 107473,
    "sibling_ids": [
      107473
    ],
    "absolute_url": "/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "387 U.S. 523",
      "volume": "387",
      "reporter": "U.S.",
      "page": "523",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 1727",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1727",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 930",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "930",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 1254",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1254",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "387 U.S. 523",
        "volume": "387",
        "reporter": "U.S.",
        "page": "523",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 1727",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1727",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 930",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "930",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 1254",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1254",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "387 U.S. 523",
    "official_selection": {
      "court_class": "scotus",
      "selected": "387 U.S. 523",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-534",
      "page": null,
      "quote": "such a warrant may issue. ## Rule Administrative inspections require a warrant procedure:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-538",
      "page": null,
      "quote": "'probable cause' to issue a warrant to inspect must exist if reasonable legislative or administrative standards for conducting an area inspection are satisfied with respect to a particular dwelling.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-06-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Camara v. Municipal Court",
    "varies_by_point": false,
    "scope_note": "Overruled Frank v. Maryland; remains the foundational administrative-warrant case.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Grady",
          "cluster_id": 4649078,
          "cite": [
            "831 S.E.2d 542",
            "372 N.C. 509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. O'Donnell",
          "cluster_id": 4427767,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Ryan Mark Thompson",
          "cluster_id": 4311783,
          "cite": [
            "886 N.W.2d 224",
            "2016 Minn. LEXIS 656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane1_negative"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Simmons v. United States",
          "cluster_id": 107636,
          "cite": [
            "19 L. Ed. 2d 1247",
            "88 S. Ct. 967",
            "390 U.S. 377",
            "1968 U.S. LEXIS 2167"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brignoni-Ponce",
          "cluster_id": 109311,
          "cite": [
            "45 L. Ed. 2d 607",
            "95 S. Ct. 2574",
            "422 U.S. 873",
            "1975 U.S. LEXIS 10"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Mimms",
          "cluster_id": 109751,
          "cite": [
            "54 L. Ed. 2d 331",
            "98 S. Ct. 330",
            "434 U.S. 106",
            "1977 U.S. LEXIS 157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. De Bour",
          "cluster_id": 5682261,
          "cite": [
            "40 N.Y.2d 210",
            "386 N.Y.S.2d 375",
            "1976 N.Y. LEXIS 2873",
            "352 N.E.2d 562"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chadwick",
          "cluster_id": 109714,
          "cite": [
            "53 L. Ed. 2d 538",
            "97 S. Ct. 2476",
            "433 U.S. 1",
            "1977 U.S. LEXIS 133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cady v. Dombrowski",
          "cluster_id": 108850,
          "cite": [
            "37 L. Ed. 2d 706",
            "93 S. Ct. 2523",
            "413 U.S. 433",
            "1973 U.S. LEXIS 48"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Watson",
          "cluster_id": 109352,
          "cite": [
            "46 L. Ed. 2d 598",
            "96 S. Ct. 820",
            "423 U.S. 411",
            "1976 U.S. LEXIS 121"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107473) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDUyMTI0ODAwMDAwJnM9MzE2Nzk5OSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107473%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107473)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjM5JnM9MTEyNDcyJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107473%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107473)",
        "reviewed": 56,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 56,
        "triage_read": 0,
        "triage_snippet_classified": 56
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107473)",
    "indexed_citing_opinions": 2314,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107473,
        "count": 2314,
        "count_source": "search"
      }
    ],
    "citation_count": 3595,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/camara-v-municipal-court.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwNjI4NTUmcz0xMDI2NTcxNSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28107473%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107473,
        "cited_id": 95698,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 96230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 96902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 104239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 104766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 106109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 1306345,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 1334923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 2008391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 2049948,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 2062881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 2155771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 2305304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 2430498,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 2435050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 3620827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 3783238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 5521228,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 9442232,
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
    "date_created": "2026-07-04T23:26:45Z",
    "date_modified": "2026-07-06T07:29:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:26:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:26:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:28:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:26:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Camara v. Municipal Court

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b569-2">
<span citation-index="1" class="star-pagination" label="525"> 
   *525
   </span>
  Mr. Justice White
 </author>
<p id="AnHt">
  delivered the opinion of the Court.
 </p>
<p id="b569-3">
  In
  <em>
   Frank
  </em>
  v.
  <em>
   Maryland,
  </em>
  <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360</a></span>, this Court upheld, by a five-to-four vote, a state court conviction of a homeowner who refused to permit a municipal health inspector to enter and inspect his premises without a search warrant. In
  <em>
   Eaton
  </em>
  v.
  <em>
   Price,
  </em>
  <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">364 U. S. 263</a></span>, a similar conviction was affirmed by an equally divided Court. Since those closely divided decisions, more intensive efforts at all levels of government to contain and eliminate urban blight have led to increasing use of such inspection techniques, while numerous decisions of this Court have more fully defined the Fourth Amendment's effect on state and municipal action.
  <em>
   E. g., Mapp
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>;
  <em>
   Ker
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span>. In view of the growing nationwide importance of the problem, we noted probable jurisdiction in this case and in
  <em>
   See
  </em>
  v.
  <em>
   City of Seattle, post,
  </em>
  p. 541, to re-examine whether administrative inspection programs, as presently authorized and conducted, violate Fourth Amendment rights as those rights are enforced against the States through the Fourteenth Amendment. <span class="citation multiple-matches"><a href="/c/U.%20S./385/808/">385 U. S. 808</a></span>.
 </p>
<p id="b569-4">
  Appellant brought this action in a California Superior Court alleging that he was awaiting trial on a criminal charge of violating the San Francisco Housing Code by refusing to permit a warrantless inspection of his residence, and that a writ of prohibition should issue to the criminal court because the ordinance authorizing such inspections is unconstitutional on its face. The Superior Court denied the writ, the District Court of Appeal affirmed, and the Supreme Court of California denied a petition for hearing. Appellant properly raised and had considered by the California courts the federal constitutional questions he now presents to this Court.
 </p>
<p id="b569-5">
  Though there were no judicial findings of fact in this prohibition proceeding, we shall set forth the parties’ factual allegations. On November 6, 1963, an inspector
  <span citation-index="1" class="star-pagination" label="526"> 
   *526
   </span>
  of the Division of Housing Inspection of the San Francisco Department of Public Health entered an apartment building to make a routine annual inspection for possible violations of the city's Housing Code.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The building’s manager informed the inspector that appellant, lessee of the ground floor, was using the rear of his leasehold as a personal residence. Claiming that the building’s occupancy permit did not allow residential use of the ground floor, the inspector confronted appellant and demanded that he permit an inspection of the premises. Appellant refused to allow the inspection because the inspector lacked a search warrant.
 </p>
<p id="b570-6">
  The inspector returned on November 8, again without a warrant, and appellant again refused to allow an inspection. ' A citation was then mailed ordering appellant to appear at the district attorney’s office. When appellant failed to appear, two inspectors returned to his apartment on November 22. They informed appellant that he was required by law to permit an inspection under § 503 of the Housing Code:
 </p>
<blockquote id="b570-7">
  “Sec. 503 Right to Enter Building. Authorized employees of the City departments or City agencies, so far as may be necessary for the performance of their duties, shall, upon presentation of proper credentials, have the right to enter, at reasonable times, any building, structure, or premises in the City to perform any duty imposed upon them by the Municipal Code.”
 </blockquote>
<p id="b571-4">
<span citation-index="1" class="star-pagination" label="527"> 
   *527
   </span>
  Appellant nevertheless refused the inspectors access to his apartment without a search warrant. Thereafter, a complaint was filed charging him with refusing to permit a lawful inspection in violation of § 507 of the Code.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  Appellant was arrested on December 2 and released on bail. When his demurrer to the criminal complaint was denied, appellant filed this petition for a writ of prohibition.
 </p>
<p id="b571-5">
  Appellant has argued throughout this litigation that § 503 is contrary to the Fourth and Fourteenth Amendments in that it authorizes municipal officials to enter a private dwelling without a search warrant and without probable cause to believe that a violation of the Housing Code exists therein. Consequently, appellant contends, he may not be prosecuted under § 507 for refusing to permit an inspection unconstitutionally authorized by § 503. Relying on
  <em>
   Frank
  </em>
  v.
  <em>
   Maryland, Eaton
  </em>
  v.
  <em>
   <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">Price</a></span>,
  </em>
  and decisions in other States,
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  the District
  <span citation-index="1" class="star-pagination" label="528"> 
   *528
   </span>
  Court of Appeal held that § 503 does not violate Fourth Amendment rights because it “is part of a regulatory scheme which is essentially civil rather than criminal in nature, inasmuch as that section creates a right of inspection which is limited in scope and may not be exercised under unreasonable conditions.” Having concluded that
  <em>
   Frank
  </em>
  v.
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Maryland</a></span>,
  </em>
  to the extent that it sanctioned such warrantless inspections, must be overruled, we reverse.
 </p>
<p id="b572-5">
  I.
 </p>
<p id="b572-6">
  The Fourth Amendment provides that, “The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.” The basic purpose of this Amendment, as recognized in countless decisions of this Court, is to safeguard the privacy and security of individuals against arbitrary invasions by governmental officials. The Fourth Amendment thus gives concrete expression to a right of the people which “is basic to a free society.”
  <em>
   Wolf
  </em>
  v.
  <em>
   Colorado,
  </em>
  <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span>. As such, the Fourth Amendment is enforceable against the States through the Fourteenth Amendment.
  <em>
   Ker
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#30" aria-description="Citation for case: Ker v. California">374 U. S. 23, 30</a></span>.
 </p>
<p id="b572-7">
  Though there has been general agreement as to the fundamental purpose of the Fourth Amendment, translation of the abstract prohibition against “unreasonable searches and seizures” into workable guidelines for the decision of particular cases is a difficult task which has for many years divided the members of this Court. Nevertheless, one governing principle, justified by history and by current experience, has consistently been followed: except in certain carefully defined classes of cases, a search of private property without proper con
  <span citation-index="1" class="star-pagination" label="529"> 
   *529
   </span>
  sent is “unreasonable” unless it has been authorized by a valid search warrant. See,
  <em>
   e. g., Stoner
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">376 U. S. 483</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Jeffers,
  </em>
  <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>;
  <em>
   McDonald
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>;
  <em>
   Agnello
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span>. As the Court explained in
  <em>
   Johnson
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, 14:
 </p>
<blockquote id="b573-5">
  “The right of officers to thrust themselves into a home is also a grave concern, not only to the individual but to a society which chooses to dwell in reasonable security and freedom from surveillance. When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent.”
 </blockquote>
<p id="b573-6">
  In
  <em>
   Frank
  </em>
  v.
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Maryland</a></span>,
  </em>
  this Court upheld the conviction of one who refused to permit a warrantless inspection of private premises for the purposes of locating and abating a suspected public nuisance. Although
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  can arguably be distinguished from this case on its facts,
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  the
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  opinion has generally been interpreted as carving out an additional exception to the rule that warrantless searches are unreasonable under the Fourth Amendment. See
  <em>
   Eaton
  </em>
  v.
  <em>
   <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">Price, supra.</a></span>
  </em>
  The District Court of Appeal so interpreted
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  in this case, and that ruling is the core of appellant’s challenge here. We proceed to a re-examination of the factors which
  <span citation-index="1" class="star-pagination" label="530"> 
   *530
   </span>
  persuaded the
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  majority to adopt this construction of the Fourth Amendment’s prohibition against unreasonable searches.
 </p>
<p id="b574-5">
  To the
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  majority, municipal fire, health, and housing inspection programs “touch at most upon the periphery of the important interests safeguarded by the Fourteenth Amendment’s protection against official intrusion,” <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#367" aria-description="Citation for case: Frank v. Maryland">359 U. S., at 367</a></span>, because the inspections are merely to determine whether physical conditions exist which do not comply with minimum standards prescribed in local regulatory ordinances. Since the inspector does not ask that the property owner open his doors to a search for “evidence of criminal action” which may be used to secure the owner’s criminal conviction, historic interests of “self-protection” jointly protected by the Fourth and Fifth Amendments
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  are said not to be involved, but only the less intense “right to be secure from intrusion into personal privacy.”
  <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#365" aria-description="Citation for case: Frank v. Maryland"><em>
   Id.,
  </em>
  at 365</a></span>.
 </p>
<p id="b574-6">
  We may agree that a routine inspection of the physical condition of private property is a less hostile intrusion than the typical policeman’s search for the fruits and instrumentalities of crime. For this reason alone,
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  differed from the great bulk of Fourth Amendment cases which have been considered by this Court. But we cannot agree that the Fourth Amendment interests at stake in these inspection cases are merely “peripheral.”. It is surely anomalous to say that the individual and his private property are fully protected by the Fourth Amendment only when the individual is suspected of criminal behavior.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
  For instance, even the most law-abiding citi
  <span citation-index="1" class="star-pagination" label="531"> 
   *531
   </span>
  zen. has a very tangible interest in limiting the circumstances under which the sanctity of his home may be broken by official authority, for the possibility of criminal entry under the guise of official sanction is a serious threat to personal and family security. And even accepting
  <em>
   Frank’s
  </em>
  rather remarkable premise, inspections of the kind we are here considering do in fact jeopardize “self-protection” interests of the property owner. Like most regulatory laws, fire, health, and housing codes are enforced by criminal processes. In some cities, discovery of a violation by the inspector leads to a criminal complaint.
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  Even in cities where discovery of a violation produces only an administrative compliance order,
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
  refusal to comply is a criminal offense, and the fact of compliance is verified by a second inspection, again without a warrant.
  <a class="footnote" href="#fn9" id="fn9_ref">
   9
  </a>
  Finally, as this case demonstrates, refusal to permit an inspection is itself a crime, punishable by fine or even by jail sentence.
 </p>
<p id="b575-4">
  The
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  majority suggested, and appellee reasserts, two other justifications for permitting administrative health and safety inspections without a warrant. First, it is argued that these inspections are “designed to make the least possible demand on the individual occupant.” <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#367" aria-description="Citation for case: Frank v. Maryland">359 U. S., at 367</a></span>. The ordinances authorizing inspections are hedged with safeguards, and at any rate the inspector’s particular decision to enter must comply with the constitutional standard of reasonableness even if -he may enter without a warrant.
  <a class="footnote" href="#fn10" id="fn10_ref">
   10
  </a>
  In addition, the argument
  <span citation-index="1" class="star-pagination" label="532"> 
   *532
   </span>
  proceeds, the warrant process could not function effectively in this field. The decision to inspect an entire municipal area is based upon legislative or administrative assessment of broad factors such as the area’s age and condition. Unless the magistrate is to review such policy matters, he must issue a “rubber stamp” warrant which provides no protection at all to the property owner.
 </p>
<p id="b576-6">
  In our opinion, these arguments unduly discount the purposes behind the warrant machinery contemplated by the Fourth Amendment. Under the present system, when the inspector demands entry, the occupant has no way of knowing whether enforcement of the municipal code involved requires inspection of his premises, no way of knowing the lawful limits of the inspector’s power to search, and no way of knowing whether the inspector himself is acting under proper authorization. These are questions which may be reviewed by a neutral magistrate without any reassessment of the basic agency decision to canvass an area. Yet, only by refusing entry and risking a criminal conviction can the occupant at present challenge the inspector’s decision to search. And even if the occupant possesses sufficient fortitude to take this risk, as appellant did here, he may never learn any more about the reason for the inspection than that the law generally allows housing inspectors to gain entry. The practical effect of this system is to leave the occupant subject to the discretion of the official in the field. This is precisely the discretion to invade private property which we have consistently circumscribed by a requirement that a disinterested party warrant the need to
  <span citation-index="1" class="star-pagination" label="533"> 
   *533
   </span>
  search. See cases cited, p. 529,
  <em>
   supra.
  </em>
  We simply cannot say that the protections provided by the warrant procedure are not needed in this context; broad statutory safeguards are no substitute for individualized review, particularly when those safeguards may only be invoked at the risk of a criminal penalty.
 </p>
<p id="b577-5">
  The final justification suggested for warrantless administrative searches is that the public interest demands such a rule: it is vigorously argued that the health and safety of entire urban populations is dependent upon enforcement of minimum fire, housing, and sanitation standards, and that the only effective means of enforcing such codes is by routine systematized inspection of all physical structures. Of course, in applying any reasonableness standard, including one of constitutional dimension, an argument that the public interest demands a particular rule must receive careful consideration. But we think this argument misses the mark. The question is not, at this stage at least, whether these inspections may be made, but whether they may be made without a warrant. For example, to say that gambling raids may not be made at the discretion of the police without a warrant is not necessarily to say that gambling raids may never be made. In assessing whether the public interest demands creation of a general exception to the Fourth Amendment’s warrant requirement, the question is not whether the public interest justifies the type of search in question, but whether the authority to search should be evidenced by a warrant, which in turn depends in part upon whether the burden of obtaining a warrant is likely to frustrate the governmental purpose behind the search. See
  <em>
   Schmerber
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 770-771</a></span>. It has nowhere been urged that fire, health, and housing code inspection programs could not achieve their goals within the confines of a reasonable search warrant requirement. Thus, we do not find the public need argument dispositive.
 </p>
<p id="b578-3">
<span citation-index="1" class="star-pagination" label="534"> 
   *534
   </span>
  In summary, we hold that administrative searches of the kind at issue here are significant intrusions upon the interests protected by the Fourth Amendment, that such searches when authorized and conducted without a warrant procedure lack the traditional safeguards which the Fourth Amendment guarantees to the individual, and that the reasons put forth in
  <em>
   Frank
  </em>
  v.
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Maryland</a></span>
  </em>
  and in other cases for upholding these warrantless searches are insufficient to justify so substantial a weakening of the Fourth Amendment’s protections. Because of the nature of the municipal programs under consideration, however, these conclusions must be the beginning, not the end, of our inquiry. The
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  majority gave recognition to the unique character of these inspection programs by refusing to require search warrants; to reject that disposition does not justify ignoring the question whether some other accommodation between public need and individual rights is essential.
 </p>
<p id="b578-4">
  II.
 </p>
<p id="b578-5">
  The Fourth Amendment provides that, “no Warrants shall issue, but upon probable cause.” Borrowing from more typical Fourth Amendment cases, appellant argues not only that code enforcement inspection programs must be circumscribed by a warrant procedure, but also that warrants should issue only when the inspector possesses probable cause to believe that a particular dwelling contains violations of the minimum standards prescribed by the code being enforced. We disagree.
 </p>
<p id="b578-6">
  In cases in which the Fourth Amendment requires that a warrant to search be obtained, “probable cause” is the standard by which a particular decision to search is tested against the constitutional mandate of reasonableness. To apply this standard, it is obviously necessary first to focus upon the governmental interest which allegedly justifies official intrusion upon the constitutionally pro
  <span citation-index="1" class="star-pagination" label="535"> 
   *535
   </span>
  tected interests of the private citizen. Por example, in a criminal investigation, the police may undertake to recover specific stolen or contraband goods. But that public interest would hardly justify a sweeping search of an entire city conducted in the hope that these goods might be found. Consequently, a search for these goods, even with a warrant, is “reasonable” only when there is “probable cause” to believe that they will be uncovered in a particular dwelling.
 </p>
<p id="b579-5">
  Unlike the search pursuant to a criminal investigation, the inspection programs at issue here are aimed at securing city-wide compliance with minimum physical standards for private property. The primary governmental interest at stake is to prevent even the unintentional development of conditions which are hazardous to public health and safety. Because fires and epidemics may ravage large urban areas, because unsightly conditions adversely affect the economic values of neighboring structures, numerous courts have upheld the police power of municipalities to impose and enforce such minimum standards even upon existing structures.
  <a class="footnote" href="#fn11" id="fn11_ref">
   11
  </a>
  In determining whether a particular inspection is reasonable — and thus in determining whether there is probable cause to issue a warrant for that inspection — the need for the inspection must be weighed in terms of these reasonable goals of code enforcement.
 </p>
<p id="b579-6">
  There is unanimous agreement among those most familiar with this field that the only effective way to seek universal compliance with the minimum standards required by municipal codes is through routine periodic
  <span citation-index="1" class="star-pagination" label="536"> 
   *536
   </span>
  inspections of all structures.
  <a class="footnote" href="#fn12" id="fn12_ref">
   12
  </a>
  It is here that the probable cause debate is focused, for the agency’s decision to conduct an area inspection is unavoidably based on its appraisal of conditions in the area as a whole, not on its knowledge of conditions in each particular building. Appellee contends that, if the probable cause standard urged by appellant is adopted, the area inspection will be eliminated as a means of seeking compliance with code standards and the reasonable goals of code enforcement will be dealt a crushing blow.
 </p>
<p id="b580-6">
  In meeting this contention, appellant argues first, that his probable cause standard would not jeopardize area inspection programs because only a minute portion of the population will refuse to consent to such inspections, and second, that individual privacy in any event should be given preference to the public interest in conducting such inspections. The first argument, even if true, is irrelevant to the question whether the area inspection is reasonable within the meaning of the Fourth Amendment. The second argument is in effect an assertion that the area inspection is an unreasonable search. Unfortunately, there can be no ready test for determining reasonableness
  <span citation-index="1" class="star-pagination" label="537"> 
   *537
   </span>
  other than by balancing the need to search against the invasion which the search entails. But we think that a number of persuasive factors combine to support the reasonableness of area code-enforcement inspections. First, such programs have a long history of judicial and public acceptance. See
  <em>
   Frank
  </em>
  v.
  <em>
   Maryland,
  </em>
  <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#367" aria-description="Citation for case: Frank v. Maryland">359 U. S., at 367-371</a></span>. Second, the public interest demands that all dangerous conditions be prevented or abated, yet it is doubtful that any other canvassing technique would achieve acceptable results. Many such conditions— faulty wiring is an obvious example — are not observable from outside the building and indeed may not be apparent to the inexpert occupant himself. Finally, because the inspections are neither personal in nature nor aimed at the discovery of evidence of crime, they involve a relatively limited invasion of the urban citizen’s privacy. Both the majority and the dissent in
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  emphatically supported this conclusion:
 </p>
<blockquote id="b581-5">
  “Time and experience have forcefully taught that the power to inspect dwelling places, either as a matter of systematic area-by-area search or, as here, to treat a specific problem, is of indispensable importance to the maintenance of community health; a power that would be greatly hobbled by the blanket requirement of the safeguards necessary for a search of evidence of criminal acts. The need for preventive action is great, and city after city has seen this need and granted the power of inspection to its health officials; and these inspections are apparently welcomed by all but an insignificant few. Certainly, the nature of our society has not vitiated the need for inspections first thought necessary 158 years ago, nor has experience revealed any abuse or inroad on freedom in meeting this need by means that history and dominant public opinion have sanctioned.” <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#372" aria-description="Citation for case: Frank v. Maryland">359 U. S., at 372</a></span>.
 </blockquote>
<blockquote id="b582-5">
<span citation-index="1" class="star-pagination" label="538"> 
   *538
   </span>
  . . This is not to suggest that a health official need show the same kind of proof to a magistrate to obtain a warrant as one must who would search for the fruits or instrumentalities of crime. Where considerations of health and safety are involved, the facts that would justify an inference of 'probable cause’ to make an inspection are clearly different from those that would justify such an inference where a criminal investigation has been undertaken. Experience may show the need for periodic inspections of certain facilities without a further showing of cause to believe that substandard conditions dangerous to the public are being maintained. The passage of a certain period without inspection might of itself be sufficient in a given situation to justify the issuance of a warrant. The test of 'probable cause’ required by the Fourth Amendment can take into account the nature of the search that is being sought.” <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#383" aria-description="Citation for case: Frank v. Maryland">359 U. S., at 383</a></span> (Mr. Justice Douglas, dissenting).
 </blockquote>
<p id="b582-6">
  Having concluded that the area inspection is a “reasonable” search of private property within the meaning of the Fourth Amendment, it is obvious that “probable cause” to issue a warrant to inspect must exist if reasonable legislative or administrative standards for conducting an area inspection are satisfied with respect to a particular dwelling. Such standards, which will vary with the municipal program being enforced, may be based upon the passage of time, the nature of the building
  <em>
   (e. g.,
  </em>
  a multi-family apartment house), or the condition of the entire area, but they will not necessarily depend upon specific knowledge of the condition of the particular dwelling. It has been suggested that so to vary the probable cause test from the standard applied in criminal cases would be to authorize a “synthetic search warrant” and thereby to lessen the overall protections of the Fourth Amendment.
  <em>
   Frank
  </em>
  v.
  <em>
   Maryland,
  </em>
  359
  <span citation-index="1" class="star-pagination" label="539"> 
   *539
   </span>
  U. S., at 373. But we do not agree. The warrant procedure is designed to guarantee that a decision to search private property is justified by a reasonable governmental interest. But reasonableness is still the ultimate standard. If a valid public interest justifies the intrusion contemplated, then there is probable cause to issue a suitably restricted search warrant. Cf.
  <em>
   Oklahoma Press Pub. Co.
  </em>
  v.
  <em>
   Walling,
  </em>
  <span class="citation" data-id="9419755"><a href="/opinion/104239/oklahoma-press-publishing-co-v-walling/" aria-description="Citation for case: Oklahoma Press Publishing Co. v. Walling">327 U. S. 186</a></span>. Such an approach neither endangers time-honored doctrines applicable to criminal investigations nor makes a nullity of the probable cause requirement in this area. It merely gives full recognition to the competing public and private interests here at stake and, in so doing, best fulfills the historic purpose behind the constitutional right to be free from unreasonable government invasions of privacy. See
  <em>
   Eaton
  </em>
  v.
  <em>
   Price,
  </em>
  <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/#273" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">364 U. S., at 273-274</a></span> (opinion of Mr. Justice Brennan).
 </p>
<p id="b583-5">
  III.
 </p>
<p id="b583-6">
  Since our holding emphasizes the controlling standard of reasonableness, nothing we say today is intended to foreclose prompt inspections, even without a warrant, that the law has traditionally upheld in emergency situations. See
  <em>
   North American Cold Storage Co.
  </em>
  v.
  <em>
   City of Chicago,
  </em>
  <span class="citation" data-id="96902"><a href="/opinion/96902/north-american-cold-storage-co-v-city-of-chicago/" aria-description="Citation for case: North American Cold Storage Co. v. City of Chicago">211 U. S. 306</a></span> (seizure of unwholesome food);
  <em>
   Jacobson
  </em>
  v.
  <em>
   Massachusetts,
  </em>
  <span class="citation" data-id="96230"><a href="/opinion/96230/jacobson-v-massachusetts/" aria-description="Citation for case: Jacobson v. Massachusetts">197 U. S. 11</a></span> (compulsory smallpox vaccination);
  <em>
   Compagnie Francaise
  </em>
  v.
  <em>
   Board of Health,
  </em>
  <span class="citation" data-id="9417887"><a href="/opinion/95698/compagnie-francaise-de-navigation-a-vapeur-v-louisiana-state-board-of/" aria-description="Citation for case: Compagnie Francaise De Navigation a Vapeur v. Louisiana...">186 U. S. 380</a></span> (health quarantine);
  <em>
   Kroplin
  </em>
  v.
  <em>
   Truax,
  </em>
  <span class="citation" data-id="3783238"><a href="/opinion/4026648/kroplin-v-truax/" aria-description="Citation for case: Kroplin v. Truax">119 Ohio St. 610</a></span>, <span class="citation" data-id="3783238"><a href="/opinion/4026648/kroplin-v-truax/" aria-description="Citation for case: Kroplin v. Truax">165 N. E. 498</a></span> (summary destruction of tubercular cattle). On the other hand, in the .case of most routine area inspections, there is no compelling urgency to inspect at a particular time or on a particular day. Moreover, most citizens allow inspections of their property without a warrant. Thus, as a practical matter and in light of the Fourth Amendment’s requirement that a warrant specify the property to be searched, it seems likely that warrants should normally be sought only after entry is refused unless
  <span citation-index="1" class="star-pagination" label="540"> 
   *540
   </span>
  there has been a citizen complaint or there is other satisfactory reason for securing immediate entry. Similarly, the requirement of a warrant procedure does not suggest any change in what seems to be the prevailing local policy, in most situations, of authorizing entry, but not entry by force, to inspect.
 </p>
<p id="b584-5">
  IV.
 </p>
<p id="b584-6">
  In this case, appellant has been charged with a crime for his refusal to permit housing inspectors to enter his leasehold without a warrant. There was no emergency demanding immediate access; in fact, the inspectors made three trips to the building in an attempt to obtain appellant’s consent to search. Yet no warrant was obtained and thus appellant was unable to verify either the need for or the appropriate limits of the inspection. No doubt, the inspectors entered the public portion of the building with the consent of the landlord, through the building’s manager, but appellee does not contend that such consent was sufficient to authorize inspection of appellant’s premises. Cf.
  <em>
   Stoner
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">376 U. S. 483</a></span>;
  <em>
   Chapman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span>;
  <em>
   McDonald
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>. Assuming the facts to be as the parties have alleged, we therefore conclude that appellant had a constitutional right to insist that the inspectors obtain a warrant to search and that appellant may not constitutionally be convicted for refusing to consent to the inspection. It appears from the opinion of the District Court of Appeal that under these circumstances a writ of prohibition will issue to the criminal court under California law.
 </p>
<p id="b584-7">
  The judgment is vacated and the case is remanded for further proceedings not inconsistent with this opinion.
 </p>
<p id="b584-8">
<em>
   It is so ordered.
  </em>
</p>
<judges id="b584-9">
  [For dissenting opinion of Mr. Justice Clark, see
  <em>
   post,
  </em>
  p. 546.]
 </judges>












<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b570-8">
   The inspection was conducted pursuant to § 86 (3) of the San Francisco Municipal Code, which provides that apartment house operators shall pay an annual license fee in part to defray the cost of periodic inspections of their buildings. The inspections are to be made by the Bureau of Housing Inspection “at least once a year and as often thereafter as may be deemed necessary.” The permit of occupancy, which prescribes the apartment units which a building may contain, is not issued until the license is obtained.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b571-6">
   “Sec. 507 PENALTY FOR Violation. Any person, the owner or his authorized agent who violates, disobeys, omits, neglects, or refuses to comply with, or who resists or opposes the execution of any of the provisions of this Code, or any order of the Superintendent, the Director of Public Works, or the Director of Public Health made pursuant to this Code, shall be guilty of a misdemeanor and upon conviction thereof shall be punished by a fine not exceeding five hundred dollars ($500.00), or by imprisonment, not exceeding six (6) months or by both such fine and imprisonment, unless otherwise provided in this Code, and shall be deemed guilty of a separate offense for every day such violation, disobedience, omission, neglect or refusal shall continue.”
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b571-7">
<em>
    Givner
   </em>
   v.
   <em>
    State,
   </em>
   <span class="citation" data-id="2305304"><a href="/opinion/2305304/givner-v-state/" aria-description="Citation for case: Givner v. State">210 Md. 484</a></span>, <span class="citation" data-id="2305304"><a href="/opinion/2305304/givner-v-state/" aria-description="Citation for case: Givner v. State">124 A. 2d 764</a></span> (1956);
   <em>
    City of St. Louis
   </em>
   v.
   <em>
    Evans,
   </em>
   <span class="citation" data-id="2435050"><a href="/opinion/2435050/city-of-st-louis-v-evans/" aria-description="Citation for case: City of St. Louis v. Evans">337 S. W. 2d 948</a></span> (Mo. 1960);
   <em>
    State ex rel. Eaton
   </em>
   v.
   <em>
    Pnce,
   </em>
   <span class="citation no-link">168 Ohio St. 123</span>, <span class="citation no-link">151 N. E. 2d 523</span> (1958), aff’d by an equally divided Court, <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">364 U. S. 263</a></span> (1960). See also
   <em>
    State
   </em>
   v.
   <em>
    Rees,
   </em>
   <span class="citation" data-id="9570716"><a href="/opinion/1306345/state-v-rees/" aria-description="Citation for case: State v. Rees">258 Iowa 813</a></span>, <span class="citation" data-id="9570716"><a href="/opinion/1306345/state-v-rees/" aria-description="Citation for case: State v. Rees">139 N. W. 2d 406</a></span> (1966);
   <em>
    Commonwealth
   </em>
   v.
   <em>
    Hadley,
   </em>
   <span class="citation" data-id="2008391"><a href="/opinion/2008391/commonwealth-v-hadley/" aria-description="Citation for case: Commonwealth v. Hadley">351 Mass. 439</a></span>, <span class="citation" data-id="2008391"><a href="/opinion/2008391/commonwealth-v-hadley/" aria-description="Citation for case: Commonwealth v. Hadley">222 N. E. 2d 681</a></span> (1966), appeal docketed Jan. 5, 1967, No. 1179, Misc., O. T. 1966;
   <em>
    People
   </em>
   v.
   <em>
    Laverne,
   </em>
   14 N. Y. 2d 304, <span class="citation" data-id="5521228"><a href="/opinion/5673733/people-v-laverne/" aria-description="Citation for case: People v. Laverne">200 N. E. 2d 441</a></span> (1964).
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b573-7">
   In
   <em>
    <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>,
   </em>
   the Baltimore ordinance required that the health inspector “have cause to suspect that a nuisance exists in any house, cellar or enclosure” before he could demand entry without a warrant, a requirement obviously met in
   <em>
    <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
   </em>
   because the inspector observed extreme structural decay and a pile of rodent feces on the appellant’s premises. Section 503 of the San Francisco Housing Code has no such “cause” requirement, but neither did the Ohio ordinance at issue in
   <em>
    Eaton
   </em>
   v.
   <em>
    <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">Price</a></span>,
   </em>
   a case which four Justices thought was controlled by
   <em>
    Frank.
   </em>
   <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/#264" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">364 U. S., at 264, 265, n. 2</a></span> (opinion of Mr. Justice BrennaN).
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b574-7">
   See
   <em>
    Boyd
   </em>
   v.
   <em>
    United States,
   </em>
   116 17. S. 616. Compare
   <em>
    Schmerber
   </em>
   v.
   <em>
    California,
   </em>
   <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#766" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 766-772</a></span>.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b574-8">
   See
   <em>
    Abel v. United States,
   </em>
   <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#254" aria-description="Citation for case: Abel v. United States">362 U. S. 217, 254-256</a></span> (MR. Justice Brennan, dissenting);
   <em>
    District of Columbia
   </em>
   v.
   <em>
    Little,
   </em>
   85 U. S. App. D. C. 242, <span class="citation" data-id="9442232"><a href="/opinion/223783/district-of-columbia-v-little/" aria-description="Citation for case: District of Columbia v. Little">178 F. 2d 13</a></span>, aff’d, <span class="citation" data-id="104766"><a href="/opinion/104766/district-of-columbia-v-little/" aria-description="Citation for case: District of Columbia v. Little">339 U. S. 1</a></span>.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b575-5">
   See New York, N. Y., Administrative Code § D26-8.0 (1964).
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b575-6">
   See Washington, D. C., Housing Regulations §2104.
  </p>
</div><div class="footnote" id="fn9" label="9">
<a class="footnote" href="#fn9_ref">
   9
  </a>
<p id="b575-7">
   This is the more prevalent enforcement procedure. See Note, Enforcement of Municipal Housing Codes, <span class="citation no-link">78 Harv. L. Rev. 801</span>, 813-816.
  </p>
</div><div class="footnote" id="fn10" label="10">
<a class="footnote" href="#fn10_ref">
   10
  </a>
<p id="b575-8">
   The San Francisco Code requires that the inspector display-proper credentials, that he inspect “at reasonable times,” and that
   <span citation-index="1" class="star-pagination" label="532"> 
    *532
    </span>
   he not obtain entry by force, at least when there is no emergency. The Baltimore ordinance in
   <em>
    <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
   </em>
   required that the inspector “have cause to suspect that a nuisance exists.” Some cities notify residents in advance, by mail or posted notice, of impending area inspections. State courts upholding these inspections without warrants have imposed a general reasonableness requirement. See cases cited, n. 3,
   <em>
    supra.
   </em>
</p>
</div><div class="footnote" id="fn11" label="11">
<a class="footnote" href="#fn11_ref">
   11
  </a>
<p id="b579-7">
   See
   <em>
    Abbate Bros.
   </em>
   v.
   <em>
    City of Chicago,
   </em>
   <span class="citation" data-id="2049948"><a href="/opinion/2049948/abbate-bros-inc-v-city-of-chicago/" aria-description="Citation for case: Abbate Bros., Inc. v. City of Chicago">11 Ill. 2d 337</a></span>, <span class="citation" data-id="2049948"><a href="/opinion/2049948/abbate-bros-inc-v-city-of-chicago/" aria-description="Citation for case: Abbate Bros., Inc. v. City of Chicago">142 N. E. 2d 691</a></span>;
   <em>
    City of Louisville
   </em>
   v.
   <em>
    Thompson,
   </em>
   <span class="citation" data-id="2430498"><a href="/opinion/2430498/city-of-louisville-v-thompson/" aria-description="Citation for case: City of Louisville v. Thompson">339 S. W. 2d 869</a></span> (Ky.) ;
   <em>
    Adamec
   </em>
   v.
   <em>
    Post,
   </em>
   <span class="citation" data-id="3620827"><a href="/opinion/3637215/adamec-v-post/" aria-description="Citation for case: Adamec v. Post">273 N. Y. 250</a></span>, <span class="citation" data-id="3620827"><a href="/opinion/3637215/adamec-v-post/" aria-description="Citation for case: Adamec v. Post">7 N. E. 2d 120</a></span>;
   <em>
    Paquette
   </em>
   v.
   <em>
    City of Fall River,
   </em>
   <span class="citation" data-id="2062881"><a href="/opinion/2062881/paquette-v-city-of-fall-river/" aria-description="Citation for case: Paquette v. City of Fall River">338 Mass. 368</a></span>, <span class="citation" data-id="2062881"><a href="/opinion/2062881/paquette-v-city-of-fall-river/" aria-description="Citation for case: Paquette v. City of Fall River">155 N. E. 2d 775</a></span>;
   <em>
    Richards
   </em>
   v.
   <em>
    City of Columbia,
   </em>
   227 S. C. 538, <span class="citation" data-id="9585880"><a href="/opinion/1334923/richards-v-city-of-columbia/" aria-description="Citation for case: Richards v. City of Columbia">88 S. E. 2d 683</a></span>;
   <em>
    Boden
   </em>
   v.
   <em>
    City of Milwaukee,
   </em>
   <span class="citation" data-id="2155771"><a href="/opinion/2155771/boden-v-city-of-milwaukee/" aria-description="Citation for case: Boden v. City of Milwaukee">8 Wis. 2d 318</a></span>, <span class="citation" data-id="2155771"><a href="/opinion/2155771/boden-v-city-of-milwaukee/" aria-description="Citation for case: Boden v. City of Milwaukee">99 N. W. 2d 156</a></span>.
  </p>
</div><div class="footnote" id="fn12" label="12">
<a class="footnote" href="#fn12_ref">
   12
  </a>
<p id="b580-7">
   See Osgood &amp; Zwerner, Rehabilitation and Conservation, 25 Law &amp; Contemp. Prob. 705, 718 and n. 43; Schwartz, Crucial Areas in Administrative Law, <span class="citation no-link">34 Geo. Wash. L. Rev. 401</span>, 423 and n. 93; Comment, Rent Withholding and the Improvement of Substandard Housing, <span class="citation no-link">53 Calif. L. Rev. 304</span>, 316-317; Note, Enforcement of Municipal Housing Codes, <span class="citation no-link">78 Harv. L. Rev. 801</span>, 807, 851; Note, Municipal Housing Codes, <span class="citation no-link">69 Harv. L. Rev. 1115</span>, 1124-1125. Section 311 (a) of the Housing and Urban Development Act of 1965, <span class="citation no-link">79 Stat. 478</span>, <span class="citation no-link">42 U. S. C. § 1468</span> (1964 ed., Supp. I), authorizes grants of federal funds “to cities, other municipalities, and counties for the purpose of assisting such localities in carrying out programs of concentrated code enforcement in deteriorated or deteriorating areas in which such enforcement, together with those public improvements to be provided by the locality, may be expected to arrest the decline of the area.”
  </p>
</div></div></opinion>
```

---
