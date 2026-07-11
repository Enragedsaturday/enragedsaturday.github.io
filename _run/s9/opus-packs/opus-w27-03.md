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

## GROUP: content/cases/Bond v. United States.md  (`case`, 6 assertions)

### content_page

```
---
title: "Bond v. United States"
type: case
citation: "529 U.S. 334 (2000)"
parallel_cite: "120 S. Ct. 1462; 146 L. Ed. 2d 365"
neutral_cite: 2000 U.S. LEXIS 2520
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2000
date_decided: 2000-04-17
docket: 98-9349
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2000-04-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Bond v. United States
  varies_by_point: false
  scope_note: "Good law; the rule that exploratory tactile manipulation of a traveler's bag is a search remains controlling."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118354/bond-v-united-states/"
  cluster_id: 118354
  opinion_id: 9433930
  identity_checked: true
homes:
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Key — Progeny"
  - page: "[[Abandonment]]"
    role: "Related (cross-doctrine)"
related: ["[[California v. Ciraolo]]", "[[Florida v. Riley]]", "[[United States v. Place]]", "[[Terry v. Ohio]]"]
aliases: ["Bond v. United States (2000)"]
tags: ["case", "fourth-amendment", "search", "luggage", "tactile", "reasonable-expectation-of-privacy"]
holding: "An officer's physical manipulation (squeezing) of a bus passenger's soft carry-on luggage is a Fourth Amendment search; tactile inspection is more intrusive than visual observation."
lake:
  record_id: Bond v. United States
  status: verified
  projected_at: 2026-07-06
---

# Bond v. United States

*529 U.S. 334 (2000)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Border Patrol agent boarded a stopped Greyhound bus to check immigration status. Walking back toward the front, he squeezed the soft luggage in the overhead bins, felt a "brick-like" object in Bond's green canvas bag, obtained Bond's consent to open it, and found methamphetamine. Bond moved to suppress, arguing the agent's squeezing of his bag was an unreasonable search.

## Issue
Whether a law enforcement officer's physical manipulation of a bus passenger's soft carry-on luggage is a "search" within the meaning of the Fourth Amendment.

## Rule
Yes. Tactile examination is more invasive than visual observation: distinguishing the aerial-observation cases, the Court explained that "[p]hysically invasive inspection is simply more intrusive than purely visual inspection." — 529 U.S. at 337. ^pin-337

A traveler retains a privacy interest against exploratory squeezing: "a bus passenger clearly expects that his bag may be handled. He does not expect that other passengers or bus employees will, as a matter of course, feel the bag in an exploratory manner. But this is exactly what the agent did here. We therefore hold that the agent's physical manipulation of petitioner's bag violated the Fourth Amendment." — *Id.* at 338–339. ^pin-338

## Application
Bond, by placing his bag in the overhead bin, expected that fellow passengers and bus personnel might move or handle it — but not that they would feel it in the deliberate, exploratory manner the agent used to detect its contents. Because that manipulation exceeded the casual handling a traveler anticipates, it invaded a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] and constituted a search; the agent had no warrant or other justification for it.

## Conclusion
The agent's exploratory squeezing of the bag was a Fourth Amendment search; the judgment was reversed. Personal luggage carried by a traveler retains Fourth Amendment protection against tactile, exploratory inspection even when exposed to incidental public handling.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Distinguishes the visual-observation line ([[California v. Ciraolo]], [[Florida v. Riley]]) and confirms that a traveler's bag is an "effect" with retained privacy (cf. [[United States v. Place]]).

## Appears on
- [[Reasonable Expectation of Privacy]] — *Key — Progeny*
- [[Abandonment]] — *Related (cross-doctrine)*

## Sources
- *Bond v. United States*, 529 U.S. 334 (2000) — https://www.courtlistener.com/opinion/118354/bond-v-united-states/ — pinpoints: 337, 338–339.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a9eb7638bceb1625", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "529 U.S. 334 (2000)", "court": "U.S. Supreme Court", "neutral_cite": "2000 U.S. LEXIS 2520", "official_citation_present": true, "parallel_cite": "120 S. Ct. 1462; 146 L. Ed. 2d 365", "title": "Bond v. United States", "year": "2000"}}
{"assertion_id": "0a09e592f1329389", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Key — Progeny", "title": "Bond v. United States"}}
{"assertion_id": "a548181e4117121e", "dimension": "support", "kind": "home_role", "locator": {"home": "Abandonment"}, "payload": {"home": "Abandonment", "role": "Related (cross-doctrine)", "title": "Bond v. United States"}}
{"assertion_id": "e7f20bee6b93582d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An officer's physical manipulation (squeezing) of a bus passenger's soft carry-on luggage is a Fourth Amendment search; tactile inspection is more intrusive than visual observation.", "title": "Bond v. United States"}}
{"assertion_id": "2aa1172fc07ff082", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Bond v. United States"}}
{"assertion_id": "4fc33704e100542b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2000-04-17", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Bond v. United States", "field_i_validity": "good_law", "scope_note": "Good law; the rule that exploratory tactile manipulation of a traveler's bag is a search remains controlling.", "title": "Bond v. United States", "varies_by_point": "false"}}
```

