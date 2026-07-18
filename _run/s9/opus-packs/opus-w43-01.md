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

## GROUP: content/cases/Ybarra v. Illinois.md  (`case`, 7 assertions)

### content_page

```
---
title: "Ybarra v. Illinois"
type: case
citation: "444 U.S. 85 (1979)"
parallel_cite: "100 S. Ct. 338; 62 L. Ed. 2d 238"
neutral_cite: 1979 U.S. LEXIS 151
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-11-28
docket: 78-5937
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1979-11-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Ybarra v. Illinois
  varies_by_point: false
  scope_note: "Good law; the rule that a premises warrant confers no authority to search persons merely present remains controlling. Distinct from Michigan v. Summers / Bailey v. United States, which permit detaining occupants during execution of a premises warrant."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110158/ybarra-v-illinois/"
  cluster_id: 110158
  opinion_id: 9427721
  identity_checked: true
homes:
  - page: "[[Detention and Search of Persons at the Scene]]"
    role: "Key — Limits / Narrows"
  - page: "[[Securing the Scene]]"
    role: "Related (scene-securing overlap)"
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Related (cross-doctrine)"
related: ["[[Michigan v. Summers]]", "[[Bailey v. United States]]", "[[Terry v. Ohio]]", "[[Maryland v. Buie]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrants", "search-of-persons", "terry-frisk", "probable-cause"]
holding: "A warrant to search premises does not authorize searching persons who merely happen to be present; a search or frisk of a person requires cause particularized to that person — probable cause to search, or for a Terry frisk reasonable suspicion that the person is armed and dangerous."
lake:
  record_id: Ybarra v. Illinois
  status: verified
  projected_at: 2026-07-10
---

# Ybarra v. Illinois

*444 U.S. 85 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers obtained a warrant to search the Aurora Tap Tavern and its bartender, "Greg," for heroin, based on an informant who reported seeing heroin on Greg and in a drawer behind the bar. Executing the warrant, officers patted down every patron present, including Ybarra, a customer about whom they knew nothing. The first patdown detected a cigarette pack; an officer later retrieved it and found heroin inside. Ybarra moved to suppress.

## Issue
Whether a warrant authorizing the search of a tavern and its bartender permits officers to search a patron who merely happens to be present, and whether the patdown of that patron was a valid *[[Terry v. Ohio|Terry]]* frisk.

## Rule
No. A premises warrant does not reach the persons of those merely present; cause must be individualized. "[A] person's mere propinquity to others independently suspected of criminal activity does not, without more, give rise to probable cause to search that person." — 444 U.S. at 91. ^pin-91

"Where the standard is probable cause, a search or seizure of a person must be supported by probable cause particularized with respect to that person." — [*Id.*](https://www.courtlistener.com/opinion/110158/ybarra-v-illinois/#:~:text=Where%20the%20standard%20is%20probable) ^pin-91a

A protective frisk likewise demands individualized suspicion: "The initial frisk of Ybarra was simply not supported by a reasonable belief that he was armed and presently dangerous, a belief which this Court has invariably held must form the predicate to a patdown of a person for weapons." — *Id.* at 92–93. ^pin-92

## Application
The warrant and its supporting complaint named only the tavern and "Greg" and said nothing about patrons, so there was no probable cause to search Ybarra when the warrant issued or when it was executed. On entering, the officers did not recognize Ybarra, and he made no suspicious gestures or movements; the most the officer could cite was that Ybarra wore a 3/4-length lumber jacket common to any tavern patron in an Illinois March. With neither probable cause particularized to Ybarra nor any articulable basis to believe he was armed and dangerous, both the frisk and the ensuing pocket search were unlawful.

## Conclusion
The search of Ybarra violated the Fourth Amendment and the heroin should have been suppressed. A warrant to search premises gives officers no authority to search the persons of those who merely happen to be present.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Ybarra* remains good law. It limits what a premises warrant authorizes as to persons; it is distinct from (and not disturbed by) [[Michigan v. Summers]] and [[Bailey v. United States]], which permit *detaining* occupants incident to executing a premises warrant but do not authorize searching them without individualized cause.

## Appears on
- [[Securing the Scene]] — *Limits / Narrows*
- [[Terry Stops and Reasonable Suspicion]] — *Related (cross-doctrine)*

## Sources
- *Ybarra v. Illinois*, 444 U.S. 85 (1979) — https://www.courtlistener.com/opinion/110158/ybarra-v-illinois/ — pinpoints: 91, 92–93.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "79fe0133f28e2199", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "444 U.S. 85 (1979)", "court": "U.S. Supreme Court", "neutral_cite": "1979 U.S. LEXIS 151", "official_citation_present": true, "parallel_cite": "100 S. Ct. 338; 62 L. Ed. 2d 238", "title": "Ybarra v. Illinois", "year": "1979"}}
{"assertion_id": "19b1034e41074122", "dimension": "support", "kind": "home_role", "locator": {"home": "Detention and Search of Persons at the Scene"}, "payload": {"home": "Detention and Search of Persons at the Scene", "role": "Key — Limits / Narrows", "title": "Ybarra v. Illinois"}}
{"assertion_id": "797e28819e966f85", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Related (cross-doctrine)", "title": "Ybarra v. Illinois"}}
{"assertion_id": "8ce9f69301731648", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrant to search premises does not authorize searching persons who merely happen to be present; a search or frisk of a person requires cause particularized to that person — probable cause to search, or for a Terry frisk reasonable suspicion that the person is armed and dangerous.", "title": "Ybarra v. Illinois"}}
{"assertion_id": "cb0c88a435588c41", "dimension": "support", "kind": "home_role", "locator": {"home": "Securing the Scene"}, "payload": {"home": "Securing the Scene", "role": "Related (scene-securing overlap)", "title": "Ybarra v. Illinois"}}
{"assertion_id": "20aa583956058590", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Ybarra v. Illinois"}}
{"assertion_id": "fc27cdaebd3b1be6", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1979-11-28", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Ybarra v. Illinois", "field_i_validity": "good_law", "scope_note": "Good law; the rule that a premises warrant confers no authority to search persons merely present remains controlling. Distinct from Michigan v. Summers / Bailey v. United States, which permit detaining occupants during execution of a premises warrant.", "title": "Ybarra v. Illinois", "varies_by_point": "false"}}
```

### lake record — Ybarra v. Illinois

