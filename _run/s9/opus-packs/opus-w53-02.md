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

## GROUP: content/cases/United States v. Johns.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Johns"
type: case
citation: "469 U.S. 478 (1985)"
parallel_cite: "105 S. Ct. 881; 83 L. Ed. 2d 890; 53 U.S.L.W. 4126"
neutral_cite: 1985 U.S. LEXIS 45
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-01-21
docket: 83-1625
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-01-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Johns
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111305/united-states-v-johns/"
  cluster_id: 111305
  opinion_id: 9429826
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[Carroll v. United States]]", "[[California v. Acevedo]]", "[[Chambers v. Maroney]]", "[[United States v. Gastiaburo]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "container-search", "delayed-search", "probable-cause"]
holding: "A warrantless search of packages lawfully removed from a vehicle on PC is not rendered unreasonable merely because officers delayed the…"
lake:
  record_id: United States v. Johns
  status: verified
  projected_at: 2026-07-09
---

# United States v. Johns

*469 U.S. 478 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Customs officers investigating a smuggling operation watched two pickup trucks rendezvous with small planes at a remote Arizona airstrip; agents detected the odor of marihuana coming from packages wrapped in plastic and paper in the trucks. They arrested the people at the scene, drove the trucks to DEA headquarters, and moved the packages into a DEA warehouse. Without a warrant, agents opened the packages about three days later and found marihuana. The Ninth Circuit suppressed it, holding the automobile exception did not authorize a search three days after the packages were removed.

## Issue
Whether the automobile exception permits a warrantless search of packages that officers had probable cause to search and lawfully removed from vehicles, when the search occurs three days after the packages were removed.

## Rule
Yes. Where officers had probable cause and the authority to search the vehicles and their containers under the [[Carroll v. United States]] / *[[United States v. Ross|Ross]]* automobile-exception line, a later search of the removed packages is not made unreasonable by delay. The Court framed the question as "whether the subsequent warrantless search was unreasonable merely because it occurred three days after the packages were unloaded from the pickup trucks." — 469 U.S. at 482. ^pin-482

It answered no: "Inasmuch as the Government was entitled to seize the packages and could have searched them immediately without a warrant, we conclude that the warrantless search three days after the packages were placed in the DEA warehouse was reasonable and consistent with our precedent involving searches of impounded vehicles." — *Id.* at 487. ^pin-487

A defendant who would invalidate such a delayed search must show prejudice to a protected interest: here "respondents have not even alleged, much less proved, that the delay in the search of packages adversely affected legitimate interests protected by the Fourth Amendment." — [*Id.*](https://www.courtlistener.com/opinion/111305/united-states-v-johns/#:~:text=respondents%20have%20not%20even%20alleged%2C) ^pin-487a

## Application
On these facts the three-day delay did not defeat the search. The Customs officers conducted a vehicle search "at least to the extent of entering the trucks and removing the packages," and there was probable cause — the plain odor of marihuana — to believe the packages held contraband. Because the Government could have opened the packages immediately without a warrant, it did not lose that authority by waiting: the respondents did not challenge the seizure of the trucks or packages, never sought their return, and never alleged that the delay harmed any Fourth Amendment interest. The delayed warehouse search was therefore reasonable, by analogy to the Court's impounded-vehicle cases.

## Conclusion
The warrantless search of the packages three days after their removal from the trucks was reasonable under the automobile exception; the Ninth Circuit's suppression order was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Johns* extends the [[Carroll v. United States]] / *[[United States v. Ross|Ross]]* automobile-exception rule (later unified for containers in [[California v. Acevedo]]) to delayed container searches, and is relied on by lower courts rejecting any "temporal limit" on the exception (e.g., [[United States v. Gastiaburo]]).

## Appears on
- [[Automobile Exception]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Johns*, 469 U.S. 478 (1985) — https://www.courtlistener.com/opinion/111305/united-states-v-johns/ — pinpoints: 482, 487.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ae6c07234a3334ab", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "469 U.S. 478 (1985)", "court": "U.S. Supreme Court", "neutral_cite": "1985 U.S. LEXIS 45", "official_citation_present": true, "parallel_cite": "105 S. Ct. 881; 83 L. Ed. 2d 890; 53 U.S.L.W. 4126", "title": "United States v. Johns", "year": "1985"}}
{"assertion_id": "7e7b792645c2c673", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrantless search of packages lawfully removed from a vehicle on PC is not rendered unreasonable merely because officers delayed the…", "title": "United States v. Johns"}}
{"assertion_id": "daa15ed73f82737d", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Key — Progeny / Refinement", "title": "United States v. Johns"}}
{"assertion_id": "a04d6d20a87c2ada", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1985-01-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Johns", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Johns", "varies_by_point": "false"}}
{"assertion_id": "fdd47a52d615575a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Johns"}}
```

### lake record — United States v. Johns

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Johns",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Johns",
    "case_name_short": "Johns",
    "case_name_full": "UNITED STATES v. JOHNS Et Al.",
    "input_case_name": "United States v. Johns",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-01-21",
    "year": 1985,
    "docket": "83-1625",
    "cluster_id": 111305,
    "lead_opinion_id": 9429826,
    "sibling_ids": [
      111305,
      9429826,
      9429827
    ],
    "absolute_url": "/opinion/111305/united-states-v-johns/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "469 U.S. 478",
      "volume": "469",
      "reporter": "U.S.",
      "page": "478",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 881",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "881",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 890",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "890",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4126",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4126",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 45",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "45",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "469 U.S. 478",
        "volume": "469",
        "reporter": "U.S.",
        "page": "478",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 881",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "881",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 890",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "890",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 45",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "45",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4126",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4126",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "469 U.S. 478",
    "official_selection": {
      "court_class": "scotus",
      "selected": "469 U.S. 478",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-482",
      "page": null,
      "quote": "--- # United States v. Johns *469 U.S. 478 (1985)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Customs officers investigating a smuggling operation watched two pickup trucks rendezvous with small planes at a remote Arizona airstrip; agents detected the odor of marihuana coming from packages wrapped in plastic and paper in the trucks. They arrested the people at the scene, drove the trucks to DEA headquarters, and moved the packages into a DEA warehouse. Without a warrant, agents opened the packages about three days later and found marihuana. The Ninth Circuit suppressed it, holding the automobile exception did not authorize a search three days after the packages were removed. ## Issue Whether the automobile exception permits a warrantless search of packages that officers had probable cause to search and lawfully removed from vehicles, when the search occurs three days after the packages were removed. ## Rule Yes. Where officers had probable cause and the authority to search the vehicles and their containers under the [[Carroll v. United States]] / *Ross* automobile-exception line, a later search of the removed packages is not made unreasonable by delay. The Court framed the question as",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-487",
      "page": null,
      "quote": "Inasmuch as the Government was entitled to seize the packages and could have searched them immediately without a warrant, we conclude that the warrantless search three days after the packages were placed in the DEA warehouse was reasonable and consistent with our precedent involving searches of impounded vehicles.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-487a",
      "page": null,
      "quote": "respondents have not even alleged, much less proved, that the delay in the search of packages adversely affected legitimate interests protected by the Fourth Amendment.",
      "star_marker": "487",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 28246,
      "fragment": "#:~:text=respondents%20have%20not%20even%20alleged%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-01-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Johns",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Edward Sullivan",
          "cluster_id": 2821420,
          "cite": [
            "797 F.3d 623",
            "2015 U.S. App. LEXIS 13702",
            "2015 WL 4547498"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chad Camou",
          "cluster_id": 2759861,
          "cite": [
            "773 F.3d 932",
            "2014 U.S. App. LEXIS 23347",
            "2014 WL 6980135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hill v. State",
          "cluster_id": 1619349,
          "cite": [
            "303 S.W.3d 863",
            "2009 WL 3821453"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Earnest Lynn Ross",
          "cluster_id": 3131028,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Monterio Desha Hill v. State",
          "cluster_id": 2855208,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andrew Wamsley v. State",
          "cluster_id": 2854445,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Blevins v. State",
          "cluster_id": 1384203,
          "cite": [
            "74 S.W.3d 125",
            "2002 WL 535490"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Padilla",
          "cluster_id": 7042664,
          "cite": [
            "111 F.3d 685",
            "97 Cal. Daily Op. Serv. 2744",
            "97 Daily Journal DAR 4867",
            "1997 U.S. App. LEXIS 7123"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Doe",
          "cluster_id": 196225,
          "cite": [
            "61 F.3d 107",
            "1995 U.S. App. LEXIS 20643",
            "1995 WL 452641"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
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
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Acevedo",
          "cluster_id": 2175164,
          "cite": [
            "216 Cal. App. 3d 586",
            "265 Cal. Rptr. 23",
            "1989 Cal. App. LEXIS 1266"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lyle Gerald Johns",
          "cluster_id": 533056,
          "cite": [
            "891 F.2d 243",
            "1989 U.S. App. LEXIS 18434",
            "1989 WL 146951"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Anthony Prati",
          "cluster_id": 514000,
          "cite": [
            "861 F.2d 82",
            "27 Fed. R. Serv. 66",
            "1988 U.S. App. LEXIS 16205",
            "1988 WL 121235"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
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
        "journal_ref": "United States v. Johns:lane2_top_cited"
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
        "journal_ref": "United States v. Johns:lane2_top_cited"
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
        "journal_ref": "United States v. Johns:lane2_top_cited"
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
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neal v. State",
          "cluster_id": 2347917,
          "cite": [
            "256 S.W.3d 264",
            "2008 Tex. Crim. App. LEXIS 754",
            "2008 WL 2437667"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Safford Unified School District 1 v. Redding",
          "cluster_id": 145852,
          "cite": [
            "174 L. Ed. 2d 354",
            "129 S. Ct. 2633",
            "557 U.S. 364",
            "2009 U.S. LEXIS 4735",
            "21 Fla. L. Weekly Fed. S 1011",
            "77 U.S.L.W. 4591"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Guzman",
          "cluster_id": 1785574,
          "cite": [
            "959 S.W.2d 631",
            "1998 Tex. Crim. App. LEXIS 12",
            "1998 WL 28103"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Pace, Anthony Besase, Christ Savides, Donald Smith, John Cialoni, and Robert Wilson",
          "cluster_id": 538544,
          "cite": [
            "898 F.2d 1218",
            "1990 U.S. App. LEXIS 3831"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Amador Rodriguez Chaidez, A/K/A Rodriguez Amador Chaidez and Amador Rodriguez",
          "cluster_id": 543654,
          "cite": [
            "906 F.2d 377",
            "1990 U.S. App. LEXIS 11006",
            "1990 WL 88172"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stabile",
          "cluster_id": 183984,
          "cite": [
            "633 F.3d 219",
            "2011 U.S. App. LEXIS 1945",
            "2011 WL 294036"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Josey v. State",
          "cluster_id": 1760044,
          "cite": [
            "981 S.W.2d 831",
            "1998 Tex. App. LEXIS 6635",
            "1998 WL 734011"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Taketa and Thomas O'Brien",
          "cluster_id": 554097,
          "cite": [
            "923 F.2d 665",
            "91 Daily Journal DAR 307",
            "91 Cal. Daily Op. Serv. 314",
            "1991 U.S. App. LEXIS 86",
            "1991 WL 594"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Serafin Alfonso, Humberto Rayo, Fabian Mora, Primo Antonio Serrano-Tellez",
          "cluster_id": 450644,
          "cite": [
            "759 F.2d 728",
            "18 Fed. R. Serv. 1398",
            "1985 U.S. App. LEXIS 30539"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. McSween",
          "cluster_id": 7205,
          "cite": [
            "53 F.3d 684",
            "1995 WL 309564"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Steven Ricciardelli",
          "cluster_id": 610895,
          "cite": [
            "998 F.2d 8",
            "1993 U.S. App. LEXIS 14891",
            "1993 WL 210540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony H. Lindsey",
          "cluster_id": 77608,
          "cite": [
            "482 F.3d 1285",
            "2007 WL 894366"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Burgess",
          "cluster_id": 172511,
          "cite": [
            "576 F.3d 1078",
            "80 Fed. R. Serv. 344",
            "2009 U.S. App. LEXIS 17823",
            "2009 WL 2436674"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Cast",
          "cluster_id": 2099235,
          "cite": [
            "556 N.E.2d 69",
            "407 Mass. 891",
            "1990 Mass. LEXIS 315"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Solomon Philip Panitz, United States of America v. Andrew Stewart Baumwald",
          "cluster_id": 544607,
          "cite": [
            "907 F.2d 1267",
            "1990 U.S. App. LEXIS 11808"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Darren Eugene Henderson",
          "cluster_id": 772238,
          "cite": [
            "241 F.3d 638"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Staula",
          "cluster_id": 196665,
          "cite": [
            "80 F.3d 596",
            "1996 U.S. App. LEXIS 5821",
            "1996 WL 134813"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ernesto J. Benevento, Ernest A. Benevento, Earl A. Keller, and Carmine Loiacono",
          "cluster_id": 499444,
          "cite": [
            "836 F.2d 60",
            "1987 U.S. App. LEXIS 16699"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Randolph Williams",
          "cluster_id": 490903,
          "cite": [
            "822 F.2d 1174",
            "262 U.S. App. D.C. 112",
            "1987 U.S. App. LEXIS 8870"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Moses",
          "cluster_id": 2039425,
          "cite": [
            "557 N.E.2d 14",
            "408 Mass. 136",
            "1990 Mass. LEXIS 329"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111305 OR 9429826 OR 9429827) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01ODc3NzkyMDAwMDAmcz0yMTMzNTg1JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111305+OR+9429826+OR+9429827%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 13,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 14,
        "triage_snippet_classified": 186
      },
      "lane2_top_cited": {
        "query": "cites:(111305 OR 9429826 OR 9429827)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04OCZzPTUyNzYwNiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111305+OR+9429826+OR+9429827%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111305 OR 9429826 OR 9429827)",
        "reviewed": 9,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 9,
        "triage_read": 0,
        "triage_snippet_classified": 9
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111305 OR 9429826 OR 9429827)",
    "indexed_citing_opinions": 334,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111305,
        "count": 292,
        "count_source": "search"
      },
      {
        "opinion_id": 9429826,
        "count": 47,
        "count_source": "search"
      },
      {
        "opinion_id": 9429827,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 515,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-johns.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcyNjg0MTgmcz00ODg2NzEyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111305+OR+9429826+OR+9429827%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111305,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 108995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 109332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 110776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 111157,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 371884,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 398924,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 418796,
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
    "date_created": "2026-07-06T00:50:45Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:51:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:51:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:55:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:51:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Johns

```
<opinion type="majority">
<author id="b621-9">Justice O’Connor</author>
<p id="AU5">delivered the opinion of the Court.</p>
<p id="b621-10">In <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982), the Court held that if police officers have probable cause to search a lawfully stopped vehicle, they may conduct a warrantless search of any containers found inside that may conceal the <page-number citation-index="1" label="480">*480</page-number>object of the search. The issue in the present case is whether <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>authorizes a warrantless search of packages several days after they were removed from vehicles that police officers had probable cause to believe contained contraband. Although the Court of Appeals for the Ninth Circuit acknowledged that under <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>the police officers could have searched the packages when they were first discovered in the vehicles, the court concluded that the delay after the initial seizure made the subsequent warrantless search unreasonable within the meaning of the Fourth Amendment. <span class="citation multiple-matches"><a href="/c/F.%202d/707/1093/">707 F. 2d 1093</a></span> (1983). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./467/1250/">467 U. S. 1250</a></span> (1984), and we now reverse.</p>
<p id="b622-5">I</p>
<p id="b622-6">Pursuant to an investigation of a suspected drug smuggling operation, a United States Customs officer went to respondent Duarte’s residence in Tucson, Ariz., where he saw two pickup trucks. The Customs officer observed the trucks drive away, and he contacted other officers who conducted ground and air surveillance of the trucks as they traveled 100 miles to a remote private airstrip near Bowie, Ariz., approximately 50 miles from the Mexican border. Soon after the trucks arrived, a small aircraft landed. Although the Customs officers on the ground were unable to see what transpired, their counterparts in the air informed them that one of the trucks had approached the airplane. After a short time, the aircraft departed. A second small aircraft landed and then departed.</p>
<p id="b622-7">Two Customs officers on the ground came closer and parked their vehicles about 30 yards from the two trucks. One officer approached to investigate and saw an individual at the rear of one of the trucks covering the contents with a blanket. The officer ordered respondents to come out from behind the trucks and to lie on the ground. As he and the other officer walked towards the trucks, they smelled the odor of marihuana. They saw in the back of the trucks <page-number citation-index="1" label="481">*481</page-number>packages wrapped in dark green plastic and sealed with tape. Based on their prior experience, the officers knew that smuggled marihuana is commonly packaged in this manner. Respondents Duarte, Leon, Gomez, Redmond, and Soto were arrested at the scene. The Customs Office surveillance aircraft followed the two small airplanes back to Tucson. Respondents Johns and Hearron, the pilots, were arrested upon landing.</p>
<p id="b623-5">The Customs officers did not search the pickup trucks at the desert airstrip. Instead, after arresting the respondents who were at the scene, the Customs officers took the trucks back to Drug Enforcement Administration (DEA) headquarters in Tucson. The packages were removed from the trucks and placed in a DEA warehouse. Without obtaining a search warrant, DEA agents opened some of the packages and took samples that later proved to be marihuana. Although the record leaves unclear precisely when the agents opened the packages, the parties do not dispute the conclusion of the Court of Appeals, 707 F. 2d, at 1095, that the search occurred three days after the packages were seized from the pickup trucks.</p>
<p id="b623-6">A federal grand jury in the District of Arizona indicted respondents for conspiracy to possess and possession of marihuana with intent to distribute, in violation of <span class="citation no-link">21 U. S. C. §§ 841</span>(a)(1) and 846. Before trial, the District Court granted respondents’ motion to suppress the marihuana, and the Government appealed pursuant to <span class="citation no-link">18 U. S. C. § 3731</span>. The Court of Appeals rejected the Government’s contentions that the plain odor of marihuana emanating from the packages made a warrant unnecessary and that respondents Johns and Hearron lacked standing to challenge the search of the packages. 707 F. 2d, at 1095-1096, 1099-1100. Neither of these issues is before this Court. Finally, the Court of Appeals held that <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>did not authorize the warrantless search of the packages three days after they were removed from the pickup trucks. 707 F. 2d, at 1097-1099. Because we disagree with this conclusion, we reverse.</p>
<p id="b624-4"><page-number citation-index="1" label="482">*482</page-number>II</p>
<p id="b624-5">Respondents argue that we should affirm the suppression of the marihuana on the ground that the Customs officers never had probable cause to conduct a vehicle search, and therefore <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>is inapplicable to this case. Instead, respondents contend that <em>United States </em>v. Chadwick, <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977), establishes that the warrantless search was unlawful. These arguments are not persuasive. The events surrounding the rendezvous of the aircraft and the pickup trucks at the isolated desert airstrip indicated that the vehicles were involved in smuggling activity. The Customs officers on the ground were unable to observe the airplanes after they landed, and consequently did not see the packages loaded into the pickup trucks. After the officers came closer and detected the distinct odor of marihuana, they had probable cause to believe that the vehicles contained contraband. See <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 149, 162</a></span> (1925). Given their experience with drug smuggling cases, the officers no doubt suspected that the scent was emanating from the packages that they observed in the back of the pickup trucks. The officers, however, were unaware of the packages until they approached the trucks, and contraband might well have been hidden elsewhere in the vehicles. We agree with the Court of Appeals, see 707 F. 2d, at 1097, that the Customs officers had probable cause to believe that not only the packages but also the vehicles themselves contained contraband.</p>
<p id="b624-6">Under the circumstances of this case, respondents’ reliance on <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>is misplaced. In <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>, </em>police officers had probable cause to believe that a footlocker contained contraband. As soon as the footlocker was placed in the trunk of an automobile, the officers seized the footlocker and later searched it without obtaining a warrant. The Court in <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>refused to hold that probable cause generally supports the warrantless search of luggage. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#11" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 11-13</a></span>. <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>, </em>however, did not involve the exception <page-number citation-index="1" label="483">*483</page-number>to the warrant requirement recognized in <em>Carroll </em>v. <em>United States, supra, </em>because the police had no probable cause to believe that the automobile, as contrasted to the footlocker, contained contraband. See <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#11" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 11-12</a></span>. This point is underscored by our decision in <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>, </em>which held that notwithstanding <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>police officers may conduct a warrantless search of containers discovered in the course of a lawful vehicle search. See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#810" aria-description="Citation for case: United States v. Ross">456 U. S., at 810-814</a></span>. Given our conclusion that the Customs officers had probable cause to believe that the pickup trucks contained contraband, <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>is simply inapposite. See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#817" aria-description="Citation for case: United States v. Ross">456 U. S., at 817</a></span>.</p>
<p id="b625-5">Respondents further contend that the record fails to show that a vehicle search ever in fact occurred. This argument is meritless. It is true that the trucks were not searched at the scene, and the record leaves unclear whether the Customs officers thoroughly searched the trucks after they were taken to DEA headquarters. The record does show, however, that the packages were unloaded from the trucks. Thus, the Customs officers conducted a vehicle search at least to the extent of entering the trucks and removing the packages. The possibility that the officers did not search the vehicles more extensively does not affect our conclusion that the packages were removed pursuant to a vehicle search. The issue presented by this case is whether the subsequent warrantless search was unreasonable merely because it occurred three days after the packages were unloaded from the pickup trucks.</p>
<p id="b625-6">Ill</p>
<p id="b625-7">Our analysis of the central issue in this case begins with our decision in <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>. </em>There the Court observed that the exception to the warrant requirement recognized by <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>allows a search of the same scope as could be authorized by a magistrate. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#823" aria-description="Citation for case: United States v. Ross">456 U. S., at 823, 825</a></span>. “A warrant to search a vehicle would support a search of every part of the vehicle that might contain the object of the search.” <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#821" aria-description="Citation for case: United States v. Ross"><em>Id., </em>at 821</a></span>. Although probable cause may not generally justify a war-<page-number citation-index="1" label="484">*484</page-number>rantless search of a container, the Court noted that the protection afforded by the Fourth Amendment varies in different settings. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#823" aria-description="Citation for case: United States v. Ross">Id., at 823</a></span>. “[A]n individual’s expectation of privacy in a vehicle and its contents may not survive if probable cause is given to believe that the vehicle is transporting contraband.” <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ibid.</a></span> </em>Cf. <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#367" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 367-368</a></span> (1976) (discussing lesser expectation of privacy in motor vehicles); <em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590-591</a></span> (1974) (plurality opinion). Consequently, “[i]f probable cause justifies the search of a lawfully stopped vehicle, it justifies the search of every part of the vehicle and its contents that may conceal the object of the search.” <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#825" aria-description="Citation for case: United States v. Ross">456 U. S., at 825</a></span>.</p>
<p id="b626-5"><em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>, </em>as the Court of Appeals acknowledged, 707 F. 2d, at 1098, establishes that the Customs officers could have lawfully searched the packages when they were first discovered inside the trucks at the desert airstrip. Moreover, our previous decisions indicate that the officers acted permissibly by waiting until they returned to DEA headquarters before they searched the vehicles and removed their contents. See <em>id., </em>at 1099. There is no requirement that the warrantless search of a vehicle occur contemporaneously with its lawful seizure. <em>Texas </em>v. <em>White, </em><span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/#68" aria-description="Citation for case: Texas v. White">423 U. S. 67, 68</a></span> (1975) <em>(per curiam); Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 52</a></span> (1970). “[T]he justification to conduct such a warrantless search does not vanish once the car has been immobilized.” <em>Michigan </em>v. <em>Thomas, </em><span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#261" aria-description="Citation for case: Michigan v. Thomas">458 U. S. 259, 261</a></span> (1982) <em>(per curiam). </em>A vehicle lawfully in police custody may be searched on the basis of probable cause to believe that it contains contraband, and there is no requirement of exigent circumstances to justify such a warrantless search. <span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#261" aria-description="Citation for case: Michigan v. Thomas"><em>Id., </em>at 261-262</a></span>; see also <em>Florida </em>v. <em>Meyers, </em><span class="citation" data-id="9429577"><a href="/opinion/111157/florida-v-meyers/" aria-description="Citation for case: Florida v. Meyers">466 U. S. 380</a></span> (1984) <em>(per curiam).</em></p>
<p id="b626-6">The Court of Appeals concluded that <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>allows warrant-less searches of containers only if the search occurs “immediately” as part of the vehicle inspection or “soon thereafter.” See 707 F. 2d, at 1099. Neither <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>nor our other vehicle search cases suggest any such limitation. <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>involved the <page-number citation-index="1" label="485">*485</page-number>warrantless search of two different containers. After making a roadside arrest of the driver of an automobile, police officers opened the trunk and discovered a paper bag that contained what appeared to be narcotics. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#801" aria-description="Citation for case: United States v. Ross"><em>Ross, supra, </em>at 801</a></span>. The officers took the car to police headquarters and after a more thorough search discovered a leather pouch containing currency. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#801" aria-description="Citation for case: United States v. Ross">456 U. S., at 801</a></span>. <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>did not distinguish between the search of the paper bag that occurred at the scene of arrest and the later search of the leather pouch. Because the police had probable cause to search the entire vehicle, the Court concluded that the police were entitled to open the containers discovered inside without first obtaining a warrant. See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#817" aria-description="Citation for case: United States v. Ross"><em>id., </em>at 817</a></span>. <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>did not suggest that this conclusion was affected by the fact that the leather pouch was not searched until after the police had impounded the vehicle or by the existence of exigent circumstances that might have made it impractical to secure a warrant for the search of the container. Instead, <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>indicated that the legality of the search was determined by reference to the exception to the warrant requirement recognized by <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>.</em></p>
<p id="b627-5"><em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>, </em>as the Court of Appeals noted, did observe in a footnote that if police may immediately search a vehicle on the street without a warrant, “a search soon thereafter at the police station is permitted if the vehicle is impounded.” <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#807" aria-description="Citation for case: United States v. Ross">456 U. S., at 807, n. 9</a></span>. When read in context, these remarks plainly do not suggest that searches of containers discovered in the course of a vehicle search are subject to temporal restrictions not applicable to the vehicle search itself. Moreover, <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>expressly refused to limit the application of the <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>exception by requiring police officers to secure a warrant before they searched containers found inside a lawfully stopped vehicle. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#821" aria-description="Citation for case: United States v. Ross">456 U. S., at 821, n. 28</a></span>. “The scope of a warrantless search of an automobile ... is not defined by the nature of the container in which the contraband is secreted. Rather, it is defined by the object of the search and the places in which there is probable cause to believe that it may <page-number citation-index="1" label="486">*486</page-number>be found.” <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross"><em>Id., </em>at 824</a></span>. Consequently, the fact that a container is involved does not in itself either expand or contract the well-established exception to the warrant requirement recognized in <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>. </em>See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross">456 U. S., at 824</a></span>.</p>
<p id="b628-5">The approach of the Court of Appeals not only lacks support in our decision in <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>, </em>but it also fails to further the privacy interests protected by the Fourth Amendment. Whether respondents ever had a privacy interest in the packages reeking of marihuana is debatable. We have previously observed that certain containers may not support a reasonable expectation of privacy because their contents can be inferred from their outward appearance, <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 764-765, n. 13</a></span> (1979), and based on this rationale the Fourth Circuit has held that “plain odor” may justify a warrantless search of a container. See <em>United States </em>v. <em>Haley, </em><span class="citation" data-id="9468815"><a href="/opinion/398924/united-states-v-michael-ray-haley-william-harry-riehl/#203" aria-description="Citation for case: United States v. Michael Ray Haley William Harry Riehl">669 F. 2d 201, 203-204</a></span>, and n. 3, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./457/1117/">457 U. S. 1117</a></span> (1982). The Ninth Circuit, however, rejected this approach, 707 F. 2d, at 1096, and the Government has not pursued this issue on appeal. We need not determine whether respondents possessed a legitimate expectation of privacy in the packages. Because the Customs officers had probable cause to believe that the pickup trucks contained contraband, any expectation of privacy in the vehicles or their contents was subject to the authority of the officers to conduct a warrantless search. See <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#823" aria-description="Citation for case: United States v. Ross">456 U. S., at 823</a></span>.</p>
<p id="b628-6">The warrantless search of the packages was not unreasonable merely because the Customs officers returned to Tucson and placed the packages in a DEA warehouse rather than immediately opening them. Cf. <em>United States </em>v. <em>Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#119" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 119-120</a></span> (1984) (no privacy interest in package that was in possession of and had been examined by private party); <em>Michigan </em>v. <span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#261" aria-description="Citation for case: Michigan v. Thomas"><em>Thomas, supra, </em>at 261</a></span>. The practical effect of the opposite conclusion would only be to direct police officers to search immediately all containers that they discover in the course of a vehicle search. Cf. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#807" aria-description="Citation for case: United States v. Ross"><em>Ross, supra, </em><page-number citation-index="1" label="487">*487</page-number>at 807, n. 9</a></span> (noting similar consequence if police could not conduct warrantless search after vehicle is impounded). This result would be of little benefit to the person whose property is searched, and where police officers are entitled to seize the container and continue to have probable cause to believe that it contains contraband, we do not think that delay in the execution of the warrantless search is necessarily unreasonable. Cf. <em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#592" aria-description="Citation for case: Cardwell v. Lewis">417 U. S., at 592-593</a></span> (impoundment and 1-day delay did not make examination of exterior of vehicle unreasonable where it could have been done on the spot); <em>United States </em>v. <em>Edwards, </em><span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/#805" aria-description="Citation for case: United States v. Edwards">415 U. S. 800, 805-806</a></span> (1974) (warrantless search of suspect’s clothing permissible notwithstanding delay after initial arrest).</p>
<p id="b629-5">We do not suggest that police officers may indefinitely retain possession of a vehicle and its contents before they complete a vehicle search. Cf. <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#523" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 523</a></span> (1971) (White, J., dissenting). Nor do we foreclose the possibility that the owner of a vehicle or its contents might attempt to prove that delay in the completion of a vehicle search was unreasonable because it adversely affected a privacy or possessory interest. Cf. <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983). We note that in this case there was probable cause to believe that the trucks contained contraband and there is no plausible argument that the object of the search could not have been concealed in the packages. Respondents do not challenge the legitimacy of the seizure of the trucks or the packages, and they never sought return of the property. Thus, respondents have not even alleged, much less proved, that the delay in the search of packages adversely affected legitimate interests protected by the Fourth Amendment. Inasmuch as the Government was entitled to seize the packages and could have searched them immediately without a warrant, we conclude that the war-rantless search three days after the packages were placed in the DEA warehouse was reasonable and consistent with our <page-number citation-index="1" label="488">*488</page-number>precedent involving searches of impounded vehicles. See <em>Florida </em>v. <em>Meyers, </em><span class="citation" data-id="9429577"><a href="/opinion/111157/florida-v-meyers/" aria-description="Citation for case: Florida v. Meyers">466 U. S. 380</a></span> (1984); <em>Michigan </em>v. <em>Thomas, </em><span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/" aria-description="Citation for case: Michigan v. Thomas">458 U. S. 259</a></span> (1982); <em>Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 61-62</a></span> (1967) (upholding warrantless search that took place seven days after seizure of automobile pending forfeiture proceedings).</p>
<p id="b630-5">Accordingly, the decision of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b630-6">
<em>It is so ordered.</em>
</p>
</opinion>
```

---

## GROUP: content/cases/United States v. Knights.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Knights"
type: case
citation: "534 U.S. 112 (2001)"
parallel_cite: "122 S. Ct. 587; 151 L. Ed. 2d 497"
neutral_cite: 2001 U.S. LEXIS 10950
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2001
date_decided: 2001-12-10
docket: 00-1260
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2001-12-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Knights
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118468/united-states-v-knights/"
  cluster_id: 118468
  opinion_id: 9434170
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Griffin v. Wisconsin]]", "[[Samson v. California]]", "[[United States v. Cortez]]", "[[Terry v. Ohio]]"]
aliases: []
tags: ["case", "fourth-amendment", "probation-search", "reasonable-suspicion", "search-condition", "general-balancing"]
holding: "A warrantless search of a probationer subject to a search condition, supported by reasonable suspicion, is reasonable under the Fourth…"
lake:
  record_id: United States v. Knights
  status: verified
  projected_at: 2026-07-09
---

# United States v. Knights

*534 U.S. 112 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Knights was on probation for a drug offense under a condition that he submit his person, property, residence, vehicle, and effects "to search at anytime, with or without a search warrant, warrant of arrest or reasonable cause by any probation officer or law enforcement officer." After a PG&E transformer was set on fire — the latest of many vandalism incidents for which Knights was a suspect — a detective searched his apartment, with reasonable suspicion, and found incendiary materials, bolt cutters, and a PG&E padlock. The District Court found reasonable suspicion but suppressed the evidence because the search was "investigatory" rather than "probationary"; the Ninth Circuit affirmed.

## Issue
Whether a warrantless search of a probationer's residence, authorized by a probation search condition and supported by reasonable suspicion, is reasonable under the Fourth Amendment — even where the officer's purpose was investigatory rather than probationary.

## Rule
Yes. Balancing the probationer's diminished privacy against the State's interest in supervising probationers, the Court applied ordinary Fourth Amendment reasonableness rather than the special-needs doctrine, and held: "We hold that the balance of these considerations requires no more than reasonable suspicion to conduct a search of this probationer's house." — 534 U.S. at 121. ^pin-121

"When an officer has reasonable suspicion that a probationer subject to a search condition is engaged in criminal activity, there is enough likelihood that criminal conduct is occurring that an intrusion on the probationer's significantly diminished privacy interests is reasonable." — *Id.*

The Court's ultimate holding: "We therefore hold that the warrantless search of Knights, supported by reasonable suspicion and authorized by a condition of probation, was reasonable within the meaning of the Fourth Amendment." — *Id.* at 122. ^pin-122

It expressly reserved the question whether a *suspicionless* search would be reasonable, "because the search in this case was supported by reasonable suspicion." — [*Id.* at 120](https://www.courtlistener.com/opinion/118468/united-states-v-knights/#:~:text=because%20the%20search%20in%20this) n.6. ^pin-120

## Application
On these facts the apartment search was reasonable. Knights's probation order "significantly diminished" his expectation of privacy, while the State's heightened interest in apprehending probationer-recidivists justified a lesser-than-probable-cause standard. The investigatory purpose did not matter, because the Court rested its holding on "ordinary Fourth Amendment analysis," under which "[s]ubjective intentions play no role." Since the District Court found — and Knights conceded — that the search was supported by reasonable suspicion, and the probation condition authorized it, the warrantless search of his apartment satisfied the Fourth Amendment. The Court did not decide whether the same search would have been reasonable with no individualized suspicion at all.

## Conclusion
A probation-condition search of Knights's home, supported by reasonable suspicion, was reasonable under the Fourth Amendment regardless of the officer's investigatory motive; the Ninth Circuit's judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Knights* rests on general Fourth Amendment balancing rather than the special-needs rationale of [[Griffin v. Wisconsin]], and it expressly left open the suspicionless-search question — which [[Samson v. California]] later answered for *parolees* (suspicionless searches reasonable given parolees' even more diminished privacy).

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Knights*, 534 U.S. 112 (2001) — https://www.courtlistener.com/opinion/118468/united-states-v-knights/ — pinpoints: 120 n.6, 121, 122.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9f6c14664d7fc728", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "534 U.S. 112 (2001)", "court": "U.S. Supreme Court", "neutral_cite": "2001 U.S. LEXIS 10950", "official_citation_present": true, "parallel_cite": "122 S. Ct. 587; 151 L. Ed. 2d 497", "title": "United States v. Knights", "year": "2001"}}
{"assertion_id": "578b4d9c74ae506d", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key — Progeny / Refinement", "title": "United States v. Knights"}}
{"assertion_id": "e1e412579cb71758", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrantless search of a probationer subject to a search condition, supported by reasonable suspicion, is reasonable under the Fourth…", "title": "United States v. Knights"}}
{"assertion_id": "8ab82cb1bd330c4b", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Knights"}}
{"assertion_id": "f4dbd0daf6193fb9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2001-12-10", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Knights", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Knights", "varies_by_point": "false"}}
```

