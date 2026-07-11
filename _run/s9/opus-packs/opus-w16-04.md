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

## GROUP: _overhaul2/lake/cases/United States v. Hensley.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Hensley"
type: case
citation: "469 U.S. 221 (1985)"
parallel_cite: "105 S. Ct. 675; 83 L. Ed. 2d 604; 53 U.S.L.W. 4053"
neutral_cite: 1985 U.S. LEXIS 34
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-01-08
docket: 83-1330
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-01-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Hensley
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111294/united-states-v-hensley/"
  cluster_id: 111294
  opinion_id: 9429804
  identity_checked: true
homes:
  - page: "[[Collective Knowledge and the Fellow-Officer Rule]]"
    role: "Key — Anchor"
related: ["[[Terry v. Ohio]]", "[[Delaware v. Prouse]]", "[[United States v. Cortez]]"]
aliases: []
tags: ["case", "fourth-amendment", "terry-stop", "collective-knowledge", "fellow-officer-rule", "wanted-flyer", "completed-crime"]
holding: "Police may conduct a Terry investigatory stop in objective reliance on a wanted flyer or bulletin issued by another police department if…"
lake:
  record_id: United States v. Hensley
  status: verified
  projected_at: 2026-07-06
---

# United States v. Hensley

*469 U.S. 221 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After an armed tavern robbery in St. Bernard, Ohio, an informant told Officer Davis that Thomas Hensley had driven the getaway car. Davis took a written statement and issued a "wanted flyer" to other Cincinnati-area departments, describing Hensley and the robbery and asking them to pick him up. Covington, Kentucky officers, who had read the flyer at shift changes, recognized Hensley days later, stopped his car, and — after one officer approached and saw a handgun — arrested him. Hensley, a felon, was convicted of being a felon in possession.

## Issue
(1) Whether the Fourth Amendment permits a *[[Terry v. Ohio|Terry]]* investigatory stop on reasonable suspicion that a person was involved in a *completed* crime; and (2) whether officers may make such a stop in objective reliance on a "wanted flyer" issued by another department.

## Rule
Yes to both. First, *[[Terry v. Ohio|Terry]]* stops are not confined to ongoing or imminent crimes: "if police have a reasonable suspicion, grounded in specific and articulable facts, that a person they encounter was involved in or is wanted in connection with a completed felony, then a *Terry* stop may be made to investigate that suspicion." — 469 U.S. at 229. ^pin-229

Second, the validity of a stop made in reliance on a bulletin turns on the issuing department's knowledge, judged objectively: "It is the objective reading of the flyer or bulletin that determines whether other police officers can defensibly act in reliance on it." — *Id.* at 232. ^pin-232

"Assuming the police make a *Terry* stop in objective reliance on a flyer or bulletin, we hold that the evidence uncovered in the course of the stop is admissible if the police who *issued* the flyer or bulletin possessed a reasonable suspicion justifying a stop, and if the stop that in fact occurred was not significantly more intrusive than would have been permitted the issuing department." — *Id.* at 233. ^pin-233

## Application
On these facts the Covington stop was lawful. Although the robbery was already completed, the St. Bernard police had a reasonable suspicion — grounded in the informant's specific account that Hensley drove the getaway car, reduced to a written statement — sufficient to justify a stop, and that suspicion "underlies and supports their issuance of the flyer." The Covington officers acted in objective reliance on the flyer, and the stop they made "was not significantly more intrusive than would have been permitted the St. Bernard police." Because the issuing department had the requisite reasonable suspicion and the actual stop stayed within those bounds, "the investigatory stop was reasonable under the Fourth Amendment, and the evidence discovered during the stop was admissible." The Court did not need to decide whether the issuing department had probable cause, nor whether *[[Terry v. Ohio|Terry]]* reaches all completed crimes — reasonable suspicion of a completed felony was enough.

## Conclusion
A *[[Terry v. Ohio|Terry]]* stop may rest on reasonable suspicion of a completed felony, and officers may make it in objective reliance on another department's flyer where the issuing department had reasonable suspicion; the Sixth Circuit's judgment reversing the conviction was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Hensley* is the foundational SCOTUS statement of the collective-knowledge / fellow-officer rule for investigatory stops, extending the [[Terry v. Ohio]] framework to completed crimes and to inter-department bulletin reliance.

## Appears on
- [[Collective Knowledge and the Fellow-Officer Rule]] — *Key — Anchor*