```json
{
  "schema_version": "s2.v1",
  "record_id": "Ybarra v. Illinois",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Ybarra v. Illinois",
    "case_name_short": "Ybarra",
    "case_name_full": "Ybarra v. Illinois",
    "input_case_name": "Ybarra v. Illinois",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-11-28",
    "year": 1979,
    "docket": "78-5937",
    "cluster_id": 110158,
    "lead_opinion_id": 9427721,
    "sibling_ids": [
      110158,
      9427721,
      9427722,
      9427723
    ],
    "absolute_url": "/opinion/110158/ybarra-v-illinois/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "444 U.S. 85",
      "volume": "444",
      "reporter": "U.S.",
      "page": "85",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 338",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "338",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "62 L. Ed. 2d 238",
        "volume": "62",
        "reporter": "L. Ed. 2d",
        "page": "238",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 151",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "151",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "444 U.S. 85",
        "volume": "444",
        "reporter": "U.S.",
        "page": "85",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 338",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "338",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "62 L. Ed. 2d 238",
        "volume": "62",
        "reporter": "L. Ed. 2d",
        "page": "238",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 151",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "151",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "444 U.S. 85",
    "official_selection": {
      "court_class": "scotus",
      "selected": "444 U.S. 85",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-91",
      "page": null,
      "quote": "for heroin, based on an informant who reported seeing heroin on Greg and in a drawer behind the bar. Executing the warrant, officers patted down every patron present, including Ybarra, a customer about whom they knew nothing. The first patdown detected a cigarette pack; an officer later retrieved it and found heroin inside. Ybarra moved to suppress. ## Issue Whether a warrant authorizing the search of a tavern and its bartender permits officers to search a patron who merely happens to be present, and whether the patdown of that patron was a valid *Terry* frisk. ## Rule No. A premises warrant does not reach the persons of those merely present; cause must be individualized.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-91a",
      "page": null,
      "quote": "Where the standard is probable cause, a search or seizure of a person must be supported by probable cause particularized with respect to that person.",
      "star_marker": "91",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 9860,
      "fragment": "#:~:text=Where%20the%20standard%20is%20probable",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-92",
      "page": null,
      "quote": "The initial frisk of Ybarra was simply not supported by a reasonable belief that he was armed and presently dangerous, a belief which this Court has invariably held must form the predicate to a patdown of a person for weapons.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-11-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Ybarra v. Illinois",
    "varies_by_point": false,
    "scope_note": "Good law; the rule that a premises warrant confers no authority to search persons merely present remains controlling. Distinct from Michigan v. Summers / Bailey v. United States, which permit detaining occupants during execution of a premises warrant.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Ybarra v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Correll Thomas v. C. Dillard",
          "cluster_id": 3191530,
          "cite": [
            "818 F.3d 864",
            "2016 U.S. App. LEXIS 6210",
            "2016 WL 1319765"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Mercedes-De la Cruz",
          "cluster_id": 2803337,
          "cite": [
            "787 F.3d 61",
            "2015 U.S. App. LEXIS 8624",
            "2015 WL 3378255"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hubert v. State",
          "cluster_id": 1464366,
          "cite": [
            "312 S.W.3d 554",
            "2010 Tex. Crim. App. LEXIS 636",
            "2010 WL 2077166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Andrew Milton Flatter",
          "cluster_id": 795237,
          "cite": [
            "456 F.3d 1154",
            "2006 U.S. App. LEXIS 20435",
            "2006 WL 2269055"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Quigley",
          "cluster_id": 1925418,
          "cite": [
            "2005 VT 128",
            "892 A.2d 211",
            "179 Vt. 567",
            "2005 Vt. LEXIS 312"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ngai Man Lee",
          "cluster_id": 200295,
          "cite": [
            "317 F.3d 26",
            "2003 U.S. App. LEXIS 657",
            "2003 WL 133007"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Leday v. State",
          "cluster_id": 5269706,
          "cite": [
            "997 S.W.2d 406",
            "1999 Tex. App. LEXIS 6452",
            "1999 WL 650783"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Proctor",
          "cluster_id": 198057,
          "cite": [
            "148 F.3d 39",
            "1998 WL 377739"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fernando Vizcarra-Martinez",
          "cluster_id": 698348,
          "cite": [
            "57 F.3d 1506",
            "42 Fed. R. Serv. 215",
            "95 Daily Journal DAR 8123",
            "95 Cal. Daily Op. Serv. 4735",
            "1995 U.S. App. LEXIS 15146",
            "1995 WL 366970"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane1_negative"
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
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walczyk v. Rio",
          "cluster_id": 2704,
          "cite": [
            "496 F.3d 139",
            "2007 WL 2199005"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Club Retro, L.L.C. v. Hilton",
          "cluster_id": 1459439,
          "cite": [
            "568 F.3d 181",
            "2009 U.S. App. LEXIS 9864",
            "2006 WL 6245546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Glaser",
          "cluster_id": 2607117,
          "cite": [
            "902 P.2d 729",
            "11 Cal. 4th 354",
            "45 Cal. Rptr. 2d 425",
            "95 Daily Journal DAR 13816",
            "95 Cal. Daily Op. Serv. 8067",
            "1995 Cal. LEXIS 5961"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dudley Lee Berry, A/K/A David Sarver, United States of America v. Jessica Linda Ann Zabish, A/K/A Joanne Sarver",
          "cluster_id": 399309,
          "cite": [
            "670 F.2d 583",
            "1982 U.S. App. LEXIS 20874"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Dodt",
          "cluster_id": 5686979,
          "cite": [
            "61 N.Y.2d 408",
            "462 N.E.2d 1159",
            "474 N.Y.S.2d 441",
            "1984 N.Y. LEXIS 4120"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Freeman v. City of Santa Ana",
          "cluster_id": 7034204,
          "cite": [
            "68 F.3d 1180",
            "96 Cal. Daily Op. Serv. 25",
            "96 Daily Journal DAR 29",
            "1995 U.S. App. LEXIS 37134",
            "1995 WL 611554"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 1783262,
          "cite": [
            "658 S.W.2d 623",
            "1983 Tex. Crim. App. LEXIS 1212"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hosvaldo Lopez",
          "cluster_id": 797423,
          "cite": [
            "482 F.3d 1067",
            "2007 WL 725641",
            "2007 U.S. App. LEXIS 5709"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'HARA v. State",
          "cluster_id": 2275765,
          "cite": [
            "27 S.W.3d 548",
            "2000 Tex. Crim. App. LEXIS 83",
            "2000 WL 1347932"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin Davis (03-1451) and Keith Presley (03-1621)",
          "cluster_id": 792556,
          "cite": [
            "430 F.3d 345",
            "2005 U.S. App. LEXIS 25124",
            "2005 WL 3108503"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Micah J. Gourde",
          "cluster_id": 793638,
          "cite": [
            "440 F.3d 1065",
            "2006 U.S. App. LEXIS 5890",
            "2006 WL 574302"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oliveira v. Mayer",
          "cluster_id": 7028788,
          "cite": [
            "23 F.3d 642",
            "1994 WL 161075"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wright v. State",
          "cluster_id": 1870455,
          "cite": [
            "7 S.W.3d 148",
            "1999 Tex. Crim. App. LEXIS 146",
            "1999 WL 1178566"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dufort v. City of New York",
          "cluster_id": 8443570,
          "cite": [
            "874 F.3d 338",
            "2017 WL 4847620",
            "2017 U.S. App. LEXIS 21322"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michelletti",
          "cluster_id": 6205,
          "cite": [
            "13 F.3d 838",
            "1994 U.S. App. LEXIS 1229",
            "1994 WL 19106"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramirez v. City of Buena Park",
          "cluster_id": 1227729,
          "cite": [
            "560 F.3d 1012",
            "2009 U.S. App. LEXIS 6394",
            "2009 WL 764568"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Fernando Vizcarra-Martinez",
          "cluster_id": 705138,
          "cite": [
            "66 F.3d 1006"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hart v. O'Brien",
          "cluster_id": 13422,
          "cite": [
            "127 F.3d 424",
            "47 Fed. R. Serv. 1447",
            "1997 U.S. App. LEXIS 30452",
            "1997 WL 656282"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rivera v. United States",
          "cluster_id": 8996598,
          "cite": [
            "928 F.2d 592",
            "1991 U.S. App. LEXIS 4608",
            "1991 WL 37132"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Romain",
          "cluster_id": 201394,
          "cite": [
            "393 F.3d 63",
            "2004 WL 2997954"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Price v. Kramer",
          "cluster_id": 7079802,
          "cite": [
            "200 F.3d 1237",
            "2000 WL 14442"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Perry",
          "cluster_id": 3176980,
          "cite": [
            "292 Neb. 708",
            "874 N.W.2d 36"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. James",
          "cluster_id": 2127694,
          "cite": [
            "645 N.E.2d 195",
            "163 Ill. 2d 302",
            "206 Ill. Dec. 190",
            "1994 Ill. LEXIS 173"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ybarra v. Illinois:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110158 OR 9427721 OR 9427722 OR 9427723) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03OTM0MTEyMDAwMDAmcz0xNDk0MTU2JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110158+OR+9427721+OR+9427722+OR+9427723%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110158 OR 9427721 OR 9427722 OR 9427723)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDAmcz0zMjU4OSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110158+OR+9427721+OR+9427722+OR+9427723%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110158 OR 9427721 OR 9427722 OR 9427723)",
        "reviewed": 35,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 35,
        "triage_read": 1,
        "triage_snippet_classified": 34
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110158 OR 9427721 OR 9427722 OR 9427723)",
    "indexed_citing_opinions": 454,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110158,
        "count": 198,
        "count_source": "search"
      },
      {
        "opinion_id": 9427721,
        "count": 272,
        "count_source": "search"
      },
      {
        "opinion_id": 9427722,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427723,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2086,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/ybarra-v-illinois.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNDE5ODYmcz0xMDU4MTY5NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110158+OR+9427721+OR+9427722+OR+9427723%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110158,
        "cited_id": 100621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 108966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 109432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 109584,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 109953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 110100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 110127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 266664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 348314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 1545697,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 2141409,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 2281017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 2620876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 4004065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110158,
        "cited_id": 5171457,
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
    "date_created": "2026-07-06T04:55:11Z",
    "date_modified": "2026-07-10T00:12:42Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:55:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:55:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:59:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:55:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Ybarra v. Illinois

```
<opinion type="majority">
<author id="b233-5">Mr. Justice Stewart</author>
<p id="AmX">delivered the opinion of the Court.</p>
<p id="b233-6">An Illinois statute authorizes law enforcement officers to detain and search any person found on premises being searched pursuant to a search warrant, to protect themselves from attack or to prevent the disposal or concealment of anything described in the warrant.<footnotemark>1</footnotemark> The question before us is whether the application of this statute to the facts of the present case violated the Fourth and Fourteenth Amendments.</p>
<p id="b233-7">I</p>
<p id="b233-8">On March 1, 1976, a special agent of the Illinois Bureau of Investigation presented a "Complaint for Search Warrant” to a judge of an Illinois Circuit Court. The complaint recited that the agent had spoken with an informant known to the police to be reliable and:</p>
<blockquote id="b233-9">“3. The informant related . . . that over the weekend of 28 and 29 February he was in the [Aurora Tap Tavern, located in the city of Aurora, Ill.] and observed fif<page-number citation-index="1" label="88">*88</page-number>teen to twenty-five tin-foil packets on the person of the bartender 'Greg’ and behind the bar. He also has been in the tavern on at least ten other occasions and has observed tin-foil packets on ‘Greg’ and in a drawer behind the bar. The informant has used heroin in the past and knows that tin-foil packets are a common method of packaging heroin.</blockquote>
<blockquote id="b234-5">“4. The informant advised . . . that over the weekend of 28 and 29 February he had a conversation with ‘Greg’ and was advised that ‘Greg’ would have heroin for sale on Monday, March 1, 1976. This conversation took place in the tavern described.”</blockquote>
<p id="b234-6">On the strength of this complaint, the judge issued a warrant authorizing the search of “the following person or place: . . . [T]he Aurora Tap Tavern. . . . Also the person of ‘Greg’, the bartender, a male white with blondish hair appx. 25 years.” The warrant authorized the police to search for “evidence of the offense of possession of a controlled substance,” to wit, “[h]eroin, contraband, other controlled substances, money, instrumentalities and narcotics, paraphernalia used in the manufacture, processing and distribution of controlled substances.”</p>
<p id="b234-7">In the late afternoon of that day, seven or eight officers proceeded to the tavern. Upon entering it, the officers announced their purpose and advised all those present that they were going to conduct a “cursory search for weapons.” One of the officers then proceeded to pat down each of the 9 to 13 customers present in the tavern, while the remaining officers engaged in an extensive search of the premises.</p>
<p id="b234-8">The police officer who frisked the patrons found the appellant, Ventura Ybarra, in front of the bar standing by a pinball machine. In his first patdown of Ybarra, the officer felt what he described as “a cigarette pack with objects in it.” He did not remove this pack from Ybarra’s pocket. Instead, he moved on and proceeded to pat down other customers. <page-number citation-index="1" label="89">*89</page-number>After completing this process the officer returned to Ybarra and frisked him once again. This second search of Ybarra took place approximately 2 to 10 minutes after the first. The officer relocated and retrieved the cigarette pack from Ybarra’s pants pocket. Inside the pack he found six tinfoil packets containing a brown powdery substance which later turned out to be heroin.</p>
<p id="b235-5">Ybarra was subsequently indicted by an Illinois grand jury for the unlawful possession of a controlled substance. He filed a pretrial motion to suppress all the contraband that had been seized from his person at the Aurora Tap Tavern. At the hearing on this motion the State sought to justify the search by reference to the Illinois statute in question. The trial court denied the motion to suppress, finding that the search had been conducted under the authority of subsection (b) of the statute, to “prevent the disposal or concealment of [the] things particularly described in the warrant.” The case proceeded to trial before the court sitting without a jury, and Ybarra was found guilty of the possession of heroin.</p>
<p id="b235-6">On appeal, the Illinois Appellate Court held that the Illinois statute was not unconstitutional “in its application to the facts” of this case. <span class="citation" data-id="2015587"><a href="/opinion/2015587/people-v-ybarra/#64" aria-description="Citation for case: People v. Ybarra">58 Ill. App. 3d 57, 64</a></span>, <span class="citation" data-id="2015587"><a href="/opinion/2015587/people-v-ybarra/#1017" aria-description="Citation for case: People v. Ybarra">373 N. E. 2d 1013, 1017</a></span>. The court acknowledged that, had the warrant directed that a “large retail or commercial establishment” be searched, the statute could not constitutionally have been read to “authorize a ‘blanket search’ of persons or patrons found” therein. <span class="citation" data-id="2015587"><a href="/opinion/2015587/people-v-ybarra/#62" aria-description="Citation for case: People v. Ybarra"><em>Id., </em>at 62</a></span>, <span class="citation" data-id="2015587"><a href="/opinion/2015587/people-v-ybarra/#1016" aria-description="Citation for case: People v. Ybarra">373 N. E. 2d, at 1016</a></span>. The court interpreted the statute as authorizing the search of persons found on premises described in a warrant only if there is “some showing of a connection with those premises, that the police officer reasonably suspected an attack, or that the person searched would destroy or conceal items described in the warrant.” <span class="citation" data-id="2015587"><a href="/opinion/2015587/people-v-ybarra/#61" aria-description="Citation for case: People v. Ybarra"><em>Id., </em>at 61</a></span>, <span class="citation" data-id="2015587"><a href="/opinion/2015587/people-v-ybarra/#1016" aria-description="Citation for case: People v. Ybarra">373 N. E. 2d, at 1016</a></span>. Accordingly, the State Appellate Court found that the search of Ybarra had been constitutional because it had been “conducted in a <page-number citation-index="1" label="90">*90</page-number>one-room bar where it [was] obvious from the complaint . . . that heroin was being sold or dispensed,” <span class="citation" data-id="2015587"><a href="/opinion/2015587/people-v-ybarra/#62" aria-description="Citation for case: People v. Ybarra"><em>id., </em>at 62</a></span>, <span class="citation" data-id="2015587"><a href="/opinion/2015587/people-v-ybarra/#1016" aria-description="Citation for case: People v. Ybarra">373 N. E. 2d, at 1016</a></span>, because “the six packets of heroin . . . could easily ¡[have been] concealed by the defendant and thus thwart the purpose of the warrant,” <span class="citation" data-id="2015587"><a href="/opinion/2015587/people-v-ybarra/#61" aria-description="Citation for case: People v. Ybarra"><em>id., </em>at 61</a></span>, <span class="citation" data-id="2015587"><a href="/opinion/2015587/people-v-ybarra/#1016" aria-description="Citation for case: People v. Ybarra">373 N. E. 2d, at 1016</a></span>, and because Ybarra was not an “innocent strange[r] having no connection with the' premises,” <em><span class="citation" data-id="2015587"><a href="/opinion/2015587/people-v-ybarra/" aria-description="Citation for case: People v. Ybarra">ibid.</a></span> </em>The court, therefore, affirmed Ybarra’s conviction, and the Illinois Supreme Court denied his petition for leave to appeal. There followed an appeal to this Court, and we noted probable jurisdiction. <span class="citation no-link">440 U. S. 790</span>.</p>
<p id="b236-5">II</p>
<p id="b236-6">There is no reason to suppose that, when the search warrant was issued on March 1, 1976, the authorities had probable cause to believe that any person found on the premises of the Aurora Tap Tavern, aside from “Greg,” would be violating the law.<footnotemark>2</footnotemark> The search warrant complaint did not allege that the bar was frequented by persons illegally purchasing drugs. It did not state that the informant had ever seen a patron of the tavern purchase drugs from “Greg” or from any other person. Nowhere, in fact, did the complaint even mention the patrons of the Aurora Tap Tavern.</p>
<p id="b236-7">Not only was probable cause to search Ybarra absent at the time the warrant was issued, it was still absent when the police executed the warrant. Upon entering the tavern, the <page-number citation-index="1" label="91">*91</page-number>police did not recognize Ybarra and had no reason to believe that he had committed, was committing, or was about to commit any offense under state or federal law. Ybarra made no gestures indicative of criminal conduct, made no movements that might suggest an attempt to conceal contraband, and said nothing of a suspicious nature to the police officers. In short, the agents knew nothing in particular about Ybarra, except that he was present, along with several other customers, in a public tavern at a time when the police had reason to believe that the bartender would have heroin for sale.</p>
<p id="b237-5">It is true that the police possessed a warrant based on probable cause to search the tavern in which Ybarra happened to be at the time the warrant was executed.<footnotemark>3</footnotemark> But, a person’s mere propinquity to others independently suspected of criminal activity does not, without more, give rise to probable cause to search that person. <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#62" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 62-63</a></span>. Where the standard is probable cause, a search or seizure of a person must be supported by probable cause particularized with respect to that person. This requirement cannot be undercut or avoided by simply pointing to the fact that coincidentally there exists probable cause to search or seize another or to search the premises where the person may happen to be. The Fourth and Fourteenth Amendments protect the “legitimate expectations of privacy” of persons, not places. See <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#138" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 138-143, 148-149</a></span>; <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351-352</a></span>.</p>
<p id="b237-6">Each patron who walked into the Aurora Tap Tavern on March 1, 1976, was clothed with constitutional protection against an unreasonable search or an unreasonable seizure. That individualized protection was separate and distinct from <page-number citation-index="1" label="92">*92</page-number>the Fourth and Fourteenth Amendment protection possessed by the proprietor of the tavern or by “Greg.” Although the search warrant, issued upon probable cause, gave the officers authority to search the premises and to search “Greg,” it gave them no authority whatever to invade the constitutional protections possessed individually by the tavern's customers.<footnotemark>4</footnotemark></p>
<p id="b238-5">Notwithstanding the absence of probable cause to search Ybarra, the State argues that the action of the police in searching him and seizing what was found in his pocket was nonetheless constitutionally permissible. We are asked to find that the first patdown search of Ybarra constituted a reasonable frisk for weapons under the doctrine of <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span>. If this finding is made, it is then possible to conclude, the State argues, that the second search of Ybarra was constitutionally justified. The argument is that the pat-down yielded probable cause to believe that Ybarra was carrying narcotics, and that this probable cause constitutionally supported the second search, no warrant being required in light of the exigencies of the situation coupled with the ease with which Ybarra could have disposed of the illegal substance.</p>
<p id="b238-6">We are unable to take even the first step required by this argument. The initial frisk of Ybarra was simply not supported by a reasonable belief that he was armed and presently <page-number citation-index="1" label="93">*93</page-number>dangerous, a belief which this Court has invariably held must form the predicate to a patdown of a person for weapons.<footnotemark>5</footnotemark> <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 146</a></span>; <em>Terry </em>v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio"><em>Ohio, supra, </em>at 21-24, 27</a></span>. When the police entered the Aurora Tap Tavern on March 1, 1976, the lighting was sufficient for them to observe the customers. Upon seeing Ybarra, they neither recognized him as a person with a criminal history nor had any particular reason to believe that he might be inclined to assault them. Moreover, as Police Agen't Johnson later testified, Ybarra, whose hands were empty, gave no indication of possessing a weapon, made no gestures or other actions indicative of an intent to commit an assault, and acted generally in a manner that was not threatening. At the suppression hearing, the most Agent Johnson could point to was that Ybarra was wearing a %-length lumber jacket, clothing which the State admits could be expected on almost any tavern patron in Illinois in early March. In short, the State is unable to articulate any specific fact that would have justified a police officer at the scene in even suspecting that Ybarra was armed and dangerous.</p>
<p id="b239-5">The <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>case created an exception to the requirement of probable cause, an exception whose “narrow scope” this Court “has been careful to maintain.” <footnotemark>6</footnotemark> Under that doctrine a law enforcement officer, for his own protection and safety, may conduct a patdown to find weapons that he reasonably believes or suspects are then in the possession of the person he has accosted. See, <em>e. g., Adams </em>v. <em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Williams, supra</a></span> </em>(at night, in high-crime district, lone police officer approached person believed by officer to possess gun and narcotics). Nothing in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>can be understood to allow a generalized <page-number citation-index="1" label="94">*94</page-number>“cursory search for weapons” or, indeed, any search whatever for anything but weapons. The “narrow scope” of the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>exception does not permit a frisk for weapons on less than reasonable belief or suspicion directed at the person to be frisked, even though that person happens to be on premises where an authorized narcotics search is taking place.</p>
<p id="b240-5">What has been said largely disposes of the State’s second and alternative argument in this case. Emphasizing the important governmental interest “in effectively controlling traffic in dangerous, hard drugs” and the ease with which the evidence of narcotics possession may be concealed or moved around from person to person, the State contends that .the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>“reasonable belief or suspicion” standard should be made applicable to aid the evidence-gathering function of the search warrant. More precisely, we are asked to construe the Fourth and Fourteenth Amendments to permit evidence searches of persons who, at the commencement of the search, are on “compact” premises subject to a search warrant, at least where the police have a “reasonable belief” that such persons “are connected with” drug trafficking and “may be concealing or carrying away the contraband.”</p>
<p id="b240-6">Over 30 years ago, the Court rejected a similar argument in <em>United States </em>v. <em>Di Re, </em><span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#583" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 583-587</a></span>. In that case, a federal investigator had been told by an informant that a transaction in counterfeit gasoline ration coupons was going to occur at a particular place. The investigator went to that location at the appointed time and saw the car of one of the suspected parties to the illegal transaction. The investigator went over to the car and observed a man in the driver’s seat, another man (Di Re) in the passenger’s seat, and the informant in the back. The informant told the investigator that the person in the driver’s seat had given him counterfeit coupons. Thereupon, all three men were arrested and searched. Among the arguments unsuccessfully advanced by the Government to support the constitutionality of the search of Di Re was the contention that the investigator could <page-number citation-index="1" label="95">*95</page-number>lawfully have searched the car, since he had reasonable cause to believe that it contained contraband, and correspondingly could have searched any occupant of the car because the contraband sought was of the sort “which could easily be concealed on the person.” <footnotemark><em>7</em></footnotemark><em> </em>Not deciding whether or not under the Fourth Amendment the car could have been searched, the Court held that it was “not convinced that a person, by mere presence in a suspected car, loses immunities from search of his person to which he would otherwise be entitled.” <footnotemark>8</footnotemark></p>
<p id="AQ">The <em>Di Re </em>case does not, of course, completely control the case at hand. There the Government investigator was proceeding without a search warrant, and here the police possessed a warrant authorizing the search of the Aurora Tap Tavern. Moreover, in <em>Di Re </em>the Government conceded that its officers could not search all the persons in a house being searched pursuant to a search warrant.’<footnotemark>9</footnotemark> The State makes no such concession in this case. Yet the governing principle in both cases is basically the same, and we follow that principle today. The “long-prevailing” constitutional standard of probable cause embodies “ 'the best compromise that has been found for accommodating [the] often opposing interests’ in 'safeguard [ing] citizens from rash and unreasonable inter<page-number citation-index="1" label="96">*96</page-number>ferences with privacy' and in ‘seek[ing] to give fair leeway for enforcing the law in the community's protection.' ”<footnotemark>10</footnotemark></p>
<p id="b242-5">For these reasons, we conclude that the searches of Ybarra and the seizure of what was in his pocket contravened the Fourth and Fourteenth Amendments.<footnotemark>11</footnotemark> Accordingly, the judgment is reversed, and the case is remanded to the Appellate Court of Illinois, Second District, for further proceedings not inconsistent with this opinion.</p>
<p id="b242-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b233-12"> The statute in question is Ill. Rev. Stat., ch. 38, §108-9 (1975), which provides in full:</p>
<blockquote id="b233-13">“In the execution of the warrant the person executing the same may reasonably detain to search any person in the place at the time:</blockquote>
<blockquote id="b233-14">“(a) To protect himself from attack, or</blockquote>
<blockquote id="b233-15">“ (b) To prevent the disposal or concealment of any instruments, articles or things particularly described in the warrant.”</blockquote>
</footnote>
<footnote label="2">
<p id="b236-8"> The warrant issued on March 1, 1976, did not itself authorize the search of Ybarra or of any other patron found on the premises of the Aurora Tap Tavern. It directed the police to search “the following person or place: . . . the Aurora Tap Tavern. . . . Also the person of ‘Greg’. . . <em>.” </em>Had the issuing judge intended that the warrant would or could authorize a search of every person found within the tavern, he would hardly have specifically authorized the search of “Greg” alone. “Greg” was an 'employee of the tavern, and the complaint upon which the search warrant was issued gave every indication that he would be present at the tavern on March 1.</p>
</footnote>
<footnote label="3">
<p id="b237-7"> Ybarra concedes that the warrant issued on March 1, 1976, was supported by probable cause insofar as it purported to authorize a search of the premises of the Aurora Tap Tavern and a search of the person of “Greg,” the bartender.</p>
</footnote>
<footnote label="4">
<p id="b238-7"> The Fourth Amendment directs that “no Warrants shall issue, but upon probable cause . . . and particularly describing the place to be searched, and the persons or things to be seized.” Thus, “open-ended” or “general” warrants are constitutionally prohibited. See <em>Lo-Ji Sales, Inc. </em>v. <em>New York, </em><span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York">442 U. S. 319</a></span>; <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#311" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 311</a></span>; <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#7" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 7-8</a></span>; <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#480" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 480-482</a></span>. It follows that a warrant to search a place cannot normally be construed to authorize a search of each individual in that place. The warrant for the Aurora Tap Tavern provided no basis for departing from this general rule. Consequently, we need not consider situations where the warrant itself authorizes the search of unnamed persons in a place and is supported by probable cause to believe that persons who will be in the place at the time of the search will be in possession of illegal drugs.</p>
</footnote>
<footnote label="5">
<p id="b239-6"> Since we conclude that the initial patdown of Ybarra was not justified under the Fourth and Fourteenth Amendments, we need not decide whether or not the presence on Ybarra’s person of “a cigarette pack with objects in it” yielded probable cause to believe that Ybarra was carrying any illegal substance.</p>
</footnote>
<footnote label="6">
<p id="b239-11"> <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#210" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 210</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b241-5"><em> </em><span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#586" aria-description="Citation for case: United States v. Di Re">332 U. S., at 586</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b241-6"> <em>Id., </em>at 587.</p>
</footnote>
<footnote label="9">
<p id="b241-7"> “The Government says it would not contend that, armed with a search warrant for a residence only, it could search all persons found in it. But an occupant of a house could be used to conceal this contraband on his person quite as readily as can an occupant of a car. Necessity, an argument advanced in support of this search, would seem as strong a reason for searching guests of a house for which a search warrant had issued as for search of guests in a car for which none had been issued. By a parity of reasoning with that on which the Government disclaims the right to search occupants of a house, we suppose the Government would not contend that if it had a valid search warrant for the car only it could search the occupants as an incident to its execution. How then could we say that the right to search a car without a warrant confers greater latitude to search occupants than a search by warrant would permit?” <em>Ibid.</em></p>
</footnote>
<footnote label="10">
<p id="b242-9"> <em>Dunaway </em>v. <em>New York, </em>442 U. S., at 208, quoting <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span>.</p>
<p id="b242-10">The circumstances of this case do not remotely approach those in which the Court has said that a search may be made on less than probable cause. In addition to <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span>, see, <em>e. g., Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648</a></span>; <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307</a></span>; <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation no-link">428 U. S. 643</span>; <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span>; <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span>; <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span>; <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span>.</p>
</footnote>
<footnote label="11">
<p id="b242-11"> Our decision last Term in <em>Michigan </em>v. <em>DeFillippo, </em><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">443 U. S. 31</a></span>, does not point in a different direction. There we held that the Fourth and Fourteenth Amendments had not been violated by an arrest based on a police officer's probable cause to believe that the suspect had committed or was committing a substantive criminal offense, even though the statute creating the offense was subsequently declared unconstitutional. Here, the police officers acted on the strength of Ill. Rev. Stat., ch. 38, § 108-9 (1975), but that statute does not define the elements of a substantive criminal offense under state law. The statute purports instead to authorize the police in some circumstances to make searches and seizures without probable cause and without search warrants. This state lawy therefore, falls within the category of statutes purporting to authorize searches without probable cause, which the Court has not hesitated to hold invalid as authority for unconstitutional searches. See, e. <em>g., Torres </em>v. <em>Puerto Rico, </em><span class="citation" data-id="9795098"><a href="/opinion/2620876/torres-v-puerto-rico/" aria-description="Citation for case: Torres v. Puerto Rico">442 U. S. 465</a></span>; <em>Almeida-Sanchez </em>v. <em>United States, </em><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span>; <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span>; <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span>.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Foster v. California.md  (`case`, 5 assertions)

