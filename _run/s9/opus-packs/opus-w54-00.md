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

## GROUP: content/cases/United States v. Montoya de Hernandez.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Montoya de Hernandez"
type: case
citation: "473 U.S. 531 (1985)"
parallel_cite: "105 S. Ct. 3304; 87 L. Ed. 2d 381; 53 U.S.L.W. 5048"
neutral_cite: 1985 U.S. LEXIS 120
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-07-01
docket: 84-755
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-07-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Montoya de Hernandez
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111509/united-states-v-montoya-de-hernandez/"
  cluster_id: 111509
  opinion_id: 9430181
  identity_checked: true
homes:
  - page: "[[Border Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Flores-Montano]]", "[[United States v. Martinez-Fuerte]]", "[[Almeida-Sanchez v. United States]]", "[[Terry v. Ohio]]", "[[United States v. Cortez]]"]
aliases: ["United States v. Rosa Elvira Montoya de Hernandez"]
tags: ["case", "fourth-amendment", "border-searches", "reasonable-suspicion", "alimentary-canal-smuggling", "detention"]
holding: "The prolonged detention of a suspected alimentary-canal (balloon) smuggler at the border is reasonable when customs officers have…"
lake:
  record_id: United States v. Montoya de Hernandez
  status: verified
  projected_at: 2026-07-06
---

# United States v. Montoya de Hernandez

*473 U.S. 531 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Rosa Elvira Montoya de Hernandez arrived at Los Angeles International Airport on a flight from Bogotá, Colombia. Customs inspectors found her travel story implausible — frequent short trips, about $5,000 cash but no checks or credit cards, no hotel reservations, and minimal luggage — and a strip search revealed a firm fullness in her abdomen and two pairs of underpants lined with a paper towel. Suspecting she was a "balloon swallower," inspectors detained her for roughly 16 hours awaiting a monitored bowel movement after she declined an x-ray; a court order eventually authorized an examination that produced 88 cocaine-filled balloons from her alimentary canal. The Ninth Circuit reversed her conviction, requiring a "clear indication" of smuggling.

## Issue
What level of suspicion justifies detaining an incoming international traveler at the border, beyond a routine customs search, on suspicion of alimentary-canal smuggling — and whether the prolonged detention here was reasonable.

## Rule
Reasonable suspicion governs such nonroutine border detentions of persons. "We hold that the detention of a traveler at the border, beyond the scope of a routine customs search and inspection, is justified at its inception if customs agents, considering all the facts surrounding the traveler and her trip, reasonably suspect that the traveler is smuggling contraband in her alimentary canal." — 473 U.S. at 541. ^pin-541

Officials must have a "particularized and objective basis for suspecting the particular person" of such smuggling, not an "inchoate and unparticularized suspicion or 'hunch.'"

The detention may last as long as is reasonably necessary to confirm or dispel the suspicion: "in the presence of articulable suspicion of smuggling in her alimentary canal, the customs officers were not required by the Fourth Amendment to pass respondent and her 88 cocaine-filled balloons into the interior. Her detention for the period of time necessary to either verify or dispel the suspicion was not unreasonable." — *Id.* at 544. ^pin-544

## Application
On these facts the inspectors had reasonable suspicion and the detention was reasonable. Montoya's implausible itinerary, her cash without ordinary financial instruments, the absence of luggage and reservations, the firm abdominal fullness, and Inspector Talamantes's experience apprehending dozens of balloon swallowers on that very flight supplied a particularized, objective basis to suspect alimentary-canal smuggling — far more than a hunch. Because such smuggling gives no external signs and cannot be detected by a frisk or strip search, the officers were not obliged to let her pass into the country; detaining her until her bodily processes could verify or dispel the suspicion was reasonable, and the length and discomfort of the detention "resulted solely from the method by which she chose to" smuggle and her refusal of the x-ray alternative.

## Conclusion
Reasonable suspicion justified the nonroutine border detention, and its duration was reasonable; the Ninth Circuit's reversal of the conviction was itself reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Montoya de Hernandez* sets the reasonable-suspicion standard for nonroutine border *detentions of persons*; [[United States v. Flores-Montano]] later confined that "routine vs. non-routine" analysis to person searches and held it inapplicable to *vehicle* searches at the border. It draws the reasonable-suspicion standard from the [[Terry v. Ohio]] / [[United States v. Cortez]] line.