### lake record — Bond v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Bond v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Bond v. United States",
    "case_name_short": "Bond",
    "case_name_full": "Bond v. United States",
    "input_case_name": "Bond v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2000-04-17",
    "year": 2000,
    "docket": "98-9349",
    "cluster_id": 118354,
    "lead_opinion_id": 9433930,
    "sibling_ids": [
      118354,
      9433930,
      9433931
    ],
    "absolute_url": "/opinion/118354/bond-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "529 U.S. 334",
      "volume": "529",
      "reporter": "U.S.",
      "page": "334",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "120 S. Ct. 1462",
        "volume": "120",
        "reporter": "S. Ct.",
        "page": "1462",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "146 L. Ed. 2d 365",
        "volume": "146",
        "reporter": "L. Ed. 2d",
        "page": "365",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2000 U.S. LEXIS 2520",
        "volume": "2000",
        "reporter": "U.S. LEXIS",
        "page": "2520",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "529 U.S. 334",
        "volume": "529",
        "reporter": "U.S.",
        "page": "334",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "120 S. Ct. 1462",
        "volume": "120",
        "reporter": "S. Ct.",
        "page": "1462",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "146 L. Ed. 2d 365",
        "volume": "146",
        "reporter": "L. Ed. 2d",
        "page": "365",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 U.S. LEXIS 2520",
        "volume": "2000",
        "reporter": "U.S. LEXIS",
        "page": "2520",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "529 U.S. 334",
    "official_selection": {
      "court_class": "scotus",
      "selected": "529 U.S. 334",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-337",
      "page": null,
      "quote": "within the meaning of the Fourth Amendment. ## Rule Yes. Tactile examination is more invasive than visual observation: distinguishing the aerial-observation cases, the Court explained that",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-338",
      "page": null,
      "quote": "a bus passenger clearly expects that his bag may be handled. He does not expect that other passengers or bus employees will, as a matter of course, feel the bag in an exploratory manner. But this is exactly what the agent did here. We therefore hold that the agent's physical manipulation of petitioner's bag violated the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2000-04-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Bond v. United States",
    "varies_by_point": false,
    "scope_note": "Good law; the rule that exploratory tactile manipulation of a traveler's bag is a search remains controlling.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Bond v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Morris Wise",
          "cluster_id": 4448990,
          "cite": [
            "877 F.3d 209"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rickey Beene",
          "cluster_id": 3183556,
          "cite": [
            "818 F.3d 157",
            "2016 U.S. App. LEXIS 4331",
            "2016 WL 890127"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Peterson",
          "cluster_id": 3961890,
          "cite": [
            "879 N.E.2d 806",
            "173 Ohio App. 3d 575",
            "2007 Ohio 5667"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Poteet v. Sullivan",
          "cluster_id": 2332316,
          "cite": [
            "218 S.W.3d 780",
            "2007 WL 289871"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Camacho",
          "cluster_id": 2546036,
          "cite": [
            "3 P.3d 878",
            "98 Cal. Rptr. 2d 232",
            "23 Cal. 4th 824",
            "2000 Cal. Daily Op. Serv. 6235",
            "2000 Daily Journal DAR 8273",
            "2000 Cal. LEXIS 5605"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane1_negative"
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
        "journal_ref": "Bond v. United States:lane2_top_cited"
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
        "journal_ref": "Bond v. United States:lane2_top_cited"
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
        "journal_ref": "Bond v. United States:lane2_top_cited"
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
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 622304,
          "cite": [
            "181 L. Ed. 2d 911",
            "132 S. Ct. 945",
            "565 U.S. 400",
            "2012 U.S. LEXIS 1063"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 2140668,
          "cite": [
            "767 N.E.2d 638",
            "97 N.Y.2d 341",
            "741 N.Y.S.2d 147"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
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
        "journal_ref": "Bond v. United States:lane2_top_cited"
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
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Turrubiate v. State",
          "cluster_id": 2948365,
          "cite": [
            "399 S.W.3d 147",
            "2013 WL 1438172",
            "2013 Tex. Crim. App. LEXIS 635"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
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
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Maynard",
          "cluster_id": 152441,
          "cite": [
            "615 F.3d 544",
            "392 U.S. App. D.C. 291",
            "2010 U.S. App. LEXIS 16417",
            "2010 WL 3063788"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robles",
          "cluster_id": 5607956,
          "cite": [
            "23 Cal. 4th 789",
            "3 P.3d 311",
            "2000 Daily Journal DAR 7789",
            "97 Cal. Rptr. 2d 914",
            "2000 Cal. Daily Op. Serv. 5894",
            "2000 Cal. LEXIS 5217"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lisa Amaechi v. Matthew West, and Bernard R. Pfluger Town of Dumfries",
          "cluster_id": 771726,
          "cite": [
            "237 F.3d 356",
            "2001 U.S. App. LEXIS 267",
            "2001 WL 20530"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robles",
          "cluster_id": 2545158,
          "cite": [
            "3 P.3d 311",
            "97 Cal. Rptr. 2d 914",
            "23 Cal. 4th 789"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Darlie Kee Darin Routier v. City of Rowlett Texas Jimmy Ray Patterson Chris Frosch Greg Davis, Assistant District Attorney for Dallas County",
          "cluster_id": 772922,
          "cite": [
            "247 F.3d 206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cregan",
          "cluster_id": 2681818,
          "cite": [
            "2014 IL 113600"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Reyes Fabian Olivera-Mendez",
          "cluster_id": 797553,
          "cite": [
            "484 F.3d 505",
            "2007 U.S. App. LEXIS 10492",
            "2007 WL 1296781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Granville, Anthony",
          "cluster_id": 2950015,
          "cite": [
            "423 S.W.3d 399",
            "2014 WL 714730",
            "2014 Tex. Crim. App. LEXIS 237"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Perea-Rey",
          "cluster_id": 801335,
          "cite": [
            "680 F.3d 1179",
            "2012 U.S. App. LEXIS 10941",
            "2012 WL 1948973"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Quartavious Davis",
          "cluster_id": 2798570,
          "cite": [
            "785 F.3d 498",
            "2015 WL 2058977"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Weaver",
          "cluster_id": 5639938,
          "cite": [
            "12 N.Y.3d 433",
            "909 N.E.2d 1195"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Krise v. State",
          "cluster_id": 853398,
          "cite": [
            "746 N.E.2d 957",
            "2001 Ind. LEXIS 394",
            "2001 WL 493444"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Frederick Alonzo Waller",
          "cluster_id": 792220,
          "cite": [
            "426 F.3d 838",
            "2005 U.S. App. LEXIS 22941",
            "2005 WL 2708784"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth King",
          "cluster_id": 770537,
          "cite": [
            "227 F.3d 732",
            "2000 WL 1209277"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118354 OR 9433930 OR 9433931) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 177,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 177,
        "triage_read": 6,
        "triage_snippet_classified": 171
      },
      "lane2_top_cited": {
        "query": "cites:(118354 OR 9433930 OR 9433931)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02OCZzPTEyNDg0NTkmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118354+OR+9433930+OR+9433931%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118354 OR 9433930 OR 9433931)",
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
    "complete_query": "cites:(118354 OR 9433930 OR 9433931)",
    "indexed_citing_opinions": 238,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118354,
        "count": 202,
        "count_source": "search"
      },
      {
        "opinion_id": 9433930,
        "count": 41,
        "count_source": "search"
      },
      {
        "opinion_id": 9433931,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 413,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/bond-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc3NjY0OTUmcz02NDcxNTEyJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118354+OR+9433930+OR+9433931%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118354,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 111833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 112067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 112175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 729772,
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
    "date_created": "2026-07-04T20:07:56Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:08:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:08:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:12:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:08:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Bond v. United States

```
<opinion type="majority">
<author id="b411-7">Chief Justice Rehnquist</author>
<p id="Ahq">delivered the opinion of the Court.</p>
<p id="b411-8">This case presents the question whether a law enforcement officer’s physical manipulation of a bus passenger’s carry-on luggage violated the Fourth Amendment’s proscription against unreasonable searches. We hold that it did.</p>
<p id="b411-9">Petitioner Steven Dewayne Bond was a passenger on a Greyhound bus that left California bound for Little Rock, Arkansas. The bus stopped, as it was required to do, at the permanent Border Patrol checkpoint in Sierra Blanca, Texas. Border Patrol Agent Cesar Cantu boarded the bus to check the immigration status of its passengers. After reaching the back of the bus, having satisfied himself that the passengers were lawfully in the United States, Agent Cantu began walking toward the front. Along the way, he squeezed the soft luggage which passengers had placed in the overhead storage space above the seats.</p>
<p id="b412-4"><page-number citation-index="1" label="336">*336</page-number>Petitioner was seated four or five rows from the back of the bus. As Agent Cantu inspected the luggage in the compartment above petitioner’s seat, he squeezed a green canvas bag and noticed that it contained a “brick-like” object. Petitioner admitted that the bag was his and agreed to allow Agent Cantu to open it.<footnotemark>1</footnotemark> Upon opening the bag, Agent Cantu discovered a “brick” of methamphetamine. The brick had been wrapped in duct tape until it was oval-shaped and then rolled in a pair of pants.</p>
<p id="b412-5">Petitioner was indicted for conspiracy to possess, and possession with intent to distribute, methamphetamine in violation of <span class="citation no-link">84 Stat. 1260</span>, <span class="citation no-link">21 U. S. C. § 841</span>(a)(1). He moved to suppress the drugs, arguing that Agent Cantu conducted an illegal search of his bag. Petitioner’s motion was denied, and the District Court found him guilty on both counts and sentenced him to 57 months in prison. On appeal, he conceded that other passengers had access to his bag, but contended that Agent Cantu manipulated the bag in a way that other passengers would not. The Court of Appeals rejected this argument, stating that the fact that Agent Cantu’s manipulation of petitioner’s bag was calculated to detect contraband is irrelevant for Fourth Amendment purposes. <span class="citation" data-id="6981740"><a href="/opinion/7076945/united-states-v-bond/#227" aria-description="Citation for case: United States v. Bond">167 F. 3d 225, 227</a></span> (CA5 1999) (citing <em>California </em>v. <em>Ciraolo, </em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207</a></span> (1986)). Thus, the Court of Appeals affirmed the denial of the motion to suppress, holding that Agent Cantu’s manipulation of the bag was not a search within the meaning of the Fourth Amendment. <span class="citation" data-id="6981740"><a href="/opinion/7076945/united-states-v-bond/#227" aria-description="Citation for case: United States v. Bond">167 F. 3d, at 227</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./528/927/">528 U. S. 927</a></span> (1999), and now reverse.</p>
<p id="b412-6">The Fourth Amendment provides that “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated....” A traveler’s personal luggage is clearly an “effect” protected by the Amendment. See <em>United States </em>v. <page-number citation-index="1" label="337">*337</page-number><em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U. S. 696, 707</a></span> (1983). Indeed, it is undisputed here that petitioner possessed a privacy interest in his bag.</p>
<p id="b413-5">But the Government asserts that by exposing his bag to the public, petitioner lost a reasonable expectation that his bag would not be physically manipulated. The Government relies on our decisions in <em>California </em>v. <em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo, supra,</a></span> </em>and <em>Florida </em>v. <em>Riley, </em><span class="citation" data-id="9431518"><a href="/opinion/112175/florida-v-riley/" aria-description="Citation for case: Florida v. Riley">488 U. S. 445</a></span> (1989), for the proposition that matters open to public observation are not protected by the Fourth Amendment. In <em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo</a></span>, </em>we held that police observation of a backyard from a plane flying at an altitude of 1,000 feet did not violate a reasonable expectation of privacy. Similarly, in <em><span class="citation" data-id="9431518"><a href="/opinion/112175/florida-v-riley/" aria-description="Citation for case: Florida v. Riley">Riley</a></span>, </em>we relied on <em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo</a></span> </em>to hold that police observation of a greenhouse in a home’s curtilage from a helicopter passing at an altitude of 400 feet did not violate the Fourth Amendment. We reasoned that the property was “not necessarily protected from inspection that involves no physical invasion,” and determined that because any member of the public could have lawfully observed the defendants’ property by flying overhead, the defendants’ expectation of privacy was “not reasonable and not one ‘that society is prepared to honor.’ ” See <span class="citation" data-id="9431518"><a href="/opinion/112175/florida-v-riley/#449" aria-description="Citation for case: Florida v. Riley"><em>Riley, supra, </em>at 449</a></span> (explaining and relying on Ciraolo’s reasoning).</p>
<p id="b413-6">But <em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo</a></span> </em>and <em><span class="citation" data-id="9431518"><a href="/opinion/112175/florida-v-riley/" aria-description="Citation for case: Florida v. Riley">Riley</a></span> </em>are different from this case because they involved only visual, as opposed to tactile, observation. Physically invasive inspection is simply more intrusive than purely visual inspection. For example, in <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 16-17</a></span> (1968), we stated that a “careful [tactile] exploration of the outer surfaces of a person’s clothing all over his or her body” is a “serious intrusion upon the sanctity of the person, which may inflict great indignity and arouse strong resentment, and it is not to be undertaken lightly.” Although Agent Cantu did not “frisk” petitioner’s person, he did conduct a probing tactile examination of petitioner’s carry-on luggage. Obviously, petitioner’s bag was not part of his person. But travelers are particularly concerned <page-number citation-index="1" label="338">*338</page-number>about their earry-on luggage; they generally use it to transport personal items that, for whatever reason, they prefer to keep close at hand.</p>
<p id="b414-4">Here, petitioner concedes that, by placing his bag in the overhead compartment, he could expect that it would be exposed to certain kinds of touching and handling. But petitioner argues that Agent Cantu’s physical manipulation of his luggage “far exceeded the casual contact [petitioner] could have expected from other passengers.” Brief for Petitioner 18-19. The Government counters that it did not.</p>
<p id="b414-5">Our Fourth Amendment analysis embraces two questions. First, we ask whether the individual, by his conduct, has exhibited an actual expectation of privacy; that is, whether he has shown that “he [sought] to preserve [something] as private.” <em>Smith </em>v. <em>Maryland, </em><span class="citation multiple-matches"><a href="/c/U.%20S./442/785/">442 U. S. 785</a></span>, 740 (1979) (internal quotation marks omitted). Here, petitioner sought to preserve privacy by using an opaque bag and placing that bag directly above his seat. Second, we inquire whether the individual’s expectation of privacy is “one that society is prepared to recognize as reasonable.” <em>Ibid, </em>(internal quotation marks omitted).<footnotemark>2</footnotemark> When a bus passenger places a bag in an overhead bin, he expects that other passengers or bus employees may move it for one reason or another. Thus, a bus passenger clearly expects that his bag may be handled. He does not expect that other passengers or bus employees will, <page-number citation-index="1" label="339">*339</page-number>as a matter of course, feel the bag in an exploratory manner. But this is exactly what the agent did here. We therefore hold that the agent’s physical manipulation of petitioner’s bag violated the Fourth Amendment.</p>
<p id="b415-5">The judgment of the Court of Appeals is</p>
<p id="b415-6">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b412-7"> The Government has not argued here that petitioner’s consent to Agent Cantu’s opening the bag is a basis for admitting the evidence.</p>
</footnote>
<footnote label="2">
<p id="b414-6"> The parties properly agree that the subjective intent of the law enforcement officer is irrelevant in determining whether that officer’s actions violate the Fourth Amendment. Brief for Petitioner 14; Brief for United States 33-34; see <em>Whren </em>v. <em>United States, </em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States">517 U. S. 806, 813</a></span> (1996) (stating that “we have been unwilling to entertain Fourth Amendment challenges based on the actual motivations of individual officers”); <em>California </em>v. <em>Ciraolo, </em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#212" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207, 212</a></span> (1986) (rejecting respondent’s challenge to “the authority of government to observe his activity from any vantage point or place if the viewing is motivated by a law enforcement purpose, and not the result of a casual, accidental observation”). This principle applies to the agent’s acts in this case as well; the issue is not his state of mind, but the objective effect of his actions.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Boyd v. United States.md  (`case`, 6 assertions)

### content_page

```
---
title: "Boyd v. United States"
type: case
citation: "116 U.S. 616 (1886)"
parallel_cite: "6 S. Ct. 524; 29 L. Ed. 746; 3 A.F.T.R. (P-H) 2488"
neutral_cite: 1886 U.S. LEXIS 1806
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1886
date_decided: 1886-02-01
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 1886-02-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Boyd v. United States
  varies_by_point: true
  scope_note: "Boyd's holding that compelling production of private papers violates the Fourth/Fifth Amendments, and its 'mere evidence' rule, have been abandoned (Warden v. Hayden) and sharply limited (Fisher v. United States). Boyd's account of Entick v. Carrington as the historical foundation of the Fourth Amendment — the proposition for which it is cited here — remains good law and is frequently cited."
  point_overrides:
    - point: legacy-limited-boyd-v-united-states
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: Warden v. Hayden
          cluster_id: 107465
          cite: 387 U.S. 294
          field_ii: limited
      scope_note: "Boyd's holding that compelling production of private papers violates the Fourth/Fifth Amendments, and its 'mere evidence' rule, have been abandoned (Warden v. Hayden) and sharply limited (Fisher v. United States). Boyd's account of Entick v. Carrington as the historical foundation of the Fourth Amendment — the proposition for which it is cited here — remains good law and is frequently cited."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/91573/boyd-v-united-states/"
  cluster_id: 91573
  opinion_id: 91573
  identity_checked: true
homes:
  - page: "[[Common Law Origins]]"
    role: "Key — Anchor"
related: ["[[Entick v. Carrington]]", "[[Warden v. Hayden]]"]
aliases: ["Boyd v. US"]
tags: ["case", "fourth-amendment", "common-law-origins", "fifth-amendment", "history"]
holding: "Recounts the founding history and adopts *Entick v. Carrington* as 'the true and ultimate expression of constitutional law' embodied in the Fourth Amendment."
lake:
  record_id: Boyd v. United States
  status: verified
  projected_at: 2026-07-06
---

# Boyd v. United States

*116 U.S. 616 (1886)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In a federal customs forfeiture proceeding, the government invoked a statute to compel Boyd to produce private business invoices for use against him. Boyd objected that the compelled production was both an unreasonable search and seizure and a form of compelled self-incrimination. To decide what the Fourth Amendment forbids, the Court turned to the English origins of the constitutional guarantee.

## Issue
What the Framers of the Fourth Amendment understood "unreasonable searches and seizures" to mean — and, in answering, whether *[[Entick v. Carrington]]* states the foundational principle the Amendment embodies.

## Rule
The Court adopted Lord Camden's judgment in *[[Entick v. Carrington]]* as the constitutional touchstone. Every American statesman of the founding era "considered it as the true and ultimate expression of constitutional law". — 116 U.S. at 626. ^pin-626

Accordingly, *[[Entick v. Carrington|Entick]]*'s "propositions were in the minds of those who framed the Fourth Amendment to the Constitution, and were considered as sufficiently explanatory of what was meant by unreasonable searches and seizures." — *Id.* at 626-627. ^pin-627

*(Note: the broader Boyd holding equating compelled production of papers with an unreasonable search and self-incrimination has since been limited — see Treatment below. The Entick/historical proposition stated here is undisturbed.)*

## Application
Reading the Fourth Amendment through *[[Entick v. Carrington|Entick]]*, the Court held that the statutory compulsion of Boyd's private papers, for use against him in the forfeiture, fell within the constitutional prohibition on unreasonable searches and ran together with the Fifth Amendment privilege; the judgment against Boyd was reversed.

## Conclusion
The compelled production violated the Fourth and Fifth Amendments. As a matter of doctrine the decision survives chiefly for its founding-era account of the Amendment's origins; its papers-production holding has not endured (see Treatment).

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Limited by** *Fisher v. United States* (compelled production of papers analyzed under act-of-production doctrine, not Boyd's broad Fourth/Fifth Amendment convertibility) and **abandoned in part by** [[Warden v. Hayden]] (rejecting the "mere evidence" rule).
- The portion for which this page cites *Boyd* — its adoption of [[Entick v. Carrington]] as the historical expression of the Fourth Amendment — remains good law and is regularly invoked.

## Appears on
- [[Common Law Origins]] — *Key — Anchor*

## Sources
- *Boyd v. United States*, 116 U.S. 616 (1886) — https://www.courtlistener.com/opinion/91573/boyd-v-united-states/ — pinpoints: 626, 627.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e729e0971ffa4668", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "116 U.S. 616 (1886)", "court": "U.S. Supreme Court", "neutral_cite": "1886 U.S. LEXIS 1806", "official_citation_present": true, "parallel_cite": "6 S. Ct. 524; 29 L. Ed. 746; 3 A.F.T.R. (P-H) 2488", "title": "Boyd v. United States", "year": "1886"}}
{"assertion_id": "721fa2ef720a2c2e", "dimension": "support", "kind": "home_role", "locator": {"home": "Common Law Origins"}, "payload": {"home": "Common Law Origins", "role": "Key — Anchor", "title": "Boyd v. United States"}}
{"assertion_id": "b76b525c94027985", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Recounts the founding history and adopts *Entick v. Carrington* as 'the true and ultimate expression of constitutional law' embodied in the Fourth Amendment.", "title": "Boyd v. United States"}}
{"assertion_id": "2ed8ef4c5ffc9dab", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1886-02-01", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Boyd v. United States", "field_i_validity": "caution", "scope_note": "Boyd's holding that compelling production of private papers violates the Fourth/Fifth Amendments, and its 'mere evidence' rule, have been abandoned (Warden v. Hayden) and sharply limited (Fisher v. United States). Boyd's account of Entick v. Carrington as the historical foundation of the Fourth Amendment — the proposition for which it is cited here — remains good law and is frequently cited.", "title": "Boyd v. United States", "varies_by_point": "true"}}
{"assertion_id": "7bd258911e7cabb8", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Boyd v. United States"}}
{"assertion_id": "e0f1f7ca655879d5", "dimension": "treatment", "kind": "treatment_override", "locator": {"point": "legacy-limited-boyd-v-united-states"}, "payload": {"by": [{"cite": "387 U.S. 294", "cluster_id": "107465", "field_ii": "limited", "name": "Warden v. Hayden"}], "field_i_validity": "caution", "point": "legacy-limited-boyd-v-united-states", "point_label": "Legacy limited treatment point", "s3_binding_status": "provisional", "title": "Boyd v. United States"}}
```

### lake record — Boyd v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Boyd v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Boyd v. United States",
    "case_name_short": "Boyd",
    "case_name_full": "Boyd v. United States",
    "input_case_name": "Boyd v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1886-02-01",
    "year": 1886,
    "docket": null,
    "cluster_id": 91573,
    "lead_opinion_id": 91573,
    "sibling_ids": [
      91573,
      9417418,
      9417419
    ],
    "absolute_url": "/opinion/91573/boyd-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "116 U.S. 616",
      "volume": "116",
      "reporter": "U.S.",
      "page": "616",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "6 S. Ct. 524",
        "volume": "6",
        "reporter": "S. Ct.",
        "page": "524",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "29 L. Ed. 746",
        "volume": "29",
        "reporter": "L. Ed.",
        "page": "746",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 A.F.T.R. (P-H) 2488",
        "volume": "3",
        "reporter": "A.F.T.R. (P-H)",
        "page": "2488",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1886 U.S. LEXIS 1806",
        "volume": "1886",
        "reporter": "U.S. LEXIS",
        "page": "1806",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "116 U.S. 616",
        "volume": "116",
        "reporter": "U.S.",
        "page": "616",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "6 S. Ct. 524",
        "volume": "6",
        "reporter": "S. Ct.",
        "page": "524",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "29 L. Ed. 746",
        "volume": "29",
        "reporter": "L. Ed.",
        "page": "746",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1886 U.S. LEXIS 1806",
        "volume": "1886",
        "reporter": "U.S. LEXIS",
        "page": "1806",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 A.F.T.R. (P-H) 2488",
        "volume": "3",
        "reporter": "A.F.T.R. (P-H)",
        "page": "2488",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "116 U.S. 616",
    "official_selection": {
      "court_class": "scotus",
      "selected": "116 U.S. 616",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-626",
      "page": null,
      "quote": "to mean \u2014 and, in answering, whether *Entick v. Carrington* states the foundational principle the Amendment embodies. ## Rule The Court adopted Lord Camden's judgment in *Entick v. Carrington* as the constitutional touchstone. Every American statesman of the founding era",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-627",
      "page": null,
      "quote": "propositions were in the minds of those who framed the Fourth Amendment to the Constitution, and were considered as sufficiently explanatory of what was meant by unreasonable searches and seizures.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "1886-02-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Boyd v. United States",
    "varies_by_point": true,
    "scope_note": "Boyd's holding that compelling production of private papers violates the Fourth/Fifth Amendments, and its 'mere evidence' rule, have been abandoned (Warden v. Hayden) and sharply limited (Fisher v. United States). Boyd's account of Entick v. Carrington as the historical foundation of the Fourth Amendment \u2014 the proposition for which it is cited here \u2014 remains good law and is frequently cited.",
    "point_overrides": [
      {
        "point": "legacy-limited-boyd-v-united-states",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "Warden v. Hayden",
            "cluster_id": 107465,
            "cite": "387 U.S. 294",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Boyd's holding that compelling production of private papers violates the Fourth/Fifth Amendments, and its 'mere evidence' rule, have been abandoned (Warden v. Hayden) and sharply limited (Fisher v. United States). Boyd's account of Entick v. Carrington as the historical foundation of the Fourth Amendment \u2014 the proposition for which it is cited here \u2014 remains good law and is frequently cited."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "Warden v. Hayden",
          "cluster_id": 107465,
          "cite": "387 U.S. 294",
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
          "name": "Andrew Lennette, Individually and on behalf of C.L., O.L. and S.L., Minor Children v. State of Iowa, Melody Siver, Amy Howell, and Valerie Lovaglia",
          "cluster_id": 6476611,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Pittman",
          "cluster_id": 10160783,
          "cite": [
            "367 Or. 498",
            "479 P.3d 1028"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Krystal Wagner, Individually and as Administrator of the Estate of Shane Jensen v. State of Iowa and William L. Spece a/k/a Bill L. Spece",
          "cluster_id": 4844322,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. McCarthy",
          "cluster_id": 4746120,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane1_negative"
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
        "journal_ref": "Boyd v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amended July 5, 2017 State of Iowa v. Maurice D. Angel and Kemia B. McDowell",
          "cluster_id": 4471947,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Maurice D. Angel and Kemia B. McDowell",
          "cluster_id": 4384931,
          "cite": [
            "893 N.W.2d 904",
            "2017 WL 1422692",
            "2017 Iowa Sup. LEXIS 41"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wheeler v. State",
          "cluster_id": 3182294,
          "cite": [
            "135 A.3d 282",
            "2016 Del. LEXIS 121",
            "2016 WL 825395"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Yee",
          "cluster_id": 3062319,
          "cite": [
            "177 So. 3d 72",
            "2015 Fla. App. LEXIS 15198",
            "2015 WL 5965213"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Riley v. Cal. United States",
          "cluster_id": 2680439,
          "cite": [
            "189 L. Ed. 2d 430",
            "134 S. Ct. 2473",
            "2014 U.S. LEXIS 4497",
            "82 U.S.L.W. 4558"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Isaac Andrew Baldon III",
          "cluster_id": 4472245,
          "cite": [
            "829 N.W.2d 785",
            "2013 WL 1694553",
            "2013 Iowa Sup. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Miranda v. Arizona",
          "cluster_id": 107252,
          "cite": [
            "16 L. Ed. 2d 694",
            "86 S. Ct. 1602",
            "384 U.S. 436",
            "1966 U.S. LEXIS 2817",
            "10 Ohio Misc. 9",
            "36 Ohio Op. 2d 237",
            "10 A.L.R. 3d 974"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bivens v. Six Unknown Named Agents of Federal Bureau of Narcotics",
          "cluster_id": 108375,
          "cite": [
            "29 L. Ed. 2d 619",
            "91 S. Ct. 1999",
            "403 U.S. 388",
            "1971 U.S. LEXIS 23"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katz v. United States",
          "cluster_id": 107564,
          "cite": [
            "19 L. Ed. 2d 576",
            "88 S. Ct. 507",
            "389 U.S. 347",
            "1967 U.S. LEXIS 2"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wong Sun v. United States",
          "cluster_id": 106515,
          "cite": [
            "9 L. Ed. 2d 441",
            "83 S. Ct. 407",
            "371 U.S. 471",
            "1963 U.S. LEXIS 2431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mapp v. Ohio",
          "cluster_id": 106285,
          "cite": [
            "6 L. Ed. 2d 1081",
            "81 S. Ct. 1684",
            "367 U.S. 643",
            "1961 U.S. LEXIS 812"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carroll v. United States",
          "cluster_id": 100567,
          "cite": [
            "267 U.S. 132",
            "45 S. Ct. 280",
            "69 L. Ed. 543",
            "1925 U.S. LEXIS 361"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chimel v. California",
          "cluster_id": 107979,
          "cite": [
            "23 L. Ed. 2d 685",
            "89 S. Ct. 2034",
            "395 U.S. 752",
            "1969 U.S. LEXIS 1166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schmerber v. California",
          "cluster_id": 107262,
          "cite": [
            "16 L. Ed. 2d 908",
            "86 S. Ct. 1826",
            "384 U.S. 757",
            "1966 U.S. LEXIS 1129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roe v. Wade",
          "cluster_id": 108713,
          "cite": [
            "35 L. Ed. 2d 147",
            "93 S. Ct. 705",
            "410 U.S. 113",
            "1973 U.S. LEXIS 159"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griswold v. Connecticut",
          "cluster_id": 107082,
          "cite": [
            "14 L. Ed. 2d 510",
            "85 S. Ct. 1678",
            "381 U.S. 479",
            "1965 U.S. LEXIS 2282"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stone v. Powell",
          "cluster_id": 109540,
          "cite": [
            "49 L. Ed. 2d 1067",
            "96 S. Ct. 3037",
            "428 U.S. 465",
            "1976 U.S. LEXIS 86"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. United States",
          "cluster_id": 104504,
          "cite": [
            "92 L. Ed. 2d 436",
            "68 S. Ct. 367",
            "333 U.S. 10",
            "1948 U.S. LEXIS 2583",
            "92 L. Ed. 436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gilbert v. California",
          "cluster_id": 107487,
          "cite": [
            "18 L. Ed. 2d 1178",
            "87 S. Ct. 1951",
            "388 U.S. 263",
            "1967 U.S. LEXIS 1086"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malloy v. Hogan",
          "cluster_id": 106862,
          "cite": [
            "12 L. Ed. 2d 653",
            "84 S. Ct. 1489",
            "378 U.S. 1",
            "1964 U.S. LEXIS 993"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Weeks v. United States",
          "cluster_id": 98094,
          "cite": [
            "232 U.S. 383",
            "34 S. Ct. 341",
            "58 L. Ed. 652",
            "1914 U.S. LEXIS 1368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Calandra",
          "cluster_id": 108898,
          "cite": [
            "38 L. Ed. 2d 561",
            "94 S. Ct. 613",
            "414 U.S. 338",
            "1974 U.S. LEXIS 145",
            "66 Ohio Op. 2d 320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(91573 OR 9417418 OR 9417419) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzE5MDY4ODAwMDAwJnM9MjMzMjY4NyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%2891573+OR+9417418+OR+9417419%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(91573 OR 9417418 OR 9417419)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDM2JnM9MTA5NDMyJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%2891573+OR+9417418+OR+9417419%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(91573 OR 9417418 OR 9417419)",
        "reviewed": 33,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 33,
        "triage_read": 0,
        "triage_snippet_classified": 33
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(91573 OR 9417418 OR 9417419)",
    "indexed_citing_opinions": 2274,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 91573,
        "count": 2081,
        "count_source": "search"
      },
      {
        "opinion_id": 9417418,
        "count": 242,
        "count_source": "search"
      },
      {
        "opinion_id": 9417419,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3820,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/boyd-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3OTQxNCZzPTk1MDA5NTImdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%2891573+OR+9417418+OR+9417419%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LRU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-04T20:12:41Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:13:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:13:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:31Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:13:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Boyd v. United States

```
<div>
<center><b><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U.S. 616</a></span> (1886)</b></center>
<center><h1>BOYD<br>
v.<br>
UNITED STATES.</h1></center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 11, 14, 1885.</center>
<center>Decided February 1, 1886.</center>
ERROR TO THE CIRCUIT COURT OF THE UNITED STATES FOR THE SOUTHERN DISTRICT OF NEW YORK.
<p><span class="star-pagination">*617</span> <i>Mr. Edwin B. Smith</i> for plaintiff in error. <i>Mr. Stephen G. Clarke</i> was with him on the brief.</p>
<p><i>Mr. Solicitor-General</i> for defendant in error.</p>
<p>MR. JUSTICE BRADLEY delivered the opinion of the court.</p>
<p>This was an information filed by the District Attorney of the United States in the District Court for the Southern District of New York, in July, 1884, in a cause of seizure and forfeiture of property, against thirty-five cases of plate glass, seized by the collector as forfeited to the United States, under § 12 of the "Act to amend the customs revenue laws, and to repeal moieties," passed June 22, 1874. <span class="citation no-link">18 Stat. 186</span>.</p>
<p>It is declared by that section that any owner, importer, consignee, &amp;c., who shall, with intent to defraud the revenue, make, or attempt to make, any entry of imported merchandise, by means of any fraudulent or false invoice, affidavit, letter or paper, or by means of any false statement, written or verbal, or who shall be guilty of any wilful act or omission by means whereof the United States shall be deprived of the lawful duties, or any portion thereof, accruing upon the merchandise, or any portion thereof, embraced or referred to in such invoice, affidavit, letter, paper, or statement, or affected by such act or omission, shall for each offence be fined in any sum not exceeding $5000 nor less than $50, or be imprisoned for any time not exceeding two years, or both; and, in addition to such fine, such merchandise shall be forfeited.</p>
<p>The charge was that the goods in question were imported <span class="star-pagination">*618</span> into the United States to the port of New York, subject to the payment of duties; and that the owners or agents of said merchandise, or other person unknown, committed the alleged fraud, which was described in the words of the statute. The plaintiffs in error entered a claim for the goods, and pleaded that they did not become forfeited in manner and form as alleged. On the trial of the cause it became important to show the quantity and value of the glass contained in twenty-nine cases previously imported. To do this the district attorney offered in evidence an order made by the District Judge under § 5 of the same act of June 22, 1874, directing notice under seal of the court to be given to the claimants, requiring them to produce the invoice of the twenty-nine cases. The claimants, in obedience to the notice, but objecting to its validity and to the constitutionality of the law, produced the invoice; and when it was offered in evidence by the district attorney they objected to its reception on the ground that, in a suit for forfeiture, no evidence can be compelled from the claimants themselves, and also that the statute, so far as it compels production of evidence to be used against the claimants is unconstitutional and void.</p>
<p>The evidence being received, and the trial closed, the jury found a verdict for the United States, condemning the thirty-five cases of glass which were seized, and judgment of forfeiture was given. This judgment was affirmed by the Circuit Court, and the decision of that court is now here for review.</p>
<p>As the question raised upon the order for the production by the claimants of the invoice of the twenty-nine cases of glass, and the proceedings had thereon, is not only an important one in the determination of the present case, but is a very grave question of constitutional law, involving the personal security, and privileges and immunities of the citizen, we will set forth the order at large. After the title of the court and term, it reads as follows, to wit:</p>
         "The United States of America           |
                    <i>against</i>                       &gt;
E.A.B., 1-35, Thirty-five Cases of Plate Glass.  |
<p>"Whereas the attorney of the United States for the Southern <span class="star-pagination">*619</span> District of New York has filed in this court a written motion in the above-entitled action, showing that said action is a suit or proceeding other than criminal, arising under the customs revenue laws of the United States, and not for penalties, now pending undetermined in this court, and that in his belief a certain invoice or paper belonging to and under the control of the claimants herein will tend to prove certain allegations set forth in said written motion, hereto annexed, made by him on behalf of the United States in said action, to wit, the invoice from the Union Plate Glass Company or its agents, covering the twenty-nine cases of plate glass marked G.H.B., imported from Liverpool, England, into the port of New York in the vessel Baltic, and entered by E.A. Boyd &amp; Sons at the office of the collector of customs of the port and collection district aforesaid on April 7th, 1884, on entry No. 47,108:</p>
<p>"Now, therefore, by virtue of the power in the said court vested by section 5 of the act of June 22, 1874, entitled `An act to amend the customs-revenue laws and to repeal moieties,' it is ordered that a notice under the seal of this court, and signed by the clerk thereof, be issued to the claimants, requiring them to produce the invoice or paper aforesaid before this court in the court-rooms thereof in the United States post-office and court-house building in the city of New York on October 16th, 1884, at eleven o'clock a.m., and thereafter at such other times as the court shall appoint, and that said United States attorney and his assistants and such persons as he shall designate shall be allowed before the court, and under its direction and in the presence of the attorneys for the claimants, if they shall attend, to make examination of said invoice or paper and to take copies thereof; but the claimants or their agents or attorneys shall have, subject to the order of the court, the custody of such invoice or paper, except pending such examination."</p>
<p>The 5th section of the act of June 22, 1874, under which this order was made, is in the following words, to wit:</p>
<p>"In all suits and proceedings other than criminal arising under any of the revenue laws of the United States, the attorney representing the government, whenever in his belief any <span class="star-pagination">*620</span> business book, invoice, or paper belonging to, or under the control of, the defendant or claimant, will tend to prove any allegation made by the United States, may make a written motion, particularly describing such book, invoice, or paper, and setting forth the allegation which he expects to prove; and thereupon the court in which suit or proceeding is pending may, at its discretion, issue a notice to the defendant or claimant to produce such book, invoice, or paper in court, at a day and hour to be specified in said notice, which, together with a copy of said motion, shall be served formally on the defendant or claimant by the United States marshal by delivering to him a certified copy thereof, or otherwise serving the same as original notices of suit in the same court are served; and if the defendant or claimant shall fail or refuse to produce such book, invoice, or paper in obedience to such notice, the allegations stated in the said motion shall be taken as confessed, unless his failure or refusal to produce the same shall be explained to the satisfaction of the court. And if produced the said attorney shall be permitted, under the direction of the court, to make examination (at which examination the defendant, or claimant, or his agent, may be present) of such entries in said book, invoice, or paper as relate to or tend to prove the allegation aforesaid, and may offer the same in evidence on behalf of the United States. But the owner of said books and papers, his agent or attorney, shall have, subject to the order of the court, the custody of them, except pending their examination in court as aforesaid." <span class="citation no-link">18 Stat. 187</span>.</p>
<p>This section was passed in lieu of the 2d section of the act of March 2, 1867, entitled "An act to regulate the Disposition of the Proceeds of Fines, Penalties, and Forfeitures incurred under the Laws relating to the Customs and for other Purposes," <span class="citation no-link">14 Stat. 547</span>, which section of said last-mentioned statute authorized the district judge, on complaint and affidavit that any fraud on the revenue had been committed by any person interested or engaged in the importation of merchandise, to issue his warrant to the marshal to enter any premises where any invoices, books, or papers were deposited relating to such merchandise, and take possession of such books and papers and <span class="star-pagination">*621</span> produce them before said judge, to be subject to his order, and allowed to be examined by the collector, and to be retained as long as the judge should deem necessary. This law being in force at the time of the revision, was incorporated into §§ 3091, 3092, 3093 of the Revised Statutes.</p>
<p>The section last recited was passed in lieu of the 7th section of the act of March 3, 1863, entitled "An act to prevent and punish Frauds upon the Revenue, to provide for the more certain and speedy Collection of Claims in Favor of the United States, and for other Purposes." <span class="citation no-link">12 Stat. 737</span>. The 7th section of this act was in substance the same as the 2d section of the act of 1867, except that the warrant was to be directed to the collector instead of the marshal. It was the first legislation of the kind that ever appeared on the statute book of the United States, and, as seen from its date, was adopted at a period of great national excitement, when the powers of the government were subjected to a severe strain to protect the national existence.</p>
<p>The clauses of the Constitution, to which it is contended that these laws are repugnant, are the Fourth and Fifth Amendments. The Fourth declares, "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no warrants shall issue, but upon probable cause, supported by oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." The Fifth Article, amongst other things, declares that no person "shall be compelled in any criminal case to be a witness against himself."</p>
<p>But, in regard to the Fourth Amendment, it is contended that, whatever might have been alleged against the constitutionality of the acts of 1863 and 1867, that of 1874, under which the order in the present case was made, is free from constitutional objection, because it does not authorize the search and seizure of books and papers, but only requires the defendant or claimant to produce them. That is so; but it declares that if he does not produce them, the allegations which it is affirmed they will prove shall be taken as confessed. This is tantamount <span class="star-pagination">*622</span> to compelling their production; for the prosecuting attorney will always be sure to state the evidence expected to be derived from them as strongly as the case will admit of. It is true that certain aggravating incidents of actual search and seizure, such as forcible entry into a man's house and searching amongst his papers, are wanting, and to this extent the proceeding under the act of 1874 is a mitigation of that which was authorized by the former acts; but it accomplishes the substantial object of those acts in forcing from a party evidence against himself. It is our opinion, therefore, that a compulsory production of a man's private papers to establish a criminal charge against him, or to forfeit his property, is within the scope of the Fourth Amendment to the Constitution, in all cases in which a search and seizure would be; because it is a material ingredient, and effects the sole object and purpose of search and seizure.</p>
<p>The principal question, however, remains to be considered. Is a search and seizure, or, what is equivalent thereto, a compulsory production of a man's private papers, to be used in evidence against him in a proceeding to forfeit his property for alleged fraud against the revenue laws  is such a proceeding for such a purpose an "<i>unreasonable</i> search and seizure" within the meaning of the Fourth Amendment of the Constitution? or, is it a legitimate proceeding? It is contended by the counsel for the government, that it is a legitimate proceeding, sanctioned by long usage, and the authority of judicial decision. No doubt long usage, acquiesced in by the courts, goes a long way to prove that there is some plausible ground or reason for it in the law, or in the historical facts which have imposed a particular construction of the law favorable to such usage. It is a maxim that, <i>consuetudo est optimus interpres legum;</i> and another maxim that, <i>contemporanea expositio est optima et fortissima in lege.</i> But we do not find any long usage, or any contemporary construction of the Constitution, which would justify any of the acts of Congress now under consideration. As before stated, the act of 1863 was the first act in this country, and, we might say, either in this country or in England, so far as we have been able to ascertain, which authorized the <span class="star-pagination">*623</span> search and seizure of a man's private papers, or the compulsory production of them, for the purpose of using them in evidence against him in a criminal case, or in a proceeding to enforce the forfeiture of his property. Even the act under which the obnoxious writs of assistance were issued<sup>[*]</sup> did not go as far as this, but only authorized the examination of ships and vessels, and persons found therein, for the purpose of finding goods prohibited to be imported or exported, or on which the duties were not paid, and to enter into and search any suspected vaults, cellars, or warehouses for such goods. The search for and seizure of stolen or forfeited goods, or goods liable to duties and concealed to avoid the payment thereof, are totally different things from a search for and seizure of a man's private books and papers for the purpose of obtaining information therein contained, or of using them as evidence against him. The two things differ <i>toto clo.</i> In the one case, the government is entitled to the possession of the property; in the other it is not. The seizure of stolen goods is authorized by the common law; and the seizure of goods forfeited for a breach of the revenue laws, or concealed to avoid the duties payable on them, has been authorized by English statutes for at least two centuries past;<sup>[]</sup> and the like seizures have been authorized by our own revenue acts from the commencement of the government. The first statute passed by Congress to regulate the collection of duties, the act of July 31, 1789, <span class="citation no-link">1 Stat. 29</span>, 43, contains provisions to this effect. As this act was passed by the same Congress which proposed for adoption the original amendments to the Constitution, it is clear that the members of that body did not regard searches and seizures of this kind as "unreasonable," and they are not embraced within the prohibition of the amendment. So, also, the supervision authorized to be exercised by officers of the revenue over the manufacture or custody of excisable articles, and the entries thereof in books required by law <span class="star-pagination">*624</span> to be kept for their inspection, are necessarily excepted out of the category of unreasonable searches and seizures. So, also, the laws which provide for the search and seizure of articles and things which it is unlawful for a person to have in his possession for the purpose of issue or disposition, such as counterfeit coin, lottery tickets, implements of gambling, &amp;c., are not within this category. <i>Commonwealth</i> v. <i>Dana,</i> 2 Met. (Mass.) 329. Many other things of this character might be enumerated. The entry upon premises, made by a sheriff or other officer of the law, for the purpose of seizing goods and chattels by virtue of a judicial writ, such as an attachment, a sequestration, or an execution, is not within the prohibition of the Fourth or Fifth Amendment, or any other clause of the Constitution; nor is the examination of a defendant under oath after an ineffectual execution, for the purpose of discovering secreted property or credits, to be applied to the payment of a judgment against him, obnoxious to those amendments.</p>
<p>But, when examined with care, it is manifest that there is a total unlikeness of these official acts and proceedings to that which is now under consideration. In the case of stolen goods, the owner from whom they were stolen is entitled to their possession; and in the case of excisable or dutiable articles, the government has an interest in them for the payment of the duties thereon, and until such duties are paid has a right to keep them under observation, or to pursue and drag them from concealment; and in the case of goods seized on attachment or execution, the creditor is entitled to their seizure in satisfaction of his debt; and the examination of a defendant under oath to obtain a discovery of concealed property or credits is a proceeding merely civil to effect the ends of justice, and is no more than what the court of chancery would direct on a bill for discovery. Whereas, by the proceeding now under consideration, the court attempts to extort from the party his private books and papers to make him liable for a penalty or to forfeit his property.</p>
<p>In order to ascertain the nature of the proceedings intended by the Fourth Amendment to the Constitution under the terms "unreasonable searches and seizures," it is only necessary to <span class="star-pagination">*625</span> recall the contemporary or then recent history of the controversies on the subject, both in this country and in England. The practice had obtained in the colonies of issuing writs of assistance to the revenue officers, empowering them, in their discretion, to search suspected places for smuggled goods, which James Otis pronounced "the worst instrument of arbitrary power, the most destructive of English liberty, and the fundamental principles of law, that ever was found in an English law book;" since they placed "the liberty of every man in the hands of every petty officer."<sup>[*]</sup> This was in February, 1761, in Boston, and the famous debate in which it occurred was perhaps the most prominent event which inaugurated the resistance of the colonies to the oppressions of the mother country. "Then and there," said John Adams, "then and there was the first scene of the first act of opposition to the arbitrary claims of Great Britain. Then and there the child Independence was born."</p>
<p>These things, and the events which took place in England immediately following the argument about writs of assistance in Boston, were fresh in the memories of those who achieved our independence and established our form of government. In the period from 1762, when the North Briton was started by John Wilkes, to April, 1766, when the House of Commons passed resolutions condemnatory of general warrants, whether for the seizure of persons or papers, occurred the bitter controversy between the English government and Wilkes, in which the latter appeared as the champion of popular rights, and was, indeed, the pioneer in the contest which resulted in the abolition of some grievous abuses which had gradually crept into the administration of public affairs. Prominent and principal among these was the practice of issuing general <span class="star-pagination">*626</span> warrants by the Secretary of State, for searching private houses for the discovery and seizure of books and papers that might be used to convict their owner of the charge of libel. Certain numbers of the North Briton, particularly No. 45, had been very bold in denunciation of the government, and were esteemed heinously libellous. By authority of the secretary's warrant Wilkes's house was searched, and his papers were indiscriminately seized. For this outrage he sued the perpetrators and obtained a verdict of £1000 against Wood, one of the party who made the search, and £4000 against Lord Halifax, the Secretary of State who issued the warrant. The case, however, which will always be celebrated as being the occasion of Lord Camden's memorable discussion of the subject, was that of <i>Entick</i> v. <i>Carrington and Three Other King's Messengers,</i> reported at length in 19 Howell's State Trials, 1029. The action was trespass for entering the plaintiff's dwelling-house in November, 1762, and breaking open his desks, boxes, &amp;c., and searching and examining his papers. The jury rendered a special verdict, and the case was twice solemnly argued at the bar. Lord Camden pronounced the judgment of the court in Michaelmas Term, 1765, and the law as expounded by him has been regarded as settled from that time to this, and his great judgment on that occasion is considered as one of the landmarks of English liberty. It was welcomed and applauded by the lovers of liberty in the colonies as well as in the mother country. It is regarded as one of the permanent monuments of the British Constitution, and is quoted as such by the English authorities on that subject down to the present time.<sup>[*]</sup></p>
<p>As every American statesmen, during our revolutionary and formative period as a nation, was undoubtedly familiar with this monument of English freedom, and considered it as the true and ultimate expression of constitutional law, it may be confidently asserted that its propositions were in the minds <span class="star-pagination">*627</span> of those who framed the Fourth Amendment to the Constitution, and were considered as sufficiently explanatory of what was meant by unreasonable searches and seizures. We think, therefore, it is pertinent to the present subject of discussion to quote somewhat largely from this celebrated judgment.</p>
<p>After describing the power claimed by the Secretary of State for issuing general search warrants, and the manner in which they were executed, Lord Camden says: "Such is the power, and, therefore, one would naturally expect that the law to warrant it should be clear in proportion as the power is exorbitant. If it is law, it will be found in our books; if it is not to be found there, it is not law.</p>
<p>"The great end for which men entered into society was to secure their property. That right is preserved sacred and incommunicable in all instances where it has not been taken away or abridged by some public law for the good of the whole. The cases where this right of property is set aside by positive law are various. Distresses, executions, forfeitures, taxes, &amp;c., are all of this description, wherein every man by common consent gives up that right for the sake of justice and the general good. By the laws of England, every invasion of private property, be it ever so minute, is a trespass. No man can set his foot upon my ground without my license, but he is liable to an action though the damage be nothing; which is proved by every declaration in trespass where the defendant is called upon to answer for bruising the grass and even treading upon the soil. If he admits the fact, he is bound to show, by way of justification, that some positive law has justified or excused him. The justification is submitted to the judges, who are to look into the books, and see if such a justification can be maintained by the text of the statute law, or by the principles of the common law. If no such excuse can be found or produced, the silence of the books is an authority, against the defendant, and the plaintiff must have judgment. According to this reasoning, it is now incumbent upon the defendants to show the law by which this seizure is warranted. If that cannot be done, it is a trespass.</p>
<p>"Papers are the owner's goods and chattels; they are his <span class="star-pagination">*628</span> dearest property; and are so far from enduring a seizure, that they will hardly bear an inspection; and though the eye cannot by the laws of England be guilty of a trespass, yet where private papers are removed and carried away the secret nature of those goods will be an aggravation of the trespass, and demand more considerable damages in that respect. Where is the written law that gives any magistrate such a power? I can safely answer, there is none; and, therefore, it is too much for us, without such authority, to pronounce a practice legal which would be subversive of all the comforts of society.</p>
<p>"But though it cannot be maintained by any direct law, yet it bears a resemblance, as was urged, to the known case of search and seizure for stolen goods. I answer that the difference is apparent. In the one, I am permitted to seize my own goods, which are placed in the hands of a public officer, till the felon's conviction shall entitle me to restitution. In the other, the party's own property is seized before and without conviction, and he has no power to reclaim his goods, even after his innocence is declared by acquittal.</p>
<p>"The case of searching for stolen goods crept into the law by imperceptible practice. No less a person than my Lord Coke denied its legality, 4 Inst. 176; and, therefore, if the two cases resembled each other more than they do, we have no right, without an act of Parliament, to adopt a new practice in the criminal law, which was never yet allowed from all antiquity. Observe, too, the caution with which the law proceeds in this singular case. There must be a full charge upon oath of a theft committed. The owner must swear that the goods are lodged in such a place. He must attend at the execution of the warrant, to show them to the officer, who must see that they answer the description... .</p>
<p>"If it should be said that the same law which has with so much circumspection guarded the case of stolen goods from mischief, would likewise in this case protect the subject by adding proper checks; would require proofs beforehand; would call up the servant to stand by and overlook; would require him to take an exact inventory, and deliver a copy: my answer is, that all these precautions would have been long <span class="star-pagination">*629</span> since established by law, if the power itself had been legal; and that the want of them is an undeniable argument against the legality of the thing."</p>
<p>Then, after showing that these general warrants for search and seizure of papers originated with the Star Chamber, and never had any advocates in Westminster Hall except Chief Justice Scroggs and his associates, Lord Camden proceeds to add:</p>
<p>"Lastly, it is urged as an argument of utility, that such a search is a means of detecting offenders by discovering evidence. I wish some cases had been shown, where the law forceth evidence out of the owner's custody by process. There is no process against papers in civil causes. It has been often tried, but never prevailed. Nay, where the adversary has by force or fraud got possession of your own proper evidence, there is no way to get it back but by action. In the criminal law such a proceeding was never heard of; and yet there are some crimes, such, for instance, as murder, rape, robbery, and house-breaking, to say nothing of forgery and perjury, that are more atrocious than libelling. But our law has provided no paper-search in these cases to help forward the conviction. Whether this proceedeth from the gentleness of the law towards criminals, or from a consideration that such a power would be more pernicious to the innocent than useful to the public, I will not say. It is very certain that the law obligeth no man to accuse himself; because the necessary means of compelling self-accusation, falling upon the innocent as well as the guilty, would be both cruel and unjust; and it would seem, that search for evidence is disallowed upon the same principle. Then, too, the innocent would be confounded with the guilty."</p>
<p>After a few further observations, his Lordship concluded thus: "I have now taken notice of everything that has been urged upon the present point; and upon the whole we are all of opinion, that the warrant to seize and carry away the party's papers in the case of a seditious libel, is illegal and void."<sup>[*]</sup></p>
<p><span class="star-pagination">*630</span> The principles laid down in this opinion affect the very essence of constitutional liberty and security. They reach farther than the concrete form of the case then before the court, with its adventitious circumstances; they apply to all invasions on the part of the government and its employés of the sanctity of a man's home and the privacies of life. It is not the breaking of his doors, and the rummaging of his drawers, that constitutes the essence of the offence; but it is the invasion of his indefeasible right of personal security, personal liberty and private property, where that right has never been forfeited by his conviction of some public offence,  it is the invasion of this sacred right which underlies and constitutes the essence of Lord Camden's judgment. Breaking into a house and opening boxes and drawers are circumstances of aggravation; but any forcible and compulsory extortion of a man's own testimony or of his private papers to be used as evidence to convict him of crime or to forfeit his goods, is within the condemnation of that judgment. In this regard the Fourth and Fifth Amendments run almost into each other.</p>
<p>Can we doubt that when the Fourth and Fifth Amendments to the Constitution of the United States were penned and adopted, the language of Lord Camden was relied on as expressing the true doctrine on the subject of searches and seizures, and as furnishing the true criteria of the reasonable and "unreasonable" character of such seizures? Could the men who proposed those amendments, in the light of Lord Camden's opinion, have put their hands to a law like those of March 3, 1863, and March 2, 1867, before recited? If they could not, would they have approved the 5th section of the act of June 22, 1874, which was adopted as a substitute for the previous laws? It seems to us that the question cannot admit of a doubt. They never would have approved of them. The struggles against arbitrary power in which they had been engaged for more than twenty years, would have been too deeply engraved in their memories to have allowed them to approve of such insidious disguises of the old grievance which they had so deeply abhorred.</p>
<p>The views of the first Congress on the question of compelling <span class="star-pagination">*631</span> a man to produce evidence against himself may be inferred from a remarkable section of the judiciary act of 1789. The 15th section of that act introduced a great improvement in the law of procedure. The substance of it is found in § 724 of the Revised Statutes, and the section as originally enacted is as follows, to wit:</p>
<p>"All the said courts of the United States shall have power in the trial of actions at law, on motion and due notice thereof being given, to require the parties to produce books or writings in their possession or power, which contain evidence pertinent to the issue, <i>in cases and under circumstances where they might be compelled to produce the same by the ordinary rules of proceeding in chancery;</i> and if a plaintiff shall fail to comply with such order to produce books or writings, it shall be lawful for the courts respectively, on motion, to give the like judgment for the defendant as in cases of nonsuit; and if a defendant shall fail to comply with such order to produce books or writings, it shall be lawful for the courts respectively, on motion as aforesaid, to give judgment against him or her by default."<sup>[*]</sup></p>
<p>The restriction of this proceeding to "cases and under circumstances where they [the parties] might be compelled to produce the same [books or writings] by the ordinary rules of proceeding in chancery," shows the wisdom of the Congress of 1789. The court of chancery had for generations been weighing and balancing the rules to be observed in granting discovery on bills filed for that purpose, in the endeavor to fix upon such as would best secure the ends of justice. To go beyond the point to which that court had gone may well have been thought hazardous. Now it is elementary knowledge, that one cardinal rule of the court of chancery is never to decree a discovery which might tend to convict the party of a crime, or to forfeit his property.<sup>[]</sup> And any compulsory discovery by extorting the party's oath, or compelling the production of his <span class="star-pagination">*632</span> private books and papers, to convict him of crime, or to forfeit his property, is contrary to the principles of a free government. It is abhorrent to the instincts of an Englishman; it is abhorrent to the instincts of an American. It may suit the purposes of despotic power; but it cannot abide the pure atmosphere of political liberty and personal freedom.</p>
<p>It is proper to observe that when the objectionable features of the acts of 1863 and 1867 were brought to the attention of Congress, it passed an act to obviate them. By the act of February 25, 1868, <span class="citation no-link">15 Stat. 37</span>, entitled "An act for the Protection in certain Cases of Persons making Disclosures as Parties, or testifying as Witnesses," the substance of which is incorporated in § 860 of the Revised Statutes, it was enacted "that no answer or other pleading of any party, and no discovery, or evidence obtained by means of any judicial proceeding from any party or witness in this or any foreign country, shall be given in evidence, or in any manner used against such party or witness, or his property or estate, in any court of the United States, or in any proceeding by or before any officer of the United States, in respect to any crime, or for the enforcement of any penalty or forfeiture by reason of any act or omission of such party or witness."</p>
<p>This act abrogated and repealed the most objectionable part of the act of 1867 (which was then in force) and deprived the government officers of the convenient method afforded by it for getting evidence in suits of forfeiture; and this is probably the reason why the 5th section of the act of 1874 was afterwards passed. No doubt it was supposed that in this new form, couched as it was in almost the language of the 15th section of the old judiciary act, except leaving out the restriction to cases in which the court of chancery would decree a discovery, it would be free from constitutional objection. But we think it has been made to appear that this result has not been attained; and that the law, though very speciously worded, is still obnoxious to the prohibition of the Fourth Amendment of the Constitution, as well as of the Fifth.</p>
<p>It has been thought by some respectable members of the profession that the two acts, that of 1868 and that of 1874, as being in <i>pari materia,</i> might be construed together so as to restrict <span class="star-pagination">*633</span> the operation of the latter to cases other than those of forfeiture; and that such a construction of the two acts would obviate the necessity of declaring the act of 1874 unconstitutional. But as the act of 1874 was intended as a revisory act on the subject of revenue frauds and prosecutions therefor, and as it expressly repeals the 2d section of the act of 1867, but does not repeal the act of 1868, and expressly excepts criminal suits and proceedings, and does not except suits for penalties and forfeitures, it would hardly be admissible to consider the act of 1868 as having any influence over the construction of the act of 1874. For the purposes of this discussion we must regard the 5th section of the latter act as independent of the act of 1868.</p>
<p>Reverting then to the peculiar phraseology of this act, and to the information in the present case, which is founded on it, we have to deal with an act which expressly excludes criminal proceedings from its operation (though embracing civil suits for penalties and forfeitures), and with an information not technically a criminal proceeding, and neither, therefore, within the literal terms of the Fifth Amendment to the Constitution any more than it is within the literal terms of the Fourth. Does this relieve the proceedings or the law from being obnoxious to the prohibitions of either? We think not; we think they are within the spirit of both.</p>
<p>We have already noticed the intimate relation between the two amendments. They throw great light on each other. For the "unreasonable searches and seizures" condemned in the Fourth Amendment are almost always made for the purpose of compelling a man to give evidence against himself, which in criminal cases is condemned in the Fifth Amendment; and compelling a man "in a criminal case to be a witness against himself," which is condemned in the Fifth Amendment, throws light on the question as to what is an "unreasonable search and seizure" within the meaning of the Fourth Amendment. And we have been unable to perceive that the seizure of a man's private books and papers to be used in evidence against him is substantially different from compelling him to be a witness against himself. We think it is within the clear intent and meaning of those terms. We are also clearly of opinion that <span class="star-pagination">*634</span> proceedings instituted for the purpose of declaring the forfeiture of a man's property by reason of offences committed by him, though they may be civil in form, are in their nature criminal. In this very case, the ground of forfeiture as declared in the 12th section of the act of 1874, on which the information is based, consists of certain acts of fraud committed against the public revenue in relation to imported merchandise, which are made criminal by the statute; and it is declared, that the offender shall be fined not exceeding $5000 nor less than $50, or be imprisoned not exceeding two years, or both; and in addition to such fine such merchandise shall be forfeited. These are the penalties affixed to the criminal acts; the forfeiture sought by this suit being one of them. If an indictment had been presented against the claimants, upon conviction the forfeiture of the goods could have been included in the judgment. If the government prosecutor elects to waive an indictment, and to file a civil information against the claimants  that is, civil in form  can he by this device take from the proceeding its criminal aspect and deprive the claimants of their immunities as citizens, and extort from them a production of their private papers, or, as an alternative, a confession of guilt? This cannot be. The information, though technically a civil proceeding, is in substance and effect a criminal one. As showing the close relation between the civil and criminal proceedings on the same statute in such cases, we may refer to the recent case of <i>Coffey</i> v. <i>The United States, ante,</i> 436; in which we decided that an acquittal on a criminal information was a good plea in bar to a civil information for the forfeiture of goods, arising upon the same acts. As, therefore, suits for penalties and forfeitures incurred by the commission of offences against the law, are of this quasi-criminal nature, we think that they are within the reason of criminal proceedings for all the purposes of the Fourth Amendment of the Constitution, and of that portion of the Fifth Amendment which declares that no person shall be compelled in any criminal case to be a witness against himself; and we are further of opinion that a compulsory production of the private books and papers of the owner of goods sought to be forfeited in such a suit is compelling <span class="star-pagination">*635</span> him to be a witness against himself, within the meaning of the Fifth Amendment to the Constitution, and is the equivalent of a search and seizure  and an unreasonable search and seizure  within the meaning of the Fourth Amendment. Though the proceeding in question is divested of many of the aggravating incidents of actual search and seizure, yet, as before said, it contains their substance and essence, and effects their substantial purpose. It may be that it is the obnoxious thing in its mildest and least repulsive form; but illegitimate and unconstitutional practices get their first footing in that way, namely, by silent approaches and slight deviations from legal modes of procedure. This can only be obviated by adhering to the rule that constitutional provisions for the security of person and property should be liberally construed. A close and literal construction deprives them of half their efficacy, and leads to gradual depreciation of the right, as if it consisted more in sound than in substance. It is the duty of courts to be watchful for the constitutional rights of the citizen, and against any stealthy encroachments thereon. Their motto should be <i>obsta principiis.</i> We have no doubt that the legislative body is actuated by the same motives; but the vast accumulation of public business brought before it sometimes prevents it, on a first presentation, from noticing objections which become developed by time and the practical application of the objectionable law.</p>
<p>There have been several decisions in the Circuit and District Courts sustaining the constitutionality of the law under consideration, as well as the prior laws of 1863 and 1867. The principal of these are <i>Stockwell</i> v. <i>United States,</i> 3 Clifford, 284; <i>In re Platt and Boyd,</i> <span class="citation" data-id="8635885"><a href="/opinion/8656040/in-re-platt/" aria-description="Citation for case: In re Platt">7 Ben. 261</a></span>; <i>United States</i> v. <i>Hughes,</i> 12 Blatchford, 553; <i>United States</i> v. <i>Mason,</i> <span class="citation" data-id="8639082"><a href="/opinion/8659227/united-states-v-mason/" aria-description="Citation for case: United States v. Mason">6 Bissell, 350</a></span>; <i>United States</i> v. <i>Three Tons of Coal,</i> <span class="citation" data-id="8686970"><a href="/opinion/8703793/united-states-v-three-tons-of-coal/" aria-description="Citation for case: United States v. Three Tons of Coal">6 Bissell, 379</a></span>; <i>United States</i> v. <i>Distillery No. Twenty-eight,</i> <span class="citation" data-id="8638551"><a href="/opinion/8658698/united-states-v-distillery-no-twenty-eight/" aria-description="Citation for case: United States v. Distillery No. Twenty-Eight">6 Bissell, 483</a></span>. The first and leading case was that of <i>Stockwell</i> v. <i>United States</i><i>,</i> decided by Mr. Justice Clifford and Judge Shepley, the law under discussion being that of 1867. Justice Clifford delivered the opinion, and relied principally upon the collection statutes, which authorized the seizure of goods liable to duty, as being a contemporaneous <span class="star-pagination">*636</span> exposition of the amendments, and as furnishing precedents of analogous laws to that complained of. As we have already considered the bearing of these laws on the subject of discussion, it is unnecessary to say anything more in relation to them. The learned justice seemed to think that the power to institute such searches and seizures as the act of 1867 authorized, was necessary to the efficient collection of the revenue, and that no greater objection can be taken to a warrant to search for books, invoices, and other papers appertaining to an illegal importation than to one authorizing a search for the imported goods; and he concluded that, guarded as the new provision is, it is scarcely possible that the citizen can have any just ground of complaint. It seems to us that these considerations fail to meet the most serious objections to the validity of the law. The other cases followed that of <i>Stockwell</i> v. <i>United States</i> as a precedent, with more or less independent discussion of the subject. The case of <i><span class="citation" data-id="8635885"><a href="/opinion/8656040/in-re-platt/" aria-description="Citation for case: In re Platt">Platt and Boyd</a></span>,</i> decided in the District Court for the Southern District of New York, was also under the act of 1867, and the opinion in that case is quite an elaborate one; but, of course, the previous decision of the Circuit Court in the Stockwell case had a governing influence on the District Court. The other cases referred to were under the 5th section of the act of 1874. The case of <i>United States</i> v. <i>Hughes</i> came up, first, before Judge Blatchford in the District Court in 1875. <span class="citation" data-id="8638870"><a href="/opinion/8659015/united-states-v-hughes/" aria-description="Citation for case: United States v. Hughes">8 Ben. 29</a></span>. It was an action of debt to recover a penalty under the customs act, and the judge held that the 5th section of the act of 1874, in its application to suits for penalties incurred before the passage of the act, was an <i>ex post facto</i> law, and therefore, as to them, was unconstitutional and void; but he granted an order <i>pro forma</i> to produce the books and papers required, in order that the objection might come up on the offer to give them in evidence. They were produced in obedience to the order, and offered in evidence by the district attorney, but were not admitted. The district attorney then served upon one of the defendants a subpna <i>duces tecum,</i> requiring him to produce the books and papers; and this being declined, he moved for an order to compel him to produce them; but the Court refused to make such order. The books and <span class="star-pagination">*637</span> papers referred to had been seized under the act of 1867, but were returned to the defendants under a stipulation to produce them on the trial. The defendants relied not only on the unconstitutionality of the laws, but on the act of 1868, before referred to, which prohibited evidence obtained from a party by a judicial proceeding from being used against him in any prosecution for a crime, penalty, or forfeiture. Judgment being rendered for the defendant, the case was carried to the Circuit Court by writ of error, and, in that court, Mr. Justice Hunt held that the act of 1868 referred only to personal testimony or discovery obtained from a party or witness, and not to books or papers wrested from him; and, as to the constitutionality of the law, he merely referred to the case of Stockwell, and the judgment of the District Court was reversed. In view of what has been already said, we think it unnecessary to make any special observations on this decision. In <i>United States</i> v. <i><span class="citation" data-id="8639082"><a href="/opinion/8659227/united-states-v-mason/" aria-description="Citation for case: United States v. Mason">Mason</a></span></i><i>,</i> Judge Blodgett took the distinction that, in proceedings <i>in rem</i> for a forfeiture, the parties are not required by a proceeding under the act of 1874 to testify or furnish evidence against themselves, because the suit is not against them, but against the property. But where the owner of the property has been admitted as a claimant, we cannot see the force of this distinction; nor can we assent to the proposition that the proceeding is not, in effect, a proceeding against the owner of the property, as well as against the goods; for it is his breach of the laws which has to be proved to establish the forfeiture, and it is his property which is sought to be forfeited; and to require such an owner to produce his private books and papers, in order to prove his breach of the laws, and thus to establish the forfeiture of his property, is surely compelling him to furnish evidence against himself. In the words of a great judge, "Goods, as goods, cannot offend, forfeit, unlade, pay duties, or the like, but men whose goods they are."<sup>[*]</sup></p>
<p>The only remaining case decided in the United States courts <span class="star-pagination">*638</span> to which we shall advert is that of <i>United States</i> v. <i><span class="citation" data-id="8638551"><a href="/opinion/8658698/united-states-v-distillery-no-twenty-eight/" aria-description="Citation for case: United States v. Distillery No. Twenty-Eight">Distillery No. Twenty-eight</a></span></i><i>.</i> In that case Judge Gresham adds to the view of Judge Blodgett, in <i>United States</i> v. <i><span class="citation" data-id="8639082"><a href="/opinion/8659227/united-states-v-mason/" aria-description="Citation for case: United States v. Mason">Mason</a></span></i><i>,</i> the further suggestion, that as in a proceeding <i>in rem</i> the owner is not a party, he might be compelled by a subpna <i>duces tecum</i> to produce his books and papers like any other witness; and that the warrant or notice for search and seizure, under the act of 1874, does nothing more. But we cannot say that we are any better satisfied with this supposed solution of the difficulty. The assumption that the owner may be cited as a witness in a proceeding to forfeit his property seems to us gratuitous. It begs the question at issue. A witness, as well as a party, is protected by the law from being compelled to give evidence that tends to criminate him, or to subject his property to forfeiture. <i>Queen</i> v. <i>Newell,</i> Parker, 269; 1 Greenleaf on Evid., §§ 451-453. But, as before said, although the owner of goods, sought to be forfeited by a proceeding <i>in rem,</i> is not the nominal party, he is, nevertheless, the substantial party to the suit; he certainly is so, after making claim and defence; and, in a case like the present, he is entitled to all the privileges which appertain to a person who is prosecuted for a forfeiture of his property by reason of committing a criminal offence.</p>
<p>We find nothing in the decisions to change our views in relation to the principal question at issue.</p>
<p>We think that the notice to produce the invoice in this case, the order by virtue of which it was issued, and the law which authorized the order, were unconstitutional and void, and that the inspection by the district attorney of said invoice, when produced in obedience to said notice, and its admission in evidence by the court, were erroneous and unconstitutional proceedings. We are of opinion, therefore, that</p>
<p><i>The judgment of the Circuit Court should be reversed, and the cause remanded, with directions to award a new trial.</i></p>
<p>MR. JUSTICE MILLER, with whom was the CHIEF JUSTICE, concurring:</p>
<p>I concur in the judgment of the court, reversing that of the Circuit Court, and in so much of the opinion of this court as <span class="star-pagination">*639</span> holds the 5th section of the act of 1874 void as applicable to the present case.</p>
<p>I am of opinion that this is a criminal case within the meaning of that clause of the Fifth Amendment to the Constitution of the United States which declares that no person "shall be compelled in any criminal case to be a witness against himself."</p>
<p>And I am quite satisfied that the effect of the act of Congress is to compel the party on whom the order of the court is served to be a witness against himself. The order of the court under the statute is in effect a subpna <i>duces tecum,</i> and, though the penalty for the witness's failure to appear in court with the criminating papers is not fine and imprisonment, it is one which may be made more severe, namely, to have charges against him of a criminal nature, taken for confessed, and made the foundation of the judgment of the court. That this is within the protection which the Constitution intended against compelling a person to be a witness against himself, is, I think, quite clear.</p>
<p>But this being so, there is no reason why this court should assume that the action of the court below, in requiring a party to produce certain papers as evidence on the trial, authorizes an unreasonable search or seizure of the house, papers, or effects of that party.</p>
<p>There is in fact no search and no seizure authorized by the statute. No order can be made by the court under it which requires or permits anything more than service of notice on a party to the suit. That there may be no mistake as to the effect of the statute and the power to be exercised under it, I give the section here <i>verbatim:</i></p>
<p>"SEC. 5. That in all suits and proceedings other than criminal arising under any of the revenue laws of the United States, the attorney representing the Government, whenever, in his belief, any business book, invoice, or paper, belonging to or under the control of the defendant or claimant, will tend to prove any allegation made by the United States, may make a written motion, particularly describing such book, invoice, or paper, and setting forth the allegation which he expects to prove; and thereupon the court in which suit or proceeding is <span class="star-pagination">*640</span> pending may, at its discretion, issue a notice to the defendant or claimant to produce such book, invoice, or paper, in court, at a day and hour to be specified in said notice, which, together with a copy of said motion, shall be served formally on the defendant or claimant, by the United States marshal, by delivering to him a certified copy thereof, or otherwise serving the same as original notices of suit in the same court are served; and if the defendant or claimant shall fail or refuse to produce such book, invoice, or paper in obedience to such notice, the allegations stated in the said motion shall be taken as confessed, unless his failure or refusal to produce the same shall be explained to the satisfaction of the court. And if produced, the said attorney shall be permitted, under the direction of the court, to make examination (at which examination the defendant or claimant, or his agent, may be present) of such entries in said book, invoice, or paper as relate to or tend to prove the allegation aforesaid, and may offer the same in evidence on behalf of the United States. But the owner of said books and papers, his agent or attorney, shall have, subject to the order of the court, the custody of them, except pending their examination in court as aforesaid." <span class="citation no-link">18 Stat. 187</span>.</p>
<p>Nothing in the nature of a search is here hinted at. Nor is there any seizure, because the party is not required at any time to part with the custody of the papers. They are to be produced in court, and, when produced, the United States attorney is permitted, under the direction of the court, to make examination in presence of the claimant, and may offer in evidence such entries in the books, invoices, or papers as relate to the issue. The act is careful to say that "the owner of said books and papers, his agent or attorney, shall have, subject to the order of the court, the custody of them, except pending their examination in court as aforesaid."</p>
<p>The Fourth Amendment says: "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no warrant shall issue, but upon probable cause, supported by oath or affirmation, and particularly describing the place to be searched and the person or thing to be seized."</p>
<p><span class="star-pagination">*641</span> The things here forbidden are two  search and seizure. And not all searches nor all seizures are forbidden, but only those that are unreasonable. Reasonable searches, therefore, may be allowed, and if the thing sought be found, it may be seized.</p>
<p>But what search does this statute authorize? If the mere service of a notice to produce a paper to be used as evidence, which the party can obey or not as he chooses is a search, then a change has taken place in the meaning of words, which has not come within my reading, and which I think was unknown at the time the Constitution was made. The searches meant by the Constitution were such as led to seizure when the search was successful. But the statute in this case uses language carefully framed to forbid any seizure under it, as I have already pointed out.</p>
<p>While the framers of the Constitution had their attention drawn, no doubt, to the abuses of this power of searching private houses and seizing private papers, as practiced in England, it is obvious that they only intended to restrain the abuse, while they did not abolish the power. Hence it is only <i>unreasonable</i> searches and seizures that are forbidden, and the means of securing this protection was by abolishing searches under warrants, which were called general warrants, because they authorized searches in any place, for any thing.</p>
<p>This was forbidden, while searches founded on affidavits, and made under warrants which described the thing to be searched for, the person and place to be searched, are still permitted.</p>
<p>I cannot conceive how a statute aptly framed to require the production of evidence in a suit by mere service of notice on the party, who has that evidence in his possession, can be held to authorize an unreasonable search or seizure, when no seizure is authorized or permitted by the statute.</p>
<p>I am requested to say that the CHIEF JUSTICE concurs in this opinion.</p>
<h2>NOTES</h2>
<p>[*]  <i>Note by the Court.</i>  13 &amp; 14 Car. 2, c. 11, § 5.</p>
<p>[]  <i>Note by the Court.</i>  12 Car. 2, c. 19; 13 &amp; 14 Car. 2, c. 11; 6 &amp; 7 W. &amp; M., c. 1; 6 Geo. 1, c. 21; 26 Geo. 3, c. 59; 29 Geo. 3, c. 68, § 153; &amp;c.; and see the article "Excise, &amp;c.," in Burn's Justice, and Williams's Justice, <i>passim,</i> and Evans's Statutes, vol. 2, p. 221, sub-pages 176, 190, 225, 361, 431, 447.</p>
<p>[*]  <i>Note by the Court.</i>  Cooley's Constitutional Limitations, 301-303, (5th ed. 368, 369). A very full and interesting account of this discussion will be found in the works of John Adams, vol. 2, Appendix A, pp. 523-525; vol. 10, pp. 183, 233, 244, 256, &amp;c., and in Quincy's Reports, pp. 469-482: and see <i>Paxton's Case,</i> do. 51-57, which was argued in November of the same year (1761). An elaborate history of the writs of assistance is given in the Appendix to Quincy's Reports, above referred to, written by Horace Gray, Jr., Esq., now a member of this court.</p>
<p>[*]  <i>Note by the Court.</i>  See May's Constitutional History of England, vol. 3, (American ed., vol. 2) chap. 11; Broom's Constitutional Law, 558; Cox's Institutions of the English Government, 437.</p>
<p>[*]  <i>Note by the Court.</i>  See further as to searches and seizures, Story on the Constitution, §§ 1901, 1902, and notes; Cooley's Constitutional Limitations, 299, (5th ed. 365); Sedgwick on Stat. and Const. Law, 2d Ed. 498; Wharton Com. on Amer. Law, § 560; <i>Robinson</i> v. <i>Richardson,</i> <span class="citation no-link">13 Gray, 454</span>.</p>
<p>[*]  <i>Note by the Court.</i>  Sixty-two years later a similar act was passed in England, viz., the act of 14 and 15 Vict., c. 99, § 6. See Pollock on Power of Courts to compel production of Documents, 5.</p>
<p>[]  <i>Note by the Court.</i>  See Pollock on Production of Documents, 27; 77 Law. Lib 12 [8].</p>
<p>[*]  <i>Note by the Court.</i>  Vaughan, C.J., in <i>Sheppard</i> v. <i>Gosnold,</i> Vaugh. 159, 172, approved by Ch. Baron Parker in <i>Mitchell qui tam</i> v. <i>Torup,</i> Parker, 227, 236.</p>

</div>
```

---

## GROUP: content/cases/Brady v. Maryland.md  (`case`, 5 assertions)

### content_page

```
---
title: "Brady v. Maryland"
type: case
citation: "373 U.S. 83 (1963)"
parallel_cite: "83 S. Ct. 1194; 10 L. Ed. 2d 215"
neutral_cite: 1963 U.S. LEXIS 1615
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1963
date_decided: 1963-05-13
docket: 490
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1963-05-13
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brady v. Maryland
  varies_by_point: false
  scope_note: "Foundational disclosure rule; later refined (not undermined) by Giglio and United States v. Bagley."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106598/brady-v-maryland/"
  cluster_id: 106598
  opinion_id: 106598
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Anchor"
related: ["[[Giglio v. United States]]", "[[United States v. Bagley]]", "[[Kyles v. Whitley]]"]
aliases: ["Brady v. MD"]
tags: ["case", "due-process", "brady", "disclosure", "exculpatory-evidence"]
holding: "The prosecution's suppression of evidence favorable to the accused that is material to guilt or punishment violates due process —…"
lake:
  record_id: Brady v. Maryland
  status: verified
  projected_at: 2026-07-06
---

# Brady v. Maryland

*373 U.S. 83 (1963)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Brady and a companion, Boblit, were tried separately for a murder committed in the course of a robbery. Brady admitted participating but insisted Boblit did the actual killing. Before trial Brady's counsel asked to see Boblit's statements; the prosecution turned over several but withheld the one in which Boblit admitted the killing. Brady discovered the withheld confession only after he had been convicted and sentenced to death.

## Issue
Whether the prosecution's suppression of evidence favorable to the accused, requested by the defense and material to guilt or punishment, violates due process.

## Rule
"We now hold that the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution." — 373 U.S. at 87. ^pin-87

## Application
Boblit's withheld confession was favorable to Brady and material to punishment — it bore directly on his comparative culpability and thus on the sentence. Because the State had suppressed it, due process was violated as to the punishment phase, although the Court agreed the violation did not require relitigating guilt where Brady had admitted his participation.

## Conclusion
The suppression of the favorable, material confession violated due process; the judgment limiting Brady's new trial to the question of punishment was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The rule was **extended** to impeachment evidence by [[Giglio v. United States]] and its materiality standard elaborated by [[United States v. Bagley]] and [[Kyles v. Whitley]].

## Appears on
- [[Brady and Giglio]] — *Key — Anchor*

## Sources
- *Brady v. Maryland*, 373 U.S. 83 (1963) — https://www.courtlistener.com/opinion/106598/brady-v-maryland/ — pinpoint: 87.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "402da357b5e067dc", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "373 U.S. 83 (1963)", "court": "U.S. Supreme Court", "neutral_cite": "1963 U.S. LEXIS 1615", "official_citation_present": true, "parallel_cite": "83 S. Ct. 1194; 10 L. Ed. 2d 215", "title": "Brady v. Maryland", "year": "1963"}}
{"assertion_id": "678adcc76e547fe0", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key — Anchor", "title": "Brady v. Maryland"}}
{"assertion_id": "68cd13ae94a8b226", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The prosecution's suppression of evidence favorable to the accused that is material to guilt or punishment violates due process —…", "title": "Brady v. Maryland"}}
{"assertion_id": "e5c4ffbddf8c4b5c", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1963-05-13", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Brady v. Maryland", "field_i_validity": "good_law", "scope_note": "Foundational disclosure rule; later refined (not undermined) by Giglio and United States v. Bagley.", "title": "Brady v. Maryland", "varies_by_point": "false"}}
{"assertion_id": "f71f3b433ebf698a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Brady v. Maryland"}}
```

### lake record — Brady v. Maryland

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brady v. Maryland",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Brady v. Maryland",
    "case_name_short": "Brady",
    "case_name_full": "Brady v. Maryland",
    "input_case_name": "Brady v. Maryland",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1963-05-13",
    "year": 1963,
    "docket": "490",
    "cluster_id": 106598,
    "lead_opinion_id": 106598,
    "sibling_ids": [
      106598,
      9422583,
      9422584
    ],
    "absolute_url": "/opinion/106598/brady-v-maryland/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "373 U.S. 83",
      "volume": "373",
      "reporter": "U.S.",
      "page": "83",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "83 S. Ct. 1194",
        "volume": "83",
        "reporter": "S. Ct.",
        "page": "1194",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 L. Ed. 2d 215",
        "volume": "10",
        "reporter": "L. Ed. 2d",
        "page": "215",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1963 U.S. LEXIS 1615",
        "volume": "1963",
        "reporter": "U.S. LEXIS",
        "page": "1615",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "373 U.S. 83",
        "volume": "373",
        "reporter": "U.S.",
        "page": "83",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 S. Ct. 1194",
        "volume": "83",
        "reporter": "S. Ct.",
        "page": "1194",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 L. Ed. 2d 215",
        "volume": "10",
        "reporter": "L. Ed. 2d",
        "page": "215",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1963 U.S. LEXIS 1615",
        "volume": "1963",
        "reporter": "U.S. LEXIS",
        "page": "1615",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "373 U.S. 83",
    "official_selection": {
      "court_class": "scotus",
      "selected": "373 U.S. 83",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-87",
      "page": null,
      "quote": "--- # Brady v. Maryland *373 U.S. 83 (1963)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Brady and a companion, Boblit, were tried separately for a murder committed in the course of a robbery. Brady admitted participating but insisted Boblit did the actual killing. Before trial Brady's counsel asked to see Boblit's statements; the prosecution turned over several but withheld the one in which Boblit admitted the killing. Brady discovered the withheld confession only after he had been convicted and sentenced to death. ## Issue Whether the prosecution's suppression of evidence favorable to the accused, requested by the defense and material to guilt or punishment, violates due process. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1963-05-13",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brady v. Maryland",
    "varies_by_point": false,
    "scope_note": "Foundational disclosure rule; later refined (not undermined) by Giglio and United States v. Bagley.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Jevric",
          "cluster_id": 10873877,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Faretta v. California",
          "cluster_id": 109309,
          "cite": [
            "45 L. Ed. 2d 562",
            "95 S. Ct. 2525",
            "422 U.S. 806",
            "1975 U.S. LEXIS 83"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bagley",
          "cluster_id": 111514,
          "cite": [
            "87 L. Ed. 2d 481",
            "105 S. Ct. 3375",
            "473 U.S. 667",
            "1985 U.S. LEXIS 130",
            "53 U.S.L.W. 5084"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wade",
          "cluster_id": 107486,
          "cite": [
            "18 L. Ed. 2d 1149",
            "87 S. Ct. 1926",
            "388 U.S. 218",
            "1967 U.S. LEXIS 1085"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schlup v. Delo",
          "cluster_id": 117893,
          "cite": [
            "130 L. Ed. 2d 808",
            "115 S. Ct. 851",
            "513 U.S. 298",
            "1995 U.S. LEXIS 701",
            "1995 WL 20524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. Carrier",
          "cluster_id": 111727,
          "cite": [
            "91 L. Ed. 2d 397",
            "106 S. Ct. 2639",
            "477 U.S. 478",
            "1986 U.S. LEXIS 66",
            "54 U.S.L.W. 4820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Imbler v. Pachtman",
          "cluster_id": 109387,
          "cite": [
            "47 L. Ed. 2d 128",
            "96 S. Ct. 984",
            "424 U.S. 409",
            "1976 U.S. LEXIS 25"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
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
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Giglio v. United States",
          "cluster_id": 108471,
          "cite": [
            "31 L. Ed. 2d 104",
            "92 S. Ct. 763",
            "405 U.S. 150",
            "1972 U.S. LEXIS 83"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'Sullivan v. Boerckel",
          "cluster_id": 118296,
          "cite": [
            "144 L. Ed. 2d 1",
            "119 S. Ct. 1728",
            "526 U.S. 838",
            "1999 U.S. LEXIS 4003"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Agurs",
          "cluster_id": 109506,
          "cite": [
            "49 L. Ed. 2d 342",
            "96 S. Ct. 2392",
            "427 U.S. 97",
            "1976 U.S. LEXIS 72"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyles v. Whitley",
          "cluster_id": 117923,
          "cite": [
            "131 L. Ed. 2d 490",
            "115 S. Ct. 1555",
            "514 U.S. 419",
            "1995 U.S. LEXIS 2845"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pace v. DiGuglielmo",
          "cluster_id": 142891,
          "cite": [
            "161 L. Ed. 2d 669",
            "125 S. Ct. 1807",
            "544 U.S. 408",
            "2005 U.S. LEXIS 3705",
            "5 Cal. Daily Op. Serv. 3526",
            "73 U.S.L.W. 4304",
            "18 Fla. L. Weekly Fed. S 250"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Strickler v. Greene",
          "cluster_id": 118307,
          "cite": [
            "144 L. Ed. 2d 286",
            "119 S. Ct. 1936",
            "527 U.S. 263",
            "1999 U.S. LEXIS 4191"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Martinez v. Ryan",
          "cluster_id": 625711,
          "cite": [
            "182 L. Ed. 2d 272",
            "132 S. Ct. 1309",
            "566 U.S. 1",
            "2012 U.S. LEXIS 2317"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donnelly v. DeChristoforo",
          "cluster_id": 109024,
          "cite": [
            "40 L. Ed. 2d 431",
            "94 S. Ct. 1868",
            "416 U.S. 637",
            "1974 U.S. LEXIS 138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marion",
          "cluster_id": 108420,
          "cite": [
            "30 L. Ed. 2d 468",
            "92 S. Ct. 455",
            "404 U.S. 307",
            "1971 U.S. LEXIS 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Phillips",
          "cluster_id": 110645,
          "cite": [
            "71 L. Ed. 2d 78",
            "102 S. Ct. 940",
            "455 U.S. 209",
            "1982 U.S. LEXIS 69"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Robbins",
          "cluster_id": 118332,
          "cite": [
            "145 L. Ed. 2d 756",
            "120 S. Ct. 746",
            "528 U.S. 259",
            "2000 U.S. LEXIS 825"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Trombetta",
          "cluster_id": 111206,
          "cite": [
            "81 L. Ed. 2d 413",
            "104 S. Ct. 2528",
            "467 U.S. 479",
            "1984 U.S. LEXIS 103",
            "52 U.S.L.W. 4744"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Youngblood",
          "cluster_id": 112156,
          "cite": [
            "102 L. Ed. 2d 281",
            "109 S. Ct. 333",
            "488 U.S. 51",
            "1988 U.S. LEXIS 5404"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCleskey v. Zant",
          "cluster_id": 112573,
          "cite": [
            "113 L. Ed. 2d 517",
            "111 S. Ct. 1454",
            "499 U.S. 467",
            "1991 U.S. LEXIS 2218",
            "59 U.S.L.W. 4288",
            "91 Cal. Daily Op. Serv. 2680",
            "91 Daily Journal DAR 4340"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moran v. Burbine",
          "cluster_id": 111614,
          "cite": [
            "89 L. Ed. 2d 410",
            "106 S. Ct. 1135",
            "475 U.S. 412",
            "1986 U.S. LEXIS 32",
            "54 U.S.L.W. 4265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herrera v. Collins",
          "cluster_id": 112808,
          "cite": [
            "122 L. Ed. 2d 203",
            "113 S. Ct. 853",
            "506 U.S. 390",
            "1993 U.S. LEXIS 1017"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garcetti v. Ceballos",
          "cluster_id": 145653,
          "cite": [
            "164 L. Ed. 2d 689",
            "126 S. Ct. 1951",
            "547 U.S. 410",
            "2006 U.S. LEXIS 4341"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Caldwell v. Mississippi",
          "cluster_id": 111471,
          "cite": [
            "86 L. Ed. 2d 231",
            "105 S. Ct. 2633",
            "472 U.S. 320",
            "1985 U.S. LEXIS 96",
            "53 U.S.L.W. 4743"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106598 OR 9422583 OR 9422584) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzU0MjY1NjAwMDAwJnM9MTA3OTc2NzImdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106598+OR+9422583+OR+9422584%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      },
      "lane2_top_cited": {
        "query": "cites:(106598 OR 9422583 OR 9422584)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjEyJnM9MjExNTk0NSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28106598+OR+9422583+OR+9422584%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106598 OR 9422583 OR 9422584)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzYwNDAwMDAwMDAwJnM9MTA3MDY4MDQmdD1vJmQ9MjAyNi0wNy0wNiZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106598+OR+9422583+OR+9422584%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106598 OR 9422583 OR 9422584)",
    "indexed_citing_opinions": 19246,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106598,
        "count": 17003,
        "count_source": "search"
      },
      {
        "opinion_id": 9422583,
        "count": 2633,
        "count_source": "search"
      },
      {
        "opinion_id": 9422584,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 33964,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brady-v-maryland.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yLjQ2NzM5OTEmcz0yNDU4MzMzJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106598+OR+9422583+OR+9422584%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106598,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 102863,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 103282,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 103332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 103798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 104054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 104183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 104272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 104681,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 104695,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 105403,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 105566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 106054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 106521,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 1932282,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 2204133,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 2324852,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 2333601,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 2336815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 3482675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 3486546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 3486645,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 3487541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 3488520,
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
    "date_created": "2026-07-04T20:17:56Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:18:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:18:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:22:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:18:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brady v. Maryland

```
<div>
<center><b><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U.S. 83</a></span> (1963)</b></center>
<center><h1>BRADY<br>
v.<br>
MARYLAND.</h1></center>
<center>No. 490.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 18-19, 1963.</center>
<center>Decided May 13, 1963.</center>
CERTIORARI TO THE COURT OF APPEALS OF MARYLAND.
<p><span class="star-pagination">*84</span> <i>E. Clinton Bamberger, Jr.</i> argued the cause for petitioner. With him on the brief was <i>John Martin Jones, Jr.</i></p>
<p><i>Thomas W. Jamison III,</i> Special Assistant Attorney General of Maryland, argued the cause for respondent. With him on the brief were <i>Thomas B. Finan,</i> Attorney General, and <i>Robert C. Murphy,</i> Deputy Attorney General.</p>
<p>Opinion of the Court by MR. JUSTICE DOUGLAS, announced by MR. JUSTICE BRENNAN.</p>
<p>Petitioner and a companion, Boblit, were found guilty of murder in the first degree and were sentenced to death, their convictions being affirmed by the Court of Appeals of Maryland. <span class="citation" data-id="1505680"><a href="/opinion/1505680/boblit-v-state/" aria-description="Citation for case: Boblit v. State">220 Md. 454</a></span>, <span class="citation" data-id="1505680"><a href="/opinion/1505680/boblit-v-state/" aria-description="Citation for case: Boblit v. State">154 A. 2d 434</a></span>. Their trials were separate, petitioner being tried first. At his trial Brady took the stand and admitted his participation in the crime, but he claimed that Boblit did the actual killing. And, in his summation to the jury, Brady's counsel conceded that Brady was guilty of murder in the first degree, asking only that the jury return that verdict "without capital punishment." Prior to the trial petitioner's counsel had requested the prosecution to allow him to examine Boblit's extrajudicial statements. Several of those statements were shown to him; but one dated July 9, 1958, in which Boblit admitted the actual homicide, was withheld by the prosecution and did not come to petitioner's notice until after he had been tried, convicted, and sentenced, and after his conviction had been affirmed.</p>
<p>Petitioner moved the trial court for a new trial based on the newly discovered evidence that had been suppressed by the prosecution. Petitioner's appeal from a denial of that motion was dismissed by the Court of Appeals without prejudice to relief under the Maryland <span class="star-pagination">*85</span> Post Conviction Procedure Act. <span class="citation" data-id="2324852"><a href="/opinion/2324852/brady-v-state/" aria-description="Citation for case: Brady v. State">222 Md. 442</a></span>, <span class="citation" data-id="2324852"><a href="/opinion/2324852/brady-v-state/" aria-description="Citation for case: Brady v. State">160 A. 2d 912</a></span>. The petition for post-conviction relief was dismissed by the trial court; and on appeal the Court of Appeals held that suppression of the evidence by the prosecution denied petitioner due process of law and remanded the case for a retrial of the question of punishment, not the question of guilt. <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/" aria-description="Citation for case: Brady v. State">226 Md. 422</a></span>, 174 A 2d 167. The case is here on certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./371/812/">371 U. S. 812</a></span>.<sup>[1]</sup></p>
<p>The crime in question was murder committed in the perpetration of a robbery. Punishment for that crime in Maryland is life imprisonment or death, the jury being empowered to restrict the punishment to life by addition of the words "without capital punishment." 3 Md. Ann. Code, 1957, Art. 27, § 413. In Maryland, by reason of the state constitution, the jury in a criminal case are "the Judges of Law, as well as of fact." Art. XV, § 5. The question presented is whether petitioner was denied a federal right when the Court of Appeals restricted the new trial to the question of punishment.</p>
<p><span class="star-pagination">*86</span> We agree with the Court of Appeals that suppression of this confession was a violation of the Due Process Clause of the Fourteenth Amendment. The Court of Appeals relied in the main on two decisions from the Third Circuit Court of Appeals<i>United States ex rel. Almeida</i> v. <i>Baldi,</i> <span class="citation" data-id="229184"><a href="/opinion/229184/united-states-ex-rel-almeida-v-baldi/" aria-description="Citation for case: United States Ex Rel. Almeida v. Baldi">195 F. 2d 815</a></span>, and <i>United States ex rel. Thompson</i> v. <i>Dye,</i> 221 F. 2d 763which, we agree, state the correct constitutional rule.</p>
<p>This ruling is an extension of <i>Mooney</i> v. <i>Holohan,</i> <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103, 112</a></span>, where the Court ruled on what nondisclosure by a prosecutor violates due process:</p>
<blockquote>"It is a requirement that cannot be deemed to be satisfied by mere notice and hearing if a State has contrived a conviction through the pretense of a trial which in truth is but used as a means of depriving a defendant of liberty through a deliberate deception of court and jury by the presentation of testimony known to be perjured. Such a contrivance by a State to procure the conviction and imprisonment of a defendant is as inconsistent with the rudimentary demands of justice as is the obtaining of a like result by intimidation."</blockquote>
<p>In <i>Pyle</i> v. <i>Kansas,</i> <span class="citation" data-id="103727"><a href="/opinion/103727/pyle-v-kansas/#215" aria-description="Citation for case: Pyle v. Kansas">317 U. S. 213, 215-216</a></span>, we phrased the rule in broader terms:</p>
<blockquote>"Petitioner's papers are inexpertly drawn, but they do set forth allegations that his imprisonment resulted from perjured testimony, knowingly used by the State authorities to obtain his conviction, and from the deliberate suppression by those same authorities of evidence favorable to him. These allegations sufficiently charge a deprivation of rights guaranteed by the Federal Constitution, and, if proven, would entitle petitioner to release from his present custody. <i>Mooney</i> v. <i>Holohan,</i> <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103</a></span>."</blockquote>
<p><span class="star-pagination">*87</span> The Third Circuit in the <i><span class="citation" data-id="229184"><a href="/opinion/229184/united-states-ex-rel-almeida-v-baldi/" aria-description="Citation for case: United States Ex Rel. Almeida v. Baldi">Baldi</a></span></i> case construed that statement in <i>Pyle</i> v. <i><span class="citation" data-id="103727"><a href="/opinion/103727/pyle-v-kansas/" aria-description="Citation for case: Pyle v. Kansas">Kansas</a></span></i> to mean that the "suppression of evidence favorable" to the accused was itself sufficient to amount to a denial of due process. <span class="citation" data-id="229184"><a href="/opinion/229184/united-states-ex-rel-almeida-v-baldi/#820" aria-description="Citation for case: United States Ex Rel. Almeida v. Baldi">195 F. 2d, at 820</a></span>. In <i>Napue</i> v. <i>Illinois,</i> <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264, 269</a></span>, we extended the test formulated in <i>Mooney</i> v. <i><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">Holohan</a></span></i> when we said: "The same result obtains when the State, although not soliciting false evidence, allows it to go uncorrected when it appears." And see <i>Alcorta</i> v. <i>Texas,</i> <span class="citation" data-id="105566"><a href="/opinion/105566/alcorta-v-texas/" aria-description="Citation for case: Alcorta v. Texas">355 U. S. 28</a></span>; <i>Wilde</i> v. <i>Wyoming,</i> <span class="citation" data-id="106054"><a href="/opinion/106054/wilde-v-wyoming/" aria-description="Citation for case: Wilde v. Wyoming">362 U. S. 607</a></span>. Cf. <i>Durley</i> v. <i>Mayo,</i> <span class="citation" data-id="9421301"><a href="/opinion/105403/durley-v-mayo/#285" aria-description="Citation for case: Durley v. Mayo">351 U. S. 277, 285</a></span> (dissenting opinion).</p>
<p>We now hold that the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution.</p>
<p>The principle of <i>Mooney</i> v. <i><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">Holohan</a></span></i> is not punishment of society for misdeeds of a prosecutor but avoidance of an unfair trial to the accused. Society wins not only when the guilty are convicted but when criminal trials are fair; our system of the administration of justice suffers when any accused is treated unfairly. An inscription on the walls of the Department of Justice states the proposition candidly for the federal domain: "The United States wins its point whenever justice is done its citizens in the courts."<sup>[2]</sup> A prosecution that withholds evidence on demand of an accused which, if made available, <span class="star-pagination">*88</span> would tend to exculpate him or reduce the penalty helps shape a trial that bears heavily on the defendant. That casts the prosecutor in the role of an architect of a proceeding that does not comport with standards of justice, even though, as in the present case, his action is not "the result of guile," to use the words of the Court of Appeals. <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/#427" aria-description="Citation for case: Brady v. State">226 Md., at 427</a></span>, <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/#169" aria-description="Citation for case: Brady v. State">174 A. 2d, at 169</a></span>.</p>
<p>The question remains whether petitioner was denied a constitutional right when the Court of Appeals restricted his new trial to the question of punishment. In justification of that ruling the Court of Appeals stated:</p>
<blockquote>"There is considerable doubt as to how much good Boblit's undisclosed confession would have done Brady if it had been before the jury. It clearly implicated Brady as being the one who wanted to strangle the victim, Brooks. Boblit, according to this statement, also favored killing him, but he wanted to do it by shooting. We cannot put ourselves in the place of the jury and assume what their views would have been as to whether it did or did not matter whether it was Brady's hands or Boblit's hands that twisted the shirt about the victim's neck. . . . [I]t would be `too dogmatic' for us to say that the jury would not have attached any significance to this evidence <i>in considering the punishment of the defendant Brady.</i>
</blockquote>
<blockquote>"Not without some doubt, we conclude that the withholding of this particular confession of Boblit's was prejudicial to the defendant Brady. . . .</blockquote>
<blockquote>"The appellant's sole claim of prejudice goes to the punishment imposed. <i>If Boblit's withheld confession had been before the jury, nothing in it could have reduced the appellant Brady's offense below murder in the first degree.</i> We, therefore, see no occasion to retry that issue." <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/#429" aria-description="Citation for case: Brady v. State">226 Md., at 429-430</a></span>, <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/#171" aria-description="Citation for case: Brady v. State">174 A. 2d, at 171</a></span>. (Italics added.)</blockquote>
<p><span class="star-pagination">*89</span> If this were a jurisdiction where the jury was not the judge of the law, a different question would be presented. But since it is, how can the Maryland Court of Appeals state that nothing in the suppressed confession could have reduced petitioner's offense "below murder in the first degree"? If, as a matter of Maryland law, juries in criminal cases could determine the admissibility of such evidence on the issue of innocence or guilt, the question would seem to be foreclosed.</p>
<p>But Maryland's constitutional provision making the jury in criminal cases "the Judges of Law" does not mean precisely what it seems to say.<sup>[3]</sup> The present status of that provision was reviewed recently in <i>Giles</i> v. <i>State,</i> <span class="citation" data-id="2336815"><a href="/opinion/2336815/giles-v-state/" aria-description="Citation for case: Giles v. State">229 Md. 370</a></span>, <span class="citation" data-id="2336815"><a href="/opinion/2336815/giles-v-state/" aria-description="Citation for case: Giles v. State">183 A. 2d 359</a></span>, appeal dismissed, <span class="citation multiple-matches"><a href="/c/U.%20S./372/767/">372 U. S. 767</a></span>, where the several exceptions, added by statute or carved out by judicial construction, are reviewed. One of those exceptions, material here, is that "Trial courts have always passed and still pass upon the admissibility of evidence the jury may consider on the issue of the innocence or guilt of the accused." <span class="citation" data-id="2336815"><a href="/opinion/2336815/giles-v-state/#383" aria-description="Citation for case: Giles v. State">229 Md., at 383</a></span>, <span class="citation" data-id="2336815"><a href="/opinion/2336815/giles-v-state/#365" aria-description="Citation for case: Giles v. State">183 A. 2d, at 365</a></span>. The cases cited make up a long line going back nearly a century. <i>Wheeler</i> v. <i>State,</i> <span class="citation" data-id="7894155"><a href="/opinion/7943451/wheeler-v-state/#570" aria-description="Citation for case: Wheeler v. State">42 Md. 563, 570</a></span>, stated that instructions to the jury were advisory only, "except in regard to questions as to what shall be considered as evidence." And the court "having such right, it follows of course, that it also has the right to prevent counsel from arguing against such an instruction." <i>Bell</i> v. <i>State,</i> <span class="citation" data-id="7895894"><a href="/opinion/7945112/bell-v-state/#120" aria-description="Citation for case: Bell v. State">57 Md. 108, 120</a></span>. And see <i>Beard</i> v. <i>State,</i> <span class="citation" data-id="7897944"><a href="/opinion/7947021/beard-v-state/#280" aria-description="Citation for case: Beard v. State">71 Md. 275, 280</a></span>, <span class="citation" data-id="7897944"><a href="/opinion/7947021/beard-v-state/#1045" aria-description="Citation for case: Beard v. State">17 A. 1044, 1045</a></span>; <i>Dick</i> v. <i>State,</i> <span class="citation" data-id="3488520"><a href="/opinion/3490537/dick-v-state/#21" aria-description="Citation for case: Dick v. State">107 Md. 11, 21</a></span>, <span class="citation" data-id="3488520"><a href="/opinion/3490537/dick-v-state/#290" aria-description="Citation for case: Dick v. State">68 A. 286, 290</a></span>. Cf. <i>Vogel</i> v. <i>State,</i> <span class="citation" data-id="3486645"><a href="/opinion/3488709/vogel-v-state/" aria-description="Citation for case: Vogel v. State">163 Md. 267</a></span>, <span class="citation" data-id="3486645"><a href="/opinion/3488709/vogel-v-state/" aria-description="Citation for case: Vogel v. State">162 A. 705</a></span>.</p>
<p><span class="star-pagination">*90</span> We usually walk on treacherous ground when we explore state law,<sup>[4]</sup> for state courts, state agencies, and state legislatures are its final expositors under our federal regime. But, as we read the Maryland decisions, it is the court, not the jury, that passes on the "admissibility of evidence" pertinent to "the issue of the innocence or guilt of the accused." <i>Giles</i> v. <i>State, supra</i><i>.</i> In the present case a unanimous Court of Appeals has said that nothing in the suppressed confession "could have reduced the appellant Brady's offense below murder in the first degree." We read that statement as a ruling on the admissibility of the confession on the issue of innocence or guilt. A sporting theory of justice might assume that if the suppressed confession had been used at the first trial, the judge's ruling that it was not admissible on the issue of innocence or guilt might have been flouted by the jury just as might have been done if the court had first admitted a confession and then stricken it from the record.<sup>[5]</sup> But we cannot raise that trial strategy to the dignity of a constitutional right and say that the deprival of this defendant of that sporting chance through the use of a <span class="star-pagination">*91</span> bifurcated trial (cf. <i>Williams</i> v. <i>New York,</i> <span class="citation" data-id="9420330"><a href="/opinion/104681/williams-v-new-york/" aria-description="Citation for case: Williams v. New York">337 U. S. 241</a></span>) denies him due process or violates the Equal Protection Clause of the Fourteenth Amendment.</p>
<p><i>Affirmed.</i></p>
<p>Separate opinion of MR. JUSTICE WHITE.</p>
<p>1. The Maryland Court of Appeals declared, "The suppression or withholding by the State of material evidence exculpatory to an accused is a violation of due process" without citing the United States Constitution or the Maryland Constitution which also has a due process clause.<sup>[*]</sup> We therefore cannot be sure which Constitution was invoked by the court below and thus whether the State, the only party aggrieved by this portion of the judgment, could even bring the issue here if it desired to do so. See <i>New York City</i> v. <i>Central Savings Bank,</i> <span class="citation" data-id="8154343"><a href="/opinion/8192409/new-york-city-v-central-savings-bank/" aria-description="Citation for case: New York City v. Central Savings Bank">306 U. S. 661</a></span>; <i>Minnesota</i> v. <i>National Tea Co.,</i> <span class="citation" data-id="9419097"><a href="/opinion/103332/minnesota-v-national-tea-co/" aria-description="Citation for case: Minnesota v. National Tea Co.">309 U. S. 551</a></span>. But in any event, there is no cross-petition by the State, nor has it challenged the correctness of the ruling below that a new trial on punishment was called for by the requirements of due process. In my view, therefore, the Court should not reach the due process question which it decides. It certainly is not the case, as it may be suggested, that without it we would have only a state law question, for assuming the court below was correct in finding a violation of petitioner's rights in the suppression of evidence, the federal question he wants decided here still remains, namely, whether denying him a new trial on guilt as well as punishment deprives him of equal protection. There is thus a federal question to deal with in this Court, cf. <i>Bell</i> v. <i>Hood,</i> <span class="citation" data-id="9419809"><a href="/opinion/104272/bell-v-hood/" aria-description="Citation for case: Bell v. Hood">327 U. S. 678</a></span>, <span class="star-pagination">*92</span> wholly aside from the due process question involving the suppression of evidence. The majority opinion makes this unmistakably clear. Before dealing with the due process issue it says, "The question presented is whether petitioner was denied a federal right when the Court of Appeals restricted the new trial to the question of punishment." After discussing at some length and disposing of the suppression matter in federal constitutional terms it says the question still to be decided is the same as it was before: "The question remains whether petitioner was denied a constitutional right when the Court of Appeals restricted his new trial to the question of punishment."</p>
<p>The result, of course, is that the due process discussion by the Court is wholly advisory.</p>
<p>2. In any event the Court's due process advice goes substantially beyond the holding below. I would employ more confining language and would not cast in constitutional form a broad rule of criminal discovery. Instead, I would leave this task, at least for now, to the rulemaking or legislative process after full consideration by legislators, bench, and bar.</p>
<p>3. I concur in the Court's disposition of petitioner's equal protection argument.</p>
<p>MR. JUSTICE HARLAN, whom MR. JUSTICE BLACK joins, dissenting.</p>
<p>I think this case presents only a single federal question: did the order of the Maryland Court of Appeals granting a new trial, limited to the issue of punishment, violate petitioner's Fourteenth Amendment right to equal protection?<sup>[1]</sup> In my opinion an affirmative answer would <span class="star-pagination">*93</span> be required <i>if</i> the Boblit statement would have been admissible on the issue of guilt at petitioner's original trial. This indeed seems to be the clear implication of this Court's opinion.</p>
<p>The Court, however, holds that the Fourteenth Amendment was not infringed because it considers the Court of Appeals' opinion, and the other Maryland cases dealing with Maryland's constitutional provision making juries in criminal cases "the Judges of Law, as well as of fact," as establishing that the Boblit statement would not have been admissible at the original trial on the issue of petitioner's guilt.</p>
<p>But I cannot read the Court of Appeals' opinion with any such assurance. That opinion can as easily, and perhaps more easily, be read as indicating that the new trial limitation followed from the Court of Appeals' concept of its power, under § 645G of the Maryland Post Conviction Procedure Act, Md. Code, Art. 27 (1960 Cum. Supp.) and Rule 870 of the Maryland Rules of Procedure, to fashion appropriate relief meeting the peculiar circumstances of this case,<sup>[2]</sup> rather than from the view that the Boblit statement would have been relevant at the original trial only on the issue of punishment. <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/#430" aria-description="Citation for case: Brady v. State">226 Md., at 430</a></span>, <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/#171" aria-description="Citation for case: Brady v. State">174 A. 2d, at 171</a></span>. This interpretation is indeed fortified by the Court of Appeals' earlier general discussion as to the admissibility of third-party confessions, which falls short of saying anything that is dispositive <span class="star-pagination">*94</span> of the crucial issue here. <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/#427" aria-description="Citation for case: Brady v. State">226 Md., at 427-429</a></span>, <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/#170" aria-description="Citation for case: Brady v. State">174 A. 2d, at 170</a></span>.<sup>[3]</sup></p>
<p>Nor do I find anything in any of the other Maryland cases cited by the Court (<i>ante,</i> p. 89) which bears on the admissibility <i>vel non</i> of the Boblit statement on the issue of guilt. None of these cases suggests anything more relevant here than that a jury may not "overrule" the trial court on questions relating to the admissibility of evidence. Indeed they are by no means clear as to what happens if the jury in fact undertakes to do so. In this very case, for example, the trial court charged that "in the final analysis the jury are the judges of both the <i>law</i> and the facts, and the verdict in this case is <i>entirely</i> the jury's responsibility." (Emphasis added.)</p>
<p>Moreover, uncertainty on this score is compounded by the State's acknowledgment at the oral argument here that the withheld Boblit statement <i>would</i> have been admissible at the trial on the issue of guilt.<sup>[4]</sup></p>
<p>In this state of uncertainty as to the proper answer to the critical underlying issue of state law, and in view of the fact that the Court of Appeals did not in terms <span class="star-pagination">*95</span> address itself to the equal protection question, I do not see how we can properly resolve this case at this juncture. I think the appropriate course is to vacate the judgment of the State Court of Appeals and remand the case to that court for further consideration in light of the governing constitutional principle stated at the outset of this opinion. Cf. <i>Minnesota</i> v. <i>National Tea Co.,</i> <span class="citation" data-id="9419097"><a href="/opinion/103332/minnesota-v-national-tea-co/" aria-description="Citation for case: Minnesota v. National Tea Co.">309 U. S. 551</a></span>.</p>
<h2>NOTES</h2>
<p>[1]  Neither party suggests that the decision below is not a "final judgment" within the meaning of <span class="citation no-link">28 U. S. C. § 1257</span> (3), and no attack on the reviewability of the lower court's judgment could be successfully maintained. For the general rule that "Final judgment in a criminal case means sentence. The sentence is the judgment" (<i>Berman</i> v. <i>United States,</i> <span class="citation" data-id="102863"><a href="/opinion/102863/berman-v-united-states/#212" aria-description="Citation for case: Berman v. United States">302 U. S. 211, 212</a></span>) cannot be applied here. If in fact the Fourteenth Amendment entitles petitioner to a new trial on the issue of guilt as well as punishment the ruling below has seriously prejudiced him. It is the right to a trial on the issue of guilt "that presents a serious and unsettled question" (<i>Cohen</i> v. <i>Beneficial Loan Corp.,</i> <span class="citation" data-id="9420349"><a href="/opinion/104695/cohen-v-beneficial-industrial-loan-corp/#547" aria-description="Citation for case: Cohen v. Beneficial Industrial Loan Corp.">337 U. S. 541, 547</a></span>) that "is fundamental to the further conduct of the case" (<i>United States</i> v. <i>General Motors Corp.,</i> <span class="citation" data-id="9419563"><a href="/opinion/104054/united-states-v-general-motors-corp/#377" aria-description="Citation for case: United States v. General Motors Corp.">323 U. S. 373, 377</a></span>). This question is "independent of, and unaffected by" (<i>Radio Station WOW</i> v. <i>Johnson,</i> <span class="citation" data-id="9419695"><a href="/opinion/104183/radio-station-wow-inc-v-johnson/#126" aria-description="Citation for case: Radio Station Wow, Inc. v. Johnson">326 U. S. 120, 126</a></span>) what may transpire in a trial at which petitioner can receive only a life imprisonment or death sentence. It cannot be mooted by such a proceeding. See <i>Largent</i> v. <i>Texas,</i> <span class="citation" data-id="103798"><a href="/opinion/103798/largent-v-texas/#421" aria-description="Citation for case: Largent v. Texas">318 U. S. 418, 421-422</a></span>. Cf. <i>Local No. 438</i> v. <i>Curry,</i> <span class="citation" data-id="9422517"><a href="/opinion/106521/local-no-438-construction-general-laborers-union-v-curry/#549" aria-description="Citation for case: Local No. 438 Construction &amp; General Laborers&#x27; Union v....">371 U. S. 542, 549</a></span>.</p>
<p>[2]  Judge Simon E. Sobeloff when Solicitor General put the idea as follows in an address before the Judicial Conference of the Fourth Circuit on June 29, 1954:
</p>
<p>"The Solicitor General is not a neutral, he is an advocate; but an advocate for a client whose business is not merely to prevail in the instant case. My client's chief business is not to achieve victory but to establish justice. We are constantly reminded of the now classic words penned by one of my illustrious predecessors, Frederick William Lehmann, that the Government wins its point when justice is done in its courts."</p>
<p>[3]  See Dennis, Maryland's Antique Constitutional Thorn, 92 U. of Pa. L. Rev. 34, 39, 43; Prescott, Juries as Judges of the Law: Should the Practice be Continued, 60 Md. St. Bar Assn. Rept. 246, 253-254.</p>
<p>[4]  For one unhappy incident of recent vintage see <i>Oklahoma Packing Co.</i> v. <i>Oklahoma Gas &amp; Electric Co.,</i> <span class="citation" data-id="9419072"><a href="/opinion/103282/oklahoma-packing-co-v-oklahoma-gas-electric-co/" aria-description="Citation for case: Oklahoma Packing Co. v. Oklahoma Gas &amp; Electric Co.">309 U. S. 4</a></span>, that replaced an earlier opinion in the same case, <span class="citation no-link">309 U. S. 703</span>.</p>
<p>[5]  "In the matter of confessions a hybrid situation exists. It is the duty of the Court to determine from the proof, usually taken out of the presence of the jury, if they were freely and voluntarily made, etc., and admissible. If admitted, the jury is entitled to hear and consider proof of the circumstances surrounding their obtention, the better to determine their weight and sufficiency. The fact that the Court admits them clothes them with no presumption for the jury's purposes that they are either true or were freely and voluntarily made. However, after a confession has been admitted and read to the jury the judge may change his mind and strike it out of the record. Does he strike it out of the jury's mind?" Dennis, Maryland's Antique Constitutional Thorn, 92 U. of Pa. L. Rev. 34, 39. See also <i>Bell</i> v. <i>State, supra,</i> at 120; <i>Vogel</i> v. <i>State,</i> <span class="citation" data-id="3486645"><a href="/opinion/3488709/vogel-v-state/#272" aria-description="Citation for case: Vogel v. State">163 Md., at 272</a></span>, <span class="citation" data-id="3486645"><a href="/opinion/3488709/vogel-v-state/#706" aria-description="Citation for case: Vogel v. State">162 A., at 706-707</a></span>.</p>
<p>[*]  Md. Const., Art. 23; <i>Home Utilities Co., Inc.,</i> v. <i>Revere Copper &amp; Brass, Inc.,</i> <span class="citation" data-id="2333601"><a href="/opinion/2333601/home-utilities-co-v-revere-copper-brass-inc/" aria-description="Citation for case: Home Utilities Co. v. Revere Copper &amp; Brass, Inc.">209 Md. 610</a></span>, <span class="citation" data-id="2333601"><a href="/opinion/2333601/home-utilities-co-v-revere-copper-brass-inc/" aria-description="Citation for case: Home Utilities Co. v. Revere Copper &amp; Brass, Inc.">122 A. 2d 109</a></span>; <i>Raymond</i> v. <i>State,</i> <span class="citation" data-id="3486546"><a href="/opinion/3488611/raymond-v-state-ex-rel-szydlouski/" aria-description="Citation for case: Raymond v. State Ex Rel. Szydlouski">192 Md. 602</a></span>, <span class="citation" data-id="3486546"><a href="/opinion/3488611/raymond-v-state-ex-rel-szydlouski/" aria-description="Citation for case: Raymond v. State Ex Rel. Szydlouski">65 A. 2d 285</a></span>; <i>County Comm'rs of Anne Arundel County</i> v. <i>English,</i> <span class="citation" data-id="3487541"><a href="/opinion/3489580/county-commissioners-v-english/" aria-description="Citation for case: County Commissioners v. English">182 Md. 514</a></span>, <span class="citation" data-id="3487541"><a href="/opinion/3489580/county-commissioners-v-english/" aria-description="Citation for case: County Commissioners v. English">35 A. 2d 135</a></span>; <i>Oursler</i> v. <i>Tawes,</i> <span class="citation" data-id="3482675"><a href="/opinion/3484836/oursler-v-tawes/" aria-description="Citation for case: Oursler v. Tawes">178 Md. 471</a></span>, <span class="citation" data-id="3482675"><a href="/opinion/3484836/oursler-v-tawes/" aria-description="Citation for case: Oursler v. Tawes">13 A. 2d 763</a></span>.</p>
<p>[1]  I agree with my Brother WHITE that there is no necessity for deciding in this case the broad due process questions with which the Court deals at pp. 86-88 of its opinion.</p>
<p>[2]  Section 645G provides in part: "If the court finds in favor of the petitioner, it shall enter an appropriate order with respect to the judgment or sentence in the former proceedings, and any supplementary orders as to rearraignment, retrial, custody, bail, discharge, correction of sentence, or other matters that may be necessary and proper." Rule 870 provides that the Court of Appeals "will either affirm or reverse the judgment from which the appeal was taken, or direct the manner in which it shall be modified, changed or amended."</p>
<p>[3]  It is noteworthy that the Court of Appeals did not indicate that it was limiting in any way the authority of <i>Day</i> v. <i>State,</i> <span class="citation" data-id="1932282"><a href="/opinion/1932282/day-v-state/" aria-description="Citation for case: Day v. State">196 Md. 384</a></span>, <span class="citation" data-id="1932282"><a href="/opinion/1932282/day-v-state/" aria-description="Citation for case: Day v. State">76 A. 2d 729</a></span>. In that case two defendants were jointly tried and convicted of felony murder. Each admitted participating in the felony but accused the other of the homicide. On appeal the defendants attacked the trial court's denial of a severance, and the State argued that neither defendant was harmed by the statements put in evidence at the joint trial because admission of the felony amounted to admission of guilt of felony murder. Nevertheless the Court of Appeals found an abuse of discretion and ordered separate new trials on all issues.</p>
<p>[4]  In response to a question from the Bench as to whether Boblit's statement, had it been offered at petitioner's original trial, would have been admissible for all purposes, counsel for the State, after some colloquy, stated: "It would have been, yes."</p>

</div>
```

---

## GROUP: content/cases/Brendlin v. California.md  (`case`, 5 assertions)

### content_page

```
---
title: "Brendlin v. California"
type: case
citation: "551 U.S. 249 (2007)"
parallel_cite: "127 S. Ct. 2400; 168 L. Ed. 2d 132"
neutral_cite: 2007 U.S. LEXIS 7897
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2007
date_decided: 2007-06-18
docket: 06-8120
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2007-06-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brendlin v. California
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145712/brendlin-v-california/"
  cluster_id: 145712
  opinion_id: 145712
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Key — Progeny / Refinement"
related: ["[[Rakas v. Illinois]]", "[[Delaware v. Prouse]]", "[[California v. Hodari D.]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "traffic-stop", "seizure", "passenger"]
holding: "When a vehicle is stopped, a passenger is seized just as the driver is, and so may challenge the constitutionality of the stop."
lake:
  record_id: Brendlin v. California
  status: verified
  projected_at: 2026-07-09
---

# Brendlin v. California

*551 U.S. 249 (2007)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A deputy stopped a car to verify a temporary operating permit, admitting there was nothing unusual about the permit and no reason to believe a violation. Bruce Brendlin was the front-seat passenger. The deputy recognized him, confirmed a parole-violation warrant, arrested him, and a search turned up methamphetamine-manufacturing materials. Brendlin moved to suppress, arguing the stop unlawfully seized him.

## Issue
Whether a passenger in a vehicle is "seized" by a traffic stop, so that he has [[Standing to Challenge a Search|standing to challenge]] the constitutionality of the stop.

## Rule
"When a police officer makes a traffic stop, the driver of the car is seized within the meaning of the Fourth Amendment." — 551 U.S. at 251. ^pin-251

"We hold that a passenger is seized as well and so may challenge the constitutionality of the stop." — [*Id.*](https://www.courtlistener.com/opinion/145712/brendlin-v-california/#:~:text=We%20hold%20that%20a%20passenger) ^pin-251b

## Application
When the deputy pulled the car over, a reasonable person in Brendlin's position as a passenger would not have believed he was free to leave; he was therefore seized at the moment the car stopped. Because the State conceded the stop itself lacked justification, Brendlin could challenge it and seek suppression of what the seizure produced.

## Conclusion
A passenger is seized by a traffic stop and may challenge it; the judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Brendlin* applies the seizure framework of [[California v. Hodari D.]] and [[Rakas v. Illinois]] to confirm passenger standing in vehicle stops.

## Appears on
- [[Standing to Challenge a Search]] — *Key — Progeny / Refinement*

## Sources
- *Brendlin v. California*, 551 U.S. 249 (2007) — https://www.courtlistener.com/opinion/145712/brendlin-v-california/ — pinpoint: 251.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "97681f6424bd3a7d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "551 U.S. 249 (2007)", "court": "U.S. Supreme Court", "neutral_cite": "2007 U.S. LEXIS 7897", "official_citation_present": true, "parallel_cite": "127 S. Ct. 2400; 168 L. Ed. 2d 132", "title": "Brendlin v. California", "year": "2007"}}
{"assertion_id": "ba770e288f6c4127", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "When a vehicle is stopped, a passenger is seized just as the driver is, and so may challenge the constitutionality of the stop.", "title": "Brendlin v. California"}}
{"assertion_id": "c403dff53cec012a", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Key — Progeny / Refinement", "title": "Brendlin v. California"}}
{"assertion_id": "d984f74d61a00a3d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2007-06-18", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Brendlin v. California", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Brendlin v. California", "varies_by_point": "false"}}
{"assertion_id": "dbbc8f37fffbc7bb", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Brendlin v. California"}}
```

### lake record — Brendlin v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brendlin v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Brendlin v. California",
    "case_name_short": "Brendlin",
    "case_name_full": "Brendlin v. California",
    "input_case_name": "Brendlin v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2007-06-18",
    "year": 2007,
    "docket": "06-8120",
    "cluster_id": 145712,
    "lead_opinion_id": 145712,
    "sibling_ids": [
      145712
    ],
    "absolute_url": "/opinion/145712/brendlin-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "551 U.S. 249",
      "volume": "551",
      "reporter": "U.S.",
      "page": "249",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "127 S. Ct. 2400",
        "volume": "127",
        "reporter": "S. Ct.",
        "page": "2400",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "168 L. Ed. 2d 132",
        "volume": "168",
        "reporter": "L. Ed. 2d",
        "page": "132",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2007 U.S. LEXIS 7897",
        "volume": "2007",
        "reporter": "U.S. LEXIS",
        "page": "7897",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "551 U.S. 249",
        "volume": "551",
        "reporter": "U.S.",
        "page": "249",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "127 S. Ct. 2400",
        "volume": "127",
        "reporter": "S. Ct.",
        "page": "2400",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "168 L. Ed. 2d 132",
        "volume": "168",
        "reporter": "L. Ed. 2d",
        "page": "132",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2007 U.S. LEXIS 7897",
        "volume": "2007",
        "reporter": "U.S. LEXIS",
        "page": "7897",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "551 U.S. 249",
    "official_selection": {
      "court_class": "scotus",
      "selected": "551 U.S. 249",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-251",
      "page": null,
      "quote": "by a traffic stop, so that he has standing to challenge the constitutionality of the stop. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-251b",
      "page": null,
      "quote": "We hold that a passenger is seized as well and so may challenge the constitutionality of the stop.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 7394,
      "fragment": "#:~:text=We%20hold%20that%20a%20passenger",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2007-06-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brendlin v. California",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Brendlin v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Zachariah J. Marshall v. State of Indiana",
          "cluster_id": 4594526,
          "cite": [
            "117 N.E.3d 1254"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Buckley",
          "cluster_id": 4468007,
          "cite": [
            "90 N.E.3d 767",
            "478 Mass. 861"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Arizona v. Johnson",
          "cluster_id": 145912,
          "cite": [
            "172 L. Ed. 2d 694",
            "129 S. Ct. 781",
            "555 U.S. 323",
            "2009 U.S. LEXIS 868"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Zamudio",
          "cluster_id": 2634388,
          "cite": [
            "181 P.3d 105",
            "75 Cal. Rptr. 3d 289",
            "43 Cal. 4th 327",
            "2008 Cal. LEXIS 4431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
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
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heien v. North Carolina",
          "cluster_id": 2760668,
          "cite": [
            "190 L. Ed. 2d 475",
            "135 S. Ct. 530",
            "2014 U.S. LEXIS 8306",
            "83 U.S.L.W. 4021",
            "25 Fla. L. Weekly Fed. S 20"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
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
        "journal_ref": "Brendlin v. California:lane2_top_cited"
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
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. Madrid",
          "cluster_id": 4867542,
          "cite": [
            "592 U.S. 306",
            "141 S. Ct. 989",
            "209 L. Ed. 2d 190"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark Atkinson v. City of Mountain View",
          "cluster_id": 819982,
          "cite": [
            "709 F.3d 1201",
            "2013 WL 462381",
            "2013 U.S. App. LEXIS 2703"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Woodard",
          "cluster_id": 2540788,
          "cite": [
            "341 S.W.3d 404",
            "2011 Tex. Crim. App. LEXIS 447",
            "2011 WL 1261320"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
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
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Henderson",
          "cluster_id": 1057155,
          "cite": [
            "2013 IL 114040"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Harmon",
          "cluster_id": 4670342,
          "cite": [
            "2019 COA 156"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maurice Lewis v. City of Chicago",
          "cluster_id": 4583974,
          "cite": [
            "914 F.3d 472"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wade, Christopher James",
          "cluster_id": 2947716,
          "cite": [
            "422 S.W.3d 661",
            "2013 WL 4820299",
            "2013 Tex. Crim. App. LEXIS 1314"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
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
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brooks v. Gaenzle",
          "cluster_id": 152652,
          "cite": [
            "614 F.3d 1213",
            "2010 U.S. App. LEXIS 16488",
            "2010 WL 3122800"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
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
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shaun J. Matz v. Rodney Klotka",
          "cluster_id": 2739950,
          "cite": [
            "769 F.3d 517",
            "2014 U.S. App. LEXIS 19074",
            "2014 WL 4960311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Castleberry",
          "cluster_id": 2282066,
          "cite": [
            "332 S.W.3d 460",
            "2011 Tex. Crim. App. LEXIS 283",
            "2011 WL 709697"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morris v. Noe",
          "cluster_id": 623700,
          "cite": [
            "672 F.3d 1185",
            "2012 WL 604170",
            "2012 U.S. App. LEXIS 3927"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Waters v. B. Madson",
          "cluster_id": 4609057,
          "cite": [
            "921 F.3d 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cosby",
          "cluster_id": 2105166,
          "cite": [
            "898 N.E.2d 603",
            "231 Ill. 2d 262",
            "325 Ill. Dec. 556",
            "2008 Ill. LEXIS 890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thompson",
          "cluster_id": 2623710,
          "cite": [
            "166 P.3d 1015",
            "284 Kan. 763",
            "2007 Kan. LEXIS 487"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Johnson",
          "cluster_id": 2012814,
          "cite": [
            "927 N.E.2d 1179",
            "237 Ill. 2d 81",
            "340 Ill. Dec. 168",
            "2010 Ill. LEXIS 657"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Campbell",
          "cluster_id": 1353842,
          "cite": [
            "549 F.3d 364",
            "2008 U.S. App. LEXIS 24313",
            "2008 WL 5060374"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145712) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTAwOTQwODAwMDAwJnM9NDQxMTk3NiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145712%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(145712)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDImcz0yNDc5NTE5JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28145712%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145712)",
        "reviewed": 69,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 69,
        "triage_read": 0,
        "triage_snippet_classified": 69
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145712)",
    "indexed_citing_opinions": 780,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145712,
        "count": 780,
        "count_source": "search"
      }
    ],
    "citation_count": 1525,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brendlin-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxMzUyMzYmcz0xMDMwMzI4MiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145712%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145712,
        "cited_id": 32811,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 109953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 110351,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 112218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 112579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 118086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 121153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 195379,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 558629,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 584528,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 708240,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 769930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 781879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 793575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 794964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 1254533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 1314003,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 1344951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2150438,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2177108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2226476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2388757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2460636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2575734,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2581401,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2620702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2639027,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LCU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-04T20:22:58Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:23:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:23:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:26:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:23:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brendlin v. California

```
(Slip Opinion)              OCTOBER TERM, 2006                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                     BRENDLIN v. CALIFORNIA

      CERTIORARI TO THE SUPREME COURT OF CALIFORNIA

      No. 06–8120. Argued April 23, 2007—Decided June 18, 2007
After officers stopped a car to check its registration without reason to
  believe it was being operated unlawfully, one of them recognized peti
  tioner Brendlin, a passenger in the car. Upon verifying that Brendlin
  was a parole violator, the officers formally arrested him and searched
  him, the driver, and the car, finding, among other things, metham
  phetamine paraphernalia. Charged with possession and manufac
  ture of that substance, Brendlin moved to suppress the evidence ob
  tained in searching his person and the car, arguing that the officers
  lacked probable cause or reasonable suspicion to make the traffic
  stop, which was an unconstitutional seizure of his person. The trial
  court denied the motion, but the California Court of Appeal reversed,
  holding that Brendlin was seized by the traffic stop, which was
  unlawful. Reversing, the State Supreme Court held that suppression
  was unwarranted because a passenger is not seized as a constitu
  tional matter absent additional circumstances that would indicate to
  a reasonable person that he was the subject of the officer’s investiga
  tion or show of authority.
Held: When police make a traffic stop, a passenger in the car, like the
 driver, is seized for Fourth Amendment purposes and so may chal
 lenge the stop’s constitutionality. Pp. 4–13.
    (a) A person is seized and thus entitled to challenge the govern
 ment’s action when officers, by physical force or a show of authority,
 terminate or restrain the person’s freedom of movement through
 means intentionally applied. Florida v. Bostick, 501 U. S. 429, 434;
 Brower v. County of Inyo, 489 U. S. 593, 597. There is no seizure
 without that person’s actual submission. See, e.g., California v. Ho
 dari D., 499 U. S. 621, 626, n. 2. When police actions do not show an
 unambiguous intent to restrain or when an individual’s submission
 takes the form of passive acquiescence, the test for telling when a
2                      BRENDLIN v. CALIFORNIA

                                  Syllabus

    seizure occurs is whether, in light of all the surrounding circum
    stances, a reasonable person would have believed he was not free to
    leave. E.g., United States v. Mendenhall, 446 U. S. 544, 554 (princi
    pal opinion). But when a person “has no desire to leave” for reasons
    unrelated to the police presence, the “coercive effect of the encounter”
    can be measured better by asking whether “a reasonable person
    would feel free to decline the officers’ requests or otherwise terminate
    the encounter.” Bostick, supra, at 435–436. Pp. 4–6.
       (b) Brendlin was seized because no reasonable person in his posi
    tion when the car was stopped would have believed himself free to
    “terminate the encounter” between the police and himself. Bostick,
    supra, at 436. Any reasonable passenger would have understood the
    officers to be exercising control to the point that no one in the car was
    free to depart without police permission. A traffic stop necessarily
    curtails a passenger’s travel just as much as it halts the driver, di
    verting both from the stream of traffic to the side of the road, and the
    police activity that normally amounts to intrusion on “privacy and
    personal security” does not normally (and did not here) distinguish
    between passenger and driver. United States v. Martinez-Fuerte, 428
    U. S. 543, 554. An officer who orders a particular car to pull over acts
    with an implicit claim of right based on fault of some sort, and a sen
    sible person would not expect the officer to allow people to come and
    go freely from the physical focal point of an investigation into faulty
    behavior or wrongdoing. If the likely wrongdoing is not the driving,
    the passenger will reasonably feel subject to suspicion owing to close
    association; but even when the wrongdoing is only bad driving, the
    passenger will expect to be subject to some scrutiny, and his attempt
    to leave would be so obviously likely to prompt an objection from the
    officer that no passenger would feel free to leave in the first place. It
    is also reasonable for passengers to expect that an officer at the scene
    of a crime, arrest, or investigation will not let people move around in
    ways that could jeopardize his safety. See, e.g., Maryland v. Wilson,
    519 U. S. 408, 414–415. The Court’s conclusion comports with the
    views of all nine Federal Courts of Appeals, and nearly every state
    court, to have ruled on the question. Pp. 6–9.
       (c) The State Supreme Court’s contrary conclusion reflects three
    premises with which this Court respectfully disagrees. First, the
    view that the police only intended to investigate the car’s driver and
    did not direct a show of authority toward Brendlin impermissibly
    shifts the issue from the intent of the police as objectively manifested
    to the motive of the police for taking the intentional action to stop the
    car. Applying the objective Mendenhall test resolves any ambiguity
    by showing that a reasonable passenger would understand that he
    was subject to the police display of authority. Second, the state
                    Cite as: 551 U. S. ____ (2007)                   3

                               Syllabus

  court’s assumption that Brendlin, as the passenger, had no ability to
  submit to the police show of authority because only the driver was in
  control of the moving car is unavailing. Brendlin had no effective
  way to signal submission while the car was moving, but once it came
  to a stop he could, and apparently did, submit by staying inside.
  Third, there is no basis for the state court’s fear that adopting the
  rule this Court applies would encompass even those motorists whose
  movement has been impeded due to the traffic stop of another car.
  An occupant of a car who knows he is stuck in traffic because another
  car has been pulled over by police would not perceive the show of au
  thority as directed at him or his car. Pp. 9–13.
    (d) The state courts are left to consider in the first instance
  whether suppression turns on any other issue. P. 13.
38 Cal. 4th 1107, 136 P. 3d 845, vacated and remanded.

  SOUTER, J., delivered the opinion for a unanimous Court.
                        Cite as: 551 U. S. ____ (2007)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 06–8120
                                   _________________


    BRUCE EDWARD BRENDLIN, PETITIONER v.

               CALIFORNIA 

    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                      CALIFORNIA

                                 [June 18, 2007] 


   JUSTICE SOUTER delivered the opinion of the Court.
   When a police officer makes a traffic stop, the driver of
the car is seized within the meaning of the Fourth
Amendment. The question in this case is whether the
same is true of a passenger. We hold that a passenger is
seized as well and so may challenge the constitutionality
of the stop.
                              I
  Early in the morning of November 27, 2001, Deputy
Sheriff Robert Brokenbrough and his partner saw a
parked Buick with expired registration tags. In his ensu
ing conversation with the police dispatcher, Brokenbrough
learned that an application for renewal of registration was
being processed. The officers saw the car again on the
road, and this time Brokenbrough noticed its display of a
temporary operating permit with the number “11,” indicat
ing it was legal to drive the car through November. App.
115. The officers decided to pull the Buick over to verify
that the permit matched the vehicle, even though, as
Brokenbrough admitted later, there was nothing unusual
about the permit or the way it was affixed. Brokenbrough
2                    BRENDLIN v. CALIFORNIA

                          Opinion of the Court

asked the driver, Karen Simeroth, for her license and saw
a passenger in the front seat, petitioner Bruce Brendlin,
whom he recognized as “one of the Brendlin brothers.” Id.,
at 65. He recalled that either Scott or Bruce Brendlin had
dropped out of parole supervision and asked Brendlin to
identify himself.1 Brokenbrough returned to his cruiser,
called for backup, and verified that Brendlin was a parole
violator with an outstanding no-bail warrant for his ar
rest. While he was in the patrol car, Brokenbrough saw
Brendlin briefly open and then close the passenger door of
the Buick. Once reinforcements arrived, Brokenbrough
went to the passenger side of the Buick, ordered him out of
the car at gunpoint, and declared him under arrest. When
the police searched Brendlin incident to arrest, they found
an orange syringe cap on his person. A patdown search of
Simeroth revealed syringes and a plastic bag of a green
leafy substance, and she was also formally arrested.
Officers then searched the car and found tubing, a scale,
and other things used to produce methamphetamine.
  Brendlin was charged with possession and manufacture
of methamphetamine, and he moved to suppress the evi
dence obtained in the searches of his person and the car as
fruits of an unconstitutional seizure, arguing that the
officers lacked probable cause or reasonable suspicion to
make the traffic stop. He did not assert that his Fourth
Amendment rights were violated by the search of Si
meroth’s vehicle, cf. Rakas v. Illinois, 439 U. S. 128 (1978),
but claimed only that the traffic stop was an unlawful
seizure of his person. The trial court denied the suppres
sion motion after finding that the stop was lawful and
Brendlin was not seized until Brokenbrough ordered him
out of the car and formally arrested him. Brendlin
——————
  1 The parties dispute the accuracy of the transcript of the suppression

hearing and disagree as to whether Brendlin gave his name or the false
name “Bruce Brown.” App. 115.
                      Cite as: 551 U. S. ____ (2007)                       3

                           Opinion of the Court

pleaded guilty, subject to appeal on the suppression issue,
and was sentenced to four years in prison.
   The California Court of Appeal reversed the denial of
the suppression motion, holding that Brendlin was seized
by the traffic stop, which they held unlawful. 8 Cal. Rptr.
3d 882 (2004) (officially depublished). By a narrow major
ity, the Supreme Court of California reversed. The State
Supreme Court noted California’s concession that the
officers had no reasonable basis to suspect unlawful opera
tion of the car, 38 Cal. 4th 1107, 1114, 136 P. 3d 845, 848
(2006),2 but still held suppression unwarranted because a
passenger “is not seized as a constitutional matter in the
absence of additional circumstances that would indicate to
a reasonable person that he or she was the subject of the
peace officer’s investigation or show of authority,” id., at
1111, 136 P. 3d, at 846. The court reasoned that Brendlin
was not seized by the traffic stop because Simeroth was its
exclusive target, id., at 1118, 136 P. 3d, at 851, that a
passenger cannot submit to an officer’s show of authority
while the driver controls the car, id., at 1118–1119, 135
P. 3d, at 851–852, and that once a car has been pulled off
the road, a passenger “would feel free to depart or other
wise to conduct his or her affairs as though the police were
not present,” id., at 1119, 136 P. 3d, at 852. In dissent,
Justice Corrigan said that a traffic stop entails the seizure
of a passenger even when the driver is the sole target of
police investigation because a passenger is detained for
the purpose of ensuring an officer’s safety and would not
feel free to leave the car without the officer’s permission.
Id., at 1125, 136 P. 3d, at 856.
   We granted certiorari to decide whether a traffic stop
——————
  2 California conceded that the police officers lacked reasonable suspi

cion to justify the traffic stop because a “ ‘vehicle with an application for
renewal of expired registration would be expected to have a temporary
operating permit.’ ” 38 Cal. 4th, at 1114, 136 P. 3d, at 848 (quoting
Brief for Respondent California in No. S123133 (Sup. Ct. Cal.), p. 24).
4                BRENDLIN v. CALIFORNIA

                     Opinion of the Court

subjects a passenger, as well as the driver, to Fourth
Amendment seizure, 549 U. S. __ (2007). We now vacate.
                              II 

                              A

   A person is seized by the police and thus entitled to
challenge the government’s action under the Fourth
Amendment when the officer, “ ‘by means of physical force
or show of authority,’ ” terminates or restrains his freedom
of movement, Florida v. Bostick, 501 U. S. 429, 434 (1991)
(quoting Terry v. Ohio, 392 U. S. 1, 19, n. 16 (1968)),
“through means intentionally applied,” Brower v. County
of Inyo, 489 U. S. 593, 597 (1989) (emphasis in original).
Thus, an “unintended person . . . [may be] the object of the
detention,” so long as the detention is “willful” and not
merely the consequence of “an unknowing act.” Id., at
596; cf. County of Sacramento v. Lewis, 523 U. S. 833, 844
(1998) (no seizure where a police officer accidentally
struck and killed a motorcycle passenger during a high-
speed pursuit). A police officer may make a seizure by a
show of authority and without the use of physical force,
but there is no seizure without actual submission; other
wise, there is at most an attempted seizure, so far as the
Fourth Amendment is concerned. See California v. Ho
dari D., 499 U. S. 621, 626, n. 2 (1991); Lewis, supra, at
844, 845, n. 7.
   When the actions of the police do not show an unambi
guous intent to restrain or when an individual’s submis
sion to a show of governmental authority takes the form of
passive acquiescence, there needs to be some test for
telling when a seizure occurs in response to authority, and
when it does not. The test was devised by Justice Stewart
in United States v. Mendenhall, 446 U. S. 544 (1980), who
wrote that a seizure occurs if “in view of all of the circum
stances surrounding the incident, a reasonable person
would have believed that he was not free to leave,” id., at
                 Cite as: 551 U. S. ____ (2007)            5

                     Opinion of the Court

554 (principal opinion). Later on, the Court adopted Jus
tice Stewart’s touchstone, see, e.g., Hodari D., supra, at
627; Michigan v. Chesternut, 486 U. S. 567, 573 (1988);
INS v. Delgado, 466 U. S. 210, 215 (1984), but added that
when a person “has no desire to leave” for reasons unre
lated to the police presence, the “coercive effect of the
encounter” can be measured better by asking whether “a
reasonable person would feel free to decline the officers’
requests or otherwise terminate the encounter,” Bostick,
supra, at 435–436; see also United States v. Drayton, 536
U. S. 194, 202 (2002).
   The law is settled that in Fourth Amendment terms a
traffic stop entails a seizure of the driver “even though the
purpose of the stop is limited and the resulting detention
quite brief.” Delaware v. Prouse, 440 U. S. 648, 653
(1979); see also Whren v. United States, 517 U. S. 806,
809–810 (1996). And although we have not, until today,
squarely answered the question whether a passenger is
also seized, we have said over and over in dicta that dur
ing a traffic stop an officer seizes everyone in the vehicle,
not just the driver. See, e.g., Prouse, supra, at 653
(“[S]topping an automobile and detaining its occupants
constitute a ‘seizure’ within the meaning of [the Fourth
and Fourteenth] Amendments”); Colorado v. Bannister,
449 U. S. 1, 4, n. 3 (1980) (per curiam) (“There can be no
question that the stopping of a vehicle and the detention of
its occupants constitute a ‘seizure’ within the meaning of
the Fourth Amendment”); Berkemer v. McCarty, 468 U. S.
420, 436–437 (1984) (“[W]e have long acknowledged that
stopping an automobile and detaining its occupants consti
tute a seizure” (internal quotation marks omitted)); United
States v. Hensley, 469 U. S. 221, 226 (1985) (“[S]topping a
car and detaining its occupants constitute a seizure”);
Whren, supra, at 809–810 (“Temporary detention of indi
viduals during the stop of an automobile by the police,
even if only for a brief period and for a limited purpose,
6                BRENDLIN v. CALIFORNIA

                     Opinion of the Court

constitutes a ‘seizure’ of ‘persons’ within the meaning of
[the Fourth Amendment]”).
  We have come closest to the question here in two cases
dealing with unlawful seizure of a passenger, and neither
time did we indicate any distinction between driver and
passenger that would affect the Fourth Amendment
analysis. Delaware v. Prouse considered grounds for
stopping a car on the road and held that Prouse’s suppres
sion motion was properly granted. We spoke of the arrest
ing officer’s testimony that Prouse was in the back seat
when the car was pulled over, see 440 U. S., at 650, n. 1,
described Prouse as an occupant, not as the driver, and
referred to the car’s “occupants” as being seized, id., at
653. Justification for stopping a car was the issue again in
Whren v. United States, where we passed upon a Fourth
Amendment challenge by two petitioners who moved to
suppress drug evidence found during the course of a traffic
stop. See 517 U. S., at 809. Both driver and passenger
claimed to have been seized illegally when the police
stopped the car; we agreed and held suppression unwar
ranted only because the stop rested on probable cause.
Id., at 809–810, 819.
                              B
  The State concedes that the police had no adequate
justification to pull the car over, see n. 2, supra, but ar
gues that the passenger was not seized and thus cannot
claim that the evidence was tainted by an unconstitutional
stop. We resolve this question by asking whether a rea
sonable person in Brendlin’s position when the car stopped
would have believed himself free to “terminate the en
counter” between the police and himself. Bostick, supra,
at 436. We think that in these circumstances any reason
able passenger would have understood the police officers
to be exercising control to the point that no one in the car
was free to depart without police permission.
                      Cite as: 551 U. S. ____ (2007)                     7

                          Opinion of the Court

   A traffic stop necessarily curtails the travel a passenger
has chosen just as much as it halts the driver, diverting
both from the stream of traffic to the side of the road, and
the police activity that normally amounts to intrusion on
“privacy and personal security” does not normally (and did
not here) distinguish between passenger and driver.
United States v. Martinez-Fuerte, 428 U. S. 543, 554
(1976). An officer who orders one particular car to pull
over acts with an implicit claim of right based on fault of
some sort, and a sensible person would not expect a police
officer to allow people to come and go freely from the
physical focal point of an investigation into faulty behavior
or wrongdoing. If the likely wrongdoing is not the driving,
the passenger will reasonably feel subject to suspicion
owing to close association; but even when the wrongdoing
is only bad driving, the passenger will expect to be subject
to some scrutiny, and his attempt to leave the scene would
be so obviously likely to prompt an objection from the
officer that no passenger would feel free to leave in the
first place. Cf. Drayton, supra, at 197–199, 203–204 (find
ing no seizure when police officers boarded a stationary
bus and asked passengers for permission to search for
drugs).3
   It is also reasonable for passengers to expect that a
police officer at the scene of a crime, arrest, or investiga
tion will not let people move around in ways that could
jeopardize his safety. In Maryland v. Wilson, 519 U. S.
408 (1997), we held that during a lawful traffic stop an
officer may order a passenger out of the car as a precau
——————
   3 Of course, police may also stop a car solely to investigate a passen

ger’s conduct. See, e.g., United States v. Rodriguez-Diaz, 161 F. Supp.
2d 627, 629, n. 1 (Md. 2001) (passenger’s violation of local seatbelt law);
People v. Roth, 85 P. 3d 571, 573 (Colo. App. 2003) (passenger’s viola
tion of littering ordinance). Accordingly, a passenger cannot assume,
merely from the fact of a traffic stop, that the driver’s conduct is the
cause of the stop.
8                    BRENDLIN v. CALIFORNIA

                         Opinion of the Court

tionary measure, without reasonable suspicion that the
passenger poses a safety risk. Id., at 414–415; cf. Pennsyl
vania v. Mimms, 434 U. S. 106 (1977) (per curiam) (driver
may be ordered out of the car as a matter of course). In
fashioning this rule, we invoked our earlier statement that
“ ‘[t]he risk of harm to both the police and the occupants is
minimized if the officers routinely exercise unquestioned
command of the situation.’ ” Wilson, supra, at 414 (quot
ing Michigan v. Summers, 452 U. S. 692, 702–703 (1981)).
What we have said in these opinions probably reflects a
societal expectation of “ ‘unquestioned [police] command’ ”
at odds with any notion that a passenger would feel free to
leave, or to terminate the personal encounter any other
way, without advance permission. Wilson, supra, at 414.4
    Our conclusion comports with the views of all nine
Federal Courts of Appeals, and nearly every state court, to
have ruled on the question. See United States v. Kimball,
25 F. 3d 1, 5 (CA1 1994); United States v. Mosley, 454
F. 3d 249, 253 (CA3 2006); United States v. Rusher, 966
F. 2d 868, 874, n. 4 (CA4 1992); United States v. Grant,
349 F. 3d 192, 196 (CA5 2003); United States v. Perez, 440
F. 3d 363, 369 (CA6 2006); United States v. Powell, 929
F. 2d 1190, 1195 (CA7 1991); United States v. Ameling,
328 F. 3d 443, 446–447, n. 3 (CA8 2003); United States v.
Twilley, 222 F. 3d 1092, 1095 (CA9 2000); United States v.
Eylicio-Montoya, 70 F. 3d 1158, 1163–1164 (CA10 1995);
State v. Bowers, 334 Ark. 447, 451–452, 976 S. W. 2d 379,
381–382 (1998); State v. Haworth, 106 Idaho 405, 405–
406, 679 P. 2d 1123, 1123–1124 (1984); People v. Bunch,
——————
   4 Although the State Supreme Court inferred from Brendlin’s decision

to open and close the passenger door during the traffic stop that he was
“awar[e] of the available options,” 38 Cal. 4th 1107, 1120, 136 P. 3d
845, 852 (2006), this conduct could equally be taken to indicate that
Brendlin felt compelled to remain inside the car. In any event, the test
is not what Brendlin felt but what a reasonable passenger would have
understood.
                    Cite as: 551 U. S. ____ (2007)                  9

                        Opinion of the Court

207 Ill. 2d 7, 13, 796 N. E. 2d 1024, 1029 (2003); State v.
Eis, 348 N. W. 2d 224, 226 (Iowa 1984); State v. Hodges,
252 Kan. 989, 1002–1005, 851 P. 2d 352, 361–362 (1993);
State v. Carter, 69 Ohio St. 3d 57, 63, 630 N. E. 2d 355,
360 (1994) (per curiam); State v. Harris, 206 Wis. 2d 243,
253–258, 557 N. W. 2d 245, 249–251 (1996). And the
treatise writers share this prevailing judicial view that a
passenger may bring a Fourth Amendment challenge to
the legality of a traffic stop. See, e.g., 6 W. LaFave, Search
and Seizure §11.3(e), pp. 194, 195, and n. 277 (4th ed.
2004 and Supp. 2007) (“If either the stopping of the car,
the length of the passenger’s detention thereafter, or the
passenger’s removal from it are unreasonable in a Fourth
Amendment sense, then surely the passenger has stand
ing to object to those constitutional violations and to have
suppressed any evidence found in the car which is their
fruit” (footnote omitted)); 1 W. Ringel, Searches & Sei
zures, Arrests and Confessions §11:20, p. 11–98 (2d ed.
2007) (“[A] law enforcement officer’s stop of an automobile
results in a seizure of both the driver and the passenger”).5
                             C
   The contrary conclusion drawn by the Supreme Court of
California, that seizure came only with formal arrest,
reflects three premises as to which we respectfully dis
agree. First, the State Supreme Court reasoned that
Brendlin was not seized by the stop because Deputy Sher
iff Brokenbrough only intended to investigate Simeroth
and did not direct a show of authority toward Brendlin.
The court saw Brokenbrough’s “flashing lights [as] di
rected at the driver,” and pointed to the lack of record
evidence that Brokenbrough “was even aware [Brendlin]
——————
  5 Only two State Supreme Courts, other than California’s, have stood
against this tide of authority. See People v. Jackson, 39 P. 3d 1174,
1184–1186 (Colo. 2002) (en banc); State v. Mendez, 137 Wash. 2d 208,
222–223, 970 P. 2d 722, 729 (1999) (en banc).
10                BRENDLIN v. CALIFORNIA

                     Opinion of the Court

was in the car prior to the vehicle stop.” 38 Cal. 4th, at
1118, 136 P. 3d, at 851. But that view of the facts ignores
the objective Mendenhall test of what a reasonable pas
senger would understand. To the extent that there is
anything ambiguous in the show of force (was it fairly seen
as directed only at the driver or at the car and its occu
pants?), the test resolves the ambiguity, and here it leads
to the intuitive conclusion that all the occupants were
subject to like control by the successful display of author
ity. The State Supreme Court’s approach, on the contrary,
shifts the issue from the intent of the police as objectively
manifested to the motive of the police for taking the inten
tional action to stop the car, and we have repeatedly re
jected attempts to introduce this kind of subjectivity into
Fourth Amendment analysis. See, e.g., Whren, 517 U. S.,
at 813 (“Subjective intentions play no role in ordinary,
probable-cause Fourth Amendment analysis”); Chesternut,
486 U. S., at 575, n. 7 (“[T]he subjective intent of the
officers is relevant to an assessment of the Fourth
Amendment implications of police conduct only to the
extent that that intent has been conveyed to the person
confronted”); Mendenhall, 446 U. S., at 554, n. 6 (principal
opinion) (disregarding a Government agent’s subjective
intent to detain Mendenhall); cf. Rakas, 439 U. S., at 132–
135 (rejecting the “target theory” of Fourth Amendment
standing, which would have allowed “any criminal defen
dant at whom a search was directed” to challenge the
legality of the search (internal quotation marks omitted)).
   California defends the State Supreme Court’s ruling on
this point by citing our cases holding that seizure requires
a purposeful, deliberate act of detention. See Brief for
Respondent 9–14. But Chesternut, supra, answers that
argument. The intent that counts under the Fourth
Amendment is the “intent [that] has been conveyed to the
person confronted,” id., at 575, n. 7, and the criterion of
willful restriction on freedom of movement is no invitation
                 Cite as: 551 U. S. ____ (2007)          11

                     Opinion of the Court

to look to subjective intent when determining who is
seized. Our most recent cases are in accord on this point.
In Lewis, 523 U. S. 833, we considered whether a seizure
occurred when an officer accidentally ran over a passenger
who had fallen off a motorcycle during a high-speed chase,
and in holding that no seizure took place, we stressed that
the officer stopped Lewis’s movement by accidentally
crashing into him, not “through means intentionally ap
plied.” Id., at 844 (emphasis deleted). We did not even
consider, let alone emphasize, the possibility that the
officer had meant to detain the driver only and not the
passenger. Nor is Brower, 489 U. S. 593, to the contrary,
where it was dispositive that “Brower was meant to be
stopped by the physical obstacle of the roadblock—and
that he was so stopped.” Id., at 599. California reads this
language to suggest that for a specific occupant of the car
to be seized he must be the motivating target of an offi
cer’s show of authority, see Brief for Respondent 12, as if
the thrust of our observation were that Brower, and not
someone else, was “meant to be stopped.” But our point
was not that Brower alone was the target but that officers
detained him “through means intentionally applied”; if the
car had had another occupant, it would have made sense
to hold that he too had been seized when the car collided
with the roadblock. Neither case, then, is at odds with our
holding that the issue is whether a reasonable passenger
would have perceived that the show of authority was at
least partly directed at him, and that he was thus not free
to ignore the police presence and go about his business.
  Second, the Supreme Court of California assumed that
Brendlin, “as the passenger, had no ability to submit to
the deputy’s show of authority” because only the driver
was in control of the moving vehicle. 38 Cal. 4th, at 1118,
1119, 136 P. 3d, at 852. But what may amount to submis
sion depends on what a person was doing before the show
of authority: a fleeing man is not seized until he is physi
12                   BRENDLIN v. CALIFORNIA

                          Opinion of the Court

cally overpowered, but one sitting in a chair may submit to
authority by not getting up to run away. Here, Brendlin
had no effective way to signal submission while the car
was still moving on the roadway, but once it came to a stop
he could, and apparently did, submit by staying inside.
   Third, the State Supreme Court shied away from the
rule we apply today for fear that it “would encompass even
those motorists following the vehicle subject to the traffic
stop who, by virtue of the original detention, are forced to
slow down and perhaps even come to a halt in order to
accommodate that vehicle’s submission to police author
ity.” Id., at 1120, 136 P. 3d, at 853. But an occupant of a
car who knows that he is stuck in traffic because another
car has been pulled over (like the motorist who can’t even
make out why the road is suddenly clogged) would not
perceive a show of authority as directed at him or his car.
Such incidental restrictions on freedom of movement
would not tend to affect an individual’s “sense of security
and privacy in traveling in an automobile.” Prouse, 440
U. S., at 662. Nor would the consequential blockage call
for a precautionary rule to avoid the kind of “arbitrary and
oppressive interference by [law] enforcement officials with
the privacy and personal security of individuals” that the
Fourth Amendment was intended to limit. Martinez-
Fuerte, 428 U. S., at 554.6
   Indeed, the consequence to worry about would not flow
from our conclusion, but from the rule that almost all
courts have rejected. Holding that the passenger in a
——————
   6 California claims that, under today’s rule, “all taxi cab and bus pas

sengers would be ‘seized’ under the Fourth Amendment when the cab
or bus driver is pulled over by the police for running a red light.” Brief
for Respondent 23. But the relationship between driver and passenger
is not the same in a common carrier as it is in a private vehicle, and the
expectations of police officers and passengers differ accordingly. In
those cases, as here, the crucial question would be whether a reason
able person in the passenger’s position would feel free to take steps to
terminate the encounter.
                    Cite as: 551 U. S. ____ (2007)                  13

                         Opinion of the Court

private car is not (without more) seized in a traffic stop
would invite police officers to stop cars with passengers
regardless of probable cause or reasonable suspicion of
anything illegal.7 The fact that evidence uncovered as a
result of an arbitrary traffic stop would still be admissible
against any passengers would be a powerful incentive to
run the kind of “roving patrols” that would still violate the
driver’s Fourth Amendment right. See, e.g., Almeida-
Sanchez v. United States, 413 U. S. 266, 273 (1973) (stop
and search by Border Patrol agents without a warrant or
probable cause violated the Fourth Amendment); Prouse,
supra, at 663 (police spot check of driver’s license and
registration without reasonable suspicion violated the
Fourth Amendment).
                        *    *     *
  Brendlin was seized from the moment Simeroth’s car
came to a halt on the side of the road, and it was error to
deny his suppression motion on the ground that seizure
occurred only at the formal arrest. It will be for the state
courts to consider in the first instance whether suppres
sion turns on any other issue. The judgment of the Su
preme Court of California is vacated, and the case is re
manded for further proceedings not inconsistent with this
opinion.
                                            It is so ordered.



——————
  7 Compare Delaware v. Prouse, 440 U. S. 648, 663 (1979) (requiring

“at least articulable and reasonable suspicion” to support random,
investigative traffic stops), and United States v. Brignoni-Ponce, 422
U. S. 873, 880–884 (1975) (same), with Whren v. United States, 517
U. S. 806, 810 (1996) (“[T]he decision to stop an automobile is reason
able where the police have probable cause to believe that a traffic
violation has occurred”), and Atwater v. Lago Vista, 532 U. S. 318, 354
(2001) (“If an officer has probable cause to believe that an individual
has committed even a very minor criminal offense in his presence, he
may, without violating the Fourth Amendment, arrest the offender”).

```

---