## Sources
- *United States v. Hensley*, 469 U.S. 221 (1985) — https://www.courtlistener.com/opinion/111294/united-states-v-hensley/ — pinpoints: 229, 232, 233.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8a37ae1cea2f1000", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Hensley"}, "payload": {"all": [{"cite": "469 U.S. 221", "page": "221", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "469"}, {"cite": "105 S. Ct. 675", "page": "675", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "105"}, {"cite": "83 L. Ed. 2d 604", "page": "604", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "83"}, {"cite": "1985 U.S. LEXIS 34", "page": "34", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1985"}, {"cite": "53 U.S.L.W. 4053", "page": "4053", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "53"}], "display": "469 U.S. 221", "official": {"cite": "469 U.S. 221", "page": "221", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "469"}, "official_selection_present": true, "record_id": "United States v. Hensley"}}
{"assertion_id": "07138dd159967981", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-229", "record_id": "United States v. Hensley"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-229", "pinpoint_status": "slip-only", "quote": "issued by another department. ## Rule Yes to both. First, *Terry* stops are not confined to ongoing or imminent crimes:", "quote_fidelity": "mismatch", "record_id": "United States v. Hensley", "star_marker": null}}
{"assertion_id": "5968e7fc1d62ed96", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-233", "record_id": "United States v. Hensley"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-233", "pinpoint_status": "slip-only", "quote": "Assuming the police make a *Terry* stop in objective reliance on a flyer or bulletin, we hold that the evidence uncovered in the course of the stop is admissible if the police who *issued* the flyer or bulletin possessed a reasonable suspicion justifying a stop, and if the stop that in fact occurred was not significantly more intrusive than would have been permitted the issuing department.", "quote_fidelity": "mismatch", "record_id": "United States v. Hensley", "star_marker": null}}
{"assertion_id": "71f0f1890dac5154", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-232", "record_id": "United States v. Hensley"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-232", "pinpoint_status": "slip-only", "quote": "It is the objective reading of the flyer or bulletin that determines whether other police officers can defensibly act in reliance on it.", "quote_fidelity": "mismatch", "record_id": "United States v. Hensley", "star_marker": null}}
{"assertion_id": "f3020968dfbf790a", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Hensley"}, "payload": {"as_of_content": "1985-01-08", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Hensley", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Hensley

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Hensley",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Hensley",
    "case_name_short": "Hensley",
    "case_name_full": "United States v. Hensley",
    "input_case_name": "United States v. Hensley",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-01-08",
    "year": 1985,
    "docket": "83-1330",
    "cluster_id": 111294,
    "lead_opinion_id": 9429804,
    "sibling_ids": [
      111294,
      9429804,
      9429805
    ],
    "absolute_url": "/opinion/111294/united-states-v-hensley/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "469 U.S. 221",
      "volume": "469",
      "reporter": "U.S.",
      "page": "221",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 675",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "675",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 604",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "604",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4053",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4053",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 34",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "34",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "469 U.S. 221",
        "volume": "469",
        "reporter": "U.S.",
        "page": "221",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 675",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "675",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 604",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "604",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 34",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "34",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4053",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4053",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "469 U.S. 221",
    "official_selection": {
      "court_class": "scotus",
      "selected": "469 U.S. 221",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-229",
      "page": null,
      "quote": "issued by another department. ## Rule Yes to both. First, *Terry* stops are not confined to ongoing or imminent crimes:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-232",
      "page": null,
      "quote": "It is the objective reading of the flyer or bulletin that determines whether other police officers can defensibly act in reliance on it.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-233",
      "page": null,
      "quote": "Assuming the police make a *Terry* stop in objective reliance on a flyer or bulletin, we hold that the evidence uncovered in the course of the stop is admissible if the police who *issued* the flyer or bulletin possessed a reasonable suspicion justifying a stop, and if the stop that in fact occurred was not significantly more intrusive than would have been permitted the issuing department.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-01-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Hensley",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 10843215,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane1_negative"
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
        "journal_ref": "United States v. Hensley:lane1_negative"
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
        "journal_ref": "United States v. Hensley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Connor William Clar Steffens",
          "cluster_id": 4332280,
          "cite": [
            "889 N.W.2d 691",
            "2016 Iowa App. LEXIS 1316",
            "2016 WL 7393893"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Keene",
          "cluster_id": 3189183,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Emerson",
          "cluster_id": 2830814,
          "cite": [
            "2015 MT 254",
            "380 Mont. 487",
            "2015 Mont. LEXIS 441",
            "355 P.3d 763"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Guzman v. State",
          "cluster_id": 2449770,
          "cite": [
            "955 S.W.2d 85",
            "1997 Tex. Crim. App. LEXIS 72",
            "1997 WL 587024"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Prado Navarette v. California",
          "cluster_id": 2670795,
          "cite": [
            "188 L. Ed. 2d 680",
            "134 S. Ct. 1683",
            "2014 U.S. LEXIS 2930",
            "82 U.S.L.W. 4282",
            "572 U.S. 393",
            "24 Fla. L. Weekly Fed. S 690",
            "2014 WL 1577513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Yeargan",
          "cluster_id": 1060948,
          "cite": [
            "958 S.W.2d 626",
            "1997 Tenn. LEXIS 574",
            "1997 WL 724993"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Winston v. Lee",
          "cluster_id": 111380,
          "cite": [
            "84 L. Ed. 2d 662",
            "105 S. Ct. 1611",
            "470 U.S. 753",
            "1985 U.S. LEXIS 76",
            "53 U.S.L.W. 4367"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Derichsweiler v. State",
          "cluster_id": 2539048,
          "cite": [
            "348 S.W.3d 906",
            "2011 Tex. Crim. App. LEXIS 112",
            "2011 WL 255299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Letner and Tobin",
          "cluster_id": 2630926,
          "cite": [
            "235 P.3d 62",
            "50 Cal. 4th 99",
            "112 Cal. Rptr. 3d 746",
            "2010 Cal. LEXIS 7290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Maumee v. Weisner",
          "cluster_id": 2689810,
          "cite": [
            "1999 Ohio 68",
            "87 Ohio St. 3d 295"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zellner v. Summerlin",
          "cluster_id": 2707,
          "cite": [
            "494 F.3d 344",
            "2007 U.S. App. LEXIS 17272",
            "2007 WL 2067932"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vincent Anthony Perdue",
          "cluster_id": 656633,
          "cite": [
            "8 F.3d 1455",
            "1993 U.S. App. LEXIS 28321",
            "1993 WL 437983"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. McKnight",
          "cluster_id": 6894158,
          "cite": [
            "107 Ohio St. 3d 101",
            "837 N.E.2d 315"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delk v. State",
          "cluster_id": 1669263,
          "cite": [
            "855 S.W.2d 700",
            "1993 Tex. Crim. App. LEXIS 88",
            "1993 WL 120353"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gates v. Texas Deparment of Protective & Regulatory Services",
          "cluster_id": 62905,
          "cite": [
            "537 F.3d 404",
            "2008 WL 2875378"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thomas L. Feathers Kathleen Feathers v. William Aey J.P. Donohue, City of Akron",
          "cluster_id": 780866,
          "cite": [
            "319 F.3d 843",
            "2003 U.S. App. LEXIS 2642",
            "2003 WL 296924"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Kennedy",
          "cluster_id": 1374527,
          "cite": [
            "726 P.2d 445",
            "107 Wash. 2d 1",
            "1986 Wash. LEXIS 1273"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111294 OR 9429804 OR 9429805) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzk4MTI0ODAwMDAwJnM9MjY3MDc5NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111294+OR+9429804+OR+9429805%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111294 OR 9429804 OR 9429805)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNDEmcz0yNDI5NjQ2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111294+OR+9429804+OR+9429805%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111294 OR 9429804 OR 9429805)",
        "reviewed": 54,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 54,
        "triage_read": 2,
        "triage_snippet_classified": 52
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111294 OR 9429804 OR 9429805)",
    "indexed_citing_opinions": 1345,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111294,
        "count": 1147,
        "count_source": "search"
      },
      {
        "opinion_id": 9429804,
        "count": 216,
        "count_source": "search"
      },
      {
        "opinion_id": 9429805,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2344,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-hensley.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwNDQ4MDgmcz0xMDE2MTI2OSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111294+OR+9429804+OR+9429805%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111294,
        "cited_id": 107411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 109009,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 311449,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 324941,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 336263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 372580,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 422083,
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
    "date_created": "2026-07-06T00:38:19Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:38:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:38:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:41:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:38:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Hensley

```
<opinion type="majority">
<author id="b365-4"><page-number citation-index="1" label="223">*223</page-number>Justice O’Connor</author>
<p id="AXO">delivered the opinion of the Court.</p>
<p id="b365-5">We granted certiorari in this case, <span class="citation multiple-matches"><a href="/c/U.%20S./467/1203/">467 U. S. 1203</a></span> (1984), to determine whether police officers may stop and briefly detain a person who is the subject of a “wanted flyer” while they attempt to find out whether an arrest warrant has been issued. We conclude that such stops are consistent with the Fourth Amendment under appropriate circumstances.</p>
<p id="b365-6">I</p>
<p id="b365-7">On December 4, 1981, two armed men robbed a tavern in the Cincinnati suburb of St. Bernard, Ohio. Six days later, a St. Bernard police officer, Kenneth Davis, interviewed an informant who passed along information that respondent Thomas Hensley had driven the getaway car during the armed robbery. Officer Davis obtained a written statement from the informant and immediately issued a “wanted flyer” to other police departments in the Cincinnati metropolitan area.</p>
<p id="b365-8">The flyer twice stated that Hensley was wanted for investigation of an aggravated robbery. It described both Hensley and the date and location of the alleged robbery, and asked other departments to pick up and hold Hensley for the St. Bernard police in the event he were located. The flyer also warned other departments to use caution and to consider Hensley armed and dangerous.</p>
<p id="b365-9">The St. Bernard Police Department’s “wanted flyer” was received by teletype in the headquarters of the Covington Police Department on December 10,' 1981. Covington is a Kentucky suburb of Cincinnati that is approximately five miles from St. Bernard. The flyer was read aloud at each change of shift in the Covington Police Department between December 10 and December 16, 1981. Some of the Coving-ton officers were acquainted with Hensley, and after December 10 they periodically looked for him at places in Covington he was known to frequent.</p>
<p id="b365-10">On December 16, 1981, Covington Officer Terence Eger saw a white Cadillac convertible stopped in the middle of a <page-number citation-index="1" label="224">*224</page-number>Covington street. Officer Eger saw Hensley in the driver’s seat and asked him to move on. As Hensley drove away, Eger inquired by radio whether there was a warrant outstanding for Hensley’s arrest. Before the dispatcher could answer, two other Covington officers who were in separate cars on patrol interrupted to say that there might be an Ohio robbery warrant outstanding on Hensley. The officers, Daniel Cope and David Rassache, subsequently testified that they had heard or read the St. Bernard flyer on several occasions, that they recalled that the flyer sought a stop for investigation only, and that in their experience the issuance of such a flyer was usually followed by the issuance of an arrest warrant. While the dispatcher checked to see whether a warrant had been issued, Officer Cope drove to a Holman Street address where Hensley occasionally stayed, and Officer Rassache went to check a second location.</p>
<p id="b366-5">The dispatcher had difficulty in confirming whether a warrant had been issued. Unable to locate the flyer, she called the Cincinnati Police Department on the mistaken belief that the flyer had originated in Cincinnati. The Cincinnati Police Department transferred the call to its records department, which placed the dispatcher on hold. In the meantime, Officer Cope reported that he had sighted a white Cadillac approaching him on Holman Street. Cope turned on his flashing lights and Hensley pulled over to the curb. Before Cope left his patrol car, the dispatcher advised him that she had “Cincinnati hunting for the warrant,” App. 49, but that she had not yet confirmed it. Cope approached Hensley’s car with his service revolver drawn and pointed into the air. He had Hensley and a passenger seated next to him step out of the car.</p>
<p id="b366-6">Moments later, Officer Rassache arrived in his separate car. He recognized the passenger, Albert Green, a convicted felon. Rassache stepped up to the open passenger door of Hensley’s car and observed the butt of a revolver protruding from underneath the passenger’s seat. Green <page-number citation-index="1" label="225">*225</page-number>was then arrested. A search of the car uncovered a second handgun wrapped in a jacket in the middle of the front seat and a third handgun in a bag in the back seat. After the discovery of these weapons, Hensley was also arrested.</p>
<p id="b367-5">After state handgun possession charges against Hensley were dismissed, Hensley was indicted by a federal grand jury in the Eastern District of Kentucky for being a convicted felon in possession of firearms in violation of 18 U. S. C. App. § 1202(a)(1). Hensley moved to suppress the handguns from evidence on the grounds that the Covington police had imper-missibly stopped him in violation of the Fourth Amendment and the principles announced in <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). The District Judge held the stop to be proper and denied the motion. Respondent was convicted after a bench/ trial and sentenced to two years in federal prison.</p>
<p id="b367-7">The United States Court of Appeals for the Sixth Circuit reversed the conviction. <span class="citation" data-id="422083"><a href="/opinion/422083/united-states-v-thomas-j-hensley/" aria-description="Citation for case: United States v. Thomas J. Hensley">713 F. 2d 220</a></span> (1983). The panel noted that the Covington police could not justifiably conclude from the St. Bernard flyer that a warrant had been issued for Hensley’s arrest; nor could the Covington police stop the respondent while they attempted to find out whether a warrant had in fact been issued. Reviewing this Court’s decisions applying <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>the Sixth Circuit concluded that investigative stops remain a narrow exception to the probable-cause requirement, and that this Court has manifested a “clear intention to restrict investigative stops to settings involving the investigation of ongoing crimes.” <span class="citation" data-id="422083"><a href="/opinion/422083/united-states-v-thomas-j-hensley/#225" aria-description="Citation for case: United States v. Thomas J. Hensley">713 F. 2d, at 225</a></span>. Since Covington police encountered Hensley almost two weeks after the armed robbery in St. Bernard, they had no reason to believe they were investigating an ongoing crime. Because the Covington police were familiar only with the St. Bernard flyer, and not with the specific information which led the St. Bernard police to issue the flyer, the Court of Appeals held they lacked a reasonable suspicion sufficient-to justify an investigative stop. The Court of Appeals concluded that Hensley’s conviction rested on evidence obtained <page-number citation-index="1" label="226">*226</page-number>through an illegal arrest, and therefore had to be reversed. We disagree, and now reverse.</p>
<p id="b368-5">II</p>
<p id="b368-6">The Fourth Amendment protects the right of the people to be secure in their persons, houses, papers, and effects against unreasonable searches and seizures. In <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry, supra,</a></span> </em>and subsequent cases, this Court has held that, consistent with the Fourth Amendment, police may stop persons in the absence of probable cause under limited circumstances. See <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#207" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 207-211</a></span> (1979). In particular, the Court has noted that law enforcement agents may briefly stop a moving automobile to investigate a reasonable suspicion that its occupants are involved in criminal activity. See <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 881</a></span> (1975) (within United States borders, Government interest in preventing illegal entry of aliens permits a <em>Terry </em>stop on reasonable suspicion that particular vehicle contains aliens). Although stopping a car and detaining its occupants constitute a seizure within the meaning of the Fourth Amendment, the governmental interest in investigating an officer’s reasonable suspicion, based on specific and articulable facts, may outweigh the Fourth Amendment interest of the driver and passengers in remaining secure from the intrusion. See <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#653" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 653-655</a></span> (1979).</p>
<p id="b368-7">In this case, the Sixth Circuit announced two prerequisites to such an investigatory stop and held that they were lacking: first, the crime being investigated was not imminent or ongoing, but rather was already completed; second, the “wanted flyer” was insufficient to create a reasonable suspicion that respondent had engaged in criminal activity. If either part of this analysis is correct, then it was indeed improper to stop respondent, and his conviction cannot stand. We accordingly turn to the separate but related issues of <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stops to investigate completed crimes and <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stops in reliance on another police department’s “wanted flyer.”</p>
<p id="b369-4"><page-number citation-index="1" label="227">*227</page-number>A</p>
<p id="b369-5">This is the first case we have addressed in which police stopped a person because they suspected he was involved in a completed crime. In our previous decisions involving investigatory stops on less than probable cause, police stopped or seized a person because they suspected he was about to commit a crime, <em>e. g., <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry, supra,</a></span> </em>or was committing a crime at the moment of the stop, <em>e. g., Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972). Noting that <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983), struck down a particularly intrusive detention of a person suspected of committing an ongoing crime, the Court of Appeals in this case concluded that we clearly intended to restrict investigative stops to the context of ongoing crimes.</p>
<p id="b369-6">We do not agree with the Court of Appeals that our prior opinions contemplate an inflexible rule that precludes police from stopping persons they suspect of past criminal activity unless they have probable cause for arrest. To the extent previous opinions have addressed the issue at all, they have suggested that some investigative stops based on a reasonable suspicion of past criminal activity could withstand Fourth Amendment scrutiny. Thus <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 417, n. 2</a></span> (1981), indicates in a footnote that “[o]f course, an officer may stop and question a person if there are reasonable grounds to believe that person is wanted for past criminal conduct.” And in <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983), decided barely a month before the Sixth Circuit’s opinion, this Court stated that its prior opinions acknowledged police authority to stop a person “when the officer has reasonable, articulable suspicion that the person <em>has been, </em>is, or is about to be engaged in criminal activity.” <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#702" aria-description="Citation for case: United States v. Place"><em>Id., </em>at 702</a></span> (emphasis added). See also <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#699" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 699</a></span>, and n. 7 (1981). Indeed, <em>Florida </em>v. <em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span> </em>itself suggests that certain seizures are justifiable under the Fourth Amendment even in the absence of probable cause “if there is articulable suspicion that a person <em>has committed </em>or is about to commit a crime.” <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#498" aria-description="Citation for case: Florida v. Royer">460 U. S., at 498</a></span> (plurality opinion) (emphasis added).</p>
<p id="b370-4"><page-number citation-index="1" label="228">*228</page-number>At the least, these dicta suggest that the police are not automatically shorn of authority to stop a suspect in the absence of probable cause merely because the criminal has completed his crime and escaped from the scene. The precise limits on investigatory stops to investigate past criminal activity are more difficult to define. The proper way to identify the limits is to apply the same test already used to identify the proper bounds of intrusions that further investigations of imminent or ongoing crimes. That test, which is grounded in the standard of reasonableness embodied in the Fourth Amendment, balances the nature and quality of the intrusion on personal security against the importance of the governmental interests alleged to justify the intrusion. <em>United States </em>v. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place"><em>Place, supra, </em>at 703</a></span>; <em>Michigan </em>v. <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#698" aria-description="Citation for case: Michigan v. Summers"><em>Summers, supra, </em>at 698-701</a></span>. When this balancing test is applied to stops to investigate past crimes, we think that probable cause to arrest need not always be required.</p>
<p id="b370-5">The factors in the balance may be somewhat different when a stop to investigate past criminal activity is involved rather than a stop to investigate ongoing criminal conduct. This is because the governmental interests and the nature of the intrusions involved in the two situations may differ. As we noted in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>one general interest present in the context of ongoing or imminent criminal activity is “that of effective crime prevention and detection.” <em>Terry, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 22</a></span>. A stop to investigate an already completed crime does not necessarily promote the interest of crime prevention as directly as a stop to investigate suspected ongoing criminal activity. Similarly, the exigent circumstances which require a police officer to step in before a crime is committed or completed are not necessarily as pressing long afterwards. Public safety may be less threatened by a suspect in a past crime who now appears to be going about his lawful business than it is by a suspect who is currently in the process of violating the law. Finally, officers making a stop to investigate past crimes may have a wider range of opportunity to <page-number citation-index="1" label="229">*229</page-number>choose the time and circumstances of the stop. See <em>Brown </em>v. <em>Texas, </em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 51</a></span> (1979); ALI Model Code of Pre-Arraignment Procedure 12 (Prop. Off. Draft No. 1, 1972).</p>
<p id="b371-5">Despite these differences, where police have been unable to locate a person suspected of involvement in a past crime, the ability to briefly stop that person, ask questions, or check identification in the absence of probable cause promotes the strong government interest in solving crimes and bringing offenders to justice. Restraining police action until after probable cause is obtained would not only hinder the investigation, but might also enable the suspect to flee in the interim and to remain at large. Particularly in the context of felonies or crimes involving a threat to public safety, it is in the public interest that the crime be solved and the suspect detained as promptly as possible. The law enforcement interests at stake in these circumstances outweigh the individual’s interest to be free of a stop and detention that is no more extensive than permissible in the investigation of imminent or ongoing crimes.</p>
<p id="b371-6">We need not and do not decide today whether <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stops to investigate all past crimes, however serious, are permitted. It is enough to say that, if police have a reasonable suspicion, grounded in specific and articulable facts, that a person they encounter was involved in or is wanted in connection with a completed felony, then a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop may be made to investigate that suspicion. The automatic barrier to such stops erected by the Court of Appeals accordingly cannot stand.</p>
<p id="b371-7">B</p>
<p id="b371-8">At issue in this case is a stop of a person by officers of one police department in reliance on a flyer issued by another department indicating that the person is wanted for investigation of a felony. The Court of Appeals concluded that “the Fourth Amendment does not permit police officers in one department to seize a person simply because a neighboring <page-number citation-index="1" label="230">*230</page-number>police department has circulated a flyer reflecting the desire to question that individual about some criminal investigation that does not involve the arresting officers or their department.” <span class="citation" data-id="422083"><a href="/opinion/422083/united-states-v-thomas-j-hensley/#225" aria-description="Citation for case: United States v. Thomas J. Hensley">713 F. 2d, at 225</a></span>. This holding apparently rests on the omission from the flyer of the specific and articulable facts which led the first department to suspect respondent’s involvement in a completed crime. <em><span class="citation" data-id="422083"><a href="/opinion/422083/united-states-v-thomas-j-hensley/" aria-description="Citation for case: United States v. Thomas J. Hensley">Ibid.</a></span></em></p>
<p id="b372-5">This Court discussed a related issue in <em>Whiteley </em>v. <em>Warden, </em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560</a></span> (1971). In <em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span>, </em>a county sheriff in Wyoming obtained an arrest warrant for a person suspected of burglary. The sheriff then issued a message through a statewide law enforcement radio network describing the suspect, his car, and the property taken. At least one version of the message also indicated that a warrant had been issued. <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#564" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary"><em>Id., </em>at 564</a></span>, and n. 5. The message did not specify the evidence that gave the sheriff probable cause to believe the suspect had committed the breaking and entering. In reliance on the radio message, police in Laramie stopped the suspect and searched his car. The Supreme Court, in an opinion by Justice Harlan, ultimately concluded that the sheriff had lacked probable cause to obtain the warrant and that the evidence obtained during the search by the police in Laramie had to be excluded. In so ruling, however, the Court noted:</p>
<blockquote id="b372-6">“We do not, of course, question that the Laramie police were entitled to act on the strength of the radio bulletin. Certainly police officers called upon to aid other officers in executing arrest warrants are entitled to assume that the officers requesting aid offered the magistrate the information requisite to support an independent judicial assessment of probable cause. Where, however, the contrary turns out to be true, an otherwise illegal arrest cannot be insulated from challenge by the decision of the instigating officer to rely on fellow officers to make the arrest.” <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#568" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary"><em>Id., </em>at 568</a></span>.</blockquote>
<p id="b372-7">This language in <em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span> </em>suggests that, had the sheriff who issued the radio bulletin possessed probable cause for <page-number citation-index="1" label="231">*231</page-number>arrest, then the Laramie police could have properly arrested the defendant even though they were unaware of the specific facts that established probable cause. See <em>United States </em>v. <em>Maryland, </em><span class="citation" data-id="311449"><a href="/opinion/311449/united-states-v-napoleon-maryland-jr/#569" aria-description="Citation for case: United States v. Napoleon Maryland, Jr.">479 F. 2d 566, 569</a></span> (CA5 1973). Thus <em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span> </em>supports the proposition that, when evidence is uncovered during a search incident to an arrest in reliance merely on a flyer or bulletin, its admissibility turns on whether the officers who <em>issued </em>the flyer possessed probable cause to make the arrest. It does not turn on whether those relying on the flyer were themselves aware of the specific facts which led their colleagues to seek their assistance. In an era when criminal suspects are increasingly mobile and increasingly likely to flee across jurisdictional boundaries, this rule is a matter of common sense: it minimizes the volume of information concerning suspects that must be transmitted to other jurisdictions and enables police in one jurisdiction to act promptly in reliance on information from another jurisdiction.</p>
<p id="b373-5">Neither respondent nor the Court of Appeals suggests any reason why a police department should be able to act on the basis of a flyer indicating that another department has a warrant, but should not be able to act on the basis of a flyer indicating that another department has a reasonable suspicion of involvement with a crime. Faced with this precise issue, the Court of Appeals for the Ninth Circuit applied <em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span> </em>and concluded that, although the officer who issues a wanted bulletin must have a reasonable suspicion sufficient to justify a stop, the officer who acts in reliance on the bulletin is not required to have personal knowledge of the evidence creating a reasonable suspicion. <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9462804"><a href="/opinion/336263/united-states-v-steven-linwood-robinson/#1300" aria-description="Citation for case: United States v. Steven Linwood Robinson">536 F. 2d 1298, 1300</a></span> (1976). The Ninth Circuit there noted “that effective law enforcement cannot be conducted unless police officers can act on directions and information transmitted by one officer to another and that officers, who must often act swiftly, cannot be expected to cross-examine their fellow officers about the foundation for the transmitted information.” <span class="citation" data-id="9462804"><a href="/opinion/336263/united-states-v-steven-linwood-robinson/#1299" aria-description="Citation for case: United States v. Steven Linwood Robinson"><em>Id., </em>at 1299</a></span>.</p>
<p id="b374-4"><page-number citation-index="1" label="232">*232</page-number>It could be argued that police can more justifiably rely on a report that a magistrate has issued a warrant than on a report that another law enforcement agency has simply concluded that it has a reasonable suspicion sufficient to authorize an investigatory stop. We do not find this distinction significant. The law enforcement interests promoted by allowing one department to make investigatory stops based upon another department’s bulletins or flyers are considerable, while the intrusion on personal security is minimal. The same interests that weigh in favor of permitting police to make a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop to investigate a past crime, <em>swpra, </em>at 229, support permitting police in other jurisdictions to rely on flyers or bulletins in making stops to investigate past crimes.</p>
<p id="b374-5">We conclude that, if a flyer or bulletin has been issued on the basis of articulable facts supporting a reasonable suspicion that the wanted person has committed an offense, then reliance on that flyer or bulletin justifies a stop to check identification, see <em>United States ex rel. Kirby </em>v. <em>Sturges, </em><span class="citation" data-id="324941"><a href="/opinion/324941/united-states-of-america-ex-rel-thomas-kirby-v-david-r-sturges-chairman/#400" aria-description="Citation for case: United States of America Ex Rel. Thomas Kirby v. David R....">510 F. 2d 397, 400-401</a></span> (CA7) (Stevens, J.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./421/1016/">421 U. S. 1016</a></span> (1975), to pose questions to the person, or to detain the person briefly while attempting to obtain further information. See <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 146</a></span> (1972) (“A brief stop of a suspicious individual, in order to determine his identity or to maintain the status quo momentarily while obtaining more information, may be the most reasonable in light of the facts known to the officer at the time”). If the flyer has been issued in the absence of a reasonable suspicion, then a stop in the objective reliance upon it violates the Fourth Amendment. In such a situation, of course, the officers making the stop may have a good-faith defense to any civil suit. See <em>Scheuer </em>v. <em>Rhodes, </em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232</a></span> (1974); <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547</a></span> (1967); <em>Turner </em>v. <em>Raynes, </em><span class="citation" data-id="372580"><a href="/opinion/372580/jack-e-turner-v-e-t-raynes-and-bill-edd-jones/#93" aria-description="Citation for case: Jack E. Turner v. E. T. Raynes and Bill Edd Jones">611 F. 2d 92, 93</a></span> (CA5) (officer relying in good faith on an invalid arrest warrant has defense to civil suit), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/900/">449 U. S. 900</a></span> (1980). It is the objective reading of the flyer or bulletin that determines whether other <page-number citation-index="1" label="233">*233</page-number>police officers can defensibly act in reliance on it. Cf. Terry, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 21-22</a></span> (“it is imperative that the facts be judged against an objective standard: would the facts available to the officer at the moment of the seizure or the search ‘warrant a man of reasonable caution in the belief’ that the action taken was appropriate?”). Assuming the police make a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop in objective reliance on a flyer or bulletin, we hold that the evidence uncovered in the course of the stop is admissible if the police who <em>issued </em>the flyer or bulletin possessed a reasonable suspicion justifying a stop, <em>United States </em>v. <em><span class="citation" data-id="9462804"><a href="/opinion/336263/united-states-v-steven-linwood-robinson/" aria-description="Citation for case: United States v. Steven Linwood Robinson">Robinson, supra,</a></span> </em>and if the stop that in fact occurred was not significantly more intrusive than would have been permitted the issuing department.</p>
<p id="b375-8">H-I ► — i I — f</p>
<p id="b375-3">It remains to apply the two sets of principles described above to the stop and subsequent arrest of respondent Hensley.</p>
<p id="b375-4">At the outset, we assume, <em>arguendo, </em>that the St. Bernard police who issued the “wanted flyer” on Hensley lacked probable cause for his arrest. The District Court implied that the St. Bernard police had probable cause for arrest, but held only that the St. Bernard officers had reasonable suspicion sufficient to justify a stop. App. to Pet. for Cert. 14a. The Court of Appeals implied that probable cause might be lacking, <span class="citation" data-id="422083"><a href="/opinion/422083/united-states-v-thomas-j-hensley/#223" aria-description="Citation for case: United States v. Thomas J. Hensley">713 F. 2d, at 223</a></span>, but ultimately concluded that the question was irrelevant because the Covington police would not be entitled to make an arrest or a stop regardless of whether the St. Bernard police possessed probable cause or a reasonable suspicion. In this Court, no party contends that the St. Bernard police had probable cause to arrest Hensley.</p>
<p id="b375-5">We agree with the District Court that the St. Bernard police possessed a reasonable suspicion, based on specific and articulable facts, that Hensley was involved in an armed robbery. The District Judge heard testimony from the St. Bernard officer who interviewed the informant. On the strength of the evidence, the District Court concluded <page-number citation-index="1" label="234">*234</page-number>that the wealth of detail concerning the robbery revealed by the informant, coupled with her admission of tangential participation in the robbery, established that the informant was sufficiently reliable and credible “to arouse a reasonable suspicion of criminal activity by [Hensley] and to constitute the specific and articulable facts needed to underly a stop.” App. to Pet. for Cert. 14a. Under the circumstances, “the information carried enough indicia of reliability,” <em>Adams </em>v. <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#147" aria-description="Citation for case: Adams v. Williams"><em>Williams, supra, </em>at 147</a></span>, to justify an investigatory stop of Hensley.</p>
<p id="b376-5">The justification for a stop did not evaporate when the armed robbery was completed. Hensley was reasonably suspected of involvement in a felony and was at large from the time the suspicion arose until the stop by the Covington police. A brief stop and detention at the earliest opportunity after the suspicion arose is fully consistent with the principles of the Fourth Amendment.</p>
<p id="b376-6">Turning to the flyer issued by the St. Bernard police, we believe it satisfies the objective test announced today. An objective reading of the entire flyer would lead an experienced officer to conclude that Thomas Hensley was at least wanted for questioning and investigation in St. Bernard. Since the flyer was issued on the basis of articulable facts supporting a reasonable suspicion, this objective reading would justify a brief stop to check Hensley’s identification, pose questions, and inform the suspect that the St. Bernard police wished to question him. As an experienced officer could well assume that a warrant might have been obtained in the period after the flyer was issued, we think the flyer would further justify a brief detention at the scene of the stop while officers checked whether a warrant had in fact been issued. It is irrelevant whether the Covington officers intended to detain Hensley only long enough to confirm the existence of a warrant, or for some longer period; what matters is that the stop and detention that occurred were <page-number citation-index="1" label="235">*235</page-number>in fact no more intrusive than would have been permitted an experienced officer on an objective reading of the flyer.</p>
<p id="b377-5">To be sure, the St. Bernard flyer at issue did not request that other police departments briefly detain Hensley merely to check his identification or confirm the existence of a warrant. Instead, it asked other departments to pick up and hold Hensley for St. Bernard. Our decision today does not suggest that such a detention, whether at the scene or at the Covington police headquarters, would have been justified. Given the distance involved and the time required to identify and communicate with the department that issued the flyer, such a detention might well be so lengthy or intrusive as to exceed the permissible limits of a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop. See <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place">462 U. S., at 709</a></span>. Nor do we mean to endorse St. Bernard’s request in its flyer for actions that could forseeably violate the Fourth Amendment. We hold only that this flyer, objectively read and supported by a reasonable suspicion on the part of the issuing department, justified the length and intrusiveness of the stop and detention that actually occurred.</p>
<p id="b377-6">When the Covington officers stopped Hensley, they were authorized to take such steps as were reasonably necessary to protect their personal safety and to maintain the status quo during the course of the stop. The Covington officers’ conduct was well within the permissible range in the context of suspects who are reported to be armed and dangerous. See <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1049" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1049-1050</a></span> (1983); <em>Pennsylvania </em>v. <em>Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#110" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 110-111</a></span> (1977) <em>(per curiam). </em>Having stopped Hensley, the Covington police were entitled to seize evidence revealed in plain view in the course of the lawful stop, to arrest Hensley’s passenger when evidence discovered in plain view gave probable cause to believe the passenger had committed a crime, <em>Texas </em>v. <em>Brown, </em><span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/" aria-description="Citation for case: Texas v. Brown">460 U. S. 730</a></span> (1983) (plurality opinion), and subsequently to search the passenger compartment of the car because it was within the passenger’s immediate control. <em>New York </em><page-number citation-index="1" label="236">*236</page-number>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981). Finally, having discovered additional weapons in Hensley’s car during the course of a lawful search, the Covington officers had probable cause to arrest Hensley himself for possession of firearms.</p>
<p id="b378-5">The length of Hensley’s detention from his stop to his arrest on probable cause was brief. A reasonable suspicion on the part of the St. Bernard police underlies and supports their issuance of the flyer. Finally, the stop that occurred was reasonable in objective reliance on the flyer and was not significantly more intrusive than would have been permitted the St. Bernard police. Under these circumstances, the investigatory stop was reasonable under the Fourth Amendment, and the evidence discovered during the stop was admissible.</p>
<p id="b378-6">The judgment of the Court of Appeals is reversed, and the case is remanded for proceedings consistent with this opinion.</p>
<p id="b378-7">
<em>It is so ordered.</em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Howard Davis.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "United States v. Howard Davis"
type: case
citation: "997 F.3d 191 (2021)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, Fourth Circuit"
court_level: coa
circuit: 4th
year: 2021
date_decided: 2021-05-07
docket: ""
authority_weight: "Binding in-circuit — 4th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2021-05-07
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Howard Davis
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4881258/united-states-v-howard-davis/"
  cluster_id: 4881258
  opinion_id: 4685037
  identity_checked: true
homes:
  - page: "[[SIA Vehicles]]"
    role: "Lower-court development (role-based)"
related: ["[[Arizona v. Gant]]", "[[Chimel v. California]]"]
aliases: ["United States v. Howard Davis (4th Cir. 2021)"]
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "gant", "container-search", "reaching-distance", "fourth-circuit"]
holding: "Gant's FIRST holding (the Chimel reachability/officer-safety prong) applies OUTSIDE the vehicle context — to non-vehicular containers…"
lake:
  record_id: United States v. Howard Davis
  status: verified
  projected_at: 2026-07-06
---

# United States v. Howard Davis

*997 F.3d 191 (4th Cir. 2021)* · U.S. Court of Appeals, Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Holly Springs, North Carolina officer stopped Howard Davis's car for a window-tint violation and arrested him. While Davis was handcuffed with his hands behind his back and lying on his stomach, police searched his nearby backpack and found contraband. The district court denied suppression; Davis appealed, arguing that [[Arizona v. Gant]]'s "reaching distance" limit on [[Search Incident to Arrest|searches incident to arrest]] applied to his backpack, not just to vehicles.

## Issue
Whether the first holding of [[Arizona v. Gant]] — that a [[Search Incident to Arrest|search incident to arrest]] is justified only where the arrestee is unsecured and within reaching distance of the area searched — applies outside the automobile context, to a non-vehicular container such as a backpack.

## Rule
Yes. The officer-safety/evidence-preservation limit of *[[Arizona v. Gant|Gant]]*'s first holding is not confined to vehicles, because it rests on the rationale of [[Chimel v. California]], a non-vehicle case. The Fourth Circuit held: "Accordingly, we conclude that the first *Gant* holding applies to searches of non-vehicular containers and conclude that police officers can conduct warrantless searches of non-vehicular containers incident to a lawful arrest 'only when the arrestee is unsecured and within reaching distance of the [container] at the time of the search.'" — 997 F.3d at 196 (quoting *Gant*, 556 U.S. at 343). ^pin-196

The court distinguished *[[Arizona v. Gant|Gant]]*'s *second* holding (the evidence-of-the-offense rationale), which the Supreme Court expressly tied to "circumstances unique to the vehicle context" and said "d[id] not follow from *Chimel*." Joining "several sister circuits," it answered the cross-context question "yes."

## Application
On these facts the search could not be sustained as a [[Search Incident to Arrest|search incident to arrest]] under the rule the court adopted. Because Davis was already handcuffed with his hands behind his back and lying on his stomach when officers searched the backpack, the validity of the search turned on whether it was reasonable for the officer "to believe that Davis 'could have accessed [the backpack] at the time of the search.'" Applying *[[Arizona v. Gant|Gant]]*'s first holding to that non-vehicular container, the court held the district court erred in denying suppression and [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]] for further proceedings consistent with the reaching-distance standard.

## Conclusion
*[[Arizona v. Gant|Gant]]*'s first holding governs searches of non-vehicular containers incident to arrest; because Davis was secured and not within reaching distance of the backpack, the denial of suppression was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 4th Cir.**
- No negative subsequent treatment identified. The decision extends the first holding of [[Arizona v. Gant]] — rooted in [[Chimel v. California]] — beyond vehicles to non-vehicular containers, joining sister circuits on that question.

## Appears on
- [[SIA Vehicles]] — *Lower-court development (role-based)*

## Sources
- *United States v. Howard Davis*, 997 F.3d 191 (4th Cir. 2021) — https://www.courtlistener.com/opinion/4881258/united-states-v-howard-davis/ — pinpoint: 196. (CL's copy is the court's slip-opinion PDF without F.3d star-pagination; the 196 pinpoint is the standard reporter pinpoint for the holding — quotes verbatim-verified against the opinion text; lead opinion id 4685037.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "82aef7dfa247a353", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Howard Davis"}, "payload": {"all": [{"cite": "997 F.3d 191", "page": "191", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "997"}], "display": "997 F.3d 191", "official": {"cite": "997 F.3d 191", "page": "191", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "997"}, "official_selection_present": true, "record_id": "United States v. Howard Davis"}}
{"assertion_id": "a38251a404a649c4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-196", "record_id": "United States v. Howard Davis"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-196", "pinpoint_status": "slip-only", "quote": "limit on searches incident to arrest applied to his backpack, not just to vehicles. ## Issue Whether the first holding of [[Arizona v. Gant]] — that a search incident to arrest is justified only where the arrestee is unsecured and within reaching distance of the area searched — applies outside the automobile context, to a non-vehicular container such as a backpack. ## Rule Yes. The officer-safety/evidence-preservation limit of *Gant*'s first holding is not confined to vehicles, because it rests on the rationale of [[Chimel v. California]], a non-vehicle case. The Fourth Circuit held:", "quote_fidelity": "mismatch", "record_id": "United States v. Howard Davis", "star_marker": null}}
{"assertion_id": "8666353843cba68e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Howard Davis"}, "payload": {"as_of_content": "2021-05-07", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Howard Davis", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Howard Davis

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Howard Davis",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Howard Davis",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Howard Davis",
    "court": "U.S. Court of Appeals, Fourth Circuit",
    "court_id": "ca4",
    "court_level": "coa",
    "circuit": "4th",
    "state": null,
    "date_decided": "2021-05-07",
    "year": 2021,
    "docket": null,
    "cluster_id": 4881258,
    "lead_opinion_id": 4685037,
    "sibling_ids": [
      4685037
    ],
    "absolute_url": "/opinion/4881258/united-states-v-howard-davis/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "997 F.3d 191",
      "volume": "997",
      "reporter": "F.3d",
      "page": "191",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "997 F.3d 191",
        "volume": "997",
        "reporter": "F.3d",
        "page": "191",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "997 F.3d 191",
    "official_selection": {
      "court_class": "coa",
      "selected": "997 F.3d 191",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-196",
      "page": null,
      "quote": "limit on searches incident to arrest applied to his backpack, not just to vehicles. ## Issue Whether the first holding of [[Arizona v. Gant]] \u2014 that a search incident to arrest is justified only where the arrestee is unsecured and within reaching distance of the area searched \u2014 applies outside the automobile context, to a non-vehicular container such as a backpack. ## Rule Yes. The officer-safety/evidence-preservation limit of *Gant*'s first holding is not confined to vehicles, because it rests on the rationale of [[Chimel v. California]], a non-vehicle case. The Fourth Circuit held:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2021-05-07",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Howard Davis",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Anthony Caldwell",
          "cluster_id": 4904976,
          "cite": [
            "7 F.4th 191"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Buster",
          "cluster_id": 7454472,
          "cite": [
            "26 F.4th 627"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Perez",
          "cluster_id": 9456060,
          "cite": [
            "89 F.4th 247"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Quentin Horsley",
          "cluster_id": 9834245,
          "cite": [
            "105 F.4th 193"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Arnez Salazar",
          "cluster_id": 9403945,
          "cite": [
            "69 F.4th 474"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Milton Allen",
          "cluster_id": 10850525,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Greenfield v. United States",
          "cluster_id": 10375920,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Alexander Soto",
          "cluster_id": 10281513,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Patrick Scullark",
          "cluster_id": 10047256,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Buster",
          "cluster_id": 6444299,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4685037) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca4)",
        "reviewed": 5,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 5,
        "triage_read": 0,
        "triage_snippet_classified": 5
      },
      "lane2_top_cited": {
        "query": "cites:(4685037)",
        "reviewed": 10,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 10,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(4685037)",
        "reviewed": 6,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 6,
        "triage_read": 0,
        "triage_snippet_classified": 6
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4685037)",
    "indexed_citing_opinions": 10,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4685037,
        "count": 10,
        "count_source": "search"
      }
    ],
    "citation_count": 19,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-howard-davis.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 10,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4685037,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 152638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 187527,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 212206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 783712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 812859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 1031354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 1207926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 1854815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 2642900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 3149060,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 4350875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 4373735,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 4409493,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 4527868,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 4669653,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 7263677,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 8182816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 8413755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9423434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9424643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9425474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9428488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9430011,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9433305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9433386,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9434613,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9435359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9438355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9822018,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9841975,
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
    "date_created": "2026-07-06T00:41:37Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:41:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:41:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:43:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:41:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Howard Davis

```
                                      PUBLISHED

                       UNITED STATES COURT OF APPEALS
                           FOR THE FOURTH CIRCUIT


                                       No. 20-4035


UNITED STATES OF AMERICA,

                     Plaintiff - Appellee,

              v.

HOWARD DAVIS,

                     Defendant - Appellant.


Appeal from the United States District Court for the Eastern District of North Carolina, at
Raleigh. James C. Dever III, District Judge. (5:17–cr–00174–D–1)


Argued: January 26, 2021                                           Decided: May 7, 2021


Before GREGORY, Chief Judge, WYNN and THACKER, Circuit Judges.


Reversed and remanded by published opinion. Judge Wynn wrote the opinion, in which
Chief Judge Gregory and Judge Thacker joined.


ARGUED: Marvin D. Miller, THE LAW OFFICES OF MARVIN D. MILLER,
Alexandria, Virginia, for Appellant. Joshua L. Rogers, OFFICE OF THE UNITED
STATES ATTORNEY, Raleigh, North Carolina, for Appellee. ON BRIEF: Robert J.
Higdon, Jr., United States Attorney, Jennifer P. May-Parker, Assistant United States
Attorney, Gabriel J. Diaz, Assistant United States Attorney, OFFICE OF THE UNITED
STATES ATTORNEY, Raleigh, North Carolina, for Appellee.
WYNN, Circuit Judge:

         In Arizona v. Gant, the Supreme Court held that incident to an arrest, a vehicle may

be searched without a warrant if it was reasonable for the police to believe that the arrestee

“could have accessed his car at the time of the search.” 556 U.S. 332, 344 (2009). Here,

while Davis was handcuffed with his hands behind his back and lying on his stomach, the

police searched his nearby backpack.

         The issue we confront in this appeal is whether the Supreme Court’s holding in Gant

applies beyond the automobile context to the search of a backpack. We join several sister

circuits in answering, yes. Accordingly, we vacate and remand this matter to the district

court for further proceedings consistent with this opinion.

                                                I.

         On March 1, 2017, at around 2:45 pm, police officer Derek Richardson of the Holly

Springs, North Carolina Police Department stopped a gray Honda Accord driven by

defendant Howard Davis because he believed that the vehicle’s windows were tinted too

dark in violation of North Carolina law. Richardson approached Davis and explained that

he had pulled Davis over because of the vehicle’s window tint and obtained Davis’s license

and proof of insurance. A search of the relevant databases revealed that Davis’s license

was valid and that he “had a history of felony drug charges and convictions.” J.A. 141. 1




1
    Citations to “J.A. __” refer to the Joint Appendix filed by the parties in this appeal.


                                                2
       Two additional uniformed officers, David Veiling 2 and Paul Boyd, arrived in a

separate patrol car, parked behind Richardson’s vehicle, and activated their car’s lights.

About three minutes into the stop, while Richardson talked with the other two officers,

Davis put his hand out of his window and “ma[de] a pointing gesture indicating that he was

leaving.” J.A. 142. Davis then drove off without his license or proof of insurance, which

were still in Richardson’s possession.

       The officers gave chase. Davis raced through a residential neighborhood, at times

reaching speeds of up to 50 miles per hour—double the neighborhood’s speed limit. The

pursuit continued until Davis reached a dead-end cul-de-sac, drove in between two houses

and into someone’s backyard, got out of his vehicle carrying a backpack, ran on foot into

a swamp, and got stuck in knee-high water. Richardson, also on foot and roughly seven to

ten yards behind Davis, drew his service weapon and ordered Davis to come out of the

swamp. Davis complied by returning to dry land, dropping the backpack, and lying down

on his stomach.

       Richardson patted Davis down and found a large amount of cash on Davis’s person.

Richardson then handcuffed Davis’s hands behind his back and placed him under arrest for

“several traffic violations, including felony flee to elude.” J.A. 61–62.




2
  The record reflects two different spellings of Veiling’s surname. We use the spelling
found in the government’s briefing.


                                              3
       Afterwards, Richardson unzipped the closed backpack and discovered “large

amounts of cash and two plastic bags containing what appeared to be cocaine.” 3 J.A. 143.

A search of Davis’s vehicle revealed a digital scale, a bag containing bundles of cash, and

other items. The officers also received a report that a witness had observed Davis toss a

firearm out of his car window while fleeing. Acting on this information, the officers

recovered a .45 caliber handgun from Davis’s path of flight through the residential area.

       On June 7, 2017, a federal grand jury returned a three-count indictment charging

Davis with possession with intent to distribute twenty-eight grams or more of cocaine base

and an unspecified quantity of cocaine, in violation of 21 U.S.C. § 841(a)(1) (Count I);

possession of a firearm in furtherance of a drug trafficking offense, in violation of 18

U.S.C. § 924(c) (Count II); and being a felon in possession of a firearm, in violation of 18

U.S.C. §§ 922(g)(1) and 924 (Count III).

       Before trial, Davis filed a motion to suppress, contending that the evidence seized

from his backpack and vehicle should be suppressed because the officers’ warrantless

searches violated his rights under the Fourth Amendment. The district court denied Davis’s

motion.

       On September 11, 2018, a jury returned a guilty verdict on all three Counts. After

dismissing Davis’s felon-in-possession conviction, 4 the district court sentenced Davis to


3
  Subsequent testing confirmed that these bags contained “approximately 28 grams of
cocaine base and approximately 178 grams of cocaine.” J.A. 143–44.
4
  Davis filed a motion for a new trial on Count III in light of the Supreme Court’s decision
in Rehaif v. United States, 139 S. Ct. 2191 (2019). The government responded that it would


                                             4
420 months imprisonment on the remaining counts: 360 months on Count I, followed by

60 months on Count II, to be served consecutively. Davis timely filed a notice of appeal.

                                             II.

       On appeal of the district court’s denial of Davis’s motion to suppress, we review

legal conclusions de novo and factual findings for clear error, and we construe all evidence

in the light most favorable to the government. United States v. Vaughan, 700 F.3d 705, 709

(4th Cir. 2012).

                                             A.

       The Fourth Amendment guarantees “[t]he right of the people to be secure in their

persons, houses, papers, and effects, against unreasonable searches and seizures.” U.S.

Const. amend. IV. “‘A warrantless search by the police is invalid unless it falls within one

of the narrow and well-delineated exceptions’ to the Fourth Amendment’s warrant

requirement.” United States v. Ferebee, 957 F.3d 406, 418 (4th Cir. 2020) (quoting Flippo

v. West Virginia, 528 U.S. 11, 13 (1999) (per curiam)). “The government bears the burden

of proof in justifying a warrantless search or seizure.” United States v. McGee, 736 F.3d

263, 269 (4th Cir. 2013).

       One exception to the warrant requirement authorizes searches incident to a lawful

arrest. United States v. Robinson, 414 U.S. 218, 224 (1973). The search-incident-to-arrest

exception allows arresting officers to search both “the arrestee’s person and the area ‘within




dismiss the Count in light of the Rehaif issue. As such, the district court dismissed Count
III.

                                              5
his immediate control.’” Davis v. United States, 564 U.S. 229, 232 (2011) (quoting Chimel

v. California, 395 U.S. 752, 763 (1969)).

       This exception has its origins in Weeks v. United States, a 1914 decision in which

the Supreme Court acknowledged the government’s “right”—which had “always” been

“recognized under English and American law”—to “search the person of the accused when

legally arrested to discover and seize the fruits or evidences of crime.” 232 U.S. 383, 392

(1914).

       More than a half-century later, the Court expounded on the principles underlying

the exception in its 1969 decision in Chimel v. California. In that case, police officers

engaged in a warrantless search of the defendant’s entire home, including his attic and

garage. 395 U.S. at 753–54. The officers justified the search as a search incident to arrest.

Id. at 754–55.

       In articulating the limits of the search-incident-to-arrest exception, the Supreme

Court emphasized that it was “reasonable” for arresting officers to search the person being

arrested and the area within his reach (1) “in order to remove any weapons that the

[arrestee] might seek to use in order to resist arrest or effect his escape” and (2) “in order

to prevent [the] concealment or destruction” of evidence. Id. at 763. The Court concluded

that there was therefore “ample justification . . . for a search of [(1)] the arrestee’s person

and [(2)] the area ‘within his immediate control’—construing that phrase to mean the area

from within which he might gain possession of a weapon or destructible evidence.” Id. But




                                              6
because there was “no constitutional justification” for the warrantless search of the

defendant’s entire home, the Court held the search in Chimel to be unreasonable. Id. at 768.

       Four years later, the Supreme Court again considered the boundaries of the

exception in United States v. Robinson. There, an officer patted down the defendant during

his arrest. 414 U.S. at 220–23. The pat-down search revealed a crumpled cigarette package

containing fourteen capsules of heroin. Id. at 223. Although the arresting officer expressed

no subjective concerns about his safety or the preservation of evidence, the Court held that

the search of the defendant’s person was permissible because “[a] custodial arrest of a

suspect based on probable cause is a reasonable intrusion under the Fourth Amendment,”

and “that intrusion being lawful, a search incident to the arrest requires no additional

justification.” Id. at 235–36. As to the cigarette package, the Court held that because the

officer discovered the package “in the course of a lawful search,” the officer was “entitled

to inspect it; and when his inspection revealed the heroin capsules, he was entitled to seize

them as ‘fruits, instrumentalities, or contraband’ probative of criminal conduct.” Id. at 236

(quoting Warden v. Hayden, 387 U.S. 294, 307 (1967)).

       In 1981, the Supreme Court issued its opinion in New York v. Belton. An officer

arrested the four occupants of a vehicle for possession of marijuana. 453 U.S. 454, 455–56

(1981). While searching the car, the officer unzipped a jacket pocket he found in the back

seat and discovered cocaine. Id. at 456. Recognizing that “courts have found no workable

definition of ‘the area within the immediate control of the arrestee’ when that area arguably

includes the interior of an automobile and the arrestee is its recent occupant,” the Court

held that “when a policeman has made a lawful custodial arrest of the occupant of an


                                             7
automobile, he may, as a contemporaneous incident of that arrest, search the passenger

compartment of that automobile.” Id. at 460.

       Over time, the Court’s opinion in Belton resulted in lower-court decisions that

“treat[ed] the ability to search a vehicle incident to the arrest of a recent occupant as a

police entitlement rather than as an exception justified by the twin rationales of Chimel v.

California.” Thornton v. United States, 541 U.S. 615, 624 (2004) (O’Connor, J.,

concurring). Shortly after Justice O’Connor expressed this concern, the Court revisited the

search-incident-to-arrest exception in Arizona v. Gant—the applicability of which is at

issue in this appeal.

       In Gant, officers arrested the defendant for driving with a suspended license,

handcuffed him, and locked him in the back seat of a patrol car. 556 U.S. at 336, 344. Two

police officers then searched the defendant’s vehicle and found drugs and a firearm. Id. at

336. On review, the Supreme Court held that the officers’ search was not a valid search

incident to arrest, reaching two separate holdings.

       First, the Court noted that “[t]o read Belton as authorizing a vehicle search incident

to every recent occupant’s arrest would . . . untether the rule from the justifications

underlying the Chimel exception.” Id. at 343. Relying on the rationales articulated in

Chimel—specifically, officer safety and the preservation of evidence—the Court

concluded that police can “search a vehicle incident to a recent occupant’s arrest only when

the arrestee is unsecured and within reaching distance of the passenger compartment at the

time of the search” (the “first Gant holding”). Id. (emphasis added). The ultimate inquiry




                                             8
under the first Gant holding is whether it was reasonable for the police to believe that the

arrestee “could have accessed his car at the time of the search.” Id. at 344.

       Second, the Court concluded that “circumstances unique to the vehicle context

justify a search incident to a lawful arrest when it is reasonable to believe evidence relevant

to the crime of arrest might be found in the vehicle” (the “second Gant holding”). Id. at

343 (internal quotation marks omitted). And because (1) the defendant had been secured

and out of reach of the passenger compartment and (2) it was not reasonable to believe the

vehicle contained evidence relevant to the crime of arrest—a traffic violation—the Court

concluded that the search was unlawful. Id. at 344.

                                              B.

       On appeal, Davis urges this Court to apply the first Gant holding to “non-vehicular

containers that were not on the arrestee’s person”—in this case, his backpack. Opening Br.

at 14–15. We agree with Davis that the first Gant holding applies outside the vehicular

context.

       We reach this conclusion because, while Gant involved the warrantless search of a

vehicle incident to an arrest, Chimel did not. Considering the Supreme Court’s reliance on

the rationale of Chimel—a non-vehicle case—in reaching the first Gant holding, we do not

read Gant as limited to the vehicular context. If the Gant Court intended to limit both of its

holdings to vehicular searches, it certainly could have said so. Indeed, the Court specified

that the second Gant holding was based on “circumstances unique to the vehicle context”

(and that it “d[id] not follow from Chimel”). Gant, 556 U.S. at 343. But it made no similar




                                              9
statement regarding the first holding. Accordingly, we see no reason to limit the first Gant

holding—the one derived from Chimel—to searches of vehicles.

       We are not alone in this approach. The Third, Ninth, and Tenth Circuits have

reached the same conclusion. 5 See United States v. Shakir, 616 F.3d 315, 318 (3d Cir. 2010)

(finding “no plausible reason” to limit Gant’s application to automobile searches); United

States v. Cook, 808 F.3d 1195, 1199 n.1 (9th Cir. 2015) (“We do not read Gant’s holding

as limited only to automobile searches because the Court tethered its rationale to the

concerns articulated in Chimel, which involved a search of an arrestee’s home.”); United

States v. Knapp, 917 F.3d 1161, 1168 (10th Cir. 2019) (reading Gant as “focusing attention

on the arrestee’s ability to access weapons or destroy evidence at the time of the search . . .

regardless of whether the search involved a vehicle”).

       Accordingly, we conclude that the first Gant holding applies to searches of non-

vehicular containers and conclude that police officers can conduct warrantless searches of

non-vehicular containers incident to a lawful arrest “only when the arrestee is unsecured




5
  No circuit has held otherwise. But cf. United States v. Curtis, 635 F.3d 704, 713 (5th Cir.
2011) (declining to reach the question of “whether Gant applies solely in the vehicular-
search context or whether it generally limits the scope of the search-incident-to-arrest
exception”); United States v. Perdoma, 621 F.3d 745, 751–52 (8th Cir. 2010) (reasoning
that Gant’s holdings “must be understood in that limited [vehicular] context,” but
ultimately declining to reach the question of “to what extent Gant has application beyond
the context of vehicle searches”).

                                              10
and within reaching distance of the [container] at the time of the search.” Gant, 556 U.S.

at 343.

                                               III.

          Having determined that the first Gant holding applies outside of the vehicle context,

we next consider whether the district court erred in denying Davis’s motion to suppress.

We conclude that it did.

                                               A.

          Richardson’s warrantless search of Davis’s backpack was only permissible as a

search incident to arrest if it was reasonable for Richardson to believe that Davis “could

have accessed [the backpack] at the time of the search.” Id. at 344. In making this

determination, we consider whether Davis was “unsecured and within reaching distance”

of his backpack at the time of the search. 6 Id. at 343.

          The evidence shows that after Davis exited his vehicle with his backpack in tow, he

fled into a swamp and became bogged down in knee-high water. Richardson, with his

service weapon drawn, ordered Davis to exit the swamp, and Davis complied. Back on




6
  There remains an open question as to whether the Gant inquiry (1) amounts to a two-
factor test, both aspects of which the government must satisfy (secureness and reaching
distance), or (2) is more akin to a sliding scale with two dimensions for evaluating the
reasonableness of the officer’s belief that the arrestee could access the container so as to
retrieve a weapon or destroy evidence. But see Ferebee, 957 F.3d at 418–20 (implicitly
assuming, in what strikes as dicta, that the evaluation is a sliding scale, not a two-factor
test). We need not resolve this issue today. Under either formulation, in this case, the
government has failed to satisfy its burden of justifying the warrantless search.

                                               11
terra firma, Davis dropped his backpack and lay down on the ground, and Richardson

handcuffed his hands behind his back. Veiling and Boyd then arrived on the scene.

       Under these conditions, Richardson’s warrantless search of Davis’s backpack was

unlawful. To be sure, there is a level of precarity when police officers arrest a suspect who

has fled arrest. But there is no doubt that Davis was secured and not within reaching

distance of his backpack when Richardson unzipped and searched it. Davis was face down

on the ground and handcuffed with his hands behind his back. He had just been ordered

out of the swamp at gunpoint. The only other individuals within eyesight were officers,

who outnumbered him three to one. And while this all took place in a residential area, it

appears there was no one else around to distract the officers. Without the fluid situation

created by nearby observers, the officers were able to focus solely on Davis. We have no

difficulty in concluding that Davis was secured.

       As to whether the bag was within Davis’s reaching distance, we acknowledge that

he dropped the bag next to him before lying down. By the time of the search, however,

Davis was handcuffed—severely curtailing the distance he could reach. We need not

recount the various acrobatic maneuvers Davis would have needed to perform to place the

backpack within his reaching distance at the time of the search. It is enough to say that, at

the moment in question, the handcuffed and face-down Davis had severely restrained

mobility and was not within reaching distance of the backpack next to him.

       Seeking to resist this straightforward conclusion, the government cites this Court’s

decision in United States v. Ferebee and the Third Circuit’s decision in United States v.




                                             12
Shakir. But those opinions are of no help to the government’s position because they are

readily distinguishable.

          In Ferebee, police officers conducting a warrantless search of a third-party’s home

discovered the defendant inside holding a marijuana blunt near a backpack. 957 F.3d at

410. Upon questioning from the officers, the defendant disclaimed ownership of the

backpack. Id. An officer arrested and handcuffed the defendant before escorting him

outside, leaving the door to the house open and the backpack inside. Id. at 410–11. Another

officer who was still inside the house conducted a warrantless search of the backpack. Id.

at 411.

          Reviewing the denial of the defendant’s motion to suppress the evidence discovered

in his backpack, we held that the defendant “clearly and unequivocally disavowed

ownership of the backpack,” and therefore “abandoned the backpack and any legitimate

expectation of privacy in its contents.” Id. at 417. And assuming without deciding that Gant

applied to non-vehicular searches, we went on to find that even if the defendant did not

abandon his backpack, the search of the backpack was a proper search incident to arrest. 7

Id. at 418–19. We concluded that the defendant was unsecured because, although he was

handcuffed and physically near an officer, “he still could walk around somewhat freely and

could easily have made a break for the backpack inside the house.” Id. at 419. What’s more,



7
  Ferebee’s discussion of this point appears to have been dicta. See 957 F.3d at 423 (Floyd,
J., dissenting) (“Despite holding that Ferebee abandoned his bag, the majority, in extensive
dicta, goes on to conclude that even if Ferebee had not abandoned his bag, the search would
not have required a warrant because it was incident to Ferebee’s arrest.”). Regardless, the
case is distinguishable on the facts.

                                              13
the defendant had both the wherewithal and the dexterity to tamper with evidence while

handcuffed—surreptitiously discarding his marijuana joint without the officers noticing.

Id.

       Not so, in the case at hand. Like the defendant in Ferebee, Davis was handcuffed.

But Davis was face-down on the ground with his hands behind his back, not “mill[ing]

about” like the defendant in Ferebee. Id. In this posture—handcuffed and face-down—

Davis was secured. The contrast here is key. It was arguably reasonable for the officers in

Ferebee to believe that the defendant could access his bag because, although handcuffed

and out of reaching distance, the defendant was not secured and presumably could have

reentered the home and retrieved his bag. In contrast, Davis was both secured and not

within reaching distance. Whether the first Gant holding is framed as a two-part test or as

a spectrum-of-reasonableness inquiry, see supra note 7, it was not reasonable to believe

that Davis could have accessed his backpack at the time of the search.

       Shakir, a case we relied on in Ferebee, is no less distinguishable. In Shakir, the

defendant was placed under arrest and dropped a duffel bag at his feet. 616 F.3d at 316.

After a brief delay, officers were able to handcuff the defendant and search the duffel bag.

Id. at 316–17. The defendant moved to suppress the evidence discovered from the

warrantless search of his bag. Id. at 317.

       The Third Circuit held that the search was permissible because “there remained a

sufficient possibility that [the defendant] could access a weapon in his bag,” noting that

while the defendant was handcuffed and guarded by two police officers, he was still

standing and could access the bag if he “dropped to the floor.” Id. at 321. That Court also


                                             14
acknowledged that the defendant “was subject to an arrest warrant for armed bank robbery,

and that he was arrested in a public area near some 20 innocent bystanders, as well as at

least one suspected confederate who was guarded only by unarmed hotel security officers.”

Id. Surely underlying the Court’s reference to the number of bystanders and a possible

confederate is a realization that an arrest scene may be more fluid—and an arrestee less

secure—when officers must not only maintain custody of the arrestee, but also stay vigilant

of the crowd and any efforts by confederates to interfere with the arrest. While the presence

of bystanders on its own might not result in an unsecured arrestee, the court in Shakir

viewed all of the circumstances together and concluded that there was more than a remote

possibility that the defendant could have accessed his bag and retrieved a weapon. Id.

       Again, the case before us is distinguishable in key ways. Davis was lying on his

stomach with his hands cuffed behind his back. While the arrest in Shakir was “very low

key,” id. at 316, Davis had a gun pointed at him. Other than the three police officers on the

scene, Davis was alone. Rather than being able to drop to the floor to access his bag, like

the defendant in Shakir could have, Davis would have had to jump up from the ground or

contort his body in order to snatch the backpack away from Richardson.

       In concluding that the search of Davis’s backpack was lawful, the district court

found that Richardson, who had just witnessed Davis commit a number of crimes, had

“probable cause to arrest [Davis] for those crimes and to search his person and items within

his immediate control.” J.A. 149. But while the district court correctly noted that a search

incident to a lawful arrest is an exception to the warrant requirement, it simply concluded

that the search of Davis’s backpack was lawful because it was within his “immediate


                                             15
control”—defined as “the area from within which [an arrestee] might gain possession of a

weapon or destructible evidence.” Chimel, 395 U.S. at 763. Under Gant, however, an item

is not within a person’s immediate control if it is unreasonable to believe that they can

access it.

       In considering the search-incident-to-arrest exception, the proper question before

the district court was whether it was reasonable for Richardson to believe that Davis could

access his backpack at the time of the search. The district court committed legal error when

it ruled on the motion to suppress without applying the relevant law. And the record reflects

that Davis was secure and not within reaching distance of his backpack when Richardson

searched it. As such, there is no factual basis for finding that this was a proper search

incident to arrest under the first Gant holding. Because the district court erred in concluding

that the search of the backpack was a lawful search incident to arrest, we reverse and

remand with instructions to grant Davis’s motion to suppress.

                                              B.

       We must also address the warrantless search of Davis’s vehicle. Davis argues that

the district court erred in finding the search was permissible under another exception to the

warrant requirement, the automobile exception. See United States v. Kelly, 592 F.3d 586,

589 (4th Cir. 2010). He further contends that the search of his car was unlawful because it

was not a proper search incident to his arrest (the first Gant holding) and it was not




                                              16
reasonable to believe that evidence of his crime of arrest would be discovered in the vehicle

(the second Gant holding). We consider each exception in turn.

       Under the automobile exception, the police can search a vehicle without first

obtaining a warrant if the vehicle “is readily mobile and probable cause exists to believe it

contains contraband.” 8 Kelly, 592 F.3d at 589 (quoting Pennsylvania v. Labron, 518 U.S.

938, 940 (1996) (per curiam)). “Probable cause exists when ‘the known facts and

circumstances are sufficient to warrant a man of reasonable prudence in the belief that

contraband or evidence of a crime will be found.’” United States v. Patiutka, 804 F.3d 684,

690 (4th Cir. 2015) (quoting Ornelas v. United States, 517 U.S. 690, 696 (1996)). “The

principal components of a determination of . . . probable cause will be the events which

occurred leading up to the stop or search, and then the decision whether these historical

facts, viewed from the standpoint of an objectively reasonable police officer, amount to . . .

probable cause.” United States v. Brookins, 345 F.3d 231, 235–36 (4th Cir. 2003) (quoting

Ornelas, 517 U.S. at 696).

       In finding that the officers had “ample probable cause” to search Davis’s vehicle,

the district court relied on Davis’s “flight from the traffic stop, his ensuing arrest, [and] the

recovery of the cash and the materials in the backpack.” J.A. 149. The government points

to the same evidence in arguing that probable cause existed. But without the evidence

recovered from Davis’s backpack, probable cause for the vehicle search rests solely on


8
  The “readily mobile” inquiry asks whether an automobile “is ‘being used on the
highways’ or is ‘readily capable of such use’ rather than, say, ‘elevated on blocks.’” Kelly,
592 F.3d at 591 (quoting California v. Carney, 471 U.S. 386, 392–93, 394 n.3 (1985)).
Davis does not dispute that his vehicle was readily mobile.

                                               17
Davis’s flight, his subsequent arrest, and the cash discovered on his person. These facts

present a closer question than the one answered by the district court, and taken together,

they cannot support the warrantless search that occurred.

       While Davis’s flight coupled with the cash in his pockets may have given the

officers an articulable suspicion that evidence of a crime could be located in the vehicle, it

did not give them probable cause to circumvent the Fourth Amendment’s warrant

requirement and search the vehicle. Yet “the automobile exception requires that the police

have probable cause (not just reasonable articulable suspicion) to search.” Patiutka, 804

F.3d at 691. Could a fleeing individual with cash in his pockets have evidence of some

crime in his vehicle? Perhaps. But without more supporting facts available to tip the scales

from “articulable suspicion” to “probable cause,” the more accurate answer is, “[w]ell

perhaps, but not probably.” United States v. Lyles, 910 F.3d 787, 790–91, 794 (4th Cir.

2018) (affirming grant of motion to suppress for lack of probable cause where police

obtained warrant to search defendant’s entire house for evidence of marijuana possession

based on finding three marijuana stems in his trash). Accordingly, because the district court

should have suppressed the evidence discovered in the backpack, it also should have

concluded that the officers did not have probable cause to search the vehicle without a

warrant.

       While the district court based its decision solely on the automobile exception, we

“may affirm on any grounds apparent from the record.” United States v. Ali, 991 F.3d 561,

571 (4th Cir. 2021) (internal quotation marks omitted). But the warrantless search of the

automobile fares no better under the search-incident-to-arrest exception. As discussed


                                             18
above, the search-incident-to-arrest exception allows police to “search a vehicle incident

to a recent occupant’s arrest” so long as “the arrestee is within reaching distance of the

passenger compartment at the time of the search or it is reasonable to believe the vehicle

contains evidence of the offense of arrest.” Gant, 556 U.S. at 351 (emphasis added).

       At the time of the search, Davis was handcuffed and in Boyd’s custody. While

officers were searching the vehicle Davis had driven into a yard, Davis himself was being

searched near the police cars in the cul-de-sac. And after searching Davis, the officers sat

him on the ground before eventually placing him in the back of a police car. Nothing in the

record suggests that Davis was not secured or that he was anywhere near his vehicle at the

time of its search.

       Further, the record reflects that while Davis was initially pulled over because of his

window tint, he was ultimately arrested for traffic violations, as well as “speeding to elude

arrest and resisting an officer.” 9 J.A. 149. It certainly was not reasonable to believe that

Davis’s vehicle contained evidence of any of those crimes. 10 See, e.g., United States v.



9
  Under North Carolina’s speeding-to-elude-arrest offense, “[i]t shall be unlawful for any
person to operate a motor vehicle on a street, highway, or public vehicular area while
fleeing or attempting to elude a law enforcement officer who is in the lawful performance
of his duties.” N.C. Gen. Stat. § 20-141.5(a). And North Carolina’s offense of resisting
arrest prohibits any person from “willfully and unlawfully resist[ing], delay[ing] or
obstruct[ing] a public officer in discharging or attempting to discharge a duty of his office.”
Id. § 14-223.
10
   The government does not contend otherwise, instead focusing on the drugs in the
backpack and the gun tossed from the car. See Response Br. at 22–23. Putting aside that
the search of the backpack was unconstitutional and that the search of the car occurred
before the officers learned of the gun, the crimes of arrest were indisputably not drug- or
gun-related, whatever the officers’ suspicions may have been.

                                              19
Beene, 818 F.3d 157, 161–62 (5th Cir. 2016) (finding that the defendant’s vehicle would

not contain evidence of his crime of resisting arrest); United States v. Vinton, 594 F.3d 14,

25 (D.C. Cir. 2010) (“Had [the defendant] been arrested merely for speeding . . . , Gant’s

evidentiary rationale obviously would not have authorized a subsequent search because

under the circumstances it would have been very unlikely that evidence relevant to [that]

traffic offense[] would be found inside his car.”); United States v. Lopez, 567 F.3d 755,

758 (6th Cir. 2009) (finding a police officer’s warrantless search of the defendant’s vehicle

unreasonable because “[t]here was no reason to think that the vehicle contained evidence

of the offense of arrest, since that offense was reckless driving”); see also State v. Noel,

779 S.E.2d 877, 885 (W. Va. 2015) (finding the warrantless search of the defendant’s

vehicle unlawful under Gant because “it was unreasonable to believe that [the defendant’s]

vehicle contained evidence of the offense of his arrest, i.e., fleeing with reckless

indifference.”). As such, we reverse.

                                            IV.

       The thicket of nuanced exceptions to the warrant requirement may appear, at times,

confusing and unnavigable. Indeed, law enforcement may feel that courts are missing the

forest for the trees—focusing myopically on minor details and ignoring the big picture,

which in this case involves a man in a vehicle with tinted windows fleeing a routine traffic

stop and then transporting a backpack on foot into a swamp. Surely, some may say, the




                                             20
officers were entitled to infer that that man was up to no good, and that, at the very least,

his backpack could have evidence of a crime greater than a traffic violation.

       But that is the wrong question. As Justice O’Connor once rightly pointed out,

exceptions to the warrant requirement are not “police entitlement[s]” to searches. Thornton,

541 U.S. at 624 (O’Connor, J., concurring). Rather, they are narrow “exception[s]” which

must be “justified” by specific circumstances. Id. In the words of Chief Justice Roberts,

quoting Justice Stewart, “the warrant requirement is ‘an important working part of our

machinery of government,’ not merely ‘an inconvenience to be somehow “weighed”

against the claims of police efficiency.’” Riley v. California, 573 U.S. 373, 401 (2014)

(quoting Coolidge v. New Hampshire, 403 U.S. 443, 481 (1971)). It is the crucial role of

courts to ensure that the government conducts searches of property in which individuals

have a reasonable expectation of privacy only when permitted by a warrant or when one of

a handful of limited exceptions to the warrant requirement applies.

       For the foregoing reasons, we hold that the district court erred when it concluded

that the warrantless search of Davis’s backpack and vehicle were permissible. Accordingly,

we reverse and remand for entry of an order granting the motion to suppress, and for any

other proceedings consistent with this opinion.

                                                            REVERSED AND REMANDED




                                             21

```

---

## GROUP: _overhaul2/lake/cases/United States v. Hunt.json  (`lake-record`, 1 assertions)

### content_page

```
---
title: United States v. Hunt
type: case
citation: "No. 23-2342, slip op. (9th Cir. 2025)"
parallel_cite: ""
neutral_cite: ""
court: 9th Cir. 2025
court_level: coa
circuit: ca9
year: 2025
date_decided: 2025-08-27
docket: 23-2342
authority_weight: "Binding in-circuit — 9th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/10661637/united-states-v-hunt/"
  cluster_id: 10661637
  opinion_id: null
  identity_checked: false
lake:
  record_id: United States v. Hunt
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Abandonment]]"
    role: Key
related:
  - "[[Abandonment]]"
  - "[[Riley v. California]]"
  - "[[California v. Hodari D.]]"
  - "[[Standing to Challenge a Search]]"
tags:
  - case
  - fourth-amendment
  - abandonment
  - standing
  - digital-privacy
  - cell-phone
  - reasonable-expectation-of-privacy
  - ninth-circuit
holding: "The Ninth Circuit held that the abandonment doctrine applies to digital devices but that a court must analyze the intent to abandon the physical device separately from the intent to abandon its data; Hunt did not abandon his iPhone or its contents by dropping it after being shot five times and fleeing for medical help, so the district court erred in finding he lacked standing — but his Fourth Amendment claim nonetheless failed on the merits because agents obtained a warrant and searched the phone within a reasonable period; conviction affirmed."
---

# United States v. Hunt

*No. 23-2342, slip op. (9th Cir. 2025)* · U.S. Court of Appeals for the Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 10661637 → opinion 11128224 (FOR PUBLICATION slip No. 23-2342, filed 2025-08-27; no reporter cite yet — S2 A3 slip form); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
One December 2017 morning, Dontae Hunt was talking on his black iPhone near his apartment parking lot in Oregon when a gunman shot him five times. Hunt dropped the iPhone (which came to rest near some shrubs) and his Gucci satchel. His girlfriend took him to the emergency room; she grabbed the satchel but left the iPhone behind. Police later recovered the phone, obtained a warrant, and searched it; the evidence helped convict Hunt of possession with intent to distribute fentanyl analogue, drug conspiracy, unlawful firearm possession, and money laundering. The district court denied Hunt's suppression motion on the ground that he **abandoned** the phone — and thus lacked standing — and also denied his motion to recuse the trial judge. Hunt appealed.

## Issue
Whether Hunt abandoned his [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in his iPhone, and in the data it contained, when he dropped it after being shot and fled for medical help — losing [[Standing to Challenge a Search|standing to challenge]] the search — and, if not, whether the later warranted search of the phone satisfied the Fourth Amendment.

## Rule
Under the abandonment doctrine, a person who abandons property relinquishes his expectation of privacy in it and waives any Fourth Amendment challenge. Declining the invitation to "scuttle" that doctrine for cellphones, the panel adapted it to devices that hold "historically unprecedented amounts of private information" by separating the two objects of intent: "When determining a person's intent to abandon, courts should analyze the intent to abandon the device separately from the intent to abandon its data." — No. 23-2342, slip op. at 4. ^pin-op4

## Application
On this record, Hunt abandoned neither. The court could not infer an intent to abandon the phone or its contents from the fact that Hunt dropped it after being shot five times: the record showed he fled to seek medical help, not to disclaim the device or its data. The district court therefore erred in holding that Hunt lacked standing. His Fourth Amendment claim nonetheless failed **on the merits**, because federal agents obtained a warrant and searched the phone within a reasonable period. The panel separately rejected Hunt's recusal argument, holding that a reasonable person would not question the trial judge's impartiality.

## Conclusion
**Affirmed** (conviction and sentence). Judge Lee wrote for the panel (Christen and Lee, Circuit Judges; Bencivengo, District Judge, sitting by designation).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Hunt* is a leading digital-age refinement of **abandonment**: the doctrine survives for cellphones, but a *[[Riley v. California|Riley]]*-informed court must ask separately whether the suspect meant to abandon the **device** and whether he meant to abandon its **data** — so involuntarily dropping a phone while fleeing injury does not surrender the privacy interest in its contents. Cite it as a published [[Reading and Citing Cases#slip-opinion|slip opinion]]; the [[Reading and Citing Cases#reporter|reporter]] (F.4th) citation is pending.

## Appears on
- [[Abandonment]] — *Key*

## Sources
- [*United States v. Hunt*, No. 23-2342, slip op. (9th Cir. Aug. 27, 2025)](https://www.courtlistener.com/opinion/10661637/united-states-v-hunt/) — pinpoint: slip op. at 4 (device-vs-data separate-intent holding; FOR PUBLICATION slip opinion, no reporter pagination yet, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1ee35eab991cb24a", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Hunt"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Hunt", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Hunt

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Hunt",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Hunt",
    "case_name_short": "Hunt",
    "case_name_full": "",
    "input_case_name": "United States v. Hunt",
    "court": "9th Cir. 2025",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "2025-08-27",
    "year": 2025,
    "docket": "23-2342",
    "cluster_id": 10661637,
    "lead_opinion_id": 11128224,
    "sibling_ids": [],
    "absolute_url": "/opinion/10661637/united-states-v-hunt/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": "state",
      "selected": null,
      "reason": "no_official_class_citation"
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "9th Cir. FOR PUBLICATION slip No. 23-2342, filed 2025-08-27 (Dontae Hunt; abandoned-phone). No F.4th cite yet. (Search-floated '56 F.4th' rejected as fabricated.)",
      "legs": [
        {
          "source": "Court PDF",
          "url": "https://cdn.ca9.uscourts.gov/datastore/opinions/2025/08/27/23-2342.pdf",
          "cite": "No. 23-2342 FOR PUBLICATION, filed 2025-08-27"
        },
        {
          "source": "Official court",
          "url": "https://www.eff.org/deeplinks/2025/09/appeals-court-abandoned-phones-dont-equal-abandoned-privacy-rights",
          "cite": "links only to slip; no F.4th cite"
        }
      ]
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
    "date_created": "2026-07-06T05:53:59Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:54:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:54:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:54:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:54:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-hunt--10661637",
      "to_record_id": "United States v. Hunt",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Hunt

```
                    FOR PUBLICATION

     UNITED STATES COURT OF APPEALS
          FOR THE NINTH CIRCUIT

UNITED STATES OF AMERICA,                       No. 23-2342
                                                  D.C. No.
               Plaintiff - Appellee,
                                               3:18-cr-00475-
                                                    IM-1
    v.

DONTAE LAMONT HUNT,
                                                  OPINION
               Defendant - Appellant.

         Appeal from the United States District Court
                   for the District of Oregon
         Karin J. Immergut, District Judge, Presiding

            Argued and Submitted March 31, 2025
                     Portland, Oregon

                     Filed August 27, 2025

    Before: Morgan B. Christen and Kenneth K. Lee, Circuit
     Judges, and Cathy Ann Bencivengo, District Judge. *

                     Opinion by Judge Lee


*
  The Honorable Cathy Ann Bencivengo, United States District Judge
for the Southern District of California, sitting by designation.
2                           USA V. HUNT


                          SUMMARY **


                          Criminal Law

    The panel affirmed the district court’s orders denying
Dontae Hunt’s motion to suppress, and his recusal motion,
in a case in which Hunt was convicted of possession with
intent to distribute fentanyl analogue, conspiracy to possess
with intent to distribute and to distribute a controlled
substance, unlawful possession of firearms, and laundering
of monetary instruments.
    The abandonment doctrine states that a person who
abandons property relinquishes his expectation of privacy in
that property and thus waives any Fourth Amendment
challenge.
    Addressing how to apply the abandonment doctrine to
digital devices that may contain a massive trove of personal
information, the panel declined to scuttle the doctrine when
it comes to cellphones. The panel followed the time-tested
reasonable expectation of privacy principle while
considering that today’s technology allows us to keep
historically unprecedented amounts of private information in
devices. When determining a person’s intent to abandon,
courts should analyze the intent to abandon the device
separately from the intent to abandon its data.
    Disagreeing with the district court’s ruling that Hunt
lacked standing to challenge the search of an iPhone he
dropped after being shot five times, the panel held that the

**
  This summary constitutes no part of the opinion of the court. It has
been prepared by court staff for the convenience of the reader.
                        USA V. HUNT                        3


district court erred when it held that Hunt abandoned his
privacy interest in the phone. The record does not allow the
inference that Hunt intended to abandon the phone or its
contents when he dropped it after being shot; it shows that
he fled to seek medical help.
    The panel held that Hunt’s Fourth Amendment claim
fails on the merits because federal agents obtained a warrant
and searched his phone within a reasonable period.
   The panel rejected Hunt’s argument that the district court
judge should have recused herself because she served as the
U.S. Attorney in Oregon when her office earlier prosecuted
Hunt for a different crime. A reasonable person would not
question the district court judge’s impartiality.
   The panel rejected Hunt’s other challenges in a
concurrently filed memorandum disposition.



                        COUNSEL

Suzanne Miles (argued), Assistant United States Attorney,
Criminal Appellate Chief; Peter D. Sax, Gary Y. Sussman,
and Sarah Barr, Assistant United States Attorneys; Natalie
K. Wight, United States Attorney; Office of the United
States Attorney, United States Department of Justice,
Portland, Oregon; for Plaintiff-Appellee.
Raymond D. Moss Jr. (argued) and Jonathan S. Sack,
Morvillo Abramowitz Grand Iason & Anello PC, New York,
New York, for Defendant-Appellant.
Jennifer S. Granick, American Civil Liberties Union
Foundation, San Francisco, California; Nathan F. Wessler
4                       USA V. HUNT


and Brett M. Kaufman, American Civil Liberties Union
Foundation, New York, New York; Kelly Simon, American
Civil Liberties Union Foundation of Oregon, Portland,
Oregon; Andrew Crocker and Hannah Zhao, Electronic
Frontier Foundation, San Francisco, California; Jake
Wiener, Electronic Privacy Information Center,
Washington, D.C.; for Amici Curiae American Civil
Liberties Union, ACLU of Oregon, Electronic Frontier
Foundation, Electronic Privacy Information Center, and
National Association of Criminal Defense Lawyers.



                        OPINION

LEE, Circuit Judge:

    The abandonment doctrine states that a person who
abandons property relinquishes his expectation of privacy in
that property and thus waives any Fourth Amendment
challenge. But how should we apply the abandonment
doctrine to digital devices that may contain a massive trove
of personal information? Appellant Dontae Hunt and amici
urge us to scuttle this doctrine when it comes to cellphones.
    We decline to do so. We follow the time-tested
reasonable expectation of privacy principle while
considering that today’s technology allows us to keep
historically unprecedented amounts of private information in
devices. When determining a person’s intent to abandon,
courts should analyze the intent to abandon the device
separately from the intent to abandon its data.
    We disagree with the district court’s ruling that Hunt
lacked standing to challenge the search of his black iPhone.
                           USA V. HUNT                             5


The record does not allow the inference that Hunt intended
to abandon the phone or its contents when he dropped it after
being shot five times; it shows that he fled to seek medical
help. Hunt’s Fourth Amendment claim fails on the merits
because federal agents obtained a warrant and searched his
phone within a reasonable period.
    We also reject Hunt’s argument that the district court
judge should have recused herself because she served as the
U.S. Attorney in Oregon when her office earlier prosecuted
Hunt for a different crime. A reasonable person would not
question the district court judge’s impartiality. We affirm
the conviction and the sentence. 1
                       BACKGROUND
    I. Dontae Hunt drops his black iPhone as he gets shot
       five times.
    One early morning in December 2017, Dontae Hunt was
talking on his black iPhone as he strolled by his apartment
parking lot. A gunman suddenly appeared, firing a fusillade
of bullets at Hunt. Shot five times, Hunt dropped his black
iPhone and his Gucci satchel. Hunt’s girlfriend had
accompanied him and immediately called a female friend to
help take Hunt to a nearby hospital. The girlfriend took
Hunt’s satchel (which had fallen on the parking lot) but left
his black iPhone (which was near some shrubs). The two
women dropped Hunt off at the emergency room and left.
    The two women, however, did not make it far. The
police pulled the pair over for a traffic violation. During the
traffic stop, an officer spotted a brown Gucci satchel bag,


1
 We reject Hunt’s other challenges in a concurrently filed memorandum
disposition.
6                        USA V. HUNT


covered in blood, laying on the passenger floorboard. Inside
the bag the officer found two handguns. Hunt’s girlfriend
admitted the Gucci bag belonged to Hunt but denied
knowing the bag contained the handguns.
    Eugene police next went to the hospital to speak with
Hunt about the shooting. The officer found Hunt at the
hospital in “substantial pain.” Hunt refused to speak to the
officer. When the officer asked Hunt “if he wanted the
police to find out who shot him,” Hunt replied “no” and said
that “he was alright.” Before leaving the hospital, the officer
seized Hunt’s clothing and another iPhone—a white one—
as evidence associated with the shooting. The officer gave
Hunt a receipt for both the clothing and the white iPhone.
    Police visited the crime scene, where they found a black
iPhone near some shrubs a short distance from the shooting
location. The police took it into evidence as part of their
investigation into the shooting. No one ever came looking
for the phone, so it remained in evidence for over two years
until an unrelated investigation into a Portland overdose
death triggered police interest in the device.
    II. The federal government starts a separate drug
        investigation.
    The overdose investigation, conducted by the Portland
Police Bureau and several federal agencies, identified a
woman who sold counterfeit oxycodone pills to the
deceased. She declined to identify her supplier by name but
gave the police the supplier’s cellphone number. Relying on
this informant, the police obtained a geolocation warrant for
the registered cellphone owner, a woman who (the police
later discovered) worked for Hunt. In its affidavit in support
of the geolocation warrant, the police, however, failed to
disclose that this informant had a criminal history of lying to
                        USA V. HUNT                         7


the police. Nonetheless, the geolocation warrant ultimately
yielded additional evidence, leading the police to focus on
Hunt and to conduct an in-person surveillance of him. The
police noted that Hunt engaged in peculiar behavior common
to drug dealers trying to evade detection from law
enforcement. For example, he made well over a dozen
Walmart cash transfers using different phone numbers. The
mother of his children rented seven cars over four months,
and Hunt drove a Chevy Silverado paid for in cash by a
person with no links to Hunt. The investigation also turned
up evidence of Hunt’s past drug dealing convictions. And a
second confidential informant, with no criminal record or
known relationship to the first informant, told police that
Hunt continued to sell drugs and “store[] cash at residences
belonging to female acquaintances.”
    Federal agents used this information to obtain a premises
search warrant for three residences associated with Hunt,
including a home on Portland’s Dekum Street. During the
raid on the Dekum residence, police found counterfeit
fentanyl pills, firearms, and Hunt—barricaded in a bathroom
and allegedly flushing pills down the toilet.
 III. The government uses data from Hunt’s black
      iPhone to help convict him on drug-trafficking
      and other charges.
    The story comes full circle when federal agents filed an
affidavit in January 2020 to search several electronic
devices, including the black iPhone found at the scene of
Hunt’s shooting and held by the local police. At the time,
federal agents still lacked confirmation that the black iPhone
belonged to Hunt, though they suspected so because police
“found [it] on the ground where [Hunt] was shot.” The
8                       USA V. HUNT


search of the black iPhone produced more evidence of
Hunt’s drug dealing activities.
    Based on evidence from the searches of the Dekum
residence and the black iPhone, prosecutors charged Hunt
with several crimes, including possession with intent to
distribute fentanyl analogue, conspiracy to possess with
intent to distribute a controlled substance, unlawful
possession of a firearm, and laundering of monetary
instruments.    The case eventually landed on Judge
Immergut’s docket.
    Before the trial, Hunt moved for Judge Immergut’s
recusal. Over fifteen years earlier, Judge Immergut had
served as the U.S. Attorney for the District of Oregon when
that office prosecuted Hunt for unrelated charges. In that
case, the district court had sentenced Hunt to twenty years,
but his sentence was commuted after thirteen years. Judge
Immergut declined to recuse herself. She explained, “I have
no personal bias or prejudice against Defendant Hunt. Nor
do I have any personal recollection of Defendant Hunt or the
facts underlying his prior 2005 conviction.”          Judge
Immergut presided over the trial, which ultimately led to
Hunt’s conviction.
               STANDARD OF REVIEW
    This court reviews de novo a district court’s denial of a
motion to suppress. United States v. Yang, 958 F.3d 851,
857 (9th Cir. 2020). We review the district court’s factual
findings, including those factual findings related to
abandonment, for clear error. See id. at 858; see also United
States v. Nordling, 804 F.2d 1466, 1469 (9th Cir. 1986). For
recusal orders, we review for abuse of discretion. United
States v. McTiernan, 695 F.3d 882, 891 (9th Cir. 2012).
                          USA V. HUNT                          9


                        DISCUSSION
 I.   Judge Immergut did not abuse discretion in
      denying the recusal motion.
    As a threshold matter, we must decide whether Judge
Immergut should have recused herself because she served as
the U.S. Attorney in Oregon when that office prosecuted
Hunt in his earlier 2005 criminal proceedings. We reject
Hunt’s argument that she should have done so.
     A federal judge must “disqualify [her]self in any
proceeding in which [her] impartiality might reasonably be
questioned.” 28 U.S.C. § 455(a); see also United States v.
Holland, 519 F.3d 909, 913 (9th Cir. 2008) (quoting from
id.). This provision requires judges “to avoid even the
appearance of partiality.” Liljeberg v. Health Servs.
Acquisition Corp., 486 U.S. 847, 860 (1988) (quoting Health
Servs. Acquisition Corp. v. Liljeberg, 796 F.2d 796, 802 (5th
Cir. 1986)). We thus require recusal when “a reasonable
person with knowledge of all the facts would conclude that
the judge’s impartiality might reasonably be questioned.”
Holland, 519 F.3d at 913 (quotation omitted).
    Our circuit precedent does not establish many bright-line
rules and requires judges to take a “fact-driven” approach
that “may turn on the subtleties” of each case when applying
the recusal standard. Id. For example, in United States v.
Silver, we applied this fact-driven approach to find that a
judge did not need to recuse himself without a “factual
connection or relationship between the [] case [before him]
and [a ten-year-old] mail fraud” investigation into the
defendant that began during the judge’s tenure as the United
States Attorney. 245 F.3d 1075, 1079 (9th Cir. 2001). In
reaching that holding, Silver did not establish a rigid rule that
a judge can avoid recusal simply because the prior case lacks
10                      USA V. HUNT


a factual relationship to the case before the judge. See id.
Rather, both the age of the earlier investigation and the fact
that the judge only needed to consider the prior case for
sentencing purposes contributed to our determination that a
reasonable person would not doubt that judge’s impartiality.
Id. at 1080.
    In contrast, we did impose a bright-line rule in United
States v. Arnpriester that a judge cannot decide the same
case in which the judge participated in or supervised as the
United States Attorney. 37 F.3d 466, 467 (9th Cir. 1994).
We found categorically that a reasonable person would
question a judge’s impartiality in any such situation. See id.
    The facts of Hunt’s case convince us that Judge
Immergut did not abuse her discretion in holding that a
reasonable person would not question her impartiality. First,
as in Silver, Hunt’s current case has “no factual connection
or relationship” with his prior prosecution. See 245 F.3d at
1079. Second, over fifteen years passed between Hunt’s first
prosecution and this second case. That stretches beyond the
ten-year gap in Silver. Id. at 1080. Third, Judge Immergut
served as the United States Attorney, and not as a line
prosecutor. Many similar drug and felon-in-possession
prosecutions likely passed through her office, and Judge
Immergut, as the U.S. Attorney, likely was not directly
involved in these commonplace criminal prosecutions.
Fourth, Judge Immergut stated she did not have “any
personal recollection” of Hunt’s 2005 case and has “no
personal bias or prejudice” against him. These facts would
not lead a reasonable person to think that Judge Immergut
had any bias against Hunt. We thus next address Hunt’s
Fourth Amendment claim.
                        USA V. HUNT                        11


 II. Hunt has standing to make a Fourth Amendment
     challenge because he did not abandon his privacy
     interest in the black iPhone.
    The district court erred when it held that Hunt abandoned
the black iPhone and thus lacked standing to challenge the
search of the iPhone’s data. We, however, reject Hunt and
amici’s invitation to jettison the abandonment doctrine for
digital data. Rather, we follow the reasonable expectation of
privacy framework set by the Supreme Court and adapt the
abandonment doctrine to account for the unique
characteristics of cellphone data. That approach leads us to
hold that the abandonment doctrine can apply to cellphone
data but courts should analyze the physical phone and its
data separately to determine whether the circumstances
allow the conclusion that there was an intent to abandon
either.
   A. We apply the expectation-of-privacy principle
      while considering the unique nature of digital
      devices in applying the abandonment doctrine.
    The Fourth Amendment guarantees to the people the
right “to be secure in their persons, houses, papers, and
effects, against unreasonable searches and seizures . . . .”
U.S. CONST. amend. IV. The Framers adopted this
amendment to guard against the type of abuses they
experienced under British rule: It was a “response to the
reviled ‘general warrants’ and ‘writs of assistance’ of the
colonial era, which allowed British officers to rummage
through homes in an unrestrained search for evidence of
criminal activity.” Carpenter v. United States, 585 U.S. 296,
303 (2018) (quoting Riley v. California, 573 U.S. 373, 403
(2014)). The Fourth Amendment enshrines the founding
generation’s goals to protect “‘the privacies of life’ against
12                           USA V. HUNT


‘arbitrary power’” and “to place obstacles in the way of a too
permeating police surveillance.” Id. (citations omitted).
    But as digital “technology has enhanced the
Government’s capacity to encroach upon” traditionally
private areas of life, the judiciary has sought to preserve
“that degree of privacy against government that existed
when the Fourth Amendment was adopted.” Carpenter, 585
U.S. at 305 (citing Kyllo v. United States, 533 U.S. 27, 34
(2001)). To that end, the Supreme Court warns that “[w]hen
confronting new concerns wrought by digital technology,”
courts must be “careful not to uncritically extend existing
precedents.” Carpenter, 585 U.S. at 318.
    We follow the model set by the Supreme Court in Riley,
Carpenter, Jones, and Kyllo and apply reasonable
expectation-of-privacy principles to a world where new
technology makes possible previously unimaginable and
objectionable invasions of privacy. 2 As one leading Fourth
Amendment scholar has argued, the Supreme Court’s
framework for analyzing digital devices advances the
“original public meaning of the Fourth Amendment.” Orin
Kerr, The Digital Fourth Amendment 54–56 (2025). It does
so by preserving the same balance between the citizenry’s
right to privacy and the government’s power to investigate
that existed in the early republic. See id. at 57. The founding

2
  See Riley, 573 U.S. at 385–401 (applying the traditional warrant
exception test to cellphone data); Carpenter, 585 U.S. at 313 (applying
the traditional expectation of privacy in the “whole of [one’s] physical
movements” to cell-site data); United States v. Jones, 565 U.S. 400, 402,
411 (2012) (“What we apply is an 18th-century guarantee against
unreasonable searches” to find attaching a GPS tracking advice to a car
counts as a search); Kyllo, 533 U.S. at 34–35 (applying the traditional
expectation of privacy standard in holding that the use of thermal
imagining technology can count as a search of a home).
                              USA V. HUNT                               13


generation always understood the Fourth Amendment to
protect a certain degree of privacy and not merely a specific
set of rules. Id.; see Kyllo, 533 U.S. at 34–35.
    The Supreme Court in Riley highlighted the unique
nature of digital devices containing massive amounts of
personal data. 573 U.S. 373. The police officers there
searched cellphones right after arresting the suspects, and
justified these warrantless searches under the search
incident-to-arrest exception. The Court, however, refused to
extend this warrantless search exception to cellphones, in
large part because it recognized the “substantially greater
individual privacy interests” associated with the private and
detailed data contained in cellphones as opposed to “a brief
physical search.” Id. at 374. 3 That greater privacy interest
stems from the vast quantity and intimate quality of the data
collected throughout the day and over the years. Id. at 393.
As the Court wryly remarked, “the proverbial visitor from
Mars might conclude [cellphones] were an important feature
of human anatomy,” given that they “are now such a
pervasive and insistent part of daily life.” Id. at 385.
    Cellphones can easily contain over a decade’s worth of
private photographs, personal text messages to family and
friends, every email sent to business associates, voicemails
from years ago, and call logs documenting every call
received or dialed. The various apps on a phone can also
contain a trove of personal information. For example, a


3
  The Court also reasoned that rationales justifying a warrantless search
incident to arrest—the risk of a suspect hiding a weapon in, say, a satchel
or reaching out to destroy evidence in that satchel—do not apply to
digital data. See 573 U.S. at 386. The Court, however, recognized
exigent circumstances could still allow a warrantless search of digital
devices. Id. at 391.
14                       USA V. HUNT


search of web-browsing history may reveal intimate details
of “an individual’s private interests or concerns.” Id. at 395.
A medical-related app may disclose private health
information or prescription history. And a financial app can
divulge purchases made on a credit card, bank balances,
credit scores, and an individual’s net worth. Indeed, a
cellphone’s ability to store vast data likely allows the
government to learn more about the cellphone’s owner than
would a search of the person’s entire home or every piece of
mail received. Id. at 396–97.
    In our case, we must decide how to apply the
abandonment doctrine—a well-established exception to the
Fourth Amendment’s prohibition against a warrantless
search and seizure—to cellphones. The abandonment
doctrine holds that a person forfeits a reasonable expectation
of privacy by voluntarily abandoning property. United
States v. Fisher, 56 F.4th 673, 686 (9th Cir. 2022).
Abandonment goes to intent. Nordling, 804 F.2d at 1469. A
person shows an intent to abandon a privacy interest when,
given the totality of the circumstances, by “words, acts or
other objective indications, [the] person has relinquished a
reasonable expectation of privacy in the property at the time
of the search or seizure.” Id. (citation modified). We ask
what “words, acts or other objective indications” would
reveal a person’s intent to voluntarily abandon any
expectation of privacy in the property. See id.
    Following the Supreme Court’s framework, we apply the
abandonment doctrine to cellphones while accounting for
the unique aspects of cellphone data. Someone who loses
her cellphone through theft or negligence likely does not
intend to release to the public details of her personal life any
more than someone who loses a house key intends to invite
the public to rummage through her home. See Riley, 573
                        USA V. HUNT                        15


U.S. at 397. That house key analogy proves particularly
instructive when thinking about abandonment because the
house key and the house provide the closest pre-digital
functional analogue to the cell phone and its data. See Kerr,
supra at 65. The analogy confirms that just as courts
historically would apply the reasonable expectation of
privacy principle separately to a house key and the contents
of a house, courts today may need to distinguish a digital
device from the data it contains to preserve the degree of
privacy that existed at the time of the Fourth Amendment’s
adoption. Id. Based on the specific facts of each case, courts
should analyze the intent to abandon the device separately
from the intent to abandon its data—and not reflexively
conflate the two.
     In Fisher, the Ninth Circuit’s most analogous case, two
defendants hid a cellphone and two hard drives with
incriminating information between the insulation and wood
framing of an attic. 56 F.4th at 681. While in custody, the
defendants sold the house with the devices still hidden in the
attic. Id. The court held that the defendants had abandoned
the devices when they did not recover them “before the home
was sold.” Id. at 687 (emphasis in original). Having
intentionally left their devices in the home and then sold the
house knowing that the devices remained there, the
defendants abandoned the devices and their data. Id.
   B. Hunt did not abandon the black iPhone or its
      data.
    Hunt’s actions do not suggest an intent to abandon his
black iPhone or its data. The district court committed clear
error by finding otherwise. The serious injuries caused by
the shooting—and the traumatic and chaotic atmosphere
after—suggest that Hunt likely dropped the black iPhone and
16                       USA V. HUNT


did not intend to leave it behind. Considering the
circumstances, Hunt likely only intended to get medical
attention and flee from the shooter as soon as possible
without thinking or even knowing what happened to the
phone. This is distinguishable from the situation in Fisher,
where the Ninth Circuit found that the defendants—who sold
their house even though they knew that it contained a
cellphone and two hard drives in its attic—forfeited their
privacy interest in the devices and their content. See 56 F.4th
at 687.
    The district court acknowledged that Hunt “may have
dropped the phone in the course of being shot or fleeing,”
but reasoned that after the shooting, Hunt made no “apparent
effort to secure the black iPhone.” But the iPhone was later
found in the bushes and not plainly visible. Most people
would not scour the bushes after a shooting to find a phone
(assuming that Hunt even realized he had lost or dropped the
phone after being shot).
    The government also argues that Hunt abandoned the
black iPhone and its data by not trying to retrieve the phone
from the police. That is an important fact in assessing intent,
but there is no indication that Hunt realized that he left the
missing phone at the shooting scene for at least three
reasons. First, Hunt claims to not remember the shooting, so
he might not have known that he used the black iPhone at
the time and that the police had it. Second, the police
officers seized the white iPhone from Hunt’s person and
gave him a receipt for it, such that Hunt could have
reasonably expected the police to give him a receipt for the
black iPhone if they also had it. The police, however, did
not provide a receipt for the black iPhone. Third, Hunt
reasonably could have concluded that someone other than
the police picked up a valuable iPhone in a public parking
                         USA V. HUNT                        17


lot. We thus hold that the district court clearly erred in
finding that Hunt intended to abandon the black iPhone, and
it logically follows that he did not intend to abandon the data
in it.
    Even if we assume that Hunt had abandoned his black
iPhone by not trying to retrieve it from the police, we cannot
conclude that he also intended to abandon the data in his
phone without examining all the relevant facts. Unlike the
defendants in Fisher, Hunt did not willingly sell or give
away his black iPhone with all its personal data still intact.
See 56 F.4th at 687. Rather, he simply lost the phone during
a shooting. Though he did not follow up with the police, the
record does not establish that he had reason to suspect the
police collected the black iPhone from the crime scene. We
need not conduct a separate analysis of the stored data
because we hold that Hunt did not abandon his phone.
III. The government did not violate Hunt’s Fourth
     Amendment rights because it obtained a warrant to
     search the phone and did not hold it for an
     unreasonable period.
    While Hunt has standing to challenge the search of the
black iPhone’s data, his argument fails on the merits.
Federal agents obtained a warrant to search the iPhone’s
data. So Hunt can only complain that the government
violated the Fourth Amendment by seizing the data for an
unreasonably long period. This argument falls flat because
the Eugene police acted reasonably by collecting the iPhone
as evidence related to the shooting investigation and by
holding it until someone claimed it.
    The Fourth Amendment prohibits unreasonable searches
and seizures. Soldal v. Cook County, 506 U.S. 56, 61 (1992)
(citation modified). The Court, however, has recognized
18                      USA V. HUNT


that “special law enforcement needs, diminished
expectations of privacy, minimal intrusions, or the like” may
make a warrantless seizure reasonable. Illinois v. McArthur,
531 U.S. 326, 330 (2001). But “a seizure lawful at its
inception can nevertheless violate the Fourth Amendment
because its manner of execution unreasonably infringes
possessory interests.” United States v. Jacobsen, 466 U.S.
109, 124 (1984). To remain reasonable, a seizure must last
“no longer than reasonably necessary for the police, acting
with diligence, to obtain the warrant” to search the property.
McArthur, 531 U.S. at 332; see also United States v.
Sullivan, 797 F.3d 623, 633 (9th Cir. 2015).
    To decide whether a prolonged seizure remained
reasonable, we balance “the nature and quality of the
intrusion on the individual’s Fourth Amendment interests
against the importance of the governmental interests alleged
to justify the intrusion.” Sullivan, 797 F.3d at 633 (citation
omitted). The balance here favors the government.
    Given that Hunt lost his iPhone and never sought to
recover it, the Eugene police’s intrusion upon his possessory
interest was minimal at best. See id. (finding owner’s
inability to use a device reduced his possessory interest in
the device).
     On the other side of the ledger, the Eugene police had a
legitimate law enforcement reason to seize the black iPhone
as evidence for its investigation into the shooting. While the
iPhone might have belonged to a random passerby, its
proximity to the site of Hunt’s shooting gave police a basis
to suspect the iPhone could help identify the shooter, an
accomplice, or a witness. The police thus acted reasonably
by seizing the iPhone during the initial sweep of the parking
lot.
                         USA V. HUNT                        19


    Moreover, police had a legitimate law enforcement
reason to retain the iPhone after its initial collection simply
because it represented lost property with no identified owner
to whom the police could return it. Multiple state supreme
court cases note that the police often retain lost or mislaid
property in secure locations until the authorities can identify
the owner. See State v. Hamilton, 67 P.3d 871, 875 (Mont.
2003); State v. Ching, 678 P.2d 1088, 1093 (Haw. 1984); see
also State v. Kealey, 907 P.2d 319, 325 (Wash. Ct. App.
1995), as amended on denial of reconsideration (Feb. 26,
1996). Here, the record does not suggest that the Eugene
police did anything with the black iPhone other than hold it
in evidence.
                      CONCLUSION
   We AFFIRM the district court’s orders denying Hunt’s
motion to suppress and his recusal motion.

```

---

## GROUP: _overhaul2/lake/cases/United States v. Jackson.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Jackson"
type: case
citation: "784 F.3d 1227 (2015)"
parallel_cite: ""
neutral_cite: "2015 U.S. App. LEXIS 7397; 2015 WL 2048440"
court: "U.S. Court of Appeals, Eighth Circuit"
court_level: coa
circuit: 8th
year: 2015
date_decided: 2015-05-05
docket: ""
authority_weight: "Binding in-circuit — 8th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2015-05-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Jackson
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2798587/united-states-v-ac-jackson/"
  cluster_id: 2798587
  opinion_id: 2798587
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Leon]]", "[[Massachusetts v. Sheppard]]", "[[Herring v. United States]]"]
aliases: ["United States v. A.C. Jackson", "United States v. Jackson (8th Cir. 2015)"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "good-faith-exception", "leon", "search-warrant", "eighth-circuit"]
holding: "Although the warrant application failed to supply probable cause, the deputy acted in objectively reasonable good faith (affidavit…"
lake:
  record_id: United States v. Jackson
  status: verified
  projected_at: 2026-07-09
---

# United States v. Jackson

*784 F.3d 1227 (8th Cir. 2015)* · U.S. Court of Appeals, Eighth Circuit · **Binding in-circuit — 8th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A.C. Jackson reported a stolen firearm to a Wayne County, Missouri deputy; investigating, the deputy concluded the report was false and developed information that Jackson — a felon — possessed firearms. The deputy prepared an affidavit (reviewed and approved by the prosecutor), and a judge issued a search warrant after questioning him; the search of Jackson's home produced a firearm. The district court found the warrant was *not* supported by a substantial basis for probable cause, but denied suppression under the [[United States v. Leon]] [[The Good-Faith Exception|good-faith exception]]. Jackson, convicted of felon-in-possession, appealed.

## Issue
Whether the *[[United States v. Leon|Leon]]* [[The Good-Faith Exception|good-faith exception]] to the exclusionary rule allows admission of evidence seized under a search warrant that the district court found was not supported by probable cause, where the officer's reliance on the warrant was objectively reasonable.

## Rule
Yes. The exclusionary rule "does not apply 'when an officer acting with objective good faith has obtained a search warrant from a judge or magistrate and acted within its scope.'" — 784 F.3d at 1231 (quoting [[United States v. Leon]], 468 U.S. at 921). ^pin-1231

The dispositive question is whether the officer's reliance on the warrant was objectively reasonable, not whether the warrant was in fact supported by probable cause.

Applying that standard, the court held: "We find the actions of the deputy in executing the search warrant were taken in objectively reasonable good faith considering the deputy's knowledge and actions, the review and approval of the warrant application by the prosecutor, and the issuance of the warrant by Judge Shuller after the deputy responded to his specific questions." — *Id.* at 1232. ^pin-1232

## Application
On these facts the [[The Good-Faith Exception|good-faith exception]] applied even though the warrant lacked probable cause. The affidavit was not so "lacking in indicia of probable cause as to render official belief in its existence unreasonable": the deputy based it on his interviews of Jackson, Jackson's nephew, and Elledge; he had the prosecutor review and approve the application; and the judge issued the warrant only after asking the deputy additional questions. The court also rejected Jackson's *[[Franks v. Delaware|Franks]]* argument that the affidavit's "found the report to be false" statement was a knowing or reckless falsehood, and found no evidence the judge "wholly abandoned his judicial role." Because the deputy's reliance was objectively reasonable, "it is unnecessary to address whether the initial warrant contained sufficient probable cause." — [*Id.* at 1232](https://www.courtlistener.com/opinion/2798587/united-states-v-ac-jackson/#:~:text=lacking%20in%20indicia%20of%20probable%20cause%20as%20to%20render%20official%20belief%20in%20its%20existence%20unreasonable). ^pin-1232a

## Conclusion
The *[[United States v. Leon|Leon]]* [[The Good-Faith Exception|good-faith exception]] applied, and the evidence was admissible despite the warrant's lack of probable cause; the denial of suppression was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 8th Cir.**
- No negative subsequent treatment identified. The decision applies [[United States v. Leon]] / [[Massachusetts v. Sheppard]] good-faith reliance — good faith was *applied* to save the evidence (not held unavailable) — making it unnecessary to resolve the underlying probable-cause question.

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *United States v. A.C. Jackson*, 784 F.3d 1227 (8th Cir. 2015) — https://www.courtlistener.com/opinion/2798587/united-states-v-ac-jackson/ — pinpoints: 1231, 1232.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5788bf01ae9acf74", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Jackson"}, "payload": {"all": [{"cite": "784 F.3d 1227", "page": "1227", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "784"}, {"cite": "2015 U.S. App. LEXIS 7397", "page": "7397", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2015"}, {"cite": "2015 WL 2048440", "page": "2048440", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2015"}], "display": "784 F.3d 1227", "official": {"cite": "784 F.3d 1227", "page": "1227", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "784"}, "official_selection_present": true, "record_id": "United States v. Jackson"}}
{"assertion_id": "c2ad63e6ac1a9f32", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1232", "record_id": "United States v. Jackson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1232", "pinpoint_status": "slip-only", "quote": "We find the actions of the deputy in executing the search warrant were taken in objectively reasonable good faith considering the deputy's knowledge and actions, the review and approval of the warrant application by the prosecutor, and the issuance of the warrant by Judge Shuller after the deputy responded to his specific questions.", "quote_fidelity": "mismatch", "record_id": "United States v. Jackson", "star_marker": null}}
{"assertion_id": "d69b6317e061f7bf", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1231", "record_id": "United States v. Jackson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1231", "pinpoint_status": "slip-only", "quote": "--- # United States v. Jackson *784 F.3d 1227 (8th Cir. 2015)* · U.S. Court of Appeals, Eighth Circuit · **Binding in-circuit — 8th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A.C. Jackson reported a stolen firearm to a Wayne County, Missouri deputy; investigating, the deputy concluded the report was false and developed information that Jackson — a felon — possessed firearms. The deputy prepared an affidavit (reviewed and approved by the prosecutor), and a judge issued a search warrant after questioning him; the search of Jackson's home produced a firearm. The district court found the warrant was *not* supported by a substantial basis for probable cause, but denied suppression under the [[United States v. Leon]] good-faith exception. Jackson, convicted of felon-in-possession, appealed. ## Issue Whether the *Leon* good-faith exception to the exclusionary rule allows admission of evidence seized under a search warrant that the district court found was not supported by probable cause, where the officer's reliance on the warrant was objectively reasonable. ## Rule Yes. The exclusionary rule", "quote_fidelity": "mismatch", "record_id": "United States v. Jackson", "star_marker": null}}
{"assertion_id": "d98e65696e8b9ccf", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1232a", "record_id": "United States v. Jackson"}, "payload": {"fragment": "#:~:text=lacking%20in%20indicia%20of%20probable%20cause%20as%20to%20render%20official%20belief%20in%20its%20existence%20unreasonable", "page": null, "pin_id": "pin-1232a", "pinpoint_status": "slip-only", "quote": "lacking in indicia of probable cause as to render official belief in its existence unreasonable", "quote_fidelity": "matched", "record_id": "United States v. Jackson", "star_marker": null}}
{"assertion_id": "9133cd5b42a994d1", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Jackson"}, "payload": {"as_of_content": "2015-05-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Jackson", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Jackson

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Jackson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. A.C. Jackson",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee v. A.C. JACKSON, Defendant-Appellant",
    "input_case_name": "United States v. Jackson",
    "court": "U.S. Court of Appeals, Eighth Circuit",
    "court_id": "ca8",
    "court_level": "coa",
    "circuit": "8th",
    "state": null,
    "date_decided": "2015-05-05",
    "year": 2015,
    "docket": null,
    "cluster_id": 2798587,
    "lead_opinion_id": 2798587,
    "sibling_ids": [
      2798587
    ],
    "absolute_url": "/opinion/2798587/united-states-v-ac-jackson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "784 F.3d 1227",
      "volume": "784",
      "reporter": "F.3d",
      "page": "1227",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2015 U.S. App. LEXIS 7397",
        "volume": "2015",
        "reporter": "U.S. App. LEXIS",
        "page": "7397",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 WL 2048440",
        "volume": "2015",
        "reporter": "WL",
        "page": "2048440",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "784 F.3d 1227",
        "volume": "784",
        "reporter": "F.3d",
        "page": "1227",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 U.S. App. LEXIS 7397",
        "volume": "2015",
        "reporter": "U.S. App. LEXIS",
        "page": "7397",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 WL 2048440",
        "volume": "2015",
        "reporter": "WL",
        "page": "2048440",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "784 F.3d 1227",
    "official_selection": {
      "court_class": "coa",
      "selected": "784 F.3d 1227",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1231",
      "page": null,
      "quote": "--- # United States v. Jackson *784 F.3d 1227 (8th Cir. 2015)* \u00b7 U.S. Court of Appeals, Eighth Circuit \u00b7 **Binding in-circuit \u2014 8th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A.C. Jackson reported a stolen firearm to a Wayne County, Missouri deputy; investigating, the deputy concluded the report was false and developed information that Jackson \u2014 a felon \u2014 possessed firearms. The deputy prepared an affidavit (reviewed and approved by the prosecutor), and a judge issued a search warrant after questioning him; the search of Jackson's home produced a firearm. The district court found the warrant was *not* supported by a substantial basis for probable cause, but denied suppression under the [[United States v. Leon]] good-faith exception. Jackson, convicted of felon-in-possession, appealed. ## Issue Whether the *Leon* good-faith exception to the exclusionary rule allows admission of evidence seized under a search warrant that the district court found was not supported by probable cause, where the officer's reliance on the warrant was objectively reasonable. ## Rule Yes. The exclusionary rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1232",
      "page": null,
      "quote": "We find the actions of the deputy in executing the search warrant were taken in objectively reasonable good faith considering the deputy's knowledge and actions, the review and approval of the warrant application by the prosecutor, and the issuance of the warrant by Judge Shuller after the deputy responded to his specific questions.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1232a",
      "page": null,
      "quote": "lacking in indicia of probable cause as to render official belief in its existence unreasonable",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 6617,
      "fragment": "#:~:text=lacking%20in%20indicia%20of%20probable%20cause%20as%20to%20render%20official%20belief%20in%20its%20existence%20unreasonable",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2015-05-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Jackson",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Martece Saddler",
          "cluster_id": 5302782,
          "cite": [
            "19 F.4th 1035"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jackson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2798587) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca8)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(2798587)",
        "reviewed": 1,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(2798587)",
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
    "complete_query": "cites:(2798587)",
    "indexed_citing_opinions": 1,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2798587,
        "count": 1,
        "count_source": "search"
      }
    ],
    "citation_count": 16,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-jackson.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 1,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2798587,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2798587,
        "cited_id": 217177,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2798587,
        "cited_id": 620683,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2798587,
        "cited_id": 797654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2798587,
        "cited_id": 1468561,
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
    "date_created": "2026-07-06T00:43:08Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:43:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:43:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:44:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:43:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Jackson

```
                 United States Court of Appeals
                            For the Eighth Circuit
                        ___________________________

                                No. 14-1957
                        ___________________________

                             United States of America

                        lllllllllllllllllllll Plaintiff – Appellee

                                           v.

                                    A.C. Jackson

                      lllllllllllllllllllll Defendant – Appellant
                                      ____________

                     Appeal from United States District Court
               for the Eastern District of Missouri - Cape Girardeau
                                  ____________

                            Submitted: March 13, 2015
                               Filed: May 5, 2015
                                 ____________

Before MURPHY and SHEPHERD, Circuit Judges, and HARPOOL,1 District
Judge.
                         ____________

HARPOOL, District Judge.

       A.C. Jackson was convicted on two counts of felon in possession of a
firearm in violation of 18 U.S.C. § 922(g)(1). Jackson now appeals the district


      1
        The Honorable Douglas Harpool, United States District Judge for the Western
District of Missouri, sitting by designation.
court’s2 denial of his motion to suppress. Specifically, Jackson argues the district
court erred in finding that while the application for the search warrant failed to
supply probable cause for its issuance, the Leon good faith exception to the
exclusionary rule allowed the admission of evidence. We affirm.

                                         I.

      On March 28, 2013, a Wayne County, Missouri deputy received a call from
a dispatcher that a man wanted to report that his firearm had been stolen. When
the deputy arrived at the home of Bob Elledge he discovered the man reporting the
stolen firearm was the Defendant, A.C. Jackson. A Missouri Highway Patrol
Trooper arrived shortly thereafter to assist.

       Defendant informed the deputy that he had purchased a .22 caliber rifle from
Elledge for $200 and that Defendant’s nephew, Bobby Joe Jackson, had stolen the
rifle. When the deputy stepped outside to speak with the trooper, she informed
him Defendant was a previously convicted felon with numerous armed criminal
actions on his criminal history report.

       The officers proceeded to contact the nephew, Bobby Joe Jackson. The
nephew informed the officers he was involved in a dispute with Defendant and
feared for his life. He stated Defendant had threatened to shoot him. Bobby Joe
Jackson stated he had told Elledge this story and asked if he could take the gun to
feel safer and keep the gun away from Defendant. Elledge had agreed to give the



       2
       The Honorable Stephen N. Limbaugh, Jr., United States District Court
Judge for the Eastern District of Missouri, adopting, in part, the report and
recommendation of the Honorable Lewis M. Blanton, United States Magistrate
Judge for the Eastern District of Missouri.

                                        -2-
gun to the nephew. In addition, Defendant’s nephew informed the officers there
was another gun, a multi-barreled firearm, located in Defendant’s home.

       After questioning the nephew, the officers again questioned Defendant.
Defendant denied having any firearms in his home. He stated he had purchased the
.22 caliber rifle as an investment, and since it was not in his home he did not think
he had broken any rules. The deputy asked to search Defendant’s home but he
declined stating the deputy would have to get a warrant. The officers then arrested
Defendant and took pictures of his home to use in the application of a search
warrant.

      The deputy then prepared an affidavit for the application of a search warrant.
The affidavit contained the following sworn statement of probable cause for the
search:

      I am a member of Wayne County Sheriff’s Department. I am a
      certified Peace Officer in the State of Missouri and have been since
      2011. I have training in investigations and have been involved in
      investigations that have led to favorable conclusions.

      On Thursday, March 28, 2013, this officer received information of a
      possible stolen firearm from AC Jackson. Upon investigating said
      report this Officer found the report to be false. This Officer received
      information that AC Jackson was to be [sic] a convicted felon and to
      be in possession of other firearms at his residence on Hurley DR,
      Wappapello, Missouri. This Officer request Jackson to check his
      residence for firearms wherein he refused. This Officer has reason to
      believe there are more firearms at Jackson’s residence. This Officer
      has a statement confirming presence of firearms and ammunition at
      this trailer.

      The prosecuting attorney reviewed the application and approved it. The
deputy then presented the search warrant affidavit and application to Wayne
County, Missouri, Circuit Judge Randy Shuller. Judge Shuller asked the deputy
                                     -3-
some questions about the case and the basis for the warrant and then signed the
warrant.

       When the officers executed the warrant they discovered a Rossi multi-
barreled firearm and ammunition in the Defendant’s home. Defendant later
admitted he had purchased the .22 caliber rifle that he had previously reported
stolen, but denied the Rossi multi-barreled firearm found in his home was his.
Defendant claimed the Rossi firearm belonged to his nephew.

       Defendant was indicted for being a felon in possession of a firearm based on
the .22 caliber rifle he reported stolen and the Rossi multi-barrel firearm found in
his home. Defendant filed a motion to suppress the Rossi multi-barreled firearm,
arguing any evidence obtained during the course of the execution of the search
warrant should be excluded on the grounds that the warrant was issued in violation
of the Fourth Amendment of the Constitution of the United States because it lacked
probable cause or a reasonable basis for authorizing the search.

       After conducting a hearing on the motion to suppress, the magistrate judge
issued his report and recommendation.                 The magistrate’s report and
recommendation stated, “considering all the circumstances of Deputy Hanger’s
interaction with Judge Shuller, including the oral interchange,” Judge Shuller had a
susbstantial basis for concluding probable cause existed. The magistrate further
stated that if his report and recommendation on probable cause was found to be
incorrect by the district court, then the good faith exception should be applied.

       The district court ultimately denied the motion to suppress, adopting in part,
the magistrate judge’s report and recommendation. In doing so, the district court
stated it did not find “Judge Shuller had a substantial basis for … concluding that
probable cause existed [for issuance of the search warrant],” but instead held that
the “good faith” exception under Leon applied to the search.

                                         -4-
      The jury returned a verdict of guilty on both counts and Defendant was
sentenced to 210 months on each of the counts, to run concurrently. Defendant
now appeals the denial of his motion to suppress.

                                        II.

      Defendant argues the warrant in this case was based on an affidavit “so
lacking in indicia of probable cause as to render official belief in its existence
unreasonable” and therefore that the officers unlawfully obtained the Rossi firearm
from his home. Citing United States v. Leon, 468 U.S. 897, 104 S. Ct. 3405, 3421,
82 L. Ed. 2d 677 (1984). Defendant further contends the district court erred in
applying the good faith exception to allow for the introduction of the evidence
found by the officers executing the warrant.

       “On appeal from the denial of a motion to suppress, we review a district
court’s findings of fact for clear error and its determination of probable cause and
the application of the Leon exception de novo.” United States v. Houston, 665
F.3d 991, 994 (8th Cir. 2012), citing United States v. Perry, 531 F.3d 662, 665 (8th
Cir. 2008).

       “The Fourth Amendment commands that no warrants shall issue, but upon
probable cause, supported by Oath or affirmation.” United States v. Fiorito, 640
F.3d 338, 345 (8th Cir. 2011). “The ordinary sanction for police violation of
Fourth Amendment limitations has long been suppression of the evidentiary fruits
of the transgression.” Id. Yet, this exclusionary rule does not apply “when an
officer acting with objective good faith has obtained a search warrant from a judge
or magistrate and acted within its scope.” United States v. Leon, 468 U.S. at 921,
104 S.Ct. 3405. A court may consider whether the good-faith exception applies
before conducting a probable cause analysis. United States v. Proell, 485 F.3d 427,
430 (8th Cir. 2007).

                                        -5-
       Under the good-faith exception, evidence seized pursuant to a search warrant
later determined to be invalid, will not be suppressed if the executing officer’s
reliance upon the warrant was objectively reasonable. Id. The court must look at
the objectively ascertainable question of whether a reasonably well trained officer
would have known that the search was illegal despite a judge’s issuance of the
warrant. Id., citing United States v. Puckett, 466 F.3d 626, 630 (8th Cir. 2006).

      There are four situations when the good-faith exception would not apply:

      (1) when the affidavit or testimony supporting the warrant contained a
      false statement made knowingly and intentionally or with reckless
      disregard for its truth, thus misleading the issuing judge;
      (2) when the issuing judge “wholly abandoned his judicial role” in
      issuing the warrant;
      (3) when the affidavit in support of the warrant is “so lacking in
      indicia of probable cause as to render official belief in its existence
      entirely unreasonable;” and
      (4) when the warrant is “so facially deficient” that no police officer
      could reasonably presume the warrant to be valid.

Id. at 431, citing Leon, 468 U.S. at 923, 104 S.Ct. 3405.

      In assessing the objective reasonableness of a police officer’s execution of a
warrant, we must look to the totality of the circumstances, including any
information known to the officer but not presented to the issuing judge. Id. at 995.

       In this instance, the deputy preparing the affidavit for the search warrant
application had interviewed the Defendant, the Defendant’s nephew and a
neighbor. He had also viewed the location where the alleged firearm was located.
The deputy had knowledge that Defendant was a convicted felon. The deputy
prepared his affidavit based on the first hand information he obtained from
interviewing the three individuals and his knowledge that the interviews
corroborated the allegations regarding the firearms. Further, the deputy had the
                                        -6-
affidavit reviewed and approved by the prosecutor before submitting it to the court.
The Judge then signed the warrant after the deputy answered the judge’s additional
questions about the search warrant application.

       We find the actions of the deputy in executing the search warrant were taken
in objectively reasonable good faith considering the deputy’s knowledge and
actions, the review and approval of the warrant application by the prosecutor, and
the issuance of the warrant by Judge Shuller after the deputy responded to his
specific questions.

       Defendant further argues the good faith exception should not apply because
the affidavit contained false information. Defendant contends the deputy’s
statement “…this officer received information of a possible stolen firearm from
AC Jackson. Upon investigating said report this Officer found the report to be
false,” constitutes false information or a statement made with reckless disregard for
the truth.

       Again, the deputy prepared his affidavit based on the information he
received from his interviews of the Defendant, Defendant’s nephew and Elledge.
Considering the information he gained from those interviews, it is reasonable to
conclude the deputy believed Defendant’s nephew had asked Elledge to give him
the firearm in order to protect himself. Further, based on the information available
to the Deputy, it was reasonable for him to believe the firearm was not stolen, but
was rather given to the nephew to protect himself from being shot and that the
nephew did not intend to take permanent possession of the firearm.

       We further find no evidence Judge Shuller wholly abandoned his judicial
role in the issuance of the warrant. In fact, Judge Shuller made inquiry beyond the
affidavit, discussing the case with the deputy, before issuing the warrant.


                                         -7-
       Because we find that the good faith exception under Leon applies, it is
unnecessary to address whether the initial warrant contained sufficient probable
cause.
                                     III.

      Accordingly, we affirm the district court’s denial of Defendant’s motion to
suppress.
                     ______________________________




                                        -8-

```

---
