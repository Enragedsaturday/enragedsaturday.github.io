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

## GROUP: content/cases/Connally v. Georgia.md  (`case`, 5 assertions)

### content_page

```
---
title: "Connally v. Georgia"
type: case
citation: "429 U.S. 245 (1977)"
parallel_cite: "97 S. Ct. 546; 50 L. Ed. 2d 444"
neutral_cite: 1977 U.S. LEXIS 27
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-01-10
docket: 76-461
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1977-01-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Connally v. Georgia
  varies_by_point: false
  scope_note: "Controlling: a magistrate with a direct pecuniary interest in issuing warrants is not neutral and detached, so such warrants are void."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109572/connally-v-georgia/"
  cluster_id: 109572
  opinion_id: 109572
  identity_checked: true
homes:
  - page: "[[The Neutral and Detached Magistrate]]"
    role: "Progeny"
related: ["[[Coolidge v. New Hampshire]]", "[[Lo-Ji Sales, Inc. v. New York]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant-requirement", "neutral-magistrate"]
holding: "A search warrant issued by a magistrate who is paid a fee for issuing a warrant but nothing for denying one is invalid: such a magistrate has a direct, personal, pecuniary interest in issuance and is not neutral and detached as the Fourth Amendment requires."
lake:
  record_id: Connally v. Georgia
  status: verified
  projected_at: 2026-07-06
---

# Connally v. Georgia

*429 U.S. 245 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Georgia justice of the peace issued a search warrant for Connally's premises. Under Georgia's fee system, the justice received a $5 fee when he issued a warrant and nothing when he declined to issue one. The justice testified that the fee did enter his mind when deciding whether to issue a warrant. Connally challenged the warrant on the ground that it was issued by a magistrate who was not neutral and detached.

## Issue
Is a search warrant valid under the Fourth Amendment when issued by a magistrate who is compensated for issuing the warrant but receives nothing for denying it?

## Rule
No. Applying the principle of *Tumey* and *Ward*, the justice's "financial welfare . . . is enhanced by positive action and is not enhanced by negative action" — a system offering "'a possible temptation to the average man as a judge . . . [that] might lead him not to hold the balance nice, clear and true between the State and the accused.'" — 429 U.S. at 250. ^pin-250

The defendant is thus "subjected to what surely is judicial action by an officer of a court who has 'a direct, personal, substantial, pecuniary interest' in his conclusion to issue or to deny the warrant." — *Id.* ^pin-250b

The Court therefore "h[e]ld that the issuance of the search warrant by the justice of the peace in Connally's case effected a violation of the protections afforded him by the Fourth and Fourteenth Amendments." — *Id.* at 251. ^pin-251

## Application
The Georgia justice of the peace earned $5 only when he issued a warrant and nothing when he denied one, so his compensation rose with issuance — the precise pecuniary temptation the neutral-magistrate requirement forbids, and one he candidly admitted entered his mind. The fee was not *[[Common Legal Terms#de-minimis|de minimis]]*. Because the issuing official had a personal financial stake in granting the warrant, he was not the neutral and detached magistrate the Fourth Amendment demands, and the warrant was invalid.

## Conclusion
The warrant violated the Fourth and Fourteenth Amendments; the judgment of the Georgia Supreme Court was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Connally* remains controlling on the neutral-and-detached-magistrate requirement, applying the disqualifying-financial-interest principle to warrant issuance. It is taught alongside [[Coolidge v. New Hampshire]] (warrant issued by the prosecuting attorney general) and [[Lo-Ji Sales, Inc. v. New York]] (magistrate who joined the search). No negative treatment.

## Appears on
- [[The Neutral and Detached Magistrate]] — *Progeny*

## Sources
- *Connally v. Georgia*, 429 U.S. 245 (1977) (per curiam) — https://www.courtlistener.com/opinion/109572/connally-v-georgia/ — pinpoints: 250, 251.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b59bab4a3e4ffdb0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "429 U.S. 245 (1977)", "court": "U.S. Supreme Court", "neutral_cite": "1977 U.S. LEXIS 27", "official_citation_present": true, "parallel_cite": "97 S. Ct. 546; 50 L. Ed. 2d 444", "title": "Connally v. Georgia", "year": "1977"}}
{"assertion_id": "15411ffe83fda18a", "dimension": "support", "kind": "home_role", "locator": {"home": "The Neutral and Detached Magistrate"}, "payload": {"home": "The Neutral and Detached Magistrate", "role": "Progeny", "title": "Connally v. Georgia"}}
{"assertion_id": "dc35af9d707a0f0a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A search warrant issued by a magistrate who is paid a fee for issuing a warrant but nothing for denying one is invalid: such a magistrate has a direct, personal, pecuniary interest in issuance and is not neutral and detached as the Fourth Amendment requires.", "title": "Connally v. Georgia"}}
{"assertion_id": "936cf04f0600a734", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Connally v. Georgia"}}
{"assertion_id": "b1a452f5da595930", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1977-01-10", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Connally v. Georgia", "field_i_validity": "good_law", "scope_note": "Controlling: a magistrate with a direct pecuniary interest in issuing warrants is not neutral and detached, so such warrants are void.", "title": "Connally v. Georgia", "varies_by_point": "false"}}
```

### lake record — Connally v. Georgia