## Appears on
- [[Border Searches]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Montoya de Hernandez*, 473 U.S. 531 (1985) — https://www.courtlistener.com/opinion/111509/united-states-v-montoya-de-hernandez/ — pinpoints: 541, 544.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4c86ef8248dc319b", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "473 U.S. 531 (1985)", "court": "U.S. Supreme Court", "neutral_cite": "1985 U.S. LEXIS 120", "official_citation_present": true, "parallel_cite": "105 S. Ct. 3304; 87 L. Ed. 2d 381; 53 U.S.L.W. 5048", "title": "United States v. Montoya de Hernandez", "year": "1985"}}
{"assertion_id": "c69758e04cfa1ab5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The prolonged detention of a suspected alimentary-canal (balloon) smuggler at the border is reasonable when customs officers have…", "title": "United States v. Montoya de Hernandez"}}
{"assertion_id": "cd9b3f23a5d0f333", "dimension": "support", "kind": "home_role", "locator": {"home": "Border Searches"}, "payload": {"home": "Border Searches", "role": "Key — Progeny / Refinement", "title": "United States v. Montoya de Hernandez"}}
{"assertion_id": "6528e3c750989296", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1985-07-01", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Montoya de Hernandez", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Montoya de Hernandez", "varies_by_point": "false"}}
{"assertion_id": "8fffd19c808e36d4", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Montoya de Hernandez"}}
```

### lake record — United States v. Montoya de Hernandez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Montoya de Hernandez",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Montoya De Hernandez",
    "case_name_short": "Hernandez",
    "case_name_full": "UNITED STATES v. MONTOYA De HERNANDEZ",
    "input_case_name": "United States v. Montoya de Hernandez",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-07-01",
    "year": 1985,
    "docket": "84-755",
    "cluster_id": 111509,
    "lead_opinion_id": 9430181,
    "sibling_ids": [
      111509,
      9430181,
      9430182,
      9430183
    ],
    "absolute_url": "/opinion/111509/united-states-v-montoya-de-hernandez/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "473 U.S. 531",
      "volume": "473",
      "reporter": "U.S.",
      "page": "531",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 3304",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "3304",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 L. Ed. 2d 381",
        "volume": "87",
        "reporter": "L. Ed. 2d",
        "page": "381",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 5048",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "5048",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 120",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "120",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "473 U.S. 531",
        "volume": "473",
        "reporter": "U.S.",
        "page": "531",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 3304",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "3304",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 L. Ed. 2d 381",
        "volume": "87",
        "reporter": "L. Ed. 2d",
        "page": "381",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 120",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "120",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 5048",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "5048",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "473 U.S. 531",
    "official_selection": {
      "court_class": "scotus",
      "selected": "473 U.S. 531",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-541",
      "page": null,
      "quote": "of smuggling. ## Issue What level of suspicion justifies detaining an incoming international traveler at the border, beyond a routine customs search, on suspicion of alimentary-canal smuggling \u2014 and whether the prolonged detention here was reasonable. ## Rule Reasonable suspicion governs such nonroutine border detentions of persons.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-544",
      "page": null,
      "quote": "The detention may last as long as is reasonably necessary to confirm or dispel the suspicion:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-07-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Montoya de Hernandez",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Banks",
          "cluster_id": 6658146,
          "cite": [
            "434 P.3d 361",
            "364 Or. 332"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Martinez",
          "cluster_id": 4574288,
          "cite": [
            "910 F.3d 1309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Caballero",
          "cluster_id": 7319742,
          "cite": [
            "178 F. Supp. 3d 1008",
            "2016 U.S. Dist. LEXIS 51132",
            "2016 WL 1546731"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Levy",
          "cluster_id": 8442407,
          "cite": [
            "803 F.3d 120",
            "2015 U.S. App. LEXIS 17154",
            "2015 WL 5692332"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cotterman",
          "cluster_id": 213651,
          "cite": [
            "637 F.3d 1068",
            "2011 U.S. App. LEXIS 6483",
            "2011 WL 1137302"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Stefan Irving",
          "cluster_id": 794720,
          "cite": [
            "452 F.3d 110",
            "2006 U.S. App. LEXIS 16077",
            "2006 WL 1735582"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Figg v. Schroeder",
          "cluster_id": 2967701,
          "cite": [
            "312 F.3d 625",
            "2002 WL 31689413"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane1_negative"
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
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
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
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
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
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vernonia School District 47J v. Acton",
          "cluster_id": 117964,
          "cite": [
            "132 L. Ed. 2d 564",
            "115 S. Ct. 2386",
            "515 U.S. 646",
            "1995 U.S. LEXIS 4275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
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
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Indianapolis v. Edmond",
          "cluster_id": 118391,
          "cite": [
            "148 L. Ed. 2d 333",
            "121 S. Ct. 447",
            "531 U.S. 32",
            "2000 U.S. LEXIS 8084",
            "69 U.S.L.W. 4009",
            "14 Fla. L. Weekly Fed. S 9",
            "2000 Colo. J. C.A.R. 6401",
            "2000 Cal. Daily Op. Serv. 9549"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "National Treasury Employees Union v. Von Raab",
          "cluster_id": 112220,
          "cite": [
            "103 L. Ed. 2d 685",
            "109 S. Ct. 1384",
            "489 U.S. 656",
            "1989 U.S. LEXIS 6033",
            "1989 CCH OSHD 28,589",
            "4 I.E.R. Cas. (BNA) 246",
            "57 U.S.L.W. 4338",
            "49 Empl. Prac. Dec. (CCH) 38,792"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County of Allegheny v. American Civil Liberties Union",
          "cluster_id": 112331,
          "cite": [
            "106 L. Ed. 2d 472",
            "109 S. Ct. 3086",
            "492 U.S. 573",
            "1989 U.S. LEXIS 3468",
            "57 U.S.L.W. 5045"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Verdugo-Urquidez",
          "cluster_id": 112382,
          "cite": [
            "108 L. Ed. 2d 222",
            "110 S. Ct. 1056",
            "494 U.S. 259",
            "1990 U.S. LEXIS 1175",
            "1990 WL 16772"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
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
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McCullough",
          "cluster_id": 2594742,
          "cite": [
            "6 P.3d 774",
            "2000 Colo. J. C.A.R. 3950",
            "2000 Colo. LEXIS 817",
            "2000 WL 870824"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Oody",
          "cluster_id": 1740610,
          "cite": [
            "823 S.W.2d 554",
            "1991 Tenn. Crim. App. LEXIS 405"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McGee v. State",
          "cluster_id": 1960022,
          "cite": [
            "105 S.W.3d 609",
            "2003 Tex. Crim. App. LEXIS 75",
            "2003 WL 1918091"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fuller v. M.G. Jewelry",
          "cluster_id": 9003626,
          "cite": [
            "950 F.2d 1437",
            "1991 WL 258850"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gonzalez v. City of Schenectady",
          "cluster_id": 1038554,
          "cite": [
            "728 F.3d 149",
            "2013 U.S. App. LEXIS 17943",
            "2013 WL 4528864"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Manuel Melendez-Garcia",
          "cluster_id": 673526,
          "cite": [
            "28 F.3d 1046",
            "1994 U.S. App. LEXIS 16309",
            "1994 WL 313268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. $191,910.00 in U.S. Currency, Bruce R. Morgan, Claimant-Appellee",
          "cluster_id": 663161,
          "cite": [
            "16 F.3d 1051",
            "94 Daily Journal DAR 2139",
            "94 Cal. Daily Op. Serv. 1214",
            "1994 U.S. App. LEXIS 2681",
            "1994 WL 46744"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rita Ann Cardenas and Shamsideen Abiodun Lawal",
          "cluster_id": 657339,
          "cite": [
            "9 F.3d 1139"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Terry King and Valerie Jean Burdex",
          "cluster_id": 604813,
          "cite": [
            "990 F.2d 1552",
            "1993 U.S. App. LEXIS 6056"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Acosta-Colon",
          "cluster_id": 198134,
          "cite": [
            "157 F.3d 9",
            "1998 U.S. App. LEXIS 24862",
            "1998 WL 671324"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Zapata",
          "cluster_id": 195255,
          "cite": [
            "18 F.3d 971",
            "1994 WL 86216"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Flores-Montano",
          "cluster_id": 134729,
          "cite": [
            "158 L. Ed. 2d 311",
            "124 S. Ct. 1582",
            "541 U.S. 149",
            "2004 U.S. LEXIS 2548",
            "72 U.S.L.W. 4263",
            "17 Fla. L. Weekly Fed. S 207"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stuart Romm",
          "cluster_id": 795139,
          "cite": [
            "455 F.3d 990",
            "2006 U.S. App. LEXIS 18474",
            "2006 WL 2042827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Betty Lester v. City of Chicago, Officer Daniel Leahy, Officer Ernest Cain, and Sergeant John McNulty",
          "cluster_id": 495261,
          "cite": [
            "830 F.2d 706",
            "1987 U.S. App. LEXIS 14017",
            "56 U.S.L.W. 2203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111509 OR 9430181 OR 9430182 OR 9430183) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDM4ODczNjAwMDAwJnM9Mjk2NzcwMSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111509+OR+9430181+OR+9430182+OR+9430183%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(111509 OR 9430181 OR 9430182 OR 9430183)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjImcz04OTQzODQzJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111509+OR+9430181+OR+9430182+OR+9430183%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111509 OR 9430181 OR 9430182 OR 9430183)",
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
    "complete_query": "cites:(111509 OR 9430181 OR 9430182 OR 9430183)",
    "indexed_citing_opinions": 607,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111509,
        "count": 527,
        "count_source": "search"
      },
      {
        "opinion_id": 9430181,
        "count": 94,
        "count_source": "search"
      },
      {
        "opinion_id": 9430182,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430183,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 983,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-montoya-de-hernandez.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgwNDQyMTUmcz05MzI5MDUzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111509+OR+9430181+OR+9430182+OR+9430183%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111509,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 94479,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 108841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110501,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 111378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 111380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 111382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 272334,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 283495,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 285139,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 311366,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 402585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 408227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 419999,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 421712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 421842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 427199,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 428603,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 429241,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 432317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 432318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 432319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 432320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 432321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 432322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 433838,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 436008,
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
    "date_created": "2026-07-06T01:47:04Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:47:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:47:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:51:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:47:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Montoya de Hernandez

```
<opinion type="majority">
<author id="b570-10">Justice Rehnquist</author>
<p id="A3j">delivered the opinion of the Court.</p>
<p id="b570-11">Respondent Rosa Elvira Montoya de Hernandez was detained by customs officials upon her arrival at the Los Ange-les Airport on a flight from Bogota, Colombia. She was found to be smuggling 88 cocaine-filled balloons in her alimen<page-number citation-index="1" label="533">*533</page-number>tary canal, and was convicted after a bench trial of various federal narcotics offenses. A divided panel of the United States Court of Appeals for the Ninth Circuit reversed her convictions, holding that her detention violated the Fourth Amendment to the United States Constitution because the customs inspectors did not have a “clear indication” of alimentary canal smuggling at the time she was detained. <span class="citation" data-id="9472040"><a href="/opinion/433838/united-states-v-rosa-elvira-montoya-de-hernandez/" aria-description="Citation for case: United States v. Rosa Elvira Montoya De Hernandez">731 F. 2d 1369</a></span> (1984). Because of a conflict in the decisions of the Courts of Appeals on this question and the importance of its resolution to the enforcement of customs laws, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./469/1188/">469 U. S. 1188</a></span>. We now reverse.</p>
<p id="b571-5">Respondent arrived at Los Angeles International Airport shortly after midnight, March 5, 1983, on Avianca Flight 080, a direct 10-hour flight from Bogota, Colombia. Her visa was in order so she was passed through Immigration and proceeded to the customs desk. At the customs desk she encountered Customs Inspector Talamantes, who reviewed her documents and noticed from her passport that she had made at least eight recent trips to either Miami or Los Angeles. Talamantes referred respondent to a secondary customs desk for further questioning. At this desk Talamantes and another inspector asked respondent general questions concerning herself and the purpose of her trip. Respondent revealed that she spoke no English and had no family or friends in the United States. She explained in Spanish that she had come to the United States to purchase goods for her husband’s store in Bogota. The customs inspectors recognized Bogota as a “source city” for narcotics. Respondent possessed $5,000 in cash, mostly $50 bills, but had no billfold. She indicated to the inspectors that she had no appointments with merchandise vendors, but planned to ride around Los Angeles in taxicabs visiting retail stores such as J. C. Penney and K-Mart in order to buy goods for her husband’s store with the $5,000.</p>
<p id="b571-6">Respondent admitted that she had no hotel reservations, but stated that she planned to stay at a Holiday Inn. Respondent could not recall how her airline ticket was pur<page-number citation-index="1" label="534">*534</page-number>chased. When the inspectors opened respondent’s one small valise they found about four changes of “cold weather” clothing. Respondent had no shoes other than the high-heeled pair she was wearing. Although respondent possessed no checks, waybills, credit cards, or letters of credit, she did produce a Colombian business card and a number of old receipts, waybills, and fabric swatches displayed in a photo album.</p>
<p id="b572-5">At this point Talamantes and the other inspector suspected that respondent was a “balloon swallower,” one who attempts to smuggle narcotics into this country hidden in her alimentary canal. Over the years Inspector Talamantes had apprehended dozens of alimentary canal smugglers arriving on Avianca Flight 080. See App. 42; <em>United States </em>v. <em>Mendez-Jimenez, </em><span class="citation" data-id="419999"><a href="/opinion/419999/united-states-v-luis-alfonso-mendez-jimenez/#1301" aria-description="Citation for case: United States v. Luis Alfonso Mendez-Jimenez">709 F. 2d 1300, 1301</a></span> (CA9 1983).</p>
<p id="b572-6">The inspectors requested a female customs inspector to take respondent to a private area and conduct a patdown and strip search. During the search the female inspector felt respondent’s abdomen area and noticed a firm fullness, as if respondent were wearing a girdle. The search revealed no contraband, but the inspector noticed that respondent was wearing two pairs of elastic underpants with a paper towel lining the crotch area.</p>
<p id="b572-7">When respondent returned to the customs area and the female inspector reported her discoveries, the inspector in charge told respondent that he suspected she was smuggling drugs in her alimentary canal. Respondent agreed to the inspector’s request that she be x-rayed at a hospital but in answer to the inspector’s query stated that she was pregnant. She agreed to a pregnancy test before the x ray. Respondent withdrew the consent for an x ray when she learned that she would have to be handcuffed en route to the hospital. The inspector then gave respondent the option of returning to Colombia on the next available flight, agreeing to an x ray, or remaining in detention until she produced a monitored bowel movement that would confirm or rebut the inspectors’ <page-number citation-index="1" label="535">*535</page-number>suspicions. Respondent chose the first option and was placed in a customs office under observation. She was told that if she went to the toilet she would have to use a wastebasket in the women’s restroom, in order that female customs inspectors could inspect her stool for balloons or capsules carrying narcotics. The inspectors refused respondent’s request to place a telephone call.</p>
<p id="b573-5">Respondent sat in the customs office, under observation, for the remainder of the night. During the night customs officials attempted to place respondent on a Mexican airline that was flying to Bogota via Mexico City in the morning. The airline refused to transport respondent because she lacked a Mexican visa necessary to land in Mexico City. • Respondent was not permitted to leave, and was informed that she would be detained until she agreed to an x ray or her bowels moved. She remained detained in the customs office under observation, for most of the time curled up in a chair leaning to one side. She refused all offers of food and drink, and refused to use the toilet facilities. The Court of Appeals noted that she exhibited symptoms of discomfort consistent with “heroic efforts to resist the usual calls of nature.” <span class="citation" data-id="9472040"><a href="/opinion/433838/united-states-v-rosa-elvira-montoya-de-hernandez/#1371" aria-description="Citation for case: United States v. Rosa Elvira Montoya De Hernandez">731 F. 2d, at 1371</a></span>.</p>
<p id="b573-6">At the shift change at 4:00 o’clock the next afternoon, almost 16 hours after her flight had landed, respondent still had not defecated or urinated or partaken of food or drink. At that time customs officials sought a court order authorizing a pregnancy test, an x ray, and a rectal examination. The Federal Magistrate issued an order just before midnight that evening, which authorized a rectal examination and involuntary x ray, provided that the physician in charge considered respondent’s claim of pregnancy. Respondent was taken to a hospital and given a pregnancy test, which later turned out to be negative. Before the results of the pregnancy test were known, a physician conducted a rectal examination and removed from respondent’s rectum a balloon containing a foreign substance. Respondent was then placed <page-number citation-index="1" label="536">*536</page-number>formally under arrest. By 4:10 a. m. respondent had passed 6 similar balloons; over the next four days she passed 88 balloons containing a total of 528 grams of 80% pure cocaine hydrochloride.</p>
<p id="b574-5">After a suppression hearing the District Court admitted the cocaine in evidence against respondent. She was convicted of possession of cocaine with intent to distribute, <span class="citation no-link">21 U. S. C. § 841</span>(a)(1), and unlawful importation of cocaine, <span class="citation no-link">21 U. S. C. §§ 952</span>(a), 960(a).</p>
<p id="b574-6">A divided panel of the United States Court of Appeals for the Ninth Circuit reversed respondent’s convictions. The court noted that customs inspectors had a “justifiably high level of official skepticism” about respondent’s good motives, but the inspectors decided to let nature take its course rather than seek an immediate magistrate’s warrant for an x ray. <span class="citation" data-id="9472040"><a href="/opinion/433838/united-states-v-rosa-elvira-montoya-de-hernandez/#1372" aria-description="Citation for case: United States v. Rosa Elvira Montoya De Hernandez">731 F. 2d, at 1372</a></span>. Such a magistrate’s warrant required a “clear indication” or “plain suggestion” that the traveler was an alimentary canal smuggler under previous decisions of the Court of Appeals. See <em>United States </em>v. <em>Quintero-Castro, </em><span class="citation" data-id="8916798"><a href="/opinion/8927001/united-states-v-quintero-castro/" aria-description="Citation for case: United States v. Quintero-Castro">705 F. 2d 1099</a></span> (CA9 1983); <em>United States </em>v. <em>Mendez-Jimenez, </em><span class="citation" data-id="419999"><a href="/opinion/419999/united-states-v-luis-alfonso-mendez-jimenez/#1302" aria-description="Citation for case: United States v. Luis Alfonso Mendez-Jimenez">709 F. 2d 1300, 1302</a></span> (CA9 1983); but cf. <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#370" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 370, n. 5</a></span> (1976). The court applied this required level of suspicion to respondent’s case. The court questioned the “humanity” of the inspectors’ decision to hold respondent until her bowels moved, knowing that she would suffer “many hours of humiliating discomfort” if she chose not to submit to the x-ray examination. The court concluded that under a “clear indication” standard “the evidence available to the customs officers when they decided to hold [respondent] for continued observation was insufficient to support the 16-hour detention.” <span class="citation" data-id="9472040"><a href="/opinion/433838/united-states-v-rosa-elvira-montoya-de-hernandez/#1373" aria-description="Citation for case: United States v. Rosa Elvira Montoya De Hernandez">731 F. 2d, at 1373</a></span>.</p>
<p id="b574-7">The Government contends that the customs inspectors reasonably suspected that respondent was an alimentary canal smuggler, and this suspicion was sufficient to justify the detention. In support of the judgment below respondent <page-number citation-index="1" label="537">*537</page-number>argues, <em>inter alia, </em>that reasonable suspicion would not support respondent’s detention, and in any event the inspectors did not reasonably suspect that respondent was carrying narcotics internally.</p>
<p id="b575-5">The Fourth Amendment commands that searches and seizures be reasonable. What is reasonable depends upon all of the circumstances surrounding the search or seizure and the nature of the search or seizure itself. <em>New Jersey </em>v. T. <em>L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#337" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 337-342</a></span> (1985). The permissibility of a particular law enforcement practice is judged by “balancing its intrusion on the individual’s Fourth Amendment interests against its promotion of legitimate governmental interests.” <em>United States </em>v. <em>Villamonte-Marquez, </em><span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/#588" aria-description="Citation for case: United States v. Villamonte-Marquez">462 U. S. 579, 588</a></span> (1983); <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979); <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967).</p>
<p id="b575-7">Here the seizure of respondent took place at the international border. Since the founding of our Republic, Congress has granted the Executive plenary authority to conduct routine searches and seizures at the border, without probable cause or a warrant, in order to regulate the collection of duties and to prevent the introduction of contraband into this country. See <em>United States </em>v. <em>Ramsey, </em><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#616" aria-description="Citation for case: United States v. Ramsey">431 U. S. 606, 616-617</a></span> (1977), citing Act of July 31, 1789, ch. 5, <span class="citation no-link">1 Stat. 29</span>. This Court has long recognized Congress’ power to police entrants at the border. See <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#623" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 623</a></span> (1886). As we stated recently:</p>
<blockquote id="b575-9">“‘Import restrictions and searches of persons or packages at the national border rest on different considerations and different rules of constitutional law from domestic regulations. The Constitution gives Congress broad comprehensive powers “[t]o regulate Commerce with foreign Nations,” Art. I, §8, cl. 3. Historically such broad powers have been necessary to prevent smuggling and to prevent prohibited articles from <page-number citation-index="1" label="538">*538</page-number>entry.’” <span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#618" aria-description="Citation for case: United States v. Ramsey"><em>Ramsey, supra, </em>at 618-619</a></span>, quoting <em>United States </em>v. <em>12 200-Ft. Reels of Film, </em><span class="citation" data-id="9425385"><a href="/opinion/108841/united-states-v-12-200-ft-reels-of-super-8mm-film/#125" aria-description="Citation for case: United States v. 12 200-Ft. Reels of Super 8MM. Film">413 U. S. 123, 125</a></span> (1973).</blockquote>
<p id="b576-5">Consistently, therefore, with Congress’ power to protect the Nation by stopping and examining persons entering this country, the Fourth Amendment’s balance of reasonableness is qualitatively different at the international border than in the interior. Routine searches of the persons and effects of entrants are not subject to any requirement of reasonable suspicion, probable cause, or warrant,<footnotemark>1</footnotemark> and first-class mail may be opened without a warrant on less than probable cause, <em><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">Ramsey, supra.</a></span> </em>Automotive travelers may be stopped at fixed checkpoints near the border -without individualized suspicion even if the stop is based largely on ethnicity, <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#562" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 562-563</a></span> (1976), and boats on inland waters with ready access to the sea may be hailed and boarded with no suspicion whatever. <em>United States </em>v. <em><span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/" aria-description="Citation for case: United States v. Villamonte-Marquez">Villamonte-Marquez, supra.</a></span></em></p>
<p id="b576-6">These cases reflect longstanding concern for the protection of the integrity of the border. This concern is, if anything, heightened by the veritable national crisis in law enforcement caused by smuggling of illicit narcotics, see <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#561" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 561</a></span> (1980) (Powell, J., concurring), and in particular by the increasing utilization of alimentary canal smuggling. This desperate practice appears to be a relatively recent addition to the smugglers’ repertoire of deceptive practices, and it also appears to be exceedingly dif<page-number citation-index="1" label="539">*539</page-number>ficult to detect.<footnotemark>2</footnotemark> Congress had recognized these difficulties. Title <span class="citation no-link">19 U. S. C. § 1582</span> provides that “all persons coming into the United States from foreign countries shall be liable to detention and search authorized . . . [by customs regulations].” Customs agents may “stop, search, and examine” any “vehicle, beast or person” upon which an officer suspects there is contraband or “merchandise which is subject to duty.” §482; see also §§ 1467, 1481; <span class="citation no-link">19 CFR §§ 162.6</span>, 162.7 (1984).</p>
<p id="b577-5">Balanced against the sovereign’s interests at the border are the Fourth Amendment rights of respondent. Having presented herself at the border for admission, and having subjected herself to the criminal enforcement powers of the Federal Government, <span class="citation no-link">19 U. S. C. § 482</span>, respondent was entitled to be free from unreasonable search and seizure. But not only is the expectation of privacy less at the border than in the interior, see, <em>e. g., Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#154" aria-description="Citation for case: Carroll v. United States">267 U. S. <page-number citation-index="1" label="540">*540</page-number>132, 154</a></span> (1925); cf. <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#515" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 515</a></span> (1983) (Blackmun, J., dissenting), the Fourth Amendment balance between the interests of the Government and the privacy right of the individual is also struck much more favorably to the Government at the border. <em>Supra, </em>at 538.</p>
<p id="b578-4">We have not previously decided what level of suspicion would justify a seizure of an incoming traveler for purposes other than a routine border search. Cf. <em>Ramsey, </em><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#618" aria-description="Citation for case: United States v. Ramsey">431 U. S., at 618, n. 13</a></span>. The Court of Appeals held that the initial detention of respondent was permissible only if the inspectors possessed a “clear indication” of alimentary canal smuggling. <span class="citation" data-id="9472040"><a href="/opinion/433838/united-states-v-rosa-elvira-montoya-de-hernandez/#1372" aria-description="Citation for case: United States v. Rosa Elvira Montoya De Hernandez">731 F. 2d, at 1372</a></span>, citing <em>United States </em>v. <em>Quintero-Castro, </em><span class="citation" data-id="8916798"><a href="/opinion/8927001/united-states-v-quintero-castro/" aria-description="Citation for case: United States v. Quintero-Castro">705 F. 2d 1099</a></span> (CA9 1983); cf. <em>United States </em>v. <em>Mendez-Jimenez, </em><span class="citation" data-id="419999"><a href="/opinion/419999/united-states-v-luis-alfonso-mendez-jimenez/" aria-description="Citation for case: United States v. Luis Alfonso Mendez-Jimenez">709 F. 2d 1300</a></span> (CA9 1983). This “clear indication” language comes from our opinion in <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966), but we think that the Court of Appeals misapprehended the significance of that phrase in the context in which it was used in Schmerber.<footnotemark>3</footnotemark> The Court of Appeals viewed “clear indication” as an intermediate standard between “reasonable suspicion” and “probable cause.” See <span class="citation" data-id="419999"><a href="/opinion/419999/united-states-v-luis-alfonso-mendez-jimenez/#1302" aria-description="Citation for case: United States v. Luis Alfonso Mendez-Jimenez"><em>Mendez-Jimenez, supra, </em>at 1302</a></span>. But we think that the words in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>were used to indicate the necessity for particularized suspicion that the evidence sought might be found within the body of the individual, rather than as enunciating still a third Fourth Amendment threshold between “reasonable suspicion” and “probable cause.”</p>
<p id="b578-5">No other court, including this one, has ever adopted <em>Schmerber1 </em>s “clear indication” language as a Fourth Amendment standard. See, <em>e. g., Winston </em>v. <em>Lee, </em><span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/#759" aria-description="Citation for case: Winston v. Lee">470 U. S. 753, <page-number citation-index="1" label="541">*541</page-number>759-763</a></span> (1985) (surgical removal of bullet for evidence). Indeed, another Court of Appeals, faced with facts almost identical to this case, has adopted a less strict standard based upon reasonable suspicion. See <em>United States </em>v. <em>Mosquera-Ramirez, </em><span class="citation" data-id="9471932"><a href="/opinion/432318/united-states-v-luis-fernando-mosquera-ramirez/#1355" aria-description="Citation for case: United States v. Luis Fernando Mosquera-Ramirez">729 F. 2d 1352, 1355</a></span> (CA11 1984). We do not think that the Fourth Amendment’s emphasis upon reasonableness is consistent with the creation of a third verbal standard in addition to “reasonable suspicion” and “probable cause”; we are dealing with a constitutional requirement of reasonableness, not <em>mens rea, </em>see <em>United States </em>v. <em>Bailey, </em><span class="citation" data-id="9427750"><a href="/opinion/110175/united-states-v-bailey/#403" aria-description="Citation for case: United States v. Bailey">444 U. S. 394, 403-406</a></span> (1980), and subtle verbal gradations may obscure rather than elucidate the meaning of the provision in question.</p>
<p id="b579-5">We hold that the detention of a traveler at the border, beyond the scope of a routine customs search and inspection, is justified at its inception if customs agents, considering all the facts surrounding the traveler and her trip, reasonably suspect that the traveler is smuggling contraband in her alimentary canal.<footnotemark>4</footnotemark></p>
<p id="b579-6">The “reasonable suspicion” standard has been applied in a number of contexts and effects a needed balance between private and public interests when law enforcement officials must make a limited intrusion on less than probable cause. It thus fits well into the situations involving alimentary canal smuggling at the border: this type of smuggling gives no external signs and inspectors will rarely possess probable cause to arrest or search, yet governmental interests in stopping smuggling at the border are high indeed. Under this standard officials at the border must have a “particularized and objective basis for suspecting the particular person” of ali<page-number citation-index="1" label="542">*542</page-number>mentary canal smuggling. <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 417</a></span> (1981); <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#418" aria-description="Citation for case: United States v. Cortez"><em>id., </em>at 418</a></span>, citing <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 21, n. 18</a></span> (1968).</p>
<p id="b580-5">The facts, and their rational inferences, known to customs inspectors in this case clearly supported a reasonable suspicion that respondent was an alimentary canal smuggler. We need not belabor the facts, including respondent’s implausible story, that supported this suspicion, see <em>supra, </em>at 533-536. The trained customs inspectors had encountered many alimentary canal smugglers and certainly had more than an “inchoate and unparticularized suspicion or ‘hunch,’” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><em>Terry, supra, </em>at 27</a></span>, that respondent was smuggling narcotics in her alimentary canal. The inspectors’ suspicion was a “‘common-sense conclusio[n] about human behavior’ upon which ‘practical people,’ — including government officials, are entitled to rely.” <em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#346" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 346</a></span>, citing <em>United States </em>v. <em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">Cortez, supra.</a></span></em></p>
<p id="b580-6">The final issue in this case is whether the detention of respondent was reasonably related in scope to the circumstances which justified it initially. In this regard we have cautioned that courts should not indulge in “unrealistic second-guessing,” <em>United States </em>v. <em>Sharpe, </em><span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#686" aria-description="Citation for case: United States v. Sharpe">470 U. S. 675, 686</a></span> (1985), and we have noted that “creative judge[s], engaged in <em>post hoc </em>evaluations of police conduct can almost always imagine some alternative means by which the objectives of the police might have been accomplished.” <span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#686" aria-description="Citation for case: United States v. Sharpe"><em>Id., </em>at 686-687</a></span>. But “[t]he fact that the protection of the public might, in the abstract, have been accomplished by ‘less intrusive’ means does not, in itself, render the search unreasonable.” <span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#687" aria-description="Citation for case: United States v. Sharpe"><em>Id., </em>at 687</a></span>, citing <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#447" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 447</a></span> (1973). Authorities must be allowed “to graduate their response to the demands of any particular situation.” <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place">462 U. S. 696, 709, n. 10</a></span> (1983). Here, respondent was detained incommunicado for almost 16 hours before inspectors sought a warrant; the warrant then took a number of hours to procure, through no apparent fault <page-number citation-index="1" label="543">*543</page-number>of the inspectors. This length of time undoubtedly exceeds any other detention we have approved under reasonable suspicion. But we have also consistently rejected hard-and-fast time limits, <em><span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/" aria-description="Citation for case: United States v. Sharpe">Sharpe, supra;</a></span> Place, supra, </em>at 709, n. 10. Instead, “common sense and ordinary human experience must govern over rigid criteria.” <span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#685" aria-description="Citation for case: United States v. Sharpe"><em>Sharpe, supra, </em>at 685</a></span>.</p>
<p id="b581-5">The rudimentary knowledge of the human body which judges possess in common with the rest of humankind tells us that alimentary canal smuggling cannot be detected in the amount of time in which other illegal activity may be investigated through brief Terry-type stops. It presents few, if any external signs; a quick frisk will not do, nor will even a strip search. In the case of respondent the inspectors had available, as an alternative to simply awaiting her bowel movement, an x ray. They offered her the alternative of submitting herself to that procedure. But when she refused that alternative, the customs inspectors were left with only two practical alternatives: detain her for such time as necessary to confirm their suspicions, a detention which would last much longer than the typical <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop, or turn her loose into the interior carrying the reasonably suspected contraband drugs.</p>
<p id="b581-6">The inspectors in this case followed this former procedure. They no doubt expected that respondent, having recently disembarked from a 10-hour direct flight with a full and stiff abdomen, would produce a bowel movement without extended delay. - But her visible efforts to resist the call of nature, which the court below labeled “heroic,” disappointed this expectation and in turn caused her humiliation and discomfort. Our prior cases have refused to charge police with delays in investigatory detention attributable to the suspect’s evasive actions, see <em>Sharpe, </em><span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#687" aria-description="Citation for case: United States v. Sharpe">470 U. S., at 687-688</a></span>; <span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#697" aria-description="Citation for case: United States v. Sharpe"><em>id., </em>at 697</a></span> (Marshall, J., concurring in judgment), and that principle applies here as well. Respondent alone was responsible for much of the duration and discomfort of the seizure.</p>
<p id="b582-4"><page-number citation-index="1" label="544">*544</page-number>Under these circumstances, we conclude that the detention in this case was not unreasonably long. It occurred at the international border, where the Fourth Amendment balance of interests leans heavily to the Government. At the border, customs officials have more than merely an investigative law enforcement role. They are also charged, along with immigration officials, with protecting this Nation from entrants who may bring anything harmful into this country, whether that be communicable diseases, narcotics, or explosives. See <span class="citation no-link">8 U. S. C. §§ 1182</span>(a)(23), 1182(a)(6), 1222; <span class="citation no-link">19 CFR §§ 162.4-162.7</span> (1984). See also <span class="citation no-link">19 U. S. C. §482</span>; <span class="citation no-link">8 U. S. C. § 1103</span>(a). In this regard the detention of a suspected alimentary canal smuggler at the border is analogous to the detention of a suspected tuberculosis carrier at the border: both are detained until their bodily processes dispel the suspicion that they will introduce a harmful agent into this country. Cf. <span class="citation no-link">8 U. S. C. § 1222</span>; 42 CFR pt. 34 (1984); <span class="citation no-link">19 U. S. C. §§482</span>, 1582.</p>
<p id="b582-5">Respondent’s detention was long, uncomfortable, indeed, humiliating; but both its length and its discomfort resulted solely from the method by which she chose to smuggle illicit drugs into this country. In <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972), another Terry-stop case, we said that “[t]he Fourth Amendment does not require a policeman who lacks the precise level of information necessary for probable cause to arrest to simply shrug his shoulders and allow a crime to occur or a criminal to escape.” <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#145" aria-description="Citation for case: Adams v. Williams"><em>Id., </em>at 145</a></span>. Here, by analogy, in the presence of articulable suspicion of smuggling in her alimentary canal, the customs officers were not required by the Fourth Amendment to pass respondent and her 88 cocaine-filled balloons into the interior. Her detention for the period of time necessary to either verify or dispel the suspicion was not unreasonable. The judgment of the Court of Appeals is therefore</p>
<p id="b582-6">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b576-7"> See <em>United States </em>v. <em>Ramsey, </em><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#616" aria-description="Citation for case: United States v. Ramsey">431 U. S., at 616-619</a></span>; <em>Almeida-Sanchez </em>v. <em>United States, </em><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#272" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 272-273</a></span> (1973); <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#288" aria-description="Citation for case: Almeida-Sanchez v. United States"><em>id., </em>at 288</a></span> (White, J., dissenting). As the Court stated in <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#154" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 154</a></span> (1925):</p>
<blockquote id="b576-8">“Travellers may be so stopped in crossing an international boundary because of national self protection reasonably requiring one entering the country to identify himself as entitled to come in and his belongings as effects which may be lawfully brought in.”</blockquote>
</footnote>
<footnote label="2">
<p id="b577-6"> See <em>United States </em>v. <em>DeMontoya, </em><span class="citation" data-id="9471940"><a href="/opinion/432322/united-states-v-celina-nohemy-giraldo-de-montoya/" aria-description="Citation for case: United States v. Celina Nohemy Giraldo De Montoya">729 F. 2d 1369</a></span> (CA11 1984) (required surgery; swallowed 100 cocaine-filled condoms); <em>United States </em>v. <em>Pino, </em><span class="citation" data-id="9471934"><a href="/opinion/432319/united-states-v-gabriel-antonio-pino/" aria-description="Citation for case: United States v. Gabriel Antonio Pino">729 F. 2d 1357</a></span> (CA11 1984) (required surgery; 120 cocaine-filled pellets); <em>United States </em>v. <em>Mejia, </em><span class="citation" data-id="427199"><a href="/opinion/427199/united-states-v-german-mejia/" aria-description="Citation for case: United States v. German Mejia">720 F. 2d 1378</a></span> (CA5 1983) (75 balloons); <em>United States </em>v. <em>Couch, </em><span class="citation" data-id="408227"><a href="/opinion/408227/united-states-v-joseph-mark-couch/#605" aria-description="Citation for case: United States v. Joseph Mark Couch">688 F. 2d 599, 605</a></span> (CA9 1982) (36 capsules); <em>United States </em>v. <em>Quintero-Castro, </em><span class="citation" data-id="8916798"><a href="/opinion/8927001/united-states-v-quintero-castro/" aria-description="Citation for case: United States v. Quintero-Castro">705 F. 2d 1099</a></span> (CA9 1983) (120 balloons); <em>United States </em>v. <em>Saldarriaga-Marin, </em><span class="citation" data-id="436008"><a href="/opinion/436008/united-states-v-gloria-saldarriaga-marin-marina-hoyos-gomez-del-soccorro/" aria-description="Citation for case: United States v. Gloria Saldarriaga-Marin, Marina Hoyos...">734 F. 2d 1425</a></span> (CA11 1984); <em>United States </em>v. <em>Vega-Barvo, </em><span class="citation" data-id="9471930"><a href="/opinion/432317/united-states-v-maria-vega-barvo/" aria-description="Citation for case: United States v. Maria Vega-Barvo">729 F. 2d 1341</a></span> (CA11 1984) (135 condoms); <em>United States </em>v. <em>Mendez-Jimenez, </em><span class="citation" data-id="419999"><a href="/opinion/419999/united-states-v-luis-alfonso-mendez-jimenez/" aria-description="Citation for case: United States v. Luis Alfonso Mendez-Jimenez">709 F. 2d 1300</a></span> (CA9 1983) (102 balloons); <em>United States </em>v. <em>Mosquera-Ramirez, </em><span class="citation" data-id="9471932"><a href="/opinion/432318/united-states-v-luis-fernando-mosquera-ramirez/" aria-description="Citation for case: United States v. Luis Fernando Mosquera-Ramirez">729 F. 2d 1352</a></span> (CA11 1984) (95 condoms); <em>United States </em>v. <em>Castrillon, </em><span class="citation" data-id="424734"><a href="/opinion/424734/united-states-v-oscar-alfonso-castrillon/" aria-description="Citation for case: United States v. Oscar Alfonso Castrillon">716 F. 2d 1279</a></span> (CA9 1983) (83 balloons); <em>United States </em>v. <em>Castaneda-Castaneda, </em><span class="citation" data-id="9471936"><a href="/opinion/432320/united-states-v-jose-jaime-castaneda-castaneda-and-betulia-jara-de/" aria-description="Citation for case: United States v. Jose Jaime Castaneda-Castaneda and...">729 F. 2d 1360</a></span> (CA11 1984) (2 smugglers; 201 balloons); <em>United States </em>v. <em>Caicedo-Guamizo, </em><span class="citation" data-id="429241"><a href="/opinion/429241/united-states-v-jose-orlando-caicedo-guarnizo/" aria-description="Citation for case: United States v. Jose Orlando Caicedo-Guarnizo">723 F. 2d 1420</a></span> (CA9 1984) (85 balloons); <em>United States </em>v. <em>Henao-Castano, </em><span class="citation" data-id="9471938"><a href="/opinion/432321/united-states-v-rodrigo-henao-castano/" aria-description="Citation for case: United States v. Rodrigo Henao-Castano">729 F. 2d 1364</a></span> (CA11 1984) (85 condoms); <em>United States </em>v. <em>Ek, </em><span class="citation" data-id="9469126"><a href="/opinion/402585/united-states-v-robert-karl-ek/" aria-description="Citation for case: United States v. Robert Karl Ek">676 F. 2d 379</a></span> (CA9 1982) (30 capsules); <em>United States </em>v. <em>Padilla, </em><span class="citation" data-id="8919792"><a href="/opinion/8929700/united-states-v-padilla/" aria-description="Citation for case: United States v. Padilla">729 F. 2d 1367</a></span> (CA11 1984) (115 condoms); <em>United States </em>v. <em>Gomez-Diaz, </em><span class="citation" data-id="421842"><a href="/opinion/421842/united-states-v-jamie-alberto-gomez-diaz/" aria-description="Citation for case: United States v. Jamie Alberto Gomez-Diaz">712 F. 2d 949</a></span> (CA5 1983) (69 balloons); <em>United States </em>v. <em>D’Allerman, </em><span class="citation" data-id="421712"><a href="/opinion/421712/united-states-v-constanza-dallerman-aka-reyna-maria-murcia/" aria-description="Citation for case: United States v. Constanza D&#x27;allerman, A/K/A Reyna Maria...">712 F. 2d 100</a></span> (CA5 1983) (80 balloons); <em>United States </em>v. <em>Contento-Pachon, </em><span class="citation" data-id="9471547"><a href="/opinion/428603/united-states-v-juan-manuel-contento-pachon/" aria-description="Citation for case: United States v. Juan Manuel Contento-Pachon">723 F. 2d 691</a></span> (CA9 1984) (129 balloons).</p>
</footnote>
<footnote label="3">
<p id="b578-6"> In that ease we stated:</p>
<blockquote id="b578-7">“The interests in human dignity and privacy which the Fourth Amendment protects forbid any such intrusion [beyond the body’s surface] on the mere chance that desired evidence might be obtained. In the absence of a clear indication that in fact such evidence will be found, these fundamental human interests require law officers to suffer the risk that such evidence may disappear unless there is an immediate search.” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#769" aria-description="Citation for case: Schmerber v. California">384 U. S., at 769-770</a></span>.</blockquote>
</footnote>
<footnote label="4">
<p id="b579-7"> It is also important to note what we do <em>not </em>hold. Because the issues are not presented today we suggest no view on what level of suspicion, if any, is required for nonroutine border searches such as strip, body-cavity, or involuntary x-ray searches. Both parties would have us decide the issue of whether aliens possess lesser Fourth Amendment rights at the border; that question was not raised in either court below and we do not consider it today.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Osage.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Osage"
type: case
citation: "235 F.3d 518 (2000)"
parallel_cite: 2000 Colo. J. C.A.R. 6671
neutral_cite: "2000 U.S. App. LEXIS 32020; 2000 WL 1842404"
court: "U.S. Court of Appeals, 10th Circuit"
court_level: coa
circuit: 10th
year: 2000
date_decided: 2000-12-15
docket: ""
authority_weight: "Binding in-circuit — 10th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2000-12-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Osage
  varies_by_point: false
  scope_note: "Good law. Applies and cabins Florida v. Jimeno: general consent does not authorize destroying a container."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/160502/united-states-v-osage/"
  cluster_id: 160502
  opinion_id: 160502
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Limiting"
related: ["[[Florida v. Jimeno]]", "[[Schneckloth v. Bustamonte]]", "[[Georgia v. Randolph]]"]
aliases: ["United States v. David Blake Osage", "United States v. Osage (10th Cir. 2000)"]
tags: ["case", "fourth-amendment", "consent-searches", "scope-of-consent", "containers", "tenth-circuit"]
holding: "General consent to a search does not authorize an officer to destroy a container: before an officer may actually destroy or render completely useless a container otherwise within the scope of a permissive search, the officer must obtain explicit authorization or have some other lawful basis to proceed."
lake:
  record_id: United States v. Osage
  status: verified
  projected_at: 2026-07-09
---

# United States v. Osage

*235 F.3d 518 (10th Cir. 2000)* · U.S. Court of Appeals, 10th Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
On an Amtrak train passing through Albuquerque, Officer Salazar asked David Blake Osage for permission to search his luggage; Osage answered "yeah, I guess," nodded, and gestured toward a black bag. Inside the bag the officer found four 28-ounce cans labeled "tamales in gravy." Noticing that one can's label appeared re-glued and that the can felt and sounded like it held salt rather than tamales in liquid, the officer used a Leatherman tool to cut the can open, discovering methamphetamine inside. Osage was charged with possession with intent to distribute methamphetamine (21 U.S.C. § 841); the district court denied suppression, reasoning that Osage's consent was voluntary and that he never limited its scope or objected as the can was opened. Osage pleaded guilty, reserving his right to appeal the suppression ruling.

## Issue
Whether a suspect's general consent to search his luggage authorized the officer to cut open — and thereby destroy — a sealed can found inside.

## Rule
The scope of a consent search is bounded by the consent given, "measured by objective reasonableness: 'what would the typical reasonable person have understood by the exchange between the officer and the suspect?'" — 235 F.3d at 520 (quoting *Florida v. Jimeno*, 500 U.S. 248, 251 (1991)). ^pin-520

General consent to search an area reaches containers within it that could hold contraband — but it does not reach destroying them: "We acknowledge that the Supreme Court and this court have previously stated that a general consent to search a particular area is reasonably understood to extend to a search of containers within that area that could contain contraband . . . . However, we do not read that authority to permit the destruction of such containers." — *Id.* at 521. ^pin-521

The court therefore held: "before an officer may actually destroy or render completely useless a container which would otherwise be within the scope of a permissive search, the officer must obtain explicit authorization, or have some other, lawful, basis upon which to proceed." — [235 F.3d at 522](https://www.courtlistener.com/opinion/160502/united-states-v-osage/#:~:text=before%20an%20officer%20may%20actually). ^pin-522

## Application
Assuming Osage's consent was valid, opening the sealed can exceeded the scope of that consent because doing so destroyed the can — "rendering it useless and incapable of performing its designated function," which the court found "more like breaking open a locked briefcase than opening the folds of a paper bag." Because the government never claimed independent suspicion or probable cause to detain or open the cans, and obtained no explicit authorization to destroy them, the destruction of the can fell outside the consent and could not be justified on any other ground.

## Conclusion
The search exceeded the scope of consent; the Tenth Circuit reversed the denial of suppression of the methamphetamine and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 10th Cir.**
- *Osage* applies and **cabins** [[Florida v. Jimeno]]'s objective-reasonableness scope-of-consent test: while general consent reaches containers that might hold contraband, it does not authorize an officer to destroy a container without explicit authorization or another lawful basis. It is an illustrative limit on the reach of consent for the [[Consent Searches]] doctrine.

## Appears on
- [[Consent Searches]] — *Limiting*

## Sources
- *United States v. Osage*, 235 F.3d 518 (10th Cir. 2000) — https://www.courtlistener.com/opinion/160502/united-states-v-osage/ — pinpoints: 520, 521, 522.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "dfc576bf57dbd29c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "235 F.3d 518 (2000)", "court": "U.S. Court of Appeals, 10th Circuit", "neutral_cite": "2000 U.S. App. LEXIS 32020; 2000 WL 1842404", "official_citation_present": true, "parallel_cite": "2000 Colo. J. C.A.R. 6671", "title": "United States v. Osage", "year": "2000"}}
{"assertion_id": "37a63ddfabe3a3bd", "dimension": "support", "kind": "home_role", "locator": {"home": "Consent Searches"}, "payload": {"home": "Consent Searches", "role": "Limiting", "title": "United States v. Osage"}}
{"assertion_id": "ef77d6d49f2ad29a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "General consent to a search does not authorize an officer to destroy a container: before an officer may actually destroy or render completely useless a container otherwise within the scope of a permissive search, the officer must obtain explicit authorization or have some other lawful basis to proceed.", "title": "United States v. Osage"}}
{"assertion_id": "05d0ea32bdbba88a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2000-12-15", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Osage", "field_i_validity": "good_law", "scope_note": "Good law. Applies and cabins Florida v. Jimeno: general consent does not authorize destroying a container.", "title": "United States v. Osage", "varies_by_point": "false"}}
{"assertion_id": "090768e4d5f99874", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 10th Cir.", "title": "United States v. Osage"}}
```

### lake record — United States v. Osage

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Osage",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Osage",
    "case_name_short": "Osage",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. David Blake OSAGE, Defendant-Appellant",
    "input_case_name": "United States v. Osage",
    "court": "U.S. Court of Appeals, 10th Circuit",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "10th",
    "state": null,
    "date_decided": "2000-12-15",
    "year": 2000,
    "docket": null,
    "cluster_id": 160502,
    "lead_opinion_id": 160502,
    "sibling_ids": [
      160502
    ],
    "absolute_url": "/opinion/160502/united-states-v-osage/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "235 F.3d 518",
      "volume": "235",
      "reporter": "F.3d",
      "page": "518",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "2000 Colo. J. C.A.R. 6671",
        "volume": "2000",
        "reporter": "Colo. J. C.A.R.",
        "page": "6671",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2000 U.S. App. LEXIS 32020",
        "volume": "2000",
        "reporter": "U.S. App. LEXIS",
        "page": "32020",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 WL 1842404",
        "volume": "2000",
        "reporter": "WL",
        "page": "1842404",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "235 F.3d 518",
        "volume": "235",
        "reporter": "F.3d",
        "page": "518",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 Colo. J. C.A.R. 6671",
        "volume": "2000",
        "reporter": "Colo. J. C.A.R.",
        "page": "6671",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 U.S. App. LEXIS 32020",
        "volume": "2000",
        "reporter": "U.S. App. LEXIS",
        "page": "32020",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 WL 1842404",
        "volume": "2000",
        "reporter": "WL",
        "page": "1842404",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "235 F.3d 518",
    "official_selection": {
      "court_class": "coa",
      "selected": "235 F.3d 518",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-520",
      "page": null,
      "quote": "Noticing that one can's label appeared re-glued and that the can felt and sounded like it held salt rather than tamales in liquid, the officer used a Leatherman tool to cut the can open, discovering methamphetamine inside. Osage was charged with possession with intent to distribute methamphetamine (21 U.S.C. \u00a7 841); the district court denied suppression, reasoning that Osage's consent was voluntary and that he never limited its scope or objected as the can was opened. Osage pleaded guilty, reserving his right to appeal the suppression ruling. ## Issue Whether a suspect's general consent to search his luggage authorized the officer to cut open \u2014 and thereby destroy \u2014 a sealed can found inside. ## Rule The scope of a consent search is bounded by the consent given,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-521",
      "page": null,
      "quote": "We acknowledge that the Supreme Court and this court have previously stated that a general consent to search a particular area is reasonably understood to extend to a search of containers within that area that could contain contraband . . . . However, we do not read that authority to permit the destruction of such containers.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-522",
      "page": null,
      "quote": "before an officer may actually destroy or render completely useless a container which would otherwise be within the scope of a permissive search, the officer must obtain explicit authorization, or have some other, lawful, basis upon which to proceed.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 12507,
      "fragment": "#:~:text=before%20an%20officer%20may%20actually",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2000-12-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Osage",
    "varies_by_point": false,
    "scope_note": "Good law. Applies and cabins Florida v. Jimeno: general consent does not authorize destroying a container.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Dubbs Ex Rel. Dubbs v. Head Start, Inc.",
          "cluster_id": 163684,
          "cite": [
            "336 F.3d 1194",
            "2003 U.S. App. LEXIS 14578",
            "2003 WL 21690533"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "No. 01-5098",
          "cluster_id": 782823,
          "cite": [
            "336 F.3d 1194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lyons",
          "cluster_id": 170093,
          "cite": [
            "510 F.3d 1225",
            "2007 U.S. App. LEXIS 29307",
            "2007 WL 4395442"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marquez",
          "cluster_id": 163723,
          "cite": [
            "337 F.3d 1203",
            "2003 U.S. App. LEXIS 15374",
            "2003 WL 21758415"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gregoire",
          "cluster_id": 166481,
          "cite": [
            "425 F.3d 872",
            "2005 U.S. App. LEXIS 21398",
            "2005 WL 2422788"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathan v. Nally",
          "cluster_id": 8209848,
          "cite": [
            "178 Vt. 222",
            "2005 VT 85",
            "882 A.2d 1164",
            "2005 Vt. LEXIS 168"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shaniz West v. City of Caldwell",
          "cluster_id": 4642875,
          "cite": [
            "931 F.3d 978"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carbajal-Iriarte",
          "cluster_id": 172835,
          "cite": [
            "586 F.3d 795",
            "2009 U.S. App. LEXIS 24129",
            "2009 WL 3585083"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Pikyavit",
          "cluster_id": 170798,
          "cite": [
            "527 F.3d 1126",
            "2008 U.S. App. LEXIS 11874",
            "2008 WL 2265154"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Arizona v. Rosa Elene Becerra",
          "cluster_id": 3171759,
          "cite": [
            "239 Ariz. 90",
            "366 P.3d 567",
            "731 Ariz. Adv. Rep. 9",
            "2016 Ariz. App. LEXIS 9"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 2378130,
          "cite": [
            "501 F. Supp. 2d 1284",
            "2007 U.S. Dist. LEXIS 58308",
            "2007 WL 2258451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mendoza",
          "cluster_id": 3189005,
          "cite": [
            "817 F.3d 695",
            "2016 WL 1169102",
            "2016 U.S. App. LEXIS 5597"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Santana-Aguirre",
          "cluster_id": 1451461,
          "cite": [
            "537 F.3d 929",
            "2008 U.S. App. LEXIS 17125",
            "2008 WL 3289403"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Al-Marri",
          "cluster_id": 2425981,
          "cite": [
            "230 F. Supp. 2d 535",
            "2002 U.S. Dist. LEXIS 21765",
            "2002 WL 31519619"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gomez-Arzate",
          "cluster_id": 4835114,
          "cite": [
            "981 F.3d 832"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Navas",
          "cluster_id": 1452233,
          "cite": [
            "640 F. Supp. 2d 256",
            "2009 U.S. Dist. LEXIS 37464",
            "2009 WL 1138020"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Villarreal v. State",
          "cluster_id": 6243487,
          "cite": [
            "565 S.W.3d 919"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pablo Ernesto Villarreal Jr. v. State",
          "cluster_id": 4577200,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Valdivia, R., Aplt.",
          "cluster_id": 4544418,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Santana-Aguirre",
          "cluster_id": 3045182,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Garza",
          "cluster_id": 2528576,
          "cite": [
            "269 F. Supp. 2d 1330",
            "2003 U.S. Dist. LEXIS 11095",
            "2003 WL 21499232"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jeter",
          "cluster_id": 2427055,
          "cite": [
            "394 F. Supp. 2d 1334",
            "2005 U.S. Dist. LEXIS 6790",
            "2005 WL 941178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gonzalez-Garcia",
          "cluster_id": 2147739,
          "cite": [
            "781 F. Supp. 2d 1167",
            "2011 U.S. Dist. LEXIS 27360",
            "2011 WL 938360"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(160502) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca10)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(160502)",
        "reviewed": 24,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 23,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(160502)",
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
    "complete_query": "cites:(160502)",
    "indexed_citing_opinions": 24,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 160502,
        "count": 24,
        "count_source": "search"
      }
    ],
    "citation_count": 34,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-osage.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjA2MDAwNTMmcz0xNjM3MjMmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28160502%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 160502,
        "cited_id": 112595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 153281,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 396620,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 463815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 540933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 552827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 563771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 572508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 672873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 673940,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 676092,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 754317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 763263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 769221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 1200095,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "CRU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T01:55:18Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:55:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:55:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:58:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:55:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Osage

```
                                                                       F I L E D
                                                                United States Court of Appeals
                                                                        Tenth Circuit
                                       PUBLISH
                                                                       DEC 15 2000
                    UNITED STATES COURT OF APPEALS
                                                                     PATRICK FISHER
                                                                            Clerk
                                 TENTH CIRCUIT



 UNITED STATES OF AMERICA,

               Plaintiff - Appellee,
          v.                                           No. 99-2235
 DAVID BLAKE OSAGE,

               Defendant - Appellant.


           APPEAL FROM THE UNITED STATES DISTRICT COURT
                  FOR THE DISTRICT OF NEW MEXICO
                        (D.C. NO. CR-98-552-BB)


Stuart Southerland, Tulsa, Oklahoma, for Appellant.

David N. Williams, Assistant United States Attorney (John J. Kelly, United States
Attorney, and J. Miles Hanisee, Assistant United States Attorney, on the brief),
Albuquerque, New Mexico, for Appellee.


Before LUCERO and ANDERSON , Circuit Judges, and        MILLS, * District Judge.


ANDERSON , Circuit Judge.




      *
       The Honorable Richard Mills, United States District Judge for the Central
District of Illinois, sitting by designation.
      David Blake Osage appeals his conviction on one count of possession with

intent to distribute one kilogram or more of methamphetamine, in violation of

21 U.S.C. § 841(a)(1), (b)(1)(A). Mr. Osage moved unsuccessfully to suppress

the introduction of the methamphetamine and subsequently pled guilty to the

indictment, reserving his right to appeal the suppression ruling. On appeal, he

challenges the district court’s finding that he consented to the search that resulted

in seizure of the methamphetamine. Because we conclude that the search

exceeded the scope of the consent given, we reverse and remand this case.



                                  BACKGROUND

      On June 4, 1998, Task Force Officer Sam Candelaria of the New Mexico

State Police notified Task Force Officer Jonathan Salazar that Mr. Osage would

be traveling through Albuquerque on an Amtrak train that ran between Los

Angeles and Chicago. Mr. Osage had paid cash for passage in a sleeping car

aboard the train shortly before it left California.

      Officer Salazar boarded the train in Albuquerque with another officer, both

of whom were in plain clothes. Officer Salazar confronted Mr. Osage in a

passageway in the sleeping car, identified himself as a police officer, and asked to

speak to him. The officer asked Mr. Osage about his destination and requested to

see his tickets. Mr. Osage told Officer Salazar that his tickets were in a bag in his


                                          -2-
room. The officer followed Mr. Osage to his room, where Mr. Osage produced

the tickets.

       Officer Salazar then asked Mr. Osage about his luggage, and Mr. Osage

identified two suitcases. One of the suitcases, a black bag, was closed and

locked. The officer asked for permission to search the bags. Mr. Osage

responded, “yeah, I guess.” Appellant’s App. at 311. Officer Salazar asked again

whether it would be okay to search the bags. Mr. Osage did not respond verbally,

but nodded, gestured upward with his palms, and pointed toward the black bag.

       Mr. Osage produced a key and opened the black bag. Inside, Officer

Salazar found plastic grocery bags containing four 28-ounce cans labeled

“tamales in gravy.” The officer picked up one of the cans and noticed that the

label appeared to have been tampered with, perhaps re-glued. When he shook the

can, he noticed that it did not feel and sound like it contained tamales in liquid,

but instead felt like a container of salt would feel when shaken. He then took a

Leatherman tool off his belt, opened the can, and discovered a plastic bag

containing methamphetamine.

       The district court denied Mr. Osage’s motion to suppress on the ground that

his consent to search was freely and voluntarily given, and Mr. Osage never

limited its scope to exclude opening the tamales can. Specifically, the court

stated, “[w]hile the Court was extremely skeptical that the extent of the consent


                                          -3-
extended to physically opening the tamale cans, [Mr. Osage] stood by and

watched without demur while the agent took out a can opener and split the can

lid. If [Mr. Osage] had questioned this procedure, the outcome of this motion

may well have been different.” Order at 2, Appellant’s App. at 91 (citing      United

States v. Kim , 27 F.3d 947 (3d Cir. 1994);     United States v. Torres , 663 F.2d 1019

(10th Cir. 1981), cert. denied , 456 U.S. 973 (1982); United States v. Pena , 920

F.2d 1509, 1515 (10th Cir. 1990)).



                                      DISCUSSION

       When we review the denial of a motion to suppress, we must accept the

district court’s factual findings unless they are clearly erroneous.    United States v.

Wald , 216 F.3d 1222, 1225 (10th Cir. 2000). “The district court’s determination

of reasonableness under the Fourth Amendment, however, is reviewed de novo.”

Id.



       I. Validity of Consent

       Mr. Osage argues that consent solicited by a police officer is involuntary

per se and he argues that the particular consent given in this case was not freely

and voluntarily given. He makes a number of subsidiary arguments. Because we

conclude that the district court erred in denying his motion to suppress based


                                              -4-
upon the scope of the consent, we need not address these other arguments. We

assume that Mr. Osage’s consent was validly given.



       II. Scope of Consent

       Mr. Osage argues that Officer Salazar’s actions in opening the tamale can

exceeded the scope of the search. When law enforcement officers rely upon

consent as the basis for a warrantless search, the scope of the consent determines

the permissible scope of the search.       See Florida v. Jimeno , 500 U.S. 248, 251-52

(1991). The scope of consent is measured by objective reasonableness: “what

would the typical reasonable person have understood by the exchange between the

officer and the suspect?”    Id. at 251.

       “We view the evidence in the light most favorable to the government and

must uphold a district court’s finding that a search is within the boundaries of the

consent unless it is clearly erroneous.”     United States v. Pena , 143 F.3d 1363,

1368 (10th Cir. 1998). While we have stated that a defendant’s “failure to object

to the . . . search of [a particular area] ‘may be considered an indication that the

search was within the scope of the consent,’”      id. (quoting United States v.

Espinosa , 782 F.2d 888, 892 (10th Cir. 1986)), this case presents a more narrow

issue: whether Mr. Osage’s failure to object to a search of a sealed can permitted




                                             -5-
the officer, in the course of conducting his search, to destroy the can or render it

completely useless for its intended function.     1
                                                      We conclude that it does not.

       The Supreme Court in      Jimeno held that “it was objectively reasonable for

the police to conclude that the general consent to search [defendant’s] car

included consent to search containers within that car which might bear drugs.”

Jimeno , 500 U.S. at 251. The Court accordingly upheld the opening and search of

a brown paper bag inside the car. However, the Court also stated, “[i]t is very

likely unreasonable to think that a suspect, by consenting to the search of his

trunk, has agreed to the breaking open of a locked briefcase within the trunk.”        Id.

at 251-52.

       We have not directly addressed the issue of whether a police search which

destroys or renders completely useless the item searched exceeds the scope of any

consent given for the search. However, we have hinted that a search could be “so

invasive or destructive” as to go beyond the scope of the search consented to.        See

United States v. Santurio , 29 F.3d 550, 553 (10th Cir. 1994) (noting that a “search

was not so invasive as to exceed the scope of defendant’s consent to the search”




       The government has never argued that Officer Salazar had articulable
       1

suspicion to briefly detain the cans for further investigation or probable cause to
seek a warrant. Officer Salazar has never claimed he did. At oral argument of
this appeal, the government specifically disavowed any reliance upon that ground.
Thus, this case involves only the validity and scope of Mr. Osage’s consent to the
search of the cans.

                                            -6-
where the officer “did not ‘tear up’ the van or enter the compartment” until a dog

alerted on the compartment). Other courts have reached the same conclusion.

See , e.g. , United States v. Torres , 32 F.3d 225, 231-32 (7th Cir. 1994) (“We agree

that ‘general permission to search does not include permission to inflict

intentional damage to the places or things to be searched.’”) (quoting     United

States v. Martinez , 949 F.2d 1117, 1119 (11th Cir. 1992));     United States v.

Strickland , 902 F.2d 937, 941-42 (11th Cir. 1990) (holding that a general consent

to search a car does not extend to the “intentional infliction of damage to the

vehicle or the property contained within it”);     State v. Garcia , 986 P.2d 491, 495

(N.M. Ct. App. 1999) (holding that “[d]efendant’s consent to permit the officers

to ‘look at’ her vehicle could not reasonably be interpreted to encompass drilling

into the vehicle.”), cert. granted , 990 P.2d 824 (N.M. Aug. 11, 1999).

       The district court relied upon   United States v. Kim , 27 F.3d 947 (3d Cir.

1994), United States v. Torres , 663 F.2d 1019 (10th Cir. 1981) and      United States

v. Pena , 920 F.2d 1509 (10th Cir. 1990), in support of its conclusion that Mr.

Osage’s silence while he watched Officer Salazar open the tamales can indicated

Mr. Osage’s consent to the search of the can. The government places great

reliance upon Kim in this appeal. In Kim , officers aboard an Amtrak train

received consent to search a handbag accompanying the defendant in his train

roomette. One of the officers found inside the bag six cans of “Naturade All-


                                             -7-
Natural Vegetable Protein” which “appeared to be factory-sealed cans with

factory lids which were intact.”     Kim , 27 F.3d at 950. The officer then “opened

one of the cans” and discovered methamphetamine inside.            Id.

       The Third Circuit upheld the search of the can as within the scope of the

permission granted. It relied upon     Jimeno for its conclusion that “when one gives

general permission to search for drugs in a confined area, that permission extends

to any items within that area that a reasonable person would believe to contain

drugs.” Id. at 956. It found no meaningful distinction between the brown paper

bag in Jimeno and the sealed cans in the case before it. Moreover, while

acknowledging that the Court in      Jimeno had stated that a search of a locked

suitcase in a vehicle would not be within the scope of a permissive search of the

vehicle, the Kim court summarily concluded “cans such as those found in the case

sub judice are not similar to locked briefcases.”    Id. at 957.

       We are not persuaded that     Kim requires us to reach the same conclusion in

this case. First, while the   Kim court evidently determined that a sealed can is

more like a brown paper bag than a locked briefcase, it provides no explanation

for that conclusion. Additionally, the court did not consider whether the can was

destroyed or rendered useless after being opened. Indeed, the court may have

assumed that it was not so damaged, because it relied upon and quoted the




                                             -8-
following reasoning from    United States v. Springs , 936 F.2d 1330, 1334-35 (D.C.

Cir. 1991) in support of its holding:

       the evidence supports a view that the opening of the baby powder
       container did not depend upon possession of a key, knowledge of a
       combination, or anything other than merely removing its lid.     Neither
       did the fact of its opening it render it useless, anymore than the
       opening of the folds destroyed the usefulness of the paper bag in
       Jimeno .

(emphasis added). We conclude that the opening of a sealed can, thereby

rendering it useless and incapable of performing its designated function, is more

like breaking open a locked briefcase than opening the folds of a paper bag.

       We acknowledge that the Supreme Court and this court have previously

stated that a general consent to search a particular area is reasonably understood

to extend to a search of containers within that area that could contain contraband,

absent some indication by the suspect that he wishes to terminate or limit the

search. See Jimeno , 500 U.S. at 252 (“[I]f [a suspect’s] consent would reasonably

be understood to extend to a particular container, the Fourth Amendment provides

no grounds for requiring a more explicit authorization.”);      United States v.

Gordon , 173 F.3d 761, 766 (10th Cir.) (“We consistently and repeatedly have held

a defendant’s failure to limit the scope of a general authorization to search, and

failure to object when the search exceeds what he later claims was a more limited

consent, is an indication the search was within the scope of consent.”),     cert.

denied , 120 S. Ct. 205 (1999). However, we do not read that authority to permit

                                            -9-
the destruction of such containers.   2
                                          We therefore hold that, before an officer may

actually destroy or render completely useless a container which would otherwise

be within the scope of a permissive search, the officer must obtain explicit

authorization, or have some other, lawful, basis upon which to proceed.

       For the foregoing reasons, the district court’s decision denying suppression

of the methamphetamine found in the tamales cans is REVERSED and the case is

REMANDED for further proceedings consistent herewith.




       2
        We do not read our prior cases in Torres and Pena, upon which the district
court relied, to compel a different result in this case. In Torres, a defendant gave
police permission to search a car. In conducting the search, the officers “pull[ed]
out an ashtray in the side of the door,” and “removed the air-vent cover in the side
of the door,” where they found contraband. Torres, 663 F.2d at 1021. We held
that search was “within the bounds of the actual consent given.” Id. at 1027.
       Similarly, in Pena, after receiving permission to search a vehicle, the police
officer “got a screwdriver . . . and removed the rear quarter panel vent” of the
vehicle, where he discovered contraband. Pena, 920 F.2d at 1512. The defendant
at no time objected to the search. We held that the search “was conducted within
the general scope of the permission granted.” Id. at 1515. Neither Pena nor
Torres involved the actual destruction of the item searched, as occurred in this
case.
       Other cases in our circuit have permitted some “dismantling” of an item
searched, but none have permitted complete and utter destruction or
incapacitation of an item or container. See, e.g., Pena, 143 F.3d at 1368 (holding
that consent to search motel room included “search into the area above the
bathroom ceiling” in the face of no objection by defendant); United States v.
McRae, 81 F.3d 1528, 1537-38 (10th Cir. 1996) (stating that consent to search car
trunk permitted officer to lift crinkled carpet area in the face of no objection by
defendant); Santurio, 29 F.3d at 552-53 (holding that consent to search interior of
car included removal of screws from strip holding down carpeting).

                                             -10-

```

---

## GROUP: content/cases/United States v. Padilla.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Padilla"
type: case
citation: "508 U.S. 77 (1993)"
parallel_cite: "113 S. Ct. 1936; 123 L. Ed. 2d 635"
neutral_cite: 1993 U.S. LEXIS 3126
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1993
date_decided: 1993-05-03
docket: 92-207
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1993-05-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Padilla
  varies_by_point: false
  scope_note: "Rejects the Ninth Circuit's coconspirator exception; standing remains personal. Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112856/united-states-v-padilla/"
  cluster_id: 112856
  opinion_id: 112856
  identity_checked: true
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: "Key — Progeny"
related: ["[[Alderman v. United States]]", "[[Rakas v. Illinois]]", "[[Rawlings v. Kentucky]]", "[[Soldal v. Cook County]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "conspiracy", "expectation-of-privacy"]
holding: "There is no 'coconspirator exception' to Fourth Amendment standing; a defendant's supervisory role in or joint control over a conspiracy does not by itself confer standing — only a personal privacy or property interest invaded by the search does."
lake:
  record_id: United States v. Padilla
  status: verified
  projected_at: 2026-07-09
---

# United States v. Padilla

*508 U.S. 77 (1993)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Members of a drug-trafficking conspiracy were prosecuted after police stopped and searched a car and found cocaine. The Ninth Circuit had adopted a "coconspirator exception" to standing: a co-conspirator could challenge a search if he had either a supervisory role in the conspiracy or joint control over the place or property searched. Applying that rule, it allowed several respondents to contest the stop and search even without a personal interest in the car.

## Issue
Whether a defendant may challenge a search on the strength of his supervisory role in, or joint control over property used by, a criminal conspiracy — that is, whether a "coconspirator exception" supplements the rule that [[Standing to Challenge a Search|Fourth Amendment standing]] requires a personal privacy or possessory interest.

## Rule
No; standing is personal and the conspiracy adds nothing to it. Quoting *[[Alderman v. United States|Alderman]]*: "suppression of the product of a Fourth Amendment violation can be successfully urged only by those whose rights were violated by the search itself, not by those who are aggrieved solely by the introduction of damaging evidence. Co-conspirators and codefendants have been accorded no special standing." — 508 U.S. at 82 (quoting *Alderman v. United States*, 394 U.S. 165, 171–172). ^pin-82

"Expectations of privacy and property interests govern the analysis of Fourth Amendment search and seizure claims. Participants in a criminal conspiracy may have such expectations or interests, but the conspiracy itself neither adds to nor detracts from them." — [*Id.* at 82](https://www.courtlistener.com/opinion/112856/united-states-v-padilla/#:~:text=Expectations%20of%20privacy%20and%20property). ^pin-82b

## Application
The respondents' positions in the conspiracy — one serving as the "communication link," others "in charge of transportation" — had "no bearing on their respective Fourth Amendment rights." Whether any of them could suppress the cocaine turned, case by case, on whether that respondent personally held a property interest interfered with by the stop or a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] invaded by the search of the car — not on his conspiratorial role. The Ninth Circuit's exception both contradicted *[[Alderman v. United States|Alderman]]* and was at odds with the personal-rights principle.

## Conclusion
[[Common Legal Terms#per-curiam|Per curiam]]: the "coconspirator exception" was rejected; the judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]] for individualized determinations of each respondent's personal Fourth Amendment interest.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Padilla* reaffirms the personal-rights standing rule of [[Alderman v. United States]] and [[Rakas v. Illinois]], rooted in the privacy/property interests of [[Rawlings v. Kentucky]] and [[Soldal v. Cook County]].

## Appears on
- [[Standing to Challenge a Search]] — *Key — Progeny*

## Sources
- *United States v. Padilla*, 508 U.S. 77 (1993) — https://www.courtlistener.com/opinion/112856/united-states-v-padilla/ — pinpoint: 82.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "de778aacb21e1fa4", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "508 U.S. 77 (1993)", "court": "U.S. Supreme Court", "neutral_cite": "1993 U.S. LEXIS 3126", "official_citation_present": true, "parallel_cite": "113 S. Ct. 1936; 123 L. Ed. 2d 635", "title": "United States v. Padilla", "year": "1993"}}
{"assertion_id": "ba1d92c10fb21b4a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "There is no 'coconspirator exception' to Fourth Amendment standing; a defendant's supervisory role in or joint control over a conspiracy does not by itself confer standing — only a personal privacy or property interest invaded by the search does.", "title": "United States v. Padilla"}}
{"assertion_id": "d2ce10277f4f8e9c", "dimension": "support", "kind": "home_role", "locator": {"home": "Standing to Challenge a Search"}, "payload": {"home": "Standing to Challenge a Search", "role": "Key — Progeny", "title": "United States v. Padilla"}}
{"assertion_id": "0801c78b07524237", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1993-05-03", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Padilla", "field_i_validity": "good_law", "scope_note": "Rejects the Ninth Circuit's coconspirator exception; standing remains personal. Good law.", "title": "United States v. Padilla", "varies_by_point": "false"}}
{"assertion_id": "bbeb438c122f264e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Padilla"}}
```

### lake record — United States v. Padilla

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Padilla",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Padilla",
    "case_name_short": "Padilla",
    "case_name_full": "UNITED STATES v. PADILLA Et Al.",
    "input_case_name": "United States v. Padilla",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1993-05-03",
    "year": 1993,
    "docket": "92-207",
    "cluster_id": 112856,
    "lead_opinion_id": 112856,
    "sibling_ids": [
      112856
    ],
    "absolute_url": "/opinion/112856/united-states-v-padilla/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "508 U.S. 77",
      "volume": "508",
      "reporter": "U.S.",
      "page": "77",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "113 S. Ct. 1936",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "1936",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "123 L. Ed. 2d 635",
        "volume": "123",
        "reporter": "L. Ed. 2d",
        "page": "635",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1993 U.S. LEXIS 3126",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "3126",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "508 U.S. 77",
        "volume": "508",
        "reporter": "U.S.",
        "page": "77",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 S. Ct. 1936",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "1936",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "123 L. Ed. 2d 635",
        "volume": "123",
        "reporter": "L. Ed. 2d",
        "page": "635",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 U.S. LEXIS 3126",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "3126",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "508 U.S. 77",
    "official_selection": {
      "court_class": "scotus",
      "selected": "508 U.S. 77",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-82",
      "page": null,
      "quote": "supplements the rule that Fourth Amendment standing requires a personal privacy or possessory interest. ## Rule No; standing is personal and the conspiracy adds nothing to it. Quoting *Alderman*:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-82b",
      "page": null,
      "quote": "Expectations of privacy and property interests govern the analysis of Fourth Amendment search and seizure claims. Participants in a criminal conspiracy may have such expectations or interests, but the conspiracy itself neither adds to nor detracts from them.",
      "star_marker": "82",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 9952,
      "fragment": "#:~:text=Expectations%20of%20privacy%20and%20property",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1993-05-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Padilla",
    "varies_by_point": false,
    "scope_note": "Rejects the Ninth Circuit's coconspirator exception; standing remains personal. Good law.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Padilla:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cardona-Sandoval",
          "cluster_id": 194957,
          "cite": [
            "6 F.3d 15",
            "1993 WL 374897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Cedeno",
          "cluster_id": 6096982,
          "cite": [
            "193 A.D.2d 540",
            "598 N.Y.S.2d 192",
            "1993 N.Y. App. Div. LEXIS 5275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane1_negative"
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
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sepulveda",
          "cluster_id": 195094,
          "cite": [
            "15 F.3d 1161"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, Plaintiff-Appellee/cross-Appellant v. Rene Gonzalez-Lerma, Defendant-Appellant/cross-Appellee",
          "cluster_id": 661539,
          "cite": [
            "14 F.3d 1479",
            "1994 U.S. App. LEXIS 1539"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "CAMP Legal Defense Fund, Inc. v. City of Atlanta",
          "cluster_id": 77366,
          "cite": [
            "451 F.3d 1257",
            "2006 U.S. App. LEXIS 14407",
            "2006 WL 1623279"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sarkisian",
          "cluster_id": 7079538,
          "cite": [
            "197 F.3d 966",
            "1999 WL 1083966"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moreno v. Baca",
          "cluster_id": 792690,
          "cite": [
            "431 F.3d 633",
            "2005 WL 3338300"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Robert Dale Lowe, Jr.",
          "cluster_id": 4472370,
          "cite": [
            "812 N.W.2d 554",
            "2012 Iowa Sup. LEXIS 8"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hunter Lee Williams Nicholas Edward George and Geoffrey Hillman Leek",
          "cluster_id": 784663,
          "cite": [
            "354 F.3d 497"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald L. Lingenfelter, United States of America v. Gary Marolf, AKA Gary Marlow, United States of America v. Lawrence Morgan",
          "cluster_id": 610679,
          "cite": [
            "997 F.2d 632",
            "93 Daily Journal DAR 8410",
            "93 Cal. Daily Op. Serv. 4978",
            "1993 U.S. App. LEXIS 15893"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Ervin Payne, United States of America v. Christopher Foster",
          "cluster_id": 744110,
          "cite": [
            "119 F.3d 637",
            "1997 U.S. App. LEXIS 17325"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vasak Sarkisian, United States of America v. Vitaly Semenov, United States of America v. Ashot Mikayelyan, United States of America v. Sergey Ivanchikov",
          "cluster_id": 766923,
          "cite": [
            "197 F.3d 966",
            "99 Daily Journal DAR 12221",
            "99 Cal. Daily Op. Serv. 9472",
            "1999 U.S. App. LEXIS 31553"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lopez-Lopez",
          "cluster_id": 199833,
          "cite": [
            "282 F.3d 1",
            "2002 U.S. App. LEXIS 2896",
            "2002 WL 229881"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Eric Powell",
          "cluster_id": 4346362,
          "cite": [
            "847 F.3d 760",
            "2017 FED App. 0025p",
            "2017 WL 474343",
            "2017 U.S. App. LEXIS 2093"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 1746991,
          "cite": [
            "648 So. 2d 669",
            "1994 WL 620797"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Torres",
          "cluster_id": 198221,
          "cite": [
            "162 F.3d 6",
            "1998 U.S. App. LEXIS 30808",
            "1998 WL 823184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Arturo Torres and Ramon R. Vargas-Hernandez, Also Known as Ramon Vargas",
          "cluster_id": 676092,
          "cite": [
            "32 F.3d 225"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gonzales",
          "cluster_id": 157368,
          "cite": [
            "164 F.3d 1285",
            "1999 WL 5092"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Ramos, United States of America v. Richard Ramos",
          "cluster_id": 659415,
          "cite": [
            "12 F.3d 1019",
            "1994 WL 2259",
            "1994 U.S. App. LEXIS 973"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gene Hinton (070386)",
          "cluster_id": 1086776,
          "cite": [
            "216 N.J. 211",
            "78 A.3d 553",
            "2013 WL 5745595",
            "2013 N.J. LEXIS 1092"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Laura Michelle Morning, United States of America v. Francisco Ignacio Leon-Yanez",
          "cluster_id": 702612,
          "cite": [
            "64 F.3d 531",
            "95 Cal. Daily Op. Serv. 6773",
            "95 Daily Journal DAR 11651",
            "1995 U.S. App. LEXIS 24192",
            "1995 WL 505229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Coleman, United States of America v. Andre Worthy, United States of America v. Orlando Willis",
          "cluster_id": 784218,
          "cite": [
            "349 F.3d 1077"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gonzales",
          "cluster_id": 760543,
          "cite": [
            "164 F.3d 1285",
            "1999 Colo. J. C.A.R. 1285",
            "1999 U.S. App. LEXIS 218"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Courtney Noble",
          "cluster_id": 2716405,
          "cite": [
            "762 F.3d 509",
            "2014 WL 3882493",
            "2014 U.S. App. LEXIS 15279"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Veronica M. Thompson and Veronica Andalon",
          "cluster_id": 735368,
          "cite": [
            "106 F.3d 794",
            "1997 U.S. App. LEXIS 2281"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112856) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 89,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 89,
        "triage_read": 4,
        "triage_snippet_classified": 85
      },
      "lane2_top_cited": {
        "query": "cites:(112856)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMSZzPTE0MzY0MzEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112856%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112856)",
        "reviewed": 2,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 2,
        "triage_read": 0,
        "triage_snippet_classified": 2
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112856)",
    "indexed_citing_opinions": 120,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112856,
        "count": 120,
        "count_source": "search"
      }
    ],
    "citation_count": 197,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-padilla.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjM4NDY5Mjgmcz0xMDM0NDAzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112856%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112856,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 112795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 341773,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 343457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 387237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 441830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 545151,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 571310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 580800,
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
    "date_created": "2026-07-06T01:58:19Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:58:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:58:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:07:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:58:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Padilla

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b126-5">
  Per Curiam.
 </author>
<p id="b126-6">
  The United States Court of Appeals for the Ninth Circuit has adopted what it terms a “coconspirator exception” to the rule regarding who may challenge the constitutionality of a search or seizure. Under its reasoning, a co-conspirator obtains a legitimate expectation of privacy for Fourth Amendment purposes if he has either a supervisory role in the conspiracy or joint control over the place or property involved in the search or seizure. This “exception,” apparently developed in a series of earlier decisions of the Court of Appeals, squarely contradicts the controlling case from this Court. We therefore reject it.
 </p>
<p id="b126-7">
  While patrolling Interstate Highway 10 in Casa Grande, Arizona, Officer Russel Fifer spotted a Cadillac traveling westbound at approximately 65 miles per hour. Fifer followed the Cadillac for several miles because he thought the driver acted suspiciously as he passed the patrol car. Fifer ultimately stopped the Cadillac because it was going too slowly. Luis Arciniega, the driver and sole occupant of the car, gave Fifer his driver’s license and an insurance card demonstrating that respondent Donald Simpson, a United States customs agent, owned the Cadillac. Fifer and Robert Williamson, an officer who appeared on the scene to assist Fifer, believed that Arciniega matched the drug courier profile. Acting on this belief, they requested and received Arci
  <span citation-index="1" class="star-pagination" label="79"> 
   *79
   </span>
  niega’s permission to search the vehicle. The officers found 560 pounds of cocaine in the trunk and immediately arrested Arciniega.
 </p>
<p id="b127-4">
  After agreeing to make a controlled delivery of the cocaine, Arciniega made a telephone call to his contact from a motel in Tempe, Arizona. Respondents Jorge and Maria Padilla drove to the motel in response to the telephone call, but were arrested as they attempted to drive away in the Cadillac. Like Arciniega, Maria Padilla agreed to cooperate with law enforcement officials. She led them to the house in which her husband, respondent Xavier Padilla, was staying. The ensuing investigation linked Donald Simpson and his wife, respondent Maria Sylvia Simpson, to Xavier Padilla.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
</p>
<p id="b127-5">
  Respondents were charged with conspiracy to distribute and possess with intent to distribute cocaine, in violation of <span class="citation no-link">21 U. S. C. §846</span>, and possession of cocaine with intent to distribute, in violation of § 841(a)(1). Xavier Padilla was also charged with engaging in a continuing criminal enterprise, in violation of <span class="citation no-link">21 U. S. C. § 848</span> (1988 ed. and Supp. III). Respondents moved to suppress all evidence discovered in the course of the investigation, claiming that the evidence was the fruit of the unlawful investigatory stop of Arciniega’s vehicle. The United States District Court for the District of Arizona ruled that all respondents were entitled to challenge the stop and search because they were involved in “a joint venture for transportation... that had control of the contraband.” App. to Pet. for Cert. 22a. The District Court reasoned that, as owners, the Simpsons retained a reasonable expectation of privacy in their car, but that the Padillas could
  <span citation-index="1" class="star-pagination" label="80"> 
   *80
   </span>
  contest the stop solely because of their supervisory roles and their “joint control over a very sophisticated operation----”
  <em>
   <span class="citation no-link">Id.,</span>
  </em>
  at 23a. On the merits, the District Court ruled that Officer Fifer lacked reasonable suspicion to stop Areiniega,
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  and granted respondents’ motion to suppress.
 </p>
<p id="b128-7">
  The Court of Appeals affirmed in part, vacated in part, and remanded. The court began its analysis by stating that in order “[t]o contest the legality of a search and seizure, the defendants must establish that they had a legitimate expectation of privacy’ in the place searched or the property seized.” <span class="citation multiple-matches"><a href="/c/F.%202d/960/854/">960 F. 2d 854</a></span>, 858-859 (CA9 1992) (quoting
  <em>
   Bakas
  </em>
  v.
  <em>
   Illinois,
  </em>
  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 143-144</a></span> (1978)). The court then recited its eoeonspirator rule: “[A] coconspirator’s participation in an operation or arrangement that indicates joint control and supervision of the place searched establishes standing.” 960 F. 2d, at 859 (citations omitted).
 </p>
<p id="b128-8">
  Relying on a line of eases from the Ninth Circuit, the court held that “because Xavier Padilla and Donald and Maria Simpson have demonstrated joint control and supervision over the drugs and vehicle and engaged in an active participation in a formalized business arrangement, they have standing to claim a legitimate expectation of privacy in the property searched and the items seized.”
  <em>
   Id.,
  </em>
  at 860-861. Donald Simpson established an expectation of privacy “not simply because [he] owned the car” but also because “he had a coordinating and supervisory role in the operation. He was a critical player in the transportation scheme who was essential in getting the drugs across the border.”
  <em>
   Id.,
  </em>
  at 860. Maria Simpson established a privacy interest because she “provided a communication link” between her husband, Xavier Padilla, and other members of the conspiracy, and “held a supervisory role tying everyone together and overseeing the entire operation.”
  <em>
   Ibid.
  </em>
  Xavier Padilla established an expectation of privacy because he “exhibited sub
  <span citation-index="1" class="star-pagination" label="81"> 
   *81
   </span>
  stantial control and oversight with respect to the purchase [and] the transportation through Arizona.”
  <em>
   Ibid.
  </em>
  The court expressly stated that it did not matter that Padilla was not present during the stop, or that he could not exclude others from searching the Cadillac. Ibid.
 </p>
<p id="b129-5">
  The Court
  <em>
   of
  </em>
  Appeals could not tell from the record whether Jorge and Maria Padilla “shared any responsibility for the enterprise,” or whether they were “mere employees in a family operation.”
  <em>
   Id.,
  </em>
  at 861. As a result, the court remanded to the District Court for further findings on that issue.
 </p>
<p id="b129-6">
  The Ninth Circuit appears to stand alone in embracing the “eoconspirator exception.”
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  We granted certiorari to resolve the conflict, <span class="citation multiple-matches"><a href="/c/U.%20S./506/952/">506 U. S. 952</a></span> (1992), and now reverse. It has long been the rule that a defendant can urge the suppression of evidence obtained in violation of the Fourth Amendment only if that defendant demonstrates that
  <em>
   his
  </em>
  Fourth Amendment rights were violated by the challenged search or seizure.
  <em>
   Alderman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#171" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 171-172</a></span> (1969);
  <em>
   Rakas
  </em>
  v.
  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#131" aria-description="Citation for case: Rakas v. Illinois"><em>
   Illinois, supra,
  </em>
  at 131, n. 1, 133-134</a></span>;
  <em>
   Rawlings
  </em>
  v.
  <em>
   Kentucky,
  </em>
  <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/#106" aria-description="Citation for case: Rawlings v. Kentucky">448 U. S. 98, 106</a></span> (1980). We applied this principle to the case of co-conspirators in
  <em>
   <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">Alderman</a></span>,
  </em>
  in which we said:
 </p>
<blockquote id="b129-7">
  “The established principle is that suppression of the product of a Fourth Amendment violation can be successfully urged only by those whose rights were violated
  <span citation-index="1" class="star-pagination" label="82"> 
   *82
   </span>
  by the search itself, not by those who are aggrieved solely by the introduction of damaging evidence. Co-conspirators and codefendants have been accorded no special standing.” 894 U. S., at 171-172.
 </blockquote>
<p id="b130-5">
  In
  <em>
   <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas, supra,</a></span>
  </em>
  a police search of a car yielded a box of rifle shells found in the glove compartment and a sawed-off rifle found under the passenger seat. We held that petitioners, who were passengers in the car and had no ownership interest in the rifle shells or sawed-off rifle, and no legitimate expectation of privacy in the area searched, had suffered no invasion of their Fourth Amendment rights. See also
  <em>
   <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">Rawlings, supra;</a></span> Soldal
  </em>
  v.
  <em>
   Cook County,
  </em>
  <span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/#62" aria-description="Citation for case: Soldal v. Cook County">506 U. S. 56, 62-64</a></span> (1992) (decided since the Court of Appeals rendered its decision in the present case).
 </p>
<p id="b130-6">
  The “coconspirator exception” developed by the Ninth Circuit is, therefore, not only contrary to the holding of
  <em>
   Aider-man,
  </em>
  but at odds with the principle discussed above. Expectations of privacy and property interests govern the analysis of Fourth Amendment search and seizure claims. Participants in a criminal conspiracy may have such expectations or interests, but the conspiracy itself neither adds to nor detracts from them. Neither the fact, for example, that Maria Simpson was the “communication link” between her husband and the others, nor the fact that Donald Simpson and Xavier Padilla were in charge of transportation for the conspirators, has any bearing on their respective Fourth Amendment rights.
 </p>
<p id="b130-7">
  We therefore reverse the judgment of the Court of Appeals. The case is remanded so that the court may consider whether each respondent had either a property interest protected by the Fourth Amendment that was interfered with by the stop of the automobile driven by Arciniega, or a reasonable expectation of privacy that was invaded by the search thereof.
  <em>
   <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">Alderman, supra;</a></span> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas, supra;</a></span> <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">Rawlings, supra;</a></span> <span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/" aria-description="Citation for case: Soldal v. Cook County">Soldal, supra.</a></span>
  </em>
</p>
<p id="b130-8">
<em>
   It is so ordered.
  </em>
</p>



<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b127-6">
   A related investigation led by the Drug Enforcement Agency (DEA) revealed that Warren Strubbe was also involved in the conspiracy. Although Strubbe technically is a respondent in this case, see this Court’s Rule 12.4, the Court of Appeals found that he could not challenge the stop and search of the Cadillac. Strubbe did not file a petition challenging that decision, and we therefore do not address that aspect of the court’s opinion.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b128-9">
   The Government did not challenge this finding on appeal and does not do so here.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b129-8">
   The First, Second, Fifth, Sixth, Eighth, Eleventh, and District of Columbia Circuits have declined to adopt an exception for co-conspirators or codefendants. See
   <em>
    United States
   </em>
   v.
   <em>
    Soule,
   </em>
   <span class="citation" data-id="545151"><a href="/opinion/545151/united-states-v-john-jeffrey-soule/#1036" aria-description="Citation for case: United States v. John Jeffrey Soule">908 F. 2d 1032, 1036-1037</a></span> (CA1 1990);
   <em>
    United States
   </em>
   v.
   <em>
    Galante,
   </em>
   <span class="citation" data-id="9463409"><a href="/opinion/341773/united-states-v-john-frank-galante-and-theodore-n-cameriero/#739" aria-description="Citation for case: United States v. John Frank Galante and Theodore N....">547 F. 2d 733, 739-740</a></span> (CA2 1976), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./431/969/">431 U. S. 969</a></span> (1977);
   <em>
    United States
   </em>
   v.
   <em>
    Hunter,
   </em>
   <span class="citation" data-id="343457"><a href="/opinion/343457/united-states-v-sheryl-hunter-and-ezell-allen/#1074" aria-description="Citation for case: United States v. Sheryl Hunter and Ezell Allen">550 F. 2d 1066, 1074</a></span> (CA6 1977);
   <em>
    United States
   </em>
   v.
   <em>
    DeLeon,
   </em>
   <span class="citation" data-id="387237"><a href="/opinion/387237/united-states-v-becaficio-saenz-deleon/#337" aria-description="Citation for case: United States v. Becaficio Saenz Deleon">641 F. 2d 330, 337</a></span> (CA5 1981);
   <em>
    United States
   </em>
   v.
   <em>
    Kiser,
   </em>
   <span class="citation" data-id="571310"><a href="/opinion/571310/united-states-v-stanley-carter-kiser/#424" aria-description="Citation for case: United States v. Stanley Carter Kiser">948 F. 2d 418, 424</a></span> (CA8 1991), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./503/983/">503 U. S. 983</a></span> (1992);
   <em>
    United States
   </em>
   v.
   <em>
    Brown,
   </em>
   <span class="citation" data-id="9472640"><a href="/opinion/441830/united-states-v-bruce-christian-brown-and-james-patrick-manikowski/#1507" aria-description="Citation for case: United States v. Bruce Christian Brown and James Patrick...">743 F. 2d 1505, 1507-1508</a></span> (CA11 1984);
   <em>
    United States
   </em>
   v.
   <em>
    Davis,
   </em>
   199 U. S. App. D. C. 95, 108, <span class="citation" data-id="375882"><a href="/opinion/375882/united-states-v-robert-h-davis-united-states-of-america-v-george-d/#690" aria-description="Citation for case: United States v. Robert H. Davis, United States of...">617 F. 2d 677, 690</a></span> (1979).
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/United States v. Patane.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Patane"
type: case
citation: "542 U.S. 630 (2004)"
parallel_cite: "124 S. Ct. 2620; 159 L. Ed. 2d 667"
neutral_cite: 2004 U.S. LEXIS 4577
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-06-28
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-06-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Patane
  varies_by_point: false
  scope_note: "Plurality opinion; Kennedy and O'Connor, JJ., concurred in the judgment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/137003/united-states-v-patane/"
  cluster_id: 137003
  opinion_id: 137003
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Oregon v. Elstad]]", "[[Dickerson v. United States]]", "[[Missouri v. Seibert]]", "[[New York v. Quarles]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "self-incrimination", "physical-fruits", "fruit-of-the-poisonous-tree"]
holding: "Physical fruits of an un-warned but voluntary statement are admissible."
lake:
  record_id: United States v. Patane
  status: verified
  projected_at: 2026-07-06
---

# United States v. Patane

*542 U.S. 630 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Patane was arrested in connection with a restraining-order violation. As an officer began to advise him of his *[[Miranda v. Arizona|Miranda]]* rights, Patane interrupted, saying he knew his rights, and the officer stopped. Patane then told the officers he had a Glock pistol in his bedroom. Because Patane was a convicted felon, the pistol supported a felon-in-possession charge. He moved to suppress the gun as the fruit of his unwarned statement. The Tenth Circuit ordered suppression; the Supreme Court reversed.

## Issue
Whether a failure to give *[[Miranda v. Arizona|Miranda]]* warnings requires suppression of the physical fruits — here, a pistol — of a suspect's unwarned but voluntary statements.

## Rule
No. The *[[Miranda v. Arizona|Miranda]]* rule is a prophylactic safeguard for the Self-Incrimination Clause, and that Clause is not violated by admitting the nontestimonial physical fruit of a voluntary statement. The plurality explained: "The Self-Incrimination Clause, however, is not implicated by the admission into evidence of the physical fruit of a voluntary statement. Accordingly, there is no justification for extending the *Miranda* rule to this context." — 542 U.S. at 636. ^pin-636

Because a mere failure to warn is not itself a constitutional violation, "the exclusionary rule articulated in cases such as *Wong Sun* does not apply." — *Id.* at 637. ^pin-637

## Application
Patane's statement about the Glock was voluntary, and the pistol was nontestimonial physical evidence. Admitting that physical fruit did not compel Patane to be a witness against himself, so the Self-Incrimination Clause was not violated and the failure to warn did not require suppressing the gun. The plurality observed that the case for admitting nontestimonial physical fruits (the Glock) was even stronger than the case for admitting the postwarning statements held admissible in *[[Oregon v. Elstad]]* and *[[Michigan v. Tucker]]*.

## Conclusion
The failure to give *[[Miranda v. Arizona|Miranda]]* warnings did not require suppression of the pistol; the Supreme Court reversed the Tenth Circuit and [[Reading and Citing Cases#on-remand|remanded]]. (Plurality opinion; Justices Kennedy and O'Connor concurred in the judgment, agreeing the gun need not be suppressed.)

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. Though a fractured plurality, *Patane*'s result controls: the physical fruits of an unwarned but voluntary statement are admissible. It refines the [[Oregon v. Elstad]] line and the constitutional-rule holding of [[Dickerson v. United States]], distinguishing the deliberate two-step problem addressed the same Term in [[Missouri v. Seibert]].

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Patane*, 542 U.S. 630 (2004) — https://www.courtlistener.com/opinion/137003/united-states-v-patane/ — pinpoints: 636, 637 (parallel 124 S. Ct. 2620).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3bb97dab6b914ee4", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "542 U.S. 630 (2004)", "court": "U.S. Supreme Court", "neutral_cite": "2004 U.S. LEXIS 4577", "official_citation_present": true, "parallel_cite": "124 S. Ct. 2620; 159 L. Ed. 2d 667", "title": "United States v. Patane", "year": "2004"}}
{"assertion_id": "3550fd52b6039674", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Physical fruits of an un-warned but voluntary statement are admissible.", "title": "United States v. Patane"}}
{"assertion_id": "f8a740dd0bed4753", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny / Refinement", "title": "United States v. Patane"}}
{"assertion_id": "3aaef6108c07ba57", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Patane"}}
{"assertion_id": "68c075419356c465", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2004-06-28", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Patane", "field_i_validity": "good_law", "scope_note": "Plurality opinion; Kennedy and O'Connor, JJ., concurred in the judgment.", "title": "United States v. Patane", "varies_by_point": "false"}}
```

### lake record — United States v. Patane

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Patane",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Patane",
    "case_name_short": "Patane",
    "case_name_full": "United States v. Patane",
    "input_case_name": "United States v. Patane",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-06-28",
    "year": 2004,
    "docket": null,
    "cluster_id": 137003,
    "lead_opinion_id": 137003,
    "sibling_ids": [
      137003,
      9434686,
      9434687,
      9434688,
      9434689
    ],
    "absolute_url": "/opinion/137003/united-states-v-patane/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "542 U.S. 630",
      "volume": "542",
      "reporter": "U.S.",
      "page": "630",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "124 S. Ct. 2620",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2620",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "159 L. Ed. 2d 667",
        "volume": "159",
        "reporter": "L. Ed. 2d",
        "page": "667",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 4577",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "4577",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "542 U.S. 630",
        "volume": "542",
        "reporter": "U.S.",
        "page": "630",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 2620",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2620",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "159 L. Ed. 2d 667",
        "volume": "159",
        "reporter": "L. Ed. 2d",
        "page": "667",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 4577",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "4577",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "542 U.S. 630",
    "official_selection": {
      "court_class": "scotus",
      "selected": "542 U.S. 630",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-636",
      "page": null,
      "quote": "--- # United States v. Patane *542 U.S. 630 (2004)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Patane was arrested in connection with a restraining-order violation. As an officer began to advise him of his *Miranda* rights, Patane interrupted, saying he knew his rights, and the officer stopped. Patane then told the officers he had a Glock pistol in his bedroom. Because Patane was a convicted felon, the pistol supported a felon-in-possession charge. He moved to suppress the gun as the fruit of his unwarned statement. The Tenth Circuit ordered suppression; the Supreme Court reversed. ## Issue Whether a failure to give *Miranda* warnings requires suppression of the physical fruits \u2014 here, a pistol \u2014 of a suspect's unwarned but voluntary statements. ## Rule No. The *Miranda* rule is a prophylactic safeguard for the Self-Incrimination Clause, and that Clause is not violated by admitting the nontestimonial physical fruit of a voluntary statement. The plurality explained:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-637",
      "page": null,
      "quote": "the exclusionary rule articulated in cases such as *Wong Sun* does not apply.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-06-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Patane",
    "varies_by_point": false,
    "scope_note": "Plurality opinion; Kennedy and O'Connor, JJ., concurred in the judgment.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Jenkins v. State",
          "cluster_id": 10680001,
          "cite": [
            "894 S.E.2d 566",
            "317 Ga. 585"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
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
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jones",
          "cluster_id": 4517594,
          "cite": [
            "193 A.3d 957"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cleveland v. Oles (Slip Opinion)",
          "cluster_id": 4410433,
          "cite": [
            "2017 Ohio 5834",
            "92 N.E.3d 810",
            "152 Ohio St. 3d 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
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
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "NYIA GORE v. UNITED STATES",
          "cluster_id": 4248978,
          "cite": [
            "145 A.3d 540",
            "2016 D.C. App. LEXIS 313",
            "2016 WL 4411321"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
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
        "journal_ref": "United States v. Patane:lane1_negative"
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
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In the Matter of J.T.M., a Juvenile",
          "cluster_id": 3076829,
          "cite": [
            "441 S.W.3d 455",
            "2014 WL 949949",
            "2014 Tex. App. LEXIS 2910"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. McCallum",
          "cluster_id": 2661991,
          "cite": [
            "885 F. Supp. 2d 105",
            "2012 WL 3289767"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
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
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Simon",
          "cluster_id": 2483876,
          "cite": [
            "456 Mass. 280",
            "923 N.E.2d 58",
            "2010 Mass. LEXIS 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
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
        "journal_ref": "United States v. Patane:lane1_negative"
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
        "journal_ref": "United States v. Patane:lane2_top_cited"
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
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "J. D. B. v. North Carolina",
          "cluster_id": 218925,
          "cite": [
            "180 L. Ed. 2d 310",
            "131 S. Ct. 2394",
            "564 U.S. 261",
            "2011 U.S. LEXIS 4557",
            "22 Fla. L. Weekly Fed. S 1135",
            "79 U.S.L.W. 4504"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Swain v. State",
          "cluster_id": 1490445,
          "cite": [
            "181 S.W.3d 359",
            "2005 Tex. Crim. App. LEXIS 1864",
            "2005 WL 2861584"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Davis",
          "cluster_id": 2575950,
          "cite": [
            "115 P.3d 417",
            "31 Cal. Rptr. 3d 96",
            "36 Cal. 4th 510",
            "2005 Cal. Daily Op. Serv. 6393",
            "2005 Daily Journal DAR 8733",
            "2005 Cal. LEXIS 7963"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salinas v. Texas",
          "cluster_id": 903977,
          "cite": [
            "186 L. Ed. 2d 376",
            "133 S. Ct. 2174",
            "2013 U.S. LEXIS 4697",
            "570 U.S. 178",
            "81 U.S.L.W. 4467",
            "24 Fla. L. Weekly Fed. S 294",
            "2013 WL 2922119"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People in the Interest of B.D",
          "cluster_id": 4611859,
          "cite": [
            "2019 COA 57"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. David Hooper Climer, Jr.",
          "cluster_id": 1043889,
          "cite": [
            "400 S.W.3d 537",
            "2013 WL 1694804",
            "2013 Tenn. LEXIS 354"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vega v. Tekoh",
          "cluster_id": 6480695,
          "cite": [
            "597 U.S. 134",
            "213 L. Ed. 2d 479",
            "142 S. Ct. 2095"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Knapp",
          "cluster_id": 1713730,
          "cite": [
            "2005 WI 127",
            "700 N.W.2d 899",
            "285 Wis. 2d 86",
            "2005 Wisc. LEXIS 395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Desmond v. Mukasey",
          "cluster_id": 187228,
          "cite": [
            "530 F.3d 944",
            "382 U.S. App. D.C. 31",
            "20 Am. Disabilities Cas. (BNA) 1291",
            "2008 U.S. App. LEXIS 13803",
            "2008 WL 2583022"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chamberlin v. State",
          "cluster_id": 1638526,
          "cite": [
            "989 So. 2d 320",
            "2008 WL 2761889"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clay v. State",
          "cluster_id": 2506826,
          "cite": [
            "725 S.E.2d 260",
            "290 Ga. 822",
            "2012 Fulton County D. Rep. 982",
            "2012 Ga. LEXIS 301"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Timothy Stewart",
          "cluster_id": 788327,
          "cite": [
            "388 F.3d 1079",
            "2004 U.S. App. LEXIS 23395",
            "2004 WL 2523358"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. O'NEILL",
          "cluster_id": 1946717,
          "cite": [
            "936 A.2d 438",
            "193 N.J. 148",
            "2007 N.J. LEXIS 1507"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Santiago",
          "cluster_id": 2306570,
          "cite": [
            "980 A.2d 659",
            "2009 Pa. Super. 169",
            "2009 Pa. Super. LEXIS 3268",
            "2009 WL 2634846"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carrizales-Toledo",
          "cluster_id": 167815,
          "cite": [
            "454 F.3d 1142",
            "2006 U.S. App. LEXIS 18280",
            "2006 WL 2022911"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Larry D. Peterson and Larry D. Willis",
          "cluster_id": 790977,
          "cite": [
            "414 F.3d 825",
            "2005 U.S. App. LEXIS 14431",
            "2005 WL 1661259"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Pettigrew",
          "cluster_id": 167856,
          "cite": [
            "468 F.3d 626",
            "2006 U.S. App. LEXIS 28128",
            "2006 WL 2946893"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Vondehn",
          "cluster_id": 835033,
          "cite": [
            "236 P.3d 691",
            "348 Or. 462",
            "2010 Ore. LEXIS 504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Mole (Slip Opinion)",
          "cluster_id": 4242422,
          "cite": [
            "2016 Ohio 5124",
            "149 Ohio St. 3d 215",
            "74 N.E.3d 368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Vance",
          "cluster_id": 2277859,
          "cite": [
            "188 Cal. App. 4th 1182",
            "116 Cal. Rptr. 3d 98",
            "2010 Cal. App. LEXIS 1691"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Welch v. Commonwealth",
          "cluster_id": 1793000,
          "cite": [
            "149 S.W.3d 407",
            "2004 Ky. LEXIS 276",
            "2004 WL 2623964"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Johnson",
          "cluster_id": 2282662,
          "cite": [
            "183 Cal. App. 4th 253",
            "107 Cal. Rptr. 3d 228",
            "2010 Cal. App. LEXIS 429"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Popenhagen",
          "cluster_id": 1917034,
          "cite": [
            "2008 WI 55",
            "749 N.W.2d 611",
            "309 Wis. 2d 601",
            "2008 Wisc. LEXIS 307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(137003 OR 9434686 OR 9434687 OR 9434688 OR 9434689) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTkwODUxMjAwMDAwJnM9MTQ3NzQ3NCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28137003+OR+9434686+OR+9434687+OR+9434688+OR+9434689%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 13,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(137003 OR 9434686 OR 9434687 OR 9434688 OR 9434689)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NCZzPTg5NDk4NSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28137003+OR+9434686+OR+9434687+OR+9434688+OR+9434689%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(137003 OR 9434686 OR 9434687 OR 9434688 OR 9434689)",
        "reviewed": 30,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 30,
        "triage_read": 1,
        "triage_snippet_classified": 29
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(137003 OR 9434686 OR 9434687 OR 9434688 OR 9434689)",
    "indexed_citing_opinions": 344,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 137003,
        "count": 276,
        "count_source": "search"
      },
      {
        "opinion_id": 9434686,
        "count": 75,
        "count_source": "search"
      },
      {
        "opinion_id": 9434687,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434688,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434689,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 620,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-patane.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1NDI3OCZzPTk0NDMzMzUmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28137003+OR+9434686+OR+9434687+OR+9434688+OR+9434689%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 137003,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 107739,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 109432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 110038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 111105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 112057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 112382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 112847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 117843,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 118242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 127927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 162589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 200020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 775633,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 776886,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 783781,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 1087666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 2021779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 2125014,
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
    "date_created": "2026-07-06T02:07:43Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:07:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:07:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:12:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:07:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Patane

```
<div>
<center><b><span class="citation" data-id="9434686"><a href="/opinion/137003/united-states-v-patane/" aria-description="Citation for case: United States v. Patane">542 U.S. 630</a></span> (2004)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
PATANE</h1></center>
<center>No. 02-1183.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 9, 2003.</center>
<center>Decided June 28, 2004.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE TENTH CIRCUIT.
<p><span class="star-pagination">*631</span> <span class="star-pagination">*632</span> <span class="star-pagination">*633</span> THOMAS, J., announced the judgment of the Court and delivered an opinion, in which REHNQUIST, C. J., and SCALIA, J., joined. KENNEDY, J., filed an opinion concurring in the judgment, in which O'CONNOR, J., joined, <i>post,</i> p. 644. SOUTER, J., filed a dissenting opinion, in which STEVENS and GINSBURG, JJ., joined, <i>post,</i> p. 645. BREYER, J., filed a dissenting opinion, <i>post,</i> p. 647.</p>
<p><i>Deputy Solicitor General Dreeben</i> argued the cause for petitioner. With him on the briefs were <i>Solicitor General Olson, Acting Assistant Attorney General Wray, James A. Feldman,</i> and <i>Joseph C. Wyderko.</i></p>
<p><i>Jill M. Wichlens</i> argued the cause for respondent. With her on the brief were <i>Michael G. Katz</i> and <i>Virginia L. Grady.</i><sup>[*]</sup></p>
<p>JUSTICE THOMAS announced the judgment of the Court and delivered an opinion, in which THE CHIEF JUSTICE and JUSTICE SCALIA join.</p>
<p>In this case we must decide whether a failure to give a suspect the warnings prescribed by <i>Miranda</i> v. <i>Arizona,</i> <span class="star-pagination">*634</span> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), requires suppression of the physical fruits of the suspect's unwarned but voluntary statements. The Court has previously addressed this question but has not reached a definitive conclusion. See <i>Massachusetts</i> v. <i>White,</i> <span class="citation" data-id="9011990"><a href="/opinion/9018794/massachusetts-v-white/" aria-description="Citation for case: Massachusetts v. White">439 U. S. 280</a></span> (1978) <i>(per curiam)</i> (dividing evenly on the question); see also <i>Patterson</i> v. <i>United States,</i> <span class="citation" data-id="9431278"><a href="/opinion/112057/patterson-v-united-states/" aria-description="Citation for case: Patterson v. United States">485 U. S. 922</a></span> (1988) (White, J., dissenting from denial of certiorari). Although we believe that the Court's decisions in <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), and <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433</a></span> (1974), are instructive, the Courts of Appeals have split on the question after our decision in <i>Dickerson</i> v. <i>United States,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428</a></span> (2000). See, <i>e. g., </i><i>United States</i> v. <i>Villalba-Alvarado,</i> <span class="citation" data-id="9496439"><a href="/opinion/783781/united-states-v-angel-benito-villalba-alvarado-aka-benito-angel-alvara/" aria-description="Citation for case: United States v. Angel Benito Villalba-Alvarado, A/K/A...">345 F. 3d 1007</a></span> (CA8 2003) (holding admissible the physical fruits of a <i>Miranda</i> violation); <i>United States</i> v. <i>Sterling,</i> <span class="citation" data-id="776886"><a href="/opinion/776886/united-states-v-ricky-g-sterling/" aria-description="Citation for case: United States v. Ricky G. Sterling">283 F. 3d 216</a></span> (CA4 2002) (same); <i>United States</i> v. <i>DeSumma,</i> <span class="citation" data-id="775633"><a href="/opinion/775633/united-states-v-frank-desumma-aka-doc-frank-desumma/" aria-description="Citation for case: United States v. Frank Desumma, A/K/A Doc, Frank Desumma">272 F. 3d 176</a></span> (CA3 2001) (same); <i>United States</i> v. <i>Faulkingham,</i> <span class="citation" data-id="200020"><a href="/opinion/200020/united-states-v-faulkingham/" aria-description="Citation for case: United States v. Faulkingham">295 F. 3d 85</a></span> (CA1 2002) (holding admissible the physical fruits of a negligent <i>Miranda</i> violation). Because the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule protects against violations of the Self-Incrimination Clause, which, in turn, is not implicated by the introduction at trial of physical evidence resulting from voluntary statements, we answer the question presented in the negative.</p>
<p></p>
<h2>I</h2>
<p>In June 2001, respondent, Samuel Francis Patane, was arrested for harassing his ex-girlfriend, Linda O'Donnell. He was released on bond, subject to a temporary restraining order that prohibited him from contacting O'Donnell. Respondent apparently violated the restraining order by attempting to telephone O'Donnell. On June 6, 2001, Officer Tracy Fox of the Colorado Springs Police Department began to investigate the matter. On the same day, a county probation officer informed an agent of the Bureau of Alcohol, Tobacco, and Firearms (ATF), that respondent, a convicted felon, illegally possessed a .40 Glock pistol. The ATF relayed this information to Detective Josh Benner, who worked <span class="star-pagination">*635</span> closely with the ATF. Together, Detective Benner and Officer Fox proceeded to respondent's residence.</p>
<p>After reaching the residence and inquiring into respondent's attempts to contact O'Donnell, Officer Fox arrested respondent for violating the restraining order. Detective Benner attempted to advise respondent of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights but got no further than the right to remain silent. At that point, respondent interrupted, asserting that he knew his rights, and neither officer attempted to complete the warning.<sup>[1]</sup> App. 40.</p>
<p>Detective Benner then asked respondent about the Glock. Respondent was initially reluctant to discuss the matter, stating: "I am not sure I should tell you anything about the Glock because I don't want you to take it away from me." <i>Id.,</i> at 41. Detective Benner persisted, and respondent told him that the pistol was in his bedroom. Respondent then gave Detective Benner permission to retrieve the pistol. Detective Benner found the pistol and seized it.</p>
<p>A grand jury indicted respondent for possession of a firearm by a convicted felon, in violation of <span class="citation no-link">18 U. S. C. § 922</span>(g)(1). The District Court granted respondent's motion to suppress the firearm, reasoning that the officers lacked probable cause to arrest respondent for violating the restraining order. It therefore declined to rule on respondent's alternative argument that the gun should be suppressed as the fruit of an unwarned statement.</p>
<p>The Court of Appeals reversed the District Court's ruling with respect to probable cause but affirmed the suppression order on respondent's alternative theory. The court rejected the Government's argument that this Court's decisions in <i><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad, supra,</a></span></i> and <i><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker, supra,</a></span></i> foreclosed application of the fruit of the poisonous tree doctrine of <i>Wong Sun</i> <span class="star-pagination">*636</span> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), to the present context. <span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/#1019" aria-description="Citation for case: United States v. Patane">304 F. 3d 1013, 1019</a></span> (CA10 2002). These holdings were, the Court of Appeals reasoned, based on the view that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> announced a prophylactic rule, a position that it found to be incompatible with this Court's decision in <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#444" aria-description="Citation for case: Dickerson v. United States"><i>Dickerson, supra,</i> at 444</a></span> ("<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> announced a constitutional rule that Congress may not supersede legislatively").<sup>[2]</sup> The Court of Appeals thus equated <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span></i>'s announcement that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is a constitutional rule with the proposition that a failure to warn pursuant to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is itself a violation of the Constitution (and, more particularly, of the suspect's Fifth Amendment rights). Based on its understanding of <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span>,</i> the Court of Appeals rejected the post-<span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States"><i>Dickerson</i></a></span> views of the Third and Fourth Circuits that the fruits doctrine does not apply to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violations. <span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/#1023" aria-description="Citation for case: United States v. Patane">304 F. 3d, at 1023-1027</a></span> (discussing <i>United States</i> v. <i>Sterling,</i> <span class="citation" data-id="776886"><a href="/opinion/776886/united-states-v-ricky-g-sterling/" aria-description="Citation for case: United States v. Ricky G. Sterling">283 F. 3d 216</a></span> (CA4 2002), and <i>United States</i> v. <i>DeSumma,</i> <span class="citation" data-id="775633"><a href="/opinion/775633/united-states-v-frank-desumma-aka-doc-frank-desumma/" aria-description="Citation for case: United States v. Frank Desumma, A/K/A Doc, Frank Desumma">272 F. 3d 176</a></span> (CA3 2001)). It also disagreed with the First Circuit's conclusion that suppression is not generally required in the case of negligent failures to warn, <span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/#1027" aria-description="Citation for case: United States v. Patane">304 F. 3d, at 1027-1029</a></span> (discussing <i>United States</i> v. <i>Faulkingham,</i> <span class="citation" data-id="200020"><a href="/opinion/200020/united-states-v-faulkingham/" aria-description="Citation for case: United States v. Faulkingham">295 F. 3d 85</a></span> (CA1 2002)), explaining that "[d]eterrence is necessary not merely to deter intentional wrongdoing, but also to ensure that officers diligently (non-negligently) protect  and properly are trained to protect  the constitutional rights of citizens," <span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/#1028" aria-description="Citation for case: United States v. Patane">304 F. 3d, at 1028-1029</a></span>. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./538/976/">538 U. S. 976</a></span> (2003).</p>
<p>As we explain below, the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule is a prophylactic employed to protect against violations of the Self-Incrimination Clause. The Self-Incrimination Clause, however, is not implicated by the admission into evidence of the physical fruit of a voluntary statement. Accordingly, there is no justification for extending the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule to this context. <span class="star-pagination">*637</span> And just as the Self-Incrimination Clause primarily focuses on the criminal trial, so too does the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule. The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule is not a code of police conduct, and police do not violate the Constitution (or even the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule, for that matter) by mere failures to warn. For this reason, the exclusionary rule articulated in cases such as <i>Wong Sun</i> does not apply. Accordingly, we reverse the judgment of the Court of Appeals and remand the case for further proceedings.</p>
<p></p>
<h2>II</h2>
<p>The Self-Incrimination Clause provides: "No person . . . shall be compelled in any criminal case to be a witness against himself." U. S. Const., Amdt. 5. We need not decide here the precise boundaries of the Clause's protection. For present purposes, it suffices to note that the core protection afforded by the Self-Incrimination Clause is a prohibition on compelling a criminal defendant to testify against himself at trial. See, <i>e. g., </i><i>Chavez</i> v. <i>Martinez,</i> <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#764" aria-description="Citation for case: Chavez v. Martinez">538 U. S. 760, 764-768</a></span> (2003) (plurality opinion); <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#777" aria-description="Citation for case: Chavez v. Martinez"><i>id.,</i> at 777-779</a></span> (SOUTER, J., concurring in judgment); 8 J. Wigmore, Evidence § 2263, p. 378 (J. McNaughton rev. ed. 1961) (explaining that the Clause "was directed at the employment of legal process to <i>extract from the person's own lips</i> an admission of guilt, which would thus take the place of other evidence"); see also <i>United States</i> v. <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#49" aria-description="Citation for case: United States v. Hubbell">530 U. S. 27, 49-56</a></span> (2000) (THOMAS, J., concurring) (explaining that the privilege might extend to bar the compelled production of any incriminating evidence, testimonial or otherwise). The Clause cannot be violated by the introduction of nontestimonial evidence obtained as a result of voluntary statements. See, <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#34" aria-description="Citation for case: United States v. Hubbell"><i>e. g., id.,</i> at 34</a></span> (noting that the word "`witness'" in the Self-Incrimination Clause "limits the relevant category of compelled incriminating communications to those that are `testimonial' in character"); <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#35" aria-description="Citation for case: United States v. Hubbell"><i>id.,</i> at 35</a></span> (discussing why compelled blood samples do not violate the Clause; cataloging other examples and citing cases); <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#304" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 304</a></span> ("The Fifth Amendment, of <span class="star-pagination">*638</span> course, is not concerned with nontestimonial evidence"); <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#306" aria-description="Citation for case: Oregon v. Elstad"><i>id.,</i> at 306-307</a></span> ("The Fifth Amendment prohibits use by the prosecution in its case in chief only of <i>compelled</i> testimony"); <i>Withrow</i> v. <i>Williams,</i> <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#705" aria-description="Citation for case: Withrow v. Williams">507 U. S. 680, 705</a></span> (1993) (O'CONNOR, J., concurring in part and dissenting in part) (describing "<i>true</i> Fifth Amendment claims [as] the extraction and use of <i>compelled</i> testimony"); <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#665" aria-description="Citation for case: New York v. Quarles">467 U. S. 649, 665-672</a></span>, and n. 4 (1984) (O'CONNOR, J., concurring in judgment in part and dissenting in part) (explaining that the physical fruit of a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation need not be suppressed for these reasons).</p>
<p>To be sure, the Court has recognized and applied several prophylactic rules designed to protect the core privilege against self-incrimination. See, <i>e. g., </i><span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#770" aria-description="Citation for case: Chavez v. Martinez"><i>Chavez, supra,</i> at 770-772</a></span> (plurality opinion). For example, although the text of the Self-Incrimination Clause at least suggests that "its coverage [is limited to] compelled testimony that is used against the defendant in the trial itself," <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#37" aria-description="Citation for case: United States v. Hubbell"><i>Hubbell, supra,</i> at 37</a></span>, potential suspects may, at times, assert the privilege in proceedings in which answers might be used to incriminate them in a subsequent criminal case. See, <i>e. g., </i><i>United States</i> v. <i>Balsys,</i> <span class="citation" data-id="9433709"><a href="/opinion/118242/united-states-v-balsys/#671" aria-description="Citation for case: United States v. Balsys">524 U. S. 666, 671-672</a></span> (1998); <i>Minnesota</i> v. <i>Murphy,</i> <span class="citation" data-id="9429504"><a href="/opinion/111105/minnesota-v-murphy/#426" aria-description="Citation for case: Minnesota v. Murphy">465 U. S. 420, 426</a></span> (1984); cf. <i>Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441</a></span> (1972) (holding that the Government may compel grand jury testimony from witnesses over Fifth Amendment objections if the witnesses receive "use and derivative use immunity"); <i>Uniformed Sanitation Men Assn., Inc.</i> v. <i>Commissioner of Sanitation of City of New York,</i> <span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/#284" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">392 U. S. 280, 284</a></span> (1968) (allowing the Government to use economic compulsion to secure statements but only if the Government grants appropriate immunity). We have explained that "[t]he natural concern which underlies [these] decisions is that an inability to protect the right at one stage of a proceeding may make its invocation useless at a later stage." <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#440" aria-description="Citation for case: Michigan v. Tucker">417 U. S., at 440-441</a></span>.</p>
<p><span class="star-pagination">*639</span> Similarly, in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the Court concluded that the possibility of coercion inherent in custodial interrogations unacceptably raises the risk that a suspect's privilege against self-incrimination might be violated. See <i>Dickerson,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#434" aria-description="Citation for case: Dickerson v. United States">530 U. S., at 434-435</a></span>; <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>. To protect against this danger, the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule creates a presumption of coercion, in the absence of specific warnings, that is generally irrebuttable for purposes of the prosecution's case in chief.</p>
<p>But because these prophylactic rules (including the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule) necessarily sweep beyond the actual protections of the Self-Incrimination Clause, see, <i>e. g., </i><span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#690" aria-description="Citation for case: Withrow v. Williams"><i>Withrow, supra,</i> at 690-691</a></span>; <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#306" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 306</a></span>, any further extension of these rules must be justified by its necessity for the protection of the actual right against compelled self-incrimination, <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#778" aria-description="Citation for case: Chavez v. Martinez"><i>Chavez, supra,</i> at 778</a></span> (SOUTER, J., concurring in judgment) (requiring a "`powerful showing'" before "expand[ing] . . . the privilege against compelled self-incrimination"). Indeed, at times the Court has declined to extend <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> even where it has perceived a need to protect the privilege against self-incrimination. See, <i>e. g., </i><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#657" aria-description="Citation for case: New York v. Quarles"><i>Quarles, supra,</i> at 657</a></span> (concluding "that the need for answers to questions in a situation posing a threat to the public safety outweighs the need for the prophylactic rule protecting the Fifth Amendment's privilege against self-incrimination").</p>
<p>It is for these reasons that statements taken without <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings (though not actually compelled) can be used to impeach a defendant's testimony at trial, see <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#307" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 307-308</a></span>; <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971), though the fruits of actually compelled testimony cannot, see <i>New Jersey</i> v. <i>Portash,</i> <span class="citation" data-id="9427490"><a href="/opinion/110038/new-jersey-v-portash/#458" aria-description="Citation for case: New Jersey v. Portash">440 U. S. 450, 458-459</a></span> (1979). More generally, the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule "does not require that the statements [taken without complying with the rule] and their fruits be discarded as inherently tainted," <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#307" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 307</a></span>. Such a blanket suppression rule could not be justified <span class="star-pagination">*640</span> by reference to the "Fifth Amendment goal of assuring trustworthy evidence" or by any deterrence rationale, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#308" aria-description="Citation for case: Oregon v. Elstad"><i>id.,</i> at 308</a></span>; see <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#446" aria-description="Citation for case: Michigan v. Tucker"><i>Tucker, supra,</i> at 446-449</a></span>; <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#225" aria-description="Citation for case: Harris v. New York"><i>Harris, supra,</i> at 225-226</a></span>, and n. 2, and would therefore fail our close-fit requirement.</p>
<p>Furthermore, the Self-Incrimination Clause contains its own exclusionary rule. It provides that "[n]o person . . . shall be compelled in any criminal case to be a witness against himself." Amdt. 5. Unlike the Fourth Amendment's bar on unreasonable searches, the Self-Incrimination Clause is self-executing. We have repeatedly explained "that those subjected to coercive police interrogations have an <i>automatic</i> protection from the use of their involuntary statements (or evidence derived from their statements) in any subsequent criminal trial." <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#769" aria-description="Citation for case: Chavez v. Martinez"><i>Chavez, supra,</i> at 769</a></span> (plurality opinion) (citing, for example, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#307" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 307-308</a></span>). This explicit textual protection supports a strong presumption against expanding the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule any further. Cf. <i>Graham</i> v. <i>Connor,</i> <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U. S. 386</a></span> (1989).</p>
<p>Finally, nothing in <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span>,</i> including its characterization of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> as announcing a constitutional rule, 530 U. S., at 444, changes any of these observations. Indeed, in <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span>,</i> the Court specifically noted that the Court's "subsequent cases have reduced the impact of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule on legitimate law enforcement while reaffirming <i>[Miranda]</i>'s core ruling that unwarned statements may not be used as evidence in the prosecution's case in chief." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#443" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 443-444</a></span>. This description of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> especially the emphasis on the use of "unwarned statements . . . in the prosecution's case in chief," makes clear our continued focus on the protections of the Self-Incrimination Clause. The Court's reliance on our <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> precedents, including both <i><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span></i> and <i><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>,</i> see, <i>e. g., </i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#438" aria-description="Citation for case: Dickerson v. United States"><i>Dickerson, supra,</i> at 438, 441</a></span>, further demonstrates the continuing validity of those decisions. In short, nothing in <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span></i> calls into question our continued <span class="star-pagination">*641</span> insistence that the closest possible fit be maintained between the Self-Incrimination Clause and any rule designed to protect it.</p>
<p></p>
<h2>III</h2>
<p>Our cases also make clear the related point that a mere failure to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings does not, by itself, violate a suspect's constitutional rights or even the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule. So much was evident in many of our pre-<span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States"><i>Dickerson</i></a></span> cases, and we have adhered to this view since <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span>.</i> See <i>Chavez,</i> <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#772" aria-description="Citation for case: Chavez v. Martinez">538 U. S., at 772-773</a></span> (plurality opinion) (holding that a failure to read <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings did not violate the respondent's constitutional rights); <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#789" aria-description="Citation for case: Chavez v. Martinez">538 U. S., at 789</a></span> (KENNEDY, J., concurring in part and dissenting in part) (agreeing "that failure to give a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning does not, without more, establish a completed violation when the unwarned interrogation ensues"); <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#308" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 308</a></span>; <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles">467 U. S., at 654</a></span>; cf. <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#777" aria-description="Citation for case: Chavez v. Martinez"><i>Chavez, supra,</i> at 777-779</a></span> (SOUTER, J., concurring in judgment). This, of course, follows from the nature of the right protected by the Self-Incrimination Clause, which the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule, in turn, protects. It is "`a fundamental <i>trial</i> right.'" <i>Withrow,</i> <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/" aria-description="Citation for case: Withrow v. Williams">507 U. S., at 691</a></span> (quoting <i>United States</i> v. <i>Verdugo-Urquidez,</i> <span class="citation" data-id="9431925"><a href="/opinion/112382/united-states-v-verdugo-urquidez/#264" aria-description="Citation for case: United States v. Verdugo-Urquidez">494 U. S. 259, 264</a></span> (1990)). See also <i>Chavez,</i> <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#766" aria-description="Citation for case: Chavez v. Martinez">538 U. S., at 766-768</a></span> (plurality opinion); <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#790" aria-description="Citation for case: Chavez v. Martinez"><i>id.,</i> at 790</a></span> (KENNEDY, J., concurring in part and dissenting in part) ("The identification of a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation and its consequences, then, ought to be determined at trial").</p>
<p>It follows that police do not violate a suspect's constitutional rights (or the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule) by negligent or even deliberate failures to provide the suspect with the full panoply of warnings prescribed by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> Potential violations occur, if at all, only upon the admission of unwarned statements into evidence at trial. And, at that point, "[t]he exclusion of unwarned statements ... is a complete and sufficient <span class="star-pagination">*642</span> remedy" for any perceived <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation. <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#790" aria-description="Citation for case: Chavez v. Martinez"><i>Chavez, supra,</i> at 790</a></span>.<sup>[3]</sup></p>
<p>Thus, unlike unreasonable searches under the Fourth Amendment or actual violations of the Due Process Clause or the Self-Incrimination Clause, there is, with respect to mere failures to warn, nothing to deter. There is therefore no reason to apply the "fruit of the poisonous tree" doctrine of <i>Wong Sun,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 488</a></span>.<sup>[4]</sup> See also <i>Nix</i> v. <i>Williams,</i> <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#441" aria-description="Citation for case: Nix v. Williams">467 U. S. 431, 441</a></span> (1984) (discussing the exclusionary rule in the Sixth Amendment context and noting that it applies to "<i>illegally</i> obtained evidence [and] other incriminating evidence derived from [it]" (emphasis added)). It is not for this Court to impose its preferred police practices on either federal law enforcement officials or their state counterparts.</p>
<p></p>
<h2>IV</h2>
<p>In the present case, the Court of Appeals, relying on <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span>,</i> wholly adopted the position that the taking of unwarned statements violates a suspect's constitutional rights. <span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/#1028" aria-description="Citation for case: United States v. Patane">304 F. 3d, at 1028-1029</a></span>.<sup>[5]</sup> And, of course, if this were so, a <span class="star-pagination">*643</span> strong deterrence-based argument could be made for suppression of the fruits. See, <i>e. g., </i><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#441" aria-description="Citation for case: Nix v. Williams"><i>Nix, supra,</i> at 441-444</a></span>; <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#484" aria-description="Citation for case: Wong Sun v. United States"><i>Wong Sun, supra,</i> at 484-486</a></span>; cf. <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span> (1939).</p>
<p>But <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span></i>'s characterization of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> as a constitutional rule does not lessen the need to maintain the closest possible fit between the Self-Incrimination Clause and any judge-made rule designed to protect it. And there is no such fit here. Introduction of the nontestimonial fruit of a voluntary statement, such as respondent's Glock, does not implicate the Self-Incrimination Clause. The admission of such fruit presents no risk that a defendant's coerced statements (however defined) will be used against him at a criminal trial. In any case, "[t]he exclusion of unwarned statements . . . is a complete and sufficient remedy" for any perceived <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation. <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#790" aria-description="Citation for case: Chavez v. Martinez"><i>Chavez, supra,</i> at 790</a></span> (KENNEDY, J., concurring in part and dissenting in part). See also H. Friendly, Benchmarks 280-281 (1967). There is simply no need to extend (and therefore no justification for extending) the prophylactic rule of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to this context.</p>
<p>Similarly, because police cannot violate the Self-Incrimination Clause by taking unwarned though voluntary statements, an exclusionary rule cannot be justified by reference to a deterrence effect on law enforcement, as the Court of Appeals believed, <span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/#1028" aria-description="Citation for case: United States v. Patane">304 F. 3d, at 1028-1029</a></span>. Our decision not to apply <i>Wong Sun</i> to mere failures to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings was sound at the time <i><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span></i> and <i><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span></i> were decided, and we decline to apply <i>Wong Sun</i> to such failures now.</p>
<p>The Court of Appeals ascribed significance to the fact that, in this case, there might be "little [practical] difference between [respondent's] confessional statement" and the actual physical evidence. <span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/#1027" aria-description="Citation for case: United States v. Patane">304 F. 3d, at 1027</a></span>. The distinction, the court said, "appears to make little sense as a matter of policy." <i><span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/" aria-description="Citation for case: United States v. Patane">Ibid.</a></span></i> But, putting policy aside, we have held that "[t]he word `witness' in the constitutional text limits the" <span class="star-pagination">*644</span> scope of the Self-Incrimination Clause to testimonial evidence. <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#34" aria-description="Citation for case: United States v. Hubbell">530 U. S., at 34-35</a></span>. The Constitution itself makes the distinction.<sup>[6]</sup> And although it is true that the Court requires the exclusion of the physical fruit of actually coerced statements, it must be remembered that statements taken without sufficient <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are presumed to have been coerced only for certain purposes and then only when necessary to protect the privilege against self-incrimination. See Part II, <i>supra.</i> For the reasons discussed above, we decline to extend that presumption further.<sup>[7]</sup></p>
<p>Accordingly, we reverse the judgment of the Court of Appeals and remand the case for further proceedings.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE KENNEDY, with whom JUSTICE O'CONNOR joins, concurring in the judgment.</p>
<p>In <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U. S. 649</a></span> (1984), and <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971), evidence obtained following an unwarned interrogation was held admissible. This result was based in large part on our recognition that the concerns underlying the <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), rule must be accommodated to other objectives of the criminal justice system. <span class="star-pagination">*645</span> I agree with the plurality that <i>Dickerson</i> v. <i>United States,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428</a></span> (2000), did not undermine these precedents and, in fact, cited them in support. Here, it is sufficient to note that the Government presents an even stronger case for admitting the evidence obtained as the result of Patane's unwarned statement. Admission of nontestimonial physical fruits (the Glock in this case), even more so than the postwarning statements to the police in <i><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span></i> and <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433</a></span> (1974), does not run the risk of admitting into trial an accused's coerced incriminating statements against himself. In light of the important probative value of reliable physical evidence, it is doubtful that exclusion can be justified by a deterrence rationale sensitive to both law enforcement interests and a suspect's rights during an in-custody interrogation. Unlike the plurality, however, I find it unnecessary to decide whether the detective's failure to give Patane the full <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings should be characterized as a violation of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule itself, or whether there is "[any]thing to deter" so long as the unwarned statements are not later introduced at trial. <i>Ante,</i> at 641-642.</p>
<p>With these observations, I concur in the judgment of the Court.</p>
<p>JUSTICE SOUTER, with whom JUSTICE STEVENS and JUSTICE GINSBURG join, dissenting.</p>
<p>The plurality repeatedly says that the Fifth Amendment does not address the admissibility of nontestimonial evidence, an overstatement that is beside the point. The issue actually presented today is whether courts should apply the fruit of the poisonous tree doctrine lest we create an incentive for the police to omit <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, see <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), before custodial interrogation.<sup>[1]</sup><span class="star-pagination">*646</span> In closing their eyes to the consequences of giving an evidentiary advantage to those who ignore <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the plurality adds an important inducement for interrogators to ignore the rule in that case.</p>
<p><i>Miranda</i> rested on insight into the inherently coercive character of custodial interrogation and the inherently difficult exercise of assessing the voluntariness of any confession resulting from it. Unless the police give the prescribed warnings meant to counter the coercive atmosphere, a custodial confession is inadmissible, there being no need for the previous time-consuming and difficult enquiry into voluntariness. That inducement to forestall involuntary statements and troublesome issues of fact can only atrophy if we turn around and recognize an evidentiary benefit when an unwarned statement leads investigators to tangible evidence. There is, of course, a price for excluding evidence, but the Fifth Amendment is worth a price, and in the absence of a very good reason, the logic of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> should be followed: a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation raises a presumption of coercion, <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#306" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 306-307</a></span>, and n. 1 (1985), and the Fifth Amendment privilege against compelled self-incrimination extends to the exclusion of derivative evidence, see <i>United States</i> v. <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#37" aria-description="Citation for case: United States v. Hubbell">530 U. S. 27, 37-38</a></span> (2000) (recognizing "the Fifth Amendment's protection against the prosecutor's use of incriminating information derived directly or indirectly from ... [actually] compelled testimony"); <i>Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#453" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 453</a></span> (1972). That should be the end of this case.</p>
<p>The fact that the books contain some exceptions to the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> exclusionary rule carries no weight here. In <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971), it was respect for the integrity of the judicial process that justified the admission <span class="star-pagination">*647</span> of unwarned statements as impeachment evidence. But Patane's suppression motion can hardly be described as seeking to "perver[t]" <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> "into a license to use perjury" or otherwise handicap the "traditional truth-testing devices of the adversary process." <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#225" aria-description="Citation for case: Harris v. New York">401 U. S., at 225-226</a></span>. Nor is there any suggestion that the officers' failure to warn Patane was justified or mitigated by a public emergency or other exigent circumstance, as in <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U. S. 649</a></span> (1984). And of course the premise of <i>Oregon</i> v. <i><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad, supra</a></span></i><i>,</i> is not on point; although a failure to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings before one individual statement does not necessarily bar the admission of a subsequent statement given after adequate warnings, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span>; cf. <i>Missouri</i> v. <i>Seibert, ante,</i> at 614-615 (plurality opinion), that rule obviously does not apply to physical evidence seized once and for all.<sup>[2]</sup></p>
<p>There is no way to read this case except as an unjustifiable invitation to law enforcement officers to flout <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> when there may be physical evidence to be gained. The incentive is an odd one, coming from the Court on the same day it decides <i>Missouri</i> v. <i>Seibert, ante,</i> p. 600. I respectfully dissent.</p>
<p>JUSTICE BREYER, dissenting.</p>
<p>For reasons similar to those set forth in JUSTICE SOUTER's dissent and in my concurring opinion in <i>Missouri</i> v. <i>Seibert, ante,</i> at 617, I would extend to this context the "fruit of the poisonous tree" approach, which I believe the Court has come close to adopting in <i>Seibert.</i> Under that approach, <span class="star-pagination">*648</span> courts would exclude physical evidence derived from unwarned questioning unless the failure to provide <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), warnings was in good faith. See <i>Seibert, ante,</i> at 617-618 (BREYER, J., concurring); cf. <i>ante,</i> at 645-646, n. 1 (SOUTER, J., dissenting). Because the courts below made no explicit finding as to good or bad faith, I would remand for such a determination.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the State of Alabama et al. by <i>William H. Pryor, Jr.,</i> Attorney General of Alabama, <i>Nathan A. Forrester,</i> Solicitor General, <i>Michael B. Billingsley,</i> Deputy Solicitor General, <i>Marc A. Starrett,</i> Assistant Attorney General, and by the Attorneys General for their respective States as follows: <i>M. Jane Brady</i> of Delaware, <i>Charles J. Crist, Jr.,</i> of Florida, <i>Mark J. Bennett</i> of Hawaii, <i>Lisa Madigan</i> of Illinois, <i>Steve Carter</i> of Indiana, <i>Mike McGrath</i> of Montana, <i>Jim Petro</i> of Ohio, <i>D. Michael Fisher</i> of Pennsylvania, <i>Lawrence E. Long</i> of South Dakota, <i>Paul G. Summers</i> of Tennessee, <i>Greg Abbott</i> of Texas, <i>Mark L. Shurtleff</i> of Utah, <i>William H. Sorrell</i> of Vermont, <i>Jerry W. Kilgore</i> of Virginia, <i>Peggy A. Lautenschlager</i> of Wisconsin, and <i>Patrick J. Crank</i> of Wyoming; and for the Criminal Justice Legal Foundation by <i>Kent S. Scheidegger.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the Brennan Center for Justice by <i>Stephen J. Schulhofer, Frederick A. O. Schwarz, Jr., Tom Gerety,</i> and <i>E. Joshua Rosenkranz;</i> and for the National Association of Criminal Defense Lawyers et al. by <i>James J. Tomkovicz, David M. Porter,</i> and <i>Steven R. Shapiro.</i></p>
<p>[1]  The Government concedes that respondent's answers to subsequent on-the-scene questioning are inadmissible at trial under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), despite the partial warning and respondent's assertions that he knew his rights.</p>
<p>[2]  The Court of Appeals also distinguished <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), on the ground that the second (and warned) confession at issue there was the product of the defendant's volition. <span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/#1019" aria-description="Citation for case: United States v. Patane">304 F.3d, at 1019, 1021</a></span>. For the reasons discussed below, we do not find this distinction relevant.</p>
<p>[3]  We acknowledge that there is language in some of the Court's post-<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> decisions that might suggest that the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule operates as a direct constraint on police. See, <i>e. g., </i><i>Stansbury</i> v. <i>California,</i> <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#322" aria-description="Citation for case: Stansbury v. California">511 U. S. 318, 322</a></span> (1994) <i>(per curiam)</i><i>; </i><i>Moran</i> v. <i>Burbine,</i> <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#420" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 420</a></span> (1986) (stating that "<i>Miranda</i> imposed on the police an obligation to follow certain procedures"); cf. <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#485" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477, 485</a></span> (1981). But <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> itself made clear that its focus was the admissibility of statements, see, <i>e. g.,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#439" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 439, 467</a></span>, a view the Court reaffirmed in <i>Dickerson</i> v. <i>United States,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#443" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428, 443-444</a></span> (2000) (equating the <i>Miranda</i> rule with the proposition that "unwarned statements may not be used <i>as evidence</i> in the prosecution's case in chief" (emphasis added)).</p>
<p>[4]  We reject respondent's invitation to apply the balancing test of <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">308 U. S. 338</a></span> (1939). Brief for Respondent 15-33. At issue in <i><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">Nardone</a></span></i> was the violation of a federal wiretap statute, and the Court employed an exclusionary rule to deter those violations. But, once again, there are no violations (statutory or constitutional) to deter here.</p>
<p>[5]  It is worth mentioning that the Court of Appeals did not have the benefit of our decision in <i>Chavez</i> v. <i>Martinez,</i> <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/" aria-description="Citation for case: Chavez v. Martinez">538 U. S. 760</a></span> (2003).</p>
<p>[6]  While Fourth Amendment protections extend to "persons, houses, papers, and effects," the Self-Incrimination Clause prohibits only compelling a defendant to be "a witness against himself," Amdt. 5.</p>
<p>[7]  It is not clear whether the Government could have used legal processes actually to compel respondent to produce the Glock, though there is a reasonable argument that it could have. See, <i>e. g., </i><i>United States</i> v. <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#42" aria-description="Citation for case: United States v. Hubbell">530 U. S. 27, 42-45</a></span> (2000); <i>Baltimore City Dept. of Social Servs.</i> v. <i>Bouknight,</i> <span class="citation" data-id="9431889"><a href="/opinion/112360/baltimore-city-department-of-social-services-v-bouknight/#554" aria-description="Citation for case: Baltimore City Department of Social Services v. Bouknight">493 U. S. 549, 554-556</a></span> (1990); <i>Fisher</i> v. <i>United States,</i> <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/" aria-description="Citation for case: Fisher v. United States">425 U. S. 391</a></span> (1976); <i>Warden, Md. Penitentiary</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#302" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 302-303</a></span> (1967); <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#761" aria-description="Citation for case: Schmerber v. California">384 U.S. 757, 761</a></span> (1966). But see <i>Commonwealth</i> v. <i>Hughes,</i> <span class="citation" data-id="2021779"><a href="/opinion/2021779/commonwealth-v-hughes/" aria-description="Citation for case: Commonwealth v. Hughes">380 Mass. 583</a></span>, <span class="citation" data-id="2021779"><a href="/opinion/2021779/commonwealth-v-hughes/" aria-description="Citation for case: Commonwealth v. Hughes">404 N. E. 2d 1239</a></span> (1980); <i>Goldsmith</i> v. <i>Superior Court,</i> <span class="citation" data-id="2125014"><a href="/opinion/2125014/goldsmith-v-superior-court/" aria-description="Citation for case: Goldsmith v. Superior Court">152 Cal. App. 3d 76</a></span>, <span class="citation" data-id="2125014"><a href="/opinion/2125014/goldsmith-v-superior-court/" aria-description="Citation for case: Goldsmith v. Superior Court">199 Cal. Rptr. 366</a></span> (1984). In light of this, it would be especially odd to exclude the Glock here.</p>
<p>[1]  In so saying, we are taking the legal issue as it comes to us, even though the facts give off the scent of a made-up case. If there was a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> failure, the most immediate reason was that Patane told the police to stop giving the warnings because he already knew his rights. There could easily be an analogy in this case to the bumbling mistake the police committed in <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985). See <i>Missouri</i> v. <i>Seibert, ante,</i> at 614-615 (plurality opinion).</p>
<p>[2]  To the extent that <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433</a></span> (1974) (admitting the testimony of a witness who was discovered because of an unwarned custodial interrogation), created another exception to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> it is off the point here. In <i><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span>,</i> we explicitly declined to lay down a broad rule about the fruits of unwarned statements. Instead, we "place[d] our holding on a narrower ground," relying principally on the fact that the interrogation occurred before <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was decided and was conducted in good faith according to constitutional standards governing at that time. <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">417 U. S., at 447</a></span>-448 (citing <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964)).</p>

</div>
```

---