### content_page

```
---
title: "Foster v. California"
type: case
citation: "394 U.S. 440 (1969)"
parallel_cite: "89 S. Ct. 1127; 22 L. Ed. 2d 402"
neutral_cite: 1969 U.S. LEXIS 2050
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1969
date_decided: 1969-04-01
docket: 47
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1969-04-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Foster v. California
  varies_by_point: false
  scope_note: "Good law; the rare case in which the Court found a pretrial identification so suggestive as to violate due process (noted as such in Perry v. New Hampshire)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107890/foster-v-california/"
  cluster_id: 107890
  opinion_id: 107890
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Progeny"
related: ["[[Stovall v. Denno]]", "[[Neil v. Biggers]]", "[[Manson v. Brathwaite]]", "[[Perry v. New Hampshire]]"]
aliases: []
tags: ["case", "due-process", "eyewitness-identification", "lineup", "suggestive"]
holding: "An identification procedure may be so unnecessarily suggestive that it denies due process; here a lineup that made the suspect stand out, followed by a one-on-one showup and a repeat lineup in which he was the only carryover, made identification all but inevitable and violated due process — the rare such reversal."
lake:
  record_id: Foster v. California
  status: verified
  projected_at: 2026-07-06
---

# Foster v. California

*394 U.S. 440 (1969)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
The only eyewitness to a Western Union armed robbery, manager Joseph David, viewed a police lineup of three men in which Foster — close to six feet tall — stood between two men five-foot-five or -six, and Foster wore a leather jacket like the robber's. David was unsure. Police then staged a one-to-one confrontation between David and Foster; David was still uncertain. About a week later police arranged a second lineup of five men in which Foster was the only person carried over from the first lineup. David was then "convinced."

## Issue
Whether a pretrial identification procedure can be so unnecessarily suggestive and conducive to mistaken identification that admitting the resulting identification denies the defendant due process of law.

## Rule
Yes. Even apart from the right-to-counsel rule of *[[United States v. Wade|Wade]]*/*[[Gilbert v. California|Gilbert]]* (inapplicable to pre-1967 lineups), "the conduct of identification procedures may be 'so unnecessarily suggestive and conducive to irreparable mistaken identification' as to be a denial of due process of law." — 394 U.S. at 442. ^pin-442

Applying that standard: "The suggestive elements in this identification procedure made it all but inevitable that David would identify petitioner whether or not he was in fact 'the man.' In effect, the police repeatedly said to the witness, 'This is the man.' ... This procedure so undermined the reliability of the eyewitness identification as to violate due process." — *Id.* at 443. ^pin-443

## Application
The cumulative suggestiveness was extreme: Foster stood out by height and clothing in the first lineup; when that failed to produce a positive identification, police escalated to a one-on-one showup; and when David was still tentative, a second lineup placed Foster as the only repeat participant. Each step pointed the witness to Foster, so his eventual "conviction" that Foster was the robber was the product of the procedure rather than independent recollection — a denial of due process.

## Conclusion
The identification procedure violated due process; the judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]]. *Foster* is the rare instance in which the Supreme Court found a suggestive pretrial identification unconstitutional.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The "unnecessarily suggestive" inquiry was later refined into a reliability test by [[Neil v. Biggers]] and [[Manson v. Brathwaite]], and the due-process screen was confined to police-arranged suggestiveness in [[Perry v. New Hampshire]]. *Foster* remains the paradigm of a procedure suggestive enough to require exclusion.

## Appears on
- [[Eyewitness Identification]] — *Key — Progeny*

## Sources
- *Foster v. California*, 394 U.S. 440 (1969) — https://www.courtlistener.com/opinion/107890/foster-v-california/ — pinpoints: 442, 443.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0788f86d48e9d502", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "394 U.S. 440 (1969)", "court": "U.S. Supreme Court", "neutral_cite": "1969 U.S. LEXIS 2050", "official_citation_present": true, "parallel_cite": "89 S. Ct. 1127; 22 L. Ed. 2d 402", "title": "Foster v. California", "year": "1969"}}
{"assertion_id": "e515776bbb54213b", "dimension": "support", "kind": "home_role", "locator": {"home": "Eyewitness Identification"}, "payload": {"home": "Eyewitness Identification", "role": "Key — Progeny", "title": "Foster v. California"}}
{"assertion_id": "ed20f3403829ae30", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An identification procedure may be so unnecessarily suggestive that it denies due process; here a lineup that made the suspect stand out, followed by a one-on-one showup and a repeat lineup in which he was the only carryover, made identification all but inevitable and violated due process — the rare such reversal.", "title": "Foster v. California"}}
{"assertion_id": "0418be620d433249", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Foster v. California"}}
{"assertion_id": "18dac7cc1fc709ab", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1969-04-01", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Foster v. California", "field_i_validity": "good_law", "scope_note": "Good law; the rare case in which the Court found a pretrial identification so suggestive as to violate due process (noted as such in Perry v. New Hampshire).", "title": "Foster v. California", "varies_by_point": "false"}}
```