```json
{
  "schema_version": "s2.v1",
  "record_id": "Connally v. Georgia",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Connally v. Georgia",
    "case_name_short": "Connally",
    "case_name_full": "Connally v. Georgia",
    "input_case_name": "Connally v. Georgia",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-01-10",
    "year": 1977,
    "docket": "76-461",
    "cluster_id": 109572,
    "lead_opinion_id": 109572,
    "sibling_ids": [
      109572
    ],
    "absolute_url": "/opinion/109572/connally-v-georgia/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "429 U.S. 245",
      "volume": "429",
      "reporter": "U.S.",
      "page": "245",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 546",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "546",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 L. Ed. 2d 444",
        "volume": "50",
        "reporter": "L. Ed. 2d",
        "page": "444",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 27",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "27",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "429 U.S. 245",
        "volume": "429",
        "reporter": "U.S.",
        "page": "245",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 546",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "546",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 L. Ed. 2d 444",
        "volume": "50",
        "reporter": "L. Ed. 2d",
        "page": "444",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 27",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "27",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "429 U.S. 245",
    "official_selection": {
      "court_class": "scotus",
      "selected": "429 U.S. 245",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-250",
      "page": null,
      "quote": "--- # Connally v. Georgia *429 U.S. 245 (1977)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Georgia justice of the peace issued a search warrant for Connally's premises. Under Georgia's fee system, the justice received a $5 fee when he issued a warrant and nothing when he declined to issue one. The justice testified that the fee did enter his mind when deciding whether to issue a warrant. Connally challenged the warrant on the ground that it was issued by a magistrate who was not neutral and detached. ## Issue Is a search warrant valid under the Fourth Amendment when issued by a magistrate who is compensated for issuing the warrant but receives nothing for denying it? ## Rule No. Applying the principle of *Tumey* and *Ward*, the justice's",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-250b",
      "page": null,
      "quote": "subjected to what surely is judicial action by an officer of a court who has 'a direct, personal, substantial, pecuniary interest' in his conclusion to issue or to deny the warrant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-251",
      "page": null,
      "quote": "h[e]ld that the issuance of the search warrant by the justice of the peace in Connally's case effected a violation of the protections afforded him by the Fourth and Fourteenth Amendments.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1977-01-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Connally v. Georgia",
    "varies_by_point": false,
    "scope_note": "Controlling: a magistrate with a direct pecuniary interest in issuing warrants is not neutral and detached, so such warrants are void.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Tennessee v. Rosemary L. Decosimo",
          "cluster_id": 4529649,
          "cite": [
            "555 S.W.3d 494"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Leotis B. Branigh, III",
          "cluster_id": 1034108,
          "cite": [
            "155 Idaho 404",
            "313 P.3d 732",
            "2013 WL 3718751",
            "2013 Ida. App. LEXIS 63"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane1_negative"
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
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Caperton v. A. T. Massey Coal Co., Inc.",
          "cluster_id": 145867,
          "cite": [
            "173 L. Ed. 2d 1208",
            "129 S. Ct. 2252",
            "556 U.S. 868",
            "2009 U.S. LEXIS 4157",
            "39 Envtl. L. Rep. (Envtl. Law Inst.) 20125",
            "77 U.S.L.W. 4456",
            "21 Fla. L. Weekly Fed. S 908"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marshall v. Jerrico, Inc.",
          "cluster_id": 110251,
          "cite": [
            "64 L. Ed. 2d 182",
            "100 S. Ct. 1610",
            "446 U.S. 238",
            "1980 U.S. LEXIS 126",
            "24 Wage & Hour Cas. (BNA) 681"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dalia v. United States",
          "cluster_id": 110061,
          "cite": [
            "60 L. Ed. 2d 177",
            "99 S. Ct. 1682",
            "441 U.S. 238",
            "1979 U.S. LEXIS 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ira Silverman (90-3205) Morris G. Woodard (90-5816) and Gary Caton (90-5733/91-6506)",
          "cluster_id": 592207,
          "cite": [
            "976 F.2d 1502",
            "1992 U.S. App. LEXIS 22892"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Felker v. State",
          "cluster_id": 1257587,
          "cite": [
            "314 S.E.2d 621",
            "252 Ga. 351",
            "1984 Ga. LEXIS 691"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. White",
          "cluster_id": 118287,
          "cite": [
            "143 L. Ed. 2d 748",
            "119 S. Ct. 1555",
            "526 U.S. 559",
            "1999 U.S. LEXIS 3172"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mettler Walloon, LLC v. Melrose Township",
          "cluster_id": 1991212,
          "cite": [
            "761 N.W.2d 293",
            "281 Mich. App. 184"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Robinson",
          "cluster_id": 3152697,
          "cite": [
            "303 Kan. 11",
            "363 P.3d 875",
            "2015 Kan. LEXIS 929"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hyde",
          "cluster_id": 1119531,
          "cite": [
            "921 P.2d 655",
            "186 Ariz. 252",
            "220 Ariz. Adv. Rep. 19",
            "1996 Ariz. LEXIS 75"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Railey v. Webb",
          "cluster_id": 1268291,
          "cite": [
            "540 F.3d 393",
            "2008 U.S. App. LEXIS 18230",
            "2008 WL 3905492"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lackey v. State",
          "cluster_id": 1308629,
          "cite": [
            "271 S.E.2d 478",
            "246 Ga. 331",
            "1980 Ga. LEXIS 1130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haas v. County of San Bernardino",
          "cluster_id": 2638590,
          "cite": [
            "45 P.3d 280",
            "119 Cal. Rptr. 2d 341",
            "27 Cal. 4th 1017",
            "2002 Cal. Daily Op. Serv. 3888",
            "2002 Daily Journal DAR 4893",
            "2002 Cal. LEXIS 2609"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Grigsby v. Mabry",
          "cluster_id": 1518699,
          "cite": [
            "569 F. Supp. 1273",
            "1983 U.S. Dist. LEXIS 14839"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Los Angeles Memorial Coliseum Commission v. National Football League",
          "cluster_id": 8812474,
          "cite": [
            "89 F.R.D. 497",
            "1981 U.S. Dist. LEXIS 13126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Harris",
          "cluster_id": 65395,
          "cite": [
            "566 F.3d 422",
            "2009 WL 1065970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Luis Santiago Ramirez",
          "cluster_id": 702391,
          "cite": [
            "63 F.3d 937",
            "42 Fed. R. Serv. 1270",
            "1995 U.S. App. LEXIS 21416",
            "1995 WL 465806"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Slaughter",
          "cluster_id": 1408323,
          "cite": [
            "315 S.E.2d 865",
            "252 Ga. 435",
            "1984 Ga. LEXIS 731"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William (Bob) Brown v. Wiley C. Edwards and All Other Constables in the State of Mississippi",
          "cluster_id": 427621,
          "cite": [
            "721 F.2d 1442",
            "1984 U.S. App. LEXIS 26739"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ryan",
          "cluster_id": 2001201,
          "cite": [
            "601 N.W.2d 473",
            "257 Neb. 635",
            "1999 Neb. LEXIS 158"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ismene M. Kalaris, Administrative Appeals Judge v. Raymond J. Donovan, Secretary of Labor, Julius Miller, Administrative Appeals Judge v. Raymond J. Donovan, Secretary of Labor, Ismene M. Kalaris, Administrative Appeals Judge v. Raymond J. Donovan, Secretary of Labor Julius Miller, Administrative Appeals Judge v. Raymond J. Donovan, Secretary of Labor",
          "cluster_id": 413120,
          "cite": [
            "697 F.2d 376"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John P. Davern",
          "cluster_id": 587642,
          "cite": [
            "970 F.2d 1490",
            "1992 WL 167526"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sharon Pollard",
          "cluster_id": 461623,
          "cite": [
            "778 F.2d 1177",
            "19 Fed. R. Serv. 593",
            "1985 U.S. App. LEXIS 24958"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Margaret T. Whitacre v. James F. Davey",
          "cluster_id": 532956,
          "cite": [
            "890 F.2d 1168",
            "281 U.S. App. D.C. 363",
            "1989 U.S. App. LEXIS 17393",
            "52 Empl. Prac. Dec. (CCH) 39,478",
            "51 Fair Empl. Prac. Cas. (BNA) 538",
            "1989 WL 140507"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Waterman Steamship Corp. v. Avondale Shipyards, Inc.",
          "cluster_id": 2369360,
          "cite": [
            "527 F. Supp. 256",
            "1981 U.S. Dist. LEXIS 16059"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109572) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 93,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 93,
        "triage_read": 2,
        "triage_snippet_classified": 91
      },
      "lane2_top_cited": {
        "query": "cites:(109572)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMiZzPTEyNDQxODImdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109572%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109572)",
        "reviewed": 1,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 1,
        "triage_read": 0,
        "triage_snippet_classified": 1
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109572)",
    "indexed_citing_opinions": 111,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109572,
        "count": 111,
        "count_source": "search"
      }
    ],
    "citation_count": 175,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/connally-v-georgia.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjIxMjc2NTMmcz0yOTc2OTU2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109572%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109572,
        "cited_id": 101031,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 101283,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 102105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 108582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 108629,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 1090898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 1296142,
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
    "date_created": "2026-07-05T00:52:15Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:52:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:52:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:56:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:52:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Connally v. Georgia

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b395-9">
  Per Curiam.
 </author>
<p id="b395-10">
  Appellant John Connally was indicted, tried, and convicted in the Superior Court of Walker County, Ga., for possession of marihuana in violation of the Georgia Controlled Substances Act, Ga. Code Ann. § 79A-801
  <em>
   et seq.
  </em>
  (1973). On his appeal to the Supreme Court of Georgia, he asserted trial error in four respects: the constitutional impropriety of the fee system governing the issuance of search warrants by justices of the peace in Georgia; the deprivation of his right of confrontation when revelation of an informer’s identity was refused; the failure to give a requested instruction on joint occupancy of premises; and the failure to enter a judgment of acquittal because of an alleged absence of proof of the type of cannabis involved. The Supreme Court of Georgia affirmed, with two justices dissenting (one on the first issue) and one justice concurring as to the second, third, and fourth issues and in the judgment. <span class="citation" data-id="9854792"><a href="/opinion/1296142/connally-v-state/" aria-description="Citation for case: Connally v. State">237 Ga. 203</a></span>, <span class="citation" data-id="9854792"><a href="/opinion/1296142/connally-v-state/" aria-description="Citation for case: Connally v. State">227 S. E. 2d 352</a></span> (1976). The appellant, on direct appeal here,
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  raises
  <span citation-index="1" class="star-pagination" label="246"> 
   *246
   </span>
  the first two questions. We deem the challenge to the warrant procedure worthy of consideration.
 </p>
<p id="b396-5">
  Pursuant to a search warrant issued by a justice of the peace, appellant's house was raided and marihuana found there was seized. Connally was arrested.. At his trial he moved to suppress the evidence so seized on the ground that the justice who had issued the warrant was not “a neutral and detached magistrate”
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  because he had a pecuniary interest in issuing the warrant. The trial court denied that motion, and the Supreme Court of Georgia, in affirming, rejected the constitutional challenge.
 </p>
<p id="b396-6">
  Under <span class="citation no-link">Ga. Code Ann. § 24-1601</span> (1971), the fee for the issuance of a search warrant by a Georgia justice of the peace “shall be” $5, “and it shall be lawful for said [justice] of the peace to charge and collect the same.” If the requested warrant is refused, the justice of the peace collects no fee for reviewing and denying the application. The fee so charged apparently goes into county funds and from there to the issuing justice as compensation.
 </p>
<p id="b396-7">
  At a pretrial hearing in Connally's case, the issuing justice testified on cross-examination that he was a justice primarily because he was “interested in a livelihood,” Record 502; that he received no salary,
  <em>
   ibid.;
  </em>
  that his compensation was “directly dependent on how many warrants” he issued,
  <em>
   ibid.;
  </em>
  that since January 1, 1973, he had issued “some 10,000” warrants for arrests or searches,
  <em>
   ibid.;
  </em>
  and that he had no legal background other than attendance at seminars and reading law,
  <span class="citation no-link"><em>
   id.,
  </em>
  at 506-508, 512-515</span>.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b397-4">
<span citation-index="1" class="star-pagination" label="247"> 
   *247
   </span>
  Fifty years ago, in
  <em>
   Tumey
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="101031"><a href="/opinion/101031/tumey-v-ohio/" aria-description="Citation for case: Tumey v. Ohio">273 U. S. 510</a></span> (1927), the Court considered state statutes that permitted a charge of violating the State’s prohibition laws to be tried without
  <span citation-index="1" class="star-pagination" label="248"> 
   *248
   </span>
  a jury before a village mayor. Any fine imposed was divided between the State and the village. The latter’s share was used to hire attorneys and detectives to arrest offenders and
  <span citation-index="1" class="star-pagination" label="249"> 
   *249
   </span>
  prosecute them before the mayor. When the mayor convicted, he received fees and costs, and these were in addition to his salary. The Court, in an opinion by Mr. Chief Justice Taft, unanimously held that subjecting a defendant to trial before a judge having “a direct, personal, pecuniary interest in convicting the defendant,” that is, in the $12 of fees and costs imposed,
  <span class="citation" data-id="101031"><a href="/opinion/101031/tumey-v-ohio/#523" aria-description="Citation for case: Tumey v. Ohio"><em>
   id.,
  </em>
  at 523, 531</a></span>, effected a denial of due process in violation of the Fourteenth Amendment.
 </p>
<p id="b399-6">
  This approach was reiterated in
  <em>
   Ward
  </em>
  v.
  <em>
   Village of Monroeville,
  </em>
  <span class="citation" data-id="9425043"><a href="/opinion/108629/ward-v-village-of-monroeville/" aria-description="Citation for case: Ward v. Village of Monroeville">409 U. S. 57</a></span> (1972). There, an Ohio statute authorized mayors to sit as judges of ordinance violations and certain traffic offenses. The petitioner was so convicted and fined by the mayor of Monroeville. Although the mayor had no direct personal financial stake in the outcome of cases before him, a major portion of the village’s income was derived from the fines, fees, and costs imposed in the mayor’s court. This Court,
  <span class="citation" data-id="9425043"><a href="/opinion/108629/ward-v-village-of-monroeville/#59" aria-description="Citation for case: Ward v. Village of Monroeville"><em>
   id.,
  </em>
  at 59-60</a></span>, cited
  <em>
   <span class="citation" data-id="101031"><a href="/opinion/101031/tumey-v-ohio/" aria-description="Citation for case: Tumey v. Ohio">Tumey</a></span>
  </em>
  and repeated the test formulated in that case, namely, “whether the may- or’s situation is one ‘which would offer a possible temptation to the average man as a judge to forget the burden of proof required to convict the defendant, or which might lead him not to hold the balance nice, clear and true between the State and the accused ....’” <span class="citation" data-id="9425043"><a href="/opinion/108629/ward-v-village-of-monroeville/#60" aria-description="Citation for case: Ward v. Village of Monroeville">409 U. S., at 60</a></span>.
  <em>
   Dugan
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="101283"><a href="/opinion/101283/dugan-v-ohio/" aria-description="Citation for case: Dugan v. Ohio">277 U. S. 61</a></span> (1928), where a mayor had judicial, functions but only “very limited executive authority,” and the executive power rested in a city manager and a commission, was distinguished as a situation where “the Mayor’s relationship to the finances and financial policy of the city was too remote to warrant a presumption of bias toward conviction in prosecutions before him as [a] judge,” <span class="citation" data-id="9425043"><a href="/opinion/108629/ward-v-village-of-monroeville/#60" aria-description="Citation for case: Ward v. Village of Monroeville">409 U. S., at 60-61</a></span>,
  <span citation-index="1" class="star-pagination" label="250"> 
   *250
   </span>
  and the possibility of a later
  <em>
   de novo
  </em>
  trial in another court was held to be of no constitutional relevance because the defendant was “entitled to a neutral and detached judge in the first instance.”
  <span class="citation" data-id="9425043"><a href="/opinion/108629/ward-v-village-of-monroeville/#61" aria-description="Citation for case: Ward v. Village of Monroeville"><em>
   Id.,
  </em>
  at 61-62</a></span>.
 </p>
<p id="b400-5">
  The present case, of course, is not precisely the same as
  <em>
   <span class="citation" data-id="101031"><a href="/opinion/101031/tumey-v-ohio/" aria-description="Citation for case: Tumey v. Ohio">Tumey</a></span>
  </em>
  or as
  <em>
   <span class="citation" data-id="9425043"><a href="/opinion/108629/ward-v-village-of-monroeville/" aria-description="Citation for case: Ward v. Village of Monroeville">Ward</a></span>,
  </em>
  but the principle of those cases, we conclude, is applicable to the Georgia system for the issuance of search warrants by justices of the peace. The justice is not salaried. He is paid, so far as search warrants are concerned, by receipt of the fee prescribed by statute for his
  <em>
   issuance
  </em>
  of the warrant, and he receives nothing for his
  <em>
   denial
  </em>
  of the warrant. His financial welfare, therefore, is enhanced by positive action and is not enhanced by negative action. The situation, again, is one which offers “a possible temptation to the average man as a judge ... or which might lead him not to hold the balance nice, clear and true between the State and the accused.” It is, in other words, another situation where the defendant is subjected to what surely is judicial action by an officer of a court who has “a direct, personal, substantial, pecuniary interest” in his conclusion to issue or to deny the warrant. See
  <em>
   Bennett
  </em>
  v.
  <em>
   Cottingham,
  </em>
  <span class="citation" data-id="2147032"><a href="/opinion/2147032/bennett-v-cottingham/#762" aria-description="Citation for case: Bennett v. Cottingham">290 F. Supp. 759, 762-763</a></span> (ND Ala. 1968), aff’d, <span class="citation multiple-matches"><a href="/c/U.%20S./393/317/">393 U. S. 317</a></span> (1969).
 </p>
<p id="b400-6">
<em>
   Shadwick
  </em>
  v.
  <em>
   City of Tampa,
  </em>
  <span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/" aria-description="Citation for case: Shadwick v. City of Tampa">407 U. S. 345</a></span> (1972), does not weigh to the contrary. The issue there centered in the qualification of municipal court clerks to issue arrest warrants for breaches of ordinances. The Court held that the clerks, although laymen, worked within the judicial branch under the supervision of judges and were qualified to determine the existence of probable cause. They were, therefore, “neutral and detached magistrates for purposes of the Fourth Amendment.”
  <span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/#346" aria-description="Citation for case: Shadwick v. City of Tampa"><em>
   Id.,
  </em>
  at 346</a></span>. There was no element of personal financial gain in the clerks’ issuance or nonissuance of arrest warrants. Cf.
  <em>
   Coolidge
  </em>
  v.
  <em>
   New Hampshire,
  </em>
  <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#449" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 449-453</a></span> (1971).
 </p>
<p id="b401-4">
<span citation-index="1" class="star-pagination" label="251"> 
   *251
   </span>
  We disagree with the Supreme Court of Georgia’s rulings, <span class="citation" data-id="9854792"><a href="/opinion/1296142/connally-v-state/#205" aria-description="Citation for case: Connally v. State">237 Ga., at 205-206</a></span>, <span class="citation" data-id="9854792"><a href="/opinion/1296142/connally-v-state/#354" aria-description="Citation for case: Connally v. State">227 S. E. 2d, at 354-355</a></span>, that the amount of the search warrant fee is
  <em>
   de minimis
  </em>
  in the present context, that the unilateral character of the justice’s adjudication of probable cause distinguishes the present case from
  <em>
   Turney,
  </em>
  and that, instead, this case equates with
  <em>
   Bevan
  </em>
  v.
  <em>
   Krieger,
  </em>
  <span class="citation" data-id="102105"><a href="/opinion/102105/bevan-v-krieger/#465" aria-description="Citation for case: Bevan v. Krieger">289 U. S. 459, 465-466</a></span> (1933), where a notary public’s fee for taking a deposition was measured by the folios of testimony taken.
 </p>
<p id="b401-5">
  We therefore hold that the issuance of the search warrant by the justice of the peace in Connally’s case effected a violation of the protections afforded him by the Fourth and Fourteenth Amendments of the United States Constitution. The judgment of the Supreme Court of Georgia is vacated, and the case is remanded for further proceedings not inconsistent with this opinion.
 </p>
<p id="b401-6">
<em>
   So ordered.
  </em>
</p>



<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b395-11">
   Cf.
   <em>
    Stone
   </em>
   v.
   <em>
    Powell,
   </em>
   <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U. S. 465</a></span> (1976).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b396-8">
   See
   <em>
    Johnson
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948);
   <em>
    Coolidge
   </em>
   v.
   <em>
    New Hampshire,
   </em>
   <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#453" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 453</a></span> (1971);
   <em>
    Shadwick
   </em>
   v.
   <em>
    City of Tampa,
   </em>
   <span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/#350" aria-description="Citation for case: Shadwick v. City of Tampa">407 U. S. 345, 350</a></span> (1972).
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b396-9">
   “Q In the case of a search warrant, I believe you receive compensation ultimately in the amount of $5.00, if you issue the warrant, do you not?
  </p>
<p id="b396-10">
   “A That’s true.
  </p>
<p id="b397-5">
<span citation-index="1" class="star-pagination" label="247"> 
    *247
    </span>
   “Q If you choose not to issue the warrant, what compensation do you receive?
  </p>
<p id="b397-6">
   “A I don’t know.
  </p>
<p id="b397-7">
   “Q You receive no compensation?
  </p>
<p id="b397-8">
   “A Well, I never have, I’ll put it that way.
  </p>
<p id="b397-9">
   “Q Now with respect to issuing the search warrant, Mr. Murphy, does the $5.00, since that’s the only way you get paid, does that enter your mind when you’re sitting there contemplating whether or not to issue a search warrant?
  </p>
<p id="b397-10">
   “A It has.
  </p>
<p id="b397-11">
   “Q As a matter of fact, I believe you quite honestly and candidly told me on the day we had that preliminary hearing up here, I believe that was on, the best I can recall, it was on the 18th of May, that you would be a liar if you said it didn’t enter your mind?
  </p>
<p id="b397-12">
   “A That’s what I said.
  </p>
<p id="b397-13">
   “Q Is that true now, you would be [a] liar if you said it didn’t enter your mind?
  </p>
<p id="b397-14">
   “A It’s only human nature to me.
  </p>
<p id="b397-15">
   “Q Okay. Now, I believe you said you had been a J. P. since January 1st of 1973, is that correct?
  </p>
<p id="b397-16">
<em>
    “A
   </em>
   Yes, sir.
  </p>
<p id="b397-17">
   “Q All right. Now, since January — you have to run for that office, or is it an appointed office?
  </p>
<p id="b397-18">
   “A Yes sir, it’s an elected office.
  </p>
<p id="b397-19">
   “Q Well, you ran for the office for the purpose of having employment and earning a living, is that correct?
  </p>
<p id="b397-20">
   “A That’s part of it.
  </p>
<p id="b397-21">
   “Q Of course, you like in other people’s motivations, primarily you were interested in a livelihood?
  </p>
<p id="b397-22">
   “A True.
  </p>
<p id="b397-23">
   “Q Now do you support yourself with the salary or with the fees that you receive in a J. P. system down here, or as J. P.?
  </p>
<p id="b397-24">
<em>
    “A
   </em>
   Uh huh, yes sir.
  </p>
<p id="b397-25">
   “Q And you receive no salary at all, so that your compensation is directly dependent on how many warrants you issue, is that correct?
  </p>
<p id="b398-5">
<span citation-index="1" class="star-pagination" label="248"> 
    *248
    </span>
<em>
    “A
   </em>
   That’s right.
  </p>
<p id="b398-6">
   “Q Now, since January 1st, 1973, I
   <em>
    believe you
   </em>
   told me the
   <em>
    other
   </em>
   day, and let me ask you again, you have issued some 10,000 warrants of the arrest — either arrest or search warrants, is that correct?
  </p>
<p id="b398-7">
   “A That’s pretty close, total warrants.
  </p>
<p id="b398-8">
   “Q Okay. Total warrants?
  </p>
<p id="b398-9">
   “A Criminal warrants.
  </p>
<p id="b398-10">
   “Q That would be right about 10,000 of them?
  </p>
<p id="b398-11">
<em>
    “A
   </em>
   Uh huh.
  </p>
<p id="b398-12">
   “Q Now with respect to the qualifications that you have for your office, of course, the people of Walker County elected you and under the law that would qualify you, but I believe the law prescribes some qualifications that you must have prior to the time you are elected, what are those qualifications?
  </p>
<p id="b398-13">
   “A You have to be a resident of the militia district in which you’re running for that office, registered voter, it might sound stupid but that’s all I remember.
  </p>
<p id="b398-14">
   “Q Okay. Now of course, the people have selected you as the J. P. for this militia district, and you have the qualifications that you mentioned that you are a resident and of age and so on and so forth, other than those, do you have any background, legal background or other background with respect to the instruments and issuance of warrants?
  </p>
<p id="b398-15">
<em>
    “A
   </em>
   No, sir.
  </p>
<p id="b398-16">
   “Q So, the qualifications that you have mentioned are your sole qualifications for holding your job, is that correct?
  </p>
<p id="b398-17">
   “A That’s right.
  </p>
<p id="b398-18">
   “Q Okay.
  </p>
<p id="b398-19">
   “A Up to the time I was elected.
  </p>
<p id="b398-20">
   "MR. DANIEL: Okay, sir, that’s all I have.
  </p>
<p id="b398-21">
   “THE COURT: Have you done anything since you were elected to improve any qualifications that might be necessary?
  </p>
<p id="b398-22">
   “THE WITNESS: Yes, sir.
  </p>
<p id="b398-23">
   “THE COURT: What have you done?
  </p>
<p id="b398-24">
   “THE WITNESS: I have attended several training seminars sponsored by our J. P. State Association, as a matter of fact, I’m leaving
   <span citation-index="1" class="star-pagination" label="249"> 
    *249
    </span>
   this afternoon if I can get out of here to go to a 2-day training seminar in Warner Robbins, Georgia, sponsored by the same State Association.
  </p>
<p id="b399-8">
   “I’ve bought one manual, study course from Judson-Pace at my own expense and attempted to learn a little bit more about the duties.” Record 499-500, 501-502, 506-508.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Connecticut v. Barrett.md  (`case`, 5 assertions)

### content_page

```
---
title: "Connecticut v. Barrett"
type: case
citation: "479 U.S. 523 (1987)"
parallel_cite: "107 S. Ct. 828; 93 L. Ed. 2d 920; 55 U.S.L.W. 4151"
neutral_cite: 1987 U.S. LEXIS 419
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-01-27
docket: 85-899
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-01-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Connecticut v. Barrett
  varies_by_point: false
  scope_note: Good law.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111796/connecticut-v-barrett/"
  cluster_id: 111796
  opinion_id: 111796
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny"
related: ["[[Edwards v. Arizona]]", "[[Smith v. Illinois]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "invocation", "right-to-counsel"]
holding: "A suspect may make a limited invocation of counsel; where he refuses to give a written statement without a lawyer but affirmatively agrees to talk orally, that limited request does not bar oral interrogation — courts honor the scope of the invocation as the suspect framed it."
lake:
  record_id: Connecticut v. Barrett
  status: verified
  projected_at: 2026-07-06
---

# Connecticut v. Barrett

*479 U.S. 523 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After [[Miranda and Custodial Interrogation|Miranda warnings]], Barrett told police he would not give a *written* statement without a lawyer present, but that he was willing to talk about the incident *orally*. The police took his oral statements without counsel. The Connecticut Supreme Court treated his refusal to give a written statement as an invocation of counsel barring all interrogation and suppressed the oral statements.

## Issue
Whether a suspect who refuses to make a written statement without counsel, but agrees to speak orally, has invoked his right to counsel so as to bar all further interrogation under *[[Edwards v. Arizona]]*.

## Rule
No. The right to counsel may be invoked in a limited way, and authorities may honor the limits the suspect himself sets. "Nothing in our decisions, however, or in the rationale of *Miranda*, requires authorities to ignore the tenor or sense of a defendant's response to these warnings." — 479 U.S. at 528. ^pin-528

Barrett's "limited requests for counsel ... were accompanied by affirmative announcements of his willingness to speak with the authorities," so taking his oral confession "is quite consistent with the Fifth Amendment. *Miranda* gives the defendant a right to choose between speech and silence, and Barrett chose to speak." — *Id.* at 529. ^pin-529

## Application
Barrett drew his own line: counsel for a written statement, but a willingness to talk orally. That was not a blanket invocation triggering *[[Edwards v. Arizona|Edwards]]*'s bar on all questioning. Because his decision to speak orally was a voluntary waiver and he was not "threatened, tricked, or cajoled," the police permissibly took his oral statements. The Connecticut court erred by construing his limited request as an all-purpose invocation.

## Conclusion
A limited invocation is honored as made; Barrett's oral statements were admissible. The Connecticut Supreme Court's suppression was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Barrett* complements [[Edwards v. Arizona]] and [[Smith v. Illinois]]: an invocation must be respected, but its **scope** is set by the suspect's own words; a partial invocation does not automatically bar all questioning.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny*

## Sources
- *Connecticut v. Barrett*, 479 U.S. 523 (1987) — https://www.courtlistener.com/opinion/111796/connecticut-v-barrett/ — pinpoints: 528, 529.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3c23a6c8c9c98dfe", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "479 U.S. 523 (1987)", "court": "U.S. Supreme Court", "neutral_cite": "1987 U.S. LEXIS 419", "official_citation_present": true, "parallel_cite": "107 S. Ct. 828; 93 L. Ed. 2d 920; 55 U.S.L.W. 4151", "title": "Connecticut v. Barrett", "year": "1987"}}
{"assertion_id": "7689029d77b27f99", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny", "title": "Connecticut v. Barrett"}}
{"assertion_id": "b5bd6d52ae68fc28", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A suspect may make a limited invocation of counsel; where he refuses to give a written statement without a lawyer but affirmatively agrees to talk orally, that limited request does not bar oral interrogation — courts honor the scope of the invocation as the suspect framed it.", "title": "Connecticut v. Barrett"}}
{"assertion_id": "b690e575e47f246a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1987-01-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Connecticut v. Barrett", "field_i_validity": "good_law", "scope_note": "Good law.", "title": "Connecticut v. Barrett", "varies_by_point": "false"}}
{"assertion_id": "e7b11a84aa4ffcdb", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Connecticut v. Barrett"}}
```

### lake record — Connecticut v. Barrett

```json
{
  "schema_version": "s2.v1",
  "record_id": "Connecticut v. Barrett",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Connecticut v. Barrett",
    "case_name_short": "Barrett",
    "case_name_full": "Connecticut v. Barrett",
    "input_case_name": "Connecticut v. Barrett",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-01-27",
    "year": 1987,
    "docket": "85-899",
    "cluster_id": 111796,
    "lead_opinion_id": 111796,
    "sibling_ids": [
      111796,
      9430786,
      9430787,
      9430788
    ],
    "absolute_url": "/opinion/111796/connecticut-v-barrett/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "479 U.S. 523",
      "volume": "479",
      "reporter": "U.S.",
      "page": "523",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 828",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "828",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 920",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "920",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4151",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4151",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 419",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "419",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "479 U.S. 523",
        "volume": "479",
        "reporter": "U.S.",
        "page": "523",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 828",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "828",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 920",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "920",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 419",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "419",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4151",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4151",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "479 U.S. 523",
    "official_selection": {
      "court_class": "scotus",
      "selected": "479 U.S. 523",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-528",
      "page": null,
      "quote": "--- # Connecticut v. Barrett *479 U.S. 523 (1987)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After Miranda warnings, Barrett told police he would not give a *written* statement without a lawyer present, but that he was willing to talk about the incident *orally*. The police took his oral statements without counsel. The Connecticut Supreme Court treated his refusal to give a written statement as an invocation of counsel barring all interrogation and suppressed the oral statements. ## Issue Whether a suspect who refuses to make a written statement without counsel, but agrees to speak orally, has invoked his right to counsel so as to bar all further interrogation under *Edwards v. Arizona*. ## Rule No. The right to counsel may be invoked in a limited way, and authorities may honor the limits the suspect himself sets.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-529",
      "page": null,
      "quote": "limited requests for counsel ... were accompanied by affirmative announcements of his willingness to speak with the authorities,",
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
    "composite_basis_ref": "Connecticut v. Barrett",
    "varies_by_point": false,
    "scope_note": "Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Tellez-Suarez",
          "cluster_id": 10134379,
          "cite": [
            "312 Or. App. 531",
            "493 P.3d 28"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. DeJong",
          "cluster_id": 2669581,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Plugh",
          "cluster_id": 2496,
          "cite": [
            "576 F.3d 135",
            "2009 U.S. App. LEXIS 16979",
            "2009 WL 2341966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robin Lynn Anderson v. State",
          "cluster_id": 2850439,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dickerson",
          "cluster_id": 2967209,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Larry Winsett v. Odie Washington, Warden of Dixon Correctional Center",
          "cluster_id": 748614,
          "cite": [
            "130 F.3d 269",
            "1997 U.S. App. LEXIS 32286",
            "1997 WL 716044"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cothren v. State",
          "cluster_id": 1913446,
          "cite": [
            "705 So. 2d 849",
            "1997 WL 15337"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Hendricks",
          "cluster_id": 6130812,
          "cite": [
            "222 A.D.2d 74",
            "646 N.Y.S.2d 845",
            "1996 N.Y. App. Div. LEXIS 8596"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cooper v. Dupnik",
          "cluster_id": 9008075,
          "cite": [
            "963 F.2d 1220",
            "1992 WL 88704"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dinkins v. State",
          "cluster_id": 1688238,
          "cite": [
            "894 S.W.2d 330",
            "1995 Tex. Crim. App. LEXIS 9",
            "1995 WL 40331"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1801669,
          "cite": [
            "49 Cal. 4th 405",
            "2010 D.A.R. 10",
            "111 Cal. Rptr. 3d 589",
            "233 P.3d 1000",
            "2010 Cal. LEXIS 5970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1407706,
          "cite": [
            "14 Cal. 4th 1005",
            "929 P.2d 544",
            "97 Daily Journal DAR 899",
            "97 Cal. Daily Op. Serv. 520",
            "60 Cal. Rptr. 2d 225",
            "1997 Cal. LEXIS 9"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Martinez",
          "cluster_id": 2637824,
          "cite": [
            "47 Cal. 4th 911",
            "10 Cal. Daily Op. Serv. 583",
            "224 P.3d 877",
            "105 Cal. Rptr. 3d 131",
            "2010 Cal. LEXIS 111"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Sully",
          "cluster_id": 1386747,
          "cite": [
            "812 P.2d 163",
            "53 Cal. 3d 1195",
            "283 Cal. Rptr. 144",
            "91 Cal. Daily Op. Serv. 5489",
            "1991 Cal. LEXIS 2977"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Green",
          "cluster_id": 1730571,
          "cite": [
            "655 So. 2d 272",
            "1995 WL 312446"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 1654613,
          "cite": [
            "760 N.W.2d 35",
            "277 Neb. 37"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gerald",
          "cluster_id": 2260422,
          "cite": [
            "549 A.2d 792",
            "113 N.J. 40",
            "83 A.L.R. 4th 331",
            "1988 N.J. LEXIS 107"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alvarado v. State",
          "cluster_id": 2450595,
          "cite": [
            "853 S.W.2d 17",
            "1993 Tex. Crim. App. LEXIS 70",
            "1993 WL 89307"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hunter",
          "cluster_id": 1659158,
          "cite": [
            "840 S.W.2d 850",
            "1992 WL 308879"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Thomas",
          "cluster_id": 844168,
          "cite": [
            "54 Cal. 4th 908",
            "281 P.3d 361",
            "144 Cal. Rptr. 3d 366",
            "2012 WL 3043901",
            "2012 Cal. LEXIS 7089"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hooks v. State",
          "cluster_id": 1765577,
          "cite": [
            "534 So. 2d 329"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. State",
          "cluster_id": 1775207,
          "cite": [
            "779 S.W.2d 417",
            "1989 Tex. Crim. App. LEXIS 185",
            "1989 WL 122612"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Montez",
          "cluster_id": 1345733,
          "cite": [
            "789 P.2d 1352",
            "309 Or. 564",
            "1990 Ore. LEXIS 68"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Murray",
          "cluster_id": 1824177,
          "cite": [
            "827 So. 2d 488",
            "2002 WL 1980814"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111796 OR 9430786 OR 9430787 OR 9430788) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MDUwMjQwMDAwMDAmcz01ODM0NDcmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111796+OR+9430786+OR+9430787+OR+9430788%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111796 OR 9430786 OR 9430787 OR 9430788)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTAmcz03NDg2MTQmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111796+OR+9430786+OR+9430787+OR+9430788%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111796 OR 9430786 OR 9430787 OR 9430788)",
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
    "complete_query": "cites:(111796 OR 9430786 OR 9430787 OR 9430788)",
    "indexed_citing_opinions": 362,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111796,
        "count": 325,
        "count_source": "search"
      },
      {
        "opinion_id": 9430786,
        "count": 48,
        "count_source": "search"
      },
      {
        "opinion_id": 9430787,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430788,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 572,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/connecticut-v-barrett.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY2MDcyMiZzPTQ2OTM0NDgmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28111796+OR+9430786+OR+9430787+OR+9430788%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111796,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 110065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 110987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 111288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 444143,
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
    "date_created": "2026-07-05T00:56:06Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:56:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:56:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T01:01:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:56:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Connecticut v. Barrett

```
<div>
<center><b><span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/" aria-description="Citation for case: Connecticut v. Barrett">479 U.S. 523</a></span> (1987)</b></center>
<center><h1>CONNECTICUT<br>
v.<br>
BARRETT</h1></center>
<center>No. 85-899.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 9, 1986</center>
<center>Decided January 27, 1987</center>
CERTIORARI TO THE SUPREME COURT OF CONNECTICUT
<p><span class="star-pagination">*524</span> <i>Julia DiCocco Dewey,</i> Assistant State's Attorney of Connecticut, argued the cause and filed a brief for petitioner.</p>
<p><i>Charles A. Rothfeld</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Fried, Assistant Attorney General Trott,</i> and <i>Deputy Solicitor General Bryson.</i></p>
<p><i>Robert L. Genuario</i> argued the cause for respondent. With him on the brief was <i>John F. Kavanewsky, Jr.</i><sup>[*]</sup></p>
<p><span class="star-pagination">*525</span> CHIEF JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>Respondent William Barrett was convicted after a jury trial of sexual assault, unlawful restraint, and possession of a controlled substance. The Connecticut Supreme Court reversed the convictions. It held that incriminating statements made by Barrett should have been suppressed under our decision in <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981), because Barrett, though stating his willingness to speak to police, had indicated that he would not make a written statement outside the presence of counsel. <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/" aria-description="Citation for case: State v. Barrett">197 Conn. 50</a></span>, <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/" aria-description="Citation for case: State v. Barrett">495 A. 2d 1044</a></span> (1985). We granted certiorari to consider the federal constitutional issues presented by this holding. <span class="citation multiple-matches"><a href="/c/U.%20S./476/1114/">476 U. S. 1114</a></span> (1986). We reverse.</p>
<p>In the early morning of October 24, 1980, Barrett was transported from New Haven, Connecticut, to Wallingford, where he was a suspect in a sexual assault that had occurred the previous evening. Upon arrival at the Wallingford police station, Officer Peter Cameron advised Barrett of his rights, and Barrett signed and dated an acknowledgment that he had received the warnings required by <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Barrett stated that "he would not give the police any written statements but he had no problem in talking about the incident." App. 12A.</p>
<p>Approximately 30 minutes later, Barrett was questioned by Officer Cameron and Officer John Genovese. Before this questioning, he was again advised of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights and signed a card acknowledging that he had been read the rights. Respondent stated that he understood his rights, and told the officers that he would not give a written statement unless his attorney was present but had "no problem" talking about the incident. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span></i> at 21A. Barrett then gave an oral statement admitting his involvement in the sexual assault.</p>
<p>After discovering that a tape recorder used to preserve the statement had malfunctioned, the police conducted a second <span class="star-pagination">*526</span> interview. For the third time, Barrett was advised of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights by the Wallingford police, and once again stated that "he was willing to talk about [the incident] verbally but he did not want to put anything in writing until his attorney came." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span></i> at 44A. He then repeated to the police his confession regarding the previous evening's events.</p>
<p>When the officers discovered that their tape recorder had again failed to record the statement, Officer Cameron reduced to writing his recollection of respondent's statement.</p>
<p>The trial court, after a suppression hearing, held that the confession was admissible. It found that respondent not only indicated that he understood the warnings, but also "offered the statements that he did not need anything explained to him because he understood. So it was not merely a passive acquiescence . . . ." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span></i> at 70A. Barrett's decision to make no written statement without his attorney "indicate[d] to the Court that he certainly understood from having his rights read to him that . . . he was under no obligation to give any statement." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> The court held that Barrett had voluntarily waived his right to counsel and thus allowed testimony at trial as to the content of Barrett's statement. Barrett took the stand in his own defense and testified that he had understood his rights as they were read to him. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span></i> at 130A. He was convicted and sentenced to a prison term of 9 to 18 years.</p>
<p>The Connecticut Supreme Court reversed the conviction, holding that respondent had invoked his right to counsel by refusing to make written statements without the presence of his attorney. In the court's view, Barrett's expressed desire for counsel before making a written statement served as an invocation of the right for all purposes:</p>
<blockquote>"The fact that the defendant attached his request for counsel to the making of a written statement does not affect the outcome of . . . our inquiry. No particular form of words has ever been required to trigger an individual's fifth amendment protections; nor have requests for <span class="star-pagination">*527</span> counsel been narrowly construed. The defendant's refusal to give a written statement without his attorney present was a clear request for the assistance of counsel to protect his rights in his dealings with the police. Such a request continues to be constitutionally effective despite the defendant's willingness to make oral statements. We conclude, therefore, that the defendant did invoke his right to counsel under the fifth and fourteenth amendments." <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#57" aria-description="Citation for case: State v. Barrett">197 Conn., at 57</a></span>, <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#1049" aria-description="Citation for case: State v. Barrett">495 A. 2d, at 1049</a></span> (citations omitted).</blockquote>
<p>This invocation, the court believed, brought the case within what it called the "bright-line rule for establishing a waiver of this right." <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#58" aria-description="Citation for case: State v. Barrett"><i>Id.,</i> at 58</a></span>, <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#1049" aria-description="Citation for case: State v. Barrett">495 A. 2d, at 1049</a></span>. That rule requires a finding that the suspect "(a) initiated further discussions with the police, and (b) knowingly and intelligently waived the right he had invoked." <i>Smith</i> v. <i>Illinois,</i> <span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#95" aria-description="Citation for case: Smith v. Illinois">469 U. S. 91, 95</a></span> (1984) <i>(per curiam)</i><i>.</i> See also <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#485" aria-description="Citation for case: Edwards v. Arizona"><i>Edwards, supra,</i> at 485, 486, n. 9</a></span>. Because Barrett had not initiated further discussions with police, the court found his statement improperly admitted.</p>
<p>We think that the Connecticut Supreme Court erred in holding that the United States Constitution required suppression of Barrett's statement. Barrett made clear to police his willingness to talk about the crime for which he was a suspect. The trial court found that this decision was a voluntary waiver of his rights, and there is no evidence that Barrett was "threatened, tricked, or cajoled" into this waiver. <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#476" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 476</a></span>. The Connecticut Supreme Court nevertheless held as a matter of law<sup>[1]</sup> that respondent's <span class="star-pagination">*528</span> limited invocation of his right to counsel prohibited all interrogation absent initiation of further discussion by Barrett. Nothing in our decisions, however, or in the rationale of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> requires authorities to ignore the tenor or sense of a defendant's response to these warnings.</p>
<p>The fundamental purpose of the Court's decision in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was "to assure that <i>the individual's right to choose</i> between speech and silence remains unfettered throughout the interrogation process." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#469" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 469</a></span> (emphasis added). See also <i>Moran</i> v. <i>Burbine,</i> <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#426" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 426</a></span> (1986) ("<i>Miranda</i> attempted to reconcile [competing] concerns by giving the <i>defendant</i> the power to exert some control over the course of the interrogation") (emphasis in original); <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#308" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 308</a></span> (1985) ("Once warned, the suspect is free to exercise <i>his own volition</i> in deciding whether or not to make a statement to the authorities") (emphasis added). To this end, the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> Court adopted prophylactic rules designed to insulate the exercise of Fifth Amendment rights from the government "compulsion, subtle or otherwise," that "operates on the individual to overcome free choice in producing a statement after the privilege has been once invoked." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda, supra,</i> at 474</a></span>. See also <span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#98" aria-description="Citation for case: Smith v. Illinois"><i>Smith, supra,</i> at 98</a></span>; <i>Oregon</i> v. <i>Bradshaw,</i> <span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1044" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S. 1039, 1044</a></span> (1983). One such rule requires that, once the accused "states that he wants an attorney, the interrogation must cease until an attorney is present." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda, supra,</i> at 474</a></span>. See also <i>Edwards,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484</a></span>. It remains clear, however, that this prohibition on further questioning  like other aspects of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>  is not itself required by the Fifth Amendment's prohibition on coerced confessions, but is instead justified only by reference to its prophylactic purpose. See <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles">467 U. S. 649, 654</a></span> (1984). By prohibiting further interrogation after the invocation of these rights, we erect an auxiliary barrier against police coercion.</p>
<p><span class="star-pagination">*529</span> But we know of no constitutional objective that would be served by suppression in this case. It is undisputed that Barrett desired the presence of counsel before making a written statement. Had the police obtained such a statement without meeting the waiver standards of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>,</i> it would clearly be inadmissible.<sup>[2]</sup> Barrett's limited requests for counsel, however, were accompanied by affirmative announcements of his willingness to speak with the authorities. The fact that officials took the opportunity provided by Barrett to obtain an oral confession is quite consistent with the Fifth Amendment. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> gives the defendant a right to choose between speech and silence, and Barrett chose to speak.</p>
<p>The Connecticut Supreme Court's decision to the contrary rested on the view that requests for counsel are not to be narrowly construed. <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#57" aria-description="Citation for case: State v. Barrett">197 Conn., at 57</a></span>, <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#1049" aria-description="Citation for case: State v. Barrett">495 A. 2d, at 1049</a></span>. In support of this premise, respondent observes that our prior decisions have given broad effect to requests for counsel that were less than all-inclusive. See <span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1041" aria-description="Citation for case: Oregon v. Bradshaw"><i>Bradshaw, supra,</i> at 1041-1042</a></span> ("I do want an attorney before it goes very much further"); <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#479" aria-description="Citation for case: Edwards v. Arizona"><i>Edwards, supra,</i> at 479</a></span> ("I want an attorney before making a deal"). We do not denigrate the "settled approach to questions of waiver [that] requires us to give a broad, rather than a narrow, interpretation to a defendant's request for counsel," <i>Michigan</i> v. <i>Jackson,</i> <span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#633" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625, 633</a></span> (1986), when we observe that this approach does little to aid respondent's cause. Interpretation is only required where the defendant's words, understood as ordinary people would understand them, are ambiguous. Here, however, Barrett made clear his intentions, and they were honored by police.<sup>[3]</sup> To conclude that respondent invoked his right to <span class="star-pagination">*530</span> counsel for all purposes requires not a broad interpretation of an ambiguous statement, but a disregard of the ordinary meaning of respondent's statement.</p>
<p>We also reject the contention that the distinction drawn by Barrett between oral and written statements indicates an understanding of the consequences so incomplete that we should deem his limited invocation of the right to counsel effective for all purposes. This suggestion ignores Barrett's testimony  and the finding of the trial court not questioned by the Connecticut Supreme Court  that respondent fully understood the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. These warnings, of course, made clear to Barrett that "[i]f you talk to any police officers, anything you say can and will be used against you in court." App. at 48A. The fact that some might find Barrett's decision illogical<sup>[4]</sup> is irrelevant, for we have never "embraced the theory that a defendant's ignorance of the full consequences of his decisions vitiates their voluntariness." <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#316" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 316</a></span>; <i>Colorado</i> v. <i>Spring, post,</i> p. 564.</p>
<p>For the reasons stated, the judgment of the Connecticut Supreme Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE BRENNAN, concurring in the judgment.</p>
<p>I concur in the judgment that the Constitution does not require the suppression of Barrett's statements to the police, but for reasons different from those set forth in the opinion of the Court. Barrett's contemporaneous waiver of his right to silence and limited invocation of his right to counsel (for the <span class="star-pagination">*531</span> purpose of making a written statement) suggested that he did not understand that anything he <i>said</i> could be used against him. However, the State eliminated this apparent ambiguity when it demonstrated that Barrett's waiver of his right to silence was voluntary, knowing, and intelligent. Barrett testified at trial that he understood his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, <i>i. e.,</i> he knew that he need not talk to the police without a lawyer present and that anything he said could be used against him. Under these circumstances, the waiver of the right to silence and the limited invocation of the right to counsel were valid.</p>
<p></p>
<h2>I</h2>
<p>In <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), the Court held that custodial interrogation is inherently coercive and that a defendant must receive detailed warnings that he or she has the rights to remain silent and to receive assistance of counsel before and during questioning. A statement obtained from a defendant during custodial interrogation is admissible only if the State carries its "heavy burden" of establishing that a defendant has executed a valid waiver of the privilege against self-incrimination and the right to counsel. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 475</a></span>. To do so, the State must demonstrate "an intentional relinquishment or abandonment of a known right or privilege." <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 464</a></span> (1938); see <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda, supra,</i> at 475-479</a></span>. In making this determination, courts must examine "the particular facts and circumstances surrounding that case, including the background, experience, and conduct of the accused." <i>Johnson</i> v. <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst"><i>Zerbst, supra,</i> at 464</a></span>.</p>
<p>The language and tenor of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion suggested that the Court would require that a waiver of the rights at stake be "specifically made." See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#470" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 470</a></span>. While the Court retreated from that position in <i>North Carolina</i> v. <i>Butler,</i> <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#373" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369, 373</a></span> (1979), I continue to believe that the Court should require the police to obtain an " `affirmative waiver' " of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights before proceeding with interrogation. <span class="star-pagination">*532</span> See <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">id.,</a></span></i> at 377 (quoting <i>Carnley</i> v. <i>Cochran,</i> <span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/#516" aria-description="Citation for case: Carnley v. Cochran">369 U. S. 506, 516</a></span> (1962)).</p>
<p>In this case, Barrett affirmatively waived his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. Unlike the defendant in <i><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span>,</i> Barrett orally expressed his willingness to talk with the police <i>and</i> willingly signed a form indicating that he understood his rights. The police obtained an explicit oral waiver of the right to silence. Furthermore, the officer who administered the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings to Barrett testified that the latter understood his rights "[c]ompletely": "I asked [Barrett] several times during my administration of those rights, if, in fact, he understood them; if there were points he wanted me to clarify, and he indicated to me, no, he understood everything fairly well." Tr. 452. At trial, one issue was whether Barrett voluntarily, knowingly, and intelligently waived his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, and Barrett himself testified that he understood his rights as they were read to him. <i>Id.,</i> at 879-880.<sup>[1]</sup></p>
<p>Had the State been without Barrett's testimony at trial, where he was represented by counsel, I could not reach this conclusion. Barrett's statement to police  that he would talk to them, but allow nothing in writing without counsel  created doubt about whether he actually understood that anything he <i>said</i> could be used against him. In other words, the statement is not, on its face, a knowing and intelligent waiver of the right to silence.<sup>[2]</sup> As a general matter, I believe <span class="star-pagination">*533</span> that this odd juxtaposition (a willingness to talk and an unwillingness to have anything preserved) militates against finding a knowing or intelligent waiver of the right to silence. See <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#378" aria-description="Citation for case: North Carolina v. Butler"><i>Butler, supra,</i> at 378</a></span> ("[T]here is no reason to believe that [the defendant's] oral statements, which followed a refusal to sign a written waiver form, were intended to signify relinquishment of his rights").<sup>[3]</sup> But Barrett's testimony revealed that he understood that he had rights to remain silent and to have an attorney present, and that anything he said could be used against him; nevertheless he chose to speak.</p>
<p>In sum, the State has carried its "heavy burden" of demonstrating waiver. It has shown that Barrett received the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, that he had the capacity to understand them<sup>[4]</sup> and <i>in fact</i> understood them, and that he expressly <span class="star-pagination">*534</span> waived his right to silence, saying that he "had no problem in talking about the incident." Tr. 452; see also <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#461" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 461-462, 490-491, 674</a></span>. In my view, each of these findings was essential to the conclusion that a voluntary, knowing, and intelligent waiver of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights occurred.</p>
<p></p>
<h2>II</h2>
<p>Barrett argues that his refusal to make a written statement without an attorney present constituted an invocation of the right to counsel for all purposes and that any further interrogation after this mention of his desire for an attorney was impermissible under <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981). It is settled that any plain reference, however glancing, to a need or a desire for representation must result in the cessation of questioning. See <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444-445</a></span> (questioning must cease when the accused "indicates in any manner and at any stage of the process that he wishes to consult with an attorney before speaking"); <i>Smith</i> v. <i>Illinois,</i> <span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/" aria-description="Citation for case: Smith v. Illinois">469 U. S. 91</a></span> (1984) <i>(per curiam)</i><i>.</i></p>
<p>I believe that a partial invocation of the right to counsel, without more, invariably will be ambiguous. It gives rise to doubts about the defendant's precise wishes regarding representation and about his or her understanding of the nature and scope of the right to counsel. Thus, the police may not infer from a partial invocation of the right to counsel <i>alone</i> that the defendant has waived any of his or her rights not specifically invoked.</p>
<p>However, circumstances may clarify an otherwise ambiguous situation. If the partial invocation is accompanied by an explicit waiver of the right to silence that is voluntary, knowing, and intelligent, it may lose its ambiguity.<sup>[5]</sup> It may become <span class="star-pagination">*535</span> clear that the portion of the right to counsel that was not invoked was in fact waived, when, for example, a knowing and intelligent waiver of the right to silence necessarily includes a waiver of the right to have counsel present at questioning. This is such a case.<sup>[6]</sup> Here Barrett's limited invocation was not ambiguous: It was accompanied by an express waiver of his right to silence, the validity of which was plainly established by his subsequent trial testimony. The accompaniment of Barrett's reference to his limited desire for counsel with an explicit waiver of his right to silence rendered permissible the authorities' use of his statements.<sup>[7]</sup></p>
<p>For these reasons, I concur in the judgment of the Court.</p>
<p><span class="star-pagination">*536</span> JUSTICE STEVENS, with whom JUSTICE MARSHALL joins, dissenting.</p>
<p>The Court's disposition of this case raises two troublesome questions.</p>
<p>First, why did the Court decide to exercise its discretion to grant review in this case? The facts of the case are surely unique. They do not give rise to any issue of general or recurring significance. There is no conflict among the state or federal courts on how the narrow question presented should be resolved. It is merely a case in which one State Supreme Court arguably granted more protection to a citizen accused of crime than the Federal Constitution requires.<sup>[1]</sup> The State "asks us to rule that the state court interpreted federal rights too broadly and `overprotected' the citizen." <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1068" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1068</a></span> (1983) (STEVENS, J., dissenting). If this is a sufficient reason for adding a case to our already overcrowded docket, we will need, not one, but several newly fashioned "intercircuit tribunals" to keep abreast of our work.</p>
<p>Second, why was respondent's request for the assistance of counsel any less ambiguous than the request in <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981)? In that case, the defendant said that he wanted an attorney " `before making a deal.' " <span class="star-pagination">*537</span> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#479" aria-description="Citation for case: Edwards v. Arizona"><i>Id.,</i> at 479</a></span>. He also said he would talk to the police " `but I don't want it on tape.' " <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Ibid.</a></span></i> The police interrogation complied with the everyday meaning of both of those conditions; it occurred before Edwards made any "deal"  indeed, he never made a deal  and no tape recording of the session was made. The Court nevertheless found the interrogation objectionable. In this case, respondent requested an attorney before signing a written statement. Why the police's compliance with the literal terms of that request makes the request  as opposed to the subsequent waiver<sup>[2]</sup>  any less of a request for the assistance of counsel than Edwards' is not adequately explained in the Court's opinion. In all events, the Court does not purport to change the governing rule of law that judges must "give a broad, rather than a narrow, interpretation to a defendant's request for counsel." <i>Michigan</i> v. <i>Jackson,</i> <span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#633" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625, 633</a></span> (1986).</p>
<p>I would dismiss the writ of certiorari as improvidently granted.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> urging reversal were filed for the State of Alaska et al. by <i>David Crump</i> and by the Attorneys General for their respective States as follows: <i>Harold M. Brown</i> of Alaska, <i>Robert K. Corbin</i> of Arizona, <i>John Steven Clark</i> of Arkansas, <i>John K. Van de Kamp</i> of California, <i>Duane Woodard</i> of Colorado, <i>James T. Jones</i> of Idaho, <i>Linley E. Pearson</i> of Indiana, <i>David L. Armstrong</i> of Kentucky, <i>William J. Guste, Jr.,</i> of Louisiana, <i>Frank J. Kelley</i> of Michigan, <i>Hubert H. Humphrey III</i> of Minnesota, <i>Edwin L. Pittman</i> of Mississippi, <i>William L. Webster</i> of Missouri, <i>Lacy H. Thornburg</i> of North Carolina, <i>LeRoy S. Zimmerman</i> of Pennsylvania, <i>T. Travis Medlock</i> of South Carolina, <i>Mark V. Meierhenry</i> of South Dakota, <i>Mary Sue Terry</i> of Virginia, <i>Kenneth O. Eikenberry</i> of Washington, and <i>Bronson C. La Follette</i> of Wisconsin; and for the National District Attorneys Association by <i>Robert S. Marsel, Jack E. Yelverton,</i> and <i>James P. Manak.</i></p>
<p>[1]  The Connecticut Supreme Court noted in its opinion that the trial court "impliedly found that the defendant had requested counsel." <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#56" aria-description="Citation for case: State v. Barrett">197 Conn. 50, 56</a></span>, <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#1048" aria-description="Citation for case: State v. Barrett">495 A. 2d 1044, 1048</a></span> (1985). This statement does not suggest, however, that the request for counsel was in fact all-inclusive, and the Supreme Court expressly noted the trial court's finding that defendant had refused to give a written statement without his attorney present. <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#56" aria-description="Citation for case: State v. Barrett"><i>Id.,</i> at 56, n. 6</a></span>, <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#1048" aria-description="Citation for case: State v. Barrett">495 A. 2d, at 1048, n. 6</a></span>. The holding that Barrett had invoked his right to counsel, then, rests on a legal conclusion about the effect of his limited invocation rather than on a factual finding.</p>
<p>[2]  Because the attempts to record Barrett's statements were unsuccessful, we have no occasion to consider whether the result would be different if police had taped the statements and used the recording against Barrett.</p>
<p>[3]  Since we reject the claim that Barrett's statements represent an ambiguous or equivocal response to the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, there is no need for us to address the question left open in <i>Smith</i> v. <i>Illinois,</i> <span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#96" aria-description="Citation for case: Smith v. Illinois">469 U. S. 91, 96, n. 3</a></span> (1984) <i>(per curiam)</i><i>.</i></p>
<p>[4]  We do not suggest that the distinction drawn by Barrett is in fact illogical, for there may be several strategic reasons why a defendant willing to speak to the police would still refuse to write out his answers to questions, or to sign a transcript of his answers prepared by the police, a statement that may be used against him.</p>
<p>[1]  The trial judge denied Barrett's motion to suppress the statements made following administration of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, holding:
</p>
<p>"[T]he Court concludes from the evidence it heard that [Barrett] indicated he understood perfectly what was being read to him. Not only did he indicate that he understood, he offered the statements that he did not need anything explained to him because he understood. So it was not merely a passive acquiescence and his agreement that he understood, he did go on to explain that he did not need anything explained to him because he perfectly understood." App. 70A.</p>
<p>[2]  The Court states that " `a defendant's ignorance of the full consequences of his decisions' " would not " `vitiat[e] their voluntariness.' " <i>Ante,</i> at 530 (quoting <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#316" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 316</a></span> (1985)). I do not accept that a defendant could voluntarily, knowingly, or intelligently waive a right that he or she does not understand to exist. Cf. <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#277" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 277</a></span> (1973) (BRENNAN, J., dissenting) ("The Court holds today that an individual can effectively waive this right [to be secure against an unreasonable search] even though he is totally ignorant of the fact that, in the absence of his consent, such invasions of privacy would be constitutionally prohibited. It wholly escapes me how our citizens can meaningfully be said to have waived something as precious as a constitutional guarantee without ever being aware of its existence"); <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">ibid.</a></span></i> (MARSHALL, J., dissenting) ("I would have thought that the capacity to choose necessarily depends upon knowledge that there is a choice to be made. But today the Court reaches the curious result that one can choose to relinquish a constitutional right  the right to be free of unreasonable searches  without knowing that he has the alternative of refusing to accede to a police request to search").</p>
<p>[3]  See also 1 W. LaFave &amp; J. Israel, Criminal Procedure § 6.9(f), pp. 534-535 (1984 ed.) ("[T]he <i><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span></i> facts certainly suggest that the defendant misperceived the effect of a waiver which was oral rather than written. Under such circumstances, there is much to be said for the view that the police are under an obligation to clear up misunderstandings of this nature which are apparent to any reasonable observer. Short of this, it certainly makes sense to conclude that the defendant's conduct should significantly increase the prosecution's burden to overcome the presumption against waiver of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights").</p>
<p>[4]  It is undisputed that the defendant here, unlike the defendant in <i><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span>,</i> had the capacity to understand his rights: the police ascertained that Barrett had a 12th-grade education, Tr. 458, while in <i><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span></i> there was a dispute over whether the defendant could read. <i>North Carolina</i> v. <i>Butler,</i> <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#378" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369, 378</a></span> (1979).</p>
<p>[5]  In order for a valid waiver and partial invocation of the right to counsel to occur, the accused must effect them contemporaneously. In <i>Smith</i> v. <i>Illinois,</i> <span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/" aria-description="Citation for case: Smith v. Illinois">469 U. S. 91</a></span> (1984) <i>(per curiam)</i><i>,</i> the Court considered a defendant's plain request for counsel that had been closely followed by statements rendering equivocal or ambiguous his first request. The State Supreme Court determined that the defendant's statements, considered as a totality, were ambiguous and therefore did not invoke his right to counsel. We held that "an accused's <i>postrequest</i> responses to further interrogation may not be used to cast retrospective doubt on the clarity of the initial request itself." <span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#100" aria-description="Citation for case: Smith v. Illinois"><i>Id.,</i> at 100</a></span>. Thus, if the initial request for counsel is clear, as it was here, the police may not create ambiguity in a defendant's desire by continuing to question him or her about it.</p>
<p>[6]  See also <i>United States</i> v. <i>Jardina,</i> <span class="citation" data-id="444143"><a href="/opinion/444143/united-states-v-charles-c-jardina/#949" aria-description="Citation for case: United States v. Charles C. Jardina">747 F. 2d 945, 949</a></span> (CA5 1984) (The defendant stated "without the slightest ambiguity that he would then and there answer some questions but not others" and "clearly indicated that he wished his attorney to work out a cooperative deal with the government in the future." The Court of Appeals found that these combined statements "did not invoke any <i>present</i> right to counsel").</p>
<p>[7]  It is undisputed that "[h]ad the police obtained [a written] statement without meeting the waiver standards of <i>Edwards</i> [v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981)], it would clearly be inadmissible." <i>Ante,</i> at 529. Barrett's invocation of his rights demonstrates that he opposed any immediate preservation of statements made without counsel. If the attempt to tape Barrett's statements had succeeded, the recording would have been inadmissible.
</p>
<p>In addition, the police attempted to persuade Barrett to waive the right he had asserted not to make a written statement without the assistance of counsel, not once, but twice, absent any indication from Barrett that he had changed his mind on this point. Tr. 689 ("Sergeant Genovese at the first [questioning] and Lieutenant Howard at the second inquired whether or not he had changed his mind [about reducing his statements to writing]"); see also <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#521" aria-description="Citation for case: Edwards v. Arizona"><i>id.,</i> at 521</a></span>. In <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484-485</a></span>, we held that once an accused invokes the right to counsel, he or she is not subject to further custodial interrogation "until counsel has been made available to him [or her], unless the accused . . . initiates further communication, exchanges, or conversations with the police." Here the police failed to respect Barrett's limited assertion of his right to counsel. Had a written statement been obtained as a result of these persistent efforts to change Barrett's mind, it would have been inadmissible.</p>
<p>[1]  "The central contention of the Petitioner in this action is that the Connecticut Supreme Court unduly expanded the protections accorded criminal defendants under the Fifth Amendment to the United States [C]onstitution when it determined that this defendant involuntarily waived his right to assistance of counsel at his interrogation. This result was possible only through use of a prophylactic rule which ignored the circumstances of this case." Pet. for Cert. 5.</p>
<p>[2]  In this case, the Connecticut Supreme Court interpreted the trial court's ruling as embodying a factual finding that respondent had requested the assistance of counsel but <i>thereafter</i> waived his right to counsel. It agreed with that factual determination but held that the subsequent waiver was ineffective as a matter of law. <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#60" aria-description="Citation for case: State v. Barrett">197 Conn. 50, 60</a></span>, <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#1050" aria-description="Citation for case: State v. Barrett">495 A. 2d 1044, 1050</a></span> (1985).</p>

</div>
```

---

## GROUP: content/cases/Connick v. Thompson.md  (`case`, 6 assertions)

### content_page

```
---
title: "Connick v. Thompson"
type: case
citation: ""
parallel_cite: "179 L. Ed. 2d 417; 131 S. Ct. 1350; 563 U.S. 51; 22 Fla. L. Weekly Fed. S 887; 79 U.S.L.W. 4195"
neutral_cite: 2011 U.S. LEXIS 2594
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2011
date_decided: 2011-03-29
docket: 09-571
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2011-03-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Connick v. Thompson
  varies_by_point: false
  scope_note: "Good law: a single Brady violation, without a pattern, does not establish municipal failure-to-train liability."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/7343085/connick-v-thompson/"
  cluster_id: 7343085
  opinion_id: 7261027
  identity_checked: true
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Brady and Giglio]]"
    role: "Related (cross-doctrine)"
related: ["[[City of Canton v. Harris]]", "[[Monell v. Department of Social Services]]", "[[Brady v. Maryland]]"]
aliases: []
tags: ["case", "section-1983", "municipal-liability", "failure-to-train", "deliberate-indifference", "brady"]
holding: "A single Brady violation, without a pattern of similar violations, generally cannot establish the deliberate indifference required for municipal failure-to-train liability; prosecutorial Brady training is not within Canton's narrow single-incident exception."
lake:
  record_id: Connick v. Thompson
  status: verified
  projected_at: 2026-07-09
---

# Connick v. Thompson

*563 U.S. 51 (2011)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
John Thompson was convicted of armed robbery and murder in New Orleans and spent years on death row before it emerged that prosecutors in District Attorney Harry Connick's office had suppressed a crime-lab report (blood-type evidence) favorable to him, in violation of [[Brady v. Maryland]]. His convictions were [[Reading and Citing Cases#vacated|vacated]] and he was acquitted on retrial. He sued the District Attorney's Office under § 1983, claiming Connick had been deliberately indifferent in failing to train prosecutors on their *[[Brady v. Maryland|Brady]]* obligations. A jury awarded him $14 million.

## Issue
Whether a district attorney's office may be held liable under § 1983 for failure to train its prosecutors on *[[Brady v. Maryland|Brady]]* based on a single violation, absent a pattern of similar violations.

## Rule
A pattern of violations is ordinarily required. "A pattern of similar constitutional violations by untrained employees is 'ordinarily necessary' to demonstrate deliberate indifference for purposes of failure to train." — 563 U.S. at 62. ^pin-62

*[[City of Canton v. Harris|Canton]]* recognized a "narrow range" of single-incident liability where the need for training is so obvious and the violation so predictable that a pattern is unnecessary — but that exception is confined. "Failure to train prosecutors in their *Brady* obligations does not fall within the narrow range of *Canton's* hypothesized single-incident liability." — [*Id.* at 64](https://www.courtlistener.com/opinion/7343085/connick-v-thompson/#:~:text=a-,narrow%20range). ^pin-64

## Application
Thompson did not prove a pattern of similar *[[Brady v. Maryland|Brady]]* violations: the four earlier reversals in Connick's office involved different kinds of suppressed evidence and could not have put the office on notice that training on this type of *[[Brady v. Maryland|Brady]]* violation was deficient. Nor did the single-incident theory apply: unlike the untrained-officer-with-a-gun hypothetical in *[[City of Canton v. Harris|Canton]]*, prosecutors are trained lawyers who are expected to know and apply *[[Brady v. Maryland|Brady]]*, so the need to train them on it is not the kind of "patently obvious" need that supports liability without a pattern.

## Conclusion
Reversed. A single *[[Brady v. Maryland|Brady]]* violation, without a pattern of similar violations, is insufficient to establish the [[Section 1983 Liability and Qualified Immunity|deliberate indifference]] required for municipal failure-to-train liability; the $14 million judgment could not stand.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Connick* applies and tightens the deliberate-indifference / single-incident framework of [[City of Canton v. Harris]] within the [[Monell v. Department of Social Services]] municipal-liability line, at the intersection with the prosecutor's duty under [[Brady v. Maryland]]. No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*
- [[Brady and Giglio]] — *Related (cross-doctrine)*

## Sources
- *Connick v. Thompson*, 563 U.S. 51 (2011) — https://www.courtlistener.com/opinion/213505/connick-v-thompson/ — pinpoints: 62, 64 (lead opinion id 9441299).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9af839f5135b455f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2011 U.S. LEXIS 2594", "official_citation_present": false, "parallel_cite": "179 L. Ed. 2d 417; 131 S. Ct. 1350; 563 U.S. 51; 22 Fla. L. Weekly Fed. S 887; 79 U.S.L.W. 4195", "title": "Connick v. Thompson", "year": "2011"}}
{"assertion_id": "39da9e5c24dfedb1", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "Connick v. Thompson"}}
{"assertion_id": "aa6da72193ee6674", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A single Brady violation, without a pattern of similar violations, generally cannot establish the deliberate indifference required for municipal failure-to-train liability; prosecutorial Brady training is not within Canton's narrow single-incident exception.", "title": "Connick v. Thompson"}}
{"assertion_id": "fb21bc468e2d66ef", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Related (cross-doctrine)", "title": "Connick v. Thompson"}}
{"assertion_id": "4a4b50bd9564fec4", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Connick v. Thompson"}}
{"assertion_id": "f8cebdc8fb1f8bfe", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2011-03-29", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Connick v. Thompson", "field_i_validity": "good_law", "scope_note": "Good law: a single Brady violation, without a pattern, does not establish municipal failure-to-train liability.", "title": "Connick v. Thompson", "varies_by_point": "false"}}
```

### lake record — Connick v. Thompson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Connick v. Thompson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Connick v. Thompson",
    "case_name_short": "Connick",
    "case_name_full": "HARRY F. CONNICK, DISTRICT ATTORNEY v. JOHN THOMPSON",
    "input_case_name": "Connick v. Thompson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2011-03-29",
    "year": 2011,
    "docket": "09-571",
    "cluster_id": 7343085,
    "lead_opinion_id": 7261027,
    "sibling_ids": [
      7261027,
      7261028,
      7261029
    ],
    "absolute_url": "/opinion/7343085/connick-v-thompson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 213505,
        "score": 120,
        "case_name": "Connick v. Thompson"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "179 L. Ed. 2d 417",
        "volume": "179",
        "reporter": "L. Ed. 2d",
        "page": "417",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 S. Ct. 1350",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "1350",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "563 U.S. 51",
        "volume": "563",
        "reporter": "U.S.",
        "page": "51",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 Fla. L. Weekly Fed. S 887",
        "volume": "22",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "887",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 U.S.L.W. 4195",
        "volume": "79",
        "reporter": "U.S.L.W.",
        "page": "4195",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2011 U.S. LEXIS 2594",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "2594",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "179 L. Ed. 2d 417",
        "volume": "179",
        "reporter": "L. Ed. 2d",
        "page": "417",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 U.S. LEXIS 2594",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "2594",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 S. Ct. 1350",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "1350",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "563 U.S. 51",
        "volume": "563",
        "reporter": "U.S.",
        "page": "51",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 Fla. L. Weekly Fed. S 887",
        "volume": "22",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "887",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 U.S.L.W. 4195",
        "volume": "79",
        "reporter": "U.S.L.W.",
        "page": "4195",
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
      "id": "pin-62",
      "page": null,
      "quote": "--- # Connick v. Thompson *563 U.S. 51 (2011)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background John Thompson was convicted of armed robbery and murder in New Orleans and spent years on death row before it emerged that prosecutors in District Attorney Harry Connick's office had suppressed a crime-lab report (blood-type evidence) favorable to him, in violation of [[Brady v. Maryland]]. His convictions were vacated and he was acquitted on retrial. He sued the District Attorney's Office under \u00a7 1983, claiming Connick had been deliberately indifferent in failing to train prosecutors on their *Brady* obligations. A jury awarded him $14 million. ## Issue Whether a district attorney's office may be held liable under \u00a7 1983 for failure to train its prosecutors on *Brady* based on a single violation, absent a pattern of similar violations. ## Rule A pattern of violations is ordinarily required.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-64",
      "page": null,
      "quote": "narrow range",
      "star_marker": "428",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 39484,
      "fragment": "#:~:text=a-,narrow%20range",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2011-03-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Connick v. Thompson",
    "varies_by_point": false,
    "scope_note": "Good law: a single Brady violation, without a pattern, does not establish municipal failure-to-train liability.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Brown v. City of Hous.",
          "cluster_id": 7329084,
          "cite": [
            "297 F. Supp. 3d 748"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ramona Hinojosa v. Brad Livingston",
          "cluster_id": 3155936,
          "cite": [
            "807 F.3d 657",
            "2015 U.S. App. LEXIS 20016",
            "2015 WL 7422990"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Prall v. City of Boston",
          "cluster_id": 8729956,
          "cite": [
            "985 F. Supp. 2d 115",
            "2013 WL 6076462",
            "2013 U.S. Dist. LEXIS 166128"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Foley v. Town of Lee",
          "cluster_id": 8716566,
          "cite": [
            "871 F. Supp. 2d 39",
            "2012 DNH 081",
            "2012 WL 1624947",
            "2012 U.S. Dist. LEXIS 64907"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. Town of East Haven",
          "cluster_id": 8441252,
          "cite": [
            "691 F.3d 72",
            "2012 U.S. App. LEXIS 15928",
            "2012 WL 3104523"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haley v. City of Boston",
          "cluster_id": 613874,
          "cite": [
            "657 F.3d 39",
            "2011 U.S. App. LEXIS 19223",
            "2011 WL 4347027"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Porter v. Epps",
          "cluster_id": 614341,
          "cite": [
            "659 F.3d 440",
            "2011 U.S. App. LEXIS 19756",
            "2011 WL 4471051"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Julie Helphenstine v. Lewis County",
          "cluster_id": 9374379,
          "cite": [
            "60 F.4th 305"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matusick v. Erie County Water Authority",
          "cluster_id": 8441814,
          "cite": [
            "757 F.3d 31",
            "2014 WL 700718"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Armstrong v. Ashley",
          "cluster_id": 9375737,
          "cite": [
            "60 F.4th 262"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Saldivar v. Racine",
          "cluster_id": 3189097,
          "cite": [
            "818 F.3d 14",
            "2016 U.S. App. LEXIS 5623",
            "2016 WL 1169397"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tamika Johnson v. City of Philadelphia",
          "cluster_id": 4787333,
          "cite": [
            "975 F.3d 394"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gray v. Cummings",
          "cluster_id": 4593291,
          "cite": [
            "917 F.3d 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pearlie Gambrel v. Knox Cnty., Ky.",
          "cluster_id": 6347889,
          "cite": [
            "25 F.4th 391"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Reck v. Wexford Health Sources, Inc.",
          "cluster_id": 6444901,
          "cite": [
            "27 F.4th 473"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nathson Fields v. City of Chicago",
          "cluster_id": 4820969,
          "cite": [
            "981 F.3d 534"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henderson v. Harris County",
          "cluster_id": 8248448,
          "cite": [
            "51 F.4th 125"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lefebure v. D'aquila",
          "cluster_id": 5287572,
          "cite": [
            "15 F.4th 650"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "George v. Beaver County",
          "cluster_id": 6465265,
          "cite": [
            "32 F.4th 1246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Teresa Graham v. Shannon Barnette",
          "cluster_id": 4900401,
          "cite": [
            "5 F.4th 872"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Daniel Robbins v. City of Des Moines",
          "cluster_id": 4845312,
          "cite": [
            "984 F.3d 673"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hill v. Walsh",
          "cluster_id": 4471312,
          "cite": [
            "884 F.3d 16"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gerald Marshall v. Town of Dexter",
          "cluster_id": 3134066,
          "cite": [
            "2015 ME 135",
            "125 A.3d 1141",
            "2015 Me. LEXIS 147"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Friend v. Gasparino",
          "cluster_id": 9379829,
          "cite": [
            "61 F.4th 77"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crittindon v. LeBlanc",
          "cluster_id": 6476851,
          "cite": [
            "37 F.4th 177"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Timmy Mosier v. Joseph Evans",
          "cluster_id": 9458549,
          "cite": [
            "90 F.4th 541"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Hightower v. City of Philadelphia",
          "cluster_id": 10352157,
          "cite": [
            "130 F.4th 352"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(7261027 OR 7261028 OR 7261029) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 109,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 109,
        "triage_read": 5,
        "triage_snippet_classified": 104
      },
      "lane2_top_cited": {
        "query": "cites:(7261027 OR 7261028 OR 7261029)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMCZzPTg3MTI3MDkmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%287261027+OR+7261028+OR+7261029%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(7261027 OR 7261028 OR 7261029)",
        "reviewed": 51,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 51,
        "triage_read": 0,
        "triage_snippet_classified": 51
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(7261027 OR 7261028 OR 7261029)",
    "indexed_citing_opinions": 171,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 7261027,
        "count": 171,
        "count_source": "search"
      },
      {
        "opinion_id": 7261028,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 7261029,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4362,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/connick-v-thompson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4ODkxOTUmcz0xMDAwMTEzNiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%287261027+OR+7261028+OR+7261029%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T01:01:06Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T01:01:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T01:01:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T01:09:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T01:01:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Connick v. Thompson

```
<opinion type="majority">
<p id="b520-12">OPINION OF THE COURT</p>
<p id="b520-5">[<span class="citation no-link">563 U.S. 54</span>]</p>
<author id="b520-6">Justice Thomas</author>
<p id="apa-dedup-2">delivered the opinion of the Court.</p>
<p id="b520-7">The Orleans Parish District Attorney’s Office now concedes that, in prosecuting respondent John Thompson for attempted armed robbery, prosecutors failed to disclose evidence that should have been turned over to the defense under <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U.S. 83</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">83 S. Ct. 1194</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">10 L. Ed. 2d 215</a></span> (1963). Thompson was convicted. Because of that conviction Thompson elected not to testify defense in his later trial for murder, and he was again convicted. Thompson spent 18 years in prison, including 14 years on death row. One month before Thompson’s scheduled execution, his investigator discovered the undisclosed evidence from his armed robbery trial. The reviewing court determined that the evidence was exculpatory, and both of Thompson’s convictions were vacated.</p>
<p id="b520-8">After his release from prison, Thompson sued petitioner Harry Con-nick, in his official capacity as the Orleans Parish district attorney, for damages under Rev. Stat. § 1979, <span class="citation no-link">42 U.S.C. § 1983</span>. Thompson alleged that Connick had failed to train his prosecutors adequately about their duty to produce exculpatory evidence and that the lack of training had caused the nondisclosure in Thompson’s robbery case. The jury awarded Thompson $14 million, and the Court of Appeals for the Fifth Circuit affirmed by an evenly divided en banc court. We granted certiorari to decide whether  a district attorney’s office may be held liable under § 1983 for failure to train based on a single <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation. We hold that it cannot.</p>
<p id="b520-14">I</p>
<p id="b520-15">A</p>
<p id="b520-16">In early 1985, John Thompson was charged with the murder of Raymond T. Liuzza, Jr., in New Orleans. Publicity following the murder charge led <page-number citation-index="1" label="423">*423</page-number>the victims of an unrelated</p>
<p id="aof-dedup-1">[<span class="citation no-link">563 U.S. 55</span>]</p>
<p id="b521-4">armed robbery to identify Thompson as their attacker. The district attorney charged Thompson with attempted armed robbery.</p>
<p id="b521-6">As part of the robbery investigation, a crime scene technician took from one of the victims’ pants a swatch of fabric stained with the robber’s blood. Approximately one week before Thompson’s armed robbery trial, the swatch was sent to the crime laboratory. Two days before the trial, Assistant District Attorney Bruce Whittaker received the crime lab’s report, which stated that the perpetrator had blood type B. There is no evidence that the prosecutors ever had Thompson’s blood tested or that they knew what his blood type was. Whittaker claimed he placed the report on Assistant District Attorney James Williams’ desk, but Williams denied seeing it. The report was never disclosed to Thompson’s counsel.</p>
<p id="b521-7">Williams tried the armed robbery case with Assistant District Attorney Gerry Deegan. On the first day of trial, Deegan checked all of the physical evidence in the case out of the police property room, including the bloodstained swatch. Deegan then checked all of the evidence but the swatch into the courthouse property room. The prosecutors did not mention the swatch or the crime lab report at trial, and the jury convicted Thompson of attempted armed robbery.</p>
<p id="b521-8">A few weeks later, Williams and Special Prosecutor Eric Dubelier tried Thompson for the Liuzza murder. Because of the armed robbery conviction, Thompson chose not to testify in his own defense. He was convicted and sentenced to death. <em>State </em>v. <em>Thompson, </em><span class="citation" data-id="1678561"><a href="/opinion/1678561/state-v-thompson/" aria-description="Citation for case: State v. Thompson">516 So. 2d 349</a></span> (La. 1987). In the 14 years following Thompson’s murder conviction, state and federal courts reviewed and denied his challenges to the conviction and sentence. See <em>State ex rel. Thompson </em>v. <em>Cain, </em>95-2463 (La. 4/25/96), <span class="citation" data-id="7696643"><a href="/opinion/7759076/state-ex-rel-thompson-v-cain/" aria-description="Citation for case: State ex rel. Thompson v. Cain">672 So. 2d 906</a></span>; <em>Thompson </em>v. <em>Cain, </em><span class="citation" data-id="16134"><a href="/opinion/16134/thompson-v-cain/" aria-description="Citation for case: Thompson v. Cain">161 F.3d 802</a></span> (CA5 1998). The State scheduled Thompson’s execution for May 20, 1999.</p>
<p id="b521-9">[<span class="citation no-link">563 U.S. 56</span>]</p>
<p id="b521-10">In late April 1999, Thompson’s private investigator discovered the crime lab report from the armed robbery investigation in the files of the New Orleans Police Crime Laboratory. Thompson was tested and found to have blood type O, proving that the blood on the swatch was not his. Thompson’s attorneys presented this evidence to the district attorney’s office, which, in turn, moved to stay the execution and vacate Thompson’s armed robbery conviction.<footnotemark>1</footnotemark> The Louisiana Court of Appeal then reversed Thompson’s murder conviction, concluding that the armed robbery conviction unconstitutionally deprived Thompson of his right to testify in his own defense at the murder trial. <em>State </em>v. <em>Thompson, </em>2002-0361 (La. App. 7/17/02), <span class="citation" data-id="1714044"><a href="/opinion/1714044/state-v-thompson/" aria-description="Citation for case: State v. Thompson">825 So. 2d 552</a></span>. In 2003, the district attorney’s office retried Thomp<page-number citation-index="1" label="424">*424</page-number>son for Liuzza’s murder.<footnotemark>2</footnotemark> The jury found him not guilty.</p>
<p id="b522-4">B</p>
<p id="b522-5">Thompson then brought this action against the district attorney’s office, Connick, Williams, and others, alleging that their conduct caused him to be wrongfully convicted, incarcerated for 18 years, and nearly executed. The only claim that proceeded to trial was Thompson’s claim under § 1983 that the district attorney’s office had violated <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>by failing</p>
<p id="b522-6">[<span class="citation no-link">563 U.S. 57</span>]</p>
<p id="b522-7">to disclose the crime lab report in his armed robbery trial. See <em>Brady, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U.S. 83</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">83 S. Ct. 1194</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">10 L. Ed. 2d 215</a></span>. Thompson alleged liability under two theories: (1) The <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation was caused by an unconstitutional policy of the district attorney’s office; and (2) the violation was caused by Connick’s deliberate indifference to an obvious need to train the prosecutors in his office in order to avoid such constitutional violations.</p>
<p id="b522-8">Before trial, Connick conceded that the failure to produce the crime lab report constituted a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation.<footnotemark>3</footnotemark> See Record EX608, EX880. Accordingly, the District Court instructed the jury that the “only issue” was whether the nondisclosure was caused by either a policy, practice, or custom of the district attorney’s office or a deliberately indifferent failure to train the office’s prosecutors. <em>Id., </em>at 1615.</p>
<p id="b522-9">Although no prosecutor remembered any specific training session regarding <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>prior to 1985, it was undisputed at trial that the prosecutors were familiar with the general <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>requirement that the State disclose to the defense evidence in its possession that is favorable to the accused. Prosecutors testified that office policy was to turn crime lab reports and other scientific evidence over to the defense. They also testified that, after the discovery of the undisclosed crime lab report in 1999, prosecutors disagreed about whether it had to be disclosed under <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>absent knowledge of Thompson’s blood type.</p>
<p id="b522-11">The jury rejected Thompson’s claim that an unconstitutional office policy caused the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation, but found the district attorney’s office liable for failing to train the prosecutors. The jury awarded Thompson $14 million in damages, and the District Court added more than $1 million in attorney’s fees and costs.</p>
<p id="b522-12">After the verdict, Connick renewed his objection—which he had raised on summary judgment—that he could not have</p>
<p id="b522-13">[<span class="citation no-link">563 U.S. 58</span>]</p>
<p id="b522-14">been deliberately indifferent to an obvious need for more or different <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>training because there was no evidence that he was aware of a pattern of similar <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violations. The District Court rejected this argument for the reasons that it had given in the summary judgment order. In that order, the court had concluded that a pattern of violations is not necessary to prove deliberate indifference when the need for training is “so obvious.” No. Civ. A. 03-2045 (ED La., Nov. 15, 2005), App. to Pet. for Cert. <page-number citation-index="1" label="425">*425</page-number>141a, <span class="citation no-link">2005 WL 3541035</span>, *13. Relying on <em>Canton </em>v. <em>Harris, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">489 U.S. 378</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span> (1989), the court had held that Thompson could demonstrate deliberate indifference by proving that “the DA’s office knew to a moral certainty that assis-tan[t] [district attorneys] would acquire <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>material, that without training it is not always obvious what <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>requires, and that withholding <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>material will virtually always lead to a substantial violation of constitutional rights.”<footnotemark>4</footnotemark> App. to Pet. for Cert. 141a, <span class="citation no-link">2005 WL 3541035</span>, *13.</p>
<p id="b523-4">A panel of the Court of Appeals for the Fifth Circuit affirmed. The panel acknowledged that Thompson did not present evidence of a pattern of similar <em>Brady </em>violations, <span class="citation" data-id="64218"><a href="/opinion/64218/thompson-v-connick/#851" aria-description="Citation for case: Thompson v. Connick">553 F.3d 836, 851</a></span> (2008), but held that Thompson did not need to prove a pattern, <span class="citation" data-id="64218"><a href="/opinion/64218/thompson-v-connick/#854" aria-description="Citation for case: Thompson v. Connick">id., at 854</a></span>. According to the panel, Thompson demonstrated that Connick was on notice of an obvious need for <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>training by presenting evidence “that attorneys, often fresh out of law school, would undoubtedly be required to confront <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>issues while at the DA’s Office, that erroneous decisions regarding <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>evidence would result in serious constitutional violations, that resolution of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>issues was often unclear, and that training in <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>would have been helpful.” <span class="citation" data-id="64218"><a href="/opinion/64218/thompson-v-connick/#854" aria-description="Citation for case: Thompson v. Connick">553 F.3d, at 854</a></span>.</p>
<p id="b523-5">[<span class="citation no-link">563 U.S. 59</span>]</p>
<p id="b523-6">The Court of Appeals sitting en banc vacated the panel opinion, granted rehearing, and divided evenly, thereby affirming the District Court. <span class="citation" data-id="9634025"><a href="/opinion/1456596/thompson-v-connick/" aria-description="Citation for case: Thompson v. Connick">578 F.3d 293</a></span> (CA5 2009) <em>(per curiam). </em>In four opinions, the divided en banc court disputed whether Thompson could establish municipal liability for failure to train the prosecutors based on the single <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation without proving a prior pattern of similar violations, and, if so, what evidence would make that showing. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.S./559/1004/">559 U.S. 1004</a></span>, <span class="citation multiple-matches"><a href="/c/S.%20Ct./130/1880/">130 S. Ct. 1880</a></span>, <span class="citation multiple-matches"><a href="/c/L.%20Ed.%202d/176/399/">176 L. Ed. 2d 399</a></span> (2010).</p>
<p id="b523-8">II</p>
<p id="b523-9">The <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation conceded in this case occurred when one or more of the four prosecutors involved with Thompson’s armed robbery prosecution failed to disclose the crime lab report to Thompson’s counsel. Under Thompson’s failure-to-train theory, he bore the burden of proving both (1) that Connick, the policymaker for the district attorney’s office, was deliberately indifferent to the need to train the prosecutors about their <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>disclosure obligation with respect to evidence of this type and (2) that the lack of training actually caused the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation in this case. Connick argues that he was entitled to judgment as a matter of law because Thompson did not prove that he was on actual or constructive notice of, and therefore deliberately indifferent to, a need for more or different <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>training. We agree.<footnotemark>5</footnotemark></p>
<p id="b523-10">[<span class="citation no-link">563 U.S. 60</span>]</p>
<p id="b523-11">A</p>
<p id="b523-12">Title <span class="citation no-link">42 U.S.C. § 1983</span> provides in relevant part:</p>
<blockquote id="b523-13">“Every person who, under color of any statute, ordinance, <page-number citation-index="1" label="426">*426</page-number>regulation, custom, or usage, of any State . . . subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress . . . .”</blockquote>
<p id="b524-4">A municipality or other local government may be liable under this section if the governmental body itself “subjects” a person to a deprivation of rights or “causes” a person “to be subjected” to such deprivation. See <em>Monell </em>v. <em>New York City Dept. of Social Servs., </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#692" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U.S. 658, 692</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">98 S. Ct. 2018</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">56 L. Ed. 2d 611</a></span> (1978). But, under § 1983, local governments are responsible only for “their <em>own </em>illegal acts.” <em>Pembaur </em>v. <em>Cincinnati, </em><span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#479" aria-description="Citation for case: Pembaur v. City of Cincinnati">475 U.S. 469, 479</a></span>, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">106 S. Ct. 1292</a></span>, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">89 L. Ed. 2d 452</a></span> (1986) (citing <em>Monell, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#665" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U.S., at 665-683</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">98 S. Ct. 2018</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">56 L. Ed. 2d 611</a></span>). They are not vicariously liable under § 1983 for their employees’ actions. See <em>id.., </em>at 691, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">98 S. Ct. 2018</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">56 L. Ed. 2d 611</a></span>; <em>Canton, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#392" aria-description="Citation for case: City of Canton v. Harris">489 U.S., at 392</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>; <em>Board of Comm’rs of Bryan Cty. </em>v. <em>Brown, </em><span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/#403" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">520 U.S. 397, 403</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span> (1997) (collecting cases).</p>
<p id="b524-6">Plaintiffs who seek to impose liability on local governments under § 1983 must prove that “action pursuant to official municipal policy” caused their injury. <em>Monell, </em>436 U.S.,</p>
<p id="b524-7">[<span class="citation no-link">563 U.S. 61</span>]</p>
<p id="b524-8">at 691, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">98 S. Ct. 2018</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">56 L. Ed. 2d 611</a></span>; see <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs."><em>id., </em>at 694</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">98 S. Ct. 2018</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">56 L. Ed. 2d 611</a></span>. Official municipal policy includes the decisions of a government’s lawmakers, the acts of its policymaking officials, and practices so persistent and widespread as to practically have the force of law. See <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#480" aria-description="Citation for case: Pembaur v. City of Cincinnati"><em>ibid.; Pembaur, supra, </em>at 480-481</a></span>, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">106 S. Ct. 1292</a></span>, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">89 L. Ed. 2d 452</a></span>; <em>Adickes </em>v. <em>S. H. Kress &amp; Co., </em><span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#167" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U.S. 144, 167-168</a></span>, <span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">90 S. Ct. 1598</a></span>, <span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">26 L. Ed. 2d 142</a></span> (1970). These are “action [s] for which the municipality is actually responsible.” <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#479" aria-description="Citation for case: Pembaur v. City of Cincinnati"><em>Pembaur, supra, </em>at 479-480</a></span>, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">106 S. Ct. 1292</a></span>, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">89 L. Ed. 2d 452</a></span>.</p>
<p id="b524-9">In limited circumstances, a local government’s decision not to train certain employees about their legal duty to avoid violating citizens’ rights may rise to the level of an official government policy for purposes of § 1983. A municipality’s culpability for a depri<page-number citation-index="1" label="427">*427</page-number>vation of rights is at its most tenuous where a claim turns on a failure to train. See <em>Oklahoma City </em>v. <em>Tuttle, </em><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#822" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U.S. 808, 822-823</a></span>, <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">105 S. Ct. 2427</a></span>, <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">85 L. Ed. 2d 791</a></span> (1985) (plurality opinion) (“[A] ‘policy’ of ‘inadequate training’ ” is “far more nebulous, and a good deal further removed from the constitutional violation, than was the policy in <em>Monell”). </em>To satisfy the statute, a municipality’s failure to train its employees in a relevant respect must amount to “deliberate indifference to the rights of persons with whom the [untrained employees] come into contact.” <em>Canton, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#388" aria-description="Citation for case: City of Canton v. Harris">489 U.S., at 388</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>. Only then “can such a shortcoming be properly thought of as a city ‘policy or custom’ that is actionable under § 1983.” <em>Id., </em>at 389, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>.</p>
<p id="b525-4">“ ‘[Deliberate indifference’ is a stringent standard of fault, requiring proof that a municipal actor disregarded a known or obvious consequence of his action.” <em>Bryan Cty., </em><span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/#410" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">520 U.S., at 410</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>. Thus, when city policymakers are on actual or constructive notice that a particular omission in their training program causes city employees to violate citizens’ constitutional rights, the city may be deemed deliberately indifferent if the policymakers choose to retain that program. <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/#407" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown"><em>Id., </em>at 407</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>. The city’s “ ‘policy of inaction’ ” in light of notice that its program will cause constitutional violations “is the functional equivalent of a decision by the city itself to violate</p>
<p id="ApE_">[<span class="citation no-link">563 U.S. 62</span>]</p>
<p id="b525-5">the Constitution.” <em>Canton, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#395" aria-description="Citation for case: City of Canton v. Harris">489 U.S., at 395</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span> (O’Connor, J., concurring in part and dissenting in part). A less stringent standard of fault for a failure-to-train claim “would result in <em>de facto respondeat superior </em>liability on municipalities .... <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#392" aria-description="Citation for case: City of Canton v. Harris"><em>" Id., </em>at 392</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>; see also <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#483" aria-description="Citation for case: Pembaur v. City of Cincinnati"><em>Pembaur, supra, </em>at 483</a></span>, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">106 S. Ct. 1292</a></span>, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">89 L. Ed. 2d 452</a></span> (opinion of Brennan, J.) (“[M]unicipal liability under § 1983 attaches where—and only where—a deliberate choice to follow a course of action is made from among various alternatives by [the relevant] officials . . . ”).</p>
<p id="b525-7">B</p>
<p id="b525-8">A pattern of similar constitutional violations by untrained employees is “ordinarily necessary” to demonstrate deliberate indifference for purposes of failure to train. <em>Bryan Cty., </em><span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/#409" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">520 U.S., at 409</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>. Policymakers’ “continued adherence to an approach that they know or should know has failed to prevent tortious conduct by employees may establish the conscious disregard for the consequences of their action—the ‘deliberate indifference’—necessary to trigger municipal liability.” <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/#407" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown"><em>Id., </em>at 407</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>. Without notice that a course of training is deficient in a particular respect, decisionmakers can hardly be said to have deliberately chosen a training program that will cause violations of constitutional rights.</p>
<p id="b525-9">Although Thompson does not contend that he proved a pattern of similar <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violations, <span class="citation" data-id="64218"><a href="/opinion/64218/thompson-v-connick/#851" aria-description="Citation for case: Thompson v. Connick">553 F.3d, at 851</a></span>, vacated, <span class="citation" data-id="9634025"><a href="/opinion/1456596/thompson-v-connick/" aria-description="Citation for case: Thompson v. Connick">578 F.3d 293</a></span> (en banc), he points out that, during the 10 years preceding his armed robbery trial, <page-number citation-index="1" label="428">*428</page-number>Louisiana courts had overturned four convictions because of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violations by prosecutors in Connick’s office.<footnotemark>6</footnotemark> Those four reversals could not have put Connick on notice that the office’s <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>training was inadequate with respect to the sort of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation at issue here. None of those cases involved failure to disclose blood evidence, a crime lab report, or physical or</p>
<p id="b526-4">[<span class="citation no-link">563 U.S. 63</span>]</p>
<p id="b526-5">scientific evidence of any kind. Because those incidents are not similar to the violation at issue here, they could not have put Connick on notice that specific training was necessary to avoid this constitutional violation.<footnotemark>7</footnotemark></p>
<p id="b526-6">C</p>
<p id="b526-7">1</p>
<p id="b526-8">Instead of relying on a pattern of similar <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violations, Thompson relies on the “single-incident” liability that this Court hypothesized in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span>. </em>He contends that the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation in his case was the “obvious” consequence of failing to provide specific <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>training, and that this showing of “obviousness” can substitute for the pattern of violations ordinarily necessary to establish municipal culpability.</p>
<p id="b526-9">In <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span>, </em>the Court left open the possibility that, “in a narrow range of circumstances,” a pattern of similar violations might not be necessary to show deliberate indifference. <em>Bryan Cty., supra, </em>at 409, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>. The Court posed the hypothetical example of a city that arms its police force with firearms and deploys the armed officers into the public to capture fleeing felons without training the officers in the constitutional limitation on the use of deadly force. <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#390" aria-description="Citation for case: City of Canton v. Harris"><em>Canton, supra, </em>at 390, n. 10</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>. Given the known frequency with which police attempt to arrest fleeing felons and the “predictability that an officer lacking specific tools to handle that situation will violate citizens’ rights,” the Court theorized that a city’s decision not to train the officers about constitutional limits on</p>
<p id="AF9I">[<span class="citation no-link">563 U.S. 64</span>]</p>
<p id="b526-11">the use of deadly force could reflect the city’s deliberate indifference to the “highly predictable consequence,” namely, violations of constitutional rights. <em>Bryan Cty., supra, </em>at 409, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>. The Court sought not to foreclose the possibility, however rare, that the unconstitutional consequences of failing to train could be so patently obvious that a city could be liable under § 1983 without proof of a pre-existing pattern of violations.</p>
<p id="b526-12">Failure to train prosecutors in their <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>obligations does not fall within the narrow range of <em>Canton’s </em>hypoth<page-number citation-index="1" label="429">*429</page-number>esized single-incident liability. The obvious need for specific legal training that was present in the <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>scenario is absent here. Armed police must sometimes make split-second decisions with life-or-death consequences. There is no reason to assume that police academy applicants are familiar with the constitutional constraints on the use of deadly force. And, in the absence of training, there is no way for novice officers to obtain the legal knowledge they require. Under those circumstances there is an obvious need for some form of training. In stark contrast, legal “[t] raining is what differentiates attorneys from average public employees.” <span class="citation" data-id="9634025"><a href="/opinion/1456596/thompson-v-connick/#304" aria-description="Citation for case: Thompson v. Connick">578 F.3d, at 304-305</a></span> (opinion of Clement, J.).</p>
<p id="b527-4">Attorneys are trained in the law and equipped with the tools to interpret and apply legal principles, understand constitutional limits, and exercise legal judgment. Before they may enter the profession and receive a law license, all attorneys must graduate from law school or pass a substantive examination; attorneys in the vast majority of jurisdictions must do both. See, <em>e.g., </em>La. State Bar Assn. (LSBA), Articles of Incorporation, La. Rev. Stat. Ann. § 37, ch. 4, App., Art. 14, § 7 (1988 West Supp.) (as amended through 1985). These threshold requirements are designed to ensure that all new attorneys have learned how to find, understand, and apply legal rules. Cf. <em>United States </em>v. <em>Cronic, </em><span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/#658" aria-description="Citation for case: United States v. Cronic">466 U.S. 648, 658, 664</a></span>, <span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/" aria-description="Citation for case: United States v. Cronic">104 S. Ct. 2039</a></span>, <span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/" aria-description="Citation for case: United States v. Cronic">80 L. Ed. 2d 657</a></span> (1984) (noting that the presumption “that the lawyer is competent to provide the guiding hand that the defendant</p>
<p id="ABqa">[<span class="citation no-link">563 U.S. 65</span>]</p>
<p id="b527-5">needs” applies even to young and inexperienced lawyers in their first jury trial and even when the case is complex).</p>
<p id="b527-6">Nor does professional training end at graduation. Most jurisdictions require attorneys to satisfy continuing-education requirements. See, <em>e.g., </em>LSBA, Articles of Incorporation, Art. 16, Rule 1.1(b) (effective 1987); La. Sup. Ct. Rule XXX (effective 1988). Even those few jurisdictions that do not impose mandatory continuing-education requirements mandate that attorneys represent their clients competently and encourage attorneys to engage in continuing study and education. See, <em>e.g., </em>Mass. Rule Prof. Conduct 1.1 and comment 6 (West 2006). Before Louisiana adopted continuing-education requirements, it imposed similar general competency requirements on its state bar. LSBA, Articles of Incorporation, Art. 16, EC 1—1, 1-2, DR 6-101 (West 1974) (effective 1971).</p>
<p id="b527-7">Attorneys who practice with other attorneys, such as in district attorney’s offices, also train on the job as they learn from more experienced attorneys. For instance, here in the Orleans Parish District Attorney’s Office, junior prosecutors were trained by senior prosecutors who supervised them as they worked together to prepare cases for trial, and trial chiefs oversaw the preparation of the cases. Senior attorneys also circulated court decisions and instructional memo-randa to keep the prosecutors abreast of relevant legal developments.</p>
<p id="b527-8">In addition, attorneys in all jurisdictions must satisfy character and fitness standards to receive a law license and are personally subject to an ethical regime designed to reinforce the profession’s standards. See, <em>e.g., </em>LSBA, Articles of Incorporation, Art. 14, § 7 (1985); see generally <em>id., </em>Art. 16 (1971) (Code of Professional Responsibility). Trial lawyers have a “duty to bring to bear such skill and <page-number citation-index="1" label="430">*430</page-number>knowledge as will render the trial a reliable adversarial testing process.” <em>Strickland </em>v. <em>Washington, </em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#688" aria-description="Citation for case: Strickland v. Washington">466 U.S. 668, 688</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">104 S. Ct. 2052</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">80 L. Ed. 2d 674</a></span> (1984). Prosecutors have a special “duty to seek justice, not merely to</p>
<p id="AvOL">[<span class="citation no-link">563 U.S. 66</span>]</p>
<p id="b528-4">convict.” LSBA, Articles of Incorporation, Art. 16, EC 7-13 (1971); ABA Standards for Criminal Justice 3-1.1(c) (2d ed. 1980). Among prosecutors’ unique ethical obligations is the duty to produce <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>evidence to the defense. See, <em>e.g., </em>LSBA, Articles of Incorporation, Art. 16, EC 7-13 (1971); ABA Model Rule of Prof. Conduct 3.8(d) (1984).<footnotemark>8</footnotemark> An attorney who violates his or her ethical obligations is subject to professional discipline, including sanctions, suspension, and disbarment. See, <em>e.g., </em>LSBA, Articles of Incorporation, Art. 15, §§ 5, 6 (1971); <em>id.., </em>Art. 16, DR 1-102; ABA Model Rule of Prof. Conduct 8.4 (1984).</p>
<p id="b528-5">In light of this regime of legal training and professional responsibility, recurring constitutional violations are not the “obvious consequence” of failing to provide prosecutors with formal in-house training about how to obey the law. <em>Bryan Cty., </em><span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/#409" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">520 U.S., at 409</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>. Prosecutors are not only equipped</p>
<p id="aye-dedup-1">[<span class="citation no-link">563 U.S. 67</span>]</p>
<p id="b528-7">but are also ethically bound to know what <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>entails and to perform legal research when they are uncertain. A district attorney is entitled to rely on prosecutors’ professional training and ethical obligations in the absence of specific reason, such as a pattern of violations, to believe that those tools are insufficient to prevent future constitutional violations in “the usual and recurring situations with which [the prosecutors] must deal.”<footnotemark>9</footnotemark> <em>Canton, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#391" aria-description="Citation for case: City of Canton v. Harris">489 U.S., at 391</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>. A licensed attorney making legal judgments, in his capacity as a prosecutor, about <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>material simply does not present the same “highly predictable” constitutional danger as <em>Canton’s </em>untrained officer.</p>
<p id="b528-8">A second significant difference between this case and the example in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>is the nuance of the allegedly necessary training. The <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>hypothetical assumes that the armed po<page-number citation-index="1" label="431">*431</page-number>lice officers have no knowledge at all of the constitutional limits on the use of deadly force. But it is undisputed here that the prosecutors in Connick’s office were familiar with the general <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>rule. Thompson’s complaint therefore cannot rely on the utter lack of an ability to cope with constitutional situations that underlies the <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>hypothetical, but rather must assert that prosecutors were not trained about particular <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>evidence or the specific scenario related to the violation in his case. That sort of nuance simply cannot support an inference of deliberate indifference here. As the Court said in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span>, </em>“[i]n virtually every instance where a person has had his or her constitutional rights violated by a city employee, a § 1983 plaintiff will be able to point to something the city ‘could have done’ to prevent the unfortunate incident.” <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#392" aria-description="Citation for case: City of Canton v. Harris">489 U.S., at 392</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span> (citing <em>Tuttle, </em><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#823" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U.S., at 823</a></span>, <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">105 S. Ct. 2427</a></span>, <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">85 L. Ed. 2d 791</a></span> (plurality opinion)).</p>
<p id="b529-4">[<span class="citation no-link">563 U.S. 68</span>]</p>
<p id="b529-5">Thompson suggests that the absence of any <em>formal </em>training sessions about <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>is equivalent to the complete absence of legal training that the Court imagined in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span>. </em>But failure-to-train liability is concerned with the substance of the training, not the particular instructional format. The statute does not provide plaintiffs or courts <em>carte blanche </em>to micromanage local governments throughout the United States.</p>
<p id="b529-7">We do not assume that prosecutors will always make correct <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>decisions or that guidance regarding specific <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>questions would not assist prosecutors. But showing merely that additional training would have been helpful in making difficult decisions does not establish municipal liability. “[P]rov[ing] that an injury or accident could have been avoided if an [employee] had had better or more training, sufficient to equip him to avoid the particular injury-causing conduct” will not suffice. <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#391" aria-description="Citation for case: City of Canton v. Harris"><em>Canton, supra, </em>at 391</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>. The possibility of single-incident liability that the Court left open in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>is not this case.<footnotemark>10</footnotemark></p>
<p id="b529-8">2</p>
<p id="b529-9">The dissent rejects our holding that <em>Canton’s </em>hypothesized single-incident liability does not, as a legal matter, encompass failure to train prosecutors in their <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>obligation. It would instead apply the <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>hypothetical to this case, and thus devotes almost all of its opinion to explaining</p>
<p id="AmMq">[<span class="citation no-link">563 U.S. 69</span>]</p>
<p id="b529-10">why the evidence supports liability under that theory.<footnotemark>11</footnotemark> But the dissent’s attempt to address our holding—by pointing out that not all prosecutors will necessarily have enrolled in <page-number citation-index="1" label="432">*432</page-number>criminal procedure class—misses the point. See <em>post, </em>at 106-107, 179 L. Ed. 2d, at 454-455. The reason why the <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>hypothetical is inapplicable</p>
<p id="avi-dedup-2">[<span class="citation no-link">563 U.S. 70</span>]</p>
<p id="b530-4">is that attorneys, unlike police officers, are equipped with the tools to find, interpret, and apply legal principles.</p>
<p id="b530-5">By the end of its opinion, however, the dissent finally reveals that its real disagreement is not with our holding today, but with this Court’s precedent. The dissent does not see “any reason,” <em>post, </em>at 108, 179 L. Ed. 2d, at 456, for the Court’s conclusion in <em>Bryan County </em>that a pattern of violations is “ordinarily necessary” to demonstrate deliberate indifference for purposes of failure to train, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/#409" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">520 U.S., at 409</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>. Cf. <em>id,, </em>at 406-408, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span> (explaining why a pattern of violations is ordinarily necessary). But cf. <em>post, </em>at 108, 179 L. Ed. 2d, at 455-456 (describing our reliance on <em>Bryan County </em>as “implying]” a new “limitation” on § 1983). As our precedent makes clear, proving that a municipality itself actually caused a constitutional violation by failing to train the offending employee presents “difficult problems of proof,” and we must adhere to a “stringent standard of fault,” lest municipal liability under § 1983 collapse into <em>respondeat superior,</em><footnotemark><em>12</em></footnotemark><em> Bryan Cty., supra, </em>at <page-number citation-index="1" label="433">*433</page-number>406, 410, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>; see <em>Canton, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#391" aria-description="Citation for case: City of Canton v. Harris">489 U.S., at 391-392</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>.</p>
<p id="b531-5">3</p>
<p id="b531-6">The District Court and the Court of Appeals panel erroneously believed that Thompson had proved deliberate indifference by showing the “obviousness” of a need for additional training. They based this conclusion on Con-nick’s awareness that (1) prosecutors would confront <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>issues while</p>
<p id="AHum">[<span class="citation no-link">563 U.S. 71</span>]</p>
<p id="b531-7">at the district attorney’s office; (2) inexperienced prosecutors were expected to understand <em>Brady’s </em>requirements; (3) <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>has gray areas that make for difficult choices; and (4) erroneous decisions regarding <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>evidence would result in constitutional violations. <span class="citation" data-id="64218"><a href="/opinion/64218/thompson-v-connick/#854" aria-description="Citation for case: Thompson v. Connick">553 F.3d, at 854</a></span>; App. to Pet. for Cert. 141a, <span class="citation no-link">2005 WL 3541035</span>, *13. This is insufficient.</p>
<p id="b531-8">It does not follow that, because <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>has gray areas and some <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>decisions are difficult, prosecutors will so obviously make wrong decisions that failing to train them amounts to “a decision by the city itself to violate the Constitution.” <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#395" aria-description="Citation for case: City of Canton v. Harris"><em>Canton, supra, </em>at 395</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span> (O’Connor, J., concurring in part and dissenting in part). To prove deliberate indifference, Thompson needed to show that Connick was on notice that, absent additional specified training, it was “highly predictable” that the prosecutors in his office would be confounded by those gray areas and make incorrect <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>decisions as a result. In fact, Thompson had to show that it was <em>so </em>predictable that failing to train the prosecutors amounted to <em>conscious disregard, </em>for defendants’ <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>rights. See <em>Bryan Cty., supra, </em>at 409, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>; <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#389" aria-description="Citation for case: City of Canton v. Harris"><em>Canton, supra, </em>at 389</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>. He did not do so.</p>
<p id="b531-9">III</p>
<p id="b531-10">The role of a prosecutor is to see that justice is done. <em>Berger </em>v. <em>United States, </em><span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U.S. 78, 88</a></span>, <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/" aria-description="Citation for case: Berger v. United States">55 S. Ct. 629</a></span>, <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/" aria-description="Citation for case: Berger v. United States">79 L. Ed. 1314</a></span> (1935). “It is as much [a prosecutor’s] duty to refrain from improper methods calculated to produce a wrongful conviction as it is to use every legitimate means to bring about a just one.” <em><span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/" aria-description="Citation for case: Berger v. United States">Ibid.</a></span> </em>By their own admission, the prosecutors who tried Thompson’s armed robbery case failed to carry out that responsibility. But the only issue before us is whether Connick, as the policymaker for the district attorney’s office, was deliberately indifferent to the need to train the attorneys under his authority.</p>
<p id="b531-11">We conclude that this case does not fall within the narrow range of “single-incident” liability hypothesized in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>as</p>
<p id="b531-12">[<span class="citation no-link">563 U.S. 72</span>]</p>
<p id="b531-13">a possible exception to the pattern of violations necessary to prove deliberate indifference in § 1983 actions alleging failure to train. The District Court should have granted Connick judgment as a matter of law on the failure-to-train claim because Thompson did not prove a pattern of similar violations that would “establish that the ‘policy of inaction’ [was] the functional equivalent of a decision by the city itself to violate the Constitution.” <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#395" aria-description="Citation for case: City of Canton v. Harris"><em>Canton, supra, </em>at 395</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span> (opinion of O’Connor, J.).</p>
<p id="b531-14">The judgment of the United States Court of Appeals for the Fifth Circuit is reversed.</p>
<p id="b531-15">It is so ordered.</p>
<footnote label="1">
<p id="b521-11">. After Thompson discovered the crime lab report, former Assistant District Attorney Michael Riehlmann revealed that Deegan had confessed to him in 1994 that he had “intentionally suppressed blood evidence in the armed robbery trial of John Thompson that in some way exculpated the defendant.’’ Record EX583; see also <em>id., </em>at 2677. Deegan apparently had been recently diagnosed with terminal cancer when he made his confession. Following a disciplinary complaint by the district attorney’s office, the Supreme Court of Louisiana reprimanded Riehl-mann for failing to disclose Deegan’s admission earlier. <em>In re Riehlmann, </em>2004-0680 (La. 1/19/05), <span class="citation" data-id="1755140"><a href="/opinion/1755140/in-re-riehlmann/" aria-description="Citation for case: In Re Riehlmann">891 So. 2d 1239</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b522-15">. Thompson testified in his own defense at the second trial and presented evidence suggesting that another man committed the murder. That man, the government’s key witness at the first murder trial, had died in the interval between the first and second trials.</p>
</footnote>
<footnote label="3">
<p id="b522-16">. Because Connick conceded that the failure to disclose the crime lab report violated <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>, </em>that question is not presented here, and we do not address it.</p>
</footnote>
<footnote label="4">
<p id="b523-14">. The District Court rejected Connick’s proposed deliberate indifference jury instruction— which would have required Thompson to prove a pattern of similar violations—for the same reasons as the summary judgment motion. Tr. 1013; Record 993; see also Tr. of Oral Arg. 26.</p>
</footnote>
<footnote label="5">
<p id="b523-15">. Because we conclude that Thompson failed to prove deliberate indifference, we need not reach causation. Thus, we do not address whether the alleged training deficiency, or some other cause, was the “ ‘moving force,’ ” <em>Canton </em>v. <em>Harris, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#389" aria-description="Citation for case: City of Canton v. Harris">489 U.S. 378, 389</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span> (1989) (quoting <em>Monell </em>v. <em>New York City Dept. of Social Servs., </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U.S. 658, 694</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">98 S. Ct. 2018</a></span>, <page-number citation-index="1" label="426">*426</page-number><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">56 L. Ed. 2d 611</a></span> (1978), and <em>Polk County </em>v. <em>Dodson, </em><span class="citation" data-id="9428551"><a href="/opinion/110589/polk-county-v-dodson/#326" aria-description="Citation for case: Polk County v. Dodson">454 U.S. 312, 326</a></span>, <span class="citation" data-id="9428551"><a href="/opinion/110589/polk-county-v-dodson/" aria-description="Citation for case: Polk County v. Dodson">102 S. Ct. 445</a></span>, <span class="citation" data-id="9428551"><a href="/opinion/110589/polk-county-v-dodson/" aria-description="Citation for case: Polk County v. Dodson">70 L. Ed. 2d 509</a></span> (1981)), that “actually caused’’ the failure to disclose the crime lab report, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#391" aria-description="Citation for case: City of Canton v. Harris"><em>Canton, supra, </em>at 391</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>.</p>
<p id="b524-11">The same cannot be said for the dissent, however. Affirming the verdict in favor of Thompson would require finding both that he proved deliberate indifference and that he proved causation. Perhaps unsurprisingly, the dissent has not conducted the second step of the analysis, which would require showing that the failure to provide particular training (which the dissent never clearly identifies) “actually caused’’ the flagrant—and quite possibly intentional—misconduct that occurred in this case. See <em>post, </em>at 98, 179 L. Ed. 2d, at 449 (opinion of Ginsburg, J.) (assuming that, “[h] ad Brady’s importance been brought home to prosecutors,’’ the violation at issue “surely” would not have occurred). The dissent believes that evidence that the prosecutors allegedly “misappre-hen[ded]” <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>proves causation. <em>Post, </em>at 104, n. 20, 179 L. Ed. 2d, at 453-454. Of course, if evidence of a need for training, by itself, were sufficient to prove that the lack of training “actually caused” the violation at issue, no causation requirement would be necessary because every plaintiff who satisfied the deliberate indifference requirement would necessarily satisfy the causation requirement.</p>
</footnote>
<footnote label="6">
<p id="b526-13">. Thompson had every incentive at trial to attempt to establish a pattern of similar violations, given that the jury instruction allowed the jury to find deliberate indifference based on, among other things, prosecutors’ “history of mishandling’’ similar situations. Record 1619.</p>
</footnote>
<footnote label="7">
<p id="b526-14">. Thompson also asserts that this case is not about a “single incident’’ because up to four prosecutors may have been responsible for the nondisclosure of the crime lab report and, according to his allegations, withheld additional evidence in his armed robbery and murder trials. But contemporaneous or subsequent conduct cannot establish a pattern of violations that would provide “notice to the cit[y] and the opportunity to conform to constitutional dictates <em>Canton, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#395" aria-description="Citation for case: City of Canton v. Harris">489 U.S., at 395</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span> (O’Connor, J., concurring in part and dissenting in part). Moreover, no court has ever found any of the other <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violations that Thompson alleges occurred in his armed robbery and murder trials.</p>
</footnote>
<footnote label="8">
<p id="b528-9">. The Louisiana State Bar Code of Professional Responsibility included a broad understanding of the prosecutor’s duty to disclose in 1985:</p>
<blockquote id="b528-10">“With respect to evidence and witnesses, the prosecutor has responsibilities different from those of a lawyer in private practice: the prosecutor should make timely disclosure to the defense of available evidence, known to him, that tends to negate the guilt of the accused, mitigate the degree of the offense, or reduce the punishment. Further, a prosecutor should not intentionally avoid pursuit of evidence merely because he believes it will damage the prosecution’s case or aid the accused.’’ LSBA, Articles of Incorporation, Art. 16, EC 7-13 (1971); see also ABA Model Rule of Prof. Conduct 3.8(d) (1984) (“The prosecutor in a criminal case shall. . . make timely disclosure to the defense of all evidence or information known to the prosecutor that tends to negate the guilt of the accused or mitigates the offense . . . ’’).</blockquote>
<p id="b528-11">In addition to these ethical rules, the Louisiana Code of Criminal Procedure, with which Louisiana prosecutors are no doubt familiar, in 1985 required prosecutors, upon order of the court, to permit inspection of evidence “favorable to the defendant . . . which [is] material and relevant to the issue of guilt or punishment,’’ La. Code Crim. Proc. Ann., Art. 718 (West 1981) (added 1977), as well as “any results or reports’’ of “scientific tests or experiments, made in connection with or material to the particular case,’’ if those reports are exculpatory or intended for use at trial, <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">id.,</a></span> </em>Art. 719.</p>
</footnote>
<footnote label="9">
<p id="b528-12">. Contrary to the dissent’s assertion, see <em>post, </em>at 108, n. 26, 179 L. Ed. 2d, at 456 (citing <em>post, </em>at 96-98, 179 L. Ed. 2d, at 448-449), a prosecutor’s youth is not a “specific reason’’ not to rely on professional training and ethical obligations. See <em>supra, </em>at 64-65, 179 L. Ed. 2d, at 428-429 (citing <em>United States </em>v. <em>Cronic, </em><span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/#658" aria-description="Citation for case: United States v. Cronic">466 U.S. 648, 658, 664</a></span>, <span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/" aria-description="Citation for case: United States v. Cronic">104 S. Ct. 2039</a></span>, <span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/" aria-description="Citation for case: United States v. Cronic">80 L. Ed. 2d 657</a></span> (1984)).</p>
</footnote>
<footnote label="10">
<p id="b529-11">. Thompson also argues that he proved deliberate indifference by “direct evidence of policymaker fault’’ and so, presumably, did not need to rely on circumstantial evidence at all. Brief for Respondent 37. In support, Thompson contends that Connick created a “culture of indifference’’ in the district attorney’s office, <em>id., </em>at 38, as evidenced by Connick’s own allegedly inadequate understanding of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>, </em>the office’s unwritten <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>policy that was later incorporated into a 1987 handbook, and an officewide “restrictive discovery policy,’’ Brief for Respondent 39-40. This argument is essentially an assertion that Connick’s office had an unconstitutional policy or custom. The jury rejected this claim, and Thompson does not challenge that finding.</p>
</footnote>
<footnote label="11">
<p id="b529-12">. The dissent spends considerable time finding new <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violations in Thompson’s trials. See <em>post, </em>at 81-90, 179 L. Ed. 2d, at 439-445. How these violations are relevant even to the dissent’s own legal analysis is “a mystery.’’ <em>Post, </em>at 81, n. 2, 179 L. Ed. 2d, at 439. The dissent does not list these violations among the “[a]bundant evidence’’ that it believes supports the jury’s finding that <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>training was obviously necessary. <em>Post, </em>at 93, 179 L. Ed. 2d, at 446. Nor does <page-number citation-index="1" label="432">*432</page-number>the dissent quarrel with our conclusion that contemporaneous or subsequent conduct cannot establish a pattern of violations. The only point appears to be to highlight what the dissent sees as sympathetic, even if legally irrelevant, facts.</p>
<p id="b530-8">In any event, the dissent’s findings are highly suspect. In finding two of the “new” violations, the dissent belatedly tries to reverse the Court of Appeals’ 1998 decision that those <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>claims were “without merit.” Compare <em>Thompson </em>v. <em>Cain, </em><span class="citation" data-id="16134"><a href="/opinion/16134/thompson-v-cain/#806" aria-description="Citation for case: Thompson v. Cain">161 F.3d 802, 806-808</a></span> (CA5) <em>(rejectingBrady </em>claims regarding the Perkins-Liuzza audiotapes and the Perkins police report), with <em>post, </em>at 85-86, 179 L. Ed. 2d, at 442-443 (concluding that these were <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violations). There is no basis to the dissent’s suggestion that materially new facts have called the Court of Appeals’ 1998 decision into question. Cf. <em>State </em>v. <em>Thompson, </em>2002-0361, p. 6 (La. App. 7/17/02), <span class="citation" data-id="1714044"><a href="/opinion/1714044/state-v-thompson/#555" aria-description="Citation for case: State v. Thompson">825 So. 2d 552, 555</a></span> (noting Thompson’s admission that some of his current <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>claims “ha[ve] been rejected by both the Louisiana Supreme Court and the federal courts”). Regarding the bloodstained swatch, which the dissent asserts prosecutors “blocked” the defense from inspecting by sending it to the crime lab for testing, <em>post, </em>at 84, 179 L. Ed. 2d, at 441, Thompson’s counsel conceded at oral argument that trial counsel had access to the evidence locker where the swatch was recorded as evidence. See Tr. of OralArg. 37, 42; Record EX42, EX43 (evidence card identifying “One (1) Piece of Victims <em>[sic] </em>Right Pants Leg, W/Blood” among the evidence in the evidence locker and indicating that some evidence had been checked out); Tr. 401 (testimony from Thompson’s counsel that he “[w]ent down to the evidence room and checked all of the evidence”); <em>id., </em>at 103, 369-370, 586, 602 (testimony that evidence card was “available to the public,” would have been available to Thompson’s counsel, and would have been seen by Thompson’s counsel because it was stapled to the evidence bag in “the normal process”). Moreover, the dissent cannot seriously believe that the jury could have found <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violations—indisputably, questions of law. See <em>post, </em>at 89, n. 10, 92, n. 11, 179 L. Ed. 2d, at 444-445, 446.</p>
</footnote>
<footnote label="12">
<p id="b530-9">. Although the dissent acknowledges that “deliberate indifference liability and <em>respondeat superior </em>liability are not one and the same,” the opinion suggests that it believes otherwise. <em>Post, </em>at 109, n. 28, 179 L. Ed. 2d, at 456; see, <em>e.g., post, </em>at 109, 179 L. Ed. 2d, at 456 (asserting that “the buck stops with [the district attorney]”); <em>post, </em>at 100, 179 L. Ed. 2d, at 451 (suggesting municipal liability attaches when “the prosecutors” themselves are “deliberately indifferent to what the law requires”). We stand by the longstanding rule—reaffirmed by a unanimous Court earlier this Term—that to prove a violation of § 1983, a plaintiff must prove that “the municipality’s own wrongful conduct” caused his injury, not that the municipality is ultimately responsible for the torts of its employees. <em>Los Angeles County </em>v. <em>Humphries, ante, </em><span class="citation" data-id="180037"><a href="/opinion/180037/los-angeles-county-v-humphries/#38" aria-description="Citation for case: Los Angeles County v. Humphries">562 U.S. 29, 38</a></span>, <span class="citation" data-id="180037"><a href="/opinion/180037/los-angeles-county-v-humphries/" aria-description="Citation for case: Los Angeles County v. Humphries">131 S. Ct. 447</a></span>, <span class="citation" data-id="180037"><a href="/opinion/180037/los-angeles-county-v-humphries/" aria-description="Citation for case: Los Angeles County v. Humphries">178 L. Ed. 2d 460</a></span> (2010); see <span class="citation" data-id="180037"><a href="/opinion/180037/los-angeles-county-v-humphries/#35" aria-description="Citation for case: Los Angeles County v. Humphries"><em>id., </em>at 35, 36</a></span>, <span class="citation multiple-matches"><a href="/c/S.%20Ct./131/447/">131 S. Ct. 447</a></span>, <span class="citation multiple-matches"><a href="/c/L.%20Ed.%202d/178/460/">178 L. Ed. 2d 460</a></span> (citing <em>Monell, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#691" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U.S., at 691</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">98 S. Ct. 2018</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">56 L. Ed. 2d 611</a></span>).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Coolidge v. New Hampshire.md  (`case`, 7 assertions)

### content_page

```
---
title: "Coolidge v. New Hampshire"
type: case
citation: "403 U.S. 443 (1971)"
parallel_cite: "91 S. Ct. 2022; 29 L. Ed. 2d 564"
neutral_cite: 1971 U.S. LEXIS 25
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1971
date_decided: 1971-06-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 1971-06-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Coolidge v. New Hampshire
  varies_by_point: true
  scope_note: "Horton v. California (1990) abandoned the inadvertence requirement of the Coolidge plurality's plain-view formulation; the prior-justification and immediately-apparent requirements survive."
  point_overrides:
    - point: legacy-limited-coolidge-v-new-hampshire
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: Horton v. California
          cluster_id: 112448
          cite: 496 U.S. 128
          field_ii: limited
      scope_note: "Horton v. California (1990) abandoned the inadvertence requirement of the Coolidge plurality's plain-view formulation; the prior-justification and immediately-apparent requirements survive."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108377/coolidge-v-new-hampshire/"
  cluster_id: 108377
  opinion_id: 108377
  identity_checked: true
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Key — Anchor"
  - page: "[[The Neutral and Detached Magistrate]]"
    role: "Related (cross-doctrine)"
related: ["[[Horton v. California]]", "[[Arizona v. Hicks]]", "[[Texas v. Brown]]"]
aliases: []
tags: ["case", "fourth-amendment", "plain-view", "warrant-requirement", "inadvertence", "immediately-apparent"]
holding: "ORIGIN of the modern plain-view doctrine (Stewart plurality). Plain view justifies a warrantless seizure only where the incriminating…"
lake:
  record_id: Coolidge v. New Hampshire
  status: verified
  projected_at: 2026-07-06
---

# Coolidge v. New Hampshire

*403 U.S. 443 (1971)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)* — inadvertence prong abandoned by [[Horton v. California]]
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating a murder, police seized Coolidge's car from his driveway under a warrant issued by the state attorney general (who was leading the prosecution) and later searched it, vacuuming up incriminating particles. The Court invalidated the warrant because it was not issued by a neutral and detached magistrate, then addressed whether the seizure could be sustained under the [[Plain View Doctrine|plain-view doctrine]].

## Issue
What conditions justify a warrantless seizure of evidence under the "plain view" doctrine.

## Rule
Plain view supplements a prior justified intrusion; it does not authorize a planned warrantless seizure on its own. "What the 'plain view' cases have in common is that the police officer in each of them had a prior justification for an intrusion in the course of which he came inadvertently across a piece of evidence incriminating the accused." — 403 U.S. 443, 466. ^pin-466

"[T]he extension of the original justification is legitimate only where it is immediately apparent to the police that they have evidence before them; the 'plain view' doctrine may not be used to extend a general exploratory search from one object to another until something incriminating at last emerges." — *Id.* ^pin-466a

*(The plurality's inadvertence requirement was later abandoned by [[Horton v. California]]; the prior-justification and immediately-apparent requirements remain.)*

## Application
The police knew about Coolidge's car well in advance and seized it from the driveway pursuant to an invalid warrant — a planned seizure of a known, anticipated object, not an inadvertent discovery during a lawful intrusion. Because the seizure was neither inadvertent nor supported by a valid warrant, the [[Plain View Doctrine|plain-view doctrine]] did not save it on these facts.

## Conclusion
The warrantless seizure of the car could not be justified as plain view; the evidence should have been suppressed. *Coolidge* states the modern plain-view framework (Stewart plurality).

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS** for the surviving requirements.
- **Inadvertence requirement abandoned by** [[Horton v. California]] (1990): a plain-view seizure need not be inadvertent so long as the officer is lawfully present and the incriminating character is immediately apparent. *Coolidge*'s prior-justification and immediately-apparent requirements continue to govern; [[Arizona v. Hicks]] confirmed that "immediately apparent" requires probable cause.

## Appears on
- [[Plain View Doctrine]] — *Key — Anchor*
- [[The Neutral and Detached Magistrate]] — *Related (cross-doctrine)*

## Sources
- *Coolidge v. New Hampshire*, 403 U.S. 443 (1971) — https://www.courtlistener.com/opinion/108377/coolidge-v-new-hampshire/ — pinpoint: 466.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f98cdad58be445c5", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "403 U.S. 443 (1971)", "court": "U.S. Supreme Court", "neutral_cite": "1971 U.S. LEXIS 25", "official_citation_present": true, "parallel_cite": "91 S. Ct. 2022; 29 L. Ed. 2d 564", "title": "Coolidge v. New Hampshire", "year": "1971"}}
{"assertion_id": "02a0cee1aea6af47", "dimension": "support", "kind": "home_role", "locator": {"home": "Plain View Doctrine"}, "payload": {"home": "Plain View Doctrine", "role": "Key — Anchor", "title": "Coolidge v. New Hampshire"}}
{"assertion_id": "e1270ff9c915d1bb", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "ORIGIN of the modern plain-view doctrine (Stewart plurality). Plain view justifies a warrantless seizure only where the incriminating…", "title": "Coolidge v. New Hampshire"}}
{"assertion_id": "f758909d9981bf96", "dimension": "support", "kind": "home_role", "locator": {"home": "The Neutral and Detached Magistrate"}, "payload": {"home": "The Neutral and Detached Magistrate", "role": "Related (cross-doctrine)", "title": "Coolidge v. New Hampshire"}}
{"assertion_id": "3a79f8808e02f27c", "dimension": "treatment", "kind": "treatment_override", "locator": {"point": "legacy-limited-coolidge-v-new-hampshire"}, "payload": {"by": [{"cite": "496 U.S. 128", "cluster_id": "112448", "field_ii": "limited", "name": "Horton v. California"}], "field_i_validity": "caution", "point": "legacy-limited-coolidge-v-new-hampshire", "point_label": "Legacy limited treatment point", "s3_binding_status": "provisional", "title": "Coolidge v. New Hampshire"}}
{"assertion_id": "419a9d8cfd382722", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1971-06-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Coolidge v. New Hampshire", "field_i_validity": "caution", "scope_note": "Horton v. California (1990) abandoned the inadvertence requirement of the Coolidge plurality's plain-view formulation; the prior-justification and immediately-apparent requirements survive.", "title": "Coolidge v. New Hampshire", "varies_by_point": "true"}}
{"assertion_id": "f7e7428223117ed3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Coolidge v. New Hampshire"}}
```

### lake record — Coolidge v. New Hampshire

```json
{
  "schema_version": "s2.v1",
  "record_id": "Coolidge v. New Hampshire",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Coolidge v. New Hampshire",
    "case_name_short": "Coolidge",
    "case_name_full": "Coolidge v. New Hampshire",
    "input_case_name": "Coolidge v. New Hampshire",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1971-06-21",
    "year": 1971,
    "docket": null,
    "cluster_id": 108377,
    "lead_opinion_id": 108377,
    "sibling_ids": [
      108377,
      9424643,
      9424644,
      9424645,
      9424646,
      9424647
    ],
    "absolute_url": "/opinion/108377/coolidge-v-new-hampshire/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "403 U.S. 443",
      "volume": "403",
      "reporter": "U.S.",
      "page": "443",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "91 S. Ct. 2022",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "2022",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "29 L. Ed. 2d 564",
        "volume": "29",
        "reporter": "L. Ed. 2d",
        "page": "564",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1971 U.S. LEXIS 25",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "25",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "403 U.S. 443",
        "volume": "403",
        "reporter": "U.S.",
        "page": "443",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 S. Ct. 2022",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "2022",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "29 L. Ed. 2d 564",
        "volume": "29",
        "reporter": "L. Ed. 2d",
        "page": "564",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1971 U.S. LEXIS 25",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "25",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "403 U.S. 443",
    "official_selection": {
      "court_class": "scotus",
      "selected": "403 U.S. 443",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-466",
      "page": null,
      "quote": "doctrine. ## Rule Plain view supplements a prior justified intrusion; it does not authorize a planned warrantless seizure on its own.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-466a",
      "page": null,
      "quote": "[T]he extension of the original justification is legitimate only where it is immediately apparent to the police that they have evidence before them; the 'plain view' doctrine may not be used to extend a general exploratory search from one object to another until something incriminating at last emerges.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "1971-06-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Coolidge v. New Hampshire",
    "varies_by_point": true,
    "scope_note": "Horton v. California (1990) abandoned the inadvertence requirement of the Coolidge plurality's plain-view formulation; the prior-justification and immediately-apparent requirements survive.",
    "point_overrides": [
      {
        "point": "legacy-limited-coolidge-v-new-hampshire",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "Horton v. California",
            "cluster_id": 112448,
            "cite": "496 U.S. 128",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Horton v. California (1990) abandoned the inadvertence requirement of the Coolidge plurality's plain-view formulation; the prior-justification and immediately-apparent requirements survive."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "Horton v. California",
          "cluster_id": 112448,
          "cite": "496 U.S. 128",
          "field_ii": "limited"
        },
        "field_ii": "limited",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:limited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Louisiana v. K.B.",
          "cluster_id": 10581696,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Coolidge v. New Hampshire:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bock (A169480)",
          "cluster_id": 10134134,
          "cite": [
            "310 Or. App. 329",
            "485 P.3d 931"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Coolidge v. New Hampshire:lane1_negative"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Illinois",
          "cluster_id": 109304,
          "cite": [
            "45 L. Ed. 2d 416",
            "95 S. Ct. 2254",
            "422 U.S. 590",
            "1975 U.S. LEXIS 82"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108377 OR 9424643 OR 9424644 OR 9424645 OR 9424646 OR 9424647) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTY3MTIzMjAwMDAwJnM9NDY1ODI3NyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108377+OR+9424643+OR+9424644+OR+9424645+OR+9424646+OR+9424647%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108377 OR 9424643 OR 9424644 OR 9424645 OR 9424646 OR 9424647)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzgzJnM9MTA5NTA0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108377+OR+9424643+OR+9424644+OR+9424645+OR+9424646+OR+9424647%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108377 OR 9424643 OR 9424644 OR 9424645 OR 9424646 OR 9424647)",
        "reviewed": 99,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 99,
        "triage_read": 2,
        "triage_snippet_classified": 97
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108377 OR 9424643 OR 9424644 OR 9424645 OR 9424646 OR 9424647)",
    "indexed_citing_opinions": 5998,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108377,
        "count": 5499,
        "count_source": "search"
      },
      {
        "opinion_id": 9424643,
        "count": 661,
        "count_source": "search"
      },
      {
        "opinion_id": 9424644,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424645,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424646,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424647,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 9038,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/coolidge-v-new-hampshire.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNDA0NTgmcz0xMDU1NjA2MyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28108377+OR+9424643+OR+9424644+OR+9424645+OR+9424646+OR+9424647%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108377,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 100621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 101180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 103100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107952,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 108186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 108301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 108302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 108335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 263859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 291194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 293653,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 1139971,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 1501475,
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
    "date_created": "2026-07-05T01:09:56Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T01:10:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T01:10:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:31Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T01:10:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Coolidge v. New Hampshire (truncated)

```
<div>
<center><b><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U.S. 443</a></span> (1971)</b></center>
<center><h1>COOLIDGE<br>
v.<br>
NEW HAMPSHIRE.</h1></center>
<center>No. 323.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 12, 1971</center>
<center>Decided June 21, 1971</center>
CERTIORARI TO THE SUPREME COURT OF NEW HAMPSHIRE.
<p><span class="star-pagination">*445</span> <i>Archibald Cox,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./400/814/">400 U. S. 814</a></span>, argued the cause for petitioner. With him on the briefs were <i>Matthias J. Reynolds, John A. Graf,</i> and <i>Robert L. Chiesa.</i></p>
<p><i>Alexander J. Kalinski</i> argued the cause for respondent. With him on the brief was <i>Warren B. Rudman,</i> Attorney General of New Hampshire.</p>
<p>MR. JUSTICE STEWART delivered the opinion of the Court.<sup>[*]</sup></p>
<p>We are called upon in this case to decide issues under the Fourth and Fourteenth Amendments arising in the context of a state criminal trial for the commission of a particularly brutal murder. As in every case, our single duty is to determine the issues presented in accord with the Constitution and the law.</p>
<p>Pamela Mason, a 14-year-old girl, left her home in Manchester, New Hampshire, on the evening of January 13, 1964, during a heavy snowstorm, apparently in response to a man's telephone call for a babysitter. Eight days later, after a thaw, her body was found by the side of a major north-south highway several miles away. She had been murdered. The event created great alarm in the area, and the police immediately began a massive investigation.</p>
<p>On January 28, having learned from a neighbor that the petitioner, Edward Coolidge, had been away from home on the evening of the girl's disappearance, the police went to his house to question him. They asked <span class="star-pagination">*446</span> him, among other things, if he owned any guns, and he produced three, two shotguns and a rifle. They also asked whether he would take a lie-detector test concerning his account of his activities on the night of the disappearance. He agreed to do so on the following Sunday, his day off. The police later described his attitude on the occasion of this visit as fully "cooperative." His wife was in the house throughout the interview.</p>
<p>On the following Sunday, a policeman called Coolidge early in the morning and asked him to come down to the police station for the trip to Concord, New Hampshire, where the lie-detector test was to be administered. That evening, two plainclothes policemen arrived at the Coolidge house, where Mrs. Coolidge was waiting with her mother-in-law for her husband's return. These two policemen were not the two who had visited the house earlier in the week, and they apparently did not know that Coolidge had displayed three guns for inspection during the earlier visit. The plainclothesmen told Mrs. Coolidge that her husband was in "serious trouble" and probably would not be home that night. They asked Coolidge's mother to leave, and proceeded to question Mrs. Coolidge. During the course of the interview they obtained from her four guns belonging to Coolidge, and some clothes that Mrs. Coolidge thought her husband might have been wearing on the evening of Pamela Mason's disappearance.</p>
<p>Coolidge was held in jail on an unrelated charge that night, but he was released the next day.<sup>[1]</sup> During the ensuing two and a half weeks, the State accumulated a quantity of evidence to support the theory that it was he who had killed Pamela Mason. On February 19, the results of the investigation were presented at a meeting between the police officers working on the case and the <span class="star-pagination">*447</span> State Attorney General, who had personally taken charge of all police activities relating to the murder, and was later to serve as chief prosecutor at the trial. At this meeting, it was decided that there was enough evidence to justify the arrest of Coolidge on the murder charge and a search of his house and two cars. At the conclusion of the meeting, the Manchester police chief made formal application, under oath, for the arrest and search warrants. The complaint supporting the warrant for a search of Coolidge's Pontiac automobile, the only warrant that concerns us here, stated that the affiant "has probable cause to suspect and believe, and does suspect and believe, and herewith offers satisfactory evidence, that there are certain objects and things used in the Commission of said offense, now kept, and concealed in or upon a certain vehicle, to wit: 1951 Pontiac two-door sedan. . . ." The warrants were then signed and issued by the Attorney General himself, acting as a justice of the peace. Under New Hampshire law in force at that time, all justices of the peace were authorized to issue search warrants. N. H. Rev. Stat. Ann. § 595:1 (repealed 1969).</p>
<p>The police arrested Coolidge in his house on the day the warrant issued. Mrs. Coolidge asked whether she might remain in the house with her small child, but was told that she must stay elsewhere, apparently in part because the police believed that she would be harassed by reporters if she were accessible to them. When she asked whether she might take her car, she was told that both cars had been "impounded," and that the police would provide transportation for her. Some time later, the police called a towing company, and about two and a half hours after Coolidge had been taken into custody the cars were towed to the police station. It appears that at the time of the arrest the cars were parked in the Coolidge driveway, and that although dark had fallen <span class="star-pagination">*448</span> they were plainly visible both from the street and from inside the house where Coolidge was actually arrested. The 1951 Pontiac was searched and vacuumed on February 21, two days after it was seized, again a year later, in January 1965, and a third time in April 1965.</p>
<p>At Coolidge's subsequent jury trial on the charge of murder, vacuum sweepings, including particles of gun powder, taken from the Pontiac were introduced in evidence against him, as part of an attempt by the State to show by microscopic analysis that it was highly probable that Pamela Mason had been in Coolidge's car.<sup>[2]</sup> Also introduced in evidence was one of the guns taken by the police on their Sunday evening visit to the Coolidge housea .22-caliber Mossberg rifle, which the prosecution claimed was the murder weapon. Conflicting ballistics testimony was offered on the question whether the bullets found in Pamela Mason's body had been fired from this rifle. Finally, the prosecution introduced vacuum sweepings of the clothes taken from the Coolidge house that same Sunday evening, and attempted to show through microscopic analysis that there was a high probability that the clothes had been in contact with Pamela Mason's body. Pretrial motions to suppress all this evidence were referred by the trial judge to the New Hampshire Supreme Court, which ruled the evidence admissible. 106 N. H. 186, <span class="citation" data-id="2286547"><a href="/opinion/2286547/state-v-coolidge/" aria-description="Citation for case: State v. Coolidge">208 A. 2d 322</a></span>. The jury found Coolidge guilty and he was sentenced to life imprisonment. The New Hampshire Supreme Court affirmed the judgment of conviction, 109 N. H. 403, <span class="citation" data-id="2326188"><a href="/opinion/2326188/state-v-coolidge/" aria-description="Citation for case: State v. Coolidge">260 A. 2d 547</a></span>, and we granted certiorari to consider the constitutional questions raised by the admission of this evidence against Coolidge at his trial. <span class="citation multiple-matches"><a href="/c/U.%20S./399/926/">399 U. S. 926</a></span>.</p>
<p></p>
<h2>
<span class="star-pagination">*449</span> I</h2>
<p>The petitioner's first claim is that the warrant authorizing the seizure and subsequent search of his 1951 Pontiac automobile was invalid because not issued by a "neutral and detached magistrate." Since we agree with the petitioner that the warrant was invalid for this reason, we need not consider his further argument that the allegations under oath supporting the issuance of the warrant were so conclusory as to violate relevant constitutional standards. Cf. <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span>; <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span>.</p>
<p>The classic statement of the policy underlying the warrant requirement of the Fourth Amendment is that of Mr. Justice Jackson, writing for the Court in <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, 13-14:</p>
<blockquote>"The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime. Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers. . . . When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent."</blockquote>
<p>Cf. <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#464" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 464</a></span>; <i>Giordenello</i> v. <i>United States, supra,</i> at 486. <i>Wong Sun</i> v. <span class="star-pagination">*450</span> <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#481" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 481-482</a></span>; <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#356" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 356-357</a></span>.</p>
<p>In this case, the determination of probable cause was made by the chief "government enforcement agent" of the Statethe Attorney Generalwho was actively in charge of the investigation and later was to be chief prosecutor at the trial. To be sure, the determination was formalized here by a writing bearing the title "Search Warrant," whereas in <i><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson</a></span></i> there was no piece of paper involved, but the State has not attempted to uphold the warrant on any such artificial basis. Rather, the State argues that the Attorney General, who was unquestionably authorized as a justice of the peace to issue warrants under then-existing state law, did in fact act as a "neutral and detached magistrate." Further, the State claims that <i>any</i> magistrate, confronted with the showing of probable cause made by the Manchester chief of police, would have issued the warrant in question. To the first proposition it is enough to answer that there could hardly be a more appropriate setting than this for a <i>per se</i> rule of disqualification rather than a case-by-case evaluation of all the circumstances. Without disrespect to the state law enforcement agent here involved, the whole point of the basic rule so well expressed by Mr. Justice Jackson is that prosecutors and policemen simply cannot be asked to maintain the requisite neutrality with regard to their own investigationsthe "competitive enterprise" that must rightly engage their single-minded attention.<sup>[3]</sup> Cf. <i>Mancusi</i> v. <i>DeForte,</i> <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#371" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364, 371</a></span>. As for the proposition that the existence of probable cause renders noncompliance with the warrant procedure an irrelevance, <span class="star-pagination">*451</span> it is enough to cite <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span>, decided in 1925:</p>
<blockquote>"Belief, however well founded, that an article sought is concealed in a dwelling house furnishes no justification for a search of that place without a warrant. And such searches are held unlawful notwithstanding facts unquestionably showing probable cause."</blockquote>
<p>See also <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#497" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 497-498</a></span>; <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span>. ("[T]he rights . . . against unlawful search and seizure are to be protected even if the same result might have been achieved in a lawful way.")</p>
<p>But the New Hampshire Supreme Court, in upholding the conviction, relied upon the theory that even if the warrant procedure here in issue would clearly violate the standards imposed on the Federal Government by the Fourth Amendment, it is not forbidden the States under the Fourteenth. This position was premised on a passage from the opinion of this Court in <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span>, 31:</p>
<blockquote>"Preliminary to our examination of the search and seizures involved here, it might be helpful for us to indicate what was not decided in <i>Mapp</i> [v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>]. First, it must be recognized that the `principles governing the admissibility of evidence in federal criminal trials have not been restricted . . . to those derived solely from the Constitution. In the exercise of its supervisory authority over the administration of criminal justice in the federal courts . . . this Court has . . . formulated rules of evidence to be applied in federal criminal prosecutions.' <i>McNabb</i> v. <i>United States,</i> <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U. S. 332</a></span>, 341 . . . <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span>,</i> however, established no assumption by this Court of supervisory authority over state courts . . . and, consequently, it implied no total <span class="star-pagination">*452</span> obliteration of state laws relating to arrests and searches in favor of federal law. <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> sounded no death knell for our federalism; rather, it echoed the sentiment of <i>Elkins</i> v. <i>United States, supra,</i> at 221, that `a healthy federalism depends upon the avoidance of needless conflict between state and federal courts' by itself urging that `[f]ederal-state cooperation in the solution of crime under constitutional standards will be promoted, if only by recognition of their now mutual obligation to respect <i>the same fundamental criteria</i> in their approaches.' <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#658" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 658</a></span>." (Emphasis in <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span>.</i>)</blockquote>
<p>It is urged that the New Hampshire statutes which at the time of the searches here involved permitted a law enforcement officer himself to issue a warrant was one of those "workable rules governing arrests, searches and seizures to meet `the practical demands of effective criminal investigation and law enforcement' in the States," <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#34" aria-description="Citation for case: Ker v. California"><i>id.,</i> at 34</a></span>, authorized by <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span>.</i></p>
<p>That such a procedure was indeed workable from the point of view of the police is evident from testimony at the trial in this case:</p>
<blockquote>"The Court: You mean that another police officer issues these [search warrants]?</blockquote>
<blockquote>"The Witness: Yes. Captain Couture and Captain Shea and Captain Loveren are J. P.'s.</blockquote>
<blockquote>"The Court: Well, let me ask you, Chief, your answer is to the effect that you never go out of the department for the Justice of the Peace?</blockquote>
<blockquote>"The Witness: It hasn't been ourpolicy to go out of the department.</blockquote>
<blockquote>"Q. Right. Your policy and experience, is to have a fellow police officer take the warrant in the capacity of Justice of the Peace?</blockquote>
<blockquote>"A. That has been our practice."</blockquote>
<p><span class="star-pagination">*453</span> But it is too plain for extensive discussion that this now abandoned New Hampshire method of issuing "search warrants" violated a fundamental premise of both the Fourth and Fourteenth Amendmentsa premise fully developed and articulated long before this Court's decisions in <i>Ker</i> v. <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">California, supra</a></span></i><i>,</i> and <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>. As Mr. Justice Frankfurter put it in <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>, 27-28:</p>
<blockquote>"The security of one's privacy against arbitrary intrusion by the policewhich is at the core of the Fourth Amendmentis basic to a free society. It is therefore implicit in `the concept of ordered liberty' and as such enforceable against the States through the Due Process Clause. The knock at the door, whether by day or by night, as a prelude to a search, without authority of law but solely on the authority of the police, did not need the commentary of recent history to be condemned . . . ."</blockquote>
<p>We find no escape from the conclusion that the seizure and search of the Pontiac automobile cannot constitutionally rest upon the warrant issued by the state official who was the chief investigator and prosecutor in this case. Since he was not the neutral and detached magistrate required by the Constitution, the search stands on no firmer ground than if there had been no warrant at all. If the seizure and search are to be justified, they must, therefore, be justified on some other theory.</p>
<p></p>
<h2>II</h2>
<p>The State proposes three distinct theories to bring the facts of this case within one or another of the exceptions to the warrant requirement. In considering them, we must not lose sight of the Fourth Amendment's fundamental guarantee. Mr. Justice Bradley's admonition in his opinion for the Court almost a century ago in <i>Boyd</i> <span class="star-pagination">*454</span> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 635</a></span>, is worth repeating here:</p>
<blockquote>"It may be that it is the obnoxious thing in its mildest and least repulsive form; but illegitimate and unconstitutional practices get their first footing in that way, namely, by silent approaches and slight deviations from legal modes of procedure. This can only be obviated by adhering to the rule that constitutional provisions for the security of person and property should be liberally construed. A close and literal construction deprives them of half their efficacy, and leads to gradual depreciation of the right, as if it consisted more in sound than in substance. It is the duty of courts to be watchful for the constitutional rights of the citizen, and against any stealthy encroachments thereon."<sup>[4]</sup></blockquote>
<p>Thus the most basic constitutional rule in this area is that "searches conducted outside the judicial process, without prior approval by judge or magistrate, are <i>per se</i> <span class="star-pagination">*455</span> unreasonable under the Fourth Amendmentsubject only to a few specifically established and well-delineated exceptions."<sup>[5]</sup> The exceptions are "jealously and carefully drawn,"<sup>[6]</sup> and there must be "a showing by those who seek exemption . . . that the exigencies of the situation made that course imperative."<sup>[7]</sup> "[T]he burden is on those seeking the exemption to show the need for it."<sup>[8]</sup> In times of unrest, whether caused by crime or racial conflict or fear of internal subversion, this basic law and the values that it represents may appear unrealistic or "extravagant" to some. But the values were those of the authors of our fundamental constitutional concepts. In times not altogether unlike our own they wonby legal and constitutional means in England,<sup>[9]</sup> and by revolution on this continenta right of personal security against arbitrary intrusions by official power. If times have changed, reducing everyman's scope to do as he pleases in an urban and industrial world, the changes have made the values served by the Fourth Amendment more, not less, important.<sup>[10]</sup></p>
<p></p>
<h2>A</h2>
<p>The State's first theory is that the seizure on February 19 and subsequent search of Coolidge's Pontiac were "incident" to a valid arrest. We assume that the arrest of Coolidge inside his house was valid, so that the first condition of a warrantless "search incident" is met. <i>Whiteley</i> v. <i>Warden,</i> <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560</a></span>, 567 n. 11. And since the events in issue took place in 1964, we assess the State's argument <span class="star-pagination">*456</span> in terms of the law as it existed before <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>, which substantially restricted the "search incident" exception to the warrant requirement, but did so only prospectively. <i>Williams</i> v. <i>United States,</i> <span class="citation" data-id="9424503"><a href="/opinion/108301/williams-v-united-states/" aria-description="Citation for case: Williams v. United States">401 U. S. 646</a></span>. But even under pre-<span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California"><i>Chimel</i></a></span> law, the State's position is untenable.</p>
<p>The leading case in the area before <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> was <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>, which was taken to stand "for the proposition, <i>inter alia,</i> that a warrantless search `incident to a lawful arrest' may generally extend to the area that is considered to be in the `possession' or under the `control' of the person arrested." <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#760" aria-description="Citation for case: Chimel v. California"><i>Chimel, supra,</i> at 760</a></span>. In this case, Coolidge was arrested inside his house; his car was outside in the driveway. The car was not touched until Coolidge had been removed from the scene. It was then seized and taken to the station, but it was not actually searched until two days later.</p>
<p>First, it is doubtful whether the police could have carried out a contemporaneous search of the car under <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> standards. For this Court has repeatedly held that, even under <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span>,</i> "[a] search may be incident to an arrest ` "only if it is substantially contemporaneous with the arrest and is confined to the <i>immediate</i> vicinity of the arrest. . . ." ' " <i>Vale</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#33" aria-description="Citation for case: Vale v. Louisiana">399 U. S. 30, 33</a></span>, quoting from <i>Shipley</i> v. <i>California,</i> <span class="citation" data-id="9424104"><a href="/opinion/107982/shipley-v-california/#819" aria-description="Citation for case: Shipley v. California">395 U. S. 818, 819</a></span>, quoting from <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#486" aria-description="Citation for case: Stoner v. California">376 U. S. 483, 486</a></span>. (Emphasis in <i><span class="citation" data-id="9424104"><a href="/opinion/107982/shipley-v-california/" aria-description="Citation for case: Shipley v. California">Shipley</a></span>.</i>) Cf. <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S., at 30-31</a></span>; <i>James</i> v. <i>Louisiana,</i> <span class="citation" data-id="107102"><a href="/opinion/107102/james-v-louisiana/" aria-description="Citation for case: James v. Louisiana">382 U. S. 36</a></span>. These cases make it clear beyond any question that a lawful pre-<span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California"><i>Chimel</i></a></span> arrest of a suspect outside his house could never by itself justify a warrantless search inside the house. There is nothing in search-incident doctrine (as opposed to the special rules for automobiles and evidence in "plain view," to be considered below) that suggests <span class="star-pagination">*457</span> a different result where the arrest is made inside the house and the search outside and at some distance away.<sup>[11]</sup></p>
<p>Even assuming, <i>arguendo,</i> that the police might have searched the Pontiac in the driveway when they arrested Coolidge in the house, <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span>, makes plain that they could not legally seize the car, remove it, and search it at their leisure without a warrant. In circumstances virtually identical to those here, MR. JUSTICE BLACK'S opinion for a unanimous Court held that "[o]nce an accused is under arrest and in custody, then a search [of his car] made at another place, without a warrant, is simply not incident to the arrest." <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States"><i>Id.,</i> at 367</a></span>. <i>Dyke</i> v. <i>Taylor Implement Mfg. Co.,</i> <span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S. 216</a></span> Cf. <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#47" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 47</a></span>. Search-incident doctrine, in short, has no applicability to this case.<sup>[12]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*458</span> B</h2>
<p>The second theory put forward by the State to justify a warrantless seizure and search of the Pontiac car is that under <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>, the police may make a warrantless search of an automobile whenever they have probable cause to do so, and, under our decision last Term in <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span>, whenever the police may make a legal contemporaneous search under <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i> they may also seize the car, take it to the police station, and search it there. But even granting that the police had probable cause to search the car, the application of the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case to these facts would extend it far beyond its original rationale.</p>
<p><i>Carroll</i> did indeed hold that "contraband goods concealed and illegally transported in an automobile or other vehicle may be searched for without a warrant,"<sup>[13]</sup> provided that "the seizing officer shall have reasonable or probable cause for believing that the automobile which he stops and seizes has contraband liquor therein which is being illegally transported."<sup>[14]</sup> Such searches had been explicitly authorized by Congress, and, as we have pointed out elsewhere,<sup>[15]</sup> in the conditions of the time "[a]n automobile . . . was an almost indispensable instrumentality in large-scale violation of the National Prohibition Act, and the car itself therefore was treated somewhat as an offender and became contraband." In two later cases,<sup>[16]</sup> each involving an occupied automobile stopped on the open highway and searched for contraband <span class="star-pagination">*459</span> liquor, the Court followed and reaffirmed <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>.</i><sup>[17]</sup> And last Term in <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers, supra,</a></span></i> we did so again.</p>
<p>The underlying rationale of <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> and of all the cases that have followed it is that there is</p>
<blockquote>"a necessary difference between a search of a store, dwelling house or other structure in respect of which a proper official warrant readily may be obtained, and a search of a ship, motor boat, wagon or automobile, <span class="star-pagination">*460</span> for contraband goods, where <i>it is not practicable to secure a warrant</i> because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153</a></span>. (Emphasis supplied.)</blockquote>
<p>As we said in <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney"><i>Chambers, supra,</i> at 51</a></span>, "exigent circumstances" justify the warrantless search of "an automobile <i>stopped on the highway,</i>" where there is probable cause, because the car is "movable, the occupants are alerted, and the car's contents may never be found again if a warrant must be obtained." "[T]he opportunity to search is fleeting . . . ." (Emphasis supplied.)</p>
<p>In this case, the police had known for some time of the probable role of the Pontiac car in the crime. Coolidge was aware that he was a suspect in the Mason murder, but he had been extremely cooperative throughout the investigation, and there was no indication that he meant to flee. He had already had ample opportunity to destroy any evidence he thought incriminating. There is no suggestion that, on the night in question, the car was being used for any illegal purpose, and it was regularly parked in the driveway of his house. The opportunity for search was thus hardly "fleeting." The objects that the police are assumed to have had probable cause to search for in the car were neither stolen nor contraband nor dangerous.</p>
<p>When the police arrived at the Coolidge house to arrest him, two officers were sent to guard the back door while the main party approached from the front. Coolidge was arrested inside the house, without resistance of any kind on his part, after he had voluntarily admitted the officers at both front and back doors. There was no way in which he could conceivably have gained access to the automobile after the police arrived on his property. When Coolidge had been taken away, the police informed Mrs. Coolidge, the only other adult occupant of the <span class="star-pagination">*461</span> house, that she and her baby had to spend the night elsewhere and that she could not use either of the Coolidge cars. Two police officers then drove her in a police car to the house of a relative in another town, and they stayed with her there until around midnight, long after the police had had the Pontiac towed to the station house. The Coolidge premises were guarded throughout the night by two policemen.<sup>[18]</sup></p>
<p>The word "automobile" is not a talisman in whose presence the Fourth Amendment fades away and disappears. <span class="star-pagination">*462</span> And surely there is nothing in this case to invoke the meaning and purpose of the rule of <i>Carroll</i> v. <i>United States</i>no alerted criminal bent on flight, no fleeting opportunity on an open highway after a hazardous chase, no contraband or stolen goods or weapons, no confederates waiting to move the evidence, not even the inconvenience of a special police detail to guard the immobilized automobile. In short, by no possible stretch of the legal imagination can this be made into a case where "it is not practicable to secure a warrant," <i>Carroll,supra,</i> at 153, and the "automobile exception," despite its label, is simply irrelevant.<sup>[19]</sup></p>
<p><span class="star-pagination">*463</span> Since <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> would not have justified a warrantless search of the Pontiac at the time Coolidge was arrested, the later search at the station house was plainly illegal, at least so far as the automobile exception is concerned. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers, supra,</a></span></i> is of no help to the State, since that case held only that, where the police may stop and search an automobile under <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i> they may also seize it and search it later at the police station.<sup>[20]</sup> Rather, this case is controlled by <i>Dyke</i> v. <i>Taylor Implement Mfg. Co., supra</i><i>.</i> There the police lacked probable cause to seize or search the defendant's automobile at the time of his <span class="star-pagination">*464</span> arrest, and this was enough by itself to condemn the subsequent search at the station house. Here there was probable cause, but no exigent circumstances justified the police in proceeding without a warrant. As in <i><span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">Dyke</a></span>,</i> the later search at the station house was therefore illegal.<sup>[21]</sup></p>
<p></p>
<h2>C</h2>
<p>The State's third theory in support of the warrantless seizure and search of the Pontiac car is that the car itself was an "instrumentality of the crime," and as such might be seized by the police on Coolidge's property because it was in plain view. Supposing the seizure to be thus lawful, the case of <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span>, is said to support a subsequent warrantless search at the station house, with or without probable cause. Of course, the distinction between an "instrumentality of crime" and "mere evidence" was done away with by <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span>, and we may assume that the police had probable cause to seize the automobile.<sup>[22]</sup> But, for the reasons that follow, we hold that the "plain view" exception to the warrant requirement is inapplicable to this case. Since the seizure was therefore <span class="star-pagination">*465</span> illegal, it is unnecessary to consider the applicability of <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">Cooper, supra,</a></span></i> to the subsequent search.<sup>[23]</sup></p>
<p>It is well established that under certain circumstances the police may seize evidence in plain view without a warrant. But it is important to keep in mind that, in the vast majority of cases, <i>any</i> evidence seized by the police will be in plain view, at least at the moment of seizure. The problem with the "plain view" doctrine has been to identify the circumstances in which plain view has legal significance rather than being simply the normal concomitant of any search, legal or illegal.</p>
<p>An example of the applicability of the "plain view" doctrine is the situation in which the police have a warrant to search a given area for specified objects, and in the course of the search come across some other article of incriminating character. Cf. <i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#358" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 358</a></span>; <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#465" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 465</a></span>; <i>Steele</i> v. <i>United States,</i> <span class="citation" data-id="100621"><a href="/opinion/100621/steele-v-united-states-no-1/" aria-description="Citation for case: Steele v. United States No. 1">267 U. S. 498</a></span>; <i>Stanley</i> v. <i>Georgia,</i> <span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/#571" aria-description="Citation for case: Stanley v. Georgia">394 U. S. 557, 571</a></span> (STEWART, J., concurring in result). Where the initial intrusion that brings the police within plain view of such an article is supported, not by a warrant, but by one of the recognized exceptions to the warrant requirement, the seizure is also legitimate. Thus the police may inadvertently come across evidence while in "hot pursuit" of a fleeing suspect. <i>Warden</i> v. <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden, supra</a></span></i><i>;</i> cf. <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span>. And an object that comes into view during a search incident to arrest that is appropriately limited in scope under existing law may be seized without a warrant.<sup>[24]</sup><i>Chimel</i> v. <i>California,</i> 395 <span class="star-pagination">*466</span> U. S., at 762-763. Finally, the "plain view" doctrine has been applied where a police officer is not searching for evidence against the accused, but nonetheless inadvertently comes across an incriminating object. <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U. S. 234</a></span>; <i>Frazier</i> v. <i>Cupp,</i> <span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731</a></span>; <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#43" aria-description="Citation for case: Ker v. California">374 U. S., at 43</a></span>. Cf. <i>Lewis</i> v. <i>United States,</i> <span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/" aria-description="Citation for case: Lewis v. United States">385 U. S. 206</a></span>.</p>
<p>What the "plain view" cases have in common is that the police officer in each of them had a prior justification for an intrusion in the course of which he came inadvertently across a piece of evidence incriminating the accused. The doctrine serves to supplement the prior justificationwhether it be a warrant for another object, hot pursuit, search incident to lawful arrest, or some other legitimate reason for being present unconnected with a search directed against the accusedand permits the warrantless seizure. Of course, the extension of the original justification is legitimate only where it is immediately apparent to the police that they have evidence before them; the "plain view" doctrine may not be used to extend a general exploratory search from one object to another until something incriminating at last emerges. <span class="star-pagination">*467</span> Cf. <i>Stanley</i> v. <span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/#571" aria-description="Citation for case: Stanley v. Georgia"><i>Georgia, supra,</i> at 571-572</a></span> (STEWART, J., concurring in result).</p>
<p>The rationale for the "plain view" exception is evident if we keep in mind the two distinct constitutional protections served by the warrant requirement. First, the magistrate's scrutiny is intended to eliminate altogether searches not based on probable cause. The premise here is that <i>any</i> intrusion in the way of search or seizure is an evil, so that no intrusion at all is justified without a careful prior determination of necessity. See, <i>e. g., </i><i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>; <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span>; <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span>; <i>Chimel</i> v. <i>California,</i> 395 U. S., at 761-762. The second, distinct objective is that those searches deemed necessary should be as limited as possible. Here, the specific evil is the "general warrant" abhorred by the colonists, and the problem is not that of intrusion <i>per se,</i> but of a general, exploratory rummaging in a person's belongings. See, <i>e. g., </i><i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S., at 624-630</a></span>; <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#195" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 195-196</a></span>; <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476</a></span>. The warrant accomplishes this second objective by requiring a "particular description" of the things to be seized.</p>
<p>The "plain view" doctrine is not in conflict with the first objective because plain view does not occur until a search is in progress. In each case, this initial intrusion is justified by a warrant or by an exception such as "hot pursuit" or search incident to a lawful arrest, or by an extraneous valid reason for the officer's presence. And, given the initial intrusion, the seizure of an object in plain view is consistent with the second objective, since it does not convert the search into a general or exploratory one. As against the minor peril to Fourth Amendment protections, there is a major gain in effective law enforcement. Where, once an otherwise lawful search is in progress, the police inadvertently come upon <span class="star-pagination">*468</span> a piece of evidence, it would often be a needless inconvenience, and sometimes dangerousto the evidence or to the police themselvesto require them to ignore it until they have obtained a warrant particularly describing it.</p>
<p>The limits on the doctrine are implicit in the statement of its rationale. The first of these is that plain view <i>alone</i> is never enough to justify the warrantless seizure of evidence. This is simply a corollary of the familiar principle discussed above, that no amount of probable cause can justify a warrantless search or seizure absent "exigent circumstances." Incontrovertible testimony of the senses that an incriminating object is on premises belonging to a criminal suspect may establish the fullest possible measure of probable cause. But even where the object is contraband, this Court has repeatedly stated and enforced the basic rule that the police may not enter and make a warrantless seizure. <i>Taylor</i> v. <i>United States,</i> <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">286 U. S. 1</a></span>; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>; <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>; <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#497" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 497-498</a></span>; <i>Chapman</i> v. <i>United States,</i> <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span>; <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span>.<sup>[25]</sup></p>
<p><span class="star-pagination">*469</span> The second limitation is that the discovery of evidence in plain view must be inadvertent.<sup>[26]</sup> The rationale of the exception to the warrant requirement, as just stated, <span class="star-pagination">*470</span> is that a plain-view seizure will not turn an initially valid (and therefore limited) search into a "general" one, while the inconvenience of procuring a warrant to cover an inadvertent discovery is great. But where the discovery is anticipated, where the police know in advance the location of the evidence and intend to seize it, the situation is altogether different. The requirement of a warrant to seize imposes no inconvenience whatever, or at least none which is constitutionally cognizable in a legal system that regards warrantless searches as "<i>per se</i> <span class="star-pagination">*471</span> unreasonable" in the absence of "exigent circumstances."</p>
<p>If the initial intrusion is bottomed upon a warrant that fails to mention a particular object, though the police know its location and intend to seize it, then there is a violation of the express constitutional requirement of "Warrants . . . particularly describing . . . [the] things to be seized." The initial intrusion may, of course, be legitimated not by a warrant but by one of the exceptions to the warrant requirement, such as hot pursuit or search incident to lawful arrest. But to extend the scope of such an intrusion to the seizure of objectsnot contraband nor stolen nor dangerous in themselveswhich the police know in advance they will find in plain view and intend to seize, would fly in the face of the basic rule that no amount of probable cause can justify a warrantless seizure.<sup>[27]</sup></p>
<p><span class="star-pagination">*472</span> In the light of what has been said, it is apparent that the "plain view" exception cannot justify the police seizure of the Pontiac car in this case. The police had ample opportunity to obtain a valid warrant; they knew the automobile's exact description and location well in advance; they intended to seize it when they came upon Coolidge's property. And this is not a case involving contraband or stolen goods or objects dangerous in themselves.<sup>[28]</sup></p>
<p><span class="star-pagination">*473</span> The seizure was therefore unconstitutional, and so was the subsequent search at the station house. Since evidence obtained in the course of the search was admitted at Coolidge's trial, the judgment must be reversed and the case remanded to the New Hampshire Supreme Court. <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>.</p>
<p></p>
<h2>D</h2>
<p>In his dissenting opinion today, MR. JUSTICE WHITE marshals the arguments that can be made against our interpretation of the "automobile" and "plain view" exceptions to the warrant requirement. Beyond the <span class="star-pagination">*474</span> unstartling proposition that when a line is drawn there is often not a great deal of difference between the situations closest to it on either side, there is a single theme that runs through what he has to say about the two exceptions. Since that theme is a recurring one in controversies over the proper meaning and scope of the Fourth Amendment, it seems appropriate to treat his views in this separate section, rather than piecemeal.</p>
<p>Much the most important part of the conflict that has been so notable in this Court's attempts over a hundred years to develop a coherent body of Fourth Amendment law has been caused by disagreement over the importance of requiring law enforcement officers to secure warrants. Some have argued that a determination by a magistrate of probable cause as a precondition of any search or seizure is so essential that the Fourth Amendment is violated whenever the police might reasonably have obtained a warrant but failed to do so. Others have argued with equal force that a test of reasonableness, applied after the fact of search or seizure when the police attempt to introduce the fruits in evidence, affords ample safeguard for the rights in question, so that "[t]he relevant test is not whether it is reasonable to procure a search warrant, but whether the search was reasonable."<sup>[29]</sup></p>
<p>Both sides to the controversy appear to recognize a distinction between searches and seizures that take place on a man's propertyhis home or officeand those carried out elsewhere. It is accepted, at least as a matter of principle, that a search or seizure carried out on a suspect's premises without a warrant is <i>per se</i> unreasonable, unless the police can show that it falls within one of a carefully defined set of exceptions based on the <span class="star-pagination">*475</span> presence of "exigent circumstances."<sup>[30]</sup> As to other kinds of intrusions, however, there has been disagreement about the basic rules to be applied, as our cases concerning automobile searches, electronic surveillance, street searches and administrative searches make clear.<sup>[31]</sup></p>
<p>With respect to searches and seizures carried out on a suspect's premises, the conflict has been over the question of what qualifies as an "exigent circumstance." It might appear that the difficult inquiry would be when it is that the police can enter upon a person's property to seize his "person . . . papers, and effects," without prior judicial approval. The question of the scope of search and seizure once the police are on the premises would appear to be subsidiary to the basic issue of when intrusion is permissible. But the law has not developed in this fashion.</p>
<p>The most common situation in which Fourth Amendment issues have arisen has been that in which the police enter the suspect's premises, arrest him, and then carry out a warrantless search and seizure of evidence. Where there is a warrant for the suspect's arrest, the evidence seized may later be challenged either on the ground that the warrant was improperly issued because there was not probable cause,<sup>[32]</sup> or on the ground that the police search and seizure went beyond that which they could carry out as an incident to the execution of the arrest warrant.<sup>[33]</sup> Where the police act without an <span class="star-pagination">*476</span> arrest warrant, the suspect may argue that an arrest warrant was necessary, that there was no probable cause to arrest,<sup>[34]</sup> or that even if the arrest was valid, the search and seizure went beyond permissible limits.<sup>[35]</sup> Perhaps because each of these lines of attack offers a plethora of litigable issues, the more fundamental question of when the police may arrest a man in his house without a warrant has been little considered in the federal courts. This Court has chosen on a number of occasions to assume the validity of an arrest and decide the case before it on the issue of the scope of permissible warrantless search. <i>E. g., </i><i>Chimel</i> v. <i>California, supra</i><i>.</i> The more common inquiry has therefore been: "Assuming a valid police entry for purposes of arrest, what searches and seizures may the police carry out without prior authorization by a magistrate?"</p>
<p>Two very broad, and sharply contrasting answers to this question have been assayed by this Court in the past. The answer of <i>Trupiano</i> v. <i>United States, supra</i><i>,</i> was that <i>no</i> searches and seizures could be legitimated by the mere fact of valid entry for purposes of arrest, so long as there was no showing of special difficulties in obtaining a warrant for search and seizure. The contrasting answer in <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span>, and <i>United States</i> v. <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz, supra</a></span></i><i>,</i> was that a valid entry for purposes of arrest served to legitimate warrantless searches and seizures throughout the premises where the arrest occurred, however spacious those premises might be.</p>
<p>The approach taken in <i>Harris</i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> was open to the criticism that it made it so easy for the police to arrange to search a man's premises without a warrant <span class="star-pagination">*477</span> that the Constitution's protection of a man's "effects" became a dead letter. The approach taken in <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span>,</i> on the other hand, was open to the criticism that it was absurd to permit the police to make an entry in the dead of night for purposes of seizing the "person" by main force, and then refuse them permission to seize objects lying around in plain sight. It is arguable that if the very substantial intrusion implied in the entry and arrest are "reasonable" in Fourth Amendment terms, then the less intrusive search incident to arrest must also be reasonable.</p>
<p>This argument against the <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span></i> approach is of little force so long as it is assumed that the police must, in the absence of one of a number of defined exceptions based on "exigent circumstances," obtain an arrest warrant before entering a man's house to seize his person. If the Fourth Amendment requires a warrant to enter and seize the person, then it makes sense as well to require a warrant to seize other items that may be on the premises. The situation is different, however, if the police are under no circumstances required to obtain an arrest warrant before entering to arrest a person they have probable cause to believe has committed a felony. If no warrant is ever required to legitimate the extremely serious intrusion of a midnight entry to seize the person, then it can be argued plausibly that a warrant should never be required to legitimate a very sweeping search incident to such an entry and arrest. If the arrest without a warrant is <i>per se</i> reasonable under the Fourth Amendment, then it is difficult to perceive why a search incident in the style of <i>Harris</i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> is not <i>per se</i> reasonable as well.</p>
<p>It is clear, then, that the notion that the warrantless entry of a man's house in order to arrest him on probable cause is <i>per se</i> legitimate is in fundamental conflict with the basic principle of Fourth Amendment law that <span class="star-pagination">*478</span> searches and seizures inside a man's house without warrant are <i>per se</i> unreasonable in the absence of some one of a number of well defined "exigent circumstances." This conflict came to the fore in <i>Chimel</i> v. <i>California, supra</i><i>.</i></p>
<p>The Court there applied the basic rule that the "search incident to arrest" is an exception to the warrant requirement and that its scope must therefore be strictly defined in terms of the justifying "exigent circumstances." The exigency in question arises from the dangers of harm to the arresting officer and of destruction of evidence within the reach of the arrestee. Neither exigency can conceivably justify the far-ranging searches authorized under <i>Harris</i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span>.</i> The answer of the dissenting opinion of MR. JUSTICE WHITE in <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>,</i> supported by no decision of this Court, was that a warrantless entry for the purpose of arrest on probable cause is legitimate and reasonable no matter what the circumstances. 395 U. S., at 776-780. From this it was said to follow that the full-scale search incident to arrest was also reasonable since it was a lesser intrusion. 395 U. S., at 772-775.</p>
<p>The same conflict arises in this case. Since the police knew of the presence of the automobile and planned all along to seize it, there was no "exigent circumstance" to justify their failure to obtain a warrant. The application of the basic rule of Fourth Amendment law therefore requires that the fruits of the warrantless seizure be suppressed. MR. JUSTICE WHITE's dissenting opinion, however, argues once again that so long as the police could reasonably make a warrantless nighttime entry onto Coolidge's property in order to arrest him, with no showing at all of an emergency, then it is absurd to prevent them from seizing his automobile as evidence of the crime.</p>
<p>MR. JUSTICE WHITE takes a basically similar approach to the question whether the search of the automobile in <span class="star-pagination">*479</span> this case can be justified under <i>Carroll</i> v. <i>United States, supra</i><i>,</i> and <i>Chambers</i> v. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney, supra</a></span></i><i>. Carroll,</i> on its face, appears to be a classic example of the doctrine that warrantless searches are <i>per se</i> unreasonable in the absence of exigent circumstances. Every word in the opinion indicates the Court's adherence to the underlying rule and its care in delineating a limited exception. Read thus, the case quite evidently does not extend to the situation at bar. Yet if we take the viewpoint of a judge called on only to decide in the abstract, after the fact, whether the police have behaved "reasonably" under all the circumstancesin short if we simply ignore the warrant requirement<span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States"><i>Carroll</i></a></span> comes to stand for something more. The stopping of a vehicle on the open highway and a subsequent search amount to a major interference in the lives of the occupants. <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> held such an interference to be reasonable without a warrant, given probable cause. It may be thought to follow <i>a fortiori</i> that the seizure and search herewhere there was no stopping and the vehicle was unoccupiedwere also reasonable, since the intrusion was less substantial, although there were no exigent circumstances whatever. Using reasoning of this sort, it is but a short step to the position that it is <i>never</i> necessary for the police to obtain a warrant before searching and seizing an automobile, provided that they have probable cause. And MR. JUSTICE WHITE appears to adopt exactly this view when he proposes that the Court should "treat searches of automobiles as we do the arrest of a person."</p>
<p>If we were to accept MR. JUSTICE WHITE'S view that warrantless entry for purposes of arrest and warrantless seizure and search of automobiles are <i>per se</i> reasonable, so long as the police have probable cause, it would be difficult to see the basis for distinguishing searches of houses and seizures of effects. If it is reasonable for the police to make a warrantless nighttime entry for the purpose <span class="star-pagination">*480</span> of arresting a person in his bed, then surely it must be reasonable as well to make a warrantless entry to search for and seize vital evidence of a serious crime. If the police may, without a warrant, seize and search an unoccupied vehicle parked on the owner's private property, not being used for any illegal purpose, then it is hard to see why they need a warrant to seize and search a suitcase, a trunk, a shopping bag, or any other portable container in a house, garage, or back yard.</p>
<p>The fundamental objection, then, to the line of argument adopted by MR. JUSTICE WHITE in his dissent in this case and in <i>Chimel</i> v. <i>California, supra</i><i>,</i> is that it proves too much. If we were to agree with MR. JUSTICE WHITE that the police may, whenever they have probable cause, make a warrantless entry for the purpose of making an arrest, and that seizures and searches of automobiles are likewise <i>per se</i> reasonable given probable cause, then by the same logic <i>any</i> search or seizure could be carried out without a warrant, and we would simply have read the Fourth Amendment out of the Constitution. Indeed, if MR. JUSTICE WHITE is correct that it has generally been assumed that the Fourth Amendment is not violated by the warrantless entry of a man's house for purposes of arrest, it might be wise to re-examine the assumption. Such a re-examination "would confront us with a grave constitutional question, namely, whether the forceful nighttime entry into a dwelling to arrest a person reasonably believed within, upon probable cause that he had committed a felony, under circumstances where no reason appears why an arrest warrant could not have been sought, is consistent with the Fourth Amendment." <i>Jones</i> v. <i>United States,</i> 357 U. S., at 499-500.</p>
<p>None of the cases cited by MR. JUSTICE WHITE disposes of this "grave constitutional question." The case of <i>Warden</i> v. <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden, supra</a></span></i><i>,</i> where the Court elaborated <span class="star-pagination">*481</span> a "hot pursuit" justification for the police entry into the defendant's house without a warrant for his arrest, certainly stands by negative implication for the proposition that an arrest warrant is required in the absence of exigent circumstances. See also <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#728" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 728</a></span>; <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#481" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 481-482</a></span>. The Court of Appeals for the District of Columbia Circuit, sitting <i>en banc,</i> has unanimously reached the same conclusion.<sup>[36]</sup> But we find it unnecessary to decide the question in this case. The rule that "searches conducted outside the judicial process, without prior approval by judge or magistrate, are <i>per se</i> unreasonable under the Fourth Amendmentsubject only to a few specifically established and well-delineated exceptions,"<sup>[37]</sup> is not so frail that its continuing vitality depends on the fate of a supposed doctrine of warrantless arrest. The warrant requirement has been a valued part of our constitutional law for decades, and it has determined the result in scores and scores of cases in courts all over this country. It is not an inconvenience to be somehow "weighed" against the claims of police efficiency. It is, or should be, an important working part of our machinery of government, operating as a matter of course to check the "well-intentioned but mistakenly over-zealous executive officers"<sup>[38]</sup> who are a part of any system of law enforcement. If it is to be a true guide to constitutional police action, rather than just a pious phrase, then "[t]he exceptions cannot be enthroned into the rule." <i>United States</i> v. <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#80" aria-description="Citation for case: United States v. Rabinowitz"><i>Rabinowitz, supra,</i> at 80</a></span> (Frankfurter, J., dissenting). The confinement of the exceptions to their appropriate scope was the function of <i>Chimel</i> v. <i>California, supra</i><i>,</i> where we dealt with the <span class="star-pagination">*482</span> assumption that a search "incident" to a lawful arrest may encompass all of the premises where the arrest occurs, however spacious. The "plain view" exception is intimately linked with the search-incident exception, as the cases discussed in Part C above have repeatedly shown. To permit warrantless plain-view seizures without limit would be to undo much of what was decided in <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>,</i> as the similar arguments put forward in dissent in the two cases indicate clearly enough.</p>
<p>Finally, a word about <i>Trupiano</i> v. <i>United States, supra</i><i>.</i> Our discussion of "plain view" in Part C above corresponds with that given in <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span>.</i> Here, as in <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span>,</i> the determining factors are advance police knowledge of the existence and location of the evidence, police intention to seize it, and the ample opportunity for obtaining a warrant. See <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S., at 707</a></span>-708 and n. 27, <i>supra.</i> However, we do not "reinstate" <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span>,</i> since we cannot adopt all its implications. To begin with, in <i>Chimel</i> v. <i>California, supra</i><i>,</i> we held that a search of the person of an arrestee and of the area under his immediate control could be carried out without a warrant. We did not indicate there, and do not suggest here, that the police must obtain a warrant if they anticipate that they will find specific evidence during the course of such a search. See n. 24, <i>supra.</i> And as to the automobile exception, we do not question the decisions of the Court in <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span>, and <i>Chambers</i> v. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney, supra</a></span></i><i>,</i> although both are arguably inconsistent with <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span>.</i></p>
<p>MR. JUSTICE WHITE'S dissent characterizes the coexistence of <i>Chimel, Cooper, Chambers,</i> and this case as "punitive," "extravagant," "inconsistent," "without apparent reason," "unexplained," and "inexplicable." <i>Post,</i> at 517, 519, 521. It is urged upon us that we have here a "ready opportunity, one way or another, <span class="star-pagination">*483</span> to bring clarity and certainty to a body of law that lower courts and law enforcement officials often find confusing." <i>Post,</i> at 521. Presumably one of the ways in which MR. JUSTICE WHITE believes we might achieve clarity and certainty would be the adoption of his proposal that we treat entry for purposes of arrest and seizure of an automobile alike as <i>per se</i> reasonable on probable cause. Such an approach might dispose of this case clearly and certainly enough, but, as we have tried to show above, it would cast into limbo the whole notion of a Fourth Amendment warrant requirement. And it is difficult to take seriously MR. JUSTICE WHITE'S alternative suggestion that clarity and certainty, as well as coherence and credibility, might also be achieved by modifying <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> and overruling <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i> and <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">Cooper</a></span>.</i> Surely, quite apart from his strong disagreement on the merits, he would take vehement exception to any such cavalier treatment of this Court's decisions.</p>
<p>Of course, it would be nonsense to pretend that our decision today reduces Fourth Amendment law to complete order and harmony. The decisions of the Court over the years point in differing directions and differ in emphasis. No trick of logic will make them all perfectly consistent. But it is no less nonsense to suggest, as does MR. JUSTICE WHITE, <i>post,</i> at 521, 520, that we cease today "to strive for clarity and consistency of analysis," or that we have "abandoned any attempt" to find reasoned distinctions in this area. The time is long past when men believed that development of the law must always proceed by the smooth incorporation of new situations into a single coherent analytical framework. We need accept neither the "clarity and certainty" of a Fourth Amendment without a warrant requirement nor the facile consistency obtained by wholesale overruling of recently decided cases. A remark by <span class="star-pagination">*484</span> MR. JUSTICE HARLAN concerning the Fifth Amendment is applicable as well to the Fourth:</p>
<blockquote>"There are those, I suppose, who would put the `liberal construction' approach of cases like <i>Miranda</i> [v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>,] and <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886), side-by-side with the balancing approach of <i>Schmerber</i> [v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span>,] and perceive nothing more subtle than a set of constructional antinomies to be utilized as convenient bootstraps to one result or another. But I perceive in these cases the essential tension that springs from the uncertain mandate which this provision of the Constitution gives to this Court." <i>California</i> v. <i>Byers,</i> <span class="citation" data-id="9424566"><a href="/opinion/108335/california-v-byers/#449" aria-description="Citation for case: California v. Byers">402 U. S. 424, 449-450</a></span> (concurring in judgment).</blockquote>
<p>We are convinced that the result reached in this case is correct, and that the principle it reflectsthat the police must obtain a warrant when they intend to seize an object outside the scope of a valid search incident to arrestcan be easily understood and applied by courts and law enforcement officers alike. It is a principle that should work to protect the citizen without overburdening the police, and a principle that preserves and protects the guarantees of the Fourth Amendment.</p>
<p></p>
<h2>III</h2>
<p>Because of the prospect of a new trial, the efficient administration of justice counsels consideration of the second substantial question under the Fourth and Fourteenth Amendments presented by this case. The petitioner contends that when the police obtained a rifle and articles of his clothing from his home on the night of Sunday, February 2, 1964, while he was being interrogated at the police station, they engaged in a search and seizure violative of the Constitution. In order to <span class="star-pagination">*485</span> understand this contention, it is necessary to review in some detail the circumstances of the February 2 episode.</p>
<p></p>
<h2>A</h2>
<p>The lie-detector test administered to Coolidge in Concord on the afternoon of the 2d was inconclusive as to his activities on the night of Pamela Mason's disappearance, but during the course of the test Coolidge confessed to stealing $375 from his employer. After the group returned from Concord to Manchester, the interrogation about Coolidge's movements on the night of the disappearance continued, and Coolidge apparently made a number of statements which the police immediately checked out as best they could. The decision to send two officers to the Coolidge house to speak with Mrs. Coolidge was apparently motivated in part by a desire to check his story against whatever she might say, and in part by the need for some corroboration of his admission to the theft from his employer. The trial judge found as a fact, and the record supports him, that at the time of the visit the police knew very little about the weapon that had killed Pamela Mason. The bullet that had been retrieved was of small caliber, but the police were unsure whether the weapon was a rifle or a pistol. During the extensive investigation following the discovery of the body, the police had made it a practice to ask all those questioned whether they owned any guns, and to ask the owners for permission to run tests on those that met the very general description of the murder weapon. The trial judge found as a fact that when the police visited Mrs. Coolidge on the night of the 2d, they were unaware of the previous visit during which Coolidge had shown other officers three guns, and that they were not motivated by a desire to find the murder weapon.</p>
<p><span class="star-pagination">*486</span> The two plainclothesmen asked Mrs. Coolidge whether her husband had been at home on the night of the murder victim's disappearance, and she replied that he had not. They then asked her if her husband owned any guns. According to her testimony at the pretrial suppression hearing, she replied, "Yes, I will get them in the bedroom." One of the officers replied, "We will come with you." The three went into the bedroom where Mrs. Coolidge took all four guns out of the closet. Her account continued:</p>
<blockquote>"A. I believe I asked if they wanted the guns. One gentleman said, `No'; then the other gentleman turned around and said, `We might as well take them.' I said, `If you would like them, you may take them.'</blockquote>
<blockquote>"Q. Did you go further and say, `We have nothing to hide.'?</blockquote>
<blockquote>"A. I can't recall if I said that then or before. I don't recall.</blockquote>
<blockquote>"Q. But at some time you indicated to them that as far as you were concerned you had nothing to hide, and they might take what they wanted?</blockquote>
<blockquote>"A. That was it.</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. Did you feel at that time that you had something to hide?</blockquote>
<blockquote>"A. No."</blockquote>
<p>The two policemen also asked Mrs. Coolidge what her husband had been wearing on the night of the disappearance. She then produced four pairs of trousers and indicated that her husband had probably worn either of two of them on that evening. She also brought out a hunting jacket. The police gave her a receipt for the guns and the clothing, and, after a search of the Coolidge cars not here in issue, took the various articles to the police station.</p>
<p></p>
<h2>
<span class="star-pagination">*487</span> B</h2>
<p>The first branch of the petitioner's argument is that when Mrs. Coolidge brought out the guns and clothing, and then handed them over to the police, she was acting as an "instrument" of the officials, complying with a "demand" made by them. Consequently, it is argued, Coolidge was the victim of a search and seizure within the constitutional meaning of those terms. Since we cannot accept this interpretation of the facts, we need not consider the petitioner's further argument that Mrs. Coolidge could not or did not "waive" her husband's constitutional protection against unreasonable searches and seizures.</p>
<p>Had Mrs. Coolidge, wholly on her own initiative, sought out her husband's guns and clothing and then taken them to the police station to be used as evidence against him, there can be no doubt under existing law that the articles would later have been admissible in evidence. Cf. <i>Burdeau</i> v. <i>McDowell,</i> <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465</a></span>. The question presented here is whether the conduct of the police officers at the Coolidge house was such as to make her actions their actions for purposes of the Fourth and Fourteenth Amendments and their attendant exclusionary rules. The test, as the petitioner's argument suggests, is whether Mrs. Coolidge, in light of all the circumstances of the case, must be regarded as having acted as an "instrument" or agent of the state when she produced her husband's belongings. Cf. <i>United States</i> v. <i>Goldberg,</i> <span class="citation" data-id="263859"><a href="/opinion/263859/united-states-v-morris-c-goldberg-also-known-as-moe-goldberg-and-m-c/" aria-description="Citation for case: United States v. Morris C. Goldberg, Also Known as Moe...">330 F. 2d 30</a></span> (CA3), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./377/953/">377 U. S. 953</a></span> (1964); <i>People</i> v. <i>Tarantino,</i> <span class="citation" data-id="9536654"><a href="/opinion/1139971/people-v-tarantino/" aria-description="Citation for case: People v. Tarantino">45 Cal. 2d 590</a></span>, <span class="citation" data-id="9536654"><a href="/opinion/1139971/people-v-tarantino/" aria-description="Citation for case: People v. Tarantino">290 P. 2d 505</a></span> (1955); see <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U. S. 28</a></span>; <i>Gambino</i> v. <i>United States,</i> <span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/" aria-description="Citation for case: Gambino v. United States">275 U. S. 310</a></span>.</p>
<p>In a situation like the one before us there no doubt always exist forces pushing the spouse to cooperate with <span class="star-pagination">*488</span> the police. Among these are the simple but often powerful convention of openness and honesty, the fear that secretive behavior will intensify suspicion, and uncertainty as to what course is most likely to be helpful to the absent spouse. But there is nothing constitutionally suspect in the existence, without more, of these incentives to full disclosure or active cooperation with the police. The exclusionary rules were fashioned "to prevent, not to repair," and their target is official misconduct. They are "to compel respect for the constitutional guaranty in the only effectively available wayby removing the incentive to disregard it." <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 217</a></span>. But it is no part of the policy underlying the Fourth and Fourteenth Amendments to discourage citizens from aiding to the utmost of their ability in the apprehension of criminals. If, then, the exclusionary rule is properly applicable to the evidence taken from the Coolidge house on the night of February 2, it must be upon the basis that some type of unconstitutional police conduct occurred.</p>
<p>Yet it cannot be said that the police should have obtained a warrant for the guns and clothing before they set out to visit Mrs. Coolidge, since they had no intention of rummaging around among Coolidge's effects or of dispossessing him of any of his property. Nor can it be said that they should have obtained Coolidge's permission for a seizure they did not intend to make. There was nothing to compel them to announce to the suspect that they intended to question his wife about his movements on the night of the disappearance or about the theft from his employer. Once Mrs. Coolidge had admitted them, the policemen were surely acting normally and properly when they asked her, as they had asked those questioned earlier in the investigation, including Coolidge himself, about any guns there might be in the house. The question <span class="star-pagination">*489</span> concerning the clothes Coolidge had been wearing on the night of the disappearance was logical and in no way coercive. Indeed, one might doubt the competence of the officers involved had they not asked exactly the questions they did ask. And surely when Mrs. Coolidge of her own accord produced the guns and clothes for inspection, rather than simply describing them, it was not incumbent on the police to stop her or avert their eyes.</p>
<p>The crux of the petitioner's argument must be that when Mrs. Coolidge asked the policemen whether they wanted the guns, they should have replied that they could not take them, or have first telephoned Coolidge at the police station and asked his permission to take them, or have asked her whether she had been authorized by her husband to release them. Instead, after one policeman had declined the offer, the other turned and said, "We might as well take them," to which Mrs. Coolidge replied, "If you would like them, you may take them."</p>
<p>In assessing the claim that this course of conduct amounted to a search and seizure, it is well to keep in mind that Mrs. Coolidge described her own motive as that of clearing her husband, and that she believed that she had nothing to hide. She had seen her husband himself produce his guns for two other policemen earlier in the week, and there is nothing to indicate that she realized that he had offered only three of them for inspection on that occasion. The two officers who questioned her behaved, as her own testimony shows, with perfect courtesy. There is not the slightest implication of an attempt on their part to coerce or dominate her, or, for that matter, to direct her actions by the more subtle techniques of suggestion that are available to officials in circumstances like these. To hold that the conduct of the police here was a search and seizure would be to hold, in effect, that a criminal suspect has constitutional protection against <span class="star-pagination">*490</span> the adverse consequences of a spontaneous, good-faith effort by his wife to clear him of suspicion.<sup>[39]</sup></p>
<p>The judgment is reversed and the case is remanded to the Supreme Court of New Hampshire for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE HARLAN, concurring.</p>
<p>From the several opinions that have been filed in this case it is apparent that the law of search and seizure is due for an overhauling. State and federal law enforcement officers and prosecutorial authorities must find quite intolerable the present state of uncertainty, which extends even to such an everyday question as the circumstances under which police may enter a man's property to arrest him and seize a vehicle believed to have been used during the commission of a crime.</p>
<p>I would begin this process of re-evaluation by overruling <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), and <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963). The former of these cases made the federal "exclusionary rule" applicable to the States. The latter forced the States to follow all the ins and outs of this Court's Fourth Amendment decisions, handed down in federal cases.</p>
<p>In combination <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> and <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span></i> have been primarily responsible for bringing about serious distortions and incongruities in this field of constitutional law. Basically these have had two aspects, as I believe an examination of our more recent opinions and certiorari docket will show. First, the States have been put in a federal mold with respect to this aspect of criminal law enforcement, thus depriving the country of the opportunity to observe <span class="star-pagination">*491</span> the effects of different procedures in similar settings. See, <i>e. g.,</i> Oaks, Studying the Exclusionary Rule in Search and Seizure, <span class="citation no-link">37 U. Chi. L. Rev. 665</span> (1970), suggesting that the assumed "deterrent value" of the exclusionary rule has never been adequately demonstrated or disproved, and pointing out that because of <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> all comparative statistics are 10 years old and no new ones can be obtained. Second, in order to leave some room for the States to cope with their own diverse problems, there has been generated a tendency to relax federal requirements under the Fourth Amendment, which now govern state procedures as well. For an illustration of that tendency in another constitutional field, again resulting from the infelicitous "incorporation" doctrine, see <i>Williams</i> v. <i>Florida,</i> <span class="citation" data-id="9424326"><a href="/opinion/108186/williams-v-florida/" aria-description="Citation for case: Williams v. Florida">399 U. S. 78</a></span> (1970). Until we face up to the basic constitutional mistakes of <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> and <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span>,</i> no solid progress in setting things straight in search and seizure law will, in my opinion, occur.</p>
<p>But for <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> and <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span>,</i> I would have little difficulty in voting to sustain this conviction, for I do not think that anything the State did in this case could be said to offend those values which are "at the core of the Fourth Amendment." <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span> (1949); cf. <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">347 U. S. 128</a></span> (1954); <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952).</p>
<p>Because of <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> and <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span>,</i> however, this case must be judged in terms of federal standards, and on that basis I concur, although not without difficulty, in Parts I, II-D, and III of the Court's opinion and in the judgment of the Court.<sup>[*]</sup> It must be recognized that the case is a close one. The reason I am tipped in favor of MR. JUSTICE <span class="star-pagination">*492</span> STEWART'S position is that a contrary result in this case would, I fear, go far toward relegating the warrant requirement of the Fourth Amendment to a position of little consequence in federal search and seizure law, a course which seems to me opposite to the one we took in <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), two Terms ago.</p>
<p>Recent scholarship has suggested that in emphasizing the warrant requirement over the reasonableness of the search the Court has "stood the fourth amendment on its head" from a historical standpoint. T. Taylor, Two Studies in Constitutional Interpretation 23-24 (1969). This issue is perhaps most clearly presented in the case of a warrantless entry into a man's home to arrest him on probable cause. The validity of such entry was left open in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499-500</a></span> (1958), and although my Brothers WHITE and STEWART both feel that their contrary assumptions on this point are at the root of their disagreement in this case, <i>ante,</i> at 477-479; <i>post,</i> at 510-512, 521, the Court again leaves the issue open. <i>Ante,</i> at 481. In my opinion it does well to do so. This matter should not be decided in a state case not squarely presenting the issue and where it was not fully briefed and argued. I intimate no view on this subject, but until it is ripe for decision, I hope in a federal case, I am unwilling to lend my support to setting back the trend of our recent decisions.</p>
<p>MR. CHIEF JUSTICE BURGER, dissenting in part and concurring in part.</p>
<p>I join the dissenting opinion of MR. JUSTICE WHITE and in Parts II and III of MR. JUSTICE BLACK'S concurring and dissenting opinion. I also agree with most of what is said in Part I of MR. JUSTICE BLACK'S opinion, but I am not prepared to accept the proposition that the Fifth Amendment requires the exclusion of evidence <span class="star-pagination">*493</span> seized in violation of the Fourth Amendment. I join in Part III of MR. JUSTICE STEWART'S opinion.</p>
<p>This case illustrates graphically the monstrous price we pay for the exclusionary rule in which we seem to have imprisoned ourselves. See my dissent in <i>Bivens</i> v. <i>Six Unknown Named Agents of Federal Bureau of Narcotics, ante,</i> p. 411.</p>
<p>On the merits of the case I find not the slightest basis in the record to reverse this conviction. Here again the Court reaches out, strains, and distorts rules that were showing some signs of stabilizing, and directs a new trial which will be held more than seven years after the criminal acts charged.</p>
<p>Mr. Justice Stone, of the Minnesota Supreme Court, called the kind of judicial functioning in which the Court indulges today "bifurcating elements too infinitesimal to be split."</p>
<p>MR. JUSTICE BLACK, concurring and dissenting.</p>
<p>After a jury trial in a New Hampshire state court, petitioner was convicted of murder and sentenced to life imprisonment. Holding that certain evidence introduced by the State was seized during an "unreasonable" search and that the evidence was inadmissible under the judicially created exclusionary rule of the Fourth Amendment, the majority reverses that conviction. Believing that the search and seizure here was reasonable and that the Fourth Amendment properly construed contains no such exclusionary rule, I dissent.</p>
<p>The relevant facts are these. Pamela Mason, a 14-year-old school girl, lived with her mother and younger brother in Manchester, New Hampshire. She occasionally worked after school as a babysitter and sought such work by posting a notice on a bulletin board in a local laundromat. On January 13, 1964, she arrived home from school about 4:15 p. m. Pamela's mother told her <span class="star-pagination">*494</span> that a man had called seeking a babysitter for that evening and said that he would call again later. About 4:30 p. m., after Pamela's mother had left for her job as a waitress at a nearby restaurant, Pamela received a phone call. Her younger brother, who answered the call but did not overhear the conversation, later reported that the caller was a man. After the call, Pamela prepared dinner for her brother and herself, then left the house about 6 p. m. Her family never again saw her alive. Eight days later, on January 21, 1964, Pamela's frozen body was discovered in a snowdrift beside an interstate highway a few miles from her home. Her throat had been slashed and she had been shot in the head. Medical evidence showed that she died some time between 8 and 10 p. m. on January 13, the night she left home.</p>
<p>A manhunt ensued. Two witnesses informed the police that about 9:30 p. m. on the night of the murder they had stopped to offer assistance to a man in a 1951 Pontiac automobile which was parked beside the interstate highway near the point where the little girl's dead body was later found. Petitioner came under suspicion seven days after the body was discovered when one of his neighbors reported to the police that petitioner had been absent from his home between 5 and 11 p. m. on January 13, the night of the murder. Petitioner owned a 1951 Pontiac automobile that matched the description of the car which the two witnesses reported seeing parked where the girl's body had been found. The police first talked with petitioner at his home on the evening of January 28, fifteen days after the girl was killed, and arranged for him to come to the police station the following Sunday, February 2, 1964. He went to the station that Sunday and answered questions concerning his activities on the night of the murder, telling the police that he had been shopping in a neighboring town at the <span class="star-pagination">*495</span> time the murder was committed. During questioning, petitioner confessed to having committed an unrelated larceny from his employer and was held overnight at the police station in connection with that offense. On the next day, he was permitted to go home.</p>
<p>While petitioner was being questioned at the police station on February 2, two policemen went to petitioner's home to talk with his wife. They asked what firearms the petitioner owned and his wife produced two shotguns and two rifles which she voluntarily offered to the police. Upon examination the University of Rhode Island Criminal Investigation Laboratory concluded that one of the firearms, a Mossberg .22-caliber rifle, had fired the bullet found in the murdered girl's brain.</p>
<p>Petitioner admitted that he was a frequent visitor to the laundromat where Pamela posted her babysitting notice and that he had been there on the night of the murder. The following day a knife belonging to petitioner, which could have inflicted the murdered girl's knife wounds, was found near that laundromat. The police also learned that petitioner had unsuccessfully contacted four different persons before the girl's body had been discovered in an attempt to fabricate an alibi for the night of January 13.</p>
<p>On February 19, 1964, all this evidence was presented to the state attorney general who was authorized under New Hampshire law to issue arrest and search warrants. The attorney general considered the evidence and issued a warrant for petitioner's arrest and four search warrants including a warrant for the seizure and search of petitioner's Pontiac automobile.</p>
<p>On the day the warrants issued, the police went to the petitioner's residence and placed him under arrest. They took charge of his 1951 Pontiac which was parked in plain view in the driveway in front of the house, and, two hours later, towed the car to the police station. <span class="star-pagination">*496</span> During the search of the automobile at the station, the police obtained vacuum sweepings of dirt and other fine particles which matched like sweepings taken from the clothes of the murdered girl. Based on the similarity between the sweepings taken from petitioner's automobile and those taken from the girl's clothes, experts who testified at trial concluded that Pamela had been in the petitioner's car. The rifle given to the police by petitioner's wife was also received in evidence.</p>
<p>Petitioner challenges his conviction on the ground that the rifle obtained from his wife and the vacuum sweepings taken from his car were seized in violation of the Fourth Amendment and were improperly admitted at trial. With respect to the rifle voluntarily given to the police by petitioner's wife, the majority holds that it was properly received in evidence. I agree. But the Court reverses petitioner's conviction on the ground that the sweepings taken from his car were seized during an illegal search and for this reason the admission of the sweepings into evidence violated the Fourth Amendment. I dissent.</p>
<p></p>
<h2>I</h2>
<p>The Fourth Amendment prohibits unreasonable searches and seizures. The Amendment says nothing about consequences. It certainly nowhere provides for the exclusion of evidence as the remedy for violation. The Amendment states: "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." No examination of that text can find an exclusionary rule by a mere process of construction. Apparently the first suggestion that the Fourth Amendment somehow embodied a rule of evidence came <span class="star-pagination">*497</span> in Justice Bradley's majority opinion in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886). The holding in that case was that ordinarily a person may not be compelled to produce his private books and papers for use against him as proof of crime. That decision was a sound application of accepted principles of common law and the command of the Fifth Amendment that no person shall be compelled to be a witness against himself. But Justice Bradley apparently preferred to formulate a new exclusionary rule from the Fourth Amendment rather than rely on the already existing exclusionary rule contained in the language of the Fifth Amendment. His opinion indicated that compulsory production of such evidence at trial violated the Fourth Amendment. Mr. Justice Miller, with whom Chief Justice Waite joined, concurred solely on the basis of the Fifth Amendment, and explicitly refused to go along with Justice Bradley's novel reading of the Fourth Amendment. It was not until 1914, some 28 years after <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> and when no member of the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> Court remained, that the Court in <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, stated that the Fourth Amendment itself barred the admission of evidence seized in violation of the Fourth Amendment. The <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> opinion made no express confession of a break with the past. But if it was merely a proper reading of the Fourth Amendment, it seems strange that it took this Court nearly 125 years to discover the true meaning of those words. The truth is that the source of the exclusionary rule simply cannot be found in the Fourth Amendment. That Amendment did not when adopted, and does not now, contain any constitutional rule barring the admission of illegally seized evidence.</p>
<p>In striking contrast to the Fourth Amendment, the Fifth Amendment states in express, unambiguous terms that no person "shall be compelled in any criminal case <span class="star-pagination">*498</span> to be a witness against himself." The Fifth Amendment in and of itself directly and explicitly commands its own exclusionary rulea defendant cannot be compelled to give evidence against himself. Absent congressional action taken pursuant to the Fourth Amendment, if evidence is to be excluded, it must be under the Fifth Amendment, not the Fourth. That was the point so ably made in the concurring opinion of Justice Miller, joined by Chief Justice Waite, in <i>Boyd</i> v. <i>United States, supra</i><i>,</i> and that was the thrust of my concurring opinion in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#661" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 661</a></span> (1961).</p>
<p>The evidence seized by breaking into Mrs. Mapp's house and the search of all her possessions, was excluded from evidence, not by the Fourth Amendment which contains no exclusionary rule, but by the Fifth Amendment which does. The introduction of such evidence compels a man to be a witness against himself, and evidence so compelled must be excluded under the Fifth Amendment, not because the Court says so, but because the Fifth Amendment commands it.</p>
<p>The Fourth Amendment provides a constitutional means by which the Government can act to obtain evidence to be used in criminal prosecutions. The people are obliged to yield to a proper exercise of authority under that Amendment.<sup>[1]</sup> Evidence properly seized under the Fourth Amendment, of course, is admissible at trial. But nothing in the Fourth Amendment provides that evidence seized in violation of that Amendment must be excluded.</p>
<p>The majority holds that evidence it views as improperly seized in violation of its ever changing concept of the Fourth Amendment is inadmissible. The majority <span class="star-pagination">*499</span> treats the exclusionary rule as a judge-made rule of evidence designed and utilized to enforce the majority's own notions of proper police conduct. The Court today announces its new rules of police procedure in the name of the Fourth Amendment, then holds that evidence seized in violation of the new "guidelines" is automatically inadmissible at trial. The majority does not purport to rely on the Fifth Amendment to exclude the evidence in this case. Indeed, it could not. The majority prefers instead to rely on "changing times" and the Court's role as it sees it, as the administrator in charge of regulating the contacts of officials with citizens. The majority states that in the absence of a better means of regulation, it applies a court-created rule of evidence.</p>
<p>I readily concede that there is much recent precedent for the majority's present announcement of yet another new set of police operating procedures. By invoking this rulemaking power found not in the words but somewhere in the "spirit" of the Fourth Amendment, the Court has expanded that Amendment beyond recognition. And each new step is justified as merely a logical extension of the step before.</p>
<p>It is difficult for me to believe the Framers of the Bill of Rights intended that the police be required to prove a defendant's guilt in a "little trial" before the issuance of a search warrant. But see <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964); <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969). No such proceeding was required before or after the adoption of the Fourth Amendment, until this Court decided <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> and <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>.</i> Likewise, eavesdroppers were deemed to be competent witnesses in both English and American courts up until this Court in its Fourth Amendment "rulemaking" capacity undertook to lay down rules for electronic surveillance. <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#70" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 70</a></span> (1967) (BLACK, J., dissenting); <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#364" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 364</a></span> (1967) (BLACK, J., dissenting). <span class="star-pagination">*500</span> The reasonableness of a search incident to an arrest, extending to areas under the control of the defendant and areas where evidence may be found, was an established tenet of English common law, and American constitutional law after adoption of the Fourth Amendment that is, until <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969). The broad, abstract, and ambiguous concept of "privacy" is now unjustifiably urged as a comprehensive substitute for the Fourth Amendment's guarantee against "unreasonable searches and seizures." <i>Griswold</i> v. <i>Connecticut,</i> <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/" aria-description="Citation for case: Griswold v. Connecticut">381 U. S. 479</a></span> (1965).</p>
<p>Our Government is founded upon a written Constitution. The draftsmen expressed themselves in careful and measured terms corresponding with the immense importance of the powers delegated to them. The Framers of the Constitution, and the people who adopted it, must be understood to have used words in their natural meaning, and to have intended what they said. The Constitution itself contains the standards by which the seizure of evidence challenged in the present case and the admissibility of that evidence at trial is to be measured in the absence of congressional legislation. It is my conclusion that both the seizure of the rifle offered by petitioner's wife and the seizure of the automobile at the time of petitioner's arrest were consistent with the Fourth Amendment and that the evidence so obtained under the circumstances shown in the record in this case could not be excluded under the Fifth Amendment.</p>
<p></p>
<h2>II</h2>
<p>The majority holds that the warrant authorizing the seizure and search of petitioner's automobile was constitutionally defective and void. With respect to search warrants, the Fourth Amendment provides that "no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place <span class="star-pagination">*501</span> to be searched, and the persons or things to be seized." The majority concedes that the police did show probable cause for the issuance of the warrant. The majority does not contest that the warrant particularly described the place to be searched, and the thing to be seized.</p>
<p>But compliance with state law and the requirements of the Fourth Amendment apparently is not enough. The majority holds that the state attorney general's connection with the investigation automatically rendered the search warrant invalid. In the first place, there is no language in the Fourth Amendment which provides any basis for the disqualification of the state attorney general to act as a magistrate. He is a state official of high office. The Fourth Amendment does not indicate that his position of authority over state law enforcement renders him ineligible to issue warrants upon a showing of probable cause supported by oath or affirmation. The majority's argument proceeds on the "little trial" theory that the magistrate is to sit as a judge and weigh the evidence and practically determine guilt or innocence before issuing a warrant. There is nothing in the Fourth Amendment to support such a magnified view of the magistrate's authority. The state attorney general was not barred by the Fourth Amendment or any other constitutional provision from issuing the warrant.</p>
<p>In the second place, the New Hampshire Supreme Court held in effect that the state attorney general's participation in the investigation of the case at the time he issued the search warrant was "harmless error" if it was error at all. I agree. It is difficult to imagine a clearer showing of probable cause. There was no possibility of prejudice because there was no room for discretion. Indeed, it could be said that a refusal to issue a warrant on the showing of probable cause made in this case would have been an abuse of discretion. In light <span class="star-pagination">*502</span> of the showing made by the police, there is no reasonable possibility that the state attorney general's own knowledge of the investigation contributed to the issuance of the warrant. I see no error in the state attorney general's action. But even if there was error, it was harmless beyond reasonable doubt. See <i>Harrington</i> v. <i>California,</i> <span class="citation" data-id="9424056"><a href="/opinion/107952/harrington-v-california/" aria-description="Citation for case: Harrington v. California">395 U. S. 250</a></span> (1969); <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967).</p>
<p>Therefore, it is my conclusion that the warrant authorizing the seizure and search of petitioner's automobile was constitutional under the Fourth Amendment, and that the evidence obtained during that search cannot be excluded under the Fifth Amendment. Moreover, I am of the view that, even if the search warrant had not issued, the search in this case nonetheless would have been constitutional under all three of the principles considered and rejected by the majority.</p>
<p></p>
<h2>III</h2>
<p>It is impo

[...TRUNCATED 112441 of 232441 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