### lake record — United States v. Knights

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Knights",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Knights",
    "case_name_short": "Knights",
    "case_name_full": "United States v. Knights",
    "input_case_name": "United States v. Knights",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2001-12-10",
    "year": 2001,
    "docket": "00-1260",
    "cluster_id": 118468,
    "lead_opinion_id": 9434170,
    "sibling_ids": [
      118468,
      9434170,
      9434171
    ],
    "absolute_url": "/opinion/118468/united-states-v-knights/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "534 U.S. 112",
      "volume": "534",
      "reporter": "U.S.",
      "page": "112",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "122 S. Ct. 587",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "587",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "151 L. Ed. 2d 497",
        "volume": "151",
        "reporter": "L. Ed. 2d",
        "page": "497",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2001 U.S. LEXIS 10950",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "10950",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "534 U.S. 112",
        "volume": "534",
        "reporter": "U.S.",
        "page": "112",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "122 S. Ct. 587",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "587",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "151 L. Ed. 2d 497",
        "volume": "151",
        "reporter": "L. Ed. 2d",
        "page": "497",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 U.S. LEXIS 10950",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "10950",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "534 U.S. 112",
    "official_selection": {
      "court_class": "scotus",
      "selected": "534 U.S. 112",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-121",
      "page": null,
      "quote": "; the Ninth Circuit affirmed. ## Issue Whether a warrantless search of a probationer's residence, authorized by a probation search condition and supported by reasonable suspicion, is reasonable under the Fourth Amendment \u2014 even where the officer's purpose was investigatory rather than probationary. ## Rule Yes. Balancing the probationer's diminished privacy against the State's interest in supervising probationers, the Court applied ordinary Fourth Amendment reasonableness rather than the special-needs doctrine, and held:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-122",
      "page": null,
      "quote": "\u2014 *Id.* The Court's ultimate holding:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-120",
      "page": null,
      "quote": "because the search in this case was supported by reasonable suspicion.",
      "star_marker": "122",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 24268,
      "fragment": "#:~:text=because%20the%20search%20in%20this",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2001-12-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Knights",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Hilton",
          "cluster_id": 10018723,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hilton",
          "cluster_id": 5144554,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Norman",
          "cluster_id": 4736927,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Shipps",
          "cluster_id": 4725703,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane1_negative"
      },
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
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Stenhoff",
          "cluster_id": 4609284,
          "cite": [
            "2019 ND 106",
            "925 N.W.2d 429"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4603999,
          "cite": [
            "119 N.E.3d 669",
            "481 Mass. 710"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane1_negative"
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
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Parker",
          "cluster_id": 4329293,
          "cite": [
            "152 A.3d 309",
            "2016 Pa. Super. 280",
            "2016 Pa. Super. LEXIS 751"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane1_negative"
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
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chandler",
          "cluster_id": 7318545,
          "cite": [
            "164 F. Supp. 3d 368",
            "2016 U.S. Dist. LEXIS 17682",
            "2016 WL 614679"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Moore",
          "cluster_id": 3168462,
          "cite": [
            "473 Mass. 481",
            "43 N.E.3d 294"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gall v. United States",
          "cluster_id": 145843,
          "cite": [
            "169 L. Ed. 2d 445",
            "128 S. Ct. 586",
            "552 U.S. 38",
            "2007 U.S. LEXIS 13083"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
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
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nicholas Omar Midgette",
          "cluster_id": 796984,
          "cite": [
            "478 F.3d 616",
            "2007 U.S. App. LEXIS 4153",
            "2007 WL 572127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Samson v. California",
          "cluster_id": 145640,
          "cite": [
            "165 L. Ed. 2d 250",
            "126 S. Ct. 2193",
            "547 U.S. 843",
            "2006 U.S. LEXIS 4885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Luedemann",
          "cluster_id": 2008176,
          "cite": [
            "857 N.E.2d 187",
            "222 Ill. 2d 530",
            "306 Ill. Dec. 94",
            "2006 Ill. LEXIS 1641"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cyril Korte v. HHS",
          "cluster_id": 2709178,
          "cite": [
            "735 F.3d 654",
            "2013 WL 5960692"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Segundo v. State",
          "cluster_id": 1590541,
          "cite": [
            "270 S.W.3d 79",
            "2008 Tex. Crim. App. LEXIS 1505",
            "2008 WL 4724093"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delores Henry v. Melody Hulett",
          "cluster_id": 4774392,
          "cite": [
            "969 F.3d 769"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Villarreal, David",
          "cluster_id": 2948963,
          "cite": [
            "475 S.W.3d 784",
            "2014 Tex. Crim. App. LEXIS 1898",
            "2014 WL 6734178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Parrish Kappes",
          "cluster_id": 2792248,
          "cite": [
            "782 F.3d 828",
            "2015 WL 1546810"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Fernandez",
          "cluster_id": 8438634,
          "cite": [
            "388 F.3d 1199",
            "2004 WL 2399856"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Center for Bio-Ethical Reform, Inc. v. Los Angeles County Sheriff Department",
          "cluster_id": 1235108,
          "cite": [
            "533 F.3d 780",
            "2008 U.S. App. LEXIS 13975",
            "2008 WL 2599683"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tommie T. Childs",
          "cluster_id": 776249,
          "cite": [
            "277 F.3d 947",
            "2002 U.S. App. LEXIS 760",
            "2002 WL 63798"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
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
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chanthasouxat",
          "cluster_id": 76272,
          "cite": [
            "342 F.3d 1271",
            "2003 WL 21994747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicholas v. Goord",
          "cluster_id": 8439101,
          "cite": [
            "430 F.3d 652",
            "2005 WL 3150611"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Merritt Sharp, III v. County of Orange",
          "cluster_id": 4427211,
          "cite": [
            "871 F.3d 901",
            "2017 WL 4126947",
            "2017 U.S. App. LEXIS 18148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ramos",
          "cluster_id": 2507985,
          "cite": [
            "101 P.3d 478",
            "21 Cal. Rptr. 3d 575",
            "34 Cal. 4th 494",
            "2004 Daily Journal DAR 14175",
            "2004 Cal. Daily Op. Serv. 10418",
            "2004 Cal. LEXIS 11332"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Cameron Kincade",
          "cluster_id": 787362,
          "cite": [
            "379 F.3d 813",
            "2004 U.S. App. LEXIS 17191",
            "2004 WL 1837840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Samuels",
          "cluster_id": 2601800,
          "cite": [
            "228 P.3d 229",
            "2009 Colo. App. LEXIS 1789",
            "2009 WL 3297504"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Donald Reyes, Robert Jubic",
          "cluster_id": 776901,
          "cite": [
            "283 F.3d 446",
            "2002 U.S. App. LEXIS 3646"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Motley v. Parks",
          "cluster_id": 3035469,
          "cite": [
            "432 F.3d 1072",
            "2005 WL 3556971"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Frank Fernandez, United States of America v. Roy Gavaldon, AKA Spider, United States of America v. David Gonzales-Contreras, AKA David Contreras-Gonzalez, United States of America v. Dominick Shewmaker Gonzales, AKA Solo, AKA Dominick Gonzales, United States of America v. Jimmy Sanchez, AKA Seal D, AKA Smokey, United States of America v. Suzanne Schoenberg Sanchez",
          "cluster_id": 788340,
          "cite": [
            "388 F.3d 1199",
            "2004 U.S. App. LEXIS 22328"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Tommy Tyler, Jr.",
          "cluster_id": 4472243,
          "cite": [
            "830 N.W.2d 288",
            "2013 WL 1785988",
            "2013 Iowa Sup. LEXIS 44"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118468 OR 9434170 OR 9434171) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDQ5MDE0NDAwMDAwJnM9MzE1OTI2NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118468+OR+9434170+OR+9434171%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(118468 OR 9434170 OR 9434171)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzEmcz0yODEyOTA1JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28118468+OR+9434170+OR+9434171%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118468 OR 9434170 OR 9434171)",
        "reviewed": 50,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 50,
        "triage_read": 0,
        "triage_snippet_classified": 50
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118468 OR 9434170 OR 9434171)",
    "indexed_citing_opinions": 872,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118468,
        "count": 762,
        "count_source": "search"
      },
      {
        "opinion_id": 9434170,
        "count": 126,
        "count_source": "search"
      },
      {
        "opinion_id": 9434171,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1481,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-knights.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxMjkxOTMmcz0xMDI5ODE1NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118468+OR+9434170+OR+9434171%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118468,
        "cited_id": 104314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 108606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 111105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 118277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 118405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 741978,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 1160907,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 1162126,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 5452320,
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
    "date_created": "2026-07-06T01:06:03Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:07:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:07:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:11:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:07:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Knights

```
<opinion type="majority">
<author id="b304-4"><page-number citation-index="1" label="114">*114</page-number>Chief Justice Rehnquist</author>
<p id="A6f">delivered the opinion of the Court.</p>
<p id="b304-5">A California court sentenced respondent Mark James Knights to summary probation for a drug offense. The probation order included the following condition: that Knights would “[s]ubmit his . . . person, property, place of residence, vehicle, personal effects, to search at anytime, with or without a search warrant, warrant of arrest or reasonable cause by any probation officer or law enforcement officer.” Knights signed the probation order, which stated immediately above his signature that “I HAVE. RECEIVED A COPY, READ AND UNDERSTAND THE ABOVE TERMS AND CONDITIONS OF PROBATION AND AGREE TO ABIDE BY SAME.” App. 49. In this case, we decide whether a search pursuant to this probation condition, and supported by reasonable suspicion, satisfied the Fourth Amendment.</p>
<p id="b304-6">Three days after Knights was placed on probation, a Pacific Gas &amp; Electric (PG&amp;E) power transformer and adjacent Pacific Bell telecommunications vault near the Napa County Airport were pried open and set on fire, causing an estimated $1.5 million in damage. Brass padlocks had been removed and a gasoline accelerant had been used to ignite the fire. This incident was the latest in more than 30 recent acts of vandalism against PG&amp;E facilities in Napa County. Suspicion for these acts had long focused on Knights and his friend, Steven Simoneau. The incidents began after PG&amp;E <page-number citation-index="1" label="115">*115</page-number>had filed a theft-of-services complaint against Knights and discontinued his electrical service for failure to pay his bill. Detective Todd Hancock of the Napa County Sheriff’s Department had noticed that the acts of vandalism coincided with Knights’ court appearance dates concerning the theft of PG&amp;E services. And just a week before the arson, a sheriff’s deputy had stopped Knights and Simoneau near a PG&amp;E gas line and observed pipes and gasoline in Simon-eau’s pickup truck.</p>
<p id="b305-5">After the PG&amp;E arson, a sheriff’s deputy drove by Knights’ residence, where he saw Simoneau’s truck parked in front. The deputy felt the hood of the truck. It was warm. Detective Hancock decided to set up surveillance of Knights’ apartment. At about 3:10 the next morning, Simoneau exited the apartment carrying three cylindrical items. Detective Hancock believed the items were pipe bombs. Simoneau walked across the street to the bank of the Napa River, and Hancock heard three splashes. Simon-eau returned without the cylinders and drove away in his truck. Simoneau then stopped in a driveway, parked, and left the area. Detective Hancock entered the driveway and observed a number of suspicious objects in the truck: a Molotov cocktail and explosive materials, a gasoline can, and two brass padlocks that fit the description of those removed from the PG&amp;E transformer vault.</p>
<p id="b305-6">After viewing the objects in Simoneau’s truck, Detective Hancock decided to conduct a search of Knights’ apartment. Detective Hancock was aware of the search condition in Knights’ probation order and thus believed that a warrant was not necessary.<footnotemark>1</footnotemark> The search revealed a detonation cord, ammunition, liquid chemicals, instruction manuals on chemistry and electrical circuitry, bolt cutters, telephone pole-climbing spurs, drug paraphernalia, and a brass padlock stamped “PG&amp;E.”</p>
<p id="b306-4"><page-number citation-index="1" label="116">*116</page-number>Knights was arrested, and a federal grand jury subsequently indicted him for conspiracy to commit arson, for possession of an unregistered destructive device, and for being a felon in possession of ammunition. Knights moved to suppress the evidence obtained during the search of his apartment. The District Court held that Detective Hancock had “reasonable suspicion” to believe that Knights was involved with incendiary materials. App. to Pet. for Cert. 30a. The District Court nonetheless granted the motion to suppress on the ground that the search was for “investigatory” rather than “probationary” purposes. The Court of Appeals for the Ninth Circuit affirmed. <span class="citation multiple-matches"><a href="/c/F.%203d/219/1138/">219 F. 3d 1138</a></span> (2000). The Court of Appeals relied on its earlier decisions holding that the search condition in Knights’ probation order “must be seen as limited to probation searches, and must stop short of investigation searches.” <em>Id., </em>at 1142-1143 (citing <em>United States </em>v. <em>Ooley, </em><span class="citation" data-id="741978"><a href="/opinion/741978/united-states-of-america-plaintiff-appellee-v-norman-lee-ooley-jr/#371" aria-description="Citation for case: UNITED STATES of America, Plaintiff-Appellee, v. Norman...">116 F. 3d 370, 371</a></span> (CA9 1997)).</p>
<p id="b306-5">The Supreme Court of California has rejected this distinction and upheld searches pursuant to the California probation condition “whether the purpose of the search is to monitor the probationer or to serve some other law enforcement purpose.” <em>People </em>v. <em>Woods, </em><span class="citation" data-id="5452320"><a href="/opinion/5607944/people-v-woods/#681" aria-description="Citation for case: People v. Woods">21 Cal. 4th 668, 681</a></span>, <span class="citation" data-id="5452320"><a href="/opinion/5607944/people-v-woods/#1027" aria-description="Citation for case: People v. Woods">981 P. 2d 1019, 1027</a></span> (1999), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./529/1023/">529 U. S. 1023</a></span> (2000). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./532/1018/">532 U. S. 1018</a></span> (2001), to assess the constitutionality of searches made pursuant to this common California probation condition.</p>
<p id="b306-6">Certainly nothing in the condition of probation suggests that it was confined to searches bearing upon probationary status and nothing more. The search condition provides that Knights will submit to a search “by any probation officer or law enforcement officer” and does not mention anything about purpose. App. 49. The question then is whether the Fourth Amendment limits searches pursuant to this probation condition to those with a “probationary” purpose.</p>
<p id="b307-4"><page-number citation-index="1" label="117">*117</page-number>Knights argues that this limitation follows from our decision in <em>Griffin </em>v. <em>Wisconsin, </em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868</a></span> (1987). Brief for Respondent 14. In <em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span>, </em>we upheld a search of a probationer conducted pursuant to a Wisconsin regulation permitting “any probation officer to search a probationer’s home without a warrant as long as his supervisor approves and as long as there are ‘reasonable grounds’ to believe the presence of contraband,” <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#870" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S., at 870-871</a></span>. The Wisconsin regulation that authorized the search was not an express condition of Griffin’s probation; in fact, the regulation was not even promulgated at the time of Griffin’s sentence.<footnotemark>2</footnotemark> The regulation applied to all Wisconsin probationers, with no need for a judge to make an individualized determination that the probationer’s conviction justified the need for warrantless searches. We held that a State’s operation of its probation system presented a “special need” for the “exercise of supervision to assure that [probation] restrictions are in fact observed.” <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#875" aria-description="Citation for case: Griffin v. Wisconsin"><em>Id., </em>at 875</a></span>. That special need for supervision justified the Wisconsin regulation and the search pursuant to the regulation was thus reasonable. <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#875" aria-description="Citation for case: Griffin v. Wisconsin"><em>Id., </em>at 875-880</a></span>.</p>
<p id="b307-5">In Knights’ view, apparently shared by the Court of Appeals, a warrantless search of. a probationer satisfies the Fourth Amendment only if it is just like the search at issue in <em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span> </em>— i. <em>e., </em>a “special needs” search conducted by a probation officer monitoring whether the probationer is complying with probation restrictions. This dubious logic — that an opinion upholding the constitutionality of a particular search implicitly holds unconstitutional any search that is not like it — runs contrary to <em>Griffin’s </em>express statement that its “special needs” holding made it “unnecessary to consider whether” warrantless searches of probationers were other<page-number citation-index="1" label="118">*118</page-number>wise reasonable within the meaning of the Fourth Amendment.<footnotemark>3</footnotemark> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#878" aria-description="Citation for case: Griffin v. Wisconsin"><em>Id., </em>at 878,880</a></span>.</p>
<p id="b308-5">We now consider that question in assessing the constitutionality of the search of Knights’ apartment. The Government, advocating the approach of the Supreme Court of California, see <em><span class="citation" data-id="5452320"><a href="/opinion/5607944/people-v-woods/" aria-description="Citation for case: People v. Woods">Woods, supra,</a></span> </em>contends that the search satisfied the Fourth Amendment under the “consent” rationale of cases such as <em>Zap </em>v. <em>United States, </em><span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/" aria-description="Citation for case: Zap v. United States">328 U. S. 624</a></span> (1946), and <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973). In the Government’s view, Knights’ acceptance of the search condition was voluntary because he had the option of rejecting probation and going to prison instead, which the Government argues is analogous to the voluntary decision defendants often make to waive their right to a trial and accept a plea bargain.<footnotemark>4</footnotemark></p>
<p id="b308-6">We need not decide whether Knights’ acceptance of the search condition constituted consent in the <em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span> </em>sense of a complete waiver of his Fourth Amendment rights, however, because we conclude that the search of Knights was reasonable under our general Fourth Amendment approach of “examining the totality of the circumstances,” <em>Ohio </em>v. <em>Robinette, </em><span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/#39" aria-description="Citation for case: Ohio v. Robinette">519 U. S. 33, 39</a></span> (1996), with the probation search condition being a salient circumstance.</p>
<p id="b308-7">The touchstone of the Fourth Amendment is reasonableness, and the reasonableness of a search is determined “by <page-number citation-index="1" label="119">*119</page-number>assessing, on the one hand, the degree to which it intrudes upon an individual’s privacy and, on the other, the degree to which it is needed for the promotion of legitimate governmental interests.” <em>Wyoming </em>v. <em>Houghton, </em><span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/#300" aria-description="Citation for case: Wyoming v. Houghton">526 U. S. 295, 300</a></span> (1999). Knights’ status as a probationer subject to a search condition informs both sides of that balance. “Probation, like incarceration, is ‘a form of criminal sanction imposed by a court upon an offender after verdict, finding, or plea of guilty.’ ” <em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin, supra,</a></span> </em>at 874 (quoting G. Killinger, H. Kerper, &amp; P. Cromwell, Probation and Parole in the Criminal Justice System 14 (1976)). Probation is “one point. . . on a continuum of possible punishments ranging from solitary confinement in a maximum-security facility to a few hours of mandatory community service.” <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#874" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S., at 874</a></span>. Inherent in the very nature of probation is that probationers “do not enjoy/the absolute liberty to which every citizen is entitled.’” <em>Ibid, </em>(quoting <em>Morrissey </em>v. <em>Brewer, </em><span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#480" aria-description="Citation for case: Morrissey v. Brewer">408 U. S. 471, 480</a></span> (1972)). Just as other punishments for criminal convictions curtail an offender’s freedoms, a court granting probation may impose reasonable conditions that deprive the offender of some freedoms enjoyed by law-abiding citizens.</p>
<p id="b309-5">The judge who sentenced Knights to probation determined that it was necessary to condition the probation on Knights’ acceptance of the search provision. It was reasonable to conclude that the search condition would further the two primary goals of probation — rehabilitation and protecting society from future criminal violations.<footnotemark>5</footnotemark> The probation order clearly expressed the search condition and Knights was unambiguously informed of it. The probation condition <page-number citation-index="1" label="120">*120</page-number>thus significantly diminished Knights’ reasonable expectation of privacy.<footnotemark>6</footnotemark></p>
<p id="b310-5">In assessing the governmental interest side of the balance, it must be remembered that “the very assumption of the institution of probation” is that the probationer “is more likely than the ordinary citizen to violate the law.” <em>Griffin, </em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#880" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S., at 880</a></span>. The recidivism rate of probationers is significantly higher than the general crime rate. See U. S. Dept, of Justice, Office of Justice Programs, Bureau of Justice Statistics, Recidivism of Felons on Probation, 1986-89, pp. 1, 6 (Feb. 1992) (reporting that 43% of 79,000 felons placed on probation in 17 States were rearrested for a felony within three years while still on probation); U. S. Dept, of Justice, Office of Justice Programs, Bureau of Justice Statistics, Probation and Parole Violators in State Prison, 1991, p. 3 (Aug. 1995) (stating that in 1991, 23% of state prisoners were probation violators). And probationers have even more of an incentive to conceal their criminal activities and quickly dispose of incriminating evidence than the ordinary criminal because probationers are aware that they may be subject to supervision and face revocation of probation, and possible incarceration, in proceedings in which the trial rights of a jury and proof beyond a reasonable doubt, among other things, do not apply, see <em>Minnesota </em>v. <em>Murphy, </em><span class="citation" data-id="9429504"><a href="/opinion/111105/minnesota-v-murphy/#435" aria-description="Citation for case: Minnesota v. Murphy">465 U. S. 420, 435, n. 7</a></span> (1984) (“[TJhere is no right to a jury trial before probation may be revoked”); <span class="citation no-link">18 U. S. C. § 3583</span>(e).</p>
<p id="b310-6">The State has a dual concern with a probationer. On the one hand is the hope that he will successfully complete pro<page-number citation-index="1" label="121">*121</page-number>bation and be integrated back into the community. On the other is the concern, quite justified, that he will be more likely to engage in criminal conduct than an ordinary member of the community. The view of the Court of Appeals in this case would require the State to shut its eyes to the latter concern and concentrate only on the former. But we hold that the Fourth Amendment does not put the State to such a choice. Its interest in apprehending violators of the criminal law, thereby protecting potential victims of criminal enterprise, may therefore justifiably focus on probationers in a way that it does'not on the ordinary citizen.</p>
<p id="b311-5">We hold that the balance of these considerations requires no more than reasonable suspicion to conduct a search of this probationer’s house. The degree of individualized suspicion required of a search is a determination of when there is a sufficiently high probability that criminal conduct is occurring to make the intrusion on the individual’s privacy interest reasonable. See <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#418" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 418</a></span> (1981) (individualized suspicion deals “with probabilities”). Although the Fourth Amendment ordinarily requires the degree of probability embodied in the term “probable cause,” a lesser degree satisfies the Constitution when the balance of governmental and private interests makes such a standard reasonable. See, <em>e.g., Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968); <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975). Those interests warrant a lesser than probable-cause standard here. When an officer has reasonable suspicion that a probationer subject to a search condition is engaged in criminal activity, there is enough likelihood that criminal conduct is occurring that an intrusion on the probationer’s significantly diminished privacy interests is reasonable.</p>
<p id="b311-6">The same circumstances that lead us to conclude that reasonable suspicion is constitutionally sufficient also render a warrant requirement unnecessary. See <em>Illinois </em>v. <em>McArthur, </em><span class="citation" data-id="9434039"><a href="/opinion/118405/illinois-v-mcarthur/#330" aria-description="Citation for case: Illinois v. McArthur">531 U. S. 326, 330</a></span> (2001) (noting that general <page-number citation-index="1" label="122">*122</page-number>or individual circumstances, including “diminished expectations of privacy,” may justify an exception to the warrant requirement).</p>
<p id="b312-5">Because our holding rests on ordinary Fourth Amendment analysis that considers all the circumstances of a search, there is no basis for examining official purpose. With the limited exception of some special needs and administrative search cases, see <em>Indianapolis </em>v. <em>Edmond, </em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#45" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S. 32, 45</a></span> (2000), “we have been unwilling to entertain Fourth Amendment challenges based on the actual motivations of individual officers.” <em>Whren </em>v. <em>United States, </em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States">517 U. S. 806, 813</a></span> (1996).</p>
<p id="b312-6">The District Court found, and Knights concedes, that the search in this case was supported by reasonable suspicion. We therefore hold that the warrantless search of Knights, supported by reasonable suspicion and authorized by a condition of probation, was reasonable within the meaning of the Fourth Amendment. The judgment of the Court of Appeals is reversed, and the cause is remanded for further proceedings consistent with this opinion.</p>
<p id="b312-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b305-7"> Hancock had seen a copy of the probation order when he was checking Knights’ file in the Sheriff’s Department office.</p>
</footnote>
<footnote label="2">
<p id="b307-6"> Griffin was placed on probation in September 1980, <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#870" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S., at 870</a></span>, and the regulation was not promulgated until December 1981, <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#871" aria-description="Citation for case: Griffin v. Wisconsin"><em>id., </em>at 871</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b308-8"> The Wisconsin Supreme Court had held in <em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span> </em>that “probation diminishes a probationer’s reasonable expectation of privacy — so that a probation officer may, consistent with the Fourth Amendment, search a probationer’s home without a warrant, and with only ‘reasonable grounds’ (not probable cause) to believe that contraband is present.” <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#872" aria-description="Citation for case: Griffin v. Wisconsin"><em>Id., </em>at 872</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b308-9"> The Government sees our unconstitutional conditions doctrine as a limitation on what a probationer may validly consent to in a probation order. The Government argues that the search condition is not an unconstitutional condition because waiver of Fourth Amendment rights “directly furthers the State’s interest in the effective administration of its probation system.” Brief for United States 22.</p>
</footnote>
<footnote label="5">
<p id="b309-6"> Under California law, a probation condition is invalid if it (1) has no relationship to the crime of which defendant was convicted; (2) relates to conduct which in itself is not criminal; and (3) requires or forbids conduct which is not reasonably related to future criminality. <em>People </em>v. <em>Lent, </em><span class="citation" data-id="9543130"><a href="/opinion/1162126/people-v-lent/#485" aria-description="Citation for case: People v. Lent">15 Cal. 3d 481, 485-486</a></span>, <span class="citation" data-id="9543130"><a href="/opinion/1162126/people-v-lent/#548" aria-description="Citation for case: People v. Lent">541 P. 2d 545, 548</a></span> (1975).</p>
</footnote>
<footnote label="6">
<p id="b310-7"> We do not decide whether the probation condition so diminished, or completely eliminated, Knights’ reasonable expectation of privacy (or constituted consent, see <em>supra, </em>at 118) that a search by a law enforcement officer without any individualized suspicion would have satisfied the reasonableness requirement of the Fourth Amendment. The terms of the probation condition permit such a search, but we need not address the constitutionality of a suspicionless search because the search in this case was supported by reasonable suspicion.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Kolsuz.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Kolsuz
type: case
citation: "890 F.3d 133 (2018)"
parallel_cite: ""
neutral_cite: ""
court: 4th Cir. 2018
court_level: coa
circuit: ca4
year: 2018
date_decided: 2018-05-18
docket: 16-4687
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
  opinion_url: "https://www.courtlistener.com/opinion/4499413/united-states-v-hamza-kolsuz/"
  cluster_id: 4499413
  opinion_id: null
  identity_checked: false
lake:
  record_id: United States v. Kolsuz
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Border Searches]]"
    role: Key
related:
  - "[[Border Searches]]"
  - "[[Riley v. California]]"
  - "[[United States v. Aigbekaen]]"
  - "[[United States v. Montoya de Hernandez]]"
tags:
  - case
  - fourth-amendment
  - border-search
  - forensic-search
  - cell-phone
  - digital-privacy
  - reasonable-suspicion
  - good-faith-exception
  - fourth-circuit
holding: "The Fourth Circuit held that a month-long off-site forensic examination of a smartphone seized at an international airport is a border search, but that under Riley it is a nonroutine border search requiring at least individualized suspicion — while expressly reserving whether reasonable suspicion suffices or a probable-cause warrant is required — and affirmed the denial of suppression under the good-faith exception because the agents reasonably relied on precedent holding that no warrant was required."
---

# United States v. Kolsuz

*890 F.3d 133 (4th Cir. 2018)* (No. 16-4687) · U.S. Court of Appeals for the Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4499413 → opinion 4276666 (890 F.3d 133, decided 2018-05-09, amended 2018-05-18); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Hamza Kolsuz was detained at Washington Dulles International Airport while trying to board a flight to Turkey after customs agents found firearms parts in his luggage. Agents arrested him, seized his smartphone, and subjected it to a **month-long, off-site forensic analysis** that produced a nearly 900-page report cataloguing the phone's data. The district court denied Kolsuz's motion to suppress, applying the Fourth Amendment's border-search exception and holding that the forensic examination was a **nonroutine** border search justified by reasonable suspicion. Kolsuz was convicted of attempting to smuggle firearms out of the country and a related conspiracy count, and appealed the suppression ruling.

## Issue
Whether the off-site forensic analysis of Kolsuz's smartphone was a border search at all once he and the phone were in custody, and, if so, whether under *[[Riley v. California]]* the weighty privacy interest in smartphone data requires more than reasonable suspicion — a warrant based on probable cause — to conduct a forensic border search of a phone.

## Rule
At the border or its functional equivalent, agents may conduct **routine** searches without a warrant or any individualized suspicion, but **nonroutine, highly intrusive** searches require individualized suspicion. Reading that framework together with *[[Riley v. California|Riley]]*'s recognition that digital devices hold a uniquely vast and private trove of data, the court classified a forensic phone search as nonroutine: "We also agree with the district court that under *Riley*, the forensic examination of Kolsuz's phone must be considered a nonroutine border search, requiring some measure of individualized suspicion." — 890 F.3d 133, slip op. at 4. ^pin-op4

## Application
The forensic analysis remained a **border search** despite the temporal and spatial distance between the off-site examination and Kolsuz's airport interception — the justification for the border exception was broad enough to reach it. And under *[[Riley v. California|Riley]]*, that forensic examination was **nonroutine**, requiring individualized suspicion rather than qualifying as a suspicionless routine inspection. The court expressly declined to decide **what** that standard must be — reasonable suspicion, as the district court held, or a probable-cause warrant, as Kolsuz urged — because the question was not outcome-determinative: the agents reasonably relied on precedent holding that no warrant was required, so under the [[The Good-Faith Exception|good-faith exception]] suppression would be inappropriate even if the court disagreed on the standard.

## Conclusion
**Affirmed.** Judge Harris wrote for the court, joined by Judge Motz; Judge Wilkinson concurred in the judgment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Kolsuz* is the Fourth Circuit's foundational digital-border-search holding: forensic device searches at the border are **nonroutine** and demand at least individualized suspicion under *[[Riley v. California|Riley]]*, though the court reserved whether reasonable suspicion or a warrant is required. The circuit soon supplied the missing piece in *[[United States v. Aigbekaen|Aigbekaen]]* (2019), which added a **border-nexus** limit. Frame *Kolsuz* within the unresolved circuit split over forensic device searches (Ninth and Fourth Circuits requiring suspicion; Eleventh requiring none) — never as a settled nationwide device rule.

## Appears on
- [[Border Searches]] — *Key*

## Sources
- [*United States v. Kolsuz*, 890 F.3d 133 (4th Cir. 2018)](https://www.courtlistener.com/opinion/4499413/united-states-v-hamza-kolsuz/) — pinpoint: slip op. at 4 (forensic-device-search-is-nonroutine holding; the CL opinion text is slip-paginated, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "10472a8579623cdf", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "890 F.3d 133 (2018)", "court": "4th Cir. 2018", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Kolsuz", "year": "2018"}}
{"assertion_id": "0c4fca31e14cef11", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Fourth Circuit held that a month-long off-site forensic examination of a smartphone seized at an international airport is a border search, but that under Riley it is a nonroutine border search requiring at least individualized suspicion — while expressly reserving whether reasonable suspicion suffices or a probable-cause warrant is required — and affirmed the denial of suppression under the good-faith exception because the agents reasonably relied on precedent holding that no warrant was required.", "title": "United States v. Kolsuz"}}
{"assertion_id": "215b6e74ed7b3cc5", "dimension": "support", "kind": "home_role", "locator": {"home": "Border Searches"}, "payload": {"home": "Border Searches", "role": "Key", "title": "United States v. Kolsuz"}}
{"assertion_id": "5d496508421cb662", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Kolsuz", "varies_by_point": "false"}}
{"assertion_id": "84969b66294f55bb", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 4th Cir.", "title": "United States v. Kolsuz"}}
```

### lake record — United States v. Kolsuz

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Kolsuz",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Hamza Kolsuz",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Kolsuz",
    "court": "4th Cir. 2018",
    "court_id": "ca4",
    "court_level": "coa",
    "circuit": "ca4",
    "state": null,
    "date_decided": "2018-05-18",
    "year": 2018,
    "docket": "16-4687",
    "cluster_id": 4499413,
    "lead_opinion_id": 4276666,
    "sibling_ids": [],
    "absolute_url": "/opinion/4499413/united-states-v-hamza-kolsuz/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "890 F.3d 133",
      "volume": "890",
      "reporter": "F.3d",
      "page": "133",
      "type": 1,
      "selected_official": true,
      "source": "web-dual-leg"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "890 F.3d 133",
        "volume": "890",
        "reporter": "F.3d",
        "page": "133",
        "type": 1,
        "selected_official": true,
        "source": "web-dual-leg"
      }
    ],
    "display": "890 F.3d 133",
    "official_selection": {
      "court_class": "coa",
      "selected": "890 F.3d 133",
      "reason": "web-dual-leg"
    },
    "web_legs": [
      {
        "source": "Google Scholar",
        "url": "https://scholar.google.com/scholar_case?case=150597407311153261",
        "cite": "890 F.3d 133",
        "checked_date": "2026-07-07"
      },
      {
        "source": "FindLaw",
        "url": "https://caselaw.findlaw.com/us-4th-circuit/1895857.html",
        "cite": "890 F.3d 133",
        "checked_date": "2026-07-07"
      }
    ]
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
    "date_created": "2026-07-06T05:54:09Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:54:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:54:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:54:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:54:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-kolsuz--4499413",
      "to_record_id": "United States v. Kolsuz",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Kolsuz

```
                                     PUBLISHED

                      UNITED STATES COURT OF APPEALS
                          FOR THE FOURTH CIRCUIT


                                      No. 16-4687


UNITED STATES OF AMERICA,

                    Plaintiff-Appellee,

      v.

HAMZA KOLSUZ,

                    Defendant-Appellant.


Appeal from the United States District Court for the Eastern District of Virginia, at
Alexandria. T.S. Ellis, III, District Judge. (1:16-cr-00053-TSE)


Argued: October 26, 2017                                        Decided: May 9, 2018
                               Amended: May 18, 2018


Before WILKINSON, MOTZ, and HARRIS, Circuit Judges.


Affirmed by published opinion. Judge Harris wrote the opinion, in which Judge Motz
joined. Judge Wilkinson wrote a separate opinion concurring in the judgment.


ARGUED: Todd M. Richman, OFFICE OF THE FEDERAL PUBLIC DEFENDER,
Alexandria, Virginia, for Appellant. Jeffrey Michael Smith, National Security Division,
UNITED STATES DEPARTMENT OF JUSTICE, Washington, D.C., for Appellee.
Esha Bhandari, AMERICAN CIVIL LIBERTIES UNION, New York, New York, for
Amici American Civil Liberties Union, ACLU of Virginia, ACLU of Maryland, ACLU
of North Carolina, ACLU of South Carolina, and ACLU of West Virginia. ON BRIEF:
Geremy C. Kamens, Federal Public Defender, OFFICE OF THE FEDERAL PUBLIC
DEFENDER, Alexandria, Virginia, for Appellant. Dana Boente, United States Attorney,
Mary B. McCord, Acting Assistant Attorney General for National Security, Heather
Alpino, UNITED STATES DEPARTMENT OF JUSTICE, Washington, D.C., for
Appellee.      Hope R. Amezquita, AMERICAN CIVIL LIBERTIES UNION
FOUNDATION OF VIRGINIA, Richmond, Virginia, Nathan Freed Wessler, Vera
Eidelman, AMERICAN CIVIL LIBERTIES UNION FOUNDATION, New York, New
York, for Amici American Civil Liberties Union, ACLU of Virginia, ACLU of
Maryland, ACLU of North Carolina, ACLU of South Carolina, and ACLU of West
Virginia. Curt Levey, THE COMMITTEE FOR JUSTICE, Washington, D.C., Erica L.
Marshall, CAUSE OF ACTION INSTITUTE, Washington, D.C., for Amici Cause of
Action Institute, The Committee for Justice, and Floor64, Inc. Sophia Cope, Adam
Schwartz, ELECTRONIC FRONTIER FOUNDATION, San Francisco, California, for
Amici Electronic Frontier Foundation, Asian Americans Advancing Justice-Asian Law
Caucus, Council on American-Islamic Relations (CAIR), CAIR California, CAIR
Florida, CAIR Missouri, CAIR New York, CAIR Ohio, CAIR Dallas/Fort Worth, and
The National Association of Criminal Defense Lawyers. Michael Price, BRENNAN
CENTER FOR JUSTICE AT NYU SCHOOL OF LAW, New York, New York, for
Amicus Brennan Center for Justice.




                                       2
PAMELA HARRIS, Circuit Judge:

      Hamza Kolsuz was detained at Washington Dulles International Airport while

attempting to board a flight to Turkey because federal customs agents found firearms

parts in his luggage. After arresting Kolsuz, the agents took possession of his smartphone

and subjected it to a month-long, off-site forensic analysis, yielding a nearly 900-page

report cataloguing the phone’s data.     The district court denied Kolsuz’s motion to

suppress, applying the Fourth Amendment’s border search exception and holding that the

forensic examination was a nonroutine border search justified by reasonable suspicion.

Kolsuz ultimately was convicted of attempting to smuggle firearms out of the country

and an associated conspiracy charge.

      Kolsuz now challenges the denial of his suppression motion. First, he argues that

the forensic analysis of his phone should not have been treated as a border search at all.

According to Kolsuz, once both he and his phone were in government custody, the

government interest in preventing contraband from crossing the border was no longer

implicated, so the border exception should no longer apply. Second, relying chiefly on

Riley v. California, 134 S. Ct. 2473 (2014) (holding that search incident to arrest

exception does not apply to searches of cell phones), Kolsuz urges that the privacy

interest in smartphone data is so weighty that even under the border exception, a forensic

search of a phone requires more than reasonable suspicion, and instead may be conducted

only with a warrant based on probable cause.

      We agree with the district court that the forensic analysis of Kolsuz’s phone is

properly categorized as a border search.        Despite the temporal and spatial distance

                                            3
between the off-site analysis of the phone and Kolsuz’s attempted departure at the airport,

the justification for the border exception is broad enough to reach the search in this case.

We also agree with the district court that under Riley, the forensic examination of

Kolsuz’s phone must be considered a nonroutine border search, requiring some measure

of individualized suspicion. What precisely that standard should be – whether reasonable

suspicion is enough, as the district court concluded, or whether there must be a warrant

based on probable cause, as Kolsuz suggests – is a question we need not resolve:

Because the agents who conducted the search reasonably relied on precedent holding that

no warrant was required, suppression of the report would be inappropriate even if we

disagreed. Accordingly, we affirm the judgment of the district court.



                                             I.

                                            A.

       We begin with the Fourth Amendment principles that govern this case. As a

general rule, the Fourth Amendment requires that law enforcement searches be

accompanied by a warrant based on probable cause. Arizona v. Gant, 556 U.S. 332, 338

(2009). But there are exceptions, and one such exception typically covers our nation’s

borders. At a border – or at a border’s “functional equivalent,” like the international

airport at which Kolsuz was intercepted – government agents may conduct “routine”

searches and seizures of persons and property without a warrant or any individualized

suspicion. Almeida-Sanchez v. United States, 413 U.S. 266, 272–73 (1973); United

States v. Montoya de Hernandez, 473 U.S. 531, 538 (1985). The Supreme Court has

                                             4
described the border exception as “grounded in the recognized right of the sovereign to

control, subject to substantive limitations imposed by the Constitution, who and what

may enter the country.” United States v. Ramsey, 431 U.S. 606, 620 (1977); see United

States v. Flores-Montano, 541 U.S. 149, 152 (2004) (border exception rests on

government interest in “preventing the entry of unwanted persons and effects”). Routine

searches and seizures at the border therefore are exempted from standard Fourth

Amendment requirements so that the government can “prevent the introduction of

contraband” into the country and bar entry by those who would bring harm across the

border, “whether that be communicable diseases, narcotics, or explosives.” Montoya de

Hernandez, 473 U.S. at 537, 544.

      In this case, the search in question was initiated when Kolsuz attempted to exit the

country, not to enter. But we have long held that the rationales underlying the border

exception extend to exit as well as entry searches. See United States v. Oriakhi, 57 F.3d

1290, 1296–97 (4th Cir. 1995). The “fundamental principles of national sovereignty”

that are the basis for the border search exception, we have explained, apply equally to

government efforts to “protect[] and monitor[] exports from the country” as they do to

efforts to control imports. Id. at 1296, 1297. Thus, with respect to exit searches, the

border search exception is justified by the government’s power to regulate the export of

currency and other goods. Id. at 1297. And that power surely extends to controls on the

exports of dangerous weapons, like the firearms parts at issue here. See, e.g., United

States v. Boumelhem, 339 F.3d 414, 422–23 (6th Cir. 2003) (applying border exception to

exit search of shipping container believed to hold smuggled firearms).

                                            5
       Even at the border, however, the government’s authority is not without limits. The

“ultimate touchstone” of the Fourth Amendment, Riley, 134 S. Ct. at 2482, remains

“reasonableness.” See Montoya de Hernandez, 473 U.S. at 538. While suspicionless

border searches generally are “reasonable simply by virtue of the fact that they occur at

the border,” Ramsey, 431 U.S. at 616, the Supreme Court also has recognized a category

of “nonroutine” border searches that are constitutionally reasonable only if based on

individualized suspicion. See Montoya de Hernandez, 473 U.S. at 541 (holding that

overnight detention for monitored bowel movement followed by rectal examination is

“beyond the scope of a routine customs search” and permissible under the border

exception only with reasonable suspicion). Such nonroutine border searches, the Court

has suggested, include “highly intrusive searches” that implicate especially significant

“dignity and privacy interests,” as well as destructive searches of property and searches

carried out in “particularly offensive” manners. Flores-Montano, 541 U.S. at 152, 154 &

n.2.

                                           B.

       In January 2016, Turkish citizen Hamza Kolsuz entered the United States in

Miami, Florida, on a tourist visa. By that time, Kolsuz already was well known to

government authorities. In December 2012, agents had discovered 163 firearms parts in

his luggage when Kolsuz checked in for a flight to Turkey at John F. Kennedy

International Airport in New York. The parts were listed on the United States Munitions

List (“USML”), subjecting them to export controls and a license requirement under the

Arms Export Control Act, 22 U.S.C. § 2778(b)(2). See 22 C.F.R. §§ 120.2, 121.1 (setting

                                           6
out USML, and defining “defense articles and defense services” subject to control under

the Act). Agents explained the licensing requirements to Kolsuz and his companions,

and ultimately seized the weapons parts. Just one month later, in January 2013, the

process more or less repeated itself: Kolsuz arrived at JFK Airport for a flight to Turkey;

a search of his checked luggage revealed firearms parts; and a licensing determination

disclosed that although the parts were listed on the USML, Kolsuz had not obtained the

requisite export license.

       When Kolsuz reentered the country on January 25, 2016, the authorities were

ready for him. On February 1, 2016, Charles Reich, a Special Agent with United States

Customs and Border Protection (“CBP”) in New York, reached out to CBP officers on

duty at Washington Dulles International Airport (“Dulles”) to let them know that Kolsuz,

who had been stopped before while attempting to smuggle firearms parts out of the

country, would be traveling from Dulles to Turkey the following day. Agent Reich urged

the officers to search Kolsuz’s luggage for firearms parts, and followed up with an email

containing additional information and a list of questions to ask Kolsuz about his

associates and activities.

       On February 2, 2016, Kolsuz began his return trip by checking in at Miami

International Airport for a series of flights that would take him through Dulles and on to

Turkey. When Kolsuz and his luggage reached Dulles, CBP officers Lauren Colgan and




                                            7
Jonathan Budd conducted an outbound customs examination of his two checked bags. 1

Once again, they found multiple firearms parts: 18 handgun barrels, 22 9mm handgun

magazines, four .45 caliber handgun magazines, and one .22 caliber conversion kit.

Colgan and Budd, thanks to their training, immediately recognized that the barrels and

conversion kit were listed on the USML and thus could not be removed from the country

without a license. And when Kolsuz was stopped on the jetway as he attempted to board

his flight to Turkey, he admitted that he was in possession of firearms parts for which he

did not have a federal license.

       After transporting Kolsuz to a secondary inspection area, the officers conducted

what would be the first of two searches of Kolsuz’s iPhone 6 Plus. This search – often

referred to as a “manual” search – involved using the iPhone’s touch screen, which was

not password protected, to scroll through Kolsuz’s recent calls and text messages. The

officers also confirmed through a records search that Kolsuz had no export license or

pending application for a license. After an interview with a number of CBP officers,

Kolsuz was arrested.

       At that point, CBP Special Agent Adam Coppolo initiated the second search of

Kolsuz’s phone, this one commonly known as a “forensic” search.             Coppolo first

transported the phone approximately four miles from Dulles to the Homeland Security


       1
         Kolsuz never has suggested that this standard customs search of his checked
luggage presents any constitutional problem. Nor could he: It is long established that a
search of luggage taken from or bound for an overseas flight is a routine border search
that may be conducted on a suspicionless basis. See Montoya de Hernandez, 473 U.S. at
538; see also, e.g., United States v. Ezeiruaku, 936 F.2d 136, 140–41 (3d Cir. 1991).

                                            8
Investigations office in Sterling, Virginia. There, Computer Forensic Agent Michael Del

Vacchio attached the phone to a Cellebrite Physical Analyzer, which extracts data from

electronic devices, and conducted an advanced logical file system extraction. The phone

remained in airplane mode throughout, so the forensic examination did not reach data

stored remotely – or “in the cloud” – and was instead limited to data stored on the phone

itself. Even so, the data extraction process lasted for a full month, and yielded an 896-

page report that included Kolsuz’s personal contact lists, emails, messenger

conversations, photographs, videos, calendar, web browsing history, and call logs, along

with a history of Kolsuz’s physical location down to precise GPS coordinates.

                                                C.

      Kolsuz was indicted on three counts: (i) attempting to export firearms parts on the

USML without a license, in violation of the Arms Export Control Act, 22 U.S.C. §§

2278(b) and (c); (ii) attempting to smuggle goods from the United States in violation of

18 U.S.C. § 554(a); and (iii) conspiracy to commit those offenses, in violation of 18

U.S.C. § 371.

      Before trial, Kolsuz filed a motion to suppress the report generated by the forensic

examination of his phone, arguing primarily that the border exception did not apply to the

search. According to Kolsuz, a forensic search of a phone that occurs miles away from

an airport and for a month after an attempted departure does not constitute a “border

search.” Moreover, Kolsuz contended, the rationales justifying the border exception were

not implicated in this case, because at the time of the search there was no prospect that

either he or his phone – both securely in government custody – would be crossing the

                                            9
border. Instead, Kolsuz argued, the forensic search should be treated as a search incident

to his arrest, and under Riley v. California, cell phones may be searched incident to arrest

only with a warrant based on probable cause.

       In a comprehensively reasoned opinion, the district court denied Kolsuz’s

suppression motion. United States v. Kolsuz, 185 F. Supp. 3d 843, 860 (E.D. Va. 2016).

The court held first that the forensic search of Kolsuz’s phone was properly evaluated as

a border search. That Kolsuz had been arrested, the district court explained, did not

transform the forensic examination into a search incident to arrest or render the border

exception inapplicable; both the Fourth Circuit and other courts have held that a border

search may be conducted after a traveler is arrested and no longer in a position to cross

the border. Id. at 851 (citing United States v. Ickes, 393 F.3d 501, 507 (4th Cir. 2005)).

Similarly, the court found, it is well established that a search initiated at the border may

fall under the border exception even if it ultimately is conducted off-site and over a long

period of time. Id. at 851–52.

       Now applying the border exception, the district court went on to consider whether

the forensic search of Kolsuz’s smartphone was a routine border search, subject to no

Fourth Amendment requirements, or whether, as Kolsuz urged, it was a nonroutine

search that required some degree of individualized suspicion. The court acknowledged

that in Ickes, the Fourth Circuit treated as routine a border inspection of a computer’s

contents, accessed manually “in the same way a typical user would” and without any

“sophisticated forensic analysis.” Id. at 853 (citing Ickes, 393 F.3d at 502–03). But that

decision, the court determined, “does not address whether more sophisticated forensic

                                            10
searches” also may be classified as routine, id. at 854, particularly in light of the Supreme

Court’s subsequent decision in Riley and its emphasis on the significant privacy interests

in the digital contents of phones.

       The court concluded that while the manual search of Kolsuz’s iPhone at the airport

was a routine border search, 2 the off-site forensic analysis of the phone’s data qualified as

a nonroutine search. After Riley, the court found, a forensic search of a phone no longer

can be analogized to an ordinary search of luggage or some other container at the border,

given the breadth and sensitivity of the private information that may be uncovered. It is

“difficult to conceive of a property search more invasive or intrusive than a sophisticated,

digital search of a cell phone,” the court concluded, which might be compared to a “body

cavity search” of a phone. Id. at 856 (quoting United States v. Saboonchi, 990 F. Supp.

2d 536, 569 (D. Md. 2014)).

       As a nonroutine border search, the court went on to hold, the forensic analysis of

Kolsuz’s phone required particularized suspicion, in the form of the familiar reasonable

suspicion standard. The court rejected the more demanding requirement of a warrant

based on probable cause, noting that no reported case has held a border search to that

standard. Instead, courts consistently have deemed reasonable suspicion sufficient to


       2
         Although the district court addressed this initial search in the course of its
reasoning, Kolsuz’s suppression motion is limited to the subsequent forensic
examination. On appeal, Kolsuz expressly disclaims any challenge to the manual search
of his phone at Dulles, which in any event did not reveal information used against him at
trial.




                                             11
justify even the most intrusive of nonroutine border searches, including body cavity and

alimentary canal searches.     Because the government in this case had “more than

reasonable suspicion” that a forensic examination of Kolsuz’s phone would reveal

evidence of both past and ongoing attempts to export firearms parts illegally, the court

concluded, the forensic search was reasonable under the Fourth Amendment. Id. at 859,

860.

       The parties consented to a bench trial, and the district court found Kolsuz guilty of

all three counts against him. In finding that Kolsuz acted with the requisite willfulness,

the court relied in part on messages Kolsuz exchanged with a co-conspirator, obtained

from the forensic search of Kolsuz’s phone. 3 The court ultimately entered judgment only

on the Arms Export Control Act and conspiracy counts against Kolsuz, dismissing the

smuggling charge on the government’s motion. Kolsuz was sentenced to 30 months in

prison and three years of supervised release, and this timely appeal followed.



                                                 II.

       Kolsuz’s appeal is a narrow one, and we begin by clarifying what is and is not in

front of us today. First, Kolsuz does not challenge the manual search of his smartphone,

undertaken on-site at the airport as he tried to depart for Turkey. We thus have no


       3
         The court also adopted an independent willful blindness theory, under which it
was “unnecessary to rely” on the messages recovered from Kolsuz’s phone. J.A. 243
n.34. As the government recognizes, however, that theory does not apply to the
conspiracy charge of which Kolsuz was convicted, and thus does not provide an
alternative basis for affirming the district court judgment in full.

                                            12
occasion to consider application of the border exception to manual searches of electronic

devices, conducted at the border and roughly contemporaneously with an attempted

crossing.   Cf. United States v. Molina-Isidoro, 884 F.3d 287, 289 (5th Cir. 2018)

(sustaining manual search of phone at border under good-faith exception to Fourth

Amendment exclusionary rule).

      Nor does Kolsuz challenge the seizure of his phone, either initially at the airport or

later at the Homeland Security Investigations office where it was forensically examined.

The Fourth Amendment protects property as well as privacy, see Flores-Montano, 541

U.S. at 154, and a seizure reasonable at its inception must remain reasonable in scope and

duration to satisfy the Fourth Amendment, see Montoya de Hernandez, 473 U.S. at 541–

42. But perhaps because he was in custody while the government undertook its month-

long forensic analysis, Kolsuz has not asserted any impairment of a possessory interest in

his phone. Accordingly, we do not address whether and under what circumstances an

extended confiscation of a traveler’s phone – quite apart from any search undertaken –

might constitute an unreasonable seizure of property for Fourth Amendment purposes.

Cf. Saboonchi, 990 F. Supp. 2d at 569 (noting that forensic searches of digital devices

may deprive individuals of their possessions for periods of days or weeks).

      That leaves the question that is raised by this appeal: whether the forensic search

of Kolsuz’s phone, and the associated invasion of Kolsuz’s privacy, was justified under

the border search exception. In considering the district court’s denial of Kolsuz’s motion

to suppress, we review that court’s legal conclusions de novo and its factual findings for

clear error, considering the evidence in the light most favorable to the government. See

                                            13
United States v. Palmer, 820 F.3d 640, 648 (4th Cir. 2016). For the reasons given below,

we affirm.

                                            A.

       Kolsuz’s primary argument is that the forensic analysis of his phone was not

subject to the border search exception at all. Once he was arrested and his phone seized

and transported miles from the airport, Kolsuz contends, the government interest that

underlies the border search exception – preventing contraband from crossing a border –

was no longer at issue, and the border exception was therefore inapplicable. Rather,

standard Fourth Amendment rules governed the forensic search, and required a warrant

based on probable cause because the search was incident to Kolsuz’s arrest. See Riley,

134 S. Ct. at 2485, 2493–94 (holding that the search incident exception does not apply to

cell phones, which generally may be searched incident to arrest only with probable cause

and a warrant). We cannot agree.

       First, as the district court explained, the border exception is not rendered

inapplicable because a search initiated at a border ultimately is conducted at some

physical or temporal remove. See Kolsuz, 185 F. Supp. 3d at 851–52 (“as several courts

have held, an off-site forensic search of an electronic device over a long period of time is

nonetheless a border search”); see also, e.g., United States v. Cotterman, 709 F.3d 952,

961–62 (9th Cir. 2013) (en banc) (applying border exception to forensic examination of

laptop computer conducted miles from and days after attempted border crossing);

Saboonchi, 990 F. Supp. 2d at 548–49, 561 (applying border exception to forensic search

of cell phones conducted several hundred miles from border crossing). Indeed, after

                                            14
pressing this point before the district court, Kolsuz concedes it on appeal, agreeing that

the location and timing of the search in this case are consistent with the border search

exception.

       Nor, as the district court determined, does the fact of Kolsuz’s arrest transform the

examination of his phone into a search incident to arrest, triggering Riley and calling for a

search warrant based on probable cause. In Ickes, our court applied the border search

exception to approve a manual search of computer data that occurred only after the

defendant had been arrested, obviating any threat of an imminent border crossing. See

393 F.3d at 503; see also, e.g., United States v. Ramos, 190 F. Supp. 3d 992, 998–1000

(S.D. Cal. 2016) (rejecting argument that arrest renders border exception inapplicable by

making it impossible for defendant or contraband to cross border). Kolsuz attempts to

distinguish Ickes on the ground that it involved an entry search rather than the exit search

at issue here, but for these purposes, it makes no difference: As we have explained,

where the relevant governmental interests are present, the border search exception

extends equally to entry and exit searches, see Oriakhi, 57 F.3d at 1296–97, and any rule

carving out post-arrest searches from that doctrine would apply equally in both contexts,

as well.

       In its strongest form, Kolsuz’s argument combines all of these factors – his arrest

as he sought to depart the country, the phone in government custody miles from the

border, the month-long gap between the action at the airport and the end of the search –

and argues that taken together, they show that the search in this case is entirely

“untethered” from any justification behind the border exception. The rationale allowing

                                             15
outgoing border searches, as Kolsuz describes it, is limited to intercepting contraband as

it crosses the national border. Here, with the phone as well as the firearms parts seized

by the government and Kolsuz under arrest, there was no contraband poised to exit the

country and thus no nexus to that rationale. When that is the case, Kolsuz argues, the

border search exception does not apply, because the concerns underlying a warrant

exception “define the boundaries of the exception.” See Gant, 566 U.S. at 339.

       Kolsuz’s foundational premise is correct: As a general rule, the scope of a warrant

exception should be defined by its justifications. See Riley, 134 S. Ct. at 2484–88 (asking

whether “application of the search incident to arrest doctrine to this particular category of

effects would untether the rule from the justifications underlying the [search incident to

arrest] exception”). As a result, where the government interests underlying a Fourth

Amendment exception are not implicated by a certain type of search, and where the

individual’s privacy interests outweigh any ancillary governmental interests, the

government must obtain a warrant based on probable cause. See id. At some point, in

other words, even a search initiated at the border could become so attenuated from the

rationale for the border search exception that it no longer would fall under that exception.

See Molina-Isidoro, 884 F.3d at 295–97 (Costa, J., concurring) (questioning whether

search for evidence as opposed to contraband is consistent with justifications for border

search exception).

       But this is not that case. On the facts here, the link between the search of Kolsuz’s

phone and the interest that justifies border searches was sufficient to trigger the border

exception on any account of a “nexus” requirement. Government agents forensically

                                             16
searched Kolsuz’s phone because they had reason to believe – and good reason to

believe, in the form of two suitcases filled with firearms parts – that Kolsuz was

attempting to export firearms illegally and without a license. See Kolsuz, 185 F. Supp. 3d

at 859–60. That is a transnational offense that goes to the heart of the border search

exception, which rests in part on “the sovereign interest of protecting and monitoring

exports from the country.” See Oriakhi, 57 F.3d at 1297; see also Boumelhem, 339 F.3d

at 423 (holding that exit search for firearms implicates “significant government interests”

not only in controlling exports but also in national security). This is not a case, in other

words, in which the government invokes the border exception on behalf of its generalized

interest in law enforcement and combatting crime. Cf. United States v. Vergara, 884

F.3d 1309, 1317 (11th Cir. 2018) (Jill Pryor, J., dissenting) (relying on “general law

enforcement justification” to approve evidentiary border searches would “untether the

[border search exception] from its justifications”). Here, there is a direct link between the

predicate for the search and the rationale for the border exception.

       Moreover, as the district court explained, the agents who searched Kolsuz’s phone

reasonably believed that their search would reveal not only evidence of the export

violation they already had detected, but also “information related to other ongoing

attempts to export illegally various firearms parts.” Kolsuz, 185 F. Supp. 3d at 860. The

government emphasizes that finding – not contested by Kolsuz – in its argument before

us, and properly so. The justification behind the border search exception is broad enough

to accommodate not only the direct interception of contraband as it crosses the border,

but also the prevention and disruption of ongoing efforts to export contraband illegally,

                                             17
through searches initiated at the border. See, e.g., Ramos, 190 F. Supp. 3d at 999

(approving post-arrest “investigatory” border search of cell phone for information about

larger smuggling organization and “more contraband entering into the country at that

time”); United States v. Mendez, 240 F. Supp. 3d 1005, 1007–10 (D. Ariz. 2017)

(approving post-arrest border search of cell phone for evidence of additional contraband

entering country); cf. United States v. Kim, 103 F. Supp. 3d 32, 44, 46, 59 (D.D.C. 2015)

(holding unreasonable forensic search of laptop at border where search was expected to

reveal evidence of past but not ongoing criminal activity).

       In the circumstances presented here, we agree with the government’s bottom line:

Because the forensic search of Kolsuz’s phone was conducted at least in part to uncover

information about an ongoing transnational crime – in particular, information about

additional illegal firearms exports already underway, by freight or in the custody of a

coconspirator, see Kolsuz, 185 F. Supp. 3d at 860 – it “fits within the core of the

rationale” underlying the border search exception. Brief of United States at 19–20.

                                            B.

       Most of Kolsuz’s appeal is devoted to his argument against application of the

border exception. But Kolsuz has a fallback position, as well: Even under the border

exception, Kolsuz contends, the forensic search of his phone constituted a nonroutine

border search “unsupported by the type of reasonable suspicion required to justify” such

searches. Defendant’s Brief at 31. Again, we disagree.




                                            18
                                             1.

       Like the district court, we begin by considering the first premise of Kolsuz’s

argument: that the forensic search of his cell-phone data qualifies as a nonroutine border

search, requiring some level of particularized suspicion. We agree with the district court

that particularly in light of the Supreme Court’s decision in Riley, a forensic border

search of a phone must be treated as nonroutine, permissible only on a showing of

individualized suspicion. See Kolsuz, 185 F. Supp. 3d at 852–58.

       As described above, the Supreme Court has held that even at the border,

individualized suspicion is necessary to justify certain “highly intrusive searches,” in

light of the significance of the individual “dignity and privacy interests” infringed.

Flores-Montano, 541 U.S. at 152. Beyond that general guidance, the Court has not

delineated precisely what makes a search nonroutine. Compare id. at 155 (removal and

disassembly of car’s gas tank does not qualify as nonroutine border search) with Montoya

de Hernandez, 473 U.S. at 541–42 (16-hour detention for monitored bowel movement

pending rectal examination is nonroutine). But as the district court ably explains, in

deciding whether a search rises to the level of nonroutine, courts have focused primarily

on how deeply it intrudes into a person’s privacy. Kolsuz, 185 F. Supp. 3d at 853. Under

that approach, border searches of luggage, outer clothing, and personal effects

consistently are treated as routine, while searches that are most invasive of privacy – strip

searches, alimentary-canal searches, x-rays, and the like – are deemed nonroutine and

permitted only with reasonable suspicion. See id. at 853 & n.14 (citing cases).



                                             19
       By that metric, even before the Supreme Court issued its 2014 decision in Riley,

there was a convincing case for categorizing forensic searches of digital devices as

nonroutine. See Cotterman, 709 F.3d at 963–68 (holding that forensic examination of

computer is nonroutine border search requiring reasonable suspicion); Saboonchi, 990 F.

Supp. 2d at 549–60 (same as to smartphones and flash drives). First is the matter of

scale: The sheer quantity of data stored on smartphones and other digital devices dwarfs

the amount of personal information that can be carried over a border – and thus subjected

to a routine border search – in luggage or a car. “The average 400-gigabyte laptop hard

drive can store over 200 million pages. . . . Even a car full of packed suitcases with

sensitive documents cannot hold a candle to the sheer, and ever-increasing, capacity of

digital storage.” Cotterman, 709 F.3d at 964. Subjected to comprehensive forensic

analysis, a digital device can reveal an unparalleled breadth of private information.

       The uniquely sensitive nature of that information matters, as well. Smartphones

and laptops “contain the most intimate details of our lives: financial records, confidential

business documents, medical records and private emails,” id., and also may provide

access to data stored remotely, id. at 965. 4 The report generated by the month-long

logical file system extraction of data from Kolsuz’s phone is a case in point, revealing

896 pages’ worth of sensitive data including personal contacts, photographs, web


       4
          The forensic search of Kolsuz’s phone, which remained in airplane mode
throughout, did not extend to information stored remotely (“in the cloud”), nor to residual
data of files that had been deleted by Kolsuz. Kolsuz, 185 F. Supp. 3d at 849 & n.8. Like
the district court, however, we decline “to distinguish an extensive forensic search of a
cell phone from a very extensive forensic search of a cell phone.” Id. at 857.

                                            20
browsing history, and a “history of [Kolsuz’s] physical location down to precise GPS

coordinates,” J.A. 94 – the kind of information that, analyzed cumulatively, “generates a

precise, comprehensive record of a person’s public movements that reflects a wealth of

detail about her familial, political, professional, religious and sexual associations.” See

United States v. Jones, 565 U.S. 400, 415 (2012) (Sotomayor, J., concurring). And

finally, while an international traveler can mitigate the intrusion occasioned by a routine

luggage search by leaving behind her diaries, photographs, and other especially personal

effects, the same is not true, at least practically speaking, when it comes to smartphones

and digital devices. Portable electronic devices are ubiquitous – for many, the most

reliable means of contact when abroad – and it is neither “realistic nor reasonable to

expect the average traveler to leave his digital devices at home when traveling.”

Saboonchi, 990 F. Supp. 2d at 556.

       And then came Riley, in which the Supreme Court confirmed every particular of

that assessment. Riley holds that the search incident to arrest exception, which allows for

automatic searches of personal effects in the possession of an arrestee, does not apply to

manual searches of cell phones. 134 S. Ct. at 2493–94. The key to Riley’s reasoning is

its express refusal to treat such phones as just another form of container, like the wallets,

bags, address books, and diaries covered by the search incident exception. See id. at

2488–90.    Instead, Riley insists, cell phones are fundamentally different “in both a

quantitative and a qualitative sense” from other objects traditionally subject to

government searches. Id. at 2489. And that is so, Riley explains, for precisely the

reasons already identified by cases treating border searches of digital devices as

                                             21
nonroutine: the “immense storage capacity” of cell phones, putting a vastly larger array

of information at risk of exposure, id.; the special sensitivity of the kinds of information

that may be stored on a phone, such as browsing history and historical location data, id. at

2490; and, finally, the “element of pervasiveness that characterizes cell phones,” id.,

making them an “insistent part of daily life,” id. at 2484.

       After Riley, we think it is clear that a forensic search of a digital phone must be

treated as a nonroutine border search, requiring some form of individualized suspicion.

See Kolsuz, 185 F. Supp. 3d at 858; see also United States v. Saboonchi, 48 F. Supp. 3d

815, 819 (D. Md. 2014) (“Saboonchi II”) (discussing ways in which Riley confirms prior

holding that border searches of digital devices are nonroutine). Indeed, the impact of

Riley is plain enough that the government’s brief does not seriously contest this point,

focusing instead on the argument (which we next address) that nonroutine or not, the

search of Kolsuz’s phone was justified under the border exception. 5 We also note that

shortly after argument in this case, the Department of Homeland Security adopted a

policy that treats forensic searches of digital devices as nonroutine border searches,

insofar as such searches now may be conducted only with reasonable suspicion of

       5
         The government does note that in Ickes, 393 F.3d at 505–07, our court treated a
search of a computer as a routine border search, requiring no individualized suspicion for
the search. But as the district court explained, Ickes approved a manual, on-site
inspection of computer contents that would be accessible to any user, and did not address
the use of the sophisticated forensic search methods at issue here. Kolsuz, 185 F. Supp.
3d at 853–54; see also Saboonchi, 990 F. Supp. 2d at 546 (distinguishing Ickes on same
ground). Because Kolsuz does not challenge the initial manual search of his phone at
Dulles, we have no occasion here to consider whether Riley calls into question the
permissibility of suspicionless manual searches of digital devices at the border.


                                             22
activity that violates the customs laws or in cases raising national security concerns. U.S.

Customs and Border Prot., CBP Directive No. 3340-049A, Border Search of Electronic

Devices 5 (2018). That the agency has chosen to adopt these requirements, of course,

does not establish that they are constitutionally mandated. Cf. Ickes, 393 F.3d at 507

(distinguishing between agency practice and constitutional requirements). But it does

suggest, as courts have anticipated, that the distinction between manual and forensic

searches is a perfectly manageable one, see Cotterman, 709 F.3d at 967 (categorizing

forensic searches as nonroutine requires only “that officers make a commonsense

differentiation between a manual review of files on an electronic device and application

of computer software to analyze a hard drive”), and that treating forensic phone searches

as nonroutine need not interfere unduly with the agency’s protective mission at the

border, see Saboonchi, 990 F. Supp. 2d at 570. 6

                                             2.

       That the forensic analysis of Kolsuz’s phone data qualifies as a nonroutine border

search does not resolve this case. Nonroutine searches are permitted under the border


       6
         The new policy does not use the “routine” and “nonroutine” terminology of
Supreme Court case law, distinguishing instead between “basic” and “advanced”
searches. But the import is the same. “Basic” searches (like those we term “manual”) are
examinations of an electronic device that do not entail the use of external equipment or
software and may be conducted without suspicion. “Advanced” searches (like “forensic”
searches) involve the connection of external equipment to a device – such as the
Cellebrite Physical Analyzer used on Kolsuz’s phone – in order to review, copy, or
analyze its contents, and are subject to the restrictions noted above. See U.S. Customs
and Border Prot., CBP Directive No. 3340-049A, Border Search of Electronic Devices 4–
5 (2018); Molina-Isidoro, 884 F.3d at 294 & n.2 (Costa, J., concurring).


                                            23
exception, so long as they are accompanied by the appropriate level of individualized

suspicion. See Montoya de Hernandez, 473 U.S. at 540–41 & n.4.

      The district court concluded that under the border exception, the “highest level of

Fourth Amendment protection available” is the reasonable suspicion standard, which was

met in this case. 7 Kolsuz, 185 F. Supp. 3d at 858–59. As the district court explained,

courts consistently have required only reasonable suspicion even when reviewing the

most intrusive of nonroutine border searches and seizures – like, for instance, the one at

issue in Montoya de Hernandez, in which the Supreme Court held that with reasonable

suspicion, the government could detain a traveler thought to be smuggling contraband in

her alimentary canal for 16 hours while it monitored her bowel movements and sought a

court order for a rectal examination. Id. at 852–53, 858–59.

      Of course, certain searches conducted under exceptions to the warrant requirement

may require more than reasonable suspicion. See, e.g., California v. Carney, 471 U.S.

386, 393–95 (1985) (holding that automobile exception to the Fourth Amendment

permits a warrantless search of a motor home if based on probable cause). Perhaps the

      7
         Kolsuz also argues that even if the search of his phone could be justified by
reasonable suspicion, what would be required is reasonable suspicion that contraband, as
opposed to evidence, would be found on the device. Otherwise, according to Kolsuz, the
search would be “untethered” from the constitutional justification for border searches:
the interception of contraband as it crosses the border. If this argument sounds familiar,
that is because it is a reformulation of Kolsuz’s threshold argument against any
application of the border exception to this case, addressed above. And for essentially the
reasons already given, we cannot agree. The district court found – and Kolsuz does not
dispute – that the agents here had reason to believe that their search of Kolsuz’s phone
would reveal not only evidence of past export-control violations, but also evidence of
ongoing efforts to smuggle firearms over the border. Kolsuz, 185 F. Supp. 3d at 860.
That is enough to “tether” the search to the rationale behind the border exception.

                                           24
same is true of some nonroutine border searches, as Kolsuz argues, but we need not

resolve that question here. As the government reminds us, even if a search is judged to

be constitutionally flawed in some way, its fruits need not be suppressed if the agents

acted “in reasonable reliance on binding precedent.” Davis v. United States, 564 U.S.

229, 241 (2011); see United States v. Baker, 719 F.3d 313, 320–21 (4th Cir. 2013)

(describing Davis). In such circumstances, suppression can do little to deter police

misconduct, and the “social costs” of suppression – the exclusion from trial of reliable

evidence bearing on guilt or innocence – outweigh any deterrence benefits. Davis, 564

U.S. at 237–38.

      At the time the CBP officers conducted their forensic search of Kolsuz’s phone,

there was at least some case law indicating that reasonable suspicion might be required.

See Kolsuz, 185 F. Supp. 3d at 855–58 (discussing cases). But there was no case

suggesting that even more would be necessary – for a forensic search of a phone at the

border or, indeed, for any border search, no matter how nonroutine or invasive. And that

remains the case today: Even as Riley has become familiar law, there are no cases

requiring more than reasonable suspicion for forensic cell phone searches at the border.

But see Vergara, 884 F.3d at 1313–19 (Jill Pryor, J., dissenting) (after Riley, forensic

search of phone is not subject to border search exception and therefore requires warrant

based on probable cause).

      Under these circumstances, we think it was reasonable for the CBP officers who

conducted the forensic analysis of Kolsuz’s phone to rely on the established and uniform

body of precedent allowing warrantless border searches of digital devices that are based

                                          25
on at least reasonable suspicion. See Molina-Isidoro, 884 F.3d at 293 (applying good-

faith exception to warrantless manual search of phone at border). Under Davis’s “good-

faith” exception to the Fourth Amendment exclusionary rule, that reasonable reliance by

itself is enough to bar suppression of the evidence generated by the search. See Baker,

719 F.3d at 321. Accordingly, we need not – and will not – reach the issue of whether

more than reasonable suspicion is required for a search of this nature in affirming the

judgment of the district court.     See Molina-Isidoro, 884 F.3d at 294 (Costa, J.,

concurring) (reliance on good-faith exception particularly appropriate in area of rapid

legal and technological change).



                                           III.

      For the reasons given above, the judgment of the district court is

                                                                           AFFIRMED




                                           26
WILKINSON, Circuit Judge, concurring in the judgment:

       I thank the majority for its thoughtful opinion. While I agree with much of what is

said, my point of departure is quite basic. The majority appears to leave the legislative

and executive branches shivering in the cold. Those branches have a critical role to play

in defining the standards for a border search, and they are much better equipped than we

are to appreciate both the privacy interests at stake and the magnitude of the practical

risks involved.

       The standard of reasonableness in the particular context of a border search should

be principally a legislative question, not a judicial one. Congress should decide that

standard. Courts should apply it. This is a separation of powers approach that makes use

of the respective capabilities of all three branches of government, not just one.

       The infirmity of a constitutional rule in the unique context of a border search is

clear. Such a rule claims for courts the sole prerogative to set standards in an area where

legislative inquiry would be invaluable and where the executive maintains a strong

sovereign interest. Diminishing the other two branches flirts with real-life dangers. The

whole enterprise calls for the greatest caution and circumspection, not premature

declarations of constitutional rules.

       If individualized suspicion is to be required in order to conduct what the majority

asserts is a “nonroutine border search,” Maj. Op. at 4, then Congress must say so. And in

all events, there was plainly reasonable suspicion to conduct the search here. The

majority should have stopped right there. Assuming without deciding that reasonable

suspicion was even required, it is present here in triplicate.

                                              27
       Instead my colleagues wander from what Article III indisputably envisions as the

core role of courts: simply to decide a case or controversy. The majority turns

prescriptive, but the pronouncement here is too abstract and floats too far above the

realities at the border.

       Lethal capabilities are advancing at a rapid pace. Detection of destructive devices

is becoming more difficult. Nation states, terrorist bands, and individual arms merchants

see profit and prestige and power in joining the arms race. Might we wish to hear in a

manner more probing than appellate briefs and oral argument exactly what are the

dimensions of the threats we face? What makes us think the elective branches would

downgrade the significant privacy interests the majority rightly identifies? Might the

other two branches, if given a fair chance, have something to say? And do not Articles I

and II, which set forth the legislative and executive roles in matters of grave international

import, give them the right to say it? Who are we to propound the idea that democratic

bodies, where Fourth Amendment reasonableness is concerned, have nothing to

contribute?

       Alarmist? Hyperbolic? Perhaps. But if we so limit the role of our coordinate

branches with a constitutional ruling, how shall we ever know?

                                             I.

       The majority fairly recounts the facts here, and they are straightforward and

incriminating. Before his arrest at Dulles airport, Customs and Border Protection (CBP)

agents had twice stopped Kolsuz, a Turkish national, at JFK airport for carrying

contraband firearms parts proscribed by statute. See 22 U.S.C. § 2278. On both

                                             28
occasions, Kolsuz failed to produce the license required to export those parts. Both times,

CBP agents informed Kolsuz that he needed a license to export those items.

       Kolsuz reentered the United States on January 25, 2016, on a tourist visa. He again

purchased numerous gun parts. Law enforcement officials who were familiar with

Kolsuz’s previous attempts to export contraband firearms asked CBP to search Kolsuz’s

bags when he tried to return to Turkey. When Kolsuz arrived at Dulles, CBP searched his

bags. The inspection revealed eighteen handgun barrels, twenty-two 9 mm handgun

magazines, four .45 caliber handgun magazines, and one .22 caliber Glock conversion

kit. All of these firearms parts are restricted items on the U.S. Munitions List. At no time

did Kolsuz have permission to export them. Based on Kolsuz’s previous attempts to bring

firearm parts out of the country, CBP had ample reason to suspect that Kolsuz might

again try to export firearms.

       Following the search of Kolsuz’s bags, CBP officers interrogated Kolsuz and

performed a cursory inspection of his iPhone. At the end of the interrogation, Kolsuz was

arrested and his iPhone seized. At that point, his iPhone was transported to Sterling,

Virginia, where federal law enforcement conducted an “advanced logical file system

extraction” of the iPhone. This extraction, as the majority notes, generated an 896-page

report on the information contained in the phone.

                                            II.

       This was plainly a border search. See Maj. Op. at 18. Assuming reasonable

suspicion of Kolsuz’s criminal activity is somehow required, it clearly existed here. We

need go no further. Rather than deciding the case on solid and suitably limited grounds,

                                            29
the majority goes on to prescribe a constitutional standard whose rationale would label a

great many cell phone searches undertaken at the border as “nonroutine” and forbidden

absent prior individualized suspicion.

       While the majority purports not to reach the question of the justification required

for the manual search of Kolsuz’s cell phone at Dulles airport, see Maj. Op. at 22 n.5, the

rhetorical thrust of its opinion as concerns cell phones and smartphones may be read by

many courts to require individualized suspicion for border searches of all cell phones

period. Or if the majority intends a less sweeping standard, the slipperiness of the

distinction between intrusive and less intrusive cell phone searches and between those

that are routine and those that are nonroutine will lead, I fear, to difficulties in application

down the road. While the majority’s constitutional venture may be correct, it also may

well not be. Again, we are not the ones to set the standard.

       We are, each of us, in over our heads. We have no idea of the dangers we are

courting. JFK and Dulles are quintessential border posts. See Almeida-Sanchez v. United

States, 413 U.S. 266, 273 (1973). Thousands of international travelers go through them

every day. Yet the majority hardly grapples with how law enforcement is expected to

ascertain individualized suspicion when dealing with such numbers. The privacy interest,

while weighty, is the only side of a precarious balance that seems to concern the majority,

and this in the application of the Fourth Amendment, which articulates reasonableness

and hence balance as a standard. See Katz v. United States, 389 U.S. 347, 360 (1967).

       One would hope that rather than charging unnecessarily ahead, the majority would

recognize the need for congressional input, which the enunciation of constitutional

                                              30
standards makes more difficult. Constitutional standards are preemptive. They sweep all

other pieces off the board. Judicially promulgated constitutional standards say essentially,

“That’s that. The Constitution is the highest law, and the judiciary shall be its sole

guardian.”

       Empirical questions lie at the heart of the tension between privacy and security

interests at the border. How many people travel through international airports every day?

What screening techniques and investigative resources does government have available?

What materials are being smuggled in and out, and by whom? What practical obstacles

exist to individualized findings? What, in other words, is the magnitude of danger courted

by progressive step-ups of search requirements?

       The limited glimpse from a single case does no more than beg the question: What

is the reality of it all? This is why any Fourth Amendment standard is best designed here

through the more adaptable legislative process and the wider lens of legislative hearings.

See Riley v. California, 134 S. Ct. 2473, 2497-98 (2014) (Alito, J., concurring in the

judgment) (“Legislatures, elected by the people, are in a better position than we are to

assess and respond to the changes that have already occurred and those that almost

certainly will take place in the future.”). For “[a]s new technologies continue to appear in

the marketplace and outpace existing surveillance law, the primary job of evaluating their

impact on privacy rights and of updating the law must remain with the branch of

government designed to make such policy choices, the legislature.” In re Askin, 47 F.3d

100, 106 (4th Cir. 1995).



                                            31
       The majority contends that the “Department of Homeland Security adopted a

policy that treats forensic searches of digital devices as nonroutine border searches.” Maj.

Op. at 22. I think the document is more complex than this, but in all events, it proves my

point—that in this narrow area agency policy born of actual and ongoing experience is

more adaptable than a freeze-frame constitutional ruling.

       Courts too often assume Congress is desensitized to the need for privacy

protections. This does lawmakers a disservice. Congress has long sought to strike a

balance between privacy and security in the context of digital searches. See, e.g., USA

Freedom Act of 2015, Pub. L. No. 114-23, 129 Stat. 268 (limiting government

surveillance of telephone records); 18 U.S.C. §§ 2510-22 (2012) (limiting the

government’s ability to monitor electronic communications); Orin S. Kerr, The Effect of

Legislation on Fourth Amendment Protection, 115 Mich. L. Rev. 1117, 1120 (2017)

(observing “the recent enactment of more and stronger statutory privacy laws” by federal

and state legislatures in the past five years). And, though of course not directly relevant in

the context of a federal border search, states have historically also protected Fourth

Amendment privacy rights. See Kerr, 115 Mich. L. Rev. at 1120 (documenting state

statutes limiting the use of digital searches).

       It is sometimes said in non-border search cases that the judiciary does no more

than provide “a floor” which Congress can exceed at its discretion. See, e.g., Kelsey v.

Cty. of Schoharie, 567 F.3d 54, 64 (2d Cir. 2009); Graves v. Mahoning Cty., 821 F.3d

772, 778 (6th Cir. 2016). But the so-called floor in this case is not some innocuous

minimum, but a hugely consequential policy judgment that certain categories of border

                                              32
searches will require individualized suspicion. The fact that Congress has not thus far

seen fit to adopt a court’s preferred standard gives us no license to act preemptively with

an unnecessary constitutional disquisition. The dangers of this notion are underscored by

the majority’s reservation here of the question whether probable cause or a warrant may

be required for some unspecified categories of border searches in the future. See Maj. Op.

at 24-25. This does not sound like any sort of “floor” at all.

       The dangers of judicial standard-setting in an area as sensitive as border searches

is thus apparent. Here the legislative process would be informed by numerous

representatives of the executive branch, who can lend their practical insights and

experience to the inquiry. The executive’s role has always been thought especially

important in an area such as border searches, where it has long been held to have a

uniquely sovereign interest. The border search exception to the Fourth Amendment’s

warrant requirement is based on the “longstanding right of the sovereign to protect itself

by stopping and examining persons and property crossing into this country.” United

States v. Ramsey, 431 U.S. 606, 616 (1977). As the Supreme Court has explained, “[t]he

Government’s interest in preventing the entry of unwanted persons and effects is at its

zenith at the international border.” See United States v. Flores-Montano, 541 U.S. 149,

152 (2004). That interest is so powerful that border searches “are reasonable simply by

virtue of the fact that they occur at the border.” Ramsey, 431 U.S. at 616.

       The role of courts is thus not to blanket the field of border searches by preempting

constitutionally the contributions that the other two branches of our government are

constitutionally empowered and uniquely positioned to make. Marbury v. Madison did of

                                             33
course say that it is “emphatically the province and duty of the judicial department to say

what the law is.” 5 U.S. (1 Cranch) 137, 177 (1803). But that is a very different

proposition from holding that constitutional interpretation must be solely a judicial

function. Indeed “the general architecture of [the Constitution] would seem to imply a

basic coequality among the three departments. . . . [I]t nowhere explicitly raises the Court

above coordinate legislative and executive departments.” Akhil Reed Amar, Architecture,

77 Ind. L.J. 671, 692-93 (2002). This is not a new idea. James Madison wrote that “none

of [the three branches of government] ought to possess, directly or indirectly, an

overruling influence over the others in the administration of their respective powers.” The

Federalist No. 48 (James Madison). But it is precisely that “overruling influence” the

majority asserts in its unnecessary constitutional exercise today.

                                            III.

       The general search that all of us must undergo at airports attests to the difficulties

of ensuring airborne security through individualized suspicion. Our new world has

brought inconvenience and intrusions on an indiscriminate basis, which none of us

welcome, but which most of us undergo in the interest of assuring a larger common good.

Our old world of relative security and relative privacy, if indeed it ever existed, is now

gone with the wind. It is painful to dream of retrieving what is ours no longer.

       The Supreme Court has often noted how technology endangers privacy. As it

observed in Riley, “[m]odern cell phones, as a category, implicate privacy concerns far

beyond those implicated by the search of a cigarette pack, a wallet, or a purse.” 134 S. Ct.

at 2488-89. But Riley involved the warrantless search of a cell phone following an

                                             34
ordinary roadside arrest after a traffic violation. The defendant was not at the border. The

setting here is far different from Riley.

       Nor does the privacy interest recognized in Riley begin to answer the question of

who should strike the balance between privacy and security at the border of the country,

the point most freighted with security threats and the point at which a nation asserts and

affirms its very right to nationhood.

       Porous borders are uniquely tempting to those intent upon inflicting the vivid

horrors of mass casualties. Then too, there is the danger of highly classified technical

information being smuggled out of this country only to go into the hands of foreign

nations who do not wish us well and who seek to build their armaments to an ever more

perilous state.

       It is no secret that rapid technological advances have enhanced the ability of

criminal syndicates and terrorist networks to execute transnational schemes through the

coordination now made possible by instantaneous communications. To give criminal

enterprises the advantage of technological advancements and at the same time impair

access of law enforcement to those same developments risks recalibrating the Fourth

Amendment balance in a manner that does not comport with reasonableness. Cell phones

may prove essential to revealing the scope of a conspiracy; who is involved; what

weapons and devices the conspirators possess; what the purpose and plans and timing of

the plotted criminal acts may be; and where indeed those who would carry out these acts

may be located.



                                            35
       But to stop there is to halve the equation. The majority is right to emphasize that

searches of cell phones and the like can reveal a trove of data unconnected to any

criminal offense. The intrusion upon personal privacy is undoubtedly severe. One may of

course say that international travelers are on notice that border inspections may be

uniquely intrusive, and that travelers can prepare for that prospect by not taking a full

load of personal data abroad, where additional dangers of theft and inadvertent loss may

also await. But the fact that we can pack our digital suitcase with the same care that we

pack personal belongings in traditional luggage still does not nullify the reality that these

sorts of searches look into our lives in a way that is deeply uncomfortable, especially

when government itself becomes the agent of intrusion. But the ultimate question here is

not whether there is a balance to be struck between what are highly significant privacy

and security interests. It is what branch of government is best suited to make that

determination. In this case, where there is a longstanding historical practice in border

searches of deferring to the legislative and executive branches, the majority should have

shown a modest measure of restraint simply by deciding the case. Our role in this narrow

area is more the application of standards than the creation of them. In reaching to

formulate a constitutional rule, the majority has turned the whole thing on its head.

       We are ruling in a vacuum. We are building a doctrinal house without foundation.

The majority opinion provides little context or background or real-life picture of Dulles

Airport. It leaves little role for the legislative branch. At what point the domestic

conveniences of cell phone use should ripen into transnational entitlements is primarily

for the political branches to determine. The elected branches are also best able to gauge at

                                             36
what point the creeping constitutionalization of border searches reflects the cultural

habits and practices of an elite group of transnational Americans at the risk of

endangerment that knows no class bounds.

       It is ill advised to ignore the role of the political branches in addressing a

phenomenon that may fall short of the formal warfare contemplated in Articles I and II,

but still retains major features of international conflict. To reach beyond the Article III

function is to court grave dangers which we may perceive as remote and hypothetical

until one day, very suddenly, they are not. Not that any one case or any one appellate

court will likely bring down havoc on our heads. In our shielded circumstances, we may

never know or be apprised of many effects of our decisions. Still it is uncomfortable to

guess. I have nothing but respect for my friends in the majority. But taken cumulatively,

rulings slowly constitutionalizing border searches are taking chances with the safety and

lives of our fellow Americans. And this, as a judge, I cannot do.




                                            37

```

---

## GROUP: content/cases/United States v. Leary.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Leary"
type: case
citation: "846 F.2d 592 (1988)"
parallel_cite: ""
neutral_cite: "1988 U.S. App. LEXIS 5755; 1988 WL 39811"
court: "U.S. Court of Appeals, Tenth Circuit"
court_level: coa
circuit: 10th
year: 1988
date_decided: 1988-05-02
docket: ""
authority_weight: "Binding in-circuit — 10th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: null
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Leary
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/505922/united-states-v-richard-j-leary-and-fl-kleinberg-co/"
  cluster_id: 505922
  opinion_id: 505922
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Leon]]", "[[Massachusetts v. Sheppard]]", "[[Coolidge v. New Hampshire]]", "[[Groh v. Ramirez]]"]
aliases: ["United States v. Leary (10th Cir. 1988)", "United States v. Richard J. Leary"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "particularity", "general-warrant", "overbreadth", "good-faith-exception", "tenth-circuit"]
holding: "A facially overbroad / general warrant (authorizing seizure of records 'relating to' violations of the export laws, offering no…"
lake:
  record_id: United States v. Leary
  status: verified
  projected_at: 2026-07-09
---

# United States v. Leary

*846 F.2d 592 (10th Cir. 1988)* · U.S. Court of Appeals, Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Customs agents investigating suspected violations of the federal export laws by F.L. Kleinberg & Co. (and Richard Leary) obtained a warrant authorizing seizure of business records "relating to" violations of the export laws, with no further limitation. Executing it, the agents seized broad swaths of documents, including records concerning transactions, countries, and commodities not mentioned in the affidavit and unrelated to the suspected deal. The district court suppressed the evidence as the product of an overbroad warrant; the government appealed.

## Issue
(1) Whether a warrant authorizing seizure of records "relating to" violations of the export laws satisfies the Fourth Amendment's [[Particularity|particularity]] requirement; and (2) whether the [[United States v. Leon]] [[The Good-Faith Exception|good-faith exception]] saves evidence seized under such a facially overbroad warrant.

## Rule
No to both. The [[Particularity|particularity]] requirement bars general, exploratory rummaging: it "ensures that a search is confined in scope to particularly described evidence relating to a specific crime for which there is demonstrated probable cause." — 846 F.2d at 600 (quoting *Voss v. Bergsgaard*). ^pin-600

A warrant that fails to cabin the executing officer's discretion is an unconstitutional general warrant: "A warrant that directs an officer to seize records 'relating to' violations of the federal export laws offers no such guidelines. The officers were left to their own discretion." — *Id.* at 609. ^pin-609

The Leon [[The Good-Faith Exception|good-faith exception]] does not save such a warrant: "We find the warrant so facially deficient in its description of the items to be seized that the executing officers could not reasonably rely on it." — [*Id.* at 609](https://www.courtlistener.com/opinion/505922/united-states-v-richard-j-leary-and-fl-kleinberg-co/#:~:text=We%20find%20the%20warrant%20so). ^pin-609a

"Accordingly, we hold that the 'good faith' exception is inapplicable in these circumstances and affirm the district court's decision to suppress all of the evidence from the Kleinberg warrant." — *Id.* at 610. ^pin-610

## Application
On these facts the warrant was an unconstitutional general warrant and good faith could not rescue it. The "relating to" language gave the agents no criteria to distinguish seizable from non-seizable records, and the record showed they used the warrant's breadth (not any affidavit specificity) to seize documents far beyond the suspected transaction — "[t]here is no portion of the Kleinberg warrant that adequately defines the items to be seized," so the affidavit could not cure it and severance was impossible. Good faith was unavailable because a reasonably well-trained officer "should know that a warrant must provide guidelines for determining what evidence may be seized," and a warrant this facially deficient could not be reasonably presumed valid — placing it within *[[United States v. Leon|Leon]]*'s own exception for warrants "so facially deficient . . . that the executing officers cannot reasonably presume it to be valid." The Court did not reach the separate probable-cause defect.

## Conclusion
The warrant was facially overbroad and the *[[United States v. Leon|Leon]]* [[The Good-Faith Exception|good-faith exception]] did not apply; the district court's suppression of all evidence seized under it was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 10th Cir.**
- No negative subsequent treatment identified. *Leary* applies the [[Particularity|particularity]] rule of [[Coolidge v. New Hampshire]] and marks the boundary of [[United States v. Leon]] / [[Massachusetts v. Sheppard]] good-faith: a facially overbroad general warrant cannot support objectively reasonable reliance.

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Leary*, 846 F.2d 592 (10th Cir. 1988) — https://www.courtlistener.com/opinion/505922/united-states-v-richard-j-leary-and-fl-kleinberg-co/ — pinpoints: 600, 609, 610.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0be367dea03651b6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "846 F.2d 592 (1988)", "court": "U.S. Court of Appeals, Tenth Circuit", "neutral_cite": "1988 U.S. App. LEXIS 5755; 1988 WL 39811", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Leary", "year": "1988"}}
{"assertion_id": "25cbf3f954ccc1f3", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A facially overbroad / general warrant (authorizing seizure of records 'relating to' violations of the export laws, offering no…", "title": "United States v. Leary"}}
{"assertion_id": "fb7edbbd184a5ca4", "dimension": "support", "kind": "home_role", "locator": {"home": "The Good-Faith Exception"}, "payload": {"home": "The Good-Faith Exception", "role": "Key — Progeny / Refinement", "title": "United States v. Leary"}}
{"assertion_id": "16de1d431dcee7ff", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 10th Cir.", "title": "United States v. Leary"}}
{"assertion_id": "7b86941c165ec240", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Leary", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Leary", "varies_by_point": "false"}}
```

### lake record — United States v. Leary

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Leary",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Richard J. Leary, and F.L. Kleinberg & Co.",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellant, v. Richard J. LEARY, and F.L. Kleinberg & Co., Defendants-Appellees",
    "input_case_name": "United States v. Leary",
    "court": "U.S. Court of Appeals, Tenth Circuit",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "10th",
    "state": null,
    "date_decided": "1988-05-02",
    "year": 1988,
    "docket": null,
    "cluster_id": 505922,
    "lead_opinion_id": 505922,
    "sibling_ids": [
      505922
    ],
    "absolute_url": "/opinion/505922/united-states-v-richard-j-leary-and-fl-kleinberg-co/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "846 F.2d 592",
      "volume": "846",
      "reporter": "F.2d",
      "page": "592",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1988 U.S. App. LEXIS 5755",
        "volume": "1988",
        "reporter": "U.S. App. LEXIS",
        "page": "5755",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 WL 39811",
        "volume": "1988",
        "reporter": "WL",
        "page": "39811",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "846 F.2d 592",
        "volume": "846",
        "reporter": "F.2d",
        "page": "592",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 U.S. App. LEXIS 5755",
        "volume": "1988",
        "reporter": "U.S. App. LEXIS",
        "page": "5755",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 WL 39811",
        "volume": "1988",
        "reporter": "WL",
        "page": "39811",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "846 F.2d 592",
    "official_selection": {
      "court_class": "coa",
      "selected": "846 F.2d 592",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-600",
      "page": null,
      "quote": "violations of the export laws satisfies the Fourth Amendment's particularity requirement; and (2) whether the [[United States v. Leon]] good-faith exception saves evidence seized under such a facially overbroad warrant. ## Rule No to both. The particularity requirement bars general, exploratory rummaging: it",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-609",
      "page": null,
      "quote": "A warrant that directs an officer to seize records 'relating to' violations of the federal export laws offers no such guidelines. The officers were left to their own discretion.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-609a",
      "page": null,
      "quote": "We find the warrant so facially deficient in its description of the items to be seized that the executing officers could not reasonably rely on it.",
      "star_marker": "609",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 90650,
      "fragment": "#:~:text=We%20find%20the%20warrant%20so",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-610",
      "page": null,
      "quote": "Accordingly, we hold that the 'good faith' exception is inapplicable in these circumstances and affirm the district court's decision to suppress all of the evidence from the Kleinberg warrant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": null,
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Leary",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Cooper",
          "cluster_id": 223162,
          "cite": [
            "654 F.3d 1104",
            "108 A.F.T.R.2d (RIA) 5815",
            "2011 U.S. App. LEXIS 16825",
            "2011 WL 3559929"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Russell R. George, AKA Rusty, and Pamela A. Johnson-Sherman, Francis R. Lajoice",
          "cluster_id": 590903,
          "cite": [
            "975 F.2d 72",
            "1992 U.S. App. LEXIS 22728"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Ray Erwin",
          "cluster_id": 523285,
          "cite": [
            "875 F.2d 268",
            "1989 U.S. App. LEXIS 6543",
            "1989 WL 51352"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re Grand Jury Subpoenas Dated December 10, 1987. Does I Through IV v. United States",
          "cluster_id": 556527,
          "cite": [
            "926 F.2d 847",
            "91 Daily Journal DAR 1973",
            "91 Cal. Daily Op. Serv. 1168",
            "1991 U.S. App. LEXIS 2243"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thao Dinh Le",
          "cluster_id": 157748,
          "cite": [
            "173 F.3d 1258",
            "1999 Colo. J. C.A.R. 2740",
            "1999 U.S. App. LEXIS 5794",
            "1999 WL 176192"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Daniel Scott Gahagan (87-1991), Michael John Gahagan (87-1993), Susan Soper (87-1992)",
          "cluster_id": 517440,
          "cite": [
            "865 F.2d 1490"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tanell Rashaad Curry, T/n Tanell R. Curry",
          "cluster_id": 546301,
          "cite": [
            "911 F.2d 72",
            "1990 U.S. App. LEXIS 13423",
            "1990 WL 111468"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Galpin",
          "cluster_id": 931473,
          "cite": [
            "720 F.3d 436",
            "2013 WL 3185299"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mark James Dahlman",
          "cluster_id": 660281,
          "cite": [
            "13 F.3d 1391",
            "1993 U.S. App. LEXIS 33363",
            "1993 WL 527367"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Burke",
          "cluster_id": 184136,
          "cite": [
            "633 F.3d 984",
            "2011 U.S. App. LEXIS 2082",
            "2011 WL 310520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael McMonagle v. Northeast Women's Center, Inc",
          "cluster_id": 112364,
          "cite": [
            "493 U.S. 901",
            "110 S. Ct. 261",
            "58 U.S.L.W. 3237",
            "107 L. Ed. 2d 210",
            "1989 U.S. LEXIS 4670"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Parker D. Langston, United States of America v. Huey Lee Francis, United States of America v. Enoch McIlroy United States of America v. William McIlroy United States of America v. James McIlroy United States of America v. Speck Aron Ross",
          "cluster_id": 587373,
          "cite": [
            "970 F.2d 692",
            "1992 U.S. App. LEXIS 15017"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joaquin Emilio Mesa-Rincon, United States of America v. Peter Scott Stoppe",
          "cluster_id": 546962,
          "cite": [
            "911 F.2d 1433",
            "1990 U.S. App. LEXIS 14187",
            "1990 WL 117972"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mark A. Harris",
          "cluster_id": 541818,
          "cite": [
            "903 F.2d 770",
            "30 Fed. R. Serv. 586",
            "1990 U.S. App. LEXIS 7973",
            "1990 WL 62995"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James S. Anderson",
          "cluster_id": 757710,
          "cite": [
            "154 F.3d 1225",
            "1998 Colo. J. C.A.R. 5134",
            "1998 U.S. App. LEXIS 22547",
            "98 CJ C.A.R. 5134"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Guidry",
          "cluster_id": 159006,
          "cite": [
            "199 F.3d 1150",
            "2000 Colo. J. C.A.R. 16",
            "84 A.F.T.R.2d (RIA) 7443",
            "1999 U.S. App. LEXIS 33145"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Arthur Theodore Towne Dane Joseph Treiber",
          "cluster_id": 610668,
          "cite": [
            "997 F.2d 537",
            "93 Cal. Daily Op. Serv. 4520",
            "93 Daily Journal DAR 7722",
            "1993 U.S. App. LEXIS 14481",
            "1993 WL 210527"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. SDI Future Health, Inc.",
          "cluster_id": 1459636,
          "cite": [
            "568 F.3d 684",
            "103 A.F.T.R.2d (RIA) 2436",
            "2009 U.S. App. LEXIS 13003",
            "2009 WL 1508763"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Roccaforte",
          "cluster_id": 1274940,
          "cite": [
            "919 P.2d 799",
            "20 Brief Times Rptr. 997",
            "1996 Colo. LEXIS 209",
            "1996 WL 342294"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Center Art Galleries--Hawaii, Inc. William D. Mett v. United States",
          "cluster_id": 523623,
          "cite": [
            "875 F.2d 747",
            "1989 U.S. App. LEXIS 6983",
            "1989 WL 51355"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. Gracey",
          "cluster_id": 154737,
          "cite": [
            "111 F.3d 1472",
            "1997 WL 192018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Herrera",
          "cluster_id": 167373,
          "cite": [
            "444 F.3d 1238",
            "2006 U.S. App. LEXIS 9830",
            "2006 WL 1017642"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re the Matter of the Search of Kitty's East, 735 E. Colfax Avenue, Denver, Colorado. Kitty's East v. United States",
          "cluster_id": 543204,
          "cite": [
            "905 F.2d 1367",
            "1990 U.S. App. LEXIS 9064",
            "1990 WL 74065"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ezra Griffith",
          "cluster_id": 4419946,
          "cite": [
            "867 F.3d 1265",
            "2017 WL 3568288",
            "2017 U.S. App. LEXIS 15636"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Angevine",
          "cluster_id": 162077,
          "cite": [
            "281 F.3d 1130",
            "2002 U.S. App. LEXIS 2746",
            "2002 WL 254138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(505922) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca10)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(505922)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNCZzPTE1ODkwNjEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28505922%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(505922)",
        "reviewed": 13,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 13,
        "triage_read": 0,
        "triage_snippet_classified": 13
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(505922)",
    "indexed_citing_opinions": 121,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 505922,
        "count": 121,
        "count_source": "search"
      }
    ],
    "citation_count": 230,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-leary.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU0OTI2Njgmcz00NDExNjU3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28505922%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 505922,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 105594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 109522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 110325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 111066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 111252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 111263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 304369,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 324061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 346767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 350518,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 355493,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 362453,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 371945,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 373913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 374752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 376886,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 380192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 387515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 392049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 393709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 394830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 397225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 405042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 406519,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 408050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 412106,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 424091,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 434740,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 440371,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 442866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 444625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 445307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 450796,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 451731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 451751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 451967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 453574,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 458765,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 458774,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 458949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 458952,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 461301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 461431,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 461601,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 463621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 467613,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 471869,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 472649,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 474531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 474635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 475515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 475840,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 478417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 479836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 480985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 484648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 484709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 487817,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 492430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 493275,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 493687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 495037,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 498743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 501767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 502477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 503533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 1392737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 1394599,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 1482053,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 1519992,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 1577597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 1875700,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 1876547,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 2149373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 2595045,
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
    "date_created": "2026-07-06T01:16:56Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:17:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:17:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:20:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:17:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Leary (truncated)

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b690-7">
  STEPHEN H. ANDERSON, Circuit Judge.
 </author>
<p id="b690-8">
  The government appeals from the district court’s decision granting defendants’ motion to suppress evidence seized under a search warrant. We affirm the district court, holding that the defendants’ fourth amendment rights were infringed, that the search warrant was facially overbroad and invalid, and that the evidence seized should be suppressed.
 </p>
<p id="b690-9">
  I. Background
 </p>
<p id="b690-10">
  This appeal stems from the execution of a search warrant at the offices of the F.L. Kleinberg Company (“Kleinberg”) in Boulder, Colorado on August 23, 1984. Klein-berg and Richard J. Leary, a vice-president at Kleinberg, were subsequently indicted for conspiring to violate the Export Administration Act. 50 U.S.C.App. § 2410. Kleinberg and Leary, as defendants, moved to suppress the fruits of the search of the Kleinberg offices. The district court granted that motion and the government appeals pursuant to <span class="citation no-link">18 U.S.C. § 3731</span>.
 </p>
<p id="b690-11">
  The search warrant was obtained by federal customs agent John Juhasz on the basis of his affidavit alleging violations of the Arms Export Control Act, <span class="citation no-link">22 U.S.C. § 2778</span>, and the Export Administration Act. The affidavit recites in detail the purchase and attempted export of a Micro-tel Precision Attenuation Measurement Receiver
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  by Kleinberg in 1984. In short, the affidavit alleges that Kleinberg did not have the proper license to export this particular piece of equipment and that Kleinberg was attempting to illegally export the receiver to the People’s Republic of China via a series of “front” companies in Hong Kong. The affidavit addresses only this single transaction and the companies
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  involved in that transaction. No other companies, countries, or commodities are mentioned in the affidavit or alleged to be part of any illegal export scheme.
 </p>
<p id="b690-16">
  Based on the affidavit, a warrant was issued to search the Kleinberg offices and seize the following property:
 </p>
<blockquote id="Avh">
  Correspondence, Telex messages, contracts, invoices, purchase orders, shipping documents, payment records, export documents, packing slips, technical data, recorded notations, and other records and communications relating to the purchase, sale and illegal exportation of materials in violation of the Arms Export Control Act, 22 U.S.C. 2778, and the Export Administration Act of 1979, 50 U.S. C.App. 2410.
 </blockquote>
<p id="b690-17">
  The warrant was executed on August 23, 1984 by Agent Juhasz and six other Customs officers. Twenty boxes of business records were seized including references to sales and sales contacts throughout the world, telexes to Australia and South Africa, information from applicants for employment with Kleinberg, Leary’s application with Shearson American Express for per
  <span citation-index="1" class="star-pagination" label="595"> 
   *595
   </span>
  sonal financial planning, Leary’s life insurance policy, and correspondence relating to other businesses for which Leary acted as sales representative.
 </p>
<p id="b691-4">
  After the indictment, Kleinberg and Leary moved to suppress all of the evidence seized in the search. The district court granted that motion, finding first that the affidavit was not supported by probable cause,
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  and second, that the warrant did not sufficiently specify the evidence to be seized. The court also found that the “good faith” exception to the exclusionary rule adopted by the United States Supreme Court in
  <em>
   United States v. Leon,
  </em>
  <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U.S. 897</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">82 L.Ed.2d 677</a></span> (1984) was inapplicable.
 </p>
<p id="b691-5">
  On appeal, the government argues (1) Leary and Kleinberg have no standing to raise a fourth amendment claim; (2) the warrant was sufficiently particular in specifying the items to be seized; (3) the warrant was supported by probable cause; and (4) even if the warrant is found upon review to be invalid, reliance on the warrant was “objectively reasonable” and the evidence should not be suppressed under the reasoning of
  <em>
   <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>.
  </em>
</p>
<p id="b691-6">
  II. Standing
 </p>
<p id="b691-7">
  In
  <em>
   Rakas v. Illinois,
  </em>
  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U.S. 128</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. 421</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">58 L.Ed.2d 387</a></span> (1978) the Supreme Court abandoned a separate analysis of “standing” for claims of violations of the fourth amendment in favor of an analysis focusing on the “substantive question of whether or not the proponent of the motion to suppress has had his own Fourth Amendment rights infringed by the search and seizure which he seeks to challenge.”
  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#133" aria-description="Citation for case: Rakas v. Illinois"><em>
   Id.
  </em>
  at 133</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#425" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. at 425</a></span>.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
<em>
   See Rawlings v. Kentucky,
  </em>
  <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/#104" aria-description="Citation for case: Rawlings v. Kentucky">448 U.S. 98, 104</a></span>, <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/#2561" aria-description="Citation for case: Rawlings v. Kentucky">100 S.Ct. 2556, 2561</a></span>, <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">65 L.Ed.2d 633</a></span> (1980);
  <em>
   United States v. Hansen,
  </em>
  <span class="citation" data-id="392049"><a href="/opinion/392049/united-states-v-gary-e-hansen-daniel-e-means-aka-daniel-e-johnson/" aria-description="Citation for case: United States v. Gary E. Hansen, Daniel E. Means, AKA...">652 F.2d 1374</a></span>, 1379 n. 2 (10th Cir.1981). “Whether a person has standing to contest a search on fourth amendment grounds turns on whether the person had a legitimate expectation of privacy in the area searched, not merely in the items seized.”
  <em>
   United States v. Skowronski,
  </em>
  <span class="citation" data-id="493687"><a href="/opinion/493687/united-states-v-william-michael-skowronski/#1418" aria-description="Citation for case: United States v. William Michael Skowronski">827 F.2d 1414, 1418</a></span> (10th Cir.1987) (citing
  <em>
   United States v. Salvucci,
  </em>
  <span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/#93" aria-description="Citation for case: United States v. Salvucci">448 U.S. 83, 93</a></span>, <span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/#2554" aria-description="Citation for case: United States v. Salvucci">100 S.Ct. 2547, 2554</a></span>, <span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">65 L.Ed.2d 619</a></span> (1980)). Determining whether a legitimate or justifiable expectation of privacy exists, in turn, involves two inquiries. First, the claimant must show a subjective expectation of privacy in the area searched, and second, that expectation must be one that “society is prepared to recognize as ‘reasonable.’ ”
  <em>
   Hudson v. Palmer,
  </em>
  <span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/#525" aria-description="Citation for case: Hudson v. Palmer">468 U.S. 517, 525</a></span>, <span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/#3199" aria-description="Citation for case: Hudson v. Palmer">104 S.Ct. 3194, 3199</a></span>, <span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/" aria-description="Citation for case: Hudson v. Palmer">82 L.Ed.2d 393</a></span> (1984) (quoting in part
  <em>
   Katz v. United States,
  </em>
  <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U.S. 347, 361</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#516" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507, 516</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L.Ed.2d 576</a></span> (1967) (Harlan, J., concurring));
  <em>
   see also United States v. Owens,
  </em>
  <span class="citation" data-id="463621"><a href="/opinion/463621/united-states-v-merle-ellis-owens/#150" aria-description="Citation for case: United States v. Merle Ellis Owens">782 F.2d 146, 150</a></span> (10th Cir.1986). The “ultimate question” is “whether one’s claim to privacy from government intrusion is reasonable in light of all the surrounding circumstances.”
  <em>
   Rakas,
  </em>
  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#152" aria-description="Citation for case: Rakas v. Illinois">439 U.S. at 152</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#435" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. at 435</a></span> (Powell, J., concurring). Finally, standing is a legal question, and “[wjhere the facts are not in dispute, this court may review the question of standing de novo.”
  <em>
   United States v. Kuespert,
  </em>
  <span class="citation" data-id="458765"><a href="/opinion/458765/united-states-v-lee-a-kuespert/#1067" aria-description="Citation for case: United States v. Lee A. Kuespert">773 F.2d 1066, 1067</a></span> (9th Cir.1985).
 </p>
<p id="b691-14">
  There is no doubt that a corporate officer or employee may assert a reasonable or legitimate expectation of privacy in his corporate office.
  <em>
   Cf. Mancusi v. DeForte,
  </em>
  <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#369" aria-description="Citation for case: Mancusi v. DeForte">392 U.S. 364, 369</a></span>, <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#2124" aria-description="Citation for case: Mancusi v. DeForte">88 S.Ct. 2120, 2124</a></span>, <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">20 L.Ed.2d 1154</a></span> (1968) (“It has long been settled that one has standing to object to a search of his office, as well as of his home.”);
  <em>
   United States v. Lefkowitz,
  </em>
  <span class="citation" data-id="1519992"><a href="/opinion/1519992/united-states-v-lefkowitz/#230" aria-description="Citation for case: United States v. Lefkowitz">464 F.Supp. 227, 230</a></span> (C.D.Cal.1979) (corporate officers
  <span citation-index="1" class="star-pagination" label="596"> 
   *596
   </span>
  had sufficient privacy interest in corporate office suite),
  <em>
   aff'd,
  </em>
  <span class="citation" data-id="376886"><a href="/opinion/376886/united-states-v-albert-m-lefkowitz/" aria-description="Citation for case: United States v. Albert M. Lefkowitz">618 F.2d 1313</a></span> (9th Cir.),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./449/824/">449 U.S. 824</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./101/86/">101 S.Ct. 86</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/66/27/">66 L.Ed.2d 27</a></span> (1980);
  <em>
   see also
  </em>
  4 W. LaFave,
  <em>
   Search and Seizure
  </em>
  § 11.3(d) (2d ed. 1987) [hereinafter LaFave]. Similarly, “it seems clear that a corporate defendant has standing with respect to searches of corporate premises and seizure of corporate records ”
  <em>
   Id.
  </em>
  at 316.
  <em>
   See G.M. Leasing Corp. v. United States,
  </em>
  <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#353" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U.S. 338, 353</a></span>, <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#629" aria-description="Citation for case: G. M. Leasing Corp. v. United States">97 S.Ct. 619, 629</a></span>, <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/" aria-description="Citation for case: G. M. Leasing Corp. v. United States">50 L.Ed.2d 530</a></span> (1977);
  <em>
   Auster Oil &amp; Gas, Inc. v. Stream,
  </em>
  <span class="citation" data-id="8956372"><a href="/opinion/8965067/auster-oil-gas-inc-v-stream/" aria-description="Citation for case: Auster Oil &amp; Gas, Inc. v. Stream">835 F.2d 597</a></span> (5th Cir.1988). In addition, except in rare circumstances, a warrant is as necessary to support a search of commercial premises as private premises.
  <em>
   See Blackie’s House of Beef, Inc. v. Castillo,
  </em>
  <span class="citation" data-id="394830"><a href="/opinion/394830/blackies-house-of-beef-inc-v-leonel-j-castillo-commissioner-of-the/" aria-description="Citation for case: Blackie&#x27;s House of Beef, Inc. v. Leonel J. Castillo,...">659 F.2d 1211</a></span>, 1216 n. 5 (D.C.Cir.1981) (citing
  <em>
   Marshall v. Barlow’s, Inc.,
  </em>
  <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U.S. 307</a></span>, <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">98 S.Ct. 1816</a></span>, <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">56 L.Ed.2d 305</a></span> (1978)),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./455/940/">455 U.S. 940</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./102/1432/">102 S.Ct. 1432</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/71/651/">71 L.Ed.2d 651</a></span> (1982).
 </p>
<p id="b692-4">
  Normally, our inquiry would end here. The government argues, however, that Leary and Kleinberg lack the requisite expectation of privacy in their offices and records because of the regulatory scheme imposed upon exporters by the federal government and the company’s “open door” policy toward government inspectors. For purposes of clarity, we repeat the government’s argument in some detail:
 </p>
<blockquote id="b692-5">
  [T]he government would concede that if it were not for the regulatory scheme requiring that the defendants make, keep and produce the seized records to the government upon request, and the company’s open door policy, both defendants would be able to assert a privacy interest in the seized records under
  <em>
   Rakas v. Illinois,
  </em>
  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U.S. 128</a></span> [<span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. 421</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">58 L.Ed.2d 387</a></span>] (1978).
 </blockquote>
<blockquote id="b692-6">
  The standing argument asserted by the government is limited to the very unusual facts of this case_ [T]he defendants operated in a highly regulated industry where the law required them to make, keep and produce all documents relating in any way to an export. Furthermore, company policy was that the government could come, scheduled or unscheduled and ask for any file or information it needed. Thus, the government’s argument is that any privacy interest in the required records was waived by the company and Mr. Leary.
 </blockquote>
<blockquote id="b692-9">
  Mr. Leary must have known that under these circumstances any company record could be turned over to the government upon request at any time, whether he was present or not, without the government being required to resort to legal process.
 </blockquote>
<blockquote id="b692-10">
  The company’s position is somewhat different, because it could have revoked the policy at any time. But it did not. At the conclusion of the search the President, Frederick L. Kleinberg, invited the agents back to examine any remaining records at a later time.
 </blockquote>
<p id="b692-11">
  Reply Brief of Appellant at 3-5 (citations omitted).
 </p>
<p id="b692-12">
  We find the government’s argument inherently misleading, as it attempts to concede an expectation of privacy with one hand and remove it with the other. Moreover, the argument confuses the law relating to searches or inspections of “regulated” industries with simple recordkeeping requirements.
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  Nevertheless, we will analyze the government’s position in detail. The government’s standing argument consists of two related questions: First, do the regulatory requirements imposed on exporters licensed by the government and Kleinberg’s “open door” policy constitute “circumstances” that render Leary and Kleinberg’s expectation of privacy unreasonable?
  <em>
   See Rakas,
  </em>
  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#152" aria-description="Citation for case: Rakas v. Illinois">439 U.S. at 152</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#435" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. at 435</a></span> (Powell, J., concurring). Second, have Leary and Kleinberg “waived”
  <span citation-index="1" class="star-pagination" label="597"> 
   *597
   </span>
  their fourth amendment rights by participating in a regulated business and by adopting an “open door” policy, inviting government agents to inspect their business records? We address these questions in turn.
 </p>
<p id="b693-4">
  Federal regulations implementing the nation’s export control laws impose comprehensive recordkeeping requirements on exporters. It is clear, however, that licensed exporters retain their fourth amendment rights. The key provision is <span class="citation no-link">15 C.F.R. § 387.13</span>(f)(1) (1987):
 </p>
<blockquote id="b693-5">
  Persons within the United States may be requested to produce records which are required to be kept by any provision of the Export Administration Regulations or by any order, and to make them available for inspection and copying by any authorized agent, official or employee of the International Trade Administration, the U.S. Customs Service, or the U.S. Government, without any charge or expense to such agent, official or employee. The [government] encourage[s] voluntary cooperation with such requests. When voluntary cooperation is not forthcoming, the Office of Export Enforcement and the Office of Antiboycott Compliance are authorized to issue subpoenas for books, records and other writings. In instances where a person does not comply with a subpoena, the Department of Commerce may petition a district court to have the subpoena enforced.
 </blockquote>
<p id="A-K">
  The district court properly analyzed the effect of these requirements:
 </p>
<blockquote id="b693-6">
  The Department of Commerce could have requested inspection and copying of records relating to export at any time, and if the company refused to allow voluntary inspection, the government could have subpoenaed the records. This required procedure affords the protection of judicial review before records can be seized without permission.... The fact that a warrant is required for a full-scale criminal search and seizure of records required to be kept recognizes the fourth amendment’s protection of privacy even in these circumstances and restrictions on the government’s power to intrude on that privacy.
 </blockquote>
<p id="b693-11">
  Mem. Opinion at 4.
  <em>
   Cf. United States v. Molt,
  </em>
  <span class="citation" data-id="2149373"><a href="/opinion/2149373/united-states-v-molt/" aria-description="Citation for case: United States v. Molt">444 F.Supp. 491</a></span> (E.D.Pa.),
  <em>
   aff'd,
  </em>
  <span class="citation" data-id="9465383"><a href="/opinion/362453/united-states-v-henry-a-molt-jr/" aria-description="Citation for case: United States v. Henry A. Molt, Jr">589 F.2d 1247</a></span> (3d Cir.1978);
  <em>
   see also Railway Labor Executives’ Ass’n v. Burnley,
  </em>
  <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#584" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley">839 F.2d 575, 584</a></span> (9th Cir.1988) (“When no ... plan [authorizing warrantless inspections] is built into the legislation regulating a specific industry, the [Supreme] Court has required a warrant as a condition of a reasonable search.”);
  <em>
   Serpas v. Schmidt,
  </em>
  <span class="citation" data-id="9476620"><a href="/opinion/493275/don-serpas-raymond-johnson-and-carl-waters-individually-and-on-behalf-of/#28" aria-description="Citation for case: Don Serpas, Raymond Johnson and Carl Waters, Individually...">827 F.2d 23, 28</a></span> (7th Cir.1987) (“[A] history of pervasive regulation of an industry is not by itself enough to render the warrant requirement superfluous_ [T]he Supreme Court has sanctioned warrantless searches of commercial premises in certain industries subject to longstanding governmental oversight.... [however] [i]n each of these cases, ... Congress expressly authorized the terms and conditions of searches on specified premises.”),
  <em>
   cert. denied,
  </em>
  — U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./108/1075/">108 S.Ct. 1075</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/99/234/">99 L.Ed.2d 234</a></span> (1988). Neither the export regulations nor the export statutes authorize a warrantless search and seizure of business records,
  <em>
   see
  </em>
  <span class="citation no-link">22 U.S.C. § 2778</span>(e); 50 U.S.C.App. § 2411; Brief of Appellant at 14, yet the government would have us hold that the regulatory scheme negates the licensed exporter’s right to challenge an invalid warrant. In other words, the government concedes that it must obtain a warrant but argues that it need not obtain a valid warrant. We refuse to adopt this reasoning.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
</p>
<p id="b694-3">
<span citation-index="1" class="star-pagination" label="598"> 
   *598
   </span>
  Similarly, the company’s “open door” policy does not negate the defendants’ expectation of privacy. There is a distinction of constitutional significance between the company’s policy, which invited government agents to “visit ... and ask for any file or information they want or need,” and a thorough search of the offices and seizure and removal of twenty boxes of files, including personal records and documents unrelated to the company’s regulated export activities. Leary and Kleinberg retained control over the premises and records and had the authority to restrict the government’s access by the terms of the policy. In sum, we find a reasonable expectation of privacy in these circumstances.
 </p>
<p id="b694-4">
  For substantially the same reasons, we reject the government’s argument that Leary and Kleinberg either waived their fourth amendment rights or consented to the search. When evaluating fourth amendment rights, there is no clear distinction between “consent” to a search and a “waiver” of one’s privacy interest. The government, however, attempts to draw a distinction in this case, that is, that Leary and Kleinberg either “consented” to the August 23 search, or evidenced an ongoing consent to be searched at any time (a “waiver”).
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  Despite the government’s effort to cast this inquiry as one of waiver, the proper analysis focuses on consent. In fact, the Supreme Court has expressly rejected the use of “waiver” analysis in fourth amendment cases in favor of a “voluntary consent” test.
  <em>
   See Schneckloth v. Bustamonte,
  </em>
  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#235" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218, 235-46</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#2052" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041, 2052-57</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L.Ed.2d 854</a></span> (1973). Thus, to determine whether, by granting any ongoing consent, Leary and Kleinberg effectively “waived” their fourth amendment rights, our analysis is guided by the law developed for analyzing “consent” searches.
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
</p>
<p id="b694-9">
  Initially, we reject any suggestion that Leary and Kleinberg specifically consented to the August 23, 1984 search. When a government agent claims authority to search under a warrant, “he announces in effect that the occupant has no right to resist the search. The situation is instinct with coercion — albeit colorably lawful coercion. Where there is coercion there cannot be consent.”
  <em>
   Bumper v. North Carolina,
  </em>
  <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#550" aria-description="Citation for case: Bumper v. North Carolina">391 U.S. 543, 550</a></span>, <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#1792" aria-description="Citation for case: Bumper v. North Carolina">88 S.Ct. 1788, 1792</a></span>, <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">20 L.Ed.2d 797</a></span> (1968). In fact, the Supreme Court has stated that: “A search conducted in reliance upon a warrant cannot later be justified on the basis of consent if it turns out that the warrant was invalid.”
  <em>
   Bumper,
  </em>
  <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#549" aria-description="Citation for case: Bumper v. North Carolina">391 U.S. at 549</a></span>, <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#1792" aria-description="Citation for case: Bumper v. North Carolina">88 S.Ct. at 1792</a></span>.
  <a class="footnote" href="#fn9" id="fn9_ref">
   9
  </a>
</p>
<p id="b695-3">
<span citation-index="1" class="star-pagination" label="599"> 
   *599
   </span>
  Similarly, we find no evidence that Leary and Kleinberg granted an ongoing consent to searches by Customs officers. We recently addressed the question of consent in detail, recognizing that the Supreme Court requires that “consent to a Fourth Amendment search must be voluntary
  <em>
   in fact
  </em>
  and free of coercion under the totality of the circumstances....”
  <em>
   United States v. Carson,
  </em>
  <span class="citation" data-id="9475015"><a href="/opinion/471869/united-states-v-george-l-carson/#1150" aria-description="Citation for case: United States v. George L. Carson">793 F.2d 1141, 1150</a></span> (10th Cir.) (citing
  <em>
   Schneckloth,
  </em>
  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#248" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. at 248-49</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#2058" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. at 2058-59</a></span>) (emphasis in original),
  <em>
   cert. denied,
  </em>
  — U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./107/315/">107 S.Ct. 315</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.%202d/93/289/">93 L.Ed. 2d 289</a></span> (1986). In addition, we have noted that consent “is a question of fact to be determined from the totality of all the circumstances [and] [t]he Government has the burden of proving that consent was given freely and voluntarily.”
  <em>
   United States v. Recalde,
  </em>
  <span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1453" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d 1448, 1453</a></span> (10th Cir.1985) (citations omitted).
  <a class="footnote" href="#fn10" id="fn10_ref">
   10
  </a>
</p>
<p id="b695-5">
  There is no evidence that Kleinberg and Leary granted an ongoing consent to the search of their offices or records by participating in a regulated activity. The federal recordkeeping regulations leave exporters with a substantial privacy interest. Government agents may be required to resort to judicial process to obtain desired records. Absent a statutory scheme authorizing warrantless searches, there is no waiver of constitutional rights in the mere fact that Leary and Kleinberg chose to participate in an activity regulated and licensed by the government.
  <em>
   See Marshall v. Barlow’s Inc.,
  </em>
  <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U.S. 307, 312-14, 323-24</a></span>, <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#1820" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">98 S.Ct. 1816, 1820-21, 1826</a></span>, <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">56 L.Ed.2d 305</a></span> (1978).
 </p>
<p id="b695-6">
  Nor do we find any ongoing consent in the company’s “open door” policy. As we noted earlier, Kleinberg did not invite the government to rummage through company files and carry out any documents that the agents found interesting. Equally important is the fact that “[w]hen the basis for a search or seizure is consent, the government must conform to the limitations placed upon the right granted to search, seize or retain the papers or effects.”
  <em>
   Mason v. Pulliam,
  </em>
  <span class="citation" data-id="9463909"><a href="/opinion/346767/harve-d-mason-and-pat-j-mason-v-ralph-j-pulliam-special/#429" aria-description="Citation for case: Harve D. Mason and Pat J. Mason v. Ralph J. Pulliam...">557 F.2d 426, 429</a></span> (5th Cir.1977);
  <em>
   see also United States v. Gay,
  </em>
  <span class="citation" data-id="458949"><a href="/opinion/458949/united-states-v-thomas-norman-gay/#377" aria-description="Citation for case: United States v. Thomas Norman Gay">774 F.2d 368, 377</a></span> (10th Cir.1985) (“The scope of a consent search is limited by the breadth of the actual consent itself.”);
  <em>
   United States v. Milian-Rodriguez,
  </em>
  <span class="citation" data-id="450796"><a href="/opinion/450796/united-states-v-ramon-milian-rodriguez/#1563" aria-description="Citation for case: United States v. Ramon Milian-Rodriguez">759 F.2d 1558, 1563</a></span> (11th Cir.) (“the government may not use consent to a search which was initially described as narrow as license to conduct a general search”),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./474/845/">474 U.S. 845</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./106/135/">106 S.Ct. 135</a></span>, <span class="citation" data-id="9049585"><a href="/opinion/9056060/kabanuk-v-minnesota/" aria-description="Citation for case: Kabanuk v. Minnesota">88 L.Ed.2d 112</a></span> (1985). Even if Kleinberg’s policy can be characterized as an ongoing consent to government searches, the government exceeded the scope of that consent in two respects. First, Kleinberg invited government agents to inspect and copy records, not seize them. Second, Kleinberg’s invitation extended only to those documents related to regulated export activities. The government searched and seized records dealing with Leary’s personal and financial affairs and business activities unrelated to exports.
 </p>
<p id="b695-10">
  In addition, we find a compelling policy reason to reject the government’s argument. As the regulations indicate, the government encourages voluntary cooperation with requests for export documents and information. Yet the government urges us to find that Kleinberg’s voluntary cooperation has resulted in a waiver of fourth amendment rights.
  <a class="footnote" href="#fn11" id="fn11_ref">
   11
  </a>
  This interpre
  <span citation-index="1" class="star-pagination" label="600"> 
   *600
   </span>
  tation of the law would deliver a serious blow to the government’s “voluntary cooperation” efforts and discourage “open door” policies in the export industry.
 </p>
<p id="b696-4">
  Accordingly, we find no consent or “waiver” and conclude that both Leary and Kleinberg have had their fourth amendment rights infringed by this search and seizure and may seek suppression of the evidence. We proceed to review the adequacy of the search warrant.
 </p>
<p id="b696-5">
  III. Particularity
 </p>
<p id="b696-6">
  The fourth amendment requires that warrants “particularly describ[e] ... the persons or things to be seized.” U.S. Const, amend. IV. This requirement prevents a “general, exploratory rummaging in a person’s belongings,”
  <em>
   Coolidge v. New Hampshire,
  </em>
  <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#467" aria-description="Citation for case: Coolidge v. New Hampshire">403 U.S. 443, 467</a></span>, <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#2038" aria-description="Citation for case: Coolidge v. New Hampshire">91 S.Ct. 2022, 2038</a></span>, <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">29 L.Ed.2d 564</a></span> (1971) and “ ‘makes general searches ... impossible and prevents the seizure of one thing under a warrant describing another. As to what is be taken, nothing is left to the discretion of the officer executing the warrant.’ ”
  <em>
   Stanford v. Texas,
  </em>
  <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas">379 U.S. 476, 485</a></span>, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#511" aria-description="Citation for case: Stanford v. Texas">85 S.Ct. 506, 511</a></span>, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">13 L.Ed.2d 431</a></span> (1965) (quoting Ma
  <em>
   rron v. United States, 275
  </em>
  U.S. 192, 196, <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#76" aria-description="Citation for case: Marron v. United States">48 S.Ct. 74, 76</a></span>, <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">72 L.Ed. 231</a></span> (1927)).
  <em>
   See Andresen v. Maryland,
  </em>
  <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#480" aria-description="Citation for case: Andresen v. Maryland">427 U.S. 463, 480</a></span>, <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#2748" aria-description="Citation for case: Andresen v. Maryland">96 S.Ct. 2737, 2748</a></span>, <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">49 L.Ed.2d 627</a></span> (1976);
  <em>
   United States v. Medlin,
  </em>
  <span class="citation" data-id="503533"><a href="/opinion/503533/united-states-v-arvle-edgar-medlin/#1199" aria-description="Citation for case: United States v. Arvle Edgar Medlin">842 F.2d 1194, 1199</a></span> (10th Cir.1988);
  <em>
   Voss v. Bergsgaard,
  </em>
  <span class="citation" data-id="8935318"><a href="/opinion/8944758/voss-v-bergsgaard/#404" aria-description="Citation for case: Voss v. Bergsgaard">774 F.2d 402, 404</a></span> (10th Cir.1985). “The particularity requirement [also] ensures that a search is confined in scope to particularly described evidence relating to a specific crime for which there is demonstrated probable cause.”
  <em>
   Voss,
  </em>
  <span class="citation" data-id="8935318"><a href="/opinion/8944758/voss-v-bergsgaard/#404" aria-description="Citation for case: Voss v. Bergsgaard">774 F.2d at 404</a></span>.
 </p>
<p id="b696-7">
  The test applied to the description of the items to be seized is a practical one. “ ‘A description is sufficiently particular when it enables the searcher to reasonably ascertain and identify the things authorized to be seized.’ ”
  <em>
   United States v. Wolfenbarger,
  </em>
  <span class="citation" data-id="412106"><a href="/opinion/412106/united-states-v-john-q-wolfenbarger/#752" aria-description="Citation for case: United States v. John Q. Wolfenbarger">696 F.2d 750, 752</a></span> (10th Cir.1982) (quoting
  <em>
   United States v. Wuagneux,
  </em>
  <span class="citation" data-id="406519"><a href="/opinion/406519/united-states-v-george-wuagneux/#1348" aria-description="Citation for case: United States v. George Wuagneux">683 F.2d 1343, 1348</a></span> (11th Cir.1982)).
  <a class="footnote" href="#fn12" id="fn12_ref">
   12
  </a>
  Even a warrant that describes the items to be seized in broad or generic terms may be valid “when the description is as specific as the circumstances and the nature of the activity under investigation permit.”
  <em>
   United States v. Santarelli,
  </em>
  <span class="citation" data-id="461431"><a href="/opinion/461431/united-states-v-dominic-santarelli/#614" aria-description="Citation for case: United States v. Dominic Santarelli">778 F.2d 609, 614</a></span> (11th Cir.1985);
  <em>
   see United States v. Strand,
  </em>
  <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/#453" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers">761 F.2d 449, 453</a></span> (8th Cir.1985) (“degree of specificity required necessarily depends upon the circumstances of each particular case”). However, the fourth amendment requires that the government describe the items to be seized with as much specificity as the government’s knowledge and circumstances allow, and “warrants are conclusively invalidated by their substantial failure to specify as nearly as possible the distinguishing characteristics of the goods to be seized.”
  <em>
   United States v. Fuccillo,
  </em>
  <span class="citation" data-id="480985"><a href="/opinion/480985/united-states-v-carl-a-fuccillo/#176" aria-description="Citation for case: United States v. Carl A. Fuccillo">808 F.2d 173, 176</a></span> (1st Cir.),
  <em>
   cert. denied,
  </em>
  — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./107/2481/">107 S.Ct. 2481</a></span>, <span class="citation no-link">96 L.Ed.2d 374</span> (1987).
 </p>
<p id="b696-13">
  The district court found the Kleinberg warrant overbroad. That legal conclusion is subject to
  <em>
   de novo
  </em>
  review on appeal.
  <em>
   See United States v. Fannin,
  </em>
  <span class="citation" data-id="487817"><a href="/opinion/487817/united-states-v-john-fannin/#1381" aria-description="Citation for case: United States v. John Fannin">817 F.2d 1379, 1381</a></span> (9th Cir.1987);
  <em>
   United States v. Spilotro,
  </em>
  <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/#963" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and...">800 F.2d 959, 963</a></span> (9th Cir.1986). Therefore, our task is to determine if the language of the Kleinberg warrant is sufficiently particular to achieve the requirements of the fourth amendment.
 </p>
<p id="b696-14">
  The warrant under scrutiny here included only two limitations. First, the documents to be seized had to fall within a long list of business records typical of the documents kept by an export company. Second, those documents had to relate to
  <span citation-index="1" class="star-pagination" label="601"> 
   *601
   </span>
  “the purchase, sale and illegal exportation of materials in violation of the” federal export laws. In this context — the search of the offices of an export company — these limitations provide no limitation at all. The warrant authorizes, and the customs agents conducted, a general search of the Kleinberg offices.
  <a class="footnote" href="#fn13" id="fn13_ref">
   13
  </a>
</p>
<p id="b697-4">
  A.
  <em>
   The warrant is facially overbroad.
  </em>
</p>
<p id="b697-5">
  The Kleinberg warrant suffers from three flaws. First, it authorizes a general search in conjunction with a federal crime and is overbroad on its face. In Foss
  <em>
   v. Bergsgaard,
  </em>
  <span class="citation" data-id="8935318"><a href="/opinion/8944758/voss-v-bergsgaard/" aria-description="Citation for case: Voss v. Bergsgaard">774 F.2d 402</a></span> (10th Cir.1985), we invalidated a similar warrant. The warrant in Foss authorized government agents to seize documents and records “[a]ll of which are evidence of violations of Title <span class="citation no-link">18, United States Code, Section 371</span>.”
  <span class="citation no-link"><em>
   Id.
  </em>
  at 405</span>. We concluded that “[e]ven if the reference to Section 371 [the federal conspiracy statute] is construed as a limitation, it does not constitute a constitutionally adequate particularization of the items to be seized.”
  <em>
   <span class="citation no-link">Id.</span>
  </em>
<a class="footnote" href="#fn14" id="fn14_ref">
<em>
    14
   </em>
</a>
</p>
<p id="b697-10">
  The government argues that
  <em>
   <span class="citation" data-id="8935318"><a href="/opinion/8944758/voss-v-bergsgaard/" aria-description="Citation for case: Voss v. Bergsgaard">Voss</a></span>
  </em>
  does not apply here because the export statutes describe a much narrower range of criminal activity. We disagree. While some federal statutes may be narrow enough to meet the fourth amendment’s requirement, the two statutes cited by the Kleinberg warrant cover a broad range of activity and the reference to those statutes does not sufficiently limit the scope of the warrant.
  <a class="footnote" href="#fn15" id="fn15_ref">
   15
  </a>
</p>
<p id="b697-11">
  Moreover, a series of decisions from other circuits have held that reference to a broad federal statute is not a sufficient limitation on a search warrant. For example, in
  <em>
   Roche v. United States,
  </em>
  <span class="citation" data-id="373913"><a href="/opinion/373913/united-states-v-john-c-roche/#7" aria-description="Citation for case: United States v. John C. Roche">614 F.2d 6, 7</a></span> (1st Cir.1980) the warrant authorized the seizure of books, records and documents “which are evidence, fruits, and instrumen-talities of the violation of Title <span class="citation no-link">18, United States Code Section 1341</span> [mail fraud].” The court found this limitation to be “no
  <span citation-index="1" class="star-pagination" label="602"> 
   *602
   </span>
  limitation at all.”
  <span class="citation no-link"><em>
   Id.
  </em>
  at 8</span>. The Ninth Circuit has consistently applied the same rule. In
  <em>
   United States v. Cardwell,
  </em>
  <span class="citation" data-id="405042"><a href="/opinion/405042/united-states-v-james-b-cardwell-united-states-of-america-v-marvin/#77" aria-description="Citation for case: United States v. James B. Cardwell, United States of...">680 F.2d 75, 77</a></span> (9th Cir.1982), “[t]he only limitation on the search and seizure of appellants’ business papers was the requirement that they be the instrumentality or evidence of violation of the general tax evasion statute, <span class="citation no-link">26 U.S.C. § 7201</span>. That is not enough.” The court’s reasoning in
  <em>
   Card-well
  </em>
  is equally applicable here:
 </p>
<blockquote id="b698-4">
  “ ‘[Limiting’ the search to only records that are evidence of the violation of a certain statute is generally not enough.... If items that are illegal, fraudulent, or evidence of illegality are sought, the warrant must contain some guidelines to aid the determination of what may or may not be seized.”
 </blockquote>
<p id="b698-5">
<span class="citation no-link"><em>
   Id.
  </em>
  at 78</span>. Where the warrant provides no such guidelines, it is impermissibly over-broad on its face.
  <em>
   See also Rickert v. Sweeney,
  </em>
  <span class="citation" data-id="8949178"><a href="/opinion/8958115/rickert-v-sweeney/#909" aria-description="Citation for case: Rickert v. Sweeney">813 F.2d 907, 909</a></span> (8th Cir.1987) (warrant limited only by references to the general conspiracy statute and general tax evasion statute did “not limit the search in any substantive manner”);
  <em>
   United States v. Spilotro,
  </em>
  <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/#965" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and...">800 F.2d 959, 965</a></span> (9th Cir.1986) (“effort to limit discretion solely by reference to criminal statutes was inadequate”);
  <em>
   United States v. Abrams,
  </em>
  <span class="citation" data-id="9842939"><a href="/opinion/374752/united-states-v-maurice-abrams/#542" aria-description="Citation for case: United States v. Maurice Abrams">615 F.2d 541, 542-43</a></span> (1st Cir.1980) (warrant limited only by reference to records and federal fraud statute is overbroad); In re
  <em>
   Lafayette Academy,
  </em>
  <span class="citation" data-id="9466280"><a href="/opinion/371945/in-the-matter-of-the-application-of-lafayette-academy-inc-appeal-of/#3" aria-description="Citation for case: In the Matter of the Application of Lafayette Academy,...">610 F.2d 1, 3</a></span> (1st Cir.1979) (over-broad warrant allowed “seizure of most every sort of book or paper ... limited only by the qualification that the seized item be evidence of violations of ... ‘18 U.S.C. 286, 287, 371, 1001 and 1014.’ ”).
 </p>
<p id="b698-9">
  We agree with the reasoning of these courts. As an irreducible minimum, a proper warrant must allow the executing officers to distinguish between items that may and may not be seized.
  <a class="footnote" href="#fn16" id="fn16_ref">
   16
  </a>
<em>
   See
  </em>
  2 La-Fave, § 4.6(a), at 235-36. The Kleinberg warrant does not provide that guidance. An unadorned reference to a broad federal statute does not sufficiently limit the scope of a search warrant. Absent other limiting factors, such a warrant does not comply with the requirements of the fourth amendment.
  <a class="footnote" href="#fn17" id="fn17_ref">
   17
  </a>
<em>
   See Andresen v. Maryland,
  </em>
  <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#480" aria-description="Citation for case: Andresen v. Maryland">427 U.S. 463, 480-82</a></span>, <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#2748" aria-description="Citation for case: Andresen v. Maryland">96 S.Ct. 2737, 2748-49</a></span>, <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">49 L.Ed.2d 627</a></span> (1976).
 </p>
<p id="b698-10">
  Nor did the list of business records to be seized provide any meaningful limitation on the Kleinberg search. The warrant encompassed virtually every document that one might expect to find in a modem export company’s office. Again, the fourth amendment requires more.
  <em>
   See Id.; see also In re Grand Jury Proceedings (Young),
  </em>
  <span class="citation" data-id="9471119"><a href="/opinion/424091/in-re-grand-jury-proceedings-appeal-of-robert-e-young/#498" aria-description="Citation for case: In Re Grand Jury Proceedings. Appeal of Robert E. Young">716 F.2d 493, 498</a></span> (8th Cir.1983) (“laundry list of various type of records is insufficient to save the search warrant”);
  <em>
   Roberts v. United States,
  </em>
  <span class="citation" data-id="1394599"><a href="/opinion/1394599/roberts-v-united-states/#934" aria-description="Citation for case: Roberts v. United States">656 F.Supp. 929, 934</a></span> (S.D.N.Y.1987) (“By listing every type
  <span citation-index="1" class="star-pagination" label="603"> 
   *603
   </span>
  of record that could conceivably be found in an office, the warrant effectively authorized the inspectors to cart away anything that they could find on the premises.”);
  <em>
   cf. Cardwell,
  </em>
  <span class="citation" data-id="405042"><a href="/opinion/405042/united-states-v-james-b-cardwell-united-states-of-america-v-marvin/#78" aria-description="Citation for case: United States v. James B. Cardwell, United States of...">680 F.2d at 78</a></span>;
  <em>
   Abrams,
  </em>
  <span class="citation" data-id="9842939"><a href="/opinion/374752/united-states-v-maurice-abrams/#543" aria-description="Citation for case: United States v. Maurice Abrams">615 F.2d at 543</a></span>;
  <em>
   Roche,
  </em>
  <span class="citation" data-id="373913"><a href="/opinion/373913/united-states-v-john-c-roche/#7" aria-description="Citation for case: United States v. John C. Roche">614 F.2d at 7</a></span>;
  <em>
   Lafayette Academy,
  </em>
  <span class="citation" data-id="9466280"><a href="/opinion/371945/in-the-matter-of-the-application-of-lafayette-academy-inc-appeal-of/#5" aria-description="Citation for case: In the Matter of the Application of Lafayette Academy,...">610 F.2d at 5</a></span>.
 </p>
<p id="b699-4">
  We recognize that some lower courts have found similar warrants to be sufficiently particular. The government relies on
  <em>
   United States v. Moller-Butcher,
  </em>
  <span class="citation" data-id="1482053"><a href="/opinion/1482053/united-states-v-moller-butcher/#557" aria-description="Citation for case: United States v. Moller-Butcher">560 F.Supp. 550, 557</a></span> (D.Mass.1983) where the district court found a warrant seeking “records which are required under the Export Administration Act, <span class="citation no-link">15 C.F.R. § 387.13</span>, by all businesses sending electronic equipment outside the United States” to be sufficiently particular. The district court in
  <em>
   United States v. Gregg,
  </em>
  <span class="citation" data-id="1577597"><a href="/opinion/1577597/united-states-v-gregg/#966" aria-description="Citation for case: United States v. Gregg">629 F.Supp. 958, 966-67</a></span> (W.D.No.1986),
  <em>
   aff'd
  </em>
  <span class="citation" data-id="495037"><a href="/opinion/495037/united-states-v-werner-ernst-gregg-and-roswitha-gregg/" aria-description="Citation for case: United States v. Werner Ernst Gregg and Roswitha Gregg">829 F.2d 1430</a></span> (8th Cir.1987), approved a similar warrant. We are unpersuaded by these decisions. Neither court clearly explained why the warrant in question is sufficient; the analysis is brief and concluso-ry.
  <a class="footnote" href="#fn18" id="fn18_ref">
   18
  </a>
  Moreover, there are distinguishing features that limit the value of these decisions in our present inquiry.
  <a class="footnote" href="#fn19" id="fn19_ref">
   19
  </a>
</p>
<p id="b699-5">
  The government also argues that the facial overbreadth of the warrant is not fatal because any doubts about what was to be seized “could be resolved by resort to the affidavit which was a part of the warrant and which the agents had with them at the location of the search.” Brief of Appellant at 38. We disagree. It is true that the particularity of an affidavit may cure an overbroad warrant, but only “where the affidavit and the search warrant ... can be reasonably said to constitute one document. Two requirements must be satisfied to reach this result: first, the affidavit and search warrant must be physically connected so that they constitute one document; and second, the search warrant must expressly refer to the affidavit and incorporate it by reference using suitable words of reference.” 2 LaFave, § 4.6(a), at 241 (quoting
  <em>
   Bloom v. State,
  </em>
  <span class="citation" data-id="1876547"><a href="/opinion/1876547/bloom-v-state/" aria-description="Citation for case: Bloom v. State">283 So.2d 134</a></span> (Fla.App.1973));
  <em>
   see <span class="citation" data-id="1876547"><a href="/opinion/1876547/bloom-v-state/" aria-description="Citation for case: Bloom v. State">Id.</a></span>
  </em>
  cases cited at n. 28; 3 C. Wright,
  <em>
   Federal Practice and Procedure
  </em>
  § 670, at 723 (2d ed. 1982);
  <em>
   United States v. Medlin,
  </em>
  <span class="citation" data-id="474635"><a href="/opinion/474635/united-states-v-arvle-edgar-medlin/" aria-description="Citation for case: United States v. Arvle Edgar Medlin">798 F.2d 407</a></span>, 410 n. 1 (10th Cir.1986) (“When an affidavit is
  <em>
   attached
  </em>
  to a warrant and incorporated by reference into the warrant, it can be used to cure a lack of particularity.”);
  <a class="footnote" href="#fn20" id="fn20_ref">
   20
  </a>
<em>
   United States v. Hayes,
  </em>
  <span class="citation" data-id="9475068"><a href="/opinion/472649/united-states-v-jude-r-hayes/#1354" aria-description="Citation for case: United States v. Jude R. Hayes">794 F.2d 1348, 1354</a></span> (9th Cir.1986),
  <em>
   cert. denied,
  </em>
  — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./107/1289/">107 S.Ct. 1289</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/94/146/">94 L.Ed.2d 146</a></span> (1987) (affidavits did not accompany warrant);
  <em>
   United States v. Strand,
  </em>
  <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/#453" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers">761 F.2d 449, 453</a></span> (8th Cir.1985) (affidavit accompanied warrant but was not incorporated).
 </p>
<p id="b699-11">
  The Kleinberg warrant did not incorporate the affidavit; there is no reference to the affidavit on the face of the warrant. In addition, there is no clear evidence in the record to support the government’s assertion that the affidavit “was a part of the warrant.” Finally, and perhaps most importantly, the search itself was not limited by the affidavit. If the affidavit was available to the agents searching the Kleinberg
  <span citation-index="1" class="star-pagination" label="604"> 
   *604
   </span>
  offices, it certainly was not used to limit the search.
  <a class="footnote" href="#fn21" id="fn21_ref">
   21
  </a>
  The agents seized documents related to transactions, countries and commodities not mentioned in the affidavit. In fact, the agents seized documents unrelated to Kleinberg’s export business.
  <a class="footnote" href="#fn22" id="fn22_ref">
   22
  </a>
  Even if the technical requirements for incorporation were met, it would be improper to allow the affidavit to cure the lack of particularity in the warrant where the government agents relied on the breadth of the warrant, not the specificity of the affidavit, to define the scope of the search.
  <em>
   Cf. United States v. Spilotro,
  </em>
  <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/#967" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and...">800 F.2d 959, 967</a></span> (9th Cir.1986) (“government’s argument that the agents were somehow constructively guided by the affidavit in executing the warrants is unpersuasive”);
  <em>
   Lafayette Academy,
  </em>
  <span class="citation" data-id="9466280"><a href="/opinion/371945/in-the-matter-of-the-application-of-lafayette-academy-inc-appeal-of/#5" aria-description="Citation for case: In the Matter of the Application of Lafayette Academy,...">610 F.2d at 5</a></span> (“[S]elf-restraint on the part of the ... executing officers does not erase the fact that under the broadly worded warrant appellees were subject to a greater exercise of power than that which may have actually transpired and for which probable cause had been established. The particularity requirement is a check to just this sort of risk.” (citations omitted)).
 </p>
<p id="b700-4">
  B.
  <em>
   Information was available to make the warrant more particular.
  </em>
</p>
<p id="b700-5">
  In addition to being overbroad on its face, the Kleinberg warrant is flawed because information was available to the government to make the description of the items to be seized much more particular. Admittedly, a general description is not always invalid.
 </p>
<blockquote id="b700-9">
  “Courts tend to tolerate a greater degree of ambiguity [in the warrant’s description] where law enforcement agents have done the best that could reasonably be expected under the circumstances, have acquired all the descriptive facts which a reasonable investigation could be expected to cover, and have insured that all those facts were included in the warrant.”
 </blockquote>
<p id="b700-10">
<em>
   United States v. Young,
  </em>
  <span class="citation" data-id="8925220"><a href="/opinion/8934968/united-states-v-young/#759" aria-description="Citation for case: United States v. Young">745 F.2d 733, 759</a></span> (2d Cir.1984),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./470/1084/">470 U.S. 1084</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./105/1842/">105 S.Ct. 1842</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/85/142/">85 L.Ed.2d 142</a></span> (1985). In this case, however, the government’s argument that the warrant was “as specific as the circumstances and the nature of the activity under investigation permit” is untenable. Agent Juhasz’ affidavit in support of the warrant was very specific, alleging the attempted illegal export of a specific product to the People’s Republic of China via a series of specific companies in Hong Kong. Yet none of this information was reflected in the warrant. The warrant could have been limited to documents related to the Micro-tel transaction, to the companies suspected of participating in the illegal export, to the countries involved in the route of the export, Hong Kong and China, or to a specific period of time coincident to the suspect transaction. Yet the government chose to include none of these limiting factors. As the Ninth Circuit found in
  <em>
   <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and...">Spilotro</a></span>,
  </em>
</p>
<blockquote id="b701-3">
<span citation-index="1" class="star-pagination" label="605"> 
   *605
   </span>
  “[T]he government could have narrowed most of the descriptions in the warrants either by describing in greater detail the items one commonly expects to find on premises used for the criminal activities in question, or at the very least, by describing the criminal activities themselves rather than simply referring to the statute believed to have been violated. As the warrants stand, however, they authorize wholesale seizures of entire categories of items not generally evidence of criminal activity, and provide no guidelines to distinguish items used lawfully from those the government had probable cause to seize.”
 </blockquote>
<p id="b701-4">
<em>
   Spilotro,
  </em>
  <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/#964" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and...">800 F.2d at 964</a></span>;
  <em>
   see also United States v. Fuccillo,
  </em>
  <span class="citation" data-id="480985"><a href="/opinion/480985/united-states-v-carl-a-fuccillo/#176" aria-description="Citation for case: United States v. Carl A. Fuccillo">808 F.2d 173, 176</a></span> (1st Cir.) (“ ‘In light of the information available to the agents which could have served to narrow the scope of the warrant and protect the defendants’ personal rights, the warrant was inadequate.’ ”) (quoting
  <em>
   United States v. Klein,
  </em>
  <span class="citation" data-id="9464268"><a href="/opinion/350518/united-states-v-allan-michael-klein/#190" aria-description="Citation for case: United States v. Allan Michael Klein">565 F.2d 183, 190</a></span> (1st Cir.1977)),
  <em>
   cert. denied,
  </em>
  — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./107/2481/">107 S.Ct. 2481</a></span>, <span class="citation no-link">96 L.Ed.2d 374</span> (1987);
  <em>
   United States v. Cook,
  </em>
  <span class="citation" data-id="393709"><a href="/opinion/393709/united-states-v-lee-cook-and-jackie-b-kirk/#733" aria-description="Citation for case: United States v. Lee Cook and Jackie B. Kirk">657 F.2d 730, 733</a></span> (5th Cir. Unit A Sept.1981) (“Failure to employ the specificity available will invalidate a general description in a warrant.”).
 </p>
<p id="b701-7">
  C.
  <em>
   The scope of the warrant exceeded the probable cause.
  </em>
</p>
<p id="b701-8">
  The final factor leading us to conclude that the Kleinberg warrant was impermissibly overbroad is that even if we assume that Agent Juhasz’ affidavit established probable cause to issue a search warrant, the scope of the warrant far exceeded the probable cause to support it. The fourth amendment requires not only that the warrant sufficiently specify the evidence to be seized, but also that the scope of the warrant be limited to the specific areas and things for which there is probable cause to search.
  <em>
   Maryland v. Garrison,
  </em>
  <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/" aria-description="Citation for case: Maryland v. Garrison">480 U.S. 79</a></span>, <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#1017" aria-description="Citation for case: Maryland v. Garrison">107 S.Ct. 1013, 1017</a></span>, <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/" aria-description="Citation for case: Maryland v. Garrison">94 L.Ed.2d 72</a></span> (1987). “An otherwise unobjectionable description of the objects to be seized is defective if it is broader than can be justified by the probable cause upon which the warrant is based.” 2 LaFave, § 4.6(a), at 236;
  <em>
   see United States v. Bentley,
  </em>
  <span class="citation" data-id="492430"><a href="/opinion/492430/united-states-v-david-bentley-richard-degen-allen-yung-and-walter/#1110" aria-description="Citation for case: United States v. David Bentley, Richard Degen, Allen...">825 F.2d 1104, 1110</a></span> (7th Cir.) (“When the probable cause covers fewer documents in a system of files, the warrant must ... tell the officers how to separate the documents to be seized from others.”),
  <em>
   cert. denied,
  </em>
  — U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./108/240/">108 S.Ct. 240</a></span>, <span class="citation no-link">98 L.Ed.2d 198</span> (1987);
  <em>
   Rickert v. Sweeney,
  </em>
  <span class="citation" data-id="8949178"><a href="/opinion/8958115/rickert-v-sweeney/#909" aria-description="Citation for case: Rickert v. Sweeney">813 F.2d 907, 909</a></span> (8th Cir.1987) (“Although probable cause existed to search the records of one particular project, the warrant failed to so limit the search.”);
  <em>
   Spilo-tro,
  </em>
  <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/#967" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and...">800 F.2d at 967</a></span> (list of criminal statutes in warrant went beyond probable cause in affidavit);
  <em>
   Voss,
  </em>
  <span class="citation" data-id="8935318"><a href="/opinion/8944758/voss-v-bergsgaard/#408" aria-description="Citation for case: Voss v. Bergsgaard">774 F.2d at 408</a></span> (Logan, J., concurring) (“The breadth of a warrant must be justified by the breadth of the probable cause.”);
  <em>
   cf. VonderAhe v. Howland,
  </em>
  <span class="citation" data-id="9461326"><a href="/opinion/324061/donn-vonderahe-and-barbara-vonderahe-v-roy-h-howland/#369" aria-description="Citation for case: Donn Vonderahe and Barbara Vonderahe v. Roy H. Howland">508 F.2d 364, 369</a></span> (9th Cir.1974) (“[Ajlthough there may have been ‘probable cause’ to search for and seize [records of a certain type and date] there was no probable cause shown for a seizure of all the ... books and records, or ... personal and private papers.”) In other words, a search warrant is also impermissibly over-broad if it authorizes the search and seizure of evidence that is not supported by probable cause. A generous reading of the affidavit may disclose probable cause for a search of the Kleinberg offices limited to documentary evidence of transactions related to the Micro-tel receiver or to shipments to Hong Kong, but in no event is there probable cause to support a general search for evidence of violations of the export laws. The government asserts that the affidavit “describ[ed] a systematic scheme for committing a specific narrow export offense.” Reply Brief of Appellant at 15. That is not accurate; the affidavit includes only a general reference to the export of electronic equipment to the People’s Republic of China through Hong Kong, and references no Kleinberg transactions apart from the export of the Micro-tel receiver.
 </p>
<p id="b701-13">
  In summary, we find the Kleinberg warrant overbroad in every respect.
  <a class="footnote" href="#fn23" id="fn23_ref">
   23
  </a>
  The
  <span citation-index="1" class="star-pagination" label="606"> 
   *606
   </span>
  warrant contains no limitation on the scope of the search, it is not as particular as the circumstances would allow or require and it extends far beyond the scope of the supporting affidavit. The warrant is invalid and we must determine if the evidence seized should be suppressed.
 </p>
<p id="b702-4">
  IY. Exclusion
 </p>
<p id="b702-5">
  Our conclusion that the Kleinberg warrant was invalid does not necessarily mean that the evidence seized under the warrant must be suppressed. The government argues that we should apply the “good faith” exception
  <a class="footnote" href="#fn24" id="fn24_ref">
   24
  </a>
  to the exclusionary rule created in
  <em>
   United States v. Leon,
  </em>
  <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U.S. 897</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">82 L.Ed.2d 677</a></span> (1984) and reverse the district court’s decision.
  <a class="footnote" href="#fn25" id="fn25_ref">
   25
  </a>
  The district court found the good faith exception inapplicable, but we note that whether the “good faith” exception to the exclusionary rule should be applied is a question of law, subject to
  <em>
   de novo
  </em>
  review by this court.
  <a class="footnote" href="#fn26" id="fn26_ref">
   26
  </a>
<em>
   See United States v. Mi-
  </em>
<span citation-index="1" class="star-pagination" label="607"> 
   *607
   </span>
<em>
   chaelian,
  </em>
  <span class="citation" data-id="478417"><a href="/opinion/478417/united-states-v-ara-michaelian/#1046" aria-description="Citation for case: United States v. Ara Michaelian">803 F.2d 1042, 1046</a></span> (9th Cir.1986);
  <em>
   United States v. Maggitt,
  </em>
  <span class="citation" data-id="461601"><a href="/opinion/461601/united-states-v-willie-b-maggitt-aka-willie-b-madgett/#1034" aria-description="Citation for case: United States v. Willie B. Maggitt, A/K/A Willie B. Madgett">778 F.2d 1029, 1034-35</a></span> (5th Cir.1985),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./476/1184/">476 U.S. 1184</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./106/2920/">106 S.Ct. 2920</a></span>, <span class="citation" data-id="9054533"><a href="/opinion/9060924/keplinger-v-united-states/" aria-description="Citation for case: Keplinger v. United States">91 L.Ed.2d 548</a></span> (1986).
 </p>
<p id="b703-4">
  In
  <em>
   <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>,
  </em>
  the Supreme Court modified the fourth amendment exclusionary rule to provide that evidence seized under a warrant later found to be invalid may be admissible if the executing officers acted in good faith and in reasonable reliance on the warrant.
  <em>
   United States v. Medlin,
  </em>
  <span class="citation" data-id="474635"><a href="/opinion/474635/united-states-v-arvle-edgar-medlin/#409" aria-description="Citation for case: United States v. Arvle Edgar Medlin">798 F.2d 407, 409</a></span> (10th Cir.1986);
  <em>
   see generally
  </em>
  1 LaFave § 1.3. The
  <em>
   <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>
  </em>
  Court applied the “good faith” exception to admit the evidence from a search warrant subsequently invalidated by a lack of probable cause. In
  <em>
   Massachusetts v. Sheppard,
  </em>
  <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#988" aria-description="Citation for case: Massachusetts v. Sheppard">468 U.S. 981, 988</a></span>, <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#3427" aria-description="Citation for case: Massachusetts v. Sheppard">104 S.Ct. 3424, 3427</a></span>, <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">82 L.Ed.2d 737</a></span> (1984) the Court held that the same exception could also be applied to warrants that violate the fourth amendment’s particularity requirement.
 </p>
<p id="b703-5">
  Of course,
  <em>
   <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>
  </em>
  does not mean that evidence obtained under an invalid warrant should never be suppressed. “The Court mandated that the exclusionary rule be invoked only in those ‘unusual’ cases in which its purposes would be served, i.e., in which it would deter police misconduct.”
  <em>
   Medlin,
  </em>
  <span class="citation" data-id="474635"><a href="/opinion/474635/united-states-v-arvle-edgar-medlin/#409" aria-description="Citation for case: United States v. Arvle Edgar Medlin">798 F.2d at 409</a></span>. The Court also identified certain circumstances where suppression remains an appropriate remedy, including where the warrant is “so facially
  <em>
   deficient
  </em>
  — i.e., in failing to particularize the place to be searched or the things to be seized — that the executing officers cannot reasonably presume it to be valid.”
  <em>
   Leon,
  </em>
  <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#923" aria-description="Citation for case: United States v. Leon">468 U.S. at 923</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#3420" aria-description="Citation for case: United States v. Leon">104 S.Ct. at 3420</a></span> (citations omitted).
  <a class="footnote" href="#fn27" id="fn27_ref">
   27
  </a>
  In determining whether the exception should be applied, the “good-faith inquiry is confined to the objectively ascertainable question whether a reasonably well trained officer would have known that the search was illegal despite the magistrate’s authorization.”
  <em>
   Leon,
  </em>
  <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U.S. at 922</a></span> n. 23, 104 S.Ct. at 3420 n. 23. To answer this “objectively ascertainable question,” we are to consider “all of the circumstances,”
  <em>
   id.
  </em>
  and assume that the executing “officers have a reasonable knowledge of what the law prohibits.”
  <em>
   Id.
  </em>
  at 919 n. 20, 104 S.Ct. at 3419 n. 20. Accordingly, under
  <em>
   <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>
  </em>
  and
  <em>
   <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard</a></span>,
  </em>
  even though we have previously determined the Kleinberg warrant to be facially invalid, we must also review the text of the warrant and the circumstances of the search to ascertain whether the agents might have “reasonably presume[d] it to be valid.”
  <em>
   Leon,
  </em>
  <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#923" aria-description="Citation for case: United States v. Leon">468 U.S. at 923</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#3420" aria-description="Citation for case: United States v. Leon">104 S.Ct. at 3420</a></span>.
 </p>
<p id="b703-10">
  The application of the “good faith” exception to an overbroad warrant has not yet been directly addressed by this court. However, there is guidance from other courts of appeals. This question has been most frequently considered by the Ninth Circuit. In
  <em>
   United States v. Crozier, 111
  </em>
  F.2d 1376, 1379 (9th Cir.1985) the government executed a warrant “that did not describe any particular property to be seized; it merely authorized the seizure of ‘Material evidence of violation 21 USC 841, 846.’ ” The court found the warrant facially over-broad and held that the agent could not reasonably rely on it.
  <span class="citation no-link"><em>
   Id.
  </em>
  at 1381</span>. “In contrast to the detective in
  <em>
   Sheppard,”
  </em>
  and similar to the customs agents here, the Ninth Circuit found that the agent “did not take ‘every step that could reasonably be expected of him.’”
  <em>
   <span class="citation no-link">Id.</span>
  </em>
  at 1382 (citing
  <em>
   Sheppard,
  </em>
  <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#989" aria-description="Citation for case: Massachusetts v. Sheppard">468 U.S. at 989</a></span>, <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#3428" aria-description="Citation for case: Massachusetts v. Sheppard">104 S.Ct. at 3428</a></span>). Specifically, the agent in
  <em>
   Crozier
  </em>
  failed to make the warrant as particular as the information available would allow and
  <span citation-index="1" class="star-pagination" label="608"> 
   *608
   </span>
  “obtained no specific assurance from the magistrate that the overbroad warrant was acceptable.”
  <em>
   <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Id.</a></span>
  </em>
</p>
<p id="b704-4">
  The Ninth Circuit reached the same conclusion in
  <em>
   United States v. Spilotro,
  </em>
  <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and...">800 F.2d 959</a></span> (9th Cir.1986). In
  <em>
   <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and...">Spilotro</a></span>,
  </em>
  the warrant authorized the search and seizure of property and records which were “evidence of violations” of a list of federal criminal statutes.
  <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/#961" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and..."><em>
   Id.
  </em>
  at 961</a></span>. The court relied on
  <em>
   Crozier
  </em>
  to find that the “good faith” exception was inapplicable to a facially overbroad warrant.
  <em>
   See also United States v. Washington,
  </em>
  <span class="citation" data-id="474531"><a href="/opinion/474531/united-states-v-ralph-h-washington/#1473" aria-description="Citation for case: United States v. Ralph H. Washington">797 F.2d 1461, 1473</a></span> (9th Cir.1986) (“the overbroad sections of the ... warrant are so facially deficient that any evidence obtained in reliance upon either of them must be suppressed”);
  <em>
   cf. United States v. Michaelian,
  </em>
  <span class="citation" data-id="478417"><a href="/opinion/478417/united-states-v-ara-michaelian/#1047" aria-description="Citation for case: United States v. Ara Michaelian">803 F.2d 1042, 1047</a></span> (9th Cir.1986) (warrants did not “approximate the degree of facial deficiency which would preclude objective reasonable reliance”).
 </p>
<p id="b704-5">
  The First Circuit has adopted similar reasoning. In
  <em>
   United States v. Fuccillo,
  </em>
  <span class="citation" data-id="480985"><a href="/opinion/480985/united-states-v-carl-a-fuccillo/#176" aria-description="Citation for case: United States v. Carl A. Fuccillo">808 F.2d 173,176-77</a></span> (1st Cir.),
  <em>
   cert. denied,
  </em>
  — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./107/2481/">107 S.Ct. 2481</a></span>, <span class="citation no-link">96 L.Ed.2d 374</span> (1987), the court invalidated warrants that inadequately described the stolen goods to be seized. As in this case, the court found that the “executing agents ... had no ‘physical criteria or detailed description in the warrant to enable them to determine what they might lawfully seize.’ ”
  <em>
   <span class="citation no-link">Id.</span>
  </em>
  at 177 (quoting
  <em>
   Montilla Records of Puerto Rico v. Morales,
  </em>
  <span class="citation" data-id="9464772"><a href="/opinion/355493/application-of-montilla-records-of-puerto-rico-inc-v-the-honorable-julio/#326" aria-description="Citation for case: Application of Montilla Records of Puerto Rico, Inc. v....">575 F.2d 324, 326-27</a></span> (1st Cir.1978)).
  <em>
   <span class="citation" data-id="480985"><a href="/opinion/480985/united-states-v-carl-a-fuccillo/" aria-description="Citation for case: United States v. Carl A. Fuccillo">Fuccillo</a></span>
  </em>
  also determined that the “good faith” exception was inapplicable, but focused on a different aspect of
  <em>
   <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>.
  </em>
  The warrant in
  <em>
   <span class="citation" data-id="480985"><a href="/opinion/480985/united-states-v-carl-a-fuccillo/" aria-description="Citation for case: United States v. Carl A. Fuccillo">Fuccillo</a></span>
  </em>
  authorized the FBI to seize cartons of women’s clothing and records related to those cartons. However, in executing the warrant, “the agents seized, in addition to the authorized cartons of
  <em>
   women’s
  </em>
  clothing, racks of clothing, empty boxes, and most disturbingly, two racks of
  <em>
   men’s
  </em>
  clothing. The
  <em>
   entire contents
  </em>
  of [a] warehouse were seized.”
  <span class="citation" data-id="480985"><a href="/opinion/480985/united-states-v-carl-a-fuccillo/#177" aria-description="Citation for case: United States v. Carl A. Fuccillo"><em>
   Id.
  </em>
  at 177-78</a></span> (emphasis in original). The court found the “good faith” exception inapplicable for three reasons. First, the agents exceeded the scope of the warrant. Second, the “agents were reckless in not including in the affidavit information which was known or easily accessible to them.”
  <span class="citation" data-id="480985"><a href="/opinion/480985/united-states-v-carl-a-fuccillo/#178" aria-description="Citation for case: United States v. Carl A. Fuccillo"><em>
   Id.
  </em>
  at 178</a></span>. Finally, the warrant was “ ‘so facially deficient... that the executing officers cannot reasonably presume it to be valid.’ ”
  <em>
   <span class="citation" data-id="480985"><a href="/opinion/480985/united-states-v-carl-a-fuccillo/" aria-description="Citation for case: United States v. Carl A. Fuccillo">Id.</a></span>
  </em>
  at 178 (quoting
  <em>
   Leon,
  </em>
  <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#923" aria-description="Citation for case: United States v. Leon">468 U.S. at 923</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#3420" aria-description="Citation for case: United States v. Leon">104 S.Ct. at 3420</a></span>).
  <em>
   Cf. United States v. Diaz,
  </em>
  <span class="citation" data-id="502477"><a href="/opinion/502477/united-states-v-leoncio-l-diaz-aka-leonel-diaz/#6" aria-description="Citation for case: United States v. Leoncio L. Diaz, A/K/A Leonel Diaz">841 F.2d 1, 6</a></span> (1st Cir.1988) (“[W[hile the warrant was overbroad ..., it was not so facially deficient that [the Agent] could not have reasonably and in good faith believed that it adequately authorized the search he undertook.”).
  <a class="footnote" href="#fn28" id="fn28_ref">
   28
  </a>
  The findings in
  <em>
   Fucillo
  </em>
  parallel our analysis of the Kleinberg warrant and search.
 </p>
<p id="b704-10">
  We are also in accord with the Eighth Circuit’s analysis of the “good faith” exception in
  <em>
   United States v. Strand,
  </em>
  <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers">761 F.2d 449</a></span> (8th Cir.1985). The warrant in
  <em>
   <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers">Strand</a></span>
  </em>
  authorized the search of an apartment for “stolen mail which is evidence of and the fruits of the crime of theft from the mail.”
  <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/#452" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers"><em>
   Id.
  </em>
  at 452</a></span>. The postal inspectors executing the warrant found stolen mail, but also seized certain household items that matched items that had been reported missing. The court held that the “warrant authorized a search only for ‘stolen mail,’ and that it did not describe the other items to be seized with sufficient particularity to be valid under the Fourth Amendment.”
  <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/#453" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers"><em>
   Id.
  </em>
  at 453-54</a></span>. The court then considered whether the evidence was admissible under the “good faith” exception, concluding that there was no “objectively reasonable basis for the postal inspectors to have believed that the warrant authorized the seizure of [the household] items” and that the exception did not apply.
  <a class="footnote" href="#fn29" id="fn29_ref">
   29
  </a>
<span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/#456" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers"><em>
   Id.
  </em>
  at 456</a></span>. Again, the court’s reasoning is applicable to the Klein-berg warrant and search. First, the
  <em>
   <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers">Strand</a></span>
  </em>
  court noted that the “seizure of ordinary household goods ... went far beyond the seizure expressly authorized by
  <span citation-index="1" class="star-pagination" label="609"> 
   *609
   </span>
  the
  <em>
   warrant_” <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers">Id.</a></span>
  </em>
  Second, the “seizure of household items ... not only went beyond the seizure contemplated by the warrant, but also went far beyond the seizure contemplated by the affidavit.”
  <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/#457" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers"><em>
   Id.
  </em>
  at 457</a></span>. Thus, the postal inspectors could not “reasonably believe” they had the authority to seize the household items. The court also found “no showing of any good reason for the lack of more particularized descriptions.”
  <em>
   <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers">Id.</a></span>
  </em>
</p>
<p id="b705-5">
  We have found only one appellate decision that reaches a contrary conclusion.
  <a class="footnote" href="#fn30" id="fn30_ref">
   30
  </a>
  In
  <em>
   United States v. Buck,
  </em>
  <span class="citation" data-id="484648"><a href="/opinion/484648/united-states-v-marilyn-buck/" aria-description="Citation for case: United States v. Marilyn Buck">813 F.2d 588</a></span> (2d Cir.),
  <em>
   cert. denied,
  </em>
  — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./108/167/">108 S.Ct. 167</a></span>, <span class="citation no-link">98 L.Ed.2d 121</span> (1987) police officers were investigating the robbery of an armored car. Witnesses identified a car leaving the scene with several gunmen. Working through the night, the police traced the car to an apartment and sought a telephone warrant to search the apartment. The judge placed the officer under oath, elicited details of the crime and investigation and then verbally authorized a warrant “to seize any papers, things or property of any kind relating to previously described crime.”
  <span class="citation no-link"><em>
   Id.
  </em>
  at 590</span>. The court found the language of the warrant impermissibly broad, but found no police misconduct: “While it can safely be said that the police here performed reasonably under the circumstances and collected all the ‘descriptive facts’ they could ... they clearly did not insure that all known facts were included in the warrant. The warrant only described the crimes — and gave no limitation whatsoever on the kind of evidence sought.”
  <span class="citation no-link"><em>
   Id.
  </em>
  at 591-92</span>. The court found the evidence admissible under
  <em>
   <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>
  </em>
  and
  <em>
   <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard</a></span>
  </em>
  because “the officers made considerable efforts to comply with the dictates of the Fourth Amendment.”
  <em>
   Id.
  </em>
  at 592. The court reasoned that the evidence should not be suppressed because “the law was unsettled as to how particular the description of the articles to be seized must be” and under those circumstances, “a reasonably well-trained police officer could not be expected to know that the warrant” violated the fourth amendment.
  <em>
   Id.
  </em>
  at 593.
 </p>
<p id="b705-9">
  Obviously,
  <em>
   <span class="citation" data-id="484648"><a href="/opinion/484648/united-states-v-marilyn-buck/" aria-description="Citation for case: United States v. Marilyn Buck">Buck</a></span>
  </em>
  presents a different factual situation than we face here. Moreover, we are not expecting the agents to anticipate legal determinations or resolve ambiguities in the law. A reasonably well-trained officer should know that a warrant must provide guidelines for determining what evidence may be seized.
  <a class="footnote" href="#fn31" id="fn31_ref">
   31
  </a>
  A warrant that directs an officer to seize records “relating to” violations of the federal export laws offers no such guidelines. The officers were left to their own discretion.
 </p>
<p id="b705-10">
  We conclude that the government may not rely on the “good faith” exception in this case and that all evidence seized under the Kleinberg warrant should be suppressed. We find the warrant so facially deficient in its description of the items to be seized that the executing officers could not reasonably rely on it. That conclusion
  <span citation-index="1" class="star-pagination" label="610"> 
   *610
   </span>
  is reinforced by the government’s conduct and the circumstances of the search. This is one of those “unusual” cases where suppression of the evidence is appropriate to deter government misconduct. As we said in
  <em>
   United States v. Owens,
  </em>
  <span class="citation" data-id="463621"><a href="/opinion/463621/united-states-v-merle-ellis-owens/#152" aria-description="Citation for case: United States v. Merle Ellis Owens">782 F.2d 146, 152</a></span> (10th Cir.1986), the search here “exemplifies the very type of official conduct the exclusionary rule is intended to deter.”
  <a class="footnote" href="#fn32" id="fn32_ref">
   32
  </a>
  Accordingly, we hold that the “good faith” exception is inapplicable in these circumstances and affirm the district court’s decision to suppress all of the evidence from the Kleinberg warrant.
 </p>
<p id="b706-4">
  V. Probable Cause
 </p>
<p id="b706-5">
  Because we have decided to suppress the evidence based on the warrant’s over-breadth, there is no need to review the district court’s decision that the warrant was not supported by probable cause.
 </p>
<p id="b706-6">
  The district court’s decision granting defendants’ motion to suppress is AFFIRMED.
 </p>
































<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b690-13">
   . The Micro-tel receiver is a "device used to measure or test the basic output of electronic parts." Brief of Appellees at 2 (citing R. Vol. Ill at 202).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b690-14">
   . The affidavit specifically mentions six companies involved in the Micro-tel transaction: Kleinberg; Micro-tel Corporation, a Maryland manufacturer; Union Air Transport, Kleinberg’s shipping agent in California; Hong Kong Computer Company, the purchaser in Hong Kong; Dataventures International, Ltd., another Hong Kong company which was supposed to purchase the receiver from Hong Kong Computer; and Tak Sing Company of Hong Kong, the final purchaser of the receiver in Hong Kong.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b691-10">
   . According to the district court:
  </p>
<blockquote id="b691-11">
   The evidence shows that the magistrate was led to believe a crime had been committed by the defendants when Agent Juhasz could not himself have believed that the facts he set forth in his affidavit constituted a crime. The affidavit on its face fails to establish probable cause that any crime had been committed if the relevant statutes and facts are examined.
  </blockquote>
<p id="b691-12">
   Mem.Opinion at 5-6.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b691-15">
   . Nevertheless, fourth amendment claims are still commonly analyzed in terms of "standing."
   <em>
    See
   </em>
   3 C. Wright,
   <em>
    Federal Practice and Procedure
   </em>
   § 674 (2d ed. 1982);
   <em>
    see, e.g., United States v. Salvucci,
   </em>
   <span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">448 U.S. 83</a></span>, 87 n. 4, <span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">100 S.Ct. 2547</a></span>, 2551 n. 4, <span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">65 L.Ed.2d 619</a></span> (1980);
   <em>
    United States v. Skowronski,
   </em>
   <span class="citation" data-id="493687"><a href="/opinion/493687/united-states-v-william-michael-skowronski/#1417" aria-description="Citation for case: United States v. William Michael Skowronski">827 F.2d 1414, 1417-18</a></span> (10th Cir.1987);
   <em>
    United States v. Salazar,
   </em>
   <span class="citation" data-id="479836"><a href="/opinion/479836/united-states-v-edgar-salazar/#1396" aria-description="Citation for case: United States v. Edgar Salazar">805 F.2d 1394, 1396</a></span> (9th Cir.1986);
   <em>
    United States v. Gerena,
   </em>
   <span class="citation" data-id="1392737"><a href="/opinion/1392737/united-states-v-gerena/#1232" aria-description="Citation for case: United States v. Gerena">662 F.Supp. 1218, 1232-40</a></span> (D.Conn.1987).
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b692-7">
   . The government suggests that the defendants’ fourth amendment rights are somehow limited by the reasoning of
   <em>
    Shapiro v. United States,
   </em>
   <span class="citation" data-id="9420211"><a href="/opinion/104585/shapiro-v-united-states/" aria-description="Citation for case: Shapiro v. United States">335 U.S. 1</a></span>, <span class="citation" data-id="9420211"><a href="/opinion/104585/shapiro-v-united-states/" aria-description="Citation for case: Shapiro v. United States">68 S.Ct. 1375</a></span>, <span class="citation no-link">92 L.Ed. 1787</span> (1970) and
   <em>
    Peterman
   </em>
   v.
   <em>
    Coleman,
   </em>
   <span class="citation" data-id="453574"><a href="/opinion/453574/frank-peterman-bruce-horne-v-gerry-coleman-in-his-official-capacity-as/" aria-description="Citation for case: Frank Peterman, Bruce Horne v. Gerry Coleman, in His...">764 F.2d 1416</a></span> (11th Cir.1985). A careful review of those cases demonstrates that they are inapplicable here. Both decisions conclude that the government may impose recordkeeping and inspection requirements on certain businesses without violating the fourth amendment. The validity of the recordkeeping and inspection requirements imposed upon licensed exporters are not at issue.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b693-7">
   . Of course “[a]n expectation of privacy in commercial premises, ... is different from, and indeed less than, a similar expectation in an individual's home. This expectation is particularly attenuated in commercial property employed in ‘closely regulated’ industries."
   <em>
    New York v. Burger,
   </em>
   — U.S. -, <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#2642" aria-description="Citation for case: New York v. Burger">107 S.Ct. 2636, 2642</a></span>, <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/" aria-description="Citation for case: New York v. Burger">96 L.Ed.2d 601</a></span> (1987) (citations omitted). Nevertheless, we reject the government's argument that the nature of the Kleinberg business diminishes the defendants’ expectation of privacy. The reduced expectation of privacy in commercial premises is important in two respects, neither of which is relevant to our disposition of this case. First, the reduced expectation of privacy may justify a statutory authorization of warrantless inspections or searches.
   <em>
    See Id,
   </em>
   at 2643-44. The government concedes that a warrant was required to search the Kleinberg offices. Second, the nature of the premises may "affect the type of evidence that constitutes
   <span citation-index="1" class="star-pagination" label="598"> 
    *598
    </span>
   probable cause to obtain a search warrant in the particular case.”
   <em>
    Blackie’s House of Beef,
   </em>
   <span class="citation" data-id="394830"><a href="/opinion/394830/blackies-house-of-beef-inc-v-leonel-j-castillo-commissioner-of-the/" aria-description="Citation for case: Blackie&#x27;s House of Beef, Inc. v. Leonel J. Castillo,...">659 F.2d at 1216</a></span> n. 5. We find no need to reach the question of probable cause.
   <em>
    See infra
   </em>
   at 610.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b694-6">
   . For an example of ongoing consent treated as a waiver, see
   <em>
    American Postal Workers Union v. United States Postal Service,
   </em>
   <span class="citation" data-id="2595045"><a href="/opinion/2595045/american-postal-workers-union-v-united-states-postal-service/#501" aria-description="Citation for case: American Postal Workers Union v. United States Postal...">671 F.Supp. 497, 501-02</a></span> (S.D.Ohio 1987) (Where "postal regulations, express terms of locker assignment agreements and collective bargaining agreements providefd] for nonconsensual inspection of employee lockers by post office personnel," postal employees "expressly waived any Fourth Amendment rights they might otherwise have in their assigned lockers.”).
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b694-7">
   . We believe that
   <em>
    <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span>
   </em>
   demands that we review the government's "waiver” argument as a question of consent.
   <em>
    See Schneckloth,
   </em>
   <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#246" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. at 246</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#2057" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. at 2057</a></span>. We also find the Court’s quotation from Justice Black instructive: " “Waiver’ is a vague term used for a great variety of purposes, good and bad, in the law.,”
   <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#235" aria-description="Citation for case: Schneckloth v. Bustamonte"><em>
    Id.
   </em>
   at 235</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. at 2052</a></span> (quoting
   <em>
    Green
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9421521"><a href="/opinion/105594/green-v-united-states/#191" aria-description="Citation for case: Green v. United States">355 U.S. 184, 191</a></span>, <span class="citation" data-id="9421521"><a href="/opinion/105594/green-v-united-states/#226" aria-description="Citation for case: Green v. United States">78 S.Ct. 221, 226</a></span>, <span class="citation" data-id="9421521"><a href="/opinion/105594/green-v-united-states/" aria-description="Citation for case: Green v. United States">2 L.Ed.2d 199</a></span> (1957)).
  </p>
</div><div class="footnote" id="fn9" label="9">
<a class="footnote" href="#fn9_ref">
   9
  </a>
<p id="b694-10">
   .The Court’s language in
   <em>
    <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">Bumper</a></span>
   </em>
   has not been applied literally in all cases.
   <em>
    See Comeaux v. Henderson,
   </em>
   <span class="citation" data-id="304369"><a href="/opinion/304369/claude-comeaux-v-c-murray-henderson-warden/#1346" aria-description="Citation for case: Claude Comeaux v. C. Murray Henderson, Warden">462 F.2d 1345, 1346</a></span> (5th Cir.1972) ("not every consent to a search is automatically vitiated simply because a tainted warrant is immediately or remotely involved”);
   <em>
    United States v. Stine,
   </em>
   <span class="citation" data-id="1875700"><a href="/opinion/1875700/united-states-v-stine/#370" aria-description="Citation for case: United States v. Stine">458 F.Supp. 366, 370</a></span> (E.D.Pa.1978) (“In a proper case, a voluntary consent may break the chain of causation between an illegal search warrant and a subsequent search.").
  </p>
<p id="b694-11">
   At the same time, it is clear that the reasoning of
   <em>
    <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">Bumper</a></span>
   </em>
   applies in a commercial context and is relevant here. Professor LaFave has noted "if the businessman admits [a government] inspector only after being told that the inspector has a right to conduct a warrantless inspection, this is not consent but merely an acquiescence to a claim of lawful authority no different than that in
   <em>
    Bumper
   </em>
   v.
   <em>
    <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">North Carolina</a></span>.
   </em>
   If the inspector makes such a claim, then ... ‘the legality of the search depends not on consent but on the authority of a valid statute.’ ’’ 3 LaFave, § 10.2(b), at 637 (quoting in part
   <em>
    United States
   </em>
   v.
   <em>
    Biswell,
   </em>
   <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U.S. 311</a></span>, <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">92 S.Ct. 1593</a></span>, <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">32 L.Ed.2d 87</a></span> (1972)). As we have noted, the export statutes
   <span citation-index="1" class="star-pagination" label="599"> 
    *599
    </span>
   and regulations do not authorize warrantless inspections.
  </p>
</div><div class="footnote" id="fn10" label="10">
<a class="footnote" href="#fn10_ref">
   10
  </a>
<p id="b695-8">
   . In reviewing the district court’s decision on the question of consent, we rely on the lower court’s factual findings unless they are clearly erroneous.
   <em>
    See United States v. Lopez,
   </em>
   <span class="citation" data-id="461084"><a href="/opinion/461084/united-states-v-augustin-alonso-lopez/#548" aria-description="Citation for case: United States v. Augustin Alonso Lopez">777 F.2d 543, 548</a></span> (10th Cir.1985);
   <em>
    Recalde,
   </em>
   <span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1453" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d at 1453</a></span>. However, the question of consent or waiver was not raised in the same fashion below; while the district court found that the defendants had standing to assert their fourth amendment claims, there was no explicit finding on the question of consent. Accordingly, we review the record to answer this question. Because the facts are essentially undisputed, there is no reason to remand for factual determinations.
   <em>
    See <span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/" aria-description="Citation for case: United States v. Miguel Angel Recalde">Id.</a></span>
   </em>
   at 1453 n. 4;
   <em>
    cf. United States v. Skowronski,
   </em>
   <span class="citation" data-id="493687"><a href="/opinion/493687/united-states-v-william-michael-skowronski/" aria-description="Citation for case: United States v. William Michael Skowronski">827 F.2d 1414</a></span>, 1417 n. 2 (10th Cir.1987);
   <em>
    United States v. Hansen,
   </em>
   <span class="citation" data-id="392049"><a href="/opinion/392049/united-states-v-gary-e-hansen-daniel-e-means-aka-daniel-e-johnson/#1383" aria-description="Citation for case: United States v. Gary E. Hansen, Daniel E. Means, AKA...">652 F.2d 1374, 1383</a></span> (10th Cir.1981).
  </p>
</div><div class="footnote" id="fn11" label="11">
<a class="footnote" href="#fn11_ref">
   11
  </a>
<p id="b695-12">
   . Furthermore, the government asks that we adopt this reasoning in a case where the government
   <em>
    did not rely
   </em>
   on the policy of voluntary cooperation but entered the premises with a search warrant.
   <em>
    See Bumper v. North Carolina,
   </em>
<span citation-index="1" class="star-pagination" label="600"> 
    *600
    </span>
   <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">391 U.S. 543</a></span>, <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">88 S.Ct. 1788</a></span>, <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">20 L.Ed.2d 797</a></span> (1968).
  </p>
</div><div class="footnote" id="fn12" label="12">
<a class="footnote" href="#fn12_ref">
   12
  </a>
<p id="b696-9">
   . Thus, the direction in
   <em>
    <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">Stanford</a></span>
   </em>
   that "nothing is left to the discretion of the officer” has been interpreted in a variety of "practical" ways.
   <em>
    See, e.g., United States v. Strand,
   </em>
   <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/#453" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers">761 F.2d 449, 453</a></span> (8th Cir.1985) ("The constitutional standard for particularity of description in a search warrant is that the language be sufficiently definite to enable the searcher reasonably to ascertain and identify the things authorized to be seized.");
   <em>
    see also
   </em>
   2 LaFave, § 4.6(a); 3 C. Wright,
   <em>
    Federal Practice and Procedure
   </em>
   § 670, at 720-22 (2d ed. 1982). The common theme of all descriptions of the particularity standard is that the warrant must allow the executing officer to distinguish between items that may and may not be seized.
  </p>
</div><div class="footnote" id="fn13" label="13">
<a class="footnote" href="#fn13_ref">
   13
  </a>
<p id="b697-6">
   .The government cites a number of cases where warrants for business records have been held sufficiently particular to meet the requirements of the fourth amendment. We have reviewed these cases and find that they do not support the government’s claim, as the warrants in question were more particular than the one we review here, or the warrants were as particular as the information available would allow.
   <em>
    See, e.g., Andresen v. Maryland,
   </em>
   <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#481" aria-description="Citation for case: Andresen v. Maryland">427 U.S. 463, 481-82</a></span>, <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#2749" aria-description="Citation for case: Andresen v. Maryland">96 S.Ct. 2737, 2749</a></span>, <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">49 L.Ed.2d 627</a></span> (1976) (documents limited to a specific transaction);
   <em>
    United States v. Lamport,
   </em>
   <span class="citation" data-id="467613"><a href="/opinion/467613/united-states-v-frederick-e-lamport-jr/#476" aria-description="Citation for case: United States v. Frederick E. Lamport, Jr.">787 F.2d 474, 476</a></span> (10th Cir.) (more specific warrant),
   <em>
    cert. denied,
   </em>
   — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./107/166/">107 S.Ct. 166</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/93/104/">93 L.Ed.2d 104</a></span> (1986);
   <em>
    Marvin v. United States,
   </em>
   <span class="citation" data-id="434740"><a href="/opinion/434740/dr-jack-l-marvin-patricia-marvin-v-united-states/#673" aria-description="Citation for case: Dr. Jack L. Marvin, Patricia Marvin v. United States">732 F.2d 669, 673-74</a></span> (8th Cir.1984) (records to be seized limited by type and date);
   <em>
    United States v. Wuagneux,
   </em>
   <span class="citation" data-id="406519"><a href="/opinion/406519/united-states-v-george-wuagneux/" aria-description="Citation for case: United States v. George Wuagneux">683 F.2d 1343</a></span>, 1350 n. 5 (11th Cir.1982) (more specific warrant),
   <em>
    cert. denied,
   </em>
   <span class="citation multiple-matches"><a href="/c/U.S./464/814/">464 U.S. 814</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./104/69/">104 S.Ct. 69</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/78/83/">78 L.Ed.2d 83</a></span> (1983);
   <em>
    United States
   </em>
   v.
   <em>
    Timpani,
   </em>
   <span class="citation" data-id="397225"><a href="/opinion/397225/united-states-v-joseph-a-timpani/#4" aria-description="Citation for case: United States v. Joseph A. Timpani">665 F.2d 1, 4-5</a></span> (1st Cir.1981) ("it is difficult to see how the search warrant could have been made significantly more precise");
   <em>
    United States v. Dennis,
   </em>
   <span class="citation" data-id="380192"><a href="/opinion/380192/united-states-v-willie-h-dennis/#792" aria-description="Citation for case: United States v. Willie H. Dennis">625 F.2d 782, 792</a></span> (8th Cir.1980) (warrant as specific as circumstances would allow). None of the decisions cited by the government allow a general description where the information was readily available to significantly narrow the search. The government argues that
   <em>
    <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">Andresen</a></span>
   </em>
   authorizes the seizure of general business records, but the warrant in
   <em>
    <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">Andresen</a></span>
   </em>
   was limited to a specific transaction.
   <em>
    See
   </em>
   In re
   <em>
    Grand Jury Proceedings (Young),
   </em>
   <span class="citation" data-id="9471119"><a href="/opinion/424091/in-re-grand-jury-proceedings-appeal-of-robert-e-young/" aria-description="Citation for case: In Re Grand Jury Proceedings. Appeal of Robert E. Young">716 F.2d 493</a></span>, 498 n. 7 (8th Cir.1983);
   <em>
    United States v. Roche,
   </em>
   <span class="citation" data-id="373913"><a href="/opinion/373913/united-states-v-john-c-roche/" aria-description="Citation for case: United States v. John C. Roche">614 F.2d 6</a></span>, 7 n. 2 (1st Cir.1980). If the Kleinberg warrant had been explicitly limited to documents related to the Micro-tel transaction it would be comparable to the warrant in
   <em>
    <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">Andresen</a></span>.
   </em>
</p>
</div><div class="footnote" id="fn14" label="14">
<a class="footnote" href="#fn14_ref">
   14
  </a>
<p id="b697-13">
   .
   <em>
    <span class="citation" data-id="8935318"><a href="/opinion/8944758/voss-v-bergsgaard/" aria-description="Citation for case: Voss v. Bergsgaard">Voss</a></span>
   </em>
   differs from the current case in two respects. First, the search in
   <em>
    <span class="citation" data-id="8935318"><a href="/opinion/8944758/voss-v-bergsgaard/" aria-description="Citation for case: Voss v. Bergsgaard">Voss</a></span>
   </em>
   implicated first amendment concerns that are not present here. Second, the conspiracy statute is arguably broader than the export statutes cited in the Kleinberg warrant. However, neither distinction is reason to depart from our holding. The first amendment concerns were not central to the decision but merely made the "warrants’ overbreadth ... even more egregious."
   <em>
    Voss,
   </em>
   <span class="citation" data-id="8935318"><a href="/opinion/8944758/voss-v-bergsgaard/#405" aria-description="Citation for case: Voss v. Bergsgaard">774 F.2d at 405</a></span>. Similarly, the differences in the statutes cited are not significant.
  </p>
</div><div class="footnote" id="fn15" label="15">
<a class="footnote" href="#fn15_ref">
   15
  </a>
<p id="b697-14">
   . We emphasize that it is not the mere reference to the statute that makes the Kleinberg warrant overbroad, it is the
   <em>
    absence of any limiting features.
   </em>
   In other words, the warrant is limited neither by the list of records to be seized, nor by the reference to the export statutes. If the warrant were narrower in either respect, or if it included some other limitation, we might find it valid. For example, this court found the warrant in
   <em>
    United States v. Lamport,
   </em>
   <span class="citation" data-id="467613"><a href="/opinion/467613/united-states-v-frederick-e-lamport-jr/#476" aria-description="Citation for case: United States v. Frederick E. Lamport, Jr.">787 F.2d 474, 476</a></span> (10th Cir.),
   <em>
    cert. denied,
   </em>
   — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./107/166/">107 S.Ct. 166</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/93/104/">93 L.Ed.2d 104</a></span> (1986), sufficiently specific where the statutory reference (to the mail fraud statute) was limited by a list of specific items (medical records limited by patients and dates).
  </p>
</div><div class="footnote" id="fn16" label="16">
<a class="footnote" href="#fn16_ref">
   16
  </a>
<p id="b698-6">
   . The government argues that the "agents based their decisions on the guidelines set forth in the warrant which they testified was sufficiently descriptive.” Brief of Appellant at 39. But the government’s citations to the record of the suppression hearing do not support that assertion. The record clearly indicates that the agents relied on Agent Juhasz' instructions.
   <em>
    See, e.g.,
   </em>
   R. Vol. Ill at 31-32, 45-47. The only acknowledged guidance from the face of the warrant by the agents is that they "were looking for records reflecting possible violations of the Export Administration Act, ...”
   <em>
    Id.
   </em>
   at 30.
  </p>
</div><div class="footnote" id="fn17" label="17">
<a class="footnote" href="#fn17_ref">
   17
  </a>
<p id="b698-7">
   . In
   <em>
    United States v. Sawyer, 799
   </em>
   F.2d 1494 (11th Cir.1986) the Elev

[...TRUNCATED 29024 of 149024 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