### lake record — Foster v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Foster v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Foster v. California",
    "case_name_short": "Foster",
    "case_name_full": "Foster v. California",
    "input_case_name": "Foster v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1969-04-01",
    "year": 1969,
    "docket": "47",
    "cluster_id": 107890,
    "lead_opinion_id": 107890,
    "sibling_ids": [
      107890,
      9423977,
      9423978
    ],
    "absolute_url": "/opinion/107890/foster-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "394 U.S. 440",
      "volume": "394",
      "reporter": "U.S.",
      "page": "440",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "89 S. Ct. 1127",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "1127",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 402",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "402",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1969 U.S. LEXIS 2050",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "2050",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "394 U.S. 440",
        "volume": "394",
        "reporter": "U.S.",
        "page": "440",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 S. Ct. 1127",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "1127",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 402",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "402",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1969 U.S. LEXIS 2050",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "2050",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "394 U.S. 440",
    "official_selection": {
      "court_class": "scotus",
      "selected": "394 U.S. 440",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-442",
      "page": null,
      "quote": "## Issue Whether a pretrial identification procedure can be so unnecessarily suggestive and conducive to mistaken identification that admitting the resulting identification denies the defendant due process of law. ## Rule Yes. Even apart from the right-to-counsel rule of *Wade*/*Gilbert* (inapplicable to pre-1967 lineups),",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-443",
      "page": null,
      "quote": "The suggestive elements in this identification procedure made it all but inevitable that David would identify petitioner whether or not he was in fact 'the man.' In effect, the police repeatedly said to the witness, 'This is the man.' ... This procedure so undermined the reliability of the eyewitness identification as to violate due process.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1969-04-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Foster v. California",
    "varies_by_point": false,
    "scope_note": "Good law; the rare case in which the Court found a pretrial identification so suggestive as to violate due process (noted as such in Perry v. New Hampshire).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Dickson",
          "cluster_id": 4244499,
          "cite": [
            "141 A.3d 810",
            "322 Conn. 410",
            "2016 Conn. LEXIS 236"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Newman",
          "cluster_id": 2791286,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Carl Leonard Lively v. State",
          "cluster_id": 3100720,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Guidry",
          "cluster_id": 37891,
          "cite": [
            "406 F.3d 314",
            "2005 U.S. App. LEXIS 5607",
            "2005 WL 768764"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "James David Carter v. Ricky Bell, Warden Paul Summers, Attorney General",
          "cluster_id": 769405,
          "cite": [
            "218 F.3d 581",
            "2000 U.S. App. LEXIS 15651",
            "2000 F. App'x 0221P"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hull v. State",
          "cluster_id": 1142679,
          "cite": [
            "607 So. 2d 369",
            "1992 WL 201066"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Glover v. State",
          "cluster_id": 1639517,
          "cite": [
            "787 S.W.2d 544",
            "1990 Tex. App. LEXIS 1050",
            "1990 WL 59411"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Neil v. Biggers",
          "cluster_id": 108639,
          "cite": [
            "34 L. Ed. 2d 401",
            "93 S. Ct. 375",
            "409 U.S. 188",
            "1972 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baker v. McCollan",
          "cluster_id": 110132,
          "cite": [
            "61 L. Ed. 2d 433",
            "99 S. Ct. 2689",
            "443 U.S. 137",
            "1979 U.S. LEXIS 141"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manson v. Brathwaite",
          "cluster_id": 109693,
          "cite": [
            "53 L. Ed. 2d 140",
            "97 S. Ct. 2243",
            "432 U.S. 98",
            "1977 U.S. LEXIS 116"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Young",
          "cluster_id": 111353,
          "cite": [
            "84 L. Ed. 2d 1",
            "105 S. Ct. 1038",
            "470 U.S. 1",
            "1985 U.S. LEXIS 49",
            "53 U.S.L.W. 4159"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barefoot v. Estelle",
          "cluster_id": 111017,
          "cite": [
            "77 L. Ed. 2d 1090",
            "103 S. Ct. 3383",
            "463 U.S. 880",
            "1983 U.S. LEXIS 110",
            "51 U.S.L.W. 5189",
            "13 Fed. R. Serv. 449"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
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
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kirby v. Illinois",
          "cluster_id": 108554,
          "cite": [
            "32 L. Ed. 2d 411",
            "92 S. Ct. 1877",
            "406 U.S. 682",
            "1972 U.S. LEXIS 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hasting",
          "cluster_id": 110933,
          "cite": [
            "76 L. Ed. 2d 96",
            "103 S. Ct. 1974",
            "461 U.S. 499",
            "1983 U.S. LEXIS 31",
            "51 U.S.L.W. 4572"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coleman v. Alabama",
          "cluster_id": 108182,
          "cite": [
            "26 L. Ed. 2d 387",
            "90 S. Ct. 1999",
            "399 U.S. 1",
            "1970 U.S. LEXIS 17"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gimmy v. People",
          "cluster_id": 1231296,
          "cite": [
            "645 P.2d 262",
            "1982 Colo. LEXIS 568"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gregory v. City of Louisville",
          "cluster_id": 2973641,
          "cite": [
            "444 F.3d 725",
            "2006 WL 909935"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Manuel Concepcion, Roberto Aponte, and Nelson Frias",
          "cluster_id": 597808,
          "cite": [
            "983 F.2d 369"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
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
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gray v. State",
          "cluster_id": 1666205,
          "cite": [
            "728 So. 2d 36",
            "1998 WL 452320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Frank Howard v. Barbara Bouchard, Warden",
          "cluster_id": 789998,
          "cite": [
            "405 F.3d 459",
            "2005 U.S. App. LEXIS 7271",
            "2005 WL 976980"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mattas",
          "cluster_id": 1231857,
          "cite": [
            "645 P.2d 254"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ex Parte Adams",
          "cluster_id": 1784512,
          "cite": [
            "768 S.W.2d 281",
            "1989 Tex. Crim. App. LEXIS 39",
            "1989 WL 16461"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Anderson",
          "cluster_id": 2222943,
          "cite": [
            "205 N.W.2d 461",
            "389 Mich. 155",
            "1973 Mich. LEXIS 99"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Diaz",
          "cluster_id": 75261,
          "cite": [
            "248 F.3d 1065",
            "2001 WL 392392"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alex Wong, Roger Kwok, Chen I. Chung, Tung Tran, Danny Ngo, Brian Chan, Joseph Wang, Chiang T. Cheng, and Steven Ng",
          "cluster_id": 683141,
          "cite": [
            "40 F.3d 1347",
            "1994 U.S. App. LEXIS 31286"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hernandez-Cuevas v. Taylor",
          "cluster_id": 1034188,
          "cite": [
            "723 F.3d 91",
            "2013 U.S. App. LEXIS 14469",
            "2013 WL 3742484"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gregory v. City of Louisville",
          "cluster_id": 793983,
          "cite": [
            "444 F.3d 725"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107890 OR 9423977 OR 9423978) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NjIzNzc2MDAwMDAmcz01MTI4ODgzJnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107890+OR+9423977+OR+9423978%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      },
      "lane2_top_cited": {
        "query": "cites:(107890 OR 9423977 OR 9423978)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTQmcz0xODExMzkyJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107890+OR+9423977+OR+9423978%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107890 OR 9423977 OR 9423978)",
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
    "complete_query": "cites:(107890 OR 9423977 OR 9423978)",
    "indexed_citing_opinions": 722,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107890,
        "count": 667,
        "count_source": "search"
      },
      {
        "opinion_id": 9423977,
        "count": 71,
        "count_source": "search"
      },
      {
        "opinion_id": 9423978,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1048,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/foster-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcxMzcwMyZzPTQ4NTY3MjgmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28107890+OR+9423977+OR+9423978%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107890,
        "cited_id": 102885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 107638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 107685,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 107821,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 1184080,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 1341981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 1376991,
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
    "date_created": "2026-07-05T04:37:49Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T04:38:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T04:38:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T04:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T04:38:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Foster v. California

```
<div>
<center><b><span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">394 U.S. 440</a></span> (1969)</b></center>
<center><h1>FOSTER<br>
v.<br>
CALIFORNIA.</h1></center>
<center>No. 47.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 19, 1968.</center>
<center>Decided April 1, 1969.</center>
CERTIORARI TO THE COURT OF APPEAL OF CALIFORNIA, FIFTH APPELLATE DISTRICT.
<p><i>Kenneth L. Maddy,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./391/902/">391 U. S. 902</a></span>, argued the cause and filed briefs for petitioner.</p>
<p><i>Doris H. Maier,</i> Assistant Attorney General of California, argued the cause for respondent. With her on the brief were <i>Thomas C. Lynch,</i> Attorney General, and <i>Charles P. Just,</i> Deputy Attorney General.</p>
<p><span class="star-pagination">*441</span> MR. JUSTICE FORTAS delivered the opinion of the Court.</p>
<p>Petitioner was charged by information with the armed robbery of a Western Union office in violation of California Penal Code § 211a. The day after the robbery one of the robbers, Clay, surrendered to the police and implicated Foster and Grice. Allegedly, Foster and Clay had entered the office while Grice waited in a car. Foster and Grice were tried together. Grice was acquitted. Foster was convicted. The California District Court of Appeal affirmed the conviction; the State Supreme Court denied review. We granted certiorari, limited to the question whether the conduct of the police lineup resulted in a violation of petitioner's constitutional rights. <span class="citation multiple-matches"><a href="/c/U.%20S./390/994/">390 U. S. 994</a></span> (1968).</p>
<p>Except for the robbers themselves, the only witness to the crime was Joseph David, the late-night manager of the Western Union office. After Foster had been arrested, David was called to the police station to view a lineup. There were three men in the lineup. One was petitioner. He is a tall manclose to six feet in height. The other two men were shortfive feet, five or six inches. Petitioner wore a leather jacket which David said was similar to the one he had seen underneath the coveralls worn by the robber. After seeing this lineup, David could not positively identify petitioner as the robber. He "thought" he was the man, but he was not sure. David then asked to speak to petitioner, and petitioner was brought into an office and sat across from David at a table. Except for prosecuting officials there was no one else in the room. Even after this one-to-one confrontation David still was uncertain whether petitioner was one of the robbers: "truthfully I was not sure," he testified at trial. A week or 10 days later, the police arranged for David to view a second lineup. There were five men in that lineup. Petitioner was the only person in the second lineup who had <span class="star-pagination">*442</span> appeared in the first lineup. This time David was "convinced" petitioner was the man.</p>
<p>At trial, David testified to his identification of petitioner in the lineups, as summarized above. He also repeated his identification of petitioner in the courtroom. The only other evidence against petitioner which concerned the particular robbery with which he was charged was the testimony of the alleged accomplice Clay.<sup>[1]</sup></p>
<p>In <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), and <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967), this Court held that because of the possibility of unfairness to the accused in the way a lineup is conducted, a lineup is a "critical stage" in the prosecution, at which the accused must be given the opportunity to be represented by counsel. That holding does not, however, apply to petitioner's case, for the lineups in which he appeared occurred before June 12, 1967. <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967). But in declaring the rule of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> to be applicable only to lineups conducted after those cases were decided, we recognized that, judged by the "totality of the circumstances," the conduct of identification procedures may be "so unnecessarily suggestive and conducive to irreparable mistaken identification" as to be a denial of due process of law. <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#302" aria-description="Citation for case: Gilbert v. California"><i>Id.,</i> at 302</a></span>. See <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#383" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 383</a></span> (1968); cf. P. Wall, Eye-Witness Identification in Criminal Cases; J. Frank &amp; B. Frank, Not Guilty; 3 J. Wigmore, Evidence § 786<i>a</i> (3d ed. 1940); 4, <i>id.,</i> § 1130.</p>
<p>Judged by that standard, this case presents a compelling example of unfair lineup procedures.<sup>[2]</sup> In the <span class="star-pagination">*443</span> first lineup arranged by the police, petitioner stood out from the other two men by the contrast of his height and by the fact that he was wearing a leather jacket similar to that worn by the robber. See <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#233" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 233</a></span>. When this did not lead to positive identification, the police permitted a one-to-one confrontation between petitioner and the witness. This Court pointed out in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> that "[t]he practice of showing suspects singly to persons for the purpose of identification, and not as part of a lineup, has been widely condemned." 388 U. S., at 302. Even after this the witness' identification of petitioner was tentative. So some days later another lineup was arranged. Petitioner was the only person in this lineup who had also participated in the first lineup. See Wall, <i>supra,</i> at 64. This finally produced a definite identification.</p>
<p>The suggestive elements in this identification procedure made it all but inevitable that David would identify petitioner whether or not he was in fact "the man." In effect, the police repeatedly said to the witness, "<i>This</i> is the man." See <i>Biggers</i> v. <i>Tennessee,</i> <span class="citation" data-id="9423641"><a href="/opinion/107638/biggers-v-tennessee/#407" aria-description="Citation for case: Biggers v. Tennessee">390 U. S. 404, 407</a></span> (dissenting opinion). This procedure so undermined the reliability of the eyewitness identification as to violate due process.</p>
<p>In a decision handed down since the Supreme Court of California declined to consider petitioner's case, it reversed a conviction because of the unfair makeup of a lineup. In that case, the California court said: "[W]e do no more than recognize . . . that unfairly constituted lineups have in the past too often brought about the conviction of the innocent." <i>People</i> v. <i>Caruso,</i> <span class="citation" data-id="9551395"><a href="/opinion/1184080/people-v-caruso/#188" aria-description="Citation for case: People v. Caruso">68 Cal. 2d 183, 188</a></span>, <span class="citation" data-id="9551395"><a href="/opinion/1184080/people-v-caruso/#340" aria-description="Citation for case: People v. Caruso">436 P. 2d 336, 340</a></span> (1968). In the present case the pretrial confrontations clearly were so arranged as to make the resulting identifications virtually inevitable.</p>
<p><span class="star-pagination">*444</span> The respondent invites us to hold that any error was harmless under <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967). We decline to rule upon this question in the first instance. Accordingly, the judgment is reversed and the case remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>Reversed and remanded.</i></p>
<p>MR. JUSTICE WHITE, with whom MR. JUSTICE HARLAN and MR. JUSTICE STEWART concur, being unwilling in this case to disagree with the jury on the weight of the evidence, would affirm the judgment.</p>
<p>MR. JUSTICE BLACK, dissenting.</p>
<p>The Court here directs the California courts to set aside petitioner Foster's conviction for armed robbery of the Western Union Telegraph Co. at Fresno, California. The night manager of the telegraph company testified before the court and jury that two men came into the office just after midnight, January 25, 1966, wrote a note telling him it was a holdup, put it under his face, and demanded money, flashed guns, took $531 and fled. The night manager identified Foster in the courtroom as one of the men, and he also related his identification of Foster in a lineup a week or so after the crime. The manager's evidence, which no witness disputed, was corroborated by the testimony of a man named Clay, who was Foster's accomplice in the robbery and who testified for the State. The testimony of these two eyewitnesses was also corroborated by proof that Foster and another person had committed a prior armed robbery of a Western Union office in another city six years before, when they appeared at the company's office, presented a note to an employee announcing their holdup, flashed a gun, and fled with company money. In this case Foster's attorney admitted conviction <span class="star-pagination">*445</span> for the prior Western Union armed robbery.<sup>[1]</sup> The circumstances of the two robberies appear to have been practically indistinguishable. Such evidence that a particular person committed a prior crime has been almost universally accepted as relevant and admissible to prove that the same person was responsible for a later crime of the same nature.<sup>[2]</sup> A narration of these facts, falling from the lips of eyewitnesses, and not denied by other eyewitnesses, would be enough, I am convinced, to persuade nearly all lawyers and judges, unhesitatingly to say, "There was clearly enough evidence of guilt here for a jury to convict the defendant since, according to practice, and indeed constitutional command, the weight of evidence is for a jury, and not for judges." Nevertheless the Court in this case looks behind the evidence given by witnesses on the stand and decides that because of the circumstances under which one witness first identified the defendant as the criminal, the United States Constitution requires that the conviction be reversed. The Court, however, fails to spell out exactly what should happen to this defendant if there must be a retrial, and thus avoids the apparently distasteful task of specifying whether (1) at the new trial the jury would again be permitted to hear the eyewitness' testimony and the in-court identification, so long as he does not refer to the previous lineups, or (2) the eyewitness' "tainted" identification testimony must be entirely excluded, thus compelling Foster's acquittal. Objection to this ambiguity is the first of my reasons for dissent.</p>
<p></p>
<h2>
<span class="star-pagination">*446</span> I.</h2>
<p>The Court declares the judgment of conviction is reversed and the case remanded for further proceedings not inconsistent with this opinion. I am compelled to say that if I were the trial judge in this case I would not know how to proceed or how to decide whether the "error" in this case was harmless. Of course, when a confession is held to have been compelled, that confession must not be admitted to convict the defendant at all. But the situation in this case is not that simple. For the Court has in effect decided here that the officers of the law have so "arranged" lineups that the eyewitness to the robbery has been led to make an "irreparable mistaken identification." In other words, no one now or hereafter can believe his identification of Foster as the robber. Since he and the accomplice are the only eyewitnesses, and since, in order to convict, California law requires evidence of an accomplice to be corroborated, the Court's direction means, I suppose, that the trial judge here should dismiss the case.<sup>[3]</sup> The Court's dilemma, which leads to its ambiguous judgment as to the further disposition of this case, points, I think, to the irreparable harm done to the cause of justice by the Court's holding in this case.</p>
<p></p>
<h2>II.</h2>
<p>Far more fundamental, however, is my objection to the Court's basic holding that evidence can be ruled constitutionally inadmissible whenever it results from identification <span class="star-pagination">*447</span> procedures that the Court considers to be " `unnecessarily suggestive and conducive to irreparable mistaken identification.' "<sup>[4]</sup> One of the proudest achievements of this country's Founders was that they had eternally guaranteed a trial by jury in criminal cases, at least until the Constitution they wrote had been amended in the manner they prescribed. Only last year in <i>Duncan</i> v. <i>Louisiana,</i> <span class="citation" data-id="9423691"><a href="/opinion/107685/duncan-v-louisiana/" aria-description="Citation for case: Duncan v. Louisiana">391 U. S. 145</a></span> (1968), this Court emphatically decided, over strong dissents, that this constitutional right to trial by jury in criminal cases is applicable to the States. Of course it is an incontestable fact in our judicial history that the jury is the sole tribunal to weigh and determine facts. That means that the jury must, if we keep faith with the Constitution, be allowed to hear eyewitnesses and decide for itself whether it can recognize the truth and whether they are telling the truth. It means that the jury must be allowed to decide for itself whether the darkness of the night, the weakness of a witness' eyesight, or any other factor impaired the witness' ability to make an accurate identification. To take that power away from the jury is to rob it of the responsibility to perform the precise functions the Founders most wanted it to perform. And certainly a Constitution written to preserve this indispensable, unerodible core of our system for trying criminal cases would not have included, hidden among its provisions, a slumbering sleeper granting the judges license to destroy trial by jury in whole or in part.</p>
<p>This brings me to the constitutional theory relied upon by the Court to justify its invading the constitutional right of jury trial. The Court here holds that:</p>
<blockquote>"[J]udged by the `totality of the circumstances,' the conduct of identification procedures may be `so <span class="star-pagination">*448</span> unnecessarily suggestive and conducive to irreparable mistaken identification' as to be a denial of due process of law. . . .</blockquote>
<blockquote>"Judged by that standard, this case presents a compelling example of unfair lineup procedures." <i>Ante,</i> at 442.</blockquote>
<p>I do not deny that the "totality of circumstances" can be considered to determine whether some specific constitutional prohibitions have been violated, such, for example, as the Fifth Amendment's command against compelling a witness to incriminate himself. Whether evidence has been compelled is, of course, a triable issue of fact. And the constitutional command not to compel a person to be a witness against himself, like other issues of fact, must be determined by a resolution of all facts and the "totality" of them offered in evidence. Consequently were the Court's legal formula posed for application in a coerced testimony case, I could agree to it. But it is not. Instead the Court looks to the "totality of circumstances" to show "unfair lineup procedures." This means "unfair" according to the Court's view of what is unfair. The Constitution, however, does not anywhere prohibit conduct deemed unfair by the courts. As we recently said in <i>United States</i> v. <i>Augenblick,</i> <span class="citation" data-id="107821"><a href="/opinion/107821/united-states-v-augenblick/#352" aria-description="Citation for case: United States v. Augenblick">393 U. S. 348, 352</a></span> (1969): "Rules of evidence are designed in the interests of fair trials. But unfairness in result is no sure measure of unconstitutionality."</p>
<p>The Constitution sets up its own standards of unfairness in criminal trials in the Fourth, Fifth, and Sixth Amendments, among other provisions of the Constitution. Many of these provisions relate to evidence and its use in criminal cases. The Constitution provides that the accused shall have the right to compulsory process for obtaining witnesses in his favor. It ordains that evidence shall not be obtained by compulsion of the accused. It ordains that the accused shall have the right to confront <span class="star-pagination">*449</span> the witnesses against him. In these ways the Constitution itself dictates what evidence is to be excluded because it was improperly obtained or because it is not sufficiently reliable. But the Constitution does not give this Court any general authority to require exclusion of all evidence that this Court considers improperly obtained or that this Court considers insufficiently reliable. Hearsay evidence, for example, is in most instances rendered inadmissible by the Confrontation Clause, which reflects a judgment, made by the Framers of the Bill of Rights, that such evidence may be unreliable and cannot be put in proper perspective by cross-examination of the person repeating it in court. Nothing in this constitutional plan suggests that the Framers drew up the Bill of Rights merely in order to mention a few types of evidence "for illustration," while leaving this Court with full power to hold unconstitutional the use of any other evidence that the Justices of this Court might decide was not sufficiently reliable or was not sufficiently subject to exposure by cross-examination. On the contrary, as we have repeatedly held, the Constitution leaves to the States and to the people all these questions concerning the various advantages and disadvantages of admitting certain types of evidence. <i>Spencer</i> v. <i>Texas,</i> <span class="citation" data-id="9423324"><a href="/opinion/107342/spencer-v-texas/" aria-description="Citation for case: Spencer v. Texas">385 U. S. 554</a></span> (1967); <i>Michelson</i> v. <i>United States,</i> <span class="citation" data-id="9420246"><a href="/opinion/104607/michelson-v-united-states/" aria-description="Citation for case: Michelson v. United States">335 U. S. 469</a></span> (1948).</p>
<p>It has become fashionable to talk of the Court's power to hold governmental laws and practices unconstitutional whenever this Court believes them to be "unfair," contrary to basic standards of decency, implicit in ordered liberty, or offensive to "those canons of decency and fairness which express the notions of justice of English-speaking peoples . . . ."<sup>[5]</sup> All of these different general <span class="star-pagination">*450</span> and indefinable words or phrases are the fruit of the same, what I consider to be poisonous, tree, namely, the doctrine that this Court has power to make its own ideas of fairness, decency, and so forth, enforceable as though they were constitutional precepts. When I consider the incontrovertible fact that our Constitution was written to limit and define the powers of the Federal Government as distinguished from the powers of States, and to divide those powers granted the United States among the separate Executive, Legislative, and Judicial branches, I cannot accept the premise that our Constitution grants any powers except those specifically written into it, or absolutely necessary and proper to carry out the powers expressly granted.</p>
<p>I realize that some argue that there is little difference between the two constitutional views expressed below:</p>
<blockquote>One. No law should be held unconstitutional unless its invalidation can be firmly planted on a specific constitutional provision plus the Necessary and Proper Clause.</blockquote>
<blockquote>Two. All laws are unconstitutional that are unfair, shock the conscience of the Court, offend its sense of decency, or violate concepts implicit in ordered liberty.</blockquote>
<p>The first of these two constitutional standards plainly tells judges they have no power to hold laws unconstitutional unless such laws are believed to violate the written Constitution. The second constitutional standard, based on the words "due process," not only does not require judges to follow the Constitution as written, but actually encourages judges to hold laws unconstitutional on the basis of their own conceptions of fairness and justice. This formula imposes no "restraint" on judges beyond requiring them to follow their own best judgment as to what is wise, just, and best under the circumstances of a particular case. This case well illustrates the extremes <span class="star-pagination">*451</span> to which the formula can take men who are both wise and good. Although due process requires that courts summon witnesses so that juries can determine the guilt or innocence of defendants, the Court, because of its sense of fairness, decides that due process deprives juries of a chance to hear witnesses who the Court holds could not or might not tell the truth.</p>
<p>I began my opposition to this fallacious concept of "due process" even before I became a member of this Court<sup>[6]</sup> and expressed it formally soon after my service on the Court began.<sup>[7]</sup> And it was not long before I emphasized that quite a different belief about the meaning of the phrase "due process" had long existed in our judicial history in opposition to the "decency and fairness" doctrine. See <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#235" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227, 235-236, n. 8</a></span> (1940).</p>
<p>My experience on the Court has confirmed my early belief that the "decency and fairness" due process test cannot stand consistently with our written Constitution.</p>
<p></p>
<h2>III.</h2>
<p>I agree with the Court that we should not undertake to pass on the question of harmless error for the first time in this Court. Under the Court's holding, the case should be remanded to the state courts for decision of this question.</p>
<p>In recent years this Court has, in a series of cases, held that most of the Bill of Rights is now applicable against the States as well as against the Federal Government. This has brought about a tremendous increase in the number of state criminal cases involving federal questions, some of which depend on the particular facts and circumstances of the case. In Fifth Amendment <span class="star-pagination">*452</span> confession cases, for example, courts must under prevailing practice hear evidence to determine whether confessions were compelled. This Court has power in cases of that kind to review evidence before the trial courts. No one can now predict with accuracy how great a number of such cases are destined to come before us, but all know it will be many. Should we not make it an almost invariable practice to accept lower court findings of fact on such issues, our Supreme Court is likely to find itself pre-occupied with the business of a state court of criminal appeals, a condition not devoutly to be wished in the Court's interest or in the interest of the administration of justice in general. This problem is magnified many times over when account is taken of the harmless-error rules that many States have now adopted, since these rules also raise factual issues involving a federal question whenever the error itself is federal. See <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967). If trial errors are found some courts along the line must determine whether the error was harmless. That question has, because of this Court's judgment, now arisen in this case. I agree with the Court that we should not decide this question here. In the present posture of criminal law, there are simply too many federal questions in the state cases before us to defend a practice of our deciding in the first instance that there was no harmless error. There are many reasons for this other than the necessity of saving our time for the vastly more important issues we must decide. To say the least, the question whether an error in a particular case is harmless is an issue peculiarly for lower, not for the highest, appellate courts. Then, too, this issue can usually be tried more efficiently, and just as fairly, by the local court that tried the case or by the local appellate court that heard the first appeal. This Court was not established to try such minor issues of fact for the first time. Of course, I do not mean to suggest that <span class="star-pagination">*453</span> there should be an ironclad rule always barring the Court from deciding an issue in cases if it plainly and manifestly appears that it would be egregiously unjust and undoubtedly wrong to leave an issue undecided. But I do not think this even distantly approaches being such a case. Even though I steadfastly believe the Court's basic holding is error, I do agree that we should not establish a precedent of passing on harmless error for the first time in this Court before the courts below have had an opportunity to consider the question.</p>
<p>For the above reasons I dissent from the reversal and remand of this case.</p>
<h2>NOTES</h2>
<p>[1]  California law requires that an accomplice's testimony be corroborated. California Penal Code § 1111. There was also evidence that Foster had been convicted for a similar robbery committed six years before.</p>
<p>[2]  The reliability of properly admitted eyewitness identification, like the credibility of the other parts of the prosecution's case is a matter for the jury. But it is the teaching of <i>Wade, Gilbert,</i> and <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall, supra,</a></span></i> that in some cases the procedures leading to an eyewitness identification may be so defective as to make the identification constitutionally inadmissible as a matter of law.</p>
<p>[1]  Counsel also admitted a prior felony conviction of assault with intent to commit rape, a circumstance relevant in California in connection with punishment.</p>
<p>[2]  See <i>Spencer</i> v. <i>Texas,</i> <span class="citation" data-id="9423324"><a href="/opinion/107342/spencer-v-texas/" aria-description="Citation for case: Spencer v. Texas">385 U. S. 554</a></span>, 560-561 and n. 7 (1967); <i>State</i> v. <i>Chance,</i> <span class="citation" data-id="1168782"><a href="/opinion/1168782/state-v-chance/" aria-description="Citation for case: State v. Chance">92 Ariz. 351</a></span>, <span class="citation" data-id="1168782"><a href="/opinion/1168782/state-v-chance/" aria-description="Citation for case: State v. Chance">377 P. 2d 197</a></span> (1962); <i>Nester</i> v. <i>State,</i> <span class="citation" data-id="1376991"><a href="/opinion/1376991/nester-v-state/" aria-description="Citation for case: Nester v. State">75 Nev. 41</a></span>, <span class="citation" data-id="1376991"><a href="/opinion/1376991/nester-v-state/" aria-description="Citation for case: Nester v. State">334 P. 2d 524</a></span> (1959); <i>Mosley</i> v. <i>State,</i> <span class="citation" data-id="1341981"><a href="/opinion/1341981/mosley-v-state/" aria-description="Citation for case: Mosley v. State">211 Ga. 611</a></span>, <span class="citation" data-id="1341981"><a href="/opinion/1341981/mosley-v-state/" aria-description="Citation for case: Mosley v. State">87 S. E. 2d 314</a></span> (1955); 2 J. Wigmore, Evidence § 416 (3d ed. 1940 and 1964 Supp.).</p>
<p>[3]  The Court apparently means that the only other evidence against Foster in this casehis prior conviction for involvement in a crime of a similar typeis constitutionally admissible. See <i>Spencer</i> v. <i><span class="citation" data-id="9423324"><a href="/opinion/107342/spencer-v-texas/" aria-description="Citation for case: Spencer v. Texas">Texas, supra</a></span></i><i>.</i> But it may be doubtful whether this past conviction, although highly relevant to the question of guilt, could constitute corroboration of the accomplice's testimony, within the meaning of the California requirement.</p>
<p>[4]  <i>Ante,</i> at 442, quoting from <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#302" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293, 302</a></span> (1967).</p>
<p>[5]  <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#417" aria-description="Citation for case: Malinski v. New York">324 U. S. 401, 417</a></span> (opinion of Frankfurter, J.) (1945); see also <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952); <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">347 U. S. 128</a></span> (1954).</p>
<p>[6]  See, <i>e. g.,</i> 81 Cong. Rec. App., pt. 9, pp. 638-639; <i>id.,</i> at 307.</p>
<p>[7]  See, <i>e. g., </i><i>McCart</i> v. <i>Indianapolis Water Co.,</i> <span class="citation" data-id="9418947"><a href="/opinion/102885/mccart-v-indianapolis-water-co/#423" aria-description="Citation for case: McCart v. Indianapolis Water Co.">302 U. S. 419, 423</a></span> (1938) (dissenting opinion).</p>

</div>
```

---

## GROUP: content/cases/Frank v. Maryland.md  (`case`, 5 assertions)

### content_page

```
---
title: Frank v. Maryland
type: case
citation: "359 U.S. 360 (1959)"
parallel_cite: "79 S. Ct. 804; 3 L. Ed. 2d 877"
neutral_cite: 1959 U.S. LEXIS 1085
court: U.S.
court_level: scotus
circuit: ""
year: 1959
date_decided: 1959-05-04
docket: 278
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
  opinion_url: "https://www.courtlistener.com/opinion/105880/frank-v-maryland/"
  cluster_id: 105880
  opinion_id: null
  identity_checked: true
lake:
  record_id: Frank v. Maryland
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: Historical / origin
related:
  - "[[Camara v. Municipal Court]]"
  - "[[See v. City of Seattle]]"
tags:
  - case
  - fourth-amendment
  - administrative-search
  - special-needs
  - housing-inspection
  - overruled
  - historical
holding: "A municipal health inspector could demand entry to a home to look for nuisance conditions without a warrant, enforced by a fine for refusal, without violating the Due Process Clause — a rule overruled eight years later by Camara v. Municipal Court (1967), which required warrants for administrative inspections."
---

# Frank v. Maryland

*359 U.S. 360 (1959)* (No. 278) · Supreme Court of the United States · **Historical** · Treatment: **Overruled — rendered as history (⚪ unverified, pending S9)** — overruled by [[Camara v. Municipal Court]] (1967)
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the subsequent-history treatment below is authored orientation, not machine-certified. Identity cluster 105880 → 359 U.S. 360, decided 1959-05-04; Rule quote string-matched to the CL opinion text 2026-07-07. -->

## Background
A Baltimore health inspector, investigating a rat-infestation complaint, came to Aaron Frank's home and asked to inspect it for conditions the City Health Code proscribed. Frank refused to admit him without a warrant. Under § 120 of the Code, that refusal was itself an offense, and Frank was convicted and fined $20. He challenged the conviction, arguing that punishing him for resisting a warrantless inspection of his home violated the Fourteenth Amendment.

## Issue
Whether conditioning a criminal penalty on a homeowner's refusal to admit a health inspector, who has no warrant, to search the home for code violations is consistent with the Due Process Clause of the Fourteenth Amendment.

## Rule
The Court (Frankfurter, J.) upheld the ordinance. It reasoned that a routine, area-based health inspection touches only the periphery of the privacy the Fourteenth Amendment protects, is hedged with safeguards (advance notice, no forced entry), and serves a long-settled public-health function. Weighing that limited intrusion against the community's interest, the Court concluded: "In light of the long history of this kind of inspection and of modern needs, we cannot say that the carefully circumscribed demand which Maryland here makes on appellant's freedom has deprived him of due process of law." — 359 U.S. at 373. ^pin-373

## Application
Because the inspector could not force entry and the only consequence of refusal was a modest fine — not a search of the home over the occupant's objection — the Court treated the demand as a reasonable administrative measure rather than the kind of criminal search the warrant requirement governs. The [[Common Legal Terms#dissenting-opinion|dissent]] (Douglas, J., joined by Warren, C.J., Black and Brennan, JJ.) warned that the decision let officials into the home without the warrant the Fourth Amendment was written to require.

## Conclusion
The conviction was **affirmed** by a 5–4 vote. Frankfurter, J., delivered the opinion of the Court.

## Treatment & subsequent history
**Overruled by [[Camara v. Municipal Court]] (1967).** *Frank* held that administrative inspections of the home fall outside the warrant requirement. Eight years later *[[Camara v. Municipal Court|Camara]]* rejected that view, holding that administrative searches are significant Fourth Amendment intrusions and generally require a warrant — though one issued on area-based "administrative probable cause" rather than individualized suspicion. Its companion case, *[[See v. City of Seattle]]*, applied the same rule to commercial premises.

*Status note (⚪):* authored from a CourtListener-verified identity stub; the overruled treatment above is well-settled but has not completed the project's two-key certification, so the page renders under the ⚪ banner until S9 promotion. Preserved as **history**, never as live law.

## Appears on
- [[Special Needs and Administrative Searches]] — *Historical / origin*

## Sources
- [*Frank v. Maryland*, 359 U.S. 360 (1959)](https://www.courtlistener.com/opinion/105880/frank-v-maryland/) — pinpoint: 373 (Opinion of the Court; Frankfurter, J.); Rule quote string-matched to the CL opinion text 2026-07-07. Overruled by *Camara v. Municipal Court*, 387 U.S. 523 (1967) (successor page: [[Camara v. Municipal Court]]).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "87ebdbb0a6ecfaf4", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "359 U.S. 360 (1959)", "court": "U.S.", "neutral_cite": "1959 U.S. LEXIS 1085", "official_citation_present": true, "parallel_cite": "79 S. Ct. 804; 3 L. Ed. 2d 877", "title": "Frank v. Maryland", "year": "1959"}}
{"assertion_id": "2245c0b7f23fadbe", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A municipal health inspector could demand entry to a home to look for nuisance conditions without a warrant, enforced by a fine for refusal, without violating the Due Process Clause — a rule overruled eight years later by Camara v. Municipal Court (1967), which required warrants for administrative inspections.", "title": "Frank v. Maryland"}}
{"assertion_id": "f86eb746638e4fd2", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Historical / origin", "title": "Frank v. Maryland"}}
{"assertion_id": "27b8e7ce767cd27d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Frank v. Maryland", "varies_by_point": "false"}}
{"assertion_id": "bd15bf732759280d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Frank v. Maryland"}}
```

### lake record — Frank v. Maryland

```json
{
  "schema_version": "s2.v1",
  "record_id": "Frank v. Maryland",
  "status": "under_review",
  "identity": {
    "case_name": "Frank v. Maryland",
    "case_name_short": "Frank",
    "case_name_full": "Frank v. Maryland",
    "input_case_name": "Frank v. Maryland",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1959-05-04",
    "year": 1959,
    "docket": "278",
    "cluster_id": 105880,
    "lead_opinion_id": 9421796,
    "sibling_ids": [],
    "absolute_url": "/opinion/105880/frank-v-maryland/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "359 U.S. 360",
      "volume": "359",
      "reporter": "U.S.",
      "page": "360",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "79 S. Ct. 804",
        "volume": "79",
        "reporter": "S. Ct.",
        "page": "804",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 L. Ed. 2d 877",
        "volume": "3",
        "reporter": "L. Ed. 2d",
        "page": "877",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1959 U.S. LEXIS 1085",
        "volume": "1959",
        "reporter": "U.S. LEXIS",
        "page": "1085",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "359 U.S. 360",
        "volume": "359",
        "reporter": "U.S.",
        "page": "360",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 S. Ct. 804",
        "volume": "79",
        "reporter": "S. Ct.",
        "page": "804",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 L. Ed. 2d 877",
        "volume": "3",
        "reporter": "L. Ed. 2d",
        "page": "877",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1959 U.S. LEXIS 1085",
        "volume": "1959",
        "reporter": "U.S. LEXIS",
        "page": "1085",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "359 U.S. 360",
    "official_selection": {
      "court_class": "scotus",
      "selected": "359 U.S. 360",
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
    "date_created": "2026-07-07T13:27:55Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:28:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:28:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:28:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:28:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "frank-v-maryland--105880",
      "to_record_id": "Frank v. Maryland",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Frank v. Maryland

```
<opinion type="majority">
<author id="b431-4"><page-number citation-index="1" label="361">*361</page-number>Mr. Justice Frankfurter</author>
<p id="Az-">delivered the opinion of the Court.</p>
<p id="b431-5">Acting on a complaint from a resident of the 4300 block of Reisterstown Road, Baltimore, Maryland, that there were rats in her basement, Gentry, an inspector of the Baltimore City Health Department, began an. inspection of the houses in the vicinity looking for the source of the rats. In the middle of the afternoon of February 27, 1958, Gentry knocked on the door of appellant’s detached frame home at 4335 Reisterstown Road. After receiving no response he proceeded to inspect the area outside the house. This inspection revealed that the house was in an “extreme state of decay,” and that in the rear of the house there was a pile later identified as “rodent feces mixed with, straw and trash and debris to approximately half a ton.” During this inspection appellant came around the side of the house and asked Gentry to explain, his presence. Gentry responded that he had evidence of rodent infestation and asked appellant for permission to inspect the basement area. Appellant refused. At no time did Gentry have a warrant authorizing him to enter. The next forenoon Gentry, in the company of two police officers, returned to appellant’s house. After receiving no response to his knock, he reinspécted the exterior of the premises. He then swore out a warrant for appellant’s arrest alleging a violation of § 120 of Art. 12 of the Baltimore City Code. That section provides: <page-number citation-index="1" label="362">*362</page-number>Appellant was arrested on March 5, and the next'day was found guilty of the offense alleged in the warrant by a Police Justice for the Northern District .of Baltimore and fined twenty dollars. Ón appeal, the Criminal Court of Baltimore, in a <em>de novo </em>proceeding, also found appellant guilty. The Maryland Court of Appeals denied certio-rari. . The case came here under a challenge, <span class="citation no-link">28 U. S. C. § 1257</span> (2), to the validity of § 120 to determine whether appellant’s conviction for resisting an inspection of his house without a warrant was obtained in violation of the Fourteenth Amendment.</p>
<blockquote id="AYK"><page-number citation-index="1" label="361">*361</page-number>“Whenever the Commissioner of Health shall have cause to suspect that a nuisance exists in any house, cellar or enclosure, he may demand entry therein in the day time, and if the owner or occupier shall refuse or delay to open the same and admit a free examination, he shall forfeit and pay for every such refusal the sum of Twenty Dollars.”</blockquote>
<p id="b432-4"><page-number citation-index="1" label="362">*362</page-number>The Health.Code of the City of Baltimore, of which § 120 is an important part, deals with many of the multiform aspects of hygiene in modern urban, areas. A vital portion concerns the hygiene of housing. Typical of the content and method of enforcing its provisions is the section requiring that-“[e]very'dwelling and every part thereof shall.be kept clean and free-from any accumulation- of dirt, filth, rubbish, garbage or similar matter, and shall be kept free from vermin or rodent infestation.” Baltimore City Code; Art. 12, § 112. If the occupant of a building fails to meet this standard, he is notified by the Commissioner of Health to abate the substandard conditions.<footnotemark>1</footnotemark> Failure to remove these hazards to community health gives- rise to criminal prosecution. <em>Ibid. </em>The attempted inspection of appellant’s home was merely to ascertain the existence of evils to be corrected upon due notification or, in default of such correction, to be made the basis of punishment.</p>
<p id="AF0">We have said that “[t]he security of one’s privacy against arbitrary intrusion by the police” is fundamental to a free society and as such protected by the Fourteenth <page-number citation-index="1" label="363">*363</page-number>Amendment. <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span>. Application of the broad, restraints of due process compels inquiry into the naturé of the demand being made upon individual freedom in a particular context and the justification of social need on which the demand rests.</p>
<p id="b433-4">The history of the constitutional protection against official invasion of the citizen’s home makes explicit the human concerns which it was meant to respect. In years prior to the Revolution leading voices in England and the Colonies protested against the ransacking by Crown officers of the homes of citizens in séarch of evidence of crime or of illegally imported goods. The vivid memory by the newly independent Americans of these abuses produced the Fourth Amendment as a safeguard against such arbitrary official action by officers of the new Union, as like provisions had already found their way into State Constitutions.</p>
<p id="b433-5">In 1765, in England, what is properly called the great case of <em>Entick </em>v. <em>Carrington, </em>19 Howell’s State Trials, col. 1029, announced the principle of English law which became part of the Bill of Rights and whose basic protection has become imbedded in the concept of due process of law. It was there decided that English law did not allow officers of the Crown to break into a citizen’s home, under cover of a general executive warrant, to search for evidence of the utterance of libel. Among the reasons given for that decision were these:</p>
<blockquote id="b433-6">“It is very certain, that the law obligeth no man to accuse himself; because the necessary means of compelling self-accusation, falling upon the innocent' as well as the guilty, would be both cruel and unjust; and it should seem, that search for evidence is disallowed upon the -same principle. There tod the innocent would be confounded with the guilty.” <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Id.,</a></span> </em>at col. 1073.</blockquote>
<p id="b434-3"><page-number citation-index="1" label="364">*364</page-number>These were not novel pronouncements to the colonists. A few years earlier, in Boston, revenue' officers had been authorized to uso-Writs of Assistance, empowering them to search suspected places, inclúding private houses, for smuggled goods. In 1761 the validity of the use of the Writs was contested in the historic proceedings in Boston. James Otis attacked the Writ of Assistance because its use placed “the liberty of every man in the hands of every petty officer.” <footnotemark>2</footnotemark> His powerful argument so impressed itself first on his audience and later on the people of all the Colonies that President Adams' was in retrospect moved to say that “American Independence was then and there bórn.” <footnotemark>3</footnotemark> Many years later this Court, in <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, carefully reviewed, this history and pointed "out, as did. Lord Camden in <em>Entick v. Carrington, </em>that</p>
<blockquote id="b434-4">“. . ., the ‘unreasonable searches and seizures’ condemned in the Fourth Amendment are almost always made for the purpose of compelling a man to give</blockquote>
<blockquote id="b435-3"><page-number citation-index="1" label="365">*365</page-number>evidence against himself, which in criminal cases is condemned in the. Fifth Amendment; and compelling a man 'in a criminal case to be a witness against himself,’ which is condemned in the Fifth Amendment, throws light on the question as to what is an ‘unreasonable search and seizure’ within the meaning of the Fourth Amendment.” ' <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#633" aria-description="Citation for case: Boyd v. United States">116 U. S., at 633</a></span>.</blockquote>
<p id="b435-4">Against this background two protections emerge from the broad constitutional proscription of official invasion. The first of these is the right to be secure from intrusion into personal privacy, the right to shut* the door on officials óf the state unless their entry is under proper authority of law. The second, and intimately related protection, is self-protection: the right to resist unauthorized entry which has as its design the securing of information to fortify the coercive power of the state against the individual, information which may be used to effect a further deprivation of life or liberty or property. Thus, evidence of criminal action may not, save in very limited and closely confined situations, be seized without a judicially issued search warrant. It is this aspect of the constitutional protection to. which the quoted passages from <em>Entick </em>v. <em>Carrington </em>and <em>Boyd </em>v. <em>United States </em>refer. Certainly it is not necessary to accept any particular theory of the interrelationship of the Fourth and Fifth Amendments<footnotemark>4</footnotemark> to realize what history makes plain, that it was on the issue of the right to be secure from searches for evidence to be used in criminal prosecutions or for forfeitures that the great battle for fundamental liberty was fought. While these concerns for individual rights were the historic impulses behind the Fourth Amendment and its analogues in state constitutions, the application <page-number citation-index="1" label="366">*366</page-number>of the Fourth Amendment and\the extent to which the essential right of privacy is protected by the Due Process Clause of the Fourteenth Amendment are of course not restricted within these historic bounds.</p>
<p id="A9oW">But giving the fullést scope to this constitutional right to privacy, its protection cannot be here invoked. The attempted inspection of appellant’s home is -merely to determine whether conditions exist which the Baltimore Health Code proscribes. If they do appellant is notified to remedy the infringing conditions. No evidence for criminal prosecution is sought to be seized. Appellant is simply directed to do what he could have been ordered to do without any inspection, and what he cannot properly resist, namely, act in a manner consistent with the maintenance of minimum community standards of health and well-being, including his own. Appellant’s resistance can only, be based, not on admissible self-protection, but on a rarely voiced denial of any official justification for seeking to enter his home. The constitutional “liberty” that is asserted is the absolute right to refuse consent for an inspéction designed and pursued solely for the protection of the community’s health, even when the inspection is conducted with due regard for every convenience of time and place.</p>
<p id="b436-5">• The power of inspection granted by the Baltimore City Code is strictly limited, moré exacting than the analogous provisions of many other municipal codes. ' Valid grounds for suspicion of the existence of a nuisance must exist. Certainly the presence of a pile of filth in the back yard combined with the run-down condition of the house gave adequate grounds for such suspicion. The inspection must be made in the day time. Here was no midnight knock on the door, but an orderly visit in the middle of the afternoon with no suggestion that the hour was inconvenient. Moreover, the inspector has no power to force <page-number citation-index="1" label="367">*367</page-number>entry and did not attempt it. A. fine is imposed for resistance, but officials are not authorized to break past the unwilling occupant.</p>
<p id="b437-5">Thus, not only does the inspection touch at most upon the periphery of the important interests safeguarded by the Fourteenth Amendment’s protection against official intrusion, but it is hedged about with safeguards designed to make the least possible demand on .the individual occupant, and to cause only the slightest restriction on his claims of privacy. Such a demand must be assessed in the light of thé needs which have produced it.</p>
<p id="b437-6">Inspection without a warrant, as an adjunct to a regulatory scheme for the general welfare, of the community and not as a means of enforcing the criminal law, has antecedents deep in our history. For more than 200 years Maryland has empowered its officers to enter upon ships, carriages', shops, and homes in the service of the common welfare. In pre-revolutionary days trade, on which the viability oh the struggling Colonies depended, was of primary concern. Thus, at a time when the' tobacco trade was a vital part of Maryland’s economy, inspections of ships and carriages without a warrant could be made' to enforce uniform' standards for packing and shipping tobacco.<footnotemark>5</footnotemark> Similarly, suspected evasion of import <page-number citation-index="1" label="368">*368</page-number>duties on liquor and other goods could be found out by-inspection of stores and homes.<footnotemark>6</footnotemark> Generally the power of entry' was carefully limited,, requiring that ground for suspicion must exist and that the inspection be conducted between “the rising and the setting of the sun.” <footnotemark>7</footnotemark></p>
<p id="A0Wc">In 1776 the newly independent State of Maryland incorporated, as part of its basic Declaration of Rights, the principle</p>
<blockquote id="b438-4">“That all warrants, without oath or affirmation, to search suspected places, or to seize any person or property, are grievous and oppressive; and all general warrants — to search suspected places, or to apprehend suspected persons, without naming or describing the place, or the person in special — are illegal, and ought not to be granted.” See 3 Thorpe, Federal-and State Constitutions (1909), 1688.</blockquote>
<p id="b438-5">This provision was a product of the same history of abuse and protest that gave birth to the Fourth ■ Amendment.<footnotemark>8</footnotemark> It remains today as an essential part of Maryland’s Constitution. Yet, the years following its proclamation saw not a decline but a'marked increase in statutory authorization for inspection of the citizen’s home. Not only were the old regulations continued, but the power of <page-number citation-index="1" label="369">*369</page-number>inspection was extended to new community concerns. In 1782, Commissioners were empowered to “enter upon the lots, grounds, and possessions, of any person or persons . ...” in order to regulate and keep in repair the common sewerage systems.<footnotemark>9</footnotemark> Five years later similar entries on private property were allowed for the purpose of keeping the public roads in repair.<footnotemark>10</footnotemark> Typical of the regulatory statutes enacted in this period was an act permitting the clerk of the market “to examine and weigh all such bread, and to seize, for the use of the poor of the county, all such as they shall find deficient in weight or fineness, and not baked or marked as aforesaid . .,. .” <footnotemark>11</footnotemark> The penalty for resisting the entry of the clerk was “five pounds current money.” And so; when, in 1801, the power of inspection without a warrant became an instrument of the enforcement of the Baltimore health laws, no novel or untried procedures' were being invoked. The ordinance now challenged derives from this 1801 ordinance. It provided:</p>
<blockquote id="b439-4">“And be it enanted and ordained, That when, and as often as. the said commissioners of health, or any of them, shall have cause-to suspect a nuisance dangerous to the health of the city exists in any house, cellar or inclosure shut up from public view, they, or any one of them, may demand entry therein in the day time for the purpose of examining the same, and if the owner or occupier thereof shall refuse or delay <page-number citation-index="1" label="370">*370</page-number>to open the same and to admit a free examination, he shall forfeit and pay for every such refusal the sum of twenty dollars, for the use of the corporation.” <footnotemark>12</footnotemark></blockquote>
<p id="b440-4">From the passage of this ordinance to the present the prevention and abatement of “nuisances” on private property has been one-of the chief concerns of the Baltimore City Health Department.<footnotemark>13</footnotemark> In the latter half of the nineteenth century, in the years following the ratification of the Fourteenth Amendment, thousands upon thousands of inspections were made under authority df this ordinance.<footnotemark>14</footnotemark>. Thus - the system of inspection here under attack, having its beginning in Maryland’s colonial history, has been an integral part of the enforcement of Baltimore’s health laws for more than a century and a half. The legal significance of such a long and consistent history of state practice has been illuminated for us by Mr. Justice Holmes:</p>
<blockquote id="b440-5">“The Fourteenth Amendment, itself a historical product, did not destroy history for the States and substitute mechanical compartments of law all exactly alike. If a thing has been practised for two hundred years by common consent, it will need a strong case for the Fourteenth Amendment to affect it, . . . .” <em>Jackman </em>v. <em>Rosenbaum Co., </em><span class="citation" data-id="100034"><a href="/opinion/100034/jackman-v-rosenbaum-co/#31" aria-description="Citation for case: Jackman v. Rosenbaum Co.">260 U. S. 22, 31</a></span>. (As to the constitutional significance of a “time-honored procedure” see <em>Murray’s Lessee </em>v. <em>Hoboken Land and Improvement Co., </em><span class="citation" data-id="87010"><a href="/opinion/87010/den-ex-dem-murray-v-hoboken-land-improvement-co/" aria-description="Citation for case: Den Ex Dem. Murray v. Hoboken Land &amp; Improvement Co.">18 How. 272</a></span>, and <em>Ownbey </em>v. <em>Morgan, </em><span class="citation" data-id="99782"><a href="/opinion/99782/ownbey-v-morgan/" aria-description="Citation for case: Ownbey v. Morgan">256 U. S. 94</a></span>.)</blockquote>
<p id="b441-4"><page-number citation-index="1" label="371">*371</page-number>Of course, this wise reminder, that what free people have found consistent' with their enjoyment of freedom for centuries is hardly to be deemed to violate due process, does not freeze due process within the confines of historical facts or discredited attitudes.<footnotemark>15</footnotemark> “It is of the very nature of a free .society to advance in its standards of what is deemed reasonable and right. Representing as it does a living principle, due process is not confined within a permanent catalogue of whgt may at a given time be deemed the limits or the essentials of fundamental rights.” <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span>.</p>
<p id="b441-5">The power here challenged rests not only on a long history of its exercise. It is a power which was continually strengthened and applied to wider concerns through those very years when the right of individuals to be free, from peremptory official invasion received increasing legislative and judicial protection. Nor is this a situation where a new body of knowledge displaces previous premises of action. There is a total want of important modification in the circumstances or the structure of society which calls for a disregard of so much history. On the contrary, the problems which gave rise to these ordinances have multiplied manifold, as have the difficulties of enforcement. The need to maintain basic, minimal standards of housing, to prevent the spread of disease and of that pervasive breakdown in the fiber of a people which is produced by slums and the absence of the barest essentials of civilized living, has mounted to a major concern of American government. The growth of cities, the crowding of populations, the increased awareness of the responsibility of the state for the living conditions of its citizens, all have combined to create problems of the <page-number citation-index="1" label="372">*372</page-number>enforcement of minimum standards of far greater magnitude than the writers of these ancient inspection laws ever dreamed. Time and experience have -forcefully taúght that the power to inspect dwelling places, either as a matter of. systematic área-by-area search or, as here, to treat a specific problem, is of indispensable importance to the maintenance of community health; a power that would be greatly hobbled by the blanket requirement of the safeguards necessary for a search of evidence of criminal acts. The need for preventive action is great, and city after city has seen this need and granted the power of inspection to its health officials; and these inspections are apparently welcomed by all but an insignificant few.<footnotemark>16</footnotemark> Certainly, the nature of our society has not vitiated the need for inspections first thought necessary 158 years;ago, nor has experience revealed any abuse or inroad on freedom in meeting this need by means that history and dominant public opinion have sanctioned.</p>
<p id="b442-4">That there is “a total unlikeness” between “official acts and proceedings,” <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 624</a></span>, for which the legal protection of privacy requires a <page-number citation-index="1" label="373">*373</page-number>search warrant under the Fourteenth Amendment, and the situation now under consideration is laid bare by the suggestion that the kind of an' inspection by a health official with which we are concerned may be satisfied by what is, in effect, a synthetic search warrant, an authorization “for periodic inspections.” L a search warrant •be constitutionally required, the requirement cannot be flexibly interpreted to dispense with the rigorous constitutional restrictions for its issue. A loose basis for granting a search warrant for the situation before us is to enter by way of the back door to a recognition of the fact that by reason of their intrinsic elements, their historic sanctions, and their safeguards, the Maryland proceedings .requesting permission to make a search without intruding when permission is denied, do not offend the protection of the Fourteenth Amendment.</p>
<p id="b443-4">In light of the long history of this kind of inspection and of modern needs, we cannot say that the carefully circumscribed demand which Maryland here makes on appellant’s freedom has deprived him of due process of law.</p>
<p id="b443-5">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b432-6"> If the nuisance constitutes an actual menace to health the Commissioner may abate it forthwith. Baltimore City Code, Art. 12, §112.</p>
</footnote>
<footnote label="2">
<p id="b434-5"> Tudor, Life of James Otis (1823), 66. No complete text of the Otis speech is extant, but see notes of Horace Gray, Jr. in Quincy’s Massachusetts Reports for 1761-1762, App. I, pp. 469 <em>et seq. </em>Tudor’s life contains an account of it as well as of the events leading to the. speech and the reaction to it-.</p>
</footnote>
<footnote label="3">
<p id="b434-6"> <em>Id., </em>at 61. Adams said:</p>
<blockquote id="b434-7">“Otis was a flame of fire; with a promptitude of classical allusions, a depth of research, a rapid summary of historical events and dates, a profusion of legal authorities, a prophetic glance of his eyes into futurity, and a ’ rapid torrent of impetuous eloquence, he hurried away all before him. American Independence was then and there born. The seeds of patriots and heroes, to defend the <em>Non sine Diis animosus infans; </em>to defend the vigorous youth, were then and there sown. Every man of an immense crouded audience appeared to me to go away as I did, ready to take arms against Writs of Assistance. Then and there, was the first scene of . the first act of opposition, to the arbitrary claims- of Great Britain. Then and there, the child Independence was born. In fifteen years, i. e. in 1776, he grew up to manhood, and declared himself free.” <em>Id., </em>at 60-61.</blockquote>
</footnote>
<footnote label="4">
<p id="b435-5"> The Court in <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, relied heavily on the interrelationship between the Fourth and Fifth Amendments, a view challenged by Professor Wigmore. See 8 Wigmore; Evidence. (3d ed. 19.40), §2264.</p>
</footnote>
<footnote label="5">
<p id="b437-7"> Nearly all the early Maryland statutes are contained in Records of the States of the United States of America, a collection compiled by the Library of Congress in association with .the University of North Carolina in 1949. This collection is on microfilm. Many volumes of the early Maryland Session Laws are available in various library collections throughout the country. No complete collection is known to exist. A typical tobacco inspection statute is Maryland Laws, November 1773, c. 1, §§ LXXIV, LXXX. At times a warrant was required for inspections. of homes. <em>Id., </em>§ LXXIII. See also Maryland Laws, 1717, c. VII. Other Colonies also had statutes allowing inspection to enforce standards for the manufacture or shipping of various items of trade. See, e. <em>g., </em>Virginia Laws, 15 Geo. II (1742), <page-number citation-index="1" label="368">*368</page-number>c. IV (pork and beef); Virginia Laws, 12 Geo. Ill (1772), c. ll (flour and bread); Pennsylvania Laws, 1722,' c. CCLII (flour and bread); Pennsylvania Laws, 1727, c. CCXCV (beef and pork); Pennsylvania Laws, 1729-1730, c. CCCXVI (hemp).</p>
</footnote>
<footnote label="6">
<p id="b438-9"> See, <em>e. g., </em>Maryland. Laws, 1715, e. XLVI (tobacco); Maryland Laws, May 1756, p. 5, §XLVI; Maryland Laws, March 1758, p. 3, §X.</p>
</footnote>
<footnote label="7">
<p id="b438-12"> <em>Ibid.</em></p>
</footnote>
<footnote label="8">
<p id="b438-13"> See <em>Givner </em>v. <em>State, </em><span class="citation" data-id="2305304"><a href="/opinion/2305304/givner-v-state/#492" aria-description="Citation for case: Givner v. State">210 Md. 484, 492-494</a></span>, <span class="citation" data-id="2305304"><a href="/opinion/2305304/givner-v-state/#768" aria-description="Citation for case: Givner v. State">124 A. 2d 764, 768-769</a></span>. The Maryland Court of Appeals has said that this provision of its Declaration of Rights (originally Article 23, now Article 26) is <em>“in pari materia” </em>with the Fourth Amendment to the United States Constitution. <span class="citation" data-id="2305304"><a href="/opinion/2305304/givner-v-state/#492" aria-description="Citation for case: Givner v. State"><em>Id., </em>at 492</a></span>.</p>
</footnote>
<footnote label="9">
<p id="b439-5"> Maryland Laws, Nov. 1782, c. XVII, § VII. A similar law had been in force in Pennsylvania since 1761. Pennsylvania Laws, 1761— 1762, c. C.CCCLXXX.</p>
</footnote>
<footnote label="10">
<p id="b439-7"> Maryland Laws, April 1787, c. XXIII. See also Pennsylvania Laws, 1782, ci MXXXI.</p>
</footnote>
<footnote label="11">
<p id="b439-8"> Maryland Laws, Nov. 1789, c. VIII, § 5. ■ See also Maryland Laws, Nov. 1792, c. LXV, § VII; Maryland Laws. 1793, c. LVI; Maryland Laws, 1784, c. VII.</p>
</footnote>
<footnote label="12">
<p id="b440-6"> Baltimore Ordinances, 1801-1802, No. 23, §6. The Baltimore City Health Department may be the oldest in the country. See 35 Am. J. of Public Health (Jan. 1945), 49.</p>
</footnote>
<footnote label="13">
<p id="b440-7"> See Howard, Public Health Administration and the Natural History of Disease in Baltimore, Maryland, 1797-1920 (1924), 140.</p>
</footnote>
<footnote label="14">
<p id="AOI"> See, <em>id., </em>at 145-146. For example, in 1880 there were 4,292 nuisances inspected by sanitary inspectors. In 1890 there were 34,138 such inspections. <em>Ibi</em>d.</p>
</footnote>
<footnote label="15">
<p id="b441-6"> Compare <em>Kotch </em>v. <em>Board of River Port Pilot Comm’rs, </em><span class="citation" data-id="9419962"><a href="/opinion/104397/kotch-v-board-of-river-port-pilot-commrs-for-port-of-new-orleans/" aria-description="Citation for case: Kotch v. Board of River Port Pilot Comm&#x27;rs for Port of...">330 U. S. 552</a></span>, and <em>Ownbey </em>v. <em>Morgan, </em><span class="citation" data-id="99782"><a href="/opinion/99782/ownbey-v-morgan/" aria-description="Citation for case: Ownbey v. Morgan">256 U. S. 94</a></span>, with <em>Brown </em>v. <em>Board of Education, </em><span class="citation" data-id="105221"><a href="/opinion/105221/brown-v-board-of-education/" aria-description="Citation for case: Brown v. Board of Education">347 U. S. 483</a></span>.</p>
</footnote>
<footnote label="16">
<p id="A2W"> The Baltimore Health Department keeps á record of the number of inspections made annually. All but a few of these are inspections of dwellings. The figures for the last five years are as follows: 1954, 28,081 inspections; 1955, 25,021 inspections; 1956, 35,120 inspections; 1957, 33,573 inspections; 1958, 36,119 inspections. Memorandum of Appellee at Request of Court 2. The Health Commissioner of Baltimore estimates that the number of prosecutions under §120 average one per year.</p>
<p id="b442-7">Of 57 cities whose health codes were studied by the Urban Renewal Administration, 36 empowered their officers to enter and inspect for violations. See Provisions of Housing Codes in Various American Cities, Urban Renewal Bulletin No. 3 (published by Urban Renewal Administration of the Housing and Home Finance Agency 1956).</p>
<p id="b442-8">For a discussion of some of the problems of Urban Renewal, see Note, <span class="citation no-link">72 Harv. L. Rev. 504</span>.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Frazier v. Cupp.md  (`case`, 5 assertions)

### content_page

```
---
title: "Frazier v. Cupp"
type: case
citation: "394 U.S. 731 (1969)"
parallel_cite: "89 S. Ct. 1420; 22 L. Ed. 2d 684"
neutral_cite: 1969 U.S. LEXIS 1870
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1969
date_decided: 1969-04-23
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1969-04-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Frazier v. Cupp
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107913/frazier-v-cupp/"
  cluster_id: 107913
  opinion_id: 107913
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Colorado v. Connelly]]", "[[Brown v. Mississippi]]", "[[Schneckloth v. Bustamonte]]"]
aliases: []
tags: ["case", "confessions", "voluntariness", "police-deception", "due-process", "totality"]
holding: "Police misrepresentation (falsely telling a suspect his codefendant had confessed) did not render the confession involuntary; deception…"
lake:
  record_id: Frazier v. Cupp
  status: under_review
  projected_at: 2026-07-06
---

# Frazier v. Cupp

*394 U.S. 731 (1969)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Martin Frazier was questioned about a murder. During the interrogation an officer falsely told him that his cousin and companion, Jerry Lee Rawls, had already confessed and implicated him. After receiving partial warnings of his rights, Frazier then made an incriminating statement. He later argued the confession was involuntary because it had been induced by the officer's deception.

## Issue
Whether a confession is rendered involuntary, and thus inadmissible, because the police obtained it by falsely telling the suspect that an accomplice had already confessed.

## Rule
No. Police deception is one relevant factor, but it does not by itself make an otherwise voluntary confession inadmissible; voluntariness is judged on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]. "The fact that the police misrepresented the statements that Rawls had made is, while relevant, insufficient in our view to make this otherwise voluntary confession inadmissible. These cases must be decided by viewing the 'totality of the circumstances' . . . ." — 394 U.S. at 739. ^pin-739

## Application
Frazier received partial warnings of his rights before confessing, the questioning was of short duration, and he was a mature individual of normal intelligence. Against that backdrop the officer's misrepresentation that Rawls had confessed — though relevant — was not enough to overbear his will, so on the totality of these circumstances the confession was voluntary and properly admitted.

## Conclusion
The confession was voluntary despite the police misrepresentation; the conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Frazier* remains the leading authority that interrogation deception is only one factor in the totality-of-the-circumstances voluntariness inquiry — consistent with the later rule of [[Colorado v. Connelly]] that involuntariness requires coercive police conduct.

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Frazier v. Cupp*, 394 U.S. 731 (1969) — https://www.courtlistener.com/opinion/107913/frazier-v-cupp/ — pinpoint: 739.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "946fb3149078bf76", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "394 U.S. 731 (1969)", "court": "U.S. Supreme Court", "neutral_cite": "1969 U.S. LEXIS 1870", "official_citation_present": true, "parallel_cite": "89 S. Ct. 1420; 22 L. Ed. 2d 684", "title": "Frazier v. Cupp", "year": "1969"}}
{"assertion_id": "1adc309c77c804bd", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Progeny / Refinement", "title": "Frazier v. Cupp"}}
{"assertion_id": "3a588cf7b5e374b2", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Police misrepresentation (falsely telling a suspect his codefendant had confessed) did not render the confession involuntary; deception…", "title": "Frazier v. Cupp"}}
{"assertion_id": "45fcc22e7649031e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Frazier v. Cupp"}}
{"assertion_id": "74d552e16d4a8245", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1969-04-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Frazier v. Cupp", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Frazier v. Cupp", "varies_by_point": "false"}}
```

### lake record — Frazier v. Cupp

```json
{
  "schema_version": "s2.v1",
  "record_id": "Frazier v. Cupp",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Frazier v. Cupp",
    "case_name_short": "Frazier",
    "case_name_full": "Frazier v. Cupp, Warden",
    "input_case_name": "Frazier v. Cupp",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1969-04-23",
    "year": 1969,
    "docket": null,
    "cluster_id": 107913,
    "lead_opinion_id": 107913,
    "sibling_ids": [
      107913
    ],
    "absolute_url": "/opinion/107913/frazier-v-cupp/",
    "identity_method": "pending",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "394 U.S. 731",
      "volume": "394",
      "reporter": "U.S.",
      "page": "731",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "89 S. Ct. 1420",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "1420",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 684",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "684",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1969 U.S. LEXIS 1870",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "1870",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "394 U.S. 731",
        "volume": "394",
        "reporter": "U.S.",
        "page": "731",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 S. Ct. 1420",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "1420",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 684",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "684",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1969 U.S. LEXIS 1870",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "1870",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "394 U.S. 731",
    "official_selection": {
      "court_class": "scotus",
      "selected": "394 U.S. 731",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-739",
      "page": null,
      "quote": "--- # Frazier v. Cupp *394 U.S. 731 (1969)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Martin Frazier was questioned about a murder. During the interrogation an officer falsely told him that his cousin and companion, Jerry Lee Rawls, had already confessed and implicated him. After receiving partial warnings of his rights, Frazier then made an incriminating statement. He later argued the confession was involuntary because it had been induced by the officer's deception. ## Issue Whether a confession is rendered involuntary, and thus inadmissible, because the police obtained it by falsely telling the suspect that an accomplice had already confessed. ## Rule No. Police deception is one relevant factor, but it does not by itself make an otherwise voluntary confession inadmissible; voluntariness is judged on the totality of the circumstances.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1969-04-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Frazier v. Cupp",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Flores Ramos",
          "cluster_id": 10160768,
          "cite": [
            "367 Or. 292",
            "478 P.3d 515"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Vasquez-Santiago",
          "cluster_id": 10133179,
          "cite": [
            "301 Or. App. 90",
            "456 P.3d 270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Larry Whitfield",
          "cluster_id": 2968731,
          "cite": [
            "695 F.3d 288",
            "2012 U.S. App. LEXIS 17762",
            "2012 WL 3591038"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hughes",
          "cluster_id": 214334,
          "cite": [
            "640 F.3d 428",
            "2011 U.S. App. LEXIS 7338",
            "2011 WL 1332061"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Burnette",
          "cluster_id": 2519721,
          "cite": [
            "535 F. Supp. 2d 772",
            "2007 WL 4911523"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane1_negative"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "North Carolina v. Butler",
          "cluster_id": 110065,
          "cite": [
            "60 L. Ed. 2d 286",
            "99 S. Ct. 1755",
            "441 U.S. 369",
            "1979 U.S. LEXIS 91"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lego v. Twomey",
          "cluster_id": 108429,
          "cite": [
            "30 L. Ed. 2d 618",
            "92 S. Ct. 619",
            "404 U.S. 477",
            "1972 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sharp v. State",
          "cluster_id": 2458281,
          "cite": [
            "707 S.W.2d 611",
            "1986 Tex. Crim. App. LEXIS 1225"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miller v. Fenton",
          "cluster_id": 111542,
          "cite": [
            "88 L. Ed. 2d 405",
            "106 S. Ct. 445",
            "474 U.S. 104",
            "1985 U.S. LEXIS 144",
            "54 U.S.L.W. 4022"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Tucker",
          "cluster_id": 109063,
          "cite": [
            "41 L. Ed. 2d 182",
            "94 S. Ct. 2357",
            "417 U.S. 433",
            "1974 U.S. LEXIS 71"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Green v. State",
          "cluster_id": 1657475,
          "cite": [
            "934 S.W.2d 92",
            "1996 Tex. Crim. App. LEXIS 185",
            "1996 WL 512395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Georgia v. Randolph",
          "cluster_id": 145669,
          "cite": [
            "164 L. Ed. 2d 208",
            "126 S. Ct. 1515",
            "547 U.S. 103",
            "2006 U.S. LEXIS 2498"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. State",
          "cluster_id": 1577216,
          "cite": [
            "790 S.W.2d 568",
            "1989 Tex. Crim. App. LEXIS 151",
            "1989 WL 69709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beckwith v. United States",
          "cluster_id": 109430,
          "cite": [
            "48 L. Ed. 2d 1",
            "96 S. Ct. 1612",
            "425 U.S. 341",
            "1976 U.S. LEXIS 147",
            "37 A.F.T.R.2d (RIA) 1232"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Edwards",
          "cluster_id": 108995,
          "cite": [
            "39 L. Ed. 2d 771",
            "94 S. Ct. 1234",
            "415 U.S. 800",
            "1974 U.S. LEXIS 120"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jenkins",
          "cluster_id": 1195356,
          "cite": [
            "997 P.2d 1044",
            "95 Cal. Rptr. 2d 377",
            "22 Cal. 4th 900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tennessee v. Street",
          "cluster_id": 111424,
          "cite": [
            "85 L. Ed. 2d 425",
            "105 S. Ct. 2078",
            "471 U.S. 409",
            "1985 U.S. LEXIS 9",
            "53 U.S.L.W. 4527",
            "17 Fed. R. Serv. 817"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moore v. Illinois",
          "cluster_id": 109757,
          "cite": [
            "54 L. Ed. 2d 424",
            "98 S. Ct. 458",
            "434 U.S. 220",
            "1977 U.S. LEXIS 163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107913) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDgwMjU5MjAwMDAwJnM9MjIyNDg4MiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107913%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 6,
        "triage_snippet_classified": 194
      },
      "lane2_top_cited": {
        "query": "cites:(107913)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMzUmcz0xNTUwODA2JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107913%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107913)",
        "reviewed": 22,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 22,
        "triage_read": 0,
        "triage_snippet_classified": 22
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107913)",
    "indexed_citing_opinions": 940,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107913,
        "count": 940,
        "count_source": "search"
      }
    ],
    "citation_count": 1469,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/frazier-v-cupp.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc5MDYxNTImcz03ODYxNzE4JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107913%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107913,
        "cited_id": 103352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107684,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107848,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 278627,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 1296618,
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
    "date_created": "2026-07-05T04:55:46Z",
    "date_modified": "2026-07-06T07:48:51Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T04:55:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T04:55:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:01:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T04:55:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Frazier v. Cupp

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b806-12">
  Mr. Justice Marshall
 </author>
<p id="AKM">
  delivered the opinion of the Court.
 </p>
<p id="b806-13">
  Petitioner was convicted in an Oregon state court of second-degree murder in connection with the September 22, 1964, slaying of one Russell Anton Marleau. After the Supreme Court of Oregon had affirmed his conviction, <span class="citation" data-id="1296618"><a href="/opinion/1296618/state-v-frazier/" aria-description="Citation for case: State v. Frazier">245 Ore. 4</a></span>, <span class="citation" data-id="1296618"><a href="/opinion/1296618/state-v-frazier/" aria-description="Citation for case: State v. Frazier">418 P. 2d 841</a></span> (1966), petitioner filed a petition for a writ of habeas corpus in the United States District Court for the District of Oregon. The District Court granted the writ, but the Court of Appeals for the Ninth Circuit reversed, <span class="citation" data-id="278627"><a href="/opinion/278627/clarence-t-gladden-warden-v-martin-rene-frazier/" aria-description="Citation for case: Clarence T. Gladden, Warden v. Martin Rene Frazier">388 F. 2d 777</a></span> (1968). We
  <span citation-index="1" class="star-pagination" label="733"> 
   *733
   </span>
  granted certiorari to consider three contentions of error raised by petitioner. <span class="citation multiple-matches"><a href="/c/U.%20S./393/821/">393 U. S. 821</a></span> (1968). Although petitioner’s case has been ably briefed and argued by appointed counsel, we find none of these allegations sufficient to warrant reversal.
 </p>
<p id="b807-5">
  I.
 </p>
<p id="b807-6">
  Petitioner’s first argument centers on certain allegedly prejudicial remarks made during the prosecutor’s opening statement. Petitioner had been indicted jointly with his cousin, Jerry Lee Rawls, who pleaded guilty to the same offense. Prior to petitioner’s trial, petitioner’s defense counsel told the prosecutor that Rawls would invoke his privilege against self-incrimination if he were called to the stand; defense counsel warned the prosecutor not to rely in his opening statement upon Rawls’ expected testimony. The prosecutor replied that he would act on the basis of “all of the information I have concerning [Rawls’] testimony.” Before trial, he consulted with a police officer who had spoken to Rawls and with Rawls’ probation officer; each indicated his belief that Rawls would testify. Similar information came, through a sheriff’s report, from some of Rawls’ close relatives. Because of these reports, the prosecutor concluded that Rawls would testify if asked to do so. The court below felt that the prosecutor also relied on the fact that Rawls had pleaded guilty and was awaiting sentence. This would give him reason, the court felt, to cooperate with the prosecutor.
 </p>
<p id="b807-7">
  In any case, after the trial began the prosecutor included in his opening statement a summary of the testimony he expected to receive from Rawls. The summary was not emphasized in any particular way; it took only a few minutes to recite and was sandwiched between a summary of petitioner’s own confession and a description of the circumstantial evidence the State would introduce.
 </p>
<p id="b808-5">
<span citation-index="1" class="star-pagination" label="734"> 
   *734
   </span>
  At one point the prosecutor referred to a paper he was holding in his hands to refresh his memory about something Rawls had said. Although the State admitted in argument here that the jury might fairly have believed that the prosecutor was referring to Rawls’ statement, he did not explicitly tell the jury that this paper was Rawls’ confession, nor did he purport to read directly from it. A motion for a mistrial was made at the close of the opening statement, but it was denied. Later, the prosecutor called Rawls to the stand. Rawls informed the court that he intended to assert his privilege against self-incrimination in regard to every question concerning his activities on the morning of September 22,1964. The matter was not further pursued, and Rawls was dismissed from the stand. His appearance could not have lasted more than two or three minutes. The motion for mistrial was renewed and once again denied.
 </p>
<p id="b808-6">
  Petitioner argues that this series of events placed the substance of Rawls’ statement before the jury in a way that “may well have been the equivalent in the jury’s mind of testimony,”
  <em>
   Douglas
  </em>
  v.
  <em>
   Alabama,
  </em>
  <span class="citation" data-id="9422992"><a href="/opinion/107015/douglas-v-alabama/#419" aria-description="Citation for case: Douglas v. Alabama">380 U. S. 415, 419</a></span> (1965), and that, as in
  <em>
   Bruton
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/#128" aria-description="Citation for case: Bruton v. United States">391 U. S. 123, 128</a></span> (1968), the statement “added substantial, perhaps even critical, weight to the Government’s case in a form not subject to cross-examination . . . .” In this way, petitioner claims he was denied his constitutional right of confrontation, guaranteed by the Sixth and Fourteenth Amendments to the Constitution. See
  <em>
   Pointer
  </em>
  v.
  <em>
   Texas,
  </em>
  <span class="citation" data-id="9422988"><a href="/opinion/107014/pointer-v-texas/" aria-description="Citation for case: Pointer v. Texas">380 U. S. 400</a></span> (1965). Although the judge did caution the jurors that they “must not regard any statement made by counsel in your presence during the proceedings concerning the facts of this case as evidence,” petitioner contends that
  <em>
   Bruton
  </em>
  v.
  <em>
   United <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">States, supra,</a></span>
  </em>
  disposes of the contention that limiting instructions of this sort can be relied upon to cure the error which occurred. Although the question thus posed is not an
  <span citation-index="1" class="star-pagination" label="735"> 
   *735
   </span>
  easy one, we cannot agree with petitioner’s conclusion.
 </p>
<p id="b809-4">
  First of all, it is clear that this case is quite different from either
  <em>
   <span class="citation" data-id="9422992"><a href="/opinion/107015/douglas-v-alabama/" aria-description="Citation for case: Douglas v. Alabama">Douglas</a></span>
  </em>
  or
  <em>
   <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span>.
  </em>
  In
  <em>
   <span class="citation" data-id="9422992"><a href="/opinion/107015/douglas-v-alabama/" aria-description="Citation for case: Douglas v. Alabama">Douglas</a></span>,
  </em>
  the prosecutor called the defendant’s coconspirator to the stand and read his alleged confession to him; the coconspirator was required to assert his privilege against self-incrimination repeatedly as the prosecutor asked him to confirm or deny each statement. The Court found that this procedure placed powerfully incriminating evidence before the jury in a manner which effectively denied the right of cross-examination. Here, Rawls was on the stand for a very short time and only a paraphrase of the statement was placed before the jury. This was done not during the trial, while the person making the statement was on the stand, but in an opening statement. In addition, the jury was told that the opening statement should not be considered as evidence. Certainly the impact of the procedure used here was much less damaging than was the case in
  <em>
   <span class="citation" data-id="9422992"><a href="/opinion/107015/douglas-v-alabama/" aria-description="Citation for case: Douglas v. Alabama">Douglas</a></span>.
  </em>
  And unlike the situation in
  <em>
   <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span>,
  </em>
  the jury was not being asked to perform the mental gymnastics of considering an incriminating statement against only one of two defendants in a joint trial. Moreover, unlike the situation in either
  <em>
   <span class="citation" data-id="9422992"><a href="/opinion/107015/douglas-v-alabama/" aria-description="Citation for case: Douglas v. Alabama">Douglas</a></span>
  </em>
  or
  <em>
   <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span>,
  </em>
  Rawls’ statement was not a vitally important part of the prosecution’s case.
 </p>
<p id="b809-5">
  We believe that in these circumstances the limiting instructions given were sufficient to protect petitioner’s constitutional rights.
  <a class="footnote" href="#fn*" id="fn*_ref">
   *
  </a>
  As the Court said in
  <em>
   Bruton,
  </em>
  <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/#135" aria-description="Citation for case: Bruton v. United States">391 U. S., at 135</a></span>, “Not every admission of inadmissible hearsay or other evidence can be considered to be reversible error unavoidable through limiting instructions; instances occur in almost every trial where inadmissible evidence creeps in, usually inadvertently.” See
  <em>
   Hopt
  </em>
  v.
  <em>
   Utah,
  </em>
  120
  <span citation-index="1" class="star-pagination" label="736"> 
   *736
   </span>
  U. S. 430, 438 (1887). It may be that some remarks included in an opening or closing statement could be so prejudicial that a finding of error, or even constitutional error, would be unavoidable. But here we have no more than an objective summary of evidence which the prosecutor reasonably expected to produce. Many things might happen during the course of the trial which would prevent the presentation of all the evidence described in advance. Certainly not every variance between the advance description and the actual presentation constitutes reversible error, when a proper limiting instruction has been given. Even if it is unreasonable to assume that a jury can disregard a coconspirator’s statement when introduced against one of two joint defendants, it does not seem at all remarkable to assume that the jury will ordinarily be able to limit its consideration to the evidence introduced during the trial. At least where the anticipated, and unproduced, evidence is not touted to the jury as a crucial part of the prosecution’s case, “it is hard for us to imagine that the minds of the jurors would be so influenced by such incidental statements during this long trial that they would not appraise the evidence objectively and dispassionately.”
  <em>
   United States
  </em>
  v.
  <em>
   Socony-Vacuum Oil Co.,
  </em>
  <span class="citation" data-id="9419105"><a href="/opinion/103352/united-states-v-socony-vacuum-oil-co/#239" aria-description="Citation for case: United States v. Socony-Vacuum Oil Co.">310 U. S. 150, 239</a></span> (1940).
 </p>
<p id="b810-5">
  The Court of Appeals seemed to feel that this aspect of the case turned on whether or not the prosecutor acted “in a good faith expectation that Rawls would testify.” <span class="citation" data-id="278627"><a href="/opinion/278627/clarence-t-gladden-warden-v-martin-rene-frazier/#780" aria-description="Citation for case: Clarence T. Gladden, Warden v. Martin Rene Frazier">388 F. 2d, at 780-781</a></span>. While we do not believe that the prosecutor’s good faith, or lack of it, is controlling in determining whether a defendant has been deprived of the right of confrontation guaranteed by the Sixth and Fourteenth Amendments, we agree with the Court of Appeals’ factual determination in this case. The evidence presented in the record is sufficient to support the Oregon Supreme Court’s conclusion that “the state could reasonably expect [Rawls] to testify in line with his
  <span citation-index="1" class="star-pagination" label="737"> 
   *737
   </span>
  previous statements.” <span class="citation" data-id="1296618"><a href="/opinion/1296618/state-v-frazier/#9" aria-description="Citation for case: State v. Frazier">245 Ore., at 9</a></span>, <span class="citation" data-id="1296618"><a href="/opinion/1296618/state-v-frazier/#843" aria-description="Citation for case: State v. Frazier">418 P. 2d, at 843</a></span>, Accordingly, there is no need to decide whether the type of prosecutorial misconduct alleged to have occurred would have been sufficient to constitute reversible constitutional error. Cf.
  <em>
   Miller
  </em>
  v.
  <em>
   Pate,
  </em>
  <span class="citation" data-id="107354"><a href="/opinion/107354/miller-v-pate/" aria-description="Citation for case: Miller v. Pate">386 U. S. 1</a></span> (1967). Therefore, because we find neither prosecutorial misconduct nor a deprivation of the right of confrontation, we agree with the Court of Appeals that nothing which occurred during the prosecution’s opening statement would warrant federal habeas relief.
 </p>
<p id="b811-5">
  II.
 </p>
<p id="b811-6">
  Petitioner’s second argument concerns the admission into evidence of his own confession. The circumstances under which the confession was obtained can be summarized briefly. Petitioner was arrested about 4:15 p. m. on September 24, 1964. He was taken to headquarters where questioning began at about 5 p. m. The interrogation, which was tape-recorded, ended slightly more than an hour later, and by 6:45 p. m. petitioner had signed a written version of his confession.
 </p>
<p id="b811-7">
  After the questioning had begun and after a few routine facts were ascertained, petitioner was questioned briefly about the location of his Marine uniform. He was next asked where he was on the night in question. Although he admitted that he was with his cousin Rawls, he denied being with any third person. Then petitioner was given a somewhat abbreviated description of his constitutional rights. He was told that he could have an attorney if he wanted one and that anything he said could be used against him at trial. Questioning thereafter became somewhat more vigorous, but petitioner continued to deny being with anyone but Rawls. At this point, the officer questioning petitioner told him, falsely, that Rawls had been brought in and that he had confessed. Petitioner still was reluctant to talk, but
  <span citation-index="1" class="star-pagination" label="738"> 
   *738
   </span>
  after the officer sympathetically suggested that the victim had started a fight by making homosexual advances, petitioner began to spill out his story. Shortly after he began he again showed signs of reluctance and said, “I think I had better get a lawyer before I talk any more. I am going to get into trouble more than I am in now.” The officer replied simply, “You can’t be in any more trouble than you are in now,” and the questioning session proceeded. A full confession was obtained and, after further warnings, a written version was signed.
 </p>
<p id="b812-5">
  Since petitioner was tried after this Court’s decision in
  <em>
   Escobedo
  </em>
  v.
  <em>
   Illinois,
  </em>
  <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964), but before the decision in
  <em>
   Miranda
  </em>
  v.
  <em>
   Arizona,
  </em>
  <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), only the rule of the former case is directly applicable.
  <em>
   Johnson
  </em>
  v.
  <em>
   New Jersey,
  </em>
  <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719</a></span> (1966). Petitioner argues that his statement about getting a lawyer was sufficient to bring
  <em>
   <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>
  </em>
  into play and that the police should immediately have stopped the questioning and obtained counsel for him. We might agree were
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  applicable to this case, for in
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  this Court held that “[i]f . . . [a suspect] indicates in any manner and at any stage of the process that he wishes to consult with an attorney before speaking there can be no questioning.” 384 U. S., at 444-445. But
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  does not apply to this case. This Court in
  <em>
   Johnson
  </em>
  v.
  <em>
   <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">New Jersey</a></span>
  </em>
  pointedly rejected the contention that the specific commands of
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  should apply to all
  <em>
   post-Escobedo
  </em>
  cases. The Court recognized “[t]he disagreements among other courts concerning the implications of
  <em>
   Escobedo,” Johnson
  </em>
  v.
  <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#734" aria-description="Citation for case: Johnson v. New Jersey"><em>
   New Jersey, supra,
  </em>
  at 734</a></span>, and concluded that the States, although free to apply
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  to
  <em>
   post-Escobedo
  </em>
  cases,
  <em>
   id.,
  </em>
  at 733, were not required to do so. The Oregon Supreme Court, in affirming petitioner’s conviction, concluded that the confession was properly introduced into evidence. Under
  <em>
   <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">Johnson</a></span>,
  </em>
  we would be
  <span citation-index="1" class="star-pagination" label="739"> 
   *739
   </span>
  free to disagree with this conclusion only if we felt compelled to do so by the specific holding of
  <em>
   <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>.
  </em>
</p>
<p id="b813-5">
  We do not believe that
  <em>
   <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>
  </em>
  covers this case. Petitioner's statement about seeing an attorney was neither as clear nor as unambiguous as the request Escobedo made. The police in
  <em>
   <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>
  </em>
  were unmistakably informed of their suspect’s wishes; in fact Escobedo’s attorney was present and repeatedly requested permission to see his client. Here, on the other hand, it is possible that the questioning officer took petitioner’s remark not as a request that the interrogation cease but merely as a passing comment. Petitioner did not pursue the matter, but continued answering questions. In this context, we cannot find the denial of the right to counsel which was found so crucial in
  <em>
   <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>.
  </em>
</p>
<p id="b813-6">
  Petitioner also presses the alternative argument that his confession was involuntary and that it should have been excluded for that reason. The trial judge, after an evidentiary hearing during which the tape recording was played, could not agree with this contention, and our reading of the record does not lead us to a contrary conclusion. Before petitioner made any incriminating statements, he received partial warnings of his constitutional rights; this is, of course, a circumstance quite relevant to a finding of voluntariness.
  <em>
   Davis
  </em>
  v.
  <em>
   North Carolina,
  </em>
  <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#740" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737, 740-741</a></span> (1966). The questioning was of short duration, and petitioner was a mature individual of normal intelligence. The fact that the police misrepresented the statements that Rawls had made is, while relevant, insufficient in our view to make this otherwise voluntary confession inadmissible. These cases must be decided by viewing the “totality of the circumstances,” see,
  <em>
   e. g., Clewis
  </em>
  v.
  <em>
   Texas,
  </em>
  <span class="citation" data-id="107419"><a href="/opinion/107419/clewis-v-texas/#708" aria-description="Citation for case: Clewis v. Texas">386 U. S. 707, 708</a></span> (1967), and on the facts of this case we can find no error in the admission of petitioner’s confession.
 </p>
<p id="b814-4">
<span citation-index="1" class="star-pagination" label="740"> 
   *740
   </span>
  III.
 </p>
<p id="b814-5">
  Petitioner’s final contention can be dismissed rather quickly. He argues that the trial judge erred in permitting some clothing seized from petitioner’s duffel bag to be introduced into evidence. This duffel bag was being used jointly by petitioner and his cousin Rawls and it had been left in Rawls’ home. The police, while arresting Rawls, asked him if they could have his clothing. They were directed to the duffel bag and both Rawls and his mother consented to its search. During this search, the officers came upon petitioner’s clothing and it was seized as well. Since Rawls was a joint user of the bag, he clearly had authority to consent to its search. The officers therefore found evidence against petitioner while in the course of an otherwise lawful search. Under this Court’s past decisions, they were clearly permitted to seize it.
  <em>
   Harris
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U. S. 234</a></span>
  <em>
   (1968); Warden
  </em>
  v.
  <em>
   Hayden,
  </em>
  <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967). Petitioner argues that Rawls only had actual permission to use one compartment of the bag and that he had no authority to consent to a search of the other compartments. We will not, however, engage in such metaphysical subtleties in judging the efficacy of Rawls’ consent. Petitioner, in allowing Rawls to use the bag and in leaving it in his house, must be taken to have assumed the risk that Rawls would allow someone else to look inside. We find no valid search and seizure claim in this case.
 </p>
<p id="b814-6">
  Because we find none of petitioner’s contentions meritorious, we affirm the judgment of the Court of Appeals.
 </p>
<p id="b814-7">
<em>
   Affirmed.
  </em>
</p>
<judges id="b814-8">
  Mr. Chief Justice Warren and Mr. Justice Douglas concur in the result.
 </judges>
<judges id="b814-9">
  Mr. Justice Fortas took no part in the consideration or decision of this case.
 </judges>

<div class="footnotes"><div class="footnote" id="fn*" label="*">
<a class="footnote" href="#fn*_ref">
   *
  </a>
<p id="b809-6">
   A more specific limiting instruction might have been desirable, but none was requested.
  </p>
</div></div></opinion>
```

---
